"""Checks Codex's synonyms.tsv and homonyms.jsonl rows against GBIF. Writes out/gbif.jsonl, one verdict per row."""
import csv, json, sys, time, urllib.request, urllib.parse
out = sys.argv[1]
import os; os.makedirs(out, exist_ok=True)
def get(url):
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'seen-back-desk'}), timeout=30) as r:
                return json.load(r)
        except Exception as e:
            err = str(e); time.sleep(2 * (i + 1))
    return {'_error': err}
res = []
for r in csv.DictReader(open('ci/gbif/synonyms.tsv', encoding='utf-8'), delimiter='\t'):
    g = r['old_genus']
    m = get('https://api.gbif.org/v1/species/match?name=%s&rank=GENUS&verbose=true' % urllib.parse.quote(g))
    # every GBIF name usage for the genus string, so a homonym in another kingdom is visible
    s = get('https://api.gbif.org/v1/species/search?q=%s&rank=GENUS&status=ACCEPTED&status=SYNONYM&limit=50' % urllib.parse.quote(g))
    usages = [{'key': u.get('key'), 'name': u.get('scientificName'), 'canonical': u.get('canonicalName'), 'kingdom': u.get('kingdom'), 'family': u.get('family'), 'order': u.get('order'), 'status': u.get('taxonomicStatus'), 'accepted': u.get('accepted'), 'acceptedKey': u.get('acceptedKey')} for u in (s.get('results') or []) if u.get('canonicalName') == g]
    res.append({'file': 'synonyms', 'row': r, 'match': {k: m.get(k) for k in ('usageKey', 'scientificName', 'status', 'matchType', 'confidence', 'kingdom', 'family', 'order', 'synonym', 'acceptedUsageKey', 'note')}, 'usages': usages, 'error': m.get('_error')})
for l in open('ci/gbif/homonyms.jsonl', encoding='utf-8'):
    if not l.strip(): continue
    r = json.loads(l)
    k = get('https://api.gbif.org/v1/species/%s' % r['gbif_key'])
    res.append({'file': 'homonyms', 'row': r, 'record': {x: k.get(x) for x in ('key', 'scientificName', 'canonicalName', 'rank', 'taxonomicStatus', 'kingdom', 'order', 'family', 'accepted', 'acceptedKey')}, 'error': k.get('_error')})
with open(os.path.join(out, 'gbif.jsonl'), 'w') as f:
    for x in res: f.write(json.dumps(x, ensure_ascii=False) + '\n')
print(len(res), 'rows')
