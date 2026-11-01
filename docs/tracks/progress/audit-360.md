# audit-360: desk-d267, evidence lines 1 to 4

Audited 1 November 2026 from the desk-d267 files present untracked in the worktree (docs/tracks/progress/desk-d267.md and docs/views/evidence/desk-d267.jsonl, 4 lines; neither committed here, neither edited). Worktree HEAD and origin/main b9db4cff (desk-d266 closed). `python3 -I tools/senses/check.py | grep 'd267\.'`: "docs/views/evidence/desk-d267.jsonl: 4 records, 0 problems". Quote lengths (`len(q.split())`): 29, 22, 22, 15, all within 40. Non-ASCII in quotes: "±" and "°" (line 1), "–" U+2013 and "°" (lines 2, 3), "°" (line 4); all as printed (see each line). Format model audit 358; desk-audit.md evidence clause (40-word limit, no 125-character limit; a lead is not reinstated on length alone); abutting pieces judged under the six conditions of audit-324.md, cuts under audit-331.md.

Sources opened (WebFetch): pmc.ncbi.nlm.nih.gov/articles/PMC8207348 (two passes) and PMC4893327 (two passes), both returned by my WebSearches (PMC copies of the version of record, accepted as in audit 307 and oa-read.md step 3); oaj.fupress.net/index.php/ah/article/view/1777 (two passes) and its download/1777/1777 PDF (two passes); api.crossref.org/v1/works/ for 10.1002/ece3.7521, 10.7717/peerj.2085 and 10.13128/Acta_Herpetol-18117 (all answered; none robots_disallowed); amphibiansoftheworld.amnh.org Craugastor-loki; reptile-database.reptarium.cz Iberolacerta/galani, Podarcis/bocagei, Podarcis/siculus. University repository copies (usal.es, unileon.es, jcyl.es), zendy, Dryad and DOAJ mirrors in the results were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 6 WebSearches.

## Bibliographic and licence

- Line 1 (Percino-Daniel et al. 2021). Crossref: Ruth Percino-Daniel, José M. Contreras López, Oswaldo Téllez-Valdés, Fausto R. Méndez de la Cruz, Alejandro Gonzalez-Voyer, Daniel Piñero, in the recorded order; title identical; Ecology and Evolution 11(11): 6688-6702; issued 2021-05 (print 2021-06); CC BY 4.0 vor; relation empty, no update-to. PMC page prints "This is an open access article under the terms of the" ... "http://creativecommons.org/licenses/by/4.0/" "License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited." Accepted. Faults 0. (The PMC search-result title carries U+2010 in "direct‐developing"; the record's ASCII hyphen follows Crossref; uncounted.)
- Lines 2, 3 (Ortega, Mencía, Pérez-Mellado 2016, PeerJ). Crossref: authors in the recorded order; title identical; PeerJ 4, e2085, no issue; issued 2016-05-31; CC BY 4.0, content-version unspecified; relation has-review only. Page prints "This is an open access article distributed under the terms of the Creative Commons Attribution License" and "PeerJ. 2016 May 31;4:e2085. doi: 10.7717/peerj.2085". Accepted under the Crossref "unspecified" plus page-printed sentence pairing. Faults 0.
- Line 4 (Ortega, Mencía, Pérez-Mellado 2016, Acta Herpetologica). Crossref: authors in the recorded order; title identical; Acta Herpetologica 11(2): 127-133; issued 2016-12-25; no licence field (vor PDF links only); relation empty. Publisher page: byline "Zaida Ortega, Abraham Mencía, Valentín Pérez-Mellado", "Acta Herpetologica, 11(2), 127–133", "Published 2016-12-25", "DOI: https://doi.org/10.13128/Acta_Herpetol-18117"; licence "This work is licensed under a Creative Commons Attribution 4.0 International License." (as the note says) and, in the Copyright Notice, "Creative Commons Attribution 4.0 International Public License (CC-BY-4.0)". Publisher's own free full text with a CC BY sentence: accepted. Faults 0.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names

- Craugastor loki: Amphibian Species of the World "Craugastor loki (Shannon and Werler, 1955)", original name "Eleutherodactylus loki Shannon and Werler, 1955"; range includes "the Pacific versant of Chiapas"; no split of Chiapas populations stated. Family Craugastoridae and order Anura from the page's URL path (Amphibia/Anura/Brachycephaloidea/Craugastoridae/Craugastorinae/Craugastor), as the note says. Met.
- Iberolacerta galani "ARRIBAS, CARRANZA & ODIERNA, 2006"; "Lacertidae, Lacertinae, Sauria, Lacertoidea, Squamata (lizards)"; distribution "Spain (Montes de León, NW Iberia), elevation 1000-2000 m." Met.
- Podarcis bocagei "(LOPEZ-SEOANE, 1885)", same higher taxa; synonyms begin "Lacerta muralis var. bocagei LOPEZ-SEOANE 1885: 18". The page does not name León province (distribution "NW/WC Spain, N/W/EC Portugal"); the paper places the sampled population at Lago de La Baña. Met.
- Podarcis siculus "(RAFINESQUE-SCHMALTZ, 1810)", same higher taxa; "Lacerta sicula RAFINESQUE-SCHMALTZ 1810: 8" and the "Podarcis sicula" spellings are listed under it; Italy entry "(introduced to Menorca)"; the only subspecies tied to Menorca, cetti, is listed in synonymy of the nominate form. The paper names no subspecies and says the population "would be introduced from Sicily and/or Sardinia (Silva-Rocha et al., 2012)" (tool summary of the sentence). Met. Side note (uncounted): main's existing row for this species, docs/views/audit/corrected/herps.jsonl:74 (sense_light_nonvisual), files it as "Podarcis sicula", and gbif-names.tsv line 3932 holds "Podarcis sicula FUZZY ACCEPTED"; the two spellings will split one species in the views unless the owner normalises them.

Name faults 0.

## Duplicates

git grep on origin/main (b9db4cff) across the whole docs/ tree (evidence, audit, audit/corrected, audit/ALL, sheets, searched, gaps, progress) for Craugastor loki, loki, galani, Iberolacerta, bocagei, siculus, sicula, Menorca, Canutells, Percino, Ortega, ece3.7521, 7521, peerj.2085, 2085 and 18117/Acta_Herpetol. No record of any of the four species under sense_thermal and none of the three DOIs anywhere. Hits: Craugastor augusti and other congeners (oa-2 vision rows); Iberolacerta cyreni (sweep-67 lambda_max_nm, desk-d253 sense_chemical); Podarcis bocagei only in gaps/cells.jsonl (vision cells); Podarcis sicula only herps:74 (sense_light_nonvisual, parietal eye) and a sweep-7 search query; Menorca only desk-d222 / audit-309 (Podarcis lilfordi odour). Branch-only additions of all origin/research/desk-d2* and audit-3* branches: only research/desk-d222 (P. lilfordi, mentions P. siculus scent response in its Discussion summary) and research/desk-d230 (the progress note hold). audit-3*.md hold-outs: none names these species or DOIs (audit-309 mentions Menorca for P. lilfordi only).

Lines 2 and 3 are a retry, not a repeat. The d230 hold was the desk's own (desk-d230.md line 20: "the value sentences exceed 125 characters or are table rows ... held"); no audit held the lead (audit 323 audited the four filed d230 records only). Under desk-audit.md the lead is not reinstated on length alone; I reopened the source and checked it below. The cause of the hold is cured: there is no 125-character limit for evidence, and the sentence is 22 words, read whole by my independent pass. The two records draw on one sentence, each value in its own clause ("the preferred temperature range of I. galani was 27.9–29.7 °C" / "the preferred temperature range of P. bocagei was 30.1–34.5 °C"), so each carries only its own numbers.

Duplicates 0.

## Trait keys and conventions

sense_thermal for whole-animal gradient preference follows main (Phymaturus tenebrosus, Darevskia praticola, Podarcis muralis, Laudakia stellio, Stenocercus and Phyllodactylus rows, Cnemaspis mysoriensis). Main's conventions are mixed: text strings with units "C" or "categorical (...)" (Phymaturus: "mean preferred body temperature 35.36 +/- 0.38 C, set-point range 34.09-36.59 C"), bare numbers with the statistic in units (d263 rows now on main), and one list (Camponotus rufipes [26.9, 33.2], units "°C"). No interquartile or 50% range is filed as a list on main; the one set-point range is in a text string. Lines 2 to 4 file [lo, hi] lists with "C (preferred temperature range ...)" in units; check.py accepts this and I do not count it, but it joins the open owner question in audit 358 on one form for gradient rows.

Grade m right on all four (one named species measured). Trait-key faults 0.

## Per-record findings

### Line 1, Craugastor loki, pooled mean Tsel 21.83 C

Results 3.2, verbatim in two abutting pieces in one response: "When we pooled populations, the mean of Tsel is 21.83 ± 2.18°C, and the minimum and maximum means of" | "Tsel are 19.60 ± 1.70°C and 23.70 ± 1.30°C, respectively." Join as the desk's; no space before "°C", as quoted. Sentence before ends "(F 1,930 = 7.97, p = .0049, Table S3, Figure S6a)."; after: "The Tsel recorded in the lowlands and at intermediate elevations (bioclimatic domains: green, orange, and yellow)" "is within the range of the operative temperature (Te) and body temperature (Tb) recorded." Quote form MATCH, 29 words.

Verified, verbatim: "In total, we studied fifteen populations of Craugastor loki from the Sierra Madre de Chiapas"; "The frogs were kept for 3 days in plastic containers with the original substrate at laboratory temperature (~23°C)"; "Due to the short amount of time we kept frogs in the laboratory, not allowing them to acclimate"; "we recorded preferred temperature (Tpref) on day 1, critical thermal minimum (CTmin) on day 2"; Table 1 caption "Mean ± SE for the body temperature (Tb), operative temperature (Te), and preferred temperature range (Tsel)" and footnote "while n is the number of sampled frogs for each population for Tsel."; model "we used the gls function implemented in the nlme package" "to fit a linear model with heterogeneous variances" "organized hierarchically by individuals and then by population from low to high elevation." No sentence on sex or age class (tool summary).

The pooling. Verbatim: "The preferred temperature (Tsel) for each population varied with elevation (F 13,930 = 25.51, p < .0001;" "and differed between the bioclimatic domains (F 4,930 = 9.29, p < .0001". The value 21.83 C is a mean pooled across fifteen populations that the same Results show to differ significantly (population means 19.60 to 23.70 C), and the record's own quote opens "When we pooled populations". Under rules.md (pooled records = errors), as the launch prompt applies it to a pooled mean across significantly different groups, the logged value is a pooled record. The record discloses that Tsel "varied with elevation and bioclimatic domain" but gives no test statistic, and it does not change what was filed. Secondary faults: the units say the ± is unlabelled, while the Table 1 caption labels the population ± values as SE (the pooled ± is unlabelled in the sentence); the denominator df 930 is far above the roughly 200 frogs of Table 1 (my sum, tool summary), so readings rather than frogs appear to be the replicates, which the record does not say; Tsel was recorded on day 1 of the 3 days, before the CT trials.

**Line 1 error (pooled mean across populations that differ significantly in Tsel). HOLD OUT.** Not fixable by text replacement: the fix would be a different record (per-population Table 1 rows with their n, or a range of population means filed as such with the F tests), which needs fresh desk work on Table 1, whose rows this audit did not read verbatim.

### Lines 2 and 3, Iberolacerta galani [27.9, 29.7] and Podarcis bocagei [30.1, 34.5] C

Results, my independent pass, verbatim in two abutting pieces in one response: "Thus, the preferred temperature range of I. galani was 27.9–29.7 °C" | "and the preferred temperature range of P. bocagei was 30.1–34.5 °C." En dash U+2013 between the numbers and a space before "°C" (tool confirmed); the means sentence before prints "28.8±0.47°C" without spaces, which the quote does not use. My join point differs from the desk's, and the reassembled sentence is identical, so condition 3 of audit-324.md is met. **Quote MATCH**, 22 words. Sentence before: "The average preferred temperatures were lower for I. galani than for P. bocagei (I. galani: T ¯pref=28.8±0.47°C, n = 24;" "P. bocagei: T ¯pref=32.3±2.11°C, n = 24; Mann–Whitney U-test, U = 42.00, P < 0.0001)."; after: "Furthermore, the preferred temperature range of I. galani was significantly narrower than the preferred temperature range" "of P. bocagei (Levene’s test, W = 33.151, P < 0.0001)."

Verified, verbatim: "The 50% of central values of preferred body temperatures (that is, the interquartile range) was considered as the" "preferred temperature range to assess thermoregulation"; "We used 24 adult lizards (12 males, 12 females) from each species, with 6 hourly measures of Tpref"; "The thermal gradient was built in a glass terrarium (100 × 60 × 60 cm) with a 150 W infrared lamp over one of the sides,"; Tpref "recorded in the cloaca with a digital thermometer" "each hour in the period from 08.00 to 18.00 h (GMT)."; "Lizards were housed in individual terraria, fed daily with mealworms"; "The study area was in the Natural Monument "Lago de La Baña" (León province, Spain"; "located at 1,400 m asl"; "we captured lizards by noosing during their daily activity period"; "lizards were released completely unharmed at their capture sites"; "All means were reported with standard deviations (sd)."; "Thus, data of both genders were combined in subsequent analyses." Sex nulls (tool summary with figures): I. galani 28.9 ± 0.48 vs 28.8 ± 0.49, F1,22 = 0.118, P = 0.734; P. bocagei 32.9 ± 1.63 vs 31.8 ± 2.44, F1,22 = 1.746, P = 0.200. Years (tool summary): I. galani August 2011, P. bocagei August 2013. No acclimation period or fasting stated (tool summary). All as the records say.

The value says no more than the quote: the units call it the interquartile range of Tpref, which is the Methods' definition; the records do not claim it is per individual. Uncounted (my own construction): with SD 0.47 C for I. galani, a normal spread of individual values would give an interquartile width near 0.63 C, against the printed 1.8 C, so the range was probably computed from all readings rather than from individual means; the paper does not say. Uncounted additions: label the ± as SD; give the Levene statistic.

**Lines 2 and 3 MATCH.** The d230 hold reason is cured.

### Line 4, Podarcis siculus (Menorca) [28.40, 31.57] C

Abstract, verbatim in one piece: "The preferred temperature range of the species was similar for males and females: 28.40-31.57 °C." Hyphen-minus between the numbers and a space before "°" (tool's reading of the displayed text; raw encoding not inspected). Neighbours: "Body temperatures were not significantly related to substrate temperatures for any season." / "Introduced Italian wall lizards of Menorca are effective thermoregulators, with an effectiveness of 0.82 during summer." **Quote MATCH**, 15 words. The abstract opens "We studied the thermal ecology of an introduced population of the Italian wall lizard, Podarcis siculus," "in Menorca (Balearic Islands, Spain)." Population right.

Verified from the PDF, verbatim: "We used 24 P. siculus adult lizards, 14 males and 10 females."; "We captured lizards from the same location of field sampling"; "There, we housed lizards on individual terraria and fed them with mealworms and crickets."; "We built the thermal gradient in a glass terrarium (100 x 60 x 60 cm) with a 150 W infrared lamp over one of the sides."; "a gradient between 20 to 60 ºC."; "we measured the selected temperature of a lizard each hour from 08:00 to 17:00 h (GMT) with a digital thermometer."; "We considered the 50% of the central values of selected body temperatures as the preferred temperatures range (PTR)" "in all analyses, as it is the more common procedure, although we also report the 80%"; "Thus, we pooled them in subsequent analyses, and considered a preferred temperature range (PTR) for this population."; "The 50% PTR is 28.40 - 31.57 °C, and the 80% PTR is 26.85-32.54 °C."; "We reported mean values of variables accompanied by standard errors." Sex test (tool summary with figures): males 29.84 ± 0.41 (n = 14), females 30.15 ± 0.31 (n = 10), F1,22 = 0.301, P = 0.589. Trials 12 to 14 June 2013 (tool summary); no acclimation or capture-to-trial interval stated (tool summary). Sexes pooled after a null test, which is disclosed, so the pooling is not a pooled-record error.

Fault: the paper prints a conflicting value for the logged quantity. Discussion, verbatim: "The preferred temperature range of P. siculus, obtained in the late spring, ranges from 28.40 to 31.70 °C." The Abstract and Results give 31.57 C as the upper limit; the record does not mention the 31.70 C reading. The boring explanation is a typo in the Discussion, two of three printings agree, and the filed value can stand, but the conflict has to be disclosed. Uncounted: the ± figures in conditions are SE (Methods), unlabelled in the record; the trials fall in what the paper calls late spring.

**Line 4 error (conflicting Discussion value 28.40 to 31.70 C for the same range omitted).** Fixable.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Craugastor loki, pooled mean Tsel 21.83 C | error, HOLD OUT | whole record | quote MATCH (29); mean pooled over 15 populations that differ significantly (elevation F13,930 = 25.51, domain F4,930 = 9.29, both p < .0001) |
| 2 | Iberolacerta galani, IQR [27.9, 29.7] C | MATCH | none (optional uncounted additions) | quote MATCH (22), own clause; d230 hold cured |
| 3 | Podarcis bocagei, IQR [30.1, 34.5] C | MATCH | none (optional uncounted additions) | as line 2 |
| 4 | Podarcis siculus, 50% PTR [28.40, 31.57] C | error, fixable | conditions, note | quote MATCH (15); Discussion prints 28.40 to 31.70 C, not disclosed |

Errors 2 of 4 audited records (50%), above the 5% bar. By kind: pooled record 1 (line 1, held out); omitted conflicting value 1 (line 4); quote form 0; bibliographic 0; licence 0; names 0; duplicates 0 against main, all desk-d2* and audit-3* branches and the audit-3* hold-outs; grading 0. Lines 2 and 3 pass and may merge as filed (or with the uncounted additions below).

## Unchecked

- Craugastor loki Table 1 rows (per-population means, SE and n) were not read verbatim; the "roughly 200 frogs" is the tool's sum. Supplementary Tables S1 to S3 not opened.
- Whether the PeerJ and Acta Herpetologica ranges were computed from all readings or from per-lizard values (neither paper says; my inference only).
- The PeerJ year and month of each species' gradient trials, the sex test figures, and the absence of acclimation and fasting statements are tool summary.
- Acta Herpetologica: the hyphen-minus in the abstract range is the tool's reading of displayed text; trial dates, sex test figures and the origin sentence are tool summary.
- Reptile Database distribution for P. bocagei does not name León; the paper's locality was not checked against another range source.

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 1: HOLD OUT. The value is a mean pooled across fifteen populations whose Tsel differs significantly with elevation (F13,930 = 25.51, p < .0001) and bioclimatic domain (F4,930 = 9.29, p < .0001). Not to be merged; a refile would need per-population Table 1 rows (or a range of population means with the tests) read verbatim in a new desk unit.

Line 2 (uncounted, optional):
- `conditions`: "mean Tpref of I. galani 28.8 +/- 0.47 C (n = 24)" -> "mean Tpref of I. galani 28.8 +/- 0.47 C (SD; n = 24)"
- `conditions`: "the I. galani range was significantly narrower than that of P. bocagei (Levene's test)." -> "the I. galani range was significantly narrower than that of P. bocagei (Levene's test, W = 33.151, P < 0.0001). The paper does not say whether the interquartile range was taken over all hourly readings or over per-lizard values."

Line 3 (uncounted, optional):
- `conditions`: "mean Tpref of P. bocagei 32.3 +/- 2.11 C (n = 24)" -> "mean Tpref of P. bocagei 32.3 +/- 2.11 C (SD; n = 24)"
- `conditions`: "the P. bocagei range was significantly wider than that of I. galani (Levene's test)." -> "the P. bocagei range was significantly wider than that of I. galani (Levene's test, W = 33.151, P < 0.0001). The paper does not say whether the interquartile range was taken over all hourly readings or over per-lizard values."

Line 4, counted:
- `conditions`: "The Methods define the PTR as the central 50% of Tsel values" -> "The Discussion prints the same 50% range as 28.40 to 31.70 C ('obtained in the late spring'), against 28.40 to 31.57 C in the Abstract and Results; the record follows the two agreeing printings. The Methods define the PTR as the central 50% of Tsel values"
- `note`: "Abstract sentence read whole in one piece;" -> "Abstract sentence read whole in one piece (the Discussion's 31.70 C upper limit conflicts with it; audit 360);"

Line 4, uncounted:
- `conditions`: "the Results give mean Tsel of males 29.84 +/- 0.41 C (n = 14) and females 30.15 +/- 0.31 C (n = 10)" -> "the Results give mean Tsel of males 29.84 +/- 0.41 C (SE; n = 14) and females 30.15 +/- 0.31 C (SE; n = 10)"
- `conditions`: "Tsel was measured between 12 and 14 June 2013," -> "Tsel was measured between 12 and 14 June 2013 (late spring by the paper's own season definition),"

Verdict: 2 of 4 audited records in error (50%), above the 5% bar. Line 1 held out (pooled record); line 4 fixable with the text above; lines 2 and 3 pass, and the d230 hold on peerj.2085 is cured.
