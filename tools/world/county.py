#!/usr/bin/env python3
"""A trial on tuning photos only: a county bias for a group head.

Where the page uses the county list (in the county's time zone) it could add to each row's bias lambda times the log of
the ratio of the row's label's share among the Alachua training photos to its weighted share among the head's fitting
photos: the classes' prior moved from the world's toward the county's. The kinds those wildlife photos cannot speak for
keep their bias (by default person, none, cat, dog and deer, whose photos come from the COCO set). The Alachua tuning
photos are scored with the list and the COCO tuning photos with the list, against today's page, for lambda 0 to 1.
It reads OUT/head.npz, which tools/world/head.py --dump writes before any test photo is loaded, and reads no test photo.

Usage: python3 -I tools/world/county.py ROOT HEAD_NPZ [--slot models/pocket] [--keep person,none,cat,dog,deer]
       [--weights 1,10,3] (the fit's weights of the world, COCO and Alachua photos; those of --recipe merge)
"""
import argparse
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import head as H  # noqa: E402

F = H.F


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("root")
    ap.add_argument("head")
    ap.add_argument("--slot", default=os.path.join(HERE, "..", "..", "models", "pocket"))
    ap.add_argument("--keep", default="person,none,cat,dog,deer")
    ap.add_argument("--weights", default="1,10,3")
    ap.add_argument("--settings", default="1:0.7,1:0.9,2:0.7", help="t_kind:w_kind pairs to try besides the head's own")
    a = ap.parse_args()
    z = np.load(a.head)
    Wk, b2, labels, carried = z["rows"], z["bias_rows"], list(z["labels"]), [str(g) for g in z["carried"]]
    fu = json.loads(str(z["fusion"]))
    spec = {"species": z["species"], "species_bias": z["species_bias"]}
    today = H.Today(a.root)
    by_key = H.county_keys(a.root)
    W, _ = H.world_parts(a.root, ("fit",), "auto", today)
    A, _ = H.alachua_parts(a.root, ("fit", "tune"), "auto", today, by_key)
    C, _ = H.coco_parts(a.root, ("fit", "tune"), "auto", today)
    slot = F.load_slot(a.slot)
    m_old = slot["manifest"]
    T_old = H.Table(slot, slot["table"], list(F.KINDS))
    sci2group = {r["sci"]: g for (eyes, g, r) in by_key.values()}
    rows = [[r[0], r[1], (sci2group.get(r[0], "other") if r[2] == "other" else r[2]), r[3]] for r in slot["table"]]
    rows = [[r[0], r[1], (r[2] if (r[2] not in H.NEW or r[2] in carried) else "other"), r[3]] for r in rows]
    T = H.Table(spec, rows, H.KINDS_ALL)
    L = H.LABELS

    def shares(ys, ws):
        s = np.zeros(len(L))
        for y, w in zip(ys, ws):
            for k, c in zip(*np.unique(y, return_counts=True)):
                s[L.index(k)] += w * c
        return s / s.sum()
    ww, wc, wa = H.floats(a.weights)
    pfit = shares([W["fit"]["y"], C["fit"]["y"], A["fit"]["y"]], [ww, wc, wa])
    pA = shares([A["fit"]["y"]], [1.0])
    delta = np.log(np.maximum(pA, 1e-4)) - np.log(np.maximum(pfit, 1e-4))
    for k in [k for k in a.keep.split(",") if k]:
        delta[L.index(k)] = 0.0
    ya = H.folded(A["tune"]["y"], carried)
    sel = np.isin(ya, H.VIEWS)
    ko, _ = H.answer(A["tune"]["Xt"], A["tune"]["month"], slot["kinds"], slot["kind_bias"], m_old["kinds"]["labels"], m_old["fusion"], T_old)
    kc_old, _ = H.answer(C["tune"]["Xt"], C["tune"]["month"], slot["kinds"], slot["kind_bias"], m_old["kinds"]["labels"], m_old["fusion"], T_old)
    today_a = float(np.mean(ko[sel] == ya[sel]))
    today_c = H.balanced_share(kc_old, C["tune"]["y"], H.COCO_KEYS)
    print("today's page on the tuning photos: Alachua, old kinds right %.4f; COCO %.4f" % (today_a, today_c))
    print("the head: %s, groups named %s; rows kept unshifted: %s" % (json.dumps({k: fu[k] for k in ("t_kind", "w_kind", "kind_at")}), carried, a.keep))
    print("largest shifts: " + ", ".join("%s %+.2f" % (L[i], delta[i]) for i in np.argsort(-np.abs(delta))[:10]))
    pairs = [(fu["t_kind"], fu["w_kind"])] + [tuple(float(x) for x in p.split(":")) for p in a.settings.split(",") if p]
    pairs = list(dict.fromkeys(pairs))
    out = []
    for lam in (0.0, 0.25, 0.5, 0.75, 1.0):
        for tk, wk in pairs:
            f2 = dict(fu, t_kind=tk, w_kind=wk)
            kb = tk * (b2 + lam * delta)
            ka, _ = H.answer(A["tune"]["X"], A["tune"]["month"], Wk, kb, labels, f2, T)
            kc, _ = H.answer(C["tune"]["X"], C["tune"]["month"], Wk, kb, labels, f2, T)
            sa = float(np.mean(ka[sel] == ya[sel])); sc = H.balanced_share(kc, C["tune"]["y"], H.COCO_KEYS)
            out.append({"lambda": lam, "t_kind": tk, "w_kind": wk, "alachua_old": round(sa, 4), "alachua_change": round(100 * (sa - today_a), 2),
                        "coco": round(sc, 4), "coco_change": round(100 * (sc - today_c), 2)})
            print("lambda %.2f, t_kind %.1f, w_kind %.1f: Alachua old kinds %.4f (%+.2f points); COCO %.4f (%+.2f)" % (lam, tk, wk, sa, 100 * (sa - today_a), sc, 100 * (sc - today_c)))
    json.dump(out, open(os.path.splitext(a.head)[0] + ".county.json", "w"), indent=1)


if __name__ == "__main__":
    main()
