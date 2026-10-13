# Sensing sheet, round 3: spider (order Araneae, every family except Salticidae)

Written on 13 October 2026, from 01:45 UTC. The evidence log is `docs/views/evidence/spider.jsonl`; "Log 43, 44" below means lines 43 and 44 of that file, each a single measurement with its source, page and quote. The wanted list is `docs/views/wanted/spider.jsonl`. Jumping spiders (Salticidae) belong to the `jumper` unit and appear here only for comparison.

Read for this sheet: the collection topics `spider-web-tarantula`, `spider-night`, `spider-general`, `spider-day` and `arachnids-other` (titles and abstracts searched, full texts read where the folder holds them); the owner's library copies of eight papers and parts of four books (section 7 lists which chapters came through); publisher abstract pages, a university thesis repository and the MDN pages on phone sensors. Unfinished parts are marked in section 5.

## 1. Scope

### Taxa and records

The unit covers every spider outside family Salticidae. GBIF holds 2,927,814 iNaturalist research-grade spider records (dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7, orderKey 1496, family facet, read 13 October 2026; the total is unchanged since the earlier sheet's reading of 11 October). Salticidae holds 684,540 of them, which leaves **2,243,274 records** for this unit. The 59 other families in the facet's top 60 hold 2,235,165; the families below the top 60 hold 8,109 (0.4%).

| Family | Common name | World records | Share of this unit | Proposed view |
|---|---|---:|---:|---|
| Araneidae | orb weavers | 918,443 | 40.9% | `spider` |
| Theridiidae | cobweb spiders | 195,578 | 8.7% | `spider` |
| Thomisidae | crab spiders | 173,427 | 7.7% | `crabspider` |
| Pisauridae | nursery web and fishing spiders | 161,306 | 7.2% | `hunter` |
| Lycosidae | wolf spiders | 125,899 | 5.6% | `hunter` |
| Tetragnathidae | long-jawed orb weavers | 92,534 | 4.1% | `spider` |
| Agelenidae | funnel weavers | 61,822 | 2.8% | `spider` |
| Sparassidae | huntsman spiders | 61,542 | 2.7% | `hunter` |
| Pholcidae | cellar spiders | 55,684 | 2.5% | `spider` |
| Oxyopidae | lynx spiders | 49,795 | 2.2% | `crabspider` |
| Theraphosidae | tarantulas | 42,576 | 1.9% | `tarantula` |
| Linyphiidae | sheet weavers | 32,339 | 1.4% | `spider` |
| Philodromidae | running crab spiders | 25,024 | 1.1% | `crabspider` |
| Gnaphosidae | ground spiders | 24,825 | 1.1% | `tarantula` |
| Zoropsidae | | 19,454 | 0.9% | `hunter` |
| Dysderidae | woodlouse hunters | 17,714 | 0.8% | `tarantula` |
| Scytodidae | spitting spiders | 13,309 | 0.6% | `tarantula` |
| Anyphaenidae | ghost spiders | 12,406 | 0.6% | `tarantula` |
| Sicariidae | recluses | 11,191 | 0.5% | `tarantula` |
| Corinnidae | | 11,106 | 0.5% | `tarantula` |
| Ctenidae | wandering spiders | 10,905 | 0.5% | `hunter` |
| Deinopidae | net-casting spiders | 2,849 | 0.1% | `netcaster` |
| 37 more families in the top 60 | | 115,437 | 5.1% | by family, below |
| families outside the top 60 | | 8,109 | 0.4% | `spider` (the order rule) |

Family names for the GBIF keys were read from `https://api.gbif.org/v1/species/<key>` for every key the repository's cached name list lacked.

**Alachua County, Florida** (`docs/views/no-view-us-fl-alachua.csv`, records through 2024): 4,660 spider records, of which Salticidae holds 1,107, leaving **3,553 records** for this unit in 122 species. The most recorded are the Golden Silk Spider (*Trichonephila clavipes*, 702), the Mabel Orchard Orbweaver (*Leucauge argyrobapta*, 415), the Yellow Garden Spider (*Argiope aurantia*, 275), the Green Lynx Spider (*Peucetia viridans*, 246), the Spinybacked Orbweaver (*Gasteracantha cancriformis*, 228), the White-banded Fishing Spider (*Dolomedes albineus*, 153), the Brown Widow (*Latrodectus geometricus*, 108), the Ogre-faced Spider (*Deinopis spinosa*, 88), the Pantropical Huntsman Spider (*Heteropoda venatoria*, 77), the Six-spotted Fishing Spider (*Dolomedes triton*, 76) and the Tailed Cellar Spider (*Crossopriza lyoni*, 73).

### Where the views split

Four lines divide spiders that people photograph into groups that meet the world differently enough that one picture would be false for the other side.

**Line 1: a web, or no web.** Web builders find prey almost entirely through the silk. Orb and sheet weavers carry only 7 to 11 airflow hairs (trichobothria) on a leg, where the wandering spider *Cupiennius salei* carries close to a thousand in all (Log 30, 33, 121). A flying insect only makes an orb weaver lift its front legs in defence, and prey capture needs thread vibration (Log 34, 251); an airflow stimulus never made a web spider jump (Log 123). The side eyes of most web builders carry a canoe-shaped mirror that gives a blurred, astigmatic image (Log 67, 70, 94), and the axes of their eyes spread evenly round the body in a halo, where visual hunters cluster several eye pairs at the front (Log 106, 107). A cellar spider hunts with little or no use of vision (Log 229). Hunting spiders without webs carry grate-shaped mirrors behind large rear eyes, see down to moonlight and find prey by sight, airflow and ground vibration (Log 20, 68, 138, 153, 201). Shares: web builders 1,423,379 records (63.5% of this unit) and 2,612 in Alachua (73.5%); everything else 36.5% and 26.5%.

**Line 2: among the hunters, the slow night eyes of wandering spiders against the fast day eyes of the ambushers on plants.** A wandering spider's eyes stop following flicker at 4.3 to 8.6 Hz (Log 206) and see below 0.01 lux (Log 138). A day-active crab spider's side and rear eyes follow 20 to 30 Hz (Log 110 to 112), and its front middle eyes are 2.3 log units less sensitive than the others (Log 118). Crab spiders analyze the space in front with four eyes at once (Log 58) and see sharply only very close, noticing movement to about 20 cm (Log 101). Wolf, fishing, huntsman and wandering spiders hold 385,294 records (17.2%) and 467 in Alachua (13.1%); crab, lynx and running crab spiders hold 248,246 (11.1%) and 308 in Alachua (8.7%). Lynx spiders are placed with the crab spiders partly by inference: the Green Lynx Spider waits on flowers and strikes at insects within a centimetre, as crab spiders do (Log 269, 270, 101), lynx spiders cluster their eyes at the front like other visual hunters (Log 106), and their eyes are known only from histology (Log 221 to 223).

**Line 3: the net-casting spiders.** Their two rear middle eyes are probably the largest simple eyes in arthropods, with an F-number of 0.58, no mirror layer, and receptors that each absorb about 2,000 times as much light as a human or jumping spider receptor viewing the same field (Log 1, 2, 10, 11). They hunt by sight at night with a net held in the front legs, and they strike backward at sounds (Log 14, 135, 259). The hunter picture would be false for them in field, sensitivity and hearing. Deinopidae holds 2,849 records (0.1%) and 88 in Alachua (2.5%), where the Ogre-faced Spider is the eighth most recorded spider of this unit.

**Line 4: tarantulas and the ground hunters.** Tarantulas and other mygalomorphs carry the primitive sheet-like mirror (Log 66), small eyes bunched on a mound (Log 105), and in the purse-web and trapdoor families corneas that block ultraviolet (Log 190). A trapdoor spider catches prey as well with its eyes covered (Log 183); tarantulas locate prey with airflow hairs and club-shaped foot hairs that feel the soil tremble (Log 178), and court by signals through the ground (Log 180, 181). Ground, sac, recluse and spitting spiders also hunt without a web, and their eyes are small: canoe-mirror eyes in ground and sac spiders (Log 67), six eyes in several families (Log 104), one receptor class in a recluse (Log 191), and in some ground spiders two lensless eyes turned into a sky compass (Log 155, 217). They hold 175,397 records (7.8%: 56,634 mygalomorphs and 118,763 ground and sac spiders) and 78 in Alachua (2.2%).

Lines considered and left inside a view: fishing spiders (*Dolomedes*) feel water-surface waves (Log 243 to 248) and get a genus setting inside `hunter`; huntsman spiders resolve more coarsely (Log 226) and stay in `hunter`; cobweb and cellar spiders hang in tangles (Log 231 to 236) and stay in `spider` with a different web drawing.

### The views, committed

| View | Chip | Families | World share of this unit | Alachua share | The picture in one line |
|---|---|---|---:|---:|---|
| `spider` | Spider | every family not named below: Araneidae, Theridiidae, Tetragnathidae, Agelenidae, Pholcidae, Linyphiidae, Uloboridae, Desidae, Dictynidae, Filistatidae, Amaurobiidae, Oecobiidae, Arkyidae, Segestriidae, Eresidae, Mimetidae, Hypochilidae, Stiphidiidae, Hahniidae, Titanoecidae, Cybaeidae, Nesticidae and the families outside the top 60 | 63.9% (with the 0.4% outside the top 60) | 73.5% | a coarse, soft, faint picture under a web that ripples when the phone is knocked or a sound arrives |
| `hunter` | Wolf, fishing or huntsman spider | Lycosidae, Pisauridae, Sparassidae, Ctenidae, Trechaleidae, Zoropsidae, Selenopidae | 17.2% | 13.1% | the whole circle squeezed into the screen, lifted in the dark, slow, with moving things glowing grey and the ground's tremors arriving as ripples |
| `crabspider` | Crab or lynx spider | Thomisidae, Oxyopidae, Philodromidae | 11.1% | 8.7% | a wide, coarse, daylight picture with a fast surround and a slow second picture stepping along in front |
| `netcaster` | Net-casting spider | Deinopidae | 0.1% | 2.5% | the ground below by starlight, lifted far, grainy and grey, whipping back at a hum |
| `tarantula` | Tarantula or ground spider | Mygalomorphae (all families) and Gnaphosidae, Dysderidae, Scytodidae, Anyphaenidae, Sicariidae, Corinnidae, Cheiracanthiidae, Trachelidae, Miturgidae, Clubionidae, Hersiliidae, Lamponidae, Liocranidae, Phrurolithidae, Trochanteriidae, Zodariidae, Palpimanidae | 7.8% | 2.2% | a dark, nearly blind picture in which knocks and soft taps on the table arrive as ripples and moving air stirs the edges |

In `tools/species/eyes.py` this is a set of family rules placed before the order rule (Araneae goes to `spider`), as Salticidae goes to `jumper`. Mygalomorph families are listed one by one there, since the tool matches families. Hersiliidae, Zoropsidae and Selenopidae were placed by hunting mode alone; no source opened here measures their eyes.

## 2. The views

Rows are written in the form of `EYES` in `src/cam.a.js`. Picture fields use the names of `paramsOf` on `main` and the fields the engine branch `agent/engine` has added (`zones`, `salience`, `glow`, `glowC`, `gaze`, `ripple`, `senses`, `byGenus`, `cue`). `SIDE_GREEN` is the engine branch's invented matrix for a single green receptor. Engine fields that do not exist yet are marked **new**.

### 2.1 `spider`: web builders

#### Rows

`['m', 'The web', 'A Golden Silk Spider feels its prey through the silk. A trapped insect shakes the web 5 to 30 times a second, and the shaking reaches some legs ten to thirty times more strongly than others, which tells the spider where the insect is. A knock on the phone, or on the table under it, sends a ripple in from that side.']`
Log 43, 44, 47 (Landolfa and Barth 1996, *Trichonephila clavipes*; 20 to 30 dB is a ratio of 10 to 32 in amplitude). The ripple is the engine branch's knock input.

`['m', 'Feeling for still prey', 'When an insect in the web goes still, an orb weaver plucks the threads and feels how they answer. One orb weaver found a speck weighing 0.4 milligrams this way, 6 centimetres from the hub, in three trials out of four. Tap the screen to pluck, and whatever moves answers brighter for a moment.']`
Log 49 (*T. clavipes* shakes the web to find a still object), 252 (*Zygiella x-notata*, Klärner and Barth 1982), 195 (*Uloborus diversus* crouches or shakes the web when prey goes quiet, Hung and colleagues 2026).

`['m', 'Wind', 'Wind shakes an orb web most strongly at under 10 shakes a second, and orb weavers seldom attack anything shaking that slowly. This view lets the slow sway of your hand pass and answers only sharp knocks.']`
Log 40, 42 (Masters 1984, *Larinioides sclopetarius*).

`['m', 'Hearing through silk', 'A bridge spider hears through its web, because the silk moves with the air. Half of the spiders tested turned or crouched at a tone of 68 decibels from a loudspeaker 3 metres away, and the web gives each one a listening surface up to 10,000 times its own size. With the microphone on, this view makes the web shimmer when a sound arrives.']`
Log 130, 131, 258 (Zhou and colleagues 2022; 6 of 12 at 68 dB and 11 of 12 at 88 dB, both at 200 Hz; the 10,000 is the authors' estimate).

`['m', 'Noise', 'Traffic noise slows an orb weaver’s answer to its web. In quiet, Banded Garden Spiders responded to a cricket that landed in the web within a third of a second, and with street noise playing, many took 5 to 10 seconds. In a loud place this view’s ripples fade.']`
Log 240, 241 (De and Blackledge 2026, *Argiope trifasciata*; 0.29 s in quiet, 4.89 s on average under 75 to 85 dB traffic noise, 40% of responders at 5 to 10 s).

`['m', 'Eyes', 'Orb weavers have eight small eyes, and parts of them form no sharp image at all. A mirror layer behind six of the eyes sends light back through the light-sensing cells for a second chance at catching it, and blurs what image there is. This view is coarse and soft.']`
Log 91 (eight eyes), 67 and 94 (canoe-shaped mirror in Araneidae, about a quarter of the retina in *Araneus*), 70 (blurred, astigmatic line image), 261 (the mirror's job).

`['g', 'Sharpness', 'The eyes of web builders have hardly been measured. In a funnel weaver the light-sensing cells in most of its eyes sit about 3 degrees apart, which gives under a three-hundredth of your sharpness. This view uses that figure.']`
Log 92 (web builders' eyes unstudied), 71 (*Tegenaria*, 3 degrees; 1 / (2 × 3) = 0.17 cycles per degree, and 0.17 / 60 is 1/360).

`['m', 'Colour', 'Garden spiders of the genus Argiope see green best with all eight eyes, and they also answer ultraviolet light, most strongly with the two front middle eyes. In two species studied in Japan, single cells of those front eyes include a blue-sensing kind as well. This view keeps colour faint and leans it green.']`
Log 271 to 274 (Tiedemann, Ventura and Ades 1986, *Argiope argentata*: 525 nm in the principal eyes, 530 nm in the others, one receptor type from 425 to 625 nm, ultraviolet responses strongest in the principal eyes), 165 to 167 (Yamashita and Tateda 1978: 360, 480 to 500 and 540 nm in single cells of the anterior median eyes of *A. bruennichi* and *A. amoena*), 168 (one class in the anterior lateral eyes).

`['m', 'Night', 'The eyes of orb weavers grow more sensitive and slower at night, on a daily rhythm set by signals from the brain. After dark by your phone’s clock, this view lifts dim light further and lets movement smear more.']`
Log 267, 268 (Yamashita's project report: the anterior lateral eyes of *Argiope bruennichi* and *A. amoena* gain sensitivity in the night state and their receptor responses broaden, under efferent control), 256 (Yamashita and Nakamura 1999, the principal eyes of *Araneus ventricosus*; a day-active jumping spider showed no rhythm), 86.

`['m', 'Cobwebs and cellar spiders', 'Widows and cellar spiders hang in tangled webs. Flies caught in a widow’s web shake it about 30 times a second, and a courting male shakes it near 50 times a second, far more gently. A cellar spider hunts with almost no use of its eyes.']`
Log 231, 234, 235 (Vibert and colleagues 2014, *Latrodectus hesperus*: 28.6 Hz flies, 31.8 Hz crickets, 52.3 Hz males; 21 mm/s against 1.9 mm/s), 229 (Jackson and Brassington 1987, *Pholcus phalangioides*).

`['i', 'How the picture is drawn', 'Nobody knows what a web feels like to its spider, or how fast an orb weaver’s eyes are. This view draws a faint web that ripples when the phone is knocked or a sound arrives, draws what moves brighter than what stays still, and borrows its slow pace from a wandering spider. Those choices are the app’s own.']`
Log 34, 48 (vibration leads prey capture), 134 (side eyes regarded as motion detectors), 206 (*Cupiennius*, 4.3 to 8.6 Hz, borrowed).

`['x', 'Smell', 'A male garden spider smells the scent of a female through pores in the hairs on all his walking legs. The picture leaves smell out.']`
Log 203 (Talukder and colleagues 2025, *Argiope bruennichi*).

#### The picture

```
spider: { chip: 'Spider', who: 'a spider', fov: 340, cpd: .17, pupil: 'o', M: SIDE_GREEN, sat: .35, gain: 1.3, gate: .6, persist: .15,
  salience: 1, glow: .5, glowC: [.85, .85, .85], ripple: 1, senses: { motion: true, jolt: true, mic: [100, 10000] },
  web: 'orb', byFamily: { Theridiidae: { web: 'tangle' }, Pholcidae: { web: 'tangle' }, Linyphiidae: { web: 'sheet' }, Agelenidae: { web: 'funnel' } },
  pluck: 1, hush: 1, night: 1.4,
  cue: 'Hold the phone still, or lay it down. Knock beside it, or make a sound, and the web answers.', rows: [ ... ] }
```

| Field | Value | Behind it | Invented? |
|---|---|---|---|
| `fov` | 340 | Log 107 (lens axes spread evenly in a halo in orb weavers, which likely maximizes total field), 170 ("complete visual surveillance" in two hackled orb weavers). No total field in degrees was found. | the number is invented |
| `cpd` | .17 | Log 71 (3 degrees between receptors in a funnel weaver's side eyes). Log 70 and 94: the mirror region forms no focused image, so the true picture is softer still in parts. | |
| `pupil` | 'o' | Log 70 (a single-chambered camera eye). | invented |
| `M` | `SIDE_GREEN` | Log 168 (one green class in the front side eyes of *Argiope*). | the matrix is invented |
| `sat` | .35 | Log 165 to 168 (three classes only in the two front middle eyes; one in the front side eyes). | invented |
| `gain` | 1.3 | Log 86, 93 (most spiders are active at night). | invented |
| `night` **new** | from local sunset to sunrise by the phone's clock, 1.4 times the gain and 1.5 times the trail length | Log 256, 267, 268 | the sizes and the clock rule are invented |
| `gate` | .6 | Log 34, 48, 229; Log 134 | invented |
| `persist` | .15 | Log 206: 1/8.6 to 1/4.3 s is 0.12 to 0.23 s. Borrowed from a wandering spider. | borrowed |
| `salience`, `glow`, `glowC` | 1, .5, grey | Log 134 | strength and colour invented |
| `ripple`, `senses` | 1; knock, motion, microphone from 100 Hz to 10 kHz | Log 43 to 47 (direction from amplitude across the legs), 130 (100 Hz to 10 kHz), 40 and 42 (slow sway ignored, matching the engine's knock threshold) | the mapping is invented |
| `web` **new** | 'orb', with 'tangle', 'sheet' and 'funnel' by family | Log 43 to 46 (orb), 231 to 236 (tangle and sheet) | the drawing is invented |
| `pluck` **new** | 1 | Log 49, 195, 252 | invented |
| `hush` **new** | 1 | Log 240, 241 | invented |
| `dof`, `fovea`, `topoA`, `topoS`, `fall`, `uvBlue` | leave out | no source | |

#### New effects

1. **A web that carries direction.** The person sees a faint web over the picture, centred on the screen as the spider sits at the hub: radial threads and a spiral for orb weavers, a loose tangle for cobweb and cellar spiders, a flat mesh for sheet and funnel weavers. A knock on the phone, or on the table it lies on, sends a pulse along the threads from the side of the knock toward the centre; the threads on that side light up ten to thirty times more than those across from it (Log 44), and the pulse fades as it travels, fastest for side-to-side shaking (Log 46). The phone's accelerometer stands in for the leg tips, through `devicemotion`; on iPhones the page must call `DeviceMotionEvent.requestPermission()` from a tap and wait for "granted" (MDN). Following the 5 to 30 Hz rhythm of the shaking itself needs readings at 60 a second or more, and `DeviceMotionEvent.interval` reports what the hardware gives (MDN), so the rate should be read on each phone and the pulse drawn as a single event where it is too low. Difficulty: low to moderate; the engine branch already starts a ripple from the side of a knock, and the web is a procedural pattern in the shader. What makes it beautiful: the web catches each knock the way dew catches light, and its shape follows the family photographed.
2. **Pluck.** A tap on the screen sends a ring out from the hub, and moving things flash brighter as it passes, the way an orb weaver tests its web (Log 49, 195, 252). Input: touch. Difficulty: low, a ring and a read of the movement map. Beautiful because the person learns to ask the scene a question and see it answer.
3. **A web that hears.** With the microphone on, sound onsets between 100 Hz and 10 kHz make the whole web shimmer (Log 130, 131). One microphone gives no direction, so the shimmer is even across the web. The engine branch already filters the microphone by band and asks consent in plain words first. Difficulty: low.
4. **Hush.** In a loud place (a high running level on the microphone), ripples and shimmer grow fainter and arrive late, by up to a few seconds, as traffic noise delayed Banded Garden Spiders from 0.29 s to 4.89 s on average (Log 240, 241). Difficulty: low. Beautiful because the street visibly dulls the spider's world and quiet brings it back.
5. **Night eyes.** From local sunset to sunrise, by the phone's clock, the picture lifts dim light further and its trails lengthen, as an orb weaver's eyes grow more sensitive and slower at night (Log 256, 267, 268). Difficulty: trivial. The sizes of both changes are invented.
6. **Later: the body as a sensor.** A garden spider reads which way its web rocks from the pitch and roll of its own body, and pitch carries about 15 times the signal of roll in an *Argiope* web (Log 196). The phone's gyroscope could stand in, brightening threads on the side the phone tips toward. Difficulty: moderate, because a hand tips a phone all the time; it fits a phone lying on a soft surface best.

### 2.2 `hunter`: wolf, nursery web and fishing, huntsman and wandering spiders

#### Rows

`['m', 'Eyes all round', 'A wolf spider’s eight eyes look in every direction at once, and its four large rear eyes take in the whole circle around it. The camera holds a slice of that, so this view squeezes a wide sweep into the screen.']`
Log 149 (*Lycosa leuckartii*, 360 degrees), 87 (Land 1985: rear middle fields take the whole front, rear side fields take over from 60 to 80 degrees), 22 (*Cupiennius*), 224 and 254 (*Heteropoda venatoria*).

`['m', 'Sharpness', 'The sharpest eyes of a large wolf spider, the big pair facing forward, have light-sensing cells two-thirds of a degree apart, which gives about an eightieth of your sharpness. Other wolf spiders and their relatives measured so far see more coarsely, and this view uses a middle value.']`
Log 145 (0.67 degrees; 1 / (2 × 0.67) = 0.75 cycles per degree), 146 to 148, 72 (0.35), 98 (0.28), 19 and 140 (*Cupiennius*, 0.37 to 0.5).

`['m', 'Dim light', 'A mirror layer behind the rear eyes sends light back through the light-sensing cells, and it shines green in a flashlight beam at night. A wandering spider still sees by moonlight. This view lifts dim light, more as the scene grows darker.']`
Log 153 (Benson and Suter 2013, eyeshine in wolf and fishing spiders), 20 and 68 (grate-shaped mirror), 261, 138 (*Cupiennius*, below 0.01 lux), 150 and 21 (F-numbers 0.58 to 0.74).

`['g', 'Movement', 'The side and rear eyes catch movement, and the system that detects it ignores colour, so a moving coloured stripe looks like a grey one to a wandering spider. In this view, things that move glow grey.']`
Log 142 (only the side and rear eyes detect moving targets), 141 (Orlando and Schmid 2011), 29.

`['g', 'Pace', 'A wandering spider’s eyes stop following a flickering light at 4.3 to 8.6 flashes a second, a seventh of your rate or less. Movement in this view leaves trails.']`
Log 206 (Fenk and Schmid 2011).

`['m', 'Colour', 'A wolf spider’s side and rear eyes carry a single kind of colour-sensing cell, most sensitive to green, and its two small front middle eyes add ultraviolet. Colour is faint in this view.']`
Log 151 (505 to 510 nm), 152 (360 to 370 nm), 207 (three opsins in *Pardosa astrigera*).

`['g', 'Moving air', 'Hunting spiders carry hundreds of fine hairs on their legs that swing in the slightest breath of air. A wandering spider feels a fly humming more than half a metre away, and it leaps at the swirling air the fly leaves behind it. With the microphone on, a nearby buzz sends ripples through this view.']`
Log 30 (936 hairs, tuned between 40 and 600 Hz), 32 and 176 (felt to 55 to 60 cm), 121, 122 (the wake triggers the jump).

`['g', 'The ground', 'Slit-shaped sense organs near the leg joints feel the ground tremble. A wandering spider turns toward the leg that felt a tremor first, and a difference of 4 thousandths of a second between legs is enough to steer it. A knock on the phone, or on the table it lies on, sends a ripple in from that side.']`
Log 36, 124, 125 (weak vibration releases attack, strong vibration escape).

`['m', 'Fishing spiders', 'Fishing spiders feel ripples on the water through their legs. A Six-spotted Fishing Spider answers only water waves from prey more than 10 centimetres away, and a sight alone set off an attack in only 14 trials out of 100. For fishing spiders, this view spreads its ripples across the bottom of the picture like rings on water.']`
Log 243, 244, 245, 246, 247 (Bleckmann and Barth 1984, *Dolomedes triton*: best at 40 to 70 Hz, aim within about 9 degrees).

`['m', 'Huntsman spiders', 'Six of a Pantropical Huntsman Spider’s eight eyes together cover nearly all the space around it, and one pair of them looks up at the sky. In tests it ran toward dark bars only when they were at least 4 to 8 degrees wide.']`
Log 224, 253, 254, 226 (Lorenz 2012).

`['x', 'Sky compass', 'Wolf spiders read the pattern of polarized light in the sky with their two front middle eyes, and use it to find the way home. This view leaves that sense out.']`
Log 154 (Dacke and colleagues 2001), 156 (*Lycosa tarantula*), 215.

#### The picture

```
hunter: { chip: 'Wolf, fishing or huntsman spider', who: 'a hunting spider', fov: 360, cpd: .5, pupil: 'o', M: SIDE_GREEN, sat: .2, gain: 2.2, persist: .15,
  salience: 1, glow: .8, glowC: [.85, .85, .85], ripple: 1, senses: { motion: true, jolt: true, mic: [40, 600] },
  dark: { gain: 3, cpd: .3, persist: .3 },
  zones: [{ id: 'front', shape: 'ellipse', at: [.5, .5], size: [.28, .22], soft: .1, gaze: 1 }],
  gaze: { zone: 'front', trigger: 'jolt', jump: 80, reach: 15, dwell: [500, 1200] },
  byGenus: { Dolomedes: { water: 1, senses: { jolt: true, mic: [40, 70] } } },
  cue: 'Lay the phone down. Knock on the table beside it, and watch the tremor arrive.', rows: [ ... ] }
```

| Field | Value | Behind it | Invented? |
|---|---|---|---|
| `fov` | 360 | Log 149, 87, 22, 254 | |
| `cpd` | .5 | Log 145 to 148, 72, 98, 19, 140 (measured range 0.28 to 0.75) | the choice within the range is invented |
| `pupil` | 'o' | Log 70 | invented |
| `M` | `SIDE_GREEN` | Log 151, 137 (*Cupiennius* 520 to 540 nm), 159 (*Leucorchestris* 525 to 540 nm) | the matrix is invented |
| `sat` | .2 | Log 141, 151 | invented |
| `gain` | 2.2 | Log 138, 150, 20, 153 | the size is invented |
| `dark` **new** | as the scene's mean brightness falls, gain rises to 3, sharpness falls to .3 and trails lengthen to .3 s | Log 138 (principal eyes up to 0.81 log units more sensitive at night), 205 (more contrast needed below about 16 cd/m²), 160 (*Leucorchestris* pools in space and time under starlight to recover coarse shapes) | the curve is invented |
| `persist` | .15 | Log 206 | |
| `salience`, `glow`, `glowC` | 1, .8, grey | Log 142, 141 | strength invented |
| `zones`, `gaze` | a small window, moved 4 to 15 degrees toward the side of a knock | Log 144 (Kaps and Schmid 1996: a touch or air puff on one side swings that side's principal retina 4 to 15 degrees), 219 | trigger and size invented |
| `ripple`, `senses` | 1; knock, motion, microphone from 40 to 600 Hz | Log 30 (hairs tuned 40 to 600 Hz), 124 | the mapping is invented |
| `byGenus.Dolomedes` | water rings; microphone 40 to 70 Hz | Log 245, 246 | the drawing is invented |

#### New effects

1. **Dark adaptation.** As the camera's picture darkens, the view lifts it more, and in very dim light it grows smoother and slower, keeping coarse shapes visible where the person's own view goes black (Log 138, 160, 205). Input: the camera's own mean brightness, with no new permission. Difficulty: low to moderate. Beautiful because dusk becomes the spider's daylight.
2. **Prey or threat.** A gentle knock draws a ripple from its side and swings the small window toward it; a hard knock makes the whole picture flinch back and dim for half a second (Log 125). Input: accelerometer, with the iPhone permission tap. Difficulty: low, a second threshold on the engine branch's knock.
3. **Hairs in the air.** With the microphone on, sound between 40 and 600 Hz near the phone makes fine ripples, and blowing gently on the phone does too (Log 30, 121). Difficulty: low. A phone microphone measures air pressure, while the spider's hairs follow the movement of the air itself, so the ripples stand in for what the hairs feel.
4. **Rings on water** for *Dolomedes* (the White-banded and Six-spotted Fishing Spiders hold 229 Alachua records): ripples drawn as widening ellipses on the lower half of the picture, as on a pond seen at a low angle, from knocks and from sound between 40 and 70 Hz (Log 243 to 246). Difficulty: low to moderate. Phone microphones may record 40 Hz weakly, which needs a check on real phones.

### 2.3 `crabspider`: crab, lynx and running crab spiders

#### Rows

`['m', 'Eyes', 'A crab spider’s eight small eyes together cover nearly all the space above and around it. Four of them look straight ahead, so anything that lands in front is seen by several eyes at once.']`
Log 54 to 59 (Insausti and colleagues 2012, *Misumena vatia*), 119, 120 (*Xysticus cristatus*), 187 (small eyes for the body).

`['m', 'Fast side eyes', 'The side and rear eyes of a crab spider follow a flickering light up to 20 to 30 flashes a second, and the two front middle eyes only about 10. This view draws the surround smoothly and lets a faint second picture straight ahead step along about ten times a second.']`
Log 110 to 115 (Fischer and colleagues 2026).

`['m', 'Sharpness', 'A crab spider’s light-sensing cells sit 2 to 4 degrees apart, so it sees anything clearly only up close. It notices movement up to about 20 centimetres away and grabs prey that comes within a centimetre.']`
Log 73 to 76 (Land 1985, *Xysticus*: 1.8 to 4.2 degrees, which gives 0.12 to 0.28 cycles per degree), 101 (Foelix 2011, citing Homann 1934).

`['m', 'Colour', 'The Goldenrod Crab Spider has green-sensing and ultraviolet-sensing cells, and two other crab spiders measured so far have a single green-sensing kind. Colour in this view is faint and leans green.']`
Log 60, 61 (520 and 340 nm), 116, 117 (504 and 511 nm).

`['m', 'Daylight', 'A common European crab spider hunts by day in sunny, open grassland, taking bees and hoverflies, and its front middle eyes need far more light than its other eyes. This view does not lift dim light.']`
Log 264, 118 (Fischer and colleagues 2026, *Xysticus cristatus*). A ground-dwelling relative of dark places has slower eyes (Log 265, 114, 115).

`['m', 'Eyes help the catch', 'Crab spiders with their eyes covered catch fewer flies, even though their eyes are small for their bodies.']`
Log 187 (England and colleagues 2026, *Sidymella rubrosignata*).

`['i', 'Lynx spiders', 'A Green Lynx Spider waits on a flower and leaps at insects that hover within a centimetre of it, much as a crab spider does. Nobody has measured how its eyes work, so this view assumes they work like a crab spider’s.']`
Log 269, 270 (Sánchez-Solano and colleagues 2026, *Peucetia viridans*), 266, 106, 221 to 223 (Kovoor and Muñoz-Cuevas 1997: structure only; the front side eyes may resolve best, and the rear and front side eyes, with a rudimentary mirror layer, seem suited to movement).

`['x', 'Ultraviolet', 'The Goldenrod Crab Spider also sees ultraviolet light, and the corneas of crab spiders let it through. This view leaves ultraviolet out.']`
Log 61, 189 (Hu and colleagues 2014).

#### The picture

```
crabspider: { chip: 'Crab or lynx spider', who: 'a crab spider or lynx spider', fov: 340, cpd: .2, pupil: 'o', M: SIDE_GREEN, sat: .3, persist: .04,
  salience: 1, glow: .6, glowC: [.8, 1, .7],
  zones: [{ id: 'front', shape: 'ellipse', at: [.5, .5], size: [.55, .5], soft: .15, cpd: .28, slow: { step: 10, mix: .35 } }],
  cue: 'Hold still, as a crab spider waits on a flower.', rows: [ ... ] }
```

| Field | Value | Behind it | Invented? |
|---|---|---|---|
| `fov` | 340 | Log 59 (almost the whole upper hemisphere), 119 (almost 360 degrees of fast vision, the authors' inference) | the number is invented |
| `cpd` | .2 | Log 73 to 76 | the choice within 0.12 to 0.28 is invented |
| front `zone` | an ellipse ahead at .28 cycles per degree | Log 58 (four eyes analyze the space in front), 74 and 120 (the large anterior lateral eyes face forward, 1.8 to 2.6 degrees) | the shape is invented |
| `persist` | .04 | Log 110 to 112 (20 to 30 Hz; 1/25 s) | |
| front `slow` **new** | a second picture at 35% that steps 10 times a second | Log 113, 115 (front middle eyes about 10 Hz) | the mix is invented |
| `M`, `sat` | `SIDE_GREEN`, .3 | Log 60, 116, 117 | invented |
| `gain` | leave out | Log 118, 264 | |
| `salience`, `glow` | 1, .6 | Log 119 | invented |
| `pupil` | 'o' | Log 70 | invented |
| `uvBlue` | leave out | the `x` row | |

#### New effects

1. **Two speeds in one picture.** The surround runs smooth and fast; straight ahead, a faint second picture lags and jumps ten times a second, the slow front middle eyes catching up with the fast side eyes (Log 110 to 115). Input: camera only. Difficulty: moderate; the engine keeps a ring of past frames, and the zone needs one extra read from it at a time rounded to a tenth of a second. Beautiful because a fly landing in front arrives twice, once at once and once a beat later.
2. **Near movement only.** Movement that fills a large part of the front glows, and small distant movement fades, following the 20 cm reach of a crab spider's attention (Log 101). Without depth the app judges nearness by apparent size, which is a guess. Difficulty: moderate.

### 2.4 `netcaster`: net-casting spiders

#### Rows

`['m', 'Giant eyes', 'An ogre-faced spider’s two rear middle eyes are the largest single eyes known in any arthropod, 1.4 millimetres across. Each light-sensing cell in them gathers about 2,000 times as much light as one of yours looking at the same scene.']`
Log 1, 11 (Blest and Land 1977, *Dinopis subrufus*), 2 (F-number 0.58).

`['m', 'Hunting by starlight', 'It hangs head down at night from a frame of silk, holding a small net between its front legs, and throws the net over insects that walk beneath it. With those big eyes covered, it catches few of them. Point the phone at the ground to look where it looks.']`
Log 262, 14 (no trip-line, so no vibration warns it), 259 (Stafstrom and Hebets 2016, *Deinopis spinosa*), 13, 260.

`['m', 'Sharpness', 'Those eyes trade detail for light. Their light-sensing cells sit about one and a half degrees apart, which gives under a hundredth of your sharpness.']`
Log 3, 4 (1.48 degrees, 0.34 cycles per degree), 9.

`['m', 'Dim light', 'The eyes give half their strongest response at light midway between starlight and moonlight, and the spider keeps catching prey under starlight alone. This view lifts the dark a long way, and in deep darkness the picture turns grainy.']`
Log 84 (Land 1985, from Laughlin and colleagues 1980), 213, 214 (Morehouse 2020: sensitivity like that of mid-water animals, ten times a person's), 83.

`['m', 'Hearing', 'An ogre-faced spider hears through its legs. Tones of 150 and 400 vibrations a second make it strike backward, the way it snatches flying insects it cannot see. With the microphone on, a hum makes this view whip up and back, as the spider strikes.']`
Log 135, 136 (Lesser 2021, reporting Stafstrom and colleagues 2020: brain responses peak at 150 to 200, 400 to 450 and 700 to 750 Hz; leg nerves answer 1 to 10 kHz).

`['i', 'Colour', 'Nobody has measured colour vision in net-casting spiders. This view shows the night in grey.']`
Log 13 (nocturnal), 10 (no mirror layer). The grey is the app's choice.

`['x', 'The other eyes', 'Six smaller eyes watch the rest of its surroundings, about eighteen times less sensitive than the big pair. This view shows only what the big pair sees.']`
Log 12, 5 to 7, 263.

#### The picture

```
netcaster: { chip: 'Net-casting spider', who: 'a net-casting spider', fov: 180, cpd: .34, pupil: 'o', sat: 0, gain: 1.3, persist: .2,
  zones: [{ id: 'pm', shape: 'ellipse', at: [.5, .55], size: [.85, .85], soft: .2, gain: 3.2 }],
  grain: 1, senses: { mic: [150, 750] }, strike: 1, cast: 1,
  cue: 'Point the phone at the ground, as the spider hangs head down over a path at night.', rows: [ ... ] }
```

| Field | Value | Behind it | Invented? |
|---|---|---|---|
| `fov` | 180 | Log 263 (the giant eyes give maximum sensitivity over only part of the field); the field in degrees was not found | invented |
| `cpd` | .34 | Log 4 | |
| `zones` | the giant eyes' ellipse with gain 3.2, the rest 1.3 | Log 11, 12 (18 times), 83 (S = 387 µm²), 84 | the shape and both gains are invented |
| `sat` | 0 | the `i` row | invented |
| `persist` | .2 | Log 9 and 133 (receptors 20 µm wide and up to 110 µm long); no temporal measurement | invented |
| `grain` **new** | noise that grows as the scene darkens | the `Dim light` row | invented |
| `senses`, `strike` **new** | microphone 150 to 750 Hz; on a sound onset the picture whips upward and back in about 0.3 s | Log 135, 136 | the drawing is invented |
| `cast` **new** | a tap throws a square net that spreads down over the touched spot | Log 14, 262 | invented |
| `pupil` | 'o' | Log 1 | invented |

#### New effects

1. **Starlight grain.** In dim scenes the view lifts the picture far and adds a fine, shifting grain that grows as light falls, so the ground below looks luminous and alive with noise. Input: the camera's brightness. Difficulty: low; noise is among the engine branch's planned effects.
2. **The backward strike.** With the microphone on, a hum or buzz between 150 and 750 Hz whips the picture upward and back for a moment, then it settles (Log 135, 136). Difficulty: low to moderate. Beautiful because the person hears the spider's world turn the picture over.
3. **Casting the net.** A tap throws a square net of fine lines down over the touched spot and draws it closed (Log 14, 262). Difficulty: low, an overlay.

### 2.5 `tarantula`: tarantulas, trapdoor spiders and the ground hunters

#### Rows

`['m', 'Feeling the ground', 'A tarantula finds its prey through the hairs on its legs. Club-shaped sense hairs feel the soil tremble, and fine hairs answer the slightest movement of the air. Lay the phone down, and a knock on the table beside it sends a ripple in from that side.']`
Log 178 (den Otter 1973, *Sericopelma rubronitens*: trichobothria and club-shaped sensilla detect and locate prey), 184 (club-shaped airflow hairs on the feet of all tarantulas; whether these are den Otter's club-shaped sensilla is not settled by the abstracts read).

`['m', 'Trapdoor spiders', 'A trapdoor spider catches prey as well with its eyes covered, and it catches far fewer when a rubber mat damps the trembling of the ground.']`
Log 183 (Nakamura and colleagues 2022, *Latouchia typica*).

`['m', 'Signals through the ground', 'Male tarantulas court by drumming with their palps, tapping their legs and shaking their bodies, and in one species the tremors carry at least 1.36 metres through the ground.']`
Log 180, 181 (Quirici and Costa 2005, 2007).

`['m', 'Legs as filters', 'A tarantula’s flexible legs damp the shaking of its own body, so the tremors its feet pick up come through clearer.']`
Log 198 (Miller and colleagues 2026, *Grammostola pulchra*).

`['g', 'Eyes', 'Tarantulas have eight small eyes bunched on a mound at the front of the head, and they hunt at night close to their retreats. In one tarantula that has been measured, the eyes carry a single kind of light-sensing cell, most sensitive to blue-green light near 500 nanometres. This view is coarse, dim and nearly colourless.']`
Log 105, 102, 182, 185 (Dahl and Granda 1989, *Aphonopelma chalcodes*), 66.

`['m', 'Ultraviolet', 'Purse-web and trapdoor spiders have corneas that block ultraviolet light, unlike the hunting spiders measured. This view shows no ultraviolet.']`
Log 190, 189 (Hu and colleagues 2014).

`['i', 'Sharpness', 'Nobody has measured how sharply a tarantula sees. This view draws a very coarse picture, a guess based on how small its eyes are and how little it uses them.']`
Log 183, 188, 102.

`['g', 'Ground spiders', 'Ground spiders, sac spiders, recluses and spitting spiders also hunt without a web, and their small eyes give coarse pictures. A Chilean recluse has only one kind of light-sensing cell, and some ground spiders have turned two eyes into a compass that reads the sky at dusk.']`
Log 67, 70, 104, 191 (Tapia and colleagues 2019), 155, 217.

`['x', 'Warmth', 'A tarantula has sense cells that answer a rise in temperature, probably too weakly to feel a warm animal at a distance. The picture leaves warmth out.']`
Log 179.

#### The picture

```
tarantula: { chip: 'Tarantula or ground spider', who: 'a tarantula or ground spider', fov: 300, cpd: .1, pupil: 'o', M: SIDE_GREEN, sat: .1, gain: 1.6, persist: .15,
  ripple: 1.4, senses: { motion: true, jolt: true, mic: [20, 300] }, stillJolt: 1, bristle: 1,
  cue: 'Lay the phone down and wait. Knock beside it, or blow on it gently.', rows: [ ... ] }
```

| Field | Value | Behind it | Invented? |
|---|---|---|---|
| `fov` | 300 | Log 105 (eyes on a mound; almost panoramic in *Liphistius*) | invented |
| `cpd` | .1 | no measurement | invented (`i` row) |
| `M`, `sat` | `SIDE_GREEN`, .1 | Log 185, 191 | invented |
| `uvBlue` | leave out | Log 190 | |
| `gain` | 1.6 | Log 102, 182, 66 | invented |
| `persist` | .15 | no measurement | invented |
| `ripple`, `senses` | 1.4; knock, motion, microphone from 20 to 300 Hz | Log 178, 181, 183 | the mapping is invented |
| `stillJolt` **new** | when the phone lies still, the knock threshold drops so soft taps register | Log 178 | invented |
| `bristle` **new** | fine radial streaks at the edges while the microphone hears moving air | Log 178, 184 | invented |

#### New effects

1. **Feeling the floor.** When the phone lies still, the view lowers its knock threshold so that soft taps on the table register, each arriving as a ripple from its side, and between tremors the camera picture sinks to a dark, coarse wash (Log 178, 183). Input: accelerometer. Difficulty: moderate; each phone's resting noise differs, so the threshold should be set from the first seconds of stillness. Beautiful because the table becomes a drum skin that the picture listens to.
2. **Hairs in the air.** Moving air on the microphone, including a person blowing gently at the phone, makes fine streaks bristle at the edges of the picture (Log 178). Difficulty: low.

## 3. The earlier `spider` sheet, re-checked

`main` has no `spider` entry in `EYES`, so this section re-checks the rows and numbers that `docs/views/sheets/spider.md` proposed for it.

| Earlier row or number | Verdict | Now |
|---|---|---|
| 'The web': 5 to 30 shakes a second, ten to thirty times stronger on some legs | confirmed | Landolfa and Barth 1996 read in full (Log 43, 44); the earlier sheet had the abstract |
| 'Drawn as' (`x`): only what moves is shown in place of the web | superseded | the Australian Museum page was not re-opened; the substance holds on primary sources (Log 70, 92, 229), and the web is now drawn (section 2.1) |
| 'Eyes' (`g`): eight eyes, few see well, web builders lean on the silk | confirmed, sources replaced | Log 91, 67, 70, 34, 48, 169; the museum quotes were not re-opened, and the sentence the earlier sheet quoted from Stafstrom and Hebets 2016 is not in that paper's abstract, the part read here |
| 'Sharpness' (`g`): about 2 degrees, borrowed from *Cupiennius* | corrected | the *Cupiennius* figure is confirmed (Log 15 to 19), but a web builder's own eye samples at 3 degrees (Log 71), so `cpd` falls from .5 to .17 |
| 'Pace' (`g`): 4.3 to 8.6 Hz | confirmed for *Cupiennius*, regraded | Log 206; for web builders it is borrowed, so it moves into an `i` row |
| 'Colour' (`g`): *Argiope* has ultraviolet, blue and green receptors in some eyes | confirmed and made exact | the open question about Morehouse 2020's wording is settled by the primary papers: the three classes sit in the anterior median (principal) eyes, and the anterior lateral eyes have one (Log 165 to 168); the earlier source note's "secondary eyes" reading was wrong; an ERG study of *A. argentata* found a single green type in every eye with ultraviolet responses strongest in the principal eyes (Log 271 to 274), so the blue class may be rare |
| 'Hearing through silk' (`x`): loudspeaker 3 m away, area up to 10,000 times | confirmed, upgraded | Zhou and colleagues 2022 read in full (Log 130, 131, 258); the earlier mark was `secondary`; the response was 6 of 12 spiders at 68 dB and 11 of 12 at 88 dB; the row is now `m`, because the microphone draws it |
| 'Wolf spiders' (`x`): large rear eyes with a mirror layer that shines | confirmed, superseded | Log 153, 68; now the `hunter` view |
| 'Net-casting spiders' (`x`): caught walking prey by sight; lenses 1.4 mm | confirmed, superseded | Log 259 (abstract), 1, 2; now the `netcaster` view |
| `fov` 300 (invented) | replaced | 340, still invented, now leaning on Log 107 and 170 |
| `cpd` .5 | corrected | .17 (Log 71) |
| `gate` 1 (invented) | changed | .6 (invented), since moving things now glow and the web carries the rest |
| `persist` .15 | kept | graded as borrowed (Log 206) |
| `M`, `sat` left out | changed | a faint, green-weighted picture (Log 168) |
| world records 2,927,814 and Alachua 4,660 | confirmed | read again on 13 October 2026 |

## 4. Species with their own measurements

| Species | Alachua records | View | Log lines |
|---|---:|---|---|
| Golden Silk Spider, *Trichonephila clavipes* | 702 | `spider` | 33, 34, 43 to 50, 249 to 251 (web vibration: 5 to 30 Hz, direction from amplitude, latency 0.1 s, lowest threshold 280 to 420 Hz for side-to-side shaking); no eye measurement |
| *Argiope* (Yellow Garden Spider 275, Banded Garden Spider 23) | 298 | `spider` | 165 to 168 and 267, 268 (*A. bruennichi*, *A. amoena* receptors and their night state), 271 to 274 (*A. argentata* spectra), 196 (*A. trifasciata* pitch and roll), 240, 241 (noise), 203 (smell); nothing measured in *A. aurantia* itself (Hoffmaster 1982 is on the wanted list) |
| Bridge spider, *Larinioides sclopetarius* | 0 | `spider` | 39 to 42, 130 to 132, 258 |
| Western black widow, *Latrodectus hesperus*, for Alachua's Brown Widow (108) and Southern Black Widow (27) | 135 | `spider` | 231 to 239 |
| Cellar spiders, *Pholcus phalangioides* and *P. ancoralis*, for the Tailed Cellar Spider (73) | 73 | `spider` | 229, 230, 242 |
| Hackled orb weavers, *Uloborus diversus* and *U. glomosus* | 15 | `spider` | 170, 194, 195 |
| Six-spotted Fishing Spider, *Dolomedes triton* | 76 | `hunter` | 164, 243 to 248 |
| Pantropical Huntsman Spider, *Heteropoda venatoria* | 77 | `hunter` | 224 to 227, 253 to 255 |
| *Cupiennius salei*, the model for Alachua's Florida Wandering Spider (*Ctenus captiosus*, 29) | 29 | `hunter` | 15 to 26, 30 to 32, 36 to 38, 121 to 126, 137 to 144, 176, 177, 205, 206, 228, 257 |
| Wolf spiders: *Lycosa leuckartii*, *L. tarantula*, *Schizocosa* species | 83 (Lycosidae) | `hunter` | 145 to 150, 156, 157, 51, 52, 199 to 201, 204, 208 |
| Namib huntsman, *Leucorchestris arenicola* | 0 | `hunter` | 158 to 161 |
| Goldenrod Crab Spider, *Misumena vatia* | 0 | `crabspider` | 54 to 63 |
| *Xysticus cristatus* and *Ozyptila praticola* | 0 | `crabspider` | 110 to 120, 264, 265 (and *Xysticus* sp. 73 to 76, 81) |
| Ogre-faced Spider, *Deinopis spinosa*, with *Dinopis subrufus* (now *Asianopis subrufa*) for the optics | 88 | `netcaster` | 133, 135, 136, 259, 260; 1 to 14, 262, 263 |
| Tarantulas: *Aphonopelma chalcodes*, *Sericopelma rubronitens*, *Eupalaestrus weijenberghi*, *Grammostola pulchra*; trapdoor spider *Latouchia typica* | 8 (mygalomorphs) | `tarantula` | 185, 178, 179, 180, 181, 198, 183 |
| Chilean recluse, *Loxosceles laeta* | 0 | `tarantula` | 191 |

The Green Lynx Spider (*Peucetia viridans*, 246 Alachua records, the fourth most recorded spider of this unit) has a field observation of its hunting (Log 269, 270) and no measurement of its eyes; its genus appears only in a histology abstract (Log 222).

## 5. Gaps and how to fill them

- **Orb weaver sharpness and field.** Nothing measured in degrees. Nearest: a funnel weaver's side eyes at 3 degrees (Log 71) and the structure of *Araneus* side eyes (Log 94). Inference: 0.1 to 0.2 cycles per degree, softer where the mirror region lies. To fill: Uehara and colleagues 1977 and 1978 on *Argiope amoena* eyes, and Homann 1971 (wanted).
- **Orb weaver flicker.** Nothing found. Nearest: 4.3 to 8.6 Hz in the nocturnal *Cupiennius* (Log 206) and 10 to 30 Hz in day-active crab spiders (Log 110 to 115). Inference: night-active orb weavers are probably slow like *Cupiennius*; day-active *Argiope* may be faster, and nothing measured settles it.
- **Cobweb, cellar, sheet and funnel weaver eyes.** Nothing measured beyond the mirror types (Log 66, 67) and a cellar spider's indifference to vision (Log 229).
- **Wolf spider flicker.** Nothing found. Nearest: *Cupiennius*. To fill: DeVoe 1964 (wanted).
- **Lynx spiders.** Only a histology abstract (Log 221 to 223) and one field observation of a strike (Log 269). This is the largest gap in Alachua, with 270 records. Inference: crab spider values with the lynx spiders' front cluster; to fill: Kovoor and Muñoz-Cuevas 1997 in full (wanted).
- **Running crab spiders.** No mirror layer (Log 69, 210); nothing else.
- **Tarantula sharpness, field and flicker.** Nothing found. Inference from eye size (Log 188) and behaviour (Log 183). To fill: Homann 1971; Henton and Crawford 1966 on polarization (wanted).
- **Huntsman flicker and colour.** Resolution at least 4 to 8 degrees in *Heteropoda* (Log 226); spectral peaks in *Leucorchestris* (Log 159).
- **Fishing spider eyes.** F-number 0.9 (Log 162) and eyeshine (Log 153); no sharpness measured.
- **Net-casting field in degrees and flicker.** Not found in Blest and Land 1977 as read. To fill: Laughlin and colleagues 1980; Stafstrom and colleagues 2020 (wanted).
- **Vibration in crab and lynx spiders.** Nothing found in this session.
- **How to infer for an unmeasured family.** Eye arrangement follows hunting ecology (Log 106, 107), and eye size follows visual hunting, web building and time of activity (Log 188). An unmeasured family should take the values of the nearest measured family with the same hunting mode and time of activity, and the row is graded `i`.
- **Unfinished in this session.** The chapters of Barth 1985 after page 73 and all of Foelix 2025 could not be read (section 7); Stafstrom and colleagues 2020 and DeVoe 1962 and 1964 failed to open.

## 6. Closed sources wanted

The same list as `docs/views/wanted/spider.jsonl`, most useful first. Priority 1 would change a picture, 2 would confirm or correct a row, 3 is background. Every DOI comes from a page opened in this session: the collection's index, the reference list of Pande and colleagues 2026, the contents of Barth 1985, or the publisher's page.

1. Priority 1. Kovoor J, Muñoz-Cuevas A 1997. Comparative structure of the visual system of lynx spiders (Oxyopidae) and its relation to habitat and behaviour. Zoologischer Anzeiger 235(3-4): 133-145. https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/7979075. Would give lynx spider eye fields and resolution, now borrowed from crab spiders, for the Green Lynx Spider, the fourth most recorded spider of this unit in Alachua; no DOI was found. Views: `crabspider`.
2. Priority 1. DeVoe RD 1964. Linear electrical flicker responses from the eye of the wolf spider. Documenta Ophthalmologica. doi 10.1007/bf00160569. Would give a wolf spider's own flicker limit, which the hunter view now borrows from Cupiennius. Views: `hunter`.
3. Priority 1. Barth FG 1985. Neuroethology of the spider vibration sense. In: Barth FG (ed) Neurobiology of Arachnids. Springer, Berlin, 1985, chapter XI, pp. 203-229 (DOI is the book's). doi 10.1007/978-3-642-70348-5. Would set vibration thresholds and frequency ranges for web builders against hunters, behind every ripple effect; the owner's 18 MB copy came through only to p. 73, so a copy split into chapters would do. Views: `spider`, `hunter`, `tarantula`.
4. Priority 1. Uehara A, Toh Y, Tateda H 1977. Fine structure of the eyes of orb-weavers, Argiope amoena L. Koch (Araneae: Argiopidae). Cell and Tissue Research. doi 10.1007/bf00222056. Would give receptor spacing in an orb weaver's own principal eyes, replacing the funnel weaver figure the web view borrows. Views: `spider`.
5. Priority 1. Uehara A, Toh Y, Tateda H 1978. Fine structure of the eyes of orb-weavers, Argiope amoena L. Koch (Aranea: Argiopidae). 2. The anterolateral, posterolateral and posterommedial eyes. Cell and Tissue Research. doi 10.1007/bf00224933. Would give receptor spacing and mirror layout in an orb weaver's side eyes, which fill most of the web view's field. Views: `spider`.
6. Priority 1. Homann H 1971. Die Augen der Araneae. Zeitschrift für Morphologie der Tiere 69: 201-272. doi 10.1007/BF00277623. Would give eye structure and fields across families, filling the web builders', tarantulas' and lynx spiders' fields and sharpness. Views: `spider`, `tarantula`, `crabspider`, `hunter`.
7. Priority 1. Stafstrom JA, Menda G, Nitzany EI, Hebets EA, Hoy RR 2020. Ogre-Faced, Net-Casting Spiders Use Auditory Cues to Detect Airborne Prey. Current Biology. doi 10.1016/j.cub.2020.09.048. The primary paper behind the net-casting spider's hearing, now read through a summary; it would set the microphone band and the distance for the strike effect. Views: `netcaster`.
8. Priority 1. Foelix R 2025. Spider Biology, chapter 4: Neurobiology, pp. 87-136. Springer Cham. doi 10.1007/978-3-031-96011-6. The newest synthesis of spider eyes and sense organs; the owner's copy returned no text to the reading tool. Views: `spider`, `hunter`, `crabspider`, `netcaster`, `tarantula`.
9. Priority 2. Reißland A, Görner P 1985. Trichobothria. In: Barth FG (ed) Neurobiology of Arachnids. Springer, Berlin, 1985, chapter VIII, pp. 138-161 (DOI is the book's). doi 10.1007/978-3-642-70348-5. Would give airflow-hair numbers and thresholds across families, confirming or correcting the Moving air rows. Views: `hunter`, `tarantula`, `spider`.
10. Priority 2. Barth FG 1985. Slit sensilla and the measurement of cuticular strains. In: Barth FG (ed) Neurobiology of Arachnids. Springer, Berlin, 1985, chapter IX, pp. 162-188 (DOI is the book's). doi 10.1007/978-3-642-70348-5. Would confirm the slit sense organ figures behind the ground rows. Views: `hunter`, `tarantula`, `spider`.
11. Priority 2. Yamashita S 1985. Photoreceptor cells in the spider eye: spectral sensitivity and efferent control. In: Barth FG (ed) Neurobiology of Arachnids. Springer, Berlin, 1985, chapter VI, pp. 103-117 (DOI is the book's). doi 10.1007/978-3-642-70348-5. Would give the size of the nightly rise in orb weaver eye sensitivity, which the web view's night lift now invents. Views: `spider`, `hunter`.
12. Priority 2. Görner P, Claas B 1985. Homing behavior and orientation in the funnel-web spider, Agelena labyrinthica Clerck. In: Barth FG (ed) Neurobiology of Arachnids. Springer, Berlin, 1985, chapter XIV, pp. 275-297 (DOI is the book's). doi 10.1007/978-3-642-70348-5. Would show what a funnel weaver uses its eyes and the sky for, and whether the web view needs a sky-compass row. Views: `spider`.
13. Priority 2. Laughlin SB, Blest AD, Stowe S 1980. The sensitivity of receptors in the posterior median eye of the nocturnal spider, Dinopis. Journal of Comparative Physiology A. doi 10.1007/bf00611878. The primary measurement behind the half-maximal response between starlight and moonlight, now read through Land 1985. Views: `netcaster`.
14. Priority 2. Hoffmaster DK 1982. Responses of the spider Argiope aurantia to low frequency phasic and continuous vibrations. Animal Behaviour. doi 10.1016/s0003-3472(82)80246-7. Would give the Yellow Garden Spider's own low-frequency vibration responses (275 Alachua records). Views: `spider`.
15. Priority 2. Crawford JD 1984. Orientation in a vertical plane: The use of light cues by an orb-weaving spider, Araneus diadematus clerk. Animal Behaviour. doi 10.1016/s0003-3472(84)80334-6. Would show what an orb weaver uses its eyes for in the web, confirming or correcting the Eyes row. Views: `spider`.
16. Priority 2. Bleckmann H, Barth FG 1984. Sensory ecology of a semi-aquatic spider (Dolomedes triton). Behavioral Ecology and Sociobiology 14: 303-312. doi 10.1007/BF00299502. The full figures behind the fishing spider row, read so far only in abstract fragments. Views: `hunter`.
17. Priority 2. Klärner D, Barth FG 1982. Vibratory signals and prey capture in orb-weaving spiders (Zygiella x-notata, Nephila clavipes; Araneidae). Journal of Comparative Physiology 148: 445-455. doi 10.1007/BF00619783. The full threshold curves for the Golden Silk Spider, read so far only in abstract fragments. Views: `spider`.
18. Priority 2. Henton WW, Crawford FT 1966. The discrimination of polarized light by the tarantula. Journal of Comparative Physiology A (as the collection lists it). doi 10.1007/bf00343655. Would show whether tarantulas read polarized light, which would add an x row to the tarantula view. Views: `tarantula`.
19. Priority 2. Opell BD, Cushing PE 1986. Visual fields of orb web and single line web spiders of the family Uloboridae (Arachnida, Araneida). Zoomorphology 106: 199-204. doi 10.1007/BF00312040. Would give measured fields for hackled orb weavers, including the genus of Alachua's Featherlegged Orbweaver, behind the web view's field. Views: `spider`.
20. Priority 2. Mortimer B, Soler A, Wilkins L, Vollrath F 2019. Decoding the locational information in the orb web vibrations of Araneus diadematus and Zygiella x-notata. Journal of the Royal Society Interface. doi 10.1098/rsif.2019.0201. Would confirm or correct how direction is carried across the legs in an orb web, behind the web overlay. Views: `spider`.
21. Priority 2. DeVoe RD 1962. Linear Superposition of Retinal Action Potentials to Predict Electrical Flicker Responses from the Eye of the Wolf Spider, Lycosa baltimoriana (Keyserling). The Journal of General Physiology. doi 10.1085/jgp.46.1.75. May give the flicker range a wolf spider eye follows; the page failed to open in this session. Views: `hunter`.
22. Priority 3. Blest AD 1985. The fine structure of spider photoreceptors in relation to function. In: Barth FG (ed) Neurobiology of Arachnids. Springer, Berlin, 1985, chapter V, pp. 79-102 (DOI is the book's). doi 10.1007/978-3-642-70348-5. Background on receptor membrane turnover by day and night across families. Views: `hunter`, `netcaster`, `spider`.
23. Priority 3. Winsor AM, Morehouse NI, Jakob EM 2023. Distributed Vision in Spiders. In: Distributed Vision (Springer Series in Vision Research), pp. 267-318. doi 10.1007/978-3-031-23216-9_10. A recent review of how spiders combine their eyes, as background for every view. Views: `spider`, `hunter`, `crabspider`, `netcaster`, `tarantula`.
24. Priority 3. Schröer W-D 1974. Zum mechanismus der analyse polarisierten lichtes bei Agelena gracilens C. L. Koch (Araneae, Agelenidae). Zeitschrift für Morphologie der Tiere. doi 10.1007/bf00394375. Background on polarization in funnel weavers' principal eyes. Views: `spider`.
25. Priority 3. Robinson MH, Robinson B 1971. The Predatory Behavior of the Ogre-Faced Spider Dinopis longipes F. Cambridge (Araneae: Dinopidae). American Midland Naturalist 85: 85-96. doi 10.2307/2423914. Background on how net-casting spiders hunt, for the net-casting effect. Views: `netcaster`.
26. Priority 3. Dornfeldt K 1975. [Role of the principal and accessory eyes in the photomenotactic orientation of the funnel spider Agelena labyrinthica (CL.)]. Zeitschrift für Tierpsychologie. doi 10.1111/j.1439-0310.1975.tb01996.x. Background on what each eye pair of a funnel weaver does. Views: `spider`.

## 7. Sources

Records and names, `opened`: the GBIF occurrence search (family facet for orderKey 1496 in dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7, read 13 October 2026, https://api.gbif.org/v1/occurrence/search?datasetKey=50c9509d-22c7-4a22-a47d-8c48425ef4a7&orderKey=1496&facet=familyKey&limit=0&facetLimit=60), GBIF species pages for the family keys (https://api.gbif.org/v1/species/<key>), and `docs/views/no-view-us-fl-alachua.csv`.

What came through of the owner's books: Barth (ed.) 1985, Neurobiology of Arachnids (Springer, doi 10.1007/978-3-642-70348-5), front matter, contents, chapters I to III and chapter IV (Land) from p. 53 to about p. 73, after which the reading tool returned nothing and the 18 MB file was too large to download; Land and Nilsson 2012, Animal Eyes, pp. 1 to about 65 (chapters 1 to 3); Foelix 2011, Biology of Spiders (the owner's preview copy), pp. 1 to 34; Foelix 2025, Spider Biology (Springer Cham, doi 10.1007/978-3-031-96011-6, details from the publisher's page), nothing, because the reading tool returned no text and the file was too large to download.

Every source behind a log line, one line each, with the log lines it supports:

- Barth FG, Wastl U, Humphrey JAC, Devarakonda R 1993. Dynamics of arthropod filiform hairs. II. Mechanical properties of spider trichobothria (Cupiennius salei Keys.). Philosophical Transactions of the Royal Society of London B 340: 445-461. https://doi.org/10.1098/rstb.1993.0084. `opened` (owner's library copy). Log 30 to 35.
- Barth FG, Nakagawa T, Eguchi E 1993. Vision in the ctenid spider Cupiennius salei: spectral range and absolute sensitivity. Journal of Experimental Biology 181: 63-79. https://doi.org/10.1242/jeb.181.1.63. `opened` (abstract). Log 137 to 138.
- Barth FG, Höller A 1999. Dynamics of arthropod filiform hairs. V. The response of spider trichobothria to natural stimuli. Philosophical Transactions of the Royal Society B. https://doi.org/10.1098/rstb.1999.0370. `opened` (abstract). Log 176.
- Barth FG 2020. A spider in motion: facets of sensory guidance. Journal of Comparative Physiology A. https://doi.org/10.1007/s00359-020-01449-z. `opened` (full text). Log 121 to 127.
- Benson KE, Suter RB 2013. Reflections on the tapetum lucidum and eyeshine in lycosoid spiders. Journal of Arachnology. https://doi.org/10.1636/B12-35.1. `opened` (abstract). Log 153.
- Bleckmann H, Barth FG 1984. Sensory ecology of a semi-aquatic spider (Dolomedes triton). Behavioral Ecology and Sociobiology 14: 303-312. https://doi.org/10.1007/BF00299502. `opened` (abstract on the publisher's page, quoted in fragments). Log 243 to 248.
- Blest AD, Land MF 1977. The physiological optics of Dinopis subrufus L. Koch: a fish-lens in a spider. Proceedings of the Royal Society of London B 196: 197-222. https://doi.org/10.1098/rspb.1977.0037. `opened` (owner's library copy). Log 1 to 14, 262 to 263.
- Blest AD, Day WA 1978. The rhabdomere organization of some nocturnal pisaurid spiders in light and darkness. Philosophical Transactions of the Royal Society of London B. https://doi.org/10.1098/rstb.1978.0016. `opened` (abstract). Log 163.
- Campione E, Schmid A 2014. Brightness discrimination in the day- and night-adapted hunting spider Cupiennius salei. Journal of Experimental Biology. https://doi.org/10.1242/jeb.103366. `opened` (abstract). Log 205.
- Choi N, Miller P, Hebets EA 2024. Vibroscape analysis reveals acoustic niche overlap and plastic alteration of vibratory courtship signals in ground-dwelling wolf spiders. Communications Biology. https://doi.org/10.1038/s42003-023-05700-6. `opened` (abstract). Log 208.
- Chong KL, Grahn A, Perl CD, Sumner-Rooney L 2024. Allometry and ecology shape eye size evolution in spiders. Current Biology 34: 3178-3188. https://doi.org/10.1016/j.cub.2024.06.020. `opened` (abstract). Log 188.
- Chuang A 2011. Size and motherhood of the spider Pholcus ancoralis (Araneae: Pholcidae) affects whirling and other defensive behaviors. eScholarship (California Digital Library), student research paper. https://doi.org/10.60950/bgtl.2011.4.chuang.a. `opened` (abstract). Log 242.
- Clemente CJ, McMaster KA, Fox L, Meldrum L, Main BY, Stewart T 2005. Visual acuity of the sheet-web building spider Badumna insignis (Araneae, Desidae). Journal of Arachnology 33(3): 726-734. https://doi.org/10.1636/S04-35.1. `opened` (abstract). Log 169.
- Clemente CJ, McMaster KA, Fox E, Meldrum L, Stewart T, Main BY 2010. The visual system of the Australian wolf spider Lycosa leuckartii (Araneae: Lycosidae): visual acuity and the functional role of the eyes. Journal of Arachnology 38: 398-406. https://doi.org/10.1636/B09-96.1. `opened` (abstract). Log 145 to 150.
- Dacke M, Doan TA, O'Carroll DC 2001. Polarized light detection in spiders. Journal of Experimental Biology 204(14). https://doi.org/10.1242/jeb.204.14.2481. `opened` (abstract). Log 154 to 155.
- Dahl RD, Granda AM 1989. Spectral sensitivities of photoreceptors in the ocelli of the tarantula Aphonopelma chalcodes (Araneae, Theraphosidae). Journal of Arachnology 17(2): 195-205. https://www.biodiversitylibrary.org/part/226315. `opened` (abstract). Log 185.
- De P, Blackledge TA 2026. Experimental exposure to anthropogenic noise disrupts early-stage prey localization in the orb-weaving spider Argiope trifasciata. Urban Ecosystems 29: 217. https://doi.org/10.1007/s11252-026-02076-3. `opened` (full text). Log 240 to 241.
- DeVoe RD, Small RJW, Zvargulis JE 1969. Spectral sensitivities of wolf spider eyes. Journal of General Physiology 54(1). https://doi.org/10.1085/jgp.54.1.1. `opened` (abstract). Log 151.
- DeVoe RD 1972. Dual sensitivities of cells in wolf spider eyes at ultraviolet and visible wavelengths of light. Journal of General Physiology 59(3). https://doi.org/10.1085/jgp.59.3.247. `opened` (abstract). Log 152.
- England SJ, Rose L, Penna-Gonçalves V, Herberstein ME, Sumner-Rooney L 2026. Crab spider vision improves their prey capture despite low visual system investment. Royal Society Open Science. https://doi.org/10.1098/rsos.260045. `opened` (abstract). Log 187.
- Fenk LM, Schmid A 2010. The orientation-dependent visual spatial cut-off frequency in a spider. Journal of Experimental Biology. https://doi.org/10.1242/jeb.041939. `opened` (abstract). Log 140.
- Fenk LM, Schmid A 2011. Flicker-induced eye movements and the behavioural temporal cut-off frequency in a nocturnal spider. Journal of Experimental Biology 214(21): 3658-3663. https://doi.org/10.1242/jeb.060855. `opened` (abstract). Log 206.
- Finck A 1972. Vibration sensitivity in an orb-weaver. American Zoologist 12(3): 539. https://doi.org/10.1093/icb/12.3.539. `opened` (abstract). Log 172.
- Finck A 1981. The lyriform organ of the orb-weaving spider Araneus sericatus: vibration sensitivity is altered by bending the leg. Journal of the Acoustical Society of America. https://doi.org/10.1121/1.386678. `opened` (abstract). Log 173.
- Fischer FL, Scharff N, Garm AL 2026. Photoreceptor physiology of two species of crab spiders (Araneae: Thomisidae). Journal of Comparative Physiology A. https://doi.org/10.1007/s00359-026-01802-8. Read at https://pmc.ncbi.nlm.nih.gov/articles/PMC13395977/. `opened` (full text). Log 110 to 120, 264 to 265.
- Foelix RF 2011. Biology of Spiders, 3rd edition. Oxford University Press, New York (ISBN 978-0-19-973482-5). https://openlibrary.org/isbn/9780199734825. `opened` (book, read in part as stated above). Log 99 to 105.
- Foley S, Saranathan V, Piel WH 2020. The evolution of coloration and opsins in tarantulas (preprint; published in Proceedings of the Royal Society B, doi 10.1098/rspb.2020.1688). bioRxiv. https://doi.org/10.1101/2020.04.25.061366. `opened` (full text). Log 128 to 129.
- French AS, Torkkeli PH, Seyfarth E-A 2002. From stress and strain to spikes: mechanotransduction in spider slit sensilla. Journal of Comparative Physiology A 188: 739-752. https://doi.org/10.1007/s00359-002-0363-1. `opened` (owner's library copy). Log 36 to 38.
- Gordon SD, Uetz GW 2012. Environmental interference: impact of acoustic noise on seismic communication and mating success. Behavioral Ecology. https://doi.org/10.1093/beheco/ars016. `opened` (abstract). Log 204.
- Guadanucci JPL 2012. Trichobothrial morphology of Theraphosidae and Barychelidae spiders (Araneae, Mygalomorphae). Zootaxa 3439. https://doi.org/10.11646/zootaxa.3439.1.1. `opened` (abstract). Log 184.
- Han SI, Blackledge TA 2024. Directional web strikes are performed by ray spiders in response to airborne prey vibrations. Journal of Experimental Biology. https://doi.org/10.1242/jeb.249237. `opened` (abstract). Log 175.
- Hebets EA 2005. Attention-altering signal interactions in the multimodal courtship display of the wolf spider Schizocosa uetzi. Behavioral Ecology 16(1): 75-82. https://doi.org/10.1093/beheco/arh133. `opened` (owner's library copy). Log 51 to 53.
- Heiling AM, Cheng K, Chittka L, Göth A, Herberstein ME 2005. The role of UV in crab spider signals: effects on perception by prey and predators. Journal of Experimental Biology. https://doi.org/10.1242/jeb.01861. `opened` (abstract). Log 186.
- Hu Z, Xu X, Chen Z, Li H, Wang X, Wu L, Liu F, Chen J, Li D 2014. The spectral transmission of non-salticid spider corneas. Journal of Experimental Biology. https://doi.org/10.1242/jeb.099069. `opened` (abstract). Log 189 to 190.
- Hung H-Y, Corver A, Gordus A 2026. Dynamic vibration-driven feedback shapes predator-prey interactions in an orb-weaving spider. PLoS Computational Biology. https://doi.org/10.1371/journal.pcbi.1014802. `opened` (full text). Log 194 to 195.
- Insausti TC, Defrize J, Lazzari CR, Casas J 2012. Visual fields and eye morphology support color vision in a color-changing crab-spider. Arthropod Structure & Development 41: 155-163. https://doi.org/10.1016/j.asd.2011.11.003. `opened` (owner's library copy). Log 54 to 65.
- Jackson RR, Brassington RJ 1987. The biology of Pholcus phalangioides (Araneae, Pholcidae): predatory versatility, araneophagy and aggressive mimicry. Journal of Zoology. https://doi.org/10.1111/j.1469-7998.1987.tb01531.x. `opened` (abstract). Log 229 to 230.
- Kaps F, Schmid A 1996. Mechanism and possible behavioural relevance of retinal movements in the ctenid spider Cupiennius salei. Journal of Experimental Biology 199: 2451-2458. https://doi.org/10.1242/jeb.199.11.2451. `opened` (abstract). Log 144.
- Klopsch C, Kuhlmann HC, Barth FG 2012. Airflow elicits a spider's jump towards airborne prey. I. Airflow around a flying blowfly. Journal of the Royal Society Interface. https://doi.org/10.1098/rsif.2012.0186. `opened` (abstract). Log 177.
- Klärner D, Barth FG 1982. Vibratory signals and prey capture in orb-weaving spiders (Zygiella x-notata, Nephila clavipes; Araneidae). Journal of Comparative Physiology 148: 445-455. https://doi.org/10.1007/BF00619783. `opened` (abstract on the publisher's page, quoted in fragments). Log 249 to 252.
- Kovoor J, Muñoz-Cuevas A 1997. Comparative structure of the visual system of lynx spiders (Oxyopidae) and its relation to habitat and behaviour. Zoologischer Anzeiger 235(3-4): 133-145. https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/7979075. `opened` (abstract, on an index page that gives it). Log 221 to 223, 266.
- Krugner R, Espindola C, Justus N, Hatton RL 2023. Web Vibrations in Intraspecific Contests of Female Black Widow Spiders, Latrodectus hesperus. Environmental Entomology. https://doi.org/10.1093/ee/nvad003. `opened` (abstract). Log 237.
- Kundu P, Choi N, Rundus AS, Santer RD, Hebets EA 2022. Uncovering 'hidden' signals: previously presumed visual signals likely generate air particle movement. Frontiers in Ecology and Evolution. https://doi.org/10.3389/fevo.2022.939133. `opened` (full text). Log 200.
- Kundu P, Hebets EA 2025. Potential role of foreleg trichobothria in the reception of air particle movement during wolf spider courtship. Journal of Arachnology. https://doi.org/10.1636/JOA-S-22-065. `opened` (abstract). Log 199.
- Land MF 1985. The morphology and optics of spider eyes. In: Barth FG (ed) Neurobiology of Arachnids, pp. 53-78. Springer, Berlin. https://doi.org/10.1007/978-3-642-70348-5. `opened` (book, read in part as stated above). Log 66 to 94.
- Land MF, Barth FG 1992. The quality of vision in the ctenid spider Cupiennius salei. Journal of Experimental Biology 164: 227-242. https://doi.org/10.1242/jeb.164.1.227. `opened` (owner's library copy). Log 15 to 29.
- Land MF, Nilsson D-E 2012. Animal Eyes, 2nd edition. Oxford University Press, Oxford (ISBN 978-0-19-958114-6). https://openlibrary.org/isbn/9780199581146. `opened` (book, read in part as stated above). Log 95 to 98.
- Landolfa MA, Barth FG 1996. Vibrations in the orb web of the spider Nephila clavipes: cues for discrimination and orientation. Journal of Comparative Physiology A 179: 493-508. https://doi.org/10.1007/BF00192316. `opened` (owner's library copy). Log 43 to 50.
- Lesser E 2021. Ogre-faced spiders listen with their legs. Journal of Experimental Biology. https://doi.org/10.1242/jeb.235077. `opened` (abstract; secondary for Stafstrom and colleagues 2020, which it reports). Log 135 to 136.
- Lorenz CD 2012. The spider Heteropoda venatoria and its visual system. Diplomarbeit, University of Vienna (supervisor A. Schmid). https://doi.org/10.25365/thesis.21679. Read at https://utheses.univie.ac.at/detail/19377. `opened` (abstract, and the full text through the university repository). Log 224 to 228, 253 to 255.
- Lott M, Dal Poggetto VF, Greco G, Pugno NM, Bosia F 2022. Prey localization in spider orb webs using modal vibration analysis. Scientific Reports. https://doi.org/10.1038/s41598-022-22898-3. `opened` (full text). Log 197.
- Masmeijer T, Slavič J, De P, Blackledge TA, Habtour E 2026. Gyroscopic spiders: web mechanical intelligence facilitates prey sensing (Research Square preprint; published in Scientific Reports, doi 10.1038/s41598-026-66753-1). Research Square. https://doi.org/10.21203/rs.3.rs-9944883/v1. `opened` (full text). Log 196.
- Masters WM 1984. Vibrations in the orbwebs of Nuctenea sclopetaria (Araneidae). II. Prey and wind signals and the spider's response threshold. Behavioral Ecology and Sociobiology 15: 217-223. https://doi.org/10.1007/BF00292978. `opened` (owner's library copy). Log 39 to 42.
- Miller TE, Rogers S, Wu JJ, Cicirello A, Taylor GK, Mortimer B 2026. Spider leg biomechanics as an information filter for vibration sensing. Proceedings of the Royal Society B. https://doi.org/10.1098/rspb.2026.0915. `opened` (full text). Log 198.
- Moreau S, Saneeibajgiran S, Korst L, Montiglio P-O 2025. Learn to hear your prey: The role of associative learning on web building and hunting behaviour in black widow spiders (Latrodectus hesperus). bioRxiv (preprint). https://doi.org/10.1101/2025.07.04.663247. `opened` (abstract). Log 238 to 239.
- Morehouse NI, Buschbeck EK, Zurek DB, Steck M, Porter ML 2017. Molecular evolution of spider vision: new opportunities, familiar players. Biological Bulletin 233: 21-38. https://doi.org/10.1086/693977. `opened` (abstract). Log 193.
- Morehouse N 2020. Spider vision. Current Biology 30: R975-R980 (pages as printed in the reference list of Pande et al. 2026). https://doi.org/10.1016/j.cub.2020.07.042. Read at https://homepages.uc.edu/~morehonn/wp-content/uploads/2021/02/Morehouse-NI-2020-Curr-Biol.pdf. `opened` (full text). Log 209 to 220, 261.
- Nakamura S, Mukai H, Tokuda M 2022. A trapdoor spider, Latouchia typica (Araneae: Halonoproctidae), uses vibrational cues as a trigger for predatory behavior. Invertebrate Biology. https://doi.org/10.1111/ivb.12388. `opened` (abstract). Log 183.
- Neuhofer DN, Machan R, Schmid A 2009. Visual perception of motion in a hunting spider. Journal of Experimental Biology. https://doi.org/10.1242/jeb.027136. `opened` (abstract). Log 142.
- Nørgaard T 2005. Nocturnal navigation in Leucorchestris arenicola (Araneae, Sparassidae). Journal of Arachnology. https://doi.org/10.1636/04-113.1. `opened` (abstract). Log 161.
- Nørgaard T, Nilsson D-E, Henschel JR, Garm A, Wehner R 2008. Vision in the nocturnal wandering spider Leucorchestris arenicola (Araneae: Sparassidae). Journal of Experimental Biology 211: 816-823. https://doi.org/10.1242/jeb.010546. `opened` (abstract). Log 158 to 160.
- Opell BD, Ware AD 1987. Changes in visual fields associated with web reduction in the spider family Uloboridae. Journal of Morphology 192: 87-100. https://doi.org/10.1002/jmor.1051920202. `opened` (abstract). Log 170.
- Orlando E, Schmid A 2011. Colour blindness of the movement-detecting system of the spider Cupiennius salei. Journal of Experimental Biology. https://doi.org/10.1242/jeb.051672. `opened` (abstract). Log 141.
- Ortega-Escobar J, Ruiz MA 2014. Visual odometry in the wolf spider Lycosa tarantula (Araneae: Lycosidae). Journal of Experimental Biology. https://doi.org/10.1242/jeb.091868. `opened` (abstract). Log 156.
- Ortega-Escobar J, Ruiz MA 2017. Role of the different eyes in the visual odometry in the wolf spider Lycosa tarantula (Araneae, Lycosidae). Journal of Experimental Biology 220: 259-265. https://doi.org/10.1242/jeb.145763. `opened` (abstract). Log 157.
- den Otter CJ 1973. Setiform sensilla and prey detection in the bird-spider Sericopelma rubronitens Ausserer (Araneae, Theraphosidae). Netherlands Journal of Zoology. https://doi.org/10.1163/002829674X00048. `opened` (abstract). Log 178 to 179.
- Pande A, Rose L, England SJ, Rahman IA, Pérez-de la Fuente R, Bodey AJ, Wanelik K, Schlepütz CM, Günther J, Rau C, Blanke A, Sumner-Rooney L 2026. Hunting ecology predicts eye arrangements in the modular visual system of spiders. Current Biology 36: 1-7. https://doi.org/10.1016/j.cub.2026.06.019. `opened` (full text). Log 106 to 109.
- Quirici V, Costa FG 2005. Seismic communication during courtship in two burrowing tarantula spiders: an experimental study on Eupalaestrus weijenberghi and Acanthoscurria suina. Journal of Arachnology. https://doi.org/10.1636/S03-22. `opened` (abstract). Log 180.
- Quirici V, Costa FG 2007. Seismic sexual signal design of two sympatric burrowing tarantula spiders from meadows of Uruguay: Eupalaestrus weijenberghi and Acanthoscurria suina (Araneae, Theraphosidae). Journal of Arachnology. https://doi.org/10.1636/ST06-08.1. `opened` (abstract). Log 181.
- Ruhland F, Caudal J-P, Blois-Heulin C, Trabalon M 2016. Male tarantula spiders' reactions to light and odours reveal their motor asymmetry. Journal of Zoology. https://doi.org/10.1111/jzo.12388. `opened` (abstract). Log 182.
- Schedl A 2017. No evidence for the perception of polarised light in the ctenid spider Cupiennius salei. Thesis, University of Vienna. https://doi.org/10.25365/thesis.49142. `opened` (abstract). Log 257.
- Schmid A 1998. Different functions of different eye types in the spider Cupiennius salei. Journal of Experimental Biology 201: 221-225. https://doi.org/10.1242/jeb.201.2.221. `opened` (abstract). Log 143.
- Seo J-H, Kim K-J, Kim H, Moon M-J 2020. Lyriform vibration receptors in the web-building spider, Nephila clavata (Araneidae: Araneae: Arachnida). Entomological Research. https://doi.org/10.1111/1748-5967.12470. `opened` (abstract). Log 174.
- Stafstrom JA, Hebets EA 2016. Nocturnal foraging enhanced by enlarged secondary eyes in a net-casting spider. Biology Letters. https://doi.org/10.1098/rsbl.2016.0152. `opened` (abstract). Log 259 to 260.
- Stafstrom JA, Michalik P, Hebets EA 2017. Sensory system plasticity in a visually specialized, nocturnal spider. Scientific Reports 7: 46627. https://doi.org/10.1038/srep46627. `opened` (full text). Log 133 to 134.
- Suter RB 2003. Trichobothrial mediation of an aquatic escape response: directional jumps by the fishing spider, Dolomedes triton, foil frog attacks. Journal of Insect Science 3: 19. https://doi.org/10.1093/jis/3.1.19. `opened` (abstract). Log 164.
- Sánchez-Solano K, Robledo-Ospina L, Rao D 2026. Insect perception and flight response to a colourful sit and wait predator. Research Square (preprint). https://doi.org/10.21203/rs.3.rs-9715971/v1. `opened` (preprint page, quoted in fragments). Log 269 to 270.
- Talukder MB, Müller CHG, Zhang D, Schulz S, Löfstedt C, Wang H, Uhl G 2025. Olfaction with legs: spiders use wall-pore sensilla for pheromone detection. Proceedings of the National Academy of Sciences. https://doi.org/10.1073/pnas.2415468121. `opened` (abstract). Log 203.
- Tapia F, Olivares J, Schmachtenberg O 2019. The visual spectral sensitivity of the Chilean recluse spider Loxosceles laeta. Journal of Experimental Biology. https://doi.org/10.1242/jeb.217133. `opened` (abstract). Log 191.
- Tiedemann KB, Ventura DF, Ades C 1986. Spectral sensitivities of the eyes of the orb web spider Argiope argentata (Fabricius). Journal of Arachnology 14(1): 71-78. https://biostor.org/reference/214396. `opened` (full text, the BioStor PDF hosted on archive.org). Log 271 to 274.
- Tong C, Fan Z, Wang L-Y, Zhang Z-S 2026. Genomic signature of repeated transitions to diurnality in spiders. Molecular Biology and Evolution. https://doi.org/10.1093/molbev/msag159. `opened` (abstract). Log 192.
- Vibert S, Scott C, Gries G 2014. A meal or a male: the 'whispers' of black widow males do not trigger a predatory response in females. Frontiers in Zoology 11: 4. https://doi.org/10.1186/1742-9994-11-4. `opened` (full text). Log 231 to 236.
- Walcott C 1963. The effect of the web on vibration sensitivity in the spider, Achaearanea tepidariorum (Koch). Journal of Experimental Biology 40: 595-611. https://doi.org/10.1242/jeb.40.4.595. `opened` (abstract). Log 171.
- Williams DS 1979. The physiological optics of a nocturnal semi-aquatic spider, Dolomedes aquaticus (Pisauridae). Zeitschrift für Naturforschung C. https://doi.org/10.1515/znc-1979-5-625. `opened` (abstract). Log 162.
- Willmott NJ, Black JR, McNamara KB, Wong BBM, Jones TM 2024. The effects of artificial light at night on spider brains. Biology Letters. https://doi.org/10.1098/rsbl.2024.0202. `opened` (abstract). Log 202.
- Wilson RJ, Mulrey TEP, Baldrick D, Uetz GW 2024. The effects of differential eye occlusion on prey and mate recognition in the brush-legged wolf spider Schizocosa ocreata (Hentz, 1844). Journal of Arachnology. https://doi.org/10.1636/JOA-S-22-059. `opened` (abstract). Log 201.
- Yamashita S, Tateda H 1978. Spectral sensitivities of the anterior median eyes of the orb web spiders, Argiope bruennichii and A. amoena. Journal of Experimental Biology 74(1). https://doi.org/10.1242/jeb.74.1.47. `opened` (abstract). Log 165 to 167.
- Yamashita S 1993. Physiological and behavioral studies of changes in absolute and spectral sensitivities on spiders eyes (KAKENHI project 03640608, project report summary, fiscal years 1991-1993). KAKEN database of grants-in-aid, Japan Society for the Promotion of Science. https://kaken.nii.ac.jp/grant/KAKENHI-PROJECT-03640608/. `opened` (project report summary). Log 267 to 268.
- Yamashita S, Arita F 1995. Efferent control in the anterior lateral eyes of orb weaving spiders. Zoological Science 12. https://doi.org/10.2108/zsj.12.385. `opened` (abstract). Log 168.
- Yamashita S, Nakamura T 1999. Circadian oscillation of sensitivity of spider eyes: diurnal and nocturnal spiders. Journal of Experimental Biology. https://doi.org/10.1242/jeb.202.18.2539. `opened` (abstract). Log 256.
- Zhai S, Ren B, Zhang X, Shen F, Ma M, Li X, Li R 2025. Functional study of opsin genes in Pardosa astrigera (Araneae: Lycosidae). Insects 16(6): 595. https://doi.org/10.3390/insects16060595. `opened` (abstract). Log 207.
- Zhou J, Lai J, Menda G, Stafstrom JA, Miles CI, Hoy RR, Miles RN 2022. Outsourced hearing in an orb-weaving spider that uses its web as an auditory sensor. Proceedings of the National Academy of Sciences 119(14): e2122789119. https://doi.org/10.1073/pnas.2122789119. `opened` (full text). Log 130 to 132, 258.
- Zopf LM, Schmid A, Fredman D, Eriksson BJ 2013. Spectral sensitivity of the ctenid spider Cupiennius salei Keys. Journal of Experimental Biology. https://doi.org/10.1242/jeb.086256. `opened` (abstract). Log 139.
- Chamberland L, Agnarsson I, Quayle IL, Ruddy T, Starrett J, Bond JE 2022. Biogeography and eye size evolution of the ogre-faced spiders. Scientific Reports. https://doi.org/10.1038/s41598-022-22157-5. `opened` (abstract and full text, collection). Used only for the move of the Australian species of *Deinopis*, *Dinopis subrufus* among them, to *Asianopis*.

Phone inputs, `opened`: MDN, `DeviceMotionEvent.requestPermission()` (https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEvent/requestPermission_static: needs transient activation from a user gesture, resolves to "granted" or "denied", secure contexts only); MDN, Sensor APIs (https://developer.mozilla.org/en-US/docs/Web/API/Sensor_APIs: the `frequency` option is readings per second and the actual rate may be lower; permission names `accelerometer` and `gyroscope`; a Permissions Policy can block them); MDN, `DeviceMotionEvent.interval` (https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEvent/interval: the interval in milliseconds at which the hardware gives data). The engine branch `agent/engine` (`src/cam.a.js`, `src/cam.b.js`, `src/cam.c1.js`) was read for the names of its new fields.

## 8. Questions for a specialist

1. Has anyone measured flicker fusion or receptor spacing in an orb weaver, in particular *Argiope* or *Trichonephila*?
2. Do lynx spiders (*Peucetia*, *Oxyopes*) have fast secondary eyes like those of day-active crab spiders, or slow ones like those of wolf spiders?
3. Is the ground and sac spider group (Gnaphosidae, Clubionidae, Anyphaenidae, Corinnidae and their relatives) closer in sensing to tarantulas or to wolf spiders, and which of these families use vision when hunting?
4. For a web builder, does the direction of a prey's vibration across the legs work the same way in a tangle web as in an orb web?
5. Which wolf spiders hunt by day, and do their eyes differ in speed or sensitivity from the night-active ones?
6. How well would a phone's accelerometer, sampled at 60 Hz or so, capture the 5 to 30 Hz shaking that orb weavers use, compared with a laser vibrometer on the web?
