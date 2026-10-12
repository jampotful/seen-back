#!/usr/bin/env python3
"""How many of the nineteen groups each encoder lets a head find on the world photos: a measurement for the choice of
the base app's encoder (docs/COVERAGE.md, step 4).

For each model, a group head of the kind tools/world/head.py fits (logistic regression, C = 20, a photo weighted by its
group's count to the power -0.5, the licence rule `nc`) is fitted on the world fitting photos alone and read alone,
with no species list, on the world tuning and test photos, every vector from the original model (none from a phone's
runtime, since only TinyCLIP 39M/16 has those). Then, on the tuning photos, the groups are folded as head.py folds
them (the worst failing group back in `other`, refit, until every group carried passes), and the test photos are read
once for the groups carried. The Alachua and COCO photos are left out, since not every model has their vectors; so
this compares encoders on one task and does not stand in for head.py's pass marks.

Usage: python3 -I tools/world/encoders.py ROOT --models tinyclip-39m-16,bioclip-b16 --out OUT
ROOT holds lab/<model>/images/world-fit.* and world-eval.* (and card.json) for each model, and world/ as in head.py.
Writes OUT/encoders.json and OUT/ENCODERS.md.
"""
import argparse
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import head as H  # noqa: E402

NEW = list(H.NEW)


def load(root, model, name):
    p = os.path.join(root, "lab", model, "images", name)
    return H.unit(np.load(p + ".f16.npy")), json.load(open(p + ".ids.json"))


def sets(root, model):
    fit = {r["id"]: r for r in H.read_csv(os.path.join(root, "world", "lab", "world-fit", "manifest.csv"))}
    ev = {r["id"]: r for r in H.read_csv(os.path.join(root, "world", "lab", "world-eval", "manifest.csv"))}
    X, ids = load(root, model, "world-fit")
    keep = [i for i, j in enumerate(ids) if j in fit and H.licence_ok(fit[j]["licence"])]
    out = {"fit": (X[keep], np.array([fit[ids[i]]["group"] for i in keep], dtype=object))}
    Xe, ide = load(root, model, "world-eval")
    for s in ("tune", "test"):
        k = [i for i, j in enumerate(ide) if j in ev and ev[j]["set"] == s]
        out[s] = (Xe[k], np.array([ev[ide[i]]["group"] for i in k], dtype=object))
    return out


def argmax_kind(X, Wk, bk, labels):
    return np.array(labels, dtype=object)[(X.astype(np.float64) @ Wk.T + bk).argmax(1)]


def one(root, model, max_fit=0):
    t0 = time.time()
    S = sets(root, model)
    Xf, yf0 = S["fit"]
    if max_fit and len(yf0) > max_fit:                 # a quick look on a machine with little time: an even sample
        k = np.random.default_rng(H.SEED).choice(len(yf0), max_fit, replace=False)
        Xf, yf0 = Xf[k], yf0[k]
    res = {"model": model, "photos": {k: int(len(v[1])) for k, v in S.items()}, "width": int(Xf.shape[1])}
    try:
        card = json.load(open(os.path.join(root, "lab", model, "card.json")))
        res["params"] = (card.get("params") or {}).get("image")
        res["source"] = card.get("source"); res["licence"] = card.get("licence")
    except (OSError, ValueError):
        pass
    labels_all = H.OLD + NEW
    Wk, bk, info = H.fit_head(Xf, yf0, 0.5, labels_all)
    for s in ("tune", "test"):
        X, y = S[s]
        k = argmax_kind(X, Wk, bk, labels_all)
        marks = H.group_marks(k, y, NEW)
        sel = np.isin(y, H.VIEWS); so = y == "other"
        res["every_group_" + s] = {"right": round(float(np.mean(k == y)), 4), "old_groups_right": round(float(np.mean(k[sel] == y[sel])), 4),
                                   "other_given_a_view": round(float(np.isin(k[so], H.VIEWS).mean()), 4),
                                   "groups_passing": sum(1 for m in marks.values() if m["pass"]), "marks": marks}
    H.log(model, "every group: test right %s, groups passing %d" % (res["every_group_test"]["right"], res["every_group_test"]["groups_passing"]))
    carried, history = list(NEW), []
    while True:
        labels = H.OLD + carried
        Wk, bk, _ = H.fit_head(Xf, H.folded(yf0, carried), 0.5, labels)
        X, y0 = S["tune"]; y = H.folded(y0, carried)
        marks = H.group_marks(argmax_kind(X, Wk, bk, labels), y, carried)
        fails = {g: m for g, m in marks.items() if not m["pass"]}
        history.append({"carried": len(carried), "failing": sorted(fails)})
        if not fails:
            break
        worst = min(fails, key=lambda g: min(fails[g]["named"] or 0, fails[g]["right_when_called"] or 0))
        carried.remove(worst)
        H.log(model, "put back in other:", worst)
    X, y0 = S["test"]; y = H.folded(y0, carried)
    k = argmax_kind(X, Wk, bk, labels)
    marks = H.group_marks(k, y, carried)
    sel = np.isin(y, H.VIEWS); so = y == "other"
    res["folded"] = {"carried": carried, "history": history, "test_marks": marks,
                     "test_passing": sum(1 for m in marks.values() if m["pass"]),
                     "test_right": round(float(np.mean(k == y)), 4), "old_groups_right": round(float(np.mean(k[sel] == y[sel])), 4),
                     "other_given_a_view": round(float(np.isin(k[so], H.VIEWS).mean()), 4)}
    res["seconds"] = round(time.time() - t0)
    H.log(model, "folded: %d carried, %d pass on test" % (len(carried), res["folded"]["test_passing"]))
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("root")
    ap.add_argument("--models", default="tinyclip-39m-16,bioclip-b16,bioclip25-mobile-fastvit")
    ap.add_argument("--out", required=True)
    ap.add_argument("--max-fit", type=int, default=0, help="fit on at most this many photos (0: all)")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    rows = []
    for m in a.models.split(","):
        if not os.path.exists(os.path.join(a.root, "lab", m, "images", "world-eval.f16.npy")):
            H.log(m, "has no world vectors here; left out")
            continue
        rows.append(one(a.root, m, a.max_fit))
    json.dump(rows, open(os.path.join(a.out, "encoders.json"), "w"), indent=1)
    L = ["# Encoders on the world photos", "", "Made by `tools/world/encoders.py` (%s). Heads fitted on the world fitting photos alone and read alone; the original models' vectors." % time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "",
         "| Model | image parameters | width | every group: test right | old groups right | `other` given a view | groups passing (of 19) | after the fold: groups carried | pass on test | old groups right | `other` given a view |",
         "|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|"]
    for r in rows:
        e = r["every_group_test"]; f = r["folded"]
        L.append("| %s | %s | %d | %s | %s | %s | %d | %s | %d | %s | %s |" % (
            r["model"], "{:,}".format(r["params"]) if r.get("params") else "–", r["width"], e["right"], e["old_groups_right"], e["other_given_a_view"],
            e["groups_passing"], ", ".join(f["carried"]) or "none", f["test_passing"], f["old_groups_right"], f["other_given_a_view"]))
    L += ["", "Every group's marks on the test photos with all nineteen carried (named / right when called):", "",
          "| Group | " + " | ".join(r["model"] for r in rows) + " |", "|---|" + "---|" * len(rows)]
    for g in NEW:
        L.append("| %s | " % g + " | ".join("%s / %s" % (r["every_group_test"]["marks"][g]["named"], r["every_group_test"]["marks"][g]["right_when_called"]) for r in rows) + " |")
    open(os.path.join(a.out, "ENCODERS.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    H.log("written", a.out)


if __name__ == "__main__":
    main()
