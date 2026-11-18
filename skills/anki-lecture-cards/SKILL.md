---
name: anki-lecture-cards
description: "Turn a lecture, slides, notes, sheet or any study material into a ready-to-import Anki .apkg file whose cards always land in the right course deck with no duplicates. Use whenever the user uploads study material and asks for Anki cards or flashcards (\"anki\", \"flashcards\", \"اعمل كروت\"), or writes a course code with or without a lecture number (e.g. \"CHEM 101 L3\", \"Math 201 lecture 2\"), even if they never say Anki. Also use for Anki cards on a topic without a file (e.g. \"AI Agents\")."
license: MIT
metadata:
  author: Omar Issam
  version: "1.0.0"
---

# Anki Lecture Cards

The user studies a lecture, then sends the material here with a course code and a
lecture number. Produce excellent cards and deliver them as one `.apkg` built by
`scripts/build_apkg.py`.

The script is the contract with the user's Anki. It derives the deck ID from the
deck name, every card's GUID from its content, and uses two fixed note types
(`StudyPipeline Basic`, `StudyPipeline Cloze`) that persist in the user's
collection after the first import. Always build through this script and never write
your own genanki code: different IDs would create duplicate decks and note types in
the user's Anki.

Reply to the user in their language. If they write in Arabic, reply in clear Arabic and
keep technical terms in English.

## Step 1: Set up and read the material

```bash
pip install genanki  # add --break-system-packages on externally managed Python installs
```

Read the whole material before writing anything, including examples, exercises and
any practice questions, since those reveal the exam style. For PDFs, read the text
layer and render pages that contain equations, diagrams or tables as images, because
text extraction mangles them. For slides saved as images, look at them directly.

## Step 2: Resolve the deck and the lecture

From the user's message, take:

- **Deck key:** a course code such as `CHEM 101`, `math201` or `CS-301`, or a topic such
  as `AI Agents`. Pass it to the script exactly as written; the script normalises it
  (`chem 101` → `Uni::CHEM101`, `AI Agents` → `AI::Agents`). If the message has no code
  and the material is clearly a course lecture, ask for the code in one short question.
- **Lecture:** first from the message (`L3`, `lec 3`, `3`); otherwise from the material
  (title slide, header, file name like `Lec03.pdf`). If it is still unknown, ask one short
  question. Do not guess, because a wrong lecture tag is worse than none. For non-lecture
  material, pass values like `Sheet 2`, `Lab 1` or `Section 3`. Topic decks without
  lectures can omit it.
- **Course title:** infer it from the material for `deck_description`
  (e.g. `CHEM101 — General Chemistry I`). The description is not used for matching,
  so a best inference is fine; leave just the code if the title is unclear.

## Step 3: Determine the exam profile

Decide how this course is examined, in this order of evidence:

1. A question sheet, quiz or past exam anywhere in this conversation → analyse it and mirror it.
2. Questions or exercises inside the lecture itself.
3. The nature of the subject (e.g. calculus is problem-heavy; a descriptive course leans MCQ).
4. If nothing is conclusive, use **Mixed**.

The profiles (MCQ, Written, Mixed) and how each changes the card mix are defined in
`references/card_rules.md`.

## Step 4: Map the lecture before writing

Build a private map: core concepts, relationships, formulas, procedures,
conditions and exceptions, confusable pairs, examples, and likely exam traps.
Write cards from this map, not slide by slide. Slide-order paraphrasing produces
trivia cards and misses the connections that exams test.

## Step 5: Write the cards

Read `references/card_rules.md` in full first. It has the principles, the `Type::` tags,
the profile rules, MathJax/code conventions and worked examples.

Aim for complete coverage of every examinable idea with zero filler. That is usually
20–60 notes per lecture: more for dense theory or formula lectures, fewer for thin ones.
Never pad to reach a number.

## Step 6: Self-review

Before building, check every card against this list and fix what fails:

- Answerable from its front alone, months later, mixed with other courses?
- One idea only? If not, split it.
- No duplicates or near-duplicates?
- Every item in the lecture map covered?
- Card-type mix matches the chosen profile?
- MathJax uses `\( \)` / `\[ \]`, code is escaped, fields are HTML (no markdown)?
- Exactly one `Type::` tag per card, and `source` filled where the location is known?

## Step 7: Build

Write the spec to `spec.json` in your working directory:

```json
{
  "deck": "CHEM 101",
  "lecture": 3,
  "deck_description": "CHEM101 — General Chemistry I",
  "cards": [
    {"type": "basic",
     "front": "How does a catalyst increase reaction rate?",
     "back": "It provides an alternative pathway with a lower activation energy.",
     "extra": "Like taking a tunnel through the mountain instead of climbing over it.",
     "source": "CHEM101 · L03 · slide 14",
     "tags": ["Type::Concept"]},
    {"type": "cloze",
     "text": "A catalyst is {{c1::not consumed}} by the reaction it speeds up.",
     "source": "CHEM101 · L03 · slide 14",
     "tags": ["Type::Concept"]}
  ]
}
```

In JSON, escape MathJax backslashes: `"\\( k[A] \\)"`.

Then run:

```bash
python <skill-dir>/scripts/build_apkg.py spec.json outputs/
```

The script names the file itself (e.g. `CHEM101_L03.apkg`), adds the lecture and semester
tags automatically, and prints a JSON summary. If it prints `VALIDATION FAILED`, fix the
listed cards and rerun. Read every warning and fix the real problems before delivering.

## Step 8: Deliver

Hand the `.apkg` file to the user, then write a short reply in their language:

- The deck and lecture tag, and the note count broken down by `Type::`.
- The exam profile you chose and the evidence, in one line.
- Anything worth doing manually, e.g. key diagrams that suit Anki's built-in Image
  Occlusion (name the slides). For problem-heavy courses, a reminder that solving
  problems still needs practice outside Anki.
- One line on importing: double-click the file or use Import File.

Do not paste the cards into the chat, since the user reviews them in Anki.

## Special cases

- **Regenerating a lecture:** GUIDs come from the card text, so regenerating with
  different wording adds new notes that duplicate the old ones in meaning. If the user
  asks to redo a lecture, offer to generate only the missing cards instead. If they
  want a full replacement, tell them to first delete the old cards in Browse
  (search `tag:Uni::CHEM101::L03`, select all, delete), then import the new file.
- **Adding to a lecture already done:** keep the same deck key and lecture; write only
  new cards that do not overlap what they already have.
- **Several lectures in one message:** run one spec per lecture, so each file and each
  set of lecture tags stays clean.
- **Material in Arabic:** cards stay in English with the course's English terminology
  wherever the course uses it. If the course itself is taught with Arabic terms, follow
  the course and mention that choice in the reply.
