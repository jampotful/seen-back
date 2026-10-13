# Sensing sheet: salamander and newt (order Caudata), with a note on caecilians (Gymnophiona)

This sheet was written on 12 October 2026, from 14:06 to 14:45 EDT. It was audited on 12 October 2026, from 14:51 to 15:15 EDT, and the corrections are listed in `salamander.audit.md`. The row "Still things" is regraded from `m` to `i`, three rows are reworded, and the parts of the Isayama and colleagues (2014) entry that need the full text remain unconfirmed. The unfinished items are these:

- I found no source, in the time given, for sharpness (acuity), field of view, pupil shape, flicker fusion or dim-light sensitivity in any salamander. Those fields are left unset or marked **invented**.
- I found no source that tests whether a salamander ignores prey that keeps still. The decision to leave `gate` unset rests on a maze study in tiger salamanders and is explained in section 3.
- The lateral line is sourced for amphibians in general (Britannica) and in the axolotl, and the electric sense in the axolotl and, by a meeting abstract, in amphiumas. I opened nothing on the sirens or mudpuppies.
- Pages I could not read: Roth (1976) on prey catching in *Hydromantes italicus* at https://link.springer.com/article/10.1007/BF00663434 (refused with HTTP 429, rate limited); the bioRxiv abstract page for the caecilian preprint, Wikipedia's "Salamander" article and the PMC copy of a review of flicker-fusion rates (PMC9803175), all three withdrawn at a permission prompt; Graves and Placyk (2001, 2002) on red-backed salamander foraging, whose repository records hold no abstract; and a Semantic Scholar record for Roth (1976), withdrawn at a permission prompt.
- The Nature page for Phillips and Borland (1992) names neither the species nor the wavelengths. The figures for the newt's compass come from Phillips and colleagues (2001).

## 1. Scope

**What the view holds.** The proposed view "salamander, newt and caecilian" holds 632,992 iNaturalist research-grade records in GBIF (read 11 October 2026, from the assignment): Caudata 631,944 and Gymnophiona 1,048. Caecilians are 0.17% of the group.

**Caudata, by family** (GBIF facet, dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7, read 12 October 2026; the families sum to 631,944, the order total). Common names in brackets are my glosses.

| Family | Records | Share of Caudata |
|---|---:|---:|
| Plethodontidae (lungless salamanders) | 272,719 | 43.2% |
| Salamandridae (newts, fire salamanders) | 264,814 | 41.9% |
| Ambystomatidae (mole salamanders, axolotl) | 83,570 | 13.2% |
| Hynobiidae (Asian salamanders) | 4,995 | 0.8% |
| Rhyacotritonidae (torrent salamanders) | 1,648 | 0.3% |
| Proteidae (mudpuppies, olm) | 1,354 | 0.2% |
| Sirenidae (sirens) | 1,091 | 0.2% |
| Amphiumidae (amphiumas) | 1,083 | 0.2% |
| Cryptobranchidae (giant salamanders, hellbender) | 670 | 0.1% |

The four families whose adults live in water (Proteidae, Sirenidae, Amphiumidae, Cryptobranchidae) hold 4,198 records, 0.7% of the order. That grouping is my general knowledge, and I opened no source for it.

**Most recorded species worldwide** (GBIF facet, same dataset and date; names from https://api.gbif.org/v1/species/{key}, common names my glosses):

| Species | Records |
|---|---:|
| Eastern Red-backed Salamander, *Plethodon cinereus* | 74,121 |
| Eastern Newt, *Notophthalmus viridescens* | 61,966 |
| Fire Salamander, *Salamandra salamandra* | 42,025 |
| Spotted Salamander, *Ambystoma maculatum* | 30,711 |
| California Newt, *Taricha torosa* | 28,222 |
| California Slender Salamander, *Batrachoseps attenuatus* | 20,921 |
| Ensatina, *Ensatina eschscholtzii* | 18,915 |
| Rough-skinned Newt, *Taricha granulosa* | 17,412 |
| Smooth Newt, *Lissotriton vulgaris* | 17,405 |

These nine hold 311,698 records, 49.3% of the order. Seven of the nine are lungless salamanders (three) or newts (four).

**In Alachua County** the group holds 148 records (from `docs/views/no-view-us-fl-alachua.csv`): Striped Newt 31, Eastern Newt 30, Two-toed Amphiuma 26, Greater Siren 20, coastal plain dwarf salamander 18, Mole Salamander 9, Southeastern Slimy Salamander 8, Southern Dwarf Siren 4, Three-lined Salamander 1 and Mud Salamander 1. The amphiuma and the two sirens hold 50 of the 148 (34%), so the water-dwelling forms are far commoner here than worldwide.

**One view can be true for the salamanders and newts.** The members measured all have eyes with cones for ultraviolet, short and long wavelengths, or (in the fire salamander) three receptor types with ultraviolet sensitivity. That covers the tiger salamander, three newts including the Smooth Newt, and the Fire Salamander, and the ultraviolet cone gene was found in 40 of 58 species from six families (Mège and colleagues, 2016). The water-dwelling forms keep their eyes (no source was opened for their eyes) and add senses a camera cannot carry (the lateral line, electric sense), which go in `x` rows.

**Caecilians and the olm stay outside the view.**

- Caecilians have "reduced eyes covered by skin or bone". Their short-wavelength cone genes are lost, and the authors of the study I read find no conclusive evidence of cone cells and write that light intensity and spectra "may be the only visual information available to caecilians" (Navarrete Méndez and colleagues, 2025, in the Discussion of the bioRxiv preprint, where it is offered as interpretation). Their honest picture is close to the plant's: light and colour with no image.
- The olm (*Proteus anguinus*) has a regressed eye that still carries visual pigments, a reduced pineal organ, and skin that is itself sensitive to light through melanopsin in its pigment cells (AmphibiaWeb, citing Kos and colleagues, 2001). Its honest picture is also light without an image.

If the group has to split, the line falls between the eyed salamanders and newts on one side and the caecilians and the olm on the other. The commonest members are all on the eyed side. Other blind cave salamanders would join the olm, which is my suggestion; I opened no source on them.

**Recommendation.** Build one view, `salamander`, for order Caudata, and send Gymnophiona and the olm to `other` (light only), whose `field: 1, sat: 0` picture is the nearest the engine has to their sense until each has a sheet. There are three implementation notes.

- `tools/species/eyes.py` routes Anura to `frog` and would route Caudata to `salamander`, with *Proteus anguinus* as a species exception to `other`, and Gymnophiona to `other`.
- The word table in `src/cam.r.js` (line 48) sends "olm" and "caecilian" to `salamander`. Those two words should move to `other`.
- `salamander` would leave `GROUPS` for `EYES` in `src/cam.a.js` and join `ORDER`.

## 2. The rows

```
['m', 'Ultraviolet', 'Tiger salamanders and newts have cones tuned to ultraviolet light, which is invisible to you, near 360 nanometres in the tiger salamander and 340 to 360 in three newts. The gene for that cone turned up in 40 of 58 salamander species tested.'],
```
Source: Ma and colleagues, 2001, for the tiger salamander's ultraviolet cone pigment at 356 nm (360 nm with the A2 chromophore). Isayama and colleagues, 2014, for ultraviolet cones in hatchling and terrestrial adult tiger salamanders, which their abstract states. The audit could not open the full text, so the larval recordings and the table value of 361 nm that the first draft cited are unconfirmed, and the row uses neither. Korenyak and Govardovskii, 2013, for ultraviolet cones at 340 to 359 nm in *Pleurodeles waltl*, *Lissotriton vulgaris* and *Cynops orientalis*. Mège and colleagues, 2016, for the gene in 40 of 58 species from six families.

```
['m', 'Hunting by ultraviolet', 'Smooth newt larvae catch more water fleas when ultraviolet light is present, and larvae raised without it catch fewer.'],
```
Source: Martin and colleagues, 2016, in *Lissotriton vulgaris*. Daphnia survived better when ultraviolet was absent during testing, and larvae reared without ultraviolet captured prey less efficiently.

```
['m', 'Colour', 'The fire salamander snapped at a coloured worm dummy moving across a differently coloured background of equal brightness, so it tells colours apart by hue. Its three kinds of receptor peak near 450, 500 and 570 nanometres, and colours stay as your camera gives them.'],
```
Source: Przyrembel, Keller and Neumeyer, 1995, in *Salamandra salamandra*: trichromatic colour vision, with the results fitting three receptor types near 450, 500 and 570 nm. The same abstract says its ultraviolet sensitivity "is not due to a separate ultraviolet photoreceptor".

```
['m', 'Distance', 'The fire salamander refocuses its eyes before it turns to prey, and judges distance that way. The tongue-shooting lungless salamanders have eyes set forward, and the two eyes’ views line up at the tongue’s farthest reach; one Sardinian species was photographed with its tongue out almost 6 centimetres, and salamanders of its genus flick the tongue out in about a hundredth of a second.'],
```
Source: Werner and Himstedt, 1984, in *Salamandra salamandra*: refraction makes a myopic shift before the salamander turns to the prey, so "fire salamanders use accommodation for distance estimation". The second sentence is measured in members outside the commonest species: Wiggers, Roth, Eurich and Straub, 1995, in tongue-projecting salamanders (Bolitoglossini; the abstract names no species): frontal eyes, and binocular neurons whose fields share zero disparity at distances matching the tongue's maximum reach. Sanders, 1997 (UC Berkeley release reporting Deban, Wake and Roth in *Nature*, 1997), for *Hydromantes supramontis*: one photograph showed the tongue extended almost 6 cm, about 80% of head and body length. The hundredth of a second is a separate sentence in the release, "They can flick them out in about a hundredth of a second", said of these salamanders in general; the release ties it to no particular strike. The *Nature* page gives neither figure in its preview.

```
['i', 'Still things', 'This view keeps still things, which the frog view drops, and that choice is our guess: no test of whether a salamander ignores still prey was found, though tiger salamanders learned to turn the way a visual mark in a maze showed them. For prey, a relative of the red-backed salamander weighs a moving target’s size and speed above its shape.'],
```
Source: Kundey and colleagues, 2016, in *Ambystoma tigrinum*. The salamanders learned to turn in the direction indicated by a compound visual cue in a cross-maze when it was the only cue that predicted reward, though they preferred to learn a fixed turn. The abstract does not say where the cues were placed or whether any moved. A salamander walking a maze sees a fixed mark shift as it moves, so the study does not test whether a still salamander sees still things, and the row is graded `i`. Schülert, 2004, in *Plethodon shermani*: with animated prey dummies, size and velocity were the dominant features, and movement pattern, shape and contrast counted for less.

```
['g', 'Night', 'Fire salamanders are active at night. A model of their eyes says they can tell a red throat from a yellow one by night light.'],
```
Source: Aguilar and colleagues, 2024, in *Salamandra salamandra gallaica*, "a nocturnal amphibian". The finding comes from visual models of conspecifics and predators under night-light conditions. The page I read does not give the models' inputs, and it reports no behavioural test.

```
['x', 'Smell', 'Lungless salamanders tap their snouts on the ground, and a groove running from each nostril to the lip draws odours up to the nose. They follow smells to food and away from danger, and a camera records no smell.'],
```
Source: Zug, 2020, Britannica, "lungless salamander": nasolabial grooves from the upper lip to a nostril, nose tapping, odour particles moved up the groove by capillary action, and odours used for "chemical alarm cues, directions to food sources".

```
['x', 'Moving water and electricity', 'Larvae and salamanders that live wholly in water have a lateral line, which feels movement and pressure changes in the water around them. The axolotl also has sensors for electric fields, amphiumas respond to weak electric currents, and a camera records none of this.'],
```
Source: Zug, 2018, Britannica, "lateral line system": in amphibians the system "occurs only in larval forms and in adult forms that are completely aquatic", and it serves "to detect movements and pressure changes in the surrounding water". Münz, Claas and Fritzsch, 1984, in *Ambystoma mexicanum*: electroreceptive units (ampullary organs) and mechanoreceptive units (neuromasts) in the head lateral line. Keathley and Moon, 2021 (meeting abstract), in *Amphiuma means* and *A. tridactylum*: behavioural responses, including likely feeding responses, to low-voltage alternating and direct currents. That abstract gives no field strengths and does not report the organs in amphiumas.

```
['x', 'Magnetic compass', 'The eastern newt has a magnetic compass that works through light-sensitive cells in or near the pineal organ, at the top of the brain. In light of wavelengths longer than 500 nanometres its chosen direction swings a quarter turn, and a camera records none of this.'],
```
Source: Phillips and Borland, 1992: magnetic compass orientation in a semiaquatic salamander is affected by the wavelength of light. Phillips, Deutschlander, Freake and Borland, 2001, on *Notophthalmus viridescens*: under light above 500 nm the newt's magnetic compass direction is rotated by 90°, and the short-wavelength input is mediated by extraocular photoreceptors in or near the pineal organ. The words "at the top of the brain" are my gloss of where the pineal organ sits.

```
['i', 'Ultraviolet tint, sharpness, field and pupil', 'A phone can’t capture ultraviolet light, so the violet tint here stands in for it. Sharpness, field of view, pace and pupil are our best guesses.'],
```
Source: none opened for any of these. The statement that a phone camera cannot record ultraviolet is general knowledge, and I opened no source for it.

## 3. The picture

**What the view shows.** The view shows the camera picture with its colours kept and a violet sheen standing in for ultraviolet. It is softer than yours and slightly wider, a tap brings one distance into focus, and still things stay in it.

**Why `gate` stays unset.** The frog's rule rests on frogs ignoring still prey. For salamanders I found no test of still prey either way. What I did find shows salamanders using visual marks placed in a maze, which the abstract does not describe as moving (tiger salamanders, Kundey and colleagues, 2016), and prey tests run with moving dummies (Przyrembel and colleagues, 1995; Schülert, 2004). A gate would erase marks like those, so the picture keeps them. This is a judgement on thin evidence and is the first open question.

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Salamander, newt', 'a salamander or newt' | This is the app's wording. `who` matches the existing `GROUPS` entry. |
| `fov` | 260 | This value is **invented**. No field of view was found for any salamander. The value sits below the frog's 340 (itself a guess) because the tongue-shooting lungless salamanders have eyes set forward (Wiggers and colleagues, 1995). |
| `cpd` | 4 | This value is **invented**. No acuity was found. The value repeats the frog's guess. |
| `pupil` | 'o' | This value is **invented**. No source on pupil shape was opened. |
| `sheen` | .6 | The strength is **invented**, and it rests on the row "Ultraviolet". It matches the reptile and wader entries. |
| `M` | unset (identity) | This rests on the row "Colour": the fire salamander has three receptor types and tells colours by hue. |
| `uvBlue` | unset | The bee's false-colour shift would claim a separate ultraviolet channel moved into view. The fire salamander's ultraviolet sensitivity comes from its 500 nm receptor (Przyrembel and colleagues, 1995), so the sheen is the smaller claim. |
| `gate` | unset (0) | See above and the row "Still things". |
| `field` | unset (0) | Salamanders and newts have eyes. Caecilians and the olm go to `other` (section 1). |
| `gain` | unset | No comparison with human dim-light sensitivity was found. The row "Night" supports colour at night by a model and gives no ratio. |
| `rate`, `persist` | unset | No flicker-fusion measurement for any salamander was read. |
| `fovea` | unset | Wiggers and colleagues (1995) report that in the tongue-shooters most tectal neurons are activated by the retinal area for the frontal field, which magnifies that region. The commonest species, the red-backed salamander and the newts, are outside that tribe (no source was opened for the red-backed salamander's tribe), and no figure was given. |
| `dof` | 12 | This rests on the row "Distance": the fire salamander focuses on prey to judge its distance (Werner and Himstedt, 1984), which the engine's tap-to-focus blur can suggest. The strength is **invented**, half the alligator's 24. |
| `topoA`, `topoS`, `fall`, `noGreen`, `hold`, `thrust` | unset | No source supports them. |
| `cue` | 'Tap what you would catch to bring it into focus. Colours stay, with a violet tint for ultraviolet.' | This is the app's wording. |

Here is a sketch of the entry for the owner to place. No file was changed.

```
salamander: { chip: 'Salamander, newt', who: 'a salamander or newt', fov: 260, cpd: 4, pupil: 'o', dof: 12, sheen: .6,
  cue: 'Tap what you would catch to bring it into focus. Colours stay, with a violet tint for ultraviolet.', rows: [ /* the ten rows above */ ] }
```

## 4. What the engine cannot draw yet

| Effect | What it would show | Phone input that could stand in | Judgement |
|---|---|---|---|
| The newt's magnetic compass | It would show a faint line across the picture pointing along the magnetic field, which swings a quarter turn when the scene's light is mostly longer than 500 nm (green to red). | The phone's magnetometer could give the field's direction, which browsers expose as a compass heading through device-orientation events (my understanding; I opened no source), and the camera's average colour could stand in for the light's wavelength. | It is medium work. The rule comes from the newt, and the line itself would be the app's drawing. |
| The tongue's reach | It would show one narrow band of sharp focus fixed at the tongue's reach, with everything nearer and farther soft, for the tongue-shooters. | The engine's depth guess from height in the frame could serve, with `dof` held at a fixed near focus. `dof: 12` with a tap already moves the focus as the fire salamander's eye does. | It is easy, but the distance chosen would be invented. |
| The lateral line (axolotl and other water dwellers) | It would show ripples or pressure drawn around things that move close to the animal. | Motion between camera frames could stand in for nearby water movement, and the motion sensors register the phone being moved. | It is medium work and would be invented. |
| The electric sense (axolotl, amphiumas) | Nearby living things would glow faintly through mud or murk. | No phone input senses weak electric fields in water. | It is impossible as measurement. |
| Smell by nose tapping | It has no visual form, though a tap on the screen could stand for a nose tap. | No phone input senses odour. | It is impossible as measurement. A tap-to-sniff gesture would be decoration. |
| Ultraviolet | It would show ultraviolet patterns on flowers, prey and other salamanders. | An ordinary camera records none (general knowledge, no source opened), and the sheen stands in. | It is impossible as measurement. |
| Caecilians and the olm | It would show light, colour and direction with no image. | The camera can supply it at `field: 1`, as for the plant and `other`. | It is trivial. A caecilian or olm entry could reuse the plant's settings once it has its own rows. |

## 5. Sources

- Isayama, T., Chen, Y., Kono, M., Fabre, E., Slavsky, M., DeGrip, W. J., Ma, J.-X., Crouch, R. K. and Makino, C. L., 2014. Coexpression of three opsins in cone photoreceptors of the salamander *Ambystoma tigrinum*. *Journal of Comparative Neurology* 522(10): 2249 to 2265. PMID 24374736. doi:10.1002/cne.23531 (the DOI was not confirmed in the audit). Findings confirmed from the abstract: UV, S and L cones and rods; UV cones contain three opsins and are present in hatchlings and terrestrial adults. Findings the audit could not confirm, because the full text would not open: M and S rods, S cones lost after metamorphosis, "Aquatic salamander retinas are populated mainly by rods", most recordings from large larvae, and a table value of 361 nm. **opened** by the first draft (https://pmc.ncbi.nlm.nih.gov/articles/PMC3997598); the audit read the abstract at https://eye.hms.harvard.edu/publications/coexpression-three-opsins-cone-photoreceptors-salamander-ambystoma-tigrinum.
- Ma, J.-X., Kono, M., Xu, L., Das, J., Ryan, J. C., Hazard, E. S., Oprian, D. D. and Crouch, R. K., 2001. Salamander UV cone pigment: sequence, expression, and spectral properties. *Visual Neuroscience* 18(3): 393 to 399. doi:10.1017/S0952523801183057. Finding: the tiger salamander UV cone pigment absorbs maximally at 356 nm (A1) and 360 nm (A2). **opened** (abstract at https://scholarworks.brandeis.edu/esploro/outputs/journalArticle/Salamander-UV-cone-pigment-Sequence-expression/9923958141301921).
- Korenyak, D. A. and Govardovskii, V. I., 2013. Photoreceptors and visual pigments in three species of newts. *Journal of Evolutionary Biochemistry and Physiology* 49(4): 399 to 407. doi:10.1134/S0022093013040038. Findings: in *Pleurodeles waltl*, *Lissotriton vulgaris* and *Cynops orientalis*, red-sensitive cones peaking at 593 to 611 nm, blue-sensitive at 470 to 489 nm and UV-sensitive at 340 to 359 nm; A2 chromophore dominant. **opened** (abstract via https://dx.doi.org/10.1134/S0022093013040038).
- Martin, M., Théry, M., Rodgers, G., Goven, D., Sourice, S., Mège, P. and Secondi, J., 2016. UV wavelengths experienced during development affect larval newt visual sensitivity and predation efficiency. *Biology Letters* 12(2): 20150954. doi:10.1098/rsbl.2015.0954. Findings: in *Lissotriton vulgaris* larvae, prey survived better without UV during testing; larvae reared without UV captured prey less efficiently, with about 53% lower SWS1 expression. **opened** (https://pmc.ncbi.nlm.nih.gov/articles/PMC4780554).
- Mège, P., Ödeen, A., Théry, M., Picard, D. and Secondi, J., 2016. Partial opsin sequences suggest UV-sensitive vision is widespread in Caudata. *Evolutionary Biology* 43(1): 109 to 118. doi:10.1007/s11692-015-9353-4. Finding: SWS1 sequences recovered in 40 of 58 species from six families (the page does not name the families). **opened** (abstract at https://link.springer.com/article/10.1007/s11692-015-9353-4).
- Przyrembel, C., Keller, B. and Neumeyer, C., 1995. Trichromatic color vision in the salamander (*Salamandra salamandra*). *Journal of Comparative Physiology A* 176(4): 575 to 586. doi:10.1007/BF00196422. Findings: prey-catching sensitivity maxima at 500 and 570 nm with a moving worm dummy on surrounds of equal subjective brightness; three receptor types near 450, 500 and 570 nm; phototaxis maxima at 360 to 400, 520 to 540 and 600 to 640 nm; UV sensitivity "not due to a separate ultraviolet photoreceptor". **opened** (abstract at https://link.springer.com/article/10.1007/BF00196422).
- Aguilar, Pérez i de Lanuza, Martínez-Gil, Dajčman, Simčič, Pinho, Žagar and Megía-Palma, 2024 (initials not checked). Color morphs of the fire salamander are discriminated at night by conspecifics and predators. *Journal of Zoology* 322(2): 141 to 155. doi:10.1111/jzo.13131. Finding: visual models indicate that conspecifics and predators can discriminate red and yellow morphs of *S. s. gallaica* under night light. **opened** (abstract at https://docta.ucm.es/entities/publication/c9d33648-17ba-47d7-8853-e532671c5d66).
- Werner, C. and Himstedt, W., 1984. Eye accommodation during prey capture behaviour in salamanders (*Salamandra salamandra* L.). *Behavioural Brain Research* 12(1): 69 to 73. doi:10.1016/0166-4328(84)90204-3, PMID 6732915. Finding: refraction makes a myopic shift before the salamander turns to prey, so fire salamanders use accommodation for distance estimation. The page lists both authors, while its metadata lists only Himstedt. **opened** (abstract at https://eurekamag.com/research/021/017/021017443.php).
- Wiggers, W., Roth, G., Eurich, C. and Straub, A., 1995. Binocular depth perception mechanisms in tongue-projecting salamanders. *Journal of Comparative Physiology A* 176(3): 365 to 377. doi:10.1007/BF00219062. The page names the first three authors and then "et al.", and shows no issue number, so the fourth author and the issue were not confirmed in the audit. Findings: in tongue-projecting salamanders (Bolitoglossini), frontally oriented eyes; most tectal neurons are activated by the retinal area for the frontal field, which magnifies that region; the two monocular fields of binocular neurons have zero disparity at distances that coincide with the tongue's maximum reach. **opened** (abstract at https://link.springer.com/doi/10.1007/BF00219062).
- Wiggers, W. and Roth, G., 1991. Anatomy, neurophysiology and functional aspects of the nucleus isthmi in salamanders of the family Plethodontidae. *Journal of Comparative Physiology A* 169: 165 to 176. doi:10.1007/BF00215863. Finding: in tongue-projecting plethodontids, isthmo-tectal signals that arrive in the tectum together with the direct ones left the retina 10 to 30 ms earlier, and the authors hypothesize that these time differences are used to calculate three-dimensional trajectories of fast-moving prey. Used only in the open questions. **opened** (abstract at https://link.springer.com/article/10.1007/BF00215863).
- Sanders, R., 3 September 1997. More extreme than chameleons, some salamanders literally shoot their tongues at insects, UC Berkeley scientists discover. UC Berkeley news release. https://newsarchive.berkeley.edu/news/media/releases/97legacy/salamander.html. Findings: one photograph showed a *Hydromantes supramontis* tongue extended almost 6 cm, about 80% of head and body length; "They can flick them out in about a hundredth of a second" is said of these salamanders in general. **opened**. It reports Deban, S. M., Wake, D. B. and Roth, G., 1997. Salamander with a ballistic tongue. *Nature* 389(6646): 27 to 28. doi:10.1038/37898. The audit opened that page (https://www.nature.com/articles/37898): its figure caption names *H. supramontis*, and its preview gives neither the reach nor the time, so both figures rest on the release.
- Kundey, S. M. A., Millar, R., McPherson, J. and colleagues, 2016. Tiger salamanders' (*Ambystoma tigrinum*) response learning and usage of visual cues. *Animal Cognition* 19: 533 to 541. doi:10.1007/s10071-016-0954-9. Findings: salamanders preferred response learning, and in a cross-maze all learned to turn in the direction indicated by a compound visual cue when it alone predicted reward. The abstract does not say where the cue was placed. **opened** (abstract at https://link.springer.com/article/10.1007/s10071-016-0954-9).
- Schülert, N., 2004. *Dynamik und Kontextabhängigkeit in den Antworteigenschaften tectaler Neurone und im Orientierungsverhalten des Salamanders Plethodon shermani durch unterschiedliche Merkmale visueller Stimuli*. Doctoral dissertation, Universität Bremen. Finding: with animated prey dummies, size and velocity were the dominant features. **opened** (English abstract at https://media.suub.uni-bremen.de/handle/elib/1997?locale=en).
- Zug, G. R., 2020. Lungless salamander. *Encyclopaedia Britannica*, published 5 April 2020. https://www.britannica.com/print/article/351606. Findings: nasolabial grooves from lip to nostril, nose tapping, capillary transport of odour particles, odours used for alarm cues and directions to food. **opened**.
- Zug, G. R., 2018. Lateral line system. *Encyclopaedia Britannica*, published 3 May 2018. https://www.britannica.com/print/article/331503. Findings: in amphibians the lateral line occurs only in larvae and wholly aquatic adults, and detects movements and pressure changes in the water. **opened**.
- Keathley, C. M. and Moon, B. R., 2021. Electroreception in amphiuma salamanders. Society for Integrative and Comparative Biology, 2021 virtual annual meeting, abstract 96-5. https://sicb.org/abstracts/electroreception-in-amphiuma-salamanders. Finding: *Amphiuma means* and *A. tridactylum* showed behavioural responses, including likely feeding responses, to low-voltage alternating and direct currents (no field strengths given). This is a meeting abstract and has not been peer reviewed as far as the page shows. **opened**.
- Münz, H., Claas, B. and Fritzsch, B., 1984. Electroreceptive and mechanoreceptive units in the lateral line of the axolotl *Ambystoma mexicanum*. *Journal of Comparative Physiology A* 154(1): 33 to 44. doi:10.1007/BF00605387. Finding: ampullary organs (electroreceptive) and neuromasts (mechanoreceptive) in the head lateral line. **opened** (abstract at https://iro.uiowa.edu/esploro/outputs/journalArticle/Electroreceptive-and-mechanoreceptive-units-in-the/9984070450002771).
- Phillips, J. B. and Borland, S. C., 1992. Behavioural evidence for use of a light-dependent magnetoreception mechanism by a vertebrate. *Nature* 359: 142 to 144. doi:10.1038/359142a0. Finding: magnetic compass orientation in a semiaquatic salamander is affected by the wavelength of light (species and wavelengths not on the page). **opened** (abstract preview at https://www.nature.com/articles/359142a0).
- Phillips, J. B., Deutschlander, M. E., Freake, M. J. and Borland, S. C., 2001. The role of extraocular photoreceptors in newt magnetic compass orientation: parallels between light-dependent magnetoreception and polarized light detection in vertebrates. *Journal of Experimental Biology* 204: 2543 to 2552. Findings: in the newt, compass direction rotated by 90° under light above 500 nm; short-wavelength input from extraocular photoreceptors in or near the pineal organ. **opened** (https://cob.silverchair.com/jeb/article/204/14/2543/32976/The-role-of-extraocular-photoreceptors-in-newt and the PDF at https://cob.silverchair.com/jeb/article-pdf/204/14/2543/1238880/2543.pdf). The 90° rotation is stated in the paper's introduction, and the pineal location in its summary. It cites Deutschlander, M. E., Borland, S. C. and Phillips, J. B., 1999, Extraocular magnetic compass in newts, *Nature* 400: 324 to 325, for long-wavelength caps over the pineal region mimicking whole-animal exposure. **secondary** (through Phillips and colleagues, 2001).
- Navarrete Méndez, M. J., Amini, S. S., Santos, J. C., Saal, J., Wake, M. H., Ron, S. R. and Tarvin, R. D., 2025. Caecilians maintain a functional long-wavelength-sensitive cone opsin gene despite signatures of relaxed selection and more than 200 million years of fossoriality. *Evolution* 79(12): 2756 to 2775. doi:10.1093/evolut/qpaf190. Findings: reduced eyes covered by skin or bone; LWS intact; SWS1 and SWS2 lost; no conclusive evidence of cone cells; light intensity and spectra "may be the only visual information available to caecilians". The published abstract holds the first, second and fourth of these; the loss of SWS1 and SWS2 and the quoted sentence come from the preprint, the quotation from its Discussion, where it is offered as interpretation. **opened** (record and abstract excerpts at https://researchcollaborations.elsevier.com/en/publications/caecilians-maintain-a-functional-long-wavelength-sensitive-cone-o/, and the full bioRxiv preprint, doi:10.1101/2025.02.07.636964, at https://www.biorxiv.org/content/10.1101/2025.02.07.636964.full.pdf).
- AmphibiaWeb. *Proteus anguinus* Laurenti, 1768. Account by B. Bulog and A. van der Meijden, 1999, edited by K. Whittaker and M. S. Koo, 2024. https://amphibiaweb.org/species/4229. Findings: regressed eye with visual pigments; skin sensitive to light through melanopsin in melanophores; reduced pineal organ with degenerated photosensitive cells. **opened**. It cites Kos, M., Bulog, B., Szél, A. and Röhlich, P., 2001, Immunocytochemical demonstration of visual pigments in the degenerate retinal and pineal photoreceptors of the blind cave salamander (*Proteus anguinus*), *Cell and Tissue Research* 303(1): 15 to 25. **secondary** (through AmphibiaWeb).
- GBIF.org occurrence API, dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7, read 12 October 2026. Order keys from https://api.gbif.org/v1/species/match (Caudata 953, Gymnophiona 775). Facets: Caudata by family and by species, total 631,944. Names from https://api.gbif.org/v1/species/{key}. **opened**.
- This repository: `src/cam.a.js`, `src/cam.r.js`, `tools/species/eyes.py`, `docs/VIEWS.md`, `docs/views/world-orders.csv`, `docs/views/no-view-us-fl-alachua.csv`. Findings: engine fields, existing entries, routing, order totals and the Alachua species. **opened**.

## 6. Open questions for a sensory scientist

1. Does any terrestrial salamander, the Eastern Red-backed Salamander above all, strike at prey that keeps still, by sight alone? The answer decides `gate`, and this sheet leaves it off on the strength of one maze study.
2. What do the eyes of the Eastern Red-backed Salamander and the Eastern Newt resolve, in cycles per degree, and how wide is their field? Every sharpness and field value here is invented.
3. Do the lungless salamanders, the largest family, carry separate ultraviolet cones as the tiger salamander and newts do, or ultraviolet sensitivity through another receptor as the fire salamander does?
4. How fast do salamander photoreceptors follow flicker, and how much dimmer than you can a nocturnal salamander still see? Either answer would set `rate` or `gain`.
5. In the tongue-shooters, signals that reach the brain's tectum by way of the nucleus isthmi left the retina 10 to 30 milliseconds before the direct signals they arrive with (Wiggers and Roth, 1991). Is depth at the tongue's reach judged by the two eyes' disparity alone, and does the same hold for the red-backed salamander, which sits outside that tribe (no source was opened for its tribe)?
