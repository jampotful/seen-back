# mobileclip2-s0 on the test split

_This file is written by `tools/eval/report.py` from `docs/eval/study1.json`. Rerun the script to change it._

Species rows made from the English name; settings chosen on `val`: {"min_n": 10, "lam": 0.0, "c": 1.0, "ratio": 0.012, "t_species": 70, "alpha_prior": 0.84, "species_in_list": 2143, "combinations_tried": 108}. Top-1 22.6% (21.3 to 23.8) without the prior and 33.8% (32.3 to 35.2) with it.

## By kind of eye

| Kind | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| cat | 11 | 18.2% (0.0 to 45.5) | 63.6% (36.4 to 90.9) | 9.1% |
| dog | 6 | 50.0% (16.7 to 83.3) | 83.3% (50.0 to 100.0) | 50.0% |
| squirrel | 36 | 61.1% (44.4 to 77.8) | 86.1% (75.0 to 97.2) | 27.8% |
| deer | 36 | 69.4% (52.8 to 83.3) | 72.2% (55.6 to 86.1) | 47.2% |
| rabbit | 31 | 90.3% (77.4 to 100.0) | 96.8% (90.3 to 100.0) | 77.4% |
| hawk | 82 | 52.4% (42.7 to 63.4) | 74.4% (64.6 to 84.2) | 43.9% |
| wader | 382 | 68.6% (64.1 to 73.0) | 90.3% (87.2 to 93.2) | 64.1% |
| bird | 531 | 43.9% (39.7 to 48.2) | 69.9% (66.1 to 73.6) | 32.4% |
| alligator | 110 | 81.8% (74.6 to 88.2) | 95.5% (90.9 to 99.1) | 62.7% |
| reptile | 268 | 46.6% (40.7 to 52.6) | 73.9% (69.0 to 79.1) | 25.4% |
| frog | 97 | 39.2% (29.9 to 48.4) | 71.1% (61.9 to 80.4) | 21.6% |
| bee | 126 | 35.7% (27.8 to 43.7) | 53.2% (44.4 to 61.9) | 11.9% |
| insect | 962 | 21.7% (19.2 to 24.4) | 38.9% (35.8 to 41.8) | 12.4% |
| plant | 1223 | 17.5% (15.3 to 19.8) | 32.1% (29.5 to 34.8) | 8.7% |
| other | 296 | 27.0% (22.0 to 32.4) | 45.6% (39.9 to 51.3) | 13.9% |

## By class

| Kingdom / class | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| Animalia / Insecta | 1088 | 23.4% (21.0 to 25.9) | 40.5% (37.8 to 43.4) | 12.3% |
| Animalia / Aves | 995 | 54.1% (51.1 to 57.2) | 78.1% (75.6 to 80.5) | 45.5% |
| Plantae / Magnoliopsida | 878 | 18.2% (15.8 to 20.7) | 31.6% (28.7 to 34.6) | 8.2% |
| Plantae / Liliopsida | 291 | 12.7% (8.9 to 16.5) | 29.9% (24.4 to 35.4) | 9.3% |
| Animalia / Squamata | 209 | 45.9% (38.8 to 52.6) | 71.3% (65.1 to 77.0) | 23.9% |
| Animalia / Arachnida | 154 | 29.2% (22.1 to 37.0) | 47.4% (39.6 to 55.8) | 18.2% |
| Animalia / Mammalia | 139 | 60.4% (52.5 to 68.3) | 76.3% (69.1 to 83.5) | 42.4% |
| Animalia / Crocodylia | 110 | 81.8% (74.6 to 88.2) | 95.5% (90.9 to 99.1) | 62.7% |
| Animalia / Amphibia | 101 | 38.6% (29.7 to 47.5) | 70.3% (61.4 to 79.2) | 20.8% |
| Animalia / Testudines | 59 | 49.1% (37.3 to 62.7) | 83.0% (72.9 to 91.5) | 30.5% |
| Fungi / Agaricomycetes | 39 | 20.5% (7.7 to 33.3) | 41.0% (25.6 to 56.4) | 7.7% |
| Plantae / Polypodiopsida | 38 | 28.9% (15.8 to 44.7) | 50.0% (34.2 to 65.8) | 7.9% |
| all other classes | 96 | 29.2% (19.8 to 38.5) | 49.0% (38.5 to 59.4) | 10.4% |

## By how often the species was recorded before 2025

| Records before 2025 | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| not in the list | 36 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 0.0% |
| 1 or 2 records | 58 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 17.2% |
| 3 to 9 | 138 | 0.0% (0.0 to 0.0) | 0.0% (0.0 to 0.0) | 10.1% |
| 10 to 49 | 468 | 9.8% (7.3 to 12.6) | 25.0% (21.4 to 28.8) | 9.2% |
| 50 to 199 | 1195 | 21.9% (19.7 to 24.3) | 44.6% (41.8 to 47.4) | 13.8% |
| 200 or more | 2302 | 48.3% (46.2 to 50.3) | 68.1% (66.0 to 69.9) | 31.1% |

## By calendar month

| Month | Photos | Top-1 with prior | Top-5 with prior | Top-1 without prior |
|---|---:|---:|---:|---:|
| 01 | 208 | 36.1% (29.8 to 42.8) | 56.2% (49.5 to 63.0) | 27.4% |
| 02 | 251 | 39.8% (33.9 to 45.8) | 62.5% (56.6 to 68.1) | 27.5% |
| 03 | 458 | 33.0% (28.6 to 37.1) | 55.5% (50.9 to 59.8) | 19.9% |
| 04 | 755 | 33.0% (29.5 to 36.6) | 49.5% (46.0 to 53.2) | 22.1% |
| 05 | 383 | 34.2% (29.8 to 38.9) | 50.4% (45.4 to 55.6) | 23.0% |
| 06 | 317 | 35.6% (30.6 to 41.0) | 51.1% (45.4 to 56.8) | 24.3% |
| 07 | 384 | 31.8% (27.1 to 36.5) | 48.2% (43.2 to 52.9) | 22.1% |
| 08 | 368 | 29.3% (24.7 to 34.0) | 47.5% (42.7 to 52.7) | 18.5% |
| 09 | 454 | 34.8% (30.4 to 39.2) | 55.3% (50.7 to 59.9) | 21.8% |
| 10 | 227 | 30.4% (24.7 to 36.1) | 52.4% (46.3 to 58.6) | 16.7% |
| 11 | 258 | 33.3% (27.5 to 39.1) | 55.8% (49.6 to 61.6) | 23.6% |
| 12 | 134 | 42.5% (33.6 to 50.7) | 64.2% (56.0 to 72.4) | 35.1% |

## Kind of eye from the kind phrases: what was said (columns) for each true kind (rows)

Accuracy 75.4% (74.1 to 76.6). Photos called `person`: 0.07%; called `none`: 0.17% (the test split holds neither).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | person | other | none |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 6 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| dog | 0 | 4 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| squirrel | 0 | 0 | 31 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| deer | 0 | 1 | 0 | 27 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 3 | 0 | 2 | 0 |
| rabbit | 0 | 0 | 5 | 0 | 23 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| hawk | 0 | 1 | 1 | 0 | 0 | 66 | 5 | 4 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 1 | 0 |
| wader | 0 | 0 | 2 | 0 | 0 | 5 | 335 | 21 | 9 | 2 | 0 | 1 | 2 | 5 | 0 | 0 | 0 |
| bird | 0 | 1 | 15 | 1 | 2 | 51 | 104 | 308 | 9 | 9 | 1 | 2 | 9 | 9 | 2 | 3 | 5 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 103 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 |
| reptile | 0 | 0 | 3 | 1 | 1 | 1 | 3 | 2 | 35 | 184 | 10 | 1 | 16 | 8 | 0 | 2 | 1 |
| frog | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 5 | 82 | 0 | 6 | 0 | 0 | 1 | 0 |
| bee | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 96 | 26 | 1 | 0 | 1 | 0 |
| insect | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 4 | 1 | 26 | 23 | 51 | 823 | 18 | 0 | 12 | 0 |
| plant | 0 | 0 | 4 | 0 | 0 | 0 | 3 | 1 | 8 | 9 | 16 | 33 | 105 | 1042 | 1 | 1 | 0 |
| other | 0 | 2 | 6 | 2 | 2 | 0 | 2 | 1 | 6 | 21 | 5 | 7 | 166 | 42 | 0 | 34 | 0 |

## Kind of eye taken from the top species, with the prior

Accuracy 83.5% (82.4 to 84.6).

| true \ said | cat | dog | squirrel | deer | rabbit | hawk | wader | bird | alligator | reptile | frog | bee | insect | plant | other |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 3 | 1 |
| dog | 0 | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| squirrel | 0 | 0 | 24 | 1 | 4 | 0 | 1 | 2 | 1 | 0 | 0 | 0 | 0 | 3 | 0 |
| deer | 0 | 1 | 0 | 26 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 3 |
| rabbit | 0 | 0 | 0 | 0 | 29 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| hawk | 0 | 0 | 0 | 0 | 0 | 61 | 6 | 7 | 0 | 0 | 0 | 0 | 2 | 6 | 0 |
| wader | 0 | 0 | 0 | 0 | 0 | 4 | 334 | 22 | 2 | 3 | 0 | 0 | 2 | 15 | 0 |
| bird | 0 | 0 | 2 | 0 | 2 | 15 | 41 | 407 | 2 | 9 | 0 | 0 | 22 | 26 | 5 |
| alligator | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 90 | 7 | 2 | 0 | 3 | 3 | 2 |
| reptile | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 1 | 2 | 208 | 2 | 0 | 21 | 22 | 8 |
| frog | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 11 | 76 | 0 | 3 | 3 | 2 |
| bee | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 87 | 22 | 12 | 3 |
| insect | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 39 | 6 | 21 | 814 | 46 | 34 |
| plant | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 7 | 1 | 3 | 57 | 1120 | 31 |
| other | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 2 | 9 | 4 | 3 | 30 | 24 | 221 |

## Commonest mistakes

Of 2742 wrong answers for species that are in the list, 146 named another species of the same genus and 525 another species of the same family. 36 test photos show a species that is not in the list.

| Photos | The species | What was said | Observations |
|---:|---|---|---|
| 21 | *Tillandsia usneoides* (Spanish moss) | *Quercus virginiana* (southern live oak) | [258041966](https://www.inaturalist.org/observations/258041966) [269389202](https://www.inaturalist.org/observations/269389202) [275829239](https://www.inaturalist.org/observations/275829239) |
| 14 | *Tillandsia usneoides* (Spanish moss) | *Distimake dissectus* (Alamo vine) | [300178257](https://www.inaturalist.org/observations/300178257) [302906275](https://www.inaturalist.org/observations/302906275) [302495385](https://www.inaturalist.org/observations/302495385) |
| 11 | *Tillandsia usneoides* (Spanish moss) | *Phoradendron leucarpum* (American Mistletoe) | [300745029](https://www.inaturalist.org/observations/300745029) [304541566](https://www.inaturalist.org/observations/304541566) [304541589](https://www.inaturalist.org/observations/304541589) |
| 11 | *Parthenocissus quinquefolia* (Virginia creeper) | *Toxicodendron radicans* (eastern poison ivy) | [273193100](https://www.inaturalist.org/observations/273193100) [273175823](https://www.inaturalist.org/observations/273175823) [327404110](https://www.inaturalist.org/observations/327404110) |
| 10 | *Ardisia crenata* (Coralberry) | *Prunus caroliniana* (Carolina laurelcherry) | [259055365](https://www.inaturalist.org/observations/259055365) [260316816](https://www.inaturalist.org/observations/260316816) [264133197](https://www.inaturalist.org/observations/264133197) |
| 10 | *Sabal palmetto* (cabbage palmetto) | *Serenoa repens* (saw palmetto) | [260736021](https://www.inaturalist.org/observations/260736021) [260738332](https://www.inaturalist.org/observations/260738332) [261485232](https://www.inaturalist.org/observations/261485232) |
| 9 | *Dryophytes squirellus* (Squirrel Tree Frog) | *Dryophytes cinereus* (Green Treefrog) | [267517969](https://www.inaturalist.org/observations/267517969) [277900760](https://www.inaturalist.org/observations/277900760) [287282858](https://www.inaturalist.org/observations/287282858) |
| 7 | *Tillandsia usneoides* (Spanish moss) | *Asimina longifolia* (polecatbush) | [298493865](https://www.inaturalist.org/observations/298493865) [300178351](https://www.inaturalist.org/observations/300178351) [300178225](https://www.inaturalist.org/observations/300178225) |
| 6 | *Anolis carolinensis* (Green Anole) | *Anolis sagrei* (Brown Anole) | [260386834](https://www.inaturalist.org/observations/260386834) [275047138](https://www.inaturalist.org/observations/275047138) [311709818](https://www.inaturalist.org/observations/311709818) |
| 6 | *Coluber constrictor* (North American Racer) | *Nerodia fasciata* (Banded Watersnake) | [312508530](https://www.inaturalist.org/observations/312508530) [322680413](https://www.inaturalist.org/observations/322680413) [341929173](https://www.inaturalist.org/observations/341929173) |
| 5 | *Alligator mississippiensis* (American Alligator) | *Nerodia fasciata* (Banded Watersnake) | [261267492](https://www.inaturalist.org/observations/261267492) [277896165](https://www.inaturalist.org/observations/277896165) [320472410](https://www.inaturalist.org/observations/320472410) |
| 5 | *Ardea herodias* (Great Blue Heron) | *Egretta caerulea* (Little Blue Heron) | [260173151](https://www.inaturalist.org/observations/260173151) [284865338](https://www.inaturalist.org/observations/284865338) [322086277](https://www.inaturalist.org/observations/322086277) |
| 5 | *Bidens alba* (White beggarticks) | *Erigeron quercifolius* (oakleaf fleabane) | [269205028](https://www.inaturalist.org/observations/269205028) [273435830](https://www.inaturalist.org/observations/273435830) [276663258](https://www.inaturalist.org/observations/276663258) |
| 5 | *Callicarpa americana* (American beautyberry) | *Cnidoscolus stimulosus* (spurge nettle) | [275149528](https://www.inaturalist.org/observations/275149528) [344659489](https://www.inaturalist.org/observations/344659489) [365017304](https://www.inaturalist.org/observations/365017304) |
| 5 | *Erythemis simplicicollis* (Eastern Pondhawk) | *Pachydiplax longipennis* (Blue Dasher) | [270924716](https://www.inaturalist.org/observations/270924716) [317603794](https://www.inaturalist.org/observations/317603794) [319794448](https://www.inaturalist.org/observations/319794448) |
