# clip-b32 on the test split

_This file is written by `tools/eval/report.py` from `docs/eval/study1.json`. Rerun the script to change it._

Species rows made from the English name; settings chosen on `val`: {"min_n": 10, "lam": 0.0, "c": 0.1, "ratio": 0.012, "t_species": 70, "alpha_prior": 0.84, "species_in_list": 2143, "combinations_tried": 108}. Top-1 16.4% (15.3 to 17.5) without the prior and 31.8% (30.4 to 33.2) with it.

## By kind of eye

| Kind | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| cat | 11 | 18.2% (0.0 to 45.5) | 63.6% (36.4 to 90.9) | 18.2% |
| dog | 6 | 16.7% (0.0 to 50.0) | 50.0% (16.7 to 83.3) | 50.0% |
| squirrel | 36 | 61.1% (44.4 to 77.8) | 75.0% (61.1 to 88.9) | 13.9% |
| deer | 36 | 55.6% (38.9 to 72.2) | 77.8% (63.9 to 88.9) | 22.2% |
| rabbit | 31 | 83.9% (71.0 to 96.8) | 96.8% (90.3 to 100.0) | 25.8% |
| hawk | 82 | 56.1% (45.1 to 67.1) | 70.7% (61.0 to 81.7) | 35.4% |
| wader | 382 | 58.1% (53.4 to 63.1) | 83.8% (80.1 to 87.2) | 47.9% |
| bird | 531 | 39.7% (35.6 to 44.1) | 66.8% (62.7 to 70.6) | 22.2% |
| alligator | 110 | 89.1% (82.7 to 94.5) | 94.5% (90.0 to 98.2) | 63.6% |
| reptile | 268 | 42.9% (37.3 to 48.5) | 74.2% (69.0 to 79.5) | 22.4% |
| frog | 97 | 15.5% (8.2 to 22.7) | 70.1% (60.8 to 78.3) | 10.3% |
| bee | 126 | 24.6% (17.5 to 32.5) | 50.8% (42.1 to 58.7) | 7.9% |
| insect | 962 | 19.3% (16.9 to 21.7) | 36.1% (33.2 to 39.0) | 7.4% |
| plant | 1223 | 23.1% (20.7 to 25.5) | 37.0% (34.3 to 39.9) | 7.0% |
| other | 296 | 19.9% (15.5 to 24.7) | 40.5% (35.1 to 46.0) | 8.1% |

## By class

| Kingdom / class | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| Animalia / Insecta | 1088 | 19.9% (17.6 to 22.3) | 37.8% (35.0 to 40.8) | 7.4% |
| Animalia / Aves | 995 | 48.1% (45.2 to 51.2) | 73.7% (71.1 to 76.5) | 33.2% |
| Plantae / Magnoliopsida | 878 | 17.2% (14.7 to 19.6) | 31.9% (28.9 to 35.0) | 4.9% |
| Plantae / Liliopsida | 291 | 38.8% (33.3 to 44.7) | 50.2% (44.3 to 56.0) | 12.0% |
| Animalia / Squamata | 209 | 45.5% (38.3 to 52.1) | 76.1% (69.9 to 81.8) | 23.9% |
| Animalia / Arachnida | 154 | 21.4% (14.9 to 27.9) | 44.2% (36.4 to 51.9) | 8.4% |
| Animalia / Mammalia | 139 | 54.7% (46.0 to 62.6) | 75.5% (68.3 to 82.7) | 22.3% |
| Animalia / Crocodylia | 110 | 89.1% (82.7 to 94.5) | 94.5% (90.0 to 98.2) | 63.6% |
| Animalia / Amphibia | 101 | 14.8% (7.9 to 21.8) | 68.3% (59.4 to 77.2) | 10.9% |
| Animalia / Testudines | 59 | 33.9% (22.0 to 45.8) | 67.8% (55.9 to 79.7) | 17.0% |
| Fungi / Agaricomycetes | 39 | 17.9% (7.7 to 30.8) | 30.8% (17.9 to 46.2) | 0.0% |
| Plantae / Polypodiopsida | 38 | 28.9% (15.8 to 44.7) | 44.7% (28.9 to 60.5) | 13.2% |
| all other classes | 96 | 21.9% (14.6 to 30.2) | 40.6% (31.2 to 50.0) | 8.3% |

## By how often the species was recorded before 2025

| Records before 2025 | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| not in the list | 36 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 0.0% |
| 1 or 2 records | 58 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 5.2% |
| 3 to 9 | 138 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 4.3% |
| 10 to 49 | 468 | 4.5% (2.6 to 6.4) | 15.2% (12.2 to 18.6) | 7.0% |
| 50 to 199 | 1195 | 17.4% (15.3 to 19.6) | 41.3% (38.3 to 44.0) | 8.7% |
| 200 or more | 2302 | 48.1% (46.1 to 50.1) | 70.3% (68.5 to 72.2) | 23.5% |

## By calendar month

| Month | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| 01 | 208 | 33.7% (26.9 to 40.4) | 58.7% (51.9 to 64.9) | 19.2% |
| 02 | 251 | 39.8% (33.9 to 45.8) | 62.2% (56.6 to 67.7) | 20.7% |
| 03 | 458 | 32.3% (28.2 to 36.7) | 52.0% (47.6 to 56.5) | 15.5% |
| 04 | 755 | 29.9% (26.6 to 33.1) | 47.9% (44.2 to 51.5) | 15.4% |
| 05 | 383 | 31.3% (26.9 to 35.8) | 48.6% (43.6 to 53.5) | 18.3% |
| 06 | 317 | 29.0% (24.0 to 34.1) | 47.3% (42.0 to 53.0) | 14.8% |
| 07 | 384 | 27.1% (22.7 to 31.5) | 45.3% (40.1 to 50.3) | 14.6% |
| 08 | 368 | 31.8% (26.9 to 36.4) | 53.0% (47.8 to 58.1) | 17.4% |
| 09 | 454 | 32.2% (27.8 to 36.6) | 55.7% (51.1 to 60.4) | 14.3% |
| 10 | 227 | 31.3% (25.1 to 37.4) | 51.5% (44.9 to 57.7) | 11.9% |
| 11 | 258 | 36.4% (30.2 to 42.2) | 57.8% (51.9 to 63.6) | 18.6% |
| 12 | 134 | 35.8% (28.3 to 44.0) | 60.5% (52.2 to 68.7) | 23.1% |

## Kind of eye from the kind phrases: what was said (columns) for each true kind (rows)

Accuracy 72.0% (70.6 to 73.3). Photos called `person`: 0.17%; called `none`: 0.02% (the test split holds neither).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | person | other | none |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 6 | 0 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| dog | 0 | 3 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| squirrel | 0 | 0 | 31 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| deer | 0 | 2 | 1 | 21 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 |
| rabbit | 0 | 0 | 3 | 0 | 26 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| hawk | 0 | 0 | 4 | 0 | 0 | 63 | 8 | 3 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 1 | 0 |
| wader | 0 | 0 | 7 | 2 | 0 | 5 | 355 | 7 | 4 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| bird | 0 | 1 | 30 | 0 | 3 | 44 | 197 | 230 | 6 | 7 | 1 | 0 | 4 | 3 | 2 | 3 | 0 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 97 | 3 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| reptile | 0 | 0 | 16 | 0 | 1 | 0 | 9 | 2 | 28 | 168 | 5 | 1 | 14 | 6 | 0 | 18 | 0 |
| frog | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 10 | 78 | 0 | 5 | 0 | 0 | 3 | 0 |
| bee | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 105 | 14 | 4 | 0 | 2 | 0 |
| insect | 0 | 0 | 6 | 0 | 0 | 3 | 6 | 3 | 1 | 35 | 9 | 109 | 731 | 33 | 0 | 26 | 0 |
| plant | 0 | 0 | 13 | 0 | 1 | 4 | 34 | 2 | 1 | 7 | 3 | 51 | 28 | 1065 | 1 | 12 | 1 |
| other | 1 | 1 | 13 | 1 | 0 | 1 | 7 | 1 | 4 | 21 | 5 | 12 | 138 | 45 | 4 | 42 | 0 |

## Kind of eye taken from the top species, with the prior

Accuracy 81.9% (80.7 to 83.1).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | other |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 4 | 1 | 2 |
| dog | 0 | 1 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| squirrel | 0 | 0 | 24 | 0 | 3 | 0 | 0 | 1 | 1 | 3 | 0 | 0 | 1 | 1 | 2 |
| deer | 0 | 0 | 0 | 21 | 1 | 0 | 1 | 2 | 1 | 0 | 0 | 0 | 2 | 5 | 3 |
| rabbit | 0 | 0 | 0 | 0 | 29 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| hawk | 0 | 0 | 0 | 0 | 0 | 64 | 2 | 8 | 0 | 1 | 1 | 0 | 1 | 5 | 0 |
| wader | 0 | 0 | 2 | 3 | 2 | 5 | 317 | 31 | 5 | 4 | 0 | 0 | 3 | 9 | 1 |
| bird | 0 | 0 | 3 | 0 | 3 | 26 | 44 | 395 | 7 | 12 | 0 | 0 | 21 | 15 | 5 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 98 | 3 | 2 | 0 | 2 | 1 | 1 |
| reptile | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 1 | 10 | 224 | 6 | 0 | 15 | 7 | 2 |
| frog | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 17 | 68 | 0 | 7 | 1 | 3 |
| bee | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 3 | 0 | 91 | 15 | 13 | 3 |
| insect | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 2 | 1 | 83 | 8 | 31 | 755 | 40 | 39 |
| plant | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 5 | 3 | 24 | 1 | 3 | 31 | 1144 | 10 |
| other | 1 | 0 | 3 | 0 | 0 | 1 | 2 | 0 | 1 | 17 | 2 | 5 | 39 | 21 | 204 |

## Commonest mistakes

Of 2825 wrong answers for species that are in the list, 136 named another species of the same genus and 492 another species of the same family. 36 test photos show a species that is not in the list.

| Photos | The species | What was said | Observations |
|---:|---|---|---|
| 12 | *Anolis carolinensis* (Green Anole) | *Anolis sagrei* (Brown Anole) | [271728086](https://www.inaturalist.org/observations/271728086) [275047138](https://www.inaturalist.org/observations/275047138) [283243854](https://www.inaturalist.org/observations/283243854) |
| 10 | *Dryophytes cinereus* (Green Treefrog) | *Osteopilus septentrionalis* (Cuban Tree Frog) | [284722708](https://www.inaturalist.org/observations/284722708) [291386145](https://www.inaturalist.org/observations/291386145) [296111604](https://www.inaturalist.org/observations/296111604) |
| 8 | *Egretta thula* (Snowy Egret) | *Ardea alba* (Great Egret) | [257540383](https://www.inaturalist.org/observations/257540383) [278980010](https://www.inaturalist.org/observations/278980010) [267604475](https://www.inaturalist.org/observations/267604475) |
| 7 | *Osteopilus septentrionalis* (Cuban Tree Frog) | *Anaxyrus terrestris* (Southern Toad) | [278882303](https://www.inaturalist.org/observations/278882303) [295096538](https://www.inaturalist.org/observations/295096538) [302363269](https://www.inaturalist.org/observations/302363269) |
| 7 | *Dryophytes squirellus* (Squirrel Tree Frog) | *Dryophytes cinereus* (Green Treefrog) | [277900760](https://www.inaturalist.org/observations/277900760) [287282858](https://www.inaturalist.org/observations/287282858) [311678028](https://www.inaturalist.org/observations/311678028) |
| 7 | *Strix varia* (Barred Owl) | *Buteo lineatus* (Red-shouldered Hawk) | [258313350](https://www.inaturalist.org/observations/258313350) [260464161](https://www.inaturalist.org/observations/260464161) [261487976](https://www.inaturalist.org/observations/261487976) |
| 7 | *Meleagris gallopavo* (Wild Turkey) | *Aramus guarauna* (Limpkin) | [262474906](https://www.inaturalist.org/observations/262474906) [304161618](https://www.inaturalist.org/observations/304161618) [339479873](https://www.inaturalist.org/observations/339479873) |
| 6 | *Ardea alba* (Great Egret) | *Eudocimus albus* (White Ibis) | [260943580](https://www.inaturalist.org/observations/260943580) [270078942](https://www.inaturalist.org/observations/270078942) [311113087](https://www.inaturalist.org/observations/311113087) |
| 6 | *Tillandsia usneoides* (Spanish moss) | *Anolis sagrei* (Brown Anole) | [300178257](https://www.inaturalist.org/observations/300178257) [302906282](https://www.inaturalist.org/observations/302906282) [306076008](https://www.inaturalist.org/observations/306076008) |
| 6 | *Grus canadensis* (Sandhill Crane) | *Eudocimus albus* (White Ibis) | [326935378](https://www.inaturalist.org/observations/326935378) [327290307](https://www.inaturalist.org/observations/327290307) [331586594](https://www.inaturalist.org/observations/331586594) |
| 6 | *Egretta tricolor* (Tricolored Heron) | *Ardea herodias* (Great Blue Heron) | [257406135](https://www.inaturalist.org/observations/257406135) [260943635](https://www.inaturalist.org/observations/260943635) [265466677](https://www.inaturalist.org/observations/265466677) |
| 6 | *Tradescantia ohiensis* (Ohio spiderwort) | *Tradescantia fluminensis* (Rio Spiderwort) | [270636391](https://www.inaturalist.org/observations/270636391) [341794464](https://www.inaturalist.org/observations/341794464) [342937048](https://www.inaturalist.org/observations/342937048) |
| 6 | *Baeolophus bicolor* (Tufted Titmouse) | *Mimus polyglottos* (Northern Mockingbird) | [384750346](https://www.inaturalist.org/observations/384750346) [399976904](https://www.inaturalist.org/observations/399976904) [399347800](https://www.inaturalist.org/observations/399347800) |
| 6 | *Eumaeus atala* (Atala) | *Battus philenor* (Pipevine Swallowtail) | [320831159](https://www.inaturalist.org/observations/320831159) [342498738](https://www.inaturalist.org/observations/342498738) [388905762](https://www.inaturalist.org/observations/388905762) |
| 5 | *Gallinula chloropus* (Eurasian Moorhen) | *Porphyrio martinica* (Purple Gallinule) | [275925411](https://www.inaturalist.org/observations/275925411) [295561466](https://www.inaturalist.org/observations/295561466) [317614767](https://www.inaturalist.org/observations/317614767) |
