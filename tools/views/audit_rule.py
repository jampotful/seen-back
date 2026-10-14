#!/usr/bin/env python3
"""The narrower grade rule decided in burst 9 (docs/views/audit/SAMPLE.md), applied to the audit's stored reasons.

The second pass graded a record 'g' when its passage reports another study's measurement, a review's table, or names the
measured animal by a common or genus name. The research brief means something narrower: 'g' when the measured taxon is
a different taxon from the record's (one member or a narrower group standing for a wider record, a wider group standing
for a narrower one, or a relative). A review that reports a measurement on the record's own taxon is graded by what it
reports, which is 'm'. This module reads the second pass's reason and decides, for each correction from 'm' to 'g',
whether the reason names such a taxon mismatch. Where it does not, the grade goes back to 'm'.

    keep_g(reason) -> True when the reason names a taxon mismatch (the 'g' stands)
"""
import re

MISMATCH = re.compile("|".join([
    r"narrower", r"wider (?:group|taxon|than)", r"broader (?:group|taxon|than)", r"a wider",
    r"\bone species\b", r"single species", r"from a member", r"\ba member of", r"\bthat one\b", r"\bone (?:caterpillar|animal|individual)",
    r"a handful", r"not (?:for )?the whole", r"as (?:a )?wholes?\b", r"claim for all", r"(?:extended|generali[sz]ed) beyond",
    r"\brelatives?\b", r"congener", r"\banother species\b", r"\bother species\b", r"different species", r"a different taxon",
    r"\bpresumed\b", r"hypothes", r"without naming a species", r"or any species",
    r"genus-level", r"taxon should be", r"taxon (?:is|was) corrected", r"corrected the taxon", r"changes? the taxon",
    r"taxon (?:is|was) changed", r"borrowed from",
]), re.I)


def keep_g(reason):
    return bool(MISMATCH.search(reason or ""))


def main():
    """python3 -I tools/views/audit_rule.py [ALL.jsonl] [decisions.jsonl] : writes one decision a line for every correction
    from 'm' to 'g' whose reason names no taxon mismatch, setting the grade back to 'm'."""
    import json, os, sys
    here = os.path.dirname(os.path.abspath(__file__))
    audit = os.path.join(here, "..", "..", "docs", "views", "audit")
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(audit, "ALL.jsonl")
    dst = sys.argv[2] if len(sys.argv) > 2 else os.path.join(audit, "decisions.jsonl")
    rows = [json.loads(l) for l in open(src, encoding="utf-8") if l.strip()]
    mg = [r for r in rows if r["verdict"] == "correct" and r.get("grade") == "m" and r.get("grade_final") == "g"]
    out = [{"id": r["id"], "set": {"grade": "m"},
            "why": "burst 9 rule: the passage reports a measurement on the record's own taxon (from a review, a cited study, "
                   "or by a common or genus name), so the grade stays m"} for r in mg if not keep_g(r.get("reason"))]
    with open(dst, "w", encoding="utf-8") as f:
        for d in out:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
    print("%d corrections from m to g; %d keep g; %d decisions written to %s" % (len(mg), len(mg) - len(out), len(out), dst))


if __name__ == "__main__":
    main()
