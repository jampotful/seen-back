# Audit 94: desk-d4 (7 plant genera; branch origin/research/desk-d4, head c1dd31e2)

## Lines judged

No sample was drawn: the launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: all 14 lines of docs/views/searched/desk-d4.jsonl (1 to 14).
- Evidence records: all 6 lines of docs/views/evidence/desk-d4.jsonl (1 to 6).
- Wanted lines: all 5, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (14 lines) and the wanted file (5 lines) prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), the counting rule of audit 39, and the rulings of audits 84 and 86 to 90; audits 90 and 92 served as the format.

Queries. `harvest_get.py` (origin/ci, no network) prints "in no harvest run yet" for all seven genera: Hemerocallis, Chromolaena, Cyanthillium, Hexastylis, Hypoxis, Cichorium and Larrea. Every record lists "web: " lines only, and no unlabelled line appears. `harvest_get.py Asarum` shows Asarum in harvest run 2 with sense_chemical its only open trait.

Chased. I ran the five labelled family searches myself:
- "Asteraceae photoreceptor review" and "Xanthorrhoeaceae OR Asphodelaceae photoreceptor review" both returned link.springer.com 10.1007/s44372-025-00446-3 on the first page.
- "Aristolochiaceae photoreceptor review" returned both 10.1007/s44372-025-00446-3 and the doc.rero.ch 309979 PDF (10.1007/s00239-004-0294-2).
- "Hypoxidaceae photoreceptor review" and "Zygophyllaceae photoreceptor review" returned doc.rero.ch 309979.
Every chased DOI is therefore supported, as audits 86 and 87 accept for genera in no harvest run.

Main. I checked origin/main (ef4c0414) evidence and searched files for every genus:
- Hemerocallis: diel and sense_chemical on main (sweep-42:2 to 4); sense_light_nonvisual open. The unit's claim holds.
- Chromolaena: diel, sense_chemical and sense_light_nonvisual on main (sweep-42:11 to 13). Holds.
- Cichorium: diel on main (sweep-5:11, recheck-18-fixed:2). Holds.
- Larrea: diel on main (sweep-6:36). Holds.
- Hypoxis: **sense_light_nonvisual on main** (sweep-46:8, H. hemerocallidea, Shaik and Leanya 2014), the congener carry the genus rule uses. The unit still writes a null genus record for it (line 11).
- Asarum: sense_light_nonvisual on main (sweep-19:5 and recheck-6-fixed:8, A. heterotropoides).
- Main also holds older search records for all seven genera (sweep-5, -6, -42, -46, -47); the unit's records re-screen those cells, which is noted and not counted.
- No unit evidence line repeats main.

Names. POWO (opened) gives Hexastylis arifolia as "a synonym of Asarum arifolium" (ipni 121846-2) and Hexastylis ruthii as a synonym of Asarum arifolium var. ruthii (121856-2). GRIN (opened) accepts Hexastylis but says the evidence indicates it "should be sunk into Asarum". The unit's own note gives the POWO synonymy. Under the brief's ruling (audit 88: Mahonia aquifolium is Berberis aquifolium), records filed under Hexastylis are filed under a synonym's genus. Hemerocallis aurantiaca filed as H. fulva and Vernonia cinerea filed as Cyanthillium cinereum are correct accepted-name moves. The other six genera are accepted.

Searches. I ran 32 WebSearches:
- 5 family-review searches for chased;
- 3 for genus status;
- 13 on the null records (Cyanthillium diel and chemical 4, Hypoxis diel 2 and light/chemical 1, Hexastylis 3, 1 pooled focusing search for the seven eye_type records, plus 2 overlapping);
- 6 for evidence sources;
- 5 for wanted lines.
I fetched only URLs my own searches returned. A www-cambridge-org.ezproxyberklee.flo.org result and a springerlink.bibliotecabuap.elogim.com result were left alone; a proquest.com result was not opened. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed.

## Search record verdicts (14)

| Line | Record | Verdict |
|---|---|---|
| 1 | Hemerocallis eye_type | ok. Web-only, chased supported; my pooled focusing search returned only the general set (PMC8309337, FIU cas_bio/44, Nature 075535b0, PMC9257597), nothing on Hemerocallis. |
| 2 | Chromolaena eye_type | ok. Same; nothing on Chromolaena. |
| 3 | Cyanthillium eye_type | ok. Same; nothing on Cyanthillium or Vernonia cinerea. |
| 4 | Cyanthillium diel | ok. My searches ("Cyanthillium cinereum flower opening time anthesis morning capitula", "Vernonia cinerea floral biology anthesis time pollination") returned flora pages (Wikipedia, VicFlora, NParks, Lucid), a Capsicum anthesis paper and Brazilian Vernonieae work. No opening hour for C. cinereum. |
| 5 | Cyanthillium sense_chemical | ok. My germination and elicitor searches returned Shaukat et al. 2004 (AGRIS opened: light, temperature, moisture, salinity and pappus only; salinity is not a cue main logs, audit 88), a UKZN thesis on Centrapalus pauciflorus (opened, a different genus), the smoke paper on other species (Çatav et al. 2024), and MPMI elicitor papers not on Vernonia. No hormone, nitrate, smoke or volatile response for C. cinereum. The biblat volatile title is rightly screened as tissue chemistry. |
| 6 | Hexastylis eye_type | **error: filed under a synonym's genus.** POWO treats the species as Asarum arifolium; Asarum's eye_type is already covered by main (harvest-18:3, sweep-19:4). The pooled search found nothing either way. |
| 7 | Hexastylis sense_light_nonvisual | **error: filed under a synonym's genus, and contradicts main.** Under Asarum the trait is closed on main by A. heterotropoides (sweep-19:5), so a null genus record repeats a closed cell. My two searches found no Hexastylis germination or light trial (Kennesaw poster and general seed papers only). |
| 8 | Hexastylis diel | **error: filed under a synonym's genus.** Asarum diel already has a main search record (harvest-18:3, sweep-19:4). My scent and opening-time search returned scent-methods papers on other genera and nothing on Hexastylis. |
| 9 | Hypoxis eye_type | ok. Web-only, chased supported; the pooled search found nothing. |
| 10 | Hypoxis diel | **error: missed measurement.** My search "Hypoxis floral biology pollination flowers last one day open at" returned the SANBI PlantZAfrica account of Hypoxis hemerocallidea (pza.sanbi.org/node/10428, opened; Hölscher, National Herbarium, Pretoria, November 2009), which states "The flowers are short-lived and close at midday." That is flower closing time for a named species of the genus, the kind of observation main already accepts for Cichorium (Holdrege 2016). The same search returned Cohen 1939, "A Survey of the Genus Hypoxis Linn in the Transvaal" (Wits thesis, opened), which says the flowers "close at night" and open wide on sunny days, a genus-level lead. The record searched H. hirsuta and Ren et al. 2019 only. Fork below. |
| 11 | Hypoxis sense_light_nonvisual | **error: repeats a cell closed on main.** Main holds sweep-46:8 (H. hemerocallidea, seeds germinate in light and dark), and desk-screen point 4 says a trait with evidence on main gets no search record. The record's own note says "that genus-level carry stands". My search found no H. hirsuta light trial (Oliver thesis on CPUT and Arabidopsis DOF papers only). |
| 12 | Hypoxis sense_chemical | **error: contradicts the unit's own evidence.** Evidence line 2 of this unit logs H. hemerocallidea GA3 and KNO3 germination for the genus, which closes the cell once merged, yet this line records "found: none" for the genus. Under point 4 the trait gets no search record. Fork below. |
| 13 | Cichorium eye_type | ok. Chased supported; the pooled search found nothing. |
| 14 | Larrea eye_type | ok. Chased supported; the pooled search found nothing. Larrea light and chemical are rightly held on the wanted list. |

Search record errors: **6 of 14 (42.9%)**, lines 6, 7, 8, 10, 11 and 12.

## Evidence record verdicts (6)

| Line | Record | Verdict |
|---|---|---|
| 1 | Cyanthillium cinereum sense_light_nonvisual | ok. AGRIS page opened: Shaukat, Siddiqui, Ali, Sikander 2004, Int J Biol Biotechnol 1(3): 279-291. The quote is verbatim; light stimulated germination more than darkness, best constant temperature 30 C. Grade m, partial. |
| 2 | Hypoxis hemerocallidea sense_chemical | ok. Journal page opened: Shaik and Leanya 2014, AJTCAM 11(2): 330-333. The GA3 result and "23.3 and 26.7%" in 1% and 4% KNO3 "under light conditions only" are in the abstract. The quote stops before "in both light and dark conditions", so it is not a whole sentence (form only, value right). The page shows no DOI; the DOI matches main's sweep-46:8 for the same paper. |
| 3 | Cichorium intybus sense_light_nonvisual | ok. Rhodes repository PDF opened: title page November 1984 (the item page says 1985; the record follows the title page). Section 3.5.4 holds the quoted words; three cultivars, only Luxor differed, on day 4. Grade m. The quote is a fragment, as the record's note says. |
| 4 | Cichorium intybus sense_chemical | ok. EKB page opened: Ibrahim 2021, J Plant Prod 12(7): 747-755, 10.21608/jpp.2021.187442. The quoted words are verbatim; MeJ was superior to SA. The elicitor was fed through seedling roots, a living-plant response (10(d)). |
| 5 | Cichorium intybus sense_light_nonvisual | ok. ISHS page opened: Póvoa, Farinha, Generoso 2011, Acta Hortic 925: 213-219, 10.17660/ActaHortic.2011.925.31. Quote verbatim; 12 h photoperiod against darkness at 20 C, best 53.5%. |
| 6 | Hemerocallis fulva sense_light_nonvisual | ok. KoreaScience page opened: Lee 2001, J Korean Soc Environ Restor Technol 4(1): 52-56; 100,000, 22,000 and 7,700 lux. The quote stops mid-sentence (the abstract continues "to show a wide adaptation to various light intensities"), form only. Filing H. aurantiaca under H. fulva follows POWO. |

Evidence errors: **0 of 6 (0%)**.

## Counts

- Search records: 6 of 14, 42.9%.
- Evidence: 0 of 6, 0%.
- Unit: 6 of 20, 30.0%.

Pooled with the desk's audits 83 to 90, from audit 90's figures (search records 48 in 1026; 52 in 1090 with evidence):
- Search records: 54 in 1040, 5.2%.
- With evidence included: 58 in 1110, 5.2%.
(Audit 92 already moved the pool to 51 in 1038 and 56 in 1113; adding this unit to that gives 57 in 1052, 5.4%, and 63 in 1133, 5.6%.)

Forks that would change the count:
- Lines 6 to 8 (Hexastylis). If the owner keeps Hexastylis as a queue genus despite POWO, lines 6 and 8 stand, and line 7 no longer meets Asarum's main evidence. Search errors would then be 3 of 14 (21.4%).
- Line 10 (Hypoxis diel). If the desk wants a dated paper rather than the SANBI species account, the line stands and Cohen 1939 is a lead.
- Line 12 (Hypoxis sense_chemical). If unit evidence that is not yet on main does not engage point 4, the line stands.
- Even with every fork read in the unit's favour, line 11 remains and the search records fail at 1 of 14 (7.1%).

**Verdict: fail.** The search records fail at 42.9% (6 error lines); the evidence passes at 0 of 6. The whole files were judged, so drop the error lines and the rest stands.

**Error lines to drop:**
- docs/views/searched/desk-d4.jsonl: lines 6, 7, 8, 10, 11 and 12.
  - Lines 6 to 8: refile under Asarum, or drop; Asarum's open trait on main is sense_chemical only.
  - Line 10: reopen Hypoxis diel; the SANBI account (close at midday, H. hemerocallidea) and Cohen 1939 can close it.
  - Lines 11 and 12: drop; the cells are closed by sweep-46:8 and this unit's evidence line 2.
- docs/views/evidence/desk-d4.jsonl: none.

## Wanted lines (listed, not counted)

- Line 1 (Tipton 1985): authors, title, J Amer Soc Hort Sci 110: 615-618 match the USDA Woody Plant Seed Manual Larrea chapter (fs.usda.gov, opened), which says "Conditions conducive to germination include darkness". DOI empty; none seen.
- Line 2 (Barbour 1968): author, year, title, Ecology 49: 915-923 match the NYBG record (opened).
- Line 3 (Jardine et al. 2010): authors, year, ACP 10: 12191-12206 and DOI match the Copernicus PDF (opened). The PDF says the branches were enclosed on living field plants, with no applied stimulus, so it is an emission inventory; it stays doubtful under 10(a).
- Line 4 (Geng et al.): title, authors and DOI match the CNKI page (opened); species are H. lilio-asphodelus, H. fulva 'Golden Doll' and H. minor at 20, 40, 70 and 100% light. No year or journal shown, so the empty fields are right.
- Line 5 (Davis, Frett, Kitto 2014): authors, Native Plants J 15(3): 247-254 and DOI match the npj page (opened); H. arifolia var. arifolia is among the species, with IBA at 0 to 10 μM and survival equal across treatments. Fault: filed under Hexastylis arifolia, which POWO lists as Asarum arifolium.

## Leads

- Hypoxis hemerocallidea diel: SANBI PlantZAfrica (Hölscher 2009), "close at midday".
- Hypoxis diel (genus): Cohen 1939, Wits thesis, "The flowers close at night".
- Larrea tridentata sense_light_nonvisual: the USDA seed manual's darkness statement points to Tipton 1985 and Barbour 1968 (wanted lines 1 and 2).

## Blocked pages

- None of my fetches was refused. The besnet copy of Ren et al. 2019 was read to 100,000 characters only (abstract gives season, no hour).
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
