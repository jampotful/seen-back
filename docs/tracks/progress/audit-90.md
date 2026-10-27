# Audit 90: desk-c12 (16 plant genera; branch origin/research/desk-c12, head 47867368)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: all 21 lines of docs/views/searched/desk-c12.jsonl (1 to 21).
- Evidence records: all 8 lines of docs/views/evidence/desk-c12.jsonl (1 to 8).
- Wanted lines: all 7, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on a copy of the searched file (21 lines), with the wanted file (7 lines), prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e) included), the counting rule of audit 39, and the rulings of audits 84, 86 and 87. Audits 88 and 89 (origin/research/audit-88 and -89) served as the format.

Queries. `harvest_get.py` ran without the network (it reads origin/ci). A script compared each record's unprefixed `queries` with every `query` and `family review` line the harvest prints for the genus. All 15 records for harvested genera (lines 1 to 15: Rumex, Lunaria, Ficaria, Urtica, Daucus, Ficus, Lespedeza, Cenchrus, Cerastium, Carex) match word for word and in order, with the "web: " lines after them. No harvest shows "gave up", and no unlabelled line appears. Salix, Olea and Coccoloba (lines 16 to 21) are in no harvest run and list "web: " lines only.

Chased.
- Lines 1 to 15 name exactly the citation-step DOIs their harvest output prints.
- Lines 16 to 21 name 10.1007/s00239-004-0294-2. The doc.rero.ch PDF (opened) is Lariguet and Dunand 2005, "Plant Photoreceptors: Phylogenetic Overview", J Mol Evol 61: 559-569, with that DOI.
  - My "Salicaceae photoreceptor review" and "Polygonaceae photoreceptor review" searches both returned doc.rero.ch 309979 on the first page. Salix (16, 17) and Coccoloba (19 to 21) are therefore supported, as in audits 86 and 87.
  - I ran "Oleaceae photoreceptor review", Olea's only family search, twice (standard and extended). Neither run returned it. Only a longer query of my own, with "plant photoreceptors phylogenetic overview" added, did. Line 18 is therefore unsupported (fork below).

Main. I checked origin/main (5abfdeb5) docs/views/evidence/*.jsonl for every genus in the unit.
- Rumex holds sense_light_nonvisual (oa-13b:420, 421, 426, 470 and more) and sense_chemical (oa-13b:422, 439, 442), and no diel. The unit's claim holds.
- Botrypus holds sense_light_nonvisual (sweep-31:3), its only open trait, and the unit writes no Botrypus record. That claim holds too.
- No unit search record names a trait that main holds evidence for. No unit evidence record duplicates main: main has Cardamine, Carex, Ficus, Lunaria and Urtica light only, Salix chemical only, and Olea light and chemical only.
- Line 2 (Lunaria sense_chemical) repeats a desk-screen search record already on main, rescreen-2:24. Both missed the same measurement, so the repeat is noted, not counted separately.

Screened. Every screened DOI is printed by the harvest output. The OpenAlex ids are in the harvest's query id lists or works (harvest_get.load()). One reason is wrong: line 10 screens the two buffelgrass papers 10.2135/cropsci2002.1075 and 10.2135/cropsci2000.402391x as "Title does not name Cenchrus", but buffelgrass is Cenchrus ciliaris. The 2002 abstract (Burson, Hussey, Actkinson, Shafer, Crop Sci 42(4): 1075-1080; AGRIS opened) gives pollination only in days before anthesis, with no hour. My search did not return the 2000 paper. Neither is shown to hold a measurement, so neither is counted.

Searches. I ran about 60 WebSearches:
- 12 for evidence sources and taxonomy;
- 5 for family reviews;
- 2 or more of my own for every null record (genus and common name, plus germination, hormone, herbivore or anthesis searches under 10(e));
- 1 pooled focusing search for the seven eye_type records;
- 7 for wanted lines.

I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. An ezproxyberklee.flo.org result and a springerlink.bibliotecabuap.elogim.com result were left alone. No paper text is committed.

## Search record verdicts (21)

| Line | Record | Verdict |
|---|---|---|
| 1 | Rumex diel | ok. Queries match (11 harvest, 5 web), and chased is the printed citation steps. My three searches returned Piotrowska 2008 on R. acetosella pollen production (DOAJ opened: seasonal only), Denisow and Antoń 2012 (Aquilegia only), and flora pages. No Rumex hour. |
| 2 | Lunaria sense_chemical | **error: missed measurement.** My search "Lunaria annua seed germination gibberellin OR GA3 OR dormancy OR stratification" returned first the bioRxiv preprint "Effect of Potassium Nitrate and Calcium Chloride priming on germination and seedling growth of Honesty (Lunaria annua L.)" (biorxiv.org 10.1101/2022.12.02.518881, full PDF opened). It reports that seeds primed with 1% KNO3 had the highest emergence (76.3%), germinated earlier than all other treatments, and gave the best seedling vigour. Nitrate on living seed is a 10(e) cue, and audit 88 counted KNO3 the same way. The page shows no authors or year. |
| 3 | Ficaria sense_chemical | ok, with a lead. Queries match. My searches (Ficaria verna and Ranunculus ficaria) returned flora pages, Park et al. 2024 on three other Ranunculus species (DOAJ opened, no Ficaria), and Egensperger and Rauschert 2020, "Understanding bulbil germination requirements in lesser celandine, Ranunculus ficaria" (Ohio J Sci 120, conference abstract; CSU profile opened, no abstract shown). That last title is a lead, not a shown measurement. |
| 4 | Urtica sense_chemical | **error: missed measurement.** My search "Urtica dioica stinging trichome density induced herbivory jasmonate" returned the AGRIS record (opened) for Pullin and Gilbert 1989, "The stinging nettle, Urtica dioica, increases trichome density after herbivore and mechanical damage", Oikos 54(3): 275-280. The title states a herbivore-induced response of a living plant, which the owner's reading counts, so under 10(e) the snippet closes the cell as a lead. The same session's germination search also returned Szewczuk 2001, "Effect of variable temperature and solution of gibberellic acid on the germination of stinging nettle seeds (Urtica dioica L.)", Ann UMCS sect EEE IX Suppl: 333-337 (repozytorium.up.lublin.pl opened, no abstract). Under 10(e) that title belongs on the wanted list, never outside it. |
| 5 | Daucus diel | ok, with a lead. Queries match. My searches returned extension and flora pages and the J Poll Ecol paper the record names. A title search for the screened 1912 note "The Diurnal Nodding of the Wild Carrot and Other Plants" (W2311088261) returned only weed pages. It is screened by title as umbel movement. It may still give opening times, so it stays a lead. |
| 6 | Daucus sense_chemical | **error: missed measurement.** My search "Daucus carota seed germination gibberellic acid GA3 priming" returned Hossain, Hossain, Ferdousi and Haque 2015, "Effect of foliar application of GA3 and plant ages on yield and quality of carrot seed", J Sylhet Agric Univ 2(2): 171-178 (jsau.sau.ac.bd PDF opened). GA3 at 200 ppm sprayed on living carrot plants gave the best seed quality and yield, and the text gives germination rising from 47.31% in the control to 93.0%. That is an applied-hormone response of a living plant (10(d)). The same search returned other carrot GA3 and hormone-priming titles: PMC12764683 (permission unanswered), a biblat record on umbel position and gibberellic acid in carrot germination (access check), and an IJH priming paper. |
| 7 | Ficus eye_type | ok. Queries match. The screened works are light-capture and unrelated papers, rightly screened under the owner's wording. My pooled focusing search returned only the general set (PMC8309337, FIU cas_bio/44, Nature 075535b0, PMC9824129). |
| 8 | Lespedeza sense_chemical | ok. Queries match. My searches returned the ASHS L. tomentosa scarification abstract, Keeley and Fotheringham 1998 on Emmenanthe and Phacelia (frames.gov and USGS opened, no Lespedeza), the smoke paper on three non-unit species (below), and induced-resistance papers on cotton. No Lespedeza chemical response. |
| 9 | Lespedeza eye_type | ok. Queries match, and the pooled search found no Lespedeza focusing work. |
| 10 | Cenchrus diel | **error: missed measurement.** My search "Cenchrus americanus pearl millet anthesis time of day flowering hours stigma emergence" returned Kulshreshtha and Ravindra Nath, "The Biology of Flowering in Pennisetum americanum (L.) Leeke", J Indian Bot Soc 66: 64-67 (indianbotsoc.org PDF opened). It reports that florets "started opening from 5.00 P.M., and by 7.00 P.M. all the florets were opened", and that anther dehiscence ran from 11.00 P.M. to 6.45 A.M. POWO (235186-2, opened) gives Pennisetum glaucum as "a synonym of Cenchrus americanus". The Florida Plant Atlas (opened) accepts Cenchrus americanus (L.) Morrone with Pennisetum americanum L. as its basionym. So this is flower-opening timing in a named species of Cenchrus. The record searched buffelgrass and fountain grass only. |
| 11 | Cenchrus eye_type | ok. Queries match, and the pooled search found nothing on Cenchrus. |
| 12 | Cerastium diel | ok. Queries match. My two searches returned sunflower circadian work, flora pages for C. fontanum and C. arvense, and garden pages. No hour. |
| 13 | Cerastium sense_chemical | ok. Queries match. My searches returned three celery papers (MDPI Plants 13: 2096, Springer BF00025395 and BF00385203, all opened, no Cerastium) and weed fact sheets. No Cerastium hormone, nitrate, smoke or volatile response. |
| 14 | Cerastium eye_type | ok. Queries match, and the pooled search found nothing. |
| 15 | Carex eye_type | ok. Queries match. The lens-cell candidates are leaf anatomy and structural colour works, rightly screened, and the pooled search found nothing on Carex. |
| 16 | Salix diel | ok. Web-only, and chased is supported. My searches returned Füssel et al. 2007, J Chem Ecol 33: 749-765 (Springer opened). It covers floral scent across 34 Salix species, sex and population variation, with no time of day. The other results were the general circadian-scent review (PMC4829607) and anthesis papers on other crops. |
| 17 | Salix eye_type | ok. Web-only, chased supported, and the pooled search found nothing. |
| 18 | Olea eye_type | **error: unsupported chased.** Web-only. Its only family search, "web: Oleaceae photoreceptor review", did not return doc.rero.ch 309979 when I ran it, standard or extended. No harvest supports 10.1007/s00239-004-0294-2 for Olea either. The record says the PDF "came back from the labelled family searches", but only my wider query of my own surfaced it. Fork below. Nothing on Olea focusing came back. |
| 19 | Coccoloba sense_light_nonvisual | ok. Web-only, and chased is supported. My searches returned the USDA tropical tree manual for C. uvifera (rngr PDF opened: one sowing in 50% shade, no light comparison), a C. gigantifolia fruit-maturity paper (SciELO opened, no light treatment), and a Dioon shade paper. |
| 20 | Coccoloba sense_chemical | ok. Web-only, and chased is supported. My searches returned salt-stress work on C. uvifera seedlings: Bullaín-Galardis et al. 2023, Terra Latinoamericana 41 (AGRIS opened), and a Tropentag poster. Salinity is not a cue main logs under sense_chemical (audit 88). No hormone, nitrate, smoke or volatile trial. |
| 21 | Coccoloba diel | **error: missed measurement.** My search "Coccoloba uvifera floral biology anthesis time of day flower opening pollination" returned first Madriz and Ramírez 1996, "Biología reproductiva de Coccoloba uvifera (Polygonaceae) una especie polígamo-dioica", Rev Biol Trop 44(3A): 105-115 (UCR page opened; abstract holds no hour). The open PDF on tropicalstudies.org, returned by the same search, gives "una máxima apertura floral y producción de néctar desde las 08:00 hasta las 12:00 horas". That is flower opening timing in a named species. |

Search record errors: **6 of 21 (28.6%)**, lines 2, 4, 6, 10, 18 and 21.

## Evidence record verdicts (8)

Every line is abstract-level and partial. In each case I opened a page my own search returned.

| Line | Record | Verdict |
|---|---|---|
| 1 | Cardamine hirsuta sense_chemical | ok. Frontiers text page opened: Bakhtiari, Glauser and Rasmann 2018, Front Plant Sci 9, 10.3389/fpls.2018.01230. The quote is verbatim, and the abstract gives "a strong positive effect of root induction on the resistance against AG herbivory". Applied JA on living roots counts under 10(d). Grade m. |
| 2 | Alliaria petiolata sense_chemical | ok. Springer page opened: Yasin and Andreasen 2015, Plant Growth Regul 77: 307-315. The quote is verbatim, as is "SA inhibited germination". The record's journal field omits volume 77 and says "issue 3" (cosmetic). |
| 3 | Ficus racemosa diel | ok. Pherobase page opened: Borges, Bessière and Ranganathan 2013, J Chem Ecol 39(5): 630-642, 10.1007/s10886-013-0280-5, on F. racemosa. The quote is verbatim. Day and night scent profiles of syconia count as scent timing under the owner's reading of plant diel. |
| 4 | Ficus hahliana sense_chemical | ok. Cambridge page opened: Mrazova and Sam 2019, J Trop Ecol 35(4): 157-164, 10.1017/S0266467419000117. The quote and the 52.3% and 20.8% per day are verbatim. A living tree's response to applied MeJA counts under 10(d). The caterpillars were dummies, which changes nothing. |
| 5 | Salix nipponica sense_light_nonvisual | ok. KoreaScience page opened: Lee, Son, Kim and Oh 2002, J Wetlands Res 4(2): 1-11. "Seed germination was little affected by light." is verbatim. Grade m, a germination light response. |
| 6 | Carex flava diel | ok. Natuurtijdschriften page and PDF opened: Vonk 1979, Acta Bot Neerl 28(1): 1-20. The quote is verbatim. The PDF gives "In the morning before about 5 a.m. (solar time) the anthers protrude" and thecae opening at 7 to 9 a.m. for all five taxa of the complex, so grade g is right. |
| 7 | Carex inops sense_chemical | ok. NPJ page opened: Broadlick and Bakker 2019, Native Plants J 20(3): 253-265, 10.3368/npj.20.3.253. The quote is verbatim. A tested smoke cue with a small response counts. |
| 8 | Olea europaea diel | ok. SciELO and UFC pages opened: Zambon, Silva, Pio, Bianchini and de Oliveira 2018, Rev Ciênc Agron 49(2). The quote is verbatim. The SciELO keywords name Olea europaea L. and the cultivar 'Arbequina', so the binomial is supported. |

Genus status. Every taxon is a name of its own genus, so the synonym-of-another-genus rule does not apply to any of them.

Evidence errors: **0 of 8 (0%)**.

## Counts

- Search records: 6 of 21, 28.6%.
- Evidence: 0 of 8, 0%.
- Unit: 6 of 29, 20.7%.

Pooled with the desk's other audits of desk-screen units. I start from audit 87's figures as written: search records 39 in 965, and 41 in 990 with the evidence samples. Audit 88 adds 2 in 29 and 3 in 37. Audit 89 adds 1 in 11 and 2 in 34. Audit 89's own pooled line, "42 in 1024", should read 43 in 1024, since 41 + 2 = 43. Before this audit the pool stood at 42 in 1005 search records and 46 in 1061 overall. With audit 90:
- Search records: 48 in 1026, 4.7%.
- With evidence included: 52 in 1090, 4.8%.

Forks that would change the count:
- Line 18 (Olea chased). If the desk accepts the record's word that its labelled Oleaceae search returned the rero PDF, line 18 stands. Search records would then be 5 of 21 (23.8%), and the verdict is unchanged.
- Line 4 (Urtica). If the desk reads mechanical and herbivore damage as no chemical cue, the Szewczuk 2001 GA3 title still had to go on the wanted list under 10(e). I count the line once either way.
- Line 2 (Lunaria). The measurement is a bioRxiv preprint whose page shows no authors. If the desk wants a peer-reviewed source, the line still had to hold the trait out under point 3.

**Verdict: fail.** The search records fail at 28.6% (six error lines). The evidence passes at 0 of 8. Both whole files were judged, so drop the error lines and the rest of the unit stands.

**Error lines to drop:**
- docs/views/searched/desk-c12.jsonl: lines 2, 4, 6, 10, 18 and 21.
  - Lines 2, 4, 6, 10 and 21 reopen Lunaria sense_chemical, Urtica sense_chemical, Daucus sense_chemical, Cenchrus diel and Coccoloba diel. The works named above can close them.
  - Line 18 (Olea eye_type) can be rewritten with a chased reason, or with a supported family-review DOI.
- docs/views/evidence/desk-c12.jsonl: none.

## Wanted lines (listed, not counted)

- Lines 1 to 3 (Lespedeza photoperiod papers, 10.1104/pp.27.3.644, 10.2134/agronj1955.00021962004700120004x, 10.2135/cropsci1968.0011183x000800030014x): my title searches did not return their pages, so none is checked.
- Line 4 (Martínez Sánchez et al. 2013): the authors and year match the redalyc PDF (opened), which gives Rev Mex Cienc Agríc Pub. Esp. Núm. 6: 1263-1272. The INIFAP page (opened) gives DOI 10.29312/remexca.v0i6.1289, and the line's DOI field is empty.
- Line 5 (Planta Daninha, southern sandbur): the title and the KNO3 1 to 3% result match the SciELO abstract (opened), which shows no authors, year or DOI either. The DOAJ record from my search failed at its site. The abstract states a nitrate dormancy-breaking result for C. echinatus, which could close Cenchrus sense_chemical as a lead.
- Line 6 (Cerastium regelii, 10.1111/j.1756-1051.1990.tb01761.x): not returned by my search, so not checked.
- Line 7 (10.1515/popore-2017-0001): the DOI and year match the PAN PDF (opened): Kellmann-Sopyła, Koc, Górecki, Domaciuk and Giełwanowska 2017, Pol Polar Res 38(1): 83-104. The authors field is empty. The PDF states greenhouse temperature (18 to 22 C) and no light regime, so it probably holds no light trial.

## Leads

- Lunaria annua sense_chemical: the KNO3 priming preprint (10.1101/2022.12.02.518881).
- Urtica dioica sense_chemical: Pullin and Gilbert 1989 (Oikos 54: 275-280) and Szewczuk 2001 (GA3 germination).
- Daucus carota sense_chemical: Hossain et al. 2015 (foliar GA3).
- Cenchrus americanus diel: Kulshreshtha and Ravindra Nath (J Indian Bot Soc 66: 64-67).
- Coccoloba uvifera diel: Madriz and Ramírez 1996 (Rev Biol Trop 44(3A): 105-115).
- Ficaria verna: Egensperger and Rauschert 2020, on bulbil germination requirements.
- Daucus diel: the 1912 diurnal-nodding note (W2311088261).
- Cenchrus ciliaris diel: "Stigma Receptivity and Seed Set in Protogynous Buffelgrass" (10.2135/cropsci2000.402391x), still unread.
- The smoke and karrikinolide paper the unit saw blocked (Çatav et al. 2024, Ann Bot Fenn 61(1): 31-40, 10.5735/085.061.0106; bioone issue page opened) covers Onopordum caricum, Sarcopoterium spinosum and Stachys cretica, none of them in this unit.

## Blocked pages

- pmc.ncbi.nlm.nih.gov PMC12764683: permission unanswered, not retried.
- biblat.unam.mx (carrot gibberellic acid record): access check.
- journals.pan.pl: bot check, so I used czasopisma.pan.pl.
- POWO 77244975-1: failed at its site.
- doaj.org 520e7f2384a24297b1c43475a3f1414c: failed at its site.
- ri.conicet.gov.ar 11336/29981: empty page.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
