# Claude Design build prompt — Lakeside Heating & Air

Paste this directly into Claude (or whatever tool "Claude Design" turns out to be
concretely) to generate the actual site. Compiled from Strategy → Architecture → UI/UX →
Copy → Discoverability requirements.

---

**Build a single-page HVAC company website for Lakeside Heating & Air, a residential HVAC
contractor in Belmont Cragin, Chicago, IL.**

## Business details (use exactly, everywhere — this is the NAP source of truth for the site)
- **Name:** Lakeside Heating & Air
- **Address:** 4210 W Belmont Ave, Chicago, IL 60641
- **Phone:** (773) 555-0142
- **Hours:** Mon–Fri 7:00 AM–7:00 PM, Sat 8:00 AM–4:00 PM, 24/7 emergency line
- **Service area:** Belmont Cragin, Hermosa, Cragin, Montclare, Galewood, Elmwood Park
- **Rating:** 4.7★ across 62 reviews

## Positioning (from Strategy)
The trusted neighborhood HVAC company with the reviews to prove it — easy to book same-day.
Primary conversion goal: phone call or instant booking. Secondary: maintenance-plan signup.
Audience: homeowners in a breakdown-urgency moment, comparing this business against 2-3
other local HVAC companies who already have websites.

## Page architecture (from Architecture), in order
1. **Hero** — trust + urgency framing, technician photo, headline + subhead + primary CTA
2. **Services grid** — AC repair, furnace repair, installation, maintenance plans, emergency service
3. **Review carousel** — 6 cards, full text (see below)
4. **Service-area map** — real geographic map graphic covering the neighborhoods listed above, not a plain text list
5. **Financing / membership block** — maintenance-plan CTA as the secondary conversion path
6. **Sticky mobile "Call Now / Book Now" bar** — persists across scroll on mobile
7. **FAQ** — see content below
8. **Contact / booking form** — phone-first, form as backup. Simulate a success/confirmation
   state on submit (no backend yet, but the interaction should complete, not dead-end)

## Visual direction (from UI/UX)
- Palette: navy (#1a2233 / #2c3a5c) + warm amber (#ffb020) accent — trust + warmth, not
  generic corporate blue
- Type: bold, condensed sans-serif for headlines; clean readable body text
- Photography: full-bleed, realistic technician/truck imagery throughout — not stock-generic
  "smiling contractor in a polo" clichés, and not visibly-empty placeholder boxes
- High-contrast CTA buttons (amber on navy, or navy on white)
- Sticky mobile call bar is non-negotiable — most of this traffic is mobile, urgency-driven

## Copy (from Copy — factual-correctness + humanizer passed)
- **Headline:** "Belmont Cragin's most-reviewed HVAC company — now online."
- **Subhead:** "62 five-star neighbors can't be wrong. Same-day service, honest pricing, no
  surprises."
- **Primary CTA:** "Book a same-day visit."
- **Secondary CTA:** "See our maintenance plans."
- Tone: direct, local, confident without oversell. Short sentences. No "elevate your comfort
  experience" style AI-tell copy.

## Review carousel content (6 cards)
1. "Our furnace died at 11pm in January and someone was at our door by 8am. Fixed it same visit." — Maria T.
2. "Upfront pricing, no upsell pressure. Replaced our AC unit in one day." — James R.
3. "Been using them for 3 years for maintenance. Always on time, always explain what they're doing." — Priya D.
4. "Called two other companies first, neither called back. Lakeside picked up on the second ring." — Tom W.
5. "Fair price on a new furnace install, and they cleaned up after themselves." — Angela K.
6. "Their technician found a problem the last company missed. Saved us a much bigger repair later." — Dave S.

## FAQ content
**Do you offer financing for new installations?**
Yes — 0% financing for 12 months on qualifying furnace and AC installations, with longer-term plans available for larger systems.

**How fast can you respond to an emergency?**
Same-day service for calls received before 3 PM on weekdays; a 24/7 emergency line for after-hours furnace and AC failures, typically on-site within 2 hours.

**What areas do you service?**
Belmont Cragin, Hermosa, Cragin, Montclare, Galewood, and Elmwood Park. Just outside this area? Call — we take nearby neighborhoods case by case.

**Do you offer maintenance plans?**
Yes — our seasonal plan covers a spring AC tune-up and fall furnace inspection, with priority scheduling and a 10% discount on any repairs during the plan term.

## Discoverability requirements (do not skip these)
- Embed `LocalBusiness` schema markup using the business details block above exactly as given
- `FAQPage` schema wrapping the FAQ content above
- NAP block in the footer must exactly match the business details block above
- Reviews section structured as real, selectable text (not embedded as an image), so it's
  excerptable by an AI answer engine

## Illustration (generate one, don't skip this step)
Build one custom illustration: a simple flat-icon-style diagram of the 4 most common
furnace issues (no heat, strange noises, thermostat problems, poor airflow), matching the
navy/amber palette. This demonstrates the illustration hand-off step of the build process —
describe it precisely, generate a reference version, then have Claude Design produce the
on-brand final version matching this site's exact visual system.

## What NOT to do
- Don't invent review quotes, ratings, or claims beyond what's given above
- Don't use generic stock photography where a considered, on-brand photo direction is possible
- Don't skip the schema/NAP items — they're the reason this account was diagnosed as losing
  local-pack and AEO visibility in the first place
