# Trials for the group head, on tuning photos only

`exp.py` runs these trials (`python3 -I tools/world/exp.py ROOT WORKTREE TRIAL`, where ROOT holds `lab/tinyclip-39m-16/images`, `data/` from `pub/data-alachua` and `world/` from `pub/data-world`). It never reads the test photos. The lines below are its outputs of 12 October 2026, recovered from the session's record after the machine they ran on was replaced; the trial names are `today`, `gap`, `C`, `ceiling`, `fold`, `mix`, `calib` and `merge`, and the last three lines are `merge` with `COMBOS=0:2:10,0:3:10,0:4:20` (power : Alachua weight : COCO weight).

Keys: `world_old` and `coco_alone` are changes in the share right against today's slot (world photos with the head alone; COCO with the head alone); `best_feasible` is `[Alachua change, COCO change, t_kind, w_kind]` for the best setting that keeps COCO within 1 point; `marks` are `[named, right when called]` per carried group; `other_view` is the share of `other` photos given a view.

```
{"carried": 19, "fails": 14, "old_world_alone": 0.0643, "other_view": 0.2, "alachua_best": [0.006, 2.0, 0.3], "coco_fused": -0.2208, "coco_alone": -0.0077, "world_right": 0.7064, "s": 122}
{'fungus': (0.483, 0.594), 'crab': (0.577, 0.523), 'mammal': (0.523, 0.525), 'worm': (0.527, 0.568), 'sealife': (0.593, 0.546), 'snail': (0.573, 0.581), 'spider': (0.7, 0.667), 'cephalopod': (0.667, 0.697), 'salamander': (0.687, 0.777), 'slime': (0.813, 0.701), 'shark': (0.743, 0.715), 'fish': (0.74, 0.716), 'scorpion': (0.727, 0.804), 'jumper': (0.763, 0.729), 'flyingfox': (0.767, 0.849), 'tick': (0.783, 0.791), 'bat': (0.833, 0.831), 'whale': (0.88, 0.833), 'primate': (0.88, 0.871)}
{"carried": 18, "fails": 13, "old_world_alone": 0.065, "other_view": 0.195, "alachua_best": [0.006, 2.0, 0.3], "coco_fused": -0.2207, "coco_alone": -0.0093, "world_right": 0.7109, "s": 133}
{'mammal': (0.533, 0.519), 'crab': (0.597, 0.52), 'worm': (0.543, 0.566), 'sealife': (0.593, 0.546), 'snail': (0.563, 0.587), 'spider': (0.703, 0.668), 'cephalopod': (0.683, 0.688), 'slime': (0.807, 0.699), 'salamander': (0.703, 0.776), 'shark': (0.743, 0.719), 'scorpion': (0.72, 0.8), 'jumper': (0.763, 0.725), 'fish': (0.747, 0.727), 'flyingfox': (0.773, 0.85), 'tick': (0.79, 0.787), 'bat': (0.83, 0.836), 'whale': (0.88, 0.838), 'primate': (0.88, 0.868)}
{"carried": 17, "fails": 12, "old_world_alone": 0.0712, "other_view": 0.2967, "alachua_best": [0.0054, 2.0, 0.3], "coco_fused": -0.2202, "coco_alone": -0.009, "world_right": 0.7089, "s": 143}
17:20:08 photos {"world": {"fit": 98518, "tune": 10200, "test": 10200, "casual": 10199}, "alachua": {"fit": 81566, "tune": 1788, "test": 4161}, "coco": {"fit": 1769, "tune": 3056, "test": 1240}}
17:20:10 parity with fuse.py on 60 Alachua photos, today's slot: 0 different
today: alachua old 0.8941, world old 0.6662, coco 0.9538
{"power": 0.0, "amult": 1.0, "world_old": 0.0436, "coco_alone": -0.01, "best_feasible": [-0.0443, -0.01, 2.0, 0.9], "best_any": [0.006, -0.2252, 2.0, 0.3], "marks": {"primate": [0.867, 0.861], "whale": [0.857, 0.865], "bat": [0.763, 0.833]}, "s": 134}
{"power": 0.0, "amult": 3.0, "world_old": 0.0364, "coco_alone": -0.0139, "best_feasible": null, "best_any": [0.0096, -0.2271, 2.0, 0.3], "marks": {"primate": [0.833, 0.871], "whale": [0.847, 0.864], "bat": [0.757, 0.819]}, "s": 112}
{"power": 0.5, "amult": 1.0, "world_old": 0.0905, "coco_alone": -0.0063, "best_feasible": [-0.0156, -0.0098, 1.0, 0.7], "best_any": [0.006, -0.2201, 2.0, 0.3], "marks": {"primate": [0.907, 0.829], "whale": [0.91, 0.791], "bat": [0.877, 0.669]}, "s": 86}
{"power": 0.5, "amult": 3.0, "world_old": 0.0793, "coco_alone": -0.0102, "best_feasible": [-0.0126, -0.0094, 0.5, 0.9], "best_any": [0.0066, -0.2219, 2.0, 0.3], "marks": {"primate": [0.883, 0.828], "whale": [0.903, 0.779], "bat": [0.843, 0.654]}, "s": 101}
{"power": 1.0, "amult": 1.0, "world_old": 0.0976, "coco_alone": -0.0051, "best_feasible": [-0.0239, -0.0051, 1.0, 0.7], "best_any": [0.0042, -0.22, 1.0, 0.3], "marks": {"primate": [0.913, 0.765], "whale": [0.93, 0.696], "bat": [0.933, 0.58]}, "s": 89}
{"power": 0.5, "amult": 1.0, "head": "raw", "groups_pass": 5, "world_old": 0.0643, "coco_alone": -0.0077, "best_feasible": [-0.0275, -0.0084, 0.5, 0.9], "s": 444}
{'primate': (0.88, 0.871), 'whale': (0.88, 0.833), 'bat': (0.833, 0.831), 'tick': (0.783, 0.791), 'flyingfox': (0.767, 0.849), 'jumper': (0.763, 0.729), 'scorpion': (0.727, 0.804), 'fish': (0.74, 0.716), 'shark': (0.743, 0.715), 'slime': (0.813, 0.701), 'salamander': (0.687, 0.777), 'spider': (0.7, 0.667), 'cephalopod': (0.667, 0.697), 'snail': (0.573, 0.581), 'sealife': (0.593, 0.546), 'worm': (0.527, 0.568), 'crab': (0.577, 0.523), 'mammal': (0.523, 0.525), 'fungus': (0.483, 0.594)}
{"power": 0.5, "amult": 1.0, "head": "calibrated", "groups_pass": 7, "world_old": 0.0619, "coco_alone": -0.0082, "best_feasible": [-0.0269, -0.0086, 0.5, 0.9], "s": 444}
{'primate': (0.873, 0.885), 'whale': (0.86, 0.854), 'bat': (0.833, 0.836), 'tick': (0.793, 0.785), 'flyingfox': (0.767, 0.846), 'scorpion': (0.753, 0.753), 'jumper': (0.75, 0.763), 'slime': (0.75, 0.74), 'fish': (0.73, 0.732), 'shark': (0.72, 0.727), 'salamander': (0.713, 0.759), 'spider': (0.67, 0.718), 'cephalopod': (0.68, 0.669), 'snail': (0.583, 0.574), 'worm': (0.537, 0.559), 'mammal': (0.53, 0.534), 'sealife': (0.597, 0.526), 'crab': (0.603, 0.516), 'fungus': (0.56, 0.511)}
{'primate': (0.88, 0.871), 'whale': (0.88, 0.833), 'bat': (0.833, 0.831), 'tick': (0.783, 0.791), 'flyingfox': (0.767, 0.849), 'jumper': (0.763, 0.729), 'scorpion': (0.727, 0.804), 'fish': (0.74, 0.716), 'shark': (0.743, 0.715), 'slime': (0.813, 0.701), 'salamander': (0.687, 0.777), 'spider': (0.7, 0.667), 'cephalopod': (0.667, 0.697), 'snail': (0.573, 0.581), 'sealife': (0.593, 0.546), 'worm'
{'primate': (0.873, 0.885), 'whale': (0.86, 0.854), 'bat': (0.833, 0.836), 'tick': (0.793, 0.785), 'flyingfox': (0.767, 0.846), 'scorpion': (0.753, 0.753), 'jumper': (0.75, 0.763), 'slime': (0.75, 0.74), 'fish': (0.73, 0.732), 'shark': (0.72, 0.727), 'salamander': (0.713, 0.759), 'spider': (0.67, 0.718), 'cephalopod': (0.68, 0.669), 'snail': (0.583, 0.574), 'worm': (0.537, 0.559), 'mammal': (0
{"power": 0.0, "amult": 1.0, "head": "raw", "groups_pass": 3, "world_old": 0.0717, "coco_alone": -0.0092, "best_feasible": [-0.0173, -0.0092, 2.0, 0.7], "s": 149}
{'primate': (0.873, 0.868), 'whale': (0.877, 0.843), 'bat': (0.833, 0.833), 'tick': (0.747, 0.818), 'flyingfox': (0.747, 0.882), 'slime': (0.77, 0.736), 'shark': (0.727, 0.734), 'fish': (0.747, 0.704), 'jumper': (0.703, 0.779), 'spider': (0.693, 0.678), 'scorpion': (0.673, 0.824), 'cephalopod': (0.667, 0.694), 'salamander': (0.653, 0.787), 'snail': (0.577, 0.582), 'sealife': (0.573, 0.557), 'c
{"power": 0.0, "amult": 1.0, "head": "calibrated", "groups_pass": 5, "world_old": 0.0705, "coco_alone": -0.0092, "best_feasible": [-0.0185, -0.0092, 2.0, 0.7], "s": 149}
{'primate': (0.863, 0.89), 'whale': (0.853, 0.859), 'bat': (0.837, 0.839), 'tick': (0.787, 0.792), 'flyingfox': (0.75, 0.882), 'salamander': (0.74, 0.745), 'slime': (0.737, 0.747), 'shark': (0.73, 0.728), 'scorpion': (0.727, 0.76), 'fish': (0.743, 0.703), 'jumper': (0.69, 0.831), 'spider': (0.683, 0.709), 'cephalopod': (0.663, 0.701), 'snail': (0.567, 0.592), 'sealife': (0.56, 0.56), 'fungus':
{"power": 1.0, "amult": 3.0, "world_old": 0.0962, "coco_alone": -0.0091, "best_feasible": [-0.0132, -0.007, 1.0, 0.7], "best_any": [0.0066, -0.2033, 0.5, 0.5], "marks": {"primate": [0.903, 0.795], "whale": [0.923, 0.682], "bat": [0.917, 0.574]}, "s": 434}
{"power": 0.0, "amult": 2.0, "cmult": 10.0, "named": ["primate", "whale", "bat"], "world_old": 0.0429, "coco_alone": 0.0053, "best_feasible": [-0.0066, 0.0051, 1.0, 0.7], "other_view": 0.1027, "marks": {"primate": [0.85, 0.873], "whale": [0.84, 0.878], "bat": [0.793, 0.847]}, "s": 139}
{"power": 0.0, "amult": 3.0, "cmult": 10.0, "named": ["primate", "whale", "bat"], "world_old": 0.0393, "coco_alone": 0.0039, "best_feasible": [-0.0036, 0.0055, 1.0, 0.7], "other_view": 0.108, "marks": {"primate": [0.86, 0.875], "whale": [0.833, 0.871], "bat": [0.79, 0.853]}, "s": 148}
{"power": 0.0, "amult": 4.0, "cmult": 20.0, "named": ["primate", "whale", "bat"], "world_old": 0.0331, "coco_alone": 0.0046, "best_feasible": [-0.0054, 0.0065, 1.0, 0.7], "other_view": 0.1149, "marks": {"primate": [0.85, 0.885], "whale": [0.837, 0.869], "bat": [0.77, 0.872]}, "s": 128}
```

## The port in head.py, on tuning photos only (13 October 2026)

`python3 -I tools/world/head.py ROOT --slot models/pocket --out OUT --recipe merge --tune-only`, and the same with `--recipe merge-other`, on TinyCLIP 39M/16 in the sandbox, before any test photo was loaded. `merge-other` is `merge` with `other`'s bias raised, in steps of 0.05, until at most 9% of the world tuning photos in `other` are given a view, then the fold and the settings again.

| On the tuning photos | today | merge | merge-other |
|---|---:|---:|---:|
| groups named (named / right when called) | | primate 0.86 / 0.8716, whale 0.8467 / 0.8639, bat 0.7967 / 0.8566 | primate 0.86 / 0.8716, whale 0.8433 / 0.8694, bat 0.79 / 0.8745 |
| old kinds right, world photos, the head alone | 0.6662 | 0.7045 | 0.6855 |
| old kinds right, Alachua photos, head and list | 0.8941 | 0.8894 | 0.8846 |
| COCO, with the list / the head alone | 0.9538 | 0.9596 / 0.9581 | 0.9567 / 0.9553 |
| `other` given a view | | 0.1133 | 0.0890 |
| settings | | t_kind 1.0, w_kind 0.7, kind_at 0.87 | t_kind 1.0, w_kind 0.7, kind_at 0.88, `other` +2.65 |

The port agrees with the trial's lines above to about half a point (bat 0.7967 / 0.8566 against 0.79 / 0.853, `other` 0.1133 against 0.108, Alachua −0.47 against −0.36 points); those lines came from a machine since replaced, and a fit's last digits follow the machine.

Chosen on these numbers, before any test photo was read: `merge-other` is the candidate to ship for TinyCLIP, since `merge` gives a view to more than 10% of `other` on the tuning photos. `merge` is read on the test photos too, as the track's brief asks (runs `m1` and `m2`, `ci/world/runs/`).

## A county bias, on tuning photos only (13 October 2026, after the test readings of `RESULTS.md`)

Both TinyCLIP heads failed only, or also, the Alachua mark on the test photos. `tools/world/county.py ROOT OUT/head.npz` (the `merge-other` head of `head.py --recipe merge-other --tune-only --dump`, fitted in the sandbox) adds, where the page uses the county list, lambda times the log of each label's share among the Alachua training photos over its weighted share among the fitting photos (world 1, COCO 10, Alachua 3) to the row's bias; person, none, cat, dog and deer, whose photos come from the COCO set, keep theirs. Today's page on these photos: Alachua old kinds 0.8941, COCO 0.9538.

| lambda | Alachua old kinds, t_kind 1.0, w_kind 0.7 | COCO with the list |
|---:|---:|---:|
| 0 | 0.8846 (−0.96 points) | 0.9567 |
| 0.25 | 0.8917 (−0.24) | 0.9589 |
| 0.5 | 0.8977 (+0.36) | 0.9606 |
| 0.75 | 0.8983 (+0.42) | 0.9606 |
| 1 | 0.8971 (+0.30) | 0.9606 |

Shifting person, none, cat, dog and deer too costs COCO 0.8 to 3.9 points at lambda 0.5 to 1. The idea came after the test photos were read, so it is to be measured on Alachua photos no recipe has seen: the tuning photos here gave −0.65 points for `merge-other`, which the test photos put at −1.89. The page would need a second bias for the kinds head, used only with the list.
