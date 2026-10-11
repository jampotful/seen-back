# bioclip25-h14 on the test split

_This file is written by `tools/eval/report.py` from `docs/eval/study1.json`. Rerun the script to change it._

Species rows made from the scientific name; settings chosen on `val`: {"min_n": 1, "lam": 0.0, "c": 1.0, "ratio": 0.016, "t_species": 50, "alpha_prior": 0.8, "species_in_list": 5911, "combinations_tried": 108}. Top-1 92.9% (92.1 to 93.7) without the prior and 93.4% (92.7 to 94.2) with it.

## By kind of eye

| Kind | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| cat | 11 | 90.9% (72.7 to 100.0) | 90.9% (72.7 to 100.0) | 90.9% |
| dog | 6 | 83.3% (50.0 to 100.0) | 83.3% (50.0 to 100.0) | 83.3% |
| squirrel | 36 | 97.2% (91.7 to 100.0) | 100.0% (100.0 to 100.0) | 94.4% |
| deer | 36 | 91.7% (80.6 to 100.0) | 94.4% (86.1 to 100.0) | 91.7% |
| rabbit | 31 | 100.0% (100.0 to 100.0) | 100.0% (100.0 to 100.0) | 100.0% |
| hawk | 82 | 92.7% (86.6 to 97.6) | 98.8% (96.3 to 100.0) | 93.9% |
| wader | 382 | 95.3% (92.9 to 97.4) | 98.7% (97.4 to 99.7) | 95.8% |
| bird | 531 | 93.0% (90.6 to 95.3) | 96.0% (94.2 to 97.5) | 92.3% |
| alligator | 110 | 97.3% (93.6 to 100.0) | 97.3% (93.6 to 100.0) | 93.6% |
| reptile | 268 | 93.3% (90.3 to 96.3) | 98.5% (97.0 to 99.6) | 92.9% |
| frog | 97 | 90.7% (84.5 to 95.9) | 100.0% (100.0 to 100.0) | 93.8% |
| bee | 126 | 88.1% (81.8 to 93.7) | 96.8% (93.7 to 99.2) | 88.1% |
| insect | 962 | 91.9% (90.2 to 93.6) | 97.5% (96.6 to 98.4) | 90.8% |
| plant | 1223 | 94.8% (93.4 to 95.9) | 98.3% (97.5 to 98.9) | 94.4% |
| other | 296 | 92.6% (89.5 to 95.3) | 96.6% (94.6 to 98.3) | 91.5% |

## By class

| Kingdom / class | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| Animalia / Insecta | 1088 | 91.5% (89.8 to 93.1) | 97.4% (96.4 to 98.4) | 90.4% |
| Animalia / Aves | 995 | 93.9% (92.5 to 95.3) | 97.3% (96.2 to 98.2) | 93.8% |
| Plantae / Magnoliopsida | 878 | 94.9% (93.4 to 96.2) | 98.3% (97.4 to 99.1) | 94.4% |
| Plantae / Liliopsida | 291 | 94.5% (91.8 to 96.9) | 98.3% (96.6 to 99.7) | 94.5% |
| Animalia / Squamata | 209 | 93.8% (90.0 to 96.7) | 98.6% (96.7 to 100.0) | 93.8% |
| Animalia / Arachnida | 154 | 92.2% (87.7 to 96.1) | 96.1% (92.9 to 98.7) | 90.9% |
| Animalia / Mammalia | 139 | 93.5% (89.2 to 97.1) | 96.4% (92.8 to 99.3) | 92.8% |
| Animalia / Crocodylia | 110 | 97.3% (93.6 to 100.0) | 97.3% (93.6 to 100.0) | 93.6% |
| Animalia / Amphibia | 101 | 91.1% (85.2 to 96.0) | 100.0% (100.0 to 100.0) | 94.1% |
| Animalia / Testudines | 59 | 91.5% (83.0 to 98.3) | 98.3% (94.9 to 100.0) | 89.8% |
| Fungi / Agaricomycetes | 39 | 97.4% (92.3 to 100.0) | 97.4% (92.3 to 100.0) | 94.9% |
| Plantae / Polypodiopsida | 38 | 97.4% (92.1 to 100.0) | 100.0% (100.0 to 100.0) | 97.4% |
| all other classes | 96 | 91.7% (86.4 to 96.9) | 96.9% (92.7 to 100.0) | 91.7% |

## By how often the species was recorded before 2025

| Records before 2025 | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| not in the list | 36 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 0.0% |
| 1 or 2 records | 58 | 87.9% (79.3 to 96.5) | 98.3% (94.8 to 100.0) | 86.2% |
| 3 to 9 | 138 | 80.4% (73.9 to 87.0) | 96.4% (92.8 to 99.3) | 84.1% |
| 10 to 49 | 468 | 90.6% (87.8 to 93.2) | 98.9% (97.9 to 99.8) | 90.6% |
| 50 to 199 | 1195 | 95.6% (94.4 to 96.7) | 99.1% (98.5 to 99.6) | 94.8% |
| 200 or more | 2302 | 95.3% (94.4 to 96.1) | 98.3% (97.8 to 98.8) | 94.5% |

## By calendar month

| Month | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| 01 | 208 | 89.4% (85.1 to 93.3) | 95.7% (92.8 to 98.1) | 90.4% |
| 02 | 251 | 94.8% (92.0 to 97.2) | 97.6% (95.6 to 99.2) | 93.6% |
| 03 | 458 | 93.7% (91.3 to 95.9) | 98.9% (97.8 to 99.8) | 94.1% |
| 04 | 755 | 92.5% (90.3 to 94.3) | 97.0% (95.6 to 98.2) | 91.3% |
| 05 | 383 | 93.2% (90.6 to 95.6) | 97.4% (95.6 to 98.7) | 92.7% |
| 06 | 317 | 92.1% (89.0 to 95.0) | 96.2% (94.0 to 98.1) | 90.8% |
| 07 | 384 | 94.5% (92.2 to 96.6) | 99.0% (97.9 to 99.7) | 93.8% |
| 08 | 368 | 93.5% (90.8 to 95.9) | 98.4% (97.0 to 99.5) | 93.2% |
| 09 | 454 | 95.6% (93.6 to 97.4) | 98.7% (97.6 to 99.6) | 95.4% |
| 10 | 227 | 93.8% (90.8 to 96.5) | 97.8% (95.6 to 99.6) | 93.8% |
| 11 | 258 | 93.8% (90.7 to 96.5) | 97.3% (95.3 to 99.2) | 93.0% |
| 12 | 134 | 93.3% (88.8 to 97.0) | 97.0% (94.0 to 99.2) | 92.5% |

## Kind of eye from the kind phrases: what was said (columns) for each true kind (rows)

Accuracy 70.1% (68.7 to 71.4). Photos called `person`: 0.00%; called `none`: 0.00% (the test split holds neither).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | person | other | none |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 10 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dog | 0 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| squirrel | 0 | 0 | 33 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 |
| deer | 0 | 0 | 0 | 32 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| rabbit | 0 | 0 | 0 | 0 | 30 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| hawk | 0 | 0 | 1 | 0 | 0 | 68 | 9 | 0 | 1 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| wader | 1 | 0 | 1 | 0 | 0 | 2 | 361 | 0 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| bird | 3 | 0 | 5 | 0 | 3 | 6 | 194 | 105 | 17 | 2 | 4 | 1 | 106 | 62 | 0 | 23 | 0 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 107 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| reptile | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 26 | 211 | 0 | 1 | 8 | 0 | 0 | 20 | 0 |
| frog | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 96 | 0 | 0 | 0 | 0 | 1 | 0 |
| bee | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 107 | 16 | 3 | 0 | 0 | 0 |
| insect | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 2 | 0 | 0 | 13 | 870 | 29 | 0 | 44 | 0 |
| plant | 0 | 0 | 0 | 0 | 0 | 0 | 29 | 0 | 4 | 3 | 1 | 69 | 317 | 767 | 0 | 33 | 0 |
| other | 1 | 2 | 2 | 4 | 0 | 0 | 4 | 0 | 4 | 1 | 4 | 1 | 105 | 30 | 0 | 138 | 0 |

## Kind of eye taken from the top species, with the prior

Accuracy 98.1% (97.6 to 98.5).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | other |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 10 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dog | 0 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| squirrel | 0 | 0 | 36 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| deer | 0 | 0 | 0 | 33 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| rabbit | 0 | 0 | 0 | 0 | 31 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| hawk | 0 | 0 | 0 | 0 | 1 | 78 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| wader | 1 | 0 | 1 | 0 | 0 | 2 | 372 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| bird | 1 | 0 | 2 | 0 | 0 | 0 | 3 | 513 | 0 | 1 | 1 | 0 | 3 | 3 | 4 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 107 | 1 | 0 | 0 | 0 | 0 | 2 |
| reptile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 264 | 1 | 1 | 1 | 0 | 0 |
| frog | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 97 | 0 | 0 | 0 | 0 |
| bee | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 117 | 2 | 7 | 0 |
| insect | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 954 | 6 | 1 |
| plant | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 8 | 1211 | 1 |
| other | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 3 | 288 |

## Commonest mistakes

Of 240 wrong answers for species that are in the list, 70 named another species of the same genus and 111 another species of the same family. 36 test photos show a species that is not in the list.

| Photos | The species | What was said | Observations |
|---:|---|---|---|
| 4 | *Graminorthezia tillandsiae* (spanish moss orthezia) | *Tillandsia usneoides* (Spanish moss) | [271498111](https://www.inaturalist.org/observations/271498111) [271500303](https://www.inaturalist.org/observations/271500303) [271498942](https://www.inaturalist.org/observations/271498942) |
| 3 | *Anolis carolinensis* (Green Anole) | *Anolis sagrei* (Brown Anole) | [267634318](https://www.inaturalist.org/observations/267634318) [314400629](https://www.inaturalist.org/observations/314400629) [332918102](https://www.inaturalist.org/observations/332918102) |
| 2 | *Phalacrocorax auritus* (Double-crested Cormorant) | *Anhinga anhinga* (Anhinga) | [327603431](https://www.inaturalist.org/observations/327603431) [359654897](https://www.inaturalist.org/observations/359654897) |
| 2 | *Pontederia crassipes* (common water hyacinth) | *Aramus guarauna* (Limpkin) | [264089116](https://www.inaturalist.org/observations/264089116) [334163514](https://www.inaturalist.org/observations/334163514) |
| 2 | *Archilochus colubris* (Ruby-throated Hummingbird) | *Euglandina rosea* (Rosy Wolfsnail) | [278380461](https://www.inaturalist.org/observations/278380461) [385053392](https://www.inaturalist.org/observations/385053392) |
| 2 | *Amblyomma americanum* (Lone Star Tick) | *Ophiodothella angustissima* (no English name) | [261294259](https://www.inaturalist.org/observations/261294259) [261302406](https://www.inaturalist.org/observations/261302406) |
| 2 | *Chrysis fuscipennis* (no English name) | *Chrysis smaragdula* (no English name) | [306849679](https://www.inaturalist.org/observations/306849679) [309373875](https://www.inaturalist.org/observations/309373875) |
| 2 | *Schistocerca serialis* (Cuban bird grasshopper) | *Schistocerca americana* (American Bird Grasshopper) | [265451336](https://www.inaturalist.org/observations/265451336) [384288171](https://www.inaturalist.org/observations/384288171) |
| 2 | *Schistocerca alutacea* (Leather-colored Bird Grasshopper) | *Schistocerca obscura* (Obscure Bird Grasshopper) | [391573074](https://www.inaturalist.org/observations/391573074) [402761834](https://www.inaturalist.org/observations/402761834) |
| 1 | *Alligator mississippiensis* (American Alligator) | *Favolus tenuiculus* (Tropical White Polypore) | [259259877](https://www.inaturalist.org/observations/259259877) |
| 1 | *Alligator mississippiensis* (American Alligator) | *Pseudemys peninsularis* (Peninsular Cooter) | [321884797](https://www.inaturalist.org/observations/321884797) |
| 1 | *Alligator mississippiensis* (American Alligator) | *Lycoperdon curtisii* (Curtis's Puffball) | [259259324](https://www.inaturalist.org/observations/259259324) |
| 1 | *Anolis sagrei* (Brown Anole) | *Anolis carolinensis* (Green Anole) | [347848192](https://www.inaturalist.org/observations/347848192) |
| 1 | *Anolis sagrei* (Brown Anole) | *Eleutherodactylus planirostris* (Greenhouse Frog) | [400342618](https://www.inaturalist.org/observations/400342618) |
| 1 | *Anolis sagrei* (Brown Anole) | *Pycnoscelus surinamensis* (Surinam Cockroach) | [314339319](https://www.inaturalist.org/observations/314339319) |
