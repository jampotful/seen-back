#!/usr/bin/env python3
"""Photos with nothing alive in them, made here, and their vectors from the pocket encoder (burst 12, item 2).

COCO's `none` rows are rooms and tables (furniture, electronics, kitchens, food). The odd photos that went wrong in the page before
build 9 were of another sort, a brick wall and a heap of old coins, and no host with more photos can be reached from the cloud
machines. So this script draws such subjects itself, seeded and repeatable, in eight families: coins on cloth or wood, brick walls,
stones and gravel, rust on metal, tiles, plastic toys, stains on fabric, and cracked concrete. Each picture varies in colour, scale,
count, light, blur, noise and JPEG quality. The repository's own odd test photos (test/rec/photos: wall, rings, dots, stripes, odd,
small) are added as family `repo`.

They are drawn pictures, so they say how the head treats such textures and shapes, and not how it treats a phone's photo of the
same things; docs/LOG.md says so beside the numbers.

The vectors come from models/pocket/vision.int8-per-channel.onnx through onnxruntime on the CPU, after the worker's own steps
(vendor/rec-worker.js: Pillow's bicubic to 224 on the shortest side, floor, centre crop, the manifest's mean and std).

Usage: python3 -I tools/world/nonlife_make.py OUT [--per 60]
Writes OUT/nonlife-made.f16.npy (unit vectors), OUT/nonlife-made.ids.json, OUT/manifest.csv (id, family, set) and the pictures
under OUT/photos/ (not committed). The set (tune or test) is by a hash of the id, half and half within each family.
"""
import argparse, csv, hashlib, io, json, math, os, pathlib
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = pathlib.Path(__file__).resolve().parents[2]
SEED = 20261018


def noise(rng, w, h, scale, octaves=3):
    out = np.zeros((h, w))
    amp = 1.0
    for o in range(octaves):
        s = max(2, int(scale / (2 ** o)))
        small = rng.random((max(2, h // s), max(2, w // s)))
        out += amp * np.asarray(Image.fromarray((small * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC), dtype=np.float64) / 255
        amp *= 0.5
    return (out - out.min()) / (np.ptp(out) or 1)


def tint(gray, c0, c1):
    g = gray[..., None]
    return (np.array(c0) * (1 - g) + np.array(c1) * g).clip(0, 255).astype(np.uint8)


def jitter(rng, c, d=25):
    """A shared change of brightness of up to d, and up to a third of that in each channel, so that a colour keeps its hue."""
    shift = int(rng.integers(-d, d + 1))
    return tuple(int(np.clip(v + shift + rng.integers(-(d // 3), d // 3 + 1), 0, 255)) for v in c)


def background(rng, w, h):
    kind = rng.integers(0, 3)
    if kind == 0:   # cloth
        base = jitter(rng, [(40, 60, 120), (120, 30, 40), (60, 60, 60), (30, 90, 60), (180, 170, 150)][rng.integers(0, 5)], 30)
        n = noise(rng, w, h, 6, 2)
        return tint(n, tuple(v * 0.7 for v in base), base)
    if kind == 1:   # wood table
        y = np.linspace(0, 1, h)[:, None] * np.ones((1, w))
        n = noise(rng, w, h, 40, 3)
        g = (np.sin((y * rng.uniform(20, 60) + n * 6) * math.pi) + 1) / 2
        return tint(g, jitter(rng, (90, 55, 30)), jitter(rng, (170, 120, 70)))
    n = noise(rng, w, h, 30, 3)  # plain counter
    c = jitter(rng, (200, 200, 195), 40)
    return tint(n, tuple(v * 0.85 for v in c), c)


def coins(rng, w, h):
    im = Image.fromarray(background(rng, w, h))
    d = ImageDraw.Draw(im)
    metals = [((150, 80, 40), (220, 140, 90)), ((140, 140, 145), (230, 230, 235)), ((150, 120, 40), (240, 210, 110)), ((70, 60, 50), (130, 110, 80))]
    for _ in range(int(rng.integers(1, 30))):
        r = int(rng.uniform(0.04, 0.2) * min(w, h)); x = int(rng.integers(0, w)); y = int(rng.integers(0, h))
        dark, light = metals[rng.integers(0, len(metals))]
        d.ellipse([x - r + r // 6, y - r + r // 6, x + r + r // 6, y + r + r // 6], fill=(30, 25, 20))       # shadow
        for k in range(r, 0, -1):
            t = k / r
            c = tuple(int(dark[j] * t + light[j] * (1 - t) * 0.9 + 10 * rng.random()) for j in range(3))
            d.ellipse([x - k, y - k, x + k, y + k], fill=c)
        d.ellipse([x - r, y - r, x + r, y + r], outline=dark, width=max(1, r // 10))
        d.ellipse([x - int(r * 0.75), y - int(r * 0.75), x + int(r * 0.75), y + int(r * 0.75)], outline=dark, width=max(1, r // 25))
        for _ in range(int(rng.integers(3, 12))):                                                                 # worn relief
            a = rng.uniform(0, 2 * math.pi); q = rng.uniform(0, 0.6) * r
            d.line([x + q * math.cos(a), y + q * math.sin(a), x + q * math.cos(a) + rng.uniform(-r, r) * 0.3, y + q * math.sin(a) + rng.uniform(-r, r) * 0.3], fill=dark, width=max(1, r // 20))
    return im


def bricks(rng, w, h):
    mortar = jitter(rng, (170, 165, 155), 30)
    im = Image.new("RGB", (w, h), mortar); d = ImageDraw.Draw(im)
    bh = int(rng.uniform(0.04, 0.12) * h); bw = int(bh * rng.uniform(2.0, 3.2)); gap = max(2, bh // 7)
    base = jitter(rng, [(150, 60, 40), (120, 50, 35), (170, 110, 80), (110, 100, 95)][rng.integers(0, 4)], 20)
    for row, y in enumerate(range(-bh, h + bh, bh + gap)):
        off = (row % 2) * (bw // 2)
        for x in range(-bw - off, w + bw, bw + gap):
            d.rectangle([x, y, x + bw, y + bh], fill=jitter(rng, base, 25))
    arr = np.asarray(im, dtype=np.float64) * (0.8 + 0.4 * noise(rng, w, h, 8, 3)[..., None])
    return Image.fromarray(arr.clip(0, 255).astype(np.uint8))


def stones(rng, w, h):
    im = Image.fromarray(tint(noise(rng, w, h, 10, 2), (60, 55, 50), (110, 100, 90))); d = ImageDraw.Draw(im)
    big = rng.random() < 0.5
    for _ in range(int(rng.integers(20, 60) if big else rng.integers(150, 500))):
        r = int((rng.uniform(0.04, 0.14) if big else rng.uniform(0.01, 0.04)) * min(w, h)); x = int(rng.integers(0, w)); y = int(rng.integers(0, h))
        c = jitter(rng, [(130, 125, 120), (160, 140, 110), (90, 90, 95), (200, 195, 185)][rng.integers(0, 4)], 30)
        e = rng.uniform(0.6, 1.0)
        d.ellipse([x - r, y - int(r * e), x + r, y + int(r * e)], fill=c, outline=tuple(int(v * 0.6) for v in c))
    arr = np.asarray(im, dtype=np.float64) * (0.85 + 0.3 * noise(rng, w, h, 4, 2)[..., None])
    return Image.fromarray(arr.clip(0, 255).astype(np.uint8))


def rust(rng, w, h):
    metal = tint(noise(rng, w, h, 50, 2), (90, 95, 100), (160, 165, 170))
    r = noise(rng, w, h, rng.uniform(20, 80), 4)
    m = (r > rng.uniform(0.3, 0.6)).astype(np.float64)[..., None]
    rr = tint(noise(rng, w, h, 5, 3), (90, 40, 15), (190, 100, 40))
    return Image.fromarray((metal * (1 - m) + rr * m).astype(np.uint8))


def tiles(rng, w, h):
    grout = jitter(rng, (200, 200, 195), 30)
    im = Image.new("RGB", (w, h), grout); d = ImageDraw.Draw(im)
    s = int(rng.uniform(0.06, 0.25) * min(w, h)); g = max(2, s // 15)
    glaze = jitter(rng, [(240, 240, 235), (60, 110, 160), (180, 60, 50), (40, 40, 40), (90, 150, 110)][rng.integers(0, 5)], 20)
    for y in range(0, h, s + g):
        for x in range(0, w, s + g):
            d.rectangle([x, y, x + s, y + s], fill=jitter(rng, glaze, 8))
    arr = np.asarray(im, dtype=np.float64) * (0.9 + 0.2 * noise(rng, w, h, 60, 2)[..., None])
    return Image.fromarray(arr.clip(0, 255).astype(np.uint8))


def toys(rng, w, h):
    im = Image.fromarray(background(rng, w, h)); d = ImageDraw.Draw(im)
    for _ in range(int(rng.integers(1, 8))):
        c = [(220, 30, 30), (30, 80, 220), (250, 200, 20), (30, 170, 60), (240, 120, 20), (250, 250, 250)][rng.integers(0, 6)]
        x = int(rng.integers(0, w)); y = int(rng.integers(0, h)); s = int(rng.uniform(0.08, 0.3) * min(w, h)); t = rng.integers(0, 3)
        if t == 0:
            for k in range(s, 0, -2):
                f = k / s; d.ellipse([x - k, y - k, x + k, y + k], fill=tuple(int(v * (0.55 + 0.45 * (1 - f))) for v in c))
        elif t == 1:
            d.polygon([(x, y), (x + s, y), (x + s, y + s), (x, y + s)], fill=c)
            d.polygon([(x, y), (x + s // 3, y - s // 3), (x + s + s // 3, y - s // 3), (x + s, y)], fill=tuple(min(255, int(v * 1.2) + 20) for v in c))
            d.polygon([(x + s, y), (x + s + s // 3, y - s // 3), (x + s + s // 3, y + s - s // 3), (x + s, y + s)], fill=tuple(int(v * 0.6) for v in c))
        else:
            for k in range(0, s, max(1, s // 6)):
                d.rectangle([x + k, y, x + k + s // 8, y + s // 2], fill=c)
                d.ellipse([x + k, y - s // 16, x + k + s // 8, y + s // 16], fill=tuple(int(v * 0.8) for v in c))
    return im


def stains(rng, w, h):
    base = jitter(rng, [(235, 230, 220), (200, 210, 230), (230, 200, 200), (120, 120, 125)][rng.integers(0, 4)], 15)
    cloth = tint(noise(rng, w, h, 3, 2), tuple(v * 0.9 for v in base), base).astype(np.float64)
    st = noise(rng, w, h, rng.uniform(30, 90), 4)
    m = np.clip((st - rng.uniform(0.45, 0.7)) * 6, 0, 1)[..., None]
    col = np.array(jitter(rng, [(120, 70, 40), (90, 30, 50), (60, 60, 40), (150, 120, 60)][rng.integers(0, 4)], 20), dtype=np.float64)
    return Image.fromarray((cloth * (1 - 0.7 * m) + col * 0.7 * m).clip(0, 255).astype(np.uint8))


def concrete(rng, w, h):
    im = Image.fromarray(tint(noise(rng, w, h, rng.uniform(3, 20), 4), jitter(rng, (95, 95, 95)), jitter(rng, (175, 172, 168)))); d = ImageDraw.Draw(im)
    for _ in range(int(rng.integers(1, 6))):
        x, y = rng.uniform(0, w), rng.uniform(0, h); a = rng.uniform(0, 2 * math.pi)
        for _ in range(int(rng.integers(10, 40))):
            a += rng.uniform(-0.6, 0.6); nx, ny = x + 12 * math.cos(a), y + 12 * math.sin(a)
            d.line([x, y, nx, ny], fill=(40, 40, 40), width=int(rng.integers(1, 4))); x, y = nx, ny
    return im


FAMILIES = {"coins": coins, "bricks": bricks, "stones": stones, "rust": rust, "tiles": tiles, "toys": toys, "stains": stains, "concrete": concrete}


def finish(rng, im):
    if rng.random() < 0.5:
        im = im.filter(ImageFilter.GaussianBlur(rng.uniform(0.3, 1.8)))
    arr = np.asarray(im, dtype=np.float64)
    arr = arr * rng.uniform(0.7, 1.2) + rng.normal(0, rng.uniform(1, 8), arr.shape)        # light and sensor noise
    im = Image.fromarray(arr.clip(0, 255).astype(np.uint8))
    b = io.BytesIO(); im.save(b, "JPEG", quality=int(rng.integers(55, 92))); b.seek(0)
    return Image.open(b).convert("RGB")


def prepare(im, man):
    v = man["vision"]; S = v["size"]; w, h = im.size
    ow, oh = (S, math.floor(S * h / w)) if w <= h else (math.floor(S * w / h), S)
    if (ow, oh) != (w, h):
        im = im.resize((ow, oh), Image.BICUBIC)
    left, top = (ow - S) // 2, (oh - S) // 2
    a = np.asarray(im.crop((left, top, left + S, top + S)), dtype=np.float32) / 255
    a = (a - np.array(v["mean"], np.float32)) / np.array(v["std"], np.float32)
    return a.transpose(2, 0, 1)[None]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("out"); ap.add_argument("--per", type=int, default=60)
    a = ap.parse_args()
    out = pathlib.Path(a.out); (out / "photos").mkdir(parents=True, exist_ok=True)
    import onnxruntime as ort
    man = json.load(open(ROOT / "models" / "pocket" / "manifest.json"))
    sess = ort.InferenceSession(str(ROOT / "models" / "pocket" / man["vision"]["url"]), providers=["CPUExecutionProvider"])
    rows, vecs = [], []

    def add(pid, fam, im):
        e = sess.run([man["vision"]["output"]], {man["vision"]["input"]: prepare(im, man)})[0][0].astype(np.float64)
        vecs.append(e / (np.linalg.norm(e) or 1))
        st = "tune" if int(hashlib.sha256(("nonlife|" + pid).encode()).hexdigest()[:8], 16) % 2 == 0 else "test"
        rows.append({"id": pid, "family": fam, "set": st})

    for fam, fn in FAMILIES.items():
        for i in range(a.per):
            rng = np.random.default_rng([SEED, list(FAMILIES).index(fam), i])
            w, h = [(640, 480), (480, 640), (800, 600), (600, 800), (640, 640)][rng.integers(0, 5)]
            im = finish(rng, fn(rng, w, h))
            pid = "%s-%03d" % (fam, i)
            im.save(out / "photos" / (pid + ".jpg"), quality=90)
            add(pid, fam, im)
    for name in ("wall.png", "rings.png", "dots.png", "stripes.png", "odd.png", "small.png"):
        p = ROOT / "test" / "rec" / "photos" / name
        if p.exists():
            add("repo-" + name.split(".")[0], "repo", Image.open(p).convert("RGB"))
    np.save(out / "nonlife-made.f16.npy", np.array(vecs, dtype=np.float16))
    json.dump([r["id"] for r in rows], open(out / "nonlife-made.ids.json", "w"))
    with open(out / "manifest.csv", "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=["id", "family", "set"]); wr.writeheader(); wr.writerows(rows)
    print(len(rows), "photos;", {s: sum(r["set"] == s for r in rows) for s in ("tune", "test")})


if __name__ == "__main__":
    main()
