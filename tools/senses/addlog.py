#!/usr/bin/env python3
"""Append evidence records to a unit's log, checking each one.

    python3 -I tools/senses/addlog.py <unit> < records.jsonl

Each input line is one JSON object, one measurement (docs/views/research/BRIEF.md gives the fields and trait keys).
Lines are appended to docs/views/evidence/<unit>.jsonl, found from this file's place in the repository.
A record that fails a check stops the run before anything is written, with the reason.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import check  # noqa: E402  (tools/senses/check.py, loaded by path)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    unit = sys.argv[1]
    out = os.path.join(ROOT, "docs", "views", "evidence", unit + ".jsonl")
    rows = []
    for n, line in enumerate(sys.stdin, 1):
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except ValueError as e:
            sys.exit("line %d is not JSON: %s" % (n, e))
        r.setdefault("unit", unit)
        r.setdefault("opened", True)
        bad = check.problems(r)
        if bad:
            sys.exit("line %d: %s\n%s" % (n, "; ".join(bad), line[:200]))
        rows.append(r)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "a", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("added %d to %s" % (len(rows), os.path.relpath(out, ROOT)))


if __name__ == "__main__":
    main()
