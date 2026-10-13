# Sensing sheet: mammal groups (mammal, primate, whale, bat, flying fox)

Written on 13 October 2026, from 01:46 UTC, by one research agent. The evidence behind it is the log `docs/views/evidence/mammal-groups.jsonl`, cited below by line number ("log 55" is the 55th line). The wanted list is `docs/views/wanted/mammal-groups.jsonl`.

**How the sources were read.** Most lines come from the literature collection on `pub/lit-t1` (topics `mammals-other`, `primates`, `marine-mammals` and `bats`, with the neighbouring `carnivores` and `ungulates`), read on disk: open full texts where the collection holds them, and otherwise the abstracts it stores. Publisher pages and a few public pages were read through the web tool, which returns a summary with short verbatim quotes; those lines say so. Two paywalled works came from the owner's library and are cited with short quotes only: Caves, Brandley and Johnsen 2018 (all 15 pages of the main article; the supplementary tables of species values are not in the copy) and Land and Nilsson 2012, *Animal Eyes*, 2nd edition (front matter, chapters 1 and 2, and chapter 3 up to its section on sensitivity, about pages 1 to 64; chapters 4 to 9, including "Amphibious eyes" on p. 117 and "Mirrors in eyes" on p. 130, did not come through). The collection sometimes shortens or reorders author lists (it gives Moss and Surlykke 2010 under Moss alone, and Boonman and colleagues 2013 in another order); the authors of the most used papers were checked on the publisher's page, and the rest are as the collection records them.

**Record counts** are iNaturalist research-grade records in GBIF (dataset `50c9509d-22c7-4a22-a47d-8c48425ef4a7`), read on 13 October 2026 from GBIF's public API with facets by family, genus or species. The bat family counts are the ones the earlier bat sheet read on 11 October and its audit re-read on 12 October; the flying fox total of 22,639 was read again today and has not changed.

**Unfinished, and pages refused.**

- **Not measured anywhere I could open:** flicker fusion for any member of the five groups (one primate study is on the wanted list); field of view for any primate, whale, dolphin, flying fox or insect-eating bat; pupil shape for most of the mammal group; colour vision of koalas, hedgehogs, shrews, skunks, mongooses, ringtails and sea otters; acuity of raccoons, Virginia opossums, bears, otters, pigs and koalas.
- **Read only as titles, so no line rests on them:** Simmons and colleagues 1983 and Geberl, Kugler and Wiegrebe 2019 on the sharpness of bat sonar; Hanke and Dehnhardt 2009 and Schusterman and Balliet 1971 on aerial acuity as light falls in seals and sea lions; Griebel and Schmid 1996 and Newman and Robinson 2006 on manatee colour; Ordy and Samorajski 1968 on primate flicker fusion; Mass 2001 on the beluga's visual field. All are on the wanted list.
- **Refused:** PubMed showed a browser check instead of the record (two requests). Europe PMC's search service answered one query with HTTP 429 (rate limit) at about 02:00 UTC, and I made no further requests to it. ScienceDirect refused Ordy and Samorajski 1968 by its robots rule. The Michigan State University repository refused a thesis on the raccoon's forepaw. The shell could not reach GBIF or Europe PMC directly (HTTP 403 at the session's proxy), so GBIF was read through the web tool.

## 1. Scope

### What the five groups hold

| Group (key) | What it holds | World records | Most recorded |
|---|---|---:|---|
| `mammal` | the mammals outside every other view: raccoons, bears, weasels and otters, skunks, mongooses, kangaroos, koalas, possums, opossums, pigs, hippos, rhinos, elephants, moles, shrews, hedgehogs, armadillos, sloths, anteaters, pangolins, platypus, echidnas | 1,019,965 | Common raccoon, Virginia opossum, American black bear |
| `whale` | whales, dolphins, porpoises, seals, sea lions, walruses, manatees, dugongs | 274,115 | Harbour seal (44,546), humpback whale (31,040), California sea lion (30,683) |
| `primate` | every primate but people | 192,888 | Crab-eating macaque (15,934), mantled howler (10,810), vervet monkey (10,239) |
| `bat` | every bat family except Pteropodidae | 71,170 | Big brown bat, Mexican free-tailed bat, proboscis bat (bat sheet) |
| `flyingfox` | family Pteropodidae | 22,639 | Grey-headed, Indian and black flying foxes (bat sheet) |

The `mammal` total and the `whale`, `primate`, `bat` and `flyingfox` totals agree with `docs/COVERAGE.md`. The `mammal` total sums the orders listed in `docs/views/world-orders.csv` for it, and its carnivores are the Carnivora families left after cats, dogs, seals, sea lions and walruses (1,058,789 Carnivora records less 296,559 Canidae, 165,169 Felidae, 79,366 Phocidae, 72,575 Otariidae and 1,075 Odobenidae is 444,045).

**Alachua County, Florida.** The county's list (`docs/views/no-view-us-fl-alachua.csv`) holds nine species of this unit's `mammal` group: Common raccoon 281, Virginia opossum 137, Eurasian wild pig 61, North American river otter 53, Eastern mole 51, American black bear 14, Striped skunk 8, Southern short-tailed shrew 3 and North American least shrew 2. It holds six bats, all calling bats (Mexican free-tailed 179, Southeastern myotis 50, Tricolored 28, Evening 5, Seminole 4, Northern yellow 2), and one sirenian, the West Indian manatee (2). It holds no primate, flying fox, whale or seal. The nine-banded armadillo is not on the county's list.

### Where the views should split

Each split below is a place where the commonly photographed members sense the world differently enough that one picture would be false for some of them. The pocket model names groups only, so each group keeps one entry under its own key, used whenever only the group is known; the further entries are reached when the species is known, by the taxonomy rule in `tools/species/eyes.py`.

**`bat` and `flyingfox`.** The earlier bat sheet's split at family Pteropodidae stands (section 3). Calling bats build their surroundings from echoes and see about 0.1 to 1 cycle per degree (log 55 to 74); flying foxes make no calls and see about 4 (log 75, 76). Inside `flyingfox`, colour splits by genus: *Pteropus* (68.8% of flying fox records) has blue and green cones, while *Rousettus*, *Eidolon* and *Epomophorus* (18.4% together) have the green cone only (log 146, 147); the other genera (12.8%, led by *Cynopterus*) are unmeasured. That is drawn as a colour variant of one view. Inside `bat`, the horseshoe and roundleaf bats (Rhinolophidae and Hipposideridae, 10.5% of `bat` records) have lost the ultraviolet cone and call in long constant tones (log 85); that difference waits for a species-level profile.

**`whale`: four entries.**

| Entry | Who | Records | Share of `whale` | Why it differs |
|---|---|---:|---:|---|
| `seal` | seals, sea lions, walrus | 153,016 | 55.8% | one cone near 510 nm; amphibious eye with a slit and pinhole pupil; measured field of 208 degrees; whiskers that follow wakes (log 15, 34, 36, 42) |
| `dolphin` | toothed whales, dolphins, porpoises | 67,250 | 24.5% | one cone near 524 nm, or none in sperm whales; two sharp areas; double-slit pupil; narrow sonar beam (log 9, 23, 25, 49) |
| `whale` | baleen whales, and the group's default | 45,099 | 16.5% | rods only; tuned near 484 to 493 nm; about 4 cycles per degree (log 1, 12, 13, 29) |
| `manatee` | manatees, dugongs | 8,750 | 3.2% | two cones; about 1.3 cycles per degree; touch hairs over the body (log 17, 45, 46) |

The default entry is shared by the whole group when the species is unknown, so its rows say only what holds for whales and seals alike: no colour, coarse sight, eyes that focus under water, and a reflecting layer (log 5, 19, 20, 159). Rod-only vision covers the baleen whales and the sperm whales (17.3% of the group's records; log 1 to 4).

**`primate`: three entries.**

| Entry | Who | Records | Share of `primate` | Why it differs |
|---|---|---:|---:|---|
| `primate` | Old World monkeys, apes, howler monkeys | 129,432 | 67.1% | three cones in every animal; sharp sight (log 99 to 108, 91) |
| `capuchin` | New World monkeys except howlers and owl monkeys | 49,844 | 25.8% | every male and some females see two colours; others three (log 106, 163) |
| `lemur` | lemurs, lorises, galagos, tarsiers, owl monkeys | 13,612 | 7.1% | two cones or one; 4 to 9 cycles per degree; reflecting layer in lemurs and galagos (log 109 to 116, 165) |

**`mammal`: three entries.**

| Entry | Who | Records | Share of `mammal` | Why it differs |
|---|---|---:|---:|---|
| `mammal` | everyone below not named in the other two | 739,649 | 72.5% | two cones (log 7, 124 to 127, 134, 139) |
| `raccoon` | raccoons (*Procyon*), kinkajou, Virginia opossum, pangolins; with a rods-only variant for armadillos, sloths and anteaters | 194,801 and 57,257 | 19.1% and 5.6% | one cone (log 120, 122) or none (log 141) |
| `mole` | moles (Talpidae) | 28,258 | 2.8% | eyes under skin or tiny; touch and smell lead (log 130, 154, 169) |

The `raccoon` split follows the earlier mammal sheet with three changes. Only the Virginia opossum goes to it, because South American opossums have two cones (log 123); it holds 82.4% of opossum records. Coatis (*Nasua*, 23,197 records) go to `mammal`, as dichromats (log 121). Rods-only animals become a variant of `raccoon` with a glare effect (section 2), because they share its grey picture. Pangolins (1,227 records) follow the earlier sheet's reading of Emerling and Springer 2015 (one cone left), which I did not reopen. The ringtail (*Bassariscus*, 6,418 records) and the olingos are unmeasured, nocturnal procyonids, and stay in `mammal` until someone measures them.

The `mole` split also follows the earlier sheet, with a correction: 60.6% of mole records are European moles, whose tiny eyes carry blue- and green-sensitive cones (log 130), so "no picture at all" is untrue for most mole records. The `mole` view keeps a picture of light only (no image), and now keeps the colour of that light. Eastern moles (11.0%) have skin over their eyes (log 169), and star-nosed moles (6.0%) live by touch (log 154).

Hedgehogs (European hedgehog 34,345 records, 3.4% of `mammal`) and shrews (22,088, 2.2%) have no source here. They stay in `mammal` by default, and section 5 says how a value could be inferred.

**Summary of the twelve entries.**

| Key | Chip | Routing rule (first match wins) | Records | Share of its group |
|---|---|---|---:|---:|
| `bat` | Bat | order Chiroptera | 71,170 | 100% |
| `flyingfox` | Flying fox, fruit bat | family Pteropodidae (before `bat`) | 22,639 | 100% |
| `whale` | Whale, dolphin, seal | Cetacea families Balaenopteridae, Eschrichtiidae, Balaenidae, Neobalaenidae; also every photo named only to the group | 45,099 | 16.5% |
| `seal` | Seal, sea lion, walrus | families Phocidae, Otariidae, Odobenidae | 153,016 | 55.8% |
| `dolphin` | Dolphin, porpoise | Cetacea families Delphinidae, Phocoenidae, Physeteridae, Kogiidae, Monodontidae, Ziphiidae (GBIF's Hyperoodontidae), Iniidae, Pontoporiidae, Platanistidae, Lipotidae | 67,250 | 24.5% |
| `manatee` | Manatee, dugong | order Sirenia | 8,750 | 3.2% |
| `primate` | Monkey, ape | order Primates | 129,432 | 67.1% |
| `capuchin` | Capuchin, spider monkey, marmoset | families Cebidae, Callitrichidae, Pitheciidae, Atelidae except genus *Alouatta* | 49,844 | 25.8% |
| `lemur` | Lemur, loris, galago | suborder Strepsirrhini families, Tarsiidae, Aotidae | 13,612 | 7.1% |
| `mammal` | Bear, otter, kangaroo, pig | the orders in `docs/views/world-orders.csv` for this group | 739,649 | 72.5% |
| `raccoon` | Raccoon, opossum, armadillo | genera *Procyon*, *Potos*; species *Didelphis virginiana*; orders Pholidota, Cingulata, Pilosa | 252,058 | 24.7% |
| `mole` | Mole | family Talpidae | 28,258 | 2.8% |

Sea otters (13,624 records) and polar bears are marine mammals by habit and carnivores by family. They stay in `mammal` with their families, because their cones are the ordinary mammalian pair (log 17; Levenson and colleagues 2006 for the sea otter, in the earlier sheet).

## 2. The views

### `bat` (every bat family except Pteropodidae)

**Rows.**

1. `['m', 'Calls', 'A Mexican free-tailed bat, the bat recorded most often in Alachua County, calls about four times a second while it searches for insects, and a big brown bat calls 5 to 10 times. Each call brings back one brief sound picture of what lies ahead. This view holds its picture and renews it at that pace.']`
   Log 67 (Jung and colleagues 2014, Table 2: 3.7 calls a second); log 55 and 56 (Moss and Surlykke 2010).
2. `['m', 'Closing in', 'When a big brown bat closes in on an insect, it calls 20 to 80 times a second, and up to about 170 times in the final buzz. Its echoes then tell it distance to within about 1.5 centimetres, where its slower search calls tell it only to 15 centimetres or so.']`
   Log 55, 57 (Moss and Surlykke 2010).
3. `['g', 'Reach', 'An insect-eating bat hears the echo of a small insect from about 2 to 14 metres away, depending on the bat, the insect and the keenness of its hearing. Large shapes such as trees return echoes from tens of metres away. Beyond that, its calls bring back nothing it can hear.']`
   Log 60 (Boonman and colleagues 2013, calculated for two bats); log 59 (21 m for large objects in *Eptesicus bottae*).
4. `['m', 'Sound beam', 'A bat sends each call forward in a cone. In a flight room a big brown bat's cone is 60 to 90 degrees wide, about as wide as this camera's view, and in the wild a Daubenton's bat narrows it to about 30 to 50 degrees. The bat swings the cone from one object to the next, aiming within about 5 degrees.']`
   Log 58 (Moss and Surlykke 2010); log 66 (Surlykke and colleagues 2008: half-amplitude angles of 14 and 25 degrees, doubled to full widths; see the note on log 66).
5. `['g', 'Sharpness', 'Insect-eating bats see little detail. A big brown bat makes out about half a cycle to two thirds of a cycle per degree, roughly a hundredth of your sharpness, and Daubenton's bat about the same. This view is blurred to match.']`
   Log 62 (big brown bat, 0.7 to 1 degree, as Boonman and colleagues report); log 74 (Daubenton's bat 0.6); log 69, 71, 92 (other species 0.1 to 2).
6. `['m', 'Dim light', 'In one test a big brown bat could still tell a white object from its background by sight in light no brighter than 0.0008 lux. Many bats start hunting at dusk, in light of 1 to 10 lux, and use their eyes and their echoes together. The shadows are lifted here.']`
   Log 63 (Ellins and Masterson 1974, as Boonman and colleagues report); log 61.
7. `['g', 'Colour', 'Most bats studied have two kinds of colour-sensing cells, and one kind detects ultraviolet light, which people cannot see. These cells make up only 2 to 4 in every hundred light-sensing cells, so colour is drained from this view. Horseshoe bats, roundleaf bats and vampire bats have lost the ultraviolet kind.']`
   Log 82 (Müller and colleagues 2009), 83 (Li and colleagues 2018: 357 to 359 nm), 85 (Jones and colleagues 2013), 88 (Kries and colleagues 2018).
8. `['m', 'Eyes and ears together', 'When what a bat sees and what its echoes tell it disagree, it follows its eyes. Bats with simpler calls have larger eyes than the most skilled callers.']`
   Log 86 (Jones and colleagues 2013, a review); log 90 (Thiagavel and colleagues 2018).
9. `['x', 'Echoes', 'A bat's calls are pitched too high for a phone's own microphone to record. Until the app can draw echoes from the camera's sense of distance, this view leaves them out.']`
   Sources: ecoObs FAQ (the built-in microphone of an iPhone or iPad does not pick up bat calls), opened today; log 55 to 68 for the calls themselves. When the echo picture below is built, this row becomes `['i', 'Echoes', 'A bat's calls are pitched too high for a phone's own microphone to record, so this view draws distance from the camera instead and shows it as an echo picture. That drawing is the app's own.']`.
10. `['x', 'Magnetic compass', 'Greater mouse-eared bats set an inner magnetic compass by the sunset and use it to fly home. The picture leaves this sense out.']`
    Log 89 (Holland, Borissov and Siemers 2010).
11. `['x', 'Body heat', 'A common vampire bat feels the body heat of the animal it feeds on through three small pits on its nose. The picture leaves this sense out.']`
    Log 87 (Jones and colleagues 2013, reviewing Kürten and Schmidt 1982 and Gracheva and colleagues 2011).

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who`, `cue` | 'Bat', 'a bat', 'Each call brings back one snapshot, so the picture holds, then jumps.' | The app's wording, kept from the earlier sheet. |
| `cpd` | 0.6 | Daubenton's bat 0.6 (log 74); big brown bat 0.5 to 0.7 (log 62). |
| `hold`, `thrust` | 200 and 30 ms | A cycle of 230 ms gives 4.3 renewals a second, between the free-tailed bat's 3.7 (log 67) and the big brown bat's 5 to 10 (log 55). The exact pair is **invented**. The earlier sheet's 110 and 30 ms (7 a second) fit the big brown bat and run faster than the bat most recorded in Alachua. |
| `sat` | 0.2 | **Invented**, after the cone share of 2 to 4% (log 82). |
| `gain` | 1.6 | **Invented**; dim light (log 63). |
| `pupil` | 'o' | **Invented**; no source found, and with `dof` unset it changes nothing. |
| `topoS`, `fall` | 0.4 and 0.8 | Peak ganglion cell density low in the back of the retina with horizontally drawn-out isodensity lines, only 2 to 4 times the density elsewhere (log 70), so a weak band. The values are **invented**. The band would sit a little above centre, since the lower back retina looks up and forward; the engine cannot yet move it. |
| `fov`, `M`, `uvBlue`, `sheen`, `rate`, `persist`, `gate`, `field` | unset | No field of view, flicker rate or colour model is sourced; the ultraviolet cone is lost in several lineages (log 85, 88). |

**New effects.**

*The echo picture (the main proposal).* What the person would see: the camera image fades almost to black, and the scene is drawn again as pale light where surfaces face the phone, brightest for what is near and in the middle, dimming with distance and at the cone's edge, and gone beyond the bat's reach. The picture is a strobe: each call paints one fresh frame, which then darkens until the next call, about four times a second while nothing is near. When something sits close in the middle of the view, the calls quicken to 20 to 80 a second and then to a buzz near 170, so the strobe runs together into a steady image just before the catch (log 55, 56, 65). Distance is drawn in steps, coarse while searching and fine while closing in, so the search picture looks like contour bands and the approach picture smooths out (log 57: about 15 cm against 1.5 cm). The cone is about 60 degrees across in search, about the width of the screen, and widens a little in the buzz (log 58, 65, 66). Small things that move become sparks, because a moving insect's echo changes from call to call; that drawing is **invented** and uses the engine's motion map. In dusk light, a faint, very blurred and nearly colourless camera image sits under the echoes, and it fades out as the scene darkens, so the bat's eyes and ears share the picture at dusk and the echoes take over at night (log 61, 86). The way the image and the echoes are weighted by light is **invented**, and it uses the frame's mean brightness, which the engine already computes for `gain`.

Which phone input could stand in. A phone cannot hear bat calls (ecoObs FAQ), so the stand-in must be a sense of distance, and there are four:

1. *A depth model on the camera image.* Monocular depth estimation predicts depth from a single image; Depth Anything V2 gives relative depth and ZoeDepth absolute depth (Hugging Face documentation, opened today). The app already runs image models in the page. The bat helps here: a searching bat renews its picture only about four times a second, so a depth model that manages a few frames a second matches the animal (log 67). That match is my own observation. Speed on a phone was not measured.
2. *The phone's depth camera.* Apple's Pro iPhones have carried a LiDAR scanner since 2020, measuring up to 5 m (phyphox, opened today), about a bat's reach for insects (log 60). It needs native code in `native/ios-shell`, which today only hosts a web view.
3. *ARCore's Depth API on Android.* It builds depth images from motion, adds a time-of-flight sensor where one exists, covers 0 to 65 m and is most accurate from 0.5 to 5 m, with the same field and timestamps as the camera image; only some phones support it (Google's ARCore documentation, opened today). The WebXR Depth Sensing Module (an Editor's Draft of 25 August 2026) lets a web page read such depth buffers inside an immersive session. Whether the Android shell's web view offers that session was not checked.
4. *Real echoes from the phone itself.* FingerIO sent inaudible sound at 18 to 20 kHz from a Samsung Galaxy S4's own speaker and tracked a finger to about 8 mm across about half a square metre with the phone's own microphones (Nandakumar, Iyer, Tan and Gollakota, CHI 2016, opened today). That reaches far less than a bat does, at a quarter of a bat's pitch, and it asks for the microphone. As an optional "near echoes" mode it would make the phone ping, which is the most truthful stand-in on offer and the least practical.

How hard. The drawing is a new mode: depth to brightness with a fall-off, a cone mask, quantized depth, a frame held and dimmed between calls, a call rate that rises as the nearest central depth shrinks, and a blend with the blurred camera image. All of it is shader work on one depth texture, and the hold already exists for the heron. The depth source is the hard part: medium with a small model in the page (cost to be measured), hard with LiDAR or ARCore because the shells need native code.

What would make it beautiful as well as true: one cold colour on black, like moonlight on frost, with the contour bands of search giving way to smooth relief as a target nears, and the strobe audible as rhythm on screen. The approach and buzz give the view a climax that no other view has.

*A sharp band above centre.* The bats measured see best through the low back of the retina (log 70; and a dorsal area in Daubenton's bat, log 74), which would look up and forward. The engine places sharpness only at the centre or along the horizon. A vertical offset for `topoA` or `topoS` would draw it; this is easy once a scientist confirms where the area looks (section 8).

### `flyingfox` (family Pteropodidae)

**Rows.**

1. `['m', 'Sharpness', 'Grey-headed and black flying foxes see about 4 cycles per degree, a fifteenth of your sharpness and several times an insect-eating bat's. The view is blurred to match.']`
   Log 75 (Cechetto and colleagues 2020: *Pteropus alecto*, *P. poliocephalus* and *Rousettus aegyptiacus*); log 76 (Murugavel and colleagues 2022: Indian flying fox 4.0, *Cynopterus sphinx* 2.7, *Rousettus leschenaultii* 2.8).
2. `['m', 'Colour', 'Flying foxes have two kinds of colour-sensing cells, one sensitive to blue and one to green, as most mammals do. The view shows colours the way a person with only two kinds sees them.']`
   Log 146 (Müller, Goodman and Peichl 2007: three *Pteropus* species).
3. `['m', 'Built for dusk', 'Colour cells make up less than one in a hundred of a flying fox's light-sensing cells, and the rest are rods, the cells that work in dim light. Colour is muted here and the shadows are lifted.']`
   Log 148 (cones 0.25 to 0.6% of photoreceptors; rods 350,000 to 800,000 per square millimetre).
4. `['m', 'Fruit bats without blue', 'Rousettes, epauletted fruit bats and the African fruit bats related to the straw-coloured fruit bat have only the green-sensitive kind and see no colour. When the app knows one of these species, the view turns grey.']`
   Log 147 (*Rousettus madagascariensis*, *Eidolon dupreanum*, *Epomophorus gambianus*). The straw-coloured fruit bat itself (*Eidolon helvum*) was not measured, so for it the row stands at `g`.
5. `['m', 'Looking forward', 'A flying fox's two eyes share a field 54 degrees wide in front of it, and its brain joins the two eyes' views in the way a primate's brain does.']`
   Log 149 (Rosa and Schmid 1994); log 151 (Pettigrew 1986).
6. `['m', 'Mirror behind the eye', 'In the straw-coloured fruit bat a reflecting layer lines a rippled retina and sends light back through the light-sensing cells for a second chance to catch it.']`
   Log 79 (Peter-Ajuzie and colleagues 2021).
7. `['m', 'No calls', 'Flying foxes make no echolocation calls. Like most fruit bats of Africa, Asia and Australia, they find their way and their food by sight and smell.']`
   Log 75 (both *Pteropus* species are non-echolocating); log 168 (Boonman and colleagues 2013).
8. `['x', 'Clicks', 'Rousettes find their way in the dark with clicks of the tongue, and they click faster and louder as the light fades. This view draws no echoes.']`
   Log 81 (Danilovich and Yovel 2019); log 152 (rousette hearing 2.25 to 64 kHz).
9. `['x', 'Smell', 'A flying fox finds ripe fruit and flowers partly by scent, which this view leaves out.']`
   Log 168.
10. `['i', 'Field of view', 'No measurement of a flying fox's whole field was found. The view keeps the camera's field.']`

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who`, `cue` | 'Flying fox, fruit bat', 'a flying fox', 'The picture is coarse and muted, and the shadows are lifted.' | The app's wording, from the earlier sheet. |
| `cpd` | 4 | Log 75, 76. |
| `M` | DEUTAN | A two-cone model with S and L cones (log 146). The choice of the deutan matrix is **invented**, and SOURCES.md lists the two-cone arithmetic as unchecked. The long-wave cone's peak in flying foxes was not found. |
| `sat` | 0.6 | **Invented**, after a cone share under 1% (log 148); lower than the earlier sheet's 0.7 because the rod share is now measured directly. |
| `gain` | 1.5 | **Invented**; rods and a tapetum (log 148, 79). |
| `pupil` | 'o' | The straw-coloured fruit bat's pupil is round (log 80); `g` for *Pteropus*. |
| `topoA`, `fall` | 1 and 1.0 | A temporal area in all three Indian species (log 77), which looks forward; Rousettus's field of best vision is 27 degrees wide (log 150). `fall` is **invented**. |
| `fov` | unset | No whole-field measure (row 10). The 54-degree binocular field (log 149) would set a sharper central overlap in a future zone. |
| Variant for *Rousettus*, *Eidolon*, *Epomophorus* | `M`: GREYL = [.35, .55, .1, .35, .55, .1, .35, .55, .1], `sat` 0 | One green-sensitive cone (log 147). The weights are **invented**, since the cone's peak was not found. |

**New effects.** *Colour by genus*, the same mechanism the jumping spider draft asks for: when the full database names a *Rousettus*, *Eidolon* or *Epomophorus* species, the view switches to the grey matrix. It is easy (a per-genus override of `M` and `sat`). *A forward overlap zone*: a sharper, slightly brighter central region 54 degrees wide where both eyes overlap (log 149), drawn with the engine's new zones; easy, and invented in its exact edge.
