> Note for the session: this message contains all five files in full, one after another. Where the prompt points to `context/ghl-spine/0X-...md`, use the matching section further down this message instead.

# Master prompt: GHL as the spine, three business lines

Paste everything below the line into the cloud session as the first message. The four context files (01 to 04) sit next to this one. Commit this whole folder into the repo under `/context/ghl-spine/` (about 32 KB, no other folders needed), or paste `99-ALL-IN-ONE-PASTE.md` instead, which has everything in one message.

---

## Who I am and what this session is

I'm Adam. I run three business lines under MSM Global Consulting Pvt Ltd (an Indian company, team in Bhubaneswar, selling mostly into the US):

1. **Leasify**: residential leasing conversion ops (US, Chicago and Texas metros).
2. **RevLabs US SMB**: productized websites, SEO, CRM and follow-up automation for US local service businesses.
3. **Table Foundry International (TF Direct)**: direct-ordering platform for independent US restaurants, NYC first.

Full context for each line is in:

- `context/ghl-spine/01-CONTEXT-LEASIFY.md`
- `context/ghl-spine/02-CONTEXT-REVLABS-US-SMB.md`
- `context/ghl-spine/03-CONTEXT-TF-INTERNATIONAL.md`
- `context/ghl-spine/04-GHL-TEARDOWN-PROTOCOL.md`

Read all four before doing anything. Treat what they call "locked" as locked. Don't re-debate it.

**The question:** should GoHighLevel (GHL) be the shared operating spine (CRM, pipelines, conversations, calendars, workflows, phone/SMS/email, sites/funnels, payments, reputation, AI agents) across all three lines, and should we white-label it and resell it as our own product? I want a full teardown of GHL judged on three things only: **cost, usability for our team and our clients, and how well its workflows match what each line actually needs to do.** Not a generic GHL review.

## How to run it: multi-agent, one master strategist on top

Use a master strategist that orchestrates five sub-agents. Each line agent works only on its own line and reports back in the fixed format below. The master is the only one who compares lines and makes the final call.

| Agent | Job | Uses the browser? |
|---|---|---|
| **Master strategist** | Plans the run, briefs the agents, merges findings, red-teams them, writes the verdict | No |
| **GHL teardown agent** | Builds the shared fact base on GHL: plans, real prices, usage costs, features, limits, white-label mechanics, API. Follows `04-GHL-TEARDOWN-PROTOCOL.md` | **Yes, the only one** |
| **Leasify agent** | Maps Leasify's workflows onto GHL, finds the gaps, costs it | No, asks the teardown agent to check things |
| **RevLabs agent** | Same for RevLabs US SMB | No, same |
| **TF agent** | Same for TF International | No, same |
| **Red-team agent** | After the line reports land, attacks them: lock-in, compliance, hidden costs, "what breaks at 100 clients" | No |

Rules for the agents:

- Only the teardown agent drives the browser, so there's one clean session in GHL. Line agents send it specific questions ("can a workflow trigger on a custom object field change?", "what does LC Phone charge per outbound SMS segment?") and it answers from the live account or the official docs, with a screenshot or link as proof.
- Every fact about GHL gets a source tag: `[live-account]`, `[ghl-docs]`, `[ghl-pricing-page]`, `[marketplace]`, `[community/reddit]` (weakest, say so), or `[assumption]`. Prices must carry the date checked. Nothing from memory gets passed off as current.
- Line agents don't invent numbers about our business. If a number isn't in the context file, they mark it `[assumption]` and give the range they used.
- Run the line agents in parallel once the teardown agent has the first fact base (plans, pricing, feature list). Don't wait for the full teardown to finish before starting them.

## The steps

1. **Plan gate (the only stop before the work).** Show me a one-screen plan: agents, what each produces, which model each uses, rough time. If you have a model-selector or routing skill, run it and show the routing card. Then wait for me to say **"go"**. After "go", don't stop to ask permission again. Run through to the end.
2. **Browser gate.** When the teardown agent is ready for the live account, tell me. I'll log in to GHL myself in the browser. You never type my password, never touch 2FA, never save credentials. Wait until I say "logged in". While waiting, work from the public pricing page, docs and marketplace.
3. **Teardown** (per protocol 04).
4. **Line fit analysis**, one per line, in the format below.
5. **Cost model** across all three lines at 1, 10, 25, 50 and 100 paying clients each, per GHL plan option.
6. **Red team.**
7. **Master verdict.**

## What each line agent must produce

One markdown file per line, same headings so the master can compare:

1. **What this line needs the spine to do**: the 10 to 20 core workflows, written as plain steps (trigger, action, owner, outcome). Take them from the context file, don't make up new ones.
2. **Workflow fit table**: each workflow, one row. Columns: GHL feature that covers it, fit (Native / Native with workaround / Needs integration / Not possible), how it would be built, effort in hours, monthly cost it drives, risk.
3. **What GHL replaces** in our current or planned stack, and what it can't replace.
4. **What we'd still have to build or buy** around it (integrations, middleware like Zapier/Make/n8n, custom code, our own database).
5. **Cost per client per month** at 1, 10, 50, 100 clients, broken into: GHL plan share, usage (phone, SMS, email, AI), add-ons, integrations, our labour. Compare it to what the line charges.
6. **Usability**: for our team (who builds, who operates daily, learning curve) and for the end client (would a busy owner actually log in and use this, or does it need to be fully done-for-them?).
7. **White-label angle**: does reselling GHL as our own branded product make sense for this line's buyer, at this line's price? If yes, at what price and packaging.
8. **Verdict for this line**: one of *Use GHL as the spine* / *Use GHL for part (say which part)* / *Don't use GHL*. With the three biggest reasons and the one thing that would change the call.

## What the master strategist must produce

- **`00-VERDICT.md`**, one page, bullets: the recommendation for each line, for the shared spine, and for white-label. Decided, not a menu of options. Include the plan tier to buy and when to upgrade.
- **`01-GHL-TEARDOWN.md`**: the shared fact base (feature by feature, cost by cost, limits, lock-in, API), all source-tagged.
- **`02-LEASIFY-FIT.md`**, **`03-REVLABS-FIT.md`**, **`04-TF-FIT.md`**: the line reports.
- **`05-COST-MODEL.md`** plus `05-cost-model.csv`: all three lines on one sheet, per plan option, 1 to 100 clients each, with every assumption listed.
- **`06-WHITE-LABEL-PLAN.md`**: brand structure (one agency account with sub-accounts per line, or separate agency accounts per brand), domains, desktop and mobile app branding, how rebilling works, what we charge, what the client sees and doesn't see, and how we leave GHL later if we need to.
- **`07-RISKS-AND-RED-TEAM.md`**: every risk with likelihood, impact, and the mitigation.
- **`08-SETUP-PLAN-30-60-90.md`**: if the verdict is yes to any part, the build order: which snapshot/sub-account first, which workflows first, what gets tested on a real client first.

Write all outputs to `/analysis/ghl-spine/` in the repo. Markdown only, no .docx.

## Things the analysis must answer directly (don't skip these)

- Can **one GHL agency account** carry all three brands cleanly, or does white-labelling three different brands force three agency accounts? What does that do to cost?
- **SaaS mode and rebilling**: can MSM Global (an Indian company) actually run GHL SaaS mode and rebill US clients? SaaS mode rebilling runs through Stripe connected to the agency. Check whether an Indian entity can get the Stripe account this needs, or whether we need a US entity/partner. This could decide the white-label question on its own.
- **A2P 10DLC and phone compliance** for US SMS through LC Phone or Twilio: who registers (us or each client), time to approve, cost, and how it fits our locked rules (RevLabs: no autodialer, no call recording, Texas email-only, text only after a spoken request; TF: email-first, no cold texts).
- **Data ownership and exit**: can we export contacts, conversations, pipelines, custom objects and workflows? What's the pain of leaving at 50 clients?
- **GHL sites vs our own builds**: does a GHL-hosted site pass RevLabs' SEO gate (title, description, canonical, sitemap, schema, llms.txt, speed)? Build one test page in the sandbox and check it. This decides whether Track B sites get built in GHL.
- **Custom objects and API v2**: good enough for Leasify's property/unit/lead model and TF's restaurant/guest data, or does the real data have to live in our own Postgres/Supabase with GHL as the engagement layer only?
- **AI features** (Conversation AI, Voice AI, AI Employee, workflow AI steps): what they cost per sub-account, what they actually do in the live account, and whether they could replace or host Leasify's "Amy Scott" AI agent.
- **Where GHL is clearly the wrong tool** for each line. Say it plainly.

## How to write

- Plain, simple words. Short bullets. Say what a thing is the first time you name it; don't assume I know GHL's internal terms.
- **No em-dashes anywhere.** Use commas, full stops or colons.
- Sentence-case headings. No "in summary" wrap-ups, no hedge-and-announce phrasing, no filler.
- When it comes to prices and packaging, **pick the option most likely to convert and say why**. Don't hand me a list of open decisions.
- Don't restate the context files back to me. Use them.
- Keep the first version lean. We're early: we need paying clients in the next 180 days, not a perfect platform. If GHL is overkill for a line right now, say that.

## Safety rules for the live GHL account

In `04-GHL-TEARDOWN-PROTOCOL.md`. Short version: sandbox sub-account only, no messages to real contacts, no buying numbers or add-ons, no billing or plan changes, no deleting anything that already exists. Ask me before anything that costs money.


---

# Context: Leasify

Condensed from `Leasify 2.0` (MASTER_HANDOVER.md, HANDOVER.md, the June strategic handover, Dual_User_Journey_Analysis.md; Aug 2026). **The "Uber model" is out of scope for this analysis**: no field-runner network, no runner dispatch app, no per-tour runner pay, no brokerage-margin model. Ignore any runner/dispatch material if you come across it.

## What Leasify is (locked)

- A **conversion operations** company for residential leasing. It runs the process between a qualified lead and a closed outcome: a tour, an application, a signed lease, a move-in.
- It does **not** generate leads, run ads, supply VAs, run a call centre, implement CRMs for clients, or replace the client's leasing team. It adds capacity.
- Problem it solves: landlords and locators get leads, they're too busy to follow up properly, leads go cold, revenue is lost. Not a demand problem, a follow-up problem.
- Pillars: lead to conversion, revenue recovery, dead-lead reactivation, pipeline progression.
- One brand only (Leasify). RevFoundry is shelved. Indian real estate developers were removed from scope on 19 Aug 2026.
- Markets: Chicago / Illinois and Texas metros (Dallas-Fort Worth, Houston, Austin, San Antonio).
- Leasify's methods came out of HomeEasy, a Chicago apartment-locating business Adam runs. HomeEasy is the live test bed.

## Who buys it and what they pay (locked)

| Client type | Monthly retainer |
|---|---|
| Apartment locators | $499 |
| Small property managers (80 to 500 units) | $499 |
| Student housing | $499 |
| Senior living | $499 |
| Corporate housing | $499 |
| Regional property managers (500 to 2,000 units) | $999 |
| Mortgage | $499 to $999 |
| Enterprise multifamily | Commission only |

- Plus a performance commission on every tier. **Commission rates are still not set.** Never quoted in outreach, only on the discovery call.
- Outreach order: locators, small PMs, student housing, regional PMs, senior living, corporate housing, mortgage, enterprise.
- Price path per client: months 1 to 3 at $499 to $999; months 3 to 6 at $1,500 to $3,500; month 6 onwards $3,500 to $10,000 once embedded across properties.
- Pilot: first 2 weeks free as an "implementation and calibration period". Billing starts at go-live. Month to month after, 30 days' notice.
- Guarantee covers response-time SLAs, follow-up frequency, coverage hours and reporting cadence. It does **not** guarantee leases, occupancy or revenue. Miss the SLA, next month free.
- Rule: don't raise the entry price before the first client signs. One brand, one go-to-market.

## What Leasify does every day (the workflows GHL would have to carry)

For each client, and for HomeEasy itself:

1. **Lead intake from many places**: listing sites (Zillow, Apartments.com and similar), web forms, phone, text, email, chat. Today leads are scattered across 5+ systems.
2. **Instant first response**: target under 5 minutes, ideally under 60 seconds, 24/7. Today this is done by an AI agent called **"Amy Scott"** that chats with renters and pulls out budget, move-in date, credit, voucher status and what they need. (Which platform Amy Scott runs on is not stated in the files: find out or mark as unknown.)
3. **Qualification tiers**: All leads, then Responders, then Non-Negative, then Hot (budget, move date and credit all stated).
4. **Lift Score**: every lead a human progresses must score at least 1.2 on a 5-variable score (deal type, timeline urgency, response latency, call outcome, and one more in the tracker). Calculated today in an Excel tracker.
5. **Matching renters to units**: using an inventory of 111 properties / 215 units across 15 Chicago neighbourhood clusters, merged from Atlas inventory and WPD Management's AppFolio vacancy feed. Each unit carries crime, transit, reviews, pet policy, laundry, elevator and voucher data.
6. **Housing voucher checks**: compare the renter's voucher against CHA payment standards and Mobility Zone caps.
7. **Price floors by area**: e.g. Chicago premium areas $1,500 per bed minimum; South Side floors $1,200 (1BR), $1,400 (2BR), $1,600 (3BR). Texas floors not set yet.
8. **Tour booking**: book first, staff within 24 hours in Chicago; warm hand-off in Texas. Reminders at 24h, 2h and 15 min. Target no-show rate under 20% (today about 35%).
9. **Application chasing**: documents, income checks, follow-ups until approval.
10. **Dead-lead reactivation**: sequences to leads 7, 14, 30, 90+ days old. Target: 10% of 90-day-old leads reactivated. This is the highest-value upsell.
11. **Founder daily report**: deal-by-deal, every day, with owner, committed action and due time for each deal.
12. **Weekly performance report to each client**.
13. **Alerts**: a Python script (`lead_pulse_monitor.py`) polls leads, scores urgency, geocodes the address, and sends Slack/email alerts with de-duplication.
14. **Commission tracking and collection** from landlords after a lease is signed.
15. **Renewal reminders**: ping past renters about 60 days before their lease ends.

## What already exists (tech)

- Python scripts: alert engine, address lookup, Chicago submarket analysis, Texas metro analysis, lead geo-classification.
- Neighbourhood Intel: a renter match tool (HTML/PDF) and a JSON database of the 111 properties.
- Excel daily report tracker with the Lift Score.
- **Decision 19 Aug 2026: build a fresh Postgres database** for leads, tours and daily reporting. No existing database to pull from. This analysis has to say whether GHL becomes the system of record, or Postgres stays the system of record and GHL sits on top for messaging and pipelines.
- Property systems at clients: AppFolio, Yardi, RealPage, Entrata. GHL has no native link to these as far as we know: verify.

## Open questions this analysis should settle

- Does Leasify run all client work inside **one** GHL sub-account (Leasify's own), or does each client get their **own** sub-account? Which fits "we don't implement CRMs for clients"?
- Can GHL custom objects hold properties, units and voucher rules well enough to do matching, or does matching stay in Python/Postgres and push results into GHL?
- Can GHL's AI (Conversation AI / Voice AI / AI Employee) do Amy Scott's job, at what cost per client?
- The June docs say "AI can't qualify or close, humans do". The August docs lean into AI triage. The fit analysis should say where the human stays in the loop inside GHL.
- Is a white-labelled "Leasify platform" something PMs would pay for on top of the service, or is Leasify a done-for-you service where the tool stays invisible?


---

# Context: RevLabs US SMB

Condensed from `RevLabs US SMB` (00-Consolidation-Handover, US_SMB_Digital_Growth_Business_Handover, Track B offer and change log, go-live checklist, GTM plan to 5 Oct, compliance handovers, Track A and Track C playbooks; Sep 2026).

## What it is

- Productized digital growth systems for US local service businesses, delivered cheaply from India using internal tools, Claude and reusable templates.
- Positioning: "we find where your sales system is losing leads, then build the website, funnel, CRM and automation to fix it." Not "cheap websites", not "an AI agency".
- Founder-led sales from India, calling US hours (7:30 pm to 12:30 am IST, Mon to Fri). Two founders.
- Target verticals: auto repair, car detailing, hair/beauty, HVAC, plumbing, roofing, dental, med spa, lawyers, landscaping, handyman, pet spa, vets, realtors, mortgage brokers. Plan: 2 verticals x 150 accounts = 300 targeted businesses a month.
- **GHL is already the settled outreach/CRM tool** (decided 31 Aug 2026): email sending, calling/SMS, CRM and pipeline. What's still open is whether client websites get built in GHL, and whether GHL becomes the whole delivery platform that clients use.

## The three tracks

**Track B: first website for businesses with none** (the live track, locked offer)

- $49 to start, $150 when it's live. Live in 5 business days or no balance.
- Domain in the client's name, first year included.
- $29/month to keep it running (hosting, SSL, backups, monthly SEO re-check, up to 4 small changes a month). First month free, cancel any time, client keeps everything.
- One-page site: 3 services, hours, area, tap-to-call, enquiry form to email and phone, linked to their Google listing, passes our SEO gate (`seo_gate.py`: title, description, canonical, sitemap, schema, etc.), set up in Google Search Console and Bing.
- Not included: logo, photos, extra pages, payments, real booking system, ads.
- Upsell at day 45 only, to clients whose site is producing enquiries: **Growth $99/mo** (Google Business posts, review requests, more pages, monthly report), Funnel +$199, Automation $300, Full system $999.
- Change requests: $49 small change, $99 new section, $149 extra page.
- Year-one value per client: $199 + 11 x $29 = $518. "The monthly is the business."
- Current demo sites are on Netlify Drop. Payment links for $49 and $150 exist (processor not named in files: check).

**Track A: SEO engine** (internal tool name "Clearlane")

- Audit, plan and tracker today. Building toward a monthly SEO retainer (monthly report, rank tracking, content briefs, link outreach, local content). Uses Semrush, Apollo, Apify. Retainer prices not set yet.

**Track C: fixing AI-built sites**

- Businesses whose Lovable/Bolt/Replit/Base44 sites still show defaults (Google lists them as "Lovable App", no sitemap, no schema). We show it in a 60 to 90 second Loom, fix it for the same price shape as Track B. Email and Loom only, any state.

**The full system (the $999 target sale)**

- Website + funnel + AI automation + CRM + lead pipeline + automated follow-up + calling/text + $100 communication credit (a credit, not unlimited) + setup. Automations sold around specific jobs: missed-call text back, lead qualification, booking, follow-up, review requests, nurture.

## Compliance rules (locked, the spine must respect these)

- **Illinois is the phone state.** Hand-dialled only.
- **Texas is email and Loom only.** No calls, no texts, no live video, ever (we won't register under Texas Bus. & Com. Code ch. 302).
- **Ohio parked.** Growth comes from "green" states where calling is allowed without registration (26 states incl. Illinois, Georgia, New York).
- **Never an autodialer, predictive dialer or recorded voicemail drop.** Permanent.
- **No call recording** on Track B calls.
- **A text only goes out when the person asked for it in a live conversation**, and the rep logs their exact words. No text after a voicemail or an unanswered call.
- Scrub call lists against the National Do Not Call Registry.
- No quoting modelled "you're losing $X a month" figures. No copied Google reviews or photos on demos.
- Texas email lane runs from its own warmed sending domain.

So any GHL feature that auto-dials, power-dials, records by default, or fires SMS from a workflow without a logged consent flag is a risk. The fit analysis must say how to lock those off per sub-account.

## Current tools around it

- Lead Gen Tool (Python): scrapes Google Maps, enriches, scores and segments prospects (HOT/WARM/COLD by need: full stack, funnel, website, CRO), outputs call sheets and trackers (Excel). Dallas and Chicago lists built.
- SEO baseline kit and `seo_gate.py`.
- Crowd-test and Monte Carlo simulation kit for testing offers.
- Excel trackers and scorecards for the week.

## What this analysis must settle for RevLabs

- Should every paying client get their own GHL sub-account from day one (even the $29/month site client), or only once they upgrade to Growth $99 / $999?
- Can the $29/month tier survive the GHL cost per sub-account plus usage? At what client count does the agency plan pay for itself?
- Should Track B sites be built on GHL Sites (only if they pass `seo_gate.py`) or stay as static builds on Netlify/Cloudflare with GHL forms embedded?
- White-label: sell "RevLabs" as our own branded platform (GHL SaaS mode) at $99 / $299 / $999 tiers, or keep GHL invisible and sell done-for-you?
- How our internal prospecting pipeline (Lead Gen Tool output) flows into GHL for calling and email, with the compliance flags carried over.


---

# Context: Table Foundry International (TF Direct, US)

Condensed from `Table Foundry\International Expansion` (Strategy Sep 2026/TF_Direct_US_Strategy_Sep2026.md, Competitive Landscape 24 Sep 2026, Pricing Logic, BUILD-PLAN, Product Suite v2; Jul to Sep 2026).

## What it is (decided Sep 2026)

- **US only.** UK, Canada, Australia dropped.
- Buyer: independent US restaurants, 1 to 5 locations, already paying big third-party delivery commissions.
- **First city: New York City.** NYC raised the cap on what delivery apps can take from 23% to 43% in 2025, and apps had to notify restaurants by 30 June 2026. That's the reason to call.
- Pitch, one sentence: your own ordering page, delivery drivers included in the price, and a payment split you can see, not a bill you have to trust.
- Only two claims up front: (1) delivery is built in (Uber Direct dispatch, already built and verified), (2) you see exactly what you're paid and what's taken out.
- The real moat is the payment plumbing: **Stripe Connect with each restaurant as its own merchant of record.** Not the delivery feature.
- Parent: Table Foundry already runs a zero-commission ordering platform for restaurants in India. The international build reuses its modules.

## Price and cost (decided)

- **Charge $249/month.** No $99 founding price.
- Real cost to serve: about **$12.85 per restaurant per month** at ~300 orders (about $4.50 hosting share, about $8.35 Stripe, SMS and email).
- **Ignore the old $122/month cost figure.** It came from a retracted document.
- Check real Stripe Connect payout fees once the first pilot is live.
- Don't say "zero commission, ever" in the US until the India platform-fee bug is confirmed off.

## Stack already built or specced (this is custom, not GHL)

- Next.js multi-tenant "golden template" (menu, cart, guest accounts, domains, billing, KDS, go-live, i18n, audit log, impersonation).
- Supabase / Postgres with row-level security across 34 tables, tenant isolation tested.
- Stripe Connect payments, Uber Direct delivery dispatch.
- Twilio SMS (~$0.008 per SMS, 2 to 3 per order), SendGrid email, a small LLM "concierge".
- Automated site generation per restaurant at about $3 build cost (Design DNA tokens, cuisine copy packs).
- Planned or partly built modules from the India side: **TF Reputation** (review requests, negative-feedback catch), **TF Engage** (email/SMS/WhatsApp campaigns: welcome, win-back, birthday), **TF Loyalty** and **GuestIQ** (guest CRM, repeat recognition), **MenuIQ**, **TF Ops**.
- Loyalty/CRM and marketing automation are the biggest "table stakes" gaps vs competitors (10 of 13 have loyalty/CRM, 8+ have marketing automation). If prospects stall on "does it have loyalty?", those move up the build order.

## Competitors studied (13)

Toast, Owner.com, ChowNow, Popmenu, SpotOn, Square, Flipdish, me&u, GloriaFood (being sunset April 2027), Olo/BentoBox, Thanx, Slice, Deliverect. Nine are US-first. This is the most crowded market in the research.

## Go-to-market rules (decided)

- **No international marketing spend before 30 Nov 2026** (India evidence-window rule). Direct one-to-one sales conversations are allowed now.
- One person part-time (Sovit), no new hire, until one restaurant pays for a real pilot.
- First steps: pick 2 to 3 NYC independents, pitch the two claims, ask for a deposit or signed commitment, onboard the first by hand, then build the repeatable version.
- **First contact by email, not text.** Cold texts to US numbers are a TCPA risk. WhatsApp only once a US WhatsApp Business account and templates are approved (not yet).
- Not doing yet: reservations, a consumer discovery app, multi-location chains, AI-led pitching.

## Where GHL could plausibly fit for TF (test each, don't assume)

1. **TF's own sales pipeline**: NYC prospect list, email-first sequences, discovery calls, pilot deposits. Small volume (2 to 3 restaurants first, then dozens).
2. **Restaurant-facing marketing layer**: use GHL (white-labelled as "TF Engage" / "TF Reputation") for review requests, win-back and birthday campaigns, instead of building those modules. This is the big question.
3. **Onboarding and support**: intake forms, onboarding checklist, client comms.

The tension to resolve: TF's cost to serve is $12.85/month and the price is $249. A GHL sub-account per restaurant plus usage could multiply the cost base. Guest and order data already lives in Supabase; putting guests in GHL too means syncing two databases. And ordering, payments and delivery will never live in GHL. So the question is whether GHL is worth it as the **engagement layer only**, or whether finishing TF's own Engage/Reputation modules is cheaper and cleaner.


---

# GHL teardown protocol (for the teardown agent)

## Browser and account safety (non-negotiable)

- Adam logs in himself. Never type, store, read out or ask for a password or 2FA code. If a login screen appears, stop and ask Adam.
- Create or use **one sandbox sub-account** named `ZZ-TEST-Spine-Analysis`. Do all hands-on testing there. Don't open, edit or export data in any other existing sub-account unless Adam says so.
- **No spending.** Don't buy phone numbers, add-ons, AI Employee, WordPress hosting, domains, credits or marketplace apps. Don't change the plan, billing, SaaS configurator prices or payment settings. If a test needs something paid, write down what it would cost and ask Adam.
- **No outbound messages to real people.** Only test SMS/email/calls to a number or inbox Adam gives you, or use preview/test modes.
- **No deletions** of anything that existed before this session.
- Don't turn on any dialer, power dialer, call recording or voicemail drop, even to test. Read the settings only.
- Log every action you take in the account in `/analysis/ghl-spine/teardown-action-log.md` (time, what, why).

## Part 1: plans and money

Check the live pricing page, the account's billing page (read only) and the docs. Record, with the date checked:

- Every plan tier (Starter, Unlimited, Agency Pro / SaaS Pro, anything newer): monthly and annual price, sub-account limits, users, what's locked per tier.
- **SaaS mode**: which tier, how the SaaS configurator works, how rebilling of phone/email/AI usage works, the markup we can set, and **what the Stripe requirements are**. Check specifically whether an Indian company can connect a Stripe account that works for SaaS mode, or whether a US entity is needed.
- **Usage costs** (LC Phone, LC Email, Twilio/Mailgun if bring-your-own): per SMS segment, per MMS, per call minute in/out, per number per month, per email, A2P 10DLC brand and campaign fees, carrier fees.
- **AI costs**: Conversation AI, Voice AI, Reviews AI, Content AI, AI Employee bundle, workflow AI steps. Per sub-account or per use.
- Add-ons: white-label mobile app, WordPress hosting, premium workflow actions, extra domains, anything with a monthly fee.
- Hidden or easy-to-miss costs: premium triggers/actions billed per execution, email validation, phone number porting, international sending.

## Part 2: features, tried in the sandbox where possible

For each, say what it does, whether you tested it live, what's missing, and what it would replace in our stack:

- Contacts, custom fields, tags, smart lists, **custom objects** (limits, relations, whether workflows can trigger on them), associations.
- Opportunities and pipelines (multiple pipelines, stage automations, reporting).
- Conversations inbox (SMS, email, calls, FB/IG, Google Business chat, WhatsApp, live chat widget).
- Phone system: numbers, call routing, IVR, missed-call text back, **dialer settings, recording defaults and how to switch recording off per sub-account**, DND and quiet-hours controls, consent tracking.
- Workflows: triggers, actions, if/else, waits, webhooks in and out, custom code steps, AI steps, limits and execution costs. Build one missed-call-text-back workflow and one 5-step follow-up in the sandbox.
- Calendars: round-robin, team calendars, reminders, no-show handling.
- Sites, funnels, forms, surveys: build one Track B-style one-page site in the sandbox and check page title, meta description, canonical, sitemap, schema/JSON-LD support, custom code injection, llms.txt/robots.txt control, page speed (run Lighthouse or PageSpeed on the test URL).
- Payments: Stripe/other integrations, invoices, text-to-pay, subscriptions, order forms.
- Reputation: review requests, review widget, AI replies, Google Business integration.
- Reporting and attribution: dashboards, call reporting, ad reporting, per-sub-account and agency-level.
- Snapshots: what they copy (and don't), how updates push to existing sub-accounts.
- Users and permissions: roles, limiting what a client user can see and change.
- Mobile app (LeadConnector) and white-label app options.
- API v2 and webhooks: auth (OAuth vs private integration tokens), rate limits, what objects are exposed, marketplace app model. Can our own Postgres/Supabase and Python tools read and write to it cleanly?
- Data export: what can be exported (contacts, conversations, opportunities, custom objects, workflows) and in what format.

## Part 3: white-label mechanics

- Agency white-label domain for the desktop app: how many per agency account, can we run three brands (Leasify, RevLabs, Table Foundry) from one agency account, or does each brand need its own?
- Custom domains per sub-account, branded emails, removing GHL/LeadConnector branding from client-facing pages, invoices, emails, the mobile app.
- What the end client still sees that says "HighLevel" or "LeadConnector".
- GHL's terms on reselling and what they forbid.

## Part 4: usability

- How long did it take to set up each sandbox test, and what was confusing.
- What a non-technical local business owner would have to learn to use it themselves.
- What our India team would have to learn to operate 50 sub-accounts.
- Known reliability problems (outages, deliverability complaints, support quality) from community sources, clearly tagged as such.

## Output format

`01-GHL-TEARDOWN.md`, one section per part above. Every line tagged `[live-account]`, `[ghl-docs]`, `[ghl-pricing-page]`, `[marketplace]`, `[community/reddit]` or `[assumption]`, with dates on prices. Screenshots saved to `/analysis/ghl-spine/screens/` and referenced by filename.


---

