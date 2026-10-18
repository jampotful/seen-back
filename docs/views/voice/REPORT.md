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
| hawk | 3 | 3 | 2 | 1 |
| insect | 3 | 3 | 3 | 0 |
| jumper | 14 | 1 | 1 | 0 |
| plant | 3 | 3 | 2 | 0 |
| rabbit | 1 | 1 | 0 | 0 |
| reptile | 1 | 1 | 0 | 0 |
| spider | 8 | 4 | 4 | 0 |
| squirrel | 3 | 3 | 1 | 0 |
| wader | 5 | 5 | 4 | 0 |
| all | 72 | 54 | 36 | 1 |

### The rows that differ

| view | row | live grade | evidence grade (shares m / g / i) | numbers not found | live text |
|---|---|---|---|---|---|
| alligator | Sharpest spot | g | i (5 / 0 / 95%) | - | Crocodiles see most sharply along a band level with the horizon. It lets them scan the waterline without turning their heads. |
| alligator | Colour | g | m (63 / 23 / 14%) | - | Crocodiles have three kinds of colour-sensing cells, as people do, so this view leaves colours as your camera shows them. |
| alligator | Pupil | g | m (63 / 0 / 37%) | - | An alligator’s pupil is a vertical slit. It smears out-of-focus things up and down, and this view does the same. |
| bee | Sharpness | g | i (18 / 32 / 50%) | - | Most insects see less than a sixtieth as much detail as people do. |
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
| hawk | Speed | m | i (3 / 12 / 85%) | 50 | A peregrine falcon can see a light flicker up to 129 times a second, and a Harris’s hawk up to 77. People see flicker up to 50 or 60 times a second. This view r |
| insect | Sharpness | g | i (4 / 8 / 88%) | - | Most insects see less than a sixtieth as much detail as people do. |
| insect | Speed | g | i (0 / 0 / 100%) | - | Flies and dragonflies can see a light flicker more than 100 times a second, and one beetle up to 400. People stop at about 60. This view runs slowly and then ju |
| insect | Ultraviolet | i | g (2 / 62 / 37%) | - | Bees and some other insects can see ultraviolet light, which people can’t. Phone cameras capture very little of it, so the violet tint in this view stands in fo |
| jumper | Colour | m | i (0 / 22 / 78%) | - | Most jumping spiders, Phidippus among them, see ultraviolet and green. Habronattus also sees red, in a small patch at the centre of each front eye, and this vie |
| plant | No picture | g | i (0 / 0 / 100%) | - | A plant has nothing like a lens to focus light into an image. It senses how much light there is, what colour it is, and which direction it comes from. |
| plant | Neighbours | m | i (1 / 0 / 99%) | - | Plants compare red light with far-red light, a colour just past the edge of what people can see. The balance tells a plant that a neighbour is growing close by, |
| spider | The web | m | i (22 / 0 / 78%) | - | A Golden Silk Spider feels its prey through the silk, and a trapped insect shakes the web 5 to 30 times a second. The shaking arrives ten to thirty times strong |
| spider | Eyes | g | i (0 / 0 / 100%) | - | Most spiders have eight eyes and few see well. Most register little more than changes between light and dark, and spiders that build webs lean on the shaking of |
| spider | Sharpness | g | i (0 / 0 / 100%) | - | A wandering spider resolves nothing finer than about 2 degrees, under a hundredth of your sharpness. The picture borrows that figure for web builders. |
| spider | Pace | g | i (0 / 0 / 100%) | - | A wandering spider stops following flicker between 4.3 and 8.6 times a second, a seventh of your rate or less, so movement smears into trails. |
| squirrel | Speed | g | i (13 / 12 / 75%) | - | A golden-mantled ground squirrel can follow a light flickering at more than 100 times a second, and a yellow-pine chipmunk does about the same. An American red  |
| wader | Head movement | m | i (11 / 6 / 83%) | - | Herons, egrets, cranes, pigeons and chickens hold their heads still while they walk, so their eyes stay fixed on the world. Then the head darts forward to catch |
| wader | Speed | g | i (7 / 3 / 91%) | - | In pigeons, each dart forward takes about a tenth of a second. |
| wader | Sharpness | g | i (0 / 0 / 100%) | - | Most birds see half as much detail as people do, or less. |
| wader | Ultraviolet | g | i (0 / 0 / 100%) | - | A whooping crane’s shortest-wave cone peaks near 405 nanometers and a pigeon’s near 410, both in the violet. The gene for that cone is the violet type in a gray |

Live rows with no matching row in `rows.py` (not compared): bee: How the colours are shown; jumper: Eight eyes, one picture, The side eyes, Living things stand out, The front eyes, Jumps and scans, Looking away on purpose, Sleep, How the picture is drawn, Living movement, How the colours are shown, Hearing, Colours it cannot tell apart, A moment slowed; spider: Knocks and low sounds, Hearing through silk, Wolf spiders, Being tried: web and air.
<!-- live-disagreement:end -->
