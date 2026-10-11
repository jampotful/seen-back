# Exported slots, scored as the page would

_This file is written by `tools/eval/report.py` from `docs/eval/shipped-*.json`. Rerun the script to change it._

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

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.20 | 99.6% (99.5 to 99.8) | 98.5% (98.1 to 98.9) | 86.7% (66.7 to 100.0) | – | – | – |
| 95 in 100 | 0.20 | 99.6% (99.5 to 99.8) | 98.5% (98.1 to 98.9) | 86.7% (66.7 to 100.0) | – | – | – |
| 98 in 100 | no level reached it | – | – | – | – | – | – |

## `sentences-tinyclip-39m-16`

The slot holds the head `sentences` for `tinyclip-39m-16` (species_com), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `product`, t_kind 20, w_kind 0.5, alpha_prior 1. On 1803 tuning photos (val) the thresholds came out as name_at 0.40 and offer_at 0.53. On the 4197 test photos the kind of eye is right for 84.5% (83.4 to 85.6); the top species is right for 34.9% (33.5 to 36.4) and is among the first five for 53.8% (52.3 to 55.3). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind phrases`. With kind_at 0.42 (set on wildlife tuning photos alone, because the extra set's vectors were not published for this model), the page asserts a kind for 68.4% (67.0 to 69.9) of the wildlife test photos and is right for 95.7% (95.0 to 96.5) of those; for the 31.6% (30.1 to 33.0) where it is not sure, the true kind is among its three likeliest for 90.6% (88.9 to 92.2). The slot needs: fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 15.4% | the name is right for 93.0% (91.0 to 94.9); the kind for 98.9% (98.1 to 99.7) |
| three species to choose from | 3.3% | the three hold the species for 84.9% (78.4 to 90.6); the kind is right for 99.3% (97.8 to 100.0) |
| a kind of eye only | 81.3% | the kind is right for 81.2% (79.8 to 82.5) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.42):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 18.2% (0.0 to 45.5) | 0.0% | – | 36.4% | 0.0% | 0.0% | 0.0% | insect (5) |
| dog | 6 | 50.0% (16.7 to 83.3) | 0.0% | – | 50.0% | 0.0% | 0.0% | 0.0% | deer (1) |
| squirrel | 36 | 75.0% (61.1 to 88.9) | 33.3% | 100.0% | 62.5% | 0.0% | 0.0% | 30.6% | plant (4) |
| deer | 36 | 55.6% (38.9 to 72.2) | 30.6% | 90.9% | 60.0% | 0.0% | 0.0% | 27.8% | plant (9) |
| rabbit | 31 | 87.1% (74.2 to 96.8) | 67.7% | 100.0% | 80.0% | 0.0% | 0.0% | 64.5% | bird (1) |
| hawk | 82 | 82.9% (74.4 to 91.5) | 61.0% | 96.0% | 78.1% | 0.0% | 0.0% | 36.6% | wader (5) |
| wader | 382 | 89.5% (86.4 to 92.7) | 75.9% | 99.3% | 92.4% | 0.0% | 0.0% | 50.0% | bird (23) |
| bird | 531 | 77.6% (73.8 to 81.0) | 44.3% | 93.2% | 90.5% | 0.0% | 0.0% | 22.4% | wader (40) |
| alligator | 110 | 90.0% (84.5 to 95.5) | 78.2% | 100.0% | 70.8% | 0.0% | 0.0% | 79.1% | plant (8) |
| reptile | 268 | 73.1% (67.9 to 78.4) | 40.7% | 93.6% | 91.2% | 0.0% | 0.0% | 22.0% | insect (37) |
| frog | 97 | 72.2% (63.9 to 81.4) | 54.6% | 100.0% | 81.8% | 0.0% | 0.0% | 3.1% | insect (20) |
| bee | 126 | 57.1% (49.2 to 65.9) | 70.6% | 68.5% | 81.1% | 0.0% | 0.0% | 0.0% | insect (43) |
| insect | 962 | 96.0% (94.7 to 97.1) | 82.5% | 98.1% | 100.0% | 0.0% | 0.0% | 3.8% | plant (24) |
| plant | 1223 | 96.9% (95.8 to 97.8) | 87.7% | 99.5% | 98.7% | 0.0% | 0.0% | 6.2% | insect (31) |
| other | 296 | 33.8% (28.4 to 39.5) | 16.2% | 2.1% | 94.4% | 0.0% | 0.0% | 0.7% | insect (154) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.32 | 86.3% (85.2 to 87.3) | 90.7% (89.8 to 91.7) | 82.3% (79.2 to 85.2) | – | – | – |
| 95 in 100 | 0.42 | 68.4% (67.0 to 69.9) | 95.7% (95.0 to 96.5) | 90.6% (88.9 to 92.2) | – | – | – |
| 98 in 100 | 0.56 | 36.8% (35.3 to 38.3) | 99.3% (98.8 to 99.7) | 94.9% (94.0 to 95.7) | – | – | – |

## `sentences-tinyclip-8m-16`

The slot holds the head `sentences` for `tinyclip-8m-16` (species_com), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `product`, t_kind 20, w_kind 0.5, alpha_prior 0.625. On 1803 tuning photos (val) the thresholds came out as name_at 0.42 and offer_at 0.47. On the 4197 test photos the kind of eye is right for 78.9% (77.7 to 80.1); the top species is right for 25.3% (24.0 to 26.7) and is among the first five for 43.2% (41.7 to 44.7). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind phrases`. With kind_at 0.54 (set on wildlife tuning photos alone, because the extra set's vectors were not published for this model), the page asserts a kind for 31.1% (29.7 to 32.6) of the wildlife test photos and is right for 98.3% (97.6 to 99.0) of those; for the 68.9% (67.5 to 70.3) where it is not sure, the true kind is among its three likeliest for 91.1% (90.0 to 92.1). The slot needs: fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 9.2% | the name is right for 90.1% (87.0 to 93.2); the kind for 99.0% (97.7 to 99.7) |
| three species to choose from | 5.1% | the three hold the species for 81.9% (76.8 to 86.6); the kind is right for 97.2% (94.9 to 99.1) |
| a kind of eye only | 85.7% | the kind is right for 75.7% (74.3 to 77.1) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.54):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 36.4% (9.1 to 63.6) | 0.0% | – | 54.5% | 0.0% | 0.0% | 0.0% | plant (6) |
| dog | 6 | 16.7% (0.0 to 50.0) | 0.0% | – | 33.3% | 0.0% | 0.0% | 16.7% | deer (2) |
| squirrel | 36 | 52.8% (36.1 to 69.4) | 16.7% | 100.0% | 53.3% | 0.0% | 0.0% | 30.6% | plant (5) |
| deer | 36 | 41.7% (25.0 to 58.3) | 8.3% | 100.0% | 48.5% | 0.0% | 0.0% | 25.0% | plant (12) |
| rabbit | 31 | 77.4% (61.3 to 90.3) | 38.7% | 100.0% | 78.9% | 0.0% | 0.0% | 45.2% | insect (2) |
| hawk | 82 | 68.3% (58.5 to 78.0) | 29.3% | 95.8% | 75.9% | 0.0% | 0.0% | 19.5% | bird (9) |
| wader | 382 | 80.9% (77.0 to 84.8) | 45.0% | 99.4% | 85.2% | 0.0% | 0.0% | 32.2% | bird (44) |
| bird | 531 | 73.1% (69.3 to 76.6) | 10.4% | 94.5% | 88.2% | 0.0% | 0.0% | 12.2% | plant (44) |
| alligator | 110 | 77.3% (69.1 to 84.5) | 41.8% | 100.0% | 79.7% | 0.0% | 0.0% | 62.7% | plant (9) |
| reptile | 268 | 50.0% (44.4 to 55.6) | 4.5% | 100.0% | 81.2% | 0.0% | 0.0% | 6.7% | insect (84) |
| frog | 97 | 49.5% (40.2 to 59.8) | 15.5% | 86.7% | 70.7% | 0.0% | 0.0% | 1.0% | insect (40) |
| bee | 126 | 45.2% (36.5 to 54.0) | 17.5% | 77.3% | 90.4% | 0.0% | 0.0% | 0.8% | insect (51) |
| insect | 962 | 93.1% (91.5 to 94.7) | 45.0% | 99.1% | 99.8% | 0.0% | 0.0% | 1.8% | plant (40) |
| plant | 1223 | 95.5% (94.3 to 96.7) | 40.6% | 100.0% | 99.2% | 0.0% | 0.0% | 3.1% | insect (45) |
| other | 296 | 36.5% (31.1 to 42.2) | 2.4% | 14.3% | 96.5% | 0.0% | 0.0% | 0.3% | insect (153) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.38 | 70.5% (69.2 to 71.9) | 90.9% (89.8 to 92.0) | 82.6% (80.4 to 84.6) | – | – | – |
| 95 in 100 | 0.54 | 31.1% (29.7 to 32.6) | 98.3% (97.6 to 99.0) | 91.1% (90.0 to 92.1) | – | – | – |
| 98 in 100 | 0.61 | 14.7% (13.7 to 15.8) | 99.5% (98.9 to 100.0) | 92.7% (91.8 to 93.5) | – | – | – |

## `val-bioclip2-l14`

The slot holds the head `prototypes + sentences` for `bioclip2-l14` (species_sci, beta 8, bias for species without photos 0.65), fitted on `images/alachua-2025 (two thirds of val)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 20, w_kind 0.5, alpha_prior 0.6. On 565 tuning photos (the third of val kept for tuning) the thresholds came out as name_at 0.05 and offer_at never (no level reached nine in ten). On the 4197 test photos the kind of eye is right for 98.5% (98.1 to 98.9); the top species is right for 91.7% (90.9 to 92.6) and is among the first five for 97.6% (97.1 to 98.0). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The slot needs: species.bias_url (build 7 of the page); fusion.rule mix (build 7 of the page).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 99.6% | the name is right for 92.0% (91.2 to 92.8); the kind for 98.7% (98.3 to 99.0) |
| three species to choose from | 0.0% | the three hold the species for –; the kind is right for – |
| a kind of eye only | 0.4% | the kind is right for 46.7% (20.0 to 73.3) |

## `val-tinyclip-39m-16`

The slot holds the head `prototypes + sentences` for `tinyclip-39m-16` (species_com, beta 8, bias for species without photos 0.65), fitted on `images/alachua-2025 (two thirds of val)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 20, w_kind 0.7, alpha_prior 0.75. On 565 tuning photos (the third of val kept for tuning) the thresholds came out as name_at 0.63 and offer_at never (no level reached nine in ten). On the 4197 test photos the kind of eye is right for 86.8% (85.7 to 87.7); the top species is right for 36.9% (35.5 to 38.4) and is among the first five for 55.8% (54.3 to 57.3). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The slot needs: species.bias_url (build 7 of the page); fusion.rule mix (build 7 of the page).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 19.4% | the name is right for 88.7% (86.6 to 90.9); the kind for 98.4% (97.4 to 99.3) |
| three species to choose from | 0.0% | the three hold the species for –; the kind is right for – |
| a kind of eye only | 80.6% | the kind is right for 83.9% (82.7 to 85.2) |

## `val-tinyclip-8m-16`

The slot holds the head `discriminant + sentences` for `tinyclip-8m-16` (shrinkage 0.03, species_com, gamma 3), fitted on `images/alachua-2025 (two thirds of val)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `mix`, t_kind 50, w_kind 0.3, alpha_prior 0.5. On 565 tuning photos (the third of val kept for tuning) the thresholds came out as name_at 0.31 and offer_at 0.33. On the 4197 test photos the kind of eye is right for 77.5% (76.2 to 78.8); the top species is right for 25.6% (24.3 to 26.9) and is among the first five for 43.8% (42.3 to 45.3). `person` was said for 0.02% of these photos and `none` for 0.10%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The slot needs: species.bias_url (build 7 of the page); fusion.rule mix (build 7 of the page).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 8.3% | the name is right for 89.9% (86.5 to 92.8); the kind for 99.1% (98.0 to 100.0) |
| three species to choose from | 6.7% | the three hold the species for 78.2% (73.2 to 82.9); the kind is right for 97.1% (95.0 to 98.9) |
| a kind of eye only | 85.1% | the kind is right for 73.9% (72.5 to 75.3) |
