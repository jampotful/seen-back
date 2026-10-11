# Trained heads (Study 2): the machinery, proven on a stand-in

_This file is written by `tools/eval/report.py` from `docs/eval/study2-val.json`. Rerun the script to change it._

This run is a stand-in that proves the machinery. No training vectors were published when it ran, so two thirds of the `val` photos were used to fit the heads and the last third to choose settings. With about two fitting photos a species, these numbers say little about what the real training set (up to sixty photos a species) will give. They are here to show that every step runs and to be replaced.

## tinyclip-39m-16

Fitted on 1226 photos of 574 species (`images/alachua-2025 (two thirds of val)`); settings chosen on 565 tuning photos; tested on 4197 test photos (`images/alachua-2025.wasm-int8-per-channel`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 22.9% (21.7 to 24.1) | 40.1% (38.7 to 41.6) | 34.6% (33.2 to 36.0) | 54.1% (52.6 to 55.6) | 85.9% (84.9 to 87.0) | species_com; alpha 1.25; lam 0, c 0.1 |
| prototypes | 27.5% (26.1 to 28.9) | 43.9% (42.4 to 45.4) | 30.1% (28.7 to 31.5) | 45.7% (44.2 to 47.2) | 83.9% (82.8 to 85.0) | class means; alpha 0.38; lam 0, c 0.1 |
| prototypes + sentences | 32.5% (31.1 to 34.0) | 49.9% (48.5 to 51.4) | 36.9% (35.5 to 38.4) | 55.8% (54.3 to 57.3) | 86.5% (85.5 to 87.5) | species_com, beta 8, bias for species without photos 0.65; alpha 0.75; lam 0, c 0.1 |
| discriminant | 32.5% (31.1 to 34.0) | 45.2% (43.7 to 46.8) | 32.6% (31.2 to 34.0) | 45.4% (43.8 to 46.9) | 82.9% (81.8 to 84.1) | shrinkage 0.3; alpha 0.02; lam 0, c 0.1 |
| discriminant + sentences | 33.5% (32.0 to 34.9) | 46.3% (44.8 to 47.9) | 34.6% (33.2 to 36.1) | 49.3% (47.8 to 50.9) | 74.8% (73.5 to 76.2) | shrinkage 0.1, species_com, gamma 1; alpha 0.31; lam 0, c 0.1 |
| mapped to BioCLIP 2 | 26.5% (25.2 to 27.9) | 46.4% (44.9 to 47.9) | 35.3% (33.8 to 36.8) | 58.0% (56.5 to 59.6) | 81.2% (80.0 to 82.3) | ridge 0.01, 1226 pairs; alpha 0.94; lam 0, c 0.1 |

| Kind of eye from | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 77.3% (76.0 to 78.7) | 0.05% | 0.10% |
| trained on the fitting photos (logistic regression, 14 kinds, no row for `person` or `none`) | 84.5% (83.4 to 85.5) | 0.00% | 0.00% |
| trained rows, with the sentence rows for `person` and `none` kept beside them | 84.4% (83.2 to 85.5) | 0.10% | 0.33% |
| summed species probabilities of the head `prototypes + sentences` | 86.5% (85.5 to 87.5) | 0.00% | 0.00% |
| the page's combination of kind phrases and species list (rule `mix`, t_kind 20, w_kind 0.7; species head `prototypes + sentences`) | 86.7% (85.7 to 87.7) | 0.00% | 0.00% |
| the page's combination of kind phrases and species list (rule `product`, t_kind 100, w_kind 0.2; species head `prototypes + sentences`) | 86.6% (85.6 to 87.7) | 0.05% | 0.02% |

Top-1 with the prior for each head, by how many fitting photos the species has:

| Fitting photos of the species | Test photos | sentences | prototypes | prototypes + sentences | discriminant | discriminant + sentences | mapped to BioCLIP 2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| no training photo | 1326 | 12.6% | 0.0% | 7.7% | 0.0% | 0.0% | 9.6% |
| 1 or 2 | 1072 | 26.7% | 21.5% | 30.5% | 19.6% | 27.2% | 24.3% |
| 3 to 9 | 1253 | 46.4% | 49.2% | 54.3% | 56.5% | 56.6% | 51.9% |
| 10 to 29 | 312 | 77.2% | 69.9% | 78.5% | 76.9% | 80.5% | 73.1% |
| 30 or more | 234 | 75.2% | 84.2% | 83.8% | 89.3% | 85.9% | 91.5% |

**Confidence.** For the head `prototypes + sentences`, the scale was set on the tuning photos (expected calibration error 0.046 there). A species is named when its probability is at least 0.63, the lowest level from which named species were right at least nine times in ten on the tuning photos; no level for offers reached nine in ten. On the test photos a species is then named for 19.5% (18.2 to 20.7) of photos and that name is right for 88.6% (86.4 to 90.8) of them; three species are offered for 0.0% (0.0 to 0.0) and hold the right one for –; 80.5% (79.3 to 81.8) get a kind of eye only. These figures leave out the page's rule that names and offers must agree with the winning kind; the exported slot is scored with that rule.

| Top probability | Tuning photos | Mean probability | Share right |
|---|---:|---:|---:|
| 0.0 to 0.1 | 101 | 6.4% | 9.9% |
| 0.1 to 0.2 | 143 | 14.3% | 17.5% |
| 0.2 to 0.3 | 87 | 25.1% | 29.9% |
| 0.3 to 0.4 | 51 | 35.0% | 33.3% |
| 0.4 to 0.5 | 39 | 44.9% | 41.0% |
| 0.5 to 0.6 | 27 | 54.1% | 63.0% |
| 0.6 to 0.7 | 26 | 64.7% | 57.7% |
| 0.7 to 0.8 | 25 | 74.7% | 92.0% |
| 0.8 to 0.9 | 27 | 85.3% | 92.6% |
| 0.9 to 1.0 | 39 | 94.6% | 97.4% |

- The map into BioCLIP 2's space was fitted on 1226 pairs of vectors of the same photos.
- The wildlife records hold no people and no photos with nothing alive in them. The sentence rows for `person` and `none` are kept, with a bias set on the tuning photos so that at most 0.5% of them are called `person` or `none`. How often a person is then called a person is unmeasured.

## tinyclip-8m-16

Fitted on 1226 photos of 574 species (`images/alachua-2025 (two thirds of val)`); settings chosen on 565 tuning photos; tested on 4197 test photos (`images/alachua-2025.wasm-int8-per-channel`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 14.6% (13.5 to 15.7) | 27.6% (26.3 to 28.9) | 25.8% (24.5 to 27.1) | 44.6% (43.1 to 46.1) | 78.1% (76.8 to 79.3) | species_com; alpha 1.25; lam 0, c 0.1 |
| prototypes | 21.3% (20.1 to 22.5) | 36.5% (35.1 to 38.0) | 24.0% (22.7 to 25.3) | 38.8% (37.4 to 40.3) | 77.6% (76.4 to 78.8) | class means; alpha 0.50; lam 2, c 1 |
| prototypes + sentences | 24.3% (23.0 to 25.6) | 41.3% (39.9 to 42.7) | 26.9% (25.6 to 28.3) | 44.4% (42.8 to 46.0) | 78.2% (76.9 to 79.4) | species_com, beta 2, bias for species without photos 0.8; alpha 0.62; lam 0, c 0.1 |
| discriminant | 24.6% (23.3 to 25.9) | 38.1% (36.6 to 39.6) | 24.9% (23.6 to 26.3) | 38.3% (36.8 to 39.8) | 76.7% (75.4 to 77.9) | shrinkage 0.3; alpha 0.25; lam 2, c 1 |
| discriminant + sentences | 26.5% (25.2 to 27.9) | 41.2% (39.7 to 42.7) | 25.6% (24.3 to 26.9) | 43.8% (42.3 to 45.3) | 74.7% (73.5 to 76.1) | shrinkage 0.03, species_com, gamma 3; alpha 0.50; lam 0, c 0.1 |
| mapped to BioCLIP 2 | 16.5% (15.5 to 17.7) | 32.4% (31.1 to 33.9) | 24.3% (23.0 to 25.6) | 45.3% (43.8 to 46.9) | 71.6% (70.2 to 72.9) | ridge 0.01, 1226 pairs; alpha 0.75; lam 0, c 0.1 |

| Kind of eye from | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 72.4% (71.0 to 73.8) | 0.05% | 0.21% |
| trained on the fitting photos (logistic regression, 14 kinds, no row for `person` or `none`) | 77.0% (75.7 to 78.3) | 0.00% | 0.00% |
| trained rows, with the sentence rows for `person` and `none` kept beside them | 76.7% (75.4 to 77.9) | 0.26% | 0.86% |
| summed species probabilities of the head `discriminant + sentences` | 74.7% (73.5 to 76.1) | 0.00% | 0.00% |
| the page's combination of kind phrases and species list (rule `mix`, t_kind 50, w_kind 0.3; species head `discriminant + sentences`) | 77.5% (76.2 to 78.8) | 0.02% | 0.10% |
| the page's combination of kind phrases and species list (rule `product`, t_kind 50, w_kind 0.3; species head `discriminant + sentences`) | 78.1% (76.8 to 79.3) | 0.02% | 0.10% |

Top-1 with the prior for each head, by how many fitting photos the species has:

| Fitting photos of the species | Test photos | sentences | prototypes | prototypes + sentences | discriminant | discriminant + sentences | mapped to BioCLIP 2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| no training photo | 1326 | 6.7% | 0.0% | 5.3% | 0.0% | 8.4% | 4.2% |
| 1 or 2 | 1072 | 16.1% | 13.9% | 17.6% | 10.3% | 16.9% | 14.6% |
| 3 to 9 | 1253 | 34.8% | 37.9% | 39.9% | 40.2% | 34.8% | 33.0% |
| 10 to 29 | 312 | 66.7% | 59.9% | 61.9% | 70.2% | 60.3% | 57.0% |
| 30 or more | 234 | 74.8% | 83.3% | 76.1% | 91.0% | 68.0% | 92.3% |

**Confidence.** For the head `discriminant + sentences`, the scale was set on the tuning photos (expected calibration error 0.174 there). A species is named when its probability is at least 0.31, the lowest level from which named species were right at least nine times in ten on the tuning photos; three species are offered when the first three together reach 0.34, set the same way. On the test photos a species is then named for 8.3% (7.4 to 9.1) of photos and that name is right for 89.7% (86.5 to 92.8) of them; three species are offered for 7.4% (6.7 to 8.2) and hold the right one for 80.8% (76.6 to 84.9); 84.3% (83.2 to 85.4) get a kind of eye only. These figures leave out the page's rule that names and offers must agree with the winning kind; the exported slot is scored with that rule.

| Top probability | Tuning photos | Mean probability | Share right |
|---|---:|---:|---:|
| 0.0 to 0.1 | 398 | 4.4% | 12.6% |
| 0.1 to 0.2 | 88 | 14.1% | 46.6% |
| 0.2 to 0.3 | 36 | 24.6% | 69.4% |
| 0.3 to 0.4 | 26 | 34.0% | 88.5% |
| 0.4 to 0.5 | 12 | 44.3% | 83.3% |
| 0.5 to 0.6 | 3 | 56.1% | 100.0% |
| 0.6 to 0.7 | 1 | 61.9% | 100.0% |
| 0.7 to 0.8 | 1 | 71.2% | 100.0% |
| 0.8 to 0.9 | 0 | – | – |
| 0.9 to 1.0 | 0 | – | – |

- The map into BioCLIP 2's space was fitted on 1226 pairs of vectors of the same photos.
- The wildlife records hold no people and no photos with nothing alive in them. The sentence rows for `person` and `none` are kept, with a bias set on the tuning photos so that at most 0.5% of them are called `person` or `none`. How often a person is then called a person is unmeasured.

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
| the page's combination of kind phrases and species list (rule `mix`, t_kind 20, w_kind 0.5; species head `prototypes + sentences`) | 98.5% (98.1 to 98.9) | 0.00% | 0.00% |
| the page's combination of kind phrases and species list (rule `product`, t_kind 20, w_kind 0.5; species head `prototypes + sentences`) | 98.6% (98.2 to 98.9) | 0.00% | 0.00% |

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

- The wildlife records hold no people and no photos with nothing alive in them. The sentence rows for `person` and `none` are kept, with a bias set on the tuning photos so that at most 0.5% of them are called `person` or `none`. How often a person is then called a person is unmeasured.
