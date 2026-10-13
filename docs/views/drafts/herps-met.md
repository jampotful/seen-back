# herps-met: round 2 draft rows (alligator, frog, reptile)

Drafted 13 October 2026. Log lines are in `docs/views/evidence/herps-met.jsonl` (new in this unit) and `docs/views/evidence/herps.jsonl` (round 1, branch `research/herps`). "R1" below means a round-1 line. Final wording comes later.

## 1. Scope and mismatches

No gap table exists on `main`. Counts come from `docs/views/world-orders.csv` (Anura 2,055,810 iNaturalist research-grade records) and the Alachua file, which lists only species without a view, so it holds no frogs or reptiles. I used the Alachua fauna the owner named (alligator, anoles, turtles, treefrogs) plus the common species I know occur there, and I have no record count for them. The species list below is my own construction.

Most met, by view:
- alligator view: American alligator (Alachua), spectacled caiman and Nile and saltwater crocodiles (world).
- frog view: green treefrog (Dryophytes cinereus), squirrel and pine woods treefrogs, southern leopard frog (Lithobates sphenocephalus), bullfrog, Cuban treefrog, southern toad and oak toad, cane toad (Rhinella marina), narrowmouth toad; Europe: common frog (Rana temporaria), common toad (Bufo bufo), European treefrog.
- reptile view: red-eared slider, peninsula cooter and Florida redbelly, gopher tortoise, box turtle, softshell and snapping turtles; green and brown anoles; fence lizard, skinks (ground skink, five-lined skinks), Mediterranean and Indo-Pacific geckos; garter, water, rat and corn snakes, cottonmouth and rattlesnakes; green iguana.

Where the views should split (the reptile view is one guess for animals that differ in pupil, retina, pigments and a heat sense):
- reptile into turtle, lizard (anole and fence lizard, skink separately only if data arrive), gecko, and snake, with pit vipers (and boas and pythons) adding an infrared overlay.
- alligator stays one view for Alligator; caimans and crocodiles are a separate genus for rule 3 and a measured disagreement on colour (below).
- frog stays one view, with toads (horizontal pupil) distinct from treefrogs and ranids only if the pupil survey (wanted, Cervino 2021) shows it.

## 2. Alligator view (Alligator mississippiensis)

Today's rows speak of crocodiles. Replacement rows:

- [m] Colour. You have four kinds of colour-sensing cell, one more than a person. They absorb best near 444, 503, 535 and 566 nm, from violet-blue to yellow-green. You also have one kind of rod, at 501 nm. (R1 Sillman and Ronan 1991, five lines; R1 Wald 1957.) Carry block: the saltwater crocodile has three classes (R1 Nagloo 2016). Two measured crocodilian families disagree, so rule 5 blocks carrying the count to caimans and crocodiles in either direction. The row is written for the alligator only.
- [g] Night. A mirror layer behind your retina sends light back through it, which helps at dusk. Carried within the genus from the Chinese alligator (new line: Wan 2013, Alligator sinensis); R1 Ollivier 2004 says the layer is a retinal tapetum in crocodilians.
- [g] Pupil. Your pupil is a vertical slit. Banks 2015 (R1) reports slits for crocodilians as ambush hunters. No Alligator line is in the log. Wanted: Martinez and Plummer 2022; Beatty 2024 (pupil diameters, 165 juveniles).
- [i] Sharpest spot. The waterline band is borrowed from the saltwater crocodile's visual streak (R1 Nagloo 2016, Crocodylus). Rule 3 does not carry it across genera, so for an alligator it is a guess that you share the arrangement.
- [m] Sound and touch (x row). Your jaws carry dome-shaped pressure organs that detect small surface ripples (R1 Soares 2002; R1 Vanderbilt 2012 for A. mississippiensis), and you hear from about 100 Hz to 8 kHz (R1 Higgs 2002). The view cannot show either; a microphone input could stand in for hearing.
- [i] Field of view, sharpness, depth: no alligator measurement. Crocodylus porosus acuity is 8.8 cycles per degree and C. johnstoni 8.0 (R1 Nagloo 2016); numbers never travel (rule 1), so the picture keeps its guessed values and says so.

## 3. Frog view

Borrowers measured: Rana temporaria, Bufo bufo, Rhinella marina, Lithobates catesbeianus, L. pipiens, L. sphenocephalus, Dryophytes cinereus (pigments); treefrogs appear only in pigment lines.

- [g] Colour (new row). You have two kinds of rod: ordinary rods near 502 nm and "green" rods near 432 nm, which are blue-sensitive and found only in frogs, toads and some salamanders. Your cones include a red-sensitive kind near 560 to 580 nm and, in ranid frogs, a blue kind near 431 to 433 nm. New lines: Schott 2022 Table 1 for Bufo bufo, Rhinella marina, D. cinereus, L. catesbeianus, L. pipiens, L. sphenocephalus, R. temporaria; Table 2 and abstract show the same four opsin genes (RH1, LWS, SWS1, SWS2; no RH2) in the narrowmouth toad, southern toad relatives, eastern spadefoot, bullfrog, leopard frog and green treefrog. Gene presence predicts, and does not measure, a pigment. Rule 2 lets the repertoire travel within Anura (several families agree); wavelengths stay with the species named. Green treefrog cone values are not in the table (R1 line for D. cinereus gives only 2 classes from King and Douglass 1993; that line is at odds with four opsin genes and needs the original paper).
- [m] Movement. Leopard frogs and common toads strike at moving dummies and may ignore still prey (R1 Lettvin 1959, Ingle 1973, Roth and Wiggers 1983). Written for those animals; no line shows it for treefrogs, so the wording should say "frogs and toads that have been tested".
- [g] Speed. Cane toads fuse a flicker above about 7 Hz (R1 Inger 2014, grade g, a compiled figure). Rule 1: state it for the cane toad only. Wanted: Nowak and Green 1983 (toad rods) as the primary source.
- [g] Pupil. True toads have a horizontal pupil (R1 Thomas 2021). Ranids and treefrogs are not in the log; wanted: Cervino 2021.
- [i] Field of view and sharpness. Acuity: leopard frog 2.8 and common frog 4.3 (R1 Aho 1997, g); Japanese treefrog 0.9 to 2.1 (R1 Pushchin 2019). Numbers do not travel; treefrogs keep a guessed value.

## 4. Reptile view (split proposals)

Turtle (Trachemys scripta elegans measured; Pseudemys, Sternotherus, Chelydra carry only by rule 2 from order Testudines where families agree, which is not yet shown):
- [m] Colour. Four cone kinds with peaks at 372 (ultraviolet), 458, 515 and 617 nm, red and orange oil droplets in the red cones (R1 Loew and Govardovskii 2001, five lines).
- [m] Sharpest spot. A horizontal band across the retina, level with the eye's long axis (R1 Peterson and Ulinski 1979); electrophysiology gives 4.4 to 9.9 cycles per degree (R1 Northmore 1991).
- [m] Pupil: enlarges three- to four-fold in the dark (R1 Granda 1995).
- [g] Loggerhead: forages in mid-water by day, turning toward prey about 5.7 m away on average (new line, Narazaki 2013); sea turtles express more blue-sensitive opsin than freshwater turtles (new line, Terai 2023).

Lizard (anoles): R1 lines hold ultraviolet cone at 365 nm for 17 Caribbean Anolis (g by order) and A. carolinensis 358; two foveae; acuity 1.21 cycles per degree in the brown anole's periphery and about ten times that in the fovea of the green anole (R1 Fleishman 2017, the second number is derived). Fence lizards and skinks have no Alachua measurement; the African skink Trachylepis has an all-cone retina (new line, El-Bakary 2023), which does not carry to Scincella or Plestiodon by rule 3.

Gecko: Hemidactylus turcicus UV cone 363 to 366 nm (R1 Loew 1996); Tarentola gecko colour at night and multifocal slit pupil (R1 Roth and Kelber 2004, Roth 2009). Genus Hemidactylus (garnotii, mabouia) takes pupil and pigment by rule 3 and 2 only partly; flagged.

Snake: pine snake Pituophis melanoleucus has two cone opsins (UV 370 nm and 534 nm) and a rhodopsin at 481 nm in an all-cone retina (new lines, Bhattacharyya 2017); garter snake Thamnophis has the same kind of retina (R1 Schott 2016). Colubrids and vipers therefore see with two cone colours plus a blue-shifted rhodopsin; the current reptile view's "violet tint" is a guess that fits the UV cone but not the colour count, and the lens of day-active snakes filters UV (R1 Simoes 2016). Acuity: ball python 0.13, northern water snake 4.25 cycles per degree (R1 Gomez 2024); not transferable.

Pit vipers (infrared overlay): R1 holds Crotalus oreganus, Gloydius, Agkistrodon contortrix and Crotalinae lines (threshold 0.003 C, strikes launched from 0.5 to 8.5 m). Rule 3 gives Crotalus a pit overlay; cottonmouth and pigmy rattlesnake are the same subfamily, a rule 4 exception proposed in `carry.jsonl`.

## 5. Mostly borrowed after this pass

Alligator (sharpness, field, pupil), green treefrog and squirrel treefrog (everything except opsin genes and one pigment pair), Cuban treefrog, southern toad, ground skink and five-lined skink, fence lizard, cooter and redbelly turtles, gopher tortoise, cottonmouth, rat snake, green iguana (parietal eye only).

## 6. Wanted

See `docs/views/wanted/herps-met.jsonl` (29 lines).

## 7. Sources

Opened in this unit (collection full text or abstract): Schott 2022 (full text), Bhattacharyya 2017 (full text), Terai 2023 (full text), Narazaki 2013 (full text), El-Bakary 2023 (full text), Wan 2013 (full text). Round-1 sources as in `research/herps`.

## 8. Question for a specialist

Does the saltwater crocodile's three-class result (Nagloo 2016) reflect a different method from Sillman and Ronan's four in the alligator, or a real difference between the families?
