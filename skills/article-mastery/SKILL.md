---
name: article-mastery
description: "Turn a single article URL into a full one-on-one mastery lesson instead of a summary: model the article's domain, difficulty and hidden assumptions, design a teaching strategy for that specific article, research outside sources to fill gaps and verify claims, then teach deeply enough that the reader can explain, defend and apply it without the source. Use whenever the user pastes or links an article and asks to learn it, master it, deeply understand it, \"teach me this\", \"break this down properly\", or turn it into a lesson, thread or script, in Arabic or English. Do NOT use for a plain \"summarize this\", \"tl;dr\" or \"key points\" request."
license: MIT
metadata:
  author: Omar Issam
  version: "1.0.0"
---

# Article Mastery

The point of this skill is mastery, not summary. A summary compresses; this produces the opposite — it expands understanding until the reader could teach the topic themselves, argue about it, and use it, without re-reading the original. If you ever notice yourself instinctively shortening or trimming to save space, that instinct is what this skill overrides.

## Inputs

Two things are required:
1. **The article** — a URL, or pasted text if the user already gave you the content.
2. **Language** — Arabic or English. If the user hasn't said which and the language of their message doesn't make it obvious, ask (don't guess) — it changes not just the output language but the terminology-preservation rules below.

If either is genuinely ambiguous (e.g. multiple links pasted with no indication which one), ask which article. Don't ask about anything else — difficulty level, audience, depth — those are things you determine yourself in Step 1, not things to hand back to the user as questions.

## Step 1 — Build a real model of the article before writing anything

Fetch the full article with a web-fetch tool (not just a search snippet) and read it properly before drafting a word of explanation. You're building an internal map, not skimming for a summary. Work out:

- Domain and subdomain (e.g. "ML" isn't enough — is this optimization theory, systems/infra, applied NLP, research methodology?)
- Difficulty level (beginner / intermediate / advanced) — this determines how much scaffolding you need to add
- The core objective: what problem is this article actually trying to solve, and for whom
- Target audience the *author* assumed — often different from who's actually reading it now
- Core concepts and, critically, the *relationships* between them — articles are rarely a flat list of facts, they usually build one idea on another
- Technical terms and keywords that need defining
- Background knowledge the article assumes but never states
- Hidden assumptions — claims the author treats as obvious that a newcomer wouldn't find obvious at all

Don't start Step 4 until this model is solid. A shaky model produces an explanation that mirrors the article's own gaps instead of fixing them.

## Step 2 — Design the teaching strategy for *this* article

There's no fixed template here on purpose — a philosophy paper, a systems-design postmortem, and a stats methods paper all fail to teach well if forced into the same shape. Decide, based on what you found in Step 1, which of these tools actually earn their place:

- Progressive build-up (simple version → full version)
- Real-world examples or analogies (only ones that actually map cleanly — a strained analogy is worse than none)
- Comparisons against something the reader likely already knows
- Step-by-step walkthroughs of a process or mechanism
- Mental models that will outlast the specific article
- Cause-and-effect chains
- Historical or contextual framing, when it explains *why* something is the way it is
- Text-based diagrams (ASCII/structured breakdowns), when spatial or structural relationships are hard to hold in your head otherwise

Use only what genuinely improves comprehension for this specific piece. Padding in a technique because the list exists defeats the purpose.

## Step 3 — Fill the gaps the article leaves

Articles are frequently incomplete, outdated, or written assuming context the reader doesn't have. Where that matters for understanding, search for it:

- Background the article assumes but doesn't explain
- Clarification for concepts the article treats too briefly
- Verification of load-bearing technical or factual claims — especially numbers, dates, and anything that might be stale
- Context that changes how a claim should land (e.g. the article is from a few years ago and the situation has since moved)

Every piece of outside material must directly improve understanding of *this* article — don't pad with interesting-but-tangential research. Cite external sources you actually use.

This is also where standard sourcing discipline applies: paraphrase in your own words rather than reproducing text, and never quote more than a small fragment from any one source — even in service of "teaching thoroughly." Depth means explaining the idea better than the source did, not reproducing more of the source.

## Step 4 — Teach it, don't summarize it

This is the core deliverable. For every concept that matters, go as deep as the concept needs — that means, where relevant:

- What it is, and why it exists (what problem it's a response to)
- How it actually works, mechanically
- When to use it / when not to — real trade-offs, not hedge-everything caveats
- Advantages, limitations, and the practical implications of both
- Common misconceptions and the mistakes people actually make because of them
- How it connects to the other concepts in the article — nothing should sit in isolation

Explain terminology as you use it rather than assuming it. Don't assume prior knowledge beyond what's genuinely required for the domain and stated difficulty level from Step 1. The test for whether you've done this right: after reading, the person should be able to explain the topic to someone else, argue about it, answer follow-up questions on it, and actually apply it — not just recognize it if they saw it again.

Longer is fine when the length is doing work. It's not fine when it's restating the same point in different words — cut that, not the substance.

## Step 5 — Self-review before sending

Before finalizing, check your own draft against:

- Every concept flagged as important in Step 1 actually got explained, not just mentioned
- The logical flow holds together — a reader shouldn't hit a concept that depends on something not yet introduced
- Nothing is factually shaky (recheck anything you're not fully sure of)
- No repeated points that add length without adding understanding
- Concepts are connected to each other, not delivered as a disconnected list
- It reads as *teaching*, not as a rewritten or translated version of the article

Revise before sending if any of these fail.

## Output rules

- Write the entire response in the requested language.
- **If Arabic**: write naturally in Arabic, but keep technical terms, API/library/framework names, protocol names, and standard industry terminology in English rather than forcing an awkward translation. Mixing is expected and correct here, not a compromise.
- **If English**: write naturally in English throughout.
- No fixed section template — let the structure from Step 2 shape the output. It should read like a single coherent one-on-one lesson from someone who actually knows the material, not a rewritten article, not a translation, and not a slide-by-slide walkthrough of the source's own structure.
