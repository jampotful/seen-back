# Exported slots, scored as the page would

_This file is written by `tools/eval/report.py` from `docs/eval/shipped-*.json`. Rerun the script to change it._

## `live-pocket`

The slot holds the head `sentences` for `tinyclip-39m-16` (species_com), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `product`, t_kind 100, w_kind 0.3, alpha_prior 1. On 1803 tuning photos (val) the thresholds came out as name_at 0.40 and offer_at 0.53. On the 4197 test photos the kind of eye is right for 83.7% (82.5 to 84.8); the top species is right for 34.9% (33.5 to 36.4) and is among the first five for 53.8% (52.3 to 55.3). `person` was said for 0.05% of these photos and `none` for 0.05%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind phrases`. With kind_at 0.71 (set on wildlife tuning photos alone, because the extra set's vectors were not published for this model), the page asserts a kind for 68.6% (67.2 to 70.0) of the wildlife test photos and is right for 95.7% (95.0 to 96.5) of those; for the 31.4% (30.0 to 32.8) where it is not sure, the true kind is among its three likeliest for 92.1% (90.6 to 93.5).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 15.2% | the name is right for 93.4% (91.4 to 95.2); the kind for 99.1% (98.1 to 99.7) |
| three species to choose from | 3.3% | the three hold the species for 85.5% (79.7 to 91.3); the kind is right for 99.3% (97.8 to 100.0) |
| a kind of eye only | 81.5% | the kind is right for 80.2% (78.8 to 81.5) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.71):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 45.5% (18.2 to 72.7) | 18.2% | 100.0% | 66.7% | 0.0% | 0.0% | 0.0% | plant (2) |
| dog | 6 | 66.7% (33.3 to 100.0) | 16.7% | 100.0% | 80.0% | 0.0% | 0.0% | 0.0% | deer (1) |
| squirrel | 36 | 75.0% (61.1 to 88.9) | 55.6% | 100.0% | 50.0% | 0.0% | 0.0% | 30.6% | plant (3) |
| deer | 36 | 63.9% (47.2 to 77.8) | 38.9% | 92.9% | 68.2% | 0.0% | 0.0% | 27.8% | plant (6) |
| rabbit | 31 | 93.5% (83.9 to 100.0) | 77.4% | 100.0% | 100.0% | 0.0% | 0.0% | 64.5% | bird (1) |
| hawk | 82 | 85.4% (76.8 to 92.7) | 68.3% | 94.6% | 80.8% | 0.0% | 0.0% | 36.6% | wader (4) |
| wader | 382 | 89.8% (86.7 to 92.7) | 77.5% | 98.3% | 93.0% | 0.0% | 0.0% | 49.7% | bird (19) |
| bird | 531 | 75.0% (71.0 to 78.5) | 46.0% | 92.2% | 90.9% | 0.2% | 0.2% | 21.7% | wader (54) |
| alligator | 110 | 91.8% (86.4 to 96.4) | 81.8% | 100.0% | 70.0% | 0.0% | 0.0% | 79.1% | plant (6) |
| reptile | 268 | 75.0% (69.8 to 79.8) | 47.4% | 95.3% | 88.7% | 0.0% | 0.4% | 22.0% | insect (31) |
| frog | 97 | 76.3% (68.0 to 84.5) | 60.8% | 100.0% | 84.2% | 0.0% | 0.0% | 3.1% | insect (14) |
| bee | 126 | 65.9% (57.9 to 73.8) | 64.3% | 79.0% | 91.1% | 0.0% | 0.0% | 0.0% | insect (33) |
| insect | 962 | 94.3% (92.7 to 95.7) | 79.7% | 98.3% | 100.0% | 0.0% | 0.0% | 3.8% | plant (20) |
| plant | 1223 | 96.2% (95.0 to 97.1) | 85.5% | 99.4% | 98.3% | 0.1% | 0.0% | 6.1% | insect (39) |
| other | 296 | 23.6% (18.9 to 28.4) | 17.9% | 0.0% | 94.7% | 0.0% | 0.0% | 0.7% | insect (175) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.52 | 85.7% (84.6 to 86.7) | 90.3% (89.3 to 91.2) | 86.8% (84.0 to 89.5) | – | – | – |
| 95 in 100 | 0.71 | 68.6% (67.2 to 70.0) | 95.7% (95.0 to 96.5) | 92.1% (90.6 to 93.5) | – | – | – |
| 98 in 100 | 0.89 | 35.9% (34.4 to 37.5) | 99.1% (98.6 to 99.5) | 95.8% (95.0 to 96.5) | – | – | – |

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
| 98 in 100 | 0.20 | 99.6% (99.5 to 99.8) | 98.5% (98.1 to 98.9) | 86.7% (66.7 to 100.0) | – | – | – |

## `sentences-tinyclip-39m-16`

The slot holds the head `sentences` for `tinyclip-39m-16` (species_com), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `product`, t_kind 20, w_kind 0.5, alpha_prior 0.75. On 1803 tuning photos (val) the thresholds came out as name_at 0.28 and offer_at never (no level reached nine in ten). On the 4197 test photos the kind of eye is right for 83.7% (82.6 to 84.8); the top species is right for 35.3% (33.9 to 36.8) and is among the first five for 55.1% (53.6 to 56.6). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind phrases`. With kind_at 0.43 (set on wildlife tuning photos alone, because the extra set's vectors were not published for this model), the page asserts a kind for 65.7% (64.3 to 67.1) of the wildlife test photos and is right for 95.6% (94.8 to 96.3) of those; for the 34.3% (32.9 to 35.7) where it is not sure, the true kind is among its three likeliest for 89.4% (87.8 to 90.9). The slot needs: fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 17.6% | the name is right for 89.8% (87.5 to 91.9); the kind for 98.4% (97.4 to 99.2) |
| three species to choose from | 0.0% | the three hold the species for –; the kind is right for – |
| a kind of eye only | 82.4% | the kind is right for 80.6% (79.3 to 81.8) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.43):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 18.2% (0.0 to 45.5) | 0.0% | – | 36.4% | 0.0% | 0.0% | 0.0% | insect (6) |
| dog | 6 | 50.0% (16.7 to 83.3) | 0.0% | – | 50.0% | 0.0% | 0.0% | 0.0% | insect (2) |
| squirrel | 36 | 75.0% (61.1 to 88.9) | 30.6% | 100.0% | 64.0% | 0.0% | 0.0% | 30.6% | plant (4) |
| deer | 36 | 47.2% (30.6 to 63.9) | 27.8% | 90.0% | 57.7% | 0.0% | 0.0% | 27.8% | plant (9) |
| rabbit | 31 | 87.1% (74.2 to 96.8) | 64.5% | 100.0% | 72.7% | 0.0% | 0.0% | 67.7% | bird (1) |
| hawk | 82 | 79.3% (70.7 to 87.8) | 58.5% | 95.8% | 76.5% | 0.0% | 0.0% | 42.7% | bird (7) |
| wader | 382 | 88.2% (84.8 to 91.4) | 72.0% | 99.6% | 85.0% | 0.0% | 0.0% | 57.9% | bird (27) |
| bird | 531 | 79.1% (75.3 to 82.5) | 36.3% | 93.3% | 89.6% | 0.0% | 0.0% | 29.0% | wader (31) |
| alligator | 110 | 88.2% (81.8 to 93.6) | 71.8% | 100.0% | 71.0% | 0.0% | 0.0% | 76.4% | plant (8) |
| reptile | 268 | 67.5% (61.9 to 72.8) | 29.9% | 91.2% | 85.6% | 0.0% | 0.0% | 23.1% | insect (58) |
| frog | 97 | 63.9% (54.6 to 73.2) | 49.5% | 91.7% | 81.6% | 0.0% | 0.0% | 7.2% | insect (30) |
| bee | 126 | 55.6% (47.6 to 64.3) | 69.0% | 66.7% | 82.1% | 0.0% | 0.0% | 0.8% | insect (45) |
| insect | 962 | 96.5% (95.2 to 97.5) | 83.0% | 98.4% | 100.0% | 0.0% | 0.0% | 5.1% | plant (24) |
| plant | 1223 | 96.6% (95.4 to 97.5) | 86.6% | 99.6% | 99.4% | 0.0% | 0.0% | 6.6% | insect (36) |
| other | 296 | 32.4% (27.0 to 37.9) | 16.2% | 2.1% | 96.8% | 0.0% | 0.0% | 0.7% | insect (165) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.32 | 86.2% (85.1 to 87.2) | 89.9% (88.9 to 90.9) | 79.3% (75.7 to 82.4) | – | – | – |
| 95 in 100 | 0.43 | 65.7% (64.3 to 67.1) | 95.6% (94.8 to 96.3) | 89.4% (87.8 to 90.9) | – | – | – |
| 98 in 100 | 0.57 | 30.2% (28.8 to 31.7) | 99.2% (98.7 to 99.7) | 94.3% (93.4 to 95.1) | – | – | – |

## `sentences-tinyclip-8m-16`

The slot holds the head `sentences` for `tinyclip-8m-16` (species_com), fitted on `none (sentence rows only)`, with 5911 species rows. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `product`, t_kind 20, w_kind 0.5, alpha_prior 1. On 1803 tuning photos (val) the thresholds came out as name_at 0.56 and offer_at 0.62. On the 4197 test photos the kind of eye is right for 79.5% (78.2 to 80.6); the top species is right for 26.4% (25.1 to 27.8) and is among the first five for 45.4% (43.9 to 46.9). `person` was said for 0.00% of these photos and `none` for 0.00%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind phrases`. With kind_at 0.53 (set on wildlife tuning photos alone, because the extra set's vectors were not published for this model), the page asserts a kind for 41.5% (40.0 to 43.0) of the wildlife test photos and is right for 97.8% (97.0 to 98.4) of those; for the 58.5% (57.0 to 60.0) where it is not sure, the true kind is among its three likeliest for 91.5% (90.4 to 92.6). The slot needs: fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 9.7% | the name is right for 88.2% (85.0 to 91.4); the kind for 97.3% (95.6 to 98.8) |
| three species to choose from | 5.5% | the three hold the species for 81.8% (76.2 to 86.6); the kind is right for 97.4% (95.2 to 99.1) |
| a kind of eye only | 84.8% | the kind is right for 76.2% (74.8 to 77.6) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.53):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 36.4% (9.1 to 63.6) | 0.0% | – | 54.5% | 0.0% | 0.0% | 0.0% | plant (6) |
| dog | 6 | 0.0% (0.0 to 0.0) | 16.7% | 0.0% | 20.0% | 0.0% | 0.0% | 16.7% | deer (3) |
| squirrel | 36 | 58.3% (41.7 to 75.0) | 27.8% | 100.0% | 50.0% | 0.0% | 0.0% | 36.1% | plant (6) |
| deer | 36 | 47.2% (30.6 to 63.9) | 19.4% | 100.0% | 65.5% | 0.0% | 0.0% | 25.0% | plant (11) |
| rabbit | 31 | 80.7% (64.5 to 93.5) | 48.4% | 100.0% | 81.2% | 0.0% | 0.0% | 38.7% | insect (2) |
| hawk | 82 | 70.7% (61.0 to 80.5) | 40.2% | 93.9% | 75.5% | 0.0% | 0.0% | 22.0% | wader (9) |
| wader | 382 | 82.2% (78.3 to 85.9) | 55.5% | 99.5% | 88.2% | 0.0% | 0.0% | 27.0% | bird (40) |
| bird | 531 | 71.0% (67.2 to 74.8) | 20.0% | 93.4% | 89.6% | 0.0% | 0.0% | 12.4% | wader (54) |
| alligator | 110 | 85.5% (79.1 to 91.8) | 60.9% | 100.0% | 81.4% | 0.0% | 0.0% | 69.1% | plant (8) |
| reptile | 268 | 56.0% (50.0 to 61.6) | 10.8% | 100.0% | 87.9% | 0.0% | 0.0% | 9.7% | insect (52) |
| frog | 97 | 54.6% (45.4 to 63.9) | 20.6% | 95.0% | 70.1% | 0.0% | 0.0% | 1.0% | insect (33) |
| bee | 126 | 45.2% (36.5 to 54.0) | 28.6% | 75.0% | 88.9% | 0.0% | 0.0% | 0.8% | insect (51) |
| insect | 962 | 90.4% (88.4 to 92.2) | 46.0% | 98.4% | 99.4% | 0.0% | 0.0% | 2.6% | plant (46) |
| plant | 1223 | 96.7% (95.6 to 97.6) | 61.3% | 100.0% | 99.6% | 0.0% | 0.0% | 4.2% | insect (30) |
| other | 296 | 38.2% (32.8 to 43.9) | 4.1% | 8.3% | 92.3% | 0.0% | 0.0% | 2.0% | insect (129) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.38 | 72.0% (70.7 to 73.4) | 91.1% (90.0 to 92.1) | 85.3% (83.2 to 87.2) | – | – | – |
| 95 in 100 | 0.53 | 41.5% (40.0 to 43.0) | 97.8% (97.0 to 98.4) | 91.5% (90.4 to 92.6) | – | – | – |
| 98 in 100 | 0.64 | 16.0% (14.9 to 17.2) | 99.6% (99.0 to 100.0) | 93.8% (93.0 to 94.5) | – | – | – |

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

The slot holds the head `prototypes + sentences` for `tinyclip-39m-16` (species_taxon_com, beta 8, bias for species without photos 0.8), fitted on `images/alachua-2025 (two thirds of val)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `product`, t_kind 20, w_kind 0.7, alpha_prior 1. On 565 tuning photos (the third of val kept for tuning) the thresholds came out as name_at 0.89 and offer_at 0.94. On the 4197 test photos the kind of eye is right for 87.0% (85.9 to 88.0); the top species is right for 36.3% (34.9 to 37.8) and is among the first five for 58.8% (57.2 to 60.2). `person` was said for 0.02% of these photos and `none` for 0.02%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind phrases`. With kind_at 0.46 (set on wildlife tuning photos alone, because the extra set's vectors were not published for this model), the page asserts a kind for 77.7% (76.4 to 79.0) of the wildlife test photos and is right for 95.4% (94.7 to 96.1) of those; for the 22.3% (21.0 to 23.6) where it is not sure, the true kind is among its three likeliest for 91.4% (89.7 to 93.3). The slot needs: species.bias_url (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 14.9% | the name is right for 91.8% (89.6 to 93.9); the kind for 98.2% (97.1 to 99.2) |
| three species to choose from | 7.0% | the three hold the species for 90.2% (86.8 to 93.6); the kind is right for 97.6% (95.6 to 99.3) |
| a kind of eye only | 78.1% | the kind is right for 83.9% (82.6 to 85.1) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.46):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 63.6% (36.4 to 90.9) | 36.4% | 100.0% | 57.1% | 0.0% | 0.0% | 27.3% | plant (3) |
| dog | 6 | 66.7% (33.3 to 100.0) | 33.3% | 100.0% | 75.0% | 0.0% | 0.0% | 33.3% | deer (1) |
| squirrel | 36 | 80.6% (66.7 to 91.7) | 72.2% | 96.2% | 70.0% | 0.0% | 0.0% | 58.3% | wader (3) |
| deer | 36 | 72.2% (58.3 to 86.1) | 55.6% | 95.0% | 62.5% | 0.0% | 0.0% | 52.8% | other (4) |
| rabbit | 31 | 90.3% (77.4 to 100.0) | 80.6% | 100.0% | 100.0% | 0.0% | 0.0% | 45.2% | other (1) |
| hawk | 82 | 84.2% (75.6 to 91.5) | 84.1% | 95.7% | 69.2% | 0.0% | 0.0% | 39.0% | bird (4) |
| wader | 382 | 89.3% (86.1 to 92.2) | 86.4% | 95.8% | 90.4% | 0.0% | 0.0% | 38.0% | bird (21) |
| bird | 531 | 80.2% (76.6 to 83.4) | 69.7% | 89.7% | 92.5% | 0.2% | 0.0% | 23.5% | wader (42) |
| alligator | 110 | 86.4% (80.0 to 92.7) | 79.1% | 98.9% | 65.2% | 0.0% | 0.0% | 68.2% | plant (5) |
| reptile | 268 | 82.8% (78.4 to 87.3) | 67.5% | 94.5% | 92.0% | 0.0% | 0.4% | 14.9% | plant (22) |
| frog | 97 | 77.3% (69.1 to 85.6) | 64.9% | 98.4% | 85.3% | 0.0% | 0.0% | 3.1% | reptile (12) |
| bee | 126 | 66.7% (58.7 to 74.6) | 81.0% | 77.5% | 79.2% | 0.0% | 0.0% | 4.8% | insect (26) |
| insect | 962 | 88.5% (86.3 to 90.5) | 74.1% | 95.7% | 97.6% | 0.0% | 0.0% | 4.9% | plant (44) |
| plant | 1223 | 98.5% (97.8 to 99.2) | 96.0% | 99.6% | 95.9% | 0.0% | 0.0% | 6.9% | insect (10) |
| other | 296 | 63.5% (58.1 to 68.9) | 32.4% | 77.1% | 93.5% | 0.0% | 0.0% | 2.7% | insect (58) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.32 | 92.3% (91.5 to 93.1) | 90.9% (90.0 to 91.8) | 81.8% (77.5 to 85.9) | – | – | – |
| 95 in 100 | 0.46 | 77.7% (76.4 to 79.0) | 95.4% (94.7 to 96.1) | 91.4% (89.7 to 93.3) | – | – | – |
| 98 in 100 | 0.59 | 60.3% (58.8 to 61.9) | 97.8% (97.2 to 98.3) | 94.8% (93.7 to 95.8) | – | – | – |

## `val-tinyclip-8m-16`

The slot holds the head `discriminant + sentences` for `tinyclip-8m-16` (shrinkage 0.03, species_com, gamma 1), fitted on `images/alachua-2025 (two thirds of val)`, with 5911 species rows, and a bias a row. Every photo's vector (`images/alachua-2025.wasm-int8-per-channel`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). Settings: rule `product`, t_kind 50, w_kind 0.3, alpha_prior 0.5. On 565 tuning photos (the third of val kept for tuning) the thresholds came out as name_at never (no level reached nine in ten) and offer_at 0.24. On the 4197 test photos the kind of eye is right for 77.6% (76.4 to 78.9); the top species is right for 25.3% (24.0 to 26.6) and is among the first five for 45.5% (44.0 to 47.0). `person` was said for 0.05% of these photos and `none` for 0.10%; the set holds neither. The top species from fuse.py differs from a direct matrix computation on the same files for 0 photos. The kinds head is `kind phrases`. With kind_at 0.58 (set on wildlife tuning photos alone, because the extra set's vectors were not published for this model), the page asserts a kind for 52.4% (50.9 to 54.0) of the wildlife test photos and is right for 94.3% (93.3 to 95.3) of those; for the 47.6% (46.0 to 49.1) where it is not sure, the true kind is among its three likeliest for 89.0% (87.6 to 90.4). The slot needs: species.bias_url (build 7 of the page); fusion.kind_at (the build of the page that has the answer `not sure`).

| What the page would show | Share of test photos | Right |
|---|---:|---|
| a species name | 0.0% | the name is right for –; the kind for – |
| three species to choose from | 16.2% | the three hold the species for 83.2% (80.3 to 85.9); the kind is right for 97.2% (95.9 to 98.4) |
| a kind of eye only | 83.8% | the kind is right for 73.9% (72.3 to 75.3) |

The kind of eye on the wildlife test photos, one row a true kind (kind_at 0.58):

| True kind | Photos | Kind right | Kind asserted | Right when asserted | True kind among the three when not sure | Said `person` | Said `none` | A species named | Commonest wrong answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cat | 11 | 36.4% (9.1 to 63.6) | 9.1% | 100.0% | 30.0% | 0.0% | 9.1% | 0.0% | plant (5) |
| dog | 6 | 16.7% (0.0 to 50.0) | 16.7% | 0.0% | 20.0% | 0.0% | 0.0% | 0.0% | deer (2) |
| squirrel | 36 | 52.8% (36.1 to 69.4) | 16.7% | 100.0% | 50.0% | 0.0% | 0.0% | 0.0% | plant (6) |
| deer | 36 | 44.4% (27.8 to 61.1) | 16.7% | 83.3% | 66.7% | 0.0% | 0.0% | 0.0% | plant (12) |
| rabbit | 31 | 74.2% (58.1 to 90.3) | 41.9% | 100.0% | 72.2% | 0.0% | 0.0% | 0.0% | plant (3) |
| hawk | 82 | 58.5% (47.6 to 69.5) | 36.6% | 96.7% | 73.1% | 0.0% | 0.0% | 0.0% | bird (18) |
| wader | 382 | 80.9% (76.7 to 84.8) | 53.7% | 98.0% | 89.3% | 0.0% | 0.0% | 0.0% | bird (44) |
| bird | 531 | 71.0% (67.2 to 74.8) | 20.7% | 91.8% | 90.3% | 0.4% | 0.4% | 0.0% | wader (52) |
| alligator | 110 | 70.0% (60.9 to 78.2) | 40.0% | 100.0% | 77.3% | 0.0% | 0.0% | 0.0% | reptile (11) |
| reptile | 268 | 47.4% (41.4 to 53.0) | 11.2% | 76.7% | 81.9% | 0.0% | 0.4% | 0.0% | insect (81) |
| frog | 97 | 44.3% (34.0 to 54.6) | 24.7% | 70.8% | 65.8% | 0.0% | 0.0% | 0.0% | insect (43) |
| bee | 126 | 39.7% (31.8 to 48.4) | 46.8% | 49.2% | 89.6% | 0.0% | 0.0% | 0.0% | insect (59) |
| insect | 962 | 93.1% (91.6 to 94.7) | 66.9% | 98.0% | 99.7% | 0.0% | 0.0% | 0.0% | plant (46) |
| plant | 1223 | 96.3% (95.3 to 97.4) | 79.1% | 99.5% | 99.6% | 0.0% | 0.0% | 0.0% | insect (37) |
| other | 296 | 30.7% (25.7 to 36.1) | 19.3% | 17.5% | 95.0% | 0.0% | 0.0% | 0.0% | insect (156) |

Other bars for an asserted kind, each level set on the tuning photos:

| Asserted kind right at least | kind_at | Asserted, wildlife test | Right when asserted | True kind among the three when not sure | Asserted, extra test | Right when asserted | True kind among the three when not sure |
|---|---:|---:|---:|---:|---:|---:|---:|
| 90 in 100 | 0.47 | 70.0% (68.6 to 71.4) | 89.5% (88.5 to 90.6) | 85.5% (83.5 to 87.2) | – | – | – |
| 95 in 100 | 0.58 | 52.4% (50.9 to 54.0) | 94.3% (93.3 to 95.3) | 89.0% (87.6 to 90.4) | – | – | – |
| 98 in 100 | 0.70 | 29.4% (28.1 to 30.9) | 98.3% (97.5 to 99.0) | 92.1% (91.0 to 93.0) | – | – | – |
