# 02 Leasify: GHL fit

> **Master note (see `00-VERDICT.md`, `07`):** the verdict holds, with these changes. SMS is modelled at 20 segments per lead, not 12. The $499 tier is capped at 500 leads, not 1,000. HomeEasy starts as a 100-hour MVP. Listing-site leads get email or a call first. SLA wording excludes vendor outages.

Basis: `01-GHL-TEARDOWN.md` (docs only, checked 28 Sep 2026, no live account). Facts are cited as `[tag, via 01]`. Anything not in 01 is marked `[assumption]`. Our labour is $8/hour (range $5 to $12), SMS delivered cost is about $0.0115 per segment, and the GHL plan is Unlimited at $297 shared by three lines.

## Decisions this report makes

- **One sub-account per client**, run by us, client never logs in. HomeEasy gets its own sub-account first as the test bed. A sub-account is a separate client workspace inside our GHL agency account.
- **Postgres stays the system of record.** GHL is the messaging, calendar and pipeline layer on top. No custom objects at launch.
- **Matching, voucher checks, price floors, Lift Score and reports stay in Python/Postgres.** Results are pushed into GHL as plain fields and text.
- **Texts go out under the client's own A2P brand**, not Leasify's. A2P 10DLC is the US carrier registration needed to text from normal numbers.
- **No white-label "Leasify platform".** Done-for-you, tool invisible.
- **Amy Scott's platform is unknown.** The files never say where she runs. Nothing below claims GHL replaces her. It says what GHL could do and what to test.

---

## 1. What this line needs the spine to do

Seventeen workflows, taken from the context file. Format: trigger, action, owner, outcome.

| # | Workflow | Trigger | Action | Owner | Outcome |
|---|---|---|---|---|---|
| 1 | Lead intake | Lead arrives from listing site, web form, call, text, email or chat | Create or update one lead record, tag the source | System | One place for all leads instead of 5+ |
| 2 | Instant first response | New lead | Reply in under 60 seconds, 24/7. Ask budget, move-in date, credit, voucher, needs | AI (Amy Scott) | Answers captured, lead engaged |
| 3 | Qualification tiers | Answers captured or lead replies | Move lead through All, Responders, Non-Negative, Hot | System | Hot means budget, move date and credit all stated |
| 4 | Lift Score | A human progresses a lead | Score 5 variables, block progress below 1.2 | System, then human | Only worthwhile leads get human time |
| 5 | Unit matching | Lead reaches Responder or better | Match against 111 properties / 215 units (crime, transit, pets, laundry, elevator) | Postgres service | Shortlist of units sent to renter |
| 6 | Voucher check | Renter says they have a voucher | Compare to CHA payment standards and Mobility Zone caps | Postgres service | Only eligible units offered |
| 7 | Price floors | Before any unit is offered | Apply area floors (e.g. Chicago premium $1,500 per bed) | Postgres service | No below-floor offers. Texas floors not set |
| 8 | Tour booking and hand-off | Hot lead, or renter asks for a tour | Book first. Chicago: staff within 24h. Texas: warm hand-off | AI books, human staffs | Tour on the calendar with an owner |
| 9 | Tour reminders | Tour booked | Send at 24h, 2h, 15 min | System | Fewer no-shows |
| 10 | No-show recovery | Tour marked no-show | Rebook sequence, flag to human | System, human | No-show rate from about 35% toward under 20% (target, not a feature) |
| 11 | Application chasing | Tour done, application started | Ask for documents, income proof, follow up until approval | Human plus system | Application approved |
| 12 | Dead-lead reactivation | Lead idle 7, 14, 30, 90+ days | Timed sequences | System, human on reply | Target 10% of 90-day leads reactivated |
| 13 | Founder daily report | Every day | Deal-by-deal list with owner, committed action, due time | Adam reads | Nothing slips |
| 14 | Weekly client report | Every week | Performance summary per client | Ops sends | Proof for retainer and SLA |
| 15 | Alerts | New or urgent lead (`lead_pulse_monitor.py`) | Score urgency, geocode, Slack/email, de-duplicate | System | Human moves fast on urgent leads |
| 16 | Commission tracking | Lease signed | Record commission, invoice landlord, chase | Ops | Commission collected. Rates not set yet |
| 17 | Renewal reminders | 60 days before lease end | Ping past renter | System | Repeat business |

---

## 2. Workflow fit table

Effort is our build hours (first build, one snapshot). A snapshot is a saved template of a sub-account setup that can be loaded into new sub-accounts. "Premium" means GHL's $0.01 per execution workflow actions [ghl-docs, via 01]. Monthly cost is at base volume (see section 5).

| # | Workflow | GHL feature | Fit | How it would be built | Hrs | Monthly cost it drives | Risk |
|---|---|---|---|---|---|---|---|
| 1 | Lead intake | Inbox, forms, chat widget, phone, API v2 | Needs integration | Web, phone, text, email, chat are native [ghl-docs, via 01]. Listing sites are not native [assumption, via 01]: forward their notification emails to a mailbox, parse in n8n or Python, create the contact by API v2. Use API, not GHL's inbound webhook, to avoid $0.01 per lead | 24 | $0 on GHL side (inbound webhook would be $10) | Parsers break when a site changes its email. Renters from listing sites gave no opt-in we control (see A2P) |
| 2 | Instant first response | Conversation AI plus a first-touch workflow | Native with workaround | Workflow sends a fixed first text within seconds. Conversation AI takes the thread. Prompt holds the 5 questions and client-approved facts. Writes answers to contact fields [assumption: field writing not confirmed in 01] | 20 | About $21 AI (pay-per-use) plus SMS | Wrong claims in chat. Deliverability. Depends on the Amy Scott test |
| 3 | Qualification tiers | Pipeline stages, tags, smart lists | Native | One pipeline, four stages. Workflow moves stage when fields fill | 12 | $0 | Low |
| 4 | Lift Score | Custom fields, workflow | Native with workaround | Score computed in Postgres (5th variable still unnamed in the tracker), pushed to a number field. A workflow holds the lead if under 1.2 | 12 | Inside Workflow Pro bucket | Formula drifts if it lives in two places. Keep it in Postgres only |
| 5 | Unit matching | Custom webhook action, custom fields | Needs integration | GHL sends renter facts to our matching API. API returns top 3 units as text and links. A workflow texts them. No property data stored in GHL | 40 | $0.01 per call, in Workflow Pro bucket | Latency on every reply. Service down means no matches. Add a fallback text and a human task |
| 6 | Voucher check | Same webhook | Needs integration | Rule tables (CHA standards, Mobility caps) in Postgres. Returns pass/fail plus max rent | 16 | Included in row 5 call | Payment standards change. Need an update routine and owner |
| 7 | Price floors | Same webhook | Needs integration | Floors table in Postgres by area and bed count. Texas rows empty until Adam sets them | 6 | Included in row 5 call | Texas has no floors, matching there runs unfloored |
| 8 | Tour booking, hand-off | Calendars, appointment triggers, internal notifications | Native with workaround | Calendar per client. AI books through calendar link. Chicago: unassigned slot plus 24h staffing task. Texas: workflow rings or texts the assigned human | 18 | $0 | Calendar features not verified in 01 [assumption]. Hand-off to client staff is by notification, not login |
| 9 | Tour reminders | Workflow with waits before appointment | Native | Three SMS at 24h, 2h, 15 min. Reply C to confirm | 10 | 3 segments per tour, in SMS usage | Quiet hours. Texas and Chicago are both Central time, fine |
| 10 | No-show recovery | Appointment status trigger | Native with workaround | Status "no show" starts rebook texts, then a human task after 2 tries | 10 | In SMS usage | Someone must mark no-shows. If not, the trigger never fires |
| 11 | Application chasing | Pipeline stage, tasks, forms with upload | Native with workaround | Stage "Application" starts a doc-request sequence. Human tasks with due dates. Income checks stay in the client's own system | 14 | In SMS usage | Documents by text is a privacy risk. Use a secure form link |
| 12 | Dead-lead reactivation | Smart list on last activity, workflow, Drip Mode for bulk [ghl-docs, via 01] | Native | Four timed sequences (7, 14, 30, 90). Email first, SMS second. Replies stop the sequence and alert a human | 14 | One-off blast of about 9,000 segments per 3,000 old leads is about $100 | Old leads with no proven consent. Carrier filtering on cold blasts. Needs legal view |
| 13 | Founder daily report | API v2 read of opportunities and tasks, plus Postgres | Needs integration | Nightly script pulls open deals and tasks from every sub-account (100 requests per 10s per location [marketplace, via 01], plenty), renders one page, emails it. GHL has no cross-account deal report [assumption] | 24 | $0 | Only as good as owner and due-time discipline in GHL tasks |
| 14 | Weekly client report | Postgres plus script, sent by LC Email | Needs integration | Template PDF or email per client from Postgres events. Built once, runs for all | 20 | About $0 | Numbers must match what the client sees in their own system |
| 15 | Alerts | Workflow internal notifications, Slack action | Native with workaround | Keep `lead_pulse_monitor.py` for urgency scoring and geocoding. Point it at GHL events. Simple alerts by GHL email/SMS notification. Slack action is premium [community, via 01] | 8 | About $0.01 per alert | Two alert paths can double-fire. De-dupe stays in the script |
| 16 | Commission tracking | Invoices, Stripe [ghl-docs, via 01] | Native with workaround | Rates not set, so do not build now. Later: ledger table in Postgres, invoice landlord from the entity that has Stripe (see questions) | 16 | $0 until built | Stripe India is invite-only [stripe-docs, via 01]. Which entity bills is unknown |
| 17 | Renewal reminders | Date field plus date-based workflow trigger [assumption: not in 01] | Native with workaround | Store lease-end date on signed lease. Workflow fires at minus 60 days | 6 | Tiny | Nobody captures the lease-end date today |

Build total: 270 hours. Add 30 hours for snapshot packaging and testing: **300 hours, about $2,400 at $8** ($1,500 to $3,600 at $5 to $12).

### Listing sites and property systems

| System | Native in GHL? | Plan |
|---|---|---|
| Zillow, Apartments.com | No [assumption, via 01 section 2.3] | Email forward and parse, or their lead feeds if the client's account offers one. Needs a live check per site |
| AppFolio | No connector found [community, via 01] | Already feeds Postgres for WPD by our own script. Do not push AppFolio data into GHL |
| Yardi, RealPage, Entrata | No connector found [community, via 01] | Same. Client-by-client API or export. Do not promise this at sale |

Rule: property software feeds Postgres. GHL only ever sees the finished shortlist text.

---

## 3. What GHL replaces, and what it can't

**Replaces**
- The 5+ places leads sit today, as one inbox per client.
- Excel stage tracking (stages and owners), not the score.
- Tour booking sheets and manual reminders.
- Manual dead-lead follow-up.
- Part of the Slack/email alerts.
- Possibly Amy Scott's messaging layer. Unknown, see below.

**Can't replace**
- Matching, voucher checks, price floors, Neighbourhood Intel. GHL has no joins, no SQL and no unit-level rule logic [assumption, via 01 section 2.1].
- Lift Score formula.
- Founder and client reports.
- The AppFolio, Yardi, RealPage, Entrata links.
- Commission logic.
- The client's own property management or leasing CRM. We do not replace it, which fits "we don't implement CRMs".

---

## 4. What we'd still have to build or buy

- **Postgres schema** (already decided 19 Aug): leads, tours, consent, message log, properties, units, voucher rules, floors, scores.
- **Matching API** (Python, small web service) wrapping the existing tools and JSON database.
- **Event sink**: GHL webhooks to Postgres for contact, message, appointment, stage changes. Postgres holds the full history so GHL can be swapped out later (exit is painful [community, via 01]).
- **n8n or Python jobs**: listing-email parser, nightly founder report, weekly client PDFs, and the existing `lead_pulse_monitor.py`.
- **Consent ledger** in Postgres: text of the opt-in, timestamp, source. GHL has no consent ledger [assumption, via 01 section 2.4].
- **Onboarding checklist per client**: sub-account from snapshot, number, A2P brand and campaign, sending domain, lead-source forwarding, recording off, quiet hours, AI prompt with client facts.
- **Provisioning script** (optional, later): create sub-accounts and push settings by API. Whether Unlimited's "basic API" allows this or needs Agency Pro's "advanced API" is unknown [ghl-pricing-page, via 01].
- **Shared infrastructure**: small server for n8n and the matching API plus managed Postgres, monitoring. $60/mo at 1 to 10 clients, $150 at 50, $250 at 100 [assumption].

### System of record: the rule

| Data | Lives in | GHL holds |
|---|---|---|
| Properties, units, voucher rules, floors | Postgres only | Nothing. Shortlist text only |
| Lead facts (budget, move date, credit, voucher, tier, Lift Score) | Postgres | A copy in custom fields for workflows |
| Consent and full message log | Postgres | Live conversation thread |
| Pipeline stage, appointments | Both, synced by webhook | Working copy |
| Reports | Postgres | Nothing |

- GHL custom objects: max 10 per sub-account and 300K records each [ghl-docs, via 01]. Capacity is not the problem, 215 units is tiny. The problem is no matching logic and a second copy to keep in sync. So: **zero custom objects at launch**. Revisit only if a client wants to see unit lists inside GHL, and then only as a read-only copy.
- GHL says workflows can trigger on custom object create and change [ghl-docs, via 01]. Not needed here.
- Test for the rule: if GHL vanished tomorrow, we lose workflows and numbers, not data.

---

## 5. Cost per client per month

Plan: Unlimited $297 shared across three lines with the same client count N. Plan share per client = $297 / (3 x N) [shared assumption]. Postgres, n8n and the matching service are shared infra.

### Volume assumptions per client per month (all [assumption])

Leasify clients are lead-heavy. Base is a small PM or locator with a steady listing feed.

| Driver | Low | Base | High | Note |
|---|---|---|---|---|
| New leads | 300 | 1,000 | 3,000 | Regional PM at 500 to 2,000 units is the high case |
| SMS segments, in and out, all workflows | 3,600 | 12,000 | 36,000 | About 12 per lead: chat, tour reminders (3 per tour), reactivation |
| Emails | 1,800 | 6,000 | 18,000 | Email first for old leads |
| Conversation AI replies | 1,800 | 6,000 | 18,000 | About 6 per lead |
| Voice AI minutes (inbound only) | 0 | 100 | 500 | Outbound AI calls off, see AI section |
| Phone numbers | 1 | 2 | 3 | $1.15 each |
| Premium workflow actions | 3,000 | 10,000 | 30,000 | About 3 to 10 per lead |

### Unit prices used

- SMS $0.0115 delivered [$0.00747 plus $0.004 carrier, shared assumption]. Email $0.675 per 1,000. Number $1.15. [ghl-docs, via 01]
- Conversation AI $0.0035 per reply, range $0.002 to $0.005 [community estimate, via 01].
- Voice AI $0.06 per minute plus inbound call $0.01165, so $0.072 per minute [ghl-docs, via 01].
- A2P: brand $22.50 (low) or $64 (base and high) one-time, spread over 12 months. Campaign $1.50 (low) or $10 a month [ghl-docs, via 01]. Base uses the $10 standard campaign to be safe. Low-volume mixed at $1.50 may be enough, live check owed.
- Workflow Pro $10 (10,000 runs) at low and base, $25 (30,000 runs) at high [ghl-docs, via 01].
- Labour per client per month, ongoing plus onboarding spread over 12 months: 3h low, 5h base, 10h high.
- Build cost: 300 hours, $2,400, spread over 12 months = $200 a month, split across N clients.

### Base case, per client per month (US$)

| Line | 1 client | 10 clients | 50 clients | 100 clients |
|---|---|---|---|---|
| GHL plan share (Unlimited) | 99.00 | 9.90 | 1.98 | 0.99 |
| Usage: SMS 138.00, email 4.05, numbers 2.30, Conversation AI 21.00, Voice AI 7.20 | 172.55 | 172.55 | 172.55 | 172.55 |
| Add-ons: A2P campaign 10.00, A2P one-time spread 5.33, Workflow Pro 10.00 | 25.33 | 25.33 | 25.33 | 25.33 |
| Integrations (shared infra share) | 60.00 | 6.00 | 3.00 | 2.50 |
| Our labour, per client (5h at $8) | 40.00 | 40.00 | 40.00 | 40.00 |
| Build cost share | 200.00 | 20.00 | 4.00 | 2.00 |
| **Total** | **596.88** | **273.78** | **246.86** | **243.37** |
| Margin at $499 | -97.88 (-20%) | 225.22 (45%) | 252.14 (51%) | 255.63 (51%) |
| Margin at $999 | 402.12 (40%) | 725.22 (73%) | 752.14 (75%) | 755.63 (76%) |

Agency Pro $497 case, only needed for SaaS mode: plan share is 165.67, 16.57, 3.31, 1.66. Extra over Unlimited: +66.67, +6.67, +1.33, +0.67 per client.

### Low and high volume, total cost per client

| Case | 1 client | 10 clients | 50 clients | 100 clients |
|---|---|---|---|---|
| Low: total | 446.45 | 123.35 | 96.43 | 92.94 |
| Low: margin at $499 | 52.55 (11%) | 375.65 (75%) | 402.57 (81%) | 406.06 (81%) |
| High: total | 1,007.93 | 684.83 | 657.91 | 654.42 |
| High: margin at $499 | -508.93 | -185.83 | -158.91 | -155.42 |
| High: margin at $999 | -8.93 (-1%) | 314.17 (31%) | 341.09 (34%) | 344.58 (34%) |

### What the numbers say

- **Volume decides margin, not the GHL plan.** SMS is about 80% of base usage ($138 of $173). The plan share is under 4% once N reaches 10. The same texts cost the same on any platform.
- **A heavy-lead client at $499 loses money.** At 3,000 leads a month cost is about $650 to $690. Regional PMs at $999 hold about 31 to 34%.
- **Fix in the contract, not the tool:** state a fair-use lead cap on the $499 tier (about 1,000 leads a month). Above it, bill about $225 per extra 1,000 leads (cost about $173 plus 30%) or move the client to the $999 tier. This does not change the entry price. Adam decides.
- **Excluded:** the service delivery labour (people running tours, calls, application chasing). That cost exists with or without GHL. Margins above are after platform cost only.
- **AI pricing pick:** pay-per-use beats AI Employee. Growth ($50) covers only 1,000 responses, below base volume of 6,000. Unlimited ($97) only wins above about 27,700 replies a month at $0.0035. Pay-per-use is $21 at base, $6 to $63 across the range.
- **Pilot cost:** 2 free weeks is about half a month of usage plus set-up, roughly $150 to $200 per new client at base, plus A2P wait time (below).
- **Rate limits:** 100 requests per 10 seconds and 200,000 a day per location [marketplace, via 01]. A 5,000-contact reactivation import takes minutes. Not a constraint.

### A2P 10DLC: whose brand sends renter texts

| Option | Cost | Verdict |
|---|---|---|
| **Client's own brand** (each client registers in its own sub-account) | $22.50 to $64 once, then $1.50 to $10 a month [ghl-docs, via 01]. We do the paperwork. Client gives legal name, EIN, website, privacy policy | **Pick.** Renters see the property or locator name they inquired about. Carriers check the message matches the brand. One client's problem cannot block the others |
| Leasify's brand for all clients | One $10 campaign | Reject. Texts say "Leasify", renters expect the property name. One shared brand sending for many landlords looks like a lead reseller [assumption]. One carrier flag hits every client. MSM may not be able to register without a US EIN [01 says unclear] |
| HomeEasy | Own brand, own campaign | Use HomeEasy's own brand for HomeEasy's sub-account |

- **Timing:** 24 to 72 hours, up to about 7 business days if manual vetting [community, via 01]. Register on day 1 of the free pilot or the "instant response" promise cannot be tested. Unregistered texts are blocked by carriers [community, via 01].
- **Opt-in problem:** the most common rejection is no visible opt-in language [ghl-docs, via 01]. Listing-site leads did not fill in our form. The client's own web form can carry opt-in wording. For listing-site leads, first reply may need to be email or a call, with text starting once the renter replies or gives consent. Have counsel confirm before launch [assumption].
- **Cost at 50 clients:** about $500 a month in campaign fees at $10 each, already inside the table above.

---

## 6. Usability

### Amy Scott and Conversation AI

- **Platform unknown.** Her stack, cost and prompt are not in the files. Find out before deciding anything about replacement.
- **What GHL offers:** Conversation AI on text channels, Voice AI on phone, Workflow AI [ghl-docs, via 01]. Not tested live.
- **Could it do Amy's job?** For first response, 5 questions and booking a tour: likely yes for text. Untested points that decide it: writing answers into contact fields, calling our matching API mid-chat, booking calendar slots, stopping when a human replies. See questions.
- **Cost per client:** base $21 a month AI, plus SMS. $6 low, $63 high. Voice AI (inbound only) about $7 at 100 minutes.
- **No outbound Voice AI.** The FCC treats AI voices as artificial voice under TCPA, so prior express written consent is needed [community, via 01]. Listing-site leads do not have that. Text-first, human calls.

### Where the human stays in the loop

The June handover said AI can't qualify or close. The August plan uses AI triage. Both fit if AI collects and a human decides.

| Step | AI | Human |
|---|---|---|
| First reply, 5 questions, FAQ from client-approved facts | Yes | Reviews a sample weekly |
| Tier assignment (Hot rule is mechanical: budget, move date, credit all stated) | Workflow, from fields | Confirms before Lift Score allows progress |
| Voucher eligibility, rent quotes, exceptions, fair-housing topics | Never states as final | Yes. Chicago treats voucher income as protected [assumption, legal check owed] |
| Tour booking | Yes | Staffs within 24h (Chicago), warm hand-off (Texas) |
| Applications, approvals, complaints, negotiation | No | Yes |
| Stop rule | Workflow turns AI off when a human replies or the lead goes Hot | Takes over |

### Our team

- **Builders:** one workflow builder in India owns the snapshot (272 to 300 hours over roughly 8 to 10 weeks part-time). Community says 6 to 8 weeks to be confident in GHL [community, via 01].
- **Daily operators:** the leasing ops team lives in the unified inbox, calendar and pipeline, on the mobile app. That is the realistic surface [via 01].
- **Learning curve:** the top GHL complaint [community, via 01]. Keep it small: one pipeline, one calendar, about 12 workflows, no funnels or sites.
- **Fragility:** 40 incidents in 90 days, median 12 minutes [community, via 01]. Alerts must not depend on GHL alone, hence the Postgres event log and the Python alert script.
- **Update risk:** pushing a snapshot update over customised sub-accounts may overwrite edits [assumption, via 01]. Forbid local edits, or tag them.

### The end client

- **PMs and locators will not log in.** They already have AppFolio, Yardi or a locator CRM. A second login fights "we don't implement CRMs".
- **They get:** the weekly report, a Slack or email alert on Hot leads, a calendar invite for tours, and texts sent in their brand.
- **If a client's leasing agent must act,** send SMS or email with the lead card. If they insist on a login, use a limited user with no builder access. Users are unlimited [ghl-pricing-page, via 01]. Treat as an exception, not the offer.

---

## 7. White-label angle

- **No.** Do not sell a "Leasify platform" now.
- **Why PMs will not pay for it:** they buy an outcome (faster response, more tours, recovered leads). They already pay for property software. Adding a software fee raises the price above $499 for something they do not want to learn. It also breaks the locked rule that Leasify does not implement CRMs.
- **Mechanics also block it:**
  - SaaS mode needs Agency Pro ($497) and Stripe on the agency. Stripe India is invite-only. It needs a US entity first [stripe-docs, via 01].
  - GHL's minimum advertised price rule limits advertising a package of 2 or more core features below its standard price [ghl-docs, via 01]. Another reason not to sell software cheaply.
  - White-label mobile app is $497 a month [ghl-pricing-page, via 01]. No revenue to justify it.
- **Option most likely to convert:** done-for-you, one flat retainer ($499 or $999), tool invisible, with a stated lead cap. It matches the locked price path and pilot. What clients see: their own brand on texts, a Leasify-branded weekly report.
- **Branding to set up:** client-brand A2P registration, client or subdomain sending domain for email (needs a DNS record from the client), Leasify-branded report.
- **Later, not now:** once 10 or more clients are live and enterprise multifamily asks for dashboards, offer a read-only report page built from Postgres. That does not need GHL SaaS mode.

---

## 8. Verdict for this line

**Use GHL for part.** The part: the messaging and follow-up layer per client: inbox, texts and email, calendars, tour reminders, no-show rebooking, pipeline stages, reactivation sequences, and (if the test passes) the AI first responder. Postgres and Python keep matching, vouchers, floors, Lift Score, reports, alerts logic, commission and all system-of-record data.

Three biggest reasons:
1. GHL replaces the plumbing we would otherwise build: inbox, calendars, reminders, reactivation, A2P handling. That plumbing is the follow-up problem Leasify sells. It costs $297 shared, about $10 a client at 10 clients.
2. It can't do the hard, valuable parts (unit matching, voucher rules, Lift Score, deal report). Keeping them in Postgres also gives us a clean exit from GHL, which is painful otherwise.
3. Usage, not the plan, is the cost. About $246 to $274 per client at base volume on 10 to 50 clients (45 to 51% margin at $499 before service labour). A lead cap is needed because high-volume clients lose money at $499.

**One thing that would change the call:** if the sandbox test shows Conversation AI cannot write answers into contact fields, call our matching API mid-chat and hand off to a human, then Amy Scott stays where she is (or is custom built) and GHL shrinks to calendar, reminders and reactivation. If it also cannot ingest leads and hold client-brand A2P, drop to "Don't use GHL".

---

## Questions for the teardown agent / live-account check

1. Conversation AI: can it write extracted answers (budget, move date, credit, voucher) into contact custom fields, call a webhook mid-conversation, book calendar appointments, and stop when a human replies or a tag is set? Does pay-per-use need any setup or minimum? [dependent cells: rows 2 and 8, AI cost]
2. Per-reply token cost with a 300-word knowledge base and a 4-turn history: is $0.0035 right, or higher? [assumption in section 5]
3. Calendars: round-robin, unassigned slot, reminders, "no show" status trigger, time zones. Not researched in 01. [rows 8 to 10]
4. Are inbound webhook, custom webhook and custom code premium at $0.01? Are custom-object triggers, date-based triggers and plain SMS/email premium? [Workflow Pro assumption]
5. A2P: are brands and campaigns per sub-account only? Is a client-brand registration allowed when the agency (MSM, India) files it? What is the throughput cap on low-volume standard, and is the $1.50 mixed campaign enough for 12,000 segments a month?
6. Date-based workflow trigger (lease-end minus 60 days): does it exist as a trigger on a custom date field? [row 17]
7. Do our API needs (contacts, opportunities, tasks, sub-account creation, webhooks, custom fields) work on Unlimited's "basic API", or do they need Agency Pro's "advanced API"? [cost, section 4]
8. Is there any Zillow, Apartments.com, AppFolio, Yardi, RealPage or Entrata app in the GHL marketplace? [rows 1, 5]
9. Does a Private Integration Token get its own rate limit, and can one be scoped per sub-account? [event sink design]
10. Snapshot push: does it overwrite customised workflows in a live sub-account?
11. Drip Mode for bulk: can it be used for reactivation sequences with per-contact timing and quiet hours? [row 12]

Not GHL questions, for Adam:
- Which platform does Amy Scott run on today, and what does it cost per month?
- What is the 5th variable of the Lift Score?
- Which entity bills landlords for commission, and does it have a US Stripe account?
- What does the client's opt-in language for listing-site leads look like, and has counsel approved texting them?
