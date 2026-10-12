# The group head on world photos

Made by `tools/world/head.py` (2026-10-12T21:29:37Z). The page is scored as it would run: away from the county's time zone the page leaves the county list out (the head alone); in it, the head and the list are combined by the rule mix.

Recipe chosen on the tuning photos: power 0.0, with the Alachua training photos. Groups carried (3): primate, whale, bat. Put back in `other` (16): fungus, slime, spider, jumper, fish, shark, snail, sealife, crab, salamander, worm, scorpion, tick, mammal, flyingfox, cephalopod.
Settings for the county: t_kind 0.5, w_kind 1.0, kind_at 0.57 (levels {'world': 0.57, 'alachua': 0.47, 'coco': 0.22}).

| Pass mark | Measured | Passes |
|---|---|---|
| Old groups right, world test photos, the head alone (away from the county): 95% interval of the paired difference above −2 points | today 0.6838, new 0.7121, difference 0.0283 (0.0167 to 0.0398), 4200 photos | yes |
| Old groups right, Alachua test photos, head and list combined: 95% interval of the paired difference above −2 points | today 0.9018, new 0.846, difference -0.0558 (-0.0654 to -0.0468), 3871 photos | no |
| Every group carried found (named and right when called, 75% or more each, world test photos, head alone) | 3 of 3 pass | yes |
| People, pets and rooms within 1 point of today (COCO test) | today 0.9467; new with the list 0.9499, alone 0.9499; a new group named 0 times in 2480 answers | yes |
| `other` given a view under 10% (world test photos, head alone) | today 0.32, new 0.1018, of 5100 photos | no |
| Head under 50 KB | 20480 bytes | yes |

For the record, the world test photos with the county list combined (as in the county's time zone): old groups today 0.6838, new 0.7121, difference 0.0283 (0.0167 to 0.0398).

| Group carried | test photos | named | called | right when called | passes |
|---|---:|---:|---:|---:|---|
| primate | 300 | 0.8667 | 308 | 0.8442 | yes |
| whale | 300 | 0.8 | 286 | 0.8392 | yes |
| bat | 300 | 0.7867 | 278 | 0.8489 | yes |

`other` on the world test photos, by what the photo shows:

| Truth | photos | given a view today | given a view, new | the views given, new |
|---|---:|---:|---:|---|
| other | 300 | 0.4533 | 0.2167 | plant 40, insect 14, bird 2, cat 2, wader 1 |
| fungus | 300 | 0.38 | 0.17 | plant 34, insect 14, bee 3 |
| slime | 300 | 0.1967 | 0.0267 | plant 4, insect 4 |
| spider | 300 | 0.2067 | 0.0833 | insect 15, bee 6, plant 2, reptile 1, rabbit 1 |
| jumper | 300 | 0.3133 | 0.13 | insect 29, bee 7, frog 2, rabbit 1 |
| fish | 300 | 0.13 | 0.0333 | reptile 4, bird 2, frog 2, plant 1, alligator 1 |
| shark | 300 | 0.1333 | 0.02 | bird 3, insect 2, plant 1 |
| snail | 300 | 0.1467 | 0.0367 | insect 6, plant 2, reptile 2, frog 1 |
| sealife | 300 | 0.09 | 0.0267 | plant 6, insect 1, reptile 1 |
| crab | 300 | 0.2767 | 0.0767 | insect 18, plant 2, frog 2, alligator 1 |
| salamander | 300 | 0.76 | 0.1867 | reptile 41, frog 11, alligator 2, plant 1, bee 1 |
| worm | 300 | 0.3067 | 0.0767 | insect 13, reptile 6, plant 3, bird 1 |
| scorpion | 300 | 0.4267 | 0.08 | insect 20, bee 2, frog 2 |
| tick | 300 | 0.3433 | 0.09 | insect 19, reptile 3, deer 2, plant 1, frog 1 |
| mammal | 300 | 0.6433 | 0.38 | squirrel 37, cat 19, rabbit 14, dog 13, deer 10 |
| flyingfox | 300 | 0.5267 | 0.0967 | bird 13, insect 6, hawk 4, frog 2, plant 2 |
| cephalopod | 300 | 0.1067 | 0.0 |  |

The creatures with no group of their own given a view, by order: Martellivirales as plant 4; Sarcoptiformes as plant 4; Chroococcales as plant 4; Patatavirales as plant 3; Pseudomonadales as plant 3; ? as insect 3; Sarcoptiformes as insect 2; Nostocales as plant 2; Geplafuvirales as plant 2; Acholeplasmatales as plant 2; Picornavirales as insect 2; Trombidiformes as plant 2; Articulavirales as wader 1; Sarcoptiformes as bee 1; Peronosporales as plant 1; Mononegavirales as dog 1; Synechococcales as insect 1; Mesostigmata as plant 1; Cirlivirales as hawk 1; Mononegavirales as plant 1.

World test photos, every label: right 0.8056 (today 0.621); asserted 0.5742, right when asserted 0.9517.

Alachua test photos, every label: right 0.8431 (today 0.8919); asserted 0.6191, right when asserted 0.9728.

By continent (new, today): AF 0.8238, 0.626 of 1674; AN 0.7955, 0.6591 of 220; AS 0.7966, 0.6006 of 1790; EU 0.7927, 0.6176 of 1611; NA 0.8062, 0.6078 of 1739; OC 0.8023, 0.6442 of 1543; SA 0.8133, 0.6285 of 1623.

Commonest confusions: other as insect 163; other as plant 101; plant as other 98; insect as other 92; bee as insect 69; other as reptile 65; frog as other 59; squirrel as other 59; bat as other 52; reptile as other 50; whale as other 47; wader as bird 46; bird as wader 41; other as squirrel 38; bee as other 37.

The fold, on the tuning photos (carried, failing):
- 19 carried, world right 0.6971; failing: fungus 0.5033/0.5922, slime 0.77/0.7287, spider 0.7/0.6667, jumper 0.71/0.7889, fish 0.7467/0.7111, shark 0.7333/0.7261, snail 0.58/0.5762, sealife 0.5633/0.569, crab 0.5233/0.534, salamander 0.6567/0.7912, worm 0.5033/0.572, scorpion 0.6667/0.823, tick 0.7267/0.8226, mammal 0.5233/0.5131, flyingfox 0.7433/0.878, cephalopod 0.6633/0.6862
- 18 carried, world right 0.6989; failing: slime 0.7567/0.7299, spider 0.6967/0.672, jumper 0.7067/0.7766, fish 0.7533/0.7129, shark 0.7367/0.7246, snail 0.5667/0.5862, sealife 0.5667/0.5705, crab 0.52/0.5288, salamander 0.6567/0.7944, worm 0.5033/0.5593, scorpion 0.6633/0.8257, tick 0.7367/0.8277, mammal 0.5233/0.5268, flyingfox 0.7467/0.875, cephalopod 0.67/0.6955
- 17 carried, world right 0.7038; failing: slime 0.7633/0.7411, spider 0.6967/0.6808, jumper 0.7067/0.7852, fish 0.7667/0.7278, shark 0.7333/0.7333, snail 0.57/0.6042, sealife 0.5833/0.5833, crab 0.51/0.5406, salamander 0.6433/0.7975, scorpion 0.67/0.8204, tick 0.7333/0.8209, mammal 0.5267/0.5338, flyingfox 0.7467/0.875, cephalopod 0.6667/0.6873
- 16 carried, world right 0.7104; failing: spider 0.7/0.6774, jumper 0.7033/0.7844, fish 0.7567/0.7229, shark 0.74/0.7327, snail 0.54/0.6207, sealife 0.5633/0.5788, salamander 0.66/0.7888, scorpion 0.6667/0.823, tick 0.7233/0.822, mammal 0.5267/0.5374, flyingfox 0.7467/0.8819, cephalopod 0.6467/0.708
- 15 carried, world right 0.7058; failing: spider 0.7/0.6863, jumper 0.7067/0.7852, fish 0.7467/0.7134, shark 0.7367/0.7294, snail 0.53/0.6115, sealife 0.5667/0.5743, salamander 0.6333/0.7755, scorpion 0.6633/0.8326, tick 0.73/0.8233, flyingfox 0.7467/0.8854, cephalopod 0.6367/0.6895
- 14 carried, world right 0.7185; failing: spider 0.7/0.6818, jumper 0.7067/0.7852, fish 0.7367/0.7294, shark 0.73/0.7324, sealife 0.5167/0.6175, salamander 0.6267/0.7769, scorpion 0.66/0.8285, tick 0.7333/0.8429, flyingfox 0.7467/0.8854, cephalopod 0.6333/0.7224
- 13 carried, world right 0.7288; failing: slime 0.72/0.7552, spider 0.6933/0.682, jumper 0.71/0.7831, fish 0.7167/0.7363, shark 0.7233/0.7356, salamander 0.6267/0.7673, scorpion 0.6433/0.8502, tick 0.73/0.8359, flyingfox 0.7467/0.8854, cephalopod 0.6033/0.7542
- 12 carried, world right 0.74; failing: slime 0.7167/0.7544, spider 0.6933/0.691, jumper 0.71/0.786, fish 0.7067/0.7544, shark 0.69/0.7473, salamander 0.63/0.7778, scorpion 0.65/0.8405, tick 0.7333/0.8365
- 11 carried, world right 0.7469; failing: slime 0.7333/0.7666, spider 0.6967/0.6967, jumper 0.7033/0.7815, fish 0.6967/0.7518, shark 0.7033/0.7563, scorpion 0.66/0.839, tick 0.7333/0.8397, flyingfox 0.7433/0.8814
- 10 carried, world right 0.7484; failing: slime 0.73/0.7794, spider 0.6767/0.6835, jumper 0.71/0.7802, fish 0.6933/0.7429, shark 0.7/0.7609, tick 0.7267/0.8289, flyingfox 0.7433/0.8814
- 9 carried, world right 0.7544; failing: slime 0.72/0.7883, jumper 0.7067/0.7794, fish 0.7/0.7447, shark 0.7067/0.7544, tick 0.6967/0.8394, flyingfox 0.7467/0.8889
- 8 carried, world right 0.7614; failing: slime 0.72/0.7798, jumper 0.6867/0.8306, fish 0.6967/0.7385, shark 0.7/0.742, flyingfox 0.7433/0.892
- 7 carried, world right 0.7729; failing: slime 0.7267/0.7814, fish 0.7067/0.7491, shark 0.7033/0.7482
- 6 carried, world right 0.7791; failing: slime 0.7167/0.7734, fish 0.6567/0.7725, flyingfox 0.7367/0.884
- 5 carried, world right 0.7928; failing: slime 0.72/0.7742, flyingfox 0.7333/0.8871
- 4 carried, world right 0.8067; failing: flyingfox 0.7267/0.8826
- 3 carried, world right 0.8043; failing: none
