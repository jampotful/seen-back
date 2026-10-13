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

### Whales, dolphins, seals and manatees: water, air and rods

**How sight under water and in air differ.** A land mammal's cornea does much of its focusing, because light bends where air meets the eye. Under water the cornea adds little, so marine mammals focus with a powerful, nearly spherical lens and are sharp-sighted when submerged (log 19, 161, 170). In air the cornea's extra power then makes the eye short-sighted (log 34). Seals counter this with a centrally flattened cornea and a pupil that closes to a vertical slit and then a pinhole in bright light, and dolphins with a pupil that closes to two small slits (log 25, 34). In bright light, harbour seals and bottlenose dolphins resolve gratings about equally well in air and in water (log 24, 35). In dim light the pupil opens, the correction weakens, and the seal's acuity in air falls with the light; Hanke and Dehnhardt (2009) measured that decline, and only its title was readable here (wanted list). Under water, murk blurs a harbour seal's sight fast (log 40), and depth dims and blues the light: in clear ocean, blue light falls tenfold every 70 m and the sun's light is gone below about 1,000 m, where glowing animals are the only light (log 97). Coastal waters absorb blue instead (log 18, note).

What this means for the picture. A phone is almost always in air, so each of these views shows the animal's sight in air, the way a seal on a beach or a dolphin beside a boat sees the person holding the phone. In bright scenes the view is coarse but evenly sharp, with deep focus from the pinhole; as the scene darkens, the blur and the shallow focus grow. A switch marked "Under water" (the app's own invention) removes the dim-air blur and adds the water's own effect on light: a haze and a blue-green cast that deepen with a depth or murkiness the person chooses (log 40, 97).

**What rod-only and cone-poor retinas mean.** Seals and toothed whales keep one kind of cone, the green-sensitive one, beside their rods (log 5). A single kind of cone cannot compare colours, so in daylight the picture has no hue at all, and the grey is weighted by that one pigment: near 510 nm in the harbour seal and 522 to 531 nm in dolphins and porpoises, both well short of a land mammal's long-wave cone near 555 nm (log 9, 10, 15). My inference from those peaks is that reds look darker to a seal or a dolphin than to a dog. In dim light, comparing the cone with the rods may give back a little colour (log 16, 18), so the seal view keeps a faint tint in dim scenes, an invented strength. Baleen whales and sperm whales have no working cones at all, only rods tuned near 479 to 493 nm (log 1 to 4, 11 to 13), so their grey sits bluer still. In land mammals, rods alone mean coarse sight in dim light and dazzle in bright light (log 142). Whether whale rods are dazzled at the sunlit surface is unknown, so the `whale` view adds only a mild glare (invented) and the question goes to a specialist (section 8). Manatees keep two kinds of cone (log 17) and keep some colour.

### `whale` (baleen whales, and any whale, dolphin or seal named only to its group)

**Rows.**

1. `['m', 'No colour', 'Humpback whales and the other rorquals, grey whales, right whales and sperm whales have lost the genes for both kinds of colour-sensing cell. They see with rods alone, the cells people use at night, so this view is grey.']`
   Log 1 to 3 (Meredith and colleagues 2013, genes); log 4 (Schweikert and colleagues 2016: no cone opsin in the bowhead retina).
2. `['m', 'Seals and dolphins too', 'Seals, sea lions, dolphins and porpoises have kept just one kind of colour-sensing cell, so they too see the world in greys.']`
   Log 5, 6 (Peichl, Behrmann and Kröger 2001: seven toothed whales and five seals and sea lions); log 95 (Land and Nilsson 2012).
3. `['m', 'Tuned to the sea', 'A humpback whale's eye is most sensitive to blue-green light near 492 nanometres. In clear ocean water, blue light reaches deepest. The grey of this view is weighted toward blue-green.']`
   Log 13 (humpback retina, Dartnall 1962 as reviewed); log 12; log 97.
4. `['m', 'Sharpness', 'A humpback whale's eye resolves about 4 cycles per degree, a fifteenth of your sharpness. It can make out the outline of a large animal far off, and loses fine detail beyond three or four body lengths.']`
   Log 29 (Bolin and colleagues 2025).
5. `['m', 'Two sharp areas', 'A humpback whale sees best in two areas of its view, one ahead of it and one out to the side and behind.']`
   Log 158 (Lisney and Collin 2018); log 21.
6. `['g', 'Built for water', 'The eyes of whales, seals and manatees focus sharply under water. In air most of them would be short-sighted, and most have ways to correct it.']`
   Log 19 (Mass and Supin 2007, a review); log 170.
7. `['m', 'Mirror behind the eye', 'Whales have a reflecting layer behind the retina that shines blue-green and gives dim light a second pass through the eye. The shadows are lifted here.']`
   Log 159 (humpback and Bryde's whales); log 160 (pygmy sperm whale and bottlenose dolphin).
8. `['x', 'Depth of the sea', 'Under water, light fades with depth. In the clearest ocean, blue light falls tenfold every 70 metres, and below about a kilometre the only light comes from glowing animals. This view cannot tell how deep the water is.']`
   Log 97 (Land and Nilsson 2012).

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who`, `cue` | 'Whale, dolphin, seal', 'a whale', 'The world in greys, coarse, and lifted from the shadows.' | The app's wording. |
| `cpd` | 4 | Humpback 3.95 (log 29); within the seal and dolphin ranges (log 22, 39). |
| `M` | GREY490 = [.05, .6, .35, .05, .6, .35, .05, .6, .35] | Rods near 484 to 493 nm (log 12, 13). The weights are **invented**: equal rows give grey, and the weighting toward the camera's green and blue stands in for a blue-green pigment. |
| `sat` | 0 | Log 1 to 6. |
| `gain` | 1.5 | **Invented**; reflecting layers (log 159, 160). |
| `pupil` | 'v' | Seals and dolphins close their pupils to slits (log 25, 34); baleen whale pupils were not found, so `g` for them. |
| `topoS`, `fall` | 0.5 and 1.0 | Two sharp areas, ahead and to the side and back (log 158, 21); the band is the engine's nearest shape, and the values are **invented**. |
| `glare` (new) | 0.3 | **Invented**; rod-only retinas are dazzled in land mammals (log 142), and whales are unmeasured. |
| `fov`, `dof`, `rate` | unset | No whale field, pupil size or flicker rate found. |

### `seal` (seals, sea lions and the walrus)

**Rows.**

1. `['m', 'One kind of colour cell', 'Seals and sea lions have lost the blue-sensitive colour cell. A harbour seal's single kind is most sensitive near 510 nanometres, a blue-green, so in daylight it sees no colour at all and this view is grey.']`
   Log 5 (Peichl and colleagues 2001); log 15, 16 (Crognale and colleagues 1998).
2. `['g', 'Colour at dusk', 'In dim light, when its rods and its one kind of colour cell both work, a seal may tell some colours apart by comparing the two. This view keeps a faint tint in dim scenes, and the strength of that tint is the app's guess.']`
   Log 16, 18 (Griebel and Peichl 2003).
3. `['m', 'Sharpness', 'In tests in clear water, harbour seals resolved stripes between a tenth and a twenty-fifth as fine as you can. Their retinas could support finer sight, about 11 cycles per degree under water and 9 in air.']`
   Log 39 (Weiffen and colleagues 2006: 5.5 and 12.7 minutes of arc, two seals); log 27 (Hanke, Peichl and Dehnhardt 2009); log 26 (harp seal 9 to 11 under water); log 33 (single targets of about 0.3 degree under water, Sandow and colleagues 2026).
4. `['m', 'Water and air', 'A seal's eye is built to focus under water. In air its cornea blurs the picture, and in bright light its pupil closes to a slit and then a pinhole that sharpens it again. This view sharpens in bright scenes and blurs as the light fades.']`
   Log 34, 35 (Sandow and colleagues 2026, summarizing earlier work). How fast the blur grows as light falls is **invented** until Hanke and Dehnhardt 2009 is read (wanted list).
5. `['m', 'Field of view', 'A harbour seal takes in about 208 degrees around itself without moving its eyes, and both eyes see the middle 67 degrees. Its view reaches high overhead, toward the surface of the water.']`
   Log 36 to 38 (Hanke, Römer and Dehnhardt 2006).
6. `['m', 'Murky water', 'Cloudy water blurs a harbour seal's sight quickly, and each step of murkiness takes away a large share of what it can make out.']`
   Log 40 (Weiffen and colleagues 2006).
7. `['m', 'Dim light', 'Harbour seals and California sea lions adjust to darkness faster than people and see in dimmer light. Elephant seals, which hunt deeper, adjust in half their time and see in dimmer light still. The shadows are lifted here.']`
   Log 30, 31 (Levenson and Schusterman 1999); log 32 (pupils); log 20, 161 (reflecting layers).
8. `['m', 'Hearing in two worlds', 'A harbour seal hears low sounds almost as well in air as under water. A California sea lion hears best in air, and an elephant seal best under water.']`
   Log 47 (Kastak and Schusterman 1998).
9. `['x', 'Whiskers', 'A seal can follow the invisible trail of water that a swimming fish leaves behind, by its whiskers alone, even when the trail is tens of seconds old. Wild elephant seals hunt this way in the dark of the deep sea. The picture leaves this sense out.']`
   Log 42 (Dehnhardt and colleagues 2001), 43, 44 (Adachi and colleagues 2022).

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who`, `cue` | 'Seal, sea lion, walrus', 'a seal', 'Sharper in bright light; softer as the light fades.' | The app's wording. |
| `fov` | 208 | Log 36. |
| `cpd` | 5 | Behavioural 2.4 to 5.5 under water (log 39); anatomical 8.7 in air and 11.5 under water (log 27). The pick of 5 within that span is **invented**. |
| `topoA`, `topoS`, `fall` | 0.7, 0.3 and 1.2 | An area centralis with a moderate streak running from it (log 28); the weights are **invented**. |
| `pupil` | 'v' | Log 34. |
| `dof` | 16, scaled by light (new) | **Invented** strength; the pinhole gives deep focus in bright light and the open pupil shallow focus in dim light (log 34, 98). |
| `M` | GREY510 = [.15, .65, .2, .15, .65, .2, .15, .65, .2] | One cone near 510 nm (log 15). The weights are **invented**. |
| `sat` | 0, rising to 0.15 in dim scenes (new) | Log 16, 18; the 0.15 is **invented**. |
| `gain` | 1.5 | **Invented**; reflecting layer and fast dark adaptation (log 20, 31). |
| `rate`, `persist`, `gate` | unset | No seal flicker rate found. |

### `dolphin` (toothed whales: dolphins, porpoises, sperm and beaked whales, belugas, river dolphins)

**Rows.**

1. `['m', 'One kind of colour cell', 'Dolphins and porpoises have lost the blue-sensitive colour cell. A bottlenose dolphin's remaining kind is most sensitive near 524 nanometres and its rods near 488, so this view is grey. Sperm whales have lost both kinds of colour cell.']`
   Log 5 (Peichl and colleagues 2001); log 8, 9 (Fasick and Robinson 2016); log 3 (Meredith and colleagues 2013); log 14 (a dolphin failed tests of colour, Madsen 1976 as reviewed).
2. `['m', 'Sharpness', 'A bottlenose dolphin's retina resolves about 9 minutes of arc under water and 12 in air, roughly a twentieth of your sharpness. This view is blurred to match.']`
   Log 22 (Mass and Supin 1995).
3. `['m', 'Two sharp areas', 'A dolphin sees best in two areas of its view, one ahead of it and one out to the side and behind. This view sharpens the middle and the far edges of the picture.']`
   Log 23 (Mass and Supin 1995: two high-density spots in the temporal and nasal retina); log 21.
4. `['m', 'Water and air', 'In bright daylight a bottlenose dolphin sees about as well in air as under water. Its pupil closes to two small slits, and they cancel most of the blur its eye would otherwise have in air.']`
   Log 24, 25 (Herman and colleagues 1975).
5. `['m', 'Sound beam', 'A dolphin or porpoise probes the water ahead with clicks sent in a narrow beam, about 20 to 40 degrees across, and clicks faster as it closes in. By echoes alone, a bottlenose dolphin can tell apart two objects 1.5 degrees apart.']`
   Log 49 (Wisniewska and colleagues 2015: off-axis angles doubled; see its note); log 54 (Jensen and colleagues 2009); log 48 (Branstetter and colleagues 2022).
6. `['m', 'Looking ahead', 'A wild finless porpoise checks the water up to 77 metres ahead with its clicks, then swims on in silence for less than 20 metres before it checks again.']`
   Log 51 (Akamatsu and colleagues 2005).
7. `['m', 'Mirror behind the eye', 'A bottlenose dolphin has a reflecting layer behind its retina, made of fine fibres that shine blue and green. The shadows are lifted here.']`
   Log 160 (Young and colleagues 1988).
8. `['x', 'Clicks', 'A porpoise clicks at about 130 to 140 thousand vibrations a second and listens to the echoes. The picture leaves this sense out until the app can draw echoes.']`
   Log 50 (Kyhn and colleagues 2013).
9. `['x', 'Electric sense', 'Guiana dolphins sense weak electric fields through small pits on the snout where whiskers once grew. The picture leaves this sense out.']`
   Log 41 (Czech-Damal and colleagues 2011).

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who`, `cue` | 'Dolphin, porpoise', 'a dolphin', 'Grey and coarse, sharpest ahead and at the far edges.' | The app's wording. |
| `cpd` | 3 | Log 22 (2.5 in air, 3.3 under water). |
| `M` | GREY524 = [.2, .65, .15, .2, .65, .15, .2, .65, .15] | One cone near 524 nm (log 9). The weights are **invented**. |
| `sat` | 0 | Log 5, 14. |
| `gain` | 1.4 | **Invented**; reflecting layer (log 160). |
| `pupil` | 'v', then 'w' (new) | Two slits (log 25); 'v' is the engine's nearest shape until a double-slit pupil exists. |
| `dof` | 10, scaled by light (new) | **Invented**, as for the seal. |
| `topoA` | 0.6, plus sharp edges (new zones) | Two sharp areas (log 23); values **invented**. |
| `fov` | unset | The beluga's visual field (Mass 2001) is on the wanted list. |

### `manatee` (manatees and dugongs)

**Rows.**

1. `['g', 'Colour', 'Manatees and dugongs have two kinds of colour-sensing cells, as most land mammals do. This view shows colours the way a person with two kinds sees them.']`
   Log 17 (Griebel and Peichl 2003, a review). The manatee's own pigment peaks (Newman and Robinson 2006) are on the wanted list.
2. `['m', 'Sharpness', 'In tests, the sharper-eyed of two Florida manatees made out stripes about 21 to 24 minutes of arc wide in bright light, about a fortieth of your sharpness. The other manatee saw much less. This view is blurred to match the first.']`
   Log 45 (Bauer and colleagues 2003).
3. `['m', 'No closer look', 'The same manatee saw no better when it swam to within 30 centimetres of a target, which suggests that manatees use their eyes for larger things at a middle distance.']`
   Log 45 (same abstract).
4. `['g', 'Built for water', 'A manatee's eye focuses sharply under water.']`
   Log 19 (Mass and Supin 2007).
5. `['x', 'Touch all over', 'A Florida manatee has about 1,500 sensitive hairs on each side of its body, a few centimetres apart. They may let it feel currents and nearby animals in murky water, as a fish feels them with its lateral line. The picture leaves this sense out.']`
   Log 46 (Reep, Marshall and Stoll 2002).
6. `['i', 'Field, pupil and dim light', 'No measurements were found for these. The view keeps the camera's field and draws a round pupil.']`

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who`, `cue` | 'Manatee, dugong', 'a manatee', 'Two colours, and very coarse.' | The app's wording. |
| `cpd` | 1.3 | Log 45 (1.25 to 1.43). The engine's lowest `cpd` today is 1 (bees); at 1.3 a phone screen of 24 degrees holds about 31 cycles. |
| `M` | DEUTAN | Two cones (log 17); the choice of matrix is **invented**. |
| `sat` | 0.8 | **Invented**. |
| `pupil` | 'o' | **Invented** (row 6). |

### New effects for the whale group

| Effect | What the person would see | Phone input | How hard | Evidence |
|---|---|---|---|---|
| Blur and focus set by light (`seal`, `dolphin`) | In daylight the grey picture is coarse but evenly sharp, everything in focus; indoors or at dusk it softens and the background melts. | The frame's mean brightness, already computed for `gain`; the phone's light sensor where the browser exposes it. | Easy: scale `inv` (blur) and `dof` by a curve of brightness. The curve is invented until Hanke and Dehnhardt 2009 is read. | Log 24, 34, 35, 98 |
| Double-slit pupil (`dolphin`) | Out-of-focus lights split into two side-by-side blurs, a quiet signature of the dolphin's eye. | None. | Medium: a two-lobe blur kernel along one axis, in the pass that draws `pupil`. | Log 25 |
| Two sharp zones (`dolphin`, `whale`) | The middle and the far left and right edges are sharp, and the rest is softer. With `fov` above 180 the edges hold what lies to the side and behind. | None. | Medium, with the engine's new zones. | Log 21, 23, 158 |
| Under water (`whale`, `seal`, `dolphin`, `manatee`) | A switch adds a blue-green haze that thickens with a chosen depth, and a murk slider that blurs (the seal's sight falls fast with murk). | A button and a slider; nothing can sense the water. | Easy. The mapping from depth to haze is invented, though tied to blue light falling tenfold every 70 m. | Log 40, 97 |
| Wakes (`seal`, optional) | Anything that moves leaves a slowly fading trail behind it, like ink spreading in water, which lasts many seconds, as a fish's wake lasts for a seal. | The camera's motion map. | Easy to medium: motion-gated `persist` with a long decay. It stands in for a sense of touch and must carry an `i` row. | Log 42 to 44 |
| Sonar beam (`dolphin`) | A narrow cone in the middle of the screen, about a third of its width, lights up as an echo picture refreshed click by click; outside the cone the grey eye image stays. The clicks quicken as something nears the centre. | The same depth sources as the bat's echo picture. | Hard, as for bats; it reuses the bat's machinery with a narrower cone and a longer reach. | Log 49, 51, 54 |
| Glare (`whale`; and the rods-only variant of `raccoon`) | Bright parts of the scene bloom and wash toward white. | The frame's brightness. | Easy: highlight compression with bloom. | Log 142 |

### `primate` (Old World monkeys, apes and howler monkeys; also any primate named only to its group)

**Rows.**

1. `['m', 'Colour', 'Old World monkeys and apes have three kinds of colour-sensing cells, as people do. In the crab-eating macaque, the primate recorded most often, they are most sensitive near 430, 531 and 561 nanometres, a close match for a person's. This view leaves colour as your camera shows it.']`
   Log 101 to 103 (Baylor, Nunn and Schnapf 1987; the red and green cones matched human colour-matching curves); log 104 (rhesus cones near 536 and 565 nm, rods 502); log 99, 96.
2. `['m', 'Every animal alike', 'Colour vision varies less among Old World monkeys and apes than it does among people. All 25 monkeys tested, from eight species, had the same three kinds of cell.']`
   Log 100 (Jacobs and Deegan 1999); log 105 (Jacobs 1996).
3. `['m', 'Howler monkeys', 'Howler monkeys are the only monkeys of the Americas in which every animal, male or female, sees three colours.']`
   Log 107 (Carvalho and colleagues 2017); log 108 (Silveira and colleagues 2014).
4. `['m', 'Sharpness', 'A chimpanzee sees about as much detail as a person, and a rhesus macaque a little less in bright light. Monkeys and apes that are active by day resolve 30 to 75 cycles per degree. This view keeps your sharpness.']`
   Log 91 (64 cycles per degree, Spence 1934 as Caves and colleagues 2018 report), 118 (Matsuzawa 1990), 119 (Cavonius and Robbins 1973), 114 (Veilleux and Kirk 2009).
5. `['m', 'Night sight', 'In very dim light a rhesus macaque makes out finer detail than a person does.']`
   Log 119.
6. `['g', 'No eye shine', 'Like people, monkeys and apes have no reflecting layer behind the retina, so their eyes do not shine back at a torch at night.']`
   Log 129 (Ollivier and colleagues 2004), 165 (Pirie 1959).
7. `['x', 'Smell', 'Apes, Old World monkeys and howler monkeys carry more broken genes for smell than other monkeys and lemurs, a loss that came about alongside full colour vision. The picture leaves smell out.']`
   Log 164 (Gilad and colleagues 2004).
8. `['i', 'Field of view and pace', 'No measurement of field of view or of the speed of sight was found for monkeys or apes. The view keeps the camera's field and your pace.']`

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who`, `cue` | 'Monkey, ape', 'a monkey or ape', 'Three colours and sharp sight, much as yours.' | The app's wording. |
| `cpd` | unset (60) | Log 91, 114, 118. |
| `M`, `sat` | unset (identity) | Log 101 to 103. |
| `gain` | unset | No reflecting layer (log 129, 165). |
| `pupil` | 'o' | **Invented**; no primate pupil source was opened, and it has no effect without `dof`. |
| `fov`, `topoA`, `rate` | unset | Row 8. |

This view changes almost nothing, and that is the finding. Its interest lies beside `capuchin` and `lemur`, where the same order splits three ways in colour and more than tenfold in sharpness. A comparison card that shows one scene through all three primate views would teach that at a glance; it needs no engine work.

### `capuchin` (New World monkeys except howler and owl monkeys)

**Rows.**

1. `['g', 'Two colours or three', 'In capuchins, spider monkeys, squirrel monkeys and marmosets, every male sees with two kinds of colour-sensing cells, like a person who confuses reds and greens. Some females have three kinds and see colour as you do. This view shows the two-colour version, and a tap shows the three-colour one.']`
   Log 106 (Carvalho and colleagues 2017), 105 (Jacobs 1996). The tap is the app's own.
2. `['m', 'Which two', 'A male's longer-wave cell may peak anywhere from about 535 to 563 nanometres, depending on which form of the gene he carries, so two males of one species can see reds and greens differently.']`
   Log 106 (capuchins and squirrel monkeys: 563, 550 and 535 nm).
3. `['m', 'Smelling instead', 'Wild white-faced capuchins that cannot tell red from green sniff fruit more often than those that can.']`
   Log 163 (Melin and colleagues 2019, 75 wild monkeys). The white-faced capuchin is the fifth most recorded primate.
4. `['m', 'Sharpness', 'A common marmoset resolves about 30 cycles per degree, half your sharpness. This view is blurred to match.']`
   Log 117 (Troilo, Rowland and Judge 1993). For capuchins and spider monkeys the value is `g`.
5. `['g', 'No eye shine', 'Like other monkeys, these have no reflecting layer behind the retina.']`
   Log 129.
6. `['x', 'Scent of ripe fruit', 'Capuchins judge fruit partly by smell, and they sniff more often at fruits whose scent grows as they ripen. The picture leaves smell out.']`
   Log 163.
7. `['i', 'Field of view and pace', 'No measurement of field of view or of the speed of sight was found for these monkeys. The view keeps the camera's field and your pace.']`

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who`, `cue` | 'Capuchin, spider monkey, marmoset', 'a New World monkey', 'Two colours for every male; tap for a female's three.' | The app's wording. |
| `cpd` | 30 | Marmoset (log 117). |
| `M` | DEUTAN, and identity on a tap (new) | Log 106. A male with the 563 nm form lacks a cell near 530 nm and resembles a person missing the green-sensitive cone, which the deutan matrix models; a male with the 535 nm form resembles the protan case. The default and the tap are **invented**. |
| `pupil`, `gain`, `fov` | 'o', unset, unset | **Invented** pupil; no reflecting layer (log 129). |

**New effect.** *The colour coin.* The polymorphism is the most interesting fact about these monkeys: in one troop, some animals see a red fruit against green leaves and others do not (log 106, 163). A tap that switches between the male's two-colour view and a female's three-colour view, with a short line saying which is shown, makes that visible. A second tap could switch to the protan-like male. Easy: it swaps `M`.

### `lemur` (lemurs, lorises, galagos, tarsiers and owl monkeys)

**Rows.**

1. `['m', 'Colour', 'Ring-tailed lemurs and brown lemurs have two kinds of colour-sensing cells, most sensitive near 437 and 545 nanometres, like a person who confuses reds and greens. This view shows colours that way.']`
   Log 111 (Jacobs and Deegan 1993), 112 (Jacobs and Deegan 2003), 113 (Valenta and colleagues 2015).
2. `['g', 'A few with three', 'In a few lemurs, among them sifakas, the red ruffed lemur and the blue-eyed black lemur, some females have a third kind and see three colours.']`
   Log 110 (Carvalho and colleagues 2017).
3. `['g', 'No colour', 'Owl monkeys, lorises, galagos and several tarsiers have lost the blue-sensitive cell and see no colour at all. When the app knows one of these animals, the view turns grey.']`
   Log 109 (Carvalho and colleagues 2017).
4. `['m', 'Sharpness', 'A blue-eyed black lemur resolves about 4 to 5 cycles per degree, a twelfth to a fifteenth of your sharpness, and a tarsier's eye could resolve about 9. This view is blurred to about 4.']`
   Log 115, 116 (Veilleux and Kirk 2009).
5. `['g', 'Golden eye shine', 'Lemurs and galagos have a reflecting layer behind the retina made of crystals of riboflavin, a vitamin. It gives their eyes a golden shine in torchlight and gives dim light a second pass through the eye. The shadows are lifted here.']`
   Log 165 (Pirie 1959), 129 (the second pass, Ollivier and colleagues 2004).
6. `['g', 'Night against day', 'Primates that are active at night see less detail than those active by day, because their eyes trade sharpness for sensitivity.']`
   Log 93 (Caves and colleagues 2018), 114.
7. `['x', 'Smell', 'Lemurs keep more working genes for smell than monkeys and apes do. The picture leaves smell out.']`
   Log 164 (Gilad and colleagues 2004).

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who`, `cue` | 'Lemur, loris, galago', 'a lemur', 'Two colours, coarse detail, and the shadows lifted.' | The app's wording. |
| `cpd` | 4 | Log 115. |
| `M` | DEUTAN | Two cones (log 111); the matrix is **invented**. |
| `sat` | 0.8 | **Invented**. |
| `gain` | 1.6 | **Invented**; riboflavin tapetum (log 165). |
| `pupil` | 'o' | **Invented**. |
| Variant for Aotidae, Lorisidae, Galagidae, Tarsiidae | `M`: GREY545 = [.3, .6, .1, .3, .6, .1, .3, .6, .1], `sat` 0 | One cone (log 109); the weights are **invented**, since these animals' cone peaks were not found. Tarsiers have no reflecting layer in the sources read here, so the variant keeps `gain` at 1.6 only for lorises and galagos; that split is a gap (section 5). |

### `mammal` (two kinds of cone: bears, otters, weasels, skunks, mongooses, coatis, kangaroos, koalas, possums, pigs, hippos, rhinos, elephants, hedgehogs, shrews, platypus, echidnas and others)

**Rows.**

1. `['m', 'Colour', 'Most mammals have two kinds of colour-sensing cells, where people have three. A pig's are most sensitive near 439 and 556 nanometres and an elephant's near 419 and 552, the same pair as a person who confuses reds and greens. This view shows colours that way.']`
   Log 124 (Jacobs 2013), 125, 126 (Neitz and Jacobs 1989), 134 (Yokoyama and colleagues 2005).
2. `['m', 'Bears, otters and kangaroos', 'American black bears, European otters and tammar wallabies have the same two kinds. In black bears the longer-wave cells outnumber the blue-sensitive ones by at least three to one.']`
   Log 127 (Heyward and colleagues 2020), 7 (Peichl and colleagues 2001), 139 (Ebeling, Natoli and Hemmi 2010).
3. `['g', 'Some marsupials differ', 'A few small Australian marsupials, among them the fat-tailed dunnart, may have a third kind of colour cell. No measurement was found for koalas or possums.']`
   Log 139.
4. `['m', 'Sharpness', 'Sharpness varies widely in this group. A tammar wallaby resolves about 5 cycles per degree, a numbat 5 to 6 and a black rhinoceros about 6, and an African elephant's retina could support about 14. This view is blurred to about 6, a tenth of your sharpness.']`
   Log 140 (Hemmi and Mark 1998), 137 (Arrese and colleagues 2000), 136 (Pettigrew and Manger 2008), 132 (Pettigrew and colleagues 2010).
5. `['m', 'Field of view', 'Eyes set on the sides of the head take in a wide view. A ferret sees about 270 degrees around itself and numbats and honey possums about 240, with 60 to 80 degrees seen by both eyes. This view bends the picture at its edges to suggest that sweep.']`
   Log 144, 145 (Morris and colleagues 2025), 137, 138 (Arrese and colleagues 2000, 2002).
6. `['m', 'Sharpest band', 'Rhinoceroses and elephants see most sharply along a band level with the horizon, with finer spots at its ends, and a black bear sees most sharply in a spot ahead of it. This view sharpens a band across the middle of the picture.']`
   Log 136, 132, 128.
7. `['g', 'Dim light', 'Bears, otters and other carnivores, elephants and some marsupials have a reflecting layer behind the retina, while pigs and red kangaroos have none. The shadows are lifted a little here.']`
   Log 129 (Ollivier and colleagues 2004), 133.
8. `['x', 'Electric sense', 'A platypus hunts under water with its eyes and ears shut, finding prey with electric and touch sensors in its bill. The picture leaves this sense out.']`
   Log 153 (Manger, Calford and Pettigrew 1996).
9. `['x', 'Rumbles in the ground', 'The footfalls and deep calls of elephants send vibrations through the ground that can travel for kilometres over sand. Whether and how far elephants feel them was not measured in the work read here, and the picture leaves them out.']`
   Log 157 (Mortimer and colleagues 2018).
10. `['i', 'Pupil and pace', 'No measurement of pupil shape or of how fast these animals see flicker was found. The view draws a round pupil and keeps your pace.']`

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who`, `cue` | 'Bear, otter, kangaroo, pig', 'a mammal', 'Two kinds of colour sensor, a wide view, and less detail than yours.' | The app's wording, after the earlier sheet. |
| `fov` | 260 | Ferret 271, numbat and honey possum about 240 (log 144, 137, 138). The pick within that span is **invented**. |
| `cpd` | 6 | Tammar 4.8, numbat 5.2 to 6.3, rhinoceros 6, elephant 13 to 14 anatomical and 0.6 behavioural (log 140, 137, 136, 132, 135). The pick is **invented**, and the commonest members (raccoon aside, mustelids and bears) are unmeasured. |
| `topoS`, `topoA`, `fall` | 0.7, 0.3 and 1.5 | Streaks in rhinoceros and elephant, a spot in the bear (log 136, 132, 128). The weights are **invented**. |
| `M` | DEUTAN | Two cones (log 124 to 127, 139); the elephant's pair matches a deuteranope's (log 134). SOURCES.md lists the matrix itself as unchecked. |
| `sat` | 0.85 | **Invented**, after the dog's 0.85. |
| `gain` | 1.2 | **Invented**; reflecting layers in carnivores and elephants, none in pigs (log 129, 133). |
| `pupil` | 'o' | **Invented** (row 10). |
| `dof`, `rate` | unset | No source. |

### `raccoon` (one kind of cone or none: raccoons, the kinkajou, the Virginia opossum and pangolins; a rods-only variant for armadillos, sloths and anteaters)

**Rows.**

1. `['m', 'Colour', 'A raccoon has only one kind of colour-sensing cell, where you have three, so it sees brightness without hue. The kinkajou, a relative, is the same. This view is grey.']`
   Log 120 (Jacobs and Deegan 1992).
2. `['m', 'Virginia opossum', 'The Virginia opossum also has a single kind, most sensitive to yellow-green light near 561 nanometres. Opossums of South America have two kinds.']`
   Log 122 (Jacobs and Williams 2010), 123 (Ahnelt, Hokoç and Röhlich 1995).
3. `['m', 'Coatis', 'The coati, a raccoon relative active by day, has a second, blue-sensitive kind of cell, so the app shows a coati's view in two colours.']`
   Log 121.
4. `['g', 'Dim light', 'Raccoons, like other carnivores, have a reflecting layer behind the retina. The Virginia opossum has one in the upper half of its retina, which looks at the ground ahead. The shadows are lifted here.']`
   Log 129, 162 (Braekevelt 1976). Which part of the field the upper retina serves is my inference from the eye's optics.
5. `['m', 'Rods only', 'Armadillos, sloths and anteaters have lost all their colour-sensing cells and see with rods alone, the cells people use at night. When the app knows one of these animals, the view turns grey.']`
   Log 141 (Emerling and Springer 2014).
6. `['g', 'Dazzled by day', 'Eyes that work with rods alone see coarsely in dim light and are dazzled by bright light. For armadillos, sloths and anteaters this view washes out toward white when the scene is bright, and the strength of that glare is the app's guess.']`
   Log 142 (a general description of rod monochromacy in the same paper).
7. `['i', 'Sharpness and field', 'No measurement of sharpness or field of view was found for raccoons, opossums or armadillos. These parts of the view are guesses.']`
8. `['i', 'Drawn as', 'The grey is weighted toward yellow-green, where the opossum's single colour cell is most sensitive, and toward blue-green for the rods-only animals. The weights are the app's own.']`
   Log 122 (561 nm; opossum rods near 493 nm in the same paper's introduction).
9. `['x', 'Hands', 'A raccoon's brain gives its front paws an unusually large share of the area that handles touch. The picture leaves touch out.']`
   Log 166 (Herron 1978).

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who`, `cue` | 'Raccoon, opossum, armadillo', 'a raccoon', 'One kind of colour sensor, or none. The world in greys, with the shadows lifted.' | The earlier sheet's wording. |
| `cpd` | 4 | **Invented** (row 7). |
| `M` | GREY561 = [.4, .55, .05, .4, .55, .05, .4, .55, .05] | One cone near 561 nm (log 122); the earlier sheet's weights, **invented**. |
| `sat` | 0 | Log 120, 122. |
| `gain` | 1.6 | **Invented**; reflecting layers (log 129, 162). |
| `pupil` | 'o' | **Invented**; a sloth's pupil was round after death (log 167). |
| Rods-only variant (Cingulata, Pilosa) | `M`: GREYROD = [.1, .6, .3, .1, .6, .3, .1, .6, .3]; `cpd` 2; `glare` 1.0 (new) | Log 141, 142. All three values are **invented**; no xenarthran rod peak or acuity was found. |

### `mole` (family Talpidae)

**Rows.**

1. `['m', 'Eyes under skin', 'An eastern mole's eyes are covered by a layer of skin, and they probably do little more than tell light from dark.']`
   Log 169 (Townsend 2023, Animal Diversity Web).
2. `['m', 'A tiny working eye', 'A European mole's eye is tiny, with a retina smaller than a square millimetre, yet it holds blue-sensitive and green-sensitive colour cells, and light reaches them down into the ultraviolet.']`
   Log 130, 131 (Glösmann, Steiner, Peichl and Ahnelt 2008). The European mole holds 60.6% of mole records.
3. `['m', 'Ultraviolet', 'The blue-sensitive cell of the European mole is probably tuned to ultraviolet, as it is in mice and other mammals that see ultraviolet.']`
   Log 130, 131.
4. `['i', 'Light, not shapes', 'With so small an eye, a mole probably senses light, its colour and where it comes from more than it sees shapes. This view shows only that, and the reading is the app's own.']`
   Log 130 (retina of 0.75 square millimetres with about 100,000 photoreceptors).
5. `['x', 'Star-nosed mole', 'A star-nosed mole feels its way with 22 fleshy fingers around its nostrils, touching the ground about 13 times a second. It swings the centre of the star onto anything interesting, much as your eyes jump to what catches them. The picture leaves this sense out.']`
   Log 154 (Catania 2011), 155, 156 (Catania and Remple 2003).
6. `['x', 'Nose', 'An eastern mole has a touch-sensitive patch at the tip of its nose and can tell which way a smell comes from. The picture leaves these senses out.']`
   Log 169.

**The picture.**

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who`, `cue` | 'Mole', 'a mole', '' | The app's wording. |
| `pupil`, `field` | 'none', 1 | Rows 1 and 4; the drawing the `plant` and `other` entries use. |
| `M`, `sat` | DEUTAN, 0.4 | The colour of light as an animal with two cones would sense it (log 130). Both are **invented**; the earlier sheet's `sat` of 0 is corrected for European moles. |

**New effect.** *The touch star* (for the star-nosed mole, reached by species). A tap lights a small star-shaped patch of the camera image under the finger for a fraction of a second, uncoloured and fine-grained, flickering about 13 times a second while the finger stays down; the rest of the screen stays a field of light. The flicker rate rests on log 155; the drawing is **invented** and needs an `i` row. Easy.

### New effects for the mammal group

| Effect | What the person would see | Phone input | How hard | Evidence |
|---|---|---|---|---|
| Glare (rods-only variant of `raccoon`) | Bright skies and sunlit surfaces bloom and wash toward white; shade looks clear. | The frame's brightness. | Easy (shared with the `whale` glare). | Log 142 |
| A lower field brightened (Virginia opossum) | The lower half of the picture, where the opossum's reflecting layer looks, is lifted more than the upper half. | None. | Easy: a vertical ramp on `gain`. The mapping is my inference. | Log 162 |
| Ground ripples (`mammal`, elephants only, optional) | When the phone senses a footstep or a thud, rings spread from the bottom of the screen. | The accelerometer. | Easy. It stands in for a sense the work read here did not measure, so it carries an `i` row and waits for a source on elephants' own detection. | Log 157 |
| Electric sparks (`mammal`, platypus only) | Nothing honest: no phone senses fields of a few microvolts per centimetre. | None. | Not possible as measurement. | Log 153 |

## 3. The earlier sheets re-checked

None of this unit's groups has an `EYES` entry yet, so this section checks the two earlier sheets, `docs/views/sheets/mammal.md` and `docs/views/sheets/bat.md`, row by row against sources opened today. "Not reopened" means the row rests on the earlier sheet and its audit, which opened the source on 11 or 12 October.

### `docs/views/sheets/mammal.md`

| Row or number | Verdict | Today's evidence |
|---|---|---|
| Scope: Alachua's five most recorded (raccoon, opossum, wild pig, river otter, eastern mole) | **Confirmed**, which the audit could not do | County CSV: 281, 137, 61, 53, 51. |
| Scope: order counts | **Confirmed** | `docs/views/world-orders.csv`; the Carnivora arithmetic in section 1. |
| `mammal` Colour (pig 439 and 556 nm) | **Confirmed** | Log 125, 126 (Cambridge page). |
| `mammal` Bears and otters | **Confirmed** for the bear (log 127); otters supported by the European otter (log 7) and a review (log 17); the sea otter's genes (Levenson and colleagues 2006) **not reopened** | |
| `mammal` Kangaroos | **Confirmed**, with the missing DOI found: 10.1371/journal.pone.0014231 | Log 139 (full text on disk). |
| `mammal` Platypus and echidnas (`g`) | **Confirmed**, and the platypus half can rise to `m` | Log 124 (SWS2 and LWS in monotremes); log 143 (red- and blue-sensitive cones in the platypus retina). |
| `mammal` Sharpness (blur to 5) | **Corrected** to 6 | Tammar 4.8 confirmed (log 140); added rhinoceros 6 (log 136), numbat 5.2 to 6.3 (log 137), elephant 13 to 14 anatomical (log 132). The western grey kangaroo's 11.2 (Veilleux and Kirk 2014) was **not reopened**. |
| `mammal` Elephants ("about a tenth of your sharpness") | **Corrected** | The behavioural figures stand (log 135), but the African elephant's retina predicts 13.2 to 14.4 cycles per degree (log 132), about a quarter of yours, so the one cow tested probably underperformed her eye. The row should give both. |
| `mammal` Dim light | **Confirmed**, and the authors the earlier sheet could not find are Ollivier, Samuelson, Brooks, Lewis, Kallberg and Komáromy | Log 129. |
| `mammal` Field of view and pupil (`i`) | **Corrected**: the field is now measured in a ferret and two marsupials | Log 144, 137, 138; the pupil is still unmeasured. |
| `mammal` Electric sense | The behaviour is **confirmed** (log 153); the threshold of about 50 µV per cm (Scheich and colleagues 1986) was **not reopened** | |
| `mammal` elephant colour, marked unfinished | **Filled** | Log 134: rod 496, S 419, L 552 nm, like a deuteranope. This also supports the DEUTAN matrix for elephants. |
| `raccoon` Colour | **Confirmed** | Log 120 (Springer page). The raccoon's cone peak is still not given in the abstract. |
| `raccoon` Opossum (561 nm) | **Confirmed**; routing **corrected** | Log 122. South American opossums have two cones (log 123), so only *Didelphis virginiana* goes to `raccoon` (82.4% of opossum records), and the rest of the order goes to `mammal`. |
| `raccoon` Armadillos and sloths | **Confirmed** | Log 141. |
| `raccoon` Anteaters and pangolins | **Corrected** for anteaters; pangolins **not reopened** | The 2014 abstract places rod monochromacy in the stem pilosan, sloths and anteaters together (log 141), so "their other cone is untested" no longer stands. |
| `raccoon` Dim light | **Confirmed**, and the opossum's reflecting layer is placed in the upper retina | Log 129, 162. |
| `raccoon` Sharpness, field and pupil (`i`) | Unchanged | Silveira and colleagues 1982 and Rapaport and colleagues 1981 are on the wanted list. |
| `raccoon` Drawn as (`x`) | **Corrected** to `i` | It describes the app's drawing, which is a guess, and no sense is left out. |
| `mole` Eyes and Light and dark | **Confirmed** for the eastern mole (log 169); **corrected** for the European mole | Log 130: S and M cones, an eye that passes ultraviolet. European moles hold 60.6% of mole records. |
| `mole` Snout (`x`) | **Confirmed** | Log 169. |
| Picture: `mammal` `cpd` 5, `gain` 1.2, DEUTAN | `cpd` **corrected** to 6; `gain` kept (still invented); DEUTAN kept, now sourced for elephants | Section 2. |
| Picture: `mole` `sat` 0 | **Corrected** to 0.4 | Log 130. |
| Shrews and hedgehogs left in `other` | **Superseded**: since build 21 they belong to the `mammal` group | `docs/COVERAGE.md`; still unmeasured (wanted: Bridges and Quilliam 1973). |

### `docs/views/sheets/bat.md`

| Row or number | Verdict | Today's evidence |
|---|---|---|
| Scope: the split at Pteropodidae | **Confirmed** | Section 1; flying fox total re-read today. |
| `bat` Calls | **Confirmed**; picture **corrected** | Log 55, 56. The hold and thrust now give 4.3 renewals a second, between the free-tailed bat's 3.7 (log 67, newly found) and the big brown bat's 5 to 10. |
| `bat` Distance | **Confirmed** | Log 57. |
| `bat` Reach | **Confirmed** in the audited wording | Log 60. |
| `bat` Direction | **Confirmed**, with an addition | Log 58. In the wild, Daubenton's bats narrow the beam to about 30 to 50 degrees across (log 66). Half-amplitude angles are measured from the axis and must be doubled for a full width (note on log 66). |
| `bat` Sharpness | **Confirmed** | Log 74 (0.6); added big brown bat 0.5 to 0.7 (log 62), *Myotis* 0.1 (log 71, 92), six species 0.35 to 2 (log 69). |
| `bat` Dim light | **Confirmed** | Log 63. |
| `bat` Colour | **Confirmed** | Log 82, 83, 85, 88 (vampire bats added). |
| `bat` Echoes (`x`) | **Confirmed** | ecoObs FAQ reopened today. |
| `bat` Magnetic compass (big brown bats, Holland and colleagues 2006) | **Not reopened**; supported in another bat | Log 89 (greater mouse-eared bats calibrate the compass at sunset). The row now names that bat. |
| `bat` picture `sat` 0.25 | **Corrected** to 0.2 (still invented) | Log 82. |
| `flyingfox` Sharpness | **Confirmed** | Log 75, 76. |
| `flyingfox` No calls | **Confirmed** | Log 75, 168. |
| `flyingfox` Colour (from a press release) | **Confirmed** from the paper's own abstract, with the three *Pteropus* species named | Log 146 (Müller, Goodman and Peichl 2007). |
| `flyingfox` One cone | **Confirmed**, with species named | Log 147. *Eidolon helvum* itself is unmeasured. |
| `flyingfox` Dim light (300,000 to 800,000 rods per square millimetre for bats, from a conservation page) | **Corrected** | Log 148: 350,000 to 800,000 in six pteropodids, from the paper. The comparison with people was dropped, since its page was not reopened. |
| `flyingfox` Ultraviolet (`i`, Wang and colleagues 2004) | **Not reopened**; kept | Log 85 notes that cave-roosting pteropodids lost the ultraviolet cone. |
| `flyingfox` Clicks (`x`) | **Confirmed** | Log 81. |
| `flyingfox` Field, focus and pupil (`i`) | **Partly filled** | Round pupil (log 80), binocular field 54 degrees (log 149), a temporal sharp area (log 77). |
| Picture: `flyingfox` `sat` 0.7 | **Corrected** to 0.6 (still invented) | Log 148. |
| Unfinished: no figure for the Mexican free-tailed bat | **Partly filled** | Calls (log 67) and dives (log 68); its vision paper (Lemus and colleagues 2026) is on the wanted list. |

## 4. Species with their own measurements

These commonly photographed species are measured well enough for a profile of their own later.

| Species | Records | What is measured | Log lines |
|---|---:|---|---|
| Harbour seal (*Phoca vitulina*) | 44,546 | cone 510 nm; acuity in water, air and turbidity; single targets; field 208 and binocular 67 degrees; area centralis and streak; pupil and cornea; whisker trails; hearing in two media | 15, 16, 27, 28, 33 to 40, 42, 47 |
| Humpback whale (*Megaptera novaeangliae*) | 31,040 | rods only (genes); retina near 492 nm; acuity 3.95; two sharp areas; blue-green tapetum | 1, 13, 29, 158, 159 |
| Common bottlenose dolphin (*Tursiops truncatus*) | 16,874 | rod 488 and cone 524 nm; colour tests; acuity in both media; two sharp areas; double-slit pupil; sonar beam and angular resolution; tapetum | 8, 9, 14, 22 to 25, 48, 53, 54, 160 |
| Crab-eating macaque (*Macaca fascicularis*) | 15,934 | cones 430, 531, 561 nm | 101 to 103 |
| Rhesus macaque (*Macaca mulatta*) | 6,991 | rods 502, cones 536 and 565 nm; acuity across luminance | 104, 119 |
| White-faced capuchin (*Cebus imitator*) | 8,461 | colour polymorphism in a wild troop, and its effect on sniffing | 163 |
| Big brown bat (*Eptesicus fuscus*) | 5,579 (bat sheet) | call rates; range accuracy; beam; aiming; acuity; dim-light limit | 55 to 58, 62, 63 |
| Mexican free-tailed bat (*Tadarida brasiliensis*) | 3,822 (bat sheet); 179 in Alachua | search calls; dives | 67, 68 |
| Daubenton's bat (*Myotis daubentonii*) | not counted | acuity 0.6; field beam; visual threshold | 66, 73, 74 |
| Grey-headed and black flying foxes (*Pteropus poliocephalus*, *P. alecto*) | 5,590 and 2,406 (bat sheet) | acuity about 4 | 75 |
| Egyptian rousette (*Rousettus aegyptiacus*) | in 553 *Rousettus* | acuity; field of best vision; hearing; clicks and vision together | 75, 81, 150, 152 |
| Common raccoon (*Procyon lotor*) | in 137,710 *Procyon* | one cone; forepaw cortex | 120, 166 |
| Virginia opossum (*Didelphis virginiana*) | 54,547 | one cone 561 nm; tapetum in the upper retina | 122, 162 |
| American black bear (*Ursus americanus*) | in 71,923 Ursidae | two cones, 3:1; area centralis | 127, 128 |
| African elephant (*Loxodonta africana*) | in 28,818 Proboscidea | pigments; anatomical and behavioural acuity; tapetum; streak | 132 to 135 |
| Tammar wallaby (*Macropus eugenii*) | in 89,090 Macropodidae | two cones; acuity 4.8 | 139, 140 |
| European mole (*Talpa europaea*) | 17,116 | S and M cones; ultraviolet | 130, 131 |
| Star-nosed mole (*Condylura cristata*) | 1,700 | the star's touch, rate and saccades | 154 to 156 |
| Platypus (*Ornithorhynchus anatinus*) | in 23,545 Monotremata | retina; electric and touch hunting | 143, 153 |
| Florida manatee (*Trichechus manatus*) | 7,903 | acuity; touch hairs | 45, 46 |
| Northern elephant seal (*Mirounga angustirostris*) | in 79,366 Phocidae | dark adaptation; pupil range; tapetum; wild whisker hunting | 30, 32, 43, 161 |

## 5. Gaps and how to fill them

| Trait the views need | Who lacks it | Nearest measured relative, and how a value could be inferred |
|---|---|---|
| Flicker fusion (`rate`) | all five groups | Nothing measured opened. The only primate study is wanted (Ordy and Samorajski 1968). Until then every view keeps your pace. An inference from photoreceptor speed is possible only with recordings no source here gives, so for now nothing is known. |
| Sharpness of the raccoon and the Virginia opossum | `raccoon` | The rule that acuity follows eye length (log 94) and falls in nocturnal species (log 93) points below the dog's 11 but gives no number. The opossum's ganglion cell map (Rapaport and colleagues 1981) and its behavioural acuity (Silveira and colleagues 1982) are both wanted; with eye length and peak ganglion cell density, cycles per degree follow from the same sampling arithmetic the numbat and rhinoceros papers use (log 136, 137). |
| Sharpness of bears, otters, skunks, pigs and koalas | `mammal` | The black bear's cone-dense area centralis (log 128) promises good acuity without a number. The method above applies to any retina mapped; the hippopotamus is mapped (Coimbra and colleagues 2017, wanted). The view's 6 is a pick inside the measured span (log 136, 137, 140). |
| Colour of koalas, possums and wombats | `mammal` | The nearest measured diprotodont is the tammar wallaby, a dichromat (log 139); some other marsupials may be trichromats (same line). Drawing koalas as dichromats is an inference from that relative and should stay `g`. |
| Colour of hedgehogs and shrews | `mammal` | Nothing opened. Bridges and Quilliam 1973 (wanted) measured hedgehog pigments. Until then they take the group's default, which is a guess for them. |
| Rod peak and acuity of armadillos, sloths and anteaters | rods-only variant | Mammalian rods measured here peak at 493 to 502 nm (log 104, 122, 134); the variant's blue-green weighting follows that range. Acuity is unknown; the small eye of the anteater (log 167's companion paper, abstract only) suggests very coarse sight, and the variant's 2 is a guess. |
| Field of view of primates | `primate`, `capuchin`, `lemur` | Nothing measured opened. Forward-facing eyes, the primate pathway that flying foxes share (log 151) and a binocular field of 54 degrees in *Pteropus* (log 149) say nothing direct about monkeys, so the views keep the camera's field. |
| Field of view of whales and dolphins | `whale`, `dolphin` | The beluga's field (Mass 2001) is wanted. The two sharp areas (log 23, 158) imply a wide field reaching behind the eye; a value such as 300 degrees would be an inference from them and the seal's measured 208 (log 36). |
| How a seal's sight in air worsens as light falls | `seal` | Hanke and Dehnhardt 2009 and Schusterman and Balliet 1971 (both wanted). The dolphin's equal acuity in both media in bright light (log 24) fixes the bright end of the curve; the dim end is a guess. |
| The manatee's cone peaks | `manatee` | Newman and Robinson 2006 (wanted). The nearest measured large herbivore with two cones in this log is the elephant (log 134); borrowing its peaks would be an inference from a different order, and the view's DEUTAN is that kind of guess. |
| How sharp and how wide the echo picture is | `bat`, `dolphin` | Geberl and colleagues 2019 and Simmons and colleagues 1983 (wanted) for bats; a dolphin's echo angular resolution of 1.5 degrees (log 48) and a bat's aiming accuracy of 5 degrees (log 58) bracket it. Echo strength falls with distance by the sonar equation, which Boonman and colleagues apply (log 60); the brightness fall-off can follow that equation. |
| Whether whale rods are dazzled at the surface | `whale` | Nothing opened. A specialist question (section 8). |
| Where each sharp area looks | `bat`, `dolphin`, `mammal` | The retinal positions are measured (log 70, 74, 23, 128); turning them into directions in the visual field needs each eye's orientation in the head, which no source here gives. |
| Tapetum in tarsiers and owl monkeys | `lemur` variant | The sources opened do not say. Lemurs and galagos have one (log 165). |

## 6. Closed sources wanted

The list in `docs/views/wanted/mammal-groups.jsonl`, most useful first:

1. Hanke and Dehnhardt 2009, aerial acuity of harbour seals as light falls (doi:10.1007/s00359-009-0439-2). Sets the seal view's light-dependent blur.
2. Schusterman and Balliet 1971, California sea lion acuity in air and water by luminance (doi:10.1111/j.1749-6632.1971.tb13088.x).
3. Geberl, Kugler and Wiegrebe 2019, the spatial resolution of bat biosonar (doi:10.1016/j.cub.2019.04.046). Sets the sharpness of the echo picture.
4. Ordy and Samorajski 1968, acuity and ERG flicker fusion in diurnal and nocturnal primates (doi:10.1016/0042-6989(68)90028-x). The only primate flicker source found.
5. Silveira, Picanço Diniz and Oswaldo-Cruz 1982, contrast sensitivity and acuity of the opossum (doi:10.1016/0042-6989(82)90227-9).
6. Mass 2001, visual field and resolution of the beluga (doi:10.1023/a:1013326521559).
7. Newman and Robinson 2006, visual pigments of the West Indian manatee (doi:10.1016/j.visres.2006.03.010).
8. Graydon, Giorgi and Pettigrew 1987, vision in flying foxes (doi:10.1071/am87021).
9. Simmons and colleagues 1983, angle discrimination by the big brown bat's sonar (doi:10.1007/bf00612586).
10. Griebel and Schmid 1996, colour vision in the manatee (doi:10.1016/0042-6989(95)00323-1).
11. Cowey and Ellis 1967, acuity of rhesus and squirrel monkeys (doi:10.1037/h0024821).
12. Jacobs and colleagues 1993, photopigments of the owl monkey (doi:10.1016/0042-6989(93)90168-v).
13. Bridges and Quilliam 1973, visual pigments of moles and hedgehogs (doi:10.1016/0042-6989(73)90239-3).
14. Melin and colleagues 2014, dichromacy in the Samoan flying fox (doi:10.1007/s00359-014-0951-x).
15. Danilovich and colleagues 2015, bats regulate biosonar by available visual information (doi:10.1016/j.cub.2015.11.003).
16. Lemus and colleagues 2026, free-tailed bats use vision and hearing in a maze (doi:10.1007/s00359-026-01813-5).
17. Rapaport, Wilson and Rowe 1981, ganglion cells of the Virginia opossum (doi:10.1002/cne.901990403).
18. Strobel and colleagues 2020, amphibious vision in sea otters (doi:10.1007/s00359-020-01436-4).
19. White and colleagues 1971, acuity of the killer whale (doi:10.1016/0014-4886(71)90066-5).
20. Chang and colleagues 2026, bat eye movements (doi:10.1016/j.cub.2026.03.013).
21. Eitan and colleagues 2022, daylight echolocation in visual bats (doi:10.1016/j.cub.2022.02.075).
22. Winter, López and von Helversen 2003, ultraviolet vision in a bat (doi:10.1038/nature01971).
23. Coimbra, Bertelsen and Manger 2017, ganglion cells and acuity of the hippopotamus (doi:10.1002/cne.24179).
24. Kay and Kirk 2000, bones as evidence of activity pattern and acuity in primates (doi:10.1002/1096-8644(200010)113:2<235::aid-ajpa7>3.0.co;2-9).

## 7. Sources

Every source behind a log line, one line each, with how it was read. "Opened" means read in this session.

- Adachi T, Naito Y, Robinson PW, Costa DP, Hückstädt LA, Holser RR, Iwasaki W, Takahashi A, 2022. Whiskers as hydrodynamic prey sensors in foraging seals. *Proceedings of the National Academy of Sciences of the USA*. doi:10.1073/pnas.2119502119. **opened** (full text on disk in the collection). Log 43, 44.
- Ahnelt PK, Hokoç JN, Röhlich P, 1995. Photoreceptors in a primitive mammal, the South American opossum, Didelphis marsupialis aurita: characterization with anti-opsin immunolabeling. *Visual Neuroscience*. doi:10.1017/s0952523800009366. **opened** (abstract stored in the collection). Log 123.
- Akamatsu T, Wang D, Wang K, Naito Y, 2005. Biosonar behaviour of free-ranging porpoises. *Proceedings of the Royal Society B*. doi:10.1098/rspb.2004.3024. **opened** (abstract stored in the collection). Log 51.
- Arrese CA, Archer M, Runham PB, Dunlop SA, Beazley LD, 2000. Visual system in a diurnal marsupial, the numbat (Myrmecobius fasciatus): retinal organization, visual acuity and visual fields. *Brain, Behavior and Evolution*. doi:10.1159/000006650. **opened** (abstract stored in the collection). Log 137.
- Arrese CA, Archer M, Beazley LD, 2002. Visual capabilities in a crepuscular marsupial, the honey possum (Tarsipes rostratus): a visual approach to ecology. *Journal of Zoology*. doi:10.1017/s0952836902000183. **opened** (abstract stored in the collection). Log 138.
- Au WWL, Moore PWB, Pawloski DA, 1986. Echolocation transmitting beam of the Atlantic bottlenose dolphin. *Journal of the Acoustical Society of America*. doi:10.1121/1.394012. **opened** (abstract stored in the collection). Log 53.
- Bauer GB, Colbert DE, Gaspard JC, Littlefield B, Fellner W, 2003. Underwater visual acuity of Florida manatees (Trichechus manatus latirostris). *International Journal of Comparative Psychology*. doi:10.46867/c43p4v. **opened** (abstract stored in the collection). Log 45.
- Baylor DA, Nunn BJ, Schnapf JL, 1987. Spectral sensitivity of cones of the monkey Macaca fascicularis. *Journal of Physiology*. doi:10.1113/jphysiol.1987.sp016691. **opened** (abstract stored in the collection). Log 101, 102, 103.
- Bolin J, Moreno V, Johnsen S, Schweikert LE, 2025. Humpback whale (Megaptera novaeangliae) visual acuity allows silhouette detection but not fine detail discrimination over ecological distances. *Proceedings of the Royal Society B*. doi:10.1098/rspb.2024.3101. **opened** (abstract stored in the collection). Log 29.
- Boonman A, Bar-On Y, Cvikel N, Yovel Y, 2013. It's not black or white: on the range of vision and echolocation in echolocating bats. *Frontiers in Physiology*. doi:10.3389/fphys.2013.00248. **opened** (full text on disk in the collection). Log 60, 61, 62, 63, 168.
- Bowmaker JK, Dartnall HJA, Lythgoe JN, Mollon JD, 1978. The visual pigments of rods and cones in the rhesus monkey, Macaca mulatta. *Journal of Physiology*. doi:10.1113/jphysiol.1978.sp012151. **opened** (abstract stored in the collection). Log 104.
- Braekevelt CR, 1976. Fine structure of the retinal epithelium and tapetum lucidum of the opossum (Didelphis virginiana). *Journal of Morphology*. doi:10.1002/jmor.1051500110. **opened** (abstract stored in the collection). Log 162.
- Branstetter BK, Brietenstein R, Goya G, Tormey MN, Wu T, Finneran JJ, 2022. Spatial acuity of the bottlenose dolphin (Tursiops truncatus) biosonar system with a bat and human comparison. *Journal of the Acoustical Society of America*. doi:10.1121/10.0011676. **opened** (abstract stored in the collection). Log 48.
- Carvalho LS, Pessoa DMA, Mountford JK, Davies WIL, Hunt DM, 2017. The genetic and evolutionary drives behind primate color vision. *Frontiers in Ecology and Evolution*. doi:10.3389/fevo.2017.00034. **opened** (full text on disk in the collection). Log 99, 106, 107, 109, 110.
- Catania KC, Remple FE, 2003. Tactile foveation in the star-nosed mole. *Brain, Behavior and Evolution*. doi:10.1159/000073755. **opened** (abstract stored in the collection). Log 155, 156.
- Catania KC, 2011. The sense of touch in the star-nosed mole: from mechanoreceptors to the brain. *Philosophical Transactions of the Royal Society B*. doi:10.1098/rstb.2011.0128. **opened** (abstract stored in the collection). Log 154.
- Caves EM, Brandley NC, Johnsen S, 2018. Visual acuity and the evolution of signals. *Trends in Ecology and Evolution*. doi:10.1016/j.tree.2018.03.001. **opened** (owner's library copy; short quotes only). Log 91, 92, 93, 94.
- Cavonius CR, Robbins DO, 1973. Relationships between luminance and visual acuity in the rhesus monkey. *Journal of Physiology*. doi:10.1113/jphysiol.1973.sp010267. **opened** (abstract stored in the collection). Log 119.
- Cechetto C, de Busserolles F, Jakobsen L, Warrant EJ, 2020. Retinal ganglion cell topography and spatial resolving power in echolocating and non-echolocating bats. *Brain, Behavior and Evolution*. doi:10.1159/000508863. **opened** (publisher or repository page, read through the web tool). Log 74, 75.
- Crognale MA, Levenson D, Ponganis PJ, Deegan JF, Jacobs GH, 1998. Cone spectral sensitivity in the harbor seal (Phoca vitulina) and implications for color vision. *Canadian Journal of Zoology*. doi:10.1139/z98-129. **opened** (abstract stored in the collection). Log 15, 16.
- Czech-Damal NU, Liebschner A, Miersch L, Klauer G, Hanke FD, Marshall CD, Dehnhardt G, Hanke W, 2011. Electroreception in the Guiana dolphin (Sotalia guianensis). *Proceedings of the Royal Society B*. doi:10.1098/rspb.2011.1127. **opened** (abstract stored in the collection). Log 41.
- Céchetto C, Jakobsen L, Warrant EJ, 2023. Visual detection threshold in the echolocating Daubenton's bat (Myotis daubentonii). *Journal of Experimental Biology*. doi:10.1242/jeb.244451. **opened** (publisher or repository page, read through the web tool). Log 73.
- Danilovich S, Yovel Y, 2019. Integrating vision and echolocation for navigation and perception in bats. *Science Advances*. doi:10.1126/sciadv.aaw6503. **opened** (full text on disk in the collection). Log 81.
- Dehnhardt G, Mauck B, Hanke W, Bleckmann H, 2001. Hydrodynamic trail-following in harbor seals (Phoca vitulina). *Science*. doi:10.1126/science.1060514. **opened** (abstract stored in the collection). Log 42.
- Ebeling W, Natoli RC, Hemmi JM, 2010. Diversity of color vision: not all Australian marsupials are trichromatic. *PLoS ONE*. doi:10.1371/journal.pone.0014231. **opened** (full text on disk in the collection). Log 139.
- Eklöf J, Šuba J, Petersons G, Rydell J, 2014. Visual acuity and eye size in five European bat species in relation to foraging and migration strategies. *Environmental and Experimental Biology*. https://eeb.lu.lv/EEB/201403/EEB_12_Eklof.shtml. **opened** (abstract stored in the collection). Log 71.
- Emerling CA, Springer MS, 2014. Genomic evidence for rod monochromacy in sloths and armadillos suggests early subterranean history for Xenarthra. *Proceedings of the Royal Society B*. doi:10.1098/rspb.2014.2192. **opened** (abstract stored in the collection). Log 141, 142.
- Fasick JI, Robinson PR, 2016. Adaptations of cetacean retinal pigments to aquatic environments. *Frontiers in Ecology and Evolution*. doi:10.3389/fevo.2016.00070. **opened** (full text on disk in the collection). Log 8 to 170 (8 lines).
- Gilad Y, Wiebe V, Przeworski M, Lancet D, Pääbo S, 2004. Loss of olfactory receptor genes coincides with the acquisition of full trichromatic vision in primates. *PLoS Biology*. doi:10.1371/journal.pbio.0020005. **opened** (full text on disk in the collection). Log 164.
- Glösmann M, Steiner M, Peichl L, Ahnelt PK, 2008. Cone photoreceptors and potential UV vision in a subterranean insectivore, the European mole. *Journal of Vision*. doi:10.1167/8.4.23. **opened** (abstract stored in the collection). Log 130, 131.
- Griebel U, Peichl L, 2003. Colour vision in aquatic mammals: facts and open questions. *Aquatic Mammals*. doi:10.1578/016754203101024040. **opened** (abstract stored in the collection). Log 17, 18.
- Hanke FD, Peichl L, Dehnhardt G, 2009. Retinal ganglion cell topography in juvenile harbor seals (Phoca vitulina). *Brain, Behavior and Evolution*. doi:10.1159/000235612. **opened** (abstract stored in the collection). Log 27, 28.
- Hanke W, Römer R, Dehnhardt G, 2006. Visual fields and eye movements in a harbor seal (Phoca vitulina). *Vision Research*. doi:10.1016/j.visres.2006.02.004. **opened** (publisher or repository page, read through the web tool). Log 36, 37, 38.
- Heffner RS, Koay G, Heffner HE, 1999. Sound localization in an Old-World fruit bat (Rousettus aegyptiacus): acuity, use of binaural cues, and relationship to vision. *Journal of Comparative Psychology*. doi:10.1037//0735-7036.113.3.297. **opened** (abstract stored in the collection). Log 150.
- Hemmi JM, Mark RF, 1998. Visual acuity, contrast sensitivity and retinal magnification in a marsupial, the tammar wallaby (Macropus eugenii). *Journal of Comparative Physiology A*. doi:10.1007/s003590050264. **opened** (publisher or repository page, read through the web tool). Log 140.
- Herman LM, Peacock MF, Yunker MP, Madsen CJ, 1975. Bottle-nosed dolphin: double-slit pupil yields equivalent aerial and underwater diurnal acuity. *Science*. doi:10.1126/science.1162351. **opened** (abstract stored in the collection). Log 24, 25.
- Herron P, 1978. Somatotopic organization of mechanosensory projections to SII cerebral neocortex in the raccoon (Procyon lotor). *Journal of Comparative Neurology*. doi:10.1002/cne.901810403. **opened** (abstract stored in the collection). Log 166.
- Heyward JL, Reynolds BD, Foster ML, Archibald KE, Stoskopf MK, Mowat FM, 2020. Retinal cone photoreceptor distribution in the American black bear (Ursus americanus). *The Anatomical Record*. doi:10.1002/ar.24472. **opened** (abstract stored in the collection). Log 127, 128.
- Holland RA, Borissov IM, Siemers BM, 2010. A nocturnal mammal, the greater mouse-eared bat, calibrates a magnetic compass by the sun. *Proceedings of the National Academy of Sciences of the USA*. doi:10.1073/pnas.0912477107. **opened** (abstract stored in the collection). Log 89.
- Jacobs GH, Deegan JF, 1992. Cone photopigments in nocturnal and diurnal procyonids. *Journal of Comparative Physiology A*. doi:10.1007/BF00223965. **opened** (publisher or repository page, read through the web tool). Log 120, 121.
- Jacobs GH, Deegan JF, 1993. Photopigments underlying color vision in ringtail lemurs (Lemur catta) and brown lemurs (Eulemur fulvus). *American Journal of Primatology*. doi:10.1002/ajp.1350300307. **opened** (abstract stored in the collection). Log 111.
- Jacobs GH, 1996. Primate photopigments and primate color vision. *Proceedings of the National Academy of Sciences of the USA*. doi:10.1073/pnas.93.2.577. **opened** (abstract stored in the collection). Log 105.
- Jacobs GH, Deegan JF, 1999. Uniformity of colour vision in Old World monkeys. *Proceedings of the Royal Society B*. doi:10.1098/rspb.1999.0881. **opened** (abstract stored in the collection). Log 100.
- Jacobs GH, Deegan JF, 2003. Diurnality and cone photopigment polymorphism in strepsirrhines: examination of linkage in Lemur catta. *American Journal of Physical Anthropology*. doi:10.1002/ajpa.10309. **opened** (abstract stored in the collection). Log 112.
- Jacobs GH, Williams GA, 2010. Cone pigments in a North American marsupial, the opossum (Didelphis virginiana). *Journal of Comparative Physiology A*. doi:10.1007/s00359-010-0519-3. **opened** (full text on disk in the collection). Log 122.
- Jacobs GH, 2013. Losses of functional opsin genes, short-wavelength cone photopigments, and color vision: a significant trend in the evolution of mammalian vision. *Visual Neuroscience*. doi:10.1017/s0952523812000429. **opened** (abstract stored in the collection). Log 124.
- Jakobsen L, Brinkløv S, Surlykke A, 2013. Intensity and directionality of bat echolocation signals. *Frontiers in Physiology*. doi:10.3389/fphys.2013.00089. **opened** (full text on disk in the collection). Log 64, 65.
- Jensen FH, Bejder L, Wahlberg M, Madsen PT, 2009. Biosonar adjustments to target range of echolocating bottlenose dolphins (Tursiops sp.) in the wild. *Journal of Experimental Biology*. doi:10.1242/jeb.025619. **opened** (abstract stored in the collection). Log 54.
- Jones GA, Teeling EC, Rossiter SJ, 2013. From the ultrasonic to the infrared: molecular evolution and the sensory biology of bats. *Frontiers in Physiology*. doi:10.3389/fphys.2013.00117. **opened** (full text on disk in the collection). Log 84, 85, 86, 87.
- Jung K, Molinari J, Kalko EKV, 2014. Driving factors for the evolution of species-specific echolocation call design in New World free-tailed bats (Molossidae). *PLoS ONE*. doi:10.1371/journal.pone.0085279. **opened** (full text on disk in the collection). Log 67.
- Kastak DA, Schusterman RJ, 1998. Low-frequency amphibious hearing in pinnipeds: methods, measurements, noise, and ecology. *Journal of the Acoustical Society of America*. doi:10.1121/1.421367. **opened** (abstract stored in the collection). Log 47.
- Klećkowska-Nawrot J, Barszcz K, Stegmann KO, Goździewska-Harłajczuk K, 2023. The organ of vision morphology of the southern two-toed sloth (Choloepus didactylus Linnaeus, 1758; Pilosa, Choloepodidae). *Anatomia Histologia Embryologia*. doi:10.1111/ahe.12984. **opened** (abstract stored in the collection). Log 167.
- Kloepper LN, Tuninetti A, Bentley I, Harding CD, Brighton CH, Izadi MR, Stevenson RL, Taylor GK, 2025. Stereotyped active sensing in fast-diving echolocating bats. *iScience*. doi:10.1016/j.isci.2025.114099. **opened** (full text on disk in the collection). Log 68.
- Koay G, Heffner RS, Heffner HE, 1998. Hearing in a megachiropteran fruit bat (Rousettus aegyptiacus). *Journal of Comparative Psychology*. doi:10.1037//0735-7036.112.4.371. **opened** (abstract stored in the collection). Log 152.
- Kries K, Barros MAS, Duytschaever G, Orkin JD, Janiak MC, Pessoa DMA, Melin AD, 2018. Colour vision variation in leaf-nosed bats (Phyllostomidae): links to cave roosting and dietary specialization. *Molecular Ecology*. doi:10.1111/mec.14818. **opened** (abstract stored in the collection). Log 88.
- Kyhn LA, Tougaard J, Beedholm K, Jensen FH, Ashe E, Williams R, Madsen PT, 2013. Clicking in a killer whale habitat: narrow-band, high-frequency biosonar clicks of harbour porpoise (Phocoena phocoena) and Dall's porpoise (Phocoenoides dalli). *PLoS ONE*. doi:10.1371/journal.pone.0063763. **opened** (full text on disk in the collection). Log 50.
- Land MF, Nilsson D-E, 2012. Animal Eyes, 2nd edition (Oxford Animal Biology Series). *Oxford University Press*. doi:10.1093/acprof:oso/9780199581139.001.0001. **opened** in part (owner's library copy: front matter, chapters 1 and 2, chapter 3 to its section on sensitivity). Log 95, 96, 97, 98.
- Levenson D, Schusterman RJ, 1997. Pupillometry in seals and sea lions: ecological implications. *Canadian Journal of Zoology*. doi:10.1139/z97-838. **opened** (abstract stored in the collection). Log 32.
- Levenson D, Schusterman RJ, 1999. Dark adaptation and visual sensitivity in shallow and deep-diving pinnipeds. *Marine Mammal Science*. doi:10.1111/j.1748-7692.1999.tb00892.x. **opened** (abstract stored in the collection). Log 30, 31.
- Li L, Chi H, Liu H, Xia Y, Irwin DM, Zhang S, Liu Y, 2018. Retention and losses of ultraviolet-sensitive visual pigments in bats. *Scientific Reports*. doi:10.1038/s41598-018-29646-6. **opened** (full text on disk in the collection). Log 83.
- Lisney TJ, Collin SP, 2018. Retinal topography in two species of baleen whale (Cetacea: Mysticeti). *Brain, Behavior and Evolution*. doi:10.1159/000495285. **opened** (abstract stored in the collection). Log 158, 159.
- Madsen PT, Johnson MP, Aguilar de Soto N, Zimmer WMX, Tyack PL, 2005. Biosonar performance of foraging beaked whales (Mesoplodon densirostris). *Journal of Experimental Biology*. doi:10.1242/jeb.01327. **opened** (abstract stored in the collection). Log 52.
- Manger PR, Calford MB, Pettigrew JD, 1996. Properties of electrosensory neurons in the cortex of the platypus (Ornithorhynchus anatinus): implications for processing of electrosensory stimuli. *Proceedings of the Royal Society B*. doi:10.1098/rspb.1996.0092. **opened** (abstract stored in the collection). Log 153.
- Manske U, Schmidt U, 1976. Visual acuity of the vampire bat, Desmodus rotundus, and its dependence upon light intensity. *Zeitschrift für Tierpsychologie*. doi:10.1111/j.1439-0310.1976.tb00967.x. **opened** (abstract stored in the collection). Log 72.
- Mass AM, Supin AYa, 1995. Ganglion cell topography of the retina in the bottlenosed dolphin, Tursiops truncatus. *Brain, Behavior and Evolution*. doi:10.1159/000113554. **opened** (abstract stored in the collection). Log 22, 23.
- Mass AM, Supin AYa, 2003. Retinal topography of the harp seal Pagophilus groenlandicus. *Brain, Behavior and Evolution*. doi:10.1159/000073273. **opened** (abstract stored in the collection). Log 26.
- Mass AM, Supin AYa, 2007. Adaptive features of aquatic mammals' eye. *The Anatomical Record*. doi:10.1002/ar.20529. **opened** (abstract stored in the collection). Log 19, 20, 21.
- Matsuzawa T, 1990. Form perception and visual acuity in a chimpanzee. *Folia Primatologica*. doi:10.1159/000156494. **opened** (abstract stored in the collection). Log 118.
- Melin AD, Nevo O, Shirasu M, Williamson RE, Garrett EC, Endo M, Sakurai K, Matsushita Y, Touhara K, Kawamura S, 2019. Fruit scent and observer colour vision shape food-selection strategies in wild capuchin monkeys. *Nature Communications*. doi:10.1038/s41467-019-10250-9. **opened** (full text on disk in the collection). Log 163.
- Meredith RW, Gatesy J, Emerling CA, York VM, Springer MS, 2013. Rod monochromacy and the coevolution of cetacean retinal opsins. *PLoS Genetics*. doi:10.1371/journal.pgen.1003432. **opened** (full text on disk in the collection). Log 1, 2, 3.
- Morris JM, Fernández-Juricic E, Plummer CE, Moore BA, 2025. Visual field of the ferret (Mustela putorius furo), rat (Rattus norvegicus), and tree shrew (Tupaia belangeri). *Journal of Vision*. doi:10.1167/jov.25.13.8. **opened** (full text on disk in the collection). Log 144, 145.
- Mortimer B, Rees WL, Koelemeijer P, Nissen-Meyer T, 2018. Classifying elephant behaviour through seismic vibrations. *Current Biology*. doi:10.1016/j.cub.2018.03.062. **opened** (abstract stored in the collection). Log 157.
- Moss CF, Surlykke A, 2010. Probing the natural scene by echolocation in bats. *Frontiers in Behavioral Neuroscience*. doi:10.3389/fnbeh.2010.00033. **opened** (full text on disk in the collection). Log 55, 56, 57, 58, 59.
- Murugavel B, Mitkus M, Somanathan H, Kelber A, 2022. Retinal ganglion cell topography and spatial resolution in three Indian pteropodid bats. *Brain, Behavior and Evolution*. doi:10.1159/000528417. **opened** (abstract stored in the collection). Log 76, 77, 78.
- Müller B, Goodman SM, Peichl L, 2007. Cone photoreceptor diversity in the retinas of fruit bats (Megachiroptera). *Brain, Behavior and Evolution*. doi:10.1159/000102971. **opened** (abstract stored in the collection). Log 146, 147, 148.
- Müller B, Glösmann M, Peichl L, Knop GC, Hagemann C, Ammermüller J, 2009. Bat eyes have ultraviolet-sensitive cone photoreceptors. *PLoS ONE*. doi:10.1371/journal.pone.0006390. **opened** (full text on disk in the collection). Log 82.
- Neitz J, Jacobs GH, 1989. Spectral sensitivity of cones in an ungulate. *Visual Neuroscience*. doi:10.1017/S0952523800011949. **opened** (publisher or repository page, read through the web tool). Log 125, 126.
- Ollivier FJ, Samuelson DA, Brooks DE, Lewis PA, Kallberg ME, Komáromy AM, 2004. Comparative morphology of the tapetum lucidum (among selected species). *Veterinary Ophthalmology*. doi:10.1111/j.1463-5224.2004.00318.x. **opened** (abstract stored in the collection). Log 129.
- Peichl L, Behrmann G, Kröger RHH, 2001. For whales and seals the ocean is not blue: a visual pigment loss in marine mammals. *European Journal of Neuroscience*. doi:10.1046/j.0953-816x.2001.01533.x. **opened** (abstract stored in the collection). Log 5, 6, 7.
- Peter-Ajuzie IK, Nwaogu IC, Majesty-Alukagberie LO, Ajaebili AC, Farrag FA, Kassab M, Morsy KS, Abumandour MMA, 2021. Ocular morphology of the fruit bat, Eidolon helvum, and the optical role of the choroidal papillae in the megachiropteran eye: a novel insight. *Folia Morphologica*. doi:10.5603/fm.a2021.0072. **opened** (full text on disk in the collection). Log 79, 80.
- Pettigrew JD, 1986. Flying primates? Megabats have the advanced pathway from eye to midbrain. *Science*. doi:10.1126/science.3945827. **opened** (abstract stored in the collection). Log 151.
- Pettigrew JD, Dreher B, Hopkins CS, McCall MJ, Brown M, 1988. Peak density and distribution of ganglion cells in the retinae of microchiropteran bats: implications for visual acuity. *Brain, Behavior and Evolution*. doi:10.1159/000116531. **opened** (abstract stored in the collection). Log 69, 70.
- Pettigrew JD, Manger PR, 2008. Retinal ganglion cell density of the black rhinoceros (Diceros bicornis): calculating visual resolution. *Visual Neuroscience*. doi:10.1017/s0952523808080498. **opened** (abstract stored in the collection). Log 136.
- Pettigrew JD, Bhagwandin A, Haagensen M, Manger PR, 2010. Visual acuity and heterogeneities of retinal ganglion cell densities and the tapetum lucidum of the African elephant (Loxodonta africana). *Brain, Behavior and Evolution*. doi:10.1159/000314898. **opened** (abstract stored in the collection). Log 132, 133.
- Pirie A, 1959. Crystals of riboflavin making up the tapetum lucidum in the eye of a lemur. *Nature*. doi:10.1038/183985a0. **opened** (publisher or repository page, read through the web tool). Log 165.
- Reep RL, Marshall CD, Stoll ML, 2002. Tactile hairs on the postcranial body in Florida manatees: a mammalian lateral line?. *Brain, Behavior and Evolution*. doi:10.1159/000064161. **opened** (abstract stored in the collection). Log 46.
- Rosa MGP, Schmid LM, 1994. Topography and extent of visual-field representation in the superior colliculus of the megachiropteran Pteropus. *Visual Neuroscience*. doi:10.1017/s0952523800006878. **opened** (abstract stored in the collection). Log 149.
- Sandow LM, Miersch L, Hanke FD, 2026. Underwater visual single target acuity in harbor seals (Phoca vitulina). *Journal of Comparative Physiology A*. doi:10.1007/s00359-026-01837-x. **opened** (full text on disk in the collection). Log 33, 34, 35.
- Schweikert LE, Fasick JI, Grace MS, 2016. Evolutionary loss of cone photoreception in balaenid whales reveals circuit stability in the mammalian retina. *Journal of Comparative Neurology*. doi:10.1002/cne.23996. **opened** (abstract stored in the collection). Log 4.
- Shyan-Norwalt MR, Peterson J, Milankow B, Staggs TE, Dale R, 2009. Initial findings on visual acuity thresholds in an African elephant (Loxodonta africana). *Zoo Biology*. doi:10.1002/zoo.20259. **opened** (abstract stored in the collection). Log 135.
- Silveira LCL, Saito CA, da Silva Filho M, Kremers J, Bowmaker JK, Lee BB, 2014. Alouatta trichromatic color vision: cone spectra and physiological responses studied with microspectrophotometry and single unit retinal electrophysiology. *PLoS ONE*. doi:10.1371/journal.pone.0113321. **opened** (abstract stored in the collection). Log 108.
- Smodlaka H, Khamas WA, Palmer L, Lui B, Borovac JA, Cohn BA, Schmitz L, 2016. Eye histology and ganglion cell topography of northern elephant seals (Mirounga angustirostris). *The Anatomical Record*. doi:10.1002/ar.23342. **opened** (abstract stored in the collection). Log 161.
- Surlykke A, Pedersen SB, Jakobsen L, 2008. Echolocating bats emit a highly directional sonar sound beam in the field. *Proceedings of the Royal Society B*. doi:10.1098/rspb.2008.1505. **opened** (full text on disk in the collection). Log 66.
- Thiagavel J, Céchetto C, Santana SE, Jakobsen L, Warrant EJ, Ratcliffe JM, 2018. Auditory opportunity and visual constraint enabled the evolution of echolocation in bats. *Nature Communications*. doi:10.1038/s41467-017-02532-x. **opened** (full text on disk in the collection). Log 90.
- Townsend S, 2023. Scalopus aquaticus, eastern mole. *Animal Diversity Web*. https://animaldiversity.org/accounts/Scalopus_aquaticus/. **opened** (publisher or repository page, read through the web tool). Log 169.
- Troilo D, Rowland HC, Judge SJ, 1993. Visual optics and retinal cone topography in the common marmoset (Callithrix jacchus). *Vision Research*. doi:10.1016/0042-6989(93)90038-x. **opened** (abstract stored in the collection). Log 117.
- Valenta K, Edwards M, Rafaliarison RR, Johnson SE, Holmes SM, Brown KA, Dominy NJ, Lehman SM, Parra EJ, Melin AD, 2015. Visual ecology of true lemurs suggests a cathemeral origin for the primate cone opsin polymorphism. *Functional Ecology*. doi:10.1111/1365-2435.12575. **opened** (abstract stored in the collection). Log 113.
- Veilleux CC, Kirk EC, 2009. Visual acuity in the cathemeral strepsirrhine Eulemur macaco flavifrons. *American Journal of Primatology*. doi:10.1002/ajp.20665. **opened** (abstract stored in the collection). Log 114, 115, 116.
- Weiffen M, Möller B, Mauck B, Dehnhardt G, 2006. Effect of water turbidity on the visual acuity of harbor seals (Phoca vitulina). *Vision Research*. doi:10.1016/j.visres.2005.08.015. **opened** (publisher or repository page, read through the web tool). Log 39, 40.
- Wisniewska DM, Ratcliffe JM, Beedholm K, Christensen CB, Johnson M, Koblitz JC, Wahlberg M, Madsen PT, 2015. Range-dependent flexibility in the acoustic field of view of echolocating porpoises (Phocoena phocoena). *eLife*. doi:10.7554/elife.05651. **opened** (full text on disk in the collection). Log 49.
- Yokoyama S, Takenaka N, Agnew D, Shoshani J, 2005. Elephants and human color-blind deuteranopes have identical sets of visual pigments. *Genetics*. doi:10.1534/genetics.104.039511. **opened** (abstract stored in the collection). Log 134.
- Young NM, Hope GM, Dawson WW, Jenkins RL, 1988. The tapetum fibrosum in the eyes of two small whales. *Marine Mammal Science*. doi:10.1111/j.1748-7692.1988.tb00537.x. **opened** (abstract stored in the collection). Log 160.
- Zeiss CJ, Schwab IR, Murphy CJ, Dubielzig RW, 2011. Comparative retinal morphology of the platypus. *Journal of Morphology*. doi:10.1002/jmor.10959. **opened** (abstract stored in the collection). Log 143.

Pages behind the counts, the phone inputs and the citations, all **opened** today:

- GBIF occurrence API, dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7, facets by family, genus and species for Primates (key 798), Cetacea (733), Sirenia (802), Carnivora (732), Phocidae (5310), Otariidae (5309), Delphinidae (5314), Balaenopteridae (5313), Procyonidae (5311), Mustelidae (5307), Soricomorpha (803), Talpidae (9469), Erinaceomorpha (829), Didelphimorphia (783), Diprotodontia (1452) and Pteropodidae (9367); the species API for names; family keys also from the GBIF name files on the repository's `ci` branch (`runs/fetch/10`, `runs/fetch/11`).
- This repository: `src/cam.a.js`, `docs/SOURCES.md`, `docs/VIEWS.md`, `docs/COVERAGE.md`, `docs/views/no-view-us-fl-alachua.csv`, `docs/views/world-orders.csv`, `data/regions/us-fl-alachua/species.json`, `tools/species/eyes.py`, `native/README.md`, `docs/tracks/engine.md`, and the earlier sheets and audits.
- ecoObs, EcoBatRec FAQ, https://ecobatrec.ecoobs.com/faq.html: the built-in microphone of an iPad or iPhone does not pick up bat calls.
- phyphox, LiDAR, https://phyphox.org/lidar/: Apple's Pro handhelds have a LiDAR scanner since 2020, measuring up to 5 m.
- Hugging Face, Monocular depth estimation (Transformers documentation), https://huggingface.co/docs/transformers/tasks/monocular_depth_estimation: depth from one image; Depth Anything V2 (relative) and ZoeDepth (absolute).
- Google, ARCore Depth API, https://developers.google.com/ar/develop/depth: depth from motion, with a time-of-flight sensor where present; 0 to 65 m, most accurate from 0.5 to 5 m; supported only on some phones.
- W3C Immersive Web Working Group, WebXR Depth Sensing Module, Editor's Draft of 25 August 2026, https://immersive-web.github.io/depth-sensing/: depth buffers for web pages from supported XR devices, read on the CPU or as GPU textures.
- Nandakumar R, Iyer V, Tan D, Gollakota S, 2016. FingerIO: using active sonar for fine-grained finger tracking. CHI 2016. https://fingerio.cs.washington.edu/fingerio.pdf: inaudible 18 to 20 kHz from a Samsung Galaxy S4's speaker, tracked with its microphones to about 8 mm over about 0.5 square metres.
- Environmental and Experimental Biology, article page for Eklöf, Šuba, Petersons and Rydell 2014, https://eeb.lu.lv/EEB/201403/EEB_12_Eklof.shtml: authors, journal, volume 12, pages 1 to 6 (the abstract itself is in the collection).
- Oxford Academic, book page for *Animal Eyes*, 2nd edition, https://academic.oup.com/book/10639: DOI 10.1093/acprof:oso/9780199581139.001.0001 and the year.
- Europe PMC records for PMIDs 7620874 and 3191381: the years of Mass and Supin 1995 and Pettigrew and colleagues 1988, which the collection gives as 2008; and for PMIDs 16564067 and 16197975, the abstracts of Hanke, Römer and Dehnhardt 2006 and of Weiffen and colleagues 2006.
- Frontiers article pages for Moss and Surlykke 2010 and Boonman and colleagues 2013: the author lists.

Used from the earlier sheets and **not reopened**, so **secondary** here: Levenson and colleagues 2006 (sea otter and polar bear cones); Emerling and Springer 2015 on pangolins (the earlier sheet's reading of the eScholarship PDF); Veilleux and Kirk 2014 (western grey kangaroo 11.2 cycles per degree); Scheich and colleagues 1986 (platypus threshold of about 50 µV per cm); Holland and colleagues 2006 (big brown bat magnetic homing); Wang and colleagues 2004 (ultraviolet opsin in the Formosan flying fox); Slonaker 1899 (eastern mole).

## 8. Questions for a specialist

1. For an echo picture of a big brown or free-tailed bat, what spatial resolution, depth steps and fall-off with distance should the image have, and is a dense depth image a fair stand-in for what a calling bat builds, or would sparse bright points at strong echoes be truer?
2. Are the rods of baleen whales and sperm whales dazzled at the sunlit surface, or does the closing pupil protect them? How should a rods-only picture behave in daylight, for whales and for armadillos?
3. How steeply does a harbour seal's or sea lion's sight in air fall as the light dims, and below what light level does the slit and pinhole pupil stop correcting the eye's short sight in air?
4. Where in the visual field, in degrees from straight ahead, do the sharp areas of insect-eating bats, dolphins, black bears and elephants look?
5. Which dichromat model fits best, for a camera-colour matrix: a capuchin male with the 563 nm or the 535 nm form of the long-wave pigment, a lemur with its cone near 545 nm, a pig with 556 nm, an elephant with 552 nm? Is a single deutan matrix acceptable for all of them?
6. Are there measurements, published or not, of cone types or acuity in koalas, European hedgehogs, shrews, ringtails, skunks or sea otters, the most photographed members of these groups that this sheet could not cover?
