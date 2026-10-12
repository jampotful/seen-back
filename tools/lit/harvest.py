#!/usr/bin/env python3
"""Gather the scientific literature on how a group of creatures senses the world, for the senses research
(docs/views/senses/). Runs on a build machine, which reaches the open scholarly indexes directly.

For one topic of tools/lit/topics.json it asks two open indexes for works whose title or abstract names one of the
topic's creatures and one of its senses:
  OpenAlex      https://api.openalex.org/works (records released under CC0, abstracts included)
  Europe PMC    https://www.ebi.ac.uk/europepmc/webservices/rest/search
merges the answers by DOI, and keeps for each work its citation, its abstract as OpenAlex gives it, where it can be
read free, and under what licence. The full text is kept only when the work is published under a Creative Commons
licence or in the public domain: from Europe PMC's open-access XML where it has one, otherwise from the openly
licensed PDF through pdftotext. Every other work keeps its citation, abstract and addresses, and is read on the web.

Writes OUT/<topic>/index.jsonl (one work a line), OUT/<topic>/text/<key>.txt and OUT/<topic>/SUMMARY.md.
Usage: python3 -I tools/lit/harvest.py --topics tools/lit/topics.json --topic spider-day --out corpus [--max-text 400]
"""
import argparse
import concurrent.futures as cf
import html
import json
import math
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

UA = "RegardsSensesHarvester/1.0 (+https://github.com/jampotful/seen-back)"
OPEN = {"cc-by", "cc-by-sa", "cc-by-nc", "cc-by-nc-sa", "cc-by-nd", "cc-by-nc-nd", "cc0", "public-domain", "pd"}
OA_URL = "https://api.openalex.org/works"
EPMC_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def get(url, tries=4, timeout=60, binary=False, limit=40_000_000):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read(limit + 1)
                if len(data) > limit:
                    raise ValueError("over %d bytes" % limit)
                ctype = r.headers.get("Content-Type", "")
                return (data, ctype) if binary else data.decode("utf-8", "replace")
        except (urllib.error.HTTPError) as e:
            last = e
            if e.code in (400, 401, 403, 404, 410, 451):
                break
            time.sleep(2 ** i)
        except Exception as e:  # network trouble: wait and try again
            last = e
            time.sleep(2 ** i)
    raise RuntimeError("%s: %s" % (url[:120], last))


def norm_licence(s):
    s = (s or "").strip().lower().replace(" ", "-").replace("_", "-")
    s = re.sub(r"-?\d(\.\d)?$", "", s)
    if s in ("cc-zero", "cc0-1.0"):
        s = "cc0"
    return s


def norm_doi(d):
    d = (d or "").strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    return d or None


def abstract_of(inv):
    if not inv:
        return ""
    pos = []
    for w, ps in inv.items():
        for p in ps:
            pos.append((p, w))
    return " ".join(w for _, w in sorted(pos))


def openalex(query, cap):
    out, cursor = [], "*"
    sel = "id,doi,title,publication_year,authorships,primary_location,best_oa_location,locations,open_access,abstract_inverted_index,cited_by_count,type,ids"
    while cursor and len(out) < cap:
        url = OA_URL + "?" + urllib.parse.urlencode({"filter": "title_and_abstract.search:" + query, "per-page": 200, "cursor": cursor, "select": sel})
        j = json.loads(get(url))
        res = j.get("results") or []
        out += res
        cursor = (j.get("meta") or {}).get("next_cursor")
        if not res:
            break
        time.sleep(0.2)
    return out[:cap]


def epmc(query, cap):
    out, cursor = [], "*"
    while cursor and len(out) < cap:
        url = EPMC_URL + "?" + urllib.parse.urlencode({"query": query, "format": "json", "resultType": "core", "pageSize": 1000, "cursorMark": cursor})
        j = json.loads(get(url))
        res = (j.get("resultList") or {}).get("result") or []
        out += res
        nxt = j.get("nextCursorMark")
        cursor = nxt if nxt and nxt != cursor and res else None
        time.sleep(0.2)
    return out[:cap]


def or_terms(terms, wild=False):
    q = []
    for t in terms:
        t = t.strip()
        if " " in t and not t.startswith('"'):
            t = '"%s"' % t
        q.append(t if wild else t.replace("*", ""))
    return "(" + " OR ".join(q) + ")"


def from_openalex(w, rank):
    best = w.get("best_oa_location") or {}
    locs = w.get("locations") or []
    lic, pdf, land = None, None, None
    for L in [best] + locs:
        l2 = norm_licence((L or {}).get("license"))
        if l2 in OPEN and (L or {}).get("pdf_url"):
            lic, pdf, land = l2, L.get("pdf_url"), L.get("landing_page_url")
            break
    if lic is None:
        lic = norm_licence(best.get("license")) or None
        pdf, land = best.get("pdf_url"), best.get("landing_page_url")
    ids = w.get("ids") or {}
    pmcid = (ids.get("pmcid") or "").rsplit("/", 1)[-1] or None
    if pmcid and not pmcid.upper().startswith("PMC"):
        pmcid = "PMC" + pmcid
    src = ((w.get("primary_location") or {}).get("source") or {})
    return {"doi": norm_doi(w.get("doi")), "openalex": (w.get("id") or "").rsplit("/", 1)[-1] or None,
            "pmid": (ids.get("pmid") or "").rsplit("/", 1)[-1] or None, "pmcid": pmcid,
            "title": html.unescape(w.get("title") or ""), "year": w.get("publication_year"),
            "authors": [((a.get("author") or {}).get("display_name") or "") for a in (w.get("authorships") or [])][:20],
            "venue": src.get("display_name"), "type": w.get("type"), "cited_by": w.get("cited_by_count") or 0,
            "abstract": abstract_of(w.get("abstract_inverted_index")),
            "oa_status": (w.get("open_access") or {}).get("oa_status"), "licence": lic, "pdf_url": pdf,
            "landing_url": land or (w.get("doi") or None), "rank_openalex": rank}


def from_epmc(r, rank):
    lic = norm_licence(r.get("license")) or None
    return {"doi": norm_doi(r.get("doi")), "pmid": r.get("pmid"), "pmcid": r.get("pmcid"),
            "title": html.unescape(re.sub(r"<[^>]+>", "", r.get("title") or "")), "year": int(r["pubYear"]) if str(r.get("pubYear", "")).isdigit() else None,
            "authors": [a.strip() for a in (r.get("authorString") or "").split(",") if a.strip()][:20],
            "venue": ((r.get("journalInfo") or {}).get("journal") or {}).get("title"), "type": r.get("pubType"),
            "cited_by": r.get("citedByCount") or 0, "epmc_oa": r.get("isOpenAccess") == "Y" and r.get("inEPMC") == "Y",
            "licence": lic, "rank_epmc": rank, "source_epmc": r.get("source"), "epmc_id": r.get("id")}


def merge(works_oa, works_ep):
    by, order = {}, []
    def key_of(w):
        return w.get("doi") or ("pmid:" + w["pmid"] if w.get("pmid") else None) or ("oa:" + w["openalex"] if w.get("openalex") else None) or ("epmc:" + str(w.get("epmc_id")))
    for w in works_oa + works_ep:
        k = key_of(w)
        if k in by:
            o = by[k]
            for f, v in w.items():
                if v not in (None, "", [], 0) and o.get(f) in (None, "", [], 0):
                    o[f] = v
            if w.get("licence") in OPEN and o.get("licence") not in OPEN:
                o["licence"] = w["licence"]
        else:
            by[k] = dict(w); by[k]["key"] = k; order.append(k)
    out = [by[k] for k in order]
    for w in out:
        r1, r2 = w.get("rank_openalex"), w.get("rank_epmc")
        w["found_by"] = [s for s, r in (("openalex", r1), ("europepmc", r2)) if r is not None]
        # earlier in either list, found by both, and cited more come first
        best = min([r for r in (r1, r2) if r is not None] or [10 ** 6])
        w["score"] = round(1.0 / (1 + best) * (1.5 if r1 is not None and r2 is not None else 1.0) + 0.002 * math.log1p(w.get("cited_by") or 0), 6)
    out.sort(key=lambda w: -w["score"])
    return out


def slug(k):
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", k)[:120]


def xml_text(xml):
    root = ET.fromstring(xml)
    lines = []
    def text(el):
        return re.sub(r"\s+", " ", "".join(el.itertext())).strip()
    t = root.find(".//article-title")
    if t is not None:
        lines.append("# " + text(t))
    ab = root.find(".//abstract")
    if ab is not None:
        lines += ["", "## Abstract", text(ab)]
    body = root.find(".//body")
    if body is not None:
        for el in body.iter():
            tag = el.tag.split("}")[-1]
            if tag == "title":
                lines += ["", "## " + text(el)]
            elif tag == "p":
                lines.append(text(el))
    for tw in root.iter():
        if tw.tag.split("}")[-1] != "table-wrap":
            continue
        cap = tw.find(".//caption")
        lab = tw.find(".//label")
        lines += ["", "## Table " + (text(lab) if lab is not None else "") + ": " + (text(cap) if cap is not None else "")]
        for tr in tw.iter():
            if tr.tag.split("}")[-1] == "tr":
                lines.append(" | ".join(text(c) for c in tr if c.tag.split("}")[-1] in ("td", "th")))
    for fg in root.iter():
        if fg.tag.split("}")[-1] == "fig":
            cap = fg.find(".//caption")
            lab = fg.find(".//label")
            if cap is not None:
                lines += ["", "## Figure " + (text(lab) if lab is not None else "") + ": " + text(cap)]
    return "\n".join(lines)


def pdf_text(data):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "a.pdf")
        open(p, "wb").write(data)
        r = subprocess.run(["pdftotext", "-enc", "UTF-8", p, "-"], capture_output=True, timeout=120)
        return r.stdout.decode("utf-8", "replace")


def full_text(w):
    """The work's text, if it is openly licensed: Europe PMC's XML first, else the PDF."""
    if w.get("pmcid") and (w.get("epmc_oa") or w.get("licence") in OPEN):
        try:
            x = get("https://www.ebi.ac.uk/europepmc/webservices/rest/%s/fullTextXML" % w["pmcid"], tries=2)
            t = xml_text(x)
            if len(t) > 2000:
                return t, "europepmc-xml"
        except Exception:
            pass
    if w.get("licence") in OPEN and w.get("pdf_url"):
        try:
            data, ctype = get(w["pdf_url"], tries=2, binary=True)
            if data[:5] == b"%PDF-":
                t = pdf_text(data)
                if len(t) > 2000:
                    return t, "pdf"
        except Exception:
            pass
    return None, None


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--topics", default="tools/lit/topics.json")
    ap.add_argument("--topic", required=True)
    ap.add_argument("--out", default="corpus")
    ap.add_argument("--cap", type=int, default=1500, help="most works asked of each index for each query")
    ap.add_argument("--max-text", type=int, default=400)
    a = ap.parse_args()
    cfg = json.load(open(a.topics))
    senses = cfg["senses"]
    T = next(t for t in cfg["topics"] if t["name"] == a.topic)
    outd = os.path.join(a.out, a.topic)
    os.makedirs(os.path.join(outd, "text"), exist_ok=True)
    groups = T.get("senses", ["vision"])
    sense_terms = [s for g in groups for s in senses[g]]
    queries = []
    for taxa in [T["taxa"][i:i + 12] for i in range(0, len(T["taxa"]), 12)]:   # long OR lists are split, since very long queries are refused
        queries.append((or_terms(taxa), or_terms(sense_terms)))
    for extra in T.get("extra", []):                                       # whole queries given as they are, for topics with no creatures to name
        queries.append((extra, None))
    oa_works, ep_works, n_oa, n_ep = [], [], 0, 0
    for tq, sq in queries:
        q_oa = tq + (" AND " + sq if sq else "")
        try:
            res = openalex(q_oa, a.cap)
            oa_works += [from_openalex(w, n_oa + i) for i, w in enumerate(res)]
            n_oa += len(res)
            log("openalex", len(res), q_oa[:140])
        except Exception as e:
            log("openalex failed:", e)
        q_ep = ("TITLE_ABS:" + tq + (" AND TITLE_ABS:" + sq if sq else "")) if sq else tq
        try:
            res = epmc(q_ep, a.cap)
            ep_works += [from_epmc(r, n_ep + i) for i, r in enumerate(res)]
            n_ep += len(res)
            log("europepmc", len(res), q_ep[:140])
        except Exception as e:
            log("europepmc failed:", e)
    works = merge(oa_works, ep_works)
    log("works", len(works))
    want = [w for w in works if (w.get("licence") in OPEN and w.get("pdf_url")) or (w.get("pmcid") and (w.get("epmc_oa") or w.get("licence") in OPEN))][:a.max_text]
    got = {}
    with cf.ThreadPoolExecutor(8) as ex:
        futs = {ex.submit(full_text, w): w for w in want}
        for f in cf.as_completed(futs):
            w = futs[f]
            try:
                t, how = f.result()
            except Exception:
                t, how = None, None
            if t:
                name = slug(w["key"]) + ".txt"
                head = "%s\n%s (%s). %s. %s. doi:%s. Licence: %s. Text from %s.\n\n" % (w["title"], ", ".join(w.get("authors") or [])[:400], w.get("year"), w.get("venue") or "", w.get("landing_url") or "", w.get("doi") or "", w.get("licence") or "open-access subset", how)
                open(os.path.join(outd, "text", name), "w", encoding="utf-8").write(head + t)
                got[w["key"]] = ("text/" + name, how)
    with open(os.path.join(outd, "index.jsonl"), "w", encoding="utf-8") as f:
        for w in works:
            w["text"], w["text_from"] = got.get(w["key"], (None, None))
            f.write(json.dumps(w, ensure_ascii=False) + "\n")
    s = ["# %s" % a.topic, "", "Made by `tools/lit/harvest.py` on %s." % time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), "",
         "- works found: %d (OpenAlex %d, Europe PMC %d, before merging)" % (len(works), n_oa, n_ep),
         "- with an abstract: %d" % sum(1 for w in works if w.get("abstract")),
         "- openly licensed with a text to fetch: %d; texts kept: %d (Europe PMC XML %d, PDF %d)" % (
             len(want), len(got), sum(1 for v in got.values() if v[1] == "europepmc-xml"), sum(1 for v in got.values() if v[1] == "pdf")),
         "- free to read without an open licence (read on the web): %d" % sum(1 for w in works if w.get("oa_status") in ("bronze", "green", "hybrid", "gold", "diamond") and w["key"] not in got),
         "", "Queries:"] + ["- `%s`" % (tq + (" AND " + sq if sq else "")) for tq, sq in queries]
    open(os.path.join(outd, "SUMMARY.md"), "w", encoding="utf-8").write("\n".join(s) + "\n")
    log("written", outd, "texts", len(got))


if __name__ == "__main__":
    main()
