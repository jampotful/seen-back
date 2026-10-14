# Precision audit 2, 14 October 2026 (sweeps 5 to 31, web and intake files)

Second run of the precision test of `docs/views/research/THOROUGH.md`, by Opus, after `audit-2026-10-14.md` and `recheck-1.md`.

## Sample

Pool: `docs/views/evidence/sweep-*.jsonl` for sweeps 5 to 31 (sweep 23 and 24 have no evidence file; sweep-21 and sweep-25 were rechecked whole in recheck 1 and are left out), the web method files `birds-met`, `herps-met`, `insects-met`, `mammals-met`, and `intake-2` to `intake-8` (the `-failed` files, `reread-1`, `jumper` and `recheck-1-fixed` left out). The 20 records of the first audit and the records retracted in `docs/views/audit/ALL.jsonl` are skipped. Records of fish, sharks, spiders, scorpions, cephalopods, stomatopods and the few with no order are outside the five views and not drawn (59 records).

View by order: insects (the insect orders), birds (the avian orders), mammals, herps (Testudines, Crocodylia, Anura, Caudata, Squamata), plants (orders ending in -ales). Seed 20261014 (`random.Random`), 12 per view without replacement, weight 3 for partial records and 1 otherwise, weight divided by 4 once a file already has three records in the view. 31 of the 60 are partial. An id is `<file>:<line>`.

Each source URL was opened with WebFetch, which returns a summary, so each quote was checked by asking for the exact string and the nearest verbatim sentence; where a page was blocked the record is `unverifiable`. Verdicts: `correct`; `requote` (value right, quote not on the page or stitched); `regrade`; `retarget` (value is on another page or in another work); `retract` (the page does not support the value); `unverifiable`. Corrections are in `docs/views/recheck/recheck-2.jsonl`; no evidence file is edited.

## Results

| # | id | view | taxon / trait | grade | partial | verdict | note |
|---|---|---|---|---|---|---|---|
| 1 | sweep-19:14 | plants | Helianthus annuus / sense_light_nonvisual | m | yes | pending |  |
| 2 | sweep-9:13 | plants | Arisaema triphyllum / diel | m | no | pending |  |
| 3 | sweep-20:1 | plants | Centranthus ruber / sense_chemical | m | yes | pending |  |
| 4 | sweep-20:8 | plants | Chamaecrista fasciculata / diel | m | yes | pending |  |
| 5 | sweep-16:9 | plants | Passiflora foetida / diel | m | yes | pending |  |
| 6 | sweep-12:4 | plants | Dactylorhiza majalis / sense_chemical | m | yes | pending |  |
| 7 | sweep-13:4 | plants | Ulmus pumila / sense_light_nonvisual | m | yes | pending |  |
| 8 | sweep-15:11 | plants | Crataegus monogyna / sense_chemical | m | yes | pending |  |
| 9 | sweep-20:5 | plants | Ornithogalum umbellatum / diel | m | yes | pending |  |
| 10 | sweep-29:8 | plants | Marchantia polymorpha / sense_light_nonvisual | m | yes | pending |  |
| 11 | sweep-14:1 | plants | Jacobaea vulgaris / sense_light_nonvisual | m | yes | pending |  |
| 12 | sweep-11:7 | plants | Athyrium filix-femina / sense_light_nonvisual | m | yes | pending |  |
| 13 | sweep-29:2 | insects | Gryllus bimaculatus / lambda_max_nm | m | yes | pending |  |
| 14 | sweep-15:13 | insects | Colias eurytheme / fov_h_deg | m | yes | pending |  |
| 15 | sweep-8:9 | insects | Halyomorpha halys / spectral_range_nm | m | yes | pending |  |
| 16 | intake-2:28 | insects | Paravespula vulgaris / lambda_max_nm | m | no | pending |  |
| 17 | insects-met:37 | insects | Callophrys sheridanii / lambda_max_nm | m | no | pending |  |
| 18 | intake-5:39 | insects | Solenopsis invicta / new trait | m | no | pending |  |
| 19 | insects-met:4 | insects | Heliconius erato / filter_pigments | m | no | pending |  |
| 20 | insects-met:24 | insects | Popillia japonica / receptor_classes | m | no | pending |  |
| 21 | sweep-31:1 | insects | Deilephila elpenor / interommatidial_deg | m | yes | pending |  |
| 22 | sweep-12:10 | insects | Chauliognathus pulchellus / spectral_range_nm | m | yes | pending |  |
| 23 | sweep-11:15 | insects | Lymantria xylina / interommatidial_deg | m | yes | pending |  |
| 24 | sweep-22:6 | insects | Heliconius erato cyrbia / interommatidial_deg | m | yes | pending |  |
| 25 | sweep-15:6 | birds | Cuculus poliocephalus / oil_droplets | m | yes | pending |  |
| 26 | sweep-6:16 | birds | Podiceps cristatus / binocular_deg | m | no | pending |  |
| 27 | sweep-19:10 | birds | Gyps africanus / binocular_deg | m | yes | pending |  |
| 28 | sweep-11:10 | birds | Sturnella magna / acuity_cpd | m | yes | pending |  |
| 29 | sweep-6:32 | birds | Selasphorus platycercus / spectral_range_nm | m | no | pending |  |
| 30 | intake-3:40 | birds | Grus americana / lambda_max_nm | m | no | pending |  |
| 31 | sweep-6:10 | birds | Sterna striata / colour_vision | m | no | pending |  |
| 32 | sweep-19:9 | birds | Gyps fulvus / binocular_deg | m | yes | pending |  |
| 33 | intake-8:6 | birds | Strix aluco / lambda_max_nm | m | no | pending |  |
| 34 | intake-4:30 | birds | Grus americana / eye_movement | m | no | pending |  |
| 35 | intake-8:15 | birds | Bubo virginianus / cff_hz | m | no | pending |  |
| 36 | sweep-12:8 | birds | Platycercus elegans / lambda_max_nm | m | yes | pending |  |
| 37 | intake-7:27 | mammals | Camelus dromedarius / tapetum | m | no | pending |  |
| 38 | sweep-29:4 | mammals | Oryctolagus cuniculus / tapetum | m | yes | pending |  |
| 39 | intake-6:18 | mammals | Myocastor coypus / fovea | m | yes | pending |  |
| 40 | intake-8:35 | mammals | Capra hircus / tapetum | m | yes | pending |  |
| 41 | intake-5:31 | mammals | Capra hircus / fov_h_deg | m | no | pending |  |
| 42 | intake-6:16 | mammals | Myocastor coypus / pupil_shape | m | yes | pending |  |
| 43 | intake-3:3 | mammals | Bos taurus / acuity_cpd | m | no | pending |  |
| 44 | intake-3:5 | mammals | Bos taurus / fov_h_deg | m | no | pending |  |
| 45 | intake-5:24 | mammals | Bos taurus / lambda_max_nm | m | no | pending |  |
| 46 | sweep-27:9 | mammals | Equus caballus / receptor_classes | m | yes | pending |  |
| 47 | mammals-met:7 | mammals | Kerodon rupestris / pupil_shape | m | no | pending |  |
| 48 | intake-7:24 | mammals | Bos taurus / colour_vision | m | no | pending |  |
| 49 | herps-met:19 | herps | Bufo bufo / lambda_max_nm | m | no | pending |  |
| 50 | sweep-6:5 | herps | Trachemys scripta elegans / lambda_max_nm | m | no | pending |  |
| 51 | intake-8:28 | herps | Triturus cristatus / depth_cue | m | no | pending |  |
| 52 | sweep-19:2 | herps | Rhinella marina / motion | m | yes | pending |  |
| 53 | sweep-7:12 | herps | Bufo japonicus / motion | m | no | pending |  |
| 54 | herps-met:23 | herps | Dryophytes cinereus (as Hyla cinerea) / receptor_classes | g | no | pending |  |
| 55 | intake-3:50 | herps | Anura / pupil_shape | g | no | pending |  |
| 56 | herps-met:17 | herps | Rana temporaria / lambda_max_nm | m | no | pending |  |
| 57 | sweep-6:35 | herps | Trachemys scripta elegans (as Pseudemys scripta elegans) / acuity_cpd | m | no | pending |  |
| 58 | sweep-17:14 | herps | Chelonia mydas / lambda_max_nm | m | yes | pending |  |
| 59 | sweep-17:12 | herps | Chelonia mydas / fovea | m | yes | pending |  |
| 60 | sweep-7:10 | herps | Bufo bufo / motion | m | no | pending |  |

## Error rate

Checked 0 of 60; verifiable 0; wrong (requote, regrade, retarget or retract) 0: **0%**.

By batch (wrong / verifiable sampled):

| batch | sampled | verifiable | wrong | rate |
|---|---|---|---|---|
| herps-met | 3 | 0 | 0 | 0% |
| insects-met | 3 | 0 | 0 | 0% |
| intake-2 | 1 | 0 | 0 | 0% |
| intake-3 | 4 | 0 | 0 | 0% |
| intake-4 | 1 | 0 | 0 | 0% |
| intake-5 | 3 | 0 | 0 | 0% |
| intake-6 | 2 | 0 | 0 | 0% |
| intake-7 | 2 | 0 | 0 | 0% |
| intake-8 | 4 | 0 | 0 | 0% |
| mammals-met | 1 | 0 | 0 | 0% |
| sweep-6 | 5 | 0 | 0 | 0% |
| sweep-7 | 2 | 0 | 0 | 0% |
| sweep-8 | 1 | 0 | 0 | 0% |
| sweep-9 | 1 | 0 | 0 | 0% |
| sweep-11 | 3 | 0 | 0 | 0% |
| sweep-12 | 3 | 0 | 0 | 0% |
| sweep-13 | 1 | 0 | 0 | 0% |
| sweep-14 | 1 | 0 | 0 | 0% |
| sweep-15 | 3 | 0 | 0 | 0% |
| sweep-16 | 1 | 0 | 0 | 0% |
| sweep-17 | 2 | 0 | 0 | 0% |
| sweep-19 | 4 | 0 | 0 | 0% |
| sweep-20 | 3 | 0 | 0 | 0% |
| sweep-22 | 1 | 0 | 0 | 0% |
| sweep-27 | 1 | 0 | 0 | 0% |
| sweep-29 | 3 | 0 | 0 | 0% |
| sweep-31 | 1 | 0 | 0 | 0% |

