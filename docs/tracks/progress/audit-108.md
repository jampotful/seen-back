# Audit 108: desk-d16 (plant genera; branch origin/research/desk-d16, head 38ed0970)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: the single line of docs/views/searched/desk-d16.jsonl (line 1, Ranunculus diel).
- Evidence records: all 9 lines of docs/views/evidence/desk-d16.jsonl (1 to 9), every one abstract-level, grade m, "partial": true.
- Wanted lines: none (the unit has no wanted file).

## Gate

`python3 -I tools/views/screen_candidates.py --check` on a copy of the searched file (1 line) with an empty wanted file prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), the counting rule of audit 39, and the rulings of audits 84, 86 to 90 and 98, with audits 90 and 98 as the format. The launch prompt's readings are binding: sense_chemical counts living responses and volatile signalling only, hormone and elicitor responses on living plants included; ethylene on seed or plant counts as a hormone response; KNO3 priming needs a judgment (below). I ran 35 WebSearches: 9 for the null record (flower opening, anthesis, nyctinasty, scent timing, R. sceleratus, R. aquatilis/peltatus, R. glacialis/adoneus, R. asiaticus, and the screened van Doorn review), 17 for the nine evidence sources, 4 for names (POWO), and 1 for the Lunaria journal version. I fetched only URLs my own searches returned (or a link a fetched page printed). No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened: a webvpn.zafu.edu.cn proxy (twice), a springerlink.bibliotecabuap.elogim.com proxy and a bdp.academia.edu result were left alone. No paper text is committed.

Queries. `harvest_get.py Ranunculus` ran without the network (it reads origin/ci, harvest run 4 with supplement run 12). It prints, in order: "Ranunculus phytochrome photoreceptor", "Ranunculus light perception", "Ranunculus phototropism", the citation step on 10.3389/fpls.2020.597823, "Ranunculus photoperiod", "Ranunculus circadian rhythm", and family review "Ranunculaceae photoreceptor review" (125 hits). Line 1 lists these six word for word and in order, then five "web: " lines. No "gave up" and no unlabelled line.

Chased. Line 1 names 10.3389/fpls.2020.597823, the DOI of the citation step the harvest prints ("works citing 10.3389/fpls.2020.597823 that name Ranunculus: 5"). Under audits 90 and 98 a printed citation-step DOI is supported. The note's wording, that "the harvest's family-review search returned no Ranunculaceae review of flower timing", is accurate: the family review ran (125 hits) and its works are colour-vision, heliotropism and heterophylly reviews, none on flower opening hours. Accepted.

Screened. The record names all nine diel candidates `screen_candidates.py` lists, with correct reasons (moth pollination review, Arabidopsis halleri, honeybee, van Doorn and van Meeteren's general review, linalool review, Portulaca, soybean pulvinus, Culicoides, melatonin review). My title search for the van Doorn review returned no page showing a Ranunculus hour.

Main (origin/main d8281f66).
- Main evidence for the unit's genera: Ranunculus asiaticus sense_light_nonvisual (sweep-6:31); Datura wrightii diel (sweep-10:10); Lunaria annua sense_light_nonvisual (sweep-19:18, recheck-quotes-3-fixed:152); genus Juglans sense_light_nonvisual (oa-12:440, low red:far-red, another work); nothing for Castilleja. No unit evidence line repeats or contradicts evidence on main.
- Main holds older null search records that the unit's evidence now supersedes: Ranunculus sense_chemical (sweep-6:20), Datura sense_chemical and sense_light_nonvisual (sweep-10:38), Lunaria sense_chemical (rescreen-2:24, sweep-19:34), Juglans sense_chemical and sense_light_nonvisual (sweep-15:4), Castilleja sense_chemical (sweep-13:25). As in audits 90 and 98 these are noted and not counted; they should be marked superseded when the unit merges.
- No main diel evidence for Ranunculus, so line 1 contradicts nothing. It repeats sweep-6:20 (diel none), noted and not counted.

The seven harvest-c12 leads. All seven are on main's docs/views/wanted/harvest-c12.jsonl, and each evidence record names the lead's species:
- line 88 (10.1038/s41598-024-80159-x) = evidence 1, DOI matches, R. sceleratus in the abstract;
- line 89 (10.3390/plants12020370) = evidence 2, DOI matches, R. sceleratus;
- line 97 (10.1007/s10886-010-9878-z) = evidence 4, DOI matches, D. wrightii;
- line 98 (10.7554/eLife.00421) = evidence 5, DOI matches, D. wrightii;
- line 100 (Bhat et al. 2023, Environment and Ecology, DOI empty) = evidence 6, which gives the bioRxiv DOI 10.1101/2022.12.02.518881 of the preprint of the same title; L. annua named in title and quote;
- line 101 (Flores et al. 2017, FAVE 16(2), DOI empty) = evidence 7, no DOI, same title, authors and year; J. nigra;
- line 102 (10.3390/antiox14080974) = evidence 8, DOI matches, J. regia.

Skipped cells (the progress note's "not written" list). Each has leads on main:
- Ranunculus slnv and sense_chemical for repens, acris, abortivus: harvest-c12 wanted 92 (10.1007/BF00989298), 93 (10.2307/2260434), 94 (R. abortivus and R. bulbosus germination, 1976), plus 90 (10.1139/b81-189).
- Datura stramonium: harvest-c12 wanted 96 (10.1046/j.1365-3180.1998.00086.x).
- Ficus sense_chemical: harvest-c12 wanted 116 to 120 (Grison-Pigé 2001, Cao 2023, Cao 2026, Dubuisson 2024, Ferreira and Pasqual 2007), and desk-c12:4 (F. hahliana MeJA) on main.
- Lespedeza sense_light_nonvisual: desk-c12 wanted 1 to 3 and harvest-c12 wanted 121 to 129 (photoperiod, nyctinasty and germination titles).
The skip claims hold.

Genus status.
- Castilleja: POWO 325881-2 (opened) "This genus is accepted". NPSpecies 415616 (opened) lists Castilleja affinis Hook. & Arn. as accepted in Orobanchaceae. The POWO species page (49379-2) failed at its site; the Wikipedia list of Castilleja species (opened), which follows POWO as of 2024, lists "Castilleja affinis Hook. & Arn." So the record's genus, family (Orobanchaceae) and binomial stand.
- Ranunculus sceleratus: POWO 713776-1 failed at its site, so its status on POWO is unchecked here. The genus rule bears on it only if POWO moved the species to another genus; main already files R. sceleratus leads under Ranunculus.
- Datura, Lunaria and Juglans are accepted genera; I did not open their POWO pages.

## The KNO3 priming judgment (evidence line 6)

The bioRxiv full text (opened) primes Lunaria annua seed for 48 h in KNO3 (1% and 2% named) or CaCl2, against untreated seed (T1), then germinates them on wet filter paper at 24 +/- 2 C. The quote is verbatim: "Honesty (Lunaria annua L.) seeds primed with 1% KNO3 had maximum emergence rate (76.3 %)". Untreated seed reached 40% and took 14.6 days to 50% germination. The text frames nitrate as both nutrient and signalling molecule.

I count it under sense_chemical, for three reasons.
- What is measured is a germination and dormancy response of seed, which draws on its own reserves at that stage. This is not growth from nitrate taken up as a nutrient, which is what "nitrate-ion uptake does not count" excludes.
- Main files the same kind of result this way 16 times: KNO3 germination responses under sense_chemical, citing 10(e). Examples are oa-13b:422 (Rumex confertus), desk-d5:10 (Galium tricornutum), desk-d8:6, 7 and 11, desk-d9:6 (Potentilla norvegica), desk-d12:6 and desk-d18:7. Audit 90 named this same preprint as the missed Lunaria sense_chemical measurement.
- The 1% KNO3 prime beat the CaCl2 primes, which were soaked for the same 48 h. That comparison controls for hydration.

A weakness remains. The record's value sets KNO3 against untreated, unsoaked seed, so part of the gap may be a plain hydration (priming) effect. The text does not show whether a water-soaked control was run. A safer value would say "highest emergence of the KNO3 and CaCl2 primes". This is listed as a fork and not counted.

## Search record verdicts (1)

| Line | Record | Verdict |
|---|---|---|
| 1 | Ranunculus diel | ok. Queries match, chased is the printed citation step, and all nine candidates are screened with sound reasons. My nine searches returned flora, nursery and patent pages and the following: Rysiak and Żuraw 2012 on Eranthis hyemalis (DOAJ opened: flowers opened 8.00 am to 3.00 pm, another genus); Denisow and Antoń 2012 on Aquilegia (PDF opened, Ranunculus named only for pollen yield); Hou et al. 2022 on Gentianopsis (PMC8809448 opened, no Ranunculus); Fründ, Dormann and Tscharntke 2011 (Ecol Lett 14: 896-904, Freiburg PDF opened: Crepis, Leontodon, Taraxacum only); an Alpine Botany 2021 paper on R. glacialis (10.1007/s00035-021-00249-8, Springer opened: anthesis in days, stigma receptivity from day 3, no hour); and Hensel 1905, "On the Movements of Petals" (Univ Studies Nebraska 5(3), page opened: hours given only for dandelion and morning glory; the full PDF failed at its site, so a Ranunculus entry in its species list is unchecked, lead). The Tübingen "Ranunculus ficaria Blüte öffnet sich" film is Ficaria verna, a separate genus. No missed Ranunculus flower-opening or scent-timing measurement. |

Search record errors: **0 of 1**.

## Evidence record verdicts (9)

| Line | Record | Verdict |
|---|---|---|
| 1 | Ranunculus sceleratus GA (Park et al. 2024) | ok. DOAJ page opened: the seven authors, Sci Rep 14, 10.1038/s41598-024-80159-x. "the R. sceleratus seeds did not respond to the treatment with GAs; however, their germination percentage increased after undergoing warm stratification at 25℃" is in the abstract. A tested applied-hormone response with a null result counts under 10(d), as main's no-effect records do (desk-d6:3). Grade m. |
| 2 | R. sceleratus ethylene (Prokopoviča and Ievinsh 2023) | ok. MDPI page opened: Plants 12: 370, 10.3390/plants12020370. The abstract gives "1-MCP completely blocked it, but exogenous ethylene further promoted petiole elongation" and "Exogenous ethylene decreased (by 48%) but 1-MCP increased (by 48%) the Na+ accumulation". The plants were intact and growing. Ethylene on a living plant counts as a hormone response. |
| 3 | R. sceleratus light/dark germination (Smith 1986) | ok. ORO 56918 opened: Smith SJ, PhD thesis, Open University, 10.21954/ou.ro.0000de56. The sentence holds, and "this species" is R. sceleratus. A germination light/dark comparison belongs under sense_light_nonvisual. |
| 4 | Datura wrightii HIPV (Hare 2010) | ok. PMC3010200 opened: J Chem Ecol 36(12): 1363-1374, 10.1007/s10886-010-9878-z. The quoted sentence opens the abstract as given. The page confirms the abstract's spring peak and "no longer were inducible" by September. Herbivore- and MeJA-induced volatiles of living field plants count under 10(a) and 10(d). |
| 5 | D. wrightii GLV shift (Allmann et al. 2013) | ok. eLife page opened: the eight authors, eLife 2: e00421, 10.7554/eLife.00421. The quote is in the abstract. Feeding shifts (Z)-3 toward (E)-2 isomers, and moths laid more eggs on the (Z)-3-scented side. Herbivore-induced volatile emission of living plants counts under 10(a). |
| 6 | Lunaria annua KNO3 priming | ok, with the fork above. The quote and values (76.3%; 40% and 14.6 days for untreated seed) are in the bioRxiv PDF, which prints no authors. The authors, year and journal are taken from main's wanted line 100, as the record says, and I could not open the journal version (my search returned only the preprint). The access field says "open" while "partial": true is set (cosmetic). |
| 7 | Juglans nigra light (Flores et al. 2017) | ok. Journal PDF opened: Flores, Poggi, Garcia, Catraro and Gariglio, Rev FAVE Cienc Agrar 16(2), no DOI printed. The resumen sentence is verbatim. The treatments were 16 h light / 8 h dark against continuous darkness, so photoblastic neutrality is a measured light/dark response. Grade m. |
| 8 | Juglans regia MeJA (Nie et al. 2025) | ok. MDPI page opened: the nine authors, Antioxidants 14(8): 974, 10.3390/antiox14080974. Hydroponic living seedlings were given 50 uM MeJA with 50 mM NaCl. The abstract gives 16.83% less MDA and 11.60%, 10.73% and 22.25% higher SOD, POD and CAT. The fetch reports that Results section 3.4 assigns the 22.25% to APX, a discrepancy inside the paper that the record follows from the abstract (noted, not counted). |
| 9 | Castilleja affinis strigolactone analogue (Bashyal et al. 2025) | ok, requote (not counted). PMC12008575 opened: Bashyal, Müller, Chory and Bürger, STAR Protoc 6(2): 103753, 10.1016/j.xpro.2025.103753, species C. affinis. The page gives haustorium-like structures "within 3–7 days" after GR24 5DO and functional haustoria on Brachypodium after 18 days. A living seedling's response to an applied strigolactone analogue counts under 10(d). The quote is the summary's procedural sentence and states no result, and the values come from the protocol's expected outcomes (fork below). The genus and species are accepted (above). |

Evidence errors: **0 of 9**. Requote, not counted: line 9.

## Counts

- Search records: 0 of 1, 0%.
- Evidence: 0 of 9, 0%.
- Unit: 0 of 10, 0%.

Pooled with the desk's audits 83 to 90, from audit 90's figures (search records 48 in 1026; 52 in 1090 with evidence):
- Search records: 48 in 1027, 4.7%.
- With evidence included: 52 in 1100, 4.7%.

Forks that would change the count:
- Line 6 (Lunaria KNO3 priming). If the owner reads KNO3 priming against unsoaked seed as a hydration effect, not a nitrate cue, line 6 is an error. Evidence would then be 1 of 9 (11.1%) and the unit 1 of 10. The work would still not belong in `screened` under 10(e).
- Line 9 (Castilleja). If a protocol's expected-outcome statements are not read as a measurement, line 9 is an error, with the same effect on the count.
- Line 1 (Ranunculus diel). Hensel 1905 is unread in full. If its species list gives a Ranunculus opening hour from the author's own observation, line 1 is a missed measurement.

**Verdict: pass.** Both whole files were judged, and no line is an error. The unit stands as written.

**Error lines to drop:**
- docs/views/searched/desk-d16.jsonl: none.
- docs/views/evidence/desk-d16.jsonl: none.

## Leads

- Ranunculus diel: Hensel 1905, "On the Movements of Petals", University Studies (Nebraska) 5(3) (digitalcommons.unl.edu univstudiespapers/85). The full text failed at its site.
- Ranunculus glacialis: the Alpine Botany 2021 phenology paper (10.1007/s00035-021-00249-8) gives anthesis stages in days and no hour.
- Lunaria annua: the journal version of Bhat et al. 2023 (environmentandecology.com MS8.pdf on main's wanted line 100) is still unopened. It would confirm the authors and whether a hydropriming control was run.
- When the unit merges, mark main's older sense_chemical and sense_light_nonvisual null records for Ranunculus, Datura, Lunaria, Juglans and Castilleja as superseded (listed under Main).

## Blocked pages

- PMC10818387 table page: reCAPTCHA.
- POWO 49379-2 and 713776-1: failed at their site.
- digitalcommons.unl.edu viewcontent.cgi?article=1086: failed at its site.
- Left alone: onlinelibrary-wiley-com-443.webvpn.zafu.edu.cn (proxy), springerlink.bibliotecabuap.elogim.com (proxy), bdp.academia.edu.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
