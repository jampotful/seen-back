# Photos with nothing alive: the pocket head's answers, and a rule that was not shipped

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
