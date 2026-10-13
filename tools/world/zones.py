#!/usr/bin/env python3
"""The first guess of where a phone is, from its time zone alone (docs/tracks/worlddb.md, step 2).

The page reads the phone's time zone (an IANA name such as "America/New_York") and nothing else about the place. This
module turns a zone into a distribution over the cells of a world grid, from public-domain data only:

  - the tz database's zone.tab gives each zone its country and a point (one line a country and zone, so that
    "Europe/Oslo" is Norway's alone, where zone1970.tab would give it Germany, Denmark, Sweden and Svalbard);
    its `backward` file turns old and alternative names ("Asia/Calcutta", "US/Eastern") into current ones;
  - Natural Earth's countries (tools/world/grid.py rasterizes them) give each cell its countries; a cell at sea
    takes the countries of land cells next to it, so that a record made from a boat counts for the country;
  - the zone's standard offset from UTC (Python's zoneinfo) says, inside a country of several zones, which band of
    longitude the zone holds: a cell's solar time is its longitude / 15 hours, and the clocks of such countries run
    about a quarter of an hour ahead of it (the boundaries of the United States' four zones fall within about two
    degrees of the meridians this puts them on). A zone's share of a cell falls off as a normal curve in the gap
    between its offset and the cell's solar time plus 0.25 h (0.5 h a standard deviation), and mildly with distance
    from the zone's point (a factor e every 1,500 km), and never goes below a fiftieth of an even share, so that no
    cell of the country is ruled out.

  P(cell | zone) is proportional to P(zone | cell) times the cell's research-grade records plus one (people record
  where people are), over the cells of the zone's country. A zone the tables do not know gives nothing: the caller
  falls back to the world.

No timezone boundaries are used: the polygons that exist (timezone-boundary-builder) are under the ODbL, and serve only
to label the test photos (tools/world/grid.py).

Usage as a script: python3 -I tools/world/zones.py --tzdb DIR --place DIR --res 1 --out zones.json
  (DIR of --tzdb holds zone.tab and backward; --place holds country025.npy, countries.json and totals025.npy)
"""
import argparse
import datetime
import json
import math
import os
import zoneinfo

import numpy as np

R_EARTH = 6371.0088
POSIX = {"EST5EDT": "America/New_York", "CST6CDT": "America/Chicago", "MST7MDT": "America/Denver", "PST8PDT": "America/Los_Angeles",
         "EST": "America/Panama", "MST": "America/Phoenix", "HST": "Pacific/Honolulu"}
LEAD_H, STEP_H, STEP_KM, FLOOR = 0.25, 0.5, 1500.0, 0.02


def coord(s):
    """ISO 6709 as zone.tab writes it: +DDMM+DDDMM or +DDMMSS+DDDMMSS."""
    i = max(s.rfind("+"), s.rfind("-"))
    la, lo = s[:i], s[i:]

    def one(x, deg):
        sign = -1 if x[0] == "-" else 1
        x = x[1:]
        d, m, sec = int(x[:deg]), int(x[deg:deg + 2]), int(x[deg + 2:deg + 4] or 0)
        return sign * (d + m / 60 + sec / 3600)
    return one(la, 2), one(lo, 3)


def read_tab(path):
    out = []
    for line in open(path, encoding="utf-8"):
        if not line.strip() or line.startswith("#"):
            continue
        p = line.rstrip("\n").split("\t")
        la, lo = coord(p[1])
        out.append((p[0].split(","), la, lo, p[2]))
    return out


def read_links(path):
    links = {}
    for line in open(path, encoding="utf-8"):
        p = line.split("#")[0].split()
        if len(p) >= 3 and p[0] == "Link":
            links[p[2]] = p[1]
    return links


def std_offset(zone, year=2026):
    """The zone's standard offset in hours (the smaller of mid-January's and mid-July's), or None."""
    try:
        z = zoneinfo.ZoneInfo(zone)
    except Exception:
        return None
    o = [datetime.datetime(year, m, 15, 12, tzinfo=z).utcoffset().total_seconds() / 3600 for m in (1, 7)]
    return min(o)


def resolve(name, known, links):
    """The zone.tab name a phone's zone name stands for, or None."""
    seen = set()
    while name and name not in known and name not in seen:
        seen.add(name)
        name = POSIX.get(name) or links.get(name)
    return name if name in known else None


def coarse_countries(country025, ncountries, res):
    """For each cell of a grid of `res` degrees, a boolean matrix (cells, countries): which countries its quarter-degree
    cells hold. A cell at sea takes the countries of the land cells round it."""
    f = int(round(res / 0.25))
    nr, nc = 720 // f, 1440 // f
    c = country025.reshape(720, 1440)
    M = np.zeros((nr * nc, ncountries), bool)
    rr, cc = np.nonzero(c >= 0)
    M[(rr // f) * nc + (cc // f), c[rr, cc]] = True
    land = M.any(1).reshape(nr, nc)
    G = M.reshape(nr, nc, ncountries)
    near = np.zeros_like(G)
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            sh = np.roll(G, dc, axis=1)
            if dr:
                sh = np.roll(sh, dr, axis=0)
                if dr > 0:
                    sh[:dr] = False
                else:
                    sh[dr:] = False
            near |= sh
    sea = ~land
    G = G | (near & sea[:, :, None])
    return G.reshape(nr * nc, ncountries)


def haversine(la1, lo1, la2, lo2):
    p1, p2 = np.radians(la1), np.radians(la2)
    dp, dl = p2 - p1, np.radians(lo2 - lo1)
    h = np.sin(dp / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(dl / 2) ** 2
    return 2 * R_EARTH * np.arcsin(np.sqrt(np.minimum(1, h)))


def build(tzdb, country025, countries, totals025, res, keep=1e-7):
    """{zone: (cells int32 array, weights float64 array summing to 1)}, the alias map, and notes."""
    tab = read_tab(os.path.join(tzdb, "zone.tab"))
    links = read_links(os.path.join(tzdb, "backward"))
    f = int(round(res / 0.25))
    nr, nc = 720 // f, 1440 // f
    t = np.asarray(totals025, np.float64).reshape(720, 1440)
    T = t.reshape(nr, f, nc, f).sum((1, 3)).reshape(-1)
    M = coarse_countries(np.asarray(country025), len(countries), res)
    cidx = {c: i for i, c in enumerate(countries)}
    lat = -90 + (np.arange(nr) + 0.5) * res
    lon = -180 + (np.arange(nc) + 0.5) * res
    LA, LO = np.meshgrid(lat, lon, indexing="ij")
    LA, LO = LA.reshape(-1), LO.reshape(-1)
    by_country = {}
    for cs, la, lo, z in tab:
        by_country.setdefault(cs[0], []).append((z, la, lo, std_offset(z)))
    out, notes = {}, {"no_cells_in_country": [], "no_offset": []}
    for cc_, zs in by_country.items():
        ci = cidx.get(cc_)
        cells = np.nonzero(M[:, ci])[0] if ci is not None else np.zeros(0, np.int64)
        if len(zs) == 1 or len(cells) == 0:
            share = {zs[0][0]: np.ones(len(cells))} if len(zs) == 1 else {}
        else:
            sc = []
            for z, la, lo, off in zs:
                if off is None:
                    notes["no_offset"].append(z)
                    off = LO[cells] / 15 + LEAD_H
                gap = off - LO[cells] / 15 - LEAD_H
                sc.append(-(gap / STEP_H) ** 2 / 2 - haversine(LA[cells], LO[cells], la, lo) / STEP_KM)
            sc = np.array(sc)
            sc -= sc.max(0, keepdims=True)
            p = np.exp(sc)
            p /= p.sum(0, keepdims=True)
            p = (1 - FLOOR) * p + FLOOR / len(zs)
            share = {zs[k][0]: p[k] for k in range(len(zs))}
        for z, la, lo, off in zs:
            if z in share and len(cells):
                w = share[z] * (T[cells] + 1)
                cz = cells
            else:                                      # no land of its own on this grid: the cells within 300 km of its point
                notes["no_cells_in_country"].append(z)
                d = haversine(LA, LO, la, lo)
                cz = np.nonzero(d <= max(300.0, res * 111.2))[0]
                if len(cz) == 0:
                    cz = np.array([int(np.argmin(d))])
                w = (T[cz] + 1) * np.exp(-haversine(LA[cz], LO[cz], la, lo) / 300.0)
            w = w / w.sum()
            k = w >= keep * w.max()
            out[z] = (cz[k].astype(np.int32), w[k] / w[k].sum())
    alias = {}
    for name in set(links) | set(POSIX):
        r = resolve(name, out, links)
        if r and r != name:
            alias[name] = r
    return out, alias, notes


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--tzdb", required=True)
    ap.add_argument("--place", required=True)
    ap.add_argument("--res", type=float, default=1.0)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    country = np.load(os.path.join(a.place, "country025.npy"))
    countries = json.load(open(os.path.join(a.place, "countries.json")))
    totals = np.load(os.path.join(a.place, "totals025.npy"))
    zones, alias, notes = build(a.tzdb, country, countries, totals, a.res)
    json.dump({"res": a.res, "zones": {z: [c.tolist(), [round(float(x), 7) for x in w]] for z, (c, w) in sorted(zones.items())},
               "alias": dict(sorted(alias.items())), "notes": notes}, open(a.out, "w"))
    print("zones %d, aliases %d, cells in all %d; %s" % (len(zones), len(alias), sum(len(c) for c, _ in zones.values()), json.dumps(notes)))


if __name__ == "__main__":
    main()
