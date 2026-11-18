# Course memory — linking lectures across sessions

Each lecture is usually studied in a new session. When the environment can search earlier sessions of the same course (for example, a per-course project with past-conversation search, or a notes folder the agent can read), earlier `lecture-mastery` sessions become retrievable. Do not rely on a scratch filesystem for continuity unless you know it persists between sessions.

## When

At the start, after ingesting the lecture and before the diagnosis — only when earlier sessions are searchable. Otherwise, skip silently.

## How

1. Identify the course and a few distinctive concept names from the current lecture and its prerequisites.
2. Run 1–3 short content searches over past sessions (course code, prerequisite concept names, "Consolidation" / "weak points"). Keep it to a few searches.
3. If a past `lecture-mastery` session is found, open at most one or two, preferring their Consolidation section (concept list and weak points).

## What to extract

- Concepts already taught → link to them instead of re-teaching from zero ("in L3 we built the chain rule; here it becomes…"). Still give a one-line refresher when used.
- Weak points recorded earlier → if a weak point is a prerequisite here, bridge it deliberately and add a checkpoint question on it.
- Language and lens always come from the current command, never from history. History is used only for content links and weak points.

## Rules

- Attribute correctly: earlier explanations were the tutor's; the user's answers and mistakes were theirs.
- Do not paste old content; connect to it.
- If searches return nothing useful, proceed without mentioning it.
