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
