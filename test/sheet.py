import sys, pathlib
from PIL import Image, ImageDraw
out, w, names = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
ims = []
for n in names:
    p = pathlib.Path(__import__('os').environ.get('SHOTS','shots3')) / (n + '.png')
    if not p.exists(): p = pathlib.Path(__import__('os').environ.get('SHOTS','shots3')) / n
    im = Image.open(p).convert('RGB'); h = round(im.height * w / im.width); ims.append((n, im.resize((w, h), Image.LANCZOS)))
H = max(i.height for _, i in ims) + 18
sheet = Image.new('RGB', (w * len(ims) + 6 * (len(ims) - 1), H), (60, 60, 60))
d = ImageDraw.Draw(sheet)
for k, (n, im) in enumerate(ims):
    x = k * (w + 6); sheet.paste(im, (x, 18)); d.text((x + 3, 3), n[:40], fill=(255, 255, 255))
sheet.save(out, quality=88)
print(out, sheet.size)
