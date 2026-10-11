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
| the page's combination of kind phrases and the species list (rule `mix`, t_kind 100, w_kind 0.5; species head `sentences`) | 81.4% (80.2 to 82.6) | 0.07% | 0.07% |

**The kind decision.** The kinds head, its temperature, its weight against the species list and the rule were chosen on 1803 wildlife tuning photos and 3056 tuning photos of the extra set `coco-kinds` (`images/coco-kinds`). Another 5944 of its photos were there for fitting kind rows, and its 1240 test photos (`images/coco-kinds.wasm-int8-per-channel`) are only reported. The number tuned on is the mean of the share right on the wildlife tuning photos and of the mean share right over the extra set's kinds. Each row is one kinds head under one rule at its best setting on the tuning photos. `kind_at` is the level this computation gives for an asserted kind to be right 95 times in 100 on each tuning set by itself; the level a slot ships with is set by `tools/eval/shipped.py` through `fuse.py`.

|  | Kinds head | Rule | t_kind | w_kind | Tuning number | Wildlife tuning photos | Extra tuning photos | Kind right, wildlife test | Kind right, extra test | kind_at | Asserted, wildlife test | Right when asserted | Asserted, extra test | Right when asserted |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | kind phrases | mix | 100 | 0.5 | 84.2% | 82.0% | 86.5% | 81.4% (80.2 to 82.6) | 80.1% (77.8 to 82.3) | 0.76 | 48.8% (47.3 to 50.4) | 97.7% (97.0 to 98.3) | 29.0% (26.5 to 31.5) | 97.8% (96.1 to 99.2) |
|  | kind phrases | product | 100 | 0.7 | 83.1% | 81.0% | 85.2% | 81.1% (79.9 to 82.3) | 81.5% (79.1 to 83.5) | 0.91 | 43.0% (41.5 to 44.6) | 95.9% (94.9 to 96.7) | 27.0% (24.6 to 29.5) | 97.9% (96.1 to 99.4) |
| **chosen** | kind phrases | mix | 100 | 0.5 | 84.2% | 82.0% | 86.5% | 81.4% (80.2 to 82.6) | 80.1% (77.8 to 82.3) | 0.76 | 48.8% (47.3 to 50.4) | 97.7% (97.0 to 98.3) | 29.0% (26.5 to 31.5) | 97.8% (96.1 to 99.2) |
| what the wildlife photos alone would choose | kind phrases | product | 20 | 0.5 | 54.2% | 84.4% | 24.1% | 83.7% (82.6 to 84.8) | 22.1% (19.8 to 24.4) | none | 100.0% (100.0 to 100.0) | 83.7% (82.6 to 84.8) | 100.0% (100.0 to 100.0) | 22.1% (19.8 to 24.4) |

The chosen setting on the extra set's test photos, by kind (no species is named in this computation):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 94.8% (92.2 to 96.8) | 73.5% | 100.0% | 86.8% | 94.8% | 0.5% | – | insect (7) |
| none | 500 | 62.8% (58.6 to 67.0) | 11.8% | 88.1% | 72.6% | 3.2% | 62.8% | – | plant (64) |
| cat | 77 | 90.9% (84.4 to 97.4) | 2.6% | 100.0% | 94.7% | 0.0% | 2.6% | – | dog (2) |
| dog | 63 | 88.9% (81.0 to 95.2) | 0.0% | – | 92.1% | 1.6% | 0.0% | – | cat (4) |
| deer | 200 | 87.0% (82.0 to 91.5) | 2.5% | 80.0% | 96.9% | 8.0% | 0.0% | – | person (16) |

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


## tinyclip-8m-16

Fitted on 0 photos of 0 species (`none (sentence rows only)`); settings chosen on 1803 tuning photos; tested on 4197 test photos (`images/alachua-2025.wasm-int8-per-channel`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 15.1% (14.0 to 16.2) | 28.0% (26.7 to 29.3) | 26.5% (25.1 to 27.8) | 45.4% (43.9 to 46.9) | 78.2% (77.0 to 79.5) | species_com; alpha 1.00; lam 0, c 0.1 |

| Kind of eye from | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 72.4% (71.0 to 73.8) | 0.05% | 0.21% |
| summed species probabilities of the head `sentences` | 78.2% (77.0 to 79.5) | 0.00% | 0.00% |
| the page's combination of kind phrases and the species list (rule `mix`, t_kind 100, w_kind 0.5; species head `sentences`) | 77.3% (76.0 to 78.6) | 0.07% | 0.26% |

**The kind decision.** The kinds head, its temperature, its weight against the species list and the rule were chosen on 1803 wildlife tuning photos and 3056 tuning photos of the extra set `coco-kinds` (`images/coco-kinds`). Another 5944 of its photos were there for fitting kind rows, and its 1240 test photos (`images/coco-kinds.wasm-int8-per-channel`) are only reported. The number tuned on is the mean of the share right on the wildlife tuning photos and of the mean share right over the extra set's kinds. Each row is one kinds head under one rule at its best setting on the tuning photos. `kind_at` is the level this computation gives for an asserted kind to be right 95 times in 100 on each tuning set by itself; the level a slot ships with is set by `tools/eval/shipped.py` through `fuse.py`.

|  | Kinds head | Rule | t_kind | w_kind | Tuning number | Wildlife tuning photos | Extra tuning photos | Kind right, wildlife test | Kind right, extra test | kind_at | Asserted, wildlife test | Right when asserted | Asserted, extra test | Right when asserted |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | kind phrases | mix | 100 | 0.5 | 80.6% | 76.9% | 84.3% | 77.3% (76.0 to 78.6) | 83.2% (81.0 to 85.2) | 0.80 | 42.5% (41.0 to 44.1) | 97.4% (96.7 to 98.2) | 28.1% (25.7 to 30.6) | 96.9% (94.8 to 98.6) |
|  | kind phrases | product | 100 | 0.7 | 79.3% | 76.0% | 82.6% | 75.7% (74.4 to 77.0) | 82.8% (80.7 to 84.9) | 0.99 | 6.9% (6.2 to 7.7) | 97.2% (95.2 to 99.0) | 5.8% (4.5 to 7.2) | 100.0% (100.0 to 100.0) |
| **chosen** | kind phrases | mix | 100 | 0.5 | 80.6% | 76.9% | 84.3% | 77.3% (76.0 to 78.6) | 83.2% (81.0 to 85.2) | 0.80 | 42.5% (41.0 to 44.1) | 97.4% (96.7 to 98.2) | 28.1% (25.7 to 30.6) | 96.9% (94.8 to 98.6) |
| what the wildlife photos alone would choose | kind phrases | product | 20 | 0.5 | 56.2% | 79.8% | 32.7% | 79.4% (78.2 to 80.6) | 26.2% (23.7 to 28.8) | none | 100.0% (100.0 to 100.0) | 79.4% (78.2 to 80.6) | 100.0% (100.0 to 100.0) | 26.2% (23.7 to 28.8) |

The chosen setting on the extra set's test photos, by kind (no species is named in this computation):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 90.8% (87.8 to 93.5) | 38.2% | 99.3% | 96.4% | 90.8% | 3.5% | – | other (16) |
| none | 500 | 78.6% (74.8 to 82.2) | 36.6% | 96.7% | 83.9% | 1.2% | 78.6% | – | plant (52) |
| cat | 77 | 92.2% (85.7 to 97.4) | 3.9% | 66.7% | 94.6% | 1.3% | 3.9% | – | none (3) |
| dog | 63 | 81.0% (71.4 to 90.5) | 0.0% | – | 90.5% | 3.2% | 0.0% | – | cat (6) |
| deer | 200 | 76.5% (70.5 to 82.0) | 5.0% | 70.0% | 91.1% | 14.0% | 2.5% | – | person (28) |

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


## bioclip2-l14

Fitted on 0 photos of 0 species (`none (sentence rows only)`); settings chosen on 1803 tuning photos; tested on 4197 test photos (`images/alachua-2025`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 90.3% (89.4 to 91.3) | 96.8% (96.2 to 97.3) | 92.5% (91.6 to 93.2) | 97.5% (97.0 to 97.9) | 98.3% (97.9 to 98.7) | species_sci; alpha 1.00; lam 2, c 1 |

| Kind of eye from | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 76.1% (74.8 to 77.4) | 0.00% | 0.00% |
| summed species probabilities of the head `sentences` | 98.3% (97.9 to 98.7) | 0.00% | 0.00% |
| the page's combination of kind phrases and the species list (rule `mix`, t_kind 100, w_kind 0.5; species head `sentences`) | 98.0% (97.6 to 98.4) | 0.00% | 0.00% |

**The kind decision.** The kinds head, its temperature, its weight against the species list and the rule were chosen on 1803 wildlife tuning photos and 3056 tuning photos of the extra set `coco-kinds` (`images/coco-kinds`). Another 5944 of its photos were there for fitting kind rows, and its 1240 test photos (`images/coco-kinds`) are only reported. The number tuned on is the mean of the share right on the wildlife tuning photos and of the mean share right over the extra set's kinds. Each row is one kinds head under one rule at its best setting on the tuning photos. `kind_at` is the level this computation gives for an asserted kind to be right 95 times in 100 on each tuning set by itself; the level a slot ships with is set by `tools/eval/shipped.py` through `fuse.py`.

|  | Kinds head | Rule | t_kind | w_kind | Tuning number | Wildlife tuning photos | Extra tuning photos | Kind right, wildlife test | Kind right, extra test | kind_at | Asserted, wildlife test | Right when asserted | Asserted, extra test | Right when asserted |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | kind phrases | mix | 100 | 0.5 | 65.2% | 97.8% | 32.6% | 98.0% (97.6 to 98.4) | 17.0% (14.9 to 19.1) | none | 100.0% (100.0 to 100.0) | 98.0% (97.6 to 98.4) | 100.0% (100.0 to 100.0) | 17.0% (14.9 to 19.1) |
|  | kind phrases | product | 100 | 0.5 | 64.9% | 98.0% | 31.8% | 97.9% (97.5 to 98.3) | 16.9% (14.8 to 19.0) | 0.97 | 53.2% (51.7 to 54.6) | 99.8% (99.6 to 100.0) | 2.5% (1.6 to 3.4) | 96.8% (90.3 to 100.0) |
| **chosen** | kind phrases | mix | 100 | 0.5 | 65.2% | 97.8% | 32.6% | 98.0% (97.6 to 98.4) | 17.0% (14.9 to 19.1) | none | 100.0% (100.0 to 100.0) | 98.0% (97.6 to 98.4) | 100.0% (100.0 to 100.0) | 17.0% (14.9 to 19.1) |
| what the wildlife photos alone would choose | kind phrases | mix | 20 | 0.7 | 64.9% | 98.3% | 31.5% | 98.3% (97.8 to 98.6) | 15.7% (13.6 to 17.7) | none | 100.0% (100.0 to 100.0) | 98.3% (97.8 to 98.6) | 100.0% (100.0 to 100.0) | 15.7% (13.6 to 17.7) |

The chosen setting on the extra set's test photos, by kind (no species is named in this computation):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 0.0% (0.0 to 0.0) | 100.0% | 0.0% | – | 0.0% | 0.0% | – | other (248) |
| none | 500 | 0.0% (0.0 to 0.0) | 100.0% | 0.0% | – | 0.0% | 0.0% | – | other (301) |
| cat | 77 | 85.7% (77.9 to 93.5) | 100.0% | 85.7% | – | 0.0% | 0.0% | – | other (8) |
| dog | 63 | 14.3% (6.3 to 23.8) | 100.0% | 14.3% | – | 0.0% | 0.0% | – | other (45) |
| deer | 200 | 68.0% (61.5 to 74.0) | 100.0% | 68.0% | – | 0.0% | 0.0% | – | wader (47) |

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
