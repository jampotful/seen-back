#!/usr/bin/env python3
"""The species people photograph at home (docs/tracks/prompts/burst13-everyday.md; tools/species/EVERYDAY.md).

Two steps, each run on a build machine through .github/workflows/everyday.yml:

  resolve  For every query of tools/species/everyday_list.csv: GBIF's match (key, scientific name, rank, status,
           lineage) from api.gbif.org, the app's kind of eye from that lineage (tools/species/eyes.py), the
           iNaturalist taxon and its English name, the number of iNaturalist observations marked captive or
           cultivated, and up to --photos of their photos under the licence rule nc, at most --per-observer from one
           person, split by observation id into tune (one in three) and test. Writes species.csv, photos.csv and
           summary.json to --out.
  build    Run by tools/species/everyday_build.py (the text rows, the extended slot and the measurements).

Nothing is taken from memory: the queries are names to look up, and every key, name, rank and lineage written out is
the one GBIF returned. A query GBIF cannot match, or matches only above the genus, is left out and said so.

Usage: python3 -I tools/species/everyday.py resolve --out DIR [--photos 30] [--per-observer 3] [--limit N]
"""
import argparse
import csv
import json
import os
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import eyes  # noqa: E402

UA = "seen-back-everyday/1 (research; github.com/jampotful/seen-back)"
GBIF = "https://api.gbif.org/v1/"
INAT = "https://api.inaturalist.org/v1/"
LICENCES = "cc0,cc-by,cc-by-nc"
_last = {"inat": 0.0}


def get(url, tries=5, pause=0.0, kind=None):
    if kind == "inat":                                   # iNaturalist asks for about one request a second
        wait = 1.05 - (time.time() - _last["inat"])
        if wait > 0:
            time.sleep(wait)
    err = None
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read()
            if kind == "inat":
                _last["inat"] = time.time()
            return json.loads(body.decode("utf-8"))
        except Exception as e:                           # noqa: BLE001 - every failure is retried, then said
            err = e
            if kind == "inat":
                _last["inat"] = time.time()
            time.sleep(min(60, 3 * (2 ** k)) + pause)
    raise IOError("%s: %s" % (url, err))


def gbif_match(name, kingdom):
    q = urllib.parse.urlencode({"name": name, "kingdom": kingdom, "verbose": "false"})
    return get(GBIF + "species/match?" + q)


def inat_taxon(names):
    """The iNaturalist taxon whose name is one of `names` (in that order), active, at species rank or below, or the
    genus when that is what the name is."""
    for nm in names:
        if not nm:
            continue
        j = get(INAT + "taxa?" + urllib.parse.urlencode({"q": nm, "per_page": 30, "locale": "en"}), kind="inat")
        want = nm.replace("× ", "").replace("×", "").lower()
        for t in j.get("results", []):
            got = (t.get("name") or "").replace("× ", "").replace("×", "").lower()
            if got == want and t.get("is_active", True):
                return t
    return None


def observations(taxon_id, n, per_observer):
    """The newest observations of the taxon marked captive or cultivated with a photo under the licence rule nc: the
    count of every such observation (any licence), and up to n photos, at most per_observer from one person."""
    base = {"taxon_id": taxon_id, "captive": "true", "locale": "en"}
    count = get(INAT + "observations?" + urllib.parse.urlencode(dict(base, per_page=0)), kind="inat").get("total_results", 0)
    out, by, page = [], {}, 1
    while len(out) < n and page <= 3:
        j = get(INAT + "observations?" + urllib.parse.urlencode(dict(base, photos="true", photo_license=LICENCES, per_page=100,
                                                                      order_by="id", order="desc", page=page)), kind="inat")
        res = j.get("results", [])
        for o in res:
            ph = (o.get("photos") or [None])[0]
            who = (o.get("user") or {}).get("id")
            if not ph or not ph.get("url") or (ph.get("license_code") or "").lower() not in LICENCES.split(","):
                continue
            if by.get(who, 0) >= per_observer:
                continue
            by[who] = by.get(who, 0) + 1
            loc = (o.get("location") or ",").split(",")
            out.append({"obs": o["id"], "photo_url": ph["url"].replace("/square.", "/medium."),
                        "licence": ph.get("license_code") or "", "zone": o.get("observed_time_zone") or o.get("time_zone") or "",
                        "lat": loc[0] if len(loc) == 2 else "", "lon": loc[1] if len(loc) == 2 else "",
                        "date": o.get("observed_on") or "", "inat_taxon": (o.get("taxon") or {}).get("id", "")})
            if len(out) >= n:
                break
        if len(res) < 100:
            break
        page += 1
    return count, out


def resolve(a):
    os.makedirs(a.out, exist_ok=True)
    rows = list(csv.DictReader(open(os.path.join(HERE, "everyday_list.csv"), encoding="utf-8")))
    if a.limit:
        rows = rows[:a.limit]
    total = get(INAT + "observations?per_page=0", kind="inat").get("total_results", 0)
    species, photos, dropped, seen = [], [], [], {}
    t0 = time.time()
    for i, r in enumerate(rows):
        q = r["query"]
        try:
            m = gbif_match(q, r["kingdom"])
        except IOError as e:
            dropped.append({"query": q, "why": "GBIF did not answer: %s" % e})
            continue
        mt, rank = m.get("matchType", "NONE"), (m.get("rank") or "").upper()
        if mt == "NONE" or rank not in ("SPECIES", "SUBSPECIES", "VARIETY", "FORM", "GENUS") or not m.get("usageKey"):
            dropped.append({"query": q, "why": "GBIF match %s at rank %s" % (mt, rank or "none")})
            continue
        key, sci = int(m["usageKey"]), m.get("canonicalName") or m.get("scientificName")
        if key in seen:
            dropped.append({"query": q, "why": "GBIF gives the same key as %s" % seen[key]})
            continue
        seen[key] = q
        kind = eyes.kind_or_group(m.get("kingdom"), m.get("phylum"), m.get("class"), m.get("order"), m.get("family"), m.get("genus"))
        try:
            t = inat_taxon([q, sci])
        except IOError as e:
            t = None
            print("iNaturalist taxa failed for %s: %s" % (q, e), flush=True)
        en, tid, count, ph = "", "", 0, []
        if t:
            tid, en = t["id"], t.get("preferred_common_name") or ""
            try:
                count, ph = observations(tid, a.photos, a.per_observer)
            except IOError as e:
                print("iNaturalist observations failed for %s: %s" % (q, e), flush=True)
        species.append({"query": q, "category": r["category"], "gbif_key": key, "sci": sci, "rank": rank,
                        "status": m.get("status", ""), "match": mt, "confidence": m.get("confidence", ""),
                        "accepted_key": m.get("acceptedUsageKey", "") or "", "kingdom": m.get("kingdom", ""),
                        "phylum": m.get("phylum", ""), "class": m.get("class", ""), "order": m.get("order", ""),
                        "family": m.get("family", ""), "genus": m.get("genus", ""), "kind": kind,
                        "inat_taxon": tid, "inat_name": (t or {}).get("name", ""), "en": en,
                        "captive_obs": count, "photos": len(ph)})
        for p in ph:
            p.update({"id": "e%d" % p["obs"], "set": "tune" if p["obs"] % 3 == 0 else "test", "gbif_key": key, "sci": sci,
                      "kind": kind, "category": r["category"], "obs_url": "https://www.inaturalist.org/observations/%d" % p["obs"]})
            photos.append(p)
        print("%3d/%d %-32s -> %s %s (%s, %s) kind %s, iNat %s %r, captive %s, photos %d (%.0fs)" % (
            i + 1, len(rows), q, key, sci, rank, m.get("status", ""), kind, tid, en, count, len(ph), time.time() - t0), flush=True)
    sf = ["query", "category", "gbif_key", "sci", "rank", "status", "match", "confidence", "accepted_key", "kingdom", "phylum",
          "class", "order", "family", "genus", "kind", "inat_taxon", "inat_name", "en", "captive_obs", "photos"]
    with open(os.path.join(a.out, "species.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=sf)
        w.writeheader()
        w.writerows(species)
    pf = ["id", "set", "gbif_key", "sci", "kind", "category", "inat_taxon", "obs_url", "photo_url", "licence", "zone", "lat", "lon", "date"]
    with open(os.path.join(a.out, "photos.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=pf, extrasaction="ignore")
        w.writeheader()
        w.writerows(photos)
    summ = {"queries": len(rows), "species": len(species), "dropped": dropped, "photos": len(photos),
            "tune": sum(p["set"] == "tune" for p in photos), "test": sum(p["set"] == "test" for p in photos),
            "inat_observations_all": total, "licences": LICENCES, "per_observer": a.per_observer,
            "by_kind": {}, "by_category": {}, "seconds": round(time.time() - t0)}
    for s in species:
        summ["by_kind"][s["kind"]] = summ["by_kind"].get(s["kind"], 0) + 1
        summ["by_category"][s["category"]] = summ["by_category"].get(s["category"], 0) + 1
    json.dump(summ, open(os.path.join(a.out, "summary.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in summ.items() if k != "dropped"}, indent=1))
    print("dropped:", json.dumps(dropped, indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("resolve")
    r.add_argument("--out", required=True)
    r.add_argument("--photos", type=int, default=30)
    r.add_argument("--per-observer", type=int, default=3)
    r.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    if a.cmd == "resolve":
        resolve(a)


if __name__ == "__main__":
    main()
