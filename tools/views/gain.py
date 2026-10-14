"""Judges every wanted paper against the state of the research, so the owner downloads only what is still needed.
Usage: python3 -I tools/views/gain.py IN.csv OUT.csv [--status STATUS.json] [--retire-upgrades] [--repo .]
IN.csv is wanted_csv.py's output. Each paper is matched (by DOI, else normalised title, as wanted_csv.py merges) to its
wanted lines in docs/views/wanted/*.jsonl, and through them to the cells it bears on in docs/views/gaps/cells.jsonl
(every view x species x trait with its state; written by gaps.py; queue.jsonl, open cells only, is the fallback):
- taxa: the cell's species, genus, family or order is named in the lines' "for" or "covers" fields, or in the CSV's
  "species it would fix" column; failing those, the listed species, genera, families and English names its title and
  reasons mention;
- traits: those of the lines' "rows" ("<view>:<row title>", through docs/views/gaps/rows.json); without rows, the traits
  its title and reasons name (tools/views/traitwords.py); with neither, every trait of the matched taxa;
- views: the views its rows or its "views" column name, when it names any.
A compilation line with "canon": true and "covers" counts every cell of its traits in the taxa it covers.
Verdicts (column "verdict"; the page hides "done" and "read" and lists "upgrade" after the rest of its priority):
- needed: at least one of its cells is open; ranked by the weight of its open cells (column "gain").
- upgrade: none open, but some are filled only by borrowing from a relative (g) or only by an abstract (partial file);
  the paper would give the species' own full measurement. With --retire-upgrades these become "done".
- done: every cell it bears on is measured in the species itself from a full text.
- read: the intake has already read the work in full from Drive (docs/views/sources/drive.jsonl), or an outside worker
  read a free copy of it in full (docs/views/sources/oa-*.jsonl, matched by DOI, else by title); never for a supplement
  or table entry, whose DOI is the article's.
- unknown: no taxa and no views to judge by; never retired, sorted at its priority's median gain.
--status writes {page id: {"v": verdict, "gc": open cells, "r": rank}} for the page's database document status/all (ArtifactData set), so
the page re-sorts and hides papers without a republish. Gains are estimates for ordering, never facts about a paper."""
import csv, glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from traitwords import traits_in
from papers_page import row as page_row

def norm(t): return re.sub(r'[^a-z0-9]+', ' ', (t or '').lower()).strip()
def key(doi, title): return 'doi:' + doi.lower().strip() if (doi or '').strip() else 'title:' + norm(title)
DOI = re.compile(r'10\.\d{4,9}/[^\s"\'<>]+')
WHY = {'done': 'Every gap it covers is now measured in the species itself.',
       'read': 'Already read in full, from your Drive folder or a free copy online.',
       'upgrade': "Its gaps are filled by borrowing from relatives or from an abstract; it would give the species' own measurement."}

def main():
    args = sys.argv[1:]; repo = '.'; status_out = None; retire_up = False
    if '--repo' in args: i = args.index('--repo'); repo = args[i + 1]; del args[i:i + 2]
    if '--status' in args: i = args.index('--status'); status_out = args[i + 1]; del args[i:i + 2]
    if '--retire-upgrades' in args: args.remove('--retire-upgrades'); retire_up = True
    src, out = args
    g = os.path.join(repo, 'docs/views/gaps'); rows_map = json.load(open(os.path.join(g, 'rows.json')))['views']
    cp = os.path.join(g, 'cells.jsonl')
    if os.path.exists(cp): cells = [json.loads(l) for l in open(cp) if l.strip()]
    else: cells = [dict(json.loads(l), state='i') for l in open(os.path.join(g, 'queue.jsonl')) if l.strip()]
    names_all = set()
    for c in cells:
        names_all.update(norm(x) for x in (c['taxon'], c['genus'], c['family'], c.get('en', '')) if x)
    names_all.discard('')
    lines = {}
    for p in glob.glob(os.path.join(repo, 'docs/views/wanted/*.jsonl')):
        if p.endswith('fixes.jsonl'): continue
        for l in open(p, encoding='utf-8'):
            try: w = json.loads(l)
            except ValueError: continue
            m = lines.setdefault(key(w.get('doi'), w.get('title')), {'taxa': set(), 'rows': set(), 'canon': False})
            m['taxa'].update(x.lower() for x in (w.get('for') or []) + (w.get('covers') or []) if isinstance(x, str))
            m['rows'].update(x for x in (w.get('rows') or []) if isinstance(x, str))
            m['canon'] |= bool(w.get('canon'))
    read = set()  # DOIs of files the intake read in full from Drive. Evidence sources are not used: an agent may have
    # read only the abstract of a work it then asked the owner to download.
    dp = os.path.join(repo, 'docs/views/sources/drive.jsonl')
    if os.path.exists(dp):
        for l in open(dp, encoding='utf-8'):
            try: j = json.loads(l)
            except ValueError: continue
            if j.get('doi') and not j.get('skipped'): read.add(j['doi'].lower().strip())
    read_titles = set()  # free copies an outside worker read in full (docs/tracks/prompts/oa-pass.md); oa-none-k lines are skipped
    for p in glob.glob(os.path.join(repo, 'docs/views/sources/oa-*.jsonl')):
        for l in open(p, encoding='utf-8'):
            try: j = json.loads(l)
            except ValueError: continue
            if j.get('skipped') or not j.get('read'): continue
            if (j.get('doi') or '').strip(): read.add(j['doi'].lower().strip())
            elif j.get('title'): read_titles.add(norm(j['title']))
    data = list(csv.DictReader(open(src, encoding='utf-8'))); fields = list(data[0].keys())
    for r in data:
        m = lines.get(key(r.get('doi'), r.get('title')), {'taxa': set(), 'rows': set(), 'canon': False})
        taxa = set(m['taxa']) | {s.strip().lower() for s in (r.get('species it would fix') or '').split(';') if s.strip()}
        traits, views = set(), {v.strip() for v in (r.get('views') or '').split(',') if v.strip()}
        for rw in m['rows']:
            v, _, title = rw.partition(':')
            for t, ks in rows_map.get(v.strip(), {}).items():
                if t.lower() == title.strip().lower(): traits.update(ks); views.add(v.strip())
        if not traits: traits = traits_in((r.get('title') or '') + ' ' + (r.get('why') or ''))
        if not taxa:  # older lines name their animals only in prose: take the listed species, genera and English names it mentions
            text = ' ' + norm((r.get('title') or '') + ' ' + (r.get('why') or '')) + ' '
            taxa = {n for n in names_all if len(n) > 3 and ' ' + n + ' ' in text}
        hit = {}; known = bool(taxa) or (bool(views) and bool(traits))
        for c in cells:
            if views and c['view'] not in views and not m['canon']: continue
            if traits and c['trait'] not in traits: continue
            names = (c['taxon'].lower(), c['genus'].lower(), c['family'].lower(), c['order'].lower(), norm(c['taxon']), norm(c.get('en', '')))
            if (taxa & set(names)) if taxa else (views and traits): hit[(c['view'], c['taxon'], c['trait'])] = c
        opened = [c for c in hit.values() if c['state'] == 'i']
        soft = [c for c in hit.values() if c['state'] == 'g' or (c['state'] == 'm' and not c.get('full', True))]
        supplement = re.search(r'supplement|additional file|table s\d|online table', (r.get('title') or ''), re.I)
        doi = (r.get('doi') or '').lower().strip()
        if ((doi and doi in read) or (not doi and norm(r.get('title')) in read_titles)) and not supplement: v = 'read'
        elif not known or not hit: v = 'unknown'
        elif opened: v = 'needed'
        elif soft: v = 'done' if retire_up else 'upgrade'
        else: v = 'done'
        r['verdict'] = v; r['verdict why'] = WHY.get(v, '')
        r['gain'] = sum(c['score'] for c in opened) if known else None; r['gain cells'] = len(opened)
        r['upgrade cells'] = len(soft)
        sp = {c['taxon']: c['records'] for c in opened}; r['gain species'] = len(sp); r['gain records'] = sum(sp.values())
    med = {}  # a paper with nothing to judge by sorts at its priority's median gain, neither first nor last
    for p in ('1', '2', '3'):
        gs = sorted(r['gain'] for r in data if (r['priority'] or '3') == p and r['gain'] is not None and r['verdict'] == 'needed')
        med[p] = gs[len(gs) // 2] if gs else 0
    tier = {'needed': 0, 'unknown': 0, 'upgrade': 1, 'done': 2, 'read': 2}
    data.sort(key=lambda r: (r['status'] != '', tier[r['verdict']], int(r['priority'] or 3),
                             -(r['gain'] if r['gain'] is not None else med[r['priority'] or '3']), int(r['rank'])))
    for n, r in enumerate(data, 1):
        r['rank'] = n
        if r['gain'] is None: r['gain'] = ''
    extra = [k for k in ('gain', 'gain cells', 'gain species', 'gain records', 'upgrade cells', 'verdict', 'verdict why') if k not in fields]
    with open(out, 'w', newline='', encoding='utf-8') as f:
        wr = csv.DictWriter(f, fieldnames=fields + extra); wr.writeheader(); wr.writerows(data)
    if status_out:
        st = {}
        for r in data:
            pid = page_row(r)['id']
            st[pid] = {'v': r['verdict'], 'gc': r['gain cells'], 'r': r['rank']}
        json.dump(st, open(status_out, 'w'), ensure_ascii=False, separators=(',', ':'))
    count = {}
    for r in data: count[r['verdict']] = count.get(r['verdict'], 0) + 1
    print(len(data), 'papers:', ', '.join(f'{v} {n}' for v, n in sorted(count.items(), key=lambda x: -x[1])))

if __name__ == '__main__':
    main()
