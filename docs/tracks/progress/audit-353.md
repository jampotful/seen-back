# audit-353: desk-d257, evidence lines 1 to 6

Audited 31 October 2026 from the desk-d257 files present untracked in the worktree (docs/tracks/progress/desk-d257.md and docs/views/evidence/desk-d257.jsonl, 6 lines; neither committed here, neither edited). Worktree HEAD and origin/main 6c4d6091 (desk-d255 after audit 351). `python3 -I tools/senses/check.py | grep 'd257\.'`: "docs/views/evidence/desk-d257.jsonl: 6 records, 0 problems". Quote lengths (`len(q.split())`): 39, 39, 34, 36, 40, 33, all within 40 (line 5 exactly at the limit); non-ASCII only "χ" (twice each in lines 1 and 2) and "–" (line 4), both checked against the page. Format model audits 350 and 351; desk-audit.md evidence clause (40-word limit, no 125-character limit); abutting pieces judged under the six conditions of audit-324.md, cuts under audit-331.md (no quote in this unit has a cut).

Sources opened (WebFetch): api.crossref.org/v1/works/ for all four DOIs (10.1371/journal.pone.0225507, 10.3390/insects11030177, 10.1371/journal.pone.0258272, 10.3390/insects15040297; one pass each, all answered, none robots_disallowed, so the desk's "Crossref refused" notes are superseded); journals.plos.org pone.0225507 (three passes); mdpi.com/2075-4450/11/3/177 (three passes); journals.plos.org pone.0258272 (one pass); mdpi.com/2075-4450/15/4/297 (three passes); api.obis.org/v3/taxon/<name> for Chionoecetes opilio (answered), Ectatomma brunneum, Neoponera inversa and Asproparthenis punctiventris (total 0, terrestrial). The query form api.obis.org/v3/taxon?scientificname=Chionoecetes opilio named in the launch prompt was refused by the tool as a repeat of a failed client_error fetch; the path form answered, as in audits 331 and 351; no other workaround. Names also from antcat.org/catalog/442939, antwiki.org Ectatomma_brunneum and Neoponera_inversa, and gd.eppo.int/taxon/CLEOPU (all from WebSearch results). No curl, mirror, PMC, repository copy, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 3 WebSearches and 21 WebFetch calls used.

## Bibliographic and licence

- Lines 1 and 2 (Pereira et al., pone.0225507). Crossref: Márlon César Pereira, Ingrid de Carvalho Guimarães, Daniel Acosta-Avalos, William Fernando Antonialli Junior; title identical; PLOS ONE 14(11) e0225507; issued 2019-11-25; CC BY 4.0 vor; relation empty; no update-to. Page: "This is an open access article distributed under the terms of the Creative Commons Attribution License,". Accepted. Faults 0.
- Line 3 (Ren et al., insects11030177). Crossref: Xiaoyun Ren, Shengyong Wu, Zhenlong Xing, Ruirui Xu, Wanzhi Cai, Zhongren Lei; title identical; Insects 11(3) 177; issued 2020-03-11; CC BY 4.0 vor; no update-to. Page metadata CC BY 3.0, no licence sentence in the body. Accepted (CC BY 3.0 page vs CC BY 4.0 Crossref). Faults 0.
- Line 4 (Cerbule et al., pone.0258272). Crossref: Kristine Cerbule, Bent Herrmann, Eduardo Grimaldo, Leif Grimsmo, Jørgen Vollstad; title identical (returned in two pieces, joined at "snow crab" | "(Chionoecetes opilio) pot fishery"); PLOS ONE 16(10) e0258272; issued 2021-10-05; CC BY 4.0 vor; no update-to. Page prints the Creative Commons Attribution License sentence. Accepted. Faults 0.
- Lines 5 and 6 (Koschier et al., insects15040297). Crossref: Elisabeth H. Koschier, Lena Dittmann, Bernhard Spangl; title identical; Insects 15(4) 297; issued 2024-04-22; CC BY 4.0 vor; no update-to. Page: "This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution" " (CC BY) license (https://creativecommons.org/licenses/by/4.0/)." Accepted. Faults 0.

Bibliographic faults 0; licence faults 0. source.access "open" right for all six.

## Names

- Ectatomma brunneum (line 1): not in gbif-names.tsv; OBIS total 0 (terrestrial). AntWiki: "Ectatomma brunneum Smith, F., 1858", valid, Formicidae, Ectatomminae, Hymenoptera (original spelling brunnea; brunneum is the current spelling). Met. The note's family route (main's Cataglyphis bicolor rows, another subfamily) is superseded by this species-level source (note replacement, uncounted).
- Neoponera inversa (line 2): not in gbif-names.tsv; OBIS total 0. AntCat 442939 "Neoponera inversa (Smith, 1858)", valid, original combination Ponera inversa; AntWiki: Formicidae, Ponerinae, Hymenoptera. Met. AntWiki also says "Separation of N. inversa from N. curvinodis is difficult."; the paper does not say who identified the colonies (uncounted, disclosed in the note replacement).
- Frankliniella occidentalis (line 3): main gbif-names.tsv:1904 EXACT ACCEPTED; Thripidae, Thysanoptera as on main's three behaviour_vision rows (insects11070423). Laboratory culture of field-collected stock (collected from Capsicum annuum in Beijing, reared on Phaseolus vulgaris pods; generations not stated) accepted at species rank under audit 332 (laboratory colonies of a wild species are not breeds). Met.
- Chionoecetes opilio (line 4): not in gbif-names.tsv; OBIS taxonID 107315 "Chionoecetes opilio" "(Fabricius, 1788)", accepted, superfamily Majoidea, family Oregoniidae, order Decapoda. The record's family and order are right. Owner question answered: Oregoniidae confirmed at species level on OBIS; the note's WoRMS-search-listing provenance is replaced (uncounted).
- Asproparthenis punctiventris (lines 5, 6): not in gbif-names.tsv; OBIS total 0. EPPO CLEOPU: preferred name "Asproparthenis punctiventris (Germar)", synonyms Bothynoderes punctiventris, Cleonus punctiventris, Lixus punctiventris; Curculionidae, Coleoptera. Met.

Name faults 0.

## Duplicates

git grep on origin/main (6c4d6091) across the whole docs/ tree (evidence, audit incl. audit/corrected and audit/ALL, sheets, searched, gaps, wanted, progress, batches) for each DOI suffix (pone.0225507, insects11030177, pone.0258272, insects15040297), for Ectatomma, Neoponera, Chionoecetes, opilio, "snow crab", Asproparthenis, and for Frankliniella occidentalis with its traits; then the branch-only additions (`git diff origin/main...<branch>`) of all 131 remote branches matching origin/research/desk-d2* or origin/research/audit-3*; and grep of docs/tracks/progress/audit-3*.md hold-outs.

- No DOI or genus of this unit is on main or on any other branch except research/desk-d257 itself; Asproparthenis appears only in desk-d226's "Not opened" list (main and its branch), a different paper (Insects 17(8)) not filed. No audit-3* hold-out names any of these DOIs.
- Frankliniella occidentalis on main: behaviour_vision (insects11070423, 3 rows), lambda_max_nm (annurev-ento-061720-071644 and fevo.2021.776827); the one "sense_chemical" hit is a Capsicum annuum plant row (desk-d127:1) that mentions the thrips. No F. occidentalis sense_chemical row; no duplicate.
- Main's sense_magnetic rows: 49 taxa, including Emberiza bruniceps (one row, ani11061541, desk-d156, audited in audit 241); no Formicidae, no ant genus, and neither ant row repeats a main magnetic row by DOI or species. Chionoecetes absent from main (the "opilio" hits are Phalangium opilio, Opiliones).

Duplicates 0.

## Trait keys and rulings

- sense_magnetic, ant coil Y-maze (lines 1, 2): owner question. Keep, with the confounds stated. The study manipulates the field with Helmholtz coils and controls coil presence ("As a control, the experiment was also performed with the coils positioned in the same place but switched off"), so the coil as an object at one arm is controlled; what is not controlled is everything that comes with powering the coils. There are no sham (current-cancelling, bifilar) coils, and the authors write that "we cannot rule out the fact that the ants could have changed their behaviour due to some kind of stress caused by the coils," "as these devices can increase the temperature of the space between them"; their body-heat tests are "not part of this study." The change is large: "the increase in the horizontal component of the MF to 60 μT, together with the vertical component of -10.6 μT," "cause an increase in the total magnetic field to 60.9 μT," "which corresponds to approximately 3 times the normal geomagnetic field." That is a response to a coil-on condition of about three times local field, not a threshold, and it cannot be read as magnetoreception proper while heat and other powered-coil effects remain. Filing it as a sense_magnetic behavioural finding with those limits in conditions is on the same footing as main's other coil-manipulation rows; the owner may prefer to hold both lines out until a sham-coil result exists. Each species carries its own clause and statistic in the quote ("E. brunneum (χ2 = 34.8, p < 0.05)" and "N. inversa (χ2 = 53.9, p < 0.05)"), so one quote for two lines is acceptable.
- sense_chemical, thrips Y-tube (line 3): acceptable (odour against solvent in a Y-tube, choice counted); lab-reared stock acceptable under audit 332.
- behaviour_vision, snow crab LED pots (line 4): owner question. Acceptable with the stimulus limits disclosed. Unlike the audit-350 Chelonia nets and the audit-351 trammel nets, the page reports no peak wavelength, intensity or flashing/constant mode for the "White and green PotLight LED fishing lights", and the authors write "However, the light intensity that can attract the crabs to the pots is unknown." The design still manipulates light (lit test pots against unlit baseline pots on the same longline, same bait), so it is not the uncontrolled-covariate case held out in audit 351 line 7; it supports "a green light in a baited pot raised legal-size catch", and nothing about colour or intensity. Fixed alternation ("Each T pot with a LED light was followed by two B pots (T-B-B-T-B-B-T…);"), soak and line differences ("it was not possible to keep similar soaking time conditions for all three experiments.") and "The pots of the three series were not fished simultaneously" must stay in conditions.
- sense_chemical, weevil olfactometer (lines 5, 6): acceptable (leaf odour against three clean-air arms, positions rotated).
- Grade `m` right for all six.

## Per-record findings

### Line 1, Ectatomma brunneum, coil Y-maze

Results sentence verbatim in two abutting pieces in one response, on two passes ("There was a significant difference between the decision-making choices of workers of E. brunneum (χ2 = 34.8, p < 0.05)" | "and N. inversa (χ2 = 53.9, p < 0.05) between the conditions with normal MF and with applied MF."); "χ2" and spaced "p < 0.05" as printed. **Quote MATCH**, 39 words.

Value says more than the quote: the quote reports only that choices differed between normal and applied field; the direction ("chose the path away from the activated coils") is from a separate Results sentence ("There was a significantly higher number of choices for the path leading to the resource" "that was not placed between the activated coils."), which carries no species or statistic. The direction is already in conditions; the value must be cut to what the quote says.

Verified, verbatim: "We evaluated the foraging behaviour and decision-making of 10 foragers of each one of the six colonies of N. inversa" "collected in the Centro de Pesquisa da Lavoura Cacaueira in Ilhéus, BA, Brazil"; "and four colonies of E. brunneum collected in the vicinity of the campus of the" "Universidade Estadual de Mato Grosso do Sul (UEMS) in Dourados, MS, Brazil."; plaster nests "kept at a temperature of 22 ± 2°C and photoperiod of 12:12 light/dark,"; "Each artificial nest was coupled to a Y-maze of 2.5 cm diameter and 65 cm length"; "a pair of Helmholtz coils was placed at on one end of the Y-maze, with each coil at 7.5 cm from the resource provided"; local field "a horizontal component of 19.8 μT," "a vertical component of -10.6 μT and a total component of 22.5 μT."; coils-off control; "No significant difference was found between the decision-making when the coils were off."; stopping "In 75% and 85% of cases, workers of N. inversa and E. brunneum, respectively, stopped their movement"; inclination ranges conflict (Fig 1 caption -23° to -10°, Discussion -28° to -10°). Coil side, trial order and trial numbers not reported (record right).

Not carried, verbatim: "two ants at the same time were allowed to access the" "Y-maze through the opening of the nest entrance." (the record gives the pairing but not that paired choices may not be independent); "we performed a chi-square test, using the path chosen by the ants as variables (with or without magnetic field)." with no counts or percentages printed ("The article gives no percentages or counts for path choice", tool summary); worker reuse, marking and whether the same colonies served both conditions are not stated (tool summary), and "the maze was cleaned with alcohol so that possible odours released by these ants would not affect the decision of following ants."; no sham coils and the authors' own stress caveat (above); the applied field is the horizontal component raised to 60 μT, total 60.9 μT, direction relative to the geomagnetic field not stated (the record's "applied field of about 60 uT" is close but not the printed construction; counted with the rest).

**Error (value exceeds quote; no sham coils, authors' stress caveat, paired-ant non-independence, missing counts and reuse omitted).** Fixable.

### Line 2, Neoponera inversa, coil Y-maze

Same sentence and verification as line 1; its clause "N. inversa (χ2 = 53.9, p < 0.05)" carries the line's value. **Quote MATCH**, 39 words. Same value fault and same omissions as line 1; the identification note (N. inversa vs N. curvinodis) is uncounted.

**Error (as line 1).** Fixable.

### Line 3, Frankliniella occidentalis, p-anisaldehyde and alfalfa volatiles

Results sentence verbatim in pieces, three passes ("Both PA and plant volatiles extracted from flowering M. sativa had attracting effects on WFT" | "(experiment sets 1 and 2, p = 0.022/0.014)," | "and the extracted volatiles were used as the olfactory cue (O)."); unspaced "0.022/0.014" with spaced "p = " as printed. **Quote MATCH**, 34 words; value says no more (the hexane control and n are design, verified: "C1, the use of pure hexane;"; "60 females were tested individually [7,23] for each experimental set.").

Verified, verbatim: collection "from Capsicum annuum (L.) in the Mentougou Bikun Vegetable Planting Center, Beijing" and rearing on Phaseolus vulgaris pods at "26 ± 1 °C"; Y-tube "inner diameter of the Y-tube olfactometer was 1 cm with two 10-cm-long arms"; "300 mL/min per arm"; "Adults aged 24 h that were starved for 4 h were used,"; "for 5 min."; "If an adult made no choice within 3 min, it was discarded and recorded as no response."; "Chi-square test," "with a 50:50 distribution."; "All analyses were conducted with SAS 9.2"; set 3 "lured 63.3% of WFT (p < 0.001, experiment set 3)."; set 5 "lured 75.0% of WFT, significantly more than the control (only 16.6% of WFT; p < 0.001; experiment set 5"; set 6 "(experiment set 6, VO: 55.0%" "V: 30.0%, p = 0.069, Figure 6a)". No percentages or chi-square values for sets 1 and 2 (record right).

Not carried, verbatim: set 7, "VO did not result in a significant increase in selection frequency compared with V alone" "but did result in an increased preference compared with O alone" "(experiment set 7, VO: 65.0%, O: 25.0%, p = 0.001, Figure 6a)."; set 4 (visual against olfactory) "The residence time of WFT on O was 213.2 ± 13.9 s, significantly higher than that of WFT on V (177.1 ± 10.9 s;" "experiment set 4, t47 = 2.59, p = 0.013)." with no choice percentages for that set (tool summary); the Y-tube dose is not stated: the only PA dose is the cylinder assay's "10% p-anisaldehyde (PA; v/v; Sigma-Aldrich, Oakville, Canada) diluted with hexane", and for volatiles only "Volatiles (10 μL) added to the yellow flower-shapes" (the VO cue) and "the airflow passed vials at the base tube"; the number of non-responders is not reported (tool summary).

**Error (sets 4 and 7 results, unstated Y-tube doses and unreported non-response omitted).** Fixable.

### Line 4, Chionoecetes opilio, green LED pots

Results sentence verbatim in three abutting pieces in one response ("In the third series using green LED lights and 17-day soaking time, the catch efficiency of the pots for snow crabs" | "with CW above the minimum landing size increased significantly by 76%" | "(CRaverage+ = 176.38 (CI:145.72–216.07))."); en dash checked. **Quote MATCH**, 36 words; value says no more.

Verified, verbatim: "We deployed 174 pots in series 1 (white LED with 8 days soak time) and 2 (white LED with 14 days soak time),"; "and 135 pots in series 3 (green LED with 17 days soak time)."; "Each of the experimental series contained 48 to 54 T pots and 81 to 126 B pots"; "In total, 1583 crabs were measured for the T pots and 2065 for the B pots"; "Pots in each of the series were linked on one separate longline"; "The depth of the fishing grounds varied between 250 and 280 m."; "1st to 24th of May 2020 in the Barents Sea"; "(ICES area 1.b)"; "After every second or third B pot there was a T pot."; "at least a 30 m distance between each pot."; no randomisation described; "The retention of undersized crabs did not differ significantly when using green LED lights,"; size distributions "did not show clear" "significant differences in any of the three series."; "No significant difference in catch efficiency between green and white LED lights were shown" "since the confidence bands overlap between the different treatments."

Not carried, verbatim: no wavelength, intensity or mode reported (tool summary) and the authors' "However, the light intensity that can attract the crabs to the pots is unknown."; "The pots of the three series were not fished simultaneously;" and "it was not possible to keep similar soaking time conditions for all three experiments." (the record gives the differing soak and line but states only that "no light intensity was found in the page text read"). Uncounted additions: undersized retention "approximately 10% and 20% in T and B pots, respectively."; "For pots with green lights, only 10–12% of the snow crabs were undersized."

**Error (stimulus undefined: no wavelength, intensity or mode, and the authors' unknown-intensity statement omitted; series not simultaneous).** Fixable.

### Line 5, Asproparthenis punctiventris, orache males only; fat hen and amaranth null

Abstract sentence verbatim in three abutting pieces in one response ("Males, but not females, responded positively to the leaf odour of the garden orache (A. hortensis)," | "and no response was observed when the weevils were tested with the leaf odours of fat hen (C. album)" | " or common amaranth (A. retroflexus)."). **Quote MATCH**, 40 words; value says no more (n = 36 per sex per plant verified: "This means the responses of 3 × 12 females and 3 × 12 males towards the leaf volatiles of each food plant" " species were recorded."; Table 1 "n = 36 per row", tool summary).

Verified: collection "In April and May of 2021 and 2022" from overwintering sites in winter wheat fields, Tullnerfeld, Lower Austria, pitfall traps "baited with the aggregation attractant Grandlure III-IV"; "5 ± 1 °C" in darkness; "A total of 48 to 72 h before the experiments, the individuals were separated by sex."; "Unmated females and males"; olfactometer "30 × 30 × 3.2 cm"; "250 mL/min at each of the 4 corners"; dark room, halogen lamp; three water-only control jars; leaf quantity "equivalent to 20 sugar beet leaves" at "BBCH stages 14 to 19"; quadrant 1 always the odour; "rotated by 90°" "after every third observation."; 6 min maximum; 3 min exclusion; chi-square goodness of fit (df = 3) and Friedman. Table 1 and Results: female A. hortensis first choice 13 vs 23, chi2 3.33, p 0.343; female time "p = 0.066"; female visits "p = 0.292"; female A. retroflexus time "p = 0.049", first choice 0.164, visits "p = 0.327"; female C. album all null; male C. album and A. retroflexus time and visits null. **MATCH.** Uncounted additions: male A. hortensis first choice 17 vs 19, chi2 11.33, p 0.010, time "(Friedman χ2 = 11.09, df = 3, p < 0.001" (that p is low for chi2 11.09 on 3 df, about 0.011 by the auditor's calculation; as printed), visits "Friedman χ2 = 19.22, df = 3, p < 0.001"; male C. album first choice 15 vs 21, chi2 6.89, p 0.076; whether excluded weevils were replaced or weevils reused is not stated (tool summary).

### Line 6, Asproparthenis punctiventris, sugar beet and chard both sexes

Abstract sentence verbatim in two abutting pieces in one response ("Females and males were equally attracted to the leaf odours of young B. vulgaris subsp. vulgaris plants," | " i.e., sugar beet and chard, as indicated by the overall picture of the behavioural parameters analysed."). **Quote MATCH**, 33 words.

Verified: Table 1 female sugar beet 18 vs 18, chi2 12.22, p 0.007; male 15 vs 21, chi2 6.22, p 0.101; female chard 17 vs 19, 11.56, 0.009; male chard 19 vs 17, 14.89, 0.002; male sugar beet time "p = 0.016", visits "p = 0.006"; chard time and visits significant in both sexes.

Not carried: female sugar-beet visits were not significant ("B. vulgaris Altissima group: Friedman χ2 = 7.19, df = 3, p = 0.066"), so for sugar beet each sex failed one of the three parameters; and the value drops the quote's qualifier "as indicated by the overall picture of the behavioural parameters analysed", stating equal attraction without it.

**Error (qualifier dropped from value; female sugar-beet visits null omitted).** Fixable.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Ectatomma brunneum, coil Y-maze | error, fixable | value, conditions, note (uncounted) | quote MATCH (39 words); value adds direction not in quote; no sham coils, authors' stress caveat, paired-ant non-independence, no counts, reuse unstated |
| 2 | Neoponera inversa, coil Y-maze | error, fixable | value, conditions, note (uncounted) | as line 1 |
| 3 | Frankliniella occidentalis, PA and alfalfa volatiles | error, fixable | conditions, note (uncounted) | quote MATCH (34 words); sets 4 and 7 omitted; Y-tube doses unstated; non-responders unreported |
| 4 | Chionoecetes opilio, green LED pots +76% | error, fixable | conditions, note (uncounted) | quote MATCH (36 words); no wavelength, intensity or mode, authors say attracting intensity unknown; series not simultaneous |
| 5 | Asproparthenis punctiventris, orache males only | MATCH | conditions, note (uncounted) | quote MATCH (40 words); male orache and fat-hen statistics uncounted |
| 6 | Asproparthenis punctiventris, sugar beet and chard | error, fixable | value, conditions | quote MATCH (33 words); "overall picture" qualifier dropped; female sugar-beet visits null (p = 0.066) omitted |

Errors 5 of 6 records (83%), above the 5% bar: scientific-context 5 (lines 1, 2, 3, 4, 6), of which value exceeding quote 3 (lines 1, 2, 6), omitted controls/confounds 3 (lines 1, 2, 4), omitted results 2 (lines 3, 6); names 0; quote form 0; bibliographic 0; licence 0; duplicates 0 against main, all 131 desk-d2* and audit-3* branches and the audit-3* hold-outs; grading 0. HOLD OUT: none.

Answers to the desk-d257 owner questions.
1. Ant coil Y-maze under sense_magnetic: keep, with the value cut to the quote and the no-sham-coil, stress/heat, threefold-field and non-independence limits in conditions; the owner may hold both lines out pending a sham-coil result.
2. Chionoecetes family: Oregoniidae (superfamily Majoidea, order Decapoda) confirmed on OBIS 107315.
3. Snow crab LED pots under behaviour_vision: acceptable as a lit-versus-unlit manipulation, but on a weaker footing than the audit-350 and audit-351 nets because the light is undefined; the record must say so.

## Unchecked

- Lines 1, 2: Fig 1 and the figures giving choice numbers (none printed in text); the Pheidole field result; who identified the ants.
- Line 3: Figure 6 bar values for sets 1, 2 and 4; whether non-responders were replaced to reach 60.
- Line 4: Fig 1 detail of light position; the coordinates as printed (tool flagged malformed); which alternation pattern belonged to which series.
- Lines 5, 6: Table 2 (time and visits as percentages); exclusions and replacement counts.

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). For blank fields the form is field = new string.

Line 1, counted:
- `value`: "chose the path away from the activated coils significantly more often than with the coils off" -> "made path choices that differed significantly from those with the coils off"
- `conditions`: "gave an applied field of about 60 uT against a local total of about 22.5 uT (roughly three times local)." -> "raised the horizontal field component to 60 uT (local horizontal 19.8, vertical -10.6, total 22.5 uT), giving a total field of about 60.9 uT, roughly three times local; the direction of the applied field relative to the geomagnetic field is not stated."
- `conditions`: "Chi-square tests of choices between conditions." -> "Chi-square test with the path chosen as the variable, coils on versus off; no choice counts or percentages are printed for either condition. Two ants entered the maze together, so choices may not be independent; whether workers were marked, reused or tested in both conditions, and whether the same colonies served both conditions, is not stated (the maze was cleaned with alcohol between ants)."
- `conditions`: "but those results are not part of the study." -> "but those results are not part of the study, and the authors write that they cannot rule out stress caused by the coils. There were no sham (current-cancelling) coils, so the applied field is not separated from heat or other effects of powering the coils."
- `note` (uncounted): "(Crossref single-DOI lookup refused, robots_disallowed)" -> "(Crossref single-DOI lookup answered in audit 353: same authors and title, PLOS ONE 14(11) e0225507, issued 2019-11-25, CC BY 4.0 vor)"
- `note` (uncounted): "taken from the ant main rows (Cataglyphis bicolor)." -> "from AntWiki (Ectatomma brunneum Smith, 1858, valid; Formicidae, Ectatomminae; audit 353)."

Line 2, counted:
- `value`: "chose the path away from the activated coils significantly more often than with the coils off" -> "made path choices that differed significantly from those with the coils off"
- `conditions`: "gave an applied field of about 60 uT against a local total of about 22.5 uT (roughly three times local)." -> "raised the horizontal field component to 60 uT (local horizontal 19.8, vertical -10.6, total 22.5 uT), giving a total field of about 60.9 uT, roughly three times local; the direction of the applied field relative to the geomagnetic field is not stated."
- `conditions`: "Chi-square tests of choices between conditions." -> "Chi-square test with the path chosen as the variable, coils on versus off; no choice counts or percentages are printed for either condition. Two ants entered the maze together, so choices may not be independent; whether workers were marked, reused or tested in both conditions, and whether the same colonies served both conditions, is not stated (the maze was cleaned with alcohol between ants)."
- `conditions`: "but those results are not part of the study." -> "but those results are not part of the study, and the authors write that they cannot rule out stress caused by the coils. There were no sham (current-cancelling) coils, so the applied field is not separated from heat or other effects of powering the coils."
- `note` (uncounted): "(Crossref single-DOI lookup refused, robots_disallowed)" -> "(Crossref single-DOI lookup answered in audit 353: same authors and title, PLOS ONE 14(11) e0225507, issued 2019-11-25, CC BY 4.0 vor)"
- `note` (uncounted): "taken from the ant main rows (Cataglyphis bicolor)." -> "from AntCat 442939 (Neoponera inversa (Smith, 1858), valid) and AntWiki (Formicidae, Ponerinae); AntWiki notes that N. inversa is difficult to separate from N. curvinodis, and the paper does not say who identified the colonies (audit 353)."

Line 3, counted:
- `conditions`: "and does not say whether arms were swapped or the stimulus side randomised." -> "and does not say whether arms were swapped or the stimulus side randomised. The Y-tube doses are not stated: 10% p-anisaldehyde in hexane is given only for the cylinder assay, and 10 uL of the alfalfa extract only for the card-plus-volatiles cue; the number of thrips recorded as no response is not reported."
- `conditions`: "the percentages for that pairing sum to 85%, unexplained." -> "the percentages for that pairing sum to 85%, unexplained. Card plus volatiles was chosen over volatiles alone (65.0% against 25.0%, p = 0.001); in the card-versus-volatiles pairing no choice percentages are given, but residence time was longer on the volatiles (213.2 +/- 13.9 s against 177.1 +/- 10.9 s, t47 = 2.59, p = 0.013). Generations in culture not stated; laboratory culture of field-collected stock accepted at species rank (audit 332)."
- `note` (uncounted): "Page prints CC BY 3.0; Crossref lookup refused (robots_disallowed), bibliographic data from the MDPI page." -> "Page metadata CC BY 3.0, no licence sentence in the body; Crossref (audit 353) gives the same authors and title, Insects 11(3) 177, issued 2020-03-11, CC BY 4.0 vor."

Line 4, counted:
- `conditions`: "no light intensity was found in the page text read, so colours are not compared at matched intensity." -> "the paper reports no wavelength, intensity or flashing/constant mode for the PotLight LEDs, and the authors write that the light intensity that can attract the crabs to the pots is unknown, so the stimulus is defined only as white or green light against none and colours are not compared at matched intensity; the three series were not fished simultaneously, and the authors say similar soak times could not be kept. Undersized retention was about 10% in test and 20% in baseline pots in the green series."
- `note` (uncounted): "Bibliographic data and CC BY 4.0 statement from the PLOS page (Crossref refused, robots_disallowed)." -> "Bibliographic data and CC BY statement from the PLOS page; Crossref (audit 353) gives the same authors and title, PLOS ONE 16(10) e0258272, issued 2021-10-05, CC BY 4.0 vor."
- `note` (uncounted): "taken from the WoRMS Oregoniidae/Chionoecetes listing seen in search (WoRMS page itself not opened; OBIS refused)." -> "confirmed on OBIS taxonID 107315 (Chionoecetes opilio (Fabricius, 1788), accepted; Majoidea, Oregoniidae, Decapoda; audit 353)."

Line 5, uncounted:
- `conditions`: "no repellent response in either sex." -> "no repellent response in either sex. Males on Atriplex hortensis: first choice 17 against 19 in the controls (chi2 = 11.33, p = 0.010), time Friedman chi2 = 11.09, df = 3, printed p < 0.001, visits chi2 = 19.22, p < 0.001; male Chenopodium album first choice 15 against 21 (chi2 = 6.89, p = 0.076). Whether excluded weevils were replaced, or weevils reused, is not stated."
- `note`: "Crossref refused (robots_disallowed), bibliographic data from the MDPI page." -> "page prints the CC BY 4.0 licence sentence; Crossref (audit 353) gives the same authors and title, Insects 15(4) 297, issued 2024-04-22, CC BY 4.0 vor. Name: EPPO CLEOPU preferred name Asproparthenis punctiventris (Germar), Curculionidae, Coleoptera."

Line 6, counted:
- `value`: "in a four-arm olfactometer" -> "in a four-arm olfactometer, as judged from the overall picture of first choice, time and visits"
- `conditions`: "For sugar beet, female first choice chi2 = 12.22, p = 0.007;" -> "For sugar beet, female first choice chi2 = 12.22, p = 0.007 and female time p = 0.001, but female visits were not significant (Friedman chi2 = 7.19, df = 3, p = 0.066), so for sugar beet each sex failed one of the three parameters;"

Verdict: 5 of 6 audited records in error (83%), above the 5% bar; lines 1, 2, 3, 4 and 6 fixable with the replacement text above; none held out; line 5 MATCH with uncounted additions.
