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
