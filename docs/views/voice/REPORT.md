# The rows pass: voice check and drafts

Written by `tools/views/voice_check.py` and `tools/views/rows.py`; each tool owns one block.

<!-- voice-check:start -->
## Voice check

`tools/views/voice_check.py` read 444 rows in 44 views (a row held in both a view's own list and its trial list counts once).
342 rows (77%) break at least one rule that a script can see; 1153 findings in all.

### By rule

| rule | findings |
|---|---:|
| humans | 46 |
| app | 628 |
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
| insect | 10 | 3 | 19 |  |  |  |  | 2 |  | 6 |  |  | 7 |
| dog | 8 | 3 | 20 |  |  |  |  | 5 |  | 2 |  |  | 4 |
| salamander | 10 |  | 21 |  |  |  |  | 10 |  | 1 |  |  | 2 |
| fox | 7 | 2 | 21 |  |  |  |  | 7 |  | 1 |  |  | 1 |
| fungus | 10 |  | 17 | 2 |  |  |  | 5 |  |  |  |  | 8 |
| owl | 7 | 2 | 23 |  |  |  | 2 | 4 |  |  |  |  | 1 |
| cephalopod | 8 | 3 | 11 |  |  |  |  | 3 | 1 | 8 |  |  | 3 |
| hawk | 7 | 2 | 11 |  |  |  |  | 1 |  | 12 |  |  | 3 |
| reef | 8 |  | 22 |  |  |  |  | 4 |  |  |  |  | 3 |
| shark | 8 |  | 23 |  |  |  |  | 4 |  | 1 |  |  | 1 |
| bigcat | 7 | 4 | 18 |  |  |  |  | 6 |  |  |  |  |  |
| spider | 7 |  | 18 |  |  |  | 1 | 1 | 1 | 2 |  |  | 5 |
| sealife | 10 |  | 14 |  |  |  |  | 4 |  | 3 |  |  | 6 |
| squirrel | 8 | 1 | 10 |  |  |  |  | 4 |  | 10 |  |  | 2 |
| alligator | 7 | 1 | 9 |  |  |  |  | 2 |  | 10 |  |  | 4 |
| bat | 10 |  | 14 |  |  |  |  | 5 |  | 3 |  |  | 4 |
| tick | 7 |  | 11 |  |  |  |  | 6 |  | 4 |  |  | 5 |
| primate | 5 | 3 | 9 |  |  |  |  | 5 |  | 5 |  |  | 3 |
| duck | 7 | 2 | 17 |  |  |  |  | 2 |  | 1 |  |  | 1 |
| frog | 10 | 1 | 11 |  |  |  | 1 |  |  | 8 |  |  | 2 |
| mammal | 8 | 1 | 10 |  |  |  |  | 5 |  | 4 |  |  | 3 |
| rabbit | 9 |  | 8 | 1 |  |  | 1 | 4 |  | 7 |  |  | 1 |
| snail | 9 |  | 9 |  |  |  |  | 7 |  | 1 |  |  | 4 |
| worm | 6 |  | 11 | 2 |  |  |  | 4 |  | 1 |  |  | 3 |
| scorpion | 8 |  | 11 |  |  |  | 1 | 2 |  | 2 |  |  | 4 |
| millipede | 5 | 1 | 12 |  |  |  |  | 3 |  |  |  |  | 3 |
| slime | 5 |  | 11 | 1 |  |  |  | 3 |  |  |  |  | 4 |
| centipede | 6 |  | 13 |  |  |  |  | 2 |  | 1 |  |  | 2 |
| plant | 5 | 1 | 7 |  |  |  |  | 4 |  | 2 |  |  | 3 |
| reptile | 7 |  | 8 |  |  |  |  |  |  | 9 |  |  |  |
| crab | 8 |  | 8 | 1 |  |  |  | 2 |  | 3 |  |  | 2 |
| wader | 8 | 1 | 7 |  |  |  |  |  |  | 6 |  |  | 2 |
| flyingfox | 7 |  | 6 |  |  |  |  | 5 |  |  |  |  | 4 |
| woodlouse | 6 |  | 7 |  |  |  |  | 2 |  | 2 |  |  | 4 |
| harvestman | 3 |  | 7 |  |  |  |  | 1 |  |  |  |  | 1 |
| other | 1 |  | 1 |  |  |  |  |  |  |  |  |  | 1 |
| person | 1 |  |  |  |  |  | 1 |  |  |  |  |  |  |
<!-- voice-check:end -->

<!-- rows-pipeline:start -->
## Rows pipeline (burst 10)

`tools/views/rows.py` drafted 62 rows of 16 views with claude-sonnet-5-5, from 20371 evidence records (the audit and the burst 9 decisions applied). Spent $0.69 at batch prices.

A draft passes when `voice_check.py` finds nothing in it, every number in it is in a record it cites, and the records cited belong to a species of the view or a relative of one. A draft that fails is sent once more with the errors; what still fails is listed. The first eight views are the ones with the most evidence records; the rest followed.

| view | rows | passed first time | passed after the retry | failed |
|---|---:|---:|---:|---:|
| bird | 4 | 4 | 0 | 0 |
| insect | 3 | 3 | 0 | 0 |
| spider | 6 | 4 | 2 | 0 |
| jumper | 7 | 7 | 0 | 0 |
| dog | 4 | 2 | 2 | 0 |
| cat | 7 | 6 | 1 | 0 |
| bee | 4 | 4 | 0 | 0 |
| plant | 3 | 3 | 0 | 0 |
| alligator | 4 | 3 | 1 | 0 |
| deer | 4 | 3 | 1 | 0 |
| frog | 3 | 2 | 0 | 1 |
| hawk | 3 | 3 | 0 | 0 |
| rabbit | 1 | 0 | 1 | 0 |
| reptile | 1 | 0 | 1 | 0 |
| squirrel | 3 | 3 | 0 | 0 |
| wader | 5 | 3 | 2 | 0 |
| the first eight | 38 | 33 (87%) | 5 | 0 |
| all | 62 | 50 (81%) | 11 | 1 |

Pass rate on the first attempt: 81%. After the retry: 98%.

### Rows that failed the first time, and why

- **alligator, Field of view, sharpness, dim light and depth**: voice check app: view
- **cat, Sharpness**: voice check numbers: 23
- **deer, Field of view**: voice check app: views; voice check app: views
- **dog, Sharpest spot**: voice check app: view; voice check app: this view; voice check app: last sentence: Nobody has measured this in the other species that share thi
- **dog, Sharpness**: voice check length: 4 sentences
- **frog, Movement**: voice check app: view
- **rabbit, The whole view**: voice check numbers: 24
- **reptile, The whole view**: voice check app: slider
- **spider, Color**: voice check numbers: 26
- **spider, Sharpness**: voice check voice_words: answer
- **wader, Head movement**: voice check spelling: grey
- **wader, Speed**: voice check app: view; voice check app: this view

### Rows that still fail after the retry

- **frog, Movement** (grade i): voice check length: 4 sentences
  - last draft: If you are a cane toad, you strike at a moving model of an insect. If you are a bullfrog, you start to avoid an object coming straight at you when it looks about 20 degrees wide to you. If you are a European toad, the nerve cells that pick out moving prey respond less when a black and white textured background moves along with the prey at the same speed. Nobody has measured how most other frogs and toads detect movement.

### Ten drafts beside the live rows

**bird, Ultraviolet** (draft grade `g`; of the species' records 0% measured, 50% carried, 50% unknown)

- Draft: Ultraviolet is light that humans cannot see at all, and in the blue tit, the European starling and the Eurasian blackbird a cone cell senses it best at about 370 nanometers. If you are a songbird, you very likely sense ultraviolet too, and a blue tit's cornea and lens let it through. Birds are not all alike here: the mallard's cone of this kind peaks in violet, and in the pied cormorant the cornea and lens block ultraviolet.
- Live: (no live row with this title)
- Cites: birds#1 (Anas platyrhynchos), birds#17 (Cyanistes caeruleus), birds-met#21 (Sturnus vulgaris), birds-met#25 (Turdus merula), recheck-5-fixed#11 (Phalacrocorax varius), recheck-5-fixed#13 (Cyanistes caeruleus)

**cat, Pupil** (draft grade `m`; of the species' records 100% measured, 0% carried, 0% unknown)

- Draft: If you are a domestic cat, an African wildcat, an ocelot, a serval or a fishing cat, the pupil in the middle of each eye is a vertical slit. If you are a lion, tiger, leopard, jaguar, mountain lion or cheetah, your pupil is round. If you are a bobcat, a caracal, a Canada lynx or an Iberian lynx, it is nearly round, and if you are a Eurasian lynx, it is oval to diamond-shaped.
- Live: `g` Pupil: In bright light your pupil shrinks to an upright slit, as the pupils of your felid ancestors did. Lions and other large cats keep a round one.
- Cites: cat-dog#20 (Felis catus), oa-2#2289 (Felis silvestris), oa-2#2325 (Leopardus pardalis), sweep-66#3 (Leptailurus serval), oa-2#2307 (Prionailurus viverrinus), cat-dog#103 (Panthera leo), cat-dog#49 (Panthera tigris), oa-2#2311 (Puma concolor), oa-2#2351 (Panthera onca), oa-2#2353 (Panthera pardus), oa-2#2315 (Acinonyx jubatus), oa-2#2323 (Lynx rufus), oa-2#2339 (Caracal caracal), oa-2#2321 (Lynx canadensis), oa-2#2317 (Lynx pardinus), cat-dog#50 (Lynx lynx)

**cat, Sharpness** (draft grade `i`; of the species' records 38% measured, 2% carried, 60% unknown)

- Draft: If you are a domestic cat, you read about 10 cycles a degree, a third of the 30 that a human reads on an eye chart. If you are a cheetah, you read about 25. If you are a wildcat of the same genus as the domestic cat, such as a sand cat, you very likely see about as sharply as it does, but for the other cats nobody has measured how sharply you see.
- Live: `g` Sharpness: If you are a domestic cat, a chart test gave one gray tabby about 8 cycles per degree and a younger cat about 18, where a human reads about 30. Behavior studies put cats between 3 and 9.
- Cites: cat-dog#17 (Felis catus), cat-dog#94 (Acinonyx jubatus)

**dog, Color** (draft grade `m`; of the species' records 42% measured, 36% carried, 21% unknown)

- Draft: If you are a domestic dog, a red fox or an arctic fox, you have two kinds of color-sensing cell, where humans have three. In the domestic dog, one kind senses light most strongly at about 430 nanometers, a violet-blue, and the other at about 555 nanometers, a yellow-green.
- Live: `i` Colour: Dogs have two kinds of colour-sensing cells, where people have three. This view shows colours as a person with two kinds would see them.
- Cites: cat-dog#40 (Vulpes vulpes), cat-dog#64 (Canis lupus familiaris), cat-dog#65 (Canis lupus familiaris), intake-4#12 (Vulpes lagopus)

**bee, Speed** (draft grade `i`; of the species' records 0% measured, 26% carried, 74% unknown)

- Draft: If you are a honeybee, you can see a light flicker even when it flashes 200 times a second, where a human stops seeing flicker at about 60. In the bumblebee Bombus hortorum the limit is about 130 flashes a second. Nobody has measured it in wasps, carpenter bees or most other bees.
- Live: `m` Speed: In bright light, a honeybee can see a light flicker up to 200 times a second, where people stop at about 60. This view runs slowly and then jumps ahead to suggest the difference.
- Cites: bee#156 (Apis mellifera), bee#262 (Bombus hortorum)

**insect, Ultraviolet** (draft grade `g`; of the species' records 2% measured, 62% carried, 37% unknown)

- Draft: Monarchs, cabbage whites, small tortoiseshells and LD moths each have a color-sensing cell that senses ultraviolet best, and so do the drone fly, the seven-spotted ladybird, a dragonfly, a damselfly and the brown marmorated stink bug. You very likely have one as well. Ultraviolet is light that humans cannot see at all.
- Live: `g` Ultraviolet, blue and green: A copper butterfly has four pigments, peaking near 360, 437, 500 and 568 nanometers. A skipper has two, near 440 and 540, and a cockroach has only an ultraviolet one and a green one. You very likely have an ultraviolet receptor, a blue one and a green one.
- Cites: insect#8 (Danaus plexippus), insect#24 (Pieris rapae crucivora), methods#476 (Aglais urticae), methods#535 (Lymantria dispar), insect#167 (Eristalis tenax), insect#190 (Coccinella septempunctata), insect#109 (Anax junius), insect#125 (Ischnura elegans), oa-8#52 (Halyomorpha halys)

**jumper, Color** (draft grade `i`; of the species' records 0% measured, 22% carried, 78% unknown)

- Draft: If you are a regal jumping spider, your big front eyes have three kinds of color-sensing cell, and one kind senses ultraviolet. If you are a Plexippus validus, you have only two kinds, green and ultraviolet, and if you are a Habronattus pyrrithrix, you have three, with the red-sensing kind in a small patch at the center of the eye. Nobody has measured how many kinds you have if you are any other jumping spider.
- Live: `m` Colour: Most jumping spiders, Phidippus among them, see ultraviolet and green. Habronattus also sees red, in a small patch at the centre of each front eye, and this view adds red there when it knows the genus.
- Cites: jumper#163 (Phidippus regius), jumper#165 (Phidippus regius), jumper#21 (Plexippus validus), jumper#106 (Habronattus pyrrithrix), jumper#107 (Habronattus pyrrithrix)

**spider, The web** (draft grade `i`; of the species' records 22% measured, 0% carried, 78% unknown)

- Draft: If you are a golden silk spider, the insects caught in your web shake it 5 to 30 times a second, while air stirred by a flying insect seldom makes you attack and often makes you lift your forelegs. If you are a six-spotted fishing spider, you jump away from a striking frog, and the fine hairs called trichobothria that sense moving air are necessary and sufficient for that jump. For most other spiders, nobody has measured how you sense vibration or moving air.
- Live: `m` The web: A Golden Silk Spider feels its prey through the silk, and a trapped insect shakes the web 5 to 30 times a second. The shaking arrives ten to thirty times stronger on some legs than on others, which gives the direction.
- Cites: spider#43 (Trichonephila clavipes), spider#246 (Trichonephila clavipes, Zygiella x-notata), spider#34 (Zygiella x-notata, Nephila clavipes), spider#161 (Dolomedes triton)

**plant, Neighbors** (draft grade `i`; of the species' records 1% measured, 0% carried, 99% unknown)

- Draft: If you are a wood strawberry, your daughter plants grow more root over live substrate than over dead substrate, so you detect the state of a patch before you touch it. You also sense red and far-red light through a protein called phytochrome B. For nearly every other plant that borrows this row, nobody has measured whether you sense your neighbors by chemicals or by light.
- Live: (no live row with this title)
- Cites: harvest-11#2 (Fragaria vesca), harvest-13#7 (Fragaria vesca)

**deer, Field of view** (draft grade `i`; of the species' records 2% measured, 6% carried, 92% unknown)

- Draft: Your eyes sit on the sides of your head, so each one looks out in a different direction. Nobody has measured how wide an area you see at once, or how much of it both of your eyes see together in front of you. Both have been measured in cattle, goats, giraffes and horses, but in no deer.
- Live: (no live row with this title)
- Cites: squirrel-deer-rabbit#120 (Cervidae (deer, as the page states it)), intake-3#4 (Bos taurus), intake-3#5 (Bos taurus), intake-5#31 (Capra hircus), intake-5#32 (Capra hircus), intake-6#14 (Giraffa camelopardalis), squirrel-deer-rabbit#148 (Equus caballus), squirrel-deer-rabbit#92 (Equus caballus), sweep-29#6 (Giraffa camelopardalis)
<!-- rows-pipeline:end -->
