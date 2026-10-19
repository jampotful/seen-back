# Audit 69: harvest-53 (branch research/harvest-53, commit a1f0b153)

Date: 19 October 2026. Auditor worked in the worktree on research/audit-69. Rules: docs/tracks/prompts/desk-audit.md and desk-screen.md (points 8 and 9, audit 52's settlement of the light-trap rule, sweep-56#5 for pupil_shape).

## Gate
`screen_candidates.py --check` on the unit's 55 search records and 10 wanted lines: 0 problems.

## Sample (random.seed(69), 20 of 55 record lines, in file order)
3, 5, 7, 11, 21, 23, 27, 28, 29, 30, 34, 36, 37, 38, 39, 41, 44, 46, 47, 52

## Verdicts
For every record the harvest queries repeat `harvest_get.py` word for word (the family review is the harvest's own last query line, and each record carries it), the `chased` text matches the harvest header (no measured relative, or a citation step that found 0 works), the canon compilations of the trait are named, and the screened entries hold no measurement.

| Line | Record | Verdict | Reason |
|---|---|---|---|
| 3 | Nannotrigona cff_hz | pass | Haarlem 2026 and Inger 2014 named; my searches (stingless bee flicker fusion) found only fly and Lepidoptera flicker work. |
| 5 | Nannotrigona lambda_max_nm | pass | Mascaro et al. 1994 (repositorio.usp.br/item/000884920) lists Nannotrigona testaceicornis among its 12 species, but gives UV 340, blue 449, green 524 nm only as means over the 12; main's sweep-79:3 precedent logs no wavelength from it, and the unit put the abstract on its wanted list. |
| 7 | Melanotis interreceptor_deg | pass | Searches on the blue mockingbird and mimid retina found no cone spacing or acuity; Caves 2023 and Martin 2017 named. |
| 11 | Amphion cff_hz | pass | Searches (nessus sphinx flicker; Amphion lamp comparison) found no sphingid flicker value for the genus. |
| 21 | Cyclophora corner_hz | pass | No corner frequency found; Frolov and Ignatova 2019 named. See the moth finding below on spectral_range_nm. |
| 23 | Polystepha interommatidial_deg | pass | Gall midge eye searches returned only generic compound-eye optics papers; Land 1997 named. |
| 27 | Phoeniconaias interreceptor_deg | pass | Lisney et al. 2020 covers Phoenicopterus ruber and P. chilensis (Montpellier record), not P. minor; Martin 2005 is a field study, wanted for fov_h_deg. |
| 28 | Phoeniconaias cff_hz | pass | Haarlem 2026, Healy 2013, Inger 2014 named; flamingo flicker search returned nothing for the family. |
| 29 | Phoeniconaias lambda_max_nm | pass | Ödeen and Håstad 2003 and 2013, Hunt 2009 and the other canon compilations named; Ödeen, Hart and Håstad 2009 (16 SWS1 sequences) names no flamingo on its page and is already on main's wanted list (web-birds). |
| 30 | Phoeniconaias spectral_range_nm | pass | As line 29; no light-trap table applies to a bird. |
| 34 | Apodemia corner_hz | pass | Searches found no riodinid flicker; Frolov and Ignatova 2019 named. |
| 36 | Megapodius interreceptor_deg | pass | Retina and ganglion-cell searches found no megapode topography; Caves 2023 named. |
| 37 | Megapodius fov_h_deg | pass | Martin 2007 and Tyrrell and Fernández-Juricic named; no megapode visual field in my searches. |
| 38 | Megapodius binocular_deg | pass | Same as line 37. |
| 39 | Megapodius cff_hz | pass | Haarlem 2026, Healy 2013 named; the hen flicker papers are Gallus. Umeton, Read and Rowe 2017 stays a lead (below). |
| 41 | Megapodius spectral_range_nm | pass | Opsin and spectral searches returned only Toomey 2016 and other canon work. |
| 44 | Uraeginthus fov_h_deg | pass | Only the zebra finch fields exist; Bennett et al. 2000 is a lead for spectral traits, which the unit left unrecorded. |
| 46 | Uraeginthus cff_hz | pass | Screened song-frequency papers hold no flicker; Umeton 2017 is a lead. |
| 47 | Nephrotoma acuity_cpd | pass | Four screened works are microscopy, trapping and chromophore chemistry; my crane fly searches found no Nephrotoma eye measurement. |
| 52 | Calonectris binocular_deg | pass | Lucas et al. 2024 holds two shearwaters (Ardenna pacifica, Puffinus bailloni) and no Calonectris, as main's rows show; Heswall et al. 2026 (ocular media of eight seabirds) has no Calonectris; Goller et al. 2018 studies cowbirds. |

## Count
Errors in the sample: 0 of 20 (0%). The desk's pooled figure before this audit was 4 errors in 517 records; pooled with this sample it is 4 in 537 (0.7%). Under 5%: the unit passes.

## Faults and findings not counted
1. The Equus claim is wrong. The unit wrote no Equus record because "main holds its pupil rows". Main holds pupil rows for E. caballus, E. ferus, E. africanus, E. quagga (filed as "quaga"), E. zebra and E. hemionus (corrected/squirrel-deer-rabbit:151, oa-2), but none for E. asinus, E. grevyi or E. kiang, which the queue still lists as open pupil_shape cells (closest = genus, "members disagree"). gbif-names.tsv gives no synonym that would cover them. Equus asinus: Zayed, Aly, Ibrahim and Kotb 2012, "Comparative morphology of the iris of donkey (Equus asinus) and buffalo", Journal of Veterinary Anatomy (journals.ekb.eg/article_44885.html), states "In donkeys the breadth of the iris is nearly uniform encircling a semicircular pupil". Not on main. I count it as a unit-level omission rather than a record error, since no record exists to be wrong. It would add one error if the owner counts the missing record, which gives 1 in 21 here and 5 in 538 pooled (0.9%), still under 5%.
2. The moth claim is wrong for Cyclophora. Nowinszky et al. 2022 (canon-22, intechopen.com/chapters/80625) lists Cyclophora annularia (row 59), C. ruficiliaria (60), C. punctaria (61) and C. linearia (62) in its visible against black-light table, so spectral_range_nm for Cyclophora is already covered by that table under point 9. The table lists no Panthea, Amphion or Datana (checked against the page text). The unit wrote no spectral_range_nm record for any moth genus, so no record is wrong.
3. Wanted lines: Martin, Jarrett, Tovey and White 2005 (Naturwissenschaften 92:351, doi 10.1007/s00114-005-0010-0) matches the line's DOI and year, and the line's authors field is empty; Mascaro, Schorn, Souza and Ventura 1994 is the authorship of the "Spectral input systems of brazilian bees" line, which also stays empty. "UVS is rare in seabirds" is Machovsky-Capuska, Huynen, Lambert and Raubenheimer 2011, Vision Research 51(12), with 16 seabird species of which the page names three (the DOI was not on the page I opened). Not verified: the DOIs of the Animals 2023 blinking paper, the JEB 2024 seabird light paper, Chen and Goldsmith's cone paper (year 0 on the line) and the Simon Fraser flicker piece (year 0).

## Leads (species lists unseen, outside canon.jsonl)
- Mascaro et al. 1994 (repositorio.usp.br/item/000884920): 12 stingless bees including Nannotrigona testaceicornis, three receptor types in all. Bears on Nannotrigona receptor_classes and colour_vision (already wanted) and, by main's precedent, not on lambda_max_nm (record 5).
- Umeton, Read and Rowe 2017 (Newcastle ePrints 232781, already audit-64 on the wanted list): table of flicker values by species; bears on records 28, 39 and 46 (Phoeniconaias, Megapodius, Uraeginthus cff_hz).
- Bennett, Hunt, Cuthill and Partridge 2000, "UV vision and mate choice in Estrildid finches from Africa, Asia and Australia" (workshop paper, Bristol record): species not shown; could bear on Uraeginthus spectral traits.
- Machovsky-Capuska et al. 2011 (16 seabirds, 13 unnamed): could bear on Calonectris lambda_max_nm and spectral_range_nm (the unit lists it as wanted).
- Eur. J. Entomol. 119:36-42 (2022) and Infusino et al. 2017 (699 moth species, UV LED against other lamps; already audit-63), and an Estonian thesis on moth catches by light source (dspace.emu.ee): lamp comparisons with unseen species lists; they bear on spectral_range_nm of any moth genus, Cyclophora first.

## Searches
About 40 WebSearch calls and 14 WebFetch calls, all on URLs my searches returned; no library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. All 20 sampled records finished.
