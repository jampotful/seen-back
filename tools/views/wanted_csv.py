"""Merges the research units' wanted lists into one ranked CSV for the owner's downloads.
Usage: python3 -I tools/views/wanted_csv.py OUT.csv WANTED.jsonl [WANTED.jsonl ...] [--have TITLES.txt] [--fix FIXES.jsonl] [--status docs/views/papers-status.jsonl]
Lines are merged by DOI, or by a normalised title when there is no DOI. Rank: priority, then how many units ask
for it, then the round-2 `records` field. TITLES.txt (optional) lists the titles of files already in the papers
folder, one a line; a wanted line whose first author and year both appear in a title is marked "in Drive".
Duplicates are folded: a paper without a DOI whose title equals, extends or is extended by the title of another paper by
the same first author in the same year joins that paper (one with a DOI first). Supplements, data packages (Dryad,
figshare) and "Data from" titles are never folded, since they share titles with their articles. --folds FOLDS.json
writes {folded page id: surviving page id}, so a tick on the folded copy can be carried over (papers_refresh.py)."""
import csv, json, re, sys
args = sys.argv[1:]; have = []
if '--have' in args:
    i = args.index('--have'); have = [l.strip().lower() for l in open(args[i + 1]) if l.strip()]; del args[i:i + 2]
status = {}
if '--status' in args:
    i = args.index('--status'); status = {j['id']: j['status'] for j in (json.loads(l) for l in open(args[i + 1], encoding='utf-8') if l.strip())}; del args[i:i + 2]
folds_out = None
if '--folds' in args:
    i = args.index('--folds'); folds_out = args[i + 1]; del args[i:i + 2]
fixes = []
if '--fix' in args:
    i = args.index('--fix'); fixes = [json.loads(l) for l in open(args[i + 1], encoding='utf-8') if l.strip()]; del args[i:i + 2]
out, paths = args[0], args[1:]
FOLDER = {'birds': 'Birds', 'insect': 'Insects', 'bee': 'Insects', 'spider': 'Spiders', 'jumper': 'Spiders', 'methods': 'General and methods'}
import hashlib
def pid(doi, title): return hashlib.sha1(((doi or '').lower().strip() or 'title:' + norm(title)).encode()).hexdigest()[:10]
def norm(t): return re.sub(r'[^a-z0-9]+', ' ', (t or '').lower()).strip()
merged = {}
for p in paths:
    for line in open(p, encoding='utf-8'):
        line = line.strip()
        if not line: continue
        try: w = json.loads(line)
        except ValueError: continue
        doi = (w.get('doi') or '').lower().strip()
        key = 'doi:' + doi if doi else 'title:' + norm(w.get('title'))
        m = merged.get(key)
        if m is None:
            m = merged[key] = dict(w, units=set(), views=set(), why=[], fixes=set(), records=0)
            m['priority'] = w.get('priority') or 3
        m['priority'] = min(m['priority'], w.get('priority') or 3)
        m['units'].add(w.get('unit') or '?'); m['views'].update(w.get('views') or [])
        m['fixes'].update(w.get('for') or []); m['records'] = max(m['records'], w.get('records') or 0)
        if w.get('why') and w['why'] not in m['why']: m['why'].append(w['why'])
def surname(a): return norm((a or '').split(',')[0].split(' ')[0])
for fx in fixes:  # corrections by first author and year, e.g. a placeholder title replaced by the real one
    for m in merged.values():
        if surname(m.get('authors')) == surname(fx['match']['authors']) and str(m.get('year')) == str(fx['match']['year']):
            m.update(fx['set'])
for m in merged.values():
    s, y = surname(m.get('authors')), str(m.get('year') or '')
    m['got'] = 'in Drive' if s and y and any(s in h and y in h for h in have) else ''
for m in merged.values():  # CC's marks from the Papers Wanted page: partial or n/a override a blank status
    st = status.get(pid(m.get('doi'), m.get('title')))
    if st in ('partial', 'n/a') and not m['got']: m['got'] = st
SUPP = re.compile(r'supplement|additional file|table s\d|online table|data from|dataset', re.I)
def foldable(m): return not SUPP.search(m.get('title') or '') and not re.match(r'10\.(5061|6084)/', (m.get('doi') or '').lower())
groups, folds = {}, {}
for k, m in merged.items():
    if foldable(m): groups.setdefault((surname(m.get('authors')), str(m.get('year') or '')), []).append(k)
for (sn, yr), keys in groups.items():
    if not sn or not yr or len(keys) < 2: continue
    keys.sort(key=lambda k: (not merged[k].get('doi'), len(norm(merged[k].get('title')))))  # papers with a DOI first, then the shorter title
    for k in [k for k in keys if not merged[k].get('doi')]:
        a = norm(merged[k].get('title'))
        if len(a) <= 12: continue
        for t in keys:
            if t == k or t in folds or k in folds: continue
            b = norm(merged[t].get('title'))
            if len(b) > 12 and (a.startswith(b) or b.startswith(a)):
                src, dst = merged[k], merged[t]
                dst['priority'] = min(dst['priority'], src['priority']); dst['units'] |= src['units']; dst['views'] |= src['views']
                dst['fixes'] |= src['fixes']; dst['records'] = max(dst['records'], src['records'])
                dst['why'] += [w for w in src['why'] if w not in dst['why']]
                if not dst['got'] and src['got']: dst['got'] = src['got']
                for f in ('url', 'get', 'journal'):
                    if not dst.get(f) and src.get(f): dst[f] = src[f]
                folds[k] = t; break
fold_ids = {pid(merged[k].get('doi'), merged[k].get('title')): pid(merged[t].get('doi'), merged[t].get('title')) for k, t in folds.items()}
for k in folds: del merged[k]
if folds_out: json.dump(fold_ids, open(folds_out, 'w'), indent=0)
rows = sorted(merged.values(), key=lambda m: (m['got'] != '', m['priority'], -len(m['units']), -m['records'], norm(m.get('title'))))
with open(out, 'w', newline='', encoding='utf-8') as f:
    c = csv.writer(f)
    c.writerow(['rank', 'priority', 'status', 'put in folder', 'authors', 'year', 'title', 'journal or book', 'doi', 'link', 'how to get it', 'why', 'species it would fix', 'asked for by', 'views'])
    for n, m in enumerate(rows, 1):
        got = m['got']
        units = sorted(m['units']); folder = next((f for u in units for k, f in FOLDER.items() if k in u), 'Regards papers (top level)')  # birds-met, web-insects ...
        if not m.get('journal') and re.search(r'isbn|book|chapter', (m.get('get') or '') + ' ' + ' '.join(m['why']), re.I): folder = 'Books'
        link = m.get('url') or (('https://doi.org/' + m['doi']) if m.get('doi') else '')
        c.writerow([n, m['priority'], got, folder, m.get('authors', ''), m.get('year', ''), m.get('title', ''), m.get('journal', ''), m.get('doi', ''), link,
                    m.get('get', ''), ' | '.join(m['why']), '; '.join(sorted(m['fixes'])), ', '.join(units), ', '.join(sorted(m['views']))])
print(len(rows), 'papers from', len(paths), 'lists;', len(folds), 'duplicates folded')
