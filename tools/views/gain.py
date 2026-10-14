"""Ranks the merged wanted list by how much open research each paper would close, so the owner downloads in that order.
Usage: python3 -I tools/views/gain.py IN.csv OUT.csv [--repo .]
IN.csv is wanted_csv.py's output. Each paper is matched (by DOI, else normalised title, as wanted_csv.py merges) to its
wanted lines in docs/views/wanted/*.jsonl, and to the open cells of docs/views/gaps/queue.jsonl it bears on:
- taxa: the cell's species, genus, family or order is named in the lines' "for" or "covers" fields, or in the CSV's
  "species it would fix" column;
- traits: those of the lines' "rows" ("<view>:<row title>", through docs/views/gaps/rows.json); without rows, the traits
  its title and reasons name (tools/views/traitwords.py); with neither, every open trait of the matched taxa;
- views: the views its rows or its "views" column name, when it names any.
A compilation line with "canon": true and "covers" counts every open cell of its traits in the taxa it covers.
A paper with no taxa and no views sorts at the median gain of its priority. Adds the columns gain (sum of cell weights), gain cells, gain species and gain records, and rewrites rank so that,
within each status and priority, papers that close more come first. These are estimates for ordering only."""
import csv, glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from traitwords import traits_in

def norm(t): return re.sub(r'[^a-z0-9]+', ' ', (t or '').lower()).strip()
def key(doi, title): return 'doi:' + doi.lower().strip() if (doi or '').strip() else 'title:' + norm(title)

def main():
    args = sys.argv[1:]; repo = '.'
    if '--repo' in args: i = args.index('--repo'); repo = args[i + 1]; del args[i:i + 2]
    src, out = args
    g = os.path.join(repo, 'docs/views/gaps'); rows_map = json.load(open(os.path.join(g, 'rows.json')))['views']
    cells = [json.loads(l) for l in open(os.path.join(g, 'queue.jsonl')) if l.strip()]
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
    data = list(csv.DictReader(open(src, encoding='utf-8'))); fields = list(data[0].keys())
    for r in data:
        m = lines.get(key(r.get('doi'), r.get('title')), {'taxa': set(), 'rows': set(), 'canon': False})
        taxa = set(m['taxa']) | {s.strip().lower() for s in (r.get('species it would fix') or '').split(';') if s.strip()}
        traits, views = set(), {v.strip() for v in (r.get('views') or '').split(',') if v.strip()}
        for row in m['rows']:
            v, _, title = row.partition(':')
            for t, ks in rows_map.get(v.strip(), {}).items():
                if t.lower() == title.strip().lower(): traits.update(ks); views.add(v.strip())
        if not traits: traits = traits_in((r.get('title') or '') + ' ' + (r.get('why') or ''))
        hit = {}; known = bool(taxa) or (bool(views) and bool(traits))
        for c in cells:
            if views and c['view'] not in views and not m['canon']: continue
            if traits and c['trait'] not in traits: continue
            names = (c['taxon'].lower(), c['genus'].lower(), c['family'].lower(), c['order'].lower())
            if (taxa & set(names)) if taxa else (views and traits): hit[(c['view'], c['taxon'], c['trait'])] = c
        r['gain'] = sum(c['score'] for c in hit.values()) if known else None; r['gain cells'] = len(hit)
        sp = {c['taxon']: c['records'] for c in hit.values()}; r['gain species'] = len(sp); r['gain records'] = sum(sp.values())
    med = {}  # a paper whose taxa and views are both unknown sorts at its tier's median gain, neither first nor last
    for p in ('1', '2', '3'):
        gs = sorted(r['gain'] for r in data if (r['priority'] or '3') == p and r['gain'] is not None)
        med[p] = gs[len(gs) // 2] if gs else 0
    data.sort(key=lambda r: (r['status'] != '', int(r['priority'] or 3), -(r['gain'] if r['gain'] is not None else med[r['priority'] or '3']), int(r['rank'])))
    for r in data:
        if r['gain'] is None: r['gain'] = ''
    for n, r in enumerate(data, 1): r['rank'] = n
    with open(out, 'w', newline='', encoding='utf-8') as f:
        wr = csv.DictWriter(f, fieldnames=fields + [k for k in ('gain', 'gain cells', 'gain species', 'gain records') if k not in fields])
        wr.writeheader(); wr.writerows(data)
    top = sorted(data, key=lambda r: -(r['gain'] or 0))[:6]
    print(len(data), 'papers;', sum(1 for r in data if r['gain']), 'with a gain;', sum(1 for r in data if r['gain'] == ''), 'unknown; top:', '; '.join(f"{r['title'][:45]} ({r['gain cells']} cells)" for r in top))

if __name__ == '__main__':
    main()
