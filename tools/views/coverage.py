"""One line on how thorough the research is, for the end of every burst (docs/views/research/THOROUGH.md).
Usage: python3 -I tools/views/coverage.py [--views] [--no-save] [--tests "search 9/10; extraction 96%; precision 1/20"]
Settled: the share of record-rows (iNaturalist research-grade records times rows) whose traits are all m or g, from
docs/views/gaps/summary.json. Open cells (docs/views/gaps/queue.jsonl, weighted by their score) split three ways:
exhausted (a search record with the full protocol: canon, chased, two or more queries), half-searched (a search record
without it) and untouched. A search record covers a cell when its "taxon" text names the cell's species or genus, or
its family or order for pigment traits or when the record says "level": "family", and its "trait" text names the
cell's trait (tools/views/traitwords.py; free-text records are matched by a heuristic). Appends to
docs/views/gaps/coverage-history.jsonl unless --no-save. Rerun tools/views/gaps.py first so the queue is current."""
import argparse, datetime, glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from traitwords import traits_in

def full(r):
    return 'canon' in r and bool(r.get('chased')) and len(r.get('queries') or []) >= 2

def word(name, text):
    return bool(name) and re.search(r'(?<![a-z])' + re.escape(name.lower()) + r'(?![a-z])', text) is not None

def cell_status(repo):
    """Every open cell of the queue with its state: exhausted, half or untouched."""
    g = os.path.join(repo, 'docs/views/gaps')
    order_traits = set(json.load(open(os.path.join(g, 'rows.json')))['classes']['order'])
    cells = [json.loads(l) for l in open(os.path.join(g, 'queue.jsonl')) if l.strip()]
    recs = []
    for p in sorted(glob.glob(os.path.join(repo, 'docs/views/searched/*.jsonl'))):
        for l in open(p, encoding='utf-8'):
            try: r = json.loads(l)
            except ValueError: continue
            recs.append((str(r.get('taxon', '')).lower(), traits_in(str(r.get('trait', ''))), full(r), r.get('level') == 'family'))
    out = []
    for c in cells:
        st = 'untouched'
        for tax, traits, isfull, fam in recs:
            if c['trait'] not in traits: continue
            hit = c['taxon'].lower() in tax or word(c['genus'], tax) or ((c['trait'] in order_traits or fam) and (word(c['family'], tax) or word(c['order'], tax)))
            if hit:
                st = 'exhausted' if isfull else 'half'
                if isfull: break
        out.append((c, st))
    return out

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--repo', default='.'); ap.add_argument('--views', action='store_true')
    ap.add_argument('--no-save', action='store_true'); ap.add_argument('--tests', default='')
    a = ap.parse_args(); g = os.path.join(a.repo, 'docs/views/gaps')
    summary = json.load(open(os.path.join(g, 'summary.json')))
    w = {'exhausted': 0, 'half': 0, 'untouched': 0}; per = {}
    status = cell_status(a.repo); cells = [c for c, _ in status]
    for c, st in status:
        w[st] += c['score']; pv = per.setdefault(c['view'], {'exhausted': 0, 'half': 0, 'untouched': 0}); pv[st] += c['score']
    tot = sum(w.values()) or 1
    rr = sum(v['row_records'] for v in summary.values()); gr = sum(v['gap_row_records'] for v in summary.values())
    settled = 100 * (rr - gr) / rr
    views = {k: round(100 * (v['row_records'] - v['gap_row_records']) / v['row_records'], 1) for k, v in summary.items()}
    hist = os.path.join(g, 'coverage-history.jsonl'); prev = None
    if os.path.exists(hist):
        lines = [l for l in open(hist) if l.strip()]; prev = json.loads(lines[-1]) if lines else None
    pct = {k: round(100 * v / tot, 1) for k, v in w.items()}
    line = (f"Coverage: settled {settled:.1f}% of record-rows; open cells {len(cells):,} "
            f"(exhausted {pct['exhausted']}%, half-searched {pct['half']}%, untouched {pct['untouched']}% of their weight)")
    if prev:
        moves = sorted(((views[k] - prev['views'].get(k, 0), k) for k in views), reverse=True)
        moved = [f"{k} {d:+.1f}" for d, k in moves if abs(d) >= 0.1][:3]
        line += f"; since {prev['date'][:16]}: settled {settled - prev['settled']:+.1f} points" + (f" ({', '.join(moved)})" if moved else '')
    if a.tests: line += f"; tests: {a.tests}"
    print(line + '.')
    if a.views:
        for k in sorted(views, key=lambda k: views[k]):
            pv = per.get(k, {'untouched': 0}); t = sum(pv.values()) or 1
            print(f"  {k:10} settled {views[k]:5.1f}%   open weight untouched {100 * pv['untouched'] / t:5.1f}%")
    if not a.no_save:
        with open(hist, 'a') as f:
            f.write(json.dumps({'date': datetime.datetime.now().isoformat(timespec='minutes'), 'settled': round(settled, 2),
                                'open_cells': len(cells), **pct, 'views': views, 'tests': a.tests}) + '\n')

if __name__ == '__main__':
    main()
