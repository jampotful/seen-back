"""Looks up every DOI cited in the evidence logs on Crossref, so the desk can compare authors, year, volume and
pages with the logged records without spending model allowance. Usage: python3 -I ci/crossref/crossref.py OUT_DIR
When ci/crossref/dois.txt exists (put it on the run branch only), it looks up those DOIs instead.
Writes OUT_DIR/crossref.jsonl: one line per DOI with title, authors as printed (family, given), year, journal,
volume, issue, page and type, or an error. Run by .github/workflows/crossref.yml."""
import glob, json, os, sys, time, urllib.error, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
dois = set()
only = os.path.join(ROOT, 'ci/crossref/dois.txt')  # a run branch may name its own DOIs, one a line (for example a wanted list's)
if os.path.exists(only):
    dois = {l.strip().lower() for l in open(only, encoding='utf-8') if l.strip().lower().startswith('10.')}
for p in ([] if dois else glob.glob(os.path.join(ROOT, 'docs/views/evidence/*.jsonl'))):
    for l in open(p, encoding='utf-8'):
        try: r = json.loads(l)
        except ValueError: continue
        d = str((r.get('source') or {}).get('doi', '')).strip().lower()
        if d.startswith('10.'): dois.add(d)
dois = sorted(dois)
print(len(dois), 'DOIs', flush=True)


def get(doi):
    url = 'https://api.crossref.org/works/' + urllib.parse.quote(doi, safe='/')
    for k in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'seen-back-desk/1.0'}), timeout=30) as f:
                return json.load(f)['message']
        except urllib.error.HTTPError as e:
            if e.code == 404: return {'error': 404}
            time.sleep(5 * (k + 1))
        except Exception:
            time.sleep(5 * (k + 1))
    return {'error': 'gave up'}


with open(os.path.join(out, 'crossref.jsonl'), 'w', encoding='utf-8') as fh:
    for i, d in enumerate(dois):
        m = get(d)
        if 'error' in m:
            rec = {'doi': d, 'error': m['error']}
        else:
            issued = (m.get('issued') or {}).get('date-parts') or [[None]]
            rec = {'doi': d, 'title': (m.get('title') or [''])[0],
                   'authors': [{'family': a.get('family', a.get('name', '')), 'given': a.get('given', '')} for a in m.get('author', [])],
                   'year': issued[0][0], 'journal': (m.get('container-title') or [''])[0], 'short': (m.get('short-container-title') or [''])[0],
                   'volume': m.get('volume'), 'issue': m.get('issue'), 'page': m.get('page'), 'article_number': m.get('article-number'), 'type': m.get('type')}
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n'); fh.flush()
        if i % 100 == 0: print(i, len(dois), flush=True)
        time.sleep(0.4)
