# Authoring guide

How skills in this repository are designed and written. Every new skill, and every change to an existing one, follows these rules.

## 1. Anatomy of a skill

```
skills/<skill-name>/
├── SKILL.md          required: frontmatter + the workflow
├── references/       optional: detail read only at the step that needs it
├── scripts/          optional: deterministic code the workflow runs
├── assets/           optional: templates and files copied into outputs
└── templates/        optional: file skeletons the workflow fills in
```

`SKILL.md` frontmatter uses only portable fields of the Agent Skills format:

```yaml
---
name: skill-name            # lowercase-hyphen, ≤ 64 chars, equals the folder name
description: "..."          # ≤ 1024 chars: what it does + when to use it + when NOT to
license: MIT
metadata:
  author: Omar Issam
  version: "1.0.0"
---
```

## 2. The description is the trigger

The agent decides whether to load a skill from its description alone, so the description carries three things:

1. **What it produces**, in one clause.
2. **When to use it**: the phrasings, commands and situations that should activate it, including the other languages users actually write in.
3. **When not to use it**: the neighbouring requests that belong to another skill or to no skill (`"Do NOT use for a plain summary"`).

## 3. The body is a workflow, not advice

- **Ordered steps.** Each step has an input, an action and an output. Later steps read earlier outputs, not chat history, when a workflow spans sessions ("files are the memory").
- **Gates.** Where a wrong guess is expensive (writing data, saving files, physical builds), the step ends with a stop and an explicit approval.
- **Quality gates.** A final check the agent runs against its own work: a script that exits non-zero, or a checklist written as yes/no questions.
- **Output rules.** What the deliverable looks like: language, format, structure, and what never appears in it.
- **Anti-patterns.** The specific failure modes this workflow exists to prevent, written down.

## 4. Keep `SKILL.md` lean

`SKILL.md` holds the workflow and the rules. Long material (rubrics, playbooks, schemas, worked examples) goes in `references/`, and the workflow names the exact step at which each file is read. Never load a reference "just in case".

## 5. Scripts over prose for anything deterministic

If a step can be done by code (building a file, validating data, verifying math, rendering images), ship a script and tell the agent to run it rather than reimplement it. Scripts:

- take paths as arguments, never hard-coded absolute paths;
- print a machine-readable summary (JSON or a fixed format);
- exit non-zero on failure;
- are covered by a test in `tests/`.

## 6. Honesty rules every skill inherits

- Never present an inference as a fact; label it.
- Never claim a check that did not run.
- Never invent names, numbers, dates, sources or state. If it is missing, say so.
- Separate what the source says from what the agent added.

## 7. Portability

- Refer to capabilities, not products: "a web-fetch tool", "a desktop-control agent", "a persistent store".
- Paths are relative to the skill (`<skill-dir>/scripts/...`) or the working directory.
- No personal data, private links, IDs or credentials in a skill. Team- or person-specific settings go in a config file the user fills in (see `meeting-report/templates/config.md`).

## 8. Before you open a pull request

```bash
python scripts/validate_skills.py
pytest -q
```

Both must pass. Add the skill to the README index and a line to `CHANGELOG.md`.
