"""Builds the Papers Wanted page from the merged wanted CSV (see wanted_csv.py).
Usage: python3 -I tools/views/papers_page.py IN.csv OUT.html [BASE_IDS.json]
Each paper gets a stable id (first 10 hex of the SHA-1 of its DOI, or of its normalised title). BASE_IDS.json, when
given, receives the list of ids embedded in the page; papers found later are added to the page's shared store
(collection `extra`) by tools/views/papers_extra.py, with no republish."""
import csv, hashlib, json, re, sys, datetime, os
def norm(t): return re.sub(r'[^a-z0-9]+', ' ', (t or '').lower()).strip()
def pid(r): return hashlib.sha1(((r['doi'] or '').lower().strip() or 'title:' + norm(r['title'])).encode()).hexdigest()[:10]
def row(r): return {'id': pid(r), 'n': int(r['rank']), 'p': int(r['priority'] or 3), 'got': r['status'] == 'in Drive', 'f': r['put in folder'].replace(' (top level)', ' (top level)'),
    'a': r['authors'], 'y': r['year'], 't': r['title'], 'j': r['journal or book'], 'u': r['link'], 'h': r['how to get it'], 'w': r['why'], 's': r['species it would fix'], 'by': r['asked for by']}
if __name__ == '__main__':
    rows = [row(r) for r in csv.DictReader(open(sys.argv[1], encoding='utf-8'))]
    tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'papers_page.html'), encoding='utf-8').read()
    page = tpl.replace('__DATA__', json.dumps(rows, ensure_ascii=False).replace('</', '<\\/')).replace('__NOW__', datetime.datetime.now().strftime('%d %B %Y, %H:%M'))
    open(sys.argv[2], 'w', encoding='utf-8').write(page.replace('�', ''))
    if len(sys.argv) > 3: json.dump([r['id'] for r in rows], open(sys.argv[3], 'w'))
    print(len(rows), 'rows,', len(page) // 1024, 'KB;', len({r['id'] for r in rows}), 'unique ids')
