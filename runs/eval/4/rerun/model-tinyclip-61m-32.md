# tinyclip-61m-32 on the test split

_This file is written by `tools/eval/report.py` from `docs/eval/study1.json`. Rerun the script to change it._

Species rows made from the English name; settings chosen on `val`: {"min_n": 1, "lam": 2.0, "c": 0.1, "ratio": 0.024, "t_species": 50, "alpha_prior": 1.2, "species_in_list": 5911, "combinations_tried": 108}. Top-1 14.9% (13.8 to 16.0) without the prior and 27.9% (26.6 to 29.2) with it.

## By kind of eye

| Kind | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| cat | 11 | 18.2% (0.0 to 45.5) | 45.5% (18.2 to 72.7) | 0.0% |
| dog | 6 | 16.7% (0.0 to 50.0) | 16.7% (0.0 to 50.0) | 16.7% |
| squirrel | 36 | 55.6% (38.9 to 72.2) | 63.9% (47.2 to 80.6) | 27.8% |
| deer | 36 | 50.0% (33.3 to 66.7) | 77.8% (63.9 to 88.9) | 13.9% |
| rabbit | 31 | 83.9% (71.0 to 96.8) | 96.8% (90.3 to 100.0) | 67.7% |
| hawk | 82 | 52.4% (41.5 to 63.4) | 70.7% (61.0 to 80.5) | 36.6% |
| wader | 382 | 53.1% (48.4 to 58.1) | 83.0% (79.1 to 86.4) | 47.1% |
| bird | 531 | 34.1% (30.1 to 38.0) | 60.3% (56.1 to 64.4) | 24.7% |
| alligator | 110 | 92.7% (87.3 to 97.3) | 98.2% (95.5 to 100.0) | 49.1% |
| reptile | 268 | 38.4% (32.5 to 44.4) | 66.8% (61.6 to 72.4) | 11.6% |
| frog | 97 | 23.7% (15.5 to 33.0) | 54.6% (44.3 to 65.0) | 10.3% |
| bee | 126 | 14.3% (8.7 to 19.9) | 39.7% (30.9 to 48.4) | 2.4% |
| insect | 962 | 14.9% (12.7 to 17.3) | 31.6% (28.7 to 34.4) | 6.6% |
| plant | 1223 | 20.0% (17.8 to 22.3) | 33.0% (30.3 to 35.6) | 6.0% |
| other | 296 | 13.9% (10.1 to 17.9) | 28.7% (24.0 to 34.1) | 3.7% |

## By class

| Kingdom / class | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| Animalia / Insecta | 1088 | 14.8% (12.8 to 16.9) | 32.5% (29.9 to 35.3) | 6.1% |
| Animalia / Aves | 995 | 42.9% (39.8 to 45.9) | 69.8% (67.0 to 72.6) | 34.3% |
| Plantae / Magnoliopsida | 878 | 14.5% (12.2 to 16.9) | 26.3% (23.6 to 29.3) | 4.8% |
| Plantae / Liliopsida | 291 | 36.8% (31.3 to 42.3) | 50.5% (44.7 to 56.4) | 9.3% |
| Animalia / Squamata | 209 | 39.2% (32.5 to 45.9) | 65.5% (58.9 to 71.8) | 8.1% |
| Animalia / Arachnida | 154 | 13.0% (7.8 to 18.8) | 28.6% (21.4 to 35.7) | 1.9% |
| Animalia / Mammalia | 139 | 49.6% (41.7 to 58.3) | 68.3% (61.2 to 76.3) | 28.1% |
| Animalia / Crocodylia | 110 | 92.7% (87.3 to 97.3) | 98.2% (95.5 to 100.0) | 49.1% |
| Animalia / Amphibia | 101 | 22.8% (14.8 to 30.7) | 52.5% (43.6 to 62.4) | 10.9% |
| Animalia / Testudines | 59 | 35.6% (23.7 to 47.5) | 71.2% (59.3 to 81.4) | 23.7% |
| Fungi / Agaricomycetes | 39 | 15.4% (5.1 to 28.2) | 23.1% (10.3 to 35.9) | 2.6% |
| Plantae / Polypodiopsida | 38 | 18.4% (7.9 to 31.6) | 50.0% (34.2 to 65.8) | 5.3% |
| all other classes | 96 | 17.7% (10.4 to 26.0) | 31.2% (21.9 to 40.6) | 7.3% |

## By how often the species was recorded before 2025

| Records before 2025 | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| not in the list | 36 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 0.0% |
| 1 or 2 records | 58 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 3.5% |
| 3 to 9 | 138 | 0.7% (0.0 to 2.2) | 1.5% (0.0 to 3.6) | 5.1% |
| 10 to 49 | 468 | 1.5% (0.4 to 2.6) | 6.8% (4.7 to 9.2) | 4.5% |
| 50 to 199 | 1195 | 9.5% (8.0 to 11.3) | 30.1% (27.6 to 32.8) | 6.7% |
| 200 or more | 2302 | 45.5% (43.4 to 47.5) | 68.2% (66.2 to 70.1) | 22.3% |

## By calendar month

| Month | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| 01 | 208 | 30.8% (24.5 to 37.0) | 48.1% (41.3 to 54.8) | 23.6% |
| 02 | 251 | 32.7% (27.1 to 38.2) | 53.0% (47.0 to 59.4) | 17.9% |
| 03 | 458 | 26.9% (22.9 to 30.6) | 47.2% (42.8 to 51.7) | 14.2% |
| 04 | 755 | 27.2% (24.1 to 30.2) | 43.0% (39.5 to 46.5) | 13.0% |
| 05 | 383 | 29.8% (25.3 to 34.2) | 48.8% (43.9 to 53.8) | 17.0% |
| 06 | 317 | 24.6% (19.9 to 29.3) | 42.3% (36.9 to 47.6) | 12.6% |
| 07 | 384 | 26.8% (22.4 to 31.5) | 45.3% (40.1 to 50.3) | 13.5% |
| 08 | 368 | 28.0% (23.6 to 32.6) | 47.8% (42.7 to 53.0) | 12.8% |
| 09 | 454 | 26.4% (22.5 to 30.4) | 47.6% (43.0 to 52.0) | 13.2% |
| 10 | 227 | 25.1% (19.8 to 30.4) | 41.9% (35.7 to 48.0) | 13.2% |
| 11 | 258 | 30.6% (25.2 to 36.4) | 52.7% (46.5 to 58.5) | 14.7% |
| 12 | 134 | 30.6% (23.1 to 38.8) | 53.7% (45.5 to 62.7) | 26.1% |

## Kind of eye from the kind phrases: what was said (columns) for each true kind (rows)

Accuracy 72.6% (71.2 to 74.1). Photos called `person`: 0.05%; called `none`: 0.21% (the test split holds neither).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | person | other | none |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 6 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| dog | 0 | 2 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| squirrel | 0 | 0 | 30 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 3 | 0 | 1 | 0 |
| deer | 0 | 1 | 0 | 26 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 4 | 0 |
| rabbit | 0 | 0 | 4 | 0 | 24 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| hawk | 0 | 0 | 1 | 0 | 0 | 68 | 5 | 2 | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 2 | 0 |
| wader | 0 | 0 | 6 | 2 | 0 | 5 | 319 | 23 | 15 | 3 | 0 | 0 | 1 | 8 | 0 | 0 | 0 |
| bird | 4 | 2 | 14 | 1 | 1 | 64 | 105 | 271 | 15 | 11 | 1 | 1 | 5 | 15 | 1 | 13 | 7 |
| alligator | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 101 | 0 | 1 | 0 | 1 | 0 | 0 | 4 | 0 |
| reptile | 0 | 0 | 7 | 0 | 0 | 0 | 3 | 5 | 36 | 160 | 2 | 0 | 13 | 12 | 0 | 29 | 1 |
| frog | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 1 | 0 | 14 | 62 | 0 | 7 | 1 | 0 | 9 | 0 |
| bee | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 3 | 0 | 90 | 22 | 5 | 0 | 4 | 0 |
| insect | 0 | 0 | 2 | 0 | 1 | 4 | 1 | 4 | 1 | 57 | 13 | 76 | 719 | 35 | 0 | 49 | 0 |
| plant | 0 | 0 | 5 | 1 | 0 | 3 | 2 | 1 | 5 | 13 | 4 | 46 | 38 | 1092 | 0 | 12 | 1 |
| other | 1 | 0 | 7 | 3 | 1 | 4 | 0 | 0 | 3 | 23 | 3 | 17 | 119 | 37 | 1 | 77 | 0 |

## Kind of eye taken from the top species, with the prior

Accuracy 76.4% (75.2 to 77.6).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | other |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 3 | 3 | 0 |
| dog | 0 | 1 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| squirrel | 0 | 0 | 20 | 1 | 3 | 1 | 2 | 1 | 0 | 3 | 1 | 0 | 0 | 4 | 0 |
| deer | 0 | 0 | 0 | 20 | 1 | 0 | 2 | 0 | 2 | 1 | 0 | 0 | 1 | 7 | 2 |
| rabbit | 0 | 0 | 0 | 0 | 27 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 1 |
| hawk | 0 | 0 | 0 | 0 | 1 | 58 | 7 | 5 | 1 | 0 | 0 | 0 | 1 | 8 | 1 |
| wader | 0 | 0 | 2 | 3 | 1 | 2 | 313 | 31 | 8 | 3 | 0 | 0 | 2 | 16 | 1 |
| bird | 0 | 0 | 0 | 0 | 0 | 30 | 42 | 365 | 21 | 18 | 1 | 0 | 17 | 32 | 5 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 102 | 1 | 0 | 0 | 2 | 3 | 1 |
| reptile | 0 | 0 | 1 | 0 | 0 | 1 | 4 | 2 | 29 | 193 | 3 | 0 | 14 | 18 | 3 |
| frog | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 2 | 22 | 62 | 0 | 6 | 0 | 3 |
| bee | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 6 | 1 | 60 | 28 | 24 | 4 |
| insect | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 8 | 7 | 134 | 18 | 22 | 693 | 58 | 18 |
| plant | 0 | 0 | 2 | 1 | 0 | 0 | 2 | 4 | 3 | 13 | 2 | 0 | 52 | 1131 | 13 |
| other | 0 | 0 | 4 | 0 | 0 | 0 | 1 | 0 | 6 | 33 | 9 | 1 | 61 | 20 | 161 |

## Commonest mistakes

Of 2992 wrong answers for species that are in the list, 99 named another species of the same genus and 414 another species of the same family. 36 test photos show a species that is not in the list.

| Photos | The species | What was said | Observations |
|---:|---|---|---|
| 10 | *Anolis carolinensis* (Green Anole) | *Anolis sagrei* (Brown Anole) | [264044135](https://www.inaturalist.org/observations/264044135) [271728086](https://www.inaturalist.org/observations/271728086) [275047138](https://www.inaturalist.org/observations/275047138) |
| 10 | *Ardea alba* (Great Egret) | *Eudocimus albus* (White Ibis) | [270078942](https://www.inaturalist.org/observations/270078942) [289932455](https://www.inaturalist.org/observations/289932455) [311113087](https://www.inaturalist.org/observations/311113087) |
| 9 | *Apalone ferox* (Florida Softshell Turtle) | *Alligator mississippiensis* (American Alligator) | [265904896](https://www.inaturalist.org/observations/265904896) [321527076](https://www.inaturalist.org/observations/321527076) [322986936](https://www.inaturalist.org/observations/322986936) |
| 8 | *Dryophytes squirellus* (Squirrel Tree Frog) | *Osteopilus septentrionalis* (Cuban Tree Frog) | [273882305](https://www.inaturalist.org/observations/273882305) [277900760](https://www.inaturalist.org/observations/277900760) [294496288](https://www.inaturalist.org/observations/294496288) |
| 7 | *Dryophytes cinereus* (Green Treefrog) | *Osteopilus septentrionalis* (Cuban Tree Frog) | [282297697](https://www.inaturalist.org/observations/282297697) [291386145](https://www.inaturalist.org/observations/291386145) [296111604](https://www.inaturalist.org/observations/296111604) |
| 7 | *Liquidambar styraciflua* (American sweetgum) | *Cnidoscolus stimulosus* (spurge nettle) | [264029450](https://www.inaturalist.org/observations/264029450) [270791806](https://www.inaturalist.org/observations/270791806) [274956160](https://www.inaturalist.org/observations/274956160) |
| 7 | *Egretta tricolor* (Tricolored Heron) | *Egretta caerulea* (Little Blue Heron) | [257406135](https://www.inaturalist.org/observations/257406135) [278128783](https://www.inaturalist.org/observations/278128783) [283799371](https://www.inaturalist.org/observations/283799371) |
| 7 | *Coluber constrictor* (North American Racer) | *Nerodia fasciata* (Banded Watersnake) | [265087903](https://www.inaturalist.org/observations/265087903) [322680413](https://www.inaturalist.org/observations/322680413) [327292244](https://www.inaturalist.org/observations/327292244) |
| 6 | *Tillandsia usneoides* (Spanish moss) | *Anisomorpha buprestoides* (Southern Two-striped Walkingstick) | [298418777](https://www.inaturalist.org/observations/298418777) [300178060](https://www.inaturalist.org/observations/300178060) [300745080](https://www.inaturalist.org/observations/300745080) |
| 6 | *Grus canadensis* (Sandhill Crane) | *Eudocimus albus* (White Ibis) | [326935378](https://www.inaturalist.org/observations/326935378) [327290307](https://www.inaturalist.org/observations/327290307) [331586594](https://www.inaturalist.org/observations/331586594) |
| 6 | *Parthenocissus quinquefolia* (Virginia creeper) | *Cnidoscolus stimulosus* (spurge nettle) | [315730332](https://www.inaturalist.org/observations/315730332) [325062994](https://www.inaturalist.org/observations/325062994) [352810660](https://www.inaturalist.org/observations/352810660) |
| 6 | *Vitis rotundifolia* (muscadine) | *Cnidoscolus stimulosus* (spurge nettle) | [279112456](https://www.inaturalist.org/observations/279112456) [288354635](https://www.inaturalist.org/observations/288354635) [320220435](https://www.inaturalist.org/observations/320220435) |
| 6 | *Egretta tricolor* (Tricolored Heron) | *Ardea herodias* (Great Blue Heron) | [260943635](https://www.inaturalist.org/observations/260943635) [265466677](https://www.inaturalist.org/observations/265466677) [376538471](https://www.inaturalist.org/observations/376538471) |
| 6 | *Egretta thula* (Snowy Egret) | *Ardea alba* (Great Egret) | [278980010](https://www.inaturalist.org/observations/278980010) [267604475](https://www.inaturalist.org/observations/267604475) [296277085](https://www.inaturalist.org/observations/296277085) |
| 6 | *Phalacrocorax auritus* (Double-crested Cormorant) | *Anhinga anhinga* (Anhinga) | [289662493](https://www.inaturalist.org/observations/289662493) [302885778](https://www.inaturalist.org/observations/302885778) [321884842](https://www.inaturalist.org/observations/321884842) |
