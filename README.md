# Mach Lilies

Marketing site for **Mach Lilies Limited**, an independent **agentic operations &
AI engineering consultancy**. We design, deploy, govern and operate safe AI agent
workflows that perform real business processes — with human oversight, audit-ready
governance and measurable ROI.

> **Mach speed. Lily craft.** — safe AI agents that do real business work.

## Brand system

A bespoke, single-source identity. Everything derives from one geometric idea —
**The Mach Lily**: a two-whorl botanical bloom (3 outer + 3 inner recurved
petals) tilted into motion. Mach (velocity) × Lilies (rare, elegant craft).

| Token | Value |
| --- | --- |
| Ink (canvas) | `#0d0c0a` |
| Bone (type) | `#f1ebdc` |
| Accent (velocity + stem) | `#c9f24c` |
| Display / Body / Mono | Fraunces · Inter · Space Mono |

## Files

- `index.html` — the homepage (self-contained: shared CSS + vanilla JS, no build, no deps).
- `services/<slug>/index.html` — service & offer pages. **Generated** — do not hand-edit; edit the
  data + template in `tools/generate_service_pages.py` and regenerate. Slugs:
  - Agentic offers: `agentic-operations`, `agentops-ai-governance`, `ai-pilot-rescue`,
    `ai-assurance-evaluation`, `ai-modernisation-factory`, and the flagship `agentic-operations-sprint`.
  - Engineering bench: `ai-consulting`, `product-engineering`, `cloud-platform`,
    `data-analytics`, `design-experience`, `strategy-advisory`.
- `assets/` — shared `css/site.css`, `js/site.js`, plus bespoke icon, logo, social and media art.
  - `favicon.svg`, `favicon-{16,32,48}.png`, `apple-touch-icon.png`, `icon-{192,512}.png`, `icon-maskable.svg`
  - `logo-mark.svg`, `logo-mark-line.svg`, `logo-lockup.svg`
  - `og-image.png` / `.svg` — 1200×630 social share card
  - `site.webmanifest`
  - `media/` — generative art panels (capabilities, workflows, studio) + `_preview.png` contact sheet
- `sitemap.xml`, `robots.txt`, `llms.txt`, `humans.txt` — crawl, SEO and AI-search (GEO) files.
- `tools/` — generators: `generate_service_pages.py` (service/offer pages) and the asset generators.

## Regenerating

```bash
python3 tools/generate_service_pages.py   # all /services/<slug>/index.html pages

pip install Pillow
python3 tools/generate_brand_assets.py    # logo, favicon, icons, OG, manifest
python3 tools/generate_media.py           # media art panels + preview sheet
```

SVG is used on-site and by modern browsers; the PNGs are pixel-identical
fallbacks for social sharing, iOS and PWA (which require raster).
