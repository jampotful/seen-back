#!/usr/bin/env python3
"""Compare two first-pass runs of the audit against the settled second-pass verdicts.

    python3 -I tools/lit/audit_compare.py --old verdicts.jsonl --new verdicts.jsonl --adjudicated adjudicated.jsonl \
        --flagged flagged.jsonl [--sample 300 --seed 1]

A settled record is one the second pass (Sonnet, reading the paper's passage) decided as confirm, correct or retract.
For each first pass the script reports:
- the flag rate over every record both runs sent;
- on the settled records: the share whose flag status agrees with the second pass (flagged exactly when the second pass
  corrected or retracted the record), the share of records the second pass confirmed that the first pass flagged (false
  alarms), the share it corrected or retracted that the first pass flagged (hits), and the grade agreement (the first
  pass's better_grade equals the grade the second pass left the record with; retracted records are left out);
- the same figures on a sample of N settled records drawn evenly across units.
"""
import argparse, collections, json, random


def rows(path):
    return [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]


def final_grade(a, given):
    if a["verdict"] == "correct":
        return (a.get("corrected_record") or {}).get("grade", given)
    return given


def stats(ids, V, A, G):
    c = collections.Counter()
    for i in ids:
        v, a = V.get(i), A[i]
        if v is None:
            c["not_sent"] += 1
            continue
        change = a["verdict"] in ("correct", "retract")
        flagged = bool(v["flags"])
        c["n"] += 1
        c["agree"] += flagged == change
        if change:
            c["changed"] += 1; c["hit"] += flagged
        else:
            c["confirmed"] += 1; c["false_alarm"] += flagged
        if a["verdict"] != "retract" and v.get("better_grade"):
            c["grade_n"] += 1
            c["grade_agree"] += v["better_grade"] == final_grade(a, G[i])
            if G[i] != final_grade(a, G[i]):
                c["gradechg_n"] += 1; c["gradechg_agree"] += v["better_grade"] == final_grade(a, G[i])
    return c


def show(name, c):
    pc = lambda x, y: "%.1f%% (%d/%d)" % (100.0 * x / y, x, y) if y else "-"
    bal = lambda h, hn, f, fn: "%.1f%%" % (50.0 * (h / hn + 1 - f / fn)) if hn and fn else "-"
    return ("%s: balanced flag accuracy (mean of hit rate and 1 minus false-alarm rate) %s; flag status agrees with the second pass %s; hit rate on corrected or retracted %s; false alarms on confirmed %s; "
            "grade agrees %s; of the records whose grade the second pass changed, grade agrees %s" % (
                name, bal(c["hit"], c["changed"], c["false_alarm"], c["confirmed"]), pc(c["agree"], c["n"]), pc(c["hit"], c["changed"]), pc(c["false_alarm"], c["confirmed"]),
                pc(c["grade_agree"], c["grade_n"]), pc(c["gradechg_agree"], c["gradechg_n"])))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--old", required=True); ap.add_argument("--new", required=True)
    ap.add_argument("--adjudicated", required=True); ap.add_argument("--flagged", required=True)
    ap.add_argument("--sample", type=int, default=300); ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    old = {r["id"]: r for r in rows(a.old)}
    new = {r["id"]: r for r in rows(a.new)}
    A = {r["id"]: r for r in rows(a.adjudicated) if r["verdict"] in ("confirm", "correct", "retract")}
    G = {r["id"]: r["record"].get("grade") for r in rows(a.flagged)}
    both = [i for i in old if i in new]
    for name, V in (("old", old), ("new", new)):
        print("%s first pass: flagged %d of %d records both runs sent (%.1f%%); grade flags %d; units flags %d; taxon flags %d" % (
            name, sum(1 for i in both if V[i]["flags"]), len(both), 100.0 * sum(1 for i in both if V[i]["flags"]) / len(both),
            sum(1 for i in both if "grade" in V[i]["flags"]), sum(1 for i in both if "units" in V[i]["flags"]),
            sum(1 for i in both if "taxon" in V[i]["flags"])))
    settled = sorted(i for i in A if i in old and i in new)
    print("settled records both runs saw: %d" % len(settled))
    by = collections.defaultdict(list)
    for i in settled:
        by[i.split(":")[0]].append(i)
    rng = random.Random(a.seed)
    sample, units = [], sorted(by)
    pools = {u: rng.sample(by[u], len(by[u])) for u in units}
    while len(sample) < min(a.sample, len(settled)):
        for u in units:
            if pools[u] and len(sample) < a.sample:
                sample.append(pools[u].pop())
    for label, ids in (("all settled", settled), ("sample of %d across %d units" % (len(sample), len({i.split(':')[0] for i in sample})), sample)):
        print("--", label)
        print(show("  old", stats(ids, old, A, G)))
        print(show("  new", stats(ids, new, A, G)))


if __name__ == "__main__":
    main()
