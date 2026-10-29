# Audit 139: desk-d49 (29 October 2026)

Unit: desk-d49, branch origin/research/desk-d49 (head e263da93). Files: docs/views/evidence/desk-d49.jsonl (9 lines) and docs/tracks/progress/desk-d49.md. The unit is a lead-reading unit with no searched or wanted file, so the mechanical gate and the search-record draw have nothing to run on; all 9 evidence lines were judged. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed. Quotes were checked against pages my own WebSearches returned, asking the fetch tool for the exact sentence and its boundaries; lengths were counted with Python on the record's string. I used 16 WebSearches.

Rulings applied (launch prompt and brief): one whole sentence of at most 125 characters, verbatim, giving the study's own result with a direction or magnitude; POWO synonyms and hybrids are errors; a record repeating main is an error; genus-level filing when a species is named is an error; mis-copied dose units are errors; set-light, shade, photoperiod, UV, night-light and germination light/dark trials count under sense_light_nonvisual; plant diel = flower opening and scent timing; hormone and elicitor responses count under sense_chemical.

## Main

origin/main holds no evidence for Panicum capillare, Minthostachys, Lathyrus aphaca, Hepatica nobilis, Arabis procurrens, Iberis sempervirens or Melissa officinalis (main has Hepatica asiatica, Lathyrus japonicus and Panicum virgatum only). For Foeniculum vulgare main holds sense_chemical (10.1007/BF00025215) and two sense_light_nonvisual records on long-day bolting (desk-c11, recheck-6-fixed, sweep-17), different papers and a different response, so line 5 neither repeats nor contradicts them. The Panicum, Lathyrus, Foeniculum and Hepatica papers appear on main only as wanted lines (harvest-c11, desk-d33, sweep-9), which these records settle.

## Evidence verdicts (9)

| line | taxon / trait | verdict | reason |
|---|---|---|---|
| 1 | Panicum capillare / sense_light_nonvisual | ok | Frontiers full text (opened): the Light subsection of Results holds the sentence verbatim as a whole sentence, 106 characters, with a direction (stimulation); the same subsection gives 56% under 12 h photoperiod at 30/25 and 35/25 C against 1 to 8% in darkness, matching the value; seed source B confirmed. Authors Wu, Asaduzzaman, Shephard, Ma; Front Agron 3, 2021; DOI agrees. POWO 181618-2: accepted. Germination light/dark trial. |
| 2 | Minthostachys mollis / sense_light_nonvisual | ok | Journal PDF on revistas.unal.edu.co (opened): abstract sentence 3, verbatim, 73 characters, direction (strong inhibition in darkness); sentence 5 gives above 80% under the light treatments. Authors, Acta Biol Colomb 16(2): 149-154, 2011 agree with the journal view page, which shows no article DOI (journal DOI only). WFO wfo-0000241026: Minthostachys mollis accepted (the POWO URL my search returned was a different name, Xenopoma verticillatum, so acceptance rests on WFO). |
| 3 | Minthostachys mollis / sense_chemical | ok | Same PDF: abstract sentence 4, verbatim, 47 characters; GA3 at 0, 5, 15 and 25 ppm matches the value's doses and unit. A measured null response to an applied hormone on living seed, which main logs as evidence (audits 107, 108, 110 rulings). Same paper as line 2 but a different trait, so no repeat. |
| 4 | Lathyrus aphaca / sense_light_nonvisual | ok | SciELO abstract (opened): sentence 4 verbatim, 123 characters, a whole sentence with a direction; sentence 9 is the over-125 photoperiod sentence the note mentions. The SciELO page printed no authors or DOI; the record takes them from the desk-d33 wanted line on main (Crossref), and the DOAJ hit for the quote names Planta Daninha, June 2019, consistent. POWO 501579-1: accepted. |
| 5 | Foeniculum vulgare / sense_light_nonvisual | ok | Frontiers full text (opened): the Results sentence is verbatim, 124 characters, direction and p value. The paper states light only in lx (12 lx and 24 lx, set by the number of LED modules), so the unit is copied correctly, however low the figures look. A set-light-intensity trial on living plants. Authors (Jo, Lee, Byeon, Park, Ryoo, Hwang) agree. Foeniculum vulgare accepted (long-standing name, not re-checked on a POWO page). |
| 6 | Hepatica nobilis / diel | ok | Zenodo PDF (opened): the sentence is verbatim, 121 characters, times and maximum given; Żuraw, Rysiak, Szymczak, Modern Phytomorphology 4: 39-43, 2013 as printed. Flower opening counted on living plants: plant diel. POWO 711404-1: "This species is accepted." |
| 7 | Arabis procurrens / diel | ok | pbsociety.org.pl article page aa.1656 (opened): abstract sentence 6, verbatim, 108 characters, magnitude given. Authors agree (Strzałkowska-Abramek, Tymoszuk, Jachuła, Bożek); DOAJ lists Acta Agrobotanica, April 2016; the article id aa.1656 matches the DOI suffix. The result pools the two species, so grade g filed at species rank under each named species is right (audit 138 ruling). WFO wfo-0000542687: accepted; the worldfloradb page was bot-blocked. |
| 8 | Iberis sempervirens / diel | ok | Same sentence and paper as line 7, filed for the other named species; not a repeat of main or of line 7 (different species). POWO 324670-2: accepted. |
| 9 | Melissa officinalis / diel | ok | Journal PDF on pbsociety.org.pl (opened): "The number of open flowers until 900 accounted for 66% of all flowers which opened during the day." verbatim as printed (900 for 9.00), 98 characters, magnitude given; the next sentences give "one half fewer" between 900 and 1100 and buds opening until noon, matching the value. Chwil, Acta Agrobotanica 62(2): 23-30, 2009; no DOI printed. Melissa officinalis accepted (long-standing name, not re-checked on a POWO page). |

Epithets and varieties: no record carries a variety, subspecies or hybrid; Panicum capillare, Lathyrus aphaca, Hepatica nobilis and Iberis sempervirens were confirmed on POWO pages, Minthostachys mollis and Arabis procurrens on WFO pages. None is filed at genus rank where a species is named.

Evidence errors: **0 of 9 (0%)**.

## Note for the desk (not counted)

- The branch adds an empty file docs/views/evidence/-h.jsonl (0 bytes), apparently a command-line flag taken as a file name. It should be dropped before merge.
- The progress note's open lead (Eranthis hyemalis diel, Rysiak and Żuraw 2011) was not checked here.
- The Minthostachys PDF's Results give natural 80%, white 85%, red 91%; the value's "above 80%" is the abstract's wording and is right.

## Counts and verdict

- Evidence: 0 errors in 9, 0%.
- Search records: none in the unit.
- Pooled with audits 83 to 90 (the pool as carried by audit 138: 52 in 1096 overall, 48 in 1026 search records): overall 52 in 1105, 4.7%; search records unchanged at 48 in 1026, 4.7%.
- **Verdict: pass.** All nine evidence lines stand.

## Error lines

- docs/views/evidence/desk-d49.jsonl: none
- docs/views/searched/desk-d49.jsonl: no file
- docs/views/wanted/desk-d49.jsonl: no file

## Blocked pages

- public-pages-files-2025.frontiersin.org text for 10.3389/fpls.2022.1067713 (redirect not in provenance; the frontiersin.org full page served the text instead).
- worldfloradb.net Arabis procurrens page: bot protection.
