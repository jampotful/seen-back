#!/usr/bin/env python3
"""Checks for tools/world/place.py (the encounter rule and the prior over species) and tools/world/zones.py (the first
guess from the time zone). Made-up records on real grids; the tz database's own tables when --tzdb gives them.

Usage: python3 -I tools/world/test_place.py [--tzdb DIR]
"""
import argparse
import math
import os
import sys

import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import place  # noqa: E402
import zones  # noqa: E402

FAILS = []


def check(ok, what):
    print(("ok    " if ok else "FAIL  ") + what, flush=True)
    if not ok:
        FAILS.append(what)


def brute_disc(g, v, radius):
    la = np.repeat(g.lat, g.nc)
    lo = np.tile(g.lon, g.nr)
    out = np.zeros(g.n)
    for i in np.nonzero(v)[0]:
        out[zones.haversine(la, lo, la[i], lo[i]) <= radius] += v[i]
    return out


def made_up(g, S=40, seed=7):
    """Species 0-9 near Gainesville, 10-19 near London, 20-29 everywhere both are, 30-38 near Sydney, 39 nowhere."""
    rng = np.random.default_rng(seed)
    places = {"gnv": (29.65, -82.32), "lon": (51.5, -0.12), "syd": (-33.87, 151.21)}
    cells, rows, counts = [], [], []
    for s in range(S - 1):
        where = ["gnv"] if s < 10 else ["lon"] if s < 20 else ["gnv", "lon"] if s < 30 else ["syd"]
        for w in where:
            la, lo = places[w]
            for _ in range(5):
                c = int(g.cell(la + rng.normal(0, 1.5), lo + rng.normal(0, 1.5)))
                cells.append(c)
                rows.append(s)
                counts.append(int(rng.integers(1, 50)))
    return place.Records(g, np.array(cells), np.array(rows), np.array(counts), S), places


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tzdb", default="")
    a = ap.parse_args()

    for res in (1.0, 2.0):
        g = place.Grid(res)
        rng = np.random.default_rng(1)
        v = np.zeros(g.n)
        v[rng.integers(0, g.n, 200)] = rng.random(200)
        v[g.cell(89.9, 10)] = 3.0                      # a cell at the pole, whose disc is whole rows
        check(np.allclose(g.disc_sum(v, 400.0), brute_disc(g, v, 400.0)), "disc sums equal brute force at %g degrees" % res)

    g = place.Grid(1.0)
    R, places = made_up(g)
    P0 = place.Place(R, radius_km=400.0, eps=0.02)
    cg, cl, cs = (int(g.cell(*places[k])) for k in ("gnv", "lon", "syd"))
    check(abs(P0.world.sum() - 1) < 1e-12 and P0.world.min() > 0, "the world guess is a distribution with no zero")
    check(np.allclose(P0.first_guess("Nowhere/Atlantis"), P0.world), "an unknown zone gives the world")

    # zones given directly: Gainesville's cell alone
    P1 = place.Place(R, zones={"America/New_York": (np.array([cg]), np.array([1.0]))}, alias={"US/Eastern": "America/New_York"})
    f = P1.first_guess("US/Eastern")
    check(abs(f[cg] - (0.98 + 0.02 * P1.world[cg])) < 1e-12, "a zone's guess is (1 - eps) its cells plus eps the world, through an alias")

    # the encounter rule
    P = P1.posterior(None, [0, 1, 2])
    check(P[cg] > 100 * P[cl] and P[cg] > 100 * P[cs], "three species of Gainesville bring the world to Gainesville")
    P = P1.posterior(None, [10, 11])
    check(P[cl] > 100 * P[cg], "two of London's bring it to London")
    Pa = P1.posterior(None, [3, 25, 12])
    Pb = P1.posterior(None, [12, 3, 25])
    check(np.allclose(Pa, Pb), "the order of meeting does not matter")
    direct = P1.world * P1.share_near(3) * P1.share_near(25) * P1.share_near(12)
    check(np.allclose(Pa, direct / direct.sum()), "the update is the product of the shares, normalized")
    Pw = P1.posterior("Europe/London", [])
    check(np.allclose(Pw, P1.world), "a zone the tables lack leaves the world")

    # the prior over species
    for P in (P1.world, P1.first_guess("America/New_York"), P1.posterior(None, [30, 31])):
        ls = P1.log_share(P)
        check(abs(np.exp(ls).sum() - 1) < 1e-9, "the prior over species sums to one")
    one = np.zeros(g.n)
    one[cl] = 1.0
    ls = P1.log_share(one)
    n = np.array([P1.local_counts(s)[cl] for s in range(R.S)])
    check(np.allclose(ls, np.log((n + 1) / (P1.N[cl] + R.S))), "at one known cell the prior is the disc's (n + 1) / (N + S)")
    check(np.argmax(ls[:20]) >= 10, "at London a species of London leads those of Gainesville")
    mix = 0.3 * one
    mix[cg] = 0.7
    lsm = P1.log_share(mix)
    lg = np.array([(P1.local_counts(s)[cg] + 1) / (P1.N[cg] + R.S) for s in range(R.S)])
    check(np.allclose(np.exp(lsm), 0.3 * np.exp(ls) + 0.7 * lg), "under two cells the prior is the mixture of theirs")

    # the true circle round a photo, from quarter-degree cells
    g4 = place.Grid(0.25)
    rng = np.random.default_rng(3)
    la = 29.65 + rng.normal(0, 3, 4000)
    lo = -82.32 + rng.normal(0, 3, 4000)
    c4 = g4.cell(la, lo)
    rw = rng.integers(0, 50, 4000)
    keys = np.unique(c4.astype(np.int64) * 64 + rw, return_counts=True)
    cc, rr, nn = keys[0] // 64, keys[0] % 64, keys[1]
    o = np.argsort(cc, kind="stable")
    ls = place.circle_share(29.65, -82.32, cc[o], rr[o], nn[o], 50, 400.0)
    cen_la = -90 + (cc // 1440 + 0.5) * 0.25
    cen_lo = -180 + (cc % 1440 + 0.5) * 0.25
    inside = zones.haversine(cen_la, cen_lo, 29.65, -82.32) <= 400.0
    n = np.bincount(rr[inside], weights=nn[inside], minlength=50)
    check(np.allclose(ls, np.log((n + 1) / (n.sum() + 50))), "the circle prior counts the quarter-degree cells within 400 km")

    if a.tzdb:
        # the first guess from the tz database's own tables, on made-up countries (boxes) and records
        names = ["NO", "SE", "US", "IN"]
        country = np.full(720 * 1440, -1, np.int16)
        g4 = place.Grid(0.25)
        LA = np.repeat(g4.lat, g4.nc)
        LO = np.tile(g4.lon, g4.nr)
        for i, (la0, la1, lo0, lo1) in enumerate([(58, 71, 5, 15), (55, 69, 15.1, 24), (25, 49, -124.7, -67), (8, 35, 68, 97)]):
            country[(LA >= la0) & (LA <= la1) & (LO >= lo0) & (LO <= lo1)] = i
        totals = np.where(country >= 0, 10.0, 0.0)
        zs, alias, notes = zones.build(a.tzdb, country, names, totals, 1.0)
        g = place.Grid(1.0)
        cla = np.repeat(g.lat, g.nc)
        clo = np.tile(g.lon, g.nr)

        def mass(z, cond):
            c, w = zs[z]
            return float(w[cond[c]].sum())
        check(abs(sum(zs["Europe/Oslo"][1]) - 1) < 1e-9, "a zone's guess sums to one")
        check(mass("Europe/Oslo", (clo >= 3) & (clo <= 16) & (cla >= 57)) > 0.999, "Europe/Oslo is Norway's, not Germany's or Sweden's")
        check(mass("America/Los_Angeles", clo < -114) > 0.7, "America/Los_Angeles lies mostly west of 114 W")
        check(mass("America/New_York", clo > -88) > 0.7, "America/New_York lies mostly east of 88 W")
        check(mass("America/New_York", (cla < 31) & (clo > -88)) > 0.02, "America/New_York leaves room for Florida")
        check(mass("America/Chicago", (clo > -100) & (clo < -84)) > 0.6, "America/Chicago lies mostly between 100 W and 84 W")
        check(alias.get("Asia/Calcutta") == "Asia/Kolkata" and alias.get("US/Eastern") == "America/New_York" and alias.get("EST5EDT") == "America/New_York",
              "old names and POSIX names find their zones")
        check(mass("Asia/Kolkata", (clo >= 67) & (clo <= 98)) > 0.99, "Asia/Kolkata is India's")
        check(all(len(c) > 0 for c, _ in zs.values()), "every zone has cells, its country's or those near its point")
    print("%d failed" % len(FAILS))
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
