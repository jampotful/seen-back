# Herps: alligator, reptiles, frog and salamander (research round 3, unit `herps`)

Written on 13 October 2026, from 01:48 UTC, on branch `research/herps`. The evidence log is `docs/views/evidence/herps.jsonl` (cited below as L1, L2 and so on, by line number), and the wanted list is `docs/views/wanted/herps.jsonl`. This sheet replaces `docs/views/sheets/salamander.md` where it goes further, re-checks the `alligator`, `reptile` and `frog` entries of `EYES` in `src/cam.a.js`, and proposes nine views in their place.

What could and could not be read:

- **Land and Nilsson (2012), *Animal Eyes*, 2nd edition**, from the owner's library. A first text extraction stopped near page 66. The whole book (291 pages) then came through as a PDF, and I read every passage on reptiles and amphibians in it: chapters 1 to 3, the land-vertebrate eyes of chapter 5 (pp. 94 to 129, with the visual fields of pp. 116 to 117 read from the rendered figure, and "Amphibious eyes" on pp. 117 to 119), and "Movements of the eyes" (chapter 9, pp. 215 to 242). Nineteen log lines come from it (L22 to L27, L193, L202 to L213).
- **Sites that refused with HTTP 429**, after which I fetched nothing more from them: Europe PMC's REST service (for Bakken and Krochmal 2007 and Gracheva and colleagues 2010), the Crossref API (for the year of Fite and Lister), journals.plos.org (for the species table of Inger and colleagues 2014), and link.springer.com (for doi 10.1007/BF00611872, after nine abstracts had been read there). PubMed, PubMed Central, the Journal of Experimental Biology and IEEE Xplore returned bot checks or empty pages.
- The shell on this machine could reach only GitHub, so every web page was read through the fetch tool, which answers questions about a page. Every quotation in the log was asked for verbatim, and short quotations are what the log keeps.

## 1. Scope

### What the four views hold today

Counts are iNaturalist research-grade records in GBIF (dataset `50c9509d-22c7-4a22-a47d-8c48425ef4a7`), read through the GBIF API on 13 October 2026 as facets by family and genus. Family names come from `https://api.gbif.org/v1/species/{key}` and from `runs/fetch/10` on the `ci` branch, whose counts for the older family keys matched mine exactly. Common names are my glosses.

| View today | Taxa | World records | Alachua records (to 2024) |
|---|---|---:|---:|
| `alligator` | Crocodylia | 128,405 | 2,781 (all American Alligator) |
| `reptile` | Squamata 3,778,723, Testudines 842,818, Sphenodontia (tuatara) 1,672 | 4,623,213 | 9,642 |
| `frog` | Anura | 2,055,810 | 4,857 |
| `salamander` (a group with no view yet) | Caudata 631,944, Gymnophiona 1,048 (counts from the earlier sheet, read 12 October) | 632,992 | 148 |

The reptile view alone holds more records than the bee view (4,555,326 in `docs/VIEWS.md`), and it is one guessed row today.

**Most recorded worldwide.** Squamates: Western Fence Lizard 151,228; Common Garter Snake 144,689; Green Anole 110,190; Brown Anole 109,010; Common Wall Lizard 79,644; Side-blotched Lizard 66,657; Northern Watersnake 64,594; Green Iguana 58,609; Gopher Snake 56,890; Dekay's Brownsnake 44,841. Turtles: Pond Slider 172,017; Painted Turtle 133,906; Common Snapping Turtle 87,673. Frogs: American Toad 152,297; Green Frog 114,582; American Bullfrog 101,114; Common Toad 77,425; Common Frog 64,712. The two European species near the top of the frog list, the common toad and the common frog, are the animals of most of the classic experiments on amphibian vision (L118, L121, L122, L125, L126).

**Most recorded in Alachua County** (`data/regions/us-fl-alachua/species.json`, records through 2024). Reptiles: Brown Anole 2,194; Green Anole 1,316; North American Racer 596; Banded Watersnake 525; Florida Softshell 458; Pond Slider 425; Gopher Tortoise 389; Eastern Fence Lizard 358; Common Box Turtle 225; Striped Mud Turtle 221; Common Ribbon Snake 215; Florida Cottonmouth 213. Frogs: Southern Toad 961; Cuban Tree Frog 908; Green Treefrog 895; Squirrel Tree Frog 401; Greenhouse Frog 247. Salamanders: Striped Newt 31; Eastern Newt 30; Two-toed Amphiuma 26; Greater Siren 20. Every gecko recorded in the county is a nocturnal house gecko (*Hemidactylus*, 341 records, and one Tokay), and every viper is a pit viper (Florida Cottonmouth, Eastern Diamondback, Pygmy and Timber Rattlesnakes, 335 records).

### Where the views should split

The reptile view cannot be one picture. The groups inside it differ in the number and tuning of their colour-sensing cells, in sharpness by a factor of about ten, in where their sharp regions lie, in pupil shape, in whether they see colour at night, and in whether they carry a heat sense that joins sight in the brain. The commitments, with the evidence for each line:

1. **Turtles apart from the rest.** Turtles have four cone types with red, orange, yellow and clear oil droplets and red-sensing cells near 620 nm (L100 to L106, L109 to L111), a horizontal streak (L112, L179) and slow photoreceptors (L107). Snakes mostly have two cone types (L77 to L80, L40), and lizards have yellow and green droplets and no red ones (L55, L111).
2. **Snakes apart from lizards.** Snakes measured see about 2.3 to 2.9 cycles per degree (L87, L88, L90) and mostly have two cone types; anoles reach about 12 at the fovea (L175). Snakes have no third eye (lizards do: L69, L70) and lean on the tongue and the vomeronasal organ (L93, L99).
3. **Heat-sensing snakes apart from other snakes.** Pit vipers, pythons and many boas carry pits whose heat signals land on the same brain map as sight (L30, L31, L36, L48, L196). Colubrids lack them (L38). The split is by subfamily Crotalinae and families Boidae and Pythonidae. Some boas have no pits and still sense heat less well (L36, L48); they stay in the heat view.
4. **Geckos at night apart from lizards by day.** Nocturnal geckos have no rods, see colour in moonlight, have multifocal optics and slit pupils that close to pinholes, and lack the third eye (L63 to L67, L70, L136, L170). Day geckos (*Phelsuma*, *Lygodactylus*) have single-focus eyes (L65) and cone retinas tuned like other day lizards (L199), and they go with `lizard`.
5. **Anoles apart from other lizards.** Anoles have two foveae in each eye (L58, L59), measured acuity in the commonest Alachua species (L174 to L176), measured ultraviolet vision (L54, L56, L60) and measured motion preferences (L61, L62), and they hunt by sight with little use of smell (L95, L96). They are 36.4% of Alachua's reptile records.
6. **Blind snakes and worm lizards to `other`.** Blind snakes have a much reduced visual system (L200). The Florida Worm Lizard is sent with them on its burrowing life alone; I opened no source on its eyes.
7. **Crocodilians stay one view.** Alligators and crocodiles share the streak, the slit pupil and the face domes, and the measured alligator cones (L1 to L6) are close to those of crocodiles (L10 to L14).
8. **Frogs stay one view.** Toads, ranid frogs and treefrogs share two rod types (L126, L130), a movement-led prey response with stationary vision kept (L118 to L123) and acuity near 1 to 4 cycles per degree (L114 to L116). Diurnal poison frogs (Dendrobatidae, 1.1% of frog records) are the first candidates for a split later.
9. **Salamanders and newts as one view; caecilians and the olm to `other`.** This is the earlier sheet's split, now with a measured acuity and evidence on still prey (L140, L141, L149, L161). Caecilians: L157. The olm (L152, L153) is outside the view.

Record shares of the present reptile view after the split. Pit vipers are counted from twelve resolved genera (*Crotalus*, *Agkistrodon*, *Trimeresurus*, *Bothrops*, *Sistrurus*, *Bothriechis*, *Tropidolaemus*, *Protobothrops*, *Gloydius*, *Craspedocephalus*, *Porthidium*, *Ovophis*: 205,014 of the 245,739 viperid records); six genera without pits hold 35,900 (*Vipera*, *Bitis*, *Echis*, *Daboia* and *Cerastes*, the true vipers, and *Causus*, the night adders), and 4,825 viperid records in small genera were not resolved and stay with `snake`. The sorting follows Wikipedia, read on 13 October 2026: its list of crotaline species names eleven of the twelve pit-viper genera, and its *Craspedocephalus* page places that genus in Crotalinae; its Viperinae page lists five of the six genera without pits, says true vipers lack "the heat-sensing pit organs that characterize their sister group", and puts *Causus* in a subfamily of its own, Causinae. Day geckos are *Phelsuma* (15,648) and *Lygodactylus* (9,434) of the 206,629 Gekkonidae records; Sphaerodactylidae (16,462) were not resolved by genus and stay with `gecko`.

| Proposed view | Taxa | World records | Share of the reptile view | Alachua records | Share in Alachua |
|---|---|---:|---:|---:|---:|
| `lizard` | lizards except anoles, nocturnal geckos and worm lizards; day geckos; tuatara | 1,744,380 | 37.7% | 914 | 9.5% |
| `snake` | snakes except pit vipers, boas, pythons and blind snakes | 1,211,317 | 26.2% | 2,370 | 24.6% |
| `turtle` | Testudines | 842,818 | 18.2% | 2,117 | 22.0% |
| `anole` | Dactyloidae | 289,683 | 6.3% | 3,511 | 36.4% |
| `gecko` | Gekkota except *Phelsuma* and *Lygodactylus* | 269,472 | 5.8% | 342 | 3.5% |
| `pitviper` | Crotalinae, Boidae, Pythonidae | 249,492 | 5.4% | 337 | 3.5% |
| `other` (light only) | blind snakes, worm lizards | 16,051 | 0.3% | 51 | 0.5% |

Within turtles, sea turtles are 5.8% (L178, L179 and L201 cover them), and pond turtles (Emydidae) 61.6%. Within crocodilians, Alligatoridae are 70.5%, Crocodylidae 29.0% and Gavialidae 0.5%. Within frogs, Ranidae are 30.0%, Bufonidae 28.1% and the treefrog families 27.4%.

**The set of views I commit to:** `alligator`, `turtle`, `snake`, `pitviper`, `lizard`, `anole`, `gecko`, `frog` and `salamander`. Blind snakes, worm lizards, caecilians and the olm go to `other`. `tools/species/eyes.py` would route by family (and Crotalinae by genus, since the GBIF backbone gives no subfamily), and the word table in `src/cam.r.js` would need "anole", "gecko", "rattlesnake", "viper", "python", "boa", "turtle", "tortoise" and "terrapin" entries. I did not change either file.

## 2. The proposed views

Rows follow the pattern of build 22. Each row is followed by the log lines behind it. In the picture tables, **invented** marks a value that is the app's own choice.

### 2.1 `alligator` (Crocodylia): revised

```
['m', 'Colour', 'Alligators have colour-sensing cells of three main kinds, tuned to blue, green and yellow light, close to the three kinds people have. They have none for ultraviolet. This view leaves colours as your camera shows them.'],
```
L1 to L6 (Sillman and colleagues 1991: single cones at 444 and 535 nm, double cones at 566 and 503 nm, in the alligator itself), L21 (Guo and colleagues 2023: no ultraviolet pigment), L193 (a person's red-sensing cone peaks near 564 nm). No behavioural test of colour vision in a crocodilian was found.

```
['g', 'Sharpest band', 'The crocodiles that have been measured see most sharply along a band level with the horizon. This view sharpens the same band and blurs what lies above and below it.'],
```
L9 (Nagloo and colleagues 2016, saltwater and freshwater crocodiles).

```
['g', 'Sharpness', 'At their sharpest, saltwater and freshwater crocodiles see about a seventh as much detail as people do. This view is blurred to match.'],
```
L7, L8 (8.8 and 8.0 cycles per degree; 60 / 8.4 is about 7).

```
['g', 'Pupil', 'Alligators and crocodiles have pupils that close to vertical slits, a shape common in animals that wait in ambush. A caiman turns its eyes as it raises or lowers its head, which keeps the slit upright. A slit like this smears out-of-focus things up and down, and this view does the same.'],
```
L169, L195 (Banks and colleagues 2015), L171 (caiman eye rotation, cited there).

```
['g', 'Night', 'An alligator’s retina holds far more rods, the cells that work in dim light, than cones, and its rods adjust to the dark quickly. Behind the retina, crocodilians have a reflecting layer that sends light back through it a second time. This view brightens the shadows.'],
```
L5 (rods dominate the alligator retina), L18 (Wald and colleagues 1957: rods dark-adapt at the pace of cones in other animals), L19 (Ollivier and colleagues 2004: a retinal tapetum in crocodilians).

```
['g', 'Under water', 'Crocodilians focus well on distant things in air. Under water their eyes are badly out of focus. This view shows the world above the water.'],
```
L162 (Fleishman and colleagues 1988, six crocodilian species).

```
['x', 'Touch', 'Alligators have small dark domes dotted over the skin of the jaws and face. The domes respond to pressure and vibration more sensitively than your fingertips, and some respond best to the ripples a small splash makes. A waiting alligator turns toward silent ripples even in total darkness, and a camera records none of this.'],
```
L164, L165 (Leitch and Catania 2012, as reported by Vanderbilt University; the domes ignore electric fields and salt), L166 (Soares 2002).

```
['x', 'Hearing', 'Alligators hear low and middle-pitched sounds, from about 100 to 8,000 vibrations a second in air, most keenly near 1,000. Under water they hear from 100 to 2,000 vibrations a second. A camera records no sound.'],
```
L167, L168 (Higgs and colleagues 2002).

```
['g', 'Field of view', 'In most reptiles the eyes face out to the sides, each taking in about 170 degrees, and the two views overlap by a few tens of degrees in front. No one has measured an alligator’s field. This view follows the general rule, bending the picture at its edges to fit about 310 degrees.'],
```
L202, L203 (Land and Nilsson 2012, pp. 116 to 117). The total is my arithmetic: 2 × 170 − about 30 = 310. The same rule gives 307 degrees for the one snake measured, beside its measured 308.5 (L85, L86).

```
['i', 'Depth', 'How an alligator judges distance has not been measured, so depth here is guessed from height in the frame, and a tap moves the focus.'],
```
No source.

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Alligator, crocodile', 'an alligator or crocodile' | The app's wording; the view covers crocodiles (29% of records). |
| `fov` | 310 (was 280) | L202, L203: two eyes of about 170 degrees overlapping by a few tens of degrees; the overlap of 30 is **invented** within that range. |
| `cpd` | 8.4 | L7, L8 (mean of the two crocodiles; was 9, graded a guess). |
| `topoS` | 1 | L9. |
| `fall` | 2.6 | **invented** (unchanged; the abstract gives no gradient). |
| `pupil` | 'v' | L169, L171, L195. |
| `dof` | 24 | **invented** strength (unchanged). |
| `gain` | 1.6 | Direction from L5, L18, L19; the amount is **invented**. |
| `sat` | unset (was .9) | Nothing supports muting colour: L1 to L3. |
| `M`, `uvBlue`, `sheen` | unset | L21: no ultraviolet pigment, so no violet tint. |
| `rate`, `persist` | unset | No crocodilian flicker value was found. |
| `cue` | 'The sharpest part is a band along the horizon. Tap the side of your phone to send a ripple along the waterline.' | The app's wording. |

**New effects.**

- **Ripples felt by the face.** A tap or knock on the phone, read from the accelerometer (`devicemotion`), sends rings outward along the sharp band from the side the tap came from, fading in about a second. The phone's body stands in for the water's surface, and the accelerometer for the face domes (L164, L166). The phone samples motion at about 60 per second, so it cannot resolve the domes' 20 to 35 Hz tuning; a tap is a broad jolt and serves. Medium work (iOS asks permission for motion). The rings could be drawn as refraction of the picture itself, a lensing of the image along the waterline, with no added colour.
- **The waterline.** When the phone tilts down past the horizon (orientation sensor), the part of the picture below the horizon softens strongly, since crocodilian eyes are badly defocused under water (L162). The mapping from tilt to "under water" is **invented**. Easy.

### 2.2 `turtle` (Testudines): new

```
['m', 'Colour', 'Pond sliders have four kinds of colour-sensing cells, tuned to ultraviolet, blue, green and red light, where people have three. Tests of their behaviour and of their nerve cells show they use all four to see colour. This view deepens colours and adds a violet tint for ultraviolet.'],
```
L100 to L103 (Loew and Govardovskii 2001: 617, 515, 458 and 372 nm), L109 (Ventura and colleagues 2001: ultraviolet opponency), L110 (Rocha and colleagues 2008, reporting behavioural tetrachromacy; the behavioural paper is on the wanted list).

```
['g', 'Coloured filters', 'Each colour-sensing cell in a turtle’s eye holds a droplet of coloured oil, red, orange, yellow or clear, that filters light before it reaches the cell. The filters narrow the colours each cell answers to, which helps in telling similar colours apart in bright light. This view strengthens small differences in colour.'],
```
L104, L105 (the droplets in the Pond Slider), L111 (turtles and birds are the only tetrapods with red droplets), L23 (Land and Nilsson 2012: the droplets "sharpen up" the cones' sensitivities), L113 (Hart and colleagues 2006: a benefit in bright light, a cost in dim light).

```
['m', 'Deep red', 'A turtle’s red-sensing cells respond best to light near 620 to 630 nanometres. A person’s red-sensing cells peak near 564 nanometres, so a turtle’s reach further into deep red. This view gives reds a little extra strength.'],
```
L100, L108 (617 nm pigment, 630 nm with the droplet), L106 (620 nm in Reeves' turtle), L193.

```
['m', 'Sharpness', 'Pond sliders see about a sixth to a fourteenth as much detail as people do, judged by signals recorded from their brains. This view is blurred to match.'],
```
L177 (Northmore and Granda 1991: 4.4 to 9.9 cycles per degree; 60 / 9.9 = 6, 60 / 4.4 = 14). L83 (a box turtle at 0.26 by an eye-movement test, cited by Gomez and colleagues) is far lower; such tests give low figures in reptiles (L180 shows low gains), and the brain recordings agree with the cone spacing.

```
['m', 'Sharpest band', 'A pond slider sees most sharply along a band level with the horizon, where the cells that carry the retina’s signals to the brain are packed most densely. Sea turtle hatchlings have similar bands, and some turn their eyes to keep them level. This view sharpens the same band.'],
```
L112 (Peterson and Ulinski 1979), L179 (Oliver and colleagues 2000).

```
['m', 'Slow eyes', 'A pond slider’s colour-sensing cells take about a tenth to a fifth of a second to respond fully to a weak flash at 20 degrees Celsius. Reptiles as a group stop seeing flicker at about 43 flashes a second on average, a little slower than people. This view leaves short trails behind things that move.'],
```
L107 (Baylor and Hodgkin 1973), L139 (Inger and colleagues 2014).

```
['x', 'Hearing', 'Pond sliders hear low sounds best, around 300 to 500 vibrations a second, and their ears are more sensitive under water than in air. A camera records no sound.'],
```
L191 (Christensen-Dalsgaard and colleagues 2012).

```
['i', 'Ultraviolet', 'A phone camera captures little ultraviolet light, so the violet tint here stands in for what a turtle’s fourth kind of colour-sensing cell sees.'],
```
No source for the stand-in.

```
['g', 'Under water', 'Turtles that live in water, like diving ducks, are thought to keep their focus under water by squeezing the lens forward into the pupil with a ring of muscle. A person’s eye loses most of its focusing power in water. This view keeps the part of the picture below the waterline as sharp as the rest.'],
```
L208 (Land and Nilsson 2012, pp. 118 to 119: "as do aquatic turtles and water snakes"). A person under water loses 40 dioptres and can add only 10 (same pages). The alligator view does the opposite (L162).

```
['g', 'Field of view', 'In most reptiles the eyes face out to the sides, each taking in about 170 degrees, and the two views overlap by a few tens of degrees in front. No one has measured a turtle’s field. This view follows the general rule, bending the picture at its edges to fit about 310 degrees.'],
```
L202, L203.

```
['i', 'Pupil', 'No source we opened gives the shape of a turtle’s pupil, so the round pupil here is a guess.'],
```
L173 gives the pupil's dark dilation (three- to four-fold in area) and no shape.

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Turtle, tortoise', 'a turtle or tortoise' | The app's wording. |
| `fov` | 310 | L202, L203; the overlap of 30 is **invented**. |
| `cpd` | 7 | L177 (middle of 4.4 to 9.9). |
| `topoS`, `fall` | 1, 1.5 | L112, L179; the fall is **invented**. |
| `pupil` | 'o' | **invented** (L173 gives no shape). |
| `sat` | 1.25 | Direction from L23, L100 to L105, L113; amount **invented**. |
| `M` | a mild red boost, for example `[1.1, -0.05, -0.05, 0, 1, 0, 0, 0, 1]` | Direction from L100, L108, L193; values **invented**. |
| `sheen` | .6 | L103, L109; strength **invented**, as for the earlier reptile view. |
| `persist` | .1 | Direction from L107, L139; amount **invented**. |
| `cue` | 'Colours run deeper, with a violet tint for ultraviolet, and quick movements leave short trails.' | The app's wording. |

**New effects.**

- **Oil-droplet colour.** A local colour-contrast filter: hue differences between neighbouring pixels are stretched a little before display, which shows narrowed cone tuning as crisper colour boundaries (L23, L113). Easy in the shader. It should fade as the scene darkens, since droplets cost sensitivity in dim light (L113).
- **Horizon held level.** Brown (1969) reports by his title that the turtle's linear area is held to the horizon by non-visual cues (abstract not available; on the wanted list). If the paper bears this out, the sharp band could follow the phone's roll from the orientation sensor, staying level while the picture tilts. Easy, once the source is read.

### 2.3 `snake` (snakes without heat pits): new

```
['g', 'Colour', 'Most snakes have two kinds of colour-sensing cells, one most sensitive to ultraviolet and one to green and yellow light, where people have three, so they tell apart fewer colours. Some snakes active by day, such as garter snakes, have extra cell types that may let them see more. This view shows colours as a person with two kinds of cells would see them, with a violet tint for ultraviolet.'],
```
L77, L78 (ball python: 361 and 550 nm), L79, L80 (boa: 357 and 549 nm), L40 (vipers: rh1, sws1, lws), L92 (diurnal colubrids have four cone types), L91 (a garter snake's rods transformed into cone-like cells).

```
['g', 'Sharpness', 'Most snakes that have been measured see about a twentieth to a twenty-fifth as much detail as people do. This view is blurred to match.'],
```
L87 (paradise tree snake, 2.89), L88 (two pit vipers, 2.3 to 2.8), L90 (two South American colubrids, 2.4 to 2.7). L84 (a northern watersnake at 4.25, cited by Gomez and colleagues) is higher; L82 (ball python, 0.13 by an eye-movement test) is far lower.

```
['g', 'Field of view', 'A paradise tree snake takes in about 310 degrees around itself, and both of its eyes see a region about 33 degrees wide straight ahead. That fits the general rule for reptiles, two eyes of about 170 degrees each that overlap a little in front. This view bends the picture at its edges to suggest the wider sweep.'],
```
L85, L86 (Zamore and colleagues 2020: 308.5 and 33.0 degrees), L202, L203.

```
['m', 'Movement', 'Garter snakes strike at prey that moves far more readily than at the same prey held still, and the smell of prey makes them strike more. This view brightens whatever moves.'],
```
L98 (Burghardt and Denny 1983, Common Garter Snake).

```
['x', 'Tongue', 'A snake flicks its forked tongue to gather scent particles and carries them to a sense organ that opens into its mouth. Garter snakes find their shelters and one another by this sense, and corn snakes and rat snakes flick their tongues faster when they smell mice. A camera records no scent.'],
```
L93 (Schwenk), L99 (Heller and Halpern 1982), L43 (Saviola and colleagues 2012).

```
['i', 'Ultraviolet', 'Snakes active at night have eyes that let ultraviolet light reach the retina, and some snakes active by day filter it out. A phone camera captures little ultraviolet light, so the violet tint here is a stand-in.'],
```
L81 (Simões and colleagues 2016).

```
['i', 'Pupil', 'Snakes that wait in ambush or hunt at night tend to have vertically slit pupils, and the others tend to have round ones. This view uses a round pupil, which is our guess for the commonest snakes.'],
```
L172 (Brischoux and colleagues 2010).

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Snake', 'a snake' | The app's wording. |
| `fov` | 310 | L85 (308.5 in a colubrid), L202. |
| `cpd` | 2.5 | L87, L88, L90. |
| `topoS`, `fall` | .4, .8 | Streaks in some species (L89, L90); values **invented**. |
| `pupil` | 'o' | **invented**, with L172. |
| `M` | `DEUTAN` | Two cone types (L77 to L80); the matrix is an approximation the app already uses, entered from memory (`docs/SOURCES.md`). |
| `sheen` | .4 | L81; strength **invented**. |
| `dof` | 8 | **invented**. |
| `cue` | 'Colours run together into fewer, and whatever moves stands out.' | The app's wording. |

**New effects.** A **motion-brightening** layer from the motion-salience map: moving regions gain contrast and brightness, decaying over about half a second (L98). Easy once the engine's motion map lands. Smell has no phone input; I propose nothing for it.

### 2.4 `pitviper` (pit vipers, boas and pythons): new

```
['m', 'Heat pits', 'Rattlesnakes, copperheads and other pit vipers have a pit on each side of the face, between the eye and the nostril. A thin membrane in each pit warms when infrared light from a warm body falls on it, and the nerves there respond to warming of a few thousandths of a degree. This view adds a glow over things it guesses are warm.'],
```
L46 (the pits' place), L45 (Moon 2011: 0.003 °C), L35 (Graf and Machta 2024: milli-kelvin), L22 (Land and Nilsson: nerve endings, no visual pigment), L34 (copperhead receptors).

```
['m', 'Coarse heat picture', 'The heat picture is very coarse. Western rattlesnakes could not make out heat patterns finer than about 9 degrees across, the size of a 16-centimetre patch seen from a metre away. This view draws the glow soft and large.'],
```
L28 (Clark and colleagues 2022). L30 (heat cells' receptive fields of 25 to 70 degrees). The patch size is my arithmetic: 2 × tan(4.5°) × 100 cm = 15.7 cm.

```
['m', 'Heat joins sight', 'In a rattlesnake’s brain, signals from the pits and from the eyes arrive on the same map of the world, and some nerve cells respond only when both report the same object. This view lays the heat glow over the camera picture.'],
```
L30, L31 (Hartline and colleagues 1978; Newman and Hartline 1981).

```
['m', 'Warm against cool', 'A pit viper picks out a warm animal most easily against a cool, even background, and far less well against a patterned background or one as warm as the prey. Ambushing sidewinders face toward places where the ground’s temperature changes sharply. This view weakens the glow over busy backgrounds.'],
```
L29 (Clark and colleagues 2022), L33 (Chen and colleagues 2017), L39 (Schraft and colleagues 2019).

```
['m', 'Range', 'A pit viper senses a warm animal’s heat from up to about two-thirds of a metre away. Short-tailed pit vipers striking at mice launched from 1 to 9 centimetres away, and they still caught prey with either their eyes or their pits covered.'],
```
L45 (66.3 cm), L50, L32 (Chen and colleagues 2012). L47 (up to about 1 m, cited by Graf and Machta) is secondary.

```
['g', 'Boas and pythons', 'Most pythons and some boas have rows of heat pits along their lips, and many other boas sense heat through the same nerve endings without pits. Their pits are at least four times less sensitive than a pit viper’s.'],
```
L196, L36, L48.

```
['g', 'Eyes', 'Pit vipers, boas and pythons have two kinds of colour-sensing cells, one for ultraviolet and one for green and yellow light, and see about a twentieth to a twenty-fifth as much detail as people do. This view shows colours as a person with two kinds of cells would see them and blurs the picture to match.'],
```
L40, L77 to L80, L88.

```
['g', 'Pupil', 'Rattlesnakes hunt from ambush, and snakes that hunt this way or at night tend to have vertically slit pupils. A slit smears out-of-focus things up and down, and this view does the same.'],
```
L39, L172, L195.

```
['m', 'A signal for snakes', 'California ground squirrels confronting a rattlesnake wave their tails and heat them up, and the heat makes the snake turn more defensive. They wave without heating for gopher snakes, which have no heat pits.'],
```
L38 (Rundus and colleagues 2007; the defensive shift was shown with a robotic squirrel).

```
['x', 'Tongue', 'A rattlesnake strikes a mouse, lets it go, and then follows its scent trail with the tongue. Rattlesnakes whose tongue-scent organ had been disabled stopped trailing and eating struck prey, and a camera records no scent.'],
```
L44 (Kardong and Bels 1998: the prey is released), L41 (Alving and Kardong 1996), L42 (Graves and Duvall 1985).

```
['x', 'Hearing', 'A ball python hears low sounds best, between 80 and 160 vibrations a second, by sensing how they shake its skull. A camera records no sound.'],
```
L190 (Christensen and colleagues 2012).

```
['i', 'Heat stand-in', 'A phone cannot sense heat, so this view treats things that move as warm, because a pit viper’s heat cells respond most to warm things that appear or move. Real warmth would also light up still people and animals.'],
```
L30.

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Pit viper, boa, python', 'a heat-sensing snake' | The app's wording. |
| `fov` | 310 | From the colubrid (L85) and the general rule (L202, L203); not measured in this group. |
| `cpd` | 2.5 | L88. |
| `topoS`, `fall` | .4, .8 | L89; values **invented**. |
| `pupil` | 'v' | L172, L195. |
| `M` | `DEUTAN` | L40, L77 to L80, with the caveat in 2.3. |
| `sheen` | .3 | L40, L81; strength **invented**. |
| `gain` | 1.3 | Rods dominate (L80, L89); amount **invented**. |
| `dof` | 20 | **invented**. |
| `heat` (new) | glow from the motion map, blurred to at least 9 degrees, transient | L28, L30, L31, L29, L33. |
| `cue` | 'Warm things glow, soft and large. A phone cannot feel heat, so things that move stand in for warm ones.' | The app's wording. |

**New effect: the heat glow.** The camera's motion map, downsampled to a grid about 9 degrees of the animal's field per cell (L28), blurred with a kernel matching the 25 to 70 degree receptive fields (L30), is added over the picture as a soft white-orange glow. Each cell's glow rises when motion appears and decays over about half a second, since the heat cells respond transiently (L30). The glow is divided by the average motion of its surround, so a busy, moving background (wind in leaves, the phone's own movement) weakens it (L29, L33). Cost: a 32 × 24 motion grid and a separable blur, light on a phone. Two upgrades: a person-and-pet segmentation model, which would make still warm bodies glow as real heat would, at the cost of a model on the phone; and, on the few phones with thermal cameras, the real thing. The glow should look like light seen through frosted glass, large and soft, with no hard edges and no false-colour palette, so that it reads as a second sense laid over sight.

### 2.5 `lizard` (lizards by day, day geckos, tuatara): new

```
['g', 'Colour', 'Many lizards active by day have four kinds of colour-sensing cells, one of them tuned to ultraviolet light, where people have three. Droplets of yellow, green or clear oil in the cells filter the light that reaches them. This view deepens colours slightly and adds a violet tint for ultraviolet.'],
```
L51 to L55 (seventeen anoles), L68 (a flat lizard: four single-cone classes), L182 (an Australian dragon: three pigments found), L184 (a skink's yellowish droplets), L23. The authors of L68 write that the visual systems of day lizards "appear to be broadly conserved".

```
['g', 'Sharp centre', 'Many lizards have a fovea, a deep pit in the retina where the cells are packed most tightly, and Australian dragons add a band of sharp sight along the horizon. This view sharpens the centre and the horizon.'],
```
L182, L183 (dragons), L184 (a skink), L198 (lacertids, monitors and gekkonids have the same kind of fovea).

```
['g', 'Sharpness', 'In the anoles that have been measured, the fovea sees about a fifth as much detail as a person and the rest of the eye about a fiftieth. This view uses similar values for other lizards, which is a guess based on that relative.'],
```
L174, L175.

```
['g', 'Third eye', 'Most lizards, apart from geckos and racerunners, have a third eye on top of the head, the parietal eye, with its own small lens and retina, and it forms no picture. Its cells respond in opposite ways to blue and to green light, and wall lizards need it to steer by the sun. This view shows a glow at the top of the screen whose colour follows the balance of blue and green light.'],
```
L69 (Tosini 1997), L70 (Romero and de Souza 2025: geckos and teiids lack it; the Six-lined Racerunner is a teiid in the Alachua list), L71 to L73 (opposed responses to short and long wavelengths), L74 (Foà and colleagues 2009), L76 (fence lizards without it choose warmer temperatures), L27.

```
['x', 'Tongue', 'Skinks, racerunners and glass lizards flick their tongues often to pick up scent, and they find hidden prey this way. Lizards that hunt from ambush, such as fence lizards and agamas, flick their tongues much less and hunt by sight. A camera records no scent.'],
```
L93, L94 (Baeckens and colleagues 2016), L95 (Cooper 1989: a spiny lizard and an agamid), L97 (Little Brown Skink).

```
['g', 'Field of view', 'A lizard’s eyes face almost straight out to the sides, and each takes in about 170 degrees. The two views overlap by only about 18 degrees in front, so a lizard sees about 320 degrees around itself. This view bends the picture at its edges to fit that sweep.'],
```
L204 (Land and Nilsson 2012, Fig. 5.14: a lizard's eye axis at 85 degrees and a binocular overlap of 18 degrees; the species is not named), L202. The total is my arithmetic: 2 × 170 − 18 = 322.

```
['i', 'Pupil', 'Slit pupils are common in lizards and snakes, but no source we opened covers the commonest day lizards, so the round pupil here is a guess.'],
```
L207 (slits are "more commonly vertical, as in many lizards, snakes, and mammals").

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Lizard', 'a lizard' | The app's wording. |
| `fov` | 320 | L202, L204. |
| `cpd` | 10 | From the anole fovea (L175); **invented** for other lizards. |
| `topoA`, `topoS`, `fall` | 1, .4, 2.0 | L182 to L184; values **invented**. |
| `pupil` | 'o' | **invented**. |
| `sat`, `sheen` | 1.1, .6 | L51 to L55, L68; amounts **invented**. |
| `third` (new) | a top strip in light-only mode | L71 to L74. |
| `cue` | 'The centre is sharp, colours run deeper with a violet tint, and a glow at the top shows what the third eye senses.' | The app's wording. |

**New effect: the third eye.** A strip along the top of the screen shows no image at all, only a soft glow whose colour is the ratio of blue to green light averaged over the top third of the camera picture, changing slowly (over several seconds). It uses the engine's light-only mode (`field: 1`) in one region. The behaviour of the cells is measured (L71 to L73); the strip's form and timing are **invented**. Medium work once regions with their own settings exist. It could be drawn as a faint, slowly breathing band, like dawn light on a ceiling.

### 2.6 `anole` (Dactyloidae): new

```
['m', 'Two sharp spots', 'Anoles have two sharp spots in each eye: a deep fovea in the middle of the retina, which looks out to the side, and a shallower one toward the back of the eye, which looks forward where the two eyes’ views overlap. This view sharpens the centre of the picture and two spots out to the left and right, and blurs the rest.'],
```
L58 (Green Anole), L59 (fourteen anoles: the central fovea is the deeper and denser). The directions each fovea faces are my reading of the eye's optics (the back, or temporal, retina sees forward); no source states the visual axes, and the question is listed in section 8.

```
['m', 'Sharpness', 'Away from its sharp spots, a brown anole sees about a fiftieth as much detail as a person. Its central fovea sees about ten times more sharply, about a fifth as well as a person. This view is blurred to match.'],
```
L174 (Brown Anole, 1.21 cycles per degree), L175 (Green Anole fovea, ten times greater).

```
['m', 'Colour and ultraviolet', 'Anoles have four kinds of colour-sensing cells, spread from ultraviolet to red light, where people have three. In tests they found a coloured patch against its background using all four, ultraviolet included. This view deepens colours and adds a violet tint for ultraviolet.'],
```
L51 to L54, L56, L57 (Green Anole pigments and its reach into deep red), L60 (Fleishman and Persons 2001).

```
['g', 'Throat fans', 'A male anole signals by opening a colourful throat fan, the dewlap, and in some species the fan reflects ultraviolet strongly where its background reflects little. A brown anole can see the pattern on a fan from about a metre away with its fovea, and only from closer than half a metre with the rest of the eye.'],
```
L197 (Leal and Fleishman 2002), L176 (Fleishman and colleagues 2017).

```
['g', 'Sudden movement', 'Anoles notice a small, sudden jump in position, about a third of a degree in less than a tenth of a second, more readily than the other kinds of motion tested. Their eyes grow used to leaves swaying in the wind. This view flashes whatever jumps suddenly and lets steady swaying fade.'],
```
L61 (Fleishman and Pallus 2010, from a motion-detector model that matches anole behaviour), L62 (Fleishman 1992).

```
['m', 'Third eye', 'Green anoles have a small third eye on top of the head that sends bursts of nerve signals when light comes on or goes off, and it forms no picture. This view shows a glow at the top of the screen that brightens and dims with the light.'],
```
L75 (Miller and Wolbarsht 1962), L70.

```
['x', 'Sight first', 'Anoles hunt by sight. Green anoles in a test ignored swabs carrying the smell of crickets, though male brown anoles noticed where females had been and flicked their tongues there a little more. A camera records no scent.'],
```
L95, L96.

```
['g', 'Field of view', 'A lizard’s eyes face almost straight out to the sides, each taking in about 170 degrees, and the two views overlap by about 18 degrees in front. No one has measured an anole’s field. This view follows the measured lizard, bending the picture at its edges to fit about 320 degrees.'],
```
L204, L202. The lizard in L204 is not named.

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Anole', 'an anole' | The app's wording. |
| `fov` | 320 | L202, L204. |
| `cpd` | 12 | L175. |
| `topoA`, `fall` | 1, 3.0 | Peak 12 falling to about 1.2 (L174); the fall value that gives a tenfold drop is **invented** for the engine. |
| `spots` (new) | two lateral sharp spots at ±90 degrees of azimuth, with the centre spot at half their sharpness | L58, L59 (the central fovea is denser than the temporal); positions are my optics reading; the half is **invented**. |
| `pupil` | 'o' | **invented**. |
| `sat`, `sheen` | 1.15, .7 | L54, L56, L60, L197; amounts **invented**. |
| `jump` (new) | flash on abrupt displacement, habituation to steady oscillation | L61, L62. |
| `third` (new) | as in `lizard` | L75. |
| `cue` | 'Three sharp spots, ahead and to each side. Sudden jumps flash, and swaying leaves fade.' | The app's wording. |

**New effects.**

- **Two foveae.** With a 320-degree field squeezed into the screen, the lateral spots land a little more than halfway from the centre to each edge (90 of 160 degrees). This needs the engine's regions with their own sharpness. Easy once regions exist.
- **Sudden jumps.** A temporal filter on the motion map that answers to onsets: displacement that starts within about 100 ms makes a brief bright flash, and motion that keeps repeating at the same place (leaves in wind) is divided down over a few seconds of adaptation (L61, L62). Medium work. It would look like the world going quiet around you until something twitches.

### 2.7 `gecko` (nocturnal geckos): new

```
['g', 'Colour by moonlight', 'Nocturnal geckos see colour in light as dim as faint moonlight, where people see only shades of grey. A helmet gecko told blue from grey by colour alone at that level. This view keeps colours in dim light.'],
```
L63 (Roth and Kelber 2004: 0.002 cd/m²), L194 (people become colour-blind between 0.01 and 0.001 cd/m²), L136.

```
['m', 'No red', 'Geckos have no rods, the cells most animals use in dim light, and see with three kinds of cones, for ultraviolet, blue and green light. The Mediterranean house gecko, common in Alachua County, is one of those measured. With no cells for red, red things look darker to a gecko, and this view darkens reds and shows ultraviolet as blue.'],
```
L63 (no rods, three cone types), L66 (Loew and colleagues 1996: *Hemidactylus turcicus* and *H. garnotii*, ultraviolet cones at 363 to 366 nm among green- and blue-sensitive cells).

```
['g', 'Sensitive eyes', 'A helmet gecko’s eye is about 350 times more sensitive than a person’s colour vision at the dimmest light where each can still see colour, thanks to its large cones and its optics. This view brightens dim scenes strongly.'],
```
L64 (Roth and colleagues 2009).

```
['g', 'Pupil', 'A gecko’s pupil opens wide in the dark and closes in bright light to a vertical slit whose notched edges meet, leaving a row of tiny holes, four in the helmet gecko. The closed pupil lets in several hundred to a thousand times less light than the open one, where a person’s pupil changes the light only about tenfold. This view uses a vertical slit.'],
```
L170 (Banks and colleagues 2015: area changes about 300-fold, a cat's 135-fold), L205, L206 (Land and Nilsson 2012: the notches line up into pinholes; more than a thousand-fold), L214 (Renero-Carrillo 2014: four small pupils in the helmet gecko), L215 (Underwood 1951: most geckos have vertical slits, many with lobed margins), L195.

```
['i', 'Copies', 'Each of the four holes in a helmet gecko’s closed pupil should form its own image, so anything out of focus would appear as a short vertical row of four overlapping copies. No study we opened has tested what a gecko makes of them. This view shows out-of-focus things that way in bright light.'],
```
L214, L205. The copies are my working of the optics: an out-of-focus point is drawn in the shape of the pupil, here four dots in a row.

```
['g', 'Rings of focus', 'A helmet gecko’s eye has rings of different focusing power, about the spread needed to bring all the colours it sees to a focus at once. A day gecko’s eye has a single focus. A slit keeps all the rings in use when the pupil closes, and among land vertebrates surveyed, slit pupils were found only in eyes with such rings.'],
```
L65 (Roth and colleagues 2009), L216, L217 (Malmström and Kröger 2006).

```
['g', 'Slow at night', 'To see colour in near darkness, nocturnal geckos give up some sharpness and speed. In a test of flickering light in 1939, a dwarf gecko stopped seeing flicker at lower rates than the other animals then measured. This view leaves trails behind things that move in dim light.'],
```
L136 (Kelber 2010), L220 (Crozier and Wolf 1939, *Sphaerodactylus*; the abstract gives no figure).

```
['i', 'Field and sharpness', 'No one has measured how wide a house gecko’s view is or how much detail it sees. The field here follows a measured lizard, about 320 degrees, and the sharpness is a guess.'],
```
L204, L202 for the field; L198 gives a fovea in gekkonids and no acuity.

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Gecko', 'a gecko' | The app's wording. |
| `fov` | 320 | L202, L204. |
| `cpd` | 4 | **invented**. |
| `topoA`, `fall` | .6, 1.0 | L198; values **invented**. |
| `pupil` | 'v' | L170. |
| `M`, `uvBlue` | `BEE`, 1 | Ultraviolet, blue and green cones (L66): the bee view's convention of moving colours over by one, which the app has already chosen for a UV-blue-green eye. |
| `gain` | 2.5 | Direction from L64; amount **invented**. |
| `persist` | .2 in dim light, 0 in bright | L136; amounts **invented**. |
| `copies` (new) | 4 vertical copies of out-of-focus areas when the scene is bright | L214, L205; the drawing is **invented** optics. |
| `cue` | 'Colours stay as the light fades, reds go dark, and in bright light things out of focus split into a row of copies.' | The app's wording. |

**New effect: pinhole copies.** In bright scenes, the depth-of-field blur is replaced by four faint copies stacked vertically, their spacing growing with the guessed distance from focus. Medium work (four offset samples in the blur pass). As the scene darkens toward dusk, the copies merge into one blur, as the pupil opens.

### 2.8 `frog` (Anura): revised

```
['m', 'Movement', 'Frogs and toads strike most readily at small things that move. They still see what keeps still: toads strike at still prey dummies, and frogs steer around still obstacles. A toad’s prey-detecting nerve cells go quiet when the whole background moves with the prey, as it does when the toad turns. This view shows moving things at full strength, dims still ones, and dims both while your phone is turning.'],
```
L123 (Honigmann 1944), L118 (Roth and Wiggers 1983), L119 (Ingle 1973), L120 (Lock and Collett 1980), L122 (Tsai and Ewert 1988), L219 (Recktenwald and colleagues 2017: a part of the leopard frog's thalamus appears to process the still surroundings), L163 (Lettvin and colleagues 1959, the source of the current row).

```
['i', 'Fading', 'A sitting bullfrog keeps its eyes almost perfectly still as it breathes, raising them only about six hundredths of a millimetre with each breath. In people, an image held that still on the eye fades within a few seconds, leaving only what moves, though no one has tested whether a frog’s still world fades. This view lets still things fade slowly while you hold the phone steady.'],
```
L218 (Witzmann and colleagues 2019, American Bullfrogs filmed by X-ray), L211 (Land and Nilsson 2012, p. 231, people), L212 (the same authors' suggestion that toads and snakes may see only movement when they keep still, which they call an idea).

```
['g', 'Speed', 'Amphibians that have been tested stop seeing flicker at about 20 flashes a second on average, and the cane toad at about 7, much slower than people. In dim light a frog’s rods may gather light for as long as three seconds. This view leaves trails behind anything that moves.'],
```
L137, L138 (Inger and colleagues 2014), L129 (Yovanovich and colleagues 2017, citing earlier work).

```
['g', 'Sharpness', 'Leopard frogs see about a twentieth as much detail as people do, judged by the finest stripes that still set off a prey-catching jump. This view is blurred to match.'],
```
L114 (2.8 cycles per degree; 60 / 2.8 = 21), L115, L116.

```
['m', 'Night colour', 'Frogs and toads have two kinds of rods, the cells for dim light, where people have one. Frogs jumping toward a light told blue from green at the very limit of their vision, and toads still used colour to choose prey on a clear night lit only by stars. This view keeps colours as the light fades.'],
```
L126, L127, L128 (Yovanovich and colleagues 2017, common frog and common toad), L130 (Green Treefrog), L194.

```
['m', 'Looming', 'A bullfrog leaps away when an approaching object grows to fill about 20 degrees of its view, whatever the object’s speed. This view flashes when something swells quickly toward the camera.'],
```
L124 (Yamamoto and colleagues 2003).

```
['g', 'Escape toward blue', 'A startled frog leaps toward the light, and it chooses blue light over other colours, even over a brighter mix of blue and green.'],
```
L131 (Muntz 1963).

```
['g', 'Depth', 'A toad judges how far away prey is with both eyes, and with one eye it focuses on the prey to gauge the distance. Toads plan their path around a fence before they set off and judge a gap by its real width. This view brings the place you tap into focus.'],
```
L121 (Jordan and colleagues 1980), L120.

```
['g', 'Pupil', 'True toads have pupils shaped like horizontal ovals, and every frog in a large survey that is active by day had an elongated pupil. A horizontal pupil smears out-of-focus things sideways, and this view does the same.'],
```
L192 (Thomas and colleagues 2021).

```
['x', 'Hearing', 'Frogs hear with two organs in each inner ear, one for low sounds up to about 1,000 vibrations a second and one for higher sounds, and most species hear best at the pitches of their own calls. The green treefrog hears most keenly near 900 and 3,000 vibrations a second, the two main pitches of the male’s call. A camera records no sound.'],
```
L133 (Goutte and colleagues 2017), L185, L186 (Moss and Simmons 1986; Simmons 1988). L134 records two Brazilian toadlets that cannot hear their own calls.

```
['g', 'Field of view', 'In most amphibians the eyes face out to the sides, each taking in about 170 degrees, and the two views overlap by a few tens of degrees in front. No frog’s field was measured in the sources we opened. This view follows the general rule, bending the picture at its edges to fit about 310 degrees.'],
```
L202, L203. Fite (1973), on the wanted list, measured frogs and toads.

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `fov` | 310 (was 340) | L202, L203; the overlap of 30 is **invented**. |
| `cpd` | 2.8 | L114 (was 4, graded a guess). |
| `topoS`, `fall` | .4, .6 | A treefrog's streak (L117); values **invented**. |
| `pupil` | 'h' | L192 (was a guess). |
| `persist` | .15 | L137, L138, L129 (unchanged). |
| `gate` | a fade (was 1): still parts dim from full strength to .4 over about 3 seconds while the phone is held still, and recover when it moves | Still things are seen (L118 to L120, L123, L219); a still image fades over seconds in people (L211); the bullfrog's eyes stay still (L218); the floor of .4 and the 3 seconds are **invented**. |
| `gain` | 1.6 | Direction from L125, L127; amount **invented**. |
| `dof` | 12 | L121; strength **invented**. |
| `selfmask` (new) | gate lifts toward dimming everything while the gyroscope reports turning | L122. |
| `loom` (new) | flash when a region expands past 20 degrees quickly | L124. |
| `cue` | 'Moving things stand out, still ones fade, and anything that swells toward you flashes.' | The app's wording. |

**New effects.**

- **Fading while still.** A running average of the picture is built while the gyroscope reports the phone still, and the parts that match it are dimmed toward .4 with a time constant of about 3 seconds; any turn of the phone resets the average (L211, L218). Easy.
- **Self-motion masking.** While the gyroscope reports the phone turning faster than a few degrees a second, the motion highlight is suppressed, as moving backgrounds mask a toad's prey cells (L122). Easy.
- **Looming flash.** The motion map's divergence (expansion) is summed over regions; when a region grows past about 20 degrees of the animal's field quickly, the whole picture flashes once and briefly drops in brightness (L124). Medium work.
- **The chorus.** With microphone permission, sound energy in the bands of the frog's two hearing organs (below about 1,000 and above about 1,000 vibrations a second; L133) gently pulses the brightness of the picture's lower half. For a recognized Green Treefrog the bands narrow to about 900 and 3,000 (L185, L186), so its own species' calls make the picture throb and other sounds barely do. The microphone stands in for the ear, and the drawing is **invented**. Medium work (the Web Audio API's AnalyserNode). At a pond at night, a chorus would set the whole lower half pulsing.

### 2.9 `salamander` (Caudata): new, building on `docs/views/sheets/salamander.md`

The earlier sheet's rows are kept where I could reopen their sources. Two of its numbers are now measured: sharpness (it had 4, invented) and the response to still things (it had a guess).

```
['m', 'Ultraviolet', 'Tiger salamanders and newts have colour-sensing cells tuned to ultraviolet light, which is invisible to you, near 356 nanometres in the tiger salamander and 340 to 359 in three newts.'],
```
L144 (Ma and colleagues 2001), L145 (Isayama and colleagues 2014), L146 (Korenyak and Govardovskii 2013). The earlier sheet's "40 of 58 species" (Mège and colleagues) could not be reopened and is left out.

```
['m', 'Hunting by ultraviolet', 'Smooth newt larvae catch more water fleas when ultraviolet light is present, and larvae raised without it catch fewer.'],
```
L148 (Martin and colleagues 2016).

```
['m', 'Colour', 'Adult fire salamanders snapped at a coloured worm dummy moving across a differently coloured background of equal brightness, so they tell colours apart by hue. Their three kinds of colour-sensing cells peak near 450, 500 and 570 nanometres. This view leaves colours as your camera shows them.'],
```
L159 (Przyrembel and colleagues 1995), L143 (fire salamander larvae see two colour dimensions), L147 (newt red cones at 593 to 611 nm).

```
['m', 'Sharpness', 'An eastern newt sees about a thirtieth to a fortieth as much detail as a person, and no part of its retina is sharper than the rest. This view is blurred evenly to match.'],
```
L140, L141 (Pushchin and Karetin 2009: 1.4 to 1.95 cycles per degree; 60 / 1.95 = 31, 60 / 1.4 = 43), L142 (no fovea in seven lungless salamanders).

```
['m', 'Still things', 'Red-backed salamanders find and eat prey that does not move, guided by its smell, and fire salamanders snap at still shapes once they have seen something move. This view keeps still things in the picture.'],
```
L149 (David and Jaeger 1981, Eastern Red-backed Salamander), L161 (Himstedt and colleagues 1978).

```
['m', 'Distance', 'A fire salamander refocuses its eyes on prey before it turns to strike, and judges distance that way. Lungless salamanders that shoot out their tongues have eyes set forward, and the two eyes’ views line up at the tongue’s farthest reach. This view brings the place you tap into focus.'],
```
L187 (Werner and Himstedt 1984), L158 (Wiggers and colleagues 1995).

```
['m', 'Slow in the dark', 'A salamander’s rods pass on slow changes in light, between about one and a half and four a second, more readily than fast ones. This view leaves trails when the light is dim.'],
```
L156 (Armstrong-Gold and Rieke 2003, tiger salamander).

```
['x', 'Smell', 'Lungless salamanders tap their snouts on the ground, and a groove running from each nostril to the lip draws odours up to the nose. They follow smells to food and away from danger, and a camera records no smell.'],
```
L188 (Zug 2020), L149.

```
['x', 'Moving water and electricity', 'Salamanders that live in water have a lateral line, rows of small sense organs that feel movement in the water around them. Some also have organs for weak electric fields, and amphiumas, among the salamanders most recorded in Alachua County, react to weak electric currents. A camera records none of this.'],
```
L155 (Tovar and colleagues 2025), L154 (Fritzsch 1981), L189 (Keathley and Moon 2021, a meeting abstract).

```
['x', 'Magnetic compass', 'The eastern newt has a magnetic compass that works through light-sensitive cells in or near the pineal organ, at the top of the brain. Light of different colours changes the direction it chooses, and a camera records none of this.'],
```
L150 (Phillips and colleagues 2001). L151 (Rough-skinned Newts steer by sun and moon even with their eyes removed).

```
['i', 'Ultraviolet tint, field and pupil', 'A phone captures little ultraviolet light, so the violet tint here stands in for it. Most amphibians have eyes facing the sides that see about 310 degrees around them, but lungless salamanders that shoot out their tongues have eyes set forward, so the field here is a guess between the two. The pupil shape is a guess too.'],
```
L202, L203 (the general rule), L158 (forward-set eyes in tongue-shooting lungless salamanders). No source for the tint or the pupil.

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Salamander, newt', 'a salamander or newt' | As in `GROUPS`. |
| `fov` | 280 (was 260 in the earlier sheet) | **invented**, between the side-facing amphibian rule (about 310; L202, L203) and the forward-set eyes of tongue-shooting salamanders (L158). |
| `cpd` | 1.7 | L140 (was 4, invented). |
| `topoA`, `topoS`, `fall` | unset | L141, L142. |
| `pupil` | 'o' | **invented**. |
| `sheen` | .6 | L144 to L146, L148; strength **invented**. |
| `M`, `uvBlue` | unset | L159, L160 (the fire salamander's ultraviolet sensitivity runs through its 500 nm receptor). |
| `dof` | 12 | L187; strength **invented**. |
| `gate` | unset | L149, L161. |
| `persist` | .3 when the scene is dark, 0 when bright | L156; amounts **invented**. |
| `cue` | 'Still things stay in view. Tap what you would catch to bring it into focus.' | The app's wording. |

**New effects.** Persistence that grows as the camera's average brightness falls (L156), shared with `gecko`. Easy. The magnetic compass line and the lateral-line ripples proposed in the earlier sheet stand as written there.

## 3. The existing views re-checked

### `alligator`

| Field or row today | Check | Source |
|---|---|---|
| `fov` 280 | corrected to 310 from the general rule for reptiles and amphibians (g); nothing measured in crocodilians | L202, L203 |
| `cpd` 9 | confirmed in size, corrected in grade: 8.0 to 8.8 in two crocodiles (g) | L7, L8 |
| `topoS` 1 | confirmed (g) | L9 |
| `fall` 2.6 | unsupported | none |
| `pupil` 'v' | confirmed as a group statement (g); `docs/SOURCES.md` said no source named crocodilians | L169, L171, L195 |
| `dof` 24 | invented strength | none |
| `gain` 1.6 | direction supported (g); amount invented | L5, L18, L19 |
| `sat` .9 | unsupported; set to 1 | L1 to L3 |
| Row 'Sharpest spot' (g) | first sentence confirmed; the second ("It lets them scan the waterline without turning their heads") is not in the source and is cut | L9 |
| Row 'Colour' (g) | corrected: the alligator itself was measured (Sillman and colleagues 1991), with four cone pigments of which three sit in single and principal double cones near 444, 535 and 566 nm, and no ultraviolet cone; regraded m | L1 to L6, L21 |
| Row 'Pupil' (g) | confirmed (g), now sourced | L169, L171 |
| Row 'Field of view, sharpness, dim light and depth' (i) | sharpness and dim light now have sources; the field now follows a group rule (g), and depth remains a guess | L7, L8, L5, L18, L19, L202, L203 |
| `docs/SOURCES.md`: Nagloo 2016 via *Science News* | confirmed from the primary abstract | L7 to L14 |

### `reptile`

| Field or row today | Check | Source |
|---|---|---|
| `fov` 280 | too narrow: a colubrid was measured at 308.5, a lizard's 18-degree overlap gives about 320, and the general rule for reptiles about 310 | L85, L202 to L204 |
| `cpd` 15 | corrected per group: snakes about 2.5, turtles about 7, anole fovea about 12 and periphery about 1.2 | L87, L88, L90, L177, L174, L175 |
| `topoA` 1, `fall` 1.2 | corrected: turtles and crocodilians have streaks; anoles two foveae; many lizards a central fovea that, in eyes on the sides of the head, looks sideways | L112, L59, L184 |
| `pupil` 'o' | corrected for geckos, pit vipers and boas (vertical slits) | L170, L172, L205, L207, L214, L215 |
| `sheen` .6 | supported as a stand-in: ultraviolet cones measured in anoles, turtles, geckos, pythons and boas | L54, L103, L66, L77, L79 |
| Row 'The whole view' (i) | "eyes on the sides of the head": supported for skinks (L184); "one sharp spot straight ahead": wrong for most groups; "the ability to see ultraviolet": confirmed | as above |
| `docs/SOURCES.md` "entered from memory: ultraviolet vision in lizards and turtles" | confirmed | L54, L56, L103, L109 |

### `frog`

| Field or row today | Check | Source |
|---|---|---|
| `fov` 340 | corrected to 310 from the general rule for amphibians (g); no frog measurement opened | L202, L203 |
| `cpd` 4 | corrected to 2.8 (g); 4.3 by an older eye-movement test | L114, L115, L116 |
| `pupil` 'h' | confirmed for toads and day-active frogs (g) | L192 |
| `persist` .15 | supported (g) | L137, L138, L129 |
| `gate` 1 | corrected: frogs and toads see still things; set to a slow, partial fade while the phone is held still | L118 to L120, L123, L211, L218, L219 |
| Row 'Movement' (m) | corrected: "takes little notice of the parts of its world that stay still, and it can starve beside food that never moves" comes from the introduction of Lettvin and colleagues (1959), read here as quoted in lecture notes; it is a remark, and later experiments show stationary vision | L163, L118 to L123 |
| Row 'Speed' (g) | confirmed: 6.7 Hz for the cane toad (Inger and colleagues 2014), which is rare in Alachua (one record); the amphibian mean is 19.2 Hz | L137, L138 |
| Row 'Field of view, sharpness and pupil' (i) | sharpness and pupil now sourced; the field now follows a group rule (g) | L114, L192, L202, L203 |
| `docs/SOURCES.md`: Lettvin via NYU lecture notes | the notes carry the quotation the row rests on; the paper itself did not render here, so the wording is checked against the notes alone, and the claim is the authors' remark | L163 |

## 4. Species with their own measurements

These are commonly photographed species measured well enough for a profile of their own later.

| Species | Records (world; Alachua) | What is measured | Log lines |
|---|---|---|---|
| American Alligator | 2,781 in Alachua | cone and rod pigments, fast rod dark adaptation, hearing in air and water, face domes, extraretinal light sense | L1 to L6, L17, L18, L20, L164 to L168 |
| Pond Slider | 172,017; 425 | four cone pigments, seven cone types with oil droplets, ultraviolet opponency, acuity 4.4 to 9.9, streak, response times, pupil, independent eye movements, hearing | L100 to L105, L107 to L109, L112, L173, L177, L180, L191 |
| Brown Anole | 109,010; 2,194 | peripheral acuity, dewlap-pattern distances, chemical sense | L174, L176, L96 |
| Green Anole | 110,190; 1,316 | pigments in vitro, ultraviolet cone, two foveae with foveal rod opsin, foveal acuity, parietal eye, no prey-odour use | L54, L56 to L58, L75, L95, L175 |
| Mediterranean House Gecko | 172 in Alachua | ultraviolet, blue and green cones | L66 |
| Common Garter Snake | 144,689; 80 | movement and odour in prey attack; vomeronasal shelter and aggregation | L98, L99 |
| Ball Python | 2 in Alachua | cone pigments, optokinetic acuity, hearing by skull vibration | L77, L78, L82, L190 |
| Western Rattlesnake | (not resolved) | heat-picture resolution, vomeronasal trailing, squirrels' heat signal | L28, L29, L38, L41 |
| Green Treefrog | 895 in Alachua | two rod types, hearing tuned to 900 and 3,000 Hz | L130, L185, L186 |
| American Bullfrog | 101,114; 185 | looming threshold, eyes held still while breathing | L124, L218 |
| Common Toad and Common Frog | 77,425 and 64,712 | still-prey strikes, low-light snapping, depth by accommodation, rod-based colour at threshold, blue phototaxis | L118, L121, L122, L125 to L127, L131 |
| Eastern Newt | 61,966; 30 | acuity, retinal topography, magnetic compass | L140, L141, L150 |
| Eastern Red-backed Salamander | 74,121 | feeding on still prey by smell | L149 |

## 5. Gaps and how to fill them

- **Field of view** for crocodilians, turtles, anoles, geckos, frogs and salamanders: no measurement in the group itself was opened. The values here use the textbook rule of about 170 degrees per eye with a few tens of degrees of overlap (L202, L203), a lizard's 18-degree overlap (L204), and a colubrid's measured 308.5 degrees (L85), which the rule matches to within 2 degrees. A value for each group could be inferred from orbit orientation in skull scans with a lens model, as done for that snake (L85); Cerio and Witmer (2023, crocodylian eye position, title in the collection) is a start for crocodilians. For frogs, Fite (1973) is wanted.
- **Flicker fusion** for crocodilians, lizards, geckos and salamanders: none opened. Nearest: the reptile mean of 43 Hz (L139); turtle cone response times (L107); the salamander rod synapse's 1.5 to 4 Hz passband in the dark (L156); Jenssen and Swenson (1974) for anoles and Crozier and Wolf (1939) for a gecko are in the collection without numbers.
- **Acuity of non-anole lizards and of geckos**: none opened. The anole fovea is the nearest relative (L175); New and Bull (2011) for a skink and Röll (2001) for geckos are wanted.
- **Snake hearing in colubrids**: nothing opened; the python's 80 to 160 Hz (L190) is the nearest.
- **Crocodilian flicker, field and colour behaviour**: nothing known; the pigments are measured (L1 to L6).
- **Whether a frog's still world fades**: measured only in people (L211); the bullfrog's still eyes (L218) make it possible. Leopard frogs, by the title of Skorina and colleagues (2011), move their heads and not their eyes; no abstract could be opened.
- **The heat sense in a picture**: the coarse resolution is measured (L28); how a snake perceives a still warm animal over seconds is not. Bakken and Krochmal (2007) is wanted for the pit's field of view.
- **Directions of the anole foveae**: no source gives the visual axes; inferred from optics in 2.6.
- **The worm lizard's eyes**: no source opened; sent to `other` on its habits alone.
- **Aquatic salamanders' vision** (amphiumas and sirens, a third of Alachua's salamander records): nothing opened on their eyes. Nearest: the newt and tiger salamander measurements, with the lateral line and electric sense as `x` rows.
- **Pinhole copies in geckos**: the four holes are measured in the helmet gecko (L214); the copies are my own working of the optics (2.7), and what a gecko makes of them is untested.

## 6. Closed sources wanted

The same list as `docs/views/wanted/herps.jsonl`, most useful first. Priority 1 would change a view's picture, 2 would confirm or correct a row, and 3 is background.

1. (Priority 1) Fite KV (1973). The visual fields of the frog and toad: a comparative study. *Behavioral Biology*. doi:10.1016/s0091-6773(73)80131-2. It would replace the frog view's field of view and binocular overlap, now set from a general rule for amphibians, with measured frogs and toads.
2. (Priority 1) Brown KT (1969). A linear area centralis extending across the turtle retina and stabilized to the horizon by non-visual cues. *Vision Research*. doi:10.1016/0042-6989(69)90047-9. It would show whether the turtle's sharp band should stay level with the horizon as the phone tilts.
3. (Priority 1) Bakken GS, Krochmal AR (2007). The imaging properties and sensitivity of the facial pits of pitvipers as determined by optical and heat-transfer analysis. *Journal of Experimental Biology*. doi:10.1242/jeb.006965. It would give the pit organ's field of view and optical blur, which set the size and softness of the heat glow.
4. (Priority 1) Jenssen TA, Swenson B (1974). An ecological correlate of critical flicker-fusion frequencies for some *Anolis* lizards. *Vision Research*. doi:10.1016/0042-6989(74)90164-3. It would give anole flicker fusion, which sets the anole view's pace and is the nearest value for other lizards.
5. (Priority 1) Manteuffel G, Himstedt W (1978). The aerial and aquatic visual acuity of the optomotor response in the crested newt (*Triturus cristatus*). *Journal of Comparative Physiology A*. doi:10.1007/bf00657609. It would give a newt's acuity by behaviour in air and in water, which sets the salamander view's sharpness.
6. (Priority 1) Röll B (2001). Gecko vision: retinal organization, foveae and implications for binocular vision. *Vision Research*. doi:10.1016/s0042-6989(01)00093-1. It would give gecko foveae and acuity, which the gecko view now borrows from anoles.
7. (Priority 1) New STD, Bull CM (2011). Retinal ganglion cell topography and visual acuity of the sleepy lizard (*Tiliqua rugosa*). *Journal of Comparative Physiology A*. doi:10.1007/s00359-011-0635-8. It would give a skink's acuity and retinal topography for the lizard view's sharpness and sharp spot.
8. (Priority 2) Heath JE, Northcutt RG, Barber RP (1969). Rotational optokinesis in reptiles and its bearing on pupillary shape. *Journal of Comparative Physiology A*. doi:10.1007/bf00298043. It would check the slit and round pupils in the alligator, gecko, pitviper and lizard views against measured eye movements.
9. (Priority 2) Martinez PS, Plummer CE (2022). Ophthalmology of Crocodilia: alligators, crocodiles, caimans, and gharials. Springer eBooks (book chapter). doi:10.1007/978-3-030-71302-7_15. It would check the crocodilian pupil, tapetum and field-of-view rows against a veterinary review.
10. (Priority 2) Arnold K, Neumeyer C (1987). Wavelength discrimination in the turtle *Pseudemys scripta elegans*. *Vision Research*. doi:10.1016/0042-6989(87)90159-3. It would confirm by behaviour the four-cone colour vision that the turtle view's colour rows rest on.
11. (Priority 2) Aho A-C (1996). The visual acuity of the frog (*Rana pipiens*). *Journal of Comparative Physiology A*. doi:10.1007/s003590050023. It would give the full method and conditions behind the frog view's 2.8 cycles per degree, now taken from a conference abstract.
12. (Priority 2) Skorina LK, Kazaure HS, Gruberg ER (2011). Leopard frogs move their heads, but not their eyes: Implications for perception of stationary objects. *Neuroscience Letters*. doi:10.1016/j.neulet.2011.07.025. It would show whether leopard frogs hold their eyes still enough for a still scene to fade, which sets the strength and speed of the frog view's fading.
13. (Priority 2) Recktenwald EW, Skorina LK, Neeb CN, Dudkin EA, Gruberg ER (2014). Light and shadow: visual recognition of the stationary environment by leopard frogs. *Behavioural Processes*. doi:10.1016/j.beproc.2014.08.008. It would say what leopard frogs recognize in their still surroundings, which sets how much of a still scene the frog view keeps.
14. (Priority 2) Fleishman LJ (1986). Motion detection in the presence and absence of background motion in an *Anolis* lizard. *Journal of Comparative Physiology A*. doi:10.1007/bf00612043. It would set how strongly the anole view damps movement when the whole scene sways.
15. (Priority 2) Safer A, Grace MS (2004). Infrared imaging in vipers: differential responses of crotaline and viperine snakes to paired thermal targets. *Behavioural Brain Research*. doi:10.1016/j.bbr.2004.01.020. It would show whether true vipers without pits respond to heat, which decides whether they belong in the heat view.
16. (Priority 2) Grace MS, Woodward OM, Church DR, Calisch G (2001). Prey targeting by the infrared-imaging snake *Python molurus*: effects of experimental and congenital visual deprivation. *Behavioural Brain Research*. doi:10.1016/s0166-4328(00)00336-3. It would confirm that pythons can aim strikes by heat alone, which places pythons and boas in the heat view.
17. (Priority 3) Gracheva EO and colleagues (2010). Molecular basis of infrared detection by snakes. *Nature*. doi:10.1038/nature08943. It is the primary source for the heat-sensing channel of pit vipers, boas and pythons, open in PubMed Central, though every route to it returned a rate limit or a bot check.
18. (Priority 3) Hutchison VH, Kosh RJ (1974). Thermoregulatory function of the parietal eye in the lizard *Anolis carolinensis*. *Oecologia*. doi:10.1007/bf00345581. It would show how the parietal eye changes basking in anoles, which bears on the third-eye strip.
19. (Priority 3) Bartol S, Musick JA, Ochs AL (2002). Visual acuity thresholds of juvenile loggerhead sea turtles (*Caretta caretta*): an electrophysiological approach. *Journal of Comparative Physiology A*. doi:10.1007/s00359-001-0262-x. It would give a sea turtle's acuity for comparison with the pond slider's.
20. (Priority 3) Lindquist SB, Bachmann MD (1982). The role of visual and olfactory cues in the prey catching behavior of the tiger salamander, *Ambystoma tigrinum*. *Copeia*. doi:10.2307/1444271. It would weigh sight against smell in a salamander's strike, which sets the strength of the salamander view's movement gate.
21. (Priority 3) Placyk JS, Graves BM (2002). Prey detection by vomeronasal chemoreception in a plethodontid salamander. *Journal of Chemical Ecology*. doi:10.1023/a:1015213918739. It would support the salamander view's smell row with a measured vomeronasal response to prey.

## 7. Sources

Each source is listed once with its log lines. "opened" means I read the abstract or text this session; "secondary" names the source relied on.

- Alving WR, Kardong KV (1996), *Brain, Behavior and Evolution* 48(3): 165 to 172, doi:10.1159/000113195. Opened (abstract in the collection; year from Europe PMC). L41.
- Arden GB, Tansley K (1962), *Journal of General Physiology*, doi:10.1085/jgp.45.6.1145. Opened. L199.
- Ariel M (1990), *Visual Neuroscience*, doi:10.1017/s0952523800000055. Opened. L180.
- Armstrong-Gold CE, Rieke F (2003), *Journal of Neuroscience*, doi:10.1523/jneurosci.23-09-03796.2003. Opened. L156.
- Baeckens S, Van Damme R, Cooper WE (2016), *Journal of Evolutionary Biology*, doi:10.1111/jeb.13032. Opened. L94.
- Baeckens S, Driessens T, Van Damme R (2016), *PeerJ*, doi:10.7717/peerj.1874. Opened. L96.
- Banks MS, Sprague WW, Schmoll J, Parnell JAQ, Love GD (2015), *Science Advances* 1: e1500391, doi:10.1126/sciadv.1500391. Opened (accepted manuscript, Durham repository; the DOI as printed on the eScholarship copy). L169 to L171, L195.
- Barbour HR and colleagues (2002), *Journal of Comparative Neurology*, doi:10.1002/cne.10308. Opened. L182.
- Bartol S, Mellgren RL, Musick JA (2003), *International Journal of Comparative Psychology*, doi:10.46867/c4t601. Opened. L178.
- Baylor DA, Hodgkin AL (1973), *Journal of Physiology*, doi:10.1113/jphysiol.1973.sp010340. Opened. L107, L108.
- Biswas A, Ghosh A, Agashe M (2025), *Proceedings of the Royal Society B*, doi:10.1098/rspb.2025.0199. Opened (full text). L37, L48, L49, L196.
- Brischoux F, Pizzatto L, Shine R (2010), *Journal of Evolutionary Biology*, doi:10.1111/j.1420-9101.2010.02046.x. Opened. L172.
- Burghardt GM, Denny D (1983), *Zeitschrift für Tierpsychologie*, doi:10.1111/j.1439-0310.1983.tb02161.x. Opened. L98.
- Chen Q and colleagues (2012), *PLoS ONE*, doi:10.1371/journal.pone.0034989. Opened (full text). L32, L50.
- Chen Q and colleagues (2017), *Journal of Experimental Biology*, doi:10.1242/jeb.155382. Opened. L33.
- Christensen CB, Christensen-Dalsgaard J, Brandt C, Madsen P (2012), International Congress of Neuroethology, doi:10.3389/conf.fnbeh.2012.27.00110. Opened (conference abstract). L190.
- Christensen-Dalsgaard J, Brandt C, Willis K, Christensen C, Ketten D, Edds-Walton P, Fay R, Madsen P, Carr C (2012), *Proceedings of the Royal Society B* 279: 2816 to 2824. Opened (Curtin University repository abstract; no DOI on that page). L191.
- Clark RW, Bakken GS, Reed EJ, Soni A (2022), *Journal of Experimental Biology*, doi:10.1242/jeb.244478. Opened. L28, L29.
- Cooper WE (1989), *Copeia*, doi:10.2307/1445446. Opened. L95.
- Crozier WJ, Wolf E (1939), *Journal of General Physiology* 22(5): 555 to 566, doi:10.1085/jgp.22.5.555. Opened (abstract on the publisher's page). L220.
- David RS, Jaeger RG (1981), *Copeia*, doi:10.2307/1444234. Opened. L149.
- Davies WIL and colleagues (2009), *Journal of Neuroscience*, doi:10.1523/jneurosci.0517-09.2009. Opened. L77, L78.
- Emerling CA (2016), *Molecular Biology and Evolution* 34(3): 666, doi:10.1093/molbev/msw265. Opened. L15, L16.
- Engbretson GA, Hutchison VH (1976), *Journal of Experimental Zoology*, doi:10.1002/jez.1401980105. Opened. L76.
- Fite KV, Lister BC (indexed 2008; PubMed id 7326573), *Brain, Behavior and Evolution*, doi:10.1159/000121639. Opened. L59.
- Fleishman LJ (1992), *American Naturalist*, doi:10.1086/285304. Opened. L62.
- Fleishman LJ, Howland HC, Howland MJ, Rand AS, Davenport ML (1988), *Journal of Comparative Physiology A* 163: 441 to 443, doi:10.1007/bf00604898. Opened. L162.
- Fleishman LJ, Loew ER, Whiting MJ (2011), *Proceedings of the Royal Society B*, doi:10.1098/rspb.2011.0118. Opened. L68.
- Fleishman LJ, Pallus AC (2010), *Proceedings of the Royal Society B*, doi:10.1098/rspb.2010.0742. Opened. L61.
- Fleishman LJ, Persons M (2001), *Journal of Experimental Biology*, doi:10.1242/jeb.204.9.1559. Opened. L60.
- Fleishman LJ, Yeo AI, Perez CW (2017), *Journal of Experimental Biology*, doi:10.1242/jeb.150458. Opened. L174 to L176.
- Foà A and colleagues (2009), *Journal of Experimental Biology*, doi:10.1242/jeb.032987. Opened. L74.
- Fritzsch B (1981), *Zeitschrift für Naturforschung C*, doi:10.1515/znc-1981-5-628. Opened. L154.
- Gamble T, Greenbaum E, Jackman TR, Bauer AM (2015), *Biological Journal of the Linnean Society*, doi:10.1111/bij.12536. Opened. L67.
- Gioanni H, Bennis M, Sansonetti A (1993), *Visual Neuroscience*, doi:10.1017/s0952523800006167. Opened. L181.
- Gomez Z, Cameron DJ, Eng CL (2024), *Veterinary Ophthalmology*, doi:10.1111/vop.13259. Opened (full text). L82; secondary for L83 and L84 (its references 9 and 10).
- Goris RC (2011), *Journal of Herpetology*, doi:10.1670/10-238.1. Opened. L36.
- Goutte S and colleagues (2017), *Scientific Reports*, doi:10.1038/s41598-017-12145-5. Opened (full text). L133, L134.
- Gower DJ and colleagues (2019), *Biological Journal of the Linnean Society*, doi:10.1093/biolinnean/blz003. Opened. L40.
- Gower DJ and colleagues (2021), *Genome Biology and Evolution*, doi:10.1093/gbe/evab253. Opened. L200.
- Graf IR, Machta BB (2024), *PNAS*, doi:10.1073/pnas.2308215121. Opened (full text). L35; secondary for L47 (its reference 7).
- Granda AM and colleagues (1995), *Visual Neuroscience*, doi:10.1017/s0952523800006763. Opened. L173.
- Graves BM, Duvall D (1985), *Zeitschrift für Tierpsychologie*, doi:10.1111/j.1439-0310.1985.tb01385.x. Opened. L42.
- Guo J and colleagues (2023), *Proceedings of the Royal Society B*, doi:10.1098/rspb.2023.0530. Opened. L21.
- Hart NS, Lisney TJ, Collin SP (2006), *Journal of Experimental Biology*, doi:10.1242/jeb.02568. Opened. L113.
- Hartline PH, Kass L, Loop MS (1978), *Science*, doi:10.1126/science.628839. Opened. L30.
- Hauzman E and colleagues (2014), *Brain, Behavior and Evolution*, doi:10.1159/000365275. Opened. L90.
- Hauzman E and colleagues (2017), *BMC Evolutionary Biology*, doi:10.1186/s12862-017-1110-0. Opened. L92.
- Heller SB, Halpern M (1982), *Journal of Comparative and Physiological Psychology*, doi:10.1037//0735-7036.96.6.984. Opened. L99.
- Higgs DM and colleagues (2002), *Journal of Comparative Physiology A* 188: 217 to 223, doi:10.1007/s00359-002-0296-8. Opened (repository abstract). L167, L168.
- Himstedt W, Tempel P, Weiler J (1978), *Journal of Comparative Physiology* 124: 49 to 52, doi:10.1007/bf00656390. Opened (Springer summary). L161.
- Honigmann H (1944), *Proceedings of the Royal Society B*, doi:10.1098/rspb.1944.0019. Opened. L123.
- Inger R, Bennie J, Davies TW, Gaston KJ (2014), *PLoS ONE* 9(5): e98631, doi:10.1371/journal.pone.0098631. Opened (article page). L137 to L139.
- Ingle D (1973), *Science*, doi:10.1126/science.181.4104.1053. Opened. L119.
- Isayama T and colleagues (2014), *Journal of Comparative Neurology* 522(10), doi:10.1002/cne.23531. Opened. L145.
- Jordan M, Luthardt G, Meyer-Naujoks C, Roth G (1980), *Zeitschrift für Naturforschung C*, doi:10.1515/znc-1980-9-1036. Opened. L121.
- Kardong KV, Bels V (1998), *Journal of Experimental Biology*, doi:10.1242/jeb.201.6.837. Opened. L44.
- Kavaliers M (1980), *Photochemistry and Photobiology*, doi:10.1111/j.1751-1097.1980.tb03987.x. Opened. L20.
- Kawamura S, Yokoyama S (1998), *Vision Research*, doi:10.1016/s0042-6989(97)00160-0. Opened. L56, L57.
- Keathley CM, Moon BR (2021), SICB meeting abstract 96-5. Opened. L189.
- Kelber A (2010), *Journal of Vision*, doi:10.1167/10.15.3. Opened. L136, L194.
- King RB, Douglass JK, Phillips JB, Baube CL (1993), *Journal of Experimental Zoology*, doi:10.1002/jez.1402670107. Opened. L130.
- Korenyak DA, Govardovskii VI (2013), *Journal of Evolutionary Biochemistry and Physiology*, doi:10.1134/s0022093013040038. Opened. L146, L147.
- Land MF, Nilsson D-E (2012), *Animal Eyes*, 2nd edition, Oxford University Press, https://global.oup.com/academic/product/animal-eyes-9780199581146 (publisher's page opened for the contents). Opened (owner's copy, the whole book; every passage on reptiles and amphibians read, and Fig. 5.14 read from the rendered page). L22 to L27, L193, L202 to L213.
- Landreth HF, Ferguson DE (1967), *Science*, doi:10.1126/science.158.3807.1459. Opened. L151.
- Larsen LO, Pedersen JN (1981), *Amphibia-Reptilia*, doi:10.1163/156853882x00248. Opened. L125.
- Leal M, Fleishman LJ (2002), *Proceedings of the Royal Society B*, doi:10.1098/rspb.2001.1904. Opened. L197.
- Lettvin, Maturana, McCulloch and Pitts (1959), What the frog's eye tells the frog's brain. Secondary (quoted in D. Heeger's lecture notes, New York University, 2003; the paper itself did not render). L163.
- Levenson D, Eckert SA, Crognale MA, Deegan JF, Jacobs GH (2004), *Copeia*, doi:10.1643/cp-03-217r1. Opened. L201.
- Linke R, Roth G, Rottluff B (1986), *Journal of Morphology*, doi:10.1002/jmor.1051890204. Opened. L142.
- Lock A, Collett T (1980), *Proceedings of the Royal Society B*, doi:10.1098/rspb.1980.0009. Opened. L120.
- Loew ER, Fleishman LJ, Foster F, Provencio I (2002), Visual pigments and oil droplets in diurnal lizards, *Journal of Experimental Biology*, doi:10.1242/jeb.205.7.927. Opened (abstract; authors as the collection gives them). L51 to L55.
- Loew ER, Govardovskii VI (2001), *Visual Neuroscience*, doi:10.1017/s0952523801185081. Opened. L100 to L104.
- Loew ER, Govardovskii VI, Röhlich P, Szél A (1996), *Visual Neuroscience*, doi:10.1017/s0952523800007483. Opened. L66.
- Malmström T, Kröger R (2006), *Journal of Experimental Biology* 209(1): 18 to 25, doi:10.1242/jeb.01959. Opened (abstract on the Lund University repository record). L216, L217.
- Ma J-X and colleagues (2001), *Visual Neuroscience*, doi:10.1017/s0952523801183057. Opened. L144.
- Martin M and colleagues (2016), *Biology Letters*, doi:10.1098/rsbl.2015.0954. Opened. L148.
- McDevitt DS, Brahma SK, Jeanny J-C, Hicks D (1993), *Anatomical Record*, doi:10.1002/ar.1092370302. Opened. L58.
- Miller WH, Wolbarsht ML (1962), *Science*, doi:10.1126/science.135.3500.316. Opened. L75.
- Mitra AT and colleagues (2022), *Proceedings of the Royal Society B*, doi:10.1098/rspb.2022.0767. Opened. L135.
- Moiseenkova VY and colleagues (2003), *American Journal of Physiology*, doi:10.1152/ajpregu.00024.2002. Opened. L34.
- Moon C (2011), *Anatomy & Cell Biology*, doi:10.5115/acb.2011.44.1.8. Opened (full text). L45, L46.
- Moss CF, Simmons AM (1986), *Journal of Comparative Physiology A* 159(2): 257 to 266, doi:10.1007/bf00612308. Opened. L185.
- Muntz WRA (1963), *Journal of Experimental Biology*, doi:10.1242/jeb.40.2.371. Opened. L131.
- Nagloo N, Collin SP, Hemmi JM, Hart NS (2016), *Journal of Experimental Biology*, doi:10.1242/jeb.135673. Opened. L7 to L14.
- Nagloo N and colleagues (2019), *Journal of Comparative Neurology*, doi:10.1002/cne.24780. Opened. L183.
- Navarrete Méndez MJ and colleagues (2025), *Evolution*, doi:10.1093/evolut/qpaf190. Opened. L157.
- Newman EA, Hartline PH (1981), *Science*, doi:10.1126/science.7256281. Opened. L31.
- Nicoletto PF (1985), *Journal of Herpetology*, doi:10.2307/1564202. Opened. L97.
- Northmore DPM, Granda AM (1991), *Visual Neuroscience*, doi:10.1017/s0952523800010403. Opened. L177.
- Ohtsuka T (1985), *Science*, doi:10.1126/science.4023716. Opened. L105.
- Ohtsuka T (1985), *Journal of Comparative Neurology*, doi:10.1002/cne.902370202. Opened. L106.
- Oliver LJ and colleagues (2000), *Marine and Freshwater Behaviour and Physiology*, doi:10.1080/10236240009387095. Opened. L179.
- Ollivier FJ and colleagues (2004), *Veterinary Ophthalmology*, doi:10.1111/j.1463-5224.2004.00318.x. Opened. L19.
- Peterson EH, Ulinski PS (1979), *Journal of Comparative Neurology*, doi:10.1002/cne.901860103. Opened. L112.
- Phillips JB, Deutschlander ME, Freake MJ, Borland SC (2001), *Journal of Experimental Biology*, doi:10.1242/jeb.204.14.2543. Opened. L150.
- Przyrembel C, Keller B, Neumeyer C (1995), *Journal of Comparative Physiology A* 176(4): 575 to 586, doi:10.1007/bf00196422. Opened. L159, L160.
- Pushchin II (2019), *Journal of Anatomy*, doi:10.1111/joa.13075. Opened. L116, L117.
- Pushchin II, Karetin YA (2009), *Journal of Comparative Neurology*, doi:10.1002/cne.22127. Opened. L140, L141.
- Recktenwald EW, Dudkin EA, Skorina LK, Saidel WM, Gruberg ER (2017), *Brain, Behavior and Evolution*, doi:10.1159/000481393. Opened. L219.
- Renero-Carrillo FJ (2014), Latin America Optics and Photonics Conference, doi:10.1364/laop.2014.lf1b.5. Opened (conference abstract). L214.
- Rocha FAF and colleagues (2008), *Visual Neuroscience*, doi:10.1017/s0952523808080516. Opened. L110.
- Röll B (2001), *Journal of Comparative Neurology*, doi:10.1002/cne.1082. Opened. L184, L198.
- Romero RD, de Souza FSJ (2025), *Genome Biology and Evolution*, doi:10.1093/gbe/evaf058. Opened. L70.
- Roth A, Schlegel PA (indexed 2008), *Brain, Behavior and Evolution*, doi:10.1159/000116556. Opened. L152.
- Roth G, Wiggers W (1983), *Zeitschrift für Tierpsychologie*, doi:10.1111/j.1439-0310.1983.tb01339.x. Opened. L118.
- Roth LSV, Kelber A (2004), *Proceedings of the Royal Society B*, doi:10.1098/rsbl.2004.0227. Opened. L63.
- Roth LSV and colleagues (2009), *Journal of Vision*, doi:10.1167/9.3.27. Opened. L64, L65.
- Rundus AS and colleagues (2007), *PNAS*, doi:10.1073/pnas.0702599104. Opened. L38.
- Saviola AJ, McKenzie VJ, Chiszar D (2012), *Acta Herpetologica*, doi:10.13128/acta_herpetol-9491. Opened. L43.
- Schlegel PA, Roth A (indexed 2008), *Brain, Behavior and Evolution*, doi:10.1159/000112987. Opened. L153.
- Schott RK and colleagues (2015), *PNAS*, doi:10.1073/pnas.1513284113. Opened. L91.
- Schott RK and colleagues (2021), bioRxiv, doi:10.1101/2021.08.27.457945. Opened. L132.
- Schraft HA, Bakken GS, Clark RW (2019), *Scientific Reports*, doi:10.1038/s41598-019-40466-0. Opened. L39.
- Schwenk K (indexed 2008), *Brain, Behavior and Evolution*, doi:10.1159/000113830. Opened. L93.
- Science STKE editors (2006), summary of Su C-Y and colleagues, *Science* 311: 1617 to 1621, doi:10.1126/stke.3272006tw104. Secondary (editor's summary). L72.
- Sillman AJ, Johnson JL, Loew ER (2001), *Journal of Experimental Zoology*, doi:10.1002/jez.1076. Opened. L79, L80.
- Sillman AJ, Ronan SJ, Loew ER (1991), *Proceedings of the Royal Society B*, doi:10.1098/rspb.1991.0016. Opened. L1 to L6.
- Simmons AM (1988), *Journal of Comparative Physiology A* 162: 397 to 403, doi:10.1007/bf00606126. Opened. L186.
- Simões BF and colleagues (2016), *Molecular Biology and Evolution*, doi:10.1093/molbev/msw148. Opened. L81.
- Soares D (2002), *Nature* 417: 241 to 242, doi:10.1038/417241a. Opened. L166.
- Solessio E, Engbretson GA (1993), *Nature* 364: 442 to 445, doi:10.1038/364442a0. Opened (preview). L73.
- Tashiro JH, Ventura DF, Hauzman E (2022), *Frontiers in Neuroanatomy*, doi:10.3389/fnana.2021.770804. Opened. L88, L89.
- Tempel P, Himstedt W (1979), *Zeitschrift für Naturforschung C*, doi:10.1515/znc-1979-9-1040. Opened. L143.
- Thomas KN and colleagues (2021), bioRxiv, doi:10.1101/2021.08.15.456426. Opened (full text). L192.
- Tosini G (1997), *Ethology Ecology & Evolution*, doi:10.1080/08927014.1997.9522875. Opened. L69.
- Tovar RU and colleagues (2025), *PNAS*, doi:10.1073/pnas.2504850122. Opened. L155.
- Tsai H-J, Ewert J-P (1988), *Brain, Behavior and Evolution*, doi:10.1159/000116530. Opened. L122.
- Twyman H and colleagues (2016), *Proceedings of the Royal Society B*, doi:10.1098/rspb.2016.1208. Opened. L111.
- Underwood G (1951), *Copeia*, doi:10.2307/1439099. Opened (the opening paragraph, in the collection). L215.
- Vanderbilt University News (8 November 2012), on Leitch D and Catania K (2012) in the *Journal of Experimental Biology*. Opened; secondary for the primary study. L164, L165.
- Ventura DF, Zana Y, de Souza JM, DeVoe RD (2001), *Journal of Experimental Biology*, doi:10.1242/jeb.204.14.2527. Opened. L109.
- Wikipedia (read 13 October 2026), "List of crotaline species and subspecies", "Craspedocephalus" and "Viperinae". Opened; secondary, for the sorting of viper genera in section 1.
- Wada S and colleagues (2012), *PLoS ONE*, doi:10.1371/journal.pone.0039003. Opened. L71.
- Wald G, Brown PK, Kennedy D (1957), *Journal of General Physiology*, doi:10.1085/jgp.40.5.703. Opened. L17, L18.
- Werner C, Himstedt W (1984), *Behavioural Brain Research* 12(1): 69 to 73, doi:10.1016/0166-4328(84)90204-3. Opened (EurekaMag record). L187.
- Wiggers W, Roth G, Eurich C, Straub A (1995), *Journal of Comparative Physiology A* 176(3): 365 to 377, doi:10.1007/bf00219062. Opened (Springer abstract; the fourth author is confirmed by the collection). L158.
- Witzmann F, Brainerd EL, Konow N (2019), *Integrative Organismal Biology*, doi:10.1093/iob/obz011. Opened (full text in the collection). L218.
- Yamamoto K, Nakata M, Nakagawa H (2003), *Brain, Behavior and Evolution*, doi:10.1159/000073272. Opened. L124.
- Yovanovich CA and colleagues (2017), *Philosophical Transactions of the Royal Society B*, doi:10.1098/rstb.2016.0066. Opened (full text). L126 to L129.
- Zamore SA, Araújo N, Socha JJ (2020), *Integrative and Comparative Biology*, doi:10.1093/icb/icaa143. Opened. L85 to L87.
- Zug GR (2020), Lungless salamander, *Encyclopaedia Britannica*. Opened. L188.
- Aho A-C (1997), *Perception* (conference abstract), doi:10.1068/v970294. Opened. L114; secondary for L115 (Birukow 1937).
- GBIF occurrence API, dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7, read 13 October 2026, and `runs/fetch/10` on the `ci` branch. Opened. Section 1.
- This repository: `src/cam.a.js`, `docs/SOURCES.md`, `docs/VIEWS.md`, `docs/COVERAGE.md`, `docs/views/sheets/salamander.md` and its audit, `data/regions/us-fl-alachua/species.json`. Opened.

## 8. Questions for a specialist

1. Which way do an anole's two foveae look, in degrees from the head's long axis? The `anole` picture places the central fovea's sharp spots out to the sides and the temporal fovea's straight ahead, from optics alone.
2. Does a pit viper's heat image of a still, warm animal fade within seconds, as the transient tectal responses (L30) suggest, or does it persist? The answer decides whether the heat stand-in should be motion or a model of warm bodies.
3. Do frogs and toads keep seeing a still scene while they themselves keep still, or does it fade? Leopard frogs move their heads and not their eyes (title in the collection, Skorina and colleagues 2011), and the answer sets the frog's `gate` strength.
4. How wide is the visual field of an alligator, a pond slider, a fence lizard, a house gecko, a toad and a newt? Every `fov` in these views but the snakes' is invented.
5. Do diurnal colubrids such as garter snakes and racers use their transformed rods (L91, L92) for a third colour channel? The answer decides whether `snake` keeps the two-cone matrix.
6. Does the lizard parietal eye's blue-green opposition track the colour of the sky through twilight, and on what timescale? The answer sets the third-eye strip's colour rule and speed.
