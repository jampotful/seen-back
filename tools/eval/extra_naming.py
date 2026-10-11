#!/usr/bin/env python3
"""How often a slot names or offers a species on the extra set's test photos (people, rooms, cats, dogs, grazing animals)
at given thresholds, through tools/fusion/fuse.py.

  python3 -I tools/eval/extra_naming.py <root> <slot dir> --name <label> [--name-at 0.78] [--offer-at 0.67] [--out docs/eval/extra-naming-<label>.json]

A species name on a photo of a person or of a room is always wrong. For a cat or a horse it may be right: the list
holds the Domestic Cat and the Domestic Horse, and no dog, cow or sheep.
"""
import argparse, collections, copy, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "fusion"))
import ev, kinds
import fuse as F

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("slot")
ap.add_argument("--name", required=True)
ap.add_argument("--name-at", type=float)
ap.add_argument("--offer-at", type=float)
ap.add_argument("--out")
a = ap.parse_args()
slot = F.load_slot(a.slot)
man = copy.deepcopy(slot["manifest"])
if a.name_at is not None:
    man["fusion"]["name_at"] = a.name_at
if a.offer_at is not None:
    man["fusion"]["offer_at"] = a.offer_at
model = man["evaluation"]["model"]
XT = kinds.load(a.root, model, want_wasm="wasm" in man["evaluation"]["test_vectors"])
if XT is None or not len(XT["test"]["ids"]):
    raise SystemExit("no vectors of the extra set's test photos for " + model)
X = XT["test"]["X"].astype(np.float64)
X /= np.linalg.norm(X, axis=1, keepdims=True)
kd, sd = X @ slot["kinds"].T, X @ slot["species"].T
eyes = XT["test"]["eyes"]
named, offered = np.zeros(len(X), bool), np.zeros(len(X), bool)
names = collections.defaultdict(collections.Counter)
for j in range(len(X)):
    r = F.fuse(man, slot["table"], int(XT["test"]["month"][j]), kd[j], sd[j], kind_bias=slot["kind_bias"], species_bias=slot["species_bias"])
    named[j], offered[j] = r["named"] is not None, len(r["offers"]) > 0
    if r["named"]:
        names[eyes[j]][r["named"]["en"] or r["named"]["sci"]] += 1
rows = [{"kind": k, "n": int((eyes == k).sum()), "named": ev.ci(named[eyes == k]), "offered": ev.ci(offered[eyes == k]), "commonest_names": names[k].most_common(4)} for k in kinds.EXTRA_KINDS if (eyes == k).any()]
pn = (eyes == "person") | (eyes == "none")
out = {"made_by": "tools/eval/extra_naming.py", "slot": a.name, "model": model, "vectors": XT["test"]["vectors"], "fusion": man["fusion"], "rows": rows,
       "person_or_none": {"n": int(pn.sum()), "named": ev.ci(named[pn]), "offered": ev.ci(offered[pn])}}
for g in rows:
    print("%-7s n %4d named %5.1f%% (%.1f to %.1f)  offered %5.1f%%  %s" % (g["kind"], g["n"], 100 * g["named"][0], 100 * g["named"][1], 100 * g["named"][2], 100 * g["offered"][0], g["commonest_names"]))
ev.write_json(a.out or "docs/eval/extra-naming-%s.json" % a.name, out)
