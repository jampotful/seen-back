# audit-317: desk-d227, evidence lines 1 to 5

Audited 31 October 2026 from the desk-d227 files present untracked in the worktree (docs/tracks/progress/desk-d227.md and docs/views/evidence/desk-d227.jsonl, 9 lines; neither committed here, neither edited). Lines 6 to 9 belong to audit 318. HEAD and origin/main db3c6ecd (desk-d226). `python3 -I tools/senses/check.py | grep d227`: "docs/views/evidence/desk-d227.jsonl: 9 records, 0 problems". Quote lengths (`len(q.split())`) for lines 1 to 5: 26, 32, 11, 27, 16, all within 40. Evidence records only; audits 314 to 316 are the format model.

Sources opened (WebFetch): www.mdpi.com pages for 10.3390/insects10090274 (three passes), 10.3390/insects17060554 (one), 10.3390/ijms27094029 (one), 10.3390/biology14081032 (two), 10.3390/ani11010174 (two); api.crossref.org/v1/works for all five DOIs; for the sawfly family, bionames.org/references/2193d8de0672abf99fbe58e66b7abc9e and a Wikipedia mirror page for Nesoselandria (no use). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened (a ResearchGate result appeared in one search and was not opened). WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 3 WebSearches and 16 WebFetch calls used.

## Bibliographic and licence

- Line 1, Germinara, Pistillo, Griffo, Garonna, Di Palma 2019, Crossref /v1: authors in the recorded order; title verbatim; Insects 10(9), 274, issued 2019-08-27; CC BY 4.0 vor; relation empty, no update-to. Page: no licence sentence in the body, metadata CC BY 3.0. Accepted. Met.
- Line 2, Sun et al. 2026, Crossref /v1: eight authors Qi Sun to Tianyu Liang in the recorded order; title verbatim; Insects 17(6), 554, issued 2026-05-28; CC BY 4.0 vor; relation empty. Met.
- Line 3, Zhou et al. 2026, Crossref /v1: ten authors Mengqing Zhou to Bibo Zhou in the recorded order; title verbatim (with "(Selandriidae: Rhopographus)"); International Journal of Molecular Sciences 27(9), 4029, issued 2026-04-30; CC BY 4.0 vor; relation empty. Met.
- Line 4, Xie, Yuan, Wang, Tang, Yang, Zheng, Li 2025, Crossref /v1: authors in the recorded order; title verbatim; Biology 14(8), 1032, issued 2025-08-11; CC BY 4.0 vor; relation empty. Met.
- Line 5, de Vincenzi et al. 2021, Crossref /v1: ten authors Giovanni de Vincenzi to Francesco Filiciotto in the recorded order; title verbatim; Animals 11(1), 174, issued 2021-01-13; CC BY 4.0 vor; relation empty. Met.

Bibliographic faults 0; licence faults 0. source.access "open" right on all five. No retraction or update-to on any DOI.

## Names

- Aromia bungii (Cerambycidae, Coleoptera), Phthonoloba viridifasciata (Geometridae, Lepidoptera), Tomicus yunnanensis (Curculionidae, Coleoptera; Scolytinae is a curculionid subfamily; main's oa-1 rows leave family blank), Scyliorhinus canicula (Scyliorhinidae, Carcharhiniformes; same as main's desk-d147.jsonl:7; gbif-names.tsv:4413 "EXACT ACCEPTED"): right.
- Rhoptroceros cyatheae (line 3): family "Selandriidae" is not main's convention. Main files the selandriine genus Selandria under Tenthredinidae (gaps/cells.jsonl:4183, bee.md:508; 937 Tenthredinidae family fields, no "Selandriidae" anywhere on main), and Selandriinae is a tenthredinid subfamily (bionames.org reference title "Two new species of Selandriinae from China (Hymenoptera, Tenthredenidae)", Acta Zootaxonomica Sinica 32(4): 775-778, 2007). The paper's body gives "Rhoptroceros cyatheae (Hymenoptera: Selandriidae)" and its title adds "Rhopographus" without explanation (tool summary). **Name fault (family), fixable.** The species epithet itself could not be checked: a quoted search for "Rhoptroceros cyatheae" returned no taxonomic source. Unchecked, not counted.

Name faults 1 (line 3).

## Duplicates

git grep on origin/main across the whole docs tree (evidence, audit/corrected, audit/ALL.jsonl, searched, sheets, gaps, codex-findings, progress notes, batches) for "Aromia", "bungii", "Phthonoloba", "viridifasciata", "Rhoptroceros", "cyatheae", "Tomicus", "yunnanensis", "Scyliorhinus", "canicula", "Germinara", "de Vincenzi", "Boats Noise", "Phototactic Dimorphism", "Alsophila", "Selandri" and the five DOI suffixes. None of the five DOIs is on main. Aromia bungii appears only in desk-d217.md:21 (held lead); Phthonoloba and Rhoptroceros only in desk-d217.md:19 and desk-d218.md:19 (held leads). Tomicus yunnanensis is on main only for opsin_sequences_recovered (oa-1.jsonl:4433 to 4435, recheck-codex-b-fixed.jsonl:452 to 454, ALL.jsonl:5739 to 5741, all retracted there). Scyliorhinus canicula is on main for cff_hz (oa-3.jsonl:218, oa-6.jsonl:187), fovea (oa-3.jsonl:409) and sense_electric (desk-d147.jsonl:7; fish-shark corrected line 128 pooled with Raja), never sense_hearing. Duplicate faults 0.

## Per-record findings

### Line 1, Aromia bungii, male and female EAG similar, 17 of 90 differ

Discussion, verbatim in two consecutive segments: "A large degree of similarity between the EAG responses of males and females was observed" "with only 17 of the 90 compounds tested eliciting significant differences." MATCH, 26 words; value says no more. Confirmed: Marigliano apricot logs, 10 to 15 day old unmated adults, "Each compound was tested on five antennae of different insects of each sex.", 1 mg loads, mineral oil control and (Z)-3-hexenol standard after every five compounds, "Stimuli were randomly sequenced in the first and second set of experiments", mV ranges and 12 male-higher / 5 female-higher (tool summary for the split).

**Error (preparation misdescribed; dose-series and first-set results and sex null omitted; normalisation omitted).** (a) The paper ran three sets: "In the first set of experiments, the EAG responses of the basal (first to third), middle (fourth to sixth)..." (six VOCs on antennal portions); "In a second set of experiments, the EAG responses of flagellomeres seven to nine to different concentrations..." ((Z)-3-hexenol dose series); "In a third series of experiments, the EAG responses of flagellomeres seven to nine to 1 mg loads of test VOCs" (the 90-compound screen). The record's method says "on antennae", but the screen used excised distal portions (flagellomeres seven to nine), and it calls the dose series the "second set" as if the screen were the first. (b) Omitted dose-response results: "In both sexes, the activation threshold was 0.1 μg (p < 0.05; one-sample t-test).", "Male and female EAG responses increased from the 100 to 1000 μg doses" "indicating that no saturation of olfactory receptors occurred at the 100 µg dose.", and "For all doses tested, there were no significant differences" "between the mean EAG responses of the terminal male and female flagellomeres." (c) Omitted first-set result: "The mean EAG responses of the distal flagellomeres were significantly higher than those of the middle flagellomeres" (middle above basal, tool summary). (d) Omitted correction: "The resultant EAG value was corrected based on the reduction of the EAG amplitude to the standard stimulus" after subtracting the nearest mineral oil controls (tool summary for the subtraction); sex comparison by "Student's t-test" "(p = 0.05) for independent samples." Fixable.

### Line 2, Phthonoloba viridifasciata, female EAG 0.387 mV to 0.206 mV

Results 3.2, verbatim in two consecutive segments: "Female adults exhibited stronger EAG responses to 4-ethylbenzaldehyde (EAG = 0.387 ± 0.027 mV) among all tested compounds," "while showing the weakest EAG response to decane (EAG = 0.206 ± 0.008 mV)." MATCH, 32 words. Confirmed: Chishui larvae, 2 to 3 day unmated adults, five concentrations in ascending order, 0.5 s stimulus, 30 s interval, n-hexane before and after, sex differences for undecane (p < 0.05) and 4-ethylbenzaldehyde (p < 0.01), no sex difference for the other three; number of antennae not reported.

**Error (concentration said to be unstated when the figure states it; values are relative EAG; dose-response omitted).** (a) The record says the concentration is not stated; the Figure 2 caption says "Bars represent the relative EAG values of adults at 10−1 mol/L (mean ± SE)." So the mV values are relative EAG values at the highest concentration. (b) Omitted: "Undecane did not induce significant EAG responses in either sex at low concentrations (10−3, 10−4, and 10−5 mol/L)." and "For females, significant EAG responses were observed starting at 10−3 mol/L, and the response plateaued at 10−2 mol/L." (4-ethylbenzaldehyde). Fixable. Uncounted (behaviour, outside this trait): the Y-olfactometer results conflict internally (Abstract calls decane at 10⁻⁵ mol/L attractive to females; Results "exerted significant repellent effects on females"; tool summary), which matters if the desk files a behaviour record from this paper.

### Line 3, Rhoptroceros cyatheae, males stronger than females for most volatiles

Discussion, verbatim: "For most volatile compounds, male sawflies exhibited stronger responses than females." MATCH, 11 words. Confirmed: Chishui collection, 1 to 3 days post-emergence, virgin, 27 females and 27 males, triplicate, five concentrations low to high, n-hexane control, nine of 13 EAD-active compounds, Abstract (nine) versus Results 2.1 (13) wording mismatch, antenna preparation referred back to the GC-EAD section and not described there, 3-methylheptane slightly higher in females.

**Error (significant-null range omitted; female-higher compound omitted; relative EAG omitted; family).** (a) Results verbatim: "No significant sexual differences were observed in the relative EAG values elicited by all tested VOCs in the low-concentration range (0.01 and 0.1 μL/mL) and at 10 μL/mL." The record's "sex differences were concentration-dependent and larger at high concentrations" hides that three of five concentrations, including 10 μL/mL, show no sex difference for any compound. (b) "2-octanone induced significant sexual differences in relative EAG values at 10 μL/mL and 100 μL/mL" (this conflicts with the null at 10 μL/mL just quoted; tool returned both) and the Discussion says "females exhibited more significant EAG responses to 2-octanone."; the record lists only 3-methylheptane as female-higher. "tridecane caused highly significant sexual differences". No p values printed; two-way ANOVA. (c) Responses are relative: "Relative EAG response = EAG − (EAG ck1 + EAG ck2)/2,". (d) Family, under Names. Fixable.

### Line 4, Tomicus yunnanensis, phototaxis sensitivity by sex

Abstract, verbatim in two consecutive segments: "Phototaxis tests revealed females are highly sensitive to 360 nm, 380 nm, and 700 nm wavelengths," "while males exhibit high sensitivity to 360 nm and 400 nm." MATCH, 27 words. Confirmed: JiuLong Shan, January to February, 30 same-sex adults per trial, three replicates, each beetle used once, 300 to 700 nm in 20 nm steps (Methods), 300 lux at the stationary zone, 10 min dark adaptation and 10 min exposure, ANOVA F values, most beetles stay in the stationary zone.

**Error (value reframes the quote; criterion for "sensitive" and internal inconsistencies omitted).** (a) The value says "phototaxis peaks"; the quote says "highly sensitive". The Results define the female set as "peak sensitivity at 360 nm, 380 nm, and 700 nm" "(statistically indistinguishable from natural light responses)", that is, wavelengths whose response did not differ from natural light, and give no operational metric; "Following a 10 min exposure period, beetles in all zones were counted." with no scoring formula (tool summary). (b) The Figure 6 caption gives 200 to 700 nm against the Methods' 300 to 700 nm, and the ANOVA df (27,56) imply 28 conditions against 21 wavelengths plus darkness and natural light (tool summary). (c) Beetles "newly emerged" were collected in January to February while the Introduction gives April to May emergence (tool summary); sex was assigned by sound production checked against the last abdominal tergites. Fixable. Auditor's comment, not counted: a 300 lux calibration cannot equate stimuli at 300 to 360 nm, where photopic weighting is near zero; the record's "not photon-matched" covers the point in part.

### Line 5, Scyliorhinus canicula, tendency to occupy least noisy sections

Abstract, verbatim: "Moreover, their spatial distribution highlighted a tendency to occupy the least noisy sections of the aquarium." MATCH, 16 words. Confirmed: 12 sharks (6 + 6), trawled between Elba and Sardinia, month-long acclimation, 4 x 1 x 1.5 m tank in eight cells, underwater speaker "On the left wall" with limited response below a marked frequency, 100 to 140 dB re 1 μPa, random order, each animal used once, three replicates per condition (so three sharks per condition), Kruskal-Wallis H = 39.4, N = 96, p = 0.0005. No particle motion; the paper does not measure hearing and takes elasmobranch sensitivity from the literature: "Some studies have shown that elasmobranchs have an acoustic sensitivity threshold between 20 and 1500 Hz." and "there are no studies specifically focused on the inner ear of S. canicula."

**Error, HOLD OUT (value contradicted by the paper's own Results; hearing not shown).** (a) The quieter end is the right, farthest from the left-wall transducer (Discussion: "63% of this value was spatially distributed in the section farthest from the transducer"). Results: "In terms of spatial occupancy, there were no significant differences in swimming time among cells."; in the biological condition the sharks used the left (speaker) side more, "but also a difference, although not statistically, in the left section with respect to the right section" (65.1% and 34.9%); in the boat-louder condition the right-side bias was "although not statistically significant." (36.3% and 63.7%); no left/right result is given for the biological-louder condition. No significant result supports "least noisy sections"; the only significant spatial results are up/down at p = 0.05 (bottom use), and the noise field along the vertical axis is not reported. The Abstract sentence overstates the Results, so a record carrying it files an unsupported value. (b) Trait: the brief asks for hearing measured, not inferred. The paper measures a swimming-time response to playback in a small tank with sound pressure only; with three sharks per condition, N = 96 apparently from cells x replicates (not explained in the paper), and N1 = N2 = 12 unexplained, the experiment does not separate inner-ear hearing from near-field particle-motion or lateral-line detection, and the paper names none of these. The swimming-time result (48-word Abstract sentence; Results "Significant differences among the experimental acoustic conditions") shows a behavioural response to the playback, not hearing. Not fixable by text replacement; held out.

## Trait key

- Lines 1 to 3, sense_chemical: fit (EAG of living insects to host or test volatiles).
- Line 4, behaviour_vision: fits (phototaxis to monochromatic light), with the calibration and definition caveats in conditions.
- Line 5, sense_hearing: does not fit as filed (see line 5 (b)); counted inside the line 5 error, not separately.

Trait key faults 0 counted separately.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Aromia bungii, 17 of 90 differ by sex | error, fixable | method, conditions | Quote MATCH (26 words); screen used flagellomeres 7 to 9, not whole antennae; set order misstated; dose-series threshold, no saturation and no sex difference at any dose omitted; portion gradient and normalisation omitted |
| 2 | Phthonoloba viridifasciata, 0.387 to 0.206 mV | error, fixable | conditions | Quote MATCH (32 words); figure states 10⁻¹ mol/L and relative EAG; dose-response nulls and threshold omitted |
| 3 | Rhoptroceros cyatheae, males stronger | error, fixable | family, conditions | Quote MATCH (11 words); no sex difference at 0.01, 0.1 and 10 μL/mL omitted; 2-octanone female-higher omitted; relative EAG omitted; family Selandriidae against main's Tenthredinidae |
| 4 | Tomicus yunnanensis, sensitive wavelengths | error, fixable | value, conditions | Quote MATCH (27 words); "peaks" reframes "highly sensitive"; criterion "indistinguishable from natural light" omitted; 200 vs 300 nm and df inconsistency omitted |
| 5 | Scyliorhinus canicula, least noisy sections | error, HOLD OUT | whole record | Quote MATCH (16 words); Results show no significant cell or left/right difference; hearing not separated from near-field mechanosensation |

5 of 5 records in error (100%): scientific-context 5 (lines 1 to 5; line 5 also value unsupported and trait misapplied), value beyond quote 1 (line 4, counted within the same record), name 1 (line 3, same record), quote form 0, duplicates 0, bibliographic 0, licence 0, grading 0. HOLD OUT: line 5.

Pooled with audits 172 to 316: 375 of 783 evidence records (47.9%), adding 5 of 5 to audit 316's 370 of 778. Audit 318 judges lines 6 to 9 of this unit at the same time; its count should be added to this one, not to 783.

## Replacement text

Line 1:
- `method`: replace "electroantennography on antennae of males and females, 90 volatile compounds," with "electroantennography on excised distal antennal portions (flagellomeres seven to nine) of males and females, 90 volatile compounds,".
- `conditions`: replace "a second set used a (Z)-3-hexenol dose series of 0.001 to 100 ug/uL in ascending order on flagellomeres seven to nine;" with "the paper ran three sets: a first set compared basal, middle and distal antennal portions with six VOCs (distal flagellomeres responded significantly more than middle, and middle more than basal), a second set used a (Z)-3-hexenol dose series of 0.001 to 100 ug/uL (10 uL per load) in ascending order on flagellomeres seven to nine, and the 90-compound screen was the third set on flagellomeres seven to nine; dose-response: 'In both sexes, the activation threshold was 0.1 μg (p < 0.05; one-sample t-test).', responses still rose from 100 to 1000 ug (no saturation at 100 ug), and at every dose male and female terminal flagellomeres did not differ significantly; each response was corrected for control (mineral oil) and for the decline of antennal responsiveness using the standard;".
- `conditions`: replace "of the 17 differing compounds, male responses exceeded female for 12 and female exceeded male for 5;" with "of the 17 differing compounds (independent-samples Student's t-test, p = 0.05), male responses exceeded female for 12 and female exceeded male for 5;".

Line 2:
- `conditions`: replace "the quoted sentence does not say which concentration the mV values come from and the number of antennae is not stated;" with "the Figure 2 caption states 'Bars represent the relative EAG values of adults at 10−1 mol/L (mean ± SE).', so the quoted mV values are relative EAG values at the highest concentration; the number of antennae is not stated; dose-response: 'Undecane did not induce significant EAG responses in either sex at low concentrations (10−3, 10−4, and 10−5 mol/L).', and female responses to 4-ethylbenzaldehyde were significant from 10−3 mol/L and plateaued at 10−2 mol/L;".

Line 3:
- `family`: replace "Selandriidae" with "Tenthredinidae".
- `conditions`: replace "sex differences were concentration-dependent and larger at high concentrations;" with "sex differences were concentration-dependent: 'No significant sexual differences were observed in the relative EAG values elicited by all tested VOCs in the low-concentration range (0.01 and 0.1 μL/mL) and at 10 μL/mL.'; 2-octanone is reported as differing between sexes at 10 and 100 uL/mL (females higher, per the Discussion), which conflicts with that null at 10 uL/mL, and tridecane differed highly significantly; no p values are printed (two-way ANOVA, Figure 2 symbols only); responses are relative EAG values, the response minus the mean of the two n-hexane controls;".
- `note` (uncounted): replace "Name as printed in the title." with "Name as printed in the title; the paper's family Selandriidae is filed as Tenthredinidae (subfamily Selandriinae), main's convention; the species epithet was not checked against a taxonomic authority."

Line 4:
- `value`: replace "phototaxis peaks: females at 360, 380 and 700 nm; males at 360 and 400 nm" with "in phototaxis tests, females highly sensitive to 360, 380 and 700 nm and males to 360 and 400 nm".
- `conditions`: replace "per-wavelength values are only in Figure 6" with "per-wavelength values are only in Figure 6; the Results describe the female wavelengths as 'statistically indistinguishable from natural light responses', and the paper gives no scoring formula beyond counting beetles in all zones; the Figure 6 caption gives 200 to 700 nm against the Methods' 300 to 700 nm, and the ANOVA df (27,56) imply 28 conditions, more than the 21 wavelengths plus darkness and natural light described; beetles called newly emerged were collected in January to February although the Introduction gives emergence in April to May; sex was assigned by sound production checked against the last abdominal tergites".

Line 5: HOLD OUT. The Abstract value is not supported by the Results (no significant difference among cells; left/right differences not significant in any condition, and the biological condition leaned toward the speaker side), and the playback design does not establish hearing as distinct from near-field mechanosensation. No replacement; drop the record. If the owner wants a behavioural noise-response row, it would need a trait other than sense_hearing and the swimming-time Results sentence, which neither the desk nor this audit has read whole.

Values marked "(tool summary)" in the findings and reused above (middle above basal, control subtraction in line 1, the Figure 6 range and the df count, the January to April mismatch) should be confirmed against the page text when the desk applies them.

## Unchecked

- Rhoptroceros cyatheae as an accepted species name (no authority reached); Phthonoloba viridifasciata authority (not looked up).
- Line 1: whether mineral-oil subtraction used the two nearest controls (tool summary); Table values for the 17 differing compounds.
- Line 2: Figure 2 per-sex bar values; antenna count.
- Line 3: the Figure 2 legend's significance symbols per compound and concentration.
- Line 4: Figure 6 per-wavelength values and the list of 28 ANOVA groups.
- Line 5: Table 2 sound levels per cell (the noise field along the vertical axis).

## Owner questions (the unit's, answered)

- Rhoptroceros family: file as Tenthredinidae (main's convention for Selandriinae), with the paper's "Selandriidae" in the note. The title's "Rhopographus" is unexplained in the paper.

## Progress note

Accurate on citations, licences, quotes and duplicates. The Records list carries the faults above: Aromia without the no-sex-difference dose series; Phthonoloba's concentration called unstated; Rhoptroceros without the null at three concentrations; Tomicus as "peaks"; Scyliorhinus filed as hearing on an Abstract claim its Results do not support.

Verdict: 5 of 5 records in error (100%), above the 5% bar. Lines 1 to 4 fixable with the replacement text above; line 5 HOLD OUT. Pooled 375 of 783 (47.9%) before audit 318.

This report is model output and carries no authority.
