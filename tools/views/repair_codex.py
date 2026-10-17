"""Repairs the evidence that the closed Codex branches added (pull requests 18, 19 and 20), without any model call.

For each evidence file it takes the lines a branch adds to main, appends them in branch order to main's own lines (so
every id "<unit>:<line>" on main stays what it was), and then, for the added lines only:
  (a) sets partial: true where the record shows a compiled table, review, secondary report, appendix compilation or an
      abstract-only read (the audit 27 rule), as a ledger row (action "correct", supersedes "<unit>:<line>") and as a line
      of a fixes file that tools/views/gaps.py reads;
  (b) lists quotes that open mid-sentence or stop before the sentence does, as requote candidates (the tool never writes
      quote text, because the sentence has to be read on the page);
  (c) lists journal fields without a volume or pages, and author lists that were shortened, for the Crossref step the desk
      runs (python3 -I tools/views/crossref_compare.py on a run/crossref result);
  (d) carries the audit rows that audits 28, 29 and 31 wrote (recheck-<n>.jsonl on research/audit-<n>) over to the new
      line numbers, matching records by content, so that retractions and requotes already found are not lost.
Nothing in an evidence line is rewritten: the ledger holds the corrected copies, as the desk's Crossref fix does.

Usage:
  python3 -I tools/views/repair_codex.py --base origin/main --branch origin/codex-round-2026-10-16 --branch ... \\
      --out-evidence docs/views/evidence --ledger docs/views/recheck/recheck-rp1.jsonl \\
      --fixes docs/views/fixes/codex-partial.jsonl --report-dir docs/views/repair \\
      [--audit origin/research/audit-28:28 ...] [--units oa-1,oa-2 ...] [--repo DIR]
"""
import argparse, collections, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UNIT = "recheck-rp1"

# ---------- (a) the partial flag ----------
NOT_OPENED = re.compile(
    r"original(?: paper| article| study| work)?(?: was| is| were)? not (?:been )?(?:opened|read|seen|accessed|checked|obtained)"
    r"|(?:cited|primary|underlying|source) (?:studies|study|papers?|sources?|articles?|references?|works?)[^.;]{0,40}"
    r"(?:were|was|are|is) not (?:opened|read|seen|accessed|obtained)", re.I)
SECONDARY = re.compile(r"\bsecondary\b", re.I)
COMPILED = re.compile(r"\bcompil(?:ation|ed|es)\b", re.I)
REVIEWED = re.compile(r"\breview\b", re.I)
NEG = re.compile(r"(?:\bnot\b|\bno\b|\bnor\b|\bnever\b|\bnon\b|\bwithout\b)[^.;]{0,25}$", re.I)


def _hits(pattern, text):
    """Matches of pattern in text that no negation ("not a compilation") sits just before."""
    return [m.group(0) for m in pattern.finditer(text) if not NEG.search(text[max(0, m.start() - 30):m.start()])]


def partial_reason(r):
    """The reason this record must carry partial: true, or None. Deterministic; reads method, note, where and access."""
    if r.get("partial"):
        return None
    method, note, where = (str(r.get(k) or "") for k in ("method", "note", "where"))
    text = " ".join((method, note, where))
    why = []
    h = [m.group(0) for m in NOT_OPENED.finditer(text)]
    if h: why.append("the record says the original was not opened (%r)" % h[0].lower())
    if _hits(SECONDARY, text): why.append("the record calls the read secondary")
    if _hits(COMPILED, method + " " + where) or _hits(re.compile(r"\bcompiled (?:by|from|in|classification|dataset|table)", re.I), note):
        why.append("the value is read from a compilation")
    if _hits(REVIEWED, method) or _hits(re.compile(r"\b(?:in|by|from|via) (?:the |a |an )?[^.;]{0,60}\breview\b", re.I), note):
        why.append("the value is read from a review")
    acc = str((r.get("source") or {}).get("access") or "").lower()
    if acc in ("abstract", "closed"):
        why.append("access is %s, so only an abstract or a page was read" % acc)
    return "; ".join(why) or None


# ---------- (b) the quote ----------
TABULAR = re.compile(r"\b(?:table|csv|xlsx?|sheet|row|rows|column|supplement\w*|dataset|appendix|S\d|tsv|spreadsheet)\b", re.I)
SMALL_LEAD = re.compile(r"^(?:[a-z]{1,2}[A-Z0-9]|[a-z]+[A-Z]|pH\b|n\s*=|mRNA|rRNA|cDNA|eBird|iNat|et al|dB\b|cm\b|mm\b|nm\b|um\b|µm\b|kHz\b|Hz\b|ms\b|c/deg\b|cpd\b)")


def quote_flag(r):
    """'start' when the quote opens in mid-sentence, 'end' when it stops before the sentence does, 'both', or None.
    Table rows, spreadsheet lines and figure labels are the pipeline's convention and are left alone."""
    q = r.get("quote")
    if not isinstance(q, str) or not q.strip():
        return None
    q = q.strip()
    where = str(r.get("where") or "")
    if "\t" in q or TABULAR.search(where) or (q.count(",") >= 4 and re.search(r"\d", q)):
        return None
    out = []
    if len(q.split()) < 5: return None          # a short phrase is a deliberate quotation of a term
    if q[0] not in "…[(\"'“‘" and not q.startswith("...") and q[0].isalpha() and q[0].islower() and not SMALL_LEAD.match(q):
        out.append("start")
    if len(q.split()) >= 8 and q[-1] not in ".?!\"”')]" and not q.endswith(("…", "...")):
        out.append("end")
    return "both" if len(out) == 2 else (out[0] if out else None)


# ---------- (c) journal and authors ----------
NOT_JOURNAL = re.compile(r"data ?portal|dryad|zenodo|figshare|repository|thesis|dissertation|web page|wikipedia|preprint|biorxiv|"
                         r"github|database|dataset|archive|handbook|book|proceedings of the \w+ conference", re.I)
DATA_DOI = re.compile(r"^10\.(?:5061|5281|6084|5519|1101|17632|5555|25675|4121|48550|31219)/")


def journal_gaps(r):
    s = r.get("source") or {}
    j = str(s.get("journal") or "").strip()
    doi = str(s.get("doi") or "").strip().lower()
    if not doi or DATA_DOI.match(doi) or NOT_JOURNAL.search(j):
        return []
    if not j:
        return ["journal"]
    if not re.search(r"\d", j):
        return ["volume", "pages"]
    out = []
    if ":" not in j and not re.search(r"\b\d+\s*[-–]\s*\d+\b|\be\d+\b", j): out.append("pages")
    return out


def author_gaps(r):
    a = str((r.get("source") or {}).get("authors") or "").strip()
    if not a: return ["authors empty"]
    if re.search(r"\bet al\b|…|\.\.\.", a, re.I): return ["author list shortened with et al or an ellipsis"]
    return []


# ---------- the evidence lines ----------
def git(repo, *args):
    p = subprocess.run(["git", "-C", repo, *args], capture_output=True)
    return p.stdout.decode("utf-8") if p.returncode == 0 else None


def show(repo, ref, path):
    t = git(repo, "show", "%s:%s" % (ref, path))
    return [] if t is None else [l for l in t.split("\n") if l.strip()]


def lines_added(base, branch):
    """The branch's lines that main does not have (multiset difference), in the branch's order, and the base lines the branch dropped."""
    have = collections.Counter(base)
    added = []
    for l in branch:
        if have[l] > 0: have[l] -= 1
        else: added.append(l)
    gone = collections.Counter(branch)
    dropped = []
    for l in base:
        if gone[l] > 0: gone[l] -= 1
        else: dropped.append(l)
    return added, dropped


def combine(base, branches):
    """main's lines, then each branch's added lines not already present. Returns lines and the branch label per added line."""
    out = list(base)
    seen = collections.Counter(base)
    label = {}
    for name, bl in branches:
        add, _ = lines_added(base, bl)
        for l in add:
            if seen[l] > 0: continue
            seen[l] += 1
            out.append(l)
            label[len(out)] = name
    return out, label


def ckey(r):
    return (r.get("taxon"), r.get("trait"), json.dumps(r.get("value"), sort_keys=True), (r.get("source") or {}).get("doi"), r.get("quote"))


def ledger_row(r, rid, action, reason, **over):
    nr = {k: v for k, v in r.items() if k not in ("rechecked", "audit", "supersedes", "action", "reason", "from_audit")}
    nr.update(over)
    nr.update({"unit": UNIT, "supersedes": rid, "action": action, "reason": reason})
    return nr


FIX = lambda rid: {"id": rid, "partial": True, "reason": "read from a compilation, table, review, secondary report or abstract (repair_codex, 17 October 2026)"}


def build(units, base, branches, audit_rows=(), only_added=True):
    """units: names. base/branches: functions (unit) -> lines. Returns a dict with the combined files, ledger, fixes and reports."""
    res = {"combined": {}, "ledger": [], "fixes": [], "requote": [], "journal": [], "authors": [], "dropped": [],
           "counts": collections.Counter(), "audit_unmatched": []}
    index = {}
    for u in units:
        b = base(u)
        lines, label = combine(b, [(n, f(u)) for n, f in branches])
        res["combined"][u] = lines
        for n, f in branches:
            _, dropped = lines_added(b, f(u))
            for l in dropped:
                res["dropped"].append({"unit": u, "branch": n, "line": l})
        for i in range(len(b) + 1, len(lines) + 1):
            try: r = json.loads(lines[i - 1])
            except ValueError: continue
            index.setdefault(ckey(r), []).append("%s:%d" % (u, i))
    audited = {}
    for ar in audit_rows:
        ids = index.get(ckey(ar["_original"]), []) if ar.get("_original") else []
        if not ids:
            res["audit_unmatched"].append(ar.get("supersedes"))
            continue
        audited[ids[0]] = ar
    for u, lines in res["combined"].items():
        nb = len(base(u))
        for i in range(nb + 1, len(lines) + 1):
            rid = "%s:%d" % (u, i)
            try: r = json.loads(lines[i - 1])
            except ValueError: continue
            res["counts"]["added"] += 1
            if rid in audited:
                ar = audited[rid]
                row = {k: v for k, v in ar.items() if not k.startswith("_")}
                row.update({"unit": UNIT, "supersedes": rid, "from_audit": ar.get("unit")})
                pr = partial_reason(row)
                if pr and not row.get("partial") and row.get("action") != "retract":
                    row["partial"] = True; row["reason"] = row.get("reason", "") + " Also: partial set by the repair rule (%s)." % pr
                if row.get("partial") and not r.get("partial") and row.get("action") != "retract":
                    res["fixes"].append(FIX(rid))
                res["ledger"].append(row)
                res["counts"]["audit_" + str(row.get("action"))] += 1
                if row.get("action") == "retract":
                    continue
                r = row
            else:
                pr = partial_reason(r)
                if pr:
                    res["ledger"].append(ledger_row(r, rid, "correct", "Partial flag set by script (tools/views/repair_codex.py, audit 27 rule): %s." % pr, partial=True))
                    res["counts"]["partial_set"] += 1
                    res["counts"]["partial_set:" + u] += 1
                    res["fixes"].append(FIX(rid))
            qf = quote_flag(r)
            if qf:
                res["requote"].append({"id": rid, "doi": (r.get("source") or {}).get("doi"), "cut": qf, "quote": r.get("quote"), "where": r.get("where")})
                res["counts"]["requote:" + qf] += 1
            jg = journal_gaps(r)
            if jg:
                res["journal"].append({"id": rid, "doi": (r.get("source") or {}).get("doi"), "journal": (r.get("source") or {}).get("journal"), "missing": jg})
                res["counts"]["journal"] += 1
            ag = author_gaps(r)
            if ag:
                res["authors"].append({"id": rid, "doi": (r.get("source") or {}).get("doi"), "authors": (r.get("source") or {}).get("authors"), "fault": ag[0]})
                res["counts"]["authors"] += 1
    return res


def load_audit(repo, ref, n):
    """Audit rows of recheck-<n>.jsonl on ref, each with the original record found in ref's own evidence file at the superseded line."""
    out = []
    for l in show(repo, ref, "docs/views/recheck/recheck-%s.jsonl" % n):
        try: ar = json.loads(l)
        except ValueError: continue
        sup = str(ar.get("supersedes") or "")
        m = re.match(r"^([\w-]+):(\d+)$", sup)
        if not m: continue
        ev = git(repo, "show", "%s:docs/views/evidence/%s.jsonl" % (ref, m.group(1)))
        if ev is None: continue
        ev = ev.split("\n")
        try: ar["_original"] = json.loads(ev[int(m.group(2)) - 1])
        except (ValueError, IndexError): continue
        out.append(ar)
    return out


def write_jsonl(path, rows):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=ROOT)
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--branch", action="append", required=True)
    ap.add_argument("--units")
    ap.add_argument("--out-evidence")
    ap.add_argument("--ledger"); ap.add_argument("--fixes"); ap.add_argument("--report-dir")
    ap.add_argument("--audit", action="append", default=[], help="REF:N, the audit branch and its recheck number")
    a = ap.parse_args(argv)
    ev = "docs/views/evidence/%s.jsonl"
    if a.units: units = a.units.split(",")
    else:
        names = set()
        for ref in a.branch:
            d = git(a.repo, "diff", "--name-only", a.base, ref, "--", "docs/views/evidence") or ""
            names.update(os.path.basename(x)[:-6] for x in d.split() if x.endswith(".jsonl"))
        units = sorted(names)
    baseL = lambda u: show(a.repo, a.base, ev % u)
    branches = [(ref.split("/", 1)[-1], (lambda u, ref=ref: show(a.repo, ref, ev % u))) for ref in a.branch]
    audit = []
    for spec in a.audit:
        ref, n = spec.rsplit(":", 1)
        audit += load_audit(a.repo, ref, n)
    res = build(units, baseL, branches, audit)
    res["combined"] = {u: v for u, v in res["combined"].items() if len(v) > len(baseL(u))}
    if a.out_evidence:
        os.makedirs(a.out_evidence, exist_ok=True)
        for u, lines in res["combined"].items():
            open(os.path.join(a.out_evidence, u + ".jsonl"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    if a.ledger: write_jsonl(a.ledger, res["ledger"])
    if a.fixes: write_jsonl(a.fixes, res["fixes"])
    if a.report_dir:
        d = a.report_dir
        write_jsonl(os.path.join(d, "requote-candidates.jsonl"), res["requote"])
        write_jsonl(os.path.join(d, "crossref-todo.jsonl"), res["journal"] + res["authors"])
        dois = sorted({x["doi"] for x in res["journal"] + res["authors"] if x["doi"]})
        open(os.path.join(d, "crossref-dois.txt"), "w").write("\n".join(dois) + "\n")
        write_jsonl(os.path.join(d, "dropped-main-lines.jsonl"), res["dropped"])
        json.dump({"counts": dict(sorted(res["counts"].items())), "audit_unmatched": res["audit_unmatched"], "units": units,
                   "lines": {u: len(v) for u, v in res["combined"].items()}},
                  open(os.path.join(d, "counts.json"), "w"), indent=1)
    print(json.dumps(dict(sorted(res["counts"].items())), indent=1))
    print("audit rows unmatched:", len(res["audit_unmatched"]), "| main lines a branch dropped:", len(res["dropped"]))


if __name__ == "__main__":
    main()
