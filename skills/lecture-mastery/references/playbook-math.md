# Playbook — Mathematical lectures (calculus, linear algebra, probability, statistics, discrete math, proofs)

## What mastery means here

The user can: state definitions and theorems with their exact conditions; reproduce key derivations and explain why each step is valid; solve every exam problem type; see the geometric or intuitive meaning; and recognize when a result does *not* apply.

## Teaching moves

1. **Meaning before manipulation.** Before any symbol-pushing, say what the object *is*: a derivative is a local rate / best linear approximation; a determinant is signed volume scaling; an eigenvector is a direction the map only stretches. Symbols without meaning are memorized, not understood.

2. **Derivations: name every move.** For each step, say what was done and why it's legal: "add and subtract the same term", "apply the chain rule to the outer function", "valid because the limit of a product is the product of limits when both exist". Never write "it follows that" without the reason. Where the slides jump, fill in every missing step.

3. **Proofs: skeleton first.** Before the line-by-line proof, give the proof's strategy in one or two sentences (contradiction? induction? construct an example? bound and squeeze?) and its *key idea* — the one trick that makes it work. Then the steps. Then: which hypothesis was used where (and what breaks if you remove it).

4. **Conditions are content.** For every theorem, show a counterexample where a hypothesis fails and the conclusion fails with it. This is where real understanding lives and where exams set traps.

5. **Geometric and numerical intuition.** Sketch (or describe precisely, or visualize) the picture. Plug in numbers to show the formula behaves as claimed.

6. **Special and limiting cases.** What happens at 0, at infinity, when the matrix is the identity, when n = 1? Special cases both check formulas and build intuition.

7. **Sanity checks.** Dimensions/units, signs, symmetry, known special cases. Teach the user to run these on their own answers.

8. **Problem ladder.** For each exam problem type: one fully worked example → the recognition cue ("when you see a product of a polynomial and exp, think integration by parts") → the standard pitfalls in that type.

## Common traps to address when relevant

- Algebra slips: sign errors, dropping absolute values, dividing by something that may be zero, sqrt(x²) = x.
- Chain rule and product rule confusion; forgetting the inner derivative.
- Integration: forgetting to change limits in substitution; forgetting +C.
- Linear algebra: matrix multiplication order; (AB)⁻¹ = B⁻¹A⁻¹; not every matrix is diagonalizable.
- Probability: P(A|B) vs P(B|A); independence vs mutual exclusivity; base-rate neglect.
- Statistics: correlation vs causation; what a p-value is not.

## Verification

- Verify every derivation's result and every intermediate identity you assert with `scripts/verify_math.py` (equal / diff / integrate / limit / series / solve / simplify / numeric).
- Compute all numerical examples by script.
- If the slides contain an error, prove it: show the correct result verified, and a numeric counterexample to the slide's version.

## Checkpoint questions for math

Mix: one "state the theorem with conditions", one computation of exam shape, one "why is this step valid / what breaks if…", and optionally one "construct a counterexample".
