# Audit 88: desk-c11 (12 plant genera; branch origin/research/desk-c11, head dccf0f78)

## Samples (seed 88), drawn before any record was read

Search records (29 lines): `random.seed(88)`, `random.sample(range(1, 30), 20)`, sorted: 1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 17, 18, 19, 21, 24, 26, 27, 28.

Evidence records: all 8 lines of docs/views/evidence/desk-c11.jsonl are judged.

## Gate

`python3 -I tools/views/screen_candidates.py --check docs/views/searched/desk-c11.jsonl --wanted docs/views/wanted/desk-c11.jsonl` prints "0 problems".

## Method

Judged against desk-audit.md, desk-screen.md points 1 to 10 (the owner's readings 10(a) to 10(e) included) and the rulings of audits 84, 86 and 87 named in the launch prompt: an unlabelled direct OpenAlex query line is waived (audit 84); a `chased` family-review DOI found by a labelled web search is accepted for genera in no harvest run (audits 86, 87); a `chased` DOI that no harvest or web search supports is an error.

Queries. `harvest_get.py` ran without the network. Five genera are in harvest runs: Foeniculum, Hypochaeris, Tecoma, Achillea, Apocynum. A script compared each of their records' unprefixed `queries` with every `query` and `family review` line the output prints (lines 1 to 4, 17, 18, 21, 22, 25 to 27): all match word for word and in order (Foeniculum 11, Hypochaeris 7, Tecoma 11, Achillea 4, Apocynum 13), with the "web: " lines after them. No harvest shows a failed step. The other seven genera are in no harvest run and list "web: " lines only. No unlabelled line appears.

Chased. Harvest-genus records name exactly the citation-step DOIs the output prints (Foeniculum 10.1111/ele.12205; Hypochaeris and Achillea 10.1016/j.tree.2009.09.010, Achillea also 10.1126/science.aaf9793; Tecoma 10.1603/022.038.0629 and 10.1111/een.12947; Apocynum 10.1002/ece3.71923). The Poaceae and Asteraceae no-run records name 10.1007/s44372-025-00446-3: my own WebSearches "Poaceae photoreceptor review" and "Asteraceae photoreceptor review" both returned link.springer.com/article/10.1007/s44372-025-00446-3 second on the first page, so it is supported as in audits 86 and 87. Nasturtium names PMC9369451: my "Brassicaceae photoreceptor review" search returned it first. Mahonia gives a reason (none found), which my searches do not contradict.

Searches. I ran about 75 WebSearches: 17 for evidence and taxonomy, 3 for family reviews, 3 for wanted lines, 3 pooled focusing searches for the eight eye_type records, and two or more of my own (genus and common name, plus germination, hormone or anthesis searches under 10(e)) for every other record. I fetched only URLs my searches returned. One permission request (ia902800.us.archive.org biostor-137766) went unanswered and was not retried; PMC table PMC10818387 and plantarum.izbis.bg.ac.rs served bot checks. No ResearchGate, academia.edu (one andhrauniversity.academia.edu result was left alone), Sci-Hub, LibGen or proxy page was opened, and no paper text is committed.

Extension. The sample of 20 holds exactly one error (line 4), 5.0%, which desk-audit.md step 5 leaves undecided. The extension draws 15 more; only 9 lines were left (2, 9, 14, 16, 20, 22, 23, 25, 29), so all 9 were judged, and the whole file of 29 is now judged.

## Search record verdicts (sample of 20)

| Line | Record | Verdict |
|---|---|---|
| 1 | Foeniculum diel | ok. Queries match. My searches returned Denisow and Anton 2012 on Aquilegia (Acta Agrobot 65(1), opened: hours for Aquilegia only), onion and dragon-fruit floral biology (Mysore J Agric Sci, opened) and gene-bank pages. No fennel opening hour. |
| 3 | Hypochaeris eye_type | ok. Queries match. The Tagetes macular review and the general focusing set are rightly screened; my pooled searches returned only the general set (PMC8309337, FIU cas_bio/44, nature.com 075535b0). |
| 4 | Hypochaeris sense_chemical | ERROR (missed measurement). Queries match, chased supported. My search "Hypochaeris radicata germination gibberellin OR smoke OR nitrate" returned first Wala, Kolodziejek and Patykowski 2021, PLOS ONE 16(1), e0244737, "Nitrogen signals and their ecological significance for seed germination of ten psammophilous plant species" (ideas.repec.org page opened): H. radicata seed was germinated on KNO3, NH4NO3 and NH4Cl at four concentrations, and the abstract states it "had no preference and wide tolerance to the type of nitrogen-containing compound". Nitrate is one of the germination cues 10(e) names, and main logs KNO3 germination under sense_chemical (Rumex confertus). |
| 5 | Sorghastrum diel | ok. Web-only, chased supported. My three searches returned iDigBio specimen records, the USGS plant ID page, cultivar patents and the Setaria anther-timing paper (Desai et al. 2018, Front Plant Sci, opened: Setaria only). No Indiangrass hour. |
| 6 | Sorghastrum eye_type | ok. Web-only. My grass bulliform-cell search returned leaf-anatomy papers on other grasses; nothing on Sorghastrum focusing. |
| 7 | Packera sense_light_nonvisual | ok. Web-only. My searches returned the Leverett ECU thesis the record names (cold stratification only), nursery pages, and nothing on light under the older Senecio names (Senecio aureus, obovatus, tomentosus: seed-shop and Brazilian Senecio pages). |
| 8 | Packera diel | ok. Web-only. My searches returned sunflower circadian anthesis work (Helianthus) and nursery pages; no Packera hour. |
| 10 | Packera sense_chemical | ok. Web-only. My germination-chemical and jasmonate searches returned Themeda, Lima bean and general smoke papers; no Packera. |
| 11 | Cortaderia diel | ok. Web-only. My searches returned extension, weed and garden pages with seasons only. |
| 12 | Cortaderia eye_type | ok. Web-only. Pooled focusing searches returned nothing on Cortaderia. |
| 13 | Cortaderia sense_chemical | ok. Web-only. My searches returned two C. selloana germination studies: the Sardinian wetland study (core.ac.uk 54593875, opened: temperature and NaCl only) and Lazaro-Lobo et al. 2024, Plant Stress 12: 100483 (DOAJ opened: temperature, waterlogging, drought, seed mass). Salinity tolerance is not a cue main logs under sense_chemical. No hormone, nitrate or smoke trial. |
| 15 | Nasturtium eye_type | ok. Web-only, chased supported. Pooled focusing searches returned nothing on watercress. |
| 17 | Tecoma eye_type | ok. Queries match. The rod-opsin and carpenter-bee works are rightly screened; pooled searches returned the general focusing set. |
| 18 | Tecoma sense_chemical | ok. Queries match. The screened florivory paper (10.3389/fpls.2022.813418) is on Pyrostegia venusta (UNESP record opened). My searches returned two T. stans germination studies, Vargas-Figueroa and Torres-Gonzalez 2018 (Rev Biol Trop 66(2), redalyc opened) and Socolowski, Vieira and Takaki 2008 (Braz Arch Biol Technol 51(4), SciELO opened); both test light and temperature only, a sense_light_nonvisual matter not open in this unit. An Addis Ababa GA3/KNO3 thesis is on Hagenia (opened). No Tecoma chemical response. |
| 19 | Cosmos diel | ok. Web-only. My searches returned sunflower circadian work, an Illinois weed page and NParks; no Cosmos opening hour. |
| 21 | Achillea diel | ok. Queries match. My searches returned Achillea cultivar patents and herbarium pages; no hour of opening. |
| 24 | Mahonia eye_type | ok, with a fork (below). Web-only. Pooled searches returned nothing on Mahonia focusing. |
| 26 | Apocynum eye_type | ok. Queries match. The screened BHL books and the battery paper are rightly screened; nothing on Apocynum focusing. |
| 27 | Apocynum sense_chemical | ok, with a lead. Queries match. Honey volatiles are rightly screened as a processed product. My searches returned a rice jasmonate seed treatment, a Populus MeJA study (both opened, no Apocynum) and a DePauw student poster, Claypool, Douglas and Keith 2022, "Latex Induction and Effects of Herbivory on Apocynum cannabinum" (opened): its abstract states the aim and gives no result, so it is a wanted-list lead, not a missed measurement. |
| 28 | Bromus diel | ok, with a lead. Web-only. My search "Bromus inermis anthesis time of day hours pollen shedding" returned Jones and Newell 1946, "Pollination Cycles and Pollen Dispersal in Relation to Grass Improvement", Nebraska Agric Exp Stn Res Bull 148 (digitalcommons.unl.edu ardhistrb/206, opened). Its abstract states the aim "to determine the time of day and the number of days that certain grasses shed pollen" and lists bromegrass among the keywords, but names no species or hour, and I could not open the bulletin. Grass pollen shedding marks floret opening, so this probably holds a Bromus inermis hour; I count it as a lead. |

Sample of 20: 1 error (line 4), 5.0%.

## Search record verdicts (extension: the 9 lines left)

| Line | Record | Verdict |
|---|---|---|
| 2 | Foeniculum eye_type | ok. Queries match; nothing on fennel focusing. |
| 9 | Packera eye_type | ok. Web-only; nothing on Packera focusing. |
| 14 | Nasturtium diel | ok. Web-only. My searches returned Silva et al. 2011 on Tropaeolum majus (An Acad Bras Cienc 83(4), redalyc opened: "anthesis is diurnal", no hour, and another genus), a variety-testing protocol and flora pages. No watercress hour. |
| 16 | Nasturtium sense_chemical | ERROR (missed measurement). My search "Nasturtium officinale seed germination gibberellin OR nitrate OR light dark" returned first Al-Awad, Hamami and Ibrahim, Latakia University Journal (Biological Sciences) 33(3) (journal.latakia-univ.edu.sy article 6174, opened; the page gives 2019 as the publication date and 2011 for the issue). Watercress seed from four Syrian sites was germinated in GA3 at several concentrations, and 0.1 mg/L gave 88.33% (Btara) and 86.66% (Sargon) in light at 20 C. An applied-hormone germination trial on a named species is a sense_chemical measurement under 10(d) and 10(e). The same search also returned elicitor work on watercress microshoot cultures (PMC8763773, not opened), which the excised-tissue precedent of audit 81 would leave out. |
| 20 | Cosmos eye_type | ok. Web-only; nothing on Cosmos focusing. |
| 22 | Achillea eye_type | ok. Queries match; nothing on Achillea focusing. |
| 23 | Mahonia sense_light_nonvisual | ok, with the fork below. Web-only. My search returned the same flora and seed pages; the UW student protocol for M. aquifolium (opened) holds no light test, only habitat notes on shade tolerance. |
| 25 | Apocynum diel | ok. Queries match. My searches returned the Setaria, Aquilegia and dragon-fruit papers and dogbane extension pages; no hour of opening. |
| 29 | Bromus eye_type | ok. Web-only. The Bromus stem anatomy paper is rightly screened; nothing on focusing. |

Extension: 1 error in 9 (line 16).

Fork on Mahonia (not counted in the search records). POWO 31334-2 (opened) accepts Berberis aquifolium Pursh with Mahonia aquifolium as a homotypic synonym, and the Wikipedia genus page (opened) says most sources since 2023, POWO and WFO included, sink Mahonia into Berberis. The queue lists Mahonia and Berberis as separate genera, so lines 23 and 24 do what the queue asks, and I count them as ok. If the desk follows POWO for the queue too, the Mahonia cells belong under Berberis and lines 23 and 24 should be held.

## Evidence record verdicts (all 8)

| Line | Record | Verdict |
|---|---|---|
| 1 | Foeniculum vulgare sense_chemical | ok. link.springer.com 10.1007/BF00025215 opened: Thomas 1994, Plant Growth Regul 14(2): 139-143; all three varieties responded to GA4/7 solutions with higher germination in light at 20 to 30 C. Living seed, applied hormone (10(d)); grade m. Accepted status of F. vulgare was not re-read in POWO. |
| 2 | Tecoma stans diel | ok. threatenedtaxa.org JoTT 322 opened: Jonathan, Raju, Branham, Devi 2009, 1(2): 126-127, 10.11609/JoTT.o1871.126-7; "two anthesis schedules in a day", 0500-0800 and 1500-1700 hrs. Accepted status of T. stans was not re-read in POWO. |
| 3 | Achillea collina sense_chemical | ok. expertise.unimi.it 249132 opened: Manzo, Panseri, Giorgi 2013 (congress abstract); the quote is verbatim. Aphid- and jasmonic acid-induced emission of living plants (10(a), 10(d)). POWO (ipni 60477838-2, opened): Achillea collina accepted. |
| 4 | Achillea fragrantissima sense_light_nonvisual | ok. agjsr.agu.edu.bh paper 360 opened: Al-Charchafchi, Clor, Jawad 1986, 4(1): 22-31; the quote is verbatim. POWO 173984-1 (opened): accepted. |
| 5 | Mahonia aquifolium sense_chemical | ERROR (taxon). The value and quote hold (idpan.poznan.pl vol-74/74-149-155 opened: Pipinis et al. 2015, Dendrobiology 74: 149-155, DOI 10.12657/denbio.074.015 on the page). But POWO 31334-2 (opened) gives "Berberis aquifolium Pursh ... This species is accepted" with Mahonia aquifolium (Pursh) Nutt. as a homotypic synonym, and Berberis is a separate genus in queue.jsonl (Berberis thunbergii). By the audit 86 Eupatorium ruling the record logs a synonym of another genus. |
| 6 | Apocynum venetum sense_light_nonvisual | ok. PMC8248540 opened: Jiang, She, Tian, Tanveer, Wang 2021, 10.3389/fpls.2021.671157; the quote is verbatim. WFO 0000245931 (opened): accepted. Light against darkness (10(d)). |
| 7 | Bromus sterilis sense_light_nonvisual | ok. agriculturejournals.cz PSE 2024 70(5): 287-295 opened: seven authors as recorded, 10.17221/21/2024-PSE; the quote is in the abstract. POWO (Anisantha sterilis page, opened): "This name is a synonym of Bromus sterilis", so Bromus is the accepted genus. |
| 8 | Bromus auleticus sense_chemical | ok. inia.uy Gonzalez-and-Condon-2020.pdf opened: title "Germination of Bromus auleticus after different treatments to release seed dormancy", Silvana Gonzalez and Federico Condon, Seed Sci Technol 48(1): 27-31, 2020, DOI 10.15258/sst.2020.48.1.04. The rebuilt title, authors, year and DOI all match. The quote is verbatim; GA3 0.05% MGT 17.2 d against 19.2 d control and KNO3 alone not uniform across lots, as the value says. The POWO page for B. auleticus (ipni 393544-1, returned by my search) failed at its site, so its status was not read; no source I saw treats it under another genus. |

Evidence errors: 1 of 8 (line 5, taxon), 12.5%. All values come from abstracts and are marked `partial`; quotecheck against full texts has not been run.

## Counts

- Search records, sample of 20: 1 error, 5.0%, undecided under step 5.
- Search records, all 29 (20 plus the 9 of the extension): 2 errors, 6.9%.
- Evidence: 1 of 8, 12.5%.
- The unit as judged: 3 errors in 37, 8.1%.

Pooled with the desk's other audits of desk-screen units, using audit 87's figures as written (39 search-record errors in 965; 41 in 990 with the evidence samples):
- Search records: 41 in 994, 4.1%.
- With the evidence: 44 in 1027, 4.3%.

Two forks would change the count:
1. Bromus diel (line 28). If the desk counts Jones and Newell 1946 as a missed measurement, line 28 becomes an error: 3 in 29 search records (10.3%).
2. Mahonia. The evidence error at line 5 follows the audit 86 Eupatorium ruling. If the desk keeps Mahonia as the queue's genus, line 5 is ok (0 of 8), and the unit has 2 in 37 (5.4%).

**Verdict: fail.** The 29 search records hold 2 errors (6.9%), above the 5% line. Since every search record and every evidence record has been judged, dropping the error lines leaves 27 search records and 7 evidence records with no known error.

**Error lines to drop:**
- docs/views/searched/desk-c11.jsonl: lines 4 and 16.
- docs/views/evidence/desk-c11.jsonl: line 5 (or move it to Berberis aquifolium if the desk files it there).

## Wanted lines (listed, not counted)

- Line 1, Emal 1971: digitalcommons.unl.edu archivaltheses/867 (opened) gives James G. Emal, December 1971, M.S. thesis, University of Nebraska-Lincoln, and no DOI. The record matches.
- Line 2, Jani and Mankad: indianbotsoc.org article 322 (opened) gives Goral Jani and Archna Mankad, no year, no DOI, and 87(3&4) 162-169 from the PDF file name. The record matches; the year stays empty.
- Line 3, Bromus 2003: cris.bgu.ac.il (opened) gives Israel J Plant Sci 51(4): 267-273, 1 December 2003, no authors and no DOI value. The record matches.

## Leads

- Bromus inermis diel: Jones and Newell 1946 (above).
- Apocynum cannabinum sense_chemical: Claypool, Douglas and Keith 2022 poster on herbivory and latex induction (above).
- Nasturtium officinale sense_chemical: elicitor treatment of watercress microshoot cultures (PMC8763773), if the desk admits in-vitro shoots.
- Hypochaeris radicata and Nasturtium officinale sense_chemical: the two works behind the errors are ready to log as evidence.
- Bromus japonicus light: "Influence of storage, temperature, and light on germination of Japanese brome seed" (repository.arizona.edu 10150/644420, not opened), for a Bromus cell already closed in this unit.
