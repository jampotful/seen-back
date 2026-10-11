# bioclip-b16 on the test split

_This file is written by `tools/eval/report.py` from `docs/eval/study1.json`. Rerun the script to change it._

Species rows made from the taxonomy and English name; settings chosen on `val`: {"min_n": 1, "lam": 0.0, "c": 1.0, "ratio": 0.016, "t_species": 70, "alpha_prior": 1.12, "species_in_list": 5911, "combinations_tried": 108}. Top-1 62.3% (60.7 to 63.8) without the prior and 69.5% (68.0 to 71.0) with it.

## By kind of eye

| Kind | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| cat | 11 | 45.5% (18.2 to 72.7) | 81.8% (54.5 to 100.0) | 72.7% |
| dog | 6 | 50.0% (16.7 to 83.3) | 50.0% (16.7 to 83.3) | 50.0% |
| squirrel | 36 | 83.3% (69.4 to 94.4) | 86.1% (72.2 to 97.2) | 77.8% |
| deer | 36 | 75.0% (61.1 to 88.9) | 86.1% (75.0 to 97.2) | 66.7% |
| rabbit | 31 | 96.8% (90.3 to 100.0) | 100.0% (100.0 to 100.0) | 83.9% |
| hawk | 82 | 75.6% (65.8 to 84.2) | 90.2% (82.9 to 96.3) | 73.2% |
| wader | 382 | 79.6% (75.4 to 83.5) | 93.2% (90.6 to 95.5) | 75.6% |
| bird | 531 | 68.7% (64.6 to 72.5) | 83.8% (80.6 to 87.0) | 59.1% |
| alligator | 110 | 72.7% (64.5 to 80.9) | 81.8% (74.6 to 89.1) | 50.9% |
| reptile | 268 | 70.9% (65.7 to 76.5) | 92.2% (88.8 to 95.2) | 64.2% |
| frog | 97 | 59.8% (49.5 to 69.1) | 87.6% (80.4 to 93.8) | 52.6% |
| bee | 126 | 59.5% (50.8 to 68.2) | 81.8% (74.6 to 88.1) | 54.0% |
| insect | 962 | 66.0% (63.1 to 68.9) | 83.7% (81.3 to 85.9) | 60.3% |
| plant | 1223 | 71.3% (68.7 to 73.8) | 86.8% (85.0 to 88.7) | 62.5% |
| other | 296 | 61.5% (55.7 to 66.5) | 81.8% (77.0 to 86.2) | 57.8% |

## By class

| Kingdom / class | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| Animalia / Insecta | 1088 | 65.3% (62.5 to 68.1) | 83.5% (81.3 to 85.8) | 59.6% |
| Animalia / Aves | 995 | 73.5% (70.8 to 76.1) | 87.9% (85.8 to 90.0) | 66.6% |
| Plantae / Magnoliopsida | 878 | 72.4% (69.5 to 75.5) | 86.6% (84.3 to 88.8) | 63.8% |
| Plantae / Liliopsida | 291 | 68.4% (63.2 to 73.9) | 87.3% (83.2 to 91.1) | 60.5% |
| Animalia / Squamata | 209 | 74.2% (67.9 to 79.9) | 92.8% (89.0 to 96.2) | 68.4% |
| Animalia / Arachnida | 154 | 63.6% (56.5 to 71.4) | 84.4% (78.6 to 90.3) | 62.3% |
| Animalia / Mammalia | 139 | 71.9% (64.8 to 79.1) | 84.9% (78.4 to 90.6) | 68.3% |
| Animalia / Crocodylia | 110 | 72.7% (64.5 to 80.9) | 81.8% (74.6 to 89.1) | 50.9% |
| Animalia / Amphibia | 101 | 60.4% (50.5 to 69.3) | 87.1% (80.2 to 93.1) | 51.5% |
| Animalia / Testudines | 59 | 59.3% (47.5 to 71.2) | 89.8% (81.4 to 96.6) | 49.1% |
| Fungi / Agaricomycetes | 39 | 53.8% (38.5 to 69.2) | 66.7% (51.3 to 79.5) | 46.2% |
| Plantae / Polypodiopsida | 38 | 73.7% (60.5 to 86.8) | 89.5% (79.0 to 97.4) | 57.9% |
| all other classes | 96 | 66.7% (57.3 to 76.0) | 87.5% (80.2 to 93.8) | 58.3% |

## By how often the species was recorded before 2025

| Records before 2025 | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| not in the list | 36 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 0.0% |
| 1 or 2 records | 58 | 36.2% (24.1 to 48.3) | 63.8% (51.7 to 75.9) | 48.3% |
| 3 to 9 | 138 | 40.6% (32.6 to 48.5) | 68.8% (61.6 to 76.8) | 48.5% |
| 10 to 49 | 468 | 52.8% (48.3 to 57.0) | 76.9% (73.1 to 80.6) | 52.6% |
| 50 to 199 | 1195 | 66.7% (64.1 to 69.5) | 86.1% (84.2 to 88.0) | 62.4% |
| 200 or more | 2302 | 78.1% (76.3 to 79.7) | 90.9% (89.7 to 92.0) | 66.3% |

## By calendar month

| Month | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| 01 | 208 | 65.4% (59.1 to 71.6) | 78.4% (73.1 to 84.1) | 56.7% |
| 02 | 251 | 71.3% (65.3 to 76.9) | 84.1% (79.3 to 88.4) | 63.7% |
| 03 | 458 | 67.9% (63.8 to 72.3) | 87.1% (84.1 to 90.2) | 62.2% |
| 04 | 755 | 69.0% (65.7 to 72.2) | 86.2% (83.7 to 88.7) | 61.5% |
| 05 | 383 | 72.6% (67.9 to 76.8) | 88.8% (85.4 to 91.9) | 66.1% |
| 06 | 317 | 70.0% (65.0 to 75.1) | 86.1% (82.0 to 89.9) | 65.3% |
| 07 | 384 | 66.7% (61.7 to 71.4) | 85.7% (82.3 to 89.1) | 60.9% |
| 08 | 368 | 71.5% (66.6 to 76.1) | 87.0% (83.4 to 90.2) | 63.9% |
| 09 | 454 | 70.9% (66.7 to 75.1) | 87.0% (83.7 to 90.1) | 64.1% |
| 10 | 227 | 70.0% (64.3 to 76.2) | 88.5% (84.6 to 92.5) | 59.0% |
| 11 | 258 | 68.6% (62.8 to 74.0) | 84.1% (79.5 to 88.4) | 57.0% |
| 12 | 134 | 70.2% (61.9 to 77.6) | 85.8% (79.8 to 91.8) | 64.2% |

## Kind of eye from the kind phrases: what was said (columns) for each true kind (rows)

Accuracy 45.5% (44.0 to 47.0). Photos called `person`: 14.34%; called `none`: 3.55% (the test split holds neither).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | person | other | none |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 8 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dog | 0 | 4 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| squirrel | 0 | 0 | 30 | 1 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| deer | 0 | 0 | 0 | 30 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| rabbit | 0 | 0 | 2 | 0 | 29 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| hawk | 1 | 1 | 2 | 0 | 0 | 65 | 11 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| wader | 2 | 2 | 2 | 3 | 0 | 1 | 354 | 1 | 7 | 0 | 3 | 0 | 0 | 1 | 6 | 0 | 0 |
| bird | 24 | 9 | 59 | 5 | 3 | 13 | 202 | 96 | 12 | 2 | 4 | 7 | 5 | 50 | 39 | 1 | 0 |
| alligator | 2 | 1 | 0 | 0 | 0 | 0 | 4 | 2 | 97 | 0 | 2 | 1 | 0 | 0 | 0 | 1 | 0 |
| reptile | 3 | 10 | 30 | 0 | 5 | 0 | 4 | 0 | 63 | 96 | 4 | 1 | 0 | 22 | 28 | 1 | 1 |
| frog | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 90 | 0 | 1 | 1 | 0 | 0 | 0 |
| bee | 1 | 0 | 0 | 7 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 107 | 6 | 0 | 3 | 0 | 1 |
| insect | 67 | 7 | 16 | 73 | 11 | 12 | 20 | 2 | 7 | 16 | 16 | 49 | 172 | 145 | 300 | 10 | 39 |
| plant | 34 | 25 | 7 | 30 | 8 | 0 | 7 | 0 | 30 | 2 | 6 | 101 | 20 | 719 | 147 | 0 | 87 |
| other | 13 | 8 | 10 | 17 | 8 | 0 | 6 | 0 | 4 | 4 | 11 | 20 | 13 | 71 | 77 | 13 | 21 |

## Kind of eye taken from the top species, with the prior

Accuracy 92.2% (91.4 to 93.0).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | other |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 5 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 1 |
| dog | 0 | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| squirrel | 0 | 0 | 30 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 0 |
| deer | 0 | 1 | 0 | 29 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 3 |
| rabbit | 0 | 0 | 0 | 0 | 31 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| hawk | 0 | 0 | 0 | 0 | 0 | 75 | 1 | 4 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| wader | 0 | 0 | 1 | 0 | 0 | 3 | 356 | 11 | 1 | 4 | 0 | 0 | 1 | 3 | 2 |
| bird | 0 | 1 | 2 | 0 | 0 | 8 | 23 | 467 | 0 | 9 | 0 | 1 | 4 | 15 | 1 |
| alligator | 1 | 0 | 0 | 0 | 0 | 2 | 10 | 0 | 80 | 5 | 6 | 0 | 0 | 4 | 2 |
| reptile | 0 | 0 | 1 | 0 | 2 | 0 | 2 | 5 | 4 | 246 | 1 | 0 | 1 | 4 | 2 |
| frog | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 4 | 89 | 0 | 1 | 2 | 0 |
| bee | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 106 | 3 | 14 | 1 |
| insect | 0 | 0 | 2 | 0 | 0 | 1 | 1 | 4 | 0 | 11 | 2 | 2 | 907 | 19 | 13 |
| plant | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 2 | 1 | 4 | 5 | 3 | 13 | 1190 | 2 |
| other | 1 | 0 | 3 | 5 | 1 | 1 | 1 | 2 | 1 | 6 | 0 | 2 | 14 | 4 | 255 |

## Commonest mistakes

Of 1243 wrong answers for species that are in the list, 185 named another species of the same genus and 416 another species of the same family. 36 test photos show a species that is not in the list.

| Photos | The species | What was said | Observations |
|---:|---|---|---|
| 9 | *Anolis sagrei* (Brown Anole) | *Anolis carolinensis* (Green Anole) | [264832050](https://www.inaturalist.org/observations/264832050) [265329104](https://www.inaturalist.org/observations/265329104) [266681336](https://www.inaturalist.org/observations/266681336) |
| 9 | *Dryophytes squirellus* (Squirrel Tree Frog) | *Dryophytes cinereus* (Green Treefrog) | [267517969](https://www.inaturalist.org/observations/267517969) [277900760](https://www.inaturalist.org/observations/277900760) [287282858](https://www.inaturalist.org/observations/287282858) |
| 5 | *Anolis carolinensis* (Green Anole) | *Anolis sagrei* (Brown Anole) | [311709818](https://www.inaturalist.org/observations/311709818) [314400629](https://www.inaturalist.org/observations/314400629) [332918102](https://www.inaturalist.org/observations/332918102) |
| 5 | *Gallinula chloropus* (Eurasian Moorhen) | *Porphyrio martinica* (Purple Gallinule) | [260198166](https://www.inaturalist.org/observations/260198166) [277205090](https://www.inaturalist.org/observations/277205090) [334111790](https://www.inaturalist.org/observations/334111790) |
| 5 | *Dryophytes squirellus* (Squirrel Tree Frog) | *Osteopilus septentrionalis* (Cuban Tree Frog) | [273882305](https://www.inaturalist.org/observations/273882305) [282454567](https://www.inaturalist.org/observations/282454567) [287189527](https://www.inaturalist.org/observations/287189527) |
| 5 | *Tillandsia recurvata* (ballmoss) | *Tillandsia usneoides* (Spanish moss) | [289906730](https://www.inaturalist.org/observations/289906730) [298420694](https://www.inaturalist.org/observations/298420694) [339189736](https://www.inaturalist.org/observations/339189736) |
| 5 | *Archilochus colubris* (Ruby-throated Hummingbird) | *Thryothorus ludovicianus* (Carolina Wren) | [278380991](https://www.inaturalist.org/observations/278380991) [278380461](https://www.inaturalist.org/observations/278380461) [278383970](https://www.inaturalist.org/observations/278383970) |
| 5 | *Asimina pygmaea* (Dwarf pawpaw) | *Asimina longifolia* (polecatbush) | [272449846](https://www.inaturalist.org/observations/272449846) [282876106](https://www.inaturalist.org/observations/282876106) [286648515](https://www.inaturalist.org/observations/286648515) |
| 4 | *Alligator mississippiensis* (American Alligator) | *Ardea herodias* (Great Blue Heron) | [321884797](https://www.inaturalist.org/observations/321884797) [328634164](https://www.inaturalist.org/observations/328634164) [357360853](https://www.inaturalist.org/observations/357360853) |
| 4 | *Alligator mississippiensis* (American Alligator) | *Lithobates catesbeianus* (American Bullfrog) | [299187184](https://www.inaturalist.org/observations/299187184) [346176466](https://www.inaturalist.org/observations/346176466) [360464711](https://www.inaturalist.org/observations/360464711) |
| 4 | *Grus canadensis* (Sandhill Crane) | *Mycteria americana* (Wood Stork) | [331586594](https://www.inaturalist.org/observations/331586594) [332213432](https://www.inaturalist.org/observations/332213432) [339090700](https://www.inaturalist.org/observations/339090700) |
| 4 | *Bubulcus ibis* (Cattle Egret) | *Ardea alba* (Great Egret) | [260046688](https://www.inaturalist.org/observations/260046688) [315377099](https://www.inaturalist.org/observations/315377099) [344927480](https://www.inaturalist.org/observations/344927480) |
| 4 | *Strix varia* (Barred Owl) | *Buteo lineatus* (Red-shouldered Hawk) | [261487976](https://www.inaturalist.org/observations/261487976) [269039776](https://www.inaturalist.org/observations/269039776) [295866527](https://www.inaturalist.org/observations/295866527) |
| 4 | *Quiscalus quiscula* (Common Grackle) | *Quiscalus major* (Boat-tailed Grackle) | [262597663](https://www.inaturalist.org/observations/262597663) [331849210](https://www.inaturalist.org/observations/331849210) [349647830](https://www.inaturalist.org/observations/349647830) |
| 3 | *Tillandsia usneoides* (Spanish moss) | *Quercus virginiana* (southern live oak) | [298493902](https://www.inaturalist.org/observations/298493902) [302664633](https://www.inaturalist.org/observations/302664633) [330619072](https://www.inaturalist.org/observations/330619072) |
