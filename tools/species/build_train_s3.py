#!/usr/bin/env python3
"""Build the training manifest from iNaturalist's open-data files, with no API in the way.

A second route to data/train/<name>/manifest.csv (format: docs/CONTRACTS.md), written on the night GBIF's occurrence
search kept answering "too many requests". iNaturalist publishes monthly tab-separated snapshots of its openly licensed
observations and photos in a public bucket (https://github.com/inaturalist/inaturalist-open-data):
observations.csv.gz, photos.csv.gz and taxa.csv.gz. This script takes two small extracts of them, made by
ci/data/train_s3.sh with awk while the files stream past:

  obs.tsv      research-grade observations inside the region's bounding box (header kept)
  photos.tsv   the photos of those observations (header kept)
  taxa.csv.gz  the whole taxonomy file (small)

and writes the manifest: observations dated through the species list's `records_through`, identified to a species that
is in the species list (matched by scientific name; a subspecies counts as its species; a species GBIF files under
another name is matched through the evaluation photos, see below), one photo an observation (the first), up to --cap a species, ranked by sha256("<seed>|<photo id>") so the choice can be repeated. Rows are in order of
each photo's rank within its species, so any prefix of the file is a fair, smaller training set.

Names that differ: the evaluation manifest carries GBIF species keys and iNaturalist photo ids. Joined to the photos
file, each evaluation photo shows which iNaturalist species its observation is filed under. When most of a list
species' evaluation photos sit under an iNaturalist name that no list species carries (iNaturalist's Gallinula
galeata for GBIF's Gallinula chloropus), observations under that name count for the list species too. The same
join is written, with --inat-out, as the iNaturalist taxon most often attached to each key (inat.json's format).

Differences from the GBIF route, stated plainly: the region is a bounding box around Alachua County, not the county's
outline, so some photos come from just over the line; iNaturalist blurs the place of some threatened species; `gbif_id`
is empty; licences are written as the files give them ("CC-BY-NC", no version). No names of people are written.

Usage: python3 tools/species/build_train_s3.py --obs obs.tsv --photos photos.tsv --taxa taxa.csv.gz
"""
import argparse
import csv
import datetime
import gzip
import hashlib
import json
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

COLUMNS = ["id", "gbif_id", "obs_url", "key", "sci", "en", "kingdom", "class", "order", "family", "eyes",
           "date", "month", "photo_url", "licence", "split"]
INFRA = ("subspecies", "variety", "form", "infrahybrid")


def log(*a):
    print(*a, flush=True)


def rank_of(seed, pid):
    return hashlib.sha256(("%s|%s" % (seed, pid)).encode()).hexdigest()


def read_tsv(path):
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8", newline="") as f:
        head = f.readline().rstrip("\n").split("\t")
        for line in f:
            yield dict(zip(head, line.rstrip("\n").split("\t")))


def pct(a, b):
    return "%.1f%%" % (100.0 * a / b) if b else "n/a"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--obs", required=True)
    ap.add_argument("--photos", required=True)
    ap.add_argument("--taxa", required=True)
    ap.add_argument("--out", default="data/train/alachua-pre2025")
    ap.add_argument("--region-dir", default="data/regions/us-fl-alachua")
    ap.add_argument("--eval", default="data/eval/alachua-2025/manifest.csv")
    ap.add_argument("--cap", type=int, default=60)
    ap.add_argument("--seed", default="seen-back/alachua-pre2025/s3/v1")
    ap.add_argument("--snapshot", default="", help="date of the open-data files, for the summary")
    ap.add_argument("--inat-out", default="", help="write the evaluation photos' iNaturalist names per key here (JSON)")
    args = ap.parse_args()
    t0 = time.time()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    region = Path(args.region_dir)
    sp = json.loads((region / "species.json").read_text(encoding="utf-8"))
    by_name = {}
    dup_names = set()
    for s in sp["species"]:
        if s["sci"] in by_name:
            dup_names.add(s["sci"])          # two keys, one name: the more recorded one keeps the name
            if s["n"] <= by_name[s["sci"]]["n"]:
                continue
        by_name[s["sci"]] = s
    through = sp["source"]["records_through"]
    problems, checks = [], []

    log("== taxonomy")
    taxa = {}
    for r in read_tsv(args.taxa):
        taxa[r["taxon_id"]] = (r.get("rank", ""), r.get("name", ""), r.get("ancestry", ""))
    log("  %d taxa" % len(taxa))

    def species_of(tid):
        """(taxon id, name) of the species a taxon belongs to: itself at species rank, its species ancestor below that."""
        t = taxa.get(tid)
        if not t:
            return ("", "")
        rank, name, anc = t
        if rank == "species" or rank == "hybrid":
            return (tid, name)
        if rank in INFRA:
            for a in reversed(anc.split("/")):
                ta = taxa.get(a)
                if ta and ta[0] == "species":
                    return (a, ta[1])
            return ("", " ".join(name.split()[:2]))
        return ("", "")

    eval_rows = []
    if Path(args.eval).exists():
        for r in csv.DictReader(open(args.eval, encoding="utf-8")):
            m = re.search(r"/photos/(\d+)/", r["photo_url"])
            eval_rows.append((r["key"], m.group(1) if m else ""))
    eval_photos = {p for _, p in eval_rows if p}
    eval_n = len(eval_rows)

    log("== observations")
    allobs = {}
    for r in read_tsv(args.obs):
        allobs[r["observation_uuid"]] = (r.get("observed_on", ""), r.get("taxon_id", ""))
    n_obs = len(allobs)
    log("  %d research-grade observations in the box" % n_obs)

    log("== photos")
    first, photo_obs = {}, {}                    # observation -> its first photo; evaluation photo -> observation
    n_ph = 0
    for r in read_tsv(args.photos):
        n_ph += 1
        u, pid, ext = r.get("observation_uuid", ""), r.get("photo_id", ""), r.get("extension", "")
        if pid in eval_photos:
            photo_obs[pid] = u
        if u not in allobs or not pid or not ext:
            continue
        try:
            pos = int(r.get("position") or 0)
        except ValueError:
            pos = 0
        cur = first.get(u)
        if cur is None or pos < cur[0]:
            first[u] = (pos, pid, ext, r.get("license", ""))

    log("== the evaluation photos' iNaturalist names")
    sci_of = {str(s["key"]): s["sci"] for s in sp["species"]}
    entry_of = {str(s["key"]): s for s in sp["species"]}
    tally = defaultdict(Counter)
    for key, pid in eval_rows:
        u = photo_obs.get(pid)
        if u in allobs:
            stid, nm = species_of(allobs[u][1])
            if nm:
                tally[key][(stid, nm)] += 1
    joined = sum(sum(c.values()) for c in tally.values())
    inat = {}
    cands = defaultdict(list)
    for key, c in tally.items():
        (stid, nm), k = c.most_common(1)[0]
        tot = sum(c.values())
        inat[key] = {"inat_id": int(stid) if stid.isdigit() else 0, "sci": nm, "en": "", "share": round(k / tot, 3), "n": tot}
        if key in sci_of and nm != sci_of[key] and nm not in by_name and k / tot >= 0.5:
            cands[nm].append((k, key))
    alias = {}
    for nm, ks in cands.items():
        ks.sort(reverse=True)
        if len(ks) == 1 or ks[0][0] > 2 * ks[1][0]:
            alias[nm] = entry_of[ks[0][1]]
        else:
            problems.append("ambiguous iNaturalist name %s (keys %s); not used" % (nm, ks))
    line = ("evaluation photos found in the open-data photos file: %d of %d (keys: %d); keys whose photos sit mostly under "
            "another iNaturalist name: %d; names used as aliases: %d" % (joined, eval_n, len(tally),
            sum(1 for k, v in inat.items() if k in sci_of and v["sci"] != sci_of[k]), len(alias)))
    log("  " + line)
    checks.append(line)

    obs, why = {}, Counter()
    via_alias = Counter()
    for u, (d, tid) in allobs.items():
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", d):
            why["no date"] += 1
            continue
        if d > through:
            why["dated after %s" % through] += 1
            continue
        stid, nm = species_of(tid)
        if not nm:
            why["not identified to a species"] += 1
            continue
        s = by_name.get(nm)
        if not s:
            s = alias.get(nm)
            if not s:
                why["species not in the species list by name"] += 1
                continue
            via_alias[nm] += 1
        obs[u] = (d, s, tid, nm)
    line = "observations in the box, research grade: %d; kept: %d (through an alias: %d); left out: %s" % (
        n_obs, len(obs), sum(via_alias.values()), dict(why))
    log("  " + line)
    checks.append(line)
    line = "photo rows read: %d; kept observations with a photo: %d of %d" % (
        n_ph, sum(1 for u in obs if u in first), len(obs))
    log("  " + line)
    checks.append(line)

    per = defaultdict(list)
    shared = 0
    for u in obs:
        if u not in first:
            continue
        pos, pid, ext, lic = first[u]
        if pid in eval_photos:
            shared += 1
            continue
        d, s, tid, nm = obs[u]
        per[str(s["key"])].append((u, pid, ext, lic, d))
    chosen = []
    for k, recs in per.items():
        s = obs[recs[0][0]][1]
        ranked = sorted(recs, key=lambda c: rank_of(args.seed, c[1]))[: args.cap]
        for r, c in enumerate(ranked):
            chosen.append((r, -s["n"], int(k), int(c[1]), c, s))
    chosen.sort(key=lambda t: t[:4])
    rows = []
    for i, (rank, _, key, _, (u, pid, ext, lic, d), s) in enumerate(chosen, 1):
        rows.append({
            "id": "t%06d" % i, "gbif_id": "", "obs_url": "https://www.inaturalist.org/observations/%s" % u, "key": key,
            "sci": s["sci"], "en": s["en"], "kingdom": s.get("kingdom", ""), "class": s.get("class", ""),
            "order": s.get("order", ""), "family": s.get("family", ""), "eyes": s["eyes"], "date": d, "month": int(d[5:7]),
            "photo_url": "https://inaturalist-open-data.s3.amazonaws.com/photos/%s/medium.%s" % (pid, ext),
            "licence": lic or "", "split": "train", "_rank": rank,
        })
    late = [r for r in rows if r["date"] > through]
    if late:
        problems.append("%d rows dated after %s" % (len(late), through))
    if len({r["photo_url"] for r in rows}) != len(rows):
        problems.append("a photo appears twice")
    if not rows:
        problems.append("no rows")
    checks.append("rows dated after %s: %d; photos shared with the evaluation manifest (%d rows) and left out: %d" % (
        through, len(late), eval_n, shared))
    with open(out / "manifest.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(COLUMNS)
        for r in rows:
            w.writerow([r[c] for c in COLUMNS])
    log("  wrote %s: %d rows" % (out / "manifest.csv", len(rows)))

    n_per = Counter(str(r["key"]) for r in rows)
    in_list = len(sp["species"])
    L = ["# Training photos: around Alachua County, observations through %s" % through, "",
         "Built by `tools/species/build_train_s3.py` on %s (UTC) from iNaturalist's open-data files%s. %d rows from %d of the list's %d species, at most %d a species." % (
             datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M"),
             (" of " + args.snapshot) if args.snapshot else "", len(rows), len(n_per), in_list, args.cap), "",
         "Rows are in order of each photo's rank within its species, so the first rows hold every species' first photo.", "",
         "The manifest is published only on the branch `pub/data-alachua` as `train/%s/manifest.csv`." % out.name, "",
         "This route differs from the species list's in three ways: the region is a bounding box (latitude 29.42 to 29.95, "
         "longitude -82.66 to -82.05), which takes in a strip of the neighbouring counties; iNaturalist blurs the place of some "
         "threatened species, so a few are missed or misplaced; and species are matched to the list by scientific name, so a "
         "species GBIF files under another name has no training photos here.", "",
         "## Checks", ""] + ["- " + c for c in checks]
    if dup_names:
        L.append("- scientific names carried by two keys in the species list (the more recorded key keeps the photos): %s" % ", ".join(sorted(dup_names)))
    L += ["", "## Photos a species", "", "| photos | species |", "|---|---:|"]
    for lo, hi in ((args.cap, args.cap), (30, args.cap - 1), (10, 29), (5, 9), (2, 4), (1, 1)):
        L.append("| %s | %d |" % ("%d" % lo if lo == hi else "%d to %d" % (lo, hi), sum(1 for v in n_per.values() if lo <= v <= hi)))
    L.append("| none | %d |" % (in_list - len(n_per)))
    for title, col in (("By kind of eye", "eyes"), ("By class", "class"), ("By licence", "licence")):
        L += ["", "## " + title, "", "| %s | rows | share |" % col, "|---|---:|---:|"]
        for v, n in Counter(r[col] or "(none)" for r in rows).most_common(30):
            L.append("| %s | %d | %s |" % (v, n, pct(n, len(rows))))
    L += ["", "## Rows by rank within species", "", "| first rows | cover ranks below |", "|---:|---:|"]
    for cut in (1, 5, 10, 20, 30, 45, args.cap):
        L.append("| %d | %d |" % (sum(1 for r in rows if r["_rank"] < cut), cut))
    missing = sorted(((s["n"], s["sci"], s["en"]) for s in sp["species"] if str(s["key"]) not in n_per), reverse=True)[:30]
    L += ["", "## The most recorded species with no training photo here", "", "| records in the list | species | English name |", "|---:|---|---|"]
    for n, a, e in missing:
        L.append("| %d | *%s* | %s |" % (n, a, e))
    L += ["", "## List species matched through another iNaturalist name", "",
          "From the evaluation photos (see the top of `tools/species/build_train_s3.py`).", "",
          "| GBIF name (list) | iNaturalist name | observations kept | rows |", "|---|---|---:|---:|"]
    rows_by_key = n_per
    for nm, s in sorted(alias.items(), key=lambda t: -via_alias[t[0]]):
        L.append("| *%s* | *%s* | %d | %d |" % (s["sci"], nm, via_alias[nm], rows_by_key.get(str(s["key"]), 0)))
    if args.inat_out:
        Path(args.inat_out).write_text(json.dumps(inat, ensure_ascii=False, sort_keys=True, indent=0) + "\n", encoding="utf-8")
        log("  wrote %s: %d keys" % (args.inat_out, len(inat)))
    if problems:
        L += ["", "## Problems", ""] + ["- " + p for p in problems]
    (out / "SUMMARY.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    log("  wrote %s; %.0fs" % (out / "SUMMARY.md", time.time() - t0))
    if problems:
        log("PROBLEMS:\n  " + "\n  ".join(problems))
        sys.exit(2)
    log("all checks passed")


if __name__ == "__main__":
    main()
