# オンライン睡眠クリニック（プロジェクト・フォルダ案内）

**更新日**：2026-05-09  

このフォルダは、オンライン睡眠診療の**戦略・文献・ブログ下書き・バックログ**を一元管理するためのものです。公開サイトの実体はリポジトリ直下の **`blog-site/`**（Astro）。

---

## まず読むもの（優先順）

| 文書 | 内容 |
|---|---|
| [`three_pillars_strategy.md`](three_pillars_strategy.md) | 三本柱・裾野と睡眠オンラインを芯に置く理由（**§0**）・法務チェックリスト |
| [`blog_articles_backlog_50.md`](blog_articles_backlog_50.md) | 睡眠ブログ**コア50本＋拡張**（例：**#51〜** 内科×睡眠）・**`#`＝投稿順**・下書きファイル名と対応 |
| [`literature_content_map.md`](literature_content_map.md) | ローカルPDFと記事論点のマッピング（§7.1＝トリビアと下書き） |
| [`drafts/README.md`](drafts/README.md) | 下書きの置き場・執筆の型・睡眠／男性／女性の一覧 |

補助：`plan.md`（開業手順のチェックリスト）、`social_posts_draft_20.md`（X/note 骨子）。

---

## 番号ルール（混同防止）

- **`blog_articles_backlog_50.md` の `#`**  
  **投稿順**です。`drafts/sleep/draft_blog_<#>_*.md` の **ファイル名の数字**と一致させます（例：#4 → `draft_blog_04_cbti_intro.md`）。  
  同ファイルの一覧表にある **柱（英字）** は **A睡眠一般〜F他科×睡眠** で統一されています。**旧番号**（再採番前の 13・43 など）を参照する資料は、Git 履歴を見てください。

- **男性・女性の下書き**（`drafts/male/`・`drafts/female/`）  
  それぞれ **`blog_backlog_male_menopause_30.md`** / **`blog_backlog_female_menopause_30.md`** の番号です。**睡眠50本の `#` とは別系列**です。

---

## フォルダ構成（抜粋）

```
オンライン睡眠クリニック/
├── README.md                    ← 本ファイル
├── three_pillars_strategy.md
├── plan.md
├── blog_articles_backlog_50.md
├── blog_backlog_male_menopause_30.md
├── blog_backlog_female_menopause_30.md
├── literature_content_map.md
├── social_posts_draft_20.md
└── drafts/
    ├── README.md
    ├── sleep/                   ← 柱① 睡眠（ファイル名＝バックログ投稿順 #）
    ├── male/
    └── female/
```

公開ビルド：`../../blog-site/src/content/blog/`（宣言2本は既にコピー済みの例あり）。

---

## 関連（リポジトリ外のメモ）

- 文献PDF：`Desktop/睡眠/精神医学` 等（`literature_content_map.md` 冒頭に記載）
- 親ディレクトリの `経営/ブログ・コンテンツ/strategy.md` はサイト全体の技術・SEO方針
