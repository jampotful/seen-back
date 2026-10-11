"""Interim fusion settings for the pocket slot, chosen in a hurry on the night of 10 October 2026.

The slot exported by the evaluation was tuned on wildlife photos alone, and called a photo of a person or of a coffee
cup a plant. This script scores a grid of settings through tools/fusion/fuse.py on (a) 600 validation photos from the
wildlife set and (b) fifteen sample photos that ship with scikit-image and scikit-learn (people, objects, a cat,
plants), keeps the setting with the most sample photos right and then the best kind accuracy, and reports it on the
4,197 test photos. Fifteen photos are a sanity check, not a measurement; a head trained with photos of people and of
nothing alive replaces all of this.

Usage: python3 -I tools/eval/interim.py <directory with data/ and lab/ extracted from the pub branches>
It expects lab/tinyclip-39m-16w/images/alachua-2025.wasm-int8-per-channel.* and the slot at models/pocket.
"""
# Interim fusion settings for the pocket slot: kind accuracy on iNat val/test through tools/fusion/fuse.py,
# plus a handful of local photos of people and of nothing alive, which the wildlife photos cannot speak for.
import sys, json, csv, copy, glob, os, numpy as np
sys.path.insert(0, '/home/claude/seen-back/tools/fusion')
from fuse import fuse, dots, load_slot
from PIL import Image
import onnxruntime as ort
A = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/analysis'   # a directory holding data/ and lab/ as extracted from the pub branches
slot = load_slot('/home/claude/seen-back/models/pocket')
M0, table = slot['manifest'], slot['table']
rows = {r['id']: r for r in csv.DictReader(open(f'{A}/data/eval/alachua-2025/manifest.csv'))}
ids = json.load(open(f'{A}/lab/tinyclip-39m-16w/images/alachua-2025.wasm-int8-per-channel.ids.json'))
if isinstance(ids, dict): ids = ids.get('ids') or ids.get('rows')
E = np.load(f'{A}/lab/tinyclip-39m-16w/images/alachua-2025.wasm-int8-per-channel.f16.npy').astype(np.float64)
E /= np.linalg.norm(E, axis=1, keepdims=True)
R = [rows[i] for i in ids]
KD = E @ slot['kinds'].T; SD = E @ slot['species'].T
split = np.array([r['split'] for r in R]); eyes = np.array([r['eyes'] for r in R]); month = np.array([int(r['month']) - 1 for r in R])
# local sanity photos through the same int8 file (onnxruntime on this machine; Pillow preprocessing as the lab's)
sess = ort.InferenceSession('/home/claude/seen-back/models/pocket/vision.int8-per-channel.onnx', providers=['CPUExecutionProvider'])
mean = np.array(M0['vision']['mean'], dtype=np.float32); std = np.array(M0['vision']['std'], dtype=np.float32)
def embed(path):
    im = Image.open(path).convert('RGB'); w, h = im.size; s = 224 / min(w, h)
    im = im.resize((max(224, int(w * s)) if w >= h else 224, 224 if w >= h else max(224, int(h * s))), Image.BICUBIC)
    w, h = im.size; l, t = (w - 224) // 2, (h - 224) // 2
    x = (np.asarray(im.crop((l, t, l + 224, t + 224)), dtype=np.float32) / 255 - mean) / std
    e = sess.run(None, {'pixel_values': x.transpose(2, 0, 1)[None]})[0][0].astype(np.float64)
    return e / np.linalg.norm(e)
SK = '/usr/local/lib/python3.13/dist-packages/skimage/data/'; SL = '/usr/local/lib/python3.13/dist-packages/sklearn/datasets/images/'
sanity = [(SK + 'astronaut.png', 'person'), (SK + 'camera.png', 'person'), (SK + 'coffee.png', 'none'), (SK + 'rocket.jpg', 'none'), (SK + 'motorcycle_left.png', 'none'),
          (SK + 'brick.png', 'none'), (SK + 'gravel.png', 'none'), (SK + 'text.png', 'none'), (SK + 'page.png', 'none'), (SK + 'coins.png', 'none'), (SK + 'clock_motion.png', 'none'),
          (SK + 'chelsea.png', 'cat'), (SL + 'flower.jpg', 'plant'), (SK + 'grass.png', 'plant'), ('/home/claude/seen-back/test/assets/garden.jpg', 'plant')]
SE = [(os.path.basename(p), want, embed(p)) for p, want in sanity]
def run(fus, idx):
    M = copy.deepcopy(M0); M['fusion'].update(fus)
    ok = named = named_ok = 0
    for i in idx:
        o = fuse(M, table, int(month[i]), KD[i], SD[i])
        ok += o['kind'] == eyes[i]
        if o['named']:
            named += 1; named_ok += (o['named']['sci'] == R[i]['sci'])
    return ok / len(idx), named / len(idx), (named_ok / named if named else 0)
def sane(fus):
    M = copy.deepcopy(M0); M['fusion'].update(fus); out = []
    for name, want, e in SE:
        o = fuse(M, table, 9, dots(slot['kinds'], e), dots(slot['species'], e))
        out.append((name, want, o['kind'], round(o['kindP'], 2)))
    return out
rng = np.random.default_rng(0)
val = np.where(split == 'val')[0]; test = np.where(split == 'test')[0]
vs = rng.choice(val, 600, replace=False)
print('sanity photos under the exported settings:', [(n, w, k, p) for n, w, k, p in sane({})])
best = []
for rule in ('mix', 'product'):
    for tk in (20, 40, 60, 100):
        for wk in (0.3, 0.5, 0.7, 0.85):
            fus = {'rule': rule, 't_kind': tk, 'w_kind': wk}
            s = sane(fus); right = sum(1 for n, w, k, p in s if k == w)
            acc, nm, nmok = run(fus, vs)
            best.append((right, acc, rule, tk, wk, nm, nmok, [(n, k) for n, w, k, p in s if k != w]))
            print('%-8s t_kind %-4s w_kind %-5s sanity %2d/%d  val kind %.3f  named %.3f right %.3f  wrong: %s' % (rule, tk, wk, right, len(SE), acc, nm, nmok, [(n, k) for n, w, k, p in s if k != w]), flush=True)
best.sort(reverse=True)
r = best[0]; fus = {'rule': r[2], 't_kind': r[3], 'w_kind': r[4]}
print('chosen', fus, 'sanity', r[0], 'val kind', r[1])
print('test (all 4197): kind %.4f named %.4f right when named %.4f' % run(fus, test))
print('exported settings on test: kind %.4f named %.4f right %.4f' % run({}, test))
json.dump(fus, open(f'{A}/slots/interim_fusion.json', 'w'))
