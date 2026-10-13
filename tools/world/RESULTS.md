# The group head: results of 13 October 2026

For `docs/tracks/head.md` (track A1, which lives on `main`): the merge recipe on TinyCLIP 39M/16 and on BioCLIP B/16, against every pass mark of `docs/COVERAGE.md`, and the two encoders' speed in Chromium. The commit before this one says it adds this to `docs/tracks/head.md`; that file is not on this branch, so the results are here.

`tools/world/head.py --recipe merge` is the merge trial ported; `--recipe merge-other` adds `other`'s bias raised until at most 9% of the world tuning photos in `other` get a view (chosen on tuning photos, before any test photo was read: `EXPERIMENTS.md`). Each run read the test photos once; a group that failed there was merged into `other`, the settings chosen again on the tuning photos, and the test photos read a second time, both readings kept. Results are `runs/worldhead/4` to `7` on `ci`, from the settings in `ci/world/runs/`; the slots are `pub/heads-world-m1`, `-m2`, `-b1` and `-b2`.

| Pass mark | TinyCLIP, merge (m1) | TinyCLIP, merge-other (m2) | B/16, merge (b1) | B/16, merge-other (b2) |
|---|---|---|---|---|
| Groups named: 75% named and 75% right when called | 3 of 3 (primate, whale, bat) | 3 of 3 | 12 of 12, second reading (cephalopod 0.73 / 0.78 on the first) | 11 of 11, second reading (cephalopod 0.69 / 0.82) |
| Old kinds, world photos, head alone: paired difference, points | +2.36 (+1.24 to +3.48), yes | +1.29 (+0.17 to +2.40), yes | +9.55 (+8.17 to +11.00), yes | +5.93 (+4.52 to +7.38), yes |
| Old kinds, Alachua photos, head and list | −1.63 (−2.22 to −1.06), no | −1.89 (−2.51 to −1.29), no | +1.78 (+0.80 to +2.71), yes | +0.23 (−0.78 to +1.21), yes |
| COCO within 1 point of today's 0.9467, with the list / alone | 0.9553 / 0.9550, yes | 0.9553 / 0.9541, yes | 0.8564 / 0.8574, no | 0.8448 / 0.8412, no |
| `other` given a view, under 10% | 10.49%, no | 9.00%, yes | 13.25%, no | 6.63%, yes |
| Head file under 50 KB | 36,864 bytes, yes | yes | yes | yes |
| Time a photo within 5% of today | the same encoder and 9,728 more multiply-adds, yes | yes | 1.98 times, no | no |

- B/16's tuning and test photos are scored on the original model's vectors: the laboratory made no WASM vectors for it (`tools/lab/lab.py pixels` reproduces only transformers' image processors, and lab runs 43 to 45 stopped there). TinyCLIP's are the phone runtime's. B/16's county list rows were fitted by head.py as the shipped ones were (discriminant, shrinkage 0.3, chosen on the Alachua tuning photos, top-1 there 0.763).
- B/16's COCO loss is in its vectors: a logistic head fitted on the COCO fitting photos alone gets 0.897 of the five kinds right on the COCO tuning photos (balanced; dogs 0.81), against 0.969 for TinyCLIP's vectors.
- Settings: TinyCLIP t_kind 1.0, w_kind 0.7, kind_at 0.86 and 0.87; B/16 t_kind 2.0, w_kind 0.7, kind_at 0.99. The world photos set kind_at, so in the county the page would assert a kind for 59% to 67% of photos, against 82% today. `other`'s bias rose 2.25 (m2) and 4.0 (b2).
- On the tuning photos TinyCLIP's Alachua difference was −0.47 (m1) and −0.65 (m2) points; on the test photos −1.63 and −1.89.

Speed (`tools/world/speed.mjs`, `runs/worldspeed/1`): headless Chromium 141, onnxruntime-web 1.30.0 (`vendor/ort`) in a worker, the laboratory's int8-per-channel files, a cross-origin isolated page, a build machine with 4 cores (AMD EPYC 9V74); the median of 90 photos in three rounds.

| Encoder | file | one thread | four threads |
|---|---:|---:|---:|
| TinyCLIP 39M/16 | 40,978,137 bytes | 296 ms | 153 ms |
| BioCLIP B/16 | 89,802,361 bytes | 587 ms | 305 ms |

The page runs one thread, since four need cross-origin isolation, which the static host does not give.

TinyCLIP's original-model vectors give nearly the same tuning numbers as its WASM vectors (`--recipe merge-other --vectors torch --tune-only`: world old kinds 0.691 against 0.6855, Alachua 0.8846 against 0.8846, `other` 0.0898 against 0.0890), so B/16's figures on original-model vectors are probably close to what its phone runtime would give, if its int8 file loses as little.

## What the results say

No head passes every mark, so nothing was prepared on `agent/head-ship`. B/16 finds four times as many groups and gains on creatures everywhere, but loses about 10 points on people, pets and empty rooms, a loss that sits in its vectors, and takes twice as long a photo. TinyCLIP `merge-other` fails only the county's old kinds (−1.89, interval to −2.51). A county bias (`EXPERIMENTS.md`, the last section) wins back about 1.3 points on the tuning photos at no cost to COCO; it wants a second kinds bias in the page, used with the list, and Alachua photos that no recipe has yet been read on.
