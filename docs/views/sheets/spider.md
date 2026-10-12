# Sensing sheet: spider (order Araneae)

This sheet was written on 11 October 2026, from 17:41 to 19:20 EDT. The work ran past the 40 minutes the brief set, and the unfinished parts are listed at the end of section 5.

This is the checked version, audited on 12 October 2026 from 04:51 to 05:17 EDT. The corrections are listed in `spider.audit.md`.

## 1. Scope

**Taxa.** The view covers order Araneae (GBIF orderKey 1496): 2,927,814 iNaturalist research-grade records in GBIF, read 11 October 2026. That is 1.73% of all records, and spiders are the second-largest group with no view.

**What people photograph, worldwide** (GBIF facet by family within Araneae, read 11 October 2026; the top 15 families):

| Family | Common name | Records | Share of spider records | How it meets prey |
|---|---|---:|---:|---|
| Araneidae | orb weavers | 918,443 | 31.4% | web |
| Salticidae | jumping spiders | 684,540 | 23.4% | sight |
| Theridiidae | cobweb spiders | 195,578 | 6.7% | web |
| Thomisidae | crab spiders | 173,427 | 5.9% | ambush, no web |
| Pisauridae | nursery web and fishing spiders | 161,306 | 5.5% | hunting, no web |
| Lycosidae | wolf spiders | 125,899 | 4.3% | hunting, no web |
| Tetragnathidae | long-jawed orb weavers | 92,534 | 3.2% | web |
| Agelenidae | funnel weavers | 61,822 | 2.1% | web |
| Sparassidae | huntsman spiders | 61,542 | 2.1% | hunting, no web |
| Pholcidae | cellar spiders | 55,684 | 1.9% | web |
| Oxyopidae | lynx spiders | 49,795 | 1.7% | hunting, no web |
| Theraphosidae | tarantulas | 42,576 | 1.5% | hunting, no web |
| Linyphiidae | sheet weavers | 32,339 | 1.1% | web |
| Philodromidae | running crab spiders | 25,024 | 0.9% | hunting, no web |
| Gnaphosidae | ground spiders | 24,825 | 0.8% | hunting, no web |
| all other families | | 222,480 | 7.6% | |

The last column is this sheet's own summary; no source opened here states it family by family. The six web-building families in the table hold 1,356,400 records (46.3%), which is six in ten of the records outside the jumping spiders. Jumping spiders hold 23.4%. The other hunting families hold 22.7%, of which wolf spiders hold 4.3%.

**Alachua County, Florida** (`docs/views/no-view-us-fl-alachua.csv`): 161 species and 4,660 records. Orb weavers lead with 1,740 records (37.3%), then jumping spiders with 1,107 (23.8%) and long-jawed orb weavers with 434 (9.3%). Web builders of all families hold 2,609 records (56.0%). The most recorded species are the Golden Silk Spider (*Trichonephila clavipes*, Araneidae, 702), the Mabel Orchard Orbweaver (*Leucauge argyrobapta*, Tetragnathidae, 415), the Twin-flagged Jumping Spider (*Anasaitis canosa*, Salticidae, 284) and the Yellow Garden Spider (*Argiope aurantia*, Araneidae, 275).

**Can one view be true?** It cannot. The two largest families meet the world in opposite ways. A jumping spider has two front eyes that resolve 5 to 12.5 cycles per degree over a narrow strip that muscles swing about, six more eyes covering nearly the whole circle, ultraviolet and green receptors, and a depth sense that compares a sharp layer of retina with a blurred one. An orb weaver sits in its web and feels its prey through the silk, at 5 to 30 shakes a second, and the difference in strength across its legs gives the direction. Most spiders register little more than changes of light and dark. A picture drawn for one of these two families is false for the other.

**Recommendation.** The group should split at family Salticidae into two views.

- `jumper` takes family Salticidae (23.4% of world spider records, 23.8% in Alachua). Its picture is a sharp, magnified centre inside a near-complete circle of coarse vision.
- `spider` takes every other spider (76.6%). Its picture is built for the web builders, because they are the commonest photographed spiders: the orb weavers are the largest family worldwide and the Golden Silk Spider is the most recorded spider in Alachua. The commonest photographed spiders therefore get the web picture, which is very coarse light and shade in which only what moves is drawn, standing in for the shaking of the web.

The cost of this choice is that wolf spiders (4.3%) and net-casting spiders see better in dim light than the `spider` picture shows, and the eyes of the other hunting families (18.4%) were not researched for this sheet. Two `x` rows in `spider` say so. A third view for wolf spiders and their hunting relatives is the next split if one is wanted; figures toward it are in Land and Barth 1992, Morehouse 2020 and Stafstrom and Hebets 2016.

In `tools/species/eyes.py` the split is one family rule (`Salticidae` goes to `jumper`) placed before the order rule (`Araneae` goes to `spider`), in the way Felidae and Canidae are handled now.

## 2. The rows

### `jumper` (Salticidae)

`['g', 'Sharpness', 'The two big front eyes resolve 5 to 12.5 cycles per degree, depending on the species, against your 60. The centre is drawn sharp and pulled close.']`
Source: Morehouse 2020 (jumping spider principal eyes resolve points 0.04 to 0.1 degrees apart; the conversion to cycles per degree, one cycle for every two such spacings, is this sheet's); Shepeleva 2022 (*Portia fimbriata*, 12.5 cycles per degree, "only five times lower" than the human fovea's 60); Australian Museum (the front eyes give "a clear, focussed telephoto image").

`['g', 'Where it is sharp', 'That sharpness covers a narrow upright strip, from under 1 to 5 degrees wide and up to 20 high. Muscles swing the retina, and the strip with it, across whatever the spider examines.']`
Source: Shepeleva 2022 (principal-eye field from 0.8 degrees in *Portia fimbriata* to 5 degrees wide and 20 high in *Metaphidippus aeneolus*; three pairs of muscles move the retina); De Agrò, Rößler and Shamble 2024 (principal eyes about 5 degrees).

`['g', 'Field', 'The six other eyes cover about 330 to 350 degrees between them, nearly the whole circle, to your 180. The camera holds a slice of it, and the edges are invented.']`
Source: De Agrò, Rößler and Shamble 2024 (*Menemerus semilimbatus*, the genus of the Gray Wall Jumping Spider: front side eyes about 100 degrees and rear side eyes about 260 in its results; secondary eyes about 350 together, a figure its introduction gives for jumping spiders in general); Shepeleva 2022 (*Trite planiceps*, about 330 degrees).

`['g', 'Movement', 'The two front side eyes catch movement and steer the sharp eyes onto it. Without that guidance the sharp eyes cannot track a moving target.']`
Source: Jakob and colleagues 2018 (the principal eyes "can thus precisely target moving stimuli, but only with the guidance of the secondary eyes"; the University of Massachusetts report of that work, https://www.umass.edu/news/article/umass-amherst-research-shows-spider-eyes, says the secondary eyes are needed for the principal eyes to track moving stimuli); Bruce and colleagues 2021 (*Phidippus audax*, the Bold Jumping Spider: motion-sensitive front side eyes overlap the principal eyes and direct them).

`['m', 'Colour', 'The Regal Jumping Spider has receptors near 370 nanometres, in ultraviolet, and 530, in green. Reds are drawn dark with a model of a person missing red cones, and the violet for ultraviolet is invented.']`
Source: De Voe 1975 (*Phidippus regius*, the Regal Jumping Spider, 109 records in Alachua: ultraviolet cells near 370 nm, green near 532 nm, and cells with both peaks); Zurek and colleagues 2015 (the principal eyes of most jumping spiders use only two pigments).

`['g', 'Colour at the edges', 'The side eyes carry a single green receptor and see no colour. Colour is muted everywhere here, because the picture cannot keep it to the centre.']`
Source: Shepeleva 2022, citing its reference 21 (front and rear side eyes monochromatic, green, peak near 535 to 540 nm).

`['g', 'Depth', 'A jumping spider judges distance by comparing a sharp image on the deepest layer of its retina with a blurred one on the layer above, and under red light it often misjudges its jumps. Here near and far are guessed from height in the frame, and a tap moves the focus.']`
Source: Nagata and colleagues 2012 (*Hasarius adansoni*, Adanson's jumping spider: four tiered layers; the two deepest are green-sensitive; only the deepest receives a focused green image; the colour of the light changed depth judgement), with the red-light result from the Phys.org report of that paper; Morehouse 2020 (jumping spiders judge depth by image defocus).

`['x', 'Hearing', 'A Bold Jumping Spider freezes at a low hum of 80 vibrations a second, and its brain still answers that hum from more than three metres away. The picture has no sound.']`
Source: Shamble and colleagues 2016 (*Phidippus audax*: spiders froze at 80 Hz tones of 65 dB SPL with the speaker 2 m away; neural responses to 80 to 380 Hz at 65 dB SPL persisted beyond 3 m; stimulating hairs on the foreleg patella was enough to drive the neural response, and the authors say these hairs likely play a role in hearing).

**Jumping spider figures, gathered**

| Measure | Figure | Species | Source |
|---|---|---|---|
| Sharpness, principal eyes | 12.5 cycles per degree | *Portia fimbriata* | Shepeleva 2022, from its reference 18 |
| Receptor spacing, principal eyes | 0.04 to 0.07 degrees | jumping spiders | Morehouse 2020 |
| Receptor spacing, densest secondary eyes | 0.4 to 0.7 degrees | spiders | Morehouse 2020 |
| Field, principal eyes | 0.8 to 5 degrees wide, up to 20 high | *Portia fimbriata*, *Metaphidippus aeneolus* | Shepeleva 2022 |
| Field, front side eyes | about 50 degrees each side, about 100 in all | *Menemerus semilimbatus* | De Agrò and colleagues 2024 |
| Field, rear side eyes | about 260 degrees | *Menemerus semilimbatus* | De Agrò and colleagues 2024 |
| Field, rear middle eyes | small, vestigial, facing the sky | jumping spiders | De Agrò and colleagues 2024; Morehouse 2020 |
| Field, all secondary eyes | about 330 to 350 degrees | *Trite planiceps*; *M. semilimbatus* | Shepeleva 2022; De Agrò and colleagues 2024 |
| Colour, principal eyes | ultraviolet near 370 to 377 nm, green near 525 to 532 nm | *Phidippus regius*; *Habronattus pyrrithrix* | De Voe 1975; Zurek and colleagues 2015 |
| Colour, extra class | predicted near 626 nm, made by a red filter over some green receptors | *Habronattus pyrrithrix* | Zurek and colleagues 2015 |
| Colour, extra class | blue near 480 to 500 nm | a *Maratus* species | Shepeleva 2022, from its reference 23 |
| Colour, side eyes | green only, near 535 to 540 nm | jumping spiders | Shepeleva 2022, from its reference 21 |
| Colour, rear middle eyes | ultraviolet near 370, blue near 480 | jumping spiders | Shepeleva 2022, from its reference 32 |
| Depth | defocus between the two deepest, green-sensitive layers | *Hasarius adansoni* | Nagata and colleagues 2012 |
| Hearing | 80 Hz at 65 dB SPL; freezing with the speaker 2 m away, brain responses beyond 3 m | *Phidippus audax* | Shamble and colleagues 2016 |
| Flicker | no measurement found | | |

### `spider` (every other spider, built for the web builders)

`['m', 'The web', 'A Golden Silk Spider feels its prey through the silk, and a trapped insect shakes the web 5 to 30 times a second. The shaking arrives ten to thirty times stronger on some legs than on others, which gives the direction.']`
Source: Landolfa and Barth 1996 (*Nephila clavipes*, which GBIF now files as *Trichonephila clavipes*, the Golden Silk Spider: prey vibrations peaked between 5 and 30 Hz; amplitude differences of 20 to 30 dB around the hub and at the leg tips indicate the direction of the stimulus; 20 to 30 dB is a ten- to thirtyfold difference in amplitude).

`['x', 'Drawn as', 'The picture cannot draw the shaking of the web. Only what moves is shown in its place, so hold the phone as still as a spider holds its web.']`
Source: the app's own choice, leaning on the Australian Museum ("Most are able to detect little more than light-dark intensity changes").

`['g', 'Eyes', 'Most spiders have eight eyes and few see well. Most register little more than changes between light and dark, and spiders that build webs lean on the shaking of the silk.']`
Source: Australian Museum ("Spiders usually have eight eyes", "few have good eyesight", most "detect little more than light-dark intensity changes"); Stafstrom and Hebets 2016 (web builders "tend to rely more on vibrational cues in their web for foraging and mating"); Clemente and colleagues 2005 (*Badumna insignis*, a sheet-web spider: resolution and sensitivity low, especially in the secondary eyes).

`['g', 'Sharpness', 'A wandering spider resolves nothing finer than about 2 degrees, under a hundredth of your sharpness. The picture borrows that figure for web builders.']`
Source: Land and Barth 1992 (*Cupiennius salei*, Ctenidae, a wandering spider: the receptor mosaic limits the finest resolvable grating to a period of about 2 degrees or more, which is 0.5 cycles per degree or less).

`['g', 'Pace', 'A wandering spider stops following flicker between 4.3 and 8.6 times a second, a seventh of your rate or less, so movement smears into trails.']`
Source: Fenk and Schmid 2011 (*Cupiennius salei*: behavioural temporal cut-off between 4.3 and 8.6 cycles per second; no faster flicker raised eye-muscle activity).

`['g', 'Colour', 'Orb weavers of the yellow garden spider’s genus carry ultraviolet, blue and green receptors in some of their eyes. Colour is left as the camera gives it, and their ultraviolet is not drawn.']`
Source: Morehouse 2020 (among the exceptions to colour vision in the principal eyes it lists "the UV-, blue-, and green-sensitive photoreceptors found in the secondary eyes of the ctenid spider Cupiennius salei," followed by "and orb weavers in the genus Argiope"; *Argiope* is the Yellow Garden Spider's genus). The sentence can be read two ways, and its most natural reading supports the row (open question 5).

`['x', 'Hearing through silk', 'A bridge spider turns toward a loudspeaker three metres away, because its web moves with the air and works as a listening surface up to 10,000 times larger than its body. The picture has no sound.']`
Source: Zhou and colleagues 2022 (*Larinioides sclopetarius*, Araneidae: the web captures sound-induced movement of air particles, and the spider detects and locates the source; loudspeaker 3 m away; sound-sensitive area up to 10,000 times the spider's).

`['x', 'Wolf spiders', 'Wolf spiders have four large rear eyes backed by a mirror layer, which shines back in a flashlight beam and helps them spot movement in dim light. This picture leaves that out.']`
Source: Australian Museum (the four large posterior eyes of wolf spiders have well-developed tapeta that help them spot prey movement in low light and shine in torchlight).

`['x', 'Net-casting spiders', 'The Ogre-faced Spider catches walking prey by sight at night, and net-casting spiders have the largest single lenses known in any arthropod, 1.4 millimetres across. This picture leaves out their night sight.']`
Source: Stafstrom and Hebets 2016 (*Deinopis spinosa*, the Ogre-faced Spider, 88 records in Alachua: covering the large rear middle eyes cut its capture of walking prey in the field and in the laboratory); Morehouse 2020 (*Deinopis* lenses 1.4 mm across, F-number 0.58, the largest single lenses known from arthropods).

## 3. The picture

Proposed entries in the form of `src/cam.a.js`:

```
jumper: { chip: 'Jumping spider', who: 'a jumping spider', fov: 350, cpd: 8, topoA: 1, fall: 7, fovea: 2.5, pupil: 'o', dof: 14, M: PROTAN, sat: .5, sheen: .5,
  cue: 'The centre is sharp and pulled close, inside nearly the whole circle. Tap to move the focus.', rows: [ ... ] }
spider: { chip: 'Spider', who: 'a spider', fov: 300, cpd: .5, pupil: 'o', gate: 1, persist: .15,
  cue: 'Hold still, as a spider holds its web. Only what moves reaches you.', rows: [ ... ] }
```

### `jumper`

| Field | Value | Behind it | Invented? |
|---|---|---|---|
| `fov` | 350 | Field row: about 350 degrees in *Menemerus semilimbatus* (De Agrò and colleagues 2024) and about 330 in *Trite planiceps* (Shepeleva 2022). The engine shrinks the camera picture to 0.51 and invents the rest. | |
| `cpd` | 8 | Sharpness row: 5 to 12.5 cycles per degree across jumping spider principal eyes (Morehouse 2020; Shepeleva 2022). | the choice of 8 within that range is invented |
| `topoA` | 1 | Where it is sharp row: one sharp region at the centre. The true region is an upright strip, which the engine cannot draw (section 4). | |
| `fall` | 7 | Half a frame height from the centre the engine then blurs eight times more than at the centre, which brings 8 cycles per degree down to 1. The densest secondary-eye spacing, 0.4 to 0.7 degrees (Morehouse 2020), gives 0.7 to 1.25 cycles per degree. | the mapping is invented |
| `fovea` | 2.5 | Sharpness row: the principal eyes give a telephoto image (Australian Museum). | the magnitude is invented |
| `pupil` | 'o' | Spider eyes are single-lens camera-like eyes (Shepeleva 2022). `'none'` would bring the insect hexagons during the change of eyes. | invented |
| `dof` | 14 | Depth row (Nagata and colleagues 2012). The blur stands in for the defocus comparison, with depth guessed from height in the frame. | the strength is invented |
| `M` | PROTAN | Colour row: receptors near 370 and 532 nm (De Voe 1975). The human protan model keeps a cone near 530 nm and loses the long one, so reds fall dark; it keeps a blue cone where the spider's short receptor is in ultraviolet. The matrix itself is listed in `docs/SOURCES.md` as entered from memory. | the model is invented |
| `sat` | .5 | Colour at the edges row: side eyes green only (Shepeleva 2022), and most of the screen is side-eye territory. | invented |
| `sheen` | .5 | Colour row: an ultraviolet receptor (De Voe 1975), drawn as the app's usual violet. | invented |
| `gain` | leave out | Jumping spiders hunt by day (Morehouse 2020). | |
| `rate` | leave out | No flicker measurement found. | |

### `spider`

| Field | Value | Behind it | Invented? |
|---|---|---|---|
| `fov` | 300 | No measurement for web builders. In *Cupiennius salei* the rear middle and rear side eyes together cover nearly the whole upper hemisphere (Land and Barth 1992). | invented |
| `cpd` | .5 | Sharpness row: finest grating about 2 degrees in *Cupiennius salei* (Land and Barth 1992). | |
| `pupil` | 'o' | As for `jumper`. | invented |
| `gate` | 1 | Drawn as row; most spiders register little more than changes of light and dark (Australian Museum). It stands in for the web, which the engine cannot draw. | invented |
| `persist` | .15 | Pace row: cut-off 4.3 to 8.6 Hz in *Cupiennius salei* (Fenk and Schmid 2011). `persist` is a time constant in seconds, and 0.15 s lies between 1/8.6 and 1/4.3 of a second. The frog uses the same value for a 6.7 Hz toad. | |
| `M`, `sat` | leave out | Colour row: *Argiope* has ultraviolet, blue and green receptors (Morehouse 2020), so colour stays as the camera gives it. | |
| `dof`, `gain`, `fovea`, `topoA`, `topoS`, `fall` | leave out | No source. | |

With `gate` and `persist` the `spider` view resembles the frog's, made eight times coarser, and the rows carry the difference. The plant's light-only picture (`field: 1`) was considered and not taken, because spider eyes have lenses that form an image: Land and Barth 1992 found the image "of good quality in all eyes" of *Cupiennius salei*.

## 4. What the engine cannot draw yet

Today the app reads only the camera. `src/cam.c1.js` asks for video with `audio: false`, and no file in `src/` or `index.html` listens for device motion.

1. **Vibration of the web, the main sense of the commonest spiders.** It would show a pulse arriving from the side a disturbance comes from, strongest on that side of the frame, and repeating at the 5 to 30 per second rhythm of struggling prey (Landolfa and Barth 1996). The phone's motion sensors could stand in for it. A tap on the phone, or on a table it rests on, shakes it as prey shakes a web; the accelerometer measures that, and the axis of the jolt could set the side the pulse comes from. The person's own hand shakes the phone too, which is one more reason for the cue to hold still. Following 30 shakes a second needs the sensor read at least 60 times a second, and whether each phone and browser does so, and whether the browser first asks the person's permission, needs checking. The microphone also hears taps, but only once the sound has crossed the air, so the motion sensors are the closer stand-in for a thread. This is moderately hard. Reading the sensor is easy, and a fair sense of direction from one point on one phone is the hard part, because the spider compares eight legs spread across the web.
2. **Hearing through hairs and through the web.** It would show a low hum, such as the 80 per second that a Bold Jumping Spider freezes at from 2 m and that its brain answers from beyond 3 m (Shamble and colleagues 2016) or a loudspeaker across a room for a bridge spider (Zhou and colleagues 2022), as a pulse or brightening of the picture. The microphone could stand in for it, filtered to low pitches. This is easy to read, with two costs: a camera app would add a microphone prompt, and how well phone microphones record low pitches needs checking.
3. **Several eyes with different fields and colour (`jumper`).** It would show a narrow upright strip that is sharp and coloured, inside a wide grey surround that draws mostly movement. The engine has one sharpness shape (a spot or a horizontal band), one saturation for the whole picture, and one movement gate for the whole picture. It needs an upright strip shape, saturation that falls away with the sharpness map, and the frog's gate applied only outside the centre. The camera alone supplies this. This is easy to moderately hard, and all of it is shader work.
4. **A sharp strip that jumps to movement (`jumper`).** The side eyes steer the principal eyes onto what moves (Jakob and colleagues 2018). The engine already keeps a record of change for the frog's gate; the sharp centre could move to the largest change and drift back. Today a tap moves only the depth focus. This is moderately hard.
5. **Depth from defocus (`jumper`).** True near and far would let the blur follow distance, as the spider's blurred retinal layer does (Nagata and colleagues 2012). A camera feed in the browser carries no distances; some phones give depth to native apps, and a depth-estimating model could guess it from the picture. This is hard in the browser and possible in a native build.

## 5. Sources

Records and names:

- GBIF.org, read 11 October 2026. Occurrence search API, dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7, orderKey 1496, facet familyKey, top 15. https://api.gbif.org/v1/occurrence/search?datasetKey=50c9509d-22c7-4a22-a47d-8c48425ef4a7&orderKey=1496&facet=familyKey&limit=0&facetLimit=15. Total 2,927,814 and the family counts in section 1. `opened`
- GBIF.org species API, read 11 October 2026: keys 7359 Araneidae, 9583 Theridiidae, 2151272 Tetragnathidae, 7353 Agelenidae, 7370 Gnaphosidae (https://api.gbif.org/v1/species/<key>). `opened`. The other ten family keys were named from the repository's cached copy of GBIF's family names (`runs/fetch/10/names-family-animalia-*.json` on the `ci` branch, fetched from api.gbif.org on 11 October 2026), and the counts in that cache's family facet agree with the live facet.
- GBIF.org species match for *Nephila clavipes*, read 11 October 2026: a synonym of *Trichonephila clavipes* (key 10886629), Araneidae. https://api.gbif.org/v1/species/match?name=Nephila%20clavipes&rank=SPECIES&kingdom=Animalia. `opened`
- Repository file `docs/views/no-view-us-fl-alachua.csv`: Alachua spider records summed by family. Read locally.

Senses:

- Landolfa, M. A. and Barth, F. G. 1996. Vibrations in the orb web of the spider *Nephila clavipes*: cues for discrimination and orientation. *Journal of Comparative Physiology A* 179: 493-508. https://doi.org/10.1007/BF00192316. Prey vibrations peak at 5 to 30 Hz; amplitude differences of 20 to 30 dB around the hub and at the leg tips indicate direction. `opened` (abstract)
- Zhou, J., Lai, J., Menda, G., Stafstrom, J. A., Miles, C. I., Hoy, R. R. and Miles, R. N. 2022. Outsourced hearing in an orb-weaving spider that uses its web as an auditory sensor. *PNAS* 119(14): e2122789119. https://doi.org/10.1073/pnas.2122789119. *Larinioides sclopetarius*; the web captures sound-induced air movement and the spider locates the source; loudspeaker 3 m away; area up to 10,000 times the spider's. `secondary` (the Sci.News report at https://www.sci.news/biology/acoustic-spider-web-10675.html and the Cornell Chronicle report at https://news.cornell.edu/node/323908; the author list from the journal reference at https://sciencedaily.com/releases/2022/03/220329114714.htm; the PNAS page failed to load, and the preprint at https://www.biorxiv.org/content/10.1101/2021.10.17.464740v2 could not be opened at audit)
- Shamble, P. S., Menda, G., Golden, J. R., Nitzany, E. I., Walden, K., Beatus, T., Elias, D. O., Cohen, I., Miles, R. N. and Hoy, R. R. 2016. Airborne acoustic perception by a jumping spider. *Current Biology* 26(21): 2913-2920. https://doi.org/10.1016/j.cub.2016.08.041. *Phidippus audax*; freezing at 80 Hz and 65 dB SPL with the speaker 2 m away; neural responses beyond 3 m; foreleg hairs. `opened` (abstract at https://escholarship.org/uc/item/0n97m3hq; the 2 m from the methods of the full text at https://escholarship.org/content/qt0n97m3hq/qt0n97m3hq.pdf)
- De Voe, R. D. 1975. Ultraviolet and green receptors in principal eyes of jumping spiders. *Journal of General Physiology* 66(2): 193-207. https://doi.org/10.1085/jgp.66.2.193. *Phidippus regius*: receptors near 370 and 532 nm, and dual cells at 370 and 525. `opened` (abstract)
- Zurek, D. B., Cronin, T. W., Taylor, L. A., Byrne, K., Sullivan, M. L. G. and Morehouse, N. I. 2015. Spectral filtering enables trichromatic vision in colorful jumping spiders. *Current Biology* 25(10): R403-R404. https://doi.org/10.1016/j.cub.2015.03.033 (volume, issue, pages and DOI as given by Sci.News at https://www.sci.news/biology/science-habronattus-jumping-spiders-trichromatic-color-vision-02816.html; pages also in the lab's publication list). *Habronattus pyrrithrix*: green 530 nm, ultraviolet 377 nm, filtered red predicted near 626 nm; most jumping spiders use two pigments. `opened` (PDF at https://homepages.uc.edu/~morehonn/wp-content/uploads/2018/10/Zurek-DB-et-al-2015-Current-Biology.pdf)
- Nagata, T. and colleagues (the repository page opened named Takashi Nagata, Michiyo Kinoshita and Kentaro Arikawa among the authors without the full list). 2012. Depth perception from image defocus in a jumping spider. *Science* 335(6067): 469-471. https://doi.org/10.1126/science.1211667. *Hasarius adansoni*: four tiered layers; the two deepest green-sensitive; the second layer always receives a defocused image; the colour of the light changed depth judgement. `opened` (abstract at https://ir.soken.ac.jp/records/4203; the red-light misjudgement from the Phys.org report at https://m.phys.org/news/2012-01-spider-fuzzy-eyesight-distance.html)
- Morehouse, N. 2020. Spider vision. *Current Biology* 30: R963-R983, 7 September 2020 (pages from the PDF's running header and the lab's publication list at https://homepages.uc.edu/~morehonn/publications/; no DOI is printed on the PDF). https://homepages.uc.edu/~morehonn/wp-content/uploads/2021/02/Morehouse-NI-2020-Curr-Biol.pdf. Principal-eye spacing 0.04 to 0.07 degrees and densest secondary 0.4 to 0.7; points resolved 0.04 to 0.1 degrees apart; *Deinopis* lenses 1.4 mm, F-number 0.58; eight eyes typical; *Argiope* secondary-eye colour receptors; jumping spiders diurnal; depth by image defocus. `opened`
- Shepeleva, I. P. 2022 (online 31 December 2021). A comparative analysis of the camera-like eyes of jumping spiders and humans. *Vision* 6(1): 2. https://doi.org/10.3390/vision6010002. *Portia fimbriata* 12.5 cycles per degree; principal field 0.8 to 5 degrees wide and 20 high; three pairs of retinal muscles; secondary eyes about 330 degrees in *Trite planiceps*; receptor peaks for each eye pair. `opened`. The primary papers behind these figures (its references 17, 18, 21, 23, 26, 32 and 33) were not opened, and their figures are `secondary` through this review.
- De Agrò, M., Rößler, D. C. and Shamble, P. S. 2024. Eye-specific detection and a multi-eye integration model of biological motion perception. *Journal of Experimental Biology* 227: jeb247061. https://doi.org/10.1242/jeb.247061. Principal eyes about 5 degrees; front side eyes about plus or minus 50, about 100 in all in *Menemerus semilimbatus*; rear side eyes about 260; secondary eyes about 350 together; rear middle eyes vestigial. `opened` (PDF at https://epub.uni-regensburg.de/58626/1/jeb247061.pdf)
- Bruce, M., Daye, D., Long, S. M., Winsor, A. M., Menda, G., Hoy, R. R. and Jakob, E. M. 2021. Attention and distraction in the modular visual system of a jumping spider. *Journal of Experimental Biology* 224: jeb231035. https://doi.org/10.1242/jeb.231035. *Phidippus audax*: motion-sensitive front side eyes overlap and direct the principal eyes. `opened` (https://par.nsf.gov/servlets/purl/10223200)
- Jakob, E. M., Long, S. M., Harland, D. P., Jackson, R. R., Carey, A., Searles, M. E., Porter, A. H. and colleagues. 2018. Lateral eyes direct principal eyes as jumping spiders track objects. *Current Biology* 28(18): R1092-R1093. https://doi.org/10.1016/j.cub.2018.07.065. The principal eyes target moving things only with the side eyes' guidance. `opened` (record at https://agresearch.figshare.com/articles/journal_contribution/Lateral_eyes_direct_principal_eyes_as_jumping_spiders_track_objects/22738157)
- Land, M. F. and Barth, F. G. 1992. The quality of vision in the ctenid spider *Cupiennius salei*. *Journal of Experimental Biology* 164: 227-242. https://cob.silverchair.com/jeb/article-pdf/164/1/227/2465183/jexbio_164_1_227.pdf. Finest grating about 2 degrees or more; image of good quality in all eyes; F-numbers 0.58 to 0.74; gridiron tapeta in the secondary eyes; rear eyes cover nearly the upper hemisphere; eyes resemble those of wolf spiders. `opened`
- Fenk, L. M. and Schmid, A. 2011. Flicker-induced eye movements and the behavioural temporal cut-off frequency in a nocturnal spider. *Journal of Experimental Biology* 214(21): 3658-3663. https://doi.org/10.1242/jeb.060855. *Cupiennius salei*: behavioural cut-off between 4.3 and 8.6 cycles per second. `opened` (summary at https://cob.silverchair.com/jeb/article-split/214/21/3658/10588/Flicker-induced-eye-movements-and-the-behavioural; citation from https://journals.biologists.com/jeb/article/214/21/3658/10588/)
- Clemente, C. J., McMaster, K. A., Fox, L., Meldrum, L., Main, B. Y. and Stewart, T. 2005. Visual acuity of the sheet-web building spider *Badumna insignis* (Araneae, Desidae). *Journal of Arachnology* 33(3): 726-734. https://doi.org/10.1636/S04-35.1. Resolution and sensitivity low, especially in the secondary eyes. `opened` (abstract at https://research.usc.edu.au/esploro/outputs/journalArticle/Visual-acuity-of-the-sheet-web-building/99449164402621)
- Stafstrom, J. A. and Hebets, E. A. 2016. Nocturnal foraging enhanced by enlarged secondary eyes in a net-casting spider. *Biology Letters* 12(5): 20160152. https://doi.org/10.1098/rsbl.2016.0152. *Deinopis spinosa*: covering the large eyes cut capture of walking prey; web builders tend to rely more on vibration in the web. `opened` (full text at https://pmc.ncbi.nlm.nih.gov/articles/PMC4892245/)
- Australian Museum. How spiders see the world. Updated 6 December 2022. https://australian.museum/learn/animals/spiders/how-spiders-see-the-world/. Eight eyes usual, few see well, most detect little more than light-dark changes; wolf spider tapeta and eyeshine; net-casting spiders' enlarged rear middle eyes; jumping spiders' telephoto front eyes. `opened`

Pages that could not be read: Europe PMC refused two queries (HTTP 429, rate limit) and was not retried; a PMC page on air-flow hairs returned a browser check; BioOne (a wolf spider tapetum paper), HAL and Phaidra blocked automated access; the PNAS page for Zhou and colleagues failed to load. Tiedemann, Ventura and Ades 1986 (*Journal of Arachnology* 14: 71-78, spectral sensitivities of *Argiope argentata*) was seen only as a citation and backs nothing here.

**Not finished.** No source on air-flow hairs (trichobothria) in web builders was opened, so the sheet has no row for them. No source on vibration felt through the ground in jumping spiders was opened, so the `jumper` rows carry hearing only. Crab spider and lynx spider vision was not researched. The view for wolf spiders and their relatives exists only as two `x` rows and the sources named in section 1. The world family counts stop at the top 15.

## 6. Open questions for a vision or sensory scientist

1. What are the measured acuity and fields of an orb weaver's eyes (*Trichonephila*, *Argiope*, *Leucauge*)? The `spider` view borrows 2 degrees from *Cupiennius*, a wandering spider with good eyes for its group.
2. Does a hub-sitting orb weaver respond to visual movement near its web? If it does not, is "only what moves is drawn" a fair stand-in for the web, or does it give the eyes a role they lack?
3. Has flicker fusion or temporal resolution been measured in any jumping spider?
4. Could one phone accelerometer give a fair likeness of the web's cues, the 5 to 30 Hz band and the 20 to 30 dB differences between legs, and what sampling rate would that need?
5. Do *Argiope* secondary eyes carry ultraviolet, blue and green receptors, as this reading of Morehouse 2020 has it, and does Tiedemann, Ventura and Ades 1986 agree?
