# Audit 114: desk-d24 (4 evidence records; branch origin/research/desk-d24, head dcab24ed)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so error lines can simply be dropped.
- Evidence records: all 4 lines of docs/views/evidence/desk-d24.jsonl.
- Search records: none (the unit has no searched file).
- Wanted lines: none (the unit has no wanted file).
- Leads the unit left alone: 4 spot-checked from its progress file (Dioscorea villosa/deltoidea, Ulmus, Acer platanoides, Melinis minutiflora), plus two "cell already closed" claims checked on main (Tecoma stans, Chenopodium album).

## Gate

The unit has no searched or wanted file, so `screen_candidates.py --check` has nothing to check. All 4 evidence lines parse as JSON. Quote lengths: 78, 105, 107 and 114 characters, each within 125 (the notes state 77, 104 and 113, one short each; not counted).

## Method

Judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), audit 39's counting rule, the rulings in the shared brief, and audits 111 to 113 as format. For each record I ran a title WebSearch, fetched URLs that search returned, and compared authors, year, journal, DOI, quote, value, method, conditions, grade and partial flag. Names were checked on POWO pages my searches returned. I checked origin/main (e7db7d4d) docs/views/evidence and docs/views/searched for every taxon and DOI. 13 WebSearches. The Frontiers /text page for the Pyrus paper (public-pages-files-2025 redirect) and PMC12414344 were not answered at the permission step and were not retried; the Frontiers PDF was read instead. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed.

## Evidence verdicts (4)

| Line | Record | Verdict |
|---|---|---|
| 1 | Typha domingensis sense_light_nonvisual (Carhuancho León et al. 2020, BMC Plant Biol 20: 377, 10.1186/s12870-020-02573-3) | **ok.** BMC page (opened): the quote is a whole abstract sentence, word for word; DT0d to DT20d dark treatments, constant 17.5 to 30 C and alternating regimes, 3 replicates of 33 seeds, 12 h photoperiod, PAR 85 +/- 9 under white fluorescent tubes, all match; the text adds "cattail seeds do not germinate in darkness at any temperature". Germination light/dark trial on living seed, 10(e). The page printed the first three authors and "et al."; the title and DOI match the search result. Wording to fix, not counted: the Methods list five populations (Badajoz, Cuenca, Madrid, Seville, and Toledo for validation), where the record says four. POWO acceptance rests on the record's citation; main files no Typha domingensis line. |
| 2 | Triadica sebifera sense_chemical (Shah et al. 2020, Front Plant Sci 11: 216, 10.3389/fpls.2020.00216) | **ok.** Frontiers PDF (opened): the quote is verbatim, a whole Results sentence ending "(Figure 1B)."; Methods give half MS with 0, 100, 150, 200 mM NaCl and 0, 100, 200, 300 mM mannitol and de-coated seeds; Results give survival 30 +/- 5 and 10 +/- 5% without KAR1 and 90 +/- 5 and 80 +/- 10% with it; the Results do print "200 nM NaCl" against mM in Methods, as the record says. The 14 authors in the record's order match the Frontiers text page. A living seed's response to applied karrikin is an elicitor/hormone-type response inside 10(d). POWO 256588-2 (opened): "This species is accepted"; Triadica is the genus main already files (harvest-c7:25, sweep-26:37). Filing the paper's Sapium sebiferum under the accepted Triadica sebifera is right; the fetched POWO page printed no names under its homotypic-synonym heading, so the synonymy itself rests on the record and main's sweep-26:37 query. |
| 3 | Androsace villosa sense_light_nonvisual (Arslan, Kirmizi, Güleryüz, Sakar 2011, Acta Biol Cracov Ser Bot 53(2): 32-36, 10.2478/v10182-011-0029-9) | **ok.** journals.pan.pl PDF (opened): authors in order, year, volume, issue, pages and DOI printed on the paper itself match, so the citation is the Androsace paper's and not the Dioscorea lead's (that lead is Butuzova and Torshilova 2025, Bot Zhurn 110(2): 135-149, 10.31857/S0006813625020022, a different DOI, authors and year; confirmed on journals.rcsi.science). Quote verbatim, a whole sentence; controls 24% in darkness and 0% under photoperiod; 15 days chilling at 4 C; GA3 100, 150, 250 ppm; Uludag seeds. Abstract-level sentence, `partial` true, grade m. POWO ipni 700470-1 (opened): "This species is accepted." Wording to fix, not counted: the PDF gives continuous darkness at 20 C but the photoperiod at 20/10 C, so "each germinated ... at 20 C" in `method` is wrong for the photoperiod arm (the comparison is confounded with temperature, which the value should say). |
| 4 | Pyrus betulifolia sense_chemical (Wang, He, Li, Bai, Teng, Hui 2025, Front Plant Sci 16: 1667946, 10.3389/fpls.2025.1667946) | **error (quote not a whole sentence).** Frontiers PDF (opened): authors, volume and article number match, and the words are verbatim, but the sentence goes on after "non-dormant seed coats" with "(Figure 2C), suggesting that dormant seed coats function similarly to exogenous ABA in preventing embryo ..." with no period at "seed coats"; the fetch also reported the full sentence as over 125 characters. The note's "returned whole by the first fetch" is wrong. Doses: the PDF prints "100 mM ABA" (Results 2.2 and the Figure 2, 3 and 4 legends), "10 mM fluridone" and "100 mM GA3 or GA4+7" (Figure 5 legend), and the Methods print no concentration, so the record reports the printed unit faithfully; 100 mM ABA (about 26 g/L) is far above any usual dose and is very likely a micromolar typo in the paper, which the record flags; the value must not be used as a dose. 82.22% (fluridone, 13 days) and 8.70% (intact dormant) match. Trait: applied ABA suppressing germination of living embryos and seed is a hormone response on living tissue, inside the owner's 10(d) reading. Further fault, not counted: the Methods give 22 +/- 2 C with 16 h light; 21 C belongs to the post-stratification germination of Results 2.1, so "21 C" in `conditions` is wrong. Name: the paper spells betulaefolia throughout; main already files Pyrus betulifolia (desk-d11:7). |

Repeats of main: none. Main holds no evidence for Typha domingensis, Triadica, Androsace or Pyrus betulifolia sense_chemical, and none of the four DOIs is in any evidence or searched file on main. Main's Pyrus genus-level sense_chemical line (desk-d11, 10.1023/b:joec.0000006671.53045.16) and Typha latifolia lines are other taxa or papers. Main's null records sweep-26:37 (Triadica, sense_chemical) and sweep-16:26 (Typha, sense_light_nonvisual) are contradicted by lines 1 and 2, main's fault, not counted.

## Leads left alone (spot-checked, not counted)

| Lead | Unit's reason | My check |
|---|---|---|
| Dioscorea villosa/deltoidea (10.31857/S0006813625020022) | temperature stratification only | **Confirmed.** journals.rcsi.science (opened): stratification regimes only; seeds kept in the dark and moved to light once germination began, with no light/dark or hormone comparison. |
| Ulmus (Nomiya 2010, J For Res 15: 123-130, 10.1007/s10310-009-0165-1) | one 16 h dark/8 h light regime, no dark treatment | **Confirmed for the abstract** (Springer page opened): U. davidiana var. japonica, U. laciniata and U. parvifolia under one 16/8 h regime. One sentence of about 106 characters says U. laciniata responded negatively to "favorable light conditions", but it compares conditions within a regime and gives no dark control; the skip stands. |
| Acer platanoides ABA/GA proteome (10.1186/1471-2229-9-48) | no doses in abstract, proteome result | **Confirmed as far as read.** The BMC figure page (opened) names water, ABA and GA imbibition with stratification at 3 C but no concentrations or percentages; the full text was not read. |
| Melinis minutiflora (10.1590/S0101-31222009000300019) | no light/dark sentence; chemical cell closed | **Unchecked for the lead** (my search did not return it). Pointer: Martins, Hay and Carmona 2009, Revista Árvore 33(4): 713-722 (redalyc PDF opened) ran germination in light at 20-30 C and in foil-wrapped darkness at 25 C on two cultivars; light and temperature are confounded, so it may not settle the cell. Main holds Melinis minutiflora sense_chemical only (desk-d10). |
| Tecoma stans, Chenopodium album | cell already closed | **Confirmed** on main: Tecoma stans sense_light_nonvisual (sweep-44); Chenopodium album sense_chemical (desk-d11) and sense_light_nonvisual (oa-12, oa-13b, sweep-16). |

## Counts

- Search records: 0 of 0.
- Evidence: 1 of 4 (line 4).
- Unit: 1 of 4, 25%.

Pooled with audits 83 to 90, from audit 113's figures (search records 48 in 1026; with evidence 54 in 1104):
- Search records: 48 in 1026, 4.7% (unchanged).
- With evidence included: 55 in 1108, 4.96%.

**Verdict: fail** (evidence 1 of 4, above 5%). Lines 1 to 3 stand and can merge.

**Error lines to drop:**
- docs/views/evidence/desk-d24.jsonl: line 4 (Pyrus betulifolia, quote not a whole sentence). It can return with a whole sentence of 125 characters or fewer, `conditions` corrected to 22 +/- 2 C, and the doses kept marked "as printed, unit doubtful".

Follow-ups:
- Line 1: "four Spanish populations" should read five (four modelled, Toledo for validation).
- Line 3: the photoperiod arm ran at 20/10 C, the darkness arm at 20 C; say so in `method` and the value.
- Main's null records sweep-26:37 (Triadica) and sweep-16:26 (Typha) should be re-opened when lines 1 and 2 land.
- Melinis minutiflora sense_light_nonvisual: Martins et al. 2009 (Revista Árvore) is a candidate, confounded with temperature.
