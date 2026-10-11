#!/usr/bin/env python3
"""Write a head chosen by Study 2 in the layout docs/CONTRACTS.md gives for models/<slot>/.

  python3 -I tools/eval/export_heads.py <root> --head <root>/heads/<train>/<model>.npz --out <dir>

Writes into <dir>:
  manifest.json            id, licence, source, the image encoder's file name, size and sha256 on the laboratory's branch, width, kinds, species, fusion
  kinds.f16.bin            the laboratory's seventeen kind rows (sentence-made, unit length), little-endian float16
  species.f16.bin          one row a species, little-endian float16; the score of a row is t_species * (row . e) + bias
  species.bias.f32.bin     the biases, little-endian float32 (only when the head has any)
  species.json             {"columns", "keys": [GBIF species keys], "species": [[scientific, English, kind, twelve monthly weights], ...]}, rows in the order of the vectors
The monthly weights are the month's records plus lam times a twelfth of the year's records plus c, so that the page's
own arithmetic (share of the month's weight, floored at prior_floor) gives the prior that was tuned.
name_at and offer_at are left at 2 (never) here; tools/eval/shipped.py sets them from the tuning photos through tools/fusion/fuse.py.
English names follow iNaturalist (data/regions/<region>/inat.json) when that file is published, and the species list otherwise.
This script does not write into models/: the coordinator assembles what ships.
"""
import argparse, json, os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ev

T_SPECIES = 100.0

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("--head", required=True)
ap.add_argument("--out", required=True)
a = ap.parse_args()
z = np.load(a.head, allow_pickle=False)
meta = json.loads(str(z["meta"]))
rows, bias, keep = z["rows"].astype(np.float32), z["bias"].astype(np.float32), z["keep"]
model = meta["model"]
lab = os.path.join(a.root, "lab", model)
card = json.load(open(os.path.join(lab, "card.json"), encoding="utf-8"))
species = ev.read_species(a.root)
os.makedirs(a.out, exist_ok=True)

stored = (rows / np.float32(T_SPECIES)).astype("<f2")
assert np.isfinite(stored).all(), "a row does not fit in float16"
stored.tofile(os.path.join(a.out, "species.f16.bin"))
has_bias = bool(np.abs(bias).max() > 0)
if has_bias:
    bias.astype("<f4").tofile(os.path.join(a.out, "species.bias.f32.bin"))

inat_path = os.path.join(a.root, "data", "regions", ev.REGION, "inat.json")
inat = json.load(open(inat_path, encoding="utf-8")) if os.path.exists(inat_path) else {}
W = ev.prior_weights(np.array([s["m"] for s in species], dtype=np.float64), np.array([s["n"] for s in species], dtype=np.float64), meta["lam"], meta["c"])
table, keys = [], []
for i in keep.tolist():
    s = species[i]
    en = (inat.get(str(s["key"])) or {}).get("en") or s["en"]
    table.append([s["sci"], en, s["eyes"], [round(float(w), 3) for w in W[i]]])
    keys.append(s["key"])
with open(os.path.join(a.out, "species.json"), "w", encoding="utf-8") as f:
    json.dump({"columns": ["sci", "en", "kind", "m"], "names_from": "inat.json" if inat else "species.json", "keys": keys, "species": table}, f, ensure_ascii=False, separators=(",", ":"))
    f.write("\n")

K, klabels = ev.load_text(a.root, model, "kinds")
K.astype("<f2").tofile(os.path.join(a.out, "kinds.f16.bin"))
fus = meta.get("fusion") or {"rule": "mix", "t_kind": 100.0, "w_kind": 0.5}
ship = card.get("ship")
manifest = {
    "id": model, "licence": card.get("licence", ""), "source": card.get("source_url", card.get("source", "")),
    "vision": ({"url": os.path.basename(ship), "bytes": card.get("ship_bytes"), "sha256": card.get("ship_sha256"), "from": "pub/lab-%s:%s" % (model, ship),
                "input": card.get("onnx", {}).get("input", "pixel_values"), "output": card.get("onnx", {}).get("output", "image_embeds"),
                "size": card["input"]["size"], "mean": card["input"]["mean"], "std": card["input"]["std"], "resize": "shortest-bicubic-antialias", "crop": "center"}
               if ship else {"note": "this model runs on the server from its original weights; no file is shipped to the phone", "size": card["input"]["size"], "mean": card["input"]["mean"], "std": card["input"]["std"]}),
    "width": int(rows.shape[1]),
    "kinds": {"url": "kinds.f16.bin", "labels": list(klabels)},
    "species": {"url": "species.f16.bin", "table": "species.json", "count": len(table)},
    "fusion": {"t_kind": fus["t_kind"], "t_species": T_SPECIES, "alpha_prior": round(meta["alpha_prior"], 4), "w_kind": fus["w_kind"], "rule": fus["rule"],
               "name_at": 2.0, "offer_at": 2.0, "prior_floor": 1e-6},
    "fusion_note": "alpha_prior, the prior's smoothing, t_kind, w_kind and the rule were chosen on %s by tools/eval/study2.py; name_at and offer_at are set by tools/eval/shipped.py" % meta["tuned_on"],
    "evaluation": {"model": model, "head": meta["head"], "choice": meta["choice"], "train": meta["train"], "train_vectors": meta["train_vectors"], "test_vectors": meta["test_vectors"],
                   "tuned_on": meta["tuned_on"], "prior_smoothing": {"lam": meta["lam"], "c": meta["c"]}},
    "needs": [n for n in (("species.bias_url (build 7 of the page)" if has_bias else None), ("fusion.rule mix (build 7 of the page)" if fus["rule"] == "mix" else None)) if n],
}
if has_bias:
    manifest["species"]["bias_url"] = "species.bias.f32.bin"
with open(os.path.join(a.out, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=1)
    f.write("\n")
size = sum(os.path.getsize(os.path.join(a.out, n)) for n in os.listdir(a.out))
print("slot", a.out, "| head:", meta["head"], "| species rows", len(table), "| bias:", has_bias, "| %.1f MB without the image encoder" % (size / 1e6))
