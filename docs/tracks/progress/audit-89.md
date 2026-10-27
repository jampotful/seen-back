# Audit 89: desk-c9 (9 plant genera; branch origin/research/desk-c9, head 392e6f3a)

## Lines judged

No sample was drawn: the launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: all 11 lines of docs/views/searched/desk-c9.jsonl (1 to 11).
- Evidence records: all 23 lines of docs/views/evidence/desk-c9.jsonl (1 to 23). The progress note says 18; the file holds 23.
- Wanted lines: all 5, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (11 lines) and the wanted file (5 lines) prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e) included), and the rulings of audits 84, 86 and 87. Audit 88 is not on origin.

Queries. `harvest_get.py` ran without the network (it reads origin/ci). A script compared each record's unprefixed `queries` with every `query` and `family review` line the harvest prints for the genus. All nine records for harvested genera match word for word and in order, with the "web: " lines after them: Erigeron (lines 1, 2), Heterotheca (5), Prunus (6), Mirabilis (7), Nymphaea (8), Melia (9) and Polygonatum (10, 11). Colocasia (3, 4) is in no harvest run and lists "web: " lines only. No harvest shows a failed step, and no unlabelled line appears.

Chased. Every DOI named is printed by the harvest output for its genus.
- Erigeron, Heterotheca and Mirabilis name a citation-step DOI. Heterotheca and Mirabilis each name one of their two steps; the other steps returned 0 works. Mirabilis's step 10.3732/ajb.92.1.2 returned 2 works: a Springer book chapter and a regeneration paper, neither with optics.
- Prunus, Nymphaea, Melia and Polygonatum have no citation step. Each names the first work of its harvest family review. The unit itself calls these weak, but the output supports them.
- Colocasia gives a reason.

Screened. Every screened DOI or OpenAlex id is printed by the harvest output or listed by `screen_candidates.py`. W7220607642 is a Tagetes macular-health review, and W2099882410 is the Metasequoia leaf paper. I read them against titles and abstract starts. None holds a measurement of the record's trait in a species of the genus.

Searches. I ran about 50 WebSearches:
- 20 for evidence sources and taxonomy;
- 3 or more per diel record (Erigeron, Colocasia, Polygonatum);
- 4 for Heterotheca sense_chemical;
- 2 pooled focusing searches for the seven eye_type genera;
- 7 for wanted lines.

I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.

## Search record verdicts (11)

| Line | Record | Verdict |
|---|---|---|
| 1 | Erigeron diel | ok. Queries match (6 harvest, 8 web), and chased is the printed citation step. My searches returned flora, garden and phenology pages, and Lee and Kim 1991 on E. annuus (koreascience, opened), which gives months only. A blog post (birdsoutsidemywindow.org 2021, opened) observes E. philadelphicus and E. annuus heads closing at sunset and opening in the morning. It gives no clock time and cites no study, so I treat it as a lead (below), as audits 86 and 87 treated extension pages. |
| 2 | Erigeron eye_type | ok. Queries match. The Tagetes review carries the owner's wording. My pooled focusing searches returned only the general set (AskNature, FIU cas_bio/44, PMC9824129). |
| 3 | Colocasia diel | **error: missed measurement.** Web-only. Ivancic, Lebot, Roupsard, Quéro Garcia and Okpul 2004, "Thermogenic flowering of taro (Colocasia esculenta, Araceae)", Can J Bot 82(11): 1557-1565, 10.1139/b04-118. The abstract record I opened (portal.univ.edu.vu, from my search "thermogenic flowering of taro Colocasia esculenta Araceae Ivancic") gives timing. The inflorescence becomes fragrant on the night of the female phase, thermogenesis peaks at 05:00, and protogyny and pollination fall in the early hours of the day. That is scent and flower-phase timing in a named species, which the owner's reading counts under plant diel. The record's own diel search ("Colocasia OR taro flower opening time anthesis") did not surface it. A second hit, Naiola et al. (ISTRC 6th symposium, opened: "Anthesis began between 8:00 p.m. and 1:00 a.m."), is for Colocasia gigantea. WFO and POWO give that species as Leucocasia gigantea, another genus, so it is not counted here. |
| 4 | Colocasia eye_type | ok. Web-only, and the chased reason holds. Nothing on taro focusing came back. |
| 5 | Heterotheca sense_chemical | ok, with an open lead. Queries match (5 harvest, 3 web), and chased is a printed citation step. The ten screened works name no Heterotheca. My searches returned Flint and Palmblad 1978 on H. grandiflora (Oecologia 36: 33-43, Springer abstract opened: achene dimorphism, no chemical treatment), the EPPO summary of Quaye et al. 2011 (opened: temperature and burial only, and herbicide control rather than a germination cue), and a USDA GA paper on Helianthus, another genus. The Weed Science paper "Germination, growth, development, and control of camphorweed (Heterotheca subaxillaris)" came back again. cambridge.org refused my fetch (permission unanswered), as it refused the unit's, so whether it holds a chemical-cue result is unknown. Under desk-screen point 3 such a work belongs on the wanted list with the trait held out of the record. Audit rule 4 counts only a measurement shown to be missed, so I do not count it. |
| 6 | Prunus eye_type | ok. Queries match. Chased is the first work of the harvest's Rosaceae family review. My pooled search returned no Prunus focusing work. |
| 7 | Mirabilis eye_type | ok. Queries match (9 harvest, 5 web). The five screened works carry the owner's wording and none has Mirabilis optics. |
| 8 | Nymphaea eye_type | ok. Queries match. The hydropote papers (SciELO abb, which my search also returned) are gland ultrastructure with no optics. |
| 9 | Melia eye_type | ok. Queries match (12 harvest, 3 web). The screened works are pharmacology and cell papers, and chased is the printed Cedrela family-review work. |
| 10 | Polygonatum diel | ok. Queries match (13 harvest, 6 web). My searches returned three works with no hour of opening: the 2021 China J Chin Mater Med abstract on P. cyrtonema reproduction (bvsalud wpr-879007, opened: days and months only), Odintsova and Fishchuk 2017 on P. multiflorum (Acta Agrobot 70(1), opened: relative stages only), and the P. cyrtonema bee-efficiency paper (mdpi Biology 14(3): 276, opened: bee activity hours only). |
| 11 | Polygonatum eye_type | ok. Queries match, and nothing on Polygonatum focusing came back. |

Search record errors: **1 of 11 (9.1%)**, line 3.

## Evidence record verdicts (23)

Every line is graded m, partial and abstract-level. In each case I opened a page my search returned and found the quoted words and the value there.

| Line | Record | Verdict |
|---|---|---|
| 1 | Asclepias curassavica sense_chemical | ok. Dryad page opened: Meier and Hunter 2019. The quote is verbatim. The page names A. curassavica, A. incarnata and Aphis nerii. Herbicide-induced volatiles of living plants count under 10(a). |
| 2 | Asclepias incarnata sense_chemical | ok. Same page and sentence ("in both species"). |
| 3 | Asclepias syriaca sense_chemical | ok. Springer page opened: Agrawal, Hastings, Patrick and Knight 2014, J Chem Ecol 40: 717-729. The quote is verbatim, and herbivore-induced resistance counts. |
| 4 | Erigeron speciosus sense_light_nonvisual | ok. USU aspen bibliography page opened: Hoffman 1985, Bull Torrey Bot Club 112(4): 409-413. The words "germinated less in dark than in light" are there. |
| 5 | Erigeron canadensis sense_light_nonvisual | ok. Cambridge page opened: Nandula et al. 2006, Weed Sci 54(5): 898-902, and the quote is verbatim. POWO (opened) gives Conyza canadensis as a synonym of Erigeron canadensis. |
| 6 | Erigeron bonariensis sense_light_nonvisual | ok. Pestinfo page opened: Vidal et al. 2007, Planta Daninha 25: 309-315. "The species are positive photoblastic" covers both species. |
| 7 | Erigeron canadensis sense_light_nonvisual | ok. Same page. |
| 8 | Erigeron canadensis sense_chemical | **error: owner's reading.** DOAJ page opened: Follmer et al. 2021, Sci Rep 11, 10.1038/s41598-021-95164-7. The treatments are aqueous P, K, Ca and Mg nutrient solutions at two pH levels. A response to nutrient ions is excluded from plant sense_chemical, since it involves no hormone, elicitor, herbivore or volatile. The record also has two inconsistencies with the abstract. The quote (potassium "synergistic" on seedling development) does not support the value (phosphorus inhibiting germination). The abstract gives P as "~7 times" inhibition and "~4 times reduction". |
| 9 | Colocasia esculenta sense_chemical | ok. AGRIS page opened: Ferraren and Nunez 1991, and the quote is verbatim. GA3 applied to living plants counts under 10(d). |
| 10 | Colocasia esculenta sense_light_nonvisual | ok. Embrapa PDF opened: de Oliveira et al. 2004, shade at 0, 25, 50 and 75%. The quote is verbatim, and this is a set-light-intensity trial. |
| 11 | Melia azedarach diel | ok. Cambridge page opened: Mohapatra, Das, Kar and Das, Plant Genet Resour 23(1), 10.1017/S1479262124000376. The quote is verbatim (anthesis peaks 08:00 to 10:00). |
| 12 | Mirabilis jalapa sense_chemical | ok. DergiPark page opened: Hatipoğlu 2026, 10.38093/cupmap.1865903, and the quote is verbatim. |
| 13 | Nymphaea minuta sense_light_nonvisual | ok. ThaiJo page opened: Chittawanij et al. 2026, 10.22299/apst.2026.273811, which names N. minuta. Mix LED gave flowering at 54.75 days and white fluorescent at 75.00 days. The genus is right. My search returned a POWO entry for Nymphaea dimorpha I.M.Turner beside the N. minuta Wikipedia page, which suggests a replacement name. That is noted, not counted. |
| 14 | Nymphaea alba sense_light_nonvisual | ok. Avesis page opened: Sumlu, Atar and Khawar 2010, 24(1): 1582-1586. The quote is verbatim, and the page also gives the 2 to 3 times longer dark seedlings. |
| 15 | Nymphaea alba sense_chemical | ok. Same page. BAP+IAA failure and TDZ at 51.37% are verbatim, a growth-regulator response (10(d)). |
| 16 | Polygonatum odoratum sense_chemical | ok. KoreaScholar page opened: Kang et al. 1999, 7(1): 16-21. The quote is verbatim, and the Korean abstract gives 1.0 mM GA3. |
| 17 | Polygonatum cyrtonema sense_light_nonvisual | ok. PJB page opened: Liu et al. 2025, 57(3). The quote is verbatim, and both species are named. |
| 18 | Polygonatum sibiricum sense_light_nonvisual | ok. Same page. |
| 19 | Polygonatum cyrtonema sense_light_nonvisual | ok. CASB page opened: Tong, Zhang, Chen, Gao, Geng and Li 2020, 36(28): 84-91, with shade at 83, 61 and 38% transmittance. The quote is a list fragment rather than a sentence (requote, not counted). The page gives DOI 10.11924/j.issn.1000-6850.casb20191000697, which the record could carry. |
| 20 | Prunus cerasoides diel | ok. PPHouse page opened: Chauhan et al. 2025, 10.23910/1.2025.6130. Peak anthesis is 12:00 to 14:00 and "no anthesis between 6:00 pm to 6:00 am" is verbatim. |
| 21 | Prunus sellowii sense_light_nonvisual | ok. UFPR page opened: Rodrigues, Hirano and Nogueira 2008, 9(1): 91-94. The page gives 57% and 51%. |
| 22 | Prunus avium sense_light_nonvisual | ok. TÜBİTAK page opened: Bantis and Radoglou 2017, 41(2): 314-321, and the quote is verbatim. |
| 23 | Prunus spachiana sense_chemical | ok. DOAJ page opened: Kim et al. 2024, Plants 13(4): 502, and the quote is verbatim. |

Evidence errors: **1 of 23 (4.3%)**, line 8.

## Counts

- Search records: 1 of 11, 9.1%.
- Evidence: 1 of 23, 4.3%.
- Unit: 2 of 34, 5.9%.

Pooled with the desk's other audits of desk-screen units, using audit 87's figures as written (search records 39 in 965; with evidence samples 41 in 990):
- Search records: 40 in 976, 4.1%.
- With evidence included: 42 in 1024, 4.1%.

Forks that would change the count:
- If the desk reads the Ivancic et al. abstract as thermogenesis timing rather than flower-phase or scent timing, line 3 stands. Search records would then be 0 of 11.
- If the desk reads the Weed Science camphorweed paper as a work the record had to hold out under point 3, line 5 also fails.
- If the desk reads Follmer et al. as a germination cue (10(e) lists nitrate), line 8 stands on its trait but still needs a quote that supports its value.

**Verdict: fail.** Both whole files were judged, so drop the error lines and the rest of the unit stands. The evidence passes on its own (4.3%), and the search records fail (9.1%).

**Error lines to drop:**
- docs/views/searched/desk-c9.jsonl: line 3 (Colocasia diel). The cell reopens; Ivancic et al. 2004 (10.1139/b04-118) can close it.
- docs/views/evidence/desk-c9.jsonl: line 8 (Erigeron canadensis sense_chemical, Follmer et al. 2021). Erigeron sense_chemical then reopens, and wanted line 1 (10.1093/jxb/eraa124) is its lead.

## Wanted lines (listed, not counted)

- Line 1 (10.1093/jxb/eraa124, 2020): the DOI and title match papers.ecosyste.ms (opened). The authors field is empty, but that page gives McCauley, McAdam, Bhide, Thimmapuram, Banks and Young.
- Line 2 (Erschbamer et al. 2010, Ber nat-med Ver Innsbruck 96: 73-88): authors, year and pages match the zobodat PDF (opened). The PDF says E. uniflorus germinated better in light than in darkness, with values in figures only.
- Line 3 (Melia volkensii, 10.3390/plants15020322): my search returned PMC12844993 with this title. I did not open it (PMC reCAPTCHA), so the DOI is not checked.
- Line 4 (Mirabilis jalapa, Jurnal Bioshell, 10.56013/bio.v14i1.3530): my search did not return it, so it is not checked.
- Line 5 (Tyagi, Taylor and Deo 2004, S Pac J Nat Sci 22(1): 62-66): authors, year, volume and pages match the USP repository record (opened). That record gives no DOI. The DOI 10.1071/SP04007 matches the CSIRO URL my search returned (not opened).

## Leads

- Colocasia diel: Ivancic et al. 2004 (above).
- Leucocasia gigantea diel, if that genus is queued: Naiola et al. (ISTRC 6th symposium), "Anthesis began between 8:00 p.m. and 1:00 a.m.", and Ivancic et al. 2008, J Plant Res 121(1): 73-82 (title only, from the CIRAD list).
- Erigeron diel: the blog observation of E. philadelphicus and E. annuus heads closing at sunset (no clock time, no study).
- Heterotheca sense_chemical: the Weed Science camphorweed germination paper (cambridge.org C78A3028F1828E0730EB909329B0BADB), still unread.

## Blocked pages

- pmc.ncbi.nlm.nih.gov PMC8329304: permission unanswered, so I used DOAJ instead.
- bioone.org WS-06-006R2.1: served meta tags only, so I used Cambridge.
- cambridge.org camphorweed abstract: permission unanswered.
- sfb.univie.ac.at: redirected to a maintenance page.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
