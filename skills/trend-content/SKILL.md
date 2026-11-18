---
name: trend-content
description: "End-to-end pipeline that turns the latest AI news into a research-backed carousel post (Instagram or LinkedIn): scans the newest AI developments (models, papers, infrastructure, funding, products, policy, essays), proposes the top 3 with one recommendation, deep-researches the pick, outlines and writes every slide, runs a critic and fact-check pass, builds designed 1080x1350 slides, then writes the caption, first comment, posting time and music pick. Use whenever the user invokes trend-content or /trend-content, says \"go\" or \"يلا\" to start a content run, or asks for a post or carousel about the latest or trending AI news."
license: MIT
metadata:
  author: Omar Issam
  version: "1.0.0"
---

# trend-content

A gated pipeline: **Scan → Pick → Research → Outline → Write → Review → Build → Publish kit.**
Each gate ends with a stop and waits for the user. Never skip a gate, never run two gates in one turn unless the user explicitly says to go straight through ("do it all", "كمّل للآخر").

The whole point is authority, not reach-bait. Every post should leave a smart reader knowing something they didn't know, with numbers they can trust. A post that repeats the headline everyone else posted has failed even if it looks good.

## Before the first run: the brand profile

Visual identity, creator name, tagline, audience and timezone live in `references/brand.md`. If its placeholders (`{{CREATOR_NAME}}`, `{{TAGLINE}}`, `{{AUDIENCE}}`, `{{TIMEZONE}}`) are still unfilled, ask the user for them once at Phase 0 and use the answers for the whole run. The default visual theme ("Terminal Dark") works as-is.

## Language and voice

- Talk to the user in their language, keeping technical terms in English.
- Slide copy, caption and first comment are in **English** unless the user asks otherwise.
- Be direct. If a topic is weak, say it's weak. If the user's pick is worse than the alternative, say why, once, then do what they chose.

## Reference files (read when the phase says so)

| File | Read at |
|---|---|
| `references/scan-and-score.md` | Phase 1: search plan, source list, scoring rubric |
| `references/story-frameworks.md` | Phase 2–3: narrative templates per topic type, hook formulas, slide archetypes |
| `references/review-checklist.md` | Phase 4: the critic pass |
| `references/brand.md` | Phase 0 and Phase 5: brand profile, visual identity, layout chrome, typography |
| `references/visual-components.md` | Phase 5: ready-made slide building blocks |
| `assets/slide-base.html` | Phase 5: base artboard every slide starts from |
| `scripts/render_slides.py` | Phase 5: export slides to PNG |
| `references/publish-kit.md` | Phase 6: caption, first comment, timing, music |

---

## Phase 0: Start

Triggered by "go", "يلا", "/trend-content", or any request for a post about recent AI news.

- If the user already named a topic ("make one about X"), skip Phase 1 and go to Phase 2 with that topic.
- Otherwise start Phase 1 immediately. Don't ask what they want first; the scan is the question.
- Get the real current date and time from the environment and use the date in every search query. Stale queries return stale news.

## Phase 1: Scan and pick (GATE 1)

Read `references/scan-and-score.md` first.

1. Run a broad scan: **at least 10 searches across at least 6 of the categories** (models, research papers, infrastructure/compute, funding & M&A, products & agents, policy & regulation, open source, notable essays/articles, hardware/inventions). One search per category minimum; don't combine categories into one query.
2. Keep only items from the **last 7 days**, prioritising the last 72 hours. Confirm each item's date from the source, not from memory.
3. Build a candidate pool of 8–15 items, score each with the rubric, and pick the top 3.
4. Present them in this shape (in the user's language, technical terms in English):

```
## Top 3 right now

### 1. [Title] · [category] · [date]
What happened: one or two lines.
Why it matters: the stakes, concretely.
The angle: the non-obvious story nobody else will post.
Score: X/16 · Risk: [saturation / thin data / unverified claims]

### 2. ...
### 3. ...

## My pick: #N
Why this one beats the other two, in 2–3 sentences.
```

5. End with one line: pick one of the three, go with the recommendation, or bring your own topic. **Stop.**

Honesty rule: if the week is slow and nothing scores above 9/16, say so and recommend the strongest evergreen angle on a recent item instead of inflating a weak story.

## Phase 2: Deep research + outline (GATE 2)

Read `references/story-frameworks.md`.

1. **Primary sources first**: the official announcement, paper (arXiv/PDF), system/model card, SEC filing, press release, or the company's own blog. Fetch the full page, don't rely on snippets.
2. **Then 3–5 independent sources**: reputable coverage, expert commentary, critics, competitor context. Look deliberately for the skeptical view and for what the headline leaves out.
3. **Context**: what came before (previous version, competitor numbers, prior funding), and what this changes.
4. Target 8–20 tool calls for this phase. Stop when every number you plan to use is sourced.
5. Build a **fact table** (keep it in your working notes, show a condensed version to the user):

| Claim | Number | Source | Who says it | Confidence |
|---|---|---|---|---|

"Who says it" matters: company-reported vs independently measured must stay distinguishable all the way to the slides.

6. Find the **thesis**: one sentence the whole carousel argues. Not "X was released" but "X shows that Y". Test: would a smart AI engineer learn something from the thesis alone?
7. Propose the plan:

```
## Research
3–5 bullets: what's true, what's surprising, what's overhyped, what's missing from other coverage.

## Thesis
One sentence.

## Additions
Anything beyond the obvious story worth including (context, a hidden metric, a contrarian read).

## Proposed outline (N slides)
01 · [Role: Hook] · [key message] · Visual: [component, e.g. big number + bar compare]
02 · ...
```

Slide count: 6–10. Fewer, denser slides beat padding. Every slide needs one job and one visual.

8. **Stop.** Wait for approval or edits.

## Phase 3: Write every slide

After approval, write the full copy for each slide:

- Headline (≤ 10 words), supporting copy (≤ 45 words), the dominant number or visual element, and a source note where a number appears.
- One idea per slide. The slide must make sense if it's the only one someone screenshots.
- Numbers exactly as the source states them, with the qualifier ("up to", "in the vendor's own testing", "at high effort").
- Paraphrase sources; never paste sentences from articles. Direct quotes only if essential, under 15 words, one per source.

Don't show this draft yet. Go straight to Phase 4.

## Phase 4: Critic pass (GATE 3)

Read `references/review-checklist.md` and run it as a **separate reviewer**, not as the author. Assume the draft has at least three problems and find them.

1. Re-verify every number against the fact table. Any number without a source is removed or sourced.
2. Check logic (unit mixing, correlation vs causation, "7x benchmark = 7x smarter" style leaps), hype words, redundancy between slides, hook strength, and whether each slide earns its place.
3. Fix everything you found.
4. Present:

```
## Final copy
SLIDE 01 · [role]
[headline]
[copy]
Visual: [...]
...

## What the review changed
3–6 bullets: what the review caught and how it was fixed.
```

5. **Stop.** Wait for "ok" / "let's go" / edits. Apply edits and re-show only the changed slides.

## Phase 5: Build the slides

Read `references/brand.md`, `references/visual-components.md` and `assets/slide-base.html`.

1. For each slide, copy `assets/slide-base.html` to `slides/NN.html` (`01.html`, `02.html`, …) and fill it: header topic and counter, section label, headline, then the main area built from the visual components. Replace every `{{accent}}`, `{{CREATOR_NAME}}` and `{{TAGLINE}}` with the brand profile's values.
2. Compute every bar width and dot position from the data (see the component rules); never eyeball.
3. Export to PNG:
   ```bash
   pip install playwright && python -m playwright install chromium   # once
   python <skill-dir>/scripts/render_slides.py slides/ out/
   ```
   The script renders each `NN.html` at exactly 1080×1350 and reports any slide whose content overflows the frame. Fix overflowing slides and re-render.
4. Look at every PNG once. Fix clipped text, collisions and low-contrast accents; don't loop more than once per slide.
5. Hand the PNGs (and the HTML sources, so the user can edit text) to the user. If the environment has a design canvas or a page host, publishing the slides there is a bonus, not a requirement.

After building, tell the user in 2–4 lines what each slide shows visually.

## Phase 6: Publish kit

Read `references/publish-kit.md`, then deliver in one message:

1. **Caption** (English), following the caption structure.
2. **First comment** with the primary source(s) and "figures are [company]-reported" where relevant.
3. **Posting time**: a specific day and hour in the audience's timezone with the reasoning, plus the Insights check.
4. **Music** (Instagram): 3 instrumental options with one line each on why they fit. Names only, never lyrics.
5. **First-hour checklist**: 2–3 actions.

Then stop. The run is done.

---

## Rules that hold across all phases

- **Never invent.** No made-up numbers, quotes, dates, funding amounts or benchmark results. If data is missing, say so and design around it.
- **Company-reported ≠ independently verified.** Label it on the slide or in the footnote.
- **A benchmark measures one thing.** Always say what it measures before celebrating the score.
- **No hype vocabulary**: "game-changer", "revolutionary", "insane", "🚨", "10x" without evidence.
- **No real people's faces, logos as decoration, copyrighted images, or AI-robot clichés.** The data is the visual.
- If the user interrupts mid-pipeline with a change, apply it and continue from the current phase; don't restart.
- If a search tool fails or returns thin results, reformulate and retry before concluding there's no news.
