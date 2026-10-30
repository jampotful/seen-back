# audit-179: desk-d89 (1 evidence record, no search records, no wanted lines)

Audited 29 October 2026 from the desk-d89 files copied untracked into the worktree (progress note and 1 evidence line; neither is committed here). Mechanical gate: `screen_candidates.py --check` with empty searched and wanted files prints "0 problems". Quote length counted here: 113 characters; it is one whole sentence, the last (sixth) sentence of the English abstract, and the WebFetch summariser confirmed it word for word on a yes/no request. 1 WebSearch used.

Duplicates: git grep on origin/main (5b0456e6) under docs and views finds no record for Aristotelia and not the DOI, so the line repeats and contradicts nothing.

Sources opened: revistabosque.org/index.php/bosque/article/view/394 (English title and abstract, six sentences; Bosque, Vol. 38 No. 3, 2017, Short Communications; the page prints no DOI or page range); revistabosque.org/index.php/bosque/article/download/394/252 (the open Spanish PDF, read through three WebFetch passes; printed citation BOSQUE 38(3): 593-597, 2017, DOI 10.4067/S0717-92002017000300017); api.crossref.org/works/10.4067/S0717-92002017000300017 (Rodríguez Beraud M, Tampe Pérez J in that order, Bosque (Valdivia) 38(3): 593-597, 2017, Spanish title); POWO 19666-2 (Aristotelia chilensis (Molina) Stuntz, "This species is accepted", Central and S. Chile to Argentina); IPNI 19666-2 (Elaeocarpaceae).

| line | taxon / trait | verdict | reason |
|---|---|---|---|
| 1 | Aristotelia chilensis / sense_chemical | ERROR (contrary result omitted) | Citation holds: authors in order, journal as printed, 38(3) with the issue copied, pages 593-597, year and DOI match the PDF and Crossref (163, 173); `where` names the article page and the PDF opened (171). Accepted name: POWO 19666-2 accepts it (the repo follows POWO; GBIF agrees) (176). Scope: GA3 and BAP are hormones; fluridone is an applied growth regulator (an ABA and carotenoid synthesis inhibitor), and desk-screen 10(d) admits "an applied hormone, growth regulator or elicitor", with growth retardants already logged on main (desk-d13 Cortaderia selloana, uniconazole, accepted in audit 103), so the FLU results belong in the record and should be stated, not dropped. Full-text figures carried and partial false (174, 176): Gmax at 60 days BAP 100 uM 85%, BAP 10 uM 79%, GA3 10 and 100 uM 77 and 72%, FLU 10 and 100 uM 74 and 75%, control 66%; descriptive statistics only (mean and SE, arcsine transform, SPSS), as the value says. Lag phase settled from the pages: the English abstract says GA3 and FLU germination "started after a lag phase of 40 days"; the Spanish resumen instead says these treatments began "una fase de mayor aceleración posterior a los 40 días"; the Results give onset after day 10 and never mention a lag, and the Discussion puts the GA3 rise between days 20 and 40. The paper contradicts itself and the record flags the conflict honestly. The control is no conflict: 27% at day 30 (resumen and abstract only) and 66% Gmax at day 60 (Results) are different measures, and the record prints both correctly. The fault is in the onset results the record read: the Results put germination onset "posteriormente al décimo día" for GA3 10 and 100 uM, BAP 10 uM and the control alike, and later for FLU, "entre el décimo primero y décimo segundo día", against the control's day 10. The record cites GA3's day-10 onset but not that the control started the same day, and does not carry FLU's later onset, a result contrary to the abstract's "GA3 and FLU accelerated germination" from the paragraph the desk read (162, 164, 176, 177, 178 line 2). Only BAP 100 uM started earlier (day 6), also not carried |

Faults noted, not counted:
- Line 1: conditions reads "abstract: control reached 27% at 30 days and BAP 100 uM 74%; GA3 and FLU 10 and 100 uM reached maximum germination of 77/72% (GA3) and 74/75% (FLU), BAP 79% (10 uM) and 85% (100 uM)"; the abstract gives only the 74%, 27% and 85% figures, and the GA3, FLU and BAP 10 uM maxima are Results figures. The values are in the source; the attribution is loose.
- Line 1: conditions omits the abstract's 40-day length of the lag phase and the Spanish resumen's different wording ("mayor aceleración" after 40 days), which together settle that the English abstract mistranslates or misstates the Spanish.
- Line 1: the Results also give time to 50% of Gmax, 18 days for BAP 100 uM and 20 days for BAP 10 uM; not carried, not contrary.
- Line 1: the Discussion and Conclusions say nothing on fluridone; the only FLU claims are the abstract's acceleration and the Results' higher Gmax with later onset.
- desk-d89.md: none of the held-out leads was checked.

Evidence errors: 1 of 1 (100.0%). Error lines: 1.
Search records: none in the unit (0 of 0). Wanted lines: none.

Pooled with audits 172 to 178: 13 of 36 evidence records (36.1%; audit 172 3 of 7, audit 173 0 of 5, audit 174 1 of 4, audit 175 0 of 3, audit 176 2 of 4, audit 177 3 of 6, audit 178 3 of 6, audit 179 1 of 1).

Verdict: fail on line 1. It can be refiled with the onset results (control, GA3 10 and 100 uM and BAP 10 uM after day 10, BAP 100 uM day 6, FLU days 11 to 12), the FLU results stated as a growth-regulator response, the abstract's 40-day lag beside the resumen's "mayor aceleración posterior a los 40 días", and the Gmax figures attributed to the Results.

Blocked or left alone: POWO urn:lsid taxon URL and results page (client error; the short taxon/19666-2 URL opened); WFO search (robots refusal). No library proxy, ResearchGate, academia.edu or Sci-Hub page opened; no paper text committed.

Stray files: none committed; the desk-d89 copies stay untracked.
