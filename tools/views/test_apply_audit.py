#!/usr/bin/env python3
"""python3 -I tools/views/test_apply_audit.py : checks apply_audit.py on a small log in a temporary directory."""
import json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "apply_audit.py")


def run(*args):
    return subprocess.run([sys.executable, "-I", TOOL, *args], capture_output=True, text=True)


with tempfile.TemporaryDirectory() as d:
    recs = [{"taxon": "A a", "trait": "t", "value": 1, "grade": "m"}, {"taxon": "B b", "trait": "t", "value": 2, "grade": "m"},
            {"taxon": "C c", "trait": "t", "value": 3, "grade": "m"}, {"taxon": "D d", "trait": "t", "value": 4, "grade": "m"},
            {"taxon": "E e", "trait": "t", "value": 5, "grade": "m"}]
    log = os.path.join(d, "u.jsonl")
    open(log, "w").write("".join(json.dumps(r) + "\n" for r in recs))
    before = open(log).read()
    key = lambda i, v, **kw: dict({"unit": "u", "id": "u:%d" % i, "line": i, "taxon": recs[i - 1]["taxon"], "trait": "t",
                                   "value": recs[i - 1]["value"], "verdict": v}, **kw)
    allp = os.path.join(d, "ALL.jsonl")
    rows = [key(1, "stands"), key(2, "correct", corrected_record=dict(recs[1], grade="g"), reason="named a genus only"),
            key(3, "retract", reason="no such value"), key(4, "flagged_unchecked", reason="no source text"),
            dict(key(5, "correct", corrected_record=dict(recs[4], value=9)), value=6)]       # line 5 changed since the audit
    open(allp, "w").write("".join(json.dumps(r) + "\n" for r in rows))
    out = os.path.join(d, "u.corrected.jsonl")
    r = run(log, "--all", allp, "--out", out)
    assert r.returncode == 1 and "PROBLEM line 5" in r.stderr, r.stderr
    got = [json.loads(l) for l in open(out)]
    assert len(got) == 4, got                                    # the retracted line is gone
    assert got[1]["grade"] == "g" and got[1]["audit"]["was"] == {"grade": "m"}, got[1]
    assert got[2]["audit"]["verdict"] == "flagged_unchecked" and got[2]["taxon"] == "D d"
    assert got[3]["value"] == 5 and got[3]["taxon"] == "E e"     # the stale row did not touch line 5
    assert open(log).read() == before
    assert run(log, "--all", allp, "--out", log).returncode != 0 and open(log).read() == before
    assert run(log, "--all", allp, "--out", out).returncode != 0           # exists, no --force
    r = run(log, "--all", allp, "--out", out, "--force", "--retracted", "keep", "--no-mark")
    got = [json.loads(l) for l in open(out)]
    assert len(got) == 5 and all("audit" not in g for g in got) and got[2]["value"] == 3
print("ok")
