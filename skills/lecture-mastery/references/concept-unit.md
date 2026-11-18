# The Concept Unit — how every concept is taught

Every concept is taught through this unit. The playbook for the lecture type shapes the content of each element (e.g. the "Worked example" of a math concept is a derivation-backed problem; of a code concept, a program you actually ran).

## The seven elements

1. **The Problem** — Why does this concept exist? What breaks, or what can't be done, without it? This is the most-skipped and most important element: a concept with no problem attached is memorized, not understood. With a lens, the problem can come from the lens world — but the lecture's own motivation is still stated.

2. **Intuition** — A mental model, analogy, or picture that makes the idea feel obvious *before* the formalism. State where the analogy breaks; an analogy that is silently wrong at the edges plants misconceptions.

3. **Formalism** — The precise definition, statement, formula, or syntax, exactly as needed for the exam. Explain every symbol and every condition ("why must f be differentiable here?"). Conditions and edge cases are part of the definition, not footnotes.

4. **Worked example** — Fully solved, with the reason for each step ("we factor here because…"). At least one example must be exam-shaped. With a lens, a second example comes from the lens world — it is added, never substituted.

5. **Misconceptions** — The specific mistakes people make with this concept and why they're wrong. Be concrete ("students often treat P(A|B) as P(B|A) — here's a case where they differ by 100×").

6. **Connections** — How it links to earlier concepts (in this lecture, earlier lectures from course memory) and what it enables next. This is what turns isolated facts into a structure.

7. **Check** — One quick question the user can answer in their head right now. (The formal checkpoint comes at the end of the part.)

Then, when relevant: `🔭 Beyond the lecture` extensions and lens depth, following the no-gap ladder.

## Sizing

- **Major concepts:** all seven elements, full depth, often more than one worked example.
- **Minor concepts:** at minimum Problem (one line can suffice), Formalism, and an example or connection. Correctness and completeness are never reduced — only room.
- Do not print the element names as rigid headers every time. Use them as a checklist; write as a strong teacher talks. Headers per concept are fine.

## Writing standards

- Explain *why* at every step; a step without a reason is a gap.
- Precise language. "Roughly" and "basically" are allowed only when followed by the precise version.
- Short paragraphs; display math and code on their own lines.
- Prefer one excellent example over three shallow ones — but hotspots deserve a second angle.
- No filler, no motivational talk, no "great question".

## Compact illustration (Arabic, to show the style)

> ### Conditional Probability
>
> **المشكلة:** الاحتمال العادي بيفترض إنك مش عارف أي حاجة. بس في الواقع دايماً بيجيلك معلومة جديدة، فإزاي تحدّث الاحتمال بناءً عليها؟
>
> **الفكرة:** لما تعرف إن B حصل، العالم بتاعك اتقلص وبقى B بس. فالسؤال بقى: جوه B، قد إيه من المساحة دي فيها A؟
>
> $$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$
>
> الشرط P(B) > 0 مش تفصيلة: لو B مستحيل الحدوث، مفيش "عالم جديد" تقيس جواه أصلاً.
>
> **غلطة شائعة:** إن P(A|B) زي P(B|A). مثال: احتمال إن حد يكون لاعب basketball لو هو طويل قليل، لكن احتمال إنه طويل لو هو لاعب basketball عالي جداً.

Notice: the equation sits on its own line, technical terms stay in English, and each claim carries its reason.
