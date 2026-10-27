"""Open-access pass, network half: run on a build machine (the workspace cannot reach these sites).

For each paper in a list it looks the paper up (Crossref, OpenAlex, Europe PMC, Semantic Scholar),
downloads the best free, legal copy it finds, turns it into text, checks that the text is the paper,
and writes:
  out/lookup.jsonl   one line a paper: the full bibliographic record from Crossref (every author,
                     journal, volume, issue, pages, type), where a free copy was found, which one was
                     read, and whether the paper's title appears in it. Metadata only.
  out/enc/<id>.bin   the text, encrypted to the public key in ci/oa/pub.pem (RSA-OAEP wraps an AES-GCM
                     key; the text is gzipped first). The repository is public and the papers are under
                     copyright, so no readable paper text ever leaves the machine. Only the holder of the
                     private key (the control room and its reading agents) can read these files.

Never used: ResearchGate, Academia.edu, Sci-Hub, LibGen, Z-Library, library proxies.

Usage: python3 ci/oa/oa.py --batch oa-9 ci/oa/list.jsonl out
"""
import argparse
import gzip
import hashlib
import html
import io
import json
import os
import pathlib
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36 seen-back-oa/1"
BANNED = ("researchgate.net", "academia.edu", "sci-hub", "libgen", "z-lib", "zlibrary", "booksc", "pdfdrive",
          "ezproxy", "libproxy", "elogim", "idm.oclc.org", "proxy.")  # library proxies never opened
CAP = 30 * 1024 * 1024


def get(url, accept=None, timeout=60, tries=3):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept or "*/*"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read(CAP + 1)
                return r.status, r.headers.get("Content-Type", ""), data, r.geturl()
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 503):
                time.sleep(3 * (i + 1))
                continue
            return e.code, "", b"", url
        except Exception as e:  # timeouts, resets
            last = e
            time.sleep(2 * (i + 1))
    return 0, "", str(last).encode()[:200], url


def jget(url):
    s, ct, data, _ = get(url, accept="application/json")
    if s != 200:
        return None
    try:
        return json.loads(data.decode("utf-8", "replace"))
    except Exception:
        return None


def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def title_in(title, text):
    words = [w for w in norm(title).split() if len(w) > 3][:8]
    if not words:
        return False
    body = norm(text[:20000])
    hits = sum(1 for w in words if w in body)
    return hits >= max(2, int(0.75 * len(words)))


def crossref(doi):
    j = jget("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    if not j:
        return None
    m = j.get("message", {})
    authors = []
    for a in m.get("author", []) or []:
        if a.get("family"):
            authors.append((a.get("family") + (", " + a["given"] if a.get("given") else "")).strip())
        elif a.get("name"):
            authors.append(a["name"])
    year = None
    for k in ("published-print", "published-online", "issued", "created"):
        dp = (m.get(k) or {}).get("date-parts")
        if dp and dp[0] and dp[0][0]:
            year = dp[0][0]
            break
    return {
        "title": (m.get("title") or [""])[0],
        "authors": authors,
        "journal": (m.get("container-title") or [""])[0],
        "volume": m.get("volume", ""),
        "issue": m.get("issue", ""),
        "pages": m.get("page", "") or m.get("article-number", ""),
        "year": year,
        "type": m.get("type", ""),
        "publisher": m.get("publisher", ""),
        "license": [l.get("URL") for l in (m.get("license") or [])][:3],
    }


def openalex_doi(doi):
    return jget("https://api.openalex.org/works/doi:" + urllib.parse.quote(doi)
                + "?select=id,doi,display_name,publication_year,type,open_access,best_oa_location,locations,authorships")


def openalex_title(title, first_author, year):
    q = urllib.parse.quote(" ".join(norm(title).split()[:14]))
    j = jget("https://api.openalex.org/works?filter=title.search:" + q
             + "&per-page=5&select=id,doi,display_name,publication_year,type,open_access,best_oa_location,locations,authorships")
    if not j:
        return None
    fa = norm(first_author).split()[:1]
    for w in j.get("results", []):
        t_ok = norm(w.get("display_name")) == norm(title) or (
            len(set(norm(title).split()) & set(norm(w.get("display_name")).split())) >= 0.85 * len(set(norm(title).split())))
        y_ok = not year or not w.get("publication_year") or abs(int(w["publication_year"]) - int(str(year)[:4])) <= 1
        names = " ".join(norm((a.get("author") or {}).get("display_name")) for a in (w.get("authorships") or [])[:3])
        a_ok = not fa or (fa[0] in names)
        if t_ok and y_ok and a_ok:
            return w
    return None


def europepmc(doi):
    j = jget("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%22" + urllib.parse.quote(doi)
             + "%22&resultType=core&format=json")
    if not j:
        return None
    r = (j.get("resultList") or {}).get("result") or []
    return r[0] if r else None


def s2(doi):
    time.sleep(1.1)
    return jget("https://api.semanticscholar.org/graph/v1/paper/DOI:" + urllib.parse.quote(doi)
                + "?fields=title,openAccessPdf,externalIds,publicationTypes")


def xml_text(data):
    """Europe PMC JATS XML to text: paragraphs, section titles, table rows (cells joined by ' | '), captions."""
    root = ET.fromstring(data)
    out = []

    def txt(e):
        return re.sub(r"\s+", " ", "".join(e.itertext())).strip()

    t = root.find(".//article-title")
    if t is not None:
        out.append(txt(t))
    ab = root.find(".//abstract")
    if ab is not None:
        out.append("ABSTRACT\n" + txt(ab))
    body = root.find(".//body")
    if body is not None:
        for e in body.iter():
            tag = e.tag.split("}")[-1]
            if tag == "title":
                out.append("\n## " + txt(e))
            elif tag == "p" and not any(p.tag.split("}")[-1] in ("table-wrap", "fig") for p in []):
                out.append(txt(e))
            elif tag == "table-wrap":
                cap = e.find(".//caption")
                lab = e.find("label")
                out.append("\nTABLE " + (txt(lab) if lab is not None else "") + " " + (txt(cap) if cap is not None else ""))
                for tr in e.iter():
                    if tr.tag.split("}")[-1] == "tr":
                        out.append(" | ".join(txt(c) for c in tr if c.tag.split("}")[-1] in ("td", "th")))
            elif tag == "fig":
                cap = e.find(".//caption")
                lab = e.find("label")
                out.append("FIGURE " + (txt(lab) if lab is not None else "") + " " + (txt(cap) if cap is not None else ""))
    back = root.find(".//back")
    if back is not None:
        for tw in back.iter():
            if tw.tag.split("}")[-1] == "table-wrap":
                for tr in tw.iter():
                    if tr.tag.split("}")[-1] == "tr":
                        out.append(" | ".join(txt(c) for c in tr if c.tag.split("}")[-1] in ("td", "th")))
    return "\n".join(x for x in out if x)


def pdf_text(data):
    p = pathlib.Path("/tmp/oa_tmp.pdf")
    p.write_bytes(data)
    plain = subprocess.run(["pdftotext", "-enc", "UTF-8", str(p), "-"], capture_output=True, timeout=180).stdout.decode("utf-8", "replace")
    layout = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", str(p), "-"], capture_output=True, timeout=180).stdout.decode("utf-8", "replace")
    return plain + "\n\n=== LAYOUT (same PDF, columns kept, for tables) ===\n\n" + layout


def html_text(raw):
    raw = re.sub(r"(?is)<(script|style|noscript|svg|nav|header|footer)\b.*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</(p|div|li|tr|h[1-6]|section|article|table|caption)>", "\n", raw)
    raw = re.sub(r"(?i)</t[dh]>", " | ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    raw = html.unescape(raw)
    raw = re.sub(r"[ \t\r\f\v]+", " ", raw)
    return re.sub(r"\n\s*\n+", "\n\n", raw).strip()


def encrypt(text, pub):
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    key = AESGCM.generate_key(bit_length=256)
    nonce = os.urandom(12)
    ct = AESGCM(key).encrypt(nonce, gzip.compress(text.encode("utf-8")), None)
    pk = serialization.load_pem_public_key(pub)
    wrapped = pk.encrypt(key, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return len(wrapped).to_bytes(2, "big") + wrapped + nonce + ct


def variants(url):
    """Other addresses for the same free copy: PMC pages to Europe PMC, HAL record to its document, Zenodo and Figshare records to their files."""
    out = []
    m = re.search(r"ncbi\.nlm\.nih\.gov/pmc/articles/(?:PMC)?(\d+)", url)
    if m:
        pmc = "PMC" + m.group(1)
        out += [("xml", "https://www.ebi.ac.uk/europepmc/webservices/rest/%s/fullTextXML" % pmc, "Europe PMC " + pmc),
                ("pdf", "https://europepmc.org/api/getPdf?pmcid=%s" % pmc, "Europe PMC PDF " + pmc)]
    m = re.search(r"(https?://hal\.[^/]+/[^/?#]+)", url)
    if m and not url.rstrip("/").endswith("document"):
        out.append(("pdf", m.group(1) + "/document", "HAL document"))
    m = re.search(r"zenodo\.org/(?:record|records)/(\d+)", url)
    if m:
        j = jget("https://zenodo.org/api/records/" + m.group(1))
        for f in (j or {}).get("files", [])[:3]:
            u = (f.get("links") or {}).get("self")
            if u and (f.get("key", "").lower().endswith(".pdf")):
                out.append(("pdf", u, "Zenodo file"))
    m = re.search(r"figshare\.com/articles/(?:[^/]+/)*(\d{5,})", url)
    if m:
        j = jget("https://api.figshare.com/v2/articles/" + m.group(1))
        for f in (j or {}).get("files", [])[:3]:
            if f.get("name", "").lower().endswith(".pdf") and f.get("download_url"):
                out.append(("pdf", f["download_url"], "Figshare file"))
    return out


def meta_pdf(raw):
    m = re.search(r'<meta[^>]+name=["\']citation_pdf_url["\'][^>]+content=["\']([^"\']+)', raw, re.I) or \
        re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']citation_pdf_url', raw, re.I)
    return html.unescape(m.group(1)) if m else None


def candidates(oa, epmc, s2r):
    """Free copies in order of preference: (kind, url, note)."""
    c = []
    if epmc and epmc.get("pmcid") and (epmc.get("isOpenAccess") == "Y" or epmc.get("inPMC") == "Y" or epmc.get("inEPMC") == "Y"):
        c.append(("xml", "https://www.ebi.ac.uk/europepmc/webservices/rest/%s/fullTextXML" % epmc["pmcid"], "Europe PMC " + epmc["pmcid"]))
    if oa:
        locs = []
        if oa.get("best_oa_location"):
            locs.append(oa["best_oa_location"])
        locs += [l for l in (oa.get("locations") or []) if l.get("is_oa")]
        seen = set()
        for l in locs:
            for kind, key in (("pdf", "pdf_url"), ("html", "landing_page_url")):
                u = l.get(key)
                if u and u not in seen:
                    seen.add(u)
                    src = ((l.get("source") or {}).get("display_name") or "")
                    c.append((kind, u, "OpenAlex location: " + src + (" (" + (l.get("version") or "") + ")" if l.get("version") else "")))
    if s2r and (s2r.get("openAccessPdf") or {}).get("url"):
        c.append(("pdf", s2r["openAccessPdf"]["url"], "Semantic Scholar openAccessPdf"))
    for kind, u, n in list(c):
        c += [v for v in variants(u) if v[1] not in {x[1] for x in c}]
    # html after all pdfs
    c.sort(key=lambda x: {"xml": 0, "pdf": 1, "html": 2}[x[0]])
    return [x for x in c if not any(b in x[1].lower() for b in BANNED)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", required=True)
    ap.add_argument("src")
    ap.add_argument("out")
    a = ap.parse_args()
    out = pathlib.Path(a.out)
    (out / "enc").mkdir(parents=True, exist_ok=True)
    pub = (pathlib.Path(__file__).parent / "pub.pem").read_bytes()
    rows = [json.loads(l) for l in open(a.src) if l.strip()]
    rows = [r for r in rows if r["batch"] == a.batch]
    lk = open(out / "lookup.jsonl", "w")
    for r in rows:
        rec = {"batch": r["batch"], "entry": r["entry"], "title_given": r.get("title"), "doi": (r.get("doi") or "").strip().lower(),
               "checked": [], "found": [], "read": None, "title_match": None, "text_sha256": None, "chars": 0}
        try:
            doi = rec["doi"]
            oa = epmc = s2r = None
            if doi:
                rec["crossref"] = crossref(doi)
                oa = openalex_doi(doi); rec["checked"].append("openalex")
                epmc = europepmc(doi); rec["checked"].append("europepmc")
            else:
                first = (r.get("authors") or "").split(",")[0].split(";")[0]
                oa = openalex_title(r.get("title") or "", first, r.get("year"))
                rec["checked"].append("openalex-title")
                if oa and oa.get("doi"):
                    doi = oa["doi"].replace("https://doi.org/", "").lower()
                    rec["doi_found"] = doi
                    rec["crossref"] = crossref(doi)
                    epmc = europepmc(doi); rec["checked"].append("europepmc")
            if oa:
                rec["openalex"] = {"id": oa.get("id"), "type": oa.get("type"), "is_oa": (oa.get("open_access") or {}).get("is_oa"),
                                   "oa_status": (oa.get("open_access") or {}).get("oa_status"), "title": oa.get("display_name"),
                                   "year": oa.get("publication_year")}
            if epmc:
                rec["europepmc"] = {k: epmc.get(k) for k in ("pmid", "pmcid", "isOpenAccess", "inPMC", "inEPMC", "pubType", "license")}
            cands = candidates(oa, epmc, None)
            if not cands and doi:
                s2r = s2(doi); rec["checked"].append("semanticscholar")
                cands = candidates(oa, epmc, s2r)
            rec["found"] = [{"kind": k, "url": u, "note": n} for k, u, n in cands]
            want = (rec.get("crossref") or {}).get("title") or (oa or {}).get("display_name") or r.get("title") or ""
            for kind, url, note in cands:
                s, ct, data, final = get(url, accept="application/pdf,text/html,application/xml;q=0.9,*/*;q=0.8")
                if s != 200 or not data or len(data) > CAP:
                    rec.setdefault("failed", []).append({"url": url, "status": s})
                    continue
                if any(b in final.lower() for b in BANNED):
                    continue
                try:
                    if kind == "xml" or data[:200].lstrip().startswith(b"<?xml") and b"<article" in data[:3000]:
                        text = xml_text(data)
                    elif data[:5] == b"%PDF-":
                        text = pdf_text(data)
                    else:
                        raw = data.decode("utf-8", "replace")
                        text = html_text(raw)
                        mp = meta_pdf(raw)
                        if len(text) < 30000 and mp and not any(b in mp.lower() for b in BANNED):
                            mp = urllib.parse.urljoin(final, mp)
                            s2_, ct2, d2, f2 = get(mp, accept="application/pdf,*/*;q=0.8")
                            if s2_ == 200 and d2[:5] == b"%PDF-":
                                text, url, note = pdf_text(d2), mp, note + "; PDF named by the page's citation_pdf_url"
                except Exception as e:
                    rec.setdefault("failed", []).append({"url": url, "error": str(e)[:120]})
                    continue
                if len(text) < 6000:
                    rec.setdefault("failed", []).append({"url": url, "status": s, "short": len(text)})
                    continue
                ok = title_in(want, text)
                if not ok and kind == "html":
                    rec.setdefault("failed", []).append({"url": url, "status": s, "title_match": False})
                    continue
                rec.update({"read": {"kind": kind, "url": url, "final_url": final.split("?")[0] if final and "X-Amz-" in final or final and "AWSAccessKeyId" in final else final, "note": note}, "title_match": ok,
                            "chars": len(text), "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()})
                (out / "enc" / ("%s-%s.bin" % (r["batch"], r["entry"]))).write_bytes(encrypt(text, pub))
                break
        except Exception as e:
            rec["error"] = str(e)[:200]
        lk.write(json.dumps(rec, ensure_ascii=False) + "\n")
        lk.flush()
        print(r["batch"], r["entry"], "read" if rec.get("read") else "none", (rec.get("read") or {}).get("kind", ""), flush=True)


if __name__ == "__main__":
    main()
