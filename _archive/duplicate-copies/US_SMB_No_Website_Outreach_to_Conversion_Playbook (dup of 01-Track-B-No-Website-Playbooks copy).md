# US SMB No-Website Segment: Full Outreach Sequence

**Companion to:** `US_SMB_GTM_Outreach_to_Conversion_Playbook.md` (the core flow this document forks from), `US_SMB_Pricing_and_Deliverables_Reference.md` (pricing ladder), and the live tracker `no_website_hot_launch_sep1.xlsx` (Lead Master Engine, `outputs\`) — 203 accounts, Dallas + Chicago, Sep 1–7 2026 launch window.

**Why this segment gets its own sequence, not a variant paragraph:** the core playbook's flow (research → email 1 → follow-up email → LinkedIn → call → text → break-up email → demo → close) assumes a website exists to audit and an email address exists to scrape. Neither is true here. 0 of 203 accounts have an extractable email — by definition, if there's no website there's nowhere for the scraper to find one. This is a **phone-and-text-only motion**, not an email sequence with a phone stage bolted on, and the pitch itself inverts: the core flow says *"your site is leaking revenue,"* this one says *"you have zero web presence despite real demand, here's what that's costing you."*

---

## 1. Who's in This Segment and Why

The main Lead Master Engine scorer caps every no-website account at 50/100 — it simply can't run the checks (booking funnel, mobile, schema, ad tags, tracking) that live on a page that doesn't exist. That silently buried genuinely strong businesses under the HOT threshold no matter how good the underlying business was.

Recalibration rule: **any no-website account with 50+ Google reviews — the model's own top demand breakpoint — is HOT.** These aren't weak leads with no signal; they're proven, trusted, high-demand businesses that are simply invisible online. 203 qualify across the full 3,057-account universe (Dallas 84, Chicago 119).

This is the single cleanest pitch in the whole US SMB motion: there is no ambiguity about whether they need a website. They don't have one. The only question is whether they know what that's costing them.

---

## 2. Before Any Outreach: What Already Exists Per Account

Unlike the core flow, there is no separate research layer to run before Touch 1 — the tracker ships ready to call:

| Field | Where it lives | What it's for |
|---|---|---|
| Business name, vertical, city, phone | Tracker tab | Call targeting |
| Google review count + rating | Tracker tab | The credibility hook in the opener — "you've got {Reviews} reviews, genuinely strong" |
| Revenue Leak Low/High ($/mo) | Tracker tab (from `leak.py`'s `missed_calls + no_website_full_loss` model) | The dollar figure for the call — **framing for the conversation, not an audited figure**, say so if pressed |
| Launch Day / Launch Date | Tracker tab | Which of the 5 dispatch days (Sep 1–7) this account is worked |
| Outreach Stage, Called?, Texted?, Notes | Tracker tab | Live state — update after every touch, this drives the Dashboard tab |

**The one manual check before dialing:** confirm the business is still open and the phone number is live (dead numbers get tagged `bad_data` and removed, same as the core flow's §4). Skip the deeper 5-minute pre-call research pass from the core playbook §2.2 — there's no site or socials to freshness-check.

**Channel coverage:** Phone 199/203 (98%), Email 0/203. This wave is not staged in Apollo or any email sender — don't build an email step for it.

---

## 3. The Full Flow, Stage by Stage

| Stage | Timing | Channel | Goal | Advance when | Branch/stop when |
|---|---|---|---|---|---|
| 0. Dispatch | Pre-outreach | Internal | Account assigned to its launch day, sorted by review count within the day | Tracker row exists | — |
| 1. Call attempt | Day 1 of that account's launch day | Phone | Live conversation; book the 15-minute walkthrough | Conversation had | No answer → voicemail (§5.2) + Stage 2; wrong number → `lost`, `bad_data` |
| 2. Text follow-up | Same day or next business day, only after a call attempt was made | SMS | Low-friction nudge referencing the call, offer to send an example | Reply | No reply after 2–3 business days → Stage 3 |
| 3. Second call attempt | Day 3–4 from Touch 1 | Phone | Re-attempt live conversation, different time of day than Touch 1 | Conversation had | No answer again → Stage 4 |
| 4. Break-up text | Day 7–10 from Touch 1 | SMS | Last low-pressure touch, explicitly removes pressure | Reply (often positive) | No reply → mark cold, recycle in 60–90 days |
| 5. Walkthrough | Scheduled off any positive reply/call | Call/screen-share (or a quick example site sent by text if hesitant) | Show what a real site + Google/AI-search setup would look like for this specific business, pitch the $199 entry | Verbal interest | Ghost after booking → same no-show handling as core flow §4 |
| 6. Close | Same call or immediate follow-up | Call/text | Close the $199 website entry; use it as the door-opener into the $999 Complete Growth System, not the ceiling | Payment | Objection → §6; "need to think" → structured follow-up |
| 7. Onboarding → Delivery → Retention | Post-sale | Same as core flow §§9–11 | — | — | — |
| 8. Loss / recycle | Any point marked lost | Internal | Tag reason (§9 below), requeue in 60–90 days | — | Two consecutive lost cycles → deprioritize |

**Why no email or LinkedIn stage:** there's no address to send to, and a no-website business owner in these verticals (auto repair, HVAC, plumbing, and similar trades skew the 203) is reliably lower-yield on LinkedIn than a dentist or architect — the core flow already scopes LinkedIn to higher-ticket verticals only (§3, Stage 3). Don't manufacture an email step by guessing an address; a wrong-guess cold email to a business with no site reads as spam immediately.

**Why texting is gated on a prior call, not sent cold:** this is a compliance rule, not a style preference — see §7. The existing Text Drafts tab is already built this way ("tried calling... noticed you don't have a website"), keep it that way.

---

## 4. Call & Voicemail Script Library

These are the live scripts already built into the tracker's **Call Script** tab — reproduced here with the surrounding sequence logic. Treat every bracketed field as a merge from the Tracker row; never read the placeholder text aloud.

### 4.1 Opening (first 30 seconds)

> "Hi, is this {Business Name}? Hi [Name], this is [Your Name] — quick call, thirty seconds. I was pulling up {Vertical} businesses in {City} and noticed you've got {Reviews} reviews on Google — genuinely strong — but no website. Is that right, or did I miss it?"

This does three things the core flow's opener doesn't need to: confirms the business (some no-website accounts have a Facebook page or directory listing that looks site-like), leads with a real number instead of a vague finding, and gets a yes/no that pulls them into the conversation before any pitch starts.

### 4.2 The gap

> "So here's the thing: people who already know you can still find you through Google Maps. But anyone comparing a few options before they call — which is most people now — can't find you at all if they search your name or 'best {vertical} near me.' They just call whoever shows up with a real site."

### 4.3 The number

> "Based on your review volume, that's likely costing you somewhere around ${Revenue Leak Low}–${Revenue Leak High} a month in calls that go to a competitor instead — just from not having a front door online."

If pressed on where the number comes from: it's a modeled estimate from review volume and category norms, not an audit of their actual books — say so plainly, don't oversell its precision.

### 4.4 The offer

> "What we do is build a fast, mobile-first website plus your Google Business and AI-search setup — so you show up when people ask ChatGPT or Google's AI answers, not just classic search — built specifically for {vertical} businesses, live in about [X days], no long build process."

The AI-search line is the one piece of this pitch that's genuinely new relative to the core flow's audit-led angle — worth keeping front and center, it's the most differentiated thing being said on this call.

### 4.5 The ask

> "Worth 15 minutes for me to show you what it'd look like for {Business Name} specifically?"

### 4.6 If hesitant

> "Totally fair — no pressure. Can I text you a quick example of what we'd build, so you can look at it whenever?"

This is the bridge into Stage 2 (text follow-up) — always take the "send me an example" yes over letting the call end with nothing scheduled.

### 4.7 If not interested

> "No worries at all — if that ever changes, feel free to reach out. Have a good one."

One graceful close, no pushing. Tag `not_interested`, recycle in 90 days per §9.

### 4.8 Voicemail (under 20 seconds)

> "Hi, this is [Your Name] — I help {vertical} businesses in {City} get found online. Noticed {Business Name} doesn't have a website despite {Reviews} great reviews — wanted to show you what that's likely costing you and what a quick fix looks like. Call or text me back at [Your Number], or I'll try again."

---

## 5. Text Script Library

The **Text Drafts** tab has one pre-written message per account (all 203, business-name- and review-count-merged). Sample pattern:

> "Hi, this is [Your Name] — tried calling {Business Name}. Noticed you don't have a website despite {Reviews} reviews on Google. We build fast, affordable sites for {vertical} businesses in {City} — happy to send a quick example if useful. Let me know!"

**Rule this is built around, and must stay true when hand-editing any draft:** every text in this tab is framed as a follow-up to an attempted call, never a cold opener. That's what keeps this compliant — see §7.

### 5.2 Break-up text (Stage 4, Day 7–10)

Not yet pre-drafted per account in the tracker — use this template, merge the fields by hand:

> "Hi [Name], last note from me — I'll stop reaching out after this. If it's ever useful: {Business Name} is likely losing real calls to competitors just from not showing up online, especially in AI search now. No response needed, door's open whenever the timing's better. — [Your Name]"

---

## 6. Objection Handling — No-Website Specific

The core flow's objection table (§6 of the companion doc) still applies for generic objections ("send it in writing," "need to think about it," "why calling from overseas"). These are the objections specific to a business that has genuinely operated without a website, which the core table doesn't cover:

| Objection | What's really being said | Response framework |
|---|---|---|
| "We've done fine without a website all these years" | Real proof point, not a bluff — respect it, don't argue against their own track record | "You clearly have — {Reviews} reviews doesn't happen by accident. This isn't about fixing something broken, it's about the calls you're not seeing at all right now, from people who never find you to leave a review or call in the first place" |
| "We get all our business from Google Maps / referrals already" | Believes their current channel is sufficient | "Maps works great for people who already know to look for you. The gap is the person comparing 2–3 options before they call — they search a phrase, not your name, and right now that search only shows whoever has a site" |
| "I tried a website before and it did nothing" | Real prior bad experience with a site that existed but didn't perform | Don't argue the old site was bad — differentiate on mechanism: "That's actually really common — a site that exists but isn't built around getting the phone to ring is barely better than no site. This is built specifically to convert calls, not just to exist" |
| "Who's going to maintain it / I don't have time for this" | Fears an ongoing burden, not just the upfront cost | Point to the $99/mo maintenance tier explicitly: "That's exactly what the $99/month covers — updates, hosting, and upkeep are on us, not something that lands on your desk" |
| "How much does this cost" (asked before the walkthrough) | Wants to gate the conversation on price before investing time | Don't quote cold — bridge to the walkthrough: "It depends a little on what {Business Name} actually needs, which is exactly what the 15 minutes is for — but the entry point starts at $199, and I'll show you exactly what that gets you" |
| "We're just a small shop, we don't need anything fancy" | Assumes this is an enterprise-grade, expensive build | "That's the point — this isn't a custom agency build, it's a fixed, fast, mobile-first site built for exactly this size of business. $199 to start, live in about [X days]" |

For every objection not listed here, fall back to the core playbook's table and general rule: never argue, downsell before discounting, surface the real objection before responding to the stated one.

---

## 7. Compliance Notes — Phone/Text-Only Wave

*Not legal advice — confirm with counsel before scaling past this initial 203-account wave, same caveat as the core playbook.*

- **Manual calls to business lines** (what every script above assumes — a human dialing one number at a time, no autodialer, no prerecorded voice): low regulatory risk. TCPA's autodialer/prerecorded-voice restrictions don't reach manual human dialing after *Facebook v. Duguid*, and the National DNC Registry only covers residential numbers, not dedicated business lines.
- **A sole proprietor's personal cell used as the business line** (common across this segment — auto repair, HVAC, plumbing shops often list an owner's cell) can still sit on the DNC Registry. Manual calls remain fine; any future autodialer/prerecorded use to that number would need consent first.
- **Texting is the real exposure in this wave**, more than the core flow, because every one of these 203 texts is a first text to a number that has never had email contact. TCPA treats a cell number as a cell number regardless of business status — a bulk or automated cold text needs prior express written consent ($500–$1,500/violation if skipped). This is exactly why every script in §5 is framed as "tried calling..." rather than a cold opener: **never send the text-draft tab as a first touch.** Call first, text only after that attempt. Keep it manual, one at a time, reply-triggered.
- **No email exists for this wave by design** — don't attempt to guess or scrape one to add an email step; a guessed cold email to a no-website business reads as spam and adds risk for no channel benefit.
- **Suppression**: one opt-out (on a call or a text) suppresses both channels for that contact immediately and permanently — same principle as the core flow §4's "remove me" rule, and the only hard stop in this sequence.

---

## 8. Close & Pricing — Entry Point Is $199, Not $999

This is the one place this segment's flow structurally diverges from the core playbook's close (§5.5), and it's deliberate, already named in the companion doc's vertical-variant section: **has-website accounts get pitched straight into the $999 Complete Growth System; no-website accounts open on the $199 website.**

The logic: a business with zero web presence needs the asset to exist before a $999 system built around that asset makes sense to them. Pitching $999 cold to someone who has never had a site invites sticker shock on a category they haven't evaluated yet; pitching $199 first gets a yes on the thing they can immediately picture (a real website), and creates the natural on-ramp to the funnel ($199), automation ($300), and full $999 system afterward.

1. **$199 Website** — the opening ask on every walkthrough in this segment. Live in [X days], mobile-first, built for the vertical.
2. Once delivered and live, re-approach at the 30–45 day mark (per the core flow's downsell-buyer handling, §4) as an upgrade conversation: funnel (+$199), automation ($300), or the full $999 system.
3. Name the $99/mo recurring plan on the initial call too, even though the entry sale is $199 — it's the answer to the "who maintains this" objection in §6, not a separate pitch to save for later.

**Open question, not yet settled** (per the pricing reference doc and Adam's own note): whether $199 is the right anchor for this call or whether it should sit lower for this specific segment, since these are businesses that have never paid for a web asset before. Don't freelance a different number on live calls — raise it internally before the next wave if the $199 close rate on this segment looks meaningfully different from the has-website $999-anchored motion.

---

## 9. Loss Reason Taxonomy

Same taxonomy as the core flow (§12 there) for consistency across both waves — use these exact tags in the Tracker's Notes column:

`not_interested` · `bad_data` (wrong number/closed business) · `budget` · `timing` · `chose_competitor` · `chose_diy` · `ghosted_no_reason_given` · `unresponsive_after_N_touches` · `opted_out`

---

## 10. Tracking — Use the Tracker/Dashboard Tabs As-Is

Every account update happens in the live workbook (`no_website_hot_launch_sep1.xlsx`), not a separate tracker:

1. Open the **Tracker** tab — one row per account, sorted by review count within each launch day.
2. Call using the **Call Script** tab (§4 above).
3. No answer → text using the **Text Drafts** tab (§5), or the break-up template (§5.2) once past Stage 3.
4. Update `Outreach Stage` / `Called?` / `Texted?` / `Notes` after every touch — the **Dashboard** tab recalculates from these columns automatically, no manual rollup needed.

`Outreach Stage` values already built into the tracker: `Not Started → Called → No Answer → Follow-up → Booked → Not Interested`. Map the flow above onto these exactly — don't invent new stage labels, it'll break the Dashboard tab's rollup.

**Launch schedule (superseded 2026-09-02 — see §11).** The original 203-account, Sep 1–7 schedule below never actually had outreach run against it (Tracker still read 100% Not Started as of Sep 2). It's kept here for the historical record of how the first file was sequenced; the live schedule is now the merged 531-account file in §11.

| Day | Date | Accounts |
|---|---|---|
| 1 | Tue Sep 1 | 41 |
| 2 | Wed Sep 2 | 41 |
| 3 | Thu Sep 3 | 41 |
| 4 | Fri Sep 4 | 40 |
| 5 | Mon Sep 7 | 40 |

203 total — Dallas 84, Chicago 119.

---

## 11. Current Footprint, Merged Master Tracker, and the Real Launch (Sep 7 2026)

Three more no-website sweeps ran after this doc's first version (2026-09-01/02), covering 6 additional metros and, for the first time, the WARM and COLD tiers (not just HOT):

| Wave | File | Accounts | Tiers | Cities |
|---|---|---|---|---|
| Original | `no_website_hot_launch_sep1.xlsx` | 203 | HOT only | Dallas, Chicago |
| Round 2 | `no_website_san_antonio_columbus_sep2026.xlsx` | 65 | HOT/WARM/COLD | San Antonio, Columbus OH |
| Round 3 (grid-tiled) | `no_website_tx_metros_gridtiled_sep2026.xlsx` | 263 | HOT/WARM/COLD | Fort Worth, Houston, Austin, El Paso |

None of the three had actually been dialed as of Sep 2 — all still read 100% Not Started. Rather than run three separate trackers on three separate schedules, they're merged into one file: **`no_website_master_launch.xlsx`** — 531 accounts (383 HOT, 110 WARM, 38 COLD) across 8 metros, re-sequenced from the real launch date, **Monday Sep 7 2026**, at 45 accounts/day for one rep (business days only), sorted tier-first (HOT → WARM → COLD) then reviews descending within tier. HOT tier runs Sep 7–18 (10 working days), WARM Sep 21–22, COLD Sep 23. Same 5-tab format (README/Tracker/Call Script/Text Drafts/Dashboard) as every prior file — everything in §§3–8 of this doc applies unchanged, including the WARM/COLD accounts, since tier reflects review-proven demand, not a different pitch or channel.

**Working WARM and COLD for the first time — what actually changes:** nothing in the call flow or scripts. The only adjustment is expectation-setting: a WARM (10–49 review) or COLD (3–9 review) account has a thinner credibility hook ("you've got {Reviews} reviews" lands softer at 12 than at 200) and a smaller modeled Revenue Leak $ range. Don't inflate the number to compensate — if the leak estimate feels too small to be a compelling hook on a COLD account, lead more on the offer (§4.4) and less on the number (§4.3) for that call.

Vertical mix has also shifted with the new cities — Cosmetology, Pet Spa, Car Detailing, Landscaping, Veterinarian, and Mortgage Broker now show up in real volume alongside the original Auto Repair/HVAC/Plumbing mix. See §12 for vertical-specific hook variants.

**Confirmed pattern across every city swept so far:** lawyer, realtor, dental, med-spa, HVAC, and roofing consistently return few or zero no-website accounts — licensing and referral pressure keeps those professions online almost universally. Auto repair, cosmetology (hair/nail salons), car detailing, handyman, landscaping, and pet grooming/spa are where no-website volume concentrates. If a future sweep is trying to maximize no-website list size, weight vertical selection toward those six rather than sweeping all 15 evenly.

**Next cities, if expanding past this footprint:** target additional metros in the Houston/Dallas population tier (not San Antonio/Columbus tier — those returned noticeably thinner yield even after accounting for population, since Google Places' ~60-result-per-phrase ceiling bites harder relative to a smaller metro), always using the grid-tiled scan (`grid_scan.py`, not the original single-center `scraper.py`) from the first run rather than discovering the coverage-ceiling problem again. Prioritize geographic diversification away from the current TX-heavy footprint — Phoenix, Atlanta, Charlotte, Indianapolis, and Denver are reasonable next candidates: all comparable in metro size to Houston/Fort Worth, all outside Texas and the Midwest cities already covered, and none raise a materially different regulatory or compliance profile for the manual call/text motion in §7.

---

## 12. Vertical-Specific Hook Variants

The Call Script in §4 is deliberately generic — every vertical merges into the same template. These are the small, targeted adjustments worth making live on the call once the account's `Vertical` field tells you which of the six high-yield categories (§11) you're dialing. Treat these as additions to the existing opener/gap, not replacements.

**Auto Repair.** The comparison set is franchise chains (Jiffy Lube, Christian Brothers, Midas) that rank in every local search — that's the competitor to name in §4.3/objection responses, since it's concrete and the owner already knows them. Common objection specific to this vertical: *"We get by on repeat customers and referrals."* Response: "That's exactly why the reviews are so strong — the gap isn't your existing customers, it's the one-time driver who's never used you before and searches 'brake repair near me' when their check-engine light comes on. That's the call going to whoever has a site."

**Cosmetology (hair/nail salons).** Many of these accounts substitute Instagram or a Facebook page for a website — worth confirming on the opener rather than assuming zero presence. Objection: *"We're on Instagram, that's enough."* Response: "Instagram's great for showing the work — the gap is it doesn't show up when someone searches 'nail salon near me' on Google or asks ChatGPT, and DM-only booking loses people who just want to tap and book. This isn't instead of Instagram, it plugs the gap next to it."

**Car Detailing.** Frequently mobile or appointment-only, and up against booking-app competitors (Spiffy, and similar) that own the search result even in car detailing's own city. Lead the offer (§4.4) on booking flow specifically — "so someone can book a time slot directly instead of calling and hoping you pick up" — since that's the concrete mechanism this vertical's owners respond to.

**Handyman.** Usually a single owner-operator, decision made on the spot with no one else to consult — the fastest close cycle of the six. Often has no business email at all (not just none scraped) — don't imply one exists anywhere in the call.

**Landscaping.** Seasonal and often contract-based (HOA, recurring mowing/maintenance) rather than one-off jobs — the strongest angle is seasonal sign-ups happening online before a competitor's site catches them first, not per-job leakage. Worth timing outreach ahead of a season change if the calendar allows it, not something this fixed 45/day cadence currently optimizes for.

**Pet Grooming/Spa.** Reviews frequently name specific pets — if one comes up in the pre-call glance at the account, use it; it's a stronger, more specific opener than the generic review-count hook in §4.1. Facebook groups are a common informal booking channel here too, same dynamic as Cosmetology's Instagram substitution above.

**A regulated-vertical account shows up anyway (rare).** If a lawyer, dentist, HVAC, or similar account appears in this tracker despite the pattern in §11, treat it as a genuine anomaly worth extra care rather than a data error to dismiss — these owners are more likely to have deliberately opted out of a web presence (a med-spa doctor avoiding public visibility, a small-practice lawyer relying entirely on referral relationships) and may need a different objection response than the ones in §6, which assume the absence is an oversight rather than a choice. Ask directly rather than assuming: "I noticed you don't have a site, which is actually unusual for {vertical} — is that intentional, or just never gotten to?"

---

## 13. Quick-Reference Call Card

Everything above condensed to what a rep actually needs open during a live call — print this section or keep it on a second screen; the full logic in §§3–8 is the reference for anything this card doesn't resolve.

**Flow:** Opener (confirm + review-count hook) → Gap (Maps vs. search) → Number (modeled $ leak) → Offer ($199 site + Google/AI-search setup) → Ask (15 min) → book or bridge to text.

**If hesitant:** offer to text an example, don't push for the call slot twice.
**If not interested:** one graceful line, tag `not_interested`, hang up — no second attempt on the same call.
**No answer:** voicemail (§4.8, under 20 sec) → text follow-up only after this call attempt, never cold.

**Top 5 objections, one-line responses** (full versions in §6):
1. *"Done fine without a website"* → respect the track record, reframe as calls you never see, not something broken.
2. *"We're on Maps/Instagram/Facebook already"* → that channel works for people who already know you; the gap is the comparison shopper who doesn't.
3. *"Tried a site before, did nothing"* → differentiate on mechanism (built to convert calls, not just exist), don't argue the old one.
4. *"Who maintains it?"* → name the $99/mo plan directly, it's the answer.
5. *"How much?"* → don't quote cold, bridge to the 15-minute walkthrough, mention $199 as the starting point.

**Close:** open on $199 website entry (not $999 — see §8), name the $99/mo plan on the same call, never discount before downselling.

**Compliance in one line:** manual dial, manual text, text only after a prior call attempt, any opt-out kills all channels immediately.

---

## 14. What This Doc Deliberately Doesn't Cover

- **The has-website HOT wave's audit-led pitch and email sequence** — that's the companion doc, `US_SMB_GTM_Outreach_to_Conversion_Playbook.md`, unchanged by this fork.
- **A locked entry price for this segment** — flagged as open in §8, resolve before scaling past this wave.
- **A launch file or cadence beyond the current 8-metro, 531-account footprint** — §11 names reasonable next-city candidates, but no sweep has been run against them yet; don't assume coverage that doesn't exist.
