# The rows pass: voice check and drafts

Written by `tools/views/voice_check.py` and `tools/views/rows.py`; each tool owns one block.

<!-- voice-check:start -->
## Voice check

`tools/views/voice_check.py` read 444 rows in 44 views (a row held in both a view's own list and its trial list counts once).
341 rows (77%) break at least one rule that a script can see; 1139 findings in all.

### By rule

| rule | findings |
|---|---:|
| humans | 46 |
| app | 614 |
| voice_words | 14 |
| banned | 0 |
| contrast | 0 |
| fragment | 7 |
| spelling | 156 |
| length | 4 |
| numbers | 159 |
| dash | 0 |
| hedge | 0 |
| grade_words | 139 |

### By view

| view | rows flagged | humans | app | voice_words | banned | contrast | fragment | spelling | length | numbers | dash | hedge | grade_words |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cat | 16 | 5 | 33 | 1 |  |  |  | 6 |  | 3 |  |  | 8 |
| jumper | 13 | 1 | 35 | 5 |  |  |  | 4 |  | 1 |  |  | 3 |
| whale | 8 | 2 | 19 |  |  |  |  | 9 | 2 | 9 |  |  | 3 |
| bee | 11 | 3 | 25 |  |  |  |  | 4 |  | 6 |  |  | 4 |
| bird | 10 | 2 | 21 |  |  |  |  | 1 |  | 12 |  |  | 5 |
| deer | 10 | 2 | 21 | 1 |  |  |  | 6 |  | 3 |  |  | 4 |
| fish | 11 |  | 19 |  |  |  |  | 2 |  | 10 |  |  | 6 |
| insect | 10 | 3 | 18 |  |  |  |  | 2 |  | 6 |  |  | 7 |
| dog | 8 | 3 | 20 |  |  |  |  | 5 |  | 2 |  |  | 4 |
| fox | 7 | 2 | 21 |  |  |  |  | 7 |  | 1 |  |  | 1 |
| salamander | 10 |  | 19 |  |  |  |  | 10 |  | 1 |  |  | 2 |
| fungus | 10 |  | 16 | 2 |  |  |  | 5 |  |  |  |  | 8 |
| owl | 7 | 2 | 22 |  |  |  | 2 | 4 |  |  |  |  | 1 |
| cephalopod | 8 | 3 | 11 |  |  |  |  | 3 | 1 | 8 |  |  | 3 |
| hawk | 7 | 2 | 11 |  |  |  |  | 1 |  | 12 |  |  | 3 |
| reef | 8 |  | 22 |  |  |  |  | 4 |  |  |  |  | 3 |
| shark | 8 |  | 23 |  |  |  |  | 4 |  | 1 |  |  | 1 |
| spider | 7 |  | 18 |  |  |  | 1 | 1 | 1 | 2 |  |  | 5 |
| bigcat | 7 | 4 | 17 |  |  |  |  | 6 |  |  |  |  |  |
| sealife | 10 |  | 14 |  |  |  |  | 4 |  | 3 |  |  | 6 |
| squirrel | 8 | 1 | 10 |  |  |  |  | 4 |  | 10 |  |  | 2 |
| alligator | 7 | 1 | 9 |  |  |  |  | 2 |  | 10 |  |  | 4 |
| bat | 10 |  | 14 |  |  |  |  | 5 |  | 3 |  |  | 4 |
| tick | 7 |  | 11 |  |  |  |  | 6 |  | 4 |  |  | 5 |
| primate | 5 | 3 | 9 |  |  |  |  | 5 |  | 5 |  |  | 3 |
| frog | 10 | 1 | 11 |  |  |  | 1 |  |  | 8 |  |  | 2 |
| mammal | 8 | 1 | 10 |  |  |  |  | 5 |  | 4 |  |  | 3 |
| duck | 7 | 2 | 16 |  |  |  |  | 2 |  | 1 |  |  | 1 |
| rabbit | 9 |  | 8 | 1 |  |  | 1 | 4 |  | 7 |  |  | 1 |
| snail | 9 |  | 9 |  |  |  |  | 7 |  | 1 |  |  | 4 |
| worm | 6 |  | 11 | 2 |  |  |  | 4 |  | 1 |  |  | 3 |
| scorpion | 8 |  | 11 |  |  |  | 1 | 2 |  | 2 |  |  | 4 |
| millipede | 5 | 1 | 12 |  |  |  |  | 3 |  |  |  |  | 3 |
| centipede | 6 |  | 13 |  |  |  |  | 2 |  | 1 |  |  | 2 |
| slime | 5 |  | 10 | 1 |  |  |  | 3 |  |  |  |  | 4 |
| plant | 5 | 1 | 7 |  |  |  |  | 4 |  | 2 |  |  | 3 |
| crab | 8 |  | 8 | 1 |  |  |  | 2 |  | 3 |  |  | 2 |
| wader | 8 | 1 | 7 |  |  |  |  |  |  | 6 |  |  | 2 |
| flyingfox | 7 |  | 6 |  |  |  |  | 5 |  |  |  |  | 4 |
| woodlouse | 6 |  | 7 |  |  |  |  | 2 |  | 2 |  |  | 4 |
| reptile | 6 |  | 2 |  |  |  |  |  |  | 9 |  |  |  |
| harvestman | 3 |  | 7 |  |  |  |  | 1 |  |  |  |  | 1 |
| other | 1 |  | 1 |  |  |  |  |  |  |  |  |  | 1 |
| person | 1 |  |  |  |  |  | 1 |  |  |  |  |  |  |
<!-- voice-check:end -->

<!-- rows-pipeline:start -->
## Rows pipeline (burst 10)

`tools/views/rows.py` drafted 49 rows of 14 views with claude-sonnet-5-5, from 20371 evidence records (the audit and the burst 9 decisions applied). Spent $0.73 at batch prices.

A draft passes when `voice_check.py` finds nothing in it, every number in it is in a record it cites, and the records cited belong to a species of the view or a relative of one. A draft that fails is sent once more with the errors; what still fails is listed. The first eight views are the ones with the most evidence records; the rest followed.

| view | rows | passed first time | passed after the retry | failed |
|---|---:|---:|---:|---:|
| bird | 4 | 2 | 2 | 0 |
| insect | 3 | 2 | 1 | 0 |
| jumper | 7 | 5 | 2 | 0 |
| dog | 4 | 2 | 2 | 0 |
| bee | 4 | 3 | 0 | 1 |
| plant | 3 | 1 | 2 | 0 |
| alligator | 4 | 3 | 1 | 0 |
| deer | 4 | 0 | 4 | 0 |
| frog | 3 | 1 | 2 | 0 |
| hawk | 3 | 2 | 1 | 0 |
| rabbit | 1 | 0 | 1 | 0 |
| reptile | 1 | 0 | 1 | 0 |
| squirrel | 3 | 2 | 1 | 0 |
| wader | 5 | 2 | 3 | 0 |
| the first eight | 25 | 15 (60%) | 9 | 1 |
| all | 49 | 25 (51%) | 23 | 1 |

Pass rate on the first attempt: 51%. After the retry: 98%.

### Rows that failed the first time, and why

The reasons are found again by checking the batch's first replies with the checker as it stands now, which no longer counts 'slider' (a turtle) or 'camera-type eye' as talk about the app; the reptile row that this fixed still shows as passing only on its second attempt in the counts above.

- **alligator, Pupil**: voice check voice_words: report
- **bee, Red**: voice check contrast: Y, not X: None of them peaks in red, not even in the large red-tailed bumblebee.
- **bird, Sharpness**: voice check voice_words: reports; voice check length: 4 sentences
- **bird, Ultraviolet**: voice check voice_words: reports
- **deer, Color**: voice check voice_words: reports
- **deer, Field of view**: voice check app: view; voice check voice_words: reports
- **deer, Pupil**: the number 13 is in none of the cited records
- **deer, Sharpness, dim light and depth**: voice check voice_words: reports
- **dog, Field of view, dim light and depth**: voice check numbers: 539
- **dog, Sharpness**: voice check voice_words: reports
- **frog, Movement**: voice check voice_words: reports
- **frog, Speed**: voice check voice_words: reports
- **hawk, Sharpness**: voice check voice_words: reports; voice check numbers: 33; voice check numbers: 138
- **insect, Sharpness**: voice check voice_words: reports; voice check numbers: 0.7; voice check numbers: 0.5
- **jumper, Eye movement**: voice check app: view; voice check app: this view; voice check app: last sentence: Of the jumping spiders that borrow this view, only the bold 
- **jumper, Sharpness**: the number 60 is in none of the cited records
- **plant, Green and time**: voice check voice_words: reports
- **plant, Neighbors**: voice check voice_words: reports; voice check voice_words: reports
- **rabbit, The whole view**: voice check voice_words: reports; voice check grade_words: an i row that does not say that nobody knows
- **reptile, The whole view**: voice check voice_words: reports
- **squirrel, Speed**: voice check voice_words: reports
- **wader, Head movement**: voice check spelling: grey
- **wader, Sharpness**: voice check voice_words: reports
- **wader, Speed**: voice check voice_words: reports

### Rows that still fail after the retry

- **bee, Red** (grade g): voice check voice_words: reports
  - last draft: In the honey bee, three kinds of color-sensing cell have been measured, peaking in ultraviolet, blue and green, and a review reports the same three kinds in the buff-tailed bumblebee, the large red-tailed bumblebee and the European wool carder bee. None of the three kinds peaks in red, even in the large red-tailed bumblebee. If you are another bee, you very likely have these same three kinds.

### Ten drafts beside the live rows

**bird, Ultraviolet** (draft grade `g`; of the species' records 0% measured, 50% carried, 50% unknown)

- Draft: Ultraviolet is light that humans cannot see at all. In the blue tit, the European starling and the Eurasian blackbird, one kind of color-sensing cell peaks in it, between 360 and 375 nanometers, and a review table gives 315 nanometers as the point where the blue tit's lens and cornea pass half the light, so if you are a songbird you very likely sense ultraviolet. If you are a mallard, the matching cell peaks at 415 nanometers, in violet, and if you are a cormorant you very likely get almost no ultraviolet, since the lens and cornea of the pied cormorant block it.
- Live: `g` Ultraviolet: A starling, a blue tit and a blackbird have a short-wave cone that peaks in the ultraviolet, between 360 and 375 nanometers, and gulls have the same type. A mallard, a pigeon and a chicken have the violet type instead, which peaks between 410 and 420. If you are a duck or a vulture, you very likely see little ultraviolet, and if you are a songbird or a gull, you very likely see it.
- Cites: birds#17 (Cyanistes caeruleus), birds-met#21 (Sturnus vulgaris), birds-met#25 (Turdus merula), recheck-5-fixed#13 (Cyanistes caeruleus), birds#1 (Anas platyrhynchos), recheck-5-fixed#11 (Phalacrocorax varius)

**dog, Color** (draft grade `m`; of the species' records 42% measured, 36% carried, 21% unknown)

- Draft: You have two kinds of color-sensing cell, where a human has three. This has been measured in the domestic dog, the red fox and the arctic fox, and each has two kinds.
- Live: `i` Colour: Dogs have two kinds of colour-sensing cells, where people have three. This view shows colours as a person with two kinds would see them.
- Cites: cat-dog#64 (Canis lupus familiaris), cat-dog#40 (Vulpes vulpes), intake-4#12 (Vulpes lagopus)

**bee, Speed** (draft grade `i`; of the species' records 0% measured, 26% carried, 74% unknown)

- Draft: If you are a honeybee, a lamp that looks steady to a human can look like it is flashing to you, because you can see flicker up to about 200 flashes a second, where a human stops at about 60. If you are a bumblebee, you very likely see flicker up to about 130 flashes a second, since that is what was measured in a relative, Bombus hortorum. If you are any other kind of bee or a wasp, nobody has measured how fast you see.
- Live: `m` Speed: In bright light, a honeybee can see a light flicker up to 200 times a second, where people stop at about 60. This view runs slowly and then jumps ahead to suggest the difference.
- Cites: bee#156 (Apis mellifera), bee#262 (Bombus hortorum)

**insect, Ultraviolet** (draft grade `g`; of the species' records 2% measured, 62% carried, 37% unknown)

- Draft: Ultraviolet is light that humans cannot see at all. In the monarch, the cabbage white, the small tortoiseshell, the drone fly, the seven-spotted ladybird beetle and the green darner dragonfly, one kind of color-sensing cell is most sensitive to ultraviolet, and you very likely have such a cell too.
- Live: `i` Ultraviolet: Bees and some other insects can see ultraviolet light, which people can’t. Phone cameras capture very little of it, so the violet tint in this view stands in for it.
- Cites: insect#8 (Danaus plexippus), insect#24 (Pieris rapae crucivora), methods#476 (Aglais urticae), insect#167 (Eristalis tenax), insect#190 (Coccinella septempunctata), insect#109 (Anax junius)

**jumper, Color** (draft grade `i`; of the species' records 0% measured, 22% carried, 78% unknown)

- Draft: In every jumping spider measured, the big front eyes have cells that sense ultraviolet and cells that sense green. A regal jumping spider has three kinds of color-sensing cell, and Habronattus pyrrithrix gets a third color channel, for red, only in a small patch at the center of the retina, while Plexippus validus has just two kinds. Nobody has measured how many kinds of color-sensing cell you have unless you are one of those species.
- Live: `m` Colour: Most jumping spiders, Phidippus among them, see ultraviolet and green. Habronattus also sees red, in a small patch at the centre of each front eye, and this view adds red there when it knows the genus.
- Cites: jumper#102 (Habronattus pyrrithrix), jumper#106 (Habronattus pyrrithrix), jumper#107 (Habronattus pyrrithrix), jumper#12 (Saitis barbipes), jumper#163 (Phidippus regius), jumper#165 (Phidippus regius), jumper#21 (Plexippus validus)

**plant, Neighbors** (draft grade `i`; of the species' records 1% measured, 0% carried, 99% unknown)

- Draft: If you are a wood strawberry, you sense red and far-red light with a protein called phytochrome B, and according to a review, your daughter plants grow more root over live ground than over dead ground. If you are a common selfheal, a review found that strong far-red light slowed the growth of your plantlets in a lab. For most of you, nobody has measured whether you sense a neighbor by its light or by its scent.
- Live: `m` Neighbours: Plants compare red light with far-red light, a colour just past the edge of what people can see. The balance tells a plant that a neighbour is growing close by, even before the neighbour shades it. Phone cameras capture very little far-red light.
- Cites: harvest-11#2 (Fragaria vesca), harvest-13#7 (Fragaria vesca), harvest-15#1 (Prunella vulgaris)

**deer, Field of view** (draft grade `i`; of the species' records 2% measured, 6% carried, 92% unknown)

- Draft: Your eyes sit on the sides of your head, and a book on deer says they let you watch almost a complete circle, about 310 degrees. The book does not say how that was found, and nobody has measured how much of the space around you both of your eyes see at once. In goats, which are not deer, a review states a field of 320 to 340 degrees, with 20 to 60 degrees seen by both eyes together.
- Live: `g` Field of view: Reindeer grazing with their eyes turned level are given a combined field of about 360 degrees along the ground, and horses a field of about 320. Nobody has measured the field of a white-tailed deer, so you very likely see most of the way around you without turning your head.
- Cites: squirrel-deer-rabbit#120 (Cervidae (deer, as the page states it)), intake-5#31 (Capra hircus), intake-5#32 (Capra hircus)
<!-- rows-pipeline:end -->

<!-- burst10-before-after:start -->

### Before and after the four corrections (burst 10)

The same checker run over the views on main before the corrections and over the corrected views. The corrections changed five rows (deer, wader, bird, squirrel and bigcat) in the five views and added one (the clouded leopard).

| | rows read | rows flagged | findings | humans | app | voice_words | banned | contrast | fragment | spelling | length | numbers | dash | hedge | grade_words |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| before | 443 | 346 | 1168 | 50 | 635 | 14 | 0 | 0 | 7 | 156 | 4 | 160 | 0 | 0 | 142 |
| after | 444 | 341 | 1139 | 46 | 614 | 14 | 0 | 0 | 7 | 156 | 4 | 159 | 0 | 0 | 139 |
<!-- burst10-before-after:end -->

<!-- live-disagreement:start -->
## Live rows against the evidence (burst 11b)

`tools/views/rows_live.py` sets each live row beside the evidence. The grade is the one `rows.py` computes for the row (the grade most of the species' records fall under, the carry rules applied; partial records count as measured). A value is flagged when a number of 10 or more in the live text is in no record of the row's traits for a species of the view or a relative of one (a flag is a prompt to read the row, not a verdict, since a row may rest on a paper outside the evidence logs). No live row was changed.

| view | live rows | compared | grade differs | a number unsupported |
|---|---:|---:|---:|---:|
| alligator | 4 | 4 | 3 | 0 |
| bee | 5 | 4 | 3 | 0 |
| bird | 4 | 4 | 2 | 0 |
| cat | 7 | 7 | 4 | 0 |
| deer | 4 | 4 | 3 | 0 |
| dog | 4 | 4 | 2 | 0 |
| frog | 3 | 3 | 2 | 0 |
| hawk | 3 | 3 | 2 | 0 |
| insect | 3 | 3 | 3 | 0 |
| jumper | 14 | 1 | 1 | 0 |
| plant | 3 | 3 | 2 | 0 |
| rabbit | 1 | 1 | 0 | 0 |
| reptile | 1 | 1 | 0 | 0 |
| spider | 8 | 4 | 4 | 0 |
| squirrel | 3 | 3 | 1 | 0 |
| wader | 5 | 5 | 4 | 0 |
| bat | 10 | 9 | 7 | 0 |
| bigcat | 9 | 9 | 3 | 1 |
| centipede | 8 | 7 | 5 | 0 |
| cephalopod | 8 | 7 | 5 | 0 |
| crab | 9 | 9 | 7 | 0 |
| duck | 8 | 7 | 3 | 0 |
| fish | 11 | 7 | 5 | 0 |
| flyingfox | 8 | 7 | 3 | 1 |
| fox | 8 | 6 | 1 | 1 |
| fungus | 13 | 9 | 7 | 1 |
| harvestman | 7 | 6 | 4 | 0 |
| mammal | 10 | 9 | 6 | 2 |
| millipede | 8 | 7 | 6 | 0 |
| owl | 9 | 7 | 5 | 1 |
| primate | 6 | 5 | 4 | 1 |
| reef | 8 | 5 | 4 | 0 |
| salamander | 11 | 10 | 4 | 1 |
| scorpion | 8 | 6 | 5 | 0 |
| sealife | 13 | 11 | 6 | 3 |
| shark | 8 | 7 | 6 | 0 |
| slime | 8 | 5 | 4 | 0 |
| snail | 11 | 9 | 6 | 2 |
| tick | 9 | 9 | 8 | 2 |
| whale | 8 | 6 | 5 | 1 |
| woodlouse | 9 | 7 | 5 | 1 |
| worm | 9 | 7 | 6 | 0 |
| all | 306 | 247 | 166 | 18 |

### The rows that differ

| view | row | live grade | evidence grade (shares m / g / i) | numbers not found | live text |
|---|---|---|---|---|---|
| alligator | Sharpest spot | g | i (12 / 5 / 83%) | - | Crocodiles see most sharply along a band level with the horizon. It lets them scan the waterline without turning their heads. |
| alligator | Colour | g | m (63 / 23 / 14%) | - | Crocodiles have three kinds of colour-sensing cells, as people do, so this view leaves colours as your camera shows them. |
| alligator | Pupil | g | m (63 / 0 / 37%) | - | An alligator’s pupil is a vertical slit. It smears out-of-focus things up and down, and this view does the same. |
| bee | Sharpness | g | i (18 / 33 / 50%) | - | Most insects see less than a sixtieth as much detail as people do. |
| bee | Red | m | g (27 / 37 / 36%) | - | Bees have no colour-sensing cells for red, so red flowers and objects look dark to them. |
| bee | Speed | m | i (0 / 26 / 74%) | - | In bright light, a honeybee can see a light flicker up to 200 times a second, where people stop at about 60. This view runs slowly and then jumps ahead to sugge |
| bird | Speed | g | i (4 / 1 / 95%) | - | Birds can see a light flicker 40 to 140 times a second, and the fastest fliers are at the top of that range. People see flicker up to about 60 times a second. T |
| bird | Sharpness | g | i (0 / 0 / 100%) | - | Most birds see half as much detail as people do, or less. |
| cat | Sharpness | m | i (38 / 2 / 60%) | - | Cats see about a fifth to a tenth as much detail as people do. This view is blurred to match. |
| cat | Colour | m | i (35 / 4 / 60%) | - | Cats have two kinds of colour-sensing cells in their eyes, where people have three. Reds and greens are hard for them to tell apart, so reds look olive or grey  |
| cat | Field of view | m | i (35 / 2 / 63%) | - | A cat takes in about 200 degrees around itself, and a person about 180. A phone camera sees far less than either, so this view bends the picture at its edges to |
| cat | Dim light | m | i (35 / 0 / 65%) | - | Cats can see in light six to eight times dimmer than people need. This view brightens the shadows to show it. |
| deer | Colour | m | g (32 / 65 / 3%) | - | White-tailed deer have two kinds of colour-sensing cells, where people have three. Reds and oranges look yellow or grey to them. |
| deer | Field of view | g | i (2 / 6 / 92%) | - | Reindeer grazing with their eyes turned level are given a combined field of about 360 degrees along the ground, and horses a field of about 320. Nobody has meas |
| deer | Pupil | g | m (48 / 7 / 45%) | - | Grazing animals have pupils shaped like horizontal bars. The shape widens their view along the ground and cuts glare from the sky. It also smears out-of-focus t |
| dog | Sharpest spot | m | i (42 / 0 / 58%) | - | Dogs with long noses see most sharply along a band level with the horizon. Dogs with short noses see most sharply in one central spot. This view shows the band. |
| dog | Colour | i | m (42 / 36 / 21%) | - | Dogs have two kinds of colour-sensing cells, where people have three. This view shows colours as a person with two kinds would see them. |
| frog | Movement | m | i (10 / 18 / 71%) | - | A frog takes little notice of the parts of its world that stay still, and it can starve beside food that never moves. This view shows only what changes, so hold |
| frog | Speed | g | i (1 / 2 / 97%) | - | A cane toad can see a light flicker only about 7 times a second, a ninth as often as a person can. Anything that moves smears into a trail. |
| hawk | Sharpness | g | i (0 / 0 / 100%) | - | Eagles see more than twice as much detail as people do. A phone camera can’t capture that much detail, so this view magnifies the centre to suggest it. |
| hawk | Speed | m | i (3 / 12 / 85%) | - | A peregrine falcon can see a light flicker up to 129 times a second, and a Harris’s hawk up to 77. People see flicker up to 50 or 60 times a second. This view r |
| insect | Sharpness | g | i (4 / 8 / 88%) | - | Most insects see less than a sixtieth as much detail as people do. |
| insect | Speed | g | i (0 / 0 / 100%) | - | Flies and dragonflies can see a light flicker more than 100 times a second, and one beetle up to 400. People stop at about 60. This view runs slowly and then ju |
| insect | Ultraviolet | i | g (2 / 62 / 37%) | - | Bees and some other insects can see ultraviolet light, which people can’t. Phone cameras capture very little of it, so the violet tint in this view stands in fo |
| jumper | Colour | m | i (0 / 31 / 69%) | - | Most jumping spiders, Phidippus among them, see ultraviolet and green. Habronattus also sees red, in a small patch at the centre of each front eye, and this vie |
| plant | No picture | g | i (0 / 0 / 100%) | - | A plant has nothing like a lens to focus light into an image. It senses how much light there is, what colour it is, and which direction it comes from. |
| plant | Neighbours | m | i (1 / 0 / 99%) | - | Plants compare red light with far-red light, a colour just past the edge of what people can see. The balance tells a plant that a neighbour is growing close by, |
| spider | The web | m | i (22 / 0 / 78%) | - | A Golden Silk Spider feels its prey through the silk, and a trapped insect shakes the web 5 to 30 times a second. The shaking arrives ten to thirty times strong |
| spider | Eyes | g | i (0 / 0 / 100%) | - | Most spiders have eight eyes and few see well. Most register little more than changes between light and dark, and spiders that build webs lean on the shaking of |
| spider | Sharpness | g | i (0 / 0 / 100%) | - | A wandering spider resolves nothing finer than about 2 degrees, under a hundredth of your sharpness. The picture borrows that figure for web builders. |
| spider | Pace | g | i (0 / 0 / 100%) | - | A wandering spider stops following flicker between 4.3 and 8.6 times a second, a seventh of your rate or less, so movement smears into trails. |
| squirrel | Speed | g | i (13 / 12 / 75%) | - | A golden-mantled ground squirrel can follow a light flickering at more than 100 times a second, and a yellow-pine chipmunk does about the same. An American red  |
| wader | Head movement | m | i (11 / 3 / 86%) | - | Herons, egrets, cranes, pigeons and chickens hold their heads still while they walk, so their eyes stay fixed on the world. Then the head darts forward to catch |
| wader | Speed | g | i (7 / 3 / 91%) | - | In pigeons, each dart forward takes about a tenth of a second. |
| wader | Sharpness | g | i (0 / 0 / 100%) | - | Most birds see half as much detail as people do, or less. |
| wader | Ultraviolet | g | i (0 / 0 / 100%) | - | A whooping crane’s shortest-wave cone peaks near 405 nanometers and a pigeon’s near 410, both in the violet. The gene for that cone is the violet type in a gray |
| bat | Calls | m | i (21 / 0 / 79%) | - | A big brown bat calls 5 to 10 times a second while searching, 20 to 80 times while closing in, and up to about 170 times in the final buzz. Each call returns on |
| bat | Distance | m | i (21 / 0 / 79%) | - | From the delay of each echo, a big brown bat judges distance to within about 1.5 centimetres with its short hunting calls, and only to 15 centimetres or worse w |
| bat | Reach | g | i (21 / 0 / 79%) | - | A bat hears an insect’s echo from about 2 to 14 metres away, depending on the bat and the insect, and a forest edge from up to about 50 metres. Beyond that, its |
| bat | Direction | m | i (21 / 0 / 79%) | - | A big brown bat swings its beam of sound from one object to the next with an accuracy of about 5 degrees. The beam spreads over a cone of 60 to 90 degrees, abou |
| bat | Sharpness | g | i (13 / 16 / 71%) | - | Daubenton’s bat, an insect-eating relative, resolves about 0.6 cycles per degree to your 60, a hundredth of yours. The screen is blurred to match. |
| bat | Dim light | m | i (1 / 7 / 92%) | - | In one test a big brown bat could no longer tell things apart by sight once the light fell to between 0 and 0.0008 lux. Shadows are lifted to suggest it. |
| bat | Colour | g | i (0 / 0 / 100%) | - | Some bats have a cone for ultraviolet and some have lost it, and no phone records ultraviolet. In two leaf-nosed bats only 2 to 4 in a hundred light receptors a |
| bigcat | Clouded leopard | i | i (37 / 0 / 63%) | 200 | Nobody agrees on a clouded leopard’s pupil. A survey of more than 200 species lists it as a vertical slit, while a study of a preserved eye found it round at re |
| bigcat | Lens | m | i (0 / 0 / 100%) | - | A tiger's lens focuses every colour at the same depth, where a house cat's lens has zones for several. Why the large cats lack those zones is unknown. |
| bigcat | Colour | m | i (0 / 9 / 91%) | - | Lions, tigers, leopards and cheetahs have two kinds of colour-sensing cells, as house cats do, where people have three. This view shows colours the way a person |
| bigcat | Dim light | m | i (0 / 0 / 100%) | - | In a study of the eyes of three kinds of wild cat, the lions had the largest tapetum, the mirror-like layer behind the retina that gives light a second pass. Th |
| centipede | Eyes | m | i (33 / 0 / 67%) | - | The house centipede has a compound eye of about 150 to 200 facets on each side of its head. Most large tropical centipedes have four simple eyes on each side, a |
| centipede | Colour | m | i (33 / 0 / 67%) | - | The house centipede's eye is most sensitive to blue light near 448 nanometres and has a second peak in ultraviolet near 350. This view weights its grey toward b |
| centipede | Dark shapes | m | i (6 / 0 / 94%) | - | Centipedes run from light and toward dark shapes. The house centipede, the brown centipede and a large Scolopendra all head for a dark screen at the side of an  |
| centipede | Sunlight as heat | m | i (0 / 0 / 100%) | - | A large Asian centipede feels sunlight as heat in its antennae, which warm by more than 8 degrees Celsius within ten seconds of strong sun. |
| centipede | Soil centipedes | g | i (0 / 0 / 100%) | - | Soil centipedes are blind. In one of them every known gene for sensing light is missing, while the house centipede keeps those genes. |
| cephalopod | Colour | m | i (28 / 27 / 44%) | - | Almost all of these animals have a single visual pigment, with its peak between 470 and 500 nanometres, near 480 in octopus. With one pigment they cannot tell h |
| cephalopod | Field | g | i (0 / 17 / 83%) | - | Oval squid from three weeks old see about 323 degrees around themselves. One eye of a cuttlefish covers 253 degrees, and the two eyes of a cuttlefish overlap by |
| cephalopod | Where it is sharp | m | i (13 / 43 / 44%) | - | The receptors of an octopus are packed most densely in a horizontal stripe across the middle of the retina, about 55,000 per square millimetre against 18,000 to |
| cephalopod | Pupil | m | i (16 / 0 / 84%) | - | An octopus pupil is round in the dark and shrinks to a horizontal slit in bright light, down to about a tenth of its dark area. A cuttlefish can shrink its pupi |
| cephalopod | Flicker | g | i (32 / 32 / 37%) | - | A squid stops seeing flicker near 51 a second in dim light and a cuttlefish near 30. An octopus reaches 72 in bright light and only 20 when the light is far dim |
| crab | All around | g | i (0 / 0 / 100%) | - | A fiddler crab’s eyes stand on tall stalks and see the whole way around. The picture is squeezed and bent to suggest that. |
| crab | Sharpness | g | i (28 / 13 / 59%) | - | From side to side a fiddler crab’s facets point about 1.3 degrees apart, so it resolves about 0.4 cycles per degree to your 60. |
| crab | Colour | m | g (6 / 57 / 37%) | - | Most light cells in a crab’s eye share one pigment, most sensitive to blue-green near 500 nanometres, so reds go dark. Female fiddler crabs still pick a yellow  |
| crab | Ultraviolet | m | i (0 / 0 / 100%) | - | Female fiddler crabs prefer males whose claws reflect ultraviolet. A phone lens that was tested let through between a fifth and a hundredth of it, and the pictu |
| crab | Pace | m | i (0 / 0 / 100%) | - | In daylight a fiddler crab’s eye follows flicker to about 74 a second, a little past your 60. Once its eye has adapted to the dark, it follows only about 35 to  |
| crab | Night | m | i (0 / 1 / 99%) | - | At night a fiddler crab’s dark-adapted eye answers to light about a thousand times dimmer than the same dark-adapted eye does by day. |
| crab | Crayfish | m | i (0 / 0 / 100%) | - | Crayfish and slipper lobsters have superposition eyes, a design suited to dim water. A crayfish has one set of light cells most sensitive to violet and another  |
| duck | All the way around | m | i (34 / 11 / 55%) | - | A mallard sees all the way around itself and over its head. Its two eyes overlap in a narrow strip, about 22 degrees wide, that runs from the bill up over the c |
| duck | Colour | m | i (0 / 0 / 100%) | - | Ducks have four kinds of colour-sensing cells, one more than people, and the fourth responds to violet light. A mallard's eye blocks most ultraviolet light befo |
| duck | Sharpness | i | m (41 / 25 / 34%) | - | This part of the view is a guess. It assumes that a duck sees about a fifth as much detail as a person, the middle value for birds. |
| fish | Sharpness | m | i (13 / 15 / 72%) | - | A bluegill resolves about 5 cycles per degree and a pumpkinseed about 3.6, against your 60. The screen is blurred to what such an eye would keep of it. |
| fish | Colour | m | i (2 / 11 / 87%) | - | Largemouth bass have two cone types, near 535 and 614 nanometres, and none for blue. Trained bass confused blue with black and yellow-green with white, so for s |
| fish | Field | g | i (1 / 0 / 99%) | - | A golden shiner sees about 335 degrees around itself, 31 of them with both eyes, and is blind only in a wedge of 25 degrees behind. The camera holds a slice of  |
| fish | Where it is sharp | g | i (1 / 1 / 98%) | - | A golden shiner sees most sharply a little ahead and above, at 2.9 cycles per degree, and at 1.2 toward the edges. |
| fish | Pace | g | i (16 / 5 / 79%) | - | A spiny damselfish follows flicker to 89 a second, and the bony fish in one survey average 46. You stop near 60, so the picture keeps your pace. |
| flyingfox | No calls | m | i (0 / 0 / 100%) | - | Flying foxes make no echolocation calls and find their way by sight and smell. |
| flyingfox | Colour | m | g (0 / 66 / 34%) | - | Flying foxes have two cone types, a blue and a green, as most mammals do. Cones are about one in two hundred of their light receptors, so colour is muted here. |
| flyingfox | Dim light | g | i (0 / 0 / 100%) | 300,000, 800,000 | Bats pack 300,000 to 800,000 rods into each square millimetre of retina, two to five times your densest. Shadows are lifted to suggest it. |
| fox | Night eyes | m | i (0 / 0 / 100%) | - | A red fox's retina holds more rods for each cone than an Arctic fox's, the mark of an eye built for night in woodland. This view brightens the shadows. |
| fox | Hearing | x | m (71 / 0 / 29%) | 4,000 | A red fox hears sounds from about 51 to 48,000 vibrations a second, and at 4,000 a second its hearing is keener than a house cat's. This view leaves sound out. |
| fungus | No picture | g | i (4 / 0 / 96%) | - | A fungus has no eye. Its cells read how much light there is, mostly blue and green, and which way it comes from. |
| fungus | Colour | m | i (0 / 0 / 100%) | - | The young stalk of the split gill mushroom bends toward violet and green light and ignores orange and red. Another gilled mushroom, Coprinopsis cinerea, needs a |
| fungus | Red | g | i (0 / 0 / 100%) | - | Some moulds read red as well. Aspergillus nidulans uses phytochrome, the red receptor of plants, and red light holds back its sexual spores. The picture follows |
| fungus | Faint light | g | i (0 / 0 / 100%) | - | The stalk of the pin mould Phycomyces turns toward light as faint as a billionth of a watt on a square metre, and it still steers in light ten billion times bri |
| fungus | Down | m | i (4 / 0 / 96%) | - | A mushroom stem laid on its side starts to turn up in about 25 minutes, and its tip is upright again within 3 to 4 hours. The gills of a field mushroom turn bac |
| fungus | Pace | g | i (4 / 0 / 96%) | 15 | Genes that light switches on in the mould Neurospora peak 15 to 30 minutes later, and the pin mould stalk starts to bend within 5 minutes. Your eyes follow flic |
| fungus | Lichens | m | i (26 / 0 / 74%) | - | A lichen is a fungus with algae living inside it, and the algae make food from light. The orange lichen Xanthoria parietina makes a pigment, parietin, in its ou |
| harvestman | Eyes | m | i (0 / 0 / 100%) | - | A harvestman has a single pair of eyes, set back to back on a small turret in the middle of its body. Each eye looks out to one side. |
| harvestman | Rough images | m | i (0 / 0 / 100%) | - | A harvestman's eyes probably give only a rough picture of light and dark. A large dark object makes a species of Leiobunum flee, and in the laboratory harvestme |
| harvestman | Colour and dim light | g | i (0 / 0 / 100%) | - | In two cave harvestmen from New Zealand the eyes respond to ultraviolet, blue and green light, over a range of brightness of at least a hundred thousand to one. |
| harvestman | Touch and taste | m | i (0 / 0 / 100%) | - | Harvestmen find food, mates and enemies mostly by touching and tasting them with their first pair of legs and their palps, and they sense little from a distance |
| mammal | Colour | m | i (1 / 44 / 55%) | - | A domestic pig has two kinds of colour sensor, most sensitive near 439 and 556 nanometres, and you have three. We show colours the way a person with only two ki |
| mammal | Bears and otters | m | g (0 / 69 / 31%) | - | An American black bear has a blue-sensitive cone and a red-green one, with at least three red-green cones to each blue. Sea otters carry genes for the same pair |
| mammal | Kangaroos | m | g (1 / 99 / 0%) | - | The tammar wallaby, a small kangaroo, has only two kinds of cone. Some other Australian marsupials have a third. |
| mammal | Platypus and echidnas | g | i (14 / 0 / 86%) | - | The platypus and echidnas carry genes for two kinds of cone pigment, as most mammals do. |
| mammal | Sharpness | m | i (27 / 6 / 67%) | - | A tammar wallaby resolves about 4.8 cycles per degree, a twelfth of your 60. A western grey kangaroo’s retina could carry about 11. We blur the picture to about |
| mammal | Elephants | m | m (100 / 0 / 0%) | 11 | Asian elephants make out a gap of 8 to 11 minutes of arc near the tip of the trunk, about a tenth of your sharpness. One African elephant managed only 48 minute |
| mammal | Dim light | g | i (0 / 0 / 100%) | - | Bears, otters and other carnivores have a reflecting layer behind the retina that gives light a second pass. Pigs and red kangaroos have none, so the shadows ar |
| mammal | Electric sense | x | i (14 / 0 / 86%) | 50 | A platypus senses weak electric fields through its bill, down to about 50 millionths of a volt across a centimetre, and can find and avoid objects by them. No p |
| millipede | Eyes | m | i (0 / 0 / 100%) | - | Most millipedes have a small cluster of large-faceted eyes on each side of the head. The flat-backed millipedes, among them the greenhouse millipede, which is p |
| millipede | Sharpness | m | i (1 / 1 / 98%) | - | In behaviour tests the millipede Cylindroiulus punctatus made out a dark shape about 20 degrees wide, enough to find shelter and little more. A person sees deta |
| millipede | Light through the skin | m | i (20 / 0 / 80%) | - | The greenhouse millipede senses light through its skin. Light makes it walk more without steering it anywhere, so it keeps moving until it happens upon a dark p |
| millipede | Touch | m | i (0 / 0 / 100%) | - | A walking millipede taps the ground constantly with the tips of its antennae, and touch shapes most of what it does. |
| millipede | Taste and damp | m | i (0 / 0 / 100%) | - | A millipede tastes food by touching it, and in tests it showed no response to smells. Drying out keeps it walking, and once it settles on damp ground it is slow |
| millipede | Night | g | i (0 / 0 / 100%) | - | Many millipedes come out only at night. The luminous millipede Paraspirobolus lucifugus avoids light and keeps a daily clock. |
| owl | Eyes that face forward | m | i (3 / 22 / 75%) | - | An owl's eyes face forward, so their views overlap across about 45 degrees in front, more than in most birds. Its whole view spans about 200 degrees. |
| owl | Fixed eyes | m | i (4 / 27 / 68%) | - | An owl's eyes barely move in their sockets, by less than one degree, so the owl turns its whole head to look, as far as about 270 degrees. |
| owl | Night vision | m | i (3 / 22 / 75%) | - | A tawny owl's eye works close to the limit that any vertebrate eye can reach in dim light. This view brightens the shadows. |
| owl | Colour | m | i (3 / 22 / 75%) | - | Owls have lost the colour-sensing cells for violet and ultraviolet light that other birds have, and only about one cone in ten carries a coloured droplet of oil |
| owl | Hearing | m | i (3 / 0 / 97%) | 10,000 | Owls can find and catch prey by sound alone. A barn owl hears faint sounds about 20 decibels quieter than other birds can, and hears pitches above 10,000 vibrat |
| primate | Colour | m | i (1 / 40 / 60%) | - | A cynomolgus monkey has three kinds of cone, most sensitive near 430, 531 and 561 nanometres. Macaques share this three-cone plan with people and apes, so colou |
| primate | Other monkeys see less colour | g | i (0 / 39 / 60%) | - | Owl monkeys and bushbabies have a single kind of cone for medium and long light and lack colour vision. Male marmosets have two kinds of cone, and howler monkey |
| primate | Sharpness | m | g (20 / 41 / 38%) | - | Young rhesus monkeys reached 26.3 cycles per degree on a grating test, the highest value the test could assess. A marmoset's cone mosaic could carry about 30, a |
| primate | Field of view | i | i (0 / 0 / 100%) | 136 | No record gives a monkey's whole field of view. One skull model gives a chimpanzee-like eye socket a sideways reach of 115 degrees against 136 for a person, whi |
| primate | Night monkeys | m | i (0 / 0 / 100%) | - | The owl monkey is the only night-active monkey. Its retina is fully adapted to the dark and its fovea is only rudimentary. |
| reef | Colour | m | i (0 / 12 / 88%) | - | Damselfish, the family of the clownfish, have four kinds of colour-sensing cells, one of them for ultraviolet light, and many wear ultraviolet patterns that the |
| reef | Sharpness | m | i (6 / 14 / 80%) | - | Small reef fish see coarsely. An Ambon damselfish and a dottyback resolved about a fortieth as much detail as you do, though the cells in their eyes are packed  |
| reef | Eyes that move apart | m | i (1 / 1 / 98%) | - | Wrasses, blennies, pufferfish, triggerfish and seahorses can turn each eye on its own, and each eye has a small sharp centre, called a fovea. One eye can follow |
| reef | Pace | m | i (2 / 1 / 97%) | - | A squirrelfish, a reef fish that hunts at night, follows a flickering light up to 70 flashes a second in bright light, faster than you can, and only about 40 at |
| salamander | Ultraviolet | m | i (0 / 8 / 92%) | 40, 58 | Tiger salamanders and newts have cones tuned to ultraviolet light, which is invisible to you, near 360 nanometres in the tiger salamander and 340 to 360 in thre |
| salamander | Colour | m | i (13 / 4 / 83%) | - | The fire salamander snapped at a coloured worm dummy moving across a differently coloured background of equal brightness, so it tells colours apart by hue. Its  |
| salamander | Distance | m | i (8 / 2 / 90%) | - | The fire salamander refocuses its eyes before it turns to prey, and judges distance that way. The tongue-shooting lungless salamanders have eyes set forward, an |
| salamander | Night | g | i (35 / 28 / 37%) | - | Fire salamanders are active at night. A model of their eyes says they can tell a red throat from a yellow one by night light. |
| scorpion | All around | g | i (0 / 0 / 100%) | - | A scorpion's eyes can apparently take in the whole way around its body. The two middle eyes together cover a full circle, with about forty degrees of overlap ab |
| scorpion | Two kinds of eyes | g | i (0 / 0 / 100%) | - | The pair of eyes in the middle of the head are the main eyes. They give a fairly sharp picture and tell shapes apart. The side eyes, three to five pairs, seem t |
| scorpion | Many small eyes | m | i (0 / 0 / 100%) | - | Buthid scorpions have five pairs of small side eyes. The first three are about 0.3 mm across and the last two are about 0.12 mm across in one species. |
| scorpion | Blue and green | m | i (1 / 24 / 74%) | - | Electrical recordings from the eyes of two scorpion genera peak in blue light at 470 nanometres and in green light at 525. The recordings do not say how many ki |
| scorpion | Eyes for the night | g | i (0 / 0 / 100%) | - | Scorpions are active at night and their eyes can sense starlight. In one species the middle eyes are about a thousand times more sensitive at night than by day. |
| sealife | No picture | i | m (87 / 0 / 13%) | - | Sea anemones and corals have no eyes. The picture keeps only how much light there is, what colour it is and where it comes from. |
| sealife | Blue moonlight | m | i (0 / 0 / 100%) | - | A small sea anemone released its eggs and sperm in step only when blue light, standing in for a full moon, shone through five nights of each month. White light  |
| sealife | Shadows | g | m (100 / 0 / 0%) | - | A surf clam has a nerve that senses light by itself. When a shadow falls, the nerve fires a burst and the clam pulls in its siphon. |
| sealife | Moon jellies | m | i (4 / 0 / 96%) | - | A moon jelly has small cups of light-sensing cells around its rim, and it swims faster in brighter light. Without those cups it no longer does. |
| sealife | Scallops and giant clams | x | m (86 / 14 / 0%) | 200 | A scallop has up to 200 eyes along the edge of its shell, each focusing light with a mirror, and a giant clam has several hundred pinhole eyes. This view does n |
| sealife | Box jellyfish | x | m (100 / 0 / 0%) | 24 | Box jellyfish have 24 eyes, some with lenses, and one kind looks up through the water to steer by the trees above it. This view does not draw them. |
| sealife | Eyes at the arm tips | g | i (41 / 0 / 59%) | 250, 100, 30 | A starfish has an eye at the tip of each arm. In the crown-of-thorns starfish each eye has about 250 tiny facets and looks out sideways over a patch about 100 d |
| sealife | Grey and slow | g | i (0 / 0 / 100%) | - | The blue sea star is colour blind, and its eyes follow flicker only up to 1 or 2 times a second, against about 60 for yours. The starfish picture is grey, and a |
| shark | Colour | m | i (0 / 1 / 99%) | - | Every shark studied so far has only one kind of colour-sensing cell, so sharks are probably colour blind. They can tell apart shades of brightness that differ b |
| shark | Sharpness | m | i (5 / 6 / 89%) | - | Sharks see between a twentieth and a sixth as much detail as you do. Fast hunters of open water, like the bigeye thresher, are at the sharp end, and bottom-dwel |
| shark | Sharpest band | m | i (4 / 2 / 94%) | - | Many sharks, such as the lemon shark, see most sharply along a band level with the horizon, which lets them scan the sea floor or the open water without moving  |
| shark | Pace | m | i (17 / 15 / 68%) | - | Sharks follow a flickering light up to 16 to 31 flashes a second, a quarter to a half of your rate, so quick movement smears for them. This view leaves trails b |
| shark | Two eyes | m | i (6 / 12 / 82%) | - | A shark’s eyes sit on the sides of its head, and in a lemon shark the two fields overlap by only about 10 degrees in front. Hammerheads swing their heads from s |
| shark | Electric sense | m | i (5 / 0 / 95%) | - | Sharks feel the faint electric fields around living animals through gel-filled pores on the snout, called the ampullae of Lorenzini. A young hammerhead turns to |
| slime | No picture | g | i (30 / 0 / 70%) | - | A slime mould is one huge cell, from a kingdom apart from the fungi. It has no eye, and it reads how much light falls on it and of what colour. |
| slime | Colour | m | i (30 / 0 / 70%) | - | Physarum polycephalum crawls away from blue light and far-red light, and toward red light. |
| slime | Hunger | m | i (30 / 0 / 70%) | - | Well fed, it moves away from light. Short of food, it moves toward light, and after several days without food, light turns it into spore heads. |
| slime | Pace | m | i (30 / 0 / 70%) | - | Its body swells and thins every one to two minutes, and its speed rises and falls over about 20 minutes. Your eyes follow flicker to about 60 a second. |
| snail | Eyes | m | i (0 / 0 / 100%) | - | A land snail or slug has a small eye with a lens at the tip of each upper tentacle. In the White-lipped Snail each eye is about a quarter of a millimetre across |
| snail | Sharpness | m | i (0 / 4 / 95%) | 15 | The garden snail's eye resolves about 15 degrees, so it keeps under a thousandth of the detail you see. Behaviour tests put a red slug's resolution at about 52  |
| snail | Colour | m | i (1 / 22 / 77%) | - | A slug's eye is most sensitive to blue near 480 nanometres in the dark and to violet near 420 in daylight. The picture is drawn in grey weighted to blue. |
| snail | Light without eyes | m | i (1 / 0 / 99%) | - | A slug whose eyes have been removed still crawls away from bright light, which it senses with its brain. |
| snail | Shadows | g | m (100 / 0 / 0%) | 490 | A pond snail pulls back into its shell when a shadow falls on it. It feels the shadow through its skin, most strongly in blue-green light near 490 nanometres. |
| snail | Sea slugs | g | m (100 / 0 / 0%) | - | A nudibranch's eyes lie deep under the skin behind its rhinophores. Even so, one nudibranch crawled toward a black stripe placed outside its arena. |
| tick | Eyes | m | i (14 / 7 / 79%) | - | The Lone Star Tick and the dog ticks have one pair of eyes. The black-legged ticks have none. |
| tick | Where they look | g | i (0 / 0 / 100%) | 33 | In the tropical bont tick, of the Lone Star Tick’s genus, each eye has one lens and takes in a patch 43 degrees wide and 49 high, aimed 39 degrees out from stra |
| tick | Shapes | g | i (34 / 0 / 66%) | 18 | A camel tick walks toward a dark disc on a pale background once the disc spans about 5 degrees, and toward the outline of a camel as small as a real one 18 metr |
| tick | Colour | g | i (0 / 0 / 100%) | - | The tropical bont tick is most sensitive to blue light near 480 nanometres, with a single peak. The picture is drawn in grey from the camera’s blue and green, a |
| tick | Without eyes | g | i (0 / 0 / 100%) | - | The sheep tick, in the same genus as the black-legged ticks, has two rows of about twenty light-sensitive cells along its upper sides. In a laboratory, its nymp |
| tick | Questing | m | i (34 / 0 / 66%) | - | A questing tick grips a grass tip with its back two pairs of legs and holds the front pair out, ready to climb onto a passing host. Those front legs carry Halle |
| tick | Heat | m | i (48 / 0 / 52%) | - | Lone Star Ticks steer by radiant heat through a covered pit on each front leg, and at least seven in ten adult females detected a square 10 centimetres across,  |
| tick | Breath | g | i (34 / 0 / 66%) | - | In the tropical bont tick, one receptor cell in that same organ responds most to changes in carbon dioxide of a hundredth of a percent around the level in open  |
| whale | Colour | m | i (17 / 30 / 54%) | - | Dolphins, porpoises and seals have a single kind of cone, tuned to long wavelengths, and no blue-sensitive cone. In dolphins and porpoises that cone peaks near  |
| whale | Some colour may remain | m | i (18 / 29 / 54%) | - | Baleen whales and sperm whales have lost the genes for their cone pigments and rely on rods alone. A manatee has two kinds of cone, and a California sea lion pi |
| whale | Sharpness | m | i (41 / 4 / 55%) | - | A humpback whale resolves about 3.95 cycles per degree and a Bryde's whale 4.8. A false killer whale, a Pacific white-sided dolphin and a beluga managed 2.6 to  |
| whale | Field of view | g | i (17 / 0 / 83%) | - | A dolphin's eyes sit on the sides of its head. Each sees 120 to 130 degrees to its side, and the two overlap by only 20 to 30 degrees in front. Together that is |
| whale | Dim light | m | i (20 / 1 / 78%) | - | A bottlenose dolphin sees low light half a log unit better than a person, about three times better, but 0.2 log units worse in bright light. Dolphins, harbour s |
| whale | Whiskers | x | m (56 / 0 / 44%) | 100, 30 | Seal whiskers are most sensitive to vibration between 10 and 100 hertz, and a harbour seal can follow a fish's wake for up to 30 seconds after the fish has pass |
| woodlouse | Eyes | g | i (16 / 8 / 76%) | 25, 22, 2,400, 6,000 | Two small-eyed water isopods have 4 and about 25 facets to an eye, and a close picture of a Rough Woodlouse’s eye shows 22. The Asian shore crab has 2,400 to 6, |
| woodlouse | Sharpness | g | i (0 / 0 / 100%) | - | The sea slater, a big-eyed seashore relative, has facets about 7 degrees apart, which resolves about 0.07 cycles per degree, near an eight-hundredth of your 60. |
| woodlouse | Dark | m | i (0 / 0 / 100%) | - | Woodlice turn away from light toward dark shelters, where the air is damper and cooler. |
| woodlouse | Dry air | m | i (0 / 0 / 100%) | - | Woodlice shelter more when the air is dry, and huddled together they lose about half as much water as they do alone. |
| woodlouse | Night | m | i (35 / 8 / 57%) | - | About six in ten Common Pill Woodlice are active at night, against nine in ten of Philoscia muscorum, the fourth most recorded woodlouse. |
| worm | No eyes | m | i (5 / 0 / 95%) | - | An earthworm has no eyes. Light-sensitive cells lie in the skin of every segment, most of them at the head and the tail, and tiny windows in a layer of pigment  |
| worm | Bright and dim | m | i (5 / 0 / 95%) | - | An earthworm crawls away from ordinary light, but it moves toward light that is very dim. |
| worm | A mole digging | m | i (0 / 0 / 100%) | - | Florida earthworms rush out of their burrows when the ground carries the vibration of a digging mole. Bait collectors copy it by scraping a stake driven into th |
| worm | Leeches | m | i (5 / 0 / 95%) | - | A medicinal leech has five pairs of eyecups on its head and seven pairs of light-sensing spots in every segment of its body. The spots on its back respond best  |
| worm | Flatworms | g | i (0 / 0 / 100%) | - | Each cup-shaped eye of a freshwater planarian samples the world about every 35 degrees, and behaviour tests on another planarian give the same coarse sharpness. |
| worm | Fan worms | m | g (6 / 94 / 0%) | - | Fan worms and Christmas tree worms have eyes on their feathery tentacles. Their light-sensing pigment peaks at 464 nanometres, close to the blue light of a shal |

Live rows with no matching row in `rows.py` (not compared): bee: How the colours are shown; jumper: Eight eyes, one picture, The side eyes, Living things stand out, The front eyes, Jumps and scans, Looking away on purpose, Sleep, How the picture is drawn, Living movement, How the colours are shown, Hearing, Colours it cannot tell apart, A moment slowed; spider: Knocks and low sounds, Hearing through silk, Wolf spiders, Being tried: web and air; bat: Being tried: clap and see; centipede: Being tried: shadows; cephalopod: How it is drawn; duck: Being tried: the sky overhead; fish: Looking up, How it is drawn, Being tried: looking up, Being tried: the window as a field; flyingfox: Field, focus and pupil; fox: Being tried: north, Guesses; fungus: Colour and time, Being tried: the hour in a minute, Being tried: the patient view, Being tried: which way is down; harvestman: Not in the picture; mammal: Being tried: the rumble; millipede: Being tried: shaking ground; owl: Being tried: hearing as light, Guesses; primate: What the app chose; reef: Red light fades, How the eyes are drawn, Distance; salamander: Being tried: north; scorpion: The app's choices, Settings the app chose; sealife: How it is drawn, Tonight's moon; shark: The glow; slime: Colour and time, Being tried: the hour in a minute, Being tried: the patient view; snail: How it is drawn, Dusk; whale: The app's own choices, Being tried: echo rings; woodlouse: No picture, Being tried: shadows; worm: The picture, Being tried: the shadow alarm.
<!-- live-disagreement:end -->

<!-- rows-try:start -->
## Rows pipeline, the views behind ?try= (18 October)

`tools/views/rows.py` drafted 185 rows of 26 views behind `?try=` with claude-sonnet-5-5, from 20371 evidence records (the audit and the burst 9 decisions applied). Spent $1.94 at batch prices.

The rows and the traits they rest on are `docs/views/gaps/try-rows.json` (every live row about the animal; rows about the drawing or the app's choices are left out), and the species that borrow each view are `docs/views/gaps/try-species.json` (`tools/views/try_species.py`: the 60 most recorded species of the view's world group or taxa, and the measured species of the view). A row about one group (elephants, chitons) is drafted for that group's species. A row with no evidence record at all is not sent when its live row claims something (graded m, g or x), since the draft could only say that nobody has measured it. A draft passes when `voice_check.py` finds nothing in it, every number in it is in a record it cites, and the records cited belong to a species of the view or a relative of one. A draft that fails is sent once more with the errors; what still fails is listed. The live rows, the `offered` flags and the specs are unchanged.

| view | rows | passed first time | passed after the retry | failed | not sent |
|---|---:|---:|---:|---:|---:|
| bat | 9 | 6 | 3 | 0 | 0 |
| bigcat | 8 | 6 | 2 | 0 | 1 |
| centipede | 6 | 4 | 0 | 2 | 1 |
| cephalopod | 7 | 0 | 5 | 2 | 0 |
| crab | 8 | 3 | 5 | 0 | 1 |
| duck | 7 | 3 | 4 | 0 | 0 |
| fish | 7 | 2 | 5 | 0 | 0 |
| flyingfox | 7 | 5 | 2 | 0 | 0 |
| fox | 6 | 6 | 0 | 0 | 0 |
| fungus | 8 | 5 | 3 | 0 | 1 |
| harvestman | 6 | 2 | 4 | 0 | 0 |
| mammal | 9 | 4 | 4 | 1 | 0 |
| millipede | 7 | 3 | 3 | 1 | 0 |
| owl | 7 | 1 | 6 | 0 | 0 |
| primate | 5 | 3 | 2 | 0 | 0 |
| reef | 5 | 3 | 2 | 0 | 0 |
| salamander | 10 | 8 | 2 | 0 | 0 |
| scorpion | 6 | 1 | 5 | 0 | 0 |
| sealife | 10 | 7 | 2 | 1 | 1 |
| shark | 6 | 4 | 2 | 0 | 1 |
| slime | 5 | 2 | 1 | 2 | 0 |
| snail | 9 | 4 | 5 | 0 | 0 |
| tick | 9 | 6 | 2 | 1 | 0 |
| whale | 6 | 6 | 0 | 0 | 0 |
| woodlouse | 5 | 2 | 2 | 1 | 2 |
| worm | 7 | 4 | 3 | 0 | 0 |
| all | 185 | 100 (54%) | 74 | 11 | 8 |

Pass rate on the first attempt: 54%. After the retry: 94%.

### Rows that failed the first time, and why

The reasons are found again by checking the batch's first replies with the checker as it stands now, which no longer counts 'slider' (a turtle) or 'camera-type eye' as talk about the app; the reptile row that this fixed still shows as passing only on its second attempt in the counts above.

- **bat, Distance**: voice check voice_words: reports
- **bat, Reach**: voice check voice_words: reports
- **bat, Sharpness**: voice check voice_words: reports
- **bigcat, Field of view and depth**: voice check voice_words: reports
- **bigcat, Sharpness**: voice check numbers: 23; voice check numbers: 1942; the number 1942 is in none of the cited records
- **centipede, Dark shapes**: voice check app: screen; voice check voice_words: reports
- **centipede, Soil centipedes**: voice check grade_words: an i row that does not say that nobody knows
- **cephalopod, Color**: the number 2020 is in none of the cited records
- **cephalopod, Field**: voice check voice_words: reports; voice check numbers: 63
- **cephalopod, Flicker**: voice check voice_words: reports
- **cephalopod, Polarized light**: voice check app: view; voice check app: in this view; voice check app: last sentence: Nobody has measured whether you see polarized light if you a
- **cephalopod, Pupil**: voice check voice_words: reports
- **cephalopod, Sharpness**: voice check voice_words: reports; voice check voice_words: reports
- **cephalopod, Where it is sharp**: voice check voice_words: reports
- **crab, Color**: voice check voice_words: reports
- **crab, Crayfish**: voice check voice_words: reports
- **crab, Night**: voice check app: view; voice check app: in this view; voice check app: last sentence: Nobody has measured how well you see in the dark if you are 
- **crab, Pace**: voice check voice_words: reports
- **crab, Sharpness**: voice check voice_words: reports; voice check numbers: 1.5
- **duck, Below the bill**: voice check voice_words: report
- **duck, Color**: voice check voice_words: reports
- **duck, Sharpness**: voice check voice_words: reports
- **duck, Touch**: voice check voice_words: reports
- **fish, Color**: voice check voice_words: report
- **fish, Pace**: voice check voice_words: report
- **fish, Sharpness**: voice check voice_words: reports
- **fish, Ultraviolet**: voice check voice_words: reports
- **fish, Where it is sharp**: voice check voice_words: reports; voice check contrast: instead of: A review reports a vertical streak instead of a patch in the glyrna.
- **flyingfox, Sharpness**: voice check spelling: grey
- **flyingfox, Ultraviolet**: voice check voice_words: reports
- **fungus, Color**: voice check voice_words: reports
- **fungus, Down**: voice check voice_words: reports
- **fungus, Red**: voice check voice_words: reports
- **harvestman, Color and dim light**: voice check voice_words: report; voice check numbers: 1988; the number 1988 is in none of the cited records
- **harvestman, Eyes**: voice check voice_words: reports
- **harvestman, Hidden eyes**: voice check voice_words: reports
- **harvestman, Touch and taste**: voice check voice_words: reports
- **mammal, Dim light**: voice check voice_words: reports; voice check voice_words: reported
- **mammal, Electric sense**: voice check voice_words: reports
- **mammal, Elephants**: voice check fragment: Sharpness.
- **mammal, Kangaroos**: voice check voice_words: reports; voice check contrast: not X, but Y: Other kangaroos and wallabies of your genus have not been measured, bu; voice check fragment: Colors.; voice check numbers: 539
- **mammal, Sharpness**: voice check spelling: grey
- **millipede, Light through the skin**: voice check numbers: 1951; the number 1951 is in none of the cited records
- **millipede, Night**: voice check voice_words: reports
- **millipede, Taste and damp**: voice check numbers: 1951; the number 1951 is in none of the cited records
- **millipede, Touch**: voice check app: taps
- **owl, Eyes that face forward**: voice check voice_words: reports; voice check numbers: 34
- **owl, Fixed eyes**: voice check voice_words: reports
- **owl, Hearing**: voice check voice_words: reports
- **owl, Night vision**: voice check voice_words: reports
- **owl, Sharpness**: voice check voice_words: reports
- **owl, Where sounds come from**: voice check voice_words: reports
- **primate, Color**: voice check voice_words: reports; voice check voice_words: reports
- **primate, Other monkeys see less color**: voice check voice_words: reports
- **reef, Color**: voice check voice_words: reports
- **reef, Sharpness**: voice check voice_words: reports
- **salamander, Color**: voice check voice_words: reports
- **salamander, Moving water and electricity**: voice check voice_words: reports
- **scorpion, All around**: voice check voice_words: reports; voice check fragment: Picture a full circle around your body.
- **scorpion, Eyes for the night**: voice check voice_words: reports
- **scorpion, Many small eyes**: voice check voice_words: reported; voice check numbers: 353; voice check grade_words: an i row that does not say that nobody knows
- **scorpion, The ground and the air**: voice check voice_words: reports
- **scorpion, Two kinds of eyes**: voice check voice_words: reports
- **sealife, Eyes at the arm tips**: voice check voice_words: reports
- **sealife, Gray and slow**: voice check voice_words: reports
- **sealife, Sea urchins**: voice check voice_words: reports; voice check numbers: 0.01; voice check numbers: 0.03
- **shark, Color**: voice check voice_words: reports
- **shark, Sharpness**: voice check voice_words: reports
- **slime, Hunger**: voice check voice_words: reports; the number 1950 is in none of the cited records
- **slime, No eyes**: voice check voice_words: reports
- **slime, Pace**: voice check voice_words: reports
- **snail, Color**: voice check voice_words: reports; voice check numbers: 496
- **snail, Eyes**: voice check voice_words: reports; voice check voice_words: reports
- **snail, Light without eyes**: voice check voice_words: reports; voice check voice_words: reports
- **snail, Sea slugs**: voice check voice_words: reports
- **snail, Sharpness**: voice check voice_words: reports
- **tick, Eyes**: voice check voice_words: reports; voice check numbers: 1977; the number 1977 is in none of the cited records
- **tick, Heat**: voice check voice_words: reports
- **tick, Without eyes**: voice check voice_words: report
- **woodlouse, Color**: voice check voice_words: reports
- **woodlouse, Night**: the number 40 is in none of the cited records
- **woodlouse, Sharpness**: voice check numbers: 0.05
- **worm, A mole digging**: voice check contrast: Y, not X: In the Mediterranean medicinal leech, an abstract of nerve recordings 
- **worm, Leeches**: voice check voice_words: reports
- **worm, Touch, taste and damp**: voice check voice_words: reports; voice check numbers: 1969; the number 1969 is in none of the cited records

### Rows that still fail after the retry

- **centipede, Dark shapes** (grade i): voice check numbers: 1934
  - last draft: If you are a brown centipede, you run toward a black panel at the side of an arena, according to a 1934 experiment described in a review. If you are a Chinese red-headed centipede, you avoid sunlight less when your antennae are covered with foil, so your antennae take part in that avoidance. Nobody has measured what a dark shape looks like to you or how sharply you see its edges.
- **centipede, Soil centipedes** (grade i): voice check voice_words: reported
  - last draft: You live underground, where a commentary on the maritime centipede's genome says every centipede in your order, the Geophilomorpha, is blind. Nobody has reported an eye count for your own species, so nobody can say for certain that you have no eyes.
- **cephalopod, Sharpness** (grade m): voice check length: 4 sentences
  - last draft: If you are a common octopus, a review gives your sharpness as about 45 cycles a degree, finer than the 30 a human reads on an eye chart. If you are a pale octopus, another review gives only 3 to 7. If you are a bigfin reef squid, you see about 2 cycles a degree at 2 months old, and if you are a European common cuttlefish, the largest animals in bright light can tell stripes apart when they are about half a degree apart. If you are a chambered nautilus, stripes must be 5 to 11 degrees apart, and nobody has measured this in most other cephalopods.
- **cephalopod, Color** (grade i): voice check voice_words: reports
  - last draft: If you are a European common cuttlefish, your eyes have only one visual pigment, and a paper reports that cuttlefish have been shown to be color blind. A review lists one pigment for the common octopus as well, and three for the firefly squid. For most other octopuses, squid and cuttlefish, nobody has measured how many kinds of color-sensing cell you have.
- **mammal, Kangaroos** (grade g): voice check spelling: grey
  - last draft: If you are a tammar wallaby, you have two kinds of color-sensing cone, where humans have three. Nobody has counted the cones of the grey kangaroos, the euro or the sandy wallaby, so if you are one of them, you very likely have two kinds as well, like your relative the tammar wallaby.
- **millipede, Night** (grade i): voice check numbers: 2022; the number 2022 is in none of the cited records
  - last draft: One millipede, Paraspirobolus lucifugus, moves away from light and is active only at night, and its daily rhythm is apparently run by an internal clock, according to the abstract of a 2022 paper by Meyer-Rochow. Nobody has recorded whether you are active at night or by day.
- **sealife, Sea urchins** (grade m): voice check app: draws
  - last draft: A human thumb held at arm's length covers about 2 degrees, and you need a target several thumbs wide before you can pick it out. If you are an Atlantic purple sea urchin, you turned toward targets only when they were 45 degrees wide or more, and if you are a Diadema africanum, you move toward dark objects only when they are 30 to 70 degrees wide, according to a modeling paper that draws on the behavioral test. If you are a Pacific purple sea urchin, the spacing of your spines predicts a finest detail of about 8 to 11 degrees, and if you are an Arctic green sea urchin, you very likely see about as coarsely as that close relative.
- **slime, No eyes** (grade i): voice check numbers: 1938; the number 1950 is in none of the cited records; the number 1938 is in none of the cited records
  - last draft: You have no eyes, yet light matters to you, and nobody has measured how most slime molds sense it. If you are a dog vomit slime mold, a 1950 paper reviewing work from 1938 states that you cannot form fruiting bodies without light. If you are Physarum polycephalum, a light-sensing pigment called a phytochrome is one reason your plasmodium breaks into fragments in light, and if you are Didymium iridis, you need both starvation and light before you make spores.
- **slime, Pace** (grade i): the number 1950 is in none of the cited records
  - last draft: If you are a dog vomit slime mold, a 1950 review of earlier work says your plasmodium cannot fruit without light. In another slime mold, Physarum polycephalum, a light-sensing molecule called a phytochrome is one of the receptors that breaks the plasmodium into pieces in light. Nobody has measured how fast you respond to light.
- **tick, Without eyes** (grade i): voice check numbers: 2003; the number 2003 is in none of the cited records
  - last draft: If you are a castor bean tick, you have strings of light-sensing cells on your left and right sides, and a 2003 paper by Perret says they sense shifts in light intensity. Nobody has measured this in any other tick, so if you are another kind, nobody knows whether you have these strings or how well they work.
- **woodlouse, Sharpness** (grade i): voice check voice_words: reports
  - last draft: Nobody has measured how sharply you see. Of the isopods, only one has been measured: if you are a Natatolana borealis, a review table reports that your compound eye reads less than a hundredth of the fine detail a human reads.

### Rows not sent

- **bigcat, Lens**: no record of lens_chromatic_aberration for these species or their relatives in the evidence logs; the live row is graded m
- **centipede, Sunlight as heat**: no record of sense_thermal for these species or their relatives in the evidence logs; the live row is graded m
- **crab, All around**: no record of fov_h_deg for these species or their relatives in the evidence logs; the live row is graded g
- **fungus, Water**: no record of sense_humidity for these species or their relatives in the evidence logs; the live row is graded x
- **sealife, Blue moonlight**: no record of sense_light_nonvisual for these species or their relatives in the evidence logs; the live row is graded m
- **shark, Smell first**: no record of sense_chemical for these species or their relatives in the evidence logs; the live row is graded x
- **woodlouse, Dry air**: no record of sense_humidity for these species or their relatives in the evidence logs; the live row is graded m
- **woodlouse, Damp air**: no record of sense_humidity for these species or their relatives in the evidence logs; the live row is graded x

### Ten drafts beside the live rows

**owl, Sharpness** (draft grade `m`; of the species' records 46% measured, 30% carried, 23% unknown)

- Draft: A human reads about 30 cycles a degree on an eye chart, and owls range from far below that to a little above it. If you are a barn owl of the kind called Tyto alba pratincola, a compilation lists only 4, and a tawny owl tested on behavior reads about 11. Estimates from the density of cells in the retina give about 15 for a burrowing owl, 25 for a great gray owl, 30 for a great horned owl and 40 for a snowy owl.
- Live: `m` Sharpness: A barn owl sees only a fifteenth to a twentieth as much detail as a person does, and other owls measured average about a third. This view is blurred to about a sixth of a person's sharpness, between the two.
- Cites: birds#49 (Tyto alba pratincola), canon-5#155 (Strix aluco), canon-5#157 (Strix nebulosa), canon-5#21 (Athene cunicularia), canon-5#33 (Bubo scandiacus), canon-5#35 (Bubo virginianus)

**fox, Pupil** (draft grade `m`; of the species' records 100% measured, 0% carried, 0% unknown)

- Draft: If you are a red fox or an arctic fox, your pupil is a narrow vertical slit. If you are a gray fox, your pupil is oval, unlike the slits of foxes in the genus Vulpes, such as the red fox.
- Live: `m` Pupil: A red fox's pupil narrows in bright light to a tall, thin oval, close to a house cat's slit, and its lens has zones that bring several colours into focus together. Out-of-focus things smear up and down in this view.
- Cites: cat-dog#104 (Urocyon cinereoargenteus), cat-dog#51 (Vulpes vulpes), intake-4#14 (Vulpes lagopus)

**bat, Calls** (draft grade `i`; of the species' records 21% measured, 0% carried, 79% unknown)

- Draft: If you are a big brown bat, you send out 5 to 10 search calls a second, each up to 15 to 20 milliseconds long. If you are a Mexican free-tailed bat, you send out about 4 a second, each about 14 milliseconds long. Nobody has measured the search calls of most other bats, so for them these figures are unknown.
- Live: `m` Calls: A big brown bat calls 5 to 10 times a second while searching, 20 to 80 times while closing in, and up to about 170 times in the final buzz. Each call returns one snapshot, so the picture holds, then jumps, about seven times a second. That rendering is this app’s invention.
- Cites: mammal-groups#55 (Eptesicus fuscus), mammal-groups#67 (Tadarida brasiliensis)

**shark, Electric sense** (draft grade `i`; of the species' records 5% measured, 0% carried, 95% unknown)

- Draft: A flatfish buried in sand gives off a faint electric field, and if you are a small-spotted catshark, you find it by that field alone and give the same feeding response to two buried electrodes. If you are a scalloped hammerhead, a juvenile turns toward a prey-like electric field from about 30 centimeters away. Electric sense has been measured in only a few sharks, rays and rabbit fish, and for most others, including you if you are none of these, nobody has measured it.
- Live: `m` Electric sense: Sharks feel the faint electric fields around living animals through gel-filled pores on the snout, called the ampullae of Lorenzini. A young hammerhead turns toward a prey-like field from about 30 centimetres away.
- Cites: fish-shark#127 (Sphyrna lewini, Carcharhinus plumbeus), fish-shark#128 (Scyliorhinus canicula, Raja clavata)

**tick, Heat** (draft grade `i`; of the species' records 48% measured, 0% carried, 52% unknown)

- Draft: If you are an adult female lone star tick, at least 7 in 10 of your kind can detect a warm plate the size of a hand from a meter away. If you are an American dog tick, a review of the work states that unfed adults with their Haller's organs present move toward infrared light. Nobody has measured whether other ticks sense heat in this way.
- Live: `m` Heat: Lone Star Ticks steer by radiant heat through a covered pit on each front leg, and at least seven in ten adult females detected a square 10 centimetres across, heated to 40 degrees Celsius, from a metre away. An ordinary phone cannot sense that heat, so it is left out.
- Cites: ground-invertebrates#160 (Amblyomma americanum), oa-3#518 (Dermacentor variabilis)

**fungus, Down** (draft grade `i`; of the species' records 4% measured, 0% carried, 96% unknown)

- Draft: If you are a meadow mushroom and your cap is tilted by up to 30 degrees, your gills turn back to straight down, and if you are a splitgill mushroom, your gills develop facing down in response to gravity. A review of experiments on gilled mushrooms found that their stems grow away from gravity and their gills grow toward it. Nobody has measured whether most other fungi sense which way is down.
- Live: `m` Down: A mushroom stem laid on its side starts to turn up in about 25 minutes, and its tip is upright again within 3 to 4 hours. The gills of a field mushroom turn back toward straight down within an hour, so the spores fall clear.
- Cites: plant-fungus-slime#111 (Schizophyllum commune), plant-fungus-slime#114 (Agaricus campestris), plant-fungus-slime#113 (Agaricales)

**crab, Polarized light** (draft grade `i`; of the species' records 3% measured, 4% carried, 93% unknown)

- Draft: Polarized light is light whose waves vibrate in one direction, and fiddler crabs, mantis shrimp and the tawny hermit crab have all been shown to see it. The tawny hermit crab and two other hermit crabs spotted predator-like shapes by polarization contrast alone. If you are not one of the crabs that were tested, nobody has measured whether you see it.
- Live: `x` Polarized light: A fiddler crab tells apart polarized light whose angle differs by 3 degrees, and uses it to pick out objects on the mud. A phone camera does not record polarization, so it is left out.
- Cites: sea-invertebrates#152 (Gonodactylus smithii, Odontodactylus scyllarus), sea-invertebrates#153 (Haptosquilla trispinosa), sea-invertebrates#154 (Uca heteropleura), sea-invertebrates#159 (Coenobita rugosus and two other hermit crabs), sea-invertebrates#183 (Uca vomeris)

**whale, Sharpness** (draft grade `i`; of the species' records 41% measured, 4% carried, 55% unknown)

- Draft: A human reads about 30 cycles a degree on an eye chart, and every whale, dolphin and seal measured so far sees far less than that. If you are a harbor seal, cell counts in the retina predict about 12 under water, and the same method gives about 4 for a minke whale, a humpback whale or a walrus and about 3 for a bottlenose dolphin. Nobody has measured how sharply you see if you are a sea lion, an elephant seal or a gray whale.
- Live: `m` Sharpness: A humpback whale resolves about 3.95 cycles per degree and a Bryde's whale 4.8. A false killer whale, a Pacific white-sided dolphin and a beluga managed 2.6 to 3.3. A harbour seal reaches 11.5 under water and a manatee only 1.6. Most of these values are estimated from the retina. A person resolves about 30, so this view blurs the picture to 3.95.
- Cites: mammal-groups#27 (Phoca vitulina), mammal-groups#186 (Balaenoptera acutorostrata), mammal-groups#29 (Megaptera novaeangliae), oa-1#4142 (Odobenus rosmarus), mammal-groups#22 (Tursiops truncatus)

**snail, Eyes** (draft grade `i`; of the species' records 0% measured, 0% carried, 100% unknown)

- Draft: A review states that in land snails and slugs the optics cannot produce a focused image on the shallow retina, so if you are one, you very likely see no sharp image. If you are a periwinkle, the same kind of review states that the lens of Littorina forms a sharp image on the retina, and if you are a nudibranch, a natural history account says your small eyes sit deep inside your body and tell light from dark without seeing images. Nobody has counted how many eyes you have.
- Live: `m` Eyes: A land snail or slug has a small eye with a lens at the tip of each upper tentacle. In the White-lipped Snail each eye is about a quarter of a millimetre across.
- Cites: ground-invertebrates#132 (Stylommatophora), canon-3#677 (Littorina), ground-invertebrates#180 (Nudibranchia)
<!-- rows-try:end -->
