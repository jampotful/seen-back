# tinyclip-8m-16 on the test split

_This file is written by `tools/eval/report.py` from `docs/eval/study1.json`. Rerun the script to change it._

Species rows made from the English name; settings chosen on `val`: {"min_n": 1, "lam": 0.0, "c": 0.1, "ratio": 0.012, "t_species": 70, "alpha_prior": 0.84, "species_in_list": 5911, "combinations_tried": 108}. Top-1 15.4% (14.3 to 16.5) without the prior and 26.4% (25.1 to 27.7) with it.

## By kind of eye

| Kind | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| cat | 11 | 45.5% (18.2 to 72.7) | 63.6% (36.4 to 90.9) | 0.0% |
| dog | 6 | 33.3% (0.0 to 83.3) | 33.3% (0.0 to 83.3) | 33.3% |
| squirrel | 36 | 55.6% (38.9 to 72.2) | 61.1% (47.2 to 77.8) | 33.3% |
| deer | 36 | 44.4% (27.8 to 61.1) | 72.2% (55.6 to 86.1) | 22.2% |
| rabbit | 31 | 67.7% (51.6 to 83.9) | 96.8% (90.3 to 100.0) | 61.3% |
| hawk | 82 | 53.7% (43.9 to 64.6) | 72.0% (62.2 to 81.7) | 35.4% |
| wader | 382 | 54.2% (49.2 to 59.4) | 82.2% (78.5 to 85.9) | 46.6% |
| bird | 531 | 37.3% (33.1 to 41.4) | 62.2% (58.0 to 65.9) | 24.1% |
| alligator | 110 | 86.4% (80.0 to 92.7) | 96.4% (92.7 to 99.1) | 66.4% |
| reptile | 268 | 32.1% (26.9 to 37.7) | 59.3% (53.7 to 64.9) | 13.1% |
| frog | 97 | 18.6% (11.3 to 25.8) | 46.4% (36.1 to 55.7) | 10.3% |
| bee | 126 | 11.1% (6.3 to 16.7) | 38.9% (30.2 to 47.6) | 3.2% |
| insect | 962 | 13.9% (11.8 to 16.1) | 28.8% (26.0 to 31.7) | 7.7% |
| plant | 1223 | 15.9% (13.9 to 18.1) | 28.3% (25.9 to 30.7) | 4.7% |
| other | 296 | 17.6% (13.2 to 22.0) | 32.1% (27.0 to 37.5) | 5.7% |

## By class

| Kingdom / class | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| Animalia / Insecta | 1088 | 13.6% (11.7 to 15.7) | 30.0% (27.4 to 32.7) | 7.2% |
| Animalia / Aves | 995 | 45.1% (42.1 to 48.3) | 70.7% (67.7 to 73.4) | 33.7% |
| Plantae / Magnoliopsida | 878 | 10.9% (8.9 to 12.9) | 22.3% (19.7 to 25.1) | 3.1% |
| Plantae / Liliopsida | 291 | 30.9% (25.8 to 36.1) | 45.0% (39.2 to 50.9) | 10.0% |
| Animalia / Squamata | 209 | 31.1% (24.9 to 37.3) | 58.9% (52.1 to 65.5) | 11.0% |
| Animalia / Arachnida | 154 | 18.8% (13.0 to 25.3) | 33.8% (26.6 to 41.6) | 5.2% |
| Animalia / Mammalia | 139 | 47.5% (39.6 to 56.1) | 67.6% (60.4 to 75.5) | 30.9% |
| Animalia / Crocodylia | 110 | 86.4% (80.0 to 92.7) | 96.4% (92.7 to 99.1) | 66.4% |
| Animalia / Amphibia | 101 | 17.8% (10.9 to 25.7) | 47.5% (37.6 to 57.4) | 10.9% |
| Animalia / Testudines | 59 | 35.6% (23.7 to 47.5) | 61.0% (47.5 to 72.9) | 20.3% |
| Fungi / Agaricomycetes | 39 | 20.5% (7.7 to 33.3) | 20.5% (7.7 to 33.3) | 2.6% |
| Plantae / Polypodiopsida | 38 | 18.4% (7.9 to 31.6) | 34.2% (21.1 to 50.0) | 0.0% |
| all other classes | 96 | 15.6% (8.3 to 22.9) | 32.3% (22.9 to 41.7) | 6.2% |

## By how often the species was recorded before 2025

| Records before 2025 | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| not in the list | 36 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 0.0% |
| 1 or 2 records | 58 | 0.0% (0.0 to 0.0) | 1.7% (0.0 to 5.2) | 5.2% |
| 3 to 9 | 138 | 0.7% (0.0 to 2.2) | 2.9% (0.7 to 5.8) | 5.1% |
| 10 to 49 | 468 | 4.3% (2.6 to 6.2) | 15.0% (12.0 to 18.2) | 5.1% |
| 50 to 199 | 1195 | 11.7% (10.0 to 13.6) | 28.9% (26.4 to 31.5) | 6.0% |
| 200 or more | 2302 | 41.1% (39.1 to 43.0) | 62.9% (60.9 to 64.8) | 23.5% |

## By calendar month

| Month | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| 01 | 208 | 28.8% (22.6 to 35.1) | 52.4% (45.2 to 59.1) | 20.2% |
| 02 | 251 | 33.9% (28.3 to 39.8) | 51.4% (45.4 to 57.4) | 22.7% |
| 03 | 458 | 24.0% (20.3 to 28.0) | 42.8% (38.4 to 47.4) | 14.8% |
| 04 | 755 | 23.3% (20.3 to 26.4) | 42.1% (38.5 to 45.7) | 13.4% |
| 05 | 383 | 27.2% (23.0 to 31.6) | 46.0% (41.2 to 50.9) | 17.8% |
| 06 | 317 | 24.3% (19.6 to 29.3) | 40.1% (34.7 to 45.4) | 12.9% |
| 07 | 384 | 25.0% (20.6 to 29.7) | 41.9% (37.0 to 47.1) | 13.3% |
| 08 | 368 | 28.3% (23.6 to 32.9) | 45.1% (39.9 to 50.3) | 14.4% |
| 09 | 454 | 24.2% (20.3 to 28.2) | 42.7% (37.9 to 47.4) | 14.3% |
| 10 | 227 | 26.4% (21.1 to 32.2) | 40.5% (34.4 to 46.7) | 13.2% |
| 11 | 258 | 28.3% (22.9 to 34.1) | 48.4% (42.6 to 54.3) | 13.2% |
| 12 | 134 | 38.8% (30.6 to 47.0) | 55.2% (47.0 to 63.4) | 26.9% |

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

Accuracy 78.2% (77.0 to 79.4).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | other |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 5 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 1 |
| dog | 1 | 2 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| squirrel | 0 | 0 | 20 | 0 | 2 | 0 | 2 | 1 | 0 | 4 | 1 | 0 | 0 | 5 | 1 |
| deer | 0 | 0 | 0 | 16 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 6 | 5 | 6 |
| rabbit | 0 | 0 | 0 | 0 | 22 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 7 | 0 |
| hawk | 0 | 0 | 0 | 1 | 1 | 61 | 4 | 5 | 0 | 1 | 0 | 0 | 3 | 6 | 0 |
| wader | 0 | 0 | 1 | 0 | 2 | 1 | 318 | 31 | 9 | 2 | 0 | 0 | 5 | 11 | 2 |
| bird | 0 | 0 | 4 | 0 | 4 | 17 | 45 | 385 | 8 | 11 | 2 | 0 | 20 | 32 | 3 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 95 | 5 | 1 | 0 | 0 | 4 | 3 |
| reptile | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 1 | 23 | 178 | 4 | 0 | 23 | 29 | 6 |
| frog | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 20 | 56 | 0 | 17 | 2 | 0 |
| bee | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 1 | 2 | 64 | 30 | 19 | 7 |
| insect | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 12 | 3 | 62 | 22 | 24 | 734 | 58 | 45 |
| plant | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 11 | 1 | 4 | 42 | 1141 | 21 |
| other | 1 | 0 | 2 | 1 | 0 | 0 | 0 | 1 | 2 | 19 | 6 | 1 | 52 | 26 | 185 |

## Commonest mistakes

Of 3054 wrong answers for species that are in the list, 108 named another species of the same genus and 466 another species of the same family. 36 test photos show a species that is not in the list.

| Photos | The species | What was said | Observations |
|---:|---|---|---|
| 10 | *Tillandsia usneoides* (Spanish moss) | *Leucauge argyrobapta* (Mabel Orchard Orbweaver) | [282177236](https://www.inaturalist.org/observations/282177236) [298418777](https://www.inaturalist.org/observations/298418777) [300178060](https://www.inaturalist.org/observations/300178060) |
| 8 | *Bidens alba* (White beggarticks) | *Oxalis corniculata* (Creeping Woodsorrel) | [258043630](https://www.inaturalist.org/observations/258043630) [258058735](https://www.inaturalist.org/observations/258058735) [258502312](https://www.inaturalist.org/observations/258502312) |
| 8 | *Liquidambar styraciflua* (American sweetgum) | *Cnidoscolus stimulosus* (spurge nettle) | [264029450](https://www.inaturalist.org/observations/264029450) [270192735](https://www.inaturalist.org/observations/270192735) [270791806](https://www.inaturalist.org/observations/270791806) |
| 8 | *Parthenocissus quinquefolia* (Virginia creeper) | *Toxicodendron radicans* (eastern poison ivy) | [273175823](https://www.inaturalist.org/observations/273175823) [327404110](https://www.inaturalist.org/observations/327404110) [315730332](https://www.inaturalist.org/observations/315730332) |
| 8 | *Vitis rotundifolia* (muscadine) | *Cnidoscolus stimulosus* (spurge nettle) | [265099555](https://www.inaturalist.org/observations/265099555) [279112456](https://www.inaturalist.org/observations/279112456) [288354635](https://www.inaturalist.org/observations/288354635) |
| 8 | *Egretta thula* (Snowy Egret) | *Ardea alba* (Great Egret) | [257540383](https://www.inaturalist.org/observations/257540383) [257514925](https://www.inaturalist.org/observations/257514925) [278980010](https://www.inaturalist.org/observations/278980010) |
| 6 | *Bidens alba* (White beggarticks) | *Torenia crustacea* (Brittle False Pimpernel) | [294456544](https://www.inaturalist.org/observations/294456544) [318519961](https://www.inaturalist.org/observations/318519961) [322612877](https://www.inaturalist.org/observations/322612877) |
| 6 | *Tillandsia usneoides* (Spanish moss) | *Quercus virginiana* (southern live oak) | [286594932](https://www.inaturalist.org/observations/286594932) [298493902](https://www.inaturalist.org/observations/298493902) [300178351](https://www.inaturalist.org/observations/300178351) |
| 6 | *Ardisia crenata* (Coralberry) | *Toxicodendron radicans* (eastern poison ivy) | [265845925](https://www.inaturalist.org/observations/265845925) [274155961](https://www.inaturalist.org/observations/274155961) [345385244](https://www.inaturalist.org/observations/345385244) |
| 6 | *Coluber constrictor* (North American Racer) | *Nerodia fasciata* (Banded Watersnake) | [312508530](https://www.inaturalist.org/observations/312508530) [341929173](https://www.inaturalist.org/observations/341929173) [342963071](https://www.inaturalist.org/observations/342963071) |
| 6 | *Sylvilagus palustris* (Marsh Rabbit) | *Asimina longifolia* (polecatbush) | [277875606](https://www.inaturalist.org/observations/277875606) [277870506](https://www.inaturalist.org/observations/277870506) [279864187](https://www.inaturalist.org/observations/279864187) |
| 5 | *Anolis carolinensis* (Green Anole) | *Anolis sagrei* (Brown Anole) | [260386834](https://www.inaturalist.org/observations/260386834) [311709818](https://www.inaturalist.org/observations/311709818) [314389827](https://www.inaturalist.org/observations/314389827) |
| 5 | *Ardea alba* (Great Egret) | *Egretta thula* (Snowy Egret) | [270078942](https://www.inaturalist.org/observations/270078942) [274807407](https://www.inaturalist.org/observations/274807407) [304486496](https://www.inaturalist.org/observations/304486496) |
| 5 | *Grus canadensis* (Sandhill Crane) | *Eudocimus albus* (White Ibis) | [324912878](https://www.inaturalist.org/observations/324912878) [326935378](https://www.inaturalist.org/observations/326935378) [332213432](https://www.inaturalist.org/observations/332213432) |
| 5 | *Orgyia detrita* (Live Oak Tussock Moth) | *Malacosoma americana* (Eastern Tent Caterpillar Moth) | [267923959](https://www.inaturalist.org/observations/267923959) [268443472](https://www.inaturalist.org/observations/268443472) [269040944](https://www.inaturalist.org/observations/269040944) |
