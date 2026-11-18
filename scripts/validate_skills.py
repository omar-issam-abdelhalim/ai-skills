#!/usr/bin/env python3
"""
Validate every skill in skills/ against the repository's authoring rules.

Checks
  - SKILL.md exists and starts with YAML frontmatter
  - name: lowercase-hyphen, <= 64 chars, equals the folder name
  - description: present, <= 1024 chars
  - license and metadata.version present
  - every relative file the skill mentions (references/, scripts/, assets/, templates/) exists
  - no sandbox-specific absolute paths or personal identifiers leak into a skill
  - the root README indexes every skill

Usage:  python scripts/validate_skills.py [--root .]
Exit code 1 if any check fails.
"""
import argparse
import re
import sys
from pathlib import Path

import yaml

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
REF_RE = re.compile(r"`?((?:references|scripts|assets|templates)/[A-Za-z0-9_.\-/]+\.[A-Za-z0-9]+)`?")
LEAK_PATTERNS = {
    "absolute machine path": re.compile(r"/mnt/[a-z-]+/|/home/[a-z_][a-z0-9_-]*/|[A-Z]:\\Users\\"),
    "email address": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?:com|edu|eg|org|net)\b"),
    "drive folder id": re.compile(r"drive\.google\.com/drive/folders/[A-Za-z0-9_-]{20,}"),
}


def frontmatter(text: str):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    return yaml.safe_load(m.group(1)), text[m.end():]


def check_skill(folder: Path) -> list[str]:
    errs = []
    skill_md = folder / "SKILL.md"
    if not skill_md.exists():
        return [f"{folder.name}: missing SKILL.md"]
    text = skill_md.read_text(encoding="utf-8")
    fm, _ = frontmatter(text)
    if fm is None:
        return [f"{folder.name}: SKILL.md has no YAML frontmatter"]

    name = fm.get("name", "")
    if not NAME_RE.match(str(name)) or len(str(name)) > 64:
        errs.append(f"{folder.name}: invalid name '{name}'")
    if name != folder.name:
        errs.append(f"{folder.name}: name '{name}' does not match folder")
    desc = fm.get("description") or ""
    if not desc.strip():
        errs.append(f"{folder.name}: empty description")
    if len(desc) > 1024:
        errs.append(f"{folder.name}: description is {len(desc)} chars (max 1024)")
    if not fm.get("license"):
        errs.append(f"{folder.name}: missing license")
    if not (fm.get("metadata") or {}).get("version"):
        errs.append(f"{folder.name}: missing metadata.version")

    for f in sorted(folder.rglob("*")):
        if not f.is_file() or f.suffix not in {".md", ".py", ".js", ".html", ".json"}:
            continue
        body = f.read_text(encoding="utf-8", errors="ignore")
        rel = f.relative_to(folder)
        for ref in sorted(set(REF_RE.findall(body))):
            if "<" in ref or "*" in ref or "NN" in ref:
                continue
            if not (folder / ref).exists():
                errs.append(f"{folder.name}/{rel}: references missing file '{ref}'")
        for label, rx in LEAK_PATTERNS.items():
            hit = rx.search(body)
            if hit:
                errs.append(f"{folder.name}/{rel}: {label} found: '{hit.group(0)}'")
    return errs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    root = ap.parse_args().root
    skills = sorted(p for p in (root / "skills").iterdir() if p.is_dir())
    readme = (root / "README.md").read_text(encoding="utf-8")

    errors = []
    for s in skills:
        errors += check_skill(s)
        if f"skills/{s.name}" not in readme:
            errors.append(f"README.md: skill '{s.name}' is not indexed")

    for e in errors:
        print("ERROR", e)
    print(f"checked {len(skills)} skills · {len(errors)} error(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
