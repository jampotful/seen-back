#!/usr/bin/env python3
"""Build data/regions/<region>/species.json and SUMMARY.md from GBIF (format: docs/CONTRACTS.md).

Every species with at least one iNaturalist research-grade record (GBIF dataset 50c9509d-...) in the region with
an event date through --through (default 2024-12-31). Counts come from occurrence-search facets on speciesKey:
one faceted query over all months gives `n`, twelve queries with month=1..12 give `m`; both are paged with
facetOffset. The script checks that the twelve months sum to `n` for every species and that the species totals
agree across the two ways of counting, and exits non-zero if they do not.

Taxonomy and canonical names come from GBIF's species API; where the backbone gives a species no phylum, class
and order, those ranks are filled from iNaturalist's taxonomy (listed in SUMMARY.md). English names: the species
is found in iNaturalist's public taxonomy archive by scientific name, and its name is iNaturalist's preferred
English name from the iNaturalist API (en_source "inat-api"; the archive does not mark the preferred name), else
an English name from the archive ("inat-taxonomy"), else GBIF's English vernacular names ("gbif-vernacular",
see common.choose_gbif_english), else empty. See names.py. The kind of eye comes from eyes.py.

Usage: python3 tools/species/build_species.py [--out data/regions/us-fl-alachua] [--cache work/cache] [--diag DIR]
Needs network access to api.gbif.org and www.inaturalist.org (run it on a build machine; see .github/workflows/data.yml).
"""
import argparse
import datetime
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402
import eyes  # noqa: E402
import names  # noqa: E402
from common import log  # noqa: E402

REGION = {"id": "us-fl-alachua", "name": "Alachua County, Florida", "gadm": "USA.10.1_1"}
BBOX = {"decimalLatitude": "29.42,29.95", "decimalLongitude": "-82.66,-82.05"}
PROBES = ["Ardea herodias", "Odocoileus virginianus", "Alligator mississippiensis", "Sciurus carolinensis",
          "Cardinalis cardinalis", "Quercus virginiana", "Procyon lotor", "Didelphis virginiana", "Gallinula galeata",
          "Anolis sagrei", "Danaus plexippus", "Sabal palmetto", "Felis catus", "Homo sapiens", "Coragyps atratus",
          "Callicarpa americana", "Lithobates sphenocephalus", "Canis familiaris", "Gopherus polyphemus"]


def region_params(args):
    if args.bbox:
        return dict(BBOX)
    return {"gadmGid": args.gadm}


def verify_region(base, diag):
    """Look at the place fields of returned records: GADM names, stateProvince, county, coordinates."""
    r = common.get_json("/occurrence/search", dict(base, limit=300))
    recs = r.get("results", [])
    tally = defaultdict(Counter)
    lat, lon = [], []
    for x in recs:
        g = x.get("gadm") or {}
        tally["gadm.level1"][(g.get("level1") or {}).get("name")] += 1
        tally["gadm.level2"][(g.get("level2") or {}).get("name")] += 1
        tally["gadm.level2.gid"][(g.get("level2") or {}).get("gid")] += 1
        tally["stateProvince"][x.get("stateProvince")] += 1
        tally["county"][x.get("county")] += 1
        tally["taxonRank"][x.get("taxonRank")] += 1
        tally["has_speciesKey"][bool(x.get("speciesKey"))] += 1
        if x.get("decimalLatitude") is not None:
            lat.append(x["decimalLatitude"])
            lon.append(x["decimalLongitude"])
    lines = ["region check on the first %d records of %d:" % (len(recs), r.get("count", 0))]
    for k, c in tally.items():
        lines.append("  %s: %s" % (k, dict(c.most_common(8))))
    if lat:
        lines.append("  latitude %.4f..%.4f, longitude %.4f..%.4f" % (min(lat), max(lat), min(lon), max(lon)))
    for field in ("gadmLevel2Gid", "gadmLevel1Gid", "stateProvince"):
        # Every record of the query, not just the first page: the facet counts of the place fields.
        try:
            r2 = common.get_json("/occurrence/search", dict(base, limit=0, facet=field, facetLimit=20), tries=3)
            fc = (r2.get("facets") or [{}])[0].get("counts", [])
            got = {c["name"]: c["count"] for c in fc}
            lines.append("  all %d records by %s: %s (sum %d)" % (r2.get("count", 0), field, got, sum(got.values())))
            tally["facet:" + field] = Counter(got)
        except Exception as e:
            lines.append("  facet on %s not available: %s" % (field, str(e)[:160]))
    if diag:
        (diag / "occurrence_sample.json").write_text(json.dumps([common.scrub_occurrence(x) for x in recs[:5]], indent=1))
    return "\n".join(lines), tally


def gather_counts(base):
    """n per species (one facet query) and m per species (twelve), with the checks."""
    n, total, pages, dups = common.facet_all(base)
    log("  all months: %d species, %d records in the query, %d facet pages, %d duplicate facet values" % (len(n), total, pages, dups))
    m = defaultdict(lambda: [0] * 12)
    month_totals, month_species_sums, month_dups = [], [], 0
    for mo in range(1, 13):
        c, t, p, d = common.facet_all(dict(base, month=mo))
        month_dups += d
        month_totals.append(t)
        month_species_sums.append(sum(c.values()))
        for k, v in c.items():
            m[k][mo - 1] = v
        log("  month %2d: %6d records, %6d in %d species, %d pages" % (mo, t, sum(c.values()), len(c), p))
    return n, total, dups, m, month_totals, month_species_sums, month_dups


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default="data/regions/us-fl-alachua")
    ap.add_argument("--gadm", default=REGION["gadm"])
    ap.add_argument("--bbox", action="store_true", help="filter by the bounding box instead of the GADM area")
    ap.add_argument("--through", default="2024-12-31", help="last event date counted (must be 31 December of a year)")
    ap.add_argument("--cache", default="work/cache")
    ap.add_argument("--diag", default="", help="directory for diagnostic samples (no names of people)")
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()
    t0 = time.time()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    diag = Path(args.diag) if args.diag else None
    if diag:
        diag.mkdir(parents=True, exist_ok=True)
    cache = common.JsonCache(Path(args.cache) / "gbif")
    if not args.through.endswith("-12-31"):
        common.die("--through must be the last day of a year so that a year range expresses it exactly")
    last_year = int(args.through[:4])
    place = region_params(args)
    base = dict(place, datasetKey=common.INAT_DATASET, year="1600,%d" % last_year)
    checks, problems = [], []

    log("== region filter: %s" % place)
    text, tally = verify_region(base, diag)
    log(text)
    checks.append(text)
    if not args.bbox:
        gids = tally["gadm.level2.gid"]
        if set(gids) != {args.gadm}:
            problems.append("records outside %s in the region sample: %s" % (args.gadm, dict(gids)))
        fac = tally.get("facet:gadmLevel2Gid")
        if fac and set(fac) != {args.gadm}:
            problems.append("records of the query fall in other GADM areas: %s" % dict(fac))
        if set(tally["gadm.level2"]) != {"Alachua"} or set(tally["gadm.level1"]) != {"Florida"}:
            problems.append("GADM names are not all Florida / Alachua: %s %s" % (dict(tally["gadm.level1"]), dict(tally["gadm.level2"])))
    c_year = common.count(base)
    c_date = common.count(dict(place, datasetKey=common.INAT_DATASET, eventDate="1600-01-01,%s" % args.through))
    c_bbox = common.count(dict(BBOX, datasetKey=common.INAT_DATASET, year="1600,%d" % last_year))
    c_all = common.count(dict(place, datasetKey=common.INAT_DATASET))
    line = ("records in region through %s: %d by year range, %d by eventDate range; all dates: %d; "
            "bounding box through %s: %d" % (args.through, c_year, c_date, c_all, args.through, c_bbox))
    log(line)
    checks.append(line)
    if c_year != c_date:
        problems.append("year-range and eventDate-range counts differ: %d vs %d" % (c_year, c_date))

    log("== counts by species and month")
    n, total, dups, m, month_totals, month_species_sums, month_dups = gather_counts(base)
    if dups or month_dups:
        problems.append("duplicate facet values while paging: %d overall, %d monthly" % (dups, month_dups))
    bad = [(k, n[k], sum(m[k])) for k in n if sum(m[k]) != n[k]]
    extra = [k for k in m if k not in n]
    sum_n = sum(n.values())
    sum_m = sum(sum(v) for v in m.values())
    line = ("species %d; records %d in the query; sum of species n %d (records without a species key: %d); "
            "sum of monthly species counts %d; sum of monthly record totals %d; species whose months do not sum to n: %d; "
            "species seen only in monthly facets: %d" % (len(n), total, sum_n, total - sum_n, sum_m, sum(month_totals), len(bad), len(extra)))
    log(line)
    checks.append(line)
    if bad:
        problems.append("months do not sum to n for %d species, e.g. %s" % (len(bad), bad[:5]))
    if extra:
        problems.append("%d species appear in monthly facets but not in the overall facet" % len(extra))
    if sum_n != sum_m:
        problems.append("species totals differ between the overall facet (%d) and the monthly facets (%d)" % (sum_n, sum_m))
    if sum(month_totals) != total:
        problems.append("monthly record totals (%d) do not add up to the region total (%d)" % (sum(month_totals), total))

    log("== taxonomy for %d species keys" % len(n))
    keys = sorted(n, key=lambda k: (-n[k], int(k) if k.isdigit() else 0, k))
    info = common.pmap(lambda k: common.species_info(k, cache), keys, workers=args.workers, desc="species API")
    if diag:
        (diag / "species_api_sample.json").write_text(json.dumps(info[:3], indent=1))
    ranks = Counter(i.get("rank") for i in info)
    status = Counter(i.get("taxonomicStatus") for i in info)
    log("  ranks %s; status %s" % (dict(ranks), dict(status)))
    checks.append("species API ranks %s; taxonomic status %s" % (dict(ranks), dict(status)))
    missing = [i["key"] for i in info if i.get("missing")]
    if missing:
        problems.append("species keys unknown to the species API: %s" % missing[:10])

    log("== English names")
    wanted = {}
    for i in info:
        nm = i.get("canonicalName") or i.get("species")
        if nm:
            wanted.setdefault(nm, i.get("kingdom"))
    inat, inat_rep, inat_taxa = {}, {}, {}
    try:
        arch = names.ensure_archive(args.cache)
        if diag:
            (diag / "inat_archive.txt").write_text(names.describe(arch, PROBES), encoding="utf-8")
        inat, inat_rep, inat_taxa = names.inat_names(arch, wanted)
        log("  iNaturalist: %s" % inat_rep)
    except Exception as e:  # the list is still useful with GBIF names; say so loudly
        log("  iNaturalist names unavailable: %s: %s" % (type(e).__name__, e))
        problems.append("iNaturalist archive could not be read: %s" % e)
    need = [i for i in info if (i.get("canonicalName") or i.get("species")) not in inat]
    gb = common.pmap(lambda i: common.choose_gbif_english(common.gbif_vernacular(i["key"], cache)), need,
                     workers=args.workers, desc="GBIF vernacular names")
    gbif_names = {str(i["key"]): g for i, g in zip(need, gb) if g}
    if diag and need:
        (diag / "gbif_vernacular_sample.json").write_text(json.dumps(
            [{"key": i["key"], "names": common.gbif_vernacular(i["key"], cache)[:12]} for i in need[:4]], indent=1, ensure_ascii=False))

    log("== writing")
    species, filled = [], []
    for k, i in zip(keys, info):
        sci = i.get("canonicalName") or i.get("species") or ""
        if sci in inat:
            en, src = inat[sci]
        elif k in gbif_names:
            en, src = gbif_names[k], "gbif-vernacular"
        else:
            en, src = "", ""
        rec = {"key": int(k) if k.isdigit() else k, "sci": sci, "en": en, "en_source": src,
               "kingdom": i.get("kingdom") or "", "phylum": i.get("phylum") or "", "class": i.get("class") or "",
               "order": i.get("order") or "", "family": i.get("family") or "", "genus": i.get("genus") or "",
               "n": n[k], "m": m[k]}
        fill_ranks(rec, inat_taxa.get(sci), filled)
        rec["eyes"] = eyes.kind_of_record(rec)
        species.append(rec)
    species.sort(key=lambda s: (-s["n"], s["sci"], str(s["key"])))
    if filled:
        checks.append("ranks filled from iNaturalist's taxonomy where the GBIF backbone gives no phylum, class or order "
                      "(%d species): %s" % (len(filled), "; ".join(filled)))
        log("  " + checks[-1])
    if inat_rep:
        checks.append("English names from iNaturalist: %s" % {k: v for k, v in inat_rep.items() if k != "place_name_examples"})
    query = ("%s/occurrence/search?datasetKey=%s&%s&year=1600,%d&facet=speciesKey (paged with facetOffset); "
             "months: the same with month=1..12" % (common.API, common.INAT_DATASET,
                                                    "&".join("%s=%s" % kv for kv in sorted(place.items())), last_year))
    head = {
        "region": dict(REGION, gadm=args.gadm) if not args.bbox else dict(REGION, gadm="", bbox=BBOX),
        "source": {"dataset": "iNaturalist research-grade observations via GBIF", "datasetKey": common.INAT_DATASET,
                   "retrieved": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
                   "records_through": args.through, "doi_or_query": query},
    }
    common.write_json_list(out / "species.json", head, species)
    log("  wrote %s: %d species" % (out / "species.json", len(species)))
    status = {str(i.get("key")): i.get("taxonomicStatus") for i in info}
    summary = make_summary(species, head, checks, problems, inat_rep, total, args, status)
    (out / "SUMMARY.md").write_text(summary, encoding="utf-8")
    log("  wrote %s" % (out / "SUMMARY.md"))
    log("  GBIF requests: %s; %.0fs" % (common.stats(), time.time() - t0))
    if problems:
        log("PROBLEMS:\n  " + "\n  ".join(problems))
        sys.exit(2)
    log("all checks passed")


def fill_ranks(rec, inat_ranks, filled):
    """Where the GBIF backbone gives a species no phylum, class and order (a hole in the backbone, not a
    different classification), take the missing ranks from iNaturalist's taxonomy so the kind of eye is not lost."""
    if not inat_ranks or rec["phylum"] or rec["class"] or rec["order"]:
        return
    got = []
    for r in ("kingdom", "phylum", "class", "order", "family", "genus"):
        if not rec[r] and inat_ranks.get(r):
            rec[r] = inat_ranks[r]
            got.append(r)
    if got:
        filled.append("%s (%s)" % (rec["sci"], ", ".join(got)))


def pct(a, b):
    return "%.1f%%" % (100.0 * a / b) if b else "n/a"


def make_summary(species, head, checks, problems, inat_rep, total, args, status=None):
    S = len(species)
    R = sum(s["n"] for s in species)
    L = []
    L.append("# Species list: %s" % head["region"]["name"])
    L.append("")
    L.append("Made by `tools/species/build_species.py` on %s from GBIF (%s, dataset `%s`), records through %s. "
             "Region filter: %s. Rerun it to check any number here." % (
                 head["source"]["retrieved"], head["source"]["dataset"], head["source"]["datasetKey"],
                 head["source"]["records_through"],
                 ("bounding box %s" % BBOX) if args.bbox else "GADM area `%s`" % head["region"]["gadm"]))
    L.append("")
    L.append("## Size")
    L.append("")
    L.append("- Species: **%d**, carrying **%d** records (all research-grade records in the region through %s: %d; "
             "the %d others are not identified to a GBIF species)." % (S, R, args.through, total, total - R))
    for t in (1, 3, 10, 50):
        L.append("- Species with n at least %d: %d" % (t, sum(1 for s in species if s["n"] >= t)))
    L.append("")
    L.append("## By kind of eye")
    L.append("")
    L.append("| Kind | Species | Records |")
    L.append("|---|---:|---:|")
    by_kind = defaultdict(lambda: [0, 0])
    for s in species:
        by_kind[s["eyes"]][0] += 1
        by_kind[s["eyes"]][1] += s["n"]
    for kd in eyes.KINDS:
        if kd in by_kind:
            L.append("| %s | %d | %d |" % (kd, by_kind[kd][0], by_kind[kd][1]))
    L.append("")
    L.append("## By class (as the GBIF backbone gives it)")
    L.append("")
    L.append("| Kingdom | Class | Species | Records |")
    L.append("|---|---|---:|---:|")
    by_class = defaultdict(lambda: [0, 0])
    for s in species:
        by_class[(s["kingdom"], s["class"] or "(none)")][0] += 1
        by_class[(s["kingdom"], s["class"] or "(none)")][1] += s["n"]
    for (kg, cl), (a, b) in sorted(by_class.items(), key=lambda kv: -kv[1][0]):
        L.append("| %s | %s | %d | %d |" % (kg, cl, a, b))
    L.append("")
    L.append("## The forty most recorded species")
    L.append("")
    L.append("| # | Scientific name | English name | n | Kind |")
    L.append("|---:|---|---|---:|---|")
    for i, s in enumerate(species[:40], 1):
        L.append("| %d | *%s* | %s | %d | %s |" % (i, s["sci"], s["en"] or "", s["n"], s["eyes"]))
    L.append("")
    L.append("## English names")
    L.append("")
    src = Counter(s["en_source"] for s in species)
    src_r = Counter()
    for s in species:
        src_r[s["en_source"]] += s["n"]
    with_en = sum(1 for s in species if s["en"])
    L.append("- Species with an English name: %d of %d (%s); records whose species has one: %s." % (
        with_en, S, pct(with_en, S), pct(sum(s["n"] for s in species if s["en"]), R)))
    L.append("- iNaturalist's preferred English name (its API, locale en, place Florida; taxon found through the "
             "taxonomy archive by scientific name), `en_source` `inat-api`: %d species (%s of records)." % (
                 src["inat-api"], pct(src_r["inat-api"], R)))
    L.append("- An English name from iNaturalist's taxonomy archive where the API gave none, `inat-taxonomy`: %d (%s)." % (
        src["inat-taxonomy"], pct(src_r["inat-taxonomy"], R)))
    L.append("- GBIF's English vernacular names, `gbif-vernacular`: %d (%s); none: %d (%s)." % (
        src["gbif-vernacular"], pct(src_r["gbif-vernacular"], R), src[""], pct(src_r[""], R)))
    if inat_rep.get("archive_choice_agrees_with_api") is not None:
        a, d = inat_rep["archive_choice_agrees_with_api"], inat_rep.get("archive_choice_differs_from_api", 0)
        L.append("- Why the API: the archive lists a taxon's English names without marking the preferred one. Taking "
                 "a name from the archive alone (a US or Florida name first, else the first name with no place) "
                 "matches iNaturalist's preferred name for %d of %d species (%s)." % (a, a + d, pct(a, a + d)))
    if inat_rep:
        L.append("- Join by scientific name to iNaturalist species: %d of %d names found; %d dropped for a kingdom mismatch; "
                 "%d ambiguous; %d with an English name." % (inat_rep.get("name_in_inat", 0), inat_rep.get("wanted", 0),
                                                            inat_rep.get("kingdom_mismatch", 0), inat_rep.get("ambiguous", 0),
                                                            inat_rep.get("with_english", 0)))
    L.append("")
    L.append("## Checks")
    L.append("")
    for c in checks:
        for ln in c.splitlines():
            L.append("    " + ln)
    L.append("")
    L.append("Problems found: %s" % ("none" if not problems else ""))
    for p in problems:
        L.append("- %s" % p)
    L.append("")
    L.append("## Noticed")
    L.append("")
    odd = []
    top_no_en = [s for s in species[:200] if not s["en"]]
    if top_no_en:
        odd.append("Among the 200 most recorded species, %d have no English name: %s." % (
            len(top_no_en), ", ".join("*%s* (%d)" % (s["sci"], s["n"]) for s in top_no_en[:10])))
    cls = Counter(s["class"] for s in species if s["class"] in ("Squamata", "Testudines", "Crocodylia", "Reptilia"))
    if cls:
        odd.append("Reptiles by the class GBIF gives them: %s." % dict(cls))
    for nm in ("Homo sapiens", "Felis catus", "Canis familiaris"):
        hit = [s for s in species if s["sci"] == nm]
        odd.append("*%s*: %s." % (nm, ("n = %d, kind %s" % (hit[0]["n"], hit[0]["eyes"])) if hit else "not in the list"))
    singles = sum(1 for s in species if s["n"] == 1)
    odd.append("%d species (%s) rest on a single record." % (singles, pct(singles, S)))
    ext = [s for s in species if s["eyes"] == "other" and s["class"] == "Mammalia"]
    if ext:
        odd.append("Mammals drawn with the `other` eye: %s." % ", ".join(
            "%s (%d)" % (s["en"] or s["sci"], s["n"]) for s in ext[:12]))
    status = status or {}
    doubt = [s for s in species if status.get(str(s["key"])) not in (None, "ACCEPTED")]
    if doubt:
        odd.append("%d species carry a GBIF taxonomic status other than ACCEPTED (%s), e.g. %s." % (
            len(doubt), dict(Counter(status.get(str(s["key"])) for s in doubt)),
            ", ".join("*%s* (%d)" % (s["sci"], s["n"]) for s in doubt[:6])))
    noclass = [s for s in species if not s["class"]]
    if noclass:
        grp = Counter("%s/%s" % (s["kingdom"], s["phylum"] or "?") for s in noclass)
        odd.append("%d species have no class in the GBIF backbone (%s); ray-finned fishes are among them, which is "
                   "harmless here because fish take the `other` eye either way. Examples: %s." % (
                       len(noclass), dict(grp), ", ".join("*%s* (%s)" % (s["sci"], s["order"] or "no order") for s in noclass[:6])))
    busiest = max(range(12), key=lambda i: sum(s["m"][i] for s in species))
    odd.append("The busiest calendar month is %s with %d records (%s of all)." % (
        ("January February March April May June July August September October November December").split()[busiest],
        sum(s["m"][busiest] for s in species), pct(sum(s["m"][busiest] for s in species), R)))
    for o in odd:
        L.append("- " + o)
    L.append("")
    return "\n".join(L)


if __name__ == "__main__":
    main()
