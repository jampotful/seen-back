#!/usr/bin/env python3
"""Draw two synthetic test photos: a garden scene and a stand-in portrait. Run with python3 -I."""
import math, pathlib, random
from PIL import Image, ImageDraw, ImageFilter

out = pathlib.Path(__file__).resolve().parent
random.seed(7)

# garden, landscape 1600 x 1200
W, H = 1600, 1200
im = Image.new("RGB", (W, H))
px = im.load()
for y in range(H):
    t = y / H
    for x in range(W):
        if t < 0.42:  # sky
            px[x, y] = (int(110 + 60 * t), int(160 + 60 * t), int(235 - 20 * t))
        else:  # foliage
            n = random.random()
            px[x, y] = (int(30 + 40 * n), int(90 + 80 * n), int(30 + 30 * n))
im = im.filter(ImageFilter.GaussianBlur(1.2))
d = ImageDraw.Draw(im)
for i in range(46):
    cx, cy = random.randint(60, W - 60), random.randint(int(H * 0.46), H - 60)
    r = random.randint(18, 54)
    col = random.choice([(214, 43, 31), (242, 210, 27), (250, 250, 246), (122, 63, 196), (240, 138, 28)])
    for k in range(6):
        a = k * math.pi / 3
        d.ellipse([cx + math.cos(a) * r - r * 0.6, cy + math.sin(a) * r - r * 0.6,
                   cx + math.cos(a) * r + r * 0.6, cy + math.sin(a) * r + r * 0.6], fill=col)
    d.ellipse([cx - r * 0.4, cy - r * 0.4, cx + r * 0.4, cy + r * 0.4], fill=(60, 40, 20))
for i in range(0, W, 3):  # a fine fence, to show sharpness loss
    if (i // 3) % 2 == 0:
        d.line([i, int(H * 0.40), i, int(H * 0.47)], fill=(245, 245, 240), width=2)
im.save(out / "garden.jpg", quality=90)

# portrait, 1200 x 1600
W, H = 1200, 1600
im = Image.new("RGB", (W, H), (150, 170, 150))
d = ImageDraw.Draw(im)
d.rectangle([0, 0, W, H * 0.35], fill=(120, 165, 225))
d.ellipse([W * 0.2, H * 0.72, W * 0.8, H * 1.3], fill=(200, 40, 35))      # red shirt
d.ellipse([W * 0.33, H * 0.22, W * 0.67, H * 0.66], fill=(196, 150, 120))  # head
d.ellipse([W * 0.41, H * 0.38, W * 0.46, H * 0.41], fill=(30, 25, 20))
d.ellipse([W * 0.54, H * 0.38, W * 0.59, H * 0.41], fill=(30, 25, 20))
d.arc([W * 0.43, H * 0.48, W * 0.57, H * 0.57], 20, 160, fill=(120, 50, 50), width=8)
d.pieslice([W * 0.31, H * 0.17, W * 0.69, H * 0.5], 180, 360, fill=(40, 30, 25))  # hair
im = im.filter(ImageFilter.GaussianBlur(0.8))
im.save(out / "portrait.jpg", quality=90)
print("wrote", out / "garden.jpg", out / "portrait.jpg")
