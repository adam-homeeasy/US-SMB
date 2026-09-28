# PRD: Agency Master Agent — US SMB Growth Systems Tooling Pipeline

Written 2026-07-27. This is the build spec for the pipeline scoped in the capacity-planner note the same day (Heavy load tier — three net-new builds plus a net-new orchestration layer). Written so each stage can be built independently, in parallel, across different tools/sessions (Claude Code on Sonnet/Opus API, Codex, AI Arena, etc.) without needing shared context — every stage's contract is the account record schema in §2, not a conversation with another agent.

**Source material assumed as background:** `US_SMB_Digital_Growth_Business_Handover.md` (offer ladder, tool priority list, target metrics), `international-smb-growth-systems-plan.md` (why this stays US-core for now, international sequencing later), `master-sales-agent-skill.md` (Clearlane's own pipeline-tool precedent — same file-based, zero-shared-memory design pattern used here), and the Website Agent v3.1 build (`website-agent-v3.1-plan.md`, plus the actual v2-era codebase found at `Web Design/workspace-.../run-pipeline.py` — Python orchestrator + `.claude/agents/*.md` subagents + file-based handoff: `brief.md` → `research.md` → `copy.md`/`design-spec.md` → assembly → `animation-spec.md` → `seo-spec.md`).

---

## 0. Goal

Build the pipeline that takes a raw list of US SMB target accounts and, with minimal founder time per account, gets each one through: **discovered → diagnosed → pitched → contacted → (if sold) delivered.** The two metrics this whole system exists to move, per the handover doc, are **Revenue per Targeted Account (RPTA)** and **founder minutes per customer** — every design decision below should be checked against "does this reduce founder minutes without reducing conversion."

---

## 1. System architecture

```
Stage 1: List Building Tool
   │  (Google Places API + website-exists check)
   ▼
Stage 2: Diagnostic Engine
   │  (SEO audit + digital-presence audit — only where a website exists)
   ▼
Stage 3: Revenue Leak Calculator
   │  (diagnostic findings → $ impact → pitch draft)
   ▼
Stage 4: Outreach Sequence
   │  (email → follow-up → US-number call → text, per the handover doc's funnel)
   ▼
Stage 5: Website Build Agent V4
   │  (only for: no-website leads, or sold customers needing a build/refresh)
   ▼
   [sale closed / lost — logged either way]

Orchestrator: Agency Master Agent
   (drives every account through 1→4, and dispatches 5 whenever an account
   needs a website built, whether that's pre-sale downsell-bait or post-sale delivery)
```

Every stage reads and writes to one shared account record (§2) rather than passing context conversationally between agents — this is the same zero-shared-memory, file-based handoff pattern already proven in the Website Agent build and in Master Sales Agent, and it's what makes parallel building across different tools possible: whoever builds Stage 2 doesn't need to know how Stage 1 was implemented, only what fields it guarantees are populated.

---

## 2. The account record — the actual contract

One JSON record per targeted account, created by Stage 1 and enriched by every later stage. This is the single most important artifact in this PRD — get this schema agreed before any stage starts building, since it's what lets stages be built in parallel without coordination calls.

```json
{
  "account_id": "uuid",
  "source": "google_places",
  "vertical": "HVAC | plumbing | roofing | med_spa | dental | law_firm | other",
  "business_name": "string",
  "address": {"street": "", "city": "", "state": "", "zip": "", "country": "US"},
  "phone": "string | null",
  "google_place_id": "string",
  "website_url": "string | null",
  "has_website": "boolean",

  "diagnostic": {
    "run_at": "timestamp | null",
    "seo_audit": { "score": "0-100 | null", "findings": ["..."] },
    "digital_presence_audit": { "score": "0-100 | null", "findings": ["..."] },
    "skipped_reason": "no_website | null"
  },

  "revenue_leak": {
    "estimate_low_usd": "number | null",
    "estimate_high_usd": "number | null",
    "basis": ["missed_calls", "weak_follow_up", "low_form_conversion", "..."],
    "pitch_summary": "string | null"
  },

  "outreach": {
    "stage": "not_started | emailed | followed_up | called | texted | demo_booked | demo_completed | won | lost",
    "loss_reason": "string | null",
    "human_minutes_spent": "number"
  },

  "website_build": {
    "needed": "boolean",
    "reason": "no_website_downsell | sold_199_website | sold_999_system | refresh",
    "status": "not_started | in_progress | delivered",
    "build_time_minutes": "number | null"
  },

  "product": {
    "sold": ["website_199", "funnel_199", "automation_300", "system_999", "recurring_99"],
    "revenue_usd": "number"
  },

  "meta": {
    "currency": "USD",
    "timezone": "string",
    "created_at": "timestamp",
    "updated_at": "timestamp"
  }
}
```

`meta.currency`/`meta.timezone` are included now, even though this build is US-only, per the international-readiness principle already agreed for the SMB/TF shared capability layer — costs nothing to include today, expensive to retrofit later.

---

## 3. Stage 1 — List Building Tool — BUILT (2026-07-27)

**Purpose:** produce a list of qualified target accounts per vertical, each flagged with whether a website exists, without manual research.

**Resolved:** the "Restaurant Search Tool" is `FnB_Scout_Tool_v2.html` — a self-contained, client-side HTML tool (no backend) that Adam already had built and validated for Table Foundry F&B prospecting: Google Places (New) Text Search across term × area combinations, in-browser triage scoring (credibility/presence/relevance → pull/consider/skip), chain/closed/catering flagging, in-browser review-sentiment mining, and CSV export. It was not in the synced Consulting OS folder — Adam supplied it directly.

**Built: `SMB_Scout_Tool.html`**, forked from it rather than built fresh from scratch, since the existing tool was already proven. Changes made:
- **`has_website` is now a first-class signal**, not just a badge: a prominent "NO WEBSITE — downsell lead" flag, a dedicated "No website only" filter, and its own count in the results summary — this is the single most important field this stage produces for the rest of the pipeline.
- **New export: "SMB account records (JSON)"** — writes the exact account record array from §2 below, ready to hand straight to Stage 2 with no reshaping. The original tool's two exports (benchmark CSV, TF/F&B client-config CSV) are kept as-is, so the same tool still serves Table Foundry prospecting.
- **Analysis mode toggle (General SMB / F&B)** — swaps the review-mining keyword library (food/service/ambience themes → responsiveness/quality-of-work/professionalism/reliability themes for local-service verticals) and turns the F&B-only catering auto-flag on/off. Same engine serves both businesses now.
- **Currency selector** ($/₹/£/A$/C$) for price-band display — small addition now, matches the international-readiness principle already agreed for TF/SMB (§2 of the combined capital-allocation plan), costs nothing to include today.
- **Vertical tag field** — labels every exported SMB record (hvac, plumbing, dental, etc.); doesn't affect the search itself.

**Mechanism (unchanged from the original tool, this is what already worked):** one Text Search (New) call per term × area combination, with a field mask that pulls `websiteUri`, phone, rating, review count, reviews, and photos directly — **no separate Place Details call needed**, unlike the from-scratch design originally sketched in this PRD (see correction below). Runs client-side in the browser with a user-pasted API key stored in `localStorage`; no server, no deploy.

**Cost correction (verified 2026-07-27 against developers.google.com/maps/billing-and-pricing/pricing — the original draft of this PRD had this wrong):** `websiteUri`, `nationalPhoneNumber`, `rating`, and `userRatingCount` all require the **Enterprise** field-mask tier for Place Details, not Pro. Since this tool requests everything in one Text Search call rather than a separate Place Details call, the relevant SKU is **Text Search Enterprise** pricing for any query that includes those fields — the original "$32/1,000 Place Details Pro" framing doesn't apply to this tool's actual mechanism. Get a live quote from Google's pricing calculator before running at real volume; don't carry forward the Pro-tier assumption.

**A leftover Python/API-wrapper script (`list_building_tool.py`) was drafted before this tool surfaced** — superseded as the primary Stage 1 deliverable, but kept on hand as a possible future headless/batch variant (e.g. for a scheduled re-run) if the browser tool's manual per-session workflow ever becomes the bottleneck.

**Deterministic-code:** entirely — no AI call anywhere in this stage, matching the original assessment.

**Output:** a batch of account records (§2) via the new JSON export, `diagnostic`, `revenue_leak`, `outreach`, `website_build`, `product` all null/unset.

---

## 4. Stage 2 — Research & Analysis Agent + SEO Agent (revised 2026-07-27, supersedes the original "Diagnostic Engine" framing below)

**Purpose:** replaces the original single "Diagnostic Engine" idea with two cooperating agents — a **Research & Analysis Agent** (competitive/design/funnel research) and a **SEO Agent** (wraps the existing `seo-tool`/`site-audit` skills for comparative SEO benchmarking). Confirmed design, ready to build.

### Research & Analysis Agent — four research passes per account

1. **Segment research** — general context on the account's vertical.
2. **Local competition** — who this specific account actually competes with in its own city/area, and how they're doing digitally.
3. **National competition, same vertical** — not a threat scan, a best-practices scan: how the best national players in this vertical handle copy, design, UI/UX, and business model. Studied to borrow from, not to worry about.
4. **Industry-agnostic design mining** — separate and broader than #3: search *any* industry for standout site architecture, UI/UX patterns, motion/animation, and copy concepts worth adapting — not limited to the vertical, since the best interaction pattern might come from an unrelated industry entirely.

Plus a fifth pass, **funnel/lead-capture assessment**: does the account have an identifiable lead magnet/funnel, how are leads likely captured today, benchmarked against both local and national competitors' funnels.

**Critical build requirement — caching, not re-running, per account:** passes #3 (national/same-vertical) and #4 (industry-agnostic) do not vary by account — they vary by vertical. Run each once per vertical, cache the result, and reuse it across every account in that vertical. Passes #2 (local competition), #5 (funnel), and the account's own SEO comparison (below) are genuinely per-account and should run fresh each time. Skipping this caching split would mean re-running the same national/industry research on every one of ~150 accounts/vertical/month — exactly the kind of cost/latency blowup that would break the $199/$999 unit economics this whole business depends on (see the handover doc's "founder minutes and cost per customer must approach zero" principle).

### SEO Agent — wraps the existing skills, adds comparative benchmarking

Reuses `seo-tool` and `site-audit` (already built, skill files available) rather than reimplementing SEO scoring. Adds one thing those skills don't do on their own: runs the audit at **three levels** — national industry benchmark, local competitor set, and the account's own site if one exists — and produces a **traffic/performance gap**, not just a standalone score.

**No-website accounts are not skipped.** If there's no site to audit, the gap is modeled as the full benchmark traffic being lost entirely (zero vs. benchmark), so every account gets a real number, not a blank `skipped_reason`.

### Data flow out of Stage 2

- SEO Agent's traffic gap → Revenue Leak Calculator (Stage 3).
- Research & Analysis Agent's funnel gap → **also** Revenue Leak Calculator (Stage 3) — two separate gap inputs feeding one dollar figure, not one.
- Research & Analysis Agent's copy/UI-UX/motion/strategy findings → Website Build Agent V4 ("Claude Design" hand-off, Stage 5).
- SEO Agent's findings → **also** Website Build Agent V4, separately, so the new build has real SEO requirements from day one.
- The funnel assessment is not a one-time pre-sale input — it persists and becomes the automatic CTA source for **post-sale** upsell (funnel-optimization/growth-engine products), so it keeps earning its keep after the account converts.

**Judgment vs. capacity-agnostic:** the four research passes are judgment-heavy by nature (that's the point — differentiated findings, not a templated score) and should run on a strong model (Fable 5 for building the agents; Sonnet as the default runtime model once built, per the 2026-07-27 model-choice discussion — Fable's premium cost and 30-day retention requirement aren't worth it for routine per-account runs once the architecture is already baked in). The SEO Agent's gap-calculation math itself is a deterministic-code candidate once the skill has run — no model call needed for the subtraction.

**Output:** `diagnostic.seo_audit` (now: score + gap vs. national/local benchmark), a new `diagnostic.competitive_research` block (segment/local/national/industry-agnostic findings + funnel assessment, cached appropriately per §4 above), `diagnostic.skipped_reason` no longer used for no-website accounts (they get a modeled full-loss gap instead of being skipped).

---

### Superseded — original "Diagnostic Engine" framing (kept for reference only)

The original plan was a single Diagnostic Engine doing an SEO audit and a vaguely-scoped "digital-presence audit," with no-website accounts simply skipped and flagged `skipped_reason: "no_website"`. Superseded by the richer, two-agent design above, which also resolves the original open question about whether a "digital-presence audit" skill exists — it doesn't need to, since the SEO Agent's benchmark comparison and the Research & Analysis Agent's competitive/funnel research together cover what that placeholder was gesturing at, more precisely than the original vague framing did.

---

## 5. Stage 3 — Revenue Leak Calculator

**Purpose:** the handover doc's own Priority 1 tool. Converts diagnostic findings into a dollar range and a pitch, per the doc's own required output shape: **Problem → estimated impact → recommended fix → relevant product/module.**

**Inputs (from the account record):** `diagnostic.seo_audit.findings`, `diagnostic.digital_presence_audit.findings`, plus assumptions that need to be set once and then run deterministically: estimated lead volume by vertical, typical missed-call rate, typical form conversion, response-delay impact, appointment rate, close rate, customer value by vertical. The handover doc lists these same inputs (§7, Priority 1) — this build should use industry-typical defaults per vertical rather than asking the lead for their real numbers (nothing is being collected from the prospect at this stage — this runs pre-outreach).

**Judgment vs. capacity-agnostic:** **judgment-critical the first time** — setting the actual formula and the per-vertical default assumptions (missed-call rate for HVAC vs. dental, e.g.) is a real business decision, not something to leave to an LLM's guess. Once that formula is set and reviewed once, this becomes a **deterministic-code candidate** — a calculator should not be re-deriving its logic via a live AI call on every account; it should be a fixed formula the account record's findings get plugged into.

**Output:** `revenue_leak.estimate_low_usd`, `estimate_high_usd`, `basis`, and a `pitch_summary` string suitable for dropping into an outreach email or into `client-proposal`-style pitch material.

---

## 6. Stage 4 — Outreach Sequence

**Purpose:** run the handover doc's outreach funnel (personalized email → follow-up email → US-number call → compliant text → audit walkthrough) against each diagnosed account, and decide the tooling for it.

**This stage is explicitly a decision task before it's a build task.** Research the marketplace (email infrastructure, calling/texting, CRM) against a build-vs-buy cost comparison, the same way `master-sales-agent-skill.md` already did for Clearlane's own pipeline — that doc's finding (enterprise CRM connectors don't fit a $0-cost stack, so most of it ended up custom-built on a plain spreadsheet + scheduled tasks) is a real precedent worth checking against before assuming SMB outreach needs different tooling.

**Deliverable for this stage, before any code:** a short build-vs-buy note — one row per candidate (email sending infra, calling/SMS provider, CRM/tracker) with cost at the 300-accounts/month volume, and a recommendation, following the same shape as the capacity-planner's own output style (scannable, not an essay).

**Judgment vs. capacity-agnostic:** the message drafting (personalized email/follow-up copy) is capacity-agnostic once the Revenue Leak Calculator's pitch_summary exists to draft from — this is exactly the kind of drafting `master-sales-agent-skill.md` already does (agent drafts, human reviews and sends, nothing auto-sent). **Keep that same guardrail here: no message is auto-sent** until this is proven out.

**Output:** `outreach.stage` progressed per account, `outreach.human_minutes_spent` logged (this is the other headline metric from the handover doc — track it from day one, not after the fact).

---

## 7. Stage 5 — Website Build Agent V4 (revised 2026-07-27 — simpler model, superseding the v3.1-trim approach below)

**Purpose:** actually build the $199 website product — either as the no-website downsell offer, or as fulfillment once an account buys. Timed, so the actual founder-minutes-per-build number is known rather than assumed.

**Direction changed after Track A shipped.** The original plan (further down this section) was to trim v3.1's 10-agent gated pipeline down to fewer stages. Adam's explicit instruction instead: **don't extend v3.1 at all — use a simpler, more linear model**, the one that actually worked well for the Table Foundry website, rather than the iterative multi-gate process that "complicated the result with limited visible improvement." That's a stronger signal than anything in the trim-table below: v3.1's complexity was tried and didn't pay for itself even on a bespoke build, so a productized $199 site shouldn't inherit any of it.

**The model that worked (Table Foundry precedent), as the actual V4 pipeline:**

1. **Strategy** — lays down the core message: who this is for, what to convey, the positioning. Reads the account record (§2) — vertical, business name, diagnostic findings where available — same auto-generated-brief idea as before, just without a separate Brief Architect / ICP Gate 0 / Synthesis Gate round.
2. **Architecture** — page structure and information hierarchy, decided directly off Strategy's output, not a separate gated round.
3. **UI/UX decisions** — attractive, clear visual direction and layout, decided directly from Strategy + Architecture. No bespoke per-site design-spec negotiation loop.
4. **Copy** — sharp, on-brand copy that conveys exactly what Strategy laid down. Two explicit quality bars, not one: **factual correctness** (a real audit pass — nothing fabricated, nothing overclaimed) and **doesn't read like AI** (the existing humanizer discipline — bans "elevate/empower/leverage," varies sentence length, active voice).
5. **Hand off to Claude Design** — Strategy + Architecture + UI/UX + Copy all feed into the actual build/assembly step. (Flag: confirm what "Claude Design" refers to concretely in this stack — treating it here as the build/assembly stage that turns the specs into the live page, analogous to the existing `run-pipeline.py` compiler, but worth Adam confirming the exact tool/handoff mechanism before this is built.)
6. **Illustrations, as a distinct side-workflow, not folded into step 5:**
   a. Write a clear, specific description of exactly what the illustration needs to convey.
   b. Generate a first-pass reference image from that description in ChatGPT's image tool.
   c. Bring that reference image back into Claude, and give Claude Design a prompt to **recreate it** matching the site's actual UI/UX and color scheme — the ChatGPT image is a visual reference for content/composition, not the final asset; Claude Design produces the on-brand version.

**What this explicitly drops versus the earlier trim-table below:** the separate ICP Gate 0, Synthesis Gate 1.5, and any bidirectional Copy ↔ UI/UX revision loop. Those were the specific pieces of v3.1 that added process without proportional visible improvement — not being carried into V4 even in a lighter form.

**What still needs deciding before this is built:** how many human checkpoints sit between Strategy and final delivery (the Table Foundry precedent presumably had at least one taste/approval pass — worth confirming whether that's one gate at the end, or a check after Strategy before Copy/Design spend effort on the wrong direction), and what template/component reuse looks like across accounts of the same vertical so this doesn't become a fully bespoke build per $199 site despite the simpler process.

---

### Superseded — original v3.1-trim plan (kept for reference, not the build direction anymore)

The original plan was to trim v3.1's 10-agent gated architecture (ICP Gate 0, Synthesis Gate 1.5, bidirectional Copy/UI-UX revision, three human approval gates) down to fewer stages, reusing the existing `run-pipeline.py` compiler for assembly and fixed per-vertical templates instead of bespoke design-spec generation per site. Superseded because Adam's direction is to use the simpler Strategy → Architecture → UI/UX → Copy → Design model above instead, which is what actually worked for Table Foundry — not a lighter version of the process that "complicated the result with limited visible improvement." The one piece worth carrying forward regardless: the existing lexical-parser-based compiler (`parse_copy_file`/`parse_design_file`/`compile_site_html`) is still a plausible deterministic-code candidate for whatever step 5 ("Claude Design") turns out to be.

**Success criterion, unchanged:** V4 exists, has been run end-to-end at least once against a real or realistic account record, and the actual wall-clock build time is logged — that number is what makes the $199 unit economics real instead of assumed.

**Output:** `website_build.status`, `website_build.build_time_minutes` populated; the live site itself delivered.

---

## 8. Stage 6 — Agency Master Agent (orchestrator)

**Purpose:** drive every account record through Stages 1→4 in order, and dispatch Stage 5 whenever `website_build.needed` becomes true (either pre-sale, as the no-website downsell bait, or post-sale, as fulfillment).

**Built last, on purpose** — it depends on Stages 1-5 existing in some working form; building the orchestrator before the pieces it orchestrates risks locking in a workflow shape that has to be redone once the real interfaces (especially Stage 2's digital-presence-audit gap, and Stage 5's actual V4 shape) are known.

**What it actually is:** a controller that, per account record —
1. Confirms Stage 1 output is present (`has_website` known).
2. If `has_website: true` → dispatch Stage 2 → Stage 3 → queue for Stage 4.
   If `has_website: false` → set `website_build.needed: true, reason: "no_website_downsell"`, skip straight to a lighter version of Stage 3/4 built around "you don't have a website at all" as the pitch, and queue Stage 5.
3. Tracks `outreach.stage` transitions and stops advancing an account once it's `won` or `lost`.
4. On a win that includes a website product (`website_199` or `system_999`), sets `website_build.needed: true, reason: "sold_..."` and dispatches Stage 5.
5. Surfaces the four handover-doc summary metrics (account→engagement, account→demo, demo→paid, RPTA) plus human-minutes-per-customer, computed directly from the account record set — no separate reporting build needed if the schema in §2 is populated correctly throughout.

**Judgment vs. capacity-agnostic:** the orchestration logic itself (the if/else routing above) is deterministic — this should be code, with each Stage invoked as a function/subagent call, not an LLM deciding routing logic per account. The one place judgment matters is deciding *when* to advance an account past a stalled outreach stage or mark it lost — that's a rule to define once (e.g. "no response after N follow-ups → lost"), not a per-account judgment call.

**Deterministic-code candidate:** the routing/orchestration layer, yes. The metrics rollup (step 5), yes — it's arithmetic over the account record set, not analysis.

---

## 9. Build sequencing (parallelizable across tools/sessions)

Given multiple terminals/tools available (Claude Code Sonnet/Opus API, Codex, AI Arena), these can genuinely run in parallel once §2's schema is locked, since each stage's contract is "read these fields, write these fields" rather than a live conversation with another stage:

- **Track A (fully independent, start immediately):** Stage 1 (List Building) — pure API wrapper, no dependency on anything else.
- **Track B (independent, start immediately):** Stage 5 (Website Build Agent V4) — the heaviest single build; only needs a realistic mock account record to build/test against, doesn't need Stage 1-4 to actually exist yet.
- **Track C (fully scoped, start immediately):** Stage 2 — both the SEO Agent (wraps existing skill machinery) and the Research & Analysis Agent (the five research passes, with the per-vertical caching split from §4) are now fully specified; no remaining blocker.
- **Track D (depends on Track C's output shape, but the formula work can start now):** Stage 3 — the per-vertical assumption-setting work (judgment-critical part) can be scoped and decided independently of Stage 2 finishing; wiring it to real diagnostic findings is the only part that waits.
- **Track E (mostly a research task, can run in parallel with everything):** Stage 4's build-vs-buy note.
- **Last, and genuinely blocked on the others:** Stage 6 (Agency Master Agent) — don't start this until at least a first working version of Stages 1, 2 (or a stub), 3, and 5 exist, per the reasoning in §8.

---

## 10. Open questions / assumptions flagged

- **"Claude Design"** (Stage 5, §7) — used here as the name of the build/assembly step Strategy/Architecture/UI-UX/Copy hand off to for the Table Foundry-style pipeline. Confirm what this concretely refers to in the actual toolchain before Stage 5 is built.
- **Human checkpoint count in the simplified V4 pipeline** (§7) — not yet decided; needs at least one confirmed checkpoint (likely after Strategy, possibly one final approval) before build.
- **Revenue Leak Calculator's per-vertical assumptions** (missed-call rate, close rate, etc. by vertical) — not yet set; this is a real business-judgment input, not something to default silently.
- **Outreach tooling build-vs-buy** — genuinely undecided; Stage 4's actual deliverable before any code is the comparison note itself.
- **V4's template set** — "a small fixed set of pre-built, per-vertical templates" is proposed in §7 but the templates themselves don't exist yet; first V4 build will likely need to produce 1-2 vertical templates as part of standing the agent up, not just the orchestration logic around them.
- **"No response after N follow-ups → lost" threshold** (§8) — not yet set; needs a number before the orchestrator's stall-detection logic can be finalized.
