"""How sharp should the service's probabilities be? Scan the temperature with the prior weight scaled alongside it.

Usage: python3 ci/service/calibrate.py --head service/heads/us-fl-alachua --images images/alachua-2025.f16.npy
           --ids images/alachua-2025.ids.json --manifest data/eval/alachua-2025/manifest.csv
Scores are t * cosine + alpha * log prior. Keeping alpha / t fixed at the first-look ratio (0.25 / 30) keeps every
ranking, so top-1 and top-5 do not move; only the probabilities change. For each t this prints, per split, the
negative log-likelihood of the true species (photos whose species is on the list), the median top-1 probability,
the kind of eye taken from the species probabilities summed by kind, and how often the top-1 probability reaches 0.6
and is right when it does. The temperature is chosen on `val`; `test` is shown for reference.
"""
import argparse
import csv
import json

import numpy as np

from check_head import load_head


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--head", required=True)
    ap.add_argument("--images", required=True)
    ap.add_argument("--ids", required=True)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--ratio", type=float, default=0.25 / 30)
    ap.add_argument("--temps", default="30,50,70,85,100,120,150")
    a = ap.parse_args()
    m, rows, keys, lp = load_head(a.head)
    table = json.load(open(a.head + "/" + m["species"]["table"], encoding="utf-8"))
    eyes = np.array([r[2] for r in table["species"]])
    kinds = sorted(set(eyes))
    ki = np.array([kinds.index(e) for e in eyes])
    K = np.array(keys)
    pos = {k: i for i, k in enumerate(keys)}
    ids = json.load(open(a.ids))
    ids = ids.get("ids") or ids.get("rows") if isinstance(ids, dict) else ids
    E = np.load(a.images).astype(np.float64)
    E /= np.linalg.norm(E, axis=1, keepdims=True)
    byid = {r["id"]: r for r in csv.DictReader(open(a.manifest, encoding="utf-8"))}
    best = None
    for split in ("val", "test"):
        sel = [i for i, x in enumerate(ids) if byid[x]["split"] == split]
        y = np.array([int(byid[ids[i]]["key"]) for i in sel])
        ye = np.array([byid[ids[i]]["eyes"] for i in sel])
        mon = np.array([int(byid[ids[i]]["month"]) - 1 for i in sel])
        idx = np.array([pos.get(v, -1) for v in y])
        C = E[sel] @ rows.T
        for t in [float(x) for x in a.temps.split(",")]:
            Z = t * C + a.ratio * t * lp[mon]
            Z -= Z.max(1, keepdims=True)
            P = np.exp(Z)
            P /= P.sum(1, keepdims=True)
            pmax = P.max(1)
            right = K[P.argmax(1)] == y
            ok = idx >= 0
            nll = float(-np.mean(np.log(np.maximum(P[np.arange(len(y))[ok], idx[ok]], 1e-12))))
            Q = np.stack([P[:, ki == k].sum(1) for k in range(len(kinds))], 1)
            ksum = float((np.array(kinds)[Q.argmax(1)] == ye).mean())
            hi = pmax >= 0.6
            print("%-4s t %5.1f alpha %.4f: top-1 %.4f  NLL %.3f  median top-1 p %.3f  kind from summed p %.4f  "
                  "top-1 p >= 0.6 on %.3f of photos, right on %s of those"
                  % (split, t, a.ratio * t, right.mean(), nll, float(np.median(pmax)), ksum, hi.mean(),
                     "%.3f" % right[hi].mean() if hi.any() else "-"))
            if split == "val" and (best is None or nll < best[0]):
                best = (nll, t)
    print("lowest val NLL at t %g (alpha %.4f)" % (best[1], a.ratio * best[1]))


if __name__ == "__main__":
    main()
