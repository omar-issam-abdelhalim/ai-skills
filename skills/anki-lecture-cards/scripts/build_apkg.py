"""
Deterministic Anki .apkg builder for the anki-lecture-cards skill.

Guarantees (do not change the constants below, the user's Anki depends on them):
  same deck key  -> same deck ID + name   (cards always land in the same deck)
  same card      -> same GUID             (re-importing never duplicates)
  note types     -> fixed IDs             ("StudyPipeline Basic" / "StudyPipeline Cloze")

Usage:
  python build_apkg.py spec.json OUTPUT        # OUTPUT = file.apkg or a directory
"""
import hashlib
import json
import os
import re
import sys
from datetime import date

import genanki


# ---------- identity ----------
def stable_id(key: str) -> int:
    return int(hashlib.sha256(key.encode("utf-8")).hexdigest()[:12], 16)


def normalize_code(raw: str) -> str:
    return re.sub(r"[\s\-_]+", "", raw).upper()


COURSE_CODE = re.compile(r"^[A-Za-z]{2,6}[\s\-_]*\d{2,4}[A-Za-z]?$")


def resolve_deck(key: str):
    key = key.strip()
    if "::" in key:
        name = "::".join(p.strip() for p in key.split("::"))
        return name, name.replace(" ", "_")
    if COURSE_CODE.match(key):
        code = normalize_code(key)
        return f"Uni::{code}", f"Uni::{code}"
    name = "::".join(p[:1].upper() + p[1:] for p in key.split())
    return name, name.replace(" ", "_")


def lecture_label(lec):
    """3 / '3' / 'L3' / 'lec 03' / 'Lecture 3' -> 'L03';  'Sheet 2' -> 'Sheet02'."""
    if lec is None or str(lec).strip() == "":
        return None
    s = str(lec).strip()
    m = re.match(r"^(?:l|lec|lecture)?[\s\-_.]*0*(\d+)$", s, re.I)
    if m:
        return f"L{int(m.group(1)):02d}"
    m = re.match(r"^([A-Za-z]+)[\s\-_.]*0*(\d+)$", s)
    if m:
        return f"{m.group(1).capitalize()}{int(m.group(2)):02d}"
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")


def semester_tag(d=None):
    d = d or date.today()
    if d.month >= 9:
        return f"Sem::{d.year}-Fall"
    if d.month == 1:
        return f"Sem::{d.year - 1}-Fall"
    if d.month <= 6:
        return f"Sem::{d.year}-Spring"
    return f"Sem::{d.year}-Summer"


# ---------- note types (FIXED IDs) ----------
CSS = """
.card {
  font-family: -apple-system, "Segoe UI", Roboto, "Noto Sans Arabic", sans-serif;
  font-size: 21px; line-height: 1.55; text-align: left;
  color: #1f2328; background: #ffffff;
  max-width: 720px; margin: 0 auto; padding: 18px;
}
.nightMode.card, .night_mode .card { color: #e6e6e6; background: #1e1e1e; }
.front { font-weight: 600; }
hr#answer { border: none; border-top: 1px solid #8884; margin: 18px 0; }
.extra {
  margin-top: 16px; padding: 10px 14px; border-radius: 8px;
  background: #8881; font-size: 18px;
  unicode-bidi: plaintext; text-align: start;
}
.source { margin-top: 14px; font-size: 13px; opacity: .55; }
code, pre { font-family: Consolas, "JetBrains Mono", monospace; font-size: 17px; }
pre { background: #8882; padding: 10px; border-radius: 6px; overflow-x: auto; text-align: left; direction: ltr; }
.cloze { font-weight: 700; color: #0969da; }
.nightMode .cloze { color: #58a6ff; }
"""

BASIC_MODEL = genanki.Model(
    stable_id("StudyPipeline::Basic::v1"),
    "StudyPipeline Basic",
    fields=[{"name": "Front"}, {"name": "Back"}, {"name": "Extra"}, {"name": "Source"}],
    templates=[{
        "name": "Card 1",
        "qfmt": '<div class="front">{{Front}}</div>',
        "afmt": ('<div class="front">{{Front}}</div><hr id="answer">'
                 '<div class="back">{{Back}}</div>'
                 '{{#Extra}}<div class="extra" dir="auto">{{Extra}}</div>{{/Extra}}'
                 '{{#Source}}<div class="source">{{Source}}</div>{{/Source}}'),
    }],
    css=CSS,
)

CLOZE_MODEL = genanki.Model(
    stable_id("StudyPipeline::Cloze::v1"),
    "StudyPipeline Cloze",
    fields=[{"name": "Text"}, {"name": "Extra"}, {"name": "Source"}],
    templates=[{
        "name": "Cloze",
        "qfmt": '<div class="front">{{cloze:Text}}</div>',
        "afmt": ('<div class="front">{{cloze:Text}}</div>'
                 '{{#Extra}}<div class="extra" dir="auto">{{Extra}}</div>{{/Extra}}'
                 '{{#Source}}<div class="source">{{Source}}</div>{{/Source}}'),
    }],
    css=CSS,
    model_type=genanki.Model.CLOZE,
)


# ---------- validation ----------
def validate(cards):
    errors, warnings = [], []
    fronts = {}
    for i, c in enumerate(cards, 1):
        kind = c.get("type", "basic")
        if kind not in ("basic", "cloze"):
            errors.append(f"card {i}: unknown type '{kind}'")
            continue
        if kind == "basic":
            if not c.get("front", "").strip() or not c.get("back", "").strip():
                errors.append(f"card {i}: basic card needs non-empty front and back")
                continue
            key = c["front"]
        else:
            text = c.get("text", "")
            if not re.search(r"\{\{c\d+::", text):
                errors.append(f"card {i}: cloze card has no {{{{c1::...}}}} deletion")
                continue
            if re.search(r"\\[\(\[][^\]\)]*\{\{c\d+::", text):
                warnings.append(f"card {i}: cloze inside MathJax, '}}}}' in LaTeX can break it")
            key = text
        norm = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", key)).strip().lower()
        if norm in fronts:
            warnings.append(f"card {i}: near-duplicate of card {fronts[norm]}; remove one")
        else:
            fronts[norm] = i
        blob = " ".join(str(v) for v in c.values() if isinstance(v, str))
        if re.search(r"\$[^$]+\$", blob) and "\\" in blob:
            warnings.append(f"card {i}: looks like $...$ LaTeX; use \\( \\) or \\[ \\] instead")
        if "**" in blob:
            warnings.append(f"card {i}: markdown '**' found; fields are HTML, use <b>")
        if kind == "basic" and len(re.sub(r"<[^>]+>", "", c["back"])) > 280:
            warnings.append(f"card {i}: long back ({len(c['back'])} chars); consider splitting or moving detail to extra")
    return errors, warnings


# ---------- build ----------
def build(spec, out):
    deck_name, tag_root = resolve_deck(spec["deck"])
    lec = lecture_label(spec.get("lecture"))
    deck = genanki.Deck(stable_id("deck::" + deck_name), deck_name, spec.get("deck_description", ""))

    errors, warnings = validate(spec["cards"])
    if errors:
        print("VALIDATION FAILED:\n  " + "\n  ".join(errors))
        sys.exit(1)

    base_tags = [semester_tag(), f"{tag_root}::{lec}" if lec else tag_root]
    counts, seen, type_tags = {"basic": 0, "cloze": 0}, set(), {}
    for c in spec["cards"]:
        kind = c.get("type", "basic")
        extra_tags = [re.sub(r"\s+", "_", t.strip()) for t in c.get("tags", []) if t.strip()]
        for t in extra_tags:
            if t.startswith("Type::"):
                type_tags[t] = type_tags.get(t, 0) + 1
        if kind == "cloze":
            key = c["text"]
            fields = [c["text"], c.get("extra", ""), c.get("source", "")]
            model = CLOZE_MODEL
        else:
            key = c["front"]
            fields = [c["front"], c["back"], c.get("extra", ""), c.get("source", "")]
            model = BASIC_MODEL
        guid = genanki.guid_for(deck_name, lec or "", key)
        if guid in seen:
            continue
        seen.add(guid)
        deck.add_note(genanki.Note(model=model, fields=fields, tags=base_tags + extra_tags, guid=guid))
        counts[kind] += 1

    if os.path.isdir(out) or not out.endswith(".apkg"):
        os.makedirs(out, exist_ok=True)
        short = deck_name.replace("Uni::", "").replace("::", "_")
        out = os.path.join(out, f"{short}_{lec}.apkg" if lec else f"{short}.apkg")
    genanki.Package(deck).write_to_file(out)

    return {"file": out, "deck": deck_name, "tags": base_tags,
            "notes": counts, "by_type": type_tags, "warnings": warnings}


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__.strip())
        sys.exit(2)
    with open(sys.argv[1], encoding="utf-8") as f:
        spec = json.load(f)
    print(json.dumps(build(spec, sys.argv[2]), ensure_ascii=False, indent=2))
