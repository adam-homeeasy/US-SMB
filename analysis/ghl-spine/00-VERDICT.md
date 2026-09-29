# 00 Verdict: GHL as the spine

28 Sep 2026. Built from `01` to `08` in this folder. The GHL facts come from public docs only, because no live account was used. Five open points are settled by the 30-minute live check in `08`, and each one is named below where it could change a call.

## The call

- **Buy GHL, but narrowly and late.** Use it as the messaging and follow-up layer for RevLabs and Leasify. Keep it out of TF for now. Our own databases stay the system of record everywhere.
- **Plan:** Starter $97 now, for RevLabs Illinois calling, the RevLabs Texas email lane and the test sandbox. **Upgrade to Unlimited $297** the day HomeEasy's build starts or the first RevLabs Growth client signs. **Switch to annual ($2,970)** at 10 paying clients on GHL. Never buy Agency Pro while GHL stays invisible.
- **One agency account**, owned by MSM, with a neutral login domain. Each client sub-account sends under the client's own brand. Move Leasify to its own agency account at 10 paying clients or at the first compliance warning, to split the blast radius.
- **White-label: no, for now.** No SaaS mode, no "RevLabs platform" or "Leasify platform", no white-label app. Keep GHL invisible and sell done-for-you, because the buyers want outcomes, not logins, and two founders can't run a help desk (`06`). Payments are **no longer the blocker**: SaaS mode now takes Marketplace payment apps, not only Stripe (`01`, correction of 29 Sep). If one of those apps onboards MSM, SaaS mode is possible without a US entity.
- **Start a US entity now** (Stripe Atlas, Delaware LLC, with an Indian CA). This is not for GHL, and a GHL payment route does not replace it. TF's Stripe Connect plan with restaurants as merchant of record looks blocked from an Indian Stripe account [stripe-docs, via 01]. The same entity gives MSM an EIN for its own texting brand and a US card for the GHL wallet.

## Leasify: use GHL for part

- **GHL does:** one sub-account per client (clients don't log in), inbox, texts and email, tour calendar, reminders at 24 h, 2 h and 15 min, no-show rebooking, qualification-tier pipeline, reactivation sequences.
- **Postgres and Python keep:** matching, vouchers, price floors, Lift Score, alerts logic, daily and weekly reports, commissions, and every lead record. No custom objects at launch.
- **Amy Scott stays where she runs today.** Test GHL Conversation AI side by side on 50 HomeEasy leads only if the live check shows it can write fields, call our matching API and hand off to a human. No outbound AI voice.
- **Texts go out under each client's own A2P brand.** Listing-site leads get email or a call first, and a text only after they reply or consent, until counsel says otherwise.
- **Pricing fix:** the $499 tier covers up to 500 new leads a month, with $35 per extra 100 or a move to $999. At 1,000 leads and a realistic 20 texts per lead, $499 earns about 24 to 32% before service labour (`05`). This is a fair-use cap, not a price rise.
- **Order:** HomeEasy first, as a 100-hour MVP. The first paid client comes only after 2 weeks of HomeEasy beat today's response time and no-show rate.

## RevLabs: use GHL for part

- **GHL does:**
  - Our own prospecting, already settled: Illinois hand-dial only, and Texas in a sub-account with no phone number.
  - One sub-account per Growth $99, Automation or Full-system client, from the first signing.
- **GHL stays out of:** the $29 Track B site (static on Netlify or Cloudflare, no sub-account, keeps a 72% margin), Track A, Track C.
- **Full system price:** $999 setup, then **$149 a month system care** from month 2. The $100 credit is one-off, and usage after it is billed at cost plus 20%. $149 holds about 60 to 67% margin on a $49 run cost. At $99 the margin falls to about 40 to 50% once the credit is gone.
- **Missed-call text back is off** until a lawyer clears text to inbound missed callers, because it conflicts with the locked "text only after a spoken request" rule. Sell "missed-call alert and callback" meanwhile. Texas clients get email-only automations.
- **Compliance is soft in GHL**, so it runs on config plus an audit. Recording is off per number, the dialer and voicemail drop are never used, and every SMS step sits behind a consent-field check. Each sub-account gets audited monthly. **If the live check shows the dialer and voicemail drop can't be disabled per sub-account or role, client delivery moves off GHL.**

## TF International: don't use GHL for now

- NYC sales run on a sheet plus email until 30 Nov and 10 or more live prospects. Sovit's hours go to the first pilot and to Stripe Connect.
- Finish TF Reputation on the existing stack, then Engage. A GHL layer would cost about $48 per restaurant at 10 restaurants against $25 for our own modules, and would add a second guest database and an opt-out sync risk (`04`).
- **What would change it:** 2 of the first 3 NYC prospects refuse to sign without review requests and win-back at launch. Then run those pilots on a light, invisible GHL setup (about 70 hours) for 90 days.

## Money

- **Plan share stops mattering fast.** At 10 clients per line it is about $20 per Leasify client and $10 per RevLabs client. Texting volume and labour are the real costs (`05`).
- **Each line passes on its own.** 2 Leasify clients, or 4 RevLabs Growth clients, cover the $297. TF alone does not.
- Monthly margin across both GHL lines plus TF, at 10 clients each: about $3,800 (47%). At 50 each: about $21,500 (53%). Those figures come before Leasify service labour.

## Stop rules (from `07`)

Stop GHL for a line if any of these happens:
- The dialer and recording lock-offs fail the live check.
- A text goes out without logged consent twice in 90 days.
- There is any carrier or A2P suspension.
- HomeEasy's median first response is over 5 minutes after 30 days on GHL.
- An opt-out takes more than 24 hours to sync to Postgres, twice.
- By day 60, the GHL owner can't provision a compliant sub-account in under 3 hours.

## Needs Adam now

1. Run the 30-minute live check in `08` (day 0).
2. Name one GHL owner from the India team by day 3, at 15 to 20 hours a week.
3. Start the US entity with a CA, and brief a US telecom lawyer on the four questions in `08`.
