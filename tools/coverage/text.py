#!/usr/bin/env python3
"""BioCLIP 2's text rows for a block of the names in lists/names.txt. Part of the coverage study (docs/COVERAGE.md).

One sentence per species, "a photo of <Genus epithet>.", encoded by BioCLIP 2's text half (loaded as the laboratory loads
it, tools/lab/lab.py, with its short-context trick), unit-normalized and saved as float16. The live rows of the larger
model average four sentences per species; this study uses one for every list, the Alachua list included, so that the
lists differ only in their size (tools/coverage/score.py also scores the live rows, for comparison).

Usage: python3 tools/coverage/text.py --names lists/names.txt --shard i/n --out rows
"""
import argparse
import json
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "lab"))
import lab  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--names", required=True)
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--out", required=True)
    ap.add_argument("--batch", type=int, default=256)
    ap.add_argument("--templates", choices=("one", "four"), default="one",
                    help="one: 'a photo of X.'; four: the four templates of labels/kinds.json averaged, as the live rows are made")
    a = ap.parse_args()
    names = open(a.names, encoding="utf-8").read().split("\n")
    if names and names[-1] == "":
        names = names[:-1]
    i, n = (int(x) for x in a.shard.split("/"))
    per = math.ceil(len(names) / n)
    lo, hi = i * per, min(len(names), (i + 1) * per)
    block = names[lo:hi]
    os.makedirs(a.out, exist_ok=True)
    m = lab.load(lab.model_entry("bioclip2-l14"))
    templates = ["a photo of {}."]
    if a.templates == "four":
        templates = json.load(open(os.path.join(HERE, "..", "..", "labels", "kinds.json"), encoding="utf-8"))["templates"]
    t0 = time.time()
    out = []
    for j in range(0, len(block), a.batch):
        names_j = [lab.bioclip_scientific({"sci": s}) for s in block[j:j + a.batch]]
        acc = np.zeros((len(names_j), 0), np.float32)
        for k, t in enumerate(templates):
            v = lab.unit(np.asarray(m.encode_text([t.format(x) for x in names_j]), dtype=np.float32))
            acc = v if k == 0 else acc + v
        out.append(lab.unit(acc))
        if (j // a.batch) % 20 == 0:
            print("  rows %d/%d (%.0fs)" % (j + len(names_j), len(block), time.time() - t0), flush=True)
    vec = np.concatenate(out) if out else np.zeros((0, 768), np.float32)
    np.save(os.path.join(a.out, "rows.%03d.f16.npy" % i), vec.astype(np.float16))
    meta = {"shard": i, "of": n, "from_row": lo, "to_row": hi, "rows": int(vec.shape[0]), "width": int(vec.shape[1]) if vec.ndim == 2 else 0,
            "seconds": round(time.time() - t0, 1), "sentences": templates, "short_context": bool(getattr(m, "short_text", False)),
            "first": block[0] if block else "", "last": block[-1] if block else ""}
    json.dump(meta, open(os.path.join(a.out, "rows.%03d.json" % i), "w"), indent=1)
    print(json.dumps(meta), flush=True)


if __name__ == "__main__":
    main()
