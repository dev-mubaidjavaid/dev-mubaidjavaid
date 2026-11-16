import re
import xml.etree.ElementTree as ET
from pathlib import Path

root = Path(__file__).resolve().parents[1]
readme = (root / "README.md").read_text(encoding="utf-8")
paths = re.findall(r"\./assets/[^)\s\"]+", readme)
missing = [p for p in sorted(set(paths)) if not (root / p[2:]).exists()]
print("refs", len(set(paths)), "missing", missing)

errs = []
svgs = list((root / "assets").rglob("*.svg"))
for s in svgs:
    try:
        ET.parse(s)
    except Exception as e:
        errs.append((str(s.relative_to(root)), str(e)))
print("svgs", len(svgs), "errors", errs)

links = sorted(set(re.findall(r"https?://[^)\s\"]+", readme)))
print("links")
for link in links:
    print(" ", link)
