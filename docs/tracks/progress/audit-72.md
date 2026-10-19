# Audit 72: harvest-55 (branch research/harvest-55, commit 0d19dd51)

Gate: `screen_candidates.py --check` on the 42 records and 6 wanted lines prints "0 problems".

## Sample (seed 72, 20 of 42 lines)

Line numbers (1-based): 1, 5, 8, 9, 12, 15, 20, 21, 22, 23, 24, 25, 26, 29, 32, 33, 35, 39, 41, 42.

## Method

For every sampled record I ran `harvest_get.py` for the genus and compared `queries` word for word (all 20 match, family review included), checked every `screened` id against the harvest output and `screen_candidates.py` (W3161012301 and W30486556 come from the latter), read `chased`, and compared `canon` with docs/views/research/canon.jsonl by trait and taxon. Main's rows were searched in docs/views/audit/corrected and docs/views/evidence under Rawlinsonia, Chlorohyla, Litoria (ewingii, gracilenta), Prionoxystus, Cossus, Lyrurus, Tetrao, Trichopoda, Thecadactylus, Gekko rapicauda, Trigona, Tetragonula, Nisaetus, Spizaetus, Surnia, Cinclodes, Lophonetta, Anas specularioides, Terathopius, Quelea and Echthromorpha. About 45 WebSearches and 25 fetches of returned URLs were used (no library proxy, ResearchGate or academia.edu page was opened; one academia.edu result was left unopened).

## Verdicts

| Line | Record | Verdict |
|---|---|---|
| 1 | Rawlinsonia acuity_cpd | ok. Litoria searched in the web pair. Main holds Litoria ewingii pupil_shape (oa-2:1815, Banks et al. 2015) and no acuity row. My frog-acuity search found nothing. |
| 5 | Trigona acuity_cpd; interommatidial_deg | ok, with a lead (below). Tetragonula rows correctly kept apart. Streinzer et al. 2016 (10.1007/s00359-016-1118-8) is on main for T. fulviventris absolute_sensitivity only. |
| 8 | Thecadactylus acuity_cpd; fovea | ok. Own searches (retina, fovea, acuity) found no Thecadactylus value. Griffing et al. 2026 (Aristelliger, not Thecadactylus) and Tansley 1959 (Hemidactylus, Tarentola) are other genera. |
| 9 | Thecadactylus fov_h_deg | ok. No visual-field value found. |
| 12 | Quelea cff_hz | ok. Haarlem 2026 named. Own searches found no quelea flicker value. |
| 15 | Nisaetus cff_hz | ok. Spizaetus searched; main's only Spizaetus row is hearing. |
| 20 | Chlorohyla cff_hz | ok. Litoria searched; Inger 2014 and Healy 2013 named (Haarlem excludes Amphibia). |
| 21 | Chlorohyla fov_h_deg | ok. No Litoria visual-field value found. |
| 22 | Chlorohyla motion | ok. |
| 23 | Echthromorpha acuity_cpd; interommatidial_deg | ok. Own searches (ichneumonid eye, Echthromorpha eye) found no ichneumonid angle. |
| 24 | Echthromorpha cff_hz; corner_hz | ok. Haarlem 2026 and Frolov and Ignatova 2019 named. |
| 25 | Echthromorpha colour_vision; lambda_max_nm; receptor_classes; spectral_range_nm | ok. Nine canon compilations named, Peitsch 1992 and Briscoe and Chittka 2001 among them. |
| 26 | Cinclodes acuity_cpd; interreceptor_deg | ok. Own searches found no furnariid value. |
| 29 | Cinclodes lambda_max_nm; spectral_range_nm | ok. Twelve avian compilations named. Casalia et al. 2021 (cardinals and tanagers) and the great bowerbird SWS1 paper do not include Cinclodes. |
| 32 | Surnia interreceptor_deg | ok. Lisney et al. 2012 (Brain Behav Evol, owl retinal topography) includes Surnia ulula (peak ganglion-cell density and a fovea) but reports ganglion cells, not receptor spacing; a lead for any fovea cell (below). |
| 33 | Surnia lambda_max_nm; spectral_range_nm | ok. Own search found only SWS1 compilations. |
| 35 | Trichopoda cff_hz; corner_hz | ok. Laughlin and Weckstrom 1993 named. Own search found a hover fly (Volucella) paper, no tachinid. |
| 39 | Lophonetta lambda_max_nm; spectral_range_nm | ok. Anas specularioides searched. Own search found nothing for the crested duck. |
| 41 | Terathopius fov_h_deg | ok. Own search found nothing for the bateleur. |
| 42 | Terathopius cff_hz | ok. |

Sample: 0 errors in 20.

## Specific tests set in the launch prompt

- Prionoxystus and point 9: the unit wrote no spectral_range_nm record for Prionoxystus (record 18 covers cff_hz and corner_hz only). Its claim that a lamp-comparison table lists no Prionoxystus holds on my reading of Table 1 of Nowinszky et al. 2022 (IntechOpen chapter 80625, summarised by the fetch tool: families Drepanidae, Lasiocampidae, Saturniidae, Sphingidae, Geometridae, Notodontidae, Erebidae, Noctuidae, Nolidae; no Cossidae, no Prionoxystus, no Calephelis). The summary came from a fetch model, so the table itself still deserves a read when logged.
- Prionoxystus and Calephelis acuity and interommatidial cells wait on the Chan et al. 2024 wanted line. Not sampled.
- Chlorohyla and Rawlinsonia: queries use the right animals (Litoria gracilenta, Litoria ewingii, dainty green tree frog, Ewing's tree frog). Main files both under Litoria; their pupil_shape cells are held (almond/slit, horizontally elongate; Banks et al. 2015, oa-2:1815 and 1820). The unit wrote no pupil_shape record for either.
- Lyrurus (lines 16, 17, not sampled) searched black grouse and Tetrao tetrix; the animal is right, and the queue's wader view is a view assignment (Phasianidae), not a search fault.
- Thecadactylus pupil_shape: no record in the unit and no main row. The Reptiles of Ecuador wanted line is reasonable. A University of the West Indies fact sheet (sta.uwi.edu, ogatt, Thecadactylus rapicauda) states "The pupils are elliptical in shape and vertical", citing Wikipedia; a secondary source, offered as a second lead.
- Genus splits (Xenochrophis/Fowlea pattern): no sampled genus has main rows under another name that the note denies. Trigona/Tetragonula is stated correctly in the record.

## Rate

- Sample: 0/20 = 0%. No error, so no extension.
- Pooled with audits 43 to 51 and 55 to 71 (7 in 607): 7/627 = 1.1%.
- Verdict: the unit passes.

## Leads (compilations or papers whose species lists I could not see)

- Streinzer, Huber and Spaethe 2016 (Trigona fulviventris, Table 1 with elided columns): the text says facet diameter is tabulated per species and that Δφ was estimated for the species from facet number; the table was not readable (PMC behind a browser check). Bears on line 5 (and line 6's sibling cells not sampled). Main holds the paper but logged absolute_sensitivity only. Uncounted because the Δφ is an estimate and I could not see the table.
- Lisney et al. 2012 (Surnia ulula fovea and ganglion-cell density): bears on line 32 only if a fovea or ganglion-cell trait is opened.
- Odeen and Hastad 2003, 2013, Odeen, Hastad and Alstrom 2011, Hunt et al. 2009: species lists unseen; bear on lines 29, 33, 39 (Cinclodes, Surnia, Lophonetta). Banks et al. 2015 bears on the Thecadactylus, Rawlinsonia, Chlorohyla pupil cells (frogs only).
- Tyrrell and Fernandez-Juricic 2017 S1 and Martin 2007: unseen species lists; bear on Terathopius and Nisaetus binocular_deg and field cells (lines 14, 37 and 41 area).
- Nowinszky et al. 2022: read through a summary only (above).

## Wanted lines (faults listed, not counted)

- Line 3 (Quelea, 10.1007/s00359-020-01404-y): the page is Lawson and Srinivasan 2020, contrast sensitivity and visual acuity of Queensland fruit flies; it does not involve Quelea. Drop the line.
- Lines 1, 2 and 4 (Chan et al. 2024 preprint, Potier et al. 2026, Karger 000329257): not checked; my fetches of doi.org/10.1242/jeb.250727 and the Karger PDF were blocked pending permission.
- Line 5 (reptilesofecuador) and line 6 (PubMed 19757966) not opened.
