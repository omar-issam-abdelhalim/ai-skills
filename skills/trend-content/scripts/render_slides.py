#!/usr/bin/env python3
"""
Render carousel slides (HTML) to 1080x1350 PNGs and flag overflow.

Usage:
    python render_slides.py SLIDES_DIR OUT_DIR [--scale 1]

Every *.html file in SLIDES_DIR is rendered in sorted order to OUT_DIR/<name>.png.
A slide "overflows" when its #slide element (or the page body) is larger than
1080x1350, i.e. text or a component spills outside the frame. Overflowing slides
are listed at the end and the exit code is 1, so the agent knows what to fix.

Requires: pip install playwright && python -m playwright install chromium
"""
import argparse
import json
import sys
from pathlib import Path

WIDTH, HEIGHT = 1080, 1350

MEASURE_JS = """
() => {
  const el = document.getElementById('slide') || document.body;
  return {w: el.scrollWidth, h: el.scrollHeight};
}
"""


def render(slides_dir: Path, out_dir: Path, scale: float) -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("playwright is not installed: pip install playwright && python -m playwright install chromium")
        return 2

    files = sorted(slides_dir.glob("*.html"))
    if not files:
        print(f"no .html slides found in {slides_dir}")
        return 2
    out_dir.mkdir(parents=True, exist_ok=True)

    results, overflow = [], []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": WIDTH, "height": HEIGHT}, device_scale_factor=scale)
        for f in files:
            page.goto(f.resolve().as_uri())
            page.wait_for_load_state("networkidle")
            size = page.evaluate(MEASURE_JS)
            png = out_dir / f"{f.stem}.png"
            page.screenshot(path=str(png), clip={"x": 0, "y": 0, "width": WIDTH, "height": HEIGHT})
            ok = size["w"] <= WIDTH and size["h"] <= HEIGHT
            if not ok:
                overflow.append(f.name)
            results.append({"slide": f.name, "png": str(png), "content": size, "fits": ok})
        browser.close()

    print(json.dumps({"rendered": results, "overflow": overflow}, indent=2))
    return 1 if overflow else 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slides_dir", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--scale", type=float, default=1.0, help="device scale factor (2 = retina PNGs)")
    args = ap.parse_args()
    sys.exit(render(args.slides_dir, args.out_dir, args.scale))


if __name__ == "__main__":
    main()
