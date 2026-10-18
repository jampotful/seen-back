#!/usr/bin/env python3
"""Which live rows disagree with the evidence (burst 11b). Changes no row.

    python3 -I tools/views/rows_live.py [--views a,b] [--no-report]

For each view that rows.py can compute (the fourteen with a gap table, and the jumping spider and the spiders), the grade the evidence
gives a row (rows.py's own computation: the grade most of the species' records fall under, carry rules applied) is set beside the grade
letter of the live row with the same title, and every number in the live row's text is looked for in the records of the row's traits that
belong to a species of the view or a relative of one (the same test rows.py gives a draft). Writes the block `live-disagreement` of
docs/views/voice/REPORT.md. Live rows whose title matches no row of rows.py are counted and not compared.
"""
import argparse
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
spec = importlib.util.spec_from_file_location("rows", os.path.join(HERE, "rows.py"))
R = importlib.util.module_from_spec(spec)
sys.modules["rows"] = R
spec.loader.exec_module(R)

VIEWS = "alligator,bee,bird,cat,deer,dog,frog,hawk,insect,jumper,plant,rabbit,reptile,spider,squirrel,wader"


def norm(t):
    t = t.lower().replace("colour", "color").replace("neighbours", "neighbors")
    return re.sub(r"[^a-z]+", " ", t).strip()


def pool_for(index, row):
    """Numbers in every record of the row's traits that belongs to a species of the view or a relative of one."""
    pool, seen = [], set()
    for key, recs in index.items():
        if key[2] not in {R.GAPS.ALIAS.get(t, t) for t in row["traits"]}:
            continue
        for r in recs:
            if id(r) in seen:
                continue
            seen.add(id(r))
            if R.related(r, row["species"]):
                R.numbers_of(r.get("value"), pool)
                R.numbers_of(r.get("quote"), pool)
    return pool


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--views", default=VIEWS)
    ap.add_argument("--no-report", action="store_true")
    a = ap.parse_args()
    views = a.views.split(",")
    tax = R.GAPS.Tax()
    import csv
    extra = os.path.join(ROOT, "docs", "views", "gaps", "taxonomy-extra.tsv")
    if os.path.exists(extra):
        for r in csv.DictReader(open(extra, encoding="utf-8"), delimiter="\t"):
            tax.add(r["genus"], r["family"], r["order"])
    species = {v: R.view_species(ROOT, v, tax) for v in views}
    recs, index, ord_ev = R.load_evidence(ROOT, tax)
    for v in views:
        for e in species[v]:
            e["genus"] = e["sci"].split(" ")[0]
            e["family"] = e["family"] or tax.family(e["genus"])
            e["order"] = e["order"] or tax.order(e["genus"])
    cls_of, carry = R.class_of(ROOT), R.read_carry(ROOT)
    table, details, nomatch = [], [], {}
    for v in views:
        live = [x for x in R.live_rows(v)]
        computed = {}
        for title, traits in R.view_rows(ROOT, v).items():
            for old, new in R.US_TITLES:
                title = title.replace(old, new)
            computed[norm(title)] = R.compute_row(ROOT, v, title, traits, species[v], index, ord_ev, tax, cls_of, carry)
        n_cmp = n_grade = n_val = 0
        for row in live:
            g, title, text = row[0], row[1], row[2]
            c = computed.get(norm(title))
            if c is None:
                nomatch.setdefault(v, []).append(title)
                continue
            n_cmp += 1
            pool = pool_for(index, c)
            bad = []
            human = re.search(r"\bhumans?\b|\bpeople\b|\byours?\b", text, re.I)
            for m in R.NUMS.finditer(text):
                n = float(m.group(1).replace(",", ""))
                if n <= 10 or (human and n in R.HUMAN_OK) or (1900 <= n <= 2100):
                    continue
                if not R.supported(n, pool):
                    bad.append(m.group(1))
            gd = g in "mgi" and g != c["grade"]
            if gd:
                n_grade += 1
            if bad:
                n_val += 1
            if gd or bad:
                details.append((v, title, g, c["grade"], c["shares"], bad, text))
        table.append((v, len(live), n_cmp, n_grade, n_val))
    lines = ["## Live rows against the evidence (burst 11b)", "",
             "`tools/views/rows_live.py` sets each live row beside the evidence. The grade is the one `rows.py` computes for the row (the grade most of the species' records fall under, the carry rules applied; partial records count as measured). A value is flagged when a number of 10 or more in the live text is in no record of the row's traits for a species of the view or a relative of one (a flag is a prompt to read the row, not a verdict, since a row may rest on a paper outside the evidence logs). No live row was changed.", "",
             "| view | live rows | compared | grade differs | a number unsupported |", "|---|---:|---:|---:|---:|"]
    for v, nl, nc, ng, nv in table:
        lines.append("| %s | %d | %d | %d | %d |" % (v, nl, nc, ng, nv))
    lines.append("| all | %d | %d | %d | %d |" % tuple(sum(t[i] for t in table) for i in (1, 2, 3, 4)))
    lines += ["", "### The rows that differ", "", "| view | row | live grade | evidence grade (shares m / g / i) | numbers not found | live text |", "|---|---|---|---|---|---|"]
    for v, title, g, cg, sh, bad, text in details:
        lines.append("| %s | %s | %s | %s (%.0f / %.0f / %.0f%%) | %s | %s |" % (
            v, title, g, cg, 100 * sh["m"], 100 * sh["g"], 100 * sh["i"], ", ".join(bad) or "-", text.replace("|", "/")[:160]))
    if nomatch:
        lines += ["", "Live rows with no matching row in `rows.py` (not compared): " + "; ".join("%s: %s" % (v, ", ".join(t)) for v, t in nomatch.items()) + "."]
    body = "\n".join(lines)
    print(body)
    if not a.no_report:
        R.VC.write_block(R.VC.REPORT, "live-disagreement", body)
    return 0


if __name__ == "__main__":
    sys.exit(main())
