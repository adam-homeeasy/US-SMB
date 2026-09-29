# 06 White-label plan

Decision: **keep GHL invisible and sell done-for-you wherever GHL is used (Leasify and RevLabs; TF stays off GHL for now). No SaaS mode, no branded "platform" product, no white-label mobile app.** One agency account carries both lines, and TF later if it joins. The plan below covers how that looks to clients, how money moves, and how we leave if we need to.

Facts are from `01-GHL-TEARDOWN.md` (public docs, checked 28 Sep 2026, no live account). Items marked "live check" are in `08`.

## Why not resell GHL as our own product

- **SaaS mode is not open to MSM yet, but the route may exist.** SaaS mode (GHL's resell-under-your-brand feature with automatic billing) needs Agency Pro ($497) plus a payment provider that supports recurring and off-session charges. Stripe India is invite-only [stripe-docs, via 01]. Since mid-2026, SaaS mode also accepts custom payment providers from the App Marketplace, which may give an Indian company a way in. No specific app has been confirmed to onboard MSM, and Razorpay is explicitly excluded [ghl-docs, via 01 correction]. **This is no longer the deciding reason.** The next three reasons are, and they hold even if payments are solved.
- **The buyers want outcomes, not software.** A plumber, a small property manager and a restaurant owner are all buying "someone handles my follow-up". A login dilutes that pitch and adds a support desk we cannot staff from two founders plus one part-time person.
- **Reseller terms add risk.** As a SaaS reseller we own all support and disputes. The minimum advertised price clause may catch a cheap tier that bundles CRM, funnels and email. GHL can suspend reselling "with or without notice" [ghl-docs, via 01].
- **It costs more.** Agency Pro plus a US entity is about $258/month more than Unlimited, and buys nothing we use (`05`).

## Brand structure

| Layer | Setup | Brand shown |
|---|---|---|
| Agency account | One, owned by MSM Global Consulting Pvt Ltd, Unlimited plan | Nobody outside the team sees it |
| Agency white-label login domain | One, set to a neutral MSM domain such as `app.<msm-domain>` | MSM Global, only seen by our team and the rare client who logs in |
| Leasify sub-accounts | One per client, plus HomeEasy | The client's own property or locator brand on texts and emails. Leasify appears only in reports |
| RevLabs internal sub-accounts | Illinois calling, Texas email lane (no phone number) | RevLabs, from separate warmed sending domains |
| RevLabs client sub-accounts | One per Growth, Automation or Full-system client | The client's own business name, number and sending domain |
| TF | No sub-account for now. Sales run on a sheet plus email (`00`) | n/a |

Why one agency account and not three (or two):
- One white-label login domain per agency is a real limit [ghl-docs, community, via 01], but it only matters if clients log in, and in a done-for-you model they don't.
- Three agencies cost $891 against $297 and triple the snapshot, audit and billing work (`05`).
- Per sub-account branding (sending domain, links domain, sites domain) already covers everything a client or their customer sees [ghl-docs, via 01].

## Domains

- **Sending domain per sub-account:** always the client's own domain or a subdomain of it, for example `mail.clientname.com`, with SPF, DKIM and DMARC set by us. For RevLabs internal use, one warmed domain for Illinois and a separate warmed domain for the Texas lane, as already locked.
- **RevLabs cold email goes through our own SMTP (bring-your-own), not the shared LC Email pool.** One cold-email complaint on the shared pool can hurt deliverability for Leasify's client sends (`07`).
- **Links domain per sub-account:** the same client domain, so tracked links do not show a GHL domain.
- **Sites domain:** not used for Track B sites, which stay as static builds on Netlify or Cloudflare with an embedded GHL form only for Growth-and-up clients (`03`). Leasify and TF do not host sites on GHL.

## Desktop and mobile apps

- **Desktop:** clients get no login by default. If a Leasify or RevLabs client insists, they get a restricted user in their own sub-account (inbox, calendar and pipeline only, no settings, workflows, phone system or billing). The role limits need a live check.
- **Mobile:** the default LeadConnector app, for the few clients who want to answer their inbox on the phone. It shows the LeadConnector name [community, via 01]. Say "we run it for you", never "there's no software".
- **White-label mobile app ($497/month):** not now. Revisit only when 20 or more clients use the app every week.

## How money moves (rebilling)

- **GHL bills us.** The plan fee and all usage (SMS, calls, email, AI, A2P fees, premium actions) come out of our agency wallet on our card [ghl-docs, via 01].
- **We bill clients on our own invoices, never GHL invoices.** GHL's PDF invoices cannot be fully white-labelled [ghl-docs, via 01], and GHL's usage rebilling runs through an agency Stripe we don't have.
- **Usage is priced into the retainer, with a cap:**
  - Leasify $499 includes up to 500 new leads a month. Above that, bill $35 per extra 100 leads (cost about $26), or move the client to the $999 tier (`05`). This is a fair-use cap, not a price rise, so the "don't raise the entry price" rule holds.
  - RevLabs Growth $99 includes normal usage: base cost is about $26 before plan share (`05`).
  - RevLabs Full system: $999 setup, then $149 a month system care from month 2 (`00`). The $100 communication credit is one-off and tracked per sub-account by us. Once it is used, usage is invoiced monthly at cost plus 20%, the simplest rule a client will accept without arguing over pennies.
  - TF: no restaurant usage on GHL.
- **Weekly usage check per sub-account.** GHL cannot hard-cap a sub-account's spend without rebilling [assumption, 03]. One saved report, 10 minutes a week.
- **Which processor charges clients:** the context mentions RevLabs payment links but does not name the processor. Keep using whatever is live. This plan does not depend on it.

## What the client sees and does not see

Sees:
- Texts from their own local number and brand, and emails from their own domain.
- Our reports: the Leasify weekly report and the RevLabs monthly report, built from our data, not GHL dashboards.
- If they log in: the MSM-branded portal limited to their inbox, calendar and pipeline.

Does not see:
- The words HighLevel or GoHighLevel, other clients, our workflows, prices of usage, or the dialer.
- Still visible in some places (live check to list them all): "LeadConnector" in the default mobile app and app-store listing, and possibly in payment pop-ups [community, ghl-docs, via 01].

## How we leave GHL later if we need to

Build the exit in from day one. It costs little now and caps the lock-in.

1. **System of record stays ours.** Leasify leads, tours, deals, Lift Score, matching and commissions live in Postgres. TF guests and orders stay in Supabase. GHL holds working copies only (`02`, `04`).
2. **Log every message and consent event out of GHL.** A webhook on every inbound and outbound message, opt-out and consent change writes to our Postgres. That gives us the conversation history and a TCPA consent record GHL cannot hold back.
3. **Workflows written down outside GHL.** Every snapshot workflow gets a one-page spec in the repo (trigger, steps, waits, filters). Rebuilding is then typing, not archaeology. Workflows only export inside snapshots, GHL to GHL [ghl-docs, via 01].
4. **Sites never on GHL.** Track B stays static, so "client keeps everything" stays true.
5. **Numbers and A2P belong to the client's brand.** Numbers can be ported out. A2P brand and campaign would be registered again on the new provider. Budget about a week of carrier vetting per client.
6. **Quarterly export drill.** Export contacts CSV from each sub-account and check the Postgres message log is complete. 30 minutes a quarter.

Estimated exit cost at 50 clients with these in place: about 1 to 2 hours per client (re-register A2P, port the number, rebuild from specs), against 2 to 4 hours without them (`01` Q4).

## When to revisit white-label

Revisit SaaS mode only when all three are true:
1. A US entity with a US Stripe account exists. It is being formed now for TF's Stripe Connect (see `00`).
2. At least 15 RevLabs clients have asked for self-serve access.
3. A lawyer has read GHL's minimum advertised price clause against the tiers we'd advertise.

Until then, keep GHL invisible.
