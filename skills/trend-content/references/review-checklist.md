# Critic pass

Switch roles: you are now a skeptical senior AI engineer and editor who will publicly call out any error. Assume the draft has at least three problems. Go through every section; record each issue and its fix.

## 1. Facts

- [ ] Every number matches the fact table exactly (value, unit, qualifier).
- [ ] Qualifiers kept: "up to", "in [company]'s testing", effort level, "partial credit", "with tools", dataset version.
- [ ] Company-reported numbers are labelled as such somewhere visible.
- [ ] Comparisons compare like with like (same benchmark version, same settings). If not, say so or drop the comparison.
- [ ] Dates, names, versions and prices are correct and current.
- [ ] Nothing is stated as fact that came from a single unverified source.

## 2. Logic

- [ ] No unit mixing (e.g. "per task" savings multiplied across calls inside that task).
- [ ] No "X% higher benchmark = X times smarter".
- [ ] No causation claimed from correlation.
- [ ] Extrapolations are labelled as such ("if this holds…").
- [ ] Each "so what" actually follows from the evidence shown.

## 3. Honesty and balance

- [ ] There is an honest-read slide: limitations, what's overhyped, where the competitor or older model still wins.
- [ ] The strongest counter-argument is represented fairly.
- [ ] No hype words, no emoji alarms, no "everything changed".
- [ ] Policy/political topics present positions, not personal verdicts.

## 4. Structure

- [ ] The hook is the most surprising true fact, not a generic summary.
- [ ] The thesis is visible by slide 3.
- [ ] No two slides make the same point. Merge or cut duplicates.
- [ ] Each slide has one job and one dominant visual.
- [ ] Slide order builds an argument; no slide could be removed without loss.
- [ ] The takeaway is memorable in one line.

## 5. Copy

- [ ] Headlines ≤ 10 words; body ≤ 45 words.
- [ ] No sentences copied from sources; quotes (if any) < 15 words, one per source.
- [ ] Plain words over jargon where possible; jargon defined once when needed.
- [ ] Reads well out of order (a screenshotted single slide still makes sense).

## 6. Brand fit

- [ ] Fits the creator's positioning in `brand.md` (default: a systems view — economics, architecture, tradeoffs).
- [ ] Gives the reader a decision or mental model, not just news.

## Output of the pass

List 3–6 concrete issues found and how each was fixed. If you genuinely found fewer than three, look again at the hook, the logic of the "so what" slide, and the qualifiers on every number before concluding.
