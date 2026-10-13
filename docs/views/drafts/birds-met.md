# Round 2 sheet: birds people meet (views `bird`, `hawk`, `wader`), draft

Written 13 October 2026. Evidence: `docs/views/evidence/birds-met.jsonl` (77 records, on top of the 218 of `research/birds`). Wanted: `docs/views/wanted/birds-met.jsonl` (27 lines). Searches that found nothing: `docs/views/searched/birds-met.jsonl`. Proposed exceptions: `docs/views/carry.jsonl`.

What was opened. Hart 2001 in full (the owner's Drive; Table 1 pigments and the ocular-media passage). Open full texts from `pub/lit-t1`: Odeen and Hastad 2013, Odeen, Hastad and Alstrom 2011, Caves et al. 2023, Olsson et al. 2021, Lucas et al. 2024, Portugal et al. 2026, Martin 2017, O'Rourke et al. 2010 (Hawk Eyes I and II), Bostrom et al. 2016. The web beyond the collection was closed to this machine (the proxy refused every host and WebFetch asked a permission nobody answered). Species-level sharpness for the backyard birds needs the supplementary tables of Caves et al. 2023 and Olsson et al. 2021, which the article texts leave out; both are priority 1 on the wanted list and both are open access, so they are quick to fetch.

## 1. Where the current rows are wrong or unsupported for species people meet

| View | Row | Problem | Species affected (Alachua records, round 1) |
|---|---|---|---|
| `wader` | Ultraviolet | Every wader species with a sequence or pigment is violet type, and a grey heron, mute swan and great crested grebe have ocular media that stop ultraviolet at 380 nm or higher. The row says ultraviolet reaches them through a violet tint. | white ibis, wood stork, herons, pigeons, doves, chickens |
| `wader` | Head movement | Bobbing is shown for pigeons, chickens, coots, moorhens and herons with long strides, and cranes at slow speeds. Nothing in the collection shows it for ibises, storks or the limpkin. | white ibis 1,015, limpkin 1,055, wood stork 634 |
| `wader` | Sharpness | The only wader-view measure is the pigeon at 12 cycles per degree (Caves, Brandley and Johnsen 2018, round 1). The view draws 25. | all |
| `hawk` | Two sharp spots | A black kite has one fovea (round 1, Potier et al. 2016, abstract). The row says hawks, eagles and falcons have two. Carry rule 5 blocks it for kites. | snail kite 628, Mississippi kite, swallow-tailed kite |
| `hawk` | Speed | The numbers are for peregrine, saker and Harris's hawk. The row's closing sentence says the view runs at the Harris's hawk's pace. | red-shouldered hawk 1,192, osprey 469, bald eagle 230 |
| `bird` | Ultraviolet | A violet cone and ultraviolet-stopping ocular media fit ducks, vultures, ibises, doves, woodpeckers and probably crows and jays, so the row is false for them. It holds for starlings, blackbirds, tits, finches and gulls (see below). | anhinga, cormorants, ducks, turkey vulture 417 |

## 2. Rows by species group, in the second person

Rows below are drafts. The log lines behind each are named by author, year, trait and taxon.

### `bird`, songbirds of the Passerida (cardinal, mockingbird, warblers, blackbirds, grackles, sparrows, starlings, finches, tits)

- `['g', 'Colour', 'You have four kinds of colour-sensing cell, one more than a person has. The fourth responds to ultraviolet light, which a phone camera barely records, so this view adds a violet tint to stand in for it.']` Measured in the starling, blackbird, blue tit, canary and zebra finch (Hart 2001, lambda_max_nm). Carried to the rest of the Passerida by the exception proposed in `carry.jsonl`, since the sequenced Passerida are all ultraviolet type (Odeen et al. 2011). Grade `g` for a cardinal or mockingbird; `m` for the starling and blackbird.
- `['m', 'Speed', 'A blue tit sees a light flicker at up to 131 times a second, and the collared and pied flycatchers 141 and 146. This view runs slowly and then jumps ahead to catch up.']` Bostrom et al. 2016 (cff_hz). Rule 1: the figure is stated for those three species only. For a cardinal the row reads "small songbirds measured so far see flicker at over 130 times a second" at grade `g`, naming the tit and flycatchers.
- `['m', 'Sharpness', 'A house sparrow resolves about 5 cycles per degree, a white-throated sparrow 8, a blackbird 18. A person resolves 60.']` Caves et al. 2023 (house sparrow 4.9, white-throated 7.7), Caves, Brandley and Johnsen 2018 (blackbird 18). Wide spread between species. Numbers do not travel (rule 1), so a mockingbird or cardinal has no sharpness figure at `m`; `bird` draws 25 and is `i`.
- `['m', 'Field of view', 'A zebra finch sees about 300 degrees around its head.']` round 1, Eckmeier et al. 2013. For other songbirds `i`.

### `bird`, crows and jays

- `['g', 'Colour', 'You have a violet-sensitive short-wave cell, where most songbirds have an ultraviolet one. This view tints toward violet and leaves out the ultraviolet shift.']` round 1, Odeen and Hastad 2003 (abstract); the primary sequences are on the wanted list. No pigment has been measured in a crow or jay, so this is `g` through a clade statement and not through rule 2. The song-bird default in `bird` is therefore wrong for them.
- `['m', 'Sharpness', 'A Eurasian jay resolves about 30 cycles per degree, half a person\'s; a blue jay about 9.']` Caves, Brandley and Johnsen 2018 (Garrulus glandarius 30); Stone 2023 (Cyanocitta cristata 8.8). The two differ by a factor of three and the genus rule forbids carrying either to the other, so the row names both and says no crow has been measured. Caves et al. 2023 report corvids with the highest residual acuity apart from falcons without giving a value; the table is wanted.
- `['g', 'Binocular view', 'Crows have the widest overlap of the two eyes among birds measured, so the view ahead is the most shared of any bird.']` Martin 2017 review of Troscianko et al. 2012 (binocular_deg). The primary paper is not opened.

### `bird`, ducks, geese and swans

- `['m', 'Field of view', 'A mallard sees about 210 degrees from the bill over the crown and a shoveler 220, and both have a strip of about 20 degrees where the eyes overlap.']` round 1, Cantlay et al. 2023; Guillemain et al. 2002. Ducks other than these two are carried within Anatidae only at `g`, as geese and swans differ (Cantlay et al. 2023).
- `['g', 'Colour', 'You have a violet-sensitive cell and your eye\'s lens and cornea block most ultraviolet, so the ultraviolet tint does not apply to you.']` Mallard pigment 415 nm and ocular media half transmission 370 to 380 nm (Hart 2001); Muscovy duck, brant and goosander sequences are violet type (Odeen and Hastad 2013). Carry proposed in `carry.jsonl`. The `bird` Ultraviolet row is false for ducks as it stands.

### `bird`, gulls and terns

- `['g', 'Colour', 'You have an ultraviolet-sensitive short-wave cell, one of the few shorebird lines that does.']` Odeen and Hastad 2013 and round 1 (Hastad et al. 2005) report this for Larus gulls, noddies and white terns as a family statement; no gull pigment has been measured. Grade `g`.
- `['g', 'Field of view', 'Terns and noddies see about 140 degrees to each side with a narrow strip about 26 degrees wide ahead and a blind area of about 35 degrees above the head.']` Lucas et al. 2024 (seven tropical seabirds; terns only). Gulls themselves are in round 1 (Cantlay et al. 2024, abstract); rule 3 stops the carry from terns to gulls.

### `bird`, vultures

- `['g', 'Colour', 'You have a violet-sensitive short-wave cell.']` turkey vulture opsin sequence (Odeen and Hastad 2013 Table 1), `g` because sequence predicts and does not measure; black vulture by the exception proposed in `carry.jsonl`.
- `['m', 'Smell', 'You find food by smell as well as by sight. A turkey vulture chose a hidden smelling ball over a colour it had learned.']` round 1, Potier et al. 2018. This is a sense the picture leaves out (`x`); nothing in the current `bird` view says so for vultures.
- `['g', 'Sharpness', 'Turkey and black vultures share a retinal map and a resolving power in the same range.']` Lisney et al. 2013 abstract (round 1); the number is on the wanted list.

### `bird`, anhinga, cormorants, pelicans

Nothing measured about the anhinga. A great cormorant sees underwater about as well as an unaided person does under water (White et al. 2007, round 1). Carry to the anhinga needs an exception (different family); not proposed until a reason is found. Mark the anhinga `i` throughout.

### `hawk`, buteos, accipiters (red-shouldered hawk, red-tailed hawk, Cooper's hawk)

- `['m', 'Field of view', 'A red-tailed hawk sees 278 degrees around its head with 33 degrees of overlap, a Cooper\'s hawk 300 with 36.']` O'Rourke et al. 2010. A red-shouldered hawk borrows the red-tailed hawk's at `g` (same genus, rule 3), naming the relative.
- `['m', 'Looking sideways', 'You glance about every few seconds. A Cooper\'s hawk turns its head most often, a red-tailed hawk waits longest between turns, and a kestrel bobs its head forward and back most.']` O'Rourke et al. 2010 Hawk Eyes II (eye_movement; three records, rates in the paper's Figure 1 only).
- `['m', 'Colour', 'You have a violet-sensitive short-wave cell. Ultraviolet adds little to what you see.']` Lind et al. 2013 (buzzard, sparrowhawk, red kite, kestrel), Odeen and Hastad 2013 (Mississippi kite, Pacific baza). Carry to the osprey needs the exception in `carry.jsonl`.

### `hawk`, kites, osprey and eagles

- Kites. The row on two sharp spots is blocked: a black kite has one fovea (round 1, Potier et al. 2016). Replace with "you have one sharp spot per eye" for Milvus only and a guess (`i`) for snail and swallow-tailed kites.
- Osprey and bald eagle: no measurement of any visual trait was found in the collection. The bald eagle appears only in a head-movement comparison (Tucker 2000, round 1: long intervals between head movements) and in eye-measurement and ERG papers that are on the wanted list.

### `wader`, herons and egrets

- `['m', 'Field of view', 'A black-crowned night heron sees 320 degrees, a cattle egret and little egret share a 20 degree overlap, and the eye axes point down so you see the ground under your bill.']` round 1, Katzir and Martin 1998; Martin and Katzir 2008; Martin 2017 (cattle egret figured). Carry to the great blue heron through rule 3 is not allowed (genus Ardea not measured for fields); the exception proposed covers Ardeidae.
- `['g', 'Head movement', 'You hold your head still while you walk with a long stride, then dart it forward. With short steps you do not.']` Necker 2007 (round 1). A grey heron bobs on long strides (Hawk Eyes II introduction citing Necker).
- `['g', 'Colour', 'You have a violet cell and your lens stops most ultraviolet, so this view tints toward violet only.']` grey heron ocular media at 380 nm or above (Olsson et al. 2021); glossy ibis and roseate spoonbill violet type (Odeen and Hastad 2013). Replace the wader view's Ultraviolet row.

### `wader`, ibises, storks, limpkin, cranes

- Ibises: violet type by sequence (glossy ibis, roseate spoonbill). A white ibis (genus Eudocimus) is a different genus from both, so its colour row stays `i` until an exception from the Threskiornithidae sequences is accepted; the owner may add one.
- Head movement: no evidence for ibises, storks or limpkins. Replace the row with a sentence about what the view does for those species.
- Cranes: whooping crane pigments are on the wanted list; blue crane binocular field is 21.5 degrees (round 1, Portugal et al. 2026). Sandhill crane `i`.

### `wader`, rails (common gallinule) and pigeons, chickens

- Common gallinule (GBIF: moorhen): 300 degree field, 34 degree overlap, head must pitch down at least 30 degrees to see the ground under the bill (Portugal et al. 2026, round 1 and mine). Bobs on land and water (Necker 2007).
- Pigeon: violet pigment 409 nm; flicker 75 and 140 Hz at two light levels in the same paper (Bostrom et al. 2016; round 1 logs both); 12 cycles per degree. Chicken: pigment 419 nm, flicker 87 Hz (Bostrom 2016). Wader view's "pigeons" row stays; "chickens" holds (Necker 2007).

## 3. Commonly met species whose rows are still mostly borrowed

anhinga, boat-tailed grackle, northern cardinal, palm warbler, northern mockingbird, red-winged blackbird (acuity and vision in an abundant bird exist as an abstract in round 1), great egret, white ibis, wood stork, limpkin, sandhill crane, osprey, snail kite, bald eagle, red-shouldered hawk, black vulture, ring-billed gull, American crow, blue jay (only a sharpness value).

## 4. Questions for a specialist

1. Do ibises and storks head-bob, and at what stride?
2. Is the snail kite's retina bifoveate like a buteo's, or single-foveate like the black kite's?
3. Are American crows and blue jays violet type, as the sequences of other corvids suggest?
