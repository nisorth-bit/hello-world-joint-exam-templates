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

## 手術記事作成ルール

ユーザーが手術メモ・術式情報を貼った場合、確認なしに以下のフローで即実行する。

### 実行フロー
1. mdファイル作成
2. Notion ページ作成（curl）
3. notion-page-map.json に追記
4. sync_to_notion.py で同期
5. git add → git commit（hookがNotion自動登録を処理）

### ファイル配置
- 保存先: `整形外科臨床/手術計画・記事/upper_limb/` or `lower_limb/`
- サブフォルダ: `humerus/` `forearm/` `wrist/` `hand/` `clavicle/` `fractures/` など解剖部位で分類
- ファイル名: `{side}_{anatomy}_{diagnosis}_{procedure}.md`（スネークケース英語）

### 必須セクション（この順番で）
1. `# 部位・診断名 手術計画・記録`
2. `## 術式名`
3. サマリー表（診断・術式・アプローチ・インプラント・術者・麻酔・体位・出血・特記）
4. 術前計画（病態・分類表 / インプラント原理・他術式との比較表 / 注意すべき構造表）
5. 手術手順（Step 1〜N、各ステップに注意事項 blockquote）
6. 術後方針表
7. Pitfall（番号付きリスト、参考文献番号付き）
8. カンファレンス用まとめ（1段落）
9. 紹介状用まとめ（短縮版、1段落）
10. 参考文献（`[^N]:` 脚注形式、PMC/PubMed URL付き）

### Notion 親ページID
- upper_limb: `35165fad-9a7d-8114-805d-f0673560a91a`
- lower_limb: `35165fad-9a7d-8144-bc1a-fde2952a9450`

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
