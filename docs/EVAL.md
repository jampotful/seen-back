# Evaluation: what the recognizers get right, and how we know

_This file is written by `tools/eval/report.py` from the JSON files under `docs/eval/`, which the scripts in `tools/eval/` produce. Do not edit it by hand. The commands are at the end._

## What was measured

The question is how often a model names the right species, and the right kind of eye, for a photo of a living thing taken in Alachua County, Florida.

- **The photos.** The evaluation set `alachua-2025` holds 6,000 research-grade iNaturalist photos dated 2025-01-01 to 2026-09-29, one photo an observation (`data/eval/alachua-2025/SUMMARY.md`). A hash of the record's id puts 1803 photos in `val` and 4197 in `test`. Every setting is chosen on `val`. Every number below comes from `test`.
- **The list.** A model answers with one of the 5911 species recorded in the county through 2024 (`data/regions/us-fl-alachua/species.json`). The list also gives each species' records by calendar month, and its kind of eye.
- **Scoring against sentences.** Each species becomes a row made by the model's text half from sentences that hold its name. A photo's score for a species is the cosine between the photo's vector and that row. Three kinds of rows were tried: the scientific name, the English name, and the taxonomy followed by the English name in the form BioCLIP was trained on.
- **The prior.** The place-and-season prior adds `alpha * log(share)` to a species' score, where `share` is the species' part of all records of that calendar month. A month's weight for a species is its records in that month, plus `lam` times a twelfth of its yearly records, plus `c`. This is the arithmetic of `tools/fusion/fuse.py`, with the smoothing written into the table's monthly weights.
- **Intervals.** Each share is followed by a 95% percentile interval from 2000 bootstrap resamples over photos (seed 20261011). The intervals describe the luck of which photos were drawn. They say nothing about photos of another kind.

## The main table

Test split, 4197 photos. For each model the species rows are the label set that did best on `val`. The kind of eye is given twice: from the model's own kind phrases (`labels/kinds.json`, seventeen rows that include `person` and `none`), and from the kind of the top species with the prior.

| Model | Kind from phrases | Kind from top species | Species rows from | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior |
|---|---:|---:|---|---:|---:|---:|---:|
| bioclip25-h14 | 70.0% (68.7 to 71.4) | 98.1% (97.6 to 98.5) | scientific name | 92.9% (92.1 to 93.7) | 97.3% (96.8 to 97.8) | 93.4% (92.7 to 94.2) | 97.7% (97.2 to 98.1) |
| bioclip2-l14 | 76.1% (74.8 to 77.4) | 98.3% (97.9 to 98.7) | scientific name | 90.3% (89.4 to 91.3) | 96.8% (96.2 to 97.3) | 92.4% (91.6 to 93.2) | 97.5% (97.0 to 97.9) |
| bioclip-b16 | 45.5% (44.0 to 47.0) | 92.2% (91.4 to 93.0) | taxonomy and English name | 62.3% (60.7 to 63.8) | 81.6% (80.4 to 82.8) | 69.5% (68.0 to 71.0) | 86.1% (85.1 to 87.2) |
| tinyclip-39m-16 | 77.6% (76.3 to 78.8) | 84.1% (82.9 to 85.2) | English name | 20.9% (19.8 to 22.2) | 37.8% (36.4 to 39.3) | 35.0% (33.6 to 36.4) | 54.1% (52.7 to 55.6) |
| tinyclip-8m-16 | 72.0% (70.6 to 73.5) | 77.7% (76.5 to 78.9) | English name | 14.9% (13.8 to 16.0) | 27.6% (26.3 to 28.9) | 25.9% (24.6 to 27.2) | 43.8% (42.3 to 45.2) |
| tinyclip-61m-32 | 72.6% (71.2 to 74.1) | 76.4% (75.2 to 77.6) | English name | 14.9% (13.8 to 16.0) | 30.3% (28.9 to 31.6) | 27.9% (26.6 to 29.2) | 46.8% (45.2 to 48.3) |
| tinyclip-40m-32 | 69.3% (67.9 to 70.8) | 75.0% (73.7 to 76.3) | English name | 15.1% (14.1 to 16.2) | 28.1% (26.8 to 29.5) | 26.7% (25.4 to 28.1) | 44.6% (43.1 to 46.1) |
| mobileclip2-s0 | 75.4% (74.1 to 76.6) | 83.5% (82.4 to 84.6) | English name | 22.6% (21.3 to 23.8) | 39.0% (37.5 to 40.4) | 33.8% (32.3 to 35.2) | 52.8% (51.4 to 54.2) |
| clip-b32 | 72.0% (70.6 to 73.3) | 81.9% (80.7 to 83.1) | English name | 16.4% (15.3 to 17.5) | 34.7% (33.2 to 36.1) | 31.8% (30.4 to 33.2) | 52.0% (50.5 to 53.5) |
| siglip2-b16 | 79.8% (78.6 to 81.0) | 63.1% (61.6 to 64.6) | scientific name | 9.5% (8.6 to 10.4) | 17.2% (16.1 to 18.4) | 16.7% (15.6 to 17.8) | 27.3% (25.9 to 28.7) |
| bioclip25-mobile-fastvit | – | – | no text half: Study 2 only | – | – | – | – |

All label sets, the gain from the prior with its interval, and the chosen settings are in [`docs/eval/labelsets.md`](eval/labelsets.md). One file a model, with the breakdowns, the confusion tables and the commonest mistakes, is at `docs/eval/model-<id>.md`.

## Baselines and the ceiling

- A recognizer held to the list can be right on at most 99.1% of test photos, because 36 of 4197 show a species with no record in the county before 2025. Held to species with at least 3 records the ceiling is 97.8%, and with at least 10 records it is 94.5%.
- The prior alone, with no photo, names the species in 2.8% (2.3 to 3.3) of test photos and has it in its first five in 8.1% (7.2 to 8.9). Always answering with the county's most recorded species is right in 2.6% (2.1 to 3.1).
- Always answering `plant`, the commonest kind, is right about the kind in 29.1% (27.8 to 30.5).
- With the species rows shuffled, top-1 falls to 0.02% for BioCLIP 2, which is what chance gives. The scores therefore depend on which row belongs to which species.

## BioCLIP 2 in more detail

BioCLIP 2 (ViT-L/14) scored against scientific names is right about the species in 90.3% (89.4 to 91.3) of test photos, and has the species in its first five in 96.8% (96.2 to 97.3). With the prior these become 92.4% (91.6 to 93.2) and 97.5% (97.0 to 97.9); the paired gain in top-1 is +2.1 (+1.4 to +2.7) points. The same computation written twice by different hands (`tools/eval/firstcheck.py` and `tools/eval/study1.py`) gives the same top-1 and top-5 without the prior.

- **Rare species lose under the prior.** For species with 1 or 2 records before 2025, top-1 is 70.7% with the prior and 79.3% without it (58 photos); for 3 to 9 records, 75.4% and 81.2% (138 photos). For species with 200 or more records it is 95.7% and 92.3% (2302 photos). The prior buys its gain on common species and pays for it on rare ones.
- **By kind of eye** (kinds with at least 30 test photos), top-1 with the prior runs from 88.8% for `other` to 100.0% for `rabbit`.
- **Its own kind phrases are weak.** Asked for the kind of eye through the kind phrases, BioCLIP 2 is right in 76.1% (74.8 to 77.4). Taking the kind from its top species is right in 98.3% (97.9 to 98.7). A biology model knows species names far better than everyday words such as "a wading bird".
- **Names that differ between GBIF and iNaturalist.** 198 test photos are of species whose GBIF name differs from the name iNaturalist uses. They were found from SUMMARY.md: the 25 most frequent of the 63 differing pairs (inat.json was not published yet). Top-1 without the prior is 94.4% (90.9 to 97.5) on those photos and 90.1% (89.2 to 91.0) on the rest, so scoring against GBIF's names did not lower the result on these photos.
- **Mistakes.** Of 283 wrong answers for species in the list, 81 named a species of the same genus and 126 one of the same family. The table of commonest mistakes, with links to the observations, is in [`docs/eval/model-bioclip2-l14.md`](eval/model-bioclip2-l14.md).

BioCLIP 2.5 (ViT-H/14) reaches 92.9% (92.1 to 93.7) without the prior and 93.4% (92.7 to 94.2) with it. Its model card does not give the date of its training data, so it cannot be shown that the test photos are new to it. That number is reported with this caveat and is kept out of any claim the app makes.

## The models small enough for a phone, scored against sentences

| Model | File the phone downloads | Kind from phrases | Kind from summed species | Top-1 | Top-1 with prior | Top-5 with prior | Top-1 with prior, WASM int8 vectors | WASM against original (points) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| tinyclip-39m-16 | 41.0 MB | 77.6% (76.3 to 78.8) | 85.8% (84.7 to 86.9) | 20.9% (19.8 to 22.2) | 35.0% (33.6 to 36.4) | 54.1% (52.7 to 55.6) | 34.5% (33.1 to 35.9) | -0.5 (-0.8 to -0.1) |
| tinyclip-8m-16 | 9.6 MB | 72.0% (70.6 to 73.5) | 80.0% (78.8 to 81.2) | 14.9% (13.8 to 16.0) | 25.9% (24.6 to 27.2) | 43.8% (42.3 to 45.2) | 25.5% (24.2 to 26.9) | -0.4 (-0.9 to +0.1) |

Scored against sentences, the small general models name the species in about a quarter to a third of test photos with the prior. That is too weak to show a species name on its own. Their kind of eye from phrases is right in about three photos in four. The vectors a phone computes (WASM, int8) cost about half a point of species top-1 against the original model's vectors; every quantized set is compared in [`docs/eval/variants.md`](eval/variants.md).

## Heads trained on photos (Study 2): machinery proven on a stand-in

This run is a stand-in that proves the machinery. No training vectors were published when it ran, so two thirds of the `val` photos were used to fit the heads and the last third to choose settings. With about two fitting photos a species, these numbers say little about what the real training set (up to sixty photos a species) will give. They are here to show that every step runs and to be replaced.

### tinyclip-39m-16

Trained on 1226 photos of 574 species (`images/alachua-2025 (two thirds of val)`); tested on 4197 test photos (`images/alachua-2025.wasm-int8-per-channel`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Settings chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 22.9% (21.7 to 24.1) | 40.1% (38.7 to 41.6) | 34.9% (33.5 to 36.4) | 56.9% (55.5 to 58.5) | 82.3% (81.2 to 83.4) | species_taxon_com; alpha 0.75; lam 0, c 0.1 |
| prototypes | 27.5% (26.1 to 28.9) | 43.9% (42.4 to 45.4) | 30.1% (28.7 to 31.5) | 45.7% (44.2 to 47.2) | 83.9% (82.8 to 85.0) | class means; alpha 0.38; lam 0, c 0.1 |
| prototypes + sentences | 33.2% (31.8 to 34.6) | 49.3% (47.9 to 50.9) | 36.3% (34.9 to 37.7) | 58.4% (56.9 to 59.9) | 86.3% (85.2 to 87.3) | species_taxon_com, beta 8, bias for species without photos 0.8; alpha 1.00; lam 0, c 0.1 |
| discriminant | 32.5% (31.1 to 34.0) | 45.2% (43.7 to 46.8) | 32.6% (31.2 to 34.0) | 45.4% (43.8 to 46.9) | 82.9% (81.8 to 84.1) | shrinkage 0.3; alpha 0.02; lam 0, c 0.1 |
| discriminant + sentences | 34.4% (33.0 to 35.9) | 48.0% (46.5 to 49.5) | 34.3% (32.8 to 35.7) | 52.0% (50.5 to 53.5) | 78.4% (77.2 to 79.7) | shrinkage 0.3, species_taxon_com, gamma 3; alpha 0.38; lam 2, c 1 |
| mapped to BioCLIP 2 | 26.5% (25.2 to 27.9) | 46.4% (44.9 to 47.9) | 35.2% (33.7 to 36.7) | 57.7% (56.2 to 59.2) | 80.4% (79.2 to 81.6) | ridge 0.01, 1226 pairs; alpha 0.75; lam 0, c 0.1 |

| Kind-of-eye head | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 77.3% (76.0 to 78.7) | 0.05% | 0.10% |
| trained on the fitting photos (logistic regression, 14 kinds, no row for `person` or `none`) | 84.5% (83.4 to 85.5) | 0.00% | 0.00% |
| trained rows, with the sentence rows for `person` and `none` kept beside them | 84.4% (83.2 to 85.5) | 0.10% | 0.33% |
| summed species probabilities of the head `prototypes + sentences` | 86.3% (85.2 to 87.3) | 0.00% | 0.00% |
| the page's combination of the kind phrases and the head `prototypes + sentences` (rule `mix`, t_kind 20, w_kind 0.7) | 86.9% (85.9 to 88.0) | 0.00% | 0.00% |
| the page's combination of the kind phrases and the head `prototypes + sentences` (rule `product`, t_kind 20, w_kind 0.7) | 86.9% (85.9 to 87.9) | 0.02% | 0.02% |

Top-1 with the prior for the head named first above each column, by how many training photos the species has:

| Training photos of the species | Test photos | sentences | prototypes | prototypes + sentences | discriminant | discriminant + sentences | mapped to BioCLIP 2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| no training photo | 1326 | 12.4% | 0.0% | 12.8% | 0.0% | 0.1% | 9.0% |
| 1 or 2 | 1072 | 27.0% | 21.5% | 25.4% | 19.6% | 27.8% | 24.2% |
| 3 to 9 | 1253 | 49.0% | 49.2% | 53.9% | 56.5% | 56.1% | 52.0% |
| 10 to 29 | 312 | 75.0% | 69.9% | 75.6% | 76.9% | 78.2% | 73.7% |
| 30 or more | 234 | 70.9% | 84.2% | 73.1% | 89.3% | 82.0% | 91.9% |

**Confidence.** For the head `prototypes + sentences`, the scale was set on the tuning photos (expected calibration error 0.101 there). A species is named when its probability is at least 0.90, the lowest level from which named species were right at least nine times in ten on the tuning photos; three species are offered when the first three together reach 0.96, set the same way. On the test photos a species is then named for 14.4% (13.3 to 15.5) of photos and that name is right for 91.5% (89.2 to 93.7) of them; three species are offered for 5.9% (5.2 to 6.7) and hold the right one for 93.2% (90.4 to 96.0); 79.7% (78.4 to 80.9) get a kind of eye only. This table leaves out the page's rule that offers come from the winning kind; the section on shipping applies it.

- The map into BioCLIP 2's space was fitted on 1226 pairs of vectors of the same photos.
- The wildlife records hold no people and no photos with nothing alive in them. The sentence rows for `person` and `none` are kept, with a bias set on the tuning photos so that at most 0.5% of them are called `person` or `none`. How often a person is then called a person is unmeasured.

### tinyclip-8m-16

Trained on 1226 photos of 574 species (`images/alachua-2025 (two thirds of val)`); tested on 4197 test photos (`images/alachua-2025.wasm-int8-per-channel`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Settings chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 14.6% (13.5 to 15.7) | 27.6% (26.3 to 28.9) | 25.8% (24.5 to 27.1) | 44.6% (43.1 to 46.1) | 78.1% (76.8 to 79.3) | species_com; alpha 1.25; lam 0, c 0.1 |
| prototypes | 21.3% (20.1 to 22.5) | 36.5% (35.1 to 38.0) | 24.0% (22.7 to 25.3) | 38.8% (37.4 to 40.3) | 77.6% (76.4 to 78.8) | class means; alpha 0.50; lam 2, c 1 |
| prototypes + sentences | 24.3% (23.0 to 25.6) | 41.3% (39.9 to 42.7) | 27.6% (26.3 to 29.0) | 45.5% (44.0 to 47.1) | 79.3% (78.1 to 80.5) | species_com, beta 2, bias for species without photos 0.8; alpha 1.00; lam 0, c 0.1 |
| discriminant | 24.6% (23.3 to 25.9) | 38.1% (36.6 to 39.6) | 24.9% (23.6 to 26.3) | 38.3% (36.8 to 39.8) | 76.7% (75.4 to 77.9) | shrinkage 0.3; alpha 0.25; lam 2, c 1 |
| discriminant + sentences | 26.5% (25.2 to 27.9) | 41.2% (39.7 to 42.7) | 25.6% (24.3 to 26.9) | 43.8% (42.3 to 45.3) | 74.7% (73.5 to 76.1) | shrinkage 0.03, species_com, gamma 3; alpha 0.50; lam 0, c 0.1 |
| mapped to BioCLIP 2 | 16.5% (15.5 to 17.7) | 32.4% (31.1 to 33.9) | 24.3% (23.0 to 25.6) | 45.3% (43.8 to 46.9) | 71.6% (70.2 to 72.9) | ridge 0.01, 1226 pairs; alpha 0.75; lam 0, c 0.1 |

| Kind-of-eye head | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 72.4% (71.0 to 73.8) | 0.05% | 0.21% |
| trained on the fitting photos (logistic regression, 14 kinds, no row for `person` or `none`) | 77.0% (75.7 to 78.3) | 0.00% | 0.00% |
| trained rows, with the sentence rows for `person` and `none` kept beside them | 76.7% (75.4 to 77.9) | 0.26% | 0.86% |
| summed species probabilities of the head `discriminant + sentences` | 74.7% (73.5 to 76.1) | 0.00% | 0.00% |
| the page's combination of the kind phrases and the head `discriminant + sentences` (rule `mix`, t_kind 50, w_kind 0.3) | 77.5% (76.2 to 78.8) | 0.02% | 0.10% |
| the page's combination of the kind phrases and the head `discriminant + sentences` (rule `product`, t_kind 50, w_kind 0.3) | 78.1% (76.8 to 79.3) | 0.02% | 0.10% |

Top-1 with the prior for the head named first above each column, by how many training photos the species has:

| Training photos of the species | Test photos | sentences | prototypes | prototypes + sentences | discriminant | discriminant + sentences | mapped to BioCLIP 2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| no training photo | 1326 | 6.7% | 0.0% | 5.5% | 0.0% | 8.4% | 4.2% |
| 1 or 2 | 1072 | 16.1% | 13.9% | 17.2% | 10.3% | 16.9% | 14.6% |
| 3 to 9 | 1253 | 34.8% | 37.9% | 40.9% | 40.2% | 34.8% | 33.0% |
| 10 to 29 | 312 | 66.7% | 59.9% | 64.1% | 70.2% | 60.3% | 57.0% |
| 30 or more | 234 | 74.8% | 83.3% | 81.2% | 91.0% | 68.0% | 92.3% |

**Confidence.** For the head `discriminant + sentences`, the scale was set on the tuning photos (expected calibration error 0.174 there). A species is named when its probability is at least 0.31, the lowest level from which named species were right at least nine times in ten on the tuning photos; three species are offered when the first three together reach 0.34, set the same way. On the test photos a species is then named for 8.3% (7.4 to 9.1) of photos and that name is right for 89.7% (86.5 to 92.8) of them; three species are offered for 7.4% (6.7 to 8.2) and hold the right one for 80.8% (76.6 to 84.9); 84.3% (83.2 to 85.4) get a kind of eye only. This table leaves out the page's rule that offers come from the winning kind; the section on shipping applies it.

- The map into BioCLIP 2's space was fitted on 1226 pairs of vectors of the same photos.
- The wildlife records hold no people and no photos with nothing alive in them. The sentence rows for `person` and `none` are kept, with a bias set on the tuning photos so that at most 0.5% of them are called `person` or `none`. How often a person is then called a person is unmeasured.

### bioclip2-l14

Trained on 1226 photos of 574 species (`images/alachua-2025 (two thirds of val)`); tested on 4197 test photos (`images/alachua-2025`).

| Species head | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior | Kind from summed species | Settings chosen on the tuning photos |
|---|---:|---:|---:|---:|---:|---|
| sentences | 90.3% (89.4 to 91.3) | 96.8% (96.2 to 97.3) | 92.0% (91.2 to 92.8) | 97.4% (96.9 to 97.9) | 98.3% (97.9 to 98.7) | species_sci; alpha 1.20; lam 2, c 1 |
| prototypes | 61.0% (59.5 to 62.5) | 65.5% (64.1 to 67.0) | 61.1% (59.6 to 62.6) | 65.5% (64.0 to 66.9) | 93.2% (92.4 to 94.0) | class means; alpha 0.40; lam 0, c 0.1 |
| prototypes + sentences | 91.3% (90.5 to 92.2) | 97.3% (96.8 to 97.8) | 91.7% (90.9 to 92.6) | 97.6% (97.1 to 98.0) | 98.5% (98.0 to 98.8) | species_sci, beta 8, bias for species without photos 0.65; alpha 0.60; lam 0, c 0.1 |
| discriminant | 60.1% (58.7 to 61.6) | 64.4% (62.9 to 65.8) | 60.3% (58.9 to 61.8) | 64.5% (63.0 to 65.9) | 89.8% (88.9 to 90.7) | shrinkage 0.3; alpha 0.30; lam 0, c 0.1 |
| discriminant + sentences | 91.0% (90.1 to 91.8) | 97.2% (96.7 to 97.7) | 91.2% (90.3 to 92.1) | 97.5% (97.0 to 98.0) | 98.5% (98.1 to 98.8) | shrinkage 1, species_sci, gamma 3; alpha 0.30; lam 0, c 0.1 |

| Kind-of-eye head | Right kind | Called `person` | Called `none` |
|---|---:|---:|---:|
| kind phrases (sentence rows, with `person` and `none`) | 76.1% (74.8 to 77.4) | 0.00% | 0.00% |
| trained on the fitting photos (logistic regression, 14 kinds, no row for `person` or `none`) | 94.4% (93.7 to 95.0) | 0.00% | 0.00% |
| trained rows, with the sentence rows for `person` and `none` kept beside them | 94.0% (93.3 to 94.7) | 0.02% | 0.86% |
| summed species probabilities of the head `prototypes + sentences` | 98.5% (98.0 to 98.8) | 0.00% | 0.00% |
| the page's combination of the kind phrases and the head `prototypes + sentences` (rule `mix`, t_kind 20, w_kind 0.5) | 98.5% (98.1 to 98.9) | 0.00% | 0.00% |
| the page's combination of the kind phrases and the head `prototypes + sentences` (rule `product`, t_kind 20, w_kind 0.5) | 98.6% (98.2 to 98.9) | 0.00% | 0.00% |

Top-1 with the prior for the head named first above each column, by how many training photos the species has:

| Training photos of the species | Test photos | sentences | prototypes | prototypes + sentences | discriminant | discriminant + sentences |
|---|---:|---:|---:|---:|---:|---:|
| no training photo | 1326 | 85.8% | 0.0% | 83.7% | 0.0% | 82.1% |
| 1 or 2 | 1072 | 93.7% | 78.3% | 94.4% | 74.5% | 93.0% |
| 3 to 9 | 1253 | 94.6% | 95.0% | 95.6% | 95.2% | 96.7% |
| 10 to 29 | 312 | 99.0% | 99.0% | 98.1% | 99.4% | 98.4% |
| 30 or more | 234 | 96.6% | 96.2% | 95.7% | 97.9% | 95.3% |

**Confidence.** For the head `prototypes + sentences`, the scale was set on the tuning photos (expected calibration error 0.022 there). A species is named when its probability is at least 0.05, the lowest level from which named species were right at least nine times in ten on the tuning photos; no level for offers reached nine in ten. On the test photos a species is then named for 100.0% (100.0 to 100.0) of photos and that name is right for 91.7% (90.9 to 92.6) of them; three species are offered for 0.0% (0.0 to 0.0) and hold the right one for –; 0.0% (0.0 to 0.0) get a kind of eye only. This table leaves out the page's rule that offers come from the winning kind; the section on shipping applies it.

- The wildlife records hold no people and no photos with nothing alive in them. The sentence rows for `person` and `none` are kept, with a bias set on the tuning photos so that at most 0.5% of them are called `person` or `none`. How often a person is then called a person is unmeasured.

## As shipped: `val-bioclip2-l14`

The slot holds the head `prototypes + sentences` for `bioclip2-l14` (species_sci, beta 8, bias for species without photos 0.65), fitted on `images/alachua-2025 (two thirds of val)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 20, w_kind 0.5, alpha_prior 0.6. On 565 tuning photos (the third of val kept for tuning) the thresholds came out as name_at 0.05 and offer_at never (no level reached nine in ten). On the 4197 test photos the kind of eye is right for 98.5% (98.1 to 98.9); the top species is right for 91.7% (90.9 to 92.6) and is among the first five for 97.6% (97.1 to 98.0). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The slot needs: species.bias_url (build 7 of the page); fusion.rule mix (build 7 of the page).

| What the page would show | Share of test photos | Right |
|---|---:|---:|
| a species name | 99.6% | the name is right for 92.0% (91.2 to 92.8); the kind for 98.7% (98.3 to 99.0) |
| three species to choose from | 0.0% | the three hold the species for –; the kind is right for – |
| a kind of eye only | 0.4% | the kind is right for 46.7% (20.0 to 73.3) |

## As shipped: `val-tinyclip-39m-16`

The slot holds the head `prototypes + sentences` for `tinyclip-39m-16` (species_taxon_com, beta 8, bias for species without photos 0.8), fitted on `images/alachua-2025 (two thirds of val)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 20, w_kind 0.7, alpha_prior 1. On 565 tuning photos (the third of val kept for tuning) the thresholds came out as name_at 0.89 and offer_at 0.96. On the 4197 test photos the kind of eye is right for 86.9% (85.9 to 88.0); the top species is right for 36.3% (34.9 to 37.7) and is among the first five for 58.4% (56.9 to 59.9). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The slot needs: species.bias_url (build 7 of the page); fusion.rule mix (build 7 of the page).

| What the page would show | Share of test photos | Right |
|---|---:|---:|
| a species name | 15.0% | the name is right for 90.9% (88.7 to 93.0); the kind for 97.5% (96.2 to 98.7) |
| three species to choose from | 4.6% | the three hold the species for 94.8% (91.7 to 97.9); the kind is right for 98.5% (96.4 to 100.0) |
| a kind of eye only | 80.4% | the kind is right for 84.3% (83.1 to 85.5) |

## As shipped: `val-tinyclip-8m-16`

The slot holds the head `discriminant + sentences` for `tinyclip-8m-16` (shrinkage 0.03, species_com, gamma 3), fitted on `images/alachua-2025 (two thirds of val)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 50, w_kind 0.3, alpha_prior 0.5. On 565 tuning photos (the third of val kept for tuning) the thresholds came out as name_at 0.31 and offer_at 0.33. On the 4197 test photos the kind of eye is right for 77.5% (76.2 to 78.8); the top species is right for 25.6% (24.3 to 26.9) and is among the first five for 43.8% (42.3 to 45.3). `person` was said for 0.02% of these photos and `none` for 0.10%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The slot needs: species.bias_url (build 7 of the page); fusion.rule mix (build 7 of the page).

| What the page would show | Share of test photos | Right |
|---|---:|---:|
| a species name | 8.3% | the name is right for 89.9% (86.5 to 92.8); the kind for 99.1% (98.0 to 100.0) |
| three species to choose from | 6.7% | the three hold the species for 78.2% (73.2 to 82.9); the kind is right for 97.1% (95.0 to 98.9) |
| a kind of eye only | 85.1% | the kind is right for 73.9% (72.5 to 75.3) |

## Decisions

- **The pocket model.** On the vectors a phone computes, and scored against sentences, TinyCLIP 39M/16 gets the kind of eye from phrases right for 77.3% (76.0 to 78.7) and the species with the prior for 34.5% (33.1 to 35.9); TinyCLIP 8M/16 gets 72.4% (71.0 to 73.8) and 25.5% (24.2 to 26.9). The first is a 41.0 MB download and took latency in its card in the laboratory's one-thread WASM run; the second is 9.6 MB and took latency in its card. Heads fitted on the real training photos have not been measured, because the training vectors were not published when this report was written, and they decide this choice: a trained head may close the gap between the two models or widen it. Until then the recommendation is TinyCLIP 39M/16 with its sentence rows and the prior, to show a kind of eye and to offer species only above the thresholds measured below, and TinyCLIP 8M/16 if the download has to stay under 10 MB.
- **The server.** BioCLIP 2 (ViT-L/14) with rows made from scientific names, all 5911 species of the list, and the prior (alpha 1.2 at temperature 100, smoothing lam 2 and c 1): top-1 92.4% (91.6 to 93.2), top-5 97.5% (97.0 to 97.9), and the kind of eye from summed species probabilities right for 98.4% (98.0 to 98.7). The kind of eye should come from the species list and the kind phrases should count for little, because this model's kind phrases alone are right for 76.1% (74.8 to 77.4). BioCLIP 2.5 measures 93.4% (92.7 to 94.2) with the prior. Its interval overlaps BioCLIP 2's, it runs at about a third of the speed by the laboratory's timing, and its training date is undocumented, so BioCLIP 2 is the one to run.
- **What the app may say about the server.** A sentence the measurements support: "On photos from Alachua County that iNaturalist's community had already identified, taken in 2025 and 2026, this recognizer named the species for about 92 photos in 100." It may add that such photos are easier than a photo taken in passing. It may not compare itself with iNaturalist's model.
- **Names and offers for `val-bioclip2-l14`.** With name_at 0.05 and offer_at never, set on the tuning photos, the page would name a species for 99.6% of test photos and be right for 92.0% (91.2 to 92.8) of those; it would offer three species for 0.0% and they would hold the right one for –.
- **Names and offers for `val-tinyclip-39m-16`.** With name_at 0.89 and offer_at 0.96, set on the tuning photos, the page would name a species for 15.0% of test photos and be right for 90.9% (88.7 to 93.0) of those; it would offer three species for 4.6% and they would hold the right one for 94.8% (91.7 to 97.9).
- **Names and offers for `val-tinyclip-8m-16`.** With name_at 0.31 and offer_at 0.33, set on the tuning photos, the page would name a species for 8.3% of test photos and be right for 89.9% (86.5 to 92.8) of those; it would offer three species for 6.7% and they would hold the right one for 78.2% (73.2 to 82.9).

## Where the first look differed

The coordinator's first look (`quick.py`) gave the numbers in the left column of each pair. The right column is this study's number for the same model and label set.

| Model | Measure | First look | This study | First look against this study's interval |
|---|---|---:|---:|---|
| bioclip2-l14 | top-1 | 90.4% | 90.3% (89.4 to 91.3) | inside the interval |
| bioclip2-l14 | top-5 | 96.8% | 96.8% (96.2 to 97.3) | inside the interval |
| bioclip2-l14 | top-1 with prior | 92.5% | 92.4% (91.6 to 93.2) | inside the interval |
| bioclip2-l14 | top-5 with prior | 97.5% | 97.5% (97.0 to 97.9) | inside the interval |
| bioclip2-l14 | kind from top species | 98.0% | 98.0% (97.6 to 98.4) | inside the interval |
| bioclip25-h14 | top-1 | 92.9% | 92.9% (92.1 to 93.7) | inside the interval |
| bioclip25-h14 | top-5 | 97.3% | 97.3% (96.8 to 97.8) | inside the interval |
| bioclip25-h14 | top-1 with prior | 93.6% | 93.4% (92.7 to 94.2) | inside the interval |
| bioclip25-h14 | top-5 with prior | 97.7% | 97.7% (97.2 to 98.1) | inside the interval |
| tinyclip-39m-16 | kind from phrases | 77.6% | 77.6% (76.3 to 78.8) | inside the interval |
| tinyclip-39m-16 | top-1 | 21.0% | 20.9% (19.8 to 22.2) | inside the interval |
| tinyclip-39m-16 | top-1 with prior | 35.0% | 35.0% (33.6 to 36.4) | inside the interval |
| tinyclip-8m-16 | kind from phrases | 72.0% | 72.0% (70.6 to 73.5) | inside the interval |
| tinyclip-8m-16 | top-1 | 15.0% | 14.9% (13.8 to 16.0) | inside the interval |
| tinyclip-8m-16 | top-1 with prior | 27.0% | 25.9% (24.6 to 27.2) | inside the interval |

The first look chose its settings on `val` from a smaller grid and without smoothing choices, so differences of a point with the prior are expected.

## Checks for leakage and for mistakes

`tools/eval/checks.py` ran 31 checks: 24 passed, 0 failed, 6 are facts to know, and 1 wait for a file that is not published yet. The full table is in [`docs/eval/checks.md`](eval/checks.md).

- **Scientific names carried by more than one species key.** 1: {"Salvia azurea": [8283204, 2927067]}. Their sentence rows are identical, so the later key can never be the top answer; photos of it on the test split: 0.
- **Test photos whose species is not in the list at all.** 36 of 4197 (so a recognizer held to the list can reach at most 0.9914)
- **Label files whose kind of eye differs from the species list.** 9 label sets (bioclip-b16, mobileclip2-s0, siglip2-b16) carry another kind of eye than the list in 1 of 5911 rows. The studies take the kind from the species list, so no number here is touched; a slot built from these label files would show the earlier kinds.
- **Label rows made from an earlier species.json.** 21 label sets (of bioclip2-l14, bioclip25-h14, clip-b32, tinyclip-39m-16, tinyclip-40m-32, tinyclip-61m-32, tinyclip-8m-16) were made before the list's English names were revised: 645 of 5911 rows carry an English name the list no longer has (keys, scientific names and kinds agree in every row). Results for species_sci are unaffected; results for species_com and species_taxon_com describe the earlier names and would change if the rows were made again.
- **Label rows made from an earlier species.json.** 9 label sets (of bioclip-b16, mobileclip2-s0, siglip2-b16) were made before the list's English names were revised: 2099 of 5911 rows carry an English name the list no longer has (keys, scientific names and kinds agree in every row). Results for species_sci are unaffected; results for species_com and species_taxon_com describe the earlier names and would change if the rows were made again.
- **How tightly BioCLIP 2 groups a species.** 1470 of 4197 test photos have a val photo within cosine 0.95, and for 1454 of those it is the same species. Photos of one species sit close together in this model, which is why a list of names is enough for it.
- **Training photos share no record with the evaluation photos.** data/train/alachua-pre2025/manifest.csv is not published yet

What the checks cover: the dates of the photos against the species list's cutoff and against the snapshot behind BioCLIP 2's training data; that no id, observation or photo address repeats; that the split follows from the record id alone; that every vector file has the manifest's 6,000 ids in order; that label rows follow the species list; that no test photo has a copy on `val`; and, once the training manifest exists, that it shares no record, observation or photo with the evaluation set. The image vectors are made from the photo file alone: `tools/lab/lab.py` (`embed_rows`) reads only the row id to find the file.

## What this does not show

- **These photos are easier than what a phone meets.** Research-grade means that people on iNaturalist, often helped by iNaturalist's own model, already agreed on the species. Photos nobody could identify are absent. A photo taken in passing, at a distance, or of a species that needs a microscope will do worse than these numbers.
- **The large models were trained on photos of this kind.** BioCLIP 2's training data was built from a GBIF snapshot of 2024-05-01 that includes iNaturalist's research-grade photos. No test photo can be in it, since all are dated 2025 or later, yet the test photos come from the same platform, the same county and in part the same observers as its training photos. The result describes that setting.
- **One region.** Every number is for Alachua County and for a list of its own species. A longer list, or a place with fewer records, will give lower numbers.
- **The labels follow GBIF's names.** Where GBIF and iNaturalist split or name a species differently, a photo is counted against GBIF's species.
- **Nothing here compares with iNaturalist's own model.** We cannot run it, and its published accuracy figures are measured on other photos with other rules. No sentence in the app may say or suggest that this recognizer matches it.
- **People, pets and photos with nothing alive in them are missing from the evaluation set.** How often a person is called a person is unmeasured here.
- **Top-5 is measured against the whole list.** The page offers three species of the winning kind; that rule is measured only in the section on shipping, when it is present.

## How to rerun

```
python3 -I tools/eval/fetch.py ROOT            # the published data and vectors, into ROOT/data and ROOT/lab
python3 -I tools/eval/checks.py ROOT           # docs/eval/checks.json
python3 -I tools/eval/study1.py ROOT           # docs/eval/study1.json (about four minutes on two cores)
python3 -I tools/eval/study2.py ROOT --train val                # trained heads with val standing in for a training set
python3 -I tools/eval/study2.py ROOT --train alachua-pre2025    # trained heads for real, once the training vectors are published
python3 -I tools/eval/export_heads.py ROOT --model MODEL --out DIR   # the chosen heads in the layout of models/<slot>/
python3 -I tools/eval/shipped.py ROOT DIR      # the exported slot, scored through tools/fusion/fuse.py
python3 -I tools/eval/report.py                # this file and the tables under docs/eval/
```

Inputs of this run: `pub/data-alachua` at `949460f866e7`; `pub/lab-bioclip-b16` at `8390d0006a34`; `pub/lab-bioclip2-l14` at `f552a63fbd5e`; `pub/lab-bioclip25-h14` at `40532989b3a9`; `pub/lab-bioclip25-mobile-fastvit` at `3c8cc3bd2386`; `pub/lab-clip-b32` at `721281767c8b`; `pub/lab-mobileclip2-s0` at `3da256a7dad0`; `pub/lab-siglip2-b16` at `5efd3b247595`; `pub/lab-tinyclip-39m-16` at `d68a5fc88c30`; `pub/lab-tinyclip-40m-32` at `6d8c0ecbd92e`; `pub/lab-tinyclip-61m-32` at `bd62f0f43f8c`; `pub/lab-tinyclip-8m-16` at `af03032158c3`.
