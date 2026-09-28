# TurboQuant: what it means for our workflow

Written 23 Sep 2026. Source: [Parthknowsai YouTube Short](https://www.youtube.com/shorts/d2WT_7G0p5g), posted 29 Mar 2026, about 468K views, 103 seconds. Transcript pulled from the video's captions.

---

## 1. What the video says

- An AI model holds your whole conversation in working memory while you chat. That memory is the "KV cache". It grows with every message, so long chats get slower and cost more to run.
- Google's TurboQuant shrinks each number in that memory from 16 bits to about 3.5 bits. Roughly 5x smaller, near-identical answers.
- The creator's own correction: this does not put big models on your phone. It means longer chats, faster replies and possibly cheaper AI on the provider's side.

## 2. What the video leaves out

| Point | Fact |
|---|---|
| It's not new | Paper out April 2025, accepted at ICLR 2026. The video's "a few days ago" refers to Google's blog post in March 2026. |
| Google's own numbers | 6x less memory at about 3 bits, up to 8x faster on H100 chips, no retraining needed. |
| Real-world numbers | Independent tests report smaller gains, around 30 to 40%. |
| Code | No official Google code. llama.cpp and vLLM support exists only as community forks and open pull requests. |
| Vector search | Also works for search-by-meaning databases, beating older compression methods in Google's tests. Not shipped in any database we'd use. |

---

## 3. What changes in our workflow

| Area | Decision | Why |
|---|---|---|
| Our AI stack (Claude, Semrush, Apollo, Apify) | **No change.** | KV cache is the provider's cost, not ours. Any saving reaches us as lower prices or longer context limits. Nothing to install. |
| Long sessions | **Keep the one-stage-per-session rule and the handover docs.** | Cheaper memory does not stop answer quality slipping in very long chats. |
| Running AI models on our own machine | **Skip.** | List tagging and first-line drafting already cost very little on Claude. A laptop build isn't worth the setup. |
| Vector search for Build 3 (content briefs) | **Park.** | If we need keyword grouping by meaning, the databases we'd pick already compress. No reason to wait for TurboQuant. |
| The video's format | **Use it.** See section 4. | This is the part that helps us now. |

### When to look at this again

- Anthropic cuts prices or raises context limits. Then re-check the cost assumptions in `capacity-planner`.
- llama.cpp or Ollama add TurboQuant to a main release, not a fork. Then look again only if Claude spend on list work has become a real line item.
- Build 3 gets a client who needs keyword grouping. Then choose a vector database with built-in compression.

---

## 4. The format we're taking from it

The video gets attention and trust in under two minutes with six beats:

1. **Hook.** "Breaking news."
2. **The problem in one line.** Long chats eat memory.
3. **How it works, in plain numbers.** 16 bits down to 3.5.
4. **Correct the hype.** "I want to set this straight."
5. **What it really does.** Longer chats, faster, cheaper.
6. **One call to action.** "Follow."

Beat 4 is the reason it works. The creator earns trust by saying what the thing *won't* do. That's the same rule as our banned-claims list in `03-Playbooks/Track-B-No-Website-Playbook-v2.md` section 3.

---

## 5. Where we use it: the Texas Loom

Texas is email and Loom only (locked 14 Sep). The handover doc lists the Texas Loom script as missing and says the Loom is now the pitch, 60 to 90 seconds, recorded against the prospect's real business. This is the script skeleton, built on the six beats.

### Rules for every Texas Loom

- **No phone number anywhere.** Not spoken, not on screen, not in the email signature, not on the demo page.
- **Show their own Google listing.** Don't run a "near me" search as proof. Results change with the searcher's location, and a search run from India says nothing about a street in Houston.
- **Nothing from the banned-claims list.** No ranking promises, no "you're losing $X", no "more customers", no AI-answer promises.
- **No delivery-day promise until one site has been built and timed.** Then use the measured number plus a buffer.
- **The email around the Loom follows CAN-SPAM** (handover doc section 6).

### Script skeleton (about 200 words, 75 to 90 seconds)

| Beat | Time | On screen | Say |
|---|---|---|---|
| 1. Hook | 0 to 5s | Their Google listing | "Hi [Name], I made this short video just for [Business]." |
| 2. The problem | 5 to 15s | Zoom on the listing, no website link | "Your listing has [N] reviews and a [rating] rating. That's strong. But there's no website linked on it." |
| 3. What we saw | 15 to 35s | Scroll their listing | "When someone taps your listing, they see your hours and reviews. They can't see your full list of services, your prices or where you work." Read out what the listing actually shows. |
| 4. Straight talk | 35 to 50s | Stay on the listing | "I won't tell you a website gets you more customers or ranks you higher. Nobody honest can promise that." |
| 5. What it does | 50 to 70s | Reference demo for their trade | "What it does: one page you own with your services, prices, hours and service area, linked from your listing. Here's one we built for a [trade]." |
| 6. The offer and one step | 70 to 90s | Offer line on screen | "It's $49 to start and $150 when it's live and you're happy with it. If you don't like it, you don't pay the rest. Hosting is $29 a month if you want us to keep it running. Reply 'yes' to this email and I'll send a short form." |

Words in [brackets] come from the pre-call check on their listing. Never guess them.

### One conflict to fix

The handover doc (section 5) says the Loom should show "their name not showing up when someone searches for their trade in their town." That's a near-me search, which the change log (section 2.5) banned as proof. This script follows the change log. **Update the handover doc so the Loom uses their own listing only.**

---

## 6. Other place it fits

- **MSM / Deckflare short-form content.** An "AI news, minus the hype" series: explain one AI story in 90 seconds, correct the overclaim, say what it means for a small business. The same six beats. Use the `nodecks-shorts` skill when this gets built.

---

## 7. Next steps

| # | Step | Where |
|---|---|---|
| 1 | Record one test Loom on a real Texas row using the skeleton above, and time it. | `02-Lists/` Texas rows |
| 2 | Write the full Texas email sequence around the Loom: first email, two follow-ups, opt-out line. | `04-Sequences-and-Scripts/` |
| 3 | Fix the near-me line in the handover doc, section 5. | `01-Plans/Track-B-Compliance-Rules-and-Channel-Strategy-Handover.md` |
| 4 | Build and time one site end to end, so the Loom can name a delivery date. | Already open item 1 in the handover doc |
| 5 | No action on TurboQuant itself. Check again when a trigger in section 3 fires. | None |

---

## Sources

- [The video](https://www.youtube.com/shorts/d2WT_7G0p5g)
- [Google Research blog: TurboQuant](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)
- [InfoQ: TurboQuant compression](https://www.infoq.com/news/2026/04/turboquant-compression-kv-cache/)
- [turbo-quant.com: paper and framework status](https://turbo-quant.com/)
- [llama.cpp discussion #20969](https://github.com/ggml-org/llama.cpp/discussions/20969)
- [TechCrunch: Google unveils TurboQuant](https://techcrunch.com/2026/03/25/google-turboquant-ai-memory-compression-silicon-valley-pied-piper/)
