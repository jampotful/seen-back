#!/usr/bin/env python3
"""Are the names right on pets and livestock? The extra set's test photos of cats, dogs, horses, cows and sheep, through a slot.

  python3 -I tools/eval/pets.py <root> <slot dir> --name <label> [--out docs/eval/pets-livestock.json]

The category of a photo is COCO's largest annotated object (data/extra/coco-kinds/largest.csv). Each photo goes through
tools/fusion/fuse.py with the slot's own files and thresholds. For each category the script counts how often a species is
named, how often the named species is the domestic species of that category, and what is named when it is another.
The species list holds the Domestic Cat (Felis catus) and the Domestic Horse (Equus caballus); it holds no domestic dog,
cow or sheep, so a name on a photo of one of those is always another species.
"""
import argparse, collections, csv, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "fusion"))
import ev, kinds
import fuse as F

DOMESTIC = {"cat": ("Felis catus",), "dog": ("Canis familiaris", "Canis lupus familiaris"), "horse": ("Equus caballus", "Equus ferus caballus"),
            "cow": ("Bos taurus",), "sheep": ("Ovis aries",)}

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("slot")
ap.add_argument("--name", required=True)
ap.add_argument("--out", default="docs/eval/pets-livestock.json")
a = ap.parse_args()
slot = F.load_slot(a.slot)
man = slot["manifest"]
model = man["evaluation"]["model"]
XT = kinds.load(a.root, model, want_wasm="wasm" in man["evaluation"]["test_vectors"])
largest = {r["id"]: r["largest"] for r in csv.DictReader(open(os.path.join(a.root, "data", "extra", kinds.EXTRA, "largest.csv"), encoding="utf-8"))}
in_table = {r[0] for r in slot["table"]}
X = XT["test"]["X"].astype(np.float64)
X /= np.linalg.norm(X, axis=1, keepdims=True)
kd, sd = X @ slot["kinds"].T, X @ slot["species"].T
cat_of = np.array([largest.get(i, "") for i in XT["test"]["ids"]])
rows = []
for c, dom in DOMESTIC.items():
    idx = np.nonzero(cat_of == c)[0]
    if not len(idx):
        continue
    named = dom_named = top_dom = 0
    wrong = collections.Counter()
    for j in idx:
        r = F.fuse(man, slot["table"], int(XT["test"]["month"][j]), kd[j], sd[j], kind_bias=slot["kind_bias"], species_bias=slot["species_bias"])
        top_dom += r["species"][0]["sci"] in dom
        if r["named"] is not None:
            named += 1
            if r["named"]["sci"] in dom:
                dom_named += 1
            else:
                wrong["%s (%s)" % (r["named"]["en"] or r["named"]["sci"], r["named"]["sci"])] += 1
    n = len(idx)
    rows.append({"category": c, "photos": n, "domestic_in_slot": any(d in in_table for d in dom), "named": "%d (%.1f%%)" % (named, 100.0 * named / n),
                 "domestic": "%d of %d named" % (dom_named, named), "other": "%d of %d named" % (named - dom_named, named),
                 "top_species_domestic": "%d (%.1f%%)" % (top_dom, 100.0 * top_dom / n),
                 "wrong_names": ", ".join("%s %d" % kv for kv in wrong.most_common(5)), "counts": {"photos": n, "named": named, "domestic": dom_named, "top_domestic": top_dom}})
tot = {k: sum(r["counts"][k] for r in rows) for k in ("photos", "named", "domestic", "top_domestic")}
text = ("The %d test photos of the extra set whose largest object COCO files as a cat, dog, horse, cow or sheep went through the slot `%s` (vectors `%s`, its own thresholds). "
        "A species was named for %d of them, and %d of those names were the domestic species of the photo's category. The species list holds the Domestic Cat and the Domestic Horse and no domestic dog, cow or sheep, "
        "so on a dog, cow or sheep every name is another species. The top species, named or not, was the domestic one for %d photos.") % (
    tot["photos"], a.name, XT["test"]["vectors"], tot["named"], tot["domestic"], tot["top_domestic"])
out = {"made_by": "tools/eval/pets.py", "slot": a.name, "model": model, "vectors": XT["test"]["vectors"], "fusion": man["fusion"], "rows": rows, "totals": tot, "text": text}
print(text)
for r in rows:
    print(r["category"], r["photos"], r["named"], r["domestic"], r["top_species_domestic"], "|", r["wrong_names"])
ev.write_json(a.out, out)
