# Round 2 sheet: the insects and bees people meet (`insects-met`), draft

Unit `insects-met`, branch `research/insects-met`, 13 October 2026. Views: `insect` (all insects except Hymenoptera other than ants, springtails included) and `bee` (Hymenoptera other than ants: bees, wasps, sawflies, parasitoids). Round-1 logs read first: `research/insect` (523 lines) and `research/bee` (267). This unit adds 52 lines to `docs/views/evidence/insects-met.jsonl`. Row wording is a first pass in the second person, to be rewritten in the owner's single pass.

No gap table existed on `main` or `agent/gaps` when this unit started. Species counts below are the ones the round-1 sheets recorded (Alachua figures) and the world order counts in `docs/views/world-orders.csv`. The open web was closed, so species-level iNaturalist counts for the world are not available here; "records" on the wanted list is filled only where a family count is known.

## 1. Scope and the six places the lending breaks

`kind_of_eye` sends every insect that is not a Hymenoptera, and every ant, to `insect` (37.4 million world records), and every other Hymenoptera to `bee` (4.56 million). Round 1 proposed eight insect views and three Hymenoptera views. Until those exist, the rows below must hold for whatever species lands on the two views. The species-level reading finds these breaks, most records first:

1. **Skippers (Hesperiidae) under the butterfly picture.** 1,120,084 world records, 12.8 percent of Papilionoidea. Skippers have optical superposition eyes (Horridge, Giddings and Stange 1972, logged in round 1; Ocybadistes walkeri in Land 1997 Table 1), where every other butterfly measured has apposition eyes. Any sentence about butterfly eyes is false for them. New in this unit: a skipper's startle jump to a camera flash completes inside 17 ms (Sourakov 2009, Florida Entomologist, one author photographing in Florida), which fits a fast, sensitive eye but is a camera timing, not a latency.
2. **Red in nymphalids is not one answer.** The Monarch and the heliconians have a red-opponent channel (Belušič et al. 2021, Table 1: Danaus plexippus 610 nm; Heliconius erato 620; Argynnis paphia 620; Speyeria aglaja 620). The Red Admiral does not, and fails to tell red hues apart (Belušič 2021 Table 1; Zaccardi et al. 2006). The Common Buckeye has one long-wavelength pigment at 510 nm (Briscoe and Bernard 2005). A row that says "butterflies see red" or "butterflies cannot see red" is false for some of the five most recorded butterflies in Alachua.
3. **Rule 2 cannot carry colour classes across Lepidoptera or across Hymenoptera.** Lepidoptera: Pieris rapae crucivora has six classes, the Monarch three plus an opponent channel, Papilio xuthus eight. Hymenoptera: a measured disagreement exists on both sides of the bee/ant line, Callonychium petuniae (Andrenidae) with a fourth class at 593 nm and the fire ant Solenopsis saevissima with a class at 620 nm (both from van der Kooi et al. 2021 Table 1; logged here as records of their own). Rule 5 therefore blocks the order-level carry for Hymenoptera, and the bee view's Red row can be carried only family by family (proposal 7 in `docs/views/carry.jsonl`).
4. **Skimmers on the dragonfly picture.** The Green Darner (Anax junius) is the only Florida odonate with a figure of its own (0.24 degree dorsal band, Land 1997). Eastern Pondhawk, Blue Dasher and Eastern Amberwing have none for acuity. The Amberwing has one behavioural measurement, and Libellula quadrimaculata (a relative) has a measured fovea orientation.
5. **Bumblebees, carpenter bees and sweat bees on the honeybee's rows.** The honeybee has 43 log lines. Bombus impatiens, the Common Eastern Bumble Bee, has its own three pigment peaks, acuity and ommatidial types. Carpenter bees have a measured Brazilian species and an Indian one. Sweat bees have Lasioglossum and a nocturnal relative (Megalopta) whose night-adapted eye must not be carried to the day-flying Agapostemon and Augochlora.
6. **Night-flying moths.** Superposition eyes, no red class in the hawkmoths measured. Manduca sexta (Florida) now has behavioural motion parameters of its own (Parthasarathy and Willis 2018). The Luna Moth and Polyphemus Moth stay on a relative (Antheraea, Actias) at grade g.

## 2. Species and what each row can say

Grades follow carry rule 6. "m" means this species, "g" a named relative by a rule or by a proposed exception, "i" a guess. Log lines are named by source because the evidence file has no stable line numbers across the three logs (`insect`, `bee`, `insects-met`).

### 2.1 View `insect`: butterflies

**Monarch, Danaus plexippus** (Alachua 714; one of the five most photographed butterflies)

- `m` Colour: "You have three kinds of colour-sensing cell, tuned to ultraviolet, blue and green light, and a fourth channel that compares green with red light, with its red side peaking near 610 nanometres. A dark orange filtering pigment in your eye sharpens your reading of long wavelengths, so you can tell orange from red and from yellow." Behind it: van der Kooi 2021 Table 1 (peaks 340, 435, 540 nm, round 1); Belušič 2021 Table 1 (610 nm opponent cell); Blackiston, Briscoe and Weiss 2011 (true colour vision, filter pigment trials; abstract). The view draws this as a colour shift with a deeper orange response; red is not in the camera's reach as a separate channel, so the picture shows the effect as separation of oranges.
- `m` Sharpness: "Each of your colour-sensing cells collects light from a patch of sky about two degrees wide, so fine detail is blurred before the image leaves the eye. In flight your head swings to cancel the wobble of your body, which keeps the patch to about five degrees at take-off." Behind it: Supple et al. 2026 preprint, open (quiescent acceptance angle 2.17 degrees; 5.28 degrees with head compensation; 9.38 degrees without). No monarch interommatidial angle is logged.
- `i` Speed: no monarch flicker value exists in any source opened. Papilio xuthus values (82 to 107 Hz by receptor class, Nakagawa and Eguchi 1994) are another family and cannot travel under rule 1. The honest row says what the view does: it runs slow and jumps ahead.
- `x` Compass: you steer by the sun with a time-compensated compass fed by a dorsal rim of polarization-sensitive cells, and sense the angle of Earth's magnetic field (round 1 lines on Danaus plexippus; unchanged).
- Wanted: Chatterjee et al. 2020 for flicker; Blackiston 2011 full text.

**Queen and Soldier, Danaus gilippus and D. eresimus**: Colour `g` by the proposed genus exception (carry.jsonl line 3), naming the Monarch. Parantica sita, a danaine measured by Nagloo, Kinoshita and Arikawa 2020, has three classes (UV, blue, green), with the green class in three subtypes; red-opponent cells were not searched for there. Sharpness and Speed `i`.

**Gulf Fritillary, Dione vanillae, Zebra Longwing, Heliconius charithonia** (Alachua 1,057 and 491; the two most recorded butterflies in the county)

- `g` Colour: "Your close relatives the postman butterfly and the fritillaries have a green-sensing cell that is switched off by red light, which gives them a red channel. Your eyes are expected to do the same, and red heliconian wing patches are probably easier for you to tell apart than for most butterflies." Behind it: Belušič 2021 Table 1 (Heliconius erato 620 nm; Argynnis paphia and Speyeria aglaja 620 nm); Zaccardi et al. 2006 (H. erato discriminates 590, 620 and 640 nm using filter pigments with one long-wavelength opsin). Exception proposed in carry.jsonl line 1, the three genera agreeing and no heliconiine disagreeing. Neither Florida species is measured.
- `i` Sharpness and Speed.

**Red Admiral, Vanessa atalanta; Painted Lady, V. cardui**

- `m` Colour (Red Admiral): "You have colour vision, with a green-sensing cell peaking near 530 nanometres, but no red channel. Red, orange-red and deep red look alike to you." Behind it: Belušič 2021 Table 1 (no G+R- cell found, green 530); Zaccardi 2006 (cannot discriminate 590, 620 and 640 nm; eyes lack filter pigments and reflect a uniform orange).
- `g` Colour (Painted Lady): same row naming the Red Admiral, by the genus exception (carry.jsonl line 2). Vanessa cardui peaks at 360, 470 and 530 nm are already logged from Land and Nilsson 2012.
- `x` Compass: Red Admirals migrate; their compass systems differ from the Monarch's (Pakhomov et al. 2025 preprint, in the collection with text; not yet logged, to be read in the next pass).

**Common Buckeye, Junonia coenia** (Alachua 582)

- `m` Colour (partial): "Your long-wavelength colour-sensing cells peak near 510 nanometres, the shortest peak among the brushfoot butterflies measured; your relatives the mourning cloak, peacock and malachite peak between 522 and 534." Behind it: Briscoe and Bernard 2005 (R510 J. coenia, R534 Nymphalis antiopa, R530 Inachis io, R522 Siproeta stelenes; abstract). The UV and blue peaks of the buckeye are not in the abstract; Heliconius and Siproeta give no number to carry.
- `i` Sharpness and Speed.

**Swallowtails: Eastern Tiger, Giant, Spicebush, Pipevine (Papilio glaucus, P. cresphontes, P. troilus, Battus philenor)**

- `i` Colour: no Florida swallowtail has a measured pigment set in a source opened. Briscoe's 1998 and 2000 papers on six Papilio glaucus opsins are in the collection without abstracts or text; both are priority 1 on the wanted list. The nearest opened relatives are Papilio xuthus (eight classes, round 1) and P. aegeus (red receptor); both are another species and genus-level carry would be at best `g` for another Papilio.
- `i` Sharpness: Bergman and Rutowski 2015 built the first interommatidial map of Battus philenor, but the abstract gives no figure. Wanted, priority 1.

**Cabbage White, Pieris rapae; whites and sulphurs**

- `m` Colour for Pieris rapae crucivora (the Japanese subspecies): six classes including two red (round 1, van der Kooi 2021). Colias eurytheme acuity 0.7 cycles per degree (Caves et al. 2018) and interommatidial angles 0.72 to 1.84 degrees (Merry et al. 2006) cover the Orange Sulphur. Phoebis sennae (Cloudless Sulphur) has Phoebis rurina as a congener (round 1). Row for Pieris rapae in North America `g` (same species, other subspecies; one phrase naming the Japanese animals).

**Skippers, Hesperiidae** (Alachua: Fiery Skipper, Silver-spotted Skipper and others; 1,120,084 world records)

- `g` Eye: "Your eyes are built differently from those of other butterflies. Light from many facets is gathered onto each light-sensing cell, which makes your eye more sensitive in dim light, and each cell takes in light from a wide patch of sky, about six to eight degrees across in the skipper measured." Behind it: Horridge, Giddings and Stange 1972 (acceptance angle 6 to 8 degrees, abstract, round 1). Land 1997 Table 1 gives the interommatidial angle of Ocybadistes walkeri as 2.0 degrees (a skipper from Australia). Carry within the family by exception (carry.jsonl line 4).
- `m` for the family on reaction: "You jump from a camera flash within about a sixtieth of a second." Sourakov 2009 (one author's photographs, grade as anecdotal).
- Wanted: Swihart 1969 (skipper colour vision and superposition eye).

**Blues, coppers and hairstreaks (Lycaenidae)**

- `m` Atala, Eumaeus atala (Florida native): long-wavelength rhodopsin red-shifted to 565 to 570 nm (Liénard et al. 2021, PNAS; text in the collection). Spring Azure: green 520 to 530 nm in Callophrys sheridanii and Celastrina ladon, same sentence. Blues' males: Lycaena heteronea has four pigments (round 1). Gray Hairstreak, Cassius Blue and others are `i`.

### 2.2 View `insect`: moths

- **Hawkmoths: Tobacco Hornworm moth, Manduca sexta (Florida): `m` Speed and Sharpness.** "In bright light your steering follows a pattern with stripes about 17 degrees apart; as the light fades you prefer finer patterns, down to about 3 degrees, and your preferred pace of passing stripes stays near 4.5 per second." (Parthasarathy and Willis 2018: preferred spatial frequency 0.06 to 0.3 cycles per degree, preferred temporal frequency 4.5 Hz, contrast limit 1 to 5 percent.) Arithmetic: wavelength = 1 / frequency, so 1/0.06 is about 17 degrees and 1/0.3 is about 3.3 degrees. This describes the pattern the steering response prefers and gives no acuity limit. Colour in dim light for the elephant hawkmoth (Kelber et al. 2002, wanted) stays a relative at `g` for other Sphingidae by genus only.
- **Corn Earworm moth, Heliothis (Helicoverpa) zea: `m` Speed.** "In the dark your eye can follow a light that flickers about 80 times a second, close to the 60 a person manages in the light." Agee 1971 (averages 78 to 88 Hz by group, dark-adapted, green light). Other noctuids: `i`.
- **Luna Moth, Actias luna; Polyphemus Moth, Antheraea polyphemus (Alachua 437 and others):** Polyphemus has its own receptor peaks (round 1). Luna borrows Actias artemis aliena (round 1) at `g`. Antheraea pernyi flicker 25 to 70 Hz (Miall 1978, round 1) travels only inside Antheraea (rule 3), so it is a `g` row for the Polyphemus only.
- **Underwings, tent caterpillar moths, and photographed caterpillars:** Round 1 flagged that many Alachua moth records are larvae. The stemmata evidence is in round 1; the proposal there stands.

### 2.3 View `insect`: dragonflies and damselflies

- **Common Green Darner, Anax junius: `m` Sharpness.** "A narrow band of your upper eye samples the sky in steps of about a quarter of a degree, finer than anything else that flies." Land 1997 Table 1 (0.24 degree, dorsal band), Anax junius acuity 2 cycles per degree (Caves, Brandley and Johnsen 2018). Eye regions are ordinary for the group.
- **Eastern Amberwing, Perithemis tenera: `m` Behaviour.** "You see an intruder best when it is straight ahead of you, and you pick it out at greater distance against far vegetation than against near leaves, so you sit facing your territory." Switzer and Eason 2000 (abstract; no distances given). Wanted, priority 2.
- **Blue Dasher, Eastern Pondhawk (Pachydiplax longipennis, Erythemis simplicicollis): `g` via proposal 6.** "Your upper eye carries a zone of sharper sight aimed at the sky, as in the dragonflies measured." The relatives named are Sympetrum striolatum (0.4 degree dorsal, 1.8 ventral; Land 1997), Libellula quadrimaculata (dorsal fovea turned away from the sun; Sauseng, Pabst and Kral 2003, text in the collection) and Libellula needhami (round 1). No acuity number travels.
- **Damselflies (Ischnura, Enallagma; Ebony Jewelwing, Calopteryx maculata):** Ischnura heterosticta has UV, blue and green receptors (Huang et al. 2014, text in the collection; round 1 holds the 360, 450 and 525 nm peaks). Calopteryx splendens and Ischnura elegans are in round 1. Whether damselflies share the dragonflies' red classes is open (Bybee et al. 2012, wanted).

### 2.4 View `insect`: flies

- **House fly, Musca domestica: `m`.** Five receptor classes in the colour system, ommatidial angle 2.5 degrees (Land 1997), acuity 0.2 cycles per degree (Caves et al. 2018). The picture is coarse: "You see in steps of about two and a half degrees."
- **Hoverflies, Eristalis tenax (Syrphidae; 44.7 percent of fly records): `m`.** Four colour-class tandems with peaks near 330, 340, 460 and 540 nm (Horridge et al. 1975, as stated by Hannah et al. 2019), and a colour discrimination that changes continuously with colour difference and shows no sharp categories (Hannah et al. 2019, free-flying, Eristalis tenax). The male's eye has finer sampling than the female's (Syritta pipiens 0.6 against 1.5 degrees, Land 1997).
- **Common Lovebug, Plecia nearctica (Alachua 342): `i`.** No vision paper exists in the collection. Bibio marci (a related March fly, Bibionidae) has 1.6 degrees dorsal and 3.7 degrees ventral and UV and green peaks (round 1), which could become a `g` row only through a family-level exception. None is proposed.
- **Mosquitoes (Aedes aegypti and others):** peaks near 345 and 523 nm only (van der Kooi 2021 Table 1, round 1). No acuity.

### 2.5 View `insect`: beetles and true bugs

- **Asian Lady Beetle, Harmonia axyridis (third most recorded species in the world list): `m` Colour (behaviour).** "You are drawn most to light of about 365, 420 and 520 nanometres. Ultraviolet and long-wavelength opsins carry that response in your eye." Qiu et al. 2025 (abstract: phototaxis peaks at 365, 420 and 520 nm; UV2 and LW knockdown remove the wavelength-specific responses; UV1 has no role found). The seven-spot ladybird (Coccinella septempunctata) has peaks at about 360, 420 and 520 and a 2.9 degree ommatidial angle (round 1, Land 1997), but those travel only to Coccinella (rule 3), not to Harmonia.
- **Japanese Beetle, Popillia japonica: `m`.** "You have two kinds of colour-sensing cell, ultraviolet and green, and none that peaks in orange, which some other beetles have." Guignard et al. 2025 (abstract; open access licence; the paper itself waits on the wanted list for the peaks).
- **Fireflies, Photinus pyralis: `m` on green peak 545 nm** and on the flash dialogue; ultraviolet class not detected in the compilation (round 1, van der Kooi 2021 Table 1; Buck 1990 for the flash timing). Photuris versicolor interommatidial angle 1.8 degrees (Land 1997) is another genus.
- **Stink bugs, milkweed bugs, cicadas, lubber grasshoppers:** `i`. The collection holds no vision paper naming Halyomorpha, Oncopeltus, Romalea or any North American cicada. Recorded in the searched file.
- **Praying mantises, Chinese mantis Tenodera sinensis (round 1):** peaks and stereopsis from movement (Nityananda et al. 2018, Rossel 1986). The Carolina Mantis (Stagmomantis carolina) is `g` by family only if the owner extends rule 3.

### 2.6 Ants (under `insect` today)

- **Florida Carpenter Ant, Camponotus floridanus: `g`** from Camponotus blandus (UV 360, green 515, likely dichromatic) and C. consobrinus (ommatidial angle 5.8 degrees in workers), by genus (rule 3 for the angle; the rule 2 order carry is blocked, so the colour row names Camponotus blandus and genus-level carry would need an exception).
- **Red Imported Fire Ant, Solenopsis invicta: `g`** from Solenopsis saevissima, with a red class at 620 nm, the one ant with a measured red receptor. Baker and Ma 2006 (ommatidia counts for S. invicta) is wanted.

## 3. View `bee`: species by species

- **Honeybee, Apis mellifera: `m`.** Round 1 holds 43 lines (peaks 346, 430, 540 nm; acuity, flicker and polarization lines). Unchanged.
- **Common Eastern Bumble Bee, Bombus impatiens: `m` Colour, Sharpness.** "You have three kinds of colour-sensing cell peaking near 346, 424 and 541 nanometres; none of them sees red. Your best resolution is about a third of a cycle per degree, less than a hundredth of a person's best, and you have three kinds of ommatidium that differ in how many ultraviolet cells they carry." Behind it: van der Kooi 2021 Table 1 (round 1); Skorupski and Chittka 2010 (348, 424, 539; round 1); Macuda et al. 2001 abstract (0.35 and 0.36 cycles per degree, horizontal and vertical gratings, 9 cd/m2, contrast 84 percent); Spaethe and Briscoe 2005 (UV-opsin ommatidial types: two, one or no ultraviolet cells). Arithmetic: 0.35/60 is 0.006, which is about 1/170 of a person's 60 cycles per degree.
- **Other bumblebees in Florida (Bombus pensylvanicus, B. bimaculatus, B. griseocollis, B. fraternus): `g`.** Colour: peaks lie in the same ranges across eleven Bombus species (UV 329 to 355, blue 424 to 450, green 524 to 542) in van der Kooi 2021 Table 1; proposal 5. Acuity: Bombus terrestris 0.21 to 0.25 cycles per degree (round 1) against B. impatiens 0.35 to 0.36 is a measured spread inside the genus; numbers never travel, so the row names each species. Flicker: B. hortorum 130 Hz (Meyer-Rochow 1981, round 1); a review gives about 110 Hz for bumblebees as a group (Meyer-Rochow 2019, abstract; not species-specific).
- **Eastern Carpenter Bee, Xylocopa virginica; Southern Carpenter Bee, X. micans: `g` for Colour, `i` for Sharpness.** The measured carpenter bees are X. brasilianorum (362, 445, 538 nm, Brazil) and the nocturnal-leaning X. tenuiscapa (India; 0.8 vertical by 1.5 horizontal degrees in the female, males with a frontal acute zone, round 1) and X. tranquebarica. Rule 3 would let Xylocopa eye geometry travel inside the genus, but those two species are larger than X. virginica and eye size follows body size (Jander and Jander 2002, wanted), so the row names them and stays `g`.
- **Sweat bees, Agapostemon and Augochlora (Halictidae): `i` for Sharpness and Speed.** Lasioglossum malachurum has blue and green peaks (442, 528 nm) only. Megalopta genalis (nocturnal) must not be carried: its eye is the opposite of a day-flying sweat bee's, so the carry is blocked by a measured contrast (rule 5). The UV class is measured in no halictid.
- **Leafcutter and mason bees, Megachile and Osmia: `m` for Osmia rufa.** "You have three colour-sensing cells peaking at 348, 436 and 572 nanometres; your green cell sits at longer wavelengths than a honeybee's, though you choose colours the way a honeybee does." Menzel et al. 1988 (abstract). The compilation in van der Kooi 2021 lists 553 nm for the same species; the two sources disagree by 19 nm on the green peak, recorded in the note on the line. Megachile `g` from Osmia and Anthidium manicatum (356, 445, 531) by the family-level carry in proposal 7.
- **Paper wasps, Polistes (Polistes dominula 358, 457, 527 nm; P. fuscatus):** `m` Colour for P. dominula; faces are recognized by colour pattern in P. fuscatus (Tibbetts 2002, 2004; Jernigan et al. 2023 wanted). Eye size and facial signals vary across 19 Polistes (Sheehan et al. 2014, round 1). Polistes exclamans and P. metricus (Alachua) `g` by genus.
- **Yellowjackets and hornets (Vespula, Vespa crabro):** `m` for Vespula germanica and V. vulgaris (peaks 347, 445, 534 and 346, 445, 531), interommatidial angles 1.0 and 1.5 degrees (Gutiérrez et al. 2024, round 1) and for Vespa crabro (night flight down to 0.01 to 0.1 cd/m2, Kelber et al. 2011, round 1).
- **Mud daubers, thread-waisted wasps, Scolia dubia, velvet ants (Mutillidae, Dasymutilla):** `i`. Bembix palmata 0.41 degree (Australia, Land 1997) belongs to the sand wasps and stands for none of these. Velvet-ant females are wingless walkers; the eye of Myrmilla capitata is dimorphic by sex (round 1). Scolia hirta and Dasymutilla coccineohirta papers are in the collection but give no eye numbers (Dasymutilla spatial learning is on the wanted list).
- **Red row for the whole view.** The current row says bees have no cells for red. That holds for the measured Apidae, Megachilidae, Vespidae and Andrena. It does not hold at order level, because of Callonychium petuniae. The row should say "the bees measured", and the species rows name the family.

## 4. Species with their own measurements (new this round)

- Common Buckeye (one pigment, 510 nm), Red Admiral (colour behaviour and eyeshine), Monarch (acceptance angle, red channel), Speckled Wood *Pararge aegeria* (males 1 degree frontally, females 1.5, nearly panoramic field, sharpest region aimed 45 degrees above the horizon, facing away from the sun; Bergman and Smolka 2021, text in the collection), Tobacco Hornworm moth, Corn Earworm moth, Asian Lady Beetle, Japanese Beetle, Eastern Amberwing, Common Eastern Bumble Bee, Red Mason Bee.

## 5. Gaps and how to fill them

- **Most-recorded species with every row `i` or `g` by a distant relative:** Eastern Tiger Swallowtail (Papilio glaucus), Zebra Longwing, Gulf Fritillary, Common Lovebug, Blue Dasher, Eastern Pondhawk, Florida Lubber, Southern Two-striped Walkingstick, North American Wheel Bug, stink bugs, Eastern Carpenter Bee, Agapostemon sweat bees, mud daubers. Zebra Longwing and Gulf Fritillary are the most useful to fix because they are the top two butterflies in the county.
- **No source in the collection:** cicada vision, stink bug vision, phasmid vision (round 1 notes Dixippus morosus 7.5 degrees), lovebug vision.
- **Nearest relatives:** skippers from Ocybadistes (Australia) and the 1972 superposition paper; skimmers from Sympetrum and Libellula; carpenter bees from X. tenuiscapa.

## 6. Closed sources wanted

See `docs/views/wanted/insects-met.jsonl` (26 lines, most useful first). Ones that would change a picture: Briscoe 1998 and 2000 (Papilio glaucus opsins), Bergman and Rutowski 2015 (Battus philenor acuity), Jander and Jander 2002 (bee eye allometry), Peitsch et al. 1992 (receptor peaks across 43 hymenopterans), Chatterjee et al. 2020 (flicker across Lepidoptera), Swihart 1969 and Horridge 1972 (skipper eye), Guignard et al. 2025 (Japanese beetle peaks), the Carleton thesis (open address given).

## 7. Sources opened this round

Opened (full text or abstract in the collection): Zaccardi et al. 2006; Briscoe and Bernard 2005; Belušič et al. 2021 (text); Liénard et al. 2021 (text); Bergman and Smolka 2021 (text); Blackiston et al. 2011 (abstract); Supple et al. 2026 (abstract, open preprint); Nagloo et al. 2020 (abstract); Parthasarathy and Willis 2018 (abstract); Agee 1971 (abstract); Sourakov 2009 (abstract); Menzel et al. 1988 (abstract); Macuda et al. 2001 (abstract); Spaethe and Briscoe 2005 (abstract); Meyer-Rochow 2019 (abstract); Qiu et al. 2025 (abstract); Guignard et al. 2025 (abstract); Switzer and Eason 2000 (abstract); Sauseng, Pabst and Kral 2003 (abstract); Land 1997 and van der Kooi et al. 2021 (owner's Drive, pdftotext, tables).

## 8. Questions for a specialist

1. Do skippers (Hesperiidae) all have superposition eyes, or only the subfamilies measured?
2. Is a red-opponent cell expected in the Gulf Fritillary and Zebra Longwing, and would a specialist accept the carry from Heliconius, Argynnis and Speyeria?
3. Does the Eastern Tiger Swallowtail share the Japanese Yellow Swallowtail's eight classes?
4. Do the Florida skimmers hunt with the same dorsal fovea as Libellula and Sympetrum?
5. Is the honeybee's three-class plan safe for Florida carpenter bees and sweat bees, given the fourth class in Callonychium?
6. Has anyone measured a cicada's or stink bug's eye?
