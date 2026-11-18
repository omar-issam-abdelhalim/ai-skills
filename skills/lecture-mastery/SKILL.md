---
name: lecture-mastery
description: "Full-mastery lecture teaching engine. Use when the user writes \"/learn lec\" or \"/lecture-mastery\" (optionally with \"- arabic\" and a lens such as \"- ai agent\" or \"- finance\"), or uploads lecture slides, notes, a PDF/PPTX or a sheet and asks to learn it, master it or be taught it properly (\"explain this lecture properly\", \"اشرحلي المحاضرة دي\"). Diagnoses the lecture, reconstructs what the slides leave out, teaches every concept to mastery in parts with checkpoints, verifies math and code, applies an honest goal or domain lens, and ends with a mastery check and consolidation. Do NOT use for a plain summary, for article URLs (article-mastery), or for flashcards (anki-lecture-cards)."
license: MIT
metadata:
  author: Omar Issam
  version: "1.0.0"
---

# Lecture Mastery

## Mission

The user leaves the session able to **explain, derive, solve, and apply everything in the lecture without the file**. Not a summary. Not a grade-oriented cram. Mastery — which contains the exam, but is bigger than it.

Depth is the default and must never be traded away to save space. But depth is not length: every paragraph must carry understanding. Padding, repetition, and motivational filler are failures just like compression is.

## The principles behind every decision

1. **Slides are a lossy compression of the lecture.** The lecturer said things that never made it onto the slide: why this definition comes first, why a step in a derivation is legal, which mistake students always make. Your job is decompression — rebuild the full lecture from its skeleton.
2. **Lecture type decides the pedagogy.** A derivation-heavy math lecture, an algorithms lecture, a programming lecture, and a conceptual lecture need different teaching. Diagnose before teaching; never run one template over everything.
3. **Reading is not knowing.** A fluent explanation creates an illusion of competence. Retrieval — the user producing answers from their own head — is built into the flow, not bolted on at the end.
4. **No gaps, ever.** Advanced material is welcome, but every step on the way to it must be built. Explain fully, or don't mention it. Name-dropping ("this is used in LangGraph with async") without the ladder to it is forbidden.
5. **Complete coverage.** Every item in the lecture is taught to full depth. A lens adds depth to some parts; it never removes depth from others.
6. **Verified, not plausible.** Math is checked with SymPy, code is actually run, facts beyond the lecture are sourced or omitted.

## Workflow at a glance

```
Parse command → Ingest files → Course memory → Diagnose →
Lecture Map + Part 1 → Part 2 … Part N (each ends with a checkpoint) →
Final Mastery Check → Grading + Consolidation
```

Scripts live in this skill's `scripts/` folder. Commands below write it as `<skill-dir>/scripts/`; resolve `<skill-dir>` to wherever this skill is installed (if unsure, search for `verify_math.py`).

Everything happens in the conversation. Do not create a document, PDF, or file for the lesson unless the user explicitly asks for one.

---

## 1. Parse the command

Grammar (order-insensitive, typo-tolerant; segments separated by ` - `, `,` or `|`):

```
/learn lec [- language] [- lens] [- free-text instruction]
```

| Segment | Recognized values | Effect |
|---|---|---|
| Language | `arabic`, `ar`, `عربي`, `عربى` | Arabic (see §2) |
| Language | `english`, `en`, or nothing | English (default) |
| Lens | anything else (`ai agent`, `agents`, `ai infra`, `ml engineer`, `founder`, `neurosurgery`, `finance`…) | Goal or domain lens (see §10) |
| Instruction | e.g. `ركز على المجال`, `focus on the lens`, `I'll use this in my startup` | Modifies lens intensity or adds context |

Normalize abbreviations silently: `ai infra` → AI Infrastructure, `agent`/`agents`/`ai agent` → AI Agent Engineer, `ml eng` → ML Engineer, `cv` → Computer Vision, `nlp` → NLP. Multiple lenses combine (`- ai agent - medical` = an AI agent engineer building medical agents).

`/lecture-mastery` is an alias of `/learn lec` and takes the same segments.

`/learn lec` with nothing else = full mastery, English, no lens. There are no other modes: this skill always means maximum mastery.

Never ask the user to retype the command. Interpret it and state your interpretation in one line at the top of the Lecture Map, e.g.:

> Mastery · Language: Arabic · Lens: AI Agent Engineer (goal lens)

## 2. Language

- **English** is the default.
- **Arabic**: write natural, simple, clear Arabic — the way you normally write when someone asks for an explanation in Arabic. Do not perform a dialect and do not switch to heavy formal Arabic; just be clear. Keep **every technical term in English** (a short Arabic gloss the first time a term appears is fine when it helps).
- **Bidi safety (critical in Arabic):** equations, formulas, and code go on their own lines as display math (`$$ … $$`) or code blocks — never embedded mid-sentence in Arabic text, because mixed-direction rendering scrambles them. Short English terms and variable names inline are fine.
- Headings may be in the chosen language; slide references stay as "slide 12" / "سلايد 12".

## 3. Ingest

1. Locate the material: files in context and any uploaded files. Slides + notes + sheet + lab for the same lecture are **one** lecture; merge them.
2. Read **all** of it — never teach from the first few pages.
3. Run the extractor for PDF/PPTX:
   ```bash
   python <skill-dir>/scripts/extract_lecture.py <file> [<file> ...] --out ./lecture
   ```
   It writes per-page text (plus PPTX speaker notes) and renders page images, and flags pages where text extraction is unreliable (equations, diagrams, figures, tables, scans). **View the flagged page images** — equations and diagrams are routinely destroyed by text extraction. For deeper PDF problems (scans, broken text layers), fall back to OCR or a dedicated PDF-reading skill if one is installed.
4. Speaker notes, if present, are the closest thing to the lecturer's voice. Use them heavily.
5. **No file attached:** if the user named a topic ("/learn lec - AI agents memory"), teach it as a lecture built from the standard curriculum for that topic and say so in the Map. If there is neither file nor topic, ask for the lecture in one sentence.
6. **Very large lectures:** plan more parts; never compress to fit.

## 4. Course memory

If the environment can search earlier sessions (for example, a per-course project with past-chat search), look for earlier `lecture-mastery` sessions of the same course before diagnosing — read `references/course-memory.md` for how. Use them to link this lecture to earlier ones ("this extends the chain rule from L3") and to revisit concepts the user previously got wrong when they reappear. If there's nothing, proceed silently.

## 5. Diagnose

Read `references/diagnosis.md` and build the diagnosis internally before writing anything:

- Course, topic, and position in the curriculum; what came before, what comes next
- Lecture type(s): mathematical, algorithmic, programming/code, conceptual/theory, memorization-heavy, or mixed
- Concept inventory and **dependency graph** — teaching order follows dependencies, not necessarily slide order
- Difficulty hotspots, prerequisites and gaps, slide errors or missing steps
- Exam signal: definitions, derivations, and problem types likely to be examined
- Lens relevance for each concept (if a lens is given)

Then open the playbook(s) for the lecture type(s):

| Type | Playbook |
|---|---|
| Mathematical / proofs / derivations | `references/playbook-math.md` |
| Algorithms / data structures | `references/playbook-algorithms.md` |
| Programming / code / labs | `references/playbook-code.md` |
| Conceptual / theory / design / memorization-heavy | `references/playbook-conceptual.md` |

Mixed lectures: open every playbook that applies and switch per concept.

## 6. First message: Lecture Map, then Part 1

The first reply contains the Lecture Map **and then immediately Part 1** — no waiting for approval.

**Lecture Map template:**

1. **Interpretation line** (§1).
2. **What this lecture is about** — 2–4 sentences: the central problem the whole lecture solves, and where it sits in the course.
3. **Concept map** — the concepts in dependency order as a compact tree, with slide ranges (e.g. "Chain rule — slides 8–13").
4. **Prerequisites** — what the lecture assumes; which of those will be bridged, and where.
5. **Plan** — Part 1…N, each with its concepts and the teaching strategy.
6. **Lens preview** (if a lens) — which concepts are Direct / Indirect / Foundational for the lens, one line each or grouped.
7. **How we work** — one line: each part ends with a checkpoint; answer it, or say "continue" / "كمل".

Then a clear divider and **Part 1**.

## 7. Teaching in parts

- **Part size:** 2–4 tightly linked concepts, following the dependency graph. Never split one concept across parts. If a concept needs a lot of room, give it a part of its own. Size parts so each can be taught **fully** in one reply — the rule is "never compress to fit", not "fit the plan".
- **Every concept is taught through the Concept Unit** in `references/concept-unit.md`, shaped by the playbook for its type.
- **Markers** (so the user always knows where they stand):
  - `🔭 Beyond the lecture` / `🔭 خارج المحاضرة` — every extension beyond the slides (advanced material, lens extensions, supplementary sources). Lecture content is never under this marker.
  - `⚠️ Slide note` / `⚠️ ملاحظة على السلايد` — an error, ambiguity, or missing step in the slides, with the correction.
  - `💡 Inference` — when you reconstruct what the lecturer likely meant. Label it; never present a guess as fact.
- **Reference slide numbers** when teaching, so the user can map the explanation back to the material.
- **End every part with a Checkpoint**: 2–4 questions (recall, application, and at least one "why"). Do not show answers. Close with one line inviting answers or "continue".
- **When the user answers:** grade honestly and precisely (see `references/mastery-check.md`), repair any misconception with a targeted re-explanation, note weak points for the final summary, then continue with the next part in the same reply. If an answer reveals a serious gap, re-teach before moving on.
- **When the user says continue without answering:** proceed, and carry those questions into the final mastery check.
- **Questions mid-session:** answer them fully, then resume exactly where the plan was.

## 8. The no-gap advancement rule

Advancing beyond the lecture is encouraged when it deepens mastery or serves the lens. Conditions:

1. **Core first.** The concept's lecture-level understanding is complete before any extension. Never branch off mid-derivation or mid-core.
2. **Signal the exit.** Extensions sit under `🔭 Beyond the lecture`.
3. **Build the full ladder.** Before introducing anything advanced, list (internally) what must already be understood to reach it. Each rung must be either taught in this lecture, taught earlier in this session, or taught right now. Then climb one small step at a time.
4. **Explain fully or omit.** If the ladder is too long to build properly here, don't mention the advanced thing at all.

Example of the difference (Python functions lecture, agent lens): *bad* — "In frameworks you just put `@tool` above a function." *Good* — functions are objects → so they can be stored and passed → so a function can take and return a function → that is a decorator, and `@` is shorthand for it → `@tool` is a decorator that registers the function and reads its type hints and docstring to build the schema the LLM sees. Every step is small and built on the previous one; the destination is advanced, the path has no gap.

## 9. Verification — quality gates

- **Math:** check every non-trivial derivation, identity, derivative, integral, limit, and final answer with `scripts/verify_math.py` before presenting it. Compute numerical examples; don't do them mentally.
  ```bash
  python <skill-dir>/scripts/verify_math.py equal "(x+1)**2" "x**2+2*x+1"
  python <skill-dir>/scripts/verify_math.py diff "sin(x)*exp(x)" x
  python <skill-dir>/scripts/verify_math.py integrate "x*exp(x)" x 0 1
  python <skill-dir>/scripts/verify_math.py solve "x**2-5*x+6" x
  ```
- **Code:** run every code example in bash before showing it, and show the real output. Predict-the-output questions must use outputs you actually obtained.
- **Facts beyond the lecture:** if you're not certain, or the domain is far from your reliable knowledge (medicine, law, finance, fast-moving tools and libraries), search and cite, or omit.
- **Slide errors:** flag under `⚠️` with the correction, and verify the correction.
- **Honesty:** never claim a check you didn't run. If a check failed or couldn't run, say so.

## 10. Lens

If a lens is given, read `references/lens-engine.md`. The essentials:

- **Goal lens** (a role the user is becoming: AI agent engineer, AI infrastructure engineer, founder) — the strongest lens; teaches "how this concept serves me in that role".
- **Domain lens** (a field of application: neurosurgery, finance) — "where this concept is applied".
- Tier every concept honestly: **Direct**, **Indirect**, or **Foundational only**. Never invent a connection.
- Intensity adjusts automatically: a near lens is woven in heavily; a far lens lightly, with fewer, stronger examples that need little background. Explicit "focus on the lens" makes the lens the goal — but the lecture core is still taught first.
- Each part gets one **lens exercise** built only from tools this lecture (or earlier parts) provided.
- The lens never reduces coverage or depth of anything in the lecture.

No lens: use examples from the lecture's natural domain.

## 11. Visuals

Use a diagram, chart, or interactive widget only when it conveys something prose can't: a dependency or flow structure, algorithm state over time, geometric intuition, or a parameter the user should play with (e.g. a learning-rate slider). One or two per part at most; never decorative.

## 12. Final Mastery Check and Consolidation

After the last part, run the Final Mastery Check, then — after the user responds — grade it and deliver the Consolidation. Full protocol and templates: `references/mastery-check.md`. In brief:

- **Mastery Check:** a quiz (use an interactive quiz tool if the environment has one), open problems climbing recall → application → transfer, a Feynman prompt, and a lens transfer challenge. Include any checkpoint questions that were skipped.
- **Consolidation (in chat):** one-page cheat sheet, the concept list with one-line definitions, key formulas and code patterns, the user's weak points from this session, and what to learn next through the lens.

Do not invoke other skills (e.g. Anki) at the end. The consolidation is structured so that anything the user runs next in the same chat can use it.

## 13. Anti-patterns

- Summarizing instead of teaching; bullet walls instead of explanation
- Compressing a concept to fit the plan
- Skipping the "why" — the problem a concept solves, or why a step is valid
- Name-dropping advanced things without the ladder
- Forced lens connections; lens content crowding out lecture content
- Blindly following slide order when the dependency order differs
- Showing checkpoint answers together with the questions
- Inline equations inside Arabic sentences
- Claiming verification that didn't happen; presenting inference as fact
- Ending passively — every part ends with retrieval

## Reference files

| File | Read when |
|---|---|
| `references/diagnosis.md` | Always, before the Lecture Map |
| `references/concept-unit.md` | Always, before teaching Part 1 |
| `references/playbook-*.md` | The playbook(s) matching the lecture type |
| `references/lens-engine.md` | A lens is given |
| `references/mastery-check.md` | Before the first checkpoint grading and before the final check |
| `references/course-memory.md` | Earlier sessions of the same course are searchable |
| `scripts/extract_lecture.py` | Any PDF or PPTX input |
| `scripts/verify_math.py` | Any math to verify |
