# Sensing sheet: ground invertebrates (snail, worm, scorpion, tick)

Research round 3, unit `ground-invertebrates`, written on 13 October 2026 from 01:47 to about 06:30 UTC. The evidence log is `docs/views/evidence/ground-invertebrates.jsonl` (lines are cited below as L1, L2 and so on, in file order) and the wanted list is `docs/views/wanted/ground-invertebrates.jsonl`. It builds on the checked sheets `docs/views/sheets/snail.md` and `docs/views/sheets/tick.md`, and every source behind a row was opened again in this session.

**What came through and what did not.** Of the two books in the owner's library, *Neurobiology of Arachnids* (Barth, ed., 1985) came through only as its front matter, chapters I to III and chapter IV to about page 73. The scorpion chapters (XVII, Root, on locomotion, and XVIII, Fleissner and Fleissner, on the clock in the visual system) and the chapters on sensilla, trichobothria and slit organs (VII to IX) were not in the copy. *Animal Eyes* (Land and Nilsson, 2nd edition, 2012) came through as chapters 1 and 2 and chapter 3 to about page 65, which holds its Table 3.1 of resolution. During the session these sites refused with HTTP 429 and I stopped fetching from them: Europe PMC (www.ebi.ac.uk), Zenodo's file store, doi.org for an Oxford title, and link.springer.com. The Biodiversity Heritage Library refused automated reading. The shell could reach only GitHub, so every page was read through the web tool.

**[unfinished]** items are marked where they occur. The main ones are these: no source I could open measures what a scorpion, harvestman or centipede resolves, so those three pictures rest on inference; no flicker or time-constant measurement was found for any animal in the unit; and the family counts behind the shares were read once, with no second count.

## 1. Scope

### What the four groups hold

Records are iNaturalist research-grade observations in GBIF (dataset `50c9509d-22c7-4a22-a47d-8c48425ef4a7`). The class and order totals come from the saved facets of 11 October 2026 (run 10 of `fetch` on the `ci` branch, `runs/fetch/10/`). The family splits were read from the GBIF API through the web tool on 13 October 2026. Species counts come from the iNaturalist open-data snapshot of 27 September 2026 (`runs/coverage/2-lists/world.tsv.gz` on `ci`, research grade, all years), so they differ slightly from GBIF's.

| Group | GROUPS label | Records | What it holds |
|---|---|---:|---|
| snail | a snail or slug | 2,227,162 | Gastropoda 2,155,631; Polyplacophora 71,088; Scaphopoda 376; two small classes 66; Monoplacophora 1 |
| worm | a worm, millipede or centipede | 370,232 | Diplopoda 170,881; Chilopoda 82,474; Annelida 66,007; Platyhelminthes 37,559; Nematoda 8,445; Nemertea 3,896; seven small phyla 970 |
| scorpion | a scorpion or harvestman | 235,122 | Opiliones 124,524; Scorpiones 99,357; Amblypygi 3,771; Uropygi 3,003; Pseudoscorpiones 2,399; Solifugae 1,810; Schizomida 222; Ricinulei 18; Palpigradi 18 |
| tick | a tick | 60,462 | Ixodida |

**Two of these totals are larger than `docs/COVERAGE.md` says.** The table of orders (`docs/views/world-orders.csv`) counts only records whose order has a saved name, and that misses two kinds of record.

- **Earthworms are missing.** GBIF places earthworms in order Crassiclitellata (key 5958860), and its 11,121 records sit in the world facet, but key 5958860 is absent from the saved order names, so the order never reached the table. It is the largest of seven unnamed orders (11,302 records in all). The worm group's 340,371 records therefore leave out every earthworm.
- **Families with no order are missing.** GBIF gives some families no order at all. Among annelids, Terebellidae (1,393), Arenicolidae (1,154) and Cirratulidae (622) are examples. Among flatworms, the sea flatworm family Pseudocerotidae (8,269) is one: Platyhelminthes hold 37,559 records, of which only about 24,500 carry an order. Among gastropods, the Alachua file itself lists Physidae, Planorbidae and Thiaridae with an empty order column, and Gastropoda hold 141,797 more records than their orders sum to. The corrected worm group is 370,232 (29,861 more than the table) and the corrected snail group 2,227,162 (141,797 more).

### Which members people photograph most

**Snails.** Worldwide the most recorded are the garden snail *Cornu aspersum* (110,204), the grove snail *Cepaea nemoralis* (74,500), the Roman snail *Helix pomatia* (52,599), the banana slug *Ariolimax columbianus* (47,423), the leopard slug *Limax maximus* (47,167) and the giant African land snail *Lissachatina fulica* (29,721); the first sea slug is *Hermissenda opalescens* (17,593) and the first sea snail the periwinkle *Littorina littorea* (16,050). Stylommatophora (land snails and slugs) hold 41.2% of the group, Nudibranchia 19.3% and chitons 3.2%. In Alachua County the most recorded are the manatee treesnail (*Drymaeus dormani*, 216), the Rosy Wolfsnail (*Euglandina rosea*, 198), the Ghost Bulimulus (145), the Florida Leatherleaf Slug (122), the Asian Tramp Snail (111) and the Island Apple Snail (*Pomacea maculata*, 109).

**Worms, millipedes and centipedes.** Millipedes hold 46.2% of the corrected group, centipedes 22.3%, annelids 17.8%, flatworms 10.1%, roundworms 2.3% and ribbon worms 1.1%.

- The most recorded millipedes are the Greenhouse Millipede *Oxidus gracilis* (28,389), the Rusty Millipede *Trigoniulus corallinus* (12,888), *Harpaphe haydeniana* (12,680), *Ommatoiulus moreleti* (8,676) and *Apheloria corrugata* (7,410).
- The most recorded centipedes are the house centipede *Scutigera coleoptrata* (26,123), *Scolopendra cingulata* (5,937), *S. polymorpha* (5,419), *S. heros* (3,811) and the brown centipede *Lithobius forficatus* (3,790).
- Among soft-bodied worms the leaders are the hammerhead worm *Bipalium kewense* (5,256), the earthworm *Lumbricus terrestris* (3,785), the fireworm *Hermodice carunculata* (3,588), the fan worm *Sabella spallanzanii* (2,999) and the horse leech *Haemopis sanguisuga* (2,305).
- In Alachua County the group's 414 records are led by the Greenhouse Millipede (65), the Rusty Millipede (59), the Wandering Hammerhead Worm *Bipalium vagum* (42), the Smokey Oak Millipede (41), the Florida Ivory Millipede (35), the Eastern Red Centipede *Scolopocryptops sexspinosus* (32), the Big-leg Centipede *Theatops posticus* (27) and the Shovel-headed Garden Worm *Bipalium kewense* (21). The county's two most recorded centipedes are blind ones.

**Scorpions and harvestmen.** Harvestmen hold 53.0% of the group and scorpions 42.3%; the remaining 4.7% are whip spiders, whip scorpions, pseudoscorpions, camel spiders and three tiny orders.

- Scorpion families: Buthidae 48.0%, Vaejovidae 20.6%, Scorpionidae 9.1%, Chactidae 6.7%, Bothriuridae 4.1%, Hormuridae 3.7%, Hadruridae 2.9%, Euscorpiidae 2.7%. The most recorded species are the striped bark scorpion *Centruroides vittatus* (11,594), *Uroctonus mordax* (4,698), *Vaejovis carolinianus* (2,202), the Arizona bark scorpion *C. sculpturatus* (2,028) and the giant hairy scorpion *Hadrurus arizonensis* (1,958).
- Harvestman families: Phalangiidae 59.1% and Sclerosomatidae 24.3%, together 83.4%; then Gonyleptidae 4.3%, Cosmetidae 4.0% and Nemastomatidae 2.4%. The most recorded species are *Phalangium opilio* (28,313), *Opilio canestrinii* (13,493) and the Banded Harvestman *Leiobunum vittatum* (8,392).
- In Alachua County the group's 106 records are the Hentz Striped Scorpion *Centruroides hentzi* (44) and five harvestmen led by *Hadrobunus grandis* (41).

**Ticks.** The American Dog Tick (20,209), the Eastern Black-legged Tick (11,235) and the Lone Star Tick (8,996) lead the world; the Lone Star Tick leads Alachua (121 of 152 tick records). The genus split is in `tick.md` and is not repeated here.

### Where the views should split

The four GROUPS labels cut across very different ways of meeting the world. Following Land and Nilsson's four classes of light-guided behaviour (L3, L4), the members fall into all of the first three: light sensed without direction (earthworm skin, the slug's brain), light with direction but no image (tick eyespots, flatworm cups), and coarse images (millipede and snail eyes, scorpion median eyes). None reaches the fourth class, sharp sight, except the conchs among the sea snails. Each line below says where one picture would be false for some members.

1. **The scorpion group splits into scorpions and harvestmen.** Scorpions carry two eye systems, a pair of median eyes and up to five lateral eyes on each side, that answer to different tasks and grow about a thousand times more sensitive at night (L10, L11, L26, L27, L43, L44). Harvestmen carry one pair of eyes on a turret looking sideways and live largely by touch and taste through their first legs and palps (L52, L53, L57, L58). Whip spiders and whip scorpions share the scorpion's layout of median and lateral eyes (L37, L70) and go with scorpions. The line falls between Opiliones (124,524, 53.0%) and the rest (110,598, 47.0%).
2. **The worm group splits three ways: millipedes, centipedes and soft-bodied worms.** Millipedes have at most low-resolution eyes and half of them have none (L77, L79, L89, L92, L93). Centipedes are fast predators whose eyes range from a compound eye of 150 to 200 facets in the house centipede to none at all in soil centipedes (L97 to L101), and some sense sunlight as heat in their antennae (L104). The soft-bodied worms (earthworms, leeches, flatworms, fan worms, ribbon worms) sense light through the skin or through eyecups that give direction without an image (L106, L107, L114, L119 to L124). The shares are millipedes 170,907 (46.2%, counting the 26 records of Pauropoda with them), centipedes 82,474 (22.3%) and soft-bodied worms 116,851 (31.6%).
3. **Within millipedes the line between eyed and eyeless orders is real, and I recommend one view for now.** The flat-backed millipedes (Polydesmida) and Platydesmida have no eyes (L89, L92, L93) and hold 84,181 records (49.3% of millipedes), including the most recorded species. The rest, 86,700 (50.7%), are mostly eyed orders, though some of their members are blind. At the measured sharpness of an eyed millipede, 56 degrees a cycle (L77), the picture is so coarse that it differs from no picture at all only in showing which side is darker. The eyeless half would get that faint cue too, and a row says so. When the full database names a species in Polydesmida or Platydesmida, the same view should drop to `field: 1`.
4. **Within centipedes, one view for now, with the house centipede as the first split later.** Scutigeromorpha (30,822, 37.4%) have compound eyes and two colour classes (L94 to L98); Scolopendridae (34,892, 42.3%) have four simple eyes on each side (L99); Lithobiomorpha hold 8.1%; and the blind families (Cryptopidae, Scolopocryptopidae and Geophilomorpha) hold 10,093 (12.2%) (L100, L101). No centipede's sharpness has been measured in any source I opened, so a split cannot yet be drawn from numbers.
5. **Within soft-bodied worms, one view.** Fan worms (Serpulidae and Sabellidae, 23,534, 20.1% of soft worms) and leeches (8,014, 6.9%) have eyes that catch shadows (L111, L114, L124). Earthworms (11,121, 9.5%) have no eyes and sense light through the skin (L106, L107). Land planarians (22,813, 19.5%) have many tiny eyes (L169). The remaining polychaetes (23,177, 19.8%), led by fireworms and honeycomb worms, were not measured in any source I opened. All of them meet light as amount and direction, and none is shown to resolve an image, so one view without a picture is true for all. Gall nematodes (most of the 8,445 roundworm records, in Anguinidae 8,245) are photographed as galls on plants, as gall mites are, and should go to `other`.
6. **The snail group keeps one view, as `snail.md` proposed.** The sea snails with large camera eyes are the exception: the strombid conchs resolve about 1 degree (L130, L131) and the periwinkle about 4.5 degrees between receptors (L1). Strombidae hold 12,703 records (0.57% of the group) and Littorinidae 45,606 (2.05%), together 2.6%. Every other member measured sees at most large patches of light and dark (L125, L126, L133, L134, L146, L181). A `conch` view for Strombidae is the first split to make when the full database names species.
7. **Ticks keep one view, as `tick.md` proposed.** The new evidence for the Lone Star Tick's own eye (L151, L152) supports the coarse picture there.

**The set of views I commit to** is seven: `snail`, `millipede`, `centipede`, `worm`, `scorpion`, `harvestman` and `tick`. The base app's group head knows only four labels, so the three new ones (`millipede`, `centipede`, `harvestman`) need the owner's word and a refit of the head on the existing world photos (`docs/COVERAGE.md`, second wave). Until then the full database can route by order. In the word table, "millipede" and "centipede" now go to `worm` and "harvestman" to `scorpion`.

## 2. The views

Blur radii below use the rule in `src/cam.b.js` (radius = 0.6 × long side ÷ `VIEW_DEG` ÷ `cpd`) with `VIEW_DEG` 24 on a phone and 34 elsewhere. Conversions from degrees to cycles per degree are mine and are given beside each value. Fields marked **invented** are the app's own choice. Several effects use engine features that track C is building now (zones, the motion-salience map and the phone's motion sensors and microphone; `docs/tracks/engine.md`).

### 2.1 `snail`: snails, slugs, sea slugs and chitons

**Rows**

```
['m', 'Eyes', 'A land snail or slug has a small eye with a lens at the tip of each upper tentacle. The lens cannot bring an image into focus on the shallow retina behind it, so the eye gathers the brightness of a wide patch of the world.'],
```
Log: L183 (Matsuo, Kawakami and Matsuo 2024, eye_type), L133 (Zieger and Meyer-Rochow 2008, eye_type), L125 (Zieger and colleagues 2008, eye_type).

```
['m', 'Sharpness', 'In behaviour tests the red slug told apart shapes about 52 degrees across, the width of a metre-wide shape seen from a metre away. This view is blurred until only the broad lie of light and dark remains.'],
```
Log: L128 (Irwin and colleagues 2022, citing Zieger and colleagues, acuity_cpd), L134 (Zieger and Meyer-Rochow 2008, acuity_cpd), L126 (Zieger and colleagues 2008, behaviour_vision). A shape 1 m wide at 1 m spans 2 × atan(0.5) = 53 degrees.

```
['m', 'Colour', 'In the snail Helix lucorum, of the same genus as the Roman snail, the eye is most sensitive to blue-green light near 496 nanometres, and both of its kinds of light-sensing cell share that peak. A snail therefore cannot tell colours apart, and this view is drawn in grey weighted toward blue-green.'],
```
Log: L138 (Chernorizov and colleagues 1993, lambda_max_nm), L139 (Chernorizov and colleagues 2007, receptor_classes).

```
['m', 'Day and night', 'A slug's eye changes its sensitivity with the light. In the dark it responds best near 480 nanometres, and in daylight near 420, a deeper blue. This view shifts its grey toward blue as the scene grows brighter.'],
```
Log: L141, L142, L143 (Matsuo and colleagues 2023, lambda_max_nm dark and light, receptor_classes).

```
['m', 'Brightness', 'The signal from a snail's eye grows with the logarithm of the light, so each tenfold rise in brightness adds the same small step. This view compresses bright areas in the same way.'],
```
Log: L140 (Shekhter, Zimachev and Arakelov 1993, absolute_sensitivity).

```
['m', 'Finding the dark', 'Slugs use their eyes mainly to find dark places to hide. The red slug and the field slug turn away from light, and they need no sharper picture for that.'],
```
Log: L126, L125, L127 (Zieger and colleagues 2008, behaviour_vision, eye_type, polarization).

```
['m', 'Light without eyes', 'A slug whose eye stalks have been removed still finds the dark end of a chamber, more slowly, because light-sensitive cells in its brain respond to blue light. Some of these brain cells are wired to the eyes.'],
```
Log: L144 (Knight 2019, summarising Nishiyama and colleagues 2019, sense_light_nonvisual), L184 (Matsuo, Kawakami and Matsuo 2024, sense_light_nonvisual).

```
['m', 'Sea slugs', 'A nudibranch's small eyes lie deep inside its body, on top of the brain. They tell light from dark, and the animal smells the water with the pair of horns on its head, called rhinophores.'],
```
Log: L181, L182 (Rudman 1999, eye_type, sense_chemical).

```
['g', 'Water snails', 'Some snails that live in water see more. A conch makes out details about 1 degree across, and a periwinkle's eye samples the world about every 4.5 degrees. Pond snails can focus an image under water in a deep pit of the retina. This view follows the land snails and sea slugs, which make up most of the records.'],
```
Log: L130, L131 (Irwin and colleagues 2022, Conomurex), L1 (Land and Nilsson 2012, Littorina), L137 (Gál and colleagues 2004, Lymnaea), L136 (Zieger and Meyer-Rochow 2008, Lymnaeidae).

```
['m', 'Chitons', 'A few kinds of chiton carry hundreds of tiny eyes in their shell plates, with lenses of the mineral aragonite, and resolve shapes about 9 to 12 degrees across. All chitons also sense light through fine pores in the shell.'],
```
Log: L146 (Speiser, Eernisse and Johnsen 2011, acuity_cpd), L147 (Liu, Sigwart and Sun 2023, eyes_count), L145 (Kingston, Chappell and Speiser 2018, behaviour_vision).

```
['x', 'Smell', 'A leopard slug finds its way home from almost a metre away by smell, walking upwind, and needs neither its slime trail nor its eyes to do it. No phone can sense smell, so it is left out.'],
```
Log: L148 (Gelperin 1974, sense_chemical).

**The picture.** A grey field of one or two broad soft patches, brighter where the sky or a lamp is and darker toward cover, weighted to blue-green, with bright light compressed. As the scene brightens the grey slides toward blue. Still things stay, since chitons orient to still shapes (L145) and slugs steer by where the dark lies (L126).

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Snail', 'a snail or slug' | `who` is the GROUPS label; `chip` **invented** |
| `cpd` | .02 | L128 and L134. The red slug's 52 degrees gives 1 / 52 = 0.019 read as a full cycle and 1 / (2 × 52) = 0.0096 read as half a cycle; the review says land snail eyes average light over large angles. Choosing .02 within that range is **invented**. Blur radius 1.25 of the long side at `VIEW_DEG` 24 and 0.88 at 34. `snail.md` used .035 from a garden snail figure of 14.5 degrees whose cited source is a study of *Littorina irrorata* (its title is in the collection index: Hamilton and Winter 1982, "Behavioural responses to visual stimuli by the snail Littorina irrorata"), so .035 is withdrawn. |
| `M` | [.05, .45, .5] in every row, dark-adapted | L138, L141. One pigment near 480 to 496 nm sits between the camera's blue and green, so blue and green are weighted about equally and red little. The weights are **invented**. |
| `M` in bright scenes (new, see below) | [.05, .25, .7] | L142. The light-adapted peak near 420 nm moves the weight to blue; weights **invented**. |
| `sat` | 0 by construction (equal rows) | L139 |
| `gain` | 1.3 | L135 says land snails see well in dim and bright light. The amount is **invented**. |
| `pupil` | 'none' | `snail.md` cited a round pupil (Shepeleva 2023); I opened only that paper's abstract, which does not state the shape. With `dof` unset the picture is the same either way. |
| `field`, `gate`, `persist`, `rate`, `fov` | unset | No flicker or field measurement was found; still things are kept (L145). |
| `cue` | 'Hold the phone low and turn it slowly. Only the broad lie of light and dark remains, and bright light counts for less than you expect.' | **invented** wording |

**New effects**

| Effect | What the person sees | Phone input | Difficulty | Beautiful and true |
|---|---|---|---|---|
| Brightness on a log scale (`logL: 1`, new field) | Bright windows and sky flatten toward the mid-greys while shadows keep their steps. | none, the camera picture | easy, one tone curve in the colour pass | The flattening follows L140. Draw it as a smooth curve, never as clipping. |
| Day and night colour (`adaptM`, new field) | Over two or three seconds the grey cools toward blue as the scene brightens and warms toward blue-green as it darkens. | mean brightness from the frame ring | easy | L141 and L142. A slow drift reads as an eye adapting, which is what it is. |
| Light in the brain | When the person covers the lens, a faint even glow follows the room's light. | the front camera's mean brightness, where a browser lets both cameras run; otherwise none | hard, and not available on many phones | L144. I recommend it only if both cameras can run together without cost. |
| Smell | none | none | impossible | It stays a row. |

### 2.2 `millipede`: millipedes (Diplopoda, with Pauropoda)

**Rows**

```
['m', 'Eyes', 'Most millipedes have a small cluster of large-faceted eyes on each side of the head. The flat-backed millipedes, among them the greenhouse millipede, which is photographed more than any other, have no eyes at all.'],
```
Log: L79 (Kirwan and Nilsson 2019, eye_type), L89 (Fox 2006, eyes_count), L92 (Marek and Bond 2009, eyes_count), L93 (Moritz and colleagues 2021, eyes_count).

```
['m', 'Sharpness', 'A snake millipede can make out a dark band about 20 degrees wide, enough to find a dark crevice and little more. A person sees detail about three thousand times finer. This view is blurred to match.'],
```
Log: L77, L78, L80 (Kirwan and Nilsson 2019, acuity_cpd, acceptance_deg, behaviour_vision). A 56 degree period is 1 / 56 = 0.018 cycles per degree, and 60 / 0.018 = 3,333.

```
['m', 'Light through the skin', 'The greenhouse millipede senses light through its skin. Light makes it walk more without steering it anywhere, so it keeps moving until it happens upon a dark place.'],
```
Log: L84 (Cloudsley-Thompson 1951, sense_light_nonvisual). The species was studied as *Paradesmus gracilis*.

```
['m', 'Touch', 'A walking millipede taps the ground constantly with the tips of its antennae, and touch shapes most of what it does.'],
```
Log: L90 (Fox 2006, sense_touch), L86 (Cloudsley-Thompson 1951, sense_touch).

```
['m', 'Taste and damp', 'A millipede tastes food by touching it, and in tests it showed no response to smells. Drying out keeps it walking, and once it settles on damp ground it is slow to move again.'],
```
Log: L87, L88 (Cloudsley-Thompson 1951, sense_chemical), L91 (Fox 2006, sense_chemical, graded g).

```
['m', 'Temperature', 'The greenhouse millipede prefers ground near 15 degrees Celsius, and a sudden drop in temperature sets it moving.'],
```
Log: L85 (Cloudsley-Thompson 1951, sense_thermal).

```
['g', 'Night', 'Many millipedes come out only at night. The luminous millipede Paraspirobolus lucifugus avoids light and keeps a daily clock.'],
```
Log: L83 (Meyer-Rochow and Yamahama 2022, diel).

```
['x', 'Shaking ground', 'A millipede curls into a tight spiral when it is disturbed, and very slight vibrations set it walking. The camera records none of this.'],
```
Log: L86 (Cloudsley-Thompson 1951, sense_touch; the summary links the spiral reflex to vibration).

**The picture.** Almost no picture: the whole frame is one soft gradient, darker on the side where the dark lies, in grey. It is the plant's `field: 1` with one difference, which side is darker, because eyed millipedes steer to dark targets (L80).

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Millipede', 'a millipede' | **invented** |
| `cpd` | .018 | L77: 1 / 56. Blur radius 1.39 of the long side at `VIEW_DEG` 24. |
| `sat` | 0 | No millipede spectral measurement was found; grey is **invented**. |
| `field` | unset; 1 for Polydesmida and Platydesmida when the full database names the species | L89, L92, L93 |
| `gate`, `persist`, `rate`, `gain` | unset | No measurement found. |
| `cue` | 'Point the phone at the ground under leaves and turn it slowly. Only the darker side of the scene remains.' | **invented** |

**New effects**

| Effect | What the person sees | Phone input | Difficulty | Beautiful and true |
|---|---|---|---|---|
| Curling | A sharp shake of the phone makes the picture wind into a dark spiral, which unwinds after a few seconds. | device motion | medium (a swirl warp and a timer) | L86. The spiral is the animal's own defence, and a slow unwinding makes a fine moment. The timing is **invented**. |
| Walking faster in light | In bright scenes the faint gradient drifts and searches across the frame; in the dark it settles. | mean brightness | easy | L84 (light changes speed, not direction). |
| Antennae | Each touch of the screen leaves a soft print that fades, as if tapped out. | the touch screen | easy | L90. It shows the sense that leads; the print's look is **invented**. |

### 2.3 `centipede`: centipedes (Chilopoda)

**Rows**

```
['m', 'Eyes', 'The house centipede has a compound eye of about 150 to 200 facets on each side of its head. Most large tropical centipedes have four simple eyes on each side, and the soil centipedes have none.'],
```
Log: L97 (Müller and colleagues 2011, eyes_count), L98 (Hemenway 1900, eyes_count), L99 (Edgecombe and colleagues 2019, eyes_count), L101 (Roberts 2014, eyes_count), L100 (Edgecombe and Koch 2008, eyes_count).

```
['m', 'Colour', 'The house centipede's eye is most sensitive to blue light near 448 nanometres and has a second peak in ultraviolet near 350. It probably has two kinds of colour-sensing cell. This view weights its grey toward blue and leaves the ultraviolet out.'],
```
Log: L94, L95, L96 (Meyer-Rochow, Müller and Lindström 2006).

```
['i', 'Sharpness', 'No one has measured how much detail a centipede sees. This view assumes the house centipede sees nearly three times as sharply as a millipede, because its eye has about seven times as many facets.'],
```
Log: L77 (millipede sharpness), L81 (about 23 facets in a millipede eye), L97, L98. The arithmetic is under the picture.

```
['m', 'Dark shapes', 'Centipedes run from light and toward dark shapes. The house centipede, the brown centipede and a large Scolopendra all head for a dark screen at the side of an arena.'],
```
Log: L102, L103 (Lewis 1981, behaviour_vision).

```
['m', 'Sunlight as heat', 'A large Asian centipede feels sunlight as heat in its antennae, which warm by more than 8 degrees Celsius within ten seconds of strong sun. With its antennae covered in foil it was slower to flee the light.'],
```
Log: L104, L105 (Yao and colleagues 2023).

```
['m', 'Smell and touch', 'A centipede's long antennae carry several kinds of sensory hairs and feed large centres for smell and touch in its brain. The brown centipede releases a scent from pores at the bases of its legs that others of its kind respond to.'],
```
Log: L186 (Sombke and colleagues 2011, sense_chemical), L187 (Littlewood and Blower 1987, sense_chemical).

```
['g', 'Soil centipedes', 'Soil centipedes are blind. In one of them every known gene for sensing light is missing, while the house centipede keeps those genes.'],
```
Log: L101 (Roberts 2014, eyes_count).

```
['x', 'Not in the picture', 'A centipede finds prey and mates largely by smell and touch through its antennae, and a camera records neither.'],
```
Log: L186, L187.

**The picture.** Coarse and grey-blue, with large dark shapes standing out, a little sharper than the millipede's. A slow warm glow builds at the top edge when the phone stays pointed into bright light (see effects).

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Centipede', 'a centipede' | **invented** |
| `cpd` | .05 | **invented** by inference: about 175 facets (L97, L98) against about 23 in one millipede eye (L81) is a ratio of about 7.6; if sharpness grows with the square root of the facet count over a similar field, the house centipede resolves about 2.8 times finer than a millipede's 56 degree period (L77), about 20 degrees, which is 0.05 cycles per degree. Blur radius 0.5 of the long side at `VIEW_DEG` 24. The assumption of a similar field is mine. |
| `M` | [.05, .25, .7] in every row | L94: one blue peak near 448 nm; weights **invented** |
| `gate`, `persist`, `rate`, `gain`, `fov` | unset | No measurement found. |
| `cue` | 'Turn toward a dark gap. Large dark shapes stand out, and bright light slowly warms the top of the view.' | **invented** |

**New effects**

| Effect | What the person sees | Phone input | Difficulty | Beautiful and true |
|---|---|---|---|---|
| Sunlit antennae | When the scene stays bright for several seconds, two warm filaments at the top of the frame glow orange and spread, and the picture darkens as if turning away. In shade they cool within seconds. | mean brightness over the last ten seconds | easy | L104 gives the time scale (more than 8 °C within 10 s, fast cooling). The filaments read as antennae and carry a real finding. Their colour and the threshold are **invented**. |
