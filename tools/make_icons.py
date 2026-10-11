#!/usr/bin/env python3
"""Draw the app's icons: an iris with a slit pupil, white on black. Usage: python3 -I tools/make_icons.py"""
import pathlib
from PIL import Image, ImageDraw

root = pathlib.Path(__file__).resolve().parent.parent
out = root / "icons"
out.mkdir(exist_ok=True)


def icon(size, pad):
    s = 4                                   # draw large, then reduce, for clean edges
    n = size * s
    im = Image.new("RGB", (n, n), (0, 0, 0))
    d = ImageDraw.Draw(im)
    c = n / 2
    r = n * (0.5 - pad) * 0.86              # iris radius
    w = max(2, round(n * 0.028))
    d.ellipse([c - r, c - r, c + r, c + r], outline=(255, 255, 255), width=w)
    rx, ry = r * 0.17, r * 0.74             # the pupil: a vertical slit
    d.ellipse([c - rx, c - ry, c + rx, c + ry], fill=(255, 255, 255))
    return im.resize((size, size), Image.LANCZOS)


icon(180, 0.10).save(out / "icon-180.png")
icon(192, 0.10).save(out / "icon-192.png")
icon(512, 0.10).save(out / "icon-512.png")
icon(512, 0.20).save(out / "icon-maskable-512.png")   # more margin, for launchers that crop to a circle
print("icons written to", out)
