#!/usr/bin/env python3
"""
Sync a local Markdown file to its corresponding Notion page.
Usage: python3 sync_to_notion.py <file_path>
"""

import sys
import os
import json
import urllib.request
import urllib.error
import re
import time

WORKSPACE = "/Users/naokinishimura/Desktop/整形外科雑誌/hello-world"
MAP_FILE  = os.path.join(WORKSPACE, ".cursor", "notion-page-map.json")
API_BASE  = "https://api.notion.com/v1"


def _load_token() -> str:
    """Read Notion token from ~/.cursor/mcp.json or NOTION_TOKEN env var."""
    token = os.environ.get("NOTION_TOKEN")
    if token:
        return token
    mcp_path = os.path.expanduser("~/.cursor/mcp.json")
    try:
        with open(mcp_path) as f:
            mcp = json.load(f)
        servers = mcp.get("mcpServers", {})
        for server in servers.values():
            env = server.get("env", {})
            for key, val in env.items():
                if "notion" in key.lower() and isinstance(val, str) and val.startswith("ntn_"):
                    return val
    except Exception:
        pass
    raise RuntimeError("Notion token not found. Set NOTION_TOKEN env var or configure ~/.cursor/mcp.json")


TOKEN = _load_token()
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}


def notion_request(method: str, path: str, body=None):
    url = f"{API_BASE}{path}"
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read())
    except urllib.error.HTTPError as e:
        msg = e.read().decode()
        print(f"[notion] {method} {path} -> {e.code}: {msg}", file=sys.stderr)
        return None


def md_to_blocks(text: str) -> list:
    """Convert Markdown text to Notion block objects (basic)."""
    blocks = []
    for line in text.splitlines():
        stripped = line.rstrip()
        if stripped.startswith("### "):
            content = stripped[4:]
            btype = "heading_3"
        elif stripped.startswith("## "):
            content = stripped[3:]
            btype = "heading_2"
        elif stripped.startswith("# "):
            content = stripped[2:]
            btype = "heading_1"
        elif re.match(r"^[-*] ", stripped):
            content = stripped[2:]
            btype = "bulleted_list_item"
        elif re.match(r"^\d+\. ", stripped):
            content = re.sub(r"^\d+\. ", "", stripped)
            btype = "numbered_list_item"
        else:
            content = stripped
            btype = "paragraph"

        rich_text = [{"type": "text", "text": {"content": content}}] if content else []
        blocks.append({"type": btype, btype: {"rich_text": rich_text}})
    return blocks


def clear_page_children(page_id: str):
    """Delete all existing blocks in a page."""
    start_cursor = None
    while True:
        path = f"/blocks/{page_id}/children"
        if start_cursor:
            path += f"?start_cursor={start_cursor}"
        result = notion_request("GET", path)
        if not result:
            break
        for block in result.get("results", []):
            notion_request("DELETE", f"/blocks/{block['id']}")
        if not result.get("has_more"):
            break
        start_cursor = result.get("next_cursor")
        time.sleep(0.3)


def append_blocks(page_id: str, blocks: list):
    """Append blocks in batches of 100 (Notion API limit)."""
    batch_size = 100
    for i in range(0, len(blocks), batch_size):
        batch = blocks[i:i + batch_size]
        result = notion_request(
            "PATCH",
            f"/blocks/{page_id}/children",
            {"children": batch},
        )
        if not result:
            print(f"[notion] Failed to append batch {i//batch_size + 1}", file=sys.stderr)
        time.sleep(0.3)


def sync_file(file_path: str):
    # Resolve relative path against workspace root
    abs_path = os.path.realpath(file_path)
    try:
        rel_path = os.path.relpath(abs_path, WORKSPACE)
    except ValueError:
        print(f"[notion] File is outside workspace: {file_path}", file=sys.stderr)
        return

    with open(MAP_FILE) as f:
        page_map = json.load(f)

    page_id = page_map.get(rel_path)
    if not page_id:
        print(f"[notion] No Notion page mapped for: {rel_path}")
        return

    print(f"[notion] Syncing {rel_path} -> {page_id}")

    try:
        with open(abs_path, encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"[notion] File not found: {abs_path}", file=sys.stderr)
        return

    blocks = md_to_blocks(content)
    clear_page_children(page_id)
    append_blocks(page_id, blocks)
    print(f"[notion] Sync complete: {rel_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: sync_to_notion.py <file_path>", file=sys.stderr)
        sys.exit(1)
    sync_file(sys.argv[1])
