# The group head on world photos

Made by `tools/world/head.py` (2026-10-12T20:46:51Z).

Chosen on the tuning photos: power 0.5, with the Alachua training photos, t_kind 0.5, w_kind 0.9, kind_at 0.55 (levels {'world': 0.55, 'alachua': 0.39, 'coco': 0.2}). Score 0.8352 (world 0.7001, Alachua 0.8613, COCO 0.9442).

| Pass mark | Measured | Passes |
|---|---|---|
| Old groups right, world test photos: 95% interval of the paired difference above −2 points | today 0.6838, new 0.74, difference 0.0562 (0.0452 to 0.0671), 4200 photos | yes |
| Old groups right, alachua test photos: 95% interval of the paired difference above −2 points | today 0.9018, new 0.8732, difference -0.0287 (-0.0364 to -0.0212), 3871 photos | no |
| Every new group found (named and right when called, 75% or more each) | 5 of 19 groups pass | no |
| People, pets and rooms within 1 point of today (COCO test) | today 0.9467, new 0.9513; a new group named for 8 of 1240 | yes |
| `other` given a view under 10% | today 0.4533, new 0.2533, of 300 photos | no |
| Head under 50 KB | 36864 bytes | yes |

| New group | test photos | named | called | right when called | passes |
|---|---:|---:|---:|---:|---|
| fungus | 300 | 0.52 | 247 | 0.6316 | no |
| slime | 300 | 0.7733 | 313 | 0.7412 | no |
| spider | 300 | 0.7067 | 313 | 0.6773 | no |
| jumper | 300 | 0.7033 | 277 | 0.7617 | no |
| fish | 300 | 0.69 | 309 | 0.6699 | no |
| shark | 300 | 0.79 | 318 | 0.7453 | no |
| snail | 300 | 0.5233 | 283 | 0.5548 | no |
| sealife | 300 | 0.5867 | 304 | 0.5789 | no |
| crab | 300 | 0.4633 | 265 | 0.5245 | no |
| salamander | 300 | 0.5767 | 228 | 0.7588 | no |
| worm | 300 | 0.5567 | 275 | 0.6073 | no |
| scorpion | 300 | 0.6867 | 255 | 0.8078 | no |
| tick | 300 | 0.7733 | 294 | 0.7891 | yes |
| mammal | 300 | 0.4367 | 263 | 0.4981 | no |
| primate | 300 | 0.8733 | 315 | 0.8317 | yes |
| whale | 300 | 0.8233 | 300 | 0.8233 | yes |
| bat | 300 | 0.8267 | 291 | 0.8522 | yes |
| flyingfox | 300 | 0.7667 | 284 | 0.8099 | yes |
| cephalopod | 300 | 0.68 | 318 | 0.6415 | no |

World test photos, every group: right 0.6945 as the page gives it, 0.7004 by the head alone; asserted 0.3653, right when asserted 0.953.

By continent: AF 0.7443 of 1674; AN 0.7136 of 220; AS 0.6972 of 1790; EU 0.6623 of 1611; NA 0.6832 of 1739; OC 0.6792 of 1543; SA 0.6962 of 1623.

Commonest confusions: salamander as reptile 59; plant as other 51; bee as insect 50; mammal as squirrel 46; wader as bird 46; fungus as slime 43; bird as wader 40; other as plant 39; squirrel as mammal 39; snail as sealife 38; dog as cat 37; fungus as plant 35; cat as dog 34; scorpion as spider 34; jumper as spider 33.
