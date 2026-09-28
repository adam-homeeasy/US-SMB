# Kush Desai's Method for Building Dynamic, High-Quality Websites

Source: YouTube channel [@realkushdesai](https://youtube.com/@realkushdesai) (Kush Desai, 11K subscribers, 381 videos, "Documenting my Entrepreneurial journey"). This note covers only the five videos on that channel that teach a website-building technique — read and transcribed directly, in isolation, with no reference to any other system.

All five are short-form videos (42–51 seconds). They share one format, then each teaches one technique.

## The recurring format

Every one of these videos follows the same four-beat structure:

1. **Hook** — name something agencies charge real money for ("$10,000 for cinematic scrolling websites," "agencies charge thousands for this scroll effect").
2. **Reveal** — show it's replicable with a specific, named AI tool stack, not generic advice.
3. **Steps** — a short numbered workflow (3–4 steps), concrete enough to follow.
4. **Honest limit + CTA** — one caveat about what the tool doesn't do, then "comment [KEYWORD] and I'll send you the full guide/prompt" — the actual master prompt is never given in the video itself, only in the gated DM.

The throughline across all five: almost every technique routes through **Claude Code** (sometimes Cursor or Codex as alternatives) driven by **one carefully engineered prompt**, plus a second, specialized AI tool for whatever Claude can't natively generate (images, video, motion). The pitch in his own words: "the tools were never the hard part, but the taste — this workflow just does the taste for you."

---

## Technique 1 — The "Premium Hero Section" 4-step workflow

Source: [Someone worked out a four-step fix that finally makes AI built website look premium.](https://www.youtube.com/watch?v=lyIiObm6Cj4) (Sep 3, 2026)

Premise: hero sections drive ~80% of a website's first impression; most AI-built ones "still look very basic and AI-generated."

1. **Step 1 — Pull the brand kit.** Drop your site URL into an AI tool (spoken as "Leora AI") and it extracts your colors, fonts, and logo automatically, so everything generated afterward is already on-brand.
2. **Step 2 — Generate the hero image.** Hit generate, pick a hero image, describe what you want, and upload a couple of reference images to steer the look.
3. **Step 3 — Animate it.** Run "image to motion," select parallax, and it animates the static image smoothly instead of leaving it flat.
4. **Step 4 — Rebuild in code.** Drop that finished asset into Claude Code and have it rebuild the actual hero section in code around the asset, on-brand.

Closing line: "the tools were never the hard part, but the taste — this workflow just does the taste for you so your site stops looking like everyone else's."

## Technique 2 — Cinematic, AI-authored scrolling website (single prompt)

Source: [Agencies charge ten thousand dollars for cinematic scrolling websites](https://www.youtube.com/watch?v=f-E5j2V5Zas) (Aug 26, 2026)

Setup:
1. Open **Claude Code**, switch the model to **Fable 5**, and push reasoning to **max**. At max reasoning, per the video, the model "plans a page like a designer, section by section."
2. Connect the **Higgsfield MCP** so Claude isn't limited to stock photos — it generates its own hero images and video through **Seedance 2.0**, matched to the brand.
3. Give it **one prompt**: describe the brand, the mood, and 4–5 scroll scenes. From that single prompt it designs the sections, generates the visuals, writes the scroll-animation code, and hands over the finished site.

Honest caveat stated in the video: the first pass gets you to ~80%; the remaining 20% is art-directing it with follow-up prompts. The generated images/video draw down your Higgsfield account's usage, so check your plan before running it heavily.

## Technique 3 — Scroll-driven "product builds itself" reveal (Apple AirPods-style)

Source: [Agencies charge thousands for websites where the product builds itself as you scroll in 6 seconds.](https://www.youtube.com/watch?v=xHebKl3usTs) (Aug 19, 2026)

Framed as the same technique Apple uses on its AirPods product page. The entire trick is one short video clip plus one prompt:

1. **Get a 6-second clip of the subject** — film it on a phone, or generate one in **Google Flow** by giving it a start frame and an end frame (Flow gives 50 free credits/day).
2. **Drop the mp4 into an empty project folder.**
3. **Paste one prompt into Claude Code or Codex.** It uses `ffmpeg` to slice the video into individual frames and binds each frame to scroll position — scrolling down "builds" the subject frame by frame, scrolling back up disassembles it.
4. Generalizes to any subject — the video explicitly says it "works for a product, a property, even a burger."

The author says he wrote a companion prompt that also handles frame preloading, pinned text sections, and mobile fallback — again gated behind a comment/DM.

## Technique 4 — Apple Human Interface Guidelines as an AI design-audit skill

Source: [This AI Skill Uses Apple's Design Principles to Fix Your Website.](https://www.youtube.com/watch?v=nop363pgeFE) (Aug 17, 2026)

Premise: you can't prompt a feeling — telling an AI to "make it premium" means nothing to it; what it can follow is explicit rules.

- Tool: the **"Apple Design Skill,"** free on GitHub — found the actual repo: [dickwu/apple-design-skill](https://github.com/dickwu/apple-design-skill). It distills Apple's Human Interface Guidelines into 53 documents across Visual Design (10 files: color, typography, icons, images, materials, Liquid Glass, motion, branding, layout), Interaction (7: gestures, keyboard, pointer, stylus, focus, game controls, drag-and-drop), UX Patterns (18: onboarding, loading states, modals, settings, notifications, auth, search, undo), Accessibility (4: screen readers, contrast, inclusive design, RTL), and Media & Technology (8: audio, video, haptics, payments, maps, ML/AI, AR). Install into Claude Code with `claude install-skill /path/to/apple-design-skill`; Cursor and Codex have their own install paths in the repo. This one isn't DM-gated at all — it's a public repo, this is just the real link.
- Primary recommended use isn't building new sites with it — it's **auditing an existing site**: drop the skill into Claude Code (also works with Cursor and Codex) and ask it to review the site you already have. It flags things a person tends to walk past — slightly-off spacing, clashing type sizes, buttons that "feel wrong."
- Coverage: web, Flutter, Electron, and React Native — not web-only.

## Technique 5 — Deployment: Cloudflare over Vercel, run entirely from the agent

Source: [Vercel is easiest place to ship your vibe-coded app and that ease is exactly what you're paying for](https://www.youtube.com/watch?v=PkQsXGjRTCI) (Aug 17, 2026)

Not a build technique but the channel's stated deployment method, included because it closes the loop from "built" to "live":

- Framing: Vercel is the easiest way to ship (push and you're live in seconds) but that convenience is a rent you pay monthly on top of the underlying cloud (it runs on AWS/etc., not its own hardware).
- **Cloudflare** sits closer to the infrastructure layer, has its own global network, and a free tier generous enough that ordinary traffic barely moves the bill.
- What used to block people from switching — Cloudflare's dashboard being unfamiliar — is now moot: Cloudflare ships an official **Claude Code plugin**. One install command, and the agent deploys the app, creates the database, wires storage and DNS, and reads logs, all from the terminal — no dashboard needed.
- Confirmed this is real and public (not gated, not exclusive to his video): [developers.cloudflare.com/agent-setup/claude-code](https://developers.cloudflare.com/agent-setup/claude-code/). From a Wrangler project root: `/plugin marketplace add cloudflare/skills` then `/plugin install cloudflare@cloudflare`. That installs (a) Cloudflare Skills — persistent knowledge of Workers/Durable Objects/D1 conventions, (b) an MCP server covering the full Cloudflare API (DNS, WAF, R2, Zero Trust) from the terminal, and (c) Wrangler CLI access for local dev, migrations, and log tailing.

---

## What's actually gated vs. what's just not spelled out

Checked each of the five "get the full guide" claims directly:

- **Technique 4 (Apple Design Skill) and Technique 5 (Cloudflare deployment) are not gated at all.** Both are real, public resources — the actual repo and the actual Cloudflare docs are linked above with install commands. Nothing to reconstruct there.
- **Techniques 1, 2, and 3 genuinely withhold the master prompt** — that part is real, not DM-list padding. What follows are *my own reconstructions* of a prompt that would carry out each described workflow, built from the steps he did disclose plus standard technique (ffmpeg frame extraction, scroll-binding, accessibility fallbacks) — not his actual wording, which I have no access to and haven't tried to obtain (I'm not going to comment/DM his funnel on your behalf to get it).

### Reconstructed prompt — Technique 1, Step 4 (rebuild hero in code)

```
I have a hero background asset at /assets/hero-motion.mp4 (looping parallax
animation) and a brand kit at /brand/brand-kit.json (colors, fonts, logo).
Rebuild the hero section of [component/page] to:
- Use the video as a full-bleed background: object-fit: cover, autoplay,
  muted, loop, playsinline, with a static first-frame poster fallback for
  slow connections and prefers-reduced-motion (swap to a static image).
- Apply the exact colors/fonts from brand-kit.json to headline, subhead,
  and CTA button — no placeholder colors or system fonts.
- Add a scrim/gradient overlay so headline text passes WCAG AA contrast
  against the video.
- Keep headline + CTA as real DOM text (not burned into the video) for
  SEO and accessibility.
- Don't let the hero asset block render; lazy-load everything below the fold.
Rebuild only the hero section — leave the rest of the page untouched.
```

### Reconstructed prompt — Technique 2 (cinematic scrolling site, single prompt)

```
Build a single-page site for [brand]. Brand: [1-2 sentence description].
Mood: [e.g. "confident, minimal, high-end fintech"]. Plan the page as 4-5
full-viewport scroll sections, each one idea (hero/problem, feature 1,
feature 2, social proof, CTA). For each section:
1. Write real copy — headline + supporting line, no lorem ipsum.
2. Decide the visual it needs and generate it via the Higgsfield MCP tool
   using Seedance 2.0, matched to the brand palette and mood — state the
   generation prompt for each asset before calling the tool.
3. Build the section as a distinct scroll-triggered block (entrance
   animation for text and visual) using [CSS scroll-timeline /
   IntersectionObserver / a scroll library — your call].
Assemble into one page with smooth scroll and consistent spacing. Before
calling it done, review every section against the others for color, type
scale, and spacing consistency.
```

### Reconstructed prompt — Technique 3 (scroll-driven frame-scrubbing reveal)

```
I have a video at ./assets/product-reveal.mp4 showing [subject] assembling
as it plays. Build a scroll-driven canvas sequence:
1. Extract frames with ffmpeg: `ffmpeg -i product-reveal.mp4 -vf fps=24
   frames/frame-%03d.jpg`, capped at [1600px] wide to keep payload down.
   Write a frames.json manifest (count + dimensions).
2. Render a <canvas> pinned full-viewport (position: sticky) for the
   height of a tall scroll container (e.g. 400vh).
3. Preload the first ~10 frames before the section can be reached, then
   stream the rest via requestIdleCallback with a loading state.
4. Map scrollY within the pinned range to a frame index (0 → last frame)
   and canvas.drawImage() the current frame inside requestAnimationFrame —
   never redraw more than once per tick. Scrolling down plays forward,
   scrolling up reverses it.
5. Add pinned text overlays that crossfade in/out at fixed scroll-progress
   breakpoints (e.g. 0-20%, 40-60%, 80-100%), timed to what's on screen.
6. Mobile/slow-connection fallback: skip the frame sequence and show a
   single autoplaying muted looping video of the same clip instead of
   shipping the full frame set.
7. Respect prefers-reduced-motion: replace the whole sequence with a
   static end-state image.
Ship as one self-contained component.
```

## Cross-cutting observations (the method, distilled)

- **One consistent stack, five techniques**: Claude Code (frequently naming Fable 5 at max reasoning specifically) as the "builder/orchestrator," paired each time with a narrow, best-in-class specialist tool for the one thing Claude can't do natively — brand-kit extraction (Leora AI), image/video generation (Higgsfield + Seedance 2.0, Google Flow), or infra (Cloudflare). Cursor and Codex are mentioned as interchangeable alternatives to Claude Code in two of the five videos.
- **"Dynamic" in this channel's vocabulary means motion tied to state, not decoration**: parallax on a hero image, a scroll position bound frame-by-frame to a pre-rendered clip, or a fully AI-authored scroll-driven page — never just a CSS transition. Two of five techniques are explicitly scroll-position-driven.
- **"High quality" / "premium" is treated as a rules problem, not a taste problem.** The recurring claim is that vague prompts ("make it premium") don't work; what works is either (a) pulling real brand constraints in automatically (Technique 1's brand-kit step) or (b) handing the agent an explicit, documented rule set to enforce (Technique 4's Apple HIG skill).
- **Every technique compresses to one master prompt** run inside an agentic coding tool, with the surrounding steps being setup/asset-prep for that one prompt — not a multi-day build process.
- **Nothing here is a finished, disclosed prompt.** Every video's real payload (the master prompt) is deliberately withheld from the video and gated behind a "comment [KEYWORD]" DM funnel — a lead-generation mechanic layered onto the teaching content itself. Anything built from this method would need those actual prompts (not published) reverse-engineered or independently written, since only the workflow shape and the named tools are public.

## Sources

- [Someone worked out a four-step fix that finally makes AI built website look premium.](https://www.youtube.com/watch?v=lyIiObm6Cj4)
- [Agencies charge ten thousand dollars for cinematic scrolling websites](https://www.youtube.com/watch?v=f-E5j2V5Zas)
- [Agencies charge thousands for websites where the product builds itself as you scroll in 6 seconds.](https://www.youtube.com/watch?v=xHebKl3usTs)
- [This AI Skill Uses Apple's Design Principles to Fix Your Website.](https://www.youtube.com/watch?v=nop363pgeFE)
- [Vercel is easiest place to ship your vibe-coded app and that ease is exactly what you're paying for](https://www.youtube.com/watch?v=PkQsXGjRTCI)
- [Kush Desai channel](https://youtube.com/@realkushdesai)
- [Apple Design Skill (dickwu/apple-design-skill)](https://github.com/dickwu/apple-design-skill) — the real, public repo behind Technique 4
- [Claude Code + Cloudflare integration docs](https://developers.cloudflare.com/agent-setup/claude-code/) — the real, public setup behind Technique 5
