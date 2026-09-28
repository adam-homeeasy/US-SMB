# Claude Design handover: AU architects one pager (v2)

This replaces the first version. Two things were missing from what got built: nobody said who NoDecks is, and none of the diagrams or tables actually got drawn, everything came out as plain paragraphs. This version fixes both. Every visual below is described as an actual shape, boxes, arrows, a real table, not a suggestion to add one if there's room. Nothing in this document is optional.

**One thing to check before this gets built again.** The "What is NoDecks" paragraph in section 2 is my best draft based on what I could see in the nodecks-website codebase (the Table Foundry build, using the nd-cream, nd-charcoal, nd-green, nd-bronze tokens). I could not find an official "about us" line anywhere in that folder, so this is a reasonable guess dressed as a paragraph, not a confirmed fact. Read it, fix anything that is wrong, then build it. Do not ship it unread.

**Format.** One flowing artboard, seven stacked sections. Every diagram or table listed below must render as an actual visual element (real boxes, real lines, a real HTML table), never as a bullet list standing in for one.

---

## Section 1: Header

**Copy, exact:**

> A quieter way to grow a practice
>
> Most studios lose good projects to slow follow ups and a website that does not say much. This is a short look at what a fix could look like for yours.

**Build prompt for Claude Design:**
Full width header, generous top margin. Headline as the largest text on the page, one line if possible. Subhead directly below it, smaller, muted color, max width around 60 characters. No image, no icon, no logo placeholder here, the wordmark for NoDecks belongs in section 2 and the footer, not here. This is the calmest section on the page, mostly whitespace.

---

## Section 2: Who this is from

**Copy, draft, confirm before use:**

> This note comes from NoDecks. We build the working systems behind a business, ordering, booking, follow up, retention, not slide decks about them. Table Foundry, our restaurant ordering platform, is one example of that: a small operator saved from commission fees with a system we built and still run. This note is the same approach, aimed at what an architecture studio actually needs.

**Build prompt for Claude Design:**
A short, quiet strip, narrower than full width, sitting directly under the header with a visible divider line above it (a single hairline rule, not a box or card). Small NoDecks wordmark or just the word "NoDecks" set in a distinct weight above the paragraph, like a byline. This section should read like a signature at the start of a letter, not a company bio slide. No logo lockup, no tagline badge, just the paragraph and the name.

---

## Section 3: The situation

**Copy, exact:**

> Architecture studios are busy, but the pipeline is leaky in a few specific places.
>
> A homeowner calls with a budget that does not match what they are picturing, and an hour of a principal's time goes into finding that out. A studio's website looks beautiful but does not show up when someone nearby searches for help. A proposal goes out as a PDF and nobody knows if it was even opened. A happy client tells a friend, but there is no simple way to turn that into the next booking.
>
> None of this is a big problem on its own. Together, it is most of a studio's growth sitting on autopilot.

**Build prompt for Claude Design, mandatory diagram:**
This section needs a real four box diagram, not a paragraph with icons floating above it. Draw four equal width boxes in a single row, connected by a thin horizontal line running behind all four, like a simple process strip. Each box holds: a small line icon (phone for the first, a magnifying glass for the second, a document with a clock for the third, a speech bubble for the fourth), a short label directly under the icon ("Unqualified enquiries," "Hard to find online," "Slow proposals," "Referrals go nowhere"), and one line of supporting detail under the label, pulled from the paragraph above and trimmed to under 15 words. On narrow screens this stacks to a single column, icon and label stay side by side per row rather than shrinking the icons to nothing. This is a diagram. It must look like one, not like four text blocks that happen to be side by side.

---

## Section 4: What this could look like

**Copy, exact:**

> There are a few ways to close these gaps, and they do not require rebuilding everything a studio already has.
>
> A short tool on the website that asks a few questions and tells a visitor honestly whether their budget fits before they book a call. A page built for the specific area and council a studio works in, so it shows up when a local homeowner is searching for help. A proposal that goes out as a simple, trackable link instead of a PDF, so a studio knows the moment it has been opened. A light system that reminds happy clients and builders to leave a review or make an introduction, without anyone having to remember to ask.
>
> Each of these can stand alone, or work together as one system behind a studio's existing website.

**Build prompt for Claude Design, mandatory grid:**
Render this as an actual two by two grid with visible separation between the four cells, either a hairline border around each cell or a generous gutter with a thin divider, Claude Design's choice, but the grid structure has to be visible, not implied by spacing alone. Each cell: a two or three word title in plain language ("Budget check," "Local search page," "Trackable proposals," "Referral reminders"), a small line icon above or beside the title, and the one sentence description from the copy, trimmed if needed. No numbering, these are independent, not sequential steps.

**Also on this section, mandatory second diagram:**
Directly below the grid, add a simple left to right flow diagram showing how a client actually moves through a studio once these are in place: five small nodes connected by arrows, labeled "Enquiry," "Budget check," "Proposal," "Project," "Referral," with the last arrow looping back from "Referral" to "Enquiry" to show the cycle closing. Plain boxes or circles, thin connecting lines, arrowheads, no illustration, this is a process diagram, similar to a simple flywheel or value chain diagram in a strategy report. This is the one visual on the page that should look most like it came out of a consulting deck.

---

## Section 5: How a studio might start

**Copy, exact:**

> Some studios want to fix one thing first and see how it goes. Others are ready to put the whole system in place at once. Both are reasonable, and the starting point does not lock anyone into anything.

**Build prompt for Claude Design, mandatory table:**
Render this as a real two column table with a visible header row and visible row dividers, using Claude Design's table component if one exists, not a styled div made to look like a table. No pricing in any cell.

| | Starting small | Building the full system |
| --- | --- | --- |
| What it is | Pick one gap that is costing the most time or the most leads right now | Everything above working together, plus a full website behind it |
| Timeline | Live within about a week | A more complete build, planned around a studio's existing site and workflow |
| Good for | A good way to see how this fits before going further | The version most studios land on once they have seen the smaller pieces work |

---

## Section 6: Why this is different from what a studio has already tried

**Copy, exact:**

> Most studios have already talked to a web designer or a marketing freelancer at some point. This is not that.
>
> This work is built around how an architecture practice actually runs: high value projects, long sales cycles, and a client base that is judging craft the moment they land on a page. Nothing here looks like a template, and nothing asks a studio to write copy, manage ad spend, or learn a new piece of software.

**Build prompt for Claude Design, mandatory visual:**
This section needs one visual, a simple two column before and after style contrast, drawn plainly, not as an illustration. Left column, headed "What most studios have," a rough sketch of a cluttered contact form, five or six generic fields stacked with no hierarchy. Right column, headed "What this looks like instead," a single clean input with one clear question. Keep both sides simple line drawings or wireframe style boxes, not photographs or icons standing in for a form. This is the smallest visual on the page but it should still be a drawn comparison, not just two paragraphs side by side.

---

## Section 7: Close

**Copy, exact:**

> If any of this sounds familiar, it is worth a short conversation to see which piece, if any, is worth fixing first.
>
> Sovit Biswal, Principal
> Mohd Asad Khan, Senior Consultant
> hello@nodecks.in
> Sovit: +91 82494 24199
> Asad: +91 72756 94363

**Build prompt for Claude Design:**
Short closing line, centered or left aligned to match the header. Below it, both names and titles set small, one per line or side by side if there is room, then the shared email, then the two phone numbers each labeled with the name they belong to. Quiet, not styled as a button, no calendar link, no "book now" language. NoDecks wordmark can sit here too, small, as the last thing on the page, since section 2 already introduced who NoDecks is.

---

## Notes for whoever builds this in Claude Design

- No pricing, no numbers with rupee or dollar signs, anywhere on the page. This version is for an exploratory meeting only.
- Every section marked mandatory above needs an actual drawn element: a box diagram, a grid with visible dividers, a real table, or a simple comparison sketch. If the previous build skipped these and rendered plain paragraphs instead, that is the main thing to fix this time.
- Section 2's paragraph is a draft. Confirm or edit it before this goes anywhere near a client.
- Keep animation, if used at all, to a light fade or rise on scroll between sections. Nothing should move on its own after the page has loaded.
- If a page break is forced for print, break between section 4 and section 5, since section 4 now carries two visuals and is the heaviest part of the page.
- Total word count should stay short. If a draft comes out longer than what is written above, trim the words, not the diagrams.
