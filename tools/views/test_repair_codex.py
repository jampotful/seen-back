#!/usr/bin/env python3
"""python3 -I tools/views/test_repair_codex.py : checks repair_codex.py on fixtures (rules, then a small git repository with a base and two branches)."""
import importlib.util, json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("repair_codex", os.path.join(HERE, "repair_codex.py"))
R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)

fails = []
def check(name, got, want):
    if got != want: fails.append("%s: got %r, wanted %r" % (name, got, want))

def rec(**kw):
    r = {"unit": "u", "taxon": "A a", "trait": "t", "value": 1, "grade": "m", "method": "ERG", "note": "", "where": "p. 3",
         "quote": "The eye of the animal has a sharp fovea.", "source": {"authors": "Doe J, Roe R", "year": 2020, "title": "T",
         "journal": "J Vis 12(3): 1-9", "doi": "10.1000/x", "url": "u", "access": "open"}}
    r.update(kw); return r

# (a) partial
check("plain", R.partial_reason(rec()), None)
check("already", R.partial_reason(rec(note="Original paper not opened.", partial=True)), None)
check("not opened", bool(R.partial_reason(rec(note="Compiled by Healy; original paper not opened here."))), True)
check("cited not opened", bool(R.partial_reason(rec(note="Secondary report in Briscoe 2001; cited primary studies were not opened."))), True)
check("secondary method", bool(R.partial_reason(rec(method="secondary literature compilation"))), True)
check("review method", bool(R.partial_reason(rec(method="IntCell; reported by review"))), True)
check("review note", bool(R.partial_reason(rec(note="Value given in the Hunt review table."))), True)
check("abstract", bool(R.partial_reason(rec(source=dict(rec()["source"], access="abstract")))), True)
check("negated", R.partial_reason(rec(note="Primary measurement, not a secondary compilation.")), None)
check("table of a primary paper", R.partial_reason(rec(where="Table 2, row 4", method="histology")), None)

# (b) quotes
check("fine", R.quote_flag(rec()), None)
check("mid start", R.quote_flag(rec(quote="one of which encodes a long-wave pigment in the retina.")), "start")
check("cut end", R.quote_flag(rec(quote="The greatest percentage of the retina is made up of rods with 97 percent being red")), "end")
check("both", R.quote_flag(rec(quote="of the retina is made up of rods with 97 percent being red and the rest")), "both")
check("marked cut", R.quote_flag(rec(quote="... of the retina is made up of rods with 97 percent being red ...")), None)
check("short phrase", R.quote_flag(rec(quote="night-time scent")), None)
check("table row", R.quote_flag(rec(quote="Passer_domesticus,78,Passeriformes,4.88,RGC Density,6.07", where="Bird.csv row 62")), None)
check("figure caption fragment", R.quote_flag(rec(quote="the blind area is indicated by", where="Fig.2 p.882")), "start")
check("symbol lead", R.quote_flag(rec(quote="pH of 7.2 was held for the whole run of the trial.")), None)

# (c) journal, authors
check("full journal", R.journal_gaps(rec()), [])
check("no volume", R.journal_gaps(rec(source=dict(rec()["source"], journal="Current Biology"))), ["volume", "pages"])
check("no pages", R.journal_gaps(rec(source=dict(rec()["source"], journal="Current Biology 30(2)"))), ["pages"])
check("empty", R.journal_gaps(rec(source=dict(rec()["source"], journal=""))), ["journal"])
check("dataset doi", R.journal_gaps(rec(source=dict(rec()["source"], journal="Dryad", doi="10.5061/dryad.x"))), [])
check("et al", len(R.author_gaps(rec(source=dict(rec()["source"], authors="Doe J, Roe R, et al.")))), 1)
check("authors ok", R.author_gaps(rec()), [])

# the git fixture: a base and two branches that both append to u, one modifies a base line
with tempfile.TemporaryDirectory() as d:
    def g(*a): return subprocess.run(["git", "-C", d, "-c", "user.name=t", "-c", "user.email=t@t", *a], capture_output=True, text=True, check=True).stdout
    def put(name, recs):
        os.makedirs(os.path.join(d, "docs/views/evidence"), exist_ok=True)
        open(os.path.join(d, "docs/views/evidence/%s.jsonl" % name), "w").write("".join(json.dumps(r) + "\n" for r in recs))
    os.makedirs(os.path.join(d, "docs/views/recheck"), exist_ok=True)
    g("init", "-q", "-b", "main")
    b1, b2 = rec(taxon="B b"), rec(taxon="C c")
    put("u", [b1, b2]); g("add", "-A"); g("commit", "-qm", "base")
    n1 = rec(taxon="D d", note="Original paper not opened.")
    n2 = rec(taxon="E e", quote="and then the eye of the animal has a sharp fovea in the retina.")
    n3 = rec(taxon="F f", source=dict(rec()["source"], journal="Nature"))
    g("checkout", "-q", "-b", "br1"); put("u", [b1, b2, n1, n2]); g("add", "-A"); g("commit", "-qm", "b1")
    g("checkout", "-q", "main"); g("checkout", "-q", "-b", "br2"); put("u", [b1, b2, n3, n1]); put("v", [n3]); g("add", "-A"); g("commit", "-qm", "b2")
    g("checkout", "-q", "main")
    out = os.path.join(d, "out")
    p = subprocess.run([sys.executable, "-I", os.path.join(HERE, "repair_codex.py"), "--repo", d, "--base", "main", "--branch", "br1", "--branch", "br2",
                        "--out-evidence", out + "/ev", "--ledger", out + "/led.jsonl", "--fixes", out + "/fx.jsonl", "--report-dir", out + "/rep"],
                       capture_output=True, text=True)
    check("exit", p.returncode, 0)
    comb = open(out + "/ev/u.jsonl").read().split("\n")[:-1]
    check("combined length", len(comb), 5)                      # 2 base + n1, n2 from br1 + n3 from br2 (n1 is not added twice)
    check("base prefix", comb[:2], [json.dumps(b1), json.dumps(b2)])
    led = [json.loads(l) for l in open(out + "/led.jsonl")]
    check("ledger ids", [r["supersedes"] for r in led], ["u:3", "v:1"][:0] or ["u:3"])
    check("ledger flag", (led[0]["partial"], led[0]["action"], led[0]["unit"]), (True, "correct", "recheck-rp1"))
    fx = [json.loads(l) for l in open(out + "/fx.jsonl")]
    check("fixes", [(x["id"], x["partial"]) for x in fx], [("u:3", True)])
    rq = [json.loads(l) for l in open(out + "/rep/requote-candidates.jsonl")]
    check("requote", [(x["id"], x["cut"]) for x in rq], [("u:4", "start")])
    todo = [json.loads(l) for l in open(out + "/rep/crossref-todo.jsonl")]
    check("crossref todo", [(x["id"], x["missing"]) for x in todo], [("u:5", ["volume", "pages"]), ("v:1", ["volume", "pages"])])
    check("v written", os.path.exists(out + "/ev/v.jsonl"), True)
    check("main unchanged", g("show", "main:docs/views/evidence/u.jsonl").count("\n"), 2)

if fails:
    print("\n".join(fails)); sys.exit(1)
print("repair_codex: all checks passed")
