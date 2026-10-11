# The larger model's kind of eye on wildlife photos: how often right, by its own probability (through tools/fusion/fuse.py).
import sys, json, csv, numpy as np
sys.path.insert(0, '/home/claude/seen-back/tools/fusion')
from fuse import fuse, load_slot
A = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/analysis'   # a directory with data/, lab/ and slots/nat extracted from the pub branches
slot = load_slot(f'{A}/slots/nat'); M, table = slot['manifest'], slot['table']
rows = {r['id']: r for r in csv.DictReader(open(f'{A}/data/eval/alachua-2025/manifest.csv'))}
ids = json.load(open(f'{A}/lab/bioclip2-l14/images/alachua-2025.ids.json'))
if isinstance(ids, dict): ids = ids.get('ids') or ids.get('rows')
E = np.load(f'{A}/lab/bioclip2-l14/images/alachua-2025.f16.npy').astype(np.float64); E /= np.linalg.norm(E, axis=1, keepdims=True)
KD = E @ slot['kinds'].T if slot.get('kinds') is not None else None; SD = E @ slot['species'].T
R = [rows[i] for i in ids]
out = []
for i, r in enumerate(R):
    o = fuse(M, table, int(r['month']) - 1, KD[i] if KD is not None else None, SD[i], kind_bias=slot.get('kind_bias'), species_bias=slot.get('species_bias'))
    out.append((r['split'], o['kind'] == r['eyes'], o['kindP'], bool(o['named']), (o['named'] or {}).get('sci') == r['sci']))
for sp in ('val', 'test'):
    S = [x for x in out if x[0] == sp]; n = len(S)
    print(sp, n, 'kind right %.4f' % (sum(x[1] for x in S) / n))
    for t in (0.5, 0.7, 0.8, 0.9, 0.95, 0.98, 0.99):
        a = [x for x in S if x[2] >= t]
        print('   kindP >= %.2f: asserted %.3f, right %.4f' % (t, len(a) / n, sum(x[1] for x in a) / max(1, len(a))))
    nm = [x for x in S if x[3]]
    print('   named %.3f, right %.4f; kind right when a species is named %.4f' % (len(nm) / n, sum(x[4] for x in nm) / max(1, len(nm)), sum(x[1] for x in nm) / max(1, len(nm))))
