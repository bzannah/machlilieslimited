# Mach Lilies

Marketing site for **Mach Lilies Limited**, an independent technology consultancy.

> **Mach speed. Lily craft.** — software that moves fast and ages well.

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

- `index.html` — the entire site (self-contained: custom CSS + vanilla JS, no build, no deps).
- `assets/` — bespoke icon, logo, social and media art.
  - `favicon.svg`, `favicon-{16,32,48}.png`, `apple-touch-icon.png`, `icon-{192,512}.png`, `icon-maskable.svg`
  - `logo-mark.svg`, `logo-mark-line.svg`, `logo-lockup.svg`
  - `og-image.png` / `.svg` — 1200×630 social share card
  - `site.webmanifest`
  - `media/` — generative art panels (capabilities, case studies, studio) + `_preview.png` contact sheet
- `tools/` — the asset generators (one source of geometry for every output).

## Regenerating assets

```bash
pip install Pillow
python3 tools/generate_brand_assets.py   # logo, favicon, icons, OG, manifest
python3 tools/generate_media.py          # media art panels + preview sheet
```

SVG is used on-site and by modern browsers; the PNGs are pixel-identical
fallbacks for social sharing, iOS and PWA (which require raster).
