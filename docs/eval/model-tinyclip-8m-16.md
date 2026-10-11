# tinyclip-8m-16 on the test split

_This file is written by `tools/eval/report.py` from `docs/eval/study1.json`. Rerun the script to change it._

Species rows made from the English name; settings chosen on `val`: {"min_n": 1, "lam": 0.0, "c": 0.1, "ratio": 0.012, "t_species": 70, "alpha_prior": 0.84, "species_in_list": 5911, "combinations_tried": 108}. Top-1 14.9% (13.8 to 16.0) without the prior and 25.9% (24.6 to 27.2) with it.

## By kind of eye

| Kind | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| cat | 11 | 45.5% (18.2 to 72.7) | 63.6% (36.4 to 90.9) | 9.1% |
| dog | 6 | 33.3% (0.0 to 83.3) | 33.3% (0.0 to 83.3) | 33.3% |
| squirrel | 36 | 55.6% (38.9 to 72.2) | 61.1% (47.2 to 77.8) | 33.3% |
| deer | 36 | 47.2% (30.6 to 63.9) | 72.2% (55.6 to 86.1) | 16.7% |
| rabbit | 31 | 67.7% (51.6 to 83.9) | 96.8% (90.3 to 100.0) | 61.3% |
| hawk | 82 | 52.4% (42.6 to 63.4) | 70.7% (61.0 to 80.5) | 34.2% |
| wader | 382 | 52.9% (47.9 to 58.1) | 80.1% (76.2 to 84.0) | 45.6% |
| bird | 531 | 36.9% (32.8 to 41.1) | 61.8% (57.6 to 65.9) | 23.4% |
| alligator | 110 | 87.3% (80.9 to 92.7) | 96.4% (92.7 to 99.1) | 66.4% |
| reptile | 268 | 32.5% (27.2 to 38.1) | 60.5% (54.5 to 66.0) | 13.4% |
| frog | 97 | 16.5% (9.3 to 24.7) | 48.4% (38.1 to 57.7) | 8.2% |
| bee | 126 | 11.1% (6.3 to 16.7) | 38.9% (30.9 to 47.6) | 2.4% |
| insect | 962 | 13.6% (11.5 to 15.8) | 27.8% (24.9 to 30.6) | 7.2% |
| plant | 1223 | 15.7% (13.6 to 17.8) | 27.8% (25.4 to 30.2) | 4.8% |
| other | 296 | 15.5% (11.5 to 19.9) | 29.4% (24.3 to 34.5) | 4.0% |

## By class

| Kingdom / class | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| Animalia / Insecta | 1088 | 13.3% (11.5 to 15.4) | 29.0% (26.4 to 31.8) | 6.6% |
| Animalia / Aves | 995 | 44.3% (41.4 to 47.3) | 69.5% (66.6 to 72.4) | 32.8% |
| Plantae / Magnoliopsida | 878 | 11.2% (9.2 to 13.2) | 22.8% (20.2 to 25.5) | 2.9% |
| Plantae / Liliopsida | 291 | 29.2% (24.1 to 34.4) | 41.2% (35.7 to 47.1) | 11.3% |
| Animalia / Squamata | 209 | 32.1% (25.8 to 38.3) | 59.3% (52.1 to 65.5) | 11.5% |
| Animalia / Arachnida | 154 | 15.6% (9.7 to 21.4) | 29.2% (22.1 to 36.4) | 2.6% |
| Animalia / Mammalia | 139 | 48.2% (40.3 to 56.8) | 66.9% (59.0 to 74.8) | 30.2% |
| Animalia / Crocodylia | 110 | 87.3% (80.9 to 92.7) | 96.4% (92.7 to 99.1) | 66.4% |
| Animalia / Amphibia | 101 | 15.8% (8.9 to 22.8) | 49.5% (39.6 to 59.4) | 8.9% |
| Animalia / Testudines | 59 | 33.9% (22.0 to 45.8) | 64.4% (50.8 to 76.3) | 20.3% |
| Fungi / Agaricomycetes | 39 | 20.5% (7.7 to 33.3) | 20.5% (7.7 to 33.3) | 0.0% |
| Plantae / Polypodiopsida | 38 | 15.8% (5.3 to 28.9) | 34.2% (21.1 to 50.0) | 0.0% |
| all other classes | 96 | 15.6% (9.3 to 22.9) | 33.3% (25.0 to 42.7) | 6.2% |

## By how often the species was recorded before 2025

| Records before 2025 | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| not in the list | 36 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 0.0% |
| 1 or 2 records | 58 | 0.0% (0.0 to 0.0) | 1.7% (0.0 to 5.2) | 5.2% |
| 3 to 9 | 138 | 0.7% (0.0 to 2.2) | 2.9% (0.7 to 5.8) | 4.3% |
| 10 to 49 | 468 | 4.5% (2.6 to 6.4) | 14.1% (11.1 to 17.1) | 5.8% |
| 50 to 199 | 1195 | 11.1% (9.4 to 13.0) | 28.7% (26.3 to 31.3) | 5.6% |
| 200 or more | 2302 | 40.5% (38.6 to 42.5) | 61.8% (59.8 to 63.7) | 22.7% |

## By calendar month

| Month | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| 01 | 208 | 29.3% (23.1 to 35.6) | 52.4% (45.7 to 59.1) | 20.2% |
| 02 | 251 | 33.1% (27.5 to 39.0) | 49.8% (43.8 to 55.8) | 22.7% |
| 03 | 458 | 24.4% (20.7 to 28.4) | 43.0% (38.6 to 47.4) | 14.8% |
| 04 | 755 | 22.9% (20.0 to 26.0) | 41.7% (38.3 to 45.4) | 13.4% |
| 05 | 383 | 26.4% (22.2 to 30.8) | 44.1% (39.2 to 49.1) | 17.0% |
| 06 | 317 | 22.7% (18.3 to 27.5) | 38.2% (33.1 to 43.5) | 11.7% |
| 07 | 384 | 24.2% (20.1 to 28.9) | 40.4% (35.7 to 45.3) | 12.2% |
| 08 | 368 | 28.8% (24.2 to 33.4) | 44.6% (39.4 to 49.7) | 14.1% |
| 09 | 454 | 23.8% (19.8 to 27.8) | 42.5% (37.9 to 46.9) | 13.4% |
| 10 | 227 | 23.8% (18.5 to 29.1) | 39.6% (33.5 to 45.8) | 11.9% |
| 11 | 258 | 29.1% (23.3 to 34.9) | 49.2% (43.0 to 55.0) | 13.2% |
| 12 | 134 | 37.3% (29.1 to 46.3) | 53.7% (45.5 to 61.9) | 26.1% |

## Kind of eye from the kind phrases: what was said (columns) for each true kind (rows)

Accuracy 72.0% (70.6 to 73.5). Photos called `person`: 0.05%; called `none`: 0.21% (the test split holds neither).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | person | other | none |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 9 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| dog | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| squirrel | 0 | 0 | 27 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 4 | 0 |
| deer | 0 | 1 | 0 | 24 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 4 | 0 | 3 | 0 |
| rabbit | 0 | 0 | 3 | 0 | 25 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| hawk | 0 | 0 | 0 | 1 | 1 | 64 | 6 | 5 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 2 |
| wader | 0 | 0 | 3 | 0 | 2 | 11 | 316 | 26 | 10 | 3 | 0 | 1 | 3 | 3 | 0 | 4 | 0 |
| bird | 4 | 4 | 25 | 1 | 7 | 49 | 126 | 254 | 11 | 8 | 6 | 3 | 7 | 14 | 1 | 7 | 4 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 102 | 2 | 1 | 0 | 0 | 2 | 0 | 1 | 0 |
| reptile | 0 | 0 | 6 | 0 | 0 | 1 | 2 | 1 | 38 | 149 | 7 | 0 | 22 | 17 | 0 | 23 | 2 |
| frog | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 13 | 57 | 0 | 13 | 0 | 0 | 11 | 0 |
| bee | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 89 | 28 | 5 | 0 | 3 | 0 |
| insect | 2 | 0 | 3 | 0 | 1 | 3 | 2 | 5 | 2 | 53 | 22 | 59 | 719 | 43 | 0 | 48 | 0 |
| plant | 0 | 0 | 2 | 0 | 0 | 2 | 6 | 1 | 2 | 10 | 1 | 26 | 43 | 1121 | 1 | 8 | 0 |
| other | 3 | 1 | 5 | 1 | 1 | 1 | 0 | 0 | 3 | 21 | 2 | 6 | 144 | 44 | 0 | 64 | 0 |

## Kind of eye taken from the top species, with the prior

Accuracy 77.7% (76.5 to 78.9).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | other |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 5 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 1 |
| dog | 1 | 2 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| squirrel | 0 | 0 | 20 | 0 | 2 | 0 | 2 | 1 | 0 | 4 | 1 | 0 | 0 | 5 | 1 |
| deer | 0 | 0 | 0 | 17 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 7 | 4 | 6 |
| rabbit | 0 | 0 | 0 | 0 | 22 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 7 | 0 |
| hawk | 0 | 0 | 0 | 1 | 1 | 61 | 4 | 5 | 0 | 1 | 0 | 0 | 3 | 5 | 1 |
| wader | 0 | 0 | 1 | 0 | 2 | 2 | 314 | 33 | 9 | 3 | 0 | 0 | 5 | 11 | 2 |
| bird | 0 | 0 | 4 | 0 | 4 | 19 | 39 | 382 | 8 | 13 | 2 | 0 | 23 | 32 | 5 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 96 | 5 | 1 | 0 | 0 | 4 | 2 |
| reptile | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 2 | 23 | 176 | 4 | 0 | 31 | 23 | 6 |
| frog | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 19 | 54 | 0 | 19 | 2 | 1 |
| bee | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 1 | 2 | 66 | 29 | 19 | 6 |
| insect | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 11 | 3 | 62 | 24 | 28 | 737 | 50 | 46 |
| plant | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 9 | 1 | 3 | 50 | 1134 | 23 |
| other | 1 | 0 | 2 | 1 | 0 | 0 | 0 | 1 | 2 | 16 | 8 | 0 | 64 | 26 | 175 |

## Commonest mistakes

Of 3073 wrong answers for species that are in the list, 110 named another species of the same genus and 466 another species of the same family. 36 test photos show a species that is not in the list.

| Photos | The species | What was said | Observations |
|---:|---|---|---|
| 9 | *Liquidambar styraciflua* (American sweetgum) | *Cnidoscolus stimulosus* (spurge nettle) | [264029450](https://www.inaturalist.org/observations/264029450) [270192735](https://www.inaturalist.org/observations/270192735) [270791806](https://www.inaturalist.org/observations/270791806) |
| 8 | *Bidens alba* (White beggarticks) | *Oxalis corniculata* (Creeping Woodsorrel) | [258043630](https://www.inaturalist.org/observations/258043630) [258058735](https://www.inaturalist.org/observations/258058735) [258502312](https://www.inaturalist.org/observations/258502312) |
| 8 | *Tillandsia usneoides* (Spanish moss) | *Leucauge argyrobapta* (Mabel Orchard Orbweaver) | [282177236](https://www.inaturalist.org/observations/282177236) [300178060](https://www.inaturalist.org/observations/300178060) [300745077](https://www.inaturalist.org/observations/300745077) |
| 8 | *Vitis rotundifolia* (muscadine) | *Cnidoscolus stimulosus* (spurge nettle) | [265099555](https://www.inaturalist.org/observations/265099555) [279112456](https://www.inaturalist.org/observations/279112456) [288354635](https://www.inaturalist.org/observations/288354635) |
| 8 | *Egretta thula* (Snowy Egret) | *Ardea alba* (Great Egret) | [257540383](https://www.inaturalist.org/observations/257540383) [257514925](https://www.inaturalist.org/observations/257514925) [278980010](https://www.inaturalist.org/observations/278980010) |
| 7 | *Bidens alba* (White beggarticks) | *Torenia crustacea* (Brittle False Pimpernel) | [294456544](https://www.inaturalist.org/observations/294456544) [318519961](https://www.inaturalist.org/observations/318519961) [322612877](https://www.inaturalist.org/observations/322612877) |
| 7 | *Parthenocissus quinquefolia* (Virginia creeper) | *Toxicodendron radicans* (eastern poison ivy) | [273175823](https://www.inaturalist.org/observations/273175823) [327404110](https://www.inaturalist.org/observations/327404110) [318659550](https://www.inaturalist.org/observations/318659550) |
| 7 | *Coluber constrictor* (North American Racer) | *Nerodia fasciata* (Banded Watersnake) | [312508530](https://www.inaturalist.org/observations/312508530) [341929173](https://www.inaturalist.org/observations/341929173) [342963071](https://www.inaturalist.org/observations/342963071) |
| 6 | *Callicarpa americana* (American beautyberry) | *Cnidoscolus stimulosus* (spurge nettle) | [273173349](https://www.inaturalist.org/observations/273173349) [275149528](https://www.inaturalist.org/observations/275149528) [344659489](https://www.inaturalist.org/observations/344659489) |
| 6 | *Tillandsia usneoides* (Spanish moss) | *Quercus virginiana* (southern live oak) | [286594932](https://www.inaturalist.org/observations/286594932) [298493902](https://www.inaturalist.org/observations/298493902) [300178351](https://www.inaturalist.org/observations/300178351) |
| 6 | *Tradescantia ohiensis* (Ohio spiderwort) | *Tradescantia fluminensis* (Rio Spiderwort) | [261844048](https://www.inaturalist.org/observations/261844048) [270636391](https://www.inaturalist.org/observations/270636391) [341794464](https://www.inaturalist.org/observations/341794464) |
| 6 | *Sylvilagus palustris* (Marsh Rabbit) | *Asimina longifolia* (polecatbush) | [277875606](https://www.inaturalist.org/observations/277875606) [277870506](https://www.inaturalist.org/observations/277870506) [279864187](https://www.inaturalist.org/observations/279864187) |
| 6 | *Dryophytes squirellus* (Squirrel Tree Frog) | *Dryophytes cinereus* (Green Treefrog) | [277900760](https://www.inaturalist.org/observations/277900760) [287282858](https://www.inaturalist.org/observations/287282858) [294496266](https://www.inaturalist.org/observations/294496266) |
| 5 | *Anolis carolinensis* (Green Anole) | *Anolis sagrei* (Brown Anole) | [260386834](https://www.inaturalist.org/observations/260386834) [311709818](https://www.inaturalist.org/observations/311709818) [314389827](https://www.inaturalist.org/observations/314389827) |
| 5 | *Ardea alba* (Great Egret) | *Egretta thula* (Snowy Egret) | [270078942](https://www.inaturalist.org/observations/270078942) [274807407](https://www.inaturalist.org/observations/274807407) [304486496](https://www.inaturalist.org/observations/304486496) |
