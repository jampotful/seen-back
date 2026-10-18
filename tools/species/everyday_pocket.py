#!/usr/bin/env python3
"""The pocket model's kind on the photos of the species people photograph at home (tools/species/EVERYDAY.md).

The pocket slot as it ships (models/pocket), TinyCLIP 39M/16's vectors from the laboratory (tools/lab/lab.py, the model
in full precision, where the page runs the int8 file of the same model), and the page's arithmetic through
tools/fusion/fuse.py: away from the county (the kinds head alone with kinds.bias) and in the county's time zone (the head
and the county list with kinds.county_bias, in the photo's month). The kind is right when it is the kind the app gives
the species (tools/species/eyes.py), a group without a view of its own counting as other.

With --detail KEYS (GBIF keys, comma-separated) every photo of those species is written out with the kinds and their
probabilities, and the county list's first species; by_species gives the kinds said for every species' test photos.

Usage: python3 -I tools/species/everyday_pocket.py --species S.csv --photos P.csv --photos-dir DIR --out DIR [--detail KEYS]
"""
import argparse
import csv
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools", "fusion"))
sys.path.insert(0, os.path.join(ROOT, "tools", "lab"))
import fuse  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--species", required=True)
    ap.add_argument("--photos", required=True)
    ap.add_argument("--photos-dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--detail", default="", help="GBIF keys whose photos are written out one by one")
    a = ap.parse_args()
    detail = {int(x) for x in a.detail.split(",") if x.strip()}
    os.makedirs(a.out, exist_ok=True)
    t0 = time.time()
    slot = fuse.load_slot(os.path.join(ROOT, "models", "pocket"))
    m, table = slot["manifest"], slot["table"]
    labels = m["kinds"]["labels"]
    import lab  # noqa: E402
    model = lab.load(lab.model_entry(m["id"]))
    ph = list(csv.DictReader(open(a.photos, encoding="utf-8")))
    ids, X, bad, el = lab.embed_rows(model, ph, a.photos_dir)
    print("photos %d embedded, %d missing, %.0fs" % (len(ids), len(bad), el), flush=True)
    pos = {x: i for i, x in enumerate(ids)}
    ph = [r for r in ph if r["id"] in pos]
    X = X[[pos[r["id"]] for r in ph]].astype(np.float64)
    X /= np.linalg.norm(X, axis=1, keepdims=True)
    kd, sd = X @ slot["kinds"].T, X @ slot["species"].T
    res = {"away": [], "county": []}
    for i, r in enumerate(ph):
        truth = r["kind"] if r["kind"] in labels else "other"
        month = int(r["date"][5:7]) - 1 if len(r.get("date") or "") >= 7 else None
        for c in res:
            if c == "away":
                o = fuse.fuse(m, table, None, kd[i], None, kind_bias=slot["kind_bias"])
            else:
                o = fuse.fuse(m, table, month, kd[i], sd[i], kind_bias=slot["kind_bias"], species_bias=slot["species_bias"],
                              kind_bias_list=slot["kind_bias_list"])
            x = {"id": r["id"], "set": r["set"], "category": r["category"], "key": int(r["gbif_key"]), "sci": r["sci"], "truth": truth,
                 "kind": o["kind"], "sure": bool(o["sure"])}
            if int(r["gbif_key"]) in detail:
                x["kinds"] = [(k["key"], round(k["p"], 3), None if k["head"] is None else round(k["head"], 3)) for k in o["kinds"][:4]]
                x["kindP"] = round(o["kindP"], 3)
                x["species"] = [(y["sci"], round(y["p"], 3), y["kind"]) for y in o["species"][:2]]
                x["zone"] = r.get("zone", "")
            res[c].append(x)
    out = {"model": m["id"], "vectors": "full precision through tools/lab/lab.py", "photos": len(ph), "missing": len(bad), "seconds": round(time.time() - t0)}
    for c, L in res.items():
        for which in ("test", "all"):
            S = [x for x in L if which == "all" or x["set"] == which]
            out["%s_%s" % (c, which)] = {"photos": len(S), "kind_right": float(np.mean([x["kind"] == x["truth"] for x in S])),
                                         "sure": float(np.mean([x["sure"] for x in S])),
                                         "right_when_sure": float(np.mean([x["kind"] == x["truth"] for x in S if x["sure"]] or [np.nan]))}
        by = {}
        for x in L:
            if x["set"] != "test":
                continue
            d = by.setdefault(x["category"], {"n": 0, "right": 0, "said": {}})
            d["n"] += 1
            d["right"] += int(x["kind"] == x["truth"])
            d["said"][x["kind"]] = d["said"].get(x["kind"], 0) + 1
        out["%s_by_category" % c] = by
        bs = {}
        for x in L:
            if x["set"] != "test":
                continue
            d = bs.setdefault(str(x["key"]), {"sci": x["sci"], "truth": x["truth"], "n": 0, "right": 0, "sure": 0, "said": {}})
            d["n"] += 1
            d["right"] += int(x["kind"] == x["truth"])
            d["sure"] += int(x["sure"])
            d["said"][x["kind"]] = d["said"].get(x["kind"], 0) + 1
        out["%s_by_species" % c] = bs
        out["%s_detail" % c] = [x for x in L if x["key"] in detail]
    json.dump(out, open(os.path.join(a.out, "pocket.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in out.items() if "by_" not in k and "detail" not in k}, indent=1))


if __name__ == "__main__":
    main()
