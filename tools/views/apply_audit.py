#!/usr/bin/env python3
"""Apply the audit's verdicts to an evidence log and write a corrected copy. The log itself is never edited.

    python3 -I tools/views/apply_audit.py LOG --all docs/views/audit/ALL.jsonl --out LOG.corrected.jsonl
        [--unit NAME] [--retracted drop|keep] [--no-mark] [--force]

LOG is docs/views/evidence/<unit>.jsonl from a research branch. The unit defaults to the file's name without .jsonl.
ALL.jsonl has one row per record: {"unit", "id" ("<unit>:<line number>"), "line", "verdict", "taxon", "trait", "value", ...}.
What each verdict does to the copy:
- correct: the line is replaced by the row's corrected_record. With marking on (the default) the record gains
  "audit": {"verdict": "correct", "was": {field: old value, ...}, "reason": ...} so that the change can be traced and undone.
- retract: the line is dropped (--retracted drop, the default) or kept and marked (--retracted keep).
- confirm, stands, unverifiable, flagged_unchecked, unseen: the line is copied unchanged. With marking on, a record that is
  flagged_unchecked or unverifiable gains "audit": {"verdict": ..., "reason": ...} so the open flag travels with it.
A row is applied only when the log's line still has the taxon, trait and value the audit saw. A line that has changed since
the audit is copied unchanged and reported, so that a log edited after the audit is never overwritten with stale fixes.
The script refuses to write over LOG, and over an existing file unless --force is given. It exits with status 1 when any
verdict could not be applied.
"""
import argparse, collections, json, os, sys

APPLIED = ("correct", "retract")
OPEN = ("flagged_unchecked", "unverifiable")


def same(a, b):
    return a == b or (isinstance(a, (int, float)) and isinstance(b, (int, float)) and abs(a - b) < 1e-9)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("log")
    ap.add_argument("--all", required=True, help="ALL.jsonl")
    ap.add_argument("--out", required=True, help="the corrected copy to write (never the log)")
    ap.add_argument("--unit", default="")
    ap.add_argument("--retracted", choices=["drop", "keep"], default="drop")
    ap.add_argument("--no-mark", action="store_true", help="do not add the audit field to changed or open records")
    ap.add_argument("--force", action="store_true", help="overwrite an existing --out file")
    a = ap.parse_args(argv)
    base = os.path.basename(a.log)
    unit = a.unit or (base[:-6] if base.endswith(".jsonl") else "")
    if not unit:
        sys.exit("cannot tell the unit from the file name; pass --unit")
    if os.path.realpath(a.out) == os.path.realpath(a.log):
        sys.exit("refusing to write over the log; --out must be a different file")
    if os.path.exists(a.out) and not a.force:
        sys.exit("%s exists; pass --force to replace it" % a.out)
    rows = {}
    for line in open(a.all, encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            if r["unit"] == unit:
                rows[r["line"]] = r
    if not rows:
        sys.exit("no rows for unit %r in %s" % (unit, a.all))
    out, count, problems = [], collections.Counter(), []
    n = 0
    for raw in open(a.log, encoding="utf-8"):
        if not raw.strip():
            continue
        n += 1
        rec = json.loads(raw)
        row = rows.get(n)
        if row is None:
            count["no audit row"] += 1
            out.append(rec); continue
        if (rec.get("taxon") != row.get("taxon") or rec.get("trait") != row.get("trait")
                or not same(rec.get("value"), row.get("value"))):
            problems.append("line %d: the log now holds %r %r %r, the audit saw %r %r %r; copied unchanged" % (
                n, rec.get("taxon"), rec.get("trait"), rec.get("value"), row.get("taxon"), row.get("trait"), row.get("value")))
            out.append(rec); continue
        v = row["verdict"]
        count[v] += 1
        if v == "correct":
            new = dict(row["corrected_record"])
            if not a.no_mark:
                was = {k: rec.get(k) for k in set(rec) | set(new) if not same(rec.get(k), new.get(k))}
                new["audit"] = {"verdict": "correct", "was": was, "reason": row.get("reason", "")}
            out.append(new)
        elif v == "retract":
            if a.retracted == "keep":
                if not a.no_mark:
                    rec = dict(rec, audit={"verdict": "retract", "reason": row.get("reason", "")})
                out.append(rec)
        elif v in OPEN and not a.no_mark:
            out.append(dict(rec, audit={"verdict": v, "reason": row.get("reason", "")}))
        else:
            out.append(rec)
    extra = [k for k in rows if k > n]
    if extra:
        problems.append("the audit has %d rows past the log's last line (%d lines); the log is shorter than the audited one" % (len(extra), n))
    with open(a.out, "w", encoding="utf-8") as f:
        for rec in out:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print("%s: %d lines read, %d written to %s" % (a.log, n, len(out), a.out))
    print("verdicts seen: " + ", ".join("%s %d" % kv for kv in sorted(count.items())))
    for p in problems:
        print("PROBLEM " + p, file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
