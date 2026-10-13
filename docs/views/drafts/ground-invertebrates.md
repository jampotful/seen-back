# Sensing sheet: ground invertebrates (snail, worm, scorpion, tick)

Research round 3, unit `ground-invertebrates`, written on 13 October 2026 from 01:47 to about 03:30 UTC. The evidence log is `docs/views/evidence/ground-invertebrates.jsonl` (lines are cited below as L1, L2 and so on, in file order) and the wanted list is `docs/views/wanted/ground-invertebrates.jsonl`. It builds on the checked sheets `docs/views/sheets/snail.md` and `docs/views/sheets/tick.md`, and every source behind a row was opened again in this session.

**What came through and what did not.** Of the two books in the owner's library, *Neurobiology of Arachnids* (Barth, ed., 1985) came through only as its front matter, chapters I to III and chapter IV to about page 73. The scorpion chapters (XVII, Root, on locomotion, and XVIII, Fleissner and Fleissner, on the clock in the visual system) and the chapters on sensilla, trichobothria and slit organs (VII to IX) were not in the copy. *Animal Eyes* (Land and Nilsson, 2nd edition, 2012) came through as chapters 1 and 2 and chapter 3 to about page 65, which holds its Table 3.1 of resolution. During the session these sites refused with HTTP 429 and I stopped fetching from them: Europe PMC (www.ebi.ac.uk), Zenodo's file store, doi.org for an Oxford title, and link.springer.com. The Biodiversity Heritage Library and J-STAGE refused automated reading under their robots rules, PubMed Central answered with a reCAPTCHA page, and the PDFs of two theses (Pulido Forero's at the Universidad Distrital and Kirwan's at Lund) failed to load, so only their abstracts and record pages were read. The shell could reach only GitHub, so every page was read through the web tool.

**What is unfinished.** No source I could open measures what a scorpion, harvestman, centipede or tick resolves, so those four pictures rest on inference; no flicker or time-constant measurement was found for any animal in the unit; and the family counts behind the shares were read once, with no second count.

## 1. Scope

### What the four groups hold

Records are iNaturalist research-grade observations in GBIF (dataset `50c9509d-22c7-4a22-a47d-8c48425ef4a7`). The class and order totals come from the saved facets of 11 October 2026 (run 10 of `fetch` on the `ci` branch, `runs/fetch/10/`). The family splits were read from the GBIF API through the web tool on 13 October 2026. Species counts come from the iNaturalist open-data snapshot of 27 September 2026 (`runs/coverage/2-lists/world.tsv.gz` on `ci`, research grade, all years), so they differ slightly from GBIF's.

| Group | GROUPS label | Records | What it holds |
|---|---|---:|---|
| snail | a snail or slug | 2,227,162 | Gastropoda 2,155,631; Polyplacophora 71,088; Scaphopoda 376; two small classes 66; Monoplacophora 1 |
| worm | a worm, millipede or centipede | 370,232 | Diplopoda 170,881; Chilopoda 82,474; Annelida 66,007; Platyhelminthes 37,559; Nematoda 8,445; Nemertea 3,896; Pauropoda 26; six small phyla 944. The 82 records of Symphyla, small myriapods that `tools/world/groups.py` also places here, are left out. |
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
- In Alachua County the group's 414 records are led by the Greenhouse Millipede (65), the Rusty Millipede (59), the Wandering Hammerhead Worm *Bipalium vagum* (42), the Smokey Oak Millipede (41), the Florida Ivory Millipede (35), the Eastern Red Centipede *Scolopocryptops sexspinosus* (32), the Big-leg Centipede *Theatops posticus* (27) and the Shovel-headed Garden Worm *Bipalium kewense* (21). The county's two most recorded centipedes are blind ones (L100, L197).

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
6. **The snail group keeps one view, as `snail.md` proposed.** The sea snails with large camera eyes are the exception: the strombid conchs resolve about 1 degree (L130, L131) and the periwinkle about 4.5 degrees between receptors (L1). Strombidae hold 12,703 records (0.57% of the group) and Littorinidae 45,606 (2.05%), together 2.6%. The land snails, slugs and sea slugs measured see at most coarse patches of light and dark (L125, L126, L133, L134, L181), the chitons with shell eyes resolve shapes about 9 to 12 degrees across (L146), and pond snails focus an image under water, though no source I opened measures how sharp it is (L136, L137). A `conch` view for Strombidae is the first split to make when the full database names species.
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
['m', 'Sharpness', 'In behaviour tests the red slug made out nothing finer than about 52 degrees, the width of a metre-wide shape seen from a metre away. This view is blurred until only the broad lie of light and dark remains.'],
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
['g', 'Shadows', 'A pond snail pulls back into its shell when a shadow passes over it. It feels the shadow through light-sensitive cells in the skin of its foot and mantle. This view flinches at a sudden shadow in the same way.'],
```
Log: L196 (Sunada, Lukowiak and Sakakibara 2012, sense_light_nonvisual).

```
['m', 'Sea slugs', 'A nudibranch's small eyes lie deep inside its body, on top of the brain. They tell light from dark, yet the nudibranch Berghia crawls toward a dark stripe set outside its dish. It smells the water with the pair of horns on its head, called rhinophores.'],
```
Log: L181, L182 (Rudman 1999, eye_type, sense_chemical), L195 (Quinlan, Cho and Katz 2021, behaviour_vision).

```
['g', 'Water snails', 'Some snails that live in water see more: a conch resolves detail down to about 1 degree, and a periwinkle's eye samples the world about every 4.5 degrees. Pond snails can focus an image under water in a deep pit of the retina. This view follows the land snails and sea slugs, which make up most of the records.'],
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
| Shadow flinch | A sudden darkening makes the soft field shrink toward a point and open again over a second or two, as a snail pulls in. | the camera's mean brightness | easy, shared with the worm view's shadow alarm | L196 (pond snail), L145 (chitons answer still dark targets). Timing **invented**. |
| Smell | none | none | impossible | It stays a row. |

### 2.2 `millipede`: millipedes (Diplopoda, with Pauropoda)

**Rows**

```
['m', 'Eyes', 'Most millipedes have a small cluster of large-faceted eyes on each side of the head. The flat-backed millipedes, among them the greenhouse millipede, which is photographed more than any other, have no eyes at all.'],
```
Log: L79 (Kirwan and Nilsson 2019, eye_type), L89 (Fox 2006, eyes_count), L92 (Marek and Bond 2009, eyes_count), L93 (Moritz and colleagues 2021, eyes_count).

```
['m', 'Sharpness', 'In behaviour tests the millipede Cylindroiulus punctatus made out a dark shape about 20 degrees wide, enough to find shelter and little more. A person sees detail about three thousand times finer. This view is blurred to match.'],
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
| `cpd` | .018 | L77: 1 / 56. Blur radius 1.39 of the long side at `VIEW_DEG` 24. Kirwan's thesis gives 63 degrees for the same species (L191), which would be 0.016; the published figure is used. |
| `sat` | 0 | No millipede spectral measurement was found; grey is **invented**. |
| `field` | unset; 1 for Polydesmida and Platydesmida when the full database names the species | L89, L92, L93 |
| `gate`, `persist`, `rate`, `gain` | unset | No measurement found. |
| `cue` | 'Point the phone at the ground under leaves and turn it slowly. Only the darker side of the scene remains.' | **invented** |

**New effects**

| Effect | What the person sees | Phone input | Difficulty | Beautiful and true |
|---|---|---|---|---|
| Curling | A sharp shake of the phone makes the picture wind into a dark spiral, which unwinds after a few seconds. | device motion | medium (a swirl warp and a timer) | L86. The spiral is the animal's own defence, and a slow unwinding makes a fine moment. The timing is **invented**. |
| Walking faster in light | In bright scenes the faint gradient drifts and searches across the frame; in the dark it settles. | mean brightness | easy | L84: light makes the animal walk more and sets no direction. |
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
['g', 'Flatworms', 'Each cup-shaped eye of a freshwater planarian samples the world about every 35 degrees, and behaviour tests on another planarian give the same coarse sharpness. Planarians flee ultraviolet light most strongly, and worms without eyes, or without heads, still flee near-ultraviolet light. Land planarians, such as the hammerhead worms, have many tiny eyes on the head.'],
```
Log: L2, L5 (Land and Nilsson 2012, interreceptor_deg, eye_type), L190 (Kirwan 2018, acuity_cpd in *Schmidtea lugubris*), L119 (Paskin and colleagues 2014, behaviour_vision), L120, L121 (Birkholz and Beane 2017), L169 (Bertone 2020, eyes_count).

```
['m', 'Fan worms', 'Fan worms and Christmas tree worms have eyes on their feathery tentacles. Their light-sensing pigment peaks at 464 nanometres, close to the blue light of a shallow reef, and a passing shadow makes them pull back into their tubes at once.'],
```
Log: L123, L124 (Bok and colleagues 2017, lambda_max_nm, eye_role), L188, L189 (Bok, Porter and Nilsson 2017, eye_role, motion).

```
['x', 'Touch, taste and damp', 'Worms meet most of the world through touch, taste and moisture. A leech's skin answers vibration up to about 50 times a second, and land planarians need damp ground to live. None of this reaches a camera.'],
```
Log: L118 (Laverack 1969, sense_touch), L170 (Bertone 2020, sense_chemical), L122 (Ascunce and colleagues 2026, sense_chemical).

```
['i', 'The picture', 'This view shows only how much light there is, where it comes from and how it changes. It weights blue light most, because planarians and the underside of a leech answer ultraviolet most strongly and blue is the nearest colour the camera records. The weighting is the app's own choice.'],
```
Log: L119 (planarian hierarchy), L115 (leech sensilla).

**The picture.** No image. The frame is a soft field whose brightness follows the scene, brighter on the side the light comes from, in grey drawn from the camera's blue more than its red. A sudden shadow makes it flinch shut.

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Worm', 'a worm or leech' | **invented**; the GROUPS label would change once millipedes and centipedes have views of their own |
| `cpd` | .014 | L2: the planarian's 35 degrees, 1 / (2 × 35) = 0.014. The behavioural 73 degrees in *Schmidtea lugubris* (L190), read as a full cycle, gives 1 / 73 = 0.014 as well. Blur radius 1.79 of the long side at `VIEW_DEG` 24, so only a gradient remains. Earthworms have no eyes at all (L107); for them the gradient stands for the directional windows in the skin, and that reading is mine. |
| `M` | [0, .3, .7] in every row | L119, L115; weights **invented** |
| `field`, `gate`, `rate` | unset | A shadow must register at once (L124), so no averaging. |
| `cue` | 'Hold still and let a hand pass over the phone. There is no picture, only light, its direction and the shock of a shadow.' | **invented** |

**New effects**

| Effect | What the person sees | Phone input | Difficulty | Beautiful and true |
|---|---|---|---|---|
| Shadow alarm | When the frame darkens sharply (for example by a third within a third of a second), the field contracts to a dark point, as a fan worm pulls in, and opens again over two or three seconds. | the camera's mean brightness | easy | L124, L188 (fan worms withdraw from encroaching objects), L189 (their receptors answer a fall in light), L113 (the leech's whole-body S cell). The fan opening again is the beautiful part. Thresholds and timing are **invented**. |
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
['m', 'A glowing body', 'Under ultraviolet light a scorpion's outer skeleton glows blue-green, though the lenses of its eyes do not. Scorpions with their eyes covered still reacted to ultraviolet light, which suggests the whole body helps to catch it. They react most strongly to ultraviolet at the light level of sunset.'],
```
Log: L35, L36 (Yong 2011, reporting Gaffin and colleagues 2012), L33 (Kloock, Kubli and Reynolds 2010), L17 (Prévost and Stemme 2020), L48 (Yang and colleagues 2013, filter_pigments), L193, L194 (Gaffin and Barker 2014).

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
| Glowing rim | At dusk by the phone's clock, and more where the scene holds strong blue and violet, a cyan-green glow rises around the edge of the frame, with small dark spots where the eyes would be, because the lenses do not glow. | the phone's clock and the camera's blue level, standing in for ultraviolet | medium (an overlay pass) | L35, L36, L48; the dusk peak follows L193, and the collector idea is a hypothesis (L194). The trigger is **invented** and must carry an `i` row if added. The glow with dark eye-spots is a striking and true image. |
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

## 3. The earlier proposals, re-checked

None of the four groups has an entry in `EYES` yet (build 22 lists them only in `GROUPS`). Two earlier sheets proposed entries, and I re-checked each row and number against sources opened in this session. "Unchecked" means I did not reopen that source today; it does not mean the row is wrong.

**`snail.md`**

| Row or field | Verdict | Reason |
|---|---|---|
| Eyes (m) | confirmed in its first sentence; the eye size unchecked | L183, L133. The 233 µm eye of *Cepaea hortensis* comes from Shepeleva (2023), whose abstract I opened; it gives no size. |
| Sharpness (m) | **corrected** | The garden snail's 14.5 degrees is withdrawn: Serb and Eernisse cite it to Hamilton and Winter (1982), and the collection index gives that paper's title as a study of *Littorina irrorata*. The red slug's 52 degrees is confirmed in Irwin and colleagues (L128), and the abstract of its primary paper, now opened, says the slugs' eyes form no sharp image (L125, L126). |
| Colour (m) | confirmed, and extended | L141, L142, L143. Added: one pigment near 496 nm in *Helix lucorum* (L138), shared by both cell types (L139). |
| Light without eyes (m) | confirmed through a summary | L144 (Knight 2019, on Nishiyama and colleagues 2019); L184 adds the wiring between eye and brain cells. The primary paper was not reopened. |
| Shadows (g, pond snail skin) | confirmed in its first half | Sunada, Lukowiak and Sakakibara (2012) reopened (L196). The 490 nm peak (IKBFU 2018) was not reopened and is left out. |
| Sea slugs (g) | confirmed, with one change | Rudman's page as I read it today places the eyes "deep inside the body on top of the brain" and says they "cannot see images but are able to distinguish light and dark" (L181). `snail.md` quoted "deep beneath the skin, behind the rhinophores"; both phrasings may be on the page. The *Berghia* stripe result is confirmed (Quinlan, Cho and Katz 2021, L195). |
| Chitons (m) | confirmed | L146, L147, L145 |
| Sea snails (g) | confirmed | L130, L131, L129; Land and Nilsson's Table 3.1 gives the periwinkle 4.5 degrees, citing Land (1981a), which matches the figure `snail.md` took from Serb and Eernisse (L1). |
| Smell (m, *Achatina*) | unchecked; replaced | Chase and Croll (1981) was not reopened. My smell row uses Gelperin (1974) on the leopard slug (L148). |
| Smell and damp (x) | half confirmed | The rhinophore half is confirmed (L182); the garden snail after rain (Kwiecien and colleagues 2022) was not reopened. |
| `cpd` .035 | **corrected to .02** | See the Sharpness row and section 2.1. |
| `M` [.05, .3, .65] | **corrected to [.05, .45, .5]**, shifting to [.05, .25, .7] in bright scenes | The 496 nm and 480 nm peaks (L138, L141) sit between the camera's blue and green; the 420 nm light-adapted peak (L142) moves the weight to blue. |
| `pupil` 'o' | unchecked | Same picture with `dof` unset. |
| `field`, `gate` unset | confirmed | L145, L126 |

**`tick.md`**

| Row or field | Verdict | Reason |
|---|---|---|
| Eyes (m) | confirmed by other sources | The NC State guide (Bertone and colleagues 2023) was not reopened. The Lone Star Tick's eye is confirmed in Phillis and Cromroy (L151), the American Dog Tick's eyes in use in Stewart and colleagues (L165), and the eyeless sheep tick in Perret and colleagues (L158). |
| Where they look (g) | confirmed | L154, L155, L156, read today on the Springer page. |
| Shapes (g) | unchecked | Kaltenrieder (1990) was not reopened. |
| Colour (g) | confirmed | L153 |
| Without eyes (g) | confirmed | L158, L159 |
| Questing (m) | half confirmed | The organ's place on the first legs is confirmed (L163); the posture (the archived CDC page) was not reopened. |
| Heat (m) | confirmed | L161, L162 |
| Breath (g) | unchecked; replaced | Steullet and Guerin (1992) was not reopened. Holscher and colleagues (1980) record carbon dioxide responses in the Lone Star, Gulf Coast and American Dog Ticks themselves (L164), so my row is graded m. |
| Smell, damp and footsteps (x) | two of three confirmed | Damp (L160) and scent (L166) are confirmed; vibration was not reopened. |
| `cpd` .1 | **corrected to .07**, both invented | The Lone Star Tick's 30 to 40 receptors (L151) over a bont-tick-sized field (L154, L155) give about 0.07; see section 2.7. |
| `M`, `pupil`, `fov`, `field`, `gate` | confirmed as `tick.md` set them | L153 for `M`; the rest are unset or equivalent. |

## 4. Species with their own measurements

These are measured well enough for a profile of their own when the full database names them.

| Species | Group | Records | Log lines | What a profile would add |
|---|---|---:|---|---|
| Strombid conchs, *Conomurex luhuanus* | snail | Strombidae 12,703; *C. luhuanus* 659 | L130, L131, L132 | A `conch` view at about 0.95 cycles per degree that answers looming shapes |
| Red slug, *Arion rufus* | snail | not listed under this name in the snapshot | L125 to L128 | The coarsest land-slug picture, with no polarization |
| *Helix lucorum* and the Roman snail | snail | *H. lucorum* 6,984; *H. pomatia* 52,599 | L138, L139, L140 | Grey from a single 496 nm pigment, log brightness |
| *Limax valentianus* and the leopard slug | snail | listed as *Ambigolimax valentianus* 1,053; *Limax maximus* 47,167 | L141 to L144, L148, L184 | Day and night colour shift, the brain's light sense, homing by smell |
| *Acanthopleura granulata* | snail | 2,740 | L146 | A dome of shell eyes at 9 to 12 degrees |
| Greenhouse Millipede, *Oxidus gracilis* | worm (millipede) | 28,389 | L84 to L88 | No eyes: skin light sense, touch, taste, temperature |
| *Cylindroiulus punctatus* | worm (millipede) | 1,825 | L77 to L80 | The measured millipede picture, 56 degrees |
| House centipede, *Scutigera coleoptrata* | worm (centipede) | 26,123 | L94 to L97, L186 | Two colour classes (448 and 350 nm), about 150 facets |
| *Scolopendra mutilans* | worm (centipede) | 1,648 | L104, L105 | Sunlight felt as heat in the antennae |
| *Lumbricus terrestris* | worm | 3,785 | L106, L107, L167, L168 | Skin light sense, dim-light approach |
| *Diplocardia mississippiensis* | worm | not in the snapshot's species list; a Florida species | L176 to L179 | The mole's vibration, 80 to 200 Hz |
| Medicinal leech, *Hirudo verbana* | worm | 119 | L111 to L117 | A body of eyes, green above and ultraviolet below |
| Christmas tree worms, *Spirobranchus* | worm | *S. giganteus* 1,993 | L123, L124 | Shadow alarm with a 464 nm pigment |
| *Androctonus australis* | scorpion | 58 | L26, L27, L28 | The night clock of the eyes |
| Sand scorpions, *Paruroctonus* and *Smeringurus* | scorpion | *P. utahensis* 144; *Smeringurus mesaensis* 924. Brownell's papers name their sand scorpion *Paruroctonus mesaensis*, and Kundu and colleagues (2025) give the sand scorpion of Gaffin and colleagues (1992) as *Smeringurus mesaensis*; reading the two names as one species is mine. | L29 to L31, L35, L36, L172, L174 | Ripples in sand, fluorescence, pectine walks |
| Striped bark scorpion, *Centruroides vittatus* | scorpion | 11,594 | L171 | Following traces by contact |
| *Phalangium opilio* | harvestman | 28,313 | L65 | Hidden eyes for the clock |
| Lone Star Tick, *Amblyomma americanum* | tick | 8,996 | L151, L152, L161, L162, L164 | Its own eye, its heat pit and its breath sense |
| American Dog Tick, *Dermacentor variabilis* | tick | 20,209 | L165 | Eyes and heat used together in the field |
| Eastern Black-legged Tick, *Ixodes scapularis* | tick | 11,235 | L166 | Deer-scent phenols |

## 5. Gaps and how to fill them

| Trait the views need | Status | Nearest measured relative and the inference (the evidence-based invention) |
|---|---|---|
| Scorpion sharpness and field per eye | not found in any source opened | Whip scorpion median-eye optics (L38): a 200 µm image distance and rhabdoms up to 20 µm give 2.9 to 5.7 degrees per receptor, 0.09 to 0.17 cycles per degree, used for the middle zone at .1. Locket (2001) and Schliwa and Fleissner (1980) would settle it (wanted). |
| Scorpion lateral-eye sensitivity margin | two sources disagree (1 against 10 log units) | Fleissner's own abstract (L27) is preferred over Loria and Prendini's citation of it (L50). Fleissner (1977b) is wanted. |
| Flicker or time constants for any animal in the unit | nothing found | Nothing is known from the sources opened; `rate` and `persist` stay unset everywhere. |
| Harvestman sharpness and colour in the common families | nothing found | The cave species (L59 to L63) give fast lenses and ultraviolet-plus-green sensitivity; too far from *Phalangium* and *Leiobunum* to set a colour matrix, so grey is used. |
| Centipede sharpness | nothing found | Inferred from facet counts against the millipede (L77, L81, L97, L98): about 0.05 cycles per degree in the house centipede. Müller and colleagues (2003) and Sombke and Müller (2023) would test it. |
| Millipede colour | nothing found | The view uses grey, since the sources opened allow no inference. |
| Earthworm colour | nothing found | Planarians and the leech's skin sensilla respond most to ultraviolet and blue (L119, L115); the worm view's blue weighting is that inference, graded i in its row. |
| Land planarian eyes | "numerous tiny eyes" only (L169) | The freshwater planarians' 35 degrees by anatomy (L2) and 73 degrees by behaviour (L190) agree at about 0.014 cycles per degree, which is used for the whole worm view. |
| Leech and fan worm resolution | not found | Five eyecups of about 50 receptors each (L114) and compound radiolar eyes (L188) suggest directional sight; no number. Bok and Nilsson (2016) is wanted. |
| Land snail sharpness beyond the red slug | partly found | 52 degrees in *Arion rufus* (L128) and the review's statement (L134). The review's tables (Zieger and Meyer-Rochow 2008) would give optics for several species (wanted). |
| Snail and tick responses to motion | not found | Nothing measured; `gate` stays unset. |
| Tick sharpness | inferred | 30 to 40 receptors (L151) over the bont tick's field (L154, L155): about 0.07 cycles per degree. |
| Pseudoscorpions and camel spiders | eye counts and one sensillum study only (L75, L76) | They join the scorpion view; nothing more is known from the sources opened. |
| Gall nematodes | none needed | They are photographed as galls and belong in `other`. |

## 6. Closed sources wanted

The same list as `docs/views/wanted/ground-invertebrates.jsonl`, most useful first. Every DOI comes from the collection's index or from a page opened in this session. Priority 1 would change a view's picture, 2 would confirm or correct a row, 3 is background.

1. **Priority 1.** Locket A, 2001. Eyes and vision (chapter in Scorpion Biology and Research). *Oxford University Press (book DOI 10.1093/oso/9780195084344.001.0001)*. doi:10.1093/oso/9780195084344.003.0003. Gives the optics of scorpion median and lateral eyes, which would replace the invented sharpness and zones of the scorpion view. Views: `scorpion`.
2. **Priority 1.** Zieger MV, Meyer-Rochow VB, 2008. Understanding the cephalic eyes of pulmonate gastropods: a review. *American Malacological Bulletin*. doi:10.4003/006.026.0206. Its tables of eye size, optics and sampling for many land and freshwater snails would set the snail view's sharpness beyond the single red slug figure; it is openly licensed on the Biodiversity Heritage Library, which refused automated reading. Views: `snail`.
3. **Priority 1.** Sombke A, Müller CHG, 2023. The visual system of Myriapoda. *Springer Series in Vision Research (book chapter)*. doi:10.1007/978-3-031-23216-9_7. A survey of millipede and centipede eyes that may give fields and facet angles, replacing the inferred centipede sharpness and testing the millipede value. Views: `millipede`, `centipede`.
4. **Priority 1.** Müller CHG, Rosenberg J, Richter S, Meyer-Rochow VB, 2003. The compound eye of Scutigera coleoptrata (Linnaeus, 1758) (Chilopoda: Notostigmophora): an ultrastructural reinvestigation that adds support to the Mandibulata concept. *Zoomorphology*. doi:10.1007/s00435-003-0085-0. Ommatidial geometry of the house centipede, the most recorded centipede, would replace the invented 0.05 cycles per degree. Views: `centipede`.
5. **Priority 1.** Schliwa M, Fleissner G, 1980. The lateral eyes of the scorpion, Androctonus australis. *Cell and Tissue Research*. doi:10.1007/bf00233611. Lateral eye structure would settle whether the side zones of the scorpion view should carry any image at all. Views: `scorpion`.
6. **Priority 1.** Fleissner G, 1977. The absolute sensitivity of the median and lateral eyes of the scorpion, Androctonus australis L. (Buthidae, Scorpiones). *Journal of Comparative Physiology A*. doi:10.1007/bf00612341. Settles whether the lateral eyes exceed the median eyes by 1 log unit or by 10, which sets the night gain of the side zones. Views: `scorpion`.
7. **Priority 1.** Fleissner G, Fleissner G, 1985. Neurobiology of a circadian clock in the visual system of scorpions. In: Barth FG (ed.) Neurobiology of Arachnids, pp. 351-376. *Springer-Verlag, Berlin*. doi:10.1007/978-3-642-70348-5_18. The scorpion chapter missing from the owner's partial copy of Barth (1985); it would give the night-state sensitivity and the eye physiology behind the scorpion view. Views: `scorpion`.
8. **Priority 2.** Bok MJ, Nilsson D-E, 2016. Fan worm eyes. *Current Biology*. doi:10.1016/j.cub.2016.06.032. Radiolar eye arrangements and their resolution would set the shadow-alarm threshold for fan worms in the worm view. Views: `worm`.
9. **Priority 2.** Gaffin DD, Bumm LA, Taylor MS, Popokina NV, Mann SN, 2012. Scorpion fluorescence and reaction to light. *Animal Behaviour (OpenAlex dates it 2011; the Zenodo record gives 1 February 2012)*. doi:10.1016/j.anbehav.2011.11.014. Gives the wavelengths and intensities behind the cuticle-as-light-collector result, which the glowing-rim effect would follow; Zenodo record 895450 holds a copy whose file was refused here. Views: `scorpion`.
10. **Priority 2.** Blass G, Gaffin DD, 2008. Light wavelength biases of scorpions. *Animal Behaviour*. doi:10.1016/j.anbehav.2007.12.022. Behavioural weighting of wavelengths would correct the scorpion colour matrix. Views: `scorpion`.
11. **Priority 2.** Fleissner G, 1977. Scorpion lateral eyes: extremely sensitive receptors of Zeitgeber stimuli. *Journal of Comparative Physiology A*. doi:10.1007/bf00612340. Confirms the lateral eyes' role and sensitivity behind the side zones. Views: `scorpion`.
12. **Priority 2.** Hamilton PV, Winter MA, 1982. Behavioural responses to visual stimuli by the snail Littorina irrorata. *Animal Behaviour*. doi:10.1016/s0003-3472(82)80147-4. Settles whether the 14.5 degrees attributed to the garden snail belongs to this periwinkle. Views: `snail`.
13. **Priority 2.** Hamilton PV, Ardizzoni SC, Penn JS, 1983. Eye structure and optics in the intertidal snail, Littorina irrorata. *Journal of Comparative Physiology A*. doi:10.1007/bf00606433. Periwinkle optics for a later conch and periwinkle split of the snail view. Views: `snail`.
14. **Priority 2.** Von Berg E, Schneider G, 1972. The spectral sensitivity of the dark-adapted eye of Helix pomatia L. *Vision Research*. doi:10.1016/0042-6989(72)90065-x. Confirms the single blue-green pigment in the Roman snail itself, behind the snail colour row. Views: `snail`.
15. **Priority 2.** Kirwan JD, Nilsson D-E, 2019. A millipede compound eye mediating low-resolution vision. *Vision Research*. doi:10.1016/j.visres.2019.09.003. The full text (openly licensed, unreachable here) gives the facet count and field of the julid eye behind the millipede view. Views: `millipede`, `centipede`.
16. **Priority 2.** Willemart RH, Farine J-P, Gnaspini P, 2008. Sensory biology of Phalangida harvestmen (Arachnida, Opiliones): a review, with new morphological data on 18 species. *Acta Zoologica*. doi:10.1111/j.1463-6395.2008.00341.x. The review's evidence on harvestman eyes and phototaxis would test the harvestman picture's two side windows and coarse sight. Views: `harvestman`.
17. **Priority 2.** Meyer-Rochow VB, Liddle AR, 1988. Structure and function of the eyes of two species of opilionid from New Zealand glow-worm caves (Megalopsalis tumida: Palpatores, and Hendea myersi cavernicola: Laniatores). *Proceedings of the Royal Society B*. doi:10.1098/rspb.1988.0023. Spectral peaks in nanometres and visual fields for harvestman eyes. Views: `harvestman`.
18. **Priority 2.** Binnington KC, 1972. The distribution and morphology of probable photoreceptors in eight species of ticks (Ixodoidea). *Parasitology Research*. doi:10.1007/bf00328750. Eyes and light-sensitive cells across tick genera, testing the eyed and eyeless rows. Views: `tick`.
19. **Priority 2.** Mitchell RD, Zhu J, Carr AL, Dhammi A, Cave GL, Sonenshine DE, Roe RM, 2017. Infrared light detection by the Haller's organ of adult American dog ticks, Dermacentor variabilis (Ixodida: Ixodidae). *Ticks and Tick-borne Diseases*. doi:10.1016/j.ttbdis.2017.06.001. Wavelengths of the heat sense in the most recorded tick, behind the Heat row. Views: `tick`.
20. **Priority 3.** Lewis JGE, 1981. Sensory responses and related behaviour (chapter). *Cambridge University Press*. doi:10.1017/cbo9780511565649.007. The full chapter on centipede light, touch and smell responses behind several centipede rows. Views: `centipede`.
21. **Priority 3.** Cloudsley-Thompson JL, 1951. On the responses to environmental stimuli, and the sensory physiology of millipedes (Diplopoda). *Proceedings of the Zoological Society of London*. doi:10.1111/j.1096-3642.1951.tb00795.x. The full paper on the greenhouse millipede's senses behind most millipede rows. Views: `millipede`.
22. **Priority 3.** Brownell P, Farley RD, 1979. Orientation to vibrations in sand by the nocturnal scorpion Paruroctonus mesaensis: mechanism of target localization. *Journal of Comparative Physiology A*. doi:10.1007/bf00613081. Timing cues behind the ripples-in-sand effect. Views: `scorpion`.

## 7. Sources

**Works behind the log.** One line each, alphabetical; all were opened in this session. L-numbers are the log lines that rest on each.

- Ascunce K, Lopez SN, Carlson JR, van Wolfswinkel JC, 2026. The sensory basis of planarian behavior. *Journal of Neuroscience*. doi:10.1523/jneurosci.1158-25.2025. **opened**: read as the abstract in the collection (`worms-myriapods`). L122.
- Ashford K, Blankenship R, Carpenter W, Wheeler I, Gaffin DD, 2018. Response of the eastern sand scorpion, Paruroctonus utahensis, to air movement from a moth analog. *Journal of Arachnology*. doi:10.1636/joa-s-17-097.1. **opened**: read as the abstract in the collection (`arachnids-other`). L174.
- Babu KS, 1985. Patterns of arrangement and connectivity in the central nervous system of arachnids. In: Barth FG (ed.) Neurobiology of Arachnids, pp. 3-19. *Springer-Verlag, Berlin*. doi:10.1007/978-3-642-70348-5. **opened**: read in the owner's library copy, which came through only in part. L6 to L8.
- Baylor ER, 1959. The responses of snails to polarized light. *Journal of Experimental Biology*. doi:10.1242/jeb.36.2.369. **opened**: read as the abstract in the collection (`snails-molluscs`). L149.
- Bertone M, 2020. Information on terrestrial flatworms and hammerhead worms (NC State Extension, 11 December 2020, updated 26 September 2024). *NC State University Entomology Extension*. https://entomology.ces.ncsu.edu/news/information-on-terrestrial-flatworms-and-hammerhead-worms/. **opened**: read at https://entomology.ces.ncsu.edu/news/information-on-terrestrial-flatworms-and-hammerhead-worms/. L169 to L170.
- Bingman VP, Graving JM, Hebets EA, Wiegmann DD, 2016. Importance of the antenniform legs, but not vision, for homing by the neotropical whip spider, Paraphrynus laevifrons. *Journal of Experimental Biology*. doi:10.1242/jeb.149823. **opened**: read as the abstract in the collection (`arachnids-other`). L72.
- Birkholz TR, Beane WS, 2017. The planarian TRPA1 homolog mediates extraocular behavioral responses to near ultraviolet light. *Journal of Experimental Biology*. doi:10.1242/jeb.152298. **opened**: read as the full text in the collection (`worms-myriapods`). L120 to L121.
- Bok MJ, Porter ML, Nilsson D-E, 2017. Phototransduction in fan worm radiolar eyes. *Current Biology*. doi:10.1016/j.cub.2017.05.093. **opened**: read at https://research-information.bris.ac.uk/files/159040708/Full_text_PDF_accepted_author_manuscript_.pdf. L188 to L189.
- Bok MJ, Porter ML, ten Hove HA, Smith RS, Nilsson D-E, 2017. Radiolar eyes of serpulid worms (Annelida, Serpulidae): structures, function, and phototransduction. *Biological Bulletin*. doi:10.1086/694735. **opened**: read as the abstract in the collection (`worms-myriapods`). L123 to L124.
- Bonato L, Orlando M, Zapparoli M, Fusco G, Bortolin F, 2017. New insights into Plutonium, one of the largest and least known European centipedes (Chilopoda): distribution, evolution and morphology. *Zoological Journal of the Linnean Society*. doi:10.1093/zoolinnean/zlw026. **opened**: read as the abstract in the collection (`worms-myriapods`). L197.
- Brownell PH, 1977. Compressional and surface waves in sand: used by desert scorpions to locate prey. *Science*. doi:10.1126/science.197.4302.479. **opened**: read as the abstract in the collection (`arachnids-other`). L29 to L30.
- Brownell PH, van Hemmen JL, 2001. Vibration sensitivity and a computational theory for prey-localizing behavior in sand scorpions. *American Zoologist*. doi:10.1093/icb/41.5.1229. **opened**: read as the abstract in the collection (`arachnids-other`). L31.
- Carr AL, Mitchell RD III, Dhammi A, Bissinger BW, Sonenshine DE, Roe RM, 2017. Tick Haller's organ, a new paradigm for arthropod olfaction: how ticks differ from insects. *International Journal of Molecular Sciences*. doi:10.3390/ijms18071563. **opened**: read as the full text in the collection (`arachnids-other`). L163.
- Carr AL, Salgado VL, 2019. Ticks home in on body heat: a new understanding of Haller's organ and repellent action. *PLoS ONE*. doi:10.1371/journal.pone.0221659. **opened**: read as the full text in the collection (`arachnids-other`). L161 to L162.
- Catania KC, 2008. Worm grunting, fiddling, and charming: humans unknowingly mimic a predator to harvest bait. *PLoS ONE*. doi:10.1371/journal.pone.0003472. **opened**: read at https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0003472. L176 to L179.
- Chernorizov AM, Shekhter ED, Arakelov GG, Zimachev MM, 1993. Vision in the edible snail: the spectral sensitivity of the dark-adapted eye (in Russian; English abstract on PubMed). *PubMed record 1338247*. https://pubmed.ncbi.nlm.nih.gov/1338247/. **opened**: read as the abstract in the collection (`snails-molluscs`), matched by title. L138.
- Chernorizov AM, Zimachev MM, Shekhter ED, Garusev A, 2007. Mechanisms of achromatic vision in snail Helix lucorum L.: intracellular study of light-sensitive cells in retina (in Russian; English abstract on PubMed). *PubMed record 17432320*. https://pubmed.ncbi.nlm.nih.gov/17432320/. **opened**: read as the abstract in the collection (`snails-molluscs`), matched by title. L139.
- Cloudsley-Thompson JL, 1951. On the responses to environmental stimuli, and the sensory physiology of millipedes (Diplopoda). *Proceedings of the Zoological Society of London*. doi:10.1111/j.1096-3642.1951.tb00795.x. **opened**: read as the abstract in the collection (`worms-myriapods`). L84 to L88.
- Costa TM, Willemart RH, 2013. First experimental evidence that a harvestman (Arachnida: Opiliones) detects odors of non-rotten dead prey by olfaction. *Zoologia (Curitiba)*. doi:10.1590/s1984-46702013000300018. **opened**: read as the abstract in the collection (`arachnids-other`). L67.
- Edgecombe GD, Huey JA, Humphreys WF, Hillyer MJ, Burger MAA, Volschenk ES, Waldock JM, 2019. Blind scolopendrid centipedes of the genus Cormocephalus from subterranean habitats in Western Australia (Myriapoda: Scolopendromorpha: Scolopendridae). *Invertebrate Systematics*. doi:10.1071/is19015. **opened**: read as the abstract in the collection (`worms-myriapods`). L99.
- Edgecombe GD, Koch M, 2008. Phylogeny of scolopendromorph centipedes (Chilopoda): morphological analysis featuring characters from the peristomatic area. *Cladistics*. doi:10.1111/j.1096-0031.2008.00220.x. **opened**: read as the abstract in the collection (`worms-myriapods`). L100.
- Flanigan KAS, Wiegmann DD, Hebets EA, Bingman VP, 2021. Multisensory integration supports configural learning of a home refuge in the whip spider Phrynus marginemaculatus. *Journal of Experimental Biology*. doi:10.1242/jeb.238444. **opened**: read as the abstract in the collection (`arachnids-other`). L73.
- Fleissner G, 1977. Differences in the physiological properties of the median and the lateral eyes and their possible meaning for the entrainment of the scorpion's circadian rhythm. *Journal of Interdisciplinary Cycle Research*. doi:10.1080/09291017709359541. **opened**: read as the abstract in the collection (`arachnids-other`). L26 to L28.
- Fox R, 2006. Pachydesmus, flat-backed millipede (Invertebrate Anatomy OnLine, Lander University, 29 June 2006). *Invertebrate Anatomy OnLine*. https://lanwebs.lander.edu/faculty/rsfox/invertebrates/pachydesmus.html. **opened**: read at https://lanwebs.lander.edu/faculty/rsfox/invertebrates/pachydesmus.html. L89 to L91.
- Friedrich M, 2024. Newly discovered harvestmen relict eyes eyeing for their functions. *BioEssays*. doi:10.1002/bies.202400194. **opened**: read as the abstract in the collection (`arachnids-other`). L65 to L66.
- Gaffin DD, Barker TN, 2014. Comparison of scorpion behavioral responses to UV under sunset and nighttime irradiances. *Journal of Arachnology 42: 111-118*. https://www.americanarachnology.org/journal-joa/joa-all-articles/article/download/arac-42-1-111.pdf/?no_cache=1. **opened**: read at https://www.americanarachnology.org/journal-joa/joa-all-articles/article/download/arac-42-1-111.pdf/?no_cache=1. L193 to L194.
- Gaffin DD, Muñoz MG, Hoefnagels MH, 2022. Evidence of learning walks related to scorpion home burrow navigation. *Journal of Experimental Biology*. doi:10.1242/jeb.243947. **opened**: read as the full text in the collection (`arachnids-other`). L172.
- Geethabali, Rao KP, 1973. A metasomatic neural photoreceptor in the scorpion. *Journal of Experimental Biology*. doi:10.1242/jeb.58.1.189. **opened**: read as the abstract in the collection (`arachnids-other`). L32.
- Gelperin A, 1974. Olfactory basis of homing behavior in the giant garden slug, Limax maximus. *Proceedings of the National Academy of Sciences*. doi:10.1073/pnas.71.3.966. **opened**: read as the abstract in the collection (`snails-molluscs`). L148.
- Groves TKH, Jellies J, 2021. Spectral responses across a dorsal-ventral array of dermal sensilla in the medicinal leech. *Journal of Comparative Physiology A*. doi:10.1007/s00359-021-01508-z. **opened**: read as the full text in the collection (`worms-myriapods`). L114 to L116.
- Gál J, Bobkova MV, Zhukov VV, Shepeleva IP, Meyer-Rochow VB, 2004. Fixed focal-length optics in pulmonate snails (Mollusca, Gastropoda): squaring phylogenetic background and ecophysiological needs (II). *Invertebrate Biology*. doi:10.1111/j.1744-7410.2004.tb00147.x. **opened**: read as the abstract in the collection (`snails-molluscs`). L137.
- Hemenway J, 1900. The structure of the eye of Scutigera (Cermatia) forceps. *Biological Bulletin*. doi:10.2307/1535588. **opened**: read as the abstract in the collection (`worms-myriapods`). L98.
- Hess WN, 1923. Reactions to light and photoreceptors of Lumbricus terrestris. *Proceedings of the Indiana Academy of Science (38th meeting, 1922), pp. 223-224*. https://journals.indianapolis.iu.edu/index.php/ias/article/download/13948/14033/20413. **opened**: read at https://journals.indianapolis.iu.edu/index.php/ias/article/download/13948/14033/20413. L167 to L168.
- Hess WN, 1925. Photoreceptors of Lumbricus terrestris, with special reference to their distribution, structure, and function. *Journal of Morphology*. doi:10.1002/jmor.1050410105. **opened**: read as the abstract in the collection (`worms-myriapods`). L106 to L107.
- Holscher KH, Gearhart HL, Barker RW, 1980. Electrophysiological responses of three tick species to carbon dioxide in the laboratory and field. *Annals of the Entomological Society of America*. doi:10.1093/aesa/73.3.288. **opened**: read as the abstract in the collection (`arachnids-other`). L164.
- Irwin AR, Williams ST, Speiser DI, Roberts NW, 2022. The marine gastropod Conomurex luhuanus (Strombidae) has high-resolution spatial vision and eyes with complex retinas. *Journal of Experimental Biology*. doi:10.1242/jeb.243927. **opened**: read as the full text in the collection (`snails-molluscs`). L128 to L132.
- Josek T, Sperrazza J, Alleyne M, Syed Z, 2020. Neurophysiological and behavioral responses of blacklegged ticks to host odors. *Journal of Insect Physiology*. doi:10.1016/j.jinsphys.2020.104175. **opened**: read as the abstract in the collection (`arachnids-other`). L166.
- Kaltenrieder M, Labhart T, Hess E, 1989. Spectral sensitivity, absolute threshold, and visual field of two tick species, Hyalomma dromedarii and Amblyomma variegatum. *Journal of Comparative Physiology A*. doi:10.1007/bf00619190. **opened**: read at https://link.springer.com/article/10.1007/BF00619190. L153 to L157.
- Kingston ACN, Chappell DR, Speiser DI, 2018. Evidence for spatial vision in Chiton tuberculatus, a chiton with eyespots. *Journal of Experimental Biology*. doi:10.1242/jeb.183632. **opened**: read as the abstract in the collection (`snails-molluscs`). L145.
- Kirwan J, 2018. Spatial vision in diverse invertebrates (doctoral thesis, Lund University; ISBN 978-91-7753-714-4). *Lund University, Faculty of Science, Department of Biology*. https://portal.research.lu.se/en/publications/dc76fe19-18de-49e6-955a-47d1a084760c. **opened**: read at https://portal.research.lu.se/en/publications/dc76fe19-18de-49e6-955a-47d1a084760c. L190 to L192.
- Kirwan JD, Nilsson D-E, 2019. A millipede compound eye mediating low-resolution vision. *Vision Research 165: 36-44*. doi:10.1016/j.visres.2019.09.003. **opened**: read as the abstract in the collection (`worms-myriapods`). L77 to L80.
- Kloock CT, Kubli A, Reynolds R, 2010. Ultraviolet light detection: a function of scorpion fluorescence. *Journal of Arachnology*. doi:10.1636/b09-111.1. **opened**: read as the abstract in the collection (`arachnids-other`). L33.
- Knight K, 2019. Slugs 'see' with light-sensitive brain (Inside JEB summary of Nishiyama et al. 2019). *Journal of Experimental Biology*. doi:10.1242/jeb.209908. **opened**: read as the abstract in the collection (`snails-molluscs`). L144.
- Kosciolek C, Desurmont GA, Thomann T, Zamprogna A, Caron V, 2024. Toward a push-pull strategy against invasive snails using chemical and visual stimuli. *Scientific Reports*. doi:10.1038/s41598-024-62225-6. **opened**: read as the abstract in the collection (`snails-molluscs`). L150.
- Kundu P, et al., 2025. Electrophysiological and behavioral responses of elongated solifuge sensilla to mechanical stimuli. *Journal of Comparative Physiology A*. doi:10.1007/s00359-025-01731-y. **opened**: read as the full text in the collection (`arachnids-other`). L76.
- Land MF, 1985. The morphology and optics of spider eyes. In: Barth FG (ed.) Neurobiology of Arachnids, pp. 53-78. *Springer-Verlag, Berlin*. doi:10.1007/978-3-642-70348-5. **opened**: read in the owner's library copy, which came through only in part. L9.
- Land MF, Nilsson D-E, 2012. Animal Eyes, 2nd edition. *Oxford University Press, Oxford (ISBN 978-0-19-958113-9)*. https://openlibrary.org/isbn/9780199581139. **opened**: read in the owner's library copy, which came through only in part. L1 to L5.
- Laverack MS, 1969. Mechanoreceptors, photoreceptors and rapid conduction pathways in the leech, Hirudo medicinalis. *Journal of Experimental Biology*. doi:10.1242/jeb.50.1.129. **opened**: read as the abstract in the collection (`worms-myriapods`). L118.
- Lehmann T, Lodde-Bensch E, Melzer RR, Metz M, 2016. The visual system of harvestmen (Opiliones, Arachnida, Chelicerata): a re-examination. *Frontiers in Zoology*. doi:10.1186/s12983-016-0182-9. **opened**: read as the full text in the collection (`arachnids-other`). L52 to L56.
- Lehmann T, Melzer RR, 2013. Looking like Limulus? Retinula axons and visual neuropils of the median and lateral eyes of scorpions. *Frontiers in Zoology*. doi:10.1186/1742-9994-10-40. **opened**: read as the full text in the collection (`arachnids-other`). L43 to L45.
- Lehmann T, Melzer RR, 2017. A tiny visual system: retinula axons and visual neuropils of Neobisium carcinoides (Hermann, 1804) (Chelicerata, Arachnida, Pseudoscorpiones). *Zoologischer Anzeiger*. doi:10.1016/j.jcz.2017.11.014. **opened**: read as the abstract in the collection (`arachnids-other`). L75.
- Lehmann T, Melzer RR, 2018. Also looking like Limulus? Retinula axons and visual neuropils of Amblypygi (whip spiders). *Frontiers in Zoology*. doi:10.1186/s12983-018-0293-6. **opened**: read as the full text in the collection (`arachnids-other`). L69 to L71.
- Lehmkuhl AM, Muthusamy A, Wagenaar DA, 2018. Responses to mechanically and visually cued water waves in the nervous system of the medicinal leech. *Journal of Experimental Biology*. doi:10.1242/jeb.171728. **opened**: read as the abstract in the collection (`worms-myriapods`). L117.
- Lewis JGE, 1981. Sensory responses and related behaviour. In: The Biology of Centipedes. *Cambridge University Press*. doi:10.1017/cbo9780511565649.007. **opened**: read as the abstract in the collection (`worms-myriapods`). L102 to L103.
- Littlewood PMH, Blower JG, 1987. The chemosensory behaviour of Lithobius forficatus. 1. Evidence for a pheromone released by the coxal organs (Myriapoda: Chilopoda). *Journal of Zoology*. doi:10.1111/j.1469-7998.1987.tb07453.x. **opened**: read as the abstract in the collection (`worms-myriapods`). L187.
- Liu X, Sigwart JD, Sun J, 2023. Phylogenomic analyses shed light on the relationships of chiton superfamilies and shell-eye evolution. *Marine Life Science & Technology*. doi:10.1007/s42995-023-00207-9. **opened**: read as the full text in the collection (`snails-molluscs`). L147.
- Locket A, 2001. Eyes and vision. In: Brownell P, Polis G (eds) Scorpion Biology and Research. *Oxford University Press*. doi:10.1093/oso/9780195084344.003.0003. **opened**: read as the abstract in the collection (`arachnids-other`). L180.
- Loria SF, Prendini L, 2014. Homology of the lateral eyes of Scorpiones: a six-ocellus model. *PLoS ONE*. doi:10.1371/journal.pone.0112913. **opened**: read as the full text in the collection (`arachnids-other`). L49 to L51.
- Machan L, 1968. Spectral sensitivity of scorpion eyes and the possible role of shielding pigment effect. *Journal of Experimental Biology*. doi:10.1242/jeb.49.1.95. **opened**: read as the abstract in the collection (`arachnids-other`). L23 to L25.
- Marek PE, Bond JE, 2009. A Müllerian mimicry ring in Appalachian millipedes. *Proceedings of the National Academy of Sciences*. doi:10.1073/pnas.0810408106. **opened**: read as the abstract in the collection (`worms-myriapods`). L92.
- Matsuo R, Koyanagi M, Sugihara T, Shirata T, Nagata T, Inoue K, Matsuo Y, Terakita A, 2023. Functional characterization of four opsins and two G alpha subtypes co-expressed in the molluscan rhabdomeric photoreceptor. *BMC Biology*. doi:10.1186/s12915-023-01789-7. **opened**: read as the full text in the collection (`snails-molluscs`). L141 to L143.
- Matsuo Y, Kawakami A, Matsuo R, 2024. Visual afferents from an eye in the terrestrial slug Limax valentianus. *Journal of Comparative Neurology*. doi:10.1002/cne.25600. **opened**: read as the abstract in the collection (`snails-molluscs`). L183 to L184.
- Meyer-Rochow VB, 1987. Aspects of the functional anatomy of the eyes of the whip-scorpion Thelyphonus caudatus (Chelicerata: Arachnida) and a discussion of their putative performance as photoreceptors. *Journal of the Royal Society of New Zealand*. doi:10.1080/03036758.1987.10418165. **opened**: read as the abstract in the collection (`arachnids-other`). L37 to L40.
- Meyer-Rochow VB, Liddle AR, 1988. Structure and function of the eyes of two species of opilionid from New Zealand glow-worm caves (Megalopsalis tumida: Palpatores, and Hendea myersi cavernicola: Laniatores). *Proceedings of the Royal Society B*. doi:10.1098/rspb.1988.0023. **opened**: read as the abstract in the collection (`arachnids-other`). L59 to L63.
- Meyer-Rochow VB, Müller CHG, Lindström M, 2006. Spectral sensitivity of the eye of Scutigera coleoptrata (Linnaeus, 1758) (Chilopoda: Scutigeromorpha: Scutigeridae). *Applied Entomology and Zoology*. doi:10.1303/aez.2006.117. **opened**: read as the abstract in the collection (`worms-myriapods`). L94 to L96.
- Meyer-Rochow VB, Yamahama Y, 2022. An anatomical and ultrastructural study of the eye of the luminescent millipede Paraspirobolus lucifugus (Gervais 1836) (Diplopoda, Spirobolida, Spiroboleliidae). *Arthropod Structure & Development*. doi:10.1016/j.asd.2022.101171. **opened**: read as the abstract in the collection (`worms-myriapods`). L81 to L83.
- Mitra O, Callaham MA, Smith ML, Yack JE, 2008. Grunting for worms: seismic vibrations cause Diplocardia earthworms to emerge from the soil. *Biology Letters*. doi:10.1098/rsbl.2008.0456. **opened**: read as the abstract in the collection (`worms-myriapods`). L108 to L109.
- Moritz L, Blanke A, Hammel JU, Wesener T, 2021. First steps toward suctorial feeding in millipedes: comparative morphology of the head of the Platydesmida (Diplopoda: Colobognatha). *Invertebrate Biology*. doi:10.1111/ivb.12312. **opened**: read as the abstract in the collection (`worms-myriapods`). L93.
- Murayama GP, Willemart RH, 2019. Are trichobothria used in terrestrial prey capture by the yellow scorpion Tityus serrulatus Lutz & Mello, 1922 (Buthidae)? *Arachnology*. doi:10.13156/arac.2019.18.3.287. **opened**: read as the abstract in the collection (`arachnids-other`). L175.
- Müller CHG, Sombke A, Hilken G, Rosenberg J, 2011. Chilopoda: sense organs. In: Minelli A (ed.) Treatise on Zoology, The Myriapoda, volume 1. *Brill, Leiden*. doi:10.1163/9789004188266_013. **opened**: read as the abstract in the collection (`worms-myriapods`). L97.
- Nisani Z, Honaker A, Jenne V, Loya F, Moon H, 2018. Evidence of airborne chemoreception in the scorpion Paruroctonus marksi (Scorpiones: Vaejovidae). *Journal of Arachnology*. doi:10.1636/joa-16-092.1. **opened**: read as the abstract in the collection (`arachnids-other`). L173.
- Paskin TR, Jellies J, Bacher J, Beane WS, 2014. Planarian phototactic assay reveals differential behavioral responses based on wavelength. *PLoS ONE*. doi:10.1371/journal.pone.0114708. **opened**: read as the full text in the collection (`worms-myriapods`). L119.
- Patten BM, 1919. Photoreactions of partially blinded whip-tail scorpions. *Journal of General Physiology*. doi:10.1085/jgp.1.4.435. **opened**: read as the full text in the collection (`arachnids-other`). L74.
- Perret J-L, Guerin PM, Diehl P-A, Vlimant M, Gern L, 2003. Darkness induces mobility, and saturation deficit limits questing duration, in the tick Ixodes ricinus. *Journal of Experimental Biology*. doi:10.1242/jeb.00345. **opened**: read at https://libra.unine.ch/handle/123456789/18757. L158 to L160.
- Phillis WA, Cromroy HL, 1977. The microanatomy of the eye of Amblyomma americanum (Acari: Ixodidae) and resultant implications of its structure. *Journal of Medical Entomology*. doi:10.1093/jmedent/13.6.685. **opened**: read as the abstract in the collection (`arachnids-other`). L151 to L152.
- Prévost ED, Stemme T, 2020. Non-visual homing and the current status of navigation in scorpions. *Animal Cognition*. doi:10.1007/s10071-020-01386-z. **opened**: read as the full text in the collection (`arachnids-other`). L10 to L22.
- Pulido Forero IC, 2026. Histology and electrical response of the eye in Tityus macrochirus and Centruroides edwardsii scorpions: Buthidae (thesis, Universidad Distrital Francisco José de Caldas). *Repositorio Universidad Distrital*. http://hdl.handle.net/11349/100704. **opened**: read as the abstract in the collection (`arachnids-other`), matched by title. L41.
- Quinlan PD, Cho AK, Katz PS, 2021. Characterization of visually-guided behaviors by the nudibranch, Berghia stephanieae (SICB 2021 annual meeting, abstract 82-5). *Society for Integrative and Comparative Biology*. https://sicb.org/?p=43735. **opened**: read at https://sicb.org/?p=43735. L195.
- Rivera Roldan NM, Gaffin DD, 2018. New, sensitive behavioral assay shows scorpions are attracted to multiple wavelengths of light. *Journal of Arachnology*. doi:10.1636/joa-s-17-068.1. **opened**: read as the abstract in the collection (`arachnids-other`). L34.
- Roberts RG, 2014. What goes '99-thump?'. *PLoS Biology*. doi:10.1371/journal.pbio.1002006. **opened**: read as the abstract in the collection (`arachnids-other`). L101, L185.
- Rudman WB, 1999. The nudibranch head (Sea Slug Forum, Australian Museum; first posted 26 March 1999, page metadata 15 July 2010). *Sea Slug Forum*. https://www.seaslugforum.net/headeudo.htm. **opened**: read at https://www.seaslugforum.net/headeudo.htm. L181 to L182.
- Shekhter ED, Zimachev MM, Arakelov GG, 1993. Vision in the edible snail. The morphology and total electrical activity of the retina (in Russian; English abstract on PubMed). *PubMed record 1336285*. https://pubmed.ncbi.nlm.nih.gov/1336285/. **opened**: read as the abstract in the collection (`snails-molluscs`), matched by title. L140.
- Silva NFS, Fowler-Finn KD, Mortara SR, Willemart RH, 2018. A Neotropical armored harvestman (Arachnida, Opiliones) uses proprioception and vision for homing. *Behaviour*. doi:10.1163/1568539x-00003503. **opened**: read as the abstract in the collection (`arachnids-other`). L64.
- Sombke A, Rosenberg J, Hilken G, Westermann M, Ernst A, 2011. The source of chilopod sensory information: external structure and distribution of antennal sensilla in Scutigera coleoptrata (Chilopoda, Scutigeromorpha). *Journal of Morphology*. doi:10.1002/jmor.10999. **opened**: read as the abstract in the collection (`worms-myriapods`). L186.
- Speiser DI, Eernisse DJ, Johnsen S, 2011. A chiton uses aragonite lenses to form images. *Current Biology*. doi:10.1016/j.cub.2011.03.033. **opened**: read as the abstract in the collection (`snails-molluscs`), matched by title. L146.
- Steinmetz SB, Bost KC, Gaffin DD, 2004. Response of male Centruroides vittatus (Scorpiones: Buthidae) to aerial and substrate-borne chemical signals. *Euscorpius*. doi:10.18590/euscorpius.2004.vol2004.iss12.1. **opened**: read as the abstract in the collection (`arachnids-other`). L171.
- Stewart NL, Stahlman H, Stewart RL, Lehman ML, Luce-Fedrow A, 2025. A field study examining the attraction of adult Dermacentor variabilis to heat stimuli associated with road edge habitats. *Pathogens*. doi:10.3390/pathogens14111147. **opened**: read as the abstract in the collection (`arachnids-other`). L165.
- Stowasser A, et al., 2019. Electrophysiology and transcriptomics reveal two photoreceptor classes and complex visual integration in Hirudo verbana. *Journal of Experimental Biology*. doi:10.1242/jeb.201764. **opened**: read as the full text in the collection (`worms-myriapods`). L111 to L113.
- Sunada H, Lukowiak K, Sakakibara M, 2012. Repetitive noxious stimulus altered the shadow-induced withdrawal behavior in Lymnaea. *Acta Biologica Hungarica 63 (Suppl. 2): 179-189*. doi:10.1556/ABiol.63.2012.Suppl.2.23. **opened**: read at https://real.mtak.hu/72427/. L196.
- Velilla E, Collinson E, Bellato L, Berg MP, Halfwerk WH, 2021. Vibrational noise from wind energy-turbines negatively impacts earthworm abundance. *Oikos*. doi:10.1111/oik.08166. **opened**: read as the abstract in the collection (`worms-myriapods`). L110.
- Warburg MR, 2013. The circadian rhythm and visual elements in scorpions: a review. *(venue not given in the OpenAlex record)*. https://openalex.org/W2417182375. **opened**: read as the abstract in the collection (`arachnids-other`), matched by title. L42.
- Willemart RH, Chelini M-C, 2007. Experimental demonstration of close-range olfaction and contact chemoreception in the Brazilian harvestman, Iporangaia pustulosa. *Entomologia Experimentalis et Applicata*. doi:10.1111/j.1570-7458.2007.00527.x. **opened**: read as the abstract in the collection (`arachnids-other`). L68.
- Willemart RH, Farine J-P, Gnaspini P, 2008. Sensory biology of Phalangida harvestmen (Arachnida, Opiliones): a review, with new morphological data on 18 species. *Acta Zoologica*. doi:10.1111/j.1463-6395.2008.00341.x. **opened**: read as the abstract in the collection (`arachnids-other`). L57 to L58.
- Yang X, Norma-Rashid Y, Lourenço WR, Zhu M-S, 2013. True lateral eye numbers for extant buthids: a new discovery on an old character. *PLoS ONE*. doi:10.1371/journal.pone.0055125. **opened**: read as the full text in the collection (`arachnids-other`). L46 to L48.
- Yao Z, Yuan L, Chen X, Wang Q, Chai L, Lu X, Yang F, Wang Y, Yang S, 2023. A thermal receptor for nonvisual sunlight detection in myriapods. *Proceedings of the National Academy of Sciences*. doi:10.1073/pnas.2218948120. **opened**: read as the full text in the collection (`worms-myriapods`). L104 to L105.
- Yong E, 2011. Why do scorpions glow in the dark (and could their whole bodies be one big eye)? (National Geographic, Not Exactly Rocket Science, 23 December 2011). *National Geographic*. https://www.nationalgeographic.com/science/article/why-do-scorpions-glow-in-the-dark-and-could-their-whole-bodies-be-one-big-eye. **opened**: read at https://www.nationalgeographic.com/science/article/why-do-scorpions-glow-in-the-dark-and-could-their-whole-bodies-be-one-big-eye. L35 to L36.
- Zieger MV, Meyer-Rochow VB, 2008. Understanding the cephalic eyes of pulmonate gastropods: a review. *American Malacological Bulletin*. doi:10.4003/006.026.0206. **opened**: read as the abstract in the collection (`snails-molluscs`). L133 to L136.
- Zieger MV, Vakoliuk IA, Tuchina OP, Zhukov VV, Meyer-Rochow VB, 2008. Eyes and vision in Arion rufus and Deroceras agreste (Mollusca; Gastropoda; Pulmonata): what role does photoreception play in the orientation of these terrestrial slugs? *Acta Zoologica*. doi:10.1111/j.1463-6395.2008.00369.x. **opened**: read as the abstract in the collection (`snails-molluscs`). L125 to L127.

**Other sources opened.**

- GBIF occurrence API, dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7. Class and order facets of 11 October 2026 saved in `runs/fetch/10/` on the `ci` branch (`world-class.json`, `world-order.json`, `world-phylum.json` and the saved name lists). Family facets read through the web tool on 13 October 2026 for Scorpiones (taxon key 872), Opiliones (907), Sabellida (1080), Scutigeromorpha (1025), Platyhelminthes (108), Annelida (42) and Littorinimorpha (7390893), with names from the species API (family lists under 872, 907, 1080 and 7390893; keys 10785866 Hadruridae, 10806831 Belisariidae, 8268 Scutigeridae, 7064 Strombidae, 7072 Naticidae; matches for Lumbricidae and Pseudocerotidae). **opened**.
- iNaturalist open-data snapshot of 27 September 2026, species list `runs/coverage/2-lists/world.tsv.gz` on the `ci` branch (research grade, all years). **opened**.
- Oxford Academic, *Scorpion Biology and Research* (2001), https://academic.oup.com/book/52750, for the book title and DOI behind Locket (2001). **opened**.
- Zenodo record 895450 (https://zenodo.org/record/895450), for the authors, DOI and abstract of Gaffin and colleagues (2012); its file was refused (HTTP 429). **opened** (record page).
- Caves, Brandley and Johnsen (2018), *Trends in Ecology & Evolution*, from the owner's library; it mentions none of the unit's animals and nothing from it is used. **opened**.
- This repository: `docs/views/research/BRIEF.md`, `docs/VIEWS.md`, `docs/COVERAGE.md`, `docs/SOURCES.md`, `docs/tracks/engine.md`, `docs/views/world-orders.csv`, `docs/views/no-view-us-fl-alachua.csv`, `docs/views/sheets/snail.md`, `snail.audit.md`, `tick.md`, `tick.audit.md`, `src/cam.a.js` (`EYES`, `GROUPS`, `paramsOf`, `VIEW_DEG`), `src/cam.b.js` (blur rule) and `src/cam.r.js` (word table). **opened**.

**Secondary: works known only through the source named.**

- Zieger and colleagues 2009, cited by Irwin and colleagues (2022) for 52 degrees in *Arion rufus*; it is the Acta Zoologica paper whose abstract I opened (Zieger and colleagues 2008), and the number itself is **secondary** (Irwin and colleagues 2022).
- Seyer (1992), *Littorina littorea* 3.6 degrees: **secondary** (Irwin and colleagues 2022).
- Land (1981a), *Littorina* 4.5 degrees and *Planaria* 35 degrees: **secondary** (Land and Nilsson 2012, Table 3.1).
- Nishiyama, Nagata, Matsuo and Matsuo (2019), the slug's brain light sense: **secondary** (Knight 2019).
- Gaffin, Bumm, Taylor, Popokina and Mann (2012), scorpions with covered eyes: **secondary** (Yong 2011), with its abstract page opened on Zenodo.
- Locket (2001), 360 degrees, low-resolution median eyes, shielding pigment migration: **secondary** (Prévost and Stemme 2020); only the chapter's abstract was opened.
- Fleissner and Fleissner (2001), median eyes as the main eyes: **secondary** (Lehmann and Melzer 2013).
- Görner (1959) and Klein (1934), centipede skototaxis: **secondary** (Lewis 1981).
- Brownell and Farley (1979a, b), tarsal vibration sensing: **secondary** (Babu 1985).
- Scheuring (1913), star-shaped rhabdoms in scorpion lateral eyes: **secondary** (Land 1985).
- Kretz, Stent and Kristan (1976), about 50 photoreceptors in each leech eyecup and a single green class: **secondary** (Groves and Jellies 2021; Stowasser and colleagues 2019).
- Willemart and colleagues, a *Leiobunum* fleeing a large dark object: **secondary** (Lehmann and colleagues 2016).
- Hamilton and Winter (1982), title only, from the collection index, used to withdraw the garden snail's 14.5 degrees.

## 8. Questions for a specialist

1. How finely do a scorpion's median eyes resolve (receptor spacing and acceptance angle), and do its lateral eyes carry any image? Do Locket's figures hold for the bark scorpions (*Centruroides*) that people photograph most?
2. At night, are a scorpion's lateral eyes about one log unit or ten log units more sensitive than its median eyes?
3. Does a scorpion's fluorescent cuticle help it detect light at natural ultraviolet levels at dusk or under the moon, and over which wavelengths?
4. What do the common harvestmen (*Phalangium opilio*, *Leiobunum*) see: the spectral sensitivity and the resolution of their turret eyes, and how far do the two fields reach forward and back?
5. Has anyone measured the interommatidial angles or behavioural acuity of the house centipede, *Scutigera coleoptrata*?
6. Do the common land snails (*Cornu aspersum*, *Cepaea nemoralis*) resolve anything finer than the red slug's 52 degrees, and do they respond to moving or looming shapes?
