# Sensing sheet: octopus, squid, crab, starfish and other sea invertebrates (round 3)

Unit `sea-invertebrates`, covering the app's groups `cephalopod` ('an octopus or squid'), `sealife` ('a sea creature') and `crab` ('a crustacean'), none of which has a view in build 22. Started 13 October 2026 at 01:47 UTC. It builds on the earlier sheets `docs/views/sheets/sealife.md` and `docs/views/sheets/crab.md` and their audits.

**What was read.** The literature collection on `pub/lit-t1`, topics `cephalopods`, `sea-life` and `crustaceans` (with `snails-molluscs` for neighbours), titles and abstracts first and then the full texts on disk. From the owner's library: Land and Nilsson, *Animal Eyes*, 2nd edition (2012), of which the front matter, chapters 1 and 2, and chapter 3 to about page 65 came through (chapters 4 to 9 did not), and, from the search for new arrivals, Caves, Brandley and Johnsen (2018), read in full. On the web: publisher, repository and university pages for abstracts and a few full texts. Europe PMC answered with HTTP 429 at 02:01 UTC, and I stopped using it.

**How to read the references.** `L12` means line 12 of `docs/views/evidence/sea-invertebrates.jsonl` (278 lines). Every row and every number below names the lines behind it. Record counts are iNaturalist research-grade records in GBIF, from `docs/views/world-orders.csv` (read 11 October 2026) and from GBIF facets I fetched in this session (section 7).

## 1. Scope

### What the three groups hold

**`cephalopod`, 60,462 records.** Octopuses (Octopoda) 29,175 (48.3%), cuttlefish (Sepiida) 19,535 (32.3%), squids 11,517 (19.0%: Myopsida 8,162, the ram's horn squid Spirulida 2,464, Oegopsida 688, pygmy squids Idiosepida 196, Bathyteuthida 2, and the vampire squid Vampyromorpha 5), nautiluses (Nautilida) 235 (0.4%).

**`sealife`, 1,467,704 records.** Clams, mussels and scallops 506,098 (34.5%); jellyfish, corals and anemones 411,623 (28.0%); starfish, urchins and sea cucumbers 401,633 (27.4%); sponges 72,180 (4.9%); sea squirts and lancelets 48,280 (3.3%); moss animals and lamp shells 20,705 (1.4%); comb jellies 7,185 (0.5%).

**`crab`, 1,232,045 records.** Decapods 743,220 (60.3%); woodlice and other isopods 380,509 (30.9%); acorn barnacles 36,997 (3.0%); goose barnacles 23,129 (1.9%); horseshoe crabs 21,193 (1.7%); amphipods 12,269 (1.0%); mantis shrimp 4,493 (0.4%); all others 10,235 (0.8%: fairy shrimp 2,582, water fleas and clam shrimp 2,239, tadpole shrimp 1,638, copepods, ostracods, mysids, krill, sea spiders 651 and smaller groups).

**Alachua County, Florida** (`docs/views/no-view-us-fl-alachua.csv`). Woodlice hold 166 records in seven species (Common Pill Woodlouse 91, Florida Fast Woodlouse 40, Oak Woodlouse 17, Little Pill Woodlouse 14 and three with one or two), with one amphipod record (Hobb's Cave Amphipod). Decapods hold 26, all freshwater: crayfish 22 (White Tubercled 9, Slough 4, Peninsula 3, Pallid Cave 3, Spider Cave 2, Everglades 1) and river shrimps 4 (Eastern Grass Shrimp 3, Bigclaw River Shrimp 1). Freshwater bivalves hold 38 (Asian Clam 14, Florida Spike 11, Paper Pondshell 4 and six mussels with one or two) and the Magnificent Bryozoan 4. No octopus, crab, starfish, jellyfish, scallop or horseshoe crab appears in the county's list.

### Where the views should split

The three groups hold animals with no eyes at all, animals whose eyes resolve only a few degrees, and the octopus, whose camera eye resolves detail of a degree or finer (L44, L46). One picture per group would be false for most of each group. These are the lines, with the evidence and the record shares.

**1. Cephalopods stay together, with settings by order.** Octopuses, cuttlefish and squid share a camera eye with one visual pigment (L2, L37, L38, L65, L81), a horizontal band of dense receptors set on the horizon (L42, L121, L125), polarization vision over the whole field (L66, L122) and the same broad range of behavioural acuity (L44, L46, L94, L127). They differ in pupil shape: a level slit in octopuses (L55, L56, L97), a W in cuttlefish (L101, L102) and a crescent or U in coastal squid (L96, L134). The pupil shapes out-of-focus blur, so the view takes its pupil from the order: octopus 48.3% of the group, cuttlefish 32.3%, squids 19.0%. Only cuttlefish are known to use two eyes for distance (L77, L78, L79), which the view leaves out for all of them.

**2. The nautilus differs enough to need its own settings** (235 records, 0.4%). Its eye is a pinhole with no lens (L107), resolving 5 to 11 degrees (L105) against about 0.3 to 1 degree in octopuses and cuttlefish (L44, L127, L129), with no band of dense receptors (L106) and a pupil that takes about 90 seconds to close (L58, L110) against 0.3 to 3 seconds in the others (L57). The octopus picture would be about thirty times too sharp for it.

**3. Within `sealife`, most animals have no image, and two kinds do.**
- **No picture, `sealife`: 1,075,142 records (73.3% of the group).** Eyeless or nearly so: anemones and corals (L211, L210), sponges and comb jellies (L25), adult sea squirts (L26), sea cucumbers (L229, L230), clams, mussels and oysters without eyes on the shell edge (438,521 records, which also hold cockles and file clams, whose eyes no source I opened describes), brittle stars and feather stars, moss animals and lamp shells. The jellyfish with simple eye cups ride here too (L202, L204). Barnacles from the crab group (60,126 records) join this picture, since their few eyes serve a shadow reflex (L143 to L146).
- **Coarse images, `starfish`: 324,985 records (22.1%).** Starfish (220,261, 15.0%) have a compound eye at each arm tip resolving 8 to 16 degrees (L216, L272, L273), and sea urchins (104,724, 7.1%) see shapes 10 degrees or wider through light-sensing cells shaded by the skeleton (L224, L269, L270), so both form a picture of a few patches. Urchins are coarser, from 10 to 45 degrees (L225, L226, L269), and take a setting of their own.
- **Many eyes that watch for movement, `scallop`: 67,577 records (4.6%).** Scallops (Pectinidae 33,463, 2.3%) have up to 200 mirror eyes resolving about 2 degrees (L233, L234, L235), ark clams (Arcidae 22,549, 1.5%) have tiny compound eyes on the shell edge that act as motion alarms (L27, L237), and giant clams (*Tridacna* 11,565, 0.8%) have several hundred pinhole eyes (L238, L239). All three respond to movement or dimming (L231, L237, L239), and drawing them with no picture would be false.
- **Box jellyfish** (Carybdeida 648 and Chirodropida 381, together 1,029 records, 0.07%) have lens eyes resolving about 10 to 15 degrees (L28, L199). The share is too small for a view, so they take settings of their own inside `sealife` (section 2.7).

**4. Within `crab`, the decapods split by eye design.** True crabs (Eubrachyura) keep the apposition eyes of their larvae, while shrimps, lobsters, crayfish and anomurans (hermit crabs and their allies) have reflecting superposition, or "mirror", eyes (L258, L256, L139). The two kinds differ in what the view draws. A fiddler crab resolves about 0.4 cycles per degree (L172), while three cleaner shrimps resolve 8 to 11 degrees, about 0.05 cycles per degree (L250), and mirror eyes can be far more sensitive in dim light (L271). Their flicker fusion is about the same once both are dark-adapted, 34 to 40 a second (L179, L252), and the shrimps' pace in bright light is not in the sources I opened. Of decapod records, true crabs hold 430,786 (58.0%), mirror-eyed decapods 256,120 (34.5%) and unplaced families 56,314 (7.6%).
- **`crab`: 435,279 records (35.3% of the group)**, the true crabs (430,786) and the mantis shrimp (4,493). The largest true-crab families are Grapsidae 76,044, Ocypodidae (fiddler and ghost crabs) 59,350, Cancridae 51,284, Varunidae 41,817, Portunidae 36,358, Carcinidae 35,458 and Epialtidae 23,609. Fiddler and ghost crabs, 13.8% of true-crab records, take a setting with the horizon band (L174, L175, L176). Mantis shrimp have apposition eyes with a band of twelve kinds of colour-sensing cells (L16, L147) and take a setting of their own (1.0% of the view).
- **`shrimp`: 256,120 records (20.8%)**, the mirror-eyed decapods: anomurans 124,947 (10.1%; hermit crabs Paguridae 38,710, Diogenidae 32,504 and Coenobitidae 25,265, with porcelain crabs, squat lobsters, king crabs and mole crabs), crayfish 62,343 (5.1%; Cambaridae 45,147), shrimps 48,263 (3.9%; Palaemonidae 24,470, Stenopodidae 4,965, Hippolytidae 3,052, Crangonidae 2,919, Alpheidae 2,286, Atyidae 1,941, Penaeidae 1,719, Rhynchocinetidae 1,166 and the cleaner shrimps), and lobsters 20,567 (1.7%; Palinuridae 16,117, Nephropidae 4,450). Crayfish take a yellower colour setting (L253).
- **Unplaced decapods: 56,314 records (4.6%).** These are 13,266 records in families too small for the facet I read and 43,048 in families I could not name in this session. Until they are placed they follow the crab view, since true crabs hold most named decapod records. **[unfinished]**
- **`woodlouse`: 392,778 records (31.9%)**, isopods 380,509 and amphipods 12,269. Woodlice have about twenty facets to an eye (L135) and the amphipod *Parhyale* about fifty (L142), against about a thousand in a horseshoe crab (L190). Both are apposition eyes (L137).
- **`horseshoe`: 21,193 records (1.7%).** About a thousand facets per eye, average resolution 0.1 cycles per degree, one green pigment in the side eyes and a clock that raises sensitivity up to 100,000 times at night (L187, L188, L190, L266). Its eye is the source of much of what is known about lateral inhibition (L155, L156, L268), which the view can draw. The share is small; the view is proposed because the measurements are complete enough to draw it well.
- **Barnacles, 60,126 records (4.9%),** go to the `sealife` picture, as above.
- **All others, 10,235 records (0.8%),** keep `other` until measured.

**Alachua County** falls almost entirely on two views. The 167 woodlouse and amphipod records go to `woodlouse`, all 26 decapods (crayfish and river shrimps) to `shrimp`, and the 42 bivalve and bryozoan records to `sealife`. Five of the crayfish records are cave crayfish, whose eyes no source I opened describes (section 5).

**Routing.** The group head names the group, as now. Within a group the view comes from the order or family when the species database names it: Nautilida to the nautilus setting; Asteroidea and Echinoidea to `starfish`; Pectinidae, Arcidae and *Tridacna* to `scallop`; Cubozoa to the box jellyfish setting; the mirror-eyed decapod families to `shrimp`; Isopoda and Amphipoda to `woodlouse`; Xiphosurida to `horseshoe`; Sessilia and Pedunculata to `sealife`. Three of the new views (`starfish`, `woodlouse`, `shrimp`) each hold more than 250,000 records and could carry their own labels for the group head.

**The views proposed:** `cephalopod` (with octopus, cuttlefish, squid and nautilus settings), `sealife` (with a box jellyfish setting), `starfish` (with an urchin setting), `scallop` (with ark clam and giant clam settings), `crab` (with fiddler crab and mantis shrimp settings), `shrimp` (with a crayfish setting), `woodlouse` and `horseshoe`.

## 2. The views

### 2.1 `cephalopod`: octopuses, cuttlefish and squid

#### Rows

`['m', 'Colour', 'Octopuses, cuttlefish and most squid have one kind of colour-sensing cell, where people have three. Trained octopuses quickly learned bright from dark, yet failed to tell yellow or violet from a grey of the same brightness. This view is grey.']`
Log: L2, L3, L37, L38, L65, L81, L82, L83, L84, L103, L104. The firefly squid, a deep-sea species, is the known exception, with three visual pigments (L4, L5, L6, L63).

`['m', 'A sharp band', 'An octopus, cuttlefish or squid packs its light-sensing cells most densely in a band across the eye, set where the horizon of its home falls. In the common octopus the band holds about two and a half to three times as many cells to the square millimetre as the rest of the retina. This view is sharpest in a level band across the middle of the screen.']`
Log: L42, L121, L125.

`['m', 'Pupil', 'In bright light an octopus closes its pupil to a level slit, and balance organs beside the brain turn the eye so that the slit stays level when the animal tilts. A cuttlefish closes its pupil to a W shape that shades the bright water above. This view shapes its blur to match, smearing sideways for an octopus and up and down for a cuttlefish.']`
Log: L55, L56, L57, L75, L97, L101, L102, L120, L134.

`['m', 'Sharpness', 'In behaviour tests, octopuses saw detail between a ninth and a thirty-fifth as fine as people do, and the largest cuttlefish tested about a seventieth. Young cuttlefish and squid see more sharply as they grow. This view is about a thirtieth as sharp as your eyes.']`
Log: L44, L45, L46, L109, L129, L127, L133, L94, L95, L126, L130, L247. The anatomical limit of the octopus eye is far finer, about 46 cycles per degree (L31, L247), and the review behind L44 says the behavioural tests may have underestimated acuity.

`['m', 'All around', 'Each eye of a golden cuttlefish takes in about 250 degrees, so the two eyes together see the whole way around, with overlaps in front and behind. Young bigfin reef squid see about 320 degrees. This view squeezes 320 degrees into the screen.']`
Log: L123, L124, L93, L49. A review gives 177 degrees for one eye of the common cuttlefish (L51), which conflicts with L123; the row follows the primary measurement.

`['m', 'Speed', 'In very bright light an octopus eye follows a light flickering up to about 72 times a second, where people stop at about 60, and at a light ten thousand times dimmer only about 20 times. A reef squid has been measured at about 50. This view gives moving things a faint trail.']`
Log: L47, L48, L92.

`['x', 'Distance by two eyes', 'A hunting cuttlefish turns both eyes forward and judges the distance to its prey by comparing the two views, as people do. Octopuses and squid are not known to do this. This view leaves it out.']`
Log: L77, L78, L79, L80, L50, L124.

`['x', 'Polarized light', 'Octopuses and cuttlefish see the angle at which light waves vibrate, which people cannot, and they notice a change in that angle of about one degree. Cuttlefish show patterns on their skin that only an eye like this can see. This view leaves this sense out.']`
Log: L64, L66, L67, L54, L74, L115, L122, L21, L68, L91.

`['x', 'Light through the skin', 'Octopus skin and suckers carry the same light-sensing proteins as the eyes, and the nerves of an octopus arm fire when the arm is lit, most strongly by blue light. Squid carry these proteins in their fins and skin. This view leaves this sense out.']`
Log: L116, L117, L90.

`['x', 'Touch and scent', 'An octopus finds much of its food by feeling with its arms, and in the dark it can follow a trail of scent upstream to food. In one test octopuses chose food more by its chemical cues than by its look. This view leaves these senses out.']`
Log: L62, L118, L119.

`['x', 'Low sounds', 'Squid and octopuses sense low sounds with balance organs near the brain, which register the back-and-forth movement of water in a sound wave. One squid responded from about 30 to 500 vibrations a second, best between 100 and 200. This view leaves this sense out.']`
Log: L113, L114, L111, L112.

`['i', 'Colour from focus', 'This part of the view is a guess. It assumes that the odd pupils of octopuses and cuttlefish let one kind of colour-sensing cell sort colours, because each colour comes into focus at a slightly different depth in the eye, and no behaviour test has shown this. The view sweeps its focus slowly, so that reds, greens and blues sharpen in turn.']`
Log: L98, L99, L40, L41, L96, L39, L100. This row belongs only with the focus-sweep effect below, which is optional. A review of 2026 judged every proposed route to colour in cephalopods insufficient or weakly supported (L100), and the published objection (Gagnon and colleagues, 2016) is on the wanted list.

**Nautilus setting.** It replaces the rows "A sharp band", "Pupil", "Sharpness" and "All around" with this one, and keeps the rest.

`['m', 'Nautilus', 'A nautilus eye is an open cup with nothing inside to focus the light, and it works like a pinhole camera open to the sea, so its picture is dim and blurred. The narrowest stripes it can make out are about 5 to 11 degrees wide, and its pupil takes about 90 seconds to close. This view of a nautilus is heavily blurred and slow to adjust to light.']`
Log: L107, L105, L106, L110, L58, L35, L108, L88. One abstract gives the lower bound of the nautilus's acuity as 1.25 degrees and another 5.5 (noted in L105); the row follows the abstract with both bounds, and Muntz (2009) is on the wanted list to settle it.

#### The picture

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Octopus, cuttlefish, squid', 'an octopus or squid' | `who` is the existing `GROUPS` wording; the chip is the app's wording. |
| `fov` | 320 | **invented**. The two eyes together cover the whole circle (L123, L124) and young squid about 323 degrees (L93). The engine compresses the picture to about half scale. |
| `cpd` | 2 | **invented** within the measured range. Behavioural acuity runs from 0.88 cycles per degree in the largest cuttlefish (L127) through 1.7 or better in the common octopus (L44) and 2.01 in a young squid (L94) to 3.1 to 6.8 in two small octopuses (L46). 2 sits in the middle of the values for the commonest species. |
| `topoS`, `fall` | 1, 1.0 | `topoS` from the band (L42, L121, L125). `fall` is an **invented** mapping of a density ratio of 2.5 to 3 between band and periphery (L42), gentler than the deer's 2.2. |
| `pupil` | 'h' octopus; 'v' cuttlefish; 'o' squid | 'h' rests on L55, L56 and L97. 'v' is an **invented** mapping: the W pupil acts as vertical slits for the frontal and rear fields (L101). 'o' is **invented**, since the engine has no crescent shape (L96, L134). |
| `dof` | 6 | **invented**. The octopus focuses by moving its lens, and a large depth of focus is likely (L60), so the value is small. |
| `M` | [.05, .5, .45, .05, .5, .45, .05, .5, .45] | An **invented** mapping of one pigment peaking between 475 and 505 nm (L37, L82, L83, L84) onto the camera's red, green and blue. Equal rows make the picture grey (L3, L103, L104). |
| `persist` | .04 | **invented**, between 1/72 and 1/20 of a second (L47, L48), by the convention that gives the frog .15 for 7 a second. The 72 was measured at an extremely bright 4.5 million candelas per square metre (L47), and most scenes a phone films are, by my reading, far dimmer (no source opened gives scene brightness). |
| `rate` | unset | The eye is faster than ours only at the extreme brightness of L47. |
| `gain`, `fovea`, `topoA`, `sat`, `gate`, `sheen`, `uvBlue`, `noGreen`, `field`, `hold`, `thrust` | unset | No source compares these eyes with a person's in dim light, and the others have no basis. |
| `cue` | 'Hold the phone level and turn slowly. The sharp band stays on the horizon, and the world is grey.' | The app's wording, resting on the rows "A sharp band" and "Colour". |

**Nautilus setting:** `cpd` .06 (1 / (2 × 8) from L35, within 0.044 to 0.09 from L105), `topoS` unset (L106), `pupil` 'o' (**invented**), `dof` 0 (**invented**: a pinhole forms its blurred image without focusing, so nothing is sharper at one distance than another; no source opened states this), `M` as above with a bluer weighting [.05, .4, .55] repeated (**invented**, from 467 nm, L88), and the slow pupil effect below.

#### New effects

| Effect | What the person sees | Phone input | Difficulty | Beauty and truth |
|---|---|---|---|---|
| The level band and slit | The sharp band and the sideways smear stay level with the real horizon however the phone is tilted, as the octopus's balance organs keep its slit level (L55). | Device orientation (gravity vector), rotating the band and the blur kernel. | Easy: one rotation uniform for the band and for the blur's long axis. | The picture visibly rights itself against the hand, which is the behaviour itself. |
| Polarization, by an outside filter | With polarized sunglasses or a polarizing film held over the camera and turned, the view compares frames at different angles and shows where the angle of polarization changes as a pale shimmer (L64, L66). | The camera, with a filter the person supplies, and the gyroscope for the filter's turn. | Hard. It needs a per-pixel record of the brightest and dimmest values over a turn, and it works only with the filter. | Water surfaces, glass and leaves change visibly, and the shimmer is the information the octopus has and people lack. It must be labelled as needing the filter. |
| Focus sweep (with the `i` row) | Every few seconds the focus drifts, and red, green and blue sharpen at slightly different moments (L98, L99). | None. | Moderate: a per-channel blur offset driven by a slow oscillator. | Beautiful as a slow breathing of colour. It is a hypothesis, so it is off by default and carries the `i` row. |
| Pace from brightness | The trail lengthens as the scene darkens, from almost none in sun to about a twentieth of a second in shade (L47, L48). | The camera's own mean brightness. | Easy: `persist` driven by a smoothed exposure value. | The trail tells the person how dim the octopus finds the room. |
| The nautilus's slow pupil | When the light changes, the nautilus picture stays too bright or too dark for most of a minute and a half before it settles (L58, L110). | The camera's mean brightness. | Easy: an exposure correction with a time constant of tens of seconds. | Walking from shade into sun shows the delay directly. |

### 2.2 `crab`: true crabs, with fiddler crab and mantis shrimp settings

#### Rows

`['g', 'All around', 'A fiddler crab holds its eyes up on tall stalks above its body and sees the whole way around. This view squeezes the whole circle into the screen.']`
Log: L141. Graded `g` because it is shown in fiddler crabs and drawn for all crabs.

`['g', 'Sharpness', 'From side to side, the facets of a fiddler crab's eye point about 1.3 degrees apart, so it sees detail about a hundred-and-fiftieth as fine as people do. A rock crab's eye is about as coarse. This view keeps only large shapes.']`
Log: L172, L173, L32, L248.

`['g', 'Danger from above', 'A fiddler crab runs from moving things above its horizon and almost never from the same things below it. It tells a diving bird from a harmless flier by how fast the image moves, how high it is and how it flickers.']`
Log: L162, L163, L164.

`['g', 'Something coming closer', 'Crabs have nerve cells that fire as an object grows quickly in view, the way a predator does when it swoops. In one mud crab these cells signal the moment the object reaches 49 degrees across.']`
Log: L161, L170, L168.

`['m', 'Colour', 'Most light-sensing cells in a crab's eye share one pigment, most sensitive to blue-green light between about 500 and 530 nanometres, and a small cell beside them is tuned to violet or ultraviolet. Female fiddler crabs still pick a yellow claw over a grey claw of any brightness. This view darkens reds and keeps blues and yellows.']`
Log: L184, L13, L14, L140, L185.

`['m', 'Speed', 'In daylight a fiddler crab's eye follows a light flickering up to about 74 times a second, where people stop at about 60. Once the eye has adapted to the dark, it follows only about 35 to 40. This view runs slightly slowly and then jumps ahead to suggest the difference.']`
Log: L177, L178, L179.

`['m', 'Night', 'At night the light-catching core of each facet in a fiddler crab's eye widens, which makes the eye about seven times more sensitive and its picture blurrier. A dark-adapted fiddler crab's eye answers at night to light about a thousand times dimmer than it does by day.']`
Log: L165, L180. The paper behind L180 gives about 1,000 times in its Results and 45,000 times in its Discussion; the row follows the Results, as the earlier sheet did.

`['m', 'The horizon band', 'Along the horizon, a fiddler crab's eye samples up-and-down detail about five times more finely than side-to-side detail, and the fine sampling falls away steeply above and below. This view draws that band for fiddler and ghost crabs.']`
Log: L174, L175, L176, L173.

`['x', 'Polarized light', 'A fiddler crab notices a change of about 3 degrees in the angle at which light waves vibrate, and it sees movement that shows only in polarized light, such as a bird crossing the polarized sky. This view leaves this sense out.']`
Log: L183, L69, L166, L167, L154, L91.

`['m', 'Mantis shrimp', 'A mantis shrimp has twelve kinds of colour-sensing cells, from ultraviolet to deep red, where people have three, yet it tells close colours apart poorly. Its eyes sweep a narrow band of special facets across what it looks at, and it recognizes colours from that sweep. This view of a mantis shrimp shows colour only in a narrow band that sweeps slowly up and down.']`
Log: L16, L15, L147, L181, L182, L148, L149, L150, L261, L262. Shown only for mantis shrimp.

`['x', 'Twisting light', 'A mantis shrimp also sees circularly polarized light, whose angle twists as it travels, and males reflect it from their tails in display. This view leaves it out.']`
Log: L18, L19, L20, L152, L153, L70. Shown only for mantis shrimp.

#### The picture

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Crab, mantis shrimp', 'a crab' | The app's wording. |
| `fov` | 360 | **invented**. The stalked eyes give a panoramic view (L141) without a number. |
| `cpd` | .4 | 0.39 cycles per degree horizontally in *Uca lactea annulipes* (L172), 0.33 in a rock crab (L32), and up to 0.4 across 96 decapods (L248). |
| `topoS`, `fall` | unset; fiddler setting 1, 2.0 | The band is measured in fiddler crabs (L174, L175, L176), so only Ocypodidae get it. `fall` 2.0 is an **invented** mapping of the fivefold ratio (L174). Which other families have the band is the first item on the wanted list. |
| `pupil` | 'none' | **invented**. No source describes a pupil. |
| `M` | PROTAN | An **invented** mapping: one main pigment at 500 to 530 nm (L184, L140) and a violet cell (L13, L14), so reds darken. Screening pigment can shift fiddler crabs toward longer wavelengths (noted in L184), so reds may darken less than drawn. |
| `rate` | .8 | 60 / 73.6 = 0.82 (L177), light-adapted by day. |
| `gain`, `persist`, `sheen` | unset | The night figures compare the eye with itself by day (L165, L180). The earlier sheet's ultraviolet sheen rested on a paper this session could not reopen (section 3). |
| `cue` | 'Hold the phone low, just above the sand or mud, and turn slowly. A crab sees the whole way around at once.' | The earlier sheet's wording, resting on "All around". |

**Mantis shrimp setting:** `M` unset and `sat` 1 inside the sweeping band, `sat` 0 outside it (**invented**, from L148, L149 and L182); `rate`, `cpd` and `fov` as for crabs (**invented**; no acuity or flicker figure was opened).

#### New effects

| Effect | What the person sees | Phone input | Difficulty | Beauty and truth |
|---|---|---|---|---|
| Danger above the horizon | Anything moving above the screen's midline flickers with a faint pulse of contrast; the same movement below it stays quiet (L162, L163). | Device orientation, to place the horizon, and the motion-salience map. | Moderate: the salience map masked by a horizon line from the gravity vector. | It shows the crab's sorting of the world in two, sky and ground, which a person can test by waving a hand above and below. |
| Looming flinch | When something grows fast in the picture and passes about 49 degrees, the view jolts and darkens for an instant (L161, L170). | The camera's optical flow (expansion). | Moderate: divergence of the flow field, thresholded. | Moving the phone toward an object triggers it, which is the response the neurons give. |
| Night widening | After dark by the phone's clock, the picture brightens and blurs about twice as much (L165, L180). | The clock and the camera's exposure. | Easy. | The same street at night looks softer and brighter, as the measured eye is. |
| Mantis shrimp band | A horizontal strip about a tenth of the screen tall, in saturated colour broken into twelve flat steps, sweeps slowly up and down over a grey picture (L16, L148, L149). | None. | Moderate: a moving mask and a hue quantizer. The scan speed is **invented** until Land and colleagues (1990) is read. | The barcode of colour moving across a grey world is the mantis shrimp's reported way of reading colour, made visible. |

### 2.3 `shrimp`: shrimps, crayfish, lobsters and hermit crabs

#### Rows

`['m', 'Mirror eyes', 'Shrimps, crayfish, lobsters and hermit crabs have eyes of square facets lined with mirrors, which bring light from many facets together onto each light-sensing cell. Eyes built this way can be far more sensitive than the eyes of true crabs, and a reflecting layer behind the cells makes them shine. This view is brighter in dim light than the crab view.']`
Log: L256, L257, L258, L138, L139, L271.

`['m', 'Sharpness', 'Three cleaner shrimps resolve detail about 8 to 11 degrees across, which is coarse for compound eyes of their size. At that sharpness a shrimp can make out the outlines of large shapes, while the colour patterns of other shrimps blur away even at short range. This view keeps only broad outlines.']`
Log: L250, L278, L248.

`['m', 'Colour', 'Cleaner shrimps have a single kind of colour-sensing cell, most sensitive to green light near 520 to 530 nanometres, and lobsters are similar. A crayfish eye is most sensitive to yellow light near 570 nanometres. This view is grey, a little brighter in greens, and yellower for crayfish.']`
Log: L251, L254, L255, L253.

`['m', 'Speed', 'The dark-adapted eyes of cleaner shrimps follow a light flickering about 34 to 39 times a second, about as fast as a fiddler crab's eye in the dark. This view gives moving things a short trail in dim light.']`
Log: L252, L179.

`['m', 'Hermit crabs', 'A land hermit crab hides when a shape grows quickly toward it and ignores shapes that shrink or stay still. Hermit crabs of land and sea also pick out a threatening shape that shows only in polarized light.']`
Log: L160, L159.

`['x', 'Smell in air', 'Land hermit crabs smell well in air, and their brains are dominated by the centres that handle smell. This view leaves smell out.']`
Log: L171.

`['x', 'Touch in the dark', 'In the light, rusty crayfish lunge at and follow each other by sight, and in the dark they fight more by touch, tapping with their antennae and pushing with their claws. This view leaves touch out.']`
Log: L259.

`['x', 'Light in the tail', 'A crayfish has light-sensing nerve cells in its tail, which also take signals from touch hairs on the tail fan, and light makes those touch signals about seven times clearer. This view leaves this sense out.']`
Log: L260.

`['i', 'Field of view', 'This part of the view is a guess. It assumes that a shrimp or crayfish sees most of the way around, and it squeezes 300 degrees into the screen.']`
Log: none; no source I opened gives the field.

#### The picture

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Shrimp, crayfish, hermit crab', 'a shrimp or crayfish' | The app's wording. |
| `fov` | 300 | **invented** (the `i` row). |
| `cpd` | .05 | 1 / (2 × 8.3) = 0.06 to 1 / (2 × 11) = 0.045 (L250); the modelled perception (L278). Measured in three cleaner shrimps only; hermit crabs, crayfish and lobsters are not measured (section 5). |
| `pupil` | 'none' | **invented**. |
| `M` | [.15, .6, .25, .15, .6, .25, .15, .6, .25]; crayfish [.35, .55, .1, .35, .55, .1, .35, .55, .1] | **invented** mappings of one class at 518 to 533 nm (L251; lobsters 520 to 525, L254; Norway lobster 498, L255) and of the crayfish's peak near 570 nm (L253). Equal rows make the picture grey. |
| `gain` | 1.4 | **invented**. Superposition eyes can be far more sensitive than apposition eyes (L271), and no comparison with a human eye was found. |
| `persist` | unset; .03 in dim scenes | 1 / 36 = 0.028 (L252), by the frog's convention, applied only when the scene is dim through the pace-from-brightness effect (section 2.1), since the figure is for dark-adapted eyes. |
| `rate`, `topoS`, `fall`, `dof`, `sat` and the rest | unset | No source supports them. |
| `cue` | 'Hold the phone low and keep the light dim. Only broad outlines remain, in green and grey.' | The app's wording. |

#### New effects

| Effect | What the person sees | Phone input | Difficulty | Beauty and truth |
|---|---|---|---|---|
| Eyeshine | In dim light, bright points (lamps, reflections) bloom into soft halos, as light gathered from many facets spreads (L256, L257). | The camera's exposure. | Easy: a bloom pass weighted by darkness. | The halo is how a mirror eye trades sharpness for light, and it is pretty. The trade itself is my inference from the optics, unsourced in the log. |
| Hermit crab looming | As for the crab, a jolt when something grows fast in view (L160). | Optical flow. | Moderate (shared with `crab`). | Shared code, one behaviour measured in each group. |

### 2.4 `woodlouse`: woodlice, sandhoppers and scuds

#### Rows

`['m', 'Twenty facets', 'Each eye of the Common Pill Woodlouse and the Rough Woodlouse has only about twenty facets, set in four rows like a small bunch of grapes. A horseshoe crab's eye has about a thousand. This view keeps only a few soft patches of light and dark.']`
Log: L135, L136, L190, L137.

`['i', 'Sharpness', 'This part of the view is a guess. It assumes the twenty facets share the eye's field evenly, each taking in a patch about 25 degrees across, which in other animals is enough for steering and finding shelter. This view is about a three-thousandth as sharp as your eyes.']`
Log: L135, L29, L30, L142, L36.

`['g', 'Colour', 'The sea slater, a seashore relative of woodlice, has three kinds of colour-sensing cells, most sensitive to ultraviolet, blue and green. This view borrows them for woodlice, keeping blues and yellows faintly and darkening reds.']`
Log: L22, L23, L24.

`['m', 'Dark shelters', 'Woodlice turn away from light and head for dark shelters.']`
Log: L263.

`['m', 'Night', 'About six in ten Common Pill Woodlice are active at night, against nine in ten of Philoscia muscorum, the fourth most recorded woodlouse.']`
Log: L265. The rank is from the earlier sheet's GBIF facet.

`['g', 'Sandhoppers and scuds', 'The amphipod Parhyale, a small shore relative of woodlice, has about fifty facets to an eye. Amphipods share the woodlouse view.']`
Log: L142, L137.

`['x', 'Dry air', 'Woodlice shelter more when the air is dry, and huddled together they lose about half as much water as they do alone. This view leaves the sense of damp air out.']`
Log: L264.

#### The picture

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Woodlouse, pill bug', 'a woodlouse' | The earlier sheet's wording. |
| `cpd` | .02 | **invented**: 1 / (2 × 25), from about twenty facets (L135) spread over a field assumed to be about 125 degrees wide, within the 5 to 30 degrees that serve coarse tasks (L30). |
| `M` | PROTAN | An **invented** mapping of the sea slater's ultraviolet, blue and green cells (L22, L23, L24): without a red-sensitive cell, reds darken. |
| `sat` | .5 | **invented**. No colour test in a woodlouse was opened. |
| `fov` | 280 | **invented**. |
| `pupil` | 'none' | **invented**. |
| `field` | unset | The earlier sheet drew no image (`field: 1`). Twenty facets in four rows form a coarse image (L135, L136), so a few patches are kept. |
| `gain`, `persist`, `rate` and the rest | unset | No time constant, flicker or dim-light figure was found. |
| `cue` | 'Hold the phone close to the ground and turn it slowly. A woodlouse heads for the darker side.' | The earlier sheet's wording, resting on "Dark shelters". |

#### New effects

| Effect | What the person sees | Phone input | Difficulty | Beauty and truth |
|---|---|---|---|---|
| Twenty facets | The picture breaks into about twenty hexagons in four rows, each one flat shade, like the bunch of grapes in L135. | None. | Easy: the engine's hexagonal mosaic (`u_mosaic` in `cam.b.js`) with larger cells than it now allows (its largest cell is 0.058 of the frame, about seventeen across). | The count is measured, so the mosaic is the truest thing in the view, and it looks like the eye itself. |
| The dark side | The darker half of the frame is drawn calm and the brighter half slightly harsh and grainy, so the eye is drawn toward shelter (L263). | The camera's brightness map. | Easy. | **invented** as a picture of preference; it should stay subtle. |

### 2.5 `horseshoe`: horseshoe crabs

#### Rows

`['m', 'Eyes', 'Each compound eye on the side of a horseshoe crab's shell has about a thousand facets and takes in about 60 per cent of the half of the world on its side. It also has two small eyes on top of the shell and several simple eyes kept from its larva.']`
Log: L190, L191, L158.

`['m', 'Sharpness', 'On average a horseshoe crab sees detail about a six-hundredth as fine as people do, and about twice as fine toward the front and near the horizon. This view is sharpest in a band across the middle.']`
Log: L188, L189, L34.

`['m', 'Edges', 'Light falling on one facet of a horseshoe crab's eye quiets the nerve signals of its neighbours, which makes edges stand out. Much of what is known about this effect in all eyes came from work on the horseshoe crab. This view brightens the light side of each edge and darkens the dark side.']`
Log: L155, L156, L268.

`['m', 'Night', 'A clock in the horseshoe crab's brain changes the structure and working of its eyes each day, making them up to 100,000 times more sensitive at night. It finds mates by sight by day and by night. After dark by the phone's clock, this view brightens.']`
Log: L187, L157, L192.

`['m', 'Colour', 'The side eyes have one kind of light-sensing cell, most sensitive to green light near 520 nanometres, so a horseshoe crab sees no colour through them. This view is grey.']`
Log: L266, L12.

`['x', 'Ultraviolet', 'The two small eyes on top of the shell answer to ultraviolet light about 200 to 320 times more strongly than to visible light, and proteins that sense ultraviolet occur in all three kinds of its eyes. This view leaves ultraviolet out.']`
Log: L267, L186, L11.

#### The picture

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Horseshoe crab', 'a horseshoe crab' | The app's wording. |
| `cpd` | .1 | Average 0.1 cycles per degree (L188); 1 / (2 × 5.5) = 0.09 from the average angle between facets (L189). |
| `topoS`, `fall` | .5, .6 | An **invented** mapping of maxima of 0.22 to 0.23 near the horizon and in front (L188), about twice the average. |
| `M` | [.1, .65, .25, .1, .65, .25, .1, .65, .25] | An **invented** mapping of one class near 520 nm (L266); equal rows make the picture grey. |
| `fov` | 280 | **invented**. Each eye covers about 60% of the hemisphere on its side (L191). |
| `pupil` | 'none' | **invented**. |
| `gain` | unset | The 100,000-fold rise compares the eye at night with itself by day (L187). |
| `cue` | 'Hold the phone low and level, as if at the water's edge. Every edge glows on its bright side.' | The app's wording, resting on "Edges". |

#### New effects

| Effect | What the person sees | Phone input | Difficulty | Beauty and truth |
|---|---|---|---|---|
| Lateral inhibition | Every edge gets a bright fringe on its light side and a dark fringe on its dark side, and broad even areas flatten (L155, L156). | None. | Easy: a difference of two blurs (centre minus surround) added back to the picture. | It is the horseshoe crab's best-known contribution to science and makes a striking, graphic picture. The strength is **invented**. |
| The night clock | After local sunset the view brightens steadily over an hour and stays bright until dawn, whatever the light in the room (L187, L157). | The phone's clock (and location, for sunset, if offered). | Easy. | The view runs on the animal's time; a person opening it at midnight sees the change. The size of the lift is **invented**, since the 100,000 is relative to the same eye. |

### 2.6 `sealife`: corals, anemones, jellyfish, sponges, sea squirts, bivalves without eyes, sea cucumbers, brittle stars and barnacles

#### Rows

`['m', 'No picture', 'Sea anemones, sponges, comb jellies and adult sea squirts have no eyes, and corals and sea cucumbers sense light through cells and proteins spread through their bodies. This view keeps only how much light there is, its colour and the direction it comes from.']`
Log: L211, L25, L26, L246, L210, L207, L230.

`['m', 'Blue light', 'Reef corals respond most to blue light near 480 nanometres, and their polyps react to light as faint as moonlight. This view is weighted toward blue.']`
Log: L205, L206, L210.

`['x', 'Full moon', 'A reef coral makes more of one blue-light-sensing protein on full-moon nights, and moonlight is one of the signals that sets the few nights each year when corals spawn together. This view leaves the moon's calendar out.']`
Log: L207, L208.

`['m', 'A walking coral', 'One free-living mushroom coral walks toward blue light, moving up to about 22 centimetres in slow pulses of one to two hours. It walked toward white light far less often.']`
Log: L209.

`['m', 'Jellyfish', 'Many jellyfish have small eyes around the rim of the bell, from simple cups of light-sensing cells to small camera eyes. Young moon jellies pulse faster in light and spend more time on the lit side of a tank.']`
Log: L202, L204, L203.

`['g', 'Shadows', 'A surf clam has a nerve that senses light by itself, and when a shadow falls it fires a burst and the clam pulls in its siphon. Barnacles close their shells when a shadow passes over them. This view shows a passing shadow as a sudden dimming.']`
Log: L241, L143, L144, L145, L146.

`['g', 'Stinging cells', 'In Hydra and other relatives of jellyfish, the stinging cells fire more readily in dim blue light than in bright blue light.']`
Log: L212.

`['m', 'Sea cucumbers', 'A sea cucumber has no eyes, yet light-sensing cells in its tentacles, skin bumps and tube feet respond best to blue light near 460 nanometres.']`
Log: L229, L230.

`['x', 'Larvae that see', 'The swimming larvae of sponges and sea squirts have light-sensing cells that steer them, though the adults have none. A sponge larva steers with a ring of pigmented cells whose long hairs bend away from bright light. This view shows the world of the adult.']`
Log: L242, L243, L244, L26, L245.

`['i', 'Clams and mussels', 'This part of the view is a guess for clams, mussels and oysters without eyes on the shell edge. It assumes that, like the surf clam, they sense only light and shadow.']`
Log: L241. No source opened covers the eyeless bivalves as a whole.

`['i', 'Brittle stars and the rest', 'This part of the view is a guess for brittle stars, feather stars, moss animals, lamp shells and lancelets, which share it without measurements of their own. One brittle star with no eyes turns toward polarized light, so some of them may sense more than this view shows.']`
Log: L228. Sumner-Rooney and colleagues (2020), on the wanted list, would say whether brittle stars see shapes.

#### The picture

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Coral, anemone, jellyfish, clam', 'a sea creature' | The earlier sheet's wording; `who` matches `GROUPS`. |
| `field` | 1 | No image (L211, L25, L26, L230). In the engine it mixes in a very coarse level of the camera image, as for the plant. |
| `M` | [.05, .4, .55, .05, .4, .55, .05, .4, .55] | An **invented** mapping weighted to blue: corals 480 nm (L205) and 471 to 476 nm (L210), a sea cucumber 459 nm (L229), a sea squirt larva 505 nm (L244), with the surf clam's 540 nm (L241) as the green end. |
| `pupil` | 'none' | **invented**. |
| `persist`, `gate`, `sat` and the rest | unset | As in the earlier sheet: the shadow must stay visible, still light is kept, and `M` already makes the picture grey. |
| `cue` | 'This creature has no picture of the world. Pass your hand over the camera to cast a shadow.' | The app's wording, resting on "Shadows". The earlier cue began with two sentence fragments. |

#### New effects

| Effect | What the person sees | Phone input | Difficulty | Beauty and truth |
|---|---|---|---|---|
| Shadow flinch | A sudden dimming of more than about an eighth makes the field contract toward the centre and slowly reopen, as a clam's siphon or a barnacle's legs withdraw (L241, L144; the 12.3% threshold is a giant clam's, L240). | The camera's mean brightness. | Easy. | A hand passed over the phone gets an answer, which is the shadow reflex these animals share. The contraction is **invented** as a picture. |
| The moon | At night, the field takes a faint blue that grows toward the full moon and fades toward the new moon (L207, L208). | The date. | Easy: a lunar phase from the date. | **invented** as a picture; the calendar is measured in a coral. It makes the coral's month visible and is honest only if the row "Full moon" changes from `x` to `i`. |

### 2.7 Box jellyfish setting, inside `sealife`

Applied to Cubozoa (1,029 records). It replaces the rows above with these and keeps "Stinging cells".

`['m', 'Box jellyfish', 'A box jellyfish has 24 eyes, six on each of four sensory clubs, and two on each club are camera eyes that form an image. One of these always looks straight up, and through the water surface it sees the trees above and steers the jellyfish toward the edge of its mangrove lagoon. This view of a box jellyfish shows a blurred, grey picture.']`
Log: L195, L196, L198, L28.

`['m', 'Sharpness', 'The camera eyes of box jellyfish form their images slightly out of focus, so they resolve only about 10 to 15 degrees, which is enough to steer around obstacles. A box jellyfish that hunts at night follows a light flickering only about two and a half times a second.']`
Log: L199, L197, L200, L201.

`['m', 'Colour', 'Box jellyfish eyes have a single kind of light-sensing cell, most sensitive to blue-green light near 500 nanometres. This view is grey.']`
Log: L193, L194.

Picture: `cpd` .05 (1 / (2 × 10), L199), `sat` 0 (L194), `M` as for `sealife`, `persist` .4 (**invented** from 2.5 a second, L200, measured in the night-active *Copula sivickisi* only), `pupil` 'none' (**invented**), `field` unset. New effect, the upward eye: when the phone points up, the picture shows the sky and trees in a round window (the engine's round aperture, `u_shape` 0), and when it points level the window closes to a dim glow (L198). Phone input: device orientation. Difficulty: easy. It is the measured behaviour of one eye type, and looking up through it at real trees is the experience the animal uses to steer.

### 2.8 `starfish`: starfish and sea urchins

#### Rows

`['m', 'Eyes at the arm tips', 'A starfish has a small compound eye at the tip of each arm, with 10 to 300 facets depending on the kind. A crown-of-thorns starfish's eye has about 250 facets and looks out sideways over a field about 100 degrees wide and 30 high. This view shows the world through a wide, low window.']`
Log: L216, L274, L277, L218.

`['m', 'Sharpness', 'The facets of a crown-of-thorns starfish point about 8 degrees apart, and those of the blue sea star about 16. That is between a thousandth and a two-thousandth as fine as people see. This view keeps only a few soft patches of light and dark.']`
Log: L272, L273, L219.

`['m', 'Finding the reef', 'A blue sea star carried away from its reef walks back to it, while one without its eyes wanders. A crown-of-thorns starfish walks toward dark shapes 14 degrees across or wider, and not toward shapes of 7 degrees.']`
Log: L215, L275, L276, L222.

`['m', 'Grey and slow', 'The blue sea star is colour blind, and its eyes are slow. The eye of a crown-of-thorns starfish follows a light flickering no faster than once every two seconds, the slowest eye measured in any animal. This view is grey, and anything that moves leaves a long trail.']`
Log: L214, L217. The flicker figure comes through a later paper (L217).

`['m', 'Sea urchins', 'A sea urchin has no eyes, and its light-sensing cells sit in its tube feet, shaded by its shell and spines. A purple sea urchin turned toward a dark disc 10 degrees wide and ignored one 6.5 degrees wide, and a European urchin answered only to shapes at least 45 degrees across. This view of an urchin is coarser than the starfish view.']`
Log: L224, L269, L270, L225, L226.

`['m', 'Steering by light', 'In the light, a chocolate chip sea star walks fast in straight lines with its tube feet working in step, and in darkness it wanders slowly.']`
Log: L223.

`['x', 'Ultraviolet', 'A green sea urchin covers itself with shells and debris and seeks shade when ultraviolet light falls on it. This view leaves ultraviolet out.']`
Log: L227.

`['x', 'Every arm at once', 'A starfish looks out from the tip of every arm at the same time, in several directions. This view shows only the direction the camera faces.']`
Log: L216, L277.

#### The picture

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Starfish, sea urchin', 'a starfish or sea urchin' | The earlier sheet's wording. |
| `cpd` | .05; urchin setting .03 | **invented** between 1 / (2 × 8) = 0.06 (L272) and 1 / (2 × 16) = 0.03 (L273). Urchins: 0.045 to 0.06 in the purple sea urchin (L270), about 0.02 in a European urchin (L225) and 0.01 to 0.03 in *Diadema* (L226). |
| `sat` | 0 | Colour blind (L214). |
| `M` | [.05, .45, .5, .05, .45, .5, .05, .45, .5] | An **invented** mapping of a peak at 485 nm (L221). |
| `persist` | 2 | **invented**: 1 / 0.5 Hz (L217), by the frog's convention. The earlier sheet's .6 rested on a secondary 1 to 2 Hz. |
| aperture | a band about 100 by 30 degrees | The engine's horizontal band (`u_shape` 2 in `cam.b.js`), from L277 and L218. It needs a new `EYES` field to carry it. |
| `fov` | 300 | **invented**, as in the earlier sheet. |
| `pupil` | 'none' | **invented**. |
| `gate`, `field` and the rest | unset | Starfish and urchins steer toward still shapes (L275, L269), so still things stay. |
| `cue` | 'Hold the phone low and level, as a starfish holds the tip of an arm. Only large dark shapes remain, and they move slowly.' | The earlier sheet's wording. |

#### New effects

| Effect | What the person sees | Phone input | Difficulty | Beauty and truth |
|---|---|---|---|---|
| The low window | The picture shows through a soft-edged band three times wider than tall (L277). | None. | Easy; the shape exists. | The arm-tip eye's field, drawn to scale. |
| Two-second trail | A hand moved across the view leaves a ghost that takes seconds to fade (L217). | None. | Easy (`persist`). | The slowest eye measured, felt directly. |
| Every arm | Turning the phone around moves the window through five positions, as if passing from arm to arm, with a soft cut between them (L216). | Device orientation (compass heading). | Moderate. | **invented** as a picture; the five arms looking out at once are measured. |

### 2.9 `scallop`: scallops, ark clams and giant clams

#### Rows

`['m', 'Many eyes', 'A scallop has up to 200 small eyes along the edges of its shell, and a giant clam has several hundred on its mantle. Ark clams have tiny compound eyes on the shell edge.']`
Log: L233, L238, L27, L237.

`['m', 'Mirrors', 'Each scallop eye focuses light with a curved mirror at its back, tiled with square crystals, onto two separate retinas.']`
Log: L234, L233.

`['m', 'Sharpness', 'The eyes of a bay scallop resolve about 2 degrees, about a two-hundred-and-fortieth as fine as people, and the scallop opens its shell most for small particles drifting slowly past. A giant clam pulls in its mantle for a dark spot 13.5 degrees wide and ignores one 11.7 degrees wide.']`
Log: L235, L236, L231, L33, L239.

`['m', 'Only movement', 'A scallop's eyes answer to dimming and to dark shapes that move, and they stay silent for a still pattern. Ark clams close their shells when something moves nearby. This view draws only what moves.']`
Log: L231, L237.

`['m', 'Colour', 'The eyes of the bay scallop are most sensitive to blue-green light near 500 nanometres. This view is grey.']`
Log: L232.

`['x', 'Ultraviolet', 'Giant clams have three light-sensing pigments, peaking at 360, 490 and 540 nanometres, and the first lies in the ultraviolet. This view leaves the ultraviolet out.']`
Log: L7, L8, L9, L10.

`['x', 'Every edge at once', 'A scallop looks out from all its eyes at once, around the whole edge of its shell. This view shows only the direction the camera faces.']`
Log: L233.

#### The picture

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Scallop, ark clam, giant clam', 'a scallop or clam' | The app's wording. |
| `cpd` | .25; ark clam .017; giant clam .03 | 1 / (2 × 2) = 0.25 (L235; 1.6 degrees and 0.31 in *Pecten*, L33). Ark clams: about 30 degrees per ommatidium (L237), 1 / (2 × 30) = 0.017. Giant clam: acceptance 16.5 degrees (L240), 1 / (2 × 16.5) = 0.03. |
| `gate` | 1 | Only movement and dimming draw a response (L231, L237). |
| `sat` | 0 | **invented**: one peak near 500 nm is known (L232), and no colour test was found. |
| `M` | [.05, .5, .45, .05, .5, .45, .05, .5, .45] | An **invented** mapping of 500 nm (L232). |
| `fov` | 300 | **invented**: eyes all around the shell's edge (L233). |
| `pupil` | 'none' | **invented**. |
| `cue` | 'Hold the phone still. Only what moves appears, and it fades when it stops.' | The app's wording, resting on "Only movement". |

#### New effects

| Effect | What the person sees | Phone input | Difficulty | Beauty and truth |
|---|---|---|---|---|
| A row of eyes | The motion-only picture shows through a row of small overlapping round windows along the lower edge of the screen, each a little coarse and each lighting up as something moves across it (L233, L231). | None. | Moderate: a tiled aperture mask over the gated picture. | **invented** as a layout; the many eyes are measured. A moving hand passed along the row lights the windows one after another. |
| The snap shut | A large movement makes the windows close for half a second, as an ark clam closes its shell (L237). | Optical flow magnitude. | Easy. | The motion alarm, felt. The timing is **invented**. |

## 3. The earlier sheets re-checked

No `EYES` entry exists for these groups in build 22, so this section checks the rows and numbers the earlier sheets proposed (`sealife.md`, `crab.md`), against sources reopened in this session.

**`sealife.md`, view `sealife`.**
- "No picture" (`i`): **corrected** to `m`. Eyelessness is measured in an anemone (L211), sponges and comb jellies (L25) and adult sea squirts (L26).
- "Full moon": **confirmed** (L207, L208), and moved to an `x` row since the view does not draw the calendar.
- "The dark hour" (Lin and colleagues, 2021): **unsupported** in this session; the paper was not reopened, and the row is dropped.
- "Blue moonlight" (Grawunder and colleagues, 2015): **unsupported** in this session, since the paper was not reopened; replaced by "Blue light" from coral measurements (L205, L206, L210).
- "Shadows" (`g`): **confirmed** (L241), with barnacles added (L143 to L146).
- "Moon jellies": **corrected**. The light response is confirmed in juveniles of *Aurelia coerulea* (L204); the clause that animals without their eye cups no longer respond rested on a source not reopened and is dropped.
- "Scallops and giant clams" (`x`): **corrected**; they now have the `scallop` view (L231 to L240).
- "Box jellyfish" (`x`): **confirmed** (L195, L198, L28), now carried by the box jellyfish setting.
- Picture: `field` 1, `pupil` 'none' and `M` blue-grey are kept; the `M` now rests on coral and sea cucumber peaks measured in this session (L205, L210, L229). The cue is reworded to remove two sentence fragments.

**`sealife.md`, view `starfish`.**
- "Eyes at the arm tips" (`g`): **confirmed** and raised to `m` (L274, L277, L216).
- "Sharpness" (`g`, 8 degrees): **confirmed** (L272); the blue sea star's 16 degrees, which the audit had removed, is **restored** from a primary paper (L273).
- "Finding home" and "Shapes": **confirmed** (L215, L275) and merged into "Finding the reef".
- "Grey and slow": **corrected**. The flicker figure is 0.5 a second in the crown-of-thorns starfish (L217), against the earlier secondary 1 to 2 a second, and `persist` changes from .6 to 2.
- "Sea urchins": **confirmed** (L269, L270).
- "The whole body" (about 200,000 cells in the tube feet; adults crawl from blue light): the location of the cells is **confirmed** (L224); the count and the blue preference are **unsupported** in this session and dropped.
- "Every arm at once" (`x`): **confirmed** (L216, L277).
- "Sea cucumbers and brittle stars" (`i`): **corrected**. Sea cucumbers are now measured (L229, L230) and go to `sealife`, with brittle stars (L228).
- Picture: `cpd` .06 becomes .05 (with .03 for urchins); `sat` 0 **confirmed** (L214); `fov` 300 kept as invented; `M` added (L221).

**`crab.md`, view `crab`.**
- "All around" (`g`): **confirmed** (L141). Zeil and Hemmi (2006) was not reopened.
- "Sharpness" (`g`): **confirmed** (L172, L173).
- "The horizon" (`x`): the fiddler crab band is **confirmed** (L174, L175, L176) and now drawn for Ocypodidae. Its absence in Grapsidae, Xanthidae and Portunidae rests on Zeil, Nalbach and Nalbach (1986), **unsupported** in this session and first on the wanted list.
- "Colour": **confirmed** in fiddler crabs (L184, L185); the shore crab figures (Bruno and colleagues, 1973) and the ghost crab figure (Qian and Frank, 2024) are **unsupported** in this session.
- "Ultraviolet": **unsupported** in this session (Detto and Backwell, 2009, and Igoe and colleagues, 2012, were not reopened); the row and the `sheen` .5 are dropped until the paper is read.
- "Pace": **confirmed** (L177, L178, L179); `rate` .8 kept.
- "Night": **confirmed** (L180), with the paper's own inconsistency noted; a second measure added (L165).
- "Crayfish": **corrected**. Crayfish move to `shrimp`; their peak near 570 nm is **confirmed** (L253); the violet class (Eguchi and colleagues, 1973), the red swamp crayfish's two classes (Kingston and Cronin, 2015) and the slipper lobsters (Hayasaka and colleagues, 2022) are **unsupported** in this session.
- "Polarized light" (`x`): **confirmed** (L183); the statement about phone cameras had no source and is dropped.
- The split: the earlier `crab` view held all decapods and mantis shrimp (747,713 records). It is **corrected**: mirror-eyed decapods go to `shrimp` (L258, L256), on the strength of their eye design, acuity and flicker (L250, L252).

**`crab.md`, view `woodlouse`.**
- "Eyes" (`g`, an amateur count of 22): **corrected** to about twenty facets in four rows in the Rough Woodlouse and the Common Pill Woodlouse (L135), graded `m`.
- "Sharpness" (the sea slater's 6.91 degrees, Keskinen and colleagues, 2002): **unsupported** in this session, since the paper was not reopened; replaced by an `i` row.
- "No picture" (`i`, `field: 1`): **corrected**. Twenty facets form a coarse image (L135, L136), so a few patches are drawn.
- "Dark", "Dry air", "Night": **confirmed** (L263, L264, L265), each secondary within the paper cited, as the earlier sheet said.
- "Colour" (`i`, grey): **corrected** to `g` with the sea slater's three pigments (L22, L23, L24).
- "Damp air" (Ruiz and Guerrero Sánchez, 2022): **unsupported** in this session; the `x` row now rests on L264.

**`crab.md`, horseshoe crab entry.** "Eyes", "Sharpness", "Night" and "Ultraviolet": **confirmed** (L190, L191, L188, L187, L192, L267). "Colour": **confirmed** for the single peak (L266); the statement that no colour vision has been found (Battelle and colleagues, 2014) is **unsupported** in this session, since the abstract reopened (L186) does not say it. The entry becomes a view, with rows on edges added (L155, L156).

## 4. Species with their own measurements

These are commonly photographed species measured well enough for a profile of their own later.

- **Common octopus, *Octopus vulgaris*:** colour blindness (L3, L103, L104), pigment (L37), receptor density and band (L42, L43), acuity (L44, L45, L109, L247), flicker (L47, L48), pupil (L55, L56, L59, L75), eye movements (L49), accommodation (L60), activity (L61), skin and sucker light sense (L116), chemical food choice (L119).
- **Common cuttlefish, *Sepia officinalis*:** acuity with growth and light (L127, L128, L133), stereopsis and vergence (L77, L78, L80), pigment (L85), W pupil (L101, L102), eye counter-rolling (L120), hunting in moonlight (L131, L132), polarization and caustics (L91).
- **Golden cuttlefish, *Sepia esculenta*:** fields and band (L123, L124, L125, L126).
- **Bigfin reef squid, *Sepioteuthis lessoniana*:** field (L93), acuity in juveniles (L94), flicker (L92).
- **Longfin inshore squid, *Doryteuthis pealeii*:** pigment (L86), light-sensing proteins outside the eye (L90), hearing (L113, L114).
- **Chambered nautilus, *Nautilus pompilius*:** the whole nautilus setting (L58, L88, L105 to L108, L110).
- **Fiddler crabs** (*Uca*, *Gelasimus*, *Afruca*, *Leptuca*): resolution and band (L172 to L176), flicker and night sensitivity (L165, L177 to L180), danger from above (L162 to L164), polarization (L166, L167, L183), colour (L184, L185).
- **Green shore crab, *Carcinus maenas*:** polarization under caustics (L91), looming after caustics (L170).
- **Peacock mantis shrimp, *Odontodactylus scyllarus*:** eye movements (L150, L151, L152), circular polarization display (L19).
- **Caribbean hermit crab, *Coenobita clypeatus*:** looming (L160), smell (L171).
- **Atlantic horseshoe crab, *Limulus polyphemus*:** the whole `horseshoe` view (L11, L12, L34, L155 to L158, L186 to L192, L266 to L268).
- **Common Pill Woodlouse and Rough Woodlouse:** facets (L135, L136), night activity (L265).
- **King scallop, *Pecten maximus*, and bay scallop, *Argopecten irradians*:** eyes and mirrors (L233, L234), motion response (L231), acuity and particle response (L235, L236), pigment (L232).
- **Small giant clam, *Tridacna maxima*:** eyes, threshold and acceptance (L238, L239, L240).
- **Crown-of-thorns starfish, *Acanthaster planci*:** eye, field, acuity, contrast and flicker (L217 to L219, L272, L274 to L277).
- **Blue sea star, *Linckia laevigata*:** colour blindness, slowness and homing (L214, L215, L273).
- **Purple sea urchin, *Strongylocentrotus purpuratus*:** photoreceptors and resolution (L224, L269, L270).
- **Acropora millepora:** moon-phase proteins, spawning cue and opsin (L207, L208, L210).
- **Box jellyfish *Tripedalia cystophora*:** pigment, obstacle avoidance and the upward eye (L193, L197, L198).

## 5. Gaps and how to fill them

- **Octopus pace in ordinary daylight.** The 72 a second was measured at 4.5 million candelas per square metre and 20 at a light ten thousand times dimmer (L47, L48), and most daylight scenes are, by my reading, far dimmer than the first. Nearest: the bigfin reef squid's 50.8 at an unstated level (L92). Hamasaki (1968) has the full curve (wanted, priority 1).
- **Cuttlefish blur shape.** The W pupil is mapped to a vertical slit by guess (L101). Mäthger and colleagues (2013) give the pupil's shape for each direction (wanted).
- **Acuity of hermit crabs, crayfish and lobsters,** 81% of the `shrimp` view (anomurans, crayfish and lobsters together, 207,857 records). Nearest: three cleaner shrimps (L250) and the review's ceiling of 0.4 cycles per degree for 96 decapods (L248). The view assumes the cleaner shrimps' value; nothing more specific is known from the sources opened.
- **Field of view of shrimps and crayfish.** Nothing opened gives a number; the `i` row says so.
- **Woodlouse acuity and field.** Only the count of facets is measured (L135). The 25 degrees per facet assumes an even spread over about 125 degrees, inside the range Land and Nilsson give for coarse tasks (L30). Nemanic (1975) would give facet sizes and angles (wanted, priority 1).
- **Woodlouse colour.** Nearest: the sea slater *Ligia exotica*, 340, 470 and 520 nm (L22 to L24). Briggs (1961) extracted a pigment from *Porcellio scaber* (wanted).
- **Mantis shrimp scan speed and band width** for the sweeping band. Land and colleagues (1990) and Marshall, Land and Cronin (2014) (wanted). Until then the speed is invented.
- **Which crab families have the horizon band.** Measured only in fiddler crabs here (L174 to L176). Zeil, Nalbach and Nalbach (1986) (wanted, priority 1).
- **Cave crayfish** (five Alachua records). No source opened describes their eyes. The view treats them as crayfish; this is a guess, and a cave-dwelling crayfish may see less or nothing.
- **Freshwater mussels** (most of Alachua's bivalves). No source opened describes their light sense; they take the `i` row for eyeless bivalves.
- **Brittle stars,** 23,745 records (Amphilepidida 15,080, Ophiacanthida 7,204, Euryalida 1,459, Ophioscolecida 2). One eyeless species orients to polarized light (L228). Sumner-Rooney and colleagues (2020) would say whether they see shapes (wanted, priority 1).
- **Anemone and coral speed.** No time constant was found for the shadow responses of anemones and corals; the `sealife` view keeps `persist` unset.
- **Box jellyfish flicker by day.** Only the night-active *Copula* is measured (L200).
- **Barnacle eyes** are counted (L145, L146) and their shadow reflex described (L144); their resolution is unknown and they need none in a view with no image.
- **Spirula and other shells.** The ram's horn squid's 2,464 records are mostly shells cast ashore; the view is the cephalopod's, which is right for the animal.

## 6. Closed sources wanted

The same list as `docs/views/wanted/sea-invertebrates.jsonl`, most useful first.

Priority 1, would change a picture:
1. Zeil J, Nalbach G, Nalbach H-O 1986. Eyes, eye stalks and the visual world of semi-terrestrial crabs. *Journal of Comparative Physiology A*. doi:10.1007/bf00603733. Which crab families have a sharp band along the horizon decides whether the crab view draws one.
2. Hamasaki DI 1968. The electroretinogram of the intact anesthetized octopus. *Vision Research*. doi:10.1016/0042-6989(68)90012-6. Octopus flicker fusion across light levels, for the cephalopod view's pace in ordinary daylight.
3. Nemanic P 1975. Fine structure of the compound eye of *Porcellio scaber* in light and dark adaption. *Tissue and Cell*. doi:10.1016/0040-8166(75)90018-x. Facet sizes and angles in the Rough Woodlouse, to replace the invented 25 degrees.
4. Land MF, Marshall NJ, Brownless D, Cronin TW 1990. The eye-movements of the mantis shrimp *Odontodactylus scyllarus* (Crustacea: Stomatopoda). *Journal of Comparative Physiology A*. doi:10.1007/bf00188107. Scan speeds and mid-band width, for the sweeping colour band.
5. Sumner-Rooney LH, Kirwan JD, Lowe EK, Ullrich-Lüter E 2020. Extraocular vision in a brittle star is mediated by chromatophore movement in response to ambient light. *Current Biology*. doi:10.1016/j.cub.2019.11.042. Whether brittle stars move from the no-picture view to the starfish view.

Priority 2, would confirm or correct a row:
6. Gagnon YL, Osorio DC, Wardill TJ, Marshall NJ, Chung W-S, Temple SE 2016. Can chromatic aberration enable color vision in natural environments? *PNAS*. doi:10.1073/pnas.1612239113.
7. Stubbs AL, Stubbs CW 2016. Spectral discrimination in color blind animals via chromatic aberration and pupil shape. *PNAS*. doi:10.1073/pnas.1524578113.
8. Mäthger LM, Barbosa A, Miner S, Hanlon RT 2006. Color blindness and contrast perception in cuttlefish (*Sepia officinalis*) determined by a visual sensorimotor assay. *Vision Research*. doi:10.1016/j.visres.2005.09.035.
9. Mäthger LM, Hanlon RT, Håkansson J, Nilsson D-E 2013. The W-shaped pupil in cuttlefish (*Sepia officinalis*): functions for improving horizontal vision. *Vision Research* 83: 19 to 24. doi:10.1016/j.visres.2013.02.016.
10. Temple SE, Pignatelli V, Cook T, How MJ, Chiou T-H, Roberts NW, Marshall NJ 2012. High-resolution polarisation vision in a cuttlefish. *Current Biology*. doi:10.1016/j.cub.2012.01.010.
11. Detto T, Backwell PRY 2009. The fiddler crab *Uca mjoebergi* uses ultraviolet cues in mate choice but not aggressive interactions. *Animal Behaviour*. doi:10.1016/j.anbehav.2009.05.014.
12. Briggs MH 1961. The visual pigment of an isopod crustacean. *Australian Journal of Biological Sciences*. doi:10.1071/bi9610487.
13. Beer S, Wentzel C, Petie R, Garm A 2016. Active control of the visual field in the starfish *Acanthaster planci*. *Vision Research*. doi:10.1016/j.visres.2016.05.007.
14. Marshall NJ, Land MF, Cronin TW 2014. Shrimps that pay attention: saccadic eye movements in stomatopod crustaceans. *Philosophical Transactions of the Royal Society B*. doi:10.1098/rstb.2013.0042.

Priority 3, background:
15. Nilsson D-E, Warrant EJ, Johnsen S, Hanlon RT, Shashar N 2012. A unique advantage for giant eyes in giant squid. *Current Biology*. doi:10.1016/j.cub.2012.02.031.
16. Shashar N, Hanlon RT, Petz AdeM 1998. Polarization vision helps detect transparent prey. *Nature*. doi:10.1038/30380.
17. Messenger JB 1968. The visual attack of the cuttlefish, *Sepia officinalis*. *Animal Behaviour*. doi:10.1016/0003-3472(68)90020-1.
18. Muntz WRA 2009. Visual behavior and visual sensitivity of *Nautilus pompilius*. *Topics in Geobiology*. doi:10.1007/978-90-481-3299-7_15.
19. Wilkens LA 1984. Ultraviolet sensitivity in hyperpolarizing photoreceptors of the giant clam *Tridacna*. *Nature*. doi:10.1038/309446a0.
20. Cronin TW, Caldwell RL, Erdmann MV 2002. Tuning of photoreceptor function in three mantis shrimp species that inhabit a range of depths. I. Visual pigments. *Journal of Comparative Physiology A*. doi:10.1007/s00359-002-0291-0.

## 7. Sources

### Opened in this session

- Adams NL 2001. UV radiation evokes negative phototaxis and covering behavior in the sea urchin Strongylocentrotus droebachiensis. *Marine Ecology Progress Series 213: 87*. doi:10.3354/meps213087. **opened (abstract, collection)**. Log L227.
- Allen GJP, Yan JJ, Kuan PL, Hayasaka O, Hsu SC, Lu MJ, Anraku K, Wu GC, Tseng YC 2026. Neurometabolic rewiring in squid (Sepioteuthis lessoniana) optic lobes drives behavioral plasticity and visual integration under environmental acidification. *Communications Biology*. doi:10.1038/s42003-025-09506-6. **opened (full text, collection)**. Log L92.
- Allen VA, Niell CM 2026. Visual computation in the cephalopod brain. *Current Opinion in Neurobiology*. doi:10.1016/j.conb.2026.103249. **opened (full text, collection)**. Log L95.
- Bagheri ZM, Jessop A-L, Kato S, Partridge JC, Shaw J, Ogawa Y, Hemmi JM 2019. A new method for mapping spatial resolution in compound eyes suggests two visual streaks in fiddler crabs. *Journal of Experimental Biology*. doi:10.1242/jeb.210195. **opened (abstract, collection)**. Log L176.
- Barlow RB Jr, Kaplan E, Renninger GH, Saito T 1987. Circadian rhythms in Limulus photoreceptors. I. Intracellular studies. *The Journal of General Physiology 89: 353-378*. doi:10.1085/jgp.89.3.353. **opened (abstract, collection)**. Log L187.
- Barnatan Y, Tomsic D, Sztarker J 2019. Unidirectional Optomotor Responses and Eye Dominance in Two Species of Crabs. *Frontiers in Physiology*. doi:10.3389/fphys.2019.00586. **opened (full text, collection)**. Log L168.
- Battelle B-A, Kempler KE, Harrison A, Dugger DR, Payne R 2014. Opsin expression in Limulus eyes: a UV opsin is expressed in each eye type and co-expressed with a visible light-sensitive opsin in ventral larval eyes. *Journal of Experimental Biology 217: 3133-3145*. doi:10.1242/jeb.107383. **opened (abstract, collection)**. Log L186.
- Battelle B-A, Ryan JF, Kempler KE, Saraf SR, Marten CE, Warren WC, Minx PJ, Montague MJ, Green PJ, Schmidt SA, Fulton LA, Patel NH and others 2016. Opsin Repertoire and Expression Patterns in Horseshoe Crabs: Evidence from the Genome of Limulus polyphemus (Arthropoda: Chelicerata). *Genome Biology and Evolution*. doi:10.1093/gbe/evw100. **opened (full text, collection)**. Log L158.
- Brauckhoff M, Wahlberg M, Haga JÅR, Karlsen HE, Wilson MN 2020. Embracing Their Prey at That Dark Hour: Common Cuttlefish (Sepia officinalis) Can Hunt in Nighttime Light Conditions. *Frontiers in Physiology*. doi:10.3389/fphys.2020.00525. **opened (full text, collection)**. Log L131-L132.
- Brodrick E, Roberts NW, Sumner-Rooney LH, Schlepütz CM, How MJ 2020. Light adaptation mechanisms in the eye of the fiddler crab Afruca tangeri. *The Journal of Comparative Neurology*. doi:10.1002/cne.24973. **opened (abstract, collection)**. Log L165.
- Brodrick EA, How MJ, Hemmi JM 2022. Fiddler crab electroretinograms reveal vast circadian shifts in visual sensitivity and temporal summation in dim light. *Journal of Experimental Biology*. doi:10.1242/jeb.243693. **opened (full text, collection)**. Log L177-L180.
- Bruski CA, Dunham D 1987. The Importance of Vision in Agonistic Communication of the Crayfish Orconectes Rusticus. I: an Analysis of Bout Dynamics. *Behaviour*. doi:10.1163/156853987x00288. **opened (abstract, collection)**. Log L259.
- Budelmann BU, Williamson R 1994. Directional sensitivity of hair cell afferents in the Octopus statocyst. *Journal of Experimental Biology 187: 245*. doi:10.1242/jeb.187.1.245. **opened (abstract, collection)**. Log L112.
- Caves EM, Frank TM, Johnsen S 2016. Spectral sensitivity, spatial resolution, and temporal resolution and their implications for conspecific signalling in cleaner shrimp. *Journal of Experimental Biology*. doi:10.1242/jeb.122275. **opened (abstract, collection)**. Log L250-L252.
- Caves EM, Brandley NC, Johnsen S 2018. Visual Acuity and the Evolution of Signals. *Trends in Ecology & Evolution 33(5)*. doi:10.1016/j.tree.2018.03.001. **opened (owner's library copy)**. Log L247-L249.
- Chang W, Hale ME 2025. Neural responses to light stimulation in the octopus arm. *Journal of Experimental Biology*. doi:10.1242/jeb.250111. **opened (full text, collection)**. Log L117.
- Chapman RM, Lall AB 1967. Electroretinogram Characteristics and the Spectral Mechanisms of the Median Ocellus and the Lateral Eye in Limulus polyphemus. *The Journal of General Physiology 50(9): 2267*. doi:10.1085/jgp.50.9.2267. **opened (full text, collection)**. Log L266-L267.
- Chung W-S, Marshall NJ 2016. Comparative visual ecology of cephalopods from different habitats. *Proceedings of the Royal Society B*. doi:10.1098/rspb.2016.1346. **opened (full text, collection)**. Log L82-L89.
- Chung W-S, Marshall NJ 2017. Complex Visual Adaptations in Squid for Specific Tasks in Different Environments. *Frontiers in Physiology*. doi:10.3389/fphys.2017.00105. **opened (full text, collection)**. Log L134.
- Coates MM, Garm A, Theobald JC, Thompson SH, Nilsson D-E 2006. The spectral sensitivity of the lens eyes of a box jellyfish, Tripedalia cystophora (Conant). *Journal of Experimental Biology*. doi:10.1242/jeb.02431. **opened (abstract, collection)**. Log L193.
- Cronin TW, Porter ML 2008. Exceptional Variation on a Common Theme: The Evolution of Crustacean Compound Eyes. *Evolution: Education and Outreach 1: 463-475*. doi:10.1007/s12052-008-0085-0. **opened (full text, collection)**. Log L137-L141, L271.
- Daly IM, How MJ, Partridge JC, Temple SE, Marshall NJ, Cronin TW, Roberts NW 2016. Dynamic polarization vision in mantis shrimps. *Nature Communications 7: 12140*. doi:10.1038/ncomms12140. **opened (full text, collection)**. Log L152.
- Daly IM, How MJ, Partridge JC, Roberts NW 2017. The independence of eye movements in a stomatopod crustacean is task dependent. *Journal of Experimental Biology*. doi:10.1242/jeb.153692. **opened (full text, collection)**. Log L150.
- Daly IM, How MJ, Partridge JC, Roberts NW 2018. Complex gaze stabilization in mantis shrimp. *Proceedings of the Royal Society B*. doi:10.1098/rspb.2018.0594. **opened (full text, collection)**. Log L151.
- Darmaillacq A-S, Mezraï N, O'Brien CE, Dickel L 2017. Visual Ecology and the Development of Visually Guided Behavior in the Cuttlefish. *Frontiers in Physiology*. doi:10.3389/fphys.2017.00402. **opened (full text, collection)**. Log L133.
- Detto T 2007. The fiddler crab Uca mjoebergi uses colour vision in mate choice. *Proceedings of the Royal Society B 274: 2785-2790*. doi:10.1098/rspb.2007.1059. **opened (abstract, collection)**. Log L185.
- Drerup C, Herbert-Read JE, How MJ 2025. Motion After-Effects Induced by Dynamic Illumination in Crab Vision. *Ecology and Evolution*. doi:10.1002/ece3.71426. **opened (full text, collection)**. Log L170.
- Feord RC, Sumner ME, Pusdekar S, Kalra L, Gonzalez-Bellido PT, Wardill TJ 2020. Cuttlefish use stereopsis to strike at prey. *Science Advances*. doi:10.1126/sciadv.aay6036. **opened (full text, collection)**. Log L77-L81.
- Fialová R, Tuf IH 2025. Spatial activity and sheltering behaviour of terrestrial isopods (Isopoda, Oniscidea): a field experiment. *ZooKeys 1225: 127-139*. doi:10.3897/zookeys.1225.125030. **opened (web page: https://zookeys.pensoft.net/article_preview.php?id=125030)**. Log L263-L265.
- Garm A, O'Connor M, Parkefelt L, Nilsson D-E 2007. Visually guided obstacle avoidance in the box jellyfish Tripedalia cystophora and Chiropsella bronzie. *Journal of Experimental Biology*. doi:10.1242/jeb.004044. **opened (abstract, collection)**. Log L197.
- Garm A, Mori S 2009. Multiple photoreceptor systems control the swim pacemaker activity in box jellyfish. *Journal of Experimental Biology*. doi:10.1242/jeb.031559. **opened (abstract, collection)**. Log L195-L196.
- Garm A, Oskarsson M, Nilsson D-E 2011. Box Jellyfish Use Terrestrial Visual Cues for Navigation. *Current Biology 21(9): 798-803*. doi:10.1016/j.cub.2011.03.054. **opened (web page: https://www.lunduniversity.lu.se/lup/publication/d9cb9142-b556-4a5f-8f00-937d4a4476e3)**. Log L198.
- Garm A, Nilsson D-E 2014. Visual navigation in starfish: first evidence for the use of vision and eyes in starfish. *Proceedings of the Royal Society B 281: 20133011*. doi:10.1098/rspb.2013.3011. **opened (abstract, collection)**. Log L214-L215.
- Garm A, Bielecki J, Petie R, Nilsson D-E 2016. Hunting in Bioluminescent Light: Vision in the Nocturnal Box Jellyfish Copula sivickisi. *Frontiers in Physiology*. doi:10.3389/fphys.2016.00099. **opened (full text, collection)**. Log L199-L201.
- Garm AL, Hamilton O, Glenner H, Irwin AR, Mah CL 2023. Eyes, Vision, and Bioluminescence in Deep-Sea Brisingid Sea Stars. *Biological Bulletin*. doi:10.1086/729983. **opened (abstract, collection)**. Log L220.
- Gorbunov MY, Falkowski PG 2002. Photoreceptors in the cnidarian hosts allow symbiotic corals to sense blue moonlight. *Limnology and Oceanography 47(1): 309*. doi:10.4319/lo.2002.47.1.0309. **opened (abstract, collection)**. Log L205-L206.
- Groeger G, Cotton PA, Williamson R 2005. Ontogenetic changes in the visual acuity of Sepia officinalis measured using the optomotor response. *Canadian Journal of Zoology*. doi:10.1139/z05-011. **opened (abstract, collection)**. Log L127-L128.
- Gwilliam GF 1965. The mechanism of the shadow reflex in Cirripedia. II. Photoreceptor cell response, second-order responses, and motor cell output. *Biological Bulletin*. doi:10.2307/1539842. **opened (abstract, collection)**. Log L143-L144.
- Hanke FD, Kelber A 2020. The Eye of the Common Octopus (Octopus vulgaris). *Frontiers in Physiology*. doi:10.3389/fphys.2019.01637. **opened**. Log L37-L63.
- Hartline HK, Wagner HG, Ratliff F 1956. Inhibition in the eye of Limulus. *The Journal of General Physiology*. doi:10.1085/jgp.39.5.651. **opened (full text, collection)**. Log L155.
- Hartline HK, Ratliff F 1957. Inhibitory interaction of receptor units in the eye of Limulus. *The Journal of General Physiology*. doi:10.1085/jgp.40.3.357. **opened (full text, collection)**. Log L156.
- Harzsch S, Hansson BS 2008. Brain architecture in the terrestrial hermit crab Coenobita clypeatus (Anomura, Coenobitidae), a crustacean with a good aerial sense of smell. *BMC Neuroscience*. doi:10.1186/1471-2202-9-58. **opened (full text, collection)**. Log L171.
- Herzog ED, Barlow RB 1992. The Limulus-eye view of the world. *Visual Neuroscience 9(6): 571-580*. doi:10.1017/S0952523800001814. **opened (web page: https://profiles.wustl.edu/en/publications/the-limulus-eye-view-of-the-world/)**. Log L188-L192.
- How MJ, Pignatelli V, Temple SE, Marshall NJ, Hemmi JM 2012. High e-vector acuity in the polarisation vision system of the fiddler crab Uca vomeris. *Journal of Experimental Biology 215: 2128-2134*. doi:10.1242/jeb.068544. **opened (abstract, collection)**. Log L183.
- How MJ, Christy JH, Roberts NW, Marshall NJ 2014. Null point of discrimination in crustacean polarisation vision. *Journal of Experimental Biology*. doi:10.1242/jeb.103457. **opened (abstract, collection)**. Log L153-L154.
- How MJ, Robertson A, Smithers SP, Wilby D 2023. Polarization vision in terrestrial hermit crabs. *Journal of Comparative Physiology A*. doi:10.1007/s00359-023-01631-z. **opened (full text, collection)**. Log L159.
- Huang J, Ren C, Qin Z, Cui Y, Zhang B, Luo P, Wang X, Xie Y, Zhang X, Yan A, Zhang Y, Fan D and others 2026. A Pentaradial and Bilateral Combined Photoreception System in the Sea Cucumber is Mediated by a Blue Light-Sensitive R-Opsin. *Advanced Science*. doi:10.1002/advs.202512095. **opened (full text, collection)**. Log L229-L230.
- Hudspeth AJ, Stuart AE 1977. Morphology and responses to light of the somata, axons, and terminal regions of individual photoreceptors of the giant barnacle. *The Journal of Physiology*. doi:10.1113/jphysiol.1977.sp012031. **opened (abstract, collection)**. Log L146.
- Hurley AC, Lange GD, Hartline PH 1978. The adjustable "pinhole camera" eye of Nautilus. *Journal of Experimental Zoology 205*. doi:10.1002/jez.1402050106. **opened (abstract, collection)**. Log L110.
- Janakis M, Guirges S, Grant AC, Paris I, LoPresti E, Speiser DI 2025. Two Decapod Crustaceans, Panopeus herbstii and Petrolisthes armatus, Stabilize Their Gaze Using Achromatic Visual Cues, but Not the Angle of Linearly Polarized Light. *Integrative Organismal Biology*. doi:10.1093/iob/obaf034. **opened (full text, collection)**. Log L169.
- Johnsen S 1994. Extraocular Sensitivity to Polarized Light in an Echinoderm. *Journal of Experimental Biology 195: 281*. doi:10.1242/jeb.195.1.281. **opened (abstract, collection)**. Log L228.
- Jordão JM, Cronin TW, Oliveira RF 2007. Spectral sensitivity of four species of fiddler crabs (Uca pugnax, Uca pugilator, Uca vomeris and Uca tangeri) measured by in situ microspectrophotometry. *Journal of Experimental Biology 210: 447-453*. doi:10.1242/jeb.02658. **opened (abstract, collection)**. Log L184.
- Kaifu K, Segawa S, Tsuchiya K 2007. Behavioral Responses to Underwater Sound in the Small Benthic Octopus Octopus ocellatus. *The Journal of the Marine Acoustics Society of Japan 34*. doi:10.3135/jmasj.34.266. **opened (abstract, collection)**. Log L111.
- Kaniewska P, Alon S, Karako-Lampert S, Hoegh-Guldberg O, Levy O 2015. Signaling cascades and the importance of moonlight in coral broadcast mass spawning. *eLife*. doi:10.7554/elife.09991. **opened (full text, collection)**. Log L208.
- Kennedy D 1960. Neural Photoreception in a Lamellibranch Mollusc. *The Journal of General Physiology 44(2): 277-299*. doi:10.1085/jgp.44.2.277. **opened (web page: https://rupress.org/jgp/article/44/2/277/30525/Neural-Photoreception-in-a-Lamellibranch-Mollusc)**. Log L241.
- Kennedy D, Bruno MS 1961. The Spectral Sensitivity of Crayfish and Lobster Vision. *The Journal of General Physiology 44(6): 1089*. doi:10.1085/jgp.44.6.1089. **opened (abstract, collection)**. Log L253-L254.
- Kingston ACN, Wardill TJ, Hanlon RT, Cronin TW 2015. An Unexpected Diversity of Photoreceptor Classes in the Longfin Squid, Doryteuthis pealeii. *PLoS ONE*. doi:10.1371/journal.pone.0135381. **opened (full text, collection)**. Log L90.
- Kirwan JD, Li T, Ullrich-Lüter J, La Camera G, Nilsson D-E, Arnone MI 2024. The sea urchin Paracentrotus lividus orients to visual stimuli. *bioRxiv*. doi:10.1101/2024.01.05.574409. **opened (abstract, collection)**. Log L225.
- Korsvig-Nielsen CE, Hall M, Motti CA, Garm A 2019. Eyes and negative phototaxis in juvenile crown-of-thorns starfish, Acanthaster species complex. *Biology Open*. doi:10.1242/bio.041814. **opened (full text, collection)**. Log L216-L219.
- Land MF 1966. Activity in the Optic Nerve of Pecten Maximus in Response to Changes in Light Intensity, and To Pattern and Movement in the Optical Environment. *Journal of Experimental Biology 45: 83*. doi:10.1242/jeb.45.1.83. **opened (abstract, collection)**. Log L231.
- Land MF 2003. The spatial resolution of the pinhole eyes of giant clams (Tridacna maxima). *Proceedings of the Royal Society B 270(1511): 185-188*. https://sussex.figshare.com/articles/journal_contribution/The_spatial_resolution_of_the_pinhole_eyes_of_giant_clams_Tridacna_maxima_/23344340. **opened (web page: https://sussex.figshare.com/articles/journal_contribution/The_spatial_resolution_of_the_pinhole_eyes_of_giant_clams_Tridacna_maxima_/23344340)**. Log L238-L240.
- Land MF, Nilsson D-E 2012. Animal Eyes, 2nd edition (Oxford Animal Biology Series). *Oxford University Press (book)*. doi:10.1093/acprof:oso/9780199581139.001.0001. **opened (owner's library copy)**. Log L1-L36.
- Layne JE 1998. Retinal Location is the Key to Identifying Predators in Fiddler Crabs (Uca Pugilator). *Journal of Experimental Biology 201: 2253*. doi:10.1242/jeb.201.15.2253. **opened (abstract, collection)**. Log L162.
- Levy O, Appelbaum L, Leggat W, Gothlif Y, Hayward DC, Miller DJ, Hoegh-Guldberg O 2007. Light-Responsive Cryptochromes from a Simple Multicellular Animal, the Coral Acropora millepora. *Science*. doi:10.1126/science.1145432. **opened (abstract, collection)**. Log L207.
- Lewis BM, Suggett DJ, Prentis PJ, Nothdurft LD 2025. Walking coral: Complex phototactic mobility in the free-living coral Cycloseris cyclolites. *PLoS ONE*. doi:10.1371/journal.pone.0315623. **opened (full text, collection)**. Log L209.
- Leys SP, Degnan BM 2001. Cytological Basis of Photoresponsive Behavior in a Sponge Larva. *Biological Bulletin*. doi:10.2307/1543611. **opened (abstract, collection)**. Log L242.
- Li T, Kirwan JD, Arnone MI, Nilsson D-E, La Camera G 2023. A model of decentralized vision in the sea urchin Diadema africanum. *iScience*. doi:10.1016/j.isci.2023.106295. **opened (full text, collection)**. Log L226.
- Liu JS, Passaglia CL 2009. Using the Horseshoe Crab, Limulus Polyphemus, in Vision Research. *Journal of Visualized Experiments*. doi:10.3791/1384. **opened (full text, collection)**. Log L157, L268.
- Loew ER 1976. Light, and photoreceptor degeneration in the Norway lobster, Nephrops norvegicus (L.). *Proceedings of the Royal Society B*. doi:10.1098/rspb.1976.0029. **opened (abstract, collection)**. Log L255.
- Luque J, Allison WT, Bracken-Grissom HD, Jenkins KM, Palmer AR, Porter ML, Wolfe JM 2019. Evolution of crab eye structures and the utility of ommatidia morphology in resolving phylogeny. *bioRxiv*. doi:10.1101/786087. **opened (abstract, collection)**. Log L258.
- Marshall NJ, Land MF, Cronin TW 2014. Shrimps that pay attention: saccadic eye movements in stomatopod crustaceans. *Philosophical Transactions of the Royal Society B*. doi:10.1098/rstb.2013.0042. **opened (abstract, collection)**. Log L261-L262.
- Martin VJ 2002. Photoreceptors of cnidarians. *Canadian Journal of Zoology*. doi:10.1139/z02-136. **opened (abstract, collection)**. Log L202.
- Maselli V, Al-Soudy A-S, Buglione M, Aria M, Polese G, Di Cosmo A 2020. Sensorial Hierarchy in Octopus vulgaris's Food Choice: Chemical vs. Visual. *Animals*. doi:10.3390/ani10030457. **opened (full text, collection)**. Log L119.
- Maselli V, Al-Soudy A-S, Norcia M, Galdiero S, Palladino S, Cirillo E, Polese G, Di Cosmo A 2025. Extraocular Photoreception in Optic Lobes, Suckers, and Skin of Octopus vulgaris. *Integrative Zoology*. doi:10.1111/1749-4877.13002. **opened (abstract, collection)**. Log L116.
- Mason BM, Koyanagi M, Sugihara T, Iwasaki M, Slepak VZ, Miller DJ, Sakai Y, Terakita A 2023. Multiple opsins in a reef-building coral, Acropora millepora. *Scientific Reports*. doi:10.1038/s41598-023-28476-5. **opened (full text, collection)**. Log L210.
- McCulloch KJ, Babonis LS, Liu A, Daly CMS, Martindale MQ, Koenig KM 2023. Nematostella vectensis exemplifies the exceptional expansion and diversity of opsins in the eyeless Hexacorallia. *EvoDevo*. doi:10.1186/s13227-023-00218-8. **opened (full text, collection)**. Log L211.
- McReynolds JS, Gorman ALF 1970. Membrane Conductances and Spectral Sensitivities of Pecten Photoreceptors. *The Journal of General Physiology 56: 392*. doi:10.1085/jgp.56.3.392. **opened (abstract, collection)**. Log L232.
- Messenger JB 1970. Optomotor Responses and Nystagmus in Intact, Blinded and Statocystless Cuttlefish (Sepia Officinalis L.). *Journal of Experimental Biology 53: 789*. doi:10.1242/jeb.53.3.789. **opened (abstract, collection)**. Log L120.
- Messenger JB, Wilson A, Hedge A 1973. Some Evidence for Colour-Blindness in Octopus. *Journal of Experimental Biology 59: 77*. doi:10.1242/jeb.59.1.77. **opened (abstract, collection)**. Log L104.
- Messenger JB 1977. Evidence That Octopus is Colour Blind. *Journal of Experimental Biology 70: 49*. doi:10.1242/jeb.70.1.49. **opened (abstract, collection)**. Log L103.
- Mooney TA, Hanlon RT, Christensen-Dalsgaard J, Madsen PT, Ketten DR, Nachtigall PE 2010. Sound detection by the longfin squid (Loligo pealeii) studied with auditory evoked potentials: sensitivity to low-frequency particle motion and not pressure. *Journal of Experimental Biology 213: 3748-3759*. doi:10.1242/jeb.048348. **opened (web page: https://cob.silverchair.com/jeb/article-pdf/213/21/3748/1430823/3748.pdf)**. Log L113-L114.
- Muntz WRA, Raj U 1984. On the Visual System of Nautilus Pompilius. *Journal of Experimental Biology 109: 253*. doi:10.1242/jeb.109.1.253. **opened (abstract, collection)**. Log L105-L107.
- Muntz WRA 1986. The Spectral Sensitivity of Nautilus Pompilius (short communication). *Journal of Experimental Biology 126: 513*. doi:10.1242/jeb.126.1.513. **opened (abstract, collection)**. Log L108-L109.
- Muntz WRA, Gwyther J 1988. Visual Acuity in Octopus Pallidus and Octopus Australis. *Journal of Experimental Biology 134: 119*. doi:10.1242/jeb.134.1.119. **opened (abstract, collection)**. Log L129.
- Mäthger LM, Hanlon RT, Håkansson J, Nilsson D-E 2013. The W-shaped pupil in cuttlefish (Sepia officinalis): Functions for improving horizontal vision. *Vision Research 83: 19-24*. doi:10.1016/j.visres.2013.02.016. **opened (web page: https://marineinfo.org/id/publication/230275)**. Log L101-L102.
- Nahmad-Rohen L, Vorobyev M 2020. Spatial Contrast Sensitivity to Polarization and Luminance in Octopus. *Frontiers in Physiology*. doi:10.3389/fphys.2020.00379. **opened (full text, collection)**. Log L72-L74.
- Nakagawa M, Miyamoto T, Ohkuma M, Tsuda M 1999. Action Spectrum for the Photophobic Response of Ciona intestinalis (Ascidieacea, Urochordata) Larvae Implicates Retinal Protein. *Photochemistry and Photobiology 70: 359*. doi:10.1562/0031-8655(1999)070<0359:asftpr>2.3.co;2. **opened (abstract, collection)**. Log L244.
- Nemanic P 1972. Some Unique Features in Compound Eyes of Two Isopods. *Proceedings, annual meeting, Electron Microscopy Society of America*. doi:10.1017/s0424820100093493. **opened (abstract, collection)**. Log L135-L136.
- Nilsson D-E 1994. Eyes as optical alarm systems in fan worms and ark clams. *Philosophical Transactions of the Royal Society B*. doi:10.1098/rstb.1994.0141. **opened (abstract, collection)**. Log L237.
- O'Connor M, Garm A, Marshall NJ, Hart NS, Ekström P, Skogh C, Nilsson D-E 2010. Visual pigment in the lens eyes of the box jellyfish Chiropsella bronzie. *Proceedings of the Royal Society B*. doi:10.1098/rspb.2009.2248. **opened (abstract, collection)**. Log L194.
- Oliva D, Tomsic D 2014. Computation of object approach by a system of visual motion-sensitive neurons in the crab Neohelice. *Journal of Neurophysiology*. doi:10.1152/jn.00921.2013. **opened (abstract, collection)**. Log L161.
- Palmer BA, Taylor GJ, Brumfeld V, Gur D, Shemesh M, Elad N, Osherov A, Oron D, Weiner S, Addadi L 2017. The image-forming mirror in the eye of the scallop. *Science 358: 1172-1175*. doi:10.1126/science.aam9506. **opened (abstract, collection)**. Log L233-L234.
- Palmer BA, Hirsch A, Brumfeld V, Aflalo ED, Pinkas I, Sagi A, Rosenne S, Oron D, Leiserowitz L, Kronik L, Weiner S, Addadi L 2018. Optically functional isoxanthopterin crystals in the mirrored eyes of decapod crustaceans. *Proceedings of the National Academy of Sciences*. doi:10.1073/pnas.1722531115. **opened (abstract, collection)**. Log L256-L257.
- Pecunioso A, Motta G, Manfrin C, Avian M, Chiandetti C, Agrillo C 2026. Shining a light on jellyfish behaviour: Enhanced motor activity and positive phototaxis in Aurelia coerulea. *Behavioural Processes*. doi:10.1016/j.beproc.2026.105409. **opened (abstract, collection)**. Log L204.
- Pei X, Wilkens LA, Moss F 1996. Light enhances hydrodynamic signaling in the multimodal caudal photoreceptor interneurons of the crayfish. *Journal of Neurophysiology*. doi:10.1152/jn.1996.76.5.3002. **opened (abstract, collection)**. Log L260.
- Petie R, Garm A, Hall MR 2016. Crown-of-thorns starfish have true image forming vision. *Frontiers in Zoology 13: 41*. doi:10.1186/s12983-016-0174-9. **opened (web page: https://link.springer.com/article/10.1186/s12983-016-0174-9)**. Log L272-L277.
- Picciani N, Kerlin JR, Jindrich K, Hensley NM, Gold DA, Oakley TH 2021. Light modulated cnidocyte discharge predates the origins of eyes in Cnidaria. *Ecology and Evolution*. doi:10.1002/ece3.7280. **opened (full text, collection)**. Log L212.
- Pires A, Woollacott RM 1997. Serotonin and Dopamine Have Opposite Effects on Phototaxis in Larvae of the Bryozoan Bugula neritina. *Biological Bulletin*. doi:10.2307/1542749. **opened (abstract, collection)**. Log L245.
- Po T, Korob L, McHenry MJ 2025. The directional control of phototaxis in sea stars (Protoreaster nodosus). *Journal of Experimental Biology*. doi:10.1242/jeb.249293. **opened (abstract, collection)**. Log L223.
- Quiroga-Artigas G, Lapébie P, Leclère L, Takeda N, Deguchi R, Jékely G, Momose T, Houliston E 2018. A gonad-expressed opsin mediates light-induced spawning in the jellyfish Clytia. *eLife*. doi:10.7554/elife.29555. **opened (full text, collection)**. Log L213.
- Ramos AP, Gustafsson OSE, Labert N, Salecker I, Nilsson D-E, Averof M 2019. Analysis of the genetically tractable crustacean Parhyale hawaiensis reveals the organisation of a sensory system for low-resolution vision. *BMC Biology*. doi:10.1186/s12915-019-0676-y. **opened (full text, collection)**. Log L142.
- Reiter S 2026. Weaving the rainbow: Color-blind color matching in cephalopods. *Current Opinion in Neurobiology*. doi:10.1016/j.conb.2026.103206. **opened (abstract, collection)**. Log L100.
- Rivera AS, Öztürk N, Fahey B, Plachetzki DC, Degnan BM, Sancar A, Oakley TH 2012. Blue-light-receptive cryptochrome is expressed in a sponge eye lacking neurons and opsin. *Journal of Experimental Biology*. doi:10.1242/jeb.067140. **opened (abstract, collection)**. Log L243.
- Schnitzler CE, Pang K, Powers ML, Reitzel AM, Ryan JF, Simmons D, Tada T, Park M, Gupta J, Brooks SY, Blakesley RW, Yokoyama S and others 2012. Genomic organization, evolution, and expression of photoprotein and opsin genes in Mnemiopsis leidyi: a new view of ctenophore photocytes. *BMC Biology*. doi:10.1186/1741-7007-10-107. **opened (full text, collection)**. Log L246.
- Shashar N, Cronin TW 1996. Polarization Contrast Vision in Octopus. *Journal of Experimental Biology 199: 999*. doi:10.1242/jeb.199.4.999. **opened (abstract, collection)**. Log L115.
- Shaw SR 1972. Decremental conduction of the visual signal in barnacle lateral eye. *The Journal of Physiology*. doi:10.1113/jphysiol.1972.sp009699. **opened (abstract, collection)**. Log L145.
- Shragai T, Ping X, Arakaki C, Garlick D, Blumstein DT, Blaisdell AP 2017. Hermit crab response to a visual threat is sensitive to looming cues. *PeerJ*. doi:10.7717/peerj.4058. **opened (full text, collection)**. Log L160.
- Smithers SP, Roberts NW, How MJ 2019. Parallel processing of polarization and intensity information in fiddler crab vision. *Science Advances*. doi:10.1126/sciadv.aax3572. **opened (full text, collection)**. Log L166.
- Smithers SP, Brett MF, How MJ, Scott-Samuel NE, Roberts NW 2024. Fiddler crabs (Afruca tangeri) detect second-order motion in both intensity and polarization. *Communications Biology*. doi:10.1038/s42003-024-06953-5. **opened (full text, collection)**. Log L167.
- Smolka J, Zeil J, Hemmi JM 2011. Natural visual cues eliciting predator avoidance in fiddler crabs. *Proceedings of the Royal Society B*. doi:10.1098/rspb.2010.2746. **opened (abstract, collection)**. Log L163.
- Smolka J, Raderschall CA, Hemmi JM 2012. Flicker is part of a multi-cue response criterion in fiddler crab predator avoidance. *Journal of Experimental Biology*. doi:10.1242/jeb.076133. **opened (abstract, collection)**. Log L164.
- Soto C, Kelber A, Hanke FD 2020. The Pupillary Response of the Common Octopus (Octopus vulgaris). *Frontiers in Physiology*. doi:10.3389/fphys.2020.01112. **opened (full text, collection)**. Log L75-L76.
- Speiser DI, Johnsen S 2008. Scallops visually respond to the size and speed of virtual particles. *Journal of Experimental Biology 211(13): 2066-2070*. doi:10.1242/jeb.017038. **opened (web page: https://fds.duke.edu/db/aas/CMAC/faculty/sjohnsen/publications/228576)**. Log L235-L236.
- Streets A, England H, Marshall NJ 2022. Colour vision in stomatopod crustaceans: more questions than answers. *Journal of Experimental Biology*. doi:10.1242/jeb.243699. **opened (full text, collection)**. Log L147-L149.
- Stubbs AL, Stubbs CW 2015. Spectral discrimination in "color blind" animals via chromatic aberration and pupil shape (bioRxiv preprint of the 2016 PNAS paper, doi 10.1073/pnas.1524578113). *bioRxiv*. doi:10.1101/017756. **opened (web page: https://www.biorxiv.org/content/10.1101/017756v1)**. Log L96-L99.
- Sugimoto C, Lei S, Ao T, Sakurai Y, Zhang X, Ikeda Y 2026. Camera-type eye specific visual ontogeny in squid (Sepioteuthis lessoniana). *Journal of Experimental Biology*. doi:10.1242/jeb.250437. **opened (full text, collection)**. Log L93-L94.
- Sweeney A, Haddock SHD, Johnsen S 2007. Comparative visual acuity of coleoid cephalopods. *Integrative and Comparative Biology*. doi:10.1093/icb/icm092. **opened (abstract, collection)**. Log L130.
- Talbot CM, Marshall NJ 2011. The retinal topography of three species of coleoid cephalopod: significance for perception of polarized light. *Philosophical Transactions of the Royal Society B*. doi:10.1098/rstb.2010.0254. **opened (abstract, collection)**. Log L121-L122.
- Temple SE, How MJ, Powell SB, Gruev V, Marshall NJ, Roberts NW 2021. Thresholds of polarization vision in octopuses. *Journal of Experimental Biology*. doi:10.1242/jeb.240812. **opened (full text, collection)**. Log L64-L71.
- Thoen HH, How MJ, Chiou T-H, Marshall NJ 2014. A different form of color vision in mantis shrimp. *Science 343: 411-413*. doi:10.1126/science.1245824. **opened (abstract, collection)**. Log L181-L182.
- Ullrich-Lüter EM, Dupont S, Arboleda E, Hausen H, Arnone MI 2011. Unique system of photoreceptors in sea urchin tube feet. *Proceedings of the National Academy of Sciences*. doi:10.1073/pnas.1018495108. **opened (abstract, collection)**. Log L224.
- Venables SV, Drerup C, Powell SB, Marshall NJ, Herbert-Read JE, How MJ 2022. Polarization vision mitigates visual noise from flickering light underwater. *Science Advances*. doi:10.1126/sciadv.abq2770. **opened (full text, collection)**. Log L91.
- Watanuki N, Kawamura G, Kaneuchi S, Iwashita T 2000. Role of vision in behavior, visual field, and visual acuity of cuttlefish Sepia esculenta. *Fisheries Science 66(3): 417*. doi:10.1046/j.1444-2906.2000.00068.x. **opened (abstract, collection)**. Log L123-L126.
- Weber C 1982. Electrical activities of a type of electroretinogram recorded from the ocellus of a jellyfish, Polyorchis penicillatus (hydromedusae). *Journal of Experimental Zoology*. doi:10.1002/jez.1402230305. **opened (abstract, collection)**. Log L203.
- Weertman W, Gopal V, Sivitilli DM, Scheel D, Gire DH 2025. Octopus track chemosensory plumes to find food. *PLoS ONE*. doi:10.1371/journal.pone.0330262. **opened (full text, collection)**. Log L118.
- Yerramilli D, Johnsen S 2010. Spatial vision in the purple sea urchin Strongylocentrotus purpuratus (Echinoidea). *Journal of Experimental Biology 213(2): 249-255*. doi:10.1242/jeb.033159. **opened (web page: https://scholars.duke.edu/publication/734169)**. Log L269-L270.
- Yoshida M, Ohtsuki H 1966. Compound Ocellus of a Starfish: Its Function. *Science 153: 197*. doi:10.1126/science.153.3732.197. **opened (abstract, collection)**. Log L221.
- Yoshida M, Ohtsuki H 1968. The phototactic behavior of the starfish, Asterias amurensis Lütken. *Biological Bulletin*. doi:10.2307/1539869. **opened (abstract, collection)**. Log L222.
- Zeil J, Al-Mutairi MM 1996. The variation of resolution and of ommatidial dimensions in the compound eyes of the fiddler crab Uca lactea annulipes (Ocypodidae, Brachyura, Decapoda). *Journal of Experimental Biology 199: 1569-1577*. doi:10.1242/jeb.199.7.1569. **opened (web page: https://cob.silverchair.com/jeb/article-pdf/199/7/1569/3391178/jexbio_199_7_1569.pdf)**. Log L172-L175.

### Data and repository files opened

- `docs/views/world-orders.csv` (order counts), `docs/views/no-view-us-fl-alachua.csv` (Alachua records), `docs/VIEWS.md`, `docs/COVERAGE.md`, `src/cam.a.js` and `src/cam.b.js` (engine fields, `GROUPS`, aperture and mosaic), `docs/views/sheets/sealife.md`, `crab.md` and their audits. **opened**.
- GBIF occurrence API, dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7, read through WebFetch on 13 October 2026: Decapoda (orderKey 637) by familyKey; Pectinida (orderKey 9250425), Arcida (orderKey 9574493) and Cardiida (orderKey 9529005) by familyKey, and Cardiidae by genusKey for *Tridacna*; family names from `https://api.gbif.org/v1/species/{key}`, the ci branch's family name lists and the earlier crab sheet's table. Findings: the decapod, scallop, ark clam and giant clam counts in section 1. **opened**.

### Secondary (cited through another work)

- Hamasaki 1968b, octopus flicker fusion: through Hanke and Kelber 2020 (L47, L48).
- Sutherland 1963 and Packard 1969, octopus acuity: through Hanke and Kelber 2020 (L44, L45) and Muntz 1986 (L109).
- Beer 1897, octopus accommodation: through Hanke and Kelber 2020 (L60).
- Kelber 2006, invertebrate pigment table: through Land and Nilsson 2012 (L1 to L24).
- Land 1981a and Land and Nilsson 1990, interreceptor angles: through Land and Nilsson 2012, Table 3.1 (L31 to L36).
- Petie and colleagues 2016a, crown-of-thorns flicker fusion: through Korsvig-Nielsen and colleagues 2019 (L217, L218).
- Messenger 1968, cuttlefish binocular field: through Feord and colleagues 2020 (L78).
- Temple and colleagues 2012, How and colleagues 2012 and 2014, and Glantz and Schroeter 2006, polarization thresholds: through Temple and colleagues 2021 (L67, L69, L70, L71).
- Groeger and colleagues 2005, cuttlefish acuity over growth: through Darmaillacq and colleagues 2017 (L133).
- Kirwan and colleagues 2018, *Diadema* acuity: through Li and colleagues 2023 (L226).
- Young 1962 and Dobson and colleagues 2014, acuity figures: through Caves, Brandley and Johnsen 2018 (L247, L248).
- Cloudsley-Thompson 1977, Warburg 1968 and Dias and colleagues 2012, woodlouse behaviour: through Fialová and Tuf 2025 (L263, L264).
- Garm and Nilsson 2014, the blue sea star's 16 degrees: through Petie, Garm and Hall 2016 (L273).

## 8. Questions for a specialist

1. How fast does the octopus or cuttlefish eye follow flicker at the brightness of an ordinary daylight scene? The classic recording used millions of candelas per square metre.
2. For a forward-looking cuttlefish with a constricted W pupil, is the blur of an out-of-focus point taller than it is wide, as this sheet assumes?
3. What are the interommatidial angles and the visual field of a common woodlouse such as *Porcellio scaber* or *Armadillidium vulgare*?
4. Do hermit crabs, crayfish and lobsters resolve detail as coarsely as cleaner shrimps (8 to 11 degrees), or closer to true crabs?
5. Do brittle stars form any spatial image, and if so at what resolution?
6. How quickly do sea anemones and corals respond to a passing shadow, and is there a measured threshold of dimming?
