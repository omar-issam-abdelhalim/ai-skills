<div align="center">

# AI Skills

**Engineered reasoning workflows for AI agents.**

Eight production-tested skills for learning, exam prep, engineering projects, content and team operations: each one a written specification with explicit triggers, an ordered workflow, quality gates and fixed output rules, so an agent runs a defined process instead of improvising.

[![CI](https://github.com/omar-issam-abdelhalim/ai-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/omar-issam-abdelhalim/ai-skills/actions/workflows/ci.yml)
![Skills](https://img.shields.io/badge/skills-8-blue?style=flat-square)
![Format](https://img.shields.io/badge/format-Agent_Skills_(SKILL.md)-orange?style=flat-square)
![Version](https://img.shields.io/badge/version-1.0.0-lightgrey?style=flat-square)
[![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

</div>

---

## Contents

- [Why skills, not prompts](#why-skills-not-prompts)
- [The skills](#the-skills)
- [Install](#install)
- [Repository layout](#repository-layout)
- [How a skill is built](#how-a-skill-is-built)
- [Quality and testing](#quality-and-testing)
- [Contributing](#contributing)
- [License](#license)

---

## Why skills, not prompts

A prompt maps an instruction straight to an output. A skill puts a defined process, and a review pass, between the request and the response.

```
Prompt                          Skill
  │                               │
  ▼                               ▼
Instruction                   Trigger conditions   ← when it activates (and when it must not)
  │                               │
  ▼                               ▼
Output                        Ordered workflow     ← how it reasons, with human approval gates
                                  │
                                  ▼
                              Quality gates        ← scripts and checklists that fail loudly
                                  │
                                  ▼
                              Output rules         ← what the result must look like
```

Every skill here follows the open [Agent Skills](https://agentskills.io) format: a folder with a `SKILL.md` (YAML frontmatter + instructions), plus optional `references/`, `scripts/`, `assets/` and `templates/` that the agent loads only when a step needs them. That keeps the always-loaded context small and the detailed knowledge one file away.

---

## The skills

### Learning

| Skill | What it does | Highlights |
|---|---|---|
| [**article-mastery**](skills/article-mastery/SKILL.md) | Turns one article into a full one-on-one mastery lesson, not a summary. | Models the article's hidden assumptions, researches gaps, self-reviews before answering. |
| [**lecture-mastery**](skills/lecture-mastery/SKILL.md) | Teaches a lecture (PDF/PPTX/notes) to full mastery in parts, with checkpoints and a final mastery check. | Lecture-type playbooks (math, algorithms, code, conceptual), SymPy verification, goal/domain lenses, Arabic or English. |
| [**book-mastery**](skills/book-mastery/SKILL.md) | Session-by-session, research-level mastery of 900–2000 page technical books. | Persistent ledger (Notion or Markdown), spaced review, hint ladder, provenance tags, L1–L5 mastery ladder. |

### Exam prep

| Skill | What it does | Highlights |
|---|---|---|
| [**anki-lecture-cards**](skills/anki-lecture-cards/SKILL.md) | Turns study material into an importable Anki `.apkg`. | Deterministic deck and card IDs (re-imports never duplicate), exam-profile-aware card mix, card validator. |
| [**exam-lab**](skills/exam-lab/SKILL.md) | Builds an offline exam-prep app from lectures, sheets and past exams. | Matches the course's real question style, quality gates (answer-length cue, T/F balance, duplicates), timed mock exam. |

### Engineering

| Skill | What it does | Highlights |
|---|---|---|
| [**circuit-lab**](skills/circuit-lab/SKILL.md) | Takes an electronics course project from PDF to hand analysis, Proteus simulation, Tinkercad layout, physical build list and a viva learning pack. | Five gated phases, files-as-memory, KCL-based design checks, playbooks of real failure modes. |

### Content and operations

| Skill | What it does | Highlights |
|---|---|---|
| [**trend-content**](skills/trend-content/SKILL.md) | Turns the week's AI news into a researched, fact-checked carousel with a publish kit. | Scoring rubric, fact table with "who says it", adversarial critic pass, HTML slide system + PNG renderer. |
| [**meeting-report**](skills/meeting-report/SKILL.md) | Turns a transcript or notes into a decision-grade meeting report with running decision and action registers. | Decision vs proposal discipline, carry-over tracking, strict respectful-content rules, cross-meeting analysis. |

---

## Install

Any agent that supports the Agent Skills format can use these skills.

**With the `skills` CLI** (installs into the right folder for your agent):

```bash
# see what's in the repo
npx skills add omar-issam-abdelhalim/ai-skills --list

# install one skill
npx skills add omar-issam-abdelhalim/ai-skills --skill lecture-mastery

# install everything, globally
npx skills add omar-issam-abdelhalim/ai-skills --all -g
```

**Manually:** copy a folder from `skills/` into your agent's skills directory (the shared convention is `.agents/skills/<skill-name>/` in a project; check your agent's docs for its global path). For apps that take an upload, zip the skill folder and upload the `.zip`.

Skills activate on their own when a request matches their description; you don't need to name them. Some also accept a command (`/learn lec`, `/exam-lab`, `/circuit-lab`, `/trend-content`).

### Requirements per skill

| Skill | Needs |
|---|---|
| article-mastery | Web search + fetch |
| lecture-mastery | Python 3, `sympy`, `pdfplumber`; `pdftoppm` or `pypdfium2` for page images; `python-pptx` (+ LibreOffice for slide images) for PPTX |
| book-mastery | PDF tools; optional Notion integration (falls back to a Markdown ledger) |
| anki-lecture-cards | Python 3, `genanki` |
| exam-lab | Python 3, Node.js; Playwright for the smoke test |
| circuit-lab | Windows + Proteus 8, a local desktop-control agent, a browser agent, Tinkercad account |
| trend-content | Web search + fetch; Playwright for PNG export |
| meeting-report | A transcript (any speech-to-text) or notes; optional Drive/wiki integration |

---

## Repository layout

```
ai-skills/
├── skills/
│   ├── article-mastery/      SKILL.md
│   ├── lecture-mastery/      SKILL.md · references/ (playbooks, lens engine, mastery check) · scripts/
│   ├── book-mastery/         SKILL.md · references/hub-and-ledger.md
│   ├── anki-lecture-cards/   SKILL.md · references/card_rules.md · scripts/build_apkg.py
│   ├── exam-lab/             SKILL.md · assets/ (app template, example data) · scripts/ (build, check)
│   ├── circuit-lab/          SKILL.md · references/ (analysis, Proteus, Tinkercad) · templates/
│   ├── trend-content/        SKILL.md · references/ · assets/slide-base.html · scripts/render_slides.py
│   └── meeting-report/       SKILL.md · templates/config.md
├── scripts/validate_skills.py   repository-wide skill validator
├── tests/                       tests for every executable script
├── docs/AUTHORING.md            how skills in this repo are designed and written
└── .github/workflows/ci.yml     validation + tests on every push
```

---

## How a skill is built

Every skill follows the same design rules (full guide: [docs/AUTHORING.md](docs/AUTHORING.md)):

- **Specification over improvisation.** Purpose, triggers, workflow and output rules are written down, not left to how a request happens to be phrased.
- **Bounded triggers.** The description says when the skill activates *and* when it must not (e.g. `article-mastery` never fires on "tl;dr").
- **Human gates where mistakes are expensive.** Plans are approved before data is written; nothing is saved before the user has seen it.
- **Verification, not plausibility.** Math is checked with SymPy, code is run, numbers carry their source, generated artifacts pass scripted checks.
- **Honesty rules.** Inferences are labelled, unverified claims are marked, and no state is ever "remembered" without a verified source.
- **Progressive disclosure.** `SKILL.md` stays lean; detail lives in `references/` and is read only at the step that needs it.

---

## Quality and testing

```bash
pip install pyyaml pytest genanki sympy
python scripts/validate_skills.py   # frontmatter, naming, broken file references, leaked private data
pytest -q                           # tests for the Anki builder, math verifier, exam-lab kit
```

CI runs both on every push and pull request.

---

## Contributing

Issues and pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/AUTHORING.md](docs/AUTHORING.md) first; every change must pass the validator and tests.

See [CHANGELOG.md](CHANGELOG.md) for release history.

---

## License

[MIT](LICENSE) © 2026 Omar Issam
