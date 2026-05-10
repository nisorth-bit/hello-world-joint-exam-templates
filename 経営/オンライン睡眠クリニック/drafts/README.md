# ブログ原稿（下書き）

オンライン診療・ブログ向けの **Markdown 原稿**を、この `drafts/` 以下にまとめる。**三本柱ごとにフォルダを分ける**。

| フォルダ | 柱 | 内容の目安 |
|---|---|---|
| **`sleep/`** | ① 睡眠 | `blog_articles_backlog_50.md` 系・痛み×睡眠・CBT-I など |
| **`male/`** | ② 男性更年期 | `blog_backlog_male_menopause_30.md` 系 |
| **`female/`** | ③ 女性更年期 | `blog_backlog_female_menopause_30.md` 系 |

## 置き場のルール

- 新規原稿は **柱に対応するサブフォルダ**へ保存する（`drafts/` 直下にばらまかない）。
- ファイル名の例：`draft_blog_<バックログ番号または題材>_<短いslug>.md`  
  - 男性柱：`male/draft_blog_male_01_loh_intro.md` のように、ファイル名でも柱が分かるとよい。
- **公開用**はリポジトリ直下の `blog-site/src/content/blog/` に同内容の `.md` を置く（Astro がビルド）。
- **柱をまたぐ参照**：別フォルダの原稿へは相対パスで書く（例：`../sleep/draft_blog_44_pain_sleep_intersection.md`）。

## 一覧

### `sleep/`（柱①）

| ファイル | バックログ | 公開コピー（Astro） |
|---|---|---|
| `draft_blog_01_chronic_pain_insomnia.md` | #1 | （未） |
| `draft_blog_13_cbti_intro.md` | #13 | （未） |
| `draft_blog_27_snoring_when_seek.md` | #27 | （未） |
| `draft_blog_33_online_sleep_who.md` | #33 | （未） |
| `draft_blog_43_sleep_declaration.md` | #43 | `blog-site/.../sleep-why-orthopedic-sleep.md` |
| `draft_blog_44_pain_sleep_intersection.md` | #44 | `blog-site/.../sleep-pain-intersection.md` |

### `male/`（柱②）

| ファイル | バックログ | 公開 |
|---|---|---|
| `draft_blog_male_01_loh_intro.md` | #1 | （三本柱そろい後） |
| `draft_blog_male_02_vitality_aging.md` | #2 | （未） |
| `draft_blog_male_03_fatigue_vs_depression.md` | #3 | （未） |
| `draft_blog_male_05_testosterone_basics.md` | #5 | （未） |
| `draft_blog_male_06_testosterone_lab.md` | #6 | （未） |
| `draft_blog_male_07_sleep_aging_men.md` | #7 | （未） |
| `draft_blog_male_08_nocturia_sleep.md` | #8 | （未） |

### `female/`（柱③）

| ファイル | バックログ | 公開 |
|---|---|---|
| `draft_blog_female_01_menopause_intro.md` | #1 | （未） |
| `draft_blog_female_02_perimenopause.md` | #2 | （未） |
| `draft_blog_female_04_sleep_menopause.md` | #4 | （未） |
| `draft_blog_female_06_mood_when_seek_care.md` | #6 | （未） |

**原稿作成時**：本文は **`Desktop/睡眠/精神医学`**、**`Desktop/男性更年期`**（LOHガイドライン含む）、**`Desktop/ホルモン`**（MHT・更年期×睡眠等）のPDFを読み、**自分の言葉で要約**する（本文の転載はしない）。

バックログとの対応は `blog_articles_backlog_50.md` および `blog_backlog_male_menopause_30.md` / `blog_backlog_female_menopause_30.md` を参照。

**連続執筆**：バックログ番号順または `blog_articles_backlog_50.md` の「公開の順番」に沿って足していくとサイト構造が崩れにくい。
