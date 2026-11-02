# audit-431: desk-d320, evidence lines 1 to 8 (lines 9 and 10 audited separately)

Audited 1 November 2026 from the desk-d320 files present untracked in the worktree (docs/views/evidence/desk-d320.jsonl, 10 lines, and docs/tracks/progress/desk-d320.md; neither committed here, neither edited). HEAD = origin/main (557f009dd). `python3 -I tools/senses/check.py | grep d320`: "10 records, 0 problems". Quote lengths (`len(q.split())`), lines 1 to 8: 29, 29, 32, 17, 17, 17, 17, 8, all within 40.

Sources opened (WebFetch, every URL from a WebSearch result): link.springer.com/10.1186/s40851-023-00205-w (two passes; opened, no refusal), zoologicalletters.biomedcentral.com figures/7 (caption only), doaj.org article 53c951a1... (metadata), mdpi.com/2076-2615/13/6/1016 (two passes), frontiersin.org/articles/10.3389/fevo.2022.787315 (three passes; the /text and public-pages-files copies gave only the abstract), pmc.ncbi.nlm.nih.gov/articles/PMC3589346 (two passes, no reCAPTCHA shown), reptile-database.reptarium.cz Trachylepis/quinquetaeniata, obis.org taxon pages 107138, 514112, 513956, 514110. Crossref list queries: prefix 10.1186 (March 2023) and prefix 10.3389 (24 March 2022) answered; prefix 10.1371 was rate-limited twice and not retried (the PMC copy prints the licence, so not needed). Single-DOI Crossref /v1/works/ refused with client_error, not worked around. Not opened: the saludcastillayleon.es PDF mirror (a hospital-library host, treated as a proxy), libmast.utm.my, ebusca.uv.mx, uitm, scribd mirror, reviewer.ly, accedacris repository PDF, WoRMS, GBIF. 15 WebSearches. WebFetch gives verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim.

## Repeats (whole docs/ tree of origin/main)

`git grep -il` for Trachylepis, s40851-023-00205, Caretta, ani13061016, Allosergestes, "Sergia tenuiremis", Phorcosergia, Eusergestes, fevo.2022.787315, Benthosema, pone.0058519, Sergestidae, and for the values 3.972 and 22.83.

- Trachylepis quinquetaeniata / 10.1186/s40851-023-00205-w: on main as eye_type (herps-met, audit/corrected/herps-met, ALL), genus-level fovea (recheck-codex-b-fixed, sweep-34) and in searched/ files. No eye_axial_length_mm or eye_diameter_mm, and 3.972 appears nowhere. Earlier audits treat a different trait from the same paper as no repeat (audit-139 line 3; audit-341 Acanthaster; the repeat rulings in audits 103, 320 and 326 all need same DOI and same trait). Lines 1 and 2: not repeats.
- Caretta caretta: on main under other traits and papers; ani13061016 and 22.83 absent; no Caretta eye_axial_length_mm or eye_diameter_mm row. Not a repeat.
- Shrimps: fevo.2022.787315 absent. **The notes' "Genus not on main under any trait" is wrong for three lines**: Allosergestes pectinatus is on main as acuity_cpd 0.12 (canon-4, Feller et al. 2021, 10.1016/j.asd.2020.101002); Phorcosergia grandis as cff_hz 22 (oa-6, Lafitte et al. 2022 review supplement); Eusergestes arcticus as cff_hz 21, 17 and 16 (oa-3, oa-6, same review). Different traits and papers, so not repeats, but the notes misstate main. Sergia tenuiremis and genus Sergia are not on main as taxa (Sergia appears only as a former name inside Phorcosergia quotes), so line 5's note stands.
- Benthosema glaciale / pone.0058519: absent. Not a repeat.

## Bibliographic and licence

- Lines 1 and 2 (El-Bakary et al. 2023). Springer page title "New insights into the retinal microstructure-diurnal activity relationship in the African five-lined skink" "(Trachylepis quinquetaeniata) (Lichtenstein, 1823)", "Volume 9, article number 7 (2023)", published 18 March 2023; byline truncated by the tool. Crossref (prefix list query): Neveen E. R. El-Bakary, Mohamed A. M. Alsafy, Samir A. A. El-Gendy, Samar M. Ez Elarab, in that order; Zoological Letters 9, issue 1, article 7, issued 2023-03-18; licence CC BY 4.0, content-version vor (and tdm). DOAJ lists the same four authors in that order. Page shows "You have full access to this open access article" and no CC sentence (tool summary). No licence sentence on the page plus Crossref CC BY 4.0 vor: accepted. Authors, title, journal 9(1): 7, year 2023, DOI match.
- Line 3 (Fumero-Hernández et al. 2023). MDPI page: Marcos Fumero-Hernández, Mario Encinoso Quintana, Ana S. Ramírez, Inmaculada Morales Fariña, Pascual Calabuig, José Raduan Jaber; "Animals 2023, 13(6), 1016"; "distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license". Accepted.
- Lines 4 to 7 (Schweikert et al. 2022). Frontiers page: authors as filed, "Front. Ecol. Evol., 24 March 2022"; no licence sentence in the returned text. Crossref: Lorian E. Schweikert, Kate N. Thomas, Vanessa M. Moreno, Anchita Casaubon, Charles Golightly, Heather D. Bracken-Grissom; title identical; volume 10, no issue, article 787315; issued 2022-03-24; CC BY 4.0 vor. Accepted.
- Line 8 (de Busserolles et al. 2013). PMC copy: Fanny de Busserolles, John L Fitzpatrick, John R Paxton, N Justin Marshall, Shaun P Collin; "2013 Mar 5;8(3):e58519."; "This is an open-access article distributed under the terms of the Creative Commons Attribution License". Licence printed on the exact copy read: accepted (Crossref content-version "unspecified" per the desk; my Crossref query was rate-limited).

Bibliographic faults 0. Licence faults 0. source.access "open" right throughout.

## Names and higher taxa

- Trachylepis quinquetaeniata: Reptile Database species entry, higher taxa Scincidae, Squamata; Mabuya quinquetaeniata in its synonym list; Egypt in the distribution. Accepted. Class Reptilia from the catalogue (disclosed).
- Caretta caretta: accepted; Cheloniidae, Testudines.
- Sergia tenuiremis (Krøyer, 1855), Allosergestes pectinatus (Sund, 1920): OBIS taxon pages list them as species under Sergestidae, Malacostraca, Decapoda, no synonym redirect. Eusergestes arcticus and Phorcosergia grandis are on main as accepted names in the Lafitte review rows ("Eusergestes arcticus Krøyer, 1855", "Phorcosergia grandis Sund, 1920"). WoRMS not opened (refused list). No name faults.
- Benthosema glaciale: accepted; Myctophidae, Myctophiformes.

## Per line

### Line 1, Trachylepis quinquetaeniata, eye_axial_length_mm 3.972

Springer page, under heading "Results": "The total axial length of the eye (from cranial to caudal part) was 3.972 ± 0.16 mm," + clause with "transverse diameter" "4.85 ± 0.25 mm" and "(Fig. 1A, B)" (tool cut the second half). The section's first sentence: "The African five-lined skink (Trachylepis quinquetaeinata) is a medium-sized lizard that measures 20 cm (7.9 inches)." Quote MATCH (29 words, whole sentence, the paper itself says "axial length"). Methods: ten adults, Abou Rawash-Giza, "The lizards were euthanized via intramuscular injection of a lethal dose of Ketamine hydrochloride"; "Both eyes were freshly dissected and prepared for light and transmission electron microscopy"; no eye count and no instrument for the eye dimensions (tool summary): as in conditions. Sex not reported: right.

Two uncounted inaccuracies (optional fixes): (a) `where` says the sentence sits in "unlabelled text"; the page prints a "Results" heading directly above the section. (b) The only statistics sentence, under Methods "Morphometric analysis", reads "The obtained TEM images were analyzed by the ImageJ application to measure the thickness of the retina layers" "and the area and circumference of the melanosomes and droplet oil," "and the mean and standard error were done by Microsoft Excel". It is scoped to TEM measures, so "the page does not say whether the ± is SD or SE" is defensible for the eye dimensions, but the record should mention that the paper's only stated statistic is mean and SE.

**Line 1 OK.**

### Line 2, Trachylepis quinquetaeniata, eye_diameter_mm 4.85

Same sentence and checks as line 1. Value is the transverse diameter as printed. Same optional fixes.

**Line 2 OK.**

### Line 3, Caretta caretta, eye_axial_length_mm 22.83

Results: "Last, the eyeball presented a mean height of 22.23 mm (range = 15.9–27), a mean width of 15.77 mm (range = 12–19.2)," "a mean length of 22.83 mm (range = 16–27.9)." Preceding sentence ends "(range = 1.8–5.56), respectively, with no significant differences." Quote MATCH (32 words). Table 1 row "Eyeball length (mm)": right 22.95 (16–27.9, SD 3.37), left 22.71 (18–27.1, SD 2.83), both 22.83 (median 22.40, 16–27.9, SD 3.00), r² 0.61, p 0.00005. Methods: "Length of the eyeball or distance between the most rostral and caudal portion of this structure"; width "the lateromedial length of the globe"; 10 turtles, 19 to 30 kg, CCL mean 41.53 cm (25–71.7), "young and subadult", no sedation, Toshiba Astelion 16-slice, "analysed by two observers": as in conditions.

Faults (one record error, fixable):
(a) **Trait says more than the quote.** The paper never uses "axial" or "anteroposterior" (tool check of the whole text). Its "length" is the rostrocaudal extent in the dorsal plane, while it measures the lateromedial extent separately as "width". Filing the rostrocaudal extent as eye_axial_length_mm asserts an optical-axis measurement the paper does not make. The desk flagged the weak spot but filed it anyway. Fix: file it as eye_diameter_mm (rostrocaudal), as main does for the myctophid rostro-caudal diameter (line 8). No Caretta eye_diameter_mm is on main, so the change creates no repeat.
(b) **Omitted significant result.** Results: "When linear regression analysis was conducted to evaluate the correlation between the measurements and the carapace length" "statistical significance was found with the lens diameter (R2 = 0.40; p = 0.00290)" "and eyeball length (R2 = 0.61; p = 0.00005)." Eyeball length scales with body size across turtles of 25 to 71.7 cm CCL, so the pooled mean depends on sample composition. The conditions omit this, and also the null "The Mann–Whitney U test revealed no significant differences when the measurements from the right and left eyes were analysed."

**Line 3 FIXABLE.**

### Lines 4 to 7, Sergestidae, eye_diameter_mm (Table 1 rows)

Table 1 sits under Materials and Methods "Sampling". Caption "Metadata of the study species’ eye diameter, body length, and ecological classifications."; footnote "*Eye and body size (mm) were measured and ecological data were provided by published literature." and "All numeric data provided are mean values, except for sample size (n), diel vertical migration (DVM)" "distance (m), and maximum reported depth (m)." Rows as returned:
- "| *Allosergestes pectinatus*[2,4] | 14 | 0.5 | 20.0 | 146[13] | 446[13] |" "| 300 | 1,300[15] | Pelagic[15] | Pesta[17] |"
- "| *Sergia tenuiremis*[1,6] | 28 | 1.3 | 45.4 | 1,250[14] | 1,750[14] |" "| 500 | 2,000[14] | Pelagic[14] | None[14] |"
- "| *Phorcosergia grandis*[7,8] | 51 | 1.5 | 56.1 | 350[14] | 1150[14] |" "| 800 | 2,300[14] | Pelagic[14] | Unlensed[19] |"
- "| *Eusergestes arcticus*[1,2] | 5 | 1.4 | 54.0 | 330[13] | 700[13] |" "| 370 | 1,000[15] | Benthopelagic[15] | Pesta[17] |"
All four quotes MATCH (whole rows, 17 words each); the species-name superscripts point to the numbered sources under the table, e.g. 1 = Krøyer 1855, 2 = Judkins and Kensley 2008 (tool summary). Method: "Measurements of eye diameter and body length (mm, ±0.1 mm resolution) were collected using Mitutoyo CD-8 ASX"; "eye diameter was measured at the maximum distance found perpendicular" "to the dorsoventral eye axis". Adults: "Our data represent shrimp in the adult stage of their ontogenetic development." Sex not stated. A table in Methods with mean values from the caption is acceptable: the quote is a whole row from one section and the value is in it.

Faults:
(a) **Omitted design confound (lines 4, 5, 6, 7; one error each).** The conditions say "preservation of the expedition animals was not read". The paper prints: "Animals from the first expedition (n = 49) were measured after fixation in 4% paraformaldehyde in 0.1 M" ... "and those from the second expedition (n = 193) were measured fresh prior to fixation."; FICC animals "were preserved in ∼70% EtOH prior to measurement." Results (Static Allometry): "Because preservation type is represented unevenly across species, we could neither determine the role of preservation type" " separate from species effects nor apply a correction for preservation type to subsequent analyses." Adding preservation type improved the mixed model (ΔAIC = 30, Table 2; "significant, but small effect", tool summary). Each species mean therefore mixes fresh, paraformaldehyde-fixed and ethanol-preserved animals in unknown proportions, with a measurable preservation effect the authors could not remove.
(b) **Wrong repeat statement in the note (lines 4, 6, 7).** "Genus not on main under any trait" is false (see Repeats). It does not change the verdict, but it must be corrected before merge.

"Smallest sample of the table (n = 5)" (line 7) was not checked against every row; unchecked.

**Lines 4, 5, 6, 7 FIXABLE.**

### Line 8, Benthosema glaciale, eye_diameter_mm 4.6

PMC copy, Results "Morphometric measurements", Table 3 ("Range of standard length, eye diameter and lens diameter for each of the 61 species of Myctophidae analysed in this study."): row "Benthosema glaciale | 1 | 42 | 4.6 | 1.8 | A | 8" under Species, n, SL, Eye ø, Lens ø, stage, Cruise. Quote MATCH (whole row, 8 words). A = adult (J = juvenile). Methods: "For each individual, the standard length, rostro-caudal eye diameter (measured in situ) and lens diameter were measured" "with digital calipers to 0.1 mm."; "When samples were acquired from collaborators (Cruises 7, 8, 9, see Table 1), the measurements were made after fixation."; Table 1 cruise 8: "Balearic Islands, Western Mediterranean Sea", "07/2010", "Double-warp modified commercial mid-water trawl/IKMT", "Day, Night", "Karnovsky". No correction: "no measurement correction was used between fresh and fixed specimens" (the 0.8% figure concerns body length under formaldehyde). The only other mention of B. glaciale is the Discussion's note that larger or older specimens become non-migrant, which bears on migration, not eye size. Conditions complete; value says no more than the row.

**Line 8 OK.**

## Summary

| Line | Taxon | Trait | Verdict | Reason |
|---|---|---|---|---|
| 1 | Trachylepis quinquetaeniata | eye_axial_length_mm | OK | quote, value and licence verified; `where` and SE wording are optional fixes |
| 2 | Trachylepis quinquetaeniata | eye_diameter_mm | OK | as line 1; same DOI on main under a different trait, not a repeat |
| 3 | Caretta caretta | eye_axial_length_mm | FIXABLE | the paper's rostrocaudal "length" is filed as axial length; the significant regression on carapace length (R2 = 0.61, p = 0.00005) and the left/right null are omitted |
| 4 | Allosergestes pectinatus | eye_diameter_mm | FIXABLE | mixed-preservation confound omitted; note misstates main |
| 5 | Sergia tenuiremis | eye_diameter_mm | FIXABLE | mixed-preservation confound omitted |
| 6 | Phorcosergia grandis | eye_diameter_mm | FIXABLE | mixed-preservation confound omitted; note misstates main |
| 7 | Eusergestes arcticus | eye_diameter_mm | FIXABLE | mixed-preservation confound omitted; note misstates main |
| 8 | Benthosema glaciale | eye_diameter_mm | OK | row, method, fixation and licence verified |

Errors: 5 of 8 (all fixable, 0 unfixable). Error lines: 3, 4, 5, 6, 7. Rate 5/8 = 62.5%.

Answer to the desk's question: a same-DOI record under a different trait is not a repeat of main (audits 139 and 341). Lines 1 and 2 stand.

## Replacement

Each old string occurs exactly once in its line (checked with a Python count on the file as it stands).

Line 3:
- `"trait": "eye_axial_length_mm"` -> `"trait": "eye_diameter_mm"`
- `"units": "mm (mean of 20 eyes; range 16–27.9)"` -> `"units": "mm (rostrocaudal eyeball length, mean of 20 eyes; range 16–27.9)"`
- `Admission dates not printed.` -> `Admission dates not printed. The Mann–Whitney U test found no significant differences between right and left eyes. Linear regression against carapace length was significant for eyeball length (R2 = 0.61; p = 0.00005) and lens diameter (R2 = 0.40; p = 0.00290), so the pooled mean depends on the size mix of the ten turtles (carapace length 25–71.7 cm). The paper uses neither 'axial' nor 'anteroposterior'; its 'length' is the rostrocaudal extent and its 'width' the lateromedial extent of the globe.`
- `Value is the rostrocaudal 'length' of the eyeball filed as axial length (the paper's own term is 'length'); flagged for the auditor.` -> `Value is the rostrocaudal 'length' of the eyeball (the paper's term), filed as eye_diameter_mm because the paper names no axial length (audit 431).`

Lines 4, 5, 6 and 7 (the same string in each):
- ` (preservation of the expedition animals was not read).` -> `; animals from the first expedition (n = 49) were measured after fixation in 4% paraformaldehyde and those from the second expedition (n = 193) fresh, so each species mean mixes fresh, fixed and ethanol-preserved animals in proportions the table does not give. Adding preservation type improved the authors' allometry model (ΔAIC = 30, a significant but small effect), and because preservation type is represented unevenly across species they could neither separate it from species effects nor correct for it.`

Line 4:
- `Genus not on main under any trait.` -> `Allosergestes pectinatus is on main as acuity_cpd (canon-4, Feller et al. 2021); no eye diameter for it on main.`

Line 6:
- `Genus not on main under any trait.` -> `Phorcosergia grandis is on main as cff_hz (oa-6, from the Lafitte et al. 2022 review supplement); no eye diameter for it on main.`

Line 7:
- `Genus not on main under any trait.` -> `Eusergestes arcticus is on main as cff_hz (oa-3 and oa-6, from the Lafitte et al. 2022 review supplement); no eye diameter for it on main.`

## Optional fixes (uncounted)

Lines 1 and 2:
- `"where": "Results (unlabelled text after Methods 'Morphometric analysis', before Fig. 1)"` -> `"where": "Results (opening paragraph, before Fig. 1)"`
- `whether the ± is SD or SE,` -> `whether the ± is SD or SE (the only statistics sentence, under Methods 'Morphometric analysis', gives mean and standard error for the TEM measurements),`
