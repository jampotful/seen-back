# Audit: tick sheet (order Ixodida, with a note on mites)

Audited 12 October 2026, from 04:51 to about 05:20 EDT, against `tick.md` as written on 11 October 2026. Every page named below was opened with WebFetch in this audit unless the line says otherwise. The corrected sheet is `tick.checked.md`.

**Verdict in brief.** No fabricated or misattributed citation was found. The figures the picture rests on all check out against their sources: the bont tick's eye fields and spectral peak, the camel tick's 4.8 degree disc and 18 metre silhouette, the sheep tick's cells, the carbon dioxide receptor, the eye list, and the gall-mite share of GBIF records. Eight things needed correcting:

- Carr and Salgado's published field figure is "at most 5.7 degrees". The sheet quotes "6 degrees or less" from the preprint.
- The 1 m heat test used adult females only, and the "Heat" row did not say so.
- Carr and colleagues (2017) state "required for host seeking" as a hypothesis, and the sheet cites it as a finding.
- The mite family table leaves out Penthaleidae (467 records).
- Four list introductions are sentence fragments.
- Two source lines needed small fixes: the Entomology Today author was missing and the Olomski title was cut short.
- Both missing DOIs are now found.

## 1. Sources

1. **Carr and Salgado, 2019, *PLoS ONE* 14(8): e0221659: confirmed, with two corrections.** Authors, year, title, journal, volume, issue and article number match at https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0221659. The abstract at https://ir.vanderbilt.edu/handle/1803/10391 matches too, including "several meters" and "previous attempts to do this have concluded that radiant heat was not used by ticks". The paper confirms these points:
   - "at least 72% of adult A. americanum females can detect the 10X10 cm plate at a distance of 1m", based on 31 of 43 ticks.
   - The arena measured 10 by 10 by 100 cm, and its end walls were the 10 by 10 cm plates.
   - The ticks were unfed adults. Responses were significant from 50 cm at 37 °C and above, with none at 22 or 30 °C.
   - Foil cladding abolished the response, and the infrared-transparent PVDC film did not.
   - Wax over the capsule apertures abolished the response.
   - Thermotaxis stopped completely at 50, 54 and 42 ng per cubic centimetre of DEET, picaridin and 2-undecanone. DEET at 50 ng per cubic centimetre did not change the choice of the carbon dioxide airstream in the Y-tube.
   - No wavelength-selective filter was tested. The 5 to 20 micrometre range is cited to Hardy (1939).
   - No live person or animal was used as a target.

   The corrections:
   - The published field figure is "the field of view of their heat sensor is at most 5.7 degrees". The sheet's "6 degrees or less" (sections 3, 4 and 6) comes from the preprint.
   - The published distance wording is "up to 4 meters under ideal conditions" (results) and "at least 4 meters" (discussion). The sheet's "< 4 meters" comes from the preprint. The paper's own two wordings disagree.
   - Only adult females of *A. americanum* were tested at 1 m. Males and both sexes of *D. variabilis* were tested at 50 cm.

   I could not open the bioRxiv preprint at https://www.biorxiv.org/content/10.1101/564179v1.full because the permission request was withdrawn, so the preprint's wording is unconfirmed. The checked sheet uses the published wording.
2. **Kaltenrieder, Labhart and Hess, 1989, *J. Comp. Physiol. A* 165(2): 155 to 164: confirmed. The DOI is now found.** The DOI is 10.1007/BF00619190. It is listed in the issue contents at https://link.springer.com/journal/359/volumes-and-issues/165-2, and the article page at https://link.springer.com/article/10.1007/BF00619190 opened with the right title, authors and pages. The Springer summary and the thesis (https://libra.unine.ch/bitstreams/1a2fadd3-3feb-47eb-8b81-ffa264e7d13f/download) both give the following figures:
   - *Amblyomma variegatum* shows "a single sensitivity maximum in the blue range (ca. 480 nm)" by phototaxis, and its electroretinogram has "only one peak in the blue range (ca. 470 nm)".
   - The *Amblyomma* optical axis lies at 39 and 33 degrees, and its field at 50% sensitivity is 43 degrees horizontally and 49 vertically.
   - The *Hyalomma* axis lies at 35 and 30 degrees, and its field is 14 by 25 degrees.
   - Thresholds are 5.2 × 10^6 photons per second per square centimetre in *Hyalomma* and 5.2 × 10^8 in *Amblyomma*.
   - *Hyalomma* has "single-lens eyes that protrude above the body surface", and *Amblyomma* has "comparatively flat single-lens eyes".
   - Only *Hyalomma* has an ultraviolet phototaxis peak, near 380 nm.

   The thesis Discussion restates the axis as "35° in the horizontal and 30° in the vertical direction", so the sheet's reading of 39 degrees as a horizontal angle is correct. The thesis also notes that at the highest irradiance the *Amblyomma* curve "showed no distinct maximum". That does not undercut the row, which follows the paper's headline result.
3. **Kaltenrieder, 1990, *Exp. Appl. Acarol.* 9(3-4): 267 to 278: confirmed through the thesis. The DOI is found but not opened.** The thesis gives these sentences verbatim:
   - "For a tick at the starting point this target appears under a visual angle of 4.8°" (the 8.8 cm disc at 12.4 degrees of elevation).
   - "this silhouette appeared like a silhouette of a real dromedary seen from a distance of ca. 18 m", which assumes a camel 200 cm high.
   - "a disk with a luminance contrast of 3:1 was necessary".
   - The targets were black or grey "in front of a white background", and "The response to stationary and moving targets increased with increasing target size".

   The issue contents at https://link.springer.com/journal/10493/volumes-and-issues/9-3 list the article as 10.1007/BF01193433. I could not read the article page at https://link.springer.com/article/10.1007/BF01193433, because the WebFetch proxy refused it with HTTP 429 (rate limited).
4. **Perret, Guerin, Diehl, Vlimant and Gern, 2003, *J. Exp. Biol.* 206(11): 1809 to 1815, doi:10.1242/jeb.00345: confirmed.** The DOI redirects to the journal's abstract page, which is behind a paywall. The full text came from the Neuchâtel repository PDF at https://libra.unine.ch/bitstreams/1725a088-1242-47ce-b427-9fc6cc1da8fc/download, reached through the record at https://libra.unine.ch/handle/123456789/18757. It gives:
   - "I. ricinus does not have eyes with corneas".
   - "two rows of 20–21 photosensitive cells located dorsolaterally", "behind coxa 2", in larvae, nymphs and adults.
   - "Almost all locomotor activities of I. ricinus occurred during darkness". Only 1% of movements fell at peak light on one cycle and 6% on the other.
   - "a drop in light intensity is sufficient to trigger mobility".
5. **Steullet and Guerin, 1992, *J. Comp. Physiol. A* 170(6): 665 to 676, doi:10.1007/BF00198976: confirmed.** The record at https://libra.unine.ch/handle/20.500.14713/60954 places the sensilla "in the capsule of Haller's organ on the tarsus". It says "variations of 0.01% around ambient (ca. 0.04%) induce the strongest frequency modulation" of the CO2-inhibited receptor, and that ticks are "activated from the resting state and attracted by CO2 concentrations of 0.04 to ca. 1%".
6. **Carr, Mitchell, Dhammi, Bissinger, Sonenshine and Roe, 2017, *IJMS* 18(7): 1563, doi:10.3390/ijms18071563: confirmed in part and corrected.** The page at https://www.mdpi.com/1422-0067/18/7/1563 gives "a unique structure found on the foretarsus of the first pair of legs". The phrase "required for host seeking" sits in a sentence that opens "We can only hypothesize", right after a test showing that removing the first legs did not change biting or attachment. It is a hypothesis, and the sheet presents it as a finding. The row text does not use the phrase, so only the source notes change.
7. **CDC, archived page captured 17 October 2012: confirmed.** The page at https://cybercemetery.unt.edu/oilspill/20121017132403mp_/http://www.cdc.gov/ticks/life_cycle_and_hosts.html gives "Ticks find their hosts by detecting animals´ breath and body odors, or by sensing body heat, moisture, and vibrations" and "Some species can even recognize a shadow". It also describes ticks holding on with the third and fourth pairs of legs, the first pair outstretched, "resting on the tips of grasses and shrubs".
8. **Entomology Today, 16 January 2018: confirmed, and the author is added.** The page at https://entomologytoday.org/2018/01/16/up-close-look-tiny-sensory-pits-ticks-use-smell/ is by Meredith Swett Walker. It says the organ "can even sense humidity and infrared light". It names Josek, Allan and Alleyne (2017), *J. Med. Entomol.*, doi:10.1093/jme/tjx232, on *I. scapularis*, *A. americanum* and *D. variabilis*.
9. **Josek, Allan and Alleyne, 2017: secondary, as the sheet marks it.** I did not open it. The details the sheet gives match Entomology Today.
10. **Bertone, Reiskind, Crawley and Watson, 2023, *Common Ticks of North Carolina*, version 1.1: confirmed.** The PDF at https://pdic.ces.ncsu.edu/wp-content/uploads/2023/04/NC_Tick_Guide_v1.0_April_14_2023.pdf says "Many ticks also have a pair of eyes" (p. 2). It gives "large eyes present" for the Lone Star tick (p. 14), "eyes present" for *D. variabilis*, *A. maculatum* and *R. sanguineus*, and says Ixodes and Haemaphysalis lack eyes (pp. 3 to 5, 10 and 11). It does not mention Hyalomma, which agrees with the sheet sourcing Hyalomma from Kaltenrieder. The file name says v1.0, and the cover says 1.1 and is dated 14 April 2023. No publisher is named, and the authors are at NC State University.
11. **Royal Horticultural Society, Gall mites: confirmed** at https://www.rhs.org.uk/biodiversity/gall-mites. It gives "usually less than 0.2 mm long", "usually only be seen with the aid of a microscope", detection by the galls, and "two pairs of legs".
12. **idtools, Eupodides: Eriophyoidea: confirmed** at the address in the sheet. It gives "distinct eyes absent", "usually 0.12 mm long or less", and "all of which are plant parasites".
13. **Lucid soil-mite key, Acariformes page: confirmed** at the address in the sheet. No author is named. It gives "eye lenses almost always well-developed" and "Most postlarval Parasitengona are predators of small invertebrates, particularly arthropods".
14. **Australian Faunal Directory, Trombidiidae: confirmed** at https://biodiversity.org.au/afd/taxa/TROMBIDIIDAE. The compiler is Bruce Halliday. Adults are "predators that feed on a wide variety of small soft-bodied insects and mites", and larvae are parasites.
15. **Olomski, 2012, *Soil Organisms* 84(2): 445 to 458: confirmed, and the title is completed.** The abstract at https://www.soil-organisms.org/SO/article/view/276 describes a single median eye in some groups and "a pair of ocelli situated anteromedially between the lateral eyes" in others. The full title ends "..., Witte & Olomski 1991", and the sheet left those words off.
16. **Wikipedia, Parasitengona: confirmed** at https://en.wikipedia.org/wiki/Parasitengona. Trombidiidae, Erythraeidae and the Hydrachnidia all fall within it.
17. **GBIF occurrence API, dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7: confirmed, with one omission.** Every count I recounted matches the sheet exactly (section 3 below). The Trombidiformes table leaves out the sixth-largest family, Penthaleidae (key 6066), with 467 records.
18. **Repository files: confirmed** (read only). The `docs/views/world-orders.csv` file gives Trombidiformes 104,815, Ixodida 60,462, Mesostigmata 689, Sarcoptiformes 589, Opilioacarida 25 and Holothyrida 11. The `docs/views/no-view-us-fl-alachua.csv` file gives the five Alachua tick species with 121, 11, 11, 8 and 1 records, and the "tick and mite" rows total 163.

## 2. Rows

1. **Eyes (m): kept.** Bertone supports the eye list and "a pair of eyes", and the species are the group's commonest members.
2. **Where they look (g): kept.** The 43 by 49 degree field, the 39 and 33 degree axis and the single lens are all confirmed in *A. variegatum*, a congener of the Lone Star Tick, so `g` is right.
3. **Shapes (g): kept.** The 4.8 degree disc, the 18 m silhouette, the dark target on a pale background and the 3 to 1 contrast are confirmed in *H. dromedarii*, a relative, so `g` is right. The row already marks the blur as the app's reading.
4. **Colour (g): kept.** The single peak near 480 nm by phototaxis and the electroretinogram peak near 470 nm are confirmed in *A. variegatum*.
5. **Without eyes (g): kept.** The two rows of 20 to 21 dorsolateral cells and the walking almost only in darkness are confirmed in *I. ricinus*.
6. **Questing (m): kept, with the source note corrected.** The posture comes from CDC, the organ's position from Carr and colleagues (2017) and the heat sense from Carr and Salgado. The note no longer cites "required for host seeking" as a finding.
7. **Heat (m): reworded.**
   - "at least seven in ten detected" becomes "at least seven in ten adult females detected", because only females were tested at 1 m.
   - "A phone cannot sense that heat" becomes "An ordinary phone cannot sense that heat". The sheet's own section 4 says that a few rugged phones carry thermal cameras. Neither form of that sentence has a source.
   - The source note now says that males and the American Dog Tick were tested at 50 cm.
   - The grade stays `m`, because the measurement is in the Lone Star Tick itself.
8. **Breath (g): kept.** The 0.01% around an ambient 0.04% is confirmed in *A. variegatum*.
9. **Smell, damp and footsteps (x): kept.** It is confirmed by the CDC sentence and by Entomology Today.

## 3. Numbers recomputed

- **The conversion of 4.8 degrees to about 0.1 cycles per degree.** If the 4.8 degree disc is read as half a cycle, one cycle spans 9.6 degrees, and 1 ÷ 9.6 = 0.104 cycles per degree. The arithmetic is right, and 0.1 is a fair rounding.
- **Whether that reading is sound.** It is sound only as a placeholder labelled invented, and the sheet labels it so. It does not measure sharpness, for four reasons.
  - 4.8 degrees is the smallest disc that made camel ticks walk toward it. That is a threshold for a behaviour. It was measured with black targets (16 to 1 contrast in the thesis) at about the best elevation (12.4 degrees, with the optimum near 13).
  - An eye can detect a lone dark spot of high contrast that is smaller than the finest stripes it can resolve. A walking response can also need more than detection. So the true limit could fall on either side of 0.1. This is a general principle of visual science, and I opened no source for it in this audit.
  - The thesis lists the stationary discs tested as 25.0, 17.7, 12.5, 8.8 and 6.3 cm, and it calls the 8.8 cm disc the smallest effective one. Scaled from 4.8 degrees, the 6.3 cm disc subtended about 3.4 degrees, and the thesis implies without stating that it failed. The threshold therefore lies between about 3.4 and 4.8 degrees, and the same half-cycle reading would give 0.10 to 0.15 cycles per degree. The sheet's 0.1 sits at the coarse end of that range. That range is my construction from the thesis's disc sizes.
  - The *Amblyomma* field at half sensitivity (43 by 49 degrees) is about three times as wide and twice as tall as that of *Hyalomma* (14 by 25). That hints, without showing, that the commoner ticks may see more coarsely still. This is my own inference, with no source.

  The plainest account of the number is that nobody has measured what any tick eye resolves, and 0.1 is an order-of-magnitude stand-in borrowed from a behaviour threshold in a desert tick. I keep the value.
- **The engine at `cpd: .1`.** In `src/cam.b.js` the blur radius is 0.6 × (longPx ÷ VIEW_DEG) × (1 ÷ cpd). In `src/cam.a.js`, VIEW_DEG is 24 on a phone and 34 elsewhere.
  - On a phone the radius is 0.6 × 10 ÷ 24 = 0.25 of the long side, as the sheet says. On a desktop it is 0.18.
  - The shader averages 16 samples over a uniform disc of that radius, which is 6 degrees.
  - A 4.8 degree black disc keeps at most (2.4 ÷ 6)² ≈ 16% of its contrast. It would show as a dip in brightness of about 15% at its centre, a faint smudge.
  - A threshold target ought to look barely visible, so the row "Shapes" and the value agree with each other.
- **The field of view.** 39 ± 21.5 degrees gives edges at 17.5 and 60.5 degrees on each side, so the two fields span 121 degrees and leave a 35 degree gap straight ahead. This is correct now that 39 degrees is confirmed as a horizontal angle. In `paramsOf`, any `fov` under 180 is clamped to a zoom of 1, so the sheet's "values under 180 change nothing" is right.
- **`M`.** The shader loads the matrix row-major (`gl.uniformMatrix3fv(u.u_M, true, ...)`). Three identical rows of .05, .45 and .5 therefore give grey: pure red maps to 0.05, and each row sums to 1. The sheet's description holds.
- **`pupil: 'none'`.** In `paramsOf`, only 'v' and 'h' change the blur shape, so 'none' and 'o' give the same picture, as the sheet says.
- **Shares.** These sums and shares are all correct:
  - 60,462 + 98,340 + 7,789 = 166,591, giving 36.3%, 59.0% and 4.7%.
  - 104,815 − 98,340 = 6,475, and 6,475 + 689 + 589 + 25 + 11 = 7,789.
  - The eyed genera hold 41,278 records (68.3%) and the eyeless ones 18,920 (31.3%).
  - The twelve largest mite families sum to 104,407, which leaves 408 records outside them.
- **Thresholds.** 5.2 × 10^8 ÷ 5.2 × 10^6 = 100, which supports "a hundred times lower".
- **Carbon dioxide.** 0.01% is "a hundredth of a percent", as the row says.

## 4. GBIF recount (12 October 2026)

All of these counts match the sheet exactly:

- Trombidiformes (key 543): 104,815 records. The families are:
  - Eriophyidae 98,340
  - Tetranychidae 1,794
  - Phytoptidae 1,056
  - Trombidiidae 975
  - Bdellidae 742
  - **Penthaleidae 467** (missing from the sheet)
  - Erythraeidae 399
  - Leeuwenhoekiidae 257
  - Tarsonemidae 116
  - Anystidae 92
  - Demodecidae 85
  - Eupodidae 84

  None of these twelve is a water-mite family. The nearest water mite is Arrenuridae, 15th with 49 records.
- Eriophyidae species: *Eriophyes tiliae* has 11,583 records and *Vasates quadripedes* has 4,465.
- Ixodida (key 1425): 60,462 records. The genera are Dermacentor 26,809, Ixodes 18,541, Amblyomma 13,032, 720 for key 2183844, Hyalomma 717 and Haemaphysalis 379. I identified the keys for Ixodes, Hyalomma and Haemaphysalis by name. The keys for Dermacentor and Amblyomma follow from the species totals. I did not look up key 2183844, so the name Rhipicephalus for its 720 records rests on the sheet alone.
- The eight leading tick species match the sheet's names and counts (20,162 down to 1,940). I identified four keys through the Alachua file and four through the species API.

## 5. Other problems

- **Mite family table.** It omits Penthaleidae (467). The checked sheet adds the family and rewrites the lead-in as a full sentence.
- **Sentence fragments.** These four were rewritten as full sentences in the checked sheet: "Two implementation notes:", "Of 104,815 records:", "What it does show:" and "Where its claims go beyond its experiments:".
- **"6 degrees or less".** The phrase appears in section 3, the section 4 table, the skin-colour paragraph, the Carr and Salgado source line and open question 1. All five places now read "at most 5.7 degrees".
- **Unfinished list.** The checked sheet updates it. The Carr and Salgado figures and the Kaltenrieder DOI are now checked. The preprint and the 1990 article page were not opened. The statements about phones still have no source.
- **Cue.** The 33 degree elevation of *A. variegatum*'s eyes was measured in the natural walking posture. A questing tick on a grass tip may hold its body otherwise, so "tilt it up" is the app's own choice. The sheet already calls the cue the app's wording, so I made no change.
- **Wording rules.** The sheet has no em dashes, no "not X but Y" turns, nothing said to matter, and no praise. Its American spellings (odors, meters, Centers) occur only inside quotations or proper names. "Aluminum" is the Canadian spelling.

## 6. Not reached

- The bioRxiv preprint (permission request withdrawn) and the Springer article page for Kaltenrieder (1990) (HTTP 429).
- Any source for the statements that an ordinary phone cannot sense body heat and that no phone records carbon dioxide.
- The searches the sheet left undone: flicker fusion or dim-light sensitivity in ticks, and eye measurements in the Lone Star Tick or the American Dog Tick. I did not run them, because they fall outside an audit of the sheet's sources.
