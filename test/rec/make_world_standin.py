#!/usr/bin/env python3
"""A stand-in for the full database of the whole world (test/rec/models/standin-world), for the "large" check of
test/rec/check_rec.js. It is the larger stand-in (test/rec/models/standin-big, made by test/rec/make_standin.py: the
same encoder, kept in the same three parts) with its rows in the world database's form (docs/tracks/worlddb.md):

  rows.i8.part00, .part01   the rows at one byte a number, a second origin's (tools/world/pack.py's quantizing)
  scale.f32, table.json     a scale a row; the names
  place.bin, zones.json     a grid of 10-degree cells (tools/world/prior.py's format), and two time zones

Two rows share the Monarch's vector: the Monarch, recorded only round Gainesville, and the Southern Monarch, recorded only
round Buenos Aires; the Great Blue Heron is recorded only round Gainesville, the Rufous Hornero (a vector no photo is near)
only round Buenos Aires, and every other species as often in both. So:
  - in the zone America/Argentina/Buenos_Aires the stripes are the Southern Monarch; in America/New_York (or US/Eastern)
    the Monarch;
  - with no zone the tables know (UTC) the two are even, and neither is named; after the heron is named, the encounter
    rule moves the place to Gainesville, and the stripes are the Monarch.
expect.json holds those answers and, for the page to match, the first guesses and priors as tools/world/place.py works
them out.

Usage: python3 -I test/rec/make_world_standin.py   (after make_standin.py)
"""
import hashlib
import json
import os
import pathlib
import sys

import numpy as np

here = pathlib.Path(__file__).resolve().parent
root = here.parent.parent
sys.path.append(str(root / "tools" / "world"))
import pack  # noqa: E402
import place  # noqa: E402
import prior  # noqa: E402

BIG_PORT = 8788
big = here / "models" / "standin-big"
out = here / "models" / "standin-world"
out.mkdir(parents=True, exist_ok=True)
mb = json.loads((big / "manifest.json").read_text())
W = mb["width"]
expect_photos = json.loads((here / "models" / "standin" / "expect.json").read_text())["photos"]
E = {k: np.array(v["embedding"], np.float64) for k, v in expect_photos.items()}
rows = json.loads((big / "species.json").read_text(encoding="utf-8"))["species"]
V = np.fromfile(big / "species.f16.bin", "<f2").astype(np.float64).reshape(len(rows), W)

names = [[r[0], r[1], r[2]] for r in rows]
vecs = [v for v in V]
mon = [r[0] for r in rows].index("Danaus plexippus")
heron = [r[0] for r in rows].index("Ardea herodias")
names.append(["Danaus erippus", "Southern Monarch", "insect"])
vecs.append(V[mon].copy())
basis = np.stack(list(E.values()))
q_, _ = np.linalg.qr(basis.T)
r_ = np.random.RandomState(5).randn(W)
r_ -= q_ @ (q_.T @ r_)
names.append(["Furnarius rufus", "Rufous Hornero", "bird"])
vecs.append(r_ / np.linalg.norm(r_))
S = len(names)
southern, hornero = S - 2, S - 1
R = np.stack(vecs)
R /= np.linalg.norm(R, axis=1, keepdims=True)
q, sc = pack.quantize(R)

# the rows in two parts, a scale a row, the names
blob = q.tobytes()
half = len(blob) // 2
parts = []
for k, piece in enumerate((blob[:half], blob[half:])):
    (out / ("rows.i8.part%02d" % k)).write_bytes(piece)
    parts.append({"url": "http://127.0.0.1:%d/test/rec/models/standin-world/rows.i8.part%02d" % (BIG_PORT, k), "bytes": len(piece), "sha256": hashlib.sha256(piece).hexdigest()})
sc.astype("<f4").tofile(out / "scale.f32")
# one row that people keep everywhere (a home share, tools/species/EVERYDAY.md): a filler row, so that no answer the checks name changes
home_row = [i for i in range(S) if names[i][1] not in ("Monarch", "Southern Monarch", "Great Blue Heron") and i not in (southern, hornero)][0]
HOME = np.zeros(S)
HOME[home_row] = 0.01
(out / "table.json").write_text(json.dumps({"species": names, "columns": 3, "home": [[home_row, 0.01]]}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

# the place: 10-degree cells; Gainesville's and Buenos Aires's
RES = 10.0
g = place.Grid(RES)
cg, cb = int(g.cell(29.65, -82.32)), int(g.cell(-34.6, -58.4))
cells, rws, cnts = [], [], []
for s in range(S):
    if s in (mon, heron):
        cells.append(cg); rws.append(s); cnts.append(100)
    elif s in (southern, hornero):
        cells.append(cb); rws.append(s); cnts.append(100)
    else:
        cells += [cg, cb]; rws += [s, s]; cnts += [50, 50]
cells, rws, cnts = np.array(cells), np.array(rws), np.array(cnts)
T = np.bincount(cells, weights=cnts, minlength=g.n)
prior.write_place(str(out / "place.bin"), RES, T, rws, cells, cnts, S)
zones = {"res": RES, "zones": {"America/New_York": [[cg], [1.0]], "America/Argentina/Buenos_Aires": [[cb], [1.0]]},
         "alias": {"US/Eastern": "America/New_York", "America/Buenos_Aires": "America/Argentina/Buenos_Aires"}}
(out / "zones.json").write_text(json.dumps(zones, separators=(",", ":")), encoding="utf-8")
PLACE = {"radius_km": 400, "eps": 0.02}


def one(name):
    b = (out / name).read_bytes()
    return {"url": "http://127.0.0.1:%d/test/rec/models/standin-world/%s" % (BIG_PORT, name), "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


FUSION = dict(mb["fusion"])
man = {"id": "standin-world", "licence": mb["licence"], "source": "test/rec/make_world_standin.py", "vision": mb["vision"], "width": W,
       "species": {"count": S, "dtype": "int8", "parts": parts, "bytes": len(blob), "sha256": hashlib.sha256(blob).hexdigest(),
                   "scale": one("scale.f32"), "table": one("table.json")},
       "place": dict(one("place.bin"), zones=one("zones.json"), **PLACE), "fusion": FUSION}
(out / "manifest.json").write_text(json.dumps(man, indent=1) + "\n", encoding="utf-8")

# what the page must say: the reference arithmetic (tools/world/place.py; the page's fusion for a slot without a kinds head)
Rp = place.Records(g, cells, rws, cnts, S)
P = place.Place(Rp, zones={k: (np.array(v[0]), np.array(v[1])) for k, v in zones["zones"].items()}, alias=zones["alias"], home=HOME, **PLACE)
Rq = q.astype(np.float64) * sc[:, None].astype(np.float64)


def answer(photo, zone, met):
    pr = P.log_share(P.posterior(zone, met))
    z = FUSION["t_species"] * (Rq @ E[photo]) + FUSION["alpha_prior"] * pr
    s = np.exp(z - z.max())
    s /= s.sum()
    kinds = {}
    for i, n in enumerate(names):
        kinds[n[2]] = kinds.get(n[2], 0) + s[i]
    kind = max(kinds, key=lambda k: kinds[k])
    top = int(np.argmax(s))
    sure = kinds[kind] >= FUSION.get("kind_at", 0)
    named = names[top][1] if sure and s[top] >= FUSION["name_at"] and names[top][2] == kind else ""
    return {"named": named, "p": round(float(s[top]), 4), "top": names[top][1], "kind": kind}


exp = {"stripes": {"UTC": answer("stripes.png", "UTC", []), "UTC, heron met": answer("stripes.png", "UTC", [heron]),
                   "America/New_York": answer("stripes.png", "America/New_York", []), "US/Eastern": answer("stripes.png", "US/Eastern", []),
                   "America/Argentina/Buenos_Aires": answer("stripes.png", "America/Argentina/Buenos_Aires", [])},
       "heron": {"UTC": answer("heron.png", "UTC", [])},
       "first_guess": {z: [round(float(x), 9) for x in P.first_guess(z)[[cg, cb]]] for z in ("UTC", "America/New_York", "America/Argentina/Buenos_Aires")},
       "after_heron": [round(float(x), 9) for x in P.posterior("UTC", [heron])[[cg, cb]]],
       "log_share_utc_heron": [round(float(x), 9) for x in P.log_share(P.posterior("UTC", [heron]))],
       "cells": [cg, cb], "rows": {"Monarch": mon, "Southern Monarch": southern, "Great Blue Heron": heron},
       "bytes": sum(p["bytes"] for p in mb["vision"]["parts"]) + len(blob) + man["species"]["scale"]["bytes"] + man["species"]["table"]["bytes"] + man["place"]["bytes"] + man["place"]["zones"]["bytes"]}
(out / "expect.json").write_text(json.dumps(exp, indent=1) + "\n", encoding="utf-8")
assert exp["stripes"]["UTC"]["named"] == "", exp["stripes"]
assert exp["stripes"]["UTC, heron met"]["named"] == "Monarch", exp["stripes"]
assert exp["stripes"]["America/New_York"]["named"] == "Monarch" and exp["stripes"]["US/Eastern"]["named"] == "Monarch", exp["stripes"]
assert exp["stripes"]["America/Argentina/Buenos_Aires"]["named"] == "Southern Monarch", exp["stripes"]
assert exp["heron"]["UTC"]["named"] == "Great Blue Heron", exp["heron"]
print(json.dumps({k: v for k, v in exp.items() if k in ("stripes", "heron", "first_guess", "after_heron", "bytes")}, indent=1))
