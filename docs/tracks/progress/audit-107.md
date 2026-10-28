# Audit 107: desk-d18 (8 evidence records; branch origin/research/desk-d18, head 630a7845)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so error lines can simply be dropped.
- Evidence records: all 8 lines of docs/views/evidence/desk-d18.jsonl. Every one is abstract-only (or read through a summary tool) and carries "partial": true. Every one is grade m.
- Search records: none (the unit has no searched file).
- Wanted lines: none (the unit has no wanted file).

## Gate

The unit has no searched or wanted file, so `screen_candidates.py --check` has nothing to check. All 8 evidence lines parse as JSON.

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e) included), the counting rule of audit 39, the rulings of audits 84 and 86 to 90, and the rulings of audits 88, 96, 104 and 105, where these leads were first found. For each record I ran a title WebSearch, fetched a URL that search returned, and compared authors, year, journal, DOI, quote, value, trait, grade and partial flag. I checked genus names on POWO/WFO pages my searches returned. I checked origin/main (af1f0b7f) docs/views/evidence and searched for every genus.

Searches: 13 WebSearches (8 for evidence titles, 5 for taxonomy). I fetched only URLs my searches returned. One search returned a www-cambridge-org.ezproxyberklee.flo.org result, which is a library proxy, and I left it alone. The PMC page for Wala et al. 2021 raised a permission request that went unanswered, so I did not retry it. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed.

## Evidence verdicts (8)

| Line | Record | Verdict |
|---|---|---|
| 1 | Senecio olympicus sense_chemical (Kırmızı, Güleryüz, Arslan 2011, Plant Species Biol 26(1): 51-57, 10.1111/j.1442-1984.2010.00302.x) | **ok, wording to fix.** The Uludağ repository page (opened) gives the authors, journal, pages, year and DOI, and the abstract's statement that chilling with GA3 under DSDL raised S. olympicus germination from 45 to 87%. That is an applied-hormone response of living seed, 10(d). Two wording faults, not counted: DSDL is "daily short-time dim light", so `conditions` "constant 20 C in darkness" leaves out the dim light; and the abstract calls 250 ppm GA3 at 20/10 C with photoperiod "an efficient way" to germinate all three species, not the best. Genus Senecio is accepted (WFO snapshot wfo-4000035060-2024-12, opened). Species status is **unchecked**: two more searches returned no POWO or WFO page for Senecio olympicus Boiss., and the europlusmed page was blocked by a bot wall. |
| 2 | Ratibida columnifera sense_chemical (Stahnke and Reese 2000, Proc S Dak Acad Sci 79: 175) | **ok.** The openprairie page (opened) confirms the authors, year, journal, the eight species with Ratibida columnifera (Nutt.) Woot. & Standl. as the only Ratibida, and the sentence that Liatris and Ratibida "showed no improvement" after ethephon. This is the rewrite audit 105 asked for (species, grade m). Main files no-response results as evidence: desk-c11 and desk-d1 hold whole-null light trials ("light did not affect seed germination", "seeds nonphotoblastic"), and several GA3 records hold partial nulls (Polygonatum odoratum, Prunus spachiana). So a measured null response to an applied ethylene releaser belongs here. The value says what the abstract says: most viable seed germinated without treatment, so the null is a ceiling, and the record does not claim that the seed cannot sense ethylene. |
| 3 | Aquilegia barbaricina sense_chemical (Porceddu, Mattana, Pritchard, Bacchetta 2017, Plant Biol 19(6): 983-993, 10.1111/plb.12610) | **ok.** The IRIS Cagliari page (opened) confirms the citation, the quote with the repository's missing spaces, 250 mg/L GA3, and the abstract's statement that W+C effects "are only partially mimicked" by GA3. Hormone response of living seed, 10(d). |
| 4 | Tropaeolum majus diel (Silva et al. 2011, An Acad Bras Cienc 83(4), 10.1590/s0001-37652011005000046) | **ok.** The SciELO page (opened) gives the six authors and the quoted sentence ("the anthesis is diurnal and the flower duration is six days, on average"), and Astylus variegatus visiting from 7 am to 5 pm with a peak at 9 to 11 am. No opening hour is given, and the record says so. Diurnal anthesis is flower-opening timing, the owner's reading of plant diel. I did not check volume and pages against a page. Main holds T. majus sense_chemical and sense_light_nonvisual evidence (desk-d11) but no diel, so this does not repeat main. Main's wanted line harvest-c11:31 is the same paper and can now be retired. |
| 5 | Hamamelis virginiana sense_chemical (Rehill and Schultz 2012, J Chem Ecol 38(5): 496-498, 10.1007/s10886-012-0115-9) | **ok, under a strict reading.** The AGRIS page (opened) confirms the citation, Hamamelis virginiana, galls with higher condensed and lower hydrolyzable tannins than leaves, and "Galled and ungalled leaf laminas never differed significantly in any phenolic measure." Strict judgement: the gall-against-leaf comparison by itself sets two different organs side by side, and the authors read it as aphid manipulation or carbon storage rather than defence, so on its own it would be tissue chemistry. But the gall exists only because the aphid induced it on a living leaf, and the galled-against-ungalled lamina comparison is a proper herbivore-induced test with an uninduced control. That test is a measured living response, with a null result. Neither is processed tissue in the owner's sense (extracts, oils, cut material): every induced-chemistry record on main assays harvested tissue. Audit 96 counted this paper as a missed measurement. Fork below. |
| 6 | Veronica serpyllifolia diel (Godin 2017, Rastitelnyi mir Aziatskoi Rossii 4(28): 42-46, 10.21782/RMAR1995-2449-2017-4(42-46)) | **ok.** The sibran.ru issue PDF (opened) gives the article, author, issue, pages and DOI, and the Russian sentences: opening begins at 7 am at 17 to 18 C, the number of open flowers peaks before noon and at midday, and opening stops completely at 18 to 20 h. I did not see the "falls sharply from 14 h" clause in the fetch summary. This is flower-opening timing of a named species. `access` "open" with "partial": true matches the note (read through a summary tool). |
| 7 | Hypochaeris radicata sense_chemical (Wala, Kołodziejek, Patykowski 2021, PLOS ONE 16(1): e0244737, 10.1371/journal.pone.0244737) | **ok.** The IDEAS/RePEc page (opened) confirms the authors, journal, year and DOI, the quote ("Hypochaeris radicata had no preference and wide tolerance"), and "High concentrations of nitrogen-containing salts inhibited completion of germination in almost all species". The record is filed under sense_chemical as a germination response of seed to nitrate and ammonium, the cue 10(e) names, and does not claim ion uptake. The trait fits. The abstract does not say whether H. radicata itself was stimulated or inhibited against the water control, and the record's value does not say either; "high concentrations inhibited most" is attributed to the ten species, as the abstract does. Main holds H. radicata diel and light evidence (sweep-19), with no sense_chemical, so this is no repeat. |
| 8 | Centaurea × gerstlaueri sense_light_nonvisual (DiTommaso et al. 2021, Weed Sci 69(1), 10.1017/wsc.2020.86) | **ok.** The BioOne page (opened) gives the five authors in the record's order, Weed Sci 69(1), 14:10 h light:dark against continuous darkness, and the quoted sentence verbatim. It was published online on 3 December 2020, and 2021 is the issue year. POWO urn:lsid:ipni.org:names:191031-1 (opened) says "This name is a synonym of Centaurea × gerstlaueri", so filing under the accepted name repairs the fault audit 104 counted on desk-d14:6, which is no longer on main. A germination light/dark trial is sense_light_nonvisual. |

## Repeats and contradictions of main

- Repeats: none. No genus here has evidence on main for the same species and trait. Main's only Senecio sense_chemical evidence is sweep-9:14 (Senecio articulatus, inflorescence odour), a different species. Audit 105 asked whether that species belongs in Curio, but the question does not touch line 1.
- Contradictions of main null search records (main's faults, not counted against this unit, as audit 104 ruled): sweep-9:33 (Senecio), sweep-15:5 (Ratibida), sweep-9:1 (Aquilegia), sweep-26:36 (Tropaeolum), harvest-19:11 and sweep-20:9 (Hamamelis), harvest-2:8 and sweep-2:5 (Veronica), sweep-19:36 (Hypochaeris), sweep-5:6 (Centaurea). Each evidence line now closes a cell that one of these records called empty.

## Counts

- Search records: 0 of 0.
- Evidence: 0 of 8.
- Unit: 0 of 8, 0%.

Pooled with audits 83 to 90, from audit 90's figures (search records 48 in 1026; with evidence 52 in 1090):
- Search records: 48 in 1026, 4.7% (unchanged).
- With evidence included: 52 in 1098, 4.7%.

Forks that would change the count:
- Line 5 (Hamamelis). If the desk reads gall tannin chemistry as tissue chemistry under 10(a), and does not count the galled-against-ungalled lamina null as an induced-response test, line 5 is an error. Evidence would then be 1 of 8 (12.5%), which fails, and the line would be dropped. I count it as ok because the lamina comparison is an herbivore-induced test with an uninduced control, and audit 96 counted the paper as a measurement.
- Line 2 (Ratibida). If the desk wants a null response logged only when the seed was dormant enough to show an effect, line 2 is an error (1 of 8). I count it as ok because main already logs whole nulls, and the value states the ceiling.
- Line 1 (Senecio olympicus). The species name stays unchecked against POWO/WFO. The genus is accepted, which is the level audits 86 and 88 ruled on.

**Verdict: pass.** 0 of 8 evidence records are errors. Lines 1 and 2 have wording to fix (line 1's `conditions` and "best"), which is not counted.

**Error lines to drop:**
- docs/views/evidence/desk-d18.jsonl: none.

Follow-ups:
- Line 1: correct `conditions` to "20 C in darkness with daily short-time dim light (DSDL)" and "best" to "an efficient way". Check Senecio olympicus Boiss. on POWO when the site opens.
- Retire main's wanted line harvest-c11:31 (Silva et al. 2011), which line 4 fills.
