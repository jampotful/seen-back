# tools/audit: an independent check of the accuracy numbers

These scripts recompute the headline numbers of `docs/EVAL.md` and look for leaks and soft spots. They were written from the prose of `docs/EVAL.md`, `docs/CONTRACTS.md` and `tools/fusion/README.md`, and they import nothing from `tools/eval/` or `tools/fusion/`. What they found is in `docs/eval/audit.md`.

## Files

- `recompute.py`: BioCLIP 2 against the 5,911 species of the list (top-1 and top-5, with and without the month prior, the kind of eye from the top species and from summed species probabilities), and the test photos through the two slots on `main` (`models/naturalist`, `models/pocket`) by the page's rule, with and without `kind_at`, and the pocket slot on the extra set's test photos under two month rules.
- `softspots.py`: dates and overlaps between the evaluation and training manifests, near-copies between test and `val` and between test and the training photos, the numbers without them, intervals that resample whole species-days and whole days, tables by kind of eye and by the species' records, and which pets and garden plants the list holds. It also scores the trained 39M slot of run 25.
- `results/recompute.json`, `results/softspots.json`: the output of the run reported in `docs/eval/audit.md`. Each share is stored with its count, so that a percentage is rounded once.

## The files they read

`ROOT` is any directory laid out as below, filled from the bare store of the `pub/*` branches (`git --git-dir=<store> show <branch>:<path> > ROOT/<dir>/<path>`):

| Under ROOT | Branch | Paths |
|---|---|---|
| `data/` | `pub/data-alachua` | `eval/alachua-2025/manifest.csv`, `regions/us-fl-alachua/species.json`, `extra/coco-kinds/manifest.csv`, `train/alachua-pre2025/manifest.csv`, `_made.txt` |
| `bc2/` | `pub/lab-bioclip2-l14` | `images/alachua-2025.f16.npy`, `images/alachua-2025.ids.json`, `text/species_sci.f16.npy`, `text/species_sci.labels.json`, `_made.txt` |
| `tc39/` | `pub/lab-tinyclip-39m-16` | `images/alachua-2025.f16.npy` and `.ids.json`, `images/alachua-2025.wasm-int8-per-channel.f16.npy` and `.ids.json`, `images/coco-kinds.wasm-int8-per-channel.f16.npy` and `.ids.json`, `images/alachua-pre2025.f16.npy` and `.ids.json`, `_made.txt` |
| `slots/pre2025-39m/` | `pub/heads-alachua-pre2025-tinyclip-39m-16` | every file |

`REPO` is a checkout of this repository; the slots are read from `REPO/models/`.

## How to run

```
nice -n 10 env OMP_NUM_THREADS=1 python3 -I tools/audit/recompute.py ROOT REPO tools/audit/results/recompute.json
nice -n 10 env OMP_NUM_THREADS=1 python3 -I tools/audit/softspots.py ROOT REPO tools/audit/results/softspots.json
```

On two shared cores the first takes about a minute and the second about forty seconds; each stays under 1.5 GB of memory.

## Choices made

- The prior for BioCLIP 2 uses the settings `docs/eval/labelsets.md` gives as chosen on `val` for scientific names: smoothing `lam` 2 and `c` 1, prior weight over temperature 0.012, temperature 100.
- A COCO photo's month is taken two ways: from the manifest's `month` column, and from `sha256("month|" + id)` modulo 12, which `tools/eval/kinds.py` uses. The second was read in that file after the first disagreed with `docs/EVAL.md`.
- "The same photographer on the same day" is approximated by "the same species on the same day", because no manifest holds a photographer's name.
- Intervals use this audit's own seed, so their ends can differ from `docs/EVAL.md` by a tenth.

## The int8 check

The comparison of the shipped int8 file's browser vectors with the original vectors (in `docs/eval/audit.md`, two rows of the agreement table) was run by hand with the functions of `recompute.py`, from `runs/lab/25-device-hybrid-fc2-w8/wasm_hybrid-fc2-w8.f16.npy` and `.ids.json` on the `ci` branch:

```
python3 -I -c "
import json, sys, numpy as np; sys.path.insert(0, 'tools/audit'); import recompute as rc
R = 'ROOT'
man = {r['id']: r for r in rc.read_manifest(R + '/data/eval/alachua-2025/manifest.csv')}
ids = json.load(open(R + '/wasm/wasm_hybrid-fc2-w8.ids.json')); W = rc.unit(rc.load_f16_npy(R + '/wasm/wasm_hybrid-fc2-w8.f16.npy'))
slot = rc.read_slot('models/naturalist'); keys = np.array(slot['keys'])
mo = np.array([int(man[x]['month']) - 1 for x in ids]); tk = np.array([int(man[x]['key']) for x in ids])
for ka in ('manifest', None):
    r = rc.page_rule(slot, W, mo, kind_at_override=ka); n = r['named']; ok = keys[r['top']] == tk
    print(ka, n.sum(), (ok & n).sum())
"
```
