# Sensing sheet: tick (order Ixodida), with a note on mites

This sheet was written on 11 October 2026, from 17:42 to 18:58 EDT, and corrected after an audit on 12 October 2026 (see `tick.audit.md`). Unfinished items are marked **[unfinished]**, and they are these:

- The bioRxiv preprint of Carr and Salgado was not reopened in the audit. The published figures, which the audit checked, are used throughout.
- The Springer page for Kaltenrieder (1990) could not be read in the audit. Its DOI comes from the journal issue contents and its figures from the thesis.
- I did not search for flicker-fusion or dim-light measurements in ticks, or for eye measurements in the Lone Star Tick or the American Dog Tick themselves.
- The rows "Heat" and "Breath" say that an ordinary phone cannot sense radiant body heat and that no phone records carbon dioxide. No source was opened for either statement, in the first session or in the audit.

## 1. Scope

**What the proposed view holds.** The proposed view "tick and mite" holds 166,591 iNaturalist research-grade records in GBIF. They fall into three parts:

- Ticks (Ixodida) hold 60,462 records (36.3%).
- Gall mites (family Eriophyidae, order Trombidiformes) hold 98,340 records (59.0%).
- All other mites hold 7,789 records (4.7%). These are the rest of Trombidiformes plus Mesostigmata 689, Sarcoptiformes 589, Opilioacarida 25 and Holothyrida 11.

The order counts come from `docs/views/world-orders.csv`. The family split comes from GBIF facets I read on 11 October 2026.

**Ticks, by genus** (GBIF facet, same dataset):

| Genus | Records | Eyes |
|---|---:|---|
| Dermacentor (dog ticks) | 26,809 | yes |
| Ixodes (black-legged ticks) | 18,541 | none |
| Amblyomma (Lone Star, Gulf Coast) | 13,032 | yes |
| Rhipicephalus | 720 | yes |
| Hyalomma | 717 | yes (Kaltenrieder, 1989) |
| Haemaphysalis | 379 | none |

Eye presence comes from Bertone and colleagues (2023) unless marked. The eyed genera hold 41,278 records (68%) and the eyeless ones hold 18,920 (31%).

**Most recorded species worldwide:**

| Species | Records |
|---|---:|
| American Dog Tick, *Dermacentor variabilis* | 20,162 |
| Eastern Black-legged Tick, *Ixodes scapularis* | 11,082 |
| Lone Star Tick, *Amblyomma americanum* | 8,990 |
| Sheep Tick, *Ixodes ricinus* | 3,994 |
| Gulf Coast Tick, *Amblyomma maculatum* | 2,635 |
| *Dermacentor occidentalis* | 2,321 |
| Marsh Tick, *Dermacentor reticulatus* | 2,157 |
| Western Black-legged Tick, *Ixodes pacificus* | 1,940 |

In Alachua County, ticks hold 152 of the 163 records in this proposed view: Lone Star Tick 121, American Dog Tick 11, Eastern Black-legged Tick 11, Gulf Coast Tick 8 and Gopher Tortoise Tick 1.

**One view can be true for ticks.** Eyed and eyeless ticks do differ:

- **Eyed ticks** have a pair of eyes, each with a single lens in the two species measured. A camel tick walks toward large dark shapes on a pale background.
- **Eyeless ticks** have rows of light-sensitive cells along the body.

The proposed picture is coarse enough that it claims little beyond light, shade and large shapes. All three are measured in eyed ticks. Only light and shade are supported for eyeless ticks. Both kinds find hosts with Haller's organ on the front legs, and a camera records none of what that organ senses.

If the group ever has to split, the line falls between Amblyomma, Dermacentor, Rhipicephalus and Hyalomma (eyes) and Ixodes and Haemaphysalis (no eyes). The commonest members are on the eyed side.

**One view cannot be true for ticks and mites together** (see Mites below).

**Recommendation.** Build one view, `tick`, for order Ixodida only, and leave every mite order in `other`. There are two implementation notes.

- `tools/species/eyes.py` would route order Ixodida to `tick`.
- The word table in `src/cam.r.js` currently sends both "tick" and "mite" to `other`. Only "tick" should move.

### Mites

The brief expected most mite records to be velvet mites and water mites. GBIF's family facets for Trombidiformes show otherwise. The order's 104,815 records fall mostly in the seven families below.

| Family | Records |
|---|---:|
| Eriophyidae (gall mites) | 98,340 |
| Tetranychidae (spider mites) | 1,794 |
| Phytoptidae | 1,056 |
| Trombidiidae (velvet mites) | 975 |
| Bdellidae (snout mites) | 742 |
| Penthaleidae | 467 |
| Erythraeidae | 399 |

- The gall mites are led by *Eriophyes tiliae* (lime nail gall, 11,583) and *Vasates quadripedes* (maple bladdergall mite, 4,465).
- No water-mite family is among the twelve largest families. The smallest of those twelve holds 84 records, and only 408 Trombidiformes records fall outside them.

**Gall mites cannot share the tick's view.** They are usually under 0.2 mm long, have two pairs of legs and no distinct eyes, and are found by the galls their feeding raises on plants (RHS; idtools). A gall-mite record is a photograph of a plant. The tick view's picture rests on eyes or light-sensitive cells, and its rows rest on Haller's organ. The sources I opened describe neither in gall mites. A gall mite would need a sheet of its own, and its honest picture may be close to nothing. Until then, `other` (light and dark only) is the nearest the engine has.

**Velvet mites, Erythraeidae and water mites cannot share it either.** They belong to the Parasitengona:

- Terrestrial members almost always have well-developed eye lenses.
- Adults mostly hunt small arthropods (Lucid key; Australian Faunal Directory).
- Water mites have lateral eyes plus a median eye or a pair of small eyes between them (Olomski, 2012).

These are eyed predators. They would need measurements of their eyes (field, sharpness and colour), and I found none.

## 2. The rows

```
['m', 'Eyes', 'The Lone Star Tick and the dog ticks have one pair of eyes. The black-legged ticks have none.'],
```
Source: Bertone and colleagues, 2023. The Lone Star tick has "large eyes present", the American dog tick has "eyes present", and Ixodes and Haemaphysalis "lack eyes".

```
['g', 'Where they look', 'In the tropical bont tick, of the Lone Star Tick’s genus, each eye has one lens and takes in a patch 43 degrees wide and 49 high, aimed 39 degrees out from straight ahead and 33 degrees up. The camera looks straight ahead, as you do.'],
```
Source: Kaltenrieder, Labhart and Hess, 1989, in *Amblyomma variegatum*. The figures are the electroretinogram field widths at half sensitivity and the optical axis.

```
['g', 'Shapes', 'A camel tick walks toward a dark disc on a pale background once the disc spans about 5 degrees, and toward the outline of a camel as small as a real one 18 metres away. The picture is blurred to match, and that reading is this app’s own.'],
```
Source: Kaltenrieder, 1990, in *Hyalomma dromedarii*. The smallest effective dark disc spanned 4.8 degrees from the start, the smallest effective silhouette matched a real dromedary at 18 m, and a contrast of 3 to 1 was needed.

```
['g', 'Colour', 'The tropical bont tick is most sensitive to blue light near 480 nanometres, with a single peak. The picture is drawn in grey from the camera’s blue and green, and that rendering is this app’s invention.'],
```
Source: Kaltenrieder, Labhart and Hess, 1989. *A. variegatum* showed "a single sensitivity maximum in the blue range (ca. 480 nm)" by phototaxis, and an electroretinogram maximum near 470 nm.

```
['g', 'Without eyes', 'The sheep tick, in the same genus as the black-legged ticks, has two rows of about twenty light-sensitive cells along its upper sides. In a laboratory, its nymphs did almost all their walking in the dark.'],
```
Source: Perret and colleagues, 2003, in *Ixodes ricinus*. It has no eyes with corneas, two rows of 20 to 21 photosensitive cells behind the second leg pair in all stages, and nearly all locomotor activity in darkness.

```
['m', 'Questing', 'A questing tick grips a grass tip with its back two pairs of legs and holds the front pair out, ready to climb onto a passing host. Those front legs carry Haller’s organ, which smells and senses heat.'],
```
Source: CDC, archived page, for the posture. Carr and colleagues, 2017, for the organ "on the foretarsus of the first pair of legs". The same paper's "required for host seeking" sits in a sentence that opens "We can only hypothesize", so it is the authors' hypothesis. Carr and Salgado, 2019, for heat.

```
['m', 'Heat', 'Lone Star Ticks steer by radiant heat through a covered pit on each front leg, and at least seven in ten adult females detected a square 10 centimetres across, heated to 40 degrees Celsius, from a metre away. An ordinary phone cannot sense that heat, so it is left out.'],
```
Source: Carr and Salgado, 2019. At least 72% of adult female *A. americanum* detected the 10 by 10 cm, 40 °C target at 1 m, and only females were tested at that distance. Waxing over the capsule's opening abolished the response. Males, and both sexes of the American Dog Tick, gave similar results at 50 cm.

```
['g', 'Breath', 'In the tropical bont tick, one receptor cell in that same organ responds most to changes in carbon dioxide of a hundredth of a percent around the level in open air. No phone records carbon dioxide, so it is left out.'],
```
Source: Steullet and Guerin, 1992, in *A. variegatum*. The CO2-inhibited receptor in the Haller's organ capsule is most modulated by changes of 0.01% near the ambient 0.04%.

```
['x', 'Smell, damp and footsteps', 'Ticks also find hosts by body odour, moisture and vibration, and none of these reaches a camera.'],
```
Source: CDC, archived page: "Ticks find their hosts by detecting animals' breath and body odors, or by sensing body heat, moisture, and vibrations." Entomology Today (2018), reporting Josek, Allan and Alleyne (2017) on the Lone Star, American Dog and Eastern Black-legged Ticks, says Haller's organ "can even sense humidity".

## 3. The picture

**What the view shows.** The tick's view shows only what a camera can carry of the tick's light sense. That is a grey field of large soft patches, with bright sky and dark shapes, in which a shadow passing over registers as it happens.

The plant precedent applies to the senses a camera cannot record. Heat, breath and smell are left out of the picture and named in the rows, as the plant's far-red row does. The view departs from the plant in two ways. It keeps a coarse picture, because eyed ticks steer toward shapes. It also keeps quick change, because the plant's 2.5 second averaging would wash out the shadow, and the sources tie shadows and falling light to tick behaviour:

- Eyeless sheep ticks walked almost only in the dark, and the authors propose that falling light sets them moving (Perret and colleagues, 2003).
- Eyed camel ticks walk toward dark shapes (Kaltenrieder, 1990).
- The CDC page says "Some species can even recognize a shadow."

**Drawn from the camera:** the camera can supply the amount of light, large dark shapes against a brighter background, and their movement.

**Stood in for:** colour is drawn as grey weighted to the camera's blue and green, and the weights are invented.

**Left out and named in the rows:** the picture leaves out heat, breath, body odour, moisture and vibration, which the sources describe as how ticks find hosts.

**Left out silently:** the picture also drops the upward and sideways aim of the two eyes, and fine detail.

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Tick', 'a tick' | This is the app's wording. |
| `cpd` | .1 | This value rests on the row "Shapes". It is my conversion of Kaltenrieder (1990): reading a 4.8 degree dark disc as half a cycle gives about 0.1 cycles per degree. The paper gives a detection threshold for a dark disc, and treating it as a resolution limit is my step, so the conversion is **invented**. The threshold was measured in *Hyalomma dromedarii*, whose eyes protrude and whose threshold for walking toward light is a hundred times lower than that of *A. variegatum* (Kaltenrieder, Labhart and Hess, 1989), so the value may flatter the commoner ticks. On a phone the blur radius comes to a quarter of the screen's long side, which leaves two or three soft patches across. |
| `M` | [.05, .45, .5, .05, .45, .5, .05, .45, .5] | This value rests on the row "Colour". The single peak near 480 nm is measured in *A. variegatum*. The weights are **invented**. Equal rows give grey, in which red goes near black, blue sky stays bright and foliage goes mid-dark. |
| `pupil` | 'none' | This value is **invented**. No source I opened describes a pupil in tick eyes. It matches the bee and plant entries and gives the same output as 'o'. |
| `field` | unset (0) | I considered `field: 1` (the plant's setting) and rejected it. The eyed ticks, 68% of records, steer toward shapes about 5 degrees across. At `cpd: .1` the picture already holds only large soft patches, close to what `field: 1` gives. |
| `persist` | unset | No source for a time constant was found, and the plant's averaging would erase the passing shadow. |
| `rate` | unset | No flicker-fusion measurement for ticks was found. |
| `gate` | unset | Kaltenrieder (1990) found stationary dark targets effective, so the picture keeps still things. |
| `fov` | unset | In *A. variegatum* the two half-sensitivity fields would span about 121 degrees, with a gap of about 35 degrees straight ahead. That is my reading of 39 ± 21.5 degrees on each side, treating the widths as edges. Values under 180 change nothing in the engine, and the aim of the two fields cannot be drawn (section 4). |
| `gain` | unset | No comparison with human dim-light sensitivity was found. |
| `topoA`, `topoS`, `fall`, `fovea`, `dof`, `sheen`, `uvBlue`, `noGreen`, `hold`, `thrust` | unset | No source supports them. The ultraviolet peak was found in *Hyalomma* only. |
| `cue` | 'Hold the phone at the height of the grass tips and tilt it up. Only large shadows remain.' | This is the app's wording. Ticks wait on the tips of grasses (CDC), and the eyes of *A. variegatum* aim 33 degrees above the horizon (Kaltenrieder, Labhart and Hess, 1989). |

Here is a sketch of the entry for the owner to place. No file was changed.

```
var TICK = [.05, .45, .5, .05, .45, .5, .05, .45, .5];   // one peak near 480 nm in Amblyomma variegatum; grey from blue and green, weights invented
tick: { chip: 'Tick', who: 'a tick', cpd: .1, pupil: 'none', M: TICK,
  cue: 'Hold the phone at the height of the grass tips and tilt it up. Only large shadows remain.', rows: [ /* the nine rows above */ ] }
```

**What Carr and Salgado (2019) shows, checked.** I read the published abstract through the Vanderbilt repository and the full bioRxiv preprint. The audit then checked these figures against the published article.

It does show the following.

- Unfed adult Lone Star Ticks (mainly females) walk toward a warm 10 by 10 cm wall in a 1 m arena. They respond at 37 °C and above from 50 cm, and at least 72% of females detect a 40 °C target from 1 m.
- Male Lone Star Ticks and both sexes of American Dog Tick gave similar results.
- The response is to radiant heat. Aluminum foil on the walls abolished it, while an infrared-transparent film against convection left it in place.
- The response depends on the capsule of Haller's organ, because waxing over the capsule's opening abolished it.
- DEET, picaridin and 2-undecanone abolished the heat response at 50, 54 and 42 ng per cubic centimetre. DEET left the carbon dioxide response in a Y-tube unchanged.

Its claims go beyond its experiments in these places.

- No person or animal was used as a target. The published "several meters" (abstract), "up to 4 meters under ideal conditions" (results) and "at least 4 meters" (discussion) for a person are extrapolations from the plate.
- The field of "at most 5.7 degrees" is the authors' inference from the target's size at 1 m. No measurement of the organ's field was made.
- No wavelengths were tested. The 5 to 20 micrometre range for body heat is cited from another source.
- The abstract notes that earlier work had concluded ticks do not use radiant heat to find hosts, so this result stands against that earlier work.

## 4. What the engine cannot draw yet

Plainly: **no phone input the app can count on stands in for heat or carbon dioxide.** Carr and Salgado cite body heat at 5 to 20 micrometres. An ordinary phone camera does not record it, and no phone sensor a web page can read measures carbon dioxide. I hold both statements as general knowledge and opened no source for either. Clip-on thermal cameras and a few rugged phones with built-in thermal cameras exist, but I did not check them in this session, and the app could not count on them.

| Effect | What it would show | Phone input that could stand in | Judgement |
|---|---|---|---|
| Heat through the capsule | A narrow spot, at most 5.7 degrees across, would brighten when the front leg points at something warm within about a metre. The capsule rides on the leg, so where it reads follows where the leg points (my inference). | None measures heat. Only the camera picture could carry a stand-in (see skin colour below). | As measurement, it is impossible. As an invention, a body-detector spot is medium work. |
| Carbon dioxide | The picture would wake from rest as breath arrives, as ticks did in a wind tunnel at about 0.04 to 1% (Steullet and Guerin, 1992). | None measures carbon dioxide. The microphone picks up a breath blown on the phone as noise, which would stand in for the act of breathing. It cannot measure carbon dioxide or a breath from across a room. | It is easy to medium work (microphone permission and audio level). It would be invented, and it must be called so in an `i` row. |
| Vibration | The picture would stir as footsteps approach. | Motion sensors register knocks to the phone, and the microphone hears footsteps. | It is medium work. It would be invented and would add little. |
| Moisture and body odour | These have no visual form. | No input that the app can read senses them, to my knowledge. | It is impossible. |
| Two eyes aimed up and out | Two soft patches of light would sit at upper left and upper right, with dimness straight ahead (*A. variegatum*: axes 39 degrees out and 33 up). | The camera picture could be masked to two windows, and the engine's aperture mask (`u_ap`, `u_shape`) could take a new shape. A phone camera is narrower than the span of both eyes, so the outer parts would be invented, as the cat's edges are. | It is easy, and worth doing once the eyes of *A. americanum* or *D. variabilis* are measured. |
| Direction from eyeless cells (Ixodes) | It is unknown whether these cells give only how much light there is or also which side it comes from. | The camera could stand in, at `field: 1`. | It waits on a source (question 3). |
| A gall mite | It would show nothing, since gall mites have no eyes and live on or inside plant galls. | No input is needed. | Drawing it as a dark screen is trivial. Whether an empty screen counts as a view is a design question for the owner. |

**Could warmth be drawn from skin-coloured areas?** It could, as the app's invention, and I recommend against it.

- A rule keyed to skin colour would light up wood, sand, cardboard and dry leaves, and would miss clothed people and furred animals.
- It would likely work better on some shades of skin than on others. That is my judgement, and I opened no source for it.
- It would also misdraw the sense itself. The measured heat sense looks along a narrow line (at most 5.7 degrees by the authors' estimate) and reached a warm square a metre away. A glow painted wherever skin appears would overstate both its width and its reach.

If the owner wants warmth drawn anyway, the closer stand-in is a person-and-animal detector that lights one small spot at the centre of the frame when a body sits there. The person would then sweep the phone the way a questing tick holds out its leg. That row would be graded `i` and would call the spot an invention.

## 5. Sources

- Carr, A. L. and Salgado, V. L., 2019. Ticks home in on body heat: a new understanding of Haller's organ and repellent action. *PLoS ONE* 14(8): e0221659. doi:10.1371/journal.pone.0221659. Findings: thermotaxis to a 40 °C, 10 by 10 cm target from 1 m by at least 72% of female *A. americanum*, abolished by waxing the capsule; field "at most 5.7 degrees" in the published article; repellent doses; distance to a person extrapolated. **opened**: the published abstract via https://ir.vanderbilt.edu/handle/1803/10391, and the full text of the bioRxiv preprint (doi:10.1101/564179), where the figures were read. The published figures were checked in the audit of 12 October 2026 at https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0221659, and they are the ones this sheet uses.
- Kaltenrieder, M., Labhart, T. and Hess, E., 1989. Spectral sensitivity, absolute threshold, and visual field of two tick species, *Hyalomma dromedarii* and *Amblyomma variegatum*. *Journal of Comparative Physiology A* 165(2): 155 to 164. doi:10.1007/BF00619190, confirmed at https://link.springer.com/article/10.1007/BF00619190, whose summary gives the same figures. Read in Kaltenrieder's 1989 Neuchâtel thesis, https://libra.unine.ch/bitstreams/1a2fadd3-3feb-47eb-8b81-ffa264e7d13f/download. Findings: *Amblyomma* single peak near 480 nm; fields 43 by 49 degrees, axes 39 and 33 degrees; thresholds 5.2 × 10^8 (*Amblyomma*) and 5.2 × 10^6 (*Hyalomma*) photons per second per square centimetre; single-lens eyes in both. **opened** (English summary in the thesis, and the Springer summary in the audit).
- Kaltenrieder, M., 1990. Scototaxis and target perception in the camel tick *Hyalomma dromedarii*. *Experimental and Applied Acarology* 9(3-4): 267 to 278. doi:10.1007/BF01193433, taken from the issue contents at https://link.springer.com/journal/10493/volumes-and-issues/9-3, because the article page could not be read. Same thesis address. Findings: smallest effective dark disc 4.8 degrees; smallest effective silhouette equal to a dromedary at 18 m; 3 to 1 contrast needed; black or grey targets on a white background; stationary targets effective. **opened** (summary in the thesis).
- Perret, J.-L., Guerin, P. M., Diehl, P.-A., Vlimant, M. and Gern, L., 2003. Darkness induces mobility, and saturation deficit limits questing duration, in the tick *Ixodes ricinus*. *Journal of Experimental Biology* 206: 1809 to 1815. doi:10.1242/jeb.00345. Findings: no eyes with corneas; two rows of 20 to 21 photosensitive cells; nearly all walking in darkness. **opened** (article page at cob.silverchair.com and record at https://libra.unine.ch/handle/123456789/18757).
- Steullet, P. and Guerin, P. M., 1992. Perception of breath components by the tropical bont tick, *Amblyomma variegatum* Fabricius (Ixodidae). I. CO2-excited and CO2-inhibited receptors. *Journal of Comparative Physiology A* 170(6): 665 to 676. doi:10.1007/BF00198976. Findings: CO2 receptors in the Haller's organ capsule, strongest response to changes of 0.01% near the ambient 0.04%, ticks activated by about 0.04 to 1%. **opened** (abstract at https://libra.unine.ch/handle/20.500.14713/60954).
- Carr, A. L., Mitchell, R. D. III, Dhammi, A., Bissinger, B. W., Sonenshine, D. E. and Roe, R. M., 2017. Tick Haller's organ, a new paradigm for arthropod olfaction: how ticks differ from insects. *International Journal of Molecular Sciences* 18(7): 1563. doi:10.3390/ijms18071563. Finding: the organ sits on the foretarsus of the first pair of legs. The paper puts its role in host seeking as a hypothesis ("We can only hypothesize"). **opened** (https://www.mdpi.com/1422-0067/18/7/1563).
- Centers for Disease Control and Prevention. Life cycle of hard ticks that spread disease. Archived copy captured 17 October 2012, https://cybercemetery.unt.edu/oilspill/20121017132403mp_/http://www.cdc.gov/ticks/life_cycle_and_hosts.html. Findings: questing posture; hosts found by breath, body odours, heat, moisture and vibrations; "Some species can even recognize a shadow"; ticks wait on the tips of grasses and shrubs. **opened** (the current CDC page could not be fetched).
- Walker, M. S., in Entomology Today, 16 January 2018. An up-close look at the tiny sensory pits that ticks use to smell. https://entomologytoday.org/2018/01/16/up-close-look-tiny-sensory-pits-ticks-use-smell/. Finding: Haller's organ detects carbon dioxide, ammonia and pheromones, and "can even sense humidity and infrared light". **opened**. It reports Josek, Tanya, Allan, Brian and Alleyne, Marianne, 2017, Morphometric analysis of chemoreception organ in male and female ticks (Acari: Ixodidae), *Journal of Medical Entomology*, doi:10.1093/jme/tjx232, on *I. scapularis*, *A. americanum* and *D. variabilis*. **secondary** (names, title, year and DOI as Entomology Today gives them; volume and pages not checked).
- Bertone, M. A., Reiskind, M. H., Crawley, S. E. and Watson, D. W., 2023. *Common Ticks of North Carolina: An Identification Guide*, version 1.1. NC State University. https://pdic.ces.ncsu.edu/wp-content/uploads/2023/04/NC_Tick_Guide_v1.0_April_14_2023.pdf. Findings: eyes in Amblyomma, Dermacentor and Rhipicephalus; none in Ixodes and Haemaphysalis. **opened**.
- Royal Horticultural Society. Gall mites. https://www.rhs.org.uk/biodiversity/gall-mites. Findings: usually under 0.2 mm, seen only with a microscope, found by their galls, two pairs of legs. **opened**.
- Invasive Mite Identification (idtools.org). Eupodides, Eriophyoidea. https://idtools.org/id/invasive_mite/Invasive_Mite_Identification/key/Major_Mite_taxa/Media/Html/Eupodides_Eriophyoidea.htm. Findings: "distinct eyes absent"; usually 0.12 mm or less; all plant parasites. **opened**.
- Acariformes, in a Lucid key to soil mites (no author named on the page). https://keys.lucidcentral.org/keys/cpitt/public/mites/Soil%20Mites/html/Parasiten.htm. Findings: terrestrial Parasitengona have "eye lenses almost always well-developed"; most adults prey on small arthropods. **opened**.
- Australian Faunal Directory. Family Trombidiidae Leach, 1815 (compiler B. Halliday). https://biodiversity.org.au/afd/taxa/TROMBIDIIDAE. Findings: adults are predators of small soft-bodied insects and mites; larvae are parasites. **opened**.
- Olomski, R., 2012. The median eye of freshwater mites (Acari: Parasitengonae, Hydrachnidia) and its fate in the stem lineage of the Euhydrachnidia, Witte & Olomski 1991. *Soil Organisms* 84(2): 445 to 458. https://www.soil-organisms.org/SO/article/view/276. Finding: water mites have lateral eyes and a median eye or a pair of ocelli between them. **opened** (abstract).
- Wikipedia. Parasitengona. https://en.wikipedia.org/wiki/Parasitengona. Finding: Trombidiidae, Erythraeidae and the water mites are Parasitengona. **opened**.
- GBIF.org occurrence API, dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7, read 11 October 2026. Facets: Ixodida by genus and species, Trombidiformes by family, Eriophyidae by species. Names come from https://api.gbif.org/v1/species/{key}, except for the four Alachua species keys, which are named from the repository's Alachua file. Findings: all counts in section 1. **opened**.
- This repository: `docs/VIEWS.md`, `docs/views/world-orders.csv`, `docs/views/no-view-us-fl-alachua.csv`. Findings: order totals and the Alachua species. **opened**.

## 6. Open questions for a sensory scientist

1. Has anyone repeated Carr and Salgado's thermotaxis result, or measured the capsule's field directly? Their "at most 5.7 degrees" is inferred from target size, and a person at several metres is an extrapolation.
2. What do the eyes of the Lone Star Tick and the American Dog Tick resolve, and where do they point? This sheet borrows field and colour from *A. variegatum* and the 5 degree target from *H. dromedarii*.
3. Do the light-sensitive cells of eyeless Ixodes give any sense of direction, or only how much light there is? Does *I. scapularis* carry the same rows as *I. ricinus*?
4. Does a passing shadow make a questing hard tick raise or wave its front legs, and how fast do tick photoreceptors follow flicker? Either answer would set `persist` or `rate`.
5. Among the mites people photograph after the eyeless gall mites, have the eyes of velvet mites or spider mites (Tetranychidae) been measured, and do spider mites have eyes at all?
