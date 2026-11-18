---
name: meeting-report
description: "Turn a meeting transcript (Whisper or any speech-to-text) or raw notes into a decision-grade meeting report, keep running decision and action registers across meetings, and analyze meeting history. Use for \"meeting report\", \"write up this meeting\", \"analyze our meetings\", \"what's still open\", \"تقرير ميتينج\", \"حلل الميتينجات\", \"إيه المفتوح\"."
license: MIT
metadata:
  author: Omar Issam
  version: "1.0.0"
---

# Meeting Report

## Purpose
A meeting report is not a summary. It exists to capture:
1. **Decisions** — what was actually agreed, why, and by whom.
2. **Commitments** — who does what, by when, and what "done" looks like.
3. **Continuity** — every report checks the previous meetings' open actions so nothing silently dies.

A person who missed the meeting must understand it fully in under 2 minutes from the Executive Summary alone.

## Configuration (read first)
This skill is team-agnostic. Team specifics live in `config.md` next to the registers (see `templates/config.md` for the format):
- Organization / team name, and the meeting types the team uses
- Glossary of terms and the People list (exact spellings and roles)
- Protected periods (exams, holidays) when no work should be scheduled
- Where reports are saved (a project folder, a Drive folder, a wiki page) and who may read which meeting types

If `config.md` does not exist, ask for the essentials once (team name, people, where to save), create it from the template, and continue. Never invent names, folders or dates that are not in the config or the transcript.

## Language rules
- **The report is written in professional English** by default (`config.md` may set another report language). Transcripts are often mixed-language (e.g. Arabic and English); translate the meaning, not word-for-word.
- Names: spell exactly as in the People list. Never guess a spelling.
- When the exact wording of an external party's commitment matters, give a short quote in the original language followed by its translation.
- File names in English.
- Chat replies to the user (questions, confirmations) follow the user's language; the report itself follows the report language.

## Respectful & professional content (NON-NEGOTIABLE)
The report documents work, decisions, and facts. It never judges people. This rule overrides completeness.
- **Nothing negative about any person** — present or absent, member, leader, other team, or external party. Not quoted, not paraphrased, not implied, not hinted through tone.
- **No insults, profanity, sarcasm, mockery, or nicknames**, even if they were said in the meeting and even if they were "just a joke". Banter and jokes are omitted entirely.
- **No words that imply bad character or bad intent:** e.g. lazy, careless, didn't care, ignored, refused, failed, blamed, complained, attacked, unprofessional. Never attribute motives.
- **Attach problems to tasks and processes, not people.**
  - Instead of "X was lazy and didn't finish the prospect list" → "A-004 (prospect list) is late; revised deadline agreed: 22 Oct."
  - Instead of "Y and Z argued about the budget" → "Different approaches to the budget were discussed; agreed approach: …"
- **Disagreements:** record the positions on the topic and the outcome, without who-said-what in heated moments and without emotional words.
- **Late or missed actions:** status ("Late") + revised deadline only. No commentary.
- **External organizations:** facts only (e.g. "Not able to sponsor this season"); never criticism.
- **Conduct incidents** (insults, harassment, serious personal conflict, wellbeing concerns): never written in the report, the registers, or any saved file. Instead, after showing the draft, tell the user privately in chat in one or two neutral lines that a part of the transcript may need the HR / people route, without repeating what was said. This note is never saved anywhere.
- **The reader test:** before finishing, read every line as if each person named in it will read it in front of the whole team. If anyone could feel embarrassed, blamed, or attacked, rewrite it neutrally or remove it.

## Modes
- **Report (default):** one transcript/notes → one report.
- **Analyze:** "analyze meetings" / "what keeps coming up" / "حلل الميتينجات" → cross-meeting analysis (see bottom).
- **Open items:** "what's open?" / "open actions" / "إيه المفتوح؟" → open actions from the Action Tracker, grouped by owner, overdue first.

---

## Step 1 — Intake
Required:
- Transcript or raw notes
- Type: one of the types in `config.md` (default set: `Team-Sync` | `Leads` | `Leadership` | `1on1` | `External` | `Cross-Team` | `Other`)
- Date (and time if known)
- Attendees (and absentees if relevant)
- External only: organization + contact person's role

Infer what the transcript makes clear. Ask ONLY for missing essentials, in ONE short message. If the date is missing, use today's date and state it in the report.

## Step 2 — Load context (continuity)
- Read `registers/Action_Tracker.md` and `registers/Decision_Log.md`: last used IDs + all OPEN actions + standing decisions.
- Read the most recent report of the same type (External: same organization) from `meetings/`.
- If the registers do not exist, this is the first report: IDs start at 001.
- If a decision in this meeting changes or contradicts a standing decision, flag it explicitly ("Supersedes D-xxx").

## Step 3 — Clean the transcript (speech-to-text realities)
- Speech-to-text often has no speaker labels, mishears names and technical terms, and repeats fragments.
- Fix obvious term errors using the Glossary in `config.md`.
- **Never guess who said something.** Unknown speaker → "(speaker unclear)". Prefer "Agreed by attendees" over guessing a person.
- Mark unintelligible or ambiguous passages `[unclear in recording]` and list them in Recording Quality Notes.
- Paraphrase; no long verbatim chunks.
- Drop jokes, side talk, and anything covered by the Respectful content rules.

## Step 4 — Extract with explicit status (most important step)
Classify every substantive item:
- **Decision:** clear agreement or a stated decider. Only these enter the Decisions table and the Decision Log. Capture the **rationale** (why) and any **alternatives rejected** when they were discussed.
- **Proposal:** raised, not agreed. Never upgrade a proposal into a decision.
- **Deferred:** explicitly postponed — note until when / on what condition.
- **Open question:** needs information or someone else's input — note who must answer.

Actions:
- Owner = a named person. "The team" / "everyone" is not an owner → flag "Owner needed".
- Deadline = explicit date. None stated → "No deadline — needs one". Never invent one.
- Definition of done = the output that proves completion.
- Dependencies = what or whom the action waits on.
- Carry-over: every previously open action gets a status from this meeting: Done / In progress / Late / Cancelled / Not discussed.

Numbers and claims — label each: `Fact` (with source) | `Estimate` | `Projection` | `Unverified`.
- Keep **earned revenue** separate from **funding / sponsorship**.
- **Reach is not impact.**
- **Interest is not confirmed support** — external support is confirmed only with written confirmation.
- Never invent numbers about the team, its projects, or partners.

Protected periods — flag ANY deadline, meeting, or task that falls inside a protected period listed in `config.md`, and propose the nearest valid date.

IDs:
- Meeting: `M-YYYYMMDD-<Type>` (append `-2` for a second same-type meeting that day)
- Decision: `D-001`, `D-002`, … (continue from the Decision Log)
- Action: `A-001`, `A-002`, … (continue from the Action Tracker)
- Risk: `R-001`, … (continue across reports)

## Step 5 — Write the report (template)

```
# Meeting Report — {Type} — {YYYY-MM-DD}

| Field | Detail |
|---|---|
| Meeting ID | M-... |
| Date & time | ... |
| Type | ... |
| Attendees | ... |
| Absent | ... |
| Chair / Note-taker | ... |
| Source | Transcript / notes |

## Executive Summary
(Max 5 lines: purpose, the key decision(s), the most important actions with owners, the top risk, what is needed from whom. Must stand alone.)

## Meeting Outcome
- Purpose achieved: Yes / Partially / No — one-line reason
- Decisions made: n | Actions assigned: n | Open questions: n

## Objective

## Follow-up on Previous Actions
| A-ID | Action | Owner | Status | Note |

## Key Discussion Points
(Grouped by topic; each point 1–3 lines; show the key arguments, not the chatter.)

## Decisions
| D-ID | Decision | Rationale | Decided by | Conditions / Supersedes |

## Proposals Not Yet Decided
| Proposal | Raised by | What is needed to decide | By when |

## Action Items
| A-ID | Action | Owner | Deadline | Definition of done | Depends on |

## Open Questions
| Question | Who must answer | By when |

## Risks
| R-ID | Risk | Likelihood (L/M/H) | Impact (L/M/H) | Mitigation | Owner |

## Approvals Required
| Item | Approver | Deadline |

## Figures Mentioned
| Figure | Classification | Source |

## Recording Quality Notes

## Next Meeting
- Date:
- Proposed agenda (3 items max, derived from open actions, open questions, and pending approvals)
```

Omit genuinely empty sections, EXCEPT Decisions, Action Items, and Follow-up on Previous Actions: if empty, write "None" so the absence is visible.

Type-specific additions:
- **External:** organization + contact role · their interests and what they asked / offered · commitments on each side with status (Verbal / Written) · next contact date and owner · recording consent obtained (Yes/No) · a ready-to-send follow-up email draft. Nothing is recorded as confirmed or delivered without evidence.
- **1on1:** wins · blockers · support needed · agreed actions. Record only what was said about the work; no personality judgments. Confidential to the leads.
- **Leadership:** decisions · different approaches discussed and the agreed outcome · escalations. Confidential to the leadership.
- **Cross-Team:** dependencies (who waits on whom) · items that must go to another team's registers (mark "→ <team>").
- **Team-Sync / Leads:** updates grouped by function or workstream, as listed in `config.md`.

## Step 6 — Quality gate (silent self-check before showing)
- **Respect check:** no negative, mocking, blaming, or intent-implying word about any person or organization; the reader test passes for every name in the report.
- Every decision is a real decision, not a proposal, and has a rationale if one was given.
- Every action has a named owner, a deadline, and a definition of done — or is visibly flagged.
- No date falls in a protected period without a flag.
- No invented names, numbers, speakers, or commitments.
- Figures are labelled; revenue vs funding and reach vs impact are separated.
- Executive Summary is 5 lines or fewer and stands alone.
- Every previously open action appears in Follow-up.
- The report language is clear, concise, and professional.

## Step 7 — Review with the user
Show the full report. If the transcript contained a conduct matter, add the private neutral note in chat (not in the report). Ask for corrections in one line. **Save nothing until the user explicitly approves** ("ok", "save", "تمام", "احفظ"). Apply corrections, then save.

## Step 8 — Save (only after approval)
File name: `YYYY-MM-DD_Meeting_<Type>_<Short-Topic>_v01` (e.g. `2026-10-14_Meeting_Team-Sync_Kickoff_v01`). Later corrections → `_v02`; never overwrite silently.

1. **Workspace:** write `meetings/<filename>.md`.
2. **Shared location (optional):** if `config.md` names one (a Drive folder, a wiki space) and a connected tool can write there, create the same document there. All meeting types go in the configured folder; the type is carried by the file name, so files sort by date. If the location cannot be reached, do NOT create folders on your own — save to the workspace only and tell the user.
3. **Registers:**
   - `registers/Decision_Log.md` — append: D-ID · date · decision · rationale · decided by · Meeting ID · status (Active / Superseded by D-xxx / Cancelled).
   - `registers/Action_Tracker.md` — append: A-ID · action · owner · deadline · definition of done · Meeting ID · status; update statuses of carried-over actions.
   - Create either file if missing. The Respectful content rules apply to registers too.
4. **Confirm back** in 3 lines: what was saved where (with links when available) + the Executive Summary formatted as a ready-to-send chat message for absentees.

Privacy:
- 1on1 and Leadership reports must never be placed anywhere that members or guests can access. If the configured folder is shared more widely, store these two types in a separate restricted location and tell the user.
- Never write member complaints, evaluations, or personal matters into any saved file; personal or wellbeing matters → note only "Referred to the people route" if it affects an action, otherwise omit.

---

## Analyze mode
Read all reports in `meetings/` and both registers. Output (same language and Respectful content rules):
1. Overdue actions (owner, days late) and actions missing an owner or deadline.
2. Decisions with no follow-up action; decisions later reversed or contradicted.
3. Recurring blockers or topics (3+ meetings) — framed as process issues, never as people issues.
4. Load distribution: open actions per person (counts only, no judgment or ranking).
5. Risk trends: risks that recur or grow.
6. Deadlines in the next 14 days, flagging any near protected periods.
7. Meeting effectiveness trend: share of meetings with decisions; actions closed on time.
8. Three suggested agenda items for the next meeting.

Separate what the records state from what you infer; label inferences.
