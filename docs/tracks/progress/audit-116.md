# Audit 116: desk-d26 (2 evidence records; branch origin/research/desk-d26, head f0eb7e00)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so error lines can simply be dropped.
- Evidence records: both lines of docs/views/evidence/desk-d26.jsonl (1 and 2).
- Search records: none (the unit has no searched file).
- Wanted lines: none (the unit has no wanted file).
- Leads the unit left alone: the Erodium cicutarium shade trial, plus three spot-checks from its progress file (Platanus orientalis, Erechtites valerianaefolia, Rivina humilis).

## Gate

The unit has no searched or wanted file, so `screen_candidates.py --check` has nothing to check. Both evidence lines parse as JSON. Quote lengths are 60 and 48 characters. Line 1's note says 59, one short (not counted).

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), audit 39's counting rule, the shared brief's rulings, and audits 90 and 114 as the format. For each record I ran a title WebSearch, fetched only URLs that search returned, and compared authors, year, journal, DOI, quote, value, conditions, grade and the partial flag. I checked names on POWO pages my searches returned. I checked origin/main (386b9ecb) docs/views/evidence and docs/views/searched for every taxon and DOI.

I used 9 WebSearches and about 15 WebFetches. Three pages were blocked and not retried:
- the Frontiers /text page (its public-pages-files-2025 redirect was not answered at the permission step);
- the Frontiers epub (binary);
- a direct curl of the Frontiers PDF (proxy 403).

No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed.

## Evidence verdicts (2)

| Line | Record | Verdict |
|---|---|---|
| 1 | Pyrus betulifolia sense_chemical (Wang, He, Li, Bai, Teng, Hui 2025, Front Plant Sci 16: 1667946, 10.3389/fpls.2025.1667946) | **ok.** I opened the Frontiers PDF. The six authors in order, the year, volume 16, article 1667946 and the DOI all match. "ABA repressed the germination of Pyrus betulaefolia embryos." is the whole first sentence of the Figure 2 legend, word for word. The legend's own (B) sentence gives "100 mM ABA", and Results 2.2 gives "with or without 100 mM ABA supplementation". Methods 4.1 gives 22 ± 2°C, 60–70% RH and a 16-h light/8-h dark cycle, which matches the record's corrected `conditions`.<br><br>**Figure legend quote.** I accept it. The sentence is the authors' own statement of the result, in words. It is no value read off a plot, so the "read from Fig. N" partial rule of oa-read.md does not apply. oa-read.md names figure captions as text to be read. Grade m (one named species, measured in this paper) and no partial flag fit.<br><br>**Dose.** The text the fetch returned holds no μ or µ anywhere. It prints mM for every dose: 100 mM ABA, 10 mM fluridone, 200 mM PAC, 100 mM GA3 or GA4+7, and 0.2 mM luciferin. 100 mM ABA is about 26 g/L. That is implausible for an aqueous germination medium, and 10 mM fluridone is implausible in the same way. I have no fetched source for either solubility; this is my own construction. The likeliest reading is micromolar, either as a misprint or as a μ glyph lost when the PDF text is extracted. I could not tell which, because the HTML and epub were blocked. The record copies the printed unit, marks it "as printed", and says "units doubtful" in `conditions`. That is the treatment audit 114 asked for. Wording to tighten (not counted): the value should say outright "probably μM; do not use as a dose".<br><br>**Trait and name.** Applied ABA on living embryos is a hormone response under 10(d). POWO 730718-1 was returned by my search, and audit 114 had opened it. Main holds Pyrus betulifolia diel (desk-d11:7) and a genus-level Pyrus sense_chemical record (desk-d11:6, another paper), so this line is no repeat. The DOI is on main only as a wanted line (harvest-c11:10), which this record can close. |
| 2 | Diospyros texana sense_light_nonvisual (Everitt 1984, J Range Manage 37(2): 189-192, 10.2307/3898913) | **ok.** I opened the Rangelands Gateway record (dlio/21756). It gives Everitt, J. H., 1984, Journal of Range Management 37(2): 189-192, and DOI 10.2307/3898913. The fetch confirmed that the exact sentence "Seeds germinated equally well in light and dark." is in the abstract. The abstract also gives germination above 90% at constant 20 to 30°C and at alternating 20-30°C, and no dormancy, which supports the value.<br><br>A light/dark germination comparison counts under 10(e), and a null effect is a measured response. Grade m and `partial: true` (abstract only) fit. POWO ipni 323100-1 (opened): "This species is accepted", with no synonyms listed.<br><br>Main holds no Diospyros texana record, and no Diospyros evidence at all. Main's null genus record sweep-15:22 (Diospyros, all four traits, D. texana named in its query) is contradicted for sense_light_nonvisual. That fault is main's and is not counted, as in audit 114. |

Genus status: Pyrus and Diospyros are accepted genera, and each taxon is accepted under its own genus.

Evidence errors: **0 of 2**.

## Leads left alone (checked, not counted)

| Lead | Unit's reason | My check |
|---|---|---|
| Erodium cicutarium shade trial (Dryad 10.5061/dryad.gd3qh, Heger 2017) | the Wiley paper (10.1111/1365-2745.12607) failed to fetch; Dryad sentences run past 125 characters whole | **Reason wrong (fault, not counted).** The Dryad page (opened twice) gives Tina Heger, 2017, with no linked article listed. One whole abstract sentence of 96 characters was confirmed word for word: "Time to first flowering was longer under heterogeneous shading, and plants produced less fruits." Treatments are no shade, homogeneous shade and heterogeneous shade in a glasshouse, on maternal families of E. cicutarium. A set-light-intensity trial counts under sense_light_nonvisual, so the cell could have closed, as m and partial, with the Dryad description as source. Audit 115's follow-up also asked for a wanted line if the article could not be read; the unit wrote none. My title search did not return the Wiley page, so the article's DOI is not checked here. My search also returned Heger, Nikles and Jacobs 2018, AoB Plants 10(1): ply009, 10.1093/aobpla/ply009 (PMC5815068, opened). That paper germinated E. cicutarium in the dark only, with no light treatment, so it cannot close the cell. |
| Platanus orientalis (Carruggio et al., SBI 2019 abstract) | light sentence 141 characters | **Confirmed.** The simaseed.unict.it PDF (opened) is Carruggio, Castrogiovanni, Impelluso and Cristaudo 2019. Its light result, "The presence of light improved germination at 15 and 20°C (near zero germination in full darkness)", comes back only as an excerpt of a longer sentence. Under the 125-character whole-sentence rule the skip stands. A " … " cut would make it usable if the desk allows cuts. |
| Erechtites valerianaefolia (Zayat and Ranal 1997) | photoblastic sentence about 145 characters | **Confirmed.** The Embrapa PAB page (opened) gives Pesq Agropec Bras 32(11): 1205-1213, 10.1590/S1678-3921.pab1997.v32.4770. The conclusion sentence "The seeds of capiçova are positively photoblastic ..." is 144 characters whole, so the skip stands. |
| Rivina humilis (Kumari et al. 2021) | abstract reports no GA3, smoke or KAR1 result for the species | **Partly wrong (fault, not counted).** The sjp.ac.lk page (opened) gives Kumari, Gunadasa, Merritt, Turner and Gama Arachchige, 2021-09-02. It names R. humilis among the tested species and has a whole 67-character sentence: "Smoke water did not improve seed germination of any of the species." That is a measured null smoke response for every species tested, R. humilis included. The GA3 and KAR1 part of the reason holds. Main's null record desk-c8:13 (Rivina sense_chemical) is open to the same lead. |

## Counts

- Search records: 0 of 0.
- Evidence: 0 of 2.
- Unit: 0 of 2, 0%.

Pooled with audits 83 to 90 onward, from audit 115's figures (search records 49 in 1032; with evidence 56 in 1118):
- Search records: 49 in 1032, 4.75% (unchanged).
- With evidence included: 56 in 1120, 5.00%.

**Verdict: pass.** Both evidence lines stand and can merge.

**Error lines to drop:**
- docs/views/evidence/desk-d26.jsonl: none.

Follow-ups:
- Line 1: add "probably μM; do not use as a dose" to the value. Fix the note's character count from 59 to 60.
- Remove the wanted line harvest-c11:10 (10.3389/fpls.2025.1667946) when line 1 lands.
- Reopen main's sweep-15:22 (Diospyros) for sense_light_nonvisual.
- Erodium cicutarium sense_light_nonvisual: Dryad 10.5061/dryad.gd3qh has the 96-character sentence above, so the next lead unit can log it.
- Rivina humilis sense_chemical: the Kumari et al. 2021 smoke sentence is a candidate null record. The sentence is group-wide, so the desk should decide between grade m and g.
