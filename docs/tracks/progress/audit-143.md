# Audit 143: desk-d53 (29 October 2026)

Unit: desk-d53, branch origin/research/desk-d53 (head d1df5fca). Files: docs/views/evidence/desk-d53.jsonl (8 lines) and docs/tracks/progress/desk-d53.md. The unit is a lead-reading unit with no searched or wanted file, so the mechanical gate and the search-record draw have nothing to run on; all 8 evidence lines were judged. The branch adds no other file (no stray file). No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed. Quotes were checked against pages my own fetches returned, asking the fetch tool whether the exact sentence is present; lengths were counted with Python on the record's string. I used 10 WebSearches.

Rulings applied (launch prompt and brief): one whole sentence of at most 125 characters, verbatim, giving the study's own result with a direction or magnitude, not a Background statement; POWO synonyms and hybrids are errors (every epithet checked; no variety or subspecies is filed); a record repeating main (paper, quote, species and trait) is an error; genus-level filing when a species is named is an error; mis-copied dose units are errors; cut twigs and branches excluded; a field gradient or correlation is not a set-light trial; plant diel = flower opening and scent timing; sense_chemical = living responses and volatile signalling (hormone, elicitor and herbivore-induced responses count; no extracts, oils, processed tissue, nutrient-ion uptake); set-light, shade, photoperiod, UV, night-light and germination light/dark trials count under sense_light_nonvisual.

## Main

None of the three DOIs (10.1007/s00425-023-04075-6, 10.1590/S1516-89132003000200011) nor the Exeter thesis, the Dicksonia, Polypodium or Appenroth papers appears in any evidence file on main. Main holds no evidence for Lotus pedunculatus, Dicksonia, Pleopeltis pleopeltifolia (only Pleopeltis furfuracea, oa-9), Elodea naias or Egeria, or Spirodela polyrhiza. Solanum tuberosum on main is sense_light_nonvisual (10.1017/wet.2026.10096) and sense_thermal (10.1016/j.xplc.2026.101848) only, so line 1's sense_chemical is new. Oenothera biennis on main is diel only (Graham, sweep-10 and recheck-quotes-3-fixed), so line 2's light trait is new.

## Evidence verdicts (8)

| line | taxon / trait | verdict | reason |
|---|---|---|---|
| 1 | Solanum tuberosum / sense_chemical | ok | UniNE Libra record (opened): sentence verbatim, 100 characters, a measured null on VOC composition of living herbivore-damaged emitters (Spodoptera exigua at none, low, high load); volatile signalling of living plants, not extracts or tuber processing. Seven authors, Planta 257(2), 2023, DOI agree. colplanta 2909763-4 (Kew data, opened): S. tuberosum var. album "is a synonym of Solanum tuberosum", so the species is the accepted name (POWO's own form pages returned client errors). |
| 2 | Oenothera biennis / sense_light_nonvisual | ok (note) | Exeter ORE record (opened): sentence verbatim, 120 characters, whole, direction given ("hastened"). It is a measurement of the named species under imposed ALAN treatment (cool white LED extending photoperiod), not a field gradient. Anic Thomas V, PhD thesis 2021, title agree; no DOI. POWO 172755-2 (opened): accepted. See note on `method`. |
| 3 | Lotus pedunculatus / sense_light_nonvisual | ok | Same record: sentence verbatim, 107 characters, whole, direction given; five-year mesocosm experiment with simulated LPS and cool white LED street lighting, an imposed treatment. POWO 503822-1 (opened): Lotus pedunculatus Cav., "This species is accepted." |
| 4 | Dicksonia sellowiana / sense_light_nonvisual | ok | SciELO page (opened): sentence verbatim, 113 characters; white light 616 lux, red light 194 lux, foil dark controls (no germination in darkness), all as the record says. Authors printed "Fiilippini", Duz, Randi; 1999; the search listing places it in Rev Bras Bot 1999 v22n1; no DOI printed. POWO 275823-2 (opened): Dicksonia sellowiana (C.Presl) Hook., "This species is accepted"; WFO 0001112345 (opened) agrees. |
| 5 | Pleopeltis pleopeltifolia / sense_light_nonvisual | ok | SciELO English abstract (opened): "Red light (short treatments) promoted germination." verbatim, 50 characters, whole, direction given; living spores, germination light trial. Felippe, Sassaki, Aveiro 1992; issue listing 1992 v6n1; no DOI. WFO 0001119519-2025-06 (opened): accepted, Polypodium pleopeltifolium Raddi its synonym. POWO pages (202105-2 and colplanta mirror) were blocked, so the name rests on WFO, as audits 141 and 142 allowed. |
| 6 | Pleopeltis pleopeltifolia / sense_chemical | ok | Same page: sentence verbatim, 76 characters, whole, directions given; applied auxin, gibberellin, ethylene-releaser and ABA on living spores (10(d)). |
| 7 | Elodea naias / sense_light_nonvisual | **error: unit mis-copied** | SciELO page (opened): sentence verbatim, 116 characters; Tavechio and Thomaz, Braz Arch Biol Technol 46(2): 203-209, 2003, DOI agree; set irradiance with lamps and shade fabric is a set-light trial. Name: WFO 0000770760-2025-06 (opened) accepts Elodea naias (Planch.) Casp. with Egeria najas Planch. its synonym; POWO 19696-1 (opened) sinks Egeria into Elodea. But the `value` gives "irradiance 0 to 124 umol m-2 s-1 PAR as printed", and the page prints "0-124 µM m-2 s-1 PAR" in the abstract and every Methods instance and never prints µmol. The treatment unit is altered and then labelled "as printed", the reverse of what audit 114 asked (copy the printed unit and mark it doubtful); the note's correct "uM" contradicts the value. |
| 8 | Spirodela polyrhiza / sense_light_nonvisual | ok | AGRIS record (opened): sentence verbatim, 77 characters, whole, a null under 8, 16 and 24 h photoperiods on eight clones in two media; J Plant Physiol 160(11): 1329-1334, 2003, title printed "photoperiodoc". AGRIS names no author; the OUCI reference list (opened) gives "Appenroth", J Plant Physiol 160, 1329, as the record has it. POWO 526250-1 (opened): accepted. |

Epithets and varieties: no record carries a variety, subspecies or hybrid; none is filed at genus rank where a species is named; the two papers that use synonyms (Polypodium pleopeltifolium, Egeria najas) are filed under the accepted names. Explicit checks: Solanum tuberosum (colplanta/Kew), Oenothera biennis, Lotus pedunculatus, Dicksonia sellowiana, Spirodela polyrhiza (POWO), Pleopeltis pleopeltifolia and Elodea naias (WFO, with POWO's genus page for Elodea).

Evidence errors: **1 of 8 (12.5%)**, line 7.

## Notes for the desk (not counted)

- Line 7 fork: if the desk reads the umol conversion as a fair correction of a misprint (the trait value is categorical and the response is right), evidence is 0 of 8. Repair: write "0 to 124 µM m-2 s-1 PAR as printed (probably µmol)".
- Line 2: `method` says the wildflowers were "grown a year in field conditions", and `conditions` says "field experiment". The abstract gives field conditions only for the six-species height result and does not say which experiment the Oenothera flowering result came from. The value stands; the two fields should say "experiment type not stated in the abstract".
- Line 5: "positively photoblastic" is not in the English abstract (which says light-sensitive, with some germination in darkness); line 6's "germinated under white light" is not stated in the English abstract either. Wording only.
- Line 8: J Plant Physiol papers of 2003 normally carry a DOI; the record leaves it empty because neither page printed one, which is right under the never-from-memory rule.

## Counts and verdict

- Evidence: 1 error in 8, 12.5%.
- Search records: none in the unit.
- Pooled with audits 83 to 90 (the pool as carried by audit 142: 52 in 1135 overall, 48 in 1026 search records): overall 53 in 1143, 4.6%; search records unchanged at 48 in 1026, 4.7%.
- **Verdict: fail** on evidence (12.5%, above 5%), on one line. The whole unit was judged, so drop or repair line 7 and the other seven records stand.

## Error lines

- docs/views/evidence/desk-d53.jsonl: line 7 (Elodea naias, irradiance unit mis-copied as "umol ... as printed" where the source prints µM)
- docs/views/searched/desk-d53.jsonl: no file
- docs/views/wanted/desk-d53.jsonl: no file

## Blocked pages

- powo.science.kew.org urn 285307-2 and 17347330-1 (client error); powo.science.kew.org urn 202105-2 and colplanta 202105-2 (permission not answered; WFO served Pleopeltis pleopeltifolia); biolib.cz (bot check).
