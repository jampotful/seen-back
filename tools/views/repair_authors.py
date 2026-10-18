"""Full author lists for lines the repair branch added: where the logged list ends in "et al." or is shorter than
Crossref's, writes recheck rows (action "correct") that replace it with Crossref's complete list in the repo's style
(Family INITIALS, comma separated). Usage: python3 -I tools/views/repair_authors.py CROSSREF.jsonl[.gz] --n NUMBER --base origin/main"""
import glob, gzip, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def initials(given):
    out = ''
    for p in re.split(r'[\s.]+', given.replace('-', ' -').strip()):
        p = p.lstrip('-')
        if p and p[0].isalpha(): out += p[0].upper()
    return out


def main():
    path = sys.argv[1]; num = sys.argv[sys.argv.index('--n') + 1]; base = sys.argv[sys.argv.index('--base') + 1]
    cr = {}
    for l in (gzip.open if path.endswith('.gz') else open)(path, 'rt', encoding='utf-8'):
        try: d = json.loads(l)
        except ValueError: continue
        if 'error' not in d and d.get('authors'): cr[d['doi']] = d
    rows = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'docs/views/evidence/*.jsonl'))):
        unit = os.path.basename(f)[:-6]
        if unit.startswith('recheck-'): continue
        t = subprocess.run(['git', '-C', ROOT, 'show', f'{base}:docs/views/evidence/{unit}.jsonl'], capture_output=True, text=True)
        have = len(t.stdout.split('\n')) - 1 if t.returncode == 0 else 0
        for i, l in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
            if i <= have or not l.strip(): continue
            try: r = json.loads(l)
            except ValueError: continue
            s = r.get('source') or {}
            m = cr.get(str(s.get('doi', '')).strip().lower())
            a = str(s.get('authors', ''))
            if not m: continue
            names = [x for x in re.split(r',\s*|;\s*', a) if x.strip() and not re.search(r'et al', x, re.I)]
            if not (re.search(r'et al', a, re.I) or len(m['authors']) > len(names)): continue
            full = []
            for x in m['authors']:
                fam = x['family'].strip()
                if fam.isupper() and len(fam) > 3: fam = fam.title()
                full.append(f"{fam} {initials(x['given'])}".strip())
            new_a = ', '.join(full)
            if new_a == a: continue
            nr = {k: v for k, v in r.items() if k not in ('rechecked', 'audit')}
            nr['source'] = dict(s, authors=new_a)
            nr.update({'unit': f'recheck-{num}', 'supersedes': f'{unit}:{i}', 'action': 'correct',
                       'reason': 'Complete author list from Crossref (build-machine lookup, run/crossref): the logged list was cut short or ended in "et al.".'})
            rows.append(nr)
    open(os.path.join(ROOT, f'docs/views/recheck/recheck-{num}.jsonl'), 'w', encoding='utf-8').write(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in rows))
    print(len(rows), 'rows')


main()
