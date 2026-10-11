# Evaluation: what the recognizers get right, and how we know

_This file is written by `tools/eval/report.py` from the JSON files under `docs/eval/`, which the scripts in `tools/eval/` produce. Do not edit it by hand. The commands are at the end._

## What was measured

The question is how often a model names the right species, and the right kind of eye, for a photo of a living thing taken in Alachua County, Florida.

- **The photos.** The evaluation set `alachua-2025` holds 6,000 research-grade iNaturalist photos dated 2025-01-01 to 2026-09-29, one photo an observation (`data/eval/alachua-2025/SUMMARY.md`). A hash of the record's id puts 1803 photos in `val` and 4197 in `test`. Every setting is chosen on `val`. Every number below comes from `test`.
- **The list.** A model answers with one of the 5911 species recorded in the county through 2024 (`data/regions/us-fl-alachua/species.json`). The list also gives each species' records by calendar month, and its kind of eye.
- **Scoring against sentences.** Each species becomes a row made by the model's text half from sentences that hold its name. A photo's score for a species is the cosine between the photo's vector and that row. Three kinds of rows were tried: the scientific name, the English name, and the taxonomy followed by the English name in the form BioCLIP was trained on.
- **The prior.** The place-and-season prior adds `alpha * log(share)` to a species' score, where `share` is the species' part of all records of that calendar month. A month's weight for a species is its records in that month, plus `lam` times a twelfth of its yearly records, plus `c`. This is the arithmetic of `tools/fusion/fuse.py`, with the smoothing written into the table's monthly weights.
- **Intervals.** Each share is followed by a 95% percentile interval from 2000 bootstrap resamples over photos (seed 20261011). The intervals describe the luck of which photos were drawn. They say nothing about photos of another kind.
- **People, pets, livestock and rooms.** The wildlife photos hold no people, no photos with nothing alive in them and almost no pets. The extra set `coco-kinds` (`data/extra/coco-kinds/SUMMARY.md`) holds 10,240 photos from COCO 2017 filed as `person`, `cat`, `dog`, `deer` (horses, cows and sheep) and `none` (rooms and objects). `tools/eval/kinds.py` cuts COCO's own training rows by a hash of the row id into a part for fitting kind rows (two thirds) and a part that joins the wildlife `val` photos whenever a setting of the kind decision is chosen (one third); COCO's own validation rows are the test rows and are only reported. A COCO photo has no date that means a season, so each is given a calendar month by a hash of its id. The number a kind decision is tuned on is the mean of the share right on the wildlife tuning photos and of the mean share right over the extra set's five kinds, because nobody knows what share of a phone's photos are of people or of rooms.

## The main table

Test split, 4197 photos. For each model the species rows are the label set that did best on `val`. The kind of eye is given twice: from the model's own kind phrases (`labels/kinds.json`, seventeen rows that include `person` and `none`), and from the kind of the top species with the prior.

| Model | Kind from phrases | Kind from top species | Species rows from | Top-1 | Top-5 | Top-1 with prior | Top-5 with prior |
|---|---:|---:|---|---:|---:|---:|---:|
| bioclip25-h14 | 70.0% (68.7 to 71.4) | 98.1% (97.6 to 98.5) | scientific name | 92.9% (92.1 to 93.7) | 97.3% (96.8 to 97.8) | 93.4% (92.7 to 94.2) | 97.7% (97.2 to 98.1) |
| bioclip2-l14 | 76.1% (74.8 to 77.4) | 98.3% (97.9 to 98.7) | scientific name | 90.3% (89.4 to 91.3) | 96.8% (96.2 to 97.3) | 92.4% (91.6 to 93.2) | 97.5% (97.0 to 97.9) |
| bioclip-b16 | 45.5% (44.0 to 47.0) | 92.2% (91.4 to 93.0) | taxonomy and English name | 62.3% (60.7 to 63.8) | 81.6% (80.4 to 82.8) | 69.5% (68.0 to 71.0) | 86.1% (85.1 to 87.2) |
| tinyclip-39m-16 | 77.6% (76.3 to 78.8) | 84.2% (83.1 to 85.4) | English name | 21.7% (20.5 to 22.9) | 38.7% (37.2 to 40.2) | 35.3% (33.8 to 36.7) | 55.1% (53.6 to 56.6) |
| tinyclip-8m-16 | 72.0% (70.6 to 73.5) | 78.2% (77.0 to 79.4) | English name | 15.4% (14.3 to 16.5) | 28.2% (26.9 to 29.5) | 26.4% (25.1 to 27.7) | 44.5% (43.0 to 46.0) |
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
- **Names that differ between GBIF and iNaturalist.** 236 test photos are of species whose GBIF name differs from the name iNaturalist uses. They were found from `inat.json`, which gives each GBIF species key the name iNaturalist most often uses for it. Top-1 without the prior is 93.2% (89.8 to 96.2) on those photos and 90.2% (89.2 to 91.1) on the rest, so scoring against GBIF's names did not lower the result on these photos.
- **Mistakes.** Of 283 wrong answers for species in the list, 81 named a species of the same genus and 126 one of the same family. The table of commonest mistakes, with links to the observations, is in [`docs/eval/model-bioclip2-l14.md`](eval/model-bioclip2-l14.md).

BioCLIP 2.5 (ViT-H/14) reaches 92.9% (92.1 to 93.7) without the prior and 93.4% (92.7 to 94.2) with it. Its model card does not give the date of its training data, so it cannot be shown that the test photos are new to it. That number is reported with this caveat and is kept out of any claim the app makes.

## The models small enough for a phone, scored against sentences

| Model | File the phone downloads | Kind from phrases | Kind from summed species | Top-1 | Top-1 with prior | Top-5 with prior | Top-1 with prior, WASM int8 vectors | WASM against original (points) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| tinyclip-39m-16 | 41.0 MB | 77.6% (76.3 to 78.8) | 85.9% (84.9 to 87.0) | 21.7% (20.5 to 22.9) | 35.3% (33.8 to 36.7) | 55.1% (53.6 to 56.6) | 34.8% (33.3 to 36.2) | -0.5 (-0.9 to -0.1) |
| tinyclip-8m-16 | 9.6 MB | 72.0% (70.6 to 73.5) | 80.2% (79.0 to 81.4) | 15.4% (14.3 to 16.5) | 26.4% (25.1 to 27.7) | 44.5% (43.0 to 46.0) | 26.1% (24.8 to 27.4) | -0.3 (-0.7 to +0.2) |

Scored against sentences, the small general models name the species in about a quarter to a third of test photos with the prior. That is too weak to show a species name on its own. Their kind of eye from phrases is right in about three photos in four. The vectors a phone computes (WASM, int8) cost about half a point of species top-1 against the original model's vectors; every quantized set is compared in [`docs/eval/variants.md`](eval/variants.md).

## Sentence rows with the prior, as the page would use them

No head was fitted here. The models' own sentence rows were given the prior, the calibration and the page's combination with the kind phrases, with every setting chosen on the whole of `val`. These are the slots that can ship before any training photo exists.

Species top-1 with the prior on the test photos (the pocket models on the vectors a phone computes):

| Species head | tinyclip-39m-16 | tinyclip-8m-16 | bioclip2-l14 |
|---|---:|---:|---:|
| sentences | 35.3% (33.9 to 36.8) | 26.5% (25.1 to 27.8) | 92.5% (91.6 to 93.2) |

Kind of eye right on the test photos:

| Kind of eye from | tinyclip-39m-16 | tinyclip-8m-16 | bioclip2-l14 |
|---|---:|---:|---:|
| kind phrases | 77.3% (76.0 to 78.7) | 72.4% (71.0 to 73.8) | 76.1% (74.8 to 77.4) |
| summed species probabilities | 80.7% (79.5 to 81.9) | 78.2% (77.0 to 79.5) | 98.3% (97.9 to 98.7) |
| the page's combination of kind phrases and the species list | 81.4% (80.2 to 82.6) | 77.3% (76.0 to 78.6) | 98.3% (97.8 to 98.6) |

The kind decision on the wildlife test photos and on the extra set's test photos (people, rooms with nothing alive, cats, dogs, grazing animals). The second row of each model shows what tuning on wildlife photos alone, as the first export did, would have chosen:

| Model |  | Kinds head and settings | Kind right, wildlife test | Kind right, extra test | `person` | `none` | `cat` | `dog` | `deer` |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| tinyclip-39m-16 | chosen | kind phrases; rule `mix`, t_kind 100, w_kind 0.5 | 81.4% (80.2 to 82.6) | 80.1% (77.8 to 82.3) | 94.8% | 62.8% | 90.9% | 88.9% | 87.0% |
| tinyclip-39m-16 | what the wildlife photos alone would choose | kind phrases; rule `product`, t_kind 20, w_kind 0.5 | 83.7% (82.6 to 84.8) | 22.1% (19.8 to 24.4) | 46.8% | 2.4% | 54.5% | 0.0% | 16.5% |
| tinyclip-8m-16 | chosen | kind phrases; rule `mix`, t_kind 100, w_kind 0.5 | 77.3% (76.0 to 78.6) | 83.2% (81.0 to 85.2) | 90.8% | 78.6% | 92.2% | 81.0% | 76.5% |
| tinyclip-8m-16 | what the wildlife photos alone would choose | kind phrases; rule `product`, t_kind 20, w_kind 0.5 | 79.4% (78.2 to 80.6) | 26.2% (23.7 to 28.8) | 27.0% | 16.4% | 79.2% | 0.0% | 37.0% |
| bioclip2-l14 | chosen | kind phrases; rule `mix`, t_kind 20, w_kind 0.7 | 98.3% (97.8 to 98.6) | – | – | – | – | – | – |
| bioclip2-l14 | what the wildlife photos alone would choose | kind phrases; rule `mix`, t_kind 20, w_kind 0.7 | 98.3% (97.8 to 98.6) | – | – | – | – | – | – |

- The extra set's vectors (people, pets, livestock, rooms) were not published for this model when this ran, so the kind decision was tuned on wildlife photos alone and says nothing about a person or an empty room.

Every head, its settings, the reliability tables and the breakdown by fitting photos are in [`docs/eval/study2-sentences.md`](eval/study2-sentences.md).

## Trained heads (Study 2): the machinery, proven on a stand-in

This run is a stand-in that proves the machinery. No training vectors were published when it ran, so two thirds of the `val` photos were used to fit the heads and the last third to choose settings. With about two fitting photos a species, these numbers say little about what the real training set (up to sixty photos a species) will give. They are here to show that every step runs and to be replaced.

Species top-1 with the prior on the test photos (the pocket models on the vectors a phone computes):

| Species head | tinyclip-39m-16 | tinyclip-8m-16 | bioclip2-l14 |
|---|---:|---:|---:|
| sentences | 35.1% (33.7 to 36.6) | 25.9% (24.6 to 27.2) | 92.4% (91.6 to 93.2) |
| prototypes | 30.1% (28.7 to 31.5) | 24.0% (22.7 to 25.3) | 61.1% (59.6 to 62.6) |
| prototypes + sentences | 36.4% (34.9 to 37.8) | 27.3% (25.9 to 28.7) | 91.7% (90.9 to 92.6) |
| discriminant | 32.6% (31.2 to 34.0) | 24.9% (23.6 to 26.3) | 60.7% (59.2 to 62.2) |
| discriminant + sentences | 34.6% (33.2 to 36.1) | 25.3% (24.0 to 26.6) | 90.8% (90.0 to 91.7) |
| mapped to BioCLIP 2 | 35.3% (33.8 to 36.8) | 24.3% (23.0 to 25.6) | – |

Kind of eye right on the test photos:

| Kind of eye from | tinyclip-39m-16 | tinyclip-8m-16 | bioclip2-l14 |
|---|---:|---:|---:|
| kind phrases | 77.3% (76.0 to 78.7) | 72.4% (71.0 to 73.8) | 76.1% (74.8 to 77.4) |
| trained on the fitting photos | 84.4% (83.3 to 85.5) | 77.1% (75.8 to 78.3) | 94.3% (93.7 to 95.0) |
| summed species probabilities | 86.5% (85.5 to 87.5) | 73.7% (72.4 to 75.0) | 98.5% (98.0 to 98.8) |
| the page's combination of kind rows fitted on the fitting photos and the extra set | 87.2% (86.2 to 88.2) | 79.5% (78.3 to 80.7) | – |
| trained rows, with the sentence rows for `person` and `none` kept beside them | – | – | 94.0% (93.3 to 94.7) |
| the page's combination of kind phrases and the species list | – | – | 98.6% (98.2 to 98.9) |

The kind decision on the wildlife test photos and on the extra set's test photos (people, rooms with nothing alive, cats, dogs, grazing animals). The second row of each model shows what tuning on wildlife photos alone, as the first export did, would have chosen:

| Model |  | Kinds head and settings | Kind right, wildlife test | Kind right, extra test | `person` | `none` | `cat` | `dog` | `deer` |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| tinyclip-39m-16 | chosen | kind rows fitted on the fitting photos and the extra set (a kind's photos weighted by the inverse square root of their number); rule `mix`, t_kind 0.5, w_kind 0.7 | 87.2% (86.2 to 88.2) | 98.2% (97.3 to 98.8) | 99.5% | 98.6% | 92.2% | 95.2% | 97.5% |
| tinyclip-39m-16 | what the wildlife photos alone would choose | kind rows fitted on the fitting photos and the extra set (a kind's photos weighted by the inverse square root of their number); rule `mix`, t_kind 0.5, w_kind 0.7 | 87.2% (86.2 to 88.2) | 98.2% (97.3 to 98.8) | 99.5% | 98.6% | 92.2% | 95.2% | 97.5% |
| tinyclip-8m-16 | chosen | kind rows fitted on the fitting photos and the extra set (every kind counts the same); rule `mix`, t_kind 0.5, w_kind 0.5 | 79.5% (78.3 to 80.7) | 96.2% (95.2 to 97.3) | 98.2% | 97.4% | 89.6% | 88.9% | 94.0% |
| tinyclip-8m-16 | what the wildlife photos alone would choose | kind rows fitted on the fitting photos and the extra set (every kind counts the same); rule `product`, t_kind 0.5, w_kind 0.5 | 79.8% (78.5 to 81.0) | 91.7% (90.0 to 93.2) | 98.0% | 98.0% | 89.6% | 3.2% | 92.0% |
| bioclip2-l14 | chosen | kind phrases; rule `product`, t_kind 20, w_kind 0.5 | 98.6% (98.2 to 98.9) | – | – | – | – | – | – |
| bioclip2-l14 | what the wildlife photos alone would choose | kind phrases; rule `product`, t_kind 20, w_kind 0.5 | 98.6% (98.2 to 98.9) | – | – | – | – | – | – |

- The extra set's vectors (people, pets, livestock, rooms) were not published for this model when this ran, so the kind decision was tuned on wildlife photos alone and says nothing about a person or an empty room.
- The extra set's vectors were not published for this model when this ran, so no kind row could be fitted for `person` or `none`. The sentence rows for the two are kept beside the trained rows, with a bias set on the tuning photos so that at most 0.5% of them are called `person` or `none`. How often a person is then called a person is unmeasured.
- The map into BioCLIP 2's space was fitted on 1226 pairs of vectors of the same photos.

Every head, its settings, the reliability tables and the breakdown by fitting photos are in [`docs/eval/study2-val.md`](eval/study2-val.md).

## What the page would show

Each slot below was written by `tools/eval/export_heads.py` in the layout of `models/<slot>/` and then scored by `tools/eval/shipped.py`, which reads the slot's own files as the page does and sends every photo through `tools/fusion/fuse.py`. The two thresholds were set on the tuning photos so that a named species, and the three offered species, were right at least nine times in ten there. Slots whose name begins with `val-` hold stand-in heads. A name that ends in `-wasm-int8` or the like is the same slot scored on other vectors of the same photos (the larger model's int8 file as the browser runs it). The kinds head, its temperature, its weight and the rule (`mix` or `product`, both in the page since build 7) were chosen by Study 2 as described above.

| Slot | Kind right | Top species right | Species named (share, threshold) | Named species right | Three offered (share, threshold) | Offer holds the species | Kind only | Kind right when kind only |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `live-pocket` | 83.7% (82.5 to 84.8) | 34.9% (33.5 to 36.4) | 15.2% at 0.4 | 93.4% (91.4 to 95.2) | 3.3% at 0.53 | 85.5% (79.7 to 91.3) | 81.5% | 80.2% (78.8 to 81.5) |
| `sentences-bioclip2-l14` | 98.3% (97.8 to 98.6) | 92.5% (91.6 to 93.2) | 99.5% at 0.05 | 92.8% (92.1 to 93.6) | 0.0% at never | – | 0.5% | 30.4% (13.0 to 47.8) |
| `sentences-tinyclip-39m-16` | 81.4% (80.2 to 82.6) | 35.3% (33.9 to 36.8) | 17.3% at 0.27 | 89.7% (87.5 to 91.9) | 0.0% at never | – | 82.7% | 77.8% (76.4 to 79.2) |
| `sentences-tinyclip-8m-16` | 77.3% (76.0 to 78.6) | 26.4% (25.1 to 27.8) | 9.4% at 0.56 | 89.1% (86.0 to 92.1) | 4.9% at 0.63 | 81.0% (76.1 to 86.3) | 85.7% | 74.0% (72.5 to 75.4) |
| `val-bioclip2-l14` | 98.6% (98.2 to 98.9) | 91.7% (90.9 to 92.6) | 99.5% at 0.05 | 92.2% (91.3 to 92.9) | 0.0% at never | – | 0.5% | 52.4% (28.6 to 71.4) |
| `val-tinyclip-39m-16` | 87.3% (86.3 to 88.3) | 36.3% (34.9 to 37.8) | 14.2% at 0.9 | 92.0% (89.6 to 94.0) | 7.3% at 0.94 | 90.3% (86.7 to 93.5) | 78.5% | 84.3% (83.1 to 85.6) |
| `val-tinyclip-8m-16` | 79.5% (78.3 to 80.7) | 25.3% (24.0 to 26.6) | 0.0% at never | – | 15.8% at 0.24 | 82.9% (79.9 to 85.7) | 84.2% | 76.1% (74.7 to 77.5) |

**Not sure is an answer.** Under `fusion.kind_at` the page asserts no kind, says that it is not sure and offers its three likeliest kinds. `tools/eval/shipped.py` sets the level through `fuse.py` as the lowest one from which an asserted kind was right at least 95 times in 100 on the wildlife tuning photos and, taken by itself, on the tuning third of the extra set. The table gives what then happens on the wildlife test photos and on the extra set's test photos. A slot whose third column says `no` was tuned before its model's vectors of the extra set were published: its level and its settings have never been asked about a person or an empty room.

| Slot | kind_at | Tuned with the extra set | Kind right, wildlife test | Kind asserted | Right when asserted | True kind among the three when not sure | Kind right, extra test | Kind asserted | Right when asserted | True kind among the three when not sure | A species named on an extra photo |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `live-pocket` | 0.88 | yes | 83.7% (82.5 to 84.8) | 38.4% (37.0 to 40.0) | 99.0% (98.5 to 99.4) | 95.6% (94.8 to 96.4) | 70.1% (67.3 to 72.6) | 3.7% (2.7 to 4.8) | 97.8% (93.5 to 100.0) | 81.7% (79.5 to 83.8) | 0.9% (0.4 to 1.5) |
| `sentences-bioclip2-l14` | 0.20 | no | 98.3% (97.8 to 98.6) | 99.6% (99.5 to 99.8) | 98.5% (98.1 to 98.9) | 86.7% (66.7 to 100.0) | – | – | – | – | – |
| `sentences-tinyclip-39m-16` | 0.76 | yes | 81.4% (80.2 to 82.6) | 48.8% (47.3 to 50.4) | 97.7% (97.0 to 98.3) | 93.4% (92.4 to 94.5) | 80.1% (77.8 to 82.3) | 28.9% (26.4 to 31.4) | 97.8% (96.1 to 99.2) | 82.9% (80.2 to 85.4) | 1.2% (0.7 to 1.8) |
| `sentences-tinyclip-8m-16` | 0.80 | yes | 77.3% (76.0 to 78.6) | 42.5% (41.0 to 44.1) | 97.4% (96.6 to 98.2) | 91.4% (90.3 to 92.5) | 83.2% (81.0 to 85.2) | 28.1% (25.7 to 30.6) | 96.9% (94.8 to 98.6) | 90.2% (88.3 to 92.2) | 1.1% (0.6 to 1.6) |
| `val-bioclip2-l14` | 0.20 | no | 98.6% (98.2 to 98.9) | 100.0% (99.9 to 100.0) | 98.6% (98.2 to 99.0) | 50.0% (0.0 to 100.0) | – | – | – | – | – |
| `val-tinyclip-39m-16` | 0.49 | yes | 87.3% (86.3 to 88.3) | 79.9% (78.7 to 81.1) | 95.1% (94.4 to 95.9) | 89.9% (87.8 to 91.9) | 98.2% (97.3 to 98.8) | 95.7% (94.5 to 96.9) | 99.2% (98.7 to 99.7) | 94.3% (86.8 to 100.0) | 6.2% (4.9 to 7.7) |
| `val-tinyclip-8m-16` | 0.53 | yes | 79.5% (78.3 to 80.7) | 52.9% (51.4 to 54.4) | 95.4% (94.5 to 96.2) | 88.6% (87.2 to 90.0) | 96.2% (95.2 to 97.3) | 70.5% (68.0 to 73.1) | 99.3% (98.7 to 99.8) | 94.3% (91.8 to 96.5) | 0.0% (0.0 to 0.0) |

A stricter bar for naming is available. The table gives, for a named species that has to be right at least 90, 95 or 98 times in 100 on `val`, the threshold that `val` gives and what then happens on the test photos. For each bar the offer threshold was set again on `val`, for the photos left without a name, so that the three offered species hold the right one nine times in ten.

| Slot | Named species right at least | name_at | Photos named | Named species right | offer_at | Photos offered three | Offer holds the species | Kind only |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `live-pocket` | 90 in 100 | 0.40 | 15.2% (14.1 to 16.4) | 93.4% (91.4 to 95.2) | 0.53 | 3.3% (2.8 to 3.9) | 85.5% (79.7 to 91.3) | 81.5% (80.3 to 82.7) |
| `live-pocket` | 95 in 100 | 0.46 | 13.1% (12.1 to 14.1) | 95.6% (94.0 to 97.3) | 0.57 | 3.1% (2.5 to 3.6) | 91.5% (86.1 to 96.1) | 83.8% (82.7 to 84.9) |
| `live-pocket` | 98 in 100 | 0.85 | 1.8% (1.4 to 2.2) | 100.0% (100.0 to 100.0) | 0.38 | 24.0% (22.7 to 25.4) | 87.5% (85.4 to 89.6) | 74.2% (72.8 to 75.5) |
| `sentences-bioclip2-l14` | 90 in 100 | 0.05 | 99.5% (99.2 to 99.7) | 92.8% (92.1 to 93.6) | never | 0.0% (0.0 to 0.0) | – | 0.5% (0.3 to 0.8) |
| `sentences-bioclip2-l14` | 95 in 100 | 0.44 | 95.7% (95.0 to 96.3) | 95.1% (94.4 to 95.7) | never | 0.0% (0.0 to 0.0) | – | 4.3% (3.7 to 5.0) |
| `sentences-bioclip2-l14` | 98 in 100 | 0.78 | 84.7% (83.5 to 85.8) | 98.0% (97.5 to 98.4) | 0.66 | 11.7% (10.8 to 12.7) | 91.8% (89.4 to 94.1) | 3.6% (3.0 to 4.2) |
| `sentences-tinyclip-39m-16` | 90 in 100 | 0.27 | 17.3% (16.2 to 18.5) | 89.7% (87.5 to 91.9) | never | 0.0% (0.0 to 0.0) | – | 82.7% (81.5 to 83.8) |
| `sentences-tinyclip-39m-16` | 95 in 100 | 0.35 | 13.2% (12.1 to 14.2) | 95.3% (93.5 to 97.1) | 0.48 | 2.4% (1.9 to 2.9) | 89.0% (83.0 to 95.0) | 84.5% (83.4 to 85.6) |
| `sentences-tinyclip-39m-16` | 98 in 100 | 0.38 | 12.4% (11.4 to 13.4) | 96.0% (94.2 to 97.5) | 0.48 | 2.8% (2.3 to 3.3) | 90.6% (85.5 to 95.7) | 84.8% (83.7 to 85.9) |
| `sentences-tinyclip-8m-16` | 90 in 100 | 0.56 | 9.4% (8.5 to 10.2) | 89.1% (86.0 to 92.1) | 0.63 | 4.9% (4.3 to 5.6) | 81.0% (76.1 to 86.3) | 85.7% (84.7 to 86.8) |
| `sentences-tinyclip-8m-16` | 95 in 100 | 0.71 | 5.1% (4.5 to 5.8) | 95.8% (93.1 to 98.2) | 0.62 | 9.4% (8.5 to 10.3) | 85.0% (81.5 to 88.6) | 85.5% (84.4 to 86.5) |
| `sentences-tinyclip-8m-16` | 98 in 100 | 0.87 | 2.0% (1.6 to 2.5) | 98.8% (96.4 to 100.0) | 0.59 | 14.0% (13.0 to 15.1) | 86.2% (83.5 to 88.9) | 84.0% (82.9 to 85.1) |

The text for each slot, with what it needs from the page, is in [`docs/eval/shipped.md`](eval/shipped.md).

## The larger model on the device

The species service has no free server to live on, so BioCLIP 2's image encoder is offered as a download and runs on the device. The laboratory made int8 files of it and ran each through onnxruntime-web's WASM build on 24 test photos (every k-th test row). `tools/eval/variant.py` sent those vectors, and the original model's vectors of the same photos, through `fuse.py` with the slot `sentences-bioclip2-l14` and its thresholds (name_at 0.78, offer_at 0.66, the levels set on `val` for a named species right 98 times in 100). Every difference is paired over the same photos. No threshold was set again: the laboratory's vectors hold test photos only, and a threshold may be set on `val` alone.

| Vectors | Cosine to the original (1st percentile) | Top species right, original vectors | Top species right, these vectors | Paired difference (points) | First five | Kind right | Species named, original | Species named, these | Named species right, these | Same top species as the original |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `bioclip2-l14-wasm-fp16` | 1.0000 (1.0000) | 87.5% (70.8 to 100.0) | 87.5% (70.8 to 100.0) | +0.0 (+0.0 to +0.0) | 91.7% (79.2 to 100.0) | 95.8% (87.5 to 100.0) | 70.8% (50.0 to 87.5) | 70.8% (50.0 to 87.5) | 100.0% (100.0 to 100.0) | 100.0% (100.0 to 100.0) |
| `bioclip2-l14-wasm-hybrid-fc2-w8` | 0.9988 (0.9962) | 94.1% (91.2 to 96.6) | 93.8% (90.9 to 96.2) | -0.3 (-0.9 to +0.0) | 96.9% (94.7 to 98.8) | 98.4% (96.9 to 99.7) | 88.8% (85.0 to 91.9) | 87.8% (84.1 to 91.2) | 97.9% (96.1 to 99.3) | 99.1% (97.8 to 100.0) |
| `bioclip2-l14-wasm-int8-per-channel` | 0.9932 (0.9713) | 94.1% (91.2 to 96.6) | 93.1% (90.0 to 95.6) | -0.9 (-2.8 to +0.9) | 98.1% (96.6 to 99.4) | 98.4% (96.9 to 99.7) | 88.8% (85.0 to 91.9) | 87.8% (84.1 to 91.2) | 97.9% (96.1 to 99.3) | 96.2% (94.1 to 98.1) |
| `bioclip2-l14-wasm-uint8-per-channel` | 0.9934 (0.9740) | 94.1% (91.2 to 96.6) | 93.4% (90.3 to 95.9) | -0.6 (-2.2 to +0.9) | 97.2% (95.3 to 98.8) | 98.1% (96.6 to 99.4) | 88.8% (85.0 to 91.9) | 88.4% (85.0 to 91.9) | 97.9% (96.1 to 99.3) | 96.9% (95.0 to 98.4) |
| `bioclip2-l14-wasm-w4-block32` | 0.9929 (0.9788) | 94.1% (91.2 to 96.6) | 94.4% (91.6 to 96.9) | +0.3 (-0.9 to +1.9) | 97.5% (95.6 to 99.1) | 98.4% (96.9 to 99.7) | 88.8% (85.0 to 91.9) | 87.5% (83.8 to 90.9) | 97.9% (96.1 to 99.3) | 97.2% (95.3 to 98.8) |
| `bioclip2-l14-wasm-w8-float` | 0.9999 (0.9996) | 94.1% (91.2 to 96.6) | 94.1% (91.2 to 96.6) | +0.0 (+0.0 to +0.0) | 97.5% (95.6 to 99.1) | 98.4% (96.9 to 99.7) | 88.8% (85.0 to 91.9) | 88.8% (85.0 to 91.9) | 97.9% (96.1 to 99.3) | 100.0% (100.0 to 100.0) |

With 24 photos an interval is several points wide, so these figures can show a large loss and cannot show a small one. The sources of the vectors: `bioclip2-l14-wasm-fp16`: runs/lab/25-device-w8-float/wasm_fp16.f16.npy on the ci branch (onnxruntime-web 1.30.0, WASM build, run 25 of the laboratory); `bioclip2-l14-wasm-hybrid-fc2-w8`: runs/lab/25-device-hybrid-fc2-w8/wasm_hybrid-fc2-w8.f16.npy on the ci branch (onnxruntime-web 1.30.0, WASM build, run 25 of the laboratory); `bioclip2-l14-wasm-int8-per-channel`: runs/lab/25-device-int8-per-channel/wasm_int8-per-channel.f16.npy on the ci branch (onnxruntime-web 1.30.0, WASM build, run 25 of the laboratory); `bioclip2-l14-wasm-uint8-per-channel`: runs/lab/25-device-uint8-per-channel/wasm_uint8-per-channel.f16.npy on the ci branch (onnxruntime-web 1.30.0, WASM build, run 25 of the laboratory); `bioclip2-l14-wasm-w4-block32`: runs/lab/28-device-w4-block32/wasm_w4-block32.f16.npy on the ci branch (onnxruntime-web 1.30.0, WASM build, run 28 of the laboratory); `bioclip2-l14-wasm-w8-float`: runs/lab/25-device-w8-float/wasm_w8-float.f16.npy on the ci branch (onnxruntime-web 1.30.0, WASM build, run 25 of the laboratory).

## Decisions

- **The pocket model.** On the vectors a phone computes, and scored against sentences, TinyCLIP 39M/16 gets the kind of eye from phrases right for 77.3% (76.0 to 78.7) and the species with the prior for 34.8% (33.3 to 36.2); TinyCLIP 8M/16 gets 72.4% (71.0 to 73.8) and 26.1% (24.8 to 27.4). The first is a 41.0 MB download and took about 333 ms a photo in the laboratory's one-thread WASM run; the second is 9.6 MB and took about 100 ms a photo. Heads fitted on the real training photos have not been measured, because the training vectors were not published when this report was written. They decide this choice: a trained head may close the gap between the two models or widen it. What can ship before then is each model's sentence rows with the prior. Scored as the page would, the 39M slot gets the kind of eye right for 81.4% (80.2 to 82.6), names a species for 17.3% of test photos and is right for 89.7% (87.5 to 91.9) of those names; the 8M slot gets 77.3% (76.0 to 78.6), 9.4% and 89.1% (86.0 to 92.1). Recommendation until trained heads are measured: TinyCLIP 39M/16, which is ahead on the kind of eye and on the share of photos it can name by more than the intervals, and TinyCLIP 8M/16 only if the download has to stay near 10 MB.
- **The pocket model, by the rule set down beforehand** (`tools/eval/decide.py`). TinyCLIP 8M/16 ships unless TinyCLIP 39M/16 is ahead on the kind of eye, as the page would decide it, by a paired difference whose 95% interval lies wholly above zero. The measure is the mean of the share right on the wildlife test photos and on the extra set's test photos. The comparison is made on the test photos: a choice among two candidates by a rule fixed beforehand, which bends the chosen slot's test figures very little, and which is the one decision here that the test photos took part in. Compared: the slots `sentences-tinyclip-39m-16` and `sentences-tinyclip-8m-16`, scored through `fuse.py` on the same photos. On the mean of the share right on the wildlife test photos and on the extra set's test photos, TinyCLIP 39M/16 is ahead of TinyCLIP 8M/16 by +0.5 points (-0.7 to +1.7), paired over the same photos. The interval reaches zero, so the smaller model ships: it is a quarter of the download and about a third of the time a photo. The slot to ship is `sentences-tinyclip-8m-16`, published as the branch `pub/heads-sentences-tinyclip-8m-16`. This choice is provisional: it was made from sentence-made slots, before heads fitted on the training photos were measured. `tools/eval/decide.py` makes it again from the trained slots when they exist.

| Photos | Measure | TinyCLIP 39M/16 | TinyCLIP 8M/16 | Paired difference (points) |
|---|---|---:|---:|---:|
| wildlife test | kind of eye right | 81.4% | 77.3% | +4.1 (+3.1 to +5.1) |
| wildlife test | kind asserted and right | 47.7% | 41.4% | +6.3 (+5.0 to +7.4) |
| wildlife test | kind asserted and wrong | 1.1% | 1.1% | +0.0 (-0.3 to +0.4) |
| wildlife test | a right species name shown | 15.5% | 8.4% | +7.2 (+6.4 to +8.1) |
| wildlife test | a species name shown | 17.3% | 9.4% | +7.9 (+7.0 to +8.9) |
| extra test | kind of eye right | 80.1% | 83.2% | -3.1 (-5.2 to -1.0) |
| extra test | kind asserted and right | 28.3% | 27.3% | +1.1 (-1.7 to +3.9) |
| extra test | kind asserted and wrong | 0.7% | 0.9% | -0.2 (-0.8 to +0.2) |
| extra test | a species name shown | 1.2% | 1.1% | +0.2 (-0.4 to +0.8) |

- **The server.** BioCLIP 2 (ViT-L/14) with rows made from scientific names, all 5911 species of the list, and the prior (alpha 1.2 at temperature 100, smoothing lam 2 and c 1): top-1 92.4% (91.6 to 93.2), top-5 97.5% (97.0 to 97.9), and the kind of eye from summed species probabilities right for 98.4% (98.0 to 98.7). The kind of eye should come from the species list and the kind phrases should count for little, because this model's kind phrases alone are right for 76.1% (74.8 to 77.4). BioCLIP 2.5 measures 93.4% (92.7 to 94.2) with the prior, a paired difference of +1.0 (+0.4 to +1.7) points from BioCLIP 2 on the same photos. The laboratory's runs embedded 1.2 photos a second with BioCLIP 2 and 0.6 with BioCLIP 2.5 on build machines without a graphics card. The date of BioCLIP 2.5's training data is undocumented, so it cannot be shown that the test photos are new to it, and no number for it can be defended in public. BioCLIP 2 is the one to run.
- **The server's files.** The slot `sentences-bioclip2-l14` holds these rows and a table whose monthly weights carry the smoothing (lam 2, c 1), with alpha_prior 1, t_species 100, rule `mix`, t_kind 20 and w_kind 0.7, all chosen on `val`. Scored as the page would, it gets the kind of eye right for 98.3% (97.8 to 98.6) of test photos and the species for 92.5% (91.6 to 93.2). Its settings differ a little from the line above because Study 2 searches a finer grid of prior weights; the two results agree within their intervals.
- **When the server should name a species.** The nine-in-ten rule lets BioCLIP 2 name a species for nearly every photo, since it is right more often than that overall. A stricter bar suits a name shown to a person: with name_at 0.78, set on `val` for 98 in 100, the slot `sentences-bioclip2-l14` names a species for 84.7% (83.5 to 85.8) of test photos and is right for 98.0% (97.5 to 98.4) of those names; with offer_at 0.66 it offers three species for 11.7% (10.8 to 12.7) and they hold the right one for 91.8% (89.4 to 94.1), and 3.6% (3.0 to 4.2) get a kind of eye only. The other bars are in the table under "What the page would show".
- **What the app may say about the server.** A sentence the measurements support: "On photos from Alachua County that iNaturalist's community had already identified, taken in 2025 and 2026, this recognizer named the species for about 91 photos in 100." It may add that such photos are easier than a photo taken in passing. It may not compare itself with iNaturalist's model.
- **The slot that is live.** `live-pocket` in the tables is `models/pocket` as it stands on `main`: TinyCLIP 39M/16, sentence rows, and the interim settings chosen by hand (rule `product`, t_kind 100, w_kind 0.3). Through `fuse.py` it gets the kind of eye right for 83.7% (82.5 to 84.8) of the wildlife test photos and names a species for 15.2%, rightly for 93.4% (91.4 to 95.2) of those names. For these settings `kind_at` comes out as 0.88: the page then asserts a kind for 38.4% (37.0 to 40.0) of the wildlife test photos and is right for 99.0% (98.5 to 99.4) of those, and where it is not sure the true kind is among its three likeliest for 95.6% (94.8 to 96.4). On the extra set's test photos (people, cats, dogs, grazing animals, rooms) it gets the kind right for 70.1% (67.3 to 72.6), asserts for 3.7% (2.7 to 4.8) and is right for 97.8% (93.5 to 100.0) of those.
- **The larger model on the device.** The head files are the slot `sentences-bioclip2-l14` with name_at 0.78 and offer_at 0.66. On the laboratory's 320 test photos the int8 vectors computed by the browser's WASM runtime change the top species for few photos (table above), and a named species stays right as often as with the original vectors, so the thresholds are kept. They could not be set again on int8 vectors, since no `val` photo has any. `tools/eval/naturalist.py` writes the files for `models/naturalist`; the `vision` block of its manifest is left for the laboratory's `parts.json`.
- **The same comparison on slots whose kind rows are fitted on photos.** The sentence slots above are the weakest form of either model on people and rooms. The stand-in slots `val-tinyclip-39m-16` and `val-tinyclip-8m-16` carry kind rows fitted on wildlife photos and on the extra set's fitting part, which is the form the trained slots will have. On them TinyCLIP 39M/16 is ahead of TinyCLIP 8M/16 by +4.9 (+4.2 to +5.6) points on the mean of the share right on the wildlife test photos and on the extra set's test photos, paired over the same photos, and the rule's answer there is `tinyclip-39m-16`. This second look was added after the first answer was seen, so it is evidence and no part of the rule; the trained slots are decided by the rule as written.

| Photos | Measure | TinyCLIP 39M/16 | TinyCLIP 8M/16 | Paired difference (points) |
|---|---|---:|---:|---:|
| wildlife test | kind of eye right | 87.3% | 79.5% | +7.8 (+6.7 to +8.9) |
| wildlife test | kind asserted and right | 76.0% | 50.4% | +25.6 (+24.2 to +26.9) |
| wildlife test | kind asserted and wrong | 3.9% | 2.5% | +1.5 (+0.9 to +2.1) |
| wildlife test | a right species name shown | 13.1% | 0.0% | +13.1 (+12.1 to +14.1) |
| wildlife test | a species name shown | 14.2% | 0.0% | +14.2 (+13.2 to +15.3) |
| extra test | kind of eye right | 98.2% | 96.2% | +1.9 (+1.1 to +2.8) |
| extra test | kind asserted and right | 95.0% | 70.0% | +25.0 (+22.5 to +27.5) |
| extra test | kind asserted and wrong | 0.7% | 0.5% | +0.2 (-0.2 to +0.8) |
| extra test | a species name shown | 6.2% | 0.0% | +6.2 (+4.9 to +7.7) |

- **What waits for the training vectors.** Fitted heads on the real training set are unmeasured: for both pocket models (prototypes, prototypes with sentence rows, the discriminant head, the map into BioCLIP 2's space) and for BioCLIP 2 itself. `bash tools/eval/run.sh ROOT alachua-pre2025` measures them, exports the best head of each model as a slot and scores it as the page would. A build-machine run on the branch `run/eval/armed-pocket` waits for the pocket models' training vectors and then does exactly that; `run/eval/armed-all` also waits for BioCLIP 2's. Both then give the extra set's vectors up to forty minutes to appear and go on with what is published. Their results come back under `runs/eval/` on the `ci` branch, the slots go to `pub/heads-alachua-pre2025-<model>`, and `docs/eval/decision-pocket.json` in the returned files names the pocket slot to ship. The whole path was tried in the evaluation sandbox on made-up vectors of the real size (86,915 training rows in the shape of the open-data manifest, with no GBIF record ids); those numbers mean nothing and are kept nowhere. The stand-in gives one hint about BioCLIP 2: adding prototypes from about 1,200 photos to its sentence rows moved top-1 without the prior from 90.3% (89.4 to 91.3) to 91.3% (90.5 to 92.2) and top-1 with the prior from 92.4% (91.6 to 93.2) to 91.7% (90.9 to 92.6), so a real gain is not shown yet.

## The first look, checked

A first look at these models, made earlier in the night with a quick script, gave the numbers in the column `First look`. The next column is this study's number for the same model and label set.

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
| tinyclip-39m-16 | top-1 | 21.0% | 21.7% (20.5 to 22.9) | inside the interval |
| tinyclip-39m-16 | top-1 with prior | 35.0% | 35.3% (33.8 to 36.7) | inside the interval |
| tinyclip-8m-16 | kind from phrases | 72.0% | 72.0% (70.6 to 73.5) | inside the interval |
| tinyclip-8m-16 | top-1 | 15.0% | 15.4% (14.3 to 16.5) | inside the interval |
| tinyclip-8m-16 | top-1 with prior | 27.0% | 26.4% (25.1 to 27.7) | inside the interval |

15 of the 15 first-look numbers fall inside this study's interval. The first look chose its settings on `val` from a smaller grid and without smoothing choices, so differences of a point with the prior are expected.

## What others publish, and why none of it is a head-to-head comparison

The sources, with quotes, addresses and the day each page was read, are in [`docs/eval/others.md`](eval/others.md). That file was written by hand from the pages it cites. Several of its quotes came through a page-reading tool and are marked there as unchecked against the raw page. In short:

- **iNaturalist tests its own model in a way close to ours and states few figures in words.** For each release it draws "1,000 random Research Grade observations in each group not seen during training time" and compares the model's suggestion with the community's species. The newest release found is v2.34 (September 2026, 123,618 taxa); its accuracy appears only in a chart image, which was not read. The latest figure stated in words is "Overall the average accuracy of 2.20 is 88.7%" (February 2025). The post does not say whether that figure uses location, whether it counts the first suggestion only, or how the average over groups is taken.
- **With and without location.** The only such pair of figures found is from 2023: the first suggestion was right for 75% from the photo alone, 83% with the older location grid and 87% with the Geomodel. The post does not describe its test photos. iNaturalist's open code multiplies the vision score by a location score that is floored at 0.005, and does not use the month in what was read. Our prior uses the month's records within one county's list.
- **Independent tests on photos taken for the purpose give lower and scattered figures.** Six plant apps on 38 species in Ireland: species right at the first attempt for 88% of flower photos and 80% of leaf photos (Pl@ntNet) down to 4% and 7% (the iNaturalist app). Five plant apps on 857 professionally identified images: 69% right with the first suggestion. Tree leaves in New Jersey: iNaturalist right to species for 70%.
- **Research-grade labels are themselves wrong a few times in a hundred.** iNaturalist's two experiments in 2024 put them at 95% and 97% correct. A difference of a point or two between two models on such labels should be read with that in mind.
- **BioCLIP 2's own card** gives a zero-shot top-1 of 55.6 averaged over ten benchmarks, with other photos, another list of labels for each benchmark, and no place or season.
- **Nothing was found** on the accuracy of Seek, on Merlin's photo identifier beyond press figures from 2015 and 2017, or from the makers of Pl@ntNet and Google Lens.

**Why none of this can be set beside our numbers.** Our figure of 92.4% (91.6 to 93.2) is for one county, a list of 5911 species, the month known, and an average over photos. iNaturalist's 88.7% covers more than 100,000 taxa over the whole world and is an average whose construction is not stated. The photos differ, the lists differ and the counting differs. The two tests also share a weakness: research-grade photos are the ones people already agreed on, often after seeing iNaturalist's own suggestion, and nobody we found has measured how much easier that makes them. We could not run iNaturalist's model on our test photos, since its vision endpoint is unpublished and needs a token. The numbers on this page describe this recognizer on this test. They are no ranking against anyone.

## Checks for leakage and for mistakes

`tools/eval/checks.py` ran 49 checks: 39 passed, 0 failed, 10 record a fact to know, and 0 could not run because a file was not published. The full table is in [`docs/eval/checks.md`](eval/checks.md).

- **Scientific names carried by more than one species key.** 1: {"Salvia azurea": [8283204, 2927067]}. Their sentence rows are identical, so the later key can never be the top answer; photos of it on the test split: 0.
- **Test photos whose species is not in the list at all.** 36 of 4197, so a recognizer held to the list can reach at most 0.9914.
- **Label files whose kind of eye differs from the species list.** 9 label sets (bioclip-b16, mobileclip2-s0, siglip2-b16) carry another kind of eye than the list in 1 of 5911 rows. The studies take the kind from the species list, so no number here is touched; a slot built from these label files would show the earlier kinds.
- **Label rows made from an earlier species.json.** 15 label sets (of bioclip2-l14, bioclip25-h14, clip-b32, tinyclip-40m-32, tinyclip-61m-32) were made before the list's English names were revised: 645 of 5911 rows carry an English name the list no longer has (keys, scientific names and kinds agree in every row). Results for species_sci are unaffected; results for species_com and species_taxon_com describe the earlier names and would change if the rows were made again.
- **Label rows made from an earlier species.json.** 9 label sets (of bioclip-b16, mobileclip2-s0, siglip2-b16) were made before the list's English names were revised: 2099 of 5911 rows carry an English name the list no longer has (keys, scientific names and kinds agree in every row). Results for species_sci are unaffected; results for species_com and species_taxon_com describe the earlier names and would change if the rows were made again.
- **How tightly BioCLIP 2 groups a species.** 1470 of 4197 test photos have a val photo within cosine 0.95, and for 1454 of those it is the same species. Photos of one species sit close together in this model, which is why a list of names is enough for it.
- **No gbif_id is shared between the training and the evaluation photos.** the training manifest's gbif_id column is empty (it was built from iNaturalist's open-data files, which carry no GBIF record id), so this comparison says nothing; the dates and the photo numbers below do the work
- **Training observations can be compared with evaluation observations by number.** 0 of 84808 training rows give the observation by its number; the others give it by its UUID, which the evaluation manifest does not hold. An observation has one date, and every training row is dated on or before 2024-12-31 while every evaluation row is dated after it, so no observation can be on both sides.
- **Training photos per species.** 84808 photos of 5467 species (most for one species: 60); rows without a species key: 0; species keys outside the list: 0; list species without a training photo: 444
- **How the extra set is cut (tools/eval/kinds.py).** fit: cat 983, deer 1016, dog 974, none 1628, person 1343; tune: cat 517, deer 484, dog 526, none 872, person 657; test: cat 77, deer 200, dog 63, none 500, person 400. `fit` (two thirds of COCO's train rows by a hash of the id) may be used to fit a kind head, `tune` joins the wildlife tuning photos for the kind decision, `test` is only reported.

What the checks cover: the dates of the photos against the species list's cutoff and against the snapshot behind BioCLIP 2's training data; that no id, observation or photo address repeats; that the split follows from the record id alone; that every vector file has the manifest's 6,000 ids in order; that label rows follow the species list; that no test photo has a copy on `val`; once the training manifest exists, that it shares no record, observation or photo number with the evaluation set and that no training photo is dated after 2024 (a manifest built from iNaturalist's open-data files carries no GBIF record id, so there the dates and the photo numbers do the work); and for the extra set, that COCO's training and validation photos stay on their own sides and that the vectors line up with the manifest. The image vectors are made from the photo file alone: `tools/lab/lab.py` (`embed_rows`) reads only the row id to find the file.

## What this does not show

- **These photos are easier than what a phone meets.** Research-grade means that people on iNaturalist, often helped by iNaturalist's own model, already agreed on the species. Photos nobody could identify are absent. A photo taken in passing, at a distance, or of a species that needs a microscope will do worse than these numbers.
- **The large models were trained on photos of this kind.** BioCLIP 2's training data was built from a GBIF snapshot of 2024-05-01 that includes iNaturalist's research-grade photos. No test photo can be in it, since all are dated 2025 or later, yet the test photos come from the same platform, the same county and in part the same observers as its training photos. The result describes that setting.
- **One region.** Every number is for Alachua County and for a list of its own species. A longer list, or a place with fewer records, will give lower numbers.
- **The labels follow GBIF's names.** Where GBIF and iNaturalist split or name a species differently, a photo is counted against GBIF's species.
- **Nothing here compares with iNaturalist's own model.** We cannot run it, and its published accuracy figures are measured on other photos with other rules. No sentence in the app may say or suggest that this recognizer matches it.
- **People, pets, livestock and rooms are measured on COCO photos only.** They are well-lit photos from a general data set, with the subject large in the frame for people. A phone held at a blank wall, a hand, a toy animal, a painting of a bird or a screen showing a heron is in neither set, and neither is a person standing in a garden, where two answers are defensible.
- **Top-5 is measured against the whole list.** The page offers three species of the winning kind; that rule is measured in the section on what the page would show.

## Rerun on a clean machine

The whole evaluation was run again on a GitHub build machine from the published branches alone, and its numbers were compared by `tools/eval/compare.py` with the files as they were committed at that time (runs/eval/4 on the ci branch, commit b5f22175e5b4, against the files under docs/eval/ made in the evaluation sandbox with the same scripts). 31228 numbers in 13 files were compared; 0 of them differ by more than 0.0005. The comparison is kept in [`docs/eval/reproduction.txt`](eval/reproduction.txt). An earlier run of Study 1 on another build machine differed from these files in 15 of 27925 numbers, each by a single photo ([`docs/eval/reproduction-trial.txt`](eval/reproduction-trial.txt)). Two scores that are almost equal can change places when another processor does the arithmetic.

A second rerun covers the files written since the kind decision was changed to include the extra set (runs/eval/13 on the ci branch (a clean build machine, commit 72c6eb043e9f, started from the branch run/eval/coco-r4 once the pocket models' vectors of the extra set were published), against the files under docs/eval/ made in the evaluation sandbox). In the sentence slots, their study, the checks, the pocket decision and the int8 comparisons, 1 of 3192 numbers differ by more than 0.0005 (Study 1: 2 of 27925). In the stand-in files 993 of 4506 numbers differ: their kind rows are fitted by an iterative optimizer, which stopped at slightly different rows on the other machine. The stand-in slot of TinyCLIP 39M/16 in the sandbox: rule mix, t_kind 0.5, w_kind 0.7, kind_at 0.5, kind right for 87.3% of the wildlife test photos and 98.2% of the extra set's test photos, a kind asserted for 78.8% of the wildlife test photos. On the build machine: rule mix, t_kind 0.5, w_kind 0.7, kind_at 0.49, kind right for 87.3% of the wildlife test photos and 98.2% of the extra set's test photos, a kind asserted for 80.0% of the wildlife test photos. A slot with fitted kind rows is therefore the same in substance on another machine and differs in late digits. The comparison is kept in [`docs/eval/reproduction-r4.txt`](eval/reproduction-r4.txt).

## How to rerun

One command does everything (fetch, checks, Study 1, Study 2, export, as-shipped scoring, this report):

```
bash tools/eval/run.sh ROOT sentences          # slots made from sentence rows
bash tools/eval/run.sh ROOT val                # the stand-in for trained heads
bash tools/eval/run.sh ROOT alachua-pre2025    # trained heads for real, once the training vectors are published
```

The steps one at a time:

```
python3 -I tools/eval/fetch.py ROOT                 # the published data and vectors, into ROOT/data and ROOT/lab
python3 -I tools/eval/checks.py ROOT                # docs/eval/checks.json
python3 -I tools/eval/study1.py ROOT                # docs/eval/study1.json, about four minutes on two cores
python3 -I tools/eval/study2.py ROOT --train TRAIN --save ROOT/heads/TRAIN      # docs/eval/study2-TRAIN.json and the chosen heads
python3 -I tools/eval/export_heads.py ROOT --head ROOT/heads/TRAIN/MODEL.npz --out ROOT/slots/TRAIN/MODEL   # a slot in the layout of models/<slot>/
python3 -I tools/eval/shipped.py ROOT ROOT/slots/TRAIN/MODEL --name TRAIN-MODEL   # thresholds and as-shipped numbers through tools/fusion/fuse.py
python3 -I tools/eval/shipped.py ROOT models/pocket --name live-pocket --no-write   # the slot that is live, scored as it stands; its manifest is left alone
python3 -I tools/eval/decide.py                     # docs/eval/decision-pocket.json: which pocket model ships, by the rule written at the top of the script
python3 -I tools/eval/variant.py ROOT SLOT --vectors FILE.f16.npy --ids FILE.ids.json --name LABEL --name-at 0.78 --offer-at 0.66   # another set of vectors of the same test photos, beside the original's
python3 -I tools/eval/naturalist.py SLOT --shipped docs/eval/shipped-NAME.json --out DIR --variant docs/eval/variant-LABEL.json   # head files for models/naturalist
python3 -I tools/eval/report.py                     # this file and the tables under docs/eval/
python3 -I tools/eval/compare.py DIR_A DIR_B        # do two runs give the same numbers?
```

Pushing a commit to a branch named `run/eval/<label>` reruns all of it on a clean build machine (`.github/workflows/eval.yml`), returns the files and a comparison with the committed numbers under `runs/eval/` on the `ci` branch, and publishes the exported slots to `pub/heads-<train>-<model>`. A branch named `run/eval/armed<label>` waits for the training vectors and then measures the trained heads only; `run/eval/coco<label>` waits for the pocket models' vectors of the extra set and then reruns everything.

Inputs of this run: `pub/data-alachua` at `6e9a8aac93d1`; `pub/lab-bioclip-b16` at `8390d0006a34`; `pub/lab-bioclip2-l14` at `f552a63fbd5e`; `pub/lab-bioclip25-h14` at `40532989b3a9`; `pub/lab-bioclip25-mobile-fastvit` at `3c8cc3bd2386`; `pub/lab-clip-b32` at `721281767c8b`; `pub/lab-mobileclip2-s0` at `3da256a7dad0`; `pub/lab-siglip2-b16` at `5efd3b247595`; `pub/lab-tinyclip-39m-16` at `7b08c6ab3201`; `pub/lab-tinyclip-40m-32` at `6d8c0ecbd92e`; `pub/lab-tinyclip-61m-32` at `8809961eda38`; `pub/lab-tinyclip-8m-16` at `eb148eec1055`.
