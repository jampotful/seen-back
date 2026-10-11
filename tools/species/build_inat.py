#!/usr/bin/env python3
"""Write data/regions/<region>/inat.json (format: docs/CONTRACTS.md): for each species-list key, the iNaturalist taxon
its records are filed under, with iNaturalist's preferred English name.

GBIF files some species under names iNaturalist does not use (GBIF's Grus canadensis is iNaturalist's Antigone
canadensis). The species list keeps GBIF's names, because the biology models were trained on them; the name shown to
a person follows iNaturalist. Two sources, in this order:

1. The evaluation manifest: each row carries a GBIF species key and an iNaturalist observation id. The observations
   are looked up in iNaturalist's API (/v1/observations, 200 ids a request, about one request a second) for the taxon
   each sits under today; a subspecies counts as its species. For each key: the species most often attached, its share
   of the key's observations that were found (`share`) and how many that is (`n`); "via": "observations".
2. Keys with no evaluation observation: iNaturalist's taxonomy archive joined by exact scientific name at rank species
   (the join behind the species list's English names); `share` is null, `n` 0, "via": "name". A key whose GBIF name
   iNaturalist does not use, and which has no evaluation observation, gets no entry.

English names: for every taxon whose name differs from GBIF's, iNaturalist's preferred English name (locale en,
preferred place Florida) through names.api_preferred; for the others the species list's `en` where it came from the
same API (`en_source` inat-api), else the archive's name the species list used, else empty.

Usage: python3 tools/species/build_inat.py [--out data/regions/us-fl-alachua/inat.json] [--cache work]
"""
import argparse
import csv
import json
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
import names  # noqa: E402
from common import UA, log  # noqa: E402

INFRA = ("subspecies", "variety", "form", "infrahybrid")
FLORIDA = 21


def species_level(t):
    """(id, name) of the species an observation's taxon belongs to, or ('', '') above species."""
    rank = (t.get("rank") or "").lower()
    tid, name = str(t.get("id") or ""), t.get("name") or ""
    if rank in ("species", "hybrid"):
        return tid, name
    if rank in INFRA:
        sid = str(t.get("min_species_taxon_id") or "")
        anc = [str(a) for a in (t.get("ancestor_ids") or [])]
        if not sid and anc:
            anc = anc[:-1] if anc[-1] == tid else anc
            sid = anc[-1] if anc else ""
        return sid, " ".join(name.split()[:2])
    return "", ""


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--region-dir", default="data/regions/us-fl-alachua")
    ap.add_argument("--eval", default="data/eval/alachua-2025/manifest.csv")
    ap.add_argument("--out", default="data/regions/us-fl-alachua/inat.json")
    ap.add_argument("--cache", default="work")
    ap.add_argument("--report", default="", help="also write a short Markdown report here")
    a = ap.parse_args()
    t0 = time.time()
    sp = json.loads((Path(a.region_dir) / "species.json").read_text(encoding="utf-8"))
    lst = {str(s["key"]): s for s in sp["species"]}

    obs_key = {}
    for r in csv.DictReader(open(a.eval, encoding="utf-8")):
        m = re.search(r"/observations/(\d+)", r["obs_url"])
        if m and r["key"] in lst:
            obs_key[m.group(1)] = r["key"]
    ids = sorted(obs_key, key=int)
    log("== %d evaluation observations of %d keys" % (len(ids), len(set(obs_key.values()))))
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept": "application/json"})
    found, codes = {}, Counter()
    for k in range(0, len(ids), 200):
        chunk = ids[k:k + 200]
        for attempt in range(1, 5):
            try:
                r = s.get("https://api.inaturalist.org/v1/observations",
                          params={"id": ",".join(chunk), "per_page": 200, "locale": "en", "preferred_place_id": FLORIDA},
                          timeout=60)
                codes[r.status_code] += 1
                if r.status_code == 200:
                    for o in r.json().get("results", []):
                        found[str(o.get("id"))] = o.get("taxon") or {}
                    break
                ra = r.headers.get("Retry-After", "")
                time.sleep(min(60, int(ra)) if ra.isdigit() else 10 * attempt)
            except (requests.RequestException, ValueError) as e:
                codes[type(e).__name__] += 1
                time.sleep(10 * attempt)
        time.sleep(1.0)
    log("  found %d of %d observations; statuses %s" % (len(found), len(ids), dict(codes)))

    tally = defaultdict(Counter)
    payload_en = {}
    above = 0
    for oid, t in found.items():
        sid, nm = species_level(t)
        if not nm:
            above += 1
            continue
        tally[obs_key[oid]][(sid, nm)] += 1
        if str(t.get("id")) == sid and t.get("preferred_common_name"):
            payload_en[sid] = t["preferred_common_name"]
    out = {}
    for key, c in tally.items():
        (sid, nm), k = c.most_common(1)[0]
        tot = sum(c.values())
        out[key] = {"inat_id": int(sid) if sid.isdigit() else 0, "sci": nm, "en": "", "share": round(k / tot, 3),
                    "n": tot, "via": "observations"}
    log("  keys from observations: %d (observations identified above species: %d)" % (len(out), above))

    rest = {lst[k]["sci"]: lst[k].get("kingdom", "") for k in lst if k not in out}
    arch_names, arch_taxa = {}, {}
    try:
        arch = names.ensure_archive(a.cache)
        arch_names, rep, arch_taxa = names.english_names(arch, rest)
        log("  taxonomy archive: %s" % rep)
    except Exception as e:  # the observations still give the entries that matter most
        log("  taxonomy archive unavailable (%s); keys without evaluation observations get no entry" % e)
    by_name = 0
    for k in lst:
        if k in out:
            continue
        t = arch_taxa.get(lst[k]["sci"])
        if t and str(t.get("id", "")).isdigit():
            out[k] = {"inat_id": int(t["id"]), "sci": lst[k]["sci"], "en": "", "share": None, "n": 0, "via": "name"}
            by_name += 1
    log("  keys from the archive by exact name: %d; keys with no entry: %d" % (by_name, len(lst) - len(out)))

    differ = sorted({str(v["inat_id"]) for k, v in out.items() if v["sci"] != lst[k]["sci"] and v["inat_id"]}, key=int)
    api = names.api_preferred(differ, place_id=FLORIDA) if differ else {}
    log("  English names asked for %d taxa whose name differs from GBIF's; answered %d" % (len(differ), len(api)))
    src = Counter()
    for k, v in out.items():
        sid = str(v["inat_id"])
        if v["sci"] != lst[k]["sci"]:
            v["en"] = api.get(sid) or payload_en.get(sid, "")
            src["differs: " + ("api" if api.get(sid) else "observation payload" if payload_en.get(sid) else "none")] += 1
        elif lst[k].get("en_source") == "inat-api":
            v["en"] = lst[k].get("en", "")
            src["same name: species list (inat-api)"] += 1
        else:
            v["en"] = payload_en.get(sid) or arch_names.get(v["sci"], "")
            src["same name: " + ("observation payload" if payload_en.get(sid) else "archive" if arch_names.get(v["sci"]) else "none")] += 1
    log("  English name sources: %s" % dict(src))
    outp = Path(a.out)
    outp.parent.mkdir(parents=True, exist_ok=True)
    keys = sorted(out, key=lambda k: -lst[k]["n"])
    outp.write_text("{\n" + ",\n".join('"%s": %s' % (k, json.dumps(out[k], ensure_ascii=False, sort_keys=True)) for k in keys)
                    + "\n}\n", encoding="utf-8")
    json.loads(outp.read_text(encoding="utf-8"))
    log("  wrote %s: %d keys; %.0fs" % (outp, len(out), time.time() - t0))

    if a.report:
        dif = [(lst[k]["n"], lst[k]["sci"], lst[k]["en"], out[k]["sci"], out[k]["en"], out[k]["share"], out[k]["n"])
               for k in keys if out[k]["sci"] != lst[k]["sci"]]
        L = ["# iNaturalist's names for the species list", "",
             "Made by `tools/species/build_inat.py` (UTC %s): %d of the list's %d keys have an entry, %d from the evaluation "
             "observations as iNaturalist files them today and %d by exact name in iNaturalist's taxonomy archive. "
             "%d keys sit under another name on iNaturalist; the forty most recorded:" % (
                 time.strftime("%Y-%m-%d %H:%M", time.gmtime()), len(out), len(lst), len(out) - by_name, by_name, len(dif)),
             "", "| records | GBIF name (list) | list's English name | iNaturalist name | iNaturalist's English name | share | observations |",
             "|---:|---|---|---|---|---:|---:|"]
        for row in dif[:40]:
            L.append("| %d | *%s* | %s | *%s* | %s | %s | %d |" % row)
        Path(a.report).write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
