#!/usr/bin/env python3
"""
Mach Lilies — service page generator.

One audited template + per-service content => six consistent, SEO-complete,
internally-linked service pages. Each page is unique (distinct copy, services,
method, FAQs) to avoid duplicate content, and carries Service + FAQPage +
BreadcrumbList + WebPage + Organization JSON-LD.

Run:  python3 tools/generate_service_pages.py
"""
import os, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://machlilies.com"

def esc(s): return html.escape(s, quote=False)

# short name + blurb for the "Related services" mesh
SHORT = {
    "ai-consulting":       ("AI Consulting", "AI, LLM and machine-learning systems, strategy to production."),
    "product-engineering": ("Product Engineering", "Custom web & mobile software, built to scale."),
    "cloud-platform":      ("Cloud & Platform", "Cloud-native architecture, DevOps and reliability."),
    "data-analytics":      ("Data & Analytics", "Pipelines, warehousing and analytics you can act on."),
    "design-experience":   ("Design & Experience", "Product UX/UI, design systems, brand and motion."),
    "strategy-advisory":   ("Strategy & Advisory", "Fractional CTO, due diligence and technology strategy."),
}
ORDER = ["ai-consulting", "product-engineering", "cloud-platform", "data-analytics", "design-experience", "strategy-advisory"]

SERVICES = {
"ai-consulting": {
  "title": "AI Consulting Services — Mach Lilies",
  "desc": "AI consulting that ships. Mach Lilies designs, builds and operates AI, LLM and machine-learning systems in production — from AI strategy to MLOps. Free first consultation.",
  "keywords": "AI consulting, AI consultancy, AI consulting services, machine learning consulting, LLM development, generative AI consultant, RAG, MLOps, AI strategy",
  "service_type": "AI and machine learning consulting",
  "eyebrow": "AI & Machine Learning Consulting",
  "h1": ("AI consulting,", "engineered into production."),
  "lead": "Mach Lilies is an independent <strong>AI consultancy</strong> that takes artificial intelligence from idea to impact. We design the strategy, build the LLM and machine-learning systems, and operate them in production — so your AI doesn't stall as a demo. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "What is AI consulting",
  "ov_hl": 'AI consulting turns <span class="hl">artificial intelligence</span> into outcomes — <span class="dim">strategy, build, and run</span>, not just slideware.',
  "ov_body": "Most AI projects die between the proof of concept and production. We exist to close that gap. As a senior, founder-led AI and machine-learning consultancy, Mach Lilies helps startups and enterprises find the use cases that pay off, build generative-AI, LLM and ML systems that work under real load, and operate them with proper MLOps. Every engagement is staffed by principals and handed off as clean, documented systems you own.",
  "svc_h2": ("AI services,", "end to end."),
  "svc_note": "From generative AI and LLM apps to custom machine learning and MLOps — engaged together or à la carte.",
  "services": [
    ("Generative AI & LLM apps", "Production LLM applications — copilots, assistants, and document and content workflows — built on Claude, GPT and open-source models.", ["LLMs","Copilots","GenAI"]),
    ("RAG & knowledge systems", "Retrieval-augmented generation over your own data: vector search, grounding, evaluation and guardrails that keep answers accurate.", ["RAG","Vector DB","Embeddings"]),
    ("AI agents & automation", "Tool-using agents and workflow automation that take real actions safely — with the right human-in-the-loop controls.", ["Agents","Tools","Workflows"]),
    ("Custom machine learning", "Bespoke ML where it beats an LLM: forecasting, recommendation, classification, computer vision and NLP.", ["ML","Forecasting","CV / NLP"]),
    ("Data & ML pipelines (MLOps)", "The backbone that keeps AI working: pipelines, feature stores, training, deployment, evaluation, monitoring and cost control.", ["MLOps","Pipelines","Monitoring"]),
    ("AI strategy & readiness", "Where AI actually pays off: opportunity mapping, data readiness, build-vs-buy, roadmaps and technical due diligence.", ["Strategy","Roadmap","Due diligence"]),
  ],
  "method_h2": ("From idea", "to MLOps."),
  "method_note": "Four movements that take AI from a hypothesis to a system that keeps earning its keep.",
  "method": [
    ("01 / Assess","Find the value","Identify the highest-value, lowest-risk AI use cases and validate data and feasibility."),
    ("02 / Prototype","Prove it fast","A working proof of concept in weeks, evaluated against real metrics — not a slideshow."),
    ("03 / Productionize","Build for keeps","Engineer it to production: tested, observable, secure, scalable and documented."),
    ("04 / Operate","Keep it sharp","MLOps: monitoring, evaluation, retraining and cost control so quality holds over time."),
  ],
  "ind_h2": ("AI for", "real industries."),
  "ind_note": "We ship AI for regulated, high-stakes domains — for both venture-backed startups and enterprises.",
  "industries": ["FinTech","HealthTech","Logistics","Retail & Commerce","B2B SaaS","Startups","Enterprise"],
  "why": [
    ("i","Senior, founder-led","The principals who scope your AI are the ones who build it. No hand-off to juniors."),
    ("ii","Production-first","We optimise for systems that survive real users and real load — not demo-day theatre."),
    ("iii","Model-agnostic","Claude, GPT, or open-source — we pick on cost, privacy and fit, never vendor loyalty."),
    ("iv","Yours to own","Clean, documented, no lock-in. We engineer our own hand-off and your team inherits it."),
  ],
  "proof_hl": 'AI that shipped: <span class="hl">+450% ROI</span>, <span class="hl">−60% wait times</span>, <span class="hl">+28% margin.</span>',
  "faq_h2": ("AI consulting,", "answered."),
  "faqs": [
    ("What is AI consulting?", "AI consulting is the practice of helping an organisation identify, design, build and operate artificial-intelligence and machine-learning systems that deliver measurable business value. A good AI consultancy covers the full path — from strategy and feasibility through to production engineering and ongoing MLOps — not just slideware or one-off demos."),
    ("What AI consulting services does Mach Lilies offer?", "We offer generative-AI and LLM application development, retrieval-augmented generation (RAG) and knowledge systems, AI agents and automation, custom machine-learning models, data and ML pipelines with MLOps, and AI strategy and readiness assessments."),
    ("How much does AI consulting cost?", "It depends on scope. Most engagements begin with a free consultation and a short, fixed-fee discovery to validate the use case, followed by milestone-based delivery priced to outcomes rather than headcount. Contact us for a tailored quote."),
    ("How long does an AI project take?", "A working prototype is usually weeks, not months. Production-grade deployment depends on data readiness, integration and compliance, but our model is to ship something real early and harden it iteratively."),
    ("Which AI models and providers do you work with?", "We are model-agnostic. We build with leading frontier models such as Anthropic Claude and OpenAI GPT, and with open-source models like Llama and Mistral when they fit better on cost, privacy or control. We recommend the right tool for the job rather than a single vendor."),
    ("Should I use RAG or fine-tuning?", "Most use cases that need current, proprietary or factual knowledge are best served by retrieval-augmented generation (RAG), which grounds the model in your data. Fine-tuning helps for fixed style, format or narrow tasks. We often combine both — and will advise based on your data and goals."),
    ("Is our data kept secure and private?", "Yes. We design for data privacy and security from the start — including private deployments, isolation of sensitive data, and provider options that do not train on your data. We work to enterprise-grade standards and align with frameworks such as ISO 27001."),
    ("Do you offer AI strategy, or only build?", "Both. We can run an AI readiness and opportunity assessment, advise on build-vs-buy and roadmaps, or act as a fractional AI/engineering leader — and we can take any of it through to production and operation."),
  ],
  "contact_h2": ("Put AI", "to work."),
  "contact_sub": "Tell us what you're building. We reply to every serious enquiry within one business day — and the first consultation is free.",
},

"product-engineering": {
  "title": "Product Engineering & Custom Software — Mach Lilies",
  "desc": "Custom software engineering from Mach Lilies — full-stack web and mobile products built to scale and engineered to last. From startup MVP to enterprise platform. Free consultation.",
  "keywords": "custom software development, product engineering, MVP development, web app development, mobile app development, software consultancy, full-stack development",
  "service_type": "Custom software engineering",
  "eyebrow": "Product & Software Engineering",
  "h1": ("Custom software,", "built to last."),
  "lead": "Mach Lilies is a <strong>product engineering</strong> studio that turns ambitious ideas into production software. We design and build full-stack web and mobile products — from a startup's first MVP to an enterprise platform — engineered to scale and made to last. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "What is product engineering",
  "ov_hl": 'Most software is <span class="dim">disposable</span>. We build the kind <span class="hl">worth keeping.</span>',
  "ov_body": "Product engineering is more than writing code — it's owning the outcome: the architecture, the build, the quality and the scale. As a senior, founder-led software consultancy, Mach Lilies designs and ships full-stack web and mobile products that are fast to release and honest under load. We move at startup speed without leaving behind the technical debt you'll regret.",
  "svc_h2": ("What we", "build."),
  "svc_note": "Full-stack web and mobile, APIs, MVPs and platform scale — engaged together or à la carte.",
  "services": [
    ("Web platforms", "Modern, fast web applications with frameworks like React and Next.js, solid back ends and APIs that scale.", ["Web","React","Next.js"]),
    ("Mobile apps", "Native and cross-platform iOS and Android apps with a shared, maintainable codebase.", ["iOS","Android","Cross-platform"]),
    ("APIs & integrations", "Clean, documented APIs and third-party integrations that don't break in production.", ["APIs","Integrations","Webhooks"]),
    ("MVPs for startups", "From zero to a fundable, real product in weeks — without the debt you'll regret later.", ["MVP","0→1","Startups"]),
    ("Platform & scale", "Re-architecting and hardening products for growth, performance and reliability.", ["Scale","Performance","Refactor"]),
    ("Quality & delivery", "Automated testing, CI/CD and observability baked in from day one — not bolted on.", ["Testing","CI/CD","Observability"]),
  ],
  "method_h2": ("From idea", "to product."),
  "method_note": "No theatre. Four movements from first call to a product your team can own and grow.",
  "method": [
    ("01 / Discover","Frame the problem","We understand the business and users before a line of code — the right question is half the build."),
    ("02 / Design","Prototype fast","Working prototypes in weeks, not slideware in months. We make ideas tangible early."),
    ("03 / Build","Ship for keeps","Production-grade from day one — tested, observable and documented for the team that inherits it."),
    ("04 / Scale","Harden & hand off","We harden, scale and transfer ownership. Success is when you no longer need us."),
  ],
  "ind_h2": ("Software for", "real industries."),
  "ind_note": "We build for regulated, high-stakes domains — for both venture-backed startups and enterprises.",
  "industries": ["FinTech","HealthTech","Logistics","Retail & Commerce","B2B SaaS","Startups","Enterprise"],
  "why": [
    ("i","Senior, end to end","Principals build your product — the people who pitch are the people who ship."),
    ("ii","Production-first","Tested, observable, documented. Built for real users, not a demo."),
    ("iii","Modern, pragmatic stack","Proven tools chosen for fit and longevity, not hype."),
    ("iv","Yours to own","Clean code, full documentation, no lock-in. Your team inherits it cleanly."),
  ],
  "proof_hl": 'Shipped: <span class="hl">50K+ users</span>, <span class="hl">40ms p99</span>, <span class="hl">99.99% uptime.</span>',
  "faq_h2": ("Product engineering,", "answered."),
  "faqs": [
    ("What is product engineering?", "Product engineering is the end-to-end design and build of software products — owning architecture, development, quality and scale, not just writing features. It blends engineering, product thinking and design to ship software that works in the real world and keeps working."),
    ("How is Mach Lilies different from a typical dev agency?", "We're a small, senior studio: the principals who scope your product build it. We optimise for production quality and long-term ownership rather than billable hours, and we engineer a clean hand-off so you're never locked in."),
    ("Can you build an MVP for my startup?", "Yes. We specialise in taking startups from zero to a fundable, real product in weeks — fast, but without the technical debt that slows you down later."),
    ("What technology stack do you use?", "We're pragmatic: typically TypeScript with React/Next.js on the front end, robust back ends (Node, Python, Go) and cloud-native infrastructure. We choose tools for fit and longevity, not hype."),
    ("Do you build both web and mobile?", "Yes — modern web applications and native or cross-platform mobile apps, often sharing logic across a maintainable codebase."),
    ("Will I own the code?", "Always. You own all code and IP, with full documentation and no lock-in. We engineer our own hand-off."),
    ("How do you ensure quality?", "Automated testing, CI/CD, code review and observability are part of every build from day one — so quality is designed in, not inspected at the end."),
  ],
  "contact_h2": ("Build your", "product."),
  "contact_sub": "Tell us what you're building. We reply to every serious enquiry within one business day — and the first consultation is free.",
},

"cloud-platform": {
  "title": "Cloud & Platform Engineering Consulting — Mach Lilies",
  "desc": "Cloud consulting from Mach Lilies — cloud-native architecture, migration, Kubernetes, DevOps and SRE. Reliable, cost-efficient platforms across AWS, GCP and Azure. Free consultation.",
  "keywords": "cloud consulting, cloud migration, Kubernetes consulting, DevOps consulting, cloud architecture, SRE, infrastructure as code, cloud cost optimization",
  "service_type": "Cloud architecture and DevOps consulting",
  "eyebrow": "Cloud & Platform Engineering",
  "h1": ("Cloud platforms,", "reliable by design."),
  "lead": "Mach Lilies is a <strong>cloud consultancy</strong> that designs, builds and runs cloud-native platforms. From migration and Kubernetes to DevOps, reliability and cost control — infrastructure you can sleep through. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "What is cloud consulting",
  "ov_hl": 'Cloud done right is <span class="hl">invisible</span> — fast, resilient, and <span class="dim">quietly affordable.</span>',
  "ov_body": "Cloud consulting is about more than lifting servers — it's architecting platforms that scale, stay up, and don't quietly drain your budget. As a senior, vendor-neutral cloud and platform consultancy, Mach Lilies designs cloud-native systems on AWS, GCP and Azure, automates them with infrastructure-as-code, and operates them with real reliability engineering.",
  "svc_h2": ("What we", "engineer."),
  "svc_note": "Architecture, migration, Kubernetes, DevOps, reliability and cost — engaged together or à la carte.",
  "services": [
    ("Cloud architecture", "Well-architected, cloud-native systems on AWS, GCP or Azure — designed for scale and resilience.", ["AWS","GCP","Azure"]),
    ("Cloud migration", "Move to the cloud, or between clouds, without the downtime horror stories.", ["Migration","Re-platform","Lift & shift"]),
    ("Kubernetes & containers", "Production Kubernetes, service mesh and container platforms that teams can actually run.", ["Kubernetes","Docker","Helm"]),
    ("DevOps & CI/CD", "Pipelines, infrastructure-as-code and golden paths your engineers will actually use.", ["IaC","Terraform","CI/CD"]),
    ("Reliability (SRE)", "SLOs, observability, incident response and resilience engineering for uptime that holds.", ["SRE","SLOs","Observability"]),
    ("Cost optimization", "FinOps that cuts cloud spend without cutting performance — often paying for itself.", ["FinOps","Cost","Efficiency"]),
  ],
  "method_h2": ("From audit", "to autopilot."),
  "method_note": "Four movements from a cloud you worry about to one that runs itself.",
  "method": [
    ("01 / Assess","Audit & plan","We map your current state, risks and costs, and agree a clear, sequenced plan."),
    ("02 / Architect","Design it right","Cloud-native architecture for scale, resilience and security — documented, not improvised."),
    ("03 / Build","Automate everything","Infrastructure-as-code, CI/CD and golden paths so changes are safe and repeatable."),
    ("04 / Operate","Run with SRE","Observability, SLOs and FinOps so the platform stays reliable and affordable."),
  ],
  "ind_h2": ("Platforms for", "real industries."),
  "ind_note": "We build cloud platforms for regulated, high-traffic domains — startups and enterprises alike.",
  "industries": ["FinTech","HealthTech","Logistics","Retail & Commerce","B2B SaaS","Startups","Enterprise"],
  "why": [
    ("i","Senior, founder-led","Principals architect and build your platform — no hand-off to juniors."),
    ("ii","Vendor-neutral","AWS, GCP or Azure — we recommend what fits, not what we resell."),
    ("iii","Reliability-obsessed","We design for the 3am page you'll never get. Uptime is a feature."),
    ("iv","Yours to own","IaC, runbooks and docs handed over — your team can operate it without us."),
  ],
  "proof_hl": 'In production: <span class="hl">99.99% uptime</span>, <span class="hl">−31% run cost</span>, <span class="hl">9.2M jobs/day.</span>',
  "faq_h2": ("Cloud consulting,", "answered."),
  "faqs": [
    ("What is cloud consulting?", "Cloud consulting helps an organisation design, migrate to, build on and operate cloud platforms (AWS, GCP, Azure) that are scalable, reliable, secure and cost-efficient. It spans architecture, migration, DevOps and site reliability engineering."),
    ("Which cloud should we use — AWS, GCP or Azure?", "It depends on your workloads, team and existing commitments. We're vendor-neutral and will recommend the best fit — or a multi-cloud approach — rather than defaulting to one provider."),
    ("Can you migrate us with minimal downtime?", "Yes. We plan migrations carefully — assessing dependencies, sequencing moves and using techniques like phased cutovers and dual-running — to minimise or eliminate downtime."),
    ("Do we actually need Kubernetes?", "Not always. Kubernetes is powerful but adds operational overhead. We'll recommend it only when your scale and team justify it, and otherwise pick simpler, cheaper options."),
    ("How do you reduce our cloud costs?", "Through FinOps: right-sizing, autoscaling, eliminating waste, smarter storage and commitment planning — typically cutting spend significantly without hurting performance."),
    ("What is SRE?", "Site Reliability Engineering applies engineering discipline to operations — defining SLOs, building observability, automating toil and improving resilience so systems stay reliable as they grow."),
    ("Will you hand over runbooks and documentation?", "Yes. We deliver infrastructure-as-code, runbooks and documentation so your team can operate the platform confidently without depending on us."),
  ],
  "contact_h2": ("Engineer your", "platform."),
  "contact_sub": "Tell us about your infrastructure. We reply to every serious enquiry within one business day — and the first consultation is free.",
},

"data-analytics": {
  "title": "Data Engineering & Analytics Consulting — Mach Lilies",
  "desc": "Data consulting from Mach Lilies — data engineering, pipelines, warehousing, analytics and BI that turn raw data into decisions, and the foundation your AI needs. Free consultation.",
  "keywords": "data engineering consulting, data analytics consulting, data pipeline, data warehouse, business intelligence, real-time data, analytics, data platform",
  "service_type": "Data engineering and analytics consulting",
  "eyebrow": "Data Engineering & Analytics",
  "h1": ("Data you can", "act on."),
  "lead": "Mach Lilies is a <strong>data consultancy</strong> that builds the pipelines, warehouses and analytics that turn raw data into decisions — and the clean foundation your AI needs. From real-time ingestion to dashboards people trust. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "What is data engineering",
  "ov_hl": 'Raw data is noise. We turn it into <span class="hl">insight you can act on</span> — <span class="dim">reliably.</span>',
  "ov_body": "Data engineering builds the plumbing — pipelines, warehouses and models — that makes analytics and AI possible; analytics turns that data into decisions. As a senior data consultancy, Mach Lilies designs modern data platforms (Snowflake, BigQuery, Databricks), builds trustworthy pipelines, and delivers analytics people actually use — including the AI-ready data foundation modern ML depends on.",
  "svc_h2": ("What we", "build."),
  "svc_note": "Pipelines, warehouses, analytics and governance — engaged together or à la carte.",
  "services": [
    ("Data pipelines", "Reliable batch and streaming pipelines (ELT) you can trust to be correct and on time.", ["ELT","Airflow","dbt"]),
    ("Data warehousing", "Modern warehouses and lakehouses — Snowflake, BigQuery, Databricks — modeled well.", ["Snowflake","BigQuery","Lakehouse"]),
    ("Analytics & BI", "Dashboards and self-serve analytics people actually use to make decisions.", ["BI","Dashboards","Metrics"]),
    ("Real-time & streaming", "Event pipelines for sub-second insight and operational analytics.", ["Streaming","Kafka","Real-time"]),
    ("Data platform & governance", "Quality, lineage, cataloguing and governance that scale with the organisation.", ["Quality","Lineage","Governance"]),
    ("AI-ready data", "The clean, well-modeled data foundation that AI and ML actually need to work.", ["ML data","Features","Foundation"]),
  ],
  "method_h2": ("From raw", "to decisions."),
  "method_note": "Four movements from scattered data to a platform that drives decisions and AI.",
  "method": [
    ("01 / Map","Audit the data","We map sources, quality and the questions the business actually needs answered."),
    ("02 / Model","Design the platform","A warehouse and data model built for trust, performance and change."),
    ("03 / Build","Pipe it reliably","Tested pipelines with quality checks so the numbers are right, every time."),
    ("04 / Activate","Insight & AI","Analytics, dashboards and the data foundation your ML and AI build on."),
  ],
  "ind_h2": ("Data for", "real industries."),
  "ind_note": "We build data platforms for regulated, high-volume domains — startups and enterprises alike.",
  "industries": ["FinTech","HealthTech","Logistics","Retail & Commerce","B2B SaaS","Startups","Enterprise"],
  "why": [
    ("i","Senior, founder-led","Principals design and build your data platform — no hand-off to juniors."),
    ("ii","Modern stack","dbt, Snowflake, BigQuery, Databricks — the proven modern data stack, done right."),
    ("iii","Decision-focused","We start from the decisions you need to make, then build backward to the data."),
    ("iv","Yours to own","Documented, tested, governed. Your team owns and trusts the platform."),
  ],
  "proof_hl": 'Delivered: <span class="hl">9.2M events/day</span>, <span class="hl">+28% margin</span>, <span class="hl">6→1 tools merged.</span>',
  "faq_h2": ("Data consulting,", "answered."),
  "faqs": [
    ("What is data engineering?", "Data engineering is the design and build of the systems that collect, move, store and prepare data — pipelines, warehouses and models — so it's reliable and ready for analytics and AI. It's the foundation everything data-driven stands on."),
    ("What's the difference between data engineering and analytics?", "Data engineering builds the trustworthy data foundation; analytics (and BI) turns that data into insight and decisions. We do both, so the two fit together cleanly."),
    ("Which data warehouse should we use?", "It depends on your scale, ecosystem and team. We're neutral across Snowflake, BigQuery and Databricks and will recommend the best fit rather than a default."),
    ("Do we need real-time or is batch enough?", "Most reporting is well served by batch. Real-time matters when decisions are operational and time-sensitive. We'll recommend the simplest approach that meets the need."),
    ("How do you ensure data quality?", "With testing, validation, monitoring and lineage built into the pipelines (using tools like dbt) — so issues are caught early and the numbers can be trusted."),
    ("Can you make our data AI-ready?", "Yes. A clean, well-modeled, well-governed data foundation is exactly what AI and ML need. We build that foundation and connect it to our AI consulting work."),
    ("Do you build dashboards and BI?", "Yes — we deliver dashboards and self-serve analytics designed for adoption, so people actually use them to make decisions."),
  ],
  "contact_h2": ("Put your data", "to work."),
  "contact_sub": "Tell us about your data. We reply to every serious enquiry within one business day — and the first consultation is free.",
},

"design-experience": {
  "title": "Product Design & UX/UI Services — Mach Lilies",
  "desc": "Product design from Mach Lilies — UX/UI, design systems, brand and motion for digital products. Interfaces that feel inevitable, designed to ship. Free consultation.",
  "keywords": "product design agency, UX/UI design services, design systems, brand design, digital product design, motion design, design engineering",
  "service_type": "Product and experience design",
  "eyebrow": "Design & Experience",
  "h1": ("Interfaces that feel", "inevitable."),
  "lead": "Mach Lilies designs <strong>digital products</strong> people love to use — product UX/UI, design systems, brand and motion. Beautiful, yes, but also usable, accessible and engineered to ship. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "What is product design",
  "ov_hl": 'The best interface is the one users <span class="hl">forget they\'re using.</span>',
  "ov_body": "Product design is where usefulness meets craft — the flows, the interface, the brand and the motion that make a product feel inevitable. As a senior design and experience studio that also engineers, Mach Lilies designs digital products that are beautiful and usable, grounded in research and built as systems — then bridges design and code so the build matches the vision.",
  "svc_h2": ("What we", "design."),
  "svc_note": "Product UX/UI, design systems, brand, motion and research — engaged together or à la carte.",
  "services": [
    ("Product (UX/UI) design", "End-to-end product design — from user flows to polished, production-ready interfaces.", ["UX","UI","Product"]),
    ("Design systems", "Scalable, documented component systems your engineers actually love to build with.", ["Systems","Components","Tokens"]),
    ("Brand & identity", "Distinctive visual identity and brand systems — like the one you're looking at.", ["Brand","Identity","Logo"]),
    ("Motion & interaction", "Micro-interactions and motion that make products feel alive and responsive.", ["Motion","Interaction","Prototyping"]),
    ("UX research", "Talk to users; design on evidence, not opinion — testing, interviews and synthesis.", ["Research","Testing","Discovery"]),
    ("Design engineering", "We bridge design and code, so the shipped product matches the designed vision.", ["Front-end","Design eng","Handoff"]),
  ],
  "method_h2": ("From insight", "to interface."),
  "method_note": "Four movements from understanding users to an interface that ships and scales.",
  "method": [
    ("01 / Understand","Research first","We learn the users and the goals — design follows evidence, not assumptions."),
    ("02 / Explore","Concept widely","Diverge on directions and prototype the promising ones quickly."),
    ("03 / Design","Systemise it","Polished interfaces built as a reusable, documented system — not one-off screens."),
    ("04 / Ship","Build with eng","We bridge to engineering so the build matches the vision, pixel for pixel."),
  ],
  "ind_h2": ("Design for", "real industries."),
  "ind_note": "We design products for complex, high-stakes domains — for startups and enterprises alike.",
  "industries": ["FinTech","HealthTech","Logistics","Retail & Commerce","B2B SaaS","Startups","Enterprise"],
  "why": [
    ("i","Senior designers","Experienced product designers do the work — no hand-off to juniors."),
    ("ii","Design + engineering","Under one roof, so designs are buildable and builds stay faithful."),
    ("iii","Accessible by default","WCAG-aware, usable for everyone — accessibility designed in, not bolted on."),
    ("iv","Yours to own","Source files, design systems and documentation handed over cleanly."),
  ],
  "proof_hl": 'Designed to perform: <span class="hl">4.9★ rating</span>, <span class="hl">−60% wait time</span>, <span class="hl">loved daily.</span>',
  "faq_h2": ("Product design,", "answered."),
  "faqs": [
    ("What does a product design agency do?", "A product design agency designs digital products end to end — user research, UX flows, UI design, design systems, brand and motion — so a product is both usable and desirable, and ready to build."),
    ("What's the difference between UX and UI?", "UX (user experience) is how a product works — the flows, structure and usability. UI (user interface) is how it looks and feels — the visual and interactive layer. Great products need both, designed together."),
    ("What is a design system?", "A design system is a documented library of reusable components, patterns and tokens that keeps a product consistent and lets teams build faster. We design systems engineers love to use."),
    ("Do you do branding too?", "Yes — visual identity, logo and brand systems. The identity on this very site is an example of our brand work."),
    ("Do you only design, or also build?", "Both. We're a design studio that also engineers, so we can take a product from research and design through to a faithful, shipped build."),
    ("Is accessibility included?", "Yes. We design to accessibility standards (WCAG) by default, so products are usable by as many people as possible."),
    ("How do you hand off to engineers?", "We deliver clean source files, a documented design system and design-engineering support — and often build the front end ourselves, so nothing is lost in translation."),
  ],
  "contact_h2": ("Design something", "rare."),
  "contact_sub": "Tell us what you're designing. We reply to every serious enquiry within one business day — and the first consultation is free.",
},

"strategy-advisory": {
  "title": "Technology Strategy & Fractional CTO — Mach Lilies",
  "desc": "Technology strategy and advisory from Mach Lilies — fractional CTO, technical due diligence, AI readiness and roadmaps. Senior, operator-led guidance when it counts. Free consultation.",
  "keywords": "technology consulting, fractional CTO, technical due diligence, technology strategy, AI readiness, CTO as a service, technology advisory, architecture review",
  "service_type": "Technology strategy and advisory",
  "eyebrow": "Strategy & Advisory",
  "h1": ("Senior guidance,", "when it counts."),
  "lead": "Mach Lilies provides <strong>technology strategy and advisory</strong> for founders, investors and leaders — fractional CTO leadership, technical due diligence, AI readiness and roadmaps. Clarity from people who have actually built the thing. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "What is technology advisory",
  "ov_hl": 'Decisions are cheap to make and <span class="hl">expensive to get wrong.</span>',
  "ov_body": "Technology strategy and advisory is senior, operator-level guidance for the decisions that matter — what to build, whether to buy, how to scale, and who to hire. As a founder-led practice, Mach Lilies acts as a fractional CTO, runs technical due diligence for investors, and turns ambition into sequenced, fundable roadmaps. Candid advice from people who have built and run the systems, not just advised on them.",
  "svc_h2": ("How we", "advise."),
  "svc_note": "Fractional leadership, due diligence, roadmaps and reviews — engaged together or à la carte.",
  "services": [
    ("Fractional CTO", "Senior technical leadership, part-time, for startups and scale-ups that aren't ready for a full-time CTO.", ["Fractional","Leadership","CTO"]),
    ("Technical due diligence", "For investors: assess a target's technology, team and risk before you commit capital.", ["Due diligence","Investors","Risk"]),
    ("Technology roadmaps", "Turn ambition into a sequenced, fundable plan your team and board can rally behind.", ["Roadmap","Planning","Strategy"]),
    ("AI readiness", "Where AI pays off, what's needed, and a realistic path to get there.", ["AI readiness","Assessment","Strategy"]),
    ("Architecture review", "A senior second opinion on your system, scaling plan and key technical bets.", ["Architecture","Review","Scaling"]),
    ("Team & hiring", "Org design, hiring plans and engineering practices that scale with the company.", ["Org design","Hiring","Process"]),
  ],
  "method_h2": ("From question", "to clarity."),
  "method_note": "Four movements from a hard decision to a plan you can act on with confidence.",
  "method": [
    ("01 / Listen","Understand goals","We start with the business and the decision at hand, not a generic framework."),
    ("02 / Assess","Read the reality","An honest assessment of the current state — tech, team, risks and options."),
    ("03 / Recommend","Give a clear plan","Direct, prioritised recommendations and a sequenced plan — no fence-sitting."),
    ("04 / Support","Help you execute","We can stay on to help deliver, or hand over a plan your team can run with."),
  ],
  "ind_h2": ("Advice for", "real industries."),
  "ind_note": "We advise founders, investors and leaders across high-stakes domains — startups to enterprises.",
  "industries": ["FinTech","HealthTech","Logistics","Retail & Commerce","B2B SaaS","Investors","Enterprise"],
  "why": [
    ("i","Operator-led","We've built and run the systems we advise on — not career advisors."),
    ("ii","Vendor-neutral","No products to push. Our only incentive is your best outcome."),
    ("iii","Candid","Direct, honest advice — including the things you may not want to hear."),
    ("iv","Confidential","Discreet by default, with NDAs and confidentiality as standard."),
  ],
  "proof_hl": 'Trusted on the big calls: <span class="hl">strategy</span>, <span class="hl">due diligence</span>, <span class="hl">scale.</span>',
  "faq_h2": ("Advisory,", "answered."),
  "faqs": [
    ("What is a fractional CTO?", "A fractional CTO is an experienced technology leader who works with you part-time — setting technical direction, leading the team and making key decisions — at a fraction of the cost and commitment of a full-time hire. Ideal for startups and scale-ups."),
    ("What is technical due diligence?", "Technical due diligence is an independent assessment of a company's technology, architecture, team, security and risks — usually for investors or acquirers evaluating a deal. We deliver a clear, honest report you can act on."),
    ("When do I need a fractional CTO?", "When you need senior technical leadership but aren't ready for a full-time CTO — for example, scoping a build, leading a small team, fundraising, or making big architecture or hiring decisions."),
    ("What is an AI readiness assessment?", "It's an evaluation of where AI can realistically create value for you, what data and capabilities you'd need, the build-vs-buy options and a pragmatic roadmap — so you invest in AI with eyes open."),
    ("Do you do due diligence for investors?", "Yes. We run technical due diligence for VCs, PE firms and acquirers — assessing the technology, team and risks of a target — discreetly and on tight timelines."),
    ("How are advisory engagements structured?", "Flexibly — from a one-off assessment or due-diligence report to an ongoing fractional-CTO retainer. We scope to the decision and timeline you're facing."),
    ("Is it confidential?", "Always. We work under NDA as standard and treat every engagement as strictly confidential."),
  ],
  "contact_h2": ("Get the", "clarity."),
  "contact_sub": "Tell us the decision you're facing. We reply to every serious enquiry within one business day — and the first consultation is free.",
},
}

# ---------------------------------------------------------------------------
NAV = '''    <nav class="nav" id="nav">
        <a href="/" class="brand" data-cursor>
            <img class="brand-mark" src="/assets/logo-mark.svg" alt="Mach Lilies" width="38" height="38" />
            <span>
                <span class="b-name">Mach Lilies</span>
                <span class="b-sub">Technology Consultancy</span>
            </span>
        </a>
        <div class="nav-links" id="nav-links">
            <a href="/#work"><span class="idx">01</span>Work</a>
            <a href="/#capabilities"><span class="idx">02</span>Capabilities</a>
            <a href="/#method"><span class="idx">03</span>Method</a>
            <a href="/#studio"><span class="idx">04</span>Studio</a>
        </div>
        <a href="mailto:machlilieslimited@gmail.com?subject=Project%20enquiry" class="nav-cta magnetic" data-cursor>Start a project</a>
        <button class="burger" id="burger" aria-label="Open menu"><span></span><span></span></button>
    </nav>
    <div class="mobile-menu" id="mobile-menu">
        <a href="/#work"><span class="idx">01</span>Work</a>
        <a href="/#capabilities"><span class="idx">02</span>Capabilities</a>
        <a href="/#method"><span class="idx">03</span>Method</a>
        <a href="/#studio"><span class="idx">04</span>Studio</a>
        <a href="/#contact"><span class="idx">05</span>Contact</a>
        <div class="mm-foot">machlilieslimited@gmail.com</div>
    </div>'''

def footer():
    svc_links = "\n".join(
        '                    <a href="/services/%s/">%s</a>' % (s, esc(SHORT[s][0]))
        for s in ORDER)
    return '''    <footer class="footer">
        <div class="wrap">
            <span class="foot-word">Mach<span class="it"> Lilies</span></span>
            <div class="foot-cols">
                <div class="foot-col">
                    <h5>The practice</h5>
                    <p>An independent AI &amp; technology consultancy. We design, engineer, and scale software worth keeping.</p>
                </div>
                <div class="foot-col">
                    <h5>Navigate</h5>
                    <a href="/#work">Work</a>
                    <a href="/#capabilities">Capabilities</a>
                    <a href="/#method">Method</a>
                    <a href="/#faq">FAQ</a>
                </div>
                <div class="foot-col">
                    <h5>Services</h5>
%s
                </div>
                <div class="foot-col">
                    <h5>Contact</h5>
                    <a href="mailto:machlilieslimited@gmail.com">machlilieslimited@gmail.com</a>
                    <p style="margin-top:0.6rem">Global remote studio.<br/>Working across time zones.</p>
                </div>
            </div>
            <div class="foot-base">
                <span>© <span id="year">2026</span> Mach Lilies Limited. All rights reserved.</span>
                <span class="tag">Mach speed. Lily craft.</span>
                <a href="#top" data-cursor>Back to top ↑</a>
            </div>
        </div>
    </footer>''' % svc_links

def jsonld(slug, d):
    url = "%s/services/%s/" % (BASE, slug)
    graph = [
        {"@type": ["Organization","ProfessionalService"], "@id": BASE+"/#org",
         "name":"Mach Lilies","legalName":"Mach Lilies Limited","url":BASE+"/",
         "logo":BASE+"/assets/logo-mark.svg","email":"machlilieslimited@gmail.com",
         "slogan":"Mach speed. Lily craft.","areaServed":{"@type":"Place","name":"Worldwide"}},
        {"@type":"Service","@id":url+"#service","name":SHORT[slug][0],
         "serviceType":d["service_type"],"url":url,
         "provider":{"@id":BASE+"/#org"},"areaServed":{"@type":"Place","name":"Worldwide"},
         "description":d["desc"],
         "audience":{"@type":"Audience","audienceType":"Startups and enterprises"},
         "hasOfferCatalog":{"@type":"OfferCatalog","name":SHORT[slug][0]+" services",
            "itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":s[0]}} for s in d["services"]]}},
        {"@type":"WebPage","@id":url+"#webpage","url":url,"name":d["title"],
         "isPartOf":{"@id":BASE+"/#website"},"about":{"@id":url+"#service"},
         "primaryImageOfPage":BASE+"/assets/og-image.png","inLanguage":"en"},
        {"@type":"BreadcrumbList","@id":url+"#breadcrumb","itemListElement":[
            {"@type":"ListItem","position":1,"name":"Home","item":BASE+"/"},
            {"@type":"ListItem","position":2,"name":"Services","item":BASE+"/#capabilities"},
            {"@type":"ListItem","position":3,"name":SHORT[slug][0],"item":url}]},
        {"@type":"FAQPage","@id":url+"#faq","mainEntity":[
            {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in d["faqs"]]},
    ]
    return json.dumps({"@context":"https://schema.org","@graph":graph}, indent=2, ensure_ascii=False)

def render_services(d):
    rows = []
    for i,(h,desc,tags) in enumerate(d["services"], 1):
        dd = ' data-d="%d"' % ((i-1)%3) if (i-1)%3 else ""
        tagspans = "".join("<span>%s</span>" % esc(t) for t in tags)
        rows.append('''                <div class="cap-row reveal"%s data-cursor>
                    <div class="cap-no">%02d</div>
                    <div class="cap-main"><h3>%s</h3><p class="cap-desc">%s</p></div>
                    <div class="cap-tags">%s</div>
                </div>''' % (dd, i, esc(h), esc(desc), tagspans))
    return "\n".join(rows)

def render_method(d):
    return "\n".join(
        '                <div class="method-step"><span class="ms-no">%s</span><h3>%s</h3><p>%s</p></div>'
        % (esc(no), esc(h), esc(p)) for no,h,p in d["method"])

def render_why(d):
    return "\n".join(
        '                <div class="why"><span class="n">%s</span><h3>%s</h3><p>%s</p></div>'
        % (esc(n), esc(h), esc(p)) for n,h,p in d["why"])

def render_faqs(d):
    return "\n".join(
        '''                <details class="faq-item"><summary><span>%s</span><i aria-hidden="true"></i></summary><div class="faq-a"><p>%s</p></div></details>'''
        % (esc(q), esc(a)) for q,a in d["faqs"])

def render_related(slug):
    cards = []
    for s in ORDER:
        if s == slug: continue
        name, blurb = SHORT[s]
        cards.append('''                <a class="rel-card magnetic" href="/services/%s/" data-cursor><span class="rel-n">↗</span><h3>%s</h3><p>%s</p></a>'''
                     % (s, esc(name), esc(blurb)))
    return "\n".join(cards)

def build(slug, d):
    url = "%s/services/%s/" % (BASE, slug)
    ind = "".join("<span>%s</span>" % esc(x) for x in d["industries"])
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="#0d0c0a" />
    <meta name="color-scheme" content="dark" />

    <title>{title}</title>
    <meta name="description" content="{desc}" />
    <link rel="canonical" href="{url}" />
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
    <meta name="author" content="Mach Lilies Limited" />
    <meta name="keywords" content="{keywords}" />

    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="Mach Lilies" />
    <meta property="og:locale" content="en_US" />
    <meta property="og:url" content="{url}" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{desc}" />
    <meta property="og:image" content="{base}/assets/og-image.png" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{title}" />
    <meta name="twitter:description" content="{desc}" />
    <meta name="twitter:image" content="{base}/assets/og-image.png" />

    <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml" />
    <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png" />
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon-16.png" />
    <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png" />
    <link rel="mask-icon" href="/assets/favicon.svg" color="#c9f24c" />
    <link rel="manifest" href="/assets/site.webmanifest" />

    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;0,9..144,700;0,9..144,900;1,9..144,400;1,9..144,500;1,9..144,600&family=Inter:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="/assets/css/site.css" />

    <script type="application/ld+json">
{jsonld}
    </script>

    <script>
      window.GA_MEASUREMENT_ID = "G-XXXXXXXXXX";
      (function () {{
        var id = window.GA_MEASUREMENT_ID;
        if (!id || id.indexOf("XXXX") !== -1) return;
        var s = document.createElement("script");
        s.async = true; s.src = "https://www.googletagmanager.com/gtag/js?id=" + id;
        document.head.appendChild(s);
        window.dataLayer = window.dataLayer || [];
        function gtag() {{ dataLayer.push(arguments); }}
        window.gtag = gtag; gtag("js", new Date()); gtag("config", id, {{ anonymize_ip: true }});
      }})();
    </script>
</head>
<body>
    <div class="grain" aria-hidden="true"></div>
    <div class="vignette" aria-hidden="true"></div>
    <div class="cursor-dot" aria-hidden="true"></div>
    <div class="cursor-ring" aria-hidden="true"><span class="c-label">View</span></div>
    <div class="progress" aria-hidden="true"></div>

{nav}

    <header class="svc-hero" id="top">
        <img class="hero-lily" id="hero-lily" src="/assets/logo-mark-line.svg" alt="" aria-hidden="true" />
        <div class="wrap" style="position:relative;z-index:2">
            <nav class="crumb reveal" aria-label="Breadcrumb">
                <a href="/">Home</a> <span>/</span> <a href="/#capabilities">Services</a> <span>/</span> <b>{short}</b>
            </nav>
            <span class="eyebrow reveal" data-d="1" style="margin-top:1.4rem;display:inline-flex">{eyebrow}</span>
            <h1 class="display reveal" data-d="1">{h1a}<br/><span class="it accent-text">{h1b}</span></h1>
            <p class="svc-lead reveal" data-d="2">{lead}</p>
            <div class="hero-cta reveal" data-d="3" style="margin-top:2.2rem">
                <a href="mailto:machlilieslimited@gmail.com?subject={subject}" class="btn btn-solid magnetic" data-cursor>Book a free consultation <span class="arrow">→</span></a>
                <a href="/#work" class="btn btn-ghost magnetic" data-cursor>See the work</a>
            </div>
        </div>
    </header>

    <section class="block manifesto">
        <div class="wrap">
            <span class="eyebrow muted reveal">{ov_eyebrow}</span>
            <p class="reveal" data-d="1" style="margin-top:1.5rem">{ov_hl}</p>
            <p class="svc-lead reveal" data-d="2" style="margin-top:2rem;max-width:72ch">{ov_body}</p>
        </div>
    </section>

    <section class="block" id="services">
        <div class="wrap">
            <div class="sec-head">
                <div>
                    <span class="eyebrow muted reveal">What we do</span>
                    <h2 class="display reveal" data-d="1" style="margin-top:1.2rem">{svc_h2a} <span class="it accent-text">{svc_h2b}</span></h2>
                </div>
                <p class="sec-no reveal" data-d="2" style="max-width:34ch">{svc_note}</p>
            </div>
            <div class="cap-list">
{services}
            </div>
        </div>
    </section>

    <section class="block method">
        <div class="wrap">
            <div class="sec-head">
                <div>
                    <span class="eyebrow muted reveal">How we work</span>
                    <h2 class="display reveal" data-d="1" style="margin-top:1.2rem">{method_h2a} <span class="it accent-text">{method_h2b}</span></h2>
                </div>
                <p class="sec-no reveal" data-d="2" style="max-width:34ch">{method_note}</p>
            </div>
            <div class="method-grid reveal" data-d="1">
{method}
            </div>
        </div>
    </section>

    <section class="block">
        <div class="wrap">
            <div class="sec-head">
                <div>
                    <span class="eyebrow muted reveal">Who we help</span>
                    <h2 class="display reveal" data-d="1" style="margin-top:1.2rem">{ind_h2a} <span class="it accent-text">{ind_h2b}</span></h2>
                </div>
                <p class="sec-no reveal" data-d="2" style="max-width:32ch">{ind_note}</p>
            </div>
            <div class="ind-grid reveal" data-d="1" style="margin-bottom:4rem">{industries}</div>
            <div class="why-grid reveal" data-d="1">
{why}
            </div>
        </div>
    </section>

    <section class="block manifesto">
        <div class="wrap">
            <span class="eyebrow muted reveal">Proof, in production</span>
            <p class="reveal" data-d="1" style="margin-top:1.5rem;max-width:26ch">{proof_hl}</p>
            <div class="hero-cta reveal" data-d="2" style="margin-top:2.4rem">
                <a href="/#work" class="btn btn-ghost magnetic" data-cursor>Read the case studies <span class="arrow">→</span></a>
            </div>
        </div>
    </section>

    <section class="block faq" id="faq">
        <div class="wrap">
            <div class="sec-head">
                <div>
                    <span class="eyebrow muted reveal">Questions</span>
                    <h2 class="display reveal" data-d="1" style="margin-top:1.2rem">{faq_h2a} <span class="it accent-text">{faq_h2b}</span></h2>
                </div>
            </div>
            <div class="faq-list reveal" data-d="1">
{faqs}
            </div>
        </div>
    </section>

    <section class="block">
        <div class="wrap">
            <div class="sec-head">
                <div>
                    <span class="eyebrow muted reveal">More from the studio</span>
                    <h2 class="display reveal" data-d="1" style="margin-top:1.2rem">Related <span class="it accent-text">services.</span></h2>
                </div>
            </div>
            <div class="rel-grid reveal" data-d="1">
{related}
            </div>
        </div>
    </section>

    <section class="block contact" id="contact">
        <img class="hero-lily" src="/assets/logo-mark-line.svg" alt="" aria-hidden="true" style="left:-12%;right:auto;opacity:0.16;width:min(50vw,520px)" />
        <div class="wrap" style="position:relative;z-index:2">
            <span class="eyebrow muted reveal" style="justify-content:center;display:inline-flex">Let's begin</span>
            <h2 class="big reveal" data-d="1">{contact_h2a} <span class="it">{contact_h2b}</span></h2>
            <p class="c-sub reveal" data-d="2">{contact_sub}</p>
            <div class="c-actions reveal" data-d="2">
                <a href="mailto:machlilieslimited@gmail.com?subject={subject}" class="btn btn-solid magnetic" data-cursor>machlilieslimited@gmail.com <span class="arrow">→</span></a>
                <a href="/" class="btn btn-ghost magnetic" data-cursor>Back to home</a>
            </div>
        </div>
    </section>

{footer}

    <script src="/assets/js/site.js" defer></script>
</body>
</html>
'''.format(
        title=esc(d["title"]), desc=esc(d["desc"]), url=url, base=BASE,
        keywords=esc(d["keywords"]), jsonld=jsonld(slug, d), nav=NAV,
        short=esc(SHORT[slug][0]), eyebrow=esc(d["eyebrow"]),
        h1a=esc(d["h1"][0]), h1b=esc(d["h1"][1]), lead=d["lead"],
        subject="Enquiry%20—%20"+SHORT[slug][0].replace(" ","%20").replace("&","and"),
        ov_eyebrow=esc(d["ov_eyebrow"]), ov_hl=d["ov_hl"], ov_body=esc(d["ov_body"]),
        svc_h2a=esc(d["svc_h2"][0]), svc_h2b=esc(d["svc_h2"][1]), svc_note=esc(d["svc_note"]),
        services=render_services(d),
        method_h2a=esc(d["method_h2"][0]), method_h2b=esc(d["method_h2"][1]),
        method_note=esc(d["method_note"]), method=render_method(d),
        ind_h2a=esc(d["ind_h2"][0]), ind_h2b=esc(d["ind_h2"][1]), ind_note=esc(d["ind_note"]),
        industries=ind, why=render_why(d), proof_hl=d["proof_hl"],
        faq_h2a=esc(d["faq_h2"][0]), faq_h2b=esc(d["faq_h2"][1]), faqs=render_faqs(d),
        related=render_related(slug),
        contact_h2a=esc(d["contact_h2"][0]), contact_h2b=esc(d["contact_h2"][1]),
        contact_sub=esc(d["contact_sub"]), footer=footer(),
    )

if __name__ == "__main__":
    print("== service pages ==")
    for slug in ORDER:
        path = os.path.join(ROOT, "services", slug, "index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w").write(build(slug, SERVICES[slug]))
        print("  wrote services/%s/index.html" % slug)
    print("done.")
