# The group head on world photos

Made by `tools/world/head.py` (2026-10-13T13:52:59Z), recipe `merge-county`, encoder `tinyclip-39m-16`. The page is scored as it would run: away from the county's time zone the page leaves the county list out (the head alone); in it, the head and the list are combined by the rule mix.
Vectors of the new head's tuning and test photos: world fit world-fit, tune world-eval.wasm-int8-per-channel, test world-eval.wasm-int8-per-channel; alachua fit alachua-pre2025, tune alachua-2025.wasm-int8-per-channel, test alachua-2025.wasm-int8-per-channel; coco fit coco-kinds, tune coco-kinds, test coco-kinds.wasm-int8-per-channel. Today's page: encoder tinyclip-39m-16, world world-eval.wasm-int8-per-channel, alachua alachua-2025.wasm-int8-per-channel, coco_tune coco-kinds, coco_test coco-kinds.wasm-int8-per-channel.

Fitting: power 0.0, with the Alachua training photos; options {"with_alachua": "yes", "powers": "0", "alachua_weight": 3.0, "coco_weight": 10.0, "calibrate": true, "groups": "merge", "t_kinds": "0.5,1,2", "w_kinds": "0.5,0.7,0.9,1.0", "settle_on": "old", "other_view": 0.09, "county_lambda": 0.5}. Groups named (3): primate, whale, bat. In `other` (16): fungus, slime, spider, jumper, fish, shark, snail, sealife, crab, salamander, worm, scorpion, tick, mammal, flyingfox, cephalopod.
Bias offsets calibrated on the world tuning photos: fungus +0.25, slime +0.25, jumper +0.25, fish -0.25, crab +0.25, salamander +0.75, worm +0.25, scorpion +0.75, tick +0.75, primate +0.25.
Settings for the county: t_kind 1.0, w_kind 0.7, kind_at 0.87 (levels {'world': 0.87, 'alachua': 0.67, 'coco': 0.2}).

| Pass mark | Measured | Passes |
|---|---|---|
| Old groups right, world test photos, the head alone (away from the county): 95% interval of the paired difference above −2 points | today 0.6838, new 0.6948, difference 0.011 (-0.0 to 0.0217), 4200 photos | yes |
| Old groups right, Alachua test photos, head and list combined: 95% interval of the paired difference above −2 points | today 0.9018, new 0.8938, difference -0.008 (-0.0142 to -0.0023), 3871 photos | yes |
| Every group named found (named and right when called, 75% or more each, world test photos, head alone) | 3 of 3 pass | yes |
| People, pets and rooms within 1 point of today (COCO test) | today 0.9467; new with the list 0.9597, alone 0.9567; a new group named 0 times in 2480 answers | yes |
| `other` given a view under 10% (world test photos, head alone) | today 0.32, new 0.0902, of 5100 photos | yes |
| Head under 50 KB | 36864 bytes | yes |

For the record, the world test photos with the county list combined (as in the county's time zone): old groups today 0.6838, new 0.7074, difference 0.0236 (0.015 to 0.0329).

| Group named | test photos | named | called | right when called | passes |
|---|---:|---:|---:|---:|---|
| primate | 300 | 0.8833 | 316 | 0.8386 | yes |
| whale | 300 | 0.7867 | 281 | 0.8399 | yes |
| bat | 300 | 0.8033 | 279 | 0.8638 | yes |

`other` on the world test photos, by what the photo shows:

| Truth | photos | given a view today | given a view, new | the views given, new |
|---|---:|---:|---:|---|
| other | 300 | 0.4533 | 0.1433 | plant 23, insect 10, bird 3, cat 2, wader 1 |
| fungus | 300 | 0.38 | 0.1533 | plant 29, insect 16, bee 1 |
| slime | 300 | 0.1967 | 0.0267 | plant 4, insect 4 |
| spider | 300 | 0.2067 | 0.1 | insect 20, bee 5, reptile 2, plant 2, rabbit 1 |
| jumper | 300 | 0.3133 | 0.12 | insect 28, bee 6, frog 1, rabbit 1 |
| fish | 300 | 0.13 | 0.05 | reptile 6, bird 3, insect 2, alligator 2, plant 1 |
| shark | 300 | 0.1333 | 0.02 | bird 3, insect 2, plant 1 |
| snail | 300 | 0.1467 | 0.0333 | insect 8, plant 1, frog 1 |
| sealife | 300 | 0.09 | 0.02 | plant 5, reptile 1 |
| crab | 300 | 0.2767 | 0.05 | insect 12, alligator 1, frog 1, plant 1 |
| salamander | 300 | 0.76 | 0.15 | reptile 34, frog 7, alligator 1, plant 1, bee 1 |
| worm | 300 | 0.3067 | 0.0667 | insect 14, reptile 3, plant 2, bird 1 |
| scorpion | 300 | 0.4267 | 0.08 | insect 21, plant 2, bee 1 |
| tick | 300 | 0.3433 | 0.0667 | insect 15, reptile 1, plant 1, frog 1, deer 1 |
| mammal | 300 | 0.6433 | 0.3733 | squirrel 31, cat 21, deer 13, rabbit 11, reptile 8 |
| flyingfox | 300 | 0.5267 | 0.0767 | bird 9, insect 5, hawk 5, plant 2, deer 1 |
| cephalopod | 300 | 0.1067 | 0.0033 | insect 1 |

The creatures with no group of their own given a view, by order: Sarcoptiformes as plant 4; Picornavirales as insect 3; ? as insect 3; Trombidiformes as plant 3; Acholeplasmatales as plant 2; Pseudomonadales as plant 2; Mesostigmata as insect 2; Articulavirales as wader 1; Peronosporales as plant 1; Mononegavirales as dog 1; Martellivirales as plant 1; Mesostigmata as plant 1; Cirlivirales as bird 1; Mononegavirales as plant 1; Mycoplasmatales as bird 1; Tolivirales as plant 1; Chitovirales as rabbit 1; Herpesvirales as alligator 1; Mulpavirales as plant 1; Plasmodiophorida as plant 1.

World test photos, every label: right 0.8051 (today 0.621); asserted 0.5926, right when asserted 0.956.

Alachua test photos, every label: right 0.8846 (today 0.8919); asserted 0.6667, right when asserted 0.9838.

By continent (new, today): AF 0.8345, 0.626 of 1674; AN 0.7818, 0.6591 of 220; AS 0.7955, 0.6006 of 1790; EU 0.7952, 0.6176 of 1611; NA 0.7999, 0.6078 of 1739; OC 0.7965, 0.6442 of 1543; SA 0.8121, 0.6285 of 1623.

Commonest confusions: other as insect 162; plant as other 123; insect as other 88; bee as insect 81; other as plant 80; wader as bird 74; other as reptile 55; squirrel as other 54; frog as other 51; reptile as other 50; whale as other 50; dog as other 43; bat as other 42; cat as other 37; hawk as bird 35.

On the tuning photos, for the head that ships: old groups right on world photos 0.6895 (today 0.6662), on Alachua photos 0.8965 (today 0.8941); `other` given a view 0.09; COCO 0.9615 with the list, 0.9568 alone (today 0.9538).

The fold, on the tuning photos (t_kind, named, failing):
- t_kind 1.0, 19 named, world right 0.6788; failing: fungus 0.5267/0.5215, slime 0.71/0.727, spider 0.63/0.7383, jumper 0.7/0.7692, fish 0.69/0.7213, shark 0.7267/0.7315, snail 0.54/0.5848, sealife 0.5567/0.5839, crab 0.5133/0.5168, salamander 0.7167/0.7049, worm 0.4733/0.5358, scorpion 0.7133/0.7839, mammal 0.4767/0.5018, flyingfox 0.7233/0.8645, cephalopod 0.6467/0.7029
- t_kind 1.0, 18 named, world right 0.6816; failing: fungus 0.5267/0.5249, slime 0.71/0.732, spider 0.63/0.7383, jumper 0.7/0.7692, fish 0.69/0.7238, shark 0.7267/0.7315, snail 0.53/0.5867, sealife 0.5567/0.588, crab 0.5067/0.5278, salamander 0.7167/0.7096, scorpion 0.7133/0.7868, mammal 0.4767/0.5018, flyingfox 0.7233/0.8645, cephalopod 0.6467/0.7029
- t_kind 1.0, 17 named, world right 0.6815; failing: fungus 0.5267/0.5267, slime 0.7067/0.731, spider 0.63/0.7383, jumper 0.7/0.7692, fish 0.69/0.7238, shark 0.7267/0.7315, snail 0.5267/0.5852, sealife 0.5567/0.588, crab 0.5067/0.5296, salamander 0.7167/0.7096, scorpion 0.7133/0.7868, flyingfox 0.7233/0.8645, cephalopod 0.6467/0.7029
- t_kind 1.0, 16 named, world right 0.689; failing: fungus 0.5267/0.5411, slime 0.7033/0.7352, spider 0.63/0.7412, jumper 0.7/0.7692, fish 0.6867/0.7254, shark 0.7267/0.7365, snail 0.49/0.6025, sealife 0.5333/0.6015, salamander 0.7167/0.7167, scorpion 0.71/0.7948, flyingfox 0.7233/0.8645, cephalopod 0.63/0.7105
- t_kind 1.0, 15 named, world right 0.6996; failing: fungus 0.5233/0.5509, slime 0.7033/0.7352, spider 0.63/0.7412, jumper 0.7/0.7692, fish 0.6767/0.7302, shark 0.7233/0.7356, sealife 0.49/0.6391, salamander 0.7167/0.7239, scorpion 0.7067/0.797, flyingfox 0.7233/0.8645, cephalopod 0.6067/0.7165
- t_kind 1.0, 14 named, world right 0.7145; failing: fungus 0.52/0.5612, slime 0.7/0.7368, spider 0.63/0.7412, jumper 0.7/0.7692, fish 0.6733/0.7399, shark 0.7233/0.7483, salamander 0.7133/0.7254, scorpion 0.7067/0.797, flyingfox 0.7233/0.8645, cephalopod 0.58/0.7532
- t_kind 1.0, 13 named, world right 0.7218; failing: slime 0.6733/0.7454, spider 0.63/0.7441, jumper 0.7/0.7692, fish 0.6733/0.7454, shark 0.7233/0.7535, salamander 0.7133/0.7279, scorpion 0.7067/0.8061, flyingfox 0.7233/0.8645, cephalopod 0.5767/0.7555
- t_kind 1.0, 12 named, world right 0.734; failing: slime 0.6733/0.7454, spider 0.63/0.7441, jumper 0.7/0.7692, fish 0.6667/0.7576, shark 0.7067/0.7653, salamander 0.7133/0.7304, scorpion 0.7067/0.8061, flyingfox 0.7233/0.8645
- t_kind 1.0, 11 named, world right 0.736; failing: slime 0.67/0.7472, jumper 0.6967/0.7712, fish 0.6667/0.7576, shark 0.7067/0.7653, salamander 0.7067/0.731, scorpion 0.7067/0.8123, flyingfox 0.7233/0.8645
- t_kind 1.0, 10 named, world right 0.7438; failing: slime 0.67/0.7472, jumper 0.6967/0.7712, shark 0.6933/0.7761, salamander 0.6933/0.7402, scorpion 0.7067/0.8185, flyingfox 0.7233/0.868
- t_kind 1.0, 9 named, world right 0.7578; failing: jumper 0.6967/0.7712, shark 0.6933/0.7761, salamander 0.6933/0.7402, scorpion 0.7067/0.8185, flyingfox 0.7233/0.868
- t_kind 1.0, 8 named, world right 0.7689; failing: jumper 0.6967/0.7712, salamander 0.6933/0.7455, scorpion 0.7067/0.8217, flyingfox 0.72/0.8675
- t_kind 1.0, 7 named, world right 0.7766; failing: jumper 0.6967/0.7712, scorpion 0.7033/0.8242, flyingfox 0.7167/0.8669
- t_kind 1.0, 6 named, world right 0.7827; failing: scorpion 0.7033/0.8242, tick 0.7367/0.8007, flyingfox 0.7167/0.8669
- t_kind 1.0, 5 named, world right 0.7905; failing: tick 0.7233/0.8127, flyingfox 0.7167/0.8669
- t_kind 1.0, 4 named, world right 0.7923; failing: tick 0.7233/0.8127
- t_kind 1.0, 3 named, world right 0.8025; failing: none
- t_kind 1.0, 3 named, world right 0.8025; failing: none
- t_kind 1.0, 3 named, world right 0.8047; failing: none
- t_kind 1.0, 3 named, world right 0.8047; failing: none
