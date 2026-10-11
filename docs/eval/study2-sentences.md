# Sentence rows with the prior, as the page would use them

_This file is written by `tools/eval/report.py` from `docs/eval/study2-sentences.json`. Rerun the script to change it._

No head was fitted here. The models' own sentence rows were given the prior, the calibration and the page's combination with the kind phrases, with every setting chosen on the whole of `val`. These are the slots that can ship before any training photo exists.

## tinyclip-39m-16

Fitted on 0 photos of 0 species (`none (sentence rows only)`); settings chosen on 1803 tuning photos; tested on 4197 test photos (`images/alachua-2025.wasm-int8-per-channel`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 22.9% (21.7 to 24.1) | 40.1% (38.7 to 41.6) | 34.8% (33.4 to 36.3) | 53.8% (52.3 to 55.3) | 82.9% (81.7 to 84.0) | species_com; alpha 1.00; lam 2, c 1 |

| Kind of eye from | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 77.3% (76.0 to 78.7) | 0.05% | 0.10% |
| summed species probabilities of the head `sentences` | 82.9% (81.7 to 84.0) | 0.00% | 0.00% |
| the page's combination of kind phrases and the species list (rule `product`, t_kind 20, w_kind 0.5; species head `sentences`) | 84.4% (83.4 to 85.5) | 0.00% | 0.00% |

**The kind decision.** The kinds head, its temperature, its weight against the species list and the rule were chosen on 1803 wildlife tuning photos alone, because this model's vectors of the extra set (people, pets, livestock, rooms) were not published when this ran. The number tuned on is the share right on the wildlife tuning photos (the extra set's vectors were not published for this model). Each row is one kinds head under one rule at its best setting on the tuning photos. `kind_at` is the level this computation gives for an asserted kind to be right 95 times in 100 on each tuning set by itself; the level a slot ships with is set by `tools/eval/shipped.py` through `fuse.py`.

|  | Kinds head | Rule | t_kind | w_kind | Tuning number | Wildlife tuning photos | Extra tuning photos | Kind right, wildlife test | Kind right, extra test | kind_at | Asserted, wildlife test | Right when asserted | Asserted, extra test | Right when asserted |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | kind phrases | mix | 20 | 0.5 | 84.2% | 84.2% | – | 84.0% (82.8 to 85.1) | – | 0.39 | 65.8% (64.3 to 67.3) | 96.4% (95.7 to 97.0) | – | – |
|  | kind phrases | product | 20 | 0.5 | 84.4% | 84.4% | – | 84.4% (83.4 to 85.5) | – | 0.42 | 68.4% (67.0 to 69.8) | 95.7% (95.0 to 96.5) | – | – |
| **chosen** | kind phrases | product | 20 | 0.5 | 84.4% | 84.4% | – | 84.4% (83.4 to 85.5) | – | 0.42 | 68.4% (67.0 to 69.8) | 95.7% (95.0 to 96.5) | – | – |
| what the wildlife photos alone would choose | kind phrases | product | 20 | 0.5 | 84.4% | 84.4% | – | 84.4% (83.4 to 85.5) | – | 0.42 | 68.4% (67.0 to 69.8) | 95.7% (95.0 to 96.5) | – | – |

**Confidence.** For the head `sentences`, the scale was set on the tuning photos (expected calibration error 0.153 there). A species is named when its probability is at least 0.40, the lowest level from which named species were right at least nine times in ten on the tuning photos; three species are offered when the first three together reach 0.60, set the same way. On the test photos a species is then named for 15.4% (14.3 to 16.6) of photos and that name is right for 92.7% (90.7 to 94.6) of them; three species are offered for 1.9% (1.5 to 2.3) and hold the right one for 92.4% (86.1 to 97.5); 82.7% (81.5 to 83.8) get a kind of eye only. These figures leave out the page's rule that names and offers must agree with the winning kind; the exported slot is scored with that rule.

| Top probability | Tuning photos | Mean probability | Share right |
|---|---:|---:|---:|
| 0.0 to 0.1 | 866 | 5.2% | 12.5% |
| 0.1 to 0.2 | 361 | 14.1% | 30.2% |
| 0.2 to 0.3 | 171 | 24.6% | 46.2% |
| 0.3 to 0.4 | 97 | 35.4% | 70.1% |
| 0.4 to 0.5 | 85 | 45.4% | 71.8% |
| 0.5 to 0.6 | 59 | 54.8% | 94.9% |
| 0.6 to 0.7 | 66 | 65.3% | 98.5% |
| 0.7 to 0.8 | 45 | 74.8% | 100.0% |
| 0.8 to 0.9 | 36 | 84.4% | 97.2% |
| 0.9 to 1.0 | 17 | 93.0% | 100.0% |

- The extra set's vectors (people, pets, livestock, rooms) were not published for this model when this ran, so the kind decision was tuned on wildlife photos alone and says nothing about a person or an empty room.

## tinyclip-8m-16

Fitted on 0 photos of 0 species (`none (sentence rows only)`); settings chosen on 1803 tuning photos; tested on 4197 test photos (`images/alachua-2025.wasm-int8-per-channel`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 14.1% (13.0 to 15.1) | 29.7% (28.4 to 31.1) | 25.3% (24.0 to 26.7) | 43.2% (41.8 to 44.7) | 76.5% (75.2 to 77.8) | species_com; alpha 0.62; lam 0, c 0.1 |

| Kind of eye from | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 72.4% (71.0 to 73.8) | 0.05% | 0.21% |
| summed species probabilities of the head `sentences` | 76.5% (75.2 to 77.8) | 0.00% | 0.00% |
| the page's combination of kind phrases and the species list (rule `product`, t_kind 20, w_kind 0.5; species head `sentences`) | 78.9% (77.7 to 80.1) | 0.00% | 0.00% |

**The kind decision.** The kinds head, its temperature, its weight against the species list and the rule were chosen on 1803 wildlife tuning photos alone, because this model's vectors of the extra set (people, pets, livestock, rooms) were not published when this ran. The number tuned on is the share right on the wildlife tuning photos (the extra set's vectors were not published for this model). Each row is one kinds head under one rule at its best setting on the tuning photos. `kind_at` is the level this computation gives for an asserted kind to be right 95 times in 100 on each tuning set by itself; the level a slot ships with is set by `tools/eval/shipped.py` through `fuse.py`.

|  | Kinds head | Rule | t_kind | w_kind | Tuning number | Wildlife tuning photos | Extra tuning photos | Kind right, wildlife test | Kind right, extra test | kind_at | Asserted, wildlife test | Right when asserted | Asserted, extra test | Right when asserted |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | kind phrases | mix | 20 | 0.7 | 78.9% | 78.9% | – | 78.8% (77.6 to 80.1) | – | 0.43 | 14.0% (13.0 to 15.1) | 97.6% (96.3 to 98.6) | – | – |
|  | kind phrases | product | 20 | 0.5 | 78.9% | 78.9% | – | 78.9% (77.7 to 80.1) | – | 0.54 | 31.1% (29.7 to 32.6) | 98.3% (97.6 to 99.0) | – | – |
| **chosen** | kind phrases | product | 20 | 0.5 | 78.9% | 78.9% | – | 78.9% (77.7 to 80.1) | – | 0.54 | 31.1% (29.7 to 32.6) | 98.3% (97.6 to 99.0) | – | – |
| what the wildlife photos alone would choose | kind phrases | product | 20 | 0.5 | 78.9% | 78.9% | – | 78.9% (77.7 to 80.1) | – | 0.54 | 31.1% (29.7 to 32.6) | 98.3% (97.6 to 99.0) | – | – |

**Confidence.** For the head `sentences`, the scale was set on the tuning photos (expected calibration error 0.111 there). A species is named when its probability is at least 0.42, the lowest level from which named species were right at least nine times in ten on the tuning photos; three species are offered when the first three together reach 0.49, set the same way. On the test photos a species is then named for 9.2% (8.3 to 10.1) of photos and that name is right for 89.7% (86.6 to 92.8) of them; three species are offered for 5.1% (4.5 to 5.8) and hold the right one for 83.8% (78.7 to 88.4); 85.6% (84.6 to 86.7) get a kind of eye only. These figures leave out the page's rule that names and offers must agree with the winning kind; the exported slot is scored with that rule.

| Top probability | Tuning photos | Mean probability | Share right |
|---|---:|---:|---:|
| 0.0 to 0.1 | 1041 | 4.9% | 8.4% |
| 0.1 to 0.2 | 343 | 14.2% | 28.6% |
| 0.2 to 0.3 | 141 | 24.0% | 48.9% |
| 0.3 to 0.4 | 92 | 34.2% | 63.0% |
| 0.4 to 0.5 | 64 | 44.9% | 75.0% |
| 0.5 to 0.6 | 49 | 54.8% | 91.8% |
| 0.6 to 0.7 | 29 | 64.0% | 89.7% |
| 0.7 to 0.8 | 29 | 75.3% | 100.0% |
| 0.8 to 0.9 | 10 | 85.4% | 100.0% |
| 0.9 to 1.0 | 5 | 92.7% | 100.0% |

- The extra set's vectors (people, pets, livestock, rooms) were not published for this model when this ran, so the kind decision was tuned on wildlife photos alone and says nothing about a person or an empty room.

## bioclip2-l14

Fitted on 0 photos of 0 species (`none (sentence rows only)`); settings chosen on 1803 tuning photos; tested on 4197 test photos (`images/alachua-2025`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 90.3% (89.4 to 91.3) | 96.8% (96.2 to 97.3) | 92.5% (91.6 to 93.2) | 97.5% (97.0 to 97.9) | 98.3% (97.9 to 98.7) | species_sci; alpha 1.00; lam 2, c 1 |

| Kind of eye from | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 76.1% (74.8 to 77.4) | 0.00% | 0.00% |
| summed species probabilities of the head `sentences` | 98.3% (97.9 to 98.7) | 0.00% | 0.00% |
| the page's combination of kind phrases and the species list (rule `mix`, t_kind 20, w_kind 0.7; species head `sentences`) | 98.3% (97.8 to 98.6) | 0.00% | 0.00% |

**The kind decision.** The kinds head, its temperature, its weight against the species list and the rule were chosen on 1803 wildlife tuning photos alone, because this model's vectors of the extra set (people, pets, livestock, rooms) were not published when this ran. The number tuned on is the share right on the wildlife tuning photos (the extra set's vectors were not published for this model). Each row is one kinds head under one rule at its best setting on the tuning photos. `kind_at` is the level this computation gives for an asserted kind to be right 95 times in 100 on each tuning set by itself; the level a slot ships with is set by `tools/eval/shipped.py` through `fuse.py`.

|  | Kinds head | Rule | t_kind | w_kind | Tuning number | Wildlife tuning photos | Extra tuning photos | Kind right, wildlife test | Kind right, extra test | kind_at | Asserted, wildlife test | Right when asserted | Asserted, extra test | Right when asserted |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | kind phrases | mix | 20 | 0.7 | 98.3% | 98.3% | – | 98.3% (97.8 to 98.6) | – | 0.20 | 99.6% (99.5 to 99.8) | 98.5% (98.1 to 98.9) | – | – |
|  | kind phrases | product | 20 | 0.5 | 98.3% | 98.3% | – | 98.3% (97.9 to 98.6) | – | 0.20 | 99.9% (99.8 to 100.0) | 98.4% (98.0 to 98.7) | – | – |
| **chosen** | kind phrases | mix | 20 | 0.7 | 98.3% | 98.3% | – | 98.3% (97.8 to 98.6) | – | 0.20 | 99.6% (99.5 to 99.8) | 98.5% (98.1 to 98.9) | – | – |
| what the wildlife photos alone would choose | kind phrases | mix | 20 | 0.7 | 98.3% | 98.3% | – | 98.3% (97.8 to 98.6) | – | 0.20 | 99.6% (99.5 to 99.8) | 98.5% (98.1 to 98.9) | – | – |

**Confidence.** For the head `sentences`, the scale was set on the tuning photos (expected calibration error 0.024 there). A species is named when its probability is at least 0.05, the lowest level from which named species were right at least nine times in ten on the tuning photos; no level for offers reached nine in ten. On the test photos a species is then named for 100.0% (100.0 to 100.0) of photos and that name is right for 92.5% (91.6 to 93.2) of them; three species are offered for 0.0% (0.0 to 0.0) and hold the right one for –; 0.0% (0.0 to 0.0) get a kind of eye only. These figures leave out the page's rule that names and offers must agree with the winning kind; the exported slot is scored with that rule.

| Top probability | Tuning photos | Mean probability | Share right |
|---|---:|---:|---:|
| 0.0 to 0.1 | 3 | 6.8% | 0.0% |
| 0.1 to 0.2 | 22 | 15.4% | 22.7% |
| 0.2 to 0.3 | 22 | 24.3% | 45.5% |
| 0.3 to 0.4 | 24 | 34.9% | 45.8% |
| 0.4 to 0.5 | 48 | 45.5% | 52.1% |
| 0.5 to 0.6 | 58 | 55.3% | 65.5% |
| 0.6 to 0.7 | 58 | 65.2% | 75.9% |
| 0.7 to 0.8 | 79 | 75.0% | 79.8% |
| 0.8 to 0.9 | 99 | 85.7% | 89.9% |
| 0.9 to 1.0 | 1390 | 98.2% | 99.0% |

- The extra set's vectors (people, pets, livestock, rooms) were not published for this model when this ran, so the kind decision was tuned on wildlife photos alone and says nothing about a person or an empty room.
