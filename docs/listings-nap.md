# Mach Lilies — listings, NAP & off-site entity

How to set up Google Business Profile (GBP), Clutch, Crunchbase and other
directories **consistently**, so Google and AI engines recognise Mach Lilies as
one entity. Off-site consistency is what turns the on-site schema (`#org`) into a
trusted, citable entity — and it is the input for the `sameAs` array we'll add to
the Organization JSON-LD once profiles exist.

> **One rule above all:** copy-paste the *same* details from the canonical block
> below into every profile. Drift ("Mach Lilies" vs "Mach Lilies Ltd" vs
> "MachLilies", different descriptions, different founding years) dilutes the
> entity signal. Pick the values once, use them everywhere.

---

## 1. Canonical identity block (copy-paste source of truth)

These mirror the on-site Organization schema, so on-site and off-site agree.

| Field | Value |
| --- | --- |
| Brand name (use this everywhere) | **Mach Lilies** |
| Legal name | Mach Lilies Limited |
| Also known as | Mach Lilies Consultancy |
| Website | https://machlilies.com |
| Contact email | hey@machlilies.com |
| Tagline | Mach speed. Lily craft. |
| Founded | **2019** |
| Area served | Worldwide (global, remote-first) |
| Logo | https://machlilies.com/assets/logo-mark.svg (PNG: `/assets/icon-512.png`) |
| Share image | https://machlilies.com/assets/og-image.png (1200×630) |
| Founders / team | Kai Krause (CEO), Zach Kosi (CTO), Mo Satoh (Business Development) |

**One-line description (≤160 chars)**
> Independent agentic operations & AI engineering consultancy. We build, govern and operate safe, production-ready AI agents with human oversight and measurable ROI.

**Standard description (1–2 sentences, for most profile bios)**
> Mach Lilies is an independent agentic operations and AI engineering consultancy. We design, deploy, govern and operate safe AI agent workflows for real business processes — with human oversight, monitoring, audit trails and measurable ROI.

**Long description (for Crunchbase / Clutch "about" fields)**
> Mach Lilies is a senior, founder-led agentic operations and AI engineering consultancy. We help companies move beyond AI experiments by designing, deploying, governing and operating AI agents that perform real business workflows — bounded by least-privilege access, human approval and a full audit trail. We sell governed AI operations, not billable hours: the principals who scope the work build and operate it, and hand over clean, documented systems with no lock-in. Most engagements begin with a fixed-scope Agentic Operations Sprint, followed by milestone-based production rollout and optional managed AgentOps support. Mach speed. Lily craft.

**Categories / tags (use the closest available in each platform)**
- Primary intent: *AI consulting · agentic AI · AI agents · AI governance (AgentOps)*
- Crunchbase: Artificial Intelligence, Machine Learning, Consulting, Software, Information Technology
- Clutch/GoodFirms focus areas: Artificial Intelligence, AI Consulting, AI Development, Custom Software Development
- GBP categories (Google's list has no "AI consultant"): primary **Software company**, secondary **Business management consultant** / **Consultant**

---

## 2. A note on "NAP" for a remote business

Classic NAP = **N**ame, **A**ddress, **P**hone. Mach Lilies currently publishes
**no street address and no phone** — it's an email-first, global remote studio.
That's fine, but it changes the playbook:

- For directories, treat the canonical tuple as **Name + Website + Email** (and a
  consistent region/"Remote, Worldwide"). Keep these identical everywhere.
- For **GBP specifically**, Google still needs *either* a physical address *or* a
  defined service area, and usually a phone for verification. Decide §3 first.

**Two decisions only you can make (needed before you publish):**
1. **Phone** — will you publish a business number? GBP verification typically needs
   one. A VoIP/Google Voice number is acceptable if used consistently.
2. **Address / service area** — a registered-office or coworking address (hidden,
   service-area mode) makes GBP far easier. No address = skip GBP, lean on
   Crunchbase/Clutch/LinkedIn instead.

> If you add a phone and/or address anywhere public, send them to me and I'll add
> `telephone` / `address` (PostalAddress) to the Organization schema so on-site and
> off-site still match.

---

## 3. Google Business Profile (GBP)

GBP helps for brand/navigational searches and Maps, but it's built for businesses
with customer contact. For a remote consultancy it's **optional** — do it only if
you'll publish a phone and (ideally) an address.

1. Go to **business.google.com** → *Add your business* → name **Mach Lilies**.
2. Category: primary **Software company** (or **Business management consultant**).
3. "Do you add a location customers can visit?" → **No** → set it up as a
   **service-area business**.
4. Service areas: add the countries/regions you actively serve (Google doesn't do
   literal "Worldwide" — pick your real markets, e.g. United Kingdom, EU, US).
5. Add **website** (`https://machlilies.com`), **email**, and a **phone** for
   verification, **hours**, the **standard description**, and **logo + photos**
   (use `og-image.png` / brand assets).
6. **Verify** — for service-area businesses this is usually video verification
   (record the requested clip) or postcard/phone.
7. After approval: add the same description, a couple of posts, and keep details
   identical to the canonical block.

If you can't/won't publish a phone or address, **skip GBP** — its value here is
marginal compared with the entity directories below.

---

## 4. Directory listings (priority order)

Do them top-to-bottom; the first three matter most for entity recognition and AI
citations. Use the canonical block verbatim each time.

1. **LinkedIn Company Page** *(highest priority — strongest entity + `sameAs`)*
   - linkedin.com/company → create → name **Mach Lilies**, website, tagline,
     standard description, industry "IT Services & IT Consulting" / "Software
     Development", logo. Link the three team members' profiles to the page.
2. **Crunchbase** *(strong signal; Google & AI models read it)*
   - crunchbase.com → *Add a company* → name, website, long description,
     founded year, categories (§1), HQ region (Remote / your city), logo, social
     links, and add Kai/Zach/Mo as people with roles.
3. **Clutch** *(B2B services; review-driven)*
   - clutch.co → *Get Listed* / create vendor profile → company name, website,
     email, founded year, focus areas (AI Consulting / AI Development), min
     project size & rate band, long description, logo. Clutch's value is **verified
     client reviews** — invite real clients only (never fabricate reviews; that
     breaks Google policy and Clutch's).
4. **GitHub organisation** — create/claim a `machlilies` org with the logo, the
   one-line description and the website link (we already reference it in the
   footer once the URL exists).
5. **GoodFirms** and/or **DesignRush** — same B2B profile as Clutch.
6. **Wellfound (AngelList)** — if you hire or raise.
7. **Wikidata item** — once there's enough independent coverage to support
   notability; a Wikidata entry is a powerful entity signal for Google and LLMs.

---

## 5. Accuracy guardrails (don't skip)

Per `docs/seo-strategy.md`, false or unverifiable claims are an E-E-A-T and legal
risk. Before publishing anywhere:

- **Founding year is 2019** (confirmed) — keep it identical on every profile.
- **Don't invent** team credentials, client logos, project counts or review stats.
- Only add **Review/AggregateRating**-type content from real, attributable clients.

---

## 6. After you create the profiles — send me the URLs

Once LinkedIn / Crunchbase / Clutch / GitHub (and GBP, if used) are live, send the
URLs and I'll:

- Add a `sameAs` array to the Organization JSON-LD (`#org`) on every page — the
  link that ties the off-site entity back to the site (a top entity signal).
- Replace the footer social `#` placeholders with the real LinkedIn / X / GitHub links.
- Add `telephone` / `address` to the schema if you decide to publish them.

This is the loop-closer: on-site schema ⇄ consistent off-site profiles ⇄ `sameAs`.
