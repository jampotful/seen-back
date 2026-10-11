# bioclip2-l14 on the test split

_This file is written by `tools/eval/report.py` from `docs/eval/study1.json`. Rerun the script to change it._

Species rows made from the scientific name; settings chosen on `val`: {"min_n": 1, "lam": 2.0, "c": 1.0, "ratio": 0.012, "t_species": 100, "alpha_prior": 1.2, "species_in_list": 5911, "combinations_tried": 108}. Top-1 90.4% (89.4 to 91.3) without the prior and 92.4% (91.6 to 93.2) with it.

## By kind of eye

| Kind | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| cat | 11 | 90.9% (72.7 to 100.0) | 90.9% (72.7 to 100.0) | 81.8% |
| dog | 6 | 83.3% (50.0 to 100.0) | 83.3% (50.0 to 100.0) | 83.3% |
| squirrel | 36 | 97.2% (91.7 to 100.0) | 100.0% (100.0 to 100.0) | 94.4% |
| deer | 36 | 97.2% (91.7 to 100.0) | 100.0% (100.0 to 100.0) | 91.7% |
| rabbit | 31 | 100.0% (100.0 to 100.0) | 100.0% (100.0 to 100.0) | 100.0% |
| hawk | 82 | 91.5% (85.4 to 96.4) | 96.3% (92.7 to 100.0) | 92.7% |
| wader | 382 | 97.1% (95.3 to 98.7) | 99.0% (97.9 to 99.7) | 96.3% |
| bird | 531 | 91.5% (88.9 to 93.8) | 96.2% (94.5 to 97.7) | 91.5% |
| alligator | 110 | 97.3% (93.6 to 100.0) | 98.2% (95.5 to 100.0) | 91.8% |
| reptile | 268 | 93.3% (90.3 to 95.9) | 98.9% (97.4 to 100.0) | 89.9% |
| frog | 97 | 90.7% (84.5 to 95.9) | 99.0% (96.9 to 100.0) | 87.6% |
| bee | 126 | 89.7% (84.1 to 94.4) | 96.8% (93.7 to 99.2) | 86.5% |
| insect | 962 | 89.0% (87.0 to 90.8) | 96.8% (95.5 to 97.8) | 87.5% |
| plant | 1223 | 94.3% (92.9 to 95.4) | 98.1% (97.3 to 98.8) | 91.1% |
| other | 296 | 88.9% (85.1 to 92.2) | 95.3% (92.6 to 97.6) | 87.2% |

## By class

| Kingdom / class | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| Animalia / Insecta | 1088 | 89.1% (87.3 to 90.8) | 96.8% (95.7 to 97.8) | 87.4% |
| Animalia / Aves | 995 | 93.7% (92.2 to 95.2) | 97.3% (96.3 to 98.2) | 93.5% |
| Plantae / Magnoliopsida | 878 | 94.0% (92.4 to 95.4) | 98.2% (97.3 to 99.0) | 91.0% |
| Plantae / Liliopsida | 291 | 95.2% (92.8 to 97.6) | 97.9% (96.2 to 99.3) | 91.1% |
| Animalia / Squamata | 209 | 94.3% (90.9 to 97.1) | 99.0% (97.6 to 100.0) | 91.4% |
| Animalia / Arachnida | 154 | 90.9% (86.4 to 95.5) | 94.8% (90.9 to 98.0) | 89.0% |
| Animalia / Mammalia | 139 | 93.5% (89.2 to 97.1) | 96.4% (92.8 to 99.3) | 90.6% |
| Animalia / Crocodylia | 110 | 97.3% (93.6 to 100.0) | 98.2% (95.5 to 100.0) | 91.8% |
| Animalia / Amphibia | 101 | 89.1% (82.2 to 95.0) | 99.0% (97.0 to 100.0) | 87.1% |
| Animalia / Testudines | 59 | 89.8% (81.4 to 96.6) | 98.3% (94.9 to 100.0) | 84.8% |
| Fungi / Agaricomycetes | 39 | 92.3% (84.6 to 100.0) | 97.4% (92.3 to 100.0) | 89.7% |
| Plantae / Polypodiopsida | 38 | 97.4% (92.1 to 100.0) | 100.0% (100.0 to 100.0) | 94.7% |
| all other classes | 96 | 88.5% (82.3 to 93.8) | 96.9% (92.7 to 100.0) | 86.5% |

## By how often the species was recorded before 2025

| Records before 2025 | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| not in the list | 36 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 0.0% |
| 1 or 2 records | 58 | 70.7% (58.6 to 82.8) | 96.6% (91.4 to 100.0) | 79.3% |
| 3 to 9 | 138 | 75.4% (68.1 to 82.6) | 93.5% (89.1 to 97.1) | 81.2% |
| 10 to 49 | 468 | 87.4% (84.4 to 90.2) | 97.9% (96.4 to 98.9) | 88.2% |
| 50 to 199 | 1195 | 93.7% (92.3 to 95.1) | 98.7% (98.1 to 99.3) | 91.7% |
| 200 or more | 2302 | 95.7% (94.9 to 96.5) | 98.5% (98.0 to 99.0) | 92.3% |

## By calendar month

| Month | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| 01 | 208 | 89.9% (86.1 to 93.8) | 95.2% (92.3 to 97.6) | 88.9% |
| 02 | 251 | 93.2% (90.0 to 96.0) | 96.8% (94.4 to 98.8) | 90.0% |
| 03 | 458 | 91.5% (88.9 to 93.9) | 98.9% (97.8 to 99.8) | 90.2% |
| 04 | 755 | 91.9% (89.9 to 93.8) | 96.3% (94.8 to 97.6) | 88.1% |
| 05 | 383 | 93.5% (90.9 to 95.8) | 97.1% (95.3 to 98.7) | 91.4% |
| 06 | 317 | 89.9% (86.4 to 93.1) | 97.5% (95.6 to 99.1) | 88.6% |
| 07 | 384 | 91.9% (89.1 to 94.5) | 98.7% (97.4 to 99.7) | 91.1% |
| 08 | 368 | 93.5% (90.8 to 95.9) | 97.3% (95.4 to 98.6) | 91.8% |
| 09 | 454 | 95.4% (93.4 to 97.4) | 98.5% (97.4 to 99.6) | 93.0% |
| 10 | 227 | 94.3% (91.2 to 96.9) | 97.4% (95.2 to 99.1) | 92.5% |
| 11 | 258 | 91.1% (87.6 to 94.6) | 97.7% (95.7 to 99.2) | 89.1% |
| 12 | 134 | 91.0% (86.6 to 95.5) | 97.8% (94.8 to 100.0) | 91.0% |

## Kind of eye from the kind phrases: what was said (columns) for each true kind (rows)

Accuracy 76.1% (74.8 to 77.4). Photos called `person`: 0.00%; called `none`: 0.00% (the test split holds neither).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | person | other | none |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 4 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 |
| dog | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 |
| squirrel | 0 | 0 | 33 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| deer | 0 | 0 | 0 | 20 | 0 | 0 | 12 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 |
| rabbit | 0 | 0 | 1 | 0 | 19 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 |
| hawk | 0 | 0 | 0 | 0 | 0 | 37 | 13 | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| wader | 0 | 0 | 0 | 1 | 0 | 1 | 373 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bird | 0 | 0 | 0 | 0 | 0 | 4 | 100 | 398 | 0 | 0 | 0 | 0 | 4 | 4 | 0 | 21 | 0 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 102 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 |
| reptile | 0 | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 1 | 170 | 0 | 0 | 0 | 2 | 0 | 84 | 0 |
| frog | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 78 | 0 | 1 | 0 | 0 | 17 | 0 |
| bee | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 84 | 27 | 1 | 0 | 14 | 0 |
| insect | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 6 | 0 | 2 | 0 | 5 | 740 | 32 | 0 | 176 | 0 |
| plant | 0 | 0 | 0 | 0 | 0 | 0 | 17 | 7 | 0 | 1 | 1 | 11 | 201 | 919 | 0 | 66 | 0 |
| other | 0 | 0 | 1 | 0 | 0 | 0 | 4 | 1 | 0 | 0 | 0 | 0 | 52 | 21 | 0 | 217 | 0 |

## Kind of eye taken from the top species, with the prior

Accuracy 98.3% (97.9 to 98.7).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | other |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| dog | 0 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| squirrel | 0 | 0 | 35 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| deer | 0 | 0 | 0 | 35 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| rabbit | 0 | 0 | 0 | 0 | 31 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| hawk | 0 | 0 | 0 | 0 | 0 | 78 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| wader | 1 | 0 | 0 | 1 | 0 | 0 | 377 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| bird | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 520 | 0 | 3 | 1 | 0 | 1 | 1 | 1 |
| alligator | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 107 | 1 | 0 | 0 | 0 | 0 | 1 |
| reptile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 263 | 1 | 1 | 0 | 0 | 1 |
| frog | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 96 | 0 | 0 | 0 | 0 |
| bee | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 119 | 1 | 6 | 0 |
| insect | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 950 | 9 | 1 |
| plant | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 4 | 1216 | 0 |
| other | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 4 | 5 | 284 |

## Commonest mistakes

Of 283 wrong answers for species that are in the list, 81 named another species of the same genus and 126 another species of the same family. 36 test photos show a species that is not in the list.

| Photos | The species | What was said | Observations |
|---:|---|---|---|
| 6 | *Archilochus colubris* (Ruby-throated Hummingbird) | *Cardinalis cardinalis* (Northern Cardinal) | [278267288](https://www.inaturalist.org/observations/278267288) [278383970](https://www.inaturalist.org/observations/278383970) [278395753](https://www.inaturalist.org/observations/278395753) |
| 4 | *Graminorthezia tillandsiae* (spanish moss orthezia) | *Tillandsia usneoides* (Spanish moss) | [271498111](https://www.inaturalist.org/observations/271498111) [271500303](https://www.inaturalist.org/observations/271500303) [271498942](https://www.inaturalist.org/observations/271498942) |
| 3 | *Phalacrocorax auritus* (Double-crested Cormorant) | *Anhinga anhinga* (Anhinga) | [321884842](https://www.inaturalist.org/observations/321884842) [327603431](https://www.inaturalist.org/observations/327603431) [359654897](https://www.inaturalist.org/observations/359654897) |
| 3 | *Dryophytes squirellus* (Squirrel Tree Frog) | *Dryophytes cinereus* (Green Treefrog) | [267517969](https://www.inaturalist.org/observations/267517969) [342504076](https://www.inaturalist.org/observations/342504076) [383147252](https://www.inaturalist.org/observations/383147252) |
| 3 | *Archilochus colubris* (Ruby-throated Hummingbird) | *Anolis sagrei* (Brown Anole) | [278380991](https://www.inaturalist.org/observations/278380991) [278380461](https://www.inaturalist.org/observations/278380461) [385091686](https://www.inaturalist.org/observations/385091686) |
| 2 | *Grus canadensis* (Sandhill Crane) | *Ardea herodias* (Great Blue Heron) | [295376145](https://www.inaturalist.org/observations/295376145) [352125613](https://www.inaturalist.org/observations/352125613) |
| 2 | *Nerodia fasciata* (Banded Watersnake) | *Agkistrodon conanti* (Florida Cottonmouth) | [268837470](https://www.inaturalist.org/observations/268837470) [311253240](https://www.inaturalist.org/observations/311253240) |
| 2 | *Camponotus floridanus* (Florida Carpenter Ant) | *Camponotus castaneus* (Chestnut Carpenter Ant) | [301708584](https://www.inaturalist.org/observations/301708584) [335856635](https://www.inaturalist.org/observations/335856635) |
| 2 | *Buteo jamaicensis* (Red-tailed Hawk) | *Buteo lineatus* (Red-shouldered Hawk) | [261257447](https://www.inaturalist.org/observations/261257447) [355843776](https://www.inaturalist.org/observations/355843776) |
| 2 | *Petiveria alliacea* (Guinea Hen Weed) | *Asimina parviflora* (Small-Flower Pawpaw) | [257407360](https://www.inaturalist.org/observations/257407360) [371088073](https://www.inaturalist.org/observations/371088073) |
| 2 | *Paroxya atlantica* (Atlantic Grasshopper) | *Paroxya clavuligera* (Olive-green Swamp Grasshopper) | [316206719](https://www.inaturalist.org/observations/316206719) [376439818](https://www.inaturalist.org/observations/376439818) |
| 2 | *Asimina pygmaea* (Dwarf pawpaw) | *Asimina longifolia* (polecatbush) | [272449846](https://www.inaturalist.org/observations/272449846) [389620097](https://www.inaturalist.org/observations/389620097) |
| 2 | *Quiscalus quiscula* (Common Grackle) | *Quiscalus major* (Boat-tailed Grackle) | [262597663](https://www.inaturalist.org/observations/262597663) [331849210](https://www.inaturalist.org/observations/331849210) |
| 2 | *Hermeuptychia intricata* (Intricate Satyr) | *Hermeuptychia hermes* (Hermes Satyr) | [328536302](https://www.inaturalist.org/observations/328536302) [387041453](https://www.inaturalist.org/observations/387041453) |
| 2 | *Schistocerca serialis* (Cuban bird grasshopper) | *Schistocerca americana* (American Bird Grasshopper) | [265451336](https://www.inaturalist.org/observations/265451336) [384288171](https://www.inaturalist.org/observations/384288171) |
