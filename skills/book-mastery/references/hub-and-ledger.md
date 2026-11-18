# Hub and Ledger Reference

Everything in the ledger is written in **English**, whatever the session language flag is.

**Two backends, one schema.** With Notion, the Hub is a page and each table below is a child database. Without Notion, the Hub is `ledger/hub.md` and each database is a Markdown table in its own file (`ledger/sessions.md`, `ledger/weak-points.md`, `ledger/exercises.md`, `ledger/missed-questions.md`, `ledger/assumptions.md`), with relations written as the related row's name. Everything below applies to both; "row", "page" and "database" mean the equivalent Markdown construct in the file backend.

## Contents
1. Book Hub structure
2. Databases and properties
3. Session page template
4. Chat ledger format
5. Write rules and failure handling

---

## 1. Book Hub structure

One Hub page per book, created in Session 0 after the learner approves the content. Title: `<Book short name> | Hub`.

Sections on the Hub page:

- **Source Inventory:** each file, type, page count, text-layer status, and the printed-to-PDF page offset (with the pages checked to derive it).
- **Book Model:** thesis or purpose, audience, structure, chapter roles. Each statement has a status: `Preliminary` or `Confirmed (session <range>)`.
- **Dependency Map:** chapter dependencies and the suggested reading order. Unclear links are written as "unclear, verify in chapter N".
- **Goals:** the learner's stated goals and target depth, as stated.
- **Coverage Map:** one row per chapter with three columns: Read, Implement, Research. Each is `not started`, `in progress (pp. x-y)`, `done`, or `skipped on purpose (reason)`.
- **Glossary and Notation Table:** terms and symbols with first-use page, the book's meaning, and notes on notation that changes between chapters.
- **Assumption Log:** open assumptions (see database below).
- **Weak Points Tracker** (database)
- **Exercise Tracker** (database)
- **Sessions** (database)
- **Papers:** linked papers and the chapter each relates to, with how (motivates, extends, critiques).

## 2. Databases and properties

### Sessions
| Property | Type | Notes |
|---|---|---|
| Name | title | The page range, e.g. `63-96`. Implement and Research sessions: `Ch4 Implement`, `Ch4 Research` |
| Type | select | Read / Implement / Research |
| Pages (printed) | text | e.g. 63-96 |
| Date | date | |
| Language flag | select | AR / ENGL |
| Target levels | multi-select | L1 to L5 |
| Status | select | complete / partial (stopped at p. N) |
| Ledger version | number | |

### Weak Points
| Property | Type | Notes |
|---|---|---|
| Name | title | Short description, e.g. "Jacobian of a vector-valued softmax" |
| Status | select | open / improving / resolved |
| Topic pages | text | where the idea lives in the book |
| Error type | select | concept / algebra / notation / misread / proof gap |
| First seen | relation | Session |
| Evidence | text | what actually went wrong, from the chat |
| Resolved by | text | the problem solved unaided in a later session |

A weak point becomes `resolved` only when the learner solves a different problem on the same idea unaided, in a different session than the one where it was found.

### Exercise Tracker
| Property | Type | Notes |
|---|---|---|
| ID | title | e.g. `4.7` |
| Type | select | computational / proof / coding / conceptual |
| Priority | select | must-do / stretch / skip (skip needs a stated reason and learner approval) |
| Status | select | not attempted / attempted / solved unaided / solved with hints / failed |
| Lowest hint level | select | none / nudge / outline / next step / full solution |
| Error type | select | concept / algebra / notation / misread / proof gap |
| Linked weak point | relation | |
| Last reviewed | date | used for spaced review |
| Verified by | text | sympy, numerical check, solutions manual (and whether the manual agreed) |

### Missed Questions (spaced review pool)
Questions the learner got wrong in sessions or reviews.
| Property | Type | Notes |
|---|---|---|
| Question | title | |
| Learner's answer | text | |
| Correct answer | text | |
| Why it went wrong | text | |
| Error type | select | concept / algebra / notation / misread / proof gap |
| Source session | relation | |
| Times reviewed | number | |
| Last result | select | correct / wrong / hint needed |
| Last reviewed | date | |

### Assumption Log
| Property | Type | Notes |
|---|---|---|
| Assumption | title | |
| Why it was needed | text | |
| Status | select | open / confirmed / refuted |
| Resolved in | relation | Session |

## 3. Session page template

Page title is the page range. Content, in this order:

1. **Properties** (above)
2. **Session Recap** (the seven sections from SKILL.md, in order)
3. **Coverage manifest:** table with item, type, triage class (load-bearing / supporting / peripheral / skip), outcome (covered / brief / skipped), reason if skipped
4. **Concepts:** mastered versus shaky, based on observed performance
5. **Missed questions:** question, learner's answer, correct answer, why, error type
6. **Exercises this session:** ID, status, lowest hint level
7. **Verification log:** what was checked by code and the result; what was not verified
8. **Next session starts at**

## 4. Chat ledger format

Printed in chat at the end of every session. Fixed header on the first line:

```
LEDGER | <Book short name> | pp. <start>-<end> | v<N>
```

Then, in English:

```
Page offset: printed p. X = PDF p. Y
Covered: <ranges>  | Skipped on purpose: <ranges + reason> | Not covered: <ranges>
Last session: <range>, <date>, type <Read/Implement/Research>, flag <AR/ENGL>
Next starts at: p. N, first review item: <item>

Open weak points:
- <name> | status | error type | pages
Open assumptions:
- <assumption> | why needed
Exercises needing review:
- <ID> | status | lowest hint level
Missed questions for review:
- <short question> | last result
Glossary/notation changes this session:
- <term or symbol>: <meaning, page>
```

This block must contain enough to continue without the persistent store.

## 5. Write rules and failure handling

- Create the Hub only after the learner has approved the content shown in Session 0.
- In every later session, show the diff first, then write. Never write changes the learner has not seen.
- Prefer updating existing rows (status changes) over creating duplicates. Search the databases before creating a row.
- Never edit or delete anything the learner has changed by hand in the ledger. If the stored content differs from your expectation, the stored content wins. Say what you noticed and ask.
- If a write fails, retry once. If it still fails, state that plainly, print the ledger in chat, and tell the learner that the chat ledger is the record until the store works again.
- If the Hub cannot be found, search the store by the Hub title. If it still is not found, say so and ask for the link. Never silently create a second Hub.
