# Audit 97: desk-d7 (Veronica, Taraxacum; branch origin/research/desk-d7, head cc0a8ffa)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: all 3 lines of docs/views/searched/desk-d7.jsonl (1 to 3).
- Evidence records: all 7 lines of docs/views/evidence/desk-d7.jsonl (1 to 7).
- Wanted lines: the file is empty.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (3 lines) and the empty wanted file prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), the counting rule of audit 39, and the rulings of audits 84 and 86 to 90, with audit 90 as the format. I ran 14 WebSearches: 3 for Veronica diel, 2 for the pooled eye_type focusing check, 5 for evidence sources, 1 for synonymy, and 3 more that the evidence and taxonomy checks needed. That is under the 40 the launch prompt allows; the null records needed no more once line 1's miss was found and the focusing searches came back empty. I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened (an independent.academia.edu result was left alone), and no paper text is committed.

Queries. `harvest_get.py` ran without the network (it reads origin/ci). Veronica (harvest run 1) prints the queries "Veronica phytochrome photoreceptor", "Veronica light perception", "Veronica phototropism" and the family review "Plantaginaceae photoreceptor review". Taraxacum (harvest run 2) prints the same three with "Taraxacum" and the family review "Asteraceae photoreceptor review". All three records copy these word for word and in order, with the "web: " lines after them. No harvest shows "gave up", and no record has an unlabelled extra line.

Chased. Veronica's harvest prints citation steps on 10.1111/een.12947 and 10.4161/psb.22704. Lines 1 and 2 name the first, which is printed (the second goes unnamed, noted only). Line 3 names 10.1126/science.aaf9793, which Taraxacum's citation step prints.

Screened. Line 3 screens 10.1104/pp.109.135509 (phytochrome B and photosynthesis in Arabidopsis) and W7220607642 (Tagetes lutein review). Both are in the Taraxacum harvest output, and neither concerns Taraxacum or epidermal focusing. Lines 1 and 2 screen nothing, and `screen_candidates.py` lists no open-trait candidates for either genus.

Queue claim. In docs/views/gaps/queue.jsonl on origin/main (cb81e765), Oenothera, Tridax, Momordica, Pluchea, Modiola, Capsella and Persicaria have no row: a case-insensitive grep for the seven names finds 0 lines. **The unit's claim holds.** Veronica has 8 rows (V. persica and V. chamaedrys: diel, eye_type, sense_chemical, sense_light_nonvisual), and Taraxacum has 3 (T. officinale: diel, eye_type, sense_light_nonvisual), as the progress note says.

Main. In docs/views/evidence on origin/main, the only evidence for either genus is Taraxacum officinale sense_chemical (canon-3:673). The unit logs no Taraxacum sense_chemical and rightly leaves Kim and Lee 2013 out. No unit line repeats or contradicts evidence on main. Main has older search records for the same cells: harvest-2:8 to 11 (Veronica, four traits), sweep-2:5 (Veronica), and harvest-10:1 (Taraxacum, diel, eye_type and light). As in audit 90, these repeats are noted and not counted. Juan et al. 1995 sits on main's wanted list (harvest-c10:36), and evidence lines 1 and 2 now log it.

Genus status. Veronica and Taraxacum are accepted genera. Every taxon in the unit is filed under its own genus. V. parnkalliana is an Australian Veronica, and any synonymy it carries (Derwentia/Parahebe) lies inside Veronica, so the synonym-of-another-genus rule touches no line.

## Search record verdicts (3)

| Line | Record | Verdict |
|---|---|---|
| 1 | Veronica diel | **error: missed measurement.** My search "Veronica floral biology anthesis daily rhythm pollination study Plantaginaceae" returned, first on the page, Godin 2017, "Антэкология Veronica serpyllifolia subsp. serpyllifolia (Plantaginaceae) в Московской области", Rastitelnyi mir Aziatskoi Rossii 4(28): 42-46 (sibran.ru PDF opened). It gives hours for flower opening: "Раскрывание цветков V. serpyllifolia начинается в 7 часов утра при температуре 17–18 °С". The number of newly opened flowers drops sharply from 14 h, and opening stops entirely by 18 to 20 h. Under the owner's reading this is flower-opening timing in a named species. The same searches also returned Milian, Melnyk, Marchyshyn and Cholach (2015, DOI 10.11603/2312-0967.2015.4.5548; ojs.tdmu.edu.ua page opened) on V. officinalis. Its abstract gives a day rhythm of bloom with the most flowers open "in the morning hours", which is a weaker lead. The record's own searches named V. persica and V. chamaedrys and found nothing. |
| 2 | Veronica eye_type | ok. Queries match and chased is printed. My pooled focusing searches ("Veronica OR Taraxacum epidermal cells lens light focusing petal conical cells", and a dandelion leaf-lens search) returned only the general set: Wilts et al. 2018, the Faraday Discussions 2020 paper, FIU cas_bio/44, Nature 075535b0, PMC9824129, and conical-cell reviews. None is on Veronica. Plant eye_type is "none" in any case. |
| 3 | Taraxacum eye_type | ok. Queries, chased and screened all hold. The same pooled searches found no Taraxacum focusing work (a dandelion microscopy hobby page and an Oradea agronomy PDF only). |

Search record errors: **1 of 3 (33.3%)**, line 1.

## Evidence record verdicts (7)

Every line is abstract-level and carries "partial": true, as it should.

| Line | Record | Verdict |
|---|---|---|
| 1 | Veronica persica sense_light_nonvisual | ok. revistas.uma.es page opened: Juan, Fernández and Pastor 1995, Acta Bot Malacit 20: 43-50, 10.24310/abm.v20i.8824. The abstract lists V. persica among the species that reached "porcentajes de germinación altos (superiores al 80%)" in light, at 22 ± 2 C, in a light-against-darkness design. The abstract gives no dark result for V. persica, as the note says. The quote stops at "alcanzaron" mid-sentence (requote, not counted). Grade m. |
| 2 | Veronica hederifolia sense_light_nonvisual | ok. Same page. Light germination was under 20%, and "En obscuridad, V. cymbalaria, V. hederifolia y V. peregrina experimentaron un aumento significativo de dicho porcentaje." is verbatim. The page's "hedertfolia" misspelling is noted correctly. Grade m. |
| 3 | Veronica peregrina sense_light_nonvisual | ok. scholars.uky.edu page opened: Baskin and Baskin 1983, Can J Bot 61(12): 3332-3336, 10.1139/b83-374. Seeds germinated to 98 to 100% in light in August and never germinated well in darkness. The fetch paraphrased that sentence, so the verbatim quote was not seen, but the value holds. Grade m. |
| 4 | Veronica parnkalliana sense_chemical | ok. Adelaide repository record opened: Guerin, Thorpe, Duval, Jusaitis and Ainsley 2013, Proc 5th Global Botanic Gardens Congress pp. 1-6, hdl 2440/91061, with no DOI. The quote "In vitro laboratory studies showed that germination was stimulated by gibberellic acid (GA3), heat or smoked water." is verbatim. Applied GA3 and smoke on living seed count under 10(d) and 10(e). Grade m. |
| 5 | Taraxacum officinale diel | ok. Springer page opened: Tanaka, Tanaka and Wada 1988, Bot Mag Tokyo 101: 103-110, 10.1007/BF02488887. The abstract gives "open for about 13–14 hr in T. officinale", and says capitula of T. officinale "opened earlier than those of T. albidum and T. japonicum in the morning in April". That is daily opening timing of a named species. The quote stops at "in" mid-sentence (requote, not counted). Grade m. |
| 6 | Taraxacum officinale sense_light_nonvisual | ok. Same page: "as low as 13 C for T. officinale" for photonastic opening. A living capitulum opening in response to light counts. The quote is again cut mid-sentence (requote, not counted). Grade m. |
| 7 | Taraxacum officinale sense_light_nonvisual | ok, with a field fault. abakus.inonu.edu.tr page opened: Tursun, Dayısoylu and Tursun 2015, KSU J Nat Sci 18(4): 48-54. The abstract gives the best germination at "20 degrees C for T. officinale" and best light as "16 hours light / 8 hours dark for S. vulgaris and T. officinale", so value and grade hold. But the record's `conditions` says "no pure darkness arm stated in the abstract", and the same abstract sentence gives "24 hours darkness" as best for Tragopogon pratensis. A darkness arm was therefore tested, and the conditions field should be corrected (not counted). The quote is a phrase (requote, not counted). |

Evidence errors: **0 of 7 (0%)**. Requotes, not counted: lines 1, 5, 6 and 7. Field fault, not counted: line 7 `conditions`.

## Counts

- Search records: 1 of 3, 33.3%.
- Evidence: 0 of 7, 0%.
- Unit: 1 of 10, 10%.

Pooled with the desk's audits 83 to 90, from audit 90's figures (search records 48 in 1026; 52 in 1090 with evidence):
- Search records: 49 in 1029, 4.8%.
- With evidence included: 53 in 1100, 4.8%.

Pooled with the running pool through audit 95, as audit 95 gives it (61 in 1088 search records; 68 in 1204 overall):
- Search records: 62 in 1091, 5.7%.
- With evidence included: 69 in 1214, 5.7%.

Audit 96 was not read and is not included.

**Verdict: fail on the search records** (1 of 3, one missed measurement); the evidence passes at 0 of 7. Both whole files were judged, so drop the error line and the rest of the unit stands.

**Error lines to drop:**
- docs/views/searched/desk-d7.jsonl: line 1 (Veronica diel). Godin 2017 on V. serpyllifolia (opening from 7 h, stopping by 18 to 20 h) can close the cell.
- docs/views/evidence/desk-d7.jsonl: none. Line 7's `conditions` wording should be corrected.

## Leads

- Veronica serpyllifolia diel: Godin 2017, Rastitelnyi mir Aziatskoi Rossii 4(28): 42-46 (sibran.ru PDF), with opening hours.
- Veronica officinalis diel: Milian et al. 2015, 10.11603/2312-0967.2015.4.5548, with a morning bloom maximum (abstract only).
- Taraxacum officinale diel: Hensel 1905 (on main's wanted list, harvest-c10:64), with 7 to 8 am opening as the desk's note reports. Not checked here.

## Blocked pages

None met. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
