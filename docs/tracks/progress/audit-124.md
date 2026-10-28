# Audit 124: desk-d33 (plant screening unit; branch origin/research/desk-d33, head 1f583f5d)

## Lines judged

No random sample was drawn. The brief asks for the whole unit to be judged, so that error lines can simply be dropped.
- Evidence: all 7 lines of docs/views/evidence/desk-d33.jsonl.
- Search records: all 53 lines of docs/views/searched/desk-d33.jsonl. Every record was checked for `queries` and `chased`. I ran my own trait searches for every null on a sense_chemical or sense_light_nonvisual cell, and for the diel cells of 12 genera. The eye_type records rest on the owner's reading 10(b) ("none" for every plant), so they were judged on queries and chased only.
- Wanted: 4 of 17 lines were checked against a page (lines 12, 15, 16, 17). The other 13 were not checked.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on the unit's searched and wanted files printed "0 problems". Every quote is 125 characters or fewer, measured by script (68 to 113).

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), the counting rule of audit 39 and the brief's rulings (audits 84 and 86 to 90). Audit 123 gave the format.
- About 50 WebSearches. I fetched only URLs that my own searches or a fetch's result returned, with one exception: I opened nepjol.info 78187 from the unit's own `screened` list. It is an open journal page.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. No paper text is committed.
- Main. I checked origin/main (3ea90ff8) docs/views/evidence, searched and wanted for every genus in the unit. Main holds evidence for Asimina diel and sense_chemical, Ornithogalum diel and sense_light_nonvisual, Sedum album diel, Nicotiana sylvestris diel, Tragopogon hybridus diel, Echinocereus sense_light_nonvisual, Humulus sense_light_nonvisual, Dryopteris sense_light_nonvisual and sense_chemical, Drosera sense_chemical, Centranthus sense_chemical, and Lathyrus japonicus sense_chemical (canon-3:674). The unit writes no search record or evidence for any of those cells. Its 7 evidence cells (Asimina triloba, Alnus glutinosa, Thalictrum rochebruneanum, Tragopogon pratensis) have no evidence on main. gaps/cells.jsonl shows every cell the unit searched as open ("i").

### Queries

`harvest_get.py` ran without the network (it reads origin/ci). Eleven genera are in a harvest run: Knautia, Asimina, Drosera, Humulus, Anacamptis, Carduus, Tragopogon, Nicotiana, Dryopteris, Ornithogalum and Lathyrus. A script compared each of their records' unprefixed `queries` with every `query` and `family review` line the harvest prints (lines 1 to 3, 16, 17, 24 to 26, 34 to 38, 42 to 44, 49 and 50). All match word for word and in order, and the "web: " lines come after them. The other 13 genera print "in no harvest run yet", and their records list "web: " lines only.

### Chased

- Lines 16, 17 (Drosera), 24 (Humulus), 25, 26 (Anacamptis), 37 (Tragopogon), 38 (Nicotiana), 42, 43 (Dryopteris) and 49, 50 (Lathyrus) name a DOI that the harvest prints in its citation step. For Lathyrus, the record says 10.3389/fpls.2015.00207 came from a Fabaceae web search. The output does print it as a citation step, so it is supported, but the label is wrong. Line 44 (Ornithogalum) gives a reason: the harvest runs no citation step for that genus, which the output confirms.
- Lines 4 to 7, 18, 19, 21 to 23, 27 to 30, 45 to 48, 51 and 52 name 10.1007/s10265-016-0785-4 (Li and Mathews) for genera in no harvest run. My own "Papaveraceae", "Annonaceae" and "Ranunculaceae photoreceptor review" searches each returned "evolutionary aspects of plant photoreceptors" (nutrition-evidence.com 249643), as audits 87 and 121 found. These are supported. Lines 45 to 48, 51 and 52 name the DOI and then say the search "returned general photoreceptor works only". That wording contradicts itself but does not change the support.
- Lines 8 to 15, 20, 31 to 33 and 39 to 41 give "none" reasons for genera in no harvest run. They are accepted.
- Lines 1 and 2 (Knautia) and line 3 (Asimina) are harvest genera. Their chased DOIs (10.1007/s44372-025-00446-3 and 10.1007/s10265-016-0785-4) are not printed by the harvest, but my own "Caprifoliaceae photoreceptor review" and "Annonaceae photoreceptor review" searches returned them. I accept them under the brief's test ("a chased DOI that no harvest or web search supports is an error"); see the fork under Counts.
- **Lines 34, 35 and 36 (Carduus).** The records name 10.1007/s10265-016-0785-4 with the reason "the harvest's own Asteraceae family search is in queries". The Carduus harvest output does not print that DOI or that title. None of the records' own "web: " lines is a family-review search. The DOI is unsupported, so all three lines are errors (as audit 90 ruled on Olea).
- **Line 53 (Centranthus).** The record names 10.1007/s10265-016-0785-4 from its labelled "Caprifoliaceae photoreceptor review" search, and says that search "returned general photoreceptor works only". When I ran the same search, it returned 10.1007/s44372-025-00446-3 and general works, but not Li and Mathews. The unit's own Knautia records (lines 1 and 2) report the same result for that query. So the chased DOI is unsupported, and the line is an error.

### Names

- POWO pages I opened: Matteuccia struthiopteris (L.) Tod., "synonym of Onoclea struthiopteris" (urn 17145680-1); Mycelis Cass., "synonym of Lactuca" (urn 10135-1); Dicentra spectabilis (L.) Lem., "This name is a synonym of Lamprocapnos spectabilis" (672659-1). Struthiopteris: the POWO species pages I opened (S. amabilis, 17420090-1; S. shaferi, 247264-2) are synonyms of Blechnum, so the unit was right to skip that genus.
- Thalictrum rochebruneanum (lines 5 and 6). The sources name T. rochebrunianum var. grandisepalum. Wikipedia, which links to POWO 714828-1, spells the accepted species rochebruneanum Franch. & Sav. and lists var. grandisepalum as a synonym. I could not read the POWO page itself (permission not answered; not retried). Logging at the species follows that treatment.
- Asimina triloba, Alnus glutinosa and Tragopogon pratensis are not in question.

## Evidence verdicts (7)

| Line | Record | Verdict |
|---|---|---|
| 1 | Asimina triloba sense_light_nonvisual (Pomper, Layne, Jones 2002) | ok. In the KSU PDF (opened) the quote is a whole abstract sentence, verbatim. The PDF confirms J Amer Soc Hort Sci 127(1): 13-19 and prints no DOI. Shade levels were 0, 28, 51, 81 and 98% outdoors and 0, 33, 56, 81 and 98% in the greenhouse. The 28/51/81% gains are in the abstract. Set-light-intensity trial under 10(d). |
| 2 | Asimina triloba sense_light_nonvisual (Finneseth, Layne, Geneve 1998) | ok. Quote verbatim and whole in the abstract on scholars.uky.edu (opened). Seed Sci Technol 26(2): 471-480; title as printed ("North AMerican"); no DOI on the page. |
| 3 | Alnus glutinosa sense_light_nonvisual (Graca 1983) | ok. Quote verbatim in the Purdue e-Pubs abstract (opened). The abstract gives five light levels (20, 37, 53, 70 and 100% of natural light) and names A. glutinosa among four species. |
| 4 | Alnus glutinosa sense_light_nonvisual (Jezdinský, Řezníček 2011) | ok. Quote verbatim in the journal abstract (opened) and reported as a result. 59(3): 81-90, 10.11118/actaun201159030081. |
| 5 | Thalictrum rochebruneanum sense_light_nonvisual (Cho, Kwon, Lee 2016) | ok. KoreaScience page (opened): the quote is verbatim, a whole sentence, in the Results. The abstract gives the dark maximum, 16.3% at 25 C. Citation and DOI 10.7732/kjpr.2016.29.3.339 match. |
| 6 | Thalictrum rochebruneanum sense_chemical (Lee, Rhie, Jung, Kim 2012) | ok. ASHS 2012 abstract (opened): quote verbatim, with the dose printed "1,000 mg·L-1" exactly as the record copies it. It is a result. GA3 response under 10(d). |
| 7 | Tragopogon pratensis sense_light_nonvisual (Qi, Upadhyaya 1993) | ok. Cambridge Core abstract (opened): quote verbatim and whole. The sentence before it names meadow salsify (stratification of secondary-dormant seeds), so grade m for T. pratensis stands. Wording point, not counted: the record does not say that the secondary dormancy was induced by anaerobiosis. |

**Evidence errors: 0 of 7.**

## Search-record verdicts (53)

"Own search" means I ran a trait search for the cell myself. "Q/C only" means only queries and chased were checked.

| Line | Record | Verdict |
|---|---|---|
| 1 | Knautia diel | ok (chased fork, below). Own scent-rhythm search: only general circadian-scent reviews; no Knautia hour. |
| 2 | Knautia eye_type | ok (chased fork). Q/C only. |
| 3 | Asimina eye_type | ok (chased fork). Q/C only. |
| 4 | Anaphalis diel | ok on Q/C. No own diel search (budget). |
| 5 | Anaphalis eye_type | ok. Q/C only. |
| 6 | Anaphalis sense_chemical | ok. Own search returned Arabidopsis jasmonate papers (whiterose 114205, core 8441522, opened); no Anaphalis trial. |
| 7 | Anaphalis sense_light_nonvisual | ok, with a lead. Kafle et al. 2025 (Nepal J Bot 2; nepjol 78187, opened) tests light against dark in 37 Nepal species, and its page names none of them. The record put it in `screened` with its species list unseen. Point 3 would send such a work to the wanted list instead. Not counted, because no Anaphalis result was shown. |
| 8 | Sherardia diel | ok on Q/C. No own diel search (budget). |
| 9 | Sherardia eye_type | ok. Q/C only. |
| 10 | Sherardia sense_chemical | ok on Q/C. No own chemical search (budget); the germination search below returned no hormone or smoke trial. |
| 11 | Sherardia sense_light_nonvisual | ok, with a lead. Own search: the eFloraSys page (opened) gives germination temperatures only, with no source. "Seed germination of five weed species under different temperatures and light conditions" (plantarum 386; Serbian twin omorika 677) sat behind a human check, and enauka was down. The record also screened this paper with "whether Sherardia is among them is unknown". It belongs on the wanted list. Not counted. |
| 12 | Mertensia diel | ok on Q/C. No own diel search (budget). |
| 13 | Mertensia eye_type | ok. Q/C only. |
| 14 | Mertensia sense_chemical | ok. Own searches: Skarpaas and Stabbetorp 2001 (Oikos 95(3): 374-382, AGRIS opened) tests physical treatments (seawater) only, and salinity does not count (audit 88). Nothing else on Mertensia. |
| 15 | Mertensia sense_light_nonvisual | ok. Same two searches; no light trial. |
| 16 | Drosera diel | ok, with a lead. Own search: the Wikipedia article on Drosera cuneifolia (opened) says the flowers "open in the morning and close by mid afternoon", with no source given. That is a lead, not a measurement (audits 12 and 89). |
| 17 | Drosera eye_type | ok. Q/C only. |
| 18 | Sedum eye_type | ok. Q/C only. |
| 19 | Sedum sense_chemical | ok. Own search returned smoke studies of other genera (Çatav et al. 2024, chaparral smoke papers); no Sedum. |
| 20 | Alnus eye_type | ok. Q/C only. |
| 21 | Echinocereus diel | ok. Three own searches: Aslan 2015, Am Midl Nat 173(1): 61-72 (NAU page opened; no opening hours in the abstract; the BioOne pages returned no text), and garden pages. No hour of opening. |
| 22 | Echinocereus eye_type | ok. Q/C only. |
| 23 | Echinocereus sense_chemical | ok. Own search returned Echinochloa and Shultz pages (the bepress redirect was not followed); no Echinocereus trial. |
| 24 | Humulus diel | ok. Own search: Ehara 1956 (J Fac Agric Kyushu Univ 10(4): 307-324, opened) gives blooming months only. |
| 25 | Anacamptis diel | ok. Own scent-rhythm search returned only general reviews and Altenburger and Matile 1990 (other species). |
| 26 | Anacamptis eye_type | ok. Q/C only. |
| 27 | Thalictrum diel | ok. Own search returned Penstemon anther-dehiscence work (J Poll Ecol 2023, DOAJ opened) and general papers; no Thalictrum hour. |
| 28 | Thalictrum eye_type | ok. Q/C only. |
| 29 | Arbutus diel | ok. Own search returned Fung and Thomson 2017 (no species named) and an Epipactis nectary paper (both opened); no Arbutus hour. |
| 30 | Arbutus eye_type | ok. Q/C only. |
| 31 | Barbarea diel | ok on Q/C. No own diel search (budget). |
| 32 | Barbarea eye_type | ok. Q/C only. |
| 33 | Barbarea sense_chemical | **error: missed measurement.** My search "Barbarea vulgaris jasmonic acid induced glucosinolates OR saponins herbivory living plants" returned Liu, Zhang, Yang, Agerbirk, Qiu, Wang, Shen, Song, Li 2016, "Aromatic glucosinolate biosynthesis pathway in Barbarea vulgaris and its response to Plutella xylostella infestation", Front Plant Sci 7: 83, 10.3389/fpls.2016.00083 (DOAJ and Pherobase pages opened). In that paper, diamondback moth larvae feeding on living G-type and P-type B. vulgaris induced hydroxylated aromatic glucosinolates and their biosynthesis genes. That is a herbivore-induced response under 10(a), as the brief reads it. The record's own query, "web: Barbarea vulgaris jasmonate OR herbivore-induced volatiles OR methyl jasmonate", did not surface it. |
| 34 | Carduus diel | **error: unsupported chased** (above). My own diel search found nothing (sunflower clock papers only). |
| 35 | Carduus eye_type | **error: unsupported chased** (above). |
| 36 | Carduus sense_light_nonvisual | **error: unsupported chased** (above). My own light/dark search found no Carduus trial. |
| 37 | Tragopogon eye_type | ok. Q/C only. |
| 38 | Nicotiana eye_type | ok. Q/C only. |
| 39 | Clintonia diel | ok on Q/C. No own diel search (budget). |
| 40 | Clintonia eye_type | ok. Q/C only. |
| 41 | Clintonia sense_chemical | ok. Own search: propagation protocols and the Holloway 2011 Georgeson Botanical Note 43 on GA (UAF PDF opened), which has no Clintonia. That note lists Actaea rubra as responding to GA ("promotes more complete germination after scarification or stratification"), a lead for the Actaea sense_chemical cell, for which the unit wrote no record. |
| 42 | Dryopteris diel | ok. Own spore-release timing search returned no Dryopteris study. |
| 43 | Dryopteris eye_type | ok. Q/C only. |
| 44 | Ornithogalum eye_type | ok. Q/C only. |
| 45 | Dicentra diel | ok on Q/C. No own diel search (budget). |
| 46 | Dicentra eye_type | ok. Q/C only. |
| 47 | Dicentra sense_chemical | ok. Own search returned the UW DICU protocol, the Korean D. spectabilis (Lamprocapnos) abstracts and Hidayati et al. 2000 (Sambucus; scholars.uky.edu opened). No Dicentra trial. The unit was right to keep the Lamprocapnos papers out. |
| 48 | Dicentra sense_light_nonvisual | ok. Same search. |
| 49 | Lathyrus diel | ok. Two own searches returned seed-company pages, a Lathyrus odoratus volatile-distribution paper (PMC11644040, no timing) and general reviews. |
| 50 | Lathyrus eye_type | ok. Q/C only. |
| 51 | Actaea diel | ok. Own search returned the Oenothera phenology paper (DOAJ opened) and garden pages; no Actaea hour. |
| 52 | Actaea eye_type | ok. Q/C only. |
| 53 | Centranthus eye_type | **error: unsupported chased** (above). |

**Search-record errors: 5 of 53 (9.4%): lines 33, 34, 35, 36, 53.**

## Wanted lines (faults listed, not counted)

- Line 16 (Robinson et al. 2019): the NC A&T profile page (opened) gives Julia Charlotte Robinson, Guochen Yang, Sanjun Gu, Zhongge Lu; HortScience 54(12): 2178-2181; 10.21273/HORTSCI14472-19; shade 0, 40, 60 and 80%. All match.
- Line 17 (Lathyrus aphaca 2019): the DOI 10.1590/s0100-83582019370100048 and the year 2019 match the gresis.osc.int record (opened). The SciELO abstract (opened) shows no authors and carries the light sentence the line cites. **Flagged: DOI with empty authors.** The journal field is empty, though the DOAJ search result titles it Planta Daninha (Jun 2019). The DOAJ page itself failed to open.
- Line 12 (Baskin and Baskin 1989): Can J Bot 67(7): 2131-2134, 10.1139/b89-269 (scholars.uky.edu opened). Matches.
- Line 15 (Zangerl and Berenbaum 1998): Chemoecology 8(4): 187-193, 10.1007/s000490050024 (experts.illinois.edu opened). Matches.
- Lines 1, 2, 7, 9 and 14 have a DOI and empty authors (flagged, not errors). Lines 1 to 11 and 13 were not checked against a page.

## Other faults (not counted)

- The branch adds an empty file, docs/views/evidence/-h.jsonl. It should not be merged.
- Thlaspi is in queue batch 24, but the progress note neither screens it nor lists it as skipped.

## Counts

- Search records: 5 of 53, 9.4%.
- Evidence: 0 of 7.
- Unit: 5 of 60, 8.3%.

Pooled with audits 83 to 90, from audit 90's figures as written (48 in 1026 search records; 52 in 1090 with evidence), as audits 122 and 123 did:
- Search records: 53 in 1079, 4.9%.
- With evidence included: 57 in 1150, 5.0% (4.96%).

Fork on chased (not counted). The brief accepts a web-found family-review DOI for genera in no harvest run. Knautia (lines 1 and 2) and Asimina (line 3) are harvest genera whose harvest family reviews ran (43 and 47 works printed) without the chased DOI. If the desk confines web-found DOIs to no-run genera, those three lines become errors too: 8 of 53 (15.1%). The verdict is unchanged either way.

**Verdict: fail (search records 9.4%, above 5%).** The unit was judged whole, so drop the error lines and the rest stands.

**Error lines to drop:**
- docs/views/searched/desk-d33.jsonl: lines 33 (Barbarea sense_chemical; missed Liu et al. 2016), 34, 35, 36 (Carduus; unsupported chased) and 53 (Centranthus; unsupported chased).
- docs/views/evidence/desk-d33.jsonl: none.

Leads for a later unit: Liu et al. 2016 (Barbarea vulgaris sense_chemical); the five-weed-species germination paper (plantarum 386) for Sherardia; Kafle et al. 2025 for Anaphalis; Holloway 2011 for Actaea rubra sense_chemical; the unsourced Wikipedia statement on Drosera cuneifolia flower opening.

## Pages opened

- kysu.edu PomperJ02.pdf; scholars.uky.edu (Finneseth 1998; Baskin 1989; Hidayati 2000); docs.lib.purdue.edu AAI8407542; acta.mendelu.cz acu-201103-0011; koreascience JAKO201620836727717; ashs.confex.com 2012 Paper10060; core-cms.cambridgecore.org (Qi and Upadhyaya); en.wikipedia.org Thalictrum_rochebruneanum and Drosera_cuneifolia.
- POWO 17145680-1, 10135-1, 672659-1, 17420090-1, 247264-2, 714359-1.
- doaj.org (Liu 2016; Fung and Thomson 2017; Penstemon 2023; Oenothera 2018); pherobase E/17705 and N/718; eflorasys 123164; nepjol 78187; eeb.lu.lv Necajeva; agris (Skarpaas 2001); experts.nau.edu (Aslan 2015); link.springer.com s00709-018-1274-5; catalog.lib.kyushu-u.ac.jp p307.pdf; uaf.edu Holloway Note 43; eprints.whiterose 114205; core.ac.uk 8441522; profiles.ncat.edu (Robinson 2019); scielo.br (Lathyrus aphaca); gresis.osc.int mj3f7-r6846; experts.illinois.edu (Zangerl 1998); frontiersin.org fpls.2016.00462 text.
- Refused or failed: POWO 714828-1 (permission not answered, not retried) and 714852-1 (site error); omorika 677 and plantarum 386 (human check); enauka.gov.rs (maintenance); pmc.ncbi.nlm.nih.gov PMC2735313 (browser check); bioone pages for Aslan 2015 (no text); doaj b2ca00fb (site error); katalog.lib.cas.cz (bot check); works.bepress.com redirect and the ncbi PMC4829607 redirect (not followed).
