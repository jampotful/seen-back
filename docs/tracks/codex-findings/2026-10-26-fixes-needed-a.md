# Fixes needed (Codex findings 2026-10-26, share A)

Written by the triage unit `research/codex-triage-a`. Nothing here was edited in place. Each group names one root cause, the exact record ids (`<file>:<line>`, lines counted from 1 in the file as on origin/main of 26 October) and the route. Finding numbers (`n`) refer to `2026-10-26.jsonl`; verdicts are in `2026-10-26-verdicts-a.jsonl`.

## A. Evidence, wanted and searched records (corrections mechanism)

### A1. Corrected copies beside retracted originals
Root cause: 375 findings (n 407 to 785 except the four in A2) are recheck-N-fixed, oa-regraded or sweep records whose twin is a line `docs/views/audit/ALL.jsonl` retracts. `gaps.py` drops retracted lines; `rows.py` read raw logs without that filter and counted both. `tools/views/rows.py` now drops them (this branch). No record needs editing. Check after merge: `python3 -I tools/views/test_rows.py`.

### A2. Duplicates with neither line retracted
Same DOI, taxon, trait, value and quote; retract the second line of each pair (or the desk's choice) through the audit mechanism.

- n 523: `oa-1:2566` repeats `oa-1:2534`
- n 532: `oa-1:3349` repeats `oa-1:3348`
- n 533: `oa-1:3353` repeats `oa-1:3352`
- n 534: `oa-1:3358` repeats `oa-1:3357`

### A3. Measurement filed under another trait
- `canon-4:157` Melanitis leda: the interommatidial angle (Df 1.44 deg) is in the note of an acuity_cpd record; the interommatidial_deg cell stays open. Add a separately sourced interommatidial_deg record. (n 19)
- `oa-3:600` and `oa-3:601` Eugenes fulgens: wavelength discrimination filed under behaviour_vision; main files the like evidence for Selasphorus platycercus under spectral_range_nm. The desk decides one rule. (n 20)

### A4. Replacement characters in quotes
- `oa-12:4` to `oa-12:12` (nine lines) and `oa-2:3345`: U+FFFD in `quote`. Restore from the free copy and re-run `quotecheck.py`. (n 405, 406)

### A5. Searched records without a date
- `docs/views/searched/web-birds.jsonl:1-16`, `web-herps.jsonl:1-13`, `web-mammals.jsonl:1-21` (50 lines, n 2429 to 2478). Date from provenance if known (QUEUE shows the web searches ran 13 October 2026), else mark unknown.

### A6. Opsin localization or transcript records filed as receptor_classes at grade m
- `oa-2:3974, 3975, 3976, 3979, 3980, 3981, 3982, 3983, 3984, 3985, 3987, 3988, 3989, 3990, 3991, 3992, 3993, 3995, 3996, 3997, 3998, 3999` (22 lines, n 3252 to 3273). Their method says the observation does not measure a class. Regrade to g under a specific trait (oa-read.md grade rule).

### A7. Plant sense_chemical records on extracts and oils
- `sweep-13:11` (Convallaria majalis), `sweep-40:5` (Crithmum maritimum), `sweep-40:14` (Oplopanax horridus): desk-screen.md point 10(a) excludes them. Retract or move out of qualifying evidence. (n 3274 to 3276)

### A8. Held intake records inside the evidence directory
- `intake-2-failed.jsonl` (12 lines), `intake-4-failed.jsonl` (7), `intake-5-failed.jsonl` (3), `intake-6-failed.jsonl` (2), `intake-8-failed.jsonl` (5). `gaps.py` and `rows.py` read every .jsonl there, so held records count. Route: retract each line through the audit, or have the control room exclude `*-failed.jsonl` from both readers. (n 3278 to 3282)

## B. Wanted records

### B1. `rows` names a row title that rows.json does not list for that view
Examples: `reptile:Colour` (34 lines), `bird:Binocular overlap` (22), `insect:Colour` (17), `bird:Fovea` (15). Route: `docs/views/wanted/fixes.jsonl` with the live title (rows.json lists, for bird: Field of view, Sharpness, Speed, Ultraviolet; for reptile: The whole view), or a trait list in the line. Three lines also hold a title cut at a comma (`web-... frog:Field of view, sharpness and pupil`, `deer:Dim light`, `cattle:Field`). 211 lines:

- `audit-62.jsonl`: 1
- `birds-met.jsonl`: 2, 4, 12, 20, 22, 24
- `external-1.jsonl`: 1
- `external-2.jsonl`: 1, 2
- `harvest-17.jsonl`: 1
- `harvest-23.jsonl`: 1, 2, 3
- `harvest-27.jsonl`: 5
- `harvest-28.jsonl`: 1, 2, 5, 6, 11
- `harvest-47.jsonl`: 2
- `harvest-57.jsonl`: 3
- `herps-met.jsonl`: 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29
- `insects-met.jsonl`: 1, 2, 6, 9, 10, 12, 15, 20, 22, 23, 24, 25
- `mammals-met.jsonl`: 1, 2, 3, 7, 8, 10, 11, 14, 15, 16, 17, 18, 19, 22, 23
- `sweep-1.jsonl`: 8
- `sweep-101.jsonl`: 1
- `sweep-105.jsonl`: 1
- `sweep-16.jsonl`: 1
- `sweep-18.jsonl`: 2, 4, 5
- `sweep-19.jsonl`: 1, 2
- `sweep-23.jsonl`: 3
- `sweep-25.jsonl`: 1, 3, 4, 5, 6
- `sweep-3.jsonl`: 5
- `sweep-30.jsonl`: 1
- `sweep-31.jsonl`: 1, 2, 3, 5
- `sweep-43.jsonl`: 1, 3, 4, 5, 6
- `sweep-44.jsonl`: 1
- `sweep-46.jsonl`: 2, 3
- `sweep-47.jsonl`: 3
- `sweep-51.jsonl`: 2
- `sweep-53.jsonl`: 1
- `sweep-55.jsonl`: 1, 2, 3, 5, 7
- `sweep-59.jsonl`: 1, 2, 3
- `sweep-64.jsonl`: 1, 2, 3, 4
- `sweep-66.jsonl`: 1
- `sweep-7.jsonl`: 1, 2, 3, 4
- `sweep-75.jsonl`: 2, 4
- `sweep-8.jsonl`: 3, 4
- `sweep-9.jsonl`: 3, 4
- `sweep-91.jsonl`: 4
- `web-birds.jsonl`: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 55, 56, 57
- `web-herps.jsonl`: 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 15, 17, 18, 19, 20, 21, 22
- `web-mammals.jsonl`: 10, 34, 35, 36, 37, 38

### B2. DOI and resolver URL disagree
- `plant-1.jsonl:89` doi 10.1016/j.envexpbot.2022.104797, url https://doi.org/10.2139/ssrn.3968764 (probably a preprint address). (n 2230)

## C. Taxonomy (control room: taxonomy-extra.tsv, gaps.py and the generated gap files)

### C1. Genus filed under its homonym's family
Root cause: `Tax` in `tools/views/gaps.py` keys by genus alone, plus `taxonomy-extra.tsv` line 70 (Drymomantis). `cells.jsonl` today: Drymomantis (frog) Mantidae; Arenaria (bird) Caryophyllaceae; Linaria, Prunella, Morus (bird, plant) Plantaginaceae, Lamiaceae, Moraceae; Aquarius, Orthosia, Iris, Colocasia, Scoparia, Amorpha, Dryas (insect, plant) under plant or moth families; Parnassius (insect) Parnasiinae. n 3 to 15. Drymomantis should read Pelodryadidae, Anura (QUEUE 382, GBIF run 22).

### C2. Synonyms the gap index does not apply
- `gbif-names.tsv` files Xenochrophis piscator under Xenochrophis (Fowlea piscator in current use); main holds its RH1 and LWS rows. (n 16)
- 66 cells in `cells.jsonl` (n 2872 to 2943, six of them only weakly: 2918, 2920, 2925, 2926, 2928, 2942) whose species has an accepted-name twin with an m record. Some twins are backbone lumps (Bombus subterraneus and Anthophora acervorum), so normalise through the table with a review.
- Lyrurus (Phasianidae) sits in the wader view in `queue.jsonl` and `cells.jsonl`. (n 17)

### C3. Empty family and order in cells.jsonl though taxonomy-gbif.tsv has them
Genera per view: bee 228, bird 253, deer 38, frog 46, hawk 49, insect 335, plant 225, reptile 320, squirrel 300, wader 145 (n 2944 to 2953). Regenerate with the table loaded.

## D. Tooling findings that hold and were left unchanged
Root cause and reason in the verdict notes. n: 1, 2, 18 (gaps.py branch reading, genus key, ids); 3308, 3309 (oa_lint sign and docstring); 3311, 3312 (coverage.py); 3313 to 3316 (gaps.py); 3318 to 3320 (screen_candidates.py); 3323 to 3325, 3327 (wanted_csv, gain, papers_extra); 3330 (addlog `opened` default); 3332, 3334 (harvest); 3335 (oa.yml `|| true`); 3349, 3350 (oa.py).
