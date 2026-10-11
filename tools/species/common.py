"""Shared pieces for the species-list and evaluation builders: a polite GBIF client, taxonomy and names.

Standard library plus `requests`. Every request names this repository in its User-Agent, retries with
exponential backoff (honouring Retry-After), and callers bound concurrency with a small thread pool.
"""
import concurrent.futures as cf
import hashlib
import json
import random
import re
import sys
import threading
import time
from collections import Counter
from pathlib import Path

import requests

UA = "seen-back-data/1 (+https://github.com/jampotful/seen-back; species lists and evaluation sets)"
API = "https://api.gbif.org/v1"
INAT_DATASET = "50c9509d-22c7-4a22-a47d-8c48425ef4a7"

_local = threading.local()
_stats = Counter()
_stats_lock = threading.Lock()


def log(*a):
    print(*a, flush=True)


def stats():
    with _stats_lock:
        return dict(_stats)


def _bump(key, n=1):
    with _stats_lock:
        _stats[key] += n


def session():
    s = getattr(_local, "s", None)
    if s is None:
        s = requests.Session()
        s.headers.update({"User-Agent": UA, "Accept": "application/json"})
        _local.s = s
    return s


def get_json(path_or_url, params=None, tries=7, timeout=90, allow_404=False):
    """GET a GBIF API path (or a full address) and return the parsed JSON."""
    url = path_or_url if path_or_url.startswith("http") else API + path_or_url
    delay = 2.0
    last = None
    for attempt in range(1, tries + 1):
        wait = delay
        try:
            r = session().get(url, params=params, timeout=timeout)
            _bump("requests")
            if r.status_code == 200:
                return r.json()
            if r.status_code == 404 and allow_404:
                return None
            last = "HTTP %s: %s" % (r.status_code, r.text[:200].replace("\n", " "))
            if r.status_code in (408, 429, 500, 502, 503, 504):
                _bump("retry_http_%s" % r.status_code)
                ra = r.headers.get("Retry-After", "")
                if ra.isdigit():
                    wait = max(wait, float(ra))
            else:
                raise RuntimeError("%s -> %s" % (r.url, last))
        except (requests.ConnectionError, requests.Timeout, requests.exceptions.ChunkedEncodingError, ValueError) as e:
            _bump("retry_exception")
            last = "%s: %s" % (type(e).__name__, e)
        if attempt < tries:
            time.sleep(wait + random.random())
            delay = min(delay * 2, 90)
    raise RuntimeError("gave up on %s %s after %d tries: %s" % (url, params or "", tries, last))


def pmap(fn, items, workers=6, desc="", every=500):
    """Apply fn to items with a bounded thread pool; return results in the order of items."""
    items = list(items)
    out = [None] * len(items)
    t0 = time.time()
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(fn, it): i for i, it in enumerate(items)}
        done = 0
        for f in cf.as_completed(futs):
            out[futs[f]] = f.result()
            done += 1
            if desc and (done % every == 0 or done == len(items)):
                log("  %s: %d/%d (%.0fs)" % (desc, done, len(items), time.time() - t0))
    return out


class JsonCache:
    """A directory of JSON answers keyed by a string, so a second builder in the same job does not refetch."""

    def __init__(self, root):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, key):
        h = hashlib.sha1(key.encode()).hexdigest()
        return self.root / h[:2] / (h + ".json")

    def get(self, key, make):
        p = self._path(key)
        if p.exists():
            try:
                return json.loads(p.read_text(encoding="utf-8"))
            except ValueError:
                pass
        val = make()
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_suffix(".tmp%d" % threading.get_ident())
        tmp.write_text(json.dumps(val), encoding="utf-8")
        tmp.replace(p)
        return val


def facet_all(params, field="speciesKey", page=1000):
    """All facet values of `field` for an occurrence search, paging with facetOffset.

    Advances by the number of values actually returned (in case the server caps facetLimit) and stops at an
    empty page. Returns (counts dict name->count, total record count of the query, pages fetched, duplicates).
    """
    out, off, pages, dups, total = {}, 0, 0, 0, None
    while True:
        q = dict(params, limit=0, facet=field, facetLimit=page, facetOffset=off)
        r = get_json("/occurrence/search", q)
        pages += 1
        total = r.get("count")
        facets = r.get("facets") or []
        counts = facets[0].get("counts", []) if facets else []
        if not counts:
            break
        for c in counts:
            if c["name"] in out:
                dups += 1
            out[c["name"]] = c["count"]
        off += len(counts)
        if pages > 500:
            raise RuntimeError("facet paging did not end")
    return out, total, pages, dups


def count(params):
    return get_json("/occurrence/search", dict(params, limit=0))["count"]


def species_info(key, cache):
    """Backbone record of a species key: canonical name, ranks and status."""
    def make():
        r = get_json("/species/%s" % key, allow_404=True)
        if r is None:
            return {"key": key, "missing": True}
        keep = ("key", "nubKey", "scientificName", "canonicalName", "rank", "taxonomicStatus", "acceptedKey",
                "kingdom", "phylum", "class", "order", "family", "genus", "species", "speciesKey", "vernacularName")
        return {k: r.get(k) for k in keep if k in r}
    return cache.get("species/%s" % key, make)


def gbif_vernacular(key, cache):
    """English names GBIF holds for a species key (name, source, preferred flag), in GBIF's order."""
    def make():
        names, off = [], 0
        while True:
            r = get_json("/species/%s/vernacularNames" % key, {"limit": 1000, "offset": off}, allow_404=True)
            if not r:
                break
            for v in r.get("results", []):
                if (v.get("language") or "").lower() in ("eng", "en", "english"):
                    names.append({"name": v.get("vernacularName"), "source": v.get("source"),
                                  "preferred": bool(v.get("preferred")), "country": v.get("country")})
            if r.get("endOfRecords", True) or not r.get("results"):
                break
            off += len(r["results"])
        return names
    return cache.get("vernacular/%s" % key, make)


def choose_gbif_english(names):
    """Pick one English name from GBIF's list.

    A name flagged `preferred` wins (the first such, preferring one with country US or no country); otherwise
    the name given by the most sources (compared case-insensitively, ties to the first seen), written in the
    casing most often used for it. Returns '' when there is none.
    """
    names = [n for n in names if n.get("name") and n["name"].strip()]
    if not names:
        return ""
    pref = [n for n in names if n.get("preferred")]
    if pref:
        pref.sort(key=lambda n: 0 if (n.get("country") in (None, "", "US")) else 1)
        return pref[0]["name"].strip()
    folded = Counter()
    first = {}
    forms = {}
    for i, n in enumerate(names):
        f = re.sub(r"\s+", " ", n["name"].strip()).casefold()
        folded[f] += 1
        first.setdefault(f, i)
        forms.setdefault(f, Counter())[n["name"].strip()] += 1
    best = sorted(folded, key=lambda f: (-folded[f], first[f]))[0]
    return forms[best].most_common(1)[0][0]


def scrub_occurrence(rec):
    """A copy of an occurrence record with only the fields this project reads: no names of people."""
    keep = ("key", "datasetKey", "basisOfRecord", "catalogNumber", "occurrenceID", "references", "taxonKey",
            "speciesKey", "acceptedTaxonKey", "scientificName", "acceptedScientificName", "taxonRank",
            "taxonomicStatus", "kingdom", "phylum", "class", "order", "family", "genus", "species",
            "kingdomKey", "phylumKey", "classKey", "orderKey", "familyKey", "genusKey", "taxonID",
            "verbatimScientificName", "eventDate", "year", "month", "day", "decimalLatitude", "decimalLongitude",
            "coordinateUncertaintyInMeters", "stateProvince", "county", "countryCode", "gadm", "license",
            "issues", "lastInterpreted", "modified")
    out = {k: rec.get(k) for k in keep if k in rec}
    out["media"] = [{k: m.get(k) for k in ("type", "format", "identifier", "references", "license") if k in m}
                    for m in rec.get("media", [])]
    return out


LICENCES = {
    "by": "CC-BY", "by-sa": "CC-BY-SA", "by-nd": "CC-BY-ND", "by-nc": "CC-BY-NC",
    "by-nc-sa": "CC-BY-NC-SA", "by-nc-nd": "CC-BY-NC-ND",
}


def licence_id(url):
    """SPDX-style identifier for a Creative Commons licence address (CC-BY-NC-4.0, CC0-1.0); else the input."""
    if not url:
        return ""
    u = url.strip()
    m = re.search(r"creativecommons\.org/licenses/([a-z-]+)/([0-9.]+)", u, re.I)
    if m and m.group(1).lower() in LICENCES:
        return "%s-%s" % (LICENCES[m.group(1).lower()], m.group(2))
    m = re.search(r"creativecommons\.org/publicdomain/zero/([0-9.]+)", u, re.I)
    if m:
        return "CC0-%s" % m.group(1)
    if re.search(r"creativecommons\.org/publicdomain/mark", u, re.I):
        return "PDM-1.0"
    simple = {"CC_BY_4_0": "CC-BY-4.0", "CC_BY_NC_4_0": "CC-BY-NC-4.0", "CC0_1_0": "CC0-1.0"}
    return simple.get(u, u)


def write_json_list(path, head, species):
    """Write {head..., "species": [...]} with one species per line, valid JSON, UTF-8."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["{"]
    for k, v in head.items():
        lines.append("  %s: %s," % (json.dumps(k), json.dumps(v, ensure_ascii=False)))
    lines.append('  "species": [')
    for i, s in enumerate(species):
        lines.append("    " + json.dumps(s, ensure_ascii=False) + ("," if i < len(species) - 1 else ""))
    lines.append("  ]")
    lines.append("}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    json.loads(path.read_text(encoding="utf-8"))  # must parse


def die(msg):
    log("FATAL: " + msg)
    sys.exit(1)
