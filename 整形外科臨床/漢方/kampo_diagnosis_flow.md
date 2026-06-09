# 漢方診察・証判定フロー

> 目標：「証を完璧に診る」ではなく「虚実・寒熱の大枠を掴み、整形外科疾患に使える処方を選べる」こと

---

## 略語一覧

| 略語 | 英語 | 日本語 |
|------|------|--------|
| RCT | Randomized Controlled Trial | ランダム化比較試験 |
| IRR | Inter-Rater Reliability | 評価者間信頼性 |
| ICC | Intraclass Correlation Coefficient | 級内相関係数 |
| AC | Agreement Coefficient | 一致係数（Gwet法） |
| ICD-10 | International Classification of Diseases, 10th revision | 国際疾病分類第10版 |
| CONSORT | Consolidated Standards of Reporting Trials | 臨床試験報告統合基準 |
| PRISMA | Preferred Reporting Items for Systematic Reviews and Meta-Analyses | 系統的レビュー・メタ解析の報告基準 |
| TCM | Traditional Chinese Medicine | 中国伝統医学 |
| CT | Computed Tomography | コンピュータ断層撮影 |
| QOL | Quality of Life | 生活の質 |
| BMI | Body Mass Index | 体格指数 |

---

## 第1章 証とは何か

証（しょう / Sho）= 患者の「今この瞬間の状態」。体質＋症状を合わせた概念（disease pattern）。

西洋医学との違い：
- 西洋医学 → 病名（ICD-10診断）から治療を決める
- 漢方 → 証（Sho: 状態パターン）から処方を決める

**同じ「腰痛」でも証が違えば処方が変わる。**

> Kampo medicine selects treatment based on the patient's current condition (Sho), rather than the disease name alone.[^1]

---

## 第2章 証判定の3軸（八綱弁証 / Hachiko-bensho）

```
証の判定
├── 虚実（きょじつ / Kyojitsu）：体力・抵抗力の強弱
├── 寒熱（かんねつ / Kannetsu）：冷えているか熱があるか
└── 気血水（きけつすい / Ki-Ketsu-Sui）：何が滞っているか
```

### エビデンス：各軸の信頼性（IRR）

Maeda-Minami ら（2021）による慢性疾患患者64例を対象とした IRR（評価者間信頼性）研究[^2]：

| 判定軸 | 一致率 | Gwet's AC | 信頼性 |
|--------|--------|-----------|--------|
| 虚実（Kyojitsu） | **85.9%** | **0.708** | 相当（Substantial） |
| 寒熱（Kannetsu） | 64.6% | 0.542 | 中等度（Moderate） |
| 気血水（Ki-Ketsu-Sui） | 35.9% | 0.254 | 弱（Fair） |

**臨床的意味：虚実と寒熱は比較的再現性が高く、初心者でも習得しやすい。気血水は専門的な訓練が必要。**

---

### 軸① 虚実（Kyojitsu / Deficiency-Excess）

最も重要かつ IRR が高い（AC = 0.708）。処方選択の根幹。

| | 虚証（きょしょう / Deficiency） | 実証（じっしょう / Excess） |
|--|-------------------------------|--------------------------|
| 体格 | 痩せ・華奢（BMI低め） | がっちり・肥満傾向 |
| 体力 | 疲れやすい・声が小さい | 体力あり・声に力 |
| 顔色 | 青白い・くすんでいる | 赤ら顔・脂性 |
| 腹診（Fukushin） | 腹壁軟・力がない | 腹壁張り・抵抗感 |
| 便通 | 軟便・下痢傾向 | 便秘傾向 |
| 訴え方 | おとなしい・遠慮がち | 積極的・症状を強く訴える |

**整形外科での実践**
- 虚証の高齢者腰痛 → 牛車腎気丸・補中益気湯
- 実証の急性腰痛・筋緊張強い → 疎経活血湯・大黄含有処方

---

### 軸② 寒熱（Kannetsu / Cold-Heat）

IRR 中等度（AC = 0.542）。問診で概ね判定可能。

| | 寒証（かんしょう / Cold pattern） | 熱証（ねつしょう / Heat pattern） |
|--|--------------------------------|--------------------------------|
| 体感 | 冷えを感じる・低体温 | 熱感・のぼせ |
| 関節症状 | 温めると楽（温熱療法有効） | 冷やすと楽（急性炎症期） |
| 口渇 | 少ない・温かいものを好む | 強い・冷たいものを好む |
| 尿 | 淡色・量多い | 濃色・量少ない |
| 舌 | 淡白・白苔 | 紅舌・黄苔 |

**整形外科での実践**
- 寒証の慢性関節痛 → 桂枝加朮附湯・当帰四逆加呉茱萸生姜湯
- 熱証の急性関節炎（発赤・熱感・腫脹）→ 越婢加朮湯

---

### 軸③ 気血水（Ki-Ketsu-Sui / Qi-Blood-Fluid）

IRR は低め（AC = 0.254）。専門的訓練を要するが、**パターン認識**で整形外科疾患に応用できる。

| | 気滞（きたい / Qi stagnation） | 血瘀（けつお / Blood stasis） | 水滞（すいたい / Fluid retention） |
|--|------------------------------|------------------------------|----------------------------------|
| 概念 | 気（エネルギー）の流れが停滞 | 血行不良・微小循環障害 | 水分代謝・体液分布の異常 |
| 症状 | 張り感・ガス・情緒不安定・CRPS様 | 固定した痛み・夜間増悪・皮膚暗紫 | 浮腫・めまい・頭重・気圧変化で悪化 |
| 舌 | 正常〜やや暗 | 暗紫・瘀斑（血流障害の所見） | 歯痕・水滑苔（水分過多） |
| 整形外科場面 | 神経障害性疼痛・CRPS | 慢性腰痛・打撲後遺症・術後疼痛遷延 | 術後浮腫・天気痛・しびれ |
| 代表処方 | 柴胡剤・四逆散 | 疎経活血湯・桂枝茯苓丸 | 五苓散・防已黄耆湯 |

---

## 第3章 四診（Shishin / Four Examinations）の実践

### ① 望診（ぼうしん / Visual inspection）：見る

**顔色**
- 青白い → 虚証・寒証・気血両虚
- 赤ら顔 → 実証・熱証・上熱下寒
- くすんだ暗色 → 血瘀

**舌診（Zessin / Tongue diagnosis）**

舌診は IRR が中等度（評価一致率 0.52、95% CI: 0.38–0.65）と報告されており[^3]、四診のなかで最も客観化しやすい所見とされる。標準化された照明・撮影条件により再現性が向上する。

| 所見 | 意味 | 整形外科での関連 |
|------|------|----------------|
| 淡紅色・薄白苔 | 正常 | — |
| 淡白舌（Pale tongue） | 気血両虚・寒証 | 術後回復遅延・高齢者 |
| 紅舌・黄苔（Red tongue, yellow coat） | 熱証・炎症 | 急性関節炎・感染 |
| 暗紫・瘀斑（Purple tongue, ecchymosis） | 血瘀（Blood stasis） | 慢性疼痛・打撲後遺症・CRPS |
| 歯痕・腫大（Tooth marks, swollen） | 水滞・脾虚 | 術後浮腫・天気痛 |
| 乾燥・亀裂（Dry, cracked） | 陰虚・津液不足 | 高齢者・利尿薬内服中 |

**体格・体型**
- 痩せ（低 BMI）→ 虚証傾向
- 肥満・むくみ → 水滞・防已黄耆湯タイプ

---

### ② 問診（もんしん / Medical interview）：聞く

整形外科で追加する漢方問診：

```
□ 冷えているか・温めると楽か（寒熱の判定）
□ 天気・気圧変化で悪化するか（水滞 → 五苓散）
□ 夜間に痛みが増すか（血瘀 → 疎経活血湯）
□ 疲れると悪化するか（虚証 → 補中益気湯系）
□ 便通・食欲の状態（脾胃 / 消化機能の評価）
□ 月経との関連（女性 → 桂枝茯苓丸・加味逍遥散等）
```

---

### ③ 切診（せっしん / Palpation）：触る

#### 脈診（Myakushin / Pulse diagnosis）

脈診の IRR は各研究で低〜中等度とされており[^4]、西洋医学的視点では再現性に課題がある。初心者は以下の基本パターンの把握から始める。

| 脈の性状 | 英語 | 意味 |
|---------|------|------|
| 浮脈（表面で触れる） | Floating pulse | 表証・初期・急性期 |
| 沈脈（深く押さないと触れない） | Deep pulse | 裏証・慢性・虚証 |
| 遅脈（60回/分未満） | Slow pulse | 寒証 |
| 数脈（90回/分以上） | Rapid pulse | 熱証・炎症・発熱 |
| 細脈（細く弱い） | Thin pulse | 虚証・血虚 |
| 弦脈（弦を弾くような張り） | Wiry pulse | 肝気鬱結・疼痛・ストレス |

#### 腹診（Fukushin / Abdominal diagnosis）

腹診は Kampo 診察の核心であり、日本独自に発展した。CT を用いた解剖学的研究（Shimada ら 2021）[^5]により、臍周囲の拍動（腹部大動脈の触知）は解剖学的位置・深さ・体型によって検出率が異なることが明らかとなった（臍上部 30%、心窩部 21%、臍下部 15%）。また Fukushin シミュレーター（13 標準腹部パターンモデル）の開発[^6]により、教育的な再現性の向上が図られている。

| 腹診所見 | 英語 | 意味 | 代表処方 |
|---------|------|------|---------|
| 腹力弱・臍下不仁（臍下が柔らかく力がない） | Infraumbilical insufficiency | 腎虚（Kidney deficiency） | 牛車腎気丸・八味地黄丸 |
| 胸脇苦満（肋骨弓下の抵抗・圧痛） | Costal arch resistance | 肝気鬱結（Liver qi stagnation） | 柴胡剤（大柴胡湯等） |
| 心下痞鞕（みぞおちの抵抗感） | Epigastric resistance | 脾胃の滞り（Gastric stagnation） | 六君子湯・半夏瀉心湯 |
| 小腹急結（左下腹部の圧痛） | Left lower abdominal spasm | 血瘀（Blood stasis） | 桃核承気湯・桂枝茯苓丸 |
| 臍周囲に拍動 | Periumbilical pulsation | 水滞（Fluid retention） | 苓桂朮甘湯・五苓散 |

---

## 第4章 整形外科症状別 証判定フロー

### 腰下肢痛・しびれ

```
腰下肢痛・しびれ
│
├─ 高齢者・冷え・夜間頻尿あり・臍下不仁
│   └─ 腎虚（Kidney deficiency）→ 牛車腎気丸
│
├─ 慢性・固定した痛み・夜間増悪・暗紫舌
│   └─ 血瘀（Blood stasis）→ 疎経活血湯
│
├─ 冷えると悪化・温めると楽・白苔
│   └─ 寒証（Cold pattern）→ 桂枝加朮附湯
│
├─ 天気・湿気で悪化・重だるい・歯痕舌
│   └─ 水滞（Fluid retention）→ 薏苡仁湯・防已黄耆湯
│
└─ 疲れると悪化・食欲不振・淡白舌
    └─ 気虚（Qi deficiency）→ 補中益気湯
```

---

### 術後管理

```
術後患者
│
├─ 食欲低下・胃もたれが前景
│   └─ 脾胃虚弱（Gastric weakness）→ 六君子湯
│
├─ 全身倦怠感・疲労が前景
│   └─ 気虚（Qi deficiency）→ 補中益気湯
│
├─ 貧血・体力低下・創傷治癒遅延
│   └─ 気血両虚（Qi-Blood deficiency）→ 十全大補湯
│
├─ 術後浮腫・腫脹（歯痕舌・臍周囲拍動）
│   └─ 水滞（Fluid retention）→ 五苓散
│
└─ フレイル・サルコペニア・意欲低下
    └─ 気血陰虚（Qi-Blood-Yin deficiency）→ 人参養栄湯
```

---

### 冷え・末梢循環

```
冷え・末梢症状
│
├─ 女性・月経痛・下肢しびれ・小腹急結
│   └─ 血瘀（Blood stasis）→ 桂枝茯苓丸
│
├─ 極度の冷え・しもやけ様・細脈
│   └─ 寒凝血瘀（Cold-Blood stasis）→ 当帰四逆加呉茱萸生姜湯
│
├─ 浮腫・肥満・膝痛・歯痕舌
│   └─ 水滞＋気虚 → 防已黄耆湯
│
└─ 天気痛・めまい・頭重・臍周囲拍動
    └─ 水滞（Fluid retention）→ 五苓散
```

---

## 第5章 診断の信頼性と臨床への活かし方

### エビデンスの現状まとめ

| 診察法 | IRR | 臨床的価値 |
|--------|-----|-----------|
| 虚実判定 | 高（AC 0.708）[^2] | **初心者から習得可能・処方の根幹** |
| 寒熱判定 | 中（AC 0.542）[^2] | 問診主体で概ね判定できる |
| 舌診 | 中（一致率 0.52）[^3] | 客観化しやすい・写真記録有用 |
| 腹診 | 中〜高（訓練次第） | Fukushin シミュレーターで習得可能[^6] |
| 脈診 | 低〜中[^4] | 補助的に使用・単独での判定は困難 |
| 気血水判定 | 低（AC 0.254）[^2] | パターン認識として活用 |

**結論：虚実と寒熱を問診＋舌診で判定するだけで、整形外科疾患の8割は対応できる。**

---

## 第6章 最初の1ヶ月でやること

### Step 1（Week 1〜2）：虚実・寒熱だけ問診で判定する

IRR が最も高い2軸に集中する。

1. 「冷えますか？温めると楽になりますか？」→ 寒熱（Kannetsu）
2. 「疲れやすいですか？食欲はありますか？」→ 虚実（Kyojitsu）

### Step 2（Week 3〜4）：舌診を加える

診察のたびに舌を観察する習慣をつける。
まず「淡白か（寒証・虚証） / 紅か（熱証） / 暗紫か（血瘀）」の3択から判断する。

### Step 3（2ヶ月目〜）：腹診の基本1所見を加える

「臍下不仁（臍下が柔らかく力がない）＝腎虚」だけ判定できれば牛車腎気丸の適応が分かる。
整形外科手術後のルーティン腹診から始めると習得しやすい。

---

## 参考文献

[^1]: Use of Kampo Diagnosis in Randomized Controlled Trials of Kampo Products in Japan: A Systematic Review. PMC4132104. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4132104/

[^2]: Maeda-Minami A, et al. Inter-Rater Reliability of Kampo Diagnosis for Chronic Diseases. Altern Ther Health Med. 2021. PMC8290296. https://pmc.ncbi.nlm.nih.gov/articles/PMC8290296/

[^3]: Objective evaluation of tongue diagnosis ability using a tongue diagnosis e-learning/e-assessment system based on a standardized tongue image database. PMC10040798. https://pmc.ncbi.nlm.nih.gov/articles/PMC10040798/

[^4]: Science-Based Medicine. A Misguided Study to Test the Reliability of Traditional Chinese Medicine Pulse Diagnosis. https://sciencebasedmedicine.org/pulse-diagnosis-and-tongue-diagnosis-in-traditional-chinese-medicine-and-a-misguided-study-to-test-the-reliability-of-pulse-diagnosis/

[^5]: Shimada et al. Anatomical factors influencing traditional abdominal examination in Kampo diagnosis: Analysis by computed tomography. Traditional & Kampo Medicine. 2021. https://onlinelibrary.wiley.com/doi/full/10.1002/tkm2.1265

[^6]: Kampo Formula-Pattern Models: The Development of 13 New Clinically Useful Standard Abdominal Pattern Models in the Fukushin Simulator. PMC9106283. https://pmc.ncbi.nlm.nih.gov/articles/PMC9106283/

---

## 推薦学習リソース

- 千福貞博. 実践！漢方診察 脈診・舌診・腹診 基本マスター. 真興交易. ISBN: 9784880025841
- 日本東洋医学会. 漢方専門医制度・研修施設一覧. https://www.jsom.or.jp/
- ツムラ医療関係者向けサイト（医師登録要）. https://www.tsumura.co.jp/
- Frontiers in Pharmacology. Traditional clinical symptoms and signs: Kampo pattern diagnosis in modern gastrointestinal disease. 2024. https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2024.1426491/full
