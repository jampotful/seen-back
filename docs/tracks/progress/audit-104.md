# Audit 104: desk-d14 (plant genera; branch origin/research/desk-d14, head 37aaa3e2)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so error lines can simply be dropped.
- Search records: none (the unit wrote no docs/views/searched/desk-d14.jsonl).
- Evidence records: all 6 lines of docs/views/evidence/desk-d14.jsonl (1 to 6).
- Wanted lines: none.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on an empty searched file with an empty wanted file prints "0 problems". There is nothing else for the gate to read.

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e) included), the counting rule of audit 39, and the rulings of audits 84 and 86 to 90; audit 103 served as the format. For each evidence record I ran a title WebSearch, fetched a URL that search returned, and compared authors, year, journal, DOI, quote and value. I checked every taxon on POWO pages my searches returned (WFO where POWO was silent), and checked origin/main (db79cd0c) docs/views/evidence, searched and wanted for every genus in the unit.

Searches: 13 WebSearches (7 for evidence titles and versions, 5 for taxonomy, 1 for the published version of the preprint). I fetched only URLs my searches returned. A search for line 6 also returned a www-cambridge-org.ezproxyberklee.flo.org result, which is a library proxy, and I left it alone. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed.

## Evidence record verdicts (6)

| Line | Record | Verdict |
|---|---|---|
| 1 | Rumex obtusifolius sense_chemical (Moore, Paul, Whittaker and Taylor 2003, Funct Ecol 17(4): 549-554) | ok. Lancaster eprints 8810 opened: authors, year, volume, issue and pages agree; both the quoted sentence (summary point 6) and the 9-fold peroxidase sentence (point 5) are in the abstract. Applied jasmonic acid on a living plant counts under 10(d). POWO (310739-2, opened) accepts Rumex obtusifolius L. The "glasshouse" condition was not checked. |
| 2 | Rumex obtusifolius sense_chemical (Moore, Taylor, Paul and Whittaker 2003, Funct Ecol 17(1): 75-81) | ok. Eprints 8812 opened: citation agrees; the quote is in abstract point 5, and the abstract itself (not only a page summary, as the note says) gives "approximately 37%" smaller final leaf area. Herbivore-induced systemic response counts under 10(a). Minor: the abstract says "controlled conditions", where the record writes "laboratory". |
| 3 | Rumex crispus sense_chemical (Hemmat, Zeng and Khan 1985, Weed Sci 33(5): 658-664, 10.1017/S0043174500083041) | ok. Cambridge page opened: authors, year, volume, issue, pages and DOI agree, and "Scarification made the seeds responsive to GA4+7" is in the abstract. Applied gibberellin on living seed counts under 10(d). POWO (224413-2, opened) accepts Rumex crispus L. |
| 4 | Centaurea jacea diel (Štenc et al. 2023, Am J Bot 110(6): e16179, 10.1002/ajb2.16179) | ok. Starfos record opened: title, journal, DOI and the quoted sentence agree; the Halle record (opened) gives the six authors in the record's order. A daily pollen-presentation schedule of the flower heads is flower timing, as audits 90, 99 and 101 counted anther dehiscence and pollen release. POWO (190753-1, opened) accepts Centaurea jacea L. The same work is a wanted lead on main for Succisa pratensis (harvest-c6 wanted line 1); logging it for C. jacea neither repeats nor contradicts main evidence. |
| 5 | Centaurea stoebe sense_chemical (Huang, Gfeller and Erb 2018, bioRxiv 441790) | ok, with a repair. The bioRxiv page I fetched served the full text without its abstract, but its Results state that (E)-β-caryophyllene partially mimics the C. stoebe root VOC effect on M. melolontha growth. The same work was published as Huang, Gfeller and Erb 2019, "Root volatiles in plant–plant interactions II: Root volatiles alter root chemistry and plant–herbivore interactions of neighbouring plants", Plant Cell Environ 42(6): 1964-1973, 10.1111/pce.13534 (PMC6849603, opened), whose abstract carries the quoted words; the record should cite that version. Volatile signalling by a living plant counts under the owner's reading. WFO (wfo-0000044770, opened) accepts Centaurea stoebe L. Fork below on whether the cell is the emitter's or the receiver's. |
| 6 | Centaurea x moncktonii sense_light_nonvisual (DiTommaso et al. 2021, Weed Sci 69(1), 10.1017/wsc.2020.86) | **error: taxon is a POWO synonym, and the note misstates POWO.** The source checks (BioOne page opened: five authors in the record's order, Weed Sci 69(1), the quoted sentence verbatim, 14:10 h light:dark against continuous darkness), so the value stands. But the POWO page the note cites (urn:lsid:ipni.org:names:191031-1, opened) states that Centaurea × moncktonii is a synonym of Centaurea × gerstlaueri, and POWO 190561-1 (opened) accepts C. × gerstlaueri with parentage C. jacea × C. nigra. The note says POWO accepts C. × moncktonii, which is false. Only an older WFO snapshot (2022-06) still accepts the name. The record should be refiled as Centaurea × gerstlaueri with the note corrected. |

Genus status. Rumex and Centaurea are accepted genera; POWO treats Jacea as a synonym (Jacea phrygia is a synonym of Centaurea phrygia, page opened), so no record is filed under a synonym's genus. Line 6's fault sits at the hybrid's name, not the genus.

Repeats of main. None. Main holds Rumex sense_chemical only for R. confertus (oa-13b:422, 439, 442), and no Centaurea evidence at all. Lines 1 to 5 contradict two null search records on main (sweep-6:33, Rumex diel/eye_type/sense_chemical, already contradicted by main's R. confertus records; sweep-5:6, Centaurea diel/eye_type/sense_chemical/sense_light_nonvisual). Finding a measurement a main null missed is the work's purpose, so that is a main problem, as audit 103 treated its contradicted nulls. Those nulls should be retired.

Evidence errors: **1 of 6 (16.7%)**, line 6.

## Skipped genera (no records written, checked against main)

- Parkinsonia: diel null desk-d1:6; light evidence desk-d1:5; sense_chemical held by desk-d1 wanted line 3 (Saberi, Harati and Tarnian 2021). Skip right.
- Panicum: diel held by desk-d1 wanted lines 4 and 5 (Davidson 1935 among them) and harvest-c11 wanted lines; light (sweep-97:3) and chemical (desk-d1:6, 7) evidence on main. Skip right.
- Ailanthus: diel null desk-d1:11; light evidence desk-d1:8, 9; sense_chemical held by desk-d1 wanted line 7 (Redwood et al. 2019) and harvest-c11 wanted lines 184 and 185 (Soler and Izquierdo 2024, 2026). Skip right.
- Polystichum: light/diel null harvest-6:2; chemical evidence oa-9:255 to 257, 273; leads desk-d1 wanted 6 (Greer and McCarthy 1997), harvest-c11 wanted 182 (Pietrak et al. 2024). Skip right.
- Equisetum: nulls sweep-3:32 and harvest-c12:1, 2; chemical evidence oa-9:213 to 218, 299; light lead harvest-c12 wanted 2 (Guillon and Fievet 2003). Skip right.
- Artemisia: diel null desk-d1:9 and sweep-3:4; light (A. annua) and chemical evidence (A. tridentata, cana, douglasiana, indica) on main; many harvest-c11 leads. Skip right.
- Cardamine: diel null harvest-8:55, light null harvest-11:2 superseded by C. hirsuta light evidence (oa-10, oa-12), chemical evidence (C. hirsuta) on main, harvest-c12 wanted leads. Skip right.
- eye_type skipped for every genus: each has an eye_type record on main (desk-d1, harvest-c12:3, plant-1:5, sweep nulls). Right.
- The progress note's reason that Rumex sense_chemical "cannot take a null record" is right: `--check` refuses a genus-trait with evidence on main.

## Counts

- Search records: 0 of 0.
- Evidence: 1 of 6, 16.7%.
- Unit: 1 of 6, 16.7%.

Pooled with audits 83 to 90, from audit 90's figures (search records 48 in 1026; with evidence 52 in 1090):
- Search records: 48 in 1026, 4.7% (unchanged).
- With evidence included: 53 in 1096, 4.8%.

Forks that would change the count:
- Line 6. If the name rule reaches only the genus (audits 86 and 88 were genus cases), line 6 stands as a rename to Centaurea × gerstlaueri, and evidence would be 0 of 6. I count it, because the note asserts a POWO status that the cited POWO page contradicts, and the record would close a cell under a name POWO does not accept.
- Line 5. If plant sense_chemical belongs to the plant that responds, the measured response here is Taraxacum officinale's (exposure to C. stoebe root volatiles raised larval growth on the dandelion), and line 5 should be refiled under T. officinale (whose sense_chemical cell main already holds, canon-3:673). I keep it under C. stoebe because the owner's reading admits volatile signalling, and main files emitter-side volatile records for Rumex confertus. If the desk reads otherwise, evidence would be 2 of 6.

**Verdict: fail** on evidence (16.7%, above 5%), on one line; the other five records stand. With the line-6 fork read leniently, the unit passes at 0 of 6.

**Error lines to drop:**
- docs/views/searched/desk-d14.jsonl: none (no file).
- docs/views/evidence/desk-d14.jsonl: line 6 (or refile it as Centaurea × gerstlaueri with the note corrected). Line 5 should cite Plant Cell Environ 42(6): 1964-1973, 10.1111/pce.13534.

## Blocked pages

- The bioRxiv 441790v1 page served the full text without its abstract; the abstract was read from PMC6849603 (the published version).
- opendata.uni-halle.de served a bot-check page; authors came from its metadata.
- www-cambridge-org.ezproxyberklee.flo.org (a library proxy) was returned by a search and not opened.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
