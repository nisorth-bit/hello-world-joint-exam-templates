# CLAUDE.md

## 基本方針
- トークン節約を優先する。
- 必要最小限のファイルだけ読む。
- 変更前に、変更予定ファイルと作業方針を簡潔に説明する。
- ユーザー確認前にファイルを編集しない。
- 長い説明を避け、要点だけ答える。

## 読まないもの
- node_modules / dist / build / .next / coverage / .astro
- .env・秘密情報・認証情報を含むファイル

## ブログ作成ルール
- 既存記事を全部読まない。必要な記事・テンプレート・READMEだけ確認する。
- まず構成案を出す。本文作成前に対象読者を確認する。
- 医学情報は断定しすぎず、必要に応じて受診を促す。

## 作業ルール
- まず計画だけ出す。編集は許可後に行う。
- 変更後は変更ファイル一覧と要点を示す。
- 長い作業になったら /compact を提案する。

## プロジェクト情報

### 開発コマンド
```bash
cd blog-site
npm run dev      # ローカル開発サーバー
npm run build    # ビルド＝テスト（frontmatter検証含む）
npm run preview  # プレビュー
```
`npm test` は存在しない。

### frontmatter 必須フィールド
```yaml
title: string
description: string
pubDate: date
```
任意: `updatedDate`, `heroImage`

### 編集禁止ファイル
- `.cursor/` 配下
- `watch_and_sync.py`（Notion同期）
- `blog-site/package-lock.json`
- `astro.config.mjs` の `site` フィールド
- `about.astro` の氏名・所属
- `Footer.astro` の著作権表示
- `privacy.astro` / `disclaimer.astro`
- 既存の医療・健康情報・事業計画の本文

### Notion同期
原稿編集前に `watch_and_sync.py` が動作中でないか確認する。

### 本番デプロイ条件
睡眠・男性更年期・女性更年期の三本柱が揃うまでデプロイしない。
デプロイ時は `astro.config.mjs` の `site` を本番URLに変更する。

### 記事の置き場
- 公開記事: `blog-site/src/content/blog/*.md`
- 下書き: `オンラインクリニック/content/drafts/sleep|male|female/`
- 下書き→公開の移動は明示的な指示があるまで行わない。

### オンラインクリニックフォルダ構成
```
オンラインクリニック/
├── README.md
├── strategy/          戦略文書（platform_strategy.md）
├── content/
│   ├── backlogs/      記事バックログ（睡眠73本・男性40本・女性40本）
│   └── drafts/        原稿下書き（sleep/ male/ female/）
├── phase1_mvp/        LP設計・プラットフォーム比較・問診フォーム
├── phase2_crm/        CRM・フォローアップ・サブスク設計
└── phase3_future/     将来内製化要件
```
