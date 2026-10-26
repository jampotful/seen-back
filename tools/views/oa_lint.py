#!/usr/bin/env python3
"""Mechanical checks for evidence records before they are committed (the faults audits 16 to 39 kept finding).

    python3 -I tools/views/oa_lint.py <records.jsonl or evidence file> [--text <paper text file>] [--since-main <branch>]

With a JSONL file it checks every record in it. With --since-main <branch> it checks only the lines that branch adds to
docs/views/evidence/ compared with origin/main. Exit status 1 when any record fails. Checks:
  value-in-quote   every number in `value` appears in `quote` (digits compared after removing spaces and thousands
                   separators; ± parts and ranges count number by number). A value read from a table row must quote the row.
  quote-shape      the quote does not start mid-sentence (a lower-case first letter, unless it begins with a mark of a cut
                   "…", a species epithet or a unit), and every cut is marked with … or ...
  quote-in-text    with --text: every piece of the quote between cut marks is in the text (spaces normalized)
  (grades: `m` for a value on the record's own taxon, a species or the group it names, own or cited; `g` for a taxon
                   mismatch, a presumption or a prediction; docs/views/audit/SAMPLE.md. Not checked here: it needs the passage.)
  partial          a note that says review, compilation, compiled, cited, after, from <Author>, Table S or "read from Fig"
                   requires partial: true
  source           authors, year, title, journal, doi or url present; a journal string carries a volume (a number) unless
                   the note says why it has none
"""
import json
import re
import subprocess
import sys

NUM = re.compile(r"\d+(?:\.\d+)?")
WORDS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
         "ten": "10", "eleven": "11", "twelve": "12", "single": "1", "half": "0.5", "both": "2", "twice": "2", "double": "2",
         "dichromatic": "2", "trichromatic": "3", "tetrachromatic": "4", "monochromatic": "1"}
PARTIAL_WORDS = re.compile(r"\b(review|compilation|compiled|cited|citing|after [A-Z]|from [A-Z][a-z]+ (?:et al|and|\()|table s\d|read from fig|secondary)\b", re.I)
SPECIES = re.compile(r"^[A-Z][a-z]+ (?:\([A-Z][a-z]+\) )?(?:x |× )?[a-z][a-z\-]+(?: (?:(?:subsp|ssp|var|f|cv)\. )?[a-z][a-z\-]+)?$")


def nums(s, words=False):
    s = re.sub(r"(?<=\d)[\u2009\u202f\u00a0](?=\d)", "", str(s))
    s = re.sub(r"(?<=\d),(?=\d{3}(?!\d))", "", s)   # thousands separators (no space after the comma)
    s = re.sub(r"(?<=\d),(?=\d{1,2}(?!\d))", ".", s)  # decimal commas
    out = NUM.findall(s)
    if words:
        out += [WORDS[w] for w in re.findall(r"[a-z]+", s.lower()) if w in WORDS]
    return out


def norm(t):
    return re.sub(r"\s+", " ", t or "").strip()


def check(r, text=None):
    errs = []
    q = r.get("quote") or ""
    qn = set(nums(q, words=True)) | set(NUM.findall(q))  # a CSV row such as "104,44,18.7" holds the numbers as printed as well
    qn |= {n.rstrip("0").rstrip(".") for n in qn if "." in n}
    for n in nums(r.get("value", "")):
        n2 = n.rstrip("0").rstrip(".") if "." in n else n
        if n not in qn and n2 not in qn:
            errs.append("value-in-quote: %s is not in the quote" % n)
    qs = q.strip()
    if qs and qs[0].islower() and qs[0].isascii() and not qs.startswith(("…", "...")):   # Greek symbols (β-ionone, α-lobe) may open a sentence
        errs.append("quote-shape: starts mid-sentence (%r)" % qs[:30])
    if text is not None:
        tn = norm(text)
        for piece in [p for p in re.split(r"\s*(?:…|\.\.\.)\s*", norm(q)) if p.strip()]:
            if piece not in tn:
                errs.append("quote-in-text: %r not found" % piece[:60])
                break
    if PARTIAL_WORDS.search(r.get("note") or "") and not r.get("partial"):
        errs.append("partial: the note says the value is not this paper's own measurement")
    s = r.get("source") or {}
    for k in ("authors", "year", "title", "journal"):
        if not s.get(k):
            errs.append("source: no %s" % k)
    if not (s.get("doi") or s.get("url")):
        errs.append("source: no doi or url")
    if s.get("journal") and not re.search(r"\d", s["journal"]) and "volume" not in (r.get("note") or "").lower():
        errs.append("source: journal has no volume (%r)" % s["journal"][:50])
    return errs


def main():
    args = sys.argv[1:]
    text = None
    if "--text" in args:
        i = args.index("--text"); text = open(args[i + 1], encoding="utf-8", errors="replace").read(); del args[i:i + 2]
    lines = []
    if "--since-main" in args:
        i = args.index("--since-main"); br = args[i + 1]; del args[i:i + 2]
        d = subprocess.run(["git", "diff", "origin/main..." + br, "--", "docs/views/evidence/"], capture_output=True, text=True).stdout
        cur = None
        for l in d.splitlines():
            if l.startswith("+++ "):
                cur = l[6:]
            elif l.startswith("+{"):
                lines.append((cur, l[1:]))
    for f in args:
        lines += [(f, l) for l in open(f) if l.strip()]
    bad = 0
    for n, (f, l) in enumerate(lines, 1):
        r = json.loads(l)
        e = check(r, text)
        if e:
            bad += 1
            print("%s #%d %s %s: %s" % (f, n, r.get("taxon"), r.get("trait"), "; ".join(e)))
    print("%d records, %d with faults" % (len(lines), bad))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
