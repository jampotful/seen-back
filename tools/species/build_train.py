#!/usr/bin/env python3
"""Build data/train/<name>/manifest.csv, its SUMMARY.md, and data/regions/<region>/inat.json (formats: docs/CONTRACTS.md).

Training photos come from the same records the species list counts: iNaturalist research-grade observations on
GBIF in the region, with a still image, dated through the list's `records_through`. Nothing here is later than
that date, so no training photo can be an evaluation photo.

The pool is read in full, one calendar month at a time (pages of 300), and a month whose pages do not add up to
its count is read again. For each species up to --cap photos are taken (one per observation, the first image),
ranked by sha256("<seed>|<gbifID>"), so the same pool and seed give the same choice. Rows are written in order of
that rank and then of species, so the first rows of the file hold every species' first photo: any prefix of the
file is a fair, smaller training set.

inat.json: for each GBIF species key, the iNaturalist species most often attached to its records here, with
iNaturalist's preferred English name for a person in Florida. GBIF files some species under names iNaturalist
does not use; the name shown to a person should be iNaturalist's.

No names of people are written.

Usage: python3 tools/species/build_train.py [--out data/train/alachua-pre2025] [--cap 60]
"""
import argparse
import csv
import datetime
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402
import names  # noqa: E402
from build_eval import COLUMNS, OBS, PHOTO, compact, rank_of  # noqa: E402
from common import log  # noqa: E402

INFRA = ("subspecies", "variety", "form", "infrahybrid")


def fetch_month(base, y, m, tries=3):
    """All records of one calendar month. Pages of 300; a month whose pages do not add up is read again."""
    for attempt in range(1, tries + 1):
        recs, off, cnt = {}, 0, None
        while True:
            r = common.get_json("/occurrence/search", dict(base, year=y, month=m, limit=300, offset=off))
            cnt = r.get("count", 0)
            res = r.get("results", [])
            for x in res:
                c = compact(x)
                recs[c["gbif_id"]] = c
            off += len(res)
            if not res or off >= cnt or r.get("endOfRecords"):
                break
        if len(recs) == cnt:
            return (y, m), cnt, list(recs.values()), attempt
    return (y, m), cnt, list(recs.values()), -attempt


def pct(a, b):
    return "%.1f%%" % (100.0 * a / b) if b else "n/a"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default="data/train/alachua-pre2025")
    ap.add_argument("--region-dir", default="data/regions/us-fl-alachua")
    ap.add_argument("--eval", default="data/eval/alachua-2025/manifest.csv")
    ap.add_argument("--gadm", default="USA.10.1_1")
    ap.add_argument("--cap", type=int, default=60)
    ap.add_argument("--seed", default="seen-back/alachua-pre2025/v1")
    ap.add_argument("--cache", default="work/cache")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--place", type=int, default=21, help="iNaturalist place for preferred names (21 is Florida)")
    args = ap.parse_args()
    t0 = time.time()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    region = Path(args.region_dir)
    sp = json.loads((region / "species.json").read_text(encoding="utf-8"))
    by_key = {str(s["key"]): s for s in sp["species"]}
    through = sp["source"]["records_through"]
    last = datetime.date.fromisoformat(through)
    base = {"gadmGid": args.gadm, "datasetKey": common.INAT_DATASET, "mediaType": "StillImage"}
    problems, checks = [], []

    log("== pool: records with a still image through %s" % through)
    ycount, total, _, _ = common.facet_all(dict(base, eventDate="1800-01-01,%s" % through), field="year", page=300)
    years = sorted(int(y) for y in ycount if int(ycount[y]) > 0)
    log("  %d records in years %s..%s" % (total, years[0], years[-1]))
    yms = [(y, m) for y in years for m in range(1, 13) if (y, m) <= (last.year, last.month)]
    got = common.pmap(lambda ym: fetch_month(base, ym[0], ym[1]), yms, workers=args.workers, desc="months", every=20)
    pool, short, dup = {}, [], 0
    for ym, cnt, recs, attempt in got:
        if attempt < 0:
            short.append((ym, cnt, len(recs)))
        for c in recs:
            if c["gbif_id"] in pool:
                dup += 1
            pool[c["gbif_id"]] = c
    pool = {k: c for k, c in pool.items() if c["date"] and c["date"] <= through}
    line = "records read: %d unique (%d seen twice), against %d counted by GBIF; months still short: %d %s" % (
        len(pool), dup, total, len(short), short[:5])
    log(line)
    checks.append(line)
    if short:
        problems.append("%d months could not be read in full" % len(short))
    if abs(len(pool) - total) > max(50, total // 200):
        problems.append("read %d records but GBIF counts %d" % (len(pool), total))

    log("== eligibility")
    why = Counter()
    per = defaultdict(list)
    inat_of = defaultdict(Counter)          # GBIF species key -> iNaturalist taxon ids on its records
    for c in pool.values():
        k = str(c["speciesKey"] or "")
        if k and c.get("taxonID"):
            inat_of[k][str(c["taxonID"])] += 1
        if c["gid2"] and c["gid2"] != args.gadm:
            why["outside the GADM area"] += 1
        elif not k:
            why["not identified to a GBIF species"] += 1
        elif k not in by_key:
            why["species not in the species list"] += 1
        elif not c["photo"] or not PHOTO.match(c["photo"]):
            why["first image missing or not in the open-data bucket"] += 1
        elif not OBS.match(c["obs_url"] or ""):
            why["no observation address"] += 1
        else:
            per[k].append(c)
    E = sum(len(v) for v in per.values())
    line = "eligible: %d of %d records, %d species; left out: %s" % (E, len(pool), len(per), dict(why))
    log(line)
    checks.append(line)

    log("== choose up to %d a species" % args.cap)
    chosen = []
    for k, recs in per.items():
        ranked = sorted(recs, key=lambda c: rank_of(args.seed, c["gbif_id"]))[: args.cap]
        for r, c in enumerate(ranked):
            chosen.append((r, -by_key[k]["n"], int(k), c))
    chosen.sort(key=lambda t: t[:3] + (int(t[3]["gbif_id"]),))
    eval_ids = set()
    if Path(args.eval).exists():
        eval_ids = {r["gbif_id"] for r in csv.DictReader(open(args.eval, encoding="utf-8"))}
    rows = []
    for i, (rank, _, key, c) in enumerate(chosen, 1):
        s = by_key[str(key)]
        m = PHOTO.match(c["photo"])
        rows.append({
            "id": "t%06d" % i, "gbif_id": c["gbif_id"], "obs_url": c["obs_url"], "key": key, "sci": s["sci"], "en": s["en"],
            "kingdom": s.get("kingdom", ""), "class": s.get("class", ""), "order": s.get("order", ""), "family": s.get("family", ""),
            "eyes": s["eyes"], "date": c["date"], "month": int(c["date"][5:7]),
            "photo_url": "https://inaturalist-open-data.s3.amazonaws.com/photos/%s/medium.%s" % (m.group(1), m.group(2)),
            "licence": common.licence_id(c["photo_licence"] or c["rec_licence"]), "split": "train", "_rank": rank,
        })
    late = [r for r in rows if r["date"] > through]
    if late:
        problems.append("%d rows dated after %s" % (len(late), through))
    both = [r for r in rows if str(r["gbif_id"]) in eval_ids]
    if both:
        problems.append("%d rows are also in the evaluation manifest" % len(both))
    if len({r["gbif_id"] for r in rows}) != len(rows):
        problems.append("duplicate gbif_id in the manifest")
    checks.append("rows dated after %s: %d; rows shared with the evaluation manifest (%d rows): %d" % (through, len(late), len(eval_ids), len(both)))
    with open(out / "manifest.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(COLUMNS)
        for r in rows:
            w.writerow([r[c] for c in COLUMNS])
    log("  wrote %s: %d rows" % (out / "manifest.csv", len(rows)))

    log("== iNaturalist's names for each GBIF species")
    inat = {}
    try:
        arch = names.ensure_archive(args.cache)
        ids = {i for cnt in inat_of.values() for i in cnt}
        tax = names.taxa_by_id(arch, ids)                      # id -> (scientific name, rank)
        dom = {}
        for k, cnt in inat_of.items():
            if k not in by_key:
                continue
            binom = Counter()
            for tid, n in cnt.items():
                t = tax.get(tid)
                if not t or not t[0]:
                    continue
                nm, rank = t
                binom[" ".join(nm.split()[:2]) if rank in INFRA else nm] += n
            if binom:
                top, n = binom.most_common(1)[0]
                dom[k] = (top, n / float(sum(cnt.values())), sum(cnt.values()))
        wanted = {}
        for k, (nm, _, _) in dom.items():
            wanted.setdefault(nm, by_key[k].get("kingdom"))
        _, rep, taxa = names.english_names(arch, wanted)       # scientific name -> iNaturalist species taxon (id, ranks)
        place = args.place if names.check_place(args.place) else 1
        api = names.api_preferred(sorted({t["id"] for t in taxa.values()}, key=lambda x: int(x) if str(x).isdigit() else 0), place_id=place)
        differ = 0
        for k, (nm, share, n) in dom.items():
            t = taxa.get(nm)
            tid = str(t["id"]) if t else ""
            en = api.get(tid, "") if tid else ""
            inat[k] = {"inat_id": int(tid) if tid.isdigit() else 0, "sci": nm, "en": en, "share": round(share, 3), "n": n}
            if nm != by_key[k]["sci"]:
                differ += 1
        line = "iNaturalist names: %d of %d species; %d carry a different scientific name from GBIF's; %d have an English name; place %s; archive report %s" % (
            len(inat), len(by_key), differ, sum(1 for v in inat.values() if v["en"]), place, {k: v for k, v in rep.items() if not isinstance(v, (list, dict))})
        log("  " + line)
        checks.append(line)
    except Exception as e:  # the manifest is still good without the names
        problems.append("iNaturalist names could not be built: %s: %s" % (type(e).__name__, e))
    if inat:
        (region / "inat.json").write_text(json.dumps(inat, ensure_ascii=False, indent=0, sort_keys=True) + "\n", encoding="utf-8")
        log("  wrote %s" % (region / "inat.json"))

    # ---- summary
    n_per = Counter(str(r["key"]) for r in rows)
    L = ["# Training photos: Alachua County, records through %s" % through, "",
         "Built by `tools/species/build_train.py` on %s (UTC). %d rows from %d species, at most %d a species." % (
             datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M"), len(rows), len(n_per), args.cap), "",
         "Rows are in order of each photo's rank within its species, so the first rows hold every species' first photo.", "",
         "## Checks", ""] + ["- " + c for c in checks] + ["", "## Photos a species", "", "| photos | species |", "|---|---:|"]
    for lo, hi in ((args.cap, args.cap), (30, args.cap - 1), (10, 29), (5, 9), (2, 4), (1, 1)):
        L.append("| %s | %d |" % ("%d" % lo if lo == hi else "%d to %d" % (lo, hi), sum(1 for v in n_per.values() if lo <= v <= hi)))
    for title, col in (("By kind of eye", "eyes"), ("By class", "class"), ("By licence", "licence")):
        L += ["", "## " + title, "", "| %s | rows | share |" % col, "|---|---:|---:|"]
        for v, n in Counter(r[col] or "(none)" for r in rows).most_common(30):
            L.append("| %s | %d | %s |" % (v, n, pct(n, len(rows))))
    L += ["", "## Rows by rank within species", "", "| first rows | cover ranks below |", "|---:|---:|"]
    for cut in (1, 5, 10, 20, 30, 45, args.cap):
        L.append("| %d | %d |" % (sum(1 for r in rows if r["_rank"] < cut), cut))
    if inat:
        diff = sorted(((by_key[k]["n"], by_key[k]["sci"], v["sci"], by_key[k]["en"], v["en"]) for k, v in inat.items() if v["sci"] != by_key[k]["sci"]), reverse=True)
        L += ["", "## Species GBIF and iNaturalist name differently (the forty most recorded)", "",
              "| records | GBIF name | iNaturalist name | English name in the list | iNaturalist's English name |", "|---:|---|---|---|---|"]
        for n, a, b, e1, e2 in diff[:40]:
            L.append("| %d | *%s* | *%s* | %s | %s |" % (n, a, b, e1, e2))
    if problems:
        L += ["", "## Problems", ""] + ["- " + p for p in problems]
    (out / "SUMMARY.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    log("  wrote %s; GBIF requests %s; %.0fs" % (out / "SUMMARY.md", common.stats(), time.time() - t0))
    if problems:
        log("PROBLEMS:\n  " + "\n  ".join(problems))
        sys.exit(2)
    log("all checks passed")


if __name__ == "__main__":
    main()
