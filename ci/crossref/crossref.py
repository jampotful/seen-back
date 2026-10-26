"""Looks up every DOI cited in the evidence logs on Crossref, so the desk can compare authors, year, volume and
pages with the logged records without spending model allowance. Usage: python3 -I ci/crossref/crossref.py OUT_DIR
When ci/crossref/dois.txt exists (put it on the run branch only), it looks up those DOIs instead.
Writes OUT_DIR/crossref.jsonl: one line per DOI with title, authors as printed (family, given), year, journal,
volume, issue, page and type, or an error. Run by .github/workflows/crossref.yml.
When ci/crossref/titles.jsonl exists (run branch only; one {"key", "title", "year"} a line, for wanted lines that
carry no DOI), it also asks Crossref's bibliographic search for each title and writes OUT_DIR/titles.jsonl: the key,
the best candidate whose title matches at 0.92 or better (and whose year is within one of a given year), and the
top three candidates, so the desk can fill a line only when the registry's title is the same work.
When ci/crossref/openalex.txt exists (run branch only; one OpenAlex work id such as W2595380620 a line, for wanted lines
that carry no DOI, often theses), it asks the OpenAlex API for each work and writes OUT_DIR/openalex.jsonl: the id, title,
year, authors as OpenAlex displays them, venue, DOI, type and open-access address."""
import glob, json, os, sys, time, urllib.error, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
dois = set()
only = os.path.join(ROOT, 'ci/crossref/dois.txt')  # a run branch may name its own DOIs, one a line (for example a wanted list's)
if os.path.exists(only):
    dois = {l.strip().lower() for l in open(only, encoding='utf-8') if l.strip().lower().startswith('10.')}
titles_in = os.path.join(ROOT, 'ci/crossref/titles.jsonl')
openalex_in = os.path.join(ROOT, 'ci/crossref/openalex.txt')
for p in ([] if dois or os.path.exists(titles_in) or os.path.exists(openalex_in) else glob.glob(os.path.join(ROOT, 'docs/views/evidence/*.jsonl'))):
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


def datacite(doi):
    """Theses, datasets and repository copies carry DataCite DOIs, which Crossref answers with 404."""
    url = 'https://api.datacite.org/dois/' + urllib.parse.quote(doi, safe='/')
    for k in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'seen-back-desk/1.0'}), timeout=30) as f:
                a = json.load(f)['data']['attributes']
            return {'doi': doi, 'title': ((a.get('titles') or [{}])[0]).get('title', ''), 'year': a.get('publicationYear'),
                    'authors': [{'family': c.get('familyName') or c.get('name', ''), 'given': c.get('givenName', '')} for c in a.get('creators', [])],
                    'journal': a.get('publisher') if isinstance(a.get('publisher'), str) else (a.get('publisher') or {}).get('name', ''),
                    'type': (a.get('types') or {}).get('resourceTypeGeneral'), 'registry': 'datacite'}
        except urllib.error.HTTPError as e:
            if e.code == 404: return None
            time.sleep(5 * (k + 1))
        except Exception:
            time.sleep(5 * (k + 1))
    return None


with open(os.path.join(out, 'crossref.jsonl'), 'w', encoding='utf-8') as fh:
    for i, d in enumerate(dois):
        m = get(d)
        if 'error' in m and m['error'] == 404 and (dc := datacite(d)):
            fh.write(json.dumps(dc, ensure_ascii=False) + '\n'); fh.flush(); time.sleep(0.4); continue
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


def norm(t):
    import re, unicodedata
    t = unicodedata.normalize('NFKD', t or '').encode('ascii', 'ignore').decode().lower()
    return re.sub(r'<[^>]+>', ' ', re.sub(r'[^a-z0-9<>/ ]+', ' ', t)).split()


def search_title(title, year):
    import difflib
    q = urllib.parse.urlencode({'query.bibliographic': title, 'rows': 5,
                                'select': 'DOI,title,author,issued,container-title,volume,issue,page,type'})
    for k in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request('https://api.crossref.org/works?' + q,
                                        headers={'User-Agent': 'seen-back-desk/1.0'}), timeout=30) as f:
                items = json.load(f)['message']['items']; break
        except Exception:
            time.sleep(5 * (k + 1))
    else:
        return {'error': 'gave up'}
    cands = []
    for m in items:
        t = (m.get('title') or [''])[0]
        yr = ((m.get('issued') or {}).get('date-parts') or [[None]])[0][0]
        score = difflib.SequenceMatcher(None, ' '.join(norm(title)), ' '.join(norm(t))).ratio()
        cands.append({'doi': m.get('DOI', '').lower(), 'title': t, 'year': yr, 'score': round(score, 3),
                      'authors': [{'family': a.get('family', a.get('name', '')), 'given': a.get('given', '')} for a in m.get('author', [])],
                      'journal': (m.get('container-title') or [''])[0], 'volume': m.get('volume'), 'issue': m.get('issue'),
                      'page': m.get('page'), 'type': m.get('type')})
    def near(a, b):
        try: return abs(int(a) - int(b)) <= 1
        except (TypeError, ValueError): return True
    ok = [c for c in cands if c['score'] >= 0.92 and near(c['year'], year)]
    return {'match': max(ok, key=lambda c: c['score']) if ok else None,
            'candidates': [{k: c[k] for k in ('doi', 'title', 'year', 'score')} for c in cands[:3]]}


if os.path.exists(titles_in):
    with open(os.path.join(out, 'titles.jsonl'), 'w', encoding='utf-8') as fh:
        for l in open(titles_in, encoding='utf-8'):
            try: q = json.loads(l)
            except ValueError: continue
            r = search_title(q.get('title', ''), q.get('year'))
            fh.write(json.dumps({'key': q.get('key'), 'query_title': q.get('title'), **r}, ensure_ascii=False) + '\n'); fh.flush()
            time.sleep(1.0)


def openalex(wid):
    url = 'https://api.openalex.org/works/' + urllib.parse.quote(wid)
    for k in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'seen-back-desk/1.0'}), timeout=30) as f:
                m = json.load(f)
            loc = m.get('primary_location') or {}
            return {'id': wid, 'title': m.get('display_name') or m.get('title') or '', 'year': m.get('publication_year'),
                    'authors': [(a.get('author') or {}).get('display_name') or a.get('raw_author_name') or '' for a in m.get('authorships', [])],
                    'venue': ((loc.get('source') or {}).get('display_name')) or '', 'doi': (m.get('doi') or '').replace('https://doi.org/', ''),
                    'type': m.get('type'), 'oa_url': ((m.get('open_access') or {}).get('oa_url')) or ''}
        except urllib.error.HTTPError as e:
            if e.code == 404: return {'id': wid, 'error': 404}
            time.sleep(5 * (k + 1))
        except Exception:
            time.sleep(5 * (k + 1))
    return {'id': wid, 'error': 'gave up'}


if os.path.exists(openalex_in):
    with open(os.path.join(out, 'openalex.jsonl'), 'w', encoding='utf-8') as fh:
        for l in open(openalex_in, encoding='utf-8'):
            wid = l.strip()
            if not wid.startswith('W'): continue
            fh.write(json.dumps(openalex(wid), ensure_ascii=False) + '\n'); fh.flush()
            time.sleep(0.5)
