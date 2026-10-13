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

### 2.4 `worm`: earthworms, leeches, flatworms, fan worms and ribbon worms

**Rows**

```
['m', 'No eyes', 'An earthworm has no eyes. Light-sensitive cells lie in the skin of every segment, most of them at the head and the tail, and tiny windows in a layer of pigment let light reach them from set directions.'],
```
Log: L106, L107 (Hess 1925, sense_light_nonvisual, eye_type), L167 (Hess 1923, sense_light_nonvisual).

```
['m', 'Bright and dim', 'An earthworm crawls away from ordinary light, but it moves toward light that is very dim.'],
```
Log: L168 (Hess 1923, behaviour_vision).

```
['m', 'A mole digging', 'Florida earthworms rush out of their burrows when the ground carries the vibration of a digging mole. Bait collectors copy it by scraping a stake driven into the soil, and worms come up as far as 12 metres away.'],
```
Log: L176 to L179 (Catania 2008, sense_vibration), L108, L109 (Mitra and colleagues 2008, sense_vibration).

```
['m', 'Leeches', 'A medicinal leech has five pairs of eyecups on its head and seven pairs of light-sensing spots in every segment of its body. The spots on its back respond best to green light, and those underneath to ultraviolet.'],
```
Log: L114, L115 (Groves and Jellies 2021, eyes_count, lambda_max_nm), L111, L112 (Stowasser and colleagues 2019, eyes_count, receptor_classes).

```
['g', 'Flatworms', 'Each cup-shaped eye of a freshwater planarian samples the world about every 35 degrees, and the animal flees ultraviolet light most strongly. It still flees near-ultraviolet light after its eyes are removed. Land planarians, such as the hammerhead worms, have many tiny eyes on the head.'],
```
Log: L2, L5 (Land and Nilsson 2012, interreceptor_deg, eye_type), L119 (Paskin and colleagues 2014, behaviour_vision), L120, L121 (Birkholz and Beane 2017), L169 (Bertone 2020, eyes_count).

```
['m', 'Fan worms', 'Fan worms and Christmas tree worms have eyes on their feathery tentacles. Their light-sensing pigment peaks at 464 nanometres, close to the blue light of a shallow reef, and a passing shadow makes them pull back into their tubes at once.'],
```
Log: L123, L124 (Bok and colleagues 2017, lambda_max_nm, eye_role).

```
['x', 'Touch, taste and damp', 'Worms meet most of the world through touch, taste and moisture. A leech's skin answers vibration up to about 50 times a second, and land planarians need damp ground to live. None of this reaches a camera.'],
```
Log: L118 (Laverack 1969, sense_touch), L170 (Bertone 2020, sense_chemical), L122 (Ascunce and colleagues 2026, sense_chemical).

```
['i', 'The picture', 'This view shows only how much light there is, where it comes from and how it changes, and it counts ultraviolet and blue light most. That weighting follows the planarians and leeches and is the app's own choice.'],
```
Log: L119 (planarian hierarchy), L115 (leech sensilla).

**The picture.** No image. The frame is a soft field whose brightness follows the scene, brighter on the side the light comes from, in grey drawn from the camera's blue more than its red. A sudden shadow makes it flinch shut.

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Worm', 'a worm or leech' | **invented**; the GROUPS label would change once millipedes and centipedes have views of their own |
| `cpd` | .014 | L2: the planarian's 35 degrees, 1 / (2 × 35) = 0.014. Blur radius 1.79 of the long side at `VIEW_DEG` 24, so only a gradient remains. Earthworms have no eyes at all (L107); for them the gradient stands for the directional windows in the skin, and that reading is mine. |
| `M` | [0, .3, .7] in every row | L119, L115; weights **invented** |
| `field`, `gate`, `rate` | unset | A shadow must register at once (L124), so no averaging. |
| `cue` | 'Hold still and let a hand pass over the phone. There is no picture, only light, its direction and the shock of a shadow.' | **invented** |

**New effects**

| Effect | What the person sees | Phone input | Difficulty | Beautiful and true |
|---|---|---|---|---|
| Shadow alarm | When the frame darkens sharply (for example by a third within a third of a second), the field contracts to a dark point, as a fan worm pulls in, and opens again over two or three seconds. | the camera's mean brightness | easy | L124 (fan worms), L113 (the leech's whole-body S cell). The fan opening again is the beautiful part. Thresholds and timing are **invented**. |
| A mole digging | A low rumble or knocks on the table make the field rise and brighten, as a worm surfaces, and settle when the ground is quiet. | the microphone's energy between about 50 and 300 Hz, with consent, or the motion sensors | medium | L177 (grunting near 80 Hz, a mole near 200 Hz), L176. The band is taken from those peaks; the response is **invented**. |
| Dim light | In near darkness the bright side draws the field toward it; in ordinary light the field leans away. | mean brightness | easy | L168 |
| A leech's body of eyes | With the phone held flat and face up, the top half of the frame leans green and the bottom half blue, as the sensilla on the back and belly do. | device orientation, and the zones of track C | medium | L115. It is a true detail; **invented** in its proportions. |

### 2.5 `scorpion`: scorpions, whip spiders, whip scorpions, pseudoscorpions and camel spiders

**Rows**

```
['m', 'Two kinds of eyes', 'A scorpion has a pair of larger eyes on top of its front shield and a row of two to five small eyes along each front corner. The middle eyes may form a rough image, and the side eyes serve as very sensitive detectors of light.'],
```
Log: L10, L11 (Prévost and Stemme 2020, eyes_count, eye_role), L43, L44 (Lehmann and Melzer 2013, eye_role), L49 (Loria and Prendini 2014, eyes_count), L46 (Yang and colleagues 2013, eyes_count).

```
['m', 'Night sight', 'A scorpion's middle eyes grow about a thousand times more sensitive at night under a daily clock, and its side eyes are about ten times more sensitive than that. This view lifts the shadows after dark by the phone's own clock.'],
```
Log: L26, L27, L28 (Fleissner 1977, absolute_sensitivity and diel, in *Androctonus australis*), L15 (Prévost and Stemme 2020). Loria and Prendini (L50) give ten log units for the side eyes' margin, which conflicts with Fleissner's own one log unit; the row follows Fleissner.

```
['m', 'Colour', 'Both kinds of eye respond best to green light near 500 nanometres, and the side eyes respond to ultraviolet as well. Scorpions see red poorly, though in sensitive tests they still turn toward it. This view draws the world in green-weighted grey and lets red fall dark.'],
```
Log: L12, L13, L14 (Prévost and Stemme 2020), L23, L24 (Machan 1968, receptor_classes), L34 (Rivera Roldan and Gaffin 2018, behaviour_vision), L41 (Pulido Forero 2026, lambda_max_nm in *Centruroides*).

```
['m', 'A glowing body', 'Under ultraviolet light a scorpion's outer skeleton glows blue-green, though the lenses of its eyes do not. Scorpions with their eyes covered still reacted to ultraviolet light, which suggests the whole body helps to catch it.'],
```
Log: L35, L36 (Yong 2011, reporting Gaffin and colleagues 2012), L33 (Kloock, Kubli and Reynolds 2010), L17 (Prévost and Stemme 2020), L48 (Yang and colleagues 2013, filter_pigments).

```
['m', 'Light in the tail', 'Nerve cells in a scorpion's tail respond to light, most strongly to yellow-green near 568 nanometres.'],
```
Log: L32 (Geethabali and Rao 1973, in *Heterometrus*).

```
['m', 'Ripples in sand', 'A sand scorpion feels the ripples a moving insect sends through sand up to half a metre away, through slit-shaped sensors in each of its eight legs. It works out the direction of prey up to 20 centimetres away from the order in which its legs feel the ripple.'],
```
Log: L29, L30 (Brownell 1977), L31 (Brownell and van Hemmen 2001), L8 (Babu 1985).

```
['m', 'Combs that taste the ground', 'Under its body a scorpion carries a pair of comb-like organs, the pectines, with thousands of sensors that touch and taste the ground. A male striped bark scorpion responds strongly to the traces a female leaves on the ground.'],
```
Log: L19 (Prévost and Stemme 2020, sense_chemical), L171 (Steinmetz, Bost and Gaffin 2004), L172 (Gaffin, Muñoz and Hoefnagels 2022).

```
['m', 'Air and damp', 'Fine upright hairs on the pincers feel the slightest current of air, and hairs on the feet sense damp ground and water vapour.'],
```
Log: L21, L20 (Prévost and Stemme 2020, sense_airflow, sense_chemical), L174 (Ashford and colleagues 2018), L175 (Murayama and Willemart 2019).

```
['m', 'Whip spiders and whip scorpions', 'Whip spiders hunt at night and find their way home with their long, feeler-like front legs, even with their eyes covered. A whip scorpion's middle eyes form a clear image, and it senses light through its skin as well as its eyes.'],
```
Log: L69, L71 (Lehmann and Melzer 2018), L72 (Bingman and colleagues 2016), L73 (Flanigan and colleagues 2021), L38 (Meyer-Rochow 1987), L74 (Patten 1919).

```
['x', 'Not in the picture', 'A scorpion hunts and finds its way largely by vibration in the ground, currents of air and the taste of the ground, and scorpions with painted eyes still found their way home. The camera records none of these senses.'],
```
Log: L22 (Prévost and Stemme 2020, *Mesobuthus eupeus*), L180 (Locket 2001), L31, L19.

```
['i', 'Sharpness', 'No one has measured how much detail a scorpion's eyes resolve. This view assumes the middle eyes make out shapes a few degrees across, as the clear image in a whip scorpion's middle eye suggests, and leaves the side eyes as soft patches of light.'],
```
Log: L38, L11. The arithmetic is under the picture.

**The picture.** A wide view squeezed into the screen. The middle holds rough shapes in green-weighted grey; the edges hold soft, brighter patches that gather light. After dark by the phone's clock the shadows lift strongly. Red objects fall dark.

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Scorpion', 'a scorpion' | `who` would replace 'a scorpion or harvestman' once harvestmen have their own view; **invented** |
| `fov` | 360 | L16 (360 degrees by physiology, Locket as cited). The engine clamps the squeeze at 0.45. |
| `cpd` | .1 in the middle (median-eye zone); .02 at the sides (lateral-eye zones) | **invented** by inference. The whip scorpion's median lens forms an image about 200 µm behind it and its rhabdoms are up to 20 µm wide (L38). A receptor 10 to 20 µm wide at 200 µm subtends 2.9 to 5.7 degrees, which gives 0.09 to 0.17 cycles per degree; .1 sits at the coarse end. The lateral eyes form no clear image (L11, L51); .02 is **invented**. Blur radius 0.25 of the long side for the middle at `VIEW_DEG` 24. |
| `M` | [.05, .7, .25] in every row | L12, L41: one green peak near 500 to 525 nm; weights **invented** |
| `gain` | 1 by day; 2.5 at night by the phone's clock, with a two-hour ramp at dusk and dawn; the side zones twice the middle's | L26 (3 log units), L27 (side eyes 1 log unit more), L28 (2 to 3 hour transitions). A screen cannot show a thousandfold change, so the amounts are **invented**. |
| `pupil`, `gate`, `persist`, `rate` | unset | No measurement found. |
| `cue` | 'Look along the ground in the evening. The middle holds rough shapes, the edges only gather light, and red goes dark.' | **invented** |

**New effects**

| Effect | What the person sees | Phone input | Difficulty | Beautiful and true |
|---|---|---|---|---|
| Night by the clock | Toward evening the shadows lift and the side patches brighten; by morning they settle. | the phone's clock and time zone | easy | L26 to L28. The view changes with the hour, as the scorpion's eyes do. |
| Glowing rim | In light rich in blue and violet, a cyan-green glow rises around the edge of the frame, with small dark spots where the eyes would be, because the lenses do not glow. | the camera's blue level, standing in for ultraviolet | medium (an overlay pass) | L35, L36, L48. The camera records too little ultraviolet to drive this from the true signal, so it is **invented** in its trigger and must carry an `i` row if added. The glow with dark eye-spots is a striking and true image. |
| Ripples in sand | Knocks felt through the phone send rings across the picture from the side the knock came from. | device motion (the sign of the first jolt) | medium | L31. A phone cannot time a wave across eight legs, so the direction is **invented**. |
| Air on the pincers | Wind on the microphone makes the edge patches shimmer. | microphone, with consent | medium | L21, L174; **invented** in form |

### 2.6 `harvestman`: harvestmen (Opiliones)

**Rows**

```
['m', 'Eyes', 'A harvestman has a single pair of eyes, set back to back on a small turret in the middle of its body. Each eye looks out to one side.'],
```
Log: L52, L53 (Lehmann and colleagues 2016, eyes_count, eye_role), L66 (Friedrich 2024, eyes_count).

```
['m', 'Rough images', 'A harvestman's eyes probably give only a rough picture of light and dark. A large dark object makes a species of Leiobunum flee, and in the laboratory harvestmen move away from light.'],
```
Log: L53, L54, L55 (Lehmann and colleagues 2016).

```
['m', 'Hidden eyes', 'The most photographed harvestman, Phalangium opilio, also carries two more pairs of eyes inside its body, both shrunk to traces. They may help set its daily clock.'],
```
Log: L65 (Friedrich 2024, eyes_count).

```
['g', 'Colour and dim light', 'In two cave harvestmen from New Zealand the eyes respond to ultraviolet, blue and green light, over a range of brightness of at least a hundred thousand to one. Their lenses gather light about as well as a camera lens set to f/1.'],
```
Log: L62, L63 (Meyer-Rochow and Liddle 1988, lambda_max_nm, absolute_sensitivity), L59, L60 (f_number). Five log units is 100,000 to 1.

```
['m', 'Touch and taste', 'Harvestmen find food, mates and enemies mostly by touching and tasting them with their first pair of legs and their palps, and they sense little from a distance.'],
```
Log: L57, L58 (Willemart, Farine and Gnaspini 2008), L68 (Willemart and Chelini 2007).

```
['g', 'Smell close up', 'Some harvestmen smell food from a short distance. One South American species found fresh dead crickets hidden under mesh.'],
```
Log: L67 (Costa and Willemart 2013).

```
['g', 'Finding the way', 'A South American harvestman uses its eyes to find its way back to its eggs, and relies on the memory of its own steps when its eyes are covered.'],
```
Log: L64 (Silva and colleagues 2018).

```
['x', 'Not in the picture', 'The touch and taste of a harvestman's legs and palps carry most of what it knows, and the camera records neither.'],
```
Log: L57, L58.

```
['i', 'Sharpness and field', 'No one has measured how much detail a harvestman sees. This view assumes coarse sight of a few large shapes, clearest out to each side.'],
```
Log: L53.

**The picture.** Two soft windows, one on each side of the screen, with large dark shapes in grey; the middle of the screen, straight ahead, is dim.

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Harvestman', 'a harvestman' | **invented** |
| `cpd` | .05 | **invented**: "rough image of light and dark" (L53), set between the millipede's .018 and the tick's .07 |
| zones | left and right bands at full brightness; the central third dimmed to about half | L53 (fields extend sideways); proportions **invented** |
| `sat` | 0 | No spectral measurement in common species; the cave species (L62) are too far from the commonest to set a colour matrix. **invented** |
| `gain` | 1.2 | L59, L60 (fast lenses) in cave species; amount **invented** |
| `cue` | 'The view looks out to both sides at once, and straight ahead is dim.' | **invented** |

**New effects**

| Effect | What the person sees | Phone input | Difficulty | Beautiful and true |
|---|---|---|---|---|
| Two side windows | The picture splits softly into left and right fields from one turret, with a dim seam ahead. | none (zones) | easy once zones exist | L52, L53 |
| Tasting legs | A touch on the screen flashes a small coloured bloom that fades, as a leg tip tastes what it meets. | the touch screen | easy | L57, L58; **invented** in form |

### 2.7 `tick`: ticks (Ixodida)

**Rows**

```
['m', 'Eyes', 'The Lone Star Tick has a simple eye on each side, a single lens over 30 to 40 light-sensitive cells. The black-legged ticks have no eyes, and their relatives carry strings of light-sensitive cells along the body instead.'],
```
Log: L151, L152 (Phillis and Cromroy 1977), L158 (Perret and colleagues 2003).

```
['m', 'Eyes in use', 'American Dog Ticks released in a field moved toward the warm edge of a road. Ticks with painted eyes, and ticks without the sense organ on their front legs, did so less.'],
```
Log: L165 (Stewart and colleagues 2025).

```
['g', 'Where they look', 'In the tropical bont tick, a relative of the Lone Star Tick, each eye takes in a patch about 43 degrees wide and 49 high, aimed 39 degrees out from straight ahead and 33 degrees up.'],
```
Log: L154, L155, L156 (Kaltenrieder, Labhart and Hess 1989).

```
['g', 'Colour', 'The bont tick's eye has a single peak of sensitivity, in blue near 480 nanometres, so it sees no colours. This view is drawn in grey from the camera's blue and green.'],
```
Log: L153.

```
['g', 'Darkness', 'The sheep tick, a relative of the black-legged ticks, walks almost only in the dark, and the coming of darkness sets it moving.'],
```
Log: L159, L158 (Perret and colleagues 2003).

```
['m', 'Heat', 'A Lone Star Tick senses the warmth of a body through a covered pit on each front leg. At least seven in ten adult females found a warm square 10 centimetres across from a metre away, and the pit looks along a narrow line at most 5.7 degrees wide.'],
```
Log: L161, L162 (Carr and Salgado 2019).

```
['m', 'Breath and scent', 'Sensors in a pit on the front legs, called Haller's organ, respond to the carbon dioxide in breath and to the scents of animals. The black-legged tick responds most strongly to the cresols in a deer's scent glands.'],
```
Log: L163 (Carr and colleagues 2017), L164 (Holscher, Gearhart and Barker 1980), L166 (Josek and colleagues 2020).

```
['g', 'Damp', 'A sheep tick spends less time waiting on a grass tip as the air grows drier.'],
```
Log: L160 (Perret and colleagues 2003).

```
['x', 'Not in the picture', 'Heat, breath and scent are how a tick finds a host, and none of them reaches a camera.'],
```
Log: L161, L163, L164.

**The picture.** As `tick.md` describes it: a grey field of large soft patches from blue and green light, in which a passing shadow registers at once. Two changes follow from the evidence above: a coarser `cpd`, and, once zones exist, two windows aimed up and out.

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Tick', 'a tick' | as `tick.md` |
| `cpd` | .07 | **invented** by inference from the Lone Star Tick's own eye: 30 to 40 receptors (L151) spread over a field like the bont tick's, about 43 by 49 degrees (L154, L155). An ellipse that size covers about 1,655 square degrees; 35 receptors give about 47 square degrees each, a spacing of about 6.9 degrees, and 1 / (2 × 6.9) = 0.072. `tick.md` reached 0.1 from a camel tick's 4.8 degree target. Blur radius 0.36 of the long side at `VIEW_DEG` 24. |
| `M` | [.05, .45, .5] in every row | L153; weights **invented** (as `tick.md`) |
| zones | two soft windows centred up and out, 39 degrees to each side and 33 degrees up, each about 43 by 49 degrees; the rest dim | L154 to L156 in the bont tick; the dim surround is **invented** |
| `pupil`, `gate`, `persist`, `rate`, `fov` | unset | as `tick.md` |
| `cue` | 'Hold the phone at the height of the grass tips and tilt it up. Only large shadows remain.' | `tick.md`, **invented** wording |

**New effects.** `tick.md` section 4 covers heat, carbon dioxide, vibration and the two eye windows, and its judgements stand. One addition:

| Effect | What the person sees | Phone input | Difficulty | Beautiful and true |
|---|---|---|---|---|
| Waking at dusk | When the scene falls dark and stays dark, the field stirs: its patches drift as if the tick had begun to walk. In bright light it is still. | mean brightness | easy | L159 (activity almost only in darkness, triggered by its onset). The drift is **invented**. |

**[unfinished]**
