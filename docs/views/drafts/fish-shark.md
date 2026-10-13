# Sensing sheet: fish, and sharks and rays (unit `fish-shark`), draft

Started 13 October 2026 at 01:47 UTC (21:47 EDT on 12 October). The evidence log is `docs/views/evidence/fish-shark.jsonl`, cited below as "log N" for its line N, and the wanted list is `docs/views/wanted/fish-shark.jsonl`. This sheet builds on `docs/views/sheets/fish.md` and its audit, and goes further where the two disagree.

**Where the reading came from.** The literature collection (`pub/lit-t1`, topics `fish` and `sharks-rays`: 8,034 works, 677 full texts) was read on disk first. From the owner's library, Land and Nilsson's *Animal Eyes* (2nd edition, 2012) came through only in part: the front matter, chapters 1 and 2 (light and vision, including light in water, colour and polarization) and chapter 3 up to p. 66. Chapters 4 to 9, among them "Aquatic eyes: the evolution of the lens", did not come through. On the web, Europe PMC refused with HTTP 429 at 01:53 UTC and was not used again; PubMed failed to fetch; the Journal of Experimental Biology's pages asked for a robot check; GBIF's API and Crossref were refused by this machine's network policy for direct requests, and GBIF answered through the fetch tool for six family lookups. Abstracts quoted as "collection index" are the OpenAlex abstracts stored in the collection, which the brief counts as opened.

## 1. Scope

**Taxa.** The unit covers every fish: ray-finned fish, lampreys, hagfish, lungfish and the coelacanth (the app's group `fish`), and sharks, rays, skates and chimaeras (the group `shark`). Together they hold 2,763,409 iNaturalist research-grade records in GBIF, read on 11 October 2026 (`docs/views/world-orders.csv`).

**What people photograph.**

- **Worldwide**, the largest families are the sunfish and black bass (Centrarchidae, 188,208 records), the carp and minnows (Cyprinidae, 186,903), wrasses (176,484), damselfish (155,557), gobies (85,468) and butterflyfish (85,395), from the earlier sheet and the family facets saved on the `ci` branch (`runs/fetch/10`). The Bluegill is the most recorded species of the largest order (46,903 records).
- **Sharks** hold 60,349 records and **rays** 70,277, so rays outnumber sharks. Chimaeras hold 1,769. Galeomorph sharks (requiem sharks, hammerheads, mackerel sharks, carpet sharks, bullhead sharks) hold 57,428 of the shark records (95.2%).
- **In Alachua County**, the 60 fish species on the county list hold 1,028 records, all of fish that live in fresh water or come into it from the coast. Sunfish hold 319 records (31.0%) and the livebearers 309 (30.1%): the Eastern Mosquitofish (197, the most recorded fish in the county), the Variable Platyfish (42), the Sailfin Molly (37) and the Least Killifish (33). Then come bullhead catfish (58), minnows (57), gars (56, nearly all Florida Gar), topminnows (43), the Brown Hoplo (35), cichlids (31), darters (30) and the Ruddy Bowfin (25). The county list holds no shark or ray.

**Where the views should split.** One picture would be false for large shares of these records along three lines.

1. **Sharks against rays.** Every shark studied has one kind of cone, so a shark sees no colour (logs 19, 20). Most rays have two cone classes and some have told colours apart in tests (logs 18, 26, 139), while skates have rods only (log 27). The eyes also face differently: rays share a view overhead and some see the whole circle (logs 94, 95), and their electric sense crowds the underside around the mouth (logs 46, 131). Rays flicker slower than sharks (logs 122 to 125). **Line: by order.** `shark` takes the eight shark orders (60,349 records, 2.2% of fish records). `ray` takes the rays, skates and chimaeras (72,046 records, 2.6%).
2. **Fresh water against the sea.** The light differs more than any eye does. Tea-coloured lakes soak up blue and leave red light, and the darkest leave only a small patch of red light overhead (logs 71, 72); clear water turns blue with depth, and sea water removes red within 10 to 20 metres (logs 4, 72, 132). The eyes follow the water: freshwater fish shift their pigments toward red, often with vitamin A2 (logs 79, 114, 142), while reef fish carry ultraviolet and blue cones and little red sensitivity (logs 62, 108, 110). Reef fish also include the families whose two eyes move independently, each with a fovea (logs 74, 75), which no freshwater minnow, catfish, gar or salmon has. **Line: by family, by the habitat where the family's records are made.** With the families and orders classified as below, `fish` takes 747,083 records (27.0% of fish records) and the new view `reef` takes 1,591,771 (57.6%). Groups with members in both waters hold 149,470 records (5.4%: scorpionfish and sculpins, sticklebacks, silversides, smelts, milkfish, sleepers, grunters), and smaller perch-order families not yet looked up hold 142,690 (5.2%); both need a species-level habitat flag, which the full database can carry. In Alachua the rule puts 997 records (97.0%) with `fish` and 27 with `reef`, and 18 of those 27 are wrong: the gizzard and threadfin shads live in Florida's fresh water, so the herring family needs that flag too. The other nine (six Hogchokers, a mullet, a needlefish and a burrfish) are coastal fish that enter rivers.
3. **Colour inside `fish`.** Sunfish and bass have two cone types and none for blue or ultraviolet (logs 80 to 83), and a study of six sunfish species found their eyes change little between light habitats (log 92). Minnows, carp, livebearers and gars have four or more cone classes including ultraviolet (logs 31 to 35, 76, 77, 112, 114). Sunfish hold 25.2% of `fish` records worldwide and 31.0% in Alachua, and the livebearers alone hold 30.1% in Alachua, so one colour setting would be false for a third of the county's fish either way. **Line: a colour setting per family**, chosen when the recognizer or the full database names the fish: `sunfish` for Centrarchidae (188,208 records), and the four-colour default for the rest.

The classification used for the shares: freshwater orders Cypriniformes, Salmoniformes, Cyprinodontiformes, Esociformes, Lepisosteiformes, Characiformes, Amiiformes, Acipenseriformes, Osteoglossiformes, Percopsiformes, Synbranchiformes, Gymnotiformes, Polypteriformes, the lampreys and the lungfish; the catfish except the sea catfish (Ariidae) and eel catfish (Plotosidae); the freshwater eels (Anguillidae); and the perch-order families Centrarchidae, Percidae, Cichlidae, Channidae and Elassomatidae. Everything else that was classified is marine, chiefly 47 perch-order families of reefs and coasts and the orders of pufferfish, seahorses, flatfish, morays, squirrelfish and herrings. Salmon, trout and sturgeon are counted as freshwater although many spend years at sea, and the killifish family includes salt-marsh species. The family counts come from the facet saved on `ci`, joined to its names file, which covers only the first 3,000 of 17,449 animal families; nine more family keys were read from GBIF's name matcher on 13 October, the sunfish key came from the earlier sheet, and four more were matched by their record counts.

**Recommendation: four views.**

| View | Holds | Records | Share of fish records |
|---|---|---:|---:|
| `fish` (freshwater fish) | ray-finned fish of fresh water, lampreys, lungfish; colour setting `sunfish` for Centrarchidae | 747,083 | 27.0% |
| `reef` (sea fish) | ray-finned fish of the sea, hagfish, the coelacanth; setting `hagfish` | 1,591,771 | 57.6% |
| mixed and unassigned | assigned by species habitat once named | 292,160 | 10.6% |
| `shark` | sharks | 60,349 | 2.2% |
| `ray` | rays, skates, chimaeras; setting `skate` | 72,046 | 2.6% |

The keys `fish` and `shark` already exist in `GROUPS` in `src/cam.a.js`. `reef` and `ray` would be new groups for the recognizer; until the group head learns them, `reef` can be chosen from the named family and `ray` from the named order. The boring alternative, one `fish` view and one `shark` view as in the earlier sheet, is simpler and would draw a two-colour, tea-tinted picture for every damselfish, and a grey picture for every stingray that has shown colour vision in tests.

## 2. The view `fish` (freshwater fish)

`chip: 'Freshwater fish'`, `who: 'a freshwater fish'`. The rows below are shown for every freshwater fish except where a setting replaces one.

### Rows

1. `['m', 'Colour of a sunfish', 'Largemouth bass have two kinds of colour-sensing cells, tuned to green and to red, and none for blue or ultraviolet. Trained bass mistook blue for black and chartreuse yellow for white. For a sunfish or bass, this view turns blues dark and yellows pale.']`
   Logs 80, 81, 82, 83 (Mitchem et al. 2019); log 92 (Bertinetti 2025) for drawing the Bluegill and other sunfish the same way. Shown in the `sunfish` setting only.
2. `['g', 'Colour of other freshwater fish', 'Minnows, carp and livebearers such as the mosquitofish have four or more kinds of colour-sensing cells, and one kind senses ultraviolet light, which people cannot see. For these fish, this view keeps your camera’s colours and adds a faint violet sheen for ultraviolet, which is the app’s own invention.']`
   Logs 114 (zebrafish cones at 365, 416, 483 and 574 nm), 112 (guppy cone classes from 359 to 560 nm), 31 to 35 (mosquitofish opsin genes, predicted from sequence), 76 and 77 (spotted gar). Shown in the default setting.
3. `['m', 'Sharpness', 'A bluegill sees about a twelfth as much detail as you do, and a largemouth bass about a twentieth. This view blurs the picture to match.']`
   Logs 84 (Bluegill, about 5 cycles per degree by behaviour), 38 (bass, 3.0 by anatomy). 5/60 and 3/60.
4. `['m', 'Sharpest spot', 'A white crappie, a kind of sunfish, has its densest patch of cone cells in the part of the eye that looks forward, drawn out along the horizon, and it starts most attacks on prey within 40 degrees of straight ahead. This view is sharpest in the middle and along the horizon.']`
   Logs 40, 41 (Browman et al. 2008); log 89 (the Golden Shiner's sharp area also looks forward).
5. `['g', 'Field of view', 'A golden shiner, a common minnow, takes in about 335 degrees around itself, and its two eyes overlap for about 31 degrees in front. A phone camera sees far less, so this view squeezes the picture and bends its edges to suggest the wider sweep.']`
   Logs 86, 87 (Pita et al. 2015).
6. `['g', 'Tea-coloured water', 'Rain washes tannins from swamps into many Florida lakes and stains them the colour of tea. Tea-coloured water soaks up blue light and leaves red, and in the darkest water almost the only light left comes from a small patch overhead. This view tints the picture amber and darkens it below and toward the edges.']`
   Logs 71 (Florida LAKEWATCH), 72 (Marques et al. 2017).
7. `['g', 'Eyes tuned toward red', 'Many freshwater fish shift their eyes toward red light by building their light-sensing pigments from vitamin A2 in place of vitamin A1. A minnow called the common shiner uses far more A2 in winter than in summer. This view leans toward red in the cooler months.']`
   Logs 79 (Cui et al. 2026), 142 (Allen et al. 1982: 17% in summer, 68% in winter), 114 (A2 in zebrafish cones).
8. `['g', 'Looking up', 'Under a calm surface, a fish sees the whole sky squeezed into a bright circle about 97 degrees across, straight overhead. Beyond the circle, the underside of the surface works like a mirror and reflects the water below. When you tilt the phone upward, this view draws the circle.']`
   Logs 69 (Sabbah et al. 2006), 70 (total internal reflection beyond 48.6 degrees, OpenStax; the mirror seen from below is the direct consequence, noted in the log).
9. `['g', 'Pace', 'Bony fish follow a flickering light up to about 46 flashes a second on average, a little below the roughly 60 at which a flickering light looks steady to you. This view keeps your pace.']`
   Log 68 (Inger et al. 2014, ray-finned fish).
10. `['x', 'Moving water', 'Rows of sensors along a fish’s head and body, called the lateral line, feel the flow and pressure of moving water within one or two body lengths. Fish use them to find prey in the dark and in murky water and to keep their places in a school. The picture leaves this sense out.']`
    Logs 48 (Scott et al. 2023), 49 (Schwalbe et al. 2012), 50, 51 (yellow perch and ruffe in the dark).
11. `['x', 'Hearing', 'Minnows, carp and catfish have small bones that link the swim bladder to the inner ear, which gives them keen hearing, and a goldfish hears best between about 350 and 1,500 vibrations a second. The picture leaves sound out.']`
    Log 119 (Ladich and Fay 2013).
12. `['x', 'Electric fields', 'Catfish and lampreys can sense the faint electric fields that living animals make in water. The picture leaves this sense out.']`
    Logs 59 (Alves-Gomes 2001), 52 (Bodznick and Northcutt 1981).

A lamprey row for a later `lamprey` setting: `['g', 'Colour of a lamprey', 'Lampreys have one or two kinds of colour-sensing cells, and the southern lamprey has two, tuned near 515 and 613 nanometres. This view shows a lamprey fewer colours than other fish.']` Logs 57, 58 (Collin et al. 2003; the other lampreys it names have one cone or none). Lampreys hold 1,863 records.

### The picture

| Field | Value | Behind it |
|---|---|---|
| `fov` | 335 | Log 86. The engine shrinks the camera picture to 180/335 = 0.54 and bends the edges for the rest. |
| `cpd` | 4 | Logs 84 (5), 38 (3.0), 88 (2.86, Golden Shiner, anatomical). The value inside the range is `invented`. Acuity follows eye size (log 140), so a later version could scale `cpd` with the fish's size where the full database knows it. |
| `topoA` | 1 | Logs 40, 89: a forward-looking area. |
| `topoS` | .5 | Log 40: the crappie's area is drawn out along the horizontal meridian. The mix of the two weights is `invented`. |
| `fall` | 1.4 | Log 88: the shiner's edge is 2.86/1.18 = 2.4 times coarser than its peak, which is `fall` 1.4 in the engine's convention (blur times 1 + `fall` at half the frame height). |
| `pupil` | 'o' | Log 104: the iris of most teleosts does not move. The round shape is `invented`. |
| `dof` | 8 | Log 104: an eye that always works wide open has a shallow depth of field. The strength is `invented`, and log 8 (focus by moving the lens) means the tap-to-focus control fits. |
| `M` (`sunfish`) | [1, 0, 0, 0, 1, 0, 0, 1, 0] | Logs 80 to 83. Read by rows, the blue channel takes the green signal, so pure blue goes black and yellow goes white, the two confusions the trained bass made. The matrix is `invented`. |
| `M` (default) | identity, `sheen` .5 | Logs 112, 114. The violet sheen is `invented`. |
| `sat` | 1 | Nothing measured calls for a change. |
| `gain` | 1 | No dim-light measurement in a freshwater fish was opened. |
| `rate` | 1 | Log 68: the measured mean (46) sits below 60, and slowing the picture would claim the opposite. Keeping the person's pace is `invented`. |
| `persist` | 0 | 1/46 = 0.02 seconds of trail, too short to see. |
| water | amber, see below | Logs 71, 72. |

```
fish: { chip: 'Freshwater fish', who: 'a freshwater fish', fov: 335, cpd: 4, topoA: 1, topoS: .5, fall: 1.4, pupil: 'o', dof: 8, sheen: .5,
  cue: 'Detail is coarse, the field is wide, and the water is the colour of tea. Tilt the phone up to see the sky as a fish does.', rows: [ /* above */ ] }
// setting sunfish (Centrarchidae): M: [1, 0, 0, 0, 1, 0, 0, 1, 0], sheen: 0, row 1 in place of row 2
```

### New effects the evidence calls for

1. **Water colour by distance (tea-coloured fresh water).** What the person sees: near things keep their colours, and farther things turn amber, then brown, then dark, with the sides and the lower part of the frame darker than the top (log 72: in blackwater the light from the sides and below is absorbed and red light comes from a small patch above). Phone input: the engine's existing guess that lower in the frame is closer, or a depth estimate from the camera where it is affordable. Drawing: the standard picture of light in water, with each colour channel multiplied by exp(−k d) and a little of the water's own colour added back as haze; k is small for red and large for blue in fresh tea-coloured water (log 72), and the opposite in the sea (logs 4, 132). The k values are `invented` until a measured spectrum of a Florida lake is found (wanted list). Cost: one multiply and one mix per pixel with a depth value already at hand; cheap. What makes it beautiful: tea water glows warm near the surface, and the darkening toward the bottom is the real reason a tannic lake looks bottomless.
2. **Snell's window when the phone looks up.** What the person sees: tilting the phone toward the sky squeezes the whole scene above into a bright disc about 97 degrees across, its rim crowded and stretched, and outside the disc the picture shows a mirror image of the lower part of the frame (logs 69, 70). Phone input: the orientation sensor for tilt (behind the engine's permission flag); the camera for the scene. The camera's roughly 70 degree field fills only the central 51 degrees of the disc (arcsin(sin 35° / 1.33) = 25.5°, doubled), so the rim is stretched from the frame's edges, as the wide field is today. Cost: one remapping pass and a tilt reading; moderate. Beauty: the disc is the single most recognizable sight of being under water.
3. **Seasonal shift for minnows.** What the person sees: the default setting leans slightly toward red in winter months, read from the phone's date (log 142). Cost: one number in the colour matrix per month; trivial. The size of the shift is `invented`; the direction is measured in one minnow.
4. **Lateral line ripples.** What the person sees: when something moves close to the phone, a soft pressure ripple runs along the edge of the screen on that side, fading with distance, as the lateral line feels flow within one or two body lengths (logs 48, 49). Phone input: the engine's motion-salience map, with large, near motion (big image motion low in the frame) standing in for a nearby swimmer; the phone's own movement removed with the motion sensors. Cost: moderate, since the salience map is already planned. The mapping from image motion to water flow is `invented` and the row stays `x` until it is drawn.
5. **Hearing for minnows, carp and catfish.** The microphone, with consent asked in plain words, could pulse the picture's edges with sound between about 350 and 1,500 Hz, the goldfish's best band (log 119). Cost: low once the engine's microphone input exists. Sound in air is a poor stand-in for sound in water, so this would be graded `i`.

## 3. The view `reef` (sea fish)

`chip: 'Sea fish'`, `who: 'a sea fish'`.

### Rows

1. `['m', 'Colour', 'Damselfish, the family of the clownfish, have four kinds of colour-sensing cells, one of them for ultraviolet light, and many wear ultraviolet patterns that they show one another. A triggerfish has three kinds, tuned to violet, blue and green. Neither has a cell tuned to red, so this view darkens reds and adds an invented violet sheen for ultraviolet.']`
   Logs 110 (Ambon damselfish cones at 365, 485, 504 and 526 nm), 62 (all 50-plus damselfish species studied), 108, 109 (Picasso triggerfish, 412, 480 and 528 nm), 64 (an anemonefish in the damselfish family).
2. `['g', 'Red light fades', 'Sea water swallows red light within the first 10 to 20 metres, so deeper down a red fish looks dark grey and a reef turns blue-green. This view tints the picture blue-green and fades reds with distance.']`
   Logs 132 (Gerlach et al. 2014), 134 (Michiels et al. 2008), 4 (blue light travels farthest).
3. `['m', 'Sharpness', 'Small reef fish see coarsely. An Ambon damselfish and a dottyback resolved about a fortieth as much detail as you do, though the cells in their eyes are packed tightly enough for about three times more. This view blurs the picture to match.']`
   Logs 90, 91 (Parker et al. 2017: 1.29 to 1.71 cycles per degree by behaviour, 3.2 to 4.6 by anatomy); 1.5/60 = 1/40.
4. `['m', 'Fine detail without blue', 'A damselfish sees fine patterns only through its cells for longer wavelengths, so a pattern that differs only in blue is a blur to it, even though it can tell the blue from the green. This view blurs the blue part of the picture more than the rest.']`
   Log 111 (Siebeck et al. 2014).
5. `['m', 'Eyes that move apart', 'Wrasses, blennies, pufferfish, triggerfish and seahorses can turn each eye on its own, and each eye has a small sharp centre, called a fovea. One eye can follow a passing fish while the other searches the reef. This view gives each half of the screen its own sharp spot, and the two wander separately.']`
   Logs 74, 75 (Hofmann and Gebhardt 2023). These groups hold over 460,000 records (wrasses 176,484, pufferfish and triggerfish 180,531, blennies 54,088, seahorses and pipefish 51,732).
6. `['m', 'Pace', 'A squirrelfish, a reef fish that hunts at night, follows a flickering light up to 70 flashes a second in bright light, faster than you can, and only about 40 at night. This view runs slightly slow in daylight and then jumps ahead to catch up.']`
   Log 65 (Fogg et al. 2023); log 66 (a cardinalfish, 42 by day).
7. `['g', 'Looking up', 'Under a calm surface, a fish sees the whole sky squeezed into a bright circle about 97 degrees across, straight overhead. Beyond the circle, the underside of the surface works like a mirror and reflects the water below. When you tilt the phone upward, this view draws the circle.']`
   Logs 69, 70.
8. `['x', 'Polarized light', 'Young anemonefish can steer by polarized light, light whose waves vibrate mostly at one angle, which people cannot see. In the sea the light is seldom polarized strongly enough to make it a reliable guide. The picture leaves it out.']`
   Log 64 (Berenshtein et al. 2014); log 121 (Hawryshyn 2010, mostly in salmon and trout).
9. `['x', 'Moving water', 'Rows of sensors along a fish’s head and body, called the lateral line, feel the flow and pressure of moving water within one or two body lengths. The picture leaves this sense out.']`
   Logs 48, 49.

Row for the `hagfish` setting (110 records): `['m', 'Hagfish', 'A hagfish’s eyes have no lens, and they probably tell it only how much light there is. For a hagfish, this view shows no picture, only the amount, colour and direction of the light.']` Logs 54 (Dong and Allison 2021), 55 (Collin et al. 2009).

### The picture

| Field | Value | Behind it |
|---|---|---|
| `fov` | 335 | `invented`, copied from the Golden Shiner (log 86); no reef fish field was opened. |
| `cpd` | 2 | Logs 90, 91: 1.3 to 1.7 by behaviour in small reef fish, 3.2 to 4.6 by anatomy. Larger reef fish have larger eyes and likely see more (log 140). The value is `invented` within the range. |
| `topoA` | 1 | Log 75: foveae in many reef groups. |
| `fall` | 1.6 | `invented`. A fovea is a sharper, smaller spot than an area. |
| `pupil` | 'o' | Log 104. Shape `invented`. |
| `M` | [.35, 0, 0, 0, 1, 0, 0, 0, 1] | Logs 108, 110: no cone beyond about 530 nm, so reds go dark. The matrix is `invented`. |
| `sheen` | .6 | Logs 62, 110. `invented`. |
| `rate` | .86 | Log 65: 60/70. A fish that is fast by day is slow at night; switching `rate` to 1 after dusk by the phone's clock would follow logs 65 and 66. |
| `field` (`hagfish`) | 1, `sat` .3 | Logs 54, 55. |
| water | blue-green, see section 2 effect 1 | Logs 4, 132. |

```
reef: { chip: 'Sea fish', who: 'a sea fish', fov: 335, cpd: 2, topoA: 1, fall: 1.6, pupil: 'o', M: [.35, 0, 0, 0, 1, 0, 0, 0, 1], sheen: .6, rate: .86,
  cue: 'Reds fade to grey, the water is blue, and each eye looks its own way.', rows: [ /* above */ ] }
// setting hagfish (Myxiniformes): field: 1, sat: .3, pupil: 'none', rows: the hagfish row only, with the looking-up and moving-water rows
```

### New effects the evidence calls for

1. **Two eyes, two gazes.** What the person sees: the left and right halves of the screen each carry a small sharp spot that drifts and jumps on its own, each drawn to movement on its side and each avoiding its last target for a while, so the two halves rarely look at the same thing (logs 74, 75). Phone input: the camera, through the engine's planned salience map and gaze controller, run twice with a separate inhibition mask per half. Cost: moderate, since it reuses the jumping spider's gaze machinery. Beauty: a person sees for the first time what it is to watch two places at once. The pattern of the drifting is `invented`; independence itself is measured.
2. **Blue loses its detail.** What the person sees: blue patterns soften while light-and-dark edges stay crisp (log 111). Drawing: blur the blue channel by a wider kernel than red and green, or blur the colour difference while keeping luminance sharp. Cost: one extra blur of one channel; low.
3. **Red fluorescence at depth.** As the water layer removes red with distance, a few reef fish keep a red glow (logs 133, 134). The app cannot know which fish fluoresce, so this stays a proposal for a later species profile, for fairy wrasses first.
4. **Day and night pace.** The phone's clock switches `rate` from .86 by day to 1 at night, following the squirrelfish's slower night vision (log 65). Trivial.

## 4. The view `shark`

`chip: 'Shark'`, `who: 'a shark'`.

### Rows

1. `['m', 'Colour', 'Every shark studied so far has only one kind of colour-sensing cell, so sharks are probably colour blind. They can tell apart shades of brightness that differ by less than 2 percent. This view shows the world in shades of grey.']`
   Logs 19, 20 (Hart et al. 2025), 17 (a bamboo shark learned shapes, not colours), 25 (brightness steps, from Ryan et al. 2017 as cited).
2. `['m', 'Sharpness', 'Sharks see between a twentieth and a sixth as much detail as you do. Fast hunters of open water, like the bigeye thresher, are at the sharp end, and bottom-dwelling night hunters, like the Port Jackson shark, are at the coarse end. This view uses the middle of that range.']`
   Logs 24, 97 (2.0 to 10.6 cycles per degree), 101 (Port Jackson shark, 3.14), 11 (young white shark, about 5).
3. `['m', 'Sharpest band', 'Many sharks, such as the lemon shark, see most sharply along a band level with the horizon, which lets them scan the sea floor or the open water without moving their eyes. White sharks have a sharp patch that looks up and to the sides, toward prey seen against the bright surface. This view sharpens a band along the horizon.']`
   Logs 103 (lemon shark), 102 (Port Jackson shark), 98, 13, 14 (white shark).
4. `['m', 'Pace', 'Sharks follow a flickering light up to 16 to 31 flashes a second, a quarter to a half of your rate, so quick movement smears for them. This view leaves trails behind anything that moves.']`
   Logs 122, 123 (bonnethead 31, blacknose shark 16), 12, 126, 67 (mean of cartilaginous fish 26.1).
5. `['m', 'Two eyes', 'A shark’s eyes sit on the sides of its head, and in a lemon shark the two fields overlap by only about 10 degrees in front. A winghead hammerhead, whose head is very wide, overlaps by 48 degrees, and hammerheads swing their heads from side to side as they swim. This view bends the edges of the picture to suggest the wide sweep.']`
   Log 93 (McComb et al. 2009).
6. `['g', 'Dim light', 'Many sharks have a mirror-like layer behind the retina, called a tapetum, which sends light back through the eye for a second chance to be caught, and in some sharks dark pigment slides over it in bright light. This view lifts the shadows a little.']`
   Logs 106 (McFarland 1990), 107 (Heath 1990).
7. `['x', 'Electric sense', 'Sharks feel the faint electric fields around living animals through gel-filled pores on the snout, called the ampullae of Lorenzini. A young hammerhead turns toward a prey-like field from about 30 centimetres away, even when the field is weaker than a billionth of a volt across a centimetre. The picture leaves this sense out.']`
   Logs 127 (Kajiura and Holland 2002), 47 (pores around the mouth and snout), 128 (Kalmijn 1971), 131.
8. `['x', 'Smell first', 'A hunting shark usually smells its prey first and follows the scent upstream, then turns to sight, the lateral line, the electric sense and touch as it closes in. The picture leaves smell out.']`
   Log 117 (Gardiner et al. 2014).

### The picture

| Field | Value | Behind it |
|---|---|---|
| `fov` | 300 | Log 93: laterally placed eyes with small overlaps. The total field was not opened, so the value is `invented`. |
| `cpd` | 5 | Logs 11, 24, 97. |
| `topoS` | 1 | Logs 98, 102, 103: horizontal streaks. |
| `fall` | 1.5 | `invented`. |
| `pupil` | 'o' | Log 105: shark pupils vary in shape. A per-species shape is a later step; the round default is `invented`. |
| `M` | [0, 1, 0, 0, 1, 0, 0, 1, 0] | Logs 19, 20; log 141 (Ryan et al. 2021 modelled a white shark's view from the camera's green channel alone). Every channel takes green, so the picture is grey. |
| `gain` | 1.3 | Logs 106, 107. The amount is `invented`. |
| `persist` | .04 | Log 67: 1/26.1 = 0.038 seconds; the measured range 16 to 31 Hz gives .03 to .06 (logs 122, 123). |

```
shark: { chip: 'Shark', who: 'a shark', fov: 300, cpd: 5, topoS: 1, fall: 1.5, pupil: 'o', M: [0, 1, 0, 0, 1, 0, 0, 1, 0], gain: 1.3, persist: .04,
  cue: 'There is no colour, only light and dark, and movement leaves trails.', rows: [ /* above */ ] }
```

### New effects the evidence calls for

1. **The electric field at close range, as an invented glow.** What the person sees: within the bottom third of the frame (the engine's stand-in for "close"), things that move like living animals take on a faint shimmering outline that brightens as the phone comes nearer, standing for fields a shark feels within about 30 to 40 centimetres (logs 44, 127). Phone input: none senses electric fields; the planned salience map's living-motion cue stands in. Cost: moderate. It must be graded `i` in a row of its own if drawn, and the row should say plainly that the glow is the app's invention.
2. **The head sweep.** A slow side-to-side drift of the picture of about 15 degrees each way, as hammerheads and other sharks swing their heads while swimming (log 93). Phone input: none needed; the motion sensors could stop the drift while the person turns the phone. Cost: low. The rhythm is `invented`.
3. **Smell first.** The view could open on a blank, slowly moving field that resolves into the picture as the person approaches something, following the hunting order in log 117. This is a way of arriving at the view, and it needs the owner's word on whether a view may change over time like this.

## 5. The view `ray` (rays, skates and chimaeras)

`chip: 'Ray, skate'`, `who: 'a ray'`.

### Rows

1. `['m', 'Colour', 'Most rays, such as stingrays and shovelnose rays, have two or three kinds of colour-sensing cells, and some have told colours apart in tests. Skates have only rods, the cells for dim light, and see in shades of grey. This view shows two colours for a ray and grey for a skate.']`
   Logs 26 (Hart et al. 2025), 139 (Hart et al. 2004, three cone pigments in two shovelnose rays), 18, 16 (freshwater stingray), 27 (skates).
2. `['m', 'All around', 'A yellow stingray sees all the way around itself in a flat circle, and a cownose ray sees all the way from above to below. Rays share a view between both eyes ahead and overhead. This view squeezes the whole circle into the screen.']`
   Logs 94, 95 (McComb and Kajiura 2008).
3. `['m', 'Sharpness', 'A freshwater stingray resolved only about a three-hundredth as much detail as you see in tests. This view is heavily blurred.']`
   Log 15 (Daniel et al. 2020: under 0.13 to 0.23 cycles per degree; 0.2/60 = 1/300).
4. `['m', 'Sharpest band', 'Skates and some stingrays see most sharply along a horizontal band. This view sharpens a band across the middle of the picture.']`
   Logs 100 (little skate), 98 (blue-spotted ribbontail ray).
5. `['m', 'Pace', 'A yellow stingray follows a flickering light only about 12 times a second in cool water and 25 in warm water, and a skate’s eye follows only 5 in dim light. This view leaves long trails behind anything that moves.']`
   Logs 124 (a meeting abstract), 125 (Green and Siegel 1975).
6. `['x', 'Electric sense', 'A ray feels the faint electric fields of animals buried in sand through pores on the underside of its head, around its mouth, where they are about five times as dense as on top. Sawfish and shovelnose rays respond to fields of a few billionths of a volt across a centimetre. The picture leaves this sense out.']`
   Logs 46, 131 (Wueringer 2012), 43 (5 to 80 nV/cm), 128 (Kalmijn 1971, a ray finding a buried flatfish).
7. `['x', 'Hearing', 'Rays and skates hear through the movement of the water itself, since they have no swim bladder, and the little skate hears best at 100 to 200 vibrations a second. The picture leaves sound out.']`
   Log 120 (Ladich and Fay 2013).

### The picture

| Field | Value | Behind it |
|---|---|---|
| `fov` | 360 | Log 94. The engine clamps the squeeze at 0.5 (180/360). |
| `cpd` | .2 | Log 15. |
| `topoS` | 1 | Logs 98, 100. |
| `fall` | 1 | `invented`. |
| `pupil` | 'o' | `invented`; ray pupils were not opened. |
| `M` | the existing `DEUTAN` matrix | Logs 26, 139: two cone classes. Using a two-cone human simulation as a stand-in is `invented`, and its colour axis is a guess. |
| `persist` | .08 | Log 124: 1/12 = 0.083 seconds. |
| `skate` setting | `sat` 0, `persist` .2 | Logs 27, 125 (5 Hz in dim light). |
| chimaeras | the ray settings | Log 28: the elephant shark expresses three cone opsins; chimaeras ride with rays, `invented`. |

```
ray: { chip: 'Ray, skate', who: 'a ray', fov: 360, cpd: .2, topoS: 1, fall: 1, pupil: 'o', M: DEUTAN, persist: .08,
  cue: 'You see almost the whole circle, softly, and movement leaves long trails.', rows: [ /* above */ ] }
// setting skate (Rajiformes): sat: 0, persist: .2
```

### New effects the evidence calls for

1. **The electric underside.** What the person sees: the lowest band of the screen, where a ray's mouth and densest pores face the sand (logs 46, 131), dims to near black, and anything moving there glows faintly as it would through the electric sense. Phone input: the salience map for motion; the tilt sensor to keep the band on the ground side. Cost: moderate. The glow is `invented` and would need its own `i` row.
2. **Warm and cool water.** The yellow stingray's flicker rate doubles from cool to warm water (log 124). The app cannot read water temperature; the season from the phone's date could stand in, `invented`.

## 6. The earlier sheet re-checked

The views proposed here are new, and no `EYES` entry exists for fish, so this section re-checks the earlier sheet's numbers against what was opened in this session.

- Bluegill about 5 cycles per degree, cone spacing 3.4 to 6.7, contrast 3% at 0.4: **confirmed** (logs 84, 85).
- Pumpkinseed 3.6 cycles per degree (Spratte et al. 2021): **not re-opened** (the journal page asked for a robot check); left out of the rows.
- Largemouth bass cones at 535 and 614 nm, no short-wavelength cones, the two confusions: **confirmed** (logs 80 to 83).
- Golden Shiner field 335 degrees, overlap 31, peak 2.86 and edge 1.18 cycles per degree, area looking forward and up: **confirmed** (logs 86 to 89).
- Spiny damselfish flicker 89 Hz (Chung et al. 2014): **not re-opened** (the repository page gives no figure, and the journal page asked for a robot check); replaced by the squirrelfish's 70 Hz (log 65) and put on the wanted list.
- Bony fish 45.9 Hz and cartilaginous fish 26.1 Hz: **confirmed** (logs 67, 68).
- Snell's window about 97 degrees: **confirmed** (log 69). The mirror outside the window, removed by the audit, is restored on the strength of total internal reflection beyond the critical angle (log 70).
- Lateral line from Zhai and colleagues' arXiv review: **replaced** by primary and review statements on cichlids and perch (logs 48 to 51).
- Sharks with one cone type: **confirmed and extended** (logs 19 to 23, 30, 42); the earlier "7 species with cones and 10 without" rested on a press release and is not used.
- Shovelnose ray cones at 477, 502, 561 and 459, 492, 553 nm: **confirmed** (log 139).
- Parker et al. 2017 reef sharpness, with the second fish a dottyback: **confirmed** (logs 90, 91).
- Clownfish ultraviolet cones (Mitchell et al. 2024) and goldfish ultraviolet cones (Joselevitch et al. 2010): **not re-opened**; the ultraviolet rows now rest on the damselfish family (log 62), the Ambon damselfish (log 110), the zebrafish (log 114) and the guppy (log 112).
- The earlier sheet's 10% share for sharks and rays together is **corrected** into two views, since rays outnumber sharks and see differently.

## 7. Species with their own measurements

- **Largemouth Bass** (*Micropterus salmoides*, the county's Florida Bass): cones, colour confusions, anatomical acuity, near point (logs 37 to 39, 80 to 83).
- **Bluegill** (*Lepomis macrochirus*): acuity and contrast (logs 84, 85). Its cones are unmeasured (section 8).
- **White Crappie** (*Pomoxis annularis*): sharp area and pursuit angles (logs 40, 41).
- **Golden Shiner** (*Notemigonus crysoleucas*, 21 Alachua records): field, overlap, acuity, sharp area (logs 86 to 89).
- **Goldfish** (*Carassius auratus*): behavioural acuity 7.1 cycles per degree and hearing (logs 1, 119).
- **Guppy** and **Western Mosquitofish**: cone classes and opsin genes (logs 31 to 36, 112, 113), the route to an Eastern Mosquitofish profile.
- **Ambon Damselfish** (*Pomacentrus amboinensis*): four cones, acuity, blue-blind fine vision (logs 90, 110, 111).
- **Picasso Triggerfish** (*Rhinecanthus aculeatus*): three cones, colour thresholds (logs 108, 109).
- **White Shark**: acuity, sharp area, hunting distance (logs 11, 13, 14, 141).
- **Bonnethead**: flicker, hunting sequence (logs 117, 122).
- **Scalloped Hammerhead** and other hammerheads: visual overlap, electric threshold (logs 93, 127).
- **Port Jackson Shark**: streak, acuity, rod-dominated retina (logs 101, 102).
- **Yellow Stingray**: full horizontal field, flicker with temperature (logs 94, 124).
- **Little Skate**: streak, electric cells (logs 100, 118).
- **Greenland Shark**: rods only (log 137).

## 8. Gaps and how to fill them

- **Bluegill cones.** No opened source measures them. Nearest relative: the largemouth bass in the same family (logs 80 to 83), and six sunfish species whose eyes vary little with habitat (log 92). Inference: draw sunfish as two-cone, graded `g`.
- **Mosquitofish sharpness and field.** None found. Nearest: the guppy (same family) through Caves et al. 2021 on the swordtail (wanted list), and acuity scaling with eye size (log 140). Inference: a small livebearer resolves less than a sunfish; the default `cpd` of 4 is likely too sharp for it.
- **Florida Gar.** Pigments only, from the spotted gar in vitro (logs 76, 77). The spotted gar retina paper (wanted list) would give cone types and topography.
- **Catfish sight.** No acuity or cone data for bullhead catfish were opened. They have electroreceptors (log 59) and many catfish have a reflecting tapetum (log 60). Nothing is known here about bullhead vision.
- **Freshwater flicker.** No sunfish or minnow flicker rate was opened; the view uses the ray-finned mean (log 68).
- **Reef fish fields of view.** None opened; `fov` is copied from the Golden Shiner.
- **Spectra of Florida waters.** No opened source gives the light spectrum under a tea-coloured Florida lake; the water effect's colour constants are invented until one is found.
- **Shark fields.** The hammerhead paper's full text (log 93, abstract only) gives monocular and total fields.
- **Ray pupils.** Not opened; the round pupil is invented.
- **Polarization in fish.** How a vertebrate cone could read polarization is disputed (logs 7, 121); nothing is drawn.

## 9. Closed sources wanted

The same list as `docs/views/wanted/fish-shark.jsonl`, most useful first (priority 1 would change a view's picture, 2 would confirm or correct a row, 3 is background).

1. (1) Bertinetti C, Mosley C, Jones S, Torres-Dowdall J 2025. Robust sensory traits across light habitats: visual signals but not receptors vary in centrarchids inhabiting distinct photic environments. Molecular Ecology. doi:10.1111/mec.17721. Would give the cone opsins of six sunfish, settling whether the Bluegill shares the bass's two-cone colour.
2. (1) Ryan LA, Hemmi JM, Collin SP, Hart NS 2017. Electrophysiological measures of temporal resolution, contrast sensitivity and spatial resolving power in sharks. Journal of Comparative Physiology A. doi:10.1007/s00359-017-1154-z. Measures flicker, contrast and acuity in the same sharks by one method, which would set the shark view's trails and blur together.
3. (1) Siebeck UE, Marshall NJ 2001. Ocular media transmission of coral reef fish: can coral reef fish see ultraviolet light?. Vision Research. doi:10.1016/s0042-6989(00)00240-6. Would show which reef families' lenses pass ultraviolet, deciding where the reef view's ultraviolet sheen belongs.
4. (1) Chung W-S, Marshall NJ, Watson S-A, Munday PL, Nilsson GE 2014. Ocean acidification slows retinal function in a damselfish through interference with GABAA receptors. Journal of Experimental Biology 217: 323-326. doi:10.1242/jeb.092478. Holds the damselfish flicker value used by the earlier sheet (89 Hz), which would set the reef view's pace for a diurnal reef fish.
5. (1) McComb DM, Tricas TC, Kajiura SM 2009. Enhanced visual fields in hammerhead sharks. Journal of Experimental Biology. doi:10.1242/jeb.032615. The full text gives monocular and total visual fields of five sharks, replacing the shark view's invented field of 300 degrees.
6. (2) Sukeena JM, Galicia CA, Wilson JD, McGinn T, Boughman JW, Robison BD, Postlethwait JH, Braasch I, Stenkamp DL, Fuerst PG 2016. Characterization and evolution of the spotted gar retina. Journal of Experimental Zoology Part B: Molecular and Developmental Evolution. doi:10.1002/jez.b.22710. Would give cone types and retinal layout for gars (56 Alachua records), now drawn from pigments expressed in a dish.
7. (2) McComb DM, Kajiura SM 2008. Visual fields of four batoid fishes: a comparative study. Journal of Experimental Biology. doi:10.1242/jeb.014506. The full text gives the vertical fields and blind areas of four rays, for placing the ray view's sharp band and dark underside.
8. (2) Caves EM, de Busserolles F, Kelley LA 2021. Sex differences in behavioural and anatomical estimates of visual acuity in the green swordtail, Xiphophorus helleri. Journal of Experimental Biology. doi:10.1242/jeb.243420. Acuity in a livebearer, the nearest measured relative of the Eastern Mosquitofish, the county's most recorded fish.
9. (2) Foster TN, Williamson AG, Foster BR, Toomey MB 2025. Light environment and seasonal variation in the visual system of the red shiner (Cyprinella lutrensis). Journal of Experimental Biology. doi:10.1242/jeb.249878. Would size the seasonal red shift proposed for minnows, now known from one 1982 shiner study.
10. (2) Horváth G, Varjú D 1995. Underwater refraction-polarization patterns of skylight perceived by aquatic animals through Snell's window of the flat water surface. Vision Research. doi:10.1016/0042-6989(94)00254-j. Would give the geometry and appearance of Snell's window and the surface outside it as an aquatic animal sees them, for drawing the looking-up effect.
11. (2) Litherland L, Collin SP, Fritsches KA 2009. Visual optics and ecomorphology of the growing shark eye: a comparison between deep and shallow water species. Journal of Experimental Biology. doi:10.1242/jeb.028589. Describes pupil movement and the tapetum in the sandbar shark, which would replace the shark view's invented pupil and dim-light lift.
12. (2) Jinson ST, Liebich J, Senft SL, Mäthger LM 2018. Retinal specializations and visual ecology in an animal with an extremely elaborate pupil shape: the little skate Leucoraja (Raja) erinacea. Journal of Comparative Neurology. doi:10.1002/cne.24465. Would give the skate's pupil shape and how it shapes blur, for the ray view's pupil.
13. (2) Kalinoski M, Hirons A, Horodysky AZ, Brill RW 2014. Spectral sensitivity, luminous sensitivity, and temporal resolution of the visual systems in three sympatric temperate coastal shark species. Journal of Comparative Physiology A. doi:10.1007/s00359-014-0950-y. More shark flicker and dim-light values for the shark view's trails and shadows.
14. (3) Kamermans M, Hawryshyn CW 2011. Teleost polarization vision: how it might work and what it might be good for. Philosophical Transactions of the Royal Society B. doi:10.1098/rstb.2010.0211. Review of how fish might read polarized light, for deciding whether any fish view should show it.
15. (3) Hawryshyn CW, Moyer HD, Allison WT, Haimberger TJ, McFarland WN 2003. Multidimensional polarization sensitivity in damselfishes. Journal of Comparative Physiology A. doi:10.1007/s00359-003-0392-4. Polarization sensitivity in adult damselfish, the largest reef family with measured eyes.
16. (3) Ladich F 2015. Peripheral hearing structures in fishes: diversity and sensitivity of catfishes and cichlids. Advances in Experimental Medicine and Biology. doi:10.1007/978-3-319-21059-9_15. Hearing ranges of catfish for the freshwater view's hearing row and microphone effect.
17. (3) Dreyfert T, Holmberg K, Struwe G 1979. Critical flicker fusion frequency of the river lamprey (Lampetra fluviatilis). Vision Research. doi:10.1016/0042-6989(79)90140-8. A lamprey's flicker rate, for a later lamprey setting.
18. (3) Fernholm B, Holmberg K 1975. The eyes in three genera of hagfish (Eptatretus, Paramyxine and Myxine): a case of degenerative evolution. Vision Research. doi:10.1016/0042-6989(75)90215-1. Confirms what hagfish eyes can detect, for the hagfish setting.
19. (3) Watt MJ, Evans CS, Joss JMP 1999. Use of electroreception during foraging by the Australian lungfish. Animal Behaviour. doi:10.1006/anbe.1999.1216. Electric sense in lungfish, which ride along with the freshwater view.

## 10. Sources

Opened in this session, one line each (`opened` means the paper, its abstract on a publisher or repository page, or its abstract in the collection index):

- Land MF, Nilsson D-E 2012. Animal Eyes, 2nd edition. Oxford University Press. Chapters 1, 2 and part of 3. `opened` (owner's library)
- Ryan LA et al. 2021. J R Soc Interface. doi:10.1098/rsif.2021.0533. `opened`
- Daniel MMM et al. 2020. J Comp Physiol A 207: 43-58. doi:10.1007/s00359-020-01454-2. `opened`
- Hart NS et al. 2025. Mol Biol Evol. doi:10.1093/molbev/msaf043. `opened`
- Chang C-H et al. 2020. PLoS ONE. doi:10.1371/journal.pone.0240313. `opened`
- Kawamura G, Kishimoto T 2002. Fisheries Science. doi:10.1046/j.1444-2906.2002.00530.x. `opened` (abstract)
- Browman HI et al. 2008. Brain Behav Evol. doi:10.1159/000115858. `opened` (abstract)
- Wueringer BE et al. 2012. PLoS ONE 7: e41605. doi:10.1371/journal.pone.0041605. `opened`
- Winther-Janson M et al. 2012. PLoS ONE. doi:10.1371/journal.pone.0049857. `opened`
- Scott E et al. 2023. R Soc Open Sci. doi:10.1098/rsos.221478. `opened`
- Schwalbe MAB et al. 2012. J Exp Biol 215: 2060-2071. doi:10.1242/jeb.065920. `opened` (repository PDF)
- Janssen J 1997. J Fish Biol. doi:10.1006/jfbi.1997.0496. `opened` (abstract)
- Bodznick D, Northcutt RG 1981. Science. doi:10.1126/science.7209544. `opened` (abstract)
- Peach MB, Marshall NJ 2000. Phil Trans R Soc B. doi:10.1098/rstb.2000.0653. `opened` (abstract)
- Dong E, Allison WT 2021. Proc R Soc B. doi:10.1098/rspb.2020.2187. `opened` (abstract)
- Collin SP et al. 2009. Phil Trans R Soc B. doi:10.1098/rstb.2009.0099. `opened` (abstract)
- Collin SP et al. 2003. Visual Neuroscience. doi:10.1017/s0952523803202030. `opened` (abstract)
- Alves-Gomes J 2001. J Fish Biol. doi:10.1006/jfbi.2001.1625. `opened` (abstract)
- Ito S et al. 1975. Proc R Soc B. doi:10.1098/rspb.1975.0134. `opened` (abstract)
- Nicol JAC et al. 1973. Can J Zool. doi:10.1139/z73-012. `opened` (abstract)
- Stieb SM et al. 2024. Ecol Evol. doi:10.1002/ece3.11186. `opened`
- Berenshtein I et al. 2014. PLoS ONE. doi:10.1371/journal.pone.0088468. `opened`
- Fogg LG et al. 2023. Proc R Soc B. doi:10.1098/rspb.2023.1749. `opened`
- Inger R et al. 2014. PLoS ONE 9: e98631. doi:10.1371/journal.pone.0098631. `opened`
- Sabbah S et al. 2006. J Opt Soc Am A 23(8). https://arago.elte.hu/sites/default/files/SnellPol_JOSAA.pdf. `opened`
- Ling SJ, Sanny J, Moebs W. University Physics Volume 3, section 1.4. OpenStax. `opened`
- Florida LAKEWATCH 2013. Newsletter volume 62, "Why is my lake turning dark?". `opened`
- Marques DA et al. 2017. PLoS Biol. doi:10.1371/journal.pbio.2001627. `opened`
- Hofmann MH, Gebhardt IC 2023. Visual Neuroscience. doi:10.1017/s0952523823000020. `opened`
- Cui Y et al. 2026. Evolution Letters. doi:10.1093/evlett/qrag006. `opened`
- Mitchem LD et al. 2019. Current Zoology 65: 43-52. doi:10.1093/cz/zoy019. `opened`
- Northmore DPM et al. 2007. Visual Neuroscience 24: 319-331. doi:10.1017/S0952523807070307. `opened` (abstract)
- Pita D et al. 2015. PeerJ 3: e1113. doi:10.7717/peerj.1113. `opened`
- Parker AN et al. 2017. J Exp Biol 220: 2387-2396. doi:10.1242/jeb.149575. `opened`
- Bertinetti C 2025. PhD dissertation, University of Notre Dame. `opened` (abstract)
- McComb DM et al. 2009. J Exp Biol. doi:10.1242/jeb.032615. `opened` (abstract)
- McComb DM, Kajiura SM 2008. J Exp Biol. doi:10.1242/jeb.014506. `opened` (abstract)
- Litherland L, Collin SP 2008. Visual Neuroscience. doi:10.1017/s0952523808080693. `opened` (abstract)
- Lisney TJ, Collin SP 2008. Brain Behav Evol. doi:10.1159/000146082. `opened` (abstract)
- Lisney TJ et al. 2012. J Fish Biol. doi:10.1111/j.1095-8649.2012.03253.x. `opened` (abstract)
- Mäthger LM et al. 2020. J Comp Neurol. doi:10.1002/cne.25014. `opened` (abstract)
- Peel LR et al. 2020. J Comp Neurol. doi:10.1002/cne.24911. `opened` (abstract)
- Hueter RE 1990. J Exp Zool. doi:10.1002/jez.1402560518. `opened` (abstract)
- Sivak JG 1990. J Exp Zool. doi:10.1002/jez.1402560504. `opened` (abstract)
- McFarland WN 1990. J Exp Zool. doi:10.1002/jez.1402560503. `opened` (abstract)
- Heath AR 1990. J Exp Zool. doi:10.1002/jez.1402560507. `opened` (abstract)
- Champ CM et al. 2016. R Soc Open Sci. doi:10.1098/rsos.160399. `opened`
- Green NF et al. 2022. J Exp Biol. doi:10.1242/jeb.243533. `opened`
- Siebeck UE et al. 2014. Front Neural Circuits. doi:10.3389/fncir.2014.00118. `opened`
- Sandkam BA et al. 2018. Current Zoology. doi:10.1093/cz/zoy047. `opened`
- Endeman D et al. 2013. PLoS ONE 8: e68540. doi:10.1371/journal.pone.0068540. `opened`
- Yoshimatsu T et al. 2020. Neuron. doi:10.1016/j.neuron.2020.04.021. `opened`
- Tappeiner C et al. 2012. Front Zool 9: 10. doi:10.1186/1742-9994-9-10. `opened`
- Gardiner JM et al. 2014. PLoS ONE 9: e93036. doi:10.1371/journal.pone.0093036. `opened`
- Bellono NW et al. 2018. Nature. doi:10.1038/s41586-018-0160-9. `opened`
- Ladich F, Fay RR 2013. Rev Fish Biol Fish 23: 317-364. doi:10.1007/s11160-012-9297-z. `opened`
- Hawryshyn CW 2010. Brain Behav Evol. doi:10.1159/000314275. `opened` (abstract)
- McComb DM et al. 2010. Physiol Biochem Zool. doi:10.1086/648394. `opened` (abstract)
- Bedore CN et al. 2013. Meeting abstract, SICB. https://nsuworks.nova.edu/occ_facpresentations/142. `opened`
- Green DG, Siegel IM 1975. Science. doi:10.1126/science.1215989. `opened` (abstract)
- Kalinoski M 2010. MS thesis, Nova Southeastern University. https://nsuworks.nova.edu/occ_stuetd/215. `opened` (abstract)
- Kajiura SM, Holland KN 2002. J Exp Biol. doi:10.1242/jeb.205.23.3609. `opened` (abstract)
- Kalmijn AJ 1971. J Exp Biol. doi:10.1242/jeb.55.2.371. `opened` (abstract)
- Montgomery JC, Bodznick D 1999. J Exp Biol. doi:10.1242/jeb.202.10.1349. `opened` (abstract)
- Kempster RM et al. 2012. J Fish Biol. doi:10.1111/j.1095-8649.2011.03214.x. `opened` (abstract)
- Wueringer BE 2012. Brain Behav Evol. doi:10.1159/000339873. `opened` (abstract)
- Gerlach T et al. 2014. Proc R Soc B. doi:10.1098/rspb.2014.0787. `opened`
- Michiels NK et al. 2008. BMC Ecol. doi:10.1186/1472-6785-8-16. `opened`
- Lupše N et al. 2021. Mol Biol Evol. doi:10.1093/molbev/msab281. `opened`
- Claes JM et al. 2014. PLoS ONE. doi:10.1371/journal.pone.0104213. `opened`
- Fogg LG et al. 2026. Nat Commun. doi:10.1038/s41467-025-67429-6. `opened`
- Bottaro M 2022. Sci Rep. doi:10.1038/s41598-022-14076-2. `opened`
- Hart NS et al. 2004. J Exp Biol 207: 4587-4594. doi:10.1242/jeb.01314. `opened` (journal page)
- Caves EM et al. 2017. J Exp Biol 220: 1586-1596. doi:10.1242/jeb.151183. `opened` (abstract)
- Allen DM et al. 1982. Can J Zool. doi:10.1139/z82-037. `opened` (abstract)
- GBIF occurrence facets (iNaturalist research-grade dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7), saved on `ci` in `runs/fetch/10` (read 11 October 2026), and GBIF species matches for nine families read 13 October 2026. `opened`

## 11. Questions for a specialist

1. Does the Bluegill share the largemouth bass's two cones at 535 and 614 nm, or does it keep a blue or ultraviolet cone?
2. Rays show three cone pigments by microspectrophotometry (Hart et al. 2004) but two cone opsin classes by later molecular work (Hart et al. 2025). Which should a picture follow, two colours or three?
3. Is the order of habitats a fair line for fish vision, or would the tannin and turbidity of the water a fish lives in today predict its eyes better than its family does?
4. How should tea-coloured water be drawn: what spectral attenuation would a Florida lake at 40 to 100 platinum-cobalt units give per metre, from red to blue?
5. Do the independent eye movements of wrasses, pufferfish and seahorses come with any measure of how often the two eyes look at different targets, so that the two-gaze effect could follow real timing?
6. For sharks, which measure of flicker best stands for daylight vision in open water, given values from 16 to 31 Hz across species and strong effects of temperature?

## Status

Draft written at about 02:40 UTC on 13 October 2026, with 142 log lines. Still to do: the wanted list file, a style check of every row, and further reading where time allows (catfish, lampreys, deep-sea fish, the remaining abstracts in the collection).
