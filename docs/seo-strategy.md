# Mach Lilies — SEO & AI-Search (GEO) Strategy

**Goal:** make Mach Lilies the consultancy people *find and trust* when they search
(or ask an AI) for AI & technology consulting.

**Honest framing first.** No one can *guarantee* a #1 Google ranking — it depends
on competition, domain authority, content depth and time, none of which a single
HTML file controls. What we *can* do is make this site technically flawless,
deeply relevant, and trusted — the controllable 100%. Ranking #1 for a head term
like "technology consultancy" is a 12–24 month program of content + authority;
ranking for specific, high-intent terms ("fractional CTO for AI startups",
"LLM consultancy for FinTech") is achievable far sooner. This document covers both.

---

## 1. Audit — current state

### Already strong
- Semantic HTML5, one `<h1>`, sensible heading order, responsive, fast (custom CSS,
  vanilla JS, no framework), HTTPS-ready (GitHub Pages), accessible focus states,
  `prefers-reduced-motion`, no-JS fallback.
- Good `<title>`/description, Open Graph + Twitter cards, full favicon/PWA set,
  bespoke OG share image.

### Fixed in this pass ✅
- **Keyword-aligned `<title>`, meta description, hero copy** ("AI & technology
  consultancy") without losing brand voice.
- **`rel=canonical`**, robots directives (`max-image-preview:large`, etc.), author,
  `og:url`/`og:site_name`/`og:locale`, absolute OG/Twitter image URLs.
- **JSON-LD structured data**: Organization + ProfessionalService, WebSite, WebPage,
  Service OfferCatalog (6 services), BreadcrumbList, **FAQPage**.
- **Visible FAQ section** (8 Q&As) — real, crawlable, query-matched content that
  also feeds FAQ rich results and AI answer engines.
- **`robots.txt`** (explicitly welcomes AI crawlers), **`sitemap.xml`**,
  **`llms.txt`** (AI-search guide), `humans.txt`.
- Image `width`/`height`/`decoding` (reduces CLS), descriptive alt text.
- Analytics + Search Console **scaffold** (inert until you add IDs).

### Deliberately NOT done (and why)
- **No Review/AggregateRating schema.** The on-site testimonials are placeholders.
  Marking up fake reviews violates Google's spam policy and risks a manual penalty.
  Add review markup *only* with real, attributable client reviews. Likewise, make
  sure the stat claims (150+ projects, 98% retention, case-study metrics) are true
  before publishing — false claims are an E-E-A-T and legal risk.

### Biggest remaining gap
- **Content depth.** One page can't rank for many competitive terms. The single
  highest-impact next step is a multi-page content architecture (§4) + an
  insights/blog program (§7). This is recommended but out of scope for this pass.

---

## 2. Action items you must complete (10 min)

1. **Buy/confirm `machlilies.com`** and point it at the host. Enforce **one**
   canonical host (e.g. redirect `www` → apex and `http` → `https`). All tags
   here assume `https://machlilies.com/`.
2. **Google Search Console** + **Bing Webmaster Tools**: verify the domain
   (uncomment the verification `<meta>` in `index.html`), submit `sitemap.xml`.
3. **Google Analytics 4**: replace `G-XXXXXXXXXX` in `index.html` with your
   Measurement ID (the snippet is inert until you do).
4. **Google Business Profile**: create one (even remote-first benefits from it).
5. Replace placeholder **social links** (footer `#`) with real LinkedIn / X /
   GitHub URLs, then add a `sameAs` array to the Organization JSON-LD — this is a
   strong entity signal for both Google and AI engines.

---

## 3. Keyword strategy

Map content to **search intent**, not just volume.

| Tier | Examples | Intent | Where it lives |
| --- | --- | --- | --- |
| Head (hard, long game) | technology consultancy, AI consulting, software consultancy | broad | Home + pillar pages |
| Body (the sweet spot) | AI consultancy for startups, machine learning consulting services, cloud migration consultancy, LLM development company, fractional CTO services | commercial | Dedicated service pages |
| Long-tail (fast wins) | how much does AI consulting cost, generative AI consultant for FinTech, RAG implementation consultant, MLOps consultancy UK | informational/commercial | FAQ + blog posts |
| Brand | Mach Lilies, Mach Lilies consultancy | navigational | Home |

**Clusters (pillar → supporting):**
- **Applied AI** → generative AI, LLM apps, RAG, AI agents, MLOps, AI strategy.
- **Cloud & Platform** → cloud migration, Kubernetes, DevOps, SRE, cost optimisation.
- **Data** → data engineering, warehousing, analytics, real-time pipelines.
- **Product Engineering** → custom software, web/mobile, MVP for startups.
- **Advisory** → fractional CTO, technical due diligence, AI readiness assessment.

Do real keyword research before committing (tools in §10). Prioritise terms where
intent = "hire someone", difficulty is moderate, and you can write the best page
on the internet for it.

---

## 4. Information architecture (recommended next build)

Move from one page to a crawlable, internally-linked structure:

```
/                         Home (overview, trust, CTA)
/services/                Services hub (pillar)
  /services/ai-consulting/
  /services/cloud-platform/
  /services/data-analytics/
  /services/product-engineering/
  /services/strategy-advisory/
/work/                    Case studies index
  /work/<case-study>/     One page per project (real metrics, problem→solution→result)
/about/                   Team, credentials, certifications (E-E-A-T)
/insights/                Blog / articles (topic clusters)
  /insights/<article>/
/contact/
```

Rules: every page = one primary keyword + clear intent, unique title/description,
one `<h1>`, internal links up to its pillar and across to siblings, its own
schema (Service / Article / CaseStudy). Keep URLs short, lowercase, hyphenated.

---

## 5. On-page standards (apply to every page)

- Title ≤ ~60 chars, primary keyword near front, brand at end.
- Meta description ≤ ~155 chars, benefit + soft CTA.
- One `<h1>` with the primary term; `<h2>/<h3>` for subtopics (use natural
  question phrasings — great for featured snippets and AI).
- First 100 words answer "what is this page and who is it for".
- Descriptive, keyword-aware alt text; `width`/`height` on images; lazy-load
  below the fold; modern formats (WebP/AVIF) for any future photography.
- Internal links with descriptive anchor text. No orphan pages.
- Schema per page type.

---

## 6. Technical SEO

- **Core Web Vitals** targets: LCP < 2.5s, INP < 200ms, CLS < 0.1. This site's
  LCP is text (good). Watch: web-font load and the hero canvas. Optimisations:
  trim unused Fraunces weights, `font-display: swap` (done), consider self-hosting
  the woff2 and `<link rel=preload>` for the primary face; keep JS work off the
  main thread / behind `requestIdleCallback`.
- One canonical host; 301 the rest. No mixed content. Valid HTTPS.
- `robots.txt` + XML sitemap submitted; keep `lastmod` honest.
- Structured data: validate at search.google.com/test/rich-results and
  validator.schema.org after every change.
- 404 page; avoid redirect chains; clean, stable URLs.
- Mobile-first: it already is — keep tap targets ≥ 44px, no layout shift.

---

## 7. Content & E-E-A-T (Experience, Expertise, Authority, Trust)

This is what actually moves rankings for a consultancy.

- **Real case studies** with named outcomes (anonymise client if needed, but keep
  the numbers true). Problem → approach → measurable result.
- **Author identity**: real bios for the principals, credentials, photos,
  LinkedIn, `Person` schema, articles bylined by them.
- **Proof**: certifications (ISO 27001, cloud partner badges), logos (with
  permission), genuine testimonials → only then add Review schema.
- **Insights program** (the engine): 2–4 articles/month answering real questions
  in your clusters. Formats that earn links and AI citations:
  - "How to / what is" explainers (snippet + AI bait)
  - Original data / benchmarks / opinionated POV (link bait)
  - Comparisons & buyer's guides ("how to choose an AI consultancy")
  - Case-study deep dives
- Refresh top pages quarterly; freshness matters.

---

## 8. Off-page / authority (the hardest, most decisive lever)

- **Digital PR**: publish original research/benchmarks; pitch to tech press.
- **Guest posts & podcasts** in FinTech/HealthTech/AI communities.
- **Quality directories & profiles**: Clutch, GoodFirms, DesignRush, LinkedIn
  company page, Crunchbase, GitHub org — consistent NAP (name/URL/email).
- **HARO / Featured / Qwoted**: expert quotes → authoritative backlinks.
- **Partnerships**: cloud/AI vendor partner listings link back with authority.
- **Wikidata / Wikipedia** entity (if notability supports it) — huge for being
  recognised as an entity by Google and AI models.
- Avoid paid link schemes / PBNs — penalty risk.

---

## 9. GEO / AEO — the AI-search strategy

Increasingly, buyers ask ChatGPT, Perplexity, Claude and Google AI Overviews
"who's the best AI consultancy for X". Optimise to be the **cited** answer.

**Implemented here:**
- `llms.txt` summarising the firm, services, proof and contact for LLMs.
- `robots.txt` explicitly allows GPTBot, ClaudeBot, PerplexityBot, Google-Extended,
  Applebot-Extended, CCBot, OAI-SearchBot.
- Rich JSON-LD entity graph + FAQPage so machines parse facts unambiguously.
- FAQ written as direct question→concise answer (the format LLMs lift).
- Consistent entity naming, slogan, email, service list across page, schema, llms.txt.

**Ongoing:**
- **Be quotable**: lead answers with a one-sentence definition, then detail.
  Use clear stats, lists, and tables — AI engines extract these.
- **Get mentioned off-site**: AI models cite sources they see across the web
  (directories, press, Reddit, comparison posts). Off-page (§8) *is* AI SEO.
- **Entity consistency**: same NAP + description everywhere; build the Wikidata item.
- **Comparison/listicle content** ("top AI consultancies for startups") — the
  pages AI engines summarise for recommendation queries.
- **Statistics/benchmark pages** that others (and AIs) cite.
- Track AI visibility: periodically ask the major assistants the target questions
  and log whether/how Mach Lilies appears; tools like Profound/Peec/Otterly emerging.

---

## 10. Measurement & tooling

- **Free/core**: Google Search Console, Bing Webmaster, GA4, Google Rich Results
  Test, schema.org validator, PageSpeed Insights / Lighthouse, Google Trends.
- **Research/rank (paid)**: Ahrefs or Semrush (keywords, competitors, backlinks,
  rank tracking) — pick one.
- **KPIs**: organic clicks & impressions (GSC), keyword rankings, indexed pages,
  Core Web Vitals pass rate, referring domains, conversions (enquiries), and
  **AI citations/mentions**.

---

## 11. Roadmap

**Now (done this pass):** technical on-page SEO, schema, FAQ, robots/sitemap/llms.txt.

**Week 1 (you):** domain live + canonical host enforced; GSC/Bing verified + sitemap
submitted; GA4 live; GBP + directory profiles; real social links + `sameAs`.

**30 days:** keyword research; write 5 service pages + 1 pillar; publish 3 case
studies with real numbers; first 3 insight articles; start directory backlinks.

**90 days:** 8–12 insight articles across clusters; digital-PR push (1 original
research piece); 10+ quality referring domains; author bios + Person schema;
begin comparison/AEO content; review GSC and double down on what's ranking.

**Ongoing:** 2–4 articles/month, quarterly refresh of top pages, monthly backlink
outreach, monthly rank + AI-citation review.
