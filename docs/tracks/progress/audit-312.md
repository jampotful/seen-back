# audit-312: desk-d224, evidence lines 1 to 5

Audited 31 October 2026 from the desk-d224 files present untracked in the worktree (docs/tracks/progress/desk-d224.md and docs/views/evidence/desk-d224.jsonl, 9 lines; neither committed here, neither edited). HEAD 785f8504 (desk-d223). This audit judges lines 1 to 5 only; audit 313 judges lines 6 to 9. `tools/senses/check.py` on the evidence file: 9 records, 0 problems. Quote lengths (`len(q.split())`) for lines 1 to 5: 17, 17, 17, 18, 14, all within 40. The unit has evidence records only, so the brief's search-record and plant-screening parts do not apply; audits 310 and 311 are the format model.

Sources opened (WebFetch): www.mdpi.com/2075-4450/11/7/423 (four passes), frontiersinzoology.biomedcentral.com/articles/10.1186/1742-9994-7-8 (three passes), www.mdpi.com/2075-4450/13/7/655 (three passes), api.crossref.org/works for the three DOIs (insects13070655 opened on the /v1/ path after two client errors). Names: main's docs/views/gaps/gbif-names.tsv and the GBIF result "Xyleborus affinis Eichhoff, 1868" (gbif.org/species/5020985) returned by my WebSearch. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 1 WebSearch and 13 WebFetch calls used.

## Bibliographic and licence

- Lines 1 to 3, Stukenberg et al. 2020, Crossref: Niklas Stukenberg, Markus Pietruska, Axel Waldherr, Rainer Meyhöfer, in the recorded order; title verbatim; Insects 11(7), 423, issued 2020-07-09; licence CC BY 4.0, content-version vor; relation empty. MDPI page metadata gives CC BY 3.0. Met; page CC BY 3.0 against Crossref CC BY 4.0 vor accepted as in earlier MDPI rulings.
- Line 4, Haug, Biehlmaier, Mueller, Neuhauss 2010, Crossref: Marion F Haug, Oliver Biehlmaier, Kaspar P Mueller, Stephan CF Neuhauss, in order; title "Visual acuity in larval zebrafish: behavior and histology" verbatim; Frontiers in Zoology 7(1), 8, issued 2010-03-01; no licence field; relation empty. Met.
- Line 5, Romero et al. 2022, Crossref: seven authors Patricia Romero to Larissa Guillén in the recorded order; title verbatim (three verified segments); Insects 13(7), 655, issued 2022-07-21; CC BY 4.0, vor; relation empty. Page licence URL CC BY 3.0. Met.

Ruling on the unit's question (Danio rerio licence on the page statement alone, no Crossref CC tag): acceptable. The BMC page, which is the publisher's version of record and the exact copy read, prints verbatim "Open Access This article is published under license to BioMed Central Ltd." and "This is an Open Access article is distributed under the terms of the Creative Commons Attribution License ( )," followed by "which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited." Under audits 307/308/310/311 the page's printed Creative Commons statement on the copy read is sufficient by itself; the Crossref vor tag is an alternative route, not an extra requirement. Missing Crossref licence metadata is common for 2010 BMC deposits and does not undercut the printed statement. The empty link means the CC BY version is not stated; the note should say "Creative Commons Attribution License, version not stated on the page" (uncounted).

Bibliographic faults 0; licence faults 0. source.access "open" right on all five.

## Names

- Frankliniella occidentalis: main gbif-names.tsv:1904 "Frankliniella occidentalis EXACT ACCEPTED"; main's three rows (audit/corrected/methods.jsonl:696 to 698) use Thripidae, Thysanoptera. Right.
- Danio rerio: main gbif-names.tsv "Danio rerio EXACT ACCEPTED" (as audit 275); main uses Cyprinidae, Cypriniformes (audit/corrected/fish-shark.jsonl:116). Right.
- Xyleborus affinis: GBIF 5020985 "Xyleborus affinis Eichhoff, 1868" (search result title); no Xyleborus on main; main files Scolytinae (Dendroctonus pseudotsugae, Hypothenemus hampei, Ips paraconfusus) under Curculionidae, as here and as the paper's title "(Coleoptera: Curculionidae: Scolytinae)". Right.

Name faults 0.

## Duplicates

git grep on origin/main across the whole docs/ tree (evidence, audit/corrected, audit/ALL.jsonl, audit/*.jsonl, recheck, searched, sheets, gaps, wanted, codex-findings, progress notes, desk-queue) for "Frankliniella", "insects11070423", "Stukenberg", "Danio", "zebrafish", "1742-9994-7-8", "Haug", "Neuhauss", "Xyleborus", "insects13070655".

- None of the three DOIs is on main. "Haug" hits on main are other authors (fungus, reptile and wanted rows), not this paper.
- Frankliniella occidentalis on main: audit/corrected/methods.jsonl:696 to 698 and audit/ALL.jsonl:3159 to 3161, lambda_max_nm 363, 476, 535 from a spectral-sensitivity review; no behaviour_vision row. Not a repeat, no contradiction.
- Danio rerio acuity_cpd on main: audit/corrected/fish-shark.jsonl:116 (Tappeiner et al. 2012, Frontiers in Zoology 9: 10, adult zebrafish, OKR, 0.56 to 0.58 c/d); canon-5.jsonl:189 and oa-1.jsonl:4000 to 4001 (Caves et al. 2024 compilation, 0.59 behavioural, 1.89 RGC). No larval acuity row, no 0.16 cpd anywhere on main; desk-d191 and desk-d143 larval rows are UV avoidance, airflow and magnetic. Not a repeat, no contradiction (larval 0.16 below adult 0.56 to 0.59 is the expected direction). Uncounted: the record's note names only jeb.246063 as main's adult value and misses the original adult measurement in audit/corrected/fish-shark.jsonl:116; see replacement text.
- Xyleborus: nothing on main.
- Lines 1, 2 and 3 share one paper but log different findings (overall ranking from the abstract; mixture inhibition; red lowest in the six-colour experiment). Line 1's conditions already carry line 3's red sentence, so line 3 adds a separately quoted result rather than a new one; not counted as a duplicate.

Duplicates 0; contradictions 0.

## Per-record findings

### Line 1, Frankliniella occidentalis, behaviour_vision, blue most attractive, then green, UV moderate

Abstract, verbatim: "Blue LEDs were most attractive, followed by green, while only a moderate attractiveness of UV was observed." MATCH, whole sentence, 17 words. The value says no more than the quote. Grade m right. Carried items verified: 1 x 1 x 0.8 m cage ("A flight cage with a base area of 1 × 1 m and a height of 0.8 m served as the arena."), 0.7 m release distance, 30 min ("Experiments were terminated after 30 min ..."), 20 and 10 replicates (Section 2.6), order randomised, about 80% females, bean plants, 23 °C, strain not stated, no blank trap, recapture 85.76%, the red sentence.

**Error (contrary result in the main experiment, ambient light and intensity omitted).** (a) In the six-colour experiment the paper prints "The result showed a strong significant preference of F. occidentalis for Blue2 (55%)" and "UVA1 (8%) and Green1 (11%) were the second most attractive after Blue2, but did not differ in their attractiveness." So in that test green did not rank above UV; the abstract's "followed by green" is not supported by it, and the record carries neither the 55% figure nor the green-equals-UV result. (b) Traps were "adjusted to the intensity of the color trap Cyan (41.2 µmol m−2 s−1)", and the cage roof let in fluorescent-tube light: "the visible light (45 µmol m−2 s−1 on average) and UVA radiation (2 µmol m−2 s−1 on average) emitted by the fluorescent tubes could enter the cage." Trap light was therefore presented against an ambient visible level slightly higher than each trap's own output; neither number is carried. (c) "at least 120" in Section 2.1 is the number collected per trial; the number released is "approx. 120 adult thrips" (Section 2.4). (d) The blue LED: Section 3.2 prints "567 nm (Blue2)" once while the Discussion and the Blue1 (452 nm) versus Blue2 comparison give 467 nm; 467 nm is right (a 567 nm peak lies in the green-yellow range and could not be called Blue2), so the record can name Blue2 at 467 nm and flag the misprint instead of leaving the wavelength out. Fixable.

Line 1: 1 record in error.

### Line 2, Frankliniella occidentalis, behaviour_vision, blue-green mixture less attractive than either component

Abstract, verbatim: "When light from blue and green LEDs was mixed, the attractiveness decreased compared to its single components." MATCH, whole sentence, 17 words. Grade m right. Carried items verified: below 10% ("the attractiveness dropped below 10% when blue and green LEDs were combined"), doubled intensity ("Even with doubling of the light intensity, the attractiveness remained at the low level").

**Error (qualifier from the graded-mixture series omitted; replicate numbers wrong for this test; ambient light omitted).** (a) Results 3.3 print "already 25% of blue light resulted in a 3-fold reduction in attractiveness" and "With increasing the contribution of the blue light to 75%, the attractiveness was similar to green" "but still significantly lower compared to blue only". At 75% blue the mixture was not below green, so "lowered attractiveness compared with either single component" holds for the equal mixtures, not for every proportion tested. (b) The record gives "20 replicates for the main multiple-choice tests and 10 for dual-choice tests", but the mixture experiments are in Section 2.7: "The first experiment was replicated 20 times, the second one 12 times, and the third one 15 times." The Figure 8 legend gives n = 18 for one of them, against the Methods (tool summary). (c) Same ambient fluorescent light (about 45 visible, 2 UVA µmol m−2 s−1) and 41.2 µmol m−2 s−1 trap intensity as line 1, not carried. Fixable.

Line 2: 1 record in error.

### Line 3, Frankliniella occidentalis, behaviour_vision, red least attractive (1%)

Section 3.1, "Attractiveness of Different Wavelengths from the Ultraviolet to the Visible Spectral Range (307–635 nm)". The page's sentence ends, verbatim, " colors (1%, p < 0.01) (Figure 3)." The record's quote stops at "(1%, p < 0.01)." and drops the trailing "(Figure 3)" without marking the cut.

**Error (quote form: trailing figure reference cut unmarked; ambient light and experiment set omitted).** (a) QUOTE RULE: cuts must be marked, including trailing figure references; the quote should carry "(Figure 3)" or mark its removal. (b) The record does not say which LEDs this experiment offered (UVA1, Blue2, Cyan, Green1, Yellow2, Red, tool summary), so "least attractive of the colours tested" has no stated comparison set; the share was 1% of recaptured thrips against Blue2 55%, Green1 11%, UVA1 8%. (c) Ambient fluorescent light and trap intensity as line 1. Fixable.

Line 3: 1 record in error.

### Line 4, Danio rerio, acuity_cpd, 0.16 cpd at 5 dpf

Verbatim on the page: "Visual acuity of 5 day old larval zebrafish was determined to be 0.16 cpd, or about 3.1 degrees." MATCH, whole sentence, 18 words. The next sentence gives the histological limit of 0.24 cpd (tool summary). Carried items verified: 90% contrast, "Varying spatial frequencies were presented with a constant angular velocity of 7.5 degrees per second.", OKR, "The wild-type strain used for larval behavioral and histological analysis was Tübingen (Tü).", n = 41 ("At a given optimal contrast of 90% all zebrafish larvae (n = 41) follow the stripes best at 0.04 cpd"), "Embryos were raised at 28°C in E3 medium", light level only as photopic and rod-saturating, 0.871 cpd adult calculation ("For comparison we subjected the adult retina to a similar analysis."). Units fit. Grade m right. The `where` "Conclusions" could not be confirmed: the fetch tool returned no top-level headings for this page at all (no Background, Results or Discussion either), and places the sentence in the closing unlabelled paragraph; not counted.

**Error (cut-off rule misdescribed, conflicting sample size and other ages omitted, preparation omitted).** (a) The method says the cut-off was "taken where eye movement no longer differed significantly from the 0.2 cpd baseline". The paper's 0.16 cpd is the finest grating that still differed from the 0.2 cpd value (set as zero) in a paired one-tailed t-test, p = 0.0055, while 0.17 cpd did not (p = 0.1557) (tool summary of the statistics); as written the rule points to 0.17. (b) The age comparison prints "We compared larvae at 4 (n = 59), 5 (n = 74) and 6 (n = 65) dpf" and "A two-way ANOVA for repeated measurements revealed no significant dependence on age ([F (df = 2) = 2.014; p = 0.161])." So 5 dpf has two sample sizes on the page (41 and 74), and acuity did not change from 4 to 6 dpf (values "data not shown"); neither is carried. (c) Larvae were placed in 3% pre-warmed methylcellulose in a 35 mm dish with sine-wave gratings from a projector (tool summary); not carried. Uncounted: the Discussion cites an external 7 to 9 dpf value of 0.175 cpd. Fixable.

Line 4: 1 record in error.

### Line 5, Xyleborus affinis, sense_chemical, 70% ethanol strongest EAG response

Section 3.1, "EAG responses of Wild and Laboratory-Reared Insects", verbatim: "In both X. affinis and X. ferrugineus, 70% ethanol elicited the strongest antennal responses." The last 50 characters returned, "ethanol elicited the strongest antennal responses.", with no figure reference inside the sentence. MATCH, whole sentence, 14 words. The Conclusions do not repeat it verbatim ("Ethanol vapor triggered the largest amplitude EAG responses in both X. affinis and X. ferrugineus."); the note's "also repeated in Conclusions" should say "restated" (uncounted). Two records from one two-species sentence: right under audits 299/300, since each record states its own species' half and the value is X. affinis's own; a genus-level record would lose information. Grade m right (X. affinis females measured). Carried items verified: females only, flight-caught at Los Tuxtlas, Veracruz, "Three and four generations of X. affinis and X. ferrugineus, respectively" (three is right for X. affinis), Platanus mexicana sawdust, 4 mL headspace, 400 mL/min, empty jar and air negative controls, randomised sequence, "A mean (+ S.E.) of 12 ± 2 beetles was tested for each bark aging period (2, 24, and 48 h; n = 36 ± 6)", three occasions, 108 ± 18 per origin.

**Error (no test behind "strongest" stated, origin effect and stimulus amounts omitted).** (a) The record says "the text reports test statistics and amplitudes appear only in a figure". The Results print no comparison of ethanol against bark odours in X. affinis; ethanol entered a Gaussian GLM with the three ageing times (tool summary), and "strongest" is read from Figure 1. The record should say no pairwise ethanol-versus-bark statistic is printed for X. affinis. (b) In X. affinis, wild and laboratory-reared females differed to bark of B. simaruba (t = −5.70, df = 565, p < 0.001) and P. schiedeana (t = −4.00, df = 565, p = 0.001), and "In X. affinis, the insect origin and odor (volatilomes used as stimuli) treatments generated different EAG responses."; no origin statistic is printed for X. affinis ethanol. Not carried. (c) Stimuli: "A jar with 15 mL of 70% ethanol was used as a positive control for EAG tests." against "a 15 g sample of grated bark was placed in a 250 mL glass jar", jars held "at 27 ± 1 °C and 60 ± 5% R.H. for 2 h", the air response subtracted from each replicate and values log+1 transformed; recording temperature not stated. Not carried. Uncounted: Table 1's caption calls the analysis a linear mixed model, against the GLM in Methods. Fixable.

Line 5: 1 record in error.

## Trait key

- Lines 1, 2, 3, behaviour_vision: fit (flight choice of whole living thrips among LED traps).
- Line 4, acuity_cpd: fits (behavioural OKR grating cut-off of one named species and stage).
- Line 5, sense_chemical: fits (EAG of living females to volatiles).

Trait key faults 0.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Frankliniella occidentalis, behaviour_vision, blue > green, UV moderate | error, fixable | conditions | Quote MATCH; in the six-colour test Green1 (11%) and UVA1 (8%) did not differ, Blue2 55%; ambient fluorescent light (45 visible, 2 UVA) vs 41.2 µmol trap intensity omitted; released number is approx. 120 |
| 2 | Frankliniella occidentalis, behaviour_vision, blue-green mixture inhibition | error, fixable | conditions | Quote MATCH; 75% blue mixture similar to green omitted; mixture replicates were 20, 12, 15 (Fig 8 n = 18), not 20/10; ambient light omitted |
| 3 | Frankliniella occidentalis, behaviour_vision, red lowest (1%) | error, fixable | quote, conditions | Trailing "(Figure 3)" cut unmarked; comparison set and shares not stated; ambient light omitted |
| 4 | Danio rerio, acuity_cpd, 0.16 cpd at 5 dpf | error, fixable | method, conditions | Quote MATCH; cut-off rule misdescribed (0.16 is the last frequency that differed, p = 0.0055; 0.17 did not); n = 41 vs 74 and no age effect 4 to 6 dpf omitted; methylcellulose preparation omitted |
| 5 | Xyleborus affinis, sense_chemical, 70% ethanol strongest EAG | error, fixable | conditions | Quote MATCH; no ethanol-vs-bark statistic printed yet record implies tests; X. affinis origin effect on bark and stimulus amounts omitted |

5 of 5 records in error (100.0%): scientific-context 5 (lines 1, 2, 3, 4, 5); quote-form 1 (line 3, also counted in its record); value beyond quote 0; duplicates 0; bibliographic 0; names 0; licence 0; trait key 0; grading 0.

Pooled with audits 172 to 311: 354 of 758 evidence records (46.7%; 349 of 753 before this audit, 5 of 5 here). Audit 313's lines 6 to 9 are not included. No search records.

## Replacement text

Lines 1, 2 and 3 (same paper), in `conditions`:
- replace "at least 120 lab-reared freshly emerged thrips of mixed sex (about 80% females) per replicate" with "approx. 120 lab-reared freshly emerged adult thrips of mixed sex (about 80% females) released per replicate (at least 120 collected)".
- replace "LEDs adjusted to equal intensity (umol m-2 s-1) except in the blue-green mixtures" with "LEDs adjusted to the intensity of the Cyan trap (41.2 umol m-2 s-1) except in the blue-green mixtures; the cage roof admitted fluorescent-tube light of about 45 umol m-2 s-1 visible and 2 umol m-2 s-1 UVA on average, so traps were seen against ambient light of similar intensity; choice tests at 23 C, 65% RH".
- replace "the printed text gives one blue LED as 567 nm in section 3.2 and 467 nm elsewhere, so no blue peak wavelength is claimed in this record" with "the blue LED Blue2 peaks at 467 nm (printed once as 567 nm in section 3.2, a misprint: it is compared there with Blue1 at 452 nm and given as 467 nm in the Discussion)".

Line 1, `conditions`: append "; in the six-colour experiment (UVA1, Blue2, Cyan, Green1, Yellow2, Red) Blue2 took 55% (p < 0.0001), and UVA1 (8%) and Green1 (11%) were second but did not differ from each other, so green ranked above UV only in other experiments".

Line 2, `conditions`: replace "20 replicates for the main multiple-choice tests and 10 for dual-choice tests;" with "the three mixture experiments were replicated 20, 12 and 15 times (Figure 8 legend gives n = 18 for one, against the Methods);" and append "; 25% blue in green cut attractiveness about threefold, and at 75% blue the mixture was similar to green alone but still significantly lower than blue alone, so the mixture fell below both components only at the lower blue proportions and equal mixtures".

Line 3:
- `quote`: replace with "The attractiveness of Red was significantly the lowest compared to all other colors (1%, p < 0.01) (Figure 3)." (19 words).
- `conditions`: append "; red 1% is from the six-colour experiment of section 3.1 (UVA1, Blue2, Cyan, Green1, Yellow2, Red), against Blue2 55%, Green1 11% and UVA1 8%".

Line 4:
- `method`: replace "cut-off taken where eye movement no longer differed significantly from the 0.2 cpd baseline" with "eye velocity at each spatial frequency compared with the 0.2 cpd value set as zero (paired one-tailed t-test); 0.16 cpd was the finest grating still differing (p = 0.0055), 0.17 cpd did not (p = 0.1557); larvae in 3% methylcellulose in a 35 mm dish, sine-wave gratings projected".
- `conditions`: replace "n = 41 larvae for the 5 dpf measurement" with "n = 41 larvae for the 5 dpf cut-off measurement (the age comparison gives n = 74 at 5 dpf); larvae at 4 (n = 59) and 6 (n = 65) dpf did not differ from 5 dpf (two-way repeated-measures ANOVA, p = 0.161; values not shown)".
- `note` (uncounted): replace "adult zebrafish acuity on main is a different paper (jeb.246063)" with "adult zebrafish acuity on main is Tappeiner et al. 2012 (audit/corrected/fish-shark.jsonl:116, 0.56 to 0.58 c/d) and the Caves et al. compilation (jeb.246063)"; and replace "naming the Creative Commons Attribution License, but its link text came back empty" with "naming the Creative Commons Attribution License (version not stated; link text empty)".

Line 5, `conditions`:
- replace "the text reports test statistics and amplitudes appear only in a figure" with "no pairwise statistic comparing ethanol with bark odours is printed for X. affinis (ethanol entered a Gaussian GLM with the three ageing times; Table 1 calls it a linear mixed model), so 'strongest' is read from Figure 1, where amplitudes appear".
- append "; in X. affinis wild and laboratory-reared females differed to B. simaruba (t = -5.70, df = 565, p < 0.001) and P. schiedeana bark (t = -4.00, df = 565, p = 0.001), with no origin statistic printed for ethanol; stimuli were 15 mL of 70% ethanol versus 15 g of grated bark per 250 mL jar, jars held at 27 +/- 1 C and 60 +/- 5% RH for 2 h; the air response was subtracted from each replicate and values log+1 transformed; recording temperature not stated; laboratory X. affinis were 3 generations (X. ferrugineus 4)".
- `note` (uncounted): replace "(also repeated in Conclusions)" with "(restated in Conclusions in other words)".

## Owner questions (the unit's, answered for lines 1 to 5)

1. Danio rerio licence on the page statement alone: acceptable (ruling above). The BMC version-of-record page prints the Creative Commons Attribution License statement; no Crossref tag is needed when the page statement is read on the exact copy.
2. Frankliniella blue LED 567 versus 467 nm: 467 nm is right and 567 nm in section 3.2 is a misprint. The records should name Blue2 at 467 nm and flag the misprint (replacement above) rather than omit the wavelength.
3. Xyleborus two-species sentence: one record per species is right (audits 299/300); do not merge into a genus-level record. Line 5 states X. affinis's half; line 6 is audit 313's.
4. Frankliniella on main under lambda_max_nm (review rows, methods.jsonl:696 to 698): no overlap by paper or trait; confirmed.

## Progress note

Accurate on citations, licences, names and duplicates, and the Xyleborus split follows precedent. The Records list carries the abstract's "then green" ranking without the six-colour result where green and UV tied, the mixture inhibition without the 75% blue exception, and the zebrafish value without the 4 to 6 dpf null age effect. The 467/567 nm misprint was found but left unresolved.

Verdict: 5 of 5 judged records (lines 1 to 5) in error (100.0%), above the 5% bar. Error lines: 1, 2, 3, 4 and 5, all fixable with the replacement text above. Pooled 354 of 758 (46.7%).

This report is model output and carries no authority.
