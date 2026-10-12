# Coverage

Compiled 12 October 2026 on branch `agent/coverage`. This is the plan for two targets the owner set, with the measurements made so far. Every figure names the script and the run behind it.

1. **The base app** (the pocket model, no download) recognizes every broad group of living things and stays quick and small.
2. **The full database** (the optional download) can name any species a person anywhere might meet.

## The base app: nineteen new groups

Nineteen new groups hold 18,267,887 of the 18,689,811 world records now in `other`. With them, the share of world records in a group the base app recognizes rises from 88.8% to 99.8%. Records are iNaturalist research-grade observations in GBIF read on 11 October 2026 (`docs/VIEWS.md`, `docs/views/world-orders.csv`); the family splits were read from GBIF the same day by the sheet agents (`docs/views/sheets/`).

| New group | What it holds | World records | Where the line comes from |
|---|---|---:|---|
| fungus | mushrooms, brackets, cup fungi, moulds, rusts, lichens | 4,768,141 | fungus sheet |
| fish | ray-finned fish, lampreys, hagfish, lungfish | 2,631,014 | fish sheet |
| spider | every spider except jumping spiders | 2,243,274 | spider sheet |
| snail, slug and chiton | snails, slugs, sea slugs, chitons, tusk shells | 2,085,365 | a first sorting, no source |
| starfish, coral, clam and other sea life | corals, anemones, jellyfish, starfish, urchins, sea cucumbers, clams, mussels, scallops, sponges, sea squirts, moss animals, comb jellies | 1,467,704 | a first sorting, no source |
| crab, woodlouse and other crustacean | crabs, crayfish, shrimp, lobsters, woodlice, barnacles, horseshoe crabs | 1,232,045 | a first sorting, no source |
| mammal | raccoons, bears, weasels, otters, opossums, kangaroos, pigs, rhinos, moles, shrews, hedgehogs, armadillos, elephants | 1,019,965 | a first sorting, no source |
| jumping spider | family Salticidae | 684,540 | spider sheet |
| salamander and newt | salamanders, newts, caecilians | 632,992 | a first sorting, no source |
| worm, millipede and centipede | earthworms, leeches, flatworms, millipedes, centipedes | 340,371 | a first sorting, no source |
| whale, dolphin, seal and manatee | whales, dolphins, porpoises, seals, sea lions, walruses, manatees | 274,115 | a first sorting, no source |
| scorpion and harvestman | scorpions, harvestmen, whip scorpions, pseudoscorpions | 235,122 | a first sorting, no source |
| monkey and ape | every primate but people | 192,888 | a first sorting, no source |
| shark and ray | sharks, rays, chimaeras | 132,395 | fish sheet |
| slime mould | the slime moulds, which are not fungi | 113,223 | fungus sheet |
| bat | every bat except flying foxes | 71,170 | bat sheet |
| tick | order Ixodida | 60,462 | tick sheet |
| octopus, squid and cuttlefish | every cephalopod | 60,462 | a first sorting, no source |
| flying fox | family Pteropodidae | 22,639 | bat sheet |

- Seaweed and other algae (168,308 records) move to `plant`, and springtails (91,432) to `insect`.
- What stays in `other` is 0.10% of world records: mites 106,129 (most of them gall mites, photographed as galls on leaves), microbes 54,040, and water bears, rotifers and velvet worms 2,015.
- Ticks and cephalopods share a count of 60,462 by coincidence; both were checked order by order in `docs/views/world-orders.csv`.
- The recognizer can learn all nineteen at once. Until a group has its view, the page names the group and shows the line it shows today for a creature with no view.

## What the groups cost

- **Megabytes.** A group is one row of 512 half-precision numbers and one bias in the group head, 1,028 bytes. The head grows from 17 labels (17,476 bytes) to 36 (37,008 bytes), 0.05% of the 40,978,137-byte encoder.
- **Time.** 19 × 512 = 9,728 more multiply-adds a photo, beside an encoder that takes about half a second.
- **Accuracy, first test.** `tools/coverage/split_other.py` refits the pocket model's group head (logistic regression, C = 20, licence rule `nc`, the Alachua fitting photos and the fitting part of the COCO extra set) once with today's labels and once with `other` split into fifteen groups close to the new ones, and scores both heads alone, without the species list, on the 4,197 Alachua test photos. Alachua has too few photos of sharks, whales or octopuses to fit those groups. Intervals are 2000 bootstrap resamples, seed 20261011.

| Weighting of groups in fitting | Old groups right, before and after | Paired change (95% interval) | Photos now in `other` named their new group | Photos now in `other` given an old group's eyes, before and after |
|---|---|---|---:|---|
| a group's photos weighted by one over the square root of their number (today's) | 87.1% to 86.0% | −1.1 points (−1.7 to −0.5) | 78.0% | 25.3% to 14.9% |
| every photo counts the same | 87.5% to 88.1% | +0.6 points (+0.1 to +1.1) | 69.3% | 28.4% to 25.0% |
| every group counts the same | 83.4% to 79.8% | −3.7 points (−4.4 to −3.0) | 77.4% | 23.6% to 11.1% |

On the vectors a phone computes, today's weighting loses 0.7 points (−1.3 to −0.2). On the COCO test photos (people, pets, livestock, empty rooms) the mean share right over the five kinds moved from 95.2% to 94.9%, and a new group was named for 3 of 1,240 photos. Large groups were found and trusted (fungus named for 85% of 62 fungus photos, 65% of fungus calls right; spider 73% of 115, 67% right). Small groups were over-called: 8 of 9 crabs were named crab, and so were 15 of 962 insects. The fitting set held 36 clams beside 31,231 insects, so world photos should lift the small groups.

## Training photos

Every photo comes from iNaturalist's open-data bucket (README at https://github.com/inaturalist/inaturalist-open-data: over 400 million photos, monthly snapshots of observations, photos and taxa). The snapshot of 27 September 2026 holds 169,713,700 research-grade observations; one pass over all of them takes 7 minutes on a build machine (`ci/coverage/counts.sh`, run `runs/coverage/1-lists` on `ci`).

- Fitting: up to 3,000 research-grade photos dated before 2025 for each of the 33 groups of creatures (the fourteen with views and the nineteen new), drawn evenly across continents and across each group's orders, a few to a species. The old groups are refitted the same way, since their rows were fitted on Alachua photos alone. About 100,000 photos, beside the 83,348 the present head was fitted on.
- Tuning and test: 300 photos a group dated 2025 or later for each, spread by continent. Test photos choose nothing.
- Nothing alive: the COCO set stays in every tuning and grows toward what the new groups invite (bread, rust, stains, coins, bark, stones, toys, empty shells).
- Pets, livestock and garden plants: the casual observations in the same snapshot (13.5 million, across 122,016 species at species rank).
- Licences: public domain, CC BY and CC BY-NC only (the rule `nc`), with the list of fitted photos published beside the head as `fitted_on` already is.

## Pass marks, set before the runs

| Claim | Measured by | Pass mark |
|---|---|---|
| The new groups cost the old ones little | paired difference in old groups right, head and species list combined as the page does, on Alachua test photos and on world test photos | the 95% interval stays above −2 points on both |
| Every new group is found | share of a group's world test photos named that group, and share of photos called that group that belong to it | 75% or more on each; a group that fails stays in `other` until it passes |
| People, pets and empty rooms are unharmed | the COCO test photos | within 1 point of today |
| `other` stops lending the wrong eyes | share of creatures with no group given an old group's eyes | under 10% |
| The base app stays light and quick | head file size; time a photo in the laboratory's phone runtime | under 50 KB; within 5% of today |
| Every row of a view holds to its source | each source opened again by an agent that has not seen the sheet | no row ships on a source nobody could open |
| The full database names species anywhere | share named and share of names right, on Alachua photos against growing lists and on 500 test photos from each continent dated 2025 or later | 97 names in 100 right on every continent |
| Pets and garden plants are named | 1,000 casual photos of the commonest captive and cultivated species | 95 names in 100 right |

## Views

Five sheets are written and each was checked by an agent that had not seen it (`docs/views/sheets/`). No source turned out to be invented or credited to the wrong paper; the checks corrected a handful of figures in each sheet. The sheets propose nine views:

| View | What the picture does | What the engine still lacks |
|---|---|---|
| jumping spider | a sharp, magnified centre inside nearly the whole circle; reds dark, ultraviolet as invented violet | an upright sharp strip that jumps to what moves |
| spider | very coarse; only what moves is drawn, in place of the web's shaking | the web's shaking, which the motion sensors could stand in for |
| fish | a 335° field at about 4 cycles per degree; blue dark and yellow pale, as for a largemouth bass | the sky squeezed into a 97° circle when the phone looks up |
| shark and ray | grey, with trails | the electric sense, which no phone can stand in for |
| bat | coarse, nearly colourless, holding and jumping about seven times a second | a picture made of echoes, from a depth sensor or a depth model |
| flying fox | 4 cycles per degree, two cone types, shadows lifted | nothing |
| tick | grey from blue and green light at 0.1 cycles per degree | heat, breath and smell |
| fungus | no picture: blue and green light and its direction, averaged slowly | gravity from the tilt sensor; averaging over minutes |
| slime mould | no picture: away from blue, toward red, pulsing | nothing |

Two findings for the page: a typed "flying fox" gets the dog's eyes, because the word table in `src/cam.r.js` matches "fox" before any bat entry exists; and `docs/SOURCES.md` backs the line that an ordinary camera cannot record ultraviolet with a page that does not say so. The next sheets follow the records: snail, starfish and coral, crab, mammal, salamander, worm, whale and seal, scorpion, monkey, octopus.

## The full database

Lists come from research-grade observations dated through 2024 in the open-data snapshot (`tools/coverage/lists.py`): 6,106 species in the county box, 8,140 within 100 km of Gainesville, 16,210 within 400 km, 55,724 within 1,600 km, 92,372 in a box round the lower 48 states, and 433,036 anywhere (465,236 counting 2025 and 2026). The commonest 2,363 species carry half of all records, 32,558 carry 90%, 100,000 carry 97.6% and 158,902 carry 99%.

`tools/coverage/score.py` scores the Alachua test photos against each list with BioCLIP 2, four sentences a species made from iNaturalist's names (`tools/coverage/text.py`), settings chosen on the tuning photos, the prior `alpha * log(share)` of the area's records with no season (run `runs/coverage/2-score` on `ci`; run 1 used one sentence and gave the same picture). A photo whose species is not in a list counts as wrong.

| List | Species | Rows, one byte a number | Right species first, prior of the list's area | Right species first, prior of the 400 km round the photo | Photos named | Names right |
|---|---:|---:|---:|---:|---:|---:|
| Alachua County list | 5,829 | 4.5 MB | 90.5% | – | 79.1% | 98.1% |
| within 100 km | 8,140 | 6.3 MB | 90.5% | – | 80.8% | 98.0% |
| within 400 km | 16,210 | 12.4 MB | 90.2% | 90.2% | 82.2% | 97.7% |
| within 1,600 km | 55,724 | 42.8 MB | 88.2% | 90.3% | 77.5% | 97.6% |
| lower 48 states | 92,372 | 70.9 MB | 87.8% | 90.2% | 74.5% | 97.8% |
| world, 100,000 commonest | 100,000 | 76.8 MB | 85.3% | 90.1% | 70.0% | 96.8% |
| world, every species | 433,156 | 332.7 MB | 85.3% | 90.2% | 69.6% | 96.7% |

Photos named and names right are for the list's own prior. With the 400 km prior, the world list names 82.6% and is right for 97.4%. Rows of one byte a number changed top-1 by 0.0 points (−0.1 to +0.1) against two bytes.

- **The place enters through the prior.** The rows can cover the world; what the app needs to know about the place is a count for each species recorded there, tens of kilobytes for a 400 km circle.
- **The plainer reading.** Alachua's photos are mostly of species the county records often, so any prior favouring what is common nearby gets them right; the flat line may owe more to Florida's dense records than to the design. A test on thinly recorded places settles it.
- **Names.** Rows from iNaturalist's names scored 87.8% on the county list with no prior, against 90.4% for the live rows from GBIF's names. The likeliest cause is the 236 test photos whose species are named differently in the two taxonomies (`docs/EVAL.md`), not yet split out. The world rows should use GBIF's names, as the county rows do.
- **The place without asking.** The phone's time zone narrows the world to a band with no permission; the creatures already met narrow it further; a library photo's own location could set it at once if the owner allows reading it on the phone.
- **Size.** With the 310 MB encoder, every species comes to about 640 MB and the 100,000 commonest to about 390 MB. A cut by world records drops species common only where few people record, which Alachua's photos cannot show.
- **Pets and garden plants.** Dogs, cats, chickens and horses have research-grade records (19,180, 68,484, 25,656 and 11,576 all time), so they are in the rows. The casual observations add 1,184 species seen mostly in captivity or gardens (50 or more casual records and more than twice their research-grade ones), 43 of them with no research-grade record before 2025.
- **The pocket model's species names.** Its species head was fitted on county photos, so outside the county it names county species. Raising `name_at` and `offer_at` above 1 in `models/pocket/manifest.json` stops that with no code changed; the decision is the owner's.

## Order of work

1. Stop the pocket model's species names outside the county (two numbers in its manifest), once the owner decides.
2. Word-table entries for the nineteen groups, ahead of `dog`.
3. World photos for 33 groups, nothing alive and casual, from the open-data snapshot, published to `pub/data-world`.
4. The new group head, scored against the pass marks; shipped with `eyes.py`, the word table and the list of groups updated.
5. Views in waves, each sheet read by the owner before it is drawn.
6. World rows from GBIF's names, four sentences, one byte a number, published in parts; plus the casual species.
7. Prior files per cell of a world grid, the time zone as the first guess, and the encounter rule, measured on held-out photos.
8. The world test: 500 photos from each continent from 2025 on, reported in `docs/EVAL.md` before the page claims anything about another continent.
9. The next sheets, in record order.

## How to rerun

- The pilot: `python3 -I tools/coverage/split_other.py DIR . OUT_JSON` with the layout in its first lines; `POWER=0` and `POWER=1` give the other two weightings.
- The lists, rows and scores: push this branch to `run/coverage/<label>`; `ci/coverage/templates.txt` says `one` or `four` sentences. Results come back as `runs/coverage/<run>-lists`, `-text-<shard>` and `-score` on `ci`. A run takes about 25 minutes with one sentence and an hour with four.
- `score.py` given the live rows reproduces the published 90.4% (no prior, test photos) for the larger model on the county list.
