"""Tests for the executable parts of the skills (run: pytest -q)."""
import importlib.util
import json
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------- repository validator ----------
def test_validator_passes():
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_skills.py")], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


# ---------- anki-lecture-cards ----------
anki = load(SKILLS / "anki-lecture-cards" / "scripts" / "build_apkg.py", "build_apkg")


@pytest.mark.parametrize("key,deck", [
    ("chem 101", "Uni::CHEM101"),
    ("CS-301", "Uni::CS301"),
    ("math201", "Uni::MATH201"),
    ("AI Agents", "AI::Agents"),
    ("Books::Deep Learning", "Books::Deep Learning"),
])
def test_resolve_deck(key, deck):
    assert anki.resolve_deck(key)[0] == deck


@pytest.mark.parametrize("raw,label", [
    (3, "L03"), ("L3", "L03"), ("lec 03", "L03"), ("Lecture 12", "L12"),
    ("Sheet 2", "Sheet02"), ("Lab 1", "Lab01"), (None, None), ("", None),
])
def test_lecture_label(raw, label):
    assert anki.lecture_label(raw) == label


def test_stable_ids_are_deterministic():
    assert anki.stable_id("deck::Uni::CHEM101") == anki.stable_id("deck::Uni::CHEM101")
    assert anki.stable_id("a") != anki.stable_id("b")


def test_validation_catches_bad_cards():
    errors, warnings = anki.validate([
        {"type": "basic", "front": "Q?", "back": ""},
        {"type": "cloze", "text": "no deletion here"},
        {"type": "basic", "front": "Same front", "back": "x"},
        {"type": "basic", "front": "same  FRONT", "back": "y"},
    ])
    assert len(errors) == 2
    assert any("near-duplicate" in w for w in warnings)


def test_build_writes_apkg(tmp_path):
    spec = {
        "deck": "CHEM 101", "lecture": 3, "deck_description": "CHEM101 — General Chemistry I",
        "cards": [
            {"type": "basic", "front": "How does a catalyst increase reaction rate?",
             "back": "It provides a pathway with lower activation energy.", "tags": ["Type::Concept"]},
            {"type": "cloze", "text": "A catalyst is {{c1::not consumed}} by the reaction.", "tags": ["Type::Concept"]},
        ],
    }
    out = anki.build(spec, str(tmp_path))
    assert Path(out["file"]).name == "CHEM101_L03.apkg"
    assert out["notes"] == {"basic": 1, "cloze": 1}
    assert zipfile.is_zipfile(out["file"])


# ---------- lecture-mastery ----------
VERIFY = SKILLS / "lecture-mastery" / "scripts" / "verify_math.py"


@pytest.mark.parametrize("args", [
    ["equal", "(x+1)**2", "x**2+2*x+1"],
    ["diff", "sin(x)*exp(x)", "x"],
    ["integrate", "x*exp(x)", "x", "0", "1"],
    ["solve", "x**2-5*x+6", "x"],
])
def test_verify_math_runs(args):
    r = subprocess.run([sys.executable, str(VERIFY), *args], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip()


def test_verify_math_detects_inequality():
    r = subprocess.run([sys.executable, str(VERIFY), "equal", "(x+1)**2", "x**2+1"], capture_output=True, text=True)
    assert "False" in r.stdout or "NOT" in r.stdout.upper()


# ---------- exam-lab ----------
EXAM = SKILLS / "exam-lab"


@pytest.mark.skipif(shutil.which("node") is None, reason="node not installed")
def test_exam_example_passes_quality_gates():
    r = subprocess.run(["node", str(EXAM / "scripts" / "check.js"), str(EXAM / "assets" / "example-data.js")],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout


def test_exam_build_injects_data(tmp_path):
    out = tmp_path / "app.html"
    subprocess.run([sys.executable, str(EXAM / "scripts" / "build.py"), str(EXAM / "assets" / "template.html"),
                    str(EXAM / "assets" / "example-data.js"), str(out)], check=True, capture_output=True)
    html = out.read_text(encoding="utf-8")
    assert "Intro to Psychology" in html
    assert html.count("/*__DATA_START__*/") == 1 and html.count("/*__DATA_END__*/") == 1
