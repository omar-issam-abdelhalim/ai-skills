# Playbook — Algorithms and data structures

## What mastery means here

The user can: explain the problem and why naive approaches fail; trace the algorithm by hand on any small input; state and use its invariant; derive its complexity; argue correctness; handle edge cases; implement it; and pick it (or not) for a new problem.

## Teaching moves

1. **Problem first, then naive solution.** Define the input, output, and constraints. Solve it the obvious way, measure its cost, and show exactly where it wastes work. The real algorithm is then the answer to "how do we stop wasting that work?" — this makes the design feel inevitable rather than magical.

2. **The core idea in one sentence.** "Keep the smallest unsettled distance so far" (Dijkstra); "split, solve halves, merge in linear time" (merge sort). Everything else is implementation.

3. **The invariant.** What is always true at each step? Show it holds initially, is preserved by each step, and implies correctness at the end. The invariant is the bridge between intuition and proof.

4. **Hand trace as a table.** Run the algorithm on a small, carefully chosen input (one that exercises the interesting cases) and show the state after every step in a table: variables, data structure contents, what changed and why. Then a second input that hits an edge case.

5. **Complexity derivation, not assertion.** Count the work: loop bounds, recurrence (and solve it — Master theorem or recursion tree), amortized arguments. Time and space. Best/average/worst when they differ, and *which input* causes the worst case.

6. **Edge cases.** Empty input, one element, duplicates, negative values, disconnected graphs, already-sorted input, overflow.

7. **Variants and choice.** When to use it vs. alternatives (tradeoff table: time, space, stability, online vs offline, constraints like negative weights).

8. **Implementation.** Clean code implementing it, run on the traced inputs, with output matching the hand trace.

## Verification

- Implement the algorithm and run it on every traced input; the table and the program output must agree.
- For complexity claims, optionally time or count operations on growing inputs to show the growth rate.
- For data-structure operations, run them and print the structure state.

## Checkpoint questions for algorithms

Mix: one "trace on this new small input", one "what's the complexity and why", one "what breaks if we change X (e.g. allow negative weights)", one "which algorithm would you choose for this scenario".
