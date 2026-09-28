# 04 TF International: GHL fit

Line: Table Foundry International (TF Direct, US). Price $249/month, cost to serve $12.85 per restaurant per month at about 300 orders (both from the line context). GHL facts come from 01-GHL-TEARDOWN.md (docs only, checked 28 Sep 2026, no live account) and carry its tags "[tag, via 01]". Everything about our business that is not in the context file is marked [assumption].

Terms used: **sub-account** is one client workspace inside our GHL agency. **Snapshot** is a copy-paste template of a sub-account setup. **PIT** is a Private Integration Token, a static API key for our own server. **A2P 10DLC** is the US carrier registration for business texting. **Premium action** is a workflow step that costs $0.01 per run.

## 1. What this line needs the spine to do

Taken from the context file. "GHL?" says whether the step is even a candidate. Steps 15 to 17 never live in GHL and are listed so nobody tries.

| # | Trigger | Action | Owner | Outcome | GHL? |
|---|---|---|---|---|---|
| 1 | NYC target list built (2 to 3 independents first, then dozens) | Load prospects, tag by neighbourhood and cuisine, one pipeline stage per step | Sovit | One place to see every prospect | Candidate |
| 2 | Prospect enters "to contact" | Email-first sequence, stop on reply. No SMS step | Sovit | Reply or no reply, logged | Candidate |
| 3 | Prospect replies yes | Book discovery call, send reminder | Sovit, Adam | Call on calendar | Candidate |
| 4 | Discovery call done | Log notes, pitch the two claims (delivery built in, visible payment split), record objection | Adam | Next step or drop | Candidate |
| 5 | Restaurant agrees | Ask for a deposit or signed commitment | Adam | Pilot committed | Candidate |
| 6 | Pilot committed | Intake form, hand onboarding checklist (menu, domain, Stripe Connect, Uber Direct, go-live) | Sovit | First restaurant live by hand | Candidate |
| 7 | Pilot live | Owner check-ins, support requests, check real Stripe payout fees | Sovit | Owner stays happy, fee facts gathered | Candidate |
| 8 | Guest places first order | Welcome message (TF Engage) | System | Guest recognised | Candidate |
| 9 | Order delivered | Review request, email first, SMS only if consented (TF Reputation) | System | More public reviews | Candidate |
| 10 | Guest gives low rating | Catch it, alert owner (TF Reputation) | System, owner | Problem fixed before it goes public | Candidate |
| 11 | Guest silent for N days | Win-back message (TF Engage) | System | Repeat order | Candidate |
| 12 | Guest birthday | Birthday message (TF Engage) | System | Repeat order | Candidate |
| 13 | Repeat guest orders | Recognise, build loyalty (TF Loyalty, GuestIQ) | System | Retention | Partial |
| 14 | US WhatsApp Business account approved | Send approved templates (TF Engage) | System | New channel | Later |
| 15 | Order placed | Cart, payment via Stripe Connect (restaurant is merchant of record), 2 to 3 order-status SMS | Supabase, Stripe, Twilio | Order paid, guest informed | Never |
| 16 | Order needs a driver | Uber Direct dispatch | Platform | Delivered | Never |
| 17 | Kitchen receives order | KDS, menu, guest accounts, site generation | Platform | Restaurant runs | Never |
| 18 | Prospect stalls on "does it have loyalty?" | Move loyalty/CRM up the build order | Adam | Decision on build order | Decision, not workflow |

## 2. Workflow fit table

Hours are [assumption], at the shared $8/hour (range $5 to $12). "Cost driven" is per month. Restaurant-facing rows assume the base volumes in section 5.

| Workflow | GHL feature | Fit | How it would be built | Hours | Monthly cost it drives | Risk |
|---|---|---|---|---|---|---|
| 1 Prospect list and pipeline | Contacts, custom fields, pipeline | Native | CSV import, one pipeline, tags | 4 | $0 extra if spine already bought | Low |
| 2 Email-first sequence | Workflow, LC Email or own SMTP | Native with workaround | Own sending domain (not a restaurant domain), SPF/DKIM/DMARC, 2 to 4 weeks warm-up, stop on reply, no SMS action, no number provisioned [community, via 01] | 8 | Under $1 (LC Email $0.675 per 1,000 [ghl-docs, via 01]) | Medium: deliverability is the top complaint [community/reddit, via 01] |
| 3 Booking | Calendar, reminders | Native | Booking link in email 2, reminder workflow (calendars not verified in 01 [assumption]) | 3 | $0 | Low |
| 4 Discovery notes | Opportunity notes, custom fields | Native | Fields for objection, cuisine, current app commission | 2 | $0 | Low |
| 5 Deposit ask | Payment link or invoice | Needs integration | Use a Stripe payment link outside GHL. Do not depend on GHL payments: MSM Stripe status is unresolved (see 01 Q2) | 2 | $0 | Medium: entity question |
| 6 Onboarding intake, checklist | Forms, tasks, pipeline stages | Native with workaround | Form plus task template per pilot. Stripe Connect KYC, domain and KDS status live in TF, so the checklist is mirrored by hand | 8 | $0 | Low |
| 7 Owner support | Conversations inbox, email | Native | Owner emails land in one inbox. Owners are a few dozen contacts, not guests | 4 | $0 | Low |
| 8 Welcome | Workflow on tag/field | Native with workaround | Needs first-order tag pushed from Supabase | 8 | In section 5 | Medium: sync |
| 9 Review request | Reputation, workflow | Native with workaround | Trigger on "order delivered" tag from sync. Google review link per restaurant. GBP connect is per sub-account and manual [ghl-docs, via 01] | 12 | SMS $0.0115 per delivered segment (0.00747 plus 0.004 carrier) | Medium: sync, consent |
| 10 Low-rating catch | Workflow, Reviews AI | Native with workaround | Rating link, branch on score, owner alert. Not verified in 01 [assumption] | 10 | Reviews AI $0.01 per reply | High: see review-gating note below |
| 11 Win-back | Workflow, smart list | Native with workaround | GHL cannot compute "no order in 30 days" from Supabase. Supabase computes it and pushes a tag [assumption] | 14 | SMS or email usage | Medium |
| 12 Birthday | Birthday field trigger | Native | Push birthday field once, workflow sends yearly | 6 | Usage only | Low, if consent held |
| 13 Loyalty, repeat recognition | Tags, smart lists | Not possible for points earn and redeem at checkout. Native with workaround for tag segments | Order count and lifetime value pushed as fields. Points live at checkout in Supabase. 01 found no loyalty feature [assumption] | 6 (tags only) | $0 | High: this is the table-stakes gap |
| 14 Guest sync, Supabase to GHL | API v2, PIT, webhooks | Needs integration | Worker that upserts guests, sets fields and tags, queues under rate limits, alerts on failure, backfills | 60 | About $1 per restaurant hosting, [assumption] | High: two databases |
| 15 Sub-account per restaurant | Snapshot push, sub-account setup | Native with workaround | Runbook: create sub-account, push snapshot, number, A2P registration, sending domain, consent fields, recording off. Automating via API may need Agency Pro's advanced API [ghl-pricing-page, via 01, unclear] | 24 build, 3 per restaurant | Number $1.15, A2P $1.50 to $10 [ghl-docs, via 01] | Medium |
| 16 Owner sees results in TF dashboard | API v2 read | Needs integration | Pull review and campaign stats into the TF dashboard so the owner never opens GHL | 30 | $0 | Medium |
| 17 WhatsApp campaigns | WhatsApp add-on | Native with workaround | Blocked until US WhatsApp Business account and templates are approved | 4 later | $10 per sub-account plus Meta per-message rates from 1 Oct 2026 [ghl-docs, via 01] | Blocked |
| 18 Order-status SMS, checkout, Stripe Connect, Uber Direct, KDS | None | Not possible (by design) | Stay on Twilio, Stripe, Uber Direct, Supabase. GHL has no delivery, no restaurant ordering, no Connect marketplace split [ghl-docs, via 01] | 0 | 0 | n/a |

Review-gating note: a catch flow that sends only unhappy guests to a private form and only happy guests to Google is "review gating", which Google's policy and US rules on suppressing reviews frown on [assumption, not in 01, verify before building]. Build it so every guest sees the public link and low scores also alert the owner. This applies to both paths.

### The three fits, tested separately

**Fit 1: TF's own sales pipeline. Works, tiny.**
- Volume is a few dozen prospects. A sheet also works. GHL saves Sovit's time on sequences, reply capture and booking, roughly 20 hours to set up, 30 with onboarding forms.
- Marginal cost is $0 if Unlimited is bought for the other lines anyway. It is not worth $297 alone for TF.
- Compliance holds by construction: do not buy a number or register A2P for the TF sub-account. No SMS channel means no accidental cold text. Set DND (do not disturb) for SMS on every prospect as a second lock [ghl-docs, via 01].
- No marketing spend before 30 Nov 2026: a CRM subscription is a tool, not campaign spend, but Adam should confirm that reading. Outreach stays one-to-one, hand-picked, no bulk lists.

**Fit 2: restaurant-facing layer as "TF Engage" / "TF Reputation". Full build works, costs more than it saves.**
- Every restaurant needs its own sub-account, number, A2P registration, sending domain and Google connection. That is the cost driver (section 5).
- GHL does not remove the sync, the consent ledger or the owner dashboard. Those are the same hours as building the modules (section 5).
- Loyalty is not closed by GHL (see section 3).
- A-lite for the first pilots is the only version that makes sense (section 8).

**Fit 3: onboarding and support. Works, partly.**
- Intake form, checklist and owner inbox are Native and cheap, and share the fit 1 sub-account.
- The hard onboarding steps (Stripe Connect KYC, domain, KDS, Uber Direct) happen in TF's golden template. GHL only mirrors them. For 2 to 3 hand-onboarded pilots the go-live module already in the template plus a shared checklist is enough.

### Two-database sync: is it acceptable?

Guests and orders live in Supabase (34 tables, row-level security). Putting guests in GHL means a second copy.

Numbers, base case (300 orders a month per restaurant):
- About 10 orders a day, 3 to 4 API calls each (upsert contact, set fields and tags, add note). About 40 calls a day against 200,000 per day per app per location [marketplace, via 01]. Each restaurant is its own location, so each has its own budget.
- Burst limit is 100 requests per 10 seconds, so 10 a second. Backfilling 5,000 guests takes about 8 minutes. Fine.
- Premium webhook actions at $0.01 [ghl-docs, via 01]: if every order fires one inbound-webhook trigger or outbound webhook, 300 executions is $3 per restaurant per month. High case 900 is $9. Whether plain API writes plus tag triggers avoid premium billing is not in 01 (question below).

Verdict: **the dollars and rate limits are acceptable. The consistency risk is not, unless scope is cut hard.**
- The real risk is consent drift. A guest texts STOP to a GHL number. If Supabase does not learn it, TF's own sends can still text them. That is a TCPA problem. Supabase must stay the consent ledger and every opt-out must return to it.
- Guest deletion requests must be applied in both places. Sub-account isolation in GHL is not row-level security. Every staff user in a sub-account sees all its guests.
- One PIT per restaurant sub-account means dozens of secrets to rotate [assumption].
- Acceptable scope if used: one-way push (guest, last order date, order count, lifetime value, birthday, consent flags) plus one return channel (opt-out, reply received, review received). Never push order line items. Never let GHL be the source for anything.

## 3. What GHL replaces, and what it can't

Replaces, partly and only if used:
- TF Reputation, the module not yet built. GHL has review requests, Google review sync into the inbox and Reviews AI [ghl-docs, via 01]. The negative-feedback flow is unverified.
- TF Engage campaigns (welcome, win-back, birthday) for email and SMS. Not WhatsApp yet.
- A sheet or Notion for TF's own prospects and onboarding.

Can't replace:
- Ordering, cart, guest accounts, KDS, menu, site generation, Stripe Connect, Uber Direct, order-status SMS. Twilio stays for those, so a restaurant would have two SMS systems and two sending numbers under the GHL path unless bring-your-own Twilio works (unconfirmed in 01, see questions).
- **TF Loyalty and GuestIQ.** 01 found no native points, rewards or stamp-card feature. GHL can hold tags like "5+ orders" but cannot earn or redeem at checkout, because checkout is in Supabase. The table-stakes gap has two halves. Marketing automation (8 or more of 13 competitors) GHL could close. Loyalty and CRM (10 of 13) it closes only for the CRM half.
- MenuIQ, TF Ops.

## 4. What we'd still have to build or buy

If GHL is used for the restaurant layer:
- Sync worker, opt-out return channel, consent ledger in Supabase, owner-facing stats in the TF dashboard. About 100 to 130 hours of the total (section 5).
- Provisioning runbook and per-restaurant A2P registration (we do the paperwork, the restaurant supplies EIN and website details [ghl-docs, via 01]).
- Sending domain and DNS per restaurant, Google Business Profile connect per restaurant.
- Loyalty in Supabase regardless.

If GHL is used only for TF's own pipeline: a sending domain, a warm-up calendar, one form and one pipeline. No engineering.

**Risk outside GHL: Stripe Connect from India.** Flag only, not solved here.
- 01 found that a Stripe India platform account supports direct charges without application fees, and does not support separate charges and transfers or cross-border destination charges [stripe-docs, via 01]. TF's plan is Connect with each restaurant as merchant of record and a payment split the restaurant can see. That may be blocked or crippled from MSM's Indian account, and a US entity may be needed (01 cites Stripe Atlas, $500 plus $100 a year, 2 to 6 weeks [stripe-docs, community, via 01]).
- Claim 2 in the pitch ("you see exactly what you're paid and what's taken out") depends on this. Settle the entity question before promising the split to a pilot, and keep the pilot deposit off this path. Stripe invitation status for MSM is also an open question in 01.

## 5. Cost per client per month at 1, 10, 50, 100 clients

"Client" here means restaurant. All volumes [assumption]. Transactional order SMS (2 to 3 per order) stays on Twilio in every case and is already in the $12.85.

| Per restaurant per month | Low | Base | High |
|---|---|---|---|
| Orders (context: about 300) | 150 | 300 | 600 |
| Marketing SMS segments (review request, win-back, birthday, replies), opted-in guests only | 150 | 400 | 1,000 |
| Marketing emails | 500 | 1,500 | 4,000 |
| Premium workflow executions | 0 | 300 | 900 |
| AI review replies | 0 | 20 | 60 |

Shared rates: SMS delivered $0.0115 per segment ($0.00747 plus $0.004 carrier). LC Email $0.675 per 1,000 [ghl-docs, via 01]. Local number $1.15 [ghl-docs, via 01]. A2P campaign $1.50 to $10 per month, base $2 [ghl-docs, via 01]. GHL plan share is $297 / (3 x N) as instructed. Labour $8/hour.

Labour assumptions [assumption]: GHL path is 3 hours onboarding per restaurant amortised over 12 months ($2.00 a month), 0.5 hour a month per restaurant ($4.00), plus 6 hours a month of platform sync monitoring spread over N ($48 / N). Own-stack path is 2.33 a month per restaurant plus 3 hours a month of module upkeep ($24 / N).

### Path A: GHL sub-account per restaurant, incremental layer

| Row | N=1 | N=10 | N=50 | N=100 |
|---|---|---|---|---|
| GHL plan share, Unlimited ($297 / 3N) | $99.00 | $9.90 | $1.98 | $0.99 |
| Usage (400 SMS $4.60, 1,500 emails $1.01, number $1.15, AI replies $0.20) | $6.96 | $6.96 | $6.96 | $6.96 |
| Add-ons (second A2P campaign $2, premium actions $3) | $5.00 | $5.00 | $5.00 | $5.00 |
| Integrations (sync worker hosting) | $1.00 | $1.00 | $1.00 | $1.00 |
| Our labour | $54.00 | $10.80 | $6.96 | $6.48 |
| **GHL layer subtotal** | **$165.96** | **$33.66** | **$21.90** | **$20.43** |
| Existing cost to serve (context) | $12.85 | $12.85 | $12.85 | $12.85 |
| First A2P campaign (needed either way, probably not in the $12.85) | $2.00 | $2.00 | $2.00 | $2.00 |
| **Total cost per restaurant** | **$180.81** | **$48.51** | **$36.75** | **$35.28** |
| Line price | $249 | $249 | $249 | $249 |
| **Margin, $ and %** | $68.19, 27% | $200.49, 81% | $212.25, 85% | $213.72, 86% |
| Agency Pro $497 case: extra plan share | +$66.67 | +$6.67 | +$1.33 | +$0.67 |
| Total with Agency Pro, margin | $247.48, $1.52 (1%) | $55.18, $193.82 (78%) | $38.08, $210.92 (85%) | $35.95, $213.05 (86%) |

Usage range: about $5 (low) to $25 (high, counting premium actions), plus $2 to $10 for the second A2P campaign. Agency Pro is needed only for SaaS mode, which needs a US entity first, and TF should stay invisible (section 7), so it is shown for completeness.

### Path B: finish TF Engage and TF Reputation on the existing stack

| Row | N=1 | N=10 | N=50 | N=100 |
|---|---|---|---|---|
| Plan share | $0 | $0 | $0 | $0 |
| Usage (400 SMS at $0.0115 = $4.60, 1,500 emails on SendGrid at about $0.40 per 1,000 = $0.60 [assumption]) | $5.20 | $5.20 | $5.20 | $5.20 |
| Add-ons, integrations | $0 | $0 | $0 | $0 |
| Our labour | $26.33 | $4.73 | $2.81 | $2.57 |
| **Layer subtotal** | **$31.53** | **$9.93** | **$8.01** | **$7.77** |
| Existing cost to serve plus first A2P | $14.85 | $14.85 | $14.85 | $14.85 |
| **Total cost per restaurant** | **$46.38** | **$24.78** | **$22.86** | **$22.62** |
| **Margin at $249** | $202.62, 81% | $224.22, 90% | $226.14, 91% | $226.38, 91% |

### The cost tension, in plain numbers

- The existing cost to serve is $12.85. At 50 restaurants the GHL layer alone is $21.90, 1.7 times the whole existing cost. The own-stack layer is $8.01.
- GHL costs $23.73 more per restaurant at 10 clients, $13.89 more at 50, $12.66 more at 100. At 50 restaurants that is about $695 a month.
- At N=1 the shared plan share ($99) and sync monitoring ($48) make GHL a loss-leader. If the $297 is already paid for the other lines, TF's marginal plan cost is $0 and the layer is about $67 at N=1 and about $16 at N=50. Still above Path B.
- Margin is not the problem at $249 once N is 10 or more (78% to 86% on Path A). The problem is that the cost line TF quotes ($12.85) becomes about $35 to $49 and the story "cost to serve is tiny" stops being true. Two of the three GHL cost drivers scale per restaurant, not per plan: the second A2P campaign and the sync labour.

### Build hours, both paths [assumption]

| Item | Path A: GHL | Path B: own stack |
|---|---|---|
| Review, negative catch, welcome, win-back, birthday logic | 50 (snapshot) | 170 (60 Reputation, 110 Engage: sender, templates, STOP handling, quiet hours, logs) |
| Guest sync, opt-out return, retry, backfill | 60 | 0 (already in Supabase) |
| Consent ledger | 16 | 20 |
| Owner-facing stats in TF dashboard | 30 | 40 |
| Provisioning runbook and automation | 24 | 0 |
| Learning GHL (01: 6 to 8 weeks to confident) | 40 | 0 |
| **Total base** | **220 h, $1,760** | **230 h, $1,840** |
| Range | 150 to 350 h | 150 to 350 h |
| At $5 to $12 per hour | $750 to $4,200 | $750 to $4,200 |

Build hours are a wash. GHL saves module logic and spends it on sync, provisioning and learning. The decision rests on run cost, data in one place and control, not on build time.

**A-lite (2 to 3 pilots only):** hand-create sub-accounts, push snapshot, weekly CSV or small script of guests, review-request and win-back only, no dashboard. About 70 hours ($560): learn 20, snapshot 30, sub-account, number, A2P and domain 12, push script 8. This is about 3 to 4 calendar weeks at part-time pace, against roughly 11 to 12 weeks for Path B at 20 hours a week. It is the only case where GHL is faster.

## 6. Usability

Our team:
- Sovit is one part-time person. 01 says 6 to 8 weeks to be a confident GHL operator, and that estimate assumes full attention [assumption]. Spending that on GHL competes with building sales and the two claims that decide the pilot.
- The build team already ships Next.js and Supabase. Path B is a familiar stack. GHL is a second tool with its own quirks: 40 incidents in 90 days, deliverability complaints, snapshot pushes that may overwrite edits [community/reddit, via 01].
- Per-restaurant onboarding gets 5 extra steps (number, A2P, sending domain, consent fields, Google connect). Approval is 24 to 72 hours, up to 7 business days [community/reddit, via 01], which sits on the critical path of every go-live.
- Fit 1 and 3 on one internal sub-account are easy: one pipeline, one form, one inbox.

End client (restaurant owner):
- A busy independent owner runs a kitchen. They will not log into a second tool with a different look. 01 says the mobile app inbox is the only realistic surface for non-technical owners and plans on done-for-you setup.
- They already use the TF dashboard (menu, KDS). Anything they need from Engage and Reputation should show there. That is the 30 hours in section 5 and it is required on both paths.

## 7. White-label angle

- **Does it make sense for TF? No. Keep GHL invisible.**
- Price test: the Branded Client Portal is $49 per sub-account, about 20% of the $249 price. The white-label mobile app is $497 a month per agency (also with Apple $99 a year and Google $25) [ghl-pricing-page, community, via 01]. Neither fits a $12.85 cost base.
- SaaS mode (reselling GHL as a product) needs Agency Pro and a US entity with Stripe first, per 01. TF does not sell a CRM. It sells ordering with delivery and a visible payment split. Selling "a branded GHL" would dilute the two claims.
- What restaurants do see: TF Reputation and TF Engage as pages in the TF dashboard, emails from the restaurant's own domain, SMS from a number registered to the restaurant. Watch for leaks: "LeadConnector" in the default app and some server-side documents [ghl-docs, community, via 01]. Never give the owner a GHL login.
- GHL's reseller terms bar sending customers to HighLevel for support and comparing our product to HighLevel [ghl-docs, via 01]. Fine for an invisible tool.
- **Packaging most likely to convert:** no separate price. Put review requests and win-back inside the $249 as line items of TF Reputation and TF Engage, and say so on the pitch after the two claims. Why: the loyalty and marketing-automation objection is what stalls deals, an add-on price invites price comparison against 13 competitors, and the decided price has no $99 founding tier to trade. Revisit an add-on only after two paying restaurants ask for more.

## 8. Verdict for this line

**Use GHL for part: TF's own sales pipeline and onboarding/support (one internal sub-account, no SMS channel, invisible). Do not use GHL as the restaurant-facing engagement layer for now. Finish TF Reputation first on the existing stack, Engage later.**

Even the small part is conditional: buy it only if the spine ($297 Unlimited) is bought for the other lines. TF alone does not justify it.

Three biggest reasons:
1. **Cost.** The GHL layer is $34 per restaurant at 10 clients and $22 at 50, against $10 and $8 for finishing the modules. It is more than the whole existing $12.85 cost to serve. At N=1 it is $166.
2. **No build saving, extra risk.** Both paths are about 220 to 230 hours. GHL adds a second guest database, an opt-out return channel that is a TCPA exposure if it slips, two SMS numbers per restaurant, and does not close loyalty (checkout stays in Supabase).
3. **Wrong timing.** The first 2 to 3 pilots are won on delivery built in and a visible payment split, not on campaigns. Sovit is part-time, and Stripe Connect from India (section 4) is the bigger threat to the pitch than any missing engagement module.

The one thing that would change the call: two of the first three NYC prospects refuse to sign without automated review requests and win-back at launch, and the spine is already bought. Then run those pilots on A-lite (about 70 hours, GHL invisible, guests pushed by script) for 90 days, and decide on the full build from real usage.

## Questions for the teardown agent / live-account check

1. Does bring-your-own Twilio work inside a GHL sub-account? If yes, one number and one A2P campaign per restaurant could serve both transactional and marketing, which removes about $2 a month and a duplicate number. Cells dependent: Path A add-ons [assumption].
2. Are inbound-webhook triggers, tag-added triggers and custom-object triggers premium ($0.01)? Are marketplace-app or PIT API webhooks (contact opt-out, inbound message events) billed? Cell dependent: premium executions, $0 to $9 per restaurant.
3. Can sub-accounts be created and snapshots pushed by API on Unlimited ("basic API access"), or is that Agency Pro ("advanced API")? Cell dependent: provisioning automation, 24 hours.
4. Is there any loyalty, points or stamp-card feature or marketplace app? 01 did not cover it. Cell dependent: section 3 loyalty gap.
5. Is there a native review request plus negative-feedback flow, and does it avoid review gating? Cell dependent: workflow 10.
6. Wallet minimum and auto-recharge defaults per sub-account. A floor per restaurant would change the usage row.
7. Does a restaurant with an EIN and site register its own A2P brand under a sub-account we create, and what happens for restaurants with no EIN? Cells dependent: A2P fees, onboarding time.
8. Snapshot push behaviour on an already-customised sub-account (overwrite or skip). Cell dependent: labour per restaurant.
9. Can the Google Business Profile connect be done by us on the restaurant's behalf, and does Reviews AI reply need the restaurant's consent? Cell dependent: workflows 9 and 10.
