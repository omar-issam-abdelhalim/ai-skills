# Brand profile

Fill the profile once; every run reads it. The visual theme below ("Terminal Dark") is the default and can be used as-is or replaced with your own palette and type.

## Profile

| Field | Value |
|---|---|
| Creator name (footer) | `{{CREATOR_NAME}}` |
| Tagline (last slide) | `{{TAGLINE}}` |
| Audience | `{{AUDIENCE}}` (e.g. AI engineers, students and founders in the Middle East + global followers) |
| Timezone | `{{TIMEZONE}}` (IANA name, e.g. `Africa/Cairo`) |
| Platform | Instagram (default) or LinkedIn |

If the user has their own design system (colors, fonts, components), it overrides the theme below.

# Theme: Terminal Dark

## Palette

| Token | Hex | Use |
|---|---|---|
| Background | `#0A0A0A` | Every slide |
| Surface | `#111111` | Boxes, formula cards, callouts |
| Accent surface | `#1A1030` / `#150F24` | Highlighted column or card (the "hero" option) |
| Rule | `#262626` | Dividers, table lines, empty bar tracks (`#171717`) |
| Text primary | `#F8F8F8` | Headlines, body |
| Text secondary | `#9CA3AF` | Supporting copy, labels, footnotes |
| Muted data | `#52525B` / `#6B7280` | The "other" bar or dot (competitor, old version) |
| Accent | `#7C3AED` | Hero numbers (≥ 60 px), bars, borders. Written as `{{accent}}` in the components |
| Accent light | `#A78BFA` | Small accent text (labels, "SWIPE →") |
| Accent lighter | `#C4B5FD` | Accent text on accent surfaces, highlighted values |

Contrast rule: `#7C3AED` on black is ~3.5:1, fine for large bold numbers only. Any accent text under ~40 px uses `#A78BFA` or `#C4B5FD`.

## Type

- Display and body: **Space Grotesk** (400/500/600/700), fallback `'Helvetica Neue', Helvetica, sans-serif`.
- Numbers, labels, code, chrome: **JetBrains Mono** (400/500/700), fallback `ui-monospace, Menlo, monospace`.
- Google Fonts link (in the slide's `<head>`): `https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@400;500;700&amp;display=swap`

| Role | Size | Weight | Notes |
|---|---|---|---|
| Hero number | 150–230 px mono | 700 | letter-spacing −0.05em, line-height 0.9 |
| Headline | 72–84 px | 700 | letter-spacing −0.035em, line-height ~1.03 |
| Statement | 36–46 px | 600 | Closing lines |
| Body | 28–32 px | 400 | line-height 1.35 |
| Section label | 24 px mono | 400 | `// SECTION NAME`, accent light, letter-spacing 0.06em |
| Data label | 18–22 px mono | 400–700 | Uppercase for headers |
| Footnote | 18–20 px mono | 400 | Secondary color, sources and qualifiers |

Nothing under 18 px. The slide is 1080 px wide and shown ~390 px wide on a phone, so 18 px is the floor for legibility.

## Layout

- Canvas: **1080 × 1350** (portrait 4:5; works for Instagram and LinkedIn document posts).
- Padding: 72 px top, 88 px sides, 64 px bottom.
- Root: flex column, gap 40 px: header chrome → main (flex-grow, `justify-content: space-between`) → footer chrome.
- Header chrome: `MODEL X 2.0 · BREAKDOWN`-style topic label left, `01 / 08` counter right, both 22 px mono secondary, then a 1 px rule.
- Footer chrome: 1 px rule, then `{{CREATOR_NAME}}` in caps left (primary) and `SWIPE →` right (accent light). On the last slide the right side becomes `{{TAGLINE}}` in caps.
- Every slide opens its main area with a `// SECTION` label, then the headline.

## Principles

- The data is the visual. No photos, no logos as decoration, no robots, no gradients, no emoji, no glow.
- One hero element per slide, in accent. Everything else is white, grey or muted.
- Competitor/old values are always grey; the subject of the post is always accent.
- Sharp corners (radius 0), 1 px rules. A technical, terminal-like aesthetic.
- Source/qualifier footnote on any slide with a number that needs one.
