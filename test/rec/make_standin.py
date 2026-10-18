#!/usr/bin/env python3
"""Build the stand-in recognizer the browser checks run against. Usage: python3 -I test/rec/make_standin.py

It is NOT a recognizer: a few convolutions with fixed random weights, quantized to int8 the way a real
encoder for the page is, so that the same operators run in the browser. Its label vectors are made from its
own embeddings of the test photos, so "this photo gives that label" is a real assertion in the browser.

Writes test/rec/models/standin/ (the slot: manifest.json, vision.int8.onnx, kinds.f16.bin, species.f16.bin, species.json),
test/rec/photos/ (the test photos) and test/rec/models/standin/expect.json (what Python got: the preprocessed pixels'
checksum, the embedding and the labels expected for each photo). Needs numpy, pillow, onnx, onnxruntime.
Also test/rec/models/standin-ext (the larger stand-in in its second form); with --ext, only that.
"""
import hashlib, json, math, pathlib, random, sys
import numpy as np
import onnx
from onnx import TensorProto, helper, numpy_helper
import onnxruntime as ort
from onnxruntime.quantization import QuantType, quantize_dynamic
from PIL import Image, ImageDraw, ImageFilter

here = pathlib.Path(__file__).resolve().parent
EXT_PORT = 8807                                        # where test/rec/check_ext.js serves the external form's parts from (a second origin)


def make_ext():
    """test/rec/models/standin-ext: the larger stand-in's encoder in the form the larger model may also come in (docs/CONTRACTS.md):
    a small graph, and its weights as an external data file cut into three parts, with standin-big's species rows. Made from
    standin-big's parts, so that it can be made by itself: python3 -I test/rec/make_standin.py --ext"""
    import tempfile
    big, ext = here / "models" / "standin-big", here / "models" / "standin-ext"
    ext.mkdir(parents=True, exist_ok=True)
    mb = json.loads((big / "manifest.json").read_text(encoding="utf-8"))
    whole = b"".join((big / ("vision.int8.onnx.part%02d" % i)).read_bytes() for i in range(len(mb["vision"]["parts"])))
    assert hashlib.sha256(whole).hexdigest() == mb["vision"]["sha256"], "standin-big's parts are not its whole"
    with tempfile.TemporaryDirectory() as tmp:          # every tensor of 1 kB or more moved, unchanged, into one file, as ci/lab/mem_pub.sh does
        onnx.save_model(onnx.load_from_string(whole), tmp + "/vision.graph.onnx", save_as_external_data=True, all_tensors_to_one_file=True,
                        location="vision.weights.bin", size_threshold=1024)
        graph, weights = pathlib.Path(tmp, "vision.graph.onnx").read_bytes(), pathlib.Path(tmp, "vision.weights.bin").read_bytes()
    (ext / "vision.graph.onnx").write_bytes(graph)
    at = "http://127.0.0.1:%d/test/rec/models/" % EXT_PORT
    cut = [0, len(weights) // 3, 2 * len(weights) // 3 + 5, len(weights)]
    parts = []
    for i in range(3):
        piece = weights[cut[i]:cut[i + 1]]
        (ext / ("vision.weights.bin.part%02d" % i)).write_bytes(piece)
        parts.append({"url": at + "standin-ext/vision.weights.bin.part%02d" % i, "bytes": len(piece), "sha256": hashlib.sha256(piece).hexdigest()})
    for f in ("species.f16.bin", "species.json"):
        (ext / f).write_bytes((big / f).read_bytes())
    v = {k: x for k, x in mb["vision"].items() if k not in ("parts", "bytes", "sha256")}
    me = dict(mb, id="standin-ext", vision=dict({"graph": {"url": at + "standin-ext/vision.graph.onnx", "bytes": len(graph), "sha256": hashlib.sha256(graph).hexdigest()},
                                                 "weights_name": "vision.weights.bin", "parts": parts, "bytes": len(weights), "sha256": hashlib.sha256(weights).hexdigest()}, **v))
    (ext / "manifest.json").write_text(json.dumps(me, indent=1) + "\n", encoding="utf-8")
    # the same slot's older form (one file in parts: standin-big's), which a check serves in this slot's place first: its parts must stay
    # kept until the form above is kept, and go then
    mo = dict(mb, id="standin-ext-old", vision=dict(mb["vision"], parts=[dict(p, url=p["url"].replace("http://127.0.0.1:8788/test/rec/models/", at)) for p in mb["vision"]["parts"]]))
    (ext / "manifest.old.json").write_text(json.dumps(mo, indent=1) + "\n", encoding="utf-8")
    print("  external form: graph %d bytes, weights %d bytes in three parts" % (len(graph), len(weights)))


if __name__ == "__main__" and "--ext" in sys.argv:
    make_ext()
    sys.exit(0)
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


# ---------- the same slot as a trained head arrives (docs/CONTRACTS.md): rows that are weights and not unit vectors, a bias for
# every row, and the mixing rule. What each photo should give is worked out by the reference, tools/fusion/fuse.py, from Python's
# own embeddings; test/rec/check_rec.js "trained" asks the browser for the same answers.
import sys
sys.path.insert(0, str(here.parents[1] / "tools" / "fusion"))
from fuse import dots as ref_dots, fuse as ref_fuse, load_slot  # noqa: E402

ki = KINDS.index
Kt, kb = K.copy(), np.zeros(len(KINDS))
Kt[ki("bird")] = 0.2 * E["small.png"]                 # small.png: its own short row now loses ...
Kt[ki("hawk")] = 1.6 * near(E["small.png"], 0.7)      # ... to a long row that points partly away. Were rows made unit length, the bird would win.
kb[ki("frog")] = -30.0                                # dots.png: a bias alone takes the frog out
St, sb = Sm * 2.0, np.zeros(len(rows))                # every species row twice as long, at half the temperature: the same scores
sb[[r[0] for r in rows].index("Buteo lineatus")] = 90.0   # small.png: a bias alone lifts a hawk that looks like nothing, and it is named
Kt.astype("<f2").tofile(slot / "kinds.trained.f16.bin")
St.astype("<f2").tofile(slot / "species.trained.f16.bin")
sb.astype("<f4").tofile(slot / "species.bias.f32.bin")
m3 = json.loads(json.dumps(manifest))
m3["id"] = "standin-trained"
m3["kinds"] = {"url": "kinds.trained.f16.bin", "labels": KINDS, "bias": [float(v) for v in kb]}
m3["species"] = {"url": "species.trained.f16.bin", "table": "species.json", "count": len(rows), "bias_url": "species.bias.f32.bin"}
m3["fusion"] = {"t_kind": 50, "t_species": 50, "alpha_prior": 0.5, "w_kind": 0.7, "name_at": 0.6, "offer_at": 0.3, "rule": "mix"}
(slot / "manifest.trained.json").write_text(json.dumps(m3, indent=1) + "\n", encoding="utf-8")
m4 = json.loads(json.dumps(m3)); m4["id"] = "standin-rule-from-the-future"; m4["fusion"]["rule"] = "vote"     # a rule no build knows: the page must refuse the slot, not guess
(slot / "manifest.unknown-rule.json").write_text(json.dumps(m4, indent=1) + "\n", encoding="utf-8")

tr = load_slot(slot / "manifest.trained.json")           # read back as the page reads it, half precision and all
plain = load_slot(slot)
trained = {}
for name in MADE:
    seen = set()
    for month in range(12):
        r = ref_fuse(tr["manifest"], tr["table"], month, ref_dots(tr["kinds"], E[name]), ref_dots(tr["species"], E[name]), kind_bias=tr["kind_bias"], species_bias=tr["species_bias"])
        seen.add((r["kind"], (r["named"] or {}).get("en", ""), tuple(o["en"] for o in r["offers"]), r["kindP"] >= 0.6))
    p0 = ref_fuse(plain["manifest"], plain["table"], 6, ref_dots(plain["kinds"], E[name]), ref_dots(plain["species"], E[name]))
    if len(seen) == 1 and list(seen)[0][3]:             # the same answer in every month, and a clear one
        kind, named, offers, _ = list(seen)[0]
        trained[name] = {"kind": kind, "named": named, "offers": list(offers), "plain_kind": p0["kind"], "plain_named": (p0["named"] or {}).get("en", "")}
expect["trained"] = trained
(slot / "expect.json").write_text(json.dumps(expect, separators=(",", ":")) + "\n", encoding="utf-8")
for name, t in trained.items():
    print("  trained head: %-13s %-8s %-22s offers %s | sentence-made: %s %s" % (name, t["kind"], t["named"] or "-", t["offers"] or "-", t["plain_kind"], t["plain_named"] or "-"))
assert trained["small.png"]["kind"] == "hawk" and trained["small.png"]["named"] == "Red-shouldered Hawk" and trained["small.png"]["plain_kind"] == "bird", trained["small.png"]
assert trained["dots.png"]["kind"] != "frog" and trained["dots.png"]["plain_kind"] == "frog", trained["dots.png"]
assert trained["heron.png"]["named"] == "Great Blue Heron", trained["heron.png"]


# ---------- "not sure is an answer" (fusion.kind_at): the same slot with one photo the kinds cannot settle. odd.png's kind (bee) gets
# a rival row, so that the kinds head gives the bee about six parts in ten; the kinds alone decide here (w_kind 1), and under
# kind_at 0.9 the page must assert nothing, and offer its three likeliest kinds with the species offers of the likeliest.
Ku = K.copy()
Ku[ki("dog")] = near(E["odd.png"], 1 - math.log(0.6 / 0.4) / FUSION["t_kind"])
Ku.astype("<f2").tofile(slot / "kinds.unsure.f16.bin")
m5 = json.loads(json.dumps(manifest))
m5["id"] = "standin-kind-at"
m5["kinds"] = {"url": "kinds.unsure.f16.bin", "labels": KINDS}
m5["fusion"] = dict(FUSION, w_kind=1, kind_at=0.9)
(slot / "manifest.kind-at.json").write_text(json.dumps(m5, indent=1) + "\n", encoding="utf-8")
ku = load_slot(slot / "manifest.kind-at.json")


def answers(s, name):
    """What the reference gives for a photo in each month, January first (the page uses the month of the day it runs)."""
    out = []
    for month in range(12):
        r = ref_fuse(s["manifest"], s["table"], month, None if s["kinds"] is None else ref_dots(s["kinds"], E[name]), ref_dots(s["species"], E[name]), kind_bias=s["kind_bias"], species_bias=s["species_bias"])
        out.append({"kind": r["kind"], "sure": r["sure"], "kindP": round(r["kindP"], 4), "kindOffers": r["kindOffers"], "named": (r["named"] or {}).get("en", ""),
                    "offers": [o["en"] or o["sci"] for o in r["offers"]], "five": [x["en"] or x["sci"] for x in r["species"][:5]]})
    return out


expect["kind_at"] = {name: answers(ku, name) for name in MADE}
assert all(a["sure"] is False and a["kindOffers"][:2] == ["bee", "dog"] and a["named"] == "" for a in expect["kind_at"]["odd.png"]), expect["kind_at"]["odd.png"][0]
assert all(a["sure"] for n, months in expect["kind_at"].items() if n != "odd.png" for a in months), expect["kind_at"]


# ---------- the larger model's stand-in (test/rec/models/standin-big): the same encoder, cut into three parts that a second origin serves
# (test/rec/serve.js <port> cors), with no kinds head: the kind is taken from the species answer. Its species rows are made so that
# it differs from the pocket stand-in where the checks need it to:
#   stripes.png  the pocket says "Insect" and offers three; this one names the Monarch
#   dots.png     the pocket says frog; this one is sure of a Great Egret, a wading bird: the change of eyes is offered, never made
#   small.png    two kinds as likely as each other: it is not sure, and nothing changes
#   wall.png     nothing it knows: it is not sure, and offers its three likeliest kinds when asked from the sheet
big = here / "models" / "standin-big"
big.mkdir(parents=True, exist_ok=True)
BIG_PORT = 8788                                        # where the checks serve the parts from by default (check_rec.js BIG_PORT)
whole = int8.read_bytes()
cut = [0, len(whole) // 3, 2 * len(whole) // 3 + 7, len(whole)]      # three parts of unequal length
parts = []
for i in range(3):
    piece = whole[cut[i]:cut[i + 1]]
    (big / ("vision.int8.onnx.part%02d" % i)).write_bytes(piece)
    parts.append({"url": "http://127.0.0.1:%d/test/rec/models/standin-big/vision.int8.onnx.part%02d" % (BIG_PORT, i), "bytes": len(piece), "sha256": hashlib.sha256(piece).hexdigest()})
brows, bvecs = [], []


def badd(sci, en, kind, m, v):
    brows.append([sci, en, kind, m]); bvecs.append(v / np.linalg.norm(v))


badd("Ardea herodias", "Great Blue Heron", "wader", month_flat, E["heron.png"])
badd("Bidens alba", "Beggarticks", "plant", month_flat, E["garden.jpg"])
badd("Danaus plexippus", "Monarch", "insect", month_flat, near(E["stripes.png"], 0.995))
badd("Dione vanillae", "Gulf Fritillary", "insect", month_flat, near(E["stripes.png"], 0.93))
badd("Danaus gilippus", "Queen", "insect", month_flat, near(E["stripes.png"], 0.92))
badd("Ardea alba", "Great Egret", "wader", month_flat, near(E["dots.png"], 0.995))
badd("Dryophytes cinereus", "Green Treefrog", "frog", month_flat, near(E["dots.png"], 0.90))
badd("Anolis sagrei", "Brown Anole", "reptile", [0] + [40] * 11, near(E["rings.png"], 0.99))
badd("Anolis carolinensis", "Green Anole", "reptile", [40] + [0] * 11, near(E["rings.png"], 0.99))
badd("Apis mellifera", "Western Honey Bee", "bee", month_flat, near(E["odd.png"], 0.995))
badd("Buteo lineatus", "Red-shouldered Hawk", "hawk", month_flat, near(E["small.png"], 0.95))
badd("Cardinalis cardinalis", "Northern Cardinal", "bird", month_flat, near(E["small.png"], 0.95))
badd("Sciurus carolinensis", "Eastern Gray Squirrel", "squirrel", month_flat, near(E["wall.png"], 0.9))      # a wall: two kinds as likely as each other
badd("Odocoileus virginianus", "White-tailed Deer", "deer", month_flat, near(E["wall.png"], 0.9))
for sci, en, kind in filler[:10]:
    if sci not in [r[0] for r in brows]:
        badd(sci, en, kind, month_flat, away(rs.randn(WIDTH)))
Sb = np.stack(bvecs)
Sb.astype("<f2").tofile(big / "species.f16.bin")
(big / "species.json").write_text(json.dumps({"columns": ["sci", "en", "kind", "m"], "species": brows}, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
mb = {
    "id": "standin-big", "licence": manifest["licence"], "source": "test/rec/make_standin.py",
    "vision": {"parts": parts, "bytes": len(whole), "sha256": hashlib.sha256(whole).hexdigest(), "input": "pixel_values", "output": "image_embeds",
               "size": SIZE, "mean": MEAN, "std": STD, "resize": "shortest-bicubic-antialias", "crop": "center"},
    "width": WIDTH,
    "species": {"url": "species.f16.bin", "table": "species.json", "count": len(brows)},
    "fusion": {"t_species": 100, "alpha_prior": 0.5, "name_at": 0.6, "offer_at": 0.3, "kind_at": 0.8},
}
(big / "manifest.json").write_text(json.dumps(mb, indent=1) + "\n", encoding="utf-8")
bs = load_slot(big)
expect["big"] = {name: answers(bs, name) for name in MADE}
(slot / "expect.json").write_text(json.dumps(expect, separators=(",", ":")) + "\n", encoding="utf-8")
for name, months in expect["big"].items():
    a = months[0]
    print("  larger stand-in: %-13s %-8s %.3f %-5s named %-18s kinds offered %s" % (name, a["kind"], a["kindP"], "sure" if a["sure"] else "not", a["named"] or "-", a["kindOffers"] or "-"))
print("  kind_at stand-in: odd.png in January", expect["kind_at"]["odd.png"][0])
eb = {name: months[0] for name, months in expect["big"].items()}
assert all(len({(a["kind"], a["sure"], a["named"], tuple(a["kindOffers"])) for a in months}) == 1 for name, months in expect["big"].items() if name != "rings.png"), "the larger stand-in should say the same in every month, the anoles apart"
assert eb["stripes.png"]["named"] == "Monarch" and eb["dots.png"]["kind"] == "wader" and eb["dots.png"]["named"] == "Great Egret" and eb["dots.png"]["sure"], (eb["stripes.png"], eb["dots.png"])
assert eb["small.png"]["sure"] is False and eb["wall.png"]["sure"] is False and eb["heron.png"]["named"] == "Great Blue Heron" and eb["odd.png"]["named"] == "Western Honey Bee", eb
# the same with a checksum of the whole that the parts cannot meet: every part passes, and the whole must still be refused
mbw = json.loads(json.dumps(mb)); mbw["id"] = "standin-big-bad-whole"; mbw["vision"]["sha256"] = "0" * 64
(big / "manifest.bad-whole.json").write_text(json.dumps(mbw, indent=1) + "\n", encoding="utf-8")
# and with a kinds head, as a larger slot may also come (the kinds head knows "nothing alive" and a person, which a species list cannot)
K.astype("<f2").tofile(big / "kinds.f16.bin")
mbk = json.loads(json.dumps(mb)); mbk["id"] = "standin-big-kinds"; mbk["kinds"] = {"url": "kinds.f16.bin", "labels": KINDS}
mbk["fusion"] = dict(mb["fusion"], t_kind=100, w_kind=0.5)
(big / "manifest.kinds.json").write_text(json.dumps(mbk, indent=1) + "\n", encoding="utf-8")
expect["big_kinds"] = {name: answers(load_slot(big / "manifest.kinds.json"), name) for name in MADE}
(slot / "expect.json").write_text(json.dumps(expect, separators=(",", ":")) + "\n", encoding="utf-8")
assert all(a["kind"] == "none" and a["sure"] for a in expect["big_kinds"]["wall.png"]) and all(a["named"] == "Great Blue Heron" for a in expect["big_kinds"]["heron.png"]), expect["big_kinds"]["wall.png"][0]
make_ext()
