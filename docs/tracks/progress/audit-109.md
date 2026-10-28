# Audit 109: desk-d20 (4 evidence records, lead-reading unit; branch origin/research/desk-d20, head a5b54c6b)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so error lines can simply be dropped.
- Evidence records: all 4 lines of docs/views/evidence/desk-d20.jsonl. All are plant sense_chemical, grade m, "partial": true.
- Search records: none (the unit has no searched file).
- Wanted lines: none (the unit has no wanted file).
- Leads the unit left alone (docs/tracks/progress/desk-d20.md): 5 spot-checked, 1 more attempted (below).

## Gate

The unit has no searched or wanted file, so `screen_candidates.py --check` has nothing to check. All 4 evidence lines parse as JSON.

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), the counting rule of audit 39, and the rulings of audits 84 and 86 to 90, with audits 90 and 107 as the format. For each record I ran a title WebSearch, fetched a page that search returned, and compared authors, year, journal, DOI, quote, value, method, conditions and the owner's reading. I checked origin/main (51d38503) docs/views/evidence for every species and genus in the unit.

Searches: 13 WebSearches (4 evidence titles, 1 POWO, 8 for left-alone leads). I fetched only URLs my searches returned. PMC9319471 (Ambrosia) raised a permission request that went unanswered and was not retried; the MDPI and DOAJ pages were used instead. A 0-doi-org.brum.beds.ac.uk result (library proxy) and a springerlink.bibliotecabuap.elogim.com result were left alone. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed.

## Evidence verdicts (4)

| Line | Record | Verdict |
|---|---|---|
| 1 | Gaillardia aristata sense_chemical | ok. MDPI page opened: Peterson, Gardner and Fraser 2025, Fire 8(10): 382, 10.3390/fire8100382. The quote is verbatim, a whole sentence in Discussion 4.2. The abstract lists "Gaillardia aristate" among the nine species with decreased germination. Method (0, 1, 10, 20, 100% smoke-water, three replicates of 15 to 25 seeds) and conditions (20 C, indirect light, 12 h light/12 h dark) match Section 2.4. Smoke on living seed counts under 10(e). POWO 317387-2 (returned by my search) accepts Gaillardia aristata Pursh. Wording to fix, not counted: the source says "no germination response at the 100% treatment", which the value reads as zero germination; the record also omits the 24 h soak and 90-day 4 C stratification. "partial" is conservative, since Discussion text was read. |
| 2 | Ambrosia artemisiifolia sense_chemical | ok. MDPI and DOAJ pages opened: Šćepanović, Košćak, Pismarović and Šoštarčić 2022, Plants 11(14): 1888, 10.3390/plants11141888. DOAJ returns the quote verbatim as one whole sentence. Conditions (25/15 C, 12 h photoperiod, 40 to 50 umol m-2 s-1) match the MDPI page. Applied ethylene and GA3 on living seed count under 10(d). Abstract-only, partial: right. Wording to fix, not counted: the abstract says germination was "improved ... by 88 and 95%", while the value says germination was raised to those figures; the value should keep the abstract's "by". |
| 3 | Phytolacca americana sense_chemical | ok. Frontiers full text opened: Neller, Klenov and Hudak 2016, Front Plant Sci 7: 283, 10.3389/fpls.2016.00283. The quote is a whole abstract sentence, verbatim. Methods give 5 mL of 5 mM JA in 0.5% ethanol, ethanol controls, four-leaf plants, leaf harvest 24 h later; Results give 8,264 transcripts at FDR < 0.05, a 2,770 subset (FDR < 0.001, FC >= 4) and 2,067 (75%) of those increased. All match. A sprayed living plant's hormone response counts under 10(d). Phytolacca americana L. is accepted (the record's POWO id; not re-opened). |
| 4 | Daucus carota sense_chemical | **error: wrong value.** Frontiers full text opened: Wang, Wu, Chen, Xu, An, Ren and Xiong 2024, Front Plant Sci 15: 1467957, 10.3389/fpls.2024.1467957. The quote is a whole abstract sentence, verbatim, and the design (cv. 'Kurodagosun', pots, weekly root irrigation from 38 d, five times, water control, roots at 70 d) matches. But the Methods give "300 mL of 100 μM MeJA (MeJA100), 200 μM MeJA (MeJA200)", and the record's value says "100 or 200 mM", a thousandfold error in the dose that reaches the owner's page. Repaired to "100 or 200 μM (300 mL per pot)", the line would stand: MeJA applied to intact living plants counts under 10(d), as for line 3. |

Repeats of main: none. Main holds sense_light_nonvisual only for Gaillardia aristata (desk-c7), Ambrosia artemisiifolia (sweep-6, recheck-quotes-3) and Daucus carota (sweep-5 and one other), and no Phytolacca evidence. None of the four DOIs is on main. Line 4 fills the Daucus sense_chemical cell that audit 90 found missed in desk-c12:6.

Genus status. Gaillardia, Ambrosia, Phytolacca and Daucus are accepted genera, and each binomial is its own accepted name.

## Leads left alone (spot check of 5)

| Lead | Unit's reason | Verdict |
|---|---|---|
| 14 Platanus occidentalis (Sperry and Chaney 1999, J Arboric / AUF 25(1): 43-47, 10.48044/jauf.1999.007) | growth retardants outside the hormone/elicitor readings | **error: missed readable measurement.** 10(d) names "an applied hormone, growth regulator or elicitor", and main logs paclobutrazol and uniconazole drenches under sense_chemical (desk-d13, Cortaderia selloana). The auf.isa-arbor.com page (opened, no login) gives, for American sycamore, phototropic curvature not significantly reduced and height growth stimulated at 0.5 and 1 ppm paclobutrazol and 0.5 ppm flurprimidol, with 5 ppm having no effect. Main holds no Platanus evidence, so the cell is open. |
| 8 Daucus carota (Rosińska, Andrzejak and Kakkerla 2023, Agriculture 13(4): 749) | melatonin priming not clearly a hormone or elicitor response | not counted. The MDPI page (opened) gives osmopriming at 25 to 200 µM melatonin raising germination by about 7 to 14% and 35 to 43% in two seed lots, which reads as a growth-regulator response under 10(d). But the unit's line 4 closes the same cell, so no open cell was lost. |
| 46 Bidens alba (Ye et al. 2025, Biology 14(10): 1310) | samples other Bidens, detached flowers | ok. MDPI page (opened) names B. pilosa var. radiata, B. frondosa and B. pilosa var. pilosa; flowers were collected and put in vials. |
| 58 Solanum nigrum (Ma et al. 2025, IJMS 26(23): 11757) | temperature only, GA/ABA measured not applied | ok. MDPI page (opened): only hypochlorite sterilisation applied; one 12 h/12 h regime, no light comparison. |
| 22 Ptelea (Floral Aromatics of Ptelea, JASHS 2021, 10.21273/jashs05119-21) | sampling of living flowers unknown | ok. DOAJ abstract (opened) says only that volatiles "emitted by flowers" were analysed; whether flowers were attached is unknown, and 10(a) excludes cut-flower sampling. |
| 12 Ficaria verna (Topolska et al. 2026, Sci Rep) | nature.com blocked, no abstract | unchecked: my search did not return the paper's page. |

## Counts

- Evidence: 1 of 4, 25.0% (line 4).
- Leads left alone, spot-checked: 1 of 5 a missed readable measurement (Platanus).
- Unit: 2 of 9 judged items, 22.2%.

Pooled with audits 83 to 90, from audit 90's figures (search records 48 in 1026; with evidence 52 in 1090):
- Search records: 48 in 1026, 4.7% (unchanged).
- With this unit's evidence: 53 in 1094, 4.8%.
- With the Platanus lead added as a judged item: 54 in 1099, 4.9%.

Forks that would change the count:
- Line 4. If the desk treats the mM-for-µM slip as wording to fix (the trait value is categorical and the response is right), evidence is 0 of 4 and only the Platanus lead remains.
- Platanus. If the desk reads paclobutrazol and flurprimidol (gibberellin-synthesis inhibitors) as outside 10(d), despite the reading's "growth regulator" and the desk-d13 record on main, the lead is not a miss.
- On both lenient readings the unit is 0 errors and passes.

**Verdict: fail** (evidence 1 of 4, above 5%; one missed lead). Lines 1 to 3 stand.

**Error lines to drop or repair:**
- docs/views/evidence/desk-d20.jsonl: line 4 (repair "100 or 200 mM" to "100 or 200 μM (300 mL per pot)", or drop).

Follow-ups:
- Read Sperry and Chaney 1999 for Platanus occidentalis sense_chemical (and phototropic curvature under sense_light_nonvisual).
- Line 1: keep "no germination response at the 100% treatment" as the source words it. Line 2: "improved germination by 88% and 95%".
- Ficaria verna lead 12 still unchecked.
