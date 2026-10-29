# Audit 147: desk-d57 (29 October 2026)

Unit: desk-d57, branch origin/research/desk-d57. Files: docs/views/evidence/desk-d57.jsonl (9 lines) and docs/tracks/progress/desk-d57.md. The unit has no searched or wanted file, so the mechanical gate and the search-record draw have nothing to run on; all 9 evidence lines were judged. **Stray file:** the branch also adds docs/views/evidence/-h.jsonl, an empty (0-byte) file, apparently left by a mistyped command; it should not be merged. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed. Quotes were checked against pages my own searches returned, asking the fetch tool whether the exact sentence is present, what precedes it and how symbols are printed; lengths were counted with Python on the record's string. I used 22 WebSearches.

Rulings applied (launch prompt and brief): one whole sentence of at most 125 characters, verbatim from its first word, giving the study's own result with a direction or magnitude, not a Background statement; numbers and units compared character by character; POWO synonyms and hybrids are errors; a record repeating main (paper, quote, species and trait) is an error; genus-level filing when a species is named is an error; cut twigs and branches excluded; a field gradient or correlation is not a set-light trial; plant diel = flower opening and scent timing; sense_chemical = living responses and volatile signalling (hormone, elicitor, herbivore-induced responses count; no extracts, oils, processed tissue); set-light, shade, photoperiod, UV, night-light and germination light/dark trials count under sense_light_nonvisual. Where an authority page could not be opened the name is reported as unconfirmed, apart from content errors.

## Main

None of the nine sources (10.1017/S0960258500003810, 10.3390/agronomy12102488, 10.1007/s10886-006-9146-4, 10.1139/b90-264, the SciELO Synedrella paper, 10.1614/WS-07-156.1, 10.1016/S1011-1344(97)00064-X, 10.1111/j.1744-7348.1990.tb04826.x, 10.1139/b94-098) appears in any evidence file on main (four DOIs sit only in wanted files and wanted-merged.csv, which is where the leads came from). Main holds no evidence record for Cirsium vulgare, Vicia villosa, Conium maculatum, Synedrella nodiflora, Tripleurospermum inodorum / Matricaria inodora or Potentilla recta. Main's Aesculus hippocastanum mentions are not sense_chemical evidence for this paper. Main's Hesperis matronalis evidence is a diel scent record (Majetic et al.), a different paper and trait. Main's Oenothera biennis evidence is the d53 night-light flowering record ("Seeing the light", quote "Flowering in Oenothera biennis was also hastened by artificial nighttime lighting...") and two diel Graham records; line 9 is a different paper (Baskin and Baskin 1994), a different quote and a germination light/dark trial, so it neither repeats nor contradicts main.

## Evidence verdicts (9)

| line | taxon / trait | verdict | reason |
|---|---|---|---|
| 1 | Cirsium vulgare / sense_light_nonvisual | ok | Cambridge abstract page (opened): sentence verbatim from its first word "However,", 94 characters, whole, direction (darkness-overwintered seeds required light). Doucet and Cavers, Seed Sci Res 7(4): 399-408, 1997, DOI agree. Germination light/dark trial. POWO 196191-1 (opened): Cirsium vulgare (Savi) Ten., "This species is accepted". |
| 2 | Vicia villosa / sense_light_nonvisual | ok | DOAJ record (opened): sentence verbatim, 62 characters, whole, curly apostrophe as printed; a measured null (light not necessary). Yang et al., Agronomy 12(10): 2488, October 2022, DOI agree. POWO 525259-1 (opened): Vicia villosa Roth, "This species is accepted"; the paper names the species without a subspecies, so species rank and the accepted species name are right. |
| 3 | Aesculus hippocastanum / sense_chemical | ok (note) | Springer page (opened): sentence verbatim, 85 characters, whole, direction (emission increased with larval development); "these substances" are the volatiles (benzaldehyde, ..., methyl salicylate) the abstract says were emitted after oviposition and early-instar mining. Herbivore-induced change in leaf volatiles caused by larvae mining leaves over their development, a living response, not an extract or pollutant injury. Johne, Weissbecker, Schütz, J Chem Ecol 32: 2303-2319, 2006 agree. POWO 781594-1 (opened): "This species is accepted". |
| 4 | Conium maculatum / sense_light_nonvisual | ok | Kentucky scholars page (opened): sentence verbatim, 97 characters, whole, direction (higher in light than darkness); MD = morphological dormancy as the abstract defines it. Baskin and Baskin, Can J Bot 68(9): 2018-2024, 1990, DOI agree. POWO 840668-1 (opened): Conium maculatum L., "This species is accepted". |
| 5 | Synedrella nodiflora / sense_light_nonvisual | ok (note) | SciELO page (opened): sentence verbatim, 119 characters, whole, direction (better in unfiltered light); it is the abstract's closing result sentence, after the growth result. Souza Filho and Takaki 2011 agree; no DOI or volume printed, as the record says. Name: colplanta.org POWO-data page 252024-1 (opened): "This species is accepted"; WFO wfo-0000126415 (opened) accepted. |
| 6 | Hesperis matronalis / sense_light_nonvisual | ok | Cambridge page (opened): sentence verbatim from "However,", 121 characters, whole, magnitude and direction; "20/10 C" is printed with a bare C and no degree sign, and "< 10%" with spaces round the symbol, exactly as the record has them. Susko and Hussein, Weed Sci 56(3): 389-393, 2008, DOI agree. POWO 285087-1 (opened): Hesperis matronalis L., "This species is accepted". |
| 7 | Tripleurospermum inodorum / sense_light_nonvisual | ok | zhenzhi.com record (opened): sentence verbatim, 38 characters, whole, magnitude; "+/-" printed as in the record. Value's 77% plateau (14 h weak white light with nitrate) and red/far-red reversibility are in the abstract. Hartmann, Krooss, Mollwo 1997, pp. 240-252, DOI agree; journal not named on the page, as the record says. POWO 256500-1 (opened): Tripleurospermum inodorum (L.) Sch.Bip. accepted, Matricaria inodora L. a homotypic synonym, so the record is filed under the accepted name. |
| 8 | Potentilla recta / sense_light_nonvisual | ok | Kentucky scholars page (opened): sentence verbatim, 56 characters, whole, a measured negative (never germinated in darkness), following the after-ripening-in-light sentence. Baskin and Baskin, Ann Appl Biol 117(3): 611-616, 1990, DOI agree. Name: WFO wfo-0000983388-2024-12 (opened) accepted; POWO species page did not surface in two searches, but POWO 2957009-4 (opened) says var. tyraica "is a synonym of Potentilla recta subsp. recta", an accepted autonym, so POWO keeps the species. |
| 9 | Oenothera biennis / sense_light_nonvisual | ok | zhenzhi.com record (opened): sentence verbatim, 95 characters, whole, magnitude; "95-100%" printed with a hyphen. Abstract also reports dark germination dropping (to 0% at one thermoperiod) later in the year, supporting the value. Kentucky scholars page (opened, no abstract) confirms Baskin CC, Baskin JM, Can J Bot 72(6): 779-782, 1994, DOI 10.1139/b94-098. POWO 172755-2 (opened): Oenothera biennis L., "This species is accepted". Not a repeat of main's d53 record (different paper, quote and kind of trial). |

Epithets and ranks: no record carries a hybrid or a POWO synonym, and none is filed at genus rank where a species is named.

Evidence errors: **0 of 9 (0%)**.

## Unconfirmed names (reported apart from errors)

- None. (Line 8, Potentilla recta, was confirmed on WFO and indirectly on POWO through the accepted autonym; no POWO species page surfaced.)

## Notes for the desk (not counted)

- Line 3: the abstract does not say how volatiles were sampled (attached leaves or detached leaves); the induction itself occurred on living trees through larval mining. The value's "after leafminer oviposition" is fair: the abstract attributes the profile change to oviposition and mining together.
- Line 5: the value's "both types germinated best under white light" compresses the abstract, which groups white light with 25 to 30 °C and high water availability as the conditions of higher germinability.
- Line 4: the page gives issue 9 (68(9)); the record omits the issue.
- Stray empty file docs/views/evidence/-h.jsonl on the unit branch.

## Counts and verdict

- Evidence: 0 errors in 9, 0%.
- Search records: none in the unit.
- Pooled with audits 83 to 90 (the pool as carried by audit 146: 55 in 1170 overall, 48 in 1026 search records): overall 55 in 1179, 4.7%; search records unchanged at 48 in 1026, 4.7%.
- **Verdict: pass** (0%, under 5%), with the stray file to be dropped before merge.

## Error lines

- docs/views/evidence/desk-d57.jsonl: none
- docs/views/evidence/desk-d57.jsonl unconfirmed name: none
- docs/views/searched/desk-d57.jsonl: no file
- docs/views/wanted/desk-d57.jsonl: no file
- stray: docs/views/evidence/-h.jsonl (empty)

## Blocked pages

- pherobase.com literature page for Johne et al. 2006 (fetch tool refused); scholars.uky.edu Oenothera page carried no abstract (zhenzhi.com record read instead).
