#!/usr/bin/env python3
"""Build the stand-in recognizer the browser checks run against. Usage: python3 -I test/rec/make_standin.py

It is NOT a recognizer: a few convolutions with fixed random weights, quantized to int8 the way a real
encoder for the page is, so that the same operators run in the browser. Its label vectors are made from its
own embeddings of the test photos, so "this photo gives that label" is a real assertion in the browser.

Writes test/rec/models/standin/ (the slot: manifest.json, vision.int8.onnx, kinds.f16.bin, species.f16.bin, species.json),
test/rec/photos/ (the test photos) and test/rec/models/standin/expect.json (what Python got: the preprocessed pixels'
checksum, the embedding and the labels expected for each photo). Needs numpy, pillow, onnx, onnxruntime.
"""
import hashlib, json, math, pathlib, random
import numpy as np
import onnx
from onnx import TensorProto, helper, numpy_helper
import onnxruntime as ort
from onnxruntime.quantization import QuantType, quantize_dynamic
from PIL import Image, ImageDraw, ImageFilter

here = pathlib.Path(__file__).resolve().parent
slot = here / "models" / "standin"   # under a models/ directory, so the service worker treats it as it will treat models/pocket/
photos = here / "photos"
slot.mkdir(parents=True, exist_ok=True)
photos.mkdir(exist_ok=True)
(slot / "pre").mkdir(exist_ok=True)

SIZE, WIDTH = 224, 512
MEAN = [0.48145466, 0.4578275, 0.40821073]
STD = [0.26862954, 0.26130258, 0.27577711]
KINDS = ["cat", "dog", "squirrel", "deer", "rabbit", "hawk", "wader", "bird", "alligator", "reptile", "frog", "bee", "insect", "plant", "other", "person", "none"]
FUSION = {"t_kind": 100, "t_species": 100, "alpha_prior": 0.5, "w_kind": 0.5, "name_at": 0.6, "offer_at": 0.3}


# ---------- the photos (drawn, so nothing here belongs to anyone)
def draw_heron(w, h, seed):
    rnd = random.Random(seed)
    im = Image.new("RGB", (w, h), (168, 196, 214))
    d = ImageDraw.Draw(im)
    d.rectangle([0, h * 0.62, w, h], fill=(72, 104, 96))
    for i in range(60):
        x = rnd.randint(0, w); y = rnd.randint(int(h * 0.55), h)
        d.line([x, y, x + rnd.randint(-12, 12), y - rnd.randint(40, 160)], fill=(60 + rnd.randint(0, 50), 110 + rnd.randint(0, 60), 50), width=3)
    d.ellipse([w * 0.34, h * 0.36, w * 0.66, h * 0.60], fill=(124, 138, 156))
    d.line([w * 0.60, h * 0.42, w * 0.66, h * 0.20], fill=(150, 160, 174), width=int(w * 0.035))
    d.ellipse([w * 0.62, h * 0.14, w * 0.72, h * 0.22], fill=(236, 236, 232))
    d.polygon([(w * 0.71, h * 0.17), (w * 0.88, h * 0.185), (w * 0.71, h * 0.20)], fill=(226, 168, 44))
    d.line([w * 0.46, h * 0.58, w * 0.44, h * 0.86], fill=(96, 92, 70), width=int(w * 0.012))
    d.line([w * 0.54, h * 0.58, w * 0.56, h * 0.86], fill=(96, 92, 70), width=int(w * 0.012))
    return im.filter(ImageFilter.GaussianBlur(0.7))


def draw_stripes(w, h, seed):
    rnd = random.Random(seed)
    im = Image.new("RGB", (w, h), (30, 30, 34))
    d = ImageDraw.Draw(im)
    for i in range(0, w + h, 46):
        d.line([i, 0, i - h, h], fill=(rnd.randint(150, 255), rnd.randint(90, 220), rnd.randint(20, 90)), width=17)
    for i in range(26):
        x, y, r = rnd.randint(0, w), rnd.randint(0, h), rnd.randint(8, 30)
        d.ellipse([x - r, y - r, x + r, y + r], fill=(20, 20, 20))
    return im


def draw_dots(w, h, seed):
    rnd = random.Random(seed)
    im = Image.new("RGB", (w, h), (226, 222, 210))
    d = ImageDraw.Draw(im)
    for i in range(900):
        x, y, r = rnd.randint(0, w), rnd.randint(0, h), rnd.randint(2, 9)
        d.ellipse([x - r, y - r, x + r, y + r], fill=(rnd.randint(0, 120), rnd.randint(0, 90), rnd.randint(60, 200)))
    return im


def draw_wall(w, h, seed):
    rnd = random.Random(seed)
    im = Image.new("RGB", (w, h), (186, 180, 170))
    d = ImageDraw.Draw(im)
    for y in range(0, h, 64):
        for x in range(-64 if (y // 64) % 2 else 0, w, 128):
            d.rectangle([x + 2, y + 2, x + 124, y + 60], fill=(150 + rnd.randint(0, 40), 86 + rnd.randint(0, 30), 70 + rnd.randint(0, 24)))
    return im


def draw_rings(w, h, seed):
    im = Image.new("RGB", (w, h), (18, 60, 44))
    d = ImageDraw.Draw(im)
    for i, r in enumerate(range(int(min(w, h) * 0.48), 10, -22)):
        d.ellipse([w / 2 - r, h / 2 - r * 0.8, w / 2 + r, h / 2 + r * 0.8], outline=(240, 230 - 9 * i, 40 + 12 * i), width=7)
    return im


garden = Image.open(here.parent / "assets" / "garden.jpg").convert("RGB")
portrait = Image.open(here.parent / "assets" / "portrait.jpg").convert("RGB")
MADE = {
    # name: (image, format). PNG photos no larger than 1280 on a side reach the page's own resize untouched, so they can be compared exactly.
    "heron.png": draw_heron(900, 1200, 3),
    "stripes.png": draw_stripes(1280, 853, 5),
    "dots.png": draw_dots(640, 640, 11),
    "wall.png": draw_wall(1024, 768, 13),
    "rings.png": draw_rings(480, 300, 17),
    "odd.png": draw_stripes(1279, 719, 23).transpose(Image.FLIP_LEFT_RIGHT),
    "small.png": draw_heron(150, 200, 29),          # smaller than the model's input: it is enlarged
    "garden.jpg": garden,                              # 1600 x 1200: the page first brings it to 1280 with the browser's own scaling
    "portrait.jpg": portrait,
}
for name, im in MADE.items():
    if name.endswith(".png"):
        im.save(photos / name, optimize=True)
    else:
        im.save(photos / name, quality=90)


# ---------- the model: fixed random weights, then int8 as onnxruntime's dynamic quantization does it
def build_model(path):
    rs = np.random.RandomState(7)

    def conv_w(o, i, k):
        w = rs.randn(o, i, k, k).astype(np.float32)
        w -= w.mean(axis=(1, 2, 3), keepdims=True)           # each filter sums to nothing, so flat colour says little and edges say much
        return (w / np.sqrt(i * k * k)).astype(np.float32)

    init = [
        numpy_helper.from_array(conv_w(24, 3, 7), "w1"), numpy_helper.from_array((rs.randn(24) * 0.05).astype(np.float32), "b1"),
        numpy_helper.from_array(conv_w(48, 24, 3), "w2"), numpy_helper.from_array((rs.randn(48) * 0.05).astype(np.float32), "b2"),
        numpy_helper.from_array(conv_w(96, 48, 3), "w3"), numpy_helper.from_array((rs.randn(96) * 0.05).astype(np.float32), "b3"),
        numpy_helper.from_array((rs.randn(96 * 16, WIDTH) / np.sqrt(96 * 16)).astype(np.float32), "wp"),
        numpy_helper.from_array((rs.randn(WIDTH) * 0.01).astype(np.float32), "bp"),
        numpy_helper.from_array(np.array([0, 96 * 16], dtype=np.int64), "shape"),
    ]
    nodes = [
        helper.make_node("Conv", ["pixel_values", "w1", "b1"], ["c1"], kernel_shape=[7, 7], strides=[4, 4], pads=[3, 3, 3, 3]),
        helper.make_node("Relu", ["c1"], ["r1"]),
        helper.make_node("Conv", ["r1", "w2", "b2"], ["c2"], kernel_shape=[3, 3], strides=[2, 2], pads=[1, 1, 1, 1]),
        helper.make_node("Relu", ["c2"], ["r2"]),
        helper.make_node("Conv", ["r2", "w3", "b3"], ["c3"], kernel_shape=[3, 3], strides=[2, 2], pads=[1, 1, 1, 1]),
        helper.make_node("Relu", ["c3"], ["r3"]),
        helper.make_node("AveragePool", ["r3"], ["p"], kernel_shape=[4, 4], strides=[4, 4], pads=[1, 1, 1, 1]),   # 14 x 14 -> 4 x 4, so where things are still counts
        helper.make_node("Reshape", ["p", "shape"], ["f"]),
        helper.make_node("MatMul", ["f", "wp"], ["m"]),
        helper.make_node("Add", ["m", "bp"], ["image_embeds"]),
    ]
    graph = helper.make_graph(nodes, "standin", [helper.make_tensor_value_info("pixel_values", TensorProto.FLOAT, ["N", 3, SIZE, SIZE])],
                              [helper.make_tensor_value_info("image_embeds", TensorProto.FLOAT, ["N", WIDTH])], init)
    model = helper.make_model(graph, opset_imports=[helper.make_opsetid("", 17)], producer_name="seen-back-standin")
    model.ir_version = 9
    onnx.checker.check_model(model)
    onnx.save(model, path)


fp32 = slot / "vision.fp32.onnx"
int8 = slot / "vision.int8.onnx"
build_model(fp32)
quantize_dynamic(str(fp32), str(int8), weight_type=QuantType.QUInt8)
ops = sorted({n.op_type for n in onnx.load(int8).graph.node})
fp32.unlink()


# ---------- preprocessing as the laboratory does it: Pillow's bicubic to the short side, centre crop, 0..1, mean and std
def pre_u8(im):
    w, h = im.size
    if w <= h:
        nw, nh = SIZE, int(SIZE * h / w)
    else:
        nw, nh = int(SIZE * w / h), SIZE
    r = im.resize((nw, nh), Image.BICUBIC)
    left, top = (nw - SIZE) // 2, (nh - SIZE) // 2
    return np.asarray(r.crop((left, top, left + SIZE, top + SIZE)), dtype=np.uint8)


def tensor(u8):
    x = (u8.astype(np.float32) / 255.0 - np.array(MEAN, dtype=np.float32)) / np.array(STD, dtype=np.float32)
    return x.transpose(2, 0, 1)[None].astype(np.float32)


sess = ort.InferenceSession(str(int8), providers=["CPUExecutionProvider"])


def embed(im):
    u8 = pre_u8(im)
    e = sess.run(["image_embeds"], {"pixel_values": tensor(u8)})[0][0].astype(np.float64)
    return u8, e / np.linalg.norm(e)


E, expect = {}, {"photos": {}, "ops": ops, "onnxruntime": ort.__version__, "pillow": Image.__version__}
for name in MADE:
    im = Image.open(photos / name).convert("RGB")
    u8, e = embed(im)
    E[name] = e
    (slot / "pre" / (name + ".u8")).write_bytes(u8.tobytes())
    expect["photos"][name] = {"w": im.size[0], "h": im.size[1], "pre_sha256": hashlib.sha256(u8.tobytes()).hexdigest(), "embedding": [round(float(v), 6) for v in e]}

names = list(MADE)
cos = np.array([[float(E[a] @ E[b]) for b in names] for a in names])
expect["cosine_between_photos"] = {"names": names, "max_off_diagonal": float(np.max(cos - np.eye(len(names))))}


# ---------- label vectors
rs = np.random.RandomState(11)
basis = np.stack([E[n] for n in names])


def away(v):
    """A unit vector at right angles to every test photo, so that it scores the same (zero) for all of them."""
    q, _ = np.linalg.qr(basis.T)
    v = v - q @ (q.T @ v)
    return v / np.linalg.norm(v)


def near(e, c):
    """A unit vector whose cosine with e is exactly c."""
    r = rs.randn(WIDTH); r -= (r @ e) * e
    q, _ = np.linalg.qr(basis.T); r = r - q @ (q.T @ r); r /= np.linalg.norm(r)
    return c * e + math.sqrt(1 - c * c) * r


# which photo stands for which kind
KIND_OF = {"heron.png": "wader", "garden.jpg": "plant", "portrait.jpg": "person", "wall.png": "none", "stripes.png": "insect", "dots.png": "frog", "rings.png": "reptile",
           "odd.png": "bee", "small.png": "bird"}
kind_vec = {k: away(rs.randn(WIDTH)) for k in KINDS}
for photo, kind in KIND_OF.items():
    kind_vec[kind] = E[photo]
K = np.stack([kind_vec[k] for k in KINDS])

# species: [scientific, English, kind, twelve monthly weights]
month_flat = [10] * 12
rows, vecs = [], []


def add(sci, en, kind, m, v):
    rows.append([sci, en, kind, m]); vecs.append(v / np.linalg.norm(v))


add("Ardea herodias", "Great Blue Heron", "wader", month_flat, E["heron.png"])                    # heron.png: named outright
add("Bidens alba", "Beggarticks", "plant", month_flat, E["garden.jpg"])                            # garden.jpg: named outright
# stripes.png: three close candidates, none of them sure -> the kind alone, and three offers
add("Dione vanillae", "Gulf Fritillary", "insect", month_flat, near(E["stripes.png"], 0.990))
add("Danaus plexippus", "Monarch", "insect", month_flat, near(E["stripes.png"], 0.986))
add("Danaus gilippus", "Queen", "insect", month_flat, near(E["stripes.png"], 0.982))
# rings.png: two candidates exactly as alike; only the month tells them apart (the first is recorded in every month but one, the second in that one only)
add("Anolis sagrei", "Brown Anole", "reptile", [0] + [40] * 11, near(E["rings.png"], 0.99))
add("Anolis carolinensis", "Green Anole", "reptile", [40] + [0] * 11, near(E["rings.png"], 0.99))
add("Apis mellifera", "Western Honey Bee", "bee", month_flat, near(E["odd.png"], 0.995))             # odd.png: named outright, though it looks much like stripes.png
# dots.png: twelve candidates exactly as alike, so the best three together stay under the offering mark -> the kind alone, no offers
for i in range(12):
    add("Anura sp. %02d" % (i + 1), "Stand-in frog %02d" % (i + 1), "frog", month_flat, near(E["dots.png"], 0.9))
# the rest score the same (zero) for every test photo
filler = [("Sciurus carolinensis", "Eastern Gray Squirrel", "squirrel"), ("Odocoileus virginianus", "White-tailed Deer", "deer"), ("Buteo lineatus", "Red-shouldered Hawk", "hawk"),
          ("Cardinalis cardinalis", "Northern Cardinal", "bird"), ("Alligator mississippiensis", "American Alligator", "alligator"), ("Dryophytes cinereus", "Green Treefrog", "frog"),
          ("Bombus impatiens", "Common Eastern Bumble Bee", "bee"), ("Sylvilagus floridanus", "Eastern Cottontail", "rabbit"), ("Lynx rufus", "Bobcat", "cat"), ("Urocyon cinereoargenteus", "Gray Fox", "dog"),
          ("Trichonephila clavipes", "Golden Silk Spider", "other"), ("Quercus virginiana", "Southern Live Oak", "plant"), ("Sabal palmetto", "Cabbage Palmetto", "plant"),
          ("Eudocimus albus", "White Ibis", "wader"), ("Anhinga anhinga", "Anhinga", "bird"), ("Coragyps atratus", "Black Vulture", "bird"), ("Pantherophis alleghaniensis", "", "reptile")]
for i in range(2):
    for sci, en, kind in filler:
        add(sci if i == 0 else sci + " " + "var" + str(i), en, kind, [rs.randint(1, 60) for _ in range(12)], away(rs.randn(WIDTH)))
Sm = np.stack(vecs)

K.astype("<f2").tofile(slot / "kinds.f16.bin")
Sm.astype("<f2").tofile(slot / "species.f16.bin")
(slot / "species.json").write_text(json.dumps({"columns": ["sci", "en", "kind", "m"], "species": rows}, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
manifest = {
    "id": "standin-random-conv", "licence": "none: random weights made by test/rec/make_standin.py", "source": "test/rec/make_standin.py",
    "vision": {"url": "vision.int8.onnx", "bytes": int8.stat().st_size, "sha256": hashlib.sha256(int8.read_bytes()).hexdigest(), "input": "pixel_values", "output": "image_embeds",
               "size": SIZE, "mean": MEAN, "std": STD, "resize": "shortest-bicubic-antialias", "crop": "center"},
    "width": WIDTH,
    "kinds": {"url": "kinds.f16.bin", "labels": KINDS},
    "species": {"url": "species.f16.bin", "table": "species.json", "count": len(rows)},
    "fusion": FUSION,
}
(slot / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n", encoding="utf-8")
# the same slot with no species, to check that the kinds alone decide there
m2 = dict(manifest); m2.pop("species"); m2["id"] = "standin-kinds-only"
(slot / "manifest.kinds-only.json").write_text(json.dumps(m2, indent=1) + "\n", encoding="utf-8")

expect["kind_of"] = KIND_OF
expect["named"] = {"heron.png": "Great Blue Heron", "garden.jpg": "Beggarticks", "odd.png": "Western Honey Bee"}
expect["offers"] = {"stripes.png": ["Gulf Fritillary", "Monarch", "Queen"]}
(slot / "expect.json").write_text(json.dumps(expect, separators=(",", ":")) + "\n", encoding="utf-8")
print("operators in the int8 stand-in:", ops)
print("model bytes:", int8.stat().st_size, "| kinds", K.shape, "| species", Sm.shape)
print("largest cosine between two different photos: %.4f" % expect["cosine_between_photos"]["max_off_diagonal"])
