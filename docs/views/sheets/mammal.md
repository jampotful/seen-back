# Sensing sheet: mammal (the mammals without a view of their own)

This sheet was written on 12 October 2026, from 14:05 to 14:46 EDT, inside a 50 minute limit, and audited from 14:51 to 15:34 EDT (see `mammal.audit.md`). The audit reworded four rows and corrected the `cpd` span, two source lines and one scope heading. It could not confirm the authors of the tapetum paper or the ranked Alachua list. Unfinished items are marked **[unfinished]**, and they are these:

- **Elephant colour.** I could not open Yokoyama and colleagues (2005) on elephant cone pigments. The PubMed page came back empty, Europe PMC refused with a rate limit (HTTP 429), and PMC showed a browser check. No elephant colour row is written.
- **Raccoon cone peak.** Jacobs and Deegan (1992) say the raccoon is monochromatic, and the peak wavelength sits behind the paywall.
- **Not found or not searched.** I found nothing on the koala, the quokka, or red and grey kangaroo cones, and nothing on the acuity of raccoons, opossums, bears or pigs. I did not search hedgehogs, shrews, hyenas, mongooses, civets, skunks or badgers. I found no field-of-view or flicker-fusion measurement for any member.
- **Pages refused.** These pages were refused, so their findings are missing or second-hand:
  - Europe PMC (three requests): rate limit.
  - Wiley, for Peichl, Behrmann and Kröger (2001): permission withdrawn.
  - The Royal Society, for Jacobs (2009): permission withdrawn.
  - PubMed 9720112, the platypus sensory review: permission withdrawn.
  - Cambridge, for the black rhinoceros retina paper: permission withdrawn.
  - Wikipedia's raccoon article: permission withdrawn.
  - PMC, for Ebeling and colleagues (2010): browser check. That paper was read through the ANU repository instead.
- **Unsourced statements.** The rows "Electric sense" and "Snout" say that no phone senses electric fields and that a camera records neither touch nor smell. I opened no source for either statement.

## 1. Scope

**What the group holds.** The group holds 1,019,965 iNaturalist research-grade records in GBIF (read 11 October 2026, from the assignment). By order:

| Order | Members | Records | Share |
|---|---|---:|---:|
| Carnivora (this group only) | raccoons, bears, weasels, otters, skunks and others | 444,045 | 43.5% |
| Diprotodontia | kangaroos, wallabies, koalas, possums, wombats | 176,478 | 17.3% |
| Artiodactyla (this group only) | pigs, peccaries, hippos | 79,123 | 7.8% |
| Didelphimorphia | opossums | 66,183 | 6.5% |
| Soricomorpha | moles and shrews | 50,373 | 4.9% |
| Erinaceomorpha | hedgehogs | 47,324 | 4.6% |
| Cingulata | armadillos | 34,702 | 3.4% |
| Proboscidea | elephants | 28,818 | 2.8% |
| Monotremata | platypus, echidnas | 23,545 | 2.3% |
| Pilosa | sloths, anteaters | 22,555 | 2.2% |
| Perissodactyla | rhinos, tapirs | 14,082 | 1.4% |
| Other orders | | 32,737 | 3.2% |

**Most recorded species.** I read three species counts from the GBIF API on 12 October 2026:

- Common Raccoon (*Procyon lotor*): 135,489 records (13.3%).
- Virginia Opossum (*Didelphis virginiana*): 54,547 records (5.3%).
- American Black Bear (*Ursus americanus*): 54,505 records (5.3%).

In Alachua County the five most recorded are the Common Raccoon, the Virginia Opossum, the Eurasian Wild Pig, the North American River Otter and the Eastern Mole. **[unfinished]** The audit could not confirm this ranking: `docs/VIEWS.md` names only the top three species in each proposed view, and the county's CSV was not opened.

**One view cannot be true for the commonest members.** The commonest members split on colour, which the picture draws on every frame.

- **One kind of cone.** The raccoon and the kinkajou are monochromatic by electroretinogram (Jacobs and Deegan, 1992). The Virginia opossum showed a single cone pigment near 561 nm and no sign of a second (Jacobs and Williams, 2010). Raccoons and opossums together hold 18.6% of the group's records and are the two most recorded members in Alachua.
- **Cones lost.** The nine-banded armadillo and the sloths carry broken copies of genes that every cone needs (Emerling and Springer, 2015). Anteaters have lost the blue-sensitive cone, and their other cone is untested. The Chinese pangolin has lost the blue-sensitive cone and kept the other.
- **Two kinds of cone.** The domestic pig has two (439 and 556 nm; Neitz and Jacobs, 1989). The American black bear has both cone types (Heyward and colleagues, 2021), and genes predict both in the sea otter and the polar bear (Levenson and colleagues, 2006). The coati, a raccoon relative active by day, has a second cone near 433 nm (Jacobs and Deegan, 1992). The tammar wallaby has "only two cone types" (Ebeling and colleagues, 2010). A student summary of Peichl and colleagues (2005) reports both cone types in brown bears (secondary).
- **Light and dark only.** The eastern mole's eyes lie under skin, and its sight goes no further than light and dark (Slonaker; Animal Diversity Web).
- **Electric sense.** The platypus finds and avoids objects by weak electric fields (Scheich and colleagues, 1986). Monotreme cone pigments come from two gene families (Jacobs, 2013), so their colour sits on the two-cone side.

A single two-cone view would be untrue in colour for the raccoon, the opossum, the armadillos, the sloths and the anteaters. A single grey view would be untrue for bears, otters, pigs, kangaroos and the platypus. Neither would be true for moles, which have no picture at all.

**Recommendation.** Build three entries, split by how the eye takes in colour.

1. **`mammal`** covers members with two kinds of cone. These are bears, otters, weasels, skunks, badgers, mongooses, hyenas, civets, coatis, kangaroos, wallabies, koalas, possums, wombats, pigs, peccaries, hippos, rhinos, tapirs, elephants, the platypus and echidnas. Many of these are unmeasured and ride on their relatives. The Eurasian Wild Pig and the River Otter fall here.
2. **`raccoon`** covers members with one kind of cone or none. These are raccoons (*Procyon*), the kinkajou (*Potos*), the opossums (order Didelphimorphia), armadillos (Cingulata), sloths and anteaters (Pilosa) and pangolins (Pholidota). The commonest member of the whole group falls here. Jacobs and Williams (2010) say that genes in two South American marsupials predict two cone pigments, so other opossums may belong in `mammal`. The order goes to `raccoon` because the Virginia opossum holds 82% of its records.
3. **`mole`** covers family Talpidae. It takes the picture that `other` already draws (light and dark, no image) and adds its own rows.

Shrews (Soricidae) and hedgehogs (Erinaceidae) stay in `other` until someone finds a source. `tools/species/eyes.py` would route the families and orders named above, and the coati (*Nasua*) goes to `mammal`. No file was changed.

## 2. The rows

### `mammal` (two kinds of cone)

```
['m', 'Colour', 'A domestic pig has two kinds of colour sensor, most sensitive near 439 and 556 nanometres, and you have three. We show colours the way a person with only two kinds sees them.'],
```
Source: Neitz and Jacobs, 1989. Electroretinogram flicker photometry in the domestic pig found two cone classes at about 439 and 556 nm.

```
['m', 'Bears and otters', 'An American black bear has a blue-sensitive cone and a red-green one, with at least three red-green cones to each blue. Sea otters carry genes for the same pair.'],
```
Source: Heyward and colleagues, 2021: "L/M cones outnumber S cones by at least 3:1". Levenson and colleagues, 2006: sea otter short-wavelength cones near 440 nm and middle-to-long cones at 545 to 560 nm, inferred from genes.

```
['m', 'Kangaroos', 'The tammar wallaby, a small kangaroo, has only two kinds of cone. Some other Australian marsupials have a third.'],
```
Source: Ebeling, Natoli and Hemmi, 2010. They confirmed "only two cone types" in the tammar. In the fat-tailed dunnart, 20 to 25% of cones were unlabelled, which points to a third type. The quokka, quenda, honey possum and fat-tailed dunnart had earlier been described as trichromatic.

```
['g', 'Platypus and echidnas', 'The platypus and echidnas carry genes for two kinds of cone pigment, as most mammals do.'],
```
Source: Jacobs, 2013 (abstract). Cone pigments come from "SWS2 and LWS in monotremes", and most mammals have two cone types.

```
['m', 'Sharpness', 'A tammar wallaby resolves about 4.8 cycles per degree, a twelfth of your 60. A western grey kangaroo’s retina could carry about 11. We blur the picture to about 5.'],
```
Source: Hemmi and Mark, 1998: behavioural acuity "about 4.8 cycles/deg", anatomical limit about 6. Veilleux and Kirk, 2014: western grey kangaroo 11.2 cycles per degree, an anatomical estimate.

```
['m', 'Elephants', 'Asian elephants make out a gap of 8 to 11 minutes of arc near the tip of the trunk, about a tenth of your sharpness. One African elephant managed only 48 minutes.'],
```
Source: Shyan-Norwalt and colleagues, 2010. One African elephant cow reached 48 minutes of arc, a 2.75 cm gap at 196 cm. The abstract reports the Asian figures from earlier studies, at about 2 m from the eyes.

```
['g', 'Dim light', 'Bears, otters and other carnivores have a reflecting layer behind the retina that gives light a second pass. Pigs and red kangaroos have none, so the shadows are lifted only a little.'],
```
Source: *Comparative morphology of the tapetum lucidum*, 2004. Carnivores have a choroidal tapetum cellulosum. The red kangaroo and the pig have no tapetum.

```
['i', 'Field of view and pupil', 'No measurement was found for these. We leave the field as your camera gives it and draw a round pupil.'],
```
Source: none. This is a guess.

```
['x', 'Electric sense', 'A platypus senses weak electric fields through its bill, down to about 50 millionths of a volt across a centimetre, and can find and avoid objects by them. No phone senses this, so it is left out.'],
```
Source: Scheich and colleagues, 1986: "behavioural and electrophysiological sensitivity of ∼50 µV cm−1". The platypus "can locate and avoid objects on the basis of d.c. fields". The second sentence is unsourced (see the unfinished items).

### `raccoon` (one kind of cone, or none)

```
['m', 'Colour', 'A raccoon has one kind of colour sensor in its eyes, and you have three. It sees brightness without hue, so the picture is grey.'],
```
Source: Jacobs and Deegan, 1992. By electroretinogram flicker photometry, the raccoon and kinkajou are monochromatic, and the coati is a dichromat. Wikipedia's *Monochromacy* says the same for procyonids, citing Peichl, Behrmann and Kröger (2001) (secondary).

```
['m', 'Opossum', 'A Virginia opossum also showed only one kind of cone, most sensitive to yellow-green light near 561 nanometres.'],
```
Source: Jacobs and Williams, 2010. They found "a single cone pigment having peak absorption at 561–562 nm". Chromatic adaptation found no second, short-wavelength pigment.

```
['m', 'Armadillos and sloths', 'The nine-banded armadillo and the sloths have broken copies of genes that every cone needs, so they see with rods alone.'],
```
Source: Emerling and Springer, 2015. *Dasypus novemcinctus* is a rod monochromat. PDE6C is inactivated in both *Choloepus* species and *Bradypus tridactylus*.

```
['m', 'Anteaters and pangolins', 'Anteaters have lost the blue-sensitive cone. The Chinese pangolin has lost it too and kept its other cone.'],
```
Source: Emerling and Springer, 2015. SWS1 is "pseudogenic" in anteaters, and their rod monochromacy is still to be tested. In *Manis pentadactyla*, SWS1 is inactivated "but all other cone phototransduction genes are functional".

```
['g', 'Dim light', 'Raccoons, like other carnivores, have a reflecting layer behind the retina, and opossums, like many marsupials, have one within it. We brighten the shadows to suggest it.'],
```
Source: *Comparative morphology of the tapetum lucidum*, 2004. Carnivores have a choroidal tapetum cellulosum, and marsupials have a retinal tapetum.

```
['i', 'Sharpness, field and pupil', 'No measurement was found for raccoons or opossums. These are our guesses.'],
```
Source: none. Veilleux and Kirk (2014) list the Virginia opossum and a two-toed sloth among their anatomical estimates, and the article text gives no value for either.

```
['x', 'Drawn as', 'The picture is grey, weighted toward yellow-green, where the opossum’s single cone is most sensitive. The weights are this app’s own.'],
```
Source: Jacobs and Williams, 2010, for the 561 nm peak. The weighting follows the bee's "Drawn as" row and is invented. Rods peak near 493 nm (the same page), so the weighting is less true for armadillos and sloths.

### `mole` (family Talpidae)

```
['m', 'Eyes', 'An eastern mole’s eyes lie under its skin, and its eyelids almost never part enough to let light in.'],
```
Source: Slonaker: "covered by the skin and true eyelids", with the cleft "practically never open enough to admit light". Animal Diversity Web: "their eyes are covered by a layer of skin".

```
['m', 'Light and dark', 'Its sight goes no further than telling light from dark, so there is no picture here.'],
```
Source: Slonaker: "the power of sight in the mole is no more than to distinguish between light and darkness". Animal Diversity Web: the eyes "likely play an important role in detecting light and dark".

```
['x', 'Snout', 'A mole finds its way and its food with a touch-sensitive patch at the tip of its nose and a keen sense of smell. Neither reaches a camera.'],
```
Source: Animal Diversity Web (Townsend, 2023). It describes a touch-sensitive glabrous patch on the end of the nose, used "to sense their surroundings ahead of them and locate prey", and noses "that can sense the direction of specific odors".

## 3. The picture

| Entry | Field | Value | Behind it |
|---|---|---|---|
| `mammal` | `chip`, `who` | 'Bear, kangaroo, pig', 'a mammal' | This is the app's wording. |
| `mammal` | `M` | DEUTAN | This value rests on the row "Colour" (pig), with the rows "Bears and otters" and "Kangaroos" behind it. Using the existing two-cone model is **invented**, and SOURCES.md lists that matrix as unchecked. The pig's long cone at 556 nm suggests a model that keeps the long cone, which DEUTAN does. That reading is mine. |
| `mammal` | `cpd` | 5 | This value rests on the row "Sharpness". The measured values run from about 0.6 (the audit's conversion of 48 minutes of arc in one African elephant, reading the gap as half a cycle) and 2.7 to 3.75 (my conversion of 8 to 11 minutes of arc in Asian elephants, read the same way) through 4.8 (tammar, behavioural) to 11.2 (grey kangaroo, anatomical). The pick of 5 within that span is **invented**. |
| `mammal` | `gain` | 1.2 | This value rests on the row "Dim light". Carnivores have a tapetum and pigs and red kangaroos have none. No dim-light ratio was found, so the value is **invented**. It is lower than the dog's 1.3 and the cat's 1.7. |
| `mammal` | `pupil` | 'o' | This value is **invented** (the row "Field of view and pupil"). |
| `mammal` | `fov`, `topoA`, `topoS`, `fall`, `dof`, `sat`, `rate` | unset | No source supports them. The black bear has a cone-dense area centralis (Heyward and colleagues, 2021), which would support `topoA` for bears. Kangaroos and pigs may differ, and I found nothing on them, so the field stays unset for the whole entry. |
| `mammal` | `cue` | 'Two kinds of colour sensor, and less detail than yours.' | This is the app's wording. |
| `raccoon` | `chip`, `who` | 'Raccoon, opossum, armadillo', 'a raccoon' | This is the app's wording. |
| `raccoon` | `M` | [.4, .55, .05, .4, .55, .05, .4, .55, .05] | This value rests on the rows "Colour", "Opossum" and "Drawn as". Equal rows give grey, weighted toward the camera's red and green to stand in for one cone near 561 nm. The weights are **invented**. Blue sky goes darker and foliage stays mid-grey. |
| `raccoon` | `cpd` | 4 | This value is **invented**. No acuity was found for any member of this entry, and the value sits below `mammal` because these are night eyes. The row "Sharpness, field and pupil" says so. |
| `raccoon` | `gain` | 1.6 | This value rests on the row "Dim light" (a tapetum in carnivores and marsupials). The value is **invented** and sits just under the cat's 1.7. |
| `raccoon` | `pupil` | 'o' | This value is **invented**. |
| `raccoon` | `fov`, `topoA`, `topoS`, `fall`, `dof`, `sat`, `rate` | unset | No source supports them. |
| `raccoon` | `cue` | 'One kind of colour sensor, or none. The world in greys, with the shadows lifted.' | This is the app's wording. |
| `mole` | `pupil`, `field`, `sat` | 'none', 1, 0 | These values rest on the rows "Eyes" and "Light and dark". This is the picture the `other` entry already draws. |
| `mole` | `chip`, `who`, `cue` | 'Mole', 'a mole', '' | This is the app's wording. |

Here is a sketch for the owner to place. No file was changed.

```
var GREY561 = [.4, .55, .05, .4, .55, .05, .4, .55, .05];   // one cone near 561 nm (Virginia opossum); weights invented
mammal: { chip: 'Bear, kangaroo, pig', who: 'a mammal', cpd: 5, pupil: 'o', M: DEUTAN, gain: 1.2,
  cue: 'Two kinds of colour sensor, and less detail than yours.', rows: [ /* the nine mammal rows */ ] },
raccoon: { chip: 'Raccoon, opossum, armadillo', who: 'a raccoon', cpd: 4, pupil: 'o', M: GREY561, gain: 1.6,
  cue: 'One kind of colour sensor, or none. The world in greys, with the shadows lifted.', rows: [ /* the seven raccoon rows */ ] },
mole: { chip: 'Mole', who: 'a mole', pupil: 'none', field: 1, sat: 0, cue: '', rows: [ /* the three mole rows */ ] }
```

## 4. What the engine cannot draw yet

| Effect | What it would show | Phone input that could stand in | Judgement |
|---|---|---|---|
| Electric sense (platypus) | Living prey under water would appear as a pull on the bill's side, without light. | No input can. As far as I know, no phone sensor reads fields of microvolts per centimetre, and I opened no source on that. The camera could stand in by marking movement, which would be an invention. | It is impossible as measurement. As an invention it is medium work, and it would need an `i` row. |
| Glare in rod-only eyes (armadillos, sloths) | A bright day would wash out toward white, since rods alone are built for dim light. That is my inference, and I opened no source on rod saturation in these animals. | The camera's own brightness could drive it. | It is easy to medium work: a new field that compresses highlights. It waits on a source. |
| A sharp spot for bears and a streak for kangaroos within one entry | Bears would get a central spot and kangaroos a band (the band is unsourced here). | No input is needed. Routing a separate bear entry would do it. | It is easy, once kangaroo topography is sourced. |
| Touch at the snout (moles) | Things would appear only where the snout touches them. | The touch screen could stand in: a tap lights a small patch under the finger in the dark field. | It is easy. It would be invented, and it must be called so in an `i` row. |
| Smell (moles, bears, pigs and others) | Smell has no visual form. | No input can stand in. | It is impossible. |

## 5. Sources

- Jacobs, G. H. and Deegan, J. F., 1992. Cone photopigments in nocturnal and diurnal procyonids. *Journal of Comparative Physiology A* 171: 351 to 358. doi:10.1007/BF00223965. Findings: the raccoon and kinkajou are monochromatic by electroretinogram flicker photometry; the coati is a dichromat with a second class near 433 nm. The raccoon's peak value was not visible. **opened** (Springer abstract page).
- Jacobs, G. H. and Williams, G. A., 2010. Cone pigments in a North American marsupial, the opossum (*Didelphis virginiana*). *Journal of Comparative Physiology A* 196(5): 379 to 384. doi:10.1007/s00359-010-0519-3. Findings: a single cone pigment at 561 to 562 nm, no short-wavelength pigment found, rods near 493 nm, and two cone opsin classes predicted in two South American marsupials. **opened** (Springer page and the eScholarship record, https://escholarship.org/uc/item/5141d6jc).
- Neitz, J. and Jacobs, G. H., 1989. Spectral sensitivity of cones in an ungulate. *Visual Neuroscience* 2(2): 97 to 100. doi:10.1017/S0952523800011949. Finding: the domestic pig has two cone classes, at about 439 and 556 nm. **opened** (Cambridge page).
- Heyward, J. L., Reynolds, B. D., Foster, M. L., Archibald, K. E., Stoskopf, M. K. and Mowat, F. M., 2021. Retinal cone photoreceptor distribution in the American black bear (*Ursus americanus*). *Anatomical Record* 304(3): 662 to 672. doi:10.1002/ar.24472. Findings: both cone types; L/M outnumber S by at least 3 to 1; a cone-dense area centralis dorsotemporal to the optic nerve; "predicted to have a dichromatic vision with high acuity". **opened**, at the University of Wisconsin ophthalmology page that gives the citation and quotes the abstract (https://www.ophth.wisc.edu/blog/2021/03/01/retinal-cone-photoreceptor-distribution-in-the-american-black-bear-ursus-americanus/). The publisher's page was not opened.
- Levenson, D. H., Ponganis, P. J., Crognale, M. A., Deegan, J. F., Dizon, A. and Jacobs, G. H., 2006. Visual pigments of marine carnivores: pinnipeds, polar bear, and sea otter. The record I opened gives no journal, volume, pages or DOI. eScholarship http://www.escholarship.org/uc/item/8sg757mn. Findings: polar bear and sea otter have short-wavelength cones near 440 nm, with middle-to-long cones at 545 to 560 nm, inferred from genes. **opened** (record at https://openpolar.no/Record/ftcdlib:qt8sg757mn).
- Ebeling, W., Natoli, R. C. and Hemmi, J. M., 2010. Diversity of color vision: not all Australian marsupials are trichromatic. *PLoS ONE* 5(12) (volume and issue from the Curtin record, https://espace.curtin.edu.au/handle/20.500.11937/12990?show=full, opened in the audit). No DOI was confirmed. Findings: the tammar wallaby has only two cone types; in the fat-tailed dunnart, 20 to 25% of cones were unlabelled. **opened** (ANU repository record with abstract, https://openresearch-repository.anu.edu.au/items/05feeda9-948e-49bd-b553-d9873a67ffb5).
- Hemmi, J. M. and Mark, R. F., 1998. Visual acuity, contrast sensitivity and retinal magnification in a marsupial, the tammar wallaby (*Macropus eugenii*). *Journal of Comparative Physiology A* 183: 379 to 387. doi:10.1007/s003590050264. Findings: behavioural acuity about 4.8 cycles per degree; anatomical limit about 6. **opened** (Springer page).
- Veilleux, C. C. and Kirk, E. C., 2014. Visual acuity in mammals: effects of eye size and ecology. *Brain, Behavior and Evolution* 83(1): 43 to 53. doi:10.1159/000357830. Findings: 11.2 cycles per degree for the western grey kangaroo (anatomical); the opossum, pig and two-toed sloth are among the anatomical estimates, with no values in the text. **opened** (Karger PDF).
- Shyan-Norwalt, M. R., Peterson, J., Milankow King, B., Staggs, T. E. and Dale, R. H. I., 2010. Initial findings on visual acuity thresholds in an African elephant (*Loxodonta africana*). *Zoo Biology* 29(1): 30 to 35. doi:10.1002/zoo.20259. Findings: one African elephant cow reached 48 minutes of arc (2.75 cm at 196 cm). **opened** (Butler University record with abstract, https://butler.elsevierpure.com/en/publications/initial-findings-on-visual-acuity-thresholds-in-an-african-elepha/). The Asian elephant figures of 8 to 11 minutes of arc near the trunk tip are **secondary**, as the same abstract reports them from earlier studies.
- Emerling, C. A. and Springer, M. S., 2015. Genomic evidence for rod monochromacy in sloths and armadillos suggests early subterranean history for Xenarthra. *Proceedings of the Royal Society B* 282(1800): 20142192. doi:10.1098/rspb.2014.2192. Findings: the armadillo and sloths are rod monochromats; anteater SWS1 is pseudogenic and their rod monochromacy is untested; the Chinese pangolin's SWS1 is inactivated with other cone genes functional. **opened** (eScholarship PDF, https://escholarship.org/content/qt8w19d5kp/qt8w19d5kp.pdf).
- Jacobs, G. H., 2013. Losses of functional opsin genes, short-wavelength cone photopigments, and color vision: a significant trend in the evolution of mammalian vision. *Visual Neuroscience* 30(1 to 2): 39 to 53. doi:10.1017/S0952523812000429. Findings: monotreme cone pigments come from SWS2 and LWS; most mammals have two cone types; SWS1 has been lost in several dozen species from five orders. **opened** (Cambridge abstract page).
- *Comparative morphology of the tapetum lucidum (among selected species)*, 2004. *Veterinary Ophthalmology* 7(1): 11 to 22. doi:10.1111/j.1463-5224.2004.00318.x. The PubMed page I opened did not show the authors, so none are given here. **[unfinished]** The audit could not confirm them either; the Wiley page and the Crossref record were refused. Findings: marsupials have a retinal tapetum and carnivores a choroidal tapetum cellulosum; the red kangaroo and the pig have none. **opened** (https://pubmed.ncbi.nlm.nih.gov/14738502/).
- Scheich, H., Langner, G., Tidemann, C., Coles, R. B. and Guppy, A., 1986. Electroreception and electrolocation in platypus. *Nature* 319: 401 to 402. doi:10.1038/319401a0. Findings: sensitivity of about 50 µV per cm; locates and avoids objects by d.c. fields; its a.c. sensitivity may detect prey muscle activity. **opened** (Nature page).
- Slonaker, J. R., 1899. A preliminary report on the eye of the mole (*Scalops aquaticus machrinus*). *Proceedings of the Indiana Academy of Science* 9: 146 to 149. The volume and year come from the issue page, https://journals.iupui.edu/index.php/ias/issue/view/644, opened in the audit. https://journals.indianapolis.iu.edu/index.php/ias/article/download/13714/13831/20201. Findings: the eye is covered by skin and true eyelids; the lid cleft is practically never open enough to admit light; sight goes no further than light and darkness. **opened**.
- Townsend, S., 2023. *Scalopus aquaticus*, eastern mole. Animal Diversity Web. https://animaldiversity.org/accounts/Scalopus_aquaticus. Findings: eyes under skin, nearly blind, light and dark; a touch-sensitive nose patch; a sense of smell that finds the direction of odours. **opened**.
- Peichl, L., Ahnelt, P. K., Dubielzig, R. R., Kübber-Heiss, A. and Schubert, C., 2005. Retinal cone types in brown bears and the polar bear indicate dichromatic color vision. *Investigative Ophthalmology and Visual Science* 46: 4539 (meeting abstract). Finding: S cones present, in a higher proportion than in many mammals. **secondary** (a student summary at https://science.umd.edu/faculty/wilkinson/BSCI338/Rev092/Peichl05.htm). This paper is used in the scope only.
- Wikipedia. *Monochromacy*. https://en.wikipedia.org/wiki/Monochromacy. Finding: the raccoon, crab-eating raccoon and kinkajou have lost S-cone function. It cites Peichl, L., Behrmann, G. and Kröger, R. H. H., 2001, For whales and seals the ocean is not blue: a visual pigment loss in marine mammals, *European Journal of Neuroscience* 13(8): 1520 to 1528, doi:10.1046/j.0953-816x.2001.01533.x. **opened** (Wikipedia). The cited paper is **secondary**, because its Wiley page was refused.
- GBIF.org occurrence API, dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7, read 12 October 2026 by scientific name. Findings: raccoon 135,489, Virginia opossum 54,547, American black bear 54,505. **opened**.
- This repository: `src/cam.a.js`, `docs/SOURCES.md` and `docs/VIEWS.md`. Findings: the existing entries and fields, and the Alachua rows. **opened**.

## 6. Open questions for a vision scientist

1. Does the raccoon carry a sparse short-wavelength cone that an electroretinogram would miss? Where does its single cone peak, and what do raccoons and Virginia opossums resolve in cycles per degree?
2. Are red and grey kangaroos, the koala and the common brushtail possum dichromats like the tammar wallaby, or trichromats like the quokka?
3. How wide are the fields of view of the raccoon, the bears, the kangaroos and the pig, and where is each sharpest (spot or streak)?
4. What do rod-only armadillos and sloths see in daylight, and is the long-wavelength cone of anteaters intact?
5. Have the cone pigments of African and Asian elephants been confirmed (Yokoyama and colleagues, 2005, could not be opened here), and has flicker fusion been measured in any member of this group?
