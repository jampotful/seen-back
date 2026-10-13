#!/usr/bin/env python3
"""The full database's world rows packed for the page (docs/tracks/worlddb.md, step 1).

Reads the rows tools/coverage/text.py made in shards (rows.<i>.f16.npy, one sentence a species, unit length) and the
names tools/world/names.py gave them (rows.tsv). Writes to --out:

  rows.i8.partNN   the rows at one byte a number: row i is round(v / s_i) with s_i = max|v| / 127, clipped to
                   -127..127, rows one after another, cut into parts of at most --part bytes
  scale.f32        one little-endian float32 a row, 1 / |q_i|, so that scale_i * q_i is the unit vector the page uses
  table.json       {"species": [[scientific, English, group], ...], "keys": [GBIF key or 0, ...], "columns": 3, ...}
  parts.json       every file and part with its length and SHA-256, the row count and width, and how the rows were made
  check.json       how close the packed rows are to the float16 rows (cosine), on every row

Usage: python3 -I tools/world/pack.py --names names --rows rows --out stage [--part 90000000]
"""
import argparse
import csv
import glob
import hashlib
import json
import os

import numpy as np


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 22), b""):
            h.update(b)
    return h.hexdigest()


def quantize(v):
    """float rows (n, d) -> int8 rows and the float32 scale that makes each a unit vector again."""
    v = np.asarray(v, np.float32)
    s = np.abs(v).max(1, keepdims=True) / 127.0
    s[s == 0] = 1.0
    q = np.clip(np.round(v / s), -127, 127).astype(np.int8)
    n = np.linalg.norm(q.astype(np.float32), axis=1)
    n[n == 0] = 1.0
    return q, (1.0 / n).astype(np.float32)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--names", required=True)
    ap.add_argument("--rows", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--part", type=int, default=90_000_000)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    names = list(csv.DictReader(open(os.path.join(a.names, "rows.tsv"), encoding="utf-8", newline=""), delimiter="\t"))
    shards = sorted(glob.glob(os.path.join(a.rows, "rows.*.f16.npy")))
    metas = [json.load(open(p[:-len(".f16.npy")] + ".json")) for p in shards]
    nshard = metas[0]["of"] if metas else 0
    if len(shards) != nshard or sorted(m["shard"] for m in metas) != list(range(nshard)):
        raise SystemExit("shards: found %d of %d" % (len(shards), nshard))
    metas.sort(key=lambda m: m["shard"])
    for m in metas:
        if m["from_row"] != sum(x["rows"] for x in metas if x["shard"] < m["shard"]):
            raise SystemExit("shard %d does not start where the one before it ends" % m["shard"])
    R = np.concatenate([np.load(os.path.join(a.rows, "rows.%03d.f16.npy" % m["shard"])) for m in metas])
    if R.shape[0] != len(names):
        raise SystemExit("%d rows for %d names" % (R.shape[0], len(names)))
    width = int(R.shape[1])
    print("rows", R.shape, flush=True)

    q, sc = quantize(R.astype(np.float32))
    whole = os.path.join(a.out, "rows.i8")
    q.tofile(whole)
    sc.astype("<f4").tofile(os.path.join(a.out, "scale.f32"))
    # how much the packing changes each row
    cos = np.empty(len(q), np.float32)
    for i in range(0, len(q), 65536):
        f = R[i:i + 65536].astype(np.float32)
        f /= np.maximum(np.linalg.norm(f, axis=1, keepdims=True), 1e-12)
        cos[i:i + 65536] = (q[i:i + 65536].astype(np.float32) * sc[i:i + 65536, None] * f).sum(1)
    check = {"rows": int(len(q)), "cosine_to_float16": {"mean": float(cos.mean()), "min": float(cos.min()),
                                                         "p001": float(np.percentile(cos, 0.1))}}

    parts, off, k, total = [], 0, 0, os.path.getsize(whole)
    with open(whole, "rb") as f:
        while off < total:
            b = f.read(a.part)
            p = os.path.join(a.out, "rows.i8.part%02d" % k)
            open(p, "wb").write(b)
            parts.append({"url": os.path.basename(p), "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()})
            off += len(b)
            k += 1
    whole_sha = sha(whole)
    os.remove(whole)

    def key(x):
        try:
            return int(x or 0)
        except ValueError:
            return 0
    table = {"species": [[r["sci"], r["en"], r["group"]] for r in names], "keys": [key(r["gbif_key"]) for r in names],
             "columns": 3, "names_from": "GBIF backbone (scientific); iNaturalist taxonomy (English)", "rows_from": "tools/world/names.py, tools/world/pack.py"}
    tp = os.path.join(a.out, "table.json")
    with open(tp, "w", encoding="utf-8") as f:
        json.dump(table, f, ensure_ascii=False, separators=(",", ":"))

    def one(name):
        p = os.path.join(a.out, name)
        return {"url": name, "bytes": os.path.getsize(p), "sha256": sha(p)}
    man = {"count": int(len(q)), "width": width, "dtype": "int8", "scale": one("scale.f32"), "table": one("table.json"),
           "rows": {"bytes": int(total), "sha256": whole_sha, "parts": parts},
           "sentences": metas[0].get("sentences"), "short_context": metas[0].get("short_context"),
           "check": check}
    json.dump(man, open(os.path.join(a.out, "parts.json"), "w"), indent=1)
    json.dump(check, open(os.path.join(a.out, "check.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in man.items() if k != "rows"}, indent=1), flush=True)
    print("parts:", [(p["url"], p["bytes"]) for p in parts], flush=True)


if __name__ == "__main__":
    main()
