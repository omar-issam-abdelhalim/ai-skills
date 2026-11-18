#!/usr/bin/env python3
"""
Extract a lecture (PDF or PPTX) into per-page text + page images, and flag pages
whose text extraction is likely unreliable (equations, diagrams, figures, scans).

Usage:
    python extract_lecture.py <file> [<file> ...] [--out DIR] [--dpi 110]

Output (per input file, under DIR/<stem>/):
    pages.md          per-page (per-slide) text, with speaker notes for PPTX
    img/page-NNN.png  rendered page images
    report.json       page count, flagged pages with reasons
A summary is printed at the end: VIEW the flagged page images before teaching.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

MATH_CHARS = set("∑∫∂√∞≈≠≤≥±×÷∇∈∉⊂⊆∪∩→⇒⇔αβγδεθλμσφωΣΠΔΩ^_=")


def render_pdf(pdf: Path, img_dir: Path, dpi: int) -> None:
    img_dir.mkdir(parents=True, exist_ok=True)
    if shutil.which("pdftoppm"):
        subprocess.run(
            ["pdftoppm", "-png", "-r", str(dpi), str(pdf), str(img_dir / "page")],
            check=False, capture_output=True,
        )
        # normalize names to page-NNN.png
        for p in img_dir.glob("page-*.png"):
            num = int(re.findall(r"(\d+)", p.stem)[-1])
            p.rename(img_dir / f"page-{num:03d}.png")
        return
    try:
        import pypdfium2 as pdfium
        doc = pdfium.PdfDocument(str(pdf))
        for i in range(len(doc)):
            doc[i].render(scale=dpi / 72).to_pil().save(img_dir / f"page-{i+1:03d}.png")
    except Exception as e:  # pragma: no cover
        print(f"[warn] could not render {pdf.name}: {e}", file=sys.stderr)


def flag_reasons(text: str, n_images: int, n_curves: int) -> list:
    reasons = []
    stripped = text.strip()
    if len(stripped) < 40:
        reasons.append("little or no extractable text (image/scan/diagram)")
    if n_images > 0:
        reasons.append(f"{n_images} embedded image(s)")
    if n_curves > 15:
        reasons.append("vector graphics (diagram/plot)")
    math_hits = sum(1 for c in stripped if c in MATH_CHARS)
    if math_hits >= 6:
        reasons.append("math-dense (verify equations visually)")
    if re.search(r"\(cid:\d+\)|\ufffd", stripped):
        reasons.append("garbled glyphs")
    return reasons


def extract_pdf(pdf: Path, out: Path, dpi: int, notes: dict | None = None) -> dict:
    import pdfplumber
    out.mkdir(parents=True, exist_ok=True)
    lines, flagged = [], []
    with pdfplumber.open(str(pdf)) as doc:
        n = len(doc.pages)
        for i, page in enumerate(doc.pages, start=1):
            text = page.extract_text() or ""
            reasons = flag_reasons(text, len(page.images), len(page.curves) + len(page.rects))
            lines.append(f"\n## Page {i}\n")
            lines.append(text.strip() or "_(no extractable text)_")
            if notes and notes.get(i):
                lines.append(f"\n**Speaker notes:** {notes[i]}")
            if reasons:
                flagged.append({"page": i, "reasons": reasons})
    (out / "pages.md").write_text("\n".join(lines), encoding="utf-8")
    render_pdf(pdf, out / "img", dpi)
    return {"pages": n, "flagged": flagged}


def pptx_notes_and_text(pptx: Path) -> tuple:
    from pptx import Presentation
    prs = Presentation(str(pptx))
    notes, texts = {}, {}
    for i, slide in enumerate(prs.slides, start=1):
        parts = []
        for shape in slide.shapes:
            if shape.has_text_frame:
                parts.append(shape.text_frame.text)
            if getattr(shape, "has_table", False) and shape.has_table:
                for row in shape.table.rows:
                    parts.append(" | ".join(c.text for c in row.cells))
        texts[i] = "\n".join(p for p in parts if p.strip())
        if slide.has_notes_slide:
            n = slide.notes_slide.notes_text_frame.text.strip()
            if n:
                notes[i] = n
    return texts, notes


def extract_pptx(pptx: Path, out: Path, dpi: int) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    texts, notes = pptx_notes_and_text(pptx)
    pdf = None
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if soffice:
        subprocess.run(
            [soffice, "--headless", "--convert-to", "pdf", "--outdir", str(out), str(pptx)],
            check=False, capture_output=True, timeout=240,
        )
        cand = out / (pptx.stem + ".pdf")
        pdf = cand if cand.exists() else None
    if pdf:
        report = extract_pdf(pdf, out, dpi, notes)
        # prefer python-pptx text if the PDF text layer is poor
        md = [f"\n## Slide {i}\n\n{t or '_(no text)_'}" + (f"\n\n**Speaker notes:** {notes[i]}" if notes.get(i) else "")
              for i, t in texts.items()]
        (out / "pages.md").write_text("\n".join(md), encoding="utf-8")
        report["speaker_notes_slides"] = sorted(notes)
        return report
    md = [f"\n## Slide {i}\n\n{t or '_(no text)_'}" + (f"\n\n**Speaker notes:** {notes[i]}" if notes.get(i) else "")
          for i, t in texts.items()]
    (out / "pages.md").write_text("\n".join(md), encoding="utf-8")
    flagged = [{"page": i, "reasons": ["could not render; check slide for visuals"]}
               for i, t in texts.items() if len(t.strip()) < 40]
    return {"pages": len(texts), "flagged": flagged, "speaker_notes_slides": sorted(notes),
            "warning": "no renderer available; images not produced"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--out", default="lecture")
    ap.add_argument("--dpi", type=int, default=110)
    args = ap.parse_args()
    root = Path(args.out)
    summary = {}
    for f in args.files:
        path = Path(f)
        if not path.exists():
            print(f"[error] not found: {path}", file=sys.stderr)
            continue
        dest = root / path.stem
        ext = path.suffix.lower()
        if ext == ".pdf":
            rep = extract_pdf(path, dest, args.dpi)
        elif ext in (".pptx", ".ppt"):
            rep = extract_pptx(path, dest, args.dpi)
        else:
            print(f"[skip] unsupported type: {path.name} (read it directly)")
            continue
        (dest / "report.json").write_text(json.dumps(rep, indent=2, ensure_ascii=False), encoding="utf-8")
        summary[path.name] = rep
        print(f"\n=== {path.name}: {rep['pages']} pages → {dest}")
        print(f"text:   {dest / 'pages.md'}")
        print(f"images: {dest / 'img'}")
        if rep.get("speaker_notes_slides"):
            print(f"speaker notes on slides: {rep['speaker_notes_slides']}")
        if rep["flagged"]:
            print("VIEW these page images before teaching:")
            for fl in rep["flagged"]:
                print(f"  page {fl['page']:>3}: {', '.join(fl['reasons'])}")
        else:
            print("no pages flagged")
    if not summary:
        sys.exit(1)


if __name__ == "__main__":
    main()
