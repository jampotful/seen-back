# Audit 133: desk-d43 (re-screen of the 18 genera dropped after audit 131; branch origin/research/desk-d43)

## Lines judged

No sample was drawn: the launch prompt asks for the whole unit.
- Search records: all 17 lines of docs/views/searched/desk-d43.jsonl.
- Evidence records: all 3 lines of docs/views/evidence/desk-d43.jsonl.
- Wanted lines: all 9 read; lines 1, 3 (from audit 131), 4, 6 and 9 (from audit 131) checked against an opened page. Faults listed, not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on the unit's searched file with its wanted file prints "0 problems".

## Method

desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), audit 39's counting rule, audits 86 to 90 and 131 for format and rulings, plus the launch prompt's rulings.

- Queries. `harvest_get.py` ran offline for all 17 genera. A script compared each record's unprefixed `queries` with every `query` and `family review` line the harvest prints: all 16 harvested records match word for word and in order, with the "web: " lines after. Daphne prints "in no harvest run yet" and lists "web: " lines only. No harvest shows "gave up".
- Chased. Every harvested genus except Paris names a DOI printed in its harvest's own family-review list (positions 1 to 4); Paris names its two citation-step DOIs (one with 0 hits), as audit 131 accepted. Daphne (no run) names the web-found review 10.1007/s44372-025-00446-3 from a labelled web search, accepted under the ruling. No harvest genus names that web DOI, and no record claims no family review where one ran. No chased error.
- Main (origin/main 928533ee). No search record names a trait with evidence on main (Epigaea chemical desk-d19:1, Comarum light desk-d21:2, Comptonia chemical desk-d41:2, Eutrochium light desk-d41:3, Phalaris light and chemical oa-12 and oa-13b, Sequoia light sweep-29:12 and Paris light sweep-29:7 are all left out). No evidence record repeats main: main has no Mercurialis, Daphne or Cynoglossum evidence.
- Taxonomy. POWO page opened: Daphne mucronata Royle "is accepted". Mercurialis annua and Cynoglossum officinale are the familiar accepted names; no hybrid or synonym epithet appears in the unit.
- Harvest scan. A script listed every harvest work whose title or abstract names the genus together with a hormone, germination, light or anthesis word, and checked whether the record screened it. This found the Pulmonaria miss (line 13).

Searches: about 37 WebSearches and the fetches of URLs they returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened (a researchgate.net Pedicularis PDF result and an mtsu.academia.edu result were left alone). No paper text is committed. Blocked: archive.org biostor-137766 (permission unanswered, not retried), pmc PMC5654834 and PMC11216845 (bot check, then permission unanswered), journals.uchicago.edu 10.1086/337484 (site error).

## Search record verdicts (17)

| Line | Record | Verdict |
|---|---|---|
| 1 | Mercurialis eye_type | ok. Plant eye_type is "none"; chased is first in the Euphorbiaceae review list. |
| 2 | Paris diel, eye_type | ok. Citation-step chased printed. My anthesis search returned Cheng et al. 2021 (sjfsci.com opened), a flowering season of 45 to 83 days and no clock hour. The harvest's "Phenophase of Cultivated Paris polyphylla" gives a stage, not an hour. |
| 3 | Daphne diel, eye_type, light | ok. No-run genus, web chased accepted. Di Sacco et al. 2021 (Springer opened) used a 12 h photoperiod as a condition and tested no light against dark. My light search returned clover and Kalmia papers (both opened, no Daphne); my scent-timing search found no Daphne. |
| 4 | Anthoxanthum (4 traits) | ok. eflorasys (opened) has blank germination fields; my GA/smoke search returned no Anthoxanthum trial. Lead unresolved: biostor-137766 (grass anthesis), permission unanswered, as for the desk. |
| 5 | Betonica (4 traits) | ok. Lead unresolved, not counted: PMC5654834 (light, GA3 and nitrogen on eight taxa of Potentillo albae-Quercetum) is still behind a bot check, and no result shows its taxa list. |
| 6 | Calypso (4 traits) | **error: missed germination work.** My search "Calypso bulbosa asymbiotic seed germination darkness light in vitro" returned "Seed Germination of North American Orchids. I. Native California and Related Species of Calypso, Epipactis, Goodyera, Piperia, and Platanthera", Botanical Gazette, 10.1086/337245 (uchicago page opened; authors and year behind the paywall). Its title names germination in the genus, so 10(e) puts it on the wanted list; the record neither screens nor wants it. |
| 7 | Chelone sense_light_nonvisual | ok. My germination search returned nursery and seed-seller pages only. |
| 8 | Cocos diel, eye_type | ok. Singh et al. 2025 (Plant Archives, opened) gives only a collection hour; Nakdaeng et al. 2025 (opened) gives hours since an incubation began, as the record says. |
| 9 | Melampyrum sense_chemical | ok. Masselink 1980 (natuurtijdschriften opened), M. pratense germination by temperature and dormancy, no chemical or light treatment. Holloway 2011 lists none of the unit's genera. |
| 10 | Comarum diel, sense_chemical | ok. Lead unresolved, not counted: Wang et al. 2024, 15 Changbai peatland species under GA soaking (DOAJ and Dryad pages opened); the abstract names six species, none Comarum, and PMC11216845 was blocked. |
| 11 | Epigaea diel, eye_type, light | ok. Woody Plant Seed Manual and NARGS pages; no light/dark trial or opening hour. |
| 12 | Oemleria (4 traits) | ok. Woody Plant Seed Manual chapter (opened): stratification only, a flowering season, no hour. |
| 13 | Pulmonaria sense_chemical | **error: missed hormone trial in the harvest output.** "Axillary Shoot Proliferation from in Vitro Culture of Pulmonaria L. Shoots", HortScience 1996, 10.21273/hortsci.31.4.630d ([4] of the Pulmonaria output): shoots of Pulmonaria 'Roy Davidson' on benzyladenine at 0 to 44.4 µM, shoot count highest at 8.8 µM. A living tissue's dose response to an applied cytokinin, 10(d); it is neither screened nor wanted. A cultivar of unstated species, so it would be a genus-level (g) record. |
| 14 | Phalaris diel | ok. My anthesis search returned sunflower and Pharbitis papers only. |
| 15 | Sequoia diel, eye_type, sense_chemical | ok. Woody Plant Seed Manual (opened): soaking and stratification, no GA3 or chemical trial, no pollen hour; the El-Malki GA3 paper is Cupressus (opened), as the record says. |
| 16 | Comptonia diel, eye_type | ok. Light cell correctly left to the wanted line (line 9). No opening-hour work found by the desk's or my scans. |
| 17 | Eutrochium diel, eye_type, chemical | ok. My searches returned extension pages and the Ageratina (E. adenophorum) MeJA paper, which is another genus. |

Search record errors: **2 of 17 (11.8%)**: lines 6 and 13.

## Evidence record verdicts (3)

| Line | Record | Verdict |
|---|---|---|
| 1 | Mercurialis annua sense_chemical | ok. Quote verbatim in the abstract (Frontiers public page opened); authors confirmed; 25% chronic tissue loss in the abstract. The bioRxiv Methods (opened) confirm polysorbate 20 and spraying every two weeks over 12 weeks; 0.01% was not seen in either page (the record flags the dose as relayed). |
| 2 | Daphne mucronata sense_chemical | ok. iris.unibs page opened: authors, Plant Biosystems 159(3): 476-487, 2025, 10.1080/11263504.2025.2485980. The quote is one abstract sentence of 121 characters reporting the result; the dose unit (ppm) is as printed. POWO: accepted. |
| 3 | Cynoglossum officinale sense_light_nonvisual | **error: the quote does not report a measured light response.** The sentence is verbatim, but the abstract (natuurtijdschriften opened) prints it twice, once after the C. officinale sentences and once after the Anchusa arvensis sentences, so it cannot by itself tie the result to C. officinale. It says only that the light response differed between populations: it states no direction, no value and not even that light changed germination in any population. The value repeats that and nothing more. Judged on the specific concern: not sufficient for sense_light_nonvisual. The work belongs on the wanted list for the full text. |

Evidence errors: **1 of 3**.

## Wanted lines (faults listed, not counted)

- Line 6 (Chelone): the journal page gives the first author as "Leif L. Richardson", not "Lindsay L.", and prints DOI 10.26786/1920-7603(2015)18, which the line leaves empty.
- Line 1 (Vandelook et al., Folia Geobot 54: 73-84) and line 4 (Runyon and Birdsall 2016, Arthropod-Plant Interactions 10: 383-391; no DOI on the page) match their pages. Lines 3 and 9 match audit 131's opened pages. Line 2's empty authors and lines 5, 7 and 8 were not reopened.

## Counts

- Search records: 2 of 17, 11.8%.
- Evidence: 1 of 3.
- Unit: 3 of 20, 15.0%. Fails (above 5%).

Pooled with audits 83 to 90, from audit 90's figures as audit 131 gives them (48 in 1026 search records; 52 in 1090 overall):
- Search records: 50 in 1043, 4.8%.
- With evidence: 55 in 1110, 5.0%.
Audits after 90 are not added, as in audits 129 to 131.

Forks:
- Line 13. If an in-vitro shoot culture counts as excised tissue (like cut-branch sampling) and not a living plant, line 13 stands and search errors fall to 1 of 17 (5.9%). The unit still fails with line 3.
- Line 6. Whether the Botanical Gazette paper tested light or hormones is unread; the count rests on 10(e), which sends any germination-titled work on a species of the genus to the wanted list.
- Evidence line 3. If the desk reads "the light response differed" as evidence that a light response exists, the record stands with grade m only after the species attribution is shown from the full text; the duplicated sentence leaves that open even then.

## Error lines

- docs/views/searched/desk-d43.jsonl: 6, 13.
- docs/views/evidence/desk-d43.jsonl: 3.
- docs/views/wanted/desk-d43.jsonl: none counted (line 6 author and DOI faults listed).
