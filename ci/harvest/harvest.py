"""Searches OpenAlex from a build machine for the genera whose open cells still lack a full search, so the research
desk's agents screen results instead of searching through a rate-limited proxy.

Usage, from the repository root on a GitHub Actions runner:
    python3 -I ci/harvest/harvest.py OUT_DIR [--top 1600] [--shard 0/2]

Which genera: the open cells of docs/views/gaps/queue.jsonl that are untouched, or half-searched with no search record
that ran the full protocol (two queries and a citation step), grouped by genus and taken in order of their summed weight.
For each genus it sends to OpenAlex (15 results each): "<Genus> vision", "<Genus> eye", one query for each group of open
traits (pigments, flicker, light sensing in plants, chemical senses, daily activity), and "<English name> vision". Then
one citation step for each source of the nearest measured relative (the queue's closest_record): works citing it that
name the genus in title or abstract. Once per family it adds "<Family> vision review". Each work is kept once per genus:
OpenAlex id, DOI, title, year, venue, the open-access link, status and licence, and the abstract's first 700 characters.

Output: OUT_DIR/harvest.jsonl, one genus a line (and one line per family review; the workflow compresses it), and
OUT_DIR/summary.txt. Genera already in an earlier run on the ci branch are skipped, so each run continues the last.
The desk reads it with tools/views/harvest_get.py. Only titles, abstracts and links are kept: no full texts."""
import json, os, re, sys, time, urllib.error, urllib.parse, urllib.request

ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, 'tools', 'views'))
import coverage as cv  # noqa: E402
from traitwords import traits_in  # noqa: E402

API = 'https://api.openalex.org'
SELECT = 'id,doi,display_name,publication_year,primary_location,open_access,best_oa_location,abstract_inverted_index'
GROUPS = [  # open traits -> one extra query
    ({'lambda_max_nm', 'receptor_classes', 'spectral_range_nm', 'colour_vision'}, 'spectral sensitivity opsin'),
    ({'cff_hz', 'corner_hz'}, 'flicker fusion temporal resolution'),
    ({'sense_chemical'}, 'olfaction chemoreception'),
    ({'diel'}, 'nocturnal diurnal activity'),
    ({'interommatidial_deg', 'interreceptor_deg', 'acuity_cpd'}, 'visual acuity'),
    ({'fov_h_deg', 'binocular_deg'}, 'visual field'),
]
PLANT = ['phytochrome photoreceptor', 'light perception', 'phototropism']
calls = 0


def get(path, params):
    global calls
    url = API + path + '?' + urllib.parse.urlencode(params)
    for attempt in range(6):
        try:
            calls += 1
            req = urllib.request.Request(url, headers={'User-Agent': 'regards-harvest (github.com/jampotful/seen-back)'})
            with urllib.request.urlopen(req, timeout=40) as r:
                time.sleep(0.12)
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(2 ** attempt); continue
            return {'error': e.code}
        except Exception as e:  # network hiccup
            time.sleep(2 ** attempt); last = str(e)
    return {'error': 'gave up'}


def abstract(inv):
    if not inv: return ''
    pos = {}
    for w, ix in inv.items():
        for i in ix: pos[i] = w
    return ' '.join(pos[i] for i in sorted(pos))[:700]


def work(w):
    loc = w.get('best_oa_location') or {}
    pl = w.get('primary_location') or {}
    oa = w.get('open_access') or {}
    return {'doi': (w.get('doi') or '').replace('https://doi.org/', ''), 'title': w.get('display_name') or '',
            'year': w.get('publication_year'), 'venue': ((pl.get('source') or {}).get('display_name') or ''),
            'oa_status': oa.get('oa_status') or '', 'oa_url': loc.get('pdf_url') or loc.get('landing_page_url') or oa.get('oa_url') or '',
            'license': loc.get('license') or '', 'abstract': abstract(w.get('abstract_inverted_index'))}


def search(q, works, filt=None):
    params = {'search': q, 'per-page': 15, 'select': SELECT} if not filt else {'filter': filt, 'per-page': 25, 'select': SELECT}
    d = get('/works', params)
    if 'error' in d: return {'q': q or filt, 'error': d['error'], 'ids': []}
    ids = []
    for w in d.get('results', []):
        wid = w['id'].rsplit('/', 1)[-1]; ids.append(wid)
        works.setdefault(wid, work(w))
    return {'q': q or filt, 'n': (d.get('meta') or {}).get('count'), 'ids': ids}


def evidence_doi(ref, cache={}):
    """'oa-6#343' -> the DOI of line 343 of docs/views/evidence/oa-6.jsonl."""
    m = re.match(r'(.+)#(\d+)$', ref or '')
    if not m: return ''
    unit, n = m.group(1), int(m.group(2))
    if unit not in cache:
        p = os.path.join(ROOT, 'docs/views/evidence', unit + '.jsonl')
        cache[unit] = open(p, encoding='utf-8').read().splitlines() if os.path.exists(p) else []
    lines = cache[unit]
    if not 0 < n <= len(lines): return ''
    try: return ((json.loads(lines[n - 1]).get('source') or {}).get('doi') or '').strip()
    except (ValueError, AttributeError): return ''


GBIF_CLASS = {'insect': 'Insecta', 'bee': 'Insecta', 'bird': 'Aves', 'wader': 'Aves', 'hawk': 'Aves', 'frog': 'Amphibia',
              'deer': 'Mammalia', 'squirrel': 'Mammalia', 'dog': 'Mammalia', 'cat': 'Mammalia', 'rabbit': 'Mammalia'}


GBIF_MISS = {}


def gbif_match(t):
    """(the GBIF backbone's genus record, None) for a genus, or (None, the reason there is none). The match must be exact,
    at genus rank, and inside the group the genus's views imply (a genus name can belong to a plant and an animal, as
    Aquarius does); when the name is a homonym, GBIF's alternatives are searched for the one inside that group."""
    views = set(t['views'])
    if views == {'plant'}: hint = {'kingdom': 'Plantae'}
    elif views == {'reptile'}: hint = {'kingdom': 'Animalia', 'phylum': 'Chordata'}
    else:
        cls = {GBIF_CLASS.get(v) for v in views}
        if len(cls) != 1 or None in cls: return None, 'mixed views'
        hint = {'kingdom': 'Animalia', 'class': cls.pop()}
    url = 'https://api.gbif.org/v1/species/match?' + urllib.parse.urlencode(dict(name=t['genus'], rank='GENUS', verbose='true', **hint))
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'regards-harvest (github.com/jampotful/seen-back)'})
            with urllib.request.urlopen(req, timeout=30) as r:
                d = json.loads(r.read()); time.sleep(0.2); break
        except Exception:
            time.sleep(2 + 2 ** attempt)
    else:
        return None, 'network'
    for c in [d] + list(d.get('alternatives') or []):
        if c.get('matchType') != 'EXACT' or c.get('rank') != 'GENUS' or not c.get('family'): continue
        if (c.get('canonicalName') or c.get('scientificName') or '').split(' ')[0] != t['genus']: continue
        if any(c.get(k) != v for k, v in hint.items()): continue
        return c, None
    return None, 'no exact genus match in the group (%s)' % (d.get('matchType') or 'none')


def gbif_family(t):
    """The family the GBIF backbone gives a genus the queue lists without one, or None (gbif_match). GBIF_MISS counts the
    reasons a lookup gave nothing, for the run's summary."""
    c, why = gbif_match(t)
    if c: return c['family']
    GBIF_MISS[why] = GBIF_MISS.get(why, 0) + 1
    return None


def taxonomy_main(out, shard, nshard):
    """TAXONOMY=1 in ci/harvest/params.env: the GBIF backbone's family and order for every genus of
    docs/views/gaps/queue.jsonl listed with neither (audit 51: 1,964 of 3,820 genera, so gaps.py finds them no measured
    relative and the harvest's citation step never runs for them). Writes OUT_DIR/taxonomy.tsv in the columns of
    docs/views/gaps/taxonomy-extra.tsv and OUT_DIR/taxonomy-miss.tsv (genus, views, reason) for the genera GBIF does not
    place; nothing in the repository changes until rows are added to taxonomy-extra.tsv and gaps.py runs again. Genera
    already in taxonomy-extra.tsv or in the desk's proposal file docs/views/gaps/taxonomy-gbif.tsv are skipped. The
    backbone ranks Squamata, Testudines and Crocodylia as classes with no order beneath them (run 18: 321 reptile
    genera came back with a family and no order), so a reptile's order is taken from that class, which is the order
    the queue already gives the reptiles it places."""
    views = {}
    for l in open(os.path.join(ROOT, 'docs/views/gaps/queue.jsonl'), encoding='utf-8'):
        if not l.strip(): continue
        c = json.loads(l)
        if c.get('family') or c.get('order'): continue
        views.setdefault(c['genus'], set()).add(c['view'])
    have = set()
    for tp in ('docs/views/gaps/taxonomy-extra.tsv', 'docs/views/gaps/taxonomy-gbif.tsv'):
        if os.path.exists(os.path.join(ROOT, tp)):
            have |= {l.split('\t')[0] for l in open(os.path.join(ROOT, tp), encoding='utf-8') if l.strip()}
    mine = [g for i, g in enumerate(sorted(g for g in views if g not in have)) if i % nshard == shard]
    day = time.strftime('%Y-%m-%d', time.gmtime()); start = time.time(); n_ok = 0; why = {}
    os.makedirs(out, exist_ok=True)
    reptile_classes = {'Squamata', 'Testudines', 'Crocodylia', 'Rhynchocephalia', 'Sphenodontia'}
    with open(os.path.join(out, 'taxonomy.tsv'), 'w', encoding='utf-8') as f, \
         open(os.path.join(out, 'taxonomy-miss.tsv'), 'w', encoding='utf-8') as m:
        f.write('genus\tfamily\torder\tsource\n'); m.write('genus\tviews\treason\n')
        for g in mine:
            c, reason = gbif_match({'genus': g, 'views': views[g]})
            note = ''
            if c and not c.get('order') and views[g] == {'reptile'} and c.get('class') in reptile_classes:
                c = dict(c, order=c['class']); note = '; order from the backbone class'
            if c and not c.get('order'): c, reason = None, 'GBIF gives a family and no order (class %s)' % c.get('class')
            if c:
                n_ok += 1
                f.write(f"{g}\t{c['family']}\t{c['order']}\tGBIF backbone species/match {day} (usageKey {c.get('usageKey')}, "
                        f"class {c.get('class') or c.get('kingdom')}{note})\n")
            else:
                why[reason] = why.get(reason, 0) + 1
                m.write(f"{g}\t{','.join(sorted(views[g]))}\t{reason}\n")
    with open(os.path.join(out, 'summary.txt'), 'w') as s:
        s.write(f'taxonomy shard {shard}/{nshard}: {n_ok} of {len(mine)} genera placed by the GBIF backbone, misses {why or 0}, '
                f'{time.time() - start:.0f} s\n')
    print(open(os.path.join(out, 'summary.txt')).read())


def fill_family(t):
    """Gives a family-less target its GBIF family, so the family review step can run; returns True when it did."""
    if t['family']: return False
    fam = gbif_family(t)
    if fam: t['family'] = fam; t['family_source'] = 'GBIF backbone'
    return bool(fam)


def targets():
    """Genera to harvest, heaviest first: open cells untouched, or half-searched without a full-protocol record."""
    g = os.path.join(ROOT, 'docs/views/gaps')
    order_traits = set(json.load(open(os.path.join(g, 'rows.json')))['classes']['order'])
    by_trait = {}
    import glob
    for p in sorted(glob.glob(os.path.join(ROOT, 'docs/views/searched/*.jsonl'))):
        for l in open(p, encoding='utf-8'):
            try: r = json.loads(l)
            except ValueError: continue
            rec = (str(r.get('taxon', '')).lower(), cv.searched_fully(r), r.get('level') == 'family')
            for t in traits_in(str(r.get('trait', ''))): by_trait.setdefault(t, []).append(rec)
    out = {}
    for l in open(os.path.join(g, 'queue.jsonl'), encoding='utf-8'):
        if not l.strip(): continue
        c = json.loads(l); full = False
        for tax, fully, fam in by_trait.get(c['trait'], ()):
            if not fully: continue
            if c['taxon'].lower() in tax or cv.word(c['genus'], tax) or ((c['trait'] in order_traits or fam) and (cv.word(c['family'], tax) or cv.word(c['order'], tax))):
                full = True; break
        if full: continue
        t = out.setdefault(c['genus'], {'genus': c['genus'], 'family': c['family'], 'order': c['order'], 'english': set(),
                                         'views': set(), 'traits': set(), 'weight': 0, 'closest': set()})
        t['weight'] += c['score']; t['traits'].add(c['trait']); t['views'].add(c['view'])
        if c.get('en'): t['english'].add(c['en'])
        if c.get('closest_record'): t['closest'].add(c['closest_record'])
    return sorted(out.values(), key=lambda t: -t['weight'])


def harvested_before():
    """Genera already in an earlier harvest run on the ci branch, so a new run does only the rest."""
    import subprocess, zlib
    subprocess.run(['git', 'fetch', '-q', '--depth', '1', 'origin', '+refs/heads/ci:refs/remotes/origin/ci'], capture_output=True)
    names = subprocess.run(['git', 'ls-tree', '-r', '--name-only', 'origin/ci', 'runs/harvest'], capture_output=True, text=True).stdout.split()
    done = set()
    for n in names:
        if not n.endswith(('harvest.jsonl.gz', 'harvest.jsonl')): continue
        raw = subprocess.run(['git', 'show', 'origin/ci:' + n], capture_output=True).stdout
        if n.endswith('.gz'):
            raw = zlib.decompressobj(16 + zlib.MAX_WBITS).decompress(raw)  # a run cut off by its time limit leaves a stream without its end
        for l in raw.decode('utf-8', 'replace').splitlines():
            try: d = json.loads(l)
            except ValueError: continue
            # a genus whose searches errored (rate limit, 'gave up') is not done; a later run tries it again
            if d.get('type') == 'genus' and not any(q.get('error') for q in d.get('queries', [])): done.add(d['genus'])
    return done


def supplement_main(out, shard, nshard):
    """SUPPLEMENT=1 in ci/harvest/params.env: for genera already harvested, adds the steps the harvest never sent for
    plants (a query on the English name with 'photoreceptor' and, once per family, '<Family> photoreceptor review')
    and a '<Family> vision review' for animal families no earlier run holds. Writes 'genus_extra' lines (genus, queries,
    works) and 'family' lines; tools/views/harvest_get.py shows them under the genus. Genus lines are not rewritten. A genus the
    queue lists without a family gets its family from the GBIF backbone (gbif_family), recorded on its genus_extra line."""
    before = harvested_before(); have_q = extras_done()
    mine = [t for i, t in enumerate([t for t in targets() if t['genus'] in before]) if i % nshard == shard]
    have_fam = harvested_families()
    fam_done = set(); n_err = 0; n_fill = 0; start = time.time(); done = 0
    os.makedirs(out, exist_ok=True)
    try:
        with open(os.path.join(out, 'harvest.jsonl'), 'w', encoding='utf-8') as f:
            for i, t in enumerate(mine, 1):
                filled = fill_family(t)
                genus, fam = t['genus'], t['family']; plant = t['views'] == {'plant'}; works = {}; queries = []
                if plant:
                    for en in sorted(t['english'])[:1]:
                        if en: queries.append(search(f'{en} photoreceptor', works))
                else:  # trait queries for traits the queue opened after the genus was harvested
                    for keys, words in GROUPS:
                        q = f'{genus} {words}'
                        if keys & t['traits'] and (genus, q) not in have_q: queries.append(search(q, works))
                if queries or filled:
                    n_err += sum(1 for q in queries if q.get('error'))
                    extra = {'type': 'genus_extra', 'genus': genus, 'queries': queries, 'works': works}
                    if filled: extra.update(family=fam, family_source=t['family_source'])
                    f.write(json.dumps(extra, ensure_ascii=False) + '\n')
                    n_fill += 1 if filled else 0
                key = (fam, plant)
                if fam and key not in fam_done and (plant or fam not in have_fam):
                    fam_done.add(key); fworks = {}
                    r = search(f'{fam} photoreceptor review' if plant else f'{fam} vision review', fworks)
                    n_err += 1 if r.get('error') else 0
                    f.write(json.dumps({'type': 'family', 'family': fam, 'query': r, 'works': fworks}, ensure_ascii=False) + '\n')
                f.flush(); done = i
    except KeyboardInterrupt:
        print('stopped by the time limit; keeping what was done', flush=True)
    with open(os.path.join(out, 'summary.txt'), 'w') as s:
        s.write(f'supplement shard {shard}/{nshard}: {done} of {len(mine)} genera done, {len(fam_done)} family reviews, '
                f'{calls} OpenAlex calls, {n_err} failed queries, {n_fill} families from GBIF (misses: {GBIF_MISS or 0}), {time.time() - start:.0f} s\n')
    print(open(os.path.join(out, 'summary.txt')).read())


PLANT_TRAIT_QUERIES = {  # plant traits -> queries the plant word list misses (audit 41: a diel and a photoperiod paper missed)
    'diel': ['flower opening time', 'nyctinasty', 'anthesis', 'pollination biology'],  # audit 43: an anthesis-hours paper missed
    'sense_light_nonvisual': ['photoperiod', 'circadian rhythm'],
    'sense_chemical': ['volatile signalling'],
}


def extras_done():
    """(genus, query) pairs an earlier run's genus or genus_extra lines hold without an error, so a rerun sends only the rest."""
    import subprocess, zlib
    names = subprocess.run(['git', 'ls-tree', '-r', '--name-only', 'origin/ci', 'runs/harvest'], capture_output=True, text=True).stdout.split()
    done = set()
    for n in names:
        if not n.endswith(('harvest.jsonl.gz', 'harvest.jsonl')): continue
        raw = subprocess.run(['git', 'show', 'origin/ci:' + n], capture_output=True).stdout
        if n.endswith('.gz'): raw = zlib.decompressobj(16 + zlib.MAX_WBITS).decompress(raw)
        for l in raw.decode('utf-8', 'replace').splitlines():
            try: d = json.loads(l)
            except ValueError: continue
            if d.get('type') in ('genus_extra', 'genus'):
                for q in d.get('queries', []):
                    if not q.get('error'): done.add((d['genus'], q.get('q')))
    return done


def plant_traits_main(out, shard, nshard):
    """PLANTTRAITS=1 in ci/harvest/params.env: for plant genera already harvested, one query per open trait's words in
    PLANT_TRAIT_QUERIES, written as 'genus_extra' lines that tools/views/harvest_get.py shows under the genus."""
    before = harvested_before(); have = extras_done()  # a rerun sends only the queries no earlier run completed
    mine = [t for i, t in enumerate([t for t in targets() if t['genus'] in before and t['views'] == {'plant'}]) if i % nshard == shard]
    n_err = 0; start = time.time(); done = 0; nq = 0
    os.makedirs(out, exist_ok=True)
    try:
        with open(os.path.join(out, 'harvest.jsonl'), 'w', encoding='utf-8') as f:
            for i, t in enumerate(mine, 1):
                fill_family(t)
                words = [w for tr in sorted(t['traits']) for w in PLANT_TRAIT_QUERIES.get(tr, [])]
                qs = [f"{t['genus']} {w}" for w in words if (t['genus'], f"{t['genus']} {w}") not in have]
                works = {}; queries = []
                for q in qs:
                    queries.append(search(q, works)); time.sleep(0.5)  # run r12 lost 40% of its queries to rate limits
                nq += len(queries); n_err += sum(1 for q in queries if q.get('error'))
                if queries:
                    extra = {'type': 'genus_extra', 'genus': t['genus'], 'queries': queries, 'works': works}
                    if t.get('family_source'): extra.update(family=t['family'], family_source=t['family_source'])
                    f.write(json.dumps(extra, ensure_ascii=False) + '\n')
                f.flush(); done = i
    except KeyboardInterrupt:
        print('stopped by the time limit; keeping what was done', flush=True)
    with open(os.path.join(out, 'summary.txt'), 'w') as s:
        s.write(f'plant traits shard {shard}/{nshard}: {done} of {len(mine)} plant genera done, {nq} queries, '
                f'{calls} OpenAlex calls, {n_err} failed queries, {time.time() - start:.0f} s\n')
    print(open(os.path.join(out, 'summary.txt')).read())


def harvested_families():
    import subprocess, zlib
    names = subprocess.run(['git', 'ls-tree', '-r', '--name-only', 'origin/ci', 'runs/harvest'], capture_output=True, text=True).stdout.split()
    fams = set()
    for n in names:
        if not n.endswith(('harvest.jsonl.gz', 'harvest.jsonl')): continue
        raw = subprocess.run(['git', 'show', 'origin/ci:' + n], capture_output=True).stdout
        if n.endswith('.gz'): raw = zlib.decompressobj(16 + zlib.MAX_WBITS).decompress(raw)
        for l in raw.decode('utf-8', 'replace').splitlines():
            try: d = json.loads(l)
            except ValueError: continue
            if d.get('type') == 'family' and not (d.get('query') or {}).get('error'): fams.add(d['family'])
    return fams


def main():
    import signal
    signal.signal(signal.SIGTERM, lambda *a: (_ for _ in ()).throw(KeyboardInterrupt()))
    args = sys.argv[1:]; out = args[0]; top = 1600; shard, nshard = 0, 1
    if '--top' in args: top = int(args[args.index('--top') + 1])
    if '--shard' in args: shard, nshard = map(int, args[args.index('--shard') + 1].split('/'))
    os.makedirs(out, exist_ok=True)
    pp = os.path.join(ROOT, 'ci/harvest/params.env')
    if os.path.exists(pp) and re.search(r'^SUPPLEMENT=1\s*$', open(pp).read(), re.M):
        return supplement_main(out, shard, nshard)
    if os.path.exists(pp) and re.search(r'^PLANTTRAITS=1\s*$', open(pp).read(), re.M):
        return plant_traits_main(out, shard, nshard)
    if os.path.exists(pp) and re.search(r'^TAXONOMY=1\s*$', open(pp).read(), re.M):
        return taxonomy_main(out, shard, nshard)
    before = harvested_before()
    allt = [t for t in targets() if t['genus'] not in before]; todo = allt[:top]
    mine = [t for i, t in enumerate(todo) if i % nshard == shard]
    fam_done = set(); n_err = 0; start = time.time(); done = 0
    plain = os.path.join(out, 'harvest.jsonl')
    try:
        with open(plain, 'w', encoding='utf-8') as f:  # one line per genus, flushed, so a run stopped by its time limit keeps what it did
            for i, t in enumerate(mine, 1):
                fill_family(t); works = {}; queries = []; genus = t['genus']
                plant = t['views'] == {'plant'}
                qs = [f'{genus} {w}' for w in PLANT] if plant else [f'{genus} vision', f'{genus} eye']
                if not plant:
                    qs += [f'{genus} {words}' for keys, words in GROUPS if keys & t['traits']]
                qs += [f'{en} vision' for en in sorted(t['english'])[:1] if en and not plant]
                for q in qs: queries.append(search(q, works))
                chase = []
                for ref in sorted(t['closest'])[:3]:
                    doi = evidence_doi(ref)
                    if not doi: continue
                    d = get('/works/doi:' + doi, {'select': 'id'})
                    if 'id' not in d: chase.append({'cited_doi': doi, 'error': d.get('error', 'no id')}); continue
                    cid = d['id'].rsplit('/', 1)[-1]
                    r = search(None, works, filt=f'cites:{cid},title_and_abstract.search:{genus}')
                    chase.append({'cited_doi': doi, 'cited_id': cid, 'n': r.get('n'), 'ids': r.get('ids', []), 'error': r.get('error')})
                n_err += sum(1 for q in queries if q.get('error')) + sum(1 for c in chase if c.get('error'))
                f.write(json.dumps({'type': 'genus', 'genus': genus, 'family': t['family'], 'order': t['order'],
                                    'english': sorted(t['english']), 'views': sorted(t['views']), 'traits': sorted(t['traits']),
                                    'weight': t['weight'], 'queries': queries, 'chase': chase, 'works': works,
                                    **({'family_source': t['family_source']} if t.get('family_source') else {})}, ensure_ascii=False) + '\n')
                fam = t['family']
                if fam and fam not in fam_done and not plant:
                    fam_done.add(fam); fworks = {}
                    r = search(f'{fam} vision review', fworks)
                    f.write(json.dumps({'type': 'family', 'family': fam, 'query': r, 'works': fworks}, ensure_ascii=False) + '\n')
                f.flush(); done = i
                if i % 50 == 0: print(f'{i}/{len(mine)} genera, {calls} calls, {n_err} errors, {time.time() - start:.0f} s', flush=True)
    except KeyboardInterrupt:
        print('stopped by the time limit; keeping what was done', flush=True)
    with open(os.path.join(out, 'summary.txt'), 'w') as s:
        s.write(f'shard {shard}/{nshard}: {done} of {len(mine)} genera done, of the top {len(todo)} still needing a harvest '
                f'({len(before)} were in earlier runs), {len(fam_done)} family reviews, {calls} OpenAlex calls, '
                f'{n_err} failed queries, {time.time() - start:.0f} s\n')
    print(open(os.path.join(out, 'summary.txt')).read())


if __name__ == '__main__':
    main()
