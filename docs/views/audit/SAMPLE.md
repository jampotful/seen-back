# The grade changes, read before they are applied (burst 9)

The second audit pass corrected 1,152 records, and 975 of those corrections change the grade: 820 from `m` to `g`, 146 from `g` to `m` and 9 between other grades. The `m`-to-`g` changes follow a rule in `SYSTEM_ADJ` (`tools/lit/audit.py`): a species-level record whose passage names only a genus, family or common name, or reports other studies, is `g`. This page reads a sample of those changes against the research brief, decides a narrower rule, and says what the corrected copies hold.

## Method

`tools/views/audit_sample.py` drew the sample with a fixed seed (9). It takes the corrections from `m` to `g`, gives each unit a share in proportion to its count (at least two where the unit has two), and spreads each unit's share across its traits. The draw gave 124 rows. For each row the script found the source in the literature collection (`pub/lit-t1`) by DOI and cut the passage around the quote the way the second pass cut it: 64 came from full text and 60 from an abstract only.

I read each passage and asked the brief's question. The brief says that `taxon` is the species actually measured, that a value from a review is graded by what the review reports, and that `m` means measured in this creature or in the typical members of the group the record names. So a review's table row for *Apis mellifera* reports a measurement on *Apis mellifera*, and its grade is `m`. A row was judged too strict when the passage puts the measurement in the record's own taxon, whoever made it. It was judged right when the passage puts the measurement in another taxon: one member or a narrower group standing for a wider record, a wider group standing for a narrower one, or a relative. Every verdict, with the words that decided it, is in `sample-judgments.jsonl`.

The same draw took 37 of the 146 `g`-to-`m` corrections (two a unit at least, so the share came to 37 where the prompt asked for about 30).

## Counts

Of the 124 `m`-to-`g` rows, 109 are too strict (88%), 14 are right and 1 is wrong for another reason.

The 109 too strict rows fall into four kinds. In 88 the passage is a review, a compiled table or a cited study whose measurement is on the record's own species. In 12 the passage states a fact about the typical members of the group the record names ("bees possess three small lens eyes"). In 7 the passage names the study animal by its common name ("six pigeons", "corn plants"). In 2 it names it by its genus (*Deilephila* for *D. elpenor*). The row wrong for another reason is `bee:141`, a false-colour convention for photographs, which describes a way of drawing and measures nothing in bees.

Of the 37 `g`-to-`m` rows, all 37 are right: each passage puts the study's own measurement in the record's taxon, and in three of them the second pass also corrected the taxon to the animals actually measured.

## Ten rows the rule graded too strictly

- `bee:214`, Apis mellifera, `lambda_max_nm` 436. 'The honeybee eye contains three types of photoreceptors ... M ... 436 nm ... (Menzel and Backhaus 1991)': the review reports a measurement on the honeybee itself.
- `herps-met:19`, Bufo bufo, `lambda_max_nm` 502. 'Bufo bufo | 502 | 432 | ... | Govardovskii et al. (2000)': a compiled measurement on the record's species.
- `insect:314`, Melanophila acuminata, `cff_hz` 400. 'the highest value of 400 Hz for the black fire beetle (Melanophila acuminate)': a compiled measurement on the record's species.
- `cat-dog:13`, Homo sapiens, `cff_hz` 60. 'Human | Homo sapiens | Homo | Mammalia | High | Behavioural | 60.0 | [70]': a compiled measurement on people.
- `mammal-groups:13`, Megaptera novaeangliae, `lambda_max_nm` 492. 'made by Dartnall on the humpback whale (maximum sensitivity of 492 nm; Dartnall, 1962)': the cited study measured the record's species.
- `birds:95`, Columba livia, `cff_hz` 140. 'Dodt's and Wirth's [12] electroretinograms (ERGs) reaching about 140 Hz in the pigeon, Columba livia': the cited study measured the record's species.
- `bee:132`, Apidae, `eyes_count` 3. 'bees possess three small lens eyes, called ocelli': a statement about the typical members of the record's group.
- `sea-invertebrates:65`, Cephalopoda (coleoids), `receptor_classes` 1. 'Cephalopods ... Their advanced camera-type eyes use only a single type of visual pigment': the typical members of the record's group.
- `birds:131`, Columba livia, `acuity_cpd` [7.5, 25.9]. 'six pigeons ... thresholds ... 1.16 to 4.0 min of arc': a primary study on pigeons; 'pigeon' names the record's species.
- `insect:364`, Deilephila elpenor, `colour_vision` "colour seen at light levels 100 times dimmer than a pers.... 'proving that Deilephila not only has colour vision': the experiment the review describes used the record's species, and the genus name refers to it.

## Ten rows the rule graded rightly

- `fish-shark:20`, Selachimorpha, `colour_vision` "every shark studied to date has a single spectral class .... 'All sharks studied to date' and 'the visual pigments of only a handful': a few species stand for the whole group.
- `fish-shark:26`, Batoidea, `receptor_classes` 2. 'many rays (Batoidea) express ... 2 spectrally distinct classes of cone': the claim covers many rays, a share of the superorder that the passage leaves open.
- `ground-invertebrates:55`, Opiliones, `behaviour_vision` "negative phototaxis in laboratory tests; many nocturnal,.... 'species of Phalangida show negative phototaxis': a narrower group than Opiliones.
- `ground-invertebrates:124`, Serpulidae, `eye_role` "silhouette-detecting burglar alarm that triggers rapid w.... 'the eyes of Spirobranchus corniculatus ... absorbs light maximally at 464 nm': one species stands for the family.
- `insect:469`, Cataglyphis, `behaviour_vision` "routes learned by sight, without trail pheromones; panor.... 'Desert ants traveling between their nest and a food site': several genera are called desert ants, and the abstract does not say which was studied.
- `insect:444`, Odonata, `eye_role` "ocelli act as equilibrium organs in flight (dorsal light.... 'dragonflies with occluded ocelli': one study on dragonflies stands for the whole order.
- `insect:349`, Odonata, `acceptance_deg` "median ocellus photoreceptors 15 deg vertical x 28 deg h.... 'acceptance angles of 15 degrees and 28 degrees' in 'the dragonfly': one species stands for the order.
- `insect:457`, Lepidoptera (caterpillars), `eyes_count` "six stemmata on each side in a saturniid caterpillar (Ma.... 'a satumiid caterpillar ... globuli quidam, numero sex': one caterpillar stands for the order.
- `jumper:182`, Phidippus regius, `colour_vision` "described as a presumed dichromat, while Habronattus tri.... 'Phidippus regius is a presumed dichromat [41]': 'presumed' marks an inference, which the passage does not tie to a measurement on this species.
- `spider:133`, Deinopis spinosa, `rhabdom_um` [20, 110]. 'spiders within the genus Deinopis ... huge photoreceptors (20 μm wide, 110 μm long27)': a genus-level figure from a cited study whose species the passage does not give.

## The rule decided

More than 15% of the sample is too strict, so the rule is narrowed. A correction from `m` to `g` keeps its `g` only when the second pass's reason names a taxon mismatch: a narrower or wider group, one species or one member standing for a group, a handful of species, a relative or congener, a claim for a whole group from part of it, a presumption or hypothesis, a genus-level figure, a taxon the reason itself corrects, or a value borrowed from another animal. Every other correction from `m` to `g` keeps the grade `m`. Those are the reviews, compilations and cited studies that report a measurement on the record's own taxon, the statements about a group's typical members, and the passages that call the study animal by a common or genus name. The second pass's other corrections to the same records (value, quote, note, trait) still apply.

The rule is `keep_g` in `tools/views/audit_rule.py`, a pattern over the stored `reason`. On the sample it agrees with the reading in 117 of 124 rows. It keeps `g` on five rows I read as too strict (`ground-invertebrates:133`, `herps:44`, `methods:42`, `sea-invertebrates:78` and `squirrel-deer-rabbit:77`, whose reasons say "a wider", "borrowed from" or "not the whole" where the passage in fact names the record's taxon) and sends two rows to `m` that I read as right or otherwise wrong (`bee:141` and `plant-fungus-slime:53`). No API was used.

Applied to all 820, the rule keeps 53 at `g` and returns 767 to `m`. The 146 corrections from `g` to `m` and the 9 other grade changes stand as the second pass made them.

## The application

`tools/views/audit_rule.py` writes `decisions.jsonl`, one line for each of the 767 records, setting the grade back to `m`. `tools/views/apply_audit.py` now takes `--decisions`: it sets those fields on the corrected record before applying it, and when the record then equals the log line it copies the line unchanged and marks it `correct_declined`. Its test covers both cases and a decision that points at a row that is no correction.

The corrected copies are in `corrected/<unit>.jsonl`, one for each of the 20 logs `ALL.jsonl` covers. The 18 research logs were read from the heads of their `research/<unit>` branches on 14 October and the two sweep logs from `main`; every audit row matched its log line, so no row was skipped as stale. No log was edited.

```
python3 -I tools/views/audit_rule.py
python3 -I tools/views/apply_audit.py LOG --all docs/views/audit/ALL.jsonl --decisions docs/views/audit/decisions.jsonl --out docs/views/audit/corrected/<unit>.jsonl
```

With the decisions, 208 records change grade, where 975 would have before. Of the 1,152 corrections, 460 records change in some field and 692 are declined, since their only change was the grade the rule now keeps.

| unit | grade changes in `ALL.jsonl` | `m` to `g` kept | `m` to `g` back to `m` | `g` to `m` | other grade changes | grade changes now | records changed now | corrections declined |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| bee | 71 | 4 | 62 | 5 | 0 | 9 | 32 | 52 |
| birds | 35 | 1 | 16 | 17 | 1 | 19 | 33 | 13 |
| birds-met | 2 | 0 | 0 | 2 | 0 | 2 | 5 | 0 |
| cat-dog | 11 | 1 | 10 | 0 | 0 | 1 | 7 | 7 |
| fish-shark | 27 | 3 | 12 | 12 | 0 | 15 | 30 | 10 |
| ground-invertebrates | 58 | 12 | 33 | 13 | 0 | 25 | 53 | 21 |
| herps | 54 | 4 | 6 | 44 | 0 | 48 | 69 | 3 |
| herps-met | 27 | 0 | 22 | 5 | 0 | 5 | 14 | 16 |
| insect | 148 | 12 | 131 | 1 | 4 | 17 | 39 | 127 |
| insects-met | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 |
| jumper | 13 | 1 | 6 | 5 | 1 | 7 | 19 | 5 |
| mammal-groups | 15 | 2 | 13 | 0 | 0 | 2 | 12 | 12 |
| mammals-met | 2 | 0 | 1 | 1 | 0 | 1 | 2 | 1 |
| methods | 340 | 1 | 338 | 0 | 1 | 2 | 4 | 338 |
| plant-fungus-slime | 48 | 5 | 31 | 12 | 0 | 17 | 34 | 23 |
| sea-invertebrates | 59 | 5 | 51 | 2 | 1 | 8 | 37 | 41 |
| spider | 24 | 1 | 1 | 21 | 1 | 23 | 38 | 0 |
| squirrel-deer-rabbit | 41 | 1 | 34 | 6 | 0 | 7 | 28 | 23 |
| sweep-21 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| sweep-25 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **all** | 975 | 53 | 767 | 146 | 9 | 208 | 460 | 692 |
