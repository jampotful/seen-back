"""English names from iNaturalist's public taxonomy archive (Darwin Core Archive).

https://www.inaturalist.org/taxa/inaturalist-taxonomy.dwca.zip holds a taxon core (taxa.csv) and vernacular-name
extensions. This module reads the archive's meta.xml to find the files and columns by their Darwin Core terms,
so it does not depend on column order. Species are joined by exact scientific name at rank species; when two
iNaturalist taxa share a name, the kingdom decides.

Choice of one English name per taxon (iNaturalist shows a place-specific name first where one applies):
  1. a name tied to the United States or Florida (locality or country code), in file order;
  2. otherwise the first name with no place attached, in file order;
  3. otherwise the first name.
The file order is checked against known preferred names by describe() in the build log.
"""
import csv
import io
import re
import sys
import time
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

import requests

from common import UA, log

ARCHIVE_URL = "https://www.inaturalist.org/taxa/inaturalist-taxonomy.dwca.zip"
NS = {"d": "http://rs.tdwg.org/dwc/text/"}
T = {
    "id": None,
    "scientificName": "http://rs.tdwg.org/dwc/terms/scientificName",
    "taxonRank": "http://rs.tdwg.org/dwc/terms/taxonRank",
    "kingdom": "http://rs.tdwg.org/dwc/terms/kingdom",
    "taxonID": "http://rs.tdwg.org/dwc/terms/taxonID",
    "vernacularName": "http://rs.tdwg.org/dwc/terms/vernacularName",
    "language": "http://purl.org/dc/terms/language",
    "locality": "http://rs.tdwg.org/dwc/terms/locality",
    "countryCode": "http://rs.tdwg.org/dwc/terms/countryCode",
    "source": "http://purl.org/dc/terms/source",
    "lexicon": "http://rs.gbif.org/terms/1.0/lexicon",  # may be absent
}
PERSONAL = re.compile(r"contributor|creator|rightsholder|recordedby|identifiedby|author", re.I)

csv.field_size_limit(sys.maxsize)


def ensure_archive(cache_dir):
    p = Path(cache_dir) / "inaturalist-taxonomy.dwca.zip"
    if p.exists() and p.stat().st_size > 1_000_000 and zipfile.is_zipfile(p):
        return p
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".part")
    for attempt in range(1, 6):
        try:
            t0 = time.time()
            with requests.get(ARCHIVE_URL, headers={"User-Agent": UA}, stream=True, timeout=120) as r:
                r.raise_for_status()
                with open(tmp, "wb") as f:
                    for chunk in r.iter_content(1 << 20):
                        f.write(chunk)
            tmp.replace(p)
            log("  downloaded %s: %.1f MB in %.0fs" % (ARCHIVE_URL, p.stat().st_size / 1e6, time.time() - t0))
            return p
        except Exception as e:  # retry the whole download
            log("  archive download attempt %d failed: %s" % (attempt, e))
            time.sleep(10 * attempt)
    raise RuntimeError("could not download " + ARCHIVE_URL)


def _fields(el):
    out = {}
    for f in el.findall("d:field", NS):
        if f.get("index") is not None:
            out[f.get("term")] = int(f.get("index"))
    return out


def read_meta(zf):
    root = ET.fromstring(zf.read("meta.xml"))
    core = root.find("d:core", NS)
    info = {"core": {"file": core.find("d:files/d:location", NS).text.strip(), "id": int(core.find("d:id", NS).get("index")),
                     "fields": _fields(core), "header": int(core.get("ignoreHeaderLines", "0")), "rowType": core.get("rowType")},
            "ext": []}
    for ext in root.findall("d:extension", NS):
        # One <extension> may list many files (iNaturalist lists one vernacular file per lexicon).
        for loc in ext.findall("d:files/d:location", NS):
            info["ext"].append({"file": loc.text.strip(),
                                "id": int(ext.find("d:coreid", NS).get("index")), "fields": _fields(ext),
                                "header": int(ext.get("ignoreHeaderLines", "0")), "rowType": ext.get("rowType")})
    return info


def _rows(zf, name, header):
    with zf.open(name) as raw:
        rd = csv.reader(io.TextIOWrapper(raw, encoding="utf-8", newline=""))
        for i, row in enumerate(rd):
            if i < header:
                continue
            yield row


def _get(row, idx):
    return row[idx].strip() if idx is not None and idx < len(row) else ""


def english_files(meta):
    """Vernacular-name extension files to read for English names: the English lexicon file when there is one."""
    vern = [e for e in meta["ext"] if T["vernacularName"] in e["fields"]]
    eng = [e for e in vern if re.search(r"(^|[-_/])english\.csv$", e["file"], re.I)]
    return eng or vern


def describe(path, probe_names=()):
    """Text describing the archive for the build log: files, sizes, meta.xml, first rows (columns naming
    people are left out), and every row for a few probe species."""
    out = []
    with zipfile.ZipFile(path) as zf:
        out.append("files:")
        for zi in zf.infolist():
            out.append("  %-45s %12d bytes (zipped %d)" % (zi.filename, zi.file_size, zi.compress_size))
        meta_txt = zf.read("meta.xml").decode("utf-8", "replace")
        out.append("meta.xml (%d chars):" % len(meta_txt))
        out.append(meta_txt[:6000])
        meta = read_meta(zf)
        for part in [meta["core"]] + meta["ext"][:3] + [e for e in meta["ext"] if re.search("english", e["file"], re.I)][:1]:
            with zf.open(part["file"]) as raw:
                head = io.TextIOWrapper(raw, encoding="utf-8", newline="")
                rd = csv.reader(head)
                rows = [r for _, r in zip(range(6), rd)]
            hdr = rows[0] if rows else []
            keep = [i for i, h in enumerate(hdr) if not PERSONAL.search(h)]
            out.append("%s, first rows (columns naming people left out):" % part["file"])
            for r in rows:
                out.append("  " + " | ".join(r[i] for i in keep if i < len(r)))
        if probe_names:
            want = set(probe_names)
            c = meta["core"]
            fi = c["fields"]
            ids = {}
            for row in _rows(zf, c["file"], c["header"]):
                nm = _get(row, fi.get(T["scientificName"]))
                if nm in want:
                    ids.setdefault(nm, []).append((_get(row, c["id"]), _get(row, fi.get(T["taxonRank"])), _get(row, fi.get(T["kingdom"]))))
            out.append("probe species in the core: %s" % ids)
            idset = {i for v in ids.values() for (i, _, _) in v}
            for e in english_files(meta):
                fe = e["fields"]
                for row in _rows(zf, e["file"], e["header"]):
                    if _get(row, e["id"]) in idset:
                        out.append("  %s: id=%s name=%r lang=%r locality=%r country=%r" % (
                            e["file"], _get(row, e["id"]), _get(row, fe.get(T["vernacularName"])),
                            _get(row, fe.get(T["language"])), _get(row, fe.get(T["locality"])),
                            _get(row, fe.get(T["countryCode"]))))
    return "\n".join(out)


RANKS = ("kingdom", "phylum", "class", "order", "family", "genus")
US_PLACE = re.compile(r"\b(United States|USA|U\.S\.|Florida|North America)\b", re.I)


def choose(rows):
    """rows: list of (name, locality, countryCode, language) in file order -> one name or ''."""
    rows = [r for r in rows if r[0]]
    if not rows:
        return ""
    us = [r for r in rows if US_PLACE.search(r[1] or "") or re.search(r"(^|[^A-Z])US([^A-Z]|$)", r[2] or "")]
    if us:
        return us[0][0]
    plain = [r for r in rows if not (r[1] or "").strip() and not (r[2] or "").strip()]
    if plain:
        return plain[0][0]
    return rows[0][0]


def english_names(path, wanted):
    """wanted: dict scientific name -> kingdom (GBIF). Returns (names dict sci -> English name, report dict)."""
    rep = {"wanted": len(wanted), "name_in_inat": 0, "ambiguous": 0, "kingdom_mismatch": 0, "with_english": 0}
    taxa = {}
    with zipfile.ZipFile(path) as zf:
        meta = read_meta(zf)
        c = meta["core"]
        fi = c["fields"]
        i_name, i_rank, i_king = fi.get(T["scientificName"]), fi.get(T["taxonRank"]), fi.get(T["kingdom"])
        rank_idx = {r: fi.get("http://rs.tdwg.org/dwc/terms/" + r) for r in RANKS}
        cand, ranks_of = {}, {}
        for row in _rows(zf, c["file"], c["header"]):
            nm = _get(row, i_name)
            if nm in wanted and _get(row, i_rank).lower() == "species":
                tid = _get(row, c["id"])
                cand.setdefault(nm, []).append((tid, _get(row, i_king)))
                ranks_of[tid] = {r: _get(row, rank_idx[r]) for r in RANKS}
        chosen = {}
        for nm, lst in cand.items():
            rep["name_in_inat"] += 1
            same = [t for t in lst if t[1] == wanted[nm]] or (lst if len(lst) == 1 else [])
            if not same:
                rep["kingdom_mismatch"] += 1
                continue
            chosen[nm] = [t[0] for t in same]
        id_rows = {}
        idset = {i for v in chosen.values() for i in v}
        for e in english_files(meta):
            fe = e["fields"]
            iv, il, iloc, icc = fe.get(T["vernacularName"]), fe.get(T["language"]), fe.get(T["locality"]), fe.get(T["countryCode"])
            for row in _rows(zf, e["file"], e["header"]):
                tid = _get(row, e["id"])
                if tid not in idset:
                    continue
                lang = _get(row, il).lower()
                if lang and lang not in ("en", "eng", "english"):
                    continue
                id_rows.setdefault(tid, []).append((_get(row, iv), _get(row, iloc), _get(row, icc), lang))
        out = {}
        for nm, ids in chosen.items():
            if len(ids) == 1:
                taxa[nm] = dict(ranks_of.get(ids[0], {}), id=ids[0])
            with_names = [i for i in ids if id_rows.get(i)]
            if len(with_names) > 1:
                rep["ambiguous"] += 1
                continue
            if with_names:
                taxa[nm] = dict(ranks_of.get(with_names[0], {}), id=with_names[0])
                rows = id_rows[with_names[0]]
                n = choose(rows)
                if n:
                    out[nm] = n
                    rep["with_english"] += 1
                    plain = [r[0] for r in rows if r[0] and not (r[1] or "").strip() and not (r[2] or "").strip()]
                    if plain and plain[0] != n:
                        rep["place_name_chosen"] = rep.get("place_name_chosen", 0) + 1
                        ex = rep.setdefault("place_name_examples", [])
                        if len(ex) < 15:
                            ex.append("%s: %s (no place: %s)" % (nm, n, plain[0]))
                    if len(rows) > 1:
                        rep["several_english"] = rep.get("several_english", 0) + 1
    return out, rep, taxa


def api_preferred(ids, place_id=1, per=30, pause=1.1):
    """iNaturalist's own preferred English name for taxon ids, from its public API (locale en, preferred place
    `place_id`, 1 = United States). Used to check the names chosen from the archive. About one request a second."""
    out = {}
    ids = list(ids)
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept": "application/json"})
    for k in range(0, len(ids), per):
        chunk = ids[k:k + per]
        url = "https://api.inaturalist.org/v1/taxa/%s" % ",".join(str(i) for i in chunk)
        for attempt in range(1, 5):
            try:
                r = s.get(url, params={"locale": "en", "preferred_place_id": place_id}, timeout=60)
                if r.status_code == 200:
                    for t in r.json().get("results", []):
                        out[str(t.get("id"))] = t.get("preferred_common_name") or ""
                    break
                time.sleep(5 * attempt)
            except (requests.RequestException, ValueError):
                time.sleep(5 * attempt)
        time.sleep(pause)
    return out
