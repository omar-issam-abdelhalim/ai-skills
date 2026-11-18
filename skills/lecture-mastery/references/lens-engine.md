# Lens Engine — goal and domain lenses

A lens answers: "Given who I want to become (or where I'll apply this), what in this lecture matters most, and how will I actually use it?" It is woven into the teaching; it is never an appendix and never a replacement for the lecture.

## Contents
1. Two kinds of lens
2. The iron rules
3. Tiering every concept
4. Intensity by distance
5. Where the lens enters the teaching
6. The lens exercise
7. Advancing through the lens (no-gap)
8. Far domains and accuracy
9. Focus mode and combined lenses
10. Lens knowledge maps: AI Agent Engineer, AI Infrastructure Engineer

---

## 1. Two kinds of lens

- **Goal lens** — a role the user is becoming: *AI agent engineer, AI infrastructure engineer, ML engineer, founder*. Question: "How does this serve me in that role?" This is the strongest lens: it links every lecture to the user's trajectory, builds a mental index ("when I build X, I'll need Y from lecture Z"), and cures inert knowledge.
- **Domain lens** — a field of application: *neurosurgery, finance, climate*. Question: "Where is this concept applied?"

Classify from the wording: roles and job titles → goal lens; fields, industries, specialties → domain lens. If ambiguous, choose the more useful reading and state it in the interpretation line.

## 2. The iron rules

1. **Coverage is sacred.** Every lecture item is taught to full depth regardless of lens relevance. The lens adds depth; it never removes it.
2. **Honesty over impressiveness.** Never fabricate or stretch a connection. "Foundational only" is a valid and respectable answer.
3. **Added, not substituted.** The exam-shaped example stays; the lens example comes in addition.
4. **No gaps.** Lens extensions obey the full no-gap ladder (SKILL.md §8).
5. **Real, specific, verifiable.** Lens content names real mechanisms and real practices, not vague claims ("this is important in AI").

## 3. Tiering every concept

| Tier | Meaning | Treatment |
|---|---|---|
| **Direct** | Used as-is in the lens's daily work | Full lecture depth + lens example + `🔭` extension to where it lives in real systems + lens exercise material |
| **Indirect** | Foundation of something the lens uses | Full lecture depth + a clear explanation of the chain from this concept to the lens use |
| **Foundational only** | No real use in the lens | Full lecture depth + one honest sentence saying so (and, if true, what it's a prerequisite for) |

Search for deep, non-obvious connections before settling on "Foundational" — e.g. integrals underlie CT image reconstruction; graph traversal underlies agent workflow execution. But a deep connection must be real and explainable without gaps.

## 4. Intensity by distance

Cognitive load is the reason: a lens the user already lives in makes examples easier; a far lens makes the user learn two new things at once.

- **Near lens** (close to the lecture and to the user's world, e.g. AI agent engineer + a Python lecture): weave heavily — lens examples for most Direct concepts, lens-based checkpoint questions, a substantial exercise per part.
- **Far lens** (e.g. neurosurgery + a calculus lecture): weave lightly — a few strong examples that require minimal background (explain any domain fact they depend on), and a transfer question at the end.

## 5. Where the lens enters the teaching

1. **The Problem** element of Direct concepts — motivate from the lens world (after the lecture's own motivation).
2. **A second worked example** from the lens world.
3. **Depth allocation** — Direct concepts get extra edge cases, limitations, and real-world behavior.
4. **Checkpoint and mastery questions** — at least one transfer question set in the lens world.
5. **The Lens Preview** in the Map and a **"what to learn next"** line in the Consolidation.

## 6. The lens exercise

One per part, when the part has Direct or Indirect concepts:

- Built **only** from tools taught in this lecture or earlier in the session. If it needs something not taught, either teach it (ladder) or change the exercise.
- Produces a miniature of a real lens system — e.g. a tool dispatcher from functions + dicts, a retry loop from exceptions, a belief update from Bayes, a scheduler from a priority queue.
- States what the real-world version adds on top, and where the user will meet it.
- Run it before presenting.

Example (Python functions + dictionaries, AI agent lens):

```python
def search(query):
    return f"results for {query}"

def calculator(expr):
    return str(eval(expr))

tools = {"search": search, "calculator": calculator}

def run_tool(name, arg):
    if name not in tools:
        return f"Error: unknown tool '{name}'"
    return tools[name](arg)

print(run_tool("calculator", "2+3*4"))
print(run_tool("translate", "hi"))
```

Then: "This is the core of tool calling in every agent framework — the LLM outputs a tool name and arguments; code routes them to the right function. Real frameworks add schemas, validation, and error feedback to the LLM." (And note under `⚠️` that `eval` is unsafe on untrusted input — a real concern since LLM output is untrusted.)

## 7. Advancing through the lens (no-gap)

Advanced lens material is welcome: the user's goal is mastery, not a grade. Every advanced destination must be reached by a complete ladder from what's already understood, under `🔭 Beyond the lecture`, after the concept's core is locked. If the ladder cannot be built fully in this session, omit the destination entirely — never name-drop.

## 8. Far domains and accuracy

For domains outside reliable knowledge (medicine, law, finance, fast-moving tools), verify lens facts by search and cite. Medical examples are illustrative, not clinical guidance — say so once. Prefer well-established facts over niche claims.

## 9. Focus mode and combined lenses

- **Focus mode** ("ركز على المجال", "focus on the lens", "I'll use this in my startup"): the lens becomes the goal. Still teach the lecture core first and completely, then give the lens a large, dedicated section per part (deeper extensions, bigger exercises).
- **Combined** (`- ai agent - medical`): the goal lens drives; the domain lens supplies the scenarios ("an AI agent engineer building clinical triage agents").
- **No lens:** examples come from the lecture's natural domain.

## 10. Lens knowledge maps

Starting points for tiering. Always re-judge against the actual lecture; these are not a substitute for thinking.

### AI Agent Engineer

| Lecture area | Direct / Indirect uses |
|---|---|
| Python fundamentals | Functions as tools; dicts/JSON as the tool-call and message format; exceptions for tool failures and retries; type hints and dataclasses/Pydantic for tool schemas and structured output; decorators for tool registration; generators for streaming; async/await for parallel tool calls; context managers for resources (Direct) |
| Data structures & algorithms | Graphs for agent workflows and state machines; queues and priority queues for task scheduling; trees and search (BFS/DFS, best-first, MCTS) for planning; hashing and caching for memoization of tool results (Direct/Indirect) |
| Probability & statistics | Sampling and temperature; uncertainty and confidence; Bayes for belief updates and LLM-as-judge reliability; evaluation design, variance across runs, significance (Direct) |
| Linear algebra | Embeddings, cosine similarity, vector search for retrieval and memory (Direct); attention internals (Indirect) |
| Calculus & optimization | Training and fine-tuning (Indirect); rarely used directly in agent building |
| Databases | Agent memory stores, retrieval, SQL tools, vector DBs (Direct) |
| OS & concurrency | Processes, threads, async, sandboxing for code-executing agents, timeouts (Direct) |
| Networking & web | HTTP APIs, rate limits, retries with backoff, auth, webhooks (Direct) |
| Software engineering | Testing and evals, logging and tracing, modular design, state management (Direct) |
| Security | Prompt injection as untrusted input, least privilege for tools, input validation (Direct) |

### AI Infrastructure Engineer

| Lecture area | Direct / Indirect uses |
|---|---|
| Python / systems programming | Resource cleanup (try/finally, context managers), subprocesses, profiling, concurrency, memory behavior (Direct) |
| Linear algebra | Matrix multiplication cost, GPU utilization, memory bandwidth vs compute bound, batching (Direct) |
| Calculus & optimization | Backprop memory (activations), optimizer state memory, mixed precision (Indirect/Direct) |
| Probability & statistics | Alerting and base rates, latency percentiles (p50/p99), capacity planning, load testing (Direct) |
| Data structures & algorithms | Scheduling, load balancing, caching (KV cache), consistent hashing, queues (Direct) |
| OS & architecture | Processes, memory hierarchy, virtualization and containers, I/O (Direct) |
| Networking & distributed systems | Collective communication, bandwidth and latency, fault tolerance, consistency (Direct) |
| Databases | Storage systems, data pipelines, checkpointing (Direct) |
