# Checks for leakage and for mistakes in the inputs

_This file is written by `tools/eval/report.py` from `docs/eval/checks.json`. Rerun the script to change it._

| Verdict | Check | What was found |
|---|---|---|
| pass | every evaluation photo is dated after the species list's last record (2024-12-31) | 6000 rows; earliest 2025-01-01, latest 2026-09-29; rows on or before 2024-12-31: 0 |
| pass | every evaluation photo is dated after the GBIF snapshot behind BioCLIP 2's training data (2024-05-01) | earliest evaluation date 2025-01-01. This says nothing about BioCLIP 2.5, whose card gives no snapshot date. |
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
| note | test photos whose species is not in the list at all | 36 of 4197 (so a recognizer held to the list can reach at most 0.9914) |
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
| note | label rows made from an earlier species.json | 21 label sets (of bioclip2-l14, bioclip25-h14, clip-b32, tinyclip-39m-16, tinyclip-40m-32, tinyclip-61m-32, tinyclip-8m-16) were made before the list's English names were revised: 645 of 5911 rows carry an English name the list no longer has (keys, scientific names and kinds agree in every row). Results for species_sci are unaffected; results for species_com and species_taxon_com describe the earlier names and would change if the rows were made again. |
| note | label rows made from an earlier species.json | 9 label sets (of bioclip-b16, mobileclip2-s0, siglip2-b16) were made before the list's English names were revised: 2099 of 5911 rows carry an English name the list no longer has (keys, scientific names and kinds agree in every row). Results for species_sci are unaffected; results for species_com and species_taxon_com describe the earlier names and would change if the rows were made again. |
| pass | test photos with an almost identical photo on val (clip-b32 cosine above 0.98) | 0 of 4197 test photos |
| pass | test photos with an almost identical photo on val (bioclip2-l14 cosine above 0.999) | 0 of 4197 test photos |
| note | how tightly BioCLIP 2 groups a species | 1470 of 4197 test photos have a val photo within cosine 0.95, and for 1454 of those it is the same species. Photos of one species sit close together in this model, which is why a list of names is enough for it. |
| waiting | training photos share no record with the evaluation photos | data/train/alachua-pre2025/manifest.csv is not published yet |
