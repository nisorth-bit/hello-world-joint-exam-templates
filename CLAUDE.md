# CLAUDE.md

## プロジェクト概要

整形外科・睡眠・更年期前後の健康情報発信リポジトリ。
Astro 製ブログ (`blog-site/`) と、非公開の原稿・事業計画 (`経営/`・`整形外科臨床/`) を含む。

## 開発コマンド

```bash
cd blog-site
npm install      # 初回のみ（Node.js >= 22.12.0）
npm run dev      # ローカル開発サーバー起動
npm run build    # ビルド確認 ＝ 実質テスト（frontmatter 検証含む）
npm run preview  # ビルド成果物のプレビュー
```

`npm test` は存在しない。`npm run build` が通ればOK。

## 記事の追加・編集

- **公開記事**: `blog-site/src/content/blog/*.md`
- **下書き**: `経営/オンライン睡眠クリニック/drafts/sleep|male|female/`
- 下書き → 公開記事への移動は、ユーザーの明示的な指示があるまで行わない。

frontmatter 必須フィールド（`npm run build` でスキーマ検証される）:

```yaml
title: string
description: string
pubDate: date
```

任意: `updatedDate`, `heroImage`

## 編集してはいけないファイル

明示的な指示なしに変更しない:

- `.cursor/` 配下のすべてのファイル
- `watch_and_sync.py`（Notion 同期スクリプト）
- `blog-site/package-lock.json`
- `blog-site/astro.config.mjs` の `site` フィールド（現在 `https://example.com`）
- 既存の医療・健康情報の本文
- 既存の事業計画・開業計画の本文
- `blog-site/src/pages/about.astro` の氏名・所属
- `blog-site/src/components/Footer.astro` の著作権表示
- `blog-site/src/pages/privacy.astro`
- `blog-site/src/pages/disclaimer.astro`

直接編集しない生成物: `node_modules/`, `dist/`, `.astro/`

## Notion 同期への注意

Markdown ファイルを編集すると `watch_and_sync.py` 経由で Notion に同期が走る可能性がある。
原稿を編集する前にこのスクリプトが動作中でないか確認する。

## 本番デプロイ前の条件

睡眠・男性更年期・女性更年期の三本柱の核記事が揃うまでデプロイしない方針。
デプロイ時には以下を確認する:

- `astro.config.mjs` の `site` を本番 URL に変更（OGP・canonical・sitemap に使用）
- `about.astro` の氏名・所属
- `Footer.astro` の著作権表示
- `privacy.astro`, `disclaimer.astro` の実情確認

## 作業原則

- 関連ファイルを読んでから変更する。
- 変更前に何をどこに変更するか簡潔に説明し、確認を取る。
- 既存の Astro 構成・content collection・コンポーネント構成に合わせる。
- 不要な依存関係・大きな設計変更を追加しない。
- 医療情報は断定的な診断・治療表現を避け、一般情報と受診目安の範囲に留める。
