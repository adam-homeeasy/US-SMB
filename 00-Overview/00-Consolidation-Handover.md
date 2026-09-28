# RevLabs US SMB: consolidation complete

Executed 27 Sep 2026, following the confirmed plan. Everything below actually happened: files were moved and, where you approved it, deleted. This replaces the original study-only handover as the record of what's where.

---

## 1. What you approved and what I did with it

1. **Old Track-B playbook docs**: you asked for a compare-first pass, not a blind archive. I diffed them against the current locked `Track-B-No-Website-Playbook-v2.md`. Verdict: genuinely superseded, not just older copies. The old docs quote a flat $199 build with no split and a $99/month plan; the current v2 uses the $49/$150 split with $29/month, explicitly logged as a deliberate pricing change. The old docs also treat "we already tried calling" as grounds to text; v2 explicitly corrects that ("a previous dial doesn't give us permission to text") because it isn't compliant. One of the four files I was pointed at (`US_SMB_No_Website_Outreach_to_Conversion_Playbook.md`) turned out to be a byte-for-byte duplicate of the live AI SEO copy, not an old draft at all — that one went to `_archive/duplicate-copies/`, the other three genuinely-superseded docs went to `01-Track-B-No-Website/Legacy-Drafts/`.
2. **Demo sites**: you said none are currently in rotation. The whole `demo/` folder (architects site, HVAC placeholder, scout-tool frontend, growth-roadmap/pipeline PDFs) is archived at `_archive/abandoned-demos/`. Only AI SEO's `Reference-Demos` (auto repair, detailing, hair salon) — the set the go-live checklist actually points at — landed in `06-Demos-and-Sales-Assets/`.
3. **Adjacent, non-US-SMB folders**: you asked to tidy rather than leave alone. Coaches & Course Creators, SaaS Segmentation, AU Architects (all its scattered pieces merged into one folder), and CRO now live under a new `Consulting OS/Adjacent-Verticals/` folder, clearly separated from RevLabs US SMB.
4. **Junk**: you said delete for real. Deleted: `Lead Master Engine/.venv` (19MB), two `__pycache__` folders, both `.vercel` cache folders in the demo tree, the five `_to_delete_cro-os-v0.x` folders in CRO (already flagged for deletion by whoever worked on it before), one Excel lock file, and the raw per-persona crowd-test data (`discuss/`, `gate/`, `jobs/`, `pitch/`, `prompts/`, `write/` subfolders in every crowd-runs run — 700+ small files). Kept per run: `report.md`, `scores.md`, `audit.md`, `crowd.json`, `state.json`.

## 2. Where everything landed

`Sovit\RevLabs US SMB\` now holds 359 files, ~20MB, structured as:

- **00-Overview/** — this doc, plus the India/US-SMB handover docs and the TF brand-engine handover that were floating loose at the top of the old playbook folder.
- **01-Track-B-No-Website/** (144 files, 9.5MB) — `Plans/`, `Scripts/`, `Playbooks/` (incl. the current canonical outreach playbook and the locked v2), `Lists/` (deduped — one copy of `no_website_master_launch.xlsx`, not two), `Lead-Gen-Tool/` (the full scraper/enrichment/ranking tool, minus the venv), `Brand-and-Naming/` (the naming-round work), `Legacy-Drafts/` (the confirmed-superseded docs, kept for reference, not deleted).
- **02-Track-A-SEO-Engine/** (30 files, 1.4MB) — kept intact and self-contained as it already was.
- **03-Track-C-AI-Built-Site-Fix/** — the smaller, separate "fix an AI-built site" track had its own playbook and scripts scattered in with everything else; split out into its own folder rather than force it into Track A or B.
- **04-Simulation-and-Testing/** (133 files, 5.2MB) — Monte Carlo docs, the crowd-test kit, and every run's finished report/scores, with the raw per-persona data pruned.
- **05-Legal-and-Compliance/** — the legal brief, risk assessment, and the two compliance-rules handovers.
- **06-Demos-and-Sales-Assets/** — just the three current reference demos.
- **_archive/** — `duplicate-copies/`, `superseded-drafts/`, `abandoned-demos/`, `misc-unclassified/` (a handful of files I couldn't confidently place — see §3).

`Sovit\Consulting OS\Adjacent-Verticals\` now holds Coaches-and-Course-Creators, SaaS-Segmentation, AU-Architects, and CRO — 272 files, 9.8MB, out of RevLabs US SMB entirely.

`Sovit\AI SEO\` and the old `Consulting OS\Lead Master Engine\` and `Consulting OS\US SMB PLaybook\` folders are now empty (AI SEO's root can't be deleted since it's the mounted folder itself, but there's nothing left inside it).

## 3. Judgment calls worth your eyes

A few files didn't have an obvious home in your original plan. I made a call on each rather than block the whole pass — flagging them here so you can move anything I got wrong:

- `TurboQuant-Workflow-Plan.md` and a Claude-SEO tooling verdict note weren't about US SMB strategy specifically (general AI/tooling notes) — filed under `00-Overview/Misc-Notes/` and `02-Track-A-SEO-Engine/` respectively.
- `agency-master-agent-prd.md`, a `List Building` CSV, and an `MVP Run` HVAC JSON file had no clear connection to the current Lead Master Engine pipeline or either track — parked in `_archive/misc-unclassified/` rather than guessed into a track folder.
- `Claude_Design_Handover_OnePager` had three versions; kept v3 live in `Playbooks/`, archived v1/v2.
- The India/US SMB services handbook existed in three copies (root, loose, and inside a workspace subfolder + zip); kept one canonical set in `00-Overview/`, archived the rest.
- **Not touched:** `Consulting OS\India_US_SMB_Services_Analysis.xlsx` sitting loose at the Consulting OS root — it's a genuinely different, earlier version (23KB vs the 55KB one I kept, several hours older) and wasn't part of the folders you asked me to consolidate, so I left it where it was rather than guess whether you still need it.

## 4. Nothing else in AI SEO's active work broke

The move happened in one pass; nothing was left half-migrated. Go-live checklist, GTM plan, legal docs, and this week's calling material are all now under `01-Track-B-No-Website/` and `05-Legal-and-Compliance/`, intact and in the same files (not rewritten).
