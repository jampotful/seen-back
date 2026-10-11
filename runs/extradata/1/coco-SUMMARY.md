# Extra photos: kinds the wildlife records lack (COCO 2017)

Built by `tools/species/build_coco.py` on 2026-10-11 05:05 (UTC) from `http://images.cocodataset.org/annotations/annotations_trainval2017.zip` (252907541 bytes, sha256 `113a836d90195ee1f884e704da6304dfaaecff1f023f49b6ca93c4aaae470268`), seed `seen-back/coco-kinds/v1`. 10240 rows: 9000 train (from COCO's train2017 annotations), 1240 test (from val2017).

The manifest lists addresses only. Photos are downloaded when a laboratory or evaluation run needs them and are never committed or republished.

## Rules

- `person`: the largest annotation (by annotated area, crowd regions left out) is a person covering at least a fifth of the image, and no animal is annotated.
- `cat`, `dog`: the largest annotation is a cat (a dog).
- `deer`: the largest annotation is a horse, a cow or a sheep; the three are taken in turn by rank.
- `none`: at least one annotation; no person, animal or potted plant annotated; every annotation in COCO's indoor supercategories (furniture, electronic, appliance, kitchen, food, indoor).
- Each kind and split is ranked by sha256(seed|image id) and the first images are taken.

## Counts

| kind | eligible in train2017 | train rows | wanted | eligible in val2017 | test rows | wanted |
|---|---:|---:|---:|---:|---:|---:|
| person | 10354 | 2000 | 2000 | 424 | 400 | 400 |
| cat | 1595 | 1500 | 1500 | 77 | 77 | 150 |
| dog | 1587 | 1500 | 1500 | 63 | 63 | 150 |
| deer | 5122 | 1500 | 1500 | 219 | 200 | 200 |
| none | 21612 | 2500 | 2500 | 910 | 500 | 500 |

Fewer than wanted, so all there are: test cat: 150 wanted, 77 there are; test dog: 150 wanted, 63 there are.

Grazing animals among the `deer` rows: train {'horse': 500, 'cow': 500, 'sheep': 500}; test {'horse': 82, 'cow': 73, 'sheep': 45} (eligible: train {'cow': 1570, 'horse': 2397, 'sheep': 1155}; test {'cow': 73, 'sheep': 45, 'horse': 101}).

## How much of the image the largest annotation covers

| split | kind | 10th percentile | median | 90th percentile |
|---|---|---:|---:|---:|
| train | person | 0.22 | 0.31 | 0.55 |
| train | cat | 0.07 | 0.25 | 0.49 |
| train | dog | 0.03 | 0.17 | 0.43 |
| train | deer | 0.01 | 0.08 | 0.27 |
| train | none | 0.02 | 0.16 | 0.83 |
| test | person | 0.21 | 0.30 | 0.57 |
| test | cat | 0.07 | 0.26 | 0.49 |
| test | dog | 0.06 | 0.21 | 0.45 |
| test | deer | 0.01 | 0.08 | 0.26 |
| test | none | 0.03 | 0.17 | 0.85 |

## Licences

The licence of each image as COCO's annotation file gives it (the `licenses` table, identical in both files: True).

| COCO id | licence column | name in COCO's table | address | train rows | test rows |
|---:|---|---|---|---:|---:|
| 1 | CC-BY-NC-SA-2.0 | Attribution-NonCommercial-ShareAlike License | http://creativecommons.org/licenses/by-nc-sa/2.0/ | 2537 | 337 |
| 2 | CC-BY-NC-2.0 | Attribution-NonCommercial License | http://creativecommons.org/licenses/by-nc/2.0/ | 1219 | 149 |
| 3 | CC-BY-NC-ND-2.0 | Attribution-NonCommercial-NoDerivs License | http://creativecommons.org/licenses/by-nc-nd/2.0/ | 2428 | 354 |
| 4 | CC-BY-2.0 | Attribution License | http://creativecommons.org/licenses/by/2.0/ | 1504 | 227 |
| 5 | CC-BY-SA-2.0 | Attribution-ShareAlike License | http://creativecommons.org/licenses/by-sa/2.0/ | 828 | 114 |
| 6 | CC-BY-ND-2.0 | Attribution-NoDerivs License | http://creativecommons.org/licenses/by-nd/2.0/ | 463 | 57 |
| 7 | no-known-copyright-restrictions | No known copyright restrictions | http://flickr.com/commons/usage/ | 21 | 2 |
| 8 | us-government-work | United States Government Work | http://www.usa.gov/copyright.shtml | 0 | 0 |

## Checks

- ids unique: True; photo addresses unique: True; images in both splits: 0; rows whose photo is outside their split's folder: 0

## Images left out (train2017 and val2017 together)

| reason | images |
|---|---:|
| a person or an animal annotated, not the largest of the wanted kinds | 35839 |
| person largest, under a fifth of the image | 26609 |
| an outdoor or vehicle annotation (vehicle) | 6632 |
| an outdoor or vehicle annotation (outdoor) | 2593 |
| potted plant annotated | 2209 |
| an outdoor or vehicle annotation (outdoor,vehicle) | 2155 |
| person largest, an animal annotated | 2105 |
| an outdoor or vehicle annotation (accessory) | 1311 |
| no annotations | 1069 |
| an outdoor or vehicle annotation (sports) | 392 |
| an outdoor or vehicle annotation (accessory,vehicle) | 222 |
| an outdoor or vehicle annotation (sports,vehicle) | 63 |
