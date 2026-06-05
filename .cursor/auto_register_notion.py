#!/usr/bin/env python3
"""
auto_register_notion.py
=======================
整形外科臨床/手術計画・記事/ 以下の .md ファイルを自動スキャンし、
notion-page-map.json に未登録のファイルを検出して Notion ページを作成・同期する。

使い方:
  # 一括登録（未登録ファイルを全て処理）
  python3 .cursor/auto_register_notion.py

  # 監視モード（新規ファイルを自動検知、60秒ごとにスキャン）
  python3 .cursor/auto_register_notion.py --watch
"""

import sys
import os
import json
import time
import re
import urllib.request
import urllib.error

WORKSPACE  = "/Users/naokinishimura/Desktop/整形外科雑誌/hello-world"
MAP_FILE   = os.path.join(WORKSPACE, ".cursor", "notion-page-map.json")
SYNC_SCRIPT = os.path.join(WORKSPACE, ".cursor", "sync_to_notion.py")
SCAN_ROOT  = os.path.join(WORKSPACE, "整形外科臨床", "手術計画・記事")
API_BASE   = "https://api.notion.com/v1"
WATCH_INTERVAL = 60  # 秒

# パスパターン → Notion 親ページID のマッピング
# キーは SCAN_ROOT からの相対パスの先頭部分（前方一致）
PARENT_MAP = {
    "upper_limb": "35165fad-9a7d-8114-805d-f0673560a91a",
    "lower_limb": "35165fad-9a7d-8144-bc1a-fde2952a9450",
}
DEFAULT_PARENT = "35165fad-9a7d-8114-805d-f0673560a91a"  # 分類不明時はUpper Limb直下


def _load_token() -> str:
    token = os.environ.get("NOTION_TOKEN")
    if token:
        return token
    mcp_path = os.path.expanduser("~/.cursor/mcp.json")
    try:
        with open(mcp_path) as f:
            mcp = json.load(f)
        headers_str = (mcp.get("mcpServers", {})
                          .get("notion", {})
                          .get("env", {})
                          .get("OPENAPI_MCP_HEADERS", ""))
        if headers_str:
            headers = json.loads(headers_str)
            auth = headers.get("Authorization", "")
            if auth.startswith("Bearer "):
                return auth[7:]
    except Exception:
        pass
    raise RuntimeError("Notion token not found. Set NOTION_TOKEN env var.")


def _api(method: str, path: str, body: dict = None) -> dict:
    token = TOKEN
    url = API_BASE + path
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        msg = e.read().decode()
        raise RuntimeError(f"Notion API {method} {path} -> {e.code}: {msg}")


def load_map() -> dict:
    with open(MAP_FILE) as f:
        return json.load(f)


def save_map(m: dict):
    with open(MAP_FILE, "w") as f:
        json.dump(m, f, ensure_ascii=False, indent=2)


def extract_title(filepath: str) -> str:
    """ファイルの H1 / H2 からタイトルを生成する。"""
    h1, h2 = "", ""
    try:
        with open(filepath, encoding="utf-8") as f:
            for line in f:
                line = line.rstrip()
                if not h1 and line.startswith("# "):
                    h1 = line[2:].strip()
                elif not h2 and line.startswith("## "):
                    h2 = line[3:].strip()
                if h1 and h2:
                    break
    except Exception:
        pass
    if h1 and h2:
        return f"{h1}（{h2}）"
    return h1 or h2 or os.path.basename(filepath).replace(".md", "")


def resolve_parent(rel_path: str) -> str:
    """ファイルの相対パスから Notion 親ページID を決定する。"""
    for prefix, parent_id in PARENT_MAP.items():
        if rel_path.startswith(prefix + "/") or rel_path.startswith(prefix + os.sep):
            return parent_id
    return DEFAULT_PARENT


def scan_unregistered(page_map: dict) -> list:
    """SCAN_ROOT 以下の .md で page_map 未登録のファイルを返す（相対パス）。"""
    unregistered = []
    for root, dirs, files in os.walk(SCAN_ROOT):
        # 不要フォルダを除外
        dirs[:] = [d for d in dirs if d not in ("node_modules", ".git", "__pycache__")]
        for fname in files:
            if not fname.endswith(".md"):
                continue
            abs_path = os.path.join(root, fname)
            rel_path = os.path.relpath(abs_path, WORKSPACE)
            if rel_path not in page_map:
                unregistered.append(rel_path)
    return sorted(unregistered)


def register_file(rel_path: str, page_map: dict) -> bool:
    """
    1. Notion ページを作成
    2. page_map に追記して保存
    3. sync_to_notion.py でコンテンツ同期
    """
    abs_path = os.path.join(WORKSPACE, rel_path)
    title = extract_title(abs_path)
    parent_id = resolve_parent(
        os.path.relpath(abs_path, SCAN_ROOT).replace(os.sep, "/")
    )

    print(f"[auto-register] 新規ファイル検出: {rel_path}")
    print(f"  タイトル : {title}")
    print(f"  親ページ : {parent_id}")

    # Notion ページ作成
    try:
        result = _api("POST", "/pages", {
            "parent": {"page_id": parent_id},
            "properties": {
                "title": {"title": [{"text": {"content": title}}]}
            }
        })
    except RuntimeError as e:
        print(f"  [ERROR] Notion ページ作成失敗: {e}")
        return False

    page_id = result.get("id")
    if not page_id:
        print("  [ERROR] page_id が取得できませんでした")
        return False

    print(f"  Notion page_id: {page_id}")

    # page_map 更新
    page_map[rel_path] = page_id
    save_map(page_map)
    print(f"  page-map 更新完了")

    # コンテンツ同期
    ret = os.system(
        f'NOTION_TOKEN="{TOKEN}" python3 "{SYNC_SCRIPT}" "{rel_path}" 2>&1'
    )
    if ret == 0:
        print(f"  Notion 同期完了")
    else:
        print(f"  [WARN] 同期スクリプトがエラーを返しました (code={ret})")

    return True


def run_once():
    """未登録ファイルを一括処理する。"""
    page_map = load_map()
    unregistered = scan_unregistered(page_map)
    if not unregistered:
        print("[auto-register] 未登録ファイルはありません。")
        return
    print(f"[auto-register] 未登録ファイル {len(unregistered)} 件を処理します。")
    for rel_path in unregistered:
        register_file(rel_path, page_map)
        page_map = load_map()  # 他プロセスの更新を反映
        time.sleep(0.5)
    print("[auto-register] 完了。")


def run_watch():
    """ループでスキャンし続ける監視モード。"""
    print(f"[auto-register] 監視モード開始（{WATCH_INTERVAL}秒ごとにスキャン）")
    print(f"  対象: {SCAN_ROOT}")
    print("  終了: Ctrl+C")
    while True:
        try:
            page_map = load_map()
            unregistered = scan_unregistered(page_map)
            for rel_path in unregistered:
                register_file(rel_path, page_map)
                page_map = load_map()
                time.sleep(0.5)
        except Exception as e:
            print(f"[auto-register] エラー: {e}")
        time.sleep(WATCH_INTERVAL)


if __name__ == "__main__":
    TOKEN = _load_token()
    if "--watch" in sys.argv:
        run_watch()
    else:
        run_once()
