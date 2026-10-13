# Parameter table: jumping spiders (family Salticidae)

Rewritten 13 October 2026 for the engine's `jumper` view. The evidence log is `docs/views/evidence/jumper.jsonl` (282 lines) and the closed sources wanted are in `docs/views/wanted/jumper.jsonl`. "L45" means line 45 of the log, which holds the source, the page or section, a quotation of at most 40 words, the grade and any arithmetic. Grades: `m` measured in this animal or in typical members of the group, `g` measured in a relative or a wider group, `i` a guess from nearby evidence, `x` a sense the picture leaves out. The word `invented` marks a value that is the app's own choice where the evidence runs out. The longer sheet this replaces (scope, the split decision, twelve rows, effects, species, gaps and sources) is in the branch history at commit 3c91140; the decisions it reached are kept below.

**Decisions carried over.** One view, `jumper`, for the whole family. Two genus settings: *Habronattus* gets a third colour class in a small central patch (L104 to L107), and *Lyssomanes* gets half the sharpness in the gaze strip (L153, L203, L280; the halving is invented). Three eye pairs are drawn (principal, front side, rear side); the posterior median eyes are left out.

**One geometry note.** A phone camera covers about 60 to 70 degrees, which lies inside the front side eyes' field (L5, L100, L116) and inside the reach of the principal eyes' sweeps (L53). The rear side eyes' field (L6, L40) has no camera image, so the view draws it as an invented surround and says so in its first row.

## 1. The parameter table

### 1a. Each eye pair

| Setting | Value | Log lines | Grade | What the evidence leaves open |
|---|---|---|---|---|
| Principal eyes (AME): field of one retina, unmoved | 2 degrees wide by 21 high (an upright strip); the whole eye's field is about 5 degrees, with a central region about 1 degree wide | L38, L39, L4, L259 | m (*Phidippus johnsoni*) | Each retina has a bend of about 30 degrees (L57), and the view draws one straight strip: `invented`. |
| AME: how far the strip moves | Up to 45 to 50 degrees along both axes, and it turns about its own axis 20 to 30 degrees each way. The lenses stay still. | L53, L51, L260, L261 | m, g | None. |
| AME: overlap between the two eyes | None; the two strips form a cross that does not overlap | L57, L58 | m (*Metaphidippus harfordi*) | The view draws one strip because a review cautions against reading the cross as a window (L86). |
| AME: sharpness | 3.8 cycles per degree at the centre (0.13 degree between receptors); 3.3 from the lens alone. The edge of the retina is coarser, 0.65 degree between receptors (0.8 cycles per degree). *Portia* reaches 12.4 and is the outlier. | L84, L35, L130, L72 | m (*Phidippus*), g for the edge | The curve between centre and edge is `invented`. |
| AME: sharpness in *Lyssomanes* | 1.9 cycles per degree | L153, L203, L280, L281 | i | Lyssomanines judge prey and rivals at shorter distances and a review calls their acuity "considerably poorer", but no figure exists: the halving is `invented`. |
| AME: colour classes | Two. An ultraviolet class peaking at 360 to 377 nm and a green class at 520 to 540 nm. The green pigment of *Hasarius adansoni* absorbs at 535 nm in solution. | L21 to L23, L163 to L165, L102, L103, L143, L198, L282 | m (*Phidippus regius*, *Plexippus validus*, *Hasarius*, *Habronattus*, *Saitis*) | Most genera common in Florida are unmeasured (section 2). |
| AME: colour classes in *Habronattus* | Three, in a small patch at the retina's centre: 377, 530 and a red-filtered class near 626 nm (predicted, not recorded) | L104 to L108, L126, L155 | m | The patch size is `invented` (1 by 3 degrees). |
| AME: colour as drawn | The green image goes into two display channels and the ultraviolet class is stood in for by the camera's blue; reds fall to a dark yellow-green | L255, L256, L197 | g | The channel weights are `invented`. Phones record no ultraviolet. |
| Front side eyes (ALE): field of one eye | From about 25 degrees across the midline to 60 degrees out; 70 by 98 degrees in *Phidippus audax*; about 100 degrees in *Menemerus semilimbatus* | L100, L116, L115, L5 | g, m | None. |
| ALE: sharpness | 1.1 cycles per degree in the acute zone (0.46 degree between receptors) and 0.48 at the edge | L114, L36, L193 | m (*Phidippus*) | None. |
| ALE: colour classes | One, green (the surround is drawn in one hue). Opsin labelling found a possible blue class in the secondary eyes of *Menemerus bivittatus*, with no recording or behaviour test. | L78, L79, L122, L150 | m (*Menemerus confusus*), g | The Gray Wall Jumping Spider is the species at issue; the full text of Steck et al. 2024 is wanted. |
| Rear side eyes (PLE): field of one eye | About 130 to 135 degrees, reaching round to directly behind | L40, L258, L6 | m | None. |
| PLE: sharpness | 0.5 cycles per degree (1.0 degree between receptors) | L37, L193 | m | None. |
| PLE: colour classes | One, green; every cell recorded in *Plexippus validus* also responded to the plane of polarized light | L30, L78, L161 | m | Polarization is not drawn. |
| Posterior median eyes (PME) | Minute and probably vestigial in most species; in *Portia* they work and cover a strip about 20 degrees wide. The view leaves them out. | L69, L166, L204, L214, L136, L121 | g | Their sharpness (about 0.05 cycles per degree) comes from a review (L193). |
| Whole animal | The side eyes together cover about 360 degrees | L41, L87 | m | The rear is `invented` content. |

### 1b. The gaze strip

| Setting | Value | Log lines | Grade | What the evidence leaves open |
|---|---|---|---|---|
| Width and height | 2 by 20 degrees | L38, L39 | m | The single straight strip is `invented` (see AME overlap). |
| Jump (saccade) speed | At least 150 degrees per second: a 15 degree saccade is complete within 0.1 s. The engine uses 300 degrees per second. | L49 | m (*Metaphidippus harfordi*) | The value above 150 is `invented`. Body turns run at 120 to 1,200 degrees per second (L162, L64 note), which describes the body and does not bound the retina. |
| Latency from movement to first turn | Shortest 80 to 120 ms; most turns begin within 100 ms of the target stopping; about 0.5 s in a cueing task in *Menemerus semilimbatus* | L64, L189 | m | The spread [0.1, 0.5] s the engine draws is `invented`; the two figures come from different stimuli. |
| What starts a jump | A small movement of a target already in view. Still targets never start one. Lights that flash in place start nothing. Whole-field movement (moving gratings) starts nothing. | L56, L62, L98, L174 | m | The phone's own movement fills the field in the same way, so the view removes it: the method (gyroscope or mean image motion) is `invented`. |
| Smallest and best target | None below 0.4 degree; half-maximal at 0.7; strongest for dots of 2 to 4 degrees | L63, L96 | m | None. |
| Best speed | Strongest at 9 degrees per second, falling at 27 to 81; neurons fed by the principal eyes prefer 16 degrees per second; turns are evoked from about 1 to 100 degrees per second | L96, L63 note, L270 | m, g | The shape of the curve is `invented`. |
| Lowest contrast | 1 per cent; in practice, contrast against the local background | L97, L274 | m | None. |
| Looming and living motion | Looming draws the gaze most and makes the spider back away; shrinking draws no more than stillness; the front side eyes prefer the motion of living things | L113, L196, L1, L145, L147 | m | The weights are `invented`. |
| Smoothly following a target | Once locked, the strip follows over at least 25 degrees, tested below 10 degrees per second, and needs the front side eyes to see it | L54, L111 | m | None. |

### 1c. Scanning, dwell and ignoring

| Setting | Value | Log lines | Grade | What the evidence leaves open |
|---|---|---|---|---|
| Scanning sweeps (side to side) | Amplitude about equal to the target's width, never under 2 degrees and up to 10; period 1.1 to 1.3 s for targets of 2 degrees or less, 2.0 to 2.4 s for targets of 11 to 12 degrees; a review gives 3 to 10 degrees per second | L50, L261, L262 | m | None. |
| Scanning rotation (torsion) | 20 to 30 degrees each way, holding each end 2 to 5 s and taking about 2 s to turn; period 5 to 8 s at first, about 15 s by the fourth or fifth cycle. Rate and amplitude do not depend on the target. | L51 | m | Scanning follows the outlines of what is seen (L228), so turning the strip along the strongest edge is `invented`. |
| Scanning bout | 5 to 94 s, most 20 to 40 s; regular for 10 to 20 s, then broken by looks at other parts of the field | L52 | m | None. |
| Idle sweeps with nothing to look at | Bouts of 1 to 10 min, up to 45 by 35 degrees, 0.05 to over 1 Hz, 2 to 100 degrees per second | L53 | m | None. |
| Dwell after a jump without scanning | Holds 1 to 2 s, then the strip drifts back to rest; a 10 degree return takes 10 to 15 s | L55 | m | None. |
| Dwell on what is shown | Principal eyes dwell longer on still or slowly moving images; image speed does not change how the retinas rotate | L219, L112, L227 | g, m | No dwell figure for freely viewed natural scenes. |
| Fewer gaze shifts while examining something | A higher threshold while the strip is on a target, except for looming | L184, L195, L196 | m | The size of the rise is `invented`. |
| Time a place is ignored after a look | About 5 s: detection at the looked-at place is poor 0.2 s after the look and recovers steadily, matching the opposite side by about 5 s | L7, L190 | m (*Menemerus semilimbatus*) | The shape between 0.2 and 5 s is `invented`. |
| Habituation at one place | Repeated movement at one retinal place stops evoking turns within one or two repeats (at most 15); a target moved a few degrees away is answered again. Orienting to a repeated stimulus falls below half within 15 repeats, and faster when repeats come closer together. | L67, L278, L220 | m | The radius of the place (3 degrees) is `invented`. |

### 1d. Flicker, dim light, sleep and the rest

| Setting | Value | Log lines | Grade | What the evidence leaves open |
|---|---|---|---|---|
| Flicker fusion | About 40 Hz, second-hand from a 1990 video study of *Maevia inclemens*. Nearest measured spiders: a day-active crab spider, 10 Hz in the principal eyes and 20 to 30 Hz in the side eyes; a night-active wandering spider, 4.3 to 8.6 Hz. | L11, L172, L173, L210 | g | No jumping spider measurement was opened (Clark and Uetz 1990 is wanted). The engine's `rate` is left at the phone's pace: `invented`. |
| Photoreceptor response time | About 24 ms, an estimate that assumes the eyes scan as fast as they can without blur | L263 | i | The only temporal figure for jumping spider receptors found. |
| Dim light | A dim-light specialist (*Cyrba algerina*) identified prey at 1.35 cd/m2, fewer at 0.54 and none at 0.24. Typical day-active species are far less sensitive: optical sensitivity of the principal eye is 0.04 to 0.09 (against 101 in an ogre-faced spider); the front side eyes of adult *Phidippus audax* are 12 to 23 times more sensitive than hatchlings'. | L152, L235, L267, L132, L119, L134 | m (*Cyrba*), g | No threshold exists for the common genera. The mapping from the phone's brightness to cd/m2 and the fade of colour and detail first are `invented`. |
| Light adaptation | For about 60 s after a light the principal-eye receptors are more sensitive than when fully dark-adapted, most so 3 to 5 s after; no daily rhythm in their sensitivity | L158, L159 | m (*Menemerus confusus*) | None. |
| Time of day | Day-active; withdraw into a silk nest in cloudy or rainy weather | L133, L141 | g | None. |
| Sleep-like retinal bouts | At night in spiderlings of *Evarcha arcuata*: bouts of retinal movement lasting a median 77 s, every median 17 min, both lengthening through the night (by 11 and 38 per cent). Adults curl their legs in bouts of a median 84 s every 28 min. | L168, L169 | m | The 60 s of stillness in the dark before the first bout is `invented`, so that a person can see one. |
| Magnification of the strip | 1.25 times in *Plexippus*, 1.54 in *Portia*, from the telephoto component | L26, L73 | m | Using it as screen magnification is `invented`. |
| Pupil, depth-of-field blur | A camera eye; a pupil in light-loving species. The second layer of the retina sees a defocused copy that gives distance, and it grew blurrier under red light in the one experiment; one attempt to repeat part of it gave a different result. | L26, L73, L194, L144, L230, L237 | m, g | Blur shape and strength are `invented`. |
| Hearing and ground vibration | Low airborne tones (80 Hz) make the spider freeze; courtship and learning use vibration through the ground. The picture leaves both out (an optional microphone or accelerometer effect). | L247, L248, L249 to L252 | x | None. |

## 2. Colour classes by genus

"Two" means ultraviolet and green. Shares are of iNaturalist research-grade records (GBIF, 13 October 2026) worldwide and in Alachua County, Florida.

| Genus | World / Alachua share | Receptor classes in the principal eyes | Log lines | Status |
|---|---|---|---|---|
| *Phidippus* | 21.7% / 21.3% | Two, near 370 and 532 nm; no red filter | L163 to L165, L109, L182, L211 | two, measured |
| *Menemerus* | 7.1% / 9.8% | Disputed: four reported from seven cells in *M. confusus*, doubted; side eyes green only, with a possible blue opsin in *M. bivittatus* | L80 to L82, L32, L78, L79, L150 | disputed |
| *Salticus* | 7.1% / 0 | Probably two; no red filter | L14, L109 | two, probable |
| *Platycryptus* | 6.6% / 4.2% | None found | | unmeasured |
| *Maratus* | 2.8% / 0 | Four claimed, with blue at 480 to 500 nm, from a conference abstract cited in a review | L191 | claimed, weak |
| *Eris*, *Paraphidippus* | 2.6% each / 1.0%, 0 | None found | | unmeasured |
| *Habronattus* | 2.5% / 0.3% | Three in a small central patch: 377, 530 and a red-filtered class near 626 nm; filters in four more species | L102 to L108, L126, L155, L183, L221 | three at the centre, measured |
| *Plexippus* | 2.3% / 2.1% | Two in *P. validus*; the Pantropical Jumping Spider, *P. paykulli*, is unmeasured | L21 to L23 | two, one species |
| *Anasaitis* | 2.2% / 25.7% | None found | | unmeasured |
| *Marpissa* | 2.2% / 0.2% | Brain anatomy only | L8, L9 | unmeasured |
| *Evarcha* | 2.1% / 0 | Behaviour only: coloured gratings chosen over every grey; red-dyed prey preferred | L46, L185 | behaviour only |
| *Lyssomanes* | 1.8% / 21.9% | None; perches chosen by brightness, with green no better than a matched grey | L239 | unmeasured |
| *Attulus*, *Hentzia*, *Colonus*, *Philaeus* | 1.5% to 1.7% each / 0, 4.8%, 6.0%, 0 | None found | | unmeasured |
| *Hasarius* | 1.5% / 0 | Two: green Rh1 (535 nm in solution) in layers 1 and 2, ultraviolet Rh3 in layers 3 and 4; the blue pigment Rh2 was never found in the principal eyes | L143, L282 | two, measured |
| *Saitis* | under 1.5% | Probably two, 359 and 526 nm; red not told from black | L12, L13, L198, L14, L176, L197 | two, measured |
| *Cosmophasis*, *Phintella*, *Maevia*, *Siler* | each under 1.5% | Ultraviolet used as a hue (*Cosmophasis*), ultraviolet B signals (*Phintella*), sensitivity 330 to 700 nm (*Maevia*), red coverage watched (*Siler*) | L200, L140, L179, L277 | behaviour or range only |

The view uses two classes for every genus except *Habronattus*.

### Claims from a summary of jumping spider vision, tested against the log

| Claim | Result | Log lines |
|---|---|---|
| The front eyes sense the human-visible spectrum and ultraviolet | Holds for sensing in every species measured. Discriminating colours across that range holds only for the *Habronattus* patch; most species have two classes, so a red looks like a darker green. | L179, L83, L186, L15, L151, L110, L107, L197 |
| The side eyes lack colour | Holds as one green class in the species recorded. A possible blue opsin in two species is untested. | L78, L79, L122, L150 |
| The side eyes act like motion detectors | They answer only to movement and start turns within 80 to 120 ms, but they also pick out living motion, looming and displacements finer than their receptor spacing, and can guide a chase alone. | L56, L62, L64, L1, L113, L157, L99, L212, L213 |
| The side eyes inform the whole picture | They aim the principal eyes, prime their scanning and pull them away with distractors. | L111, L216, L229, L234, L184, L195, L196 |
| Nobody knows exactly how the information comes together | A 2012 review says so. Separate brain pathways, interaction in scanning and neurons with body-fixed receptive fields show that something is combined. | L95, L8, L9, L19, L229, L269 |
| A busy scene, like a crowded square | The side eyes cover about 360 degrees and respond at 1 per cent contrast, but most of what reaches them is filtered out: still things, whole-field motion, flicker in place and repeated movements start no turns. The boring reading, a quiet wall with interruptions, fits the same measurements; nobody has counted how often small things move near a wild spider. | L41, L97, L56, L98, L62, L67 |
| The eyes' pictures are divided | No study describes a divided percept; one review calls the principal eyes a single "giant, virtual, and active eye". | L86, L269 |

## 3. Questions for a jumping spider specialist

1. In the species most photographed in Florida (*Anasaitis*, *Lyssomanes*, *Platycryptus*, *Colonus*, *Hentzia*, *Menemerus bivittatus*), do the principal eyes have only ultraviolet and green classes, or has any shown a red filter or a third class?
2. Do the possible blue-sensitive receptors found by opsin labelling in some side eyes (*Menemerus bivittatus*) give those eyes colour, or only brightness, and does the colour seen by the principal eyes carry over to the wide scene the side eyes watch?
3. What are the flicker fusion frequency and photoreceptor response time of the principal eyes and of the front side eyes in any jumping spider?
4. In a free-living spider on a wall, how often does the gaze strip jump to a new target, how long does it stay on one, and does the 5 second suppression of a looked-at place apply to the principal eyes as well as the front side eyes?
5. At one instant, how much of the field do the two retinal strips resolve together, and is one straight strip a fair way to draw the pair for a person?
6. Has the red-light depth result of Nagata et al. 2012 been repeated in other species, and how large is the second, defocused image in natural scenes?
