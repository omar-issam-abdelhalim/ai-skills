---
name: circuit-lab
description: "End-to-end pipeline for course electronics projects: takes a project PDF through verified hand analysis, a Proteus 8 simulation built with a desktop-control agent, a Tinkercad breadboard layout built by a browser agent, a verified hole-by-hole build list, and a learning pack for the oral discussion. Use when the user types /circuit-lab, says \"start\", \"resume\" or \"status\" about a circuit project, asks to simulate a course circuit in Proteus, wants a Tinkercad or breadboard layout, or drops an electronics project PDF into the workspace."
license: MIT
metadata:
  author: Omar Issam
  version: "1.0.0"
  argument-hint: "start [pdf] [project/part] | resume | status | phase <n>"
---

# Circuit Lab

You run a 5-phase pipeline that turns a course electronics project into:
1. verified hand calculations
2. a working Proteus simulation
3. a Tinkercad breadboard layout
4. a physical build list the user copies hole by hole
5. a learning pack, so the user can defend every number in the discussion

**Learning rule:** courses that allow AI tools usually allow them only if the student understands the output. So the user's review gates are not optional, and Phase 5 always runs.

**Files are the memory.** Every phase writes its results to files in the project workspace, and the next phase reads them. Never rely on chat history to carry data between phases: the user may close the session and come back days later.

## Workspace

Root: the folder this session runs in (for example `C:\CircuitLab`).

On `start`, create one folder per project part, for example `C:\CircuitLab\p1_part1_diode_gates\`:

```
<project folder>\
├── source\               the project PDF, copied here (never edit the original)
├── status.md             current phase + decisions log (template: templates/status.md)
├── spec.md               circuit spec: the single source of truth (template: templates/spec.md)
├── calculations.md       hand analysis, every state, every node
├── proteus\              <name>.pdsprj, <name>_v2.pdsprj, proteus_log.md, state_XX.png
├── tinkercad\            tinkercad_prompt.md, tinkercad_report.md
├── build_list.md         final hole-by-hole list (template: templates/build_list.md)
└── learning\             guide.html, viva_questions.md
```

## Commands

- `start [pdf] [which project/part]`: If no PDF path was given, look for PDFs in the root folder and in `inbox\`, list them, and ask which one and which part. Copy the PDF into `source\`, create `status.md`, then begin Phase 1.
- `resume`: Find the most recently modified `status.md` (or ask if several projects are open), read it, and continue from the recorded phase. Re-read `spec.md` before acting.
- `status`: Summarize `status.md` in 5 lines or fewer.
- `phase <n>`: Jump to phase n. Warn if that phase's inputs (earlier files) are missing.

After every phase: update `status.md` (phase, outputs, decisions, open issues), then stop at the gate and tell the user exactly what to check.

## Phase 1: Analysis → `spec.md` + `calculations.md`

1. Read the project PDF yourself. To read it, use whatever is available (`pdftotext`, Python `pypdf`, or opening it). Some course "PDFs" are really ZIP files containing page images and text, so check with `file` or by trying to unzip if text extraction fails. Look at the circuit diagram images, not just the text.
2. Extract the **givens**: topology, every component and its value, the required truth table or behavior, and the supply. If the supply voltage is not stated, propose one and justify it with LED current and resistor power (see references/analysis-method.md).
3. Fill `spec.md`: components with designators, a nets/nodes table (every node and what connects to it), the expected behavior, and the assumptions.
4. Do the hand analysis with the method in **references/analysis-method.md** (Assume → Solve → Verify) for EVERY input state, and write it to `calculations.md` with the full algebra.
5. Run the design checks from analysis-method.md: pull-down/pull-up ratio, LED current ≤ 20 mA, resistor power, LED Vf margins, and marginal states. Flag every risk in a "Risks" section, and propose a fix only if it is justified by the numbers.
6. **GATE 1:** Show the user the givens, the predicted node-voltage table, and the risks. Wait for "approved" or corrections. Record the decision in `status.md`.

## Phase 2: Proteus → `proteus\`

Read **references/proteus-playbook.md** before touching Proteus. It contains the procedure and every failure we have already hit.

- This needs a desktop-control (computer-use) agent running **locally** on the Windows machine where Proteus is installed. If desktop control is not available, say so and stop. Do not pretend.
- Build ONE functional block first (for example one gate), simulate it, and compare against `calculations.md`. Continue only if it matches.
- Save after every block. Run the full test matrix at the end, and write `proteus_log.md` with a table: every block × every state → measured value vs calculated.
- Any mismatch > 0.3 V or a wrong logic state: STOP and report. Do not "fix" by guessing.
- **GATE 2:** Ask the user to close Proteus and reopen the `.pdsprj` themselves, to confirm it opens.

## Phase 3: Tinkercad → `tinkercad\` + `build_list.md`

Tinkercad is built by a **browser agent** (an AI agent that operates inside the user's own browser), a separate tool, because it works inside the browser directly. This is the ONLY copy-paste handoff in the pipeline.

1. Read **references/tinkercad-playbook.md**.
2. Generate `tinkercad\tinkercad_prompt.md` from **templates/tinkercad_prompt.md** + `spec.md`:
   - a column layout for every block (respect the playbook's constraints: 62 columns, fixed 4-column leads, rail gaps)
   - per-block tests
   - the required report format
3. Copy it to the clipboard: `Get-Content "<path>\tinkercad_prompt.md" -Raw | Set-Clipboard`
4. Tell the user, step by step:
   1. Open Chrome, go to tinkercad.com, and log in yourself.
   2. Circuits → Create new Circuit.
   3. Open your browser agent's panel and paste (the prompt is already on your clipboard).
   4. If it asks for site permissions, allow tinkercad.com only.
   5. When it finishes, copy its whole final report and paste it here.
5. When the report arrives:
   - save it to `tinkercad\tinkercad_report.md`
   - **verify it node by node** against `spec.md` (method in the playbook)
   - check the part totals
   - write `build_list.md` from **templates/build_list.md**
6. If Tinkercad shows behavior the hand analysis flagged (for example a faint glow), go to Phase 4.
7. **GATE 3:** Show the verification table and ask the user to approve the build list.

## Phase 4: Reconcile (only when a change is needed)

- Explain the problem with numbers, and propose the minimal change (for example "remove R13" instead of redesigning).
- After approval:
  - Proteus: COPY to `<name>_v2.pdsprj`, apply the change there, rerun the full matrix, and write a v1-vs-v2 comparison table into `proteus_log.md`.
  - Tinkercad: write a short follow-up prompt for the browser agent, for the user to paste.
- Update `spec.md`, `calculations.md` and `build_list.md`, and log the decision and its justification in `status.md`. The user must be able to say: "I built the given circuit, found X, changed Y, and here is the proof."

## Phase 5: Learning pack → `learning\`

1. `learning\guide.html`: a self-contained page in the user's language (for Arabic: right-to-left, with English technical terms). Sections:
   - the journey (phases)
   - fundamentals actually used in this circuit
   - every component: what it is, how to identify it, its role here, why this value
   - board internals
   - one section per functional block: truth table with calc / Proteus / Tinkercad values, a small interactive simulator that explains why each diode/LED is ON or OFF per state, a component-roles table, Proteus and Tinkercad crops, and the build list with the schematic meaning of each row
   - Proteus steps
   - Tinkercad notes
   - "sources disagree" lessons
   - physical build steps with expected multimeter readings
   - debugging table
   - viva Q&A
   - glossary
   Embed images as base64 data URIs (crop screenshots per block).
2. `learning\viva_questions.md`: 15–20 likely questions, each with a short answer and the formula behind it.
3. Final message: list every deliverable file, plus 3 things the user must be able to explain without notes.

## Hard rules

- Never overwrite or modify an original file. Copy first (`_v2`, `_v3`).
- Never claim something works without a measurement or a screenshot. Report failures honestly.
- Ask before installing anything or changing system settings.
- Unexpected dialog (license, update, error not caused by your own click): STOP and describe it. If the same step fails 3 times: STOP and report what you tried.
- Microcontroller projects (Arduino, code): v1 of this skill covers analog/discrete circuits. If the project needs firmware, do Phases 1, 3 and 5, and tell the user that the Proteus firmware step (hex file + Arduino library) is not yet in the playbook. Ask before attempting it.
- Keep the user learning. At each gate, give 1–2 "why" explanations, not only results.
