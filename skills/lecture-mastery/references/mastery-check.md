# Checkpoints, grading, Final Mastery Check, and Consolidation

## 1. Part checkpoints

At the end of every part: 2–4 questions, no answers shown.

- At least one **recall** (define, state, reproduce) and at least one **"why"** (why is this step valid, why does this fail, why choose this).
- At least one **application** in exam shape when the part has problem types.
- A **lens transfer** question when a lens is active and the part has Direct concepts.
- Target the part's hotspots — the checkpoint should expose the misconceptions most likely to exist.
- Close with one line: answer here, or say "continue" / "كمل".

## 2. Grading the user's answers

Grade like a demanding, fair examiner who wants the student to become excellent:

1. **Verdict per question:** correct / partially correct / incorrect. No inflated praise; "correct" means correct.
2. **What's right** — briefly, specifically.
3. **What's wrong or missing** — name the exact misconception or missing step, not "needs more detail".
4. **Repair** — a targeted re-explanation from a *different angle* than the original teaching (the original angle already didn't land). Then a quick follow-up question on the same point if the gap was serious.
5. **Record the weak point** for the Consolidation.

For math, check the user's numbers with `verify_math.py`; for code, run their code. For Feynman explanations, grade on: correctness, completeness of the core mechanism, precision of terms, and whether the explanation would actually let a novice understand.

After grading, continue with the next part in the same reply (unless a serious gap requires re-teaching first).

## 3. Final Mastery Check

After the last part. Components, in order:

1. **Quiz** — 6–10 multiple-choice questions across the whole lecture with strong distractors (each distractor = a real misconception). If the interactive quiz tool is available, use it; otherwise write the questions and ask for answers.
2. **Open problems** — a ladder: recall → application (exam shape) → transfer (a situation not seen in the session). Include any checkpoint questions the user skipped.
3. **Feynman prompt** — "Explain [the lecture's central idea] in five sentences to someone who knows [prerequisite level] but hasn't seen this lecture."
4. **Lens challenge** (if a lens) — one realistic problem from the lens world that requires combining two or more concepts from the lecture.

Ask the user to answer; grade with §2 when they respond.

## 4. Consolidation (after grading the Mastery Check)

Delivered in chat. Template:

1. **The lecture in one paragraph** — the central problem and how the lecture solves it.
2. **Cheat sheet** — one screen: key definitions (precise, one line each), formulas (display math), algorithms/code patterns, decision rules. Nothing that wasn't taught.
3. **Concept list** — every concept with a one-line definition and its slide range. This list is intentionally clean and complete so that any follow-up in the same chat (flashcards, revision) can build on it.
4. **Your weak points** — every mistake and gap from this session's checkpoints and mastery check, each with the corrected understanding in one or two lines.
5. **Exam radar** — the problem types and derivations to be able to produce on demand.
6. **Next through the lens** (if a lens) — 2–4 concrete next steps: what to learn or build next that uses this lecture, with why each one matters for the role.

Do not invoke other skills. End after the Consolidation.
