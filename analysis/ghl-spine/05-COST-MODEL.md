# 05 Cost model: all three lines on one GHL spine

Checked 28 Sep 2026. GHL prices come from `01-GHL-TEARDOWN.md` (public docs, no live account). Volumes and labour come from the base cases in `02`, `03` and `04`, with the red team's corrections from `07` applied. The numbers are calculated by `cost_model.py`, not written by hand. The full grid is in `05-cost-model.csv`: 4 plan options, 5 client counts and 3 lines.

## How to read it

- **N** is the number of paying clients in each line at the same time: N Leasify clients, N RevLabs clients and N TF restaurants.
- **Cost per client** is the GHL plan share plus everything else the line pays to serve that client each month. Margin % is against the line's price.
- **Architecture modelled** is the one in `00-VERDICT.md`:
  - One agency account.
  - Leasify: one sub-account (a separate client workspace) per client, plus HomeEasy.
  - RevLabs: one sub-account per Growth or Full-system client, plus Illinois calling, the Texas email lane and the test sandbox.
  - The $29 Track B site gets no sub-account.
  - TF gets no sub-account, because TF does not use GHL for now.
- **Plan share** is split by number of sub-accounts, so the line with more sub-accounts pays more of the plan.

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
| Leasify | $695.88 (-40%) | $379.03 (24%) | $353.80 (29%) | $344.97 (31%) | $340.46 (32%) |
| RevLabs | $232.66 (-275%) | $32.01 (48%) | $22.74 (63%) | $20.07 (68%) | $18.83 (70%) |
| TF | $14.85 (94%) | $14.85 (94%) | $14.85 (94%) | $14.85 (94%) | $14.85 (94%) |
| **All three, margin/month** | $-133 (-16%) | $3,841 (47%) | $10,465 (52%) | $21,505 (53%) | $43,586 (54%) |

#### Agency Pro $497 + US entity

| Line | N=1 | N=10 | N=25 | N=50 | N=100 |
|---|---|---|---|---|---|
| Leasify | $791.56 (-59%) | $394.82 (21%) | $360.69 (28%) | $348.53 (30%) | $342.28 (31%) |
| RevLabs | $395.32 (-538%) | $42.06 (32%) | $26.19 (58%) | $21.68 (65%) | $19.60 (68%) |
| TF | $14.85 (94%) | $14.85 (94%) | $14.85 (94%) | $14.85 (94%) | $14.85 (94%) |
| **All three, margin/month** | $-392 (-48%) | $3,583 (44%) | $10,207 (50%) | $21,247 (52%) | $43,327 (53%) |

#### 3 agencies x Unlimited $891

| Line | N=1 | N=10 | N=25 | N=50 | N=100 |
|---|---|---|---|---|---|
| Leasify | $915.88 (-84%) | $415.33 (17%) | $369.64 (26%) | $353.16 (29%) | $344.63 (31%) |
| RevLabs | $606.66 (-878%) | $55.11 (11%) | $30.66 (50%) | $23.76 (62%) | $20.60 (67%) |
| TF | $14.85 (94%) | $14.85 (94%) | $14.85 (94%) | $14.85 (94%) | $14.85 (94%) |
| **All three, margin/month** | $-727 (-90%) | $3,247 (40%) | $9,871 (49%) | $20,911 (52%) | $42,992 (53%) |

Starter shows "not possible" because the architecture needs at least 5 sub-accounts once there is 1 client per line, and Starter allows 3. **Starter is right only until HomeEasy's build starts.** Before that, RevLabs Illinois, RevLabs Texas and the sandbox fit in 3 slots.

## What the numbers say

- **Unlimited $297 is the plan.** It wins at every client count. Agency Pro costs $258/month more once the US entity it needs is counted, and buys nothing we use (see `06`). Three agency accounts cost $594/month more.
- **The plan fee stops mattering fast.** At N=10 the plan share is about $20 per Leasify client and $10 per RevLabs client. Usage, labour and build amortisation drive cost, not GHL's subscription.
- **Leasify is where the risk sits.**
  - At 1,000 leads and 20 SMS segments per lead, each client costs about $340 to $380 a month.
  - That is 24 to 32% margin at $499, and that is **before** the people who hand off tours and chase applications.
  - SMS is about 87% of Leasify usage, and the same texts cost the same on any platform.
  - Fix, decided in `00`: the $499 tier covers up to 500 new leads a month. At 500 leads the cost is about $250 at N=10, so margin is about 50% before service labour. Above 500, bill $35 per extra 100 leads (cost about $26), or move the client to the $999 tier.
- **RevLabs stays healthy.** The mix is 60% Track B at $29 (no GHL cost), 30% Growth at $99 and 10% Full system at $149 a month care. Margin is 48% at N=10 and 68% at N=50.
- **TF carries no GHL cost.** If restaurants were put on GHL as TF Engage/Reputation (`04` Path A), cost per restaurant would rise from $14.85 to about $48 at N=10.
- **Each line must pass on its own, and early months are lopsided.** The first line to start carries nearly all of the $297 (`07`, error 19). On its own, the plan is covered by 2 Leasify clients or 4 RevLabs Growth clients. TF does not pass alone, which is one reason TF stays off GHL.
- **N=1 losses are build and setup costs, not GHL.** Leasify at N=1 carries the whole $200/month build amortisation and $50 shared infrastructure. RevLabs at N=1 carries its internal sub-accounts against $62 of mixed revenue.

## Assumptions (all [assumption] unless tagged)

| Input | Value | Source |
|---|---|---|
| Plan fees | Starter $97 (3 sub-accounts), Unlimited $297, Agency Pro $497 | [ghl-pricing-page, via 01] |
| US entity running cost (Agency Pro option only) | $100/yr registered agent + about $50/mo bookkeeping and FEMA filings | [stripe-docs, via 01] + [assumption] |
| SMS delivered | $0.0115 per segment ($0.00747 + $0.004 carrier) | [ghl-docs, via 01] + shared assumption |
| Email | $0.675 per 1,000 | [ghl-docs, via 01] |
| Local number | $1.15/mo | [ghl-docs, via 01] |
| A2P campaign | $1.50 (low volume mixed) to $10 (standard) per month per texting business | [ghl-docs, via 01] |
| Labour | $8/hour (range $5 to $12), plus 0.5 hour a month per client sub-account for the compliance audit | shared assumption, `07` |
| Leasify client, excl. plan | usage $264.55 (20 SMS segments per lead, `07` correction of `02`'s 12) + A2P and Workflow Pro $25.33 + labour $44 + infra ($50/N + $2) + build ($200/N) | `02`, `07` |
| RevLabs Track B, excl. plan | $8.14 (no sub-account) | `03` |
| RevLabs Growth, excl. plan | $26.19 | `03` + audit |
| RevLabs Full system care, excl. plan | $49.22 against $149/month; the $999 build is a one-off (about $687 margin) and is left out of the monthly figures | `03` + audit, price set in `00` |
| RevLabs client mix | 60% Track B, 30% Growth, 10% Full | [assumption] |
| TF per restaurant | $12.85 cost to serve + $2 A2P, no GHL | `03-CONTEXT`, `04` |
| Internal sub-accounts | RevLabs Illinois calling $25/mo, RevLabs Texas email $3, sandbox $0, HomeEasy $0 (billed to HomeEasy) | [assumption] |
| Excluded | Leasify service delivery labour (tours, calls, applications, AI review), TF ordering labour, founder sales time, AI Employee bundles (pay-per-use is cheaper at our volumes, `02`) | |

## What would move these numbers most

1. **Leasify SMS per lead.** Each extra segment per lead adds $11.50 per 1,000 leads. HomeEasy's first 2 weeks give the real number. Re-run this script with it.
2. **Leasify service labour.** At 20 hours a month and $8 an hour it is $160 per client (`07`). That is why the lead cap sits at 500, not 1,000.
3. **A2P campaign type.** Standard campaigns at $10 against low-volume mixed at $1.50, on 50 or more sub-accounts, is a difference of about $425/month.
