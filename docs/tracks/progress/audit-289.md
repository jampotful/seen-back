# audit-289: desk-d205 (6 evidence records, no search records, no wanted lines)

Audited 31 October 2026 from the desk-d205 files present untracked in the worktree (docs/tracks/progress/desk-d205.md and 6 evidence lines in docs/views/evidence/desk-d205.jsonl; neither committed here, neither edited). HEAD 871fbf20 equals origin/main and already holds desk-d204. `tools/senses/check.py` on the evidence file: 6 records, 0 problems. Quote lengths (`len(q.split())`): 18, 15, 28, 29, 34, 30, all within 40. No searched or wanted file, so every record was judged and there is no sample to draw. Rules applied: oa-audit.md "Scientific context and counting (29 October 2026)", oa-read.md and BRIEF (whole sentence, 40 words, grade, `partial`), desk-audit.md (no 125-character limit) and the publisher-copy licence rule with the owner's ruling that CC BY-NC is accepted when it is on the exact copy read and CC BY-NC-ND is held out; the shared brief's plant-screening items are superseded for this animal unit. Duplicates checked with git grep on origin/main across docs/views (evidence, audit including corrected/ and ALL.jsonl, searched, wanted, gaps), views/, src/ and docs/tracks for "Dendrobaena", "1202410", "carbon dioxide detection", "Tiliqua", "adelaidensis", "pygmy blue", "ZO20064", "Daniell", "predator scent", "Recognition of reptile", "Echinotriton", "Tylototriton", "chinhaiensis", "Chinhai", "spiny newt", "16020261" and "Avoidance Behavior in Chinhai", every trait included, and the notes and conditions of the main rows found. 2 WebSearch and 7 WebFetch calls used.

Sources opened: api.crossref.org/works/10.1071/ZO20064 and /10.3390/ANI16020261 (answered, none robots_disallowed; Smith et al. was not refetched, audit 288 read its Crossref record today); publish.csiro.au/zo/fulltext/ZO20064 (two passes); www.mdpi.com/2076-2615/16/2/261 (two passes); for names amphibiansoftheworld.amnh.org (Echinotriton chinhaiensis account) and reptile-database.reptarium.cz/Tiliqua/adelaidensis, both returned by my WebSearches. The Smith et al. text was not reopened: its two records are judged against desk-d204 lines 2 and 3 on main and audit 288's reading of the same paper. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries, so quotes were checked as MATCH/MISMATCH; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification.

## Bibliographic and licence

- Smith et al. 2023 (lines 1, 2): authors, title, Frontiers in Ecology and Evolution 11, article 1202410, 2023, CC BY 4.0, as recorded and as audit 288 read on Crossref. Moot (both lines dropped as repeats).
- Daniell et al. (line 3), fresh Crossref: Tara L. Daniell, Mark N. Hutchinson, Phil Ainsley, Michael G. Gardner, in the recorded order; title "Recognition of reptile predator scent is innate in an endangered lizard species" verbatim; Australian Journal of Zoology 68(2): 76-84; issued and online 2021-06-09, print 2021-06-22; so year 2021 is right (the CSIRO page's "Journal Compilation © CSIRO 2020" is the volume's compilation year). Licence entry: by-nc-nd/4.0, content-version vor, start 2025-05-26 (delay 1447 days); relation empty; no update-to.
- Feng et al. 2026 (lines 4 to 6), fresh Crossref: Shiyan Feng, Wei Li, Di An, Zhiya Ma, Zhenhua Luo, Aichun Xu, in order; title verbatim as recorded; Animals 16(2), article 261; issued and online 2026-01-15; CC BY 4.0 (vor); relation empty; no update-to.

Licence on the copy read:
- Line 3: the CSIRO full-text page reads "Journal Compilation © CSIRO 2020 Open Access CC BY-NC". The exact copy read carries CC BY-NC, so the owner's CC BY-NC rule applies and the licence is met. Crossref's CC BY-NC-ND registration (from 2025-05-26) is metadata about the version of record, not the licence printed on the copy read; the NC-ND hold-out rule would apply only if the copy read said NC-ND. Not counted. Uncounted: the note should record the discrepancy so a later reader is not surprised (replacement below).
- Lines 4 to 6: MDPI footer "This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license."; page metadata CC BY 3.0, the site-wide tag audits 276 and 287 noted. Met.

Bibliographic faults 0; licence faults 0.

## Names

- Tiliqua adelaidensis (line 3): Reptile Database gives "Tiliqua adelaidensis (PETERS, 1863)", Scincidae, Egerniinae (Tiliquini), original combination Cyclodus adelaidensis. Accepted. Not in docs/views/gaps/gbif-names.tsv (only Tiliqua rugosa is); owner question below. The progress note raises this only for Echinotriton.
- Echinotriton chinhaiensis (lines 4 to 6): Amphibian Species of the World titles the account "Echinotriton chinhaiensis (Chang, 1932)", original combination Tylototriton chinhaiensis Chang, 1932, with past placements in Tylototriton (Echinotriton) and Pleurodeles (tool summary). Accepted. Not in gbif-names.tsv; owner question below.
- Dendrobaena veneta (lines 1, 2): moot (dropped); the name question is audit 288's owner question 1, still open.

Name faults 0; 2 names outside gbif-names.tsv (owner questions).

## Duplicates

- **Line 1 repeats desk-d204:2 on main.** Same species, same trait (sense_chemical), same paper and DOI, same section ("Results, CO2 aversion"), same experiment (exudate assay across 0, 25, 50, 75, 100% CO2). The d205 value, the dose-dependent rise with "p<0.0001, n=12-20", is carried in d204:2's `conditions` ("dose-dependent rise across the series (n = 12-20 per the Results, p < 0.0001)"), together with the 25% null, the one-way/two-way ANOVA inconsistency and the water-rinse result that line 1 also lists. Only the quote sentence differs (the adjacent sentence of the same paragraph). A finding carried in a main row's conditions is a repeat. Drop.
- **Line 2 repeats desk-d204:3 on main.** Same species, trait, paper, section ("Results, Pharmacology") and the identical quote, "The broad-spectrum CA inhibitor acetazolamide significantly muted the response to CO2 (Figure 7A, p<0.01, n=8-13).", with the same value. Drop. Line 2's `conditions` lists further blocker results (indisulam 0.01 mM reduced the response; U-104, S4, topiramate, methylene blue, HC030013 and ZnCl2 did not). These were not verified here; d204:3's conditions name indisulam among the blockers that reduced the response but not the nulls. If wanted, they belong in a correction to d204:3 after a reading, not in a new row.
- Tiliqua adelaidensis: no row on main under any trait; Tiliqua rows on main are T. rugosa (eye and opsin traits, other papers). Not a repeat.
- Echinotriton and the Feng et al. DOI and title: none on main. Not a repeat.
- Lines 4 to 6 against each other: three findings from two experiments (visual GEE main effect; chemical activity; chemical GEE null). Not one finding twice.

The progress note's statement that Dendrobaena "had no rows (grep of docs/views ... before filing)" is wrong for the tree this unit lands on: desk-d204 merged the same paper and both findings.

Duplicates 2 (lines 1, 2). Contradictions 0.

## Per-paper findings

### Daniell et al. 2021, Tiliqua adelaidensis (line 3)

Results, "Differential response to scent treatments (Aims 1 and 2)", verbatim in chunks: "The number of tongue flicks lizards directed towards scent papers differed significantly among scent treatments" "(Table 1, Fig. 1)."; means: brown snake 24.07 ± 4.93 s.e., bluetongue 14.33 ± 2.83, Rosenberg's monitor 12.81 ± 4.04, novel control 5.81 ± 1.73, water 5.42 ± 1.59; then the quoted sentence; then "There was no significant difference among other treatments." Methods: "three treatments groups, namely, wild lizards, wild-born captive lizards and captive-born lizards"; 37 captive lizards at Monarto Safari Park ("nine potentially predator-experienced wild-born adults", "28 predator-naive captive-born offspring"); "The wild population for this study (20 lizards), was located at Tiliqua Reserve, a Nature Foundation property ~10 km from Burra"; "One paddock of the site was searched to locate 20 natural burrows."; "Scent papers were placed approximately 5 cm from lizard burrows and pinned down with nails to hold in place."; captive enclosures had "six artificial burrows per section"; scent towels left "in reptile enclosures for 48 h", frozen at -20°C, "Storage time between scent collection and trials did not exceed 3 weeks."; "Scent was collected from one eastern brown snake only."; monitor and bluetongue samples "likely to be mixtures of different individuals"; controls "1:10 diluted eucalyptus oil" and "an odourless distilled-water control"; "Scent trials were conducted over a 5-day period at both Monarto and Burra."; "The order of scent presentation was randomised among lizards."; "Lizards were filmed for 30 min, after a 30-min acclimation period after camera setup"; 16.8 to 30.1°C, no rain; repeated-measures PERMANOVA, temperature as covariate; temperature had a significant effect on tongue flicks (tool summary); "The number of tongue flicks varied among lizard origin and day but the variation was not significant."; no effect of treatment, origin or day on basking, but a significant origin by day interaction on basking; ethics approval 28/2017, no health statement.

Quote. MATCH, whole sentence, 28 words, one section, no cuts; contains the value; the value says no more. Quote-form 0.

Line 3. Counted (scientific context, who was exposed to what; fixable). `conditions` says the scent paper was "placed in the lizard's enclosure". That holds for the 37 captive lizards only. The 20 wild lizards were tested in the field at Tiliqua Reserve: the paper was pinned about 5 cm from each lizard's natural burrow. All lizards were scored at their burrows, not in an open enclosure, and a third of the sample was tested in the wild. Grade m right; `partial` false right; trait sense_chemical right (a living response to a chemical cue). Uncounted: give the means (brown snake 24.07 against water 5.42 tongue flicks), say the bluetongue and monitor scents did not differ from the controls (which the title's "reptile predator scent" outruns: only the snake scent differed), and that temperature had a significant effect on tongue flicks.

### Feng et al. 2026, Echinotriton chinhaiensis (lines 4 to 6)

Results 3.1.1, verbatim in chunks: "Based on the results of the Generalized Estimating Equation (GEE) model (Table 2)," "the between-group main effect was significant (β = 0.164, Wald χ2 = 6.416, p = 0.011)."; interaction "at 4 min" "(β = 0.182, Wald χ2 = 8.363, p = 0.018) and 6 min (β = 0.177, Wald χ2 = 4.167 p = 0.041)"; Table 2 gives β = 0.233, p = 0.004 for 4 min (tool summary). 3.1.2: visual-cue crossings 4.167 ± 2.718 against control 5.333 ± 2.551, "significantly reduced the activity level of larvae (V = 288, p = 0.017; Figure 3)". 3.2.1: "the main effect of group was not significant" "(β = 0.188, Wald χ2 = 1.608, p = 0.205)."; interaction significant at 6 min only "(β = −0.302, Wald χ2 = 4.117, p = 0.042)". 3.2.2: the quoted sentence, then Wilcoxon signed-rank "(V = 314, p < 0.001, Figure 5)". Methods: eggs from the Chinhai Spiny Newt Nature Conservation Area, April to May 2024; larvae never exposed to predators; stage at testing not stated; large bullfrogs 258.26 ± 19.70 g, small 13.93 ± 1.80 g, bought from local shops; tank 60 × 30 × 10 cm, about 4.5 cm water; "high-transparency acrylic panels" for the visual test, "perforated acrylic partitions with a pore size of 2 mm" for the chemical test; 48 h leak check; cue water from "Four healthy adult bullfrogs" kept "in 1 L of sun-exposed water for 24 h", filtered, 30 mL injected; controls: no bullfrog (visual), 30 mL plain water (chemical); 5 min acclimation; counts at 2, 4, 6, 8, 10 min; 30 replicates. On who was exposed to what: visual test, "the same five larvae in the central compartment were retained for the subsequent visual recognition experiment"; chemical test, "After the control experiment, the same five larvae were retained", with "five new larvae" for each replicate; the activity test is a Wilcoxon signed-rank (paired) test.

Quotes. Line 4 MATCH, whole sentence (the next printed sentence begins "Indicating that ..."), 29 words. Line 5 MATCH, whole sentence, 34 words. Line 6 MATCH, whole sentence, 30 words. Each contains its value and the value says no more. Quote-form 0. Trait keys: line 4 behaviour_vision fits (a behavioural response to a predator seen through a sealed clear panel, leak-checked for 48 h); lines 5 and 6 sense_chemical fit (living responses to a waterborne cue). Grade m right; `partial` false right.

Lines 4, 5, 6. Counted on each (scientific context, design; fixable). `conditions` on all three says "30 replicates of 5 larvae per group", which reads as independent control and treatment groups. The paper ran each set of five larvae first as its own control and then, the same five retained, with the bullfrog or its odour: a within-subject design with control always first, which is why the activity test is a signed-rank test. A reader of the rows cannot see that the cue effect is confounded with trial order (second exposure to the tank) and that the "groups" are the same animals. Line 4 also says the group-by-time interaction is significant "from 4 min"; the text reports it at 4 and 6 min only.

Uncounted: line 4 could add that the visual cue also lowered activity (4.167 ± 2.718 against 5.333 ± 2.551 crossings, V = 288, p = 0.017); line 5's `units` should say the count is of all five larvae together; whether ± is SD or SE is not stated in the passages read; the bullfrog is the American bullfrog (Lithobates catesbeianus), an introduced predator in the newt's range, as the title's "novel" implies.

### Smith et al. 2023, Dendrobaena veneta (lines 1, 2)

Not re-read; judged as repeats of main (above). Whether exudate output counts as sense_chemical is moot here; on main the owner's ruling (living responses to chemical cues count, the proxy noted) is met by d204's note "Exudate release is the authors' proxy for aversion".

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Dendrobaena veneta, exudate rose dose-dependently with CO2 | drop | whole record | Repeat of desk-d204:2 (same paper, section, experiment; value carried in d204:2's conditions) |
| 2 | Dendrobaena veneta, acetazolamide muted the CO2 response | drop | whole record | Repeat of desk-d204:3 (identical quote and value) |
| 3 | Tiliqua adelaidensis, brown snake scent differed from both controls | correct | conditions | Quote MATCH, citation and CC BY-NC licence on the copy read right; says scent papers were placed in enclosures, but 20 of 57 lizards were wild, tested at natural burrows in the field |
| 4 | Echinotriton chinhaiensis, visual-cue GEE group effect beta 0.164, p 0.011 | correct | conditions | Quote MATCH; "groups" were the same five larvae run control first then with the bullfrog; interaction at 4 and 6 min only |
| 5 | Echinotriton chinhaiensis, odour cut crossings 3.167 against 5.500 | correct | conditions | Quote MATCH; same paired, control-first design not stated |
| 6 | Echinotriton chinhaiensis, odour GEE group effect null, p 0.205 | correct | conditions | Quote MATCH; same paired, control-first design not stated |

Errors per record: line 1: 1 (duplicate); line 2: 1 (duplicate); line 3: 1 (scientific context); lines 4, 5, 6: 1 each (scientific context). 6 faults in 6 records; 6 of 6 records in error.

Evidence errors: 6 of 6 records (100%): duplicates 2 (lines 1, 2; unfixable, drop); scientific-context faults 4 (lines 3 to 6; fixable); quote-form 0; licence 0; bibliographic 0; name 0; abstract-access grading 0.

Pooled with audits 172 to 288: 275 of 632 evidence records (43.5%; audit 288's 269 of 626, and 6 of 6 here). No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Lines 1 and 2: drop. (Optional, after a reading of the Pharmacology section: add line 2's blocker nulls to desk-d204:3's `conditions`.)

Line 3:
- `conditions`: "57 pygmy bluetongue lizards in three groups: 20 wild lizards tested in the field at their natural burrows at Tiliqua Reserve, about 10 km from Burra, and, at Monarto Safari Park, 9 wild-born captive adults (potentially predator-experienced) and 28 captive-born predator-naive offspring housed individually with artificial burrows; scent = paper towel left 48 h in a reptile enclosure, frozen at -20 C and used within 3 weeks, pinned about 5 cm from the lizard's burrow; each lizard met each of five scents once over a 5-day period, order randomised; 30 min acclimation after camera setup then 30 min filmed, tongue flicks at the scent paper counted; scents: eastern brown snake (one animal), eastern bluetongue lizard and Rosenberg's monitor (probably pooled from several animals), a novel control (1:10 diluted eucalyptus oil) and distilled water; mean tongue flicks brown snake 24.07 ± 4.93 s.e., bluetongue 14.33 ± 2.83, monitor 12.81 ± 4.04, novel control 5.81 ± 1.73, water 5.42 ± 1.59; no significant difference among the other treatments, so only the snake scent differed from the controls; tongue flicks did not differ significantly among lizard origins or days; temperature (16.8 to 30.1 C, covariate) had a significant effect on tongue flicks; basking time did not differ with treatment; repeated-measures PERMANOVA; no scent dose and no health screening reported"
- `note`, licence sentence: "Licence on the CSIRO full-text page is CC BY-NC ('Open Access CC BY-NC'); Crossref registers CC BY-NC-ND 4.0 for the version of record from 2025-05-26. Filed under the CC BY-NC printed on the copy read."

Line 4 `conditions`: "Larvae hatched in the lab from eggs collected in the Chinhai Spiny Newt Nature Conservation Area in April-May 2024 and reared without predator exposure; larval stage not stated; 30 replicates, each of five larvae run first as their own control (empty side compartments with water at the same depth) and then, the same five larvae retained, with one American bullfrog (large class, 258.26 ± 19.70 g) placed at random in a side compartment, so control always preceded the cue; 60 x 30 x 10 cm acrylic tank, water 4.5 cm deep, three compartments separated by high-transparency acrylic panels, leak-checked for 48 h to exclude chemical cues; 5 min acclimation then larvae in the distal zone counted at 2, 4, 6, 8 and 10 min; the group-by-time interaction was significant at 4 and 6 min, and the text and Table 2 give different values for 4 min (beta 0.182, p 0.018 against 0.233, p 0.004); the visual cue also lowered midline crossings (4.167 ± 2.718 against 5.333 ± 2.551, Wilcoxon signed-rank V = 288, p = 0.017)"

Line 5:
- `conditions`: "Chemical cue = 30 mL of water conditioned 24 h by four adult bullfrogs fed frog tadpoles (1 L sun-exposed water, filtered), injected into one side compartment behind perforated acrylic partitions (2 mm pores); 30 replicates, each of five lab-hatched, predator-naive larvae (stage not stated) run first as their own control (30 mL plain sun-exposed water) and then, the same five retained, with the cue, so control always preceded the cue; Wilcoxon signed-rank V = 314, p < 0.001; odour concentration not given beyond the volume; whether ± is SD or SE not stated in the passage read; the same cue produced no significant overall spatial avoidance (see the companion record)"
- `units`: "midline crossings by the five larvae together in 10 min"

Line 6 `conditions`: "Null result for avoidance by odour alone; the group-by-time interaction was significant only at 6 min (beta = -0.302, p = 0.042); 30 replicates, each of five lab-hatched, predator-naive larvae run first as their own control (30 mL plain water) and then, the same five retained, with 30 mL of water conditioned 24 h by four adult bullfrogs, so control always preceded the cue; bullfrog odour dose beyond volume not given; the same cue lowered activity (see the companion record)"

## Owner questions

1. Progress note question 1 (exudate as sense_chemical): moot for this unit (both Dendrobaena lines are repeats); on main, d204's rows already note the aversion proxy as the ruling asks.
2. Progress note question 2 (Tiliqua licence): answered. The copy read prints CC BY-NC, so the CC BY-NC rule applies and the record stands; NC-ND appears only in Crossref's version-of-record licence. Confirm that a later NC-ND registration does not override the licence printed on the copy read.
3. Echinotriton chinhaiensis (ASW: Echinotriton chinhaiensis (Chang, 1932)) and Tiliqua adelaidensis (Reptile Database: Tiliqua adelaidensis (Peters, 1863)) are not in gbif-names.tsv; both are accepted by those authorities. Add both through the owner.

## Progress note

Accurate on DOIs, Crossref years and licences. Wrong that Dendrobaena had no rows: desk-d204 on main holds the same paper and both findings. The Tiliqua licence summary is right. Owner question 3 should also name Tiliqua adelaidensis. Held-out leads were not re-checked (they are not filed records).

Verdict: 6 records in error of 6 (100%), 6 faults, above the 5% bar; pooled 43.5%. Error lines: 1, 2, 3, 4, 5, 6. Lines 1 and 2 drop as repeats of main; lines 3 to 6 are fixable with the replacement text.

This report is model output and carries no authority.
