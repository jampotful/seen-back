# Sensing sheet: fungus (kingdom Fungi, lichens included), with slime moulds

This sheet was written on 12 October 2026, from 08:51 to 09:23 UTC (04:51 to 05:23 EDT). Unfinished items are marked **[unfinished]**, and they are these:

- **Touch has no row.** Two pages on how the bean rust fungus reads ridges on a leaf surface (a PubMed search page and a 1991 *Phytopathology* abstract on apsnet.org) were refused by the fetch tool's content filter, so I could not open them.
- **Pages I could not read:** four Europe PMC searches and the 2011 *IMA Fungus* review PDF were refused with HTTP 429 (rate limited); several PMC article pages returned a browser check (PMC4401583, PMC1456503, PMC1315395, PMC6976561); the iNaturalist API was refused (robots rule) and the GBIF and NCBI APIs were refused from the shell (proxy 403); the Wiley page for Solhaug and colleagues (2003), the PNAS page for Fleissner and colleagues (2009) and the BioOne page on the Physarum phytochrome-like receptor all failed to load.
- **No species counts for the world.** With the iNaturalist and GBIF APIs out of reach, the scope uses the order counts in the assignment and the repository's own tables.
- **No full action spectrum for any commonly photographed fungus.** The split gill was tested at four wavelengths only, and the colour weights of the picture are invented.
- **No time course for a mushroom stem bending toward light.** The split gill's stalk is shown to bend toward light, and every timed or threshold figure for bending toward light comes from the pin mould Phycomyces.
- **Electrical spiking rests on one paper opened** (Adamatzky and Gandia, 2022). The earlier intracellular recordings (Olsson and Hansson, 1995) are secondary.

## 1. Scope

**What the proposed view holds.** iNaturalist research-grade records worldwide in GBIF, read 11 October 2026 (assignment and `docs/VIEWS.md`):

- Fungus and lichen hold 4,768,141 records, 2.81% of all records, the largest group with no view.
- Slime moulds hold 113,223 records, 0.07% of all records.

**Fungi by order** (assignment): Agaricales 1,586,444 (gilled mushrooms); Polyporales 779,676 (bracket fungi); Lecanorales 396,543 (lichens); Boletales 267,190; Russulales 234,388; Pezizales 132,365 (cup fungi); Teloschistales 127,346 (lichens); Helotiales 108,911; Pucciniales 99,519 (rusts); Peltigerales 89,412 (lichens).

From `docs/views/world-orders.csv`, summed by class:

- Agaricomycetes (mushrooms, brackets, puffballs, stinkhorns) hold 3,275,167 records, 68.7% of the fungus group.
- Lichens hold about 791,052 records, 16.6%. This is my own sum of the classes Lecanoromycetes (756,310), Arthoniomycetes (20,229), Candelariomycetes (8,523) and Lichinomycetes (934), plus the orders Verrucariales (4,261) and Pyrenulales (795). It miscounts the few lichens in other classes and the few non-lichens in these.
- The moulds that the light measurements come from are rarely photographed: Mucorales, which holds the pin mould Phycomyces, has 3,227 records and Eurotiales, which holds Aspergillus, has 1,338.

**Slime moulds by order** (same file): Physarales 49,284; Ceratiomyxales 27,114; Cribrariales 17,276; Trichiales 14,170; Stemonitidales 5,255; Echinosteliales 123; Dictyosteliales 1. GBIF files them under Protozoa, phylum Mycetozoa, apart from the fungi.

**Alachua County** (`docs/views/no-view-us-fl-alachua.csv`): the fungus group has 599 species and 4,483 records. The most recorded are the Christmas lichen *Herpothallon rubrocinctum* (414, Arthoniales), the Ringless Honey Mushroom *Desarmillaria caespitosa* (281, Agaricales) and the Tropical White Polypore *Favolus tenuiculus* (167, Polyporales), then *Cerrena hydnoides* (138), the column stinkhorn (136), the Green-spored Parasol (132), snow fungus (127), golden reishi (101) and turkey-tail (94). Slime moulds have 15 species and 184 records, led by Common Coral Slime *Ceratiomyxa fruticulosa* (72) and Dog Vomit Slime Mold *Fuligo septica* (66).

**Where the measurements come from.** Most figures were measured in laboratory organisms: the moulds *Neurospora crassa* and *Aspergillus nidulans*, the pin mould *Phycomyces blakesleeanus*, the gilled mushroom *Coprinopsis cinerea* (published earlier as *Coprinus cinereus*) and the slime mould *Physarum polycephalum*. Three common species add field-relevant figures: the split gill *Schizophyllum commune* (76 Alachua records, tied for eleventh in the group there), the field mushroom *Agaricus campestris* and the orange lichen *Xanthoria parietina*. I found nothing measured in the Christmas lichen, the Ringless Honey Mushroom or the Tropical White Polypore.

**Light direction is weaker on the ground.** Moore (1994) writes that "the stems of ground agarics (gilled mushrooms) are generally non-phototropic but show a marked negative gravitropism", while "lignicolous and coprophilous hymenomycetes are often both phototropic and gravitropic". Fungi on wood and dung, which include the bracket fungi and the split gill, are the best fit for a view that shows where light comes from.

**Can one view be true for mushrooms and lichens?** It can. The picture this sheet proposes claims no image, light read through blue and green, its direction, and a slow pace. Each of those rests on fungal measurements (blue receptor, bending toward light, responses over minutes to hours). A lichen is a fungus housing algae, and nothing in it forms an image either. What sets lichens apart is carried by rows: the algae inside, the orange pigment that screens blue light from them, and their waking only when wet. The weakest point is colour. Blue and green steer a mushroom stalk and red does not, but that was measured in one mushroom, and the lichen pigment filters blue out before it reaches the algae, so the blue-weighted picture is least certain for lichens. That is a reason for a row, and it is too thin to justify a third entry.

**Can slime moulds share it?** They cannot. A slime mould is one large cell that crawls. It moves away from blue and far-red light and toward red (Hato and colleagues, 1976), it turns toward light when starved (Leitner and colleagues, 2002), and its body pulses every one to two minutes (Kuroda and colleagues, 2015). Fungi bend toward blue light over minutes to hours. The colour, the direction of the response and the pace all differ, and every fungus row would be false for it because it is not a fungus.

**Recommendation.** Build one view, `fungus`, for the whole kingdom Fungi, lichens included. Give the slime moulds (Myxomycetes and Ceratiomyxales) a small entry of their own, `slime`, which uses the same no-picture mode with its own colour, pace and rows. The line falls at the kingdom boundary, and the commonest members are on the fungus side: 4,768,141 records against 113,223, or 97.7% of the two together.

## 2. The rows

### `fungus`

```
['g', 'No picture', 'A fungus has no eye. Its cells read how much light there is, mostly blue and green, and which way it comes from.'],
```
Source: He and Liu, 2005: in *Neurospora crassa* "WC-1 is the blue-light photoreceptor", and the WC proteins "mediate almost all known light responses". Sanz and colleagues, 2009: in the pin mould *Phycomyces*, MADA (like WC-1) and MADB (like WC-2) form "the primary photoreceptor complex for fungal phototropism". No source I opened says in so many words that fungi lack an eye.

```
['m', 'Colour', 'The young stalk of the split gill mushroom bends toward violet and green light and ignores orange and red. Another gilled mushroom, Coprinopsis cinerea, needs a little blue light to make its cap, and in the dark it grows a long stem under an unfinished top.'],
```
Source: Schwalb and Shanler, 1974: the stipe of *Schizophyllum commune* was "positively phototropic to light of wavelengths 420 and 540 nm but not 600 or 660 nm". Moore, 2016: cap development "is normally dependent on illumination with low intensity blue light"; kept in continuous darkness, or lacking the *dst1* gene, the top stays rudimentary while the base elongates ("dark stipe"); the Dst1 protein resembles flavin-binding blue-light receptors.

```
['g', 'Red', 'Some moulds read red as well. Aspergillus nidulans uses phytochrome, the red receptor of plants, and red light holds back its sexual spores. The picture follows the mushrooms and leaves red dark.'],
```
Source: Blumenstein and colleagues, 2005: FphA binds biliverdin, acts as a red-light sensor and represses sexual development in red light (670 nm); dark red at 740 nm does not block it.

```
['g', 'Faint light', 'The stalk of the pin mould Phycomyces turns toward light as faint as a billionth of a watt on a square metre, and it still steers in light ten billion times brighter. The stalk is a clear cylinder that focuses about 30 per cent more light on its far side, and that difference turns it toward the light.'],
```
Source: Galland and Russo, 1984: threshold for bending 10⁻⁹ W/m² in stalks grown in the dark. Galland and Lipson, 1987, and Sanz and colleagues, 2009: a range of ten orders of magnitude. Shropshire, 1962: the cylindrical stalk gives its far side "a focusing advantage of about 30 per cent", and the stalk bends the other way when that advantage falls below 14 per cent.

```
['m', 'Down', 'A mushroom stem laid on its side starts to turn up in about 25 minutes and is upright again in 3 to 4 hours. The gills of Agaricus mushrooms turn back to hang straight down within an hour, so the spores fall clear.'],
```
Source: Kher and colleagues, 1992: mean reaction time 25.4 ± 13.1 minutes in *Coprinus cinereus*. Moore and colleagues, 1996: the apex "attains the vertical within 3 to 4 hours"; agaric stems are negatively gravitropic and the gills positively gravitropic. Moore, 1994: Buller "detected the gravitropic adjustment of the gills of Agaricus within an hour", and "Spores must fall vertically between the spines (hydnums) and gills (agarics)". The gills of *Coprinus* themselves do not respond to gravity (Moore, 1994), which is why the row names *Agaricus*.

```
['g', 'Pace', 'Genes that light switches on in the mould Neurospora peak 15 to 30 minutes later, and the pin mould stalk starts to bend within 5 minutes. Your eyes follow flicker to about 60 a second.'],
```
Source: He and Liu, 2005 (peak in 15 to 30 minutes; levels fall after 2 hours of constant light). Sanz and colleagues, 2009 (bending within 5 minutes). Inger and colleagues, 2014 (people about 60 Hz).

```
['m', 'Lichens', 'A lichen is a fungus with algae living inside it that feed it from light. The orange lichen Xanthoria parietina makes a pigment, parietin, that soaks up blue light and some ultraviolet before they reach its algae.'],
```
Source: Gauslaa and Ustvedt, 2003: parietin's two absorbance maxima lie in the UV-B and the blue, and "the blue light screening of parietin is functionally more important than the UV-B screening". Lange, Kilian and Ziegler, 1986, for lichens with green or blue-green algae taking up carbon dioxide by photosynthesis.

```
['x', 'Water', 'A lichen with green algae can wake from damp air alone, and one with blue-green algae needs liquid water. The picture does not show how wet anything is.'],
```
Source: Lange, Kilian and Ziegler, 1986: water vapour reactivated photosynthesis in every green-algal lichen tested, and the lichens with blue-green algae "required liquid water for CO2 assimilation" (73 and 33 species).

```
['x', 'Food', 'The threads of a wood-rotting fungus, Phanerochaete velutina, grow across soil to new wood. Moved to fresh soil, they regrow mostly from the side that had faced the wood. The picture has nothing for this.'],
```
Source: Fukasawa, Savoury and Boddy, 2020: regrowth from 67% of moved inocula, and "greater regrowth from the side that originally faced the new bait, implying memory of growth direction".

```
['i', 'Colour and time', 'Green counts for less than blue, dim light is lifted, and changes are averaged over about 20 seconds. A fungus answers light over minutes to hours, far slower than this. These choices are invented.'],
```
Source: the time scale comes from the Pace and Down rows. The colour weights, the lift and the 20 seconds are the app's choices; the removal of red rests on the Colour row.

### `slime`

```
['g', 'No picture', 'A slime mould is one huge cell, from a kingdom apart from the fungi. It has no eye, and it reads how much light falls on it and of what colour.'],
```
Source: Nakagaki, Yamada and Tóth, 2000 ("a large amoeba-like cell"); Hato and colleagues, 1976 (colour responses, below); the GBIF classification in `docs/views/world-orders.csv` (Protozoa, Mycetozoa).

```
['m', 'Colour', 'Physarum polycephalum crawls away from blue light and far-red light, and toward red light.'],
```
Source: Hato and colleagues, 1976: blue (peak 490 nm) and far-red (peak 720 nm) "induced negative taxis" and red (peak 650 nm) "led to positive taxis".

```
['m', 'Hunger', 'Well fed, it moves away from light. After several days without food it moves toward light, and light then turns it into spore heads.'],
```
Source: Leitner and colleagues, 2002: "In case of food limitation, plasmodia move towards light and differentiate into sporangia", and "Under optimal nutritional conditions plasmodia show a negative phototactical behavior". Masui, Yamamoto and Kono, 2025: *P. polycephalum* plasmodia "form fruiting bodies only after several days of starvation followed by light exposure".

```
['x', 'Food', 'It stretches tubes between pieces of food and finds the shortest route between them through a maze. The picture has no sense of food.'],
```
Source: Nakagaki, Yamada and Tóth, 2000.

```
['m', 'Pace', 'Its body swells and thins every one to two minutes, and its speed rises and falls over about 20 minutes. Your eyes follow flicker to about 60 a second.'],
```
Source: Kuroda and colleagues, 2015: thickness oscillates "with a period of 1–2 min", with slower oscillations of about 20 ± 10 minutes in speed, shape and period. Inger and colleagues, 2014.

```
['i', 'Colour and time', 'Green is removed and changes are averaged over about 6 seconds. Both choices are invented.'],
```
Source: none. Green was untested in the sources I opened, and the 6 seconds is the app's choice.

## 3. The picture

Proposed entries in the form of the plant entry. The rows are those of section 2.

```
var FUNGUS = [0, .4, .6, 0, .4, .6, 0, .4, .6];   // grey drawn from blue and green, no red (INVENTED weights)
fungus: { chip: 'Mushroom, lichen', who: 'a fungus', pupil: 'none', field: 1, M: FUNGUS, gain: 2, persist: 20,
  cue: 'There is no picture here, only how much blue and green light, and from where, slowly.', rows: [ ... ] }
slime: { chip: 'Slime mould', who: 'a slime mould', pupil: 'none', field: 1, noGreen: 1, persist: 6,
  cue: 'There is no picture here, only how much light, what colour, and from where.', rows: [ ... ] }
```

The chip and cue wording is invented.

**`fungus`**

| Field | Value | Behind it |
|---|---|---|
| `field` | 1 | No picture (g): He and Liu, 2005; Sanz and colleagues, 2009. The coarse sample keeps amount, colour and direction, and the Faint light row shows direction is sensed. |
| `pupil` | 'none' | Follows from the No picture row, as for the plant. |
| `M` | FUNGUS above | Red is dropped because the split gill's stalk ignores 600 and 660 nm (Colour row, Schwalb and Shanler, 1974), although the mould *Aspergillus* reads red (Blumenstein and colleagues, 2005). Green is kept because the same stalk bends toward 540 nm, and one of Phycomyces' two light systems works at 550 nm (Galland and Lipson, 1987). The weights 0.4 and 0.6 are **invented**; blue gets the larger share because WC-1 and Dst1 are blue receptors (He and Liu, 2005; Moore, 2016). The engine's matrices act row by row (see the BEE comment in `src/cam.a.js`), so equal rows give grey, and `sat` has nothing left to change. |
| `gain` | 2 | **invented**. It stands for sensitivity to faint light: a threshold of 10⁻⁹ W/m² in Phycomyces (Galland and Russo, 1984) and caps made under "low intensity blue light" (Moore, 2016). |
| `persist` | 20 (seconds) | **invented**. The real responses take 5 minutes to 4 hours (Sanz and colleagues, 2009; He and Liu, 2005; Kher and colleagues, 1992; Moore and colleagues, 1996). Twenty seconds is the app's choice and falls far short of the real pace. |
| `rate` | left at 1 | Nothing suggests a sense faster than a person's. |
| `fov`, `cpd`, `fovea`, `topoA`, `topoS`, `fall`, `dof`, `noGreen`, `uvBlue`, `sheen`, `gate`, `hold`, `thrust` | not set | The field mode replaces the image, so sharpness, field shape and focus have nothing to act on. Parietin absorbs UV-B (Gauslaa and Ustvedt, 2003), and a false-colour ultraviolet would add an invention with no fungal receptor behind it. |

**`slime`**

| Field | Value | Behind it |
|---|---|---|
| `field` | 1 | No picture (g): Nakagaki, Yamada and Tóth, 2000; Hato and colleagues, 1976. |
| `pupil` | 'none' | Follows from the No picture row. |
| `noGreen` | 1 | **invented**. Red and blue both steer it (Hato and colleagues, 1976); green was untested in what I opened. Red and blue stay in the picture. |
| `persist` | 6 (seconds) | **invented**. Its pulse runs at 1 to 2 minutes (Kuroda and colleagues, 2015), faster than a fungus and far slower than a person, so its averaging is set shorter than the fungus's. |
| `M`, `sat`, `gain`, `rate` | not set | No source I opened bears on them. |

## 4. What the engine cannot draw yet

- **Gravity.** A mushroom stem rights itself over 3 to 4 hours, and in many species the gills turn to hang straight down. The view could slowly turn the picture back to true vertical after the phone is tilted, sped up by an invented factor. The phone's motion sensors can stand in, through the browser's device orientation events. Judgement: moderate, because it needs a rotation step and, on some phones, a permission prompt.
- **Minutes and hours.** The real pace of a fungus is far slower than `persist` can hold. In `src/cam.b.js` the averaging weight is held at 0.2 or more when the phone lacks float textures, which keeps only a few frames. A low-rate store of frames (one every few seconds, averaged over ten minutes or more) would show it. The camera is the input. Judgement: moderate.
- **Toward or away.** The field mode shows where light comes from, and it cannot show what the creature does about it. Fungi bend toward light, a fed slime mould moves away and a starved one moves toward it. The whole field could lean slowly toward the brightest region for `fungus` and away from it for `slime`. The camera's coarse brightness map, which the engine already samples, is the input. Judgement: easy to moderate.
- **Nearness without contact.** A Phycomyces stalk bends away from an object 1 mm from its growing zone, whatever the object is made of and in light or dark (Cohen and colleagues, 1975). I know of no phone input that stands in. Judgement: not possible now.
- **Water.** A lichen is active only when wet (Lange and colleagues, 1986). No phone input measures how wet a surface is. A tap that "wets" the lichen would be pure invention. Judgement: not possible as a sense.
- **Food.** Mycelium reaches new wood and remembers its direction (Fukasawa and colleagues, 2020), and a slime mould joins pieces of food by the shortest route (Nakagaki and colleagues, 2000). No phone input stands in. Judgement: not possible.
- **Electrical spikes in mycelium.** Oyster mushroom mycelium (*Pleurotus ostreatus*) carries spikes of about 62 seconds and 0.48 millivolts (Adamatzky and Gandia, 2022). The engine could pulse the picture's brightness on that rhythm, but nothing on the phone would drive the pulses and the spikes are a signal inside the fungus, with no tie to the camera. Judgement: easy to draw and hard to justify, so I recommend leaving it out.
- **Bands the phone does not record.** Parietin absorbs UV-B, and a slime mould flees far-red. The app's plant entry already says a phone does not record far-red. Judgement: not possible with the camera.

## 5. Sources

1. He Q, Liu Y. 2005. Molecular mechanism of light responses in *Neurospora*: from light-induced transcription to photoadaptation. *Genes & Development* 19(23): 2888–2899. doi:10.1101/gad.1369605. https://genesdev.cshlp.org/content/19/23/2888.full.pdf. WC-1 is the blue-light photoreceptor; its LOV domain binds FAD; the WC proteins mediate almost all known light responses; light-induced genes peak in 15–30 minutes and fall after 2 hours of constant light. **opened**
2. Moore D. 2016. "2. Stem and cap morphogenesis in *Coprinopsis* fruit bodies", in *Coprinopsis: an autobiography*. davidmoore.org.uk. https://davidmoore.org.uk/Biog_01-02.htm. Cap development depends on low-intensity blue light; *dst1* mutants form "dark stipe"; Dst1 resembles flavin-binding blue-light receptors. **opened** (an author's summary; I did not open the primary *dst1* paper)
3. Blumenstein A, Vienken K, Tasler R, Purschwitz J, Veith D, Frankenberg-Dinkel N, Fischer R. 2005. The *Aspergillus nidulans* phytochrome FphA represses sexual development in red light. *Current Biology* 15(20): 1833–1838. doi:10.1016/j.cub.2005.08.061. https://www.iab.kit.edu/microbio/download/2005_Blumenstein_et_al.pdf. Red-light sensor with a biliverdin chromophore; red light (670 nm) represses sexual development and 740 nm does not. **opened**
4. Galland P, Russo VEA. 1984. Threshold and adaptation in *Phycomyces*: their interrelation and regulation by light. *Journal of General Physiology* 84(1): 119–132. doi:10.1085/jgp.84.1.119. Bending threshold 10⁻⁹ W/m² when grown in the dark, 2 × 10⁻⁷ W/m² under continuous light. **opened** (abstract)
5. Galland P, Lipson ED. 1987. Blue-light reception in *Phycomyces* phototropism: evidence for two photosystems operating in low- and high-intensity ranges. *PNAS* 84(1): 104–108. doi:10.1073/pnas.84.1.104. Two light systems split at 10⁻⁶ W/m²; latencies of 15, 40 and 50–70 minutes in stalks suddenly lit from one side; one system works better at 334, 347 and 550 nm; "the full range of 10 decades". **opened** (abstract)
6. Sanz C, Rodríguez-Romero J, Idnurm A, Christie JM, Heitman J, Corrochano LM, Eslava AP. 2009. *Phycomyces* MADB interacts with MADA to form the primary photoreceptor complex for fungal phototropism. *PNAS* 106(17): 7095–7100. doi:10.1073/pnas.0900879106. https://pmc.ncbi.nlm.nih.gov/articles/PMC2678449. Ten orders of magnitude; bending within 5 minutes; *madA* like WC-1, *madB* like WC-2; the stalk also responds to gravity. **opened**
7. Shropshire W Jr. 1962. The lens effect and phototropism of *Phycomyces*. *Journal of General Physiology* 45(5): 949–958. doi:10.1085/jgp.45.5.949. Focusing advantage of about 30 per cent on the far side for parallel light; bending reverses below 14 per cent. **opened** (abstract)
8. Cohen RJ, Jan YN, Matricon J, Delbrück M. 1975. Avoidance response, house response, and wind responses of the sporangiophore of *Phycomyces*. *Journal of General Physiology* 66(1): 67–95. doi:10.1085/jgp.66.1.67. An object 1 mm from the growing zone causes bending away, independent of its material, surface and the ambient light. **opened** (abstract)
9. Kher K, Greening JP, Hatton JP, Novak Frazer L, Moore D. 1992. Kinetics and mechanics of stem gravitropism in *Coprinus cinereus*. *Mycological Research* 96(10): 817–824. https://www.davidmoore.org.uk/Assets/Printed_documents/my_reprints/1992_Kher_etal_Kineticsmechanics_stem_gravitropism.pdf. Bending within 30 minutes; mean reaction time 25.4 ± 13.1 minutes; mean rate 0.22° per minute. DOI not seen. **opened**
10. Moore D, Hock B, Greening JP, Kern VD, Novak Frazer L, Monzer J. 1996. Gravimorphogenesis in agarics. *Mycological Research* 100(3): 257–273. https://www.davidmoore.org.uk/Assets/Printed_documents/my_reprints/1996_Moore_etal_Gravimorphogenesis%20in%20agarics.pdf. Stems negatively and gills positively gravitropic; *Coprinus* apex vertical within 3 to 4 hours; *Flammulina* re-orients within 12 hours; presentation time 7 minutes; nuclei proposed as gravity sensors. DOI not seen. **opened**
11. Gauslaa Y, Ustvedt EM. 2003. Is parietin a UV-B or a blue-light screening pigment in the lichen *Xanthoria parietina*? *Photochemical & Photobiological Sciences* 2: 424–432. doi:10.1039/B212532C. https://pubs.rsc.org/en/content/articlehtml/2003/pp/b212532c. Absorbance maxima in UV-B and blue; blue screening judged more important. **opened**
12. Lange OL, Kilian E, Ziegler H. 1986. Water vapor uptake and photosynthesis of lichens: performance differences in species with green and blue-green algae as phycobionts. *Oecologia* 71: 104–110. doi:10.1007/BF00377327. Green-algal lichens reactivated by water vapour; lichens with blue-green algae need liquid water. **opened** (abstract)
13. Fukasawa Y, Savoury M, Boddy L. 2020. Ecological memory and relocation decisions in fungal mycelial networks: responses to quantity and location of new resources. *ISME Journal* 14: 380–388. doi:10.1038/s41396-019-0536-3. https://orca.cardiff.ac.uk/id/eprint/125667/. Regrowth from 67% of moved inocula, more from the side that had faced the bait. **opened** (abstract)
14. Adamatzky A, Gandia A. 2022. Fungi anaesthesia. *Scientific Reports* 12: 340. doi:10.1038/s41598-021-04172-0. https://pmc.ncbi.nlm.nih.gov/articles/PMC8748941. *Pleurotus ostreatus* spikes: median duration 62 s, median amplitude 0.48 mV; chloroform vapour suppresses them. **opened**
15. Olsson S, Hansson BS. 1995. Action potential-like activity found in fungal mycelia is sensitive to stimulation. *Naturwissenschaften* 82: 30–31. Intracellular recordings of action-potential-like activity in hyphae. **secondary** (cited in Adamatzky and Gandia, 2022)
16. Inger R, Bennie J, Davies TW, Gaston KJ. 2014. Potential biological and ecological effects of flickering artificial light. *PLoS ONE* 9(5): e98631. doi:10.1371/journal.pone.0098631. People about 60 Hz. **opened**
17. Hato M, Ueda T, Kurihara K, Kobatake Y. 1976. Phototaxis in true slime mold *Physarum polycephalum*. *Cell Structure and Function* 1(3): 269–278. doi:10.1247/csf.1.269. Blue (490 nm) and far-red (720 nm) cause movement away, red (650 nm) movement toward. **opened** (abstract)
18. Nakagaki T, Yamada H, Tóth Á. 2000. Maze-solving by an amoeboid organism. *Nature* 407: 470. doi:10.1038/35035159. "A large amoeba-like cell" that connects two food sources by the minimum-length path through a maze. **opened** (abstract)
19. Kuroda S, Takagi S, Nakagaki T, Ueda T. 2015. Allometry in *Physarum* plasmodium during free locomotion: size versus shape, speed and rhythm. *Journal of Experimental Biology* 218(22): 3729–3738. doi:10.1242/jeb.124354. Thickness oscillates with a period of 1–2 minutes; slower oscillations of 20 ± 10 minutes. **opened**
20. Leitner S, Golderer G, Gröbner P, Werner-Felmayer G, Werner ER. 2002. Tetrahydrobiopterin, nitric oxide synthesis and cGMP concentrations in mutants of *Physarum polycephalum* with altered sporulation behavior. In Milstien S and colleagues (eds), *Chemistry and Biology of Pteridines and Folates*, Springer. doi:10.1007/978-1-4615-0945-5_39. Food-limited plasmodia move toward light and form sporangia; well-fed plasmodia move away from light. **opened** (abstract)
21. Masui M, Yamamoto P, Kono N. 2025. Loss of the starvation-and-light fruitbody formation trigger in the myxomycete *Physarum roseum*. Dataset, Dryad. doi:10.5061/dryad.hmgqnk9wh. *P. polycephalum* fruits only after several days of starvation followed by light. **opened** (dataset description; the paper it accompanies was not named there)
22. Chen S, Alim K. 2023. Network topology enables efficient response to environment in *Physarum polycephalum*. *Physical Biology* 20: 046003. doi:10.1088/1478-3975/accef2. The network moves out of blue light, which inhibits its metabolism. **opened** (not used in a row; it agrees with Hato and colleagues, 1976)
23. Adamatzky A. 2009. Steering plasmodium with light: dynamical programming of Physarum machine. arXiv:0908.0850. Strongest movement away from blue and white light; a threshold for blue near 1,500 lux. **opened**, and the figures in it are **secondary** (citing Bialczyk 1979, Schreckenbach 1984, Block and Wohlfarth-Bottermann 1981). Not used in a row.
24. Armstrong RA, Bradwell T. 2010. Growth of crustose lichens: a review. *Geografiska Annaler A* 92(1): 3–17. doi:10.1111/j.1468-0459.2010.00374.x. "Crustose species are the slowest growing of all lichens"; the abstract gives no rates. **opened** (not used in a row)
25. Schwalb MN, Shanler A. 1974. Phototropic and geotropic responses during the development of normal and mutant fruit bodies of the basidiomycete *Schizophyllum commune*. *Microbiology* 82(2): 209–212 (journal name as the publisher's page gives it). doi:10.1099/00221287-82-2-209. https://www.microbiologyresearch.org/content/journal/micro/10.1099/00221287-82-2-209. The stipe is positively phototropic at 420 and 540 nm and does not respond at 600 or 660 nm; gills develop facing downward. **opened** (abstract)
26. Moore D. 1994. Which way is up? Gravity sensing in basidiomycetes. In Nair MC, Gokulapalan C, Das L (eds), *Advances in Mushroom Biotechnology*, pp. 23–26. Scientific Publishers, Jodhpur. https://www.davidmoore.org.uk/Assets/Printed_documents/my_reprints/1994_Moore_which_way_is_upINDIAms.pdf. Ground agarics mostly non-phototropic, species on wood and dung often both phototropic and gravitropic; *Agaricus* gills readjust within an hour (after Buller); *Coprinus* gills are not gravitropic; spores must fall vertically between gills. **opened**
27. Repository tables read on 12 October 2026: `docs/VIEWS.md`, `docs/views/world-orders.csv` and `docs/views/no-view-us-fl-alachua.csv` in `the repository`, compiled from GBIF on 11 October 2026. Class sums, lichen sum and Alachua species counts. **opened** (local files)

## 6. Open questions

1. Has anyone measured a full action spectrum for cap making or stem bending in a commonly photographed mushroom, such as a honey mushroom or a polypore? The split gill was tested at four wavelengths, and where between 540 and 600 nm its response ends is unknown to me.
2. Does the fungus in a lichen read light itself through its own receptors, or is the algae's photosynthesis the lichen's only use of light? If the fungus reads it, does parietin change what it reads?
3. What is the threshold for blue light in *Coprinopsis cinerea* cap making, and is it anywhere near the 10⁻⁹ W/m² of Phycomyces?
4. Do the slime moulds most often photographed, *Ceratiomyxa* and *Fuligo*, share the colour responses measured in *Physarum polycephalum*, and does a slime mould sense anything once it has turned into spore heads?
5. Is the electrical spiking in mycelium a response to anything the fungus senses, such as light, gravity or wood, and has a second laboratory measured it in a commonly photographed species?
