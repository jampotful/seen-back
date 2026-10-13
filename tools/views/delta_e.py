#!/usr/bin/env python3
"""Colour difference between two renders, for the visibility floor (docs/ENGINE-DESIGN.md, section 5).
Usage: python3 -I tools/views/delta_e.py a.png b.png   ->  prints the 95th percentile of CIE 1976 delta E*ab, per pixel, as JSON.
Both images are blurred a little first (a Gaussian of 1 device pixel), a rough stand-in for the eye's falloff in contrast sensitivity at
a phone's pixel density; the eye model of the design is not implemented, and this is the app's own simplification.
"""
import json, sys
import numpy as np
from PIL import Image, ImageFilter


def lab(img):
    a = np.asarray(img.convert("RGB").filter(ImageFilter.GaussianBlur(1)), dtype=np.float64) / 255.0
    a = np.where(a <= 0.04045, a / 12.92, ((a + 0.055) / 1.055) ** 2.4)   # sRGB to linear
    M = np.array([[0.4124564, 0.3575761, 0.1804375], [0.2126729, 0.7151522, 0.0721750], [0.0193339, 0.1191920, 0.9503041]])
    xyz = a @ M.T / np.array([0.95047, 1.0, 1.08883])                       # D65 white
    f = np.where(xyz > (6 / 29) ** 3, np.cbrt(xyz), xyz / (3 * (6 / 29) ** 2) + 4 / 29)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


a, b = Image.open(sys.argv[1]), Image.open(sys.argv[2])
d = np.sqrt(((lab(a) - lab(b)) ** 2).sum(-1))
print(json.dumps({"p95": round(float(np.percentile(d, 95)), 3), "mean": round(float(d.mean()), 3), "max": round(float(d.max()), 2)}))
