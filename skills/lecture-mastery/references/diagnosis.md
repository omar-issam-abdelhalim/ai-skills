# Diagnosis — understand the lecture before teaching it

The diagnosis is the most important phase. Every later decision (order, strategy, depth, part boundaries, lens tiers) comes from it. Do it fully and internally; the user sees its results in the Lecture Map, not the raw analysis.

## 1. Identity and position

- **Course and topic.** Infer from the title slide, headers, course code, terminology. If uncertain, say so in the Map.
- **Position in the curriculum.** Lecture number if shown. Otherwise infer from what is assumed vs. introduced: anything used without definition is a prerequisite; anything defined is new.
- **Before and after.** What this lecture builds on, and what it sets up. Naming the next step gives the user a reason for the current one ("this is the machinery that backprop will use next week").

## 2. Lecture type

Classify each section, not just the whole lecture. Signals:

| Type | Signals |
|---|---|
| Mathematical | Definitions → theorems → proofs/derivations, many equations, worked examples with symbols |
| Algorithmic | Pseudocode, step-by-step procedures, complexity analysis, traces, data-structure diagrams |
| Programming / code | Code snippets, syntax, APIs, outputs, errors, lab instructions |
| Conceptual / theory / design | Frameworks, comparisons, architectures, tradeoffs, case studies, few equations |
| Memorization-heavy | Long lists, classifications, terminology, facts, dates, anatomy-style content |

Most lectures are mixed. Record the type per concept so the right playbook drives each one.

## 3. Concept inventory

List every concept, definition, theorem, method, formula, algorithm, and example in the material. For each, note:

- Slide range
- Whether it is **major** (central, many things depend on it, likely examined) or **minor** (supporting detail)
- What the slides actually give (definition only? example? derivation? just a name?)

Nothing in the lecture is dropped. Minor concepts still get taught — with less room, not less correctness.

## 4. Dependency graph

For each concept, what must be understood first? Build the graph and derive a teaching order via topological order. When slide order differs:

- Follow the dependency order, and reference slide numbers so the user can map back.
- If the lecturer deliberately motivates with an example before the definition, keep that — motivation-first is a valid dependency, not a violation.

Group concepts into **parts** along the graph: each part is a connected cluster (2–4 concepts) that can be taught fully in one reply. Heavy concepts may be a part of their own.

## 5. Difficulty hotspots

Where will understanding actually break? Look for:

- Steps the slides skip ("it follows that…", "similarly…", "clearly…")
- Notation overload, or notation that changes mid-lecture
- Concepts that contradict intuition
- Places where two similar concepts are easy to confuse
- Classic misconceptions of this topic (use your knowledge of how students typically fail here)

Hotspots get extra room, an extra example, and a checkpoint question.

## 6. Prerequisites and gaps

- List every prerequisite the lecture assumes.
- Decide which ones need a **bridge**: a short, complete mini-lesson placed right before the concept that needs it (not all at the start). A bridge must itself obey the no-gap rule.
- If course memory shows the user struggled with a prerequisite before, bridge it even if it seems basic.

## 7. Slide quality

- **Errors:** wrong formulas, sign errors, off-by-one, incorrect claims. Verify before flagging.
- **Missing steps:** derivations with jumps; definitions used before they are given.
- **Ambiguity:** undefined symbols, overloaded notation.

All go under `⚠️ Slide note` in the relevant spot.

## 8. Exam signal

Mastery includes the exam. Note:

- Definitions stated formally (often asked verbatim or as "define and explain")
- Derivations shown in full (often asked to reproduce)
- Worked-example patterns (the problem types to master)
- Anything the slides emphasize: "important", "note", boxes, repetition, summary slides
- Standard exam problem types for this topic in university courses

Every exam-relevant item must be covered with at least one worked example of exam shape.

## 9. Lens relevance (only if a lens is given)

Tier each concept Direct / Indirect / Foundational only (see `lens-engine.md`). Decide where the lens exercise of each part will come from.

## Output of the diagnosis

The diagnosis produces the Lecture Map (SKILL.md §6). Keep the Map compact and useful: the user should see the shape of the whole lecture in under a minute of reading.
