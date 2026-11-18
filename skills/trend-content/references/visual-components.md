# Visual components

Drop these into the main area of `assets/slide-base.html`. All values are inline styles so a slide stays a single editable file. Replace `{{accent}}` with the brand accent color; use it only for the hero element(s).

Rules for all components:
- Bar widths and dot positions are percentages of the real value on a stated scale (0–100 % unless noted). Compute them from the data; never eyeball.
- The post's subject gets `{{accent}}`; comparisons get `#52525B` (bars) or `#6B7280` (dots).
- Every numeric component sits above or beside a label saying what it measures.

## Contents
1. section-header
2. big-number
3. bar-compare
4. dumbbell
5. data-table
6. formula-box
7. stat-cards
8. level-bars
9. flow
10. from-to
11. callout
12. footnote

---

## 1. section-header

```html
<div style="display: flex; flex-direction: column; gap: 20px">
<div style="font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 24px; letter-spacing: 0.06em; color: #A78BFA">// SECTION NAME</div>
<h1 style="margin: 0; font-size: 76px; font-weight: 700; line-height: 1.04; letter-spacing: -0.035em">Headline here.</h1>
</div>
```
To color part of a headline: `<span style="color: {{accent}}">…</span>` (only at ≥ 60 px).

## 2. big-number

```html
<div style="font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 220px; font-weight: 700; line-height: 0.9; letter-spacing: -0.05em; color: {{accent}}">70.6%</div>
```
Size 150–230 px depending on character count; 5–6 characters max at 220 px across 904 px.

## 3. bar-compare

One row per item. Label width 190 px, value width 120–130 px.

```html
<div style="display: flex; flex-direction: column; gap: 22px">
<div style="display: flex; align-items: center; gap: 24px">
<div style="width: 190px; font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 26px; color: #F8F8F8">Subject</div>
<div style="flex-grow: 1; height: 22px; background: #171717">
<div style="width: 70.6%; height: 22px; background: {{accent}}"></div>
</div>
<div style="width: 130px; text-align: right; font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 28px; font-weight: 700; color: #F8F8F8">70.6%</div>
</div>
<div style="display: flex; align-items: center; gap: 24px">
<div style="width: 190px; font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 26px; color: #9CA3AF">Comparison</div>
<div style="flex-grow: 1; height: 22px; background: #171717">
<div style="width: 66.4%; height: 22px; background: #52525B"></div>
</div>
<div style="width: 130px; text-align: right; font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 28px; font-weight: 700; color: #9CA3AF">66.4%</div>
</div>
</div>
```
For non-percentage values (tokens, dollars), scale to the largest value = 100 % and say so in a label.

## 4. dumbbell (before → after, with a reference tick)

Best for the honest read: shows that the same upgrade produced very different jumps.

```html
<div style="display: flex; flex-direction: column; gap: 12px">
<div style="display: flex; justify-content: space-between; align-items: baseline">
<div style="font-size: 30px; font-weight: 600">Benchmark name</div>
<div style="font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 24px; color: #9CA3AF">10.3 → <span style="color: #C4B5FD; font-weight: 700">70.6</span> · Ref 66.4</div>
</div>
<div style="position: relative; height: 44px">
<div style="position: absolute; left: 0; right: 0; top: 21px; height: 2px; background: #262626"></div>
<div style="position: absolute; left: 10.3%; width: 60.3%; top: 19px; height: 6px; background: {{accent}}; opacity: 0.45"></div>
<div style="position: absolute; left: 10.3%; top: 10px; width: 24px; height: 24px; margin-left: -12px; border-radius: 50%; background: #6B7280"></div>
<div style="position: absolute; left: 66.4%; top: 2px; width: 4px; height: 40px; margin-left: -2px; background: #F8F8F8"></div>
<div style="position: absolute; left: 70.6%; top: 10px; width: 24px; height: 24px; margin-left: -12px; border-radius: 50%; background: {{accent}}"></div>
</div>
</div>
```
Connector: `left` = before, `width` = after − before. If after < before, swap left/width so the connector still spans the two dots. Add a legend row (grey dot / accent dot / white tick) above the group and "scale 0–100%".

## 5. data-table

Header row + data rows, subject column highlighted.

```html
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); border: 1px solid #262626">
<div style="padding: 22px 28px; font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 20px; letter-spacing: 0.06em; color: #9CA3AF">METRIC</div>
<div style="padding: 22px 28px; background: #1A1030; font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 20px; font-weight: 700; letter-spacing: 0.06em; color: #C4B5FD">SUBJECT</div>
<div style="padding: 22px 28px; font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 20px; letter-spacing: 0.06em; color: #9CA3AF">OTHER</div>
<div style="padding: 24px 28px; border-top: 1px solid #262626; font-size: 28px">Row label</div>
<div style="padding: 24px 28px; border-top: 1px solid #262626; background: #1A1030; font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 56px; font-weight: 700">$2</div>
<div style="padding: 24px 28px; border-top: 1px solid #262626; font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 56px; color: #9CA3AF">$4</div>
</div>
```
For a wider first column: `grid-template-columns: minmax(0, 1.7fr) repeat(3, minmax(0, 1fr))`. Values ≥ 5 characters: drop to 30 px.

## 6. formula-box

```html
<div style="display: flex; flex-direction: column; gap: 10px; padding: 32px 36px; background: #111111; border: 1px solid #262626; font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 30px; line-height: 1.3">
<div>cost_per_task =</div>
<div style="padding-left: 48px">(tokens_per_step × steps)</div>
<div style="padding-left: 48px">× price_per_token</div>
<div style="margin-top: 12px; font-size: 22px; color: #A78BFA">// the comment that explains the point</div>
</div>
```
Also works as a pseudo-terminal: prefix lines with `$ ` and use secondary color for output.

## 7. stat-cards

```html
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px">
<div style="display: flex; flex-direction: column; gap: 8px; padding: 28px; border: 1px solid #262626">
<div style="font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 76px; font-weight: 700; letter-spacing: -0.04em; color: {{accent}}">30%+</div>
<div style="font-size: 28px; color: #9CA3AF">faster output</div>
</div>
<div style="display: flex; flex-direction: column; gap: 8px; padding: 28px; border: 1px solid #262626">
<div style="font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 76px; font-weight: 700; letter-spacing: -0.04em; color: {{accent}}">≤30%</div>
<div style="font-size: 28px; color: #9CA3AF">cheaper per task</div>
</div>
</div>
```
Three cards: `repeat(3, …)` and 60 px numbers.

## 8. level-bars (dial, tiers, spectrum)

Ascending bars with labels; highlight the relevant range in accent and bracket it.

```html
<div style="display: flex; flex-direction: column; gap: 16px">
<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 20px; align-items: end">
<div style="height: 50px; background: {{accent}}"></div>
<div style="height: 90px; background: {{accent}}"></div>
<div style="height: 130px; background: #3F3F46"></div>
<div style="height: 175px; background: #3F3F46"></div>
<div style="height: 220px; background: #3F3F46"></div>
</div>
<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 20px; font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 24px; font-weight: 700">
<span style="color: #A78BFA">LOW</span><span style="color: #A78BFA">MED</span><span>HIGH</span><span>XHIGH</span><span>MAX</span>
</div>
<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 20px">
<div style="grid-column: span 2; padding-top: 12px; border-top: 3px solid {{accent}}; font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 18px; color: #C4B5FD">BRACKET LABEL</div>
</div>
</div>
```
Bar heights are illustrative for ordinal scales only; say so if it could be misread as data.

## 9. flow (vertical system diagram)

```html
<div style="display: flex; flex-direction: column; align-items: stretch">
<div style="align-self: center; padding: 14px 26px; border: 1px solid #3F3F46; font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 22px; letter-spacing: 0.08em; color: #9CA3AF">INPUT</div>
<div style="align-self: center; display: flex; align-items: center; gap: 16px; padding: 6px 0">
<svg width="24" height="44" viewBox="0 0 24 44" fill="none" stroke="#6B7280" stroke-width="2" aria-hidden="true"><line x1="12" y1="0" x2="12" y2="40"></line><polyline points="4,32 12,41 20,32"></polyline></svg>
<span style="font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 20px; color: #9CA3AF">edge label</span>
</div>
<div style="display: flex; justify-content: space-between; align-items: center; gap: 24px; padding: 28px 32px; background: #111111; border: 1px solid #52525B">
<div style="display: flex; flex-direction: column; gap: 8px">
<div style="font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 26px; font-weight: 700; letter-spacing: 0.04em">NODE NAME</div>
<div style="font-size: 36px; font-weight: 600">Role · Role · Role</div>
</div>
<div style="font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 24px; color: #9CA3AF">meta</div>
</div>
</div>
```
Highlighted node: `background: #150F24; border: 2px solid {{accent}}` and name color `#C4B5FD`. Max 4 nodes per slide.

## 10. from-to

```html
<div style="display: flex; flex-direction: column; gap: 14px">
<div style="font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 22px; letter-spacing: 0.08em; color: #9CA3AF">FROM</div>
<div style="font-size: 50px; font-weight: 600; color: #6B7280; text-decoration: line-through">Old question?</div>
<div style="margin-top: 20px; font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 22px; letter-spacing: 0.08em; color: #A78BFA">TO</div>
<div style="font-size: 60px; font-weight: 700; line-height: 1.08; letter-spacing: -0.03em">New question?</div>
</div>
```

## 11. callout

```html
<div style="display: flex; flex-direction: column; gap: 16px; padding: 32px 36px; background: #111111; border: 1px solid #262626">
<div style="font-size: 30px; line-height: 1.35">The nuanced point in one or two sentences.</div>
<div style="font-size: 36px; font-weight: 700; color: #C4B5FD">The memorable line.</div>
</div>
```
Full border only. No left-border accent cards.

## 12. footnote

```html
<div style="font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; font-size: 18px; line-height: 1.5; color: #9CA3AF">Qualifier and source. [Company]-reported, [date].</div>
```

## Fitting check (do the arithmetic before writing)

Main area height ≈ 1350 − 136 padding − ~100 chrome − 80 gaps ≈ **1030 px**. Sum the estimated heights of your blocks (font-size × line-height × lines + paddings + gaps). If it exceeds ~1000 px, cut copy or shrink the hero before shipping. A 76 px headline fits ~22 characters per line across 904 px; 30 px body fits ~55.
