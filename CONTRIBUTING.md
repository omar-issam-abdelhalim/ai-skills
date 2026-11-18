# Contributing

Thanks for taking the time to improve these skills.

## Reporting a problem

Open an issue with:
- the skill name and version (from its frontmatter),
- what you asked the agent and which agent/app you used,
- what happened and what you expected,
- the smallest input that reproduces it (strip any private data).

## Proposing a change

1. Fork the repository and create a branch: `fix/<skill>-<short-topic>` or `feat/<skill>-<short-topic>`.
2. Follow [docs/AUTHORING.md](docs/AUTHORING.md).
3. Keep changes focused: one skill and one concern per pull request.
4. If you change a script, update or add its test in `tests/`.
5. Bump the skill's `metadata.version` (semantic versioning: patch for fixes, minor for new behaviour, major for breaking changes to inputs or outputs) and add a line to `CHANGELOG.md`.
6. Run the checks locally:
   ```bash
   pip install pyyaml pytest genanki sympy
   python scripts/validate_skills.py
   pytest -q
   ```
7. Open the pull request and describe the problem, the change and how you tested it.

## Adding a new skill

New skills are welcome when they encode a real, repeatable workflow with clear triggers and verifiable output. Include at least one worked example or test that shows the output quality, and add the skill to the README index.
