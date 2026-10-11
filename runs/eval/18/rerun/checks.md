# Checks for leakage and for mistakes in the inputs

_This file is written by `tools/eval/report.py` from `docs/eval/checks.json`. Rerun the script to change it._

| Verdict | Check | What was found |
|---|---|---|
| pass | every evaluation photo is dated after the species list's last record (2024-12-31) | 6000 rows; earliest 2025-01-01, latest 2026-09-29; rows on or before 2024-12-31: 0 |
| pass | every evaluation photo is dated after the GBIF snapshot behind BioCLIP 2's training data (2024-05-01) | earliest evaluation date 2025-01-01. This says nothing about BioCLIP 2.5, whose card gives no snapshot date. |
| pass | no evaluation observation was created before the first one dated 2025-01-01 | observation numbers run from 257012724 to 404616041; the smallest number among observations dated 2025-01-01 is 257012724; observations with a smaller number: 0. A smaller number would mean an observation created earlier than 2025 and dated later. |
| pass | the month column is the month of the date | 0 rows disagree |
| pass | no two evaluation rows share a value of id | 6000 distinct values in 6000 rows |
| pass | no two evaluation rows share a value of gbif_id | 6000 distinct values in 6000 rows |
| pass | no two evaluation rows share a value of obs_url | 6000 distinct values in 6000 rows |
| pass | no two evaluation rows share a value of photo_url | 6000 distinct values in 6000 rows |
| pass | the split is the stated function of gbif_id alone (tools/species/build_eval.py, split_of) | 0 rows disagree; val 1803, test 4197 |
| pass | in the species list the twelve monthly counts add up to the total, and species are sorted by total | 5911 species; 0 whose months do not add up; sorted: True |
| pass | no GBIF species key appears twice in the list | 5911 keys, 5911 distinct |
| note | scientific names carried by more than one species key | 1: {"Salvia azurea": [8283204, 2927067]}. Their sentence rows are identical, so the later key can never be the top answer; photos of it on the test split: 0. |
| pass | an evaluation row's name and kind of eye equal the species list's for the same key | 0 rows disagree |
| note | test photos whose species is not in the list at all | 36 of 4197, so a recognizer held to the list can reach at most 0.9914. |
| pass | vectors of bioclip-b16 line up with the manifest and the species list | 5 files checked; all 6,000 ids in manifest order, no values missing; label rows carry the list's keys and scientific names in the list's order |
| pass | vectors of bioclip2-l14 line up with the manifest and the species list | 4 files checked; all 6,000 ids in manifest order, no values missing; label rows carry the list's keys and scientific names in the list's order |
| pass | vectors of bioclip25-h14 line up with the manifest and the species list | 4 files checked; all 6,000 ids in manifest order, no values missing; label rows carry the list's keys and scientific names in the list's order |
| pass | vectors of bioclip25-mobile-fastvit line up with the manifest and the species list | 1 files checked; all 6,000 ids in manifest order, no values missing; label rows carry the list's keys and scientific names in the list's order |
| pass | vectors of clip-b32 line up with the manifest and the species list | 4 files checked; all 6,000 ids in manifest order, no values missing; label rows carry the list's keys and scientific names in the list's order |
| pass | vectors of mobileclip2-s0 line up with the manifest and the species list | 4 files checked; all 6,000 ids in manifest order, no values missing; label rows carry the list's keys and scientific names in the list's order |
| pass | vectors of siglip2-b16 line up with the manifest and the species list | 4 files checked; all 6,000 ids in manifest order, no values missing; label rows carry the list's keys and scientific names in the list's order |
| pass | vectors of tinyclip-39m-16 line up with the manifest and the species list | 8 files checked; all 6,000 ids in manifest order, no values missing; label rows carry the list's keys and scientific names in the list's order |
| pass | vectors of tinyclip-40m-32 line up with the manifest and the species list | 7 files checked; all 6,000 ids in manifest order, no values missing; label rows carry the list's keys and scientific names in the list's order |
| pass | vectors of tinyclip-61m-32 line up with the manifest and the species list | 7 files checked; all 6,000 ids in manifest order, no values missing; label rows carry the list's keys and scientific names in the list's order |
| pass | vectors of tinyclip-8m-16 line up with the manifest and the species list | 8 files checked; all 6,000 ids in manifest order, no values missing; label rows carry the list's keys and scientific names in the list's order |
| note | label files whose kind of eye differs from the species list | 9 label sets (bioclip-b16, mobileclip2-s0, siglip2-b16) carry another kind of eye than the list in 1 of 5911 rows. The studies take the kind from the species list, so no number here is touched; a slot built from these label files would show the earlier kinds. |
| note | label rows made from an earlier species.json | 15 label sets (of bioclip2-l14, bioclip25-h14, clip-b32, tinyclip-40m-32, tinyclip-61m-32) were made before the list's English names were revised: 645 of 5911 rows carry an English name the list no longer has (keys, scientific names and kinds agree in every row). Results for species_sci are unaffected; results for species_com and species_taxon_com describe the earlier names and would change if the rows were made again. |
| note | label rows made from an earlier species.json | 9 label sets (of bioclip-b16, mobileclip2-s0, siglip2-b16) were made before the list's English names were revised: 2099 of 5911 rows carry an English name the list no longer has (keys, scientific names and kinds agree in every row). Results for species_sci are unaffected; results for species_com and species_taxon_com describe the earlier names and would change if the rows were made again. |
| pass | test photos with an almost identical photo on val (clip-b32 cosine above 0.98) | 0 of 4197 test photos |
| pass | test photos with an almost identical photo on val (bioclip2-l14 cosine above 0.999) | 0 of 4197 test photos |
| note | how tightly BioCLIP 2 groups a species | 1470 of 4197 test photos have a val photo within cosine 0.95, and for 1454 of those it is the same species. Photos of one species sit close together in this model, which is why a list of names is enough for it. |
| pass | every training photo is dated on or before 2024-12-31 | 84808 rows; latest 2024-12-31; rows after: 0 |
| note | no gbif_id is shared between the training and the evaluation photos | the training manifest's gbif_id column is empty (it was built from iNaturalist's open-data files, which carry no GBIF record id), so this comparison says nothing; the dates and the photo numbers below do the work |
| pass | no obs_url is shared between the training and the evaluation photos | 0 shared; 84808 of 84808 training rows carry a value |
| pass | no photo_url is shared between the training and the evaluation photos | 0 shared; 84808 of 84808 training rows carry a value |
| pass | no photo number is shared between the training and the evaluation photos | 6000 evaluation and 84808 training photo numbers read from the addresses; shared: 0; addresses without a number: 0 |
| note | training observations can be compared with evaluation observations by number | 0 of 84808 training rows give the observation by its number; the others give it by its UUID, which the evaluation manifest does not hold. An observation has one date, and every training row is dated on or before 2024-12-31 while every evaluation row is dated after it, so no observation can be on both sides. |
| pass | no training photo appears twice | 0 repeated photo addresses in 84808 rows |
| pass | the kind of eye of every training row is the species list's | 0 rows disagree (the studies take the kind from the species list by the row's species key) |
| note | training photos per species | 84808 photos of 5467 species (most for one species: 60); rows without a species key: 0; species keys outside the list: 0; list species without a training photo: 444 |
| pass | no two rows of the extra set share an id or a photo | 10240 rows, 10240 ids, 10240 photo addresses |
| pass | the extra set's test rows come from COCO's val2017 and its train rows from train2017 | 0 rows disagree. COCO keeps the two apart, so no photo is on both sides. |
| note | how the extra set is cut (tools/eval/kinds.py) | fit: cat 983, deer 1016, dog 974, none 1628, person 1343; tune: cat 517, deer 484, dog 526, none 872, person 657; test: cat 77, deer 200, dog 63, none 500, person 400. `fit` (two thirds of COCO's train rows by a hash of the id) may be used to fit a kind head, `tune` joins the wildlife tuning photos for the kind decision, `test` is only reported. |
| pass | extra-set vectors `coco-kinds` of tinyclip-39m-16 line up with the manifest | 10240 vectors, 10240 ids, of 10240 manifest rows; by part: fit 5944, tune 3056, test 1240 |
| pass | extra-set vectors `coco-kinds.wasm-int8-per-channel` of tinyclip-39m-16 line up with the manifest | 1240 vectors, 1240 ids, of 10240 manifest rows; by part: fit 0, tune 0, test 1240 |
| pass | extra-set test photos with an almost identical fitting or tuning photo for tinyclip-39m-16 (cosine above 0.995) | 0 of 1240 |
| pass | extra-set vectors `coco-kinds` of tinyclip-8m-16 line up with the manifest | 10240 vectors, 10240 ids, of 10240 manifest rows; by part: fit 5944, tune 3056, test 1240 |
| pass | extra-set vectors `coco-kinds.wasm-int8-per-channel` of tinyclip-8m-16 line up with the manifest | 1240 vectors, 1240 ids, of 10240 manifest rows; by part: fit 0, tune 0, test 1240 |
| pass | extra-set test photos with an almost identical fitting or tuning photo for tinyclip-8m-16 (cosine above 0.995) | 0 of 1240 |
