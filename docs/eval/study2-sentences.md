# Sentence rows with the prior, as the page would use them

_This file is written by `tools/eval/report.py` from `docs/eval/study2-sentences.json`. Rerun the script to change it._

No head was fitted here. The models' own sentence rows were given the prior, the calibration and the page's combination with the kind phrases, with every setting chosen on the whole of `val`. These are the slots that can ship before any training photo exists.

## tinyclip-39m-16

Fitted on 0 photos of 0 species (`none (sentence rows only)`); settings chosen on 1803 tuning photos; tested on 4197 test photos (`images/alachua-2025.wasm-int8-per-channel`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 23.0% (21.8 to 24.3) | 40.2% (38.7 to 41.6) | 35.3% (33.9 to 36.8) | 55.1% (53.6 to 56.6) | 80.7% (79.5 to 81.9) | species_com; alpha 0.75; lam 2, c 1 |

| Kind of eye from | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 77.3% (76.0 to 78.7) | 0.05% | 0.10% |
| summed species probabilities of the head `sentences` | 80.7% (79.5 to 81.9) | 0.00% | 0.00% |
| the page's combination of kind phrases and the species list (rule `product`, t_kind 20, w_kind 0.5; species head `sentences`) | 83.7% (82.6 to 84.8) | 0.00% | 0.00% |

**The kind decision.** The kinds head, its temperature, its weight against the species list and the rule were chosen on 1803 wildlife tuning photos alone, because this model's vectors of the extra set (people, pets, livestock, rooms) were not published when this ran. The number tuned on is the share right on the wildlife tuning photos (the extra set's vectors were not published for this model). Each row is one kinds head under one rule at its best setting on the tuning photos. `kind_at` is the level this computation gives for an asserted kind to be right 95 times in 100 on each tuning set by itself; the level a slot ships with is set by `tools/eval/shipped.py` through `fuse.py`.

|  | Kinds head | Rule | t_kind | w_kind | Tuning number | Wildlife tuning photos | Extra tuning photos | Kind right, wildlife test | Kind right, extra test | kind_at | Asserted, wildlife test | Right when asserted | Asserted, extra test | Right when asserted |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | kind phrases | mix | 20 | 0.7 | 84.0% | 84.0% | – | 83.4% (82.2 to 84.5) | – | 0.32 | 61.3% (59.9 to 62.8) | 95.8% (95.0 to 96.5) | – | – |
|  | kind phrases | product | 20 | 0.5 | 84.4% | 84.4% | – | 83.7% (82.6 to 84.8) | – | 0.43 | 65.7% (64.3 to 67.2) | 95.6% (94.8 to 96.3) | – | – |
| **chosen** | kind phrases | product | 20 | 0.5 | 84.4% | 84.4% | – | 83.7% (82.6 to 84.8) | – | 0.43 | 65.7% (64.3 to 67.2) | 95.6% (94.8 to 96.3) | – | – |
| what the wildlife photos alone would choose | kind phrases | product | 20 | 0.5 | 84.4% | 84.4% | – | 83.7% (82.6 to 84.8) | – | 0.43 | 65.7% (64.3 to 67.2) | 95.6% (94.8 to 96.3) | – | – |

**Confidence.** For the head `sentences`, the scale was set on the tuning photos (expected calibration error 0.204 there). A species is named when its probability is at least 0.28, the lowest level from which named species were right at least nine times in ten on the tuning photos; three species are offered when the first three together reach 0.45, set the same way. On the test photos a species is then named for 17.7% (16.6 to 18.9) of photos and that name is right for 89.6% (87.5 to 91.9) of them; three species are offered for 1.7% (1.4 to 2.1) and hold the right one for 83.6% (75.3 to 91.8); 80.6% (79.4 to 81.7) get a kind of eye only. These figures leave out the page's rule that names and offers must agree with the winning kind; the exported slot is scored with that rule.

| Top probability | Tuning photos | Mean probability | Share right |
|---|---:|---:|---:|
| 0.0 to 0.1 | 1077 | 4.5% | 15.1% |
| 0.1 to 0.2 | 263 | 14.2% | 39.9% |
| 0.2 to 0.3 | 147 | 24.5% | 68.0% |
| 0.3 to 0.4 | 86 | 35.2% | 74.4% |
| 0.4 to 0.5 | 67 | 45.1% | 95.5% |
| 0.5 to 0.6 | 61 | 54.5% | 96.7% |
| 0.6 to 0.7 | 44 | 64.4% | 100.0% |
| 0.7 to 0.8 | 38 | 73.9% | 97.4% |
| 0.8 to 0.9 | 19 | 84.8% | 100.0% |
| 0.9 to 1.0 | 1 | 93.5% | 100.0% |

- The extra set's vectors (people, pets, livestock, rooms) were not published for this model when this ran, so the kind decision was tuned on wildlife photos alone and says nothing about a person or an empty room.

## tinyclip-8m-16

Fitted on 0 photos of 0 species (`none (sentence rows only)`); settings chosen on 1803 tuning photos; tested on 4197 test photos (`images/alachua-2025.wasm-int8-per-channel`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 15.1% (14.0 to 16.2) | 28.0% (26.7 to 29.3) | 26.5% (25.1 to 27.8) | 45.4% (43.9 to 46.9) | 78.2% (77.0 to 79.5) | species_com; alpha 1.00; lam 0, c 0.1 |

| Kind of eye from | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 72.4% (71.0 to 73.8) | 0.05% | 0.21% |
| summed species probabilities of the head `sentences` | 78.2% (77.0 to 79.5) | 0.00% | 0.00% |
| the page's combination of kind phrases and the species list (rule `product`, t_kind 20, w_kind 0.5; species head `sentences`) | 79.4% (78.2 to 80.6) | 0.00% | 0.00% |

**The kind decision.** The kinds head, its temperature, its weight against the species list and the rule were chosen on 1803 wildlife tuning photos alone, because this model's vectors of the extra set (people, pets, livestock, rooms) were not published when this ran. The number tuned on is the share right on the wildlife tuning photos (the extra set's vectors were not published for this model). Each row is one kinds head under one rule at its best setting on the tuning photos. `kind_at` is the level this computation gives for an asserted kind to be right 95 times in 100 on each tuning set by itself; the level a slot ships with is set by `tools/eval/shipped.py` through `fuse.py`.

|  | Kinds head | Rule | t_kind | w_kind | Tuning number | Wildlife tuning photos | Extra tuning photos | Kind right, wildlife test | Kind right, extra test | kind_at | Asserted, wildlife test | Right when asserted | Asserted, extra test | Right when asserted |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | kind phrases | mix | 50 | 0.3 | 79.5% | 79.5% | – | 79.4% (78.2 to 80.6) | – | 0.68 | 44.6% (43.0 to 46.2) | 97.4% (96.7 to 98.1) | – | – |
|  | kind phrases | product | 20 | 0.5 | 79.8% | 79.8% | – | 79.4% (78.2 to 80.6) | – | 0.53 | 41.5% (39.9 to 43.0) | 97.8% (97.1 to 98.5) | – | – |
| **chosen** | kind phrases | product | 20 | 0.5 | 79.8% | 79.8% | – | 79.4% (78.2 to 80.6) | – | 0.53 | 41.5% (39.9 to 43.0) | 97.8% (97.1 to 98.5) | – | – |
| what the wildlife photos alone would choose | kind phrases | product | 20 | 0.5 | 79.8% | 79.8% | – | 79.4% (78.2 to 80.6) | – | 0.53 | 41.5% (39.9 to 43.0) | 97.8% (97.1 to 98.5) | – | – |

**Confidence.** For the head `sentences`, the scale was set on the tuning photos (expected calibration error 0.043 there). A species is named when its probability is at least 0.57, the lowest level from which named species were right at least nine times in ten on the tuning photos; three species are offered when the first three together reach 0.64, set the same way. On the test photos a species is then named for 9.3% (8.5 to 10.2) of photos and that name is right for 88.3% (85.0 to 91.3) of them; three species are offered for 6.0% (5.3 to 6.7) and hold the right one for 83.4% (78.7 to 87.8); 84.6% (83.6 to 85.7) get a kind of eye only. These figures leave out the page's rule that names and offers must agree with the winning kind; the exported slot is scored with that rule.

| Top probability | Tuning photos | Mean probability | Share right |
|---|---:|---:|---:|
| 0.0 to 0.1 | 653 | 6.3% | 6.0% |
| 0.1 to 0.2 | 458 | 14.4% | 13.8% |
| 0.2 to 0.3 | 245 | 24.6% | 31.8% |
| 0.3 to 0.4 | 139 | 34.9% | 41.7% |
| 0.4 to 0.5 | 91 | 45.0% | 52.8% |
| 0.5 to 0.6 | 60 | 54.9% | 76.7% |
| 0.6 to 0.7 | 60 | 64.8% | 86.7% |
| 0.7 to 0.8 | 37 | 74.9% | 91.9% |
| 0.8 to 0.9 | 37 | 84.6% | 94.6% |
| 0.9 to 1.0 | 23 | 93.9% | 100.0% |

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
