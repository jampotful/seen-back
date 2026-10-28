# Audit 119: desk-d29 (branch origin/research/desk-d29, head ea999e93)

## Lines judged

No sample was drawn: the launch prompt asks for the whole unit, so error lines can simply be dropped.
- Search records: all 40 lines of docs/views/searched/desk-d29.jsonl. Every null on a cell where a GA3/KNO3/smoke, light/dark, shade/photoperiod, MeJA/herbivore volatile or flower-opening finding is plausible got at least one search of my own (lines 1, 4, 6, 8, 10, 11, 12, 14, 15, 16, 20, 21, 23, 24, 26, 28, 29, 31, 35, 37, 38, 40). The eye_type lines (2, 3, 5, 7, 9, 13, 17, 19, 22, 25, 27, 30, 32, 33, 34, 36, 39) were judged mechanically (queries, chased, synonymy, owner's reading 10(b)).
- Evidence records: all 4 lines of docs/views/evidence/desk-d29.jsonl.
- Wanted lines: all 5 (faults listed, not counted).

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched and wanted files prints "0 problems". All 4 evidence lines parse. Quotes are whole sentences of 85, 103, 92 and 64 characters.

## Method

Judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), audit 39's counting rule and the brief's rulings (audits 84, 86 to 90). Audits 117 and 118 served as format. I ran 52 WebSearches (4 re-running the records' labelled family-review searches, 3 POWO, 1 wanted line, the rest for nulls) and fetched only URLs my searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened (an academia.edu hit in the Lapsana list and shibboleth.idm.home.nyu.edu hits in the Eriogonum list were left alone). No paper text is committed. origin/main is at ede3e407.

### Queries

- Lines 1 to 28 (Jacobaea, Lactuca, Rabelera, Heracleum, Matricaria, Eriogonum, Aralia, Heteromeles, Lapsana, Kalmia, Gaultheria): `harvest_get.py` prints "in no harvest run yet" for every genus; the records list "web: " lines only. No unlabelled line.
- Lines 29 to 40 (Vaccinium, Frangula, Berteroa, Elaeagnus, Geum, Pilosella, Celastrus): a script compared the unprefixed `queries` with every `query` and `family review` line harvest_get prints, supplement runs included. All 12 match word for word and in order, with the "web: " lines after them. No harvest shows "gave up".

### Chased

- Lines 1-5, 8-11, 18-28 name 10.1007/s10265-016-0785-4 (Li and Mathews 2016) for genera in no harvest run. My runs of "Asteraceae photoreceptor review", "Caryophyllaceae photoreceptor review", "Rosaceae photoreceptor review" and "Ericaceae photoreceptor review" each returned "evolutionary aspects of plant photoreceptors" on nutrition-evidence.com; opened, it gives Fay-Wei Li, Sarah Mathews, J Plant Res 2016 129(2): 115-22, DOI 10.1007/s10265-016-0785-4. Supported (audits 86, 87).
- Lines 6, 7, 12-17 give none-reasons for Apiaceae, Polygonaceae and Araliaceae; acceptable for genera in no harvest run.
- Lines 29-40 cite the harvest's own citation steps and family review, as harvest_get prints them. Supported.

### Synonyms (POWO, opened)

- Rabelera holostea (L.) M.T.Sharples & E.A.Tripp, 77205026-1: "This species is accepted."
- Jacobaea vulgaris Gaertn., 226649-1: "This species is accepted."
- Pilosella aurantiaca (L.) F.W.Schultz & Sch.Bip., 238000-1: "This species is accepted." The evidence record's filing of Hieracium aurantiacum under Pilosella is right.
- Kalmia, Frangula, Matricaria and the rest were not opened on POWO in this audit (budget); no synonym issue was seen in any result.

### Main

- Every one of the 40 search records repeats a null search record already on main for the same genus and trait (sweep-3:26, sweep-5:15, sweep-6:23, sweep-9:23, sweep-10:27, sweep-10:35, sweep-11:1, :6, :10, sweep-14:1, :3, :4, :6, sweep-15:2, :3, :40, sweep-16:8, :9). Audits 90 and 112 noted such repeats without counting them; I do the same. They are redundant and can be dropped without loss.
- No evidence line repeats evidence on main: main holds no Kalmia, Pilosella or Hieracium aurantiacum evidence, and Jacobaea vulgaris only sense_light_nonvisual (sweep-14). The Kalmia evidence contradicts main's null sweep-11:1 (sense_chemical, sense_light_nonvisual) and the Pilosella evidence main's null sweep-10:35; main's fault, not counted.

## Search record verdicts (40)

| Line | Record | Verdict |
|---|---|---|
| 1 | Jacobaea diel | ok (fork below). My searches returned Vanparys, Meerts and Jacquemart (ULB preprint, opened), which cites Harper and Wood (1957) for S. jacobaea: "pollen presentation occurs from 8 a.m. to 5 p.m., with a peak from 10 a.m. to 12 noon". Pollen presentation, not opening of capitula, and secondary; lead only. |
| 2 | Jacobaea eye_type | ok |
| 3 | Lactuca eye_type | ok |
| 4 | Rabelera diel | ok. Flora pages only. |
| 5 | Rabelera eye_type | ok |
| 6 | Heracleum diel | ok. Denisow and Antoń 2012 (aa65 37-44, opened) is Aquilegia; PMC5055817 is Silene. |
| 7 | Heracleum eye_type | ok |
| 8 | Matricaria diel | ok |
| 9 | Matricaria eye_type | ok |
| 10 | Matricaria sense_chemical | ok. Only extract-allelopathy papers (extracts of Matricaria, excluded by 10(a)) and smoke papers on other genera. |
| 11 | Matricaria sense_light_nonvisual | ok. Two searches returned chamomile and Oncosiphon papers, no M. discoidea trial. A light trial on chamomile would count for the genus if chamomile is a Matricaria in POWO; the abrates.org.br hit ("Effects of light and temperature on the germination of chamomille (Matricaria recutita) seeds") is then a lead the record missed. Not counted, because I did not open POWO for M. recutita; see fork. |
| 12 | Eriogonum diel | ok |
| 13 | Eriogonum eye_type | ok |
| 14 | Eriogonum sense_chemical | **error: missed measurement.** Christou 1974, "Germination Ecology of Five Chihuahuan Desert Winter Annuals" (UNI thesis, scholarworks.uni.edu/etd/2344, opened): aqueous leachates of Larrea tridentata at 10, 5 and 1% reduced germination and hypocotyl growth of four Eriogonum taxa; the 1% leaf leachate did not affect E. rotundifolium and E. trichopes. A living seed's response to a chemical cue (10(a)); the leachate is not Eriogonum tissue. Fork below. |
| 15 | Eriogonum sense_light_nonvisual | **error: missed measurement.** Baskin, Chesson and Baskin 1993, "Annual Seed Dormancy Cycles in Two Desert Winter Annuals", J Ecol 81(3): 551-556 (USU aspen_bib/2439, opened): Eriogonum abertianum seeds tested "in light and darkness at five thermoperiods". Also Christou 1974 (above): E. abertianum vars responded positively to light, E. trichopes not affected. Germination light/dark, 10(d)-(e). Both came on the first page of "Eriogonum seed germination light requirement darkness". |
| 16 | Aralia diel | ok |
| 17 | Aralia eye_type | ok |
| 18 | Heteromeles diel | ok |
| 19 | Heteromeles eye_type | ok |
| 20 | Heteromeles sense_chemical | ok, one lead unresolved: Keeley 1987, "Role of fire in the seed germination of woody taxa in California chaparral", Ecology 68: 434-443, 10.2307/1939275 (USGS page opened, no abstract, species list not shown). |
| 21 | Lapsana diel | ok. Only Linnaeus's flower clock (a historical table, not a measurement under the owner's reading) and flora pages. |
| 22 | Lapsana eye_type | ok |
| 23 | Lapsana sense_chemical | ok |
| 24 | Kalmia diel | ok. Explosive-pollen-release paper (10.1086/697220) is mechanics, not timing; not opened. |
| 25 | Kalmia eye_type | ok |
| 26 | Gaultheria diel | ok |
| 27 | Gaultheria eye_type | ok |
| 28 | Gaultheria sense_chemical | ok. Holloway 2011 GA note (UAF, opened) lists no Gaultheria; the Epigaea GA3 paper is another genus. |
| 29 | Vaccinium diel | ok. Bożek 2009 (Acta Agrobot 62(1), opened) and Kaczmarska 2009 (ASPHC 8(4), opened) give flowering in days and dates, no hour. |
| 30 | Vaccinium eye_type | ok |
| 31 | Frangula diel | ok. Acta Agrobot aa.2012.058 (Alnus) and 10.1007/s00606-012-0609-5 (Fritillaria), both opened, are other genera. |
| 32 | Frangula eye_type | ok |
| 33 | Berteroa eye_type | ok |
| 34 | Elaeagnus eye_type | ok |
| 35 | Geum sense_chemical | **error: missed measurement.** Douville, Abella and Perkins 2014, "Plant-derived smoke influences germination of native and invasive plants in the Northern Great Plains", ESA 2014 abstract (eco.confex.com Paper50267, opened): smoke decreased cumulative germination of Geum triflorum against the unsmoked control. Smoke response of living seed, 10(e). |
| 36 | Pilosella eye_type | ok |
| 37 | Pilosella sense_chemical | **error: missed measurement.** Di Gristina, Varshanidze and Domina 2020, "Seed germination data of three Hieracium and one Pilosella (Asteraceae) from Sicily and southern Italy", Flora Mediterranea 30: 431-437 (herbmedit.org PDF, abstract read): Pilosella hoppeana subsp. sicula is among the four taxa, and "Germination tests carried out in gibberellic acid (GA3) provided similar germination percentages." A title naming germination of a Pilosella species belongs on the wanted list at least (10(e)); the taxon-level GA3 result is in the tables, unread. Returned by my first Pilosella GA3 search. |
| 38 | Celastrus diel | ok |
| 39 | Celastrus eye_type | ok |
| 40 | Celastrus sense_chemical | ok. GA3 hits were Celtis sinensis (sciopen, opened) and Acer (agriculturejournals, opened). |

Search records: **4 errors in 40, 10.0%** (lines 14, 15, 35, 37).

## Evidence verdicts (4)

| Line | Record | Verdict |
|---|---|---|
| 1 | Jacobaea vulgaris sense_chemical (Wei, Vrieling, Mulder, Klinkhamer 2019, J Chem Ecol 45(2): 136-145, 10.1007/s10886-018-1020-7) | **ok.** WUR page (opened) confirms authors, journal, pages, DOI and the quote word for word (85 characters, whole sentence). "A range of concentrations of MeJA was added to the medium", no doses, as the record says. Grade m, partial true; POWO accepts the name. |
| 2 | Pilosella aurantiaca sense_light_nonvisual (Bear, Giljohann, Cousens, Williams 2012, Aust J Bot 60(7): 615-624, 10.1071/BT12058) | **ok.** connectsci page (opened) confirms citation and the quote word for word (103 characters). Value holds for H. aurantiacum; POWO accepts Pilosella aurantiaca. Grade m, partial true. |
| 3 | Kalmia latifolia sense_light_nonvisual (Malek, Blazich, Warren, Shelton 1989, J Environ Hortic 7(4)) | **ok.** PDF (opened) confirms authors, 7(4), pages 161-162, December 1989, the quote word for word (92 characters), cool-white lamps at 42 µmol m-2 s-1, Avery County at 923 m on 13 November 1986, and "did not stimulate germination in the dark". The journal field could carry "161-162". |
| 4 | Kalmia latifolia sense_chemical (Taylor, Conev, Harris, ASHS 2009 abstract) | **ok, with a fix.** Page (opened) confirms authors, 25 July 2009, the quote word for word (64 characters), "100 ppm" and "200 ppm" GA, and "324 µmoles·m-2·sec-1 of light from 8 a.m. to 12 a.m." Doses copied exactly. But `conditions` says "abstract gives no soak time", while the abstract says "soaking overnight" in each GA solution, and it omits the stated constant 21 C. The value is unaffected, so not counted; the conditions field should be corrected before merge. |

Evidence: **0 errors in 4.**

## Wanted lines (faults listed, not counted)

- Line 4 (Berteroa incana diel, Denisow): the pbsociety page (opened, article 1646, DOI 10.5586/aa.2009.010) lists all nine species (Hydrangea arborescens subsp. discolor, H. paniculata, Viburnum opulus, Chaenomeles japonica, Knautia arvensis, Adonis vernalis, Aster sagittifolius, Taraxacum officinale, Chelidonium majus). Berteroa incana is not among them, so the lead is dead for Berteroa. The year 2012 is unsupported: the page prints no year and the DOI's "2009" suggests 2009.
- Lines 1, 2, 3, 5: not opened (budget). Line 1 rightly leaves authors empty.

## Rates

Unit: search records 4 in 40 (10.0%); evidence 0 in 4; together 4 in 44 (9.1%).

Pooled with the running totals carried by audit 118 (search records 52 in 1044; with evidence 61 in 1137), a chain through audits 83 to 90 and on to 118:
- Search records: 56 in 1084, 5.17%.
- With evidence included: 65 in 1181, 5.50%.

Forks that would change the count:
- Line 14: if a germination response to another plant's leachate is read as allelopathy outside sense_chemical, line 14 is ok and the unit has 3 in 40 (7.5%). The unit fails either way.
- Line 1: if timed pollen presentation counts as flower-opening timing under the diel reading, Harper and Wood 1957 (cited in Vanparys et al.) makes line 1 an error too.
- Line 11: if POWO places Matricaria recutita in Matricaria (as M. chamomilla), the chamomile light/temperature germination paper (abrates.org.br artigo 5074) is a missed measurement and line 11 is an error.

**Verdict: fail** (search records 4 of 40, above 5%). The other 36 search lines and all four evidence lines stand and can merge, evidence line 4 after its conditions fix.

**Error lines to drop:**
- docs/views/searched/desk-d29.jsonl: lines 14 (Eriogonum sense_chemical), 15 (Eriogonum sense_light_nonvisual), 35 (Geum sense_chemical), 37 (Pilosella sense_chemical).
- docs/views/evidence/desk-d29.jsonl: none (line 4 needs its `conditions` corrected).

## Leads (not counted)

- Eriogonum sense_light_nonvisual: Baskin, Chesson and Baskin 1993, J Ecol 81(3): 551-556 (E. abertianum, light and darkness); Christou 1974 UNI thesis etd/2344 (four Eriogonum taxa, light and Larrea leachate).
- Geum sense_chemical: Douville, Abella and Perkins 2014, ESA abstract Paper50267 (G. triflorum, smoke lowered germination).
- Pilosella sense_chemical: Di Gristina, Varshanidze and Domina 2020, Flora Mediterranea 30: 431-437 (P. hoppeana subsp. sicula, GA3).
- Heteromeles sense_chemical: Keeley 1987, Ecology 68: 434-443, 10.2307/1939275 (species list unread).
- Jacobaea diel: Harper and Wood 1957, as cited by Vanparys, Meerts and Jacquemart (ULB dipot 2013/157150).
- Matricaria sense_light_nonvisual: chamomile light/temperature germination (abrates.org.br artigo-cientifico 5074), pending POWO on M. recutita.

## Blocked pages

- pmc.ncbi.nlm.nih.gov PMC10818387 table t001 (it came back on several anthesis searches): reCAPTCHA verification page, not retried.
