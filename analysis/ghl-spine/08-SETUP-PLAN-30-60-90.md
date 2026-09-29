# 08 Setup plan: 30, 60, 90 days

The verdict is yes to part of GHL for RevLabs and Leasify, and no for TF for now (`00`), so this is the build order for the first two. It is sized for two founders plus Sovit part-time, and for paying clients inside 180 days. Every step names the gate that must pass before the next one.

**Capacity comes first.** The line reports add up to about 434 build hours (`07`, risk 1). This plan cuts that to about 180 hours in 90 days: about 60 for RevLabs and about 100 for the HomeEasy MVP, plus 20 for the live check and snapshot. Adam names **one GHL owner** from the India team by day 3. That person builds, provisions and audits every sub-account, at about 15 to 20 hours a week.

## Day 0: the 30-minute live check (Adam, before anything else)

The public docs could not settle some questions, so these are the first thing to do in the account. Use one sandbox sub-account named `ZZ-TEST-Spine-Analysis`. Don't buy anything and don't message real contacts. The full list is at the end of `01`. These five decide the build:

| # | Check | If it fails |
|---|---|---|
| 1 | Sub-account phone settings: recording is off on a new number, and the power dialer and voicemail drop can be hidden or disabled per sub-account or per user role | RevLabs client delivery moves off GHL. GHL stays for our own prospecting only (`03`) |
| 2 | A2P Trust Center: which registrations are per sub-account, and whether a brand without a US EIN is accepted (read only, do not submit) | MSM's own texting waits for the US entity. Clients register under their own EIN anyway |
| 3 | Conversation AI can write answers into contact fields, call an outside webhook mid-chat, and hand off to a human | Leasify's AI first responder is not built in GHL. GHL shrinks to calendar, reminders and reactivation (`02`) |
| 4 | Build one page and run it through `seo_gate.py` and PageSpeed, and try serving a root `llms.txt` | Confirms Track B stays static. That is already the plan, so a failure changes nothing |
| 5 | Client user role can be limited to inbox, calendar and pipeline | Clients get reports only, no logins |
| 6 | App Marketplace, Payments: which apps work as a SaaS-mode custom payment provider, and which accept an Indian company charging US cards on subscription (added 29 Sep) | White-label stays off until a US entity exists. The verdict doesn't change either way, since white-label is off for business reasons |

Also on day 0, outside GHL:
- Check whether MSM already holds an active Stripe account, and which entity owns the RevLabs payment links (`01` check 12).
- **Start the US entity with an Indian CA:** Stripe Atlas, a Delaware LLC, $500, then $100 a year, about 2 to 6 weeks to a first payment. It is on TF's critical path for Stripe Connect whatever happens with GHL. It also gives MSM an EIN for its own A2P brand and a US card for the agency wallet (`01` Q2, `07`).
- Brief a US telecom lawyer on four questions: text-back to inbound missed callers, texting listing-site leads, Texas ch. 302 for clients' own customers, and the AI disclosure for Amy Scott (`07`).

## Days 1 to 30: RevLabs first, on Starter

RevLabs already uses GHL for outreach and is the line closest to revenue, so it goes first. Stay on **Starter $97** because 3 sub-accounts are enough. Use the 14-day free trial for the day-0 check if the account is not yet paid.

**Sub-accounts (3 of 3):**
1. **RevLabs Illinois calling.** Hand-dial only. Power dialer, voicemail drop and recording off. DNC-scrubbed list import.
2. **RevLabs Texas email lane.** No phone number at all, own warmed sending domain, email and Loom only. This is the one hard lock: with no number, it cannot call or text.
3. **Sandbox `ZZ-TEST-Spine-Analysis`.** Used for the day-0 check and for testing every snapshot change before it is pushed to a client.

TF does not get a sub-account. Sovit runs the NYC pipeline on a sheet plus email until 30 Nov and 10 or more live prospects, then re-tests (`00`).

**Build in this order:**
1. **Compliance fields snapshot.** State; `dnc_scrubbed` with date; `sms_consent_words`, `sms_consent_date` and `sms_consent_rep`; Texas tag; opt-out tag. Every SMS step in every workflow sits behind an If/Else on the consent field and a not-Texas check. Every opt-out sets DND on all channels (`03`).
2. **Cold email on our own SMTP** (bring-your-own), not the shared LC Email pool (`06`).
3. **Lead Gen Tool to GHL import.** CSV mapping from the Python output (HOT/WARM/COLD, need segment, state, DNC flag) into the calling sub-accounts. Keep it a CSV import at first, not an API sync.
4. **Message log webhook.** Every message, opt-out and consent change goes to Postgres (`06` exit plan). Build it once and reuse it everywhere.
5. **RevLabs pipeline stages**, from call attempt through audit walkthrough, $999 offer, downsell and won or lost, with loss reasons.
6. **Workflow specs in the repo.** One page per workflow, written as it is built.

**Tested on a real client first:** the first RevLabs Growth or Full-system sale. It gets its sub-account from the snapshot, which forces the upgrade in the next section. The $29 Track B clients never get a sub-account.

**Gate to day 31:** 7 days of calling from the Illinois sub-account with zero recording, zero dialer use and no SMS without a logged consent. Adam checks the call log and the consent fields.

## Days 31 to 60: Unlimited, first client sub-accounts, Leasify pilot on HomeEasy

**Upgrade to Unlimited $297** on the day a 4th sub-account is needed. That is the day HomeEasy's build starts or the first RevLabs Growth client signs, whichever comes first. Stay monthly until 10 paying clients are on GHL, then switch to annual ($2,970, which saves about $594 a year).

**RevLabs client snapshot (v1):**
- **No missed-call text back until the lawyer clears it.** The locked rule allows a text only after a spoken request in a live conversation, so the default is an instant alert to the client plus a callback task. It is sold as "missed-call alert and callback" and turned into text back per client only after written counsel sign-off (`07`).
- Web form to CRM, instant email reply, and a booking calendar with reminders.
- Review request after a job is marked done.
- A 5-step follow-up that respects quiet hours (8 am to 9 pm in the client's local time).
- The client's own A2P brand, registered on signing day. Budget 1 to 7 business days for approval [community, via 01].
- **Texas clients get email-only automations** until counsel answers the ch. 302 question for clients' own customers (`07`).

**Leasify pilot, HomeEasy first (the 4th or 5th sub-account). This is an MVP of about 100 hours, not the full 300-hour build in `02`:**
1. Pipeline stages for the qualification tiers: All, Responder, Non-Negative, Hot.
2. Tour calendar with reminders at 24 hours, 2 hours and 15 minutes, plus a no-show rebooking workflow.
3. Reactivation sequences at 7, 14, 30 and 90 days. Email first for old listing-site leads with no opt-in. Text only after the renter replies or gives consent (`02`, `07`).
4. Lift Score and matching stay in Python and Postgres. The results are written back to GHL contact fields through API v2.
5. Amy Scott stays where she runs today. Test Conversation AI side by side on 50 HomeEasy leads only if check 3 on day 0 passed.
6. The founder daily report and the client weekly report come from Postgres, not GHL dashboards. Commission tracking and the full reports wait until after the first paid client.

**Gate to day 61:** HomeEasy runs 2 weeks on GHL. Measure first-response time, no-show rate (target under 20%, about 35% today) and the reactivation rate. If response time or no-shows are worse than today's process, stop and fix before any paid Leasify client.

## Days 61 to 90: first paid Leasify client, and scale RevLabs

- **First Leasify client:** a locator or small property manager, in the locked outreach order. Their own sub-account from the HomeEasy snapshot. Their own A2P brand registered on day 1 of the 2-week free pilot, so texting is live before billing starts. The contract carries the 500-lead fair-use cap (`06`), and the SLA wording excludes outages at our platform vendors (`07`).
- **RevLabs:** every new Growth or Full-system sale is set up from the snapshot in under 2 hours. Log the actual setup minutes against the 20-hour build assumption in `03`.
- **Monthly audit habit, starting now.** For each sub-account, confirm recording is off, the dialer is unused, the consent gate is present on every SMS step, and A2P is approved. This takes about 5 minutes per sub-account. At 50 clients that is about 4 hours a month, so give it to one named person.
- **TF:** no GHL. Sheet plus email for sales, the US entity for Stripe Connect, and finish TF Reputation on the existing stack. Use GHL for restaurants (A-lite, about 70 hours) only if 2 of the first 3 NYC prospects refuse to sign without review requests and win-back at launch (`04`).

**Gate at day 90 (review with the numbers):**
- Cost per client against `05`. Flag anything more than 25% over.
- Compliance: zero recording, zero dialer use, zero texts without logged consent, zero Texas calls or texts.
- Any kill criterion in `07` hit? If yes, act on it.

## What is not in the first 90 days

- SaaS mode, Agency Pro, the white-label mobile app, and three agency accounts (`06`).
- Custom objects for Leasify properties and units, which stay in Postgres.
- Outbound Voice AI in any line. AI voices count as artificial voice under the TCPA [community, via 01].
- AI Employee bundles. Pay-per-use is cheaper at our volumes (`02`).
- GHL-hosted client websites.
