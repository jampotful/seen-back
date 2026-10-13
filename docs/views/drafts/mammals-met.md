# mammals-met: the deer, cat, dog, squirrel and rabbit views, species by species

Round 2, 13 October 2026. Sources in the logs are cited as `sdr#N` (docs/views/evidence/squirrel-deer-rabbit.jsonl, line N), `cd#N` (cat-dog.jsonl), `mg#N` (mammal-groups.jsonl) and `mm#N` (this unit's mammals-met.jsonl). Lines marked "pending" lean on a paper on `docs/views/wanted/mammals-met.jsonl`. Records per species could not be counted: GBIF, Europe PMC, PMC and science.org were refused by the egress proxy this session, so species are ranked by order-level counts in `docs/views/world-orders.csv` (Rodentia 1.41 M, Artiodactyla 0.96 M, other Carnivora 0.44 M, Lagomorpha 0.34 M, Canidae 0.30 M, Felidae 0.17 M, Equidae 0.04 M) and by what a person in Alachua County meets.

## 1. Scope and where the views should split

Species met most, Alachua County and the south-east US first: white-tailed deer, domestic cattle and horses (pasture and fence-line photographs), goats and sheep; domestic cat, bobcat, Florida panther; domestic dog, coyote, red and grey fox; eastern grey squirrel, fox squirrel, southern flying squirrel, cotton rat, cotton mouse, house mouse, brown and black rat, nutria, beaver; eastern cottontail and marsh rabbit. Worldwide the lent views add lions, tigers, leopards and cheetahs (safari records), zebras, giraffes, camels and llamas, wolves, European hares and the ground squirrels and marmots of the west.

Recommended splits, each with the evidence:

1. **Cat view: round-pupil and slit-pupil cats.** The cat row says a cat's pupil closes to a vertical slit. That is measured in the domestic cat (`cd#20`, `cd#48`) and false for tiger (round, `cd#49`), lion (round; one post-mortem description of a horizontal ovoid, `cd#103`, `cd#123`), Pallas's cat (round, `cd#124`) and cheetah (round, pending Banks 2015). Lynx lynx is intermediate (`cd#50`) and the genus Lynx is described as vertically elongated but subcircular (`cd#137`). Split by genus: *Felis*, small cats and *Lynx* take 'v'; *Panthera* and *Acinonyx* take 'o'. Puma concolor is unmeasured in the logs (wanted). Share of records: the lion, tiger, leopard and cheetah carry a large share of Felidae records outside the US; nothing here counts them.
2. **Dog view: foxes apart from dogs, wolves and coyotes.** Red fox has a vertical slit with a multifocal lens (`cd#51`, `mm#10`), where dogs and wolves have a round pupil (`cd#52`, `cd#53`, `mm#9`). The red fox has an area centralis and only a moderate streak, peak acuity 6.3 cpd (`cd#39`, `cd#41`, `cd#173`) against the dog's pronounced streak in long-nosed breeds (`cd#36`, `cd#37`). Split by genus: *Canis* (dog, wolf, coyote) round pupil and band; *Vulpes* slit pupil and a mild band over a central spot. *Urocyon* (grey fox, common in Alachua County) has only a Wikipedia statement of an oval pupil (`cd#104`, not usable) and its own cone pigments are measured only in the island fox (`cd#114`, `cd#115`).
3. **Squirrel view: three views in one.** Day-active sciurids (ground squirrels, chipmunks, marmots, prairie dogs, tree squirrels), the night-active rodents (mice, rats, cotton rats, flying squirrels) and the large hystricomorphs and beaver. The evidence for splitting: flicker fusion 108 to 120 Hz in the golden-mantled ground squirrel and 100 to 108 in the chipmunk (`sdr#5` to `sdr#10`), 60 to 65 Hz in the red squirrel, a tree squirrel (`sdr#7`, `sdr#11`), 39 Hz in the rat and 25 Hz in the albino rat (`sdr#8`, `sdr#13`), 10 to 15 Hz in the flying squirrel (`sdr#133`); acuity about 1 cpd in the rat and 0.5 cpd in the mouse (`sdr#64`, `sdr#67`); mouse and rat short cones peak in the ultraviolet near 360 nm (`sdr#68`, `sdr#84`), where squirrels have a violet-blue cone at 437 to 465 nm behind a yellow lens (`sdr#46`, `sdr#126`); mouse and rat lenses pass 56 to 81 percent of ultraviolet A (`sdr#19` to `sdr#21`). Guinea pig acuity is 0.75 to 1.65 cpd (`mm#13`). The speed row at rate 0.56 is correct for ground squirrels and chipmunks and wrong for every tree squirrel and every mouse.
4. **Deer view: keep one picture, write rows per species group.** The picture does not need to split except possibly for camelids (the band of sharp vision, see below). Cervids, bovids and horses all show a horizontal pupil and a streak, so one picture is nearly right for each, while the numbers (field, acuity, binocular overlap) differ by species and travel nowhere.
5. **Rabbit view: keep, but write it from `sdr#73` to `sdr#81`.** All Leporidae are lateral-eyed with a visual streak; hares and cottontails are not measured for colour.

## 2. Existing views checked against the species they are lent to

### deer (lent to Cervidae, Bovidae, Equidae, Antilocapridae, Camelidae, Giraffidae)

| Row | Status | Notes |
|---|---|---|
| Colour: "White-tailed deer have two kinds of colour-sensing cells" | confirmed for white-tailed deer, fallow deer (`sdr#117` to `sdr#119`), cattle, goat, sheep (`sdr#95`, `sdr#96`), horse (`sdr#90`, `sdr#91`), and pig (`mg#125`, `mg#126`) | Carry to camelids, giraffe and pronghorn by an order-level exception (carry.jsonl). The claim that "reds and oranges look yellow or grey" is an inference from a dichromat matrix, graded `g` at best. The matrix DEUTAN is entered from memory per the view file. |
| Field of view 310 degrees, graded `m` | unsupported | The only source in the log is a hunting website (`sdr#121`, graded `g`). No peer-reviewed field is in the logs for any deer. Measured: horse is near-complete with a 65 to 80 degree binocular overlap (`sdr#148`, `sdr#149`); sheep field was measured by Piggins and Phillips but the figure is not in the abstract (`mm#5`). |
| Pupil: horizontal bar | confirmed for white-tailed deer (`sdr#116`), reindeer (`sdr#113`) and horse (`sdr#152`) | Sheep, goat, cattle, camelid and giraffe pupils are not in the logs; the carry is proposed pending Banks 2015. |
| Sharpness (cpd 8) | unsupported as one number | Numbers never travel. Measured: white-tailed deer 4 to 6 cpd (`sdr#100`), horse 16.5 (`sdr#92`) and 23.3 in the best horse (`sdr#150`), sheep 14 by a review (`sdr#147`) and 0.085 to 0.19 in a behavioural paper whose units need checking (`sdr#135`), cattle and camel 2.6 to 5 by a review (`sdr#151`), dromedary 9.5 to 10 (`sdr#105`), alpaca 12.5 to 13.4 (`sdr#106`), giraffe 25 to 27 (`sdr#104`). |
| Sharpest band (topoS) | confirmed for white-tailed deer (`sdr#97`), horse (`sdr#94`, `sdr#111`, `mm#6`) and sheep (`mm#1`) | Measured disagreement to log: round 1 records a vertical streak (anakatabatic area) as common in Artiodactyla (`sdr#108`); the camel and alpaca bands are not measured here. |
| Dim light (gain 1.5) | confirmed that deer, sheep and horse have a tapetum fibrosum (`sdr#98`, `mm#2`, and Fosbury's reindeer records) | Johnson 1901 places Camelidae and pigs among animals with a red fundus and no coloured tapetum (`mm#12`, an 1901 survey, abstract only). Do not carry a tapetum row to camelids until checked. |

### cat

| Row | Status |
|---|---|
| Sharpness, "a fifth to a tenth of a person's" | confirmed for the domestic cat (`cd#18`, `cd#19`, `cd#86`); the cheetah is 23 cpd by anatomy (`cd#94`), so the row cannot be lent to big cats |
| Colour, two kinds | confirmed for the domestic cat (`cd#69` to `cd#73`); S cones labelled in cheetah, bobcat and leopard (`cd#138`); carry to lion, tiger and cougar by exception |
| Pupil, vertical slit | confirmed for the domestic cat only; false for Panthera and Acinonyx (above) |
| Field 200 degrees | confirmed for the domestic cat (`cd#77`, `cd#132`); other cats unmeasured |
| Dim light, 6 to 8 times | confirmed for the domestic cat (`cd#134`, `cd#80`); a tapetum is measured in the lion (`cd#122`) but the figure does not travel |

### dog

| Row | Status |
|---|---|
| Sharpness | confirmed for the domestic dog (`cd#29` to `cd#31`, `cd#166` to `cd#169`) and shown to vary with breed: whippet 6.7 to 15.8 cpd, pug 19.5 (`cd#167`, `cd#168`). Red fox 6.3 cpd (`cd#173`). No wolf or coyote figure. |
| Sharpest spot | confirmed for the domestic dog and wolf (`cd#37`, `cd#38`); red fox differs (`cd#39`) |
| Colour (graded `i`) | can be raised to `m` for the dog (`cd#64` to `cd#67`) and to `m` for red fox, Arctic fox and island fox (`cd#110` to `cd#115`). |
| Field 240, dim light, depth | field 240 degrees for the dog (`cd#79`); binocular 80 to 116 degrees in some breeds (`cd#33`) |

### squirrel and rabbit

Squirrel colour row: confirmed for fox squirrel, grey squirrel, ground squirrels (`sdr#47` to `sdr#52`, `sdr#126` to `sdr#131`); for mice and rats the second class is ultraviolet (`sdr#68`, `sdr#84`), so the row is not true of them as written. Speed row: confirmed for the ground squirrel and chipmunk only; red squirrel 60 to 65 Hz contradicts it for tree squirrels. Field and sharpness `i` row: now partly measured: rat 295 degrees with 90 degrees of binocular overlap (`sdr#70`, `sdr#71`), ground squirrel streak with 40 to 44 thousand photoreceptors per mm2 (`sdr#44`), 13-lined ground squirrel acuity guessed at 14 cpd (`sdr#125`, graded `i`). Rabbit: row graded `i` can now be written from `sdr#73` to `sdr#81`.

## 3. Draft rows, second person, by species or group

Each row is followed by its log lines. Grade is for the species named at the head. A row marked `[carry]` is graded `g` and names the relative.

### Deer view

**White-tailed deer (*Odocoileus virginianus*)**
- `m` Colour. You have two kinds of colour-sensing cell, one most sensitive near 450 to 460 nm and one near 537 nm, where a person has three. (`sdr#117`, `sdr#118`)
- `m` Pupil. Your pupil is a horizontal slit. (`sdr#116`)
- `m` Sharpest band. Your cones are packed into a horizontal band across the middle of the eye, and your short-wavelength cones are spread evenly. (`sdr#97`)
- `m` Sharpness. You resolve about 4 to 6 cycles per degree, a person about 60. (`sdr#100`; the estimate is from a review, so check the primary before final wording)
- `m` Dim light. Your eye has a reflecting layer behind the retina that sends light through it a second time. (`sdr#98`)
- `i` Field of view. No measured number is in hand; the 310 degrees on this page's source is a hunting site. Say the view is a guess, wide on both sides.

**Fallow deer, reindeer, moose and other deer.** Colour `g` carried from white-tailed deer (`sdr#119` measured in fallow, 542 nm). Reindeer: you also respond to ultraviolet through your rods and cones (`sdr#107`, `sdr#145`), and your tapetum colour shifts with the season (`sdr#112`, `sdr#114`, `sdr#170`); say so only for *Rangifer*.

**Horse (*Equus caballus*) and donkey, zebra [carry from horse within *Equus*]**
- `m` Colour. You have two kinds of colour-sensing cell, peaking at 428 and 539 nm. (`sdr#90`, `sdr#91`)
- `m` Field of view. You see nearly all the way around, with blind spots only directly behind and just in front of the forehead, and a binocular overlap of 65 to 80 degrees. (`sdr#148`, `sdr#149`)
- `m` Pupil. In daylight your pupil is a horizontal ellipse. (`sdr#152`)
- `m` Sharpest band. Your ganglion cells are densest in a horizontal streak, so you see best along the horizon; the density varies with the length of the nose across breeds. (`sdr#94`, `sdr#111`, `mm#6`)
- `m` Sharpness. The best horse measured resolved 23.3 cycles per degree; one summary gives 16.5. (`sdr#150`, `sdr#92`. Two papers disagree, so wording says "about 16 to 23".)
- `m` Dim light. In dim light you can still tell colours apart; one pony did so at 0.08 cd/m2, about the level of moonlight. (`sdr#110`, `sdr#153`)

**Cattle, goats and sheep (Bovidae)**
- `m` Colour. You have two kinds of colour-sensing cell, with the short peak between 444 and 455 nm and the long peak between 552 and 555 nm. (`sdr#95`, `sdr#96`)
- `m` Sheep: sharpest band and tapetum. In the sheep a horizontal streak and a central spot hold the densest ganglion cells (about 18,000 per mm2 in the central spot), and a reflecting layer sits above the optic disc. (`mm#1`, `mm#2`)
- `m` Sheep: focus. A sheep has no measurable focusing for near objects, and its eye is only slightly long-sighted. (`mm#4`)
- `g` Cattle and goat: sharpest band [carry]. Sheep have a horizontal streak, and Hebel's pig, sheep, ox, horse and dog ganglion maps (wanted) would settle cattle.
- `i` Field and acuity of cattle and goats. Nothing opened gives a figure; the logs hold only a review's 2.6 to 5 cpd for cattle and camel (`sdr#151`).

**Camelids, giraffe, pronghorn.** Colour `g` by order-level exception (carry.jsonl). Alpaca acuity 12.5 to 13.4 cpd (`sdr#106`), dromedary 9.5 to 10 (`sdr#105`), giraffe 25 to 27 (`sdr#104`): each stated only for its own species. Giraffe long-wavelength cone predicted from a gene, 5 nm longer than in relatives (`sdr#171`, `g`). Pupil and tapetum: `i`. Johnson 1901 puts Camelidae in the red-fundus group (`mm#12`).

### Cat view

**Domestic cat.** `m` two cone classes at 450 and 550 nm (`cd#69`, `cd#70`); `m` vertical slit that changes area about 135-fold (`cd#20`, `cd#21`); `m` field of 200 degrees and 140 degrees of overlap (`cd#77`, `cd#78`); `m` threshold six to eight times lower than a person's (`cd#134`); `m` acuity 3 to 9 cycles per degree (`cd#18`).

**Lion, tiger, leopard, jaguar, cheetah, cougar, bobcat.**
- `g` Colour [carry]. You have a short-wavelength cone and a long-wavelength cone, as the cheetah, bobcat and leopard do. (`cd#138`)
- `m` Tiger and `m` Pallas's cat pupil. Your pupil stays round. (`cd#49`, `cd#124`) Lion: round on the evidence of two summaries and one horizontal-ovoid description from dead tissue (`cd#103`, `cd#123`); say `g` for lion within *Panthera* (rule 3).
- `m` Lion tapetum. Your reflecting layer is made of cells and is the largest of the species in that survey. (`cd#122`)
- `m` Cheetah. You have a horizontal streak of M cones and an anatomical acuity of about 23 cycles per degree. (`cd#97`, `cd#94`)
- `m` Bobcat/Lynx. A *Lynx* pupil is an intermediate oval (`cd#50`, `cd#137`).
- No measured field, acuity or sensitivity figure for lion, tiger, cougar or bobcat; the domestic cat's numbers do not travel (rule 1).

### Dog view

**Domestic dog.** `m` two cone classes at 429 and 555 nm (`cd#64` to `cd#66`); `m` round pupil (`cd#53`); `m` flicker fusion 75 to 80 Hz (`cd#27`, `cd#28`); `m` binocular overlap 30 to 60 degrees in some breeds and 80 to 116 in others (`cd#32`, `cd#33`); `m` acuity from 5.5 to 19.5 cycles per degree by breed (`cd#166`).

**Wolf and coyote (*Canis*).** `m` for wolf: your pupil is round (`cd#52`) and your streak is pronounced (`cd#38`). `g` for coyote [carry within genus]: round pupil, streak. Coyote's own measurement is a dim-light threshold (`cd#43`); no coyote pigment or acuity is logged.

**Red fox, Arctic fox.** `m` Your pupil is a vertical slit (`cd#51`, `mm#10`). `m` You have an area centralis and a moderate streak, and 6.3 cycles per degree in the red fox (`cd#39`, `cd#41`, `cd#173`). `m` Cones at 430 to 435 and 555 nm (`cd#110` to `cd#113`).

**Grey fox (*Urocyon*).** `m` for the island fox only: cones at 430 to 435 and 555 nm (`cd#114`, `cd#115`). Everything else `i`, with the pupil flagged as unconfirmed.

### Squirrel view

**Ground squirrels, chipmunks.** `m` Flicker fusion 100 to 120 Hz in golden-mantled ground squirrel and chipmunk (`sdr#5` to `sdr#10`), so you see a light flicker that looks steady to a person; `m` two cone classes at about 437 and 519 nm (`sdr#126`, `sdr#127`); `m` yellow lens absorbs all ultraviolet (`sdr#46`); `m` cones outnumber rods about six to one with a horizontal streak (`sdr#44`, `sdr#45`).

**Grey and fox squirrels (*Sciurus*).** `m` two cone classes at 444 and 543 nm in the grey squirrel and 450 and 540 in the fox squirrel; `m` a spectral neutral point; `m` the grey squirrel lens passes no ultraviolet A, with half of the light cut off at 441 nm (`sdr#15`). Flicker fusion is not measured for either. The red squirrel, another tree squirrel, is 60 to 65 Hz (`sdr#7`, `sdr#11`), so this view should not run slow for them.

**Mice and rats.** `m` Rat: flicker fusion 39 Hz (`sdr#13`), 25 Hz in albino rats (`sdr#8`); acuity about 1 cycle per degree in pigmented rats (`sdr#64`, `sdr#159`), 0.5 in mice (`sdr#67`); a field of about 295 degrees with 90 degrees binocular (`sdr#70`, `sdr#71`); short cone in the ultraviolet near 360 nm, M cone near 502 to 511 (`sdr#68`, `sdr#69`, `sdr#82` to `sdr#85`). Rats and mice are `m` only for their own species. Wild house mice and cotton rats are not logged for vision.

**Flying squirrels.** `m` for the southern flying squirrel: photopic peak 520 nm and a flicker fusion of 10 to 15 Hz (`sdr#132`, `sdr#133`).

**Beaver, nutria, capybara, porcupine.** Beaver acuity 17 cpd (`sdr#59`, Castor fiber, European); capybara a poorly developed streak, oval vertical pupil and no tapetum (`sdr#163`, `sdr#166`); guinea pig 0.75 to 1.65 cpd (`mm#13`), peak ganglion density 1,621 per mm2 (`mm#14`). Nutria is unmeasured.

### Rabbit view

**European rabbit (*Oryctolagus*).** `m` field about 360 degrees with 24 degrees of overlap (`sdr#73`, `sdr#74`); `m` a visual streak (`sdr#75`); `m` two cone classes at 425 and 523 nm (`sdr#79`, `sdr#80`); `m` your lens passes about 13 percent of ultraviolet A (`sdr#24`).
**Cottontails.** `m` a broad visual streak along nearly the whole eye (`sdr#40`); everything else `g` [carry from rabbit, pending acceptance].
**Hares and pikas.** `g` cones are present (`sdr#88`); colour and field `i`.

## 4. Species with enough for a profile of their own

Horse (colour, field, streak, acuity, pupil, dim light), white-tailed deer, domestic cat, domestic dog, red fox (pupil, streak, acuity, pigments), black-tailed/golden-mantled ground squirrel and chipmunk (flicker, pigments, streak), grey squirrel (pigments), rat (field, acuity, flicker), European rabbit, sheep (streak, tapetum, focus).

## 5. Gaps and how to fill them

- **Deer field of view.** No peer-reviewed deer field is in the logs. Nearest measured: horse (near-complete) and sheep (measured, figure in the full text of Piggins and Phillips). Infer from skull position only as `i`.
- **Pupil of the goat, cattle, camelids, coyote, grey fox, cougar.** Banks 2015 species table (wanted, priority 1).
- **Tapetum of camelids and rodents.** Johnson 1901 (`mm#12`) and Ollivier 2004 (round 1) disagree on some of the detail; the paca has one (`sdr#164`).
- **Tree squirrel flicker and acuity.** Jacobs 1982 (wanted). Nearest: red squirrel flicker 60 to 65 Hz; do not carry the ground squirrel's 108.
- **Hare and pika.** No measurement in the collection. Nearest: rabbit and cottontail, carried by exception only.
- **Sheep acuity.** Two logged values differ by a factor of about a hundred (`sdr#135`, `sdr#147`); the behavioural papers (Tanaka 1995, Sugnaseelan 2013) are on the wanted list.
- **Cattle, goat and horse ganglion maps.** Hebel 1976 (wanted).

## 6. Closed sources wanted

See `docs/views/wanted/mammals-met.jsonl` (23 lines, priority 1 first).

## 7. Sources opened in this unit

Opened (abstract on the collection index): Shinozaki 2010 sheep retina; Piggins and Phillips 1996; Evans and McGreevy 2006; de Oliveira 2014 rock cavy; Jnawali 2021 guinea pig; Günter 2025 gerbil; Johnson 1901. Opened (full text): Paszta 2021 painted dog; Tabin 2024 (read only for its source of pupil data, Banks 2015, which it did not reproduce); Roth 2025 horse review (already logged in round 1). Round-1 logs are secondary to this sheet and are cited by line.

## 8. Questions for a specialist

1. Does a horizontal pupil hold for all Bovidae and Camelidae, or only for grazers in the survey?
2. Is the camelid band of sharp vision vertical, as the Artiodactyla thesis predicts, or horizontal?
3. Do tree squirrels (*Sciurus*) fuse flicker nearer 60 Hz, like the red squirrel, or nearer 100 Hz, like ground squirrels?
4. What is the pupil of the coyote and the grey fox?
5. How many cone classes do hares have?
