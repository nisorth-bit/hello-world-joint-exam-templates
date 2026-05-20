# オンラインクリニック

睡眠・男性更年期・女性更年期を三本柱とするオンライン診療クリニックのコンテンツ・企画フォルダ。

## フォルダ構成

```
オンラインクリニック/
├── strategy/          戦略文書・事業計画
├── content/           SEOコンテンツ（ブログ原稿・バックログ）
│   ├── backlogs/      記事バックログ（睡眠73本・男性40本・女性40本）
│   └── drafts/        原稿下書き（sleep/ male/ female/）
├── phase1_mvp/        Phase1：最短検証（LP・問診・プラットフォーム選定）
├── phase2_crm/        Phase2：CRM・継続フォロー・サブスク設計
└── phase3_future/     Phase3：将来内製化検討
```

## フェーズ方針

| フェーズ | 診療インフラ | 自作する部分 |
|---|---|---|
| **Phase1** | 既存プラットフォーム（CLINICS/curon等） | LP・SEO記事・事前問診フォーム |
| **Phase2** | 既存プラットフォーム継続 | マイページ・CRM・継続フォロー・サブスク管理 |
| **Phase3** | 一部内製化 | 予約・決済・患者管理・検査連携 |

詳細は `strategy/platform_strategy.md` 参照。

## コンテンツ現状

- 睡眠ブログ：72本（`content/drafts/sleep/`）
- 男性更年期：40本（`content/drafts/male/`）
- 女性更年期：40本（`content/drafts/female/`）
- 公開記事：`blog-site/src/content/blog/`（Astroビルド）
