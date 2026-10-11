# tinyclip-40m-32 on the test split

_This file is written by `tools/eval/report.py` from `docs/eval/study1.json`. Rerun the script to change it._

Species rows made from the English name; settings chosen on `val`: {"min_n": 1, "lam": 0.0, "c": 0.1, "ratio": 0.016, "t_species": 50, "alpha_prior": 0.8, "species_in_list": 5911, "combinations_tried": 108}. Top-1 15.1% (14.1 to 16.2) without the prior and 26.7% (25.4 to 28.1) with it.

## By kind of eye

| Kind | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| cat | 11 | 27.3% (0.0 to 54.5) | 45.5% (18.2 to 72.7) | 9.1% |
| dog | 6 | 16.7% (0.0 to 50.0) | 16.7% (0.0 to 50.0) | 16.7% |
| squirrel | 36 | 47.2% (30.6 to 63.9) | 66.7% (50.0 to 83.3) | 36.1% |
| deer | 36 | 47.2% (30.6 to 61.1) | 63.9% (47.2 to 77.8) | 13.9% |
| rabbit | 31 | 80.6% (64.5 to 93.5) | 93.5% (83.9 to 100.0) | 54.8% |
| hawk | 82 | 50.0% (39.0 to 59.8) | 67.1% (57.3 to 78.0) | 35.4% |
| wader | 382 | 53.4% (48.7 to 58.6) | 81.4% (77.5 to 85.1) | 48.2% |
| bird | 531 | 34.3% (30.3 to 38.2) | 58.4% (54.0 to 62.5) | 23.2% |
| alligator | 110 | 80.9% (73.6 to 88.2) | 90.9% (84.5 to 96.4) | 50.9% |
| reptile | 268 | 34.3% (28.4 to 39.9) | 58.2% (52.6 to 64.2) | 10.1% |
| frog | 97 | 20.6% (13.4 to 28.9) | 52.6% (42.3 to 61.9) | 11.3% |
| bee | 126 | 15.9% (9.5 to 22.2) | 37.3% (29.4 to 46.0) | 2.4% |
| insect | 962 | 14.4% (12.3 to 16.7) | 29.0% (26.3 to 32.0) | 7.2% |
| plant | 1223 | 18.8% (16.7 to 21.0) | 32.2% (29.6 to 35.0) | 7.0% |
| other | 296 | 13.5% (9.8 to 17.2) | 29.1% (24.0 to 34.1) | 3.0% |

## By class

| Kingdom / class | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| Animalia / Insecta | 1088 | 14.6% (12.5 to 16.8) | 30.0% (27.3 to 32.6) | 6.6% |
| Animalia / Aves | 995 | 42.9% (40.0 to 46.0) | 67.9% (65.1 to 70.7) | 33.8% |
| Plantae / Magnoliopsida | 878 | 13.0% (10.8 to 15.3) | 26.5% (23.7 to 29.5) | 4.1% |
| Plantae / Liliopsida | 291 | 36.4% (30.9 to 41.6) | 48.5% (42.6 to 53.9) | 16.5% |
| Animalia / Squamata | 209 | 34.9% (28.2 to 41.6) | 58.9% (52.1 to 65.5) | 7.2% |
| Animalia / Arachnida | 154 | 13.0% (7.8 to 18.2) | 30.5% (22.7 to 37.7) | 1.9% |
| Animalia / Mammalia | 139 | 48.2% (40.3 to 56.8) | 64.0% (56.1 to 71.9) | 29.5% |
| Animalia / Crocodylia | 110 | 80.9% (73.6 to 88.2) | 90.9% (84.5 to 96.4) | 50.9% |
| Animalia / Amphibia | 101 | 19.8% (12.9 to 27.7) | 50.5% (40.6 to 60.4) | 10.9% |
| Animalia / Testudines | 59 | 32.2% (20.3 to 44.1) | 55.9% (44.1 to 67.8) | 20.3% |
| Fungi / Agaricomycetes | 39 | 12.8% (2.6 to 23.1) | 20.5% (10.3 to 33.3) | 0.0% |
| Plantae / Polypodiopsida | 38 | 15.8% (5.3 to 28.9) | 31.6% (18.4 to 47.4) | 2.6% |
| all other classes | 96 | 15.6% (9.4 to 22.9) | 33.3% (24.0 to 42.7) | 3.1% |

## By how often the species was recorded before 2025

| Records before 2025 | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| not in the list | 36 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 0.0% |
| 1 or 2 records | 58 | 0.0% (0.0 to 0.0) | 1.7% (0.0 to 5.2) | 3.5% |
| 3 to 9 | 138 | 0.0% (0.0 to 0.0) | 1.4% (0.0 to 3.6) | 2.2% |
| 10 to 49 | 468 | 4.1% (2.4 to 6.0) | 10.0% (7.5 to 12.8) | 4.9% |
| 50 to 199 | 1195 | 12.6% (10.7 to 14.6) | 30.9% (28.4 to 33.6) | 7.6% |
| 200 or more | 2302 | 41.3% (39.3 to 43.3) | 63.1% (61.0 to 65.0) | 22.4% |

## By calendar month

| Month | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| 01 | 208 | 29.8% (24.0 to 36.1) | 45.7% (38.5 to 52.4) | 21.1% |
| 02 | 251 | 33.5% (27.9 to 39.4) | 49.4% (43.4 to 55.8) | 18.7% |
| 03 | 458 | 22.1% (18.3 to 25.8) | 43.0% (38.9 to 47.6) | 14.8% |
| 04 | 755 | 24.4% (21.3 to 27.4) | 42.1% (38.5 to 45.7) | 13.5% |
| 05 | 383 | 28.5% (24.0 to 32.9) | 43.9% (38.9 to 48.8) | 15.4% |
| 06 | 317 | 24.9% (20.2 to 30.0) | 40.7% (35.3 to 46.1) | 14.2% |
| 07 | 384 | 25.3% (20.8 to 29.9) | 43.0% (38.0 to 47.9) | 14.3% |
| 08 | 368 | 27.4% (23.1 to 32.1) | 44.8% (39.9 to 49.7) | 14.7% |
| 09 | 454 | 24.4% (20.7 to 28.4) | 47.6% (43.0 to 52.2) | 12.3% |
| 10 | 227 | 27.3% (21.6 to 32.6) | 40.5% (33.9 to 46.7) | 13.2% |
| 11 | 258 | 30.6% (24.8 to 36.4) | 49.6% (43.4 to 55.8) | 14.7% |
| 12 | 134 | 38.1% (29.8 to 46.3) | 55.2% (47.0 to 64.2) | 26.9% |

## Kind of eye from the kind phrases: what was said (columns) for each true kind (rows)

Accuracy 69.3% (67.9 to 70.8). Photos called `person`: 0.05%; called `none`: 0.21% (the test split holds neither).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | person | other | none |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 6 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| dog | 0 | 2 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| squirrel | 0 | 0 | 25 | 0 | 0 | 0 | 2 | 0 | 1 | 3 | 0 | 0 | 0 | 3 | 0 | 2 | 0 |
| deer | 0 | 0 | 1 | 24 | 0 | 0 | 4 | 0 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 3 | 0 |
| rabbit | 0 | 0 | 7 | 0 | 20 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| hawk | 0 | 0 | 2 | 1 | 0 | 65 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 | 0 |
| wader | 0 | 0 | 4 | 2 | 1 | 9 | 306 | 30 | 13 | 5 | 0 | 0 | 2 | 9 | 0 | 1 | 0 |
| bird | 2 | 2 | 21 | 2 | 2 | 70 | 97 | 248 | 29 | 13 | 1 | 1 | 7 | 15 | 0 | 15 | 6 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 98 | 3 | 2 | 0 | 0 | 4 | 0 | 1 | 0 |
| reptile | 0 | 0 | 7 | 0 | 0 | 0 | 2 | 7 | 34 | 161 | 1 | 0 | 16 | 14 | 0 | 25 | 1 |
| frog | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 20 | 55 | 0 | 8 | 1 | 0 | 11 | 1 |
| bee | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 3 | 1 | 91 | 20 | 4 | 0 | 4 | 0 |
| insect | 0 | 0 | 4 | 0 | 1 | 5 | 0 | 11 | 1 | 64 | 14 | 89 | 697 | 27 | 0 | 49 | 0 |
| plant | 0 | 0 | 3 | 0 | 1 | 3 | 3 | 2 | 3 | 18 | 9 | 66 | 44 | 1050 | 2 | 18 | 1 |
| other | 2 | 1 | 4 | 2 | 1 | 3 | 1 | 1 | 5 | 30 | 6 | 12 | 130 | 36 | 0 | 62 | 0 |

## Kind of eye taken from the top species, with the prior

Accuracy 75.1% (73.7 to 76.3).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | other |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 3 | 1 |
| dog | 0 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| squirrel | 0 | 0 | 18 | 0 | 1 | 0 | 2 | 1 | 2 | 5 | 1 | 0 | 1 | 4 | 1 |
| deer | 0 | 0 | 0 | 19 | 1 | 0 | 2 | 1 | 2 | 1 | 0 | 1 | 2 | 6 | 1 |
| rabbit | 0 | 0 | 0 | 0 | 25 | 1 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 1 | 1 |
| hawk | 0 | 0 | 0 | 0 | 0 | 61 | 5 | 5 | 0 | 0 | 0 | 0 | 3 | 7 | 1 |
| wader | 0 | 0 | 0 | 4 | 2 | 3 | 298 | 38 | 7 | 5 | 0 | 0 | 6 | 17 | 2 |
| bird | 0 | 0 | 3 | 0 | 1 | 21 | 38 | 362 | 18 | 21 | 3 | 0 | 19 | 42 | 3 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 4 | 89 | 4 | 2 | 0 | 0 | 7 | 3 |
| reptile | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 5 | 19 | 184 | 5 | 2 | 18 | 28 | 4 |
| frog | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 23 | 57 | 0 | 9 | 2 | 4 |
| bee | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 3 | 3 | 63 | 31 | 21 | 2 |
| insect | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 7 | 3 | 96 | 20 | 38 | 678 | 76 | 40 |
| plant | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 3 | 1 | 10 | 3 | 0 | 51 | 1135 | 17 |
| other | 1 | 0 | 2 | 1 | 0 | 0 | 2 | 1 | 3 | 33 | 8 | 7 | 51 | 30 | 157 |

## Commonest mistakes

Of 3041 wrong answers for species that are in the list, 110 named another species of the same genus and 415 another species of the same family. 36 test photos show a species that is not in the list.

| Photos | The species | What was said | Observations |
|---:|---|---|---|
| 8 | *Anolis carolinensis* (Green Anole) | *Anolis sagrei* (Brown Anole) | [264044135](https://www.inaturalist.org/observations/264044135) [275047138](https://www.inaturalist.org/observations/275047138) [307345182](https://www.inaturalist.org/observations/307345182) |
| 8 | *Trichonephila clavipes* (Golden Silk Spider) | *Leucauge argyrobapta* (Mabel Orchard Orbweaver) | [311694212](https://www.inaturalist.org/observations/311694212) [314473275](https://www.inaturalist.org/observations/314473275) [319228228](https://www.inaturalist.org/observations/319228228) |
| 6 | *Bidens alba* (White beggarticks) | *Ludwigia peruviana* (Peruvian primrose-willow) | [318519961](https://www.inaturalist.org/observations/318519961) [321303703](https://www.inaturalist.org/observations/321303703) [322612877](https://www.inaturalist.org/observations/322612877) |
| 6 | *Tillandsia usneoides* (Spanish moss) | *Ipomoea pandurata* (wild potato vine) | [298493824](https://www.inaturalist.org/observations/298493824) [300745080](https://www.inaturalist.org/observations/300745080) [302906275](https://www.inaturalist.org/observations/302906275) |
| 6 | *Egretta tricolor* (Tricolored Heron) | *Egretta caerulea* (Little Blue Heron) | [272675903](https://www.inaturalist.org/observations/272675903) [283799371](https://www.inaturalist.org/observations/283799371) [300657497](https://www.inaturalist.org/observations/300657497) |
| 6 | *Coluber constrictor* (North American Racer) | *Nerodia fasciata* (Banded Watersnake) | [265087903](https://www.inaturalist.org/observations/265087903) [322680413](https://www.inaturalist.org/observations/322680413) [341929173](https://www.inaturalist.org/observations/341929173) |
| 6 | *Orgyia detrita* (Live Oak Tussock Moth) | *Malacosoma disstria* (Forest Tent Caterpillar Moth) | [269035367](https://www.inaturalist.org/observations/269035367) [300979138](https://www.inaturalist.org/observations/300979138) [343374304](https://www.inaturalist.org/observations/343374304) |
| 5 | *Ardea herodias* (Great Blue Heron) | *Egretta caerulea* (Little Blue Heron) | [284865338](https://www.inaturalist.org/observations/284865338) [325890376](https://www.inaturalist.org/observations/325890376) [333078608](https://www.inaturalist.org/observations/333078608) |
| 5 | *Bidens alba* (White beggarticks) | *Ardisia crenata* (Coralberry) | [258043630](https://www.inaturalist.org/observations/258043630) [258058735](https://www.inaturalist.org/observations/258058735) [258502312](https://www.inaturalist.org/observations/258502312) |
| 5 | *Tillandsia usneoides* (Spanish moss) | *Platanus occidentalis* (American sycamore) | [303902412](https://www.inaturalist.org/observations/303902412) [308872548](https://www.inaturalist.org/observations/308872548) [309519601](https://www.inaturalist.org/observations/309519601) |
| 5 | *Tillandsia usneoides* (Spanish moss) | *Paederia foetida* (skunk vine) | [298493833](https://www.inaturalist.org/observations/298493833) [301064751](https://www.inaturalist.org/observations/301064751) [306076008](https://www.inaturalist.org/observations/306076008) |
| 5 | *Dryophytes cinereus* (Green Treefrog) | *Osteopilus septentrionalis* (Cuban Tree Frog) | [291386145](https://www.inaturalist.org/observations/291386145) [296111604](https://www.inaturalist.org/observations/296111604) [301385352](https://www.inaturalist.org/observations/301385352) |
| 5 | *Egretta tricolor* (Tricolored Heron) | *Ardea herodias* (Great Blue Heron) | [260943635](https://www.inaturalist.org/observations/260943635) [265466677](https://www.inaturalist.org/observations/265466677) [376538471](https://www.inaturalist.org/observations/376538471) |
| 5 | *Egretta thula* (Snowy Egret) | *Ardea alba* (Great Egret) | [257540383](https://www.inaturalist.org/observations/257540383) [278980010](https://www.inaturalist.org/observations/278980010) [313312335](https://www.inaturalist.org/observations/313312335) |
| 5 | *Dryophytes squirellus* (Squirrel Tree Frog) | *Osteopilus septentrionalis* (Cuban Tree Frog) | [273882305](https://www.inaturalist.org/observations/273882305) [277900760](https://www.inaturalist.org/observations/277900760) [294496288](https://www.inaturalist.org/observations/294496288) |
