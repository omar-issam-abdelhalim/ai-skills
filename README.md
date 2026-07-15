<div align="center">

# AI-Skills

**Engineered reasoning specifications for AI agents.**

A repository of AI Skills: each one a written specification defining a purpose, explicit trigger conditions, an ordered reasoning workflow, and fixed output rules — so an agent executes a defined process instead of improvising an answer.

![Skills Implemented](https://img.shields.io/badge/Skills_Implemented-1-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen?style=flat-square)
![Spec Format](https://img.shields.io/badge/Spec_Format-SKILL.md-orange?style=flat-square)
![Model Agnostic](https://img.shields.io/badge/Design-Model_Agnostic-9cf?style=flat-square)
![Version](https://img.shields.io/badge/Version-v0.1.0-lightgrey?style=flat-square)

</div>

---

## Table of Contents

- [What This Repository Is](#what-this-repository-is)
- [Repository Structure](#repository-structure)
- [Skill Specification Format](#skill-specification-format)
- [Skills Index](#skills-index)
- [Using a Claude Skill](#using-a-claude-skill)
- [Using a GPT](#using-a-gpt)
- [Adding a New Skill](#adding-a-new-skill)
- [Design Principles](#design-principles)
- [Contributing](#contributing)
- [A Note on This Documentation](#a-note-on-this-documentation)
- [License](#license)

---

## What This Repository Is

A skill, as built here, is a formal specification. It defines a stated purpose, explicit trigger conditions, an ordered reasoning workflow, and fixed output rules, so a model executes a defined process rather than reconstructing behavior from memory each time it's asked to do something similar.

The specification is what's designed and owned here — it is model-agnostic by intent. A given skill may then be *implemented* on more than one platform (for example, as a Claude Skill file, or as a GPT in ChatGPT). Those implementations are runtimes for the same underlying design, not separate skills to design independently — see [Skills Index](#skills-index) for what exists per skill, and where.

**Current version:** `v0.1.0`

This repository contains **one designed skill** ([`article-mastery`](#skills-index)). More will be added as they're actually built and validated — this README is updated to match what exists, not ahead of it.

### Specification vs. Instruction

```
Prompt                          Skill
  │                                │
  ▼                                ▼
Instruction                  Specification
  │                                │
  ▼                                ▼
Output                         Workflow
                                    │
                                    ▼
                               Self Review
                                    │
                                    ▼
                                 Output
```

A prompt maps an instruction directly to an output. A skill inserts a defined process — and a review pass — between the request and the response.

---

## Repository Structure

```
AI-Skills/
├── skills/
│   └── article-mastery/
│       └── SKILL.md
└── README.md
```

Skills live under `skills/` from the start, even with a single skill implemented today — so the structure doesn't need to be reorganized as more are added. Anything not shown above does not currently exist in this repository.

---

## Skill Specification Format

Every skill in this repository is written first as a single `SKILL.md` file — the master specification — with two parts:

**1. YAML frontmatter** — machine-readable metadata:
```yaml
---
name: skill-name
description: >
  What the skill does, and — critically — the trigger conditions:
  the phrasings and contexts that should activate it, and just as
  important, the ones that should NOT.
---
```

**2. Markdown body** — the specification itself, structured as:
- **Inputs** — what's required from the user, and what should be inferred rather than asked
- **Ordered workflow steps** — named stages of reasoning executed in sequence, not "think step by step" left to interpretation
- **Output rules** — exact expectations for language, structure, and tone
- A **self-review pass** before the output is finalized, checked against explicit criteria

This `SKILL.md` is the source a platform-specific implementation is built from — see [Using a Claude Skill](#using-a-claude-skill) and [Using a GPT](#using-a-gpt) for how it's actually run.

### Execution Flow

```
User Request
      │
      ▼
Trigger Conditions
      │
      ▼
Reasoning Workflow
      │
      ▼
Output Contract
      │
      ▼
Self Review
      │
      ▼
Final Response
```

This defines executable reasoning behavior through a formal specification: trigger conditions bound *when* it activates, the workflow bounds *how* it reasons, and the output rules bound *what* the result looks like — all three written down, not implicit.

---

## Skills Index

The only section of this README expected to keep growing. Each skill lists what it does, once, and every implementation currently available for it.

### 1. Article Mastery

Converts a single article into a full one-on-one mastery lesson — not a summary — deep enough that the reader could explain, defend, and apply it without going back to the source.

| Implementation | Access |
|---|---|
| Claude Skill (`SKILL.md`) | [View file](./skills/article-mastery/SKILL.md) |
| GPT (ChatGPT) | 🔜 Soon |

**Status:** Implemented

---

## Using a Claude Skill

1. In Claude, go to **Settings → Capabilities** and enable **Code execution and file creation** — Skills require it to run.
2. Go to **Customize → Skills**.
3. Click **"+"**, then either **"Upload a skill"** (a `.zip` of the skill folder) or **"Create skill"** to add it directly.
4. Toggle it on. Claude invokes it automatically once your request matches its trigger conditions — you don't need to name it.

Official sources:
- Anthropic — [Introducing Agent Skills](https://claude.com/blog/skills)
- Anthropic Engineering — [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- Claude Help Center — [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- Claude Help Center — [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

---

## Using a GPT

1. Open the GPT's link, listed per skill in the [Skills Index](#skills-index) once available.
2. Sign in to ChatGPT if prompted.
3. Send a message — the GPT already carries the skill's configured instructions, so it applies them automatically. No extra setup needed.
4. You can find any GPT you've opened before under **Explore GPTs**, or bring it into an existing chat by typing `@` followed by its name.

Official source:
- OpenAI Help Center — [GPTs in ChatGPT](https://help.openai.com/en/articles/8554407-gpts-in-chatgpt)

---

## Adding a New Skill

1. Create `skills/<skill-name>/SKILL.md` following the [Skill Specification Format](#skill-specification-format) above — frontmatter, inputs, ordered workflow, output rules, self-review. This is the master definition every implementation is built from.
2. Build whichever implementation(s) you actually have (a Claude Skill file, a GPT, or both). It's fine to ship one first and add the other later.
3. Add a new block to the [Skills Index](#skills-index): a one-line description, and a small table listing each implementation and its access link (or "Soon" if still in progress).
4. Nothing else in this README needs to change. If it does, that's a sign the new entry is inconsistent with the existing format — fix the entry, not the README.

---

## Design Principles

- **Specification over improvisation.** Behavior is defined in writing — purpose, triggers, workflow, output rules — not left to how a request happens to be phrased in the moment.
- **One specification, many implementations.** The reasoning design lives in a single `SKILL.md`. A Claude Skill file or a GPT are different runtimes for that same design, not separate things to maintain independently.
- **Depth over compression.** Where the default model behavior is to summarize, a skill can explicitly instruct it to do the opposite when that's the actual goal.
- **Bounded trigger conditions.** A skill states clearly not just when it should activate, but when it deliberately should not — precision about scope is part of the design, not an afterthought.
- **Self-review as part of the workflow, not an add-on.** The last step of the process is checking the output against explicit criteria before it's considered done.
- **Single source of truth.** A skill's details live in its own file once. The README indexes; it does not duplicate.

---

## Contributing

This is currently a single-author project in early, active development. There's no formal contribution process in place yet — that will be added once there's more than one skill to establish a pattern from. If you want to suggest something, opening an issue is the right way to start a conversation.

---

## A Note on This Documentation

This repository reflects the current implementation. Documentation evolves alongside the skills — features are documented only after they exist.

---

## License

No license file has been added to this repository yet. Until one is added, standard copyright applies by default — all rights reserved. A license (e.g. MIT) will be added once the project reaches a state intended for open reuse.
