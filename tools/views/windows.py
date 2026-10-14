"""Cuts a paper's text to the passages that can hold evidence, so a cheap model reads a fraction of it.
Usage: python3 -I tools/views/windows.py PAPER.txt [--width 500] [--check RECORDS.jsonl] > WINDOWS.txt
PAPER.txt is `pdftotext -layout` output (pages split by form feeds). Kept: every passage within WIDTH characters of a
trait word (tools/views/traitwords.py) or of a number with a unit of vision, and every line holding three or more
numbers (table rows) with the two lines above it. Overlaps merge; each window prints with its page and offset.
--check prints, instead of the windows, how many of the records' quotes fall inside the windows (window recall),
using the same normalisation as quotecheck.py; the extraction-recall test in THOROUGH.md uses it."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from traitwords import WORDS
from quotecheck import norm, found

UNIT = r'\d+(?:[.,]\d+)?\s*(?:c(?:ycles)?\s*(?:/|per)\s*deg\w*|cpd|hz|nm|°|deg(?:rees)?\b|µm|μm|um\b|mm\b|ms\b|%)'
WORD = '|'.join(sorted((re.escape(w) for w in WORDS if w != 'max'), key=len, reverse=True)) + r'|λ\s*max|lambda\s*max|retina|photorecept|cone|rod\b|eye'

def spans(text, width):
    out = [(max(0, m.start() - width), min(len(text), m.end() + width)) for m in re.finditer(UNIT + '|' + WORD, text, re.I)]
    pos = 0
    lines = text.split('\n')
    starts = []
    for ln in lines: starts.append(pos); pos += len(ln) + 1
    for i, ln in enumerate(lines):
        if len(re.findall(r'(?<![\w.])\d+(?:[.,]\d+)?(?![\w.])', ln)) >= 3:
            a = starts[max(0, i - 2)]; out.append((a, starts[i] + len(ln)))
    out.sort(); merged = []
    for a, b in out:
        if merged and a <= merged[-1][1]: merged[-1] = (merged[-1][0], max(b, merged[-1][1]))
        else: merged.append((a, b))
    return merged

if __name__ == '__main__':
    args = sys.argv[1:]; width = 500; check = None
    if '--width' in args: i = args.index('--width'); width = int(args[i + 1]); del args[i:i + 2]
    if '--check' in args: i = args.index('--check'); check = args[i + 1]; del args[i:i + 2]
    text = open(args[0], encoding='utf-8', errors='replace').read()
    sp = spans(text, width)
    kept = sum(b - a for a, b in sp)
    if check:
        recs = [json.loads(l) for l in open(check, encoding='utf-8') if l.strip()]
        win = norm('\n'.join(text[a:b] for a, b in sp)); whole = norm(text)
        inpaper = [r for r in recs if found(r.get('quote', ''), whole)]
        inwin = [r for r in inpaper if found(r.get('quote', ''), win)]
        print(f'windows keep {kept:,} of {len(text):,} characters ({100 * kept / max(1, len(text)):.0f}%); '
              f'quotes found in the paper {len(inpaper)} of {len(recs)}; of those inside the windows {len(inwin)} '
              f'({100 * len(inwin) / max(1, len(inpaper)):.0f}%)')
        for r in inpaper:
            if r not in inwin: print('  missed:', r.get('quote', '')[:120])
    else:
        for a, b in sp:
            page = text.count('\f', 0, a) + 1
            print(f'=== page {page}, offset {a}\n{text[a:b].strip()}\n')
        print(f'=== kept {kept:,} of {len(text):,} characters', file=sys.stderr)
