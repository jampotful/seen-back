#!/usr/bin/env python3
"""Merge the audit into one file with a final verdict for every record of the evidence logs.

    python3 -I tools/lit/audit_all.py --ev DIR --unseen unseen.jsonl --first verdicts.jsonl \
        --adjudicated a.jsonl [--adjudicated b.jsonl ...] --out docs/views/audit/ALL.jsonl [--counts docs/views/audit/COUNTS.md]

--ev holds <unit>.jsonl, the logs as the audit read them (record id = "<unit>:<line number>"). --first is the first pass that
counts (prompt v2). Each --adjudicated file is a second-pass result; a decided row (confirm, correct, retract, unverifiable)
in any of them settles its record, and when two files decide the same record the later file wins. Rows that say
"unchecked" supply the reason a flagged record was not settled.

Final verdicts, in the order they are decided:
  unseen             never audited: empty quote or a book source
  confirm            second pass read the paper's passage and the record stands
  correct            second pass found an error and gave the corrected record (corrected_record)
  retract            second pass found the record cannot stand
  unverifiable       second pass could not settle the flag from the passage it was given
  flagged_unchecked  first pass flagged it and no second pass settled it (reason says why)
  stands             first pass found no problem and nothing else was asked of it
"""
import argparse, collections, glob, json, os

DECIDED = ("confirm", "correct", "retract", "unverifiable")
ORDER = ("stands", "confirm", "correct", "retract", "unverifiable", "flagged_unchecked", "unseen")


def rows(path):
    return [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ev", required=True); ap.add_argument("--unseen", required=True); ap.add_argument("--first", required=True)
    ap.add_argument("--adjudicated", action="append", default=[]); ap.add_argument("--out", required=True)
    ap.add_argument("--counts", default="")
    a = ap.parse_args()
    unseen = {r["id"]: r for r in rows(a.unseen)}
    first = {r["id"]: r for r in rows(a.first)}
    decided, why = {}, {}
    for p in a.adjudicated:                       # earlier files first; a later decided row replaces an earlier one
        for r in rows(p):
            if r["verdict"] in DECIDED:
                decided[r["id"]] = r
            else:
                why[r["id"]] = r.get("reason", "")
    out, bad = [], 0
    for f in sorted(glob.glob(os.path.join(a.ev, "*.jsonl"))):
        u = os.path.basename(f)[:-6]
        n = 0
        for line in open(f, encoding="utf-8"):
            if not line.strip():
                continue
            n += 1
            rec = json.loads(line)
            i = "%s:%d" % (u, n)
            row = {"unit": u, "id": i, "line": n, "taxon": rec.get("taxon"), "trait": rec.get("trait"), "value": rec.get("value"),
                   "grade": rec.get("grade")}
            fp = first.get(i)
            if i in unseen:
                row.update(verdict="unseen", reason=unseen[i]["why"])
            elif i in decided:
                d = decided[i]
                row.update(verdict=d["verdict"], flags=d.get("flags", []), reason=d.get("reason", ""))
                if d.get("passage_quote"):
                    row["passage_quote"] = d["passage_quote"]
                if d["verdict"] == "correct":
                    row["corrected_record"] = d["corrected_record"]
                    row["grade_final"] = d["corrected_record"].get("grade")
                    if d.get("quote_change_found") is False:
                        row["quote_change_checked"] = False
            elif fp is not None and fp["flags"]:
                row.update(verdict="flagged_unchecked", flags=fp["flags"],
                           reason=why.get(i) or "flagged by the first pass; no second pass settled it")
                if fp.get("problem"):
                    row["first_pass"] = fp["problem"]
            elif fp is not None:
                row.update(verdict="stands", flags=[])
            else:
                row.update(verdict="flagged_unchecked", flags=["no_verdict"], reason="the first pass returned no row for this record")
                bad += 1
            out.append(row)
    with open(a.out, "w", encoding="utf-8") as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    c = collections.Counter(r["verdict"] for r in out)
    print("%d records; %s; %d with no first-pass row" % (len(out), ", ".join("%s %d" % (k, c[k]) for k in ORDER), bad))
    if a.counts:
        L = ["| unit | records | " + " | ".join(ORDER) + " |", "|---|---:|" + "---:|" * len(ORDER)]
        by = collections.defaultdict(collections.Counter)
        for r in out:
            by[r["unit"]][r["verdict"]] += 1
        for u in sorted(by):
            L.append("| %s | %d | %s |" % (u, sum(by[u].values()), " | ".join(str(by[u][k]) for k in ORDER)))
        L.append("| **all** | %d | %s |" % (len(out), " | ".join(str(c[k]) for k in ORDER)))
        L += ["", "| trait | records | " + " | ".join(ORDER) + " |", "|---|---:|" + "---:|" * len(ORDER)]
        bt = collections.defaultdict(collections.Counter)
        for r in out:
            bt[r["trait"]][r["verdict"]] += 1
        for t in sorted(bt, key=lambda t: -sum(bt[t].values())):
            L.append("| %s | %d | %s |" % (t, sum(bt[t].values()), " | ".join(str(bt[t][k]) for k in ORDER)))
        open(a.counts, "w", encoding="utf-8").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
