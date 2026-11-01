# audit-357: desk-d261, evidence lines 1 to 7

Audited 1 November 2026 from the desk-d261 files present untracked in the worktree (docs/tracks/progress/desk-d261.md and docs/views/evidence/desk-d261.jsonl, 7 lines; neither committed here, neither edited). Worktree HEAD and origin/main ee607fc7 (desk-d260 after audit 356). `python3 -I tools/senses/check.py | grep 'd261\.'`: "docs/views/evidence/desk-d261.jsonl: 7 records, 0 problems". Quote lengths (`len(q.split())`): 31, 40, 37, 37, 29, 33, 40, all within 40. Non-ASCII in quotes: "μ" three times and "…" in lines 3 and 4, "°" in line 5, all as printed or as a marked cut. Format model audits 355 and 356; desk-audit.md evidence clause (40-word limit, no 125-character limit); abutting pieces judged under the six conditions of audit-324.md, cuts under audit-331.md (lines 3 and 4 cut a trailing figure reference, marked).

Sources opened (WebFetch): api.crossref.org/v1/works/ for all six DOIs (10.1038/srep14805, 10.3390/life14111517, 10.3390/insects16100997, 10.3390/biology15090729, 10.1038/s41598-018-23710-x, 10.1038/s42003-024-07185-3; all answered, none robots_disallowed); nature.com srep14805 (two passes), s41598-018-23710-x (one), s42003-024-07185-3 (two); mdpi.com 2075-1729/14/11/1517 (two), 2075-4450/16/10/997 (two), 2079-7737/15/9/729 (one). Names: bionames.org/doi/10.5109/2423 (index of Morimoto 1982, Esakia 19); reptile-database.reptarium.cz/Phymaturus/williamsi. A Kyushu University library catalogue PDF in the search results was not opened (university library host). WoRMS, GBIF not opened (refused per rules). No curl, mirror, PMC, repository copy, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 2 WebSearches.

## Bibliographic and licence

- Line 1 (Pan et al. 2015). Crossref: ten authors in the recorded order; title identical; Scientific Reports 5(1) 14805; issued 2015-10-01; CC BY 4.0 vor; relation empty. Page: copyright line and "open access" only. Accepted. Faults 0.
- Line 2 (Chen et al. 2024). Crossref: six authors as recorded; title identical; Life 14(11) 1517; issued 2024-11-20; CC BY 4.0 vor. Page metadata CC BY 3.0, no body sentence. Accepted. Faults 0.
- Lines 3, 4 (Liu et al. 2025). Crossref: nine authors as recorded; title identical; Insects 16(10) 997; issued 2025-09-25; CC BY 4.0 vor. Page metadata CC BY 3.0. Accepted. Faults 0.
- Line 5 (Victorica Erostarbe et al. 2026). Crossref: five authors as recorded, accents as recorded; title identical; Biology 15(9) 729; issued 2026-05-05; CC BY 4.0 vor. Page metadata CC BY 3.0. Accepted. Faults 0.
- Line 6 (Prešern et al. 2018). Crossref: Janez Prešern, Jernej Polajnar, Maarten de Groot, Maja Zorović, Meta Virant-Doberlet; title identical; Scientific Reports 8(1) 5418; issued 2018-04-03; CC BY 4.0 vor. Accepted. Faults 0.
- Line 7 (Janža et al. 2024). Crossref: Rok Janža, Nataša Stritih-Peljhan, Aleš Škorjanc, Jernej Polajnar, Meta Virant-Doberlet; title identical; Communications Biology 7(1) 1533; issued 2024-11-19; CC BY 4.0 vor. Accepted. Faults 0.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout. Lines 6 and 7 are distinct papers (different DOIs, journals, years, designs and findings).

## Names

- Apolygus lucorum (line 1): not in gbif-names.tsv; the paper prints "Apolygus lucorum (Hemiptera: Miridae)" (verbatim). No synonym form (Lygocoris lucorum, Lygus lucorum) appears on main. Accepted status not checked against an index (GBIF refused); unchecked.
- Pagiophloeus tsushimanus (line 2): not in gbif-names.tsv. BioNames lists the species among names published in Morimoto 1982, "The family Curculionidae of Japan. 1. Subfamily Hylobiinae", Esakia 19: 51-121 (10.5109/2423, as printed on the index page). No synonym or other combination was found; Pachyrhynchus is an unrelated genus and the name is used as printed. Family from the paper's title (Coleoptera: Curculionidae). Met; accepted status rests on the original description and current use, not an index, and is noted.
- Culex quinquefasciatus, Aedes albopictus (lines 3, 4): gbif-names.tsv:1314 and :76, both ACCEPTED. Laboratory colonies accepted at species rank (audit 332). Met.
- Phymaturus williamsi (line 5): Reptile Database: "Lobo, Laspiur & Acosta, 2013", higher taxa Liolaemidae, Squamata, no other name given (tool summary). Met.
- Nezara viridula (lines 6, 7): gbif-names.tsv:3288 ACCEPTED. Both papers print "(Hemiptera, Pentatomidae)" in their own text (line 7's note says its paper names none: wrong, uncounted). Met.

Name faults 0.

## Duplicates

git grep on origin/main (ee607fc7) across the whole docs/ tree for each DOI suffix (srep14805, life14111517, insects16100997, biology15090729, 23710, 07185, s42003-024), each species name, Apolygus, lucorum, Pagiophloeus, tsushimanus, Prešern/Presern, Janža/Janza; behaviour_vision rows for the two mosquitoes; then the branch-only additions of all 140 remote branches matching origin/research/desk-d2* or origin/research/audit-3*; then the audit-3*.md hold-outs.

- No DOI of this unit is on main or any other branch except research/desk-d261 itself.
- Apolygus: searched sweep-46/sweep-101 rows only. Pagiophloeus, Phymaturus williamsi: absent.
- Mosquitoes: main holds lambda_max_nm (methods corrected:705) and acuity_cpd (canon-4:36, :49) rows; no behaviour_vision row from this paper. Not repeats.
- Nezara viridula: main holds two sense_vibration rows in docs/views/audit/corrected/insect.jsonl:425 and :427 (Virant-Doberlet and Čokl 2004 review, courtship signals; Zorović 2011, temporal pattern), plus a spectral_range_nm row (sweep-12:9). The desk note for line 6 says the species "appears only in older audit and gap files", which misses the two corrected sense_vibration rows (uncounted note fault). Different papers and values; by the audit-346 precedent not repeats. desk-d258 and audit-354 name the species only as the host of Trissolcus basalis.

Duplicates 0.

## Trait keys and rulings

- Lines 1, 2 sense_chemical: acceptable; single-dose odour preference, disclosed as not a threshold.
- Lines 3, 4 behaviour_vision (owner question 2). Acceptable with disclosure, not as a fully defined stimulus. Irradiance is stated for each step (5 to 1500 μW/cm2, UV340B meter), but the Y-maze Methods give no wavelength (345 nm only implied by "While the abovementioned experiments evaluated mosquito phototaxis with 345 nm UV light," and a 395 nm Y-maze test also exists) and do not say where irradiance was measured; the only measurement location in the paper is for the tube assay ("measured at the near-UV end of the tube"). So irradiance at the animal is not established. The record already discloses the wavelength; it must also disclose the measurement location. A UV-versus-dark phototaxis at graded intensity is a light-driven behaviour of the eye and is filed as such on main; it is not a sensitivity threshold.
- Line 5 sense_thermal: acceptable; a true spatial gradient (17 to 45 °C along 150 cm terraria from infrared lamps of different wattages at varying heights, verbatim pieces), lizards held at 24 °C for 3 to 4 days before trials, 11:00 to 18:00 h. Set-point range 34 to 36.8 °C is in conditions only; the value is categorical, so no list is needed.
- Lines 6, 7 sense_vibration (owner question 1). Line 6: a modelled behavioural threshold is acceptable under sense_vibration at grade m (grade m means "this species", docs/views/drafts/insects-met.md), on the audit-346 footing, provided the record says it is a model output: the Methods evaluate the delay distributions at hypothetical thresholds, two models give 0.27/0.39 ms and 0.31/0.46 ms (the second assumes random choice among directions), and no graded-delay behavioural test was run. The units already say "model-derived"; the value must be a two-number range. Line 7: playback of masking noise at levels registered "on the stem just below the stem-leaf branching" (verbatim), acceptable.

Grading 0 faults.

## Per-record findings

### Line 1, Apolygus lucorum, four of seven volatiles attractive

Abstract sentence verbatim in three abutting pieces in one response ("Although the adults responded to all seven synthetic plant volatiles in electroantennography tests, only four" | "(m-xylene, butyl acrylate, butyl propionate and butyl butyrate) elicited positive behavioral responses in" | "Y-tube olfactometer bioassays."); neighbouring sentences seen (tool summary). **Quote MATCH**, 31 words. Value says no more than the quote.

Verified: 60 insects per gender per compound, 10 μg on a 5 × 0.5 cm strip against mineral oil; unmated 6 to 8 day adults collected within 24 h of emergence from field-collected stock (Langfang, July and August) reared on bean pods and 10 % sucrose; Y-tube 3 cm, 15 cm arms, 60°, 300 ml/min, 2000 lux, 25 ± 1 °C; P values by sex as recorded; "Neither sex" difference P > 0.05; χ2 goodness-of-fit against 50:50; arm switching not described (tool summary). The text gives no statistics for the three non-attractive compounds (the record says "were not read"; reworded, uncounted). Omitted: "The individuals that remained unresponsive were not included in the analysis." (verbatim), their number not reported, so the test is of responders (sample composition); bioassays 08:00 to 18:00 h after 4 h starvation, Y-tube replaced "after four individuals had been tested" (uncounted additions).

**Error (sample composition: exclusion of non-responders omitted).** Fixable.

### Line 2, Pagiophloeus tsushimanus, camphor attractive

Abstract sentence verbatim in three abutting pieces in one response ("The Y-shaped olfactometer experiments and electroantennography measurements results showed that male and female adults of" | " P. tsushimanus had a positive chemotaxis towards volatiles released by C. camphora" | " and a negative chemotaxis towards volatiles released by C. chekiangensis or P. chekiangensis."). **Quote MATCH**, 40 words.

Results 3.3.1, verbatim pieces: "shows that both female (χ2 = 5.974, p < 0.01) and male (χ2 = 4.010, p < 0.05) adults" "exhibited a significantly higher response rate towards C. camphora compared to the control."; "Females did not show a significant preference for either C. chekiangensis (χ2 = 0.724, p > 0.05)" "or P. chekiangensis (χ2 = 1.290, P > 0.05) compared to the control."; "while males demonstrated a significantly lower preference rate towards C. chekiangensis (χ2 = 4.010, p < 0.05)" "and P. chekiangensis (χ2 = 4.010, p < 0.05) compared to the control."; sex comparisons of selection coefficients t = 0.535, 2.251, 0.717, all p > 0.05. Table 1 (verbatim rows): "C. camphora vs. air | 0.363 ± 0.104 | 0.306 ± 0.028", "C. chekiangensis vs. air | −0.131 ± 0.072 | −0.306 ± 0.028", "P. chekiangensis vs. air | −0.178 ± 0.097 | −0.310 ± 0.156"; no test of a coefficient against zero. The male χ2 of 4.010 printed for three comparisons and male coefficients of ±0.306 ± 0.028 for two plants support the record's reading of a reporting error. Plant-versus-plant and single-compound values (3.3.2, 3.5) match the record (tool summary).

The value carries the Abstract's "negative chemotaxis" for both sexes, which the Results show for males only; the record discloses the conflict in conditions but still files the unsupported half as the value. A value the paper's own Results contradict is an abstract-versus-Results fault; the value is cut to the C. camphora clause (says less than the quote, allowed) and the male avoidance stays in conditions. Also omitted: "If the insect did not enter the marked area within 5 min, it was recorded as a no-choice (not used for calculation)." (verbatim), number not reported (sample composition). n per sex per comparison is 18 (three repetitions of 6), as the method implies.

**Error (value carries an Abstract claim the Results contradict; no-choice exclusion omitted).** Fixable.

### Lines 3 and 4, Culex quinquefasciatus and Aedes albopictus, UV over dark

Results 3.1 sentence verbatim in three abutting pieces in one response, second pass ("Laboratory-reared Cx. quinquefasciatus and Ae. albopictus consistently preferred UV light at intensities ranging from" | "50 μW/cm2 to 1000 μW/cm2 over darkness, but did not show a significant preference between darkness and UV light at" | "1500 μW/cm2 ([Figure 1](#insects-16-00997-f001)B,C)."); the first pass returned the middle fragment only. Trailing figure reference cut and marked, acceptable under audit 331. **Quote MATCH**, 37 words each. The value's "females" and "in a Y-maze" are not in the quote; they describe sample and assay, already in method and conditions, and are moved there (uncounted).

Verified (tool summary unless quoted): the light source alternated between the long arms across two technical replicates; "Values represent mean ± SEM of ≥3 biological replicates (two technical replicates each)."; one-sample t or Wilcoxon against chance; n per intensity only in Table S1; females 4 to 10 days; Ae. aegypti LVP more sensitive as recorded. Omitted from both lines: mosquitoes that stayed in the release arm were excluded (sample composition); irradiance measurement location not stated for the Y-maze (calculated vs measured stimulus at the animal; see ruling); a 395 nm Y-maze test in which all three species preferred UV over darkness (uncounted addition). Line 4 also: the Ae. albopictus eggs were "purchased from Guangzhou Wolbaki Biotechnology Co., Ltd." (tool summary), a commercial supplier whose strain and infection status are not stated (colony origin); the record says only "purchased". That the supplier's business is Wolbachia-based mosquito control is my own reading of the company name; I have no source for the stock's infection status. And line 4's time of day: the conditions give ZT6 to ZT12 for the video assay, which is the Culex window; the Aedes video assay ran ZT1 to ZT10 (tool summary). Accepted at species rank as laboratory colonies under audit 332, with the supplier named.

**Line 3 error (release-arm exclusion and irradiance measurement location omitted).** Fixable.
**Line 4 error (as line 3; commercial supplier omitted; Culex time window given for Aedes).** Fixable.

### Line 5, Phymaturus williamsi, Tpref above field Tb

Abstract sentence verbatim in two abutting pieces in one response ("P. williamsi exhibited a preferred temperature higher than field body temperatures," | "together with high thermoregulatory effectiveness (E = 0.83) and a broad thermal tolerance range (TT = 35.41 °C)."); the sentences before and after seen; "°C" as printed. **Quote MATCH**, 29 words. Value says no more than the quote ("in a laboratory thermal gradient" is assay context).

Verified, verbatim: "We captured individuals of Phymaturus williamsi (n = 16) by hand and using nooses during October–November 2014."; Quebrada La Puerta, Calingasta, 2878 m; "kept at a controlled ambient temperature of 24 °C"; "maintained under these conditions for 8 days,"; "Thermoregulatory experiments were conducted 3–4 days after capture."; "Lizards were placed individually in terraria (150 × 45 × 80 cm)."; "A thermal gradient (17–45 °C) was generated using infrared lamps" "of different wattages positioned at varying heights"; ultrafine 1 mm cloacal thermocouples; "(11:00–18:00 h)," "recorded every 5 min for 3 h"; interquartile set-point range; "The mean body temperature (Tb) of P. williamsi was 32.20 ± 3.24 °C (n = 16)"; "Preferred body temperature (Tpref) was significantly higher than Tb (Wilcoxon signed-rank test: T = 16, p < 0.01)."; Figure 2 caption "Tpref = 35.3 °C", Tset 34 to 36.8 °C. Section 3.1 reports no sex analysis, as the record says. Natural photoperiod in captivity not carried (uncounted).

**MATCH.**

### Line 6, Nezara viridula, modelled delay threshold

Abstract sentence verbatim in two abutting pieces in one response ("Determined time delays as short as 0.5 ms resulted in marked changes in interneuron activity" | "and the decision model suggests that the behavioural threshold is in the range between 0.3 and 0.5 ms."); preceding sentence seen, the sentence ends the Abstract. **Quote MATCH**, 33 words.

Verified, verbatim: "The model's inputs were proportions of time delays and amplitude differences from the complete pool of measured values"; "the first model suggests that behavioural threshold is as low as 0.27 ms for FCS1 and 0.39 ms for FCS2."; "the behavioural threshold increased to 0.31 ms for FCS1 and 0.46 ms for FCS2." "under the assumption that searching males randomly choose one of the available directions"; "FCS1, number of tested males (N) = 11: 81%, χ2 = 72.02, df = 1, P < 0.01"; "FCS2, N = 19: 58%, χ2 = 42.91, df = 1, P < 0.05"; laboratory colony "from a single Slovenian population at the North Adriatic coastal region."; "The amplitude of stimulation was adjusted to the level of natural signals."; "the side from which the stimulation was applied was randomly changed."; "Among 51 neurons recorded in 42 individuals, in 11 interneurons neuronal activity was influenced". The record's design, nulls, the flagged χ2 inconsistency and the colony disclosure are right.

Value faults: a range filed as text where the desk files ranges as two-number lists (format); the interneuron clause is a second value in one field; the description "inter-leg time delay of a substrate vibration across a plant branching" is not in the quote; and the quote's "suggests" is dropped (the units' "model-derived" does not carry it into the value). Value becomes [0.3, 0.5] with the model qualifier in units and the interneuron result and both model variants in conditions.

**Error (value format and value says more than the quote; qualifier dropped).** Fixable.

### Line 7, Nezara viridula, masking noise

Abstract sentence verbatim in three abutting pieces in one response, second pass ("Noise impaired the ability of males to recognize the female signal and localise its source:" | "overlapping noise decreased sensitivity of receptor neurons to the signal and disrupted signal frequency encoding" | "by phase-locking units, while non-overlapping noise only affected frequency encoding."); before it "We found negative effects of vibrational noise regardless of spectral overlap, challenging common expectations.", after it "Modelling neuronal spike triggering". **Quote MATCH**, 40 words. Value says no more than the quote.

Verified, verbatim: "Adult *Nezara viridula* bugs were collected in autumn in the coastal part of Slovenia."; "We utilised 30 males in a 12-day experiment (25 tested per day)."; "Each male underwent testing in nine noise and one control treatment, the latter with only FCS played back to the plant."; "The amplitude of synthesized FCS was adjusted to 0.3 mm/s RMS,"; SNR 6, 0 and -6 dB; the three bands; "(n = 12)"; "24 to 0 dB SNR levels (in 6 dB steps)"; "For continuous data, reduced male participation in trials due to noise limited comparisons to the control" "and the 6 dB SNR levels for each playback treatment (n = 11 for signalling, n = 20 for searching)."; "In the response to FCS with added NON, neither the absolute nor the relative response reduction was evident"; "(not being statistically significant, however; Fig. 5b, Wilcoxon signed rank test with FDR correction, p > 0.05)."; "Localisation of FCS was less successful across all noise treatments compared with control," "with different bandwidths and amplitudes having similar effect". Not carried (uncounted): "with trials randomised by day and treatment" and playback side "randomized for each trial"; "Both FCS and noise were registered on the stem just below the stem-leaf branching". Note says the paper names no family; it prints "(Hemiptera, Pentatomidae)" (uncounted).

**MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Apolygus lucorum, 4 of 7 volatiles | error, fixable | conditions | quote MATCH (31); non-responders excluded, number unreported, omitted |
| 2 | Pagiophloeus tsushimanus, camphor attractive | error, fixable | value, conditions; note (uncounted) | quote MATCH (40); value files Abstract's negative chemotaxis that Results contradict for females; no-choice exclusion omitted |
| 3 | Culex quinquefasciatus, UV over dark | error, fixable | value (uncounted), conditions | quote MATCH (37); release-arm exclusion and irradiance location omitted |
| 4 | Aedes albopictus, UV over dark | error, fixable | value (uncounted), conditions | as line 3; commercial supplier omitted; wrong time window |
| 5 | Phymaturus williamsi, Tpref > Tb | MATCH | none | design, n, statistics verified |
| 6 | Nezara viridula, modelled 0.3 to 0.5 ms | error, fixable | value, units, conditions; note (uncounted) | quote MATCH (33); range not a list; extra clause and description; "suggests" dropped |
| 7 | Nezara viridula, masking noise | MATCH | conditions, note (uncounted) | design and nulls verified; family is printed in this paper |

Errors 5 of 7 audited records (71%), above the 5% bar; none held out. By kind: scientific-context 4 (lines 1, 2, 3, 4: responders-only samples on all three olfactometer/maze lines, irradiance location, supplier); abstract-versus-Results 1 (line 2); value form 1 (line 6); bibliographic 0; licence 0; names 0; duplicates 0 against main, all 140 desk-d2* and audit-3* branches and the audit-3* hold-outs; grading 0.

Answers to the desk-d261 owner questions.
1. A modelled behavioural threshold is acceptable under sense_vibration at grade m, as audit 346 accepted a modelled field under sense_electric, provided the units and conditions say it is a model output, give both model variants and their assumption, and the value is the two-number range.
2. UV versus dark at stated irradiance is acceptable under behaviour_vision with disclosure. Here the Y-maze wavelength is only implied and the irradiance measurement point is not stated, so the stimulus at the animal is not fully defined; both gaps go in conditions.

Unchecked: the GBIF/WoRMS status of Apolygus lucorum and Pagiophloeus tsushimanus (no index opened; names as printed and, for Pagiophloeus, as described by Morimoto 1982); supplementary Table S1 (n per intensity) and the Figure 1 statistics for lines 3 and 4; the field-collected Cx. quinquefasciatus results and the knockdown details in lines 3 and 4 (not reread); Phymaturus Table 1 (image); the Nezara figures and supplementary tables; the Apolygus greenhouse and field results.

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). For an empty new string the old string is deleted. "field = new string" replaces the whole field.

Line 1, counted:
- `conditions`: "The paper does not say whether Y-tube arms were swapped or assigned at random." -> "Bioassays ran 08:00 to 18:00 h after 4 h starvation; each insect was used once, with fresh filter paper, and the Y-tube was replaced with a clean one after every four insects. Individuals that remained unresponsive were not included in the analysis and their number is not reported, so the test is of responders. The paper does not say whether Y-tube arms were swapped or assigned at random."
- `conditions` (uncounted): "their P values, and percentages choosing each arm and chi-squared values, were not read." -> "the Results text gives no statistics or percentages for them."

Line 2, counted:
- `value` = "male and female adults showed positive chemotaxis in Y-tube tests toward volatiles from Cinnamomum camphora"
- `conditions`: "Tested at 2000 lx, 26 +/- 1 C;" -> "Insects that did not enter the marked area within 5 min were recorded as no-choice and not used for calculation; their number is not reported, so response rates are of responders. Tested at 2000 lx, 26 +/- 1 C;"
- `conditions`: "The Abstract sentence quoted says both sexes had a negative chemotaxis to the two other species, which the female nulls in Results do not show." -> "The Abstract sentence quoted also says both sexes had a negative chemotaxis to C. chekiangensis and P. chekiangensis; the Results support that for males only (females null, above), so the value carries only the C. camphora clause (audit 357). Selection coefficients (Table 1, female then male): C. camphora 0.363 +/- 0.104 and 0.306 +/- 0.028; C. chekiangensis -0.131 +/- 0.072 and -0.306 +/- 0.028; P. chekiangensis -0.178 +/- 0.097 and -0.310 +/- 0.156; the sexes did not differ (t = 0.535, 2.251, 0.717, all p > 0.05); no test of a coefficient against zero is reported."
- `note` (uncounted): "Family and order from the paper (title and Taxonomy line: Coleoptera: Curculionidae)." -> "Family and order from the paper (title and Taxonomy line: Coleoptera: Curculionidae). Pagiophloeus tsushimanus was described by Morimoto 1982 (Esakia 19: 51-121, 10.5109/2423, per the BioNames index); no synonym found; not in gbif-names.tsv (audit 357)."

Line 3, counted:
- `value` (uncounted) = "laboratory-reared mosquitoes consistently preferred UV light at 50 to 1000 uW/cm2 over darkness, but did not show a significant preference between darkness and UV light at 1500 uW/cm2"
- `conditions`: "Females 4 to 10 days after emergence;" -> "Females 4 to 10 days after emergence (Figure 1 legend: female mosquitoes); mosquitoes that stayed in the release arm were excluded and their number is not given in the text;"
- `conditions`: "Wavelength 345 nm is implied by Section 3.1 ('abovementioned experiments'), not stated in the Y-maze Methods." -> "Wavelength 345 nm is implied by Section 3.1 ('abovementioned experiments'), not stated in the Y-maze Methods; the Y-maze Methods name the meter (UV340B) but not where irradiance was measured, so the irradiance at the mosquito is not established. A further Y-maze test found all three species preferred 395 nm UV over darkness."
- `conditions` (uncounted): "Ae. albopictus eggs purchased" -> "Ae. albopictus eggs purchased from Guangzhou Wolbaki Biotechnology Co., Ltd. (commercial supplier; strain and Wolbachia status not stated)"

Line 4, counted:
- `value` (uncounted) = "laboratory-reared mosquitoes consistently preferred UV light at 50 to 1000 uW/cm2 over darkness, but did not show a significant preference between darkness and UV light at 1500 uW/cm2"
- `conditions`: "Females 4 to 10 days after emergence;" -> "Females 4 to 10 days after emergence (Figure 1 legend: female mosquitoes); mosquitoes that stayed in the release arm were excluded and their number is not given in the text;"
- `conditions`: "Wavelength 345 nm is implied by Section 3.1 ('abovementioned experiments'), not stated in the Y-maze Methods." -> "Wavelength 345 nm is implied by Section 3.1 ('abovementioned experiments'), not stated in the Y-maze Methods; the Y-maze Methods name the meter (UV340B) but not where irradiance was measured, so the irradiance at the mosquito is not established. A further Y-maze test found all three species preferred 395 nm UV over darkness."
- `conditions`: "Ae. albopictus eggs purchased" -> "Ae. albopictus eggs purchased from Guangzhou Wolbaki Biotechnology Co., Ltd. (commercial supplier; strain and Wolbachia status not stated; laboratory colony accepted at species rank under audit 332)"
- `conditions`: "(the video assay was run between ZT6 and ZT12)" -> "(the Aedes video assay was run between ZT1 and ZT10, the Culex one between ZT6 and ZT12)"

Line 5: no change.

Line 6, counted:
- `value` = [0.3, 0.5]
- `units`: "ms (inter-leg arrival-time difference); model-derived, not a measured threshold" -> "ms (range in which the decision model suggests the behavioural threshold for the inter-leg arrival-time difference lies; model-derived, not a measured threshold)"
- `conditions`: "Model thresholds about 0.27 to 0.46 ms;" -> "Same Abstract sentence: time delays as short as 0.5 ms resulted in marked changes in interneuron activity. Model thresholds: first model 0.27 ms for FCS1 and 0.39 ms for FCS2; second model, which assumes searching males choose randomly among the available directions, 0.31 and 0.46 ms; model inputs were the pooled measured delays and amplitude differences, evaluated at hypothetical thresholds;"
- `note` (uncounted): "the species appears only in older audit and gap files" -> "main holds two other sense_vibration rows for the species from different papers (docs/views/audit/corrected/insect.jsonl:425, Virant-Doberlet and Čokl 2004; :427, Zorović 2011; audit 357), not repeats"

Line 7 (uncounted only):
- `conditions`: "Physiology: 12 leg-nerve recordings." -> "Trials were randomised by day and treatment and the playback side was randomised per trial; signal and noise were registered on the stem just below the stem-leaf branching. Physiology: 12 leg-nerve recordings."
- `note`: "This paper's text read here names no family or order; Pentatomidae and Hemiptera follow the Abstract of the earlier paper on the same species by the same group, read in this unit (doi 10.1038/s41598-018-23710-x: 'Hemiptera, Pentatomidae')." -> "Family and order from this paper ('Southern green stink bug Nezara viridula (Hemiptera, Pentatomidae)'; audit 357)."
