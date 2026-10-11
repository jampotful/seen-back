# tinyclip-39m-16 on the test split

_This file is written by `tools/eval/report.py` from `docs/eval/study1.json`. Rerun the script to change it._

Species rows made from the English name; settings chosen on `val`: {"min_n": 1, "lam": 0.0, "c": 0.1, "ratio": 0.016, "t_species": 70, "alpha_prior": 1.12, "species_in_list": 5911, "combinations_tried": 108}. Top-1 20.9% (19.8 to 22.2) without the prior and 35.0% (33.6 to 36.4) with it.

## By kind of eye

| Kind | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| cat | 11 | 18.2% (0.0 to 45.5) | 45.5% (18.2 to 72.7) | 0.0% |
| dog | 6 | 33.3% (0.0 to 83.3) | 50.0% (16.7 to 83.3) | 33.3% |
| squirrel | 36 | 63.9% (47.2 to 80.6) | 75.0% (61.1 to 88.9) | 27.8% |
| deer | 36 | 58.3% (41.7 to 75.0) | 75.0% (61.1 to 88.9) | 16.7% |
| rabbit | 31 | 93.5% (83.9 to 100.0) | 100.0% (100.0 to 100.0) | 61.3% |
| hawk | 82 | 56.1% (45.1 to 67.1) | 79.3% (69.5 to 87.8) | 45.1% |
| wader | 382 | 66.5% (62.0 to 71.2) | 88.2% (84.8 to 91.1) | 62.0% |
| bird | 531 | 47.8% (43.7 to 52.0) | 72.5% (68.5 to 76.1) | 35.6% |
| alligator | 110 | 90.9% (85.5 to 96.4) | 93.6% (88.2 to 98.2) | 74.6% |
| reptile | 268 | 48.1% (42.2 to 54.1) | 73.5% (68.3 to 78.7) | 23.1% |
| frog | 97 | 28.9% (19.6 to 38.1) | 70.1% (60.8 to 79.4) | 19.6% |
| bee | 126 | 26.2% (19.1 to 34.1) | 51.6% (42.9 to 60.3) | 9.5% |
| insect | 962 | 19.9% (17.4 to 22.4) | 39.4% (36.5 to 42.5) | 9.7% |
| plant | 1223 | 24.2% (21.8 to 26.7) | 38.9% (36.2 to 41.7) | 7.9% |
| other | 296 | 20.3% (15.9 to 25.0) | 35.1% (29.7 to 40.5) | 4.7% |

## By class

| Kingdom / class | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| Animalia / Insecta | 1088 | 20.6% (18.1 to 23.1) | 40.8% (38.0 to 43.8) | 9.7% |
| Animalia / Aves | 995 | 55.7% (52.7 to 58.7) | 79.1% (76.5 to 81.5) | 46.5% |
| Plantae / Magnoliopsida | 878 | 18.7% (16.2 to 21.4) | 34.1% (31.1 to 37.2) | 7.3% |
| Plantae / Liliopsida | 291 | 38.8% (33.3 to 44.3) | 50.5% (44.7 to 56.0) | 10.0% |
| Animalia / Squamata | 209 | 48.8% (42.1 to 55.5) | 73.2% (67.5 to 79.0) | 22.0% |
| Animalia / Arachnida | 154 | 22.7% (16.2 to 29.9) | 37.0% (29.9 to 44.8) | 3.2% |
| Animalia / Mammalia | 139 | 58.3% (49.6 to 66.2) | 71.9% (64.8 to 79.9) | 28.1% |
| Animalia / Crocodylia | 110 | 90.9% (85.5 to 96.4) | 93.6% (88.2 to 98.2) | 74.6% |
| Animalia / Amphibia | 101 | 27.7% (19.8 to 36.6) | 69.3% (60.4 to 78.2) | 20.8% |
| Animalia / Testudines | 59 | 45.8% (32.2 to 57.6) | 74.6% (62.7 to 84.8) | 27.1% |
| Fungi / Agaricomycetes | 39 | 17.9% (7.7 to 30.8) | 28.2% (15.4 to 43.6) | 2.6% |
| Plantae / Polypodiopsida | 38 | 28.9% (15.8 to 44.7) | 47.4% (31.6 to 63.2) | 2.6% |
| all other classes | 96 | 22.9% (14.6 to 31.2) | 40.6% (31.2 to 50.0) | 7.3% |

## By how often the species was recorded before 2025

| Records before 2025 | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| not in the list | 36 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 0.0% |
| 1 or 2 records | 58 | 0.0% (0.0 to 0.0) | 3.5% (0.0 to 8.6) | 6.9% |
| 3 to 9 | 138 | 0.0% (0.0 to 0.0) | 7.2% (2.9 to 11.6) | 7.2% |
| 10 to 49 | 468 | 6.0% (3.9 to 8.3) | 16.0% (12.8 to 19.4) | 8.1% |
| 50 to 199 | 1195 | 18.9% (16.8 to 21.2) | 42.3% (39.6 to 45.1) | 11.6% |
| 200 or more | 2302 | 52.7% (50.8 to 54.8) | 72.9% (71.1 to 74.8) | 29.9% |

## By calendar month

| Month | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| 01 | 208 | 38.5% (31.2 to 45.2) | 61.5% (54.3 to 68.3) | 26.9% |
| 02 | 251 | 40.6% (35.1 to 46.2) | 62.2% (55.8 to 68.1) | 22.7% |
| 03 | 458 | 34.1% (29.9 to 38.4) | 53.5% (49.1 to 57.9) | 20.5% |
| 04 | 755 | 33.8% (30.3 to 37.4) | 51.1% (47.4 to 54.7) | 20.7% |
| 05 | 383 | 33.2% (28.5 to 38.1) | 51.2% (46.2 to 56.4) | 22.2% |
| 06 | 317 | 29.0% (24.3 to 34.1) | 50.8% (45.4 to 56.5) | 17.7% |
| 07 | 384 | 31.2% (26.6 to 35.9) | 50.3% (45.6 to 55.2) | 18.8% |
| 08 | 368 | 39.7% (34.8 to 44.6) | 55.2% (50.0 to 60.3) | 19.6% |
| 09 | 454 | 34.4% (30.2 to 38.8) | 56.4% (51.5 to 61.0) | 18.1% |
| 10 | 227 | 33.0% (26.9 to 39.2) | 49.3% (43.2 to 55.5) | 17.2% |
| 11 | 258 | 39.1% (33.3 to 45.0) | 58.5% (52.7 to 64.3) | 23.6% |
| 12 | 134 | 43.3% (35.1 to 51.5) | 63.4% (55.2 to 71.6) | 36.6% |

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

Accuracy 84.1% (82.9 to 85.2).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | other |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 3 | 2 | 0 |
| dog | 0 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| squirrel | 0 | 0 | 24 | 0 | 4 | 0 | 3 | 1 | 0 | 2 | 0 | 0 | 2 | 0 | 0 |
| deer | 0 | 0 | 0 | 21 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 5 | 7 | 0 |
| rabbit | 0 | 0 | 0 | 0 | 29 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| hawk | 0 | 0 | 1 | 0 | 0 | 63 | 6 | 5 | 0 | 0 | 0 | 0 | 0 | 7 | 0 |
| wader | 0 | 0 | 1 | 0 | 0 | 4 | 338 | 22 | 1 | 2 | 0 | 0 | 5 | 9 | 0 |
| bird | 0 | 0 | 1 | 0 | 1 | 15 | 32 | 413 | 6 | 17 | 0 | 0 | 22 | 22 | 2 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 100 | 2 | 0 | 0 | 1 | 4 | 3 |
| reptile | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 9 | 227 | 2 | 0 | 10 | 16 | 2 |
| frog | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 17 | 72 | 0 | 3 | 2 | 1 |
| bee | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 3 | 1 | 72 | 28 | 21 | 0 |
| insect | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 2 | 49 | 6 | 18 | 806 | 50 | 28 |
| plant | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 8 | 1 | 0 | 36 | 1165 | 11 |
| other | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 1 | 0 | 22 | 4 | 1 | 49 | 19 | 196 |

## Commonest mistakes

Of 2693 wrong answers for species that are in the list, 133 named another species of the same genus and 525 another species of the same family. 36 test photos show a species that is not in the list.

| Photos | The species | What was said | Observations |
|---:|---|---|---|
| 14 | *Anolis carolinensis* (Green Anole) | *Anolis sagrei* (Brown Anole) | [264044135](https://www.inaturalist.org/observations/264044135) [267634318](https://www.inaturalist.org/observations/267634318) [275047138](https://www.inaturalist.org/observations/275047138) |
| 9 | *Tillandsia usneoides* (Spanish moss) | *Paederia foetida* (skunk vine) | [300178257](https://www.inaturalist.org/observations/300178257) [300745029](https://www.inaturalist.org/observations/300745029) [300745077](https://www.inaturalist.org/observations/300745077) |
| 9 | *Dichondra carolinensis* (Carolina ponysfoot) | *Oxalis corniculata* (Creeping Woodsorrel) | [261770440](https://www.inaturalist.org/observations/261770440) [263685070](https://www.inaturalist.org/observations/263685070) [268990814](https://www.inaturalist.org/observations/268990814) |
| 8 | *Dryophytes squirellus* (Squirrel Tree Frog) | *Osteopilus septentrionalis* (Cuban Tree Frog) | [273882305](https://www.inaturalist.org/observations/273882305) [287189527](https://www.inaturalist.org/observations/287189527) [294496288](https://www.inaturalist.org/observations/294496288) |
| 7 | *Liquidambar styraciflua* (American sweetgum) | *Cnidoscolus stimulosus* (spurge nettle) | [264029450](https://www.inaturalist.org/observations/264029450) [270192735](https://www.inaturalist.org/observations/270192735) [270791806](https://www.inaturalist.org/observations/270791806) |
| 7 | *Orgyia detrita* (Live Oak Tussock Moth) | *Malacosoma disstria* (Forest Tent Caterpillar Moth) | [300979138](https://www.inaturalist.org/observations/300979138) [344548457](https://www.inaturalist.org/observations/344548457) [344790830](https://www.inaturalist.org/observations/344790830) |
| 7 | *Meleagris gallopavo* (Wild Turkey) | *Aramus guarauna* (Limpkin) | [304161618](https://www.inaturalist.org/observations/304161618) [329151107](https://www.inaturalist.org/observations/329151107) [339479873](https://www.inaturalist.org/observations/339479873) |
| 7 | *Menemerus bivittatus* (Gray Wall Jumping Spider) | *Anasaitis canosa* (Twin-flagged Jumping Spider) | [277793437](https://www.inaturalist.org/observations/277793437) [280594082](https://www.inaturalist.org/observations/280594082) [311555865](https://www.inaturalist.org/observations/311555865) |
| 6 | *Callicarpa americana* (American beautyberry) | *Cnidoscolus stimulosus* (spurge nettle) | [273173349](https://www.inaturalist.org/observations/273173349) [275149528](https://www.inaturalist.org/observations/275149528) [280890740](https://www.inaturalist.org/observations/280890740) |
| 6 | *Dryophytes cinereus* (Green Treefrog) | *Osteopilus septentrionalis* (Cuban Tree Frog) | [291386145](https://www.inaturalist.org/observations/291386145) [296111604](https://www.inaturalist.org/observations/296111604) [301385352](https://www.inaturalist.org/observations/301385352) |
| 6 | *Parthenocissus quinquefolia* (Virginia creeper) | *Cnidoscolus stimulosus* (spurge nettle) | [273175823](https://www.inaturalist.org/observations/273175823) [348422030](https://www.inaturalist.org/observations/348422030) [352810660](https://www.inaturalist.org/observations/352810660) |
| 6 | *Coluber constrictor* (North American Racer) | *Nerodia fasciata* (Banded Watersnake) | [265087903](https://www.inaturalist.org/observations/265087903) [312508530](https://www.inaturalist.org/observations/312508530) [322680413](https://www.inaturalist.org/observations/322680413) |
| 5 | *Bidens alba* (White beggarticks) | *Cnidoscolus stimulosus* (spurge nettle) | [266934008](https://www.inaturalist.org/observations/266934008) [316746691](https://www.inaturalist.org/observations/316746691) [353205775](https://www.inaturalist.org/observations/353205775) |
| 5 | *Bidens alba* (White beggarticks) | *Ludwigia peruviana* (Peruvian primrose-willow) | [318519961](https://www.inaturalist.org/observations/318519961) [321303703](https://www.inaturalist.org/observations/321303703) [322612877](https://www.inaturalist.org/observations/322612877) |
| 5 | *Phalacrocorax auritus* (Double-crested Cormorant) | *Anhinga anhinga* (Anhinga) | [289662493](https://www.inaturalist.org/observations/289662493) [302885778](https://www.inaturalist.org/observations/302885778) [321884842](https://www.inaturalist.org/observations/321884842) |
