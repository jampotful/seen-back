#!/usr/bin/env python3
"""The page's place arithmetic (placeOf in src/cam.rec.js) against tools/world/place.py, on the real place files.

Runs placeOf in Node on place.bin and zones.json (as pub/naturalist-world holds them) and compares, for a handful of time
zones and creatures met: the first guess, the posterior after each creature, and the prior over every species. It also
times the page's arithmetic. Exits 1 on a difference over 1e-9 (relative) in any number.

Usage: python3 -I tools/world/parity_place.py --ship DIR [--table DIR/table.json] [--radius 400] [--eps 0.02]
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import prior  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "..", "src", "cam.rec.js")
CASES = [("America/New_York", ["Cardinalis cardinalis", "Ardea herodias", "Anolis sagrei"]),
         ("Europe/Oslo", ["Turdus merula", "Pica pica"]),
         ("Asia/Calcutta", ["Acridotheres tristis"]),
         ("Australia/Sydney", ["Trichoglossus moluccanus", "Cracticus tibicen"]),
         ("UTC", ["Passer domesticus", "Danaus plexippus", "Columba livia"]),
         ("America/Argentina/Buenos_Aires", [])]

JS = r"""
const fs = require('fs');
const src = fs.readFileSync(process.argv[2], 'utf8');
const a = src.indexOf('  var PLACE_KEY'), b = src.indexOf('  function recognizer(o)');
let tz = 'UTC';
const localStorage = { s: {}, getItem(k) { return this.s[k] || null; }, setItem(k, v) { this.s[k] = String(v); } };
const Intl = { DateTimeFormat: () => ({ resolvedOptions: () => ({ timeZone: tz }) }) };
const placeOf = new Function('localStorage', 'Intl', 'TextDecoder', src.slice(a, b) + '\nreturn placeOf;')(localStorage, Intl, TextDecoder);
const job = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
const table = JSON.parse(fs.readFileSync(job.table, 'utf8')).species.map((r) => ({ sci: r[0], en: r[1], kind: r[2] }));
const tb = (f) => { const x = fs.readFileSync(f); return x.buffer.slice(x.byteOffset, x.byteOffset + x.byteLength); };
let t0 = Date.now();
const P = placeOf(tb(job.place), tb(job.zones), job.set, table, true);
const out = { load_ms: Date.now() - t0, cases: [] };
for (const [zone, met] of job.cases) {
  const t = P.test, rows = met.map((s) => t.row(s));
  let p = t.firstGuess(zone); const steps = [Array.from(p)];
  t0 = Date.now(); for (const r of rows) { p = t.update(p, r); steps.push(Array.from(p)); } const upd = Date.now() - t0;
  t0 = Date.now(); const L = t.logShare(p); const ls = Date.now() - t0;
  out.cases.push({ zone, met, rows, steps, share: Array.from(L), ms: { updates: upd, share: ls } });
}
fs.writeFileSync(process.argv[4], JSON.stringify(out));
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ship", required=True)
    ap.add_argument("--table", default="")
    ap.add_argument("--radius", type=float, default=400.0)
    ap.add_argument("--eps", type=float, default=0.02)
    a = ap.parse_args()
    table = a.table or os.path.join(a.ship, "table.json")
    tmp = tempfile.mkdtemp()
    job = {"table": table, "place": os.path.join(a.ship, "place.bin"), "zones": os.path.join(a.ship, "zones.json"),
           "set": {"radius_km": a.radius, "eps": a.eps}, "cases": CASES}
    jp, op, sp = os.path.join(tmp, "job.json"), os.path.join(tmp, "out.json"), os.path.join(tmp, "run.js")
    json.dump(job, open(jp, "w"))
    open(sp, "w").write(JS)
    subprocess.run(["node", "--max-old-space-size=3000", sp, os.path.abspath(SRC), jp, op], check=True)
    page = json.load(open(op))
    P = prior.load_shipped(a.ship, a.radius, a.eps)
    names = [r[0] for r in json.load(open(table, encoding="utf-8"))["species"]]
    first = {}
    for i, s in enumerate(names):
        first.setdefault(s, i)
    worst, bad = 0.0, 0
    for c in page["cases"]:
        rows = [first.get(s, -1) for s in c["met"]]
        if rows != c["rows"]:
            print("rows differ for %s: %s and %s" % (c["zone"], rows, c["rows"]))
            bad += 1
        p = P.first_guess(c["zone"])
        mine = [p]
        for r in rows:
            p = P.update(p, r)
            mine.append(p)
        ls = P.log_share(p)
        for x, y in zip(mine, c["steps"]):
            y = np.array(y)
            d = float(np.max(np.abs(x - y) / np.maximum(1e-300, np.abs(x) + 1e-12)))
            worst = max(worst, d)
        d = float(np.max(np.abs(ls - np.array(c["share"])) / np.abs(ls)))
        worst = max(worst, d)
        top = np.argsort(-ls)[:3]
        print("%-32s met %d: page %d ms for the updates, %d ms for the prior; likeliest %s" % (c["zone"], len(rows), c["ms"]["updates"], c["ms"]["share"],
                                                                                         ", ".join(names[j] for j in top)))
    print("page loaded the place files in %d ms; largest relative difference %.2e" % (page["load_ms"], worst))
    if worst > 1e-9 or bad:
        sys.exit(1)


if __name__ == "__main__":
    main()
