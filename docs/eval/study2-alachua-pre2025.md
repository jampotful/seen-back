# Heads trained on local photos (Study 2)

_This file is written by `tools/eval/report.py` from `docs/eval/study2-alachua-pre2025.json`. Rerun the script to change it._

Heads were fitted on the training photos `alachua-pre2025` (from before 2025, up to sixty a species), settings were chosen on `val`, and every number is from `test`.

## tinyclip-39m-16

Fitted on 84808 photos of 5467 species (`images/alachua-pre2025`); settings chosen on 1803 tuning photos; tested on 4197 test photos (`images/alachua-2025.wasm-int8-per-channel`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 23.0% (21.8 to 24.3) | 40.2% (38.7 to 41.6) | 35.3% (33.9 to 36.8) | 55.1% (53.6 to 56.6) | 80.7% (79.5 to 81.9) | species_com; alpha 0.75; lam 2, c 1 |
| prototypes | 36.9% (35.4 to 38.3) | 62.8% (61.3 to 64.3) | 47.3% (45.8 to 48.9) | 71.7% (70.3 to 73.1) | 87.9% (87.0 to 88.9) | class means; alpha 0.75; lam 0, c 0.1 |
| prototypes + sentences | 38.4% (37.0 to 39.9) | 63.9% (62.4 to 65.3) | 48.4% (46.9 to 50.0) | 72.4% (71.0 to 73.8) | 88.2% (87.2 to 89.2) | species_com, beta 0.1, bias for species without photos 0.2; alpha 0.62; lam 0, c 0.1 |
| discriminant | 47.6% (46.1 to 49.1) | 71.1% (69.7 to 72.5) | 53.7% (52.2 to 55.3) | 75.3% (74.0 to 76.6) | 88.2% (87.2 to 89.2) | shrinkage 0.03; alpha 0.60; lam 0, c 0.1 |
| discriminant + sentences | 47.6% (46.1 to 49.1) | 70.8% (69.3 to 72.1) | 54.1% (52.6 to 55.7) | 75.8% (74.5 to 77.2) | 88.8% (87.8 to 89.8) | shrinkage 0.3, species_com, gamma 0.03; alpha 0.56; lam 0, c 0.1 |

| Kind of eye from | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 77.3% (76.0 to 78.7) | 0.05% | 0.10% |
| trained on the fitting photos (logistic regression, 15 kinds, no row for `person` or `none`) | 86.6% (85.6 to 87.6) | 0.00% | 0.00% |
| summed species probabilities of the head `discriminant` | 88.2% (87.2 to 89.2) | 0.00% | 0.00% |
| the page's combination of kind rows fitted on the fitting photos and the extra set (every photo counts the same) and the species list (rule `mix`, t_kind 0.5, w_kind 0.7; species head `discriminant`) | 88.4% (87.4 to 89.4) | 0.00% | 0.02% |

**The kind decision.** The kinds head, its temperature, its weight against the species list and the rule were chosen on 1803 wildlife tuning photos and 3056 tuning photos of the extra set `coco-kinds` (`images/coco-kinds`). Another 5944 of its photos were there for fitting kind rows, and its 1240 test photos (`images/coco-kinds.wasm-int8-per-channel`) are only reported. The number tuned on is the mean of the share right on the wildlife tuning photos and of the mean share right over the extra set's kinds. Each row is one kinds head under one rule at its best setting on the tuning photos. `kind_at` is the level this computation gives for an asserted kind to be right 95 times in 100 on each tuning set by itself; the level a slot ships with is set by `tools/eval/shipped.py` through `fuse.py`.

|  | Kinds head | Rule | t_kind | w_kind | Tuning number | Wildlife tuning photos | Extra tuning photos | Kind right, wildlife test | Kind right, extra test | kind_at | Asserted, wildlife test | Right when asserted | Asserted, extra test | Right when asserted |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | kind phrases | mix | 100 | 0.7 | 84.2% | 81.9% | 86.4% | 81.9% (80.7 to 83.1) | 79.5% (77.2 to 81.6) | 0.76 | 65.0% (63.5 to 66.5) | 96.6% (95.9 to 97.2) | 44.4% (41.5 to 47.0) | 96.5% (94.7 to 98.0) |
|  | kind phrases | product | 100 | 0.9 | 84.0% | 80.9% | 87.1% | 80.8% (79.5 to 82.0) | 82.6% (80.4 to 84.5) | 0.96 | 37.4% (35.9 to 39.0) | 96.4% (95.4 to 97.3) | 27.0% (24.5 to 29.4) | 97.6% (95.8 to 99.1) |
|  | kind rows fitted on the fitting photos and the extra set (every photo counts the same) | mix | 0.5 | 0.7 | 92.5% | 88.5% | 96.5% | 88.4% (87.4 to 89.4) | 97.4% (96.5 to 98.2) | 0.51 | 84.7% (83.6 to 85.8) | 95.0% (94.2 to 95.7) | 95.5% (94.2 to 96.7) | 98.9% (98.3 to 99.5) |
|  | kind rows fitted on the fitting photos and the extra set (every photo counts the same) | product | 1 | 0.9 | 91.7% | 86.9% | 96.5% | 87.5% (86.5 to 88.5) | 97.4% (96.5 to 98.3) | 0.76 | 80.0% (78.9 to 81.2) | 95.2% (94.4 to 95.9) | 97.0% (96.0 to 98.0) | 98.7% (98.0 to 99.2) |
|  | kind rows fitted on the fitting photos and the extra set (a kind's photos weighted by the inverse square root of their number) | mix | 0.5 | 0.7 | 92.4% | 88.5% | 96.4% | 88.8% (87.9 to 89.8) | 97.4% (96.5 to 98.2) | 0.51 | 83.1% (82.0 to 84.3) | 95.8% (95.2 to 96.5) | 96.1% (95.0 to 97.2) | 98.7% (98.0 to 99.2) |
|  | kind rows fitted on the fitting photos and the extra set (a kind's photos weighted by the inverse square root of their number) | product | 1 | 0.9 | 91.5% | 86.5% | 96.5% | 87.0% (86.0 to 88.0) | 97.8% (97.0 to 98.6) | 0.76 | 78.7% (77.5 to 79.9) | 95.5% (94.7 to 96.2) | 97.2% (96.2 to 98.1) | 98.8% (98.1 to 99.3) |
|  | kind rows fitted on the fitting photos and the extra set (every kind counts the same) | mix | 0.5 | 0.7 | 91.9% | 87.5% | 96.3% | 88.4% (87.4 to 89.3) | 97.7% (96.9 to 98.6) | 0.52 | 78.8% (77.5 to 80.0) | 95.9% (95.2 to 96.5) | 96.9% (95.8 to 97.8) | 98.6% (97.9 to 99.2) |
|  | kind rows fitted on the fitting photos and the extra set (every kind counts the same) | product | 2 | 0.7 | 90.2% | 84.6% | 95.9% | 85.9% (84.9 to 86.9) | 97.7% (96.9 to 98.6) | 0.94 | 74.3% (72.9 to 75.6) | 95.8% (95.0 to 96.5) | 97.1% (96.0 to 98.0) | 98.7% (98.0 to 99.3) |
| **chosen** | kind rows fitted on the fitting photos and the extra set (every photo counts the same) | mix | 0.5 | 0.7 | 92.5% | 88.5% | 96.5% | 88.4% (87.4 to 89.4) | 97.4% (96.5 to 98.2) | 0.51 | 84.7% (83.6 to 85.8) | 95.0% (94.2 to 95.7) | 95.5% (94.2 to 96.7) | 98.9% (98.3 to 99.5) |
| what the wildlife photos alone would choose | kind rows fitted on the fitting photos and the extra set (every photo counts the same) | mix | 0.5 | 0.5 | 83.0% | 89.0% | 77.0% | 88.8% (87.8 to 89.7) | 91.8% (90.2 to 93.3) | 0.57 | 84.9% (83.9 to 85.9) | 95.8% (95.2 to 96.5) | 87.5% (85.7 to 89.3) | 98.8% (98.2 to 99.4) |

The chosen setting on the extra set's test photos, by kind (no species is named in this computation):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 99.2% (98.2 to 100.0) | 97.5% | 99.7% | 100.0% | 99.2% | 0.5% | – | none (2) |
| none | 500 | 97.8% (96.4 to 99.0) | 95.4% | 99.4% | 91.3% | 0.4% | 97.8% | – | cat (3) |
| cat | 77 | 90.9% (84.4 to 97.4) | 90.9% | 97.1% | 85.7% | 1.3% | 3.9% | – | none (3) |
| dog | 63 | 90.5% (82.5 to 96.8) | 88.9% | 92.9% | 100.0% | 0.0% | 0.0% | – | cat (6) |
| deer | 200 | 97.5% (95.0 to 99.5) | 95.5% | 98.4% | 100.0% | 1.0% | 0.5% | – | person (2) |

Top-1 with the prior for each head, by how many fitting photos the species has:

| Fitting photos of the species | Test photos | sentences | prototypes | prototypes + sentences | discriminant | discriminant + sentences |
|---|---:|---:|---:|---:|---:|---:|
| no training photo | 45 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| 1 or 2 | 56 | 0.0% | 1.8% | 1.8% | 0.0% | 0.0% |
| 3 to 9 | 136 | 0.0% | 10.3% | 9.6% | 12.5% | 12.5% |
| 10 to 29 | 289 | 1.7% | 19.7% | 20.8% | 31.1% | 26.6% |
| 30 or more | 3671 | 40.3% | 52.1% | 53.4% | 58.5% | 59.3% |

**Confidence.** For the head `discriminant`, the scale was set on the tuning photos (expected calibration error 0.084 there). A species is named when its probability is at least 0.81, the lowest level from which named species were right at least nine times in ten on the tuning photos; three species are offered when the first three together reach 0.96, set the same way. On the test photos a species is then named for 25.8% (24.6 to 27.2) of photos and that name is right for 88.3% (86.4 to 90.2) of them; three species are offered for 4.7% (4.1 to 5.3) and hold the right one for 90.3% (86.2 to 94.4); 69.5% (68.1 to 70.9) get a kind of eye only. These figures leave out the page's rule that names and offers must agree with the winning kind; the exported slot is scored with that rule.

| Top probability | Tuning photos | Mean probability | Share right |
|---|---:|---:|---:|
| 0.0 to 0.1 | 194 | 6.7% | 10.3% |
| 0.1 to 0.2 | 237 | 14.8% | 30.0% |
| 0.2 to 0.3 | 189 | 25.1% | 40.7% |
| 0.3 to 0.4 | 156 | 35.3% | 45.5% |
| 0.4 to 0.5 | 161 | 44.9% | 50.9% |
| 0.5 to 0.6 | 133 | 54.7% | 66.2% |
| 0.6 to 0.7 | 129 | 65.0% | 70.5% |
| 0.7 to 0.8 | 105 | 75.3% | 82.9% |
| 0.8 to 0.9 | 123 | 84.9% | 78.0% |
| 0.9 to 1.0 | 376 | 97.3% | 93.3% |

- The map into BioCLIP 2's space could not be fitted: BioCLIP 2's vectors of the fitting photos are not published yet.

## tinyclip-8m-16

Fitted on 84808 photos of 5467 species (`images/alachua-pre2025`); settings chosen on 1803 tuning photos; tested on 4197 test photos (`images/alachua-2025.wasm-int8-per-channel`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 15.1% (14.0 to 16.2) | 28.0% (26.7 to 29.3) | 26.5% (25.1 to 27.8) | 45.4% (43.9 to 46.9) | 78.2% (77.0 to 79.5) | species_com; alpha 1.00; lam 0, c 0.1 |
| prototypes | 26.3% (25.0 to 27.6) | 49.6% (48.1 to 51.0) | 37.5% (36.0 to 38.9) | 61.7% (60.2 to 63.1) | 80.1% (78.8 to 81.3) | class means; alpha 0.62; lam 0, c 0.1 |
| prototypes + sentences | 27.7% (26.4 to 29.0) | 50.5% (49.1 to 52.0) | 38.1% (36.7 to 39.6) | 62.1% (60.6 to 63.6) | 80.2% (79.0 to 81.4) | species_com, beta 0.1, bias for species without photos 0.2; alpha 0.63; lam 0, c 0.1 |
| discriminant | 34.0% (32.6 to 35.3) | 58.4% (56.9 to 59.8) | 42.5% (41.1 to 44.0) | 65.3% (63.8 to 66.7) | 81.6% (80.4 to 82.8) | shrinkage 0.3; alpha 0.50; lam 0, c 0.1 |
| discriminant + sentences | 34.5% (33.1 to 35.9) | 58.6% (57.1 to 60.1) | 42.2% (40.7 to 43.7) | 65.5% (64.0 to 66.9) | 82.3% (81.1 to 83.4) | shrinkage 0.3, species_com, gamma 0.03; alpha 0.62; lam 0, c 0.1 |

| Kind of eye from | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 72.4% (71.0 to 73.8) | 0.05% | 0.21% |
| trained on the fitting photos (logistic regression, 15 kinds, no row for `person` or `none`) | 79.0% (77.7 to 80.2) | 0.00% | 0.00% |
| summed species probabilities of the head `discriminant` | 81.6% (80.4 to 82.8) | 0.00% | 0.00% |
| the page's combination of kind rows fitted on the fitting photos and the extra set (every photo counts the same) and the species list (rule `mix`, t_kind 1, w_kind 0.7; species head `discriminant`) | 80.3% (79.0 to 81.5) | 0.02% | 0.05% |

**The kind decision.** The kinds head, its temperature, its weight against the species list and the rule were chosen on 1803 wildlife tuning photos and 3056 tuning photos of the extra set `coco-kinds` (`images/coco-kinds`). Another 5944 of its photos were there for fitting kind rows, and its 1240 test photos (`images/coco-kinds.wasm-int8-per-channel`) are only reported. The number tuned on is the mean of the share right on the wildlife tuning photos and of the mean share right over the extra set's kinds. Each row is one kinds head under one rule at its best setting on the tuning photos. `kind_at` is the level this computation gives for an asserted kind to be right 95 times in 100 on each tuning set by itself; the level a slot ships with is set by `tools/eval/shipped.py` through `fuse.py`.

|  | Kinds head | Rule | t_kind | w_kind | Tuning number | Wildlife tuning photos | Extra tuning photos | Kind right, wildlife test | Kind right, extra test | kind_at | Asserted, wildlife test | Right when asserted | Asserted, extra test | Right when asserted |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | kind phrases | mix | 100 | 0.7 | 80.2% | 76.3% | 84.2% | 76.6% (75.3 to 77.9) | 81.8% (79.6 to 83.9) | 0.86 | 43.2% (41.6 to 44.9) | 97.4% (96.6 to 98.1) | 32.7% (30.1 to 35.2) | 96.5% (94.6 to 98.0) |
|  | kind phrases | product | 50 | 0.9 | 79.8% | 76.1% | 83.5% | 76.4% (75.1 to 77.7) | 82.2% (80.0 to 84.4) | 0.87 | 11.5% (10.5 to 12.6) | 96.9% (95.2 to 98.3) | 9.6% (8.1 to 11.3) | 100.0% (100.0 to 100.0) |
|  | kind rows fitted on the fitting photos and the extra set (every photo counts the same) | mix | 1 | 0.7 | 86.9% | 80.3% | 93.4% | 80.3% (79.0 to 81.5) | 95.4% (94.2 to 96.5) | 0.82 | 58.4% (56.9 to 60.0) | 96.2% (95.5 to 97.0) | 86.8% (84.8 to 88.7) | 98.9% (98.2 to 99.4) |
|  | kind rows fitted on the fitting photos and the extra set (every photo counts the same) | product | 2 | 0.9 | 86.3% | 78.9% | 93.6% | 79.2% (77.9 to 80.4) | 95.6% (94.3 to 96.7) | 0.99 | 52.7% (51.2 to 54.2) | 96.0% (95.2 to 96.8) | 90.3% (88.6 to 92.0) | 98.8% (98.0 to 99.4) |
|  | kind rows fitted on the fitting photos and the extra set (a kind's photos weighted by the inverse square root of their number) | mix | 0.5 | 0.7 | 86.8% | 81.0% | 92.6% | 82.0% (80.7 to 83.1) | 95.6% (94.4 to 96.7) | 0.60 | 58.2% (56.7 to 59.8) | 96.3% (95.6 to 97.0) | 88.6% (86.9 to 90.3) | 99.1% (98.5 to 99.6) |
|  | kind rows fitted on the fitting photos and the extra set (a kind's photos weighted by the inverse square root of their number) | product | 0.5 | 0.9 | 85.8% | 79.1% | 92.5% | 81.0% (79.8 to 82.1) | 95.5% (94.3 to 96.6) | 0.62 | 53.8% (52.3 to 55.4) | 96.6% (95.9 to 97.3) | 92.1% (90.6 to 93.6) | 98.4% (97.6 to 99.1) |
|  | kind rows fitted on the fitting photos and the extra set (every kind counts the same) | mix | 0.5 | 0.7 | 86.2% | 79.7% | 92.8% | 81.0% (79.8 to 82.2) | 95.4% (94.2 to 96.5) | 0.60 | 52.8% (51.2 to 54.4) | 96.3% (95.6 to 97.1) | 89.3% (87.5 to 90.9) | 98.8% (98.2 to 99.4) |
|  | kind rows fitted on the fitting photos and the extra set (every kind counts the same) | product | 0.5 | 0.9 | 84.4% | 76.1% | 92.6% | 77.5% (76.3 to 78.8) | 95.7% (94.4 to 96.7) | 0.64 | 47.1% (45.5 to 48.6) | 95.9% (95.0 to 96.8) | 92.3% (90.7 to 93.7) | 98.5% (97.7 to 99.1) |
| **chosen** | kind rows fitted on the fitting photos and the extra set (every photo counts the same) | mix | 1 | 0.7 | 86.9% | 80.3% | 93.4% | 80.3% (79.0 to 81.5) | 95.4% (94.2 to 96.5) | 0.82 | 58.4% (56.9 to 60.0) | 96.2% (95.5 to 97.0) | 86.8% (84.8 to 88.7) | 98.9% (98.2 to 99.4) |
| what the wildlife photos alone would choose | kind rows fitted on the fitting photos and the extra set (a kind's photos weighted by the inverse square root of their number) | product | 0.5 | 0.5 | 79.2% | 81.8% | 76.6% | 82.1% (80.9 to 83.3) | 90.5% (88.8 to 92.1) | 0.98 | 10.3% (9.4 to 11.2) | 99.1% (98.1 to 99.8) | 13.5% (11.6 to 15.5) | 97.0% (94.0 to 99.4) |

The chosen setting on the extra set's test photos, by kind (no species is named in this computation):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 98.2% (96.8 to 99.5) | 96.0% | 99.5% | 93.8% | 98.2% | 1.2% | – | none (5) |
| none | 500 | 96.0% (94.2 to 97.6) | 93.0% | 99.8% | 82.9% | 0.4% | 96.0% | – | dog (6) |
| cat | 77 | 90.9% (84.4 to 97.4) | 88.3% | 94.1% | 77.8% | 1.3% | 5.2% | – | none (4) |
| dog | 63 | 82.5% (73.0 to 92.1) | 4.8% | 0.0% | 98.3% | 0.0% | 0.0% | – | cat (8) |
| deer | 200 | 94.0% (90.5 to 97.0) | 78.0% | 98.7% | 95.5% | 1.5% | 0.0% | – | dog (8) |

Top-1 with the prior for each head, by how many fitting photos the species has:

| Fitting photos of the species | Test photos | sentences | prototypes | prototypes + sentences | discriminant | discriminant + sentences |
|---|---:|---:|---:|---:|---:|---:|
| no training photo | 45 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| 1 or 2 | 56 | 0.0% | 0.0% | 0.0% | 1.8% | 0.0% |
| 3 to 9 | 136 | 0.0% | 7.3% | 6.6% | 9.6% | 8.1% |
| 10 to 29 | 289 | 0.7% | 9.7% | 9.3% | 18.7% | 16.3% |
| 30 or more | 3671 | 30.2% | 41.8% | 42.6% | 46.7% | 46.7% |

**Confidence.** For the head `discriminant`, the scale was set on the tuning photos (expected calibration error 0.134 there). A species is named when its probability is at least 0.98, the lowest level from which named species were right at least nine times in ten on the tuning photos; three species are offered when the first three together reach 0.92, set the same way. On the test photos a species is then named for 2.6% (2.2 to 3.1) of photos and that name is right for 89.2% (82.9 to 94.6) of them; three species are offered for 11.2% (10.2 to 12.1) and hold the right one for 90.8% (88.1 to 93.4); 86.2% (85.2 to 87.2) get a kind of eye only. These figures leave out the page's rule that names and offers must agree with the winning kind; the exported slot is scored with that rule.

| Top probability | Tuning photos | Mean probability | Share right |
|---|---:|---:|---:|
| 0.0 to 0.1 | 525 | 5.9% | 18.1% |
| 0.1 to 0.2 | 342 | 14.2% | 35.1% |
| 0.2 to 0.3 | 212 | 24.9% | 46.2% |
| 0.3 to 0.4 | 167 | 34.6% | 40.7% |
| 0.4 to 0.5 | 116 | 45.2% | 57.8% |
| 0.5 to 0.6 | 97 | 54.0% | 63.9% |
| 0.6 to 0.7 | 72 | 65.4% | 75.0% |
| 0.7 to 0.8 | 78 | 75.4% | 68.0% |
| 0.8 to 0.9 | 66 | 85.3% | 80.3% |
| 0.9 to 1.0 | 128 | 96.1% | 88.3% |

- The map into BioCLIP 2's space could not be fitted: BioCLIP 2's vectors of the fitting photos are not published yet.
