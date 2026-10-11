# Exported slots, scored as the page would

_This file is written by `tools/eval/report.py` from `docs/eval/shipped-*.json`. Rerun the script to change it._

## `live-pocket`

The slot holds the head `sentences` for `tinyclip-39m-16` (species_com), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `product`, t_kind 100, w_kind 0.3, alpha_prior 1. On 1803 tuning photos (val) the thresholds came out as name_at 0.40 and offer_at 0.53. On the 4197 test photos the kind of eye is right for 83.7% (82.5 to 84.8); the top species is right for 34.9% (33.5 to 36.4) and is among the first five for 53.8% (52.3 to 55.3). `person` was said for 0.05% of these photos and `none` for 0.05%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind phrases`. With kind_at 0.88 (set on wildlife tuning photos and the extra set's tuning third), the page asserts a kind for 38.4% (37.0 to 40.0) of the wildlife test photos and is right for 99.0% (98.5 to 99.4) of those; for the 61.6% (60.0 to 62.9) where it is not sure, the true kind is among its three likeliest for 95.6% (94.8 to 96.4). On the 1240 test photos of people, cats, dogs, grazing animals and rooms (`images/coco-kinds.wasm-int8-per-channel`), the kind is right for 70.1% (67.3 to 72.6); the page asserts a kind for 3.7% (2.7 to 4.8) and is right for 97.8% (93.5 to 100.0) of those; where it is not sure the true kind is among its three likeliest for 81.7% (79.5 to 83.8). A species is named on 0.9% (0.4 to 1.5) of these photos.

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 15.2% | the name is right for 93.4% (91.4 to 95.2); the kind for 99.1% (98.1 to 99.7) |
| three species to choose from | 3.3% | the three hold the species for 85.5% (79.7 to 91.3); the kind is right for 99.3% (97.8 to 100.0) |
| a kind of eye only | 81.5% | the kind is right for 80.2% (78.8 to 81.5) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.88):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 45.5% (18.2 to 72.7) | 0.0% | – | 72.7% | 0.0% | 0.0% | 0.0% | plant (2) |
| dog | 6 | 66.7% (33.3 to 100.0) | 0.0% | – | 83.3% | 0.0% | 0.0% | 0.0% | deer (1) |
| squirrel | 36 | 75.0% (61.1 to 88.9) | 30.6% | 100.0% | 68.0% | 0.0% | 0.0% | 30.6% | plant (3) |
| deer | 36 | 63.9% (47.2 to 77.8) | 27.8% | 100.0% | 69.2% | 0.0% | 0.0% | 27.8% | plant (6) |
| rabbit | 31 | 93.5% (83.9 to 100.0) | 61.3% | 100.0% | 100.0% | 0.0% | 0.0% | 64.5% | bird (1) |
| hawk | 82 | 85.4% (76.8 to 92.7) | 46.3% | 97.4% | 84.1% | 0.0% | 0.0% | 36.6% | wader (4) |
| wader | 382 | 89.8% (86.7 to 92.7) | 58.9% | 100.0% | 94.9% | 0.0% | 0.0% | 49.7% | bird (19) |
| bird | 531 | 75.0% (71.0 to 78.5) | 12.1% | 96.9% | 94.2% | 0.2% | 0.2% | 21.7% | wader (54) |
| alligator | 110 | 91.8% (86.4 to 96.4) | 74.5% | 100.0% | 78.6% | 0.0% | 0.0% | 79.1% | plant (6) |
| reptile | 268 | 75.0% (69.8 to 79.8) | 16.0% | 97.7% | 92.4% | 0.0% | 0.4% | 22.0% | insect (31) |
| frog | 97 | 76.3% (68.0 to 84.5) | 39.2% | 100.0% | 89.8% | 0.0% | 0.0% | 3.1% | insect (14) |
| bee | 126 | 65.9% (57.9 to 73.8) | 29.4% | 91.9% | 94.4% | 0.0% | 0.0% | 0.0% | insect (33) |
| insect | 962 | 94.3% (92.7 to 95.7) | 51.2% | 99.0% | 100.0% | 0.0% | 0.0% | 3.8% | plant (20) |
| plant | 1223 | 96.2% (95.0 to 97.1) | 44.9% | 100.0% | 99.6% | 0.1% | 0.0% | 6.1% | insect (39) |
| other | 296 | 23.6% (18.9 to 28.4) | 1.4% | 0.0% | 94.9% | 0.0% | 0.0% | 0.7% | insect (175) |

The same photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| squirrel | 11 | 100.0% (100.0 to 100.0) | – |
| deer | 10 | 100.0% (100.0 to 100.0) | – |
| rabbit | 19 | 100.0% (100.0 to 100.0) | – |
| hawk | 38 | 97.4% (92.1 to 100.0) | bird (1) |
| wader | 226 | 99.6% (98.7 to 100.0) | bird (1) |
| bird | 62 | 100.0% (100.0 to 100.0) | – |
| alligator | 83 | 98.8% (96.4 to 100.0) | reptile (1) |
| reptile | 42 | 100.0% (100.0 to 100.0) | – |
| frog | 38 | 100.0% (100.0 to 100.0) | – |
| bee | 36 | 94.4% (86.1 to 100.0) | insect (2) |
| insect | 492 | 99.2% (98.4 to 99.8) | other (3) |
| plant | 556 | 98.7% (97.7 to 99.6) | insect (3) |

The kind of eye on the extra set's test photos (`images/coco-kinds.wasm-int8-per-channel`):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 95.0% (92.8 to 97.0) | 3.0% | 100.0% | 97.7% | 95.0% | 0.5% | 0.0% | insect (10) |
| none | 500 | 60.2% (56.0 to 64.4) | 0.2% | 0.0% | 78.2% | 4.4% | 60.2% | 0.0% | plant (92) |
| cat | 77 | 81.8% (72.7 to 89.6) | 29.9% | 100.0% | 77.8% | 1.3% | 1.3% | 3.9% | plant (4) |
| dog | 63 | 6.3% (1.6 to 12.7) | 0.0% | – | 17.5% | 3.2% | 0.0% | 0.0% | insect (26) |
| deer | 200 | 60.5% (54.0 to 67.0) | 5.0% | 100.0% | 80.5% | 12.5% | 0.0% | 4.0% | plant (28) |

The extra set's test photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 23 | 100.0% (100.0 to 100.0) | – |
| deer | 10 | 100.0% (100.0 to 100.0) | – |
| plant | 1 | 0.0% (0.0 to 0.0) | none (1) |
| person | 12 | 100.0% (100.0 to 100.0) | – |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.52 | 85.7% (84.6 to 86.7) | 90.3% (89.3 to 91.2) | 86.8% (84.0 to 89.5) | 50.8% (47.9 to 53.6) | 91.3% (89.0 to 93.5) | 69.3% (65.6 to 73.0) |
| 95 in 100 | 0.88 | 38.4% (37.0 to 40.0) | 99.0% (98.5 to 99.4) | 95.6% (94.8 to 96.4) | 3.7% (2.7 to 4.8) | 97.8% (93.5 to 100.0) | 81.7% (79.5 to 83.8) |
| 98 in 100 | no level reached it | – | – | – | – | – | – |

## `sentences-bioclip2-l14`

The slot holds the head `sentences` for `bioclip2-l14` (species_sci), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 20, w_kind 0.7, alpha_prior 1. On 1803 tuning photos (val) the thresholds came out as name_at 0.05 and offer_at never (no level reached nine in ten). On the 4197 test photos the kind of eye is right for 98.3% (97.8 to 98.6); the top species is right for 92.5% (91.6 to 93.2) and is among the first five for 97.5% (97.0 to 97.9). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind phrases`. With kind_at 0.20 (set on wildlife tuning photos alone, because the extra set's vectors were not published for this model), the page asserts a kind for 99.6% (99.5 to 99.8) of the wildlife test photos and is right for 98.5% (98.1 to 98.9) of those; for the 0.4% (0.2 to 0.5) where it is not sure, the true kind is among its three likeliest for 86.7% (66.7 to 100.0). The slot needs: fusion.rule mix (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 99.5% | the name is right for 92.8% (92.1 to 93.6); the kind for 98.6% (98.3 to 99.0) |
| three species to choose from | 0.0% | the three hold the species for –; the kind is right for – |
| a kind of eye only | 0.5% | the kind is right for 30.4% (13.0 to 47.8) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.20):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 90.9% (72.7 to 100.0) | 100.0% | 90.9% | – | 0.0% | 0.0% | 100.0% | reptile (1) |
| dog | 6 | 83.3% (50.0 to 100.0) | 100.0% | 83.3% | – | 0.0% | 0.0% | 100.0% | squirrel (1) |
| squirrel | 36 | 97.2% (91.7 to 100.0) | 100.0% | 97.2% | – | 0.0% | 0.0% | 100.0% | rabbit (1) |
| deer | 36 | 97.2% (91.7 to 100.0) | 97.2% | 100.0% | 0.0% | 0.0% | 0.0% | 97.2% | wader (1) |
| rabbit | 31 | 100.0% (100.0 to 100.0) | 100.0% | 100.0% | – | 0.0% | 0.0% | 100.0% | – |
| hawk | 82 | 96.3% (91.5 to 100.0) | 100.0% | 96.3% | – | 0.0% | 0.0% | 97.6% | bird (2) |
| wader | 382 | 98.7% (97.4 to 99.7) | 99.7% | 99.0% | 100.0% | 0.0% | 0.0% | 99.2% | bird (1) |
| bird | 531 | 97.0% (95.5 to 98.3) | 98.5% | 98.3% | 87.5% | 0.0% | 0.0% | 98.7% | insect (3) |
| alligator | 110 | 97.3% (93.6 to 100.0) | 100.0% | 97.3% | – | 0.0% | 0.0% | 99.1% | other (2) |
| reptile | 268 | 98.1% (96.3 to 99.6) | 99.6% | 98.5% | 100.0% | 0.0% | 0.0% | 99.3% | alligator (2) |
| frog | 97 | 97.9% (94.8 to 100.0) | 100.0% | 97.9% | – | 0.0% | 0.0% | 99.0% | bird (1) |
| bee | 126 | 95.2% (91.3 to 98.4) | 100.0% | 95.2% | – | 0.0% | 0.0% | 99.2% | plant (5) |
| insect | 962 | 98.9% (98.1 to 99.5) | 99.9% | 98.9% | 100.0% | 0.0% | 0.0% | 99.7% | plant (8) |
| plant | 1223 | 99.4% (99.0 to 99.8) | 100.0% | 99.4% | – | 0.0% | 0.0% | 99.9% | insect (4) |
| other | 296 | 96.3% (94.3 to 98.3) | 99.0% | 96.6% | 100.0% | 0.0% | 0.0% | 99.7% | plant (5) |

The same photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 10 | 100.0% (100.0 to 100.0) | – |
| dog | 6 | 83.3% (50.0 to 100.0) | other (1) |
| squirrel | 38 | 92.1% (84.2 to 100.0) | bird (1) |
| deer | 36 | 97.2% (91.7 to 100.0) | wader (1) |
| rabbit | 32 | 96.9% (90.6 to 100.0) | squirrel (1) |
| hawk | 82 | 96.3% (91.5 to 100.0) | bird (2) |
| wader | 384 | 98.2% (96.6 to 99.5) | bird (3) |
| bird | 519 | 99.0% (98.1 to 99.8) | hawk (2) |
| alligator | 109 | 98.2% (95.4 to 100.0) | reptile (2) |
| reptile | 265 | 99.2% (98.1 to 100.0) | alligator (1) |
| frog | 95 | 100.0% (100.0 to 100.0) | – |
| bee | 120 | 100.0% (100.0 to 100.0) | – |
| insect | 962 | 98.8% (98.0 to 99.4) | other (4) |
| plant | 1235 | 98.5% (97.7 to 99.1) | insect (8) |
| other | 289 | 97.9% (96.2 to 99.3) | alligator (2) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.20 | 99.6% (99.5 to 99.8) | 98.5% (98.1 to 98.9) | 86.7% (66.7 to 100.0) | – | – | – |
| 95 in 100 | 0.20 | 99.6% (99.5 to 99.8) | 98.5% (98.1 to 98.9) | 86.7% (66.7 to 100.0) | – | – | – |
| 98 in 100 | 0.20 | 99.6% (99.5 to 99.8) | 98.5% (98.1 to 98.9) | 86.7% (66.7 to 100.0) | – | – | – |

## `sentences-tinyclip-39m-16`

The slot holds the head `sentences` for `tinyclip-39m-16` (species_com), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 100, w_kind 0.5, alpha_prior 0.75. On 1803 tuning photos (val) the thresholds came out as name_at 0.27 and offer_at never (no level reached nine in ten). On the 4197 test photos the kind of eye is right for 81.4% (80.2 to 82.6); the top species is right for 35.3% (33.9 to 36.8) and is among the first five for 55.1% (53.6 to 56.6). `person` was said for 0.07% of these photos and `none` for 0.07%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind phrases`. With kind_at 0.76 (set on wildlife tuning photos and the extra set's tuning third), the page asserts a kind for 48.8% (47.3 to 50.4) of the wildlife test photos and is right for 97.7% (97.0 to 98.3) of those; for the 51.2% (49.6 to 52.7) where it is not sure, the true kind is among its three likeliest for 93.4% (92.4 to 94.5). On the 1240 test photos of people, cats, dogs, grazing animals and rooms (`images/coco-kinds.wasm-int8-per-channel`), the kind is right for 80.1% (77.8 to 82.3); the page asserts a kind for 28.9% (26.4 to 31.4) and is right for 97.8% (96.1 to 99.2) of those; where it is not sure the true kind is among its three likeliest for 82.9% (80.2 to 85.4). A species is named on 1.2% (0.7 to 1.8) of these photos. The slot needs: fusion.rule mix (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 17.3% | the name is right for 89.7% (87.5 to 91.9); the kind for 98.6% (97.8 to 99.5) |
| three species to choose from | 0.0% | the three hold the species for –; the kind is right for – |
| a kind of eye only | 82.7% | the kind is right for 77.8% (76.4 to 79.2) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.76):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 72.7% (45.5 to 100.0) | 0.0% | – | 72.7% | 0.0% | 0.0% | 0.0% | insect (2) |
| dog | 6 | 66.7% (33.3 to 100.0) | 0.0% | – | 66.7% | 0.0% | 0.0% | 0.0% | deer (1) |
| squirrel | 36 | 88.9% (77.8 to 97.2) | 13.9% | 100.0% | 90.3% | 0.0% | 0.0% | 30.6% | plant (2) |
| deer | 36 | 72.2% (58.3 to 86.1) | 13.9% | 80.0% | 77.4% | 0.0% | 0.0% | 27.8% | plant (4) |
| rabbit | 31 | 93.5% (83.9 to 100.0) | 48.4% | 100.0% | 100.0% | 0.0% | 0.0% | 67.7% | squirrel (1) |
| hawk | 82 | 86.6% (79.3 to 93.9) | 39.0% | 96.9% | 88.0% | 0.0% | 0.0% | 45.1% | insect (3) |
| wader | 382 | 89.0% (85.6 to 91.9) | 62.0% | 99.6% | 91.7% | 0.0% | 0.0% | 59.4% | bird (15) |
| bird | 531 | 65.9% (62.0 to 70.1) | 10.7% | 96.5% | 90.3% | 0.2% | 0.2% | 24.7% | wader (76) |
| alligator | 110 | 94.5% (90.0 to 98.2) | 54.5% | 100.0% | 90.0% | 0.0% | 0.0% | 76.4% | plant (5) |
| reptile | 268 | 68.7% (63.0 to 73.9) | 17.5% | 91.5% | 90.0% | 0.0% | 0.4% | 23.1% | alligator (33) |
| frog | 97 | 80.4% (72.2 to 87.6) | 29.9% | 100.0% | 92.6% | 0.0% | 0.0% | 7.2% | insect (13) |
| bee | 126 | 75.4% (68.2 to 82.5) | 20.6% | 53.8% | 97.0% | 0.0% | 0.0% | 0.0% | insect (25) |
| insect | 962 | 91.6% (89.7 to 93.2) | 66.7% | 98.9% | 100.0% | 0.0% | 0.0% | 5.5% | bee (34) |
| plant | 1223 | 95.3% (94.0 to 96.4) | 71.6% | 99.8% | 99.1% | 0.1% | 0.1% | 6.8% | insect (41) |
| other | 296 | 16.9% (12.8 to 21.3) | 5.7% | 0.0% | 91.4% | 0.3% | 0.0% | 0.3% | insect (177) |

The same photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| squirrel | 5 | 100.0% (100.0 to 100.0) | – |
| deer | 4 | 100.0% (100.0 to 100.0) | – |
| rabbit | 15 | 100.0% (100.0 to 100.0) | – |
| hawk | 31 | 100.0% (100.0 to 100.0) | – |
| wader | 237 | 99.6% (98.7 to 100.0) | bird (1) |
| bird | 55 | 100.0% (100.0 to 100.0) | – |
| alligator | 61 | 98.4% (95.1 to 100.0) | reptile (1) |
| reptile | 44 | 97.7% (93.2 to 100.0) | bird (1) |
| frog | 29 | 100.0% (100.0 to 100.0) | – |
| bee | 15 | 93.3% (80.0 to 100.0) | insect (1) |
| insect | 659 | 96.4% (94.8 to 97.7) | other (11) |
| plant | 893 | 97.9% (96.9 to 98.8) | insect (6) |

The kind of eye on the extra set's test photos (`images/coco-kinds.wasm-int8-per-channel`):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 94.8% (92.2 to 96.8) | 73.2% | 100.0% | 86.9% | 94.8% | 0.5% | 0.0% | insect (7) |
| none | 500 | 62.8% (58.6 to 67.0) | 11.8% | 88.1% | 72.3% | 3.2% | 62.8% | 0.2% | plant (64) |
| cat | 77 | 90.9% (84.4 to 97.4) | 2.6% | 100.0% | 94.7% | 0.0% | 2.6% | 3.9% | dog (2) |
| dog | 63 | 88.9% (81.0 to 95.2) | 0.0% | – | 92.1% | 1.6% | 0.0% | 0.0% | cat (4) |
| deer | 200 | 87.0% (82.0 to 91.5) | 2.5% | 80.0% | 96.9% | 8.0% | 0.0% | 5.5% | person (16) |

The extra set's test photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 2 | 100.0% (100.0 to 100.0) | – |
| deer | 4 | 100.0% (100.0 to 100.0) | – |
| plant | 5 | 0.0% (0.0 to 0.0) | none (5) |
| person | 296 | 99.0% (97.6 to 100.0) | none (2) |
| none | 52 | 100.0% (100.0 to 100.0) | – |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.53 | 79.2% (78.0 to 80.5) | 90.5% (89.5 to 91.4) | 86.8% (84.5 to 89.0) | 49.3% (46.5 to 52.1) | 95.4% (93.6 to 97.0) | 77.7% (74.4 to 80.9) |
| 95 in 100 | 0.76 | 48.8% (47.3 to 50.4) | 97.7% (97.0 to 98.3) | 93.4% (92.4 to 94.5) | 28.9% (26.4 to 31.4) | 97.8% (96.1 to 99.2) | 82.9% (80.2 to 85.4) |
| 98 in 100 | 0.88 | 20.3% (19.1 to 21.6) | 99.5% (99.1 to 99.9) | 95.5% (94.8 to 96.2) | 18.5% (16.2 to 20.6) | 99.6% (98.7 to 100.0) | 84.5% (82.2 to 86.7) |

## `sentences-tinyclip-8m-16`

The slot holds the head `sentences` for `tinyclip-8m-16` (species_com), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 100, w_kind 0.5, alpha_prior 1. On 1803 tuning photos (val) the thresholds came out as name_at 0.56 and offer_at 0.63. On the 4197 test photos the kind of eye is right for 77.3% (76.0 to 78.6); the top species is right for 26.4% (25.1 to 27.8) and is among the first five for 45.4% (43.9 to 46.9). `person` was said for 0.07% of these photos and `none` for 0.26%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind phrases`. With kind_at 0.80 (set on wildlife tuning photos and the extra set's tuning third), the page asserts a kind for 42.5% (41.0 to 44.1) of the wildlife test photos and is right for 97.4% (96.6 to 98.2) of those; for the 57.5% (55.9 to 59.0) where it is not sure, the true kind is among its three likeliest for 91.4% (90.3 to 92.5). On the 1240 test photos of people, cats, dogs, grazing animals and rooms (`images/coco-kinds.wasm-int8-per-channel`), the kind is right for 83.2% (81.0 to 85.2); the page asserts a kind for 28.1% (25.7 to 30.6) and is right for 96.9% (94.8 to 98.6) of those; where it is not sure the true kind is among its three likeliest for 90.2% (88.3 to 92.2). A species is named on 1.1% (0.6 to 1.6) of these photos. The slot needs: fusion.rule mix (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 9.4% | the name is right for 89.1% (86.0 to 92.1); the kind for 97.5% (95.7 to 98.7) |
| three species to choose from | 4.9% | the three hold the species for 81.0% (76.1 to 86.3); the kind is right for 97.6% (95.1 to 99.5) |
| a kind of eye only | 85.7% | the kind is right for 74.0% (72.5 to 75.4) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.80):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 63.6% (36.4 to 90.9) | 0.0% | – | 81.8% | 0.0% | 9.1% | 0.0% | dog (1) |
| dog | 6 | 33.3% (0.0 to 66.7) | 16.7% | 0.0% | 60.0% | 0.0% | 0.0% | 16.7% | deer (3) |
| squirrel | 36 | 66.7% (50.0 to 83.3) | 30.6% | 100.0% | 72.0% | 0.0% | 0.0% | 36.1% | other (3) |
| deer | 36 | 69.4% (52.8 to 83.3) | 19.4% | 85.7% | 75.9% | 0.0% | 0.0% | 25.0% | plant (4) |
| rabbit | 31 | 80.7% (64.5 to 93.5) | 45.2% | 100.0% | 82.4% | 0.0% | 0.0% | 38.7% | squirrel (3) |
| hawk | 82 | 79.3% (70.7 to 87.8) | 40.2% | 93.9% | 77.6% | 0.0% | 2.4% | 22.0% | bird (4) |
| wader | 382 | 84.5% (80.9 to 88.0) | 54.5% | 99.0% | 87.4% | 0.0% | 0.0% | 27.0% | bird (27) |
| bird | 531 | 60.5% (56.3 to 64.8) | 12.1% | 89.1% | 88.2% | 0.4% | 0.9% | 10.9% | wader (87) |
| alligator | 110 | 92.7% (87.3 to 97.3) | 63.6% | 100.0% | 90.0% | 0.0% | 0.0% | 69.1% | plant (3) |
| reptile | 268 | 59.3% (53.7 to 64.9) | 11.2% | 100.0% | 87.4% | 0.0% | 1.1% | 9.3% | alligator (32) |
| frog | 97 | 58.8% (49.5 to 68.0) | 21.6% | 90.5% | 72.4% | 0.0% | 0.0% | 1.0% | insect (24) |
| bee | 126 | 65.1% (57.1 to 73.0) | 16.7% | 61.9% | 93.3% | 0.0% | 0.0% | 0.0% | insect (34) |
| insect | 962 | 83.9% (81.4 to 86.1) | 45.1% | 98.6% | 98.7% | 0.0% | 0.0% | 2.6% | plant (43) |
| plant | 1223 | 95.3% (94.1 to 96.5) | 69.6% | 100.0% | 98.4% | 0.1% | 0.0% | 4.2% | insect (35) |
| other | 296 | 27.0% (22.0 to 32.1) | 6.4% | 10.5% | 91.3% | 0.0% | 0.0% | 0.7% | insect (140) |

The same photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| squirrel | 11 | 100.0% (100.0 to 100.0) | – |
| deer | 7 | 85.7% (57.1 to 100.0) | dog (1) |
| rabbit | 14 | 100.0% (100.0 to 100.0) | – |
| hawk | 34 | 91.2% (82.3 to 100.0) | bird (2) |
| wader | 211 | 97.6% (95.3 to 99.5) | bird (4) |
| bird | 57 | 100.0% (100.0 to 100.0) | – |
| alligator | 72 | 97.2% (93.1 to 100.0) | bird (1) |
| reptile | 30 | 100.0% (100.0 to 100.0) | – |
| frog | 20 | 95.0% (85.0 to 100.0) | insect (1) |
| bee | 14 | 92.9% (78.6 to 100.0) | insect (1) |
| insect | 449 | 95.3% (93.3 to 97.1) | other (14) |
| plant | 863 | 98.6% (97.8 to 99.3) | insect (4) |
| other | 2 | 100.0% (100.0 to 100.0) | – |

The kind of eye on the extra set's test photos (`images/coco-kinds.wasm-int8-per-channel`):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 90.8% (87.8 to 93.5) | 38.2% | 99.3% | 96.4% | 90.8% | 3.5% | 0.0% | other (16) |
| none | 500 | 78.6% (74.8 to 82.2) | 36.6% | 96.7% | 83.9% | 1.2% | 78.6% | 0.0% | plant (52) |
| cat | 77 | 92.2% (85.7 to 97.4) | 3.9% | 66.7% | 94.6% | 1.3% | 3.9% | 5.2% | none (3) |
| dog | 63 | 81.0% (71.4 to 90.5) | 0.0% | – | 90.5% | 3.2% | 0.0% | 0.0% | cat (6) |
| deer | 200 | 76.5% (70.5 to 82.0) | 5.0% | 70.0% | 91.1% | 14.0% | 2.5% | 4.5% | person (28) |

The extra set's test photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 2 | 100.0% (100.0 to 100.0) | – |
| deer | 7 | 100.0% (100.0 to 100.0) | – |
| rabbit | 1 | 0.0% (0.0 to 0.0) | deer (1) |
| plant | 6 | 0.0% (0.0 to 0.0) | none (6) |
| person | 155 | 98.1% (95.5 to 100.0) | deer (2) |
| none | 178 | 99.4% (98.3 to 100.0) | person (1) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.61 | 67.5% (66.0 to 68.9) | 90.2% (89.2 to 91.3) | 88.1% (86.5 to 89.7) | 51.0% (48.2 to 53.8) | 93.8% (91.8 to 95.7) | 87.5% (84.8 to 90.0) |
| 95 in 100 | 0.80 | 42.5% (41.0 to 44.1) | 97.4% (96.6 to 98.2) | 91.4% (90.3 to 92.5) | 28.1% (25.7 to 30.6) | 96.9% (94.8 to 98.6) | 90.2% (88.3 to 92.2) |
| 98 in 100 | 0.92 | 16.6% (15.4 to 17.8) | 99.7% (99.3 to 100.0) | 93.8% (93.0 to 94.6) | 9.8% (8.2 to 11.5) | 98.4% (95.9 to 100.0) | 91.6% (90.1 to 93.2) |

## `val-bioclip2-l14`

The slot holds the head `prototypes + sentences` for `bioclip2-l14` (species_sci, beta 8, bias for species without photos 0.65), fitted on `images/alachua-2025 (two thirds of val)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `product`, t_kind 20, w_kind 0.5, alpha_prior 0.6. On 565 tuning photos (the third of val kept for tuning) the thresholds came out as name_at 0.05 and offer_at never (no level reached nine in ten). On the 4197 test photos the kind of eye is right for 98.6% (98.2 to 98.9); the top species is right for 91.7% (90.9 to 92.6) and is among the first five for 97.6% (97.1 to 98.0). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind phrases`. With kind_at 0.20 (set on wildlife tuning photos alone, because the extra set's vectors were not published for this model), the page asserts a kind for 100.0% (99.9 to 100.0) of the wildlife test photos and is right for 98.6% (98.2 to 99.0) of those; for the 0.1% (0.0 to 0.1) where it is not sure, the true kind is among its three likeliest for 50.0% (0.0 to 100.0). The slot needs: species.bias_url (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 99.5% | the name is right for 92.2% (91.3 to 92.9); the kind for 98.8% (98.4 to 99.1) |
| three species to choose from | 0.0% | the three hold the species for –; the kind is right for – |
| a kind of eye only | 0.5% | the kind is right for 52.4% (28.6 to 71.4) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.20):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 90.9% (72.7 to 100.0) | 100.0% | 90.9% | – | 0.0% | 0.0% | 100.0% | reptile (1) |
| dog | 6 | 83.3% (50.0 to 100.0) | 100.0% | 83.3% | – | 0.0% | 0.0% | 83.3% | squirrel (1) |
| squirrel | 36 | 97.2% (91.7 to 100.0) | 100.0% | 97.2% | – | 0.0% | 0.0% | 100.0% | rabbit (1) |
| deer | 36 | 97.2% (91.7 to 100.0) | 100.0% | 97.2% | – | 0.0% | 0.0% | 100.0% | alligator (1) |
| rabbit | 31 | 100.0% (100.0 to 100.0) | 100.0% | 100.0% | – | 0.0% | 0.0% | 100.0% | – |
| hawk | 82 | 96.3% (91.5 to 100.0) | 100.0% | 96.3% | – | 0.0% | 0.0% | 97.6% | bird (2) |
| wader | 382 | 98.7% (97.4 to 99.7) | 100.0% | 98.7% | – | 0.0% | 0.0% | 99.7% | bird (2) |
| bird | 531 | 98.5% (97.4 to 99.4) | 99.6% | 98.7% | 50.0% | 0.0% | 0.0% | 99.4% | other (2) |
| alligator | 110 | 96.4% (92.7 to 99.1) | 100.0% | 96.4% | – | 0.0% | 0.0% | 100.0% | other (2) |
| reptile | 268 | 97.8% (95.9 to 99.2) | 100.0% | 97.8% | – | 0.0% | 0.0% | 98.9% | alligator (2) |
| frog | 97 | 97.9% (94.8 to 100.0) | 100.0% | 97.9% | – | 0.0% | 0.0% | 100.0% | bird (1) |
| bee | 126 | 98.4% (96.0 to 100.0) | 100.0% | 98.4% | – | 0.0% | 0.0% | 98.4% | insect (1) |
| insect | 962 | 99.2% (98.5 to 99.7) | 100.0% | 99.2% | – | 0.0% | 0.0% | 99.6% | plant (6) |
| plant | 1223 | 99.4% (99.0 to 99.8) | 100.0% | 99.4% | – | 0.0% | 0.0% | 99.8% | insect (4) |
| other | 296 | 96.3% (93.9 to 98.3) | 100.0% | 96.3% | – | 0.0% | 0.0% | 99.3% | insect (4) |

The same photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 10 | 100.0% (100.0 to 100.0) | – |
| dog | 6 | 83.3% (50.0 to 100.0) | other (1) |
| squirrel | 38 | 92.1% (84.2 to 100.0) | bird (1) |
| deer | 36 | 97.2% (91.7 to 100.0) | wader (1) |
| rabbit | 32 | 96.9% (90.6 to 100.0) | squirrel (1) |
| hawk | 79 | 100.0% (100.0 to 100.0) | – |
| wader | 382 | 98.7% (97.4 to 99.7) | plant (3) |
| bird | 528 | 98.9% (97.9 to 99.6) | hawk (2) |
| alligator | 109 | 97.2% (93.6 to 100.0) | reptile (2) |
| reptile | 267 | 98.1% (96.2 to 99.6) | alligator (2) |
| frog | 95 | 100.0% (100.0 to 100.0) | – |
| bee | 124 | 100.0% (100.0 to 100.0) | – |
| insect | 966 | 98.8% (97.9 to 99.4) | other (4) |
| plant | 1230 | 98.9% (98.3 to 99.4) | insect (6) |
| other | 293 | 97.3% (95.2 to 99.0) | alligator (2) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.20 | 100.0% (99.9 to 100.0) | 98.6% (98.2 to 99.0) | 50.0% (0.0 to 100.0) | – | – | – |
| 95 in 100 | 0.20 | 100.0% (99.9 to 100.0) | 98.6% (98.2 to 99.0) | 50.0% (0.0 to 100.0) | – | – | – |
| 98 in 100 | 0.20 | 100.0% (99.9 to 100.0) | 98.6% (98.2 to 99.0) | 50.0% (0.0 to 100.0) | – | – | – |

## `val-tinyclip-39m-16`

The slot holds the head `prototypes + sentences` for `tinyclip-39m-16` (species_taxon_com, beta 8, bias for species without photos 0.8), fitted on `images/alachua-2025 (two thirds of val)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 0.5, w_kind 0.7, alpha_prior 1. On 565 tuning photos (the third of val kept for tuning) the thresholds came out as name_at 0.90 and offer_at 0.94. On the 4197 test photos the kind of eye is right for 87.3% (86.3 to 88.3); the top species is right for 36.3% (34.9 to 37.8) and is among the first five for 58.8% (57.3 to 60.2). `person` was said for 0.10% of these photos and `none` for 0.07%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind rows fitted on the fitting photos and the extra set (a kind's photos weighted by the inverse square root of their number)`. With kind_at 0.49 (set on wildlife tuning photos and the extra set's tuning third), the page asserts a kind for 79.9% (78.7 to 81.1) of the wildlife test photos and is right for 95.1% (94.4 to 95.9) of those; for the 20.1% (18.9 to 21.3) where it is not sure, the true kind is among its three likeliest for 89.9% (87.8 to 91.9). On the 1240 test photos of people, cats, dogs, grazing animals and rooms (`images/coco-kinds.wasm-int8-per-channel`), the kind is right for 98.2% (97.3 to 98.8); the page asserts a kind for 95.7% (94.5 to 96.9) and is right for 99.2% (98.7 to 99.7) of those; where it is not sure the true kind is among its three likeliest for 94.3% (86.8 to 100.0). A species is named on 6.2% (4.9 to 7.7) of these photos. The slot needs: species.bias_url (build 7 of the page); kinds.bias (build 7 of the page); fusion.rule mix (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 14.2% | the name is right for 92.0% (89.6 to 94.0); the kind for 98.5% (97.5 to 99.3) |
| three species to choose from | 7.3% | the three hold the species for 90.3% (86.7 to 93.5); the kind is right for 97.7% (95.8 to 99.4) |
| a kind of eye only | 78.5% | the kind is right for 84.3% (83.1 to 85.6) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.49):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 63.6% (36.4 to 90.9) | 63.6% | 85.7% | 25.0% | 0.0% | 9.1% | 27.3% | plant (2) |
| dog | 6 | 50.0% (16.7 to 83.3) | 0.0% | – | 66.7% | 0.0% | 0.0% | 33.3% | deer (1) |
| squirrel | 36 | 80.6% (66.7 to 91.7) | 52.8% | 94.7% | 70.6% | 0.0% | 0.0% | 58.3% | wader (3) |
| deer | 36 | 69.4% (52.8 to 83.3) | 58.3% | 95.2% | 53.3% | 0.0% | 0.0% | 52.8% | plant (5) |
| rabbit | 31 | 87.1% (74.2 to 96.8) | 51.6% | 100.0% | 86.7% | 0.0% | 0.0% | 45.2% | wader (2) |
| hawk | 82 | 75.6% (65.8 to 85.4) | 68.3% | 92.9% | 92.3% | 0.0% | 0.0% | 36.6% | bird (11) |
| wader | 382 | 85.9% (82.2 to 89.3) | 85.9% | 93.0% | 87.0% | 0.0% | 0.0% | 35.1% | bird (37) |
| bird | 531 | 85.1% (82.1 to 88.1) | 73.1% | 96.4% | 93.7% | 0.2% | 0.2% | 23.2% | wader (35) |
| alligator | 110 | 81.8% (74.6 to 89.1) | 77.3% | 96.5% | 72.0% | 0.0% | 0.0% | 67.3% | plant (7) |
| reptile | 268 | 83.6% (79.5 to 87.7) | 68.7% | 93.5% | 86.9% | 0.7% | 0.0% | 14.2% | plant (17) |
| frog | 97 | 80.4% (72.2 to 87.6) | 69.1% | 95.5% | 76.7% | 0.0% | 0.0% | 3.1% | reptile (10) |
| bee | 126 | 60.3% (51.6 to 69.0) | 69.8% | 72.7% | 89.5% | 0.0% | 0.0% | 3.2% | insect (34) |
| insect | 962 | 88.1% (86.1 to 90.0) | 79.6% | 94.6% | 97.4% | 0.1% | 0.0% | 4.9% | plant (43) |
| plant | 1223 | 98.4% (97.6 to 99.0) | 94.1% | 99.4% | 97.2% | 0.0% | 0.0% | 6.4% | insect (10) |
| other | 296 | 71.6% (66.5 to 76.7) | 60.1% | 83.1% | 89.8% | 0.0% | 0.3% | 2.0% | insect (42) |

The same photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 6 | 100.0% (100.0 to 100.0) | – |
| squirrel | 21 | 85.7% (71.4 to 100.0) | cat (1) |
| deer | 20 | 100.0% (100.0 to 100.0) | – |
| rabbit | 16 | 100.0% (100.0 to 100.0) | – |
| hawk | 54 | 96.3% (90.7 to 100.0) | bird (1) |
| wader | 319 | 95.6% (93.1 to 97.8) | bird (12) |
| bird | 396 | 94.4% (92.2 to 96.5) | wader (18) |
| alligator | 83 | 98.8% (96.4 to 100.0) | reptile (1) |
| reptile | 187 | 92.0% (88.2 to 95.7) | other (5) |
| frog | 67 | 95.5% (89.5 to 100.0) | insect (2) |
| bee | 68 | 94.1% (88.2 to 98.5) | insect (3) |
| insect | 761 | 95.3% (93.7 to 96.7) | bee (16) |
| plant | 1191 | 96.0% (94.9 to 97.2) | insect (17) |
| other | 165 | 89.7% (84.9 to 93.9) | insect (14) |

The kind of eye on the extra set's test photos (`images/coco-kinds.wasm-int8-per-channel`):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 99.5% (98.8 to 100.0) | 98.5% | 99.7% | 100.0% | 99.5% | 0.2% | 0.0% | none (1) |
| none | 500 | 98.6% (97.4 to 99.6) | 95.6% | 100.0% | 100.0% | 0.0% | 98.6% | 0.0% | cat (3) |
| cat | 77 | 92.2% (85.7 to 97.4) | 89.6% | 97.1% | 62.5% | 0.0% | 5.2% | 50.6% | none (4) |
| dog | 63 | 95.2% (88.9 to 100.0) | 90.5% | 94.7% | 100.0% | 0.0% | 0.0% | 1.6% | cat (3) |
| deer | 200 | 97.5% (95.0 to 99.5) | 94.5% | 98.4% | 100.0% | 1.0% | 0.5% | 18.5% | person (2) |

The extra set's test photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 70 | 95.7% (90.0 to 100.0) | dog (3) |
| dog | 55 | 98.2% (94.5 to 100.0) | deer (1) |
| deer | 186 | 100.0% (100.0 to 100.0) | – |
| person | 395 | 99.5% (98.7 to 100.0) | deer (2) |
| other | 1 | 0.0% (0.0 to 0.0) | person (1) |
| none | 480 | 99.6% (99.0 to 100.0) | cat (2) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.30 | 96.5% (95.9 to 97.0) | 89.2% (88.3 to 90.1) | 78.5% (71.8 to 84.6) | 99.4% (99.0 to 99.8) | 98.6% (98.0 to 99.2) | 85.7% (57.1 to 100.0) |
| 95 in 100 | 0.49 | 79.9% (78.7 to 81.1) | 95.1% (94.4 to 95.9) | 89.9% (87.8 to 91.9) | 95.7% (94.5 to 96.9) | 99.2% (98.7 to 99.7) | 94.3% (86.8 to 100.0) |
| 98 in 100 | 0.63 | 62.3% (60.8 to 63.8) | 97.7% (97.1 to 98.2) | 93.7% (92.5 to 94.9) | 86.0% (84.0 to 87.9) | 99.7% (99.3 to 100.0) | 97.1% (94.2 to 99.4) |

## `val-tinyclip-8m-16`

The slot holds the head `discriminant + sentences` for `tinyclip-8m-16` (shrinkage 0.03, species_com, gamma 1), fitted on `images/alachua-2025 (two thirds of val)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 0.5, w_kind 0.5, alpha_prior 0.5. On 565 tuning photos (the third of val kept for tuning) the thresholds came out as name_at never (no level reached nine in ten) and offer_at 0.24. On the 4197 test photos the kind of eye is right for 79.5% (78.3 to 80.7); the top species is right for 25.3% (24.0 to 26.6) and is among the first five for 45.4% (43.9 to 46.9). `person` was said for 0.14% of these photos and `none` for 0.24%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind rows fitted on the fitting photos and the extra set (every kind counts the same)`. With kind_at 0.53 (set on wildlife tuning photos and the extra set's tuning third), the page asserts a kind for 52.9% (51.4 to 54.4) of the wildlife test photos and is right for 95.4% (94.5 to 96.2) of those; for the 47.1% (45.6 to 48.6) where it is not sure, the true kind is among its three likeliest for 88.6% (87.2 to 90.0). On the 1240 test photos of people, cats, dogs, grazing animals and rooms (`images/coco-kinds.wasm-int8-per-channel`), the kind is right for 96.2% (95.2 to 97.3); the page asserts a kind for 70.5% (68.0 to 73.1) and is right for 99.3% (98.7 to 99.8) of those; where it is not sure the true kind is among its three likeliest for 94.3% (91.8 to 96.5). A species is named on 0.0% (0.0 to 0.0) of these photos. The slot needs: species.bias_url (build 7 of the page); kinds.bias (build 7 of the page); fusion.rule mix (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 0.0% | the name is right for –; the kind for – |
| three species to choose from | 15.8% | the three hold the species for 82.9% (79.9 to 85.7); the kind is right for 97.4% (96.1 to 98.5) |
| a kind of eye only | 84.2% | the kind is right for 76.1% (74.7 to 77.5) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.53):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 45.5% (18.2 to 72.7) | 0.0% | – | 63.6% | 0.0% | 9.1% | 0.0% | plant (3) |
| dog | 6 | 0.0% (0.0 to 0.0) | 0.0% | – | 16.7% | 0.0% | 0.0% | 0.0% | other (2) |
| squirrel | 36 | 52.8% (38.9 to 69.4) | 16.7% | 100.0% | 60.0% | 0.0% | 0.0% | 0.0% | plant (6) |
| deer | 36 | 69.4% (52.8 to 83.3) | 5.6% | 50.0% | 70.6% | 0.0% | 0.0% | 0.0% | plant (6) |
| rabbit | 31 | 64.5% (45.2 to 80.7) | 35.5% | 100.0% | 60.0% | 0.0% | 0.0% | 0.0% | squirrel (6) |
| hawk | 82 | 50.0% (39.0 to 61.0) | 20.7% | 88.2% | 75.4% | 0.0% | 0.0% | 0.0% | bird (25) |
| wader | 382 | 74.1% (69.4 to 78.3) | 51.0% | 94.9% | 87.2% | 0.0% | 0.0% | 0.0% | bird (72) |
| bird | 531 | 79.7% (76.1 to 83.0) | 37.1% | 95.9% | 91.9% | 0.2% | 0.9% | 0.0% | wader (47) |
| alligator | 110 | 73.6% (65.5 to 81.8) | 47.3% | 100.0% | 81.0% | 0.0% | 0.0% | 0.0% | plant (9) |
| reptile | 268 | 53.4% (47.4 to 59.3) | 14.9% | 85.0% | 82.5% | 0.7% | 0.4% | 0.0% | insect (79) |
| frog | 97 | 53.6% (44.3 to 62.9) | 22.7% | 90.9% | 72.0% | 0.0% | 1.0% | 0.0% | insect (30) |
| bee | 126 | 42.1% (34.1 to 50.0) | 44.4% | 41.1% | 84.3% | 0.0% | 0.0% | 0.0% | insect (60) |
| insect | 962 | 90.8% (88.9 to 92.5) | 59.0% | 97.4% | 99.5% | 0.2% | 0.1% | 0.0% | plant (39) |
| plant | 1223 | 95.7% (94.4 to 96.8) | 77.9% | 99.7% | 98.9% | 0.0% | 0.1% | 0.0% | insect (33) |
| other | 296 | 49.7% (44.3 to 55.4) | 33.8% | 77.0% | 83.7% | 0.3% | 0.0% | 0.0% | insect (107) |

The same photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| squirrel | 6 | 100.0% (100.0 to 100.0) | – |
| deer | 1 | 100.0% (100.0 to 100.0) | – |
| rabbit | 11 | 100.0% (100.0 to 100.0) | – |
| hawk | 15 | 100.0% (100.0 to 100.0) | – |
| wader | 192 | 96.4% (93.8 to 99.0) | bird (7) |
| bird | 199 | 95.0% (92.0 to 98.0) | wader (9) |
| alligator | 53 | 98.1% (94.3 to 100.0) | bird (1) |
| reptile | 34 | 100.0% (100.0 to 100.0) | – |
| frog | 20 | 100.0% (100.0 to 100.0) | – |
| bee | 26 | 88.5% (76.9 to 100.0) | insect (3) |
| insect | 606 | 91.2% (88.9 to 93.4) | bee (27) |
| plant | 975 | 97.4% (96.4 to 98.4) | insect (9) |
| other | 81 | 95.1% (90.1 to 98.8) | insect (3) |

The kind of eye on the extra set's test photos (`images/coco-kinds.wasm-int8-per-channel`):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 98.2% (96.8 to 99.5) | 95.0% | 99.2% | 100.0% | 98.2% | 1.5% | 0.0% | none (6) |
| none | 500 | 97.4% (95.8 to 98.8) | 89.6% | 100.0% | 86.5% | 0.6% | 97.4% | 0.0% | cat (3) |
| cat | 77 | 89.6% (83.1 to 96.1) | 20.8% | 87.5% | 91.8% | 2.6% | 5.2% | 0.0% | none (4) |
| dog | 63 | 88.9% (81.0 to 96.8) | 0.0% | – | 92.1% | 0.0% | 0.0% | 0.0% | cat (5) |
| deer | 200 | 94.0% (90.5 to 97.0) | 15.0% | 96.7% | 97.6% | 2.0% | 0.0% | 0.0% | dog (6) |

The extra set's test photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 14 | 100.0% (100.0 to 100.0) | – |
| deer | 29 | 100.0% (100.0 to 100.0) | – |
| person | 379 | 99.5% (98.7 to 100.0) | cat (1) |
| none | 452 | 99.1% (98.2 to 99.8) | person (3) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.39 | 76.7% (75.5 to 78.0) | 89.0% (87.9 to 90.1) | 81.9% (79.6 to 84.2) | 89.9% (88.2 to 91.5) | 98.7% (97.9 to 99.3) | 87.2% (81.6 to 92.8) |
| 95 in 100 | 0.53 | 52.9% (51.4 to 54.4) | 95.4% (94.5 to 96.2) | 88.6% (87.2 to 90.0) | 70.5% (68.0 to 73.1) | 99.3% (98.7 to 99.8) | 94.3% (91.8 to 96.5) |
| 98 in 100 | 0.61 | 39.7% (38.2 to 41.2) | 97.2% (96.5 to 98.0) | 90.6% (89.5 to 91.7) | 63.6% (61.1 to 66.4) | 99.9% (99.6 to 100.0) | 94.7% (92.7 to 96.7) |
