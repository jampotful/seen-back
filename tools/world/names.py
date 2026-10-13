#!/usr/bin/env python3
"""GBIF's names for the full database's world rows (docs/tracks/worlddb.md, step 1).

The world list (tools/coverage/lists.py, `world.tsv`: 433,156 iNaturalist species, most recorded first) names species
as iNaturalist does. The county rows use GBIF's names, because BioCLIP 2 was trained on them (docs/COVERAGE.md), so the
world rows do too. Each iNaturalist species is given the name GBIF's backbone accepts for it:

  1. the backbone's entries of rank species with the same canonical name are the candidates;
  2. the candidate whose kingdom, phylum, class, order and family agree most with iNaturalist's is taken, an accepted
     or doubtful entry before a synonym where they agree equally;
  3. an accepted or doubtful entry keeps its name; a synonym takes the name of the entry it points to, and of that
     entry's species where it points to a subspecies, variety or form;
  4. a name the backbone does not have keeps iNaturalist's name.

iNaturalist species that come out with the same GBIF name are one species in GBIF's taxonomy and share one row. Rows are
ordered by their research-grade records through 2024 (summed over the iNaturalist species they hold), most first.
English names follow iNaturalist, as the county list's do: the first English name its taxonomy archive gives the
taxon, else the county table's name for the same scientific name.

Writes to --out:
  rows.tsv       a line a row: row, sci (GBIF's name), en, group, records (through 2024), gbif_key, how, inat_ids
  names.txt      each row's name, in row order (what tools/coverage/text.py makes its sentences from)
  inat_rows.tsv  a line a species of world.tsv: inat_id, its row in world.tsv, its row here
  summary.json   how each name was found, and the rows that hold more than one iNaturalist species

Usage: python3 -I tools/world/names.py --world world.tsv.gz --taxa taxa.csv.gz --backbone Taxon.tsv
         [--vernacular VernacularNames-english.csv] [--county models/naturalist/species.json] --out names
(--backbone - reads the backbone's Taxon.tsv from standard input, twice not being possible: give a path.)
"""
import argparse
import csv
import gzip
import io
import json
import os
import sys
from collections import Counter, defaultdict

sys.path.append(os.path.dirname(os.path.abspath(__file__)))   # appended, so that no file here shadows a standard module
import groups  # noqa: E402

RANKS = ("kingdom", "phylum", "class", "order", "family")
INFRA = {"subspecies", "variety", "form", "infraspecificname", "infrasubspecificname"}
csv.field_size_limit(1 << 24)


def log(*a):
    print(*a, flush=True)


def opener(path):
    return gzip.open(path, "rt", encoding="utf-8", newline="") if str(path).endswith(".gz") else open(path, encoding="utf-8", newline="")


def read_world(path):
    with opener(path) as f:
        r = csv.DictReader(f, delimiter="\t")
        return [(int(x["inat_id"]), x["name"], int(x["rg_2024"])) for x in r]


def backbone_rows(path):
    """(header index, row) for each line of GBIF's Taxon.tsv. The file has no quoting."""
    with open(path, encoding="utf-8", errors="replace") as f:
        head = f.readline().rstrip("\n").split("\t")
        ix = {h: i for i, h in enumerate(head)}
        need = ("taxonID", "acceptedNameUsageID", "parentNameUsageID", "canonicalName", "taxonRank", "taxonomicStatus") + RANKS
        miss = [n for n in need if n not in ix]
        if miss:
            sys.exit("backbone: no column %s in %s" % (miss, head))
        n = len(head)
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) < n:
                p += [""] * (n - len(p))
            yield ix, p


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--world", required=True)
    ap.add_argument("--taxa", required=True)
    ap.add_argument("--backbone", required=True)
    ap.add_argument("--vernacular", default="")
    ap.add_argument("--county", default="")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    world = read_world(a.world)
    log("world list: %d species" % len(world))
    want = {nm for _, nm, _ in world}

    # iNaturalist's taxonomy: each species' names at the five ranks, and its group
    rank, name, anc = {}, {}, {}
    for tid, ancestry, rk, nm in groups.read_taxa(a.taxa):
        rank[tid], name[tid] = rk, nm
        anc[tid] = [int(x) for x in ancestry.split("/") if x.isdigit()] if ancestry else []
    log("iNaturalist taxa: %d" % len(rank))
    lineage, group = {}, {}
    for tid, _, _ in world:
        line = anc.get(tid, []) + [tid]
        lineage[tid] = {rank.get(x): name.get(x) for x in line if rank.get(x) in RANKS}
        nms = {name.get(x, "") for x in line}
        genus = next((name[x] for x in line if rank.get(x) == "genus"), None)
        family = next((name[x] for x in line if rank.get(x) == "family"), None)
        group[tid] = groups.group_of(nms, genus, family) if tid in rank else "other"

    # the backbone, first pass: every species-rank entry named as a world species is a candidate
    cand = defaultdict(list)
    seen = 0
    for ix, p in backbone_rows(a.backbone):
        seen += 1
        if p[ix["taxonRank"]].lower() != "species":
            continue
        cn = p[ix["canonicalName"]]
        if cn not in want:
            continue
        cand[cn].append({"id": p[ix["taxonID"]], "acc": p[ix["acceptedNameUsageID"]], "status": p[ix["taxonomicStatus"]].lower(),
                         "lin": {r: p[ix[r]] for r in RANKS}})
    log("backbone entries read: %d; world names with a candidate: %d of %d" % (seen, len(cand), len(want)))

    # second pass: the entries synonyms point to, and the species above an infraspecific one
    targets = {c["acc"] for cs in cand.values() for c in cs if "synonym" in c["status"] and c["acc"]}
    info = {}
    for ix, p in backbone_rows(a.backbone):
        tid = p[ix["taxonID"]]
        if tid in targets:
            info[tid] = (p[ix["taxonRank"]].lower(), p[ix["canonicalName"]], p[ix["parentNameUsageID"]], p[ix["taxonomicStatus"]].lower())
    parents = {v[2] for v in info.values() if v[0] in INFRA and v[2]}
    if parents - set(info):
        for ix, p in backbone_rows(a.backbone):
            tid = p[ix["taxonID"]]
            if tid in parents and tid not in info:
                info[tid] = (p[ix["taxonRank"]].lower(), p[ix["canonicalName"]], p[ix["parentNameUsageID"]], p[ix["taxonomicStatus"]].lower())
    log("entries pointed to: %d, found %d" % (len(targets), len(set(info) & targets)))

    def agree(c, lin):
        return sum(1 << (4 - i) for i, r in enumerate(RANKS) if lin.get(r) and c["lin"].get(r) == lin.get(r))

    how = Counter()
    gbif = {}
    for tid, nm, _ in world:
        cs = cand.get(nm)
        if not cs:
            gbif[tid] = (nm, "", "not in the backbone")
            how["not in the backbone"] += 1
            continue
        lin = lineage[tid]
        best = max(cs, key=lambda c: (agree(c, lin), "synonym" not in c["status"], c["status"] == "accepted", -int(c["id"]) if c["id"].isdigit() else 0))
        if agree(best, lin) < 16 and lin.get("kingdom"):
            gbif[tid] = (nm, "", "only in another kingdom")
            how["only in another kingdom"] += 1
            continue
        if "synonym" not in best["status"]:
            gbif[tid] = (nm, best["id"], best["status"] or "accepted")
            how[best["status"] or "accepted"] += 1
            continue
        t = info.get(best["acc"])
        if t and t[0] == "species" and t[1]:
            gbif[tid] = (t[1], best["acc"], "synonym of a species")
        elif t and t[0] in INFRA and info.get(t[2]) and info[t[2]][0] == "species" and info[t[2]][1]:
            gbif[tid] = (info[t[2]][1], t[2], "synonym of a lower rank")
        else:
            gbif[tid] = (nm, best["id"], "synonym of a higher rank, kept")
        how[gbif[tid][2]] += 1
    log("how the names were found: %s" % dict(how))

    # English names: iNaturalist's taxonomy archive first, then the county table
    en = {}
    if a.vernacular and os.path.exists(a.vernacular):
        with open(a.vernacular, encoding="utf-8", newline="") as f:
            r = csv.DictReader(f)
            for x in r:
                try:
                    k = int(x.get("id") or x.get("taxonID") or 0)
                except ValueError:
                    continue
                v = (x.get("vernacularName") or "").strip()
                if k and v and k not in en:
                    en[k] = v
        log("English names from the archive: %d" % len(en))
    county_en, county_key = {}, {}
    if a.county and os.path.exists(a.county):
        t = json.load(open(a.county, encoding="utf-8"))
        keys = t.get("keys") or []
        for i, r in enumerate(t["species"]):
            county_en.setdefault(r[0], r[1])
            if i < len(keys):
                county_key.setdefault(r[0], keys[i])

    # one row a GBIF name
    rows = {}
    for i, (tid, nm, n) in enumerate(world):
        g = gbif[tid][0]
        r = rows.get(g)
        if r is None:
            rows[g] = r = {"sci": g, "n": 0, "first": i, "members": []}
        r["n"] += n
        r["members"].append((n, i, tid))
    order = sorted(rows.values(), key=lambda r: (-r["n"], r["first"]))
    pos = {}
    with open(os.path.join(a.out, "rows.tsv"), "w", encoding="utf-8") as f, open(os.path.join(a.out, "names.txt"), "w", encoding="utf-8") as g:
        f.write("row\tsci\ten\tgroup\trecords\tgbif_key\thow\tinat_ids\n")
        for j, r in enumerate(order):
            r["members"].sort(key=lambda m: (-m[0], m[1]))
            lead = r["members"][0][2]
            name_en = en.get(lead) or county_en.get(r["sci"], "")
            key = gbif[lead][1] or str(county_key.get(r["sci"], ""))
            f.write("%d\t%s\t%s\t%s\t%d\t%s\t%s\t%s\n" % (j, r["sci"], name_en.replace("\t", " "), group[lead], r["n"], key, gbif[lead][2],
                                                       ",".join(str(m[2]) for m in r["members"])))
            g.write(r["sci"] + "\n")
            for m in r["members"]:
                pos[m[2]] = j
    with open(os.path.join(a.out, "inat_rows.tsv"), "w", encoding="utf-8") as f:
        f.write("inat_id\tworld_row\trow\n")
        for i, (tid, _, _) in enumerate(world):
            f.write("%d\t%d\t%d\n" % (tid, i, pos[tid]))
    shared = [r for r in order if len(r["members"]) > 1]
    summary = {"world_species": len(world), "rows": len(order), "how": dict(how),
               "rows_holding_more_than_one_inat_species": len(shared),
               "inat_species_in_shared_rows": sum(len(r["members"]) for r in shared),
               "examples_of_shared_rows": [[r["sci"], [name.get(m[2], "") for m in r["members"]]] for r in shared[:40]],
               "names_changed": sum(1 for tid, nm, _ in world if gbif[tid][0] != nm),
               "english_names": sum(1 for r in order if en.get(r["members"][0][2]) or county_en.get(r["sci"])),
               "groups": dict(Counter(group[r["members"][0][2]] for r in order))}
    json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1)
    log(json.dumps({k: v for k, v in summary.items() if k != "examples_of_shared_rows"}, indent=1))


if __name__ == "__main__":
    main()
