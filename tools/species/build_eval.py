#!/usr/bin/env python3
"""Build data/eval/<name>/manifest.csv and SUMMARY.md: held-out evaluation photos (format: docs/CONTRACTS.md).

Pool: every iNaturalist research-grade observation on GBIF (dataset 50c9509d-...) in the region with a still
image, dated from --start (default 2025-01-01) to the latest available, identified to species or below
(it has a GBIF speciesKey; the row is labelled with that species), whose first image is in iNaturalist's
open-data bucket.

The pool is read in full, one day at a time (eventDate=YYYY-MM-DD, pages of 300), so the sample depends only on
which records exist, not on the order GBIF returns them in. Sampling: the --size rows are shared among calendar
months in proportion to each month's pool (largest-remainder rounding); within a month, records are ranked by
sha256("<seed>|<gbifID>") and the first ones taken. The same pool and seed give the same sample.

One photo per observation: the first image. photo_url is its medium-size file in the open-data bucket
(".../photos/<id>/medium.<ext>", from the GBIF media identifier ".../original.<ext>"). licence is the image's
own licence from the media record, as an SPDX-style identifier (CC-BY-NC-4.0). split is "val" when
int(sha256(gbif_id)[:8], 16) % 10 < 3, else "test". No names of people are written.

Usage: python3 tools/species/build_eval.py [--out data/eval/alachua-2025] [--species data/regions/us-fl-alachua/species.json]
"""
import argparse
import calendar
import csv
import datetime
import hashlib
import json
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402
import eyes  # noqa: E402
import names  # noqa: E402
from common import log  # noqa: E402

COLUMNS = ["id", "gbif_id", "obs_url", "key", "sci", "en", "kingdom", "class", "order", "family", "eyes",
           "date", "month", "photo_url", "licence", "split"]
PHOTO = re.compile(r"^https?://inaturalist-open-data\.s3\.amazonaws\.com/photos/(\d+)/original\.([A-Za-z0-9]+)$")
OBS = re.compile(r"^https?://(www\.)?inaturalist\.org/observations/(\d+)$")
BBOX = {"decimalLatitude": "29.42,29.95", "decimalLongitude": "-82.66,-82.05"}


def split_of(gbif_id):
    return "val" if int(hashlib.sha256(str(gbif_id).encode()).hexdigest()[:8], 16) % 10 < 3 else "test"


def rank_of(seed, gbif_id):
    return hashlib.sha256(("%s|%s" % (seed, gbif_id)).encode()).hexdigest()


def months(start, end):
    y, m = start.year, start.month
    while (y, m) <= (end.year, end.month):
        yield y, m
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def compact(x):
    """The fields the manifest needs from one occurrence record (no names of people)."""
    media = [md for md in x.get("media", []) if md.get("type") == "StillImage"]
    first = media[0] if media else {}
    obs = x.get("references") or x.get("occurrenceID") or ""
    if not OBS.match(obs) and x.get("catalogNumber"):
        obs = "https://www.inaturalist.org/observations/%s" % x["catalogNumber"]
    return {"gbif_id": x.get("key") or x.get("gbifID"), "obs_url": obs, "speciesKey": x.get("speciesKey"),
            "taxonRank": x.get("taxonRank"), "date": (x.get("eventDate") or "")[:10], "year": x.get("year"),
            "month": x.get("month"), "photo": first.get("identifier") or "", "photo_licence": first.get("license") or "",
            "rec_licence": x.get("license") or "", "n_media": len(media),
            "gid2": ((x.get("gadm") or {}).get("level2") or {}).get("gid")}


def fetch_day(base, day, tries=3):
    """All records of one day. Pages of 300; a day whose pages do not add up to its count is read again."""
    for attempt in range(1, tries + 1):
        recs, off, cnt = {}, 0, None
        while True:
            r = common.get_json("/occurrence/search", dict(base, eventDate=day, limit=300, offset=off))
            cnt = r.get("count", 0)
            res = r.get("results", [])
            for x in res:
                c = compact(x)
                recs[c["gbif_id"]] = c
            off += len(res)
            if not res or off >= cnt or r.get("endOfRecords"):
                break
        if len(recs) == cnt:
            return day, cnt, list(recs.values()), attempt
    return day, cnt, list(recs.values()), -attempt


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default="data/eval/alachua-2025")
    ap.add_argument("--species", default="data/regions/us-fl-alachua/species.json")
    ap.add_argument("--gadm", default="USA.10.1_1")
    ap.add_argument("--bbox", action="store_true")
    ap.add_argument("--start", default="2025-01-01")
    ap.add_argument("--end", default="", help="last date (default: today, UTC)")
    ap.add_argument("--size", type=int, default=6000)
    ap.add_argument("--seed", default="seen-back/alachua-2025/v1")
    ap.add_argument("--cache", default="work/cache")
    ap.add_argument("--diag", default="")
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()
    t0 = time.time()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    diag = Path(args.diag) if args.diag else None
    if diag:
        diag.mkdir(parents=True, exist_ok=True)
    cache = common.JsonCache(Path(args.cache) / "gbif")
    start = datetime.date.fromisoformat(args.start)
    end = datetime.date.fromisoformat(args.end) if args.end else datetime.datetime.now(datetime.timezone.utc).date()
    place = dict(BBOX) if args.bbox else {"gadmGid": args.gadm}
    base = dict(place, datasetKey=common.INAT_DATASET, mediaType="StillImage")
    problems, checks = [], []

    sp = json.loads(Path(args.species).read_text(encoding="utf-8"))
    by_key = {str(s["key"]): s for s in sp["species"]}
    through = sp["source"]["records_through"]
    if args.start <= through or args.start <= "2024-05-01":
        common.die("--start must be later than the species list's records_through (%s) and 2024-05-01" % through)

    log("== pool: records with a still image, %s to %s, %s" % (start, end, place))
    mlist = list(months(start, end))
    mcount = dict(zip(mlist, common.pmap(lambda ym: common.count(dict(base, year=ym[0], month=ym[1])), mlist, workers=args.workers)))
    for ym in mlist:
        log("  %d-%02d: %d records" % (ym[0], ym[1], mcount[ym]))
    days = []
    for (y, m), c in mcount.items():
        if c:
            for d in range(1, calendar.monthrange(y, m)[1] + 1):
                dd = datetime.date(y, m, d)
                if start <= dd <= end:
                    days.append(dd.isoformat())
    log("== reading %d days" % len(days))
    got = common.pmap(lambda d: fetch_day(base, d), days, workers=args.workers, desc="days", every=60)
    pool, day_cnt = {}, Counter()
    dup_ids, short_days, retried = 0, [], 0
    for day, cnt, recs, attempt in got:
        day_cnt[day[:7]] += cnt
        if attempt < 0:
            short_days.append((day, cnt, len(recs)))
        elif attempt > 1:
            retried += 1
        for c in recs:
            if c["gbif_id"] in pool:
                dup_ids += 1
            pool[c["gbif_id"]] = c
    if diag:
        sample = common.get_json("/occurrence/search", dict(base, eventDate=days[len(days) // 2], limit=5))
        (diag / "eval_occurrence_sample.json").write_text(json.dumps([common.scrub_occurrence(x) for x in sample.get("results", [])], indent=1))
    month_mismatch = {"%d-%02d" % ym: (mcount[ym], day_cnt["%d-%02d" % ym]) for ym in mlist if mcount[ym] != day_cnt["%d-%02d" % ym]}
    line = ("records read: %d unique (%d seen twice); days re-read: %d; days still short: %d %s; months whose day "
            "counts differ from the month count: %s" % (len(pool), dup_ids, retried, len(short_days), short_days[:5], month_mismatch or "none"))
    log(line)
    checks.append(line)
    if month_mismatch:
        problems.append("day counts do not add up to month counts: %s" % month_mismatch)

    log("== eligibility")
    why = Counter()
    hosts = Counter()
    eligible = defaultdict(list)
    date_off = 0
    for c in pool.values():
        hosts[re.sub(r"^https?://([^/]+)/.*$", r"\1", c["photo"]) if c["photo"] else "(none)"] += 1
        if c["gid2"] and not args.bbox and c["gid2"] != args.gadm:
            why["outside the GADM area"] += 1
            continue
        if not c["speciesKey"]:
            why["not identified to a GBIF species (rank %s)" % c["taxonRank"]] += 1
            continue
        if not c["photo"]:
            why["no still image"] += 1
            continue
        if not PHOTO.match(c["photo"]):
            why["first image not in the open-data bucket"] += 1
            continue
        if not c["date"] or not (args.start <= c["date"] <= end.isoformat()) or not c["month"]:
            why["date outside the window"] += 1
            continue
        if not OBS.match(c["obs_url"] or ""):
            why["no observation address"] += 1
            continue
        if c["date"][:7] != "%d-%02d" % (c["year"], c["month"]):
            date_off += 1
        eligible["%d-%02d" % (c["year"], c["month"])].append(c)
    E = sum(len(v) for v in eligible.values())
    line = "eligible: %d of %d; left out: %s; photo hosts: %s; date/month disagreements: %d" % (
        E, len(pool), dict(why), dict(hosts), date_off)
    log(line)
    checks.append(line)

    log("== sample")
    size = min(args.size, E)
    keys = sorted(eligible)
    exact = {k: size * len(eligible[k]) / E for k in keys}
    quota = {k: int(exact[k]) for k in keys}
    for k in sorted(keys, key=lambda k: (-(exact[k] - quota[k]), k))[: size - sum(quota.values())]:
        quota[k] += 1
    chosen = []
    for k in keys:
        ranked = sorted(eligible[k], key=lambda c: rank_of(args.seed, c["gbif_id"]))
        chosen.extend(ranked[: quota[k]])
    log("  %d rows; quota by month: %s" % (len(chosen), quota))

    log("== taxonomy and names")
    need = sorted({str(c["speciesKey"]) for c in chosen})
    info = dict(zip(need, common.pmap(lambda k: common.species_info(k, cache), need, workers=args.workers, desc="species API")))
    new = [k for k in need if k not in by_key]
    en = {k: by_key[k]["en"] for k in need if k in by_key}
    if new:
        wanted = {}
        for k in new:
            nm = info[k].get("canonicalName") or info[k].get("species")
            if nm:
                wanted.setdefault(nm, info[k].get("kingdom"))
        try:
            arch = names.ensure_archive(args.cache)
            inat, rep = names.english_names(arch, wanted)
            log("  iNaturalist names for species not in the list: %s" % rep)
        except Exception as e:
            inat = {}
            problems.append("iNaturalist archive could not be read: %s" % e)
        rest = [k for k in new if (info[k].get("canonicalName") or info[k].get("species")) not in inat]
        gb = common.pmap(lambda k: common.choose_gbif_english(common.gbif_vernacular(k, cache)), rest, workers=args.workers)
        gmap = dict(zip(rest, gb))
        for k in new:
            nm = info[k].get("canonicalName") or info[k].get("species")
            en[k] = inat.get(nm) or gmap.get(k) or ""

    rows = []
    for c in sorted(chosen, key=lambda c: (c["date"], int(c["gbif_id"]))):
        k = str(c["speciesKey"])
        i = info[k]
        tax = {f: (i.get(f) or "") for f in ("kingdom", "phylum", "class", "order", "family", "genus")}
        m = PHOTO.match(c["photo"])
        rows.append({
            "gbif_id": c["gbif_id"], "obs_url": c["obs_url"], "key": int(k) if k.isdigit() else k,
            "sci": i.get("canonicalName") or i.get("species") or "", "en": en.get(k, ""),
            "kingdom": tax["kingdom"], "class": tax["class"], "order": tax["order"], "family": tax["family"],
            "eyes": eyes.kind_of_record(tax), "date": c["date"], "month": int(c["date"][5:7]),
            "photo_url": "https://inaturalist-open-data.s3.amazonaws.com/photos/%s/medium.%s" % (m.group(1), m.group(2)),
            "licence": common.licence_id(c["photo_licence"] or c["rec_licence"]), "split": split_of(c["gbif_id"]),
            "_licence_from_record": not c["photo_licence"],
        })
    for i, r in enumerate(rows, 1):
        r["id"] = "e%06d" % i
    bad_dates = [r for r in rows if r["date"] <= through or r["date"] <= "2024-05-01"]
    if bad_dates:
        problems.append("%d rows dated on or before %s" % (len(bad_dates), through))
    if len({r["gbif_id"] for r in rows}) != len(rows):
        problems.append("duplicate gbif_id in the manifest")
    with open(out / "manifest.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(COLUMNS)
        for r in rows:
            w.writerow([r[c] for c in COLUMNS])
    log("  wrote %s: %d rows" % (out / "manifest.csv", len(rows)))
    lic_from_rec = sum(1 for r in rows if r["_licence_from_record"])
    if lic_from_rec:
        checks.append("%d rows took the record's licence because the image carried none" % lic_from_rec)
    (out / "SUMMARY.md").write_text(make_summary(rows, by_key, sp, quota, eligible, pool, why, checks, problems, args, end), encoding="utf-8")
    log("  wrote %s; GBIF requests %s; %.0fs" % (out / "SUMMARY.md", common.stats(), time.time() - t0))
    if problems:
        log("PROBLEMS:\n  " + "\n  ".join(problems))
        sys.exit(2)
    log("all checks passed")


def pct(a, b):
    return "%.1f%%" % (100.0 * a / b) if b else "n/a"


def table(L, title, counter, total, order=None):
    L.append("| %s | Rows | Share |" % title)
    L.append("|---|---:|---:|")
    keys = order if order else [k for k, _ in counter.most_common()]
    for k in keys:
        if counter.get(k):
            L.append("| %s | %d | %s |" % (k if k != "" else "(none)", counter[k], pct(counter[k], total)))
    L.append("")


def make_summary(rows, by_key, sp, quota, eligible, pool, why, checks, problems, args, end):
    N = len(rows)
    L = ["# Evaluation photos: %s" % Path(args.out).name, ""]
    L.append("Made by `tools/species/build_eval.py` on %s from GBIF (iNaturalist research-grade observations, dataset `%s`), "
             "region %s, observations dated %s to %s, seed `%s`. Rerun it to check any number here." % (
                 datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"), common.INAT_DATASET,
                 ("bounding box %s" % BBOX) if args.bbox else "GADM area `%s`" % args.gadm, args.start, end, args.seed))
    L.append("")
    L.append("Every row is dated after %s (the species list's `records_through`) and after 2024-05-01 (the GBIF snapshot "
             "behind BioCLIP 2's training data)." % sp["source"]["records_through"])
    L.append("")
    L.append("## Size")
    L.append("")
    sp_rows = Counter(r["split"] for r in rows)
    L.append("- Rows: **%d** (val %d, test %d), from a pool of %d eligible observations (%d read)." % (
        N, sp_rows["val"], sp_rows["test"], sum(len(v) for v in eligible.values()), len(pool)))
    L.append("- Distinct species: %d (val %d, test %d)." % (
        len({r["key"] for r in rows}), len({r["key"] for r in rows if r["split"] == "val"}),
        len({r["key"] for r in rows if r["split"] == "test"})))
    L.append("- Left out of the pool: %s." % (", ".join("%s: %d" % kv for kv in why.most_common()) or "nothing"))
    L.append("")
    L.append("## Coverage by the species list")
    L.append("")
    L.append("The share of rows whose species a recognizer restricted to the list could name at all: the ceiling of its accuracy.")
    L.append("")
    L.append("| Species list restricted to | Rows covered | Share | Test rows covered | Share of test |")
    L.append("|---|---:|---:|---:|---:|")
    test = [r for r in rows if r["split"] == "test"]
    for t, label in ((1, "all species (n at least 1)"), (3, "n at least 3"), (10, "n at least 10")):
        cov = sum(1 for r in rows if str(r["key"]) in by_key and by_key[str(r["key"])]["n"] >= t)
        cov_t = sum(1 for r in test if str(r["key"]) in by_key and by_key[str(r["key"])]["n"] >= t)
        L.append("| %s | %d | %s | %d | %s |" % (label, cov, pct(cov, N), cov_t, pct(cov_t, len(test))))
    L.append("")
    L.append("## By kind of eye")
    L.append("")
    table(L, "Kind", Counter(r["eyes"] for r in rows), N, order=list(eyes.KINDS))
    L.append("## By class")
    L.append("")
    table(L, "Class", Counter("%s / %s" % (r["kingdom"], r["class"] or "(none)") for r in rows), N)
    L.append("## By month")
    L.append("")
    L.append("| Month | Pool | Rows |")
    L.append("|---|---:|---:|")
    for k in sorted(eligible):
        L.append("| %s | %d | %d |" % (k, len(eligible[k]), quota.get(k, 0)))
    L.append("")
    L.append("## By licence (of the image)")
    L.append("")
    table(L, "Licence", Counter(r["licence"] for r in rows), N)
    L.append("## English names")
    L.append("")
    L.append("- Rows with an English name: %d (%s)." % (sum(1 for r in rows if r["en"]), pct(sum(1 for r in rows if r["en"]), N)))
    L.append("")
    L.append("## Checks")
    L.append("")
    for c in checks:
        L.append("    " + c)
    L.append("")
    L.append("Problems found: %s" % ("none" if not problems else ""))
    for p in problems:
        L.append("- %s" % p)
    L.append("")
    return "\n".join(L)


if __name__ == "__main__":
    main()
