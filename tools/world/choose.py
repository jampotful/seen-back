#!/usr/bin/env python3
"""Choose the world photos for the 33 groups (docs/COVERAGE.md, "World photos"), in two steps around a pass over the
photos file.

Step `pick` reads the candidates that ci/world/world.sh kept while observations.csv.gz streamed past (at most three
research-grade observations of each species on each continent before 2025 and from 2025 on, two casual ones, and a
thin even sample of research-grade observations from 2025 on) and ranks, for each set, more observations than it
needs, so that photos refused by the licence rule can be passed over:

  fit      up to 3,000 a group, dated through 2024
  tune     300 a group, dated 2025 or later
  test     300 a group, dated 2025 or later (tune and test share no observation; a hash of the observation decides)
  casual   up to 300 a group, casual grade (captive or cultivated, or missing evidence), any date
  species  500 a continent, research grade, dated 2025 or later, at most two a species, for the full database's
           world test (every group, chosen by observation and not by group)

Within a group each set is spread evenly across continents (a continent with too few candidates gives its share to
the others), then across orders, then across species, one observation of a species at a time, with at most 30 from
any one observer. The order of everything that is not counted is set by sha256 of a seed and the observation, so a
rerun on the same snapshot chooses the same photos.

Step `finish` reads the photos of the ranked observations and keeps, in rank order, those whose first photo passes
the licence rule `nc` (docs/CONTRACTS.md: CC0, public domain, CC BY, CC BY-NC), up to each set's size, and writes the
manifests and a summary. No names of people are written; an observation's address leads to its observer.

Usage:
  python3 -I tools/world/choose.py pick --cand work/cand.tsv --casual work/casual.tsv --even work/even.tsv \
      --out work/ranked.tsv --uuids work/uuids.txt
  python3 -I tools/world/choose.py finish --ranked work/ranked.tsv --photos work/photos.tsv --taxa work/taxa.csv.gz \
      --counts work/counts.tsv --out stage/world
"""
import argparse
import csv
import gzip
import hashlib
import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from groups import GROUPS as CREATURES  # noqa: E402

GROUPS = CREATURES + ("other",)           # the 33 groups, and what is left in `other` (mites, microbes, water bears)

SEED = "seen-back/world/v1"
SIZES = {"fit": 3000, "tune": 300, "test": 300, "casual": 300}
SPECIES_TEST = 500                       # a continent
OVER = 1.6                               # ranked a set, for each photo it needs
OBSERVER_CAP = 30
CONTINENTS = ("AF", "AS", "EU", "NA", "OC", "SA", "AN")
ALLOWED = {"cc0", "pd", "cc-by", "cc-by-nc"}
COLUMNS = ["set", "group", "continent", "inat_taxon", "sci", "rank", "order", "class", "phylum", "kingdom",
           "date", "obs_url", "photo_url", "licence"]


def h(*parts):
    return hashlib.sha256(("|".join([SEED] + [str(p) for p in parts])).encode()).hexdigest()


def read_rows(path, names):
    with open(path, encoding="utf-8") as f:
        for line in f:
            v = line.rstrip("\n").split("\t")
            if len(v) == len(names):
                yield dict(zip(names, v))


CAND = ["grade", "group", "continent", "period", "order", "unit", "taxon", "uuid", "observer", "date"]


def spread(cands, size, key):
    """Rank up to size * OVER candidates: even across continents, then orders, then species, one at a time."""
    want = int(round(size * OVER))
    by_cont = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for c in cands:
        by_cont[c["continent"]][c["order"]][c["unit"]].append(c)
    avail = {k: sum(len(u) for o in v.values() for u in o.values()) for k, v in by_cont.items()}
    # equal shares across continents; a continent short of its share passes the rest on
    share = {k: 0 for k in avail}
    left, open_ = want, sorted(avail, key=lambda k: h(key, "c", k))
    while left > 0 and open_:
        each = max(1, left // len(open_))
        moved = False
        for k in list(open_):
            take = min(each, avail[k] - share[k], left)
            if take > 0:
                share[k] += take; left -= take; moved = True
            if avail[k] - share[k] <= 0:
                open_.remove(k)
            if left <= 0:
                break
        if not moved:
            break
    picked, observers = [], Counter()
    for k in sorted(share, key=lambda k: h(key, "c", k)):
        queues = []
        for o in sorted(by_cont[k], key=lambda o: h(key, "o", k, o)):
            units = by_cont[k][o]
            lists = [sorted(units[u], key=lambda c: h(key, c["uuid"])) for u in sorted(units, key=lambda u: h(key, "u", k, u))]
            q = [lst[d] for d in range(max(len(l) for l in lists)) for lst in lists if d < len(lst)]
            queues.append(q)
        got, pos = 0, [0] * len(queues)
        while got < share[k]:
            moved = False
            for qi, q in enumerate(queues):
                if got >= share[k]:
                    break
                while pos[qi] < len(q):
                    c = q[pos[qi]]; pos[qi] += 1
                    if observers[c["observer"]] < OBSERVER_CAP:
                        observers[c["observer"]] += 1
                        picked.append(((got + 0.5) / share[k], h(key, "c", k), c)); got += 1; moved = True
                        break
            if not moved:
                break
    # continents interleaved in proportion to their shares, so that any prefix of the ranking is spread as the whole is
    picked.sort(key=lambda t: (t[0], t[1]))
    return [t[2] for t in picked]


def pick(args):
    by_group = defaultdict(lambda: defaultdict(list))
    n = Counter()
    for c in read_rows(args.cand, CAND):
        n[c["period"]] += 1
        if c["group"] not in GROUPS:
            continue
        if c["period"] == "F":
            by_group[c["group"]]["fit"].append(c)
        elif c["period"] == "E":
            s = "tune" if int(h("split", c["uuid"])[:8], 16) % 2 == 0 else "test"
            by_group[c["group"]][s].append(c)
    for c in read_rows(args.casual, CAND):
        n["casual"] += 1
        if c["group"] in GROUPS:
            by_group[c["group"]]["casual"].append(c)
    print("candidates: %s" % dict(n), flush=True)
    ranked = []
    for g in GROUPS:
        for s, size in SIZES.items():
            chosen = spread(by_group[g][s], size, "%s/%s" % (g, s))
            for i, c in enumerate(chosen):
                ranked.append((s, g, i, c))
        print("%-11s %s" % (g, "  ".join("%s %d" % (s, sum(1 for r in ranked if r[0] == s and r[1] == g)) for s in SIZES)), flush=True)
    # the full database's world test: an even sample of observations, at most two a species, on each continent
    even = defaultdict(list)
    for c in read_rows(args.even, CAND):
        even[c["continent"]].append(c)
    for k in CONTINENTS:
        lst = sorted(even[k], key=lambda c: h("species", c["uuid"]))
        per, i = Counter(), 0
        for c in lst:
            if per[c["unit"]] >= 2:
                continue
            per[c["unit"]] += 1
            ranked.append(("species", c["group"], i, c)); i += 1
            if i >= int(SPECIES_TEST * OVER):
                break
        print("species test %s: %d ranked of %d" % (k, i, len(lst)), flush=True)
    with open(args.out, "w", encoding="utf-8") as out, open(args.uuids, "w", encoding="utf-8") as u:
        seen = set()
        for s, g, i, c in ranked:
            out.write("\t".join([s, g, str(i)] + [c[k] for k in CAND]) + "\n")
            if c["uuid"] not in seen:
                seen.add(c["uuid"]); u.write(c["uuid"] + "\n")
    print("ranked rows: %d, observations: %d" % (len(ranked), len(seen)))


def norm_licence(s):
    s = (s or "").strip().lower().replace("_", "-")
    return {"cc0": "cc0", "pd": "pd", "public domain": "pd", "cc-by": "cc-by", "cc-by-nc": "cc-by-nc"}.get(s, s)


def finish(args):
    first = {}                                     # observation -> (position, photo id, extension, licence)
    with open(args.photos, encoding="utf-8") as f:
        head = f.readline().rstrip("\n").split("\t")
        col = {k: i for i, k in enumerate(head)}
        for line in f:
            v = line.rstrip("\n").split("\t")
            if len(v) < len(head):
                continue
            u = v[col["observation_uuid"]]
            try:
                pos = int(v[col["position"]] or 0)
            except ValueError:
                pos = 0
            cur = first.get(u)
            pid = v[col["photo_id"]]
            if cur is None or (pos, int(pid) if pid.isdigit() else 0) < (cur[0], int(cur[1]) if cur[1].isdigit() else 0):
                first[u] = (pos, pid, v[col["extension"]], v[col["license"]])
    print("observations with photos: %d" % len(first), flush=True)
    need = set()
    rows = []
    with open(args.ranked, encoding="utf-8") as f:
        for line in f:
            v = line.rstrip("\n").split("\t")
            s, g, i = v[0], v[1], int(v[2])
            c = dict(zip(CAND, v[3:]))
            rows.append((s, g, i, c)); need.add(int(c["taxon"]))
    name, rank, anc = {}, {}, {}
    opener = gzip.open if args.taxa.endswith(".gz") else open
    with opener(args.taxa, "rt", encoding="utf-8", newline="") as f:
        r = csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        hd = next(r); col = {k: i for i, k in enumerate(hd)}
        for v in r:
            if len(v) < len(hd):
                continue
            t = int(v[col["taxon_id"]])
            name[t], rank[t] = v[col["name"]], v[col["rank"]]
            anc[t] = [int(a) for a in v[col["ancestry"]].split("/") if a.isdigit()]

    def lineage(t):
        out = {}
        for a in anc.get(t, []) + [t]:
            if rank.get(a) in ("kingdom", "phylum", "class", "order"):
                out[rank[a]] = name[a]
        return out

    target = dict(SIZES); kept = Counter(); refused = Counter(); nophoto = Counter(); lic = Counter(); shared = Counter()
    sets = defaultdict(list); used = set()
    for s, g, i, c in sorted(rows, key=lambda r: (r[0], r[1] if r[0] != "species" else r[3]["continent"], r[2])):
        k = (s, g if s != "species" else c["continent"])
        cap = SPECIES_TEST if s == "species" else target[s]
        if kept[k] >= cap:
            continue
        p = first.get(c["uuid"])
        if p is None:
            nophoto[k] += 1; continue
        l = norm_licence(p[3])
        if l not in ALLOWED:
            refused[k] += 1; continue
        if s != "species":
            if p[1] in used:
                shared[k] += 1; continue
            used.add(p[1])
        kept[k] += 1; lic[l] += 1
        t = int(c["taxon"]); ln = lineage(t)
        sets[s].append({"set": s, "group": g, "continent": c["continent"], "inat_taxon": t, "sci": name.get(t, ""),
                        "rank": rank.get(t, ""), "order": ln.get("order", ""), "class": ln.get("class", ""),
                        "phylum": ln.get("phylum", ""), "kingdom": ln.get("kingdom", ""), "date": c["date"],
                        "obs_url": "https://www.inaturalist.org/observations/%s" % c["uuid"],
                        "photo_url": "https://inaturalist-open-data.s3.amazonaws.com/photos/%s/medium.%s" % (p[1], p[2]),
                        "licence": l.upper()})
    os.makedirs(args.out, exist_ok=True)
    for s, lst in sets.items():
        with open(os.path.join(args.out, "%s.csv" % s), "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS); w.writeheader(); w.writerows(lst)
    # the same rows in the laboratory's form (tools/lab/lab.py reads `id`, `photo_url` and `split`): one manifest for
    # fitting, one for tuning, testing and casual photos (tune and test share split `eval`, for the WASM vectors), and
    # one for the species test
    for name, parts in (("world-fit", ("fit",)), ("world-eval", ("tune", "test", "casual")), ("world-species", ("species",))):
        d = os.path.join(args.out, "lab", name); os.makedirs(d, exist_ok=True)
        seen = set()
        with open(os.path.join(d, "manifest.csv"), "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["id", "split"] + COLUMNS); w.writeheader()
            for part in parts:
                for r in sets.get(part, []):
                    pid = "w" + r["photo_url"].split("/photos/")[1].split("/")[0]
                    if pid in seen:
                        continue
                    seen.add(pid)
                    w.writerow(dict(r, id=pid, split="eval" if part in ("tune", "test") else part))
    urls = Counter(r["photo_url"] for k, lst in sets.items() if k != "species" for r in lst)
    dup = sum(1 for n in urls.values() if n > 1)
    both = len({r["photo_url"] for r in sets.get("species", [])} & set(urls))
    # the summary
    counts = defaultdict(dict)
    if args.counts and os.path.exists(args.counts):
        for v in read_rows(args.counts, ["group", "continent", "period", "n"]):
            counts[v["group"]][(v["continent"], v["period"])] = int(v["n"])
    L = ["# World photos", "", "Made by `tools/world/choose.py` from iNaturalist's open-data snapshot (%s). Seed `%s`." % (args.snapshot or "date not given", SEED), ""]
    L.append("Sets: fit up to %d a group (dated through 2024), tune and test %d a group each (2025 on), casual up to %d a group, and %d research-grade photos a continent from 2025 on for the full database's world test. Licence rule `nc`: %s." % (SIZES["fit"], SIZES["tune"], SIZES["casual"], SPECIES_TEST, ", ".join(sorted(ALLOWED))))
    L.append("")
    L.append("| Group | fit | tune | test | casual | research-grade records, all time | species in fit | orders in fit | continents in fit |")
    L.append("|---|---:|---:|---:|---:|---:|---:|---:|---|")
    for g in GROUPS:
        fit = [r for r in sets.get("fit", []) if r["group"] == g]
        rec = sum(n for (k, p), n in counts[g].items() if p in ("F", "E"))
        conts = Counter(r["continent"] for r in fit)
        L.append("| %s | %d | %d | %d | %d | %s | %d | %d | %s |" % (
            g, kept[("fit", g)], kept[("tune", g)], kept[("test", g)], kept[("casual", g)], format(rec, ","),
            len({r["inat_taxon"] for r in fit}), len({r["order"] for r in fit}),
            " ".join("%s %d" % (k, conts[k]) for k in CONTINENTS if conts[k])))
    L.append("")
    L.append("| Continent | species test photos |")
    L.append("|---|---:|")
    for k in CONTINENTS:
        L.append("| %s | %d |" % (k, kept[("species", k)]))
    L.append("")
    L.append("Licences kept: %s. Ranked observations passed over for a licence outside the rule: %d; for no photo in the file: %d; for a photo already taken by another group's observation: %d. Photos in two of the group sets: %d. Photos in both the species test and a group set: %d (the two tests measure different models)." % (
        ", ".join("%s %d" % (k, v) for k, v in lic.most_common()), sum(refused.values()), sum(nophoto.values()), sum(shared.values()), dup, both))
    short = ["%s/%s %d of %d" % (k[0], k[1], kept[k], (SPECIES_TEST if k[0] == "species" else target[k[0]]))
             for k in sorted(set(list(kept) + list(refused) + list(nophoto)))
             if kept[k] < (SPECIES_TEST if k[0] == "species" else target[k[0]])]
    if short:
        L.append("")
        L.append("Sets short of their size: %s." % "; ".join(short))
    open(os.path.join(args.out, "SUMMARY.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    json.dump({"%s/%s" % k: v for k, v in kept.items()}, open(os.path.join(args.out, "counts.json"), "w"), indent=0, sort_keys=True)
    print("\n".join(L))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("pick")
    a.add_argument("--cand", required=True); a.add_argument("--casual", required=True); a.add_argument("--even", required=True)
    a.add_argument("--out", required=True); a.add_argument("--uuids", required=True)
    b = sub.add_parser("finish")
    b.add_argument("--ranked", required=True); b.add_argument("--photos", required=True); b.add_argument("--taxa", required=True)
    b.add_argument("--counts", default=""); b.add_argument("--out", required=True); b.add_argument("--snapshot", default="")
    args = ap.parse_args()
    pick(args) if args.cmd == "pick" else finish(args)


if __name__ == "__main__":
    main()
