---
name: exam-lab
description: "Build an interactive, offline exam-prep app (a single HTML file with practice mode, a timed mock exam, mistakes review and a study guide) from lectures, sheets, past exams and notes, with questions that match how the course actually examines. Use when the user types /exam-lab or asks for practice questions, a question bank or a mock exam for a quiz, midterm or final."
license: MIT
metadata:
  author: Omar Issam
  version: "1.0.0"
---

# Exam Lab

Turn whatever the user has for an exam (one lecture, a lecture + sheet, all midterm lectures, final material, past exams, screenshots, their own notes) into a practice app that asks questions **the way this course actually asks them**. Output = one self-contained HTML file that works offline: practice mode, a timed mock exam, a mistakes review and a study guide, with progress saved in the browser.

Talk to the user in their language. Keep the app UI in English. Explanations inside the app follow the user's preferred language (for Arabic speakers: Arabic with technical terms kept in English).

## The kit (reuse it, never rebuild the app by hand)

Everything the app needs ships with this skill:

| File | Role |
|---|---|
| `assets/template.html` | The app engine. Everything between `/*__DATA_START__*/` and `/*__DATA_END__*/` is replaced with the exam's data. |
| `scripts/build.py` | Injector: `python3 build.py template.html data.js out.html` |
| `scripts/check.js` | Quality gates: `node check.js data.js` (exit code 1 on errors) |
| `assets/example-data.js` | A small, complete dataset showing every question shape. Read it once before writing data. |

Copy the kit into a working folder (`kit/`) and work there. Never edit the template itself.

## Workflow

### 1. Intake
Read every file the user gives (render slide pages to images when diagrams or highlights matter). Classify each source: lecture, sheet/tutorial, past exam or quiz, the user's notes, screenshots (highlights, messages from classmates). Note what is explicitly excluded ("section 1.4 is not included").

Treat classmates' and rumored hints as **priority signals, not facts**: raise the weight of those topics, still cover everything in scope.

### 2. Exam-style analysis
Work out how this course asks questions. Strongest evidence first:
1. Past exams/quizzes of this course
2. Sheets and exercises inside the lectures
3. The user's notes about the exam ("MCQ only", "25 questions", "the instructor said...")
4. The nature of the material (definitions-heavy, case-based, calculation-heavy)

Extract: question types and their mix (MCQ / True-False / written / problems), options per MCQ, typical stems (definition, which-is-NOT, scenario-to-concept, researcher-year-finding, calculation), difficulty, exam length and time if known.

### 3. Plan, then STOP for approval
Send the user a short plan (≤ 12 lines) and wait for their OK or corrections:
- What you understood about the exam style (with the evidence)
- Question types and mix
- Per lecture: number of testable concepts found → number of practice questions; plus mock exam size and time
- Priority per lecture and why
- Anything unclear or missing (e.g. no past exam found, so style is inferred)

Question count (automatic; any number the user gives overrides). Count testable ideas, not words:
1. Build a **concept inventory** per lecture/sheet: every distinct testable unit, read from text AND diagrams, equations and tables (render pages when needed).
2. Questions per unit:
   - Definition: 1-2 (the definition + applying it)
   - Distinction between concepts (e.g. necessary vs sufficient): 1-2
   - Named example / study / researcher-year-finding: 1-2
   - List or steps: 1 + one "Which is NOT" if the list is exam-worthy
   - Sheet exercise / problem: at least 1 each (variants for key problem types)
   - Formula / diagram / table: 1-2
   - Explicit learning objective: must be covered
3. Priority scales within those ranges: top-priority lectures take the upper end, low-priority the lower end.
4. Hard limits: at most 2-3 questions per unit, and every question must test something the others don't. No minimum per lecture: a lecture with 4 real ideas gets ~5 questions. Never write filler to reach a number.
5. Word count is only a sanity check: if the total looks far off for the amount of material, re-check the inventory.
- Mock: real exam length if known; otherwise 25 for a midterm/final, 10-15 for a quiz; no mock for a single lecture unless asked. Time: real exam time if known, else ~1.2 min per MCQ.

### 4. Write the data
One `data.js` defining `CONFIG`, `B` (practice bank), `M` (mock), `G` (study guide). Write it lecture by lecture in separate files and concatenate; never hand-edit the template.

```js
const CONFIG={
  course:"Critical Thinking", exam:"Midterm",            // exam: Quiz 2 / Midterm / Final / Lecture 3 ...
  subtitle:"Chapter 1 · Dr. Example · MCQ only",
  lectures:[{id:"1.1",name:"Critical Thinking Mindset",prio:"Very high"}],  // prio: Very high | High | Medium | Low
  mock:{enabled:true,minutes:30},
  notes:["<mark>Highest weight</mark>: 1.1 and 1.6."],      // Exam focus notes: short, English
  style:["MCQ only, 4 options, definitions tested directly."], // shown in Study Guide as 'How this course asks questions'
  accent:null,                                              // e.g. "#ffd60a"; null = default yellow
  storageKey:"examlab_criticalthinking_midterm"             // unique per course+exam, never change it for the same app
};
const B=[ /* practice */ ], M=[ /* mock: NEW questions, not rewordings of B */ ];
const G={"1.1":{pts:["...key point, <b> allowed..."],traps:["..."]}};
```

Question shapes. One rule for every objective type: `o[0]` is ALWAYS the correct option. Display order is the app's job: MCQ options are shuffled, T/F is always shown True then False, and grading follows the option itself, not its position. So a T/F whose answer is False is written with False first:
```js
{l:"1.6", h:1, q:"Hastorf and Cantril (1954) concluded that:",          // h:1 = highlighted/priority point
 o:[["correct text","why it is right"],["distractor","why it is wrong"],["distractor","..."],["distractor","..."]],
 k:"the one idea to remember, in a line or two"}
{l:"1.6", t:"tf", q:"Statement: perception is objective.", o:[["False","why False"],["True","why not True"]], k:"..."}   // answer False → False written first
{l:"1.6", t:"tf", q:"Statement: memory is not a photograph.", o:[["True","..."],["False","..."]], k:"..."}           // answer True → True written first
{l:"1.6", t:"written", q:"Define ...", a:"<p>Model answer, HTML allowed</p>", k:"optional short note"}
```
Use `html:1` on a question only if `q` needs HTML (formulas, line breaks).

Writing rules:
- Match the exam's style found in step 2: same types, option count, stem patterns, difficulty.
- Distractors come from real neighbouring concepts in the same course (the classic confusions), same grammar and similar length as the correct answer. No silly options, no "All/None of the above".
- Each option's explanation says concretely why it is right or wrong (which concept it actually belongs to, what the slide says). Never just "wrong".
- `k` = the one idea to remember so a similar question is solvable next time.
- T/F: keep answers balanced (True between 30% and 70%); write the false statements as believable near-misses of the real idea, not obvious nonsense.
- Written questions: model answer only (the user marks themselves). Make it the answer a full-mark student would write.
- Problems/calculations: MCQ with distractors built from common mistakes; the correct option's explanation shows the worked steps.
- Cover every definition, named example, list, exercise and researcher/year pairing in scope. Mark highlighted/hinted points with `h:1`.
- Verify every correct answer against the source text before moving on.
- `G`: per lecture, key points + exam traps.

### 5. Quality gates (mandatory)
- `node kit/check.js data.js` must finish with 0 errors. It checks schema, duplicates, mock-vs-bank copies, T/F form and True/False balance (outside 30-70% True is an error from 4 T/F questions up), missing explanations, and the length cue (correct option = longest in > 50% of MCQs is an error; aim below 40%). Fix real warnings too.
- Re-read each lecture's questions against the slides once for factual accuracy.

### 6. Build and test
```bash
python3 kit/build.py kit/template.html data.js app.html
```
Smoke-test in a headless browser (e.g. Playwright): open the file, start a practice session, answer a few (keys 1-4, `E` explanation / model answer, `Enter` next), Exit → Save & exit → reload → Resume, finish, open the mock and submit, visit Mistakes and Study Guide. Zero page errors. Take one screenshot of a question with its explanation, fix what it shows, and do not loop.

### 7. Deliver
- Hand `app.html` to the user. It is fully self-contained and works offline in any modern browser.
- If the environment can host pages, also publish it under the title `<Course> <Exam> Prep`. To extend an existing app (e.g. add final lectures), rebuild with merged data and replace the same page, keeping the same `storageKey` so saved progress survives.
- Final message (short): what's inside (counts per type, mock size/time), the style it is built on, and two notes: progress is saved per device/browser, and a hosted copy and a local file keep separate progress.

## Defaults the user can change
- Colors: black/white base with yellow accent. Change the accent via `CONFIG.accent`; for a different base palette edit the `:root` tokens in the built file only.
- Explanation language: whatever the user prefers (it is just the data). UI stays English.
- Counts, priorities, mock length/time: whatever the user says wins.

## Don'ts
- Don't skip the plan approval in step 3.
- Don't write long stories about where a hint came from; put the useful part in `notes` in one line.
- Don't hand-write a new app or restyle the template per exam.
- Don't ship if check.js has errors or the smoke test shows page errors.
