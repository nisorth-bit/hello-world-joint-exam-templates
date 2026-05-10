# ブログ原稿（下書き）

オンライン診療・ブログ向けの **Markdown 原稿**を、この `drafts/` 以下にまとめる。**三本柱ごとにフォルダを分ける**。

**番号の意味**：`sleep/` の `draft_blog_<数字>_*.md` の **数字**は、親フォルダの **`blog_articles_backlog_50.md` における投稿順 `#`** と一致します。原稿先頭付近の **`柱` 行**にある英字タグも、`blog_articles_backlog_50.md` の定義（**A睡眠一般〜F他科×睡眠**）と揃えます。`male/`・`female/` のファイル名の数字は、**それぞれ別バックログ**（`blog_backlog_male_menopause_30.md` 等・**M1…／F1…** の柱タグ）用です。**混同しないこと**。全体の案内は [`../README.md`](../README.md)。

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
- **柱をまたぐ参照**：別フォルダの原稿へは相対パスで書く（例：`../sleep/draft_blog_02_pain_sleep_intersection.md`）。

## 執筆の型（全原稿共通）

1. **結論先出し**：本文（公開時にそのまま載せる部分）は、フロントマター直後に **`## 結論（先に）`** で2〜4文。読者が最初の30秒で「自分ごとか／何を持ち帰るか」がわかるようにする。  
2. **読者に原典を読ませない**：雑誌PDF（70のトリビア等）は**執筆者の裏付け**として使い、**知識の中身は記事本文に書く**。「目次を開いてください」といった読者負担の誘導はしない。参考文献・脚注は**信頼性と透明性**のための表記。  
3. **オンライン相談のハードル**：睡眠・更年期は「大げさに行くほどではないが整理したい」層向けに、**用語と受診目安がわかると相談しやすい**旨を結論や末尾で自然に触れてよい（効果保証・医療広告に抵触する表現は避ける。`three_pillars_strategy.md` §3 参照）。  
4. **編集上の定点（裾野と入口）**：記事は**整形外科疾患のある人だけ**に限定して書かない。**オンライン睡眠診療の入り口**として読めるかを毎回意識する。痛み×睡眠は**差別化の接点**。**内科疾患や、重症で睡眠薬中心の管理・専門治療が主役になりうる場合**は、遠隔完結を約束せず**紹介・対面**を本文で明記する（`three_pillars_strategy.md` **§0**）。

## 一覧

### `sleep/`（柱①）

睡眠記事の論点は *精神医学* 67(5) **「睡眠の正しい理解を促す70のトリビア」**と対応（`literature_content_map.md` §7.1）。**記事番号の照合は執筆・編集側**（読者向けに雑誌を開かせない）。**バックログ番号＝`blog_articles_backlog_50.md` の投稿順**に揃える（フェーズ1→3 がコア、**#51〜 は内科×睡眠など拡張**）。

| ファイル | バックログ（投稿順 #） | 公開コピー（Astro） |
|---|---|---|
| `draft_blog_01_sleep_declaration.md` | #1 | `blog-site/.../sleep-why-orthopedic-sleep.md` |
| `draft_blog_02_pain_sleep_intersection.md` | #2 | `blog-site/.../sleep-pain-intersection.md` |
| `draft_blog_03_online_sleep_who.md` | #3 | （未） |
| `draft_blog_04_cbti_intro.md` | #4 | （未） |
| `draft_blog_05_sleep_hygiene_not_enough.md` | #5 | （未） |
| `draft_blog_06_stimulus_control.md` | #6 | （未） |
| `draft_blog_07_sleep_restriction.md` | #7 | （未） |
| `draft_blog_08_long_bed_time_insomnia.md` | #8 | （未） |
| `draft_blog_09_wake_time_consistency.md` | #9 | （未） |
| `draft_blog_10_caffeine_cutoff.md` | #10 | （未） |
| `draft_blog_11_weekend_lie_in.md` | #11 | （未） |
| `draft_blog_12_bed_smartphone.md` | #12 | （未） |
| `draft_blog_13_sleep_quality_first.md` | #13 | （未） |
| `draft_blog_14_snoring_when_seek.md` | #14 | （未） |
| `draft_blog_15_daytime_sleepiness.md` | #15 | （未） |
| `draft_blog_16_osa_signs.md` | #16 | （未） |
| `draft_blog_17_sleep_tech_wearables.md` | #17 | （未） |
| `draft_blog_18_reduce_sleep_medication.md` | #18 | （未） |
| `draft_blog_19_health_info_literacy.md` | #19 | （未） |
| `draft_blog_20_first_visit_overview.md` | #20 | （未・開業後） |
| `draft_blog_21_evening_type_to_morning.md` | #21 | （未） |
| `draft_blog_22_stress_forcing_sleep.md` | #22 | （未） |
| `draft_blog_23_child_sleep_basics.md` | #23 | （未） |
| `draft_blog_24_adolescent_sleep_phase.md` | #24 | （未） |
| `draft_blog_25_neurodiversity_sleep_intro.md` | #25 | （未） |
| `draft_blog_26_menopause_sleep_changes.md` | #26 | （未） |
| `draft_blog_27_shift_work_sleep.md` | #27 | （未） |
| `draft_blog_28_elderly_early_awakening.md` | #28 | （未） |
| `draft_blog_29_morning_rise_difficulty.md` | #29 | （未） |
| `draft_blog_30_parenting_sleep_priorities.md` | #30 | （未） |
| `draft_blog_31_insomnia_subjective_gap.md` | #31 | （未） |
| `draft_blog_32_rls_legs_sleep.md` | #32 | （未） |
| `draft_blog_33_central_hypersomnia_online_limits.md` | #33 | （未） |
| `draft_blog_34_insomnia_depression_timing.md` | #34 | （未） |
| `draft_blog_35_clinic_opening_series.md` | #35 | （未・第0回） |
| `draft_blog_36_private_sleep_care_patient.md` | #36 | （未） |
| `draft_blog_37_referral_primary_care.md` | #37 | （未） |
| `draft_blog_38_chronic_pain_insomnia.md` | #38 | （未） |

**#51〜58**（内科×睡眠、**メモでは `F主軸`＋`B`**。**柱表記 `B+F`**）と **#59〜73**（**70トリビア**の論点分割・`**#70` 欠番**）はバックログにタイトル案とファイル名あり。着手時に `sleep/` へ `draft_blog_51_*` などを追加する。

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
