# The group head on world photos

Made by `tools/world/head.py` (2026-10-13T02:27:55Z), recipe `merge`, encoder `bioclip-b16`. The page is scored as it would run: away from the county's time zone the page leaves the county list out (the head alone); in it, the head and the list are combined by the rule mix.
Vectors of the new head's tuning and test photos: world fit world-fit, tune world-eval, test world-eval; alachua fit alachua-pre2025, tune alachua-2025, test alachua-2025; coco fit coco-kinds, tune coco-kinds, test coco-kinds. Today's page: encoder tinyclip-39m-16, world world-eval.wasm-int8-per-channel, alachua alachua-2025.wasm-int8-per-channel, coco_tune coco-kinds, coco_test coco-kinds.wasm-int8-per-channel.

Fitting: power 0.0, with the Alachua training photos; options {"with_alachua": "yes", "powers": "0", "alachua_weight": 3.0, "coco_weight": 10.0, "calibrate": true, "groups": "merge", "t_kinds": "0.5,1,2", "w_kinds": "0.5,0.7,0.9,1.0", "settle_on": "old", "other_view": null}. Groups named (12): slime, spider, jumper, fish, shark, salamander, scorpion, tick, primate, whale, bat, flyingfox. In `other` (7): fungus, snail, sealife, crab, worm, mammal, cephalopod.
Bias offsets calibrated on the world tuning photos: fungus -0.75, jumper +0.5, fish -0.25, crab +0.25, salamander +0.5, worm +0.25, scorpion +1.25, tick +1.25, mammal +0.25, primate +0.25, whale -0.25, bat +0.75, flyingfox +1.
County list rows fitted for this encoder: discriminant, shrinkage 0.3, prior weight 0.3, scale 0.060318 (alpha_prior 0.6); tuning top-1 0.7629.
Settings for the county: t_kind 2.0, w_kind 0.7, kind_at 0.99 (levels {'world': 0.99, 'alachua': 0.67, 'coco': 0.81}).

| Pass mark | Measured | Passes |
|---|---|---|
| Old groups right, world test photos, the head alone (away from the county): 95% interval of the paired difference above −2 points | today 0.6838, new 0.7793, difference 0.0955 (0.0817 to 0.11), 4200 photos | yes |
| Old groups right, Alachua test photos, head and list combined: 95% interval of the paired difference above −2 points | today 0.9018, new 0.9197, difference 0.0178 (0.008 to 0.0271), 3871 photos | yes |
| Every group named found (named and right when called, 75% or more each, world test photos, head alone) | 12 of 12 pass | yes |
| People, pets and rooms within 1 point of today (COCO test) | today 0.9467; new with the list 0.8564, alone 0.8574; a new group named 38 times in 2480 answers | no |
| `other` given a view under 10% (world test photos, head alone) | today 0.3004, new 0.1325, of 2400 photos | no |
| Head under 50 KB | 36864 bytes | yes |

For the record, the world test photos with the county list combined (as in the county's time zone): old groups today 0.6838, new 0.7817, difference 0.0979 (0.084 to 0.1121).

| Group named | test photos | named | called | right when called | passes |
|---|---:|---:|---:|---:|---|
| slime | 300 | 0.83 | 290 | 0.8586 | yes |
| spider | 300 | 0.8267 | 290 | 0.8552 | yes |
| jumper | 300 | 0.86 | 283 | 0.9117 | yes |
| fish | 300 | 0.8033 | 310 | 0.7774 | yes |
| shark | 300 | 0.83 | 287 | 0.8676 | yes |
| salamander | 300 | 0.81 | 291 | 0.8351 | yes |
| scorpion | 300 | 0.8567 | 302 | 0.851 | yes |
| tick | 300 | 0.8667 | 298 | 0.8725 | yes |
| primate | 300 | 0.8733 | 300 | 0.8733 | yes |
| whale | 300 | 0.87 | 307 | 0.8502 | yes |
| bat | 300 | 0.8367 | 288 | 0.8715 | yes |
| flyingfox | 300 | 0.7833 | 293 | 0.802 | yes |

`other` on the world test photos, by what the photo shows:

| Truth | photos | given a view today | given a view, new | the views given, new |
|---|---:|---:|---:|---|
| other | 300 | 0.4533 | 0.2967 | plant 50, insect 22, bird 4, bee 4, wader 3 |
| fungus | 300 | 0.38 | 0.2 | plant 36, insect 17, bee 5, rabbit 1, bird 1 |
| snail | 300 | 0.1467 | 0.02 | plant 2, insect 2, reptile 1, dog 1 |
| sealife | 300 | 0.09 | 0.0167 | plant 2, insect 1, dog 1, bird 1 |
| crab | 300 | 0.2767 | 0.0967 | insect 16, plant 8, reptile 3, frog 1, bee 1 |
| worm | 300 | 0.3067 | 0.1 | insect 19, plant 6, reptile 4, rabbit 1 |
| mammal | 300 | 0.6433 | 0.3133 | squirrel 20, dog 14, cat 13, deer 10, reptile 8 |
| cephalopod | 300 | 0.1067 | 0.0167 | plant 2, deer 1, insect 1, bird 1 |

The creatures with no group of their own given a view, by order: ? as insect 7; Nostocales as plant 5; Martellivirales as plant 4; Sarcoptiformes as insect 3; Chroococcales as plant 3; Acholeplasmatales as plant 3; Trombidiformes as plant 3; Gonyaulacales as plant 3; Rhizobiales as bee 3; Thraustochytriales as plant 2; Peronosporales as plant 2; Geplafuvirales as plant 2; Picornavirales as insect 2; Rhizobiales as plant 2; Pseudomonadales as plant 2; Plasmodiophorida as plant 2; Sarcoptiformes as plant 2; Patatavirales as plant 2; Trombidiformes as insect 1; Articulavirales as wader 1.

World test photos, every label: right 0.8033 (today 0.4456); asserted 0.616, right when asserted 0.9441.

Alachua test photos, every label: right 0.9173 (today 0.8606); asserted 0.6373, right when asserted 0.9955.

By continent (new, today): AF 0.8214, 0.4349 of 1674; AN 0.85, 0.6136 of 220; AS 0.7994, 0.4251 of 1790; EU 0.789, 0.4333 of 1611; NA 0.8062, 0.4445 of 1739; OC 0.7874, 0.4485 of 1543; SA 0.809, 0.467 of 1623.

Commonest confusions: other as plant 113; other as insect 80; plant as other 47; wader as bird 47; other as fish 43; bee as insect 38; squirrel as other 38; slime as other 37; cat as dog 36; bird as wader 32; other as slime 31; hawk as bird 31; dog as cat 30; fish as other 28; salamander as reptile 26.

On the tuning photos, for the head that ships: old groups right on world photos 0.7979 (today 0.6662), on Alachua photos 0.9151 (today 0.8941); `other` given a view 0.1379; COCO 0.8743 with the list, 0.8727 alone (today 0.9538).

Named after the fold but failing on the test photos, so put back in `other` (first reading, named / right when called): cephalopod 0.73 / 0.7821. The tables above are the second reading, for the head that ships. First reading's marks: old_groups_world yes, old_groups_alachua yes, new_groups no, coco no, other no, size yes; `other` given a view 0.1495; old groups world [0.0955, 0.0817, 0.11, 4200], Alachua [0.0178, 0.008, 0.0271, 3871].

The fold, on the tuning photos (t_kind, named, failing):
- t_kind 1.0, 19 named, world right 0.7738; failing: fungus 0.5667/0.7456, snail 0.7033/0.7128, sealife 0.6967/0.699, crab 0.6767/0.6767, worm 0.5967/0.6486, mammal 0.5833/0.5853
- t_kind 1.0, 18 named, world right 0.7763; failing: snail 0.7033/0.7177, sealife 0.69/0.697, crab 0.6767/0.6767, worm 0.5967/0.6486, mammal 0.5833/0.5853
- t_kind 1.0, 17 named, world right 0.7762; failing: snail 0.7033/0.7177, sealife 0.69/0.697, crab 0.6767/0.6767, worm 0.5967/0.6486
- t_kind 1.0, 16 named, world right 0.7789; failing: snail 0.7033/0.7201, sealife 0.69/0.697, crab 0.6667/0.6849
- t_kind 1.0, 15 named, world right 0.7838; failing: snail 0.6767/0.7276, sealife 0.6833/0.7168
- t_kind 1.0, 14 named, world right 0.7925; failing: sealife 0.6667/0.7273
- t_kind 1.0, 13 named, world right 0.804; failing: none
- t_kind 2.0, 13 named, world right 0.8016; failing: none
- t_kind 2.0, 12 named, world right 0.8087; failing: none
