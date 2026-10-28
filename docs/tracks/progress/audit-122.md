# Audit 122: desk-d32 (lead-reading unit, 5 evidence records; branch origin/research/desk-d32, head ece1124e)

## Lines judged

No sample was drawn. The unit is judged whole, so that error lines can simply be dropped.
- Evidence records: all 5 lines of docs/views/evidence/desk-d32.jsonl (1 to 5).
- Search records: none in the unit. Wanted lines: none.

## Gate

The unit has no searched or wanted file, so `screen_candidates.py --check` has nothing to run on. Quote lengths, measured by script: line 1 108, line 2 74, line 3 109, lines 4 and 5 62 characters. All are under 125, and each is one whole sentence.

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), the counting rule of audit 39, and the format of audits 90 and 121.
- I ran about 12 WebSearches and fetched only URLs those searches returned.
- Main. I checked origin/main (13bc5f74) docs/views/evidence/*.jsonl for each taxon and genus.
  - Main holds Poa pratensis sense_chemical only (desk-d1), not sense_light_nonvisual.
  - Main has no Pteridium, Platanus, Sarcopoterium or Stachys evidence.
  - No line repeats or contradicts main.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. A www-cambridge-org.ezproxyberklee.flo.org result was left alone. No paper text is committed.

## Evidence record verdicts (5)

| Line | Record | Verdict |
|---|---|---|
| 1 | Pteridium aquilinum sense_chemical | ok. I opened the pure.mpg.de PDF. It gives Radhika, Kost, Bonaventure, David and Boland 2012, PLoS ONE 7(11): e48050, 10.1371/journal.pone.0048050. The quote is verbatim and whole, in Results ("VOC emission from P. aquilinum after various treatments"). The facts match the record: doses 0.05 to 1 mM, "1 mM JA was required to significantly increase total VOC emission", 17 new compounds, (E)-beta-farnesene dominant, a blend "mainly comprised of terpenoids", and JA prepared from MeJA. The response is of the living plant: elicitors "were sprayed as aqueous solution on the fern fronds of intact plants" (greenhouse plants propagated from forest stock), and the cut plantlets appear only in the inhibitor tests. A hormone elicitor on a living plant counts under 10(d). WFO (wfo-0001107402, opened) accepts Pteridium aquilinum (L.) Kuhn. Two cosmetic points: the paper notes that 1-octen-3-ol and 3-octanone also came "to a small extent" from controls, so "absent from controls" is slightly strong; and S. littoralis induced a trace of limonene. |
| 2 | Poa pratensis sense_light_nonvisual | ok. I opened the Frontiers full-text page: Crump, Brown, Griffin-Nolan, Angeloni, Lemoine and Seymoure 2021, Front Ecol Evol 9: 732959, 10.3389/fevo.2021.732959. The quote is verbatim in the abstract. The record's 0.3 lux and 0.001 lux are as printed. The Methods' response variables (net photosynthetic rate, stomatal conductance, dark respiration and ΦPSII) match the value. Crickets were added after day 21, and the conditions field gives the height result. This is set night-light intensity on living grass, so the trait class is right. POWO 417792-1 (opened) accepts Poa pratensis L. |
| 3 | Platanus orientalis sense_light_nonvisual | **error: the value is not measured in the source.** The DOAJ record (opened) gives Lv, Hu, Zhou, Hu, Liang, Ai and Tian 2025, BMC Plant Biol 25, 10.1186/s12870-025-07179-1, and the quote is verbatim. But the sentence is in the Background, where the authors state an earlier observation that motivates the study. The study compares green leaves under streetlights with naturally yellowing leaves away from streetlights, using transcriptome and metabolome data: hormone genes, flavonoid and phenylpropanoid pathways, and JA and brassinolide levels. Per the abstract, the paper measures no senescence timing, leaf retention or chlorophyll. The record's method, "trees under streetlight ... compared with unlit trees", misdescribes this design. The delay is a prior finding restated and then inferred in the Conclusion, so grade m for a measured delayed senescence is not supported. A rewrite could carry the measured result (senescence-promoting hormone genes mostly suppressed in leaves under streetlights) with a Results sentence, or trace the earlier physiological study the Background cites. POWO 685873-1 (opened) accepts Platanus orientalis L. |
| 4 | Sarcopoterium spinosum sense_chemical | ok. I opened the bioone page: Çatav, Akbaş, Tavşanoğlu and Küçükakyüz 2024, Ann Bot Fenn 61(1), with DOI 10.5735/085.061.0106 in the URL. The quote is verbatim in the abstract, and the three species are as the note names them. "GA biosynthesis was required for germination induced by smoke water and KAR1" is in the abstract, which does not split it by species. S. spinosum alone is named as sensitive to mandelonitrile and as stimulated by ROS treatments, as the conditions field says. A karrikin response in living seed counts under 10(d). Abstract-only, so partial is right. GBIF 3001879 (opened) lists S. spinosum (L.) Spach as accepted, and POWO 741421-1 (opened) gives Sanguisorba spinosa as "a synonym of Sarcopoterium spinosum", so POWO accepts the name. |
| 5 | Stachys cretica sense_chemical | ok. It is the same source and sentence as line 4, and the record rightly leaves out the mandelonitrile and ROS results. POWO 459450-1 (opened) accepts Stachys cretica L. |

**Evidence errors: 1 of 5 (20%), line 3.**

## Counts

- Search records: none in this unit.
- Evidence: 1 of 5, 20%.
- Unit: 1 of 5, 20%.

Pooled with audits 83 to 90, from audit 90's figures as written (48 in 1026 search records; 52 in 1090 with evidence):
- Search records: 48 in 1026, 4.7% (unchanged).
- With evidence included: 53 in 1095, 4.8%.

Fork. The Background reading of line 3 rests on the fetch tool's sentence-by-sentence summary of the DOAJ abstract, because the BMC page was not opened. If the full text measures leaf retention or chlorophyll under the lights and the desk re-reads it from there, line 3 could be requoted from that passage and would stand.

**Verdict: fail (evidence 20%).** The unit was judged whole, so drop line 3 and lines 1, 2, 4 and 5 stand.

**Error lines to drop:**
- docs/views/evidence/desk-d32.jsonl: line 3 (Platanus orientalis sense_light_nonvisual).

## Pages opened

- pure.mpg.de BOL536.pdf; frontiersin.org fevo.2021.732959/full; doaj.org ad3746cde570471ea6daa39cc54bb933 (twice); bioone.org 085.061.0106 full page.
- POWO 459450-1, 417792-1, 685873-1 and 741421-1; WFO wfo-0001107402; GBIF 3001879.
- POWO 34020-1 failed at its site.
