# Audit 68: harvest-52 (desk screening unit), 19 October 2026

Unit: branch `research/harvest-52`, commit a0b9b3e4; 64 search records, 14 wanted lines (the saved copies in /tmp/au68 are identical to the commit's files). Rules: `docs/tracks/prompts/desk-audit.md`, with points 8 and 9 of `desk-screen.md`. No ResearchGate, academia.edu, Sci-Hub, LibGen, proxy or mirror page was opened (several results with `libproxy` and `elogim` hosts and academia.edu pages came back and were left shut), and no paper text is committed.

## 1. Mechanical gate

`python3 -I tools/views/screen_candidates.py --check harvest-52.jsonl --wanted harvest-52-wanted.jsonl` printed "0 problems".

## 2. Sample (drawn before reading any record)

`random.seed(68)`, `random.sample` of the 64 lines in file order, 20 line numbers (1-based):

8, 16, 17, 22, 24, 28, 29, 31, 33, 36, 38, 39, 44, 45, 47, 48, 53, 59, 60, 61

## 3. Checks

(a) Queries: for the 12 genera (Peponapis, Heteroecus, Ennomos, Gazella, Clostera, Hypothymis, Regina, Dicymolomia, Phimenes, Cacomantis, Sparganothis, Tetrastes) `harvest_get.py` was run and its query lines (genus queries, then the family review) compared with the non-"web: " queries of each record: all 20 match word for word, in order, and no output shows "gave up". Every record also lists its "web: " searches.
(b) Chased: every record gives a reason the output supports. Where the output shows citation steps (Ennomos, Clostera, Dicymolomia, Sparganothis) the "0 works naming the genus" counts match the printed lines; for the other genera the harvest printed no citation step and the record says so.
(c) Screened: every `screened` entry (all of them, 1 to 12 per record) was read against the abstract the harvest printed or a page my own search returned. None reports a measurement of the trait. The Cacomantis entry for Aidala et al. 2012 (10.5122/cbirds.2012.0035) was checked against a scispace page my search returned: it covers Chrysococcyx lucidus and Urodynamis taitensis only, with no Cacomantis.
Canon (point 8): for each of the 20 records I compared the `canon` field with the canon file's entries for the trait and the taxon's group; every entry that covers the group is named (for example Peitsch, van der Kooi, Longcore and Margetts for Heteroecus and Phimenes spectral_range_nm; Olsson, Odeen and Hastad, Hunt, Toomey, Martin, Longcore and Margetts for Cacomantis). None is missing.
Point 9: the unit holds no spectral_range_nm record for a moth genus (its spectral_range_nm records are Peponapis, Heteroecus, Hypothymis, Phimenes, Cacomantis and Tetrastes), so the Nowinszky et al. 2022 table (canon-22) changes no verdict here. Main's two stores hold no row for any of the audited genera except Gazella dorcas (pupil_shape, diel), Bonasa umbellus and Lyrurus (Tetrastes' relatives, not the genus), and Eupetomena macroura (oil_droplets, sweep-55); none touches an audited cell.
(d) Own searches (about 50 WebSearch calls): the two trait searches for each genus and trait group (Peponapis, Heteroecus, Ennomos, Gazella for two groups, Clostera, Hypothymis for three groups, Regina for two, Dicymolomia, Phimenes for two, Cacomantis, Sparganothis, Tetrastes), and a third search of my own for each genus: squash bee eye anatomy; Cynipidae eye/ERG; Geometridae ERG flicker; Notodontidae eye/ERG; Crambidae flicker; Tortricidae ERG; Eumeninae eye; gazelle retina topography; snake opsins in Regina; cuckoo SWS1 (two searches); hazel grouse retina; Monarchidae retina. Pages opened were only URLs those searches returned.

## 4. Verdicts (20 records)

| line | genus / trait | verdict | reason |
|---|---|---|---|
| 8 | Peponapis corner_hz | confirm | queries match; two screened entries are bee eye anatomy and a remote-sensing thesis; no flicker or corner-frequency work for any squash bee found; Kelber and Somanathan 2019 (Insects 10: 418) text does not name Peponapis |
| 16 | Heteroecus spectral_range_nm | confirm | all four canon compilations named; searches return Trybliographa (figitid) and Pimpla, not Heteroecus; no cynipid measurement found |
| 17 | Ennomos cff_hz | confirm | citation steps and family review as printed; the Helicoverpa light-intensity work is correctly screened; none of my searches found a geometrid flicker value |
| 22 | Gazella absolute_sensitivity | confirm | no search returned a gazelle dim-light threshold (results were chemical-network papers and a diagnostic device named Gazelle) |
| 24 | Gazella fov_h_deg | confirm | no gazelle visual-field value found; Hughes 1977 and Heesy et al. 2011 are named in `canon`; my retina search returned only cat ganglion-cell papers |
| 28 | Clostera corner_hz | confirm | nothing for Clostera or Ichthyura; Lu and Kronforst 2025 (EcoEvoRxiv review of Lepidoptera eyes) does not name the genus and covers no corner frequency |
| 29 | Hypothymis acuity_cpd | confirm | the dawn-chorus eye-size paper is eye size, not acuity; no monarch flycatcher acuity found |
| 31 | Hypothymis binocular_deg | confirm | Martin 2007, Martin 2017 and Tyrrell and Fernandez-Juricic 2017 S1 named; no direct measurement found |
| 33 | Hypothymis cff_hz | confirm | warbler infection paper is plainly irrelevant; no bird flicker value for the genus found |
| 36 | Regina fov_h_deg | confirm | no snake visual-field value found; the Frontiers in Neuroanatomy paper behind the Regina wanted line is Tashiro, Ventura and Hauzman 2022 on Bothrops jararaca and Crotalus durissus only |
| 38 | Regina receptor_classes | confirm | Kelber, Simoes, Hauzman and Katti named; the Simoes manuscript names no Regina; twelve screened entries are plainly off-topic or canon |
| 39 | Dicymolomia cff_hz | confirm | 0 citing works; no crambid flicker value found (Dodt 1954 Experientia, the untitled Springer BF02160841 hit, is vertebrate ERG) |
| 44 | Phimenes corner_hz | confirm | no eumenine flicker found |
| 45 | Phimenes colour_vision | confirm | Kelber 2003 and van der Kooi 2021 named; no eumenine colour measurement found |
| 47 | Phimenes receptor_classes | confirm | five compilations named; none logged for a eumenine on main |
| 48 | Phimenes spectral_range_nm | confirm | four compilations named; Dryad Nasonia dataset covers Nasonia only |
| 53 | Cacomantis spectral_range_nm | confirm | eight canon compilations named; the NZ cuckoo SWS1 paper and Aidala's 2015 dissertation name Chrysococcyx and Urodynamis, not Cacomantis |
| 59 | Sparganothis corner_hz | confirm | tortricid eye work found is on Lobesia, Grapholita and Cydia, other genera, on spectral and pupil traits |
| 60 | Tetrastes acuity_cpd | confirm | the black grouse study measures Lyrurus tetrix alone (audit 64); vulture and review entries screened correctly; no hazel grouse retina found |
| 61 | Tetrastes interreceptor_deg | confirm | same as line 60 |

## 5. Errors and rate

Errors: **0 of 20**, so the 95% upper bound is about 17% for this unit alone (a sample of 20 cannot bound it tighter). Rate for this audit: **0%**.
Pooled with audits 43 to 51 and 55 to 67 (4 errors in 497 records): **4 errors in 517 records, 0.8%**.
Verdict: **pass** (under 5%). No second sample (seed 6801) was drawn because no error was found.

## 6. Wanted lines (checked, not counted)

- Frontiers in Neuroanatomy 2022 (10.3389/fnana.2021.770804), Regina acuity_cpd and fovea: the DOI and year are right, the title and authors are blank. The page names Tashiro, Ventura and Hauzman and the paper studies two viperids; it holds no Regina, so the line can be dropped.
- Kelber and Somanathan 2019, Insects 10(12): 418 (Peponapis acuity): DOI and year right, authors blank (Kelber, Somanathan); the page text does not name squash bees and Tables 1 to 4 are images, so the lead stays open for the tables.
- "Behavioral spectral sensitivity in the hummingbird: a peak in the UV" (Eupetomena): the USP repository page gives the authors Frutuoso, Pardi and de Souza, 1997, IOVS 38(4): S1016, a conference abstract with no abstract text or species; the line leaves authors and journal blank.
- Not checked against a page: the Linnean Society 2023 paper (10.1093/biolinnean/blac154; authors blank), the Cardiff 2009 thesis and the remaining wanted lines.

## 7. Leads that could change a verdict (species list unseen)

- Heesy 2004 (orbit orientation and binocular overlap in mammals), Heesy, Kamilar and Willms 2011 and Hughes 1977 (canon, not in hand): lines 24 (Gazella fov_h_deg), and any Gazella binocular_deg record in the unit.
- Kopania and Clark 2024 (mammal retinal specializations, main holds 252 taxa; its bovids are cattle, goat and sheep) and PMC5705735 (body, brain and eye size against acuity), Motani and Schmitz 2011, PMC9487202 (tapetum): bear on the unsampled Gazella acuity and tapetum cells, not on lines 22 or 24.
- Hauzman et al. 2018 (12 colubrids) and Katti et al. 2019 (canon, not in hand): line 38 (Regina receptor_classes); the Simoes manuscript names no Regina.
- Martin 2007, Martin 2017 and the S1 Table of Tyrrell and Fernandez-Juricic 2017 (canon): line 31 (Hypothymis binocular_deg); Caves et al. 2018 and Martin 2017 for line 29.
- Hunt et al. 2009, Toomey et al. 2016, Longcore 2023 and Margetts et al. 2024 (canon, not in hand): line 53 (Cacomantis spectral_range_nm); Aidala's 2015 CUNY dissertation sequenced SWS1 across four avian lineages and its per-species table was not visible (line 53; also the unsampled Cacomantis lambda_max_nm).
- Haarlem et al. 2026 and Warrant and Nilsson 2006 (canon): the flicker and corner lines for Ennomos, Clostera, Dicymolomia, Sparganothis, Peponapis, Phimenes and Hypothymis (lines 8, 17, 28, 33, 39, 44, 59).
- Chan et al. 2024 (Research Square, 224 Lepidoptera species, eye morphology) and Kelber and Somanathan 2019 tables: bear on the acuity and interommatidial cells of Lithacodes, Ennomos, Clostera, Dicymolomia, Sparganothis and Peponapis, none of them a sampled record.
- Nowinszky et al. 2022 (canon-22 lamp-comparison table): its species list was not visible; it bears on spectral_range_nm only, and the unit has no moth spectral_range_nm record, so no verdict here depends on it. Eupetomena was not in the sample; its records were not audited.

## 8. Searches

About 50 WebSearch calls, all inside the ration; all 20 records were finished.
