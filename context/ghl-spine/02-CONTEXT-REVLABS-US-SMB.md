# Context: RevLabs US SMB

Condensed from `RevLabs US SMB` (00-Consolidation-Handover, US_SMB_Digital_Growth_Business_Handover, Track B offer and change log, go-live checklist, GTM plan to 5 Oct, compliance handovers, Track A and Track C playbooks; Sep 2026).

## What it is

- Productized digital growth systems for US local service businesses, delivered cheaply from India using internal tools, Claude and reusable templates.
- Positioning: "we find where your sales system is losing leads, then build the website, funnel, CRM and automation to fix it." Not "cheap websites", not "an AI agency".
- Founder-led sales from India, calling US hours (7:30 pm to 12:30 am IST, Mon to Fri). Two founders.
- Target verticals: auto repair, car detailing, hair/beauty, HVAC, plumbing, roofing, dental, med spa, lawyers, landscaping, handyman, pet spa, vets, realtors, mortgage brokers. Plan: 2 verticals x 150 accounts = 300 targeted businesses a month.
- **GHL is already the settled outreach/CRM tool** (decided 31 Aug 2026): email sending, calling/SMS, CRM and pipeline. What's still open is whether client websites get built in GHL, and whether GHL becomes the whole delivery platform that clients use.

## The three tracks

**Track B: first website for businesses with none** (the live track, locked offer)

- $49 to start, $150 when it's live. Live in 5 business days or no balance.
- Domain in the client's name, first year included.
- $29/month to keep it running (hosting, SSL, backups, monthly SEO re-check, up to 4 small changes a month). First month free, cancel any time, client keeps everything.
- One-page site: 3 services, hours, area, tap-to-call, enquiry form to email and phone, linked to their Google listing, passes our SEO gate (`seo_gate.py`: title, description, canonical, sitemap, schema, etc.), set up in Google Search Console and Bing.
- Not included: logo, photos, extra pages, payments, real booking system, ads.
- Upsell at day 45 only, to clients whose site is producing enquiries: **Growth $99/mo** (Google Business posts, review requests, more pages, monthly report), Funnel +$199, Automation $300, Full system $999.
- Change requests: $49 small change, $99 new section, $149 extra page.
- Year-one value per client: $199 + 11 x $29 = $518. "The monthly is the business."
- Current demo sites are on Netlify Drop. Payment links for $49 and $150 exist (processor not named in files: check).

**Track A: SEO engine** (internal tool name "Clearlane")

- Audit, plan and tracker today. Building toward a monthly SEO retainer (monthly report, rank tracking, content briefs, link outreach, local content). Uses Semrush, Apollo, Apify. Retainer prices not set yet.

**Track C: fixing AI-built sites**

- Businesses whose Lovable/Bolt/Replit/Base44 sites still show defaults (Google lists them as "Lovable App", no sitemap, no schema). We show it in a 60 to 90 second Loom, fix it for the same price shape as Track B. Email and Loom only, any state.

**The full system (the $999 target sale)**

- Website + funnel + AI automation + CRM + lead pipeline + automated follow-up + calling/text + $100 communication credit (a credit, not unlimited) + setup. Automations sold around specific jobs: missed-call text back, lead qualification, booking, follow-up, review requests, nurture.

## Compliance rules (locked, the spine must respect these)

- **Illinois is the phone state.** Hand-dialled only.
- **Texas is email and Loom only.** No calls, no texts, no live video, ever (we won't register under Texas Bus. & Com. Code ch. 302).
- **Ohio parked.** Growth comes from "green" states where calling is allowed without registration (26 states incl. Illinois, Georgia, New York).
- **Never an autodialer, predictive dialer or recorded voicemail drop.** Permanent.
- **No call recording** on Track B calls.
- **A text only goes out when the person asked for it in a live conversation**, and the rep logs their exact words. No text after a voicemail or an unanswered call.
- Scrub call lists against the National Do Not Call Registry.
- No quoting modelled "you're losing $X a month" figures. No copied Google reviews or photos on demos.
- Texas email lane runs from its own warmed sending domain.

So any GHL feature that auto-dials, power-dials, records by default, or fires SMS from a workflow without a logged consent flag is a risk. The fit analysis must say how to lock those off per sub-account.

## Current tools around it

- Lead Gen Tool (Python): scrapes Google Maps, enriches, scores and segments prospects (HOT/WARM/COLD by need: full stack, funnel, website, CRO), outputs call sheets and trackers (Excel). Dallas and Chicago lists built.
- SEO baseline kit and `seo_gate.py`.
- Crowd-test and Monte Carlo simulation kit for testing offers.
- Excel trackers and scorecards for the week.

## What this analysis must settle for RevLabs

- Should every paying client get their own GHL sub-account from day one (even the $29/month site client), or only once they upgrade to Growth $99 / $999?
- Can the $29/month tier survive the GHL cost per sub-account plus usage? At what client count does the agency plan pay for itself?
- Should Track B sites be built on GHL Sites (only if they pass `seo_gate.py`) or stay as static builds on Netlify/Cloudflare with GHL forms embedded?
- White-label: sell "RevLabs" as our own branded platform (GHL SaaS mode) at $99 / $299 / $999 tiers, or keep GHL invisible and sell done-for-you?
- How our internal prospecting pipeline (Lead Gen Tool output) flows into GHL for calling and email, with the compliance flags carried over.
