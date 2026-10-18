# Precision audit 33, 17 October 2026

Scope: the corrected records in `docs/views/evidence/recheck-41-fixed.jsonl` to `recheck-52-fixed.jsonl` (499 lines; recheck-41 is empty), and the lines in the codex evidence files `oa-*.jsonl` (not `oa-regraded`) and `harvest-c*.jsonl`, taken as the added population because `tools/views/repair_codex.py` is not in this worktree (`docs/views/repair/counts.json` gives 18,012 added lines). Records carry no id field, so the fixed records are named by file and line number and the codex records by `file:line`.

Draw: Python `random.seed(33)`, `random.sample` of 10 from the fixed lines (they fall in six files: 44, 45, 47, 49, 51, 52) and 10 from the added lines. Because errors were found, 15 more came from the same stream (8 fixed, 7 added, none repeated).

Method as in audits 16 and 32: WebSearch on the title, then WebFetch on a URL the search returned (the fetch tool only opens URLs it has already seen). No library login, proxy or shadow library was used and no paper text is committed. An error is any one of: a quote that is not one complete sentence or is not marked as cut, a value or grade the quote does not support, a missing `partial: true` on an abstract, compiled, table or review read, an author list that is not complete, a journal field without volume, issue or pages as printed. A record whose source would not open is `unverifiable`. Reviews are counted as needing `partial: true`, as in audit 32.

## First 20

| # | record | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 1 | recheck-47 L85 | Calendula officinalis / sense_chemical | m | unverifiable | PMC shows a browser check; no other page returned. The journal field is empty |
| 2 | recheck-44 L2 | Eristalis tenax / eye_role | m | confirm | Caltech record: abstract sentence 2, verbatim after the marked opening cut. Three authors, 209(21): 4339-4354, `partial: true` |
| 3 | recheck-49 L19 | Bubo virginianus / dark_adaptation_time_min | m | confirm | USF PDF p. 63, verbatim and complete. 18(2):62-66 |
| 4 | recheck-45 L21 | Habrocestum africanum / opsin_localization | m | error (journal) | quote verbatim and complete (NSF copy). Journal field is "Vision Research" only; the paper is 217: 108367 |
| 5 | recheck-51 L2 | Parabuteo unicinctus / head_movements_per_decision | m | error (journal) | sentence verbatim and complete (Silverchair page). Journal field "219:2639-2649" lacks the issue (219(17)). Seven authors match |
| 6 | recheck-51 L14 | Aipysurus laevis / acuity_cpd | g | error | IntechOpen review chapter, verbatim and complete, but no `partial: true` on a review. Journal field has no pages (the page gives none) |
| 7 | recheck-45 L43 | Menemerus confusus / lambda_max_nm | g | error | the page sentence runs on to "and Plexippus validus (535 nm in PLEs; Hardie and Duelli, 1978), matching the molecular studies ... (Terakita and Nagata, 2014)." The quote stops mid-sentence at 40 words with no ellipsis. Journal field also lacks volume and article number |
| 8 | recheck-47 L38 | Bombus occidentalis / behaviour_vision | g | error | verbatim and complete, p. 494 of the Annual Review chapter; no `partial: true` on a review |
| 9 | recheck-49 L29 | Corvus macrorhynchos / ganglion_density_mm2 | m | confirm | conference abstract page; the cut sentence is marked at both ends; three authors; `partial: true` |
| 10 | recheck-52 L6 | Deilephila elpenor / superposition_pupil_facets | m | error (journal) | verbatim, p. 821. Journal field "26:821-826" lacks the issue (26(6)) |
| 11 | oa-9:2180 | Alpinia caerulea / sense_light_nonvisual | m | unverifiable | Perrin Appendix S3 table row; supplement not returned. The row has no `partial` |
| 12 | oa-2:5794 | Phrynoidis juxtasper / eye_diameter_mm | m | unverifiable | GitHub CSV not openable by the fetch tool |
| 13 | oa-9:2770 | Asparagus sprengeri / sense_light_nonvisual | g | unverifiable | appendix1.xlsx not openable |
| 14 | oa-2:5620 | Odontobatrachus natator / corneal_diameter_mm | m | unverifiable | GitHub CSV |
| 15 | oa-1:5818 | Gongylophis conicus / lambda_max_nm | i | unverifiable | the City manuscript opened but holds no Table S5 (it cites "SI Table S5"). Ten authors match |
| 16 | oa-2:9695 | Menemerus bivittatus / opsin_localization | m | error | NSF copy: the page sentence is "though only for RH1 in the AMEs and RH2 in the lateral eyes (ALEs, PLEs)"; the quote "RH2 in the lateral eyes (ALEs, ... PLEs)" is a fragment. Journal field again lacks volume and article number |
| 17 | oa-9:2651 | Calystegia sepium / sense_light_nonvisual | g | unverifiable | appendix1.xlsx |
| 18 | oa-2:8561 | Heloderma suspectum / corneal_diameter_mm | g | unverifiable | CSV (vertebrate_eyesize.csv) |
| 19 | oa-9:3906 | Leptospermum polygafolium / sense_light_nonvisual | m | unverifiable | RawBinaryGermData.csv |
| 20 | oa-2:4835 | Flectonotus fitzgeraldi / eye_diameter_mm | m | unverifiable | GitHub CSV |

First 20: 10 unverifiable, 10 verifiable, 7 errors (3 journal-only).

## Extension, 15 more

| # | record | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 21 | recheck-45 L69 | Bos taurus / lambda_max_nm | g | error | USU thesis p. 12, verbatim and complete, but it sits in the Literature Review and reports Barry and Mathies (1982); no `partial: true` |
| 22 | recheck-50 L17 | Salticidae / eye_movement | g | error | Morehouse p. R977 verbatim and complete. A Current Biology magazine overview with no `partial: true`; the journal field has no volume or pages (30: R963-R983) |
| 23 | recheck-47 L67 | Anolis carolinensis / oil_droplets | m | confirm | verbatim; the trailing statistic is cut with a marked ellipsis; 2: 1410763; two authors |
| 24 | recheck-47 L43 | Fabaceae / sense_light_nonvisual | g | error | verbatim with a marked leading cut, but a review article with no `partial: true` |
| 25 | recheck-47 L23 | Papilio xuthus / lambda_max_nm | g | error | p. 477 verbatim up to the marked cut; Annual Review chapter with no `partial: true` |
| 26 | recheck-45 L49 | Caretta caretta / eye_role | m | confirm | ESR p. 71 verbatim and complete; 41: 67-77; three authors |
| 27 | recheck-52 L49 | Bothrops jararaca / lambda_max_nm | g | confirm | Frontiers PDF: verbatim with the Figure 6 and Table 3 cut marked; 15: 770804; three authors; value cites another study and is graded `g` |
| 28 | recheck-50 L10 | Salticidae / interreceptor_deg | g | error | p. R976 verbatim and complete; the same overview with no `partial: true` and no volume or pages |
| 29 | oa-2:9172 | Podocarpus rubens / sense_light_nonvisual | g | unverifiable | Springer supplementary PDF not opened |
| 30 | oa-1:2026 | Anigraea sp. / opsin_sequences_recovered | m | unverifiable | spreadsheet |
| 31 | oa-1:9580 | Planorbarius corneus / pupil_diameter_um | g | unverifiable | BioOne page returned a bot-protection page |
| 32 | oa-2:1899 | Petropedetes vulpiae / pupil_shape | m | unverifiable | NHM CSV |
| 33 | oa-1:9841 | Lepus californicus / orbit_convergence_deg | i | unverifiable | Figshare CSV |
| 34 | oa-2:5323 | Mantella aurantiaca / corneal_diameter_mm | m | unverifiable | GitHub CSV |
| 35 | oa-2:4597 | Dendropsophus parviceps / eye_diameter_mm | m | unverifiable | GitHub CSV |

Extension: 7 unverifiable, 8 verifiable, 5 errors (none journal-only).

## Error rate

- First 20: 7 errors in 10 verifiable records.
- Both draws: **12 errors in 18 verifiable records, 66.7%** (17 of 35 unverifiable).
- Excluding journal-only faults (records 4, 5 and 10): **9 errors in 18, 50%**.
- By population: the fixed records, 8 errors in 14 opened (57%; 3 journal-only); the added codex lines, 1 error in 1 opened, with the other 15 sampled lines resting on data files or supplements that did not open.

## Findings

1. The requote repair held. Of the 14 fixed records that opened, 11 carry a quote that is verbatim and complete or cut with marked ellipses. The one clear quote fault is recheck-45 L43 (Menemerus confusus), where the 40-word cap cut the sentence without a mark.
2. Most of the remaining errors are missing `partial: true` on reviews (records 6, 8, 21, 22, 24, 25, 28: Annual Review, Frontiers review, IntechOpen chapter, magazine overview, thesis literature review). The repair never set the flag for those reads.
3. Journal fields still lack the issue or volume in the fixed files (Vision Research, J Exp Biol, Current Biology), as audit 32 found in the codex files.
4. The added codex lines are mostly data rows (GitHub, NHM and Figshare CSV, spreadsheets, supplements); the fetch tool could not open them, so 15 of 16 sampled lines are unchecked. The only opened one, oa-2:9695, is a fragment quote.
5. The 5% threshold is not met on any counting.

No evidence file was edited and no correction rows were written.

## Blocked pages

PMC (browser check) for the Calendula paper; BioOne (bot protection) for Zieger and Meyer-Rochow; raw.githubusercontent.com, Figshare and NHM data files (not in the fetch tool's seen set); the Frontiers `/text` redirect for Tashiro (the `/pdf` page opened instead).
