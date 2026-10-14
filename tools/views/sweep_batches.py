"""Splits the open cells into genus batches for the round-3 sweep agents (docs/tracks/prompts/round3-sweep.md).
Usage: python3 -I tools/views/sweep_batches.py [--size 40] [--batches 3] [--out DIR]
Groups the cells of docs/views/gaps/queue.jsonl that are untouched or half-searched (coverage.py's cell_status) by genus,
orders the genera by the summed weight of those cells, and writes the next BATCHES batches of SIZE genera each to
DIR/sweep-<n>.json: [{"genus", "family", "order", "traits": [...], "species": [...], "closest": {trait: record},
"weight"}]. Prints one line per batch with its share of the open weight. Genera already in a running batch are skipped
when their names appear in DIR/running.txt, one a line, or in docs/tracks/batches/claimed.txt (handed to an outside worker)."""
import argparse, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coverage import cell_status

ap = argparse.ArgumentParser(); ap.add_argument('--size', type=int, default=40); ap.add_argument('--batches', type=int, default=3)
ap.add_argument('--out', default='.'); ap.add_argument('--repo', default='.'); a = ap.parse_args()
running = set()
for rp in (os.path.join(a.out, 'running.txt'), os.path.join(a.repo, 'docs/tracks/batches/claimed.txt')):
    if os.path.exists(rp): running |= {l.strip() for l in open(rp) if l.strip() and not l.startswith('#')}
gen = {}; total = 0
for c, st in cell_status(a.repo):
    if st == 'exhausted': continue
    total += c['score']
    if c['genus'] in running: continue
    g = gen.setdefault(c['genus'], {'genus': c['genus'], 'family': c['family'], 'order': c['order'], 'traits': set(), 'species': set(), 'closest': {}, 'weight': 0})
    g['traits'].add(c['trait']); g['species'].add(c['taxon']); g['weight'] += c['score']
    if c.get('closest_record'): g['closest'][c['trait']] = c['closest_record']
order = sorted(gen.values(), key=lambda g: -g['weight'])
os.makedirs(a.out, exist_ok=True)
for b in range(a.batches):
    batch = order[b * a.size:(b + 1) * a.size]
    if not batch: break
    for g in batch: g['traits'] = sorted(g['traits']); g['species'] = sorted(g['species'])
    path = os.path.join(a.out, f'sweep-{b + 1}.json'); json.dump(batch, open(path, 'w'), indent=1)
    w = sum(g['weight'] for g in batch)
    print(f"{path}: {len(batch)} genera, {sum(len(g['traits']) for g in batch)} genus-traits, {100 * w / max(1, total):.1f}% of the open weight; first {', '.join(g['genus'] for g in batch[:5])}")
print(f"{len(order)} genera with open cells in all")
