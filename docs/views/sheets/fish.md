# Fish: sensing sheet

Status on 11 October 2026: this sheet was written after about two hours of work, well past the 40 minutes in the brief. Three things are unfinished. No cone peaks or flicker rate were found for the Bluegill itself. No sharpness or field figure was found for sharks or rays. The physics textbook page (OpenStax) could not be opened, so the Snell's window figure rests on a journal paper and two teaching pages from physics bodies. Some pages were refused: PubMed and PubMed Central (a browser check), one Springer page and one Europe PMC query (rate limit), a Frontiers paper (server error), and Crossref and HyperPhysics (permission requests that timed out). The GBIF API was blocked for curl but opened through WebFetch.

Audited on 12 October 2026. The corrections are listed in `fish.audit.md`. The mirror outside Snell's window lost its source and was taken out of the rows, the second reef fish in the sharpness comparison turned out to be a dottyback, and the split of sharks with and without cones rests on the publisher's press release, since the paper's abstract does not give it.

## 1. Scope

**Taxa.** The view covers all fish: ray-finned fish, sharks, rays, chimaeras, lungfish, coelacanths, lampreys and hagfish. The figures are iNaturalist research-grade records in GBIF, read on 11 October 2026: 2,763,409 records (1.63% of all records), across 63 orders.

**What people photograph.** Perciformes holds 1,624,091 records, 58.8% of all fish records. GBIF's backbone keeps the old, wide Perciformes, so the reef families sit inside it. Family facets of that order and of the carp order give these counts:

| Family | Records | Share of fish records |
|---|---:|---:|
| Centrarchidae (sunfish and black bass) | 188,208 | 6.8% |
| Cyprinidae (carp and minnows; order Cypriniformes) | 186,903 | 6.8% |
| Labridae (wrasses) | 176,484 | 6.4% |
| Pomacentridae (damselfish, clownfish) | 155,557 | 5.6% |
| Gobiidae (gobies) | 85,468 | 3.1% |
| Chaetodontidae (butterflyfish) | 85,395 | 3.1% |
| Serranidae (groupers) | 80,379 | 2.9% |
| Acanthuridae (surgeonfish) | 71,703 | 2.6% |
| Sparidae (sea breams) | 67,886 | 2.5% |
| Percidae (perch, darters) | 66,855 | 2.4% |
| Scaridae (parrotfish) | 57,628 | 2.1% |
| Blenniidae (combtooth blennies) | 54,088 | 2.0% |

- **Reef and rocky shore.** Eight mostly marine families of reefs and rocky shores (wrasses, damselfish, gobies, butterflyfish, groupers, surgeonfish, parrotfish and blennies) hold 766,702 records together, which is 27.7% of fish records.
- **Freshwater sunfish and perch** hold 255,063 records (9.2%).
- **By species**, the Bluegill leads Perciformes with 46,903 records. That is 1.7% of all fish records and more than three times the next species. After it come the Green Sunfish (14,919), Pumpkinseed (14,288), Smallmouth Bass (13,967), Moorish Idol (8,917), European Perch (8,687), Sergeant Major (8,632) and Yellow Perch (8,354).
- **Carp.** Outside Perciformes, only the carp order was ranked by species. The Common Carp leads it with 22,616 records, ahead of the Creek Chub with 10,914. Of the species ranked for this sheet, the Common Carp is second only to the Bluegill. Species in the other orders were not ranked.
- **In short**, the commonest photographed fish are freshwater sunfish led by the Bluegill, the carp family led by the Common Carp, and reef fish of eight families. The counts do not record whether a fish was photographed from above the water or under it.
- **Other large orders** are Cypriniformes (carp and minnows, 7.7%), Tetraodontiformes (pufferfish and triggerfish, 6.5%) and Scorpaeniformes (4.0%).
- **Cartilaginous fish.** Sharks hold 60,349 records (2.2%), rays 70,277 (2.5%) and chimaeras 1,769.
- **The rest.** Lampreys, hagfish, lungfish and the coelacanth hold 2,087 records together (0.08%).
- **Alachua County.** In the one region built so far, the 60 recorded fish species are almost all freshwater fish. The most recorded are the Eastern Mosquitofish, the Bluegill and the Florida Bass. The county list files the Florida Bass under Micropterus salmoides, the species whose cones are given in section 2.

**Can one view be true?** It cannot. Two lines divide the group.

- **Sharks against the rest.** Every shark studied so far has one cone type, or none that could be found. The bony fish measured here have two cone types (Largemouth Bass) or four (clownfish, goldfish). Sharks and rays also feel electric fields. In one survey, cartilaginous fish follow flicker at 26 a second on average, against 46 for bony fish. A colour picture is false for a shark, and a grey picture is false for every bony fish measured here.
- **Colour within the bony fish.** The Largemouth Bass has two cone types, with none for blue or ultraviolet. The clownfish has four, one of them ultraviolet. Sharpness gives no clean line, because it was measured in different ways. By behaviour, the Bluegill resolves about 5 cycles per degree and the Pumpkinseed 3.6, against 1.3 to 1.7 in two reef fish, the Ambon Damselfish and a dottyback (Pseudochromis fuscus). By the spacing of cells in the retina, the same two reef fish come to 3.2 to 4.6, and the Bluegill's cones predict 3.4 to 6.7. The optics of a flat water surface are the same for every fish.

**Recommendation.** Two views are needed.

- **`fish`** covers the ray-finned fish (2,628,927 records). Lampreys, hagfish, lungfish and the coelacanth (2,087 records) ride along with it, unchecked. Together that is 2,631,014 records, 95.2% of fish records.
- **`shark and ray`** covers sharks, rays and chimaeras: 132,395 records, 4.8% of fish records. It is sketched at the end of section 2.

The commonest fish are on the `fish` side, and `fish` should be drawn for a sunfish, for four reasons:

1. The sunfish family is the largest single family of fish records, 1,305 records ahead of the carp family. No family in another order can pass it, because every order other than these two holds fewer records than the sunfish family alone (the next, Tetraodontiformes, holds 180,531).
2. The Bluegill is the most recorded species in the largest order by a factor of three.
3. The colour and sharpness used here were measured in sunfish themselves: the Largemouth Bass belongs to the sunfish family, and so do the Bluegill and the Pumpkinseed.
4. In Alachua County, the one region built so far, the sunfish family holds 319 of the 1,028 fish records, the most of any family. The livebearers, which include the Eastern Mosquitofish, come next with 309.

The reef families together outnumber the sunfish, and the carp family is nearly as large and includes the goldfish, which has an ultraviolet cone. However, colour vision in the reef families was measured here only in the clownfish, and the app draws ultraviolet only as invented colour, so the reef difference becomes an `x` row. A reef-fish entry with its own colour matrix can follow later as a second entry, and it needs no new engine fields.

## 2. The rows

For `fish`:

['m', 'Sharpness', 'A bluegill resolves about 5 cycles per degree and a pumpkinseed about 3.6, against your 60. The screen is blurred to what such an eye would keep of it.']
Source: Northmore, Oh and Celenza 2007 (Bluegill, behavioural cutoff about 5 c/°); Spratte and colleagues 2021 (Pumpkinseed, 3.6 c/°).

['m', 'Colour', 'Largemouth bass have two cone types, near 535 and 614 nanometres, and none for blue. Trained bass confused blue with black and yellow-green with white, so here blue goes dark and yellow goes pale.']
Source: Mitchem and colleagues 2019 (single cones 535 nm, twin cones 614 nm; chartreuse confused with white and blue with black).

['g', 'Field', 'A golden shiner sees about 335 degrees around itself, 31 of them with both eyes, and is blind only in a wedge of 25 degrees behind. The camera holds a slice of it, and the rest is invented.']
Source: Pita and colleagues 2015 (Golden Shiner: visual coverage 335°, binocular field 31°, blind area 25°).

['g', 'Where it is sharp', 'A golden shiner sees most sharply a little ahead and above, at 2.9 cycles per degree, and at 1.2 toward the edges. The sharp spot is drawn at the centre.']
Source: Pita and colleagues 2015 (peak 2.86 c/°, periphery 1.18 c/°; the dense patch of retina looks forward and upward).

['g', 'Pace', 'A spiny damselfish follows flicker to 89 a second, and the bony fish in one survey average 46. You stop near 60, so the picture keeps your pace.']
Source: Chung and colleagues 2014 (Spiny Damselfish, 89.0 Hz by flicker electroretinogram); Inger and colleagues 2014 (bony fish mean 45.9 Hz).

['x', 'Looking up', 'Under calm water the whole sky is squeezed into a circle about 97 degrees across. The picture leaves it out for now.']
Source: Sabbah and colleagues 2006 (window about 97.5° across, with the whole sky compressed into it; edge at 48.75° from the vertical for n = 1.33); IOPSpark (a cone of 97°); University of Arizona optics outreach (a 97 degree cone). This is optics, and it holds for any eye under a flat surface. Grade it `m` once the window is drawn (section 4, item 1).

['x', 'Water moving', 'Sensors along the body feel the flow and pressure of the water, and fish steer by them in the dark. The picture leaves it out.']
Source: Zhai, Zheng and Xie 2020 (superficial neuromasts sense flow direction and speed; canal neuromasts sense pressure gradients; used to manoeuvre in darkness).

['x', 'Ultraviolet', 'Clownfish and goldfish have a cone for it, and a clownfish tells colours apart better with it. Bass have none, and the picture leaves it out.']
Source: Mitchell and colleagues 2024 (Clownfish cones near 386, 497, 515 and 535 nm; finer colour discrimination with ultraviolet contrast); Joselevitch, de Souza and Ventura 2010 (goldfish have an ultraviolet photoreceptor); Mitchem and colleagues 2019 (bass: two cone types only).

For `shark and ray`, as a sketch for a later sheet:

['g', 'Colour', 'Every shark studied so far has one cone type, or none that could be found, so the picture is drawn in light and dark only. Rays have two or three cone types, so for them this picture holds too little colour.']
Source: Hart and colleagues 2011 (17 shark species, each with only a single long-wavelength cone type; the split of 7 species with cones and 10 with none found comes from the publisher's press release); Hart and colleagues 2020 (sharks are cone monochromats, rays dichromats); Hart, Lisney, Marshall and Collin 2004 (three cone pigments in two shovelnose rays).

['g', 'Pace', 'Sharks, rays and their relatives in one survey follow flicker at 26 a second on average, under half your rate, so movement smears into trails.']
Source: Inger and colleagues 2014 (cartilaginous fish mean 26.1 Hz).

['x', 'Electric fields', 'Sharks and rays feel the faint electric field of living prey, and can find a flatfish buried in sand by it at night. The picture leaves it out.']
Source: Kalmijn 1971 (flatfish covered with sand found by their bioelectric fields); "at night" from Hopkins in a JEB Classics essay on it.

['x', 'Looking up', 'Under calm water the whole sky is squeezed into a circle about 97 degrees across. The picture leaves it out for now.']
Source: as for `fish`.

['i', 'Field and sharpness', 'Both are guesses, copied from the bony fish.']
Source: none.

## 3. The picture

`fish`:

| Field | Value | Behind it |
|---|---|---|
| `fov` | 335 | The field row gives 335° for the Golden Shiner (Pita and colleagues 2015). The engine shrinks the camera picture to 0.54 of the screen (180/335) and barrel-distorts the invented rest. |
| `cpd` | 4 | The sharpness row gives about 5 for the Bluegill and 3.6 for the Pumpkinseed. The value 4 lies between them, and the exact choice is `invented`. |
| `topoA` | 1 | The row on where it is sharp gives one dense area in the Golden Shiner. The patch looks ahead and above, and placing it at the centre is `invented`. |
| `fall` | 1.4 | The same row makes the edge 2.86/1.18 = 2.4 times coarser than the peak. The engine multiplies the blur by (1 + `fall`) at half the frame's height from the centre of a central spot, so `fall` = 1.4. The mapping is the engine's own convention. |
| `pupil` | 'o' | This is `invented`, since no source on fish pupils was opened. With `dof` at 0 the shape is not seen. |
| `dof` | not set (0) | This is `invented`, since no source was found. |
| `M` | [1, 0, 0, 0, 1, 0, 0, 1, 0] | This follows the colour row (Mitchem and colleagues 2019). The engine reads the matrix by rows, so the blue channel is replaced by green: pure blue goes to black and yellow goes to white, matching the two confusions the trained bass made. Green turns toward cyan as a side effect. The matrix is `invented`. A published simulation of human vision without the blue cone could replace it. |
| `sat` | 1 (default) | Nothing measured calls for a change. |
| `gain` | 1 (default) | No source on dim light was found. |
| `sheen`, `uvBlue` | 0 | The ultraviolet row says bass have no ultraviolet cone. |
| `rate` | 1 (default) | The pace row shows the measured bony fish straddling 60 (damselfish 89, survey mean 46). For a reef-fish entry, 60/89 = 0.67 would follow the damselfish. Keeping 1 for the `fish` view is `invented`. |
| `persist`, `gate`, `hold`, `thrust`, `fovea`, `topoS`, `field`, `noGreen` | not set | Nothing calls for them. |

Proposed entry:

```
fish: { chip: 'Fish', who: 'a fish', fov: 335, cpd: 4, topoA: 1, fall: 1.4, pupil: 'o', M: [1, 0, 0, 0, 1, 0, 0, 1, 0],
  cue: 'Detail is coarse and the field is wide. Blue goes dark and yellow goes pale.', rows: [ /* section 2 */ ] }
```

`shark and ray`, as a sketch:

| Field | Value | Behind it |
|---|---|---|
| `sat` | 0 | The colour row says sharks have one cone type or none. Applying it to rays is `invented`. |
| `persist` | .04 | The pace row gives 1/26.1 seconds. This follows the frog entry, where .15 equals 1/6.7 for the cane toad. |
| `fov` | 335 | This is `invented`, copied from `fish`. |
| `cpd` | 4 | This is `invented`, copied from `fish`. Without a value the engine would draw a person's 60. |
| `pupil` | 'o' | This is `invented`. |

```
shark: { chip: 'Shark, ray', who: 'a shark or ray', fov: 335, cpd: 4, pupil: 'o', sat: 0, persist: .04,
  cue: 'There is light and dark only, and movement leaves trails.', rows: [ /* section 2 */ ] }
```

## 4. What the engine cannot draw yet

1. **Looking up through the surface (Snell's window).**
   - What it shows: when the phone points upward, the whole scene above is pressed into a circle about 97 degrees across. A ray at angle θ from the vertical in air arrives at arcsin(sin θ / 1.33) under water. What lies outside the circle has no source yet, since the Arizona page says only that light at the critical angle is completely reflected.
   - Phone input: the motion sensors give the phone's tilt, and the camera gives the scene. A phone camera covers about 70 degrees (the figure `docs/SOURCES.md` already uses), which fills only the central 51 degrees of the 97 degree circle (arcsin(sin 35° / 1.33) = 25.5°, doubled). The rest of the circle would be stretched from the edges, as the wide-field trick does now. The ring outside the circle could reuse the lower part of the frame, which is `invented`.
   - Judgement: this is moderate work, one remapping pass in the shader and a tilt reading.
2. **The lateral line (water flow and pressure along the body).**
   - What it shows: nearby things moving, felt as pressure on one side, and the fish's own movement through the water.
   - Phone input: nothing on a phone senses the medium around it. Optical flow from the camera (large nearby movement) is the nearest stand-in. It could be shown as shading along the edge of the screen nearest the movement, or given out through the vibration motor where the browser allows it. The accelerometer could stand in for the fish's own movement.
   - Judgement: a true version is hard, and a suggestive version from optical flow is moderate work.
3. **Ultraviolet, for a later reef-fish or carp entry.**
   - What it shows: patterns on fish that only an ultraviolet cone separates.
   - Phone input: no phone input records it, so any drawing is invented colour, as for bees and birds. One finding for the repository: `docs/SOURCES.md` backs "Ultraviolet cannot be recorded by an ordinary camera" with the University of Sussex page on Vasas and colleagues 2024, and a reading of that page on 11 October found no such statement. The audit on 12 October confirmed this: the page says the new system records blue, green, red and ultraviolet together and is built from commercially available cameras, and it nowhere says what an ordinary camera cannot record. That claim needs another source.
   - Judgement: the camera cannot supply it.
4. **Contrast.**
   - What it shows: a Bluegill needs about 3% contrast even at its best spatial frequency, 0.4 cycles per degree (Northmore and colleagues 2007). Low-contrast detail would vanish before fine detail does.
   - Phone input: the camera alone is enough. The engine has blur but no field for contrast loss, so this needs a contrast curve by spatial frequency.
   - Judgement: this is moderate work, one more term in the shader.
5. **The electric sense (`shark and ray`).**
   - What it shows: the faint fields around living bodies, strongest at close range.
   - Phone input: none senses bioelectric fields. A glow on bodies the recognizer finds would be wholly invented.
   - Judgement: no phone can sense it.

## 5. Sources

- GBIF occurrence search, iNaturalist research-grade dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7, read 11 October 2026: family and species facets for Perciformes (orderKey 587) and for Cypriniformes (orderKey 1153), for example https://api.gbif.org/v1/occurrence/search?datasetKey=50c9509d-22c7-4a22-a47d-8c48425ef4a7&orderKey=587&facet=familyKey&limit=0. Family and species names came from https://api.gbif.org/v1/species/{key} for each key used. Keys 2394503 (Bluegill) and 2394494 (Green Sunfish) were named from the repository's `docs/views/no-view-us-fl-alachua.csv`. The order counts came from `docs/views/world-orders.csv`. `opened`
- Northmore DPM, Oh D-J, Celenza MA, 2007. Acuity and contrast sensitivity of the bluegill sunfish and how they change during optic nerve regeneration. Visual Neuroscience 24(3): 319–331. doi:10.1017/S0952523807070307. Behavioural acuity cutoff about 5 c/°; cone spacing predicts 3.4 to 6.7 c/°; contrast sensitivity peaks at 0.4 c/° with a minimum threshold of 0.03. `opened` (abstract)
- Spratte C, Sandow L-M, Schnermann JS, Hanke FD, 2021. Single target acuity in the common sunfish (Lepomis gibbosus). Journal of Experimental Biology 224: jeb243068. doi:10.1242/jeb.243068. Pumpkinseed grating-equivalent acuity 3.6 ± 0.5 c/°; the paper cites 3 to 5.5 c/° for the Bluegill. `opened`
- Mitchem LD, Stanis S, Zhou M, Loew E, Epifanio JM, Fuller RC, 2019. Seeing red: color vision in the largemouth bass. Current Zoology 65(1): 43–52. doi:10.1093/cz/zoy019. Single cones 535 nm, twin cones 614 nm, rods 528 nm; dichromatic; trained bass confused chartreuse with white and blue with black. `opened`
- Pita D, Moore BA, Tyrrell LP, Fernández-Juricic E, 2015 (the order was confirmed on the PeerJ PDF in the audit). Vision in two cyprinid fish: implications for collective behavior. PeerJ 3: e1113. doi:10.7717/peerj.1113. Golden Shiner: visual coverage 335° in the horizontal plane (333° averaged across elevations), binocular field 31°, blind area 25°; acuity 2.86 c/° at the peak and 1.18 at the periphery; the area of high density lies in the ventro-temporal retina, looking forward and up. `opened`
- Sabbah S, Barta A, Gál J, Horváth G, Shashar N, 2006. Experimental and theoretical study of skylight polarization transmitted through Snell's window of a flat water surface. Journal of the Optical Society of America A 23(8): 1978–1987. https://arago.elte.hu/sites/default/files/SnellPol_JOSAA.pdf. Aperture about 97.5°, with the whole sky compressed into it; edge at arcsin(1/n) = 48.75° for n = 1.33. `opened`
- Institute of Physics, IOPSpark, "Snell's window". https://spark.iop.org/snells-window. A fish sees the whole hemisphere above the water in a cone of 97°. `opened`
- University of Arizona Wyant College of Optical Sciences, Outreach, "Snell's Window". https://wp.optics.arizona.edu/oscoutreach/snells-window. A 97 degree cone; at the critical angle, light is completely reflected (the page says nothing about angles beyond it). `opened`
- Chung W-S, Marshall NJ, Watson S-A, Munday PL, Nilsson GE, 2014. Ocean acidification slows retinal function in a damselfish through interference with GABAA receptors. Journal of Experimental Biology 217: 323–326. doi:10.1242/jeb.092478. Spiny Damselfish (Acanthochromis polyacanthus): maximal flicker frequency 89.0 ± 1.6 Hz in controls by flicker electroretinogram. `opened`
- Inger R, Bennie J, Davies TW, Gaston KJ, 2014. Potential biological and ecological effects of flickering artificial light. PLoS ONE 9(5): e98631. doi:10.1371/journal.pone.0098631. Mean flicker fusion 26.1 Hz in cartilaginous fish and 45.9 Hz in bony fish, with every bony fish under 100 Hz. `opened`
- Zhai Y, Zheng X, Xie G, 2020. Fish lateral line inspired perception and flow-aided control: a review. arXiv:2006.12443. https://arxiv.org/abs/2006.12443. Superficial neuromasts sense flow direction and speed; canal neuromasts sense pressure gradients; the lateral line serves manoeuvring in darkness. `opened`
- Mitchell L, Phelan A, Cortesi F, Marshall J, Chung W-S, Osorio D, Cheney K, 2024. Ultraviolet vision in anemonefish improves color discrimination. Dryad dataset doi:10.5061/dryad.wwpzgmsp9, with the preprint at bioRxiv doi:10.1101/2022.12.01.518784. Clownfish (Amphiprion ocellaris, family Pomacentridae in GBIF) cones near 386 (ultraviolet), 497, 515 and 535 nm; all four used for colour; finer discrimination with ultraviolet contrast. `opened` (dataset abstract and preprint; the published journal version was not opened, and in the audit its PubMed Central page, PMC11057877, timed out and the preprint page refused the request)
- Joselevitch C, de Souza JM, Ventura DF, 2010. No evidence of UV cone input to mono- and biphasic horizontal cells in the goldfish retina. Journal of Comparative Physiology A 196: 913–925 (the issue number was not confirmed). doi:10.1007/s00359-010-0574-9. The goldfish has an ultraviolet photoreceptor and pronounced ultraviolet sensitivity; the abstract names the ultraviolet and M cones and refers to "the other three cone types". `opened` (abstract)
- Hart NS, Theiss SM, Harahush BK, Collin SP, 2011. Microspectrophotometric evidence for cone monochromacy in sharks. Naturwissenschaften 98(3): 193–201. doi:10.1007/s00114-010-0758-8. Seventeen shark species were examined; cone pigments peak at 532 to 561 nm; each shark has only a single long-wavelength-sensitive cone type, which suggests sharks may be cone monochromats. `opened` (abstract on the Springer page, opened in the audit). The split of 7 species with cones and 10 with none observed is not in the abstract and rests on a press release: `secondary` (ScienceDaily, dated 19 January 2011 on the page and credited to Springer Science+Business Media, https://sciencedaily.com/releases/2011/01/110118092224.htm)
- Hart NS, Lamb TD, Patel HR, Chuah A, Natoli RC, Hudson NJ, Cutmore SC, Davies WIL, Collin SP, Hunt DM, 2020. Visual opsin diversity in sharks and rays. Molecular Biology and Evolution 37(3): 811–827. doi:10.1093/molbev/msz269. All shark species studied appear to be cone monochromats; rays have dichromatic colour vision from RH2 and LWS opsins. `opened` (abstract, University of Western Australia repository)
- Hart NS, Lisney TJ, Marshall NJ, Collin SP, 2004. Multiple cone visual pigments and the potential for trichromatic colour vision in two species of elasmobranch. Journal of Experimental Biology 207(26): 4587–4594. doi:10.1242/jeb.01314. The author order, year, pages and DOI were confirmed on the journal page in the audit. Cones at 477, 502 and 561 nm in the Giant Shovelnose Ray, and at 459, 492 and 553 nm in the Eastern Shovelnose Ray. `opened` (journal page)
- Kalmijn AJ, 1971. The electric sense of sharks and rays. Journal of Experimental Biology 55(2): 371–383. Sharks and rays located flatfish covered with sand by their bioelectric fields, with sight, smell and mechanical cues ruled out. `opened` (abstract, opened in the audit). "At night" comes from the commentary: `secondary` (Hopkins CD, "A biological function for electroreception in sharks and rays", JEB Classics, Journal of Experimental Biology 213: 1005–1007, with the volume and issue (213, 7) read from the PDF address and the year, 2010, inferred from the volume, doi:10.1242/jeb.034439, `opened`)
- Parker AN, Fritsches KA, Newport C, Wallis G, Siebeck UE, 2017. Comparison of functional and anatomical estimations of visual acuity in two species of coral reef fish. Journal of Experimental Biology 220: 2387–2396. doi:10.1242/jeb.149575. Ambon Damselfish (Pomacentrus amboinensis) 1.29 to 1.36 c/° by behaviour and 4.1 to 4.6 by anatomy; the dottyback Pseudochromis fuscus 1.61 to 1.71 and 3.2 to 3.6. Used in section 1 only. `opened`
- Caves EM, Sutton TT, Johnsen S, 2017. Visual acuity in ray-finned fishes correlates with eye size and habitat. Journal of Experimental Biology 220(9): 1586–1596. doi:10.1242/jeb.151183. An acuity database of 159 ray-finned species, in which eye size is the main factor. Used for open question 1 only. `opened` (abstract)

## 6. Open questions

1. Does the Bluegill share the Largemouth Bass's two cones near 535 and 614 nm, or does it keep a short-wavelength or ultraviolet cone? The colour of the whole view rests on the bass. A related question: since acuity in fish follows eye size, is a single `cpd` of 4 fair for fish photographed at very different sizes?
2. Is copying the green channel into blue a fair way to show a 535 and 614 nm dichromat to a human viewer, given that the bass's long cone sits much further into the red than a human's?
3. What flicker rate does a sunfish or bass reach in daylight? The bony fish measured so far straddle 60.
4. Should the reef families (27.7% of fish records or more) get their own colour picture? Which cone set is typical across wrasses, damselfish, butterflyfish and surgeonfish?
5. Where should lampreys and hagfish go? They hold 0.07% of fish records, and their eyes were not checked for this sheet.
