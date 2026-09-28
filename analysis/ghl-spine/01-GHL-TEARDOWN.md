# 01 GHL teardown: shared fact base

Checked: 28 Sep 2026. Method: public sources only (pricing page, HighLevel help centre, API docs, Stripe help, Twilio help, community). **No live GHL account was used.** Nothing here is `[live-account]`.

Tag key: `[ghl-pricing-page]` gohighlevel.com/pricing. `[ghl-docs]` help.gohighlevel.com. `[marketplace]` marketplace.gohighlevel.com API docs. `[stripe-docs]` support.stripe.com. `[twilio/tcr-docs]`. `[community/reddit]` blogs, reseller sites, review sites, ideas board snippets. This is the weakest tag: many of these sites sell GHL services. `[assumption]` from memory or inference, unverified.

Glossary (first use): **Agency account** is our top-level GHL account. **Sub-account** (also "location") is a separate client workspace inside the agency. **Snapshot** is a template of a sub-account setup (workflows, funnels, forms) that can be loaded into other sub-accounts. **SaaS mode** is GHL's feature for reselling GHL under your own brand with automatic billing and sub-account creation. **LC Phone / LC Email** are GHL's built-in phone/SMS and email services (LC = LeadConnector, an older brand name of GHL). **A2P 10DLC** is the US carrier registration needed to send business texts from normal 10-digit numbers. **Wallet** is prepaid credit that usage is charged against.

---

## Summary: the 12 facts that matter most

1. **Plans.** Starter $97/mo (3 sub-accounts), Unlimited $297/mo (unlimited sub-accounts), Agency Pro $497/mo (unlimited sub-accounts plus SaaS mode). Annual is 10x monthly ($970, $2,970, $4,970). Checked 28 Sep 2026. `[ghl-pricing-page]` https://www.gohighlevel.com/pricing
2. **Unlimited sub-accounts really cost $0 each at plan level**, but most extras are billed per sub-account per month (AI Employee $50 or $97, Branded Client Portal $49, WhatsApp $10, SEO tool $79, and so on) plus usage. `[ghl-pricing-page]` `[ghl-docs]`
3. **SaaS mode needs Agency Pro ($497).** Rebilling usage with a markup also needs Agency Pro. Unlimited ($297) can rebill usage at cost with no markup. `[ghl-pricing-page]` `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000002095-rebilling-reselling-and-wallets-explained
4. **Stripe is the blocker for MSM Global.** SaaS mode V1 needs the agency's own Stripe account. Stripe India is invite-only for new accounts, no self-signup. Newer SaaS V2 also allows NMI, Authorize.net and Square, but not Razorpay. So an Indian entity cannot count on SaaS mode. Fallback: a US entity (Delaware LLC via Stripe Atlas, $500 plus $100/yr) with a US Stripe account. `[stripe-docs]` `[ghl-docs]` See Direct answers.
5. **Usage prices (LC Phone).** SMS $0.00747 per segment, out and in. MMS $0.022 out. Calls $0.0166/min out, $0.01165/min in. Local number $1.15/mo. Carrier fees are extra. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/48001223556-phone-system-pricing-billing-guide
6. **Email.** LC Email $0.675 per 1,000. Email validation $2.50 per 1,000. Bring-your-own SMTP/Mailgun is supported. `[ghl-docs]`
7. **A2P 10DLC.** One-time $22.50 (sole proprietor, low volume) or $64 (high volume standard). Monthly campaign $2 (sole prop), $1.50 (low volume mixed), $10 (standard). Each business needs its own brand and campaign, so 50 sub-accounts texting means 50 registrations and roughly $75 to $500 a month in campaign fees. Unregistered US traffic is blocked by carriers since 1 Feb 2025. `[ghl-docs]` `[community/reddit]`
8. **AI Employee** bundle: $97/mo per sub-account (unlimited Conversation AI and Voice AI, fair use) or $50/mo (Growth: 1,000 Conversation AI responses and 100 Voice AI minutes). Or pay per use with no monthly fee. Phone charges are separate. `[ghl-pricing-page]` `[ghl-docs]`
9. **Premium workflow actions** cost $0.01 per execution (webhook, custom code, Workflow AI actions, formatters, Google Sheets, and similar). Workflow Pro tiers $10, $25, $50/mo bundle 10k, 30k, 65k executions. `[ghl-docs]` `[community/reddit]` for the exact action list.
10. **Custom objects** exist on all plans: max 10 objects per sub-account, 300K records per object, workflows can trigger on object Created and Changed. Full CRUD in API v2. `[ghl-docs]` `[community/reddit]`
11. **Three brands under one agency account is not cleanly supported.** One white-label login domain per agency. The community view (ideas board) is that separate trade names need separate agency accounts. Sub-account level branding (sending domain, links domain, sites domain) works. Needs a live check. `[ghl-docs]` `[community/reddit]`
12. **Exit is painful.** Contacts export to CSV only. Workflows only travel inside snapshots (GHL to GHL). Conversations and custom objects need API or third-party tools. After termination GHL may delete data after 90 days. GHL sites cannot serve a root `llms.txt` (community, ideas board). `[ghl-docs]` `[community/reddit]`

---

## Part 1: plans and money

### 1.1 Plan table (checked 28 Sep 2026)

Source for whole table: `[ghl-pricing-page]` https://www.gohighlevel.com/pricing

| Plan | Monthly | Annual | Sub-accounts | Users | Notes |
|---|---|---|---|---|---|
| Starter | $97 | $970 | 3 | Unlimited | All core features, unlimited contacts, 24/7 support |
| Unlimited | $297 | $2,970 | Unlimited | Unlimited | Adds unlimited sub-accounts, rebill phone/email with no markup, basic API access |
| Agency Pro | $497 | $4,970 | Unlimited | Unlimited | Adds SaaS mode, auto sub-account creation, rebill with markup, user/agent reporting, advanced API |
| Enterprise | Custom | Custom | Custom | Custom | Success manager, premium support, HIPAA included, white-label app listed as included |

- 14-day free trial, month-to-month, no long-term contract. `[ghl-pricing-page]`
- Annual is about 2 months free (10x monthly). `[ghl-pricing-page]`
- No newer tier than Enterprise appeared on the page. `[ghl-pricing-page]`
- Custom objects were Pro-only, opened to all tiers in Oct 2025. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000006631-custom-objects-in-all-plans-higher-limit
- Page says AI and telecom are usage-billed. `[ghl-pricing-page]`
- Starter cap of 3 sub-accounts is the only sub-account limit. Users are unlimited on all tiers. `[ghl-pricing-page]`
- One mismatch to check: the page lists the white-label mobile app as an add-on ($497) and also under Enterprise. `[ghl-pricing-page]` Ask GHL or check billing.

### 1.2 Add-ons and fixed fees (checked 28 Sep 2026)

Sources: `[ghl-pricing-page]` and `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000001156-highlevel-pricing-guide

| Add-on | Price | Scope |
|---|---|---|
| AI Employee Growth | $50/mo | per enabled sub-account |
| AI Employee Unlimited | $97/mo | per enabled sub-account |
| Branded Client Portal app | $49/mo | per sub-account |
| White-label mobile app | $497/mo or $1,491/quarter | per agency |
| Dedicated email IP | $59/mo | per IP or domain |
| WhatsApp integration | $10/mo | per sub-account |
| SEO tool (Search Atlas) | $79/mo | per sub-account |
| Premium prospecting tool | $29/mo | per sub-account |
| Online listings management | $30/mo, $150/6 mo, $300/yr | per sub-account |
| WordPress hosting | $10/mo (1 site), $220/mo (25 sites), $497/mo (unlimited) | per agency |
| Workflow Pro | $10, $25, $50/mo | per sub-account (see 1.5) |
| HIPAA compliance | $297/mo | account-wide |
| Premium support | $500/mo or $5,000/yr | agency |
| Domain purchase | market rates | per domain |
| Certification programme | $97 | one-off |

Extra costs for the white-label app: Apple Developer $99/yr and Google Play $25 one-off. `[community/reddit]`

### 1.3 SaaS mode

- **Plan needed:** Agency Pro $497. `[ghl-pricing-page]`
- **What it does:** you define paid plans in the **SaaS configurator** (name, price, which product features, usage markups). A buyer signs up on a checkout page, pays, and a sub-account is created automatically from a snapshot. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000008015-getting-started-with-the-saas-configurator
- A plan must include at least one product feature. `[ghl-docs]`
- **Two versions.** V1: Stripe only, set at agency level, agency's own Stripe is the billing system of record. V2: providers connected to an "Agency Sub-Account": Stripe, NMI, Authorize.net, Square. Set per sub-account. PayPal, Affirm/Klarna, wallets and **Razorpay are not supported in SaaS mode**. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000006075-supported-payment-providers-methods-by-product-area-what-works-where- and SaaS FAQ https://help.gohighlevel.com/support/solutions/articles/155000002129-saas-mode-faqs
- V2 announced 23 Jan 2025. Users on the ideas board report V2 gaps: no scheduled future charges, no pro-rata, no billing-interval change on existing subscriptions. `[community/reddit]` `[ghl-docs]` for the interval point.
- A sub-account can be in only one SaaS mode at a time. `[ghl-docs]`
- Turning SaaS off deletes the wallet and the balance is emailed to the agency. `[ghl-docs]`
- Indian clients need a billing address in Stripe (RBI rule). `[ghl-docs]` This is about Indian customers, not our US ones.
- Auto-recharge does not support 3DS-only cards. `[ghl-docs]`
- Currency must match between plan and category and cannot change once subscriptions exist. `[ghl-docs]`

### 1.4 Rebilling of usage (phone, email, AI)

Source: https://help.gohighlevel.com/support/solutions/articles/155000002095-rebilling-reselling-and-wallets-explained `[ghl-docs]`

- HighLevel always charges the **agency wallet** for sub-account usage. `[ghl-docs]`
- Three modes:
  - No rebilling: agency pays everything.
  - Rebill without markup: needs Unlimited ($297) or Pro. Client pays the same amount HighLevel charges us.
  - Rebill with markup: **Agency Pro ($497) only**.
- Wallets are prepaid. A card charge tops up the wallet, usage is deducted, auto-recharge fires below a set threshold. `[ghl-docs]`
- Rebilling runs through the **Agency Stripe**. `[ghl-docs]`
- Default markup on the configurator is 1.05x (5%) to cover Stripe fees. `[community/reddit]`
- Markup applies to LC services: phone, email, AI, WhatsApp. Exact per-service markup limits not found. `[ghl-docs]`

### 1.5 Usage prices (checked 28 Sep 2026)

**LC Phone** source: `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/48001223556-phone-system-pricing-billing-guide. GHL says pricing matches Twilio. It shows a 10% discount on the $0.0083 list SMS rate.

| Item | Price |
|---|---|
| SMS out, US/Canada | $0.00747 per segment |
| SMS in, US/Canada | $0.00747 per segment |
| MMS out | $0.0220 per segment |
| MMS in, local | $0.0165 per segment |
| MMS in, toll-free | $0.0200 per segment |
| Call out, US/Canada | $0.0166 per minute |
| Call in, US/Canada | $0.01165 per minute |
| Call in, toll-free | $0.0198 per minute |
| Local number | $1.15 per month |
| Toll-free number | $2.15 per month |
| Call recording | $0.0025 per minute, plus storage $0.0005 per minute per month (`[ghl-docs]` phone number options article) |
| Call transcription | $0.024 per minute |
| Answering machine detection | $0.0075 per call |
| Carrier fees | Variable, passed through per delivered segment |

- Segments: one text over 160 characters (70 with emoji) becomes several segments. `[assumption]` standard SMS rule.
- Delivered outbound cost with carrier fees is quoted at $0.011 to $0.0125 per segment. `[community/reddit]` Not in GHL docs. Treat as a range to verify.
- Calls round up to whole minutes. `[community/reddit]`

**LC Email and validation** `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000001156-highlevel-pricing-guide

| Item | Price |
|---|---|
| LC Email | $0.675 per 1,000 emails |
| Email validation | $2.50 per 1,000 |
| Dedicated IP | $59/mo |

- LC Email runs on Mailgun. `[community/reddit]`
- Bring-your-own SMTP (Gmail, SendGrid, Mailgun, SES) is supported at agency and sub-account level. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000007765-how-to-add-your-own-email-service-smtp-
- Bring-your-own Twilio: was a supported option in the past. Current status not confirmed in this run. `[assumption]` from memory, unverified.

**WhatsApp:** now priced per delivered message from 1 Oct 2026, first 1,000 service messages per number per month free. Meta rates plus $10/mo add-on. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000001428-whatsapp-pricing-billing-and-rebilling-guide (via search summary).

### 1.6 A2P 10DLC (US business texting)

Source for fees: `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000005200-a2p-10dlc-messaging-fees-registration-monthly-and-carrier-costs. GHL states all A2P fees are pass-through with no HighLevel markup.

| Item | Fee |
|---|---|
| Brand + vetting, sole proprietor | $22.50 one-time |
| Brand + vetting, low volume standard | $22.50 one-time |
| Brand + vetting, high volume standard | $64.00 one-time |
| Extra campaign under same brand | $15.00 vetting |
| Campaign monthly, sole proprietor | $2.00 |
| Campaign monthly, low volume mixed | $1.50 |
| Campaign monthly, standard | $10.00 |
| Campaign monthly, charity | $3.00 |
| Campaign monthly, emergency services | $5.00 |

- Twilio direct for comparison: $15 campaign vetting, $4 brand fee for sole prop and low volume standard, registration up to 5 business days. `[twilio/tcr-docs]` https://help.twilio.com/articles/11587910480155-A2P-10DLC-Campaign-Vetting-FAQ
- **Who registers:** each sending business needs its own brand and campaign. Community sources say registrations are per sub-account and cannot be shared. GHL's own article did not state this. `[community/reddit]` Live check owed.
- Brand needs legal name, EIN and a live website matching the brand. Sole proprietors (no EIN) can register with an OTP check. `[ghl-docs]` `[community/reddit]`
- Approval: typically 24 to 72 hours, up to about 7 business days if a brand goes to manual vetting. `[community/reddit]`
- Common rejections: no visible opt-in language, missing privacy policy, website that does not match the brand. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000007572-a2p-campaign-rejections-required-fixes-vetting-errors
- **Unregistered traffic:** since 1 Feb 2025 US carriers block essentially all unregistered A2P texts, sometimes silently. `[community/reddit]`
- Whether a non-US business (MSM, no EIN) can register for its own texting: GHL article is silent. `[ghl-docs]` Assumption: needs a US EIN or the sole-proprietor route with a US-recognised ID. Unverified.

### 1.7 AI prices (checked 28 Sep 2026)

Primary source: https://help.gohighlevel.com/support/solutions/articles/155000006652-ai-product-pricing-update (page modified 28 Sep 2026) `[ghl-docs]`. Employee plan article: https://help.gohighlevel.com/support/solutions/articles/155000003906-ai-employee-access-rebilling-and-reselling

| Product | Price | Tag |
|---|---|---|
| AI Employee Growth | $50/mo per enabled sub-account. Includes 1,000 Conversation AI responses and 100 Voice AI minutes a month | `[ghl-docs]` |
| AI Employee Unlimited | $97/mo per enabled sub-account. Unlimited Conversation AI, Voice AI "subject to fair use" | `[ghl-docs]` |
| Pay-per-use | No monthly fee | `[ghl-docs]` |
| Voice AI engine | $0.045 per minute (since 20 May 2026, was $0.06) | `[ghl-docs]` |
| Voice AI text-to-speech | $0.015/min (OpenAI or Cartesia), $0.035/min (ElevenLabs V2.5), $0.170/min (ElevenLabs V3) | `[ghl-docs]` |
| Voice AI speech-to-speech | Gemini 3.1 Flash Live $0.10/min, OpenAI GPT Realtime $0.20/min | `[ghl-docs]` |
| Voice AI typical floor | $0.06/min (engine + basic TTS), before phone charges | derived from the two rows above |
| Conversation AI | Token-based. GPT-5 $1.25 in / $10 out per 1M tokens. GPT-4.1 Mini $0.40 / $1.60 per 1M. Short SMS reply about $0.002 to $0.005 | `[ghl-docs]` rates, `[community/reddit]` per-reply estimate |
| Content AI | $0.063 per image, $0.0945 per 1,000 words | `[ghl-docs]` |
| Reviews AI | $0.01 per AI review reply | `[ghl-docs]` |
| Workflow AI Builder | Included, no extra charge | `[ghl-docs]` |
| Workflow AI actions (Summarize, Decision Maker, Intent Detection) | Premium action, $0.01 per execution | `[community/reddit]` |
| Agent Studio | Pay-per-use by model tokens. Not included in AI Employee plans | `[ghl-docs]` |

- "Phone System charges are separate." Voice AI calls pay both AI and phone rates. `[ghl-docs]`
- The old "$0.13 per minute" bundled Voice AI rate still appears on many pages. Treat as historical. `[community/reddit]`
- Fair-use meaning of "unlimited": roughly 50,000 Voice AI minutes and 200,000 messages a month before GHL contacts you. `[community/reddit]` Not in GHL docs.

### 1.8 Premium workflow actions and triggers

- Premium features: **$0.01 per execution**, per action run, not per contact. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000001156-highlevel-pricing-guide
- **Workflow Pro** (volume plan): Starter $10/mo with 10,000 executions and $0.008 overage. Growth $25/mo, 30,000, $0.006. Scale $50/mo, 65,000, $0.004. `[ghl-docs]`
- Premium list as reported (GHL's article did not list them): Custom Webhook (outbound, waits for response), Inbound Webhook trigger, Custom Code, Google Sheets, Slack, Copy Contact between sub-accounts, array functions, formatters, Workflow AI actions. ChatGPT action has its own pricing. `[community/reddit]` https://hlgrowthpartner.com/post/gohighlevel-premium-workflow-actions-costs-2026
- Three premium steps on one contact is three executions. `[community/reddit]`
- Premium features can be enabled per sub-account and rebilled. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000005678-how-to-enable-and-rebill-premium-features-for-workflows
- Whether custom-object triggers or plain SMS/email/wait actions are premium: not stated. Standard actions are free. `[assumption]`

### 1.9 Easy-to-miss costs

- A2P monthly campaign fee per sub-account, forever, even for quiet accounts. `[ghl-docs]`
- Wallet minimum and auto-recharge balances per sub-account (defaults not found). `[ghl-docs]`
- Call recording storage ($0.0005 per minute per month). `[ghl-docs]`
- Number porting and international sending fees: not found in public docs this run. `[assumption]` check billing guide.
- Per-sub-account add-ons scale linearly: 50 accounts on AI Employee Unlimited is $4,850/mo. `[ghl-pricing-page]` arithmetic.
- Storage: custom object data counts toward account storage quota. `[ghl-docs]`

### 1.10 Quick unit cost sketch (inputs are assumptions)

Illustration for a Track B style client, all `[assumption]` volumes, prices from tables above:

| Item | Volume | Monthly cost |
|---|---|---|
| Local number | 1 | $1.15 |
| A2P sole-prop campaign | 1 | $2.00 |
| 100 SMS segments in and out | 100 | $0.75 plus carrier fees (about $0.30 to $0.50 assumed) |
| 500 emails | 500 | $0.34 |
| Total, no AI | | about $4.50 to $5 |
| With AI Employee Growth | | plus $50 |

So a $29/mo client with no AI costs about $5 in usage plus a share of the $297 plan. Add AI Employee and it does not work. Full model belongs in the cost-model file.

---

## Part 2: features (docs only, none tested live)

For every area below: **Tested live: no, docs only.**

### 2.1 Contacts, custom fields, tags, smart lists, custom objects

- **What it does:** contact records with custom fields, tags, smart lists (saved filters). Custom objects are our own record types (e.g. Property, Unit, Restaurant). Associations link records. `[ghl-docs]`
- **Limits:** 10 custom objects per sub-account on all plans, 300K records per object, up to 10 unique association labels between any two objects, all field types supported. Only sub-account admins can create or edit objects. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000006631-custom-objects-in-all-plans-higher-limit
- **Association limit:** an ideas-board post calls a 1,000 association limit "unusable for real customers". `[community/reddit]` https://help.gohighlevel.com/support/solutions/articles/155000005346-association-limits (exact limit not read).
- **Workflows on custom objects:** triggers "Record Created" and "Record Changed", actions to create, update and clear fields on the object or associated records. No explicit delete trigger or per-field change trigger documented. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000004389-using-custom-objects-in-workflow-actions-and-triggers
- **Opportunity link:** associations between opportunities, companies and custom objects are supported. `[ghl-docs]`
- **Missing:** no relational queries or joins, no unit-level matching logic, no SQL. Property/unit/voucher matching stays in Postgres. `[assumption]`
- **Replaces:** a simple CRM, spreadsheets. Not a database for Leasify's 111 properties and 215 units with rule-based matching.

### 2.2 Opportunities and pipelines

- **What it does:** Kanban pipelines, stages, stage-change triggers, value, reporting. `[ghl-docs]` general knowledge
- **Detail not verified this run.** Multiple pipelines per sub-account and stage automation are standard. `[assumption]` from memory, unverified.
- **Missing:** custom scoring formulas like the Leasify Lift Score (needs custom fields plus workflow or external calc). `[assumption]`
- **Replaces:** Excel trackers for deal stages.

### 2.3 Conversations inbox

- **What it does:** one inbox for SMS, email, calls, Facebook/Instagram, WhatsApp, live chat widget, Google Business Profile. `[ghl-docs]`
- **Google Business Profile:** Google's Business Messages closed in July 2024. GHL now connects WhatsApp and text numbers to a GBP page, and syncs new Google reviews into the inbox. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000006471-add-messaging-social-channels-to-your-google-business-profile-gbp-
- **WhatsApp:** $10/mo per sub-account plus per-message Meta pricing from 1 Oct 2026. Templates needed outside the 24-hour window. Usernames from June 2026 may hide phone numbers. `[ghl-docs]`
- **Missing:** listing-site lead intake (Zillow, Apartments.com) is not native. Needs email parsing or webhook. `[assumption]`
- **Replaces:** shared inbox tools, Slack alerts partly.

### 2.4 Phone system and compliance controls

- **Numbers and settings:** per-number config: call recording, call connect, whisper message, ring timeouts, voicemail. Path: sub-account Settings, Phone System, Phone Numbers, Edit Configuration. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/48001229976-overview-of-phone-number-configuration-options
- **Call recording default:** not on by default, enabled per number. Toggle is number-level only. Users are asking for per-call control and none is documented. `[community/reddit]` https://ideas.gohighlevel.com/lcphonesystem/p/recording-enable-and-disaple-option-on-dialer-or-on-conversation
- **Recording disclosure:** optional announcement before connect when Call Connect is on, $0.00084 per 100 characters of text-to-speech. GHL says a disclaimer is often legally required. `[ghl-docs]`
- **How to keep recording off:** leave the number's recording toggle off in each sub-account. There is no documented agency-wide lock. Bake it into the snapshot and audit each sub-account. `[ghl-docs]` `[assumption]` on the lock gap.
- **Dialer:** built-in phone dialer (manual, contact search, transfers, scripts, IVR keypad). `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000005807-the-phone-dialer-overview
- **Power dialer and voicemail drop:** power dialer with call queue, dispositions, local presence, and voicemail drop exist. Enabled in Settings, Phone System. `[community/reddit]` GHL's overview article does not mention them. Whether a user permission or setting can hide or disable them per sub-account: **not found, live check owed**.
- **RevLabs rule fit:** no autodialer, no recorded voicemail drop, no recording. These features exist but are opt-in. Compliance depends on us keeping them off, not on GHL blocking them. `[assumption]`
- **DND (do not disturb):** global or per-channel, inbound or outbound, settable by workflow action. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/48001214849-how-to-use-do-not-disturb-dnd-
- **Quiet hours:** Drip Mode for bulk actions has business-hours and cutoff windows. In normal workflows, build an If/Else on the contact's local time before each SMS, else wait until 8 am. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000006472-new-drip-mode-architecture-for-bulk-actions `[community/reddit]` for the If/Else pattern.
- **Consent tracking:** no dedicated consent ledger found. Use custom fields and tags (e.g. `sms_consent_words`, `sms_consent_date`) and gate workflows on them. `[assumption]`
- **Missing:** a hard workflow-level block that refuses to send SMS without a consent flag. Must be built with If/Else branches. `[assumption]`
- **Replaces:** Twilio direct, a separate dialer. Does not replace DNC scrubbing (use our own list scrub). `[assumption]`

### 2.5 Workflows

- **What it does:** visual automation: triggers, actions, If/Else, waits, inbound and outbound webhooks, custom code (JavaScript), Workflow AI, and a natural-language builder. `[ghl-docs]`
- **Costs:** standard actions free, premium at $0.01 (see 1.8).
- **Limits:** execution and concurrency caps not found this run. `[assumption]` check.
- **Missing:** version control, tests, easy export outside snapshots.
- **Replaces:** Zapier/Make for simple flows, `lead_pulse_monitor.py` alerts partly (Slack action is premium).

### 2.6 Calendars

- **Not researched this run.** Round-robin, team calendars, reminders and no-show workflows are standard GHL. `[assumption]` from memory, unverified. Reminders at 24h, 2h, 15 min are workflow-driven.
- **Replaces:** Calendly, tour-booking spreadsheets.

### 2.7 Sites, funnels, forms

| Need | Finding | Tag |
|---|---|---|
| Page title, meta description | Editable per page | `[community/reddit]` |
| Custom meta tags | Per page, SEO Meta Data tab. Article does not mention JSON-LD or canonical | `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/48001073924-custom-meta-tags |
| Canonical | Set automatically, can be defined manually in page settings or header script | `[community/reddit]` |
| sitemap.xml | Auto-generated at yourdomain.com/sitemap.xml, plus blog sitemap | `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/48001182524-xml-sitemaps |
| robots.txt | Editable at domain level, announced as a feature | `[ghl-docs]` (feature alert), `[community/reddit]` |
| noindex | Toggle per page or meta tag | `[ghl-docs]` |
| Custom head code / JSON-LD | Custom code injection exists on pages. JSON-LD in head code is likely but not confirmed | `[community/reddit]` `[assumption]` |
| llms.txt | **Cannot upload a .txt to the domain root.** Feature request open on the ideas board | `[community/reddit]` https://ideas.gohighlevel.com/ad-reporting-and-attribution/p/adding-llmstxt-to-root-domain-websitecom-llmstxt (page returned 403, snippet only) |
| Pages at root/folders | No way to build pages under arbitrary folder paths | `[community/reddit]` |
| Page speed | No fixed score. Depends on JS load and edge caching. GHL shipped video/thumbnail speed fixes | `[community/reddit]` |
| Site audit | Built-in Site Audit tool with a health score | `[ghl-docs]` |

- **Verdict on the SEO gate:** title, description, sitemap, robots and noindex look fine. Schema depends on head code. **llms.txt fails** unless a workaround exists. Speed unknown. Must be tested with a real page.
- **Replaces:** Netlify/Cloudflare one-pagers for Track B, if the gate passes. **Risk:** hosting clients' sites on GHL ties every $29 site to the GHL account.

### 2.7b Custom domains

- Sites domain per sub-account (Sub-Account, Settings, Domains). Email sending domain per sub-account. API/branded links domain at agency and sub-account level. Client portal domain at sub-account level. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/155000002561-setting-up-whitelabel-domain-api-domain-email-sending-domain-sites-domain-client-portal-domain-

### 2.8 Payments

- **What it does:** invoices, order forms, subscriptions, payment links with Stripe and others. `[ghl-docs]` Providers: Stripe, Authorize.net, NMI, Square, PayPal for normal payments. Razorpay and PayPal are not supported in SaaS mode. `[ghl-docs]`
- **Text-to-pay:** not confirmed this run. `[assumption]` from memory, unverified.
- **Missing:** no delivery, no restaurant ordering, no Stripe Connect marketplace splits. Ordering and payments for TF stay in TF's own build.
- **Replaces:** simple invoice/payment-link tools.

### 2.9 Reputation

- **What it does:** review requests by SMS/email, review replies, Reviews AI ($0.01 per AI reply), Google reviews synced into the inbox. `[ghl-docs]`
- **Missing:** negative-feedback catch flow needs a workflow build. Not verified. `[assumption]`
- **Replaces:** TF Reputation module (planned). Real candidate.

### 2.10 Reporting and attribution

- **Not researched in depth.** Dashboards, call reports and ad reporting exist. Agency-level cross-account reporting for user/agent needs Agency Pro. `[ghl-pricing-page]` Detail `[assumption]`.
- **Replaces:** parts of the Excel weekly report. Founder daily deal report still needs custom work.

### 2.11 Snapshots

- **Copies:** workflows, funnels, calendars, forms, emails, triggers, custom fields, custom values, membership content, services, webinars, AI Studio projects. `[community/reddit]` https://help.gohighlevel.com/support/solutions/articles/48000982511-snapshots-overview
- **Does not copy:** contacts, appointments, conversations, reputation data, Stripe connections, integrations, lead-gen forms. `[community/reddit]`
- **Updates:** changes to the source do not flow automatically. You refresh the snapshot, then push to chosen sub-accounts and chosen assets inside your own agency. Outside agencies need a re-shared link. `[community/reddit]` `[ghl-docs]` version management https://help.gohighlevel.com/support/solutions/articles/155000006497-snapshot-version-management
- **Risk:** pushing over a customised sub-account can overwrite client edits. Check what "push" does to existing workflows. `[assumption]`

### 2.12 Users and permissions

- **Not verified in depth.** Roles (admin, user), per-feature permission toggles and limited-view are standard. Only location admins can export data and edit custom objects. `[ghl-docs]` for those two. Rest `[assumption]`.

### 2.13 Mobile app

- Default app is LeadConnector (free, in stores under that name). White-label app under your own name: $497/mo, needs your own Apple ($99/yr) and Google ($25) accounts. `[ghl-docs]` `[community/reddit]`
- One branded app per agency subscription appears to be the model. Not explicit. `[community/reddit]` live check owed.
- Branded Client Portal app: $49 per sub-account. `[ghl-pricing-page]`

### 2.14 API v2 and webhooks

- **Auth:** OAuth 2.0 authorization code flow for marketplace apps (access tokens expire daily, refresh needed). **Private Integration Tokens (PIT)**: scoped, static, no refresh, for our own server-to-server use. `[marketplace]` https://marketplace.gohighlevel.com/docs/Authorization/PrivateIntegrationsToken/
- **Rate limits:** 100 requests per 10 seconds (burst) and 200,000 per day, **per app per resource (location or agency)**. Each install gets its own budget. Headers: `X-RateLimit-Max`, `X-RateLimit-Remaining`, `X-RateLimit-Limit-Daily`, `X-RateLimit-Daily-Remaining`. `[marketplace]` https://marketplace.gohighlevel.com/docs/other/rate-limits/
- **PIT rate limits:** docs reference possible differences but the page gave no detail. `[marketplace]`
- **Objects exposed:** contacts, conversations, calendars, opportunities, payments, custom objects (CRUD on objects and records), and more. `[marketplace]` `[community/reddit]`
- **Webhooks:** 50+ events reported. Also inbound/outbound webhooks in workflows (premium, $0.01). `[community/reddit]` `[ghl-docs]`
- **Verdict for our stack:** Python and Supabase can read and write cleanly with a PIT per sub-account. 100 per 10 seconds is fine for our scale. Syncing 50 accounts of guest data is possible but is two databases to keep aligned. `[assumption]`

### 2.15 Data export

| Data | Export path | Tag |
|---|---|---|
| Contacts | CSV via Bulk Actions, admins only, no automation history | `[ghl-docs]` `[community/reddit]` |
| Opportunities | CSV import documented. Export not confirmed in docs. API works | `[ghl-docs]` |
| Conversations | Not in the UI as a file. Needs API or third-party tool | `[community/reddit]` |
| Custom objects | No UI export found. API v2 CRUD | `[assumption]` |
| Workflows | No standalone export. Only inside snapshots (GHL to GHL) | `[community/reddit]` |
| Funnels, sites | Snapshots only. No portable HTML export found | `[community/reddit]` |
| Phone numbers, A2P registrations, email domain settings | Stay in GHL | `[community/reddit]` |
| Sub-account transfer | Eligible sub-accounts can move between agencies with contacts, conversations, opportunities, sites, calendars. Integrations reconnect | `[community/reddit]` |

Source for the exit picture: https://www.seldonframe.com/guides/can-you-export-gohighlevel `[community/reddit]` (a competing vendor, treat as weakest).

- After termination GHL may permanently delete data after 90 days. `[ghl-docs]` https://www.gohighlevel.com/terms-of-service
- **Lost on exit:** workflow logic (must be rebuilt by hand), conversation history unless pulled by API, numbers and A2P registrations, sites unless rebuilt.

### 2.16 Integrations for property and other systems

- **AppFolio, Yardi, RealPage, Entrata:** no native GHL connector or marketplace app found in searches. AppFolio is not a direct Zapier app; people query its API via webhooks. `[community/reddit]` https://community.zapier.com/how-do-i-3/integrating-appfolio-with-gohighlevel-for-property-management-communication-52323 Plan: middleware (n8n, Make, Python) via API and webhooks. Live check: search the GHL App Marketplace.
- **Stripe:** yes for payments. **Google Business Profile:** yes (2.3). **WhatsApp:** yes (2.3).

---

## Part 3: white-label mechanics

### 3.1 How many brands per agency

- The agency has **one Whitelabel Domain** (login portal) set at Agency View, Settings, Company Settings, Whitelabel. Docs do not state whether more than one is allowed. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/48000982604-agency-company-settings-in-highlevel
- Community and the ideas board: the only way to brand different trade names under one legal entity is to buy **multiple agency accounts**. Requests for "multiple white labels per agency" are open. `[community/reddit]` https://ideas.gohighlevel.com/ad-reporting-and-attribution/p/multiple-white-labels-for-agencies (403, snippet only)
- **What can be branded per sub-account:** API/branded links domain, email sending domain, sites domain, client portal domain, WordPress domain. `[ghl-docs]`
- **Not per sub-account:** a separate login/whitelabel domain per client (docs do not say it exists). `[ghl-docs]`
- **Cost implication (`[assumption]` arithmetic):**
  - One agency, all three brands: Unlimited $297 (no SaaS) or Agency Pro $497.
  - Three separate agencies, each Pro: $1,491/mo. Each Unlimited: $891/mo.
  - Hybrid: one Pro agency for the brand that resells (RevLabs), Unlimited for done-for-you brands (Leasify, TF) where the tool is invisible: $794/mo.
- Live check owed: try adding a second whitelabel domain and check company settings.

### 3.2 What clients still see

- Logo and domain: login screen, app header, notification emails, some widgets and form footers can be branded. `[ghl-docs]`
- Cannot be fully white-labelled: mobile apps (no CSS), React pop-ups like payment modals, **PDF invoices and receipts generated server-side**, core builder UI. `[ghl-docs]` https://help.gohighlevel.com/support/solutions/articles/48000982604-agency-company-settings-in-highlevel
- No agency-wide favicon upload. Set per site, portal, membership area. `[ghl-docs]`
- "LeadConnector" name: shows in the default mobile app, app-store listing, LC Phone and LC Email service names, and possibly billing line items. `[community/reddit]` https://www.courseplatformsreview.com/blog/leadconnector/
- White-label mobile app removes LeadConnector from the app store listing. `[community/reddit]`
- Emails send from our sending domain, links from our API domain. `[community/reddit]`
- Live check owed: send a test SMS, email, invoice and portal login from a sandbox and note every mention of HighLevel or LeadConnector.

### 3.3 GHL reseller terms

Source: https://www.gohighlevel.com/terms-of-service `[ghl-docs]`

- You may not send your customers to HighLevel for support. You are fully liable to them and own dispute resolution.
- No soliciting existing HighLevel customers to cancel and buy your white-label version.
- No marketing that compares your white-label to HighLevel or claims yours is better or has more features.
- **Minimum advertised price (MAP):** you cannot advertise access to a package of 2 or more core features (funnels, CRM, email and so on) below HighLevel's standard price for a similar package. The price actually charged is not restricted, only the advertised price. Lifetime licences need written approval.
- HighLevel may suspend reselling "with or without notice". HighLevel owns usage data derived from the platform. Governing law: Texas.
- **Effect on us:** a $99 "RevLabs" tier that bundles CRM plus funnels plus email may hit the MAP rule if GHL's comparable plan is $97 or $297. Read the clause with a lawyer before advertising SaaS tier prices. `[assumption]` interpretation.

---

## Part 4: usability

Nothing was set up or timed. This is community only. `[community/reddit]`

- **Learning curve is complaint number one.** Over 140 of 651 G2 reviews mention it. Estimates: 1 to 3 weeks to feel comfortable, 6 to 8 weeks for confidence, up to 60 to 90 days by some reviewers. https://ciela.ai/blogs/is-gohighlevel-worth-it-2026-reddit
- **Non-technical business owner:** would struggle with the full builder. The mobile app (inbox, calendar, pipeline) is the realistic surface. Plan on done-for-you setup. `[assumption]`
- **India team running 50 sub-accounts:** needs snapshot discipline, a per-sub-account onboarding checklist (number, A2P, sending domain, consent fields, recording off), and one person who owns workflow builds. Estimate 6 to 8 weeks to a confident operator. `[assumption]` built on the community range.
- **Reliability:** StatusGator tracked 40 incidents in 90 days (19 major, 21 minor), median 12 minutes. Last officially acknowledged outage 22 May 2026. `[community/reddit]` https://statusgator.com/services/highlevel
- **Email deliverability:** frequent complaint. Shared sending pools plus sloppy agencies hurt reputation. Fix: own sending domain, SPF/DKIM/DMARC, 2 to 4 weeks warm-up, optional dedicated IP ($59). `[community/reddit]` https://julianmills.co.uk/why-is-my-highlevel-email-deliverability-so-bad/
- **Support:** mixed. Quality depends on the agent. Reviewers still rate it about 8.1 out of 10. Ratings are 4.5 to 4.7 out of 5 across G2, Capterra, Trustpilot. `[community/reddit]` Many review sites are affiliates.
- **Bugs:** Reddit reports inconsistent reliability across the wide feature set. `[community/reddit]`

---

## Direct answers (master prompt list)

### Q1. One agency account for three brands?

- **Public answer: probably not cleanly.** One white-label login domain per agency. Trade-name separation reportedly needs multiple agency accounts. `[ghl-docs]` `[community/reddit]`
- **What works in one agency:** sub-accounts per line, each with own sending domain, links domain, sites domain. The login URL and desktop app branding would be one brand only.
- **Cost:** see 3.1. Range $297 to $1,491/mo.
- **Needs live check:** second whitelabel domain, agency-level brand settings.

### Q2. SaaS mode and rebilling for an Indian company

- **What SaaS mode needs:** Agency Pro ($497) plus a Stripe account connected to the agency (V1), or a supported provider on an Agency Sub-Account (V2: Stripe, NMI, Authorize.net, Square). Razorpay unsupported. `[ghl-docs]`
- **Stripe India status:** "Stripe services are invite-only in India. Businesses from India are not able to sign up for a new Stripe account through our website." New businesses apply through Stripe's sales team. Stripe says it supports "a select number of businesses, with a focus on international expansion". No timeline given. `[stripe-docs]` https://support.stripe.com/questions/stripe-accounts-are-invite-only-in-india
- **Points in our favour:** our business sells services to US clients, which is international expansion. Export payments are supported for invited accounts (export limit up to 25 lakh INR per transaction for the preview). `[stripe-docs]` https://support.stripe.com/questions/india-faq
- **Recurring cards:** RBI e-mandate rules apply to India-issued cards. US clients paying with US cards are the export case. Stripe supports non-INR e-mandates only for specific currencies and international businesses. So a monthly subscription to US cards from an Indian Stripe account is a grey area to confirm with Stripe sales. `[stripe-docs]` `[assumption]` on the US-card reading.
- **Stripe Connect from India:** works only with limits. Direct charges without application fees. Separate charges and transfers unsupported. Cross-border destination charges generally prohibited. `[stripe-docs]` https://support.stripe.com/questions/stripe-india-support-for-marketplaces
  - **This matters beyond GHL:** TF's plan for Stripe Connect with each restaurant as merchant of record and platform fees looks blocked or crippled from an Indian platform account. Red team must check this.
- **Do we already have a Stripe account?** Context files mention Stripe payment links for RevLabs and Stripe Connect for TF, processor and entity not named. If MSM already holds an active Stripe India account, existing accounts stay operational. `[stripe-docs]` Confirm which entity.
- **US entity route:** Stripe Atlas forms a Delaware LLC or C-corp. Indian founders can use it. $500 fee (LRS-compliant, up to $250K a year per resident), then $100/yr registered agent. Indian ODI/FEMA compliance applies: Annual Performance Report by 31 Dec, Form FLA by 15 Jul, subsidiary structure for mixed founders. Timeline about 2 to 6 weeks to first Stripe payment including EIN and bank. `[stripe-docs]` https://support.stripe.com/questions/faq-for-indian-founders-using-stripe-atlas `[community/reddit]` for timeline. Get an Indian CA and US tax adviser.
- **Verdict, in order:**
  1. **Do not plan on SaaS mode with an Indian-entity Stripe account.** Approval is by invite, uncertain and untimed.
  2. **Best path if we want SaaS mode: a US entity with a US Stripe account (Atlas).** This also unlocks EIN for clients' A2P and Stripe Connect for TF.
  3. Optional: ask Stripe India sales for an invite in parallel, since it is free to ask.
  4. Non-Stripe V2 providers (Authorize.net, NMI, Square) normally require a US merchant account too. `[assumption]` from memory, unverified.
  5. **Fallback with no SaaS mode:** buy Unlimited ($297), keep GHL invisible, bill clients through our own invoicing, and fold usage into retainers (rebilling without markup still needs a card for wallets on Stripe, so budget the usage into price).
- **Deciding on white-label alone:** yes, this can decide it. Without a US Stripe account, no SaaS mode. Confidence: high on the Stripe status, medium on what invitation approval would look like.

### Q3. A2P 10DLC and phone compliance

- **Who registers:** each sending business needs its own brand and campaign under its own sub-account (EIN, website, opt-in proof). We do the paperwork, the client supplies the details. `[community/reddit]` `[ghl-docs]`
- **Cost:** $22.50 one-time low volume, $64 high volume, plus $1.50 to $10 monthly per campaign. 50 clients on standard campaigns is $500/mo in campaign fees alone. `[ghl-docs]`
- **Time:** 24 to 72 hours typical, up to about 7 business days if manual vetting. `[community/reddit]` Twilio says up to 5 business days. `[twilio/tcr-docs]`
- **Unregistered:** blocked. `[community/reddit]`
- **Our own texting from MSM (India):** unclear if MSM can register a brand without a US EIN. Live check. `[ghl-docs]` silent.
- **RevLabs rules:** no autodialer: leave power dialer off. No voicemail drop: leave off. No recording: number-level toggle off. Texas email-only: a workflow gate on state field (or a Texas tag) that blocks SMS and calls. Text only after a spoken request: a consent-flag custom field the rep sets, and an If/Else before every SMS. No native enforcement. `[assumption]`
- **TF rules:** email-first and no cold texts: use LC Email or own SMTP, keep SMS unregistered/unused until consent. Fine. `[assumption]`
- **Quiet hours and DND:** available. `[ghl-docs]`

### Q4. Data ownership and exit

- See 2.15. Contacts CSV yes. Workflows, conversations, custom objects, numbers: painful. No single portable export. `[community/reddit]`
- **Leaving at 50 clients:** re-register 50 A2P brands on a new platform, rebuild every workflow by hand, pull conversations by API, move numbers by port (fee unverified), rebuild sites. Estimate 2 to 4 hours per client at minimum. `[assumption]`
- **Mitigation:** keep Postgres as system of record, log every message and consent to our database through webhooks, keep workflow logic documented outside GHL.
- GHL deletes data 90 days after termination. `[ghl-docs]`

### Q5. GHL sites versus our own builds (SEO gate)

- **Per docs and community:** title, description, canonical, sitemap, robots.txt, noindex all available. Schema likely via head code. **llms.txt is not possible at root.** `[community/reddit]` `[ghl-docs]`
- **Speed:** unknown, needs a real test.
- **Not built or tested:** no sandbox page was built this run.
- **Provisional recommendation:** keep Track B one-pagers on Netlify/Cloudflare and embed GHL forms until a sandbox page passes `seo_gate.py`. `[assumption]` Live check owed.

### Q6. Custom objects and API v2: enough for Leasify and TF?

- **Leasify:** 10 objects, 300K records each, associations, create/change triggers, CRUD API. Enough to hold property and unit records. Not enough for rule-based matching (crime, transit, voucher caps, CHA payment standards, price floors). Matching stays in Python/Postgres, results pushed to GHL as fields. Postgres stays system of record. `[ghl-docs]` `[assumption]`
- **TF:** ordering, menus, orders and payments live in Supabase. Guest data would need two-way sync. GHL as engagement layer only (reviews, campaigns). `[assumption]`
- **API:** 100 requests per 10 seconds and 200,000 per day per location per app. Fine for 50 accounts. `[marketplace]`

### Q7. AI features and Amy Scott

- **Cost per sub-account:** $50 (Growth) or $97 (Unlimited) a month, or pay per use. Voice AI at least $0.06 per minute plus phone. `[ghl-docs]`
- **What they do live:** not tested. Conversation AI handles text channels, Voice AI phone conversations, Workflow AI builds workflows from prompts. `[ghl-docs]`
- **Could it replace Amy Scott?** Unknown. Amy Scott's platform is not stated in the context. Extracting budget, move-in date, credit, voucher status and matching to units needs unit data lookups, so it needs a custom webhook to our matching service (premium action, $0.01 per call). `[assumption]`
- **Human in the loop:** use Conversation AI to qualify and book, hand to a human via workflow on Hot tier. `[assumption]`
- **Voice AI compliance:** FCC treats AI-generated voices as artificial or prerecorded under TCPA, so prior express written consent is needed for AI calls to consumers. State AI-disclosure laws exist in CA, TX, FL. `[community/reddit]` https://www.fcc.gov/document/fcc-confirms-tcpa-applies-ai-technologies-generate-human-voices. **Do not use outbound Voice AI in RevLabs.** Inbound only, if at all.

### Q8. Where GHL is clearly the wrong tool

- **Leasify:** rule-based unit matching, voucher checks, price floors, Lift Score, commission tracking. GHL can trigger and message, not compute.
- **RevLabs $29/mo Track B client:** per-sub-account A2P fees, AI add-ons and a shared share of the plan eat the margin if every client gets a sub-account. Static site plus form embeds is cheaper.
- **TF:** ordering, delivery, payments, guest database. GHL is only a candidate for reviews and campaigns, and only if it does not double the cost base at $12.85 per restaurant to serve. A2P alone is $2 to $10 a month per restaurant if they text.

---

## Live-account checks still owed (about 30 minutes)

Run in a sandbox sub-account named `ZZ-TEST-Spine-Analysis`. No purchases, no real messages.

1. Billing page: confirm plan prices, wallet default recharge amount, any tier newer than Enterprise. (2 min)
2. Agency Settings, Company, Whitelabel: can a second whitelabel domain be added? Any brand or "profile" concept? (3 min)
3. Agency Settings, Phone/Email: does agency-level setting exist to force call recording off? Read only. (3 min)
4. Sub-account Settings, Phone System: is recording off on a new number by default? Is there any toggle for power dialer or voicemail drop? Is there a user permission to hide the dialer? (5 min)
5. Trust Center / A2P screen: does it accept a non-US business or one without EIN? Which registrations are per sub-account? Read only, do not submit. (4 min)
6. Payments, Integrations: which Stripe countries and account types does the connect flow accept? Check SaaS configurator screen for "Stripe" versus "Agency Sub-Account" wording. (3 min)
7. Custom objects: create a test object, add fields, association, and build a workflow on Record Created and Changed. Check whether triggers appear premium. (5 min)
8. Sites: create one page, check title, description, canonical, custom head code with JSON-LD, robots.txt editor, and whether a root `llms.txt` can be served. Run PageSpeed on the URL. (8 min, longest)
9. Export: Contacts Bulk Actions, Export. Look for conversation and custom object export options. (2 min)
10. Marketplace search: AppFolio, Yardi, RealPage, Entrata. (2 min)
11. Send one test email and view an invoice preview to list every "HighLevel" or "LeadConnector" mention. (3 min)
12. Ask Stripe: do we hold an active Stripe India account for MSM? Which entity owns the existing payment links? (1 min, outside GHL)

---

Source URLs are in the action log: `/home/user/US-SMB/analysis/ghl-spine/teardown-action-log.md`.
