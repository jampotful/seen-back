#!/usr/bin/env python3
"""Check a training manifest (and inat.json) independently of the code that built it.

Usage: python3 tools/species/check_train.py <train manifest.csv> [--species data/regions/us-fl-alachua/species.json]
       [--eval data/eval/alachua-2025/manifest.csv] [--inat data/regions/us-fl-alachua/inat.json]
       [--seed seen-back/alachua-pre2025/v1] [--cap 60]

Prints one line per check and exits 1 if any check fails. What it checks: the columns; every row dated on or before
the species list's `records_through`; month equal to the date's month; ids t000001.. in order; no gbif_id twice and
none shared with the evaluation manifest; every species key in the species list with the list's name, English name
and kind of eye; at most `cap` rows a species; the order the builder promises (within a species, rows in increasing
sha256("<seed>|<gbif_id>"); through the file, each row's rank within its species never decreases; within one rank,
species by records, most first, then key), so the first rows hold every species' first photo; the address patterns.
For inat.json: entries, how many name a species differently, and the forty most recorded of those.
"""
import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict

COLUMNS = ["id", "gbif_id", "obs_url", "key", "sci", "en", "kingdom", "class", "order", "family", "eyes",
           "date", "month", "photo_url", "licence", "split"]
PHOTO = re.compile(r"^https://inaturalist-open-data\.s3\.amazonaws\.com/photos/\d+/medium\.[A-Za-z0-9]+$")
OBS = re.compile(r"^https?://(www\.)?inaturalist\.org/observations/\d+$")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("manifest")
    ap.add_argument("--species", default="data/regions/us-fl-alachua/species.json")
    ap.add_argument("--eval", default="data/eval/alachua-2025/manifest.csv")
    ap.add_argument("--inat", default="data/regions/us-fl-alachua/inat.json")
    ap.add_argument("--seed", default="seen-back/alachua-pre2025/v1")
    ap.add_argument("--cap", type=int, default=60)
    a = ap.parse_args()
    fails = []

    def check(ok, text):
        print("%s %s" % ("ok  " if ok else "FAIL", text))
        if not ok:
            fails.append(text)

    sp = json.load(open(a.species, encoding="utf-8"))
    through = sp["source"]["records_through"]
    by_key = {str(s["key"]): s for s in sp["species"]}
    with open(a.manifest, newline="", encoding="utf-8") as f:
        rd = csv.DictReader(f)
        cols = rd.fieldnames
        rows = list(rd)
    print("%d rows, %d species, records through %s" % (len(rows), len({r['key'] for r in rows}), through))
    check(cols == COLUMNS, "columns are the contract's sixteen: %s" % (cols == COLUMNS))
    late = [r for r in rows if r["date"] > through]
    check(not late, "rows dated after %s: %d (dates %s .. %s)" % (through, len(late), min(r["date"] for r in rows), max(r["date"] for r in rows)))
    badm = [r for r in rows if int(r["month"]) != int(r["date"][5:7])]
    check(not badm, "rows whose month is not their date's month: %d" % len(badm))
    check(all(r["id"] == "t%06d" % i for i, r in enumerate(rows, 1)), "ids run t000001..t%06d in order" % len(rows))
    ids = [r["gbif_id"] for r in rows]
    check(len(set(ids)) == len(ids), "gbif_id appearing twice: %d" % (len(ids) - len(set(ids))))
    ev = {r["gbif_id"] for r in csv.DictReader(open(a.eval, newline="", encoding="utf-8"))}
    both = set(ids) & ev
    check(not both, "gbif_id shared with the evaluation manifest (%d rows): %d" % (len(ev), len(both)))
    notin = [r for r in rows if r["key"] not in by_key]
    check(not notin, "rows whose species key is not in the species list: %d" % len(notin))
    mism = [r for r in rows if r["key"] in by_key and (r["sci"] != by_key[r["key"]]["sci"] or r["en"] != by_key[r["key"]]["en"]
                                                       or r["eyes"] != by_key[r["key"]]["eyes"])]
    check(not mism, "rows whose sci, en or eyes differ from the species list: %d" % len(mism))
    n_per = Counter(r["key"] for r in rows)
    check(max(n_per.values()) <= a.cap, "most rows for one species: %d (cap %d); species at the cap: %d" % (
        max(n_per.values()), a.cap, sum(1 for v in n_per.values() if v == a.cap)))
    check(all(r["split"] == "train" for r in rows), "split is train on every row")
    check(all(PHOTO.match(r["photo_url"]) for r in rows), "photo_url is a medium file in the open-data bucket on every row")
    check(all(OBS.match(r["obs_url"]) for r in rows), "obs_url is an observation on inaturalist.org on every row")
    # order
    rank_in_species, seen, prev_hash = [], Counter(), {}
    bad_within = 0
    for r in rows:
        h = hashlib.sha256(("%s|%s" % (a.seed, r["gbif_id"])).encode()).hexdigest()
        if r["key"] in prev_hash and h <= prev_hash[r["key"]]:
            bad_within += 1
        prev_hash[r["key"]] = h
        rank_in_species.append(seen[r["key"]])
        seen[r["key"]] += 1
    check(bad_within == 0, "rows out of hash order within their species: %d" % bad_within)
    drops = sum(1 for x, y in zip(rank_in_species, rank_in_species[1:]) if y < x)
    check(drops == 0, "places where the rank within species decreases through the file: %d" % drops)
    bad_tie = 0
    for (x, r1), (y, r2) in zip(zip(rank_in_species, rows), zip(rank_in_species[1:], rows[1:])):
        if x == y:
            k1 = (-by_key[r1["key"]]["n"], int(r1["key"]))
            k2 = (-by_key[r2["key"]]["n"], int(r2["key"]))
            if k2 < k1:
                bad_tie += 1
    check(bad_tie == 0, "within one rank, places not ordered by records then key: %d" % bad_tie)
    S = len(n_per)
    check(len({r["key"] for r in rows[:S]}) == S, "the first %d rows hold %d species (every species' first photo)" % (S, len({r['key'] for r in rows[:S]})))
    for cut in (1, 5, 10, 20, 30, 45, a.cap):
        print("     rows with rank below %d: %d (first rows of the file: %s)" % (
            cut, sum(1 for x in rank_in_species if x < cut), all(x < cut for x in rank_in_species[:sum(1 for x in rank_in_species if x < cut)])))
    print("     licences: %s" % dict(Counter(r["licence"] for r in rows).most_common()))
    print("     kinds of eye: %s" % dict(Counter(r["eyes"] for r in rows).most_common()))
    missing = [k for k in by_key if k not in n_per]
    print("     species in the list with no training row: %d (records for them in the list: %d)" % (
        len(missing), sum(by_key[k]["n"] for k in missing)))
    try:
        inat = json.load(open(a.inat, encoding="utf-8"))
    except (OSError, ValueError) as e:
        check(False, "inat.json readable: %s" % e)
        inat = {}
    if inat:
        differ = {k: v for k, v in inat.items() if k in by_key and v["sci"] != by_key[k]["sci"]}
        print("inat.json: %d entries (%d not in the species list); %d name the species differently; %d have an English name; "
              "%d have inat_id 0" % (len(inat), sum(1 for k in inat if k not in by_key), len(differ),
                                     sum(1 for v in inat.values() if v.get("en")), sum(1 for v in inat.values() if not v.get("inat_id"))))
        low = [v for v in inat.values() if v.get("share", 1) < 0.5]
        print("     entries whose iNaturalist name covers under half the records: %d" % len(low))
        g = [(k, v) for k, v in inat.items() if by_key.get(k, {}).get("sci") == "Gallinula chloropus"]
        check(bool(g) and g[0][1]["sci"] == "Gallinula galeata", "Gallinula chloropus maps to %s" % (g[0][1] if g else "nothing"))
        print("     the forty most recorded species named differently (records | GBIF | iNaturalist | list English | iNaturalist English | share):")
        for k in sorted(differ, key=lambda k: -by_key[k]["n"])[:40]:
            v = differ[k]
            print("     %5d | %s | %s | %s | %s | %.3f" % (by_key[k]["n"], by_key[k]["sci"], v["sci"], by_key[k]["en"], v.get("en", ""), v.get("share", 0)))
    print("%d checks failed" % len(fails))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
