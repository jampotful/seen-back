# An independent check of the accuracy numbers

_Written by the audit of 11 October 2026 (04:37 to 05:30 Eastern). The numbers come from `tools/audit/recompute.py` and `tools/audit/softspots.py`; their output is in `tools/audit/results/`. How to rerun them is in `tools/audit/README.md`._

## What was recomputed, and how

The two scripts were written from the prose of `docs/EVAL.md`, `docs/CONTRACTS.md` and `tools/fusion/README.md`. They import nothing from `tools/eval/` or `tools/fusion/`. Code in `tools/eval/` was read only afterwards, to find the cause of a disagreement, and each place is named below.

- **Inputs.** `pub/data-alachua` at `6e9a8aa` (evaluation and training manifests, the species list, the COCO extras), `pub/lab-bioclip2-l14` at `6b92505`, `pub/lab-tinyclip-39m-16` at `a7d5002`, `pub/heads-alachua-pre2025-tinyclip-39m-16` at `6200430`, and `models/pocket/` and `models/naturalist/` on `main` at `8037aec`. EVAL.md names `pub/lab-bioclip2-l14` at `f552a63`; the test vectors on `6b92505` are byte for byte the same file as the copy extracted at 23:15. The files of `models/pocket/` are byte for byte those of `pub/heads-val-tinyclip-39m-16`.
- **BioCLIP 2 against the list.** Cosines between the test photos' vectors and the 5,911 rows made from scientific names; the prior adds `0.012 * log(share)` to the cosine, with a month's weight of `m + 2 n / 12 + 1` (the settings `labelsets.md` gives as chosen on `val`).
- **The page's rule.** Each test photo goes through the two slots on `main` as `tools/fusion/README.md` describes the page: kinds and species scored from the slot's own half-precision files and biases, the prior from the slot's table, the `mix` rule, and `kind_at`, under which no kind is asserted and no species is named.
- **Shares and intervals.** Every share below is a count divided by a count, rounded once. Intervals are 95% percentile intervals from 2000 resamples over photos with this audit's own seed, so an interval's ends can differ from EVAL.md's by a tenth.

## Disagreements

1. **The pocket model names fewer species than reported.** EVAL.md gives `val-tinyclip-39m-16` (the pocket slot live in build 8) a species named for 14.2% of the wildlife test photos and right for 92.0% of those. Under the page's rule the slot names a species for 557 of 4,197 photos (13.3%) and is right for 514 of them (92.3%); three species are offered for 342 photos (8.1%, against 7.3%). The committed per-photo record, `docs/eval/shipped-val-tinyclip-39m-16.json`, names 39 photos that the same record marks as having no asserted kind, and the page names nothing on such photos (`tools/fusion/fuse.py` on `main`, lines 152 to 157). The cause is the order of the work: these numbers were made with a `fuse.py` that had no `kind_at`, and the gate on naming reached `main` only in `8037aec` at 04:25. The trained heads of run 25 carry the same fault: run 25 ran on commit `c0cd718` (03:36), whose `fuse.py` has no `kind_at`, and its own record (`runs/eval/25/shipped-alachua-pre2025-tinyclip-39m-16.json` on the `ci` branch) names 1,044 photos (24.9%, right for 88.2%), of which it marks 76 as having no asserted kind. These are exactly the counts this audit finds with `kind_at` ignored. Under the page's rule that slot names a species for 968 photos (23.1%) and is right for 875 of them (90.4%).
2. **The larger model's slot on `main` differs from the slot that was scored.** `models/naturalist/manifest.json` carries `kind_at: 0.5`; EVAL.md, the manifest's own `fusion_thresholds_note` and the published branch `pub/heads-naturalist-bioclip2-l14` describe the slot without it. With `kind_at` 0.5 the page names a species for 3,533 of 4,197 test photos (84.2%, against 84.6%), the name is right for 3,469 of them (98.2%, against 98.1%), three species are offered for 489 photos (11.7%, against 11.3%) and hold the species for 449 (91.8%, against 92.2%), and a kind is asserted for 98.1% and right for 98.9% of those. The line in `docs/LOG.md` at 04:27 ("a species name for 84.7% of test photos and the name is right for 98.0%") is reproduced by none of the four combinations this audit tried (`val` or `test`, with or without `kind_at`); its source was not found.
3. **Four printed figures are a tenth away from their own counts.** `tools/eval/ev.py` (line 136) rounds each share to four places and `tools/eval/report.py` then prints it to one, so a share that ends in a five at the fourth place moves. Rounded once from the counts:

| Figure | Count | EVAL.md prints | Rounded once |
|---|---:|---:|---:|
| BioCLIP 2 top-1 without the prior | 3,792 of 4,197 | 90.3% | 90.4% |
| Larger model's slot, top species right | 3,880 of 4,197 | 92.5% | 92.4% |
| Pocket slot, named species right (`kind_at` ignored) | 548 of 596 | 92.0% | 91.9% |
| Pocket slot, kind right on the extra set's test photos | 1,217 of 1,240 | 98.2% | 98.1% |

   The last of these is the "98.2% of the photos of people, pets and rooms" in `docs/LOG.md` at 04:27.
4. **The month of a COCO photo changes the extra set's results.** This audit first took a COCO photo's month from the manifest's `month` column and found 59 of 63 dogs right (EVAL.md: 60) and a species named on 7.4% of the extra set's test photos (EVAL.md: 6.2%). With the month EVAL.md describes ("a calendar month by a hash of its id"; the hash, `sha256("month|" + id)` modulo 12, was read in `tools/eval/kinds.py`, line 42) every count of EVAL.md is reproduced. Both are defensible, because the page uses the phone's clock: the share of the 77 cat photos given a species name runs from 35% to 73% across the twelve months (with the hash month all 39 names given were *Felis catus*).

## The agreement table

Test split, 4,197 wildlife photos unless the row says otherwise.

| Number | docs/EVAL.md | This audit | Same to the first decimal |
|---|---:|---:|---|
| BioCLIP 2 top-1, no prior | 90.3% | 90.4% (3,792) | no: rounding, item 3 |
| BioCLIP 2 top-5, no prior | 96.8% | 96.8% (4,063) | yes |
| BioCLIP 2 top-1 with the prior | 92.4% | 92.4% (3,878) | yes |
| BioCLIP 2 top-5 with the prior | 97.5% | 97.5% (4,090) | yes |
| Paired gain from the prior | +2.1 (+1.4 to +2.7) | +2.1 (+1.4 to +2.7) | yes |
| Kind from the top species, no prior | 98.0% | 98.0% (4,114) | yes |
| Kind from the top species, with the prior | 98.3% | 98.3% (4,126) | yes |
| Kind from summed species probabilities | 98.4% | 98.4% (4,128) | yes |
| Test photos of species outside the list | 36 | 36 | yes |
| Test photos with a `val` photo within cosine 0.95 (same species) | 1,470 (1,454) | 1,470 (1,454) | yes |
| Larger model's slot: kind right | 98.0% | 98.0% (4,114) | yes |
| Larger model's slot: top species right | 92.5% | 92.4% (3,880) | no: rounding, item 3 |
| Larger model's slot: named, as scored (no `kind_at`) | 84.6% | 84.6% (3,549) | yes |
| Larger model's slot: named right, as scored | 98.1% | 98.1% (3,481) | yes |
| Larger model's slot: named, as on `main` (`kind_at` 0.5) | 84.6% | 84.2% (3,533) | no: item 2 |
| Larger model's slot: named right, as on `main` | 98.1% | 98.2% (3,469) | no: item 2 |
| Pocket slot: kind right | 87.3% | 87.3% (3,663) | yes |
| Pocket slot: kind asserted | 78.8% | 78.8% (3,307) | yes |
| Pocket slot: right when asserted | 95.5% | 95.5% (3,157 of 3,307) | yes |
| Pocket slot: top species right | 36.3% | 36.3% (1,525) | yes |
| Pocket slot: species named | 14.2% | 13.3% (557) | no: item 1 |
| Pocket slot: named species right | 92.0% | 92.3% (514 of 557) | no: item 1 |
| Pocket slot, extra set (1,240): kind right | 98.2% | 98.1% (1,217) | no: rounding, item 3 |
| Pocket slot, extra set: kind asserted | 95.5% | 95.5% (1,184) | yes |
| Pocket slot, extra set: right when asserted | 99.2% | 99.2% (1,175 of 1,184) | yes |
| Pocket slot, extra set: a species named | 6.2% | 6.2% (77) | yes, with EVAL.md's month (item 4) |
| Run 25, trained 39M slot: kind right | 88.5% | 88.5% (3,715) | yes |
| Run 25: kind asserted, right when asserted | 84.8%, 95.0% | 84.8%, 95.0% | yes |
| Run 25: top species right | 53.4% | 53.4% (2,240) | yes |
| Run 25: species named, named right | 24.9%, 88.2% | 23.1% (968), 90.4% (875) | no: item 1 |
| Int8 file through the WASM runtime, 320 test photos: named right (`kind_at` ignored) | 97.9% | 97.9% (275 of 281) | yes |
| The same, as on `main` (`kind_at` 0.5) | 97.9% | 98.2% (275 of 280) | no: item 2 |

The run 25 figures on the left are those of `runs/eval/25/shipped-alachua-pre2025-tinyclip-39m-16.json` on the `ci` branch. The int8 rows use `runs/lab/25-device-hybrid-fc2-w8/wasm_hybrid-fc2-w8.f16.npy` on the `ci` branch, the vectors the shipped file gave through onnxruntime-web's WASM build on a build machine; the script that scored them is the last block of `tools/audit/README.md`.

## Soft spots, each with its size

### Could a test photo have informed a setting?

EVAL.md says that `val` and `test` are cut by a hash of the record id. This audit did not recompute that hash; it checked that no observation address, GBIF record or photo number repeats among the 6,000 photos, so no observation sits on both sides (1,803 on `val`, 4,197 on `test`). Every threshold in the two shipped manifests was traced.

- **Pocket slot.** Its notes say that the prior, the kinds head, `t_kind`, `w_kind` and the rule were chosen on the third of `val` kept for tuning, and `name_at`, `offer_at` and `kind_at` on the same 565 photos with 3,056 tuning rows of the extra set. Nothing in it points at `test`. This audit did not rerun the tuning.
- **Larger model's slot.** The prior and the rule were chosen on `val` by `tools/eval/study2.py`, and `name_at` 0.78 and `offer_at` 0.67 on `val` at a bar of 98 in 100. That bar was picked after EVAL.md had set the test outcomes of three bars (90, 95 and 98 in 100) side by side. `kind_at` 0.5 was set by hand; the manifest's note cites `tools/eval/nat_kind_at.py`, which prints the outcome on `val` and on `test` together. The `val` figures alone support the choice (right for 0.990 of asserted kinds on `val`, by the note), and 0.5 is the lowest level that script tries. Each of these is a choice among a handful of levels, so any bend it gives the test figures is smaller than the gap between neighbouring levels.
- **The weight of one half.** `tools/fusion/README.md` calls `w_kind` of exactly one half under the `mix` rule "a coin's edge" that should be avoided. The larger model's slot ships with it. On the test photos the kind phrases and the species list point at different kinds for 998 photos (23.8%); the combination sides with the species list on 944 of them, and the kind is then right for 944 (94.6%), where the species list alone would be right for 957 (95.9%). For 90 photos (2.1%) the winning probability lies within 0.02 of one half, which is also where `kind_at` 0.5 falls.

### Are the evaluation photos later than everything the list and the prior were built from?

They are, by every date this audit could read. Evaluation photos run from 2025-01-01 to 2026-09-29, with no row before 2025. The training photos run from 1910-06-07 to 2024-12-31, with no row after 2024. The species list and its monthly counts come from a GBIF query bounded by `year=1600,2024` (`records_through` 2024-12-31). No photo number appears in both the training and the evaluation manifests. That BioCLIP 2's training data is a GBIF snapshot of 2024-05-01 rests on the dataset card quoted in `docs/eval/others.md`; this audit did not read that card again.

### Near-copies, and what the numbers are without them

- **Test against `val`** (the photos that fitted the live pocket slot's rows and set every threshold). In BioCLIP 2's space one test photo has a `val` photo above cosine 0.995 and 53 have one above 0.99, all of the same species. A photographer's name is in no manifest, so "the same photographer on the same day" was approximated by "the same species on the same day": 221 test photos (5.3%) have such a twin on `val`.
- **Without those 222 photos** the larger model's top species stays at 92.4% (3,672 of 3,975) and its named species are right for 98.1%. The live pocket slot, whose rows were fitted on two thirds of `val`, falls from 36.3% to 34.8% top species right, from 92.3% to 91.7% named right and from 87.3% to 86.9% kind right. On the 222 twin photos themselves the pocket slot's top species is right for 140 (63.1%), against 34.8% on the rest, while the larger model, which fitted nothing on `val`, gets 93.7% against 92.4%. That difference is the size of a leak through outings for heads fitted on `val`. Run 25's trained slot, fitted on photos from before 2025, moves from 53.4% to 52.9%.
- **Test against the training photos.** BioCLIP 2's vectors of the training photos are unpublished, so this used TinyCLIP 39M/16's vectors of all 84,808. No test photo has a training photo above cosine 0.99, and 11 have one above 0.98 (6 of the same species), dated years apart. Removing near-copies changes nothing because there are none at that level.

### Do photos of one outing make the intervals too narrow?

They do not, by any amount this audit could measure. Resampling whole species-days (3,949 groups) or whole days (626 groups) in place of single photos moves an interval's ends by a tenth at most: the larger model's kind right is 97.6 to 98.4 over photos and 97.5 to 98.5 over days, its named species right 97.8 to 98.6 and 97.7 to 98.6; the pocket slot's kind right is 86.3 to 88.3 and 86.2 to 88.3.

### Does the mix of kinds hide a weak kind?

Plants (1,223 photos, 29.1%) and insects (962, 22.9%) make up 52.1% of the test photos. For the larger model no kind with enough photos is weak: a named species is right for 93.5% of the 77 frogs named and for 96.5% to 100% of every other kind with 30 or more named. The pocket slot has weak kinds that its average covers: bees are given the right kind for 60.3%, and an asserted kind on a bee photo is right for 72.4%.

| Kind | Photos | Larger model: top species right | Named | Named right | Pocket: kind right | Asserted | Right when asserted | Run 25 39M: kind right | Right when asserted |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| plant | 1,223 | 94.3% | 84.2% | 98.7% | 98.3% | 93.4% | 99.5% | 98.0% | 99.5% |
| insect | 962 | 89.3% | 82.1% | 96.5% | 88.4% | 78.2% | 95.1% | 94.4% | 96.8% |
| bird | 531 | 91.5% | 85.9% | 98.7% | 84.9% | 71.8% | 96.6% | 86.8% | 94.3% |
| wader | 382 | 97.1% | 91.9% | 99.4% | 85.6% | 84.0% | 93.5% | 84.8% | 91.6% |
| other | 296 | 88.9% | 79.7% | 98.7% | 72.0% | 57.4% | 85.3% | 73.3% | 83.7% |
| reptile | 268 | 93.3% | 86.2% | 98.3% | 83.6% | 68.7% | 93.5% | 73.9% | 93.3% |
| bee | 126 | 89.7% | 74.6% | 96.8% | 60.3% | 69.0% | 72.4% | 71.4% | 77.4% |
| alligator | 110 | 97.3% | 93.6% | 100.0% | 81.8% | 77.3% | 96.5% | 74.5% | 89.7% |
| frog | 97 | 90.7% | 79.4% | 93.5% | 80.4% | 68.0% | 97.0% | 78.4% | 91.0% |
| hawk | 82 | 91.5% | 79.3% | 100.0% | 74.4% | 68.3% | 92.9% | 80.5% | 90.6% |
| squirrel | 36 | 97.2% | 83.3% | 100.0% | 80.6% | 52.8% | 94.7% | 86.1% | 100.0% |
| deer | 36 | 97.2% | 75.0% | 100.0% | 69.4% | 58.3% | 95.2% | 75.0% | 92.3% |
| rabbit | 31 | 100.0% | 100.0% | 100.0% | 87.1% | 51.6% | 100.0% | 77.4% | 95.7% |
| cat | 11 | 81.8% | 72.7% | 100.0% | 63.6% | 63.6% | 85.7% | 63.6% | 100.0% |
| dog | 6 | 83.3% | 66.7% | 100.0% | 50.0% | 0.0% | – | 83.3% | 100.0% |

### Two figures whose wording hides their make-up

- **The extra set's "kind right" is mostly people and rooms.** Of the 1,240 test photos of the extra set, 900 (72.6%) are of people and rooms, where the pocket slot is right for 99.5% and 98.6%. The pooled share is 98.1%; the mean over the five kinds is 96.6%, and cats alone are 92.2% (71 of 77). A rule that compares the pooled share with a bar of 96.5% gives cats, as a kind, about a sixth of the weight of rooms (77 photos against 500).
- **The int8 comparison counts more photos than its prose says.** EVAL.md, under "The larger model on the device", says the laboratory ran each file "on 24 test photos" and that "with 24 photos an interval is several points wide". Five of the six rows hold 320 photos (`docs/eval/variant-*.json`, `test_photos`); only `bioclip2-l14-wasm-fp16` holds 24.

### Is "the species named is right 98 times in 100" true for species with few records?

It holds for common species only. For the larger model as on `main`, a named species is right for 99.3% of 2,079 names of species with 200 or more records before 2025, 98.0% of 1,015 with 50 to 199, 96.4% of 336 with 10 to 49, 87.7% of 73 with 3 to 9 and 87.5% of 24 with 1 or 2. Of the 36 test photos of species outside the list, 6 were named, each wrongly. For the pocket slot the fall is steeper: 97.0% of 494 names for species with 200 or more records, 65.2% of 46 for 50 to 199, and 35.7% of 14 for 10 to 49.

### A pet, a houseplant or a garden flower

The list holds the cat (*Felis catus*, 190 records), the horse (*Equus caballus*, 236) and the chicken (*Gallus gallus*, 14). It holds no dog (the only *Canis* is the coyote), no cattle, sheep or goats. Of eleven common houseplants looked for, it holds only *Epipremnum aureum* (19 records). It holds none of the garden hydrangea, garden roses, camellias, gardenias, the Chinese hibiscus, zinnias, petunias or garden geraniums, though it holds the native oakleaf hydrangea and native hibiscuses. On COCO's test photos the live pocket slot names *Felis catus* on 39 of 77 cat photos, a species on 37 of 200 photos of horses, cows and sheep (33 *Equus caballus*, 3 *Bison bison*, 1 *Odocoileus virginianus*), and *Felis catus* on 1 of 63 dog photos. No number in EVAL.md measures houseplants or garden flowers. For a plant outside the list any species name the app shows is wrong, and EVAL.md's figures say nothing about how often that happens.

## What the owner may say in public, and what not

Three sentences the measurements support:

1. "On 4,197 photos taken in Alachua County in 2025 and 2026 that iNaturalist's community had already identified, the larger model put the right species first for 92 photos in 100."
2. "When the larger model shows a species name, the name was right for 98 of those photos in 100; it shows one for about 84 photos in 100, and for species with fewer than ten local records its names were right about 88 times in 100."
3. "The pocket model, which answers first, chose the right kind of eye for 87 of these photos in 100 and said it was not sure for about one in five."

Three sentences the measurements do not support:

1. "Seen Back is 98% accurate." The 98 in 100 holds for the 84% of identified wildlife photos that get a name, from one county, and falls for rare species.
2. "Point it at your dog, your houseplant or your garden and it will tell you what it is." Dogs, cattle, sheep and most garden and house plants are absent from the list, so any name shown for them is wrong, and nothing measured them.
3. "On your phone the larger model is right 98 times in 100." The figures above come from the original model's vectors. The shipped int8 file, run through the WASM runtime on a build machine, named a species for 280 of 320 test photos and was right for 275 of those (98.2%, with an interval several points wide), and no phone has run it.
