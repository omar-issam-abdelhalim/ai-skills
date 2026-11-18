# Story frameworks

## The universal spine

Every carousel follows the same arc, compressed or expanded to 6–10 slides:

1. **Hook**: the most surprising true fact, stated as a claim. Numbers beat adjectives.
2. **Context**: what this is, in one slide, for someone who missed the news.
3. **The real story**: the thesis, the non-obvious angle.
4. **Evidence**: 1–3 slides of numbers, each with one visual.
5. **The honest read**: limitations, caveats, what's overhyped.
6. **So what**: what changes for builders/founders/researchers.
7. **Takeaway + CTA**: the one line to remember, and "save this".

The honest-read slide is non-negotiable. It's what separates analysis from promotion, and it's the slide that builds trust.

## Templates by topic type

**Model release**
Hook (the surprising benchmark or economics fact) → Positioning & price → The real metric (cost per task, speed, tokens) → Capability evidence → Honest read of the benchmarks (spread across evals, company-reported) → Where it fits vs siblings/competitors (routing) → Takeaway.

**Research paper**
Hook (the result in plain words) → The problem it attacks and why it was hard → The key idea (one diagram) → Results with the baseline → Limitations the authors state + ones they don't → What it enables if it holds → Takeaway. Always name the authors' institution and say whether it's peer-reviewed or a preprint.

**Funding / M&A**
Hook (amount + what's surprising about it) → What the company actually does → The math (valuation vs revenue multiple, round size vs sector, if sourced) → Why investors are betting on it (the thesis) → The risk case → What this signals about the market → Takeaway for founders.

**Infrastructure / compute / chips**
Hook (the physical number: GW, $B, chips, cost) → What's being built and by whom → Why compute is the bottleneck here → The economics (cost per unit, energy, supply chain) → Who wins and who's exposed → What it means for model builders/startups → Takeaway.

**Product / agent launch**
Hook (what it can now do that it couldn't) → How it works (flow diagram) → Real use cases with evidence → Limits and failure modes → Competitive landscape → Builder takeaway.

**Policy / regulation / legal**
Hook (what changed and who it affects) → What the rule actually says (paraphrased, precise) → Who's affected and how → The arguments on each side (balanced, no personal political opinion) → Practical implications for builders → What to watch next. Stay evenhanded; present positions, not verdicts.

**Essay / analysis piece**
Hook (the author's strongest claim) → Who wrote it and why it matters → The argument in 3 steps → Where it's strong → Where it's weak or contested → Your synthesis → Takeaway. Paraphrase; never reproduce paragraphs.

## Hook formulas (pick one, fill with real facts)

- **Inversion**: "A mid-tier model just beat the flagship." (the smaller/cheaper/newer thing wins)
- **Hidden number**: "The price didn't change. The cost did."
- **Scale shock**: "[Company] is building [N] GW of compute. That's [concrete comparison]." (comparison must be sourced)
- **Wrong question**: "Everyone's asking X. The real question is Y."
- **Contradiction**: "[Claim] is true. It's also misleading."

Test every hook: is it true, is it specific, and would the target reader stop scrolling? If any answer is no, rewrite.

## Slide archetypes (each maps to a visual component)

| Archetype | Use for | Visual component |
|---|---|---|
| Big number | The single most important figure | `big-number` + optional `bar-compare` |
| Head-to-head | A vs B on one metric | `bar-compare` |
| Before → after across metrics | Improvement spread, honest read | `dumbbell` |
| Price / spec table | Pricing, specs, multi-model comparison | `data-table` |
| Mechanism | How something works, a formula | `formula-box` or `flow` |
| Spectrum / dial | Tradeoffs, settings, tiers | `level-bars` |
| System flow | Architecture, routing, pipelines | `flow` |
| Shift | Takeaway, old vs new thinking | `from-to` |

## Copy rules

- Headlines ≤ 10 words, supporting copy ≤ 45 words per slide.
- One idea per slide. If a slide needs "and also", split it or cut it.
- Every number carries its qualifier and source note.
- Write for a smart reader who is busy: short sentences, concrete nouns, no filler transitions.
- The last slide ends with a question or a save prompt, never both stacked with emojis.
