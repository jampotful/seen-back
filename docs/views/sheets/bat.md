# Sensing sheet: bat (order Chiroptera)

Work began at 17:41 Eastern on 11 October 2026 and ran past the 40-minute budget. Unfinished items are marked **Unfinished** where they fall and are listed together at the end.

This is the checked copy, saved beside it as bat.checked.md after an audit on 12 October 2026 (bat.audit.md). Changes are marked **Audit** where they fall.

## 1. Scope

**Taxa.** The view covers the whole order Chiroptera, which has 93,809 iNaturalist research-grade records in GBIF, 0.06% of all records (read 11 October 2026).

**Families photographed most, worldwide.** The counts below come from a GBIF occurrence search on the iNaturalist dataset (`orderKey=734`, faceted by `familyKey`), read on 11 October 2026. Keys were named from GBIF species pages and from GBIF name lists stored in the repository (section 5).

| Family | Who they are | Records | Share of bat records | Echolocation |
|---|---|---:|---:|---|
| Vespertilionidae | evening bats: big brown, red, tricolored, myotis | 37,377 | 39.8% | calls |
| Pteropodidae | flying foxes and Old World fruit bats | 22,639 | 24.1% | none; rousettes click with the tongue |
| Phyllostomidae | New World leaf-nosed bats, the Jamaican fruit bat among them | 10,907 | 11.6% | calls |
| Emballonuridae | sac-winged and sheath-tailed bats | 6,709 | 7.2% | calls |
| Molossidae | free-tailed bats | 5,335 | 5.7% | calls |
| Rhinolophidae | horseshoe bats | 5,242 | 5.6% | calls |
| Hipposideridae | roundleaf bats | 2,250 | 2.4% | calls |
| Megadermatidae | false vampires, ghost bat | 983 | 1.0% | calls |
| Seven more: Miniopteridae, Mormoopidae, Nycteridae, Noctilionidae, Natalidae, Thyropteridae, Rhinopomatidae | | 2,210 | 2.4% | calls |

The calls column rests on two general sources and on studies of particular families. GBIF's note on the order puts Pteropodidae alone in Megachiroptera and every other family in Microchiroptera, and a Sunshine Coast Council page says that only the microbats echolocate. Sources opened for this sheet describe calls in Vespertilionidae and Emballonuridae (Moss and Surlykke 2010), Rhinopomatidae (Boonman and colleagues 2013), Mormoopidae (Simões and colleagues 2019; Wilson, Britannica), Rhinolophidae and Megadermatidae (Wilson, Britannica), Molossidae in the Mexican free-tailed bat (Gillam and colleagues, a meeting abstract), and Phyllostomidae, where the Jamaican fruit bat was among the species filmed and the bats echolocated in every flight sequence (Gessinger and colleagues 2021). **Unfinished:** for Hipposideridae, Miniopteridae, Nycteridae, Noctilionidae, Natalidae and Thyropteridae, 3,815 records in all, only the two general sources support the column.

The fifteen families in the facet hold 93,652 records, and the other 157 records carry another family or none. Families other than Pteropodidae hold 71,013 records, about three quarters of all bat records.

**Species photographed most, worldwide.** The twelve species recorded most, from the same search faceted by `speciesKey`, are: grey-headed flying fox 5,590 (Pteropodidae); big brown bat 5,579 (Vespertilionidae); Mexican free-tailed bat 3,822 (Molossidae); proboscis bat 3,500 (Emballonuridae); Indian flying fox 3,277 (Pteropodidae); eastern red bat 3,087 (Vespertilionidae); straw-coloured fruit bat 2,604 (Pteropodidae); black flying fox 2,406 (Pteropodidae); tricolored bat 2,154 (Vespertilionidae); lesser horseshoe bat 2,131 (Rhinolophidae); Jamaican fruit bat 1,748 (Phyllostomidae); silver-haired bat 1,624 (Vespertilionidae). Four of the twelve are pteropodids, with 13,877 records against 23,645 for the other eight. Within Pteropodidae, four species of *Pteropus* (the grey-headed, Indian, black and spectacled flying foxes) hold 12,532 of the 22,639 records.

**Alachua County, Florida.** In the app's one built region (`docs/views/no-view-us-fl-alachua.csv`), six species hold 268 records, and all of them are calling bats: Mexican free-tailed bat 179 (Molossidae), southeastern myotis 50, tricolored bat 28, evening bat 5, Seminole bat 4 and northern yellow bat 2 (all Vespertilionidae). No pteropodid is on the county's list.

**Can one view be true?** It cannot, because the commonly photographed bats meet the world in two ways.

- Calling bats, which are every family except Pteropodidae, build their surroundings from the echoes of their own calls, and their eyes are coarse: Daubenton's bat resolves about 0.6 cycles per degree.
- Flying foxes make no echolocation calls, and their eyes are nearly seven times sharper: grey-headed and black flying foxes, two of the most photographed bats, resolve about 4 cycles per degree. Their colour differs by genus as well, since *Pteropus* has two cone types and *Rousettus*, *Epomophorus* and *Eidolon*, the straw-coloured fruit bat's genus, have one.

A view that draws echoes is false for a flying fox, and a view that draws only eyes leaves out the calling bat's main sense. The most recorded species is a flying fox, eleven records ahead of the big brown bat, so neither side can be treated as an exception.

**Where the line falls.** The line falls at the family Pteropodidae. The Jamaican fruit bat is a leaf-nosed bat, so it sits on the calling side despite its name. Rousettes are pteropodids that echolocate with tongue clicks; they go with the flying foxes, and a row says what the picture leaves out.

**Recommendation.** Split the group into two views.

1. `bat` covers every family except Pteropodidae, with about three quarters of world records and every bat recorded in Alachua County. These are the commonest photographed bats, and they should get the echo picture: a depth image refreshed call by call, bright where echoes are strong (section 4). The engine cannot draw that yet. Until it can, the entry draws their coarse, nearly colourless eyes, the picture holds and jumps at a searching bat's call rate, and an `x` row says that the echoes are missing.
2. `flyingfox` covers Pteropodidae, with about a quarter of world records and the most recorded species. It is an eye view that the present engine can already draw from sourced figures.

For `tools/species/eyes.py`, the rule sends Chiroptera to `bat` and takes family Pteropodidae first to `flyingfox`, the way the vulture rule is applied before the hawk rule. `tools/species/test_eyes.py` has a case named bat (Chiroptera, Molossidae, *Tadarida*) in its test that mammals without an eye of their own go to `other`; it would move to a test that expects `bat`, with a flying fox case beside it. `labels/kinds.json` lists "a bat" under `other`; it would move to `bat`, with "a flying fox" added for `flyingfox`. In the word table of `src/cam.r.js`, "flying fox" would go to `flyingfox` and "bat" to `bat`. Today "bat" goes to `other`, and a typed "flying fox" matches "fox" in the `dog` entry and gets a dog's eyes (checked by running the table's patterns), so the new entry has to come before `dog`. "Fruit bat" is ambiguous: sending it to `flyingfox` fits most records (22,639 pteropodid records against 10,907 for the whole leaf-nosed family), and it sends the Jamaican fruit bat to the wrong view.

**Audit:** the word-table claim holds (`src/cam.r.js` line 20, `['dog', /\b(dogs?|pupp(y|ies)|fox(es)?|coyotes?|wol(f|ves))\b/]`, with first match winning at line 27). Two more places would need changing. The `other` entry on line 8 holds `\bbats?` and comes before every animal entry, so it would still catch "bat" and "fruit bat" unless the word is taken out of it or the new entries go above it. `KINDS` on line 53 decides whether a meeting counts as a new kind and how many kinds a person has met (lines 100 and 190 to 194), and has neither new key; `src/cam.rec.js` line 15 keeps a parallel `KIND_ORDER`, said to follow `tools/fusion/fuse.py`.

## 2. The rows

### `bat` (every family except Pteropodidae)

1. `['m', 'Calls', 'A big brown bat calls 5 to 10 times a second while searching, 20 to 80 times while closing in, and up to about 170 times in the final buzz. Each call returns one snapshot, so the picture holds, then jumps, about seven times a second. That rendering is this app’s invention.']`
   Source: Moss and Surlykke 2010 (call rates measured in the big brown bat; calls "yield brief acoustic snapshots of the environment"). Wilson (Britannica) gives about 10, 25 to 50, and 200 or more a second for bats in general.
2. `['m', 'Distance', 'From the delay of each echo, a big brown bat judges distance to within about 1.5 centimetres with its short hunting calls, and only to 15 centimetres or worse with its long search calls.']`
   Source: Moss and Surlykke 2010 (85 microseconds or 1.5 cm with short broadband echoes, more than 800 microseconds or 15 cm with long narrowband echoes, big brown bat).
3. `['g', 'Reach', 'A bat hears an insect’s echo from about 2 to 14 metres away, depending on the bat and the insect, and a forest edge from up to about 50 metres. Beyond that, its calls return nothing it can hear.']`
   Source: Boonman and colleagues 2013 (calculated from measured call levels and insect echo strengths: Kuhl's pipistrelle 2 to 3.5 m at a hearing threshold of 20 dB SPL and 4 to 7 m at 0 dB SPL, the greater mouse-tailed bat 2 to 6.5 m and 5.5 to 14 m; about 50 m for large landscape objects such as forest edges, after Stilz and Schnitzler 2012). Moss and Surlykke 2010 give 21 m for large objects in *Eptesicus bottae*, after Holderied and colleagues 2005. **Audit:** the text gave only the higher-threshold ranges (2 to 6.5 m) and is reworded to the full range.
4. `['m', 'Direction', 'A big brown bat swings its beam of sound from one object to the next with an accuracy of about 5 degrees. The beam spreads over a cone of 60 to 90 degrees, about as wide as this camera’s view.']`
   Source: Moss and Surlykke 2010 (aiming accuracy about 5 degrees; a cone of 60 to 90 degrees, after Hartley and Suthers 1989). The camera's field of about 70 degrees is from `docs/SOURCES.md`. **Unfinished:** this is aiming accuracy. The big brown bat's angular resolution was studied by Simmons and colleagues 1983 (named in the reference list of Simmons 1993), and that study was not opened.
5. `['g', 'Sharpness', 'Daubenton’s bat, an insect-eating relative, resolves about 0.6 cycles per degree to your 60, a hundredth of yours. The screen is blurred to match.']`
   Source: Cechetto and colleagues 2020 (*Myotis daubentonii*, 0.6 cycles per degree from ganglion cell density). Brokaw 2024 gives about 0.35 for the rufous horseshoe bat.
6. `['m', 'Dim light', 'In one test a big brown bat could no longer tell things apart by sight once the light fell to between 0 and 0.0008 lux. Shadows are lifted to suggest it.']`
   Source: Boonman and colleagues 2013 (the big brown bat failed a visual discrimination "at a light level between 0 and 0.00079 lux"; the original study was not opened).
7. `['g', 'Colour', 'Some bats have a cone for ultraviolet and some have lost it, and no phone records ultraviolet. In two leaf-nosed bats only 2 to 4 in a hundred light receptors are cones, so colour is drained here.']`
   Source: Müller and colleagues 2009 (ultraviolet-sensitive cones in *Glossophaga soricina* and *Carollia perspicillata*; cones 2 to 4% of photoreceptors); Simões and colleagues 2019 (the ultraviolet opsin gene lost in several lineages); Brokaw 2024 (lost in the greater horseshoe bat and the white-winged vampire bat; responses to ultraviolet in at least seven insect-eating species); `docs/SOURCES.md`, after Vasas and colleagues 2024 (no ordinary camera records ultraviolet; **Audit:** added).
8. `['x', 'Echoes', 'A calling bat hears the distance to everything its calls reach, and a phone’s microphone cannot hear those calls.']`
   Source: Moss and Surlykke 2010; ecoObs FAQ (the built-in microphone of an iPhone or iPad does not pick up bat calls); University of Bristol Batmobile blog, the post "Tell me more about BatMobile…" (the in-phone microphone is not up to recording ultrasonic calls); Digital Biology, Bat Recorder (on Android, audio from the built-in microphone is not ultrasonic). **Audit:** the Bristol post is corrected and the Android source added.
9. `['x', 'Magnetic compass', 'Big brown bats steer home by the Earth’s magnetic field, which the picture does not draw.']`
   Source: Holland and colleagues 2006 (homing in big brown bats shifted with an artificially shifted magnetic field).

### `flyingfox` (Pteropodidae)

1. `['m', 'Sharpness', 'Grey-headed and black flying foxes resolve about 4 cycles per degree to your 60, a fifteenth of yours and nearly seven times an insect-eating bat’s.']`
   Source: Cechetto and colleagues 2020 (*Pteropus poliocephalus*, *P. alecto* and *Rousettus aegyptiacus* about 4; *Myotis daubentonii* 0.6). Brokaw 2024 gives about 2 for the Indian flying fox.
2. `['m', 'No calls', 'Flying foxes make no echolocation calls and find their way by sight and smell.']`
   Source: Cechetto and colleagues 2020 (*P. alecto* and *P. poliocephalus* studied as non-echolocating); Boonman and colleagues 2013 ("most old world fruit bats" rely on other senses); Sunshine Coast Council (smell and eyesight).
3. `['m', 'Colour', 'Flying foxes have two cone types, a blue and a green, as most mammals do. Cones are about one in two hundred of their light receptors, so colour is muted here.']`
   Source: Müller and colleagues 2007, through ScienceDaily (*Pteropus* has two spectral cone types, "the common mammalian condition"; cones about 0.5% of photoreceptors). **Audit:** the paper's title, authors, volume and pages are confirmed on Leo Peichl's publication list; its abstract was not read, and the release does not name the *Pteropus* species studied.
4. `['g', 'One cone', 'Rousettes, epauletted fruit bats and the genus of the straw-coloured fruit bat have only the green cone and see no colour. The picture follows the flying foxes.']`
   Source: Müller and colleagues 2007, through ScienceDaily (*Rousettus*, *Eidolon* and *Epomophorus* "completely lack blue cones"; the release does not name the species studied).
5. `['g', 'Dim light', 'Bats pack 300,000 to 800,000 rods into each square millimetre of retina, two to five times your densest. Shadows are lifted to suggest it.']`
   Source: Brokaw 2024 (bats 300,000 to 800,000 rods per square millimetre; people about 150,000 at peak).
6. `['i', 'Ultraviolet', 'The gene for the blue cone of the Formosan flying fox points to ultraviolet. No phone records it, and none is drawn.']`
   Source: Wang and colleagues 2004 (*Pteropus dasymallus formosus* has a working short-wavelength opsin gene that "may be sensitive to UV light", inferred from its sequence).
7. `['x', 'Clicks', 'Rousette fruit bats echolocate with tongue clicks and land on targets as well as calling bats do, and the picture draws no echoes.']`
   Source: Yovel, Geva-Sagiv and Ulanovsky 2011 (clicks of 50 to 100 microseconds; landing and detection of medium-sized objects comparable to laryngeal echolocators); Wilson (Britannica) (rousettes evolved echolocation independently).
8. `['i', 'Field, focus and pupil', 'These are guesses, and the camera’s field is kept.']`
   Source: none found.

## 3. The picture

### `bat`

```
bat: { chip: 'Bat', who: 'a bat', cpd: .6, pupil: 'o', sat: .25, gain: 1.6, hold: 110, thrust: 30,
  cue: 'Each call brings back one snapshot, so the picture holds, then jumps.', rows: [ ...the nine rows above... ] }
```

| Field | Value | Behind it |
|---|---|---|
| `cpd` | 0.6 | Sharpness row; Cechetto and colleagues 2020 (Daubenton's bat) |
| `hold`, `thrust` | 110 and 30 ms | `invented`. The heron's held gaze is reused as a call-by-call snapshot: a cycle of 140 ms gives about 7 snapshots a second, inside the search rate of 5 to 10 (Calls row; Moss and Surlykke 2010) |
| `sat` | 0.25 | `invented`; Colour row (cones are 2 to 4 in a hundred receptors) |
| `gain` | 1.6 | `invented`; Dim light row |
| `pupil` | 'o' | `invented`. No source was found, and with `dof` unset it changes nothing |
| `fov` | unset | No field of view for a bat's eyes was found, and the beam's cone of 60 to 90 degrees is about as wide as the camera's view of about 70 (Direction row) |
| `topoA`, `topoS`, `fall`, `fovea` | unset | Daubenton's bat has a sharp area in the upper retina (Cechetto and colleagues 2020), and no field places sharpness off centre (section 4) |
| `dof` | unset | `invented`. Depth belongs to the echoes (section 4) |
| `M`, `sheen`, `uvBlue` | unset | Colour row: some bats have lost the ultraviolet cone, and none is drawn |
| `rate` | unset | No flicker-fusion figure for any bat was found |
| `persist`, `gate`, `field` | unset | Nothing sourced calls for them |

The lowest `cpd` now in use is 1, for bees and insects. At 0.6, the 24 degrees that the app assumes for a phone screen hold about 14 cycles from edge to edge, so the value should be checked on a phone. The hold acts only on the live camera, as the heron's does.

### `flyingfox`

```
flyingfox: { chip: 'Flying fox, fruit bat', who: 'a flying fox', cpd: 4, pupil: 'o', M: DEUTAN, sat: .7, gain: 1.5,
  cue: 'The picture is coarse and muted, and the shadows are lifted.', rows: [ ...the eight rows above... ] }
```

| Field | Value | Behind it |
|---|---|---|
| `cpd` | 4 | Sharpness row; Cechetto and colleagues 2020 (grey-headed and black flying foxes) |
| `M` | DEUTAN | `invented` choice of model, following the app's cat, dog and deer. Colour row: two cone types in *Pteropus*. Which human model fits depends on where the long-wave cone peaks (open question 4) |
| `sat` | 0.7 | `invented`; Colour row (cones are about one in two hundred receptors) |
| `gain` | 1.5 | `invented`; Dim light row |
| `pupil` | 'o' | `invented`; Field, focus and pupil row |
| `fov`, `topoA`, `topoS`, `fall`, `dof` | unset | Field, focus and pupil row; nothing was found |
| `sheen`, `uvBlue` | unset | Ultraviolet row |
| `rate`, `persist`, `gate`, `hold`, `field` | unset | Nothing sourced calls for them |

## 4. What the engine cannot draw yet

**A depth image made from echoes (`bat`, and the rousettes' clicks).**
- *What it would show.* The picture would have no colour and no surface pattern. Each point would take its brightness from the strength of its echo: bright where a surface is near, large, hard and facing the bat, and dark where it is far, small, soft or slanted away (general acoustics, unsourced here). How fast strength falls with distance and angle would be the app's own model, because no source I opened gives it. Nothing would show beyond reach: insects would fade out by about 2 to 14 m and large surfaces by about 20 to 50 m (Boonman and colleagues 2013; Moss and Surlykke 2010; **Audit:** the insect range is corrected from 2 to 6.5 m). The image would fill a cone of 60 to 90 degrees and be brightest along its axis. Depth would be blurred to 15 cm or more in search and sharpened to about 1.5 cm when closing in, and direction would be blurred to about 5 degrees (Moss and Surlykke 2010). The picture would freeze between calls and refresh once per call: 5 to 10 times a second in search, 20 to 80 in approach and about 170 in the buzz. It could step up through approach and buzz as the nearest thing in the centre comes close, at distances the app would choose. The `hold` and `thrust` values in section 3 are the part of this that the present engine can already make.
- *Phone input.* The microphone cannot stand in, because built-in phone microphones do not pick up bat calls (ecoObs FAQ; Bristol Batmobile blog), and a phone would also have to send calls out; I opened no source on phone speakers and ultrasound. Two other inputs can supply depth. (1) The depth sensor: Apple's Pro handhelds have carried a LiDAR scanner since 2020 that measures up to 5 m (phyphox), about an insect's echo range, so on those devices its depth map could be drawn directly as the echo image. Whether the app's web and native builds can read it was not checked. (2) The camera with a depth model: monocular depth estimation predicts depth from a single image (Hugging Face documentation, which names Depth Anything V2 for relative depth and ZoeDepth for absolute depth). The app already names creatures with image models (`models/`), so a small depth model run on each frame is the route on phones without a depth sensor. Model size and speed on a phone were not checked.
- *How hard.* It is hard: it needs a new drawing mode (depth to brightness, the cone, the blur in depth and direction, and the hold at the call rate) and a source of depth, and it is easiest on LiDAR phones and slower and less sure with a model.

**A sharp area off centre (`bat`).** Daubenton's bat has its specialized area in the dorsal, or upper, retina (Cechetto and colleagues 2020). Because an eye's image is inverted, that area would look at the lower part of the field; this is my inference, and the source does not say it. The engine places sharpness only at the centre (`topoA`) or along the horizon (`topoS`). The view would show a sharp patch below centre, it needs no input beyond the camera, and it is easy to add as a vertical offset once a scientist confirms where the area looks.

**The magnetic compass (`bat`).** The phone's magnetometer gives a heading, which could orient or tint the picture toward magnetic north. Nothing I opened says what a compass sense is like to have, so it stays a row. Reading the sensor is easy, and drawing it honestly has no basis yet.

**Smell (`flyingfox`).** No phone input stands in for it, so it stays in the No calls row.

**Ultraviolet (both views).** No ordinary phone camera records it (`docs/SOURCES.md`, after Vasas and colleagues 2024). The invented sheen that the app gives birds, reptiles and insects is left off here, because several bat lineages have lost the cone.

## 5. Sources

- GBIF, occurrence search on the iNaturalist research-grade dataset `50c9509d-22c7-4a22-a47d-8c48425ef4a7`, `orderKey=734`, faceted by `familyKey` and by `speciesKey`, and `familyKey=9367` and `9368` faceted by species, read 11 October 2026, https://api.gbif.org/v1/occurrence/search: 93,809 bat records and the family and species counts in section 1. **opened**
- GBIF species pages for keys 9368, 9367, 9366, 9615, 9616, 9365, 3239753, 7456382, 5218655, 5787518, 2432851, 5218686, 2432837, 5218680, 2432352, 5218543, 2433095, 2432614, 2433272 and 2432341, https://api.gbif.org/v1/species/<key>: family and species names for those keys. Keys 5719, 5449, 5718, 5448, 5447, 5451 and 5450 were named from GBIF name lists stored on the repository's `ci` branch (`runs/fetch/10/names-family-animalia-*.json`), and keys 2433011 and 7665644 from `data/regions/us-fl-alachua/species.json`. **opened**
- GBIF backbone record for Chiroptera (key 734), description field, stored on the repository's `ci` branch (`runs/fetch/10/names-order-0.json`): "Includes as suborders Megachiroptera, with the single family Pteropodidae, and Microchiroptera, with the remainder." **opened**
- The repository's `docs/views/no-view-us-fl-alachua.csv`: Alachua County bat species and counts. `docs/SOURCES.md`: a phone picture covers about 70 degrees, and no ordinary camera records ultraviolet (Vasas and colleagues 2024). **opened**
- Moss, C.F. and Surlykke, A., 2010, Probing the natural scene by echolocation in bats, Frontiers in Behavioral Neuroscience 4:33, doi:10.3389/fnbeh.2010.00033: big brown bat call rates of 5 to 10, 20 to 80 and up to about 170 a second; "brief acoustic snapshots"; range accuracy of 1.5 cm with short broadband echoes and more than 15 cm with long narrowband echoes; aiming accuracy about 5 degrees; a beam cone of 60 to 90 degrees; 21 m reach for large objects in *Eptesicus bottae* (after Holderied and colleagues 2005); calls measured in *Myotis nattereri* and *Saccopteryx bilineata*. **opened** (full text)
- Boonman, A., Bar-On, Y., Cvikel, N. and Yovel, Y., 2013, It's not black or white: on the range of vision and echolocation in echolocating bats, Frontiers in Physiology 4:248, doi:10.3389/fphys.2013.00248: insect detection calculated at 2 to 3.5 m (Kuhl's pipistrelle) and 2 to 6.5 m (greater mouse-tailed bat) for a hearing threshold of 20 dB SPL, and 4 to 7 m and 5.5 to 14 m for 0 dB SPL; about 50 m for large landscape objects such as forest edges; the big brown bat's visual failure between 0 and 0.00079 lux; acuity in insect-eating bats of 0.3 to 5 degrees; most Old World fruit bats rely on other senses. **opened** (full text)
- Cechetto, C., de Busserolles, F., Jakobsen, L. and Warrant, E.J., 2020, Retinal ganglion cell topography and spatial resolving power in echolocating and non-echolocating bats, Brain, Behavior and Evolution 95(2):58 to 68, doi:10.1159/000508863: about 4 cycles per degree in *Pteropus alecto*, *P. poliocephalus* and *Rousettus aegyptiacus*; 0.6 in *Myotis daubentonii*; a dorsal specialized area in *M. daubentonii*. **opened** (abstract, University of Southern Denmark research portal)
- Müller, B., Goodman, S.M. and Peichl, L., 2007, Cone photoreceptor diversity in the retinas of fruit bats (Megachiroptera), Brain, Behavior and Evolution 70(2):90 to 104: cones about 0.5% of photoreceptors; two cone types in *Pteropus*; only the long-wave cone in *Rousettus*, *Eidolon* and *Epomophorus*. **secondary**: ScienceDaily release, https://www.sciencedaily.com/releases/2007/06/070615093131.htm; title, volume and pages from the reference list of the Sunshine Coast Council page. **Audit:** author order corrected from Leo Peichl's publication list, https://www.uni-frankfurt.de/87973921/Publikationen_Prof__Leo_Peichl ("Müller B, Goodman SM, Peichl L (2007)"); the abstract was not read.
- Müller, B., Glösmann, M., Peichl, L., Knop, G.C., Hagemann, C. and Ammermüller, J., 2009, Bat eyes have ultraviolet-sensitive cone photoreceptors, PLoS ONE 4(7):e6390, doi:10.1371/journal.pone.0006390: ultraviolet-sensitive cones in *Glossophaga soricina* and *Carollia perspicillata*; cones 2 to 4% (about 3%) of photoreceptors. **opened**
- Simões, B.F., Foley, N.M., Hughes, G.M., Zhao, H., Zhang, S., Rossiter, S.J. and Teeling, E.C., 2019, As blind as a bat? Opsin phylogenetics illuminates the evolution of color vision in bats, Molecular Biology and Evolution 36(1):54 to 68, doi:10.1093/molbev/msy192: the ultraviolet opsin gene lost in several lineages, linked to cave roosting in most pteropodids, and working in the echolocator *Pteronotus parnellii*. **opened** (abstract, University of Plymouth research portal)
- Wang, D., Oakley, T., Mower, J., Shimmin, L.C., Yim, S., Honeycutt, R.L., Tsao, H. and Li, W.-H., 2004, Molecular evolution of bat color vision genes, Molecular Biology and Evolution 21(2):295 to 302, doi:10.1093/molbev/msh015: working long-wave and short-wave opsin genes in *Haplonycteris fischeri*, *Pteropus dasymallus formosus* and *Myotis velifer*; the short-wave opsin may be sensitive to ultraviolet (inferred from sequence). **opened** (abstract, Oxford Academic)
- Brokaw, A., 2024, Blind as a bat? No such thing, Bat Conservation International, 14 June 2024, https://www.batcon.org/blind-as-a-bat-no-such-thing/: rufous horseshoe bat about 0.35 cycles per degree; Indian flying fox and ghost bat about 2; rods 300,000 to 800,000 per square millimetre against about 150,000 in people; up to 2% cones; the ultraviolet cone lost in the greater horseshoe bat and the white-winged vampire bat; responses to ultraviolet in at least seven insect-eating species. The page names no papers. **opened**
- Holland, R.A., Thorup, K., Vonhof, M.J., Cochran, W.W. and Wikelski, M., 2006, Bat orientation using Earth's magnetic field, Nature 444(7120):702, doi:10.1038/444702a: big brown bats home by a magnetic compass. **opened** (record and short abstract on RePEc/IDEAS and QxMD)
- Yovel, Y., Geva-Sagiv, M. and Ulanovsky, N., 2011, Click-based echolocation in bats: not so primitive after all, Journal of Comparative Physiology A 197(5):515 to 530, doi:10.1007/s00359-011-0639-4: *Rousettus* clicks of 50 to 100 microseconds; landing and detection comparable to laryngeal echolocators. **opened** (abstract, Tel Aviv University research portal)
- Yovel, Y., Falk, B., Moss, C.F. and Ulanovsky, N., 2011, Active control of acoustic field-of-view in a biosonar system, PLoS Biology 9(9):e1001150, doi:10.1371/journal.pbio.1001150: Egyptian fruit bats adjust click loudness and the angle between successive beams with distance and clutter. **opened** (abstract on DOAJ). Background only; no row uses a figure from it. **Audit:** not confirmed, because the PLoS page refused the request (HTTP 429).
- Wilson, D.E., Bat: Orientation, Encyclopaedia Britannica, https://www.britannica.com/animal/bat-mammal/Orientation: about 10 pulses a second in search, 25 to 50 in approach, 200 or more in a terminal phase of about 100 ms; cruising pulses of 1.5 ms in the greater false vampire bat, 4 ms in Wagner's mustached bat and 55 to 65 ms in the greater horseshoe bat; wires of 0.08 to 0.1 mm avoided; rousettes evolved echolocation independently. **opened**
- Gessinger, G., Page, R., Wilfert, L., Surlykke, A., Brinkløv, S. and Tschapka, M., 2021, Phylogenetic patterns in mouth posture and echolocation emission behavior of phyllostomid bats, Frontiers in Ecology and Evolution 9:630481, doi:10.3389/fevo.2021.630481: leaf-nosed bats, the Jamaican fruit bat among the species filmed, echolocated in all flight sequences; their calls are usually under 2 ms, multiharmonic and frequency-modulated. **opened** (full text)
- Gillam, E.H., McCracken, G.F., Westbrook, J.K., Jensen, M.L. and Balsley, B.B., Bats aloft: variation in echolocation call structure at high altitudes, Society for Integrative and Comparative Biology, meeting abstract 1.9 (the page gives no year), https://sicb.org/abstracts/bats-aloft-variation-in-echolocation-call-structure-at-high-altitudes/: echolocation calls of *Tadarida brasiliensis* recorded from 0 to 862 m above ground. **opened**
- Elemans, C.P.H., Mead, A.F., Jakobsen, L. and Ratcliffe, J.M., 2011, Superfast muscles set maximum call rate in echolocating bats, Science 333(6051):1885, doi:10.1126/science.1207309: up to 190 calls a second in the buzz. **secondary**: University of Pennsylvania release on ScienceDaily, https://www.sciencedaily.com/releases/2011/09/110929152102.htm. Background only.
- Simmons, J.A., 1993, Evidence for perception of fine echo delay and phase by the FM bat, *Eptesicus fuscus*, Journal of Comparative Physiology A 172:533 to 547, doi:10.1007/BF00213677: used only for the name of the 1983 study on horizontal angle discrimination in its reference list. **opened** (abstract page, Springer). **Audit:** the reference list gives Simmons, J.A., Kick, S.A., Lawrence, B.D., Hale, C., Bard, C. and Escudié, B., 1983, Acuity of horizontal angle discrimination by the echolocating bat, *Eptesicus fuscus*, Journal of Comparative Physiology 153:321 to 330.
- Sunshine Coast Council, The truth about flying fox vision, https://www.sunshinecoast.qld.gov.au/Environment/Education-Resources-and-Events/environment-resources-and-publications/native-animals/truth-about-flying-fox-vision: only microbats echolocate, and megabats use smell and eyesight. The page's claim that flying foxes lack a red cone was not used (open question 4). **opened**
- ecoObs, EcoBatRec FAQ, https://ecobatrec.ecoobs.com/faq.html: "the built in mic of the iPad or iPhone will not pick up bat calls"; USB microphones up to 384 kHz work. **opened**
- University of Bristol, Batmobile blog, https://batmobile.blogs.bristol.ac.uk/tag/uob: in "Tell me more about BatMobile…" (Dave Kilbey, 4 October 2012), "because bat calls are ultrasonic there's no way that the in-phone mic will be up to the job"; in "Audio Analysis on an iPhone" (markvr, 20 December 2012), recording without time expansion would need equipment that samples at 100 kHz. **opened**. **Audit:** the microphone statement is in the first post, and the sheet had named the second.
- Digital Biology, Bat Recorder, https://www.digitalbiology.com/batrecorder: an Android app page; audio from the built-in microphone "will not be ultrasonic", and ultrasound needs a USB microphone. **opened** by the audit.
- phyphox, LiDAR, https://phyphox.org/lidar/: Apple's Pro handhelds have had a LiDAR scanner since March 2020, measuring up to 5 m. **opened**
- Hugging Face, Monocular depth estimation (Transformers documentation), https://huggingface.co/docs/transformers/tasks/monocular_depth_estimation: depth predicted from a single image; Depth Anything V2 (relative) and ZoeDepth (absolute). **opened**
- Opened and not used: Thiagavel, J., Cechetto, C. and Santana, S.E. (as listed on the record), 2018, Auditory opportunity and visual constraint enabled the evolution of echolocation in bats, USF Digital Commons record, https://digitalcommons.usf.edu/kip_articles/323. The record says "This paper has been withdrawn". I could not tell whether that refers to the record or to the paper, so nothing here rests on it.

## 6. Open questions for a sensory scientist

1. For blurring direction in an echo image of a big brown bat, which figure fits: the horizontal angle discrimination threshold of Simmons and colleagues 1983 (not opened here), the aiming accuracy of about 5 degrees, or the beam width?
2. Is a depth image with brightness from echo strength a fair picture of what a calling bat builds, or would sparse points at strong echoes be truer? How should echo strength fall with distance and angle for a big brown bat's calls of about 25 to 65 kHz?
3. Where in the visual field does the dorsal specialized area of Daubenton's bat look, and do the big brown bat, the Mexican free-tailed bat and the eastern red bat have a streak, a spot or neither?
4. For flying foxes, what are the retinal layout, the field of view and the pupil shape, and where does the long-wave cone peak? A council education page says that flying foxes lack the red cone, as in protanopia, and the answer decides between the app's protan and deutan models.
5. At what light do the Mexican free-tailed bat and the big brown bat stop using sight, and do the commonest evening bats and free-tailed bats keep a working ultraviolet cone?

## Unfinished, and pages I could not read

- For Hipposideridae, Miniopteridae, Nycteridae, Noctilionidae, Natalidae and Thyropteridae (3,815 records), placement on the calling side rests on GBIF's note on the order and the Sunshine Coast Council page, with no study of those families opened.
- Angular resolution is given only as aiming accuracy (5 degrees), because Simmons and colleagues 1983 was not opened.
- No flicker-fusion rate for any bat was found, so `rate` is unset in both views.
- No figure measured in the Mexican free-tailed bat, the most recorded bat in Alachua County, was found.
- Müller and colleagues 2007 and Elemans and colleagues 2011 rest on press releases. **Audit:** the author order of the 2007 paper is now checked and corrected; its abstract is still unread.
- Pages I could not read: PubMed Central articles came back as a browser check page with no article on it. Europe PMC's search service refused the request with HTTP 429 (rate limited). Permission requests were withdrawn before they were answered for https://www.pnas.org/doi/10.1073/pnas.1006630107, https://www.nature.com/articles/s41467-017-02532-x, https://karger.com/bbe/article/70/2/90/48023, https://github.com/isl-org/MiDaS, https://arxiv.org/abs/2406.09414 and iNaturalist's species-count API. Shell access to api.gbif.org was refused by the session's network policy (HTTP 403 at the proxy), so the GBIF figures came through WebFetch.
- **Audit:** pages refused during the audit were Karger's copy of Cechetto and colleagues 2020 and Springer's copy of Yovel, Geva-Sagiv and Ulanovsky 2011 (both read on university portals instead), the PLoS Biology page of Yovel, Falk, Moss and Ulanovsky 2011, Europe PMC, and PubMed's record of Wang and colleagues 2004 (read on Oxford Academic instead). The studies cited inside the sources (Ellins and Masterson 1974, Hartley and Suthers 1989, Surlykke and colleagues 2009a, Holderied and colleagues 2005, Stilz and Schnitzler 2012, Simmons and colleagues 1983) were not opened.
- **Audit:** a question for the scientist. Boonman, Bumrungsri and Yovel 2014 (Current Biology 24(24):2962 to 2967, doi:10.1016/j.cub.2014.10.077; abstract opened at https://cris.iucc.ac.il/en/publications/nonecholocating-fruit-bats-produce-biosonar-clicks-with-their-win/) report two "nonecholocating" fruit bat species that detect objects with clicks made by their wings, without naming them in the abstract. Whether the lesser short-nosed fruit bat (*Cynopterus brachyotis*, 1,274 records, the fifth most recorded pteropodid) is one of them was not checked. No row rests on this.
