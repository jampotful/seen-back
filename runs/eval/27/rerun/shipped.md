# Exported slots, scored as the page would

_This file is written by `tools/eval/report.py` from `docs/eval/shipped-*.json`. Rerun the script to change it._

## `alachua-pre2025-by-tinyclip-39m-16`

The slot holds the head `discriminant + sentences` for `tinyclip-39m-16` (shrinkage 0.3, species_com, gamma 0.03), fitted on `images/alachua-pre2025 (licence rule by)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 0.5, w_kind 0.7, alpha_prior 0.5. On 1803 tuning photos (val) the thresholds came out as name_at 0.68 and offer_at never (no level reached nine in ten). On the 4197 test photos the kind of eye is right for 86.0% (84.9 to 87.1); the top species is right for 43.8% (42.3 to 45.4) and is among the first five for 66.0% (64.5 to 67.4). `person` was said for 0.02% of these photos and `none` for 0.14%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind rows fitted on the fitting photos and the extra set (a kind's photos weighted by the inverse square root of their number)`. With kind_at 0.54 (set on wildlife tuning photos and the extra set's tuning third), the page asserts a kind for 73.0% (71.7 to 74.4) of the wildlife test photos and is right for 96.7% (96.0 to 97.3) of those; for the 27.0% (25.6 to 28.3) where it is not sure, the true kind is among its three likeliest for 87.9% (86.0 to 89.7). On the 1240 test photos of people, cats, dogs, grazing animals and rooms (`images/coco-kinds.wasm-int8-per-channel`), the kind is right for 96.7% (95.7 to 97.7); the page asserts a kind for 92.7% (91.2 to 94.1) and is right for 99.0% (98.4 to 99.5) of those; where it is not sure the true kind is among its three likeliest for 95.6% (91.2 to 98.9). A species is named on 14.8% (12.9 to 16.9) of these photos. The slot needs: species.bias_url (build 7 of the page); kinds.bias (build 7 of the page); fusion.rule mix (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 11.7% | the name is right for 90.0% (87.4 to 92.5); the kind for 98.8% (97.8 to 99.6) |
| three species to choose from | 0.0% | the three hold the species for –; the kind is right for – |
| a kind of eye only | 88.3% | the kind is right for 84.3% (83.1 to 85.4) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.54):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 54.5% (27.3 to 81.8) | 54.5% | 100.0% | 40.0% | 0.0% | 9.1% | 54.5% | bird (1) |
| dog | 6 | 83.3% (50.0 to 100.0) | 33.3% | 100.0% | 75.0% | 0.0% | 0.0% | 33.3% | squirrel (1) |
| squirrel | 36 | 86.1% (75.0 to 97.2) | 44.4% | 100.0% | 85.0% | 0.0% | 0.0% | 41.7% | plant (2) |
| deer | 36 | 69.4% (52.8 to 83.3) | 55.6% | 95.0% | 62.5% | 0.0% | 0.0% | 52.8% | other (3) |
| rabbit | 31 | 80.7% (67.7 to 93.5) | 71.0% | 100.0% | 77.8% | 0.0% | 0.0% | 64.5% | squirrel (3) |
| hawk | 82 | 78.0% (68.3 to 86.6) | 67.1% | 96.4% | 66.7% | 0.0% | 0.0% | 36.6% | bird (11) |
| wader | 382 | 82.5% (78.5 to 86.1) | 79.3% | 93.1% | 88.6% | 0.0% | 0.0% | 34.0% | bird (48) |
| bird | 531 | 82.9% (79.5 to 86.1) | 66.5% | 95.8% | 88.8% | 0.0% | 0.8% | 18.5% | wader (32) |
| alligator | 110 | 60.0% (50.9 to 69.1) | 43.6% | 95.8% | 54.8% | 0.0% | 0.0% | 41.8% | reptile (20) |
| reptile | 268 | 72.4% (66.8 to 77.6) | 50.4% | 96.3% | 81.2% | 0.0% | 0.0% | 4.5% | insect (37) |
| frog | 97 | 76.3% (67.0 to 84.5) | 59.8% | 98.3% | 94.9% | 0.0% | 0.0% | 1.0% | insect (14) |
| bee | 126 | 69.8% (61.9 to 78.6) | 63.5% | 83.8% | 91.3% | 0.0% | 0.0% | 3.2% | insect (24) |
| insect | 962 | 90.4% (88.6 to 92.2) | 71.0% | 96.5% | 98.9% | 0.0% | 0.0% | 1.9% | plant (37) |
| plant | 1223 | 98.2% (97.4 to 98.9) | 91.3% | 99.8% | 100.0% | 0.0% | 0.1% | 5.6% | insect (12) |
| other | 296 | 69.3% (64.2 to 74.7) | 56.4% | 90.4% | 82.9% | 0.3% | 0.0% | 7.1% | insect (55) |

The same photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 6 | 100.0% (100.0 to 100.0) | – |
| dog | 2 | 100.0% (100.0 to 100.0) | – |
| squirrel | 16 | 100.0% (100.0 to 100.0) | – |
| deer | 19 | 100.0% (100.0 to 100.0) | – |
| rabbit | 22 | 100.0% (100.0 to 100.0) | – |
| hawk | 58 | 91.4% (84.5 to 98.3) | wader (3) |
| wader | 295 | 95.6% (93.2 to 97.6) | bird (13) |
| bird | 356 | 94.9% (92.7 to 96.9) | wader (15) |
| alligator | 46 | 100.0% (100.0 to 100.0) | – |
| reptile | 135 | 96.3% (92.6 to 99.3) | alligator (2) |
| frog | 59 | 96.6% (91.5 to 100.0) | insect (2) |
| bee | 75 | 89.3% (81.3 to 96.0) | insect (7) |
| insect | 674 | 97.8% (96.6 to 98.8) | other (8) |
| plant | 1145 | 97.4% (96.4 to 98.2) | insect (9) |
| other | 157 | 96.2% (93.0 to 98.7) | insect (5) |

The kind of eye on the extra set's test photos (`images/coco-kinds.wasm-int8-per-channel`):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 99.0% (98.0 to 99.8) | 94.8% | 100.0% | 95.2% | 99.0% | 0.8% | 0.0% | none (3) |
| none | 500 | 97.2% (95.6 to 98.6) | 92.2% | 99.6% | 97.4% | 0.2% | 97.2% | 0.2% | plant (5) |
| cat | 77 | 89.6% (81.8 to 96.1) | 89.6% | 95.7% | 75.0% | 1.3% | 5.2% | 85.7% | none (4) |
| dog | 63 | 90.5% (82.5 to 96.8) | 84.1% | 94.3% | 100.0% | 0.0% | 0.0% | 4.8% | cat (5) |
| deer | 200 | 95.5% (92.5 to 98.0) | 93.5% | 97.9% | 100.0% | 1.0% | 0.5% | 57.0% | dog (4) |

The extra set's test photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 70 | 94.3% (88.6 to 98.6) | dog (3) |
| dog | 53 | 94.3% (86.8 to 100.0) | deer (3) |
| deer | 183 | 100.0% (100.0 to 100.0) | – |
| plant | 1 | 0.0% (0.0 to 0.0) | none (1) |
| person | 380 | 99.7% (99.2 to 100.0) | deer (1) |
| none | 462 | 99.4% (98.5 to 100.0) | cat (3) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.36 | 90.5% (89.7 to 91.4) | 90.9% (90.0 to 91.8) | 75.6% (71.0 to 79.6) | 98.6% (98.0 to 99.3) | 97.5% (96.7 to 98.4) | 82.3% (64.7 to 100.0) |
| 95 in 100 | 0.54 | 73.0% (71.7 to 74.4) | 96.7% (96.0 to 97.3) | 87.9% (86.0 to 89.7) | 92.7% (91.2 to 94.1) | 99.0% (98.4 to 99.5) | 95.6% (91.2 to 98.9) |
| 98 in 100 | 0.69 | 57.3% (55.8 to 58.8) | 98.5% (98.0 to 99.0) | 91.9% (90.6 to 93.0) | 78.0% (75.6 to 80.5) | 99.4% (98.9 to 99.8) | 97.1% (94.9 to 98.9) |

## `alachua-pre2025-nc-tinyclip-39m-16`

The slot holds the head `discriminant` for `tinyclip-39m-16` (shrinkage 0.03), fitted on `images/alachua-pre2025 (licence rule nc)`, with 5391 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 1, w_kind 0.7, alpha_prior 0.75. On 1803 tuning photos (val) the thresholds came out as name_at 0.86 and offer_at 0.86. On the 4197 test photos the kind of eye is right for 88.1% (87.1 to 89.1); the top species is right for 53.8% (52.2 to 55.4) and is among the first five for 75.1% (73.8 to 76.5). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind rows fitted on the fitting photos and the extra set (every photo counts the same)`. With kind_at 0.69 (set on wildlife tuning photos and the extra set's tuning third), the page asserts a kind for 82.4% (81.3 to 83.6) of the wildlife test photos and is right for 95.5% (94.7 to 96.1) of those; for the 17.6% (16.4 to 18.7) where it is not sure, the true kind is among its three likeliest for 89.3% (87.0 to 91.5). On the 1240 test photos of people, cats, dogs, grazing animals and rooms (`images/coco-kinds.wasm-int8-per-channel`), the kind is right for 96.9% (95.9 to 97.8); the page asserts a kind for 93.0% (91.5 to 94.3) and is right for 98.4% (97.8 to 99.1) of those; where it is not sure the true kind is among its three likeliest for 92.0% (85.1 to 97.7). A species is named on 15.3% (13.3 to 17.4) of these photos. The slot needs: species.bias_url (build 7 of the page); kinds.bias (build 7 of the page); fusion.rule mix (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 21.2% | the name is right for 91.8% (89.9 to 93.6); the kind for 97.9% (96.9 to 98.8) |
| three species to choose from | 16.6% | the three hold the species for 87.1% (84.5 to 89.5); the kind is right for 96.0% (94.5 to 97.4) |
| a kind of eye only | 62.2% | the kind is right for 82.7% (81.3 to 84.1) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.69):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 72.7% (45.5 to 100.0) | 63.6% | 100.0% | 75.0% | 0.0% | 0.0% | 63.6% | bird (1) |
| dog | 6 | 83.3% (50.0 to 100.0) | 66.7% | 100.0% | 50.0% | 0.0% | 0.0% | 50.0% | squirrel (1) |
| squirrel | 36 | 88.9% (77.8 to 97.2) | 69.4% | 100.0% | 72.7% | 0.0% | 0.0% | 63.9% | bird (1) |
| deer | 36 | 77.8% (63.9 to 88.9) | 69.4% | 92.0% | 54.5% | 0.0% | 0.0% | 63.9% | other (3) |
| rabbit | 31 | 77.4% (61.3 to 90.3) | 74.2% | 95.7% | 75.0% | 0.0% | 0.0% | 54.8% | other (3) |
| hawk | 82 | 80.5% (72.0 to 89.0) | 76.8% | 92.1% | 84.2% | 0.0% | 0.0% | 45.1% | bird (9) |
| wader | 382 | 85.6% (81.9 to 89.3) | 83.2% | 91.8% | 87.5% | 0.0% | 0.0% | 44.0% | bird (42) |
| bird | 531 | 87.0% (84.0 to 89.8) | 77.8% | 95.4% | 91.5% | 0.0% | 0.0% | 27.9% | wader (25) |
| alligator | 110 | 65.5% (56.4 to 74.6) | 53.6% | 86.4% | 74.5% | 0.0% | 0.0% | 46.4% | reptile (20) |
| reptile | 268 | 73.9% (68.7 to 79.1) | 67.5% | 91.7% | 88.5% | 0.0% | 0.0% | 6.3% | insect (36) |
| frog | 97 | 79.4% (71.1 to 86.6) | 64.9% | 96.8% | 88.2% | 0.0% | 0.0% | 2.1% | insect (13) |
| bee | 126 | 67.5% (59.5 to 75.4) | 69.8% | 80.7% | 86.8% | 0.0% | 0.0% | 11.1% | insect (28) |
| insect | 962 | 93.8% (92.2 to 95.2) | 87.0% | 97.3% | 98.4% | 0.0% | 0.0% | 10.3% | plant (21) |
| plant | 1223 | 97.6% (96.7 to 98.5) | 94.2% | 99.4% | 100.0% | 0.0% | 0.0% | 19.1% | insect (12) |
| other | 296 | 74.0% (68.9 to 79.0) | 67.9% | 84.1% | 87.4% | 0.0% | 0.0% | 16.2% | insect (55) |

The same photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 7 | 100.0% (100.0 to 100.0) | – |
| dog | 4 | 100.0% (100.0 to 100.0) | – |
| squirrel | 28 | 89.3% (75.0 to 100.0) | bird (1) |
| deer | 24 | 95.8% (87.5 to 100.0) | other (1) |
| rabbit | 22 | 100.0% (100.0 to 100.0) | – |
| hawk | 64 | 90.6% (82.8 to 96.9) | bird (5) |
| wader | 302 | 96.7% (94.7 to 98.7) | bird (9) |
| bird | 421 | 93.6% (91.2 to 96.0) | wader (20) |
| alligator | 52 | 98.1% (94.2 to 100.0) | reptile (1) |
| reptile | 171 | 97.1% (94.2 to 99.4) | alligator (4) |
| frog | 63 | 96.8% (92.1 to 100.0) | insect (2) |
| bee | 72 | 98.6% (95.8 to 100.0) | insect (1) |
| insect | 860 | 94.7% (93.1 to 96.0) | other (23) |
| plant | 1189 | 96.3% (95.1 to 97.3) | insect (13) |
| other | 180 | 93.9% (90.0 to 97.2) | insect (6) |

The kind of eye on the extra set's test photos (`images/coco-kinds.wasm-int8-per-channel`):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 98.8% (97.5 to 99.8) | 96.5% | 99.7% | 92.9% | 98.8% | 1.0% | 0.0% | none (4) |
| none | 500 | 97.0% (95.4 to 98.4) | 96.0% | 98.3% | 80.0% | 0.0% | 97.0% | 0.2% | plant (5) |
| cat | 77 | 90.9% (84.4 to 97.4) | 90.9% | 94.3% | 100.0% | 1.3% | 5.2% | 85.7% | none (4) |
| dog | 63 | 92.1% (84.1 to 98.4) | 71.4% | 93.3% | 94.4% | 0.0% | 0.0% | 4.8% | cat (5) |
| deer | 200 | 96.5% (94.0 to 99.0) | 86.0% | 98.8% | 96.4% | 1.5% | 0.0% | 60.0% | dog (3) |

The extra set's test photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 71 | 93.0% (85.9 to 98.6) | dog (3) |
| dog | 42 | 100.0% (100.0 to 100.0) | – |
| deer | 170 | 100.0% (100.0 to 100.0) | – |
| insect | 1 | 0.0% (0.0 to 0.0) | none (1) |
| plant | 5 | 0.0% (0.0 to 0.0) | none (5) |
| person | 387 | 99.5% (98.7 to 100.0) | deer (2) |
| none | 477 | 99.0% (97.9 to 99.8) | cat (4) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.44 | 96.4% (95.8 to 96.9) | 90.1% (89.1 to 91.0) | 73.2% (66.0 to 80.4) | 99.0% (98.4 to 99.5) | 97.3% (96.3 to 98.1) | 69.2% (46.2 to 92.3) |
| 95 in 100 | 0.69 | 82.4% (81.3 to 83.6) | 95.5% (94.7 to 96.1) | 89.3% (87.0 to 91.5) | 93.0% (91.5 to 94.3) | 98.4% (97.8 to 99.1) | 92.0% (85.1 to 97.7) |
| 98 in 100 | 0.85 | 69.9% (68.5 to 71.3) | 98.0% (97.5 to 98.5) | 92.7% (91.3 to 94.1) | 84.0% (82.0 to 86.1) | 99.1% (98.6 to 99.6) | 95.5% (92.4 to 98.5) |

## `alachua-pre2025-nc-tinyclip-39m-16-at90`

The slot holds the head `discriminant` for `tinyclip-39m-16` (shrinkage 0.03), fitted on `images/alachua-pre2025 (licence rule nc)`, with 5391 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 1, w_kind 0.7, alpha_prior 0.75. On 1803 tuning photos (val) the thresholds came out as name_at 0.80 and offer_at 0.88. On the 4197 test photos the kind of eye is right for 88.1% (87.1 to 89.1); the top species is right for 53.8% (52.2 to 55.4) and is among the first five for 75.1% (73.8 to 76.5). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind rows fitted on the fitting photos and the extra set (every photo counts the same)`. With kind_at 0.69 (set on wildlife tuning photos and the extra set's tuning third), the page asserts a kind for 82.4% (81.3 to 83.6) of the wildlife test photos and is right for 95.5% (94.7 to 96.1) of those; for the 17.6% (16.4 to 18.7) where it is not sure, the true kind is among its three likeliest for 89.3% (87.0 to 91.5). On the 1240 test photos of people, cats, dogs, grazing animals and rooms (`images/coco-kinds.wasm-int8-per-channel`), the kind is right for 96.9% (95.9 to 97.8); the page asserts a kind for 93.0% (91.5 to 94.3) and is right for 98.4% (97.8 to 99.1) of those; where it is not sure the true kind is among its three likeliest for 92.0% (85.1 to 97.7). A species is named on 15.7% (13.6 to 17.7) of these photos. The slot needs: species.bias_url (build 7 of the page); kinds.bias (build 7 of the page); fusion.rule mix (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 24.5% | the name is right for 90.4% (88.5 to 92.1); the kind for 97.6% (96.6 to 98.4) |
| three species to choose from | 12.0% | the three hold the species for 88.0% (85.3 to 90.8); the kind is right for 96.0% (94.2 to 97.6) |
| a kind of eye only | 63.5% | the kind is right for 83.0% (81.6 to 84.5) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.69):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 72.7% (45.5 to 100.0) | 63.6% | 100.0% | 75.0% | 0.0% | 0.0% | 63.6% | bird (1) |
| dog | 6 | 83.3% (50.0 to 100.0) | 66.7% | 100.0% | 50.0% | 0.0% | 0.0% | 66.7% | squirrel (1) |
| squirrel | 36 | 88.9% (77.8 to 97.2) | 69.4% | 100.0% | 72.7% | 0.0% | 0.0% | 63.9% | bird (1) |
| deer | 36 | 77.8% (63.9 to 88.9) | 69.4% | 92.0% | 54.5% | 0.0% | 0.0% | 63.9% | other (3) |
| rabbit | 31 | 77.4% (61.3 to 90.3) | 74.2% | 95.7% | 75.0% | 0.0% | 0.0% | 58.1% | other (3) |
| hawk | 82 | 80.5% (72.0 to 89.0) | 76.8% | 92.1% | 84.2% | 0.0% | 0.0% | 48.8% | bird (9) |
| wader | 382 | 85.6% (81.9 to 89.3) | 83.2% | 91.8% | 87.5% | 0.0% | 0.0% | 48.4% | bird (42) |
| bird | 531 | 87.0% (84.0 to 89.8) | 77.8% | 95.4% | 91.5% | 0.0% | 0.0% | 32.6% | wader (25) |
| alligator | 110 | 65.5% (56.4 to 74.6) | 53.6% | 86.4% | 74.5% | 0.0% | 0.0% | 46.4% | reptile (20) |
| reptile | 268 | 73.9% (68.7 to 79.1) | 67.5% | 91.7% | 88.5% | 0.0% | 0.0% | 9.3% | insect (36) |
| frog | 97 | 79.4% (71.1 to 86.6) | 64.9% | 96.8% | 88.2% | 0.0% | 0.0% | 3.1% | insect (13) |
| bee | 126 | 67.5% (59.5 to 75.4) | 69.8% | 80.7% | 86.8% | 0.0% | 0.0% | 14.3% | insect (28) |
| insect | 962 | 93.8% (92.2 to 95.2) | 87.0% | 97.3% | 98.4% | 0.0% | 0.0% | 13.3% | plant (21) |
| plant | 1223 | 97.6% (96.7 to 98.5) | 94.2% | 99.4% | 100.0% | 0.0% | 0.0% | 22.0% | insect (12) |
| other | 296 | 74.0% (68.9 to 79.0) | 67.9% | 84.1% | 87.4% | 0.0% | 0.0% | 20.6% | insect (55) |

The same photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 7 | 100.0% (100.0 to 100.0) | – |
| dog | 4 | 100.0% (100.0 to 100.0) | – |
| squirrel | 28 | 89.3% (75.0 to 100.0) | bird (1) |
| deer | 24 | 95.8% (87.5 to 100.0) | other (1) |
| rabbit | 22 | 100.0% (100.0 to 100.0) | – |
| hawk | 64 | 90.6% (82.8 to 96.9) | bird (5) |
| wader | 302 | 96.7% (94.7 to 98.7) | bird (9) |
| bird | 421 | 93.6% (91.2 to 96.0) | wader (20) |
| alligator | 52 | 98.1% (94.2 to 100.0) | reptile (1) |
| reptile | 171 | 97.1% (94.2 to 99.4) | alligator (4) |
| frog | 63 | 96.8% (92.1 to 100.0) | insect (2) |
| bee | 72 | 98.6% (95.8 to 100.0) | insect (1) |
| insect | 860 | 94.7% (93.1 to 96.0) | other (23) |
| plant | 1189 | 96.3% (95.1 to 97.3) | insect (13) |
| other | 180 | 93.9% (90.0 to 97.2) | insect (6) |

The kind of eye on the extra set's test photos (`images/coco-kinds.wasm-int8-per-channel`):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 98.8% (97.5 to 99.8) | 96.5% | 99.7% | 92.9% | 98.8% | 1.0% | 0.0% | none (4) |
| none | 500 | 97.0% (95.4 to 98.4) | 96.0% | 98.3% | 80.0% | 0.0% | 97.0% | 0.2% | plant (5) |
| cat | 77 | 90.9% (84.4 to 97.4) | 90.9% | 94.3% | 100.0% | 1.3% | 5.2% | 85.7% | none (4) |
| dog | 63 | 92.1% (84.1 to 98.4) | 71.4% | 93.3% | 94.4% | 0.0% | 0.0% | 4.8% | cat (5) |
| deer | 200 | 96.5% (94.0 to 99.0) | 86.0% | 98.8% | 96.4% | 1.5% | 0.0% | 62.0% | dog (3) |

The extra set's test photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 71 | 93.0% (85.9 to 98.6) | dog (3) |
| dog | 42 | 100.0% (100.0 to 100.0) | – |
| deer | 170 | 100.0% (100.0 to 100.0) | – |
| insect | 1 | 0.0% (0.0 to 0.0) | none (1) |
| plant | 5 | 0.0% (0.0 to 0.0) | none (5) |
| person | 387 | 99.5% (98.7 to 100.0) | deer (2) |
| none | 477 | 99.0% (97.9 to 99.8) | cat (4) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.44 | 96.4% (95.8 to 96.9) | 90.1% (89.1 to 91.0) | 73.2% (66.0 to 80.4) | 99.0% (98.4 to 99.5) | 97.3% (96.3 to 98.1) | 69.2% (46.2 to 92.3) |
| 95 in 100 | 0.69 | 82.4% (81.3 to 83.6) | 95.5% (94.7 to 96.1) | 89.3% (87.0 to 91.5) | 93.0% (91.5 to 94.3) | 98.4% (97.8 to 99.1) | 92.0% (85.1 to 97.7) |
| 98 in 100 | 0.85 | 69.9% (68.5 to 71.3) | 98.0% (97.5 to 98.5) | 92.7% (91.3 to 94.1) | 84.0% (82.0 to 86.1) | 99.1% (98.6 to 99.6) | 95.5% (92.4 to 98.5) |

## `alachua-pre2025-tinyclip-39m-16`

The slot holds the head `discriminant` for `tinyclip-39m-16` (shrinkage 0.03), fitted on `images/alachua-pre2025`, with 5467 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 0.5, w_kind 0.7, alpha_prior 0.6. On 1803 tuning photos (val) the thresholds came out as name_at 0.82 and offer_at 0.98. On the 4197 test photos the kind of eye is right for 88.5% (87.5 to 89.5); the top species is right for 53.4% (51.9 to 55.0) and is among the first five for 75.1% (73.8 to 76.5). `person` was said for 0.00% of these photos and `none` for 0.02%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind rows fitted on the fitting photos and the extra set (every photo counts the same)`. With kind_at 0.51 (set on wildlife tuning photos and the extra set's tuning third), the page asserts a kind for 84.8% (83.7 to 85.9) of the wildlife test photos and is right for 95.0% (94.2 to 95.7) of those; for the 15.2% (14.1 to 16.3) where it is not sure, the true kind is among its three likeliest for 86.1% (83.4 to 88.6). On the 1240 test photos of people, cats, dogs, grazing animals and rooms (`images/coco-kinds.wasm-int8-per-channel`), the kind is right for 97.4% (96.5 to 98.2); the page asserts a kind for 95.5% (94.2 to 96.7) and is right for 98.9% (98.3 to 99.5) of those; where it is not sure the true kind is among its three likeliest for 94.6% (87.5 to 100.0). A species is named on 16.1% (14.1 to 18.2) of these photos. The slot needs: species.bias_url (build 7 of the page); kinds.bias (build 7 of the page); fusion.rule mix (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 24.9% | the name is right for 88.2% (86.2 to 90.0); the kind for 95.3% (94.1 to 96.5) |
| three species to choose from | 2.7% | the three hold the species for 92.1% (86.8 to 96.5); the kind is right for 98.2% (95.6 to 100.0) |
| a kind of eye only | 72.4% | the kind is right for 85.8% (84.6 to 87.0) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.51):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 63.6% (36.4 to 90.9) | 54.5% | 100.0% | 60.0% | 0.0% | 0.0% | 63.6% | insect (2) |
| dog | 6 | 83.3% (50.0 to 100.0) | 66.7% | 100.0% | 50.0% | 0.0% | 0.0% | 83.3% | squirrel (1) |
| squirrel | 36 | 86.1% (75.0 to 97.2) | 75.0% | 100.0% | 66.7% | 0.0% | 0.0% | 75.0% | bird (2) |
| deer | 36 | 75.0% (61.1 to 88.9) | 72.2% | 92.3% | 50.0% | 0.0% | 0.0% | 69.4% | other (4) |
| rabbit | 31 | 77.4% (61.3 to 90.3) | 74.2% | 95.7% | 75.0% | 0.0% | 0.0% | 51.6% | squirrel (3) |
| hawk | 82 | 80.5% (72.0 to 89.0) | 78.0% | 90.6% | 72.2% | 0.0% | 0.0% | 51.2% | bird (7) |
| wader | 382 | 84.8% (81.2 to 88.5) | 87.4% | 91.6% | 83.3% | 0.0% | 0.0% | 50.5% | bird (41) |
| bird | 531 | 86.8% (83.6 to 89.6) | 78.9% | 94.3% | 85.7% | 0.0% | 0.2% | 33.1% | wader (18) |
| alligator | 110 | 74.6% (66.4 to 82.7) | 61.8% | 89.7% | 64.3% | 0.0% | 0.0% | 70.0% | reptile (10) |
| reptile | 268 | 73.9% (68.7 to 79.1) | 66.4% | 93.3% | 86.7% | 0.0% | 0.0% | 7.8% | insect (38) |
| frog | 97 | 78.3% (70.1 to 85.6) | 69.1% | 91.0% | 83.3% | 0.0% | 0.0% | 2.1% | insect (13) |
| bee | 126 | 71.4% (63.5 to 79.4) | 84.1% | 77.4% | 85.0% | 0.0% | 0.0% | 18.3% | insect (22) |
| insect | 962 | 94.4% (92.9 to 95.8) | 89.0% | 96.8% | 99.1% | 0.0% | 0.0% | 11.3% | plant (25) |
| plant | 1223 | 98.0% (97.2 to 98.8) | 95.3% | 99.5% | 100.0% | 0.0% | 0.0% | 21.2% | insect (9) |
| other | 296 | 73.3% (68.2 to 78.4) | 72.6% | 83.7% | 86.4% | 0.0% | 0.0% | 20.9% | insect (61) |

The same photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 6 | 100.0% (100.0 to 100.0) | – |
| dog | 4 | 100.0% (100.0 to 100.0) | – |
| squirrel | 30 | 90.0% (80.0 to 100.0) | bird (1) |
| deer | 25 | 96.0% (88.0 to 100.0) | other (1) |
| rabbit | 22 | 100.0% (100.0 to 100.0) | – |
| hawk | 66 | 87.9% (80.3 to 95.5) | bird (7) |
| wader | 320 | 95.6% (93.1 to 97.8) | bird (13) |
| bird | 423 | 93.4% (91.0 to 95.7) | wader (22) |
| alligator | 62 | 98.4% (95.2 to 100.0) | reptile (1) |
| reptile | 174 | 95.4% (92.0 to 98.3) | alligator (6) |
| frog | 63 | 96.8% (92.1 to 100.0) | insect (2) |
| bee | 85 | 96.5% (91.8 to 100.0) | insect (3) |
| insect | 883 | 93.9% (92.3 to 95.4) | other (25) |
| plant | 1204 | 96.3% (95.2 to 97.3) | insect (14) |
| other | 191 | 94.2% (90.6 to 97.4) | insect (7) |

The kind of eye on the extra set's test photos (`images/coco-kinds.wasm-int8-per-channel`):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 99.2% (98.2 to 100.0) | 97.5% | 99.7% | 100.0% | 99.2% | 0.5% | 0.0% | none (2) |
| none | 500 | 97.8% (96.4 to 99.0) | 95.4% | 99.4% | 91.3% | 0.4% | 97.8% | 0.2% | cat (3) |
| cat | 77 | 90.9% (84.4 to 97.4) | 90.9% | 97.1% | 85.7% | 1.3% | 3.9% | 90.9% | none (3) |
| dog | 63 | 90.5% (82.5 to 96.8) | 88.9% | 92.9% | 100.0% | 0.0% | 0.0% | 7.9% | cat (6) |
| deer | 200 | 97.5% (95.0 to 99.5) | 95.5% | 98.4% | 100.0% | 1.0% | 0.5% | 62.0% | person (2) |

The extra set's test photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 74 | 91.9% (85.1 to 97.3) | dog (4) |
| dog | 53 | 98.1% (94.3 to 100.0) | deer (1) |
| deer | 188 | 100.0% (100.0 to 100.0) | – |
| plant | 1 | 0.0% (0.0 to 0.0) | none (1) |
| person | 391 | 99.5% (98.7 to 100.0) | deer (2) |
| none | 477 | 99.4% (98.5 to 100.0) | cat (2) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.32 | 96.9% (96.3 to 97.4) | 90.4% (89.5 to 91.3) | 62.9% (54.5 to 71.2) | 99.4% (99.0 to 99.8) | 97.7% (96.8 to 98.5) | 71.4% (42.9 to 100.0) |
| 95 in 100 | 0.51 | 84.8% (83.7 to 85.9) | 95.0% (94.2 to 95.7) | 86.1% (83.4 to 88.6) | 95.5% (94.2 to 96.7) | 98.9% (98.3 to 99.5) | 94.6% (87.5 to 100.0) |
| 98 in 100 | 0.64 | 71.9% (70.6 to 73.2) | 97.8% (97.2 to 98.3) | 91.2% (89.6 to 92.7) | 87.7% (85.9 to 89.6) | 99.5% (99.1 to 99.9) | 96.0% (92.8 to 98.7) |

## `alachua-pre2025-tinyclip-8m-16`

The slot holds the head `discriminant` for `tinyclip-8m-16` (shrinkage 0.3), fitted on `images/alachua-pre2025`, with 5467 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 1, w_kind 0.7, alpha_prior 0.5. On 1803 tuning photos (val) the thresholds came out as name_at 0.90 and offer_at 0.97. On the 4197 test photos the kind of eye is right for 80.3% (79.0 to 81.6); the top species is right for 42.5% (41.0 to 44.0) and is among the first five for 65.5% (64.1 to 66.9). `person` was said for 0.02% of these photos and `none` for 0.05%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind rows fitted on the fitting photos and the extra set (every photo counts the same)`. With kind_at 0.82 (set on wildlife tuning photos and the extra set's tuning third), the page asserts a kind for 58.5% (56.9 to 60.0) of the wildlife test photos and is right for 96.2% (95.4 to 96.9) of those; for the 41.5% (40.0 to 43.1) where it is not sure, the true kind is among its three likeliest for 91.5% (90.1 to 92.7). On the 1240 test photos of people, cats, dogs, grazing animals and rooms (`images/coco-kinds.wasm-int8-per-channel`), the kind is right for 95.4% (94.2 to 96.5); the page asserts a kind for 86.8% (84.8 to 88.7) and is right for 98.9% (98.2 to 99.4) of those; where it is not sure the true kind is among its three likeliest for 92.7% (88.4 to 96.3). A species is named on 15.7% (13.7 to 17.7) of these photos. The slot needs: species.bias_url (build 7 of the page); kinds.bias (build 7 of the page); fusion.rule mix (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 7.0% | the name is right for 87.5% (83.8 to 91.2); the kind for 92.9% (89.9 to 95.6) |
| three species to choose from | 2.2% | the three hold the species for 92.5% (86.2 to 96.8); the kind is right for 95.7% (91.5 to 98.9) |
| a kind of eye only | 90.7% | the kind is right for 79.0% (77.7 to 80.2) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.82):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 72.7% (45.5 to 100.0) | 18.2% | 100.0% | 100.0% | 0.0% | 9.1% | 54.5% | other (2) |
| dog | 6 | 50.0% (16.7 to 83.3) | 33.3% | 50.0% | 75.0% | 0.0% | 0.0% | 50.0% | deer (2) |
| squirrel | 36 | 61.1% (47.2 to 77.8) | 33.3% | 100.0% | 70.8% | 0.0% | 0.0% | 38.9% | bird (4) |
| deer | 36 | 75.0% (58.3 to 88.9) | 58.3% | 95.2% | 53.3% | 0.0% | 0.0% | 66.7% | plant (3) |
| rabbit | 31 | 74.2% (58.1 to 90.3) | 54.8% | 100.0% | 71.4% | 0.0% | 0.0% | 25.8% | squirrel (4) |
| hawk | 82 | 70.7% (61.0 to 80.5) | 28.0% | 91.3% | 83.1% | 0.0% | 0.0% | 6.1% | bird (14) |
| wader | 382 | 72.5% (67.8 to 77.0) | 54.5% | 91.8% | 91.4% | 0.0% | 0.0% | 17.3% | bird (75) |
| bird | 531 | 82.1% (78.9 to 85.3) | 54.2% | 98.6% | 90.9% | 0.2% | 0.2% | 7.0% | wader (33) |
| alligator | 110 | 55.5% (46.4 to 65.5) | 25.5% | 85.7% | 76.8% | 0.0% | 0.0% | 40.0% | reptile (23) |
| reptile | 268 | 51.5% (45.5 to 57.1) | 24.6% | 90.9% | 87.6% | 0.0% | 0.0% | 1.5% | insect (79) |
| frog | 97 | 52.6% (43.3 to 62.9) | 25.8% | 84.0% | 80.6% | 0.0% | 0.0% | 0.0% | insect (35) |
| bee | 126 | 44.4% (35.7 to 53.2) | 19.8% | 40.0% | 97.0% | 0.0% | 0.0% | 4.8% | insect (51) |
| insect | 962 | 89.0% (86.9 to 90.8) | 57.0% | 97.4% | 98.8% | 0.0% | 0.0% | 0.4% | plant (43) |
| plant | 1223 | 96.2% (95.1 to 97.3) | 87.9% | 99.3% | 95.9% | 0.0% | 0.0% | 4.7% | insect (19) |
| other | 296 | 60.5% (54.7 to 65.9) | 38.2% | 84.1% | 94.0% | 0.0% | 0.0% | 5.7% | insect (85) |

The same photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 2 | 100.0% (100.0 to 100.0) | – |
| dog | 1 | 100.0% (100.0 to 100.0) | – |
| squirrel | 12 | 100.0% (100.0 to 100.0) | – |
| deer | 22 | 90.9% (77.3 to 100.0) | dog (1) |
| rabbit | 17 | 100.0% (100.0 to 100.0) | – |
| hawk | 23 | 91.3% (78.3 to 100.0) | bird (1) |
| wader | 193 | 99.0% (97.4 to 100.0) | bird (2) |
| bird | 301 | 94.3% (91.7 to 96.7) | wader (13) |
| alligator | 24 | 100.0% (100.0 to 100.0) | – |
| reptile | 64 | 93.8% (87.5 to 98.4) | alligator (4) |
| frog | 21 | 100.0% (100.0 to 100.0) | – |
| bee | 11 | 90.9% (72.7 to 100.0) | insect (1) |
| insect | 559 | 95.5% (93.7 to 97.1) | other (12) |
| plant | 1102 | 96.9% (95.8 to 97.8) | insect (12) |
| other | 101 | 94.1% (89.1 to 98.0) | plant (3) |

The kind of eye on the extra set's test photos (`images/coco-kinds.wasm-int8-per-channel`):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 98.2% (96.8 to 99.5) | 96.0% | 99.5% | 93.8% | 98.2% | 1.2% | 0.0% | none (5) |
| none | 500 | 96.0% (94.2 to 97.6) | 93.0% | 99.8% | 82.9% | 0.4% | 96.0% | 0.0% | dog (6) |
| cat | 77 | 90.9% (84.4 to 97.4) | 88.3% | 94.1% | 77.8% | 1.3% | 5.2% | 85.7% | none (4) |
| dog | 63 | 82.5% (73.0 to 92.1) | 4.8% | 0.0% | 98.3% | 0.0% | 0.0% | 11.1% | cat (8) |
| deer | 200 | 94.0% (90.5 to 97.0) | 78.0% | 98.7% | 95.5% | 1.5% | 0.0% | 60.5% | dog (8) |

The extra set's test photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 67 | 95.5% (89.5 to 100.0) | dog (3) |
| dog | 1 | 0.0% (0.0 to 0.0) | deer (1) |
| deer | 154 | 100.0% (100.0 to 100.0) | – |
| plant | 1 | 0.0% (0.0 to 0.0) | none (1) |
| person | 384 | 99.5% (98.7 to 100.0) | cat (1) |
| none | 469 | 98.9% (97.9 to 99.8) | cat (3) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.64 | 75.8% (74.6 to 77.1) | 90.7% (89.7 to 91.7) | 89.7% (87.8 to 91.4) | 94.3% (93.0 to 95.6) | 97.9% (97.0 to 98.6) | 88.6% (80.0 to 95.7) |
| 95 in 100 | 0.82 | 58.5% (56.9 to 60.0) | 96.2% (95.4 to 96.9) | 91.5% (90.1 to 92.7) | 86.8% (84.8 to 88.7) | 98.9% (98.2 to 99.4) | 92.7% (88.4 to 96.3) |
| 98 in 100 | 0.93 | 42.1% (40.6 to 43.7) | 98.6% (98.0 to 99.1) | 93.3% (92.3 to 94.3) | 80.7% (78.4 to 82.9) | 99.3% (98.7 to 99.8) | 93.8% (90.4 to 96.7) |

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

## `pocket-v3`

The slot holds the head `discriminant` for `tinyclip-39m-16` (shrinkage 0.03), fitted on `images/alachua-pre2025 (licence rule nc)`, with 5391 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 1, w_kind 0.7, alpha_prior 0.75. On 1803 tuning photos (val) the thresholds came out as name_at 0.86 and offer_at 0.86. On the 4197 test photos the kind of eye is right for 88.1% (87.1 to 89.1); the top species is right for 53.8% (52.2 to 55.4) and is among the first five for 75.1% (73.8 to 76.5). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind rows fitted on the fitting photos and the extra set (every photo counts the same)`. With kind_at 0.69 (set on wildlife tuning photos and the extra set's tuning third), the page asserts a kind for 82.4% (81.3 to 83.6) of the wildlife test photos and is right for 95.5% (94.7 to 96.1) of those; for the 17.6% (16.4 to 18.7) where it is not sure, the true kind is among its three likeliest for 89.3% (87.0 to 91.5). On the 1240 test photos of people, cats, dogs, grazing animals and rooms (`images/coco-kinds.wasm-int8-per-channel`), the kind is right for 96.9% (95.9 to 97.8); the page asserts a kind for 93.0% (91.5 to 94.3) and is right for 98.4% (97.8 to 99.1) of those; where it is not sure the true kind is among its three likeliest for 92.0% (85.1 to 97.7). A species is named on 15.3% (13.3 to 17.4) of these photos. The slot needs: species.bias_url (build 7 of the page); kinds.bias (build 7 of the page); fusion.rule mix (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 21.2% | the name is right for 91.8% (89.9 to 93.6); the kind for 97.9% (96.9 to 98.8) |
| three species to choose from | 16.6% | the three hold the species for 87.1% (84.5 to 89.5); the kind is right for 96.0% (94.5 to 97.4) |
| a kind of eye only | 62.2% | the kind is right for 82.7% (81.3 to 84.1) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.69):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 72.7% (45.5 to 100.0) | 63.6% | 100.0% | 75.0% | 0.0% | 0.0% | 63.6% | bird (1) |
| dog | 6 | 83.3% (50.0 to 100.0) | 66.7% | 100.0% | 50.0% | 0.0% | 0.0% | 50.0% | squirrel (1) |
| squirrel | 36 | 88.9% (77.8 to 97.2) | 69.4% | 100.0% | 72.7% | 0.0% | 0.0% | 63.9% | bird (1) |
| deer | 36 | 77.8% (63.9 to 88.9) | 69.4% | 92.0% | 54.5% | 0.0% | 0.0% | 63.9% | other (3) |
| rabbit | 31 | 77.4% (61.3 to 90.3) | 74.2% | 95.7% | 75.0% | 0.0% | 0.0% | 54.8% | other (3) |
| hawk | 82 | 80.5% (72.0 to 89.0) | 76.8% | 92.1% | 84.2% | 0.0% | 0.0% | 45.1% | bird (9) |
| wader | 382 | 85.6% (81.9 to 89.3) | 83.2% | 91.8% | 87.5% | 0.0% | 0.0% | 44.0% | bird (42) |
| bird | 531 | 87.0% (84.0 to 89.8) | 77.8% | 95.4% | 91.5% | 0.0% | 0.0% | 27.9% | wader (25) |
| alligator | 110 | 65.5% (56.4 to 74.6) | 53.6% | 86.4% | 74.5% | 0.0% | 0.0% | 46.4% | reptile (20) |
| reptile | 268 | 73.9% (68.7 to 79.1) | 67.5% | 91.7% | 88.5% | 0.0% | 0.0% | 6.3% | insect (36) |
| frog | 97 | 79.4% (71.1 to 86.6) | 64.9% | 96.8% | 88.2% | 0.0% | 0.0% | 2.1% | insect (13) |
| bee | 126 | 67.5% (59.5 to 75.4) | 69.8% | 80.7% | 86.8% | 0.0% | 0.0% | 11.1% | insect (28) |
| insect | 962 | 93.8% (92.2 to 95.2) | 87.0% | 97.3% | 98.4% | 0.0% | 0.0% | 10.3% | plant (21) |
| plant | 1223 | 97.6% (96.7 to 98.5) | 94.2% | 99.4% | 100.0% | 0.0% | 0.0% | 19.1% | insect (12) |
| other | 296 | 74.0% (68.9 to 79.0) | 67.9% | 84.1% | 87.4% | 0.0% | 0.0% | 16.2% | insect (55) |

The same photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 7 | 100.0% (100.0 to 100.0) | – |
| dog | 4 | 100.0% (100.0 to 100.0) | – |
| squirrel | 28 | 89.3% (75.0 to 100.0) | bird (1) |
| deer | 24 | 95.8% (87.5 to 100.0) | other (1) |
| rabbit | 22 | 100.0% (100.0 to 100.0) | – |
| hawk | 64 | 90.6% (82.8 to 96.9) | bird (5) |
| wader | 302 | 96.7% (94.7 to 98.7) | bird (9) |
| bird | 421 | 93.6% (91.2 to 96.0) | wader (20) |
| alligator | 52 | 98.1% (94.2 to 100.0) | reptile (1) |
| reptile | 171 | 97.1% (94.2 to 99.4) | alligator (4) |
| frog | 63 | 96.8% (92.1 to 100.0) | insect (2) |
| bee | 72 | 98.6% (95.8 to 100.0) | insect (1) |
| insect | 860 | 94.7% (93.1 to 96.0) | other (23) |
| plant | 1189 | 96.3% (95.1 to 97.3) | insect (13) |
| other | 180 | 93.9% (90.0 to 97.2) | insect (6) |

The kind of eye on the extra set's test photos (`images/coco-kinds.wasm-int8-per-channel`):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 98.8% (97.5 to 99.8) | 96.5% | 99.7% | 92.9% | 98.8% | 1.0% | 0.0% | none (4) |
| none | 500 | 97.0% (95.4 to 98.4) | 96.0% | 98.3% | 80.0% | 0.0% | 97.0% | 0.2% | plant (5) |
| cat | 77 | 90.9% (84.4 to 97.4) | 90.9% | 94.3% | 100.0% | 1.3% | 5.2% | 85.7% | none (4) |
| dog | 63 | 92.1% (84.1 to 98.4) | 71.4% | 93.3% | 94.4% | 0.0% | 0.0% | 4.8% | cat (5) |
| deer | 200 | 96.5% (94.0 to 99.0) | 86.0% | 98.8% | 96.4% | 1.5% | 0.0% | 60.0% | dog (3) |

The extra set's test photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 71 | 93.0% (85.9 to 98.6) | dog (3) |
| dog | 42 | 100.0% (100.0 to 100.0) | – |
| deer | 170 | 100.0% (100.0 to 100.0) | – |
| insect | 1 | 0.0% (0.0 to 0.0) | none (1) |
| plant | 5 | 0.0% (0.0 to 0.0) | none (5) |
| person | 387 | 99.5% (98.7 to 100.0) | deer (2) |
| none | 477 | 99.0% (97.9 to 99.8) | cat (4) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.44 | 96.4% (95.8 to 96.9) | 90.1% (89.1 to 91.0) | 73.2% (66.0 to 80.4) | 99.0% (98.4 to 99.5) | 97.3% (96.3 to 98.1) | 69.2% (46.2 to 92.3) |
| 95 in 100 | 0.69 | 82.4% (81.3 to 83.6) | 95.5% (94.7 to 96.1) | 89.3% (87.0 to 91.5) | 93.0% (91.5 to 94.3) | 98.4% (97.8 to 99.1) | 92.0% (85.1 to 97.7) |
| 98 in 100 | 0.85 | 69.9% (68.5 to 71.3) | 98.0% (97.5 to 98.5) | 92.7% (91.3 to 94.1) | 84.0% (82.0 to 86.1) | 99.1% (98.6 to 99.6) | 95.5% (92.4 to 98.5) |

## `sentences-bioclip2-l14`

The slot holds the head `sentences` for `bioclip2-l14` (species_sci), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 100, w_kind 0.5, alpha_prior 1. On 1803 tuning photos (val) the thresholds came out as name_at 0.05 and offer_at never (no level reached nine in ten). On the 4197 test photos the kind of eye is right for 98.0% (97.6 to 98.4); the top species is right for 92.5% (91.6 to 93.2) and is among the first five for 97.5% (97.0 to 97.9). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. No level of the winning kind's probability made asserted kinds right 95 times in 100 on the tuning photos, so the slot carries no kind_at. The slot needs: fusion.rule mix (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 98.5% | the name is right for 93.3% (92.5 to 94.0); the kind for 99.1% (98.7 to 99.3) |
| three species to choose from | 0.0% | the three hold the species for –; the kind is right for – |
| a kind of eye only | 1.5% | the kind is right for 29.0% (17.7 to 40.3) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at none):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 90.9% (72.7 to 100.0) | 100.0% | 90.9% | – | 0.0% | 0.0% | 90.9% | other (1) |
| dog | 6 | 83.3% (50.0 to 100.0) | 100.0% | 83.3% | – | 0.0% | 0.0% | 100.0% | squirrel (1) |
| squirrel | 36 | 94.4% (86.1 to 100.0) | 100.0% | 94.4% | – | 0.0% | 0.0% | 91.7% | other (2) |
| deer | 36 | 94.4% (86.1 to 100.0) | 100.0% | 94.4% | – | 0.0% | 0.0% | 94.4% | wader (2) |
| rabbit | 31 | 100.0% (100.0 to 100.0) | 100.0% | 100.0% | – | 0.0% | 0.0% | 100.0% | – |
| hawk | 82 | 96.3% (91.5 to 100.0) | 100.0% | 96.3% | – | 0.0% | 0.0% | 97.6% | bird (2) |
| wader | 382 | 99.0% (97.9 to 99.7) | 100.0% | 99.0% | – | 0.0% | 0.0% | 99.2% | bird (1) |
| bird | 531 | 96.0% (94.3 to 97.5) | 100.0% | 96.0% | – | 0.0% | 0.0% | 96.6% | other (10) |
| alligator | 110 | 97.3% (93.6 to 100.0) | 100.0% | 97.3% | – | 0.0% | 0.0% | 98.2% | other (3) |
| reptile | 268 | 97.8% (95.9 to 99.2) | 100.0% | 97.8% | – | 0.0% | 0.0% | 98.9% | other (4) |
| frog | 97 | 97.9% (94.8 to 100.0) | 100.0% | 97.9% | – | 0.0% | 0.0% | 99.0% | bird (1) |
| bee | 126 | 97.6% (94.4 to 100.0) | 100.0% | 97.6% | – | 0.0% | 0.0% | 95.2% | plant (2) |
| insect | 962 | 98.7% (97.9 to 99.3) | 100.0% | 98.6% | – | 0.0% | 0.0% | 99.2% | other (6) |
| plant | 1223 | 99.1% (98.5 to 99.6) | 100.0% | 99.1% | – | 0.0% | 0.0% | 99.6% | insect (7) |
| other | 296 | 96.3% (93.9 to 98.3) | 100.0% | 96.3% | – | 0.0% | 0.0% | 97.3% | insect (5) |

The same photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 10 | 100.0% (100.0 to 100.0) | – |
| dog | 5 | 100.0% (100.0 to 100.0) | – |
| squirrel | 36 | 94.4% (86.1 to 100.0) | dog (1) |
| deer | 35 | 97.1% (91.4 to 100.0) | wader (1) |
| rabbit | 31 | 100.0% (100.0 to 100.0) | – |
| hawk | 82 | 96.3% (91.5 to 100.0) | bird (2) |
| wader | 393 | 96.2% (94.2 to 98.0) | bird (7) |
| bird | 515 | 99.0% (98.1 to 99.8) | hawk (2) |
| alligator | 109 | 98.2% (95.4 to 100.0) | reptile (2) |
| reptile | 263 | 99.6% (98.9 to 100.0) | bird (1) |
| frog | 95 | 100.0% (100.0 to 100.0) | – |
| bee | 124 | 99.2% (97.6 to 100.0) | plant (1) |
| insect | 963 | 98.6% (97.7 to 99.3) | plant (7) |
| plant | 1225 | 98.9% (98.3 to 99.5) | insect (6) |
| other | 311 | 91.6% (88.4 to 94.5) | bird (10) |

The kind of eye on the extra set's test photos (`images/coco-kinds`):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 0.0% (0.0 to 0.0) | 100.0% | 0.0% | – | 0.0% | 0.0% | 31.5% | other (248) |
| none | 500 | 0.0% (0.0 to 0.0) | 100.0% | 0.0% | – | 0.0% | 0.0% | 38.2% | other (301) |
| cat | 77 | 85.7% (77.9 to 93.5) | 100.0% | 85.7% | – | 0.0% | 0.0% | 87.0% | other (8) |
| dog | 63 | 14.3% (6.3 to 23.8) | 100.0% | 14.3% | – | 0.0% | 0.0% | 36.5% | other (45) |
| deer | 200 | 68.0% (61.5 to 74.0) | 100.0% | 68.0% | – | 0.0% | 0.0% | 75.5% | wader (47) |

The extra set's test photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 71 | 93.0% (87.3 to 98.6) | dog (4) |
| dog | 9 | 100.0% (100.0 to 100.0) | – |
| squirrel | 1 | 0.0% (0.0 to 0.0) | none (1) |
| deer | 138 | 98.6% (96.4 to 100.0) | dog (1) |
| rabbit | 1 | 0.0% (0.0 to 0.0) | dog (1) |
| hawk | 2 | 0.0% (0.0 to 0.0) | none (2) |
| wader | 93 | 0.0% (0.0 to 0.0) | deer (47) |
| bird | 68 | 0.0% (0.0 to 0.0) | none (41) |
| reptile | 13 | 0.0% (0.0 to 0.0) | person (9) |
| frog | 1 | 0.0% (0.0 to 0.0) | none (1) |
| insect | 107 | 0.0% (0.0 to 0.0) | person (77) |
| plant | 120 | 0.0% (0.0 to 0.0) | none (88) |
| other | 616 | 0.0% (0.0 to 0.0) | none (301) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | no level reached it | – | – | – | – | – | – |
| 95 in 100 | no level reached it | – | – | – | – | – | – |
| 98 in 100 | no level reached it | – | – | – | – | – | – |

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

The slot holds the head `sentences` for `tinyclip-8m-16` (species_com), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 100, w_kind 0.5, alpha_prior 1. On 1803 tuning photos (val) the thresholds came out as name_at 0.56 and offer_at 0.63. On the 4197 test photos the kind of eye is right for 77.3% (76.0 to 78.6); the top species is right for 26.4% (25.1 to 27.8) and is among the first five for 45.4% (43.9 to 46.9). `person` was said for 0.07% of these photos and `none` for 0.26%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind phrases`. With kind_at 0.80 (set on wildlife tuning photos and the extra set's tuning third), the page asserts a kind for 42.5% (41.0 to 44.1) of the wildlife test photos and is right for 97.4% (96.7 to 98.2) of those; for the 57.5% (55.9 to 59.0) where it is not sure, the true kind is among its three likeliest for 91.4% (90.2 to 92.5). On the 1240 test photos of people, cats, dogs, grazing animals and rooms (`images/coco-kinds.wasm-int8-per-channel`), the kind is right for 83.2% (81.0 to 85.2); the page asserts a kind for 28.1% (25.7 to 30.6) and is right for 96.9% (94.8 to 98.6) of those; where it is not sure the true kind is among its three likeliest for 90.2% (88.3 to 92.2). A species is named on 1.1% (0.6 to 1.6) of these photos. The slot needs: fusion.rule mix (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

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
| plant | 1223 | 95.3% (94.1 to 96.5) | 69.5% | 100.0% | 98.4% | 0.1% | 0.0% | 4.2% | insect (35) |
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
| plant | 862 | 98.6% (97.8 to 99.3) | insect (4) |
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
| 95 in 100 | 0.80 | 42.5% (41.0 to 44.1) | 97.4% (96.7 to 98.2) | 91.4% (90.2 to 92.5) | 28.1% (25.7 to 30.6) | 96.9% (94.8 to 98.6) | 90.2% (88.3 to 92.2) |
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

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.20 | 100.0% (99.9 to 100.0) | 98.6% (98.2 to 99.0) | 50.0% (0.0 to 100.0) | – | – | – |
| 95 in 100 | 0.20 | 100.0% (99.9 to 100.0) | 98.6% (98.2 to 99.0) | 50.0% (0.0 to 100.0) | – | – | – |
| 98 in 100 | 0.20 | 100.0% (99.9 to 100.0) | 98.6% (98.2 to 99.0) | 50.0% (0.0 to 100.0) | – | – | – |

## `val-tinyclip-39m-16`

The slot holds the head `prototypes + sentences` for `tinyclip-39m-16` (species_taxon_com, beta 8, bias for species without photos 0.8), fitted on `images/alachua-2025 (two thirds of val)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 0.5, w_kind 0.7, alpha_prior 1. On 565 tuning photos (the third of val kept for tuning) the thresholds came out as name_at 0.90 and offer_at 0.94. On the 4197 test photos the kind of eye is right for 87.3% (86.3 to 88.3); the top species is right for 36.3% (34.9 to 37.8) and is among the first five for 58.8% (57.2 to 60.2). `person` was said for 0.07% of these photos and `none` for 0.07%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind rows fitted on the fitting photos and the extra set (a kind's photos weighted by the inverse square root of their number)`. With kind_at 0.50 (set on wildlife tuning photos and the extra set's tuning third), the page asserts a kind for 78.8% (77.6 to 80.1) of the wildlife test photos and is right for 95.5% (94.8 to 96.1) of those; for the 21.2% (19.9 to 22.4) where it is not sure, the true kind is among its three likeliest for 90.5% (88.5 to 92.4). On the 1240 test photos of people, cats, dogs, grazing animals and rooms (`images/coco-kinds.wasm-int8-per-channel`), the kind is right for 98.2% (97.3 to 98.8); the page asserts a kind for 95.5% (94.3 to 96.6) and is right for 99.2% (98.7 to 99.7) of those; where it is not sure the true kind is among its three likeliest for 94.6% (89.3 to 100.0). A species is named on 6.2% (4.9 to 7.7) of these photos. The slot needs: species.bias_url (build 7 of the page); kinds.bias (build 7 of the page); fusion.rule mix (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 14.2% | the name is right for 92.0% (89.6 to 94.0); the kind for 98.5% (97.5 to 99.3) |
| three species to choose from | 7.3% | the three hold the species for 90.3% (86.7 to 93.5); the kind is right for 97.7% (95.8 to 99.4) |
| a kind of eye only | 78.5% | the kind is right for 84.3% (83.0 to 85.6) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.50):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 63.6% (36.4 to 90.9) | 63.6% | 85.7% | 25.0% | 0.0% | 9.1% | 27.3% | plant (2) |
| dog | 6 | 50.0% (16.7 to 83.3) | 0.0% | – | 66.7% | 0.0% | 0.0% | 33.3% | deer (1) |
| squirrel | 36 | 80.6% (66.7 to 91.7) | 52.8% | 94.7% | 70.6% | 0.0% | 0.0% | 58.3% | wader (3) |
| deer | 36 | 69.4% (52.8 to 83.3) | 58.3% | 95.2% | 53.3% | 0.0% | 0.0% | 52.8% | plant (5) |
| rabbit | 31 | 87.1% (74.2 to 96.8) | 51.6% | 100.0% | 86.7% | 0.0% | 0.0% | 45.2% | wader (2) |
| hawk | 82 | 74.4% (64.6 to 84.2) | 68.3% | 92.9% | 92.3% | 0.0% | 0.0% | 36.6% | bird (12) |
| wader | 382 | 85.6% (81.9 to 89.0) | 84.0% | 93.5% | 88.5% | 0.0% | 0.0% | 35.1% | bird (38) |
| bird | 531 | 84.9% (81.7 to 87.9) | 71.8% | 96.6% | 94.7% | 0.2% | 0.2% | 23.2% | wader (35) |
| alligator | 110 | 81.8% (74.6 to 89.1) | 77.3% | 96.5% | 72.0% | 0.0% | 0.0% | 67.3% | plant (7) |
| reptile | 268 | 83.6% (79.1 to 87.7) | 68.7% | 93.5% | 86.9% | 0.4% | 0.0% | 14.2% | plant (17) |
| frog | 97 | 80.4% (72.2 to 87.6) | 68.0% | 97.0% | 77.4% | 0.0% | 0.0% | 3.1% | reptile (10) |
| bee | 126 | 60.3% (51.6 to 69.0) | 69.0% | 72.4% | 89.7% | 0.0% | 0.0% | 3.2% | insect (34) |
| insect | 962 | 88.4% (86.3 to 90.2) | 78.2% | 95.1% | 97.1% | 0.1% | 0.0% | 4.9% | plant (42) |
| plant | 1223 | 98.3% (97.5 to 99.0) | 93.4% | 99.5% | 97.5% | 0.0% | 0.0% | 6.4% | insect (11) |
| other | 296 | 72.0% (66.9 to 77.0) | 57.4% | 85.3% | 90.5% | 0.0% | 0.3% | 2.0% | insect (41) |

The same photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 6 | 100.0% (100.0 to 100.0) | – |
| squirrel | 21 | 85.7% (71.4 to 100.0) | cat (1) |
| deer | 20 | 100.0% (100.0 to 100.0) | – |
| rabbit | 16 | 100.0% (100.0 to 100.0) | – |
| hawk | 54 | 96.3% (90.7 to 100.0) | bird (1) |
| wader | 313 | 95.9% (93.3 to 97.8) | bird (11) |
| bird | 388 | 94.8% (92.5 to 96.9) | wader (16) |
| alligator | 83 | 98.8% (96.4 to 100.0) | reptile (1) |
| reptile | 186 | 92.5% (88.7 to 96.2) | other (5) |
| frog | 67 | 95.5% (89.5 to 100.0) | insect (2) |
| bee | 67 | 94.0% (88.1 to 98.5) | insect (3) |
| insect | 747 | 95.7% (94.2 to 97.2) | bee (16) |
| plant | 1179 | 96.4% (95.2 to 97.4) | insect (14) |
| other | 160 | 90.6% (85.6 to 95.0) | insect (13) |

The kind of eye on the extra set's test photos (`images/coco-kinds.wasm-int8-per-channel`):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 99.5% (98.8 to 100.0) | 98.5% | 99.7% | 100.0% | 99.5% | 0.2% | 0.0% | none (1) |
| none | 500 | 98.6% (97.4 to 99.6) | 95.0% | 100.0% | 100.0% | 0.0% | 98.6% | 0.0% | cat (3) |
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
| none | 477 | 99.6% (99.0 to 100.0) | cat (2) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.31 | 96.0% (95.4 to 96.6) | 89.5% (88.5 to 90.5) | 79.3% (73.4 to 85.2) | 99.4% (98.9 to 99.8) | 98.6% (97.9 to 99.3) | 87.5% (62.5 to 100.0) |
| 95 in 100 | 0.50 | 78.8% (77.6 to 80.1) | 95.5% (94.8 to 96.1) | 90.5% (88.5 to 92.4) | 95.5% (94.3 to 96.6) | 99.2% (98.7 to 99.7) | 94.6% (89.3 to 100.0) |
| 98 in 100 | 0.63 | 62.4% (60.9 to 63.9) | 97.6% (97.1 to 98.2) | 93.7% (92.5 to 94.9) | 85.8% (83.9 to 87.8) | 99.8% (99.5 to 100.0) | 97.2% (94.3 to 99.4) |

## `val-tinyclip-8m-16`

The slot holds the head `discriminant + sentences` for `tinyclip-8m-16` (shrinkage 0.03, species_com, gamma 1), fitted on `images/alachua-2025 (two thirds of val)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 0.5, w_kind 0.5, alpha_prior 0.5. On 565 tuning photos (the third of val kept for tuning) the thresholds came out as name_at never (no level reached nine in ten) and offer_at 0.24. On the 4197 test photos the kind of eye is right for 79.5% (78.3 to 80.8); the top species is right for 25.3% (24.0 to 26.6) and is among the first five for 45.5% (44.0 to 47.0). `person` was said for 0.14% of these photos and `none` for 0.21%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind rows fitted on the fitting photos and the extra set (every kind counts the same)`. With kind_at 0.53 (set on wildlife tuning photos and the extra set's tuning third), the page asserts a kind for 52.6% (51.1 to 54.2) of the wildlife test photos and is right for 95.4% (94.5 to 96.2) of those; for the 47.4% (45.8 to 48.9) where it is not sure, the true kind is among its three likeliest for 88.9% (87.5 to 90.2). On the 1240 test photos of people, cats, dogs, grazing animals and rooms (`images/coco-kinds.wasm-int8-per-channel`), the kind is right for 96.4% (95.3 to 97.4); the page asserts a kind for 70.2% (67.6 to 72.7) and is right for 99.3% (98.7 to 99.8) of those; where it is not sure the true kind is among its three likeliest for 94.6% (92.2 to 96.8). A species is named on 0.0% (0.0 to 0.0) of these photos. The slot needs: species.bias_url (build 7 of the page); kinds.bias (build 7 of the page); fusion.rule mix (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 0.0% | the name is right for –; the kind for – |
| three species to choose from | 15.8% | the three hold the species for 83.0% (80.1 to 85.7); the kind is right for 97.4% (96.2 to 98.5) |
| a kind of eye only | 84.2% | the kind is right for 76.1% (74.7 to 77.6) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.53):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 45.5% (18.2 to 72.7) | 0.0% | – | 63.6% | 0.0% | 9.1% | 0.0% | plant (3) |
| dog | 6 | 0.0% (0.0 to 0.0) | 0.0% | – | 16.7% | 0.0% | 0.0% | 0.0% | insect (2) |
| squirrel | 36 | 52.8% (38.9 to 69.4) | 16.7% | 100.0% | 60.0% | 0.0% | 0.0% | 0.0% | plant (6) |
| deer | 36 | 69.4% (52.8 to 83.3) | 5.6% | 50.0% | 70.6% | 0.0% | 0.0% | 0.0% | plant (6) |
| rabbit | 31 | 64.5% (45.2 to 80.7) | 35.5% | 100.0% | 60.0% | 0.0% | 0.0% | 0.0% | squirrel (6) |
| hawk | 82 | 50.0% (39.0 to 61.0) | 20.7% | 88.2% | 75.4% | 0.0% | 0.0% | 0.0% | bird (25) |
| wader | 382 | 74.6% (70.2 to 78.8) | 50.8% | 94.8% | 87.2% | 0.0% | 0.0% | 0.0% | bird (70) |
| bird | 531 | 79.7% (76.3 to 83.0) | 36.2% | 95.8% | 92.6% | 0.2% | 0.8% | 0.0% | wader (45) |
| alligator | 110 | 73.6% (65.5 to 81.8) | 48.2% | 100.0% | 80.7% | 0.0% | 0.0% | 0.0% | plant (9) |
| reptile | 268 | 53.7% (47.8 to 59.7) | 14.2% | 86.8% | 82.6% | 0.7% | 0.4% | 0.0% | insect (78) |
| frog | 97 | 53.6% (44.3 to 62.9) | 22.7% | 90.9% | 73.3% | 0.0% | 1.0% | 0.0% | insect (30) |
| bee | 126 | 42.1% (34.1 to 50.0) | 42.1% | 37.7% | 86.3% | 0.0% | 0.0% | 0.0% | insect (60) |
| insect | 962 | 90.6% (88.7 to 92.4) | 59.1% | 97.4% | 99.5% | 0.2% | 0.1% | 0.0% | plant (40) |
| plant | 1223 | 95.7% (94.4 to 96.8) | 77.8% | 99.7% | 99.3% | 0.0% | 0.1% | 0.0% | insect (33) |
| other | 296 | 49.7% (44.3 to 55.4) | 33.8% | 77.0% | 83.7% | 0.3% | 0.0% | 0.0% | insect (107) |

The same photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| squirrel | 6 | 100.0% (100.0 to 100.0) | – |
| deer | 1 | 100.0% (100.0 to 100.0) | – |
| rabbit | 11 | 100.0% (100.0 to 100.0) | – |
| hawk | 15 | 100.0% (100.0 to 100.0) | – |
| wader | 191 | 96.3% (93.2 to 99.0) | bird (7) |
| bird | 194 | 94.8% (91.8 to 97.9) | wader (9) |
| alligator | 54 | 98.2% (94.4 to 100.0) | bird (1) |
| reptile | 33 | 100.0% (100.0 to 100.0) | – |
| frog | 20 | 100.0% (100.0 to 100.0) | – |
| bee | 23 | 87.0% (69.6 to 100.0) | insect (3) |
| insect | 607 | 91.3% (88.8 to 93.4) | bee (27) |
| plant | 972 | 97.5% (96.5 to 98.5) | insect (9) |
| other | 81 | 95.1% (90.1 to 98.8) | insect (3) |

The kind of eye on the extra set's test photos (`images/coco-kinds.wasm-int8-per-channel`):

| Photos of | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| person | 400 | 98.2% (96.8 to 99.5) | 94.8% | 99.2% | 100.0% | 98.2% | 1.5% | 0.0% | none (6) |
| none | 500 | 97.6% (96.0 to 98.8) | 89.6% | 100.0% | 88.5% | 0.4% | 97.6% | 0.0% | cat (3) |
| cat | 77 | 89.6% (83.1 to 96.1) | 18.2% | 85.7% | 92.1% | 2.6% | 5.2% | 0.0% | none (4) |
| dog | 63 | 90.5% (82.5 to 96.8) | 0.0% | – | 92.1% | 0.0% | 0.0% | 0.0% | cat (5) |
| deer | 200 | 94.0% (90.5 to 97.0) | 14.5% | 96.6% | 97.7% | 2.0% | 0.0% | 0.0% | dog (6) |

The extra set's test photos by the kind the page asserted:

| Kind asserted | Photos | Right | Commonest true kind when wrong |
|---|---:|---:|---|
| cat | 12 | 100.0% (100.0 to 100.0) | – |
| deer | 28 | 100.0% (100.0 to 100.0) | – |
| person | 378 | 99.5% (98.7 to 100.0) | cat (1) |
| none | 452 | 99.1% (98.2 to 99.8) | person (3) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.39 | 76.6% (75.4 to 77.9) | 89.0% (88.0 to 90.1) | 82.2% (79.8 to 84.5) | 89.5% (87.7 to 91.2) | 98.7% (98.0 to 99.4) | 87.7% (82.3 to 93.1) |
| 95 in 100 | 0.53 | 52.6% (51.1 to 54.2) | 95.4% (94.5 to 96.2) | 88.9% (87.5 to 90.2) | 70.2% (67.6 to 72.7) | 99.3% (98.7 to 99.8) | 94.6% (92.2 to 96.8) |
| 98 in 100 | 0.61 | 39.5% (38.0 to 41.0) | 97.3% (96.6 to 98.1) | 90.8% (89.7 to 92.0) | 63.5% (60.9 to 66.4) | 99.9% (99.6 to 100.0) | 94.9% (92.9 to 96.9) |
