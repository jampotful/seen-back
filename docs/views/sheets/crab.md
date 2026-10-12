# Sensing sheet: crab, woodlouse and other crustacean (Decapoda, Isopoda and relatives, with horseshoe crabs and sea spiders)

This sheet was written on 12 October 2026, from 14:05 to 14:34 EDT (18:05 to 18:34 UTC), inside the 50-minute limit. Unfinished items are marked **[unfinished]**, and they are these:

- **No scientific count of a woodlouse's facets was found.** The figure of 22 facets for the Rough Woodlouse (*Porcellio scaber*) comes from an electron micrograph on an amateur naturalist's page, whose species is identified only by a note on head shape. No interommatidial angle, colour measurement or flicker measurement was found for any woodlouse.
- **No measured experiment on how strongly woodlice avoid light or dry air was opened.** The rows rest on a 2025 field study's introduction, which cites the older experiments (Cloudsley-Thompson; Warburg) without my having opened them.
- **Pages I could not read.** The Europe PMC record of PMC9848968 (a woodlouse paper the searches kept returning) was refused by the fetch proxy as rate-limited (HTTP 429), and I did not retry it. The PubMed Central page of Brodrick and colleagues (2022) timed out on a permission request, so that paper was read from the publisher's PDF instead. The iNaturalist API refused the request (robots rule), and direct requests to the GBIF API from the shell were refused by the proxy (HTTP 403), so the GBIF counts below were read through the web fetch tool.
- **Statements without an opened source.** The row "Polarized light" says that a phone camera does not record polarization, and section 4 says that a web page cannot read humidity. I opened no source for either statement. (The ultraviolet rows rest on Igoe and colleagues, 2012, which found that a smartphone sensor does respond weakly to ultraviolet A, and that one phone's lens passed between 1.1% and 18.9% of it, so those rows say the phone keeps little of it.)
- **Taxa not researched.** I opened no source on the eyes of the American lobster (*Homarus americanus*), barnacles, amphipods, fairy shrimp, tadpole shrimp, copepods or sea spiders. Lobster figures come from slipper lobsters.
- **The crayfish's hundredfold night rhythm is secondary.** It comes from Garfias and colleagues (1995), who cite Rodríguez-Sosa and Aréchiga (1982). I did not open the 1982 paper.
- **Shore crab (*Carcinus maenas*) resolution was not found.** Only its spectral sensitivity was measured in a source I opened.
- **Audit, 12 October 2026, 18:51 to 19:40 UTC.** The audit could not open the abstract of Waterman and Fernández (1970), because the publisher refused the request (HTTP 429), or the 2020 correction by Anderson and colleagues, so the figures taken from them have been removed. The crayfish colours now rest on Eguchi, Waterman and Akiyama (1973) and Kingston and Cronin (2015). Every change is listed in `crab.audit.md`.

## 1. Scope

**What the group holds.** The group holds 1,232,045 iNaturalist research-grade records in GBIF (read 11 October 2026, from the assignment and `docs/views/world-orders.csv`).

| Order | Records | Share of group |
|---|---:|---:|
| Decapoda (crabs, crayfish, shrimp, lobsters) | 743,220 | 60.3% |
| Isopoda (woodlice, sea slaters) | 380,509 | 30.9% |
| Sessilia (acorn barnacles) | 36,997 | 3.0% |
| Pedunculata (goose barnacles) | 23,129 | 1.9% |
| Xiphosurida (horseshoe crabs) | 21,193 | 1.7% |
| Amphipoda | 12,269 | 1.0% |
| Stomatopoda (mantis shrimp) | 4,493 | 0.4% |
| All others (Anostraca 2,582, Notostraca 1,638, Pantopoda 651, Calanoida 213 and smaller) | 10,235 | 0.8% |

**Decapods, by family** (GBIF facet on the same dataset, read 12 October 2026; the total, 743,220, matches the order count). The column on the right says whether a source I opened measured a sharp band along the horizon in that family.

| Family | Records | Share of Decapoda | Horizon band (Zeil, Nalbach and Nalbach, 1986) |
|---|---:|---:|---|
| Grapsidae (rock crabs) | 76,044 | 10.2% | absent |
| Ocypodidae (fiddler and ghost crabs) | 59,350 | 8.0% | present |
| Cancridae | 51,284 | 6.9% | not measured |
| Cambaridae (crayfish) | 45,147 | 6.1% | not measured |
| Varunidae | 41,817 | 5.6% | not measured |
| Paguridae (hermit crabs) | 38,710 | 5.2% | not measured |
| Portunidae (swimming crabs) | 36,358 | 4.9% | absent |
| Carcinidae (shore crab) | 35,458 | 4.8% | not measured |
| Diogenidae (hermit crabs) | 32,504 | 4.4% | not measured |
| Coenobitidae (land hermit crabs) | 25,265 | 3.4% | not measured |
| Palaemonidae (prawns and grass shrimp) | 24,470 | 3.3% | not measured |
| Epialtidae | 23,609 | 3.2% | not measured |

These twelve families hold 490,016 decapod records (65.9%). The three hermit-crab families hold 96,479 (13.0%). The plain-English labels in brackets are mine.

**Woodlice, by species** (GBIF facet, read 12 October 2026; total 380,509):

| Species | Records | Share of Isopoda |
|---|---:|---:|
| Common Pill Woodlouse, *Armadillidium vulgare* | 120,321 | 31.6% |
| Rough Woodlouse, *Porcellio scaber* | 54,499 | 14.3% |
| *Oniscus asellus* | 37,205 | 9.8% |
| *Philoscia muscorum* | 23,402 | 6.2% |
| Nosy Pill Woodlouse, *Armadillidium nasatum* | 20,233 | 5.3% |
| *Trachelipus rathkii* | 16,794 | 4.4% |

The six hold 272,454 records (71.6%), and all six are woodlice of the land. No decapod family reaches 76,045 records, so the Common Pill Woodlouse is the most recorded species in the whole group.

**Alachua County** (from `docs/views/no-view-us-fl-alachua.csv`): woodlice hold 166 records across seven species, led by the Common Pill Woodlouse 91, the Florida Fast Woodlouse 40, the Oak Woodlouse 17 and the Little Pill Woodlouse 14. Decapods hold 26, of which crayfish of the genus *Procambarus* hold 20 (White Tubercled 9, Slough 4, Peninsula 3, Pallid Cave 3, Everglades 1), with the Eastern Grass Shrimp 3, the Spider Cave Crayfish 2 and the Bigclaw River Shrimp 1. There is one amphipod record.

**One view cannot be true for decapods and woodlice together.** They differ in what the eye can carry at all.

- **Crabs** have eyes of thousands of facets: the Asian shore crab (*Hemigrapsus sanguineus*, family Varunidae) has about 2,400 at 5 mm across the shell and about 6,000 at 30 mm (Eguchi and colleagues, 1989). A fiddler crab resolves about 0.4 cycles per degree from side to side over a field that runs the whole way around (Zeil and Al-Mutairi, 1996; Zeil and Hemmi, 2006). Fiddler crabs choose mates by colour and by ultraviolet, follow flicker to about 74 a second in daylight and read polarized light.
- **Woodlice** have eyes of about twenty facets: 22 in an electron micrograph of the Rough Woodlouse (McKenzie, amateur page), and 4 to 25 in two small-eyed water isopods (Nilsson, 1978). Even the big-eyed sea slater (*Ligia exotica*), with 800 to 1,500 facets, has them about 7 degrees apart (Keskinen and colleagues, 2002). Woodlice turn toward dark, damp shelter (Fialová and Tuf, 2025).

A woodlouse drawn with the crab's picture would be given sharpness, colour and pace that no source supports. A crab drawn with the woodlouse's lightness-only field would lose the colour choice, ultraviolet use and fast eye that are measured. **The line falls between Decapoda and Isopoda.** Worldwide, the decapod side holds the larger share (60.3% against 30.9%). In Alachua County the woodlouse side holds most records (166 against 26), and the single most recorded species everywhere is a woodlouse.

**Within the decapods, the horizon band is left out.** The band of sharp sight along the horizon is measured in narrow-fronted crabs (Ocypodidae and Mictyridae) and found absent in the broad-fronted families measured (Grapsidae, Xanthidae and Portunidae) (Zeil, Nalbach and Nalbach, 1986). Fiddler and ghost crabs hold 8.0% of decapod records, about one in twelve. Grapsidae and Portunidae, measured without the band, hold 15.1%. The shore crab's family (Carcinidae) and the crayfish were not covered by any source I opened. The crab view therefore draws no band, and the band is named in an `x` row. If fiddler and ghost crabs are ever split off, their view would carry it.

**Mantis shrimp** ride with the crab view. Some species have 12 kinds of photoreceptor, sampling from 300 to 720 nanometres, yet they discriminate between wavelengths poorly, and the authors propose that they recognize colours by scanning their eyes across a scene (Thoen and colleagues, 2014). The engine cannot draw that, and at 0.4% of the group it would not repay a view of its own.

**Horseshoe crabs** see in a way of their own. Each side eye has about 1,000 facets and resolves 0.1 cycles per degree on average, and a clock in the brain raises the eyes' sensitivity up to 100,000 times at night (Herzog and Barlow, 1992; Barlow and colleagues, 1987). A short entry is sketched in section 3 for later.

**Recommendation.** Build two views and leave the rest in `other`.

- `crab`: Decapoda and Stomatopoda, 747,713 records (60.7% of the group).
- `woodlouse`: Isopoda, 380,509 records (30.9%).
- `other`, until a sheet measures them: barnacles, amphipods, fairy and tadpole shrimp, copepods, horseshoe crabs and sea spiders, 103,823 records (8.4%).

There are two implementation notes.

- `tools/species/eyes.py` would route Decapoda and Stomatopoda to `crab` and Isopoda to `woodlouse`.
- The word table in `src/cam.r.js` sends woodlice, roly-polies, pill bugs, sow bugs, isopods, barnacles, amphipods, copepods, water fleas and sea spiders to `crab`. The woodlouse words (woodlice, woodlouse, roly-poly, pill bug, sow bug, isopod) would move to `woodlouse`, and the others would move to `other`. The table also names krill, which fall outside the orders in this assignment, and I found nothing on their eyes.

## 2. The rows

### The crab view

```
['g', 'All around', 'A fiddler crab’s eyes stand on tall stalks and see the whole way around. The picture is squeezed and bent to suggest that.'],
```
Source: Zeil and Hemmi, 2006: eyes "on long vertical stalks" with a "panoramic visual field" in fiddler crabs. Zeil and Al-Mutairi, 1996, measured the eyes of *Uca lactea annulipes* along vertical transects at 30-degree steps of azimuth, and noted that the field extends beyond the 45 degrees above and below the horizon at which some of their graphs stop. Graded `g` because it is measured in fiddler crabs and drawn for all crabs.

```
['g', 'Sharpness', 'From side to side a fiddler crab’s facets point about 1.3 degrees apart, so it resolves about 0.4 cycles per degree to your 60.'],
```
Source: Zeil and Al-Mutairi, 1996, in *U. lactea annulipes*: horizontal interommatidial angle 1.33 ± 0.32 degrees and horizontal resolution 0.39 ± 0.096 cycles per degree along the eye's equator, varying little across the visual field.

```
['x', 'The horizon', 'Fiddler and ghost crabs see up-and-down detail more finely in a thin band along the horizon, about five times finer than side-to-side detail in one fiddler crab, and a ghost crab keeps that band on the horizon even on a slope. They make up about one decapod record in twelve, and the families measured without the band make up more, so it is not drawn.'],
```
Source: Zeil and Al-Mutairi, 1996: vertical interommatidial angle about 0.25 degrees at the equator, against 1.33 degrees horizontally (the ratio, 5.3, is mine, and it is measured in this fiddler crab only), with a steep fall in resolution above and below. Zeil, Nalbach and Nalbach, 1986: a narrow band for vertical resolution along the horizon in narrow-fronted crabs (Ocypodidae, Mictyridae), absent in broad-fronted ones (Grapsidae, Xanthidae, Portunidae). Zeil, 1990: *Ocypode ceratophthalmus* aligns its equatorial band with the local horizon on sloping ground. Bagheri and colleagues, 2020: fiddler crabs probably have two parallel streaks, just above and just below the horizon. Record shares from the GBIF facet in section 1.

```
['m', 'Colour', 'Most light cells in a crab’s eye share one pigment, most sensitive to blue-green near 500 nanometres, so reds go dark. Female fiddler crabs still pick a yellow claw over a grey one of any brightness.'],
```
Source: Bruno, Mote and Goldsmith, 1973, in the shore crab *Carcinus maenas*: one visual pigment with its peak at 502 to 506 nm; every cell recorded, and the whole eye, most sensitive near 493 nm. Jordão, Cronin and Oliveira, 2007: the main cells (R1 to R7) of four fiddler crabs hold one class of pigment with mean peaks of 502 to 528 nm (Table 1; the abstract gives 508 to 530 nm from fitted curves), screening pigment shifts their sensitivity toward longer wavelengths, at times as far as 600 nm, and the small eighth cell could not be measured. In fiddler crabs reds may therefore darken less than drawn (the audit's inference). Detto, 2007, in *Uca mjoebergi*: females approached yellow claws over grey ones regardless of intensity. Qian and Frank, 2024: the Atlantic ghost crab (*Ocypode quadrata*) has a single dark-adapted peak at 494 nm.

```
['m', 'Ultraviolet', 'Female fiddler crabs prefer males whose claws reflect ultraviolet. A phone lens that was tested let through between a fifth and a hundredth of it, and the picture cannot pick it out, so the sheen here is invented.'],
```
Source: Detto and Backwell, 2009, in *U. mjoebergi*: mate-searching females preferred ultraviolet-reflecting males over males whose ultraviolet was blocked with sunscreen. Males choosing rivals to attack showed no such preference. Igoe, Parisi and Carter, 2012: a smartphone's sensor has some inherent sensitivity to ultraviolet A, and its lens transmitted 18.9% at 390 nm, falling to 1.1% at 340 nm (one phone, a Samsung Galaxy 5). That the picture cannot separate ultraviolet from visible light is my inference.

```
['m', 'Pace', 'In daylight a fiddler crab’s eye follows flicker to about 74 a second, a little past your 60. Once its eye has adapted to the dark, it follows only about 35 to 40.'],
```
Source: Brodrick, How and Hemmi, 2022, in the fiddler crab *Gelasimus dampieri*: flicker fusion 73.6 ± 6.1 Hz light-adapted by day, 58.8 ± 2.3 Hz light-adapted at night, 34.5 ± 5.9 Hz dark-adapted by day and 39.8 ± 3.4 Hz dark-adapted at night. These are means ± s.e.m. from the Results text; Table 1 gives the same means as ± s.d. (73.6 ± 17.3, 58.8 ± 6.4, 34.6 ± 16.6 and 39.8 ± 9.6 Hz, n = 8 crabs).

```
['m', 'Night', 'At night a fiddler crab’s dark-adapted eye answers to light about a thousand times dimmer than the same dark-adapted eye does by day.'],
```
Source: Brodrick, How and Hemmi, 2022, in *G. dampieri*: threshold intensity dark-adapted at night about three orders of magnitude below dark-adapted by day, and thresholds across states spanning six orders of magnitude. The Results give three orders of magnitude, while the Discussion says the night thresholds were on average 45,000 times dimmer, so the paper is inconsistent and the row follows the Results.

```
['m', 'Crayfish', 'Crayfish and slipper lobsters have superposition eyes, a design suited to dim water. A crayfish has one set of light cells most sensitive to violet and another most sensitive to yellow.'],
```
Source: Kingston and Cronin, 2015: the red swamp crayfish (*Procambarus clarkii*) has reflecting superposition eyes with two classes of photoreceptor, long-wavelength cells (R1 to R7) in the main rhabdom and short-wavelength eighth cells. Eguchi, Waterman and Akiyama, 1973: crayfish retinulas hold violet and yellow receptor cells, which were adapted at 450 and 570 nm, "near the λmax's of the two retinular cell classes"; the abstract does not name the species. Hayasaka and colleagues, 2022: three slipper lobsters have superposition eyes, peak at 493 to 538 nm and are "well adapted to dim light environments"; the paper cites Meyer-Rochow (2001) and Cronin and Porter (2008) for superposition eyes improving dim-light vision (**secondary** for that general point). No source opened covers true lobsters.

```
['x', 'Polarized light', 'A fiddler crab tells apart polarized light whose angle differs by 3 degrees, and uses it to pick out objects on the mud. A phone camera does not record polarization, so it is left out.'],
```
Source: How and colleagues, 2012, in *Uca vomeris*: stimuli differing in e-vector angle by as little as 3.2 degrees were detected, through a horizontal and vertical receptor array. How and colleagues, 2015, in *Uca stenodactylus*: polarization vision enhances contrast and the detection of objects on the mudflat. Tuthill and Johnsen, 2006: polarization sensitivity in the red swamp crayfish enhances the detection of moving transparent objects. The statement about phone cameras has no opened source.

### The woodlouse view

```
['g', 'Eyes', 'Two small-eyed water isopods have 4 and about 25 facets to an eye, and a close picture of a Rough Woodlouse’s eye shows 22. The Asian shore crab has 2,400 to 6,000.'],
```
Source: Nilsson, 1978: about 25 ommatidia in *Jaera albifrons* and four in *Asellus aquaticus*, both water isopods. McKenzie, amateur page (undated): an electron micrograph of an eye "made of 22 simple eyes (ocelli)", in a woodlouse the page identifies as *Porcellio scaber* by its three-lobed head. Eguchi and colleagues, 1989: *Hemigrapsus sanguineus* has about 2,400 ommatidia at 5 mm carapace width and about 6,000 at 30 mm. Graded `g` because the only count in a common woodlouse is the amateur one.

```
['g', 'Sharpness', 'The sea slater, a big-eyed seashore relative, has facets about 7 degrees apart, which resolves about 0.07 cycles per degree, near an eight-hundredth of your 60.'],
```
Source: Keskinen, Takaku, Meyer-Rochow and Hariyama, 2002, in *Ligia exotica*: interommatidial angle 6.91 ± 0.95 degrees for central ommatidia, about 800 to 1,500 ommatidia per eye. The conversion (one cycle per two facet spacings) is mine.

```
['i', 'No picture', 'With about twenty facets to an eye, a woodlouse is drawn with no image at all, only how much light there is and from where.'],
```
Source: this is my inference from the two rows above, and no source measures a woodlouse's resolution.

```
['m', 'Dark', 'Woodlice turn away from light toward dark shelters, where the air is damper and cooler.'],
```
Source: Fialová and Tuf, 2025: "Photonegative orientation is associated with searching for dark habitats (shelters)", citing Cloudsley-Thompson (1977); shelters offer higher humidity and lower temperatures than their surroundings.

```
['m', 'Dry air', 'Woodlice shelter more when the air is dry, and huddled together they lose about half as much water as they do alone.'],
```
Source: Fialová and Tuf, 2025, citing Dias and colleagues (2012) for more sheltering at lower humidity and Warburg (1968) for about 50% less evaporative water loss in aggregated animals. The figures are **secondary**.

```
['m', 'Night', 'About six in ten Common Pill Woodlice are active at night, against nine in ten of Philoscia muscorum, the fourth most recorded woodlouse.'],
```
Source: Fialová and Tuf, 2025: 60% of *A. vulgare* nocturnally active against 92% of *P. muscorum*. The paragraph opens by citing Cloudsley-Thompson (1952, 1956) for nocturnal activity, and the two percentages carry no citation of their own (**secondary**, original study not identified). Record rank from the GBIF facet in section 1.

```
['i', 'Colour', 'No measurement of a woodlouse’s colour sense was found, so the picture is grey.'],
```
Source: none found. The grey follows the `other` entry.

```
['x', 'Damp air', 'How far and how evenly a woodlouse walks changes with the dampness of the air, which a camera cannot show.'],
```
Source: Ruiz and Guerrero Sánchez, 2022: in three woodlice tested at humidities from 32.9% to 94.9%, distance travelled and regularity differed, both greatest at 50%. Fialová and Tuf, 2025, for sheltering at lower humidity.

### A horseshoe crab entry, for later

```
['m', 'Eyes', 'Each eye on the side of the shell has about a thousand facets and takes in about 60 per cent of the half of the world on its side.'],
['m', 'Sharpness', 'On average it resolves 0.1 cycles per degree, a six-hundredth of yours, and up to 0.22 toward the front.'],
['m', 'Night', 'A clock in its brain makes its eyes up to 100,000 times more sensitive at night, and it finds mates by sight by day and by night.'],
['m', 'Colour', 'Those eyes have a single peak of sensitivity near 520 nanometres, and no colour vision has been found, so the picture is grey.'],
['x', 'Ultraviolet', 'Its small eye on top of the shell responds to ultraviolet 200 to 320 times more strongly than to visible light, and a phone camera keeps little of that light.'],
```
Sources: Herzog and Barlow, 1992, in *Limulus polyphemus*: about 1,000 ommatidia; optic axes diverging 1 to 15 degrees, average 5.5; average resolution 0.1 cycles per degree, maximal 0.22 in the anterior eye along horizontal planes (0.23 near the horizon along vertical planes); one eye views about 60% of the hemisphere on its side; vision used to find mates by day and night. Barlow, Kaplan, Renninger and Saito, 1987: the circadian clock can "increase retinal sensitivity as much as 100,000 times". Chapman and Lall, 1967: lateral eye single maximum near 520 nm; median ocellus peaks at 360 and 530 to 535 nm and is roughly 200 to 320 times more sensitive to ultraviolet. Battelle and colleagues, 2014: over 1,000 ommatidia in adult lateral eyes and no evidence for colour vision. Igoe, Parisi and Carter, 2012, for how little ultraviolet reaches a phone's sensor.

## 3. The picture

### `crab`

**What the view shows.** The crab's view shows a wide, coarse, bent picture in which reds go dark, a faint sheen stands for ultraviolet, and movement runs slightly ahead of a person's.

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Crab, crayfish, shrimp', 'a crab' | This is the app's wording. |
| `fov` | 360 | This value rests on the row "All around". The sources give the field as panoramic without one number, so 360 is **invented**. The engine compresses it to half scale. |
| `cpd` | .4 | This value rests on the row "Sharpness": 0.39 cycles per degree horizontally in *U. lactea annulipes*, nearly constant across the field. Drawing it for every decapod is the `g` step. On a phone the picture keeps only coarse shapes. |
| `topoS`, `fall` | unset | This rests on the row "The horizon". The band is measured in 8.0% of decapod records and measured absent in 15.1%. |
| `pupil` | 'none' | This value is **invented**. No source I opened describes a pupil, and it matches the bee and insect entries. |
| `M` | PROTAN | This value rests on the row "Colour". The shore crab and four fiddler crabs have one main pigment peaking at 493 to 528 nm, and a fiddler crab chooses by colour. Using the existing protan matrix, the human two-cone model without the long-wave cone, is **invented**; it darkens reds. Crayfish have yellow-sensitive main cells (adapted at 570 nm, near their peak, by Eguchi and colleagues, 1973), and screening pigment shifts fiddler crabs' sensitivity toward longer wavelengths (Jordão and colleagues, 2007), so for both, reds would darken less than drawn. |
| `sheen` | .5 | This value rests on the row "Ultraviolet". The strength is **invented**. |
| `rate` | .8 | This value rests on the row "Pace": 60 divided by 73.6 gives 0.82, from *G. dampieri* light-adapted by day. A crayfish's movement-sensing fibres follow flicker only to about 10 a second (Yamaguchi and colleagues, 1973), which would give a much slower rate, but that is a measure of single nerve fibres and was not used. |
| `gain` | unset | No comparison with a human eye in dim light was found. The night rows compare each eye with itself by day (section 4). |
| `dof`, `fovea`, `topoA`, `persist`, `gate`, `uvBlue`, `noGreen`, `field`, `hold`, `thrust` | unset | No source I opened supports them. |
| `cue` | 'Hold the phone low, a hand above the sand or mud, and turn slowly. A crab sees the whole way around at once.' | This is the app's wording, resting on the row "All around". |

### `woodlouse`

**What the view shows.** The woodlouse's view shows no image: a grey field of light and shade, with the brighter side and the darker side.

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Woodlouse, pill bug', 'a woodlouse' | This is the app's wording. |
| `field` | 1 | This value rests on the rows "Eyes", "Sharpness" and "No picture". It is my inference from facet counts, so it is **invented**. |
| `sat` | 0 | This value rests on the row "Colour" and is **invented**, following `other`. |
| `pupil` | 'none' | This value is **invented**, matching `other`. |
| `persist`, `rate`, `gain` | unset | No time constant, flicker measure or dim-light comparison was found. |
| all other fields | unset | No source supports them. |
| `cue` | 'Hold the phone close to the ground and turn it slowly. A woodlouse heads for the darker side.' | This is the app's wording, resting on the row "Dark". |

The woodlouse picture is the same as the picture of `other` (`field: 1, sat: 0`). What the view adds is the rows and the cue.

### A horseshoe crab entry, for later

| Field | Value | Behind it |
|---|---|---|
| `cpd` | .1 | Herzog and Barlow, 1992: average 0.1 cycles per degree. |
| `sat` | 0 | Single peak near 520 nm (Chapman and Lall, 1967), and no evidence for colour vision (Battelle and colleagues, 2014). |
| `pupil` | 'none' | This value is **invented**. |
| `fov` | unset | Each eye views about 60% of the hemisphere on its side, and no horizontal extent was given. |
| `gain` | unset | The 100,000-fold rise is measured against the same eye by day (section 4). |

Here is a sketch of the entries for the owner to place. No file was changed.

```
crab: { chip: 'Crab, crayfish, shrimp', who: 'a crab', fov: 360, cpd: .4, pupil: 'none', M: PROTAN, sheen: .5, rate: .8,
  cue: 'Hold the phone low, a hand above the sand or mud, and turn slowly. A crab sees the whole way around at once.', rows: [ /* the nine crab rows above */ ] },
woodlouse: { chip: 'Woodlouse, pill bug', who: 'a woodlouse', pupil: 'none', field: 1, sat: 0,
  cue: 'Hold the phone close to the ground and turn it slowly. A woodlouse heads for the darker side.', rows: [ /* the eight woodlouse rows above */ ] },
// later, if wanted:
// horseshoe: { chip: 'Horseshoe crab', who: 'a horseshoe crab', cpd: .1, pupil: 'none', sat: 0, rows: [ /* the five rows above */ ] },
```

## 4. What the engine cannot draw yet

| Effect | What it would show | Phone input that could stand in | Judgement |
|---|---|---|---|
| Finer up and down than side to side | In fiddler crabs, vertical detail about five times finer than horizontal near the horizon (0.25 against 1.33 degrees). | The camera serves; the shader would need separate vertical and horizontal blur. | It is easy. |
| Two streaks at the horizon | Two sharp bands just above and just below the horizon (Bagheri and colleagues, 2020), where `topoS` draws one. | The camera serves. | It is easy, and worth doing only if fiddler and ghost crabs get their own view. |
| A band held level | A ghost crab keeps the band on the horizon as the ground tilts (Zeil, 1990). | Motion sensors give the phone's tilt, so the band could stay level as the phone turns. | It is easy to medium; iPhones ask permission for motion. |
| The eye at night | A fiddler crab's eye about a thousand times more sensitive at night than by day, a crayfish's response about a hundredfold (secondary), a horseshoe crab's up to 100,000 times. | The phone's clock could raise `gain` and lower `rate` after dark. The size of the lift against a human eye would be **invented**. | It is easy. |
| Polarization | Contrast from polarized light on mud and water (How and colleagues, 2012, 2015). | No phone input a web page can read records it, to my knowledge (no source opened). A polarizing filter held over the lens would show some of it, and the app could not count on one. | It is impossible as measurement. |
| Ultraviolet | Ultraviolet claws (fiddler crabs) and the horseshoe crab's ultraviolet-sensitive top eye. | A smartphone lens passed 1.1% of ultraviolet A at 340 nm, and the sensor responds weakly to it (Igoe and colleagues, 2012). What reaches the sensor would mix into the visible picture (my inference). The `sheen` stands in. | It is impossible as measurement with an ordinary phone, and the stand-in exists. |
| Mantis shrimp colour | Twelve kinds of receptor from 300 to 720 nm, read by scanning the eyes (Thoen and colleagues, 2014). | None. | It is hard and would serve 0.4% of the group. |
| Damp air (woodlice) | A pull toward damp, cool shelter. | No input a web page can read measures humidity, to my knowledge (no source opened). | It is impossible. |
| Two eyes aimed sideways (horseshoe crab) | Two windows of light, each covering about 60% of the half of the world on its side. | The aperture mask (`u_ap`, `u_shape`) could take a two-window shape, as the tick sheet proposed. | It is easy. |

## 5. Sources

- Zeil, J. and Al-Mutairi, M. M., 1996. The variation of resolution and of ommatidial dimensions in the compound eyes of the fiddler crab *Uca lactea annulipes* (Ocypodidae, Brachyura, Decapoda). *Journal of Experimental Biology* 199: 1569 to 1577. https://cob.silverchair.com/jeb/article-pdf/199/7/1569/3391178/jexbio_199_7_1569.pdf (DOI not checked). Findings: panoramic equatorial acute zone for vertical resolution; horizontal interommatidial angle 1.33 ± 0.32 degrees and resolution 0.39 cycles per degree; vertical angle fitted with a minimum of 0.25 at the equator (the fitted equation is labelled "rad" in one place, while the figures read in degrees); transects at 30-degree steps of azimuth; the field extends beyond the 45 degrees above and below the horizon at which some graphs stop; the strip of events in crab life about 10 degrees either side of the horizon. **opened** (full text).
- Zeil, J. and Hemmi, J. M., 2006. The visual ecology of fiddler crabs. *Journal of Comparative Physiology A* 192: 1 to 25. doi:10.1007/s00359-005-0048-7. Findings: eyes on long vertical stalks, panoramic visual field, pronounced equatorial acute zone. **opened** (abstract at https://openresearch-repository.anu.edu.au/items/4b9c6c28-641a-4300-bcdd-49777fb1e1a7/full).
- Zeil, J., Nalbach, G. and Nalbach, H.-O., 1986. Eyes, eye stalks and the visual world of semi-terrestrial crabs. *Journal of Comparative Physiology A* 159: 801 to 811. doi:10.1007/BF00603733. Findings: 17 species; narrow-fronted Ocypodidae and Mictyridae have a narrow vertical acute zone along the horizon, broad-fronted Grapsidae, Xanthidae and Portunidae lack it; no horizontal acute zone in either. **opened** (abstract).
- Zeil, J., 1990. Substratum slope and the alignment of acute zones in semi-terrestrial crabs (*Ocypode ceratophthalmus*). *Journal of Experimental Biology* 152: 573 to 576. https://cob.silverchair.com/jeb/article-pdf/152/1/573/2630896/jexbio_152_1_573.pdf. Finding: the crabs align their equatorial acute zone with the local visual horizon. **opened** (full text).
- Bagheri, Z. M., Jessop, A. L., Kato, S., Partridge, J. C., Shaw, J., Ogawa, Y. and Hemmi, J. M., 2020. A new method for mapping spatial resolution in compound eyes suggests two visual streaks in fiddler crabs. *Journal of Experimental Biology* 223: jeb210195. doi:10.1242/jeb.210195. Finding: two parallel streaks just above and below the visual horizon. **opened** (abstract at https://researchnow.flinders.edu.au/en/publications/a-new-method-for-mapping-spatial-resolution-in-compound-eyes-sugg/).
- Jordão, J. M., Cronin, T. W. and Oliveira, R. F., 2007. Spectral sensitivity of four species of fiddler crabs (*Uca pugnax*, *Uca pugilator*, *Uca vomeris* and *Uca tangeri*) measured by in situ microspectrophotometry. *Journal of Experimental Biology* 210: 447 to 453. doi:10.1242/jeb.02658. Findings: one spectral class in R1 to R7, mean peaks 502 to 528 nm (Table 1), 508 to 530 nm in the abstract; screening pigment shifts sensitivity toward longer wavelengths, at times to the 600 nm region; R8 too small to measure. **opened** (full text).
- Bruno, M. S., Mote, M. I. and Goldsmith, T. H., 1973. Spectral absorption and sensitivity measurements in single ommatidia of the green crab, *Carcinus*. *Journal of Comparative Physiology* 82: 151 to 163. doi:10.1007/BF00696150. Findings: one pigment, peak 502 to 506 nm; cells and ERG most sensitive near 493 nm. **opened** (abstract).
- Detto, T., 2007. The fiddler crab *Uca mjoebergi* uses colour vision in mate choice. *Proceedings of the Royal Society B* 274: 2785 to 2790. doi:10.1098/rspb.2007.1059. Finding: females approached yellow claws over grey regardless of intensity. **opened** (abstract at https://researchportalplus.anu.edu.au/en/publications/the-fiddler-crab-uca-mjoebergi-uses-colour-vision-in-mate-choice/).
- Detto, T. and Backwell, P. R. Y., 2009. The fiddler crab *Uca mjoebergi* uses ultraviolet cues in mate choice but not aggressive interactions. *Animal Behaviour* 78: 407 to 411. doi:10.1016/j.anbehav.2009.05.014. Finding: females preferred ultraviolet-reflecting males over sunscreen-blocked males; the visual system is called "relatively simple, probably dichromatic". **opened** (abstract at https://openresearch-repository.anu.edu.au/items/6df3a44f-7f55-4038-8846-049d6e20acca; volume, pages and DOI from https://fiddlercrab.info/references/Detto2009.1.html).
- How, M. J., Pignatelli, V., Temple, S. E., Marshall, N. J. and Hemmi, J. M., 2012. High e-vector acuity in the polarisation vision system of the fiddler crab *Uca vomeris*. *Journal of Experimental Biology* 215: 2128 to 2134. doi:10.1242/jeb.068544. Finding: e-vector differences of 3.2 degrees detected; orthogonal receptor array. **opened** (abstract at Bristol Research Information).
- How, M. J., Christy, J. H., Temple, S. E., Hemmi, J. M., Marshall, N. J. and Roberts, N. W., 2015. Target detection is enhanced by polarization vision in a fiddler crab. *Current Biology* 25: 3069 to 3073. doi:10.1016/j.cub.2015.09.073. Finding: polarization vision enhances contrast and the detection of objects on the mudflat, in *Uca stenodactylus*. **opened** (abstract at Bristol Research Information).
- Brodrick, E. A., How, M. J. and Hemmi, J. M., 2022. Fiddler crab electroretinograms reveal vast circadian shifts in visual sensitivity and temporal summation in dim light. *Journal of Experimental Biology* 225: jeb243693. doi:10.1242/jeb.243693. Findings in *Gelasimus dampieri*: flicker fusion 73.6, 58.8, 34.5 and 39.8 Hz by state; dark-adapted night thresholds about three orders of magnitude below dark-adapted day in the Results (45,000 times on average in the Discussion); ± values in the Results are s.e.m., and Table 1 gives s.d. and 34.6 Hz for dark-adapted day; apposition eyes. **opened** (publisher PDF, https://cob.silverchair.com/jeb/article-pdf/2137810/jeb243693.pdf).
- Qian, R. and Frank, T. M., 2024. Comparative study of spectral sensitivity, irradiance sensitivity, spatial resolution and temporal resolution in the visual systems of *Ocypode quadrata* and *Aratus pisonii*. *Journal of Experimental Biology* 227: jeb246813. doi:10.1242/jeb.246813. Finding: single dark-adapted peaks at 494 and 499 nm; the ghost crab has greater spatial resolution and irradiance sensitivity. **opened** (abstract at Nova Southeastern University's portal).
- Eguchi, E., Arikawa, K., Ishibashi, S., Suzuki, T. and Meyer-Rochow, V. B., 1989. Growth-related biometrical and biochemical studies of the compound eye of the crab, *Hemigrapsus sanguineus*. *Zoological Science* 6: 241 to 250. https://ia800300.us.archive.org/31/items/biostor-106922/biostor-106922.pdf. Finding: about 2,400 ommatidia at 5 mm carapace width, about 6,000 at 30 mm. **opened** (full text).
- Kingston, A. C. N. and Cronin, T. W., 2015. Short- and long-wavelength-sensitive opsins are involved in photoreception both in the retina and throughout the central nervous system of crayfish. *Journal of Comparative Physiology A* 201: 1137 to 1145. doi:10.1007/s00359-015-1043-2. Finding: *Procambarus clarkii* has reflecting superposition eyes with two photoreceptor classes. **opened** (abstract).
- Eguchi, E., Waterman, T. H. and Akiyama, J., 1973. Localization of the violet and yellow receptor cells in the crayfish retinula. *Journal of General Physiology* 62: 355 to 374. https://rupress.org/jgp/article/62/4/355/31211/Localization-of-the-Violet-and-Yellow-Receptor (DOI not checked). Findings: violet and yellow receptors occur in each retinula; cells adapted at 450 and 570 nm, near the peaks of the two retinular cell classes; species not named in the abstract. **opened** (abstract, by the audit).
- Tuthill, J. C. and Johnsen, S., 2006. Polarization sensitivity in the red swamp crayfish *Procambarus clarkii* enhances the detection of moving transparent objects. *Journal of Experimental Biology* 209: 1612 to 1616. https://cob.silverchair.com/jeb/article-pdf/209/9/1612/1258896/1612.pdf (DOI not checked). Finding: as the title states. **opened** (full text, by the audit).
- Garfias, A., Rodríguez-Sosa, L. and Aréchiga, H., 1995. Modulation of crayfish retinal function by red pigment concentrating hormone. *Journal of Experimental Biology* 198: 1447 to 1454. https://cob.silverchair.com/jeb/article-pdf/3386649/jexbio_198_7_1447.pdf. Finding: cites a circadian rhythm that changes retinal responsiveness 100-fold in *P. clarkii*. **opened**. The original, Rodríguez-Sosa and Aréchiga (1982), is **secondary** (via Garfias and colleagues).
- Yamaguchi, T., Ohtsuka, T., Katagiri, Y. and Shimozawa, T., 1973. Some spatial and temporal properties of movement fibres in the optic tract of the crayfish. *Journal of the Faculty of Science, Hokkaido University, Series VI, Zoology* 19(1): 31 to 49. https://eprints.lib.hokudai.ac.jp/repo/huscap/all/27551/19(1)_P31-49.pdf. Finding: the movement fibres' critical fusion frequency "appears to be about 10 Hz" in *P. clarkii*. **opened**.
- Hayasaka, O., Chang, H.-Y., Li, L.-C., Tseng, Y.-C. and Shao, Y. T., 2022. Nocturnal eyes in slipper lobsters (Decapoda Scyllaridae): physiological and ecological implications of habitat depths for visual traits. *Frontiers in Marine Science* 9: 807347. doi:10.3389/fmars.2022.807347. Findings: superposition eyes with square facets; peaks 493.0, 517.4 and 537.5 nm; "well adapted to dim light environments". **opened**.
- Thoen, H. H., How, M. J., Chiou, T.-H. and Marshall, J., 2014. A different form of color vision in mantis shrimp. *Science* 343: 411 to 413. doi:10.1126/science.1245824. Findings: up to 12 photoreceptor types from 300 to 720 nm; poor wavelength discrimination; colour recognition by scanning. **opened** (abstract at Bristol Research Information).
- Herzog, E. D. and Barlow, R. B., 1992. The *Limulus*-eye view of the world. *Visual Neuroscience* 9: 571 to 580. doi:10.1017/S0952523800001814. Findings: about 1,000 ommatidia; axes 1 to 15 degrees apart, average 5.5; 0.1 cycles per degree average, 0.22 anterior along horizontal planes and 0.23 near the horizon along vertical planes; about 60% of the hemisphere per eye; mates found by vision day and night. **opened** (abstract at https://profiles.wustl.edu/en/publications/the-limulus-eye-view-of-the-world/).
- Barlow, R. B., Jr., Kaplan, E., Renninger, G. H. and Saito, T., 1987. Circadian rhythms in *Limulus* photoreceptors. I. Intracellular studies. *Journal of General Physiology* 89: 353 to 378. doi:10.1085/jgp.89.3.353. Finding: the clock can increase retinal sensitivity as much as 100,000 times at night. **opened** (abstract).
- Chapman, R. M. and Lall, A. B., 1967. Electroretinogram characteristics and the spectral mechanisms of the median ocellus and the lateral eye in *Limulus polyphemus*. *Journal of General Physiology* 50: 2267 to 2287. doi:10.1085/jgp.50.9.2267. Findings: lateral eye single maximum near 520 nm; median ocellus 360 and 530 to 535 nm, about 200 to 320 times more sensitive to ultraviolet. **opened** (abstract).
- Battelle, B.-A., Kempler, K. E., Harrison, A., Dugger, D. R. and Payne, R., 2014. Opsin expression in *Limulus* eyes: a UV opsin is expressed in each eye type and co-expressed with a visible light-sensitive opsin in ventral larval eyes. *Journal of Experimental Biology* 217: 3133 to 3145. doi:10.1242/jeb.107383. Findings: over 1,000 ommatidia per adult lateral eye; no evidence for colour vision; a UV opsin in eccentric cells that recordings have yet to confirm. **opened** (full text).
- Keskinen, E., Takaku, Y., Meyer-Rochow, V. B. and Hariyama, T., 2002 (accepted March 2002; volume and pages not shown in the copy read). Postembryonic eye growth in the seashore isopod *Ligia exotica* (Crustacea, Isopoda). *Zoological Science*. https://archive.org/download/biostor-11104/biostor-11104.pdf. Findings: about 800 to 1,500 ommatidia; central interommatidial angle 6.91 ± 0.95 degrees. **opened**.
- Nilsson, H. L., 1978. The fine structure of the compound eyes of shallow-water asellotes, *Jaera albifrons* Leach and *Asellus aquaticus* L. (Crustacea: Isopoda). *Acta Zoologica* 59: 69 to 84. https://isopods.nhm.org/pdfs/20514/20514.pdf. Finding: about 25 ommatidia in *J. albifrons* and four in *A. aquaticus*. **opened**.
- McKenzie, G. J., undated. Scanning electron micrographs of a woodlouse. https://scaber.org/porcellio/woodlice/sem/. Finding: a compound eye "made of 22 simple eyes (ocelli)", species given as *Porcellio scaber* from its head. **opened**. It is an amateur page with no references, and it names no text author; its photographs are given as the property of G. J. McKenzie.
- Fialová, R. and Tuf, I. H., 2025. Spatial activity and sheltering behaviour of terrestrial isopods (Isopoda, Oniscidea): a field experiment. *ZooKeys* 1225: 127 to 139. doi:10.3897/zookeys.1225.125030. Findings: photonegative orientation tied to shelter seeking; shelters damper and cooler. **opened** (https://zookeys.pensoft.net/article_preview.php?id=125030). Its citations of Cloudsley-Thompson (1952, 1956, 1977), Dias and colleagues (2012) and Warburg (1968) are **secondary** (via Fialová and Tuf). The percentages of night activity carry no citation of their own in the paper.
- Ruiz, J. A. and Guerrero Sánchez, C. G., 2022. Recurrence analysis in the locomotion of woodlice as a function of humidity level. *Revista de Psicología* 31(1): 114 to 125 (volume and pages not shown on the page the audit opened). doi:10.5354/0719-0581.2022.67867. Finding: three woodlice at 32.9% to 94.9% humidity; activity and regularity greatest at 50%. **opened** (abstract at https://revistaschilenas.uchile.cl/handle/2250/222554).
- Igoe, D., Parisi, A. and Carter, B., 2012. Characterization of a smartphone camera's response to ultraviolet A radiation. *Photochemistry and Photobiology*. doi:10.1111/j.1751-1097.2012.01216.x (volume and pages not shown in the copy read). https://research.usq.edu.au/download/9ff995c2f31be858fb6222019e8c44bf318570274d823302cfab9c0dee1ed790/207937/Igoe_Parisi_Carter_PP_2012_AV.pdf. Findings: the camera's CMOS sensor (a Samsung Galaxy 5) has inherent ultraviolet A sensitivity; lens transmission fell from 18.9% at 390 nm to 1.1% at 340 nm; responses read at 320 to 380 nm, with 340, 360 and 380 nm used in the fit. **opened** (accepted manuscript).
- GBIF.org occurrence and species APIs, dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7, read 12 October 2026: Decapoda (orderKey 637) by familyKey; Isopoda (orderKey 643) by speciesKey; family and species names from https://api.gbif.org/v1/species/{key}, with Cancridae, Diogenidae and Epialtidae named from a backbone family listing; a name match placed the fiddler crab *Leptuca pugilator* in Ocypodidae (familyKey 4527). Findings: all world family and species counts in section 1. **opened**.
- This repository: `src/cam.a.js`, `src/cam.r.js`, `docs/VIEWS.md`, `docs/views/world-orders.csv`, `docs/views/no-view-us-fl-alachua.csv`. Findings: engine fields, word table, order totals and the Alachua species. **opened**.

## 6. Open questions for a sensory scientist

1. How many facets do the eyes of the Common Pill Woodlouse and the Rough Woodlouse have, how far apart do they point, and what colours do they respond to? This sheet's count rests on one amateur micrograph.
2. Does the shore crab (*Carcinus maenas*, family Carcinidae) or any crayfish have a band of finer vertical sight along the horizon, and what are their interommatidial angles?
3. What does the small eighth cell of a fiddler crab's ommatidium respond to: violet or ultraviolet? Detto and Backwell's result implies ultraviolet sight, and Jordão and colleagues could not measure the cell.
4. How does the dark-adapted sensitivity of a fiddler crab, a crayfish or a horseshoe crab at night compare with a dark-adapted person's? The engine's `gain` needs that comparison, and every figure found compares an eye with itself.
5. What is the photoreceptor flicker fusion of the red swamp crayfish? The only figure found, about 10 a second, is from movement-sensing nerve fibres.
