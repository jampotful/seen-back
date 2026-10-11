#!/usr/bin/env python3
"""Turn every PNG under a directory into a JPEG whose longest side is at most 1100 px, and keep the total under 8 MB.
Usage: python3 -I ci/engines/shrink.py <dir>   (needs Pillow)"""
import os, sys
from PIL import Image

root = sys.argv[1]
pngs = [os.path.join(d, f) for d, _, fs in os.walk(root) for f in fs if f.lower().endswith(".png")]


def total():
    return sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk(root) for f in fs)


for q, side in ((72, 1100), (55, 900), (45, 700)):
    for p in pngs:
        j = p[:-4] + ".jpg"
        src = p if os.path.exists(p) else None
        if not src:
            continue
        im = Image.open(src).convert("RGB")
        im.thumbnail((side, side))
        im.save(j, "JPEG", quality=q, optimize=True)
    if total() < 8 * 1024 * 1024:
        break
for p in pngs:
    if os.path.exists(p[:-4] + ".jpg"):
        os.remove(p)
print("pictures:", len(pngs), "total bytes:", total())
