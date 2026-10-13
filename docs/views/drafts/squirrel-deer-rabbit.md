# Squirrel, deer and rabbit: senses sheet (round 3)

Unit `squirrel-deer-rabbit`. It re-checks the views `squirrel` (order Rodentia), `deer` (families Cervidae, Bovidae, Equidae, Antilocapridae, Camelidae and Giraffidae) and `rabbit` (order Lagomorpha) in `src/cam.a.js`, and proposes where they should split.

Written on 13 October 2026 from 01:46 UTC, from the collection on `pub/lit-t1` (topics rodents-lagomorphs and ungulates, with mammals-other, methods and carnivores for cross-species work), two books and papers from the owner's library, and public web pages. The evidence log is `docs/views/evidence/squirrel-deer-rabbit.jsonl`; **L*n*** below means line *n* of that file. The wanted list is `docs/views/wanted/squirrel-deer-rabbit.jsonl`.

What could not be read, and why:

- **From the owner's library.** Caves, Brandley and Johnsen (2018) came through as the main text only; its supplementary tables S1 to S3, which hold the per-species acuity values, were not in the copy. Land and Nilsson (2012) came through from the front matter to chapter 3, page 63 (the start of "Available photon numbers"); chapters 4 to 9, which include the chapter on lens eyes on land and the chapter on eye movements, did not come through.
- **Refused or rate-limited.** Crossref's API, Europe PMC's REST service and PubMed each answered HTTP 429 once and were not asked again. GBIF's API was refused by this machine's network policy from the shell and answered through the fetch tool. ScienceDirect, PMC search and the iNaturalist API refuse robots, so every Elsevier paper (Vision Research, Behavioural Processes, Applied Animal Behaviour Science and others) is on the wanted list unless its abstract was in the collection. The Science Advances page for Banks and colleagues (2015), the AVMA page for Timney and Macuda (2001) and the Semantic Scholar API failed to load.

## 1. Scope and where the views should split

### What the three views hold today

Records are iNaturalist research-grade observations in GBIF. Group totals are from `docs/VIEWS.md` (read 11 October 2026). Family counts for Rodentia were read from GBIF's facets on 13 October 2026 through the fetch tool; family counts for the hoofed families come from the stored facet file `runs/fetch/10/world-family-top.json` on the `ci` branch (11 October), with Bovidae found by subtraction. Genus and species counts are from the iNaturalist open-data snapshot of 27 September 2026 as the repository's coverage run lists it (`runs/coverage/1-lists/world.tsv.gz` on `ci`, column `rg_all`); its family sums agree with GBIF's to within 1.3%. Alachua counts are from `data/regions/us-fl-alachua/species.json` (GBIF, records through 2024).

**`squirrel` (order Rodentia): 1,405,835 world records.** By continent: North America 76.2%, Europe 12.8%, Asia 5.3% (`records-by-group.tsv` on `pub/data-world`).

| Family | Members | World records | Share |
|---|---|---:|---:|
| Sciuridae | tree squirrels, ground squirrels, chipmunks, marmots, prairie dogs, flying squirrels | 1,062,360 | 75.6% |
| Castoridae | beavers | 81,805 | 5.8% |
| Cricetidae | New World mice, voles, muskrats, cotton rats, hamsters | 80,013 | 5.7% |
| Muridae | Old World mice and rats, gerbils | 57,050 | 4.1% |
| Myocastoridae | coypu (nutria) | 29,333 | 2.1% |
| Erethizontidae | New World porcupines | 24,931 | 1.8% |
| Caviidae | capybara, cavies, maras | 17,601 | 1.3% |
| Dasyproctidae | agoutis | 16,138 | 1.1% |
| Hystricidae | Old World porcupines | 8,269 | 0.6% |
| Geomyidae | pocket gophers | 7,718 | 0.5% |
| 22 other families | dormice, jerboas, mole-rats, chinchillas and others | 20,617 | 1.5% |

Within Sciuridae (snapshot genus sums): tree squirrels about 688,600, ground squirrels, chipmunks, marmots and prairie dogs about 352,200, flying squirrels about 7,900 (*Glaucomys* 4,350, *Pteromys* 1,200, *Petaurista* and others). The most recorded rodents in the world are the eastern grey squirrel (300,608), eastern fox squirrel (125,998), eastern chipmunk (80,057), American red squirrel (75,044), Eurasian red squirrel (69,438), American beaver (60,181), California ground squirrel (48,233), groundhog (45,482), muskrat (42,435), coypu (29,099) and North American porcupine (24,001). In Alachua County the view has 1,187 records in 13 species: eastern grey squirrel 1,010 (85.1%), hispid cotton rat 60 (5.1%), eastern fox squirrel 44 (3.7%), southern flying squirrel 23 (1.9%), southeastern pocket gopher 20 (1.7%), black rat 11, round-tailed muskrat 4, Florida mouse 4, house mouse 3, cotton mouse 3, American beaver 2 and brown rat 2.

**`deer` (six hoofed families): 1,002,329 world records.** By continent: North America 62.7%, Africa 16.9%, Europe 12.8%, Asia 4.9%.

| Family | Members | World records | Share |
|---|---|---:|---:|
| Cervidae | deer, elk, moose, caribou | 678,629 | 67.7% |
| Bovidae | cattle, bison, buffalo, sheep, goats, antelope | 238,801 | 23.8% |
| Equidae | horses, zebras, asses | 37,473 | 3.7% |
| Antilocapridae | pronghorn | 19,707 | 2.0% |
| Giraffidae | giraffes, okapi | 18,819 | 1.9% |
| Camelidae | camels, llamas, alpacas, guanaco, vicuña | 8,900 | 0.9% |

The most recorded species are the white-tailed deer (310,997), mule deer (150,439), roe deer (58,711), moose (45,067), wapiti (42,201), bighorn sheep (23,085), American bison (20,132), pronghorn (19,642), plains zebra (17,579), red deer (15,223), impala (13,957) and African buffalo (11,995). Domestic animals are mostly casual records, which the full database also names: cattle 4,147 research-grade and 30,085 casual, horses 11,576 and 18,869, sheep 3,172 and 13,649, goats 6,763 and 12,079, donkeys 4,758 and 5,443. In Alachua the view has 1,187 records in three species: white-tailed deer 799 (67.3%), domestic horse 236 (19.9%, many of them the free-roaming horses of Paynes Prairie) and American bison 152 (12.8%).

**`rabbit` (order Lagomorpha): 335,387 world records**, North America 75.7%, Europe 17.6%. Leporidae (rabbits and hares) hold 322,918 (96.3%) and Ochotonidae (pikas) 12,469 (3.7%). The most recorded are the eastern cottontail (138,698), European rabbit (38,839), desert cottontail (36,185), European hare (32,418), black-tailed jackrabbit (17,564), snowshoe hare (15,483) and American pika (9,820). In Alachua: marsh rabbit 459 (77.8%), eastern cottontail 127 (21.5%), European rabbit 4.

### Where the views should split

**1. Day-active squirrels against every other rodent.** The `squirrel` view today draws a day-active squirrel for every rodent, and that picture is false for the quarter of rodent records that are mice, rats, beavers and their kin.

- Day-active squirrels have yellow lenses that pass no ultraviolet: the grey squirrel's lens transmits 50% at 441 nm and none of the ultraviolet A band, the prairie dog's and Richardson's ground squirrel's 0 to 0.6% (L15 to L17, L33, L46). Mice and rats have lenses that pass 56 to 81% of ultraviolet A (L19 to L21) and cones most sensitive to ultraviolet at 359 to 362 nm (L82, L84, L86, L68; the deer mouse's S cones also carry an ultraviolet opsin, L72; Jacobs and colleagues first found such receptors in rodents, L134).
- Squirrel retinas are dominated by cones: about 15% rods in the California ground squirrel (L45) and two rods to three cones in the grey squirrel (L130). The deer mouse has about 450,000 rods and 3,000 to 6,500 cones per square millimetre (L72).
- A rat sees about 1 cycle per degree, wild rats included (L158, L159, L3, L64, L89), and a house mouse about 0.5 (L157, L67). Squirrels see a little more: they are grouped with the tree shrew's 1.2 to 2.4 (L160, L161), and the packing of a ground squirrel's cones and ganglion cells allows up to about 7 to 14 (L125, the sheet's own arithmetic). The Nile grass rat, a day-active murid, already sees more than twice what laboratory rats and mice see (L63).
- The southern flying squirrel is a sciurid that lives at night: its lens is clear (29% of ultraviolet A, L18) and one of its two retinal processes cannot follow flicker above 10 to 15 Hz (L133). It belongs with the night-active rodents.

The line: **`squirrel`** keeps family Sciuridae except the flying squirrels (genera *Glaucomys*, *Pteromys*, *Petaurista*, *Petinomys*, *Hylopetes*, *Aeromys*, *Trogopterus*, *Belomys*, *Iomys*, *Petaurillus*, *Pteromyscus*, *Eoglaucomys*, *Eupetaurus* and *Aeretes*): about 1,054,400 world records (75.0% of Rodentia) and 1,054 of Alachua's 1,187 (88.8%). A new **`mouse`** view takes every other rodent and the flying squirrels: about 351,400 world records (25.0%) and 133 in Alachua (11.2%). The `mouse` view is dominated by large rodents in world records (beavers 81,600, muskrats 42,400, coypu 29,100 and porcupines 35,100 in the snapshot, about 188,000 together, more than half of it), and nothing in this session measured their eyes except an anatomical estimate for the European beaver (L59). They join `mouse` because what is known of night-active rodents suits them better than a day squirrel's eye, and the view gives them their own sharpness (section 2.2).

**2. Tree squirrels against ground squirrels and chipmunks, inside `squirrel`.** Two measured differences change the picture without needing a second view, so they become settings chosen by genus when the full database names the species:

- **Pace.** In retinal recordings (electroretinograms, which read the eye's electrical response) the golden-mantled ground squirrel and the yellow-pine chipmunk follow flicker to 100 to 120 Hz (L5, L6, L9, L10), and the American red squirrel, a tree squirrel, to 60 to 65 Hz (L7, L11), against 55 Hz for people by the same method in the same table (L7 note). All three values come from one 1961 study that neither compilation reproduces in full (wanted).
- **Colour.** The grey squirrel's green-sensing cone peaks at 543 nm (L129) and the ground squirrels' at 517 to 519 nm (L127), so reds fall darker for a ground squirrel.

Tree squirrels hold about 65% of the view's world records, and the eastern grey squirrel alone holds 29% of the view's world records and 96% of its Alachua records, so the view's defaults follow the tree squirrel.

**3. Horses, giraffes and camels against deer, cattle and antelope.** Every hoofed animal measured has two cone types (L90 to L91, L95 to L96, L117 to L119), a horizontal streak (L92, L94, L97, L104, L106) and, where it was examined, a horizontal pupil (L113, L116). Sharpness is where they part, and it is the setting the picture shows on every frame. Measured behaviourally, the white-tailed deer resolves 4 to 6 cycles per degree (L100; red deer also under 6, L142), the sika deer about 4.8 (L103) and cattle 2.6 to 5 (L151). Horses tested behaviourally averaged about 20/30 on the Snellen scale, about 20 cycles per degree, and the best reached 23.3 (L150, L155), with 16.5 estimated from the streak's ganglion cells (L92). The giraffe's best area resolves 25 to 27 by anatomy (L104), the alpaca's 12.5 to 13.4 (L106), and the dromedary 9.5 to 10, with a behavioural 10 in one Bactrian camel (L105). A deer picture at 5 would be two to five times too blurry for these large-eyed animals. Cattle, animals of the horse's size, see far less (L155, L151), so body size alone does not draw the line. The horse's lens also blocks nearly all ultraviolet (4.6% of ultraviolet A, L31) where deer, cattle and sheep pass 15 to 27% (L25 to L28), and its eyes overlap by 65 to 80 degrees down its nose, with a blind area in front of the forehead (L93, L148, L149).

The line: **`deer`** keeps Cervidae, Bovidae and Antilocapridae, 937,137 world records (93.5% of the group) and 951 in Alachua (80.1%). A new **`horse`** view takes Equidae, Giraffidae and Camelidae, 65,192 world records (6.5%) and 236 in Alachua (19.9%), with the giraffe's and the camels' own sharpness set by family. The deer, cattle and horse values are behavioural; the giraffe's and alpaca's are anatomical. In the one animal measured both ways here, the camel, the two agree (L105), and in the horse the behavioural value exceeds the anatomical estimate (L150, L92). The horse values come through two reviews (L150, L155); Timney and Keil (1992) itself is wanted.

Cattle and bison (Alachua's 12.8%) stay with `deer`: their acuity of 2.6 to 5 (L151) matches the deer's, and their cones match sheep and goats (L95, L96). Sheep are the one unsettled member. Landolt-ring scores give about 2.6 to 5.7 if read as decimal acuity (L135), while a review states "up to 14 cycles per degree" (L147); the sheep stays with `deer` until the paper behind that figure is read.

**4. No split inside `rabbit`.** Rabbits and hares share a horizontal streak (L75, L38, L40), a nearly complete circle of view (L74) and two cones (L79, L80). Pikas (3.7%) are day-active and unmeasured here (wanted: Akaishi and colleagues 1995); they stay with `rabbit` until a measurement says otherwise.

**The set of views this sheet commits to:** `squirrel` (day-active squirrels, 75.0% of rodent records), `mouse` (all other rodents and the flying squirrels, 25.0%), `rabbit` (all lagomorphs), `deer` (deer, cattle, antelope, pronghorn, 93.5% of the hoofed group) and `horse` (horses, zebras, asses, giraffes, camels and llamas, 6.5%).

## 2. The proposed views

Rows are `[grade, title, text]` as the page shows them. Under each row, **Log** names the lines behind it. Values marked *invented* are the app's own choice.

Two engine conventions are proposed for all five views.

- **Colour from the measured cone pair.** Today's `PROTAN` and `DEUTAN` matrices treat every dichromat as a person missing one cone. The animals' long-wave cones lie between a person's green (about 530 nm) and red (about 560 nm) cones, at 502 to 543 nm in rodents, rabbits, deer and horses and at 552 to 555 nm in cattle, sheep and goats (L80, L85, L91, L96, L118, L127, L129). The sheet proposes mixing the two matrices by where the animal's long cone falls: weight w = (λ − 530) / (560 − 530), limited to 0 and 1, and matrix = (1 − w) `PROTAN` + w `DEUTAN`. That gives w = 0 for rabbits, rats, mice and ground squirrels, 0.23 for the white-tailed deer, 0.30 for the horse, 0.43 for the grey squirrel and about 0.77 for cattle. The rule is *invented*; it uses only measured peaks. The matrices themselves were entered from memory (`docs/SOURCES.md`) and need checking against Viénot, Brettel and Mollon (1999), which is outside this unit.
- **Sharpness by species where measured.** Section 4 lists the species whose own acuity the full database can apply.

### 2.1 `squirrel`: tree squirrels, ground squirrels, chipmunks, marmots and prairie dogs

Chip: "Squirrel, chipmunk, marmot". Who: "a squirrel". Cue: "Blues are dimmed, and the sharpest part is a wide band along the horizon."

**Rows**

- `['m', 'Colour', 'Grey squirrels and ground squirrels have two kinds of colour-sensing cells, most sensitive to blue and to green, where people have three. Red and orange look much like green to a squirrel, and a blue-green looks grey. This view mixes colours the same way.']`
  Log: L128, L129, L131 (grey squirrel cones at 444 and 543 nm, colourless point near 500 nm); L126, L127 (ground squirrels at 437 and 519); L47 to L49 (fox squirrel); L53 (Finlayson's squirrel cannot tell orange or red from green); L54.
- `['m', 'Yellow lenses', 'A day-active squirrel has a yellow lens that blocks ultraviolet light and part of the violet and blue. Its world looks a little as yours does through yellow sunglasses, and this view dims blues and violets to match.']`
  Log: L15 (grey squirrel, 50% transmission at 441 nm, no ultraviolet A); L16, L17 (prairie dog, Richardson's ground squirrel); L46 (thirteen-lined ground squirrel, everything below 410 nm absorbed); L33.
- `['m', 'Sharpest band', 'A squirrel sees most sharply along a broad band level with the horizon, and its sharpness falls off only gradually above and below the band. In an eastern chipmunk the sharpest region spans about 155 degrees from side to side. This view keeps a wide horizontal band sharp.']`
  Log: L44, L45, L124 (horizontal streak in two ground squirrels); L39 (chipmunk 155 degrees), L37 (prairie dog 116), L36 (groundhog 90.5).
- `['m', 'Speed', 'The eyes of ground squirrels and chipmunks respond to a flickering light up to 100 to 120 flashes a second, about twice as fast as a person's. The one tree squirrel measured, the American red squirrel, reaches 60 to 65, close to a person's. For ground squirrels and chipmunks this view runs slowly and then jumps ahead to catch up, and for tree squirrels it keeps your pace.']`
  Log: L5, L6, L9, L10 (ground squirrel and chipmunk, 100 to 120 Hz by ERG); L7, L11 (red squirrel, 60 to 65 Hz); L14 (ground squirrel optic nerve fibres follow at least 50 Hz).
- `['g', 'Dusk', 'A grey squirrel's retina has two rods, the cells that work in dim light, for every three cones. A ground squirrel's retina has about one rod in every seven cells. Tree squirrels keep more of their sight at dusk, and this view lifts the shadows a little for them.']`
  Log: L130 (grey squirrel, rods to cones about 2 to 3); L45 (ground squirrel, 1.27 million rods of 8.77 million cells); L156 (a thirteen-lined ground squirrel's dark-adapted retina needs about a thousand times more light than a rat's); L47 to L49 note (the fox squirrel's sensitivity shifts toward a 500 nm rod pigment in the dark).
- `['g', 'Sharpness', 'Grey squirrels and ground squirrels see fine detail about as poorly as tree shrews, which make out a twenty-fifth to a fiftieth of the detail a person sees. The spacing of a ground squirrel's light-sensing cells would allow more. This view assumes about a fifteenth, which is a guess.']`
  Log: L160 (squirrels grouped with the tree shrew for low spatial resolution, citing Jacobs and colleagues 1980 and 1982); L161 (tree shrew, 1.2 to 2.4 cycles per degree); L125 (cell-spacing limits of about 7 to 14, the sheet's arithmetic from L124); L44; L55.
- `['i', 'Field of view', 'This view assumes that a squirrel takes in about 300 degrees around itself, close to the 295 degrees measured in a rat. This part of the view is a guess.']`
  Log: L70.
- `['x', 'Hearing', 'A fox squirrel can tell which way a brief sound came from to within about 15 degrees. Prairie dogs and groundhogs hear pitches up to about 27,000 vibrations a second. This view leaves sound out.']`
  Log: L41, L42.

**The picture**

| Field | Value | Behind it |
|---|---|---|
| `fov` | 300 | *invented*; nearest measured rodent L70 (rat, 295) |
| `cpd` | 4 | *invented*; squirrels grouped with the tree shrew's 1.2 to 2.4 (L160, L161); upper limits about 7 to 14 from cell spacing (L125, L44) |
| `topoS` | 1 | L44, L45, L124 |
| `fall` | 0.8 | *invented*; the fall is gradual (L44: about five-fold across the whole retina) |
| new `streakW` | 150 degrees | L39 (chipmunk 155), L37 (prairie dog 116), L36 (groundhog 90.5) |
| `pupil` | 'o' | *invented*; no source for squirrel pupils was read |
| `dof` | 4 | *invented* |
| `M` | mix w = 0.43 (tree squirrels); w = 0 (ground squirrels, chipmunks, marmots) | L129, L127; the mixing rule is *invented* |
| new `yellow` | 0.4 (tree squirrels); 0.55 (ground squirrels, prairie dogs, marmots) | L15 (50% at 441 nm), L16, L17 (50% at 462 to 463 nm), L46; the size of the cut is *invented* |
| `rate` | 1 (tree squirrels); 0.5 (ground squirrels, chipmunks) | L7, L11; L5, L6, L9, L10, with people's ERG value of 55 Hz (L7 note): 55 / 108 = 0.51 |
| `gain` | 1.1 (tree squirrels); 1 (ground squirrels) | *invented*; L130, L45 |
| `sat`, `uvBlue`, `sheen` | 1, 0, 0 | L15 to L17, L33 (no ultraviolet reaches the retina) |

**New effects**

- **A yellow lens.** Before the colour mixing, the shader multiplies the camera's blue channel by (1 − `yellow`) and the green channel slightly less. A person sees a warmer picture in which blue sky darkens and violet flowers lose their violet. The cost is one multiply a pixel. It is true to the measured lens and it gives the squirrel a recognizable, sunny look.
- **A sharp band with a width.** The engine's band is sharp across the whole frame. A `streakW` setting would let the band fade at its ends, so the chipmunk's 155 degrees of best sight sit across the middle of the squeezed panorama and the far edges stay soft. It is a small change to the blur weight.
- **Pace and colour by tribe.** Both are data that the full database applies when it names a genus (section 4). No new code beyond a lookup.

### 2.2 `mouse` (new): mice, rats, voles, beavers, porcupines and the other rodents

Chip: "Mouse, rat, beaver". Who: "a mouse or rat". Cue: "Reds go dark, and the sky turns violet. Moving things leave short trails."

**Rows**

- `['m', 'Ultraviolet and green', 'Mice, rats and gerbils have two kinds of colour-sensing cells: one most sensitive to ultraviolet light, which people cannot see, and one to green. Their lenses let most ultraviolet through. The violet tint in this view stands in for ultraviolet, and its strength is the app's own choice.']`
  Log: L82 to L87 (mouse 359 and 511 nm, rat 362 and 502, gerbil 362 and 493); L68, L69; L72 (deer mouse); L19 to L21 (lenses pass 56 to 81% of ultraviolet A); L134.
- `['m', 'Reds go dark', 'The green-sensing cells of a mouse or rat respond best to blue-green light and hardly at all to red. Red things look dark to a mouse, and this view darkens them to match.']`
  Log: L83, L85, L87, L69; L66 (the rat's single visible-light cone near 510 nm).
- `['m', 'The sky above', 'In the lower part of a mouse's retina, which looks up at the sky, nearly every cone senses short wavelengths. A mouse sees the sky mostly through its ultraviolet-sensing cells, and this view shows the upper part of the picture through that channel alone.']`
  Log: L77 (in mice and rabbits every cone in a ventral zone carries the short-wave pigment). That the lower retina views the upper field follows from the optics of any camera eye; the sheet's inference.
- `['m', 'Sharpness', 'A rat sees about a sixtieth as much detail as a person does, and a house mouse about half as much as a rat. This view is blurred to match.']`
  Log: L158, L159 (Long-Evans and wild rats about 1 cycle per degree, albino strains 0.5); L3, L64, L89; L157, L67 (C57BL/6 mice about 0.5).
- `['m', 'Field of view', 'A rat takes in about 295 degrees around itself, and its two eyes overlap most above and slightly behind its head. This view bends the picture at its edges to suggest the wider sweep.']`
  Log: L70, L71.
- `['g', 'Night', 'Mice and rats are active mostly at night, and their retinas are packed with rods, the cells for dim light. A deer mouse has about a hundred rods for every cone. This view brightens the shadows and lets moving things leave short trails.']`
  Log: L72 (deer mouse, rods about 450,000 and cones 3,000 to 6,500 per mm²); L156 (a rat's retina responds to light about a thousand times dimmer than a ground squirrel's); L8, L13 (albino rats follow flicker to 25 to 39 Hz); L133 (flying squirrel rod process, 10 to 15 Hz). The length of the trails is *invented*.
- `['i', 'Larger rodents', 'Beavers, muskrats, porcupines, coypus and capybaras share this view, though little is known about their eyes. The retina of a European beaver could resolve two to three times the detail a rat sees, and this view sharpens the picture for the larger animals. That part of the view is a guess.']`
  Log: L59 (beaver, about 17 arcmin in air, 1.8 to 3.5 cycles per degree by the two possible readings); L2 note (acuity rises with eye size).
- `['x', 'Whiskers and sound', 'A rat sweeps its whiskers back and forth about eight times a second to feel its way. A house mouse hears pitches up to about 90,000 vibrations a second. This view leaves touch and sound out.']`
  Log: L140, L137, L43.

**The picture**

| Field | Value | Behind it |
|---|---|---|
| `fov` | 300 | L70 (rat, 295.4) |
| `cpd` | 1; house mouse 0.5; beavers 2.5; capybaras, agoutis, porcupines, coypu 2 | L158, L159, L3, L64; L157, L67; L59 (beaver); the larger animals' values are *invented* from L59 and L2 |
| `topoS` | 0.5 | L35 (spiny mouse, best vision 81 degrees wide); weight *invented* |
| `fall` | 0.5 | *invented* |
| `pupil` | 'o' | *invented*; rodent pupils were not in the sources read |
| `dof` | 2 | *invented* |
| `M` | new `RODENT` matrix: every channel = 0.05 R + 0.6 G + 0.35 B | *invented* weights for a single cone near 505 nm (L83, L85, L87); reds come out dark |
| `uvBlue` | 1 | L82, L84, L86; the tint is *invented* |
| new `skyBand` | upper 45% of the frame, ultraviolet channel only, held level with the horizon by the tilt sensor | L77; the share of the frame is *invented* |
| `gain` | 1.7 | *invented*; L72 |
| `persist` | 0.15 | L8, L13, L133; value *invented* |
| `sat` | 0.5 | *invented* |
| `rate` | 1 | *invented*; no mouse flicker value was found |

**New effects**

- **A sky band.** A soft-edged mask covers the upper part of the frame and shows only the ultraviolet stand-in channel (the camera's blue, darkened toward violet). The phone's accelerometer keeps the mask's edge on the real horizon, so tilting the phone up fills the screen with the violet sky and tilting it down brings back the green-grey ground. Dark birds and branches stand out against the sky band as silhouettes. The shader cost is one mask and one mix; the tilt input already exists for the wading bird's gait. It is true to the mapped retina and it gives the mouse a picture unlike any other in the app.
- **Trails in the dark.** In dim scenes the `persist` trail grows, following the slow rod responses. It reuses an existing effect.
- **Sharpness by body size.** Data only (section 4).

### 2.3 `rabbit`: rabbits, hares and pikas

Chip: "Rabbit, hare". Who: "a rabbit". Cue: "You see the whole circle at once. A band along the horizon is sharp, and the sky is shown in one colour."

**Rows**

- `['m', 'All the way around', 'A rabbit sitting still takes in the full circle around itself, 360 degrees, and its two eyes overlap by 24 degrees in front. A phone camera sees a small part of that, so this view squeezes the whole circle into the picture.']`
  Log: L74, L73.
- `['m', 'Sharp along the horizon', 'A rabbit sees most sharply along a band level with the horizon. Below the band its retina has about a tenth as many of the cells that carry detail to the brain. In cottontails the band reaches nearly all the way around, and this view keeps it sharp and blurs the rest.']`
  Log: L75 (5,400 against 550 ganglion cells per mm²); L38 (domestic rabbit, best vision 125 degrees wide); L40 (cottontails); L1.
- `['m', 'Colour', 'A rabbit has two kinds of colour-sensing cells, most sensitive to blue and to green, where people have three. Reds look dark and dull to a rabbit, and this view shows colours that way.']`
  Log: L79, L80 (wild rabbit, 425 and 523 nm); L81 (rods 498); L78 (rabbits respond differently to red and green lights).
- `['m', 'One colour for the sky', 'The lowest strip of a rabbit's retina, which looks at the sky overhead, holds only blue-sensing cones. A rabbit sees the sky above it in shades of a single colour, and this view shows the top of the picture the same way.']`
  Log: L76 (the lowest 5 to 6% of the retina holds blue cones only, 11,000 per mm²); L77. The mapping of the lower retina to the upper field is the sheet's inference from the optics.
- `['g', 'Looking ahead', 'When a rabbit turns its attention forward, its eyes can swing inward by about 18 degrees so that both see the same things ahead. This view narrows its sweep and sharpens a zone in front while you walk forward.']`
  Log: L73 (an 18-degree vergence from the freeze position, which the authors propose as a second state for forward vision). The walking trigger is *invented*.
- `['i', 'Sharpness', 'This view assumes that a rabbit sees about a twentieth as much detail as a person does, which is a guess.']`
  Log: none; wanted (Vaney 1980; Van Hof 1967).
- `['x', 'Ultraviolet', 'A rabbit's lens lets through about an eighth of the ultraviolet light that reaches it, so a rabbit may sense a little ultraviolet. This view leaves ultraviolet out.']`
  Log: L24.
- `['x', 'Hearing', 'A domestic rabbit hears pitches up to about 49,000 vibrations a second and can tell which way a brief sound came from to within about 17 degrees. This view leaves sound out.']`
  Log: L136, L139.

**The picture**

| Field | Value | Behind it |
|---|---|---|
| `fov` | 360 | L74 |
| `cpd` | 3 | *invented*; wanted |
| `topoS` | 1 | L75, L38, L40, L1 |
| `fall` | 2.2 | *invented*; ganglion cells fall tenfold below the band (L75) |
| new `streakW` | 300 degrees | L40 (cottontails, nearly the whole horizon), L38 (125 in a domestic rabbit); *invented* between them |
| new `binoc` | 24 degrees in front, widening to 42 while walking | L73 (24 in the freeze posture, plus an 18-degree vergence) |
| `pupil` | 'o' | *invented* |
| `dof` | 6 | *invented* |
| `M` | mix w = 0 (`PROTAN`) | L80 (523 nm); rule *invented* |
| new `skyBand` | upper 12% of the frame, blue channel only, levelled by the tilt sensor | L76; the share is *invented* |
| `gain` | 1.3 | *invented* |
| `rate` | 1 | *invented*; no rabbit flicker value was found |

**New effects**

- **A one-colour sky.** The same mask as the mouse's sky band, narrower and drawn in blue only: the top of the picture loses its colours and keeps its brightness. It is cheap, and together with the full circle squeezed into the screen it makes the rabbit's view legible at a glance.
- **Two postures.** While the phone is still, the full circle; when the motion sensors show steady forward walking, the view eases the sweep a little narrower and sharpens the front 42 degrees. Medium effort: it needs a smoothed walking detector and a blend between two `fov` and `binoc` states.

### 2.4 `deer`: deer, cattle, bison, sheep, goats, antelope and pronghorn

Chip: "Deer, cattle, antelope". Who: "a deer". Cue: "A wide band along the ground is sharp. Out-of-focus things smear sideways, and the smear stays level when you tilt the phone."

**Rows**

- `['m', 'Colour', 'White-tailed deer have two kinds of colour-sensing cells, most sensitive to blue and to green, where people have three. Cattle, sheep and goats have the same two kinds, with the green one shifted toward yellow. Reds and oranges are hard for them to tell from greens, and this view mixes colours the same way.']`
  Log: L117, L118 (white-tailed deer, 450 to 460 and 537 nm); L119 (fallow deer, 542); L120 (rods, 497); L95, L96 (cattle, goats and sheep, 444 to 455 and 552 to 555).
- `['m', 'Sharpness', 'A white-tailed deer sees about a tenth to a fifteenth as much detail as a person does, and sika deer, red deer and cattle score about the same. This view is blurred to match.']`
  Log: L100 (4 to 6 cycles per degree, behavioural); L142 (white-tailed and red deer under 6); L103 (sika deer, about 4.8); L135 (sheep, Landolt scores); L151 (cattle, 2.6 to 5); L123. L147 (sheep up to 14) disagrees and is unresolved.
- `['m', 'Sharpest band', 'The green-sensing cones of a deer crowd into a band across its retina that looks out along the horizon. A deer sees most sharply across the ground ahead and to its sides, and this view keeps that band sharp.']`
  Log: L97; L143 (in medium and large deer the dense cones extend toward the zone that looks ahead and down); L108.
- `['g', 'Pupil', 'A white-tailed deer's pupil is a horizontal slit. In grazing animals a slit like this widens the view along the ground and cuts the glare from the sky. It also smears out-of-focus things sideways, and this view does the same.']`
  Log: L116 (white-tailed deer); L113 (reindeer); L109 (the functions, from a summary of Banks and colleagues 2015).
- `['g', 'Level eyes', 'When a grazing animal lowers its head to feed, its eyes roll in their sockets by 50 degrees or more to keep the slit pupils level with the ground. This view keeps its sideways smear level with the real horizon however you tilt your phone.']`
  Log: L109.
- `['m', 'Night eyes', 'Behind a deer's retina lies a mirror-like layer, the tapetum, which sends light back through the retina for a second chance to be caught. With its pupil wide open, a deer's eye gathers light as well as a fast camera lens. This view brightens the shadows in dim light and adds a soft glow.']`
  Log: L98, L99 (f/1.4 at a 12 mm pupil); L112. The glow is *invented*.
- `['m', 'Seasons in the eye', 'A reindeer's tapetum changes colour with the seasons, from gold in summer to deep blue in winter. The blue layer makes the eye more sensitive in the long Arctic twilight at some cost to sharpness. White-tailed deer in the northern United States have bluer tapeta than deer in Georgia.']`
  Log: L112, L114, L115.
- `['g', 'Ultraviolet', 'The lenses of deer, cattle and sheep let through a sixth to a quarter of the ultraviolet light that reaches them, and white-tailed deer respond to some ultraviolet in tests. A faint violet tint in this view stands in for it, and the tint is the app's own choice.']`
  Log: L25 to L28; L101; L34, L107 (reindeer retinas respond to ultraviolet). L122 records the contrary claim of the present source, which gives no evidence.
- `['i', 'Field of view', 'This view assumes that a deer takes in about 310 degrees around itself, the figure a natural-history book gives. The view bends the picture at its edges to suggest it.']`
  Log: L121.
- `['g', 'Speed', 'Recordings from white-tailed deer retinas, which have yet to be published in full, suggest that deer follow a flickering light about as fast as any mammal measured, which would be one and a half to two times as fast as a person. This view runs slowly and then jumps ahead to suggest it.']`
  Log: L141 (stated in a review, no number); L5, L9, L10 (the fastest mammals in the compilations, 100 to 120 Hz). The factor is the sheet's inference.
- `['i', 'Depth', 'This view treats things lower in the picture as closer, which is a guess.']`
  Log: none.
- `['x', 'Hearing', 'Cattle can tell which way a brief sound came from only to within about 30 degrees, and goats to within 18, where people manage under a degree. Their band of sharp sight already covers most of the horizon, so a rough direction is enough to bring a sound into view. This view leaves sound out.']`
  Log: L138.

**The picture**

| Field | Value | Behind it |
|---|---|---|
| `fov` | 310 | L121 (secondary: a natural-history book) |
| `cpd` | 5 | L100, L103, L135 |
| `topoS` | 1 | L97 |
| `fall` | 2.2 | *invented* |
| `topoA` with new `spotY` | 0.3, placed 15% below centre | L143 (frontal and lower field in medium and large deer), L108; place and weight *invented* |
| `pupil` | 'h' | L116, L113 |
| new `levelPupil` | 1 (the smear axis follows gravity) | L109 |
| new `pupilDim` | in dim scenes the smear turns round | L113 (reindeer: a horizontal bar when constricted, round when dilated) |
| `dof` | 22 | *invented* |
| `M` | mix w = 0.23 (deer); w = 0.77 (cattle, bison, sheep, goats, antelope) | L118, L96; rule *invented* |
| `gain` | 1.5 | L98, L99; value *invented* |
| new `tapetum` | dim-light glow tinted gold (south) or blue (north, and reindeer in winter) | L98, L112, L115; tint and strength *invented* |
| `sheen` | 0.3 | L25 to L28, L101, L107; the tint is *invented* |
| `sat` | 0.85 | *invented* |
| `rate` | 0.6 | L141 (qualitative), with the fastest mammals at 100 to 120 Hz (L5, L9, L10) against 55 to 60 for people; value *invented* |
| `cpd` override | cattle, bison and buffalo 4 | L151 (2.6 to 5) |
| `skyBand` (roe deer only) | upper 30% of the frame through the blue channel | L144; the share is *invented* |

**New effects**

- **A level smear.** The out-of-focus smear runs along a direction the shader reads from the phone's gravity vector, so when the phone rolls, the smear stays horizontal in the world. A person who tilts the phone sees the blur refuse to tilt with it, which is exactly what a grazing animal's rolling eye does. Low cost: one rotation of the blur kernel per frame.
- **A pupil that rounds in the dark.** The smear's shape blends from a horizontal bar toward a circle as the scene darkens, using the camera's exposure or the frame's mean brightness. Low cost.
- **Tapetum glow.** In dim scenes the view lifts shadows, adds a soft halo around lights, softens detail a little and tints the lift toward the tapetum's colour. The tint can follow the phone's time zone (northern and southern deer) and, for reindeer, the month. Medium cost (one extra blur pass at low resolution). It is the deer's most beautiful true feature.

### 2.5 `horse` (new): horses, zebras, asses, giraffes, camels and llamas

Chip: "Horse, zebra, giraffe, camel". Who: "a horse". Cue: "A narrow band along the horizon is sharp. Straight ahead and above there is a blind patch."

**Rows**

- `['m', 'Sharpness', 'In daylight a horse sees about a third as much detail as a person does, and the best horses tested came close to a person. Away from a narrow band level with the horizon, its sharpness falls to about a twentieth of a person's. This view keeps a narrow band sharp and blurs the rest.']`
  Log: L150 (average about 20/30, best 23.3 cycles per degree, behavioural, through a review); L155; L92 (16.5 in the streak, 2.7 in the periphery, anatomical); L94; L111.
- `['m', 'Colour', 'Horses have two kinds of colour-sensing cells, most sensitive to blue and to green, where people have three. Reds and greens are hard for a horse to tell apart, and this view mixes colours the same way.']`
  Log: L90, L91 (428 and 539 nm).
- `['m', 'Blind spot ahead', 'A horse's two eyes overlap by 65 to 80 degrees below and along its nose, and a blind area sits right in front of its forehead. A horse lifts its nose to look at something far away with both eyes. This view darkens a patch straight ahead and above, and sharpens the overlap below it.']`
  Log: L93, L148, L149. The size of the patch is *invented*.
- `['m', 'Field of view', 'A horse sees almost all the way around itself. Its only blind areas lie behind its head and right in front of its forehead. This view bends the picture at its edges to suggest the wide sweep.']`
  Log: L149.
- `['m', 'Dim light', 'A horse can still tell colours apart in light as dim as moonlight, about as dim as a person can manage, and it can tell shapes apart on a dark, moonless night. In the horse's sharp band, rods, the cells for dim light, outnumber cones. This view lifts the shadows in dim light.']`
  Log: L110, L153, L111.
- `['m', 'No ultraviolet', 'A horse's large lens blocks nearly all ultraviolet light and lets through less than a twentieth of it. This view adds no ultraviolet tint.']`
  Log: L31.
- `['m', 'Pupil', 'In daylight a horse's pupil narrows to a horizontal oval, and in the dark it opens to a near-circle about 30 millimetres across, seven times the area. The oval smears out-of-focus things sideways. This view does the same in bright light, keeps the smear level with the real horizon, and rounds it in the dark.']`
  Log: L152; L109 (level eyes in grazing animals).
- `['m', 'Giraffes and camels', 'A giraffe's retina could resolve nearly half the detail a person sees, and an arch of extra cells sharpens its view of the ground far below its head. Camels and alpacas see about a sixth to a fifth as much as a person does. When the app knows the species, this view sets its sharpness to match.']`
  Log: L104, L105, L106.
- `['i', 'Speed', 'Little has been published on how fast a horse's eye follows flicker, so this view keeps your pace. That part is a guess.']`
  Log: L154.
- `['x', 'Hearing', 'Horses, like cattle and rabbits, judge the direction of a sound only roughly. Their wide band of sharp sight takes in the source without precise aim. This view leaves sound out.']`
  Log: L40, L138.

**The picture**

| Field | Value | Behind it |
|---|---|---|
| `fov` | 350 | L149 (near-complete; blind only behind and in front of the forehead); the number is *invented* |
| `cpd` | 20; giraffes 25; dromedary and Bactrian camels 10; llamas, alpacas, guanaco and vicuña 13 | L150 (about 20/30 on average, best 23.3), L92; L104; L105; L106 |
| `topoS` | 1 | L92, L94 |
| `fall` | 2.8 | L92 (a six-fold fall, 16.5 to 2.7); the curve is *invented* |
| new `blind` | a soft dark patch centred 20% above the middle, a fifth of the frame wide | L93 for its place; size *invented* |
| `topoA` with new `spotY` | 0.4, 20% below centre (the overlap down the nose) | L93 |
| new `binoc` | 70 degrees, centred below the middle | L148 (65 to 80), L93 |
| `pupil`, `levelPupil`, `pupilDim` | 'h', 1, 1 | L152 (oval in daylight, near-round when dilated), L109 |
| `dof` | 18 | *invented* |
| `M` | mix w = 0.30 | L91; rule *invented* |
| `gain` | 1.5 | L110, L153, L111; value *invented* |
| `sheen`, `uvBlue` | 0, 0 | L31 |
| `rate` | 1 | *invented*; L154 (not measured) |

Giraffe profile: a temporal sharp area ahead (25 to 27) on top of the streak, and a sharper lower field from the dorsal arch (L104). Camel profile: two sharp spots, one ahead and one behind, with a much blurrier middle (2 to 3) and no continuous streak (L105).

**New effects**

- **A blind patch.** A soft vignette straight ahead and above, and a sharper zone below it. A person who points the phone at something far away sees it vanish into the patch until they tip the phone down, the way a horse lifts its nose. Low cost (one mask).
- **Per-family sharpness and topography** for giraffes and camels: data, plus a second sharp spot for camels.

## 3. The existing views checked

Each current value of `src/cam.a.js` (build 22) against `docs/SOURCES.md` and the primary literature.

### `squirrel`

| Item | Now | Verdict |
|---|---|---|
| Row 'Colour' (g) | "Ground squirrels have two kinds of colour-sensing cells..." | **Confirmed, and now measured in the commonest member.** The source, Jacobs, Neitz and Crognale (1985), gives 436.7 and 517 to 519 nm in two ground squirrels (L126, L127). The grey squirrel itself has 444 and 543 nm (L128, L129) and is a behavioural dichromat (L131). Regrade m and name grey squirrels. |
| Row 'Speed' (g) | "A ground squirrel can see a light flicker on and off up to 108 times a second..." | **Corrected.** 108 Hz is Inger and colleagues' mean across daylight levels for the golden-mantled ground squirrel, measured by electroretinogram (L5); Healy and colleagues give 120 for the same animal from the same source (L9). The one tree squirrel measured reaches 60 to 65 (L7, L11), and the grey squirrel is the view's commonest member. The row should say that the figure is for ground squirrels and chipmunks and that tree squirrels are close to people. |
| Row 'Field of view and sharpness' (i) | a guess | **Partly superseded.** Sharpness remains a guess (L125 gives only upper limits). Where the sharpness lies is measured: a broad horizontal streak (L44, L45, L124, L39). Field of view remains unmeasured. |
| `fov` 270 | guess | Unsupported. Proposed 300 on the rat's 295 (L70), still *invented*. |
| `cpd` 6 | guess | **Probably too sharp.** A later paper groups grey and ground squirrels with the tree shrew (1.2 to 2.4) for low spatial resolution (L160, L161), below the anatomical limits of about 7 to 14 (L125). Proposed 4, still *invented*; the measurement (Jacobs, Birch and Blakeslee 1982) is priority 1 on the wanted list. |
| `topoS` 1, `fall` 1.0 | guesses | **Confirmed in form** (L44, L45, L124); proposed `fall` 0.8 and a band width (`streakW`). |
| `pupil` 'o', `dof` 4 | guesses | Unsupported; kept as *invented*. |
| `M` PROTAN | "Vienot, Brettel & Mollon 1999, from memory" | **Confirmed for ground squirrels** (long-wave cone at 517 to 519 nm, shorter than a person's green cone, L127). **Corrected for tree squirrels**, whose cone at 543 nm lies between a person's green and red cones (L129): proposed mix w = 0.43. The matrices themselves are still unchecked. |
| `rate` 0.56 | 60 / 108 | **Corrected**: right for ground squirrels and chipmunks, wrong for tree squirrels (L7, L11). Proposed 1 for tree squirrels and 0.5 for ground squirrels and chipmunks. |
| Missing | | The yellow lens (L15 to L17, L33, L46) is the squirrel's most visible measured trait and the view does not show it. |

### `deer`

| Item | Now | Verdict |
|---|---|---|
| Row 'Colour' (m) | "White-tailed deer have two kinds of colour-sensing cells... Reds and oranges look yellow or grey to them." | **First sentence confirmed** from the primary paper (L117, L118: 450 to 460 and 537 nm; fallow deer 542, L119). **Second sentence unsupported**: no source read tests how reds look to a deer, and with a long-wave cone at 537 nm reds should look dark more than yellow. Rewritten in section 2.4. |
| Row 'Field of view' (m) | "about 310 degrees" | **Downgraded.** The source page quotes a natural-history book, Heffelfinger (2006), with no measurement behind it (L121). Regrade i; the measurement is wanted (Hughes 1977). |
| Row 'Pupil' (g) | "...widens their view along the ground and cuts glare from the sky..." | **Confirmed.** The shape is measured in white-tailed deer (L116) and reindeer (L113). The "glare" clause that `docs/SOURCES.md` lists as unbacked is backed by the summary of Banks and colleagues (L109: horizontal pupils limit the dazzling light from above); it stays g because the paper itself did not open. |
| Row 'Sharpness, dim light and depth' (i) | guesses | **Superseded for sharpness** (L100, L103: about 5 cycles per degree) and partly for dim light (L98, L99). Depth stays a guess. |
| `fov` 310 | secondary | Kept, graded g (L121). |
| `cpd` 8 | guess | **Corrected to 5** (L100, L103, L135, L123). |
| `topoS` 1, `fall` 2.2 | guesses | `topoS` **confirmed** (L97); `fall` unsupported, kept *invented*. |
| `pupil` 'h' | Banks 2015 | **Confirmed** in white-tailed deer (L116). |
| `dof` 22 | guess | Unsupported, kept *invented*. |
| `M` DEUTAN | from memory | **Corrected for deer**: the 537 nm cone is nearer a person's green cone (proposed w = 0.23). **Confirmed for cattle, sheep and goats** (552 to 555 nm, w about 0.77). |
| `gain` 1.5 | guess | Supported in direction (L98 tapetum, L99 f/1.4); value *invented*. |
| `sat` 0.85 | guess | Unsupported, *invented*. |
| Source page (Wildlife Online) | | Also states that deer "cannot see light in the ultraviolet spectrum" with no source (L122). Behaviour (L101), lens transmission (L25, L26) and reindeer electroretinograms (L107) contradict it. The page should not be used for that claim. |

### `rabbit`

| Item | Now | Verdict |
|---|---|---|
| Row 'The whole view' (i) | "...almost all the way around itself, most sharply along the horizon, in little detail, with two kinds of colour-sensing cells." | **Confirmed in every part except detail**: the full circle (L74), the streak (L75, L38, L40, L1) and two cone types (L79, L80). "In little detail" stays a guess until Vaney (1980) is read. Replaced by the rows in section 2.3. |
| `fov` 350 | guess | **Corrected to 360** (L74), with a 24-degree overlap in front (L73). |
| `cpd` 3 | guess | Unsupported; kept *invented*; wanted. |
| `topoS` 1, `fall` 2.0 | guesses | `topoS` **confirmed** (L75); a tenfold fall in ganglion cells below the band (L75) supports a steep fall; value *invented*. |
| `pupil` 'o', `dof` 6 | guesses | Unsupported; kept *invented*. |
| `M` DEUTAN | from memory | **Corrected to PROTAN**: the rabbit's long-wave cone peaks at 523 nm (L80), shorter than a person's green cone. |
| `docs/SOURCES.md` | "The rabbit's field, streak and cones" listed as entered from memory | All three now have primary sources: L74, L75, L79 to L80. |

## 4. Species with their own measurements

Each could get its own profile when the full database names it. Values a profile would change are in bold.

- **Eastern grey squirrel** (*Sciurus carolinensis*; 300,608 world records, 1,010 in Alachua): cones at **444 and 543 nm**, rods at 502 (L128 to L130); rods to cones about 2 to 3 (L130); colourless point near 500 nm (L131); **lens 50% at 441 nm, no ultraviolet A** (L15); finds caches by sight more than smell (L56).
- **Eastern fox squirrel** (*S. niger*; 125,998; 44 in Alachua): cone mechanisms at 450 and 540 nm, dichromatic, shift toward rods in the dark (L47 to L49); localizes sound to 14.7 degrees (L41).
- **American red squirrel** (*Tamiasciurus hudsonicus*; 75,044): **flicker to 60 to 65 Hz** (L7, L11).
- **Golden-mantled ground squirrel** and **yellow-pine chipmunk** (*Callospermophilus lateralis*, *Neotamias amoenus*): **flicker to 100 to 120 Hz** (L5, L6, L9, L10).
- **California and thirteen-lined ground squirrels** (*Otospermophilus beecheyi*, 48,233; *Ictidomys tridecemlineatus*): cones at **437 and 517 to 519 nm** (L126, L127); broad streak (L44, L45, L124); lens absorbs everything below 410 nm (L46).
- **Eastern chipmunk** (*Tamias striatus*; 80,057): best vision **155 degrees** wide (L39). **Prairie dog** (*Cynomys ludovicianus*): 116 degrees (L37), no ultraviolet A through the lens (L16). **Groundhog** (*Marmota monax*; 45,482): 90.5 degrees (L36).
- **Southern flying squirrel** (*Glaucomys volans*; 23 in Alachua): rods at 500 nm, photopic mechanism near 520, **rod process slower than 10 to 15 Hz** (L132, L133); **clear lens, 29% of ultraviolet A** (L18).
- **House mouse** (*Mus musculus*): **ultraviolet cone 359 to 360 nm, green 508 to 511** (L68, L69, L82, L83); **0.5 cycles per degree** (L157, L67); lens passes 81% of ultraviolet A (L19); hears 2.3 to 90 kHz (L137).
- **Brown rat** (*Rattus norvegicus*; 19,431) and **black rat** (*R. rattus*; 8,944): ultraviolet 362, green 502 nm (L84, L85); **about 1 cycle per degree**, wild rats included (L158, L159, L3, L64, L89); field 295 degrees with binocular overlap overhead (L70, L71); flicker 25 to 39 Hz in albino rats (L8, L13); whisking 8 Hz (L140); lenses pass 56 to 81% of ultraviolet A (L20, L21).
- **Deer mouse** (*Peromyscus maniculatus*): rod-dominated, ultraviolet-type S cones (L72).
- **European beaver** (*Castor fiber*; 21,412): retinal resolution about 17 arcmin in air (L59).
- **Guinea pig** (*Cavia porcellus*), as the measured cavy: cones at **429 and 529 nm** (not ultraviolet), colourless point 480 nm (L60 to L62); flicker 50 Hz (L12); lens passes 35% of ultraviolet A (L22).
- **Degu** (*Octodon degus*): ultraviolet cone 360 nm, green 500 (L57, L58); binocular overlap 50 degrees (L65).
- **European rabbit** (*Oryctolagus cuniculus*; 38,839): cones at **425 and 523 nm**, rods 498 (L79 to L81); full circle with **24 degrees** of overlap (L73, L74); streak with a tenfold fall (L75); **blue-only strip of retina** (L76); hears to 49 kHz, localizes to 16.8 degrees (L136, L139).
- **White-tailed deer** (*Odocoileus virginianus*; 310,997; 799 in Alachua): cones at **450 to 460 and 537 nm**, rods 497 (L117, L118, L120); **4 to 6 cycles per degree** (L100); green cones in a horizontal streak (L97); tapetum over the upper eye (L98), **golden in Georgia, bluer in the north** (L115); f/1.4 to 5.6 (L99); slit pupil (L116); some ultraviolet sensitivity (L101).
- **Reindeer** (*Rangifer tarandus*): lens passes 26.5% of ultraviolet A (L25) and the retina responds to 372 nm (L34, L107); **tapetum gold in summer (541 nm), deep blue in winter (444 nm)** (L112, L114); pupil 25 mm² and horizontal when constricted, 336 mm² and round when dilated (L113).
- **Fallow deer** (*Dama dama*): green cone at 542 nm (L119). **Sika deer** (*Cervus nippon*): about 4.8 cycles per degree (L103). **Red deer** (*Cervus elaphus*): under 6 (L142). **Roe deer** (*Capreolus capreolus*; 58,711): **S cones concentrated in the ventral retina**, which views the sky (L144), so it gets the sky band.
- **Cattle, goats and sheep**: S cones 444 to 455 nm, long-wave cones **552 to 555** (L95, L96); lenses pass 22% (cattle) and 15% (sheep) of ultraviolet A (L27, L28); **cattle 2.6 to 5 cycles per degree** (L151); sheep acuity scores 0.085 to 0.19 (L135) against a stated 14 (L147); cattle localize sound to 30 degrees, goats 18 (L138).
- **Horse** (*Equus caballus*; 11,576 research-grade and 18,869 casual; 236 in Alachua): cones at **428 and 539 nm** (L90, L91); **about 20 cycles per degree behaviourally, best 23.3** (L150, L155), 16.5 in the streak and 2.7 elsewhere by anatomy (L92); peak of 4,000 ganglion cells per mm² (L94); colour to 0.02 cd/m² and shapes below 6.81 × 10⁻⁵ cd/m² (L110, L153); rods dominate the streak (L111); **65 to 80 degrees of overlap** down the nose and blind areas only behind the head and before the forehead (L93, L148, L149); pupil an oval in daylight and a near-circle of about 30 mm in the dark (L152); lens passes 4.6% of ultraviolet A (L31). Plains zebras (17,579 records) take the horse's values, as Melin and colleagues assume (L155).
- **Giraffe** (*Giraffa*; about 19,000): **25 to 27 cycles per degree**, horizontal streak, temporal area and dorsal arch (L104). **Dromedary camel**: **9.5 to 10**, two separate sharp areas (L105). **Alpaca**: **12.5 to 13.4** (L106), lens passes 6% of ultraviolet A (L30).

## 5. Gaps and how to fill them

- **Tree squirrel sharpness.** Jacobs, Birch and Blakeslee (1982) measured it and did not open (wanted, priority 1). A later paper places grey and ground squirrels with the tree shrew, which resolves 1.2 to 2.4 cycles per degree, as animals of low spatial and high temporal resolution (L160, L161). The cone spacing of the thirteen-lined ground squirrel (L124) and the ganglion-cell density of the California ground squirrel (L44) give upper limits of about 14 and 7 (L125, the sheet's arithmetic at a 5 mm focal length). The view uses 4 (*invented*) between the two.
- **Squirrel field of view.** Nothing measured. The rat's 295 degrees (L70) is the nearest rodent measurement; the chipmunk's 155-degree band of best vision (L39) shows how much of the panorama is sharp.
- **Squirrel, rodent and rabbit pupils.** Not in any source read. Round pupils are assumed (*invented*).
- **Rabbit sharpness.** Van Hof (1967) and Vaney (1980) measured it behaviourally (wanted). The ganglion-cell peak of 5,400 per mm² (L75) could give an anatomical estimate once the rabbit eye's focal length is known; no focal length was read in this session.
- **Flicker in deer, horses, cattle and rabbits.** No number was found in the collection or the two compilations (L5 to L13 come from rodents and other animals only). For white-tailed deer a review reports unpublished electroretinograms placing deer among the fastest mammals (L141), so the deer view runs slow and jumps (rate 0.6, graded g). For horses a review finds little published (L154). Healy and colleagues (2013) fit flicker rates across 34 vertebrates to body mass, mass-specific metabolic rate and light level; their model could give estimates for horses and rabbits once metabolic rates for these species are sourced. Until then the horse and rabbit views keep a person's pace, graded i.
- **Deer and horse fields of view.** The horse's field is near-complete with 65 to 80 degrees of overlap (L148, L149), with no total in degrees. Hughes (1977) holds the classic measurements (wanted). The deer's 310 degrees comes only from a book (L121).
- **Horse behavioural acuity.** Now known through two reviews (L150, L155): about 20/30 on average and 23.3 cycles per degree at best. Timney and Keil (1992) itself remains wanted to confirm the conditions.
- **Cattle and bison acuity.** A review gives cattle 2.6 to 5 cycles per degree (L151), which settles their place with deer. Bison (12.8% of Alachua's records for this group) are unmeasured and take the cattle value. **Sheep** remain unsettled between the Landolt scores (L135) and a stated 14 (L147); the paper behind the review's figure, probably Sugnaseelan and colleagues (2013), is wanted.
- **Beavers, muskrats, coypu, porcupines, capybaras and agoutis.** Half of the `mouse` view's world records and nothing measured except the beaver's anatomy (L59). The agouti's lens (15% of ultraviolet A, L23) and the guinea pig's non-ultraviolet S cone at 429 nm (L60) warn that the ultraviolet row may be false for cavies and agoutis. The view's ultraviolet tint should be turned off for Caviidae, Dasyproctidae and Cuniculidae (*invented* choice on L60 and L23).
- **Overhead binocular vision in rats.** Measured in anaesthetized albino rats (L70, L71); how a moving rat uses it is in Wallace and colleagues (2013) (wanted).
- **Pikas and zebras.** Nothing measured here; they ride on rabbits and horses.
- **Hearing in deer and horses.** Only cattle and goats (L138) and a general statement about horses (L40). Horse hearing (Heffner and Heffner 1984, cited in L139's paper) was not opened.
- **Smell.** Every animal in this unit relies heavily on smell, and no source on it was read; no row claims anything about smell.

## 6. Closed sources wanted

The same list as `docs/views/wanted/squirrel-deer-rabbit.jsonl`, most useful first (priority 1 would change a view's picture, 2 would confirm or correct a row, 3 is background).

1. (priority 1) Jacobs GH, Birch DG, Blakeslee B (1982), *Visual acuity and spatial contrast sensitivity in tree squirrels*, Behavioural Processes 7: 367-375. doi:10.1016/0376-6357(82)90008-0. The only behavioural acuity for tree squirrels, which a later paper describes as low and similar to the tree shrew's 1.2 to 2.4 cycles per degree; would replace the squirrel view's guessed 4.
2. (priority 1) Vaney DI (1980), *The grating acuity of the wild European rabbit*, Vision Research. doi:10.1016/0042-6989(80)90146-7. Behavioural acuity for the wild rabbit; would replace the rabbit view's guessed 3 cycles per degree.
3. (priority 1) Hughes A (1977), *The topography of vision in mammals of contrasting life style: comparative optics and retinal organisation*, Handbook of Sensory Physiology, Vol. 7 (Crescitelli F, ed.), pp. 613-756, Springer-Verlag. no DOI seen. Classic measurements of visual fields and streaks in rabbits, ungulates and rodents; would replace the deer's book-sourced 310 degrees and the squirrel's guessed field. Citation read in the reference list of Caves et al. 2018 (reference 10); no DOI seen.
4. (priority 1) Wallace DJ, Greenberg DS, Sawinski J, Rulla S, Notaro G, Kerr JN (2013), *Rats maintain an overhead binocular field at the expense of constant fusion*, Nature. doi:10.1038/nature12153. How freely moving rats use their overhead binocular field; decides how the mouse view draws the overlap above.
5. (priority 2) Timney B, Keil K (1992), *Visual acuity in the horse*, Vision Research. doi:10.1016/0042-6989(92)90092-w. The original of the horse acuity now read through two reviews (about 20/30 on average, best 23.3 cycles per degree); would confirm the conditions behind the horse view's sharpness.
6. (priority 2) Entsu S, Dohi H, Yamada A (1992), *Visual acuity of cattle determined by the method of discrimination learning*, Applied Animal Behaviour Science. doi:10.1016/s0168-1591(05)80052-8. The primary cattle acuity behind a review's 2.6 to 5 cycles per degree; would confirm that cattle and bison belong with deer.
7. (priority 2) Van Hof MW (1967), *Visual acuity in the rabbit*, Vision Research 7: 749-751. doi:10.1016/0042-6989(67)90037-5. A second behavioural rabbit acuity to set beside Vaney 1980.
8. (priority 2) Tansley K, Copenhaver RM, Gunkel RD (1961), *Some aspects of the electroretinographic response of the American red squirrel, Tamiasciurus hudsonicus loquax*, J Cell Compar Physl 57: 11-19 (abbreviation as given in the citing paper). no DOI seen. The original of every squirrel flicker value used (L5 to L11) and of the tree-against-ground difference that sets the squirrel view's pace. Citation read in the reference list of Inger et al. 2014 (reference 75); no DOI seen.
9. (priority 2) Harman AM, Moore S, Hoskins R, Keller P (1999), *Horse vision and an explanation for the visual behaviour originally explained by the 'ramp retina'*, Equine Veterinary Journal. doi:10.1111/j.2042-3306.1999.tb03837.x. The horse's binocular overlap and blind area in degrees, for the horse view's blind patch.
10. (priority 2) Hebel R (1976), *Distribution of retinal ganglion cells in five mammalian species (pig, sheep, ox, horse, dog)*, Anatomy and Embryology. doi:10.1007/bf00346285. Ganglion-cell maps for ox, sheep and horse; gives the streak shape and an anatomical acuity for cattle.
11. (priority 2) Veilleux CC, Kirk EC (2014), *Visual acuity in mammals: effects of eye size and ecology*, Brain, Behavior and Evolution 83: 43-53. http://refhub.elsevier.com/S0169-5347(18)30052-1/sbref0075. A compilation of mammal acuities that probably holds values for squirrels, rabbits and several hoofed animals. Citation read in the reference list of Caves et al. 2018 (reference 15); no DOI seen.
12. (priority 2) Van Hooser SD, Nelson SB (2006), *The squirrel as a rodent model of the human visual system*, Visual Neuroscience. doi:10.1017/s0952523806230098. Review of squirrel acuity, visual field and timing; may settle the squirrel view's field and sharpness.
13. (priority 2) Banks MS, et al. (2015), *Why do animal eyes have pupils of different shapes?*, Science Advances 1(7): e1500391. doi:10.1126/sciadv.1500391. Open access but did not load in this session; read directly it would move the pupil and level-eyes rows from g to m and give the rotation range.
14. (priority 2) D'Angelo GJ, Glasser A, Wendt M, Williams GA, Osborn DA, Gallagher GR, Warren RJ, Miller KV, Pardue MT (2008), *Visual specialization of an herbivore prey species, the white-tailed deer*, Canadian Journal of Zoology. doi:10.1139/z08-050. Cone densities and eye dimensions for an anatomical acuity of the white-tailed deer and the exact shape of its streak.
15. (priority 2) Jacobs GH, Neitz J, Deegan JF (1991), *Retinal receptors in rodents maximally sensitive to ultraviolet light*, Nature 353: 655-656. doi:10.1038/353655a0. Which rodents have ultraviolet cones; decides which mouse-view members keep the ultraviolet tint.
16. (priority 2) Sugnaseelan S, Prescott NB, Broom DM, Wathes CM, Phillips CJC (2013), *Visual discrimination learning and spatial acuity in sheep*, Applied Animal Behaviour Science. doi:10.1016/j.applanim.2013.04.012. Probably the source of a review's 'up to 14 cycles per degree' for sheep, against Landolt scores of about 2.6 to 5.7; decides whether sheep stay with the deer view.
17. (priority 3) Jacobs GH (1978), *Spectral sensitivity and colour vision in the ground-dwelling sciurids: results from golden mantled ground squirrels and comparisons for five species*, Animal Behaviour. doi:10.1016/0003-3472(78)90058-1. Behavioural colour vision in five ground squirrels; would confirm the ground squirrel colour setting.
18. (priority 3) Jacobs GH, Deegan JF, Neitz J (1998), *Photopigment basis for dichromatic color vision in cows, goats, and sheep*, Visual Neuroscience. doi:10.1017/s0952523898153154. Per-species cone peaks for cattle, goats and sheep (the abstract gives ranges).
19. (priority 3) Collewijn H (1970), *The normal range of horizontal eye movements in the rabbit*, Experimental Neurology. doi:10.1016/0014-4886(70)90168-8. How far a rabbit's eyes move; sets the forward-look vergence effect.
20. (priority 3) Akaishi Y, Uchiyama H, Ito H, Shimizu Y (1995), *A morphological study of the retinal ganglion cells of the Afghan pika (Ochotona rufescens)*, Neuroscience Research. doi:10.1016/0168-0102(94)00873-e. The only pika retina in the collection; tests whether pikas fit the rabbit view.
21. (priority 3) Mass AM, Supin AYa (2017), *Estimates of underwater and aerial visual acuity in the European beaver Castor fiber L. based on morphological data*, Doklady Biological Sciences. doi:10.1134/s0012496617020065. Whether the beaver's 17 arcmin is a cycle or a stripe, which doubles or halves its sharpness.

## 7. Sources

Opened in this session unless marked **secondary**.

- Arbogast, Glösmann and Peichl 2013, PLoS ONE, doi:10.1371/journal.pone.0080910. **opened** (full text).
- Amann and colleagues 2012, J Anim Physiol Anim Nutr, doi:10.1111/jpn.12016. **opened** (abstract).
- Baldwin (Wildlife Online) 2018, *Deer overview: senses, vision*, https://www.wildlifeonline.me.uk/animals/article/deer-overview-senses-vision. **secondary** for Heffelfinger 2006 and a 2015 television programme; **opened**.
- Banks and colleagues 2015, Science Advances, doi:10.1126/sciadv.1500391. **secondary** (sci.news summary, https://www.sci.news/biology/science-pupils-shape-eyes-animals-03112.html).
- Blakeslee, Jacobs and Neitz 1988, J Comp Physiol A 162: 773 to 780, doi:10.1007/BF00610966. **opened** (abstract, Springer).
- Brown 1936, J Gen Psychol, doi:10.1080/00221309.1936.9713140. **opened** (abstract).
- Carroll and colleagues 2001, Journal of Vision 1(2): 2, doi:10.1167/1.2.2. **opened** (abstract).
- Caves, Brandley and Johnsen 2018, Trends Ecol Evol 33(5), doi:10.1016/j.tree.2018.03.001. **opened** (owner's library, main text).
- Chávez and colleagues 2003, IOVS, doi:10.1167/iovs.02-0670. **opened** (abstract).
- Chou and Cullen 1984, Can J Zool, doi:10.1139/z84-120. **opened** (abstract).
- Cohen and colleagues 2014, Wildl Soc Bull, doi:10.1002/wsb.438. **opened** (abstract).
- Coimbra and colleagues 2012, J Comp Neurol, doi:10.1002/cne.23271. **opened** (abstract).
- Crijns and Op de Beeck 2019, Vision 4(1): 4, doi:10.3390/vision4010004. **opened** (abstract).
- Crognale and Jacobs 1991, Visual Neuroscience, doi:10.1017/s0952523800002583. **opened** (abstract).
- D'Angelo and colleagues 2008, Can J Zool, doi:10.1139/z08-050. **opened** (abstract).
- De Franceschi and Solomon 2018, J Physiol, doi:10.1113/jp276964. **opened** (full text); **secondary** for Prusky 2000 and Umino 2008.
- de Farias Rocha and colleagues 2016, PLoS ONE, doi:10.1371/journal.pone.0147318. **opened** (abstract).
- Douglas and Jeffery 2014, Proc R Soc B, doi:10.1098/rspb.2013.2995. **opened** (full text).
- Eigner, Wündsch and von Lützow-Kafka 1984, Ophthalmic Res 16: 48 to 53, doi:10.1159/000265293. **opened** (abstract; year from the Karger page).
- Fosbury and Jeffery 2022, Proc R Soc B, doi:10.1098/rspb.2022.1002. **opened** (full text).
- Gaillard and colleagues 2008, J Comp Neurol, doi:10.1002/cne.21798. **opened** (abstract).
- Guo and Sugita 2000, J Vet Med Sci 62: 1145, doi:10.1292/jvms.62.1145. **opened** (abstract).
- Hands, Sutherland and Bartley 1965, Biochem J 94, doi:10.1042/bj0940279. **opened** (abstract).
- Harman and colleagues 1999, Equine Vet J, doi:10.1111/j.2042-3306.1999.tb03837.x. **opened** (abstract).
- Harman and colleagues 2001, Brain Behav Evol, doi:10.1159/000047258. **opened** (abstract).
- Healy and colleagues 2013, Animal Behaviour, doi:10.1016/j.anbehav.2013.06.018. **opened** (full text); **secondary** for Tansley et al. 1961 and Williams et al. 1985.
- Heffner and Heffner 1992, J Comp Psychol 106(2): 107, doi:10.1037//0735-7036.106.2.107. **opened** (abstract).
- Heffner and Masterton 1980, J Acoust Soc Am, doi:10.1121/1.385213. **opened** (abstract).
- Heffner, Heffner and Koay 2026, J Comp Physiol A, doi:10.1007/s00359-026-01841-1. **opened** (full text).
- Hogg and colleagues 2011, J Exp Biol, doi:10.1242/jeb.053553. **opened** (abstract).
- Hughes and Vaney 1982, J Comp Neurol 204(2), doi:10.1002/cne.902040205. **opened** (abstract).
- Inger and colleagues 2014, PLoS ONE, doi:10.1371/journal.pone.0098631. **opened** (full text and reference list); **secondary** for Tansley et al. 1961 and Williams et al. 1985.
- Jacobs 1974, Brain Behav Evol 10: 307 to 321, doi:10.1159/000124321. **opened** (abstract; year from the Karger page).
- Jacobs and Deegan 1994, Behav Neurosci 108(5), doi:10.1037//0735-7044.108.5.993. **opened** (abstract).
- Jacobs, Deegan and Neitz 1998, Vis Neurosci 15(3), doi:10.1017/s0952523898153154. **opened** (abstract).
- Jacobs and colleagues 1994, J Comp Physiol A 174: 551 to 557, doi:10.1007/BF00217375. **opened** (abstract, Springer).
- Jacobs, Neitz and Crognale 1985, J Comp Physiol A 156: 503 to 509, doi:10.1007/BF00613974. **opened** (abstract, Springer).
- Jacobs, Neitz and Deegan 1991, Nature 353: 655 to 656, doi:10.1038/353655a0. **opened** (abstract page; no species named).
- Jacobs and Silverman 1976, J Comp Physiol 109: 1 to 16, doi:10.1007/BF00663431. **opened** (abstract, Springer).
- Jacobs and Tootell 1977, Can J Zool, doi:10.1139/z77-188. **opened** (abstract).
- Juliusson and colleagues 1994, *Complementary cone fields of the rabbit retina*, PubMed 8125743. **opened** (abstract in the collection index).
- Kopania and Clark 2024, Evolution Letters, doi:10.1093/evlett/qrae072. **opened** (full text).
- Kryger and colleagues 1998, Vis Neurosci 15(4), doi:10.1017/s0952523898154081. **opened** (abstract).
- Lagers-van Haselen, Van Hof and Reuter 1990, *Visual discrimination of discontinuous figures in the rabbit*, Behavioural Brain Research 36: 21 to 25, https://repub.eur.nl/pub/73193/1-s2.0-0166432890901558-main.pdf. **opened** (full text; used only for the citation of Van Hof 1967, since it measures no acuity).
- Land and Nilsson 2012, *Animal Eyes*, 2nd edition, Oxford University Press, ISBN 978-0-19-958114-6. **opened** (owner's library, front matter to p. 63).
- Long and Fisher 1983, J Comp Neurol 221(3), doi:10.1002/cne.902210308. **opened** (abstract).
- Mass and Supin 2017, Doklady Biol Sci, doi:10.1134/s0012496617020065. **opened** (abstract).
- McQuade, Williams and Eichenbaum 1986, Ethology, doi:10.1111/j.1439-0310.1986.tb00602.x. **opened** (abstract).
- Melin, Kline, Hiramatsu and Caro 2016, PLoS ONE, doi:10.1371/journal.pone.0145679. **opened** (full text); **secondary** for the horse's 23.3.
- Mitchinson and Prescott 2013, PLoS Comput Biol, doi:10.1371/journal.pcbi.1003236. **opened** (full text); **secondary** for the whisking rate.
- Morris and colleagues 2025, Journal of Vision 25(13): 8, doi:10.1167/jov.25.13.8. **opened** (full text).
- Nakamura and colleagues 2024, Mammal Study, doi:10.3106/ms2023-0085. **opened** (abstract).
- Neitz and Jacobs 1986, J Comp Psychol 100(1), doi:10.1037//0735-7036.100.1.21. **opened** (abstract).
- Newman, Hammond and D'Angelo 2025, J Exp Zool A, doi:10.1002/jez.70007. **opened** (full text).
- Newman and D'Angelo 2024, *A review of Cervidae visual ecology*, Animals 14(3): 420, doi:10.3390/ani14030420. **opened** (full text); **secondary** for its cited values and for unpublished deer electroretinograms.
- Nuboer, van Nuys and Wortel 1983, J Comp Physiol 151: 347 to 352, doi:10.1007/BF00623909. **opened** (abstract, Springer).
- Petry, Fox and Casagrande 1984, *Spatial contrast sensitivity of the tree shrew*, Vision Research 24(9): 1037 to 1042, https://unifr.ch/med/en/assets/public/professoren/rainerg/Reading list/Spatial.Contrast.Tree.Shrew.Vis.Res.1984.pdf. **opened** (scanned full text); **secondary** for Jacobs and colleagues 1980 and 1982.
- Prusky, West and Douglas 2000, Vision Research 40(16), doi:10.1016/s0042-6989(00)00081-x. **opened** (abstract, Weill Cornell VIVO page).
- Prusky, Harker, Douglas and Whishaw 2002, Behavioural Brain Research 136(2), doi:10.1016/s0166-4328(02)00126-2. **opened** (abstract, Weill Cornell VIVO page).
- Roth, Balkenius and Kelber 2008, PLoS ONE, doi:10.1371/journal.pone.0003711. **opened** (full text).
- Roth and McGreevy 2025, *Horse vision through two lenses*, Frontiers in Veterinary Science, doi:10.3389/fvets.2025.1647911. **opened** (full text); **secondary** for Timney and Keil 1992 and the cattle and camel values.
- Sajdak and colleagues 2016, Visual Neuroscience, doi:10.1017/s0952523815000346. **opened** (full text).
- Stokkan and colleagues 2013, Proc R Soc B, doi:10.1098/rspb.2013.2451. **opened** (full text).
- Sussman, Chou and Lakshminarayanan 2011, J Mod Opt, doi:10.1080/09500340.2010.548608. **opened** (abstract).
- Szél, Röhlich, Caffé and van Veen 1996, Microsc Res Tech 35(6): 445, doi:10.1002/(sici)1097-0029(19961215)35:6<445::aid-jemt4>3.0.co;2-h. **opened** (abstract).
- Tam and colleagues 2016, Proc R Soc B, doi:10.1098/rspb.2016.2275. **opened** (full text); **secondary** for the mouse cone peaks.
- Tamura and colleagues 2015, J Trop Ecol, doi:10.1017/s0266467415000310. **opened** (abstract).
- Tanaka and colleagues 1995, J Ethol 13(1): 69 to 75, doi:10.1007/BF02352565. **opened** (abstract, Springer).
- Van Hooser and Nelson 2006, Visual Neuroscience 23, doi:10.1017/s0952523806230098. **opened** (abstract).
- Vaney 1980, J Comp Neurol 189(2), doi:10.1002/cne.901890202. **opened** (abstract).
- Vega-Zuniga and colleagues 2013, PLoS ONE, doi:10.1371/journal.pone.0084199. **opened** (abstract).
- Wang and colleagues 2013, Vet Ophthalmol, doi:10.1111/vop.12131. **opened** (abstract).
- Watson and colleagues 2022, Am Midl Nat 187(1): 90, doi:10.1674/0003-0031-187.1.90. **opened** (abstract).
- Witzel, Springer and Mollenhauer 1978, Am J Vet Res 39(4): 699, doi:10.2460/ajvr.1978.39.04.699. **opened** (abstract).
- GBIF occurrence API (dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7), Rodentia family facet, read 13 October 2026; GBIF species API for family names. **opened**.
- Repository data: `runs/fetch/10` and `runs/coverage/1-lists` on `ci`; `records-by-group.tsv` on `pub/data-world`; `data/regions/us-fl-alachua/species.json`. **opened**.

## 8. Questions for a specialist

1. What behavioural acuity did Jacobs, Birch and Blakeslee (1982) find for grey squirrels, and does it differ between tree squirrels and ground squirrels?
2. Has any deer's visual field been measured with the ophthalmoscopic reflex method, and how large are the blind area behind a deer and its binocular overlap in front?
3. What flicker rates do the unpublished white-tailed deer electroretinograms show (Newman, in the 2024 review), and are there any for horses, cattle or rabbits?
4. How many degrees above the horizon does the rabbit's blue-only strip of retina cover in a sitting rabbit, and does the mouse's ultraviolet-dominated field begin at the horizon?
5. Were the red squirrel's 60 to 65 Hz and the ground squirrel's 100 to 120 Hz (Tansley and colleagues 1961) recorded under the same light, so that the difference between tree and ground squirrels is real?
6. Do beavers, muskrats, coypu and porcupines have ultraviolet-sensitive cones, as mice and rats do, or violet ones, as the guinea pig does?
