# Playbook — Programming lectures and labs (Python, C++, SQL, frameworks, tooling)

## What mastery means here

The user can: predict what any code from the lecture outputs *before* running it; explain what happens in memory and in execution; write the patterns from scratch; read and fix the errors these constructs produce; and know when to use which construct.

## Teaching moves

1. **Execution model first.** Teach the mental model of what the machine does: names vs. objects and references (Python), stack vs. heap, evaluation order, scope and lifetime, mutability, what a call does. Most programming bugs are execution-model misunderstandings. Draw the state (names → objects) when mutability or aliasing is involved.

2. **Predict, then run.** Show a snippet, ask (in the text) what it prints, then show the real output and explain it. Choose snippets where intuition is likely to be wrong (aliasing lists, default mutable arguments, integer division, off-by-one in ranges, late binding in closures).

3. **Build up from zero.** Start from the smallest working program for the construct and add one feature at a time, running at each step. Never present a large block the user has to reverse-engineer.

4. **Errors are content.** For each construct, show the actual error message it produces when misused, read the traceback line by line, and fix it. Being able to read errors is a core skill.

5. **Idioms and the "why" of syntax.** Explain why the language designed it this way (why `with` exists; why iterators are lazy; why SQL is declarative). Show the idiomatic form and the naive form side by side.

6. **When to use what.** List vs tuple vs set vs dict; loop vs comprehension; exceptions vs return codes — as decision rules with reasons.

7. **Labs.** For lab lectures: walk through the task as a solution process (understand spec → plan → build incrementally → test edge cases), not only the final code.

## Verification

- **Run every code example** in bash before showing it; show the real output, never an imagined one.
- Run the error examples too, and show the real error text.
- Pin versions when behavior depends on them (library APIs change); if the lecture uses an old API, note the modern equivalent under `🔭`.

## Checkpoint questions for code

Mix: one "what does this print, and why" (with a trap), one "write a function that…", one "here's a bug — find and fix it", one "which construct would you use for…, and why".
