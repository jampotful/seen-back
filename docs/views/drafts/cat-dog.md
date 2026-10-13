# Sensing sheet: cats and dogs (families Felidae and Canidae), with the human reference values

Written on 13 October 2026 from 01:45 UTC by the research agent for the unit `cat-dog`. The evidence log is `docs/views/evidence/cat-dog.jsonl`; a reference such as **L17** names line 17 of that log. The wanted list is `docs/views/wanted/cat-dog.jsonl`.

**What was read.** The collection on `pub/lit-t1` (topics `carnivores` and `methods`: abstracts in the index, and full texts on disk for Inger et al. 2014, Kanizsár et al. 2017, Kopania and Clark 2024 and Klećkowska-Nawrot et al. 2026). From the owner's Drive: Caves et al. 2018, the whole main text (pp. 358 to 372; the supplementary tables were not in the file); Land and Nilsson 2012, *Animal Eyes*, which came through only in part: the front matter, chapter 1, chapter 2 and chapter 3 up to p. 65 (the middle of "Sensitivity"). Chapters 4 to 9, among them chapter 5 on lens eyes on land, chapter 6 on mirrors in eyes (the tapetum) and chapter 9 on eye movements, did not come through. On the web: publisher and repository pages listed in section 7.

**Pages refused or unreachable.** These shaped what could be opened, and nothing behind them is used second-hand without saying so:

- Europe PMC's REST service, PubMed, Crossref (after six queries) and doi.org refused with a rate limit (HTTP 429), and I stopped fetching each of them.
- PubMed Central showed a browser check (reCAPTCHA) on every article, so the open copies of Gunter (1951), Loop and colleagues (1987), Bowmaker and Dartnall (1980) and the PMC copy of Banks and colleagues (2015) could not be read there.
- science.org and the Semantic Scholar API returned errors. A Harvard course copy of Hecht, Shlaer and Pirenne (1942) is closed to robots.
- The machine's own shell reaches no site but GitHub, so every web page was read through a fetch tool that relays quotations of at most 125 characters. Where a table row is quoted, the quote is the tool's rendering of the row, and the log line says so.

**Unfinished.** Marked **[unfinished]** where they occur: the pupil shapes of pumas, cheetahs, leopards, jaguars, coyotes and gray foxes in life; the cat's binocular overlap; any measured acuity for lions, tigers, pumas, bobcats or foxes; the luminance dependence of cat and dog acuity; and the check of the two-cone colour matrix (`DEUTAN`).

## 1. Scope

**The two families.** iNaturalist research-grade records in GBIF (dataset `50c9509d-22c7-4a22-a47d-8c48425ef4a7`, read on 13 October 2026 through the occurrence API with `facet=genusKey` and `facet=speciesKey`; names looked up by key). The totals match `docs/VIEWS.md` (cat 165,169; dog 296,559).

| Family and genus | Records | Share of family | Most recorded species |
|---|---:|---:|---|
| **Felidae** | **165,169** | | |
| *Felis* | 74,223 | 44.9% | domestic cat 71,687 (43.4%); wildcat 1,771 |
| *Lynx* | 36,922 | 22.4% | bobcat 34,255 (20.7%); Canada lynx 1,492 |
| *Panthera* | 29,020 | 17.6% | lion 15,206 (9.2%); leopard 7,348; jaguar 3,988; tiger 2,478 |
| *Puma* | 12,031 | 7.3% | puma 11,119 (6.7%) |
| *Leopardus* | 5,038 | 3.1% | ocelot 2,689 |
| *Acinonyx* | 4,201 | 2.5% | cheetah 4,201 |
| other genera | 3,734 | 2.3% | leopard cat 806, guiña 179 and others |
| **Canidae** | **296,559** | | |
| *Canis* | 130,881 | 44.1% | coyote 96,149 (32.4%); *Canis lupus* 28,571 (9.6%), of which domestic dogs 20,185 (6.8%); golden jackal 4,389 |
| *Vulpes* | 107,336 | 36.2% | red fox 102,818 (34.7%); Arctic fox 1,892 |
| *Urocyon* | 33,377 | 11.3% | gray fox 30,532 (10.3%); island fox 2,845 |
| *Lycalopex* | 7,319 | 2.5% | Pampas fox 4,434; culpeo 2,548 |
| *Lupulella* | 6,500 | 2.2% | jackals |
| other genera | 11,146 | 3.8% | crab-eating fox 3,352; raccoon dog 3,265; African wild dog 2,018 |

In **Alachua County** (GBIF `gadmGid=USA.10.1_1`, checked against the records' county name), Felidae hold 330 records, 281 of them free-roaming domestic cats (85%) and 49 bobcats (15%). Canidae hold 150: red fox 93 (62%), coyote 46 (31%) and gray fox 11 (7%). No domestic dog in the county has a research-grade record, since most pet photos stay casual on iNaturalist (`docs/COVERAGE.md`).

**Where the views should split.** Three differences change what the picture draws on every frame, and each follows a line between genera.

1. **Pupil and lens in cats.** The domestic cat has an upright slit pupil and a multifocal lens (L20, L48). The Siberian tiger has a round pupil and a monofocal lens (L49), and a co-author of the pupil survey says lions and tigers have round pupils, like people and dogs (L103). The lynx pupil is an upright oval (L50, L137). Across the family, slits are ancestral, and round pupils evolved six times and upright ovals two to four times, tracking the time of day a species hunts (L55). One picture that smears blur up and down would be false for the 27.4% of felid records in *Panthera*, *Puma* and *Acinonyx*. Walls (1942) states that large carnivores have round pupils and that only the smaller cats close a slit fully (L140, L142), which places the puma and the cheetah with the lions; species-by-species confirmation is **[unfinished]** (82% of slit-pupilled species stand under 42 cm at the shoulder, L23).
2. **Pupil and lens in canids.** The red fox has an upright slit, or in Walls's words a vertical ellipse, and a multifocal lens; the wolf and the dog have round pupils (L51, L141, L52, L53). The gray fox has oval pupils, on a weak source (L104). Slits and round pupils each evolved twice in the family (L56). The dog view's round pupil is false for the 47.4% of canid records in *Vulpes* and *Urocyon*, and for 69% of Alachua's.
3. **Where the eye is sharpest, in dogs.** Wolves have a pronounced horizontal streak (L38). Domestic dogs range from a streak to a strong central spot with almost no streak, in step with skull length (L36, L37). This splits breeds, which the app cannot tell apart from a photograph, so it becomes a setting inside the dog view.

**Commitment: four views.**

| View | Routing (by genus) | World records | Alachua records |
|---|---|---:|---:|
| `cat` | Felidae except the four genera below | 119,917 (72.6% of Felidae) | 330 (100%) |
| `bigcat` | *Panthera*, *Puma*, *Acinonyx*, *Neofelis* | 45,252 (27.4%; *Neofelis* not counted) | 0 |
| `dog` | Canidae except the two genera below | 155,846 (52.6% of Canidae) | 46 (31%) |
| `fox` | *Vulpes*, *Urocyon* | 140,713 (47.4%) | 104 (69%) |

Inside `cat`, *Lynx* takes an oval pupil and Pallas's cat (*Otocolobus*) a round one (L124). Inside `fox`, *Urocyon* takes an oval pupil. The South American foxes (*Lycalopex*), the raccoon dog and the bat-eared fox stay in `dog` until their pupils are known. `tools/species/eyes.py` would carry these rules, and the word table in `src/cam.r.js` would send "lion", "tiger", "leopard", "jaguar", "cougar", "puma" and "cheetah" to `bigcat`, and "fox" to `fox` (the "flying fox" exception stays). No file outside this unit's three files was changed.

## 2. The views proposed

Rows are written to the standard in the brief. Each is followed by the log lines behind it.

### 2.1 `cat` (domestic cat, bobcat, lynx, ocelot and the other small cats)

```
['m', 'Sharpness', 'In good light a cat sees fine detail about a sixth to a tenth as well as a person does. This view is blurred to match.'],
```
L17 (10 cycles per degree, behavioural), L18 (3 to 9 in behavioural studies), L95 (people about seven times sharper), L1 and L6 (people about 60).

```
['m', 'Sharpest spot', 'A cat sees most sharply in a small central patch of its retina, the area centralis. Away from that patch its sharpness falls off far more gently than a person’s does. This view keeps the centre sharp and softens the edges a little.'],
```
L88 and L89 (acuity in the area centralis, down by half an octave at 4 degrees and 1.3 octaves at 16), L2 and L60 (a person's falls to half by about 2.6 degrees and to a tenth by 7).

```
['m', 'Colour', 'Cats have two kinds of colour-sensing cells, most sensitive to blue-violet and to yellow-green light, where people have three. Reds and greens are hard for a cat to tell apart. This view shows colours the way a person with red-green colour blindness sees them.'],
```
L69, L70 and L72 (cones near 450 and 550 to 556 nm), L73, L74, L12 and L128 to L130 (people: three cones near 420, 530 and 560 nm).

```
['m', 'Pupil', 'A cat’s pupil closes to a narrow upright slit in bright light and opens wide in the dark, changing its area about 135-fold, where a person’s changes about 15-fold. A slit like this smears out-of-focus things up and down, and this view does the same.'],
```
L20, L21, L22, L24, L48. For *Lynx* the row reads: `'A bobcat’s or lynx’s pupil closes to an upright oval, between a house cat’s slit and a lion’s round pupil. This view smears out-of-focus things a little more up and down than sideways.'` (L50, L137).

```
['m', 'Lens', 'A cat’s lens has zones that bring different colours into focus together, and the slit pupil keeps every zone in use even in bright light.'],
```
L48, L54, L120.

```
['m', 'Field of view', 'A cat takes in at least 200 degrees around itself, and an early optical measurement put the limit at 287, thanks to its large, strongly curved cornea. A person takes in about 200. This view draws the lower figure, so it keeps the field your camera gives.'],
```
L77 and L132 (cat 200, secondary), L154 and L156 (287 in all, about 200 for one eye, optical), L57 (people 200, from clinical perimetry), L76 (each cat eye reaches at least 90 degrees to its own side in perimetry). The last sentence holds once the app's human reference becomes 200 degrees (section 3.3). **[unfinished]**: which figure describes the field a cat uses.

```
['m', 'Two eyes and depth', 'Both of a cat’s eyes face forward, and their views overlap over 60 to 140 degrees in front, depending on how it is measured, so a cat can judge distance by comparing them. Its upright slit adds a second cue, because out-of-focus horizontal edges blur more than vertical ones, and small hunters with eyes close to the ground make the most of it.'],
```
L76 (60, by behavioural perimetry), L144 (120 or more, Kahmann's figures as given by Walls 1942), L155 (130, Thieulin's optical figure), L78 (about 140), L107 (kittens learn a depth task much faster with both eyes), L23, L24, L125 (the blur cue and short animals). **[unfinished]**: the gap between the behavioural and the anatomical figures for overlap is not settled.

```
['i', 'Distance in this view', 'A phone camera can’t measure distance, so this view assumes that things lower in the picture are closer. Tap the screen to move the focus.'],
```
No source: the app's own convention (`docs/SOURCES.md`).

```
['m', 'Dim light', 'A cat can see by light up to about seven times dimmer than the faintest a person can use. A mirror-like layer behind its retina, the tapetum, sends light back through the light-sensing cells for a second pass. This view brightens the shadows to show it.'],
```
L80 and L134 (up to 7 times; 6 to 8 times), L81 (tapetum reflects up to 130 times more than the human fundus), L7 (people's threshold).

```
['m', 'Movement', 'In bright light a cat notices that something is moving only when it moves about ten times faster than the slowest movement a person can see.'],
```
L83, L136, L15; L26 gives 1 to 10 degrees a second for cats, rats and pigeons together, where people manage under 0.1.

```
['m', 'Flicker', 'A cat sees a flickering light as steady once it flickers faster than about 48 times a second, a little below the 60 at which people stop seeing flicker. This view leaves the pace of the picture as it is.'],
```
L25, L13.

```
['x', 'Ultraviolet', 'A cat’s lens lets through much of the ultraviolet light that a person’s lens blocks, so a cat’s blue-sensitive cells probably register some of it. A phone camera filters out almost all ultraviolet, so this view leaves it out.'],
```
L100, L102, L127.

Twelve rows.

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who`, `cue` | 'Cat', 'a cat', 'Out-of-focus things smear up and down. Tap the screen to move the focus.' | the app's wording (unchanged) |
| `fov` | 200 | L77, L132; with the human reference at 200 (section 3.3) this draws no bending |
| `cpd` | 8 | L17, L18, L95 (confirmed) |
| `topoA` | 1 | L88 |
| `fall` | 1.0 (was 2.0) | L89: at the top and bottom of a phone held upright, about 12 degrees out on the app's 24-degree screen, a cat keeps about half its central acuity, so 1 + `fall` = 2. The arithmetic is mine |
| `pupil` | 'v'; *Lynx* an oval (aspect 0.6, **invented**); *Otocolobus* 'o' | L20, L48; L50, L137; L124 |
| `dof` | 26 | **invented** (unchanged) |
| `M` | `DEUTAN` | L69, L70: two cones. Drawing them through a deuteranope simulation is **invented**: the cat's long cone (550 to 556 nm) lies about 9 nm from the human L cone that a deutan simulation keeps, and about 20 nm from the M cone a protan simulation keeps (my reasoning). The matrix itself is unverified (section 5) |
| `gain` | 1.7 | **invented** (L80, L81 say only that the cat sees in dimmer light) |
| `sat` | 0.8 | **invented** |
| `rate`, `persist` | none | L25: the cat's flicker limit is below a person's, and the difference is within the spread between methods (L13, L14) |

**New effects the evidence calls for.**

1. **A pupil that answers to the light, and a night shift.** In bright light the slit closes and the blur of out-of-focus things stretches into tall, thin streaks; in dim light the pupil opens, the blur evens out, the shadows lift and the colours drain away, because the dark-adapted cat eye signals almost entirely through rods (L21, L71). The person would watch the view breathe with the room. Phone input: the camera frame's mean brightness corrected by the exposure time and ISO that `MediaStreamTrack.getSettings()` reports on browsers that report them (to be checked on a phone), with the frame brightness alone as the fallback. Difficulty: easy to medium, one smoothed light uniform that `mix` uses to move the pupil aspect, `dof`, `sat` and `gain` between a day and a night setting. What makes it beautiful as well as true: a slow change over several seconds, since a cat's dark adaptation goes on for up to an hour (L80 note), and a night palette that leans toward the rods' blue-green peak near 501 nm (L71) in place of plain grey. The row it would add: `['m', 'Colour at night', 'In the dark, almost all of the signals leaving a cat’s eye come from rods, a single kind of light-sensing cell, so colours fade. This view loses its colour as the light fades.']` (L71).
2. **The near point.** A cat probably cannot focus on anything closer than about 25 cm (L82, secondary). Phone input: `focusDistance` from the camera track's settings, where the browser reports it; below 0.25 m the whole view softens. Difficulty: easy where the setting exists. It needs a row once built.
3. **Eyeshine.** A soft bloom around bright points at night would stand for the tapetum's second pass of light, which Walls (1942) says spreads onto neighbouring rods and can blur the image seen in dim light, though the cat is far from badly off (L149; the cat's tapetum is up to 15 cell layers thick, L148). The strength would be **invented**, and Land and Nilsson's chapter 6 (not read) should give a figure. Difficulty: easy (one blur-and-add pass, scaled by the light uniform). It needs an `i` row.

### 2.2 `bigcat` (lions, tigers, leopards, jaguars, pumas, cheetahs, clouded leopards)

```
['m', 'Pupil', 'Lions, tigers and the other large cats have round pupils, like people and dogs, where house cats have upright slits. Out-of-focus things blur evenly in every direction in this view.'],
```
L103, L49, L140 (large carnivores have round pupils; none approaches a slit). Species by species, the puma's, the leopard's, the jaguar's and the cheetah's pupils rest on that general statement (wanted: Banks et al. 2015, table S1).

```
['m', 'Lens', 'A tiger’s lens focuses every colour at the same depth, where a house cat’s lens has zones for several. Why the large cats lack those zones is unknown.'],
```
L49.

```
['m', 'Colour', 'Lions, tigers, leopards and cheetahs have two kinds of colour-sensing cells, as house cats do, where people have three. This view shows colours the way a person with red-green colour blindness sees them.'],
```
L138 (S cones in the cheetah, the bobcat and the leopard), L97 and L98 (S and M cone maps in lion, tiger, cheetah and lynx), L12.

```
['m', 'Cheetah', 'A cheetah sees about a third as much detail as a person, and about three times as much as a house cat. Its cones for yellow-green light crowd into a band along the horizon, a pattern found in animals of open country.'],
```
L94 (23 cycles per degree), L97.

```
['i', 'Sharpness', 'No measurement was found for lions, tigers, leopards or pumas. Their eyes are about one and a half times as long as a house cat’s, and longer eyes usually see finer detail, so this view guesses that they see about a fifth as much detail as a person.'],
```
L121 (tiger eye 29.4 mm), L75 (cat 19.75 mm), L122 note (lion 27.4 to 32.2 mm), L126, L143 (Walls: high acuity is found only in large animals such as the great cats).

```
['m', 'Dim light', 'In a study of the eyes of three kinds of wild cat, the lions had the largest tapetum, the mirror-like layer behind the retina that gives light a second pass. This view brightens the shadows to suggest it.'],
```
L122.

```
['i', 'Field of view and depth', 'No measurement was found for these. This view keeps the field your camera gives and assumes that things lower in the picture are closer.'],
```
No source.

```
['x', 'Ultraviolet', 'House cats’ lenses let through ultraviolet light, and big cats have not been tested. A phone camera filters out almost all ultraviolet, so this view leaves it out.'],
```
L100, L127.

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who`, `cue` | 'Lion, tiger, leopard', 'a big cat', 'Out-of-focus things blur evenly in every direction.' | the app's wording |
| `fov` | unset (the camera's field) | no source |
| `cpd` | 12; the cheetah (*Acinonyx*) 23 | 12 is an inference: cat 8 × (29.4 / 19.75) = 11.9 (L121, L75, L126), resting on acuity scaling with focal length when receptor spacing stays the same (Land and Nilsson 2012, eq. 3.2, p. 50). Cheetah L94 |
| `topoA` | 1; cheetah `topoS` 1 with `topoA` 0.4 | `topoA` by analogy with the domestic cat (**invented**); cheetah L97, weights **invented** |
| `fall` | 1.0 | by analogy with the domestic cat (L89), **invented** |
| `pupil` | 'o' | L103, L49 |
| `dof` | 14 | **invented** |
| `M` | `DEUTAN` | L138, L97; the matrix as for `cat` |
| `gain` | 1.6 | **invented** (L122) |
| `sat` | 0.8 | **invented** |

**New effects.** The night shift (2.1, effect 1) applies, with a round pupil that only widens and narrows. A cheetah setting (sharper, with a horizon band) is a species profile in waiting (section 4).

### 2.3 `dog` (domestic dog, coyote, wolf, jackals and the other canids with round pupils)

```
['m', 'Sharpness', 'Dogs see fine detail between about a third and an eighth as well as people do, depending on the dog and the test. When dogs and people were tested side by side, people saw about three times as much detail, by day and at night. This view is blurred to match.'],
```
L166 to L168 and L170 to L172 (5.5 to 19.5 cycles per degree in bright light; people 32 to 44 in the same set-up; about three times), L29 (typical 20/75), L30, L31, L46 (no better than 12.6 in earlier work), L118, L139, L1.

```
['m', 'Sharpest spot', 'Wolves and long-nosed dogs see most sharply along a band level with the horizon. Short-nosed dogs such as pugs see most sharply in one central spot, and most breeds fall in between. This view shows the band.'],
```
L36, L37, L38.

```
['m', 'A hidden fovea', 'Inside that central spot, a dog has a tiny patch where cones pack as densely as in the centre of a human eye. Many cones share each nerve fibre that leaves the eye, so a dog still sees far less detail than a person.'],
```
L44, L45, L46, L118.

```
['m', 'Colour', 'Dogs have two kinds of colour-sensing cells, most sensitive to violet-blue and to yellow-green light, where people have three. Reds, oranges, yellows and greens look much alike to a dog, and one shade of blue-green looks grey. This view shows colours the way a person with red-green colour blindness sees them.'],
```
L64 to L67, L108, L109, L68 (neutral point near 480 nm, secondary), L151 (dogs answer a deuteranopia test the way red-green colour-blind people do).

```
['m', 'Field of view', 'A dog takes in about 240 to 250 degrees around itself, where a person takes in about 200, and the figure varies by breed. Only 30 to 60 degrees straight ahead are seen by both eyes, against about 120 for a person. This view widens the picture at its edges to suggest the wider sweep.'],
```
L79, L157, L32, L33, L57, L58.

```
['m', 'Flicker', 'A dog can see a light flicker up to about 75 times a second, where a person stops at about 60, so some lamps and screens that look steady to people may flicker for a dog. This view runs slightly slowly and then jumps ahead to suggest the difference.'],
```
L27, L28, L85, L13. As `docs/SOURCES.md` says of the other views, a higher flicker limit does not show that time feels slower; the slowed picture is a way of drawing.

```
['m', 'Slow movement', 'A dog notices that something moves once it crosses about three-quarters of a degree of its view each second, about the speed of a person walking 75 metres away. People notice movement more than seven times slower.'],
```
L34, L15. A walker at 1 metre a second, 75 metres away, crosses 0.76 degrees a second (my arithmetic).

```
['m', 'Dim light', 'A dog’s retina holds more rods than a person’s, even in its sharpest area, and most dogs have a mirror-like tapetum behind the retina that gives light a second pass. In a study of 539 dogs, the tapetum was full-sized in seven dogs in ten and missing in about two in a hundred. This view brightens the shadows a little.'],
```
L119, L87, L43 (coyotes see by the natural light of many nights). Dim light helps a dog detect light and movement; it does not make it sharper-sighted than a person: at about moonlight level dogs resolved 1.8 to 3.5 cycles per degree and people 5.9 to 9.9 (L169, L171).

```
['m', 'Short noses', 'Short-nosed breeds follow a pointing hand better than long-nosed breeds, and short-headed dogs meet a stranger’s eyes sooner.'],
```
L106, L105.

```
['m', 'Movement at a distance', 'In a study of fourteen police dogs, the best recognised a moving object 810 to 900 metres away, and the same object standing still only within 585 metres.'],
```
L152 (Schmid's study as reported by Walls 1942; Miller 2001 repeats it, L84). Movement makes a distant object easier to pick out, for people as for dogs; the dog's threshold for slow movement is still higher than a person's (row "Slow movement").

```
['i', 'Distance in this view', 'A phone camera can’t measure distance, so this view assumes that things lower in the picture are closer. Tap the screen to move the focus.'],
```
No source.

```
['x', 'Ultraviolet', 'A dog’s lens lets through much of the ultraviolet light that a person’s lens blocks, so a dog’s blue-sensitive cells probably register some of it. A phone camera filters out almost all ultraviolet, so this view leaves it out.'],
```
L101, L102, L127.

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who`, `cue` | 'Dog, coyote, wolf', 'a dog', 'The sharpest part is a band along the horizon. Tap the screen to move the focus.' | the app's wording |
| `fov` | 240 | L79, L157 (confirmed: 240 and 250) |
| `cpd` | 9 (was 11) | L166, L29 to L31, L46: measured values run from about 5.5 to 19.5 cycles per degree, most between 6 and 13, with a typical dog near 8 to 10; 9 is my pick within them |
| `topoS`, `topoA` | 1 and 0.5 (was `topoS` 1 alone); short-nose setting 0.2 and 1 | L36, L37, L44; the weights are **invented** |
| `fall` | 1.6 | **invented** (unchanged) |
| `pupil` | 'o' | L53 |
| `dof` | 10 | **invented** (unchanged) |
| `M` | `DEUTAN` | L64 to L66: two cones at 429 to 435 and 555 nm; the dog's long cone sits 9 nm below the human L cone that a deutan simulation keeps (my reasoning) |
| `gain` | 1.3 | **invented** (L87, L119) |
| `sat` | 0.85 | **invented** |
| `rate` | 0.8 (new) | L27: 60 / 75, the app's convention for a faster eye |

**New effects the evidence calls for.**

1. **A nose setting.** A chip under the dog's name, "Long nose" or "Short nose", moves the sharpness from the horizon band to one central spot (L36). Easy. True to McGreevy and colleagues, and the person sees at once why a pug and a greyhound watch different parts of a room.
2. **Slow movement stands still.** Parts of the scene moving slower than about 0.8 degrees a second (L34) stay held on an earlier frame until they have moved far enough to register, then jump into place. Input: the salience map the engine track is building, with the phone's own movement removed through the gyroscope. Difficulty: medium. What the person sees: a distant walker seems to freeze and step, while anything close and quick moves as usual. The threshold needs the screen's degrees per pixel, which `VIEW_DEG` already sets. It needs a row once built.
3. **The night shift** (2.1, effect 1), with the dog's rods peaking near 508 nm (L116). For dogs the shift can follow measurements: sharpness falls from about 9 cycles per degree in room light (43 cd/m²) to about 2.6 near moonlight (0.0087 cd/m²), the middle of 1.8 to 3.5, while people fall from 32 to 44 to 6 to 10 in the same set-up (L166, L169 to L171). The ratio of dog to person stays near a third, so the view's blur should grow in the dark by the same factor as the person's own.
4. **The near point** (2.1, effect 2), at 0.33 to 0.5 m (L82).

### 2.4 `fox` (red fox, Arctic fox, gray fox and their relatives)

```
['m', 'Pupil', 'A red fox’s pupil narrows in bright light to a tall, thin oval, close to a house cat’s slit, and its lens has zones that bring several colours into focus together. Out-of-focus things smear up and down in this view.'],
```
L51, L141 (foxes have vertical ellipses; only the smaller cats close a slit fully, L142), L54. For *Urocyon* the row reads: `'A gray fox’s pupils are oval, where red foxes and their relatives have upright slits. Out-of-focus things smear a little more up and down than sideways in this view.'` (L104, a weak source; **[unfinished]**).

```
['m', 'Sharpest spot', 'A red fox sees most sharply in a small central spot, with a weaker band along the horizon. The Arctic fox, which lives on open tundra, has a stronger band. This view shows a sharp centre and a faint band.'],
```
L39, L41, L42.

```
['m', 'Colour', 'Red foxes, Arctic foxes and island gray foxes have the same two kinds of colour-sensing cells as dogs, most sensitive to violet-blue and to yellow-green light. This view shows colours the way a person with red-green colour blindness sees them.'],
```
L110 to L115, L40.

```
['m', 'Night eyes', 'A red fox’s retina holds more rods for each cone than an Arctic fox’s, the mark of an eye built for night in woodland. This view brightens the shadows.'],
```
L41 (note), L39.

```
['i', 'Sharpness', 'No measurement of a fox’s sharpness was found. A red fox’s sharpest area packs its nerve cells about as densely as a dog’s, so this view guesses that a fox sees about as much detail as a typical dog.'],
```
L39 (7,900 ganglion cells per mm²), L37 (dogs 6,400 to 14,400), L162 (foxes have rather large eyes yet low acuity, like other rod-rich carnivores of dog size). No measured eye size for foxes was found.

```
['x', 'Compass', 'Red foxes hunting mice pounce mostly toward the north-east, and the pounces that succeed cluster toward the north. The researchers think the foxes may be using the earth’s magnetic field. This view leaves that sense out.'],
```
L117.

```
['i', 'Field of view, flicker and depth', 'No measurement was found for foxes. This view keeps the field your camera gives and assumes that things lower in the picture are closer.'],
```
No source.

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who`, `cue` | 'Fox', 'a fox', 'Out-of-focus things smear up and down.' | the app's wording |
| `fov` | unset | no source |
| `cpd` | 8 | **invented** (the `i` row): the typical dog's value (L29) |
| `topoA`, `topoS` | 1 and 0.4 | L39, L42; weights **invented** |
| `fall` | 1.2 | **invented** |
| `pupil` | 'v'; *Urocyon* an oval (aspect 0.6, **invented**) | L51; L104 |
| `dof` | 22 | **invented** |
| `M` | `DEUTAN` | L110, L111 |
| `gain` | 1.6 | **invented** (L41 note) |
| `sat` | 0.8 | **invented** |

**New effects.**

1. **The compass arc.** The phone's compass (`DeviceOrientationEvent` with an absolute heading on Android, `webkitCompassHeading` on iOS after a tap for permission) could warm the lower edge of the picture faintly when the phone faces between north and east. The arc would be the app's own invention, grounded in L117, and the `x` row above would become an `i` row saying so. Difficulty: easy to medium. It turns a sense no camera has into a quiet direction in the room, which suits the evidence: the foxes' advantage is in aim.
2. **The night shift**, as in 2.1, effect 1.

### 2.5 A sketch for the app thread

The fields below follow the tables above; `ax` is a proposed numeric pupil aspect (the width of the blur relative to its height) that `paramsOf` would use in place of the fixed 0.3 for `'v'`. No file outside this unit was changed.

```
cat:    { chip: 'Cat', who: 'a cat', fov: 200, cpd: 8, topoA: 1, fall: 1.0, pupil: 'v', dof: 26, M: DEUTAN, gain: 1.7, sat: .8,
          byGenus: { Lynx: { ax: .6 }, Otocolobus: { pupil: 'o' } }, rows: [ /* the twelve rows of 2.1 */ ] },
bigcat: { chip: 'Lion, tiger, leopard', who: 'a big cat', cpd: 12, topoA: 1, fall: 1.0, pupil: 'o', dof: 14, M: DEUTAN, gain: 1.6, sat: .8,
          byGenus: { Acinonyx: { cpd: 23, topoS: 1, topoA: .4 } }, rows: [ /* the eight rows of 2.2 */ ] },
dog:    { chip: 'Dog, coyote, wolf', who: 'a dog', fov: 240, cpd: 9, topoS: 1, topoA: .5, fall: 1.6, pupil: 'o', dof: 10, M: DEUTAN, gain: 1.3, sat: .85, rate: .8,
          shortNose: { topoS: .2, topoA: 1 }, rows: [ /* the twelve rows of 2.3 */ ] },
fox:    { chip: 'Fox', who: 'a fox', cpd: 8, topoA: 1, topoS: .4, fall: 1.2, pupil: 'v', dof: 22, M: DEUTAN, gain: 1.6, sat: .8,
          byGenus: { Urocyon: { ax: .6 } }, rows: [ /* the seven rows of 2.4 */ ] }
```

In `paramsOf`, `180 / (m.fov || 180)` would become `200 / (m.fov || 200)` if the app adopts the human field of 200 degrees (section 3.3).

## 3. The existing views checked

### 3.1 `cat` in `src/cam.a.js`

| Row or field | Today | Check |
|---|---|---|
| Sharpness (`m`) | "about a fifth to a tenth as much detail as people do" | **corrected** to a sixth to a tenth. The cited source (Lamm 2013) gives 20/100 to 20/200 (L133), which is 3 to 6 cycles per degree if 20/20 is 30; behavioural gratings give 3 to 10 (L17, L18, L88), and a fifth (12) is above them |
| `cpd` 8 | | **confirmed** (L17, L18, L95) |
| Colour (`m`) | two kinds of cell; "reds look olive or grey to a cat" | **confirmed** for two cones (L69, L70, L72, L73). The olive-or-grey clause describes the drawing, and no source tests what a cat sees as red; **corrected** to say that reds and greens are hard to tell apart |
| Pupil (`m`) | slit, ambush hunters, smears up and down | **confirmed** (L20, L23, L24, L48) |
| Field of view (`m`) | cat about 200, "a person about 180" | the cat's 200 is **confirmed** from secondary sources (L77, L132), and an optical figure is wider, 287 (L154); the person's 180 is the older figure for eyes at rest (L158), **corrected** to about 200 from clinical perimetry (L57) |
| `fov` 200 | | **confirmed**; see 3.3 for the human reference |
| Dim light (`m`) | "six to eight times dimmer than people need" | **confirmed** from secondary sources only (L134; L80 says up to 7). The primary measurement, Gunter (1951), was not opened |
| Depth (`i`) | height in the frame stands for distance | **confirmed** as a guess; the slit pupil's blur cue is now an `m` row (L23, L24, L125) |
| Sharpest spot (`i`) | "assumes that a cat sees most sharply straight ahead" | **measured** now (L88, L89): upgrade to `m` |
| `topoA` 1, `fall` 2.0 | | `topoA` **confirmed**; `fall` **corrected** to 1.0 (L89) |
| `dof` 26, `gain` 1.7, `sat` 0.8 | | the app's own choices; nothing to confirm |
| `M` `DEUTAN` | | two cones **confirmed**; the matrix values remain **unsupported** (section 5) |

Walls (1942) judged cats colour-blind (L147); later recordings found two cone classes (L69, L70, L72), so his verdict is superseded. `docs/SOURCES.md` lists "a central sharp spot in cats" among the entries made from memory; it now rests on Pasternak and Horn (1991, L88). Its second row (the 2013 cat figures) is a popular article whose figures the author says he checked with veterinary ophthalmologists (L132 to L136); the primary papers in this log should replace it.

### 3.2 `dog` in `src/cam.a.js`

| Row or field | Today | Check |
|---|---|---|
| Sharpness (`m`) | "about a quarter to a seventh" | **corrected** to a third to an eighth: measured dog acuity runs from about 5.5 to 19.5 cycles per degree (L166 to L168, L29 to L31, L46), people saw about three times as much in a side-by-side test (L172), and the press summary's four to seven times (L139) rests on a table not opened |
| `cpd` 11 | | **corrected** to 9 |
| Sharpest spot (`m`) | long noses a band, short noses a spot | **confirmed** (L36, L37, L38); the fovea-like patch is new (L44) |
| `topoS` 1, `fall` 1.6 | | `topoS` **confirmed**; add `topoA` 0.5; `fall` stays an invented value |
| Colour (`i`) | two kinds of cell | **measured**: upgrade to `m` (L64 to L67, L108, L109). `docs/SOURCES.md` lists two cone types in dogs as made from memory; it now rests on Neitz and colleagues (1989) |
| Field of view, dim light and depth (`i`) | guesses | field **measured** from secondary sources (L79, L32): upgrade to `m`; dim light **measured** (L87, L119): `m`; depth stays `i` |
| `fov` 240, `pupil` 'o' | | **confirmed** (L79, L157; L53) |
| `rate` | none | add 0.8 (L27) |

### 3.3 The human reference values

Every row that compares an animal with "people" or "a person" should use these figures.

| What | Figure for rows | Behind it |
|---|---|---|
| Sharpness | about 60 cycles per degree at the centre of gaze (a cycle is one dark and one light stripe). Comparisons are fractions of 60 | L1, L6 (retinal sampling about 60), L5 (optical limit about 70 with a 2 mm pupil), L3 (73 in a textbook table) |
| Sharpness away from the centre | half by about 2.5 degrees, a tenth by about 7 degrees | L60, L2 |
| Sharpness in dim light | about 32 to 44 cycles per degree in room light and 6 to 10 near moonlight, in a test built for dogs | L170, L171 |
| Field of view | about 200 degrees side to side with both eyes; about 120 of them seen by both eyes; about 135 top to bottom | L57, L58, L59. The older round figure of 180 (L158, with the eyes at rest; repeated in L77 and L132) is smaller than clinical perimetry finds; 140 for the overlap is Kahmann's maximum (L145) |
| Flicker | about 60 times a second at the centre of view in bright light; in very bright light at the edge of view, up to about 90 to 110; fewer in dim light | L13, L61, L62, L63, L164 (rises with the logarithm of intensity) |
| Colour | three kinds of cone, most sensitive near 420 (blue-violet), 530 (green) and 560 (yellow-green) nanometres; light from about 400 to 700 nanometres | L128, L129, L130 (M and L also L10, L11, L91, L92), L12, L9 |
| Dim light | a fully dark-adapted person can just see a white surface at about a millionth of a candela per square metre, about the light of an overcast starry night | L7, L8 |
| Pupil | area changes about 15-fold | L22 |
| Movement | notices motion slower than a tenth of a degree a second; picks out dots moving together when about 5 in 100 do | L15, L16 |
| Ultraviolet | the adult lens absorbs it | L102 |

Three consequences for the code:

- `HUMAN_CPD = 60` in `src/cam.a.js` is **confirmed**.
- `paramsOf` scales the picture by `180 / fov`, taking a person's field as 180 degrees. With 200, the cat (200) would draw no bending and the dog (240) less than today; the deer, rabbit and squirrel would change in proportion. I recommend 200 and leave the change to the app thread, since it touches every view.
- The hawk row says "People see flicker up to 50 or 60 times a second", where the others say "about 60"; `docs/SOURCES.md` already notes the mismatch. "About 60" is the figure to use (L13, L61). No other row in `EYES` departs from the table above, apart from the cat's 180 degrees.

### 3.4 The deeper evidence, topic by topic

**Acuity by method.** Methods disagree, and the spread is part of the evidence (Caves et al. 2018, Box 4: anatomy gives an upper limit; optomotor tests underestimate; behaviour depends on light, motion and motivation).

| Animal | Method | Value | Log |
|---|---|---|---|
| domestic cat | behavioural gratings (several studies, summarised) | 3 to 9 cycles per degree | L18 |
| domestic cat | behavioural, textbook table (Charman 1991) | 10 | L17 |
| domestic cat | behavioural gratings across the field | 3.5 at the centre; half an octave lower at 4 degrees, 1.3 octaves lower at 16 | L88, L89 |
| domestic cat | letter (optotype) recognition, two cats | 20/33 (young cat) and 20/74 (older cat, +2 D) | L19 |
| domestic cat | press summary of a 600-species compilation | about a seventh of a person's | L95 |
| domestic dog | behavioural (Snellen-equivalent), from a review | 20/45 to 20/85; 20/60 to 20/85 in Shiba dogs; typical 20/75 | L29 to L31 |
| domestic dog | evoked potentials and other methods, summarised | no better than 12.6 cycles per degree | L46 |
| domestic dog | cone density in the fovea-like patch | 25 to 46 (an upper bound, ignoring optics and convergence) | L45 |
| domestic dog | two-choice gratings, four whippets, a pug, a sheepdog | 5.5 to 19.5 in room light (pug 19.5, whippets 6.7 to 15.8); 1.8 to 3.5 near moonlight | L166 to L169 |
| cheetah | compiled value, method not stated | 23 | L94 |
| person | foveal gratings; retinal sampling; optical limit | about 60; about 60; about 70 with a 2 mm pupil | L1, L6, L5 |
| person | the dogs' two-choice gratings | 32.1 to 44.2 in room light; 5.9 to 9.9 near moonlight | L170, L171 |

Snellen fractions convert at 30 cycles per degree for 20/20, which puts the best human eyes (60) near 20/10. The app compares animals with 60, so "a tenth as well as a person" means about 6 cycles per degree.

**Streak and area centralis.** Cat: a central area with a gentle fall-off (L88, L89), S cones peaking below it (L98); the wildcat's centre is twice as rich in cones (L96). Dog: from a pronounced streak (wolf, long skulls) to a strong central area (pug), correlated with skull length and cephalic index (L36 to L38), with a cone bouquet inside the central area (L44, L47). Red fox: a central area and a moderate streak; Arctic fox: a prominent streak (L39, L42). Cheetah: a horizontal cone streak (L97). In large carnivores the central area lies within the tapetum (L150).

**Tapetum and dim light.** Cat: threshold up to about seven times lower than a person's (L80, L134), a cellular tapetum up to 15 layers thick reflecting up to 130 times more light than the human fundus (L81, L148), dark adaptation that goes on for up to an hour (L80 note), 92% of ganglion cells rod-driven in the dark (L71). Dog: tapetum full-sized in 70% of 539 dogs and absent in 2%, smaller in small breeds (L87); rods even in the central area (L119). Coyote: threshold below natural night light (L43). Lion: the largest tapetum of three felids examined (L122). The scattered light of a tapetum can soften the dim-light image (L149). People: a white surface at about a millionth of a candela per square metre (L7).

**Colour.** Cat: S near 450 and L near 550 to 556 nm, rods 501 (L69 to L72), with an unsettled 500 nm photopic mechanism; Walls's 1942 verdict of colour blindness is superseded (L147). Dog: 429 to 435 and 555 nm, rods 508 (L64 to L66, L108, L109, L116); a neutral point near 480 nm (L68); dogs answer a deuteranopia test as red-green colour-blind people do (L151). Foxes share the dog's pigments (L110 to L115). Both cats' and dogs' lenses pass ultraviolet (L100, L101).

**Flicker.** Cat 47.5 a second (L25), dog 75 to 80 (L27, L28, L85), people about 60 centrally (L13, L61) and up to about 100 at the far edge of view in very bright light (L62, L63).

**Motion.** Dogs need about 0.76 degrees a second to see motion and 42% coherent dots to see a direction (L34, L35); people under 0.1 and about 5% (L15, L16); cats roughly ten times worse than people at slow motion (L83, L136).

**Field and overlap.** Dog 240 to 250 degrees, overlap 30 to 60 by behaviour and 80 to 116 by optics (L79, L157, L32, L33); cat at least 200 and 287 by an optical measurement, with one eye seeing about 200 and the overlap 60 to 140 by method (L76, L77, L78, L144, L154 to L156); people 200 and 120, or 180 in the older figure (L57, L58, L158). On the optical figures, the cat's whole field is wider than the dog's, which reverses the popular comparison.

**The slit pupil's optics.** A slit lets a multifocal lens work at full diameter in bright light (L54), closes almost completely (L142), changes area about 135-fold against a person's 15 (L21, L22), and blurs horizontal contours more than vertical ones (L24), a distance cue that suits short ambush hunters (L23, L125).

**Breed differences in dogs.** Skull length sets the balance of streak and central area (L36), the central density varies 6,400 to 14,400 ganglion cells per mm² between dogs (L37), short-nosed dogs follow pointing better and make eye contact sooner (L105, L106), small breeds have smaller tapeta and a fair share of Labradors have none (L87), the eyelid opening turns more frontal as the skull shortens (L36 note), sighthounds such as the borzoi and greyhound hunt by sight (L153), and some breeds are often short-sighted, toy poodles above all (L165).

## 4. Species with their own measurements

- **Domestic cat** (*Felis catus*): acuity by several methods (L17, L18, L19, L88, L89), cone and rod peaks (L69 to L72), pupil range and shape (L20, L21), lens (L48), refraction and eye length (L75), flicker (L25), lens transmission of ultraviolet (L100). Enough for the `cat` view as written.
- **Domestic dog** (*Canis lupus familiaris*): acuity (L29 to L31, L46), cone and rod peaks (L65, L66, L108, L109, L116), ganglion-cell topography by breed (L36, L37), fovea-like patch (L44, L47), flicker (L27), motion thresholds (L34, L35), tapetum by breed (L87), lens ultraviolet (L101). A profile with the nose setting is ready.
- **Red fox** (*Vulpes vulpes*): pupil and lens (L51), cones (L40, L110, L111), topography (L39, L41), compass-aligned pouncing (L117). The `fox` view rests on it.
- **Arctic fox** (*Vulpes lagopus*): stronger streak and twice the red fox's central cone density (L42, L112, L113). A profile with `topoS` near 1 would follow from L42 once its acuity is read (wanted: Malkemper and Peichl 2018).
- **Wolf** (*Canis lupus*): pronounced streak and about 200,000 ganglion cells (L38), round pupil (L52). It fits `dog` with the long-nose setting fixed.
- **Cheetah** (*Acinonyx jubatus*): 23 cycles per degree (L94) and a horizontal cone streak (L97). It deserves its own setting inside `bigcat`.
- **Tiger** (*Panthera tigris*): round pupil and monofocal lens (L49), eye length (L121).
- **Lion** (*Panthera leo*): round pupil (L103), large tapetum and eye size (L122, L123).
- **Coyote** (*Canis latrans*): the second most recorded canid in the world and in Alachua, measured only for dim light (L43); everything else is borrowed from dogs and wolves.
- **Island gray fox** (*Urocyon littoralis*): cone pigments (L114, L115), standing in for the gray fox.
- **Spanish wildcat** (*Felis silvestris tartessia*): more than twice the domestic cat's cone density in the area centralis and about 70% more ganglion cells (L96). A wildcat setting inside `cat` would be sharper than the house cat once a number is found.
- **Pallas's cat** (*Otocolobus manul*): a small cat with a round pupil (L124), the one small cat that should not take the slit.

## 5. Gaps and how to fill them

| Gap | Nearest evidence | How a value could be inferred |
|---|---|---|
| Acuity of lions, tigers, leopards, pumas | tiger eye 29.4 mm against the cat's 19.75 (L121, L75); lion eyes 27 to 32 mm (L122 note); the cheetah's 23 cycles per degree (L94) | scale the cat's 8 by the eye-length ratio: about 12 (done for `bigcat`, graded `i`). The per-species values in Veilleux and Kirk's online table would replace it |
| Pupils of pumas, leopards, jaguars, cheetahs, coyotes, gray foxes **[unfinished]** | large carnivores have round pupils (L140); felid and canid trees of pupil shape (L55, L56); the 42 cm shoulder-height pattern (L23); gray fox oval (L104) | the large cats take a round pupil (`g`); the coyote takes the dog's round pupil by analogy; pending Banks et al. 2015 table S1 |
| Bobcat vision | Eurasian lynx pupil and lens (L50); S cones in the bobcat (L138) | treat *Lynx* as one genus |
| Cat field and binocular overlap **[unfinished]** | whole field 200 (L77) or 287 by optics (L154); overlap 60 by perimetry (L76), 120 or more (L144), 130 (L155) and about 140 (L78) | the rows give the ranges and the picture draws 200; the schematic-eye papers would settle the optical figures |
| Field of view of foxes, coyotes and big cats | dogs 240 (L79), cats 200 (L77) | foxes and coyotes have dog-like skulls, so 240 by analogy (`g`); the views leave the field unset until a source appears |
| Flicker in foxes, coyotes and big cats | dog 75, cat 47.5 (L27, L25); nocturnal animals average lower flicker limits than day-active ones in one compilation (Inger et al. 2014, Results) | nothing better than "like dogs" and "like cats"; no value is drawn |
| Dim-light acuity of cats and dogs **[unfinished]** | cat threshold up to 7 times lower (L80); dogs' rods in the area centralis (L119) | the night shift can borrow the human curve shifted by a factor of 7 for cats; Pasternak and Merigan (1981; no opened page gives its citation) and Neuhaus and Regenfuss (1967, wanted) measured it |
| What the tapetum does to sharpness | tapetum present and large (L81, L87, L122); Walls (1942) says its scattered light can blur the dim-light image, less so in large eyes (L149) | a small softening at night, scaled by the light level (`i`); Land and Nilsson chapter 6 (wanted) would give a figure |
| The colour matrix `DEUTAN` | the app's comment says it was entered from memory from Viénot, Brettel and Mollon (1999) | not checked here; the paper or a library that reproduces its matrices should be compared line by line. A matrix built from the cats' and dogs' own cone curves (L65, L66, L69, L70) and the camera's spectral response would be truer, and the engine track could compute it |
| A third cone in cats | 500 nm photopic mechanism (L72), a midspectral input in dark-adapted cells (L71 note) | treated as unsettled; nothing drawn |
| Fox acuity | red fox ganglion cells 7,900 per mm² (L39), dogs 6,400 to 14,400 (L37) | the `fox` view takes the typical dog's 8 (`i`); Malkemper and Peichl (2018) estimated acuity in the full text (wanted) |

## 6. Closed sources wanted

The same list as `docs/views/wanted/cat-dog.jsonl`, most useful first.

1. Banks MS, Sprague WW, Schmoll J, Parnell JAQ, Love GD 2015, *Science Advances* 1: e1500391, supplementary table S1 (species and pupil shapes). Priority 1: the pupil for pumas, cheetahs, leopards, jaguars, bobcats, coyotes and gray foxes.
2. Neuhaus W, Regenfuss E 1967, Über die Sehschärfe des Haushundes bei verschiedenen Helligkeiten, cited by Beltran et al. 2014 as *Zentralbl Vergleich Physiol* 57: 137 to 146. Priority 1: dog acuity across light levels, for the night shift.
3. Malkemper EP, Peichl L 2018, *Journal of Comparative Neurology*, doi 10.1002/cne.24493. Priority 1: acuity estimates for red and Arctic foxes, for `fox`.
4. Veilleux CC, Kirk EC 2014, *Brain, Behavior and Evolution* 83: 43 to 53, online supplementary table 1. Priority 1: acuity by species and method for the felids and canids.
5. Coile DC, Pollitz CH, Smith JC 1989, *Physiology & Behavior* 45(6): 1087 to 1092, doi 10.1016/0031-9384(89)90092-9. Priority 2: the dog's flicker limit and its light level.
6. Loop MS, Berkley MA 1975, *Vision Research* 15: 555 to 561 (cited by Inger et al. 2014, which prints the second author as Berkeley MS). Priority 2: the cat's flicker limit and method.
7. Pasternak T, Merigan WH 1980, *Journal of Comparative and Physiological Psychology* 94: 943 to 952. Priority 2: the cat's own motion threshold.
8. Clark DL, Clark RA 2013, *Experimental Eye Research* 116: 75 to 78, doi 10.1016/j.exer.2013.08.004. Priority 2: cat grating acuity against luminance.
9. Clark DL, Clark RA 2016, *Experimental Eye Research* 153: 23 to 26, doi 10.1016/j.exer.2016.10.002. Priority 2: the cat's neutral point, for the colour matrix.
10. Peichl L 1992, *Journal of Comparative Neurology*, doi 10.1002/cne.903240412. Priority 2: streak shapes by breed, for the weights of the nose setting.
11. McGreevy P, Grassi TD, Harman AM 2003, *Brain, Behavior and Evolution*, doi 10.1159/000073756. Priority 2: the breed-by-breed table.
12. Miller PE, Murphy CJ 1995, *Journal of the American Veterinary Medical Association* 207: 1623 to 1634, as cited by Byosiere et al. 2018 (the title was not shown in the part of the review that opened). Priority 2: the primary review behind the dog's field and acuity figures.
13. Odom JV, Bromberg NM, Dawson WW 1983, Canine visual acuity: retinal and cortical field potentials evoked by pattern stimulation, *American Journal of Physiology* 245: R637 to R641 (cited by Beltran et al. 2014). Priority 2: the 12.6 cycles per degree.
14. Murphy CJ, Mutti DO, Zadnik K, Ver Hoeve J 1997, Effect of optical defocus on visual acuity in dogs, *American Journal of Veterinary Research* 58: 414 to 418 (cited by Beltran et al. 2014). Priority 2: behavioural dog acuity and the cost of defocus.
15. Ahnelt PK, Schubert C, Kübber-Heiss A, Schiviz AN, Anger E 2006, *Visual Neuroscience*, doi 10.1017/s095252380623342x. Priority 2: cone maps of lion, tiger, cheetah and lynx.
16. Land MF, Nilsson D-E 2012, *Animal Eyes*, chapter 5, Lens eyes on land, doi 10.1093/acprof:oso/9780199581139.003.0005. Priority 2: pupils and lenses of land vertebrates.
17. Land MF, Nilsson D-E 2012, *Animal Eyes*, chapter 6, Mirrors in animals (the tapetum), under the book's doi 10.1093/acprof:oso/9780199581139.001.0001. Priority 2: whether a tapetum costs sharpness.
18. Land MF, Nilsson D-E 2012, *Animal Eyes*, chapter 9, Movements of the eyes, doi 10.1093/acprof:oso/9780199581139.003.0009. Priority 3: background for a gaze effect.
19. Gunter R, Harding HGW, Stiles WS 1951, Spectral reflexion factor of the cat's tapetum, *Nature*, doi 10.1038/168293a0. Priority 3: the tint of eyeshine.
20. Wells MC, Lehner PN 1978, The relative importance of the distance senses in coyote predatory behaviour, *Animal Behaviour* 26: 251 to 258, doi 10.1016/0003-3472(78)90025-8. Priority 3: how much coyotes hunt by sight.

Not on the list because no opened page gave an exact citation: Gunter's 1951 paper on the cat's absolute threshold, Vakkur and Bishop's and Hughes's schematic eyes of the cat, Pasternak and Merigan's 1981 paper on luminance and spatial vision, Hughes's and Stone's maps of ganglion cells in the cat, and Bowmaker and Dartnall (1980), which Webvision cites (L128). They are worth finding.

## 7. Sources

- Ahnelt PK, Fernández E, Martínez O, Bolea JA, Kübber-Heiss A 2000. Irregular S-cone mosaics in felid retinas. *JOSA A*. doi 10.1364/josaa.17.000580. **opened** (abstract in the collection index).
- Ahnelt PK, Schubert C, Kübber-Heiss A, Schiviz AN, Anger E 2006. Independent variation of retinal S and M cone photoreceptor topographies. *Visual Neuroscience*. doi 10.1017/s095252380623342x. **opened** (abstract in the collection index).
- Banks MS, Sprague WW, Schmoll J, Parnell JAQ, Love GD 2015. Why do animal eyes have pupils of different shapes? *Science Advances* 1: e1500391. doi 10.1126/sciadv.1500391. **opened** (eScholarship PDF and the Durham repository copy).
- Beltran WA and 13 others 2014. Canine retina has a primate fovea-like bouquet of cone photoreceptors. *PLoS ONE* 9(3): e90390. doi 10.1371/journal.pone.0090390. **opened**.
- Bognár Z, Szabó D, Deés A, Kubinyi E 2021. Shorter headed dogs ... form eye contact faster. *Scientific Reports* 11. doi 10.1038/s41598-021-88702-w. **opened** (DOAJ record with abstract).
- Byosiere S-E, Chouinard PA, Howell TJ, Bennett PC 2018. What do dogs (*Canis familiaris*) see? *Psychonomic Bulletin & Review* 25(5): 1798 to 1813. doi 10.3758/s13423-017-1404-7. **opened**; its figures from Miller and Murphy (1995), Murphy et al. (1997), Tanaka et al. (2000), Healy et al. (2013), Duke-Elder (1958) and Walls (1942) are **secondary**.
- Caves EM, Brandley NC, Johnsen S 2018. Visual acuity and the evolution of signals. *Trends in Ecology & Evolution* 33(5): 358 to 372. doi 10.1016/j.tree.2018.03.001. **opened** (owner's Drive; main text only).
- Červený J, Begall S, Koubek P, Nováková P, Burda H 2011. Directional preference may enhance hunting accuracy in foraging foxes. *Biology Letters* 7(3): 355 to 357. doi 10.1098/rsbl.2010.1145. **opened** (abstract at the Czech Academy of Sciences repository).
- Clark DL, Clark RA 2013. Optotype recognition visual acuity in the domestic cat. *Research and Reviews in Biosciences*. **opened** (abstract in the collection index).
- Crocker RA, Ringo JL, Wolbarsht ML, Wagner HG 1980. Cone contributions to cat retinal ganglion cell receptive fields. *Journal of General Physiology*. doi 10.1085/jgp.76.6.763. **opened** (abstract in the collection index).
- Douglas RH, Jeffery G 2014. The spectral transmission of ocular media suggests ultraviolet sensitivity is widespread among mammals. *Proceedings of the Royal Society B* 281: 20132995. doi 10.1098/rspb.2013.2995. **opened** (UCL Discovery PDF).
- Fernandez-Alonso M, Innes W, Read JCA 2023. Peripheral flicker fusion at high luminance: beyond the Ferry-Porter law. *Vision* 7: 26. doi 10.3390/vision7010026. **opened** (author's PDF); Hecht and Verrijp (1933) through it is **secondary**.
- Gácsi M, McGreevy P, Kara E, Miklósi Á 2009. Effects of selection for cooperation and attention in dogs. *Behavioral and Brain Functions* 5: 31. doi 10.1186/1744-9081-5-31. **opened**.
- Granar MIKS, Nilsson BR, Hamberg-Nyström HLH 2011. Normal color variations of the canine ocular fundus. *Acta Veterinaria Scandinavica* 53: 13. doi 10.1186/1751-0147-53-13. **opened**.
- Guenther E, Zrenner E 1993. The spectral sensitivity of dark- and light-adapted cat retinal ganglion cells. *Journal of Neuroscience* 13(4): 1543 to 1550. doi 10.1523/JNEUROSCI.13-04-01543.1993. **opened** (abstract).
- Horn SW, Lehner PN 1975. Scotopic sensitivity in coyotes. *Journal of Comparative and Physiological Psychology*. doi 10.1037/h0078151. **opened** (abstract in the collection index).
- Inger R, Bennie J, Davies TW, Gaston KJ 2014. Potential biological and ecological effects of flickering artificial light. *PLoS ONE* 9(5): e98631. doi 10.1371/journal.pone.0098631. **opened**; the cat, dog and human values it lists are **secondary** (Loop and Berkley 1975; Coile et al. 1989; Hecht and Verrijp 1933; Landis 1954; Sekuler and Blake 2002).
- Jacobs GH, Deegan JF, Crognale MA, Fenwick JA 1993. Photopigments of dogs and foxes and their implications for canid vision. *Visual Neuroscience*. doi 10.1017/s0952523800003291. **opened** (abstract, openpolar record).
- Kanizsár O, Mongillo P, Battaglini L, Campana G, Marinelli L 2017. Dogs are not better than humans at detecting coherent motion. *Scientific Reports*. doi 10.1038/s41598-017-11864-z. **opened** (full text on disk).
- Klećkowska-Nawrot J and 5 others 2026. Descriptive comparative morphology of the eye and ocular adnexa in Felidae. *BMC Veterinary Research*. doi 10.1186/s12917-026-05480-1. **opened** (full text on disk).
- Kolb H 2013. Photoreceptors. *Webvision*. https://www.webvision.pitt.edu/book/part-ii-anatomy-and-physiology-of-the-retina/photoreceptors/. **opened**; Bowmaker and Dartnall (1980) through it is **secondary**.
- Konrade KA and 4 others 2012. Refractive states of eyes ... in domestic cats. *American Journal of Veterinary Research*. doi 10.2460/ajvr.73.2.279. **opened** (abstract in the collection index).
- Lamm N 2013. What do cats see? https://nickolaylamm.com/art-for-clients/what-do-cats-see/. **opened** (popular article; the source of the current cat rows).
- Land MF, Nilsson D-E 2012. *Animal Eyes*, 2nd edition. Oxford University Press. doi 10.1093/acprof:oso/9780199581139.001.0001. **opened** in part (owner's Drive: chapters 1 and 2, chapter 3 to p. 65).
- Lind O, Milton I, Andersson E, Jensen P, Roth LSV 2017. High visual acuity revealed in dogs. *PLoS ONE* 12(12): e0188557. doi 10.1371/journal.pone.0188557. **opened**.
- Lõoke M, Kanizsár O, Battaglini L, Guerineau C, Mongillo P, Marinelli L 2020. Are dogs good at spotting movement? *Current Zoology* 66(6): 699 to 701. doi 10.1093/cz/zoaa044. **opened**; its cat and human figures are **secondary**.
- Malkemper EP, Peichl L 2018. Retinal photoreceptor and ganglion cell types and topographies in the red fox and Arctic fox. *Journal of Comparative Neurology*. doi 10.1002/cne.24493. **opened** (abstract in the collection index).
- Malmström T, Kröger RHH 2006. Pupil shapes and lens optics in the eyes of terrestrial vertebrates. *Journal of Experimental Biology* 209: 18 to 25. doi 10.1242/jeb.01959. **opened**.
- McGreevy P, Grassi TD, Harman AM 2003. A strong correlation exists between the distribution of retinal ganglion cells and nose length in the dog. *Brain, Behavior and Evolution*. doi 10.1159/000073756. **opened** (abstract in the collection index).
- Meshida K and 4 others 2025. Split insertions of the oblique extraocular muscles in Carnivora. *The Anatomical Record*. doi 10.1002/ar.70016. **opened** (abstract in the collection index).
- Miller PE 2001. Vision in animals: what do dogs and cats see? Waltham/OSU Symposium, Small Animal Ophthalmology. https://www.vin.com/doc/?id=3844144. **opened** (proceedings by a veterinary ophthalmologist; used as a review).
- Mowat FM and 6 others 2008. Topographical characterization of cone photoreceptors and the area centralis of the canine retina. *Molecular Vision* 14: 2518 to 2527. **opened** (abstract on the University of Wisconsin ophthalmology page).
- Neitz J, Geist T, Jacobs GH 1989. Color vision in the dog. *Visual Neuroscience* 3(2): 119 to 125. doi 10.1017/S0952523800004430. **opened** (Cambridge abstract).
- Owens CD and 4 others 2021. Keratometry, biometry, and prediction of intraocular lens power in adult tigers. *American Journal of Veterinary Research*. doi 10.2460/ajvr.21.04.0060. **opened** (abstract in the collection index).
- Pasternak T, Horn K 1991. Spatial vision of the cat: variation with eccentricity. *Visual Neuroscience* 6(2): 151 to 158. doi 10.1017/S0952523800010531. **opened** (Cambridge abstract).
- Peck CK, Barber G, Pilsecker CE, Wark RC 1980. Visual field deficits in cats reared with cyclodeviations of the eyes. *Experimental Brain Research* 41(1): 61 to 74. doi 10.1007/BF00236680. **opened** (Springer abstract).
- Peichl L 1992. Topography of ganglion cells in the dog and wolf retina. *Journal of Comparative Neurology*. doi 10.1002/cne.903240412. **opened** (abstract in the collection index).
- Schnapf JL, Kraft TW, Nunn BJ, Baylor DA 1988. Spectral sensitivity of primate photoreceptors. *Visual Neuroscience* 1(3): 255 to 261. doi 10.1017/S0952523800001917. **opened** (Cambridge abstract).
- Smith RA (Duke University) 2018. Details that look sharp to people may be blurry to their pets. Neuroscience News, 30 May 2018. https://neurosciencenews.com/blurry-animal-vision-9193/. **opened** (press summary of Caves et al. 2018).
- Spector RH 1990. Visual fields. In Walker HK, Hall WD, Hurst JW (eds), *Clinical Methods*, 3rd edition, chapter 116. https://www.ncbi.nlm.nih.gov/books/NBK220/. **opened**.
- Strasburger H, Rentschler I, Jüttner M 2011. Peripheral vision and pattern recognition: a review. *Journal of Vision* 11(5): 13. doi 10.1167/11.5.13. **opened** (Aston repository PDF).
- Timney B 1990. Effects of brief monocular deprivation on binocular depth perception in the cat. *Visual Neuroscience* 5(3): 273 to 280. doi 10.1017/S0952523800000341. **opened** (Cambridge abstract).
- Siniscalchi M, D'Ingeo S, Fornelli S, Quaranta A 2017. Are dogs red-green colour blind? doi 10.1098/rsos.170869 (the repository page does not name the journal; the DOI is a Royal Society Open Science one). **opened** (abstract, University of Bari repository).
- Vasas V and 14 others 2024. Recording animal-view videos of the natural world using a novel camera system and software package. *PLOS Biology* 22(1): e3002444. doi 10.1371/journal.pbio.3002444. **opened**.
- Veilleux CC, Kirk EC 2014. Visual acuity in mammals: effects of eye size and ecology. *Brain, Behavior and Evolution* 83: 43 to 53. doi 10.1159/000357830. **opened** (Karger PDF, main text).
- Walls GL 1942. *The vertebrate eye and its adaptive radiation*. Bloomfield Hills, Michigan: Cranbrook Institute of Science. https://archive.org/details/vertebrateeyeits00wall (Biodiversity Heritage Library scan, no known copyright restrictions). **opened** in part, through the archive's search-inside service (scan pages 194, 249, 253 to 267, 318 to 319, 529); its colour-vision verdict on cats is out of date (L147).
- Wikipedia, Gray fox (citing Alderton 1998). https://en.wikipedia.org/wiki/Gray_fox. **opened** (weak; used for one pupil line).
- Williams RW, Cavada C, Reinoso-Suárez F 1993. Rapid evolution of the visual system: the Spanish wildcat and the domestic cat. *Journal of Neuroscience*. doi 10.1523/jneurosci.13-01-00208.1993. **opened** (abstract in the collection index).
- Yang S 2015. Pupil shape linked to ecological niche. Berkeley News, 7 August 2015. https://news.berkeley.edu/2015/08/07/pupil-shape-and-ecological-niche/. **opened** (press release quoting the authors of Banks et al. 2015).
- GBIF.org occurrence and species APIs, dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7, read 13 October 2026. **opened**.

## 8. Questions for a specialist

1. Do pumas, cheetahs, leopards and jaguars have round pupils in bright light, and do coyotes and gray foxes have round or oval ones?
2. How wide is a cat's binocular overlap: about 60 degrees, as orienting perimetry suggests, or about 140?
3. At what light level does a cat's or dog's acuity overtake a person's, and by how much does each fall between daylight and moonlight?
4. Does the tapetum's second pass of light cost sharpness or contrast enough to see?
5. Is the cat's 500 nm photopic mechanism a third cone, and should the cat's colour drawing allow for it?
6. What acuity do the eye sizes and ganglion-cell densities of lions, tigers and red foxes predict?
