# Sensing sheet: birds (the `hawk`, `wader` and `bird` views, and two new ones), draft

Written 13 October 2026 between 01:46 and about 03:30 UTC. The evidence log is `docs/views/evidence/birds.jsonl` (one measurement a line); every row below names the log lines behind it as "Log: author year (trait, taxon)". The wanted list is `docs/views/wanted/birds.jsonl`.

What was read. The literature collection on `pub/lit-t1` (topics `birds-raptors-owls`, `birds-other` and `methods`): titles and abstracts searched, and about 40 full texts opened on disk. From the owner's Drive: Hart 2001 in full; Caves, Brandley and Johnsen 2018 in full (main text and figures; the supplementary tables were not in the file); Land and Nilsson 2012, *Animal Eyes*, which came through only in part: the front matter, chapters 1 and 2, and chapter 3 to p. 65. Chapter 5 (eyes of land vertebrates, birds included) and chapter 9 (eye movements, head-bobbing in birds on p. 227) were not in the file and are on the wanted list. On the web: the Lund University research portal (abstracts of three Kelber-lab papers), Necker's own copy of his 2007 review, and two news pages.

What could not be reached. From this machine the GBIF and iNaturalist APIs, Europe PMC, PubMed and Crossref refused connections (the egress policy, or HTTP 429 from Europe PMC and Crossref, after which neither was tried again), and the Journal of Experimental Biology and ScienceDirect pages sit behind robot checks. Record shares therefore come from counts already in the repository: GBIF order counts in `docs/views/world-orders.csv`, family facets from `runs/fetch/10` on the `ci` branch (only some family keys resolve to names there), the group totals of the iNaturalist snapshot in `records-by-group.tsv` on `pub/data-world`, and the Alachua species list `data/regions/us-fl-alachua/species.json` (records through 2024).

## 1. Scope

The unit is class Aves. Today `hawk` takes orders Accipitriformes and Falconiformes except the New World vultures, `wader` takes herons, ibises, storks, cranes, limpkins and rails with pigeons, doves and gamebirds, and `bird` takes everything else (`docs/CONTRACTS.md`, `tools/species/eyes.py`).

**What people photograph.** GBIF holds 35,422,868 iNaturalist research-grade bird records in its order facets (11 October 2026). Songbirds (Passeriformes) are 45.4% of them, ducks, geese and swans (Anseriformes) 10.1%, shorebirds and gulls (Charadriiformes) 9.4%, Pelecaniformes 6.6% (herons alone 5.1%), Accipitriformes 6.2% (this figure includes the New World vultures and the osprey, which GBIF files there), pigeons and doves 3.8%, woodpeckers 3.3%, rails and cranes 2.1%, cormorants and anhingas 1.8%, gamebirds 1.5%, hummingbirds and swifts 1.5%, parrots 1.3%, falcons 1.2% and owls 1.0%. The most recorded families in the resolved family facets are ducks (3.58 million), herons (1.82 million), hawks and eagles (1.72 million), pigeons (1.35 million) and crows and jays (1.33 million).

In Alachua County the species list holds 36,462 bird records. The most recorded species in each proposed view are: hawk, red-shouldered hawk 1,192, snail kite 628, osprey 469, bald eagle 230; wader, great blue heron 1,672, great egret 1,066, limpkin 1,055, white ibis 1,015, common gallinule (filed by GBIF as Eurasian moorhen) 1,002, sandhill crane 765, wood stork 634; owl, barred owl 289, great horned owl 80, eastern screech-owl 15; duck, black-bellied whistling-duck 626, blue-winged teal 411, Muscovy duck 318, hooded merganser 199; bird, anhinga 1,331, northern cardinal 968, red-winged blackbird 665, palm warbler 659, boat-tailed grackle 626, double-crested cormorant 527, northern mockingbird 500, turkey vulture 417.

### Where the views should split

| View | Taxa | World records (GBIF orders) | Share | Alachua records | Share |
|---|---|---:|---:|---:|---:|
| `hawk` (kept) | Accipitridae, Pandionidae, Sagittariidae, Falconidae | 2,619,200, less the New World vultures | 7.4% at most | 3,337 | 9.2% |
| `wader` (kept) | Ardeidae, Threskiornithidae, Ciconiidae, Gruidae, Aramidae, Rallidae; Columbiformes; Galliformes | about 4,898,000 | 13.8% | 12,583 | 34.5% |
| `owl` (new) | Strigiformes | 369,548 | 1.0% | 410 | 1.1% |
| `duck` (new) | Anseriformes | 3,591,348 | 10.1% | 2,214 | 6.1% |
| `bird` (kept, smaller) | everything else, with the New World vultures | about 23,945,000 plus the vultures | 67.6% plus | 17,918 | 49.1% |

The iNaturalist snapshot on `pub/data-world` agrees with the first two rows (hawk 2,327,154, which already leaves out the vultures, and wader 4,892,572).

**Owls leave `bird`.** Almost every part of the `bird` picture is false for an owl. An owl's eyes face forward with a binocular overlap of 34 to 54.5 degrees (mean 45.4) and a total field near 200 degrees (Potier et al. 2023), against about 300 degrees for a songbird (zebra finch, Eckmeier et al. 2013). Owls have lost the violet and ultraviolet cone opsin (Wu et al. 2016), carry coloured oil droplets in only about one cone in ten (Hart 2001), see at light levels near the theoretical limit (Martin 1986), and a barn owl resolves 2.6 to 4 cycles per degree (Harmening et al. 2009) where `bird` draws 25. Hearing does much of their work (Martin 1986; Bala et al. 2007; Manley and Köppl 2025).

**Ducks leave `bird`.** Dabbling ducks such as the mallard and the shoveler see around and above the whole head, with a binocular strip 20 to 22 degrees wide running 210 to 220 degrees from the bill over the crown (Guillemain et al. 2002; Cantlay et al. 2023; Martin 2017). Ducks are violet-sensitive (mallard 415 nm) and their eye media block most ultraviolet (half transmission at 370 to 380 nm, Hart 2001), where most songbirds are ultraviolet-sensitive. Ducks do not head-bob (Necker 2007). Grazing geese and swans keep a blind area behind the head (Cantlay et al. 2023), so the `duck` picture follows the dabbling ducks, which make up most of the records (Alachua: whistling-ducks, teal, Muscovy duck, mergansers).

**`hawk` and `wader` stay whole.** Falcons differ from hawks in degree (sharper on average, 47.4 against 24.9 cycles per degree; faster, 102 to 129 Hz against 81 Hz) but share the two foveae and the sideways look (Tucker 2000; Mitkus et al. 2017; Caves et al. 2023; Potier et al. 2020), so they become a setting within `hawk` when the species is known. The Old World vultures in Accipitridae have only the central fovea (Potier et al. 2017) and small binocular fields with large blind areas (Martin et al. 2012), also a setting. Head-bobbing, the shared behaviour behind `wader`, is confirmed in pigeons, chickens, herons with long strides, cranes at slow walking speeds, and coots and moorhens on land and water (Necker 2007; Theunissen and Troje 2017). Ibises and storks are placed among bobbing orders only in Necker's table, which is garbled in the copy read.

**What stays in `bird`, and the settings it needs.** Songbirds are two thirds of the remaining records in Alachua (66.5%) and most of them are ultraviolet-sensitive (Passerida, Vireonidae, parrots and gulls; Ödeen and Håstad 2013; Ödeen et al. 2011), while crows, jays and tyrant flycatchers are violet-sensitive (Ödeen and Håstad 2003). In Alachua 61.7% of `bird` records are in ultraviolet-sensitive families. The picture should therefore carry a colour setting, ultraviolet by default and violet for Corvidae, Tyrannidae and the other suboscines, shorebirds other than gulls and skimmers, and the non-passerine orders other than parrots. The other groups that stay in `bird` (woodpeckers, cormorants and anhingas, hummingbirds, kingfishers, swallows, shorebirds and gulls, New World vultures) differ from songbirds in measured ways (cormorants see poorly under water, White et al. 2007; hummingbirds see 5 to 6 cycles per degree and 70 to 80 Hz, Goller et al. 2019; swallows have two foveae per eye, Tyrrell and Fernández-Juricic 2017; turkey vultures find food by smell, Potier et al. 2018), but the evidence read here does not give any of them a full picture of its own. They are candidates for species profiles (section 4). The anhinga, Alachua's most recorded `bird` species, has no visual measurement in any source read.

## 2. The proposed views

Conventions. "This view squeezes" means the engine's `fov` above 180. "Regions" are the new engine's patches with their own sharpness. A value marked `invented` is the app's own choice. Rates follow the existing convention, 60 divided by the flicker fusion frequency.

### 2.1 `hawk`: hawks, eagles, kites, ospreys, harriers and falcons

Rows:

- `['m', 'Two sharp spots', 'Most hawks, eagles and falcons have two pits of tightly packed cells in each eye, called foveae. The deep one looks out about 45 degrees to the side and the shallow one about 15 degrees. This view puts the deep fovea where your camera points, the way a hawk turns its head to look at something far away.']`
  Log: Tucker 2000 (fovea, Accipitridae and Falconidae); Mitkus et al. 2017 (fovea, Buteo buteo and others); Potier et al. 2016 (fovea, Parabuteo unicinctus); Fite and Rosenfield-Wessels (fovea, Buteo jamaicensis); Ruggeri et al. 2010 (fovea, Buteo platypterus and Buteo brachyurus); Potier et al. 2017 (fovea, Accipitriformes).
- `['m', 'Looking sideways', 'A hawk looks at distant things sideways with one eye and at close things straight ahead with both. Raptors watching something 40 metres or more away kept it in the side view at least 80 percent of the time. When you tap something close, this view turns to face it straight on.']`
  Log: Tucker 2000 (behaviour_vision; eye_movement, head moved every 2 s in hawks and falcons, 5 s in bald eagles).
- `['g', 'Sharpness', 'The sharpest eagles and falcons see about twice as much detail as people do at the centre of the deep fovea. The hawks and kites measured so far average less than half of a person\'s sharpness. This view keeps the foveae as sharp as your camera allows and blurs the rest.']`
  Log: Caves et al. 2018 (acuity_cpd, Aquila audax 138); Caves et al. 2023 (acuity_cpd, Aquila audax 143; Accipitriformes 24.9; Falconiformes 47.4); Land and Nilsson 2012 (acuity_cpd, Aquila 140, against the human fovea 72.9); Fox et al. 1976 (acuity_cpd, a falcon 160, people 60 in the same test).
- `['m', 'Speed', 'A peregrine falcon can see a light flicker up to 129 times a second, a saker falcon 102 times and a Harris\'s hawk 81 times. People stop seeing flicker at 50 to 100 times a second, depending on the size of the light. This view runs at a Harris\'s hawk\'s pace, slowing the picture and then jumping ahead.']`
  Log: Potier et al. 2020 (cff_hz, Falco peregrinus, Falco cherrug, Parabuteo unicinctus); Lund University news (cff_hz, the superseded 77).
- `['m', 'Field of view', 'A red-tailed hawk sees about 280 degrees around itself and a Cooper\'s hawk about 300. The two eyes overlap across about 35 degrees in front. This view squeezes that wider sweep onto the screen and bends its edges.']`
  Log: O'Rourke et al. 2010 (fov_h_deg and binocular_deg, Buteo jamaicensis, Accipiter cooperii, Falco sparverius); Potier et al. 2023 (binocular_deg, diurnal raptors 37.4).
- `['m', 'Steady head', 'A hawk\'s eyes hardly turn in their sockets, so it moves its whole head in quick jumps and holds it still in between. A hunting kestrel keeps its eyes fixed in place over the ground while its body works against the wind. This view holds the picture still against small movements of your phone, then jumps to catch up.']`
  Log: Tucker 2000 (eye_movement, eyes not rotated noticeably); O'Rourke et al. 2010 (eye_movement, Falco sparverius 0.88); Videler et al. 1983 (eye_movement, Falco tinnunculus); Theunissen and Troje 2017 (eye_movement, Aves).
- `['g', 'Colour', 'Hawks and falcons have four kinds of colour-sensing cells, one more than people. The fourth responds to violet light, and hawks make little use of ultraviolet. This view keeps colours close to your camera\'s and adds only a faint violet tint.']`
  Log: Hart 2001 (receptor_classes, Aves); Ödeen and Håstad 2003 (colour_vision, raptors violet type); Lind et al. 2013b (colour_vision, buzzard, sparrowhawk, red kite, kestrel); Mitkus et al. 2017 (fovea, violet and green cones in the central fovea).
- `['m', 'Vole trails', 'Kestrels were once thought to find voles by the ultraviolet glow of their urine. Measurements of raptor eyes and of vole urine show that the glow is too weak to guide them, so this view draws no such trails.']`
  Log: Lind et al. 2013b (colour_vision).
- `['g', 'Shade from the sun', 'Hawks that hunt animals on the ground have a wide blind area above the head, where a bony ridge by the eye keeps out the glare of the sky. This view darkens the top of the picture.']`
  Log: Potier et al. 2018 (binocular_deg, Accipitriformes, ground predators).
- `['x', 'Hearing', 'Hawks hear best between about 1,000 and 6,000 vibrations a second. This view leaves sound out.']`
  Log: Yamazaki et al. 2004 (sense_hearing, Spizaetus nipalensis and Accipiter gentilis).

The picture:

| Field | Value | Behind it |
|---|---|---|
| `fov` | 280 | O'Rourke et al. 2010 (fov_h_deg, red-tailed hawk 278, Cooper's hawk 300) |
| `cpd` | 25 in the deep fovea; falcon setting 47; eagle setting 60 with magnification | Caves et al. 2023 (Accipitriformes 24.9, Falconiformes 47.4); eagle 138 to 143 (Caves et al. 2018, 2023) |
| `fovea` | 1.0 by default; 2.3 in the eagle setting | the eagle setting is 140 / 60 = 2.3; magnifying is the app's way of showing detail a camera cannot record, `invented` |
| regions | deep fovea at the frame centre in the far mode, the same eye's shallow fovea 30 degrees toward the head axis; in the near mode both shallow foveae at ±15 degrees and the binocular centre | Tucker 2000 (fovea; behaviour_vision); the far and near switch is grounded in Tucker's 40 m and 8 m; the switch distance in the app is `invented` |
| `fall` | 1.4 outside the foveae | `invented`; raptor retinas fall away from fovea and streak (Inzunza et al. 1991, fovea) |
| `pupil` | 'o' | unchanged; no source read |
| `M`, `sat` | camera colours, `sat` 1.1 | four cone classes (Hart 2001); the small saturation lift stands for the oil droplets' narrowing of each cone's band (Hart 2001, oil_droplets), its size `invented` |
| `sheen` | 0.3 | violet-sensitive (Ödeen and Håstad 2003); the strength is `invented` |
| `rate` | 0.74 (falcon setting 0.47) | 60 / 81 for the Harris's hawk, 60 / 129 for the peregrine (Potier et al. 2020) |
| top shade | darken the top 15% of the frame | Potier et al. 2018 (ground predators' blind area above the head); the amount is `invented` |

New effects:

1. **Far and near looking.** In the far mode the frame centre is the deep fovea, sharp and full colour, with the head's straight-ahead direction 45 degrees to one side; the shallow fovea of the same eye is a second, softer sharp spot 30 degrees toward that side. In the near mode (a tap on something close, or a depth estimate under about 8 metres) the view turns, with a short swing of the picture, to face the object: the binocular centre is moderately sharp and the two shallow foveae sit at 15 degrees either side. Shader regions plus a tap; easy. A depth estimate would make it automatic at a cost. The beauty is in the turn itself: the person feels the hawk choose between its two ways of looking.
2. **Head jumps and hovering.** Between jumps the picture is held still in the world against the phone's rotation (gyroscope) and small shifts (accelerometer), then it snaps to catch up; for a perched hawk the hold is up to about 2 seconds (Tucker 2000), and a hunting kestrel holds its eyes fixed over the ground (Videler et al. 1983). Medium: device motion needs a permission tap on iOS. Beautiful when the person tries to hold the phone still over a lawn and the picture locks, as a kestrel's does.
3. **Locked pursuit.** When something moves across the frame, the deep fovea's sharp spot follows it at a fixed angle, the goshawk's way of pursuing (Kane et al. 2015). Uses the motion-salience map; medium.

### 2.2 `owl`: owls (new)

Rows:

- `['m', 'Eyes that face forward', 'An owl\'s eyes face forward, so their views overlap across about 45 degrees in front, more than in most birds. Its whole view spans about 200 degrees. This view keeps a wide overlapping centre and squeezes the sides.']`
  Log: Potier et al. 2023 (binocular_deg, Strigiformes 34 to 54.5, mean 45.4; fov_h_deg, Strix aluco 200); Martin 2017 (binocular_deg, Aves 20 to 30 typical).
- `['m', 'Fixed eyes', 'An owl\'s eyes barely move in their sockets, by less than one degree, so the owl turns its whole head to look, as far as about 270 degrees. This view holds still and then jumps when you turn the phone, as an owl\'s head turns.']`
  Log: Potier et al. 2023 (eye_movement, under 1 degree); Sieradzki 2022, a review (eye_movement, 270 degrees); Theunissen and Troje 2017 (eye_movement, Aves).
- `['m', 'Sharpness', 'A barn owl sees only a fifteenth to a twentieth as much detail as a person does, among the lowest values measured in any bird, and other owls measured average about a third. This view is blurred to about a sixth of a person\'s sharpness, between the two.']`
  Log: Harmening et al. 2009 (acuity_cpd, Tyto alba pratincola 2.6 to 4.0); Caves et al. 2018 (acuity_cpd, barn owl 4); Caves et al. 2023 (acuity_cpd, Strigiformes 21.9).
- `['m', 'Night vision', 'A tawny owl\'s eye works close to the limit that any vertebrate eye can reach in dim light. A barn owl sees most sharply in twilight and keeps a quarter of its sharpness when the light falls to a three-hundred-thousandth. This view brightens the shadows and keeps detail as the light fades.']`
  Log: Martin 1986 (absolute_sensitivity, Strix aluco); Orlowski et al. 2012 (absolute_sensitivity, barn owl).
- `['m', 'Colour', 'Owls have lost the colour-sensing cells for violet and ultraviolet light that other birds have, and only about one cone in ten carries a coloured droplet of oil. Barn owls have lost a second kind. This view mutes colours and lets them drain away as the light fades, when only the colourless rod cells are working.']`
  Log: Wu et al. 2016 (receptor_classes, Strigiformes); Hart 2001 (oil_droplets, Strigiformes; colour_vision, rods); Hart 2001 (lambda_max_nm, Strix aluco 463, 555, rod 503).
- `['m', 'Hearing', 'Owls can find and catch prey by sound alone. A barn owl hears faint sounds about 20 decibels quieter than other birds can, thanks to the dish of feathers around its face, and hears pitches above 10,000 vibrations a second. This view shows faint, high sounds picked up by your phone as a soft glow.']`
  Log: Martin 1986 (sense_hearing, Strigiformes); Manley and Köppl 2025 (sense_hearing, Tyto alba); Potier et al. 2023 (sense_hearing, outer ears under the facial disc).
- `['m', 'Sharpest spot', 'A barn owl\'s two sharpest spots both look at the same point straight ahead. This view keeps the centre sharpest.']`
  Log: Hazan et al. 2015 (fovea, Tyto alba).
- `['g', 'Speed', 'Owls follow quick changes less finely than daytime birds of prey. This view does not slow time down the way the hawk view does, and moving things leave short trails.']`
  Log: Potier et al. 2020, review (cff_hz, Strigiformes). The trails are `invented`.
- `['x', 'Where sounds come from', 'A barn owl can place a sound within about 3 degrees side to side and 8 degrees up and down. A phone\'s microphone cannot tell direction this well, so this view leaves direction out.']`
  Log: Bala et al. 2007 (sense_hearing, Tyto alba).

The picture:

| Field | Value | Behind it |
|---|---|---|
| `fov` | 200 | Potier et al. 2023 (fov_h_deg, tawny owl) |
| `cpd` | 10 | `invented` between the barn owl's 2.6 to 4 (Harmening et al. 2009) and the seven-owl mean of 21.9 (Caves et al. 2023); barn owl setting 3.5 |
| `topoA`, `fall` | 1, 1.0 | Hazan et al. 2015 (one forward area); `fall` `invented` |
| `pupil`, `dof` | 'o', 12 | `invented`; no source read on owl pupils or depth of field |
| `M` | camera colours with violet removed; barn owl setting a two-cone matrix | Wu et al. 2016 (no SWS1; RH2 lost in barn owls); the matrices are `invented` |
| `sat` | 0.5 in daylight, falling to 0 in darkness | Hart 2001 (10% coloured droplets; one rod class gives no colour); the curve is `invented` |
| `gain` | 1.8 | Martin 1986, Orlowski et al. 2012; the size is `invented` |
| `sheen` | 0 | Wu et al. 2016 |
| `rate`, `persist` | 1, 0.1 | Potier et al. 2020 review (low temporal resolution); `persist` `invented` |

New effects:

1. **Twilight is sharpest.** The barn owl's acuity peaks at mesopic light (Orlowski et al. 2012), so the view is slightly sharper at dusk than at noon and loses little detail in the dark, while colour drains toward grey as the scene darkens (camera exposure as input). Shader only; easy. Beautiful because it reverses the person's expectation: the owl's world sharpens as theirs fades.
2. **Sound glow.** The microphone's level in the high band (above about 5 kHz) brightens the lower half of the picture for an instant; rustles of leaves become flickers of light. Needs the microphone permission; medium. A left-right bias where a phone gives two channels; most do not, so the row leaves direction out.
3. **Head turns.** As for `hawk`, with longer holds.

### 2.3 `wader`: herons, egrets, ibises, storks, cranes, rails, limpkins, pigeons, doves and gamebirds

Rows:

- `['m', 'Head movement', 'Herons, egrets, cranes, coots, pigeons and chickens hold their heads still while they walk, so their eyes stay fixed on the world. Then the head darts forward in a tenth to a seventh of a second to catch up with the body. This view does the same while you walk.']`
  Log: Necker 2007 (eye_movement, thrust 100 to 150 ms; coots and moorhens); Theunissen and Troje 2017 (eye_movement, Columba livia).
- `['m', 'When they bob', 'Herons bob only when they take long strides, and a walking crane stops holding its head still as it speeds up. Coots and gallinules bob while swimming as well as walking.']`
  Log: Necker 2007 (eye_movement, Ardeidae; Grus americana; Fulica and Gallinula).
- `['m', 'Field of view', 'Herons see about 320 degrees around themselves, gallinules and cranes about 300, and a grouse, a relative of chickens and turkeys, 353. This view squeezes about 320 degrees onto the screen.']`
  Log: Katzir and Martin 1998 (fov_h_deg, Nycticorax nycticorax 320); Portugal et al. 2026 (fov_h_deg, Gallinula chloropus 300; binocular_deg, Grus paradisea, blind area 60.5); Potier et al. 2026 (fov_h_deg, Lyrurus tetrix 353).
- `['m', 'Seeing its feet', 'A heron\'s two eyes overlap in a tall, narrow strip that reaches down below the bill, so a standing heron can see its own feet with both eyes. This view keeps a tall strip down the middle of the picture, where both eyes overlap.']`
  Log: Martin and Katzir 2008 (binocular_deg and behaviour_vision, three herons).
- `['m', 'Two ways of looking', 'A pigeon looks at distant things with a sharp spot on the side of each eye, about 75 degrees from its beak, and at food on the ground within half a metre with a sensitive area in the lower front of its view. This view sharpens two spots to the left and right and the lower centre.']`
  Log: Kano et al. 2022 (fovea; behaviour_vision, Columba livia); Hart 2001 (fovea, red field).
- `['g', 'Sharpness', 'A pigeon sees about a fifth as much detail as a person does, and a grouse about a sixth. This view is blurred to match.']`
  Log: Caves et al. 2018 (acuity_cpd, Columba livia 12); Blough 1971 (acuity_cpd, 7.5 to 25.9); Potier et al. 2026 (acuity_cpd, Lyrurus tetrix 9.81).
- `['m', 'Colour', 'Pigeons, chickens, turkeys and quail have four kinds of colour-sensing cells, one more than people, and the fourth responds to violet light. Their eyes let through less ultraviolet than a songbird\'s. A screen cannot show the deep violet these cells pick up, so this view adds a faint violet tint to stand for it.']`
  Log: Hart 2001 (lambda_max_nm, Columba livia 409, Gallus gallus 419, Meleagris gallopavo 420, Coturnix japonica 418; spectral_range_nm, VS and UVS ocular media); Potier et al. 2026 (lambda_max_nm, Lyrurus tetrix 393).
- `['m', 'Speed', 'In behavioural tests a pigeon saw flicker up to about 75 times a second and a chicken up to about 87. This view runs slightly slow, then jumps ahead.']`
  Log: Boström et al. 2016 (cff_hz, Columba livia 75; Gallus gallus 87; and the pigeon electroretinogram 140, which is not a behavioural limit).
- `['x', 'Very low sounds', 'Homing pigeons can hear sounds far too low for people to hear, down to one vibration every 20 seconds. This view leaves them out.']`
  Log: Patrick et al. 2021 (sense_hearing, Columba livia).
- `['x', 'Touch', 'Some ibises find their food mainly by touch, probing their bills into mud. This view cannot show it.']`
  Log: Potier et al. 2023 (sense_touch, Threskiornithidae).
- `['x', 'Magnetic sense', 'Homing pigeons and chickens sense the direction of the Earth\'s magnetic field. This view leaves it out.']`
  Log: Wiltschko et al. 2021 (sense_magnetic, Columba livia and Gallus gallus); Nießner et al. 2011 (sense_magnetic, robins and chickens).

The picture:

| Field | Value | Behind it |
|---|---|---|
| `fov` | 320 | Katzir and Martin 1998; Portugal et al. 2026; Potier et al. 2026; Kano et al. 2022 (pigeon blind region about 40 degrees, an operational value) |
| `cpd` | 12 | Caves et al. 2018 (pigeon); Potier et al. 2026 (grouse 9.81) |
| regions | sharp spots at ±75 degrees (inside the squeezed frame at about ±0.47 of the half-width), a sharper lower-centre patch, and a tall central strip | Kano et al. 2022; Hart 2001 (red field); Martin and Katzir 2008; sharpness values of the patches `invented` |
| `topoS`, `fall` | replaced by the regions above | the old horizontal band has no source for these birds |
| `pupil` | 'o' | unchanged; no source read |
| `sat`, `sheen` | 1.1, 0.4 | Hart 2001 (violet-sensitive single cones, oil droplets); strengths `invented` |
| `hold`, `thrust` | 280, 120 | thrust from Necker 2007 (100 to 150 ms); hold length `invented` (no duration found; Fujita 2002 wanted) |
| `rate` | 0.75 | 60 / 80, between pigeon 75 and chicken 87 (Boström et al. 2016) |

New effects:

1. **Gait rules from the evidence.** Bobbing only when the step rate from the accelerometer suggests long strides at a slow pace, and fading out at a fast pace, as in the crane (Necker 2007). Easy (the gait detector exists).
2. **Near and far for pigeons.** Within about half a metre (tap or depth estimate) the sharp lower-centre patch takes over, for anything further the two side spots do (Kano et al. 2022). Shader regions; easy.

### 2.4 `duck`: ducks, geese and swans (new)

Rows:

- `['m', 'All the way around', 'A mallard sees all the way around itself and over its head. Its two eyes overlap in a narrow strip, about 22 degrees wide, that runs from the bill up over the crown to the back of the head. This view squeezes the whole circle onto the screen.']`
  Log: Cantlay et al. 2023 (binocular_deg, Anas platyrhynchos 22.0; fov_v_deg, 210; behaviour_vision); Guillemain et al. 2002 (fov_v_deg, Spatula clypeata 220); Martin 2017 (fov_h_deg, panoramic ducks).
- `['m', 'Below the bill', 'A dabbling duck cannot see below the level of its bill. Ducks that feed by filtering water find their food by touch instead, with sensitive tips on their bills. This view darkens the bottom edge of the picture.']`
  Log: Martin 2017 (fov_v_deg, duck below the bill); Cantlay et al. 2023 (sense_touch, Anatidae).
- `['m', 'Geese differ', 'Grazing geese and swans can see their bill tip and keep a blind area behind the head, where dabbling ducks see all around. This view follows the dabbling ducks.']`
  Log: Cantlay et al. 2023 (binocular_deg, Anatidae 16 to 38); Guillemain et al. 2002 (wigeon 150 degrees, narrow blind area behind); Martin et al. 2006 (binocular_deg, blue duck, a visual forager with a large blind area behind).
- `['m', 'Colour', 'Ducks have four kinds of colour-sensing cells, one more than people, and the fourth responds to violet light. A mallard\'s eye blocks most ultraviolet light before it reaches those cells, so this view adds no ultraviolet tint.']`
  Log: Hart 2001 (lambda_max_nm, Anas platyrhynchos 415, 452, 506, 567; spectral_range_nm, mallard 370 to 380).
- `['m', 'No bobbing', 'Ducks, geese and swans do not bob their heads when they walk, the way herons and pigeons do. This view keeps its steady head jumps but adds no bobbing.']`
  Log: Necker 2007 (eye_movement, Anatidae).
- `['i', 'Sharpness', 'This part of the view is a guess. It assumes that a duck sees about a fifth as much detail as a person, the middle value for birds.']`
  Log: Caves et al. 2018 (acuity_cpd, Aves median 11).
- `['i', 'Speed', 'This part of the view is a guess. It assumes that a duck sees flicker about as fast as a pigeon or a chicken, 75 to 90 times a second, and runs the picture slightly slow.']`
  Log: Boström et al. 2016 (cff_hz, pigeon and chicken).
- `['x', 'Touch', 'Many ducks find food by feel, with the many touch-sensing cells at the tip of the bill. This view cannot show touch.']`
  Log: Cantlay et al. 2023 (sense_touch, Anatidae); Martin et al. 2006 (sense_touch, Malacorhynchus membranaceus); Martin 2017 (fov_h_deg note).

The picture:

| Field | Value | Behind it |
|---|---|---|
| `fov` | 360 | Martin 2017; Cantlay et al. 2023 |
| `cpd` | 11 | Caves et al. 2018 (median bird), standing in for an unmeasured duck |
| regions | a narrow vertical strip at the centre running up the frame (the binocular strip), a dark band at the bottom edge (below the bill) | Cantlay et al. 2023; Martin 2017; widths `invented` |
| `pupil` | 'o' | unchanged |
| `sat`, `sheen` | 1.1, 0 | Hart 2001 (mallard VS 415, eye media 370 to 380); the saturation lift `invented` |
| `rate` | 0.75 | `invented` from pigeon and chicken (Boström et al. 2016) |

New effect: **the sky overhead.** Tilting the phone up does not lose the forward view: the top of the squeezed frame shows the sky above the head and the strip where both eyes overlap runs up into it. Uses the existing barrel squeeze plus a vertical squeeze driven by the tilt sensor; medium. It conveys the feel of an animal that watches the sky while its head is down.

### 2.5 `bird`: songbirds and every other bird

Rows:

- `['m', 'Speed', 'Small songbirds that catch insects, such as flycatchers and tits, can see a light flicker up to 130 to 146 times a second. People stop seeing flicker at 50 to 100 times a second, depending on the size of the light. This view runs slowly and then jumps ahead to suggest the difference.']`
  Log: Boström et al. 2016 (cff_hz, Ficedula hypoleuca 146, Ficedula albicollis 141, Cyanistes caeruleus 131).
- `['m', 'Sharpness', 'A house sparrow sees about a twelfth as much detail as a person does, and a phoebe or a blue jay about a seventh. A few songbirds see more: the Eurasian blackbird, a thrush, sees about a third as much as a person. This view is blurred to the level of a small songbird.']`
  Log: Caves et al. 2023 (acuity_cpd, Passer domesticus 4.9, Sayornis nigricans 8.9, and other sparrows and finches); Stone (acuity_cpd, Cyanocitta cristata 8.8, reading 3.4 minutes of arc as half a cycle); Caves et al. 2018 (acuity_cpd, Turdus merula 18; Garrulus glandarius 30).
- `['m', 'Ultraviolet', 'Most songbirds and parrots have colour-sensing cells tuned to ultraviolet light, which people cannot see, and their eyes let it through. Crows, jays and tyrant flycatchers have cells tuned to violet light instead. A screen cannot show ultraviolet, so the violet tint in this view stands in for it.']`
  Log: Hart 2001 (lambda_max_nm, Cyanistes caeruleus 371, Sturnus vulgaris 362, Turdus merula 373, Serinus canaria 369, Taeniopygia guttata 360 to 380, Melopsittacus undulatus 371; spectral_range_nm, UVS ocular media 316 to 343); Lind et al. 2013a (spectral_range_nm, 323 against 358); Ödeen and Håstad 2003 (colour_vision, Corvidae and Tyrannidae); Ödeen et al. 2011 (colour_vision, Passeriformes); Smith et al. 2002 (colour_vision, starling and quail).
- `['m', 'Colour', 'Birds have four kinds of colour-sensing cells, one more than people, and a droplet of coloured oil in each cell narrows the colours it responds to. The droplets help birds tell similar colours apart. This view strengthens colours slightly to suggest it.']`
  Log: Hart 2001 (receptor_classes; oil_droplets).
- `['m', 'Field of view', 'A zebra finch sees about 300 degrees around itself, with a blind area of about 60 degrees behind its head. This view squeezes that sweep onto the screen.']`
  Log: Eckmeier et al. 2013 (fov_h_deg, Taeniopygia guttata 300); Arnold et al. 2022 (fov_h_deg, blind area 60); Martin 2017 (fov_h_deg, one eye 160 to 180).
- `['g', 'Sharpest spots', 'A small songbird\'s sharpest spot looks forward and out to the side. A finch turns its head so that a seed falls on that spot, about 60 degrees from its beak, and a red-winged blackbird\'s single fovea in each eye points the same way. This view sharpens two spots to the left and right of centre.']`
  Log: Kano et al. 2022 (behaviour_vision, Fringillidae); Fernández-Juricic et al. 2019 (fovea, Agelaius phoeniceus); Dolan and Fernández-Juricic 2010 (fovea, one area centralis in ground foragers).
- `['m', 'Steady head', 'A flying zebra finch turns its head in quick jumps lasting about a sixtieth of a second, and holds it steady for about a tenth of a second between them. This view holds the picture still against small turns of your phone and then jumps to catch up.']`
  Log: Eckmeier et al. 2008 (eye_movement, Taeniopygia guttata); Theunissen and Troje 2017 (eye_movement, Aves).
- `['i', 'Magnetic sense', 'Many songbirds sense the direction of the Earth\'s magnetic field with their eyes, and lose their bearings in red or yellow light. This view draws the field as a faint shading that turns with your phone\'s compass and fades in red or yellow light. Nobody knows what the sense feels like to a bird, so the shading is a guess.']`
  Log: Wiltschko et al. 2021 (sense_magnetic, inclination compass; light dependence); Engels et al. 2012 (sense_magnetic, both eyes); Nießner et al. 2011 (sense_magnetic, cryptochrome 1a in the violet and ultraviolet cones); Cochran et al. 2004 (sense_magnetic, calibration at twilight); Leberecht et al. 2022, 2023 (sense_magnetic, radio noise).
- `['x', 'Polarized light', 'Songbirds that migrate at night can use polarized light to find direction, along with the stars, the sun and the magnetic field. This view leaves polarized light out.']`
  Log: Cochran et al. 2004 (polarization, Passeriformes); Able 1989 (polarization, white-throated and American tree sparrows); Hart 2001 (polarization, conflicting evidence).

The picture:

| Field | Value | Behind it |
|---|---|---|
| `fov` | 300 | Eckmeier et al. 2013; Arnold et al. 2022 |
| `cpd` | 8 | Caves et al. 2023 (small songbirds 4.7 to 8.9); Caves et al. 2018 (median bird 11) |
| regions | two sharp spots at ±60 degrees (inside the squeezed frame at ±0.4 of the half-width) | Kano et al. 2022 (finch); Dolan and Fernández-Juricic 2010; sharpness of the spots `invented` |
| `topoA`, `fall` | 0 (replaced by the side spots), 0.6 | the central spot has no source for songbirds |
| `pupil` | 'o' | unchanged; no source read |
| `sat`, `sheen` | 1.1, 0.8 by default; 0.4 in the violet setting | Hart 2001; Ödeen and Håstad 2003, 2013; strengths `invented` |
| `rate` | 0.46 | 60 / 130 (Boström et al. 2016) |
| magnetic shading | a faint, broad darkening whose position follows the angle between the camera's direction and magnetic north and the phone's tilt; opacity falls to 0 when the frame is dominated by red or yellow | `invented`; grounded in Wiltschko et al. 2021 (light dependence) and Nießner et al. 2011 |

Settings for families that stay in `bird` (applied when the database names the species): violet colour for Corvidae, Tyrannidae and other suboscines, Charadriiformes other than Laridae and Rynchopidae, and non-passerines other than parrots (Ödeen and Håstad 2003, 2013; Ödeen et al. 2009); hummingbirds `cpd` 6 and `rate` 0.8 (Goller et al. 2019); swallows four sharp spots (Tyrrell and Fernández-Juricic 2017); cormorants and anhingas `cpd` lowered in water scenes (White et al. 2007).

New effects:

1. **Head jumps** (as for `hawk`, with holds of about 90 ms; Eckmeier et al. 2008).
2. **Magnetic shading.** Uses the compass heading (`deviceorientationabsolute` on Android, `webkitCompassHeading` on iOS) and gravity from the motion sensors; colour of the frame from the camera. Easy to medium. To be beautiful it must stay faint, a slow tide of shade across the sky as the person turns, which never hides the scene.

## 3. The existing views, re-checked

### `hawk` (build 22)

| Item | Now | Verdict |
|---|---|---|
| Row "Sharpness" (g) | "Eagles see more than twice as much detail as people do..." | **Corrected.** Eagles 138 to 143 cycles per degree against 60 is 2.3 times (Caves et al. 2018, 2023), and 1.9 times against Land and Nilsson's human fovea of 72.9; a falcon reached 160 against 60 in one apparatus (Fox et al. 1976). The row applies the eagle to all hawks, while the accipitriforms in Caves et al. 2023 average 24.9 and falcons 47.4. The source in `docs/SOURCES.md` is a Duke news summary; the review itself was read. |
| Row "Speed" (m) | peregrine 129, Harris's hawk 77, people 50 or 60 | **Corrected.** The paper's abstract gives the Harris's hawk 81 Hz (Potier et al. 2020, JEB 223: jeb209031); 77 is the figure in Lund University's news article. Peregrine 129 and saker 102 confirmed. The paper is in volume 223 (2020); the collection index also lists it under 2019, the year `docs/SOURCES.md` gives. |
| Row "Field of view" (i) | keeps the camera's field | **Unsupported, now measured:** about 278 degrees in the red-tailed hawk and 300 in the Cooper's hawk (O'Rourke et al. 2010). |
| `fov` 180 | | **Corrected** to 280. |
| `cpd` 60 | | **Corrected** to 25 at the fovea for hawks and kites; falcon and eagle settings above. |
| `fovea` 2.2 | | **Unsupported as a property of the eye.** Kept only for the eagle setting, as the app's own way of showing detail beyond the camera (2.3 = 140 / 60). |
| `pupil` 'o' | | Unchecked: no source read. |
| `rate` 0.6 | | **Corrected** to 0.74 (60 / 81); the old value matched no measurement (`docs/SOURCES.md` already says so). |
| Gait left out (after Necker 2007) | | **Confirmed**: raptors do not head-bob (Necker 2007). |
| New World vultures sent to `bird` | | **Supported**: their temporal retina has an area and no fovea (Inzunza et al. 1991), and the turkey vulture finds hidden food mainly by smell (Potier et al. 2018). |

### `wader`

| Item | Now | Verdict |
|---|---|---|
| Row "Head movement" (m) | herons, egrets, cranes, pigeons, chickens | **Confirmed** (Necker 2007; Theunissen and Troje 2017), with the limits now in the second row: herons bob only with long strides, cranes stop holding the head still at speed, and coots and gallinules bob while swimming. |
| Row "Speed" (g) | each dart takes about a tenth of a second | **Confirmed**: typical thrust phases 100 to 150 ms (Necker 2007). The row's title collides with the flicker rows of other views; it is folded into "Head movement". |
| Row "Sharpness" (g) | most birds half as much or less | **Corrected**: true as a statement about birds (84% under 30 cycles per degree, Caves et al. 2018), but the pigeon resolves about 12 (7.5 to 26) and a grouse about 10. |
| Row "Ultraviolet" (i) | some birds see ultraviolet | **Corrected and upgraded** to `m`: these birds are violet-sensitive, 409 to 421 nm (Hart 2001; Potier et al. 2026 for a grouse, 393). |
| Row "Field of view" (i) | probably a wide view | **Now measured**: 300 to 353 degrees (see the rows). |
| `fov` 300 | | **Corrected** to 320. |
| `cpd` 25 | | **Corrected** to 12. |
| `topoS` 0.6, `fall` 0.8 | horizontal band | **Unsupported.** Replaced by the pigeon's side foveae, its lower-front field and the heron's tall binocular strip. |
| `sheen` 0.6 | | Invented; lowered to 0.4 for violet-sensitive eyes. |
| `hold` 280 | | Invented, still unmeasured in the sources read. |
| `thrust` 120 | | **Confirmed** (100 to 150 ms). |
| `rate` (none) | | **Added**: 0.75 from pigeon and chicken flicker. |

### `bird`

| Item | Now | Verdict |
|---|---|---|
| Row "Speed" (g) | 40 to 140, fastest fliers highest | **Corrected.** Measured behavioural values in the birds this view covers run from 69 (budgerigar) and 70 to 80 (Anna's hummingbird) to 131 to 146 (tits and flycatchers) (Boström et al. 2016; Goller et al. 2019). No source read gives 40. The highest values belong to small birds that catch insects; the hummingbird, an agile flier, is near the low end. |
| Row "Sharpness" (g) | half as much or less | **Corrected** to the songbird values: 4.7 to 8.9 cycles per degree in sparrows, finches and flycatchers, 8.8 in the blue jay, 18 in the Eurasian blackbird, 30 in the Eurasian jay (Caves et al. 2018, 2023; Stone). |
| Row "Ultraviolet" (i) | some birds | **Upgraded** to `m` with the classes named (Hart 2001; Ödeen and Håstad 2003, 2013; Ödeen et al. 2011). The phrase "Phone cameras capture very little of it" rests in `docs/SOURCES.md` on a University of Sussex news page, which describes a four-channel camera and does not say what ordinary cameras record; the new row says only that a screen cannot show ultraviolet. |
| Row "Field of view" (i) | probably wide | **Now measured**: about 300 degrees in the zebra finch. |
| `fov` 300 | | **Confirmed.** |
| `cpd` 25 | | **Corrected** to 8. |
| `topoA` 0.5, `fall` 0.6 | central spot | **Corrected**: a songbird's sharpest area looks to the side (two spots at ±60 degrees). |
| `sheen` 0.8 | | Invented; kept for ultraviolet-sensitive families. |
| `rate` 0.5 | | **Corrected** to 0.46 (60 / 130). |

## 4. Species with their own measurements

- **Barn owl** (*Tyto alba*; Alachua's American barn owl): acuity 2.6 to 4 cycles per degree, peak at twilight, a quarter kept at 5.5 log units dimmer, sound placed within 3 degrees side to side and 7.5 to 9 up and down, hearing above 10 kHz, threshold near -20 dB SPL, one forward area for both eyes, RH2 opsin lost. Log: Harmening et al. 2009; Orlowski et al. 2012; Bala et al. 2007; Manley and Köppl 2025; Hazan et al. 2015; Wu et al. 2016.
- **Tawny owl** (*Strix aluco*, the barred owl's genus): pigments 463, 503 and 555 nm with rods 503 and no violet cone found; field about 200 degrees. Log: Hart 2001; Potier et al. 2023; Martin 1986.
- **Peregrine falcon** 129 Hz; **saker falcon** 102 Hz. Log: Potier et al. 2020.
- **Harris's hawk**: 81 Hz, two foveae, acuity a little above the black kite's. Log: Potier et al. 2020; Potier et al. 2016.
- **Red-tailed hawk** and **Cooper's hawk**: fields 278 and 300 degrees, binocular 33 and 36, eye movement 4.9 and 8.4 degrees; red-tailed hawk two foveae, rod 501 nm. **American kestrel**: binocular 33 degrees, eye movement 0.9 degrees. Log: O'Rourke et al. 2010; Fite and Rosenfield-Wessels; Hart 2001.
- **Wedge-tailed eagle** (*Aquila audax*): 138 to 143 cycles per degree. Log: Caves et al. 2018, 2023; Land and Nilsson 2012.
- **Rock pigeon**: pigments 409, 453, 507, 567 nm; behavioural flicker 75 Hz; acuity 7.5 to 26 cycles per degree; foveae at ±75 degrees; red field; infrasound to 0.05 Hz; magnetic compass. Log: Hart 2001; Boström et al. 2016; Blough 1971; Caves et al. 2018; Kano et al. 2022; Patrick et al. 2021; Wiltschko et al. 2021.
- **Chicken**: pigments 419, 455, 508, 570 nm; flicker 87 Hz. **Wild turkey** (domestic turkey measured): 420, 459, 505, 563 nm; eye media 358 nm. Log: Hart 2001; Boström et al. 2016.
- **Mallard**: pigments 415, 452, 506, 567 nm, eye media 370 to 380 nm, binocular strip 22 degrees wide and 210 long. **Northern shoveler**: 20 degrees wide, 220 long. Log: Hart 2001; Cantlay et al. 2023; Guillemain et al. 2002.
- **Black-crowned night heron**: field 320 degrees, binocular 22. **Common gallinule** (as common moorhen): field 300 degrees, binocular 34, bobs walking and swimming. Log: Katzir and Martin 1998; Portugal et al. 2026; Necker 2007.
- **Blue tit** 131 Hz and pigments 371, 448, 503, 563 nm; **pied** and **collared flycatchers** 146 and 141 Hz. Log: Boström et al. 2016; Hart 2001.
- **Eastern meadowlark**: one fovea that looks above the horizon with the head at rest, binocular field reaching the bill tip. Log: Tyrrell et al. 2013.
- **Zebra finch**: field 300 degrees, head saccades. **House sparrow** 4.9, **house finch** 4.7, **white-throated sparrow** 7.7, **black phoebe** 8.9 cycles per degree. Log: Eckmeier et al. 2008, 2013; Arnold et al. 2022; Caves et al. 2023.
- **Anna's hummingbird**: 5 to 6 cycles per degree, 70 to 80 Hz. Log: Goller et al. 2019.
- **Blue jay**: 3.4 minutes of arc, about 8.8 cycles per degree. **Red-winged blackbird**: ultraviolet-sensitive, one fronto-lateral fovea per eye, a wide binocular field without foveal input (numbers in the full paper). **Great blue heron**: rods, single and double cones about 2:1:1, with oil droplets. Log: Stone; Fernández-Juricic et al. 2019; Braekevelt 1994.
- **Turkey vulture**: finds hidden food by smell. **Great cormorant**: under water sees about as well as an unaided person under water. Log: Potier et al. 2018; White et al. 2007.
- **European robin**: magnetic compass in either eye, cryptochrome 1a in the violet-ultraviolet cones. Log: Engels et al. 2012; Nießner et al. 2011.

## 5. Gaps and how to fill them

- **Sharpness of the commonest hawks** (red-shouldered hawk, osprey, bald eagle, snail kite). No value read. The accipitriform mean of 24.9 (Caves et al. 2023) stands in; the species values are in that paper's Table S1 (wanted). For the bald eagle the nearest measured eagle is the wedge-tailed eagle (138 to 143).
- **Owl sharpness in *Strix* and *Bubo*.** The barn owl (2.6 to 4) and the seven-owl mean (21.9) disagree by a factor of five. The view's 10 is an invention between them until Fite 1973 (great horned owl) and Martin and Gordon 1974 (tawny owl) are read.
- **Owl flicker fusion.** Only "low temporal resolution" (Potier et al. 2020). The view sets no speed-up, which is the plain reading of that statement.
- **Duck sharpness and flicker.** Nothing measured in the sources read. The median bird (11 cycles per degree) and the pigeon and chicken flicker (75 to 87 Hz) stand in.
- **Herons, cranes, ibises, storks and limpkins: sharpness and colour.** Visual fields are measured (above); acuity and pigments are not, in anything read. The pigeon's 12 and the violet class of the other non-passerines stand in. The whooping crane's pigments (Porter et al. 2014) are wanted.
- **Hold-phase length of head-bobbing.** No duration found; 280 ms stays an invention.
- **Wood stork and limpkin.** Nothing measured in the sources read. The wood stork forages by touch in common accounts, but no source for that was opened, so no row says it.
- **Woodpeckers and the anhinga.** No measurement on live birds in any source read. A skull model gives the anhinga the narrowest binocular field of five foot-propelled divers (Pecsics and Csörgő 2023, no value in the abstract). Woodpeckers take the songbird defaults with the violet setting (non-passerine), the anhinga the cormorant setting.
- **Corvid sharpness.** The Eurasian jay's 30 cycles per degree (Caves et al. 2018) and the blue jay's 8.8 (Stone, if 3.4 minutes of arc is half a cycle; 17.6 if it is a whole one) disagree, so corvids get no sharpness setting of their own. Their colour class is violet (Ödeen and Håstad 2003). The American and fish crows are unmeasured here.
- **The magnetic picture.** Nothing measured says what the sense looks or feels like. The shading is an invention, kept faint, grounded only in what is measured: an inclination compass, light-dependent, in both eyes, in the violet-ultraviolet cones.
- **Polarization.** Conflicting in vision (Hart 2001); used in orientation tests by migrating songbirds (Cochran et al. 2004). Left out.
- **Pupils.** No source read on bird pupils; all views keep 'o'.

## 6. Closed sources wanted

The same list as `docs/views/wanted/birds.jsonl`, most useful first (30 items).

1. Caves, Fernández-Juricic and Kelley 2023, *JEB*, supplementary Table S1 (species acuities). 10.1242/jeb.246063
2. Potier, Mitkus and Kelber 2020, *Seminars in Cell and Developmental Biology* (raptor and owl vision review). 10.1016/j.semcdb.2020.05.004
3. Höglund et al. 2019, *Vision Research* (owl opsins, oil droplets, ultraviolet). 10.1016/j.visres.2019.02.005
4. Fite 1973, *Vision Research* (great horned owl acuity). 10.1016/0042-6989(73)90101-6
5. Martin and Gordon 1974, *Vision Research* (tawny owl acuity). 10.1016/0042-6989(74)90014-5
6. Martin 1986, *Vision Research* (mallard panoramic vision). 10.1016/0042-6989(86)90112-4
7. Potier et al. 2016, *JEB* 219: 2639-2649 (Harris's hawk and black kite). 10.1242/jeb.142083
8. Gaffney and Hodos 2003, *Vision Research* (American kestrel acuity). 10.1016/s0042-6989(03)00304-3
9. Schmid and Wildsoet 1998, *Vision Research* (chick acuity). 10.1016/s0042-6989(97)00446-x
10. Land and Nilsson 2012, *Animal Eyes*, chapters 5 and 9 (the part of the Drive copy that did not come through).
11. Lisney et al. 2011, *Vision Research* (chicken flicker fusion). 10.1016/j.visres.2011.04.009
12. Potier et al. 2018, *JEB* (visual fields of 15 accipitriforms). 10.1242/jeb.177295
13. Tucker 2000, *JEB* (full text: fovea angles by species). 10.1242/jeb.203.24.3745
14. Mitkus et al. 2017, *J. Comp. Neurol.* (photoreceptors of both foveae). 10.1002/cne.24190
15. Dyson, Klump and Gauger 1998, *J. Comp. Physiol. A* (barn owl audiogram). 10.1007/s003590050214
16. Martin 1977, *Nature* (tawny owl absolute threshold). 10.1038/268636a0
17. Martin 1984, *Vision Research* (tawny owl visual fields). 10.1016/0042-6989(84)90005-1
18. Porter et al. 2014, *JEB* (whooping crane pigments). 10.1242/jeb.108456
19. Lisney et al. 2013, *Anatomical Record* (turkey and black vulture retinas). 10.1002/ar.22815
20. Martin and Young 1983, *Vision Research* (pigeon binocular field). 10.1016/0042-6989(83)90061-5
21. Fujita 2002, *Journal of Zoology* (pigeon head-bobbing timing). 10.1017/s0952836902000973
22. Dolan and Fernández-Juricic 2010, *Brain, Behavior and Evolution* (mourning dove and songbird acuity). 10.1159/000305025
23. Martin 1986, *J. Comp. Physiol. A* (starling eye and fields). 10.1007/bf00604174
24. Solov'yov, Mouritsen and Schulten 2010, *Biophysical Journal* (a cryptochrome compass in vision). 10.1016/j.bpj.2010.03.053
25. Martin 1994, *J. Comp. Physiol. A* (woodcock fields). 10.1007/bf00192728
26. Reymond 1985, *Vision Research* (wedge-tailed eagle acuity). 10.1016/0042-6989(85)90226-3
27. Ödeen and Håstad 2003, *Molecular Biology and Evolution* (species table of colour classes). 10.1093/molbev/msg108
28. Knudsen, Blasdel and Konishi 1979, *J. Comp. Physiol. A* (barn owl sound localization). 10.1007/bf00663105
29. Fernández-Juricic et al. 2008, *Ibis* (house finch and house sparrow fields). 10.1111/j.1474-919x.2008.00860.x
30. Lind et al. 2013, *JEB* (raptor eye media). 10.1242/jeb.082834

## 7. Sources

Opened means the full text, or the abstract on the collection index, a publisher, a repository or an author page, was read this session.

- Able KP 1989, *JEB* 141: 241, skylight polarization and migratory sparrows. 10.1242/jeb.141.1.241. opened (abstract)
- Arnold F et al. 2022, *Nature Ecology & Evolution*, zebra finch flight coordination. 10.1038/s41559-022-01800-4. opened (full text)
- Bala ADS, Spitzer MW, Takahashi TT 2007, *PLoS ONE*, barn owl auditory spatial acuity. 10.1371/journal.pone.0000675. opened (full text)
- Blough PM 1971, *J. Exp. Anal. Behav.*, pigeon acuity. 10.1901/jeab.1971.15-57. opened (abstract)
- Boström JE et al. 2016, *PLoS ONE*, ultra-rapid vision in birds. 10.1371/journal.pone.0151099. opened (full text); its pigeon, chicken and budgerigar values are secondary (cited from earlier studies)
- Braekevelt CR 1994, *Anat. Histol. Embryol.*, great blue heron photoreceptors. 10.1111/j.1439-0264.1994.tb00477.x. opened (abstract)
- Cantlay JC et al. 2023, *Proc. R. Soc. B*, binocular vision in Anatidae. 10.1098/rspb.2023.1213. opened (full text)
- Cantlay JC, Portugal SJ, Martin GR 2024, *Ibis*, gull and skimmer fields. 10.1111/ibi.13360. opened (abstract)
- Caves EM, Brandley NC, Johnsen S 2018, *Trends Ecol. Evol.* 33: 358-372, acuity and signals. 10.1016/j.tree.2018.03.001. opened (owner's Drive, main text)
- Caves EM, Fernández-Juricic E, Kelley LA 2023, *JEB*, acuity in 94 bird species. 10.1242/jeb.246063. opened (full text; supplement not read)
- Cochran WW, Mouritsen H, Wikelski MC 2004, *Science*, compass calibration at twilight. 10.1126/science.1095844. opened (abstract)
- Dolan T, Fernández-Juricic E 2010, *Brain Behav. Evol.*, ground foragers' retinas. 10.1159/000305025. opened (abstract)
- Eckmeier D et al. 2008, *PLoS ONE*, zebra finch gaze in flight. 10.1371/journal.pone.0003956. opened (full text)
- Eckmeier D et al. 2013, *Front. Integr. Neurosci.*, zebra finch optic flow neurons (visual field cited from Bischof 1988). 10.3389/fnint.2013.00068. opened (full text); the field value is secondary
- Engels S et al. 2012, *PLoS ONE*, compass in both eyes. 10.1371/journal.pone.0043271. opened (abstract and full text on disk)
- Fernández-Juricic E et al. 2019, *The Auk*, red-winged blackbird vision. 10.1093/auk/ukz039. opened (abstract)
- Fite KV, Rosenfield-Wessels S, *Brain Behav. Evol.* (2008 online), deep avian foveas. 10.1159/000124142. opened (abstract)
- Fox RA, Lehmkuhle SW, Westendorf DH 1976, *Science*, falcon acuity. 10.1126/science.1257767. opened (abstract)
- Goller B et al. 2019, *Physiol. Biochem. Zool.*, Anna's hummingbird resolution. 10.1086/705124. opened (abstract)
- Guillemain M, Martin GR, Fritz H 2002, *Funct. Ecol.*, dabbling duck fields. 10.1046/j.1365-2435.2002.00652.x. opened (abstract)
- Harmening WM et al. 2009, *J. Vis.*, barn owl acuity. 10.1167/9.7.13. opened (abstract)
- Hart NS 2001, *Prog. Retin. Eye Res.* 20: 675-703, avian photoreceptors. 10.1016/S1350-9462(01)00009-X. opened (owner's Drive, full text); its table values are secondary (compiled from primary studies)
- Håstad O, Ernstdotter E, Ödeen A 2005, *Biol. Lett.*, ultraviolet in plunge divers. 10.1098/rsbl.2005.0320. opened (abstract)
- Håstad O, Victorsson J, Ödeen A 2005, *PNAS*, passerine signals and predators' vision. 10.1073/pnas.0409228102. opened (abstract)
- Hazan Y et al. 2015, *Front. Integr. Neurosci.*, barn owl visual search. 10.3389/fnint.2015.00011. opened (full text)
- Inzunza O et al. 1991, *Anat. Rec.*, ganglion cells of falconiforms and a black vulture. 10.1002/ar.1092290214. opened (abstract)
- Kane SA, Fulton AH, Rosenthal LJ 2015, *JEB*, goshawk pursuit. 10.1242/jeb.108597. opened (abstract)
- Kano F et al. 2022, *Sci. Rep.*, pigeon head tracking. 10.1038/s41598-022-21931-9. opened (full text)
- Katzir G, Martin GR 1998, *Ibis*, night heron fields. 10.1111/j.1474-919x.1998.tb04554.x. opened (abstract)
- Land MF, Nilsson D-E 2012, *Animal Eyes*, 2nd edn, OUP. ISBN 978-0-19-958113-9. opened in part (front matter, chapters 1 and 2, chapter 3 to p. 65)
- Leberecht B et al. 2022, *J. Comp. Physiol. A*, radio noise and the compass. 10.1007/s00359-021-01537-8. opened (abstract)
- Leberecht B et al. 2023, *PNAS*, upper bound for radio disruption. 10.1073/pnas.2301153120. opened (abstract)
- Lind O et al. 2013a, *Proc. R. Soc. B*, transparent eye media. 10.1098/rspb.2013.2209. opened (abstract)
- Lind O et al. 2013b, *JEB*, raptor ultraviolet sensitivity. 10.1242/jeb.082834. opened (abstract)
- Lisney TJ et al. 2013, *Anat. Rec.*, New World vulture retinas. 10.1002/ar.22815. opened (abstract)
- Lucas EA et al. 2024, *Naturwissenschaften*, tropical seabird fields. 10.1007/s00114-024-01926-4. opened (full text)
- Lund University 2020, news article on Potier et al. opened (secondary)
- Manley GA, Köppl C 2025, *Biol. Lett.*, barn owl hearing. 10.1098/rsbl.2024.0680. opened (full text; owl values secondary, from cited studies)
- Martin GR 1986, *Ibis*, owl senses. 10.1111/j.1474-919x.1986.tb02674.x. opened (abstract)
- Martin GR 2014, *Phil. Trans. R. Soc. B*, visual fields. 10.1098/rstb.2013.0040. opened (abstract)
- Martin GR 2017, *Front. Neurosci.*, what drives bird vision. 10.3389/fnins.2017.00619. opened (full text)
- Martin GR, Jarrett NS, Williams M 2006, *Ibis*, blue and pink-eared duck fields. 10.1111/j.1474-919x.2006.00611.x. opened (abstract)
- Martin GR, Katzir G, *Brain Behav. Evol.* (2008 online), heron fields. 10.1159/000113571. opened (abstract)
- Martin GR, Portugal SJ, Murn CP 2012, *Ibis*, *Gyps* vulture fields. 10.1111/j.1474-919x.2012.01227.x. opened (abstract)
- Mitkus M et al. 2017, *J. Comp. Neurol.*, raptor fovea photoreceptors. 10.1002/cne.24190. opened (abstract)
- Moore BA et al. 2017, *Sci. Rep.*, fovea position and head and eye movement in 29 species. 10.1038/srep38406. opened (full text)
- Necker R 2007, *J. Comp. Physiol. A* 193: 1177-1183, head-bobbing. 10.1007/s00359-007-0281-3. opened (author's copy)
- Nießner C et al. 2011, *PLoS ONE*, cryptochrome in UV/V cones. 10.1371/journal.pone.0020091. opened (abstract)
- O'Rourke CT et al. 2010, *PLoS ONE*, hawk eyes I. 10.1371/journal.pone.0012802. opened (full text)
- Ödeen A, Håstad O 2003, *Mol. Biol. Evol.*, colour vision classes. 10.1093/molbev/msg108. opened (abstract)
- Ödeen A, Håstad O 2013, *BMC Evol. Biol.* 13: 36, ultraviolet across birds. 10.1186/1471-2148-13-36. opened (full text)
- Ödeen A, Håstad O, Alström P 2009, *Biol. Lett.*, shorebird ultraviolet. 10.1098/rsbl.2009.0877. opened (abstract)
- Ödeen A, Håstad O, Alström P 2011, *BMC Evol. Biol.* 11: 313, passerine ultraviolet. 10.1186/1471-2148-11-313. opened (full text)
- Patrick SC et al. 2021, *Front. Ecol. Evol.*, infrasound. 10.3389/fevo.2021.740027. opened (full text; pigeon value secondary, from Kreithen and Quine 1979)
- Pecsics T, Csörgő T 2023, *Ornis Hungarica*, visual fields of foot-propelled divers (modelled). 10.2478/orhu-2023-0023. opened (abstract)
- Pettigrew JD, Frost BJ, *Brain Behav. Evol.* (2008 online), tactile fovea in sandpipers. 10.1159/000118775. opened (abstract)
- Portugal SJ et al. 2026, *Ecol. Evol.*, common moorhen fields. 10.1002/ece3.74060. opened (full text; blue crane values secondary, from Martin and Shaw 2010)
- Potier S et al. 2016, *JEB* 219: 2639-2649, two raptors. 10.1242/jeb.142083. opened (abstract, Lund portal)
- Potier S et al. 2017, *Brain Behav. Evol.*, accipitriform foveae. 10.1159/000479783. opened (abstract)
- Potier S et al. 2018, *Anim. Cogn.*, sight or smell in vultures. 10.1007/s10071-018-1220-0. opened (full text)
- Potier S et al. 2018, *JEB*, raptor field shape. 10.1242/jeb.177295. opened (abstract)
- Potier S et al. 2023, *Proc. R. Soc. B*, owl binocular fields. 10.1098/rspb.2023.0664. opened (full text)
- Potier S et al. 2026, *JEB*, black grouse vision. 10.1242/jeb.250727. opened (full text)
- Potier S, Lieuvin M, Pfaff M, Kelber A 2020, *JEB* 223: jeb209031, raptor flicker. 10.1242/jeb.209031. opened (abstract, Lund portal)
- Potier S, Mitkus M, Kelber A 2020, *Semin. Cell Dev. Biol.* 106: 116-126, raptor and owl vision. 10.1016/j.semcdb.2020.05.004. opened (abstract, Lund portal)
- Rojas LM et al. 1998, *Brain Behav. Evol.*, shorebird night vision. 10.1159/000006580. opened (abstract)
- Ruggeri M et al. 2010, *Invest. Ophthalmol. Vis. Sci.*, OCT of raptor and owl retinas. 10.1167/iovs.10-5633. opened (abstract)
- Sieradzki A 2022, IntechOpen chapter, owl physiology. 10.5772/intechopen.102397. opened (full text; a review, values secondary)
- Smith EL, Greenwood VJ, Bennett ATD 2002, *JEB*, ultraviolet colour in starlings and quail. 10.1242/jeb.205.21.3299. opened (abstract)
- Stoddard MC et al. 2020, *PNAS*, hummingbird nonspectral colours. 10.1073/pnas.1919377117. opened (abstract)
- Stone RJ, thesis, University of Massachusetts Amherst (repository date 2023), blue jay acuity. 10.7275/6871623. opened (abstract)
- Theunissen LM, Troje NF 2017, *Front. Neurosci.*, pigeon head stabilization. 10.3389/fnins.2017.00551. opened (full text)
- Tucker VA 2000, *JEB* 203: 3745, deep fovea and spiral paths. 10.1242/jeb.203.24.3745. opened (abstract)
- Tyrrell LP et al. 2013, *Sci. Rep.*, eastern meadowlark vision. 10.1038/srep03231. opened (full text)
- Tyrrell LP et al. 2018, *Front. Neurosci.*, hummingbird visual space. 10.3389/fnins.2018.00016. opened (full text)
- Tyrrell LP, Fernández-Juricic E 2017, *Am. Nat.*, swallow eyes. 10.1086/691404. opened (abstract)
- Videler JJ, Weihs D, Daan S 1983, *JEB* 102: 1, kestrel hunting flight. 10.1242/jeb.102.1.1. opened (abstract)
- White CR et al. 2007, *PLoS ONE* 2: e639, cormorant vision. 10.1371/journal.pone.0000639. opened (full text)
- Wiltschko R, Nießner C, Wiltschko W 2021, *Front. Physiol.*, the magnetic compass. 10.3389/fphys.2021.667000. opened (full text; a review, values secondary)
- Wu Y et al. 2016, *Sci. Rep.*, owl and raptor retinal transcriptomes. 10.1038/srep33578. opened (full text)
- Yamazaki Y et al. 2004, *Ornithol. Sci.*, raptor hearing range. 10.2326/osj.3.85. opened (abstract)

## 8. Questions for a specialist

1. The accipitriform mean of 24.9 cycles per degree (Caves et al. 2023) is far below the eagles' 140. Are the anatomical estimates for hawks low because ganglion-cell counts miss the deep fovea's density, or do most hawks really see less detail than people?
2. For barred and great horned owls, which acuity should a view use: the barn owl's behavioural 3 to 4, or the anatomical estimates near 20?
3. Is it fair to draw a hawk's far view with the deep fovea at the centre of the frame, given that Tucker's raptors held distant objects sideways 80 percent of the time?
4. Do ibises, storks and limpkins head-bob as reliably as herons, or is their place in the `wader` view weaker than Necker's table suggests?
5. Which commonly photographed birds outside passerines and parrots are known to be ultraviolet-sensitive, beyond gulls, skimmers, some terns, trogons, motmots and sandgrouse?
6. Would any measured property of the radical-pair compass (its dependence on the angle to the field lines, its wavelength window) justify a particular shape for the invented magnetic shading?
