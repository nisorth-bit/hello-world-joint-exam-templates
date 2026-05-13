# AGENTS.md

## プロジェクト概要

このリポジトリは、整形外科・睡眠・更年期前後の健康情報発信に関する原稿、事業計画、臨床メモ、および Astro 製ブログサイトを含む作業リポジトリです。

主な構成:

- `blog-site/`: Astro + Markdown の公開用ブログサイト
- `経営/`: 開業計画、オンライン睡眠クリニック、マーケティング、財務、記事原稿など
- `整形外科臨床/`: 診察テンプレート、手術計画・記事など
- `.cursor/`: Markdown と Notion の同期設定・スクリプト
- `watch_and_sync.py`: Markdown 変更を監視して Notion に同期するスクリプト

## 基本ルール

- ユーザーから明示されるまで、既存ファイルを変更しない。
- 医療・健康情報の本文は、内容の正確性と表現リスクが高いため、勝手に書き換えない。
- 既存の方針・文体・構成を優先し、大きなリライトや再設計は事前に確認する。
- Markdown 原稿を編集する場合、Notion 同期が走る可能性に注意する。
- `.cursor/` 配下の同期設定や Notion 関連ファイルは、明示的な依頼なしに変更しない。

## Astro サイト

Astro サイトは `blog-site/` にある。

起動:

```bash
cd blog-site
npm install
npm run dev
```

ビルド確認:

```bash
cd blog-site
npm run build
```

プレビュー:

```bash
cd blog-site
npm run preview
```

Node.js は `>=22.12.0` が前提。

## 記事追加・編集

公開記事は `blog-site/src/content/blog/` に置く。

記事 Markdown の frontmatter には以下が必要:

- `title`
- `description`
- `pubDate`

任意項目:

- `updatedDate`
- `heroImage`

非公開の下書きは主に以下に置かれている:

- `経営/オンライン睡眠クリニック/drafts/sleep/`
- `経営/オンライン睡眠クリニック/drafts/male/`
- `経営/オンライン睡眠クリニック/drafts/female/`

下書きを公開記事へ移す場合は、ユーザーの明示的な指示を待つ。

## テスト・確認

専用の `npm test` はない。

Astro 側の基本確認は以下で行う:

```bash
cd blog-site
npm run build
```

これにより、Astro のビルド、content collection の frontmatter 検証、静的ページ生成を確認する。

## デプロイ注意点

`blog-site/README.md` では、睡眠・男性更年期・女性更年期の核記事が揃うまで本番デプロイしない方針。

本番公開前には以下を確認する:

- `blog-site/astro.config.mjs` の `site`
- `blog-site/src/pages/about.astro` の氏名・所属
- `blog-site/src/components/Footer.astro` の著作権表示
- `blog-site/src/pages/privacy.astro`
- `blog-site/src/pages/disclaimer.astro`

現在 `astro.config.mjs` の `site` は `https://example.com` のため、本番 URL 決定後に変更する。

## 変更してはいけないもの

明示的な依頼なしに変更しない:

- `.cursor/` 配下のファイル
- `.cursor/notion-page-map.json`
- `.cursor/notion-sync.log`
- `watch_and_sync.py`
- 既存の医療・健康情報本文
- 既存の事業計画・開業計画本文
- `blog-site/package-lock.json`
- `blog-site/astro.config.mjs` の `site`
- 公開者情報、免責事項、プライバシーポリシー

直接編集しない生成物:

- `blog-site/node_modules/`
- `blog-site/dist/`
- `blog-site/.astro/`

## 作業方針

- まず関連ファイルを読んでから変更する。
- 変更前に、何をどこに変更するか簡潔に説明する。
- 既存の Astro 構成、content collection、コンポーネント構成に合わせる。
- 不要な依存関係や大きな設計変更を追加しない。
- 医療情報を扱う場合は、断定的な診断・治療表現を避け、一般情報と受診目安の範囲に留める。
