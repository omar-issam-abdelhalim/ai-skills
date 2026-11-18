# Card Rules

Read this fully before writing any card. The goal is cards that build durable
understanding and match how the course is examined, not a paraphrase of the slides.

## Contents
1. Core principles (every card)
2. Type tags
3. Exam profiles (MCQ / Written / Mixed)
4. Math and formulas
5. Code and algorithms
6. HTML and the Extra field
7. Worked examples (bad → good)

---

## 1. Core principles

1. **Atomic.** One retrievable idea per card. If the answer contains two facts that
   could be forgotten independently, split it. Long answers get "half-remembered"
   and rated Good anyway, which silently destroys retention.
2. **Self-contained.** The card will appear months later, mixed with other courses.
   The front must be unambiguous on its own: put the needed context in the question
   ("In a first-order reaction, ...", "In a max-heap, ..."). Never write "according to
   the slide", "the above", "this method".
3. **Understanding over recall.** Prefer why / when / how / what-if / compare.
   Definitions only for terms the course actually requires, and phrase them so the
   learner must produce the meaning, not recognise wording.
4. **Short answers.** Back ideally one or two sentences. Supporting explanation
   belongs in Extra.
5. **No list cards.** Never ask "list the 5 X". For a set where membership matters,
   use one cloze note with each item as its own number (c1, c2, c3 ...), so each card
   tests one item with the others visible. For ordered steps, use Process cards
   ("In X, what step comes right after Y?").
6. **No yes/no questions.** They're 50% guessable. Turn "Does X change Y?" into
   "How does X affect Y, and why?"
7. **Faithful.** Content comes from the material. Standard, uncontroversial background
   needed to understand it is fine, but mark added clarification by putting it in
   Extra. Never invent facts, numbers, or examples that contradict the course.
8. **Course terminology.** Use the exact terms, symbols and notation of the course;
   exams use them.
9. **Source.** Fill `source` as `CODE · L03 · slide 12` (or page number) whenever
   the location is known, so the user can jump back to the material.

## 2. Type tags

Every card gets exactly one `Type::` tag:

| Tag | Tests |
|---|---|
| `Type::Concept` | what something is / its defining property |
| `Type::Why` | cause, justification, design reason |
| `Type::Compare` | the difference between two confusable things |
| `Type::Formula` | a formula, the meaning of its symbols, its units |
| `Type::Method` | which method/approach fits a given situation, and the cue |
| `Type::Condition` | when a rule/theorem applies, and when it fails |
| `Type::Process` | one transition in an ordered procedure |
| `Type::Trap` | a common mistake or misconception, and why it's wrong |
| `Type::Example` | applying a concept to a concrete small case |

Add topic tags only if the lecture has clearly distinct sub-topics
(e.g. `Topic::Kinetics`); keep them short and consistent.

## 3. Exam profiles

Choose one in Step 3 of SKILL.md and let it shape the mix of card types.
Core principles apply in every profile.

### MCQ
MCQ questions test fine discrimination between close options and exact details.
Emphasise:
- **Compare** cards for every pair of concepts a distractor could swap.
- **Trap** cards built from plausible-but-false statements:
  "Why is the claim '<false statement>' wrong?"
- Exact numbers, units, exceptions, edge cases, classifications
  ("Which category/class does X belong to, and what's the deciding feature?").
- If a sheet shows "Which of the following is NOT ...", create cards on the
  exceptions and boundaries of each category.

### Written / problem-solving
Written exams test producing explanations and solving problems.
Emphasise:
- **Method**: "What feature of the problem tells you to use X?"
- **Condition**: prerequisites of each theorem/law and when it breaks.
- **Formula** with symbol meanings and when it applies.
- **Process**: key steps of standard procedures, one transition per card.
- **Why**: the justifications a written answer must state.
- **Trap**: typical calculation/sign/unit errors.
Do not turn full worked solutions into cards; extract the decision points
("In <problem type>, what is the key first step?"). Tell the user in the final reply
that problem-solving itself still needs practice outside Anki.

### Mixed
Balance both profiles according to the content: detail-heavy parts lean MCQ,
procedural parts lean Written.

### Reading a sheet or past exam
When the user shares questions, analyse before writing: the proportion of question
types, the level (recall vs application vs analysis), recurring traps, and the
notation they use. Mirror that distribution. Mention the analysis in one or two
lines in the final reply.

## 4. Math and formulas

- Use MathJax only: inline `\( ... \)`, display `\[ ... \]`. Never `$...$`
  (Anki does not render it by default).
- In the JSON spec, backslashes must be escaped: write `"\\( E = mc^2 \\)"`.
- Do not put cloze deletions inside MathJax: `}}` in LaTeX closes the cloze early.
  Use basic cards for formulas.
- Formula card pattern: front asks for the formula in words ("What is the rate law
  for a first-order reaction?"), back gives the formula, Extra defines each symbol
  and its units. Add the reverse ("What does \( ... \) compute?") only for formulas
  that are easily confused.
- For theorems: one Condition card (hypotheses) + one Concept card (conclusion) +
  a Trap card if a hypothesis is commonly forgotten.

## 5. Code and algorithms

- Wrap code in `<pre><code> ... </code></pre>` and escape `<`, `>`, `&` as
  `&lt;`, `&gt;`, `&amp;`.
- Good targets: complexity *with the reason*, invariants, when to prefer one data
  structure/algorithm over another, and short traces on tiny inputs
  ("After the first pass of bubble sort on [3,1,2], what is the array?").
- Never ask the learner to reproduce a long block of code from memory.

## 6. HTML and the Extra field

- Fields are HTML: `<b>` sparingly for the key term, `<br>` for line breaks,
  `<ul><li>` on Back only when unavoidable. No markdown.
- Front, Back and cloze text: English.
- Extra: optional intuition, analogy, or "why it matters", in the learner's preferred
  language (for Arabic speakers: Arabic, with technical terms kept in English). Use it only when it adds understanding; it must not
  be a translation of Back.

## 7. Worked examples

**Too many facts on one card**
Bad: "What is a catalyst?" → "A substance that speeds up a reaction without being
consumed; it lowers activation energy via an alternative pathway and doesn't change
equilibrium."
Good (three notes):
- Concept: "How does a catalyst increase reaction rate?" → "It provides an
  alternative pathway with a lower activation energy."
- Trap: "How does a catalyst affect the position of equilibrium, and why?" → "It
  doesn't shift it: it lowers Ea for both forward and reverse reactions equally, so
  equilibrium is reached faster but not moved."
- Cloze: "A catalyst is {{c1::not consumed}} by the reaction it speeds up."

**Context missing**
Bad: "What is the complexity of this method?"
Good: "What is the average-case time complexity of quicksort, and why?" →
"\( O(n \log n) \): balanced partitions give about \( \log n \) levels, each
doing \( O(n) \) work."

**Method card (math)**
"In an integral of a product of a polynomial and \( e^x \), which technique fits,
and what do you choose as \( u \)?" → "Integration by parts, with \( u \) = the
polynomial (it simplifies when differentiated)."

**Condition card (math)**
"What must hold for the Mean Value Theorem to apply to \( f \) on \( [a,b] \)?" →
"\( f \) continuous on \( [a,b] \) and differentiable on \( (a,b) \)."
