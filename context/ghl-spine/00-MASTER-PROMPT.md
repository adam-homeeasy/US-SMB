# Master prompt: GHL as the spine, three business lines

Paste everything below the line into the cloud session as the first message. The four context files (01 to 04) sit next to this one. Commit this whole folder into the repo under `/context/ghl-spine/` (about 32 KB, no other folders needed), or paste `99-ALL-IN-ONE-PASTE.md` instead, which has everything in one message.

---

## Who I am and what this session is

I'm Adam. I run three business lines under MSM Global Consulting Pvt Ltd (an Indian company, team in Bhubaneswar, selling mostly into the US):

1. **Leasify**: residential leasing conversion ops (US, Chicago and Texas metros).
2. **RevLabs US SMB**: productized websites, SEO, CRM and follow-up automation for US local service businesses.
3. **Table Foundry International (TF Direct)**: direct-ordering platform for independent US restaurants, NYC first.

Full context for each line is in:

- `context/ghl-spine/01-CONTEXT-LEASIFY.md`
- `context/ghl-spine/02-CONTEXT-REVLABS-US-SMB.md`
- `context/ghl-spine/03-CONTEXT-TF-INTERNATIONAL.md`
- `context/ghl-spine/04-GHL-TEARDOWN-PROTOCOL.md`

Read all four before doing anything. Treat what they call "locked" as locked. Don't re-debate it.

**The question:** should GoHighLevel (GHL) be the shared operating spine (CRM, pipelines, conversations, calendars, workflows, phone/SMS/email, sites/funnels, payments, reputation, AI agents) across all three lines, and should we white-label it and resell it as our own product? I want a full teardown of GHL judged on three things only: **cost, usability for our team and our clients, and how well its workflows match what each line actually needs to do.** Not a generic GHL review.

## How to run it: multi-agent, one master strategist on top

Use a master strategist that orchestrates five sub-agents. Each line agent works only on its own line and reports back in the fixed format below. The master is the only one who compares lines and makes the final call.

| Agent | Job | Uses the browser? |
|---|---|---|
| **Master strategist** | Plans the run, briefs the agents, merges findings, red-teams them, writes the verdict | No |
| **GHL teardown agent** | Builds the shared fact base on GHL: plans, real prices, usage costs, features, limits, white-label mechanics, API. Follows `04-GHL-TEARDOWN-PROTOCOL.md` | **Yes, the only one** |
| **Leasify agent** | Maps Leasify's workflows onto GHL, finds the gaps, costs it | No, asks the teardown agent to check things |
| **RevLabs agent** | Same for RevLabs US SMB | No, same |
| **TF agent** | Same for TF International | No, same |
| **Red-team agent** | After the line reports land, attacks them: lock-in, compliance, hidden costs, "what breaks at 100 clients" | No |

Rules for the agents:

- Only the teardown agent drives the browser, so there's one clean session in GHL. Line agents send it specific questions ("can a workflow trigger on a custom object field change?", "what does LC Phone charge per outbound SMS segment?") and it answers from the live account or the official docs, with a screenshot or link as proof.
- Every fact about GHL gets a source tag: `[live-account]`, `[ghl-docs]`, `[ghl-pricing-page]`, `[marketplace]`, `[community/reddit]` (weakest, say so), or `[assumption]`. Prices must carry the date checked. Nothing from memory gets passed off as current.
- Line agents don't invent numbers about our business. If a number isn't in the context file, they mark it `[assumption]` and give the range they used.
- Run the line agents in parallel once the teardown agent has the first fact base (plans, pricing, feature list). Don't wait for the full teardown to finish before starting them.

## The steps

1. **Plan gate (the only stop before the work).** Show me a one-screen plan: agents, what each produces, which model each uses, rough time. If you have a model-selector or routing skill, run it and show the routing card. Then wait for me to say **"go"**. After "go", don't stop to ask permission again. Run through to the end.
2. **Browser gate.** When the teardown agent is ready for the live account, tell me. I'll log in to GHL myself in the browser. You never type my password, never touch 2FA, never save credentials. Wait until I say "logged in". While waiting, work from the public pricing page, docs and marketplace.
3. **Teardown** (per protocol 04).
4. **Line fit analysis**, one per line, in the format below.
5. **Cost model** across all three lines at 1, 10, 25, 50 and 100 paying clients each, per GHL plan option.
6. **Red team.**
7. **Master verdict.**

## What each line agent must produce

One markdown file per line, same headings so the master can compare:

1. **What this line needs the spine to do**: the 10 to 20 core workflows, written as plain steps (trigger, action, owner, outcome). Take them from the context file, don't make up new ones.
2. **Workflow fit table**: each workflow, one row. Columns: GHL feature that covers it, fit (Native / Native with workaround / Needs integration / Not possible), how it would be built, effort in hours, monthly cost it drives, risk.
3. **What GHL replaces** in our current or planned stack, and what it can't replace.
4. **What we'd still have to build or buy** around it (integrations, middleware like Zapier/Make/n8n, custom code, our own database).
5. **Cost per client per month** at 1, 10, 50, 100 clients, broken into: GHL plan share, usage (phone, SMS, email, AI), add-ons, integrations, our labour. Compare it to what the line charges.
6. **Usability**: for our team (who builds, who operates daily, learning curve) and for the end client (would a busy owner actually log in and use this, or does it need to be fully done-for-them?).
7. **White-label angle**: does reselling GHL as our own branded product make sense for this line's buyer, at this line's price? If yes, at what price and packaging.
8. **Verdict for this line**: one of *Use GHL as the spine* / *Use GHL for part (say which part)* / *Don't use GHL*. With the three biggest reasons and the one thing that would change the call.

## What the master strategist must produce

- **`00-VERDICT.md`**, one page, bullets: the recommendation for each line, for the shared spine, and for white-label. Decided, not a menu of options. Include the plan tier to buy and when to upgrade.
- **`01-GHL-TEARDOWN.md`**: the shared fact base (feature by feature, cost by cost, limits, lock-in, API), all source-tagged.
- **`02-LEASIFY-FIT.md`**, **`03-REVLABS-FIT.md`**, **`04-TF-FIT.md`**: the line reports.
- **`05-COST-MODEL.md`** plus `05-cost-model.csv`: all three lines on one sheet, per plan option, 1 to 100 clients each, with every assumption listed.
- **`06-WHITE-LABEL-PLAN.md`**: brand structure (one agency account with sub-accounts per line, or separate agency accounts per brand), domains, desktop and mobile app branding, how rebilling works, what we charge, what the client sees and doesn't see, and how we leave GHL later if we need to.
- **`07-RISKS-AND-RED-TEAM.md`**: every risk with likelihood, impact, and the mitigation.
- **`08-SETUP-PLAN-30-60-90.md`**: if the verdict is yes to any part, the build order: which snapshot/sub-account first, which workflows first, what gets tested on a real client first.

Write all outputs to `/analysis/ghl-spine/` in the repo. Markdown only, no .docx.

## Things the analysis must answer directly (don't skip these)

- Can **one GHL agency account** carry all three brands cleanly, or does white-labelling three different brands force three agency accounts? What does that do to cost?
- **SaaS mode and rebilling**: can MSM Global (an Indian company) actually run GHL SaaS mode and rebill US clients? SaaS mode rebilling runs through Stripe connected to the agency. Check whether an Indian entity can get the Stripe account this needs, or whether we need a US entity/partner. This could decide the white-label question on its own.
- **A2P 10DLC and phone compliance** for US SMS through LC Phone or Twilio: who registers (us or each client), time to approve, cost, and how it fits our locked rules (RevLabs: no autodialer, no call recording, Texas email-only, text only after a spoken request; TF: email-first, no cold texts).
- **Data ownership and exit**: can we export contacts, conversations, pipelines, custom objects and workflows? What's the pain of leaving at 50 clients?
- **GHL sites vs our own builds**: does a GHL-hosted site pass RevLabs' SEO gate (title, description, canonical, sitemap, schema, llms.txt, speed)? Build one test page in the sandbox and check it. This decides whether Track B sites get built in GHL.
- **Custom objects and API v2**: good enough for Leasify's property/unit/lead model and TF's restaurant/guest data, or does the real data have to live in our own Postgres/Supabase with GHL as the engagement layer only?
- **AI features** (Conversation AI, Voice AI, AI Employee, workflow AI steps): what they cost per sub-account, what they actually do in the live account, and whether they could replace or host Leasify's "Amy Scott" AI agent.
- **Where GHL is clearly the wrong tool** for each line. Say it plainly.

## How to write

- Plain, simple words. Short bullets. Say what a thing is the first time you name it; don't assume I know GHL's internal terms.
- **No em-dashes anywhere.** Use commas, full stops or colons.
- Sentence-case headings. No "in summary" wrap-ups, no hedge-and-announce phrasing, no filler.
- When it comes to prices and packaging, **pick the option most likely to convert and say why**. Don't hand me a list of open decisions.
- Don't restate the context files back to me. Use them.
- Keep the first version lean. We're early: we need paying clients in the next 180 days, not a perfect platform. If GHL is overkill for a line right now, say that.

## Safety rules for the live GHL account

In `04-GHL-TEARDOWN-PROTOCOL.md`. Short version: sandbox sub-account only, no messages to real contacts, no buying numbers or add-ons, no billing or plan changes, no deleting anything that already exists. Ask me before anything that costs money.
