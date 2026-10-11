#!/usr/bin/env python3
"""Gather the photos the recognizer is tried on into one directory. Usage: python3 -I ci/engines/make_photos.py <out dir>

The recognizer checks' photos (test/rec/photos), the app's test photos (test/assets/*.jpg, renamed asset-*), and three made here:
  big12mp.jpg      4000 x 3000, a phone camera's full size, to see what the page does with 12 million pixels
  wide.png         1600 x 400, a long thin picture
  info-exif6.jpg   a JPEG whose EXIF says "turn 90 degrees": browsers turn it, Pillow (and so expect.json) does not,
                   so its answer is recorded but not judged
"""
import pathlib, shutil, sys
from PIL import Image

root = pathlib.Path(__file__).resolve().parents[2]
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
for f in sorted((root / "test" / "rec" / "photos").iterdir()):
    if f.suffix.lower() in (".png", ".jpg", ".jpeg"):
        shutil.copyfile(f, out / f.name)
for f in sorted((root / "test" / "assets").glob("*.jpg")):
    shutil.copyfile(f, out / ("asset-" + f.name))
g = Image.open(root / "test" / "assets" / "garden.jpg").convert("RGB")
g.resize((4000, 3000), Image.BICUBIC).save(out / "big12mp.jpg", quality=85)
w = g.resize((1600, int(1600 * g.height / g.width)), Image.BICUBIC)
w.crop((0, (w.height - 400) // 2, 1600, (w.height - 400) // 2 + 400)).save(out / "wide.png")
p = Image.open(root / "test" / "assets" / "portrait.jpg").convert("RGB")
ex = Image.Exif(); ex[0x0112] = 6
p.save(out / "info-exif6.jpg", quality=90, exif=ex.tobytes())
for f in sorted(out.iterdir()):
    print(f.name, f.stat().st_size)
