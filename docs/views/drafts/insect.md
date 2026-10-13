# Sensing sheet: insects other than bees and wasps (`insect`), draft

Started 13 October 2026, 01:46 UTC, by a research agent working to `docs/views/research/BRIEF.md`. This sheet re-checks the view `insect` in `src/cam.a.js` (build 22) against `docs/SOURCES.md` and the primary literature, and proposes where it should split. The evidence log is `docs/views/evidence/insect.jsonl` (cited below as `L` and a line number) and the wanted list is `docs/views/wanted/insect.jsonl`.

**What was read.** The literature collection on `pub/lit-t1` (topics butterflies-moths, flies, dragonflies, beetles-bugs-others, insects-general: titles, abstracts and full texts). Three papers from the owner's library: van der Kooi et al. 2021 (read in full, its Table 1 parsed row by row), Land 1997 (read in full, both tables), and Land and Nilsson 2012, of which only the front matter, chapters 1 and 2 and chapter 3 to page 65 came through; chapters 4 to 9, which hold the compound eye and eye movement chapters, did not (wanted list, first entry). Open pages read through the web tool: Inger et al. 2014 (PLoS ONE), the Duke University summary of Caves et al. 2018, Nakagawa and Eguchi 1994 and Buck 1990 as OCR text of their Biodiversity Heritage Library scans, the authors' copy of Land and Chittka 2013, and three abstract pages (Traniello 1977, Altner and Thies 1976, ter Hofstede and Ratcliffe 2016).

**Style note.** The rows use "lens" only in its literal sense, for the lenses of compound eyes.

**What could not be reached.** The shell's egress proxy refuses api.gbif.org, the iNaturalist open-data bucket, Europe PMC, PubMed, PMC and the publisher sites; GBIF family names were read through the web tool. Europe PMC answered the web tool with HTTP 429 (rate limited) on the abstract of Chatterjee et al. 2020, and no further request went to it. PMC and BioOne answered with robot checks, and the Carleton thesis server with a robots refusal.

## 1. Scope

### What the view covers today

`insect` is the eyes given to every insect except bees and wasps (`tools/world/groups.py`, `tools/species/eyes.py`): all insect orders but Hymenoptera, plus the ant family Formicidae and the springtails and their relatives (Collembola, Protura, Diplura), which `docs/COVERAGE.md` moved here on 12 October.

World records are iNaturalist research-grade records in GBIF read on 11 October 2026 (`runs/fetch/10/world-order.json` and `world-family-top.json` on the `ci` branch; order counts as in `docs/views/world-orders.csv`). Family names for the keys that run did not name were read from GBIF's species API on 13 October. The view covers 37,379,165 world records: 36,613,620 in insect orders other than Hymenoptera, 674,113 ants and 91,432 springtails, diplurans and proturans. Alachua figures are the `n` of `data/regions/us-fl-alachua/species.json`: 55,801 records in 2,679 species with insect eyes, plus 53 springtail records.

| Group | World records | Share of the view | Largest families (world) | Alachua records | Most recorded in Alachua |
|---|---:|---:|---|---:|---|
| Butterflies (Papilionoidea, skippers included) | 8,742,940 | 23.4% | Nymphalidae 4,407,751; Lycaenidae 1,330,784; Hesperiidae 1,120,084; Pieridae 974,969; Papilionidae 862,188 | 10,360 | Gulf Fritillary 1,057; Monarch 714; Common Buckeye 582; Zebra Longwing 491 |
| Moths (all other Lepidoptera) | 10,768,912 | 28.8% | Erebidae 2,142,693; Noctuidae 2,028,294; Geometridae 2,020,890; Crambidae 1,051,630; Sphingidae 633,706 | 20,972 | Live Oak Tussock Moth 578; Luna Moth 437; Waterlily Leafcutter Moth 374; Giant Leopard Moth 342 |
| Dragonflies and damselflies (Odonata) | 3,479,477 | 9.3% | Libellulidae 1,808,866; Coenagrionidae 782,136; Aeshnidae 230,830; Calopterygidae 170,928 | 4,960 | Eastern Pondhawk 1,056; Blue Dasher 846; Ebony Jewelwing 293 |
| Flies (Diptera) | 2,302,468 | 6.2% | Syrphidae 1,028,269 (44.7% of flies); Cecidomyiidae 142,972; Asilidae 125,080; Bombyliidae 98,431 | 2,437 | Common Lovebug 342; Grallipeza nebulosa 115; Black Horse Fly 109 |
| Ants (Formicidae) | 674,113 | 1.8% | | 1,779 | Florida Carpenter Ant 337; Graceful Twig Ant 252; Red Imported Fire Ant 230 |
| Mantises (Mantodea) | 318,481 | 0.9% | Mantidae 251,177 | 294 | Grizzled Mantis 156; American Grass Mantis 74 |
| Springtails, diplurans, proturans | 91,432 | 0.2% | Entomobryomorpha 43,589 and Symphypleona 42,401 (orders) | 53 | Dicyrtomina ornata 14 |
| Everything else | 11,001,342 | 29.4% | Coleoptera 5,702,967 (Coccinellidae 1,226,095, Cerambycidae 700,385, Scarabaeidae 687,423, Chrysomelidae 591,270, Lampyridae 69,018); Hemiptera 3,273,147 (Pentatomidae 659,918); Orthoptera 1,382,598 (Acrididae 673,086, Tettigoniidae 422,603); Blattodea 148,727; Neuroptera 145,795; Phasmida 70,356 | 14,946 | Asian Lady Beetle 786; North American Wheel Bug 447; Southern Two-striped Walkingstick 438; Florida Lubber 436 |

Within Odonata, dragonflies (Anisoptera) hold 65.6% of records and damselflies (Zygoptera) 34.3%. Moths outnumber butterflies in both counts: 55% of the world's Lepidoptera records and 67% of Alachua's. Records count what people photograph; they understate night insects and overstate large, slow, colourful ones.

### Where the view should split

The evidence finds eight places where one picture is false for a large share of the members. Each line follows a taxon the app already knows from the taxonomy (`groups.py` reads order and family), so each can become a group in the pocket model's head; the head can be refitted on these labels from the photos already in `pub/data-world`.

1. **Butterflies from moths (Lepidoptera, by superfamily Papilionoidea).** Butterflies fly by day with apposition eyes (L290) and many carry four to fifteen kinds of colour-sensing cell, red ones included (L4, L5, L7, L30, L60, L387); the Japanese Yellow Swallowtail follows flicker to 107 Hz (L393). Most moths fly at night with superposition eyes ten to a thousand times as sensitive (L288), three receptor classes and no red one (L355, L66 to L97), colour vision kept into starlight (L356, L363, L364) and vision that pools over space and time as light fails (L358, L361, L362). One picture cannot be both. Skippers (Hesperiidae) are butterflies with superposition eyes (L369, L370); they stay with butterflies because they fly by day, and a skipper profile is listed in section 4. Day-flying moths (hawkmoths such as *Macroglossum*, wasp moths) stay with moths; the moth picture follows the light level, so in daylight it sharpens and speeds up as theirs do (L361, L371).
2. **Dragonflies and damselflies (Odonata) from the rest.** Their upper eye carries the finest acuity measured in insects, in bands and zones the rest of the view lacks (L234, L235, L272, L274, L335, L336), with eye regions tuned to different colours (L346), four or five receptor classes with red (L101 to L105, L115 to L129) and neurons that select and follow a single small target (L340 to L344). Damselflies share the order's receptor plan (L125 to L129, L351) and frontal acute zones (L239); they stay in this view, with a damselfly profile later if Bybee et al. 2012 (wanted) shows a difference.
3. **Flies (Diptera) from the rest.** Neural superposition eyes (L187), the fastest photoreceptors measured (L317, L322, L380, L381) and a gaze held still between saccades (L382 to L384). Hoverflies, 44.7% of fly records, share all three (L261, L384, L167 to L169).
4. **Ants (Formicidae) from the rest.** Worker ants see far coarser than other insects (L401, L268), most with two receptor classes (L406, L219 to L225), and walk by a sky compass and stored skyline views (L398 to L402, L407, L469). They moved from `bee` to `insect` on 12 October; they belong in neither.
5. **Mantises (Mantodea) from the rest.** Stereopsis that works only on movement (L409 to L411), a frontal acute zone shared by both eyes (L243, L277) and a strike range of a few centimetres (L412).
6. **Springtails (Collembola, with Diplura and Protura) from the rest.** At most eight ommatidia a side, each tens of degrees across (L451, L233): no image at all in the sense the other views draw. Diplurans and proturans have no compound eyes (L451).
7. **Everything else stays as `insect`:** beetles, true bugs, grasshoppers, crickets and katydids, cockroaches and termites, stick insects, earwigs, lacewings, mayflies, caddisflies and the small orders. Their measured eyes share the common insect plan: apposition or open-rhabdom eyes, acuity of 0.07 to 0.56 cycles per degree (L240 to L242, L244 to L252), three receptor classes for ultraviolet, blue and green in most (L1, L136 to L144, L146 to L154), and pace near or a little above a person's (L318, L319). Beetles vary in colour: the blue class was lost and regained several times (L189, L438), and the most photographed families appear to have a short-wavelength class back (seven-spot ladybird 360, 420, 520 nm, L190 to L192). That diversity is a per-family colour setting, given when the full database names the species; it does not justify a beetle view of its own on present evidence.
8. **Fireflies (Lampyridae) as a variant inside `insect`,** applied when the full database names a lampyrid: a flash dialogue on a two-second clock (L456), eyes tuned to the species' own flash colour (L216, L208, L209, L215) and superposition optics (L247). Fireflies hold 0.18% of the view's world records and 6 Alachua records, which is too few to fit as a group of their own.

**Commitment: eight views,** `butterfly`, `moth`, `dragonfly`, `fly`, `ant`, `mantis`, `springtail` and `insect` (the remainder), with a `firefly` variant of `insect`. Shares of the present view's world records: 23.4%, 28.8%, 9.3%, 6.2%, 1.8%, 0.9%, 0.2% and 29.4%. In Alachua: 18.6%, 37.6%, 8.9%, 4.4%, 3.2%, 0.5%, 0.1% and 26.8%. Seven new groups enter the pocket model's head (7 KB at 1,024 bytes a group, by the arithmetic of `docs/COVERAGE.md`). Bees and wasps keep `bee`, which is outside this unit.

**Splits considered and not made.**

- *Caterpillars from adult Lepidoptera, by life stage.* Caterpillars see with stemmata, six a side in the saturniid Malpighi described (L457), single-lens eyes of varied design (L458); the swallowtail larva has three receptor classes (L459 to L461). A caterpillar view would be as different from a moth's as the springtail's is from a beetle's. Many records of Alachua's most recorded moths, such as tent caterpillar moths and the Live Oak Tussock Moth, are probably photos of larvae; this sheet could not count them, because iNaturalist's life-stage annotations sit behind its API. If a count shows caterpillars are a large share, a `caterpillar` view needs a life-stage label in the head's photos, which iNaturalist's annotation field can supply.
- *Crickets and katydids from grasshoppers.* They hear songs and bat calls from 2 to 40 kHz (L424, L425), within a phone microphone's band, which makes a hearing overlay possible (section 2.8). Their vision differs little from the remainder's in the log (L142 to L144, L283), so the split waits for the overlay.
- *Cockroaches.* They have two receptor classes and slow, sensitive eyes (L131 to L133, L319, L447); 0.4% of the view. A family setting suffices.

## 2. The proposed views

Grades in rows follow the brief. Each row is followed by the log lines behind it. In the picture tables, *invented* marks a value that is the app's own choice; a value with a log line is drawn from that measurement as the note says.

**A note on sharpness that applies to every view below.** `cam.b.js` blurs by 0.6 of one cycle at the eye's limit, measured against a screen taken to fill 24 degrees of the viewer's sight on a phone (`VIEW_DEG`, `docs/SOURCES.md`). For insects, whose acuity lies below 1 cycle per degree, this rule draws them three to five times blurrier than they see the scene in front of the camera, because the camera's picture spans about 70 degrees of the world (the figure `docs/SOURCES.md` uses) and the wide-field compression shrinks it further. At 0.4 cycles per degree the blur radius is 6% of the screen's long side against the viewer and about 1.2% against the scene; for an ant at 0.09 it is 28% against 5%. Drawn against the scene, a butterfly's picture would hold about 28 cycles across the camera's field, which is the honest count, and it would still look strongly blurred. This sheet recommends drawing every view with acuity below 2 cycles per degree against the scene. The values below are acuities; the convention that turns them into pixels is the owner's decision.

### 2.1 `butterfly` (Papilionoidea)

**Rows**

- `['m', 'Sharpness', 'A butterfly sees between a hundredth and a two-hundredth as much detail as a person does. Each of the many small lenses in its eyes takes in a patch of the world a degree or two across, roughly the width of a fingernail held at arm’s length. This view is blurred to match.']`
  Log: L253 (Old World Swallowtail 0.9 degrees), L255 (Large White 1.8), L254 (Common Brown 1.4 to 2.6), L375 (about a degree per pixel in day insects), L312 (fingernail).
- `['m', 'Colour', 'Many butterflies have more kinds of colour-sensing cells than people do. People have three; a monarch has three and a filter that lets it tell reds from oranges, many swallowtails, whites and blues have four to eight, and the Common Bluebottle of Asia has fifteen. Your camera records only three, so this view can’t show the extra colours.']`
  Log: L11, L386, L387 (monarch), L60 (a blue, 4), L30 (Small White, 6), L7 (Japanese Yellow Swallowtail, 8), L5 (Common Bluebottle, 15).
- `['m', 'Red', 'Most insects see red poorly, and many butterflies see it well. Swallowtails, whites and blues have colour-sensing cells tuned to red, and brush-footed butterflies such as the monarch compare red with green using filters in the eye. This view keeps reds red.']`
  Log: L1, L36 to L40, L24 to L29, L56 to L59, L387, L386, L64.
- `['m', 'Ultraviolet', 'Butterflies see ultraviolet light, which people can’t, and many have wing patterns that show only in ultraviolet. A male yellow sulphur butterfly carries bright ultraviolet patches at the base of its forewings that a person cannot see.']`
  Log: L8, L12, L24, L36 (ultraviolet classes in four families), L474.
- `['i', 'How ultraviolet is shown', 'Phone cameras record very little ultraviolet light, so this view guesses where it would be from blue and pale surfaces and tints those places violet. This part of the view is the app’s own choice.']`
  Log: none; the drawing is invented, as `docs/SOURCES.md` records for the present view.
- `['g', 'Speed', 'The colour-sensing cells of a Japanese Yellow Swallowtail follow a light that flickers up to about 107 times a second, where people stop at about 60. This view runs slowly and then jumps ahead to suggest the difference.']`
  Log: L393 to L397. Graded `g`: one species stands for all butterflies.
- `['m', 'Colour in every point', 'In a butterfly’s eye, cells for several colours sit together and share the same view, so a butterfly can see the colour of a speck as small as one point of its vision. Japanese Yellow Swallowtails picked out a red dot only about a degree across.']`
  Log: L2, L374.
- `['m', 'Sharpest regions', 'Butterflies, like bees and grasshoppers, see most sharply straight ahead and along a band level with the horizon. This view keeps the centre and the horizon a little sharper than the rest.']`
  Log: L284.
- `['m', 'Spotting a mate', 'A perched male Empress Leilia butterfly notices a passing butterfly only when it flies within about 3 metres.']`
  Log: L471, L472.
- `['x', 'Magnetic sense', 'Monarchs also sense the tilt of the Earth’s magnetic field, with light-sensing proteins in their antennae and eyes, and use it to hold a course. This view leaves that sense out.']`
  Log: L390.

**The picture**

| Field | Value | Behind it |
|---|---|---|
| `fov` | 320 | invented; no butterfly field of view was found (nearest: fruit fly about 310, L450; cockroach 360, L452). Rutowski and Warrant 2002 (wanted) would set it |
| `cpd` | 0.4 | L253 (0.56), L255 (0.28), L254 (0.36 to 0.19) |
| `topoA`, `topoS`, `fall` | 0.5, 0.5, 0.8 | pattern from L284; the numbers are invented |
| `pupil`, `dof` | 'none', 0 | L313: no insect focuses, so nothing is out of focus |
| `M` | identity | butterflies see red (L4, L387); the camera's three channels are kept |
| `sat` | 1.1 | invented, a slight lift for the extra colour classes |
| `sheen` | 0.8 | invented ultraviolet, as today |
| `rate` | 0.56 | 60/107, L393 |
| `gain` | 1 | day fliers |

**New effects.** None is required. Later, a per-region colour field could give blues and coppers the male's dichromatic upper eye (L463) when the full database names a lycaenid; it costs one extra colour matrix and a vertical blend.

**Cue.** 'The picture keeps its colours, blurred, and runs slowly, then jumps ahead.'

### 2.2 `moth` (Lepidoptera other than Papilionoidea)

**Rows**

- `['m', 'Night eyes', 'Most moths fly at night with eyes built to gather light. In these eyes, light from ten or more lenses is focused onto each light-sensing cell, which makes them ten to a thousand times as sensitive as eyes like a butterfly’s. This view brightens the shadows.']`
  Log: L288, L366.
- `['m', 'Colour at night', 'Hawkmoths can tell colours apart in starlight, when people see only shades of grey. An elephant hawkmoth found a colour it had learned in light about a hundred times dimmer than a person needs to see colour. This view keeps colour in the dark.']`
  Log: L356, L363, L364, L357, L367.
- `['m', 'Red', 'Moths have colour-sensing cells for ultraviolet, blue and green, and most have none for red, so red flowers look dark to them.']`
  Log: L355, L66 to L77, L81 to L83, L88 to L90, L95 to L97.
- `['i', 'How the colours are shown', 'Since a screen can’t show ultraviolet, this view moves every colour over by one, as the bee view does: a moth’s green appears as red, its blue as green, and its ultraviolet as blue.']`
  Log: none; the drawing is the bee view's invented scheme.
- `['m', 'Dim light', 'As light fades, a moth’s eyes pool signals from neighbouring points and over longer moments. The picture stays bright and coloured, and it turns coarser and slower. This view does the same as the scene darkens.']`
  Log: L358, L362, L361, L360, L365.
- `['m', 'Speed', 'In dim light the eyes of several moths follow a flickering light 25 to 90 times a second, around a person’s 60, and they speed up in bright light. This view runs a little slowly in daylight and leaves trails at night.']`
  Log: L320, L321, L325, and the note on L318 (light adaptation raised the values by 40 to 70%).
- `['m', 'Lights at night', 'Flying insects keep their backs turned toward the brightest part of the sky, which keeps them level. A lamp at night pulls that sense of up sideways, so moths circle it, stall or flip over. This view tilts toward the brightest light.']`
  Log: L441, L442, L443.
- `['m', 'Sharpness', 'In good light a moth sees about a two-hundredth to a four-hundredth as much detail as a person does, and less as the light fails. This view is blurred to match.']`
  Log: L256 (1.9 degrees), L258 (3), L288 (1 to 5 degrees in superposition eyes).
- `['x', 'Hearing', 'Many moths have ears tuned to the high-pitched calls of hunting bats. This view leaves sound out.']`
  Log: L465.
- `['x', 'Smell', 'Night-flying moths rely more on smell than on colour to find flowers. This view leaves smell out.']`
  Log: L100.

**The picture**

| Field | Value | Behind it |
|---|---|---|
| `fov` | 320 | invented, as for butterflies |
| `cpd` | 0.25 in daylight, falling toward 0.1 in dim light | L256, L258, L288; the fall with light is from L362 and L358, its rate invented |
| `topoA`, `fall` | 0.4, 0.6 | frontal acute zone of the hummingbird hawkmoth (L371); numbers invented |
| `pupil`, `dof` | 'none', 0 | L313 |
| `M`, `uvBlue` | the bee matrix, 1 | three classes, ultraviolet, blue and green (L355); the colour shift is invented |
| `sat` | 1, kept in the dark | L357, L364 |
| `gain` | 1 in daylight rising to 3 in dim light | L288, L366; the curve invented |
| `rate` | 0.6 in daylight | Miall's 65 to 85 Hz (L320) light-adapted by 40 to 70% gives about 100 Hz: 60/100 |
| `persist` | 0 in daylight rising to 0.25 s in dim light | temporal summation, L358, L360; values invented |

**New effects.**

1. *Pooling with the light level.* The engine already knows the exposure (`u_expo`). Scale the blur radius, `persist` and `gain` with scene brightness, keeping saturation. In a dim room the picture goes coarse, slow and bright and keeps its colours, which is the measured trade (L357, L358, L362). Easy.
2. *Dorsal light tilt.* Find the brightest region in the lowest mipmap, compare its direction with gravity from the accelerometer, and roll the picture toward it by up to about 45 degrees, eased over half a second (bank angles near a lamp, L442). Under a porch light the world leans and swings round the lamp, as the moths' own flight does (L441, L443). By day, with the sky overhead, the tilt is nearly zero. Easy to moderate; needs the motion sensors.

**Cue.** 'Point it at a lamp at night: the picture tilts toward the light and keeps its colours in the dark.'

### 2.3 `dragonfly` (Odonata)

**Rows**

- `['m', 'Sharpest band', 'A dragonfly sees most sharply through a band of large lenses across the top of its eyes, which in the Common Green Darner runs over the head from one side to the other. In a darter, the upper eye resolves detail about four times finer than the lower eye. This view keeps a sharp band across the upper part of the picture.']`
  Log: L234, L272, L335, L235, L236.
- `['m', 'Sharpness', 'Even through that band, a dragonfly sees only about a thirtieth as much detail as a person does, the finest vision measured in any insect. Its lower eye is many times coarser.']`
  Log: L234 (0.24 degrees), L309 (2 cycles per degree), L236.
- `['m', 'Hunting', 'Perched dragonflies catch 83 to 97 per cent of the insects they chase. They pick prey that looks about a degree across, about the width of a fingernail at arm’s length, and a chase usually lasts less than half a second.']`
  Log: L328, L334, L331, L312.
- `['m', 'Tracking one target', 'Nerve cells in a dragonfly’s brain respond to small moving specks, even ones too small for its eyes to see clearly. When two specks move at once, the cells follow one and ignore the other, and their response grows as the chosen speck keeps to its path. This view finds small moving things and follows one at a time.']`
  Log: L342, L343, L341.
- `['m', 'Looking ahead', 'The same nerve cells become more sensitive just ahead of a target’s path, as if expecting where it will go next. This view brightens the space just ahead of the speck it follows.']`
  Log: L340.
- `['m', 'Colour', 'Dragonflies have four or five kinds of colour-sensing cells, including ones for ultraviolet and red, and as many as 30 genes for light-sensing proteins. The upper eye is tuned to the blues of the sky, and the lower eye to the colours of ground and plants.']`
  Log: L101 to L105, L110 to L123, L130, L345, L346.
- `['i', 'How the colours are shown', 'This view tints the upper part of the picture toward blue and violet and keeps reds in the lower part. These colours are the app’s own choice.']`
  Log: none; invented from the pattern in L346.
- `['g', 'Speed', 'The three small simple eyes on top of a dragonfly’s head follow a flickering light up to 220 times a second, and its main eyes are also faster than a person’s. This view runs slowly and then jumps ahead.']`
  Log: L353, L315. Graded `g`: the 220 is the ocellus; the main eyes' figure is a compilation.
- `['m', 'Level flight', 'Those simple eyes watch the horizon and help keep the head level in flight. This view keeps the horizon level when you tilt your phone.']`
  Log: L350, L444, L408.
- `['x', 'Polarized light', 'Dragonflies find water by the polarized light that smooth water reflects, and some are drawn to shiny black gravestones as if to a pond. This view leaves that sense out.']`
  Log: L347, L348, L432.

**The picture**

| Field | Value | Behind it |
|---|---|---|
| `fov` | 340 | invented; the Common Green Darner's band runs from one side over the top to the other (L335) |
| `cpd` | 1.6 in a band across the upper third, 0.3 below | L234 (2.1), L235 (1.25), L309 (2.0); L236 (0.28) |
| band width | about a fifth of the picture's height | invented; Anax's band is narrow (L272), perching skimmers' zone about 40 degrees wide (L274) |
| `pupil`, `dof` | 'none', 0 | L313 |
| `M` | upper band toward blue and violet, lower identity, blended across the middle | invented, after L346 |
| `sheen` | 0.8 | invented ultraviolet |
| `rate` | 0.3 | invented, between the compiled above-100 Hz (L315) and the ocellus's 220 (L353) |
| binocular overlap | small | L337 |

**New effects.**

1. *One target, followed.* On a frame of about 160 by 90 pixels, mark moving blobs that are small (a few pixels, standing in for the 1 to 3 degree prey of L334 and L333), let a blob's pull grow while it keeps a smooth path (L341), pick the strongest and ignore the rest (L343), brighten a spot just ahead of it (L340), and let its pull fade where it has sat for a few seconds, so a new target can win (local adaptation, L344). The sharp band swings to keep the chosen speck high in the picture, inside the 50 degree cone the dragonfly holds its prey in (L329). Midges in sunlight, a thrown seed or a bird far off become small glowing points that the view seizes and follows. Moderate: a few shader passes and a little JavaScript; it is the motion-salience map and the gaze the engine agent is building, with the size filter added.
2. *Horizon lock.* Counter-rotate the picture against the phone's roll, from gravity, to keep the horizon level (L350). Easy.
3. *Two-colour eye.* A vertical blend between two colour matrices. Easy once regions have their own colour.

**Cue.** 'The top of the picture is sharp. Small moving things are picked out and followed.'

### 2.4 `fly` (Diptera)

**Rows**

- `['m', 'Speed', 'Flies have some of the fastest eyes known. A tsetse fly’s eye follows a light that flickers up to 286 times a second in bright light, nearly five times as fast as a person’s. This view runs slowly and then jumps ahead to suggest the difference.']`
  Log: L317, L322, L315.
- `['m', 'Sharpness', 'Hoverflies and blowflies see about a hundred-and-thirtieth as much detail as a person does, house flies about a three-hundredth, and fruit flies about a six-hundredth. This view is blurred to match a hoverfly.']`
  Log: L261 (1.0 degrees), L262 (1.07 to 1.28), L265 (2.5), L266 (5).
- `['m', 'Gaze', 'A flying fly holds its gaze steady, then turns its head and body in quick jumps that approach several thousand degrees a second. During the steady moments it judges how near things are from how fast they slide past. This view holds still while you turn your phone, then jumps.']`
  Log: L382, L383, L473, L384.
- `['m', 'Field of view', 'A fruit fly sees almost all the way around itself, missing only about 50 degrees directly behind. This view bends the picture at its edges to suggest the wider sweep.']`
  Log: L450, L449.
- `['m', 'Colour', 'Flies have five kinds of colour-sensing cells, for ultraviolet, blue and green, and none tuned to red, so reds look dark to them.']`
  Log: L156 to L161, L301 to L305, L185.
- `['i', 'How the colours are shown', 'Since a screen can’t show ultraviolet, this view moves every colour over by one, as the bee view does: a fly’s green appears as red, its blue as green, and its ultraviolet as blue.']`
  Log: none; invented.
- `['m', 'Chasing', 'Males of many flies, hoverflies among them, have a patch of sharper vision for chasing females. A tiny robber fly of eastern North America spots prey a seventh of a degree across from more than half a metre away.']`
  Log: L279, L259, L377, L378.
- `['m', 'Dusk', 'A fly’s eye combines the signals of seven cells under neighbouring lenses that all look at the same point, which buys it about a quarter of an hour more flying time at sunrise and sunset.']`
  Log: L289.
- `['x', 'Polarized light', 'Horseflies find hosts and water by the polarized light that shiny surfaces reflect. This view leaves that sense out.']`
  Log: L186, L432.

**The picture**

| Field | Value | Behind it |
|---|---|---|
| `fov` | 310 | L450 (fruit fly, 360 minus a 50 degree blind spot) |
| `cpd` | 0.4 | L261 (0.5), L262 (0.4 to 0.47) |
| `topoA`, `fall` | 0.4, 0.7 | pattern from L475 (females like butterflies, males with an acute zone) and L262; the numbers are invented |
| `pupil`, `dof` | 'none', 0 | L313 |
| `M`, `uvBlue` | the bee matrix, 1 | L156 to L160, L185; drawing invented |
| `rate` | 0.24 | 60/250, invented within the measured 205 to 286 (L322, L317) |

**New effects.**

1. *Saccadic gaze.* Integrate the gyroscope; counter-rotate the picture so it holds still while the phone turns, until the turn passes about 20 degrees or a few tenths of a second go by, then snap to the new heading within about 50 milliseconds (the fly's turns reach thousands of degrees a second, L382). Between snaps the steady picture lets near things slide visibly faster than far ones, the parallax the fly reads (L473). This is the wader's held head turned into rotation, and it fits hoverflies, which hover and dart (L384). Moderate; needs the motion sensors.

**Cue.** 'Turn your phone slowly: the picture holds, then jumps.'

### 2.5 `ant` (Formicidae)

**Rows**

- `['m', 'Sharpness', 'An ant sees very little detail. A worker of an Australian carpenter ant sees about a seven-hundredth as much as a person does, and a desert ant about a five-hundredth. This view is blurred to match.']`
  Log: L401 (5.8 degrees), L268 (4).
- `['g', 'Field of view', 'Each of a desert ant’s eyes covers 150 to 170 degrees, so the two together take in nearly the whole circle around it. This view bends the picture at its edges to suggest the wider sweep.']`
  Log: L448.
- `['m', 'Colour', 'Most ants have two kinds of colour-sensing cells, for ultraviolet and green, where people have three. Some Australian bull ants have three.']`
  Log: L406, L219 to L225, L232, L405.
- `['i', 'How the colours are shown', 'This view shows an ant’s green as yellow and its ultraviolet, guessed from blue light, as blue, so reds look dark. These colours are the app’s own choice.']`
  Log: none; invented.
- `['m', 'Sky compass', 'Ants steer by the sun and by the pattern of polarized light in the blue sky, which they read with a narrow strip of specialized eye units along the top edge of each eye. The pattern forms rings around the sun and is strongest 90 degrees away from it. This view draws that pattern when you point your phone at the sky.']`
  Log: L398, L399, L400, L402, L466.
- `['m', 'Landmarks', 'Ants also learn the skyline around their nest and the views along their routes, and follow those views home. This view sharpens the line where the ground meets the sky.']`
  Log: L398, L469, L280.
- `['g', 'Speed', 'Australian bull ants that forage by day follow a flickering light up to about 189 times a second, and those that forage at night up to about 125. This view runs slowly and then jumps ahead.']`
  Log: L327, L326.
- `['x', 'Scent trails', 'Many ants, carpenter ants among them, lay scent trails between food and nest and follow them home. This view leaves smell out.']`
  Log: L468.

**The picture**

| Field | Value | Behind it |
|---|---|---|
| `fov` | 320 | L448 (two eyes of 150 to 170 degrees) |
| `cpd` | 0.09 | L401 (0.086, a carpenter ant congener of the Florida Carpenter Ant) |
| `topoS`, `fall` | 1, 1.2 | horizon streak of desert ants (L280); numbers invented |
| `pupil`, `dof` | 'none', 0 | L313 |
| `M`, `uvBlue` | [0,1,0, 0,1,0, 0,0,0], 1 | two classes (L406); the drawing invented |
| `rate` | 0.4 | 60/150, between L326 and L327 |

**New effects.**

1. *Sky compass.* From the date, the time and the longitude implied by the phone's time zone (which the app already reads, `docs/COVERAGE.md`), compute the sun's azimuth and height; from the compass and accelerometer, know where the phone points. When it points above the horizon, draw the E-vector pattern as faint bands in rings around the sun, brightest 90 degrees from it (L466). The physics is measured; the drawing is invented and the row says so through its grade. A time-zone longitude can be off by up to about 7.5 degrees, which moves the sun's computed azimuth by a few degrees; enough for a drawing. Moderate; needs the motion sensors and a compass permission on some phones.
2. *Skyline.* Sharpen and darken the boundary between bright sky and dark ground (a vertical gradient of the lowest mipmap). Invented, after L398 and L469. Easy.

**Cue.** 'Point your phone at the sky to see the pattern ants steer by.'

### 2.6 `mantis` (Mantodea)

**Rows**

- `['m', 'Depth', 'A praying mantis judges how far away its prey is by comparing the views of its two eyes, perhaps the only insect that does so. It does this for things that move, and there is no evidence that it works for things that stay still. This view brings out moving things that are near and leaves still things flat.']`
  Log: L276, L409, L411, L415.
- `['m', 'Camouflage', 'Because its depth sense works on movement, a mantis can find an insect that matches its background perfectly, as long as the insect moves.']`
  Log: L410.
- `['m', 'Striking range', 'A mantis strikes at prey a few centimetres away. Mantises wearing tiny 3D glasses struck at targets on a screen 10 centimetres off when the glasses made them appear 2.5 centimetres away.']`
  Log: L412, L411.
- `['m', 'Sharpest spot', 'A mantis sees most sharply straight ahead, where the views of its two eyes overlap. There the angle between neighbouring lenses is about a quarter of what it is at the edges of the eye, and the mantis turns to bring prey into this spot before striking.']`
  Log: L243, L277, L414.
- `['m', 'Sharpness', 'Even in that spot a mantis sees less than a seventieth as much detail as a person does. This view is sharp in the centre and very blurred toward the edges.']`
  Log: L243.
- `['m', 'Peering', 'Young mantises sway their heads from side to side before they jump, and judge distance by how far things shift against the background. Sway your phone sideways, and this view brings out what shifts most.']`
  Log: L413.
- `['g', 'Colour', 'The Chinese mantis has one main kind of colour-sensing cell, tuned to green, and a weaker response to near-ultraviolet light.']`
  Log: L416, L417, L145.
- `['i', 'How the colours are shown', 'This view assumes that a mantis sees little colour and shows the world in shades of green.']`
  Log: none; a guess from L416.
- `['x', 'Hearing', 'Many mantises have a single ear in the middle of the body, tuned to the ultrasound of hunting bats, and some swerve in flight when they hear it. This view leaves sound out.']`
  Log: L467.

**The picture**

| Field | Value | Behind it |
|---|---|---|
| `fov` | 300 | invented |
| `cpd` | 0.8 at the centre, falling to 0.2 at the edge | L243 (0.6 to 2.5 degrees) |
| `topoA`, `fall` | 1, 3 | with `topoA` 1 the blur at half the short side is 1 + 3 = 4 times the centre's, matching the fourfold change in L243 (0.6 to 2.5 degrees); placing the fourfold point there is invented |
| `fovea` | 1.3 | invented magnification of the shared frontal zone (L277) |
| `pupil`, `dof` | 'none', 0 | L313 |
| `M` | [0,0.3,0, 0,1,0, 0,0.3,0] | green-tinted grey from the camera's green (L416); invented |
| `sheen` | 0.3 | invented, the weak near-ultraviolet response (L417) |
| `rate` | 1 | no measurement; real time, invented |
| `gate` | moving and near things brightened, others dimmed to about half | L409, L410; the mix invented |

**New effects.**

1. *Moving depth.* Brighten and sharpen what moves and is near; leave still things flat and dim (L409, L410). Nearness, in increasing order of cost: (a) apparent size and closeness to the lower centre, a proxy; (b) parallax while the person sways the phone, from optical flow against the accelerometer, which is the mantis larva's own method (L413); (c) a depth model on the camera picture, which the brief says is possible at a cost. Start with (b): it is measured behaviour, it costs a flow estimate on a small frame, and it rewards the person for peering. Moderate.
2. *Strike zone.* When a moving thing is near and centred, flash the centre once (the strike is too fast for visual feedback, L414). Easy.

**Cue.** 'Only moving things that are near stand out. Sway your phone to judge distance.'

### 2.7 `springtail` (Collembola, Protura, Diplura)

**Rows**

- `['m', 'Eight eyes a side', 'A springtail has at most eight tiny eyes on each side of its head, set well apart. Each takes in a patch of the world tens of degrees across, so a springtail sees no picture, only a few patches of light and dark. This view shows sixteen soft patches of light.']`
  Log: L451, L233.
- `['m', 'Eyeless relatives', 'Diplurans and proturans, small soil animals grouped here with springtails, have no compound eyes.']`
  Log: L451.
- `['i', 'Colour and speed', 'This part of the view is a guess. It assumes that springtails see only light and dark, at the pace of your camera.']`
  Log: none.
- `['x', 'A sense of unknown use', 'Behind each antenna, springtails of three families carry a small sense organ whose job is still unknown. It may sense moisture, chemicals or warmth. This view leaves it out.']`
  Log: L470.

**The picture.** `field`-like. Sample the camera picture in 16 directions, 8 on each half, each with a soft kernel 25 to 57 degrees wide (L233), and draw 16 glowing discs on black; `sat` 0, `rate` 1, `fov` 360, all invented except the kernel widths and the count (L451). For diplurans and proturans the view would show light only, as the plant view does; they are 229 world records, too few to treat apart.

**New effects.** *Sparse eyes:* the 16-disc drawing. Easy: 16 texture reads from a low mipmap.

**Cue.** 'Only a few soft patches of light.'

### 2.8 `insect` (everything else) and its `firefly` variant

**Rows**

- `['m', 'Sharpness', 'Beetles, true bugs, grasshoppers and their relatives see between a hundredth and a thousandth as much detail as people do. A locust sees most sharply of these, a ladybird about a three-hundred-and-fiftieth as much as a person, and a stick insect about a nine-hundredth. This view is blurred to match a ladybird.']`
  Log: L240 (locust 0.9 degrees), L249 (seven-spot ladybird 2.9), L241 (stick insect 7.5), L244 to L252.
- `['m', 'Colour', 'Most of these insects have colour-sensing cells for ultraviolet, blue and green, and none for red, so reds look dark to them. Cockroaches and many beetles lack the blue cells, though several lines of beetles have regained them.']`
  Log: L1, L136 to L144, L146 to L154, L131 to L133, L189, L438, L190 to L192.
- `['i', 'How the colours are shown', 'Since a screen can’t show ultraviolet, this view moves every colour over by one, as the bee view does: an insect’s green appears as red, its blue as green, and its ultraviolet as blue.']`
  Log: none; invented.
- `['m', 'Field of view', 'An American cockroach sees all the way around itself, and grasshoppers and many other insects nearly so. This view bends the picture at its edges to suggest the wider sweep.']`
  Log: L452.
- `['m', 'Approaching things', 'Locusts have large nerve cells that fire when something looms toward them, and the signal makes a flying locust glide out of the way. This view flashes things that grow quickly in the picture.']`
  Log: L419, L420.
- `['g', 'Speed', 'In dim light a locust’s eye follows a flickering light 40 to 90 times a second and an American cockroach’s 25 to 60, close to a person’s 60, and both speed up in bright light. This view runs a little slowly.']`
  Log: L318, L319, L324.
- `['m', 'Sky compass', 'Crickets, locusts and dung beetles read the pattern of polarized light in the sky, and an African dung beetle reads it by moonlight, a million times dimmer than sunlight.']`
  Log: L422, L428, L434, L399.
- `['m', 'Distance by swaying', 'Young locusts sway their bodies from side to side before they jump, and judge distance by how far things shift.']`
  Log: L421.
- `['x', 'Hearing', 'Crickets and katydids hear songs and the calls of bats between about 2,000 and 40,000 vibrations a second. This view leaves sound out.']`
  Log: L424, L425, L427.
- `['x', 'Vibrations', 'Stink bugs court with vibrations they send through plant stems and feel with all six legs. This view leaves those vibrations out.']`
  Log: L429, L431.

**Firefly variant rows** (when the full database names a lampyrid; they replace the speed, colour and sky compass rows):

- `['m', 'Flashes', 'Males of the common eastern firefly flash about every six seconds as they fly, and a waiting female answers about two seconds after each flash. This view picks out flashes and marks where an answer would come.']`
  Log: L456.
- `['m', 'Tuned to flashes', 'A firefly’s eye is most sensitive near the colour of its own species’ flash, helped by filters in the eye.']`
  Log: L216, L208, L209, L215.
- `['m', 'Night eyes', 'Fireflies have eyes that gather light from many lenses at once, built for dusk and night.']`
  Log: L247, L288.

**The picture**

| Field | Value | Behind it |
|---|---|---|
| `fov` | 340 | L452 (cockroach 360; grasshoppers similar, same source) |
| `cpd` | 0.2 | L249 (0.17), L244 (0.24), L246 (0.33), L240 (0.56) |
| `topoA`, `topoS`, `fall` | 0.3, 0.5, 0.6 | acridid flight pattern (L284); numbers invented; katydids have no such pattern (L283) |
| `pupil`, `dof` | 'none', 0 | L313 |
| `M`, `uvBlue` | the bee matrix, 1 | three classes in most (L1); drawing invented |
| `rate` | 0.6 | invented within L318, L324 and the light-adapted rise noted on L318 |
| `gain` | 1.2 | invented; many members are nocturnal |
| firefly: `M`, `gain`, `cpd` | one yellow-green channel ([0.5,0.7,0, 0.5,0.7,0, 0,0,0]), 2.5, 0.28 | L215, L208 (one long-wavelength class); L247 (1.8 degrees, superposition); colours and gain invented |

**New effects.**

1. *Looming flash.* Where the optical flow on a small frame diverges fast (something approaching), flash it (L419, L420). Moderate, and shared with the motion-salience work.
2. *Firefly flashes.* A temporal high-pass on a low-resolution frame finds brief bright points; draw each as a glowing mark and, two seconds later, a fainter answering mark beside it (L456). At dusk in a Florida yard this turns real flashes into a conversation the firefly would expect. Easy to moderate.
3. *Song band* (for a later cricket and katydid setting). An FFT of the microphone; energy between about 2 and 20 kHz pulses the picture's brightness in time with the song (L424, L425). The phone hears this band; the view would then move hearing from an `x` row to an `m` row for crickets. Easy; needs microphone permission.
4. *Plant vibrations* (for a later stink bug setting). With the phone lying on a table, the accelerometer's high-frequency part ripples the picture (L429 to L431). Invented stand-in. Easy.

**Cue.** 'Things that rush toward you flash.' Firefly: 'At dusk, flashes are marked, and the view waits for an answer.'

## 3. The existing view `insect`, checked

`insect: { chip: 'Butterfly, other insect', who: 'an insect', fov: 320, cpd: 1, pupil: 'none', sheen: .8, rate: .45, cue: 'The view is wide and blurry, and it runs slowly, then jumps ahead.' }`. `docs/SOURCES.md` backs the measured lines with Caves, Brandley and Johnsen 2018 (through the Duke University summary) and Inger et al. 2014.

| Item | Status | Finding |
|---|---|---|
| `chip`, `who` | corrected by the split | the eight views above |
| `fov` 320 | unsupported as a number | no butterfly, moth or dragonfly field was found; the nearest measurements give 310 for the fruit fly (L450), 360 for the cockroach (L452), 300 to 340 for desert ants (L448), so 320 is a fair group value |
| `cpd` 1 | corrected | the Duke summary says most insects "can't see more than one" (L455), an upper bound. Measured values for common flying insects are 0.17 to 0.5 (L270); beetles 0.07 to 0.33 (L246 to L252); ants about 0.1 (L401, L268). Only dragonfly acute zones reach 2 (L234, L309). The view is two to six times too sharp for most of its members |
| `pupil` 'none' | confirmed | L313: insect ommatidia need no focusing, so no part of the scene is out of focus |
| `sheen` 0.8 | invented, as `docs/SOURCES.md` says | kept in the butterfly and dragonfly views |
| `rate` 0.45 | unsupported as a number | 60/133 matches no measurement. Measured: tsetse 286 Hz in bright light (L317); flies 85 to 205 dark adapted (L322); Japanese Yellow Swallowtail 82 to 107 (L393 to L397); moths 25 to 90 dark adapted (L320, L321, L325); locust 40 to 90, cockroach 25 to 60 (L318, L319); bull ants 125 and 189 (L326, L327). Per-view rates replace it |
| `cue` | confirmed in form | each new view has its own |
| Row 'Sharpness' (`g`): most insects see less than a sixtieth of a person's detail | confirmed, and understated | Land 1997 puts common flying insects at a hundred-and-twentieth to a three-hundred-and-sixtieth (L270); the row should give the measured figure and say what the view does |
| Row 'Speed' (`g`): flies and dragonflies above 100 a second | confirmed for flies (L317, L322, L315); for dragonflies only through a compilation (L315) and the ocellus (L353). `docs/SOURCES.md` lists this line as unbacked; Inger et al. 2014 now back it in words (L315) | |
| Row 'Speed': one beetle up to 400 | confirmed as Inger et al.'s statement, corrected as a row | the beetle is the black fire beetle *Melanophila acuminata*, which flies to forest fires (L314); Inger et al. give no primary source for the figure. It stands for no common beetle. Nocturnal insects average 70 Hz in the same compilation (L316) |
| Row 'Ultraviolet' (`i`): bees and some other insects see ultraviolet | corrected | an ultraviolet receptor is measured in nearly every insect group in van der Kooi et al. 2021's Table 1: butterflies, moths, dragonflies, flies, beetles, bugs, grasshoppers, cockroaches and ants (L1, L8, L66, L101, L131, L136, L146, L156, L190, L219). The seeing is `m`; only the drawing is `i`. The phone half of the row rests on a source `docs/COVERAGE.md` found does not say it, and the crab sheet's measurement of weak ultraviolet A response in one phone (Igoe, Parisi and Carter 2012) was not opened here |

## 4. Species with their own measurements

Commonly photographed species, or close relatives of them, measured well enough for a profile later. Log lines in brackets.

- **Monarch** *Danaus plexippus* (world and Alachua top five): three classes at 340, 435 and 540 nm with a red-opponent channel and orange filter pigment (L8 to L11, L386, L387); dorsal rim of about 100 ommatidia (L388); sun compass (L389, L391); magnetic inclination sense (L390). Ready.
- **Heliconians**: Zebra Longwing *Heliconius charithonia* (L18, long-wavelength only) with *H. erato* for the rest (five classes in males, red discrimination, L12 to L17, L64, L387); Gulf Fritillary *Dione vanillae* (L19, long-wavelength only). A heliconian profile can borrow *H. erato*, graded `g`.
- **Swallowtails**: the Japanese Yellow Swallowtail *Papilio xuthus* (five to eight classes, behaviour of a tetrachromat, flicker by class, colour in single pixels: L6, L7, L36 to L40, L374, L393 to L397) and the Orchard Swallowtail *P. aegeus* (red receptor for leaf choice, L41 to L45, L462) stand for Florida's swallowtails (`g`).
- **Whites and sulphurs**: the Small White (six classes including two red, L24 to L30), the Large White's wavelength-specific behaviours (L307) and acuity (L255), *Colias erate* (L31 to L35), the sulphur *Phoebis rurina* (L474).
- **Blues and coppers**: *Lycaena* (four pigments, regional dichromacy in males, L56 to L60, L463).
- **Hawkmoths**: the elephant hawkmoth (night colour vision, L66 to L68, L356, L363 to L365), the tobacco hornworm *Manduca sexta*, a Florida species (L69 to L71, L372), and the hummingbird hawkmoth (L72 to L74, L362, L371).
- **Giant silk moths**: the Polyphemus Moth *Antheraea polyphemus*, an Alachua top-thirty species, measured itself (L75 to L77), with its congener's flicker fusion (L321); the Luna Moth through *Actias artemis aliena* (L78 to L80, `g`).
- **Common Green Darner** *Anax junius*: 0.24 degree dorsal band, 28,672 ommatidia per eye (L234, L272, L273, L335, L109). Ready for a profile.
- **Skimmers** (Eastern Pondhawk, Blue Dasher): perching libellulid zones and hunting (L274, L328 to L334), Needham's Skimmer receptors (L107, L108), the Common Whitetail's head saccade (L330, L332).
- **House fly** (L156 to L161, L265, L301 to L305) and **drone fly** *Eristalis tenax* (L167 to L169, L188, L261, L384).
- **Robber fly** *Holcocephala fusca*: frontal fovea of 0.28 degrees, detection at 0.13 degrees, lock-on (L377 to L379). A profile would add the target tracker of the dragonfly view.
- **Black soldier fly** *Hermetia illucens*, Alachua's fourth most recorded fly: three ultraviolet classes and a green (L175 to L178).
- **Ladybirds**: the seven-spot ladybird (L190 to L192, L249) stands for the Asian Lady Beetle, the third most recorded species on iNaturalist in the world list (`runs/coverage/1-lists/world-head.tsv`), graded `g`.
- **Tiger beetles** *Cicindela* (L193, L194, L246, L440).
- **American cockroach** (L131 to L133, L319, L445 to L447, L452).
- **Grasshoppers**: migratory and desert locusts (L136 to L141, L240, L318, L419 to L421) stand for the American Bird Grasshopper.
- **Field crickets** (L142 to L144, L422, L423).
- **Chinese mantis** *Tenodera sinensis* (L145, L416, L417) and the African mantis *Sphodromantis lineola* for stereopsis (L411, L412).
- **Common eastern firefly** *Photinus pyralis* (L208, L456).
- **Carpenter ants** through *Camponotus consobrinus*, *C. blandus* and *C. pennsylvanicus* (L219 to L221, L401 to L403, L468), `g` for the Florida Carpenter Ant.
- **Fire ants**: *Solenopsis saevissima* has a third class at 620 nm (L229 to L231). If the Red Imported Fire Ant shares it, fire ants would see red, unlike most ants; its eyes are on the wanted list.
- **Backswimmer** *Notonecta glauca* (L149 to L151, L245, L282) and **water strider** *Gerris* (L244, L281).

## 5. Gaps and how to fill them

| Trait | Views that need it | Nearest measurement | Inference |
|---|---|---|---|
| Field of view | butterfly, moth, dragonfly, mantis | fruit fly 310 (L450), cockroach 360 (L452), desert ants 300 to 340 (L448) | flying insects with large eyes probably cover 300 to 340 degrees; the values above are invented within that range. Rutowski and Warrant 2002 (wanted) gives a butterfly |
| Flicker fusion of butterflies other than one swallowtail | butterfly | *Papilio xuthus* 82 to 107 Hz (L393 to L397); unpalatable butterflies slower (L392) | use 107 for all; slow the warningly coloured ones (heliconians, monarch) when Chatterjee et al. 2020 or the Para thesis gives numbers |
| Flicker fusion of dragonfly compound eyes | dragonfly | ocellus 220 (L353); compilation above 100 (L315) | 200 Hz, invented between |
| Flicker fusion of beetles, bugs, mantises, springtails | insect, mantis, springtail | locust 40 to 90 and cockroach 25 to 60, dark adapted (L318, L319); light adaptation adds 40 to 70% (L318 note) | about 100 Hz in daylight for diurnal members; nothing for mantises and springtails |
| Acuity of the most photographed moth families (Erebidae, Noctuidae, Geometridae, Crambidae) | moth | superposition eyes 1 to 5 degrees (L288), *Ephestia* 3 (L258) | about 2 to 3 degrees |
| Acuity of longhorn beetles, leaf beetles other than *Chrysomela*, stink bugs, katydids, cicadas | insect | ladybird 2.9 (L249), leaf beetle 5.4 (L250), bugs 1.65 to 2.1 (L244, L245) | 2 to 5 degrees; stink bugs and cicadas about 2 by their relatives |
| Colour of the Asian Lady Beetle, longhorns, stink bugs, katydids | insect | seven-spot ladybird 360, 420, 520 nm (L190 to L192); aphid, leafhopper, backswimmer trichromats (L146 to L154) | trichromat, `g` |
| Colour of the commonest Florida butterflies | butterfly | only their long-wavelength classes are measured (L18 to L23) | borrow congeners: *Heliconius erato* for heliconians, *Papilio* for swallowtails |
| Ant eyes of the Florida species | ant | carpenter ant congener (L401); hyperoptic twig ants (L404); fire ant relative's red class (L229 to L231) | twig ants sharper than the view, fire ants coarser; nothing measured for either here |
| Springtail colour and speed | springtail | none | nothing is known to this sheet |
| Caterpillar vision | a possible caterpillar view | six stemmata a side (L457); swallowtail larva's three classes (L459 to L461) | a dozen coloured points; Gilbert 1994 (wanted) would say more |
| Mantis field of view, speed | mantis | none | nothing is known to this sheet |

## 6. Closed sources wanted

The list in `docs/views/wanted/insect.jsonl`, most useful first:

1. Land and Nilsson 2012, *Animal Eyes*, chapters 7 to 9 (the Drive copy stopped at page 65).
2. Chatterjee, Mohan, Krishnan and Sane 2020, flicker fusion across Lepidoptera (10.1007/s00359-020-01429-3).
3. Laughlin and Weckström 1993, fast and slow photoreceptors in Diptera (10.1007/bf00213682).
4. Rutowski and Warrant 2002, the Empress Leilia's visual field (10.1007/s00359-001-0273-7).
5. Mischiati et al. 2014, internal models in dragonfly interception (10.1038/nature14045).
6. Olberg et al. 2007, dragonfly eye movements during interception (10.1007/s00359-007-0223-0).
7. Baker and Ma 2006, fire ant ommatidia (10.1016/j.jcz.2006.06.001).
8. Kelber, Balkenius and Warrant 2002, scotopic colour vision in hawkmoths (10.1038/nature01065).
9. Stöckl, O'Carroll and Warrant 2016, neural summation in hawkmoths (10.1016/j.cub.2016.01.030).
10. Priority 2 and 3: Rossel 1979, 1980 and 1983 (mantis acute zone, fixation, stereopsis); Nityananda et al. 2018 full text; Gilbert 1997 (tiger beetle pursuit); Cronin et al. 2000 and Martin et al. 2015 (firefly eyes); Merkhofer 1978 (firefly flicker fusion); Zeil 1983 (bibionid eyes, for the lovebug); Rutowski, Gislén and Warrant 2008; Weckström and Laughlin 1995; Kriska et al. 2009; Yang and Osorio 1991; Bybee et al. 2012; Gilbert 1994; Hammer et al. 2001.

## 7. Sources

One line per source behind the log, 109 in all. Works cited only through a review are named in the log lines' notes and are not listed here; where a log line rests on a review, the line says so and is graded by what the review reports.

- Agee HR 1971. Flicker fusion frequency of the compound eye of Heliothis zea (Lepidoptera: Noctuidae). *Annals of the Entomological Society of America 64(4):942*. https://doi.org/10.1093/aesa/64.4.942. opened, abstract.
- Altner H, Thies G 1976. The postantennal organ: a specialized unicellular sensory input to the protocerebrum in apterygotan insects (Collembola). *Cell and Tissue Research 167:97-110*. https://doi.org/10.1007/BF00220161. opened, abstract.
- Ardin P, Peng F, Mangan M, Lagogiannis K, Webb B 2016. Using an Insect Mushroom Body Circuit to Encode Route Memory in Complex Natural Environments. *PLoS computational biology*. https://doi.org/10.1371/journal.pcbi.1004683. opened, full text.
- Belušič G, Ilić M, Meglič A, Pirih P 2021. Red-green opponency in the long visual fibre photoreceptors of brushfoot butterflies (Nymphalidae). *Proceedings of the Royal Society B Biological Sciences*. https://doi.org/10.1098/rspb.2021.1560. opened, full text.
- Belwood JJ, Morris GK 1987. Bat Predation and Its Influence on Calling Behavior in Neotropical Katydids. *Science*. https://doi.org/10.1126/science.238.4823.64. opened, abstract.
- Bernard GD, Remington CL 1991. Color vision in Lycaena butterflies: spectral tuning of receptor arrays in relation to behavioral ecology. *Proceedings of the National Academy of Sciences*. https://doi.org/10.1073/pnas.88.7.2783. opened, abstract.
- Bernáth B, Szedenics G, Wildermuth H, Horváth G 2002. How can dragonflies discern bright and dark waters from a distance? The degree of polarisation of reflected light as a possible cue for dragonfly habitat selection. *Freshwater Biology*. https://doi.org/10.1046/j.1365-2427.2002.00931.x. opened, abstract.
- Blackiston DJ, Briscoe AD, Weiss MR 2011. Color vision and learning in the monarch butterfly,Danaus plexippus(Nymphalidae). *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.048728. opened, abstract.
- Bomphrey RJ, Nakata T, Henningsson P, Lin H 2016. Flight of the dragonflies and damselflies. *Philosophical Transactions of the Royal Society B Biological Sciences*. https://doi.org/10.1098/rstb.2015.0389. opened, full text.
- Brunner DP, Labhart T 1987. Behavioural evidence for polarization vision in crickets. *Physiological Entomology*. https://doi.org/10.1111/j.1365-3032.1987.tb00718.x. opened, abstract.
- Buck J, Buck E 1968. Mechanism of Rhythmic Synchronous Flashing of Fireflies. *Science*. https://doi.org/10.1126/science.159.3821.1319. opened, abstract.
- Buck J 1990. Unisex flash controls in dialog fireflies. *Biological Bulletin 179:87-95*. https://archive.org/details/biostor-10331. opened, full text as Biodiversity Heritage Library OCR, read through the web tool.
- Burton BG, Tatler BW, Laughlin SB 2001. Variations in Photoreceptor Response Dynamics Across the Fly Retina. *Journal of Neurophysiology*. https://doi.org/10.1152/jn.2001.86.2.950. opened, abstract.
- Buschbeck EK 2014. Escaping compound eye ancestry: the evolution of single-chamber eyes in holometabolous larvae. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.085365. opened, abstract.
- Collett M 2010. How desert ants use a visual landmark for guidance along a habitual route. *Proceedings of the National Academy of Sciences*. https://doi.org/10.1073/pnas.1001401107. opened, abstract.
- Combes SA, Salcedo MK, Pandit M, Iwasaki JM 2013. Capture Success and Efficiency of Dragonflies Pursuing Different Types of Prey. *Integrative and Comparative Biology*. https://doi.org/10.1093/icb/ict072. opened, abstract.
- Corrette BJ 1990. Prey capture in the praying mantis Tenodera aridifolia sinensis: coordination of the capture sequence and strike movements. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.148.1.147. opened, abstract.
- Dacke M, Byrne MJ, Scholtz CH, Warrant EJ 2004. Lunar orientation in a beetle. *Proceedings of the Royal Society B Biological Sciences*. https://doi.org/10.1098/rspb.2003.2594. opened, abstract.
- Evans BJE, O’Carroll DC, Fabian JM, Wiederman SD 2022. Dragonfly Neurons Selectively Attend to Targets Within Natural Scenes. *Frontiers in Cellular Neuroscience*. https://doi.org/10.3389/fncel.2022.857071. opened, full text.
- Fabian ST, Sondhi Y, Allen PE, Theobald JC, Lin HT 2024. Why flying insects gather at artificial light. *Nature communications*. https://doi.org/10.1038/s41467-024-44785-3. opened, full text.
- Fent K, Wehner R 1985. Ocelli: A Celestial Compass in the Desert Ant Cataglyphis. *Science*. https://doi.org/10.1126/science.228.4696.192. opened, abstract.
- Foster JJ, Tocco C, Smolka J, Khaldy L, Baird E, Byrne MJ et al. 2021. Light pollution forces a change in dung beetle orientation behavior. *Current biology : CB*. https://doi.org/10.1016/j.cub.2021.06.038. opened, abstract.
- Franzke M, Kraus CM, Dreyer D, Pfeiffer K, Beetz MJ, Stöckl A et al. 2020. Spatial orientation based on multiple visual cues in non-migratory monarch butterflies. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.223800. opened, abstract.
- Frederiksen R, Warrant EJ 2008. Visual sensitivity in the crepuscular owl butterfly Caligo memnon and the diurnal blue morpho Morpho peleides: a clue to explain the evolution of nocturnal apposition eyes?. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.012179. opened, abstract.
- Frolov RV, Matsushita A, Arikawa K 2017. Not flying blind: a comparative study of photoreceptor function in flying and non-flying cockroaches. *The Journal of experimental biology*. https://doi.org/10.1242/jeb.159103. opened, abstract.
- Futahashi R, Kawahara‐Miki R, Kinoshita M, Yoshitake K, Yajima S, Arikawa K et al. 2015. Extraordinary diversity of visual opsin genes in dragonflies. *Proceedings of the National Academy of Sciences*. https://doi.org/10.1073/pnas.1424670112. opened, abstract.
- Geurten BRH, Kern R, Braun E, Egelhaaf M 2010. A syntax of hoverfly flight prototypes. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.036079. opened, abstract.
- Gilbert C 1994. Form and Function of Stemmata in Larvae of Holometabolous Insects. *Annual Review of Entomology*. https://doi.org/10.1146/annurev.en.39.010194.001543. opened, abstract.
- Gonzalez-Bellido PT, Wardill TJ, Juusola M 2011. Compound eyes and retinal information processing in miniature dipteran species match their specific ecological demands. *Proceedings of the National Academy of Sciences*. https://doi.org/10.1073/pnas.1014438108. opened, abstract.
- Gonzalez-Bellido PT, Peng H, Yang J, Georgopoulos AP, Olberg RM 2012. Eight pairs of descending visual neurons in the dragonfly give wing motor centers accurate population vector of prey direction. *Proceedings of the National Academy of Sciences*. https://doi.org/10.1073/pnas.1210489109. opened, abstract.
- Henze MJ, Dannenhauer K, Kohler M, Labhart T, Gesemann M 2012. Opsin evolution and expression in Arthropod compound Eyes and Ocelli: Insights from the cricket Gryllus bimaculatus. *BMC Evolutionary Biology*. https://doi.org/10.1186/1471-2148-12-163. opened, full text.
- Homberg U, Heinze S, Pfeiffer K, Kinoshita M, Jundi BE 2011. Central neural coding of sky polarization in insects. *Philosophical Transactions of the Royal Society B Biological Sciences*. https://doi.org/10.1098/rstb.2010.0199. opened, abstract.
- Horridge GA, Giddings C, Stange G 1972. The superposition eye of skipper butterflies. *Proceedings of the Royal Society B Biological Sciences*. https://doi.org/10.1098/rspb.1972.0088. opened, abstract.
- Horridge GA, McLean MR, Stange G, Lillywhite PG 1977. A diurnal moth superposition eye with high resolution Phalaenoides tristifica (Agaristidae). *Proceedings of the Royal Society B Biological Sciences*. https://doi.org/10.1098/rspb.1977.0039. opened, abstract.
- Horridge GA, Duelli P 1979. Anatomy of the Regional Differences in the Eye of the Mantis Ciulfina. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.80.1.165. opened, abstract.
- Horridge GA, Marčelja L 1992. On the existence of 'fast' and ‘slow' directionally sensitive motion detector neurons in insects. *Proceedings of the Royal Society B Biological Sciences*. https://doi.org/10.1098/rspb.1992.0041. opened, abstract.
- Horváth G, Malik P, Kriska G, Wildermuth H 2007. Ecological traps for dragonflies in a cemetery: the attraction of Sympetrum species (Odonata: Libellulidae) by horizontally polarizing black gravestones. *Freshwater Biology*. https://doi.org/10.1111/j.1365-2427.2007.01798.x. opened, abstract.
- Horváth G, Kriska G 2008. Polarization vision in aquatic insects and ecological traps for polarotactic insects. *CABI eBooks*. https://doi.org/10.1079/9781845933968.0204. opened, abstract.
- Huang S, Chiou T, Marshall NJ, Reinhard JR 2014. Spectral Sensitivities and Color Signals in a Polymorphic Damselfly. *PLoS ONE*. https://doi.org/10.1371/journal.pone.0087972. opened, full text.
- Imaizumi K, Pollack GS 1999. Neural Coding of Sound Frequency by Cricket Auditory Receptors. *Journal of Neuroscience*. https://doi.org/10.1523/jneurosci.19-04-01508.1999. opened, abstract.
- Inger R, Bennie J, Davies TW, Gaston KJ 2014. Potential biological and ecological effects of flickering artificial light. *PLoS ONE 9(5):e98631*. https://doi.org/10.1371/journal.pone.0098631. opened, full text through the web tool (Table 3 is an image and was not read); a compilation, values graded by what it reports.
- Johnsen S, Kelber A, Warrant EJ, Sweeney A, Widder EA, Lee RL et al. 2006. Crepuscular and nocturnal illumination and its effects on color perception by the nocturnal hawkmoth Deilephila elpenor. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.02053. opened, abstract.
- Jundi BE, Smolka J, Baird E, Byrne MJ, Dacke M 2014. Diurnal dung beetles use the intensity gradient and the polarization pattern of the sky for orientation. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.101154. opened, abstract.
- Kelber A 1999. Ovipositing butterflies use a red receptor to see green. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.202.19.2619. opened, abstract.
- Kelber A 2003. Colour Vision in Diurnal and Nocturnal Hawkmoths. *Integrative and Comparative Biology*. https://doi.org/10.1093/icb/43.4.571. opened, abstract.
- Kelber A, Roth LSV 2006. Nocturnal colour vision – not as rare as we might think. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.02060. opened, abstract.
- Kern R, van Hateren JH, Michaelis C, Lindemann JP, Egelhaaf M 2005. Function of a Fly Motion-Sensitive Neuron Matches Eye Movements during Free Flight. *PLoS Biology*. https://doi.org/10.1371/journal.pbio.0030171. opened, full text.
- Labhart T, Meyer EP 1999. Detectors for polarized skylight in insects: a survey of ommatidial specializations in the dorsal rim area of the compound eye. *Microscopy Research and Technique*. https://doi.org/10.1002/(sici)1097-0029(19991215)47:6<368::aid-jemt2>3.0.co;2-q. opened, abstract.
- Labhart T, Baumann F, Bernard GD 2009. Specialized ommatidia of the polarization-sensitive dorsal rim area in the eye of monarch butterflies have non-functional reflecting tapeta. *Cell and Tissue Research*. https://doi.org/10.1007/s00441-009-0886-7. opened, full text.
- Land MF 1997. Visual acuity in insects. *Annual Review of Entomology 42:147-177*. https://doi.org/10.1146/annurev.ento.42.1.147. opened, owner's library (paywalled; quoted at most 40 words).
- Land MF, Nilsson D-E 2012. Animal Eyes, 2nd edition. *Oxford University Press, ISBN 978-0-19-958113-9*. https://search.worldcat.org/search?q=bn:9780199581139. opened, book: pp. 1-65 only (chapters 1, 2 and most of 3).
- Land MF, Chittka L (revisers of Chapman RF) 2013. Vision (chapter 22). *In: Simpson SJ, Douglas AE (eds) The Insects: Structure and Function, 5th edition. Cambridge University Press, pp. 708-737*. https://chittkalab.sbcs.qmul.ac.uk/2013/Land%20Chittka%202013%20The%20Insects%20-%20Vision.pdf. opened, book chapter: authors' posted copy, read through the web tool.
- Layne JE, Chen PW, Gilbert C 2006. The role of target elevation in prey selection by tiger beetles(Carabidae:Cicindelaspp.). *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.02529. opened, abstract.
- McBrien H, Millar JG 2003. Substrate-borne vibrational signals of the Consperse stink bug (Hemiptera: Pentatomidae). *The Canadian Entomologist*. https://doi.org/10.4039/n02-078. opened, abstract.
- Miall RC 1978. The flicker fusion frequencies of six laboratory insects, and the response of the compound eye to mains fluorescent 'ripple'. *Physiological Entomology 3:99-106*. https://doi.org/10.1111/j.1365-3032.1978.tb00139.x. opened, abstract.
- Mote MI, Goldsmith TH 1970. Spectral sensitivities of color receptors in the compound eye of the cockroach Periplaneta. *Journal of Experimental Zoology*. https://doi.org/10.1002/jez.1401730203. opened, abstract.
- Muinde J, Zhang T, Liang Z, Liu S, Kioko EN, Huang Z et al. 2024. Functional Anatomy of Split Compound Eyes of the Whirligig Beetles Dineutus mellyi (Coleoptera: Gyrinidae). *Insects*. https://doi.org/10.3390/insects15020122. opened, full text.
- Nakagawa T, Eguchi E 1994. Differences in flicker fusion frequencies of the five spectral photoreceptor types in the swallowtail butterfly's compound eye. *Zoological Science 11:759-762*. https://doi.org/10.5281/zenodo.16586680. opened, full text as Biodiversity Heritage Library OCR, read through the web tool.
- Narendra A, Ramirez-Esquivel F, Ribi WA 2016. Compound eye and ocellar structure for walking and flying modes of locomotion in the Australian ant, Camponotus consobrinus. *Scientific Reports*. https://doi.org/10.1038/srep22331. opened, full text.
- Nityananda V, Tarawneh G, Rosner R, Nicolas J, Crichton SOJ, Read JCA 2016. Insect stereopsis demonstrated using a 3D insect cinema. *Scientific Reports*. https://doi.org/10.1038/srep18718. opened, full text.
- Nityananda V, Tarawneh G, Henriksen S, Umeton D, Simmons A, Read JCA 2018. A Novel Form of Stereo Vision in the Praying Mantis. *Current Biology*. https://doi.org/10.1016/j.cub.2018.01.012. opened, abstract.
- Niven JE, Anderson JC, Laughlin SB 2007. Fly Photoreceptors Demonstrate Energy-Information Trade-Offs in Neural Coding. *PLoS Biology*. https://doi.org/10.1371/journal.pbio.0050116. opened, full text.
- Noor MAF, Parnell RS, Grant B 2008. A Reversible Color Polyphenism in American Peppered Moth (Biston betularia cognataria) Caterpillars. *PLoS ONE*. https://doi.org/10.1371/journal.pone.0003142. opened, full text.
- Nordström K, Bolzon DM, O’Carroll DC 2011. Spatial facilitation by a high-performance dragonfly target-detecting neuron. *Biology Letters*. https://doi.org/10.1098/rsbl.2010.1152. opened, full text.
- Ogawa Y, Falkowski M, Narendra A, Zeil J, Hemmi JM 2015. Three spectrally distinct photoreceptors in diurnal and nocturnal Australian ants. *Proceedings of the Royal Society B Biological Sciences*. https://doi.org/10.1098/rspb.2015.0673. opened, abstract.
- Ogawa Y, Narendra A, Hemmi JM 2022. Nocturnal Myrmecia ants have faster temporal resolution at low light levels but lower adaptability compared to diurnal relatives. *iScience 25:104134*. https://doi.org/10.1016/j.isci.2022.104134. opened, abstract.
- Para F 2026. Slow or Fast Eyes: Associations Between Critical Flicker Fusion Frequency and Anti-Predator Strategy in Lepidopterans. *MSc thesis, Carleton University*. https://doi.org/10.22215/etd/2026-16964. opened, abstract.
- Poteser M, Kral K 1995. Visual Distance Discrimination Between Stationary Targets in Praying Mantis: an Index of the Use of Motion Parallax. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.198.10.2127. opened, abstract.
- Reisenman CE, Insausti T, Lazzari CR 2002. Light-induced and circadian changes in the compound eye of the haematophagous bug Triatoma infestans (Hemiptera: Reduviidae). *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.205.2.201. opened, abstract.
- Rind FC, Santer RD, Wright GA 2008. Arousal Facilitates Collision Avoidance Mediated by a Looming Sensitive Visual Neuron in a Flying Locust. *Journal of Neurophysiology*. https://doi.org/10.1152/jn.01055.2007. opened, abstract.
- Robert D 1989. The Auditory Behaviour of Flying Locusts. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.147.1.279. opened, abstract.
- Rossel S 1986. Binocular Spatial Localization in the Praying Mantis. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.120.1.265. opened, abstract.
- Ruck P 1961. Electrophysiology of the Insect Dorsal Ocellus. *The Journal of General Physiology*. https://doi.org/10.1085/jgp.44.3.641. opened, abstract.
- Rutowski RL, McCoy L, Demlong MJ 2001. VISUAL MATE DETECTION IN A TERRITORIAL MALE BUTTERFLY (ASTEROCAMPA LEILIA): EFFECTS OF DISTANCE AND PERCH LOCATION. *Behaviour*. https://doi.org/10.1163/156853901750077772. opened, abstract.
- Schlotterer G 1977. Response of the locust descending movement detector neuron to rapidly approaching and withdrawing visual stimuli. *Canadian Journal of Zoology*. https://doi.org/10.1139/z77-179. opened, abstract.
- Schul J, Patterson AC 2002. What determines the tuning of hearing organs and the frequency of calls? A comparative study in the katydid genusNeoconocephalus(Orthoptera, Tettigoniidae). *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.00070. opened, abstract.
- Schwarz MB, O'Carroll DC, Evans BJE, Fabian JM, Wiederman SD 2024. Localized and Long-Lasting Adaptation in Dragonfly Target-Detecting Neurons. *eNeuro*. https://doi.org/10.1523/eneuro.0036-24.2024. opened, full text.
- Sharkey CR, Fujimoto M, Lord NP, Shin S, McKenna DD, Suvorov A et al. 2017. Overcoming the loss of blue sensitivity through opsin duplication in the largest animal group, beetles. *Scientific Reports*. https://doi.org/10.1038/s41598-017-00061-7. opened, full text.
- Sherk TE 1978. Development of the compound eyes of dragonflies (odonata). III. Adult compound eyes. *Journal of Experimental Zoology*. https://doi.org/10.1002/jez.1402030107. opened, abstract.
- Smith RA (Duke University), summarizing Caves EM, Brandley NC, Johnsen S 2018. Details that look sharp to people may be blurry to their pets. *Duke Today, 30 May 2018 (summary of Trends in Ecology and Evolution 2018, doi 10.1016/j.tree.2018.03.001)*. https://today.duke.edu/2018/05/details-look-sharp-people-may-be-blurry-their-pets. secondary: popular summary of Caves, Brandley and Johnsen 2018 (Trends Ecol Evol), read through the web tool.
- Sontag C 1971. Spectral Sensitivity Studies on the Visual System of the Praying Mantis, Tenodera sinensis. *The Journal of General Physiology*. https://doi.org/10.1085/jgp.57.1.93. opened, abstract.
- Sponberg S, Dyhr JP, Hall RW, Daniel TL 2015. Luminance-dependent visual processing enables moth flight in low light. *Science*. https://doi.org/10.1126/science.aaa3042. opened, abstract.
- Stalleicken J, Mukhida M, Labhart T, Wehner R, Frost BJ, Mouritsen H 2005. Do monarch butterflies use polarized skylight for migratory orientation?. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.01613. opened, abstract.
- Stange G, Howard J 1979. An Ocellar Dorsal Light Response in A Dragonfly. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.83.1.351. opened, abstract.
- Stöckl A, O'Carroll D, Warrant EJ 2017. Higher-order neural processing tunes motion neurons to visual ecology in three species of hawkmoths. *Proceedings of the Royal Society B Biological Sciences*. https://doi.org/10.1098/rspb.2017.0880. opened, abstract.
- Stöckl A, O’Carroll DC, Warrant EJ 2020. Hawkmoth lamina monopolar cells act as dynamic spatial filters to optimize vision at different light levels. *Science Advances*. https://doi.org/10.1126/sciadv.aaz8645. opened, full text.
- Takeuchi Y, Arikawa K, Kinoshita M 2006. Color discrimination at the spatial resolution limit in a swallowtail butterfly, Papilio xuthus. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.02311. opened, abstract.
- ter Hofstede HM, Ratcliffe JM 2016. Evolutionary escalation: the bat-moth arms race. *Journal of Experimental Biology 219(11)*. https://doi.org/10.1242/jeb.086686. opened, abstract.
- Theobald JC, Warrant EJ, O’Carroll DC 2009. Wide-field motion tuning in nocturnal hawkmoths. *Proceedings of the Royal Society B Biological Sciences*. https://doi.org/10.1098/rspb.2009.1677. opened, abstract.
- Traniello JFA 1977. Recruitment behavior, orientation, and the organization of foraging in the carpenter ant Camponotus pennsylvanicus DeGeer (Hymenoptera: Formicidae). *Behavioral Ecology and Sociobiology 2:61-79*. https://doi.org/10.1007/BF00299289. opened, abstract.
- van der Kooi CJ, Stavenga DG, Arikawa K, Belušič G, Kelber A 2021. Evolution of insect color vision: from spectral sensitivity to visual ecology. *Annual Review of Entomology 66:435-461*. https://doi.org/10.1146/annurev-ento-061720-071644. opened, owner's library (paywalled; quoted at most 40 words).
- Van Kleef JP, James AC, Stange G 2005. A Spatiotemporal White Noise Analysis of Photoreceptor Responses to UV and Green Light in the Dragonfly Median Ocellus. *The Journal of General Physiology*. https://doi.org/10.1085/jgp.200509319. opened, full text.
- Virant‐Doberlet M, Čokl A 2004. Vibrational communication in insects. *Neotropical Entomology*. https://doi.org/10.1590/s1519-566x2004000200001. opened, abstract.
- Wallace GK 1959. Visual Scanning in the Desert Locust Schistocerca Gregaria Forskål. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.36.3.512. opened, abstract.
- Wan G, Hayden AN, Iiams SE, Merlin C 2021. Cryptochrome 1 mediates light-dependent inclination magnetosensing in monarch butterflies. *Nature Communications*. https://doi.org/10.1038/s41467-021-21002-z. opened, full text.
- Ward PS, Downie DA 2005. The ant subfamily Pseudomyrmecinae (Hymenoptera: Formicidae): phylogeny and evolution of big‐eyed arboreal ants. *Systematic Entomology*. https://doi.org/10.1111/j.1365-3113.2004.00281.x. opened, abstract.
- Wardill TJ, Fabian ST, Pettigrew AC, Stavenga DG, Nordström K, Gonzalez-Bellido PT 2017. A Novel Interception Strategy in a Miniature Robber Fly with Extreme Visual Acuity. *Current Biology*. https://doi.org/10.1016/j.cub.2017.01.050. opened, full text.
- Warrant EJ, Bartsch K, Günther C 1999. Physiological optics in the hummingbird hawkmoth: a compound eye without ommatidia. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.202.5.497. opened, abstract.
- Warrant EJ, Dacke M 2010. Vision and Visual Navigation in Nocturnal Insects. *Annual Review of Entomology*. https://doi.org/10.1146/annurev-ento-120709-144852. opened, abstract.
- Warrant EJ 2017. The remarkable visual capacities of nocturnal insects: vision at the limits with small eyes and tiny brains. *Philosophical Transactions of the Royal Society B Biological Sciences*. https://doi.org/10.1098/rstb.2016.0063. opened, abstract.
- Warrant EJ, Somanathan H 2022. Colour vision in nocturnal insects. *Philosophical Transactions of the Royal Society B Biological Sciences*. https://doi.org/10.1098/rstb.2021.0285. opened, full text.
- Wehner R, Michel B, Antonsen P 1996. Visual Navigation in Insects: Coupling of Egocentric and Geocentric Information. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.199.1.129. opened, abstract.
- Wehner R 1997. The ant’s celestial compass system: spectral and polarization channels. *Birkhäuser Basel eBooks*. https://doi.org/10.1007/978-3-0348-8878-3_6. opened, abstract.
- White RH, Xu H, Münch TA, Bennett RR, Grable EA 2003. The retina ofManduca sexta: rhodopsin expression, the mosaic of green-, blue- and UV-sensitive photoreceptors, and regional specialization. *Journal of Experimental Biology*. https://doi.org/10.1242/jeb.00571. opened, abstract.
- Wiederman SD, Fabian JM, Dunbier JR, O’Carroll DC 2017. A predictive focus of gain modulation encodes target trajectories in insect vision. *eLife*. https://doi.org/10.7554/elife.26478. opened, abstract.
- Yager DD, Hoy RR 1986. The Cyclopean Ear: A New Sense for the Praying Mantis. *Science*. https://doi.org/10.1126/science.3945806. opened, abstract.
- Zhao A, Gruntman E, Nern A, Iyer N, Rogers EM, Koskela S et al. 2025. Eye structure shapes neuron function in Drosophila motion vision. *Nature*. https://doi.org/10.1038/s41586-025-09276-5. opened, full text.
- Ziemba KS, Rutowski RL 2000. Sexual Dimorphism in Eye Morphology in a Butterfly (Asterocampa leilia; Lepidoptera, Nymphalidae). *Psyche A Journal of Entomology*. https://doi.org/10.1155/2000/54503. opened, abstract.
- Zorović M 2011. Temporal Processing of Vibratory Communication Signals at the Level of Ascending Interneurons in Nezara viridula (Hemiptera: Pentatomidae). *PLoS ONE*. https://doi.org/10.1371/journal.pone.0026843. opened, abstract.

## 8. Questions for a specialist

1. Which acceptance angles and how much summation apply to the most photographed moths (erebids, noctuids, geometrids), as against hawkmoths?
2. Has a whole-head field of view been measured for any butterfly, dragonfly or mantis?
3. Do ladybirds and leaf beetles have a working blue class, which would make the most photographed beetles trichromats?
4. What flicker fusion frequencies have been measured for dragonfly compound eyes and for ordinary beetles?
5. How many ommatidia does a Red Imported Fire Ant worker have, and does *Solenopsis invicta* share the 620 nm class of *S. saevissima*?
6. What do lepidopteran stemmata resolve, and could photos of caterpillars be told from adults reliably enough to give them a view?

## Unfinished

- The life-stage share of Lepidoptera records (caterpillar photos) is uncounted.
- Phone ultraviolet response (Igoe, Parisi and Carter 2012, cited by the crab sheet) was not opened.
- Drive arrivals after this session started were checked at the end; see the commit message of the last push.
