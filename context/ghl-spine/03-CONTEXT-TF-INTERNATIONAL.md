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
