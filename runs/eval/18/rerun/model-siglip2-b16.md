# siglip2-b16 on the test split

_This file is written by `tools/eval/report.py` from `docs/eval/study1.json`. Rerun the script to change it._

Species rows made from the scientific name; settings chosen on `val`: {"min_n": 1, "lam": 2.0, "c": 0.1, "ratio": 0.008, "t_species": 100, "alpha_prior": 0.8, "species_in_list": 5911, "combinations_tried": 108}. Top-1 9.5% (8.6 to 10.4) without the prior and 16.7% (15.6 to 17.8) with it.

## By kind of eye

| Kind | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| cat | 11 | 0.0% (0.0 to 0.0) | 27.3% (0.0 to 54.5) | 0.0% |
| dog | 6 | 66.7% (33.3 to 100.0) | 83.3% (50.0 to 100.0) | 83.3% |
| squirrel | 36 | 0.0% (0.0 to 0.0) | 2.8% (0.0 to 8.3) | 0.0% |
| deer | 36 | 55.6% (38.9 to 69.4) | 69.4% (52.8 to 83.3) | 13.9% |
| rabbit | 31 | 93.5% (83.9 to 100.0) | 100.0% (100.0 to 100.0) | 90.3% |
| hawk | 82 | 21.9% (13.4 to 31.7) | 30.5% (20.7 to 41.5) | 23.2% |
| wader | 382 | 7.1% (4.7 to 10.0) | 19.1% (14.9 to 23.3) | 7.8% |
| bird | 531 | 14.9% (11.7 to 18.1) | 26.0% (22.2 to 29.9) | 12.2% |
| alligator | 110 | 91.8% (86.4 to 96.4) | 100.0% (100.0 to 100.0) | 0.0% |
| reptile | 268 | 10.1% (6.7 to 13.8) | 26.1% (20.9 to 31.7) | 7.5% |
| frog | 97 | 12.4% (6.2 to 19.6) | 24.7% (16.5 to 34.0) | 6.2% |
| bee | 126 | 9.5% (4.8 to 15.1) | 20.6% (14.3 to 27.8) | 1.6% |
| insect | 962 | 7.8% (6.2 to 9.5) | 16.5% (14.2 to 18.9) | 4.4% |
| plant | 1223 | 21.0% (18.8 to 23.2) | 30.4% (27.7 to 33.0) | 12.7% |
| other | 296 | 13.9% (9.8 to 17.9) | 28.0% (22.6 to 33.5) | 7.8% |

## By class

| Kingdom / class | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| Animalia / Insecta | 1088 | 8.0% (6.4 to 9.6) | 17.0% (14.7 to 19.3) | 4.0% |
| Animalia / Aves | 995 | 12.5% (10.4 to 14.6) | 23.7% (21.0 to 26.4) | 11.5% |
| Plantae / Magnoliopsida | 878 | 14.9% (12.8 to 17.2) | 23.9% (21.2 to 26.8) | 7.5% |
| Plantae / Liliopsida | 291 | 42.3% (36.8 to 47.8) | 52.2% (46.4 to 58.1) | 30.6% |
| Animalia / Squamata | 209 | 8.1% (4.8 to 12.0) | 22.5% (17.2 to 28.2) | 4.3% |
| Animalia / Arachnida | 154 | 18.2% (12.3 to 24.7) | 37.0% (29.2 to 44.8) | 10.4% |
| Animalia / Mammalia | 139 | 41.7% (33.8 to 50.4) | 53.2% (44.6 to 61.9) | 30.9% |
| Animalia / Crocodylia | 110 | 91.8% (86.4 to 96.4) | 100.0% (100.0 to 100.0) | 0.0% |
| Animalia / Amphibia | 101 | 11.9% (5.9 to 18.8) | 23.8% (15.8 to 31.7) | 5.9% |
| Animalia / Testudines | 59 | 17.0% (8.5 to 27.1) | 39.0% (27.1 to 52.5) | 18.6% |
| Fungi / Agaricomycetes | 39 | 5.1% (0.0 to 12.8) | 12.8% (2.6 to 23.1) | 2.6% |
| Plantae / Polypodiopsida | 38 | 5.3% (0.0 to 13.2) | 15.8% (5.3 to 28.9) | 0.0% |
| all other classes | 96 | 7.3% (2.1 to 12.5) | 16.7% (9.4 to 24.0) | 1.0% |

## By how often the species was recorded before 2025

| Records before 2025 | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| not in the list | 36 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 0.0% |
| 1 or 2 records | 58 | 1.7% (0.0 to 5.2) | 12.1% (3.5 to 20.7) | 17.2% |
| 3 to 9 | 138 | 0.7% (0.0 to 2.2) | 2.2% (0.0 to 5.1) | 1.5% |
| 10 to 49 | 468 | 3.2% (1.7 to 4.9) | 8.6% (6.0 to 11.1) | 5.1% |
| 50 to 199 | 1195 | 7.6% (6.1 to 9.2) | 16.2% (14.0 to 18.3) | 5.4% |
| 200 or more | 2302 | 25.8% (24.0 to 27.6) | 39.2% (37.1 to 41.2) | 13.0% |

## By calendar month

| Month | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| 01 | 208 | 16.4% (11.5 to 21.6) | 26.9% (21.1 to 33.2) | 8.2% |
| 02 | 251 | 20.7% (15.9 to 25.9) | 31.9% (25.9 to 37.9) | 12.3% |
| 03 | 458 | 15.3% (12.2 to 18.6) | 28.0% (24.0 to 32.1) | 9.8% |
| 04 | 755 | 16.3% (13.6 to 18.9) | 26.1% (22.8 to 29.4) | 7.1% |
| 05 | 383 | 13.8% (10.4 to 17.0) | 25.9% (21.4 to 30.0) | 5.5% |
| 06 | 317 | 15.8% (12.0 to 19.9) | 24.3% (19.6 to 29.0) | 8.5% |
| 07 | 384 | 16.7% (12.8 to 20.6) | 28.1% (23.7 to 32.6) | 11.7% |
| 08 | 368 | 20.6% (16.6 to 25.0) | 30.2% (25.5 to 34.8) | 14.9% |
| 09 | 454 | 15.6% (12.3 to 18.9) | 26.0% (22.0 to 30.0) | 8.8% |
| 10 | 227 | 14.5% (10.1 to 19.4) | 26.0% (20.7 to 32.2) | 7.0% |
| 11 | 258 | 20.2% (15.5 to 25.2) | 30.2% (24.8 to 35.7) | 12.8% |
| 12 | 134 | 17.9% (11.9 to 24.6) | 25.4% (18.7 to 32.8) | 11.9% |

## Kind of eye from the kind phrases: what was said (columns) for each true kind (rows)

Accuracy 79.8% (78.6 to 81.0). Photos called `person`: 0.48%; called `none`: 0.19% (the test split holds neither).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | person | other | none |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 8 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| dog | 0 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| squirrel | 0 | 0 | 30 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |
| deer | 0 | 1 | 1 | 28 | 1 | 0 | 2 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| rabbit | 0 | 0 | 0 | 0 | 30 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| hawk | 0 | 0 | 1 | 0 | 0 | 72 | 3 | 4 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| wader | 0 | 0 | 1 | 0 | 5 | 7 | 321 | 29 | 11 | 0 | 3 | 1 | 0 | 3 | 0 | 0 | 1 |
| bird | 1 | 0 | 9 | 1 | 3 | 32 | 63 | 391 | 10 | 3 | 2 | 3 | 2 | 3 | 4 | 0 | 4 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 106 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 0 |
| reptile | 0 | 0 | 6 | 0 | 0 | 1 | 0 | 1 | 32 | 201 | 5 | 0 | 9 | 9 | 2 | 0 | 2 |
| frog | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 92 | 0 | 1 | 0 | 0 | 0 | 0 |
| bee | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 111 | 9 | 5 | 0 | 0 | 0 |
| insect | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 2 | 13 | 17 | 86 | 819 | 19 | 2 | 0 | 0 |
| plant | 0 | 0 | 4 | 0 | 0 | 1 | 1 | 3 | 5 | 3 | 14 | 36 | 18 | 1131 | 6 | 1 | 0 |
| other | 0 | 1 | 7 | 2 | 3 | 0 | 1 | 2 | 4 | 18 | 29 | 8 | 165 | 46 | 6 | 4 | 0 |

## Kind of eye taken from the top species, with the prior

Accuracy 63.1% (61.6 to 64.6).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | other |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 7 | 2 | 1 |
| dog | 0 | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| squirrel | 0 | 0 | 3 | 1 | 4 | 1 | 1 | 1 | 3 | 1 | 19 | 0 | 0 | 2 | 0 |
| deer | 0 | 1 | 0 | 22 | 0 | 0 | 0 | 1 | 4 | 1 | 1 | 0 | 0 | 6 | 0 |
| rabbit | 0 | 0 | 0 | 0 | 30 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| hawk | 0 | 0 | 0 | 1 | 0 | 52 | 5 | 6 | 11 | 0 | 0 | 0 | 0 | 7 | 0 |
| wader | 0 | 0 | 0 | 2 | 3 | 4 | 166 | 47 | 152 | 0 | 1 | 0 | 1 | 6 | 0 |
| bird | 0 | 0 | 0 | 3 | 1 | 24 | 54 | 328 | 90 | 1 | 1 | 1 | 4 | 23 | 1 |
| alligator | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 101 | 3 | 0 | 0 | 0 | 3 | 0 |
| reptile | 0 | 0 | 1 | 0 | 0 | 23 | 1 | 9 | 29 | 141 | 4 | 0 | 27 | 31 | 2 |
| frog | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 12 | 4 | 3 | 71 | 0 | 6 | 0 | 0 |
| bee | 0 | 0 | 0 | 0 | 0 | 1 | 15 | 11 | 2 | 1 | 0 | 47 | 14 | 23 | 12 |
| insect | 0 | 0 | 1 | 11 | 0 | 39 | 76 | 54 | 39 | 19 | 22 | 29 | 551 | 52 | 69 |
| plant | 0 | 0 | 0 | 1 | 0 | 1 | 78 | 9 | 28 | 2 | 5 | 9 | 31 | 1050 | 9 |
| other | 0 | 0 | 0 | 4 | 0 | 9 | 12 | 7 | 28 | 20 | 26 | 3 | 72 | 32 | 83 |

## Commonest mistakes

Of 3459 wrong answers for species that are in the list, 80 named another species of the same genus and 402 another species of the same family. 36 test photos show a species that is not in the list.

| Photos | The species | What was said | Observations |
|---:|---|---|---|
| 32 | *Ardea herodias* (Great Blue Heron) | *Alligator mississippiensis* (American Alligator) | [260942706](https://www.inaturalist.org/observations/260942706) [262785093](https://www.inaturalist.org/observations/262785093) [267218589](https://www.inaturalist.org/observations/267218589) |
| 29 | *Gallinula chloropus* (Eurasian Moorhen) | *Alligator mississippiensis* (American Alligator) | [265543372](https://www.inaturalist.org/observations/265543372) [267252393](https://www.inaturalist.org/observations/267252393) [270346625](https://www.inaturalist.org/observations/270346625) |
| 19 | *Ardea alba* (Great Egret) | *Mycteria americana* (Wood Stork) | [260943580](https://www.inaturalist.org/observations/260943580) [265466294](https://www.inaturalist.org/observations/265466294) [274807407](https://www.inaturalist.org/observations/274807407) |
| 19 | *Sciurus carolinensis* (Eastern Gray Squirrel) | *Dryophytes squirellus* (Squirrel Tree Frog) | [257370520](https://www.inaturalist.org/observations/257370520) [261044049](https://www.inaturalist.org/observations/261044049) [267839697](https://www.inaturalist.org/observations/267839697) |
| 18 | *Ardea alba* (Great Egret) | *Eudocimus albus* (White Ibis) | [270078942](https://www.inaturalist.org/observations/270078942) [277584973](https://www.inaturalist.org/observations/277584973) [299984207](https://www.inaturalist.org/observations/299984207) |
| 18 | *Grus canadensis* (Sandhill Crane) | *Alligator mississippiensis* (American Alligator) | [272686807](https://www.inaturalist.org/observations/272686807) [273608410](https://www.inaturalist.org/observations/273608410) [273850499](https://www.inaturalist.org/observations/273850499) |
| 16 | *Dryophytes cinereus* (Green Treefrog) | *Anaxyrus terrestris* (Southern Toad) | [260555675](https://www.inaturalist.org/observations/260555675) [270615900](https://www.inaturalist.org/observations/270615900) [268377828](https://www.inaturalist.org/observations/268377828) |
| 15 | *Anolis carolinensis* (Green Anole) | *Romalea microptera* (Florida Lubber) | [333979200](https://www.inaturalist.org/observations/333979200) [273759312](https://www.inaturalist.org/observations/273759312) [278583584](https://www.inaturalist.org/observations/278583584) |
| 15 | *Buteo lineatus* (Red-shouldered Hawk) | *Pandion haliaetus* (Osprey) | [260084564](https://www.inaturalist.org/observations/260084564) [261801604](https://www.inaturalist.org/observations/261801604) [263572358](https://www.inaturalist.org/observations/263572358) |
| 15 | *Egretta tricolor* (Tricolored Heron) | *Alligator mississippiensis* (American Alligator) | [260943635](https://www.inaturalist.org/observations/260943635) [278128783](https://www.inaturalist.org/observations/278128783) [283799371](https://www.inaturalist.org/observations/283799371) |
| 14 | *Egretta caerulea* (Little Blue Heron) | *Alligator mississippiensis* (American Alligator) | [284789978](https://www.inaturalist.org/observations/284789978) [290387170](https://www.inaturalist.org/observations/290387170) [295093495](https://www.inaturalist.org/observations/295093495) |
| 13 | *Anolis sagrei* (Brown Anole) | *Buteo lineatus* (Red-shouldered Hawk) | [267928528](https://www.inaturalist.org/observations/267928528) [273329673](https://www.inaturalist.org/observations/273329673) [278619741](https://www.inaturalist.org/observations/278619741) |
| 13 | *Anolis sagrei* (Brown Anole) | *Hemidactylus turcicus* (Mediterranean Gecko) | [268131176](https://www.inaturalist.org/observations/268131176) [274016130](https://www.inaturalist.org/observations/274016130) [280391862](https://www.inaturalist.org/observations/280391862) |
| 13 | *Anolis sagrei* (Brown Anole) | *Hemidactylus mabouia* (Tropical House Gecko) | [266222507](https://www.inaturalist.org/observations/266222507) [267849426](https://www.inaturalist.org/observations/267849426) [267849290](https://www.inaturalist.org/observations/267849290) |
| 13 | *Apalone ferox* (Florida Softshell Turtle) | *Alligator mississippiensis* (American Alligator) | [294596085](https://www.inaturalist.org/observations/294596085) [298940176](https://www.inaturalist.org/observations/298940176) [311323216](https://www.inaturalist.org/observations/311323216) |
