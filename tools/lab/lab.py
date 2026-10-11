"""The model laboratory: turn an image-and-text model into label vectors, image vectors and browser-ready ONNX files.

Usage (run from the repository root; every stage writes into --out, which mirrors a model's pub/lab-<id> branch):

  python3 tools/lab/lab.py text   --model ID --labelset kinds --out DIR
  python3 tools/lab/lab.py text   --model ID --labelset species --species-json PATH --out DIR
  python3 tools/lab/lab.py images --model ID --manifest CSV --photos DIR [--shard i/n] --out DIR
  python3 tools/lab/lab.py export --model ID --manifest CSV --photos DIR --out DIR
  python3 tools/lab/lab.py images-onnx --model ID --variant int8|fp16|fp32 --manifest CSV --photos DIR [--shard i/n] --out DIR
  python3 tools/lab/lab.py merge  --model ID --manifest CSV --out DIR PART_DIR...

Models are described in tools/lab/models.json. Vectors are float16 unit rows (.npy). card.json in --out is updated, never
replaced, so that stages run at different times add to one description of the model.
"""
import argparse
import csv
import hashlib
import json
import math
import os
import pathlib
import platform
import shutil
import sys
import time

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
MODELS = HERE / "models.json"
KINDS = ROOT / "labels" / "kinds.json"


def log(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------------------------------------------------------------
# small helpers


def model_entry(model_id):
    data = json.loads(MODELS.read_text(encoding="utf-8"))
    for m in data["models"]:
        if m["id"] == model_id:
            return m
    raise SystemExit("unknown model id %r; see %s" % (model_id, MODELS))


def unit(x):
    x = np.asarray(x, dtype=np.float32)
    n = np.linalg.norm(x, axis=-1, keepdims=True)
    n[n == 0] = 1.0
    return x / n


def save_f16(path, arr):
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    np.save(path, unit(arr).astype(np.float16))


def update_card(out, patch):
    """Merge `patch` into out/card.json (dicts merge recursively; lists of stages are unioned)."""
    p = pathlib.Path(out) / "card.json"
    card = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}

    def merge(a, b):
        for k, v in b.items():
            if isinstance(v, dict) and isinstance(a.get(k), dict):
                merge(a[k], v)
            elif k == "stages" and isinstance(v, list) and isinstance(a.get(k), list):
                a[k] = sorted(set(a[k]) | set(v))
            else:
                a[k] = v
        return a

    card = merge(card, patch)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(card, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return card


def parse_shard(s):
    if not s:
        return 0, 1
    i, n = s.split("/")
    i, n = int(i), int(n)
    assert 0 <= i < n
    return i, n


def read_manifest(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def eval_name(manifest_path, override=None):
    if override:
        return override
    p = pathlib.Path(manifest_path)
    return p.parent.name if p.name == "manifest.csv" else p.stem


def shard_rows(rows, shard):
    """Contiguous blocks, so that merging is a concatenation in manifest order."""
    i, n = parse_shard(shard)
    per = math.ceil(len(rows) / n) if rows else 0
    return rows[i * per:(i + 1) * per]


def open_rgb(path):
    from PIL import Image

    im = Image.open(path)
    im.load()
    return im.convert("RGB")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def versions():
    v = {"python": platform.python_version(), "numpy": np.__version__}
    for mod in ("torch", "open_clip", "transformers", "timm", "onnx", "onnxruntime", "PIL"):
        try:
            m = __import__(mod)
            v[mod] = getattr(m, "__version__", "?")
        except Exception:
            pass
    return v


# ---------------------------------------------------------------------------------------------------------------------
# model wrappers: each gives encode_text, encode_images (raw, unnormalized embeddings), pixel_values, a vision module for
# export, and a description of its preprocessing.


class Base:
    has_text = True
    torch_model = True

    def __init__(self, entry):
        self.entry = entry

    def describe(self):
        return {}


class OpenClipModel(Base):
    def __init__(self, entry):
        super().__init__(entry)
        import open_clip
        import torch

        self.torch = torch
        src = entry["source"]
        pretrained = entry.get("pretrained")
        if pretrained:
            self.model, _, self.preprocess = open_clip.create_model_and_transforms(src, pretrained=pretrained)
            self.tokenizer = open_clip.get_tokenizer(src)
        else:
            self.model, _, self.preprocess = open_clip.create_model_and_transforms(src)
            self.tokenizer = open_clip.get_tokenizer(src)
        self.model.eval()

    def encode_text(self, texts):
        torch = self.torch
        with torch.no_grad():
            t = self.tokenizer(texts)
            return self.model.encode_text(t).float().numpy()

    def pixel_values(self, images):
        torch = self.torch
        return torch.stack([self.preprocess(im) for im in images])

    def encode_pixels(self, pv):
        torch = self.torch
        with torch.no_grad():
            return self.model.encode_image(pv).float().numpy()

    def vision_module(self):
        torch = self.torch
        model = self.model

        class V(torch.nn.Module):
            def __init__(self):
                super().__init__()
                self.m = model

            def forward(self, pixel_values):
                return self.m.encode_image(pixel_values)

        return V().eval()

    def params(self):
        total = sum(p.numel() for p in self.model.parameters())
        vis = sum(p.numel() for p in self.model.visual.parameters())
        return {"image": vis, "text": total - vis, "total": total}

    def describe(self):
        d = {"transforms": [repr(t) for t in getattr(self.preprocess, "transforms", [])]}
        cfg = getattr(self.model.visual, "preprocess_cfg", None)
        if cfg:
            d["preprocess_cfg"] = {k: (list(v) if isinstance(v, tuple) else v) for k, v in dict(cfg).items()}
        size = None
        mean = std = None
        interp = None
        resize = None
        for t in getattr(self.preprocess, "transforms", []):
            name = type(t).__name__
            if name == "Resize":
                interp = str(getattr(t, "interpolation", "")).split(".")[-1].lower()
                s = t.size
                if isinstance(s, (list, tuple)) and len(s) == 2:
                    resize = "squash to %dx%d" % (s[0], s[1])
                else:
                    resize = "shortest side to %s" % (s if not isinstance(s, (list, tuple)) else s[0])
                d["antialias"] = getattr(t, "antialias", None)
            elif name == "CenterCrop":
                cs = t.size
                size = cs[0] if isinstance(cs, (list, tuple)) else cs
                resize = (resize or "") + ", then centre crop %d" % size
            elif name == "Normalize":
                mean, std = [float(x) for x in t.mean], [float(x) for x in t.std]
            elif name == "ResizeKeepRatio":
                resize = "ResizeKeepRatio %r" % (t.__dict__,)
        if size is None:
            vs = getattr(self.model.visual, "image_size", None)
            size = vs[0] if isinstance(vs, (list, tuple)) else vs
        d.update({"size": int(size) if size else None, "mean": mean, "std": std, "interpolation": interp,
                  "resize": resize})
        return d


def as_tensor(out, name):
    """transformers 4.x returns a tensor from get_*_features; later versions may return an output object."""
    import torch

    if isinstance(out, torch.Tensor):
        return out
    v = getattr(out, name, None)
    if v is None:
        v = out.pooler_output
    return v


class HFModel(Base):
    def __init__(self, entry):
        super().__init__(entry)
        import torch
        from transformers import AutoImageProcessor, AutoModel, AutoTokenizer

        self.torch = torch
        src = entry["source"]
        kw = {}
        try:
            self.model = AutoModel.from_pretrained(src, attn_implementation="eager", **kw)
        except TypeError:
            self.model = AutoModel.from_pretrained(src, **kw)
        self.model.eval()
        self.tokenizer = AutoTokenizer.from_pretrained(src)
        self.improc = AutoImageProcessor.from_pretrained(src)
        self.kind = type(self.model).__name__

    def encode_text(self, texts):
        torch = self.torch
        with torch.no_grad():
            if "Siglip" in self.kind:
                t = self.tokenizer(texts, padding="max_length", max_length=64, truncation=True, return_tensors="pt")
            else:
                t = self.tokenizer(texts, padding=True, truncation=True, max_length=77, return_tensors="pt")
            out = self.model.get_text_features(**t)
            return as_tensor(out, "text_embeds").float().numpy()

    def pixel_values(self, images):
        return self.improc(images=images, return_tensors="pt")["pixel_values"]

    def encode_pixels(self, pv):
        torch = self.torch
        with torch.no_grad():
            out = self.model.get_image_features(pixel_values=pv)
            return as_tensor(out, "image_embeds").float().numpy()

    def vision_module(self):
        torch = self.torch
        model = self.model

        class V(torch.nn.Module):
            def __init__(self):
                super().__init__()
                self.m = model

            def forward(self, pixel_values):
                return as_tensor(self.m.get_image_features(pixel_values=pixel_values), "image_embeds")

        return V().eval()

    def params(self):
        vis = txt = 0
        for name, p in self.model.named_parameters():
            if name.startswith(("vision_model", "visual_projection")):
                vis += p.numel()
            else:
                txt += p.numel()
        return {"image": vis, "text": txt, "total": vis + txt}

    def describe(self):
        ip = self.improc
        size = ip.crop_size if getattr(ip, "do_center_crop", False) else ip.size
        if isinstance(size, dict):
            size_v = size.get("height") or size.get("shortest_edge")
        else:
            size_v = size
        rs = ip.size if isinstance(ip.size, dict) else {"value": ip.size}
        resample = getattr(ip, "resample", None)
        try:
            from PIL import Image

            interp = Image.Resampling(int(resample)).name.lower()
        except Exception:
            interp = str(resample)
        if "shortest_edge" in rs:
            resize = "shortest side to %d (PIL)" % rs["shortest_edge"]
        else:
            resize = "squash to %sx%s (PIL)" % (rs.get("height"), rs.get("width"))
        if getattr(ip, "do_center_crop", False):
            resize += ", then centre crop %s" % (size_v,)
        return {"size": int(size_v), "mean": [float(x) for x in ip.image_mean], "std": [float(x) for x in ip.image_std],
                "interpolation": interp, "resize": resize, "rescale": float(getattr(ip, "rescale_factor", 1 / 255)),
                "image_processor": type(ip).__name__, "model_class": self.kind}


class OnnxOnlyModel(Base):
    """A model published only as an ONNX image encoder, with its own folded-in normalization; no text tower."""

    has_text = False
    torch_model = False

    def __init__(self, entry):
        super().__init__(entry)
        from huggingface_hub import hf_hub_download

        self.files = {}
        for variant, fn in entry["onnx_files"].items():
            self.files[variant] = hf_hub_download(entry["source"], fn)
        import onnxruntime as ort

        self.ort = ort
        ref = entry.get("reference_variant", "fp32")
        self.sess = ort.InferenceSession(self.files[ref], providers=["CPUExecutionProvider"])
        self.input_name = self.sess.get_inputs()[0].name
        self.pp = entry["preprocess"]

    def pixel_values(self, images):
        from PIL import Image

        s = int(self.pp["size"])
        arr = []
        for im in images:
            if self.pp.get("resize") == "squash":
                im2 = im.resize((s, s), Image.Resampling.BICUBIC)
            else:
                w, h = im.size
                sc = s / min(w, h)
                im2 = im.resize((max(s, round(w * sc)), max(s, round(h * sc))), Image.Resampling.BICUBIC)
                l, t = (im2.size[0] - s) // 2, (im2.size[1] - s) // 2
                im2 = im2.crop((l, t, l + s, t + s))
            x = np.asarray(im2, dtype=np.float32) / 255.0
            if self.pp.get("mean"):
                x = (x - np.array(self.pp["mean"], np.float32)) / np.array(self.pp["std"], np.float32)
            arr.append(x.transpose(2, 0, 1))
        return np.stack(arr).astype(np.float32)

    def encode_pixels(self, pv):
        pv = np.asarray(pv, dtype=np.float32)
        b0 = self.sess.get_inputs()[0].shape[0]
        step = b0 if isinstance(b0, int) and b0 > 0 else 16  # some exports fix the batch at 1
        outs = []
        for i in range(0, len(pv), step):
            outs.append(self.sess.run(None, {self.input_name: pv[i:i + step]})[0])
        return np.concatenate(outs).astype(np.float32)

    def params(self):
        import onnx

        m = onnx.load(self.files[self.entry.get("reference_variant", "fp32")])
        n = sum(int(np.prod(t.dims)) for t in m.graph.initializer)
        return {"image": n, "text": None, "total": n, "note": "counted from ONNX initializers"}

    def describe(self):
        d = dict(self.pp)
        d["input_name"] = self.input_name
        return d


def load(entry):
    t0 = time.time()
    loader = entry["loader"]
    if loader == "open_clip":
        m = OpenClipModel(entry)
    elif loader == "transformers":
        m = HFModel(entry)
    elif loader == "onnx":
        m = OnnxOnlyModel(entry)
    else:
        raise SystemExit("unknown loader %r" % loader)
    log("loaded %s via %s in %.1fs" % (entry["id"], loader, time.time() - t0))
    return m


def base_card(entry, m):
    d = m.describe()
    card = {
        "id": entry["id"],
        "source": entry["source"],
        "source_url": entry.get("source_url"),
        "loader": entry["loader"],
        "licence": entry.get("licence"),
        "licence_url": entry.get("licence_url"),
        "role": entry.get("role"),
        "params": m.params(),
        "input": {"size": d.get("size"), "mean": d.get("mean"), "std": d.get("std"),
                  "interpolation": d.get("interpolation"), "resize": d.get("resize")},
        "preprocess_detail": d,
        "software": versions(),
    }
    return card


# ---------------------------------------------------------------------------------------------------------------------
# stage: text


def bioclip_taxonomic(sp):
    """Taxon.taxonomic from Imageomics/bioclip src/imageomics/naming.py: ranks capitalized, epithet lower case."""
    sci = sp.get("sci", "").split()
    genus = sci[0] if sci else sp.get("genus", "")
    epithet = " ".join(sci[1:]) if len(sci) > 1 else ""
    parts = [sp.get("kingdom", ""), sp.get("phylum", ""), sp.get("class", ""), sp.get("order", ""),
             sp.get("family", ""), genus]
    name = " ".join([p.capitalize() for p in parts] + [epithet.lower()]).strip()
    return " ".join(name.split())


def bioclip_scientific(sp):
    sci = sp.get("sci", "").split()
    if not sci:
        return ""
    return " ".join([sci[0].capitalize()] + [s.lower() for s in sci[1:]]).capitalize()


def encode_label_sets(m, groups, batch=256):
    """groups: list of lists of sentences. Each sentence is encoded and unit-normalized; each group is averaged and
    renormalized. Returns (n_groups, d) float32."""
    flat = [s for g in groups for s in g]
    embs = []
    t0 = time.time()
    for i in range(0, len(flat), batch):
        embs.append(unit(m.encode_text(flat[i:i + batch])))
        if (i // batch) % 10 == 0:
            log("  text %d/%d (%.1fs)" % (min(i + batch, len(flat)), len(flat), time.time() - t0))
    embs = np.concatenate(embs) if embs else np.zeros((0, 1), np.float32)
    out, k = [], 0
    for g in groups:
        out.append(unit(embs[k:k + len(g)].mean(axis=0)))
        k += len(g)
    return np.stack(out)


def stage_text(args):
    entry = model_entry(args.model)
    out = pathlib.Path(args.out)
    if entry["loader"] == "onnx":
        log("%s has no text tower; its text vectors are those of its teacher %s" % (entry["id"], entry.get("text_from")))
        update_card(out, {"text": {"note": "no text tower; use the text vectors of %s" % entry.get("text_from")}})
        return
    m = load(entry)
    card = base_card(entry, m)
    if args.labelset == "kinds":
        kinds = json.loads(KINDS.read_text(encoding="utf-8"))
        templates = kinds["templates"]
        names = list(kinds["kinds"].keys())
        groups = [[t.format(p) for p in kinds["kinds"][k] for t in templates] for k in names]
        vec = encode_label_sets(m, groups)
        save_f16(out / "text" / "kinds.f16.npy", vec)
        (out / "text" / "kinds.labels.json").write_text(json.dumps({
            "labels": names,
            "source": "labels/kinds.json",
            "kinds_sha256": sha256(KINDS),
            "method": "every phrase through every template; each sentence unit-normalized; averaged per kind; renormalized",
            "templates": templates, "sentences_per_label": [len(g) for g in groups],
        }, indent=1) + "\n", encoding="utf-8")
        log("kinds: %s -> text/kinds.f16.npy" % (vec.shape,))
        card.setdefault("text", {})["kinds"] = {"rows": len(names), "width": int(vec.shape[1])}
        card["width"] = int(vec.shape[1])
    elif args.labelset == "species":
        sj = json.loads(pathlib.Path(args.species_json).read_text(encoding="utf-8"))
        species = sj["species"]
        kinds = json.loads(KINDS.read_text(encoding="utf-8"))
        templates = kinds["templates"]
        com_groups, sci_groups, tc_groups = [], [], []
        for sp in species:
            en = (sp.get("en") or "").strip()
            sci = bioclip_scientific(sp) or sp.get("sci", "")
            name = en if en else sci
            com_groups.append([t.format(name) for t in templates])
            sci_groups.append([t.format(sci) for t in templates])
            common = en or sci  # make_wds.py: `if not common: common = taxon.scientific`
            tc_groups.append(["a photo of %s with common name %s." % (bioclip_taxonomic(sp), common)])
        region = sj.get("region", {}).get("id", "region")
        meta_rows = [{"key": sp.get("key"), "sci": sp.get("sci"), "en": sp.get("en", ""), "eyes": sp.get("eyes")}
                     for sp in species]
        for setname, groups, how in (
            ("species_com", com_groups, "English name (scientific name when there is none) through every template of labels/kinds.json; averaged; renormalized"),
            ("species_sci", sci_groups, "scientific name through every template of labels/kinds.json; averaged; renormalized"),
            ("species_taxon_com", tc_groups, "one sentence per species in BioCLIP's own caption form 'a photo of {Kingdom Phylum Class Order Family Genus epithet} with common name {common}.' "
             "(Imageomics/bioclip scripts/evobio10m/make_wds.py, key taxon_com.txt; Taxon.taxonomic in src/imageomics/naming.py; common falls back to the scientific name)"),
        ):
            vec = encode_label_sets(m, groups)
            save_f16(out / "text" / ("%s.f16.npy" % setname), vec)
            (out / "text" / ("%s.labels.json" % setname)).write_text(json.dumps({
                "labels": meta_rows, "region": region, "species_json_sha256": sha256(args.species_json),
                "species_source": sj.get("source", {}),
                "method": how, "example": groups[0] if groups else [],
            }, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            log("%s: %s" % (setname, vec.shape))
            card.setdefault("text", {})[setname] = {"rows": len(groups), "width": int(vec.shape[1]), "region": region}
        card["width"] = int(vec.shape[1])
    else:
        raise SystemExit("unknown labelset")
    card["stages"] = ["text-" + args.labelset]
    update_card(out, card)


# ---------------------------------------------------------------------------------------------------------------------
# stage: images


def iter_photos(rows, photos_dir):
    ok, bad = [], []
    for r in rows:
        p = pathlib.Path(photos_dir) / ("%s.jpg" % r["id"])
        if not p.exists():
            bad.append((r["id"], "missing"))
            continue
        ok.append((r["id"], p))
    return ok, bad


def embed_rows(m, rows, photos_dir, batch=32, pixel_fn=None, encode_fn=None):
    pixel_fn = pixel_fn or m.pixel_values
    encode_fn = encode_fn or m.encode_pixels
    ok, bad = iter_photos(rows, photos_dir)
    ids, vecs = [], []
    t0 = time.time()
    done = 0
    for i in range(0, len(ok), batch):
        chunk = ok[i:i + batch]
        ims, cid = [], []
        for rid, p in chunk:
            try:
                ims.append(open_rgb(p))
                cid.append(rid)
            except Exception as e:
                bad.append((rid, "unreadable: %s" % type(e).__name__))
        if not ims:
            continue
        pv = pixel_fn(ims)
        vecs.append(unit(encode_fn(pv)))
        ids.extend(cid)
        done += len(cid)
        if (i // batch) % 5 == 0:
            el = time.time() - t0
            log("  images %d/%d, %.2f photos/s" % (done, len(ok), done / max(el, 1e-6)))
    el = time.time() - t0
    vec = np.concatenate(vecs) if vecs else np.zeros((0, 1), np.float32)
    return ids, vec, bad, el


def stage_images(args, variant=None):
    entry = model_entry(args.model)
    out = pathlib.Path(args.out)
    rows = read_manifest(args.manifest)
    name = eval_name(args.manifest, args.evalname)
    part = shard_rows(rows, args.shard)
    i, n = parse_shard(args.shard)
    log("images: %s, eval %s, shard %d/%d, %d rows" % (entry["id"], name, i, n, len(part)))
    m = load(entry)
    card = base_card(entry, m)
    if variant is None:
        ids, vec, bad, el = embed_rows(m, part, args.photos, batch=args.batch)
        tag = ""
    else:
        import onnxruntime as ort

        f = pathlib.Path(args.onnx) if args.onnx else out / "onnx" / ("vision.%s.onnx" % variant)
        if not f.exists():
            raise SystemExit("no %s; run export first or fetch the model's pub branch into --out" % f)
        so = ort.SessionOptions()
        sess = ort.InferenceSession(str(f), so, providers=["CPUExecutionProvider"])
        iname = sess.get_inputs()[0].name

        def enc(pv):
            pv = pv.numpy() if hasattr(pv, "numpy") else np.asarray(pv)
            return sess.run(None, {iname: pv.astype(np.float32)})[0]

        ids, vec, bad, el = embed_rows(m, part, args.photos, batch=args.batch, encode_fn=enc)
        tag = "." + variant
    suffix = "" if n == 1 else ".shard-%d-of-%d" % (i, n)
    save_f16(out / "images" / ("%s%s%s.f16.npy" % (name, tag, suffix)), vec)
    (out / "images" / ("%s%s%s.ids.json" % (name, tag, suffix))).write_text(json.dumps(ids) + "\n", encoding="utf-8")
    (out / "images" / ("%s%s%s.skipped.json" % (name, tag, suffix))).write_text(json.dumps(bad, indent=0) + "\n", encoding="utf-8")
    log("images: %d embedded, %d skipped, %.1fs (%.2f photos/s)" % (len(ids), len(bad), el, len(ids) / max(el, 1e-6)))
    for rid, why in bad[:50]:
        log("  skipped %s: %s" % (rid, why))
    stats = {"rows": len(part), "embedded": len(ids), "skipped": len(bad), "seconds": round(el, 1),
             "photos_per_second": round(len(ids) / max(el, 1e-6), 2), "machine_cpus": os.cpu_count()}
    card["images"] = {name + tag: {"shards": n, ("shard_%d" % i): stats,
                                   "via": "torch" if variant is None else "onnxruntime CPU, vision.%s.onnx" % variant}}
    card["stages"] = ["images" if variant is None else "images-onnx-" + variant]
    update_card(out, card)


# ---------------------------------------------------------------------------------------------------------------------
# stage: export


def export_onnx(m, path, size, opset):
    import torch

    v = m.vision_module()
    dummy = torch.randn(2, 3, size, size)
    kw = dict(input_names=["pixel_values"], output_names=["image_embeds"],
              dynamic_axes={"pixel_values": {0: "batch"}, "image_embeds": {0: "batch"}},
              opset_version=opset, do_constant_folding=True)
    import inspect

    if "dynamo" in inspect.signature(torch.onnx.export).parameters:
        kw["dynamo"] = False
    # nn.MultiheadAttention (open_clip towers) takes a fused fast path in eval mode without gradients, and that fused
    # operator (aten::_native_multi_head_attention) cannot be exported; turn the fast path off and trace with gradients on.
    try:
        torch.backends.mha.set_fastpath_enabled(False)
    except Exception:
        pass
    with torch.enable_grad():
        torch.onnx.export(v, (dummy,), str(path), **kw)


def ort_session(path, threads=None):
    import onnxruntime as ort

    so = ort.SessionOptions()
    if threads:
        so.intra_op_num_threads = threads
        so.inter_op_num_threads = 1
        so.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL
    return ort.InferenceSession(str(path), so, providers=["CPUExecutionProvider"])


def onnx_ops(path):
    import onnx

    mm = onnx.load(str(path), load_external_data=False)
    ops = {}
    for nd in mm.graph.node:
        key = (nd.domain or "ai.onnx") + "::" + nd.op_type
        ops[key] = ops.get(key, 0) + 1
    opset = {(o.domain or "ai.onnx"): o.version for o in mm.opset_import}
    return ops, opset


def stage_export(args):
    entry = model_entry(args.model)
    out = pathlib.Path(args.out)
    od = out / "onnx"
    od.mkdir(parents=True, exist_ok=True)
    m = load(entry)
    if not m.torch_model:
        raise SystemExit("export applies to torch models; %s is already ONNX" % entry["id"])
    card = base_card(entry, m)
    size = card["input"]["size"]
    tmp = pathlib.Path(args.work or (out.parent / ("_work_" + entry["id"])))
    tmp.mkdir(parents=True, exist_ok=True)
    fp32 = tmp / "vision.fp32.onnx"
    t0 = time.time()
    export_onnx(m, fp32, size, args.opset)
    log("exported fp32 in %.1fs: %.1f MB" % (time.time() - t0, fp32.stat().st_size / 1e6))

    from onnxruntime.quantization import QuantType, quantize_dynamic

    int8 = od / "vision.int8.onnx"
    cands = {}
    for tag, pc in (("int8-per-tensor", False), ("int8-per-channel", True)):
        f = tmp / ("vision.%s.onnx" % tag)
        try:
            quantize_dynamic(str(fp32), str(f), op_types_to_quantize=["MatMul", "Gemm"], weight_type=QuantType.QInt8,
                             per_channel=pc, reduce_range=False, extra_options={"MatMulConstBOnly": True})
            cands[tag] = f
            log("%s: %.1f MB" % (tag, f.stat().st_size / 1e6))
        except Exception as e:
            log("%s failed: %s: %s" % (tag, type(e).__name__, e))
    fp16 = tmp / "vision.fp16.onnx"
    fp16_note = None
    try:
        import onnx

        try:
            from onnxruntime.transformers.float16 import convert_float_to_float16
        except Exception:
            from onnxconverter_common.float16 import convert_float_to_float16
        mm = onnx.load(str(fp32))
        m16 = convert_float_to_float16(mm, keep_io_types=True)
        onnx.save(m16, str(fp16))
        log("fp16: %.1f MB" % (fp16.stat().st_size / 1e6))
    except Exception as e:
        fp16_note = "fp16 conversion failed: %s: %s" % (type(e).__name__, e)
        log(fp16_note)
        fp16 = None

    # parity on real photos
    rows = read_manifest(args.manifest) if args.manifest else []
    ok, bad = iter_photos(rows, args.photos) if rows else ([], [])
    ims, pids = [], []
    for rid, p in ok:
        if len(ims) >= args.parity_n:
            break
        try:
            ims.append(open_rgb(p))
            pids.append(rid)
        except Exception:
            pass
    log("parity photos: %d" % len(ims))
    pv = m.pixel_values(ims) if ims else None
    ref = m.encode_pixels(pv) if ims else None
    pv_np = pv.numpy().astype(np.float32) if pv is not None else None
    files = {"fp32": fp32}
    files.update(cands)
    if fp16 is not None:
        files["fp16"] = fp16
    parity = {"model": entry["id"], "photos": len(ims), "photo_ids": pids, "opset": args.opset,
              "input": "pixel_values: float32 [N,3,%d,%d], already resized, cropped and normalized" % (size, size),
              "output": "image_embeds: float32 [N,%s], projected embedding, NOT unit-normalized (normalize before cosine)" % (card.get("width") or "D"),
              "quantization": "onnxruntime.quantization.quantize_dynamic, op_types_to_quantize=[MatMul, Gemm], weight_type=QInt8, MatMulConstBOnly=True, made twice (per_channel False and True); the one with the higher mean cosine to the original model is published as vision.int8.onnx; convolutions (the patch embedding) stay float32; activations are quantized at run time (DynamicQuantizeLinear + MatMulInteger)",
              "fp16": "onnxruntime.transformers.float16.convert_float_to_float16(keep_io_types=True); input and output stay float32",
              "files": {}}
    if fp16_note:
        parity["fp16_note"] = fp16_note
    xs1 = pv_np[:1] if pv_np is not None else np.random.randn(1, 3, size, size).astype(np.float32)
    for variant, f in files.items():
        info = {"bytes": f.stat().st_size, "mb": round(f.stat().st_size / 1e6, 2)}
        try:
            ops, opset = onnx_ops(f)
            info["ops"] = ops
            info["opset_import"] = opset
        except Exception as e:
            info["ops_error"] = str(e)
        try:
            s = ort_session(f)
            if pv_np is not None:
                outs = []
                for i in range(0, len(pv_np), 8):
                    outs.append(s.run(None, {"pixel_values": pv_np[i:i + 8]})[0])
                got = np.concatenate(outs)
                cos = (unit(got) * unit(ref)).sum(-1)
                info["cosine_vs_torch"] = {"mean": float(cos.mean()), "min": float(cos.min()),
                                           "max": float(cos.max())}
                info["output_norm_mean"] = float(np.linalg.norm(got, axis=-1).mean())
            s1 = ort_session(f, threads=1)
            for _ in range(3):
                s1.run(None, {"pixel_values": xs1})
            ts = []
            for _ in range(20):
                t0 = time.perf_counter()
                s1.run(None, {"pixel_values": xs1})
                ts.append(time.perf_counter() - t0)
            info["latency_ms_1thread"] = {"mean": round(1000 * float(np.mean(ts)), 2),
                                          "min": round(1000 * float(np.min(ts)), 2), "runs": 20, "warmup": 3,
                                          "batch": 1}
        except Exception as e:
            info["run_error"] = "%s: %s" % (type(e).__name__, e)
        parity["files"][variant] = info
        log("%s: %s" % (variant, json.dumps({k: v for k, v in info.items() if k not in ("ops",)})))
    best = None
    for tag in cands:
        c = parity["files"].get(tag, {}).get("cosine_vs_torch", {}).get("mean", -1)
        if "run_error" in parity["files"].get(tag, {}):
            continue
        if best is None or c > parity["files"][best].get("cosine_vs_torch", {}).get("mean", -1) + 1e-4:
            best = tag
    if best is None:
        raise SystemExit("no int8 file ran")
    shutil.copy(cands[best], int8)
    parity["files"]["int8"] = dict(parity["files"][best], chosen_from=best)
    files["int8"] = int8
    log("int8: published %s" % best)
    parity["machine"] = {"cpus": os.cpu_count(), "processor": platform.processor(), "machine": platform.machine()}
    parity["software"] = versions()
    # keep inputs and ORT outputs for the browser (WASM) check
    if pv_np is not None:
        k = min(len(pv_np), args.wasm_n)
        wd = tmp / "wasm"
        wd.mkdir(exist_ok=True)
        pv_np[:k].tofile(wd / "input.f32")
        (wd / "shape.json").write_text(json.dumps([k, 3, size, size]))
        np.ascontiguousarray(ref[:k], dtype=np.float32).tofile(wd / "torch_ref.f32")
        for variant in ("int8", "fp16", "fp32"):
            f = files.get(variant)
            if f is None:
                continue
            try:
                s = ort_session(f)
                got = s.run(None, {"pixel_values": pv_np[:k]})[0]
                np.ascontiguousarray(got, dtype=np.float32).tofile(wd / ("ort_%s.f32" % variant))
            except Exception:
                pass
    # publish int8 always; fp16 and fp32 when under 95 MB
    for variant in ("fp16", "fp32"):
        f = files.get(variant)
        if f is None:
            continue
        if f.stat().st_size < 95e6:
            shutil.copy(f, od / f.name)
            parity["files"][variant]["published"] = True
        else:
            parity["files"][variant]["published"] = False
            parity["files"][variant]["why_not_published"] = "over 95 MB"
    parity["files"]["int8"]["published"] = int8.stat().st_size < 95e6
    if int8.stat().st_size >= 95e6:
        shutil.move(str(int8), str(tmp / int8.name))
        parity["files"]["int8"]["why_not_published"] = "over 95 MB"
    for tag in cands:
        parity["files"][tag]["published"] = False
    for variant in parity["files"]:
        f = od / ("vision.%s.onnx" % variant)
        if f.exists():
            parity["files"][variant]["sha256"] = sha256(f)
    (od / "parity.json").write_text(json.dumps(parity, indent=1) + "\n", encoding="utf-8")
    card["onnx"] = {"input": "pixel_values", "output": "image_embeds", "output_unit_normalized": False,
                    "dynamic_batch": True, "opset": args.opset,
                    "files": {v: {"bytes": i["bytes"], "published": i.get("published", False)} for v, i in parity["files"].items()}}
    card["stages"] = ["export"]
    update_card(out, card)


# ---------------------------------------------------------------------------------------------------------------------
# stage: merge shards and parts into one model directory


def stage_merge(args):
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    rows = read_manifest(args.manifest) if args.manifest else []
    order = {r["id"]: k for k, r in enumerate(rows)}
    shards = {}
    for part in args.parts:
        part = pathlib.Path(part)
        if not part.is_dir():
            continue
        for f in part.rglob("*"):
            if f.is_dir():
                continue
            rel = f.relative_to(part)
            if rel.name in ("log.txt", "card.json") or rel.parts[0] == "_ci":
                continue
            if rel.parts[0] == "images" and ".shard-" in rel.name:
                base = rel.name.split(".shard-")[0]
                shards.setdefault(base, []).append(f)
                continue
            dest = out / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(f, dest)
        c = part / "card.json"
        if c.exists():
            update_card(out, json.loads(c.read_text(encoding="utf-8")))
    for base, fs in shards.items():
        npys = sorted(f for f in fs if f.name.endswith(".f16.npy"))
        allid, allv, skipped = [], [], []
        for npy in npys:
            idf = npy.with_name(npy.name.replace(".f16.npy", ".ids.json"))
            ids = json.loads(idf.read_text())
            v = np.load(npy)
            allid += ids
            allv.append(v)
            sk = npy.with_name(npy.name.replace(".f16.npy", ".skipped.json"))
            if sk.exists():
                skipped += json.loads(sk.read_text())
        if not allv:
            continue
        v = np.concatenate(allv)
        idx = sorted(range(len(allid)), key=lambda k: order.get(allid[k], 10 ** 9 + k))
        v = v[idx]
        allid = [allid[k] for k in idx]
        (out / "images").mkdir(parents=True, exist_ok=True)
        np.save(out / "images" / ("%s.f16.npy" % base), v.astype(np.float16))
        (out / "images" / ("%s.ids.json" % base)).write_text(json.dumps(allid) + "\n")
        (out / "images" / ("%s.skipped.json" % base)).write_text(json.dumps(skipped, indent=0) + "\n")
        log("merged %s: %d shards, %d rows, %d skipped" % (base, len(npys), len(allid), len(skipped)))
        update_card(out, {"images": {base: {"rows_embedded": len(allid), "skipped": len(skipped)}}})


# ---------------------------------------------------------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="stage", required=True)
    t = sub.add_parser("text")
    t.add_argument("--model", required=True)
    t.add_argument("--labelset", choices=["kinds", "species"], required=True)
    t.add_argument("--species-json")
    t.add_argument("--out", required=True)
    for name in ("images", "images-onnx"):
        i = sub.add_parser(name)
        i.add_argument("--model", required=True)
        i.add_argument("--manifest", required=True)
        i.add_argument("--photos", required=True)
        i.add_argument("--shard")
        i.add_argument("--evalname")
        i.add_argument("--batch", type=int, default=32)
        i.add_argument("--out", required=True)
        if name == "images-onnx":
            i.add_argument("--variant", choices=["int8", "fp16", "fp32"], required=True)
            i.add_argument("--onnx", help="the ONNX file (default: OUT/onnx/vision.VARIANT.onnx)")
    e = sub.add_parser("export")
    e.add_argument("--model", required=True)
    e.add_argument("--manifest")
    e.add_argument("--photos")
    e.add_argument("--out", required=True)
    e.add_argument("--work")
    e.add_argument("--opset", type=int, default=17)
    e.add_argument("--parity-n", type=int, default=40)
    e.add_argument("--wasm-n", type=int, default=8)
    g = sub.add_parser("merge")
    g.add_argument("--model", required=True)
    g.add_argument("--manifest")
    g.add_argument("--out", required=True)
    g.add_argument("parts", nargs="*")
    args = ap.parse_args()
    if args.stage == "text":
        if args.labelset == "species" and not args.species_json:
            ap.error("--species-json is needed for the species label sets")
        stage_text(args)
    elif args.stage == "images":
        stage_images(args)
    elif args.stage == "images-onnx":
        stage_images(args, variant=args.variant)
    elif args.stage == "export":
        stage_export(args)
    elif args.stage == "merge":
        stage_merge(args)


if __name__ == "__main__":
    main()
