#!/usr/bin/env python3
"""Where every species of the full database is recorded, and where the world test photos were taken
(docs/tracks/worlddb.md, steps 2 to 4). Run by ci/worlddb/grid.sh on a build machine, after its two passes over
iNaturalist's observations.

Inputs (all made by ci/worlddb/grid.sh):
  --rec          one research-grade record dated through 2024 a line: quarter-degree cell, taxon
                 (cell = row * 1440 + column, row = floor((lat + 90) * 4), column = floor((lon + 180) * 4))
  --taxmap       tools/world/groups.py's map: taxon, group, species, order
  --inat-rows    tools/world/names.py's inat_rows.tsv: iNaturalist species, world-list row, database row
  --test-manifest, --test-obs   the world test photos (lab/world-species on pub/data-world) and their observations
  --obs          every research-grade record of the test photos' observers
  --near         up to 300 research-grade records from 2025 on in each one-degree cell holding a test photo
  --countries    Natural Earth's countries (public domain); --tz timezone-boundary-builder's polygons (ODbL, used
                 to label the test photos' and the creatures' time zones, a measurement; nothing of it ships)

Writes to --out (published as pub/world-place):
  pairs025.NN.npz   the records of each database row in each quarter-degree cell: arrays cell, row, count (uint32),
                    sorted by cell then row, in parts under 90 MB
  totals025.npy     records a quarter-degree cell (float64), of the rows above
  country025.npy    the country of each quarter-degree cell's centre (int16 index into countries.json, -1 at sea)
  test.tsv          each test photo: id, uuid, continent, group, row (-1: its species has no row), taxon, lat, lon,
                    date, observer, zone
  met.tsv           up to ten creatures met for each test photo, in the order a test takes them: id, k, source, uuid,
                    row, lat, lon, date, zone. Sources: "before" (the same observer, earlier or the same day), "after"
                    (the same observer, later), "near" (someone else, from 2025 on, in the same one-degree cell). All
                    are research grade, in the photo's time zone, of a species with a row other than the photo's, and
                    of different species from one another
  summary.json      counts, and the number of (cell, row) pairs and their size at coarser grids
"""
import argparse
import csv
import hashlib
import json
import os
import sys

import numpy as np
import pandas as pd

NR, NC = 720, 1440          # quarter-degree cells
SHIFT = 20                  # a key is cell << SHIFT | row


def log(*a):
    print(*a, flush=True)


def varint_len(v):
    v = np.asarray(v, np.uint64)
    return 1 + (v >= 128) + (v >= 16384) + (v >= 2097152) + (v >= 268435456)


def coarse(cell, f):
    r, c = cell // NC, cell % NC
    return (r // f) * (NC // f) + (c // f)


def zones_of(lat, lon, path):
    """The tzid of each point from timezone-boundary-builder's polygons; the nearest polygon's where none holds it."""
    import shapely
    from shapely.geometry import shape
    g = json.load(open(path, encoding="utf-8"))
    geoms, ids = [], []
    for f in g["features"]:
        geoms.append(shape(f["geometry"]))
        ids.append(f["properties"].get("tzid") or f["properties"].get("TZID") or "")
    tree = shapely.STRtree(geoms)
    pts = shapely.points(np.asarray(lon, float), np.asarray(lat, float))
    out = np.array([""] * len(pts), dtype=object)
    if len(pts):
        pi, gi = tree.query(pts, predicate="intersects")
        for p, q in zip(pi, gi):
            if not out[p]:
                out[p] = ids[q]
        miss = np.nonzero(out == "")[0]
        if len(miss):
            nn = tree.nearest(pts[miss])
            for p, q in zip(miss, nn):
                out[p] = ids[q]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    for k in ("rec", "taxmap", "inat-rows", "test-manifest", "test-obs", "obs", "near", "countries", "tz", "out"):
        ap.add_argument("--" + k, required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    summary = {}

    tm = pd.read_csv(a.taxmap, sep="\t", header=None, names=["taxon", "group", "unit", "order"], dtype={"taxon": np.int64, "unit": np.int64},
                     usecols=[0, 2], quoting=3)
    ir = pd.read_csv(a.inat_rows, sep="\t")
    tmax = int(max(tm["taxon"].max(), ir["inat_id"].max())) + 1
    sp_row = np.full(tmax, -1, np.int64)
    sp_row[ir["inat_id"].to_numpy()] = ir["row"].to_numpy()
    unit = np.full(tmax, -1, np.int64)
    unit[tm["taxon"].to_numpy()] = tm["unit"].to_numpy()
    tx_row = np.where(unit >= 0, sp_row[np.clip(unit, 0, tmax - 1)], -1)
    nrows = int(ir["row"].max()) + 1
    assert nrows < (1 << SHIFT)
    log("taxa %d, database rows %d" % (tmax, nrows))

    def row_of(tx):
        tx = np.asarray(tx, np.int64)
        ok = (tx >= 0) & (tx < tmax)
        out = np.full(len(tx), -1, np.int64)
        out[ok] = tx_row[tx[ok]]
        return out

    # every record through 2024, counted a cell and a row
    keys, seen, kept = [], 0, 0
    for ch in pd.read_csv(a.rec, sep="\t", header=None, names=["cell", "taxon"], dtype=np.int64, chunksize=20_000_000):
        r = row_of(ch["taxon"].to_numpy())
        ok = r >= 0
        seen += len(r)
        kept += int(ok.sum())
        keys.append((ch["cell"].to_numpy()[ok] << SHIFT) | r[ok])
        log("  records read %d, with a row %d" % (seen, kept))
    keys = np.concatenate(keys)
    uk, cnt = np.unique(keys, return_counts=True)
    del keys
    cell = (uk >> SHIFT).astype(np.uint32)
    row = (uk & ((1 << SHIFT) - 1)).astype(np.uint32)
    cnt = cnt.astype(np.uint32)
    summary["records_through_2024"] = {"read": seen, "with_a_row": kept, "pairs_at_0.25": int(len(uk))}
    log("pairs at 0.25 degrees: %d" % len(uk))
    totals = np.bincount(cell, weights=cnt, minlength=NR * NC)
    np.save(os.path.join(a.out, "totals025.npy"), totals)
    # in parts, each under 90 MB
    per = 12_000_000
    for k, i in enumerate(range(0, len(cell), per)):
        np.savez_compressed(os.path.join(a.out, "pairs025.%02d.npz" % k), cell=cell[i:i + per], row=row[i:i + per], count=cnt[i:i + per])
    sizes = {}
    for f in (2, 4, 8, 12, 16):
        ck = (coarse(cell.astype(np.int64), f) << SHIFT) | row.astype(np.int64)
        u2, inv = np.unique(ck, return_inverse=True)
        c2 = np.bincount(inv, weights=cnt).astype(np.int64)
        cc = (u2 >> SHIFT)
        rr = (u2 & ((1 << SHIFT) - 1))
        order = np.lexsort((cc, rr))                  # by row, then cell: the layout a species at a time
        cc, rr, c2 = cc[order], rr[order], c2[order]
        first = np.r_[True, rr[1:] != rr[:-1]]
        delta = np.where(first, cc, cc - np.r_[0, cc[:-1]])
        per_row = np.bincount(rr, minlength=nrows)
        est = int(varint_len(delta).sum() + len(c2) + varint_len(per_row).sum())
        sizes["%g" % (0.25 * f)] = {"pairs": int(len(u2)), "cells_with_records": int(len(np.unique(cc))), "bytes_varint_by_species": est,
                                    "pairs_with_one_record": int((c2 == 1).sum())}
        log("grid %g degrees: %s" % (0.25 * f, sizes["%g" % (0.25 * f)]))
    summary["grids"] = sizes

    # countries of the quarter-degree cells, from Natural Earth
    import shapely
    from shapely.geometry import shape
    ne = json.load(open(a.countries, encoding="utf-8"))
    codes, geoms = [], []
    for f in ne["features"]:
        p = f["properties"]
        c = p.get("ISO_A2_EH") or p.get("ISO_A2") or ""
        if c in ("-99", "", None):
            c = p.get("WB_A2") or p.get("ADM0_A3") or "?"
        codes.append(c)
        geoms.append(shape(f["geometry"]))
    names = sorted(set(codes))
    idx = {c: i for i, c in enumerate(names)}
    tree = shapely.STRtree(geoms)
    rr, cc = np.divmod(np.arange(NR * NC), NC)
    pts = shapely.points(-180 + (cc + 0.5) * 0.25, -90 + (rr + 0.5) * 0.25)
    country = np.full(NR * NC, -1, np.int16)
    pi, gi = tree.query(pts, predicate="intersects")
    country[pi] = np.array([idx[codes[g]] for g in gi], np.int16)
    np.save(os.path.join(a.out, "country025.npy"), country)
    json.dump(names, open(os.path.join(a.out, "countries.json"), "w"))
    summary["country_cells"] = int((country >= 0).sum())
    log("cells with a country: %d" % summary["country_cells"])

    # the test photos and their places
    man = list(csv.DictReader(open(a.test_manifest, encoding="utf-8", newline="")))
    tob = {}
    for line in open(a.test_obs, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) >= 7:
            tob[p[0].lower()] = p
    test = []
    for r in man:
        u = r["obs_url"].rstrip("/").split("/")[-1].lower()
        o = tob.get(u)
        tx = int(r["inat_taxon"])
        test.append({"id": r["id"], "uuid": u, "continent": r["continent"], "group": r["group"], "taxon": tx,
                     "row": int(row_of([tx])[0]), "lat": float(o[2]) if o and o[2] else None, "lon": float(o[3]) if o and o[3] else None,
                     "date": o[4] if o else r["date"], "observer": o[1] if o else ""})
    have = [t for t in test if t["lat"] is not None]
    log("test photos %d, with a place %d, with a row %d" % (len(test), len(have), sum(t["row"] >= 0 for t in test)))
    if len(have) < 0.9 * len(test):
        sys.exit("too few test photos found in the observations")
    z = zones_of([t["lat"] for t in have], [t["lon"] for t in have], a.tz)
    for t, zz in zip(have, z):
        t["zone"] = zz
    with open(os.path.join(a.out, "test.tsv"), "w", encoding="utf-8") as f:
        f.write("id\tuuid\tcontinent\tgroup\trow\ttaxon\tlat\tlon\tdate\tobserver\tzone\n")
        for t in test:
            f.write("%s\t%s\t%s\t%s\t%d\t%d\t%s\t%s\t%s\t%s\t%s\n" % (t["id"], t["uuid"], t["continent"], t["group"], t["row"], t["taxon"],
                                                                 "" if t["lat"] is None else "%.5f" % t["lat"], "" if t["lon"] is None else "%.5f" % t["lon"],
                                                                 t["date"], t["observer"], t.get("zone", "")))
    summary["test"] = {"photos": len(test), "with_a_place": len(have), "with_a_row": sum(t["row"] >= 0 for t in test),
                       "zones": len(set(t.get("zone", "") for t in have))}

    # the creatures met: the same observer's, nearest in time (earlier first), then other people's nearby
    def read(path):
        d = pd.read_csv(path, sep="\t", header=None, names=["uuid", "observer", "lat", "lon", "date", "taxon"], dtype=str, quoting=3)
        d = d.dropna(subset=["lat", "lon", "taxon", "date"])
        d["row"] = row_of(pd.to_numeric(d["taxon"], errors="coerce").fillna(-1).astype(np.int64).to_numpy())
        return d[d["row"] >= 0]
    obs = read(a.obs)
    near = read(a.near)
    log("observers' records with a row %d; other people's near the photos %d" % (len(obs), len(near)))
    by_obs = {k: g for k, g in obs.groupby("observer")}
    near["cell1"] = [int(float(y) + 90) * 360 + int(float(x) + 180) for y, x in zip(near["lat"], near["lon"])]
    by_cell = {k: g for k, g in near.groupby("cell1")}
    cand = []                                          # (test index, source, preference, record)
    for i, t in enumerate(test):
        if t["lat"] is None:
            continue
        g = by_obs.get(t["observer"])
        if g is not None:
            g = g[(g["uuid"] != t["uuid"]) & (g["row"] != t["row"])]
            d = pd.to_datetime(g["date"], errors="coerce")
            t0 = pd.to_datetime(t["date"], errors="coerce")
            dd = (t0 - d).dt.days.to_numpy()
            ok = ~np.isnan(dd)
            g, dd = g[ok], dd[ok]
            before = dd >= 0
            pref = np.where(before, dd, 100000 + (-dd))
            o = np.argsort(pref, kind="stable")[:40]
            for j in o:
                cand.append((i, "before" if before[j] else "after", float(pref[j]), g.iloc[j]))
        k1 = int(t["lat"] + 90) * 360 + int(t["lon"] + 180)
        h = by_cell.get(k1)
        if h is not None:
            h = h[(h["observer"] != t["observer"]) & (h["row"] != t["row"])]
            hh = [int(hashlib.sha1(("%s %s" % (t["id"], u)).encode()).hexdigest()[:8], 16) for u in h["uuid"]]
            for j in np.argsort(hh)[:40]:
                cand.append((i, "near", 1e9 + j, h.iloc[j]))
    zc = zones_of([float(c[3]["lat"]) for c in cand], [float(c[3]["lon"]) for c in cand], a.tz) if cand else []
    picked = {}
    for (i, src, pref, rec), zz in sorted(zip(cand, zc), key=lambda x: (x[0][0], x[0][2])):
        t = test[i]
        L = picked.setdefault(i, [])
        if len(L) >= 10 or zz != t.get("zone") or any(int(rec["row"]) == int(x[1]["row"]) for x in L):
            continue
        L.append((src, rec, zz))
    from collections import Counter
    src3 = Counter()
    with open(os.path.join(a.out, "met.tsv"), "w", encoding="utf-8") as f:
        f.write("id\tk\tsource\tuuid\trow\tlat\tlon\tdate\tzone\n")
        for i, L in sorted(picked.items()):
            for k, (src, rec, zz) in enumerate(L, 1):
                f.write("%s\t%d\t%s\t%s\t%d\t%s\t%s\t%s\t%s\n" % (test[i]["id"], k, src, rec["uuid"], int(rec["row"]), rec["lat"], rec["lon"], rec["date"], zz))
            src3[",".join(s for s, _, _ in L[:3])] += 1
    summary["met"] = {"photos_with_three": sum(1 for L in picked.values() if len(L) >= 3), "first_three_by_source": dict(src3.most_common(12))}
    json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1)
    log(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
