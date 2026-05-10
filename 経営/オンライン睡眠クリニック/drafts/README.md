# ブログ原稿（下書き）

オンライン診療・ブログ向けの **Markdown 原稿をこのフォルダにまとめる**（睡眠・男性更年期・女性更年期などジャンル共通）。

## 置き場のルール

- 新規原稿は **必ずここに保存**する（`オンライン睡眠クリニック/` 直下にばらまかない）。
- ファイル名の例：`draft_blog_<バックログ番号または題材>_<短いslug>.md`  
  - 更年期：`draft_blog_male_01_loh_intro.md` のように、先頭で柱が分かるとよい。
- **公開用**はリポジトリ直下の `blog-site/src/content/blog/` に同内容の `.md` を置く（Astro がビルド）。

## いま入っているもの

| ファイル | 内容 | 公開コピー（Astro） |
|---|---|---|
| `draft_blog_43_sleep_declaration.md` | 宣言（睡眠） | `blog-site/.../sleep-why-orthopedic-sleep.md` |
| `draft_blog_44_pain_sleep_intersection.md` | 痛みと眠りの交差点 | `blog-site/.../sleep-pain-intersection.md` |
| `draft_blog_male_01_loh_intro.md` | 男性更年期・宣言（LOH入門） | （三本柱そろい後に blog-site へ） |
| `draft_blog_female_01_menopause_intro.md` | 女性更年期・宣言（入門） | 同上（`Desktop/男性更年期` 所蔵PDFを要約参照） |

**原稿作成時**：本文は **`Desktop/睡眠/精神医学`** および **`Desktop/男性更年期`** の雑誌PDFを読み、**自分の言葉で要約**する（本文の転載はしない）。

バックログとの対応は `blog_articles_backlog_50.md` および `blog_backlog_male_menopause_30.md` / `blog_backlog_female_menopause_30.md` を参照。
