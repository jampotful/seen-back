# Sensing sheet: bees, wasps and sawflies (order Hymenoptera except ants), draft

Started 13 October 2026, 01:46 UTC; this version 02:55 UTC. The evidence log is `docs/views/evidence/bee.jsonl` (245 lines) and the wanted list is `docs/views/wanted/bee.jsonl` (15 works). Every row below names the log lines behind it by source; the log gives the quote, place and grade for each.

What was read. The literature collection on `pub/lit-t1` (topics `bees-wasps` and `insects-general`), full texts on disk and abstracts in the index. Three works from the owner's library: van der Kooi et al. 2021 (whole paper), Land 1997 (whole paper), and Land and Nilsson 2012, *Animal Eyes*, which came through only in part: the front matter, Chapter 1, Chapter 2 and Chapter 3 up to "Available photon numbers" (about pages 1 to 63). Chapters 4 to 9, including Chapter 7 on apposition compound eyes and Chapter 9 on eye movements, did not come through. Caves et al. 2018 arrived in the library's "General and methods" folder during this session and was read, because it is the paper behind the app's current sharpness row. Web pages were read through the fetch tool where the machine's own network refused the site (GBIF, iNaturalist, Europe PMC, PubMed and Crossref all refused direct requests from this machine; the record counts below therefore come from data already in the repository).

## 1. Scope

The `bee` view covers the order Hymenoptera except ants (family Formicidae), by the rule in `docs/CONTRACTS.md`. That is the bees, the stinging wasps (paper wasps, yellowjackets, hornets, potter wasps, mud daubers, digger wasps, sand wasps, velvet ants, scoliid and spider wasps), the parasitoid wasps, the gall wasps, and the sawflies and horntails.

**Record counts.** World figures are iNaturalist research-grade records in GBIF, read on 11 October 2026 as family facets (`runs/fetch/10/world-family-top.json` on the `ci` branch). Hymenoptera holds 4,555,326 records, ants 674,113, so the unit holds 3,881,213. The name tables in that run cover only 3,000 of GBIF's 17,449 animal families, so 726,146 records (18.7%) sit in families that can be counted there but not named. For those, lower bounds come from the iNaturalist snapshot of 27 September 2026 (`runs/coverage/1-lists/world.tsv.gz`), assigning a species to a family when its genus appears in the Alachua list under that family; about 285,000 records stay unassigned. GBIF's backbone splits the vespid wasps oddly (it files *Polistes* under "Eumenidae" and *Eumenes* under "Vespidae"), so the two are counted together. Alachua figures are exact, from `data/regions/us-fl-alachua/species.json` (records through 2024).

| Side | World share of the unit | Alachua records (share) | Most recorded in Alachua | Most recorded in the world |
|---|---|---|---|---|
| Bees (Apidae, Halictidae, Megachilidae, Andrenidae, Colletidae, Melittidae) | at least 55.5% (Apidae 48.3% exact) and at most 62.8% | 1,948 (45.9%) | Western Honey Bee 469, American Bumble Bee 311, Common Eastern Bumble Bee 256, Poey's Furrow Bee 191, Brown-winged Striped Sweat Bee 188, Eastern Carpenter Bee 137 | *Apis mellifera* 548,372; *Bombus impatiens* 239,293; *Xylocopa virginica* 101,040; *Bombus griseocollis* 91,620 |
| Vespid wasps (paper wasps, yellowjackets, hornets, potter wasps) | 17.4% (exact) | 1,167 (27.5%) | Mexican Paper Wasp 170, Southern Yellowjacket 136, Metric Paper Wasp 129, Guinea Paper Wasp 102 | *Polistes dominula* 60,895; *Dolichovespula maculata* 42,447; *Polistes fuscatus* 40,248; *Vespula germanica* 32,361 |
| Other stinging wasps (Sphecidae, Crabronidae, Scoliidae, Mutillidae, Pompilidae, Chrysididae, Tiphiidae) | at least 8.8% | 829 (19.5%) | Common Eastern Velvet Ant 185, Eastern Cicada-killer 79, Great Golden Digger Wasp 64, Yellow-legged Mud-dauber 60 | *Sceliphron caementarium* 31,553; *Sphex ichneumoneus* 24,011; *Sphecius speciosus* 21,061 |
| Parasitoid wasps (ichneumonids, braconids, chalcids and others) | at least 2.2% | 168 (4.0%) | *Limonethe maurator* 24, *Neotheronia bicincta* 15, Long-tailed Giant Ichneumonid 11 | *Megarhyssa macrurus* 3,370 among genera mapped |
| Gall wasps (Cynipidae) | 7.9% (exact) | 101 (2.4%) | leafy oak gall wasp 30, *Belonocnema treatae* 27 | *Andricus quercuscalifornicus* 13,575; *Neuroterus quercusbaccarum* 11,754 |
| Sawflies and horntails (suborder Symphyta) | at least 0.8% | 32 (0.75%) | Red-headed Pine Sawfly 15, Asian Horntail 6 | *Tremex columba* 5,418; *Cimbex americanus* 2,784 among genera mapped |
| Not assigned to a family here | at most 7.3% | 0 | | |

World "most recorded" figures are the snapshot's all-time research-grade counts, which run a little ahead of the GBIF facets.

### Where the view should split

**Bees against wasps: split.** The two sides share their colour system: the bees and wasps measured have ultraviolet, blue and green receptors peaking near 345, 440 and 535 nm, varying by a few tens of nanometres across species (van der Kooi et al. 2021, Table 1, for 27 Apidae, four vespids, *Philanthus* and others; Hempel de Ibarra et al. 2014; Skorupski and Chittka 2011). Colour alone would not justify two views. What does justify it:

- The picture differs. Paper wasps, yellowjackets and hornets have a notch of cuticle at the front of each eye (Kelber et al. 2011, who say all vespids have it). In the two yellowjackets measured, it divides the eye into a lower half sampling at 1.0 to 1.5 degrees and an upper half at 2.0 to 3.0, a sharp step just above the horizon (Gutiérrez et al. 2024, for *Vespula germanica* and *V. vulgaris*), and the authors say the notch is found "in many wasps (but not bees)". Bees have no such seam; their sharp zone grades smoothly into a band along the horizon (Land 1997; Rigosi et al. 2017).
- The overall sharpness is about the same. The yellowjackets' acute zones sample at 1.0 to 1.5 degrees and the hornet's at 1.0, against the honeybee's 1.2 in its acute region (Seidl 1982, via Taylor et al. 2019). Sand wasps reach 0.41 degrees (Land 1997, *Bembix palmata*), and across 77 apoid species hunting wasps have larger eyes for their head size than bees (Trisoglio et al. 2026), so some wasps are sharper than any bee.
- The rows differ most. Nearly everything known about bees beyond colour (electric fields of flowers, the honeybee's 200 Hz pace, the magnetic sense, dance hearing, flower ultraviolet) was measured in bees and would be wrong or untested behind a wasp's name. Wasps have their own measured facts: face recognition in paper wasps (Tibbetts 2002; Caves et al. 2018), dusk flight in hornets (Kelber et al. 2011).

Share: bees 55.5 to 62.8% of world records and 45.9% of Alachua's; wasps (vespid, other stinging and parasitoid wasps together) at least 28.4% of world records and 51.0% of Alachua's.

**Gall wasps: split, provisionally.** Gall wasps hold 7.9% of the unit's world records. Their iNaturalist names ("leafy oak gall wasp", "Banded Bullet Gall Wasp") suggest that many records show the gall, a plant growth with a grub inside, and the grub has no eyes: in the rose gall wasp *Diplolepis triforma* the compound eyes begin to form only after feeding ends (Shorthouse and Leggo 2002). A bee's picture is false for a gall. The share of cynipid records that show a gall was not measured here (iNaturalist's life-stage and "gall" annotations would measure it), so this split depends on that check. If most records show adults, gall wasps join `wasp`.

**Sawflies and horntails: a colour setting inside `wasp`.** The horntail *Sirex noctilio* has only ultraviolet (364 nm) and green (527 nm) receptors and lacks the blue opsin gene. Earlier recordings found no blue receptor in any sawfly or woodwasp except *Tenthredo campestris*, and found a fourth, red receptor in *T. campestris*, *T. scrophulariae* and the woodwasp *Xiphydria camelus* (Guignard et al. 2021, reviewing Peitsch et al. 1992; van der Kooi et al. 2021 list *T. campestris* at 337, 458, 537 and 602 nm). That makes a bee or wasp colour picture false for them. At under 1% of records, and with larvae (which have only simple larval eyes, unstudied here) making up an unknown share of those, a separate group in the pocket model is not worth it: when the full database names a sawfly or horntail, the `wasp` view should switch to a two-colour setting.

**Bumblebees against honeybees: no split.** Their acuity is about the same (honeybee 0.26 cycles per degree, *Bombus terrestris* 0.21 to 0.25, *B. impatiens* 0.35; Land 1997; Kelber and Somanathan 2019; Chakravarthi 2017), their receptors match, and the measured differences (electric hairs in bumblebees, an antennal electric sense in honeybees, somewhat slower receptors in *B. impatiens*) belong in the rows and leave the picture unchanged. Body size changes acuity within both (Spaethe and Chittka 2003; Taylor et al. 2019), which belongs to species settings (Section 4).

**Velvet ants and parasitoid wasps: inside `wasp`, with rows.** Female velvet ants are wingless and walk; males find them by scent (VanderSal et al. 2016). Tiny parasitoids have eyes under a tenth of a millimetre long (Fischer et al. 2010, *Trichogramma*). Neither has enough measured vision for a picture of its own.

**Night fliers: settings, no split.** Hornets fly into deep twilight (Kelber et al. 2011), and a few bees forage at night (*Megalopta*, *Xylocopa tranquebarica*; Warrant 2008; Kelber et al. 2005), but none of the night bees is commonly photographed. A brightness lift for the genus *Vespa* is a species setting.

**The set of views.** `bee` for all bees; `wasp` for every other member of the unit except gall wasps, with a two-colour setting for sawflies and horntails and a dusk setting for hornets; and `gall` for gall wasps, provisional on the life-stage check. Splitting changes the labels the pocket model's group head learns, so the owner decides; every photo in `pub/data-world` carries its iNaturalist taxon, so a head can be refitted on these groups without new photos (`docs/COVERAGE.md`).

## 2a. The view `bee`

### Rows

- `['m', 'Sharpness', 'In bright light a honeybee sees about a two-hundredth as much detail as a person does, and in dim light about half that. A flower one centimetre across shows up for a honeybee only from 12 to 18 centimetres away. This view is blurred to match, and more so in dim light.']`
  Log: Land 1997 reporting Srinivasan and Lehrer 1988 (acuity_cpd 0.26); Kelber and Somanathan 2019 (acuity_cpd 0.25 in bright light and 0.12 in dim light; behaviour_vision, flowers at 3-5 degrees); Hecht and Wolf 1929 (acuity_cpd, a hundredth of a person's, lower at low light). 60 / 0.26 = 230. Bumblebees are about the same (Kelber and Somanathan 2019: *Bombus terrestris* 0.21, *B. impatiens* 0.35-0.36; Chakravarthi 2017: 0.25).
- `['m', 'Sharpest part', 'A bee sees most sharply just below straight ahead, where flowers and the nest entrance appear as it comes in to land, and along a band level with the horizon. Detail falls away toward the sides and behind. This view is sharpest a little below the middle of the picture.']`
  Log: Kelber and Somanathan 2019 (fovea, fronto-horizontal region in females); Rigosi et al. 2017 (acceptance_deg 1.9 frontally, 1.6 just ventral, widening with eccentricity); Land 1997 (fovea, forward-flight pattern); DLR bee eye model (eyes_count; interommatidial 2.4 to 4.6 degrees horizontally).
- `['m', 'Field of view', 'A honeybee's two eyes together take in about 310 degrees around it, leaving only a narrow blind wedge behind, and their fields overlap in front and above. A phone camera sees far less, so this view bends the picture at its edges to suggest the wider sweep.']`
  Log: Taylor et al. 2019 reporting Seidl and Kaiser 1981 (fov_h_deg 312); Kelber and Somanathan 2019 (binocular_deg 50-60; fov_h_deg, small blind region below and behind).
- `['m', 'Colour', 'Bees have three kinds of colour-sensing cells, tuned to ultraviolet, blue and green light. People also have three, but ours reach further into red and miss ultraviolet. Bees measured so far, from honeybees and bumblebees to mining bees and mason bees, have nearly the same three.']`
  Log: van der Kooi et al. 2021 (lambda_max_nm for *Apis*, *Bombus*, *Andrena*, *Osmia*, *Xylocopa* and others; receptor_classes 3); Hempel de Ibarra et al. 2014 (344, 436, 544 nm); Skorupski and Chittka 2011 (*B. impatiens* 348, 424, 539 nm); Lunau et al. 2025 (spectral_range_nm, bees see UV and people see red better).
- `['m', 'Red', 'Red looks dim to a bee, because its green-sensing cells catch only the edge of red light. Red flowers stay visible to bees, and the red flowers that bees pollinate usually also reflect ultraviolet, which makes them bright to a bee. This view darkens reds.']`
  Log: Chittka and Waser 1997 (spectral_range_nm, sensitivity extends into red); Lunau et al. 2025 (behaviour_vision, red bee flowers are bee-UV and red bird flowers bee-black); DLR photoreceptor page (UV but not far red).
- `['g', 'Ultraviolet patterns', 'Many flowers carry patterns in ultraviolet light that people cannot see. Marsh marigolds, which look plain yellow to us, have dark centres in ultraviolet, and the white flowers that bees pollinate mostly absorb it, so a bee sees them as blue-green.']`
  Log: Land and Nilsson 2012 (behaviour_vision, *Caltha palustris*, Fig. 2.4); Lunau et al. 2025 (behaviour_vision, white flowers bee-bluegreen; UV bull's eye; flowers mostly UV-absorbing).
- `['i', 'Ultraviolet in this view', 'Phone cameras record almost no ultraviolet, so this view guesses it. The guess gives ultraviolet to the open sky and to bluish surfaces and keeps it off white flowers, so the patterns on real flowers are missing. Colours are shifted by one, as in researchers' photographs of what bees see: a bee's green appears as red, its blue as green, and its ultraviolet as blue.']`
  Log: Igoe et al. 2012 (spectral_range_nm, the phone's optics pass 1.1% at 340 nm); Lunau et al. 2025 (colour_vision, the false-colour convention); Kelber and Somanathan 2019 (lambda_max_nm of the ocelli, UV-green contrast at the sky's edge).
- `['m', 'Colour and detail', 'A bee uses colour only for things that fill a wide part of its view. Small or distant things it sees only as lighter or darker, through its green-sensing cells alone. This view lays colour on in broad, soft patches and draws fine detail in a single colour.']`
  Log: Giurfa et al. 1996 (behaviour_vision, 5 degrees with green contrast, 15 without); Hempel de Ibarra et al. 2014 (colour_vision, separate channels; colour neurons' fields of 30 to 70 degrees; behaviour_vision, the 5 to 15 degree window); Lunau et al. 2025 (colour_vision, colour from about 5 degrees).
- `['m', 'Speed', 'In bright light a honeybee can follow a pattern flickering past its eyes up to about 200 times a second, and about 144 times in light ten times dimmer. People stop at about 60. This view runs slowly and then jumps ahead to suggest the difference, and it slows less in dim light.']`
  Log: Srinivasan and Lehrer 1984, moving stimuli (cff_hz 200); Inger et al. 2014 (cff_hz 144 at 300 lux, 200 at 3000 lux; cff_hz 60 for people).
- `['m', 'Glances', 'A flying bumblebee holds its gaze steady, then turns its head in a quick snap lasting between a twentieth and a seventh of a second, and holds again. Between snaps, the speed at which things slide past tells it how near they are and how fast it is flying. Turn your phone slowly and this view holds still, then snaps.']`
  Log: Boeddeker et al. 2015 (eye_movement; depth_cue); Srinivasan et al. 1996, Baird et al. 2005 and Linander et al. 2015 (motion); Kelber and Somanathan 2019 (motion, distance from green contrast).
- `['x', 'Sky compass', 'A strip of special cells along the top edge of each eye reads the pattern of polarized light in the sky, which shows where the sun is even behind cloud. Three small simple eyes on top of the head watch the sky and horizon and help in dim light. Phones cannot sense polarized light, so this view leaves the compass out.']`
  Log: Land and Nilsson 2012 (polarization); Schinz 1975 (polarization, dorsal rim of at least 60 ommatidia); Kolyfetis et al. 2025 (polarization; lambda_max_nm 340); Lunau et al. 2025 (polarization, UV receptors of the dorsal rim); Kelber and Somanathan 2019 (eye_role and absolute_sensitivity of the ocelli); Hung and Ibbotson 2014 (eye_role); Araújo et al. 2024 (polarization in ocelli).
- `['x', 'Electric fields and other senses', 'Bumblebees feel the faint electric field around a flower through the hairs on their bodies when they come within about ten centimetres, and a flower's field changes within seconds after a charged bee visits. Honeybees also smell, and they hear the low hum of a dancing nestmate through their antennae. This view leaves these senses out.']`
  Log: Clarke et al. 2013 (sense_electric); Sutton et al. 2016 (sense_electric, hairs); Clarke et al. 2017 (sense_electric, 10 cm and field thresholds; sense_chemical); Greggers et al. 2013 (sense_electric, antennae); Kirchner 1993 (sense_hearing up to 500 Hz; dances at 200 to 300 Hz).

The magnetic sense is logged (Walker and Bitterman 1989: trained bees detect a 260 nT change, 0.6% of the background field; Kirschvink et al. 1997) and left out of the rows to keep them at twelve; it can replace the electric row's second sentence if the owner prefers it.

### The picture

| Field | Value | Behind it |
|---|---|---|
| `fov` | 310 (now 320) | Taylor et al. 2019 reporting Seidl and Kaiser 1981: each eye reaches 156 degrees back at the horizon, 2 × 156 = 312 |
| `cpd` | 0.3 in bright light, falling to 0.15 in dim light (now 1) | Srinivasan and Lehrer 1988 via Land 1997 (0.26, bright light); 1 / (2 × 1.7) = 0.29 from the frontal interommatidial angle (Rigosi et al. 2017); *Bombus* 0.21 to 0.36; honeybee gratings 0.25 in bright and 0.12 in dim light (Kelber and Somanathan 2019, Table 3); the retina's own limit is higher, 0.54 (see below) |
| `topoA` | 1, magnitude invented | frontal acute zone (Rigosi et al. 2017; Land 1997) |
| `topoS` | 0.5, magnitude invented | equatorial band of finer vertical sampling (Land 1997) |
| `fall` | 0.9, invented as one number | the DLR model, built on Seidl and Kaiser 1981, varies the horizontal angle from 2.4 to 4.6 degrees; in flying insects it is smallest in front and grows toward the back (Land 1997); acceptance angles widen with eccentricity (Rigosi et al. 2017) |
| acute-zone centre (new) | about 8 degrees below the middle, size invented | fronto-ventral acute zone, "just ventral to the frontal body axis" (Rigosi et al. 2017; Kelber and Somanathan 2019) |
| `pupil` | 'none' | a compound eye has no single aperture to shape out-of-focus blur; no log line, the engine's convention |
| `dof` | 0, invented | no source opened on focusing in bee eyes |
| `M` | `[0.15, 0.85, 0, 0, 0, 1, 0, 0, 0]` (now `[0, 1, 0, 0, 0, 1, 0, 0, 0]`) | the shift by one is the published convention (Lunau et al. 2025, citing Verhoeven et al. 2018); the 0.15 of camera red in the bee's green is invented, from the green receptors' reach into red (Chittka and Waser 1997) |
| `uvBlue` | 1, with a changed guess | invented; see effect 3 |
| `sat` | 1 | no change |
| `gain` | 1 | bees are day fliers; resolution fails below room light in diurnal insects (Land 1997) |
| `rate` | 0.3 in bright light, rising to 0.42 in dim light | 60 / 200 = 0.3 at 3000 lux and 60 / 144 = 0.42 at 300 lux (Srinivasan and Lehrer 1984; Inger et al. 2014) |
| `persist` | 0 | the green receptors that drive motion vision integrate over 7.9 to 11.3 ms in bumblebees (Skorupski and Chittka 2010, 2011), less than a 16.7 ms screen frame, so no trails |
| `gate`, `hold`, `thrust`, `sheen`, `noGreen`, `field` | 0 | no evidence for them |
| glances (new) | hold up to 20 degrees of phone turn, snap in 80 ms; threshold invented | saccades of 5 to 60 degrees, typically lasting 45 to 135 ms (Boeddeker et al. 2015) |
| colour scale (new) | colour sampled about 1.6 mip levels coarser than brightness, invented | detection at 5 degrees with green contrast and 15 degrees with colour only, a factor of 3 (Giurfa et al. 1996); log2(3) = 1.6 |
| cue | "Colour comes in soft patches and detail in one colour. Turn slowly and the picture holds, then snaps." | |

At `cpd` 0.3 on a phone (`VIEW_DEG` 24), the engine's blur radius is 0.6 × (long side in pixels / 24) / 0.3, about a twelfth of the screen's long side. That is very soft, and it is what a honeybee's eye keeps of that screen. The present value of 1 draws a bee three to four times too sharp.

**A fork in "sharpness", for the owner.** Two measured figures differ by a factor of two. What a trained honeybee acts on in grating tests is 0.25 to 0.26 cycles per degree (Srinivasan and Lehrer 1988; Kelber and Somanathan 2019). What its retina passes, recorded from the lamina by pattern electroretinogram, is 0.54 (Ryan et al. 2020, through Penmetcha et al. 2025, who note that the two kinds of estimate typically disagree in honeybees). For people the two measures nearly coincide: the eye's optics and its mosaic both limit it near 60 (Land 1997), and behaviour gives roughly 60 at the centre of gaze (Caves et al. 2018), so the engine's ratio does not settle which bee figure to use. This sheet uses the behavioural figure, 0.3, because the view is meant to show what the animal makes of the scene; the retina's figure would make `cpd` 0.5 and halve the blur.

### New effects

1. **Colour in soft patches, detail in one colour.** What the person sees: colour pools in broad, soft regions while edges and small things are drawn crisply in the bee's green channel, which shows as red. A small flower far away is a dark or light speck; as the phone comes closer it takes on colour. Phone input: the camera alone. Difficulty: low. The space-and-colour pass already samples a mip chain, so chroma can be read about 1.6 levels coarser than brightness for one extra texture read per tap. What makes it beautiful and true: the bloom of colour as you approach a flower is the behaviour Giurfa et al. 1996 measured, and the watercolour look comes straight from the separation of the bee's two channels (Hempel de Ibarra et al. 2014).
2. **Glances.** What the person sees: when they turn the phone, the picture stays put, then snaps to the new direction in a blink; walking straight ahead, the world streams past. Phone input: the gyroscope's rotation rate (behind the motion flag; iOS asks on a tap). Difficulty: medium. It extends the heron's `hold` and `thrust` from walking to turning: shift the image against the accumulated turn, fill the edge from the existing mirrored border, and release in 80 ms when the turn passes a threshold or after half a second. Beautiful because it gives the view a held, deliberate stillness broken by quick looks, which is how bumblebee heads move (Boeddeker et al. 2015).
3. **A better ultraviolet guess.** What the person sees: the open sky and blue things carry the false ultraviolet blue; white flowers no longer do, so they show as the bee's blue-green. The shader now adds ultraviolet to anything bright and white (`2.5 * max(mn - 0.6, 0.0)` in `src/cam.b.js`), which draws most white flowers wrongly, since bee-pollinated white flowers absorb ultraviolet (Lunau et al. 2025). Drop that term and keep the blueness term; optionally weight it toward the top of the frame, where the sky usually is (the sky's ultraviolet against green ground is what bee ocelli use to find the horizon; Kelber and Somanathan 2019). Difficulty: trivial. True to the flowers, and the row says what is guessed.
4. **Pace and sharpness that follow the light.** What the person sees: in sun the picture steps slowly and holds its detail; indoors and at dusk it steps less and grows softer, about twice as blurred in dim light. Phone input: the camera's exposure time and gain where the browser reports them (`track.getSettings()`), or an ambient light sensor where present; the mean frame brightness alone is unreliable because the camera adjusts its exposure. Difficulty: low. True to the 200 Hz and 144 Hz values at two light levels (Srinivasan and Lehrer 1984; Inger et al. 2014) and to acuity halving in dim light (Kelber and Somanathan 2019; Hecht and Wolf 1929).
5. **Sharp zone a little low.** What the person sees: the sharpest patch sits just under the middle, where a landing bee's flower would be, and a faint band of extra sharpness runs along the horizon. Difficulty: low (one uniform for the zone's vertical offset; `topoS` exists).
6. **Optional, invented drawing: the sky compass.** What the person sees: when the sun is in the frame or near it, faint concentric bands across the sky around the sun, strongest about 90 degrees away from it, standing for the pattern of polarized light a bee reads. Phone input: the brightest region of the frame for the sun, and orientation sensors to keep the bands fixed to the sky as the phone turns. Difficulty: medium to high. The geometry of the pattern is measured (Land and Nilsson 2012, Fig. 2.7: e-vectors arranged concentrically around the sun, polarization strongest at 90 degrees); the drawing would be the app's own and its row would be graded `i`.
7. **Optional: brightness tuned to small things.** Bees detect a target by green contrast alone only when it spans 5 to 15 degrees, and lose a large target of pure brightness contrast up close (Giurfa and Vorobyev 1998, via Hempel de Ibarra et al. 2014). A partial band-pass on the brightness channel (subtracting a broad blur) would let small things pop and large flat areas fade toward mid-tone. Difficulty: medium (one more blurred read). Strength invented; try at a third.
8. **A contrast floor.** What the person sees: faint gradations drop away, such as soft shading on a petal, the haze in a sky or a pale pattern on bark, while strong edges stay; in a small-bee setting more of the faint detail goes. Phone input: the camera alone. Difficulty: medium. Take local contrast as a pixel's difference from a broad blur, divided by that blur, and soft-threshold it at the animal's threshold: 6% for the honeybee and about 17% for the small stingless bee *Tetragonula carbonaria* (pattern electroretinograms at a coarse grating of 0.05 cycles per degree; Ryan et al. 2020 via Penmetcha et al. 2025). A single threshold is the simple version; the measured threshold rises toward the blur limit (Penmetcha et al. 2025, Fig. 3a), and a version that reads the mip chain band by band would follow it. Applying a retinal threshold to the whole picture is invented. What makes it true: it shows the second limit on a bee's eye besides blur, and it is the setting that separates small bees from honeybees in the evidence above.

## 2b. The view `wasp`

### Rows

- `['m', 'Sharpness', 'Yellowjackets, hornets and paper wasps see about as much detail as a honeybee, which is less than a hundredth of what people see. Sand wasps, which hunt flies, see more than twice as sharply in a forward patch that they use to track prey. This view is blurred to match a yellowjacket.']`
  Log: Gutiérrez et al. 2024 (interommatidial_deg 1.0 and 1.5); Kelber et al. 2011 (interommatidial_deg 1.0, *Vespa crabro*); Caves et al. 2018 (interommatidial_deg about 1, *Polistes*); Taylor et al. 2019 (interommatidial_deg, honeybee acute region 1.2); Land 1997 (interommatidial_deg 0.41 and acuity_cpd 1.22, *Bembix palmata*, the forward acute zone "used for tracking prey"); Trisoglio et al. 2026 (*Bembix* among the fly-hunters). 1 / (2 × 1.0) = 0.5 cycles per degree at best, a hundred-and-twentieth of 60.
- `['m', 'Split eye', 'A notch at the front of each eye divides it into an upper and a lower part in paper wasps, yellowjackets and hornets. In yellowjackets, the lower part looks just below straight ahead and sees about twice as sharply as the upper part. This view is sharper below the horizon than above it.']`
  Log: Gutiérrez et al. 2024 (interommatidial_deg 2.0-3.0 in the upper half; fovea; acceptance_deg 1.59 frontal and 2.82 lateral); Kelber et al. 2011 (eye_type, the indentation in all vespids).
- `['m', 'Colour', 'Wasps have the same three kinds of colour-sensing cells as bees, tuned to ultraviolet, blue and green, and reds look dim to them. A tropical paper wasp has learned to pick out a blue card among cards of other colours and greys.']`
  Log: van der Kooi et al. 2021 (lambda_max_nm for *Vespula germanica*, *V. vulgaris*, *Vespa crabro*, *Polistes dominula*, *Philanthus triangulum*); Shafir 1996 (colour_vision, *Polybia occidentalis*, no red receptor).
- `['m', 'Faces', 'Northern paper wasps recognize their nestmates by the yellow markings on their faces. With their eyesight, a wasp can make out such marks only from a few centimetres away, so recognition happens face to face.']`
  Log: Tibbetts 2002 (behaviour_vision); Caves et al. 2018 (interommatidial_deg about 1; marks resolved from 1 to 5.7 cm).
- `['m', 'Hunters' eyes', 'Hunting wasps have larger eyes for the size of their heads than bees do. Bees descend from hunting wasps, and their eyes became relatively smaller when they switched from prey to pollen, which they gather by landing on flowers.']`
  Log: Trisoglio et al. 2026 (behaviour_vision).
- `['m', 'Hornets at dusk', 'European hornets keep flying deep into twilight and on moonlit nights, in light about a hundred times dimmer than common wasps need. Their eyes look much like a daytime wasp's, and their large size lets them gather more light.']`
  Log: Kelber et al. 2011 (absolute_sensitivity; diel).
- `['g', 'Field of view', 'Wasps, like bees, take in nearly the whole circle around them. This view bends the picture at its edges to suggest the wider sweep.']`
  Log: Taylor et al. 2019 reporting Seidl and Kaiser 1981 (fov_h_deg 312, honeybee); Kelber and Somanathan 2019 (fov_h_deg).
- `['i', 'Speed', 'How fast a wasp's eyes work appears not to have been measured. This view borrows the honeybee's pace, on the guess that a wasp's eyes are as quick as a bee's.']`
  Log: Srinivasan and Lehrer 1984 (cff_hz 200, honeybee), borrowed; Skorupski and Chittka 2010 (corner_hz, bumblebee speeds).
- `['i', 'Ultraviolet in this view', 'Phone cameras record almost no ultraviolet, so this view guesses it. The guess gives ultraviolet to the open sky and to bluish surfaces and keeps it off white flowers. Colours are shifted by one, as in researchers' photographs of what bees see: green appears as red, blue as green, and ultraviolet as blue.']`
  Log: as the bee's row.
- `['g', 'Small wasps', 'Many wasps are tiny parasites of other insects, and the smallest have eyes less than a tenth of a millimetre long, with facets about six thousandths of a millimetre wide. This view gives every wasp a yellowjacket's eyesight, so it is far too sharp for them.']`
  Log: Fischer et al. 2010 (eye_type, *Trichogramma evanescens*).
- `['x', 'Smell', 'Wasps find prey by smell as well as by sight, and male velvet ants find the wingless females by scent alone. This view leaves smell out.']`
  Log: Gutiérrez et al. 2024 (sense_chemical, citing Raveret et al.); VanderSal et al. 2016 (sense_chemical, *Dasymutilla*).

Setting for sawflies and horntails (replaces the Colour row when the full database names one):

- `['m', 'Colour', 'Horntails see with only two kinds of colour-sensing cells, for ultraviolet and green, and lack the blue kind that bees and other wasps have. Most sawflies measured also lack blue, and a few have a fourth kind sensitive to red. This view shows sawflies and horntails in two colours.']`
  Log: Guignard et al. 2021 (lambda_max_nm 364 and 527; receptor_classes 2; receptor_classes for Symphyta, red in *Tenthredo* and *Xiphydria*); van der Kooi et al. 2021 (lambda_max_nm for *Tenthredo campestris*, 602 nm).

### The picture

| Field | Value | Behind it |
|---|---|---|
| `fov` | 310 | borrowed from the honeybee (Taylor et al. 2019 reporting Seidl and Kaiser 1981); the wasp's whole field is unmapped |
| `cpd` | 0.3 below the horizon, as for `bee`, and 0.18 above; sand-wasp setting 0.6 below | lower half 1.0 to 1.5 degrees in the acute zone, about the honeybee's 1.2 (Gutiérrez et al. 2024; Taylor et al. 2019), so the bee's 0.3 carries over (`g`); the upper half's smallest angles are almost twice the lower half's (2.0 against 1.0 degrees in *V. germanica*, 2.2 against 1.5 in *V. vulgaris*), so about 0.3 / 1.7 = 0.18; *Bembix palmata* 0.41 degrees, 2.4 times finer than 1.0 (Land 1997) |
| `topoA` | 1, centred about 10 degrees below the middle; magnitude invented | acute zone at latitude −10 to −20 degrees in *V. germanica* (Gutiérrez et al. 2024) |
| `fall` | 0.8 | lateral acceptance angle 2.82 against 1.59 frontally, a factor of 1.8 (Gutiérrez et al. 2024) |
| `M` | as `bee`; sawfly setting `[0.15, 0.85, 0, 0.15, 0.85, 0, 0, 0, 0]` with ultraviolet in blue | same receptors as bees (van der Kooi et al. 2021); the two-colour mapping (the green receptor as yellow, ultraviolet as blue, camera blue discarded) is invented to suit an ultraviolet-green eye (Guignard et al. 2021) |
| `uvBlue` | 1, the changed guess | invented, as for `bee` |
| `gain` | 1; hornet setting 1.4, magnitude invented | hornets fly in light about a hundred times dimmer than common wasps (Kelber et al. 2011) |
| `rate` | 0.3, borrowed (`i`) | honeybee (Srinivasan and Lehrer 1984) |
| `persist` | 0 | borrowed from bees' fast receptors |
| `pupil`, `dof` | 'none', 0 | as `bee` |
| glances | as `bee`, borrowed (`i`) | bumblebees measured (Boeddeker et al. 2015); wasps' learning flights are known to include zigzags (Kelber and Somanathan 2019 cite Zeil's work) but were not logged as numbers |
| cue | "Sharper below the horizon than above. Turn slowly and the picture holds, then snaps." | |

### New effects

1. **The split eye.** What the person sees: everything below the horizon is drawn about twice as sharply as everything above it, with a faint doubled strip just above the horizon where both halves of the eye see the same band (Kelber et al. 2011 describe a region near 10 degrees elevation seen twice). Phone input: the accelerometer's gravity direction, so the seam stays level as the phone tilts. Difficulty: low to medium, using the engine agent's band zones with a gravity-driven horizon. Beautiful in the way a split-field filter is, and it follows the notched eye exactly.
2. **Hornet dusk.** For the genus *Vespa*, a lift in the shadows when the scene is dim. Phone input: frame brightness. Difficulty: trivial once species settings exist.
3. **Two-colour sawflies.** The matrix above, for Symphyta. Difficulty: trivial once species settings exist.

## 2c. The view `gall` (provisional)

### Rows

- `['g', 'No eyes yet', 'The grub inside a gall has no eyes. In the rose gall wasp, the eyes begin to form only after the grub stops feeding and starts to turn into an adult.']`
  Log: Shorthouse and Leggo 2002 (eyes_count).
- `['g', 'Life in a chamber', 'A young grub feeds over the whole inner surface of its chamber, and an older one feeds only at one end. This view shows no picture of the world outside the gall.']`
  Log: Shorthouse and Leggo 2002 (eyes_count, abstract on feeding).
- `['g', 'A long wait', 'A rose gall wasp spends autumn and winter inside its gall as a resting grub and turns into an adult in spring.']`
  Log: Shorthouse and Leggo 2002 (abstract on the prepupal phases).
- `['i', 'Light through the wall', 'This view shows only the dim light that might reach the grub through the gall's wall, warmed and slowed. That is a guess. It assumes that some light passes through the wall, and the grub may not sense light at all.']`
  Log: none; invented.
- `['g', 'The adult', 'Adult gall wasps have compound eyes, and a related wasp that has been measured sees ultraviolet, blue and green, as bees do.']`
  Log: Brown et al. 1998 (receptor_classes, *Trybliographa rapae*); Shorthouse and Leggo 2002 (compound eyes form in the prepupa).
- `['x', 'Taste and touch', 'Little is known about how the grub senses its chamber. This view leaves those senses out.']`
  Log: Shorthouse and Leggo 2002 (feeding; no sensory study found).

### The picture

`field: 1` (no image; the grub has no eyes, Shorthouse and Leggo 2002), `persist: 2.5` (slow, invented), `sat: 0.3` (invented), and a warm cast (invented). The engine's plant view already draws light without an image; this is that mode with the app's own tint. No new effect is needed.

## 3. The existing view `bee`, checked

`docs/SOURCES.md` backs the bee lines with Caves et al. 2018 (through a Duke summary), the DLR Insect Vision pages, and Inger et al. 2014. Each was opened at its source in this session.

| Item in `src/cam.a.js` | Verdict | Evidence |
|---|---|---|
| `chip: 'Bee'`, `who: 'a bee'` | corrected once the split is made: `wasp` and `gall` need their own chips | Section 1 |
| `fov: 320` | confirmed within 3%; 310 suggested | 312 degrees (Taylor et al. 2019 reporting Seidl and Kaiser 1981) |
| `cpd: 1` | corrected to 0.3 | honeybee 0.26 behavioural (Srinivasan and Lehrer 1988 via Land 1997), 0.29 anatomical, 0.54 at the retina by pattern electroretinogram (Ryan et al. 2020 via Penmetcha et al. 2025); bumblebees 0.21 to 0.36; Caves et al. 2018 give a median of 0.25 across insects. Even the retina's figure is half the present value |
| `pupil: 'none'` | confirmed as the engine's convention for a compound eye | no shaped aperture; light-adapting pigment acts as a pupil on each facet (Rigosi et al. 2017) without shaping defocus |
| `M: BEE` | confirmed as the published false-colour convention; a small red leak suggested | Lunau et al. 2025 (Verhoeven et al. 2018); Chittka and Waser 1997 |
| `uvBlue: 1` | the stand-in is acknowledged in the rows; the shader's rule is corrected | the white-boost term makes white flowers bee-white, where bee-pollinated white flowers absorb ultraviolet (Lunau et al. 2025) |
| `rate: .3` | confirmed for bright light (3000 lux); the light condition that `docs/SOURCES.md` lists as unstated is in Inger et al. 2014 | 200 Hz at 3000 lux, 144 Hz at 300 lux, from Srinivasan and Lehrer 1984, moving stimuli |
| cue "Red turns dark, and the picture runs slowly, then jumps ahead." | still true; to be replaced with the new picture's cue | |
| row `g` Sharpness, "Most insects see less than a sixtieth as much detail as people do." | confirmed as a statement about insects; corrected for bees, which see about a two-hundredth, and the grade can become `m` | Caves et al. 2018: 98% of insect values below 1.0 cycles per degree, median 0.25 |
| row `m` Red, "Bees have no colour-sensing cells for red, so red flowers and objects look dark to them." | corrected: the first clause holds for every commonly photographed bee (one Brazilian mining bee, *Callonychium petuniae*, has a class at 593 nm; van der Kooi et al. 2021); the second is half true, since bees see red weakly and many red bee flowers reflect ultraviolet | Chittka and Waser 1997; Lunau et al. 2025; DLR page (UV but not far red; no peaks or sources on the page) |
| row `m` Speed, "In bright light, a honeybee can see a light flicker up to 200 times a second, where people stop at about 60." | number and light condition confirmed; wording corrected: the measure is the limit for telling a moving, flickering pattern from a still one, and bees are poor at telling a light whose brightness alone flickers from a steady one | Srinivasan and Lehrer 1984 (moving stimuli; flickering stimuli); Inger et al. 2014 (60 Hz for people) |
| row `i` Ultraviolet, "Bees can see ultraviolet light, which people can't. Phone cameras capture very little of it, so the blue in this view stands in for it." | confirmed; `docs/COVERAGE.md` noted that the Sussex page cited for "an ordinary camera cannot record ultraviolet" does not say so, and Igoe et al. 2012 now back "very little" with figures | the phone's optics pass 18.9% at 390 nm and 1.1% at 340 nm; whole-camera response a few thousandths of a percent |
| row `i` How the colours are shown | confirmed as the researchers' convention; it can say so | Lunau et al. 2025 |

**Deeper evidence, by subject.**

- *Receptor peaks.* Honeybee workers 344, 436 and 544 nm (Hempel de Ibarra et al. 2014, from Menzel and Backhaus 1991), given as 346, 430, 540 (van der Kooi et al. 2021) and 344, 436, 556 (Land and Nilsson 2012, from Kelber 2006); drones 346, 445, 529. Bumblebees: *B. impatiens* 346 to 348, 424, 539 to 541; *B. terrestris* subspecies 336 to 348, 428 to 436, 529 to 538. Wasps: *Vespula germanica* 347, 445, 534; *V. vulgaris* 346, 445, 531; *Vespa crabro* 346, 445, 529; *Polistes dominula* 358, 457, 527; *Philanthus triangulum* 352, 445, 529. In Apidae the peaks vary little across 27 species (van der Kooi et al. 2021). Sawflies and horntails: *Sirex noctilio* 364 and 527 with no blue gene (Guignard et al. 2021); *Tenthredo campestris* 337, 458, 537, 602. Every ommatidium in a bee holds six green receptors and two that are blue, ultraviolet or one of each (van der Kooi et al. 2021; Skorupski and Chittka 2011).
- *Ultraviolet on flowers.* Most flowers absorb ultraviolet; ultraviolet patterns are fewer but strongly tied to bee pollination; the commonest pattern is an absorbing centre in a reflecting flower; pure ultraviolet-reflecting flowers are nearly absent (Lunau et al. 2025; Kevan et al. 2001). Red bee flowers usually reflect ultraviolet, red bird flowers usually do not.
- *Flicker and timing.* 200 Hz at 3000 lux and 144 Hz at 300 lux for moving patterns (Srinivasan and Lehrer 1984; Inger et al. 2014). Bees tell colour flicker from steady light well, brightness flicker poorly, and flicker involving blue best (Srinivasan and Lehrer 1984, flickering stimuli). Receptor integration times: *B. terrestris* green 7.9 ms, blue 9.8, ultraviolet 12.3; *B. impatiens* 11.3, 18.6 and 15.6 (Skorupski and Chittka 2010, 2011); receptors slow as light falls (Reber et al. 2015). Wolf 1933 found the flicker limit rises with light.
- *Acuity across the eye.* Recorded at the retina by pattern electroretinogram, honeybees resolve 0.54 cycles per degree and two Australian stingless bees with 45% fewer facets 0.53; their contrast sensitivity differs (honeybee 16.9, a 6% threshold; *Tetragonula carbonaria* 6.0, a 17% threshold; Ryan et al. 2020 via Penmetcha et al. 2025). Light-adapted acceptance angles 1.9 degrees frontally, 1.6 just below the front, widening outward (Rigosi et al. 2017); single receptors register a 0.6 degree dark square, while trained bees fail below 3 to 5 degrees. Honeybee interommatidial angles 0.9 vertical and 1.6 to 2.1 horizontal frontally (Baumgärtner 1928 via Kelber and Somanathan 2019; Rigosi et al. 2017), the eye sampling finer vertically than horizontally (Hecht and Wolf 1929; Taylor et al. 2019), though Srinivasan and Lehrer 1988 found no difference between horizontal and vertical gratings (Land 1997). Drones have a dorsal acute zone of 1 to 2 degree angles and pursue targets of 0.41 degrees (Rigosi et al. 2017; Somanathan et al. 2017) or 0.32 (Land 1997), all citing Vallet and Coles 1991. Male carpenter bees (*Xylocopa tenuiscapa*) have an upward acute zone of 0.7 degree angles and chase thrown stones as small as 0.19 degrees; females sample at 1 degree forward and slightly down (Somanathan et al. 2017). Bumblebees average 1.5 degrees across the middle of the eye, finest about 60 degrees to the side, and larger workers see more finely and with more overlap between the eyes (Taylor et al. 2019); a third more body size doubles single-target precision (Spaethe and Chittka 2003).
- *Ocelli.* Three, with honeybee receptors at 360 and 500 nm (Kelber and Somanathan 2019) and bumblebee receptors at 350 and 485 nm (Araújo et al. 2024); they focus about 100 µm behind their retinas, so their images are blurred (Hung and Ibbotson 2014); their upper retinas see the horizon and the lower ones the sky; bees with ocelli covered start and stop foraging at five times brighter light (Kelber and Somanathan 2019). Sand wasps of the tribe Bembicini have only vestigial ocelli (Trisoglio et al. 2026). Hornet ocelli are 336 to 359 µm across, common wasps' about 210 (Kelber et al. 2011).
- *Polarization.* The dorsal rim of the honeybee eye holds at least 60 specialized ommatidia (Schinz 1975) whose ultraviolet receptors have wide, coupled receptive fields of about 7 degrees (Kolyfetis et al. 2025). Bumblebee ocelli are polarization sensitive and carry the compass in dim light (Araújo et al. 2024); bumblebees can learn polarization patterns on artificial flowers seen from below (Foster et al. 2014).
- *Magnetic sense.* Trained honeybees detect a 260 nT change, 0.6% of the background (Walker and Bitterman 1989); sensitivity falls with frequency, needing over 100 µT at 60 Hz (Kirschvink et al. 1997, whose abstract also cites a static threshold of 26 nT, a factor of ten apart); stingless bees change departure angles near magnets up to about 80 µT (Vale and Acosta-Avalos 2020); bumblebees walking in darkness keep direction without odour trails (Chittka et al. 1999); the mechanism is unresolved (Oesterle et al. 2026).
- *Electric fields.* Bumblebees detect floral fields and learn colours faster with them (Clarke et al. 2013); their body hairs deflect at 0.77 to 61 V/m, antennae at 15.3 to 306 V/m (Sutton et al. 2016 via Clarke et al. 2017); honeybees sense the fields of other bees with the antennae's Johnston organ (Greggers et al. 2013); bees carry +30 to +50 pC (Clarke et al. 2017), more in warm, dry weather (Montgomery et al. 2019); field detection has been shown only within 10 cm; power-line-like fields cut honeybee landings by 71% (AC) and 53% (positive DC) (Mallinson et al. 2025). Wasps carry charge that caterpillars detect (England and Robert 2024); whether wasps sense fields is untested.
- *Motion in flight.* Bees centre between walls by balancing image speed on the two eyes, set speed by holding image speed constant, and land by holding the ground's image speed constant (Srinivasan et al. 1996; Baird et al. 2005); bumblebees use the largest optic flow in the frontal field, from the nearest obstacle (Linander et al. 2015); distance flown is measured from green-receptor contrast only (Kelber and Somanathan 2019); bees cruise at 4 to 8 m/s (Egelhaaf and Lindemann 2025); stripes of intermediate width break landings, up to 80% failures, through aliasing in the eye's mosaic (Hsieh and Yang 2026). Bumblebee head saccades typically last 45 to 135 ms and reach 1500 degrees per second (Boeddeker et al. 2015).

## 4. Species with their own measurements

| Species | Records (Alachua; world) | Measured | What a profile would change |
|---|---|---|---|
| *Apis mellifera*, Western Honey Bee | 469; 548,372 | receptors, acuity behavioural and retinal, field of view, flicker at two light levels, ocelli, dorsal rim, electric, magnetic, hearing | the `bee` view as written is a honeybee profile |
| *Bombus impatiens*, Common Eastern Bumble Bee | 256; 239,293 | receptors 348, 424, 539 nm; integration times; acuity 0.35-0.36 and 0.14 in flight control; darkness walking | sharpness 0.35; slower pace than the honeybee if the integration times are taken as a guide (an inference) |
| *Bombus terrestris* (Europe) | 0; common in Europe | receptors; acuity 0.21-0.25; size scaling; electric hairs; saccades; polarization in ocelli; receptor speed with light | sharpness by worker size |
| *Bombus pensylvanicus*, American Bumble Bee | 311; 51,111 | nothing direct | takes *B. impatiens* (`g`) |
| *Vespula germanica* and *V. vulgaris* | 0 (Alachua has *V. squamosa* 136 and *V. maculifrons* 48); 32,361 and 16,653 | acute zone, split eye, acceptance angles, receptors | the `wasp` view as written is a *Vespula* profile |
| *Vespa crabro*, European Hornet | 0; common in Europe and introduced in North America | acute zone 1 degree, dusk flight, ocelli, receptors | the hornet dusk setting |
| *Polistes dominula* and *P. fuscatus* | 0; 60,895 and 40,248 | receptors (*P. dominula*); face recognition (*P. fuscatus*); about 1 degree sampling | Alachua's *Polistes metricus*, *P. exclamans*, *P. major*, *P. dorsalis* and *P. annularis* take these (`g`) |
| *Xylocopa* carpenter bees | 211 (*X. virginica* 137, *X. micans* 74); 101,040 for *X. virginica* | Indian congeners: *X. tenuiscapa* females sample at 1 degree forward (Somanathan et al. 2017), and Table 1 of Kelber and Somanathan 2019 gives 0.8 by 1.5 degrees for *X. tenuiscapa* and 0.7 by 1.0 for *X. tranquebarica* (vertical by horizontal); receptors of the Brazilian *X. brasilianorum* (362, 445, 538 nm) | sharpness about 0.5 for *X. virginica* by inference (`g`) |
| *Tetragonula carbonaria* and *Austroplebeia australis*, Australian stingless bees | 0; 754 and 19 | retina resolves 0.53 cycles per degree, as the honeybee's does; contrast sensitivity 6.0 and 13.1 against the honeybee's 16.9; *T. carbonaria* single-target detection 0.053 | a contrast floor near 17% for *T. carbonaria*; the stingless bees most recorded in the world (*Tetragonisca angustula* 3,973, *Trigona spinipes* 3,199) are unmeasured here |
| *Philanthus triangulum*, bee-wolf | 0; 8,081 | receptors | |
| *Sirex noctilio* and *Tenthredo campestris* | 0 | receptors | the sawfly two-colour setting |

## 5. Gaps and how to fill them

- **Wasp timing.** No flicker or receptor speed was found for any vespid. Nearest: honeybee 200 Hz, bumblebee green receptors 7.9 to 11.3 ms. Inference: similar-sized day fliers with the same receptor types are likely as fast; `rate` 0.3, graded `i`.
- **Wasp field of view and polarization.** Unmapped beyond about 100 degrees of longitude (Gutiérrez et al. 2024). Take the honeybee's 312 degrees (`g`); Zeil et al. 2014 is wanted for the dorsal rim.
- **Small bees.** No acuity for the sweat bees that dominate Alachua's small-bee records (*Halictus poeyi*, *Agapostemon splendens*). The nearest evidence pulls two ways. In behaviour, the small stingless bee *Tetragonula carbonaria* detects targets at 18.8 degrees per cycle against the honeybee's 6 to 11 in the same kind of test (Kelber and Somanathan 2019, Table 3), and eye size and resolution scale with body size across Apidae (same review). At the retina, the same stingless bee resolves 0.53 cycles per degree against the honeybee's 0.54 by an identical method, while needing about three times the contrast (Penmetcha et al. 2025). One reading, which is this sheet's inference and not the authors' claim, reconciles the two: a bee that needs more contrast spots a small target later even when its eye resolves as finely. The authors add that bees in outdoor tests detect thin strands of spider silk at the distance where the behavioural figure says a 1 cm flower first appears, so the behavioural tests may understate small bees. Inference: keep `cpd` 0.3 for small bees and give them a stronger contrast floor (effect 8), pending Jander and Jander 2002 (wanted, priority 1). An earlier draft of this sheet halved `cpd` for small bees; the retinal result is the reason for the change.
- **Carpenter bees.** Florida's two species are unmeasured; the Indian *X. tenuiscapa* samples at 1 degree forward in females (Somanathan et al. 2017) and 0.8 by 1.5 degrees in Table 1 of Kelber and Somanathan 2019, so about 0.5 cycles per degree (`g`).
- **Velvet ants.** *Dasymutilla* vision is unmeasured; in the Palearctic *Myrmilla capitata*, wingless females have fewer ommatidia per area than males and apparently no ocelli (Borsotti et al. 2025, abstract). Inference: a walking female sees more coarsely than a flying wasp; nothing more is known.
- **Gall interiors.** Nothing found on light inside galls or on the grub's senses. The `gall` view's light-only picture is invention.
- **Sawfly larvae.** Many sawfly records may be larvae, which have simple larval eyes; no source on them was found. Nothing is known here.
- **Parasitoid wasps.** Apart from *Trichogramma* anatomy and one cynipoid's three receptor classes, nothing was logged; ichneumonids differ from other Apocrita in their opsin genes (Guignard et al. 2021) in ways not described there.
- **Electric and magnetic senses in wasps.** Untested in anything logged.
- **Disagreements between sources.** The honeybee's static magnetic threshold is 260 nT in Walker and Bitterman 1989 and 26 nT in the abstract of Kirschvink et al. 1997; the drone's pursuit threshold is 0.41 degrees in two papers and 0.32 in Land 1997. Reading Vallet and Coles 1991 and the Kirschvink paper would settle both.

## 6. Closed sources wanted

The same fifteen works as `docs/views/wanted/bee.jsonl`, most useful first:

1. Jander and Jander 2002, *Allometry and resolution of bee eyes (Apoidea)*, Arthropod Structure & Development, doi 10.1016/s1467-8039(01)00035-4: sharpness from body size, for species settings.
2. Peitsch et al. 1992, *The spectral input systems of hymenopteran insects and their receptor-based colour vision*, J Comp Physiol A 170:23-40, doi 10.1007/bf00190398: receptor peaks for 43 species including sawflies.
3. Giurfa and Vorobyev 1998, *The angular range of achromatic target detection by honey bees*, J Comp Physiol A, doi 10.1007/s003590050238: the 5 to 15 degree window.
4. Srinivasan and Lehrer 1985, *Temporal resolution of colour vision in the honeybee*, J Comp Physiol A, doi 10.1007/bf01351352: the timing of the colour wash.
5. Ryan, Cunningham, Hart and Ogawa 2020, *The buzz around spatial resolving power and contrast sensitivity in the honeybee, Apis mellifera*, Vision Research, doi 10.1016/j.visres.2020.02.005: the full contrast-sensitivity curve for the contrast floor, and the reasons retinal and behavioural acuity differ.
6. Srinivasan and Lehrer 1988, *Spatial acuity of honeybee vision and its spectral properties*, J Comp Physiol A 162:159-172, doi 10.1007/bf00606081.
7. Srinivasan and Lehrer 1984, *Temporal acuity of honeybee vision: behavioural studies using moving stimuli*, J Comp Physiol A 155:297-312, doi 10.1007/bf00610583.
8. Seidl and Kaiser 1981, *Visual field size, binocular domain and the ommatidial array of the compound eyes in worker honey bees*, J Comp Physiol A 143:17-26, doi 10.1007/bf00606065.
9. Menzel 1981, *Achromatic vision in the honeybee at low light intensities*, J Comp Physiol A, doi 10.1007/bf00609941.
10. Warrant, Kelber, Wallén and Wcislo 2006, *Ocellar optics in nocturnal and diurnal bees and wasps*, Arthropod Structure & Development, doi 10.1016/j.asd.2006.08.012.
11. Zeil, Ribi and Narendra 2014, *Polarisation vision in ants, bees and wasps*, Springer, doi 10.1007/978-3-642-54718-8_3.
12. Jernigan et al. 2022, *Color is necessary for face discrimination in the Northern paper wasp, Polistes fuscatus*, Animal Cognition, doi 10.1007/s10071-022-01691-9 (open on PMC, which refused this session with a rate limit).
13. Sheehan, Jinn and Tibbetts 2014, *Coevolution of visual signals and eye morphology in Polistes paper wasps*, Biology Letters, doi 10.1098/rsbl.2014.0254.
14. Wehner 1972, *Dorsoventral asymmetry in the visual field of the bee, Apis mellifica*, J Comp Physiol, doi 10.1007/bf00696429.
15. Vallet and Coles 1991, *A method of estimating the minimum visual stimulus that evokes a behavioural response in the drone, Apis mellifera male*, Vision Research 31:1453-1455 (no DOI seen).

## 7. Sources

Opened in this session (full text, abstract, or the stated pages):

- Araújo P, Belušič G, Ilić M, Foster JJ, Pfeiffer K, Baird E 2024. Polarized light detection in bumblebees varies with light intensity and is mediated by both the ocelli and compound eyes. Biology Letters. doi 10.1098/rsbl.2024.0299. opened
- Baird E, Srinivasan MV, Zhang S, Cowling A 2005. Visual control of flight speed in honeybees. J Exp Biol. doi 10.1242/jeb.01818. opened (abstract)
- Boeddeker N, Mertes M, Dittmar L, Egelhaaf M 2015. Bumblebee homing: the fine structure of head turning movements. PLoS ONE. doi 10.1371/journal.pone.0135020. opened
- Borsotti A et al. 2025. Sexual dimorphism in the sensory system of Myrmilla capitata. Arthropod Struct Dev. doi 10.1016/j.asd.2025.101479. opened (abstract)
- Brown PE, Frank CP, Groves HL, Anderson M 1998. Spectral sensitivity and visual conditioning in the parasitoid wasp Trybliographa rapae. Bull Entomol Res. doi 10.1017/s0007485300025864. opened (abstract)
- Caves EM, Brandley NC, Johnsen S 2018. Visual acuity and the evolution of signals. Trends Ecol Evol 33:358-372. doi 10.1016/j.tree.2018.03.001. opened (owner's library)
- Chakravarthi A 2017. Spatial vision in bees (doctoral thesis, Lund University). opened (abstract)
- Chittka L, Waser NM 1997. Why red flowers are not invisible to bees. Israel J Plant Sci. doi 10.1080/07929978.1997.10676682. opened (abstract)
- Chittka L, Williams NM, Rasmussen H, Thomson JD 1999. Navigation without vision: bumblebee orientation in complete darkness. Proc R Soc B. doi 10.1098/rspb.1999.0602. opened (abstract)
- Clarke D, Whitney H, Sutton G, Robert D 2013. Detection and learning of floral electric fields by bumblebees. Science. doi 10.1126/science.1230883. opened (abstract)
- Clarke D, Morley E, Robert D 2017. The bee, the flower, and the electric field. J Comp Physiol A. doi 10.1007/s00359-017-1176-6. opened
- DLR Insect Vision, Bee photoreceptor response model and Bee eye model (web pages). opened
- Egelhaaf M, Lindemann JP 2025. Path integration and optic flow in flying insects. J Comp Physiol A. doi 10.1007/s00359-025-01734-9. opened
- England SJ, Robert D 2024. Prey can detect predators via electroreception in air. PNAS. doi 10.1073/pnas.2322674121. opened
- Fischer S, Müller CHG, Meyer-Rochow VB 2010. How small can small be: the compound eye of the parasitoid wasp Trichogramma evanescens. Visual Neuroscience. doi 10.1017/s0952523810000192. opened (abstract)
- Foster JJ et al. 2014. Bumblebees learn polarization patterns. Current Biology. doi 10.1016/j.cub.2014.05.007. opened
- Giurfa M, Vorobyev M, Kevan P, Menzel R 1996. Detection of coloured stimuli by honeybees. J Comp Physiol A 178:699-709. doi 10.1007/BF00227381. opened (abstract)
- Greggers U et al. 2013. Reception and learning of electric fields in bees. Proc R Soc B. doi 10.1098/rspb.2013.0528. opened (abstract)
- Greiner B 2006. Visual adaptations in the night-active wasp Apoica pallens. J Comp Neurol. doi 10.1002/cne.20882. opened (abstract)
- Guignard Q et al. 2021. Evidence for UV-green dichromacy in the basal hymenopteran Sirex noctilio. Sci Rep. doi 10.1038/s41598-021-95107-2. opened
- Gutiérrez D, Rigosi E, Nagloo N, O'Carroll DC, Warrant EJ 2024. Spatial resolution and optical sensitivity in the compound eyes of two common European wasps. J Exp Biol. doi 10.1242/jeb.246670. opened
- Hecht S, Wolf E 1929. The visual acuity of the honey bee. J Gen Physiol. doi 10.1085/jgp.12.6.727. opened (abstract)
- Hempel de Ibarra N, Vorobyev M, Menzel R 2014. Mechanisms, functions and ecology of colour vision in the honeybee. J Comp Physiol A. doi 10.1007/s00359-014-0915-1. opened
- Hsieh H-W, Yang E-C 2026. Fine stripe patterns disrupt honey bee landings via spatial aliasing. J Comp Physiol A. doi 10.1007/s00359-026-01842-0. opened
- Hung Y-S, Ibbotson MR 2014. Ocellar structure and neural innervation in the honeybee. Front Neuroanat. doi 10.3389/fnana.2014.00006. opened
- Igoe D, Parisi A, Carter B 2012. Characterization of a smartphone camera's response to ultraviolet A radiation. Photochem Photobiol. doi 10.1111/j.1751-1097.2012.01216.x. opened (author's manuscript)
- Inger R, Bennie J, Davies TW, Gaston KJ 2014. Potential biological and ecological effects of flickering artificial light. PLoS ONE. doi 10.1371/journal.pone.0098631. opened
- Kelber A, Somanathan H 2019. Spatial vision and visually guided behavior in Apidae. Insects 10:418. doi 10.3390/insects10120418. opened
- Kelber A, Jonsson F, Wallén R, Warrant EJ, Kornfeldt T, Baird E 2011. Hornets can fly at night without obvious adaptations of eyes and ocelli. PLoS ONE. doi 10.1371/journal.pone.0021892. opened
- Kelber A et al. 2005. Light intensity limits foraging activity in nocturnal and crepuscular bees. Behav Ecol. doi 10.1093/beheco/arj001. opened (abstract)
- Kevan PG, Chittka L, Dyer AG 2001. Limits to the salience of ultraviolet. J Exp Biol. doi 10.1242/jeb.204.14.2571. opened (abstract)
- Kirchner WH 1993. Acoustical communication in honeybees. Apidologie 24(3). opened
- Kirschvink JL, Padmanabha S, Boyce CK, Oglesby J 1997. Measurement of the threshold sensitivity of honeybees to weak, extremely low-frequency magnetic fields. J Exp Biol 200:1363-1368. opened (abstract)
- Kolyfetis GE, Belušič G, Foster JJ 2025. Electrophysiological recordings reveal photoreceptor coupling in the dorsal rim areas of honeybee and bumblebee eyes. Biology Letters. doi 10.1098/rsbl.2025.0234. opened
- Land MF 1997. Visual acuity in insects. Annu Rev Entomol 42:147-177. doi 10.1146/annurev.ento.42.1.147. opened (owner's library)
- Land MF, Nilsson D-E 2012. Animal Eyes, 2nd edition. Oxford University Press. ISBN 978-0-19-958113-9. opened in part (Chapters 1 and 2, Chapter 3 to about p. 63)
- Linander N, Dacke M, Baird E 2015. Bumblebees measure optic flow for position and speed control flexibly within the frontal visual field. J Exp Biol. doi 10.1242/jeb.107409. opened (abstract)
- Lunau K, Gutierrez Camargo MG, Ren Z-X 2025. Bees, flowers and UV. Plant Biology. doi 10.1111/plb.70050. opened
- Mallinson VJ, Woodburn FA, O'Reilly LJ 2025. Weak anthropogenic electric fields affect honeybee foraging. iScience. doi 10.1016/j.isci.2025.112550. opened (abstract)
- Montgomery C, Koh KL, Robert D 2019. Measurement of electric charges on foraging bumblebees. J Phys Conf Ser. doi 10.1088/1742-6596/1322/1/012002. opened (abstract)
- Oesterle A, Kiriş A, Haase A 2026. Experimental platform to study the neuronal mechanisms of magnetoreception in the honey bee. Methods. doi 10.1016/j.ymeth.2026.09.005. opened (abstract)
- Penmetcha B, Ryan LA, Ogawa Y, Hart NS, Narendra A 2025. Visual physiology of Australian stingless bees. J Comp Physiol A. doi 10.1007/s00359-025-01740-x. opened
- Reber T et al. 2015. Effect of light intensity on flight control and temporal properties of photoreceptors in bumblebees. J Exp Biol. doi 10.1242/jeb.113886. opened (abstract)
- Rigosi E, Wiederman SD, O'Carroll DC 2017. Visual acuity of the honey bee retina and the limits for feature detection. Sci Rep. doi 10.1038/srep45972. opened
- Schinz RH 1975. Structural specialization in the dorsal retina of the bee, Apis mellifera. Cell Tissue Res 162:23-34. doi 10.1007/BF00223259. opened (abstract)
- Shafir S 1996. Color discrimination conditioning of a wasp, Polybia occidentalis. Biotropica. doi 10.2307/2389078. opened (abstract)
- Sheehan MJ, Jinn J, Tibbetts EA 2014. Coevolution of visual signals and eye morphology in Polistes paper wasps. Biology Letters. doi 10.1098/rsbl.2014.0254. opened (abstract)
- Shorthouse JD, Leggo JJ 2002. Immature stages of the galler Diplolepis triforma. Can Entomol. doi 10.4039/ent134433-4. opened (abstract)
- Skorupski P, Chittka L 2010. Differences in photoreceptor processing speed for chromatic and achromatic vision in the bumblebee, Bombus terrestris. J Neurosci. doi 10.1523/jneurosci.5700-09.2010. opened (abstract)
- Skorupski P, Chittka L 2011. Photoreceptor processing speed and input resistance changes during light adaptation correlate with spectral class in the bumblebee, Bombus impatiens. PLoS ONE. doi 10.1371/journal.pone.0025989. opened
- Somanathan H, Borges RM, Warrant EJ, Kelber A 2017. Visual adaptations for mate detection in the male carpenter bee Xylocopa tenuiscapa. PLoS ONE. doi 10.1371/journal.pone.0168452. opened
- Spaethe J, Chittka L 2003. Interindividual variation of eye optics and single object resolution in bumblebees. J Exp Biol. doi 10.1242/jeb.00570. opened (abstract)
- Srinivasan MV, Lehrer M 1984. Temporal acuity of honeybee vision: behavioural studies using moving stimuli. J Comp Physiol A 155:297-312. doi 10.1007/bf00610583. opened (abstract, publisher page)
- Srinivasan MV, Lehrer M 1984. Temporal acuity of honeybee vision: behavioural studies using flickering stimuli. Physiol Entomol. doi 10.1111/j.1365-3032.1984.tb00787.x. opened (abstract)
- Srinivasan MV, Zhang SW, Lehrer M, Collett TS 1996. Honeybee navigation en route to the goal. J Exp Biol 199:237. doi 10.1242/jeb.199.1.237. opened (abstract)
- Sutton GP, Clarke D, Morley EL, Robert D 2016. Mechanosensory hairs in bumblebees detect weak electric fields. PNAS. doi 10.1073/pnas.1601624113. opened (abstract)
- Taylor GJ et al. 2019. Bumblebee visual allometry results in locally improved resolution and globally improved sensitivity. eLife. doi 10.7554/elife.40613. opened
- Tibbetts EA 2002. Visual signals of individual identity in the wasp Polistes fuscatus. Proc R Soc B. doi 10.1098/rspb.2002.2031. opened (abstract)
- Trisoglio CF, Ferrari A, Brilli M, Zilioli M, Polidori C 2026. Evolution of peripheral visual system in the Apoidea. Ecol Evol. doi 10.1002/ece3.73608. opened
- Vale JO, Acosta-Avalos D 2020. Magnetosensitivity in the stingless bee Tetragonisca angustula. Bioelectromagnetics. doi 10.1002/bem.22312. opened (abstract)
- van der Kooi CJ, Stavenga DG, Arikawa K, Belušič G, Kelber A 2021. Evolution of insect color vision. Annu Rev Entomol 66:435-461. doi 10.1146/annurev-ento-061720-071644. opened (owner's library; the article is CC BY)
- VanderSal ND, Crews SC, Gillespie RG 2016. Is love in the air or at first sight? Mate finding cues used by sympatric male velvet ants. Invertebr Biol. doi 10.1111/ivb.12128. opened (abstract)
- Walker MM, Bitterman ME 1989. Honeybees can be trained to respond to very small changes in geomagnetic field intensity. J Exp Biol 145:489-494. opened
- Warrant EJ 2008. Seeing in the dark: vision and visual behaviour in nocturnal bees and wasps. J Exp Biol. doi 10.1242/jeb.015396. opened (abstract)
- Wolf E 1933. Critical frequency of flicker as a function of intensity of illumination for the eye of the bee. J Gen Physiol. doi 10.1085/jgp.17.1.7. opened (abstract)

Secondary (values taken through the source named):

- Baumgärtner 1928, honeybee facet angles: secondary, through Kelber and Somanathan 2019.
- Greiner et al. 2004 and Greiner 2006, honeybee and *Polistes occidentalis* optical sensitivity: secondary, through Gutiérrez et al. 2024.
- Heran 1956, Wenner 1963, Osborne et al., bee cruising speeds: secondary, through Egelhaaf and Lindemann 2025.
- Hertel 1980, Kien and Menzel 1977, colour neurons' receptive fields; Giurfa and Vorobyev 1998, the 5 to 15 degree window; Menzel and Backhaus 1991, receptor peaks: secondary, through Hempel de Ibarra et al. 2014.
- Kirschfeld 1973 and Seidl 1982, honeybee interommatidial angles; Seidl and Kaiser 1981, the field of view: secondary, through Taylor et al. 2019.
- Peitsch et al. 1992 and the per-species sources of Table 1: secondary, through van der Kooi et al. 2021.
- Ryan et al. 2020, honeybee resolving power and contrast sensitivity by pattern electroretinogram; Dyer et al. 2016, anatomical acuity of *Tetragonula carbonaria*; Sathyakumar 2021, silk detection: secondary, through Penmetcha et al. 2025.
- Srinivasan and Lehrer 1988, 0.26 cycles per degree; Vallet and Coles 1991, drone threshold; Horridge 1978 and Mazokhin-Porshnyakov 1969, interommatidial angles: secondary, through Land 1997.
- Sutton et al. 2016, hair and antenna thresholds: secondary, through Clarke et al. 2017 (the abstract was also opened).
- Verhoeven et al. 2018, the false-colour convention; Lunau et al. 2011, red flowers: secondary, through Lunau et al. 2025.

## 8. Questions for a specialist

1. Should a bee view's blur follow behavioural grating acuity (0.26 cycles per degree; Srinivasan and Lehrer 1988) or the retina's limit by pattern electroretinogram (0.54; Ryan et al. 2020), and what accounts for the factor of two between them?
2. Do vespids notice a seam where the notch divides each eye, and do sphecid and crabronid wasps share the notch and the step in sampling?
3. What share of iNaturalist's gall wasp records show galls, and has anyone measured light inside an oak gall?
4. Which sawfly and horntail families keep a blue receptor, and what do sawfly larvae see with their larval eyes?
5. Has any vespid wasp's flicker limit or receptor speed been measured?
6. Is it fair, as a drawing, to blur a bee's colour about three times more than its brightness detail to stand for the 5 and 15 degree detection limits?
