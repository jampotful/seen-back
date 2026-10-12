#!/usr/bin/env python3
"""Species lists at several sizes, from the counts ci/coverage/counts.sh makes. Part of the coverage study (docs/COVERAGE.md).

Reads work/counts/*.tsv (observations per iNaturalist taxon), taxa.csv.gz (iNaturalist's taxonomy), and, for the
evaluation, the Alachua files of pub/data-alachua (species.json, inat.json, the alachua-2025 manifest). Writes to --out:

  world.tsv        one row per species with at least one research-grade observation dated through 2024 (or in the
                   Alachua list), in the order of the text rows: inat_id, name, counts world and by region, flags
  names.txt        the scientific name of each row, in the same order (what tools/coverage/text.py turns into rows)
  eval_truth.csv   each evaluation photo with the row of its species (-1 when the species has no row) and how it was found
  summary.json     totals, list sizes, the share of observations the commonest species cover, casual observations

Subspecies, varieties and forms count for their species. Hybrids are left out, as iNaturalist's rank=species count leaves them out.
Usage: python3 -I tools/coverage/lists.py --counts work/counts --data data_in --out lists
"""
import argparse
import csv
import gzip
import json
import os
from collections import Counter

INFRA = ("subspecies", "variety", "form", "infrahybrid")
REGIONS = ("alachua_2024", "gnv100_2024", "gnv400_2024", "gnv1600_2024", "usa48_2024")
ALL_TIME = ("alachua_all", "gnv25_all", "gnv100_all", "gnv400_all", "gnv1600_all", "usa48_all")
CUTS = (1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 300000, 400000)


def log(*a):
    print(*a, flush=True)


def read_counts(path):
    c = {}
    if not os.path.exists(path):
        return c
    with open(path, encoding="utf-8") as f:
        for line in f:
            k, _, v = line.rstrip("\n").partition("\t")
            if k:
                c[k] = c.get(k, 0) + int(v)
    return c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--counts", required=True)
    ap.add_argument("--data", required=True, help="a directory holding regions/us-fl-alachua/{species,inat}.json and eval/alachua-2025/manifest.csv")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    taxa = {}
    by_name = {}
    with gzip.open(os.path.join(a.counts, "taxa.csv.gz"), "rt", encoding="utf-8", newline="") as f:
        head = f.readline().rstrip("\n").split("\t")
        ix = {h: i for i, h in enumerate(head)}
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) < len(head):
                continue
            tid, rank, name, anc = p[ix["taxon_id"]], p[ix["rank"]], p[ix["name"]], p[ix["ancestry"]]
            active = p[ix["active"]] if "active" in ix else "true"
            taxa[tid] = (rank, name, anc)
            if rank == "species":
                prev = by_name.get(name)
                if prev is None or (active in ("true", "t", "True") and not prev[1]):
                    by_name[name] = (tid, active in ("true", "t", "True"))
    log("%d taxa, %d species names" % (len(taxa), len(by_name)))

    def species_of(tid):
        t = taxa.get(tid)
        if t is None:
            return None
        rank, name, anc = t
        if rank == "species":
            return tid
        if rank in INFRA:
            for x in reversed(anc.split("/")):
                tx = taxa.get(x)
                if tx and tx[0] == "species":
                    return x
        return None

    names = ("world_rg_all", "world_rg_2024", "world_casual") + REGIONS + ALL_TIME
    raw = {n: read_counts(os.path.join(a.counts, n + ".tsv")) for n in names}
    sp = {n: Counter() for n in names}
    skipped = Counter()
    for n in names:
        for tid, c in raw[n].items():
            s = species_of(tid)
            if s is None:
                skipped[(n, (taxa.get(tid) or ("unknown",))[0])] += c
                continue
            sp[n][s] += c
    totals = {}
    with open(os.path.join(a.counts, "totals.tsv"), encoding="utf-8") as f:
        for line in f:
            k, _, v = line.rstrip("\n").partition("\t")
            totals[k] = int(v)

    # the Alachua list, mapped to iNaturalist species
    alachua = json.load(open(os.path.join(a.data, "regions/us-fl-alachua/species.json"), encoding="utf-8"))["species"]
    inat = json.load(open(os.path.join(a.data, "regions/us-fl-alachua/inat.json"), encoding="utf-8"))

    def gbif_to_inat(key, sci):
        e = inat.get(str(key))
        if e and e.get("inat_id") is not None:
            s = species_of(str(e["inat_id"]))
            if s:
                return s, "inat.json"
        b = by_name.get(sci)
        if b:
            return b[0], "same name"
        return None, "not found"

    al_map, al_how = {}, Counter()
    for s in alachua:
        t, how = gbif_to_inat(s["key"], s["sci"])
        al_how[how] += 1
        if t:
            al_map[s["key"]] = t
    al_set = set(al_map.values())
    log("Alachua list: %d species, %d mapped (%s), %d distinct iNaturalist species" % (len(alachua), len(al_map), dict(al_how), len(al_set)))

    # rows: every species with a research-grade observation through 2024, and the Alachua list
    rows = set(k for k, v in sp["world_rg_2024"].items() if v > 0) | al_set
    order = sorted(rows, key=lambda t: (-sp["world_rg_2024"].get(t, 0), int(t)))
    pos = {t: i for i, t in enumerate(order)}
    cols = ["row", "inat_id", "name", "rg_2024", "rg_all", "casual"] + list(REGIONS) + ["in_alachua_list"]
    with open(os.path.join(a.out, "world.tsv"), "w", encoding="utf-8") as f, open(os.path.join(a.out, "names.txt"), "w", encoding="utf-8") as g:
        f.write("\t".join(cols) + "\n")
        for i, t in enumerate(order):
            nm = taxa[t][1]
            f.write("\t".join(str(x) for x in [i, t, nm, sp["world_rg_2024"].get(t, 0), sp["world_rg_all"].get(t, 0), sp["world_casual"].get(t, 0)]
                              + [sp[r].get(t, 0) for r in REGIONS] + [int(t in al_set)]) + "\n")
            g.write(nm + "\n")
    log("rows: %d" % len(order))

    # evaluation photos
    man = list(csv.DictReader(open(os.path.join(a.data, "eval/alachua-2025/manifest.csv"), encoding="utf-8", newline="")))
    how_c = Counter()
    with open(os.path.join(a.out, "eval_truth.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "split", "eyes", "key", "sci", "inat_species", "row", "how"])
        for r in man:
            t, how = gbif_to_inat(r["key"], r["sci"])
            row = pos.get(t, -1) if t else -1
            how_c[how if row >= 0 else how + ", no row"] += 1
            w.writerow([r["id"], r["split"], r["eyes"], r["key"], r["sci"], t or "", row, how])

    def curve(counter):
        v = sorted(counter.values(), reverse=True)
        tot = float(sum(v)) or 1.0
        cum, out, k = 0, {}, 0
        marks = {}
        for i, x in enumerate(v, 1):
            cum += x
            if i in CUTS:
                out[str(i)] = cum / tot
            for q in (0.5, 0.8, 0.9, 0.95, 0.99):
                if q not in marks and cum / tot >= q:
                    marks[q] = i
        out["all"] = 1.0
        return {"species": len(v), "observations": int(tot), "share_by_top_n": out, "species_for_share": {str(q): marks.get(q) for q in (0.5, 0.8, 0.9, 0.95, 0.99)}}

    casual = sp["world_casual"]
    rg = sp["world_rg_all"]
    cas_top = sorted(casual.items(), key=lambda kv: -kv[1])[:200]
    mostly_casual = [t for t, c in casual.items() if c >= 50 and c > 2 * rg.get(t, 0)]
    with open(os.path.join(a.out, "casual_top.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["inat_id", "name", "casual", "research_grade_all"])
        for t, c in cas_top:
            w.writerow([t, taxa[t][1], c, rg.get(t, 0)])

    sizes = {n: sum(1 for v in sp[n].values() if v > 0) for n in names}
    summary = {
        "snapshot": open(os.path.join(a.counts, "snapshot.txt")).read().strip() if os.path.exists(os.path.join(a.counts, "snapshot.txt")) else "",
        "rows_by_quality_grade": totals,
        "observations_of_taxa_above_species_or_hybrids_left_out": {"%s | %s" % k: v for k, v in skipped.most_common(40)},
        "species_counts": sizes,
        "rows": len(order),
        "alachua_list": {"species": len(alachua), "mapped": len(al_map), "how": dict(al_how), "distinct": len(al_set)},
        "eval_truth": dict(how_c),
        "coverage_rg_2024": curve(sp["world_rg_2024"]),
        "coverage_rg_all": curve(sp["world_rg_all"]),
        "casual": {"species_with_casual": sum(1 for v in casual.values() if v > 0), "observations": int(sum(casual.values())),
                   "species_with_50_or_more_casual_and_more_than_twice_their_research_grade": len(mostly_casual),
                   "of_those_with_no_research_grade_through_2024": sum(1 for t in mostly_casual if sp["world_rg_2024"].get(t, 0) == 0)},
    }
    json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1)
    log(json.dumps({k: summary[k] for k in ("species_counts", "rows", "alachua_list", "eval_truth")}, indent=1))
    log(json.dumps(summary["coverage_rg_2024"], indent=1))


if __name__ == "__main__":
    main()
