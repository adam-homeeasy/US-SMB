# 05 Cost model: all three lines on one GHL spine

Checked 28 Sep 2026. GHL prices come from `01-GHL-TEARDOWN.md` (public docs, no live account). Volumes and labour come from the base cases in `02`, `03` and `04`. The numbers are calculated by `cost_model.py`, not written by hand. The full grid is in `05-cost-model.csv`: 4 plan options, 5 client counts and 3 lines.

## How to read it

- **N** is the number of paying clients in each line at the same time: N Leasify clients, N RevLabs clients and N TF restaurants.
- **Cost per client** is the GHL plan share plus everything else the line pays to serve that client each month. Margin % is against the line's price.
- **Architecture modelled** is the one in `00-VERDICT.md`:
  - One agency account.
  - One sub-account (a separate client workspace) per Leasify client, plus HomeEasy.
  - One sub-account per RevLabs Growth or Full-system client, plus 2 internal sub-accounts (Illinois calling, Texas email).
  - One internal TF sales sub-account.
  - No sub-account for the $29 Track B site or for TF restaurants.
- **Plan share** is split by number of sub-accounts, so a line with more sub-accounts pays more of the plan.

## Results: cost per client per month (margin %)

#### Starter $97

| Line | N=1 | N=10 | N=25 | N=50 | N=100 |
|---|---|---|---|---|---|
| Leasify | not possible | not possible | not possible | not possible | not possible |
| RevLabs | not possible | not possible | not possible | not possible | not possible |
| TF | not possible | not possible | not possible | not possible | not possible |
| **All three, margin/month** | not possible | not possible | not possible | not possible | not possible |

#### Unlimited $297

| Line | N=1 | N=10 | N=25 | N=50 | N=100 |
|---|---|---|---|---|---|
| Leasify | $599.88 (-20%) | $283.03 (43%) | $257.80 (48%) | $248.97 (50%) | $244.46 (51%) |
| RevLabs | $176.06 (-209%) | $28.76 (50%) | $20.84 (63%) | $18.39 (68%) | $17.21 (70%) |
| TF | $72.85 (71%) | $16.80 (93%) | $15.27 (94%) | $14.99 (94%) | $14.90 (94%) |
| **All three, margin/month** | $-44 (-5%) | $4,764 (59%) | $12,777 (63%) | $26,132 (65%) | $52,843 (66%) |

#### Agency Pro $497 + US entity

| Line | N=1 | N=10 | N=25 | N=50 | N=100 |
|---|---|---|---|---|---|
| Leasify | $695.56 (-39%) | $298.82 (40%) | $264.69 (47%) | $252.53 (49%) | $246.28 (51%) |
| RevLabs | $290.88 (-410%) | $37.37 (34%) | $24.02 (58%) | $19.92 (65%) | $17.96 (68%) |
| TF | $120.69 (52%) | $18.24 (93%) | $15.54 (94%) | $15.06 (94%) | $14.92 (94%) |
| **All three, margin/month** | $-302 (-38%) | $4,506 (56%) | $12,519 (62%) | $25,874 (64%) | $52,584 (65%) |

#### 3 agencies x Unlimited $891

| Line | N=1 | N=10 | N=25 | N=50 | N=100 |
|---|---|---|---|---|---|
| Leasify | $819.88 (-64%) | $319.33 (36%) | $273.64 (45%) | $257.16 (48%) | $248.63 (50%) |
| RevLabs | $440.06 (-672%) | $48.56 (15%) | $28.15 (51%) | $21.92 (62%) | $18.94 (67%) |
| TF | $182.85 (27%) | $20.10 (92%) | $15.88 (94%) | $15.15 (94%) | $14.94 (94%) |
| **All three, margin/month** | $-638 (-79%) | $4,170 (52%) | $12,183 (61%) | $25,538 (63%) | $52,249 (65%) |

Starter shows "not possible" because the architecture needs at least 5 sub-accounts once there is 1 client per line, and Starter allows 3. **Starter is right only before the first paying GHL client:** RevLabs Illinois, RevLabs Texas and TF sales fit in 3 slots.

## What the numbers say

- **Unlimited $297 is the plan.** It wins at every client count. Agency Pro costs $258/month more once the US entity it needs is included, and buys nothing we use (see `06`). Three agency accounts cost $594/month more for branding that done-for-you clients never see.
- **The plan fee stops mattering fast.** At N=10 the plan share is under $20 per client in every line. Usage and labour drive cost, not GHL's subscription.
- **Leasify is the cost driver.** At base volume (1,000 leads and 12,000 SMS segments a month), each client costs about $245 to $285, so margin is 43 to 51% at $499 before service delivery labour. SMS is about 80% of usage, and the same texts cost the same on any platform. A heavy client (3,000 leads) loses money at $499 (`02`, high case), so the $499 tier needs a fair-use lead cap of about 1,000 leads a month.
- **RevLabs margin depends on the mix.** The model assumes 60% Track B at $29, 30% Growth at $99 and 10% Full system at $99 ongoing. Track B carries no GHL cost at all. If every $29 client got a sub-account, the $29 margin would fall from 72% to 31% at N=10 (`03`).
- **TF stays cheap because restaurants are not on GHL.** The line carries only its internal sub-account share. If restaurants were put on GHL as TF Engage/Reputation (`04` Path A), cost per restaurant would rise from $14.85 to $48.51 at N=10 and $36.75 at N=50.
- **Break-even on the spine:** once Starter is outgrown, 4 RevLabs Growth clients or 2 Leasify clients cover the full $297.
- **N=1 losses are build and setup costs, not GHL.** Leasify at N=1 carries the whole $200/month build amortisation and $50 shared infrastructure. RevLabs at N=1 carries both internal sub-accounts' usage ($28) against $57 of mixed revenue.

## Assumptions (all [assumption] unless tagged)

| Input | Value | Source |
|---|---|---|
| Plan fees | Starter $97 (3 sub-accounts), Unlimited $297, Agency Pro $497 | [ghl-pricing-page, via 01] |
| US entity running cost (Agency Pro option only) | $100/yr registered agent + about $50/mo bookkeeping and FEMA filings | [stripe-docs, via 01] + [assumption] |
| SMS delivered | $0.0115 per segment ($0.00747 + $0.004 carrier) | [ghl-docs, via 01] + shared assumption |
| Email | $0.675 per 1,000 | [ghl-docs, via 01] |
| Local number | $1.15/mo | [ghl-docs, via 01] |
| A2P campaign | $1.50 (low volume mixed) to $10 (standard) per month per texting business | [ghl-docs, via 01] |
| Labour | $8/hour (range $5 to $12) | shared assumption |
| Leasify client, excl. plan | usage $172.55 + A2P and Workflow Pro $25.33 + labour $40 + infra ($50/N + $2) + build ($200/N) | `02` section 5 |
| RevLabs Track B, excl. plan | $8.14 (no sub-account) | `03` section 5 |
| RevLabs Growth, excl. plan | $22.19 | `03` section 5 |
| RevLabs Full system ongoing, excl. plan | $45.22, priced at $99/month ongoing; the $999 build is a one-off (about $687 margin) and is left out of the monthly figures | `03` section 5 |
| RevLabs client mix | 60% Track B, 30% Growth, 10% Full | [assumption] |
| TF per restaurant | $12.85 cost to serve + $2 A2P, no GHL usage | `03-CONTEXT`, `04` |
| Internal sub-accounts | RevLabs Illinois calling $25/mo, RevLabs Texas email $3, TF sales $3, HomeEasy $0 (billed to HomeEasy) | [assumption] |
| Excluded | Leasify service delivery labour (tours, calls, applications), TF ordering labour, founder sales time, AI Employee bundles (pay-per-use is cheaper at our volumes, `02`) | |

## What would move these numbers most

1. **Leasify SMS per lead.** At 12 segments per lead, SMS is $138 of the $172 in Leasify usage. At 6 segments per lead, the Leasify margin rises about 14 points.
2. **A2P campaign type.** Standard campaigns at $10 against low-volume mixed at $1.50, on 50+ sub-accounts, is a difference of about $425/month.
3. **Labour rate.** Moving from $8 to $12 an hour adds about $20 per Leasify client and $6 per RevLabs Growth client.
