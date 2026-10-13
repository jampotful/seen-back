# The group head on world photos

Made by `tools/world/head.py` (2026-10-13T02:27:44Z), recipe `merge-other`, encoder `bioclip-b16`. The page is scored as it would run: away from the county's time zone the page leaves the county list out (the head alone); in it, the head and the list are combined by the rule mix.
Vectors of the new head's tuning and test photos: world fit world-fit, tune world-eval, test world-eval; alachua fit alachua-pre2025, tune alachua-2025, test alachua-2025; coco fit coco-kinds, tune coco-kinds, test coco-kinds. Today's page: encoder tinyclip-39m-16, world world-eval.wasm-int8-per-channel, alachua alachua-2025.wasm-int8-per-channel, coco_tune coco-kinds, coco_test coco-kinds.wasm-int8-per-channel.

Fitting: power 0.0, with the Alachua training photos; options {"with_alachua": "yes", "powers": "0", "alachua_weight": 3.0, "coco_weight": 10.0, "calibrate": true, "groups": "merge", "t_kinds": "0.5,1,2", "w_kinds": "0.5,0.7,0.9,1.0", "settle_on": "old", "other_view": 0.09}. Groups named (11): spider, jumper, fish, shark, salamander, scorpion, tick, primate, whale, bat, flyingfox. In `other` (8): fungus, slime, snail, sealife, crab, worm, mammal, cephalopod.
Bias offsets calibrated on the world tuning photos: fungus -0.75, jumper +0.5, fish -0.25, shark -0.25, crab +0.25, salamander +0.75, worm +0.5, scorpion +1, tick +1.25, mammal +0.25, primate +0.25, whale -0.5, bat +1, flyingfox +1.
County list rows fitted for this encoder: discriminant, shrinkage 0.3, prior weight 0.3, scale 0.060318 (alpha_prior 0.6); tuning top-1 0.7629.
Settings for the county: t_kind 2.0, w_kind 0.7, kind_at 0.99 (levels {'world': 0.99, 'alachua': 0.68, 'coco': 0.78}).

| Pass mark | Measured | Passes |
|---|---|---|
| Old groups right, world test photos, the head alone (away from the county): 95% interval of the paired difference above −2 points | today 0.6838, new 0.7431, difference 0.0593 (0.0452 to 0.0738), 4200 photos | yes |
| Old groups right, Alachua test photos, head and list combined: 95% interval of the paired difference above −2 points | today 0.9018, new 0.9042, difference 0.0023 (-0.0078 to 0.0121), 3871 photos | yes |
| Every group named found (named and right when called, 75% or more each, world test photos, head alone) | 11 of 11 pass | yes |
| People, pets and rooms within 1 point of today (COCO test) | today 0.9467; new with the list 0.8448, alone 0.8412; a new group named 27 times in 2480 answers | no |
| `other` given a view under 10% (world test photos, head alone) | today 0.2889, new 0.0663, of 2700 photos | yes |
| Head under 50 KB | 36864 bytes | yes |

For the record, the world test photos with the county list combined (as in the county's time zone): old groups today 0.6838, new 0.755, difference 0.0712 (0.0576 to 0.085).

| Group named | test photos | named | called | right when called | passes |
|---|---:|---:|---:|---:|---|
| spider | 300 | 0.7967 | 269 | 0.8885 | yes |
| jumper | 300 | 0.86 | 283 | 0.9117 | yes |
| fish | 300 | 0.7733 | 290 | 0.8 | yes |
| shark | 300 | 0.8033 | 268 | 0.8993 | yes |
| salamander | 300 | 0.79 | 274 | 0.865 | yes |
| scorpion | 300 | 0.84 | 283 | 0.8905 | yes |
| tick | 300 | 0.84 | 275 | 0.9164 | yes |
| primate | 300 | 0.8733 | 296 | 0.8851 | yes |
| whale | 300 | 0.8533 | 286 | 0.8951 | yes |
| bat | 300 | 0.8367 | 289 | 0.8685 | yes |
| flyingfox | 300 | 0.76 | 279 | 0.8172 | yes |

`other` on the world test photos, by what the photo shows:

| Truth | photos | given a view today | given a view, new | the views given, new |
|---|---:|---:|---:|---|
| other | 300 | 0.4533 | 0.1 | plant 13, insect 8, bird 3, cat 2, wader 1 |
| fungus | 300 | 0.38 | 0.0833 | plant 18, insect 5, bee 2 |
| slime | 300 | 0.1967 | 0.0167 | insect 2, plant 1, dog 1, bee 1 |
| snail | 300 | 0.1467 | 0.0067 | insect 1, plant 1 |
| sealife | 300 | 0.09 | 0.01 | insect 1, bird 1, plant 1 |
| crab | 300 | 0.2767 | 0.05 | insect 10, plant 2, reptile 2, frog 1 |
| worm | 300 | 0.3067 | 0.0433 | insect 10, reptile 3 |
| mammal | 300 | 0.6433 | 0.2833 | squirrel 17, dog 13, cat 12, deer 10, rabbit 9 |
| cephalopod | 300 | 0.1067 | 0.0033 | insect 1 |

The creatures with no group of their own given a view, by order: ? as insect 5; Nostocales as plant 2; Acholeplasmatales as plant 2; Articulavirales as wader 1; Astrorhizida as plant 1; Mononegavirales as dog 1; Martellivirales as plant 1; Noctilucales as insect 1; Cirlivirales as bird 1; Mononegavirales as plant 1; Mycoplasmatales as bird 1; Rhizobiales as plant 1; Chitovirales as rabbit 1; Herpesvirales as alligator 1; Mulpavirales as plant 1; Plasmodiophorida as plant 1; Mesostigmata as insect 1; Picornavirales as cat 1; Sarcoptiformes as plant 1; Herpesvirales as cat 1.

World test photos, every label: right 0.8092 (today 0.4692); asserted 0.6321, right when asserted 0.9411.

Alachua test photos, every label: right 0.9031 (today 0.8611); asserted 0.5847, right when asserted 0.9971.

By continent (new, today): AF 0.822, 0.457 of 1674; AN 0.8, 0.6136 of 220; AS 0.8, 0.4469 of 1790; EU 0.7995, 0.4575 of 1611; NA 0.8143, 0.4704 of 1739; OC 0.7965, 0.4738 of 1543; SA 0.8238, 0.4929 of 1623.

Commonest confusions: plant as other 122; insect as other 57; squirrel as other 54; wader as bird 46; cat as other 45; fish as other 45; other as insect 40; other as plant 39; other as fish 37; salamander as other 36; bee as other 35; dog as cat 35; shark as other 31; bee as insect 30; dog as other 30.

On the tuning photos, for the head that ships: old groups right on world photos 0.7633 (today 0.6662), on Alachua photos 0.8995 (today 0.8941); `other` given a view 0.073; COCO 0.8623 with the list, 0.8591 alone (today 0.9538).

Named after the fold but failing on the test photos, so put back in `other` (first reading, named / right when called): cephalopod 0.6933 / 0.8221. The tables above are the second reading, for the head that ships. First reading's marks: old_groups_world yes, old_groups_alachua yes, new_groups no, coco no, other yes, size yes; `other` given a view 0.0742; old groups world [0.0595, 0.0457, 0.074, 4200], Alachua [0.0023, -0.0078, 0.0121, 3871].

The fold, on the tuning photos (t_kind, named, failing):
- t_kind 1.0, 19 named, world right 0.7736; failing: fungus 0.57/0.76, snail 0.6933/0.7099, sealife 0.6967/0.7061, crab 0.6667/0.6849, worm 0.6167/0.6126, mammal 0.5733/0.5772
- t_kind 1.0, 18 named, world right 0.7762; failing: snail 0.6933/0.7148, sealife 0.69/0.7041, crab 0.6633/0.6862, worm 0.6167/0.6146, mammal 0.5733/0.5772
- t_kind 1.0, 17 named, world right 0.7765; failing: snail 0.6933/0.7148, sealife 0.69/0.7041, crab 0.6633/0.6862, worm 0.6167/0.6146
- t_kind 1.0, 16 named, world right 0.7793; failing: snail 0.6867/0.7153, sealife 0.69/0.7089, crab 0.66/0.6972
- t_kind 1.0, 15 named, world right 0.7839; failing: snail 0.6667/0.7246, sealife 0.68/0.726
- t_kind 1.0, 14 named, world right 0.7925; failing: sealife 0.6567/0.7406
- t_kind 1.0, 13 named, world right 0.8039; failing: none
- t_kind 2.0, 13 named, world right 0.8026; failing: none
- t_kind 2.0, 13 named, world right 0.796; failing: slime 0.72/0.8606
- t_kind 2.0, 12 named, world right 0.8066; failing: none
- t_kind 2.0, 12 named, world right 0.8066; failing: none
- t_kind 2.0, 12 named, world right 0.8066; failing: none
- t_kind 2.0, 11 named, world right 0.8146; failing: none
