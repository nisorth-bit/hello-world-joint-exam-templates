# ブログ記事バックログ（コア50本＋拡張）— オンライン睡眠を入口に

**フォルダ全体の案内**：[`README.md`](README.md)（ドキュメント一覧・番号ルール）。

**想定サイト**：Astro ブログ（`経営/ブログ・コンテンツ/strategy.md` および `blog-site/`）。サブタイトル的には **オンライン睡眠クリニック向け記事リスト**（整形×痛みは差別化・後段も可）。

**下書きパス**：表内の `draft_blog_*.md` は、省略時も **`drafts/sleep/` 配下**を指します。

**編集定点（2026-05）**：**オンライン睡眠診療をフォーカス**（入り口・生活・CBT-I・受診目安）。**オンライン×整形だけ**を前面に出すと裾野が狭まるため、トリビア要約系（**A・B 列**：睡眠一般＋受診目安）を**整形患者に限定しない読者**向けに厚くする。整形外科×睡眠（**E 列**）は**差別化・接点**として配置。**内科的素因・重症例・睡眠薬中心の専門管理が主役のケース**は **F 列（他科×睡眠）** や紹介前提の記述で書く（`three_pillars_strategy.md` §0）。  

**コンセプト**：**睡眠の入り口** × CBT-I ×（任意で）痛み・身体活動との接続。  

**執筆ルール**：`literature_content_map.md` の7段テンプレ。雑誌・文献は**転載せず**、論点の裏付けに使う。

**柱タグ（一覧・表の「柱」列）**：`A` 睡眠一般（CBT-I・生活リズム・睡眠衛生）　`B` 受診目安・鑑別・安全線　`C` ライフステージ・社会　`D` クリニック運営・信頼　`E` 整形外科×睡眠　`F` 他科×睡眠（内科・精神科など専門科とのすみ分け・紹介の論点。今後追加する記事で使う）

---

## タイトル方針（再考）

- **一覧のタイトル**は、検索・SNS・一覧で「眠りの悩み」に届く言葉を優先（**慢性痛・腰痛・膝**などは**差別化用**として残すが、**サイト初回の顔**にはしなくてよい）。  
- **D（クリニック運営・宣言・信頼）**は「なぜオンラインで睡眠か」「誰に向けているか」が一読で伝わる語に寄せる。  
- **A（睡眠一般）**はトリビア由来の**生活論点**がタイトルから透けて見えるとよい（例：カフェイン、起床、スマホ）。  
- **B（受診目安）**は断定を避けつつ、「いつ受診を考えるか」が伝わるタイトルにする。  
- 公開用の**URLスラッグ**は変えずにタイトルだけ変える運用でもよい（Astro の `title` とファイル名を別管理）。

---

## 公開の順番（おすすめ・2026-05 改訂）

**一覧の `#` は投稿順（フェーズ1→2→3）**に並べています。`drafts/sleep/draft_blog_<#>_*.md` の番号もこれに合わせてある（未執筆は番号のみ）。

**方針**：初回ローンチは **#1〜16** 付近（睡眠の入り口）で裾野を広く取る。**#38〜50** の痛み×整形寄りは**最初の投稿ブロックに入れなくてよい**。

### フェーズ1（初回公開の核）

**#1〜16**（宣言・交差点・向き不向き・CBT-I・生活・質・呼吸・OSA）→ 必要に応じ **#17〜22**（スリープテック・睡眠薬減量・YMYL・初診案内・夜型・ストレス）。**本数増**：70のトリビアは**目次・見出しを1論点1記事に分割**するとロングテールに効くので、論点ごとに **#59〜** の拡張行を増やしていく（詳細は表・メモ）。

### フェーズ1b（**70トリビア**の論点分割）

**#59〜73**（一覧で **#70 は欠番**）。**#4〜16** の内容を補い、ロングテール用に**1見出し＝1記事**で増やす。公開順は **#17 の前後**でも可（編集判断）。

### フェーズ2（月数本ペース）

**#23〜37**（子ども〜育児・残りのC・準備記など）。

### フェーズ3（痛み×整形・差別化）

**#38〜50**。下書き可。**初回ローンチ不要可**。

### フェーズ4（拡張：**内科×睡眠**）

**#51〜**：内科（かかりつけ・検査が主役になりやすい）×睡眠。**一覧の柱表記が `B+F` でも、設計上の主軸は **`F`（他科×睡眠）**。**受診目安 **`B`** を必ず添える**。オンラインで完治・検査代替を約束しない前提と**紹介の目安**を毎回明示（`three_pillars_strategy.md` §0）。**#14〜16（呼吸）・#32（脚むずむず）** などと相互リンク可。

### 運用メモ

- 各記事末の**免責**は揃える。  
- **旧バックログ番号**（投稿順導入前）との対応が必要なときは Git 履歴または本コミットのリネームを参照。

---

## 一覧（投稿順）

| # | タイトル案 | 柱 | メモ（内部用） |
|---:|---|:---:|---|
| 1 | 睡眠をオンラインの入り口に——整形外科医がこのブログを書く理由 | D | **フェーズ1**。`drafts/sleep/draft_blog_01_sleep_declaration.md` · 公開 `sleep-why-orthopedic-sleep.md` |
| 2 | 痛みと眠りの交差点——このブログで届けたいこと | D | **フェーズ1**。`drafts/sleep/draft_blog_02_pain_sleep_intersection.md` · 公開 `sleep-pain-intersection.md` |
| 3 | オンライン睡眠相談、向きやすい人と慎重な人 | B+D | **フェーズ1**。`drafts/sleep/draft_blog_03_online_sleep_who.md` |
| 4 | CBT-Iとは：薬だけに頼らない不眠治療の枠組み | A | `drafts/sleep/draft_blog_04_cbti_intro.md` |
| 5 | 「睡眠衛生だけ」では足りないことがある理由 | A | `drafts/sleep/draft_blog_05_sleep_hygiene_not_enough.md` |
| 6 | 刺激制御療法——寝室とベッドの役割を分ける | A | `drafts/sleep/draft_blog_06_stimulus_control.md` |
| 7 | 睡眠制限法が怖い人へ：イメージと留意点 | A | `drafts/sleep/draft_blog_07_sleep_restriction.md` |
| 8 | 布団に長くいる時間と不眠の関係 | A | 記事34系 → `drafts/sleep/draft_blog_08_long_bed_time_insomnia.md` |
| 9 | 起床時刻をそろえると、何が変わりやすいか | A | `drafts/sleep/draft_blog_09_wake_time_consistency.md` |
| 10 | カフェインは「何時まで」が現実的か | A | `drafts/sleep/draft_blog_10_caffeine_cutoff.md` |
| 11 | 休日の寝だめの功罪を整理する | A | `drafts/sleep/draft_blog_11_weekend_lie_in.md` |
| 12 | ベッドでスマホがやめられないときの優先順位 | A | `drafts/sleep/draft_blog_12_bed_smartphone.md` |
| 13 | 「眠りの質が悪い」と感じたとき最初の着眼点 | A+B | `drafts/sleep/draft_blog_13_sleep_quality_first.md` |
| 14 | いびきが気になるとき——受診の目安の話 | B | `drafts/sleep/draft_blog_14_snoring_when_seek.md` |
| 15 | 日中に強い眠気があるとき、考えたいこと | B | `drafts/sleep/draft_blog_15_daytime_sleepiness.md` |
| 16 | 睡眠時無呼吸を疑うサインを整理する（一般情報） | B | `drafts/sleep/draft_blog_16_osa_signs.md` |
| 17 | スリープテック・ウェアラブルはどこまで参考にするか | A | `drafts/sleep/draft_blog_17_sleep_tech_wearables.md` |
| 18 | 「睡眠薬を減らしたい」相談にどう向き合うか | A+D | `drafts/sleep/draft_blog_18_reduce_sleep_medication.md` |
| 19 | 医療情報を読み分ける——信頼できる記事の目安 | D | `drafts/sleep/draft_blog_19_health_info_literacy.md` |
| 20 | はじめての方へ：初診で整理する流れ（一般説明） | D | `drafts/sleep/draft_blog_20_first_visit_overview.md`（開業後に実フローと照合） |
| 21 | 夜型生活を朝型に寄せる——現実的なステップ | A | `drafts/sleep/draft_blog_21_evening_type_to_morning.md` |
| 22 | ストレスな日に「無理に寝る」ことの功罪 | A | `drafts/sleep/draft_blog_22_stress_forcing_sleep.md` |
| 23 | 子どもの睡眠——親が押さえたい基本 | C | `drafts/sleep/draft_blog_23_child_sleep_basics.md` |
| 24 | 思春期の起床困難と睡眠相の話 | C | `drafts/sleep/draft_blog_24_adolescent_sleep_phase.md` |
| 25 | 発達特性と睡眠のつながり（入門） | C | `drafts/sleep/draft_blog_25_neurodiversity_sleep_intro.md` |
| 26 | 更年期の睡眠のつかえとからだの変化 | C | `drafts/sleep/draft_blog_26_menopause_sleep_changes.md` |
| 27 | 夜勤・交替勤務の人の睡眠の取り方 | C | `drafts/sleep/draft_blog_27_shift_work_sleep.md` |
| 28 | 高齢者の早朝覚醒と日中の眠気——何を整えるか | C | `drafts/sleep/draft_blog_28_elderly_early_awakening.md` |
| 29 | 起床困難・朝起きの悪さと生活リズムの話 | C | `drafts/sleep/draft_blog_29_morning_rise_difficulty.md` |
| 30 | 育児中の睡眠不足——現実的な優先順位 | C | `drafts/sleep/draft_blog_30_parenting_sleep_priorities.md` |
| 31 | 「ずっと眠れていない」見え方のズレがある場合 | B | `drafts/sleep/draft_blog_31_insomnia_subjective_gap.md` |
| 32 | 睡眠中の脚の違和感・むずむずについて（概要と受診目安） | B | `drafts/sleep/draft_blog_32_rls_legs_sleep.md` |
| 33 | 中枢性過眠症の話——オンライン相談の限界も含めて | B | `drafts/sleep/draft_blog_33_central_hypersomnia_online_limits.md` |
| 34 | 不眠とうつ——すみ分けと相談のタイミング | B | `drafts/sleep/draft_blog_34_insomnia_depression_timing.md` |
| 35 | オンライン睡眠クリニック準備記（随時更新シリーズ） | D | `drafts/sleep/draft_blog_35_clinic_opening_series.md`（第0回・分割可） |
| 36 | 自由診療の睡眠診療を選ぶ意味（患者さん向け） | D | `drafts/sleep/draft_blog_36_private_sleep_care_patient.md` |
| 37 | かかりつけ医の先生へ——紹介のイメージと連携 | D | `drafts/sleep/draft_blog_37_referral_primary_care.md` |
| 38 | 慢性痛と不眠は、なぜいっしょに起きやすいのか | E | **フェーズ3**。`drafts/sleep/draft_blog_38_chronic_pain_insomnia.md` |
| 39 | 腰痛で眠れない——夜に試したい整理のしかた | E | **フェーズ3** |
| 40 | 膝・股関節の痛みと睡眠の悪循環をどう断つか | E | **フェーズ3** |
| 41 | 手術後「夜だけ痛くて眠れない」ときの考え方 | E | **フェーズ3** |
| 42 | スポーツ整形の文脈で見る「睡眠＝回復」 | E | **フェーズ3** |
| 43 | 睡眠はケガのリスクや治癒とどう関わるか | E | **フェーズ3** |
| 44 | 痛みの強さと睡眠の質：説明のコツ（患者対話） | E | **フェーズ3** |
| 45 | ギプス・装具装着中の睡眠の工夫 | E | **フェーズ3** |
| 46 | ロコモティブシンドロームと睡眠（いま知りたい要点） | E | **フェーズ3** |
| 47 | 慢性痛の多角的ケアの一翼としての睡眠医療 | E | **フェーズ3** |
| 48 | ペインクリニックと睡眠：すみ分けのイメージ | B+E | **フェーズ3** |
| 49 | 整形外科の問診で「眠り」を聞く意味 | D+E | **フェーズ3** |
| 50 | 身体寄りのリラクゼーション入門——痛みとも相性よい理由 | A+E | **フェーズ3**（不眠一般にも使えるならフェーズ2で織り込み可） |
| 51 | 甲状腺のからだの変化と眠り——ひと息で目が覚める・動悸と、受診の目安 | B+F | **フェーズ4**。**F主軸**。未執筆 → `drafts/sleep/draft_blog_51_thyroid_sleep.md`。甲状腺機能と睡眠の**すみ分け**（検査はかかりつけ・内分泌） |
| 52 | 糖尿病・血糖と夜の眠り——夜間低血糖、頻尿から肥満といびきまで | B+F | **フェーズ4**。**F主軸**。未執筆 → `drafts/sleep/draft_blog_52_diabetes_metabolic_sleep.md`。**#14〜16**（OSA）・男性柱の夜間頻尿とも接続可 |
| 53 | 血圧・心臓の不調と眠り——夜間の呼吸苦、むくみ、コントロールの難しさ | B+F | **フェーズ4**。**F主軸**。未執筆 → `drafts/sleep/draft_blog_53_cardiovascular_sleep.md`。循環器・内科の検査が主役になりうる話 |
| 54 | 腎臓の病気・透析と眠り——かゆみ、脚のつり、スケジュールと寝不足 | B+F | **フェーズ4**。**F主軸**。未執筆 → `drafts/sleep/draft_blog_54_ckd_dialysis_sleep.md` |
| 55 | 肝臓・お腹のつかえと眠り——逆流、飲酒のパターンと入眠、日中の眠気 | B+F | **フェーズ4**。**F主軸**。未執筆 → `drafts/sleep/draft_blog_55_liver_gi_alcohol_sleep.md` |
| 56 | 鉄が足りないときの眠り——「だるい」と「眠れない」の見分けと脚のむずむず | B+F | **フェーズ4**。**F主軸**。未執筆 → `drafts/sleep/draft_blog_56_iron_anemia_sleep.md`。**#32**（RLS の受診目安）への送客 |
| 57 | 慢性炎症・リウマチと眠り——全身の病気としての不眠を整理する | B+F | **フェーズ4**。**F主軸**。未執筆 → `drafts/sleep/draft_blog_57_rheumatic_inflammation_sleep.md`。整形 **#38〜** とは**全身疾患の接点**として切り分け |
| 58 | 感染後も続く強い疲れと眠り——言い分けと、主治医へ相談する目安（一般論） | B+F | **フェーズ4**。**F主軸**。未執筆 → `drafts/sleep/draft_blog_58_post_infectious_fatigue_sleep.md`。病名断定はしない・鑑別の話に留める |
| 59 | 昼の強い眠気と仮眠——何分まで・いつの仮眠が議論になりやすいか | A+B | **トリビア拡張**（フェーズ1近傍で公開してもよい）。未執筆 → `drafts/sleep/draft_blog_59_napping_daytime_sleepiness.md`。70トリビアの**仮眠・カフェイン**等と隣接。`#10` とリンク |
| 60 | 「寝酒」「ナイトキャップ」と眠りの質——気分はラクでも深睡眠は別問題 | A+B | **トリビア拡張**。未執筆 → `drafts/sleep/draft_blog_60_alcohol_sleep_myth.md`。**#55** の飲酒パートとリンク可 |
| 61 | 運動と眠り——朝と夜どちらが効きやすいか、論争を一般向けに整理する | A | **トリビア拡張**。未執筆 → `drafts/sleep/draft_blog_61_exercise_timing_sleep.md` |
| 62 | メラトニン（市販・サプリ）はどこまで期待してよいか | A+B | **トリビア拡張**。未執筆 → `drafts/sleep/draft_blog_62_melatonin_general.md`。医薬品の話に拡張するなら処方監査の注意 |
| 63 | 寝室のテレビ――光と「寝落ち」の習慣をどう説明するか | A | **トリビア拡張**。未執筆 → `drafts/sleep/draft_blog_63_bedroom_tv_sleep.md`。`#12` とセットで読ませやすい |
| 64 | 長距離移動や時差のあと――体内時計に焦らず整える順序（一般） | A | **トリビア拡張**。未執筆 → `drafts/sleep/draft_blog_64_jet_lag_travel_sleep.md`。`#11` と区別して「時差」「旅行直後」を前面に |
| 65 | 「睡眠計の分数」と体感がずれるとき——主観的睡眠不足の入り口（一般説明） | A+B | **トリビア拡張**。未執筆 → `drafts/sleep/draft_blog_65_sleep_tracker_subjective_gap.md`。`#31` への送客 |
| 66 | 「夢を見ない不安」への答え――レムと主観の話だけ一般向けに | A+B | **トリビア拡張**。未執筆 → `drafts/sleep/draft_blog_66_dreams_rem_overview.md` |
| 67 | 入眠時のギュッ／ビクッ（睡眠開始時収縮）が怖いとき | A+B | **トリビア拡張**。未執筆 → `drafts/sleep/draft_blog_67_hypnic_jerk_sleep_onset.md` |
| 68 | 「頭のパン」と一瞬で起きる感じ——よくある生理と相談目安を分ける | A+B | **トリビア拡張**。未執筆 → `drafts/sleep/draft_blog_68_exploding_head_phenomenon_basic.md`。鑑別は軽め、赤旗へは **B** |
| 69 | 不眠のタイプだけ一言——入眠から早期覚醒まで、自分の話の置き場所 | A+B | **トリビア拡張**。未執筆 → `drafts/sleep/draft_blog_69_insomnia_phenotypes_overview.md`。`#4`・`#34` とリンク |
| 71 | CBT-Iで言う睡眠日記——続けられる現実ラインだけ先に決める | A | **トリビア拡張**。未執筆 → `drafts/sleep/draft_blog_71_sleep_diary_minimum_viable.md`。`#7` とリンク |
| 72 | 布団環境だけ先に決める——温度・寝返り・寒すぎ熱すぎ（いびきは軽く） | A+B | **トリビア拡張**。未執筆 → `drafts/sleep/draft_blog_72_bedding_temperature_sleep.md` |
| 73 | 加湿器・室温・乾燥と喉・むせ——いびきの話と束ねられる論点（一般） | A+B | **トリビア拡張**。未執筆 → `drafts/sleep/draft_blog_73_humidity_airway_sleep.md`。`#14` への入口 |

---

## メモ

- **採番の注意**：一覧の **`#70` は空けている**。雑誌タイトルの「70のトリビア」と**数字が被ると運用ミスが出やすい**ため。必要な論点は **#69 の次が #71**。
- **読者像**：トリビア・生活習慣・CBT-I入門（おおむね **#4〜16**）は、**整形外来に来ていない人**も読む前提で執筆する。**#59〜73** はそれを補強する**トリビア1論点1記事**用。  
- **既存ネタとの重複**：`plan.md` の「最初の3記事」は **#1（宣言）・#38（痛み×睡眠）・#4（CBT-I入口、必要なら #18）** と対応（旧タイトル案は本文に統合可）。`social_posts_draft_20.md` は **#1〜4** などにマージ。  
- **本数を増やすとき**：*精神医学* 67(5)**「睡眠の正しい理解を促す70のトリビア」**の**目次・見出し相当を1論点1記事**に割ると、`#59〜73` と同様の**トリビア拡張行**を足して **#4〜16 のコア**の直後〜並行公開でロングテールを取れる（採番は表の末尾に **`#74`〜** と続ける。`**#70` は雑誌の「70本」と混同しやすいので欠番または使わない**）。内科×睡眠は **#51〜** で **`F主軸`＋`B`** で増やす。  
- **進捗管理**：スプレッドシートにこの表をコピーし、`下書き / 推敲 / 公開 / URL` 列を足すと運用しやすい。

更新日：2026-05-09（**#17〜37** 下書きファイルを `drafts/sleep/` に追加）

---

## 柱タグの新旧対応（英字だけ旧表記のメモがある場合）

| 旧柱タグ | 現行 |
|:---:|:---:|
| A（痛み・回復×睡眠） | **E**（整形外科×睡眠） |
| B（CBT-I・生活） | **A**（睡眠一般） |
| C（鑑別・安全） | **B**（受診目安） |
| D（ライフステージ・社会） | **C** |
| E（クリニック・信頼） | **D**（クリニック運営） |
| （なし） | **F**（他科×睡眠）※新規。内科・精神科等のすみ分け記事へ |

※表の **`#`（投稿順）** の再採番以前との対応は Git 履歴を参照。
