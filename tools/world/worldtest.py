#!/usr/bin/env python3
"""The world test of the full database (docs/tracks/worlddb.md, step 4; docs/COVERAGE.md, step 8 of its order of work).

500 research-grade photos from each continent dated 2025 or later (lab/world-species on pub/data-world; BioCLIP 2 L/14's
vectors from the laboratory, pub/lab-bioclip2-l14), scored against every row of the full database as it ships (one byte
a number with a scale a row, pub/naturalist-world), the right species first or not, under four priors:

  none        the rows alone
  zone        the first guess from the phone's time zone alone (tools/world/zones.py), as the page computes it from the
              place files it downloads (tools/world/prior.py, tools/world/place.py)
  zone+3      the same, updated by the encounter rule with three creatures met: the same observer's research-grade
              records in the photo's time zone, the latest dated on or before the photo first, then later ones, then
              other people's from 2025 on in the same one-degree cell (tools/world/grid.py). Each is taken as named
              right by the app, which overstates what the app would know by the share of its names that are wrong
  circle      the true 400 km prior: the records within 400 km of the photo's own place, from quarter-degree cells,
              (n + 1) / (N + S) as tools/coverage/score.py has it

A photo's time zone is the one timezone-boundary-builder's polygons put its place in (measurement only). A photo whose
species has no row counts as wrong. The weight alpha of the prior's logarithm is chosen for each continent on the
other six (from 0 to 3), so no continent's photos choose their own setting. So is the level at which a
species is named: the lowest probability (softmax at temperature 100, the page's t_species) from which at least 97
names in 100 were right on the other six continents. Intervals: 2000 bootstrap resamples over photos, seed 20261011.

Usage: python3 -I tools/world/worldtest.py --rows DIR --vectors PREFIX --place DIR --ship DIR[,DIR] --out DIR
         [--limit N] [--radius 400] [--eps 0.02]
  --rows: pub/naturalist-world (parts.json, rows.i8.partNN, scale.f32); --vectors: images/world-species (.f16.npy,
  .ids.json); --place: pub/world-place; --ship: directories of place.bin and zones.json (tools/world/prior.py), one a grid
"""
import argparse
import csv
import json
import os
import sys
import time

import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import place  # noqa: E402
import prior  # noqa: E402

T = 100.0
ALPHAS = (0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0)
CONTINENTS = ("AF", "AS", "EU", "NA", "OC", "SA", "AN")
NAMES_RIGHT = 0.97
rng = np.random.default_rng(20261011)


def log(*a):
    print(*a, flush=True)


def boot(x):
    x = np.asarray(x, np.float64)
    if len(x) == 0:
        return [None, None, None, 0]
    idx = rng.integers(0, len(x), size=(2000, len(x)))
    b = x[idx].mean(1)
    return [float(x.mean()), float(np.percentile(b, 2.5)), float(np.percentile(b, 97.5)), int(len(x))]


def load_rows(d):
    """The rows as the page has them: one byte a number (int8, rows x width) and a float32 scale a row."""
    m = json.load(open(os.path.join(d, "parts.json")))
    raw = bytearray()
    for p in m["rows"]["parts"]:
        raw += open(os.path.join(d, p["url"]), "rb").read()
    q = np.frombuffer(bytes(raw), np.int8).reshape(m["count"], m["width"])
    sc = np.fromfile(os.path.join(d, "scale.f32"), "<f4")
    return q, sc, m


def scores(Xb, Q, sc, chunk=32768):
    """T * (x . row) for every photo of Xb and every row, a block of rows at a time."""
    out = np.empty((Xb.shape[0], Q.shape[0]), np.float32)
    for i in range(0, Q.shape[0], chunk):
        out[:, i:i + chunk] = (Xb @ Q[i:i + chunk].astype(np.float32).T) * (sc[i:i + chunk] * np.float32(T))[None, :]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--rows", required=True)
    ap.add_argument("--vectors", required=True)
    ap.add_argument("--place", required=True)
    ap.add_argument("--ship", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, default=0, help="photos a continent (0: all)")
    ap.add_argument("--radius", type=float, default=400.0)
    ap.add_argument("--eps", type=float, default=0.02)
    ap.add_argument("--batch", type=int, default=125)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    t0 = time.time()

    Q, sc, man = load_rows(a.rows)
    S = Q.shape[0]
    log("rows %s (%.0fs)" % (Q.shape, time.time() - t0))
    X = np.load(a.vectors + ".f16.npy").astype(np.float32)
    X /= np.linalg.norm(X, axis=1, keepdims=True)
    ids = json.load(open(a.vectors + ".ids.json"))
    ids = ids.get("ids") if isinstance(ids, dict) else ids
    pos = {x: i for i, x in enumerate(ids)}
    test = [r for r in csv.DictReader(open(os.path.join(a.place, "test.tsv"), encoding="utf-8"), delimiter="\t") if r["id"] in pos and r["lat"]]
    if a.limit:
        keep = []
        for c in CONTINENTS:
            keep += [r for r in test if r["continent"] == c][:a.limit]
        test = keep
    met = {}
    for r in csv.DictReader(open(os.path.join(a.place, "met.tsv"), encoding="utf-8"), delimiter="\t"):
        met.setdefault(r["id"], []).append(r)
    n = len(test)
    truth = np.array([int(r["row"]) for r in test], np.int64)
    cont = np.array([r["continent"] for r in test])
    Xt = X[[pos[r["id"]] for r in test]]
    log("photos %d, with a row %d; zones %d" % (n, int((truth >= 0).sum()), len(set(r["zone"] for r in test))))

    ships = a.ship.split(",")
    P = {}
    for d in ships:
        P[d] = prior.load_shipped(d, a.radius, a.eps)
        log("place files %s: grid %g degrees, pairs %d (%.0fs)" % (d, P[d].g.res, len(P[d].R.rows), time.time() - t0))
    c4, r4, n4 = prior.load_pairs025(a.place)
    if not (np.diff(c4) >= 0).all():
        o = np.argsort(c4, kind="stable")
        c4, r4, n4 = c4[o], r4[o], n4[o]
    st4 = np.searchsorted(c4, np.arange(720 * 1440 + 1))
    conds = ["none"] + ["zone@%s" % d for d in ships] + ["zone+3@%s" % d for d in ships] + ["circle"]
    met_used = np.zeros(n, np.int64)
    zcache = {}
    # results: for each condition and alpha, the photo's top row and the top probability
    top = {c: np.full((len(ALPHAS), n), -1, np.int64) for c in conds}
    ptop = {c: np.zeros((len(ALPHAS), n), np.float32) for c in conds}
    in3 = {c: np.zeros((len(ALPHAS), n), bool) for c in conds}        # the right species among the three likeliest
    p3 = {c: np.zeros((len(ALPHAS), n), np.float32) for c in conds}   # and the three's probability
    for b0 in range(0, n, a.batch):
        b1 = min(n, b0 + a.batch)
        Sc = scores(Xt[b0:b1], Q, sc)
        pri = {}
        for c in conds:
            if c == "none":
                continue
            M = np.empty((b1 - b0, S), np.float32)
            for k, i in enumerate(range(b0, b1)):
                r = test[i]
                if c == "circle":
                    M[k] = place.circle_share(float(r["lat"]), float(r["lon"]), c4, r4, n4, S, a.radius, st4)
                else:
                    d = c.split("@", 1)[1]
                    Pd = P[d]
                    if c.startswith("zone@"):
                        key = (d, r["zone"])
                        if key not in zcache:
                            zcache[key] = Pd.log_share(Pd.first_guess(r["zone"])).astype(np.float32)
                        M[k] = zcache[key]
                    else:
                        rows3 = [int(x["row"]) for x in met.get(r["id"], [])][:3]
                        met_used[i] = len(rows3)
                        M[k] = Pd.log_share(Pd.posterior(r["zone"], rows3))
            pri[c] = M
        for c in conds:
            for ai, al in enumerate(ALPHAS):
                Z = Sc if (c == "none" or al == 0) else Sc + np.float32(al) * pri[c]
                am = Z.argmax(1)
                mx = Z[np.arange(len(am)), am]
                lse = mx + np.log(np.exp(Z - mx[:, None]).sum(1))
                t3 = np.argpartition(-Z, 3, axis=1)[:, :3]
                z3 = np.take_along_axis(Z, t3, 1)
                ok3 = (t3 == truth[b0:b1, None]).any(1) & (truth[b0:b1] >= 0)
                pp3 = np.exp(z3 - lse[:, None]).sum(1)
                sl = slice(None) if c == "none" else ai
                top[c][sl, b0:b1] = am
                ptop[c][sl, b0:b1] = np.exp(mx - lse)
                in3[c][sl, b0:b1] = ok3
                p3[c][sl, b0:b1] = pp3
                if c == "none":
                    break
        log("  photos %d/%d (%.0fs)" % (b1, n, time.time() - t0))

    hit = {c: (top[c] == truth[None, :]) & (truth[None, :] >= 0) for c in conds}
    out = {"photos": n, "rows": S, "with_a_row": boot(truth >= 0), "alphas": list(ALPHAS), "names_right_wanted": NAMES_RIGHT,
           "radius_km": a.radius, "eps": a.eps, "creatures_met": {"photos_with_three": int((met_used == 3).sum()), "fewer": int(((met_used < 3) & (met_used >= 0)).sum())},
           "grids": {d: {"res": P[d].g.res, "pairs": int(len(P[d].R.rows))} for d in ships}, "by_condition": {}}
    for c in conds:
        e = {"by_continent": {}, "alpha_on_all": None}
        # the setting each continent gets from the other six
        ok_all = np.zeros(n, bool)
        named_all = np.zeros(n, bool)
        for C in CONTINENTS:
            here = cont == C
            if not here.any():
                continue
            other = ~here
            ai = max(range(len(ALPHAS)), key=lambda j: (hit[c][j, other].mean(), -ALPHAS[j]))
            if c == "none":
                ai = 0
            # the naming level: lowest probability from which the other six were right 97 times in 100
            p, h = ptop[c][ai, other], hit[c][ai, other]
            lvl = None
            for tau in np.round(np.arange(0.99, 0.0049, -0.01), 2):
                m = p >= tau
                if m.sum() < 50:
                    continue
                if h[m].mean() >= NAMES_RIGHT:
                    lvl = float(tau)
                else:
                    break
            hh = hit[c][ai, here]
            nm = (ptop[c][ai, here] >= lvl) if lvl is not None else np.zeros(int(here.sum()), bool)
            ok_all[here] = hh
            named_all[here] = nm
            e["by_continent"][C] = {"alpha": ALPHAS[ai], "top1": boot(hh), "name_at": lvl, "named": boot(nm), "names_right": boot(hh[nm])}
        e["all"] = {"top1": boot(ok_all), "named": boot(named_all), "names_right": boot(ok_all[named_all])}
        best = max(range(len(ALPHAS)), key=lambda j: (hit[c][j].mean(), -ALPHAS[j]))
        e["alpha_on_all"] = ALPHAS[best] if c != "none" else 0.0
        # the page's settings from every photo at that alpha: name_at as above, offer_at the lowest level from which the three
        # likeliest held the right species nine times in ten for the photos left without a name (as tools/eval/shipped.py has it,
        # but over every kind)
        bi = 0 if c == "none" else best
        p, h = ptop[c][bi], hit[c][bi]
        name_at = None
        for tau in np.round(np.arange(0.99, 0.0049, -0.01), 2):
            m = p >= tau
            if m.sum() < 50:
                continue
            if h[m].mean() >= NAMES_RIGHT:
                name_at = float(tau)
            else:
                break
        left = ~(p >= (name_at if name_at is not None else 2))
        offer_at = None
        for tau in np.round(np.arange(0.99, 0.0049, -0.01), 2):
            m = left & (p3[c][bi] >= tau)
            if m.sum() < 30:
                continue
            if in3[c][bi][m].mean() >= 0.9:
                offer_at = float(tau)
            else:
                break
        e["settings_on_all"] = {"alpha": ALPHAS[bi], "name_at": name_at, "offer_at": offer_at,
                                "named": float((p >= name_at).mean()) if name_at is not None else 0.0,
                                "names_right": float(h[p >= name_at].mean()) if name_at is not None and (p >= name_at).any() else None,
                                "top3": float(in3[c][bi].mean())}
        e["top1_by_alpha_all_photos"] = {str(al): float(hit[c][j].mean()) for j, al in enumerate(ALPHAS)} if c != "none" else {"0": float(hit[c][0].mean())}
        out["by_condition"][c] = e
        log("%-28s top-1 %.3f  named %.3f  right %.3f" % (c, e["all"]["top1"][0], e["all"]["named"][0], e["all"]["names_right"][0] or 0))
    json.dump(out, open(os.path.join(a.out, "worldtest.json"), "w"), indent=1)
    f = lambda v: "–" if v is None or v[0] is None else "%.1f%%" % (100 * v[0])
    fi = lambda v: "–" if v is None or v[0] is None else "%.1f%% (%.1f to %.1f)" % (100 * v[0], 100 * v[1], 100 * v[2])
    L = ["# The world test of the full database", "",
         "%d photos, research grade, dated 2025 or later, about 500 a continent; %d rows; %s of the photos' species have a row. "
         "Right species first, with the prior's weight chosen for each continent on the other six. Made by tools/world/worldtest.py." % (n, S, f(out["with_a_row"])), "",
         "| Continent | Photos | " + " | ".join(conds) + " |", "|---|---:|" + "---:|" * len(conds)]
    for C in CONTINENTS + ("all",):
        cells = []
        for c in conds:
            v = out["by_condition"][c]["all"]["top1"] if C == "all" else out["by_condition"][c]["by_continent"].get(C, {}).get("top1")
            cells.append(fi(v) if C == "all" else f(v))
        L.append("| %s | %d | %s |" % (C, n if C == "all" else int((cont == C).sum()), " | ".join(cells)))
    L += ["", "Named at the level that was right 97 times in 100 on the other six continents, and the share of those names right:", "",
          "| Continent | " + " | ".join(conds) + " |", "|---|" + "---:|" * len(conds)]
    for C in CONTINENTS + ("all",):
        cells = []
        for c in conds:
            e = out["by_condition"][c]["all"] if C == "all" else out["by_condition"][c]["by_continent"].get(C, {})
            cells.append("%s named, %s right" % (f(e.get("named")), f(e.get("names_right"))))
        L.append("| %s | %s |" % (C, " | ".join(cells)))
    L += ["", "Alpha chosen on the other six continents: " + "; ".join("%s %s" % (c, ",".join("%s %g" % (C, out["by_condition"][c]["by_continent"][C]["alpha"]) for C in CONTINENTS if C in out["by_condition"][c]["by_continent"])) for c in conds if c != "none"),
          "Alpha best on every photo: " + "; ".join("%s %g" % (c, out["by_condition"][c]["alpha_on_all"]) for c in conds if c != "none"),
          "Creatures met: %d photos had three, %d fewer." % (out["creatures_met"]["photos_with_three"], out["creatures_met"]["fewer"])]
    open(os.path.join(a.out, "WORLDTEST.md"), "w").write("\n".join(L) + "\n")
    log("\n".join(L))
    log("done in %.0fs" % (time.time() - t0))


if __name__ == "__main__":
    main()
