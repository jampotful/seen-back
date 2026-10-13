#!/usr/bin/env python3
"""The full database's place files, as the page downloads them (docs/tracks/worlddb.md, step 2).

From pub/world-place (tools/world/grid.py: the records of every database row in each quarter-degree cell, the countries of
the cells) and the tz database, for a grid of --res degrees:

  place.bin    "RGPL"; little-endian u32 version (1), f32 res, u32 rows of cells, u32 columns, u32 species, u32 pairs,
               u32 bytes of pairs; then each cell's research-grade records through 2024 (f32, row after row of cells from
               the south and the west); then, for each species in database order, the varint number of cells it is
               recorded in and, cell by cell in ascending order, the varint step from the cell before (the first: the cell
               itself) and the varint number of records. Varints are unsigned LEB128.
  zones.json   {"res", "zones": {zone: [[cells], [weights]]}, "alias": {name: zone}} from tools/world/zones.py

The page (placeOf in src/cam.rec.js) and tools/world/place.py read the same files.

Usage: python3 -I tools/world/prior.py --place DIR --tzdb DIR --rows N --res 1 --out DIR
"""
import argparse
import glob
import json
import os
import struct
import sys

import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import place  # noqa: E402
import zones  # noqa: E402

MAGIC = b"RGPL"


def varints(v):
    """The LEB128 bytes of each value of v (uint64), concatenated, and the number of bytes of each."""
    v = np.asarray(v, np.uint64)
    n = (1 + (v >= 1 << 7) + (v >= 1 << 14) + (v >= 1 << 21) + (v >= 1 << 28) + (v >= 1 << 35)).astype(np.int64)
    out = np.zeros(int(n.sum()), np.uint8)
    pos = np.concatenate([[0], np.cumsum(n)[:-1]])
    x = v.copy()
    for k in range(int(n.max()) if len(n) else 0):
        live = n > k
        b = (x[live] & np.uint64(127)).astype(np.uint8)
        more = n[live] > k + 1
        out[pos[live] + k] = b | (more.astype(np.uint8) << 7)
        x[live] >>= np.uint64(7)
    return out, n


def write_place(path, res, T, rows, cells, counts, S):
    """rows, cells, counts: one entry a (species, cell) pair, any order."""
    nr, nc = int(round(180 / res)), int(round(360 / res))
    o = np.lexsort((cells, rows))
    rows, cells, counts = np.asarray(rows, np.int64)[o], np.asarray(cells, np.int64)[o], np.asarray(counts, np.int64)[o]
    per = np.bincount(rows, minlength=S)
    first = np.r_[True, rows[1:] != rows[:-1]] if len(rows) else np.zeros(0, bool)
    step = np.where(first, cells, cells - np.r_[0, cells[:-1]])
    # the stream: for each species its count, then its (step, count) pairs
    seq = np.empty(S + 2 * len(rows), np.int64)
    at = np.zeros(S, np.int64)
    at[1:] = np.cumsum(1 + 2 * per[:-1])
    seq[at] = per
    idx = np.repeat(at + 1, per) + 2 * (np.arange(len(rows)) - np.repeat(np.cumsum(per) - per, per))
    seq[idx] = step
    seq[idx + 1] = counts
    body, _ = varints(seq)
    head = MAGIC + struct.pack("<IfIIIII", 1, res, nr, nc, S, len(rows), len(body))
    with open(path, "wb") as f:
        f.write(head)
        f.write(np.asarray(T, "<f4").tobytes())
        f.write(body.tobytes())
    return {"bytes": 32 + 4 * nr * nc + len(body), "pairs": int(len(rows)), "pair_bytes": int(len(body))}


def read_place(path):
    b = open(path, "rb").read()
    if b[:4] != MAGIC:
        raise ValueError("not a place file")
    ver, res, nr, nc, S, npairs, nbytes = struct.unpack("<IfIIIII", b[4:32])
    T = np.frombuffer(b, "<f4", nr * nc, 32).astype(np.float64)
    body = np.frombuffer(b, np.uint8, nbytes, 32 + 4 * nr * nc)
    # decode every varint
    ends = np.nonzero(body < 128)[0]
    starts = np.r_[0, ends[:-1] + 1]
    vals = np.zeros(len(ends), np.int64)
    for k in range(int((ends - starts).max()) + 1 if len(ends) else 0):
        live = starts + k <= ends
        vals[live] += (body[starts[live] + k].astype(np.int64) & 127) << (7 * k)
    rows, cells, counts = np.zeros(npairs, np.int64), np.zeros(npairs, np.int64), np.zeros(npairs, np.int64)
    i, j = 0, 0
    per = np.zeros(S, np.int64)
    # walk the species: count, then pairs
    pos = 0
    heads = []
    for s in range(S):
        m = int(vals[pos])
        heads.append((pos, m))
        pos += 1 + 2 * m
    if pos != len(vals):
        raise ValueError("place file of the wrong length")
    for s, (h, m) in enumerate(heads):
        if m:
            st = vals[h + 1:h + 1 + 2 * m:2]
            ct = vals[h + 2:h + 2 + 2 * m:2]
            rows[j:j + m] = s
            cells[j:j + m] = np.cumsum(st)
            counts[j:j + m] = ct
            j += m
        per[s] = m
    return {"res": float(res), "nr": nr, "nc": nc, "S": S, "T": T, "rows": rows, "cells": cells, "counts": counts}


def load_pairs025(d):
    cs, rs, ns = [], [], []
    for p in sorted(glob.glob(os.path.join(d, "pairs025.*.npz"))):
        z = np.load(p)
        cs.append(z["cell"].astype(np.int32))
        rs.append(z["row"].astype(np.int32))
        ns.append(z["count"].astype(np.int32))
    return np.concatenate(cs), np.concatenate(rs), np.concatenate(ns)


def coarsen(cells025, rows, counts, res):
    f = int(round(res / 0.25))
    cells025, rows, counts = (np.asarray(x, np.int64) for x in (cells025, rows, counts))
    r, c = cells025 // 1440, cells025 % 1440
    cc = (r // f) * (1440 // f) + (c // f)
    key = cc * (1 << 20) + rows
    u, inv = np.unique(key, return_inverse=True)
    n = np.bincount(inv, weights=counts).astype(np.int64)
    return u >> 20, u & ((1 << 20) - 1), n


def build_place(placedir, tzdb, nrows, res, out):
    os.makedirs(out, exist_ok=True)
    c4, r4, n4 = load_pairs025(placedir)
    cells, rows, counts = coarsen(c4, r4, n4, res)
    g = place.Grid(res)
    T = np.bincount(cells, weights=counts, minlength=g.n)
    info = write_place(os.path.join(out, "place.bin"), res, T, rows, cells, counts, nrows)
    country = np.load(os.path.join(placedir, "country025.npy"))
    countries = json.load(open(os.path.join(placedir, "countries.json")))
    totals = np.load(os.path.join(placedir, "totals025.npy"))
    zs, alias, notes = zones.build(tzdb, country, countries, totals, res)
    zj = {"res": res, "zones": {z: [c.tolist(), [round(float(x), 7) for x in w]] for z, (c, w) in sorted(zs.items())}, "alias": dict(sorted(alias.items()))}
    with open(os.path.join(out, "zones.json"), "w") as f:
        json.dump(zj, f, separators=(",", ":"))
    info.update({"zones": len(zs), "aliases": len(alias), "zone_cells": int(sum(len(c) for c, _ in zs.values())),
                 "zones_bytes": os.path.getsize(os.path.join(out, "zones.json")), "notes": notes})
    return info


def load_shipped(d, radius_km, eps):
    """tools/world/place.Place from place.bin and zones.json, as the page reads them."""
    P = read_place(os.path.join(d, "place.bin"))
    g = place.Grid(P["res"])
    R = place.Records(g, P["cells"], P["rows"], P["counts"], P["S"])
    if not np.allclose(R.T, P["T"], rtol=1e-6, atol=1e-3):
        raise ValueError("the cells' records do not add up to their species' records")
    z = json.load(open(os.path.join(d, "zones.json")))
    zs = {k: (np.asarray(v[0], np.int64), np.asarray(v[1], np.float64)) for k, v in z["zones"].items()}
    return place.Place(R, zones=zs, alias=z["alias"], radius_km=radius_km, eps=eps)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--place", required=True)
    ap.add_argument("--tzdb", required=True)
    ap.add_argument("--rows", type=int, required=True)
    ap.add_argument("--res", type=float, default=1.0)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    info = build_place(a.place, a.tzdb, a.rows, a.res, a.out)
    print(json.dumps(info, indent=1))


if __name__ == "__main__":
    main()
