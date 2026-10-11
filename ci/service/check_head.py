"""Score the laboratory's image vectors with a service head, using the service's arithmetic, and report top-1 on a split.

Usage: python3 ci/service/check_head.py --head service/heads/us-fl-alachua --images images/alachua-2025.f16.npy
           --ids images/alachua-2025.ids.json --manifest data/eval/alachua-2025/manifest.csv [--split test]
This shows that the head's files and prior rule reproduce the first-look numbers before any server is involved.
"""
import argparse
import csv
import json
import pathlib

import numpy as np


def load_head(d):
    d = pathlib.Path(d)
    m = json.loads((d / "manifest.json").read_text(encoding="utf-8"))
    sp = m["species"]
    rows = np.fromfile(d / sp["url"], dtype="<f2").astype(np.float64).reshape(-1, m["width"])
    t = json.loads((d / sp["table"]).read_text(encoding="utf-8"))
    W = np.array([r[3] for r in t["species"]], dtype=np.float64)
    tot = W.sum(0)
    lp = np.log(np.maximum(np.divide(W, tot, out=np.zeros_like(W), where=tot > 0), m["fusion"].get("prior_floor", 1e-6)))
    lp[:, tot <= 0] = 0
    return m, rows, t["keys"], lp.T


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--head", required=True)
    ap.add_argument("--images", required=True)
    ap.add_argument("--ids", required=True)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--split", default="test")
    a = ap.parse_args()
    m, rows, keys, lp = load_head(a.head)
    ids = json.loads(pathlib.Path(a.ids).read_text())
    ids = ids.get("ids") or ids.get("rows") if isinstance(ids, dict) else ids
    E = np.load(a.images).astype(np.float64)
    E /= np.linalg.norm(E, axis=1, keepdims=True)
    byid = {r["id"]: r for r in csv.DictReader(open(a.manifest, encoding="utf-8"))}
    keep = [i for i, x in enumerate(ids) if byid[x]["split"] == a.split]
    y = np.array([int(byid[ids[i]]["key"]) for i in keep])
    mon = np.array([int(byid[ids[i]]["month"]) - 1 for i in keep])
    Z = m["fusion"]["t_species"] * (E[keep] @ rows.T)
    K = np.array(keys)
    t1 = (K[Z.argmax(1)] == y).mean()
    Zp = Z + m["fusion"]["alpha_prior"] * lp[mon]
    t1p = (K[Zp.argmax(1)] == y).mean()
    top5p = (K[np.argsort(-Zp, 1)[:, :5]] == y[:, None]).any(1).mean()
    print("%s split, %d photos: top-1 %.4f without prior, %.4f with prior (t %g, alpha %g), top-5 with prior %.4f"
          % (a.split, len(keep), t1, t1p, m["fusion"]["t_species"], m["fusion"]["alpha_prior"], top5p))


if __name__ == "__main__":
    main()
