# Changelog

All notable changes to this repository are documented here. Skills are versioned individually through `metadata.version` in their frontmatter.

## [1.0.0] — 2026-11-18

### Added
- **lecture-mastery**: lecture teaching engine with type-specific playbooks, goal/domain lenses, checkpoints, mastery check, and `extract_lecture.py` / `verify_math.py` scripts.
- **book-mastery**: multi-session mastery of large technical books with a persistent ledger (Notion or Markdown backend).
- **anki-lecture-cards**: study material → deterministic Anki `.apkg` builder with card validation.
- **exam-lab**: offline exam-prep app kit (template, data injector, quality-gate checker, example dataset).
- **circuit-lab**: five-phase electronics project pipeline with analysis method, Proteus and Tinkercad playbooks, and templates.
- **trend-content**: AI-news carousel pipeline with scoring rubric, critic pass, configurable brand profile, HTML slide system and `render_slides.py`.
- **meeting-report**: decision-grade meeting reports with decision/action registers and a team config template.
- Repository tooling: `scripts/validate_skills.py`, tests for every script, CI workflow, authoring guide and contributing guide.

### Changed
- **article-mastery**: moved under `skills/`, frontmatter aligned with the Agent Skills format.
- README rewritten as a full index with install instructions and per-skill requirements.

## [0.1.0] — 2026-07-15

### Added
- Initial repository with the `article-mastery` specification.
