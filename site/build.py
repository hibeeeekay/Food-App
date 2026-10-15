#!/usr/bin/env python3
"""
Sweet Flavour Magazino — build script.

Takes site/_template.html (readable source) and embeds every image as a
base64 data URI, producing a single portable file: index.html

Run:  python3 site/build.py
"""
import base64, pathlib, sys, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
TPL  = ROOT / "site" / "_template.html"
OUT  = ROOT / "index.html"
WEB  = ROOT / "web"

MAP = {
    "{{HERO}}":         "hero.jpg",
    "{{CEO}}":          "ceo.jpg",
    "{{SVC_PASTRIES}}": "svc-pastries.jpg",
    "{{SVC_CAKES}}":    "svc-cakes.jpg",
    "{{SVC_PARTY}}":    "svc-party.jpg",
    "{{SVC_SOUP}}":     "svc-soup.jpg",
    "{{GAL_WEDDING}}":  "gal-cake-wedding.jpg",
    "{{GAL_BIRTHDAY}}": "gal-cake-birthday.jpg",
    "{{GAL_MEATPIE}}":  "gal-pastry-meatpie.jpg",
    "{{GAL_PLATTER}}":  "gal-chops-platter.jpg",
    "{{GAL_PUFFPUFF}}": "gal-chops-puffpuff.jpg",
}

def main() -> int:
    if not TPL.exists():
        print(f"ERROR: missing template {TPL}", file=sys.stderr)
        return 1

    html = TPL.read_text(encoding="utf-8")

    for token, filename in MAP.items():
        path = WEB / filename
        if not path.exists():
            print(f"ERROR: missing image {path}", file=sys.stderr)
            return 1
        uri = "data:image/jpeg;base64," + base64.b64encode(path.read_bytes()).decode("ascii")
        count = html.count(token)
        if count == 0:
            # A card was removed from the template; skip this image quietly.
            print(f"  (skipped {token}: not used in template)")
            continue
        html = html.replace(token, uri)

    leftovers = re.findall(r"\{\{[A-Z_]+\}\}", html)
    if leftovers:
        print(f"ERROR: unreplaced tokens: {set(leftovers)}", file=sys.stderr)
        return 1

    OUT.write_text(html, encoding="utf-8")
    size_mb = len(html.encode("utf-8")) / 1024 / 1024
    print(f"✓ Built {OUT}  ({size_mb:.2f} MB, single self-contained file)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
