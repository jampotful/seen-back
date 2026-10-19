# Photos with nothing alive: the pocket head's answers, the rule build 35 did not ship, and the rule build 39 ships

Build 39 ships a rule measured on real photographs: see "Real photographs" below. The sections before it are build 35's work on drawn pictures, kept as they were.

Burst 12, item 2, 18 October 2026. Scripts: `tools/world/nonlife.py` (the measurement and the rules) and `tools/world/nonlife_make.py` (the photos made for it). Full output: `tools/world/nonlife-report.json`.

## What was measured

The page as it runs on build 32 (the slot `models/pocket`, `merge-county`, `kind_at` 0.87), through head.py's vectorized copy of the rule, which agrees with `tools/fusion/fuse.py` on every photo checked (240 tuning and 240 test cases, 0 differ). The harm counted is an asserted living kind for a photo with nothing alive in it. Since build 22 the pocket slot names no species (`name_at` is 2), so the harm today is a kind: the page calls the subject "this creature" (kind `other`) or shows a creature's eyes.

Two sets of photos with nothing alive in them:

- COCO's `none` rows (rooms, tables, kitchens, food): 872 tuning and 500 test photos.
- 486 photos made here, since no host with more photos can be reached from the cloud machines: 60 each of coins, brick walls, stones, rust, tiles, plastic toys, stains on cloth and cracked concrete, drawn with varied color, scale, light, blur, noise and JPEG quality, and the six odd photos of `test/rec/photos`. They were encoded by the pocket encoder in onnxruntime after the worker's own resize and crop, and split by a hash into 258 tuning and 228 test photos.

| Set | Photos | Living kind asserted, with the county list | Head alone (away from the county) |
|---|---:|---:|---:|
| COCO `none`, test | 500 | 3 (2 plant, 1 cat) | 4 |
| Made, tuning | 258 | 28 (all `other`) | 136 (all `other`) |
| Made, test | 228 | 19 (all `other`) | 122 (all `other`) |

The rooms are nearly always right. The made subjects are another matter: away from the county the page calls about half of them "this creature". Stains, stones, coins and rust account for most of these, and bricks and tiles almost none. The head's own probability of `none` for these photos is near zero (median 0.0002), so the head is confident they belong to `other`, and the trouble is in what `other` was fitted on (living things of no carried group), which includes plenty of texture.

## The rules tried, on tuning photos only

Each rule turns an asserted living kind into "not sure", which opens the existing sheet. Scoring is strict: a photo a rule newly sends to the sheet counts as not named and not right for every pass mark of `docs/tracks/head.md`. File size and time do not change under any rule.

| Rule (level) | Made photos still given a living kind, list / alone (of 28 / 136) | COCO balanced, list / alone (mark 0.9367) | Old kinds, Alachua (points, lower bound) | Real `other` creatures newly asked |
|---|---|---|---|---:|
| None (today) | 28 / 136 | 0.9615 / 0.9568 | 0 | 0% |
| Head's `none` at least 0.02 | 24 / 127 | 0.9556 / 0.9471 | 0.0 (0.0) | 0% |
| Fused `none` at least 0.01 | 22 / 122 | 0.9505 / 0.9397 | 0.0 (0.0) | 0.1% |
| Winner minus `none` under 0.88 | 18 / 129 | 0.9571 / 0.9490 | -1.08 (-1.56) | 1.4% |
| Winner minus `none` under 0.89 and above | | | fails | |
| Nearness to any species row | | | fails at every level that changes anything | |
| `other` under 0.92 | 11 / 109 | unchanged | 0 | 10.5% |
| `other` under 0.95 | 4 / 59 | unchanged | 0 | 21.1% |
| `other` under 0.98 | 0 / 14 | unchanged | 0 | 42.3% |

"Real `other` creatures newly asked" is the share of world tuning photos of creatures in no carried group that the page calls "this creature" today (3,533 photos) and that the rule would send to the sheet instead. No pass mark counts these photos.

## Decision: no rule ships

The rules that look for evidence of nothing alive (the probability of `none`, its gap to the winner, nearness to any species) hold the marks only where they change almost nothing: the best of them leaves 122 of 136 made photos called "this creature" and spends most of COCO's margin. The one rule that does remove the made cases is a confidence level for `other`, and it removes them by asking about real creatures too. At 0.95 it asks about one in five creatures the page now calls "this creature". It holds every pass mark only because no mark looks at those photos, so the marks cannot vouch for it.

The plainest reading of the made photos also argues against it. Drawn pictures are far from any photo the head was fitted on, and a head is usually less sure of any picture far from its training photos, whether or not anything in it is alive. The lower confidence of `other` on drawn coins may be a sign that they are drawn, and a phone's photo of real coins may come out as sure as a real snail. The made photos can show that a rule removes drawn cases; they cannot show that it removes real ones.

The test photos were read after the tuning choice: the made test half once, and COCO, world and Alachua test photos twice (a first run, before the made photos existed, chose the head's `none` at 0.02 on COCO alone and held every mark on test). The test numbers above agree with the tuning numbers, and no choice was made on them.

## What would settle it

Real photos of the made subjects (coins, stones, stains, rust, bark, bread, toys) from a phone, a few hundred, with COCO's rooms beside them. Two uses: score the `other` level above on them before anything ships, and add them to the fit as `none` rows (as COCO's rooms are), which addresses the cause, since `other` was fitted without any such texture marked as nothing alive. `tools/world/nonlife_make.py` would need a few lines to encode a folder of photos in place of the drawn families, and `nonlife.py --made` reads its output as it is.

## Real photographs (track nonlife2, 18 October 2026)

Stated before any real photo was fetched or measured (commit on `agent/nonlife2` before the first run of `.github/workflows/nonlife.yml`).

The photos: about 1,500 real photographs from Wikimedia Commons in fifteen families (coins, stones, rust, stains, bricks, food on plates, toys, clothing, furniture, screens, cars, signs, sky and clouds, floors, walls), licensed CC0, CC BY or public domain, with each photo's licence, author and Commons page in `manifest.csv` on `pub/nonlife-real` (`tools/world/nonlife_real.py`). A photo is left out when its title, description or categories name a living thing. Each photo's set (tune or test) is fixed by a hash of its id when the manifest is made, half and half.

The rules: the five rules above, and a linear probe on the photo's vector fitted on the tuning photos only (the real tuning photos against the world tuning photos, scored out of fold on the photos it was fitted on). A rule is chosen on the tuning photos only: the fewest asserted living kinds on COCO's rooms and the real photos, among the rules that hold every pass mark of `docs/tracks/head.md` and send at most 5% of real creatures to the sheet. The 5% stands, since nothing above argues for another level.

The marks on the test photos, read once: every pass mark of `docs/tracks/head.md` as `nonlife.py` scores it; at most 5% of the world test photos of creatures the page calls "this creature" today sent to the sheet, and at most 5% of all world test photos; and at least a quarter fewer living kinds asserted on the real test photos with the head alone. The rule ships only if all three hold. The larger model's answers on the same photos are measured and reported; no rule is chosen with them.

Added after the photos were fetched and before any measurement on them was read (run 1 of `nonlife.yml` measured all 1,525 fetched photos; its results were set aside unread): the search let through photos that are not what the set is for, so every photo was looked at by eye and given a verdict in `tools/world/nonlife-real-review.csv`. 1,000 are kept (496 tune, 504 test). Left out: 361 in which something alive can be seen (people or hands, plants, trees, grass, the stained cells and bacteria the query "stain" brings, one millipede, one mite, one fly), 148 that are not photographs (paintings, prints, documents, patent drawings, rendered textures) and 16 likenesses of people or animals (dolls, mannequins, toy animals, an animal relief). The kept photos are the measurement; the same marks and the same choice apply to them. Run 1's numbers on all photos are reported beside them.

Added after run 2 chose the probe at 0.9 on the tuning photos and passed the three marks on the test photos, and before run 3: the creature photos the head work uses include COCO's own animals (cats, dogs, and the horses, cows and sheep filed as `deer`), which the marks above count only through COCO's balanced share. Run 3 reports, for the same rule with nothing chosen again, the share of those photos the rule sends to the sheet, with the county list and alone. The 5% applies to them too: the rule ships only if at most 5% of COCO's animal photos are sent to the sheet on the test photos, both ways.

### What the pocket model answers on real photos

Run 2 of `nonlife.yml` (`runs/nonlife/2-pocket` on `ci`), the page as build 38 runs it (`models/pocket`, `kind_at` 0.87), on the 1,000 kept photos. A photo counts when the page asserts a living kind for it, which today means "this creature" (`other`) almost every time.

| Photos | Tune | Test |
|---|---:|---:|
| Kept photos | 496 | 504 |
| Living kind asserted, head alone (away from the county) | 35 (32 `other`) | 34 (33 `other`) |
| Living kind asserted, with the county list | 8 | 8 |

That is about 7% with the head alone and under 2% with the list, far from the half of the drawn pictures. By family, both halves together, head alone: coins 23 of 64, rust 14 of 71, stains 8 of 52, stones 8 of 62, walls 7 of 66, and at most 2 in each of the ten other families (none at all for bricks, food, toys or furniture). Run 1, on all 1,525 fetched photos before the review, gave 66 of 746 and 70 of 779 with the head alone and 21 and 18 with the list.

### The rule chosen on the tuning photos

Every rule of the grid, scored on the tuning photos (the probe's scores out of fold), keeping only rules that hold every pass mark and send at most 5% of real creatures to the sheet. The fewest living kinds left on the 35 real tuning photos (head alone) and 8 (with the list): the head's `none` at 0.02 leaves 31 and 8; the fused `none` at 0.01, 25 and 8; the gap at 0.88, 30 and 8; `other` under 0.89, 30 and 8 (it asks about 3.5% of the creatures called "this creature"); nearness to a species, nothing passes; the probe at 0.9, 8 and 0. The probe at 0.9 is chosen. Below 0.9 it fails COCO's balanced share (0.9343 at 0.85, against the mark of 0.9367).

### The test photos

Read once for the choice (run 2) and once more for the same rule, with nothing chosen, to count COCO's animals (run 3; the probe file of both runs is the same byte for byte).

| On the test photos | Today | With the probe at 0.9 | Mark |
|---|---:|---:|---|
| Real photos with a living kind, head alone | 34 of 504 | 10 | at least a quarter fewer: 71% fewer, passes |
| Real photos with a living kind, county list | 8 | 4 | |
| COCO rooms with a living kind, list / alone | 3 / 4 of 500 | 3 / 4 | |
| World creatures called "this creature" sent to the sheet | | 3 of 3,483 (0.09%) | at most 5%, passes |
| All world test photos sent to the sheet | | 0.03% | at most 5%, passes |
| Alachua test photos sent to the sheet | | 0 | |
| COCO animals sent to the sheet | | 12 of 340 (3.5%): cats 2 of 77, dogs 0 of 63, horses, cows and sheep 10 of 200 (5.0%) | at most 5%, passes |
| Every pass mark of `docs/tracks/head.md` | pass | pass | COCO balanced 0.9445 with the list and 0.9415 alone (today 0.9597 and 0.9567, mark 0.9367); old kinds 0.0 points on world and Alachua photos; groups named unchanged |

The cost lands on animals photographed at home and on farms, which is where the probe's idea of a room, a floor and a wall meets a real creature: 3.5% of COCO's animals overall, and on its horses, cows and sheep exactly the 5% mark (5.4% on the tuning photos). Wild creatures are almost untouched.

The probe was fitted on vectors from onnxruntime on the CPU for the real photos and from the phone's WASM runtime for the world photos, which could have let it learn the runtime. It did not: on the 6,000 Alachua 2025 photos the lab holds in both forms, its mean logit differs by 0.06 between them and 8 photos reach 0.9 in each.

### What the larger model answers on them

Run 1 of `nonlife.yml` (`runs/nonlife/1-big` on `ci`, `big-photos.jsonl` photo by photo): BioCLIP 2's vectors from the original weights in torch, and the page's arithmetic for the full database (`models/naturalist`, every file its manifest names, checked by SHA-256; its kinds head from kind phrases, `kind_at` 0.5), with no time zone and in Alachua County's. Split by the review afterwards:

| Kept photos | No time zone | Alachua's zone |
|---|---:|---:|
| Living kind asserted, tune (496) | 163 | 158 |
| Living kind asserted, test (504) | 182 | 187 |
| "Nothing alive" asserted | 0 | 0 |
| Not sure | 655 | 655 |

So the larger model asserts a living kind for about a third of these photos (225 `other`, 85 `plant`, 16 `insect`, 14 `bird` among the 1,000 with no zone), and it never asserts `none`: its kind phrase for nothing alive does not win on any of them. By family, with no zone: rust 48 of 71, food 49 of 85, stones 35 of 62, stains 30 of 52, coins 26 of 64, walls 24 of 66, bricks 23 of 76, floors 22 of 73, furniture 22 of 88, screens 18 of 78, toys 17 of 67, sky 14 of 70, clothing 7 of 57, signs 6 of 32, cars 4 of 59. On all 1,525 fetched photos it is the same, 531 (34.8%).

This matters for the rule below. Where the full database is kept, a pocket answer that is not sure is handed to the larger model before the person is asked. Of the 24 test photos the probe turns to not sure (head alone), the larger model asserts `other` for 12 and is not sure of 12; so on a phone that keeps the full database the probe's gain is about halved, and the larger model needs a rule of its own (its vectors of these photos are on `ci` beside its answers).

### Decision: the probe at 0.9 ships in build 39

All four marks hold on the test photos (the three stated before measuring and the one for COCO's animals), so the rule ships: `fusion.nonlife` in `models/pocket/manifest.json` (512 weights, a bias and the level 0.9, 7.7 KB more in the manifest), applied in `fuseWith` of `src/cam.rec.js` and in `tools/fusion/fuse.py`, with 150 cases of `tools/fusion/parity.py` that use it (8 of them turned from sure to not sure, 0 differ between the page and the reference). Where the probe is at least 0.9 and the page would assert a living kind, the answer becomes not sure, and the page asks what was photographed (or, where the full database is kept, asks it first, as for any answer that is not sure). The larger model is unchanged.

`tools/world/head.py` scores "today's page" with a vectorized copy of the rule that does not apply the probe, so a later run of it reads the page as it was before build 39; `nonlife.py --fixed probe:0.9 --probe` gives the page with it (the probe is fitted again on the same photos and comes out the same).

The plainest reading of these numbers: the drawn pictures overstated the trouble, since on real photos the pocket head errs about 7% of the time alone and 2% with the list, mostly on coins, rust, stains, stones and walls. The probe removes most of those at the price of about one horse, cow or sheep in twenty and one cat in forty. The cause is still there: the 1,000 kept photos (or their tuning half) belong in the next fit of the head as `none` rows, after which the probe may no longer be needed.
