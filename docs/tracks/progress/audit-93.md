# Audit 93: desk-d3 (8 plant genera; branch origin/research/desk-d3, head 16e64ad5)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: all 14 lines of docs/views/searched/desk-d3.jsonl (1 to 14).
- Evidence records: all 11 lines of docs/views/evidence/desk-d3.jsonl (1 to 11).
- Wanted lines: none (the unit has no wanted file).

Hamamelis, Apios, Nothoscordum, Clematis, Carpinus, Cocculus, Sagittaria and Richardia were not screened by the unit and are not under audit.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on a copy of the searched file (14 lines), with an empty wanted file, prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e) included), the counting rule of audit 39, and the rulings of audits 84 and 86 to 90 as the shared brief lists them.

Queries. `harvest_get.py` ran without the network (it reads origin/ci). Liriodendron (lines 1, 2) and Juncus (9, 10) are in harvest runs. Their unprefixed `queries` match every `query` and `family review` line the harvest prints, word for word and in order (Liriodendron 13, Juncus 11), with the "web: " lines after them. Neither harvest shows "gave up". Eclipta, Hedera, Lantana and Conoclinium are in no harvest run, and their records list "web: " lines only. No unlabelled line appears.

Chased.
- Liriodendron and Juncus name the citation-step DOI the harvest prints (10.2478/foecol-2024-0024 and 10.1016/j.tree.2009.09.010, each with 0 citing works naming the genus).
- Eclipta, Lantana and Conoclinium name 10.1007/s44372-025-00446-3. My own searches "Asteraceae photoreceptor review" and "Verbenaceae photoreceptor review" both returned link.springer.com/article/10.1007/s44372-025-00446-3, so the DOI is supported, as audits 86 and 87 accept for genera in no harvest run.
- The four Conoclinium records cite the Asteraceae search that the Eclipta records (lines 3, 4) list, and do not list it in their own `queries`. The search is labelled and in the unit, so I accept it. I note it here and do not count it.
- Hedera (5, 6) gives a reason (the Araliaceae search returned no family review naming Hedera).

Screened. Every screened DOI in lines 1, 2, 9 and 10 is a candidate that `screen_candidates.py` lists for that genus and trait. I read the titles and abstract starts, and none holds a measurement of the record's trait in a species of the genus.

Open cells. Harvest headers and main's evidence give these open cells:
- Hibiscus: sense_chemical.
- Liriodendron: all four.
- Juncus: diel, eye_type and sense_chemical.
- Eclipta, Hedera and Lantana: three each, since main already holds one trait for each.
- Conoclinium: all four.
- Sonchus: none.

Every open cell has either a search record or an evidence line in the unit, and no search record covers a trait already on main.

Hibiscus. The two citation steps show "None (error gave up)", so point 6 bars a search record, and the unit wrote none. That is consistent with the rules. Point 6 does not bar an evidence line. Main holds no Hibiscus sense_chemical evidence (its Hibiscus evidence is Warner and Erwin 2003, H. moscheutos, sense_light_nonvisual), so line 1 duplicates nothing. It supersedes main's harvest search record of 16 October that called Hibiscus sense_chemical "none".

Evidence rounds. desk-screen.md point 5 says to write no evidence in screening rounds. Desk units c7, c9 and d-series units have carried evidence, and audits 86 to 90 judged it on its merits, so I do the same here.

Duplicates. None of the 11 evidence lines repeats a taxon, trait and source already on main. Main holds no Sonchus evidence. Lines 7 to 10 add measurements in cells where main's search records (harvest-13, sweep-6) say none. That reflects on those older records, and these lines contradict no evidence on main.

Searches. I ran about 40 WebSearches:
- 9 for evidence sources;
- 2 for the family-review chased DOIs;
- 5 for taxonomy (POWO and WFO);
- 1 pooled focusing search for the five eye_type records;
- about 23 of my own for the null records, at least two per diel, sense_chemical and sense_light_nonvisual record (genus plus trait words, common name or species, and a hormone or germination phrasing under 10(e)).

I fetched only URLs my searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.

## Search record verdicts (14)

| Line | Record | Verdict |
|---|---|---|
| 1 | Liriodendron diel | ok. Queries match (13 harvest, 3 web), and chased is the printed citation step. My searches returned Wikipedia, the USDA woody-plant seed manual, phenology pages, a Magnolia grandiflora flowering-dynamics paper (j.bjfu.edu.cn 9622, opened: no Liriodendron, no hour), a Dendrobium paper (bbr.nefu.edu.cn, opened) and a Haskap paper (DOAJ 451d60ce, opened). None gives a Liriodendron opening hour. |
| 2 | Liriodendron eye_type | ok. Queries match. My pooled focusing search returned only the general set (FIU cas_bio/44, AskNature, PMC9824129). |
| 3 | Eclipta diel | ok. Web-only, and chased is supported. My two searches returned sunflower circadian anthesis work (PMC9977281) and floral-biology papers on other genera. I found no Eclipta hour. |
| 4 | Eclipta eye_type | ok. Web-only. The pooled search found nothing on Eclipta. |
| 5 | Hedera eye_type | ok. Web-only, and the chased reason holds. The pooled search found nothing on ivy focusing. |
| 6 | Hedera sense_chemical | **error: missed measurement.** Marc and Hackett 1992, "Changes in the pattern of cell arrangement at the surface of the shoot apical meristem in Hedera helix L. following gibberellin treatment", Planta 186: 503-510. The DOI 10.1007/BF00198029 is in the Springer URL my search returned, and I opened that page. The abstract describes the "gibberellic acid (GA3)-induced transition from spiral to distichous phyllotaxis" in living ivy shoots, a response to an applied hormone (10(d)). Geneve 1991 also qualifies: "Patterns of adventitious root formation in English ivy", J Plant Growth Regul 10: 215-220, 10.1007/BF02279337 (scholars.uky.edu, opened). Juvenile petiole cuttings treated with NAA plus DFMA formed more roots. The record searched only germination and scent phrasings, and ivy's classic hormone work is on phase change and rooting. |
| 7 | Lantana diel | **error: missed measurement.** Barros, Rico-Gray and Díaz-Castelazo 2001, "Sincronia de floração entre Lantana camara L. (Verbenaceae) e Psittacanthus calyculatus (DC.) G. Don (Loranthaceae) ocorrentes nas dunas de La Mancha, Veracruz, Mexico", Acta Botánica Mexicana 57: 1-14. I opened the Redalyc PDF 57405701 that my search "Lantana camara anthesis time flowers open hours floral biology pollination" returned. Tagged buds were followed in the field: L. camara flowers open centripetally "a partir das 6h30", and Table 2 gives anthesis as 6h30 to 15h00. This is a flower-opening time for a named species. |
| 8 | Lantana eye_type | ok. Web-only, and chased is supported. The pooled search found nothing on Lantana. |
| 9 | Juncus diel | **error: missed measurement (fork below).** Michalski and Durka 2007, "Synchronous pulsed flowering: analysis of the flowering phenology in Juncus (Juncaceae)", Annals of Botany 100: 1271-1285 (UFZ PDF, opened from my search "Juncus flowering diurnal rhythm anther dehiscence hour stigma exsertion"). The paper counts open flowers daily in nine named Juncus species, J. effusus among them. It states "Opening of the flowers occurs before noon; therefore surveys were performed between 0900 and 1100 h." That is flower-opening timing at day and hour scale, and the record's searches (plant-profile pages only) missed it. The harvest output does not hold it. Huang, Xiong and Barrett 2013 (IJPS 174(9), 10.1086/673247, opened) gives months only and does not count. |
| 10 | Juncus eye_type | ok. Queries match. The three screened works are rightly screened, and the pooled search found nothing. |
| 11 | Conoclinium sense_light_nonvisual | ok. Web-only. My searches returned seed-company, garden.org and Rutgers propagation pages, a Baskin search that returned E. cannabinum and other Eupatorium only, and a weed-germination paper (plantarum.izbis, title only, not Conoclinium). I found no trial. WFO (opened) gives Conoclinium coelestinum as accepted, with Eupatorium coelestinum as its synonym. |
| 12 | Conoclinium sense_chemical | ok. Web-only. A growth-regulator search returned paclobutrazol and daminozide work on other genera, and nothing on Conoclinium. |
| 13 | Conoclinium diel | ok. Web-only. The record ran one diel phrasing and says why. My two searches returned Fründ et al. 2011 on flower-head closing in other Asteraceae and nature-centre pages, with no Conoclinium hour. |
| 14 | Conoclinium eye_type | ok. Web-only, and the pooled search found nothing. |

Search record errors: **3 of 14 (21.4%)**, lines 6, 7 and 9.

## Evidence record verdicts (11)

| Line | Record | Verdict |
|---|---|---|
| 1 | Hibiscus sabdariffa sense_chemical | ok. modares page opened: Saberi, Tarnian and Karimian, Ecopersia 9(1): 1-10, 2021, no DOI shown. The quote is verbatim (a clause of a sentence that begins "A comparison of means showed that"). GA priming of living seed counts under 10(d). |
| 2 | Liriodendron tulipifera sense_chemical | ok. Thünen PDF opened: Barnett and Farmer, Silvae Genetica 27(3-4). The gibberellin sentence is there (the record keeps the page's OCR errors). |
| 3 | Liriodendron tulipifera sense_light_nonvisual | ok, weak. Same PDF. Light is a test factor that "significantly influenced germination percentage", and the levels are not given. The record says so and claims no direction. |
| 4 | Eclipta prostrata sense_chemical | ok. ICAR page opened: Kedia, Kasera and Mohammed, Seed Research 42(2): 159-164, 10.56093/sr.v42i2.163227. The quote is verbatim (part of a sentence). POWO 202735-1 (opened) says "This name is a synonym of Eclipta prostrata", and Eclipta is the accepted genus. Filing the record under E. prostrata, with the published name in the note, is right. Audits 86 and 88 failed records filed under a synonym's genus, which is not the case here. |
| 5 | Hedera helix diel | ok. Graz PDF opened: Teppner, Hausl-Hofstätter, Brosch and Obermayer 2009, Mitt naturwiss Ver Steiermark 139: 183-205. "sukzessive über den Tag" is in §3.3, and the Fig. 1 caption gives anthers empty "ca. 16.40 Uhr". This is field observation of a named species. The quote is a phrase, not a sentence (requote, not counted). |
| 6 | Lantana camara sense_light_nonvisual | ok. iasj PDF opened: Taha and Sarmamy, ZJPAS 35(SpD): 189-194, 10.21271/ZJPAS.35.SpD.21. The levels are 80% (tulle), 100% and 120% (added lamps), a set-light-intensity trial (10(d)). The quote is verbatim. |
| 7 | Sonchus oleraceus sense_light_nonvisual | ok. DOAJ a42c1577 opened: Lee, Mahajan, Beregszaszi and Chauhan, Plants 13(23): 3451, 10.3390/plants13233451. The quote is verbatim. |
| 8 | Sonchus asper sense_light_nonvisual | ok. Same page, and the quote is verbatim. |
| 9 | Sonchus oleraceus sense_chemical | ok. Redalyc HTML opened: Guevara-Barrera, Magnitskiy and Balaguera-López, RFNAM 77(1): 10541-10552, 10.15446/rfnam.v77n1.107027. The page gives control 78.5%, 200 mg/L 83.5% and 600 mg/L 14.75%, and "concentrations higher than 200 mg L-1 had an inhibitory effect on germination". The value holds. The record's quote ends in "consequently," and so is not a whole sentence (requote, not counted). |
| 10 | Sonchus oleraceus diel | **error: owner's reading.** The Uppsala Linnaeus Garden page (opened) reproduces the Horologium Florae row "kålmolke Sonchus oleraceus / Sonchus lævis, 5•, 12". The page calls these "the opening and closing times he used to mark time" and does not say how the hours were obtained (observed, where, or compiled). Under the owner's reading, a historical flower-clock table is not a measurement of a named species' flower opening unless it says so, and this one does not. The m grade also fails, since nothing shows the species was measured in the source. The dot before "5" means "shortly before", which the page explains and the record says it could not read. |
| 11 | Juncus ranarius sense_chemical | ok, requote. Notulae page opened: Kołodziejek and Patykowski 2015, NBHA 43(2): 439-446, 10.15835/nbha4329752. The abstract says "the higher the GA3 concentration, the more germination occurred", so the value holds. But the quote is the light sentence ("a germination preference for light"), which supports another trait. It should be replaced with the GA3 sentence (requote, not counted). POWO 443410-1 (opened) says "This species is accepted". |

Evidence errors: **1 of 11 (9.1%)**, line 10.

## Counts

- Search records: 3 of 14, 21.4%.
- Evidence: 1 of 11, 9.1%.
- Unit: 4 of 25, 16.0%.

Pooled with the desk's other audits of desk-screen units (83 to 90), using audit 90's figures (search records 48 in 1026; with evidence 52 in 1090):
- Search records: 51 in 1040, 4.9%.
- With evidence included: 56 in 1115, 5.0%.

Forks that would change the count:
- Line 9 (Juncus diel). If the desk reads Michalski and Durka's "Opening of the flowers occurs before noon" as a methods remark and not a measurement, line 9 stands. Search records would then be 2 of 14 (14.3%), and the verdict is unchanged.
- Line 10 (Sonchus diel). If the desk reads the Horologium row as Linnaeus's own observation of a named species, line 10 stands, but only at grade g or with a note that the source does not say it was measured. Evidence would then be 0 of 11.

**Verdict: fail.** The search records fail at 21.4% (lines 6, 7 and 9). The evidence fails at 9.1% (line 10). Both whole files were judged, so drop the error lines and the rest of the unit stands.

**Error lines to drop:**
- docs/views/searched/desk-d3.jsonl: lines 6, 7 and 9.
  - Line 6: Hedera sense_chemical reopens. Marc and Hackett 1992 (10.1007/BF00198029) or Geneve 1991 (10.1007/BF02279337) can close it.
  - Line 7: Lantana diel reopens. Barros et al. 2001, Acta Bot Mex 57: 1-14 (Redalyc 57405701), can close it.
  - Line 9: Juncus diel reopens. Michalski and Durka 2007, Ann Bot 100: 1271-1285, can close it.
- docs/views/evidence/desk-d3.jsonl: line 10 (Sonchus oleraceus diel, Linnaeus flower clock). Sonchus diel then rests on main's older search records.

Requotes (not counted): evidence lines 5, 9 and 11, as above.

## Leads

- Hedera sense_chemical: Marc and Hackett 1992 (GA3, phyllotaxis), and Geneve 1991 (NAA, rooting of juvenile cuttings). Wareing and Frydman 1976 (Acta Hortic 56, 10.17660/ActaHortic.1976.56.4, opened) reports only endogenous GA, so it does not qualify.
- Lantana diel: Barros, Rico-Gray and Díaz-Castelazo 2001 (anthesis 06:30 to 15:00, field, n = 12).
- Juncus diel: Michalski and Durka 2007 (nine species, flower opening before noon, synchronous pulses).
- The unit's own open leads (Liriodendron PMC8325688, the Eclipta Weed Technology germination paper, Chauhan, Gill and Preston 2006 on Sonchus) were not chased here.

## Blocked pages

- thaiscience.info TNAH 10982012.pdf served an empty page (viewport tag only).
- Not opened: plantarum.izbis.bg.ac.rs (bot checks in audit 88) and the sciengine Chinese PDF.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
