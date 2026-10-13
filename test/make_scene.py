#!/usr/bin/env python3
"""Draw the scene clip the engine's checks run on: test/assets/scene.webm. Run with python3 -I test/make_scene.py.

Four seconds at 30 frames a second, 540 by 960 (a phone held upright), cut from test/assets/garden.jpg, with:
  - a hand's small tremor all through, and a slow pan between 2.4 s and 3.4 s;
  - a beetle that walks steadily on six legs moving in two alternating sets of three (living, jointed and rhythmic);
  - a fly that walks in short bursts and buzzes its wings while it stands (living, rhythmic);
  - an orange ball that slides at one speed in a straight line (moving, coherent, not rhythmic);
  - a patch of glints that change at random every frame (flicker with no coherent motion).
Everything moves with the background, so the pan moves the whole scene. Needs numpy, Pillow and ffmpeg with libvpx.
test/assets/scene.json gives where each of the four is in every frame, as fractions of the width and of the height from the top,
so that a check can tell what the gaze looked at.
"""
import json, math, pathlib, random, subprocess
import numpy as np
from PIL import Image, ImageDraw

here = pathlib.Path(__file__).resolve().parent
W, H, FPS, SECONDS = 540, 960, 30, 4
MARGIN = 80
random.seed(11)
rng = np.random.default_rng(11)

garden = Image.open(here / 'assets' / 'garden.jpg').convert('RGB')        # 1600 x 1200
crop_w = round(garden.height * (W + 2 * MARGIN) / (H + 2 * MARGIN))
left = (garden.width - crop_w) // 2
bg = garden.crop((left, 0, left + crop_w, garden.height)).resize((W + 2 * MARGIN, H + 2 * MARGIN), Image.LANCZOS)


def offset(t):
    """Where the camera points: tremor (a few pixels) and one slow pan."""
    tx = 2.2 * math.sin(2 * math.pi * 1.3 * t) + 1.1 * math.sin(2 * math.pi * 3.7 * t + 1.0)
    ty = 1.8 * math.sin(2 * math.pi * 1.1 * t + 0.4) + 0.9 * math.sin(2 * math.pi * 4.1 * t + 2.0)
    p = min(max((t - 2.4) / 1.0, 0.0), 1.0)
    pan = 46 * (p * p * (3 - 2 * p))
    return MARGIN + tx + pan - 23, MARGIN + ty


def beetle(d, t, ox, oy):
    x0, y0 = 120 + 70 * t, 640 - 18 * t                  # walks steadily up and to the right
    ang = math.radians(-14)
    ca, sa = math.cos(ang), math.sin(ang)
    def P(u, v):                                      # body frame (u forward) to picture
        return (x0 + u * ca - v * sa - ox + MARGIN, y0 + u * sa + v * ca - oy + MARGIN)
    phase = 2 * math.pi * 4.0 * t                     # four steps a second
    for side in (-1, 1):
        for k, u in enumerate((-9, 0, 9)):
            tri = (k + (1 if side > 0 else 0)) % 2    # two alternating sets of three legs
            swing = 7 * math.sin(phase + math.pi * tri)
            a = P(u, side * 5); b = P(u + swing, side * 17)
            d.line([a, b], fill=(20, 14, 10), width=3)
    for u, r in ((-12, 8), (1, 7), (12, 5)):
        cx, cy = P(u, 0)
        d.ellipse([cx - r, cy - r * 0.8, cx + r, cy + r * 0.8], fill=(28, 20, 14))
    return P(0, 0)


def fly(d, t, ox, oy):
    cyc = t % 1.0                                     # a burst of walking, then a stop
    hops = math.floor(t)
    step = min(cyc / 0.4, 1.0)
    x0 = 380 + 34 * (hops + step * step * (3 - 2 * step)) * math.cos(1.9)
    y0 = 400 + 34 * (hops + step * step * (3 - 2 * step)) * math.sin(1.9) * 0.6
    cx, cy = x0 - ox + MARGIN, y0 - oy + MARGIN
    if cyc > 0.4:                                     # standing: the wings buzz
        a = 0.5 + 0.5 * math.sin(2 * math.pi * 11 * t)
        for s in (-1, 1):
            wx = cx + s * (6 + 5 * a)
            d.ellipse([wx - 6, cy - 9 - 3 * a, wx + 6, cy + 1], fill=(200, 205, 215))
    else:
        jx = rng.normal(0, 0.8)
        cx += jx
    d.ellipse([cx - 6, cy - 4, cx + 6, cy + 5], fill=(18, 18, 22))
    d.ellipse([cx - 3, cy - 8, cx + 3, cy - 3], fill=(120, 20, 20))
    return cx, cy


def ball(d, t, ox, oy):
    x0, y0 = 470 - 95 * t, 820
    cx, cy = x0 - ox + MARGIN, y0 - oy + MARGIN
    d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=(240, 138, 28))
    d.ellipse([cx - 7, cy - 10, cx - 1, cy - 4], fill=(255, 210, 160))
    return cx, cy


def glints(arr, ox, oy):
    x0, y0 = int(300 - ox + MARGIN), int(560 - oy + MARGIN)
    if 0 <= x0 and x0 + 60 <= W and 0 <= y0 and y0 + 40 <= H:
        m = rng.random((40, 60)) > 0.82
        patch = arr[y0:y0 + 40, x0:x0 + 60]
        patch[m] = (250, 250, 235)
    return 300 - ox + MARGIN + 30, 560 - oy + MARGIN + 20


proc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '%dx%d' % (W, H), '-r', str(FPS), '-i', '-',
                         '-c:v', 'libvpx', '-b:v', '900k', '-crf', '12', '-auto-alt-ref', '0', '-g', '30', '-an', str(here / 'assets' / 'scene.webm')],
                        stdin=subprocess.PIPE)
where = {'beetle': [], 'fly': [], 'ball': [], 'glints': []}
for i in range(FPS * SECONDS):
    t = i / FPS
    ox, oy = offset(t)
    fr = bg.crop((round(ox), round(oy), round(ox) + W, round(oy) + H)).copy()
    d = ImageDraw.Draw(fr)
    at = {'beetle': beetle(d, t, ox, oy), 'fly': fly(d, t, ox, oy), 'ball': ball(d, t, ox, oy)}
    arr = np.asarray(fr).copy()
    at['glints'] = glints(arr, ox, oy)
    for k, (x, y) in at.items():
        where[k].append([round(x / W, 4), round(y / H, 4)])
    proc.stdin.write(arr.astype(np.uint8).tobytes())
proc.stdin.close()
proc.wait()
(here / 'assets' / 'scene.json').write_text(json.dumps({'fps': FPS, 'size': [W, H], 'living': ['beetle', 'fly'], 'where': where}, separators=(',', ':')))
print('wrote', here / 'assets' / 'scene.webm', (here / 'assets' / 'scene.webm').stat().st_size, 'bytes, and scene.json')
