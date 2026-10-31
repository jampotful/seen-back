# audit-331: desk-d237, evidence lines 1 to 4

Audited 31 October 2026 from the desk-d237 files present untracked in the worktree (docs/tracks/progress/desk-d237.md and docs/views/evidence/desk-d237.jsonl, 4 lines; neither committed here, neither edited). HEAD and origin/main fd257966 (desk-d236). `python3 -I tools/senses/check.py | grep d237`: "docs/views/evidence/desk-d237.jsonl: 4 records, 0 problems". Quote lengths (`len(q.split())`): 17, 19, 17 and 13 words, all within 40. Evidence records only; audits 328 to 330 are the format model, and the desk-audit.md evidence clause applies (40-word limit, no 125-character limit). Quotes returned in abutting pieces are judged under the six conditions in audit-324.md.

Sources opened (WebFetch): api.crossref.org/v1/works/ for 10.1371/journal.pone.0101497 and 10.1371/journal.pone.0100330 (one pass each); journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0101497 (four passes); journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0100330 (two passes); for names, api.obis.org/v3/taxon/ for Poecilia parae and Gasterosteus aculeatus. WoRMS and GBIF not opened (refused per rules). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 0 WebSearches and 10 WebFetch calls used.

## Bibliographic and licence

- Lines 1, 3, 4. Crossref: Jorge L. Hurtado-Gonzales, Ellis R. Loew, J. Albert C. Uy; "Variation in the Visual Habitat May Mediate the Maintenance of Color Polymorphism in a Poeciliid Fish"; PLoS ONE 9(7), e101497; issued and published online 2014-07-02; journal-article; relation empty, no update-to. Page byline same three names in the same order; citation verbatim "Hurtado-Gonzales JL, Loew ER, Uy JAC (2014) ... PLoS ONE 9(7): e101497." Licence: page "This is an open-access article distributed under the terms of the" "Creative Commons Attribution License, which permits unrestricted use,"; Crossref CC BY 4.0, content-version unspecified, delay 0. Accepted (Crossref unspecified + page-printed CC Attribution License). Faults 0.
- Line 2. Crossref: Yi Ta Shao, Feng-Yu Wang, Wen-Chun Fu, Hong Young Yan, Kazuhiko Anraku, I-Shiung Chen, Bertil Borg; "Androgens Increase lws Opsin Expression and Red Sensitivity in Male Three-Spined Sticklebacks"; PLoS ONE 9(6), e100330; issued and published online 2014-06-25; journal-article; relation empty, no update-to. Page byline same order; citation "PLoS ONE 9(6): e100330." Licence: page "This is an open-access article distributed under the terms of the Creative Commons Attribution License,"; Crossref CC BY 4.0, content-version unspecified, delay 0. Accepted as above. Faults 0.

source.access "open" right for all four. Bibliographic faults 0; licence faults 0.

## Names

- Poecilia parae (lines 1, 3, 4): OBIS "Poecilia parae", "Eigenmann, 1894", "accepted", family Poeciliidae, order Cyprinodontiformes, taxonID 307990 (the WoRMS AphiaID). Main's Poecilia reticulata rows (fish-shark corrected lines 112-113) carry the same family and order. Met. The note's order source (a Xiphophorus row) can stand; OBIS is now the stronger source (uncounted, replacement given).
- Gasterosteus aculeatus (line 2): OBIS "Gasterosteus aculeatus", "Linnaeus, 1758", "accepted", Gasterosteidae, Perciformes, taxonID 126505; gbif-names.tsv "EXACT ACCEPTED"; canon-3 row 122 Gasterosteidae/Perciformes. Met.

## Duplicates

git grep on origin/main (fd257966) across the whole docs/ tree (evidence, audit incl. audit/corrected and audit/ALL, sheets, searched, gaps, progress) for "Poecilia", "parae", "Hurtado", "pone.0101497", "0101497", "Gasterosteus", "stickleback", "Yi Ta Shao", "pone.0100330", "0100330". A grep of all non-audit remote branches' docs/views for the two DOIs hits only research/desk-d237 itself.

- Poecilia parae and the 0101497 DOI: no hit on main. Poecilia hits are P. reticulata (fish-shark corrected 112 lambda_max_nm [358.6, 560], 113 colour_vision, both another species and paper), the multi-species fish-shark 177 spectral_range_nm (Matsuo et al. 2021, 10.1098/rsos.210415, P. reticulata among six species), and Poecilia latipinna in an Alachua species list. Not a repeat.
- Gasterosteus aculeatus on main: colour_vision (canon-3 row 122; oa-1 rows 264-265, review-sourced behaviour) and the fish-shark 177 multi-species near-infrared optomotor threshold. No ERG row, no 0100330 hit. Stickleback progress hits: desk-d223 held a flow-refuge paper (PeerJ 5: e3121), another paper. Not a repeat.

Duplicate faults 0.

## Trait key and grading

`"trait": "erg_peak_nm"` on main: desk-d221 row 3 (Anomalops katoptron 480 nm, "in vivo electroretinogram, wavelength series", eye "whole retina") and oa-4 rows 566-574 (Hermetia illucens, regional ERG maxima, units nm). Line 2 (units nm, the most sensitive tested wavelength in a whole-eye ERG threshold series) matches that usage; the note carries "new trait" as check.py needs. lambda_max_nm fits lines 1, 3, 4 (MSP template fits, one receptor class each for lines 1 and 3; line 4 a labelled range across classes, see below). Grade `m` right for all four: one named species measured by the authors.

## Cut-quote ruling

The quote rule allows a marked cut that does not drop a qualifier. Read against the full sentences returned by the page tool (first pass of e101497 and first pass of e100330):

- Line 3. Printed sentence: "Most notably, the retina of Poecilia parae contains single cones with UV absorption at 355±1.4 nm" "(“UVS”; n = 11 individuals) and a violet/blue at 407±1.6 nm (“SWS”; n = 17 individuals)." The cut drops the class label, the count of individuals in which the UV class was found, and a second cone class. None changes what "355±1.4 nm" means; the cut is acceptable under the quote rule. But the dropped count is scientifically consequential: the UV class was recorded in 11 of the 17 fish, against 17 of 17 for the violet class, and the paper does not explain the difference (tool summary). The record nowhere gives n = 11 and its conditions describe a 17-fish sample, so a reader would take the value as resting on all 17. Counted as sample composition omitted (below), not as a quote fault.
- Line 4. Printed sentence: "Values for λmax of double cones ranged from 456 to 553 nm: 456±1 nm (n = 17 individuals)," "526±0.8 nm (n = 17 individuals), 533±2 nm (n = 11 individuals), 543±1 nm (n = 17 individuals)," "and 553±1.9 nm (n = 5 individuals)." (43 words, so a cut is needed.) The cut drops the per-class values and counts; the range statement is complete as printed and is not qualified by the list. Acceptable under the quote rule. The range spans five double-cone classes and the method labels it "Range over double-cone classes ... not a single receptor class", which is right. But the upper bound rests on 5 of 17 fish and the 533 nm class on 11; the method says "each with n individuals" without giving them, and the Discussion's reading ("some individuals may be expressing at least one different LWS as a double cone") is not carried. Counted as sample composition omitted.
- Line 2. Printed sentence: "Light-adapted sticklebacks exhibited the greatest sensitivity (lowest threshold) to light with a wavelength of 500 nm" "(21.5±1.56 quantum flux (10−5 µmol/m2/s); means ± SD) ([Fig. S2])." The cut drops the threshold flux and SD only; the figure reference after the ellipsis is kept. Acceptable. (The whole sentence is 26 words and could be quoted whole; the page prints a minus sign in "10−5", which the note writes as a hyphen, uncounted.)

Abutting-piece check: on this audit's fourth pass of e101497 the tool declined both full sentences and returned only the first pieces, so a whole-sentence quote for lines 3 and 4 would fail condition 3 of audit-324.md for now; the desk's cut quotes stand and no whole-sentence replacement is proposed for them.

## Per-record findings

### Line 1, Poecilia parae, lambda_max_nm, rod 503 nm

Quote, verbatim and whole in one piece: "Rod cells were also observed and had an estimated λmax 503±1.2 nm (mean±SD, n = 17 individuals)." MATCH, 17 words; value says no more. Design, verbatim: "males and females of P. parae were collected from the sampling sites"; "In January 2010, with the exception of individuals used for reflectance measurements"; "and were transported to our laboratory at Syracuse University."; "Fish were maintained in 20 gal aquaria with treated water at 27±1°C, on a 12∶12 h light: dark cycle"; "fish were housed in complete darkness for 24 hours."; "were used for microspectrophotometry (MSP) analyses at Cornell University, Ithaca, New York."; "MSP scans were collected at 1 nm intervals scanning from 750 to 350 nm, and back from 350 to 750 nm"; "Finally, normalized data were best-fitted using the A1 templates"; "Absorbance spectra from 30–40% of cells measured were retained for analysis"; "seven adult males (immaculata: n = 2, parae: n = 2, blue: n = 2 and yellow: n = 1 morphs) and 10 adult females"; "we have no conclusive evidence suggesting that the LWS photopigments are either polymorphic or sex-linked". No morph or sex comparison of λmax anywhere (tool summary). Wild-caught in Guyana (the page says "collected from the sampling sites" and cites an EPA collection permit), not lab-bred; no Trinidad population. All as recorded. **MATCH.** Uncounted: "either side of the Demerara River" -> page "east" and "sides" (east and west); the conditions sentence "Cone classes ... are separate values not logged here" should point to lines 3 and 4.

### Line 2, Gasterosteus aculeatus, erg_peak_nm, 500 nm

Quote verbatim, cut marked (see ruling). MATCH, 19 words. Design, verbatim: "Three-spined sticklebacks were caught at the shore of the Öresund and southern Baltic at the coast of Skåne, south Sweden."; experiment 4 fish "Dec 16th 2012 at Skåre" (tool summary of a date list); "Fish were sent by airfreight to Taiwan in July 2013."; "males were kept under a short day photoperiod at 20°C for 2 weeks before experimental treatments."; "clear artificial brackish water (0.5% salinity)."; "Five castrated males, 5 castrated males with 11 KA implants, and 5 sham-operated fish were maintained separately" "in 30 L aquaria under a long day photoperiod at 20°C for 28 days."; "Five sham-operated males were kept under short day conditions."; "Empty implants were used as controls."; "Light-adapted fish were immobilized by injection of gallamine triethiodide" after MS-222; corneal recording electrode; "diffuse white background light (c. 12 lx)." "for 1 hr before the ERG test."; "wavelengths of 400, 440, 460, 480, 500, 520, 560, 600, and 670 nm."; "10 stimuli, each of 20 ms in duration, with an inter-stimuli interval of 5 s"; threshold = "Deflection of the ERG trace"; sensitivity "–log10 of the threshold"; photon flux by "USB 2000 spectrometer", "calibrated ... at the fish eye." Results: "No significant difference in the threshold at 500 nm was observed between treatments (p>0.05 for each comparison)."; "The relative sensitivities in the green spectrum (500 or 520 nm) were far higher than those for red (600/670 nm)" "and blue (440 nm) for all treatments."; long-day vs short-day 600 nm greater, 670 nm p = 0.073; "sham-operated males and castrated males treated with 11 KA showed significantly greater" "relative sensitivity to the red part of the spectrum (600 and 670 nm)"; "No significant difference in relative sensitivity was observed at any other wavelength." Population is the coastal Öresund/southern Baltic (brackish) stock, wild-caught; the paper does not say marine or freshwater ecotype (tool summary). Thresholds measured, not intensity-matched; no matching issue arises. The record's method, n (4 x 5 males), groups, pooled 500 nm statement and the 500 nm null are right. **MATCH.** Uncounted additions: 1 h light adaptation, the wavelength list (20 to 40 nm spacing, so 500 nm is the best of the sampled points with 520 nm close: "500 or 520 nm"), brackish holding water, transport in July 2013, and the androgen effect at both 600 and 670 nm (the conditions say "(600 nm)" only).

### Line 3, Poecilia parae, lambda_max_nm, UV single cone 355 nm

Quote verbatim, cut marked; MATCH, 17 words; value says no more. Design as line 1. **Error (sample composition omitted).** The UV class was found in 11 of the 17 fish ("(“UVS”; n = 11 individuals)"); the record gives no n for the value and its conditions describe a 17-fish sample. Fixable.

### Line 4, Poecilia parae, lambda_max_nm, double cones 456-553 nm

Quote verbatim, cut marked; MATCH, 13 words. Range labelled as a range across five double-cone classes (456, 526, 533, 543, 553 nm), correctly, eye "double cones". Each of lines 1, 3, 4 is a distinct receptor-class value (rod; UVS single cone; double-cone range); the violet SWS 407 nm class is not filed. **Error (sample composition omitted).** Per-class counts not given: 456, 526 and 543 nm in 17 fish, 533 nm in 11, 553 nm in 5, so the range's upper end rests on 5 of 17 fish; the Discussion's reading that some individuals may express a different LWS pigment is not carried. Fixable.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Poecilia parae, rod 503 nm | MATCH | conditions (uncounted) | whole sentence, design complete |
| 2 | Gasterosteus aculeatus, ERG 500 nm | MATCH | conditions (uncounted) | cut drops flux only; design and null carried |
| 3 | Poecilia parae, UVS 355 nm | error | method | n = 11 of 17 fish omitted |
| 4 | Poecilia parae, double cones 456-553 nm | error | method, conditions | per-class n (553 nm in 5 fish) and LWS reading omitted |

Errors 2 of 4 records (50%), above the 5% bar; both fixable with the text below; none held out. Unchecked: the page tool did not return Figure S1/S2 or Fig. 5, the Poecilia Methods coordinates, or the number of cells measured per class; the stickleback collection dates for experiments other than 4 were only summarised.

Answers to the desk owner questions: (1) erg_peak_nm is used on main (desk-d221, oa-4) with the same units; extending check.py TRAITS is the owner's call, and until then "new trait" in the note is required. (2) A cut after the value is acceptable when the dropped text is a per-class count, a second class, or a threshold flux, as here; the count still has to appear in the record when it is the n behind the logged value.

## Replacement text

Line 1 (uncounted):
- `conditions`: "collected January 2010 from sampling sites on either side of the Demerara River, Guyana," -> "collected January 2010 from sampling sites on the east and west sides of the Demerara River, Guyana (collection permit from the Guyana Environmental Protection Agency),"
- `conditions`: "Cone classes (UV 355, violet 407, double cones 456 to 553 nm) are separate values not logged here;" -> "Cone classes (UV 355, violet 407, double cones 456 to 553 nm) are separate values (UV and double cones filed as desk-d237 lines 3 and 4; violet not filed);"
- `note`: "order as on main for another Poeciliidae row (Xiphophorus hellerii, Cyprinodontiformes)." -> "order as on main for another Poeciliidae row (Xiphophorus hellerii, Cyprinodontiformes); OBIS: Poecilia parae Eigenmann, 1894, accepted, Poeciliidae, Cyprinodontiformes, taxonID 307990 (audit 331)."

Line 2 (uncounted):
- `method`: "sensitivity = -log10 of the threshold light intensity for each of nine test wavelengths from 400 to 670 nm" -> "sensitivity = -log10 of the threshold light intensity (threshold = visible deflection of the ERG trace) for each of nine test wavelengths (400, 440, 460, 480, 500, 520, 560, 600 and 670 nm)"
- `method`: "500 nm is the most sensitive of the nine tested wavelengths, not a fitted template peak" -> "500 nm is the most sensitive of the nine tested wavelengths, not a fitted template peak; the paper groups 500 and 520 nm together as far more sensitive than 440, 600 and 670 nm"
- `conditions`: "(ERG fish caught December 2012), air-freighted to Taiwan and kept under controlled photoperiods;" -> "(experiment 4 fish caught 16 December 2012), air-freighted to Taiwan in July 2013, held in artificial brackish water (0.5% salinity) at 20 C on short day for 2 weeks, then 28 days of treatment;"
- `conditions`: "immobilised fish on diffuse white background light (c. 12 lx)." -> "fish anaesthetised with MS-222, immobilised with gallamine triethiodide and light-adapted for 1 h on diffuse white background light (c. 12 lx); corneal recording electrode."
- `conditions`: "relative red (600 nm) sensitivity rose with androgen and long day," -> "relative red sensitivity rose with androgen (600 and 670 nm, long day) and with long day (600 nm),"
- `note`: "(21.5±1.56 quantum flux (10-5 µmol/m2/s); means ± SD)" -> "(21.5±1.56 quantum flux (10−5 µmol/m2/s); means ± SD)"

Line 3 (counted):
- `method`: "UV-sensitive single cone, 355 +/- 1.4 nm;" -> "UV-sensitive single cone, 355 +/- 1.4 nm, found in 11 of the 17 fish examined (n = 11 individuals; the violet class was found in all 17; the paper gives no reason);"
- `note`: "the cut part is marked with an ellipsis and carries per-class individual counts, not a qualifier of the value)." -> "the cut part is marked with an ellipsis and carries the class label, the count n = 11 individuals and the violet class, none a qualifier of the value; the count is carried in method; cut ruled acceptable in audit 331)."
- `note` (uncounted): append " OBIS: Poecilia parae Eigenmann, 1894, accepted, Poeciliidae, Cyprinodontiformes, taxonID 307990 (audit 331)."

Line 4 (counted):
- `method`: "Range over double-cone classes (the cut text lists 456, 526, 533, 543 and 553 nm, each with n individuals); the range is not a single receptor class." -> "Range over five double-cone classes (the cut text lists 456 +/- 1 nm in 17 fish, 526 +/- 0.8 nm in 17, 533 +/- 2 nm in 11, 543 +/- 1 nm in 17 and 553 +/- 1.9 nm in 5); the range is not a single receptor class, and its upper end rests on 5 of 17 fish. Double and twin cones commonly paired as 456/526, 456/533, 456/543, 526/533, 533/533, 543/543 and 553/553."
- `conditions`: "the authors state they have no conclusive evidence that LWS photopigments are polymorphic or sex-linked." -> "the authors state they have no conclusive evidence that LWS photopigments are polymorphic or sex-linked, and suggest that some individuals may express at least one different LWS pigment as a double cone."
- `note`: "the cut part is marked with an ellipsis and carries per-class individual counts, not a qualifier of the value)." -> "the cut part is marked with an ellipsis and carries the per-class values and counts, which do not qualify the printed range; the counts are carried in method; cut ruled acceptable in audit 331; whole sentence 43 words)."
- `note` (uncounted): append " OBIS: Poecilia parae Eigenmann, 1894, accepted, Poeciliidae, Cyprinodontiformes, taxonID 307990 (audit 331)."
