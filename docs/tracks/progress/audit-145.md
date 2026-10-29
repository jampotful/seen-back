# Audit 145: desk-d55 (29 October 2026)

Unit: desk-d55, branch origin/research/desk-d55. Files: docs/views/evidence/desk-d55.jsonl (9 lines) and docs/tracks/progress/desk-d55.md. The unit has no searched or wanted file, so the mechanical gate and the search-record draw have nothing to run on; all 9 evidence lines were judged. The branch adds no other file (no stray file). No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed. Quotes were checked against pages my own searches returned or the record's open-access URL, asking the fetch tool whether the exact sentence is present and what opens it; lengths were counted with Python on the record's string. I used 15 WebSearches. One fetch was blocked (frontiersin.org /full page, permission not answered) and one returned a captcha (pmc.ncbi.nlm.nih.gov PMC8329535); the Frontiers text and PDF pages were read instead.

Rulings applied (launch prompt and brief): one whole sentence of at most 125 characters, verbatim, giving the study's own result with a direction or magnitude, not a Background statement; POWO synonyms and hybrids are errors (every epithet checked; no variety or subspecies is filed); pooled grade g must name the group the source measured; a record repeating main (paper, quote, species and trait) is an error; genus-level filing when a species is named is an error; mis-copied dose units are errors; cut twigs and branches excluded; a field gradient or correlation is not a set-light trial; plant diel = flower opening and scent timing; sense_chemical = living responses and volatile signalling; set-light, shade, photoperiod, UV, night-light and germination light/dark trials count under sense_light_nonvisual.

## Main

None of the sources (10.7717/peerj.12698, 10.3389/fpls.2021.695867, the Acta Amazonica 43(3) PDF v43n3a04, 10.1590/S1516-89132003000200011, the phytojournal 8-5-63-555 PDF, 10.5433/1679-0359.2012v33n3p867, the Redalyc 48825247015 PDF) appears in any evidence file on main. Main holds Spirodela polyrhiza (desk-d53, Appenroth 2003 turions), Pinus sylvestris (canon-3, desk-d22, oa-2; the sense_chemical one is 10.1007/s10886-016-0790-z) and Rhizophora mangle (sweep-40, R:FR) from other papers; main holds no Elodea naias / Egeria najas record (audit 143 dropped desk-d53's). No record repeats or contradicts main.

## Evidence verdicts (9)

| line | taxon / trait | verdict | reason |
|---|---|---|---|
| 1 | Lemna minor / sense_light_nonvisual | ok | PeerJ page (opened twice): sentence verbatim, 122 characters, whole, direction and magnitude (both fastest at 236 µmol m–2 s–1; unit copied exactly). Three set light intensities in the laboratory, a set-light trial. Pooled grade g names both species the source measured (title and sentence name Lemna minor and Spirodela polyrhiza). Authors Małgorzata Strzałek and Lech Kufel (PeerJ PDF, opened), PeerJ 9: e12698, 2021, DOI agree. POWO 526194-1 (opened): Lemna minor L., "This species is accepted". |
| 2 | Spirodela polyrhiza / sense_light_nonvisual | ok | Same source and quote, grade g as line 1. POWO 526214-1 (opened): Lemna polyrhiza L. "is a synonym of Spirodela polyrhiza", confirming the species name accepted. Distinct from main's Appenroth 2003 photoperiod record (different paper and quote). |
| 3 | Pinus sylvestris / sense_chemical | **error** | Quote is not the whole sentence. Frontiers text page and journal PDF (both opened) print "On the other hand, MeJA significantly slowed down seedling growth relative to control and all other induction treatments." The record drops "On the other hand," (the whole sentence is 121 characters, so it could have been copied whole). Otherwise sound: potted living seedlings in a greenhouse (methods), applied hormone; abstract gives "10 mM or 15 mM", matching the note; five authors, 2021, DOI agree; POWO 263353-1 (opened): Pinus sylvestris L., "This species is accepted." |
| 4 | Avicennia germinans / sense_light_nonvisual | ok | Acta Amazonica PDF (opened): English abstract sentence verbatim, 69 characters, whole, direction given. Full sun, 30% and 60% shading for nine months, a set shade trial. Five authors, 2013, 43(3): 291-296, no DOI printed, as the record has it. POWO 861125-1 (opened): Avicennia germinans (L.) L., "This species is accepted". |
| 5 | Rhizophora mangle / sense_light_nonvisual | **error** | Sentence verbatim, 62 characters, whole, but it reports no direction or magnitude: "Growth of seedlings of R. mangle occurred at all light levels." says growth happened, not that it rose, fell or did not differ across shade levels, so it is neither a directional result nor a stated null (the note's "measured null" is the desk's reading). Source, trial and name otherwise sound: POWO 30061148-2 (opened): Rhizophora mangle L., "This species is accepted". See fork. |
| 6 | Elodea naias / sense_light_nonvisual | ok (note) | SciELO abstract page (opened): sentence verbatim, 116 characters, whole, direction given ("stimulated"). Laboratory irradiances 0-124 µM m-2 s-1 PAR, a set-light trial. Character check: the value and quote carry no number or unit, so nothing can be mis-copied; the source's own unit is "µM m-2 s-1" (the unit that sank desk-d53's line) and the record does not reproduce it. Tavechio and Thomaz, 2003, 46(2): 203-209 agree (DOAJ, opened). Name: WFO wfo-0000770760-2025-06 (opened) accepts Elodea naias (Planch.) Casp. with Egeria najas Planch. a synonym; POWO 19696-1 (opened) says Egeria "is a synonym of Elodea", and the FWS 2025 screening (opened) cites POWO 2024 as listing "Elodea najas", an orthographic variant of the same name. Not a POWO synonym. |
| 7 | Cassia fistula / diel | ok | Journal PDF (opened): sentence verbatim, 86 characters, whole, in the abstract, a clock-time magnitude. Flowers observed on five tagged standing trees in the field, not picked flowers, so it is a flower-opening measurement. Konyak and Wani 2019, J Pharmacogn Phytochem 8(5): 1432-1435, no DOI printed, agree. POWO 484507-1 (opened): Cassia fistula L., "This species is accepted" (not moved to another genus). |
| 8 | Euphorbia heterophylla / sense_light_nonvisual | ok (note) | Redalyc PDF (opened): sentence verbatim, 100 characters, whole (a line break inside "E. heterophylla"), a measured null. Constant light, constant dark, alternation, red and far red, a germination light/dark trial. The value's "83 to 97%" is the abstract's figure. Four authors, Semina 33(3): 867-872, 2012, DOI agree. POWO 30062970-2 (opened, independently of the unit's WFO check): Euphorbia heterophylla L., "This species is accepted". |
| 9 | Bidens gardneri / sense_light_nonvisual | ok (note) | Redalyc PDF (opened): sentence verbatim, 120 characters, whole, a result (very-low-fluence response); "These achenes" are the medium newly collected achenes of the preceding sentence. Laboratory Petri-dish tests under a set white-light gradient 0 to 46.44 µmol m-2 s-1 and green light, a set-light trial, not a field gradient; the value's long and medium achenes rising with irradiance matches the abstract. Rondon, Takaki, Zaidan 2012, Rev Árvore 36(6): 1145-1153, no DOI printed, agree. Name: no POWO page opened (184923-1 client error); Wikipedia's list of Bidens species (opened) includes Bidens gardneri Baker among species POWO accepted as of November 2024, and floraoftheworld.org (opened) labels it Accepted. Accepted on secondary evidence; POWO itself unconfirmed. |

Epithets and varieties: no record carries a variety, subspecies or hybrid; none is filed at genus rank where a species is named. Explicit checks: Lemna minor, Spirodela polyrhiza, Pinus sylvestris, Avicennia germinans, Rhizophora mangle, Cassia fistula, Euphorbia heterophylla (POWO pages opened); Elodea naias (WFO opened, POWO genus page and an agency report citing POWO); Bidens gardneri (secondary pages citing POWO, POWO page not opened).

Evidence errors: **2 of 9 (22%)**, lines 3 and 5.

## Fork (owner to decide)

- Line 5: if the owner reads "growth occurred at all light levels" as a measured null (shade tolerance), line 5 stands and the unit has 1 error in 9 (11%), still a fail.

## Notes for the desk (not counted)

- Line 3: repair by quoting the whole sentence with "On the other hand," (121 characters).
- Line 6: the DOI is built from the SciELO PID S1516-89132003000200011; neither the abstract page, article page nor DOAJ record I opened prints it. POWO spells the epithet najas, WFO naias.
- Line 6: "apical shoots grown 10 days" and "lamps and shade fabrics" in `method` are not in the abstract.
- Line 8: the abstract's 83 to 97% does not match the Table 1 means (77 to 88%) in the same PDF.
- Line 9: the note's floraoftheworld.org status badge is GBIF-sourced, not POWO-sourced.

## Counts and verdict

- Evidence: 2 errors in 9, 22%.
- Search records: none in the unit.
- Pooled with audits 83 to 90 (the pool as carried by audit 144: 53 in 1151 overall, 48 in 1026 search records): overall 55 in 1160, 4.7%; search records unchanged at 48 in 1026, 4.7%.
- **Verdict: fail** (22%, over 5%). Drop or repair lines 3 and 5; the other seven lines stand.

## Error lines

- docs/views/evidence/desk-d55.jsonl: 3, 5
- docs/views/searched/desk-d55.jsonl: no file
- docs/views/wanted/desk-d55.jsonl: no file

## Blocked pages

- frontiersin.org/journals/plant-science/articles/10.3389/fpls.2021.695867/full (permission not answered); pmc.ncbi.nlm.nih.gov PMC8329535 (captcha); powo 184923-1, 526259-1, 12238-2 (client error).
