# Audit 96: desk-d6 (8 plant genera; branch origin/research/desk-d6, head c086b20f)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: all 10 lines of docs/views/searched/desk-d6.jsonl (1 to 10). The progress note says 8; the file holds 10 (Apios has four records). This is a note fault and is not counted.
- Evidence records: all 8 lines of docs/views/evidence/desk-d6.jsonl (1 to 8).
- Wanted lines: all 4, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (10 lines) and the wanted file (4 lines) prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e) included), the counting rule of audit 39, the rulings of audits 84, 86, 87, 88 and 92, and the shared audit brief of 28 October. Audit 90 served as the format.

Queries. `harvest_get.py` ran without the network. A script compared each record's unprefixed `queries` with every `query` and `family review` line the harvest prints. Hamamelis (1), Nothoscordum (6), Clematis (7) and Richardia (10) match word for word and in order, with the "web: " lines after them. No harvest for these genera shows "gave up". Apios (2 to 5) and Sagittaria (8, 9) are in no harvest run and list "web: " lines only. No unlabelled line appears.

Chased. Lines 1, 6, 7 and 10 name a DOI their harvest output prints in a citation step (10.1086/336744, 10.1656/045.023.0309, 10.1093/oxfordjournals.aob.a087596, 10.1590/1519-6984.281402). Lines 2 to 5, 8 and 9 use the "none:" form with a reason, and name no unsupported DOI.

Open cells. The harvest header on today's main lists no open traits for any genus, because main's queue has been regenerated since the desk began (cb81e765). I re-ran `harvest.targets()` with the queue of the desk's base (a64a3f88) and main's searched files. It gives Hamamelis sense_chemical; Apios, Clematis, Richardia and Sagittaria all four plant traits; Nothoscordum diel, eye_type and sense_chemical; Carpinus sense_chemical; Cocculus sense_light_nonvisual. Every search record names an open trait. Hamamelis sense_chemical also has an older record on main (harvest-19:11) that the targets do not count as full protocol, so line 1 is a rescreen and not a repeat of a closed cell (audit 92's rule applies only to cells the header shows closed).

Main. I checked origin/main (cb81e765) docs/views/evidence and searched for every genus in the unit.
- No unit evidence line repeats a main source; a scan for all eight DOIs and URLs on main found none.
- Line 8 (Richardia scabra light) adds a species to a cell main already holds (R. brasiliensis, Moura et al. 2024, recheck-16-fixed:1 and sweep-98:1), from another source. Audit 95 accepted such lines.
- Line 1 (Nothoscordum bivalve diel) adds a trait to the ANPS natural-history line on main (sweep-27:11, sense_light_nonvisual).
- Lines 5 to 7 (Carpinus) add measurements where main's older null search records (harvest-16:16, sweep-17:2) say none. As audit 93 put it, that reflects on those records, and the lines contradict no evidence on main.
- No unit search record names a trait for which main holds evidence. Sagittaria's main evidence (sweep-39:1, 2) covers sense_light_nonvisual and sense_chemical, and the unit writes records only for diel and eye_type.
- Cocculus is skipped because its harvest shows three "gave up" queries (point 6), and Carpinus gets no search record. Both are right.

Synonymy. Every genus is an accepted name of its own genus. I opened POWO pages for these names, and each says "This species is accepted": Nothoscordum bivalve (170498-2), Clematis vitalba (319145-2), Clematis microphylla (709892-1), Carpinus caroliniana (295249-1), Carpinus betulus (295248-1), Richardia scabra (764679-1), Apios americana (30141320-2), Hamamelis virginiana (430697-1) and Sagittaria latifolia (225280-2). POWO lists Anemone vitalba as a synonym of Clematis vitalba, so Clematis stands. No record is filed under a synonym's genus.

Searches. I ran 45 WebSearches:
- 16 for the null records (Apios 6, Sagittaria 3, Hamamelis 4, one pooled focusing search for the five eye_type records, and two follow-ups);
- 6 for evidence sources;
- 9 for POWO status;
- 2 for wanted lines;
- the rest for leads and resolving pages.

I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. A ResearchGate result ("In Vitro Propagation of Apios americana") was left alone. No paper text is committed.

## Search record verdicts (10)

| Line | Record | Verdict |
|---|---|---|
| 1 | Hamamelis sense_chemical | **error: missed measurement.** My search "witch hazel Hamamelis induced defense herbivore damage tannin response leaves gall aphid Hormaphis" returned the AGRIS record (opened) for Rehill and Schultz 2012, "Hormaphis hamamelidis Fundatrices Benefit by Manipulating Phenolic Metabolism of Their Host", J Chem Ecol 38(5): 496-498, 10.1007/s10886-012-0115-9. On living Hamamelis virginiana, aphid-induced galls had higher condensed and lower hydrolyzable tannins than leaves, and galled and ungalled leaf laminas did not differ. That is a measured herbivore-induced response of a living plant, which the owner's reading counts, with a negative result at lamina level. The record's jasmonate search named "herbivore induced response" but returned no Hamamelis work, and it did not try a gall or aphid wording. My germination searches (GA3, stratification, light) found only the Joiner thesis and the RNGR protocol the record already screens, and my floral scent search found only patents and a horticultural fragrance page. Fork below. |
| 2 | Apios diel | ok. Web-only, and the "none:" chased is plausible. My search returned the Torrey 2018 floral biology of Apios priceana (bioone page served no text, so it is unread), PMC linkage-map and circadian-trapping papers on other plants, and wildflower pages. No hour of opening shown for an Apios species. Lead: the A. priceana paper. |
| 3 | Apios eye_type | ok. The pooled focusing search returned only the general set (FIU cas_bio/44, AskNature, Nature 075535b0, PMC9824129), with nothing on Apios. |
| 4 | Apios sense_chemical | ok. My GA3 and scarification search returned a Wyoming forb dormancy paper (Native Plants J 25(3): 148-161, opened, species not named in the abstract), the Holloway note and general GA pages. My elicitor search returned no Apios work. |
| 5 | Apios sense_light_nonvisual | ok. Three photoperiod and tuberization searches returned potato and Begonia papers (ISHS 1134_36 and 177_20, Springer BF02357599, all opened, none on Apios), and a Korean introduction trial of A. americana (Korean J Plant Resour 18(3): 424-432, 2005, koreascholar opened: field yield, planting date and staking, no light treatment). A Plant Production Science PDF (10.1080/1343943X.2019.1709512) failed at its site, and its subject is unknown. |
| 6 | Nothoscordum eye_type | ok. Queries match; the pooled search found nothing on Nothoscordum. |
| 7 | Clematis eye_type | ok. Queries match; the screened works are insect-eye, green-flower and leaf-micromorphology titles, rightly screened, and the pooled search found nothing on Clematis. |
| 8 | Sagittaria diel | ok. My three searches returned the record's own PMC3485334 and jipb abstract 24055, Wang and Chen 1999 on S. pygmaea pollination (Plant Diversity 21(2), abstract opened, no hour), and a Florida Entomologist paper (opened) giving 08:30 to 14:30 opening for Pontederia sagittata, which is not Sagittaria. No Sagittaria opening hour. |
| 9 | Sagittaria eye_type | ok. Web-only; the pooled search found nothing on Sagittaria. |
| 10 | Richardia eye_type | ok. Queries match; the pooled search found nothing on Richardia. |

Search record errors: **1 of 10 (10%)**, line 1.

## Evidence record verdicts (8)

| Line | Record | Verdict |
|---|---|---|
| 1 | Nothoscordum bivalve diel | ok. JPE PDF opened (pollinationecology.org 585): Weiherer, Eckardt and Bernhardt 2020, J Pollin Ecol 26(3): 16-31. The quote is verbatim in Results, Floral presentation, and refers to N. bivalve. Methods says "flowers remained closed in the morning". Flower opening hours fit the owner's plant diel reading. Grade m. |
| 2 | Clematis vitalba sense_light_nonvisual | ok. Massey record opened: Jarvis-Lowry, Harrington, Ghanizadeh and Robertson 2024, Plant Biol 26(3): 457-466, 10.1111/plb.13629. The quote is verbatim in the abstract. It is a light against dark germination test, so grade m. |
| 3 | Clematis vitalba sense_chemical | ok on the value; quote fault listed. The abstract (same page) says viable seeds "remained completely morpho-physiologically dormant throughout autumn, even when treated with nitrate", which supports the value. The record's quote is a Methods fragment naming the treatment. It is not a whole sentence and does not carry the result; the abstract sentence should replace it. Not counted, as the value is right. |
| 4 | Clematis microphylla sense_chemical | ok. CSIRO page opened: Aust J Bot 32(2): 121-129, 1984, 10.1071/BT9840121. "Addition of gibberellic acid or nitrate advanced germination only slightly." is verbatim. The page I saw showed no authors, so the authors were not checked. |
| 5 | Carpinus caroliniana sense_chemical | ok. USDA FS Carpinus.pdf opened (returned by my search): Pijut, Woody Plant Seed Manual. The quote is verbatim, on American hornbeam, citing Bretzloff and Pellet 1979, HortScience 14(5): 621-622. Grade m from a review entry naming the species, as main does elsewhere. |
| 6 | Carpinus betulus sense_chemical | ok. utupub record opened: Volf, Weinhold, Seifert, Holicová, Uthe, Alander, with van Dam in the metadata; 10.1007/s10886-020-01232-z. The quote is verbatim. The abstract says "winter moth caterpillars preferred leaves from control branches over leaves from treated branches within C. betulus" and that volatile production was localized to treated branches in all three species. MeJA applied to living trees counts under 10(d). Volume and pages were not shown, so not checked. |
| 7 | Carpinus betulus sense_light_nonvisual | ok. Frontiers text and PDF opened: Zhou, Zhao, Zhang and Zhu 2022, Front Plant Sci 13, 10.3389/fpls.2022.1055984. The quote is verbatim in the abstract. Table values match: 5.26 and 8.54 cm, 11.09 and 8.13 g, and 1.91 times. A set-light-intensity trial counts under 10(d). |
| 8 | Richardia scabra sense_light_nonvisual | ok. Cambridge abstract opened: Biswas, Bell, Crayton and Paul 1975, Weed Sci 23(5): 400-403, 10.1017/S0043174500062755. The quote, the "more than 2 hr of light" and the "up to 16 hr per day" findings are all in the abstract. Grade m, partial. |

Evidence errors: **0 of 8 (0%)**.

## Counts

- Search records: 1 of 10, 10%.
- Evidence: 0 of 8, 0%.
- Unit: 1 of 18, 5.6%.

Pooled with the desk's audits 83 to 90, from audit 90's figures (search records 48 in 1026; 52 in 1090 with evidence):
- Search records: 49 in 1036, 4.7%.
- With evidence included: 53 in 1108, 4.8%.

Including audits 91 to 95, from audit 95's pooled line (61 in 1088 and 68 in 1204):
- Search records: 62 in 1098, 5.6%.
- Overall: 69 in 1222, 5.6%.

Fork that would change the count. Line 1 (Hamamelis): if the desk reads gall tannin chemistry as tissue chemistry (10(a)) rather than a herbivore-induced response, line 1 stands. The unit then has 0 errors in 18, and the gall paper should still sit in `screened` with that reason.

**Verdict: fail on the search records** (1 of 10, 10%; one error line). The evidence passes at 0 of 8. Both whole files were judged, so drop the error line and the rest of the unit stands.

**Error lines to drop:**
- docs/views/searched/desk-d6.jsonl: line 1 (Hamamelis sense_chemical). Rehill and Schultz 2012 can close the cell, or can go on the wanted list.
- docs/views/evidence/desk-d6.jsonl: none. Line 3 should be requoted with the abstract sentence on nitrate.

## Wanted lines (listed, not counted)

- Line 1 (10.1080/17550874.2024.2329741, Richardia brasiliensis preanthesis cleistogamy): my exact-title search did not return the paper, so it is not checked.
- Line 2 (10.1016/j.sajb.2022.09.027): UIB repository opened. Tomàs, Cardona, Ferriol, Llorens and Gil 2022, S Afr J Bot 151: 85-94; year and DOI match. The authors field is empty, and the registry can fill it. The abstract gives seasons (winter and summer bloom) but no hour, so the line may hold no diel measurement.
- Line 3 (peeref 2025, South American Alliaceae volatiles): not searched.
- Line 4 (Biswas et al. 1975 part II): my search returned the Cambridge resolve URL, but the abstract page was refused (permission not answered), so it is not checked. Part I's page gives Weed Sci 23(5) with authors Biswas, Bell, Crayton and Paul.

## Leads

- Hamamelis virginiana sense_chemical: Rehill and Schultz 2012 (J Chem Ecol 38(5): 496-498).
- Apios priceana diel: "Floral Biology of the federally threatened Apios priceana (Fabaceae)", J Torrey Bot Soc 145(2), 10.3159/TORREY-D-17-00042.1 (bioone served no text).
- Plant Production Science 10.1080/1343943X.2019.1709512, returned by an Apios tuberization search; its subject is unknown.

## Blocked pages

- pmc.ncbi.nlm.nih.gov PMC4240452: reCAPTCHA.
- bioone.org Apios priceana and Florida Entomologist pages: metadata only (I used the journals.flvc.org PDF for the latter).
- tandfonline.com 10.1080/1343943X.2019.1709512 PDF: client error.
- cambridge.org part II abstract: permission not answered, not retried.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
