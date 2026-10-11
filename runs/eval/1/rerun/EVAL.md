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

- **Photos that belong together.** Several photos of one species on one day often come from one outing, so they are less than independent. Resampling whole groups (one species on one day, 3949 groups) instead of single photos gives 90.3% (89.4 to 91.3) without the prior and 92.4% (91.5 to 93.2) with it, against the intervals above.
- **Rare species lose under the prior.** For species with 1 or 2 records before 2025, top-1 is 70.7% with the prior and 79.3% without it (58 photos); for 3 to 9 records, 75.4% and 81.2% (138 photos). For species with 200 or more records it is 95.7% and 92.3% (2302 photos). The prior buys its gain on common species and pays for it on rare ones.
- **By kind of eye** (kinds with at least 30 test photos), top-1 with the prior runs from 88.8% for `other` to 100.0% for `rabbit`.
- **Its own kind phrases are weak.** Asked for the kind of eye through the kind phrases, BioCLIP 2 is right in 76.1% (74.8 to 77.4). Taking the kind from its top species is right in 98.3% (97.9 to 98.7). A biology model knows species names far better than everyday words such as "a wading bird".
- **Names that differ between GBIF and iNaturalist.** 198 test photos are of species whose GBIF name differs from the name iNaturalist uses. They were found from the 25 most frequent of the 63 differing pairs, as listed in `data/eval/alachua-2025/SUMMARY.md`, because `inat.json` was not published yet (the summary counts 331 such rows in the whole set). Top-1 without the prior is 94.4% (90.9 to 97.5) on those photos and 90.1% (89.2 to 91.0) on the rest, so scoring against GBIF's names did not lower the result on these photos.
- **Mistakes.** Of 283 wrong answers for species in the list, 81 named a species of the same genus and 126 one of the same family. The table of commonest mistakes, with links to the observations, is in [`docs/eval/model-bioclip2-l14.md`](eval/model-bioclip2-l14.md).

BioCLIP 2.5 (ViT-H/14) reaches 92.9% (92.1 to 93.7) without the prior and 93.4% (92.7 to 94.2) with it. Its model card does not give the date of its training data, so it cannot be shown that the test photos are new to it. That number is reported with this caveat and is kept out of any claim the app makes.

## The models small enough for a phone, scored against sentences

| Model | File the phone downloads | Kind from phrases | Kind from summed species | Top-1 | Top-1 with prior | Top-5 with prior | Top-1 with prior, WASM int8 vectors | WASM against original (points) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| tinyclip-39m-16 | 41.0 MB | 77.6% (76.3 to 78.8) | 85.8% (84.7 to 86.9) | 20.9% (19.8 to 22.2) | 35.0% (33.6 to 36.4) | 54.1% (52.7 to 55.6) | 34.5% (33.1 to 35.9) | -0.5 (-0.8 to -0.1) |
| tinyclip-8m-16 | 9.6 MB | 72.0% (70.6 to 73.5) | 80.0% (78.8 to 81.2) | 14.9% (13.8 to 16.0) | 25.9% (24.6 to 27.2) | 43.8% (42.3 to 45.2) | 25.5% (24.2 to 26.9) | -0.4 (-0.9 to +0.1) |

Scored against sentences, the small general models name the species in about a quarter to a third of test photos with the prior. That is too weak to show a species name on its own. Their kind of eye from phrases is right in about three photos in four. The vectors a phone computes (WASM, int8) cost about half a point of species top-1 against the original model's vectors; every quantized set is compared in [`docs/eval/variants.md`](eval/variants.md).

## Sentence rows with the prior, as the page would use them

No head was fitted here. The models' own sentence rows were given the prior, the calibration and the page's combination with the kind phrases, with every setting chosen on the whole of `val`. These are the slots that can ship before any training photo exists.

Species top-1 with the prior on the test photos (the pocket models on the vectors a phone computes):

| Species head | tinyclip-39m-16 | tinyclip-8m-16 | bioclip2-l14 |
|---|---:|---:|---:|
| sentences | 34.8% (33.4 to 36.3) | 25.3% (24.0 to 26.7) | 92.5% (91.6 to 93.2) |

Kind of eye right on the test photos:

| Kind of eye from | tinyclip-39m-16 | tinyclip-8m-16 | bioclip2-l14 |
|---|---:|---:|---:|
| kind phrases | 77.3% (76.0 to 78.7) | 72.4% (71.0 to 73.8) | 76.1% (74.8 to 77.4) |
| summed species probabilities | 82.9% (81.7 to 84.0) | 76.5% (75.2 to 77.8) | 98.3% (97.9 to 98.7) |
| the page's combination of the kind phrases | 84.0% (82.8 to 85.1) | 78.8% (77.6 to 80.1) | 98.3% (97.8 to 98.6) |

- **tinyclip-39m-16.** For the head `sentences`, the scale was set on the tuning photos (expected calibration error 0.153 there). A species is named when its probability is at least 0.40, the lowest level from which named species were right at least nine times in ten on the tuning photos; three species are offered when the first three together reach 0.60, set the same way. On the test photos a species is then named for 15.4% (14.3 to 16.6) of photos and that name is right for 92.7% (90.7 to 94.6) of them; three species are offered for 1.9% (1.5 to 2.3) and hold the right one for 92.4% (86.1 to 97.5); 82.7% (81.5 to 83.8) get a kind of eye only. This table leaves out the page's rule that offers come from the winning kind; the section on shipping applies it.
- **tinyclip-8m-16.** For the head `sentences`, the scale was set on the tuning photos (expected calibration error 0.111 there). A species is named when its probability is at least 0.42, the lowest level from which named species were right at least nine times in ten on the tuning photos; three species are offered when the first three together reach 0.49, set the same way. On the test photos a species is then named for 9.2% (8.3 to 10.1) of photos and that name is right for 89.7% (86.6 to 92.8) of them; three species are offered for 5.1% (4.5 to 5.8) and hold the right one for 83.8% (78.7 to 88.4); 85.6% (84.6 to 86.7) get a kind of eye only. This table leaves out the page's rule that offers come from the winning kind; the section on shipping applies it.
- **bioclip2-l14.** For the head `sentences`, the scale was set on the tuning photos (expected calibration error 0.024 there). A species is named when its probability is at least 0.05, the lowest level from which named species were right at least nine times in ten on the tuning photos; no level for offers reached nine in ten. On the test photos a species is then named for 100.0% (100.0 to 100.0) of photos and that name is right for 92.5% (91.6 to 93.2) of them; three species are offered for 0.0% (0.0 to 0.0) and hold the right one for –; 0.0% (0.0 to 0.0) get a kind of eye only. This table leaves out the page's rule that offers come from the winning kind; the section on shipping applies it.

Every head, its settings, the reliability tables and the breakdown by fitting photos are in [`docs/eval/study2-sentences.md`](eval/study2-sentences.md).

## Trained heads (Study 2): the machinery, proven on a stand-in

This run is a stand-in that proves the machinery. No training vectors were published when it ran, so two thirds of the `val` photos were used to fit the heads and the last third to choose settings. With about two fitting photos a species, these numbers say little about what the real training set (up to sixty photos a species) will give. They are here to show that every step runs and to be replaced.

Species top-1 with the prior on the test photos (the pocket models on the vectors a phone computes):

| Species head | tinyclip-39m-16 | tinyclip-8m-16 | bioclip2-l14 |
|---|---:|---:|---:|
| sentences | 34.6% (33.2 to 36.0) | 25.8% (24.5 to 27.1) | 92.4% (91.6 to 93.2) |
| prototypes | 30.1% (28.7 to 31.5) | 24.0% (22.7 to 25.3) | 61.1% (59.6 to 62.6) |
| prototypes + sentences | 36.9% (35.5 to 38.4) | 26.9% (25.6 to 28.3) | 91.7% (90.9 to 92.6) |
| discriminant | 32.6% (31.2 to 34.0) | 24.9% (23.6 to 26.3) | 60.7% (59.2 to 62.2) |
| discriminant + sentences | 34.6% (33.2 to 36.1) | 25.6% (24.3 to 26.9) | 90.8% (90.0 to 91.7) |
| mapped to BioCLIP 2 | 35.3% (33.8 to 36.8) | 24.3% (23.0 to 25.6) | – |

Kind of eye right on the test photos:

| Kind of eye from | tinyclip-39m-16 | tinyclip-8m-16 | bioclip2-l14 |
|---|---:|---:|---:|
| kind phrases | 77.3% (76.0 to 78.7) | 72.4% (71.0 to 73.8) | 76.1% (74.8 to 77.4) |
| trained on the fitting photos | 84.4% (83.3 to 85.5) | 77.1% (75.8 to 78.3) | 94.3% (93.7 to 95.0) |
| trained rows, with the sentence rows for `person` and `none` kept beside them | 84.3% (83.2 to 85.4) | 76.7% (75.4 to 78.0) | 94.0% (93.3 to 94.7) |
| summed species probabilities | 86.5% (85.5 to 87.5) | 74.7% (73.5 to 76.1) | 98.5% (98.0 to 98.8) |
| the page's combination of the kind phrases | 86.7% (85.7 to 87.7) | 77.5% (76.2 to 78.8) | 98.5% (98.1 to 98.9) |

- **tinyclip-39m-16.** For the head `prototypes + sentences`, the scale was set on the tuning photos (expected calibration error 0.046 there). A species is named when its probability is at least 0.63, the lowest level from which named species were right at least nine times in ten on the tuning photos; no level for offers reached nine in ten. On the test photos a species is then named for 19.5% (18.2 to 20.7) of photos and that name is right for 88.6% (86.4 to 90.8) of them; three species are offered for 0.0% (0.0 to 0.0) and hold the right one for –; 80.5% (79.3 to 81.8) get a kind of eye only. This table leaves out the page's rule that offers come from the winning kind; the section on shipping applies it.
- **tinyclip-8m-16.** For the head `discriminant + sentences`, the scale was set on the tuning photos (expected calibration error 0.174 there). A species is named when its probability is at least 0.31, the lowest level from which named species were right at least nine times in ten on the tuning photos; three species are offered when the first three together reach 0.34, set the same way. On the test photos a species is then named for 8.3% (7.4 to 9.1) of photos and that name is right for 89.7% (86.5 to 92.8) of them; three species are offered for 7.4% (6.7 to 8.2) and hold the right one for 80.8% (76.6 to 84.9); 84.3% (83.2 to 85.4) get a kind of eye only. This table leaves out the page's rule that offers come from the winning kind; the section on shipping applies it.
- **bioclip2-l14.** For the head `prototypes + sentences`, the scale was set on the tuning photos (expected calibration error 0.022 there). A species is named when its probability is at least 0.05, the lowest level from which named species were right at least nine times in ten on the tuning photos; no level for offers reached nine in ten. On the test photos a species is then named for 100.0% (100.0 to 100.0) of photos and that name is right for 91.7% (90.9 to 92.6) of them; three species are offered for 0.0% (0.0 to 0.0) and hold the right one for –; 0.0% (0.0 to 0.0) get a kind of eye only. This table leaves out the page's rule that offers come from the winning kind; the section on shipping applies it.
- The map into BioCLIP 2's space was fitted on 1226 pairs of vectors of the same photos.
- The wildlife records hold no people and no photos with nothing alive in them. The sentence rows for `person` and `none` are kept, with a bias set on the tuning photos so that at most 0.5% of them are called `person` or `none`. How often a person is then called a person is unmeasured.

Every head, its settings, the reliability tables and the breakdown by fitting photos are in [`docs/eval/study2-val.md`](eval/study2-val.md).

## What the page would show

Each slot below was written by `tools/eval/export_heads.py` in the layout of `models/<slot>/` and then scored by `tools/eval/shipped.py`, which reads the slot's own files as the page does and sends every photo through `tools/fusion/fuse.py`. The two thresholds were set on the tuning photos so that a named species, and the three offered species, were right at least nine times in ten there. Slots whose name begins with `val-` hold stand-in heads.

| Slot | Kind right | Top species right | Species named (share, threshold) | Named species right | Three offered (share, threshold) | Offer holds the species | Kind only | Kind right when kind only |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `sentences-bioclip2-l14` | 98.3% (97.8 to 98.6) | 92.5% (91.6 to 93.2) | 99.5% at 0.05 | 92.8% (92.1 to 93.6) | 0.0% at never | – | 0.5% | 30.4% (13.0 to 47.8) |
| `sentences-tinyclip-39m-16` | 83.9% (82.8 to 85.0) | 34.9% (33.5 to 36.4) | 15.4% at 0.4 | 92.7% (90.7 to 94.6) | 3.3% at 0.53 | 84.9% (78.4 to 90.6) | 81.3% | 80.5% (79.2 to 81.8) |
| `sentences-tinyclip-8m-16` | 78.8% (77.6 to 80.0) | 25.3% (24.0 to 26.7) | 9.2% at 0.42 | 89.9% (86.8 to 92.7) | 5.1% at 0.47 | 81.9% (76.8 to 86.6) | 85.7% | 75.6% (74.1 to 77.0) |
| `val-bioclip2-l14` | 98.5% (98.1 to 98.9) | 91.7% (90.9 to 92.6) | 99.6% at 0.05 | 92.0% (91.2 to 92.8) | 0.0% at never | – | 0.4% | 46.7% (20.0 to 73.3) |
| `val-tinyclip-39m-16` | 86.7% (85.7 to 87.7) | 36.9% (35.5 to 38.4) | 19.4% at 0.63 | 88.7% (86.5 to 90.7) | 0.0% at never | – | 80.6% | 83.9% (82.7 to 85.2) |
| `val-tinyclip-8m-16` | 77.5% (76.2 to 78.8) | 25.6% (24.3 to 26.9) | 8.3% at 0.31 | 89.9% (86.5 to 92.8) | 6.7% at 0.33 | 78.2% (73.2 to 82.9) | 85.1% | 73.9% (72.5 to 75.3) |

The text for each slot, with what it needs from the page, is in [`docs/eval/shipped.md`](eval/shipped.md).

## Decisions

- **The pocket model.** On the vectors a phone computes, and scored against sentences, TinyCLIP 39M/16 gets the kind of eye from phrases right for 77.3% (76.0 to 78.7) and the species with the prior for 34.5% (33.1 to 35.9); TinyCLIP 8M/16 gets 72.4% (71.0 to 73.8) and 25.5% (24.2 to 26.9). The first is a 41.0 MB download and took about 333 ms a photo in the laboratory's one-thread WASM run; the second is 9.6 MB and took about 100 ms a photo. With heads fitted on the training photos, the 39M model's best head (`sentences`) names the species for 34.8% (33.4 to 36.3) of test photos with the prior and the 8M model's (`sentences`) for 25.3% (24.0 to 26.7). Recommendation: ship the model whose trained head is ahead by more than the intervals, and prefer the 8M model when they overlap, because it is a quarter of the download and a third of the time.
- **The server.** BioCLIP 2 (ViT-L/14) with rows made from scientific names, all 5911 species of the list, and the prior (alpha 1.2 at temperature 100, smoothing lam 2 and c 1): top-1 92.4% (91.6 to 93.2), top-5 97.5% (97.0 to 97.9), and the kind of eye from summed species probabilities right for 98.4% (98.0 to 98.7). The kind of eye should come from the species list and the kind phrases should count for little, because this model's kind phrases alone are right for 76.1% (74.8 to 77.4). BioCLIP 2.5 measures 93.4% (92.7 to 94.2) with the prior, a paired difference of +1.0 (+0.4 to +1.7) points from BioCLIP 2 on the same photos. It runs at about a third of the speed by the coordinator's notes, and its training date is undocumented, so no number for it can be defended in public. BioCLIP 2 is the one to run.
- **What the app may say about the server.** A sentence the measurements support: "On photos from Alachua County that iNaturalist's community had already identified, taken in 2025 and 2026, this recognizer named the species for about 91 photos in 100." It may add that such photos are easier than a photo taken in passing. It may not compare itself with iNaturalist's model.

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

`tools/eval/checks.py` ran 32 checks: 25 passed, 0 failed, 6 are facts to know, and 1 wait for a file that is not published yet. The full table is in [`docs/eval/checks.md`](eval/checks.md).

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

Inputs of this run: `pub/data-alachua` at `8cd2b174d77b`; `pub/lab-bioclip-b16` at `8390d0006a34`; `pub/lab-bioclip2-l14` at `f552a63fbd5e`; `pub/lab-bioclip25-h14` at `40532989b3a9`; `pub/lab-bioclip25-mobile-fastvit` at `3c8cc3bd2386`; `pub/lab-clip-b32` at `721281767c8b`; `pub/lab-mobileclip2-s0` at `3da256a7dad0`; `pub/lab-siglip2-b16` at `5efd3b247595`; `pub/lab-tinyclip-39m-16` at `d68a5fc88c30`; `pub/lab-tinyclip-40m-32` at `6d8c0ecbd92e`; `pub/lab-tinyclip-61m-32` at `bd62f0f43f8c`; `pub/lab-tinyclip-8m-16` at `af03032158c3`.
