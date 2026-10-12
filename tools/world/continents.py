#!/usr/bin/env python3
"""A grid of half-degree cells, each given a continent, for spreading the world photos across continents.

Made from Natural Earth's countries at 1:50 million (public domain, https://www.naturalearthdata.com), whose field
CONTINENT gives each country one continent. A country's largest polygon takes the country's continent. Its other
polygons (islands and lands overseas) take the continent of the nearest cell already given one, so French Guiana is
South America and the Canary Islands are Africa. Russia east of 60 degrees east is Asia. Cells at sea take the
continent of the nearest land cell, so a reef fish is counted with the nearest coast.

Codes: AF Africa, AN Antarctica, AS Asia, EU Europe, NA North America (with Central America and the Caribbean),
OC Oceania, SA South America.

Output: one line a cell, `<cell> <TAB> <code>`, where cell = row * 720 + column, row = floor((lat + 90) * 2) and
column = floor((lon + 180) * 2), and a picture of the grid as text, one character a cell, for checking by eye.

Usage: python3 -I tools/world/continents.py --geojson ne_50m_admin_0_countries.geojson --out grid.tsv [--map map.txt]
"""
import argparse
import json
from collections import deque

import numpy as np
from matplotlib.path import Path

CODES = {"Africa": "AF", "Antarctica": "AN", "Asia": "AS", "Europe": "EU", "North America": "NA", "Oceania": "OC",
         "South America": "SA"}
ROWS, COLS = 360, 720


def rings_of(geom):
    if geom["type"] == "Polygon":
        return [geom["coordinates"]]
    if geom["type"] == "MultiPolygon":
        return geom["coordinates"]
    return []


def area(ring):
    x = np.asarray([p[0] for p in ring]); y = np.asarray([p[1] for p in ring])
    return 0.5 * abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


def cells_in(poly):
    """Indices of the cells whose centres fall inside a polygon (outer ring less its holes)."""
    outer = np.asarray(poly[0])
    lo0, la0 = outer.min(axis=0); lo1, la1 = outer.max(axis=0)
    c0, c1 = int(np.floor((lo0 + 180) * 2)), int(np.ceil((lo1 + 180) * 2))
    r0, r1 = int(np.floor((la0 + 90) * 2)), int(np.ceil((la1 + 90) * 2))
    c0, r0 = max(c0, 0), max(r0, 0); c1, r1 = min(c1, COLS), min(r1, ROWS)
    if c1 <= c0 or r1 <= r0:
        return np.zeros(0, dtype=int)
    cc, rr = np.meshgrid(np.arange(c0, c1), np.arange(r0, r1))
    pts = np.column_stack([(cc.ravel() + 0.5) / 2 - 180, (rr.ravel() + 0.5) / 2 - 90])
    inside = Path(outer).contains_points(pts)
    for hole in poly[1:]:
        inside &= ~Path(np.asarray(hole)).contains_points(pts)
    return (rr.ravel() * COLS + cc.ravel())[inside]


def nearest_labels(grid):
    """For every cell, the code of the nearest coded cell, by steps on the grid with east and west joined."""
    lab = grid.copy()
    seen = lab != ""
    q = deque(np.flatnonzero(seen).tolist())
    while q:
        i = q.popleft(); r, c = divmod(i, COLS)
        for rr, cc in ((r - 1, c), (r + 1, c), (r, (c - 1) % COLS), (r, (c + 1) % COLS)):
            if 0 <= rr < ROWS:
                j = rr * COLS + cc
                if not seen[j]:
                    seen[j] = True; lab[j] = lab[i]; q.append(j)
    return lab


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--geojson", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--map", default="")
    args = ap.parse_args()
    feats = json.load(open(args.geojson, encoding="utf-8"))["features"]
    grid = np.full(ROWS * COLS, "", dtype=object)
    later = []                                    # (cells, country) for polygons other than a country's largest
    for f in feats:
        p = f["properties"]
        cont = CODES.get(p.get("CONTINENT") or p.get("continent") or "")
        polys = rings_of(f["geometry"])
        if not polys:
            continue
        big = max(range(len(polys)), key=lambda k: area(polys[k][0]))
        for k, poly in enumerate(polys):
            cells = cells_in(poly)
            if k == big and cont:
                grid[cells] = cont
                if (p.get("ADMIN") or p.get("NAME")) == "Russia":
                    east = cells[((cells % COLS) + 0.5) / 2 - 180 > 60]
                    grid[east] = "AS"
            else:
                later.append(cells)
    land_later = np.concatenate(later) if later else np.zeros(0, dtype=int)
    land_later = land_later[grid[land_later] == ""]
    print("cells from largest polygons: %d; from other polygons: %d" % ((grid != "").sum(), len(land_later)), flush=True)
    if len(land_later):
        grid[land_later] = nearest_labels(grid)[land_later]
    land = grid != ""
    print("land cells: %d" % land.sum(), flush=True)
    grid = nearest_labels(grid)
    with open(args.out, "w", encoding="utf-8") as out:
        for i in range(ROWS * COLS):
            out.write("%d\t%s\n" % (i, grid[i]))
    counts = {c: int((grid == c).sum()) for c in CODES.values()}
    land_counts = {c: int(((grid == c) & land).sum()) for c in CODES.values()}
    print("cells by continent (all): %s" % counts)
    print("cells by continent (land): %s" % land_counts)
    if args.map:
        letter = {"AF": "f", "AN": "n", "AS": "a", "EU": "e", "NA": "m", "OC": "o", "SA": "s"}
        with open(args.map, "w", encoding="utf-8") as m:
            for r in range(ROWS - 1, -1, -4):          # every other cell, north at the top; capitals on land
                row = []
                for c in range(0, COLS, 2):
                    i = r * COLS + c
                    ch = letter.get(grid[i], "?")
                    row.append(ch.upper() if land[i] else ch)
                m.write("".join(row) + "\n")


if __name__ == "__main__":
    main()
