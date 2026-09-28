# 03 RevLabs US SMB: GHL fit

Basis: 01-GHL-TEARDOWN.md (docs only, checked 28 Sep 2026, no live account). "[via 01]" means the fact and its source tag come from 01. GHL for RevLabs' own prospecting is settled and not re-argued. This report covers delivery to clients.

Terms used: **sub-account** = a client workspace inside our GHL agency. **Snapshot** = a template of a sub-account we can copy. **DND** = do not disturb, a per-channel block on messaging a contact. **A2P 10DLC** = US carrier registration for business texts. **PIT** = private integration token, a key for our own scripts to call the GHL API.

Decisions in one place:

| Question | Decision |
|---|---|
| Sub-account from day one for the $29 client? | No. Sub-account created on the day a client signs Growth $99 or higher. |
| Track B sites | Stay static (Netlify/Cloudflare). GHL only for funnel/booking pages on a subdomain, after a live test. |
| White-label / SaaS mode | No. Keep GHL invisible, sell done-for-you. SaaS needs a US entity first. |
| Track A and Track C | GHL stays out of delivery. Its CRM only tracks the prospects. |
| Texas | Its own sub-account with no phone number at all. |
| Plan | Starter $97 until a 4th sub-account is needed. Then Unlimited $297. Not Agency Pro. |

---

## 1. What this line needs the spine to do

Twenty workflows, taken from the context file. Prospecting (1 to 7) is live now. Delivery (8 to 20) only matters once a client signs.

| # | Trigger | Action | Owner | Outcome |
|---|---|---|---|---|
| 1 | Lead Gen Tool run finishes | Import prospects with state, tier, need, DNC and consent fields | Ops (script) | Call and email lists ready, flags intact |
| 2 | Rep starts call block (7:30 pm to 12:30 am IST) | Work the CALL_OK list, HOT first, hand-dialled | Founder | Conversations, not autodialled dials |
| 3 | Call ends | Log disposition, note, move pipeline stage | Founder | Clean funnel numbers |
| 4 | Prospect says "yes, text me" on a live call | Rep logs the exact words, date, rep name | Founder | A consent record that can be shown later |
| 5 | Consent record exists | Send the agreed text (link, time) | Workflow | Text only to people who asked |
| 6 | Any state, prospect in email lane | Cold email plus Loom link sequence, stop on reply | Workflow | Replies without calls or texts |
| 7 | Texas prospect | Email and Loom only, own warmed domain | Workflow | No call or text can ever happen |
| 8 | Prospect says yes | Take $49 start, later $150 at go-live, $29/month after | Founder | Cash and a subscription |
| 9 | $49 paid | Start 5-business-day build clock, reminders, no balance if late | Ops | Site live on time |
| 10 | Client emails a change or month ends | Log change (up to 4 a month, else $49/$99/$149), run SEO re-check | Ops | Monthly promise kept |
| 11 | Day 45 after go-live, site producing enquiries | Task to offer Growth $99 or higher | Founder | Upsell only to clients it suits |
| 12 | Enquiry form submitted on a client site | Notify owner (email), count it | Form handler | Owner sees leads, we see proof |
| 13 | Client's caller gets no answer | Missed-call text back | Workflow | Lead not lost |
| 14 | Lead replies | Ask a few qualifying questions, score | Workflow (or AI) | Owner sees only real jobs |
| 15 | Qualified lead | Offer times, book, remind, no-show follow-up | Workflow | Job booked |
| 16 | Lead goes quiet | Follow-up sequence, stop on reply | Workflow | Recovered leads |
| 17 | Job marked done | Review request (email; text only with flag) | Workflow | More Google reviews |
| 18 | Old customers on list | Nurture emails | Workflow | Repeat work |
| 19 | Month ends (Growth) | Google Business posts, monthly report | Ops | Visible value for $99 |
| 20 | Full system sold | Track the $100 communication credit against usage | Ops | Credit, not unlimited |

---

## 2. Workflow fit table

Effort hours and per-client costs are [assumption], my estimates. Unit prices are from 01.

| # | Workflow | GHL feature | Fit | How it would be built | Hours | Monthly cost it drives | Risk |
|---|---|---|---|---|---|---|---|
| 1 | Import with flags | Contacts, custom fields, smart lists, CSV import; later API v2 upsert with a PIT [marketplace, via 01] | Native with workaround | CSV import first (300 rows a month is small), Python API script when weekly | 10 | $0 | Unknown whether CSV import can set DND per row |
| 2 | Call block | Smart list plus manual dialer, tasks [ghl-docs, via 01] | Native with workaround | Smart list: lane = CALL_OK, dnc = CLEAR, tier order. Click-to-call from the record | 4 | Calls $0.0166/min out [ghl-docs, via 01] | Power dialer sits next to the manual one |
| 3 | Disposition | Pipelines, tags, notes, call log | Native | 8 stages, tag per outcome | 3 | $0 | Low |
| 4 | Consent log | Custom fields plus tag-triggered workflow | Native with workaround | Fields in section below. No consent ledger in GHL [assumption, via 01] | 4 | $0 | Rep discipline. Mirror to our own DB |
| 5 | Text after consent | Workflow SMS, DND, If/Else, LC Phone | Native with workaround | DND-SMS on by default, cleared only by the consent workflow | 5 | $0.0115 delivered per segment [assumption]; A2P $1.50 to $10/mo [ghl-docs, via 01] | Can MSM (India, no EIN) register A2P? 01 says unclear |
| 6 | Cold email | LC Email or own SMTP [ghl-docs, via 01], workflows | Native with workaround | Own sending subdomain, SPF/DKIM/DMARC, 2 to 4 week warm-up [community/reddit, via 01] | 8 | $0.675 per 1,000 [ghl-docs, via 01] | Deliverability is the top complaint. Cold-email policy not checked |
| 7 | Texas lane | Separate sub-account, no number | Native | Own sub-account, own sending domain, no LC Phone | 6 | $0 | Slot count on Starter |
| 8 | Payments | Invoices, payment links, subscriptions [ghl-docs, via 01] | Needs integration | Keep the existing payment links and processor. Move to GHL only once a Stripe account is confirmed | 3 | Processor fee about $1.14 per $29 [assumption] | Processor and entity not named in context |
| 9 | Build clock | Pipeline, workflow waits, tasks | Native with workaround | Stage per build step, wait 3 days then task, day 5 alarm | 5 | $0 | Low |
| 10 | Changes and re-check | Form to task; Python `seo_gate.py` writes result to a note or field | Needs integration | Track B clients live as contacts in our sales sub-account, not their own | 4 | $0 | Low |
| 11 | Day-45 upsell | Workflow wait, field check, task | Native with workaround | Field `enquiries_30d` set by our form handler script | 3 | $0 | Low |
| 12 | Enquiry notify | Form embed, notification | Native (Growth+) / outside GHL (Track B $29) | Track B: our own form handler emails the owner. Growth+: GHL form embedded on the static site | 2 | $0 | Form needs a sub-account, so not for $29 |
| 13 | Missed-call text back | LC Phone number, missed-call automation | Native with workaround | Not covered in 01 [assumption it exists]. Gate on consent flag or prior inbound text | 4 | Number $1.15, call in $0.01165/min | Highest compliance risk, see below |
| 14 | Qualification | Workflow If/Else on replies; Conversation AI optional | Native with workaround | Scripted 3-question flow first. Conversation AI pay-per-use only if needed | 6 | $0, or $0.002 to $0.005 a reply [community/reddit, via 01] | AI Employee at $50 or $97 would wipe the margin |
| 15 | Booking | Calendars, reminders [assumption, not researched in 01] | Native | Calendar per client, 24h and 2h reminders | 4 | SMS segments | Check calendars live |
| 16 | Follow-up | Workflows: wait, stop on reply | Native | Snapshot sequence | 5 | Segments and emails | Sends to unconsented numbers if gate missing |
| 17 | Review requests | Reputation, review links [ghl-docs, via 01] | Native with workaround | Email default. SMS needs a "customer OK to text" checkbox on the client's job form | 5 | $0.01 per AI reply if used | Negative-feedback catch not verified |
| 18 | Nurture | Email workflows | Native | Snapshot sequence | 4 | $0.675 per 1,000 | Client's old lists may lack consent |
| 19 | Report and GBP posts | Dashboards; GBP messaging only in 01 | Needs integration | Report built by our tools (Semrush, Claude). GBP posting not confirmed in 01 | 6 | $0 | GHL social/GBP posting unverified |
| 20 | $100 credit | Wallet, rebilling [ghl-docs, via 01] | Native with workaround | We absorb usage up to $100. No hard per-sub-account cap known | 3 | Actual usage | Rebilling runs through Agency Stripe. Unlimited plan rebills at cost only |

Total build: about 94 hours, plus 10 hours of testing and the compliance audit script, so about 104 hours. That is $832 at $8/hour (range $520 to $1,248) [assumption]. Snapshot once, reuse for every client.

### The $999 full system, mapped

| Promise | GHL pieces | Notes |
|---|---|---|
| Missed-call text back | LC Phone number with client's line forwarded in, missed-call workflow | Needs the client's calls to pass through a GHL number. Forwarding leg costs $0.0166/min |
| Qualification | Workflow Q&A, optional Conversation AI | Scripted first |
| Booking | Calendar, form, reminders | Embed on the site or a GHL page on a subdomain |
| Follow-up | Sequence, stop on reply | Consent gate first |
| Review requests | Reputation | Email first |
| Nurture | Email workflows | Monthly, low volume |
| Website, funnel | Static site plus GHL funnel on `book.` subdomain | Funnel +$199 in the ladder |
| $100 communication credit | Agency wallet absorbs usage | Cost is the actual usage, about $15 a month at base volume, so $100 lasts about 6.7 months. At high volume it lasts about 2.3 months |
| No AI Employee | Do not buy the $50 or $97 add-on | Keeps the $999 economics intact |

### Lead Gen Tool to GHL: how the flags travel

The Python tool computes the flags. GHL stores them and filters on them. GHL does not scrub against the Do Not Call registry [assumption, via 01], so the scrub stays in Python.

| Field (custom) | Values | Set by |
|---|---|---|
| `state` | 2-letter code | Tool |
| `lane` | CALL_OK / EMAIL_ONLY / HOLD | Tool. TX = EMAIL_ONLY. Ohio = HOLD. The 26 green states = CALL_OK. Any other state = HOLD [assumption] |
| `dnc_status`, `dnc_scrub_date` | CLEAR / LISTED / UNSCRUBBED, date | Tool. Call list requires CLEAR and a recent scrub date |
| `sms_consent` | Yes / No, default No | Rep |
| `sms_consent_words` | The prospect's exact words | Rep |
| `sms_consent_date`, `sms_consent_rep` | Date, name | Rep |
| `tier`, `need_type`, `score`, `maps_url`, `batch_id` | HOT/WARM/COLD, full stack/funnel/website/CRO | Tool |

Steps:

1. Tool exports two files per run. Texas rows go to the Texas sub-account. All other rows go to the main sales sub-account. Ohio and HOLD rows are not imported.
2. Week one: CSV import with field mapping. Later: a Python script using a PIT per sub-account. Limit is 100 requests per 10 seconds per app per resource [marketplace, via 01], far above our 300 rows a month.
3. Smart lists per tier. The call list filters on lane, dnc_status and tier. Excel call sheets stay only as a backup print.
4. Weekly Python pull from the API back to the Excel tracker (contacts, stages, consent fields). Free, unlike an outbound webhook at $0.01 an execution [community/reddit, via 01].
5. Email lane: one warmed sending domain per sub-account [ghl-docs, via 01]. That is why Texas gets its own sub-account.

### Compliance lock-offs, per sub-account

01 says none of these are enforced by GHL itself. They rely on settings and discipline [assumption, via 01]. I rank each as hard (cannot be done by mistake) or soft (a person could undo it).

| Rule | How to enforce in GHL | Strength | What 01 could not confirm |
|---|---|---|---|
| No autodialer, power dialer, voicemail drop | Leave power dialer off in Settings, Phone System. Upload no voicemail audio. Only founders are admins. Callers get the user role. Weekly screenshot audit | Soft | Whether power dialer or voicemail drop can be disabled per sub-account or hidden by a user permission. 01 says not found |
| No call recording | Recording toggle off on every number [ghl-docs, via 01]. Put it in the snapshot checklist. Off in client sub-accounts too by default | Soft | Whether new numbers default to off. Whether an agency-wide lock exists (01 says none documented). Whether the API can read number settings for an audit |
| No workflow SMS without logged consent | Contact-level DND-SMS on at import. A consent workflow clears it only if `sms_consent_words` is not empty. Second check: If/Else on the same field before every SMS. Quiet-hours If/Else on local time [community/reddit, via 01] | Medium | Whether CSV import can set DND. Whether DND blocks manual sends and bulk actions as well as workflows. Whether a user permission can hide Bulk Actions |
| Texas: no calls, no texts | Layer 1: Texas sub-account with no number and no A2P. Layer 2: `lane = EMAIL_ONLY`. Layer 3: first If/Else in every SMS or call workflow, state not TX | Hard (layer 1) | Whether two sending domains fit in one sub-account. If they do, the separate sub-account is a choice, not a need |
| No outbound AI voice | Do not buy AI Employee. Do not enable Voice AI outbound | Soft | Whether Voice AI or Conversation AI is off by default in a new sub-account |
| Text only after a spoken request, no text after a voicemail | The consent fields above. A voicemail or missed call never sets the flag | Medium | Nothing in GHL stops a rep typing a manual text if DND is off |

Missed-call text back (workflow 13) collides with the locked rule. The caller called the client. They did not ask for a text in a live conversation. Legal view is unsettled [assumption]. Default to: send only if `sms_consent = Yes` or the contact texted first. Otherwise the workflow creates a callback task and sends an email if one exists. Test an inbound call menu ("press 1 for a text") that sets the consent flag, and get a US lawyer to review before selling it in the $999.

Client sub-accounts add one point: the client is a user of their own account. Give the client a limited user, not admin, and keep the agency admin ours. Role toggles are not confirmed in 01.

---

## 3. What GHL replaces, and what it can't

**Replaces**
- Excel call sheets and weekly trackers (contacts, stages, dispositions). Not the scoring.
- A separate booking tool, review-request tool, and follow-up tool for Growth and up.
- Manual email sending from a mailbox.
- Payment links, but only later, only if a Stripe account exists.

**Cannot replace**
- Lead Gen Tool: Google Maps scrape, enrichment, HOT/WARM/COLD scoring.
- DNC registry scrub.
- `seo_gate.py`, the SEO baseline kit, and the crowd-test kit.
- Netlify or Cloudflare hosting for the $29 site (see next section).
- Loom.

### Track B sites: static, not GHL Sites

Decision: **Track B one-pagers stay on Netlify or Cloudflare. GHL is never the host of the $29 site.** Reasons:
- 01 says root `llms.txt` is not possible on GHL sites, and JSON-LD and speed are unconfirmed [community/reddit, via 01].
- Our promise is "client keeps everything, cancel any time". 01 found no portable HTML export from GHL sites, only snapshots [community/reddit, via 01]. A GHL-hosted site breaks that promise.
- A hosted GHL site needs a sub-account, which the $29 tier cannot carry (next section).

Where GHL pages are allowed: funnel or booking pages for Funnel and Full-system clients, on a subdomain such as `book.clientsite.com`. The static root site keeps `llms.txt`, sitemap and schema. 01 says GHL cannot build pages under arbitrary folder paths, so a subdomain fits.

Live test before any GHL page goes to a client (build one in a sandbox sub-account, run `seo_gate.py`):
1. Title and meta description present in the raw HTML (view source, no JavaScript).
2. Canonical present and correct.
3. `sitemap.xml` at the domain root and lists the page.
4. JSON-LD (LocalBusiness) added in head code appears in the raw HTML. This is unconfirmed in 01.
5. `robots.txt` editable.
6. `/llms.txt` at the root: expected to fail. Test whether a URL redirect can serve it. If not, record a fail.
7. Page speed on mobile against the same page on Cloudflare. Same content, same images.
8. Page content is in the server HTML, not built by JavaScript after load.
9. Any way to export the page as portable HTML.

Pass rule: items 1 to 5 and 7 to 9 must pass. Item 6 is waived only for subdomain pages.

### Track A and Track C

- **Track A (Clearlane SEO engine):** GHL adds nothing to delivery. Semrush, Apollo, Apify and the tracker do the work. GHL's SEO add-on is $79 per sub-account [ghl-pricing-page, via 01] and duplicates Semrush. Use GHL only to hold retainer prospects in the sales pipeline. Retainer prices are not set, so nothing to model.
- **Track C (fixing AI-built sites):** stays out. It is email and Loom only, any state. It ships as a static Track B style site. Prospecting lists live in the existing sales sub-account as an email-lane pipeline.

---

## 4. What we'd still have to build or buy

| Item | Why | Rough cost |
|---|---|---|
| Python push/pull script (PIT per sub-account) | Flags in, results out | 6 to 8 hours |
| Track B form handler (Cloudflare Worker or similar) | $29 clients have no sub-account. Emails the owner, appends a row we can count | 3 hours, free tier [assumption] |
| Consent mirror in our own DB or sheet | GHL has no consent ledger. It also protects us if we leave (01 exit section) | 3 hours |
| Compliance audit checklist per sub-account | Recording off, power dialer off, DND default, Texas wall | 1 hour per client, 10 hours to build |
| Warmed sending domains | One for the main lane, one for Texas, 2 to 4 weeks each | About $12 a year each [assumption] |
| Snapshot (sub-account template) | Delivery workflows 12 to 20 | Inside the 104 hours |
| US entity plus Stripe (Atlas $500, $100 a year, 2 to 6 weeks [stripe-docs, via 01]) | Only needed for SaaS mode, wallet rebilling with card, or a clean way to collect | Not now |
| US lawyer review | MAP clause and the missed-call text back | One-off [assumption] |

No Zapier, Make or n8n at this stage. Python plus the API v2 covers it.

Order of work over 180 days:
1. Days 0 to 30: workflows 1 to 7 (settled prospecting) with the lock-offs and the live checks below.
2. Days 30 to 90: workflows 8 to 12, the form handler, and the Track B build tracker.
3. From the first Growth signing: snapshot for 13 to 20, one client at a time.

---

## 5. Cost per client per month

Plan share = $297 / (3 x N), where N is the client count for the client type shown. Agency Pro $497 shown as an extra line. Carrier fee assumption: +$0.004 per SMS segment, so about $0.0115 delivered. Stripe-style processing fee 2.9% + $0.30 [assumption; processor not named in context].

**Volumes per client per month [assumption]**

| Item | Low | Base | High |
|---|---|---|---|
| Growth: emails | 200 | 500 | 1,500 |
| Growth: SMS segments (in and out) | 0 | 100 | 400 |
| Growth: premium workflow actions | 0 | 100 | 300 |
| Growth: our hours | 1 | 1.5 | 2.5 |
| Full system: emails | 800 | 2,000 | 5,000 |
| Full system: SMS segments | 250 | 600 | 2,000 |
| Full system: call minutes (in, plus the same forwarded out) | 60 | 150 | 400 |
| Full system: AI replies (pay-per-use) | 100 | 300 | 1,000 |
| Full system: premium actions | 50 | 300 | 1,500 (capped at Workflow Pro $10) |
| Full system: ongoing hours | 2 | 3 | 5 |
| Full system: setup hours (one-time) | 12 | 20 | 35 |
| Track B $29: hours (4 small changes plus re-check) | 0.5 | 0.75 | 1.5 |
| Labour rate | $5 | $8 | $12 |

### Track B $29 client, recommended (no sub-account)

The same at every client count, because GHL is not touched.

| Row | Any N |
|---|---|
| GHL plan share | $0.00 |
| Usage | $0.00 |
| Add-ons (domain renewal $12 a year, from year two) | $1.00 |
| Integrations and payment fee | $1.14 |
| Our labour (0.75 h x $8) | $6.00 |
| **Total** | **$8.14** |
| Price / margin | $29 / $20.86 (72%) |

Range: $4.64 (low) to $20.14 (high), so margin $24.36 down to $8.86.

Same client if we forced a sub-account anyway (adds plan share plus 0.25 h admin, $2):

| Row | N=1 | N=10 | N=50 | N=100 |
|---|---|---|---|---|
| Total | $109.14 | $20.04 | $12.12 | $11.13 |
| Margin | -$80.14 (-276%) | $8.96 (31%) | $16.88 (58%) | $17.87 (62%) |
| Agency Pro line, total | $175.81 | $26.71 | $13.45 | $11.80 |
| Agency Pro line, margin | -$146.81 | $2.29 | $15.55 | $17.20 |

If the client also texts, add about $6 (usage $2.64 plus A2P $3.38): at N=10 the margin falls to about $3.

### Growth $99 client (sub-account, texting on, base volumes)

| Row | N=1 | N=10 | N=50 | N=100 |
|---|---|---|---|---|
| GHL plan share | $99.00 | $9.90 | $1.98 | $0.99 |
| Usage (500 emails $0.34, 100 segments $1.15, number $1.15) | $2.64 | $2.64 | $2.64 | $2.64 |
| Add-ons (A2P $1.50 a month plus $22.50 one-time over 12) | $3.38 | $3.38 | $3.38 | $3.38 |
| Integrations and payment fee (100 premium actions $1.00, fee $3.17) | $4.17 | $4.17 | $4.17 | $4.17 |
| Our labour (1.5 h x $8) | $12.00 | $12.00 | $12.00 | $12.00 |
| **Total** | **$121.19** | **$32.09** | **$24.17** | **$23.18** |
| Price $99, margin | -$22.19 (-22%) | $66.91 (68%) | $74.83 (76%) | $75.82 (77%) |
| Agency Pro $497 line: total | $187.86 | $38.76 | $25.50 | $23.85 |
| Agency Pro: margin | -$88.86 (-90%) | $60.24 (61%) | $73.50 (74%) | $75.15 (76%) |

Cost excluding plan share ranges from $8.31 (low, email only) to $58.26 (high, standard A2P at $10, heavy texting, 2.5 h at $12). At N=10 the high case margin is $30.84 (31%).

### Full system client, ongoing monthly run cost (base)

The $999 sits in the context as a target sale. It does not say whether it is monthly or a one-off build, or whether the $100 credit repeats. I assume a one-off build price and a one-off credit [assumption]. If $999 is monthly, margin is above 85% at N=10 and the rest of this section still holds.

| Row | N=1 | N=10 | N=50 | N=100 |
|---|---|---|---|---|
| GHL plan share | $99.00 | $9.90 | $1.98 | $0.99 |
| Usage (email $1.35, SMS $6.90, calls $4.24, number $1.15, AI replies $1.20) | $14.84 | $14.84 | $14.84 | $14.84 |
| Add-ons (A2P $1.50 plus one-time over 12) | $3.38 | $3.38 | $3.38 | $3.38 |
| Integrations (300 premium actions) | $3.00 | $3.00 | $3.00 | $3.00 |
| Our labour (3 h x $8) | $24.00 | $24.00 | $24.00 | $24.00 |
| **Total ongoing** | **$144.22** | **$55.12** | **$47.20** | **$46.21** |
| Agency Pro line: total | $210.89 | $61.79 | $48.53 | $46.88 |
| If the ongoing fee is the $99 Growth price: margin | -$45.22 (-46%) | $43.88 (44%) | $51.80 (52%) | $52.79 (53%) |

Range excluding plan share: $20.35 (low) to $129.16 (high).

**One-off economics of one $999 sale (base):** price $999, minus 20 h build ($160), A2P registration $22.50, the $100 credit (spent over time), payment fee $29.27 = about $687 (69%). Range about $427 (high labour) to $787 (low labour).

Two points:
- The ladder has $99 as the only ongoing fee. That is thin once the credit is gone (44% at N=10). Bill usage above the credit at cost by our own invoice until a US Stripe exists. Or set the care fee at $139 or more to hold 60%.
- We cannot hard-cap a sub-account at $100 without rebilling [assumption, not found in 01]. Track usage weekly per client.

### When does the $297 plan pay for itself?

Contribution per client before plan cost (base): Growth $76.81, Full system $53.78 ongoing (at a $99 fee), Track B forced into a sub-account $18.86.

| Case | Clients to cover the plan |
|---|---|
| Growth clients cover the full $297 | 4 (3.9) |
| Growth clients cover only the $200 step from Starter $97 to Unlimited | 3 |
| Full system ongoing fees cover $297 | 6 |
| One $999 build covers about 2.3 months of the full $297 | 1 sale |
| $29 Track B clients each given a sub-account | 16 (15.7). Never worth it as a reason to buy the plan |
| Growth clients cover Agency Pro $497 | 7 (6.5) |

Rule: stay on Starter while the 3 sub-account slots hold RevLabs sales, RevLabs Texas email, and one other. Buy Unlimited when a 4th slot is needed (across all lines) or the 3rd Growth client is close. Do not buy Agency Pro.

### Sub-account from day one, or on upgrade?

**On upgrade to Growth $99 or higher. Never for the $29 client.**
- Margin: at N=10 a forced sub-account cuts the $29 margin from $20.86 to $8.96. At N=1 it goes negative.
- Nothing to use: the $29 client gets a static site, an emailed enquiry, and a monthly re-check. No inbox, no texts, no need for GHL.
- Keep-everything promise: static files move anywhere. A GHL site does not (01 exit section).
- Compliance surface: every sub-account is a place where recording, dialer or SMS settings can be wrong. Fewer sub-accounts, fewer audits.
- Where the Track B enquiry count lives: our own form handler, feeding the day-45 upsell check.

---

## 6. Usability

**Our team**
- Two founders call and sell. Someone in India builds and runs. 01 puts a confident operator at 6 to 8 weeks and a comfortable one at 1 to 3 weeks [community/reddit, via 01].
- One person owns the snapshot and the audit checklist. Founders only touch contacts, call lists and notes.
- Daily use for founders: smart list, click to call, disposition, consent fields. That is small. Ten to fifteen minutes to learn the consent step, and it needs a drilled habit.
- The risky part is that dangerous features (power dialer, voicemail drop, bulk SMS) are one click away from a tired caller at midnight IST.
- Reliability: 40 incidents in 90 days, median 12 minutes [community/reddit, via 01]. Acceptable for prospecting. A missed-call text back that fails silently is a client-visible failure, so test it weekly.

**End client**
- $29 client: never sees GHL.
- Growth $99: gets an email report. Does not log in.
- Full system: a busy HVAC or roofing owner will use only the inbox, calendar and pipeline in the free LeadConnector mobile app [ghl-docs, via 01] if at all. Plan on us doing the work. Do not buy the white-label app ($497) or Branded Client Portal ($49 per sub-account).

---

## 7. White-label angle

**Pick: keep GHL invisible and sell done-for-you. No branded "RevLabs platform" at $99 / $299 / $999.**

Why this is most likely to convert:
- The buyer is a plumber or a dentist who wants leads, not software. Our own pitch is "we find where your sales system leaks and fix it". A login and a dashboard dilute it.
- Our ladder is already priced as a service (Growth $99, Automation $300, Full $999).
- SaaS mode needs Agency Pro at $497 plus Stripe. Stripe India is invite-only [stripe-docs, via 01]. **It needs a US entity first** (Atlas $500, $100 a year, 2 to 6 weeks). Do not plan on it before that.
- GHL's reseller terms have a minimum advertised price rule for 2 or more core features, and a ban on comparing our product to HighLevel [ghl-docs, via 01]. A $99 tier with CRM plus funnels plus email may breach it. Needs a lawyer.
- As SaaS reseller we own support and disputes, and cannot send clients to HighLevel [ghl-docs, via 01]. A two-founder team calling US hours cannot also be a help desk.

What "invisible" still allows: our own sending and links domains per sub-account, the default LeadConnector app for the few clients who want it. Some GHL names show up (LC Phone and LC Email, PDF invoices) [community/reddit, via 01], so never say "no software". Say "we run it for you".

When to revisit: at 15 or more clients asking for self-serve logins, with a US entity and Stripe in place.

---

## 8. Verdict for this line

**Use GHL for part.**

The part:
- Yes: RevLabs' own prospecting, calling, email lane and pipeline (settled), with the compliance fields and the separate Texas sub-account.
- Yes, from the first signing: one sub-account per Growth $99, Automation and Full-system client, built from a snapshot.
- No: the $29 Track B site (hosting, form, sub-account), Track A, Track C, and any white-label or SaaS mode.

Three biggest reasons:
1. The $29 tier only works without a sub-account: $20.86 margin, against $8.96 at 10 clients if forced, and negative at 1 client. Static sites also keep the "client keeps everything" promise.
2. Compliance is enforceable by GHL config but not by GHL itself. It is hard only for Texas (no number in that sub-account). For dialer and recording it is soft, so it needs an audit habit.
3. White-label is blocked by Stripe India and the $497 plan cost. Done-for-you converts better for this buyer anyway.

One thing that would change the call: the live check on the power dialer, voicemail drop, recording and DND (questions 1 to 4 below). If they cannot be locked off in a client sub-account, the $999 delivery moves to a lighter tool and GHL stays for our own prospecting only.

---

## Questions for the teardown agent / live-account check

Dependent cells are marked [assumption] above.

1. Power dialer and voicemail drop: can either be disabled or hidden per sub-account, or per user role? Is there a user permission for the dialer at all?
2. Call recording: is it off by default on a new number? Any agency-wide lock? Can the API read a number's recording setting for an audit?
3. DND: can CSV import or the API set DND-SMS on each row? Does DND block manual sends and Bulk Actions as well as workflows? Can a workflow action clear it?
4. Which user role toggles exist: phone settings, Bulk Actions, workflow editing, export?
5. Missed-call text back: does the feature exist, what triggers it, can it be gated on a custom field, and can an inbound menu ("press 1 for a text") set a consent flag with a timestamp?
6. Sites test (9 items in section 3). Include: can a URL redirect serve `/llms.txt`, and does a GHL page render content server-side?
7. Sending domains: how many per sub-account? Is cold email allowed under LC Email and SMTP terms?
8. A2P: can MSM (India, no EIN) register its own brand? Which registrations are per sub-account? Can a client with an EIN register in our agency's name?
9. Wallet: is there a hard spend cap per sub-account with no rebilling? What are the wallet minimum and auto-recharge defaults?
10. Are standard actions (If/Else, DND, custom field update, wait) free? Is a custom-object or form trigger premium?
11. GHL forms embedded on a static site: does the embed work on Netlify and Cloudflare, capture a consent checkbox with a timestamp, and create the contact in the sub-account?
12. Social planner or GBP posting for Growth: exists and priced? 01 lists only GBP messaging and reviews.
13. Calendars and Reputation were not researched in 01: confirm reminders, no-show workflows and the negative-feedback catch.
14. Does a snapshot push overwrite client-edited workflows? Can sub-accounts be created by API on Unlimited, or is that Agency Pro only?
15. Which processor holds the current $49 and $150 payment links, and does MSM hold an active Stripe India account?

For Adam, not the teardown agent: is $999 one-off or monthly, does the $100 credit repeat, and does "enquiry form to email and phone" mean an SMS to the owner (that would need A2P per client).
