# The group head on world photos

Made by `tools/world/head.py` (2026-10-13T02:15:21Z), recipe `merge`, encoder `tinyclip-39m-16`. The page is scored as it would run: away from the county's time zone the page leaves the county list out (the head alone); in it, the head and the list are combined by the rule mix.
Vectors of the new head's tuning and test photos: world fit world-fit, tune world-eval.wasm-int8-per-channel, test world-eval.wasm-int8-per-channel; alachua fit alachua-pre2025, tune alachua-2025.wasm-int8-per-channel, test alachua-2025.wasm-int8-per-channel; coco fit coco-kinds, tune coco-kinds, test coco-kinds.wasm-int8-per-channel. Today's page: encoder tinyclip-39m-16, world world-eval.wasm-int8-per-channel, alachua alachua-2025.wasm-int8-per-channel, coco_tune coco-kinds, coco_test coco-kinds.wasm-int8-per-channel.

Fitting: power 0.0, with the Alachua training photos; options {"with_alachua": "yes", "powers": "0", "alachua_weight": 3.0, "coco_weight": 10.0, "calibrate": true, "groups": "merge", "t_kinds": "0.5,1,2", "w_kinds": "0.5,0.7,0.9,1.0", "settle_on": "old", "other_view": null}. Groups named (3): primate, whale, bat. In `other` (16): fungus, slime, spider, jumper, fish, shark, snail, sealife, crab, salamander, worm, scorpion, tick, mammal, flyingfox, cephalopod.
Bias offsets calibrated on the world tuning photos: fungus +0.25, slime +0.25, jumper +0.25, fish -0.25, crab +0.25, salamander +0.75, worm +0.25, scorpion +0.75, tick +0.75, primate +0.25, whale -0.25.
Settings for the county: t_kind 1.0, w_kind 0.7, kind_at 0.86 (levels {'world': 0.86, 'alachua': 0.64, 'coco': 0.2}).

| Pass mark | Measured | Passes |
|---|---|---|
| Old groups right, world test photos, the head alone (away from the county): 95% interval of the paired difference above −2 points | today 0.6838, new 0.7074, difference 0.0236 (0.0124 to 0.0348), 4200 photos | yes |
| Old groups right, Alachua test photos, head and list combined: 95% interval of the paired difference above −2 points | today 0.9018, new 0.8856, difference -0.0163 (-0.0222 to -0.0106), 3871 photos | no |
| Every group named found (named and right when called, 75% or more each, world test photos, head alone) | 3 of 3 pass | yes |
| People, pets and rooms within 1 point of today (COCO test) | today 0.9467; new with the list 0.9553, alone 0.955; a new group named 0 times in 2480 answers | yes |
| `other` given a view under 10% (world test photos, head alone) | today 0.32, new 0.1049, of 5100 photos | no |
| Head under 50 KB | 36864 bytes | yes |

For the record, the world test photos with the county list combined (as in the county's time zone): old groups today 0.6838, new 0.7031, difference 0.0193 (0.0105 to 0.0286).

| Group named | test photos | named | called | right when called | passes |
|---|---:|---:|---:|---:|---|
| primate | 300 | 0.88 | 315 | 0.8381 | yes |
| whale | 300 | 0.7667 | 272 | 0.8456 | yes |
| bat | 300 | 0.8133 | 285 | 0.8561 | yes |

`other` on the world test photos, by what the photo shows:

| Truth | photos | given a view today | given a view, new | the views given, new |
|---|---:|---:|---:|---|
| other | 300 | 0.4533 | 0.2467 | plant 47, insect 14, bird 4, cat 3, wader 1 |
| fungus | 300 | 0.38 | 0.21 | plant 38, insect 23, bee 2 |
| slime | 300 | 0.1967 | 0.0267 | plant 4, insect 4 |
| spider | 300 | 0.2067 | 0.1067 | insect 20, bee 5, plant 4, reptile 2, rabbit 1 |
| jumper | 300 | 0.3133 | 0.1267 | insect 29, bee 6, frog 2, rabbit 1 |
| fish | 300 | 0.13 | 0.0467 | reptile 6, bird 3, insect 2, plant 1, alligator 1 |
| shark | 300 | 0.1333 | 0.02 | bird 3, insect 2, plant 1 |
| snail | 300 | 0.1467 | 0.0467 | insect 9, plant 3, frog 2 |
| sealife | 300 | 0.09 | 0.0267 | plant 7, reptile 1 |
| crab | 300 | 0.2767 | 0.0633 | insect 15, plant 2, alligator 1, frog 1 |
| salamander | 300 | 0.76 | 0.15 | reptile 31, frog 8, alligator 2, plant 2, bee 1 |
| worm | 300 | 0.3067 | 0.07 | insect 14, reptile 4, plant 2, bird 1 |
| scorpion | 300 | 0.4267 | 0.0933 | insect 25, plant 2, bee 1 |
| tick | 300 | 0.3433 | 0.08 | insect 17, reptile 2, deer 2, plant 1, frog 1 |
| mammal | 300 | 0.6433 | 0.3767 | squirrel 32, cat 19, deer 13, rabbit 11, dog 11 |
| flyingfox | 300 | 0.5267 | 0.08 | bird 11, insect 5, hawk 4, plant 2, deer 1 |
| cephalopod | 300 | 0.1067 | 0.0133 | bird 1, plant 1, frog 1, insect 1 |

The creatures with no group of their own given a view, by order: Sarcoptiformes as plant 7; ? as insect 4; Martellivirales as plant 3; Picornavirales as insect 3; Patatavirales as plant 3; Nostocales as plant 3; Chroococcales as plant 3; Pseudomonadales as plant 3; Trombidiformes as plant 3; Acholeplasmatales as plant 2; Mesostigmata as insect 2; Gonyaulacales as plant 2; Plasmodiophorida as plant 2; Albuginales as plant 1; Articulavirales as wader 1; Peronosporales as plant 1; Mononegavirales as cat 1; Mesostigmata as plant 1; Cirlivirales as bird 1; Rhizobiales as insect 1.

World test photos, every label: right 0.8024 (today 0.621); asserted 0.5955, right when asserted 0.9555.

Alachua test photos, every label: right 0.8794 (today 0.8919); asserted 0.6712, right when asserted 0.9835.

By continent (new, today): AF 0.8292, 0.626 of 1674; AN 0.8, 0.6591 of 220; AS 0.7922, 0.6006 of 1790; EU 0.7995, 0.6176 of 1611; NA 0.7987, 0.6078 of 1739; OC 0.7881, 0.6442 of 1543; SA 0.8065, 0.6285 of 1623.

Commonest confusions: other as insect 183; other as plant 123; plant as other 94; bee as insect 87; insect as other 81; wader as bird 71; other as reptile 54; squirrel as other 51; frog as other 49; whale as other 49; reptile as other 45; bat as other 39; dog as other 38; other as bat 37; bird as wader 35.

On the tuning photos, for the head that ships: old groups right on world photos 0.704 (today 0.6662), on Alachua photos 0.8894 (today 0.8941); `other` given a view 0.1067; COCO 0.9593 with the list, 0.9584 alone (today 0.9538).

The fold, on the tuning photos (t_kind, named, failing):
- t_kind 1.0, 19 named, world right 0.6792; failing: fungus 0.5367/0.5314, slime 0.7133/0.7329, spider 0.6333/0.7336, jumper 0.7067/0.7653, fish 0.6967/0.7308, shark 0.7333/0.7213, snail 0.5433/0.5863, sealife 0.55/0.5709, crab 0.5133/0.5185, salamander 0.7133/0.7063, worm 0.4767/0.5479, scorpion 0.7167/0.779, mammal 0.4767/0.4965, flyingfox 0.7167/0.8776, cephalopod 0.65/0.6964
- t_kind 1.0, 18 named, world right 0.6817; failing: fungus 0.5367/0.5331, slime 0.7133/0.7354, spider 0.6333/0.7364, jumper 0.7067/0.7653, fish 0.6967/0.7333, shark 0.7333/0.7213, snail 0.5333/0.5861, sealife 0.55/0.581, crab 0.5067/0.526, salamander 0.7133/0.7086, scorpion 0.7167/0.779, mammal 0.4767/0.4965, flyingfox 0.7167/0.8776, cephalopod 0.65/0.6964
- t_kind 1.0, 17 named, world right 0.6816; failing: fungus 0.5367/0.5349, slime 0.71/0.7345, spider 0.6333/0.7364, jumper 0.7067/0.7653, fish 0.6967/0.7333, shark 0.7333/0.7213, snail 0.5267/0.583, sealife 0.55/0.581, crab 0.5067/0.526, salamander 0.7133/0.7086, scorpion 0.7167/0.7818, flyingfox 0.7167/0.8776, cephalopod 0.65/0.6964
- t_kind 1.0, 16 named, world right 0.6896; failing: fungus 0.5333/0.5461, slime 0.7067/0.7465, spider 0.6333/0.7393, jumper 0.7067/0.7653, fish 0.6967/0.7385, shark 0.7333/0.7261, snail 0.5/0.5929, sealife 0.5333/0.5948, salamander 0.7133/0.7181, scorpion 0.7133/0.7897, flyingfox 0.7167/0.8776, cephalopod 0.6333/0.7011
- t_kind 1.0, 15 named, world right 0.7005; failing: fungus 0.5333/0.5556, slime 0.7033/0.7482, spider 0.6333/0.7393, jumper 0.7067/0.7653, fish 0.68/0.7418, shark 0.73/0.7252, sealife 0.4967/0.6395, salamander 0.71/0.722, scorpion 0.71/0.7889, flyingfox 0.7167/0.8776, cephalopod 0.6033/0.7043
- t_kind 1.0, 14 named, world right 0.7143; failing: fungus 0.53/0.5618, slime 0.7033/0.7536, spider 0.6333/0.7393, jumper 0.7067/0.7653, fish 0.6733/0.7509, shark 0.73/0.7399, salamander 0.71/0.7245, scorpion 0.71/0.7948, flyingfox 0.7167/0.8776, cephalopod 0.5733/0.7257
- t_kind 1.0, 13 named, world right 0.7208; failing: slime 0.6767/0.7546, spider 0.6333/0.7422, jumper 0.7067/0.7653, fish 0.6733/0.7537, shark 0.73/0.7449, salamander 0.7067/0.726, scorpion 0.71/0.8008, flyingfox 0.7167/0.8776, cephalopod 0.5733/0.7288
- t_kind 1.0, 12 named, world right 0.7336; failing: slime 0.6733/0.7566, spider 0.6333/0.7422, jumper 0.7067/0.7653, fish 0.67/0.7701, shark 0.72/0.7552, salamander 0.7067/0.7285, scorpion 0.71/0.8038, flyingfox 0.7167/0.8776
- t_kind 1.0, 11 named, world right 0.7362; failing: slime 0.6733/0.7594, jumper 0.7033/0.7673, fish 0.67/0.7701, shark 0.72/0.7552, salamander 0.7/0.7317, scorpion 0.71/0.8068, flyingfox 0.7167/0.8776
- t_kind 1.0, 10 named, world right 0.7444; failing: slime 0.6733/0.7594, jumper 0.7033/0.7673, shark 0.7033/0.7757, salamander 0.6933/0.7376, scorpion 0.71/0.813, flyingfox 0.7167/0.8776
- t_kind 1.0, 9 named, world right 0.758; failing: jumper 0.7033/0.7673, shark 0.7033/0.7757, salamander 0.6933/0.7376, scorpion 0.71/0.813, flyingfox 0.7167/0.8776
- t_kind 1.0, 8 named, world right 0.7663; failing: jumper 0.7033/0.7673, shark 0.7033/0.7757, scorpion 0.71/0.8224, flyingfox 0.7133/0.877
- t_kind 1.0, 7 named, world right 0.7721; failing: shark 0.7033/0.7757, scorpion 0.7067/0.8217, tick 0.7433/0.7908, flyingfox 0.7133/0.877
- t_kind 1.0, 6 named, world right 0.7831; failing: scorpion 0.7067/0.8249, tick 0.7433/0.7936, flyingfox 0.71/0.8802
- t_kind 1.0, 5 named, world right 0.7902; failing: tick 0.7333/0.8059, flyingfox 0.71/0.8802
- t_kind 1.0, 4 named, world right 0.7919; failing: tick 0.7333/0.8059
- t_kind 1.0, 3 named, world right 0.8025; failing: none
- t_kind 1.0, 3 named, world right 0.8025; failing: none
