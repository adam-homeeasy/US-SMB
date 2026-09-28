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


