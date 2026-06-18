#!/usr/bin/env python3
"""
Mach Lilies — service page generator.

One audited template + per-service content => consistent, SEO-complete,
internally-linked service pages. Each page is unique (distinct copy, services,
method, FAQs) to avoid duplicate content, and carries Service + FAQPage +
BreadcrumbList + WebPage + Organization JSON-LD.

The site is positioned around AGENTIC OPERATIONS: building, governing and
operating safe AI agent workflows. The agentic offers lead; the original
engineering disciplines remain as the supporting delivery bench.

Run:  python3 tools/generate_service_pages.py
"""
import os, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://machlilies.com"
SPRINT = "agentic-operations-sprint"

# --- live integrations (edit here; one source for every generated page) ---
GA_ID = "G-PSM4267LV3"                                          # Google Analytics 4 measurement ID
FORM_ENDPOINT = "https://formspree.io/f/xojzonkd"               # contact-form POST endpoint (Formspree)
BOOKING_URL = "https://cal.eu/machlilies/agent-operations-sprint-intro"  # Cal booking link

def esc(s): return html.escape(s, quote=False)

# short name + blurb for the "Related services" mesh and footer
SHORT = {
    "agentic-operations":        ("Agentic Operations", "AI agents that run real business workflows, safely and governed."),
    "agentops-ai-governance":    ("AgentOps & Governance", "Permissions, logs, evaluations, approvals and cost control for agents."),
    "ai-pilot-rescue":           ("AI Pilot Rescue", "Audit stuck AI pilots; kill, fix or scale with clear ROI and controls."),
    "ai-assurance-evaluation":   ("AI Assurance", "Inventories, risk classification, oversight and audit-ready evidence."),
    "ai-modernisation-factory":  ("AI-Native Modernization", "Modernize legacy software at agentic speed with senior review."),
    "agentic-operations-sprint": ("Agentic Operations Sprint", "Map, prototype and business-case your first agent workflow."),
    "ai-consulting":             ("AI Consulting", "AI, LLM and machine-learning systems, strategy to production."),
    "product-engineering":       ("Product Engineering", "Custom web & mobile software, built to scale."),
    "cloud-platform":            ("Cloud & Platform", "Cloud-native architecture, DevOps and reliability."),
    "data-analytics":            ("Data & Analytics", "Pipelines, warehousing and analytics you can act on."),
    "design-experience":         ("Design & Experience", "Product UX/UI, design systems, brand and motion."),
    "strategy-advisory":         ("Strategy & Advisory", "Fractional CTO, due diligence and technology strategy."),
}

# agentic offers lead; foundation disciplines support
AGENTIC    = ["agentic-operations", "agentops-ai-governance", "ai-pilot-rescue", "ai-assurance-evaluation", "ai-modernisation-factory"]
FOUNDATION = ["ai-consulting", "product-engineering", "cloud-platform", "data-analytics", "design-experience", "strategy-advisory"]
ORDER      = AGENTIC + [SPRINT] + FOUNDATION       # everything we generate

# curated "related services" (3 each) — keeps the rel-grid a clean 3-up
RELATED = {
    "agentic-operations":        ["agentops-ai-governance", "ai-pilot-rescue", SPRINT],
    "agentops-ai-governance":    ["agentic-operations", "ai-assurance-evaluation", "ai-pilot-rescue"],
    "ai-pilot-rescue":           ["agentic-operations", "agentops-ai-governance", "ai-modernisation-factory"],
    "ai-assurance-evaluation":   ["agentops-ai-governance", "agentic-operations", "strategy-advisory"],
    "ai-modernisation-factory":  ["product-engineering", "agentic-operations", "cloud-platform"],
    SPRINT:                      ["agentic-operations", "agentops-ai-governance", "ai-pilot-rescue"],
    "ai-consulting":             ["agentic-operations", "agentops-ai-governance", "ai-pilot-rescue"],
    "product-engineering":       ["ai-modernisation-factory", "agentic-operations", "cloud-platform"],
    "cloud-platform":            ["agentops-ai-governance", "data-analytics", "ai-modernisation-factory"],
    "data-analytics":            ["agentic-operations", "ai-consulting", "cloud-platform"],
    "design-experience":         ["product-engineering", "agentic-operations", "strategy-advisory"],
    "strategy-advisory":         ["ai-pilot-rescue", "ai-assurance-evaluation", "agentic-operations"],
}

# footer "Services" column — agentic offers + the sprint
FOOTER_SERVICES = AGENTIC + [SPRINT]

SERVICES = {

# ============================ AGENTIC OFFERS ============================
"agentic-operations": {
  "title": "Agentic Operations-as-a-Service | Mach Lilies",
  "desc": "Safe AI agents for business workflows. Mach Lilies builds, integrates, monitors and operates governed AI agent workflows across your tools and data — with human oversight and measurable ROI.",
  "keywords": "agentic operations, AI agent implementation consultancy, AI workflow automation consulting, managed AI agents, AI operations, AI agents for business processes, governed AI agents",
  "service_type": "Agentic operations and AI workflow implementation",
  "eyebrow": "Agentic Operations",
  "h1": ("AI agents that run", "real business workflows."),
  "lead": "Mach Lilies designs, deploys, governs, and operates AI agent workflows that take work out of inboxes, documents, CRMs, finance systems and operational queues — safely, measurably, and with human oversight where it matters. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "What agentic operations means",
  "ov_hl": 'Agents don\'t need <span class="dim">unlimited autonomy</span> to create value. The strongest production systems are <span class="hl">bounded, monitored and governed.</span>',
  "ov_body": "Agentic operations is the practice of putting AI agents to work on real, repeatable business processes — and then running them like production systems, not experiments. As a senior, founder-led practice, Mach Lilies maps the workflow, builds a bounded agent against your real tools and data, wires in human approval where risk lives, and operates it with monitoring, evaluation and a full audit trail. You buy a workflow that runs and keeps improving — not billable hours.",
  "svc_h2": ("What we", "deliver."),
  "svc_note": "Workflow design, agent build, secure connectors, governance and managed operation — engaged together or in stages.",
  "services": [
    ("Workflow design", "We map the process end to end — triggers, handoffs and exceptions — and design where an agent can safely act and where a human stays in the loop.", ["Mapping","Process","Scope"]),
    ("Agent build", "Bounded, tool-using agents built against your real systems and documents, with clear permissions and predictable behaviour.", ["Agents","Tools","Bounded"]),
    ("Secure connectors", "Least-privilege integrations into CRM, ERP, email, document stores, ticketing and finance tools — scoped to the workflow and nothing more.", ["CRM","ERP","Email"]),
    ("Human-in-the-loop", "Approval gates, review queues and escalation rules, so high-risk actions always pass a person before they happen.", ["Approvals","Escalation","Review"]),
    ("Monitoring & evaluation", "Quality checks, evaluation suites and dashboards that show what the agent did, where it struggled and what it cost.", ["Evals","Logs","Dashboards"]),
    ("Managed operation", "We run the workflow as a service — monitoring, tuning, regression testing and monthly optimisation as your processes change.", ["Managed","Tuning","SLAs"]),
  ],
  "method_h2": ("Map, prototype,", "govern, operate."),
  "method_note": "Four movements that take a workflow from manual drag to a governed agent running in production.",
  "method": [
    ("01 / Map","Find the workflow","Identify the process where an agent can create value without uncontrolled risk, and agree the success measures."),
    ("02 / Prototype","Prove it on real inputs","Build a narrow working agent against realistic data and tool calls, evaluated against measurable outputs."),
    ("03 / Govern","Add the controls","Permissions, approvals, evaluations, logs and incident controls — built in before scale, not bolted on after."),
    ("04 / Operate","Run and improve","Monitor quality and cost, expand scope carefully, and report on the workflow as it runs."),
  ],
  "ind_h2": ("Built for", "operational teams."),
  "ind_note": "We work with leaders who own real processes and need them to run reliably — across document-heavy, admin-heavy work.",
  "industries": ["COO / Operations","Finance & back office","Customer operations","Insurance brokers","Accountancy","Property management","Logistics","Legal services"],
  "why": [
    ("i","Bounded by design","Agents get least-privilege access and clear limits. No open-ended autonomy inside your systems."),
    ("ii","Human oversight","People approve the actions that carry risk; the agent drafts, routes, classifies and updates."),
    ("iii","Operated, not abandoned","We monitor, evaluate and improve the workflow after launch — the value compounds."),
    ("iv","Yours to own","Source, runbooks and operational knowledge transfer to your team. No lock-in."),
  ],
  "proof_hl": 'We optimise for one thing: a <span class="hl">governed workflow</span> that <span class="hl">removes manual drag</span> and <span class="dim">keeps running safely.</span>',
  "faq_h2": ("Agentic operations,", "answered."),
  "faqs": [
    ("What is agentic operations?", "Agentic operations is the design, deployment and ongoing operation of AI agents that perform real business workflows — bounded systems that read, draft, classify, update and route work across your tools, with human approval for high-risk actions and a full audit trail. It is the difference between an AI demo and an AI workflow that runs in production."),
    ("Are these agents fully autonomous?", "No — and that is deliberate. The strongest production systems are bounded: agents get least-privilege access to only the tools and data a workflow needs, humans approve high-risk actions, and every step is logged. We design for control, not uncontrolled autonomy."),
    ("Which systems can the agents work with?", "We build secure, least-privilege connectors into the systems a workflow touches — typically CRM, ERP, email, document storage, ticketing, finance and internal tools. Access is scoped to the specific workflow and nothing more."),
    ("How do you measure ROI?", "Before we build, we estimate the time saved, error reduction and throughput gain. After launch, monitoring and evaluation track real usage and cost, so the operational impact is measured rather than assumed."),
    ("What does the managed model include?", "Ongoing monitoring, quality evaluation, regression testing when models or prompts change, cost tracking, incident response and monthly optimisation as your processes evolve. You can also take operations in-house — we hand over clean systems and runbooks."),
    ("How do we start?", "Most engagements begin with an Agentic Operations Sprint: a focused engagement that maps your highest-value workflows, prototypes the strongest one, and produces a production rollout plan with governance built in."),
  ],
  "contact_h2": ("Put one workflow", "to work."),
  "contact_sub": "Tell us the workflow you want to take off your team's plate — the systems involved, the manual effort today, and any risk or compliance concerns. We reply to every serious enquiry within one business day.",
  "cta": "Book an Agentic Operations Sprint", "cta_href": "/services/agentic-operations-sprint/",
  "cta2": "See agent workflows", "cta2_href": "/#work",
},

"agentops-ai-governance": {
  "title": "AgentOps & AI Governance Consultancy | Mach Lilies",
  "desc": "Control AI agents with permissions, audit trails, evaluations, monitoring, incident response, cost controls and human approval workflows. Mach Lilies builds the AgentOps control tower for production AI.",
  "keywords": "AgentOps, AI governance, AI agent governance, AI monitoring, AI audit trail, AI evaluation, AI risk controls, human-in-the-loop, AI incident response, agent permissions",
  "service_type": "AgentOps and AI governance implementation",
  "eyebrow": "AgentOps & AI Governance",
  "h1": ("The control tower", "for AI agents."),
  "lead": "When agents can use tools, update records, draft messages and trigger workflows, leaders need visibility and control. Mach Lilies implements the registry, permissions, evaluations, logs, approvals, monitoring, incident response and evidence packs that make agents safe to operate. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "Why AgentOps",
  "ov_hl": 'AgentOps turns AI agents from <span class="dim">risky experiments</span> into <span class="hl">manageable operational assets.</span>',
  "ov_body": "Most agentic projects stall not because the model is weak, but because no one can see what the agents can access, what they did, where they failed, who approved them, or what they cost. AgentOps is the operating layer that answers those questions. Mach Lilies builds it as part of delivery — a control tower for production AI that gives operations, technology and risk leaders the visibility and the brakes they need.",
  "svc_h2": ("Control", "capabilities."),
  "svc_note": "The operating layer for production AI agents — implemented in your environment, not described on a slide.",
  "services": [
    ("Agent registry", "A single inventory of every agent: what it does, which workflow it serves, what it can access, and who owns it.", ["Inventory","Ownership","Scope"]),
    ("Permissions & access", "Least-privilege tool and data boundaries for each agent, so it can only ever act inside its workflow.", ["Least-privilege","Boundaries","Identity"]),
    ("Approval gates", "Human-in-the-loop checkpoints for high-risk actions — review queues, sign-off and clear escalation paths.", ["Approvals","Escalation","Sign-off"]),
    ("Action logs & audit", "A complete, queryable record of every tool call, decision, escalation and approval — built for audit.", ["Audit trail","Logs","Evidence"]),
    ("Evaluation & regression", "Test suites that check prompts, models and workflows against known cases before and after every change.", ["Evals","Regression","QA"]),
    ("Monitoring & cost", "Dashboards for quality, throughput and spend, with model routing and cost controls so usage stays predictable.", ["Monitoring","FinOps","Routing"]),
    ("Incident response", "Pause, roll back or restrict an agent when behaviour changes — with a defined incident process.", ["Rollback","Kill switch","Runbook"]),
    ("Governance reporting", "Quarterly reporting that gives leaders and auditors a clear, current view of every agent in operation.", ["Reporting","Assurance","Board"]),
  ],
  "method_h2": ("From visibility", "to control."),
  "method_note": "Four movements from agents you can't see to agents you can govern with confidence.",
  "method": [
    ("01 / Inventory","See every agent","Register what's running, what it can touch and who owns it — the baseline for any control."),
    ("02 / Bound","Set the limits","Apply least-privilege permissions, approval gates and escalation rules to each workflow."),
    ("03 / Instrument","Log and evaluate","Wire in action logs, evaluation suites and dashboards so quality and cost are visible."),
    ("04 / Operate","Monitor and respond","Run monitoring, regression checks and incident response, with reporting for leaders and auditors."),
  ],
  "ind_h2": ("Built for", "risk-aware leaders."),
  "ind_note": "For the people accountable when AI acts inside the business — technology, operations, risk and compliance.",
  "industries": ["CTO / Engineering","COO / Operations","Risk & compliance","Internal audit","Regulated sectors","FinTech","HealthTech","Enterprise"],
  "why": [
    ("i","Control as delivery","We build governance into the build, not as an afterthought once something has gone wrong."),
    ("ii","Model-agnostic","The control layer works across GPT, Claude, Gemini, open-source and private deployments."),
    ("iii","Evidence-ready","Logs and reports are structured for audit and assurance from day one."),
    ("iv","Operable by you","Your team can run the control tower — we hand over dashboards, runbooks and process."),
  ],
  "proof_hl": 'Know what your agents <span class="hl">can access</span>, <span class="hl">what they did</span>, where they failed, who approved them, and <span class="hl">what they cost.</span>',
  "faq_h2": ("AgentOps,", "answered."),
  "faqs": [
    ("What is AgentOps?", "AgentOps is the operational layer for production AI agents — the registry, permissions, monitoring, evaluation, audit logs, approval workflows, cost controls and incident response that let an organisation run agents safely and account for what they do. It is to AI agents what DevOps and MLOps are to software and machine learning."),
    ("How is this different from MLOps?", "MLOps keeps models trained, deployed and monitored. AgentOps governs what agents are allowed to do once they can take actions — using tools, updating records and triggering workflows. It adds permissions, human approval, action audit trails and incident controls on top of monitoring."),
    ("Do we need AgentOps if we only have one agent?", "Even one agent that can act inside business systems needs boundaries, logging and a way to pause it. AgentOps scales down to a single workflow and grows with you as more agents go into production."),
    ("Can you govern agents we built ourselves or with another vendor?", "Yes. The control layer is model- and vendor-agnostic. We can wrap governance around existing agents, regardless of how or where they were built."),
    ("What does the audit trail capture?", "Every tool call, decision, escalation and human approval — structured so that, for any action, you can answer what happened, why, who approved it and what it cost. That record is what makes agents defensible to auditors and regulators."),
    ("How is AgentOps priced?", "Typically an implementation engagement to stand up the control layer, followed by a managed governance retainer with quarterly reporting. We scope to the number of agents and the level of oversight your risk profile requires."),
  ],
  "contact_h2": ("Govern your", "first agent."),
  "contact_sub": "Tell us which agents or AI workflows are live or planned, the systems they touch, and your risk and compliance concerns. We reply to every serious enquiry within one business day.",
  "cta": "Govern your first agent workflow", "cta_href": "mailto:machlilieslimited@gmail.com?subject=Govern%20our%20AI%20agents%20%E2%80%94%20AgentOps",
  "cta2": "Book an Agentic Operations Sprint", "cta2_href": "/services/agentic-operations-sprint/",
},

"ai-pilot-rescue": {
  "title": "AI Pilot Rescue & Productionization | Mach Lilies",
  "desc": "Stuck AI pilot? Mach Lilies audits, rescues and productionizes — or kills — stalled AI pilots with a clear ROI model, data readiness review, risk review and governance controls.",
  "keywords": "AI pilot rescue, AI productionization, stuck AI project, AI proof of concept to production, AI project audit, scale or kill AI, AI pilot to production",
  "service_type": "AI pilot rescue and productionization",
  "eyebrow": "AI Pilot Rescue",
  "h1": ("Rescue the AI pilots", "worth saving."),
  "lead": "Most AI pilots don't fail because the model is weak. They fail because the workflow, data, integration, controls and business case were never designed for production. We diagnose the pilot, decide what to kill, fix or scale, and turn the best one into a governed production workflow. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "Why pilots stall",
  "ov_hl": 'A demo proves it <span class="dim">can</span> work. Production proves it <span class="hl">does</span> — on real data, real users and real risk.',
  "ov_body": "Industry research is consistent: a large share of AI and agentic projects are abandoned because of unclear business value, cost or inadequate controls. The model is rarely the problem. The gap is everything around it — messy data, brittle integrations, missing oversight and a business case no one stress-tested. Mach Lilies runs a focused audit, gives you an honest kill / fix / scale recommendation, and productionises the pilots that deserve it.",
  "svc_h2": ("What the rescue", "delivers."),
  "svc_note": "A focused audit that ends in a clear decision and, where it is justified, a path to production.",
  "services": [
    ("Business-case audit", "We pressure-test the value: what the pilot is meant to achieve, what it would really save, and whether that justifies production.", ["ROI","Value","Case"]),
    ("Workflow fit review", "Where the pilot fits the actual process — and where it breaks against real handoffs, exceptions and edge cases.", ["Workflow","Fit","Edge cases"]),
    ("Data & system readiness", "An honest look at the data quality, sources, APIs, identity and permissions the pilot needs to work in production.", ["Data","APIs","Readiness"]),
    ("Risk & failure modes", "Where the pilot can go wrong, what that would cost, and which controls are non-negotiable before scale.", ["Risk","Controls","Safety"]),
    ("Prototype hardening", "For the pilots worth saving: hardening the prototype into something robust enough for real use.", ["Hardening","Robustness","QA"]),
    ("Production & governance plan", "A fixed-scope rollout plan with architecture, monitoring and AgentOps controls — or a clear recommendation to stop.", ["Rollout","Architecture","Plan"]),
  ],
  "method_h2": ("Audit, decide,", "harden, plan."),
  "method_note": "Four movements from a stalled pilot to a clear decision — and, where it's earned, a path to production.",
  "method": [
    ("01 / Audit","Read the pilot","Understand what was built, why it stalled, and what it was really meant to achieve."),
    ("02 / Decide","Kill, fix or scale","An honest, evidence-based recommendation — including the pilots you should stop."),
    ("03 / Harden","Make it production-fit","Fix the data, integration and control gaps that kept it stuck in demo."),
    ("04 / Plan","Path to production","A fixed-scope rollout plan with governance, monitoring and ownership built in."),
  ],
  "ind_h2": ("For teams with", "a stalled pilot."),
  "ind_note": "For leaders who invested in AI, saw a promising demo, and can't get it into reliable production.",
  "industries": ["Founders / CEO","CTO / Engineering","COO / Operations","Transformation leads","FinTech","HealthTech","Enterprise","Scale-ups"],
  "why": [
    ("i","Honest recommendations","We'll tell you to stop when stopping is right. A clear kill decision saves money too."),
    ("ii","Production-first","We've shipped systems that survive real users and real load — not demo-day theatre."),
    ("iii","Fast and focused","A short, fixed-scope audit, not an open-ended consulting retainer."),
    ("iv","Governed by default","If it goes to production, it goes with controls, monitoring and an audit trail."),
  ],
  "proof_hl": 'A clear <span class="hl">kill / fix / scale</span> decision — with an <span class="hl">ROI model</span>, a risk review and a <span class="hl">production plan.</span>',
  "faq_h2": ("Pilot rescue,", "answered."),
  "faqs": [
    ("What is AI pilot rescue?", "AI pilot rescue is a focused engagement to diagnose a stalled AI project and decide what to do with it. We audit the business case, data readiness, workflow fit and risks, then recommend whether to kill, fix or scale it — and, for the ones worth saving, produce a plan to take them to governed production."),
    ("Why do most AI pilots fail?", "Rarely because of the model. They stall on messy data, brittle integrations, missing human oversight, unclear value, and a business case no one stress-tested. Industry research attributes most cancellations to unclear value, cost and inadequate risk controls — all of which are fixable, or at least knowable early."),
    ("Will you tell us to stop?", "Yes, when that's the right answer. A clear, well-reasoned decision to kill a pilot frees budget and attention for the ones that will pay off. We'd rather give you an honest recommendation than bill you to scale something that shouldn't be."),
    ("How long does a rescue take?", "It's deliberately short and fixed-scope — typically a focused audit measured in weeks, ending in a recommendation and, where justified, a production rollout plan."),
    ("What do we get at the end?", "A kill / fix / scale recommendation, an ROI model, a data and system readiness review, a risk and failure-mode review, and — for viable pilots — a production architecture and governance plan with fixed scope."),
    ("What happens if we decide to scale?", "We can take it to production as an Agentic Operations engagement: hardening the system, building in AgentOps controls and monitoring, and operating it or handing it over to your team."),
  ],
  "contact_h2": ("Send us the pilot", "that stalled."),
  "contact_sub": "Tell us what you built, why it stalled, and what it was meant to achieve. We reply to every serious enquiry within one business day with an honest first view.",
  "cta": "Send us the pilot that stalled", "cta_href": "mailto:machlilieslimited@gmail.com?subject=AI%20pilot%20rescue%20enquiry",
  "cta2": "Book an Agentic Operations Sprint", "cta2_href": "/services/agentic-operations-sprint/",
},

"ai-assurance-evaluation": {
  "title": "AI Assurance & Governance Implementation | Mach Lilies",
  "desc": "Practical AI assurance and governance: AI system inventory, risk classification, usage policies, vendor AI due diligence, human oversight design, evaluation records and audit-ready evidence packs.",
  "keywords": "AI assurance, AI governance implementation, AI risk classification, AI system inventory, AI audit evidence, AI usage policy, vendor AI due diligence, AI evaluation, human oversight",
  "service_type": "AI assurance and governance implementation",
  "eyebrow": "AI Assurance & Evaluation",
  "h1": ("AI assurance that works", "in practice."),
  "lead": "AI governance can't live only in policy documents. Mach Lilies helps companies implement practical controls: system inventories, risk classifications, human oversight, evaluation records, vendor reviews and audit-ready evidence — the assurance that keeps AI defensible as it scales. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "Why AI assurance",
  "ov_hl": 'Governance that lives in a <span class="dim">PDF</span> protects no one. Assurance has to be <span class="hl">implemented and evidenced.</span>',
  "ov_body": "As AI moves into real workflows, leaders and regulators want the same thing: confidence that AI systems are inventoried, risk-assessed, overseen by humans where it matters, and backed by evidence. Mach Lilies turns AI policy into working controls — practical, proportionate, and built into how your teams actually operate. We focus on assurance you can show an auditor, not a framework you file and forget.",
  "svc_h2": ("Assurance", "controls."),
  "svc_note": "Practical, proportionate controls that make AI adoption defensible — implemented, not just documented.",
  "services": [
    ("AI system inventory", "A living register of the AI systems and agents in use — what they do, the data they touch, and who is accountable.", ["Inventory","Register","Ownership"]),
    ("Risk classification", "A pragmatic risk rating for each AI use case, so oversight and controls are proportionate to the stakes.", ["Risk","Tiering","Triage"]),
    ("AI usage policies", "Clear, usable policies for how AI may and may not be used — written to be followed, not filed.", ["Policy","Acceptable use","Standards"]),
    ("Human oversight design", "Where a person must stay in the loop, how they approve, and how exceptions escalate.", ["Oversight","Approval","Escalation"]),
    ("Vendor AI due diligence", "Structured review of third-party AI tools and providers — data handling, training use, security and reliability.", ["Vendors","Diligence","Third-party"]),
    ("Audit evidence packs", "The records that prove your controls work: evaluations, approvals, incidents and reviews, ready for audit.", ["Evidence","Audit","Records"]),
  ],
  "method_h2": ("Inventory, classify,", "control, assure."),
  "method_note": "Four movements that turn AI policy into controls you can operate — and evidence you can show.",
  "method": [
    ("01 / Inventory","Know what's in use","Find and register the AI systems and agents already operating across the business."),
    ("02 / Classify","Rate the risk","Tier each use case so controls and oversight match the actual stakes."),
    ("03 / Control","Implement oversight","Put human oversight, policies and evaluation records into day-to-day operation."),
    ("04 / Assure","Evidence and review","Maintain audit-ready evidence and run ongoing assurance reviews as AI use grows."),
  ],
  "ind_h2": ("For trust-led", "organisations."),
  "ind_note": "For risk, compliance and leadership teams that need AI adoption to be safe, defensible and proportionate.",
  "industries": ["Risk & compliance","Legal & GRC","Internal audit","Board / leadership","FinTech","HealthTech","Regulated sectors","Enterprise"],
  "why": [
    ("i","Practical, not theoretical","Controls built into how teams work — not a framework that sits on a shelf."),
    ("ii","Proportionate","Oversight matched to risk, so low-stakes uses aren't strangled and high-stakes ones aren't exposed."),
    ("iii","Evidence-ready","Everything is recorded, so you can show an auditor what works and why."),
    ("iv","Aligned to standards","We work to recognised security and AI-governance practices, including ISO 27001-aligned controls."),
  ],
  "proof_hl": 'Assurance you can <span class="hl">show an auditor</span> — inventories, risk tiers, oversight, and <span class="hl">evidence that holds up.</span>',
  "faq_h2": ("AI assurance,", "answered."),
  "faqs": [
    ("What is AI assurance?", "AI assurance is the set of practical controls and evidence that give an organisation — and its auditors and regulators — confidence that AI systems are known, risk-assessed, overseen and behaving as intended. It spans system inventories, risk classification, usage policies, human oversight, evaluations and audit evidence."),
    ("Is this the same as an AI policy?", "No. A policy states intent; assurance proves it. We help you write usable policies, but the value is in implementing the controls and producing the evidence that shows they actually work in day-to-day operation."),
    ("Do you guarantee regulatory compliance?", "We don't make regulatory guarantees, and you should be wary of anyone who does. We implement practical, proportionate controls aligned to recognised standards and frameworks, and we structure evidence so your compliance and legal teams can demonstrate diligence."),
    ("How does this relate to AgentOps?", "AgentOps governs AI agents at the technical level — permissions, logs, evaluations and incident response. AI assurance sits above it at the organisational level — inventory, risk classification, policy, oversight and audit evidence. They reinforce each other, and we deliver both."),
    ("Can you review third-party AI tools we use?", "Yes. Vendor AI due diligence is a core part of assurance — we review how third-party tools handle your data, whether they train on it, and their security and reliability posture, so you can adopt them with eyes open."),
    ("How are assurance engagements structured?", "Usually an implementation engagement to stand up the inventory, risk model and controls, followed by periodic assurance reviews — for example quarterly — as your AI footprint grows."),
  ],
  "contact_h2": ("Make AI", "defensible."),
  "contact_sub": "Tell us where AI is being used or planned, and your risk and compliance concerns. We reply to every serious enquiry within one business day.",
  "cta": "Book an AI assurance review", "cta_href": "mailto:machlilieslimited@gmail.com?subject=AI%20assurance%20%26%20governance%20enquiry",
  "cta2": "Explore AgentOps", "cta2_href": "/services/agentops-ai-governance/",
},

"ai-modernisation-factory": {
  "title": "AI-Native Legacy Modernization | Mach Lilies",
  "desc": "Modernize legacy software faster using AI coding agents, automated tests, documentation agents, secure architecture and senior engineering review. Production-grade, human-governed modernization.",
  "keywords": "AI legacy modernization, AI-native modernization, legacy software modernization, AI coding agents, monolith extraction, API wrapping, cloud migration, software modernization consultancy",
  "service_type": "AI-native legacy modernization",
  "eyebrow": "AI-Native Modernization",
  "h1": ("Modernize legacy software", "at agentic speed."),
  "lead": "Coding agents make code cheaper. Senior engineering makes it safe. Mach Lilies uses AI-assisted engineering, automated tests, documentation agents and architecture review to modernize legacy systems faster — while keeping senior engineers in control of architecture, security, testing and release quality. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "Why AI-native modernization",
  "ov_hl": 'Coding agents make code <span class="hl">cheaper.</span> Senior engineering makes it <span class="hl">safe.</span>',
  "ov_body": "Legacy systems are where most organisations actually live — and where AI-assisted engineering pays off fastest. Mach Lilies pairs coding agents, automated test generation and documentation agents with senior human review, so modernization moves at agentic speed without lowering the bar on architecture, security or maintainability. This is our bridge service: the same production discipline as our software practice, now accelerated by agents and governed by people.",
  "svc_h2": ("What we", "modernize."),
  "svc_note": "Assessment, test harnesses, refactoring, API wrapping, security and migration — accelerated by agents, governed by seniors.",
  "services": [
    ("Legacy assessment", "We map the system, its risks and its real constraints, and agree a sequenced modernization plan.", ["Assessment","Audit","Plan"]),
    ("Test harness creation", "Automated test generation that wraps legacy code in a safety net before anything is changed.", ["Testing","Coverage","Safety net"]),
    ("Documentation generation", "Documentation agents reconstruct the knowledge that left with the original team.", ["Docs","Knowledge","Onboarding"]),
    ("Refactoring & extraction", "Monolith extraction, refactoring and UI rebuilds — AI-assisted, senior-reviewed and incremental.", ["Refactor","Extraction","Incremental"]),
    ("API wrapping", "Wrap legacy systems in clean, documented APIs so new services and agents can build on them safely.", ["APIs","Integration","Wrapping"]),
    ("Security & cloud migration", "Security remediation and cloud migration with the same production discipline as a greenfield build.", ["Security","Cloud","Migration"]),
  ],
  "method_h2": ("Assess, protect,", "modernize, harden."),
  "method_note": "Four movements that modernize legacy systems fast — without betting the business on a big-bang rewrite.",
  "method": [
    ("01 / Assess","Map the system","Understand the architecture, risks and constraints before changing a line."),
    ("02 / Protect","Build the safety net","Generate tests and documentation so changes are safe and reversible."),
    ("03 / Modernize","Agents and seniors","AI-assisted refactoring and rebuilds, with senior engineers owning architecture and review."),
    ("04 / Harden","Ship and hand off","Production-grade quality gates, security, and a clean hand-off your team can own."),
  ],
  "ind_h2": ("For teams carrying", "legacy weight."),
  "ind_note": "For organisations whose growth is held back by software that's hard to change — but too important to replace blindly.",
  "industries": ["CTO / Engineering","Product leaders","FinTech","HealthTech","Logistics","Enterprise","Scale-ups","Private equity"],
  "why": [
    ("i","Agents accelerate, seniors govern","AI does the heavy lifting; senior engineers own architecture, security and release quality."),
    ("ii","Safety net first","We don't change legacy code until it's wrapped in tests and documented."),
    ("iii","Incremental, low-risk","Modernization in safe steps, not a risky big-bang rewrite."),
    ("iv","Yours to own","Clean, documented, tested systems handed over with no lock-in."),
  ],
  "proof_hl": 'Legacy modernized <span class="hl">faster</span> — with tests, documentation, and <span class="hl">senior review</span> on every change.',
  "faq_h2": ("Modernization,", "answered."),
  "faqs": [
    ("What is AI-native legacy modernization?", "It's modernizing legacy software using AI-assisted engineering — coding agents, automated test generation and documentation agents — with senior engineers in control of architecture, security, testing and release quality. You get the speed of agents and the safety of experienced human judgement."),
    ("Isn't letting AI touch legacy code risky?", "It would be without controls — which is why we build a safety net first. We generate tests and documentation before changing anything, work incrementally, and put senior engineers on architecture and review. Agents accelerate the work; people own the quality bar."),
    ("How is this different from your product engineering?", "Same production discipline, accelerated by agents. Our product engineering practice builds new software; AI-native modernization applies the same standards to existing systems, using agents to make assessment, testing, documentation and refactoring dramatically faster."),
    ("Do you do a full rewrite or incremental change?", "Almost always incremental. Big-bang rewrites are high-risk; we prefer to wrap legacy systems in tests and APIs and modernize in safe, reversible steps — though we'll assess and recommend honestly for your situation."),
    ("Can you migrate us to the cloud as part of this?", "Yes. Security remediation and cloud migration are part of the service, delivered with the same quality gates as a greenfield build."),
    ("Will our team be able to maintain it afterwards?", "Yes. We hand over clean, tested, documented systems with no lock-in — including the test harnesses and documentation the agents helped create, so your team can keep moving."),
  ],
  "contact_h2": ("Modernize the system", "holding you back."),
  "contact_sub": "Tell us about the legacy system, what it's blocking, and where it hurts most. We reply to every serious enquiry within one business day.",
  "cta": "Modernize the system holding you back", "cta_href": "mailto:machlilieslimited@gmail.com?subject=AI-native%20modernization%20enquiry",
  "cta2": "Talk to product engineering", "cta2_href": "/services/product-engineering/",
},

# ============================ FLAGSHIP OFFER ============================
"agentic-operations-sprint": {
  "title": "Agentic Operations Sprint | Mach Lilies",
  "desc": "The Agentic Operations Sprint is a focused engagement that maps your highest-value AI agent workflows, prototypes the strongest one, and prepares it for governed production — with an ROI model and rollout plan.",
  "keywords": "agentic operations sprint, AI agent discovery, AI workflow assessment, AI prototype engagement, AI ROI model, AI production rollout, AI opportunity assessment",
  "service_type": "Agentic operations discovery and prototype sprint",
  "eyebrow": "Flagship engagement",
  "h1": ("The Agentic", "Operations Sprint."),
  "lead": "A focused engagement that identifies, prototypes and business-cases your highest-value AI agent workflows — then prepares the strongest one for governed production. The clearest first step from AI experiments to agentic operations. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "What the Sprint is",
  "ov_hl": 'In one focused sprint: <span class="hl">map the workflows</span>, prototype the strongest, and leave with a <span class="hl">production plan.</span>',
  "ov_body": "The Agentic Operations Sprint is how most engagements with Mach Lilies begin. In a focused, fixed-scope sprint we map your highest-friction workflows, identify where agents can safely act, prototype the strongest opportunity against real inputs, and hand you a production rollout plan with governance, integrations, ROI and risk controls built in from the start. You finish with a working prototype, a clear business case, and a fixed-scope proposal — or a well-reasoned recommendation not to proceed.",
  "timeline_h2": ("Six phases,", "one focused sprint."),
  "timeline_note": "A clear sequence from mapping the work to a fixed-scope production proposal.",
  "timeline": [
    ("01","Workflow mapping","We interview operators, review tools and classify repeatable work — mapping handoffs and exceptions.","Workflow map & opportunity scorecard"),
    ("02","Data & system readiness","We check source documents, data quality, APIs, identity, permissions and tool access.","Readiness assessment & integration plan"),
    ("03","Risk & control design","We define where the agent can act, where humans approve, and what must be logged.","Control matrix & human-in-loop map"),
    ("04","Prototype","We build a narrow, working agent against realistic data and tool calls.","Working demo & quality evaluation"),
    ("05","Business case","We estimate time saved, error reduction, throughput and operational cost.","ROI model & production recommendation"),
    ("06","Rollout plan","We define the architecture, scope, implementation path and managed-service model.","Fixed-scope production proposal"),
  ],
  "sample_h2": ("A sample opportunity", "scorecard."),
  "sample_note": "Illustrative only — every Sprint produces this against your real workflows, not these examples.",
  "sample": [
    ("Renewal pack assembly","Value: high · Feasibility: high · Data readiness: medium","Recommendation: prototype first"),
    ("Inbox triage & routing","Value: high · Feasibility: medium · Data readiness: high","Recommendation: strong candidate"),
    ("Management report compilation","Value: medium · Feasibility: high · Data readiness: high","Recommendation: quick win"),
    ("Free-text exception handling","Value: medium · Feasibility: low · Data readiness: low","Recommendation: hold for now"),
  ],
  "svc_h2": ("What you", "walk away with."),
  "svc_note": "Concrete deliverables, not a slide deck — everything you need to make a confident production decision.",
  "services": [
    ("Workflow map", "Your highest-friction workflows mapped end to end — triggers, handoffs, exceptions and the manual effort they consume.", ["Mapping","Process"]),
    ("AI opportunity scorecard", "Each candidate workflow scored on value, feasibility, data readiness and risk, so the priority is obvious.", ["Scorecard","Priority"]),
    ("Data & source readiness check", "An honest assessment of the documents, data, APIs, identity and permissions an agent would need.", ["Data","APIs","Readiness"]),
    ("Risk & compliance review", "Where the agent can act, where humans approve, and what must be logged — the control matrix.", ["Risk","Controls","Approvals"]),
    ("Working prototype", "A narrow, working agent built against realistic data and tool calls, with a quality evaluation.", ["Prototype","Demo","Evals"]),
    ("ROI model", "An estimate of time saved, error reduction and throughput — the business case for production.", ["ROI","Business case"]),
    ("Production architecture", "How the strongest workflow would run in production — integrations, runtime and observability.", ["Architecture","Runtime"]),
    ("AgentOps & governance plan", "The permissions, approvals, logging, evaluation and incident controls the workflow needs to run safely.", ["AgentOps","Governance"]),
    ("Fixed-price rollout proposal", "A clear, fixed-scope proposal to take the chosen workflow to governed production.", ["Proposal","Fixed-scope"]),
  ],
  "method_h2": ("Sprint, rollout,", "operate, expand."),
  "method_note": "The Sprint is step one. It's designed to lead into production rollout and managed operation — at your pace.",
  "method": [
    ("01 / Sprint","Fixed-scope discovery","A focused sprint that maps workflows, prototypes the strongest, and produces a production plan."),
    ("02 / Rollout","Build to production","Milestone-based implementation of the chosen workflow, with governance built in from the start."),
    ("03 / Operate","Managed AgentOps","Monitoring, evaluation, cost control and optimisation as the workflow runs in production."),
    ("04 / Expand","More workflows","Once one workflow is proven and governed, extend to the next highest-value process."),
  ],
  "ind_h2": ("Who the Sprint", "is for."),
  "ind_note": "For leaders who know AI matters but need a safe, evidence-based way to get a real workflow into production.",
  "industries": ["Founders / CEO","COO / Operations","CTO / Engineering","Managing partners","Transformation leads","Operations directors","Mid-market","Scale-ups"],
  "why": [
    ("i","Fixed scope, fast","A focused engagement with a clear start, end and deliverables — not an open-ended retainer."),
    ("ii","A real prototype","You leave with something working against real inputs, not a slide deck of possibilities."),
    ("iii","Governance from day one","The rollout plan includes permissions, approvals, logging and evaluation — built in, not bolted on."),
    ("iv","An honest decision","If the strongest opportunity still isn't worth productionising, we'll tell you. Scale or kill, clearly."),
  ],
  "proof_hl": 'You finish with a <span class="hl">working prototype</span>, an <span class="hl">ROI model</span>, and a <span class="hl">fixed-scope rollout plan.</span>',
  "faq_h2": ("The Sprint,", "answered."),
  "faqs": [
    ("What is the Agentic Operations Sprint?", "It's a focused, fixed-scope engagement that maps your highest-value AI agent workflows, prototypes the strongest one against real inputs, and produces a production rollout plan with governance, integrations, ROI and risk controls. It's the clearest first step from AI experiments to agentic operations."),
    ("What do we get at the end?", "A workflow map and AI opportunity scorecard, a data and readiness check, a risk and compliance review, a working prototype with a quality evaluation, an ROI model, a production architecture, an AgentOps governance plan, and a fixed-price proposal to take the chosen workflow to production."),
    ("How long does the Sprint take?", "It's deliberately focused — a short, fixed-scope engagement rather than an open-ended project. We agree the exact scope and timeline up front, so you know precisely what you'll receive and when."),
    ("What does it cost?", "Most engagements start with a fixed-scope sprint, followed by milestone-based production rollout and optional managed AgentOps support. We scope and price the sprint to your workflows and share clear, indicative figures before any commitment."),
    ("What happens after the Sprint?", "If the business case holds, we move to a milestone-based production rollout with governance built in, and optionally operate the workflow as a managed service. If it doesn't, you'll have a clear, evidence-based recommendation not to proceed — which is valuable too."),
    ("How do we book a Sprint?", "Email machlilieslimited@gmail.com with the workflow you want to improve, the systems involved, the current manual effort, and any risk or compliance concerns. We reply to every serious enquiry within one business day."),
  ],
  "contact_h2": ("Book the", "Sprint."),
  "contact_sub": "Tell us the workflow you want to automate, the systems involved, the current manual effort, and any risk or compliance concerns. We reply to every serious enquiry within one business day.",
  "cta": "Book the Sprint", "cta_href": BOOKING_URL,
  "cta2": "Explore Agentic Operations", "cta2_href": "/services/agentic-operations/",
},

# ====================== FOUNDATION (delivery bench) ======================
"ai-consulting": {
  "title": "AI Consulting & Engineering Services | Mach Lilies",
  "desc": "AI consulting that ships. Mach Lilies designs, builds and operates AI, LLM and machine-learning systems in production — the engineering bench behind our agentic operations work. Free first consultation.",
  "keywords": "AI consulting, AI consultancy, AI consulting services, machine learning consulting, LLM development, generative AI consultant, RAG, MLOps, AI strategy, AI agents",
  "service_type": "AI and machine learning consulting",
  "eyebrow": "AI & Machine Learning Engineering",
  "h1": ("AI consulting,", "engineered into production."),
  "lead": "Mach Lilies takes artificial intelligence from idea to impact: AI strategy, LLM and machine-learning systems, and the MLOps to run them. It's the engineering bench behind our <strong>agentic operations</strong> work — generative AI, RAG and agents, taken to production and operated, not stalled as a demo. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "What is AI consulting",
  "ov_hl": 'AI consulting turns <span class="hl">artificial intelligence</span> into outcomes — <span class="dim">strategy, build and run,</span> not just slideware.',
  "ov_body": "Most AI projects die between the proof of concept and production. We exist to close that gap. As a senior, founder-led AI and machine-learning practice, Mach Lilies helps teams find the use cases that pay off, build generative-AI, LLM and ML systems that work under real load, and operate them with proper MLOps. Increasingly, that work leads into agentic operations — designing, governing and operating AI agents that run real workflows, which is now the core of what we do. Every engagement is staffed by principals and handed off as clean, documented systems you own.",
  "svc_h2": ("AI services,", "end to end."),
  "svc_note": "From generative AI and LLM apps to custom machine learning and MLOps — and the agents that put them to work.",
  "services": [
    ("Generative AI & LLM apps", "Production LLM applications — copilots, assistants, and document and content workflows — built on Claude, GPT and open-source models.", ["LLMs","Copilots","GenAI"]),
    ("RAG & knowledge systems", "Retrieval-augmented generation over your own data: vector search, grounding, evaluation and guardrails that keep answers accurate.", ["RAG","Vector DB","Embeddings"]),
    ("AI agents & automation", "Tool-using agents and workflow automation that take real actions safely — the building blocks of agentic operations.", ["Agents","Tools","Workflows"]),
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
    ("04 / Operate","Keep it sharp","MLOps: monitoring, evaluation, retraining and cost control, so quality holds over time."),
  ],
  "ind_h2": ("AI for", "real industries."),
  "ind_note": "We ship AI for regulated, high-stakes domains — for both venture-backed startups and enterprises.",
  "industries": ["FinTech","HealthTech","Logistics","Retail & Commerce","B2B SaaS","Startups","Enterprise"],
  "why": [
    ("i","Senior, founder-led","The principals who scope your AI are the ones who build it. No hand-off to juniors."),
    ("ii","Production-first","We optimise for systems that survive real users and real load — not demo-day theatre."),
    ("iii","Model-agnostic","Claude, GPT or open-source — we pick on cost, privacy and fit, never vendor loyalty."),
    ("iv","Yours to own","Clean, documented, no lock-in. We engineer our own hand-off and your team inherits it."),
  ],
  "proof_hl": 'AI taken to <span class="hl">production</span> — strategy, build and <span class="hl">MLOps</span>, measured against <span class="dim">outcomes.</span>',
  "faq_h2": ("AI consulting,", "answered."),
  "faqs": [
    ("What is AI consulting?", "AI consulting is the practice of helping an organisation identify, design, build and operate artificial-intelligence and machine-learning systems that deliver measurable business value. A good AI consultancy covers the full path — from strategy and feasibility through to production engineering and ongoing MLOps — not just slideware or one-off demos."),
    ("How does this relate to agentic operations?", "AI consulting is the engineering foundation; agentic operations is where it pays off. The LLM, RAG, agent and MLOps work here is what we use to build and operate the governed agent workflows in our Agentic Operations and AgentOps services."),
    ("How much does AI consulting cost?", "It depends on scope. Most engagements begin with a free consultation and a short, fixed-fee discovery to validate the use case, followed by milestone-based delivery priced to outcomes rather than headcount. Contact us for a tailored quote."),
    ("How long does an AI project take?", "A working prototype is usually weeks, not months. Production-grade deployment depends on data readiness, integration and compliance, but our model is to ship something real early and harden it iteratively."),
    ("Which AI models and providers do you work with?", "We are model-agnostic. We build with leading frontier models such as Anthropic Claude and OpenAI GPT, and with open-source models like Llama and Mistral when they fit better on cost, privacy or control. We recommend the right tool for the job rather than a single vendor."),
    ("Should I use RAG or fine-tuning?", "Most use cases that need current, proprietary or factual knowledge are best served by retrieval-augmented generation (RAG), which grounds the model in your data. Fine-tuning helps for fixed style, format or narrow tasks. We often combine both — and will advise based on your data and goals."),
    ("Is our data kept secure and private?", "Yes. We design for data privacy and security from the start — including private deployments, isolation of sensitive data, and provider options that do not train on your data. We work to enterprise-grade standards and align with frameworks such as ISO 27001."),
  ],
  "contact_h2": ("Put AI", "to work."),
  "contact_sub": "Tell us what you're building. We reply to every serious enquiry within one business day — and the first consultation is free.",
  "cta": "Book a free consultation", "cta_href": "mailto:machlilieslimited@gmail.com?subject=AI%20consulting%20enquiry",
  "cta2": "Explore Agentic Operations", "cta2_href": "/services/agentic-operations/",
},

"product-engineering": {
  "title": "Product Engineering & Custom Software | Mach Lilies",
  "desc": "Custom software engineering from Mach Lilies — full-stack web and mobile products built to scale and engineered to last, now accelerated by AI-assisted delivery and senior review. Free consultation.",
  "keywords": "custom software development, product engineering, MVP development, web app development, mobile app development, software consultancy, full-stack development, AI-assisted development",
  "service_type": "Custom software engineering",
  "eyebrow": "Product & Software Engineering",
  "h1": ("Custom software,", "built to last."),
  "lead": "Mach Lilies is a <strong>product engineering</strong> studio that turns ambitious ideas into production software. We design and build full-stack web and mobile products — accelerated by AI-assisted delivery, governed by senior engineers — engineered to scale and made to last. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "What is product engineering",
  "ov_hl": 'Most software is <span class="dim">disposable.</span> We build the kind <span class="hl">worth keeping.</span>',
  "ov_body": "Product engineering is more than writing code — it's owning the outcome: the architecture, the build, the quality and the scale. As a senior, founder-led software practice, Mach Lilies designs and ships full-stack web and mobile products that are fast to release and honest under load. We use AI-assisted delivery to move at startup speed, with senior engineers owning architecture, security and review — so you don't inherit the technical debt you'll regret. For existing systems, see our AI-Native Modernization service.",
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
    ("iii","AI-assisted, human-governed","Agents accelerate the build; senior engineers own architecture, security and review."),
    ("iv","Yours to own","Clean code, full documentation, no lock-in. Your team inherits it cleanly."),
  ],
  "proof_hl": 'Production software — <span class="hl">tested</span>, <span class="hl">observable</span>, and <span class="dim">documented to outlive us.</span>',
  "faq_h2": ("Product engineering,", "answered."),
  "faqs": [
    ("What is product engineering?", "Product engineering is the end-to-end design and build of software products — owning architecture, development, quality and scale, not just writing features. It blends engineering, product thinking and design to ship software that works in the real world and keeps working."),
    ("How is Mach Lilies different from a typical dev agency?", "We're a small, senior studio: the principals who scope your product build it. We optimise for production quality and long-term ownership rather than billable hours, use AI-assisted delivery to move faster, and engineer a clean hand-off so you're never locked in."),
    ("Can you build an MVP for my startup?", "Yes. We specialise in taking startups from zero to a fundable, real product in weeks — fast, but without the technical debt that slows you down later."),
    ("What technology stack do you use?", "We're pragmatic: typically TypeScript with React/Next.js on the front end, robust back ends (Node, Python, Go) and cloud-native infrastructure. We choose tools for fit and longevity, not hype."),
    ("Do you build both web and mobile?", "Yes — modern web applications and native or cross-platform mobile apps, often sharing logic across a maintainable codebase."),
    ("Will I own the code?", "Always. You own all code and IP, with full documentation and no lock-in. We engineer our own hand-off."),
    ("How do you ensure quality?", "Automated testing, CI/CD, code review and observability are part of every build from day one — so quality is designed in, not inspected at the end."),
  ],
  "contact_h2": ("Build your", "product."),
  "contact_sub": "Tell us what you're building. We reply to every serious enquiry within one business day — and the first consultation is free.",
  "cta": "Book a free consultation", "cta_href": "mailto:machlilieslimited@gmail.com?subject=Product%20engineering%20enquiry",
  "cta2": "See AI-native modernization", "cta2_href": "/services/ai-modernisation-factory/",
},

"cloud-platform": {
  "title": "Cloud & Platform Engineering Consulting | Mach Lilies",
  "desc": "Cloud consulting from Mach Lilies — cloud-native architecture, migration, Kubernetes, DevOps and SRE. Reliable, cost-efficient platforms, and the secure runtime your AI agents run on. Free consultation.",
  "keywords": "cloud consulting, cloud migration, Kubernetes consulting, DevOps consulting, cloud architecture, SRE, infrastructure as code, cloud cost optimization, AI agent runtime",
  "service_type": "Cloud architecture and DevOps consulting",
  "eyebrow": "Cloud & Platform Engineering",
  "h1": ("Cloud platforms,", "reliable by design."),
  "lead": "Mach Lilies is a <strong>cloud consultancy</strong> that designs, builds and runs cloud-native platforms. From migration and Kubernetes to DevOps, reliability and cost control — infrastructure you can sleep through, and the secure runtime your AI agents observe and operate on. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "What is cloud consulting",
  "ov_hl": 'Cloud done right is <span class="hl">invisible</span> — fast, resilient and <span class="dim">quietly affordable.</span>',
  "ov_body": "Cloud consulting is about more than lifting servers — it's architecting platforms that scale, stay up, and don't quietly drain your budget. As a senior, vendor-neutral cloud and platform practice, Mach Lilies designs cloud-native systems on AWS, GCP and Azure, automates them with infrastructure-as-code, and operates them with real reliability engineering — including the secure, observable runtime that production AI agents depend on.",
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
  "proof_hl": 'Platforms engineered for <span class="hl">uptime</span>, <span class="hl">scale</span>, and <span class="dim">cost you can defend.</span>',
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
  "cta": "Book a free consultation", "cta_href": "mailto:machlilieslimited@gmail.com?subject=Cloud%20%26%20platform%20enquiry",
  "cta2": "Explore AgentOps", "cta2_href": "/services/agentops-ai-governance/",
},

"data-analytics": {
  "title": "Data Engineering & Analytics Consulting | Mach Lilies",
  "desc": "Data consulting from Mach Lilies — data engineering, pipelines, warehousing, analytics and BI that turn raw data into decisions, and the AI-ready foundation your agents and models need. Free consultation.",
  "keywords": "data engineering consulting, data analytics consulting, data pipeline, data warehouse, business intelligence, real-time data, analytics, data platform, AI-ready data",
  "service_type": "Data engineering and analytics consulting",
  "eyebrow": "Data Engineering & Analytics",
  "h1": ("Data you can", "act on."),
  "lead": "Mach Lilies is a <strong>data consultancy</strong> that builds the pipelines, warehouses and analytics that turn raw data into decisions — and the clean, grounded foundation your AI agents and models need to work. From real-time ingestion to dashboards people trust. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "What is data engineering",
  "ov_hl": 'Raw data is noise. We turn it into <span class="hl">insight you can act on</span> — <span class="dim">reliably.</span>',
  "ov_body": "Data engineering builds the plumbing — pipelines, warehouses and models — that makes analytics and AI possible; analytics turns that data into decisions. As a senior data practice, Mach Lilies designs modern data platforms (Snowflake, BigQuery, Databricks), builds trustworthy pipelines, and delivers analytics people actually use — including the AI-ready, well-grounded data foundation that retrieval, agents and ML depend on.",
  "svc_h2": ("What we", "build."),
  "svc_note": "Pipelines, warehouses, analytics and governance — engaged together or à la carte.",
  "services": [
    ("Data pipelines", "Reliable batch and streaming pipelines (ELT) you can trust to be correct and on time.", ["ELT","Airflow","dbt"]),
    ("Data warehousing", "Modern warehouses and lakehouses — Snowflake, BigQuery, Databricks — modeled well.", ["Snowflake","BigQuery","Lakehouse"]),
    ("Analytics & BI", "Dashboards and self-serve analytics people actually use to make decisions.", ["BI","Dashboards","Metrics"]),
    ("Real-time & streaming", "Event pipelines for sub-second insight and operational analytics.", ["Streaming","Kafka","Real-time"]),
    ("Data platform & governance", "Quality, lineage, cataloguing and governance that scale with the organisation.", ["Quality","Lineage","Governance"]),
    ("AI-ready data", "The clean, well-modeled, well-grounded data foundation that AI agents and ML actually need.", ["ML data","Retrieval","Foundation"]),
  ],
  "method_h2": ("From raw", "to decisions."),
  "method_note": "Four movements from scattered data to a platform that drives decisions and AI.",
  "method": [
    ("01 / Map","Audit the data","We map sources, quality and the questions the business actually needs answered."),
    ("02 / Model","Design the platform","A warehouse and data model built for trust, performance and change."),
    ("03 / Build","Pipe it reliably","Tested pipelines with quality checks, so the numbers are right every time."),
    ("04 / Activate","Insight & AI","Analytics, dashboards and the data foundation your ML and AI agents build on."),
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
  "proof_hl": 'Data you can <span class="hl">trust</span> and <span class="hl">act on</span> — the foundation your <span class="dim">AI needs.</span>',
  "faq_h2": ("Data consulting,", "answered."),
  "faqs": [
    ("What is data engineering?", "Data engineering is the design and build of the systems that collect, move, store and prepare data — pipelines, warehouses and models — so it's reliable and ready for analytics and AI. It's the foundation everything data-driven stands on."),
    ("What's the difference between data engineering and analytics?", "Data engineering builds the trustworthy data foundation; analytics (and BI) turns that data into insight and decisions. We do both, so the two fit together cleanly."),
    ("Which data warehouse should we use?", "It depends on your scale, ecosystem and team. We're neutral across Snowflake, BigQuery and Databricks and will recommend the best fit rather than a default."),
    ("Do we need real-time or is batch enough?", "Most reporting is well served by batch. Real-time matters when decisions are operational and time-sensitive. We'll recommend the simplest approach that meets the need."),
    ("How do you ensure data quality?", "With testing, validation, monitoring and lineage built into the pipelines (using tools like dbt) — so issues are caught early and the numbers can be trusted."),
    ("Can you make our data AI-ready?", "Yes. A clean, well-modeled, well-governed data foundation is exactly what AI agents and ML need. We build that foundation and connect it to our AI and agentic operations work."),
    ("Do you build dashboards and BI?", "Yes — we deliver dashboards and self-serve analytics designed for adoption, so people actually use them to make decisions."),
  ],
  "contact_h2": ("Put your data", "to work."),
  "contact_sub": "Tell us about your data. We reply to every serious enquiry within one business day — and the first consultation is free.",
  "cta": "Book a free consultation", "cta_href": "mailto:machlilieslimited@gmail.com?subject=Data%20%26%20analytics%20enquiry",
  "cta2": "Explore Agentic Operations", "cta2_href": "/services/agentic-operations/",
},

"design-experience": {
  "title": "Product Design & UX/UI Services | Mach Lilies",
  "desc": "Product design from Mach Lilies — UX/UI, design systems, brand and motion for digital products, including the human-approval and oversight interfaces that govern AI agents. Free consultation.",
  "keywords": "product design agency, UX/UI design services, design systems, brand design, digital product design, motion design, design engineering, human-in-the-loop UX",
  "service_type": "Product and experience design",
  "eyebrow": "Design & Experience",
  "h1": ("Interfaces that feel", "inevitable."),
  "lead": "Mach Lilies designs <strong>digital products</strong> people love to use — product UX/UI, design systems, brand and motion — including the review, approval and oversight interfaces that keep humans in control of AI agents. Beautiful, usable, accessible, and engineered to ship. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "What is product design",
  "ov_hl": 'The best interface is the one users <span class="hl">forget they\'re using.</span>',
  "ov_body": "Product design is where usefulness meets craft — the flows, the interface, the brand and the motion that make a product feel inevitable. As a senior design and experience studio that also engineers, Mach Lilies designs digital products that are beautiful and usable, grounded in research and built as systems — including the human-in-the-loop approval and oversight experiences that make agentic operations safe to run. Then we bridge design and code, so the build matches the vision.",
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
    ("04 / Ship","Build with eng","We bridge to engineering, so the build matches the vision, pixel for pixel."),
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
  "proof_hl": 'Interfaces that are <span class="hl">usable</span>, <span class="hl">accessible</span>, and <span class="dim">built to ship.</span>',
  "faq_h2": ("Product design,", "answered."),
  "faqs": [
    ("What does a product design agency do?", "A product design agency designs digital products end to end — user research, UX flows, UI design, design systems, brand and motion — so a product is both usable and desirable, and ready to build."),
    ("What's the difference between UX and UI?", "UX (user experience) is how a product works — the flows, structure and usability. UI (user interface) is how it looks and feels — the visual and interactive layer. Great products need both, designed together."),
    ("What is a design system?", "A design system is a documented library of reusable components, patterns and tokens that keeps a product consistent and lets teams build faster. We design systems engineers love to use."),
    ("Do you design interfaces for AI features?", "Yes — including the human-in-the-loop experiences that make AI safe: review queues, approval flows, escalation and oversight dashboards. Good design is what keeps a person comfortably in control of an agent."),
    ("Do you only design, or also build?", "Both. We're a design studio that also engineers, so we can take a product from research and design through to a faithful, shipped build."),
    ("Is accessibility included?", "Yes. We design to accessibility standards (WCAG) by default, so products are usable by as many people as possible."),
    ("How do you hand off to engineers?", "We deliver clean source files, a documented design system and design-engineering support — and often build the front end ourselves, so nothing is lost in translation."),
  ],
  "contact_h2": ("Design something", "rare."),
  "contact_sub": "Tell us what you're designing. We reply to every serious enquiry within one business day — and the first consultation is free.",
  "cta": "Book a free consultation", "cta_href": "mailto:machlilieslimited@gmail.com?subject=Product%20design%20enquiry",
  "cta2": "Explore Agentic Operations", "cta2_href": "/services/agentic-operations/",
},

"strategy-advisory": {
  "title": "Technology Strategy, AI Governance & Fractional CTO | Mach Lilies",
  "desc": "Technology strategy and advisory from Mach Lilies — fractional CTO, technical due diligence, AI readiness, AI governance and AgentOps roadmaps. Senior, operator-led guidance when it counts.",
  "keywords": "technology consulting, fractional CTO, technical due diligence, technology strategy, AI readiness, AI governance, AgentOps roadmap, vendor AI risk, technology advisory",
  "service_type": "Technology strategy and advisory",
  "eyebrow": "Strategy & Advisory",
  "h1": ("Senior guidance,", "when it counts."),
  "lead": "Mach Lilies provides <strong>technology strategy and advisory</strong> for founders, investors and leaders — fractional CTO leadership, technical due diligence, AI readiness, AI governance and AgentOps roadmaps. Clarity from people who have actually built the thing. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "What is technology advisory",
  "ov_hl": 'Decisions are cheap to make and <span class="hl">expensive to get wrong.</span>',
  "ov_body": "Technology strategy and advisory is senior, operator-level guidance for the decisions that matter — what to build, whether to buy, how to adopt AI safely, how to scale, and who to hire. As a founder-led practice, Mach Lilies acts as a fractional CTO, runs technical due diligence for investors, and turns ambition into sequenced, fundable roadmaps — including AI readiness, AI governance and AgentOps roadmaps for boards that need clarity before they build. Candid advice from people who have built and run the systems, not just advised on them.",
  "svc_h2": ("How we", "advise."),
  "svc_note": "Fractional leadership, due diligence, roadmaps, AI governance and reviews — engaged together or à la carte.",
  "services": [
    ("Fractional CTO", "Senior technical leadership, part-time, for startups and scale-ups that aren't ready for a full-time CTO.", ["Fractional","Leadership","CTO"]),
    ("Technical due diligence", "For investors: assess a target's technology, team and risk before you commit capital.", ["Due diligence","Investors","Risk"]),
    ("Technology roadmaps", "Turn ambition into a sequenced, fundable plan your team and board can rally behind.", ["Roadmap","Planning","Strategy"]),
    ("AI readiness & governance", "Where AI pays off, what's needed, and how to adopt it safely — readiness, governance and AgentOps roadmaps.", ["AI readiness","Governance","AgentOps"]),
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
  "proof_hl": 'Senior judgement on the <span class="hl">big calls</span> — strategy, <span class="hl">due diligence</span> and <span class="dim">safe AI adoption.</span>',
  "faq_h2": ("Advisory,", "answered."),
  "faqs": [
    ("What is a fractional CTO?", "A fractional CTO is an experienced technology leader who works with you part-time — setting technical direction, leading the team and making key decisions — at a fraction of the cost and commitment of a full-time hire. Ideal for startups and scale-ups."),
    ("What is technical due diligence?", "Technical due diligence is an independent assessment of a company's technology, architecture, team, security and risks — usually for investors or acquirers evaluating a deal. We deliver a clear, honest report you can act on."),
    ("Can you advise on AI governance and risk?", "Yes. We help boards and leadership teams build AI readiness, AI usage policy, vendor AI risk reviews and AgentOps roadmaps — and we can implement the controls through our AI Assurance and AgentOps services."),
    ("What is an AI readiness assessment?", "It's an evaluation of where AI can realistically create value for you, what data and capabilities you'd need, the build-vs-buy options and a pragmatic roadmap — so you invest in AI with eyes open."),
    ("Do you do due diligence for investors?", "Yes. We run technical due diligence for VCs, PE firms and acquirers — assessing the technology, team and risks of a target — discreetly and on tight timelines."),
    ("How are advisory engagements structured?", "Flexibly — from a one-off assessment or due-diligence report to an ongoing fractional-CTO retainer. We scope to the decision and timeline you're facing."),
    ("Is it confidential?", "Always. We work under NDA as standard and treat every engagement as strictly confidential."),
  ],
  "contact_h2": ("Get the", "clarity."),
  "contact_sub": "Tell us the decision you're facing. We reply to every serious enquiry within one business day — and the first consultation is free.",
  "cta": "Book a free consultation", "cta_href": "mailto:machlilieslimited@gmail.com?subject=Strategy%20%26%20advisory%20enquiry",
  "cta2": "See AI assurance", "cta2_href": "/services/ai-assurance-evaluation/",
},
}

# ============================ INDUSTRY (VERTICAL) PAGES ============================
IND_SHORT = {
    "insurance-brokers":     "Insurance Brokers",
    "accountancy-practices": "Accountancy Practices",
}
INDUSTRY_ORDER = ["insurance-brokers", "accountancy-practices"]

INDUSTRIES = {
"insurance-brokers": {
  "title": "AI Agents for Insurance Brokers | Mach Lilies",
  "desc": "Governed AI agents for broker inboxes, renewal packs, claims intake, missing-document chasing and compliance evidence — with broker approval and a clear audit trail.",
  "keywords": "AI agents for insurance brokers, insurance broking automation, renewal pack automation, claims intake AI, broker workflow automation, insurance back-office AI",
  "service_type": "Agentic operations for insurance brokers",
  "eyebrow": "Agentic Operations for Insurance Brokers",
  "h1": ("Renewal and claims admin,", "handled by governed AI agents."),
  "lead": "Mach Lilies builds agentic workflows for broker inboxes, policy documents, renewal packs, claims intake, customer updates and compliance evidence — with broker approval and a clear audit trail. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "The pain",
  "ov_hl": 'Senior broker time disappears into <span class="dim">inboxes, chasing and paperwork</span> — not <span class="hl">advice and relationships.</span>',
  "ov_body": "Broking runs on documents, email and deadlines: renewals to prepare, insurers to compare, claims to log, clients to chase for missing information, and evidence to keep for compliance. Most of it is repeatable, deadline-driven admin that consumes your most experienced people. Mach Lilies builds bounded AI agents that take the repetitive load off broker inboxes and documents — drafting, gathering and updating — while brokers approve anything that carries risk, and every step is logged for audit.",
  "svc_h2": ("Broker workflows", "we operate."),
  "svc_note": "Bounded agents for the repeatable, deadline-driven admin that consumes senior broker time.",
  "services": [
    ("Renewal pack agent", "Assembles renewal packs from policy systems and documents, flags gaps and prepares a draft for broker review.", ["Renewals","Documents","Drafting"]),
    ("Policy comparison agent", "Extracts and compares cover, terms and exclusions across quotes to support a faster, clearer recommendation.", ["Comparison","Extraction","Quotes"]),
    ("Claims intake agent", "Captures first notification of loss, records the detail, classifies and routes claims to the right handler.", ["Claims","FNOL","Routing"]),
    ("Missing-document chase", "Identifies what's outstanding and drafts follow-ups to clients and insurers — politely and on schedule.", ["Chasing","Follow-up","Email"]),
    ("Compliance evidence agent", "Gathers and files the evidence a broker needs to demonstrate process — every action logged.", ["Evidence","Audit","Records"]),
    ("Customer update drafts", "Drafts clear status updates for clients at each step, ready for a broker to review and send.", ["Updates","Comms","Drafting"]),
  ],
  "method_h2": ("Map, prototype,", "govern, operate."),
  "method_note": "How a broker workflow becomes a governed agent — with you in control at every step.",
  "method": [
    ("01 / Map","Pick the workflow","We start with the renewal, claims or chasing workflow that costs your team the most time."),
    ("02 / Prototype","Prove it on real cases","A working agent against real, anonymised broker documents and cases, evaluated for accuracy."),
    ("03 / Govern","Broker stays in control","Broker approval on anything that carries risk, least-privilege access, and a full audit trail."),
    ("04 / Operate","Run and improve","We monitor quality, handle exceptions, and expand to the next workflow as confidence grows."),
  ],
  "ind_h2": ("Systems we", "work across."),
  "ind_note": "Bounded, least-privilege connectors into the tools brokers already use.",
  "industries": ["Email / Outlook","Broker CRM","Policy & quote systems","Document storage","Finance systems","Insurer portals","Acturis-style platforms","Spreadsheets"],
  "why": [
    ("i","Broker approval","Agents draft, gather and compare; a broker signs off anything that goes to a client or insurer."),
    ("ii","Least-privilege access","Each agent only touches the systems and data its workflow needs — nothing more."),
    ("iii","Full audit trail","Every action, document and approval is logged, so your process is evidenced for compliance."),
    ("iv","Exception escalation","Anything unusual is flagged to a person rather than guessed at."),
  ],
  "proof_hl": 'Faster renewals and claims admin, fewer missed handoffs, and a <span class="hl">clear audit trail</span> — with <span class="hl">brokers in control.</span>',
  "faq_h2": ("Brokers,", "answered."),
  "faqs": [
    ("Will an AI agent talk to my clients without me?", "No. Agents draft customer updates and chase missing documents, but a broker approves anything that goes out where it matters. The agent removes the preparation work; you keep the relationship and the final say."),
    ("Can it work with our broker management system?", "Typically yes. We build least-privilege connectors into the systems brokers use — email, CRM, policy and quote systems, document storage and finance tools — scoped to the specific workflow."),
    ("Is this compliant?", "We design for compliance support rather than making regulatory guarantees: least-privilege access, human approval where risk lives, and a complete audit trail of every action and approval, so you can evidence your process. We work to ISO 27001-aligned security practices."),
    ("What's the first workflow you'd recommend?", "Usually renewal pack preparation or missing-document chasing — they're repeatable, deadline-driven and measurable, which makes them a strong, low-risk first agent."),
    ("How do we start?", "With an Agentic Operations Sprint focused on one broker workflow: we map it, prototype an agent against real cases, and produce a rollout plan with governance built in."),
  ],
  "contact_h2": ("Map your first", "broker workflow."),
  "contact_sub": "Tell us which broker workflow costs your team the most time — renewals, claims, chasing or compliance evidence — and the systems involved. We reply within one business day.",
  "cta": "Map your first broker workflow", "cta_href": "mailto:machlilieslimited@gmail.com?subject=AI%20agents%20for%20insurance%20broking",
  "cta2": "Book an Agentic Operations Sprint", "cta2_href": "/services/agentic-operations-sprint/",
},

"accountancy-practices": {
  "title": "AI Agents for Accountancy Practices | Mach Lilies",
  "desc": "Governed AI agents for client document chasing, invoice and receipt classification, month-end close, VAT preparation and exception triage — with accountant approval and a clear audit trail.",
  "keywords": "AI agents for accountants, accountancy practice automation, client document chase, invoice classification AI, month-end close automation, VAT prep AI, bookkeeping automation",
  "service_type": "Agentic operations for accountancy practices",
  "eyebrow": "Agentic Operations for Accountancy Practices",
  "h1": ("Client chasing and month-end,", "handled by governed AI agents."),
  "lead": "Mach Lilies builds agentic workflows for client document chasing, invoice and receipt classification, month-end close, VAT preparation and exception triage — with accountant approval and a clear audit trail. <strong>Mach speed. Lily craft.</strong>",
  "ov_eyebrow": "The pain",
  "ov_hl": 'Practice capacity is eaten by <span class="dim">chasing clients and classifying paperwork</span> — not <span class="hl">advisory work.</span>',
  "ov_body": "Practices lose enormous time to repetitive admin: chasing clients for records, classifying invoices and receipts, reconciling, preparing VAT returns and pushing through month-end. It's deadline-driven, high-volume and rules-based — exactly where bounded AI agents help. Mach Lilies builds agents that chase, classify and prepare, while your accountants approve and review the work, and every action is logged for audit.",
  "svc_h2": ("Practice workflows", "we operate."),
  "svc_note": "Bounded agents for the high-volume, deadline-driven admin that limits practice capacity.",
  "services": [
    ("Client document chase", "Identifies missing records and drafts polite, scheduled follow-ups to clients until the file is complete.", ["Chasing","Records","Follow-up"]),
    ("Invoice & receipt classification", "Reads, classifies and codes invoices and receipts, flagging anything ambiguous for review.", ["Classification","Coding","Documents"]),
    ("Month-end close assistant", "Runs the repeatable close checklist, reconciles routine items and surfaces exceptions to the team.", ["Close","Reconcile","Checklist"]),
    ("VAT prep assistant", "Prepares VAT-return workings from the books and flags items that need an accountant's judgement.", ["VAT","Prep","Workings"]),
    ("Exception triage", "Sorts and routes the exceptions that need a human, so accountants spend time only where it counts.", ["Exceptions","Triage","Routing"]),
    ("Client update drafts", "Drafts status and request updates to clients, ready for review and sending.", ["Updates","Comms","Drafting"]),
  ],
  "method_h2": ("Map, prototype,", "govern, operate."),
  "method_note": "How a practice workflow becomes a governed agent — reviewed by your accountants at every step.",
  "method": [
    ("01 / Map","Pick the workflow","We start with chasing, classification or close — whichever costs the practice the most time."),
    ("02 / Prototype","Prove it on real files","A working agent against real, anonymised client records, evaluated for accuracy."),
    ("03 / Govern","Accountant in control","Accountant approval on judgement calls, least-privilege access, and a full audit trail."),
    ("04 / Operate","Run through the cycle","We operate it through month-end and quarter-end, improving it as volumes and rules change."),
  ],
  "ind_h2": ("Systems we", "work across."),
  "ind_note": "Bounded, least-privilege connectors into the tools your practice already uses.",
  "industries": ["Email / Outlook","Practice management","Xero / QuickBooks","Bookkeeping ledgers","Document portals","Client record stores","Spreadsheets","Workflow tools"],
  "why": [
    ("i","Accountant approval","Agents chase, classify and prepare; an accountant approves judgement calls and reviews the output."),
    ("ii","Least-privilege access","Each agent only touches the records and systems its workflow needs."),
    ("iii","Full audit trail","Every classification, chase and approval is logged, so the work is reviewable and evidenced."),
    ("iv","Exception escalation","Ambiguous items are flagged for a human rather than guessed at."),
  ],
  "proof_hl": 'More capacity for advisory work, faster month-end, and a <span class="hl">clear audit trail</span> — with <span class="hl">accountants in control.</span>',
  "faq_h2": ("Practices,", "answered."),
  "faqs": [
    ("Will an agent file returns or move money on its own?", "No. Agents prepare workings, classify and chase; an accountant approves and submits anything that carries risk or judgement. The agent removes preparation effort, not professional responsibility."),
    ("Does it work with Xero or QuickBooks?", "Typically yes. We build least-privilege connectors into the practice-management, bookkeeping and document tools you already use, scoped to the specific workflow."),
    ("Is client data kept secure?", "Yes. We design for least-privilege access, isolation of client data, human approval for sensitive actions, and a full audit trail — working to ISO 27001-aligned security practices."),
    ("Which workflow should we automate first?", "Usually client document chasing or invoice and receipt classification — high-volume, repetitive and measurable, which makes a strong first agent."),
    ("How do we start?", "With an Agentic Operations Sprint focused on one practice workflow: we map it, prototype an agent against real files, and produce a rollout plan with governance built in."),
  ],
  "contact_h2": ("Map your first", "practice workflow."),
  "contact_sub": "Tell us which workflow limits your capacity — chasing, classification, close or VAT prep — and the systems involved. We reply within one business day.",
  "cta": "Map your first practice workflow", "cta_href": "mailto:machlilieslimited@gmail.com?subject=AI%20agents%20for%20accountancy%20practices",
  "cta2": "Book an Agentic Operations Sprint", "cta2_href": "/services/agentic-operations-sprint/",
},
}

# related-services mesh for industry pages (targets are services)
RELATED.update({
    "insurance-brokers":     ["agentic-operations", "agentops-ai-governance", SPRINT],
    "accountancy-practices": ["agentic-operations", "agentops-ai-governance", SPRINT],
})

# ---------------------------------------------------------------------------
NAV = '''    <nav class="nav" id="nav">
        <a href="/" class="brand" data-cursor>
            <img class="brand-mark" src="/assets/logo-mark.svg" alt="Mach Lilies" width="38" height="38" />
            <span>
                <span class="b-name">Mach Lilies</span>
                <span class="b-sub">Agentic Operations</span>
            </span>
        </a>
        <div class="nav-links" id="nav-links">
            <a href="/services/agentic-operations/"><span class="idx">01</span>Agentic Ops</a>
            <a href="/services/agentops-ai-governance/"><span class="idx">02</span>AgentOps</a>
            <a href="/services/ai-pilot-rescue/"><span class="idx">03</span>Pilot Rescue</a>
            <a href="/services/ai-modernisation-factory/"><span class="idx">04</span>Modernization</a>
        </div>
        <a href="/services/agentic-operations-sprint/" class="nav-cta magnetic" data-cursor data-event="cta_sprint">Book a Sprint</a>
        <button class="burger" id="burger" aria-label="Open menu"><span></span><span></span></button>
    </nav>
    <div class="mobile-menu" id="mobile-menu">
        <a href="/services/agentic-operations/"><span class="idx">01</span>Agentic Ops</a>
        <a href="/services/agentops-ai-governance/"><span class="idx">02</span>AgentOps</a>
        <a href="/services/ai-pilot-rescue/"><span class="idx">03</span>Pilot Rescue</a>
        <a href="/services/ai-assurance-evaluation/"><span class="idx">04</span>AI Assurance</a>
        <a href="/services/ai-modernisation-factory/"><span class="idx">05</span>Modernization</a>
        <a href="/services/agentic-operations-sprint/"><span class="idx">06</span>The Sprint</a>
        <a href="/contact/"><span class="idx">07</span>Contact</a>
        <div class="mm-foot">machlilieslimited@gmail.com</div>
    </div>'''

def footer():
    svc_links = "\n".join(
        '                    <a href="/services/%s/">%s</a>' % (s, esc(SHORT[s][0]))
        for s in FOOTER_SERVICES)
    ind_links = "\n".join(
        '                    <a href="/industries/%s/">%s</a>' % (s, esc(IND_SHORT[s]))
        for s in INDUSTRY_ORDER)
    return '''    <footer class="footer">
        <div class="wrap">
            <span class="foot-word">Mach<span class="it"> Lilies</span></span>
            <div class="foot-cols">
                <div class="foot-col">
                    <h5>The practice</h5>
                    <p>An independent agentic operations &amp; AI engineering consultancy. We design, govern and operate safe AI agent workflows that do real business work.</p>
                </div>
                <div class="foot-col">
                    <h5>Services</h5>
%s
                </div>
                <div class="foot-col">
                    <h5>Industries</h5>
%s
                    <a href="/#capabilities" style="margin-top:0.4rem">What we do</a>
                    <a href="/#faq">FAQ</a>
                </div>
                <div class="foot-col">
                    <h5>Contact</h5>
                    <a href="/contact/">Start a conversation</a>
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
    </footer>''' % (svc_links, ind_links)

def jsonld(d, url, short_name, crumb_name, crumb_href):
    graph = [
        {"@type": ["Organization","ProfessionalService"], "@id": BASE+"/#org",
         "name":"Mach Lilies","legalName":"Mach Lilies Limited","url":BASE+"/",
         "logo":BASE+"/assets/logo-mark.svg","email":"machlilieslimited@gmail.com",
         "slogan":"Mach speed. Lily craft.","areaServed":{"@type":"Place","name":"Worldwide"}},
        {"@type":"Service","@id":url+"#service","name":short_name,
         "serviceType":d["service_type"],"url":url,
         "provider":{"@id":BASE+"/#org"},"areaServed":{"@type":"Place","name":"Worldwide"},
         "description":d["desc"],
         "audience":{"@type":"Audience","audienceType":"Founders, operations, technology and risk leaders"},
         "hasOfferCatalog":{"@type":"OfferCatalog","name":short_name+" services",
            "itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":s[0]}} for s in d["services"]]}},
        {"@type":"WebPage","@id":url+"#webpage","url":url,"name":d["title"],
         "isPartOf":{"@id":BASE+"/#website"},"about":{"@id":url+"#service"},
         "primaryImageOfPage":BASE+"/assets/og-image.png","inLanguage":"en"},
        {"@type":"BreadcrumbList","@id":url+"#breadcrumb","itemListElement":[
            {"@type":"ListItem","position":1,"name":"Home","item":BASE+"/"},
            {"@type":"ListItem","position":2,"name":crumb_name,"item":BASE+crumb_href},
            {"@type":"ListItem","position":3,"name":short_name,"item":url}]},
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

def render_timeline(d):
    if not d.get("timeline"): return ""
    steps = "\n".join(
        '                <div class="step"><span class="sn">%s</span><h3>%s</h3><p>%s</p><span class="deliver">%s</span></div>'
        % (esc(no), esc(name), esc(desc), esc(out)) for no,name,desc,out in d["timeline"])
    return '''    <section class="block">
        <div class="wrap">
            <div class="sec-head">
                <div>
                    <span class="eyebrow muted reveal">How the Sprint runs</span>
                    <h2 class="display reveal" data-d="1" style="margin-top:1.2rem">%s <span class="it accent-text">%s</span></h2>
                </div>
                <p class="sec-no reveal" data-d="2" style="max-width:34ch">%s</p>
            </div>
            <div class="steps reveal" data-d="1">
%s
            </div>
        </div>
    </section>

''' % (esc(d["timeline_h2"][0]), esc(d["timeline_h2"][1]), esc(d["timeline_note"]), steps)

def render_sample(d):
    if not d.get("sample"): return ""
    cards = "\n".join(
        '                <div class="why"><span class="n">%s</span><h3>%s</h3><p>%s<br/><b style="color:var(--accent);font-weight:500">%s</b></p></div>'
        % (esc("Candidate"), esc(name), esc(scores), esc(rec)) for name,scores,rec in d["sample"])
    return '''    <section class="block">
        <div class="wrap">
            <div class="sec-head">
                <div>
                    <span class="eyebrow muted reveal">Inside the Sprint</span>
                    <h2 class="display reveal" data-d="1" style="margin-top:1.2rem">%s <span class="it accent-text">%s</span></h2>
                </div>
                <p class="sec-no reveal" data-d="2" style="max-width:34ch">%s</p>
            </div>
            <div class="why-grid reveal" data-d="1">
%s
            </div>
        </div>
    </section>

''' % (esc(d["sample_h2"][0]), esc(d["sample_h2"][1]), esc(d["sample_note"]), cards)

def render_related(slug):
    cards = []
    for s in RELATED.get(slug, [x for x in ORDER if x != slug][:3]):
        name, blurb = SHORT[s]
        cards.append('''                <a class="rel-card magnetic" href="/services/%s/" data-cursor><span class="rel-n">↗</span><h3>%s</h3><p>%s</p></a>'''
                     % (s, esc(name), esc(blurb)))
    return "\n".join(cards)

def build(slug, d, base_path="services", short_name=None, crumb_name="Services", crumb_href="/#capabilities"):
    short_name = short_name or SHORT[slug][0]
    url = "%s/%s/%s/" % (BASE, base_path, slug)
    ind = "".join("<span>%s</span>" % esc(x) for x in d["industries"])
    contact_subject = "Enquiry%20—%20" + short_name.replace(" ","%20").replace("&","and")
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
      window.GA_MEASUREMENT_ID = "G-PSM4267LV3";
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
                <a href="/">Home</a> <span>/</span> <a href="{crumb_href}">{crumb_name}</a> <span>/</span> <b>{short}</b>
            </nav>
            <span class="eyebrow reveal" data-d="1" style="margin-top:1.4rem;display:inline-flex">{eyebrow}</span>
            <h1 class="display reveal" data-d="1">{h1a}<br/><span class="it accent-text">{h1b}</span></h1>
            <p class="svc-lead reveal" data-d="2">{lead}</p>
            <div class="hero-cta reveal" data-d="3" style="margin-top:2.2rem">
                <a href="{cta_href}" class="btn btn-solid magnetic" data-cursor data-event="cta_primary" data-label="{cta_label}">{cta_label} <span class="arrow">→</span></a>
                <a href="{cta2_href}" class="btn btn-ghost magnetic" data-cursor>{cta2_label}</a>
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

{timeline_section}    <section class="block" id="services">
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

{sample_section}    <section class="block method">
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
            <span class="eyebrow muted reveal">What you can expect</span>
            <p class="reveal" data-d="1" style="margin-top:1.5rem;max-width:26ch">{proof_hl}</p>
            <div class="hero-cta reveal" data-d="2" style="margin-top:2.4rem">
                <a href="/#work" class="btn btn-ghost magnetic" data-cursor>See example workflows <span class="arrow">→</span></a>
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
                <a href="/contact/" class="btn btn-solid magnetic" data-cursor data-event="cta_contact">Start a conversation <span class="arrow">→</span></a>
                <a href="mailto:machlilieslimited@gmail.com?subject={subject}" class="btn btn-ghost magnetic" data-cursor data-event="cta_email">Email us directly</a>
            </div>
        </div>
    </section>

{footer}

    <script src="/assets/js/site.js" defer></script>
</body>
</html>
'''.format(
        title=esc(d["title"]), desc=esc(d["desc"]), url=url, base=BASE,
        keywords=esc(d["keywords"]), jsonld=jsonld(d, url, short_name, crumb_name, crumb_href), nav=NAV,
        short=esc(short_name), crumb_name=esc(crumb_name), crumb_href=crumb_href, eyebrow=esc(d["eyebrow"]),
        h1a=esc(d["h1"][0]), h1b=esc(d["h1"][1]), lead=d["lead"],
        cta_label=esc(d["cta"]), cta_href=d["cta_href"],
        cta2_label=esc(d["cta2"]), cta2_href=d["cta2_href"],
        subject=contact_subject,
        ov_eyebrow=esc(d["ov_eyebrow"]), ov_hl=d["ov_hl"], ov_body=esc(d["ov_body"]),
        timeline_section=render_timeline(d), sample_section=render_sample(d),
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

CONTACT_FIELDS = [
    ("f-name","Name","text","",True,"name","half"),
    ("f-company","Company","text","",True,"organization","half"),
    ("f-role","Role","text","",False,"organization-title","half"),
    ("f-email","Email","email","",True,"email","half"),
    ("f-workflow","Which workflow do you want to automate?","text","e.g. renewal pack preparation, invoice exceptions, inbox triage",True,"","full"),
    ("f-systems","Which systems are involved?","text","CRM, email, documents, finance, ERP, support…",False,"","full"),
    ("f-effort","Current manual effort","text","e.g. ~20 hrs/week across 3 people",False,"","half"),
    ("f-risk","Risk or compliance concerns","text","e.g. client data, audit evidence, approvals",False,"","half"),
    ("f-ai","Current AI experiments (if any)","text","",False,"","full"),
]

def render_fields():
    rows = []
    for fid,label,typ,ph,req,ac,span in CONTACT_FIELDS:
        cls = "field full" if span == "full" else "field"
        reqmark = ' <span class="req">*</span>' if req else ""
        reqattr = " required" if req else ""
        phattr = ' placeholder="%s"' % esc(ph) if ph else ""
        acattr = ' autocomplete="%s"' % ac if ac else ""
        name = "email" if typ == "email" else label   # Formspree uses an "email" field for reply-to
        rows.append('''                <div class="%s">
                    <label for="%s">%s%s</label>
                    <input id="%s" name="%s" type="%s"%s%s%s />
                </div>''' % (cls, fid, esc(label), reqmark, fid, esc(name), typ, reqattr, acattr, phattr))
    return "\n".join(rows)

def build_contact():
    url = BASE + "/contact/"
    title = "Contact | Book an Agentic Operations Sprint — Mach Lilies"
    desc = "Start a conversation with Mach Lilies about an Agentic Operations Sprint. Tell us the workflow you want to automate, the systems involved and your risk concerns. We reply within one business day."
    graph = [
        {"@type":["Organization","ProfessionalService"],"@id":BASE+"/#org","name":"Mach Lilies",
         "url":BASE+"/","email":"machlilieslimited@gmail.com","slogan":"Mach speed. Lily craft.",
         "contactPoint":{"@type":"ContactPoint","email":"machlilieslimited@gmail.com","contactType":"sales","areaServed":"Worldwide","availableLanguage":"English"}},
        {"@type":"ContactPage","@id":url+"#webpage","url":url,"name":title,
         "isPartOf":{"@id":BASE+"/#website"},"about":{"@id":BASE+"/#org"},"inLanguage":"en"},
        {"@type":"BreadcrumbList","@id":url+"#breadcrumb","itemListElement":[
            {"@type":"ListItem","position":1,"name":"Home","item":BASE+"/"},
            {"@type":"ListItem","position":2,"name":"Contact","item":url}]},
    ]
    ld = json.dumps({"@context":"https://schema.org","@graph":graph}, indent=2, ensure_ascii=False)
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

    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="Mach Lilies" />
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
{ld}
    </script>

    <script>
      window.GA_MEASUREMENT_ID = "G-PSM4267LV3";
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
                <a href="/">Home</a> <span>/</span> <b>Contact</b>
            </nav>
            <span class="eyebrow reveal" data-d="1" style="margin-top:1.4rem;display:inline-flex">Start a conversation</span>
            <h1 class="display reveal" data-d="1">Book an Agentic<br/><span class="it accent-text">Operations Sprint.</span></h1>
            <p class="svc-lead reveal" data-d="2">Tell us the workflow you want to automate and we'll reply within one business day with an honest first view — no funnels, no bots. Most engagements begin with a fixed-scope Agentic Operations Sprint.</p>
        </div>
    </header>

    <section class="block" id="enquiry" style="padding-top:0">
        <div class="wrap">
            <form class="form-wrap" id="enquiry-form" action="mailto:machlilieslimited@gmail.com" method="post" enctype="text/plain" data-endpoint="{endpoint}">
                <input type="hidden" name="_subject" value="New Agentic Operations enquiry — machlilies.com" />
                <div class="form-grid">
{fields}
                    <div class="field half">
                        <label for="f-urgency">How urgent is this?</label>
                        <select id="f-urgency" name="Urgency">
                            <option>This quarter</option>
                            <option>Now</option>
                            <option>Exploratory</option>
                        </select>
                    </div>
                    <div class="field full">
                        <label for="f-outcome">Desired business outcome <span class="req">*</span></label>
                        <textarea id="f-outcome" name="Desired outcome" required placeholder="What would a good result look like in six months?"></textarea>
                    </div>
                </div>
                <div class="form-actions">
                    <button type="submit" class="btn btn-solid magnetic" data-cursor>Send enquiry <span class="arrow">→</span></button>
                    <a href="{booking}" class="btn btn-ghost magnetic" data-cursor data-event="cta_book">Or book a 30-min call</a>
                </div>
                <p class="form-note" style="margin-top:1rem">Prefer email? <a href="mailto:machlilieslimited@gmail.com" style="color:var(--accent);border-bottom:1px solid rgba(201,242,76,0.4)" data-event="cta_email">machlilieslimited@gmail.com</a> — we reply within one business day.</p>
                <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
            </form>
        </div>
    </section>

{footer}

    <script src="/assets/js/site.js" defer></script>
</body>
</html>
'''.format(title=esc(title), desc=esc(desc), url=url, base=BASE, ld=ld, nav=NAV,
           fields=render_fields(), footer=footer(), endpoint=FORM_ENDPOINT, booking=BOOKING_URL)

if __name__ == "__main__":
    print("== service pages ==")
    for slug in ORDER:
        path = os.path.join(ROOT, "services", slug, "index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w").write(build(slug, SERVICES[slug]))
        print("  wrote services/%s/index.html" % slug)
    print("== industry pages ==")
    for slug in INDUSTRY_ORDER:
        path = os.path.join(ROOT, "industries", slug, "index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w").write(build(slug, INDUSTRIES[slug], base_path="industries",
                                     short_name=IND_SHORT[slug], crumb_name="Industries", crumb_href="/#capabilities"))
        print("  wrote industries/%s/index.html" % slug)
    print("== contact ==")
    cpath = os.path.join(ROOT, "contact", "index.html")
    os.makedirs(os.path.dirname(cpath), exist_ok=True)
    open(cpath, "w").write(build_contact())
    print("  wrote contact/index.html")
    print("done.")
