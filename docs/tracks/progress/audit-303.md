# audit-303: desk-d217, evidence lines 7 to 12

Audited 31 October 2026 from the desk-d217 files present untracked in the worktree (docs/tracks/progress/desk-d217.md and docs/views/evidence/desk-d217.jsonl, 12 lines; neither committed here, neither edited). HEAD 84c29a13 (desk-d216). I judge lines 7 to 12 only; audit 302 judges lines 1 to 6. `tools/senses/check.py` on the evidence file: 12 records, 0 problems. Quote lengths (`len(q.split())`), lines 7 to 12: 11, 14, 15, 15, 28, 16, all within 40. The unit has evidence records only, so the brief's search-record and plant-screening parts do not apply; audit-301 is the format model.

Duplicates: git grep on origin/main across docs (evidence, audit/corrected, audit/ALL.jsonl, searched, wanted, sheets, gaps, codex-findings, progress notes) for "Triatoma", "rubida", "insects8030090", "Indacochea", "Cimex", "lectularius", "insects2010022", "Suchy", "Lobesia", "botrana", "insects10090281", "Gemeno", "Dastarcus", "helophoroides", "0190067", "Eptesicus" (with "magnet"), "0001676", "Holland", "Sclomina", "insects12110978", "Hypolepis", every trait included.

Sources opened (WebFetch): mdpi.com 2075-4450/8/3/90 (three passes), 2/1/22 (two passes), 10/9/281 (one pass), 12/11/978 (one pass); journals.plos.org e0190067 (one rate-limited fetch; one pass with an unencoded DOI returned a different article, Suli et al. 2012 PLoS ONE 7(2): e29727, discarded; one pass with the encoded DOI) and e0001676 (encoded, one pass); api.crossref.org/works for all six DOIs. Names: Wikipedia Larimichthys_crocea, a calacademy.org Eschmeyer catalog synonym page and PMC7706988 (Sclomina mitogenome), each returned by my WebSearch. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries with verbatim pieces of about 120 characters, so quotes were checked as MATCH/MISMATCH from piecewise verbatim returns; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 2 WebSearch and 17 WebFetch calls used.

## Bibliographic and licence

- Line 7, Indacochea et al. 2017, Crossref: Andres Indacochea, Charlotte Gard, Immo Hansen, Jane Pierce, Alvaro Romero, in the recorded order; title verbatim; Insects 8(3) 90, issued 2017-08-29; CC BY 4.0 (vor); relation empty. Page: "Insects 2017, 8(3), 90", authors "Andres Indacochea, Charlotte C. Gard, Immo A. Hansen, Jane Pierce and Alvaro Romero"; "open access Creative Common CC BY license", metadata URL CC BY 3.0. Version difference, both CC BY: met.
- Line 8, Suchy and Lewis 2011, Crossref: James T. Suchy, Vernard R. Lewis; title verbatim; Insects 2(1) 22-35, issued 2011-03-07; CC BY 3.0 (vor). Page: "Insects 2011, 2, 22-35", "Creative Commons Attribution license" at by/3.0. Met ("2(1): 22" gives the first page; acceptable).
- Line 9, Pérez-Aparicio et al. 2019, Crossref: Alicia Pérez-Aparicio, Luis M. Torres-Vila, César Gemeno; title verbatim; Insects 10(9) 281, issued 2019-09-02; CC BY 4.0 (vor). Page: "Insects 2019, 10(9), 281", metadata licence URL CC BY 3.0. Met (version difference).
- Line 10, Ren et al. 2017, Crossref: Li li Ren, Karthi Balakrishnan, You qing Luo, Stefan Schütz; title verbatim; PLOS ONE 12(12) e0190067, issued 2017-12-21; CC BY 4.0 (vor); relation empty. My page read also returned no licence or citation line (authors as Crossref). PLOS ONE page with a Crossref vor CC BY 4.0 and no conflicting tag: met, as the note records it (same ruling as audit-301 line 6).
- Line 11, Holland et al. 2008, Crossref: Richard A. Holland, Joseph L. Kirschvink, Thomas G. Doak, Martin Wikelski; title verbatim; PLoS ONE 3(2) e1676, issued 2008-02-27; CC BY 4.0 (unspecified version). Page: "Creative Commons Attribution License", no version printed. Met.
- Line 12, Huang et al. 2021, Crossref: Kerui Huang, Hui Shang, Qiong Zhou, Yun Wang, Hui Shen, Yuehong Yan; Insects 12(11) 978, issued 2021-10-28; CC BY 4.0 (vor). Page title in two verbatim pieces matches the record. My read found no printed licence statement on the page, only the metadata rights URL CC BY 3.0. Met (version difference); the note's "The MDPI page gives CC BY 3.0" should say the page metadata gives it (uncounted).

Bibliographic faults 0; licence faults 0.

## Names

- Cimex lectularius, Dastarcus helophoroides, Eptesicus fuscus: in docs/views/gaps/gbif-names.tsv as EXACT ACCEPTED. Accepted.
- Triatoma rubida, Lobesia botrana: not in gbif-names.tsv; GBIF not queried. Standard names as printed by their papers, no conflicting usage on main. Accepted on the printed name; owner question 1.
- Sclomina erinacea (line 12): PMC7706988 (mitogenome paper) gives "Sclomina erinacea Stål", "which belongs to the subfamily Harpactorinae", Reduviidae. Family as recorded. Accepted (paper, not a checklist).
- Larimichthys crocea order (line 4, audit 302's line, checked as the caller asked): Wikipedia's taxobox gives Order Acanthuriformes, Family Sciaenidae, and cites the 5th edition of Fishes of the World placing Sciaenidae in Acanthuriformes; an Eschmeyer's Catalog synonym page gives "Current status: Synonym of Larimichthys crocea (Richardson 1846)" with family Sciaenidae and no order. Acanthuriformes is consistent with Fishes of the World (5th ed.); I did not open Eschmeyer's own order classification.

Name faults 0.

## Duplicates

- Line 7: Triatoma on main is T. infestans eye_type (corrected/insect:429) and a sweep-101 search record; no T. rubida row, no 8030090, no Indacochea. Not a repeat.
- Line 8: Cimex lectularius on main is lambda_max_nm only (corrected/insect:155, corrected/methods:686); audit-51 and desk-d205 mention it as such; no sense_chemical row, no 2010022, no Suchy. Not a repeat.
- Line 9: Lobesia on main occurs only in searched records (sweep-47, -53, -55, harvest-52) and Gemeno in Cydia pomonella interommatidial rows and a tortricid spectral-sensitivity wanted row; no Lobesia evidence row, no 10090281. Not a repeat.
- Line 10: Dastarcus on main is opsin_sequences_recovered (oa-1:4394 to 4396, retracted in ALL.jsonl); no sense_chemical row, no 0190067. Not a repeat.
- Line 11: no Eptesicus sense_magnetic evidence row and no 0001676 on main. The bat sheet (docs/views/sheets/bat.md:71-72, :165; bat.audit.md:23, :51) carries a "Magnetic compass" row from Holland et al. 2006 Nature (10.1038/444702a), a different paper and a different finding (homing shifted by a shifted field, against magnetite remagnetisation here). Not a repeat; owner question 2.
- Line 12: no Sclomina, Hypolepis or 12110978 on main ("erinacea" hits are other taxa). Not a repeat.

Duplicates 0. Contradictions 0.

## Per-record findings

### Line 7, Triatoma rubida, behaviour_vision, Indacochea et al. 2017

Section 3.3 "Responses to Light", verbatim: "Triatoma rubida adults responded to all wavelengths, including red and yellow." It opens the section. MATCH, whole sentence, 11 words. Next, verbatim: "None of the attraction index means were less than 0.30; they were all greater than the index value of the control trials" / "(mean A.I. = 0.04)." Figure 4 caption, verbatim: "95% confidence intervals of attraction index means of Triatoma rubida males to different light wavelengths." / "Bootstrap analysis reveals that wavelengths of 470 and 390 nm are significantly more attractive than the control" / "(no light) (p > 0.05)." Discussion, verbatim: "Surprisingly, it was found that light of wavelength 351 nm, which is much further in the UV range, was not attractive."; "the diminished attraction of T. rubida to ultraviolet (351 nm) and yellow (591 nm) light"; "The attractive response to white light was present but not formidable." Methods (tool summary): wavelengths 351, 390, 460, 470, 507, 591, 645 nm and white; "wild adult males captured in the field 2 to 3 months before being assayed"; trials in darkness; a wavelength counted as significant only if its bootstrap CI did not overlap the control's.

**Error (null results omitted; value goes past the paper's own test).** By the paper's significance criterion only 470 and 390 nm beat the no-light control; 351, 460, 507, 591, 645 nm and white did not, and the Discussion calls 351 nm not attractive and yellow (591 nm) attraction diminished. The value adds "tested" to "all wavelengths", which the 351 nm result contradicts, and the conditions present 470 and 390 nm as the best of a set that all responded, without saying the rest were not significant. Fixable with the Figure 4 caption as the quote; replacement below.

Uncounted: the males were wild-caught and held 2 to 3 months; the caption prints "p > 0.05" where the criterion is p < 0.05 (as printed; keep and note). Trait key: trap attraction to lit LEDs is a behaviour showing what is seen; behaviour_vision fits. Grade m right.

Line 7: 1 fault.

### Line 8, Cimex lectularius, sense_chemical, Suchy and Lewis 2011

Abstract, verbatim: "Bed bugs demonstrated not simply activation, but attraction to the chemical components of breath." Preceded in the Abstract by "Levels of behavioral activity varied dramatically between bed bugs in the presence and absence of host odor." MATCH, whole sentence, 14 words, where right. Value says no more ("host" breath is the paper's "host odor"). Methods, verbatim: "The host cues were provided in the form of human breath."; "The same experimenter was used for all of the replicates."; "Five, adult bugs of the same sex were removed from the glass container"; "had been starved of blood for three weeks."; "The arena had a square base (91.44 × 91.44 cm)."; "an interval of 5 seconds between every shot". Results, verbatim: "There were no significant differences among genders or attractant status for tortuosity and the number of stops."; "gender is not significant either by itself or as an interaction with the attractant status."; males with breath "showed a significant increase in five of the eight linear walking path parameters" (females similar, tool summary). Discussion, verbatim: "This experiment fails to indicate over exactly what size distance the bed bug may detect a host from breath alone."

**Error (null results omitted; stimulus source misstated).** The conditions omit that tortuosity and number of stops did not differ with breath, that only five of eight linear parameters rose in each sex, and that sex had no effect; and they say the breath source "is not stated", when the paper states human breath from one experimenter for all replicates (a single-donor design). Fixable.

Uncounted: breath also carries CO2 and moisture; "chemical components" are not separated from either (the conditions already say no compound identity). Trait key sense_chemical fits. Grade m right.

Line 8: 1 fault (two parts, one field).

### Line 9, Lobesia botrana, sense_chemical, Pérez-Aparicio et al. 2019

Abstract, verbatim: "The female response to pheromone was lower or not different from that to plant odorants." Preceded by "The male response to the major pheromone component (E7,Z9-12:Ac) was higher than to any other stimuli" (fragment), followed by "Methyl salicylate elicited a higher response in females" / "(E)-β-farnesene elicited a higher response than several other plant odorants in both sexes." MATCH, whole sentence, 15 words. Methods, verbatim: "Six individuals of each sex and host-plant were analysed."; "loaded in 10 µL aliquots of 10 ng/µL of pheromone compounds" / "10 µg/µL of plant compounds"; "The response to n-hexane was subtracted from the response to the test compounds in the same antenna."; "In the rare cases where the subtraction resulted in a negative value, a zero was used." Discussion, verbatim: "none of the pheromone compounds elicited significantly higher responses than n-hexane in females" / "(data not shown, p > 0.05)." Conclusions, verbatim: "Small, but significant pheromone response in females grant future SSR studies". Statistics (tool summary): linear models with emmeans pairwise comparisons; pheromone and plant compounds analysed in separate subsets.

**Error (contrary statement omitted; dose confound not stated).** The conditions give the Discussion's no-difference-from-hexane result for females but not the Conclusions' "small, but significant pheromone response in females", which runs the other way. They also list the two loadings without saying the comparison in the quote sets a 1,000-fold lower pheromone load against the plant compounds, analysed in separate models (no direct test). Fixable.

Uncounted: negative subtraction results were set to zero. Trait key sense_chemical fits. Grade m right.

Line 9: 1 fault.

### Line 10, Dastarcus helophoroides, sense_chemical, Ren et al. 2017

Results, under "EAG responses of D. helophoroides to compounds from cerambycid-attacked trees", verbatim: "The compound (S)-(-)-α-pinene elicited dose-dependent EAG responses down to 10−6 dose in male beetles only." MATCH, whole sentence, 15 words; value says no more. Also verbatim: Abstract "Female and male D. helophoroides exhibited similar EAG and behavioral responses."; "However, female and male beetles did not show any significant sex specific differences between the amplitudes"; "the common plant sesquiterpene trans-β-caryophyllene did not elicit the antennal response at lower doses"; "EAG responses of ten antennae from different adult beetles of each sex were recorded."; "Ascending concentrations of each compound (10−6 to 10−1 in paraffin mg/mg) were applied to avoid olfactory adaptation."; "All EAG responses data were then normalized to cis-3-hexenol (10−3) as follows". The sex-similarity contrary result, the Tukey null and the caryophyllene null are all in the conditions. Grade m right. Trait key fits.

Uncounted: conditions could name the normalisation reference (cis-3-hexenol at 10^-3) and the ascending dose order.

Line 10: 0 counted. Stands.

### Line 11, Eptesicus fuscus, sense_magnetic, Holland et al. 2008

Abstract (single unlabelled paragraph), two consecutive verbatim pieces with no gap: "The results demonstrate that the big brown bat Eptesicus fuscus uses single domain magnetite" / " to detect the Earths magnetic field and the response indicates a polarity based receptor." "Earths" is printed without an apostrophe; "single domain" and "polarity based" unhyphenated. The join is contiguous: MATCH, whole sentence, 28 words. Value paraphrases with hyphens, saying no more. Results, verbatim: "Control bats (Figure 1A) were significantly oriented (Rayleigh test, Z = 7.462, p<0.0001)"; "Bats in the parallel-pulsed group (figure 1B) were also significantly oriented (Rayleigh test, Z = 6.791, p<0.0001)"; "The antiparallel-pulsed group (figure 1C) were not significantly oriented (Rayleigh test, Z = 0.098, p>0.05)."; "if treated as axial (Rayleigh test, Z = 4.912, p<0.005)"; "There was a significant difference in the dispersion of the groups (dispersion test: X2 = 14.74, p<0.001)." Methods (verbatim pieces): control coil currents "set in opposite directions" (the pulser sounds, no magnetic pulse; biasing field on, tool summary); bats "released in a pseudo random order to avoid always releasing one condition first during a release night."; at least one control and two to four bats per night, 24 April to 30 May 2007 (tool summary). No blinding statement found. Per-group n not stated (as the conditions say).

**Error (design controls not stated; qualifying result omitted).** For a magnetic-sense row the conditions must state the controls: they give the three groups but not that controls received a sham pulse (coil currents opposed, pulser sounding, biasing field on), not the pseudo-random release order, and not that blinding of the trackers is unstated. They also omit that the antiparallel group, unoriented as a unimodal sample, was significantly oriented when treated as axial (Z = 4.912, p < 0.005), which bears on how the polarity reading was drawn. Fixable.

Uncounted: the value is the authors' inference from remagnetisation; the conditions already say so. Grade m right. Trait key sense_magnetic fits.

Line 11: 1 fault (two parts, one field).

### Line 12, Sclomina erinacea, sense_chemical, Huang et al. 2021

Section 3.4, verbatim: "To male S. erinacea, nonanal, β-myrcene, and trans-2-hexenal showed significant attractiveness (p < 0.05, Table 4)." MATCH, whole sentence, 16 words; value says no more; where right. Next, verbatim: "As to females, only linalool showed significant attraction (p < 0.05, Table 4)." Table 4 (tool summary of the rows): β-myrcene total 30 vs 18, p = 0.0816, female 15 vs 12, p = 0.5633, male 15 vs 6, p = 0.0459; linalool total 39 vs 15, p = 0.0013, female 23 vs 7, p = 0.0027, male 16 vs 8, p = 0.0992; the nonanal and trans-2-hexenal rows were not returned. Methods, verbatim: "Each compound was tested using at least seven adults of each sex, and each test was repeated three times."; "the position of the experimental group and the control group was also exchanged."; "Another pear-shaped glass bottle holding an agar block containing 5 μL of hexane was used as the control group."; "For each test, 5 μL of the solution (10 μg/μL, 50 μg) was injected into one agar block". EAG, verbatim: "All chemicals except for α-pinene and β-myrcene elicit significantly higher relative responses". The conditions carry the female linalool result, the male linalool null, the total β-myrcene null and the EAG mismatch for β-myrcene. Grade m right. Trait key: a predator's olfactory choice of plant volatiles; sense_chemical fits.

Uncounted: conditions could add the male β-myrcene margin (15 vs 6, p = 0.0459), the 50 μg dose against a hexane arm, and the arm swapping; the note's licence wording (above).

Line 12: 0 counted. Stands.

## Trait key

- Line 7, behaviour_vision: fits (trap attraction to LED light; main uses behaviour_vision in desk-d149 to d170).
- Lines 8, 9, 10, 12, sense_chemical: fit (breath-odour orientation; EAG; olfactometer choice).
- Line 11, sense_magnetic: fits.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 7 | Triatoma rubida, behaviour_vision, all wavelengths | error, fixable | value, quote, where, conditions | Quote MATCH (11 words); only 470 and 390 nm beat the control by the paper's CI test, 351 nm not attractive, so "all wavelengths tested" overstates and the nulls are omitted |
| 8 | Cimex lectularius, sense_chemical, attraction to breath | error, fixable | conditions | Quote MATCH (14 words); tortuosity and stops nulls and sex null omitted; breath source called unstated when it is one experimenter's human breath |
| 9 | Lobesia botrana, sense_chemical, female pheromone EAG | error, fixable | conditions | Quote MATCH (15 words); Conclusions' "small, but significant pheromone response in females" omitted; 1,000-fold dose difference and separate models not stated |
| 10 | Dastarcus helophoroides, sense_chemical, male-only alpha-pinene | stands (uncounted fix) | conditions | Quote MATCH (15 words); sex-similarity and caryophyllene nulls recorded |
| 11 | Eptesicus fuscus, sense_magnetic, magnetite | error, fixable | conditions | Joined quote verified contiguous (28 words); sham, release order and blinding not stated; axial orientation of antiparallel group omitted |
| 12 | Sclomina erinacea, sense_chemical, male Y-tube attraction | stands (uncounted fixes) | conditions, note | Quote MATCH (16 words); female, linalool, total and EAG nulls recorded |

Faults per record: line 7: 1; line 8: 1; line 9: 1; line 10: 0; line 11: 1; line 12: 0. 4 faults in 6 records; 4 of 6 records in error (66.7%): scientific-context 4 (lines 7, 8, 9, 11); duplicates 0; quote-form 0; licence 0; bibliographic 0; name 0; trait key 0; grading 0.

Pooled with audits 172 to 301: 309 of 707 evidence records (43.7%; 305 of 701 before this audit, 4 of 6 here). Audit 302's lines 1 to 6 are not included. No search records.

## Replacement text

Line 7:
- `value`, replace "adults responded to all wavelengths tested, including red and yellow" with "470 and 390 nm significantly more attractive than a no-light control (bootstrap 95% CI)".
- `quote`, replace with "Bootstrap analysis reveals that wavelengths of 470 and 390 nm are significantly more attractive than the control (no light) (p > 0.05)." (22 words, whole caption sentence; "p > 0.05" as printed).
- `where`, replace "Results" with "Figure 4 caption".
- `conditions`, replace "the page-summary tool reports that the Discussion says 351 nm UV light was not attractive, which sits against 'all wavelengths' in the Results sentence (not seen in the Results);" with "wavelengths tested 351, 390, 460, 470, 507, 591 and 645 nm and white light; a wavelength counted as significant only when its bootstrap CI did not overlap the control's, and by that test 351, 460, 507, 591, 645 nm and white were not significantly more attractive than the control; the Results also say every mean A.I. was at least 0.30 against the control's 0.04 ('Triatoma rubida adults responded to all wavelengths, including red and yellow'); the Discussion says 351 nm 'was not attractive' and describes 'the diminished attraction of T. rubida to ultraviolet (351 nm) and yellow (591 nm) light'; the caption's 'p > 0.05' reads as a misprint for p < 0.05;".
- `conditions` (uncounted), replace "adult males only" with "wild adult males caught 2 to 3 months before testing, trials in darkness".

Line 8:
- `conditions`, replace "the source of the breath is not stated in the page-summary read" with "the breath was human breath from one experimenter, the same for all replicates ('The same experimenter was used for all of the replicates'); with breath, five of eight linear walking-path parameters rose significantly in males (females similar); 'There were no significant differences among genders or attractant status for tortuosity and the number of stops', and sex was not significant alone or in interaction with breath".

Line 9:
- `conditions`, append "; the Conclusions instead state 'Small, but significant pheromone response in females grant future SSR studies', against the Discussion's result that no pheromone compound beat n-hexane in females; pheromone compounds were loaded at one thousandth of the plant compounds' concentration (10 ng/uL against 10 ug/uL) and the two sets were analysed in separate models, so the quote's female pheromone versus plant comparison crosses a 1,000-fold dose difference and is not a direct test; negative values after hexane subtraction were set to zero".

Line 10 (uncounted):
- `conditions`, replace "amplitudes are normalised responses in Fig 2 and Table 2, no mV figures were read;" with "amplitudes are responses normalised to cis-3-hexenol (10^-3) in Fig 2 and Table 2, doses given in ascending order, no mV figures were read;".

Line 11:
- `conditions`, append "; controls were placed in the coil with the coil currents set in opposite directions, so the pulser sounded without delivering a magnetic pulse (sham), with the 320 uT biasing field on; bats were released in pseudo-random order, at least one control and two to four bats per night, 24 April to 30 May 2007; the page does not say whether the trackers were blind to treatment; the antiparallel-pulsed group, not oriented as a unimodal sample, was significantly oriented when treated as axial (Rayleigh Z = 4.912, p < 0.005); post hoc, the antiparallel group differed from control and parallel groups, which did not differ from each other".

Line 12 (uncounted):
- `conditions`, append "; males chose beta-myrcene 15 vs 6 (p = 0.0459); each test set 50 ug of compound on agar against a 5 uL hexane control, with the arms exchanged between tests".
- `note`, replace "The MDPI page gives CC BY 3.0;" with "The MDPI page prints no licence line; its metadata rights URL is CC BY 3.0;".

## Owner questions (the unit's, answered where I could)

1. Names not GBIF-checked (API refused to the unit; not tried here): Triatoma rubida and Lobesia botrana are not in gbif-names.tsv; Sclomina erinacea Stål is Harpactorinae, Reduviidae per its mitogenome paper (PMC7706988). Cimex lectularius, Dastarcus helophoroides and Eptesicus fuscus are EXACT ACCEPTED in gbif-names.tsv.
2. New: main's bat sheet carries a magnetic-compass row from Holland et al. 2006 (Nature, 10.1038/444702a) with no evidence row; line 11 would be main's first Eptesicus sense_magnetic evidence. The two papers make different claims (compass from a shifted field against magnetite from a remagnetising pulse); the owner may want the 2006 paper filed too.
3. MDPI CC BY 3.0 page metadata against CC BY 4.0 in Crossref (lines 7, 9, 12): accepted as a version difference, per the caller's rule. Line 8 is CC BY 3.0 in both.
4. Dastarcus (line 10): my read also printed no licence line; Crossref vor CC BY 4.0, PLOS ONE: accepted.
5. Joined quotes: the Eptesicus quote (line 11) is two contiguous pieces of one Abstract sentence, verified. Lines 1 to 6 (Larimichthys, Cyprinus, Hyphantria) are audit 302's.
6. Larimichthys crocea order Acanthuriformes (line 4, audit 302's): consistent with Fishes of the World 5th ed. as cited on Wikipedia's taxobox; Eschmeyer's synonym page names no order.

## Progress note

Accurate on citations, licences and the duplicate checks for lines 7 to 12. Its Records list has 11 bullets for 12 records (the Triatoma bullet covers lines 6 and 7). Its summaries repeat the line 7 overstatement ("adults responded to all wavelengths") and do not carry the other faults found in the conditions.

Verdict: 4 of 6 records in error (66.7%), 4 faults, above the 5% bar; pooled 309 of 707 (43.7%). Error lines: 7, 8, 9 and 11, all fixable with the replacement text above. Lines 10 and 12 can merge, with the uncounted fixes.

This report is model output and carries no authority.
