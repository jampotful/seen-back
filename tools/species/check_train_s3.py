#!/usr/bin/env python3
"""Check a training manifest built from iNaturalist's open-data files, independently of the code that built it.

Usage: python3 tools/species/check_train_s3.py <train manifest.csv> [--species data/regions/us-fl-alachua/species.json]
       [--eval data/eval/alachua-2025/manifest.csv] [--seed seen-back/alachua-pre2025/s3/v1] [--cap 60]

The open-data route differs from the GBIF route in what a row can be checked against: `gbif_id` is empty, the
observation address ends in the observation's UUID, and the ranking hash is taken over the photo id. Prints one line
per check and exits 1 if any check fails. Checks: the columns; split `train` and `gbif_id` empty everywhere; every
date a real date on or before the species list's `records_through`, month equal to the date's month; ids t000001.. in
order; no photo and no observation twice; no photo id shared with the evaluation manifest; every key in the species
list with the list's name, English name, kind of eye and taxonomy; at most `cap` rows a species; the order the
builder promises (within a species, increasing sha256("<seed>|<photo id>"); through the file, each row's rank within
its species never decreases; within one rank, species by records, most first, then key); the address patterns; the
licences. Then the numbers: photos a species, list species with no photo and the records they stand for.
"""
import argparse
import csv
import datetime
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict

COLUMNS = ["id", "gbif_id", "obs_url", "key", "sci", "en", "kingdom", "class", "order", "family", "eyes",
           "date", "month", "photo_url", "licence", "split"]
PHOTO = re.compile(r"^https://inaturalist-open-data\.s3\.amazonaws\.com/photos/(\d+)/medium\.[A-Za-z0-9]+$")
OBS = re.compile(r"^https://www\.inaturalist\.org/observations/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
LICENCES = {"CC0", "CC-BY", "CC-BY-NC", "CC-BY-SA", "CC-BY-ND", "CC-BY-NC-SA", "CC-BY-NC-ND"}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("manifest")
    ap.add_argument("--species", default="data/regions/us-fl-alachua/species.json")
    ap.add_argument("--eval", default="data/eval/alachua-2025/manifest.csv")
    ap.add_argument("--seed", default="seen-back/alachua-pre2025/s3/v1")
    ap.add_argument("--cap", type=int, default=60)
    a = ap.parse_args()
    fails = []

    def check(ok, text):
        print(("ok    " if ok else "FAIL  ") + text)
        if not ok:
            fails.append(text)

    sp = json.load(open(a.species, encoding="utf-8"))
    through = sp["source"]["records_through"]
    lst = {str(s["key"]): s for s in sp["species"]}
    with open(a.manifest, encoding="utf-8", newline="") as f:
        rd = csv.reader(f)
        head = next(rd)
        rows = [dict(zip(head, r)) for r in rd]
    check(head == COLUMNS, "columns: %s" % ("as in docs/CONTRACTS.md" if head == COLUMNS else head))
    n = len(rows)
    print("      rows: %d" % n)
    check(n > 0, "the manifest has rows")
    check(all(r["split"] == "train" for r in rows), "split is train on every row")
    check(all(r["gbif_id"] == "" for r in rows), "gbif_id is empty on every row (this route has none)")

    bad_date, late, bad_month = 0, 0, 0
    for r in rows:
        try:
            d = datetime.date.fromisoformat(r["date"])
        except ValueError:
            bad_date += 1
            continue
        if r["date"] > through:
            late += 1
        if str(d.month) != r["month"]:
            bad_month += 1
    dates = sorted(r["date"] for r in rows if re.match(r"^\d{4}-\d{2}-\d{2}$", r["date"]))
    check(bad_date == 0, "every date is a real date (bad: %d)" % bad_date)
    check(late == 0, "no row dated after records_through %s (after: %d); dates run from %s to %s" % (
        through, late, dates[0] if dates else "-", dates[-1] if dates else "-"))
    check(bad_month == 0, "month equals the date's month (differs: %d)" % bad_month)
    check([r["id"] for r in rows] == ["t%06d" % i for i in range(1, n + 1)], "ids run t000001.. in order")

    pids = []
    bad_photo = 0
    for r in rows:
        m = PHOTO.match(r["photo_url"])
        if not m:
            bad_photo += 1
            pids.append("")
        else:
            pids.append(m.group(1))
    check(bad_photo == 0, "photo addresses match the open-data bucket's pattern (others: %d)" % bad_photo)
    check(sum(1 for r in rows if not OBS.match(r["obs_url"])) == 0,
          "observation addresses are inaturalist.org/observations/<UUID> (others: %d)" % sum(1 for r in rows if not OBS.match(r["obs_url"])))
    check(len(set(pids)) == n, "no photo twice (repeated: %d)" % (n - len(set(pids))))
    check(len({r["obs_url"] for r in rows}) == n, "no observation twice (repeated: %d)" % (n - len({r["obs_url"] for r in rows})))

    ev_ph, ev_obs, ev_n, ev_dates = set(), set(), 0, []
    for r in csv.DictReader(open(a.eval, encoding="utf-8")):
        ev_n += 1
        m = re.search(r"/photos/(\d+)/", r["photo_url"])
        if m:
            ev_ph.add(m.group(1))
        ev_obs.add(r["obs_url"].replace("http://", "https://"))
        ev_dates.append(r["date"])
    shared = sum(1 for p in pids if p in ev_ph)
    check(shared == 0, "no photo shared with the evaluation manifest (%d rows, %d photo ids; shared: %d)" % (ev_n, len(ev_ph), shared))
    check(sum(1 for r in rows if r["obs_url"] in ev_obs) == 0, "no observation address shared with the evaluation manifest")
    check(min(ev_dates) > (dates[-1] if dates else ""), "every evaluation photo (from %s) is later than every training photo (to %s)" % (
        min(ev_dates), dates[-1] if dates else "-"))

    wrong = Counter()
    for r in rows:
        s = lst.get(r["key"])
        if not s:
            wrong["key not in the species list"] += 1
            continue
        for col, fld in (("sci", "sci"), ("en", "en"), ("eyes", "eyes"), ("kingdom", "kingdom"), ("class", "class"),
                         ("order", "order"), ("family", "family")):
            if r[col] != (s.get(fld) or ""):
                wrong[col + " differs from the list"] += 1
    check(not wrong, "every key is in the species list with the list's name, English name, kind and taxonomy %s" % (dict(wrong) or ""))

    per = Counter(r["key"] for r in rows)
    check(max(per.values()) <= a.cap, "at most %d rows a species (largest: %d)" % (a.cap, max(per.values())))

    # order: rank within species by the photo hash; ranks never decrease; within a rank, records (most first), then key
    seen = defaultdict(list)
    order_bad = rank_bad = within_bad = 0
    prev = None
    for r, p in zip(rows, pids):
        k = r["key"]
        h = hashlib.sha256(("%s|%s" % (a.seed, p)).encode()).hexdigest()
        if seen[k] and h < seen[k][-1]:
            order_bad += 1
        rank = len(seen[k])
        seen[k].append(h)
        s = lst.get(k, {"n": 0})
        cur = (rank, -s["n"], int(k), int(p or 0))
        if prev is not None:
            if cur[0] < prev[0]:
                rank_bad += 1
            elif cur[0] == prev[0] and cur[1:] < prev[1:]:
                within_bad += 1
        prev = cur
    check(order_bad == 0, "within a species, rows in increasing sha256(seed|photo id) (out of order: %d)" % order_bad)
    check(rank_bad == 0, "through the file, each row's rank within its species never decreases (decreases: %d)" % rank_bad)
    check(within_bad == 0, "within one rank, species by records, most first, then key (out of order: %d)" % within_bad)
    lic = Counter(r["licence"] for r in rows)
    check(set(lic) <= LICENCES, "licences are Creative Commons or CC0: %s" % dict(lic.most_common()))

    in_list = len(lst)
    none = [s for k, s in lst.items() if k not in per]
    rec_all = sum(s["n"] for s in lst.values())
    rec_none = sum(s["n"] for s in none)
    print("      species with photos: %d of %d; without: %d, standing for %d of the list's %d records (%.1f%%)" % (
        len(per), in_list, len(none), rec_none, rec_all, 100.0 * rec_none / rec_all))
    for lo, hi in ((a.cap, a.cap), (30, a.cap - 1), (10, 29), (5, 9), (2, 4), (1, 1)):
        print("      %s photos: %d species" % ("%d" % lo if lo == hi else "%d to %d" % (lo, hi), sum(1 for v in per.values() if lo <= v <= hi)))
    could = sum(min(s["n"], a.cap) for s in lst.values())
    print("      rows if every list record had a photo here: %d; rows: %d (%.1f%%)" % (could, n, 100.0 * n / could))
    big = sorted(none, key=lambda s: -s["n"])[:15]
    print("      most recorded list species with no photo: " + "; ".join("%s (%s, %d)" % (s["sci"], s["en"], s["n"]) for s in big))
    short = sorted(((s["n"], per[k], s["sci"]) for k, s in lst.items() if k in per and per[k] < min(s["n"], a.cap) // 2), reverse=True)[:10]
    print("      list species with under half the photos their records allow (records, rows, name): %s" % short)
    print("      kinds of eye: %s" % dict(Counter(r["eyes"] for r in rows).most_common()))
    if fails:
        print("%d check(s) failed" % len(fails))
        sys.exit(1)
    print("all checks passed")


if __name__ == "__main__":
    main()
