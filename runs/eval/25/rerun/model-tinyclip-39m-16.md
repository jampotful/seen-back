# tinyclip-39m-16 on the test split

_This file is written by `tools/eval/report.py` from `docs/eval/study1.json`. Rerun the script to change it._

Species rows made from the English name; settings chosen on `val`: {"min_n": 1, "lam": 0.0, "c": 0.1, "ratio": 0.016, "t_species": 70, "alpha_prior": 1.12, "species_in_list": 5911, "combinations_tried": 108}. Top-1 21.7% (20.5 to 22.9) without the prior and 35.3% (33.8 to 36.7) with it.

## By kind of eye

| Kind | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| cat | 11 | 18.2% (0.0 to 45.5) | 54.5% (27.3 to 81.8) | 0.0% |
| dog | 6 | 33.3% (0.0 to 83.3) | 50.0% (16.7 to 83.3) | 33.3% |
| squirrel | 36 | 63.9% (47.2 to 80.6) | 75.0% (61.1 to 88.9) | 33.3% |
| deer | 36 | 61.1% (44.4 to 77.8) | 75.0% (61.1 to 88.9) | 19.4% |
| rabbit | 31 | 93.5% (83.9 to 100.0) | 100.0% (100.0 to 100.0) | 61.3% |
| hawk | 82 | 56.1% (45.1 to 67.1) | 79.3% (69.5 to 87.8) | 46.3% |
| wader | 382 | 67.3% (62.8 to 72.0) | 90.0% (86.9 to 92.9) | 63.6% |
| bird | 531 | 48.6% (44.4 to 52.7) | 73.3% (69.3 to 76.8) | 37.9% |
| alligator | 110 | 90.9% (85.5 to 96.4) | 93.6% (88.2 to 98.2) | 76.4% |
| reptile | 268 | 47.0% (41.0 to 53.0) | 72.4% (67.2 to 77.2) | 23.1% |
| frog | 97 | 28.9% (20.6 to 38.1) | 71.1% (61.9 to 80.4) | 16.5% |
| bee | 126 | 23.0% (15.9 to 30.2) | 48.4% (40.5 to 57.1) | 4.8% |
| insect | 962 | 20.3% (17.9 to 22.8) | 39.8% (36.8 to 42.9) | 9.9% |
| plant | 1223 | 24.4% (22.1 to 26.9) | 40.9% (38.2 to 43.6) | 8.5% |
| other | 296 | 21.6% (16.9 to 26.7) | 37.5% (32.1 to 43.2) | 7.1% |

## By class

| Kingdom / class | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| Animalia / Insecta | 1088 | 20.6% (18.1 to 23.0) | 40.8% (38.0 to 43.8) | 9.3% |
| Animalia / Aves | 995 | 56.4% (53.5 to 59.4) | 80.2% (77.6 to 82.7) | 48.4% |
| Plantae / Magnoliopsida | 878 | 19.0% (16.5 to 21.8) | 35.9% (32.7 to 39.2) | 8.0% |
| Plantae / Liliopsida | 291 | 39.2% (33.7 to 44.7) | 53.6% (47.8 to 59.1) | 10.3% |
| Animalia / Squamata | 209 | 47.4% (40.7 to 54.1) | 70.3% (64.1 to 76.6) | 22.5% |
| Animalia / Arachnida | 154 | 24.0% (16.9 to 31.2) | 42.2% (34.4 to 50.6) | 7.1% |
| Animalia / Mammalia | 139 | 59.0% (51.1 to 66.9) | 72.7% (65.5 to 80.6) | 30.9% |
| Animalia / Crocodylia | 110 | 90.9% (85.5 to 96.4) | 93.6% (88.2 to 98.2) | 76.4% |
| Animalia / Amphibia | 101 | 27.7% (19.8 to 36.6) | 70.3% (61.4 to 79.2) | 17.8% |
| Animalia / Testudines | 59 | 45.8% (32.2 to 57.6) | 79.7% (67.8 to 89.8) | 25.4% |
| Fungi / Agaricomycetes | 39 | 17.9% (7.7 to 30.8) | 25.6% (12.8 to 41.0) | 2.6% |
| Plantae / Polypodiopsida | 38 | 26.3% (13.2 to 39.5) | 44.7% (28.9 to 60.5) | 2.6% |
| all other classes | 96 | 25.0% (16.7 to 33.3) | 40.6% (31.2 to 50.0) | 7.3% |

## By how often the species was recorded before 2025

| Records before 2025 | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| not in the list | 36 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 0.0% |
| 1 or 2 records | 58 | 0.0% (0.0 to 0.0) | 3.5% (0.0 to 8.6) | 8.6% |
| 3 to 9 | 138 | 0.0% (0.0 to 0.0) | 6.5% (2.9 to 10.9) | 8.0% |
| 10 to 49 | 468 | 6.4% (4.3 to 8.8) | 16.4% (13.2 to 19.9) | 7.5% |
| 50 to 199 | 1195 | 18.9% (16.9 to 21.2) | 42.3% (39.6 to 44.9) | 11.9% |
| 200 or more | 2302 | 53.2% (51.2 to 55.2) | 74.7% (72.9 to 76.5) | 31.1% |

## By calendar month

| Month | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| 01 | 208 | 38.9% (32.2 to 45.7) | 61.5% (54.8 to 67.8) | 27.9% |
| 02 | 251 | 41.4% (35.9 to 47.0) | 62.5% (56.2 to 68.5) | 25.5% |
| 03 | 458 | 34.1% (29.9 to 38.4) | 55.0% (50.4 to 59.6) | 21.0% |
| 04 | 755 | 34.4% (31.0 to 37.9) | 52.8% (49.1 to 56.4) | 21.1% |
| 05 | 383 | 32.4% (27.7 to 37.1) | 51.4% (46.5 to 56.4) | 23.0% |
| 06 | 317 | 30.3% (25.6 to 35.6) | 52.0% (46.7 to 57.4) | 18.9% |
| 07 | 384 | 32.0% (27.3 to 36.7) | 52.3% (47.4 to 57.3) | 20.6% |
| 08 | 368 | 39.7% (34.8 to 44.8) | 55.4% (50.3 to 60.6) | 19.8% |
| 09 | 454 | 34.1% (30.0 to 38.3) | 55.7% (51.1 to 60.1) | 18.3% |
| 10 | 227 | 33.5% (27.3 to 39.6) | 52.9% (46.7 to 59.0) | 18.9% |
| 11 | 258 | 39.1% (33.7 to 45.0) | 58.5% (52.7 to 64.3) | 22.9% |
| 12 | 134 | 43.3% (35.1 to 52.2) | 64.2% (56.0 to 72.4) | 35.8% |

## Kind of eye from the kind phrases: what was said (columns) for each true kind (rows)

Accuracy 77.6% (76.3 to 78.8). Photos called `person`: 0.05%; called `none`: 0.10% (the test split holds neither).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | person | other | none |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| dog | 0 | 4 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| squirrel | 0 | 0 | 33 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 |
| deer | 0 | 0 | 0 | 27 | 0 | 1 | 2 | 0 | 0 | 1 | 1 | 0 | 0 | 2 | 0 | 2 | 0 |
| rabbit | 0 | 0 | 3 | 0 | 28 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| hawk | 0 | 0 | 0 | 0 | 0 | 73 | 5 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| wader | 0 | 0 | 3 | 0 | 0 | 7 | 342 | 17 | 8 | 1 | 0 | 0 | 0 | 4 | 0 | 0 | 0 |
| bird | 3 | 0 | 20 | 2 | 1 | 65 | 107 | 283 | 17 | 10 | 1 | 1 | 9 | 9 | 0 | 2 | 1 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 105 | 1 | 0 | 0 | 0 | 2 | 0 | 2 | 0 |
| reptile | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 37 | 188 | 7 | 0 | 16 | 7 | 0 | 9 | 2 |
| frog | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 5 | 83 | 0 | 6 | 0 | 0 | 0 | 0 |
| bee | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 101 | 18 | 4 | 0 | 1 | 0 |
| insect | 0 | 0 | 2 | 0 | 0 | 3 | 0 | 4 | 1 | 15 | 18 | 60 | 825 | 18 | 0 | 16 | 0 |
| plant | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 3 | 3 | 6 | 39 | 50 | 1115 | 1 | 2 | 1 |
| other | 0 | 1 | 6 | 3 | 0 | 1 | 0 | 2 | 5 | 15 | 11 | 13 | 156 | 41 | 1 | 41 | 0 |

## Kind of eye taken from the top species, with the prior

Accuracy 84.2% (83.1 to 85.4).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | other |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 4 | 2 | 1 |
| dog | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 |
| squirrel | 0 | 0 | 24 | 0 | 4 | 0 | 3 | 1 | 0 | 2 | 0 | 0 | 2 | 0 | 0 |
| deer | 0 | 0 | 0 | 22 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 5 | 6 | 0 |
| rabbit | 0 | 0 | 0 | 0 | 29 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| hawk | 0 | 0 | 1 | 0 | 0 | 63 | 6 | 5 | 0 | 0 | 0 | 0 | 0 | 7 | 0 |
| wader | 0 | 0 | 1 | 0 | 0 | 4 | 339 | 22 | 1 | 2 | 0 | 0 | 5 | 8 | 0 |
| bird | 0 | 0 | 1 | 0 | 1 | 15 | 35 | 412 | 6 | 16 | 0 | 0 | 21 | 22 | 2 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 100 | 2 | 0 | 0 | 1 | 6 | 1 |
| reptile | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 9 | 225 | 2 | 0 | 10 | 18 | 2 |
| frog | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 19 | 71 | 0 | 2 | 2 | 1 |
| bee | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 3 | 1 | 73 | 27 | 21 | 0 |
| insect | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 2 | 47 | 5 | 16 | 805 | 57 | 27 |
| plant | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 6 | 1 | 0 | 33 | 1170 | 11 |
| other | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 19 | 4 | 1 | 45 | 26 | 197 |

## Commonest mistakes

Of 2681 wrong answers for species that are in the list, 125 named another species of the same genus and 516 another species of the same family. 36 test photos show a species that is not in the list.

| Photos | The species | What was said | Observations |
|---:|---|---|---|
| 13 | *Anolis carolinensis* (Green Anole) | *Anolis sagrei* (Brown Anole) | [264044135](https://www.inaturalist.org/observations/264044135) [267634318](https://www.inaturalist.org/observations/267634318) [275047138](https://www.inaturalist.org/observations/275047138) |
| 8 | *Tillandsia usneoides* (Spanish moss) | *Paederia foetida* (skunk vine) | [300178257](https://www.inaturalist.org/observations/300178257) [300745077](https://www.inaturalist.org/observations/300745077) [302906275](https://www.inaturalist.org/observations/302906275) |
| 8 | *Dichondra carolinensis* (Carolina ponysfoot) | *Oxalis corniculata* (Creeping Woodsorrel) | [261770440](https://www.inaturalist.org/observations/261770440) [268990814](https://www.inaturalist.org/observations/268990814) [284953334](https://www.inaturalist.org/observations/284953334) |
| 7 | *Liquidambar styraciflua* (American sweetgum) | *Cnidoscolus stimulosus* (spurge nettle) | [264029450](https://www.inaturalist.org/observations/264029450) [270192735](https://www.inaturalist.org/observations/270192735) [270791806](https://www.inaturalist.org/observations/270791806) |
| 7 | *Parthenocissus quinquefolia* (Virginia creeper) | *Toxicodendron radicans* (eastern poison ivy) | [327404110](https://www.inaturalist.org/observations/327404110) [316899809](https://www.inaturalist.org/observations/316899809) [318659550](https://www.inaturalist.org/observations/318659550) |
| 7 | *Orgyia detrita* (Live Oak Tussock Moth) | *Malacosoma disstria* (Forest Tent Caterpillar Moth) | [300979138](https://www.inaturalist.org/observations/300979138) [344548457](https://www.inaturalist.org/observations/344548457) [344790830](https://www.inaturalist.org/observations/344790830) |
| 7 | *Dryophytes squirellus* (Squirrel Tree Frog) | *Osteopilus septentrionalis* (Cuban Tree Frog) | [273882305](https://www.inaturalist.org/observations/273882305) [294496288](https://www.inaturalist.org/observations/294496288) [294496266](https://www.inaturalist.org/observations/294496266) |
| 6 | *Callicarpa americana* (American beautyberry) | *Cnidoscolus stimulosus* (spurge nettle) | [273173349](https://www.inaturalist.org/observations/273173349) [275149528](https://www.inaturalist.org/observations/275149528) [280890740](https://www.inaturalist.org/observations/280890740) |
| 6 | *Coluber constrictor* (North American Racer) | *Nerodia fasciata* (Banded Watersnake) | [265087903](https://www.inaturalist.org/observations/265087903) [312508530](https://www.inaturalist.org/observations/312508530) [322680413](https://www.inaturalist.org/observations/322680413) |
| 5 | *Dryophytes cinereus* (Green Treefrog) | *Osteopilus septentrionalis* (Cuban Tree Frog) | [291386145](https://www.inaturalist.org/observations/291386145) [296111604](https://www.inaturalist.org/observations/296111604) [301385352](https://www.inaturalist.org/observations/301385352) |
| 5 | *Parthenocissus quinquefolia* (Virginia creeper) | *Cnidoscolus stimulosus* (spurge nettle) | [273175823](https://www.inaturalist.org/observations/273175823) [348422030](https://www.inaturalist.org/observations/348422030) [352810660](https://www.inaturalist.org/observations/352810660) |
| 5 | *Sabal palmetto* (cabbage palmetto) | *Serenoa repens* (saw palmetto) | [260738332](https://www.inaturalist.org/observations/260738332) [261485232](https://www.inaturalist.org/observations/261485232) [362225812](https://www.inaturalist.org/observations/362225812) |
| 5 | *Phalacrocorax auritus* (Double-crested Cormorant) | *Anhinga anhinga* (Anhinga) | [289662493](https://www.inaturalist.org/observations/289662493) [302885778](https://www.inaturalist.org/observations/302885778) [321884842](https://www.inaturalist.org/observations/321884842) |
| 5 | *Apalone ferox* (Florida Softshell Turtle) | *Alligator mississippiensis* (American Alligator) | [265904896](https://www.inaturalist.org/observations/265904896) [322986936](https://www.inaturalist.org/observations/322986936) [327014977](https://www.inaturalist.org/observations/327014977) |
| 5 | *Dryophytes squirellus* (Squirrel Tree Frog) | *Dryophytes cinereus* (Green Treefrog) | [277900760](https://www.inaturalist.org/observations/277900760) [287282858](https://www.inaturalist.org/observations/287282858) [344907264](https://www.inaturalist.org/observations/344907264) |
