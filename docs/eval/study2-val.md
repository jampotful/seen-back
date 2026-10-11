# Trained heads (Study 2): the machinery, proven on a stand-in

_This file is written by `tools/eval/report.py` from `docs/eval/study2-val.json`. Rerun the script to change it._

This run is a stand-in that proves the machinery. No training vectors were published when it ran, so two thirds of the `val` photos were used to fit the heads and the last third to choose settings. With about two fitting photos a species, these numbers say little about what the real training set (up to sixty photos a species) will give. They are here to show that every step runs and to be replaced.

## tinyclip-39m-16

Fitted on 1226 photos of 574 species (`images/alachua-2025 (two thirds of val)`); settings chosen on 565 tuning photos; tested on 4197 test photos (`images/alachua-2025.wasm-int8-per-channel`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 23.0% (21.8 to 24.3) | 40.2% (38.7 to 41.6) | 35.1% (33.7 to 36.6) | 57.1% (55.7 to 58.6) | 82.2% (81.1 to 83.3) | species_taxon_com; alpha 0.75; lam 0, c 0.1 |
| prototypes | 27.5% (26.1 to 28.9) | 43.9% (42.4 to 45.4) | 30.1% (28.7 to 31.5) | 45.7% (44.2 to 47.2) | 83.9% (82.8 to 85.0) | class means; alpha 0.38; lam 0, c 0.1 |
| prototypes + sentences | 33.1% (31.7 to 34.6) | 49.2% (47.8 to 50.8) | 36.4% (34.9 to 37.8) | 58.8% (57.2 to 60.2) | 86.5% (85.5 to 87.5) | species_taxon_com, beta 8, bias for species without photos 0.8; alpha 1.00; lam 0, c 0.1 |
| discriminant | 32.5% (31.1 to 34.0) | 45.2% (43.7 to 46.8) | 32.6% (31.2 to 34.0) | 45.4% (43.8 to 46.9) | 82.9% (81.8 to 84.1) | shrinkage 0.3; alpha 0.02; lam 0, c 0.1 |
| discriminant + sentences | 34.7% (33.3 to 36.2) | 48.8% (47.4 to 50.4) | 34.6% (33.2 to 36.1) | 52.1% (50.6 to 53.6) | 76.8% (75.5 to 78.1) | shrinkage 0.1, species_taxon_com, gamma 1; alpha 0.25; lam 0, c 0.1 |
| mapped to BioCLIP 2 | 26.5% (25.2 to 27.9) | 46.4% (44.9 to 47.9) | 35.3% (33.8 to 36.8) | 58.0% (56.5 to 59.6) | 81.2% (80.0 to 82.3) | ridge 0.01, 1226 pairs; alpha 0.94; lam 0, c 0.1 |

| Kind of eye from | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 77.3% (76.0 to 78.7) | 0.05% | 0.10% |
| trained on the fitting photos (logistic regression, 14 kinds, no row for `person` or `none`) | 84.5% (83.4 to 85.5) | 0.00% | 0.00% |
| trained rows, with the sentence rows for `person` and `none` kept beside them | 84.4% (83.2 to 85.5) | 0.10% | 0.33% |
| summed species probabilities of the head `prototypes + sentences` | 86.5% (85.5 to 87.5) | 0.00% | 0.00% |
| the page's combination of kind phrases and the species list (rule `product`, t_kind 20, w_kind 0.7; species head `prototypes + sentences`) | 87.0% (85.9 to 88.0) | 0.02% | 0.02% |

**The kind decision.** The kinds head, its temperature, its weight against the species list and the rule were chosen on 565 wildlife tuning photos alone, because this model's vectors of the extra set (people, pets, livestock, rooms) were not published when this ran. The number tuned on is the share right on the wildlife tuning photos (the extra set's vectors were not published for this model). Each row is one kinds head under one rule at its best setting on the tuning photos. `kind_at` is the level this computation gives for an asserted kind to be right 95 times in 100 on each tuning set by itself; the level a slot ships with is set by `tools/eval/shipped.py` through `fuse.py`.

|  | Kinds head | Rule | t_kind | w_kind | Tuning number | Wildlife tuning photos | Extra tuning photos | Kind right, wildlife test | Kind right, extra test | kind_at | Asserted, wildlife test | Right when asserted | Asserted, extra test | Right when asserted |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | kind phrases | mix | 50 | 0.5 | 87.1% | 87.1% | – | 87.0% (86.0 to 88.0) | – | 0.60 | 74.6% (73.2 to 75.9) | 96.1% (95.4 to 96.8) | – | – |
|  | kind phrases | product | 20 | 0.7 | 87.4% | 87.4% | – | 87.0% (85.9 to 88.0) | – | 0.46 | 77.7% (76.4 to 79.0) | 95.4% (94.7 to 96.2) | – | – |
| **chosen** | kind phrases | product | 20 | 0.7 | 87.4% | 87.4% | – | 87.0% (85.9 to 88.0) | – | 0.46 | 77.7% (76.4 to 79.0) | 95.4% (94.7 to 96.2) | – | – |
| what the wildlife photos alone would choose | kind phrases | product | 20 | 0.7 | 87.4% | 87.4% | – | 87.0% (85.9 to 88.0) | – | 0.46 | 77.7% (76.4 to 79.0) | 95.4% (94.7 to 96.2) | – | – |

Top-1 with the prior for each head, by how many fitting photos the species has:

| Fitting photos of the species | Test photos | sentences | prototypes | prototypes + sentences | discriminant | discriminant + sentences | mapped to BioCLIP 2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| no training photo | 1326 | 12.3% | 0.0% | 12.6% | 0.0% | 0.0% | 9.6% |
| 1 or 2 | 1072 | 27.0% | 21.5% | 26.1% | 19.6% | 27.1% | 24.3% |
| 3 to 9 | 1253 | 49.5% | 49.2% | 53.5% | 56.5% | 58.1% | 51.9% |
| 10 to 29 | 312 | 76.0% | 69.9% | 76.0% | 76.9% | 79.2% | 73.1% |
| 30 or more | 234 | 70.9% | 84.2% | 73.1% | 89.3% | 80.3% | 91.5% |

**Confidence.** For the head `prototypes + sentences`, the scale was set on the tuning photos (expected calibration error 0.106 there). A species is named when its probability is at least 0.90, the lowest level from which named species were right at least nine times in ten on the tuning photos; three species are offered when the first three together reach 0.94, set the same way. On the test photos a species is then named for 14.3% (13.3 to 15.4) of photos and that name is right for 91.9% (89.7 to 93.8) of them; three species are offered for 9.0% (8.2 to 9.9) and hold the right one for 90.2% (87.3 to 93.1); 76.6% (75.3 to 77.9) get a kind of eye only. These figures leave out the page's rule that names and offers must agree with the winning kind; the exported slot is scored with that rule.

| Top probability | Tuning photos | Mean probability | Share right |
|---|---:|---:|---:|
| 0.0 to 0.1 | 45 | 7.4% | 2.2% |
| 0.1 to 0.2 | 85 | 14.6% | 1.2% |
| 0.2 to 0.3 | 85 | 25.2% | 17.6% |
| 0.3 to 0.4 | 56 | 35.0% | 30.4% |
| 0.4 to 0.5 | 63 | 44.7% | 34.9% |
| 0.5 to 0.6 | 47 | 55.1% | 38.3% |
| 0.6 to 0.7 | 37 | 64.1% | 40.5% |
| 0.7 to 0.8 | 31 | 75.5% | 58.1% |
| 0.8 to 0.9 | 42 | 85.0% | 73.8% |
| 0.9 to 1.0 | 74 | 96.2% | 90.5% |

- The map into BioCLIP 2's space was fitted on 1226 pairs of vectors of the same photos.
- The extra set's vectors were not published for this model when this ran, so no kind row could be fitted for `person` or `none`. The sentence rows for the two are kept beside the trained rows, with a bias set on the tuning photos so that at most 0.5% of them are called `person` or `none`. How often a person is then called a person is unmeasured.
- The extra set's vectors (people, pets, livestock, rooms) were not published for this model when this ran, so the kind decision was tuned on wildlife photos alone and says nothing about a person or an empty room.

## tinyclip-8m-16

Fitted on 1226 photos of 574 species (`images/alachua-2025 (two thirds of val)`); settings chosen on 565 tuning photos; tested on 4197 test photos (`images/alachua-2025.wasm-int8-per-channel`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 15.1% (14.0 to 16.2) | 28.0% (26.7 to 29.3) | 25.9% (24.6 to 27.2) | 44.0% (42.5 to 45.5) | 76.6% (75.3 to 77.9) | species_com; alpha 0.62; lam 0, c 0.1 |
| prototypes | 21.3% (20.1 to 22.5) | 36.5% (35.1 to 38.0) | 24.0% (22.7 to 25.3) | 38.8% (37.4 to 40.3) | 77.6% (76.4 to 78.8) | class means; alpha 0.50; lam 2, c 1 |
| prototypes + sentences | 24.4% (23.2 to 25.8) | 41.8% (40.3 to 43.2) | 27.3% (25.9 to 28.6) | 44.9% (43.4 to 46.4) | 72.9% (71.5 to 74.3) | species_com, beta 8, bias for species without photos 0.8; alpha 0.50; lam 0, c 0.1 |
| discriminant | 24.6% (23.3 to 25.9) | 38.1% (36.6 to 39.6) | 24.9% (23.6 to 26.3) | 38.3% (36.8 to 39.8) | 76.7% (75.4 to 77.9) | shrinkage 0.3; alpha 0.25; lam 2, c 1 |
| discriminant + sentences | 27.1% (25.8 to 28.5) | 41.7% (40.2 to 43.2) | 25.3% (24.0 to 26.6) | 45.5% (43.9 to 47.0) | 73.7% (72.4 to 75.0) | shrinkage 0.03, species_com, gamma 1; alpha 0.50; lam 0, c 0.1 |
| mapped to BioCLIP 2 | 16.5% (15.5 to 17.7) | 32.4% (31.1 to 33.9) | 24.3% (23.0 to 25.6) | 45.3% (43.8 to 46.9) | 71.6% (70.2 to 72.9) | ridge 0.01, 1226 pairs; alpha 0.75; lam 0, c 0.1 |

| Kind of eye from | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 72.4% (71.0 to 73.8) | 0.05% | 0.21% |
| trained on the fitting photos (logistic regression, 14 kinds, no row for `person` or `none`) | 77.0% (75.7 to 78.3) | 0.00% | 0.00% |
| trained rows, with the sentence rows for `person` and `none` kept beside them | 76.7% (75.4 to 77.9) | 0.26% | 0.86% |
| summed species probabilities of the head `discriminant + sentences` | 73.7% (72.4 to 75.0) | 0.00% | 0.00% |
| the page's combination of kind phrases and the species list (rule `product`, t_kind 50, w_kind 0.3; species head `discriminant + sentences`) | 77.7% (76.4 to 78.9) | 0.05% | 0.10% |

**The kind decision.** The kinds head, its temperature, its weight against the species list and the rule were chosen on 565 wildlife tuning photos alone, because this model's vectors of the extra set (people, pets, livestock, rooms) were not published when this ran. The number tuned on is the share right on the wildlife tuning photos (the extra set's vectors were not published for this model). Each row is one kinds head under one rule at its best setting on the tuning photos. `kind_at` is the level this computation gives for an asserted kind to be right 95 times in 100 on each tuning set by itself; the level a slot ships with is set by `tools/eval/shipped.py` through `fuse.py`.

|  | Kinds head | Rule | t_kind | w_kind | Tuning number | Wildlife tuning photos | Extra tuning photos | Kind right, wildlife test | Kind right, extra test | kind_at | Asserted, wildlife test | Right when asserted | Asserted, extra test | Right when asserted |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | kind phrases | mix | 50 | 0.3 | 79.8% | 79.8% | – | 77.3% (76.1 to 78.6) | – | 0.55 | 50.0% (48.5 to 51.6) | 94.6% (93.6 to 95.5) | – | – |
|  | kind phrases | product | 50 | 0.3 | 80.0% | 80.0% | – | 77.7% (76.4 to 78.9) | – | 0.58 | 52.3% (50.9 to 54.0) | 94.3% (93.4 to 95.3) | – | – |
| **chosen** | kind phrases | product | 50 | 0.3 | 80.0% | 80.0% | – | 77.7% (76.4 to 78.9) | – | 0.58 | 52.3% (50.9 to 54.0) | 94.3% (93.4 to 95.3) | – | – |
| what the wildlife photos alone would choose | kind phrases | product | 50 | 0.3 | 80.0% | 80.0% | – | 77.7% (76.4 to 78.9) | – | 0.58 | 52.3% (50.9 to 54.0) | 94.3% (93.4 to 95.3) | – | – |

Top-1 with the prior for each head, by how many fitting photos the species has:

| Fitting photos of the species | Test photos | sentences | prototypes | prototypes + sentences | discriminant | discriminant + sentences | mapped to BioCLIP 2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| no training photo | 1326 | 8.4% | 0.0% | 7.9% | 0.0% | 8.0% | 4.2% |
| 1 or 2 | 1072 | 20.2% | 13.9% | 19.3% | 10.3% | 14.3% | 14.6% |
| 3 to 9 | 1253 | 33.8% | 37.9% | 38.6% | 40.2% | 34.8% | 33.0% |
| 10 to 29 | 312 | 58.0% | 59.9% | 60.3% | 70.2% | 64.4% | 57.0% |
| 30 or more | 234 | 66.7% | 83.3% | 68.8% | 91.0% | 70.9% | 92.3% |

**Confidence.** For the head `discriminant + sentences`, no probability level made named species right nine times in ten on the tuning photos, so this head should name no species by itself.

| Top probability | Tuning photos | Mean probability | Share right |
|---|---:|---:|---:|
| 0.0 to 0.1 | 431 | 4.2% | 16.5% |
| 0.1 to 0.2 | 90 | 14.2% | 54.4% |
| 0.2 to 0.3 | 30 | 23.8% | 90.0% |
| 0.3 to 0.4 | 10 | 34.7% | 100.0% |
| 0.4 to 0.5 | 3 | 43.8% | 66.7% |
| 0.5 to 0.6 | 1 | 58.8% | 100.0% |
| 0.6 to 0.7 | 0 | – | – |
| 0.7 to 0.8 | 0 | – | – |
| 0.8 to 0.9 | 0 | – | – |
| 0.9 to 1.0 | 0 | – | – |

- The map into BioCLIP 2's space was fitted on 1226 pairs of vectors of the same photos.
- The extra set's vectors were not published for this model when this ran, so no kind row could be fitted for `person` or `none`. The sentence rows for the two are kept beside the trained rows, with a bias set on the tuning photos so that at most 0.5% of them are called `person` or `none`. How often a person is then called a person is unmeasured.
- The extra set's vectors (people, pets, livestock, rooms) were not published for this model when this ran, so the kind decision was tuned on wildlife photos alone and says nothing about a person or an empty room.

## bioclip2-l14

Fitted on 1226 photos of 574 species (`images/alachua-2025 (two thirds of val)`); settings chosen on 565 tuning photos; tested on 4197 test photos (`images/alachua-2025`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 90.3% (89.4 to 91.3) | 96.8% (96.2 to 97.3) | 92.4% (91.6 to 93.2) | 97.5% (97.0 to 97.9) | 98.3% (97.9 to 98.7) | species_sci; alpha 1.00; lam 2, c 1 |
| prototypes | 61.0% (59.5 to 62.5) | 65.5% (64.1 to 67.0) | 61.1% (59.6 to 62.6) | 65.5% (64.0 to 66.9) | 93.2% (92.4 to 94.0) | class means; alpha 0.40; lam 0, c 0.1 |
| prototypes + sentences | 91.3% (90.5 to 92.2) | 97.3% (96.8 to 97.8) | 91.7% (90.9 to 92.6) | 97.6% (97.1 to 98.0) | 98.5% (98.0 to 98.8) | species_sci, beta 8, bias for species without photos 0.65; alpha 0.60; lam 0, c 0.1 |
| discriminant | 60.1% (58.7 to 61.6) | 64.4% (62.9 to 65.8) | 60.7% (59.2 to 62.2) | 65.3% (63.9 to 66.8) | 91.6% (90.8 to 92.5) | shrinkage 1; alpha 0.45; lam 0, c 0.1 |
| discriminant + sentences | 91.0% (90.1 to 91.8) | 97.2% (96.7 to 97.7) | 90.8% (90.0 to 91.7) | 97.5% (97.0 to 98.0) | 98.4% (98.0 to 98.8) | shrinkage 1, species_sci, gamma 3; alpha 0.90; lam 2, c 1 |

| Kind of eye from | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 76.1% (74.8 to 77.4) | 0.00% | 0.00% |
| trained on the fitting photos (logistic regression, 14 kinds, no row for `person` or `none`) | 94.4% (93.7 to 95.0) | 0.00% | 0.00% |
| trained rows, with the sentence rows for `person` and `none` kept beside them | 94.0% (93.3 to 94.7) | 0.02% | 0.86% |
| summed species probabilities of the head `prototypes + sentences` | 98.5% (98.0 to 98.8) | 0.00% | 0.00% |
| the page's combination of kind phrases and the species list (rule `product`, t_kind 20, w_kind 0.5; species head `prototypes + sentences`) | 98.6% (98.2 to 98.9) | 0.00% | 0.00% |

**The kind decision.** The kinds head, its temperature, its weight against the species list and the rule were chosen on 565 wildlife tuning photos alone, because this model's vectors of the extra set (people, pets, livestock, rooms) were not published when this ran. The number tuned on is the share right on the wildlife tuning photos (the extra set's vectors were not published for this model). Each row is one kinds head under one rule at its best setting on the tuning photos. `kind_at` is the level this computation gives for an asserted kind to be right 95 times in 100 on each tuning set by itself; the level a slot ships with is set by `tools/eval/shipped.py` through `fuse.py`.

|  | Kinds head | Rule | t_kind | w_kind | Tuning number | Wildlife tuning photos | Extra tuning photos | Kind right, wildlife test | Kind right, extra test | kind_at | Asserted, wildlife test | Right when asserted | Asserted, extra test | Right when asserted |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | kind phrases | mix | 20 | 0.5 | 98.2% | 98.2% | – | 98.5% (98.1 to 98.9) | – | 0.20 | 100.0% (99.9 to 100.0) | 98.5% (98.1 to 98.9) | – | – |
|  | kind phrases | product | 20 | 0.5 | 98.4% | 98.4% | – | 98.6% (98.2 to 98.9) | – | 0.20 | 100.0% (99.9 to 100.0) | 98.6% (98.2 to 99.0) | – | – |
| **chosen** | kind phrases | product | 20 | 0.5 | 98.4% | 98.4% | – | 98.6% (98.2 to 98.9) | – | 0.20 | 100.0% (99.9 to 100.0) | 98.6% (98.2 to 99.0) | – | – |
| what the wildlife photos alone would choose | kind phrases | product | 20 | 0.5 | 98.4% | 98.4% | – | 98.6% (98.2 to 98.9) | – | 0.20 | 100.0% (99.9 to 100.0) | 98.6% (98.2 to 99.0) | – | – |

Top-1 with the prior for each head, by how many fitting photos the species has:

| Fitting photos of the species | Test photos | sentences | prototypes | prototypes + sentences | discriminant | discriminant + sentences |
|---|---:|---:|---:|---:|---:|---:|
| no training photo | 1326 | 87.1% | 0.0% | 83.7% | 0.0% | 80.7% |
| 1 or 2 | 1072 | 93.8% | 78.3% | 94.4% | 76.9% | 93.0% |
| 3 to 9 | 1253 | 94.6% | 95.0% | 95.6% | 94.9% | 96.7% |
| 10 to 29 | 312 | 98.4% | 99.0% | 98.1% | 98.7% | 98.7% |
| 30 or more | 234 | 96.6% | 96.2% | 95.7% | 96.2% | 97.0% |

**Confidence.** For the head `prototypes + sentences`, the scale was set on the tuning photos (expected calibration error 0.022 there). A species is named when its probability is at least 0.05, the lowest level from which named species were right at least nine times in ten on the tuning photos; no level for offers reached nine in ten. On the test photos a species is then named for 100.0% (100.0 to 100.0) of photos and that name is right for 91.7% (90.9 to 92.6) of them; three species are offered for 0.0% (0.0 to 0.0) and hold the right one for –; 0.0% (0.0 to 0.0) get a kind of eye only. These figures leave out the page's rule that names and offers must agree with the winning kind; the exported slot is scored with that rule.

| Top probability | Tuning photos | Mean probability | Share right |
|---|---:|---:|---:|
| 0.0 to 0.1 | 0 | – | – |
| 0.1 to 0.2 | 4 | 16.2% | 0.0% |
| 0.2 to 0.3 | 3 | 23.3% | 33.3% |
| 0.3 to 0.4 | 3 | 33.1% | 33.3% |
| 0.4 to 0.5 | 13 | 43.6% | 53.8% |
| 0.5 to 0.6 | 13 | 55.4% | 61.5% |
| 0.6 to 0.7 | 10 | 65.3% | 90.0% |
| 0.7 to 0.8 | 20 | 77.0% | 75.0% |
| 0.8 to 0.9 | 38 | 85.3% | 79.0% |
| 0.9 to 1.0 | 461 | 99.1% | 98.3% |

- The extra set's vectors were not published for this model when this ran, so no kind row could be fitted for `person` or `none`. The sentence rows for the two are kept beside the trained rows, with a bias set on the tuning photos so that at most 0.5% of them are called `person` or `none`. How often a person is then called a person is unmeasured.
- The extra set's vectors (people, pets, livestock, rooms) were not published for this model when this ran, so the kind decision was tuned on wildlife photos alone and says nothing about a person or an empty room.
