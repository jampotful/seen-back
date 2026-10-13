#!/usr/bin/env python3
"""Calibrate the extractor against the evidence logs that agents made by hand.

    python3 -I tools/lit/calibrate.py build   --lit DIR --evidence a.jsonl b.jsonl ... --out DIR
    python3 -I tools/lit/calibrate.py offline --lit DIR --evidence ...                      (no API: grep and format checks)
    python3 -I tools/lit/calibrate.py compare --evidence ... --table calib.jsonl --out DIR   (after extract.py has run)

`build` copies, for every source the logs cite that is in the collection, its index line and full text into DIR/calib/
(a topic folder that tools/lit/extract.py reads with --topics calib). `offline` needs no key: for each logged record it
asks whether the collection holds the source, whether the logged quote is found in the source's text or abstract, and
whether the logged value appears in the quote; that is the most the extractor could recover. `compare` takes the
extractor's table for the calib topic and reports what share of the agents' values it recovers and how many it adds.
"""
import argparse, collections, glob, importlib.util, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


E = _load("lit_extract", os.path.join(HERE, "extract.py"))
CHECK = E.load_check()


def load_evidence(paths):
    rows = []
    for p in paths:
        unit = os.path.basename(p).replace(".jsonl", "")
        for line in open(p, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                r.setdefault("unit", unit)
                rows.append(r)
    return rows


def doi_of(r):
    return E.norm_doi((r.get("source") or {}).get("doi"))


def collection_index(lit, wanted):
    """doi -> (best index line, topic). Prefers a line that has a full text, then one that has an abstract."""
    found = {}
    for p in sorted(glob.glob(os.path.join(lit, "*", "index.jsonl"))):
        topic = os.path.basename(os.path.dirname(p))
        for line in open(p, encoding="utf-8"):
            if not line.strip():
                continue
            w = json.loads(line)
            d = E.norm_doi(w.get("doi"))
            if d not in wanted:
                continue
            score = (2 if w.get("text") else 0) + (1 if w.get("abstract") else 0)
            if d not in found or score > found[d][2]:
                found[d] = (w, topic, score)
    return found


def build(lit, ev, out):
    wanted = {doi_of(r) for r in ev if doi_of(r)}
    found = collection_index(lit, wanted)
    dest = os.path.join(out, "calib")
    shutil.rmtree(dest, ignore_errors=True)
    os.makedirs(os.path.join(dest, "text"))
    n_text = n_abs = 0
    with open(os.path.join(dest, "index.jsonl"), "w", encoding="utf-8") as f:
        for d, (w, topic, _) in sorted(found.items()):
            w = dict(w)
            if w.get("text"):
                src = os.path.join(lit, topic, w["text"])
                if os.path.exists(src):
                    shutil.copy(src, os.path.join(dest, "text", os.path.basename(w["text"])))
                    w["text"] = "text/" + os.path.basename(w["text"]); n_text += 1
                else:
                    w["text"] = None
            if not w.get("text") and w.get("abstract"):
                n_abs += 1
            f.write(json.dumps(w, ensure_ascii=False) + "\n")
    print("cited sources: %d; in the collection: %d (full text %d, abstract only %d)" % (len(wanted), len(found), n_text, n_abs))
    return found


def best_text(w, lit_or_calib_dir, topic=None):
    if w.get("text"):
        p = os.path.join(lit_or_calib_dir, topic, w["text"]) if topic else os.path.join(lit_or_calib_dir, w["text"])
        if os.path.exists(p):
            return open(p, encoding="utf-8", errors="replace").read(), "text"
    return w.get("abstract") or "", "abstract"


def offline(lit, ev):
    wanted = {doi_of(r) for r in ev if doi_of(r)}
    found = collection_index(lit, wanted)
    cache = {}
    res = collections.defaultdict(collections.Counter)
    miss_examples = []
    for r in ev:
        u = r["unit"]; c = res[u]
        c["records"] += 1
        d = doi_of(r)
        if CHECK.problems(r):
            c["fails_check_py"] += 1
        if r.get("grade") in ("i", "x"):
            c["grade_i_or_x"] += 1
        if d not in found:
            c["source_not_in_collection"] += 1; continue
        w, topic, _ = found[d]
        if d not in cache:
            txt, kind = best_text(w, lit, topic)
            cache[d] = (E.squash(txt), kind)
        tsq, kind = cache[d]
        if not tsq:
            c["source_in_collection_without_text_or_abstract"] += 1; continue
        c["source_in_collection_" + kind] += 1
        q = E.squash(r.get("quote", ""))
        if len(q) >= 10 and q in tsq:
            c["quote_found_in_" + kind] += 1
            if E.value_in_quote(r.get("value"), r.get("quote", "")) is not False:
                c["recoverable_" + kind] += 1
            else:
                c["quote_found_value_not_in_quote"] += 1
        else:
            c["quote_not_found_in_" + kind] += 1
            if len(miss_examples) < 12:
                miss_examples.append((u, d, kind, r.get("quote", "")[:90]))
    return res, miss_examples


def offline_md(res, miss):
    keys = ["records", "fails_check_py", "grade_i_or_x", "source_not_in_collection",
            "source_in_collection_text", "source_in_collection_abstract", "source_in_collection_without_text_or_abstract",
            "quote_found_in_text", "quote_found_in_abstract", "quote_not_found_in_text", "quote_not_found_in_abstract",
            "quote_found_value_not_in_quote", "recoverable_text", "recoverable_abstract"]
    units = sorted(res)
    L = ["| | " + " | ".join(units) + " | all |", "|---|" + "---:|" * (len(units) + 1)]
    for k in keys:
        L.append("| %s | %s | %d |" % (k, " | ".join(str(res[u][k]) for u in units), sum(res[u][k] for u in units)))
    tot = sum(res[u]["records"] for u in units)
    rec = sum(res[u]["recoverable_text"] + res[u]["recoverable_abstract"] for u in units)
    L += ["", "Most the extractor could recover from the collection: %d of %d records (%.0f%%)." % (rec, tot, 100.0 * rec / max(tot, 1))]
    if miss:
        L += ["", "Logged quotes not found in the collection's text (first few):"] + ["- %s %s (%s): %s" % m for m in miss]
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------------------------------------------------------

def close(a, b):
    return abs(a - b) <= max(0.011, 0.01 * max(abs(a), abs(b)))


def values_match(av, tv):
    an, tn = E.numbers_in(av), E.numbers_in(tv)
    if not an:
        return None
    return all(any(close(x, y) for y in tn) for x in an)


def windows(quote, k=6):
    ws = [w for w in E.squash_words(quote)] if hasattr(E, "squash_words") else re.findall(r"\w+", quote.lower())
    return {" ".join(ws[i:i + k]) for i in range(max(len(ws) - k + 1, 1))}


def genus_overlap(a, b):
    wa = {w.lower() for w in re.findall(r"[A-Za-z]{4,}", a or "")}
    wb = {w.lower() for w in re.findall(r"[A-Za-z]{4,}", b or "")}
    return bool(wa & wb)


def coverage(calib_dir):
    """doi -> squashed text for every work in DIR/calib that has a text or an abstract."""
    cov = {}
    for line in open(os.path.join(calib_dir, "calib", "index.jsonl"), encoding="utf-8"):
        if not line.strip():
            continue
        w = json.loads(line)
        txt, _ = best_text(w, os.path.join(calib_dir, "calib"))
        if txt:
            cov[E.norm_doi(w.get("doi"))] = E.squash(txt)
    return cov


def compare(ev, table, cov):
    by_doi = collections.defaultdict(list)
    for t in table:
        by_doi[E.norm_doi(t["source"]["doi"])].append(t)
    in_calib = set(by_doi)
    levels = collections.Counter()
    per_unit = collections.defaultdict(collections.Counter)
    matched_table = set()
    detail = []
    for i, r in enumerate(ev):
        d = doi_of(r)
        c = per_unit[r["unit"]]
        if r.get("grade") in ("i", "x") or d not in cov:
            continue
        q = E.squash(r.get("quote", ""))
        reach = len(q) >= 10 and q in cov[d] and E.value_in_quote(r.get("value"), r.get("quote", "")) is not False
        cand = by_doi.get(d, [])
        # strict: same trait and every number of the logged value present in the table value
        level = None
        for j, t in enumerate(cand):
            if t["trait"] != r["trait"]:
                continue
            vm = values_match(r.get("value"), t.get("value"))
            if vm is True or (vm is None and isinstance(r.get("value"), str) and genus_overlap(r.get("taxon"), t.get("taxon"))):
                level = "strict"; matched_table.add((d, j)); break
        if level is None:
            # loose: the logged quote and a table quote share a run of six words (same passage, value may be converted)
            wq = windows(r.get("quote", ""))
            for j, t in enumerate(cand):
                if wq & windows(t.get("quote", "")):
                    level = "loose"; matched_table.add((d, j)); break
        c["logged"] += 1
        c["recovered_" + (level or "none")] += 1
        levels[level or "none"] += 1
        if reach:
            c["reachable"] += 1
            c["reachable_recovered_strict"] += level == "strict"
            c["reachable_recovered_loose"] += level == "loose"
            levels["reachable"] += 1
            levels["reachable_strict"] += level == "strict"
            levels["reachable_loose"] += level == "loose"
        if level is None and reach and len(detail) < 15:
            detail.append((r["unit"], d, r["trait"], r.get("value"), r.get("quote", "")[:80]))
    added = [t for d, ts in by_doi.items() for j, t in enumerate(ts) if (d, j) not in matched_table]
    return per_unit, levels, added, detail


def compare_md(per_unit, levels, added, detail, table):
    units = sorted(per_unit)
    L = ["| | " + " | ".join(units) + " | all |", "|---|" + "---:|" * (len(units) + 1)]
    for k in ("logged", "recovered_strict", "recovered_loose", "recovered_none", "reachable", "reachable_recovered_strict", "reachable_recovered_loose"):
        L.append("| %s | %s | %d |" % (k, " | ".join(str(per_unit[u][k]) for u in units), sum(per_unit[u][k] for u in units)))
    n = sum(per_unit[u]["logged"] for u in units)
    s, lo = levels["strict"], levels["loose"]
    rc = levels["reachable"]
    L += ["", "Reachable values (the logged quote is in the collection's text for the source and carries the value): %d. "
          "Recovered with the same trait and value: %d (%.0f%%); with the same quote but another value form: %d (%.0f%%); "
          "together %.0f%%." % (rc, levels["reachable_strict"], 100.0 * levels["reachable_strict"] / max(rc, 1),
                                 levels["reachable_loose"], 100.0 * levels["reachable_loose"] / max(rc, 1),
                                 100.0 * (levels["reachable_strict"] + levels["reachable_loose"]) / max(rc, 1))]
    L += ["", "Of %d logged values (grades m and g) on sources that the table covers: %d recovered with the same trait and value (%.0f%%), "
          "%d more with the same quote but a different value form (%.0f%%), %d not recovered." % (
              n, s, 100.0 * s / max(n, 1), lo, 100.0 * lo / max(n, 1), levels["none"]),
          "The table holds %d records on these sources; %d of them match no logged record (the additions)." % (len(table), len(added))]
    if detail:
        L += ["", "Logged values not recovered (first few):"] + ["- %s %s %s = %s: %s" % d for d in detail]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["build", "offline", "compare"])
    ap.add_argument("--lit")
    ap.add_argument("--evidence", nargs="+", required=True)
    ap.add_argument("--out", default="calib-out")
    ap.add_argument("--table")
    ap.add_argument("--calib", help="compare: the --out directory that `build` filled")
    a = ap.parse_args()
    ev = load_evidence(a.evidence)
    os.makedirs(a.out, exist_ok=True)
    if a.cmd == "build":
        build(a.lit, ev, a.out)
    elif a.cmd == "offline":
        res, miss = offline(a.lit, ev)
        md = offline_md(res, miss)
        open(os.path.join(a.out, "CALIBRATION-OFFLINE.md"), "w").write(md)
        print(md)
    else:
        table = [json.loads(l) for l in open(a.table, encoding="utf-8") if l.strip()]
        pu, lv, added, detail = compare(ev, table, coverage(a.calib or a.out))
        md = compare_md(pu, lv, added, detail, table)
        open(os.path.join(a.out, "CALIBRATION.md"), "w").write(md)
        with open(os.path.join(a.out, "calibration-additions.jsonl"), "w", encoding="utf-8") as f:
            for t in added:
                f.write(json.dumps(t, ensure_ascii=False) + "\n")
        print(md)


if __name__ == "__main__":
    main()
