# Audit 91: desk-d1 (8 plant genera; branch origin/research/desk-d1, head 25a5da54)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: all 13 lines of docs/views/searched/desk-d1.jsonl (1 to 13).
- Evidence records: all 10 lines of docs/views/evidence/desk-d1.jsonl (1 to 10).
- Wanted lines: all 7, listed and not counted.

Hemerocallis, Chromolaena, Cyanthillium, Hexastylis, Hypoxis, Cichorium and Larrea were not screened and are not under audit. Polystichum was screened but has no search record. That is allowed: main holds Polystichum sense_chemical (Hornych et al. 2021), and the unit wrote one wanted line for it.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (13 lines) and the wanted file (7 lines) prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e) included), the counting rule of audit 39, and the rulings of audits 84, 86, 87 and 90. Audits 89 and 90 served as the format.

Queries. `harvest_get.py` ran without the network (it reads origin/ci). A script compared each record's unprefixed `queries` with every `query` and `family review` line the harvest prints. Poa (line 5, 11 lines), Panicum (line 9, 13 lines) and Artemisia (lines 10 and 11, 4 lines each) match word for word and in order, with the "web: " lines after them. Marchantia, Vachellia, Parkinsonia and Ailanthus are in no harvest run ("in no harvest run yet"), and their records list "web: " lines only. No harvest shows "gave up", and no unlabelled line appears.

Chased.
- Poa, Panicum and Artemisia name 10.1016/j.tree.2009.09.010, which is the citation step each harvest prints (Poa 0 works, Panicum 0, Artemisia 7).
- The web-only genera give a "none" reason that names a labelled family search. No unsupported DOI is named.

Screened. The harvest DOIs and OpenAlex ids are in the harvest output. The web entries (PMC9824129, the Bath Spa ligule paper, the Parkia thesis, Bogawski et al. 2015, the Thompson 2008 thesis and the others) match their stated reasons. My own searches returned several of them.

Main. I checked origin/main (2f824c18) docs/views/evidence/*.jsonl for every genus.
- Marchantia: light only. Vachellia: V. bidwillii light only. Poa: P. annua and P. bulbosa light only. Panicum: P. virgatum light only (Guo et al. 2017). Artemisia: chemical (6 species) and light. Polystichum: chemical. Parkinsonia and Ailanthus: nothing.
- No search record names a trait that main holds evidence for.
- No evidence line repeats main. Evidence line 8 (Aiken and Springer 1995) adds a second, different source to Panicum virgatum sense_light_nonvisual, and it does not contradict Guo et al.
- The progress note says Panicum sense_chemical has evidence on main. It has none there, only this unit's lines 6 and 7. This is a note fault and is not counted.

Taxonomy. Marchantia, Vachellia (POWO page 77087189-1 for Vachellia karroo; Acacia karroo is its basionym), Poa, Parkinsonia, Panicum, Artemisia and Ailanthus are each accepted genera. No record is filed under a synonym's genus.

Searches. I ran 31 WebSearches:
- 15 for null search records: Parkinsonia diel 3, Ailanthus diel 3, Artemisia diel 2, Vachellia light 1, Vachellia chemical 1, Marchantia diel 1, and 1 pooled focusing search for the six eye_type records, plus a few follow-ups;
- 11 for evidence sources;
- 1 for taxonomy;
- 4 for wanted lines.

I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. One ezproxyberklee.flo.org result was left alone. No paper text is committed.

## Search record verdicts (13)

| Line | Record | Verdict |
|---|---|---|
| 1 | Marchantia polymorpha diel | ok. Web-only. Marchantia has no flowers. My search for sperm-release timing returned the MpMLO1 discharge news (CAS) and morphology pages, none with a time of day. |
| 2 | Vachellia karroo sense_light_nonvisual | ok. Web-only. My search "Acacia karroo seed germination light dark" returned scarification, salt and PEG, and moisture trials: Dadach and Khemmoudj 2022 (Agrobiologia 12(2), asjp opened), Kheloufi (univ-batna2 opened: acid and hot water only), Thomas 1998 (UNAM opened: testa and moisture), and Wilson and Witkowski 1998 (Rangelands Gateway opened: water). None has a light treatment. The other light hit, scielo rbb, is Acacia polyphylla, another genus. |
| 3 | Vachellia sense_chemical | **error: missed measurement.** Web-only. My search "Acacia farnesiana OR Vachellia karroo germination gibberellic acid OR smoke OR potassium nitrate" returned first the open PDF (iasj.rdd.edu.iq, opened) of Mahmood 2022, "Influence of seeds inoculation with PGPR, Gibberellic acid and Seaweed extract on seeds germination and seedling growth of Acacia farnesiana L.", Euphrates J Agric Sci 14(1): 59-77. In its Table 3, seeds soaked in GA3 germinated at 48.37% with none, 68.25% at 75 ppm and 78.67% at 150 ppm. The abstract gives 78.67% to 75 ppm, which disagrees with the table. Acacia farnesiana is Vachellia farnesiana. An applied hormone on living seed counts under 10(d), so the cell closes. The record's searches named Vachellia but not "Acacia farnesiana" with gibberellic acid. |
| 4 | Vachellia eye_type | ok. Pooled focusing search returned only the general set (FIU cas_bio/44, Nature 075535b0, PMC9257597 on Selaginella, arXiv algal optics). |
| 5 | Poa eye_type | ok. Queries match. The screened works are a lentil gene paper, a contact-lens paper and ligule anatomy. The pooled search found nothing on Poa. |
| 6 | Marchantia eye_type | ok. Web-only, and the pooled search found nothing. |
| 7 | Parkinsonia aculeata diel | ok. Web-only. My three searches returned Fabricante and Feitosa 2010, a literature review in ACSA 6(2) (opened: flowering season and 1 to 3 day flower life, no hour), Agra et al. 2015, Semina 36(3) (redalyc opened: dormancy, no timing), and Adgaba et al. 2016, Pak J Bot 48(4) (opened: Acacia species only). The others were extension pages and Ipomoea and Calliandra papers. |
| 8 | Parkinsonia eye_type | ok. The pooled search found nothing. |
| 9 | Panicum eye_type | ok. Queries match, and the pooled search found nothing. |
| 10 | Artemisia diel | ok, with a lead. Queries match. My searches returned the PSU ragweed abstract (Ambrosia, another genus), Denisow and Antoń 2012 (Aquilegia only, opened), and Developmental studies of A. annua (AGRIS, season only). They also returned an Acta Agrobotanica 67(1): 3-14 (2014) abstract (yadda.icm.edu.pl, opened): "The majority of Artemisia pollen grains appeared in the air before noon and in the early afternoon". That is airborne pollen at genus level, with no named species and no flower opening, so it does not meet the owner's diel reading. It stays a lead. |
| 11 | Artemisia eye_type | ok. Queries match. The epidermal anatomy survey and the Tagetes review are rightly screened, and the pooled search found nothing. |
| 12 | Ailanthus diel | ok. Web-only. My three searches returned the Thompson 2008 thesis and Aldrich et al. 2008, both screened in the record, and a magiran flower-structure paper (anther development). The Chinese search returned Zhan et al. 2014 on Acacia mangium (aeeisp opened), another genus. No Ailanthus hour of opening or scent. A redirected ESA 2006 abstract (paper 26895) was not followed. |
| 13 | Ailanthus eye_type | ok. The pooled search found nothing. |

Search record errors: **1 of 13 (7.7%)**, line 3.

## Evidence record verdicts (10)

Every line is grade m, partial and abstract-level. In each case I opened a page my own search returned and found the value there.

| Line | Record | Verdict |
|---|---|---|
| 1 | Marchantia polymorpha sense_chemical | ok. DOAJ opened: Schweizer, Monte, Solano and Reymond 2025, Plant-Environment Interactions 6(2), 10.1002/pei3.70052. The quoted words are verbatim. A herbivore-induced, JA-dependent defence counts under 10(a). |
| 2 | Vachellia farnesiana sense_light_nonvisual | ok. Pestinfo opened: Chauhan, Campbell and Galea, Weed Sci 69: 681-686. "Germination was not affected by light, suggesting that seeds are nonphotoblastic" is verbatim. |
| 3 | Poa annua sense_chemical | ok, with a fork. Mendelu page opened: Knot 2006, Acta Univ Agric Silvic Mendel Brun 54(5): 57-64. The quote is verbatim, and P. annua is named. The abstract names potassium nitrate, and the Czech abstract gives the exception, P. pratensis 'Julius'. Each cultivar was measured, and the statement covers all of them, so I accept m, as audit 89 did for "in both species". If the desk reads "all variants" as a group statement, the grade becomes g and the line still stands. |
| 4 | Poa pratensis sense_chemical | ok. UMN Conservancy opened: Morgan, Turveville, Xin and Petrella 2025. The GA4 sentence is verbatim. |
| 5 | Parkinsonia aculeata sense_light_nonvisual | ok. Rangelands Gateway opened: Everitt 1983, J Range Manage 36(4): 411-414, 10.2307/3897928. The quote is verbatim. |
| 6 | Panicum virgatum sense_chemical | ok. DOAJ opened: Muchlinski et al. 2019, Front Plant Sci 10: 1144, 10.3389/fpls.2019.01144. The MeJA sentence is verbatim, and fall armyworm feeding is in the abstract. |
| 7 | Panicum virgatum sense_chemical | ok. UNL Digital Commons opened: Sarath et al. 2006, Planta 223: 1154-1164, on P. virgatum cv Kanlow. The ABA sentence and the SNP result are in the abstract. The quote ends after "germination" where the sentence goes on ("inhibited root elongation..."), so it is a requote, not counted. |
| 8 | Panicum virgatum sense_light_nonvisual | ok, with a citation fault. Rangelands Gateway dlio/20420 (opened) gives Aiken and Springer 1995, J Range Manage 48(5): 455-458, 10.2307/4002252: "Although presence of light did not affect germination, coleoptile length under continuous darkness averaged 4.1 cm". The value is right. The record's url (experts.arizona.edu, "investigating-seed-dormancy-in-switchgrass...") names a different publication and should be replaced with the Rangelands Gateway page. Not counted. |
| 9 | Ailanthus altissima sense_light_nonvisual | ok. Annali di Botanica page opened: Di Cocco, Panero and Fabrini 2024, 14(1), 10.13133/2239-3129/18231. The page has the treatment phrase and "Seeds have been demonstrated not to have clear preferences for temperature and light". The quote is a phrase rather than a sentence (requote, not counted). |
| 10 | Ailanthus altissima sense_light_nonvisual | ok. Sapienza IRIS opened: Pepe, Gratani, Fabrini and Varone 2020, Plant Species Biol 35(4): 300-314, 10.1111/1442-1984.12286. The quote is verbatim, as is "Light promoted germination only for seeds of PA". |

Evidence errors: **0 of 10 (0%)**.

## Counts

- Search records: 1 of 13, 7.7%.
- Evidence: 0 of 10, 0%.
- Unit: 1 of 23, 4.3%.

Pooled with the desk's other audits of desk-screen units. I start from audit 90's figures as written: 48 in 1026 search records, and 52 in 1090 with evidence. With audit 91:
- Search records: 49 in 1039, 4.7%.
- With evidence included: 53 in 1113, 4.8%.

Fork that would change the count: line 3 rests on a regional journal paper whose abstract and table disagree on which GA3 dose gave 78.67%. Both doses raised germination over the 48.37% control, so the response stands either way. If the desk does not count this source, the record still had to hold the trait out under 10(e), since the title names GA3 and germination for a species of the genus.

**Verdict: fail on the search records (7.7%, above 5%); the evidence passes (0 of 10).** Both whole files were judged, so drop the error line and the rest of the unit stands. The whole unit is at 4.3%.

**Error lines to drop:**
- docs/views/searched/desk-d1.jsonl: line 3 (Vachellia sense_chemical). The cell reopens, and Mahmood 2022 (Euphrates J Agric Sci 14(1): 59-77) can close it for V. farnesiana.
- docs/views/evidence/desk-d1.jsonl: none. Line 8 needs its url corrected.

## Wanted lines (listed, not counted)

- Line 1 (Stone, Raine, Prescott and Willmer 2003, 10.1071/SB02024): the authors, year, Aust Syst Bot 16(1): 103-118 and DOI match the CSIRO page (opened).
- Line 2 (Grana 1980, 10.1080/00173138009424984): not searched, so not checked.
- Line 3 (Saberi, Harati and Tarnian 2021, Ecopersia 9(4): 279-285): the authors, year and pages match the journal page (opened), which lists no DOI. The abstract names GA3 and 0.2% KNO3 without their results, as the line says.
- Line 4 (Panicum crossing method, 10.5958/0975-928x.2019.00147.9) and line 5 (Johannesburg grasses 1935, 10.5962/p.386043): not searched, so not checked.
- Line 6 (Polystichum acrostichoides antheridiogen, 10.1086/297488): my search returned the uchicago page, and the fetch failed at its site, as it did for the unit. The year is empty, and I did not check the authors.
- Line 7 (10.3159/TORREY-D-18-00038.1): the USDA Treesearch page (opened) gives Redwood, Matlack and Huebner 2019, J Torrey Bot Soc 146(2): 79-86, with a subtitle naming Ailanthus altissima. The line's authors field is empty and could carry these names. The abstract covers soil burial and slope aspect only, with no light, GA or nitrate treatment, so it is unlikely to close sense_chemical.

## Leads

- Vachellia farnesiana sense_chemical: Mahmood 2022 (GA3 germination, above).
- Artemisia diel: the Acta Agrobotanica 67(1) circular-statistics paper on airborne Artemisia pollen (genus level; hourly concentrations).

## Blocked pages

- journals.uchicago.edu 10.1086/297488: failed at its site.
- esa.confex.com 2006 paper 26895: cross-host redirect, not followed.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
