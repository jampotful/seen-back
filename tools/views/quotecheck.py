"""Checks that each record's quote is in the paper, for free, before any model is asked.
Usage: python3 -I tools/views/quotecheck.py PAPER.pdf|PAPER.txt RECORDS.jsonl
A quote passes "verbatim" when it is in the text after normalising both sides (case, ligatures, dashes, quotation marks,
hyphens at line ends, whitespace); a quote with an ellipsis passes when each part of 15 characters or more, and each shorter part that holds a digit, is present in the quote's order.
Agents often quote a table row as a reworded line ("Columba livia Feral pigeon: UVS/VS 409, SWS 453 ..."); such a
quote passes "table" when a line of the `pdftotext -layout` text (or the line after it) names the record's taxon and
holds every number of the quote. Everything else FAILs and goes to a stronger model or is dropped. Given a PDF, the
script runs pdftotext itself (reading order for prose, -layout for tables). Exits 1 when any record fails."""
import json, re, subprocess, sys

def norm(t):
    t = (t or '').lower().replace('­', '')
    for a, b in (('ﬁ', 'fi'), ('ﬂ', 'fl'), ('ﬀ', 'ff'), ('ﬃ', 'ffi'), ('ﬄ', 'ffl'), ('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'),
                 ('–', '-'), ('—', '-'), ('−', '-'), ('‐', '-'), ('μ', 'µ'), ('\f', ' ')):
        t = t.replace(a, b)
    t = re.sub(r'-\s*\n\s*', '', t)
    return re.sub(r'\s+', ' ', t).strip()

def found(quote, normtext):
    parts = [p.strip(' .,;:') for p in re.split(r'\.\.\.|…|\[\.\.\.\]', norm(quote))]
    # a short piece is dropped as too weak to prove anything, unless it holds a digit: a number must be in the text too
    parts = [p for p in parts if len(p) >= 15 or re.search(r'\d', p)] or [norm(quote)]
    if not parts[0]: return False
    pos = 0
    for p in parts:  # the pieces must come in the quote's order
        i = normtext.find(p, pos)
        if i < 0: return False
        pos = i + len(p)
    return True

NUM = r'(?<![\d.])\d+(?:\.\d+)?(?![\d])'
def table_found(quote, taxon, lines):
    nums = set(re.findall(NUM, quote or ''))
    tax = re.sub(r'\s+', ' ', (taxon or '').lower()).strip()
    if not nums or not tax: return False
    for i, ln in enumerate(lines):
        if tax in re.sub(r'\s+', ' ', ln.lower()):
            nxt = lines[i + 1] if i + 1 < len(lines) else ''
            if re.match(r'\s*[A-Z][a-z]+ [a-z]{3,}\b', nxt): nxt = ''  # the next line is another taxon's row: its numbers are not this row's
            near = set(re.findall(NUM, ln + ' ' + nxt))
            if nums <= near: return True
    return False

def texts(path):
    if path.lower().endswith('.pdf'):
        raw = subprocess.run(['pdftotext', path, '-'], capture_output=True, text=True).stdout
        lay = subprocess.run(['pdftotext', '-layout', path, '-'], capture_output=True, text=True).stdout
    else:
        raw = lay = open(path, encoding='utf-8', errors='replace').read()
    return norm(raw), lay.split('\n')

def check(rec, raw, lines):
    q = rec.get('quote', '')
    if found(q, raw): return 'verbatim'
    if table_found(q, rec.get('taxon'), lines): return 'table'
    return 'fail'

if __name__ == '__main__':
    raw, lines = texts(sys.argv[1]); count = {'verbatim': 0, 'table': 0, 'fail': 0}
    for line in open(sys.argv[2], encoding='utf-8'):
        if not line.strip(): continue
        r = json.loads(line); k = check(r, raw, lines); count[k] += 1
        if k == 'fail': print('FAIL', r.get('taxon', ''), r.get('trait', ''), '|', r.get('quote', '')[:100])
    print(f"{count['verbatim']} verbatim, {count['table']} table rows, {count['fail']} failed")
    sys.exit(1 if count['fail'] else 0)
