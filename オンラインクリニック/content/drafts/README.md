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
- **`sleep/` のファイル名規則**：`blog_<バックログ番号>_<短いslug>.md`（`draft_` プレフィックスなし。#1〜73 すべて統一済み）
  - 男性・女性柱は旧来通り：`male/draft_blog_male_01_loh_intro.md` のようにファイル名で柱が分かるとよい。
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
| `blog_01_sleep_declaration.md` | #1 | blog-site/.../sleep-why-orthopedic-sleep.md |
| `blog_02_online_sleep_who.md` | #2 | （未） |
| `blog_03_pain_sleep_intersection.md` | #3 | blog-site/.../sleep-pain-intersection.md |
| `blog_04_cbti_intro.md` | #4 | （未） |
| `blog_05_sleep_hygiene_not_enough.md` | #5 | （未） |
| `blog_06_stimulus_control.md` | #6 | （未） |
| `blog_07_sleep_restriction.md` | #7 | （未） |
| `blog_08_long_bed_time_insomnia.md` | #8 | （未） |
| `blog_09_wake_time_consistency.md` | #9 | （未） |
| `blog_10_caffeine_cutoff.md` | #10 | （未） |
| `blog_11_stress_forcing_sleep.md` | #11 | （未） |
| `blog_12_weekend_lie_in.md` | #12 | （未） |
| `blog_13_bed_smartphone.md` | #13 | （未） |
| `blog_14_sleep_quality_first.md` | #14 | （未） |
| `blog_15_health_info_literacy.md` | #15 | （未） |
| `blog_16_first_visit_overview.md` | #16 | （未・開業後） |
| `blog_17_sleep_diary_minimum_viable.md` | #17 | （未） |
| `blog_18_insomnia_depression_timing.md` | #18 | （未） |
| `blog_19_snoring_when_seek.md` | #19 | （未） |
| `blog_20_daytime_sleepiness.md` | #20 | （未） |
| `blog_21_osa_signs.md` | #21 | （未） |
| `blog_22_sleep_tech_wearables.md` | #22 | （未） |
| `blog_23_reduce_sleep_medication.md` | #23 | （未） |
| `blog_24_evening_type_to_morning.md` | #24 | （未） |
| `blog_25_child_sleep_basics.md` | #25 | （未） |
| `blog_26_adolescent_sleep_phase.md` | #26 | （未） |
| `blog_27_neurodiversity_sleep_intro.md` | #27 | （未） |
| `blog_28_menopause_sleep_changes.md` | #28 | （未） |
| `blog_29_shift_work_sleep.md` | #29 | （未） |
| `blog_30_elderly_early_awakening.md` | #30 | （未） |
| `blog_31_morning_rise_difficulty.md` | #31 | （未） |
| `blog_32_parenting_sleep_priorities.md` | #32 | （未） |
| `blog_33_insomnia_subjective_gap.md` | #33 | （未） |
| `blog_34_rls_legs_sleep.md` | #34 | （未） |
| `blog_35_central_hypersomnia_online_limits.md` | #35 | （未） |
| `blog_36_clinic_opening_series.md` | #36 | （未・第0回） |
| `blog_37_private_sleep_care_patient.md` | #37 | （未） |
| `blog_38_referral_primary_care.md` | #38 | （未） |
| `blog_39_chronic_pain_insomnia.md` | #39 | （未） |
| `blog_40_low_back_pain_sleep.md` | #40 | （未） |
| `blog_41_hip_knee_pain_sleep.md` | #41 | （未） |
| `blog_42_postop_night_pain_sleep.md` | #42 | （未） |
| `blog_43_sports_sleep_recovery.md` | #43 | （未） |
| `blog_44_injury_healing_sleep.md` | #44 | （未） |
| `blog_45_pain_sleep_patient_talk.md` | #45 | （未） |
| `blog_46_cast_brace_sleep.md` | #46 | （未） |
| `blog_47_locomotive_syndrome_sleep.md` | #47 | （未） |
| `blog_48_multidisciplinary_chronic_pain_sleep.md` | #48 | （未） |
| `blog_49_pain_clinic_sleep_boundary.md` | #49 | （未） |
| `blog_50_orthopedic_sleep_history.md` | #50 | （未） |
| `blog_51_body_relaxation_sleep_pain.md` | #51 | （未） |
| `blog_52_thyroid_sleep.md` | #52（F主軸+B） | （未） |
| `blog_53_diabetes_metabolic_sleep.md` | #53（F主軸+B） | （未） |
| `blog_54_cardiovascular_sleep.md` | #54（F主軸+B） | （未） |
| `blog_55_ckd_dialysis_sleep.md` | #55（F主軸+B） | （未） |
| `blog_56_liver_gi_alcohol_sleep.md` | #56（F主軸+B） | （未） |
| `blog_57_iron_anemia_sleep.md` | #57（F主軸+B） | （未） |
| `blog_58_rheumatic_inflammation_sleep.md` | #58（F主軸+B） | （未） |
| `blog_59_post_infectious_fatigue_sleep.md` | #59（F主軸+B） | （未） |
| `blog_60_napping_daytime_sleepiness.md` | #60（A+B） | （未） |
| `blog_61_alcohol_sleep_myth.md` | #61（A+B） | （未） |
| `blog_62_exercise_timing_sleep.md` | #62（A） | （未） |
| `blog_63_melatonin_general.md` | #63（A+B） | （未） |
| `blog_64_bedroom_tv_sleep.md` | #64（A） | （未） |
| `blog_65_jet_lag_travel_sleep.md` | #65（A） | （未） |
| `blog_66_sleep_tracker_subjective_gap.md` | #66（A+B） | （未） |
| `blog_67_dreams_rem_overview.md` | #67（A+B） | （未） |
| `blog_68_hypnic_jerk_sleep_onset.md` | #68（A+B） | （未） |
| `blog_69_exploding_head_phenomenon_basic.md` | #69（A+B） | （未） |
| ※ **#70 欠番**（雑誌「70のトリビア」と番号混同防止） | — | — |
| `blog_71_insomnia_phenotypes_overview.md` | #71（A+B） | （未） |
| `blog_72_bedding_temperature_sleep.md` | #72（A+B） | （未） |
| `blog_73_humidity_airway_sleep.md` | #73（A+B） | （未） |

**#51〜73 はすべて作成済み（2026-05）**。次に追加するときは `#74` 以降（採番は `blog_articles_backlog_50.md` の末尾を更新して揃える）。

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
