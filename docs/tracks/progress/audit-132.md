# Audit 132: desk-d42 (14 plant genera; branch origin/research/desk-d42, head 1ebcdb2e)

## Lines judged

- Sample drawn first: `random.seed(132)`, `random.sample` of 20 from the 35 search records: lines 1, 2, 4, 6, 7, 8, 9, 10, 13, 15, 18, 21, 25, 27, 29, 30, 31, 32, 34, 35. The sample held errors, so I extended the check to all 35 lines.
- Evidence records: all 5 lines of docs/views/evidence/desk-d42.jsonl.
- Wanted lines: all 8. I list them and do not count them.

## Gate

I ran `python3 -I tools/views/screen_candidates.py --check` on a copy of the searched file (35 lines) with the wanted file (8 lines). It prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10, the counting rule of audit 39, audits 86 to 90, and the rulings in the launch prompt.

**Queries.** `harvest_get.py` reads origin/ci. Only Campanulastrum (run 6) and Castanea (run 4) are harvest genera. A script compared the unprefixed queries of lines 1 to 4 with every `query` and `family review` line the harvest prints. All four match word for word and in order (13 of 13), with the "web: " lines after them. The other 12 genera are in no harvest run and list "web: " lines only.

**Chased.**
- Campanulastrum (lines 1 and 2) names 10.1093/jxb/eru327. That DOI is printed in the harvest's own "Campanulaceae photoreceptor review" output.
- Castanea (lines 3 and 4) names the two citation-step DOIs the harvest prints, and its family review DOI 10.3390/urbansci9010014 is printed under "Fagaceae photoreceptor review".
- For genera in no harvest run, I re-ran the labelled family searches:
  - "Orchidaceae photoreceptor review", "Poaceae photoreceptor review" and "Asteraceae photoreceptor review" each return link.springer.com 10.1007/s44372-025-00446-3 on the first page. This supports lines 5, 6, 10, 11, 21 to 24, 29, 30, 34 and 35.
  - "Fabaceae photoreceptor review" returns 10.1093/jxb/erag313 first (citedrive page). This supports lines 25 and 26.
- Sanicula (7 to 9) and Tiarella (14 to 16) name a genus paper with a "no family review" reason. Chamaedaphne (12 and 13) names Densmore 1997. Menyanthes, Tribulus and Tellima give "none" reasons.
  - Tribulus and Tellima say plainly that no family search was run.
  - Tiarella says "No family review found for Saxifragaceae", but its `queries` hold no Saxifragaceae search. That reason is unsupported. It is listed as a fault and not counted, since the rulings address that claim only for harvest genera.

**Main (928533ee).** I checked docs/views/evidence/*.jsonl for every genus in the unit.
- Main holds Castanea sense_chemical and sense_light_nonvisual, Chamaedaphne light (Densmore 1997), Echinochloa chemical and light, Hieracium diel (H. umbellatum), Schizachyrium light, Mimosa sense_touch, and Campanula americana light (Koutsovoulou 2014).
- No search record nulls a trait that main holds evidence for.
- No evidence record repeats a main (paper, quote, species, trait) line.

**Searches.** I ran about 50 WebSearches:
- 9 for the evidence sources and POWO names;
- 4 for family reviews;
- one or more of my own for each genus and trait, using the germination light/dark, GA3/smoke/nitrate and anthesis phrasings;
- 3 for wanted lines.

I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and a springerlink.bibliotecabuap.elogim.com result was left alone. No paper text is committed.

## Evidence record verdicts (5)

| Line | Record | Verdict |
|---|---|---|
| 1 | Campanulastrum americanum sense_light_nonvisual | ok. I opened the UMN Experts page: Etterson and Galloway 2002, Am J Bot 89(12): 1899-1906, 10.3732/ajb.89.12.1899. The quote is verbatim, one sentence of 102 characters, and states the study's own result. Two set light levels on living clones count under 10(d). POWO has a page for Campanulastrum americanum (L.) Small (43996-2), and Campanula americana is the basionym. Main's Campanula americana line is a different paper (Koutsovoulou 2014). |
| 2 | Hieracium (genus) sense_chemical, grade g | **error: genus-level although the abstract names species.** I opened the herbmedit page: Di Gristina, Varshanidze, Domina 2020, Fl Medit 30: 431-437. The quote is verbatim (97 characters) and reports a result. But the abstract names the three Hieracium taxa it tested: H. hypochoeroides subsp. cilentanum, H. schmidtii subsp. nebrodense and H. terraccianoi, all filed under Hieracium. Under the ruling in force, a genus-level record from an abstract that names its species is an error. The record should be per species (with grade g if the pooled sentence is kept). Separately, the GA3 sentence only says germination was "similar" to the controls, so it reports no response to GA3. Fork below. |
| 3 | Chamaedaphne calyculata sense_chemical | ok. I fetched the koreascience PDF (CFKO202335557781139): Jo, Choi, Sung, Yoon 2023. A character-by-character comparison found the Korean sentence "GA3 1000mg·L-1 처리에서의 최종발아율(FGP)은 25/15°C, 15/6°C 각각 42.2%와 30.0%를 보여 무처리구 보다 각각 17.8%, 20% 높게 나타났다." identical to one whole sentence of the abstract's results. The only difference is a layout line break after "(FGP)". It is 99 characters, at most 125. The dose unit (mg·L-1, recorded as mg/L) is copied correctly. The pdf could not be read directly (proxy 403 on curl), so this rests on WebFetch's comparison. |
| 4 | Mimosa pudica sense_light_nonvisual | ok. I opened the MDPI page: Kumar, Singh, Bhatt, Sharma, Sharma, Soni 2022, Physiologia 2(4): 132-153, 10.3390/physiologia2040012. The quote is verbatim except that the page has a curly apostrophe in "plants’" (typographic). It is 90 characters and states a result. Light quality and photoperiod on a living plant count under 10(d). |
| 5 | Schizachyrium scoparium sense_chemical | ok. I opened the MSpace page: Watts 2001, MSc thesis, University of Manitoba (issued 2001-05-01). The quote is verbatim (112 characters). The doses are 0.5% KNO3 and water, as recorded. KNO3 priming counts under the ruling. The water and KNO3 soaks were equally effective, which the note says. |

Evidence errors: **1 of 5 (20%)**, line 2.

## Search record verdicts (35; sampled lines marked *)

| Line | Record | Verdict |
|---|---|---|
| 1* | Campanulastrum diel | ok. Queries and chased match the harvest. My search for C. americana flower opening returned Evanhoe and Galloway 2002 on floral longevity (besnet page opened): gender phases in hours after onset, with no opening hour. |
| 2* | Campanulastrum eye_type | ok. The pooled focusing search returned only the general set (FIU cas_bio/44, PMC9824129, Nature 075535b0). |
| 3 | Castanea diel | ok. Queries and chased match the harvest. My pollen-release and scent-rhythm searches returned only the general scent-rhythm review (PMC4829607), phenology pages and a Mesua ferrea Aerobiologia paper (opened, not Castanea). |
| 4* | Castanea eye_type | ok. The pooled focusing search found nothing on Castanea. |
| 5 | Hieracium eye_type | ok. The chased DOI is supported, and nothing on focusing came back. |
| 6* | Hieracium sense_light_nonvisual | ok. My light/dark search returned Bear et al. 2012 (Pilosella taxa, rightly excluded), the Di Gristina paper (no light treatment) and eflorasys pages for H. murorum and H. umbellatum (opened: germination fields blank). |
| 7* | Sanicula diel | ok. No opening hour came back. |
| 8* | Sanicula eye_type | ok. |
| 9* | Sanicula sense_chemical | ok. My GA3 search returned the Hawkins et al. 2010 abstract (scholars.uky and treesearch 36275 opened): stratification only, no GA3, smoke or nitrate. The other hits were core 132093023 (other genera) and the Holloway note (no Sanicula). |
| 10* | Eriophyllum diel | ok. Flora and USDA pages only. |
| 11 | Eriophyllum eye_type | ok. |
| 12 | Chamaedaphne diel | ok. My search returned Źróbek-Sokolnik et al. 2019, Plants 8(5): 129 (MDPI opened). It gives the flowering period only, with no hour. |
| 13* | Chamaedaphne eye_type | ok. |
| 14 | Tiarella diel | ok. No opening hour found. The chased reason claims a Saxifragaceae search that was not run (fault, not counted). |
| 15* | Tiarella eye_type | ok, with the same chased fault. |
| 16 | Tiarella sense_light_nonvisual | ok. Choi et al. 2018 (koreascience opened) uses a 16 h photoperiod only as the incubation condition, with no light/dark comparison. Other hits were nursery pages. |
| 17 | Menyanthes diel | ok. |
| 18* | Menyanthes eye_type | ok. |
| 19 | Menyanthes sense_chemical | ok. My germination search returned the eflorasys page (opened: blank fields), the Haraguchi PDF and the protocol. No GA3, smoke or nitrate trial. |
| 20 | Menyanthes sense_light_nonvisual | **error: a screened work reports the measurement.** The record screens Martz et al. 2009 because "no abstract sentence of at most 125 characters" gives the result. The AGRIS page (opened) is Martz, Turunen, Julkunen-Tiitto, Lakkala, Sutinen 2009, Environ Pollut 157(12): 3471-3478. It reports that UVB exclusion in field plots "significantly decreased the proportion of flavonols" in Menyanthes trifoliata leaves and raised iridoids. That is a living plant's response to a light treatment. A quote problem sends the work to the wanted list (point 3); it does not support a null. The unit's own progress note admits the work was screened only for quote length. |
| 21* | Corallorhiza diel | ok. |
| 22 | Corallorhiza eye_type | ok. |
| 23 | Corallorhiza sense_chemical | ok. Only Arum and flora pages came back. |
| 24 | Corallorhiza sense_light_nonvisual | ok, with a lead. The NU record of McKendrick et al. 2000 (opened) is field packets with no light treatment. The APPS 2022 Spiranthes paper (DOAJ opened) and the Liparis paper (abs.ek.szte.hu opened) are other genera. PMC6408697, which my search also returned, served a bot check, so it remains unread. Fork below. |
| 25* | Mimosa diel | **error: missed measurement.** My search "Mimosa floral biology anthesis hours..." returned Carvalho 2022 (UFMS TCC, repositorio.ufms.br 123456789/9306, opened). Its English abstract says the flowers of Mimosa paludosa Benth. open "at dawn (before 5:30 am)". That is flower opening time in a species of the genus. POWO lists the name; it may be treated as Mimosa setosa var. paludosa, which is still Mimosa. |
| 26 | Mimosa eye_type | ok. |
| 27* | Tribulus diel | **error: missed measurement.** My search returned Suvarna Raju and Solomon Raju 2023, J Threat Taxa 15(5): 23279-23282 (threatenedtaxa.org PDF opened): "T. terrestris flowers open after sunrise from 0600 to 0800 h", closing in late afternoon. |
| 28 | Tribulus eye_type | ok. |
| 29* | Schizachyrium diel | **error: unread candidate nulled (point 3).** The record says archive.org biostor-137766 was returned for its anthesis search and was blocked. My exact-phrase search for "Echinochloa" and "Andropogon scoparius" with "time of anthesis" returned that PDF first. A search on barnyard grass spikelets opening at set hours returned it first again. It is very probably a table of grass anthesis hours naming both species. A work that may hold the measurement keeps the trait out of the record and goes on the wanted list. My fetch was refused too (permission unanswered). Fork below. |
| 30* | Schizachyrium eye_type | ok. |
| 31* | Tellima diel | ok. Only nursery and flora pages came back. The Greya papers the record screened are on Lithophragma. |
| 32* | Tellima eye_type | ok. |
| 33 | Tellima sense_light_nonvisual | ok. Nursery and protocol pages only. |
| 34* | Echinochloa diel | **error: unread candidate nulled (point 3).** This is the same biostor-137766 case as line 29; the record names it as returned for two anthesis searches. Necajeva et al. 2022, Agron J 114: 3407-3419 (mku PDF opened), gives heading and daylength, not an hour. |
| 35* | Echinochloa eye_type | ok. |

Search record errors:
- In the 20-line sample: 4 of 20 (20%), lines 25, 27, 29 and 34.
- In all 35 lines: **5 of 35 (14.3%)**, lines 20, 25, 27, 29 and 34.

## Counts

- Search records: 5 of 35, 14.3%.
- Evidence: 1 of 5, 20%.
- Unit: 6 of 40, 15.0%.

Pooled with audits 83 to 90, from audit 90's closing figures (48 in 1026 search records, 52 in 1090 overall):
- search records: 53 in 1061, 5.0%;
- with evidence: 58 in 1130, 5.1%.

Forks that would change the count:
- Lines 29 and 34 (biostor-137766). If the desk counts only a measurement shown on a page I read, these two stand. Search records would then be 3 of 35 (8.6%), still a fail.
- Evidence line 2 (Hieracium). If the desk accepts a pooled genus-level g record when the abstract names several species (audit 131 raised the same fork), line 2 stands, and evidence is 0 of 5. Even then, its GA3 sentence reports no response ("similar" germination), so the sense_chemical cell rests on a null-effect sentence.
- Line 24 (Corallorhiza light). If PMC6408697 proves to be a Corallorhiza light trial, line 24 is a point-3 error too.

**Verdict: fail.** The search records fail at 14.3% and the evidence at 1 of 5. The whole unit was judged, so drop the error lines and the rest stands.

**Error lines to drop:**
- docs/views/searched/desk-d42.jsonl: lines 20, 25, 27, 29 and 34.
  - Line 20 reopens Menyanthes sense_light_nonvisual; Martz et al. 2009 belongs on the wanted list.
  - Lines 25 and 27 reopen Mimosa diel and Tribulus diel; the works above can close them.
  - Lines 29 and 34 reopen Schizachyrium diel and Echinochloa diel; biostor-137766 belongs on the wanted list.
- docs/views/evidence/desk-d42.jsonl: line 2.

## Wanted lines (listed, not counted)

1. Keeley and Nitzberg 1984 (BHL part 170935): not checked; my searches did not return its page.
2. Choi et al. 2018, 10.7732/kjpr.2018.31.4.363: koreascience page opened. The six authors in order, the year, KJPR 31(4): 363-371 and the DOI match, as do the GA3 figures (33.3% to 72.5%).
3. Camargo-Ricalde and Grether 1998: not checked.
4. Chauhan and Johnson 2009: pestinfo page opened. The authors, year, Weed Biol Manag 9(1): 38-45 and title match; no DOI is shown, and the line leaves the DOI empty.
5. Tabassum 2014: not checked. Tissue-culture explants may fall outside "living responses"; that is for the reader to judge.
6. and 7. The two Tribulus Vietnamese papers: not checked.
8. Holloway 2011, Georgeson Botanical Note 43: uaf.edu PDF opened. The author, year and note number match, and Tellima grandiflora sits under "Promotes germination, but specific reason unknown".

## Leads

- Menyanthes trifoliata sense_light_nonvisual: Martz et al. 2009 (10.1016/j.envpol.2009.06.022), UVB exclusion.
- Mimosa paludosa diel: Carvalho 2022 (UFMS TCC). Mimosa bimucronata (Silva et al. 2011, Planta Daninha 29) studies anthesis events, but its abstract gives no hour.
- Tribulus terrestris diel: Suvarna Raju and Solomon Raju 2023 (JoTT 15(5): 23279-23282).
- Schizachyrium and Echinochloa diel: archive.org biostor-137766, unread.
- Corallorhiza sense_light_nonvisual: PMC6408697, unread.
- Chamaedaphne calyculata: Źróbek-Sokolnik et al. 2019 states in its Discussion that germination "requires light", from unshown pilot data. Main already holds Densmore 1997.

## Blocked pages

- ia902800.us.archive.org biostor-137766 PDF: permission unanswered, not retried.
- pmc.ncbi.nlm.nih.gov PMC6408697: bot check.
- bindani.izt.uam.mx 3n203z237: binary data.
- koreascience.kr PDF by curl: proxy 403; WebFetch served it.
