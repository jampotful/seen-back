# Audit 98: desk-d9 (12 plant genera; branch origin/research/desk-d9, head 42cf7f74)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: all 19 lines of docs/views/searched/desk-d9.jsonl (1 to 19).
- Evidence records: all 15 lines of docs/views/evidence/desk-d9.jsonl (1 to 15).
- Wanted lines: all 5, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (19 lines) and the wanted file (5 lines) prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), the counting rule of audit 39, and the rulings of audits 84 and 86 to 90, with audits 90 and 97 as the format. I ran 50 WebSearches: 20 for the null records (germination, hormone, volatile and anthesis phrasings, one pooled focusing search), 4 for the labelled family searches behind `chased`, 13 for evidence sources, 9 for names (POWO), and 4 for wanted lines. I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened (a brum.beds.ac.uk proxy mirror in one result list was left alone), and no paper text is committed.

Queries. `harvest_get.py` ran without the network (it reads origin/ci). A script compared each record's unprefixed `queries` with every `query` and `family review` line the harvest prints for the genus.
- Populus (lines 8, 9) match word for word and in order.
- Nyssa (lines 4 to 7) list the four queries but leave out the harvest's family review "Nyssaceae photoreceptor review" (6 hits), which ran without error. They put a combined "web: Scrophulariaceae OR Nyssaceae photoreceptor review" in its place. Line 6 even screens 10.1093/jpe/rtv012, a work that only that family review prints, so the step was seen and then left out of `queries`. Point 7 makes this an error.
- Lolium (line 10) lists all ten queries but gives the family review as "web: Poaceae photoreceptor review" and not as the harvest line. Counted (fork below).
- Calystegia (line 11) leaves out "Convolvulaceae photoreceptor review" (77 hits) and uses "web: Fabaceae OR Convolvulaceae photoreceptor review".
- Melinis, Agave, Tipularia and Sideroxylon are in no harvest run and list "web: " lines only. No harvest shows "gave up", and no unlabelled line appears.

Chased.
- Populus (10.1111/ele.12205), Lolium (10.1016/j.tree.2009.09.010) and Calystegia (10.3906/bot-1310-57) name a citation step their harvest prints.
- Melinis names 10.1007/s44372-025-00446-3. My "Poaceae photoreceptor review" search returned it (link.springer.com), so it is supported.
- Agave and Tipularia (Asparagaceae OR Orchidaceae), and Sideroxylon (Sapotaceae OR Ulmaceae), name 10.1007/s00239-004-0294-2. Both labelled searches returned the doc.rero.ch 309979 PDF, so both are supported.
- Nyssa names 10.1007/s44372-025-00446-3, which its harvest output does not print. Its labelled web search did return it, and Nyssa has no citation step, so I do not count it separately (the lines are errors on queries anyway).

Main (origin/main a0136e11).
- **Sideroxylon obtusifolium sense_light_nonvisual is already on main**: recheck-15-fixed:4 and sweep-96:5 log the same Silva et al. 2014 paper (quixaba, photoblastic neutral). Evidence line 13 repeats it.
- **Ulmus minor sense_chemical is already closed on main** by sweep-13:5 (Wegener et al. 2001: oviposition-induced elm volatiles, the jasmonic acid blend and the parasitoid bioassay). Evidence lines 11 (Meiners and Hilker 2000, the same system and the same lab) and 12 (Büchel et al. 2012) add sources to a closed cell.
- **Agave sense_chemical has congener evidence on main**: sweep-40:13 (Polianthes tuberosa, now Agave amica, floral scent). The queue gives Agave americana sense_chemical closest "genus" (sweep-40#13). Search line 13 is therefore a null record against main evidence (audit 93 counted the Hypoxis case the same way). It is also a missed measurement (below).
- The unit repeats older search records on main for Melinis (sweep-42:12), Nyssa (sweep-97:33, 34), Agave (sweep-40:2), Calystegia (harvest-18, sweep-17:12), Tipularia (sweep-22:37, sweep-23:34) and Sideroxylon (sweep-96:30). As in audits 90 and 97, these repeats are noted and not counted.
- Taylorson 1969 sits on main's wanted list (harvest-c10) and Cicek and Tilki 2007 on harvest-c11. Lines 5, 6, 9 and 10 now log them, which is fine.

The no-record claim for Potentilla, Amphicarpaea, Verbascum and Ulmus. **It holds, but not for the reason the note gives.** The harvest headers list Potentilla open for sense_chemical only, Amphicarpaea for sense_light_nonvisual only, and Verbascum for sense_light_nonvisual only. Each of those is now covered by the unit's evidence (lines 6, 7, 1 and 3). Their other traits already have search records on main (Potentilla: harvest-12:43 and sweep-4:8; Amphicarpaea: harvest-29:25 to 27 and sweep-30:23; Verbascum: harvest-7:1, 2 and harvest-15:6). Ulmus is in no harvest run, and main holds sweep-13:12 for all four traits plus harvest-c11:1, 2. So no new record was needed. The note's reason ("cells touched by congener evidence or wanted lines; a null record would contradict them") is right only for the light and chemical cells.

Genus status (POWO, opened).
- **Calystegia sepium is a synonym of Convolvulus sepium** (POWO 30033025-2: "This name is a synonym of Convolvulus sepium"; 30074933-2 Convolvulus sepium L. accepted). Search line 11 is filed under a synonym's genus, as in audits 86 and 88.
- **Argania spinosa is a synonym of Sideroxylon spinosum** (POWO 785772-1). Argan studies therefore count for Sideroxylon, which bears on line 19.
- Accepted: Potentilla norvegica (728598-1), Lolium temulentum (407516-1) and Ulmus laevis (856879-1). Verbascum lasianthum (769943-1) was checked as a sample of the genus. The POWO page for V. bithynicum (810823-1) failed at its site, and V. wiedemannianum was not reached. Any synonymy of those two lies inside Verbascum, so the synonym-of-another-genus rule does not touch them.
- Ulmus campestris (Büchel's clone 'Dahlem') is treated as U. minor by the PMC paper itself.
- Melinis, Nyssa, Populus, Agave, Tipularia and Amphicarpaea are accepted genera, and no record is filed under a synonym of them. I did not open their POWO pages separately.

## Search record verdicts (19)

| Line | Record | Verdict |
|---|---|---|
| 1 | Melinis diel | ok. Web-only, and chased is supported. My search (Melinis repens or Rhynchelytrum repens, anthesis hours) returned flora pages (FNA, ausgrass, Magnetic Island) and nothing with an hour. |
| 2 | Melinis eye_type | ok. My pooled focusing search returned only the general set (FIU cas_bio/44, AskNature, PMC9824129, Nature 075535b0). |
| 3 | Melinis sense_chemical | **error: missed measurement.** The note says the record covers "a Melinis species", but it searched M. repens only. My search returned Khan et al. 1997, "Intercropping increases parasitism of pests", Nature 388: 631-632 (nature.com/articles/41681 opened). Its abstract says "Volatile agents produced by M. minutiflora repelled female stem-borers and attracted foraging female C. sesamiae". It also says one volatile "released by intact M. minutiflora" is a herbivore-induced compound. Living-plant volatile signalling counts under 10(a). The same search returned the follow-up "Enhancing foraging behaviour of stemborer parasitoids: role of a non-host plant Melinis minutiflora" (J Insect Behav 18: 149-169, 2005). |
| 4 | Nyssa diel | **error: queries differ** (the harvest family review is left out). My anthesis search found no Nyssa hour (USDA/ICRAF fact sheet and Trees and Shrubs Online only). |
| 5 | Nyssa eye_type | **error: queries differ.** The pooled focusing search found nothing on Nyssa. |
| 6 | Nyssa sense_chemical | **error: queries differ.** My germination and hormone search found the ASHS 2014 abstract the record names and nothing on GA3 or nitrate. |
| 7 | Nyssa sense_light_nonvisual | **error: queries differ.** My search also returned a 2007 Acta Botanica Yunnanica record (journal.kib.ac.cn Y2007/V29/I03/351). Its redirect did not resolve, so whether it covers a Nyssa light or GA3 trial is unchecked (lead). |
| 8 | Populus diel | ok. Queries and chased match. My search returned Puc and Wolski 2002 (AAEM 9: 65-69, PDF opened): poplar "releases most of its pollen grains in the morning", stated in the Introduction from another source, with no Populus hour measured (daily totals only). Martin et al. 2010 is on ragweed. No flower-opening hour. |
| 9 | Populus eye_type | ok. Queries and chased match, and the pooled search found nothing. |
| 10 | Lolium eye_type | **error: queries differ** (fork). The harvest's "Poaceae photoreceptor review" (464 hits) is given only as a "web: " line. Chased is printed, the screened ligule, conical-cell and silica works are rightly screened, and the pooled search found nothing. |
| 11 | Calystegia sense_chemical | **error: filed under a synonym's genus** (POWO: Convolvulus sepium). The queries also differ (Convolvulaceae family review left out). My search returned a herbivore-cue germination paper (PMC12647282) and an induced-twining paper on Convolvulaceae climbers, neither opened. |
| 12 | Agave eye_type | ok. Web-only, chased supported, and the pooled search found nothing. |
| 13 | Agave sense_chemical | **error: missed measurement, and congener evidence on main.** My search returned Villavicencio-Gutiérrez, Torres-Tapia, Méndez González, Curiel-López and Sánchez Pérez 2024, "Germinación de semillas en Agave potatorum Zucc.", Rev Mex Cienc For 15(86) (INIFAP PDF opened). GA3 at 500 ppm gave about 75% germination against 53% in the control, and 1,000 ppm about 61%. That is an applied-hormone response of living seed (10(d)). The same search listed other Agave germination works (Biol Res 47: 11, PMC4103986), not opened. Main also holds sweep-40:13 (Polianthes tuberosa = Agave amica, sense_chemical). |
| 14 | Tipularia diel | ok. My search returned Whigham and McWethy 1980, Am J Bot 67(4): 550-555 (Smithsonian repository PDF opened). It reports nocturnal visitors and timing in days after anthesis, with no opening hour or scent timing. |
| 15 | Tipularia eye_type | ok. The pooled search found nothing. |
| 16 | Tipularia sense_chemical | ok. My germination search returned the ODU poster the record names, plus Habenaria and Pterospora papers (Springer and biostor opened) that are not Tipularia. |
| 17 | Sideroxylon diel | **error: missed measurement.** My search returned Kiill, Martins and Silva 2014, "Biologia reprodutiva de Sideroxylon obtusifolium (Roem. & Schult.) T.D. Penn. (Sapotaceae) na região semiárida da Bahia", Rev Árvore 38(6): 1015-1025 (Embrapa Alice PDF opened). It says "Quanto à antese floral, esta foi registrada nas primeiras horas da manhã" and records the stigma changing colour "por volta das 7 h". That is flower-opening timing in a named species. |
| 18 | Sideroxylon eye_type | ok. Web-only, chased supported, and the pooled search found nothing. |
| 19 | Sideroxylon sense_chemical | **error: missed measurement.** POWO treats Argania spinosa as Sideroxylon spinosum. My search returned Alouani and Bani-Aameur 2004, "Argan (Argania spinosa (L.) Skeels) seed germination under nursery conditions: Effect of cold storage, gibberellic acid and mother-tree genotype", Ann For Sci 61(2) (afs-journal.org abstract opened). GA application alone about doubled germination, to about 60% against 35.5%. That is an applied-hormone response (10(d)). The record searched S. lanuginosum and S. celastrinum only. |

Search record errors: **10 of 19 (52.6%)**: lines 3, 4, 5, 6, 7, 10, 11, 13, 17 and 19.

## Evidence record verdicts (15)

Every line is abstract-level and carries "partial": true, as it should. For each line I opened a page my own search returned.

| Line | Record | Verdict |
|---|---|---|
| 1 | Verbascum bithynicum light | ok. AVESİS page opened: Senel, Ozdener and Incedere 2007, Pak J Biol Sci 10(7): 1118-1121, 10.3923/pjbs.2007.1118.1121. Both Verbascum germinated better in darkness than under 16:8 h or continuous light. The quote is one sentence (the fetch would not reproduce it verbatim, so its wording is not confirmed). Grade m. |
| 2 | V. bithynicum GA3 | ok. Same page: GA3 at 20, 100 and 200 mg/L completely prevented germination. Grade m, 10(d). |
| 3 | V. wiedemannianum light | ok, as line 1. |
| 4 | V. wiedemannianum GA3 | ok, as line 2. |
| 5 | Potentilla norvegica light | ok. Cambridge page opened: Taylorson 1969, Weed Sci 17(2): 144-148, 10.1017/S0043174500031192. Nearly full promotion after about 5 min of red light, and 50% after 1 s, under phytochrome control. Grade m. |
| 6 | P. norvegica KNO3 | ok, requote (not counted). The value holds (0.2% KNO3 with the temperature shift gave a synergistic rise). The quote stops at "KNO3", the start of a longer sentence, as the unit itself flags. |
| 7 | Amphicarpaea edgeworthii light | ok, requote (not counted). PMC5223113 opened: Zhang et al. 2017, Sci Rep 7: 39886, 0 to 90% shading. The quoted sentence is not verbatim: the abstract reads "Aerial and subterranean seed yield, seed mass and number for both ASP and SSP were highest in full light." The value holds. |
| 8 | Lolium perenne gibberellin | ok, requote (not counted). cykx.lzu.edu.cn opened: Shan et al. 2019, Pratacultural Sci 36(9): 2304-2311. The quote is the first clause. The sentence goes on "however, soaking in 200 mg·L–1 and 300 mg·L–1 gibberellin could significantly alleviate ... under 15% PEG stress", which matches the value. |
| 9 | Ulmus minor light | ok, requote (not counted). IBU repository opened: Çiçek and Tilki 2007, J Environ Biol 28(2): 423-425. The abstract gives light at 25 C and 30/20 C as best for U. minor (above 95%), so the value holds. The quote is the aims sentence and states no result. |
| 10 | Ulmus laevis light | ok. Same page: germination of U. laevis was not affected by temperature or light, and was fastest at 30/20 C in darkness. |
| 11 | Ulmus minor sense_chemical (Meiners and Hilker 2000) | **error: cell already closed on main** (sweep-13:5, Wegener et al. 2001, the same elm, beetle and parasitoid system). The content itself checks: PestInfo page opened, J Chem Ecol 26(1): 221-232, U. minor named, the quote verbatim, jasmonic acid mediation and a systemic response. |
| 12 | Ulmus minor sense_chemical (Büchel et al. 2012) | **error: cell already closed on main** (sweep-13:5). Content checks: PMC3439254 opened; the quote is verbatim; the plant is U. minor (clone given as U. campestris 'Dahlem'); "MeJA treated plants showed transcript abundance patterns similar to EF treated plants" is in Results, not the abstract, so `where` slightly overstates. |
| 13 | Sideroxylon obtusifolium light | **error: repeats evidence on main.** recheck-15-fixed:4 and sweep-96:5 log the same Silva et al. 2014 paper (10.25066/agrotec.v35i1.10254) with the same finding. The quote is also a first clause. |
| 14 | Tipularia discolor light | ok. Frontiers PDF opened: McCormick, Good, Mozdzer and Whigham 2022, Front Ecol Evol 10: 1047267. The quote is verbatim (the abstract's last line). The text gives shaded T. discolor lower Asat and "higher quantum efficiencies (α) than control and drought-treated plants". The value comes from the article body, so `access: "abstract"` understates it (cosmetic). Grade m. |
| 15 | Lolium temulentum sense_chemical | ok, requote (not counted). PMC6540478 opened: Dombrowski et al. 2019, BMC Plant Biol 19: 222. The quote is verbatim but is the abstract's background sentence and states no measured response. The value (a strong initial burst of differentially expressed sequences within the first hour of GLV exposure) holds. |

Evidence errors: **3 of 15 (20.0%)**: lines 11, 12 and 13. Requotes, not counted: lines 6, 7, 8, 9, 13 and 15.

## Counts

- Search records: 10 of 19, 52.6%.
- Evidence: 3 of 15, 20.0%.
- Unit: 13 of 34, 38.2%.

Pooled with the desk's audits 83 to 90, from audit 90's figures (search records 48 in 1026; 52 in 1090 with evidence):
- Search records: 58 in 1045, 5.6%.
- With evidence included: 65 in 1124, 5.8%.

Pooled with the running pool as audit 97 gives it (search records 62 in 1091, 69 in 1214 overall, through audit 95 plus 97; audit 96 not included):
- Search records: 72 in 1110, 6.5%.
- With evidence included: 82 in 1248, 6.6%.

Forks that would change the count:
- Line 10 (Lolium). If the desk accepts the family review written as a "web: " line in the same words, line 10 stands. Search records would then be 9 of 19 (47.4%).
- Lines 4 to 7 (Nyssa). If omitting the harvest family review is read as a form fault, these four stand. Search records would be 6 of 19 (31.6%), and the verdict is unchanged.
- Lines 11 and 12 (Ulmus minor chemical). If extra sources for a closed cell are allowed, only line 13 counts, and evidence would be 1 of 15 (6.7%).

**Verdict: fail.** The search records fail at 52.6% and the evidence at 20%. Both whole files were judged, so drop the error lines and the rest of the unit stands.

**Error lines to drop:**
- docs/views/searched/desk-d9.jsonl: lines 3, 4, 5, 6, 7, 10, 11, 13, 17 and 19.
  - Lines 3, 13, 17 and 19 reopen Melinis sense_chemical, Agave sense_chemical, Sideroxylon diel and Sideroxylon sense_chemical. The works named above can close them.
  - Lines 4 to 7 and 10 can be rewritten with the harvest family review line copied in.
  - Line 11 belongs under Convolvulus, if anywhere.
- docs/views/evidence/desk-d9.jsonl: lines 11, 12 and 13.

## Wanted lines (listed, not counted)

- Line 1 (Semenza, Young and Evans 1978): my search did not return its page, so it is not checked.
- Line 2 (Catara et al. 2016): iris.unict.it opened. The authors and year match, the DOI is 10.1017/S0960258515000343, and the citation is Seed Sci Res 26(1): 30-46.
- Line 3 (Zhang et al. 2015): the UKy page (opened) gives the same five authors, Am J Bot 102(6): 860-869, 10.3732/AJB.1500069. The abstract has no light or GA3 test, as the line says.
- Line 4 (10.20900/cbgg20250003): my title search did not return it, so it is not checked.
- Line 5 (Ann Bot 1962): not searched.

## Leads

- Melinis minutiflora sense_chemical: Khan et al. 1997, Nature 388: 631-632; J Insect Behav 18: 149-169 (2005).
- Agave potatorum sense_chemical: Villavicencio-Gutiérrez et al. 2024, Rev Mex Cienc For 15(86) (GA3).
- Sideroxylon obtusifolium diel: Kiill, Martins and Silva 2014, Rev Árvore 38(6): 1015-1025.
- Sideroxylon spinosum (argan) sense_chemical: Alouani and Bani-Aameur 2004, Ann For Sci 61(2), 10.1051/forest:2004011.
- Nyssa: the 2007 Acta Botanica Yunnanica record (journal.kib.ac.cn Y2007/V29/I03/351), unread.
- Convolvulus sepium: the queue and gap tables still carry Calystegia sepium; the name change should reach the taxonomy before the cells are re-searched.

## Blocked pages

- journal.kib.ac.cn Y2007/V29/I03/351: redirect to a truncated URL, not followed.
- POWO 810823-1: failed at its site.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
