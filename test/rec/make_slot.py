#!/usr/bin/env python3
"""Turn a laboratory model branch (pub/lab-<id>, checked out or extracted into a directory) into a slot the page can load.

  python3 -I test/rec/make_slot.py <lab dir> <out dir> [--species <label set, e.g. species_com>] [--list <species.json of a region>]
                                   [--inat <inat.json of that region>] [--inat-min-share 0.5]
                                   [--fusion '<json>'] [--photos <dir of photos>] [--model int8|fp16|fp32]

Writes <out dir>/manifest.json, vision.<model>.onnx, kinds.f16.bin and, with --species, species.f16.bin and species.json
(rows [scientific, English, kind, twelve monthly weights]; the weights come from --list by GBIF key, and are left out without it).

The names in the table are the names a person is shown. With --inat they are iNaturalist's (data/regions/<region>/inat.json, by GBIF
species key): its scientific name, and its English name where it has one; then the species list's English name; then the label set's.
The vectors were made from GBIF's names and stay as they are: only what is shown changes. GBIF's keys are kept beside the rows
("keys", in row order), so that a row can be traced back to the list whatever it is called on screen.
The fusion settings default to the example in docs/CONTRACTS.md and are marked as untuned.
With --photos it also writes expect.json and pre/<name>.u8: what Pillow and onnxruntime give here for each photo, for test/rec/check_rec.js to compare the browser with.
"""
import argparse, hashlib, json, pathlib, shutil
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("lab"); ap.add_argument("out")
ap.add_argument("--species"); ap.add_argument("--list"); ap.add_argument("--fusion"); ap.add_argument("--photos")
ap.add_argument("--inat", help="iNaturalist's names by GBIF species key: {\"<key>\": {\"inat_id\", \"sci\", \"en\", \"share\"}}")
ap.add_argument("--inat-min-share", type=float, default=0.0, help="use iNaturalist's name only where that taxon has at least this share of the key's records (default: always)")
ap.add_argument("--model", default="int8", help="which of the branch's files to use: int8 (the default), fp16 or fp32")
a = ap.parse_args()
lab, out = pathlib.Path(a.lab), pathlib.Path(a.out)
out.mkdir(parents=True, exist_ok=True)
card = json.loads((lab / "card.json").read_text(encoding="utf-8"))
inp, width = card["input"], card["width"]

model = out / ("vision.%s.onnx" % a.model)
shutil.copyfile(lab / "onnx" / model.name, model)
kinds = np.load(lab / "text" / "kinds.f16.npy")
labels = json.loads((lab / "text" / "kinds.labels.json").read_text(encoding="utf-8"))["labels"]
assert kinds.shape == (len(labels), width), kinds.shape
kinds.astype("<f2").tofile(out / "kinds.f16.bin")

fusion = {"t_kind": 100, "t_species": 100, "alpha_prior": 0.5, "w_kind": 0.5, "name_at": 0.6, "offer_at": 0.3}
note = "untuned: the example values of docs/CONTRACTS.md"
if a.fusion:
    fusion.update(json.loads(a.fusion)); note = "given on the command line"
manifest = {
    "id": card["id"], "licence": card.get("licence", ""), "source": card.get("source_url", card.get("source", "")),
    "vision": {"url": model.name, "bytes": model.stat().st_size, "sha256": hashlib.sha256(model.read_bytes()).hexdigest(),
               "input": card.get("onnx", {}).get("input", "pixel_values"), "output": card.get("onnx", {}).get("output", "image_embeds"),
               "size": inp["size"], "mean": inp["mean"], "std": inp["std"], "resize": "shortest-bicubic-antialias", "crop": "center"},
    "width": width,
    "kinds": {"url": "kinds.f16.bin", "labels": labels},
    "fusion": fusion, "fusion_note": note,
}
if a.species:
    vec = np.load(lab / "text" / (a.species + ".f16.npy"))
    rows = json.loads((lab / "text" / (a.species + ".labels.json")).read_text(encoding="utf-8"))["labels"]
    assert vec.shape == (len(rows), width), vec.shape
    by_key = {}
    if a.list:
        by_key = {s["key"]: s for s in json.loads(pathlib.Path(a.list).read_text(encoding="utf-8"))["species"]}
    inat = json.loads(pathlib.Path(a.inat).read_text(encoding="utf-8")) if a.inat else {}
    told = {"inat_sci": 0, "sci_differs": 0, "inat_en": 0, "list_en": 0, "label_en": 0, "no_en": 0, "below_share": 0}

    def shown(r):
        """The two names a person sees for this row: scientific, English."""
        i, l = inat.get(str(r["key"])) or {}, by_key.get(r["key"]) or {}
        if i and float(i.get("share") or 0) < a.inat_min_share:
            told["below_share"] += 1; i = {}
        clean = lambda v: " ".join(str(v or "").split())
        sci = clean(i.get("sci")) or clean(r["sci"])
        told["inat_sci"] += bool(clean(i.get("sci"))); told["sci_differs"] += bool(clean(i.get("sci"))) and clean(i.get("sci")) != clean(r["sci"])
        for source, en in (("inat_en", clean(i.get("en"))), ("list_en", clean(l.get("en"))), ("label_en", clean(r.get("en"))), ("no_en", "")):
            if en or source == "no_en":
                told[source] += 1
                return sci, en

    table = [list(shown(r)) + [r["eyes"], (by_key.get(r["key"]) or {}).get("m")] for r in rows]
    vec.astype("<f2").tofile(out / "species.f16.bin")
    (out / "species.json").write_text(json.dumps({"columns": ["sci", "en", "kind", "m"], "set": a.species, "names": "inat" if a.inat else "labels",
                                                  "keys": [r["key"] for r in rows], "species": table}, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    manifest["species"] = {"url": "species.f16.bin", "table": "species.json", "count": len(rows)}
    print("species:", len(rows), "rows,", sum(1 for t in table if t[3]), "with monthly weights")
    if a.inat:
        print("names: scientific from iNaturalist for %(inat_sci)d rows (%(sci_differs)d differ from GBIF's); English from iNaturalist %(inat_en)d, "
              "from the species list %(list_en)d, from the label set %(label_en)d, none %(no_en)d; %(below_share)d keys under the share asked for" % told)
(out / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n", encoding="utf-8")
print("slot", out, "| model", manifest["vision"]["bytes"], "bytes | kinds", kinds.shape)

if a.photos:
    import onnxruntime as ort
    from PIL import Image
    S = inp["size"]
    sess = ort.InferenceSession(str(model), providers=["CPUExecutionProvider"])
    (out / "pre").mkdir(exist_ok=True)
    expect = {"photos": {}, "onnxruntime": ort.__version__, "pillow": Image.__version__, "kinds": {}}
    for f in sorted(pathlib.Path(a.photos).iterdir()):
        if f.suffix.lower() not in (".png", ".jpg", ".jpeg"):
            continue
        im = Image.open(f).convert("RGB")
        w, h = im.size
        nw, nh = (S, int(S * h / w)) if w <= h else (int(S * w / h), S)
        r = im.resize((nw, nh), Image.BICUBIC)
        left, top = (nw - S) // 2, (nh - S) // 2
        u8 = np.asarray(r.crop((left, top, left + S, top + S)), dtype=np.uint8)
        x = ((u8.astype(np.float32) / 255.0 - np.array(inp["mean"], dtype=np.float32)) / np.array(inp["std"], dtype=np.float32)).transpose(2, 0, 1)[None].astype(np.float32)
        e = sess.run([manifest["vision"]["output"]], {manifest["vision"]["input"]: x})[0][0].astype(np.float64)
        e /= np.linalg.norm(e)
        (out / "pre" / (f.name + ".u8")).write_bytes(u8.tobytes())
        z = fusion["t_kind"] * (kinds.astype(np.float64) @ e); p = np.exp(z - z.max()); p /= p.sum()
        expect["photos"][f.name] = {"w": w, "h": h, "pre_sha256": hashlib.sha256(u8.tobytes()).hexdigest(), "embedding": [round(float(v), 6) for v in e]}
        expect["kinds"][f.name] = [[labels[i], round(float(p[i]), 4)] for i in np.argsort(-p)[:3]]
    (out / "expect.json").write_text(json.dumps(expect, separators=(",", ":")) + "\n", encoding="utf-8")
    for n, k in expect["kinds"].items():
        print("  python:", n, k)
