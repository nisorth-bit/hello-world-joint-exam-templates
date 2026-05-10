# 発信サイト（Astro）

`strategy.md` で決めた **Astro + Markdown** の公開用ブログです。

**公開タイミング**：三本柱（睡眠・男性更年期・女性更年期）の核記事が `drafts/sleep/`・`drafts/male/`・`drafts/female/` で揃うまで、**本番デプロイはしない**方針。それまではローカル `npm run dev` と原稿の双方向同期のみ。

## ローカル開発

```bash
cd blog-site
npm install   # 初回のみ
npm run dev
```

## 本番デプロイ（例：Vercel）

1. GitHub にこのリポジトリを push（`blog-site/` はルートの一部として含まれる）
2. Vercel で **Root Directory を `blog-site`** に設定
3. `astro.config.mjs` の `site` を本番 URL（`https://あなたのドメイン`）に変更（OGP・canonical・sitemap に必須）

## 記事の追加

- `src/content/blog/*.md` に frontmatter（`title`, `description`, `pubDate`）付きで保存
- 非公開のたたき台は `経営/オンライン睡眠クリニック/drafts/sleep|male|female/` に置き、公開時にここへコピー

## 公開前チェック

- [ ] `astro.config.mjs` の `site`
- [ ] `src/pages/about.astro` の氏名・所属
- [ ] `src/components/Footer.astro` の著作権表示
- [ ] `src/pages/privacy.astro` の実情に合わせた追記
