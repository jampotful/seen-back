# Audit 103: desk-d13 (plant genera; branch origin/research/desk-d13, head 152992ed)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so error lines can simply be dropped.
- Search records: all 4 lines of docs/views/searched/desk-d13.jsonl (1 to 4).
- Evidence records: all 10 lines of docs/views/evidence/desk-d13.jsonl (1 to 10).
- Wanted lines: none (the file is empty).

## Gate

`python3 -I tools/views/screen_candidates.py --check` on a copy of the searched file (4 lines), with the empty wanted file, prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e) included), the counting rule of audit 39, and the rulings of audits 84, 86, 87 and 90. Audit 90 served as the format.

Queries. `harvest_get.py` ran without the network (it reads origin/ci). Achillea (line 4) is in harvest run 2: its four unprefixed queries ("Achillea phytochrome photoreceptor", "Achillea light perception", "Achillea phototropism", "Asteraceae photoreceptor review") match the harvest's query and family-review lines word for word and in order, with the "web: " lines after them. Cortaderia, Nasturtium and Cosmos are in no harvest run, and their records list "web: " lines only. No unlabelled line appears.

Chased.
- Line 4 names 10.1016/j.tree.2009.09.010, a citation step the harvest prints (0 works naming Achillea). Supported.
- Line 1 (Cortaderia) names 10.1007/s00239-004-0294-2 (Lariguet and Dunand 2005, doc.rero.ch 309979, as audit 90 established). My own "Poaceae photoreceptor review" search returned doc.rero.ch/record/309979 on the first page. Supported, as in audits 86, 87 and 90.
- Lines 2 (Nasturtium) and 3 (Cosmos) name the same DOI, but neither record lists any family-review search (each has two "web: " lines, both on flower opening or scent), and neither genus is in a harvest run. The Achillea harvest's "Asteraceae photoreceptor review" output does not print that DOI either (grep of the full output). No harvest or listed web search supports the DOI in these two records, which audit 90 counted as an error (its line 18).

Main. I checked origin/main (e564311a) docs/views/evidence and docs/views/searched for every genus in the unit.
- No unit search record names a trait main holds evidence for: main has no diel evidence for Cortaderia, Nasturtium, Cosmos or Achillea.
- All four unit search records repeat null search records already on main: Cortaderia diel (desk-c11:10, sweep-41:11), Nasturtium diel (desk-c11:13, sweep-41:23), Cosmos diel (desk-c11:17, sweep-43:22), Achillea diel (desk-c11:19, harvest-15:18, harvest-4:25, sweep-2:9). Audit 90 noted such a repeat without counting it, and I do the same.
- Evidence line 9 (Vachellia farnesiana sense_light_nonvisual, Chauhan, Campbell and Galea 2021, 10.1017/wsc.2021.54) repeats desk-d1:2 on main: same work, same DOI, same species, trait and value ("seed germination not affected by light; seeds nonphotoblastic"). Error.
- Evidence line 5 (Achillea collina sense_chemical, Giorgi et al. 2015) repeats desk-c11:3 on main: Manzo, Panseri and Giorgi 2013, the same group's conference abstract on the same species, trait and stimuli (aphid infestation, mechanical damage, jasmonic acid, HS-SPME) and the same finding (some volatiles appear only after treatment). The journal paper is the fuller source of one experiment, and the cell was already closed with that measurement. Error (fork below). The record's note says the cell "closes at genus level", which shows the unit did not see the main record.
- Lines 4 (Achillea millefolium light), 6 and 7 (Apocynum light), and 10 (Poa bulbosa chemical) are correct new works, but each adds a species to a cell main already holds (Achillea sense_light_nonvisual: desk-c11 A. fragrantissima, harvest-15 A. gypsicola; Apocynum sense_light_nonvisual: desk-c11 A. venetum; Poa sense_chemical: desk-d1 P. annua and P. pratensis). They neither repeat a main work nor contradict one (A. androsaemifolium's light-neutral germination agrees with A. venetum's), so they are noted, not counted.

Searches. I ran 27 WebSearches: 11 for the four null records (two or three each, flower opening, anthesis, floral biology and scent timing), 1 family review, 11 for evidence titles, and 4 for taxonomy. I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed.

## Search record verdicts (4)

| Line | Record | Verdict |
|---|---|---|
| 1 | Cortaderia diel | ok. Web-only, chased supported. My searches ("Cortaderia selloana anthesis time of day florets open morning pollen release"; "pampas grass Cortaderia flowering anthesis hour daily pattern pollen emission diurnal") returned plant patents, Herbiguide, the Washington weed board findings, GrassBase, Cal-IPC, UF fact sheet and nursery pages. No hour of floret opening or pollen release for a Cortaderia species. |
| 2 | Nasturtium diel | **error: unsupported chased.** No family-review search is listed and no harvest exists, so 10.1007/s00239-004-0294-2 has no support in the record. My two searches (scientific name with "flower opening time anthesis"; watercress floral biology, flowers open morning) returned the SJST Tropaeolum paper the record names, AGRIS, floras and encyclopaedia pages. No opening or scent hour, so no missed measurement. |
| 3 | Cosmos diel | **error: unsupported chased**, as line 2. My searches returned seed-company and nursery pages, the BIO REPRO 2017 abstract book (UFMS PDF opened: a C. sulphureus visitor study gives only its 08:30 to 15:30 observation window) and Malerbo-Souza et al. 2025 on C. sulphureus as a bee bioindicator (UEM page opened: bee visits 7:00 to 12:00, a visitor timing, no opening hour). A chocolate-cosmos (C. atrosanguineus) scent-rhythm search returned only Wikipedia, nursery pages and the general Frontiers 2016 scent review. No missed measurement. |
| 4 | Achillea diel | ok. Queries match the harvest, chased printed. My searches returned plant patents, the sunflower circadian floret work (Creux et al., Helianthus), Irish wildflower and extension pages, the KAIST scent-accumulation paper (other species), and Larue-Kontić and Junker 2016, J Poll Ecol 18(5) (pollinationecology.org PDF opened): A. millefolium terpene-inhibition volatiles sampled 12 h after treatment under an 11-h photoperiod, no time of day of opening or emission. No missed measurement. |

Search record errors: **2 of 4 (50%)**, lines 2 and 3.

## Evidence record verdicts (10)

| Line | Record | Verdict |
|---|---|---|
| 1 | Cortaderia selloana sense_chemical | ok. Penn State portal opened: Sellmer, Adkins, McCall and Whipker 2001, HortTechnology 11(2): 216-219, 10.21273/horttech.11.2.216. "All rates of uniconazole resulted in plant heights which were 56% to 75% shorter" is in the abstract. Growth retardants drenched on living plants count under 10(d). Grade m, partial right. |
| 2 | Nasturtium officinale sense_chemical | ok. PMC8763773 and the Springer page were returned by my title search; the record's Springer URL and DOI 10.1007/s00253-021-11743-8 agree with them. Elicitors on living in-vitro microshoots count, as audit 78 counted MeJA on in-vitro Digitalis shoots. POWO gives Rorippa officinalis as a synonym of Nasturtium officinale, so the genus is accepted. The abstract sentence itself I did not re-read (PMC redirected and I did not refetch), so the quote rests on the record. |
| 3 | Cosmos bipinnatus sense_chemical | ok. DOAJ record opened: Yu, Liu, Yang, Liu, Fan, Yang, Xu, Zeng, Xiao, Yang, Lei, Jiang, Li, Gao and Tao 2024, BMC Plant Biol 24(1), 10.1186/s12870-024-05526-2. The abstract states low MeJA raised seedling dry weight under Cd stress by limiting root-to-shoot Cd transport. Applied MeJA counts under 10(d). |
| 4 | Achillea millefolium sense_light_nonvisual | ok. seer.ufrgs.br page opened: Lima, da-Silva, Borella, Deuner, Freitag, Mariot and do Amarante, Rev Bras Biociênc 17(2), 2020. "In addition, the synthesis of phenols and flavonoids decreased in leaves and flowers of shaded plants." is verbatim. A set-light trial under full light against coloured shading nets counts. Cell already held on main (noted). |
| 5 | Achillea collina sense_chemical | **error: repeats main.** The source checks (air.unimi.it opened: Giorgi, Manzo, Nanayakkara, Giupponi, Cocucci and Panseri 2015, Nat Prod Res 29(18): 1695-1702, 10.1080/14786419.2014.997725), and WFO accepts Achillea collina (Becker ex Rchb.f.) Heimerl. But desk-c11:3 already logs the same group's aphid, damage and jasmonic-acid volatile experiment on A. collina with the same finding. |
| 6 | Apocynum cannabinum sense_light_nonvisual | ok. Cambridge Core page opened: Huebner, Invasive Plant Sci Manag 19 (2026), e3, online 12 December 2025, 10.1017/inp.2025.10034, CC BY-NC-ND. The quote is verbatim in Results and Discussion. Germination under set light levels counts. Cell already held on main (noted). |
| 7 | Apocynum androsaemifolium sense_light_nonvisual | ok. Cambridge Core page opened: Boyd and Hughes; "Prolonged exposure to light neither promoted nor inhibited germination." is verbatim. Volume 59 issue 4 and DOI 10.1614/WS-D-11-00022.1 are in the bioone URL my search returned (the page itself served no text). Cell already held on main (noted). |
| 8 | Vachellia karroo diel | ok. UP repository record opened (Robbertse, Du Toit and Annandale 2014, Am J Plant Sci 5: 2074-2093, 10.4236/ajps.2014.513223), and the repository PDF gives "they all open on the morning of day 1 and start wilting towards the end of day 2 of anthesis" in section 3.1.3. Flower opening of a named species counts as plant diel. POWO (77087189-1, opened) states Vachellia karroo (Hayne) Banfi & Galasso is accepted, so filing under Vachellia is right. |
| 9 | Vachellia farnesiana sense_light_nonvisual | **error: repeats main** desk-d1:2 (same DOI 10.1017/wsc.2021.54, same value). |
| 10 | Poa bulbosa sense_chemical | ok. HUJI portal opened: Ofir and Kigel 1998, Physiol Plant 102(2): 163-170, 10.1034/j.1399-3054.1998.1020202.x. The quote is verbatim. Applied ABA on living plants counts under 10(d). Cell already held on main (noted). |

Genus status. Every taxon is a name of an accepted genus: Vachellia karroo and Achillea collina were checked above, and Nasturtium officinale is accepted in POWO (Rorippa officinalis is its synonym). No record is filed under a synonym's genus.

Evidence errors: **2 of 10 (20%)**, lines 5 and 9.

## Cells the unit held open or skipped

- Tecoma sense_chemical: the lead is on main (harvest-c11 wanted line 80, the phytohormone germination PDF on thebiobrio.in, plus lines 81, 86 and 87). The hold is right. Main already has a null record for it (desk-c11:16), which those leads contradict; that is a main problem, not this unit's.
- Apocynum sense_chemical: lead on main (harvest-c11 wanted line 114, 10.1007/s44372-026-00880-x, applied SA on A. venetum germination). Hold right; main's null desk-c11:25 is likewise contradicted by its own wanted line.
- Apocynum diel: W2384640753 is named only in docs/tracks/progress/harvest-c11.md (line 1392), not on a wanted list. The cell already has a null on main (desk-c11:23), so writing nothing changes nothing.
- Vachellia sense_chemical: lead on main (harvest-c11 wanted line 141, somatic embryogenesis of V. farnesiana, 10.1007/s44415-025-00064-7). Holding is defensible, since growth regulators on living explants have counted (audits 78, 82).
- Poa diel: Liem 1980 on Poa annua anthesis is on main (desk-d1 wanted line 2, harvest-c18 wanted line 14). Hold right.
- Marchantia diel: skipping is right, but the reason is misattributed. Main holds no desk-d1 Marchantia search record; the null is sweep-29:24 (diel, eye_type, sense_chemical, sense_light_nonvisual).
- eye_type: every genus has an eye_type record on main (desk-c11:11, 14, 15, 18, 20, 24; desk-d1:3, 4), except Marchantia, which is covered by sweep-29:24, not desk-c11 or desk-d1 as the progress note says. Skipping is right.

## Counts

- Search records: 2 of 4, 50%.
- Evidence: 2 of 10, 20%.
- Unit: 4 of 14, 28.6%.

Pooled with audits 83 to 90, from audit 90's figures (search records 48 in 1026; with evidence 52 in 1090):
- Search records: 50 in 1030, 4.9%.
- With evidence included: 56 in 1104, 5.1%.

Forks that would change the count:
- Lines 2 and 3 (chased). If the desk accepts the Lariguet and Dunand DOI for a web-only plant genus without a family search listed in that record (the Cortaderia record in the same file did run one), both lines stand. Search records would then be 0 of 4. Strict reading kept, as audit 90 did for Olea.
- Evidence line 5. If "repeats main" means the same work only, line 5 stands, since its source (2015 journal paper) differs from main's (2013 conference abstract). Evidence would then be 1 of 10.

**Verdict: fail.** Search records fail at 50% and evidence at 20%. Both files were judged whole, so dropping the error lines leaves the rest of the unit standing.

**Error lines to drop:**
- docs/views/searched/desk-d13.jsonl: lines 2 and 3 (they can be rewritten with a supported chased, or with a none-reason).
- docs/views/evidence/desk-d13.jsonl: lines 5 and 9.

## Blocked pages

- www.ncbi.nlm.nih.gov PMC8763773 redirected to pmc.ncbi.nlm.nih.gov, which I did not refetch.
- complete.bioone.org (Boyd and Hughes) served meta tags only.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
