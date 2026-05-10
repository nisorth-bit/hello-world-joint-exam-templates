# ブログ原稿（下書き）

オンライン診療・ブログ向けの **Markdown 原稿をこのフォルダにまとめる**（睡眠・男性更年期・女性更年期などジャンル共通）。

## 置き場のルール

- 新規原稿は **必ずここに保存**する（`オンライン睡眠クリニック/` 直下にばらまかない）。
- ファイル名の例：`draft_blog_<バックログ番号または題材>_<短いslug>.md`  
  - 更年期：`draft_blog_male_01_loh_intro.md` のように、先頭で柱が分かるとよい。
- **公開用**はリポジトリ直下の `blog-site/src/content/blog/` に同内容の `.md` を置く（Astro がビルド）。

## いま入っているもの

### 睡眠（バックログ 50）

| ファイル | 内容 | 公開コピー（Astro） |
|---|---|---|
| `draft_blog_01_chronic_pain_insomnia.md` | #1 慢性痛と不眠 | （未） |
| `draft_blog_13_cbti_intro.md` | #13 CBT-I入門 | （未） |
| `draft_blog_27_snoring_when_seek.md` | #27 いびき・受診目安 | （未） |
| `draft_blog_33_online_sleep_who.md` | #33 オンライン向き・慎重 | （未） |
| `draft_blog_43_sleep_declaration.md` | #43 宣言 | `blog-site/.../sleep-why-orthopedic-sleep.md` |
| `draft_blog_44_pain_sleep_intersection.md` | #44 痛みと眠り | `blog-site/.../sleep-pain-intersection.md` |

### 男性更年期（バックログ 30）

| ファイル | 内容 | 公開 |
|---|---|---|
| `draft_blog_male_01_loh_intro.md` | #1 LOH入門 | （三本柱そろい後） |
| `draft_blog_male_02_vitality_aging.md` | #2 活力低下の目安 | （未） |
| `draft_blog_male_03_fatigue_vs_depression.md` | #3 疲れとうつ | （未） |
| `draft_blog_male_05_testosterone_basics.md` | #5 テストステロン入門 | （未） |
| `draft_blog_male_06_testosterone_lab.md` | #6 検査結果の受け止め | （未） |
| `draft_blog_male_07_sleep_aging_men.md` | #7 睡眠×加齢男性 | （未） |
| `draft_blog_male_08_nocturia_sleep.md` | #8 夜間頻尿と睡眠 | （未） |

### 女性更年期（バックログ 30）

| ファイル | 内容 | 公開 |
|---|---|---|
| `draft_blog_female_01_menopause_intro.md` | #1 入門 | （未） |
| `draft_blog_female_02_perimenopause.md` | #2 ペリメノポーズ | （未） |
| `draft_blog_female_04_sleep_menopause.md` | #4 更年期と睡眠 | （未） |
| `draft_blog_female_06_mood_when_seek_care.md` | #6 気分と受診目安 | （未） |

**原稿作成時**：本文は **`Desktop/睡眠/精神医学`**、**`Desktop/男性更年期`**（LOHガイドライン含む）、**`Desktop/ホルモン`**（MHT・更年期×睡眠等）のPDFを読み、**自分の言葉で要約**する（本文の転載はしない）。

バックログとの対応は `blog_articles_backlog_50.md` および `blog_backlog_male_menopause_30.md` / `blog_backlog_female_menopause_30.md` を参照。

**連続執筆**：バックログ番号順または `blog_articles_backlog_50.md` の「公開の順番」に沿って足していくとサイト構造が崩れにくい。
