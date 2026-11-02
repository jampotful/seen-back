# audit-302: desk-d217, evidence lines 1 to 6 (of 12)

Audited 31 October 2026 from the desk-d217 files present untracked in the worktree (docs/tracks/progress/desk-d217.md and docs/views/evidence/desk-d217.jsonl, 12 lines; neither committed here, neither edited). HEAD 84c29a13 holds desk-d216. This audit judges lines 1 to 6 only; audit 303 judges lines 7 to 12. `tools/senses/check.py` on the evidence file: 12 records, 0 problems. Quote lengths (`len(q.split())`), lines 1 to 6: 12, 17, 19, 21, 17, 19, all within 40. The unit has evidence records only, so the shared brief's search-record and plant-screening parts do not apply; audit-301 is the format model; the caller's per-record method governs.

Sources opened (WebFetch): peerj.com/articles/2150 (one pass); peerj.com/articles/13825 (two passes); journals.plos.org article page for e0051100 (two passes, the second a character check of the quoted Abstract sentence); mdpi.com/2410-3888/8/1/26 (two passes); mdpi.com/2075-4450/7/2/19 (two passes); mdpi.com/2075-4450/8/3/90 (two passes); api.crossref.org/works for peerj.2150, peerj.13825, pone.0051100 and fishes8010026 (the two Insects DOIs were checked against the page citation lines only; Crossref for them not fetched, see below); en.wikipedia.org/wiki/Larimichthys_crocea (returned by my WebSearch). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries with verbatim pieces of about 125 characters; quotes were checked as MATCH/MISMATCH from consecutive verbatim pieces; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 1 WebSearch and 15 WebFetch calls used.

## Bibliographic and licence

- Line 1, Sfara et al. 2016, Crossref: Valeria Sfara, Gastón A. Mougabure-Cueto, Paola A. González-Audino, in the recorded order; title verbatim; PeerJ 4 e2150, no issue, issued 2016-06-28; CC BY 4.0 (unspecified); relation empty. Page: PeerJ 4:e2150, 2016, "Creative Commons Attribution License"; the page printed only "Sfara et al." (as the note says). Met.
- Line 2, Schwanitz et al. 2022, Crossref: Timothy W. Schwanitz, James J. Polashock, Dara G. Stockton, Cesar Rodriguez-Saona, Diego Sotomayor, Greg Loeb, Chloe Hawkings, as recorded; title verbatim; PeerJ 10 e13825, issued 2022-09-16; CC BY 4.0; relation empty. Page: Creative Commons Attribution License. Met.
- Line 3, Hart et al. 2012, Crossref: thirteen authors, Vlastimil Hart to Hynek Burda, in the recorded order; title verbatim; PLoS ONE 7(12) e51100, issued 2012-12-05; CC BY 4.0; relation empty. Page: "distributed under the terms of the Creative Commons Attribution License", citation PLoS ONE 7(12): e51100 (2012). Met.
- Line 4, Zhu, Zhang, Yan, Crossref: Aijun Zhu, Xiaolin Zhang, Xiaojun Yan; title verbatim; Fishes 8(1) 26; issued and published-online 2022-12-30, no published-print; CC BY 4.0 (vor). Page citation line: "Fishes, 2023, vol. 8, issue 1, article number 26" (tool summary); page CC BY with metadata link CC BY 3.0 (version difference, accepted). Uncounted: the record carries Crossref's issued year 2022 while the printed citation year is 2023; as audits 25 and 277 ruled for online-December, January-volume MDPI papers, not counted, and the note already names both; the caller's "printed year wins" points to 2023 (owner question 1).
- Line 5, Tang et al. 2016: page "Insects 2016, 7(2), 19; https://doi.org/10.3390/insects7020019", authors Rui Tang, Feng Zhang, Zhong-Ning Zhang, as recorded; page open-access statement plus CC BY 3.0 metadata link; Crossref CC BY 4.0 per the note (not re-fetched). Version difference, accepted. Met on what I read.
- Line 6, Indacochea et al. 2017: page "Insects 2017, 8(3), 90; https://doi.org/10.3390/insects8030090", authors Andres Indacochea, Charlotte C. Gard, Immo A. Hansen, Jane Pierce, Alvaro Romero, as recorded; CC BY with metadata CC BY 3.0. Met on what I read.

Bibliographic faults 0 (one uncounted year question); licence faults 0. Crossref not fetched for lines 5 and 6: authors, volume, issue and year match the page citation lines, so nothing turns on it.

## Names

GBIF API not used. docs/views/gaps/gbif-names.tsv: Blattella germanica EXACT ACCEPTED (usage 1997215); Cyprinus carpio EXACT ACCEPTED (4286975); the other four absent.
- Drosophila suzukii (Drosophilidae, Diptera), Hyphantria cunea (Erebidae, Lepidoptera), Triatoma rubida (Reduviidae, Hemiptera): printed in each paper's title; no synonymy question raised by anything read. Not checked against an authority page (none opened); not counted.
- Larimichthys crocea (line 4): Wikipedia taxobox gives Larimichthys crocea (Richardson, 1846), Sciaenidae, order Acanthuriformes, with Pseudosciaena crocea and Sciaena crocea as synonyms. Accepted (aggregator page). Main has no Sciaenidae row, so no order convention to conflict with; the unit's owner question on Perciformes is answered: Acanthuriformes is as recorded.

Name faults 0.

## Duplicates

git grep on origin/main across docs and src (evidence, audit/corrected, audit/ALL.jsonl, searched, sheets, gaps, codex-findings, batches, progress notes) for "Blattella", "germanica", "peerj.2150", "Sfara", "DEET", "suzukii", "peerj.13825", "Schwanitz", "Cyprinus carpio", "0051100", "Christmas", "magnetic alignment", "Larimichthys", "fishes8010026", "Hyphantria", "insects7020019", "Triatoma", "insects8030090", "Indacochea", every trait included.
- Line 1: Blattella germanica on main only as lambda_max_nm (corrected/insect:134, :135; ALL:1516, :1517) and harvest search records; "DEET" hits are the tick unit (desk-d201) and audit 285. Not a repeat.
- Line 2: "suzukii" on main is Striglina suzukii (oa-1 opsin rows). Not a repeat.
- Line 3: Cyprinus carpio on main is lambda_max_nm (oa-7:728 to 731, retracted in ALL) and sense_hearing (desk-d184:7, :8; desk-d160:6); no sense_magnetic carp row, no 0051100; "Christmas" hits are unrelated (flower-clock and plant rows). Not a repeat.
- Line 4: Larimichthys only in desk-d197.md:15 (an otolith paper held out). Not a repeat.
- Line 5: Hyphantria cunea on main only spectral_range_nm (oa-13a:249, :250) and gaps/queue entries. Not a repeat.
- Line 6: Triatoma on main is T. infestans eye_type (corrected/insect:429) and a Reduvius search record. Not a repeat.

Duplicates 0. Contradictions 0.

## Per-record findings

### Line 1, Blattella germanica, sense_chemical, 0.23 mV, Sfara et al. 2016

Results, verbatim: "We measured a mean electrical response of 0.23 mV to the repellent." MATCH, whole sentence, 12 words; the sentences before and after are separate (tool summary). Methods, verbatim: "Adult males of B. germanica of 7–20 days-old since molt were used."; "Nine independent replicates were performed."; "a 3 s air puff"; "loaded with 25 µl of pure DEET". Adaptation: "the ratio of the response after and before the pulse of DEET is lower than 1"; "The ratio of the responses after/before a clean air puff is near 1."; "A total recovery of the response was observed 10 min after exposure." Conditions match. Grade m right. Trait key fits (living insect antenna to an odorant).

Uncounted: each of the nine replicates is the mean of three recordings from one antenna, each antenna used once (tool summary); the page reports no variance for 0.23 mV and no absolute clean-air amplitude to set it against; the response recovered fully 10 min after the 60 s pulse. Worth adding.

Line 1: 0 counted. Stands.

### Line 2, Drosophila suzukii, sense_chemical, summer morph entered traps more, Schwanitz et al. 2022

Results, verbatim: "More summer morph flies entered the traps than winter morph flies, even at lower temperatures (Table 2)." MATCH, whole sentence, 17 words. Table 2 (tool summary): trap entry temperature χ² 334.64, df 4, p < 0.001; morphotype χ² 15.45, df 1, p < 0.001; interaction χ² 5.50, df 4, p = 0.239; survival interaction χ² 17.03, p = 0.002; activity morph χ² 7.45, p = 0.006, interaction χ² 41.04, p < 0.001. Methods, verbatim: "Inside the container, a gated trap was filled with five mL cornmeal diet (Fig. 1B)."; "Choice (response) was measured as the number of flies entering the trap out of the total number released." Discussion, verbatim: "it is possible that the height of the trap opening biased results toward flying insects."; "Indeed, our behavioral experiments show that winter morph flies appeared less motivated to seek food, despite overall higher activity levels". Females, 10 per arena, 72 h acclimation, 5 replicates per morph and temperature in three trials: as recorded.

**Error (design confound omitted, control).** Each arena held one baited trap and no unbaited trap (no blank is described in what I read, tool summary), so trap entry is not shown to be an odour response rather than entry into any trap; the response counts entrants out of all released flies, dead ones included, while summer-morph survival fell at freezing (survival interaction p = 0.002); and the authors themselves say the trap opening's height may have biased results toward flying insects. The conditions, filed under sense_chemical, state none of this. Fixable.

Uncounted: the morph main effect (χ² 15.45, df 1, p < 0.001) is the statistic behind the value and could be added; the conditions' "lower trap entry in winter morphs is not separated from activity" sits against the paper's reading (winter flies more active overall yet captured less, read as lower motivation to seek food).

Line 2: 1 fault.

### Line 3, Cyprinus carpio, sense_magnetic, North-South alignment, Hart et al. 2012

Abstract, verbatim in two consecutive pieces: "We found that carps displayed a statistically highly significant spontaneous preference" / "to align their bodies along the North-South axis." Character check returned exact. MATCH, whole sentence, 19 words. Methods and Results (tool summary): 14,537 bearings, 80 tubs, 25 localities, 18 to 24 December 2011, 817 photographs; coding blind (about 30% of photos rotated, "analyzed blindly by five members of our team"); without inflow, 8°/188°, r = 0.437, N = 69 tubs, p = 1.85×10⁻⁶; unimodal p = 0.93; quadrimodal p = 0.10; inflow correlated r = 0.045, p < 0.05, inflow tubs excluded; light r = 9.64×10⁻⁴, n.s.; "we only measured parameters of the static magnetic field"; no field manipulation. Conditions match. Magnetic design controls: blind coding is in method; no sham or field-off, and the conditions say so ("a field correlation, not a controlled field manipulation"). Grade m right; trait key fits.

Uncounted: weighted statistics (r = 0.228, p < 0.001) could be added. The record's note says the Abstract sentence came back in full, while the progress note lists the Cyprinus quote among those joined from fragments; the two should agree (the sentence is exact either way).

Line 3: 0 counted. Stands.

### Line 4, Larimichthys crocea, sense_chemical, EOG thresholds 10^-11 (CA) and 10^-12 (CDCA) mol/L, Zhu et al.

Section 3.4, verbatim in two consecutive pieces: "The free BAs CA and CDCA had similar, nearly parallel C–R curves with detection thresholds of " / "10−11 and 10−12 mol/L, respectively." MATCH, whole sentence, 21 words (the unit's joined quote confirmed as contiguous text). Preceding sentence verbatim: "The BAs conjugated with taurine, TCA, TCDCA, and TDCA had similar C–R curves, " / "with lower detection thresholds of 10−11, 10−12, and 10−12, respectively." Cross-adaptation figures (43.56, 22.49, 35.43%; CDCA and L-serine unaffected) as recorded. Figure 6 legend, verbatim: "Response magnitudes are normalized as percentages of the response to 10−5 mol/L L-serine (mean ± S.E.M., n = 5)." Methods, verbatim: "Tests were performed at least twice for each concentration of the stimulus."; Y-maze: "five randomly selected fish were placed in the Y-maze tank."; "The test of each odorant was repeated at least 20 times."; "the test solutions were added to the choice arm with fewer fish by an experimenter not visible to the fish."; "Filtered seawater and DMSO served as controls." The Methods give no criterion for the detection threshold (tool summary; Statistics says only "p < 0.05 was taken to represent statistical significance").

**Error (sample misstated).** "Y-maze (n = 20 fish per test)": each trial used a group of five fish and each odorant was repeated at least 20 times; n = 20 is trials, not fish. "EOG on 5 fish" rests on the Figure 6 legend's n = 5; the Methods give no fish count.

**Error (design detail omitted, same field).** The value is a pair of thresholds, but the paper never says how a threshold was determined, and the Y-maze put the stimulus in whichever arm held fewer fish (side not randomised). Neither is in the conditions. Fixable.

Line 4: 2 faults, 1 record in error.

### Line 5, Hyphantria cunea, sense_chemical, females more sensitive than males, Tang et al. 2016

Abstract, verbatim in two consecutive pieces: "Females were, regardless of dosages," / "more sensitive to β-ocimene and cis-2-penten-1-ol in electro-physiological response tests than males." MATCH, whole sentence, 17 words. Results, verbatim: "No significant differences were observed in females among the four tested dosages of either β-ocimene" / "(ANOVA, F3,19 = 0.53, p = 0.67, Figure 1B) or cis-2-penten-1-ol (ANOVA, F3,20 = 1.32, p = 0.294)."; "Males, responded with higher intensities to 10 μg and 100 μg β-ocimene than to 1 μg and 1000 μg" (the Abstract's "than 1 μg" discrepancy is recorded); sex comparison "(GLM, F1,53 = 20.5, p < 0.001" and "(GLM, F1,54 = 49.3, p < 0.001) than males." Methods, verbatim: "The adjusted EAG value was expressed as a specific value by dividing by the standard compound value."; "Nonanal was used as a standard compound and solvent was used as the control."; "each compound was tested with 10 different antennae per gender"; "at least 6 antennae were tested for each dosage of each chemical compound." Grade m right; trait key fits.

**Error (design confound omitted).** The sex comparison is on relative EAG values (each response divided by that antenna's nonanal response), so "female antennae more sensitive" is a statement about responses relative to nonanal; a sex difference in the nonanal response itself would produce or mask it. The conditions name nonanal as "standard" but do not say the compared values are ratios to it. Fixable.

Uncounted: "eleven leaf volatiles were EAG-active" is background work cited in the Abstract, not this paper's test; EAG moths' age and mating status are not given in the EAG Methods.

Line 5: 1 fault.

### Line 6, Triatoma rubida, sense_chemical, CO2 choice effect, Indacochea et al. 2017

Section 3.1, verbatim in two consecutive pieces: "Concentrations of CO2 in an airstream significantly affected nymph choices (χ2 = 12.2, df = 3, p = 0.0067)" / " (Figure 2a)." (the figure call is a hyperlink displaying "(Figure 2a)"; confirmed on two passes).

**Error (quote not as printed).** The quote ends "... p = 0.0067)." and drops the trailing "(Figure 2a)" unmarked, the quote-form fault audits 231 and 232 counted. Fixable.

Content holds. Verbatim: "Fifty-one T. rubida nymphs were tested in CO2 experiments, 40 made choices."; "Nymphs chose 1600 ppm CO2 in almost half of all successful trials (19 out of 40 trials)" / "followed by 3200 ppm (9 times), 800 ppm (8 times), and 0 ppm CO2 (4 times)."; "1600 ppm of CO2 was chosen significantly more often than 0 and 800 ppm of CO2" (p = 0.002 and 0.034, tool summary) "with 3200 ppm CO2 not statistically different from either group"; "There were no differences in the percent of time spent by insects in each zone (range: 13.4–22%)"; "velocity (range 0.29–0.38 cm/s) (F3,80 = 0.34, p = 0.799)"; "Different ports were randomly selected as the experimental (treatment) port to minimize bias."; nymphs "fifth-instar nymphs 2–3 weeks post-feeding". Conditions match. Grade m right.

Uncounted: method could add fifth-instar nymphs 2 to 3 weeks after feeding, treatment port randomised, choice counts per concentration (19, 9, 8, 4), pairwise p = 0.002 (1600 vs 0) and 0.034 (1600 vs 800); whether each nymph was tested once is not stated; the Abstract words the result as orientation to "either 1600 or 3200 ppm".

Line 6: 1 fault.

## Trait key

- Lines 1, 2, 4, 5, 6, sense_chemical: living animals' antennal, olfactory-epithelium or behavioural responses to odorants; fit. Line 2 is a within-species morph comparison of trap entry to a food odour; acceptable with the control caveat added.
- Line 3, sense_magnetic: spontaneous body alignment, field correlation; fits, as main's magnetic-alignment rows (desk-d186, desk-d188, cat-dog:117).

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Blattella germanica, sense_chemical, 0.23 mV EAG to DEET | stands (uncounted additions) | conditions | Quote MATCH (12 words); n = 9 males, 3 s puff, 25 µl, adaptation ratios as printed |
| 2 | Drosophila suzukii, sense_chemical, summer morph entered traps more | error, fixable | conditions | Quote MATCH (17 words); no unbaited control trap, dead flies in the denominator, and the authors' trap-height bias caveat all left out |
| 3 | Cyprinus carpio, sense_magnetic, N-S alignment | stands | none | Quote MATCH, character-checked (19 words); blind coding, no field manipulation, inflow exclusion and statistics as printed |
| 4 | Larimichthys crocea, sense_chemical, EOG thresholds 10^-11 and 10^-12 mol/L | error, fixable | conditions | Joined quote confirmed contiguous (21 words); Y-maze n = 20 is trials of five fish, not fish; no threshold criterion in the paper and stimulus put in the arm with fewer fish, not stated |
| 5 | Hyphantria cunea, sense_chemical, females more sensitive | error, fixable | conditions | Quote MATCH (17 words); sex comparison is on nonanal-normalised values, not stated |
| 6 | Triatoma rubida, sense_chemical, CO2 choice χ² 12.2 | error, fixable | quote | Quote drops the trailing "(Figure 2a)" unmarked; content holds |

Faults per record: line 1: 0; line 2: 1; line 3: 0; line 4: 2; line 5: 1; line 6: 1. 5 faults in 6 records; 4 of 6 records in error (66.7%): scientific-context 3 (lines 2, 4, 5); quote-form 1 (line 6); duplicates 0; licence 0; bibliographic 0; name 0; trait key 0; grading 0.

Pooled with audits 172 to 301: 309 of 707 evidence records (43.7%; 305 of 701 before this audit, and 4 of 6 here). Audit 303's lines 7 to 12 are not included. No search records.

## Replacement text

Line 2:
- `conditions`, replace "5 replicates per treatment per morph across three trials (Figure 4 legend says n = 15);" with "5 replicates per treatment per morph across three trials (Figure 4 legend says n = 15); each arena held a single baited trap and no unbaited control trap is described, so trap entry is not separated from entering any trap; response was 'the number of flies entering the trap out of the total number released', dead flies included, and summer-morph survival fell at freezing (survival temperature x morph chi-square 17.03, p = 0.002); the authors note 'it is possible that the height of the trap opening biased results toward flying insects'; morph main effect on trap entry chi-square 15.45, df 1, p < 0.001;".

Line 4:
- `conditions`, replace "EOG on 5 fish;" with "EOG n = 5 (Figure 6 legend; the Methods give no fish count and say each concentration was tested at least twice); the paper does not state how a detection threshold was determined (no criterion given);".
- `conditions`, replace "Y-maze (n = 20 fish per test):" with "Y-maze (groups of five fish, each odorant tested at least 20 times; the test solution was added to whichever arm held fewer fish, so side was not randomised; filtered seawater and DMSO as controls):".
- `year` (uncounted, owner's choice): 2023 if the printed citation year binds.

Line 5:
- `conditions`, replace "with solvent alone as control and nonanal as standard;" with "with solvent alone as control and nonanal as standard; all EAG values are relative (each response divided by the nonanal response), and the sex comparison is on these relative values, so a sex difference in the nonanal response itself would enter it (GLM sex effect F1,53 = 20.5 for beta-ocimene, F1,54 = 49.3 for cis-2-penten-1-ol);".
- `conditions` (uncounted), replace "eleven leaf volatiles were EAG-active and only these two were the subject of the sex comparison;" with "the Abstract cites eleven EAG-active mulberry leaf volatiles from earlier work, and only these two were tested here;".

Line 6:
- `quote`, replace with "Concentrations of CO2 in an airstream significantly affected nymph choices (χ2 = 12.2, df = 3, p = 0.0067) (Figure 2a)." (21 words).
- `method` (uncounted), append "; fifth-instar nymphs 2 to 3 weeks after feeding; the treatment port was chosen at random".
- `conditions` (uncounted), replace "the 1600 ppm port was chosen most often (19 of 40 choosing trials), more than 0 and 800 ppm," with "the 1600 ppm port was chosen most often (19 of 40 choosing trials; 3200 ppm 9, 800 ppm 8, 0 ppm 4), more than 0 ppm (p = 0.002) and 800 ppm (p = 0.034),".

Line 1 (uncounted):
- `conditions`, replace "(n = 9 per the Methods as relayed by the page-summary tool)" with "(nine replicates, each the mean of three recordings from one antenna, each antenna used once; no variance and no absolute clean-air amplitude are reported)" and append "; the response recovered fully 10 min after the 60 s pulse".

Line 3 (uncounted):
- `conditions`, append "; weighted statistics r = 0.228, p < 0.001".

## Owner questions (the unit's, answered where I could)

1. Year for Fishes 8(1): 26 (line 4): Crossref issued 2022-12-30, printed citation "Fishes 2023". Audits 25 and 277 left this uncounted; the caller's rule (printed year wins) points to 2023. Owner to fix the convention.
2. MDPI CC BY 3.0 metadata against Crossref CC BY 4.0 (lines 4 to 6): a version difference, accepted, as the caller's rules state.
3. Larimichthys crocea order: Acanthuriformes is what the taxobox read gives; main has no Sciaenidae row to conflict with.
4. Joined quotes: line 4's quote is contiguous on the page (confirmed). Line 3's quote was confirmed in one character check; its note and the progress note disagree on whether it was joined.
5. Hyphantria cunea quote (line 5): confirmed exact.

## Progress note

Accurate on citations, licences and duplicate checks for lines 1 to 6. Its summaries do not carry the faults found here (line 6's dropped figure call; lines 2, 4, 5 missing design caveats). The note lists Triatoma rubida as two traits; only line 6 (sense_chemical) is judged here.

Verdict: 4 of 6 records in error (66.7%), 5 faults, above the 5% bar; pooled 309 of 707 (43.7%). Error lines: 2, 4, 5 and 6, all fixable with the replacement text above. Lines 1 and 3 can merge.

This report is model output and carries no authority.
