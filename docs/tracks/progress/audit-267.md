# audit-267: desk-d183 (7 evidence records, no search records, no wanted lines)

Audited 30 October 2026 from the desk-d183 files present untracked in the worktree (docs/tracks/progress/desk-d183.md and 7 evidence lines in docs/views/evidence/desk-d183.jsonl; neither committed here, neither edited). `tools/senses/check.py` on the evidence file: 7 records, 0 problems. Quote lengths (`len(q.split())`), lines 1 to 7: 31, 35, 32, 18, 26, 25, 27; all within 40. No searched or wanted file, so all seven records were judged. Rules applied: oa-audit.md "Scientific context and counting (29 October 2026)", oa-read.md (grade and `partial`), BRIEF quote rules, the publisher-copy licence rule and the name rule, in the form of audits 264 to 266. Duplicates checked with git grep on origin/main (f7951387) under docs/views/evidence, docs/views/audit/corrected, docs/views/audit/ALL.jsonl, docs/views/searched and docs/views/wanted for "Carcharhinus plumbeus", sandbar, Anderson, 11459, "Apis mellifera" (acuity_cpd, behaviour_vision, motion), Desai, 251776, Tiliqua, Fleishman, famrs, 1426675, "New and Bull". 1 WebSearch and 9 WebFetch calls used (counting the refused fetch).

Sources opened: api.crossref.org/works/ 10.1038/S41598-017-11459-8, 10.1242/JEB.251776, 10.3389/FAMRS.2024.1426675, 10.1007/S00359-011-0635-8 (the primary the review cites; DOI taken from the review's Crossref reference list); link.springer.com/10.1038/s41598-017-11459-8 (record URL; two passes); journals.biologists.com jeb251776 PDF (record URL); frontiersin.org famrs.2024.1426675/full (record URL); researchnow.flinders.edu.au publication page for New and Bull 2011 (returned by my WebSearch; abstract only).

Blocked and not retried: nature.com/articles/s41598-017-11459-8 (permission not answered). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries, so quotes were checked by MATCH/MISMATCH; points marked "(tool summary)" were not returned verbatim.

## Bibliographic and licence (Crossref, fresh)

- Anderson: James M. Anderson, Tamrynn M. Clegg, Luisa V. M. V. Q. Véras, Kim N. Holland; Scientific Reports 7, issue 1, article 11042; issued and online 2017-09-08; CC BY 4.0 (vor and tdm, from 2017-09-08); relation empty, no update-to. As recorded. The Springer page labels the article open access, "© The Author(s)" (tool summary). Publisher's own free copy with Crossref vor CC BY: accepted.
- Desai: Rishabh Desai, Matthew A. Garratt, Mandyam V. Srinivasan, Sridhar Ravi; Journal of Experimental Biology 229, issue 8, article jeb251776; issued and print 2026-04-15, online 2026-04-22; CC BY 4.0 vor from 2026-04-22 (delay 7 days); relation empty, no update-to. The PDF states "This is an Open Access article distributed under the terms of the Creative Commons Attribution License". Accepted. Uncounted: the notes' "(issued 2026-04-15)" is the issue date; the licence starts 2026-04-22.
- Fleishman: Leo J. Fleishman; Frontiers in Amphibian and Reptile Science 2, article 1426675, no issue; issued 2024-08-09; CC BY 4.0 vor, delay 0; type journal-article; relation empty. As recorded.
- New and Bull (cited primary): Shaun T. D. New, C. Michael Bull, "Retinal ganglion cell topography and visual acuity of the sleepy lizard (Tiliqua rugosa)", Journal of Comparative Physiology A 197(6): 703-709, issued 2011-03-09; Crossref licence only springer.com/tdm (no Creative Commons). Not open.

Bibliographic faults 0; licence faults 0.

## Names

Carcharhinus plumbeus (usage key 2418009), Apis mellifera (1341976), Tiliqua rugosa (2462522): EXACT, ACCEPTED in docs/views/gaps/gbif-names.tsv. Name faults 0.

## Duplicates

- Anderson 2017 is on main as docs/views/audit/corrected/fish-shark.jsonl line 164 (Carcharhinus plumbeus, sense_magnetic, grade m), audited "confirm" (ALL.jsonl line 904, fish-shark:164). Its quote is word for word desk-d183 line 1's quote. Its value already carries line 2's finding ("with magnetic sense impaired they no longer discriminated"), and the audit's passage_quote is line 2's quoted sentence. Lines 1 and 2 therefore repeat main. Line 3 (100% response across 0.03 to 2.89 µT) is not on main; the main row's note says the thresholds were "not read here". Line 3 is new.
- Fleishman 2024 is on main as docs/views/evidence/oa-12.jsonl line 113: Tiliqua rugosa, acuity_cpd 7.3, same DOI, same quote, grade m, `partial: true`. desk-d183 line 7 repeats it. Main also holds 6.8 cpd for the same species from New and Bull (2011) via two other secondaries: oa-2.jsonl line 3951 (Hauzman et al. 2018, partial) and oa-8.jsonl line 210 (Nagloo et al. 2022; retracted in ALL.jsonl for journal field and partial flag). Line 7 therefore also conflicts with main's other value for the same primary.
- Desai 2026: not on main. Apis mellifera rows on main give stationary detection at 3 to 5 degrees (Kelber and Somanathan 2019), 5 degrees with green-receptor contrast and 15 degrees with colour contrast only (Giurfa et al. 1996), and grating acuity 0.12 to 0.54 cpd. Desai's sub-degree results come from a different task (shape choice in a Y-maze with oscillating 3D targets), so they do not repeat or directly contradict those rows, but a view built from them should not read 0.44 degrees as a static acuity (see note text below).

Duplicates: 3 (lines 1, 2, 7).

## Per-paper findings

### Anderson et al. 2017 (lines 1 to 3), sense_magnetic

Quotes. Lines 1 and 2 MATCH (Abstract); line 3 MATCH (Results). All whole sentences.

Context confirmed (tool summary): 7 m circular tank; coil of 100 turns of 18 AWG copper wire over 120 cm; unimpaired series 10 trials, 5 sharks in the first eight, 7 in the last two; Friedman χ² = 61.417, df = 20, p = 2.99e-06, Wilcoxon V = 0, p = 0.001953; impaired Friedman χ² = 21.382, df = 20, p = 0.375; unimpaired against impaired S+ minute W = 85, p = 0.009; neodymium magnets 1.2 x 0.3 x 0.3 cm in gelatine in sealed 2.5 x 2.5 x 1 cm boxes glued over the olfactory capsules; "we did not conduct comparative control trials with empty boxes attached." The Results give 4 sharks in seven impaired trials and 3 in three; the Methods describe the sequence differently (tool summary), so the impaired counts are not fully consistent within the paper.

Omitted confound (counts on line 3). The paper's own calculation is that the magnetic stimulus induced an electric transient above the electrosensory threshold over much of the arena:
- Results, Electrical field measurement and calculation: "Under application of weak magnetic fields (0.029 μT) used in testing, the maximum transient voltage gradient was calculated to be 74.35 nanoVolts (nV) cm/s−1 (Fig. 6) at the periphery of the tank." (verbatim, split by the tool and rejoined)
- Same section (fragment): "our calculations indicate that it remained above the 30 nV cm−1 median sensory threshold" "across more than half of the experimental arena (Fig. 6)."
- Discussion: "Thus, we cannot definitively rule out the shark electrosense being involved in observed conditioned responses." and "However, as we did not incorporate this control group into our study, we must interpret our results with a degree of caution."

Line 3's note says the paper finds it "unlikely" that transient electrical artefacts served as the stimulus and that "those figures were not logged"; line 1's note says the likelihood "was low". Neither record states that the authors' own figure puts the transient above the cited median electrosensory threshold across more than half the arena, or that they cannot rule out the electrosense. That changes the causal interpretation of a sense_magnetic record (a magnetic sense against an electrosensory response to induced transients), and the `eye` field "receptor not identified" does not convey it. Counted as a scientific-context fault on line 3 (fixable) and on lines 1 and 2 (already counted once each as duplicates). Also omitted: counts were pooled because "count information was not available on an individual level, due to the difficulty in reliably identifying individual sharks" (Methods, fragment), so line 3's "all sharks demonstrating a conditioned response" is the authors' group-level statement; add to the note (uncounted on its own).

Line 2's sham caveat is right and well put.

### Desai et al. 2026 (lines 4 to 6), behaviour_vision

Quotes. Lines 4, 5 and 6 MATCH (Abstract); whole sentences.

Results confirmed (tool summary, text and Table S1): Experiment 1 (stationary diamond against disc, trained to diamond): 3.1° 76%, p = 0.0007, binomial 0.0003; 1.9° 68%, p = 0.0232, binomial 0.0153; 0.88° p = 0.1491, binomial 0.1189; 0.44° p = 0.3818, binomial 0.1611. Experiment 2 (moving against stationary disc, trained to the stationary disc): 75% at 3.1° (text p = 0.007, Table S1 0.0007), 74% at 1.9°, 72% at 0.88°, 70% at 0.44° (p = 0.0109). Experiment 4 (both moving, trained to stationary diamond): 72% at 0.44°, 70% at 3.1°; only these two sizes were tested. Angular size is the angle at the decision point of the 205 mm central chamber; 10, 20, 43 and 70 mm stimuli. Motion ±20°, 3.5 Hz; Discussion peak angular velocity up to 500 deg/s, average near 350 deg/s. No luminance or contrast measured; the authors say illumination and contrast "could affect detection and discrimination capacities" (tool summary).

Line 4. The value restates the Abstract's ">1.9°", which the paper's own Results contradict (significant at 1.9°). The note gives the Results figures and concludes that the stationary threshold lies between 0.88 and 1.9 degrees, so the limitation is unambiguously conveyed in the record; uncounted under the harmless-compression clause, as audit 266 line 6. The value should still carry it (replacement below).

Line 5. Value right. Uncounted: Experiment 2 is disc against disc (moving against stationary), not disc against diamond as the shared `conditions` say; bees were trained only to stationary stimuli, so the moving choice runs against training. The preference shows motion attracts at 0.44°; it is not a shape-acuity result.

Line 6. Value right; note's 70% at 3.1° and 72% at 0.44° MATCH. Uncounted: Experiment 4 tested only 0.44° and 3.1°; the "not when they were stationary" comparison is with Experiment 1 (different bees); the Experiment 4 3.1° statistics (p = 0.0103, phi 0.363, binomial 0.0066) are identical to Experiment 3's 0.44° values, a likely copying error in the paper that does not touch the 0.44° value. With ±20° oscillation the moving target sweeps far more than its 0.44° size, so the result is shape discrimination of a moving target, not a static acuity; a view should not convert it to cpd (the note already declines to).

### Fleishman 2024 (line 7), Tiliqua rugosa acuity_cpd

Quote MATCH (section 3.2 Spatial acuity of the retina), whole sentence. The review gives no method for the Tiliqua figure; it describes anatomical estimation in general terms (tool summary). The desk's `method` says so.

Admissibility. Under oa-read.md (Grade bullet and `partial` bullet), a review's report of a primary value on the record's own species is admissible, graded `m`, and must carry `partial: true` with the original study named in `note`. Line 7 names New and Bull (2011) but omits `partial: true`: a counted fault by audits 27 and 29 ("a compiled or review read without `partial: true` counts as `correct`").

Contrary primary. The primary abstract (Flinders research portal page; abstract only, no licence statement, not open on Crossref): "With a post nodal distance of 6.25 mm, we calculate an upper limit of visual acuity of 6.8 c/deg." So the primary gives 6.8 cpd, as an anatomical upper limit from ganglion-cell density (1,654,200 presumed ganglion cells, peak 15,500 cells per mm², loose horizontal streak; tool summary). The review's 7.3 disagrees with the primary it cites. The record files 7.3 as an `m` value with no sign of this, which would be a counted fault even if the record were new.

The record repeats main's oa-12 line 113 exactly, so it cannot be fixed by a field change: drop it. The fix belongs on main (owner question 1).

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Carcharhinus plumbeus, more S+ approaches, p < 0.01 | duplicate (drop) | whole record; note | Same paper, trait and quote as main fish-shark:164; also omits the authors' electrosense confound |
| 2 | Carcharhinus plumbeus, impaired no S+/S- difference, p = 0.375 | duplicate (drop) | whole record | Finding already in main fish-shark:164 value; same sentence as that audit's passage quote; sham caveat right |
| 3 | Carcharhinus plumbeus, 100% response 0.03 to 2.89 µT | correct | value, note | Quote MATCH and new; omits the paper's own calculation that the induced transient exceeded the 30 nV/cm median electrosensory threshold over more than half the arena and the authors' "cannot definitively rule out the shark electrosense" (Results, Discussion); scientific-context fault |
| 4 | Apis mellifera, stationary shape change >1.9° | confirm | (value; uncounted) | Quote MATCH; Abstract contradicted by Results at 1.9°, conveyed unambiguously in note; value should say so |
| 5 | Apis mellifera, moving preferred to 0.44° | confirm | (conditions, note; uncounted) | Quote MATCH; Exp. 2 is disc vs disc, trained to stationary; flicker caveat present |
| 6 | Apis mellifera, shape discrimination at 0.44° when both move | confirm | (note; uncounted) | Quote MATCH; only 0.44° and 3.1° tested in Exp. 4; cross-experiment comparison; table copying error at 3.1° |
| 7 | Tiliqua rugosa, 7.3 cpd | duplicate (drop) | whole record; partial | Repeats main oa-12:113 exactly; omits `partial: true`; primary abstract gives 6.8 c/deg upper limit |

Evidence errors: 4 of 7 (57.1%): duplicates 3 (lines 1, 2, 7); scientific-context faults 1 (line 3; lines 1 and 7 also carry context or partial faults, counted once each); quote-form 0; licence 0; bibliographic 0; name 0; pooled or cultivar 0. Unfixable records: lines 1, 2 and 7 (drop as repeats of main). Line 3 is fixable with the counted text below.

Pooled with audits 172 to 266: 199 of 496 evidence records (40.1%; audit 265's 195 of 481, plus audit 266's 0 of 8, plus 4 of 7 here). No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Counted (line 3):
- `value`: "100% conditioned response in all unimpaired sharks (group-level counts) to every applied field intensity, 0.03 to 2.89 microtesla; the authors cannot rule out an electrosensory response to induced electric transients"
- `note`: replace "The Abstract says the paper quantifies transient electrical artefacts and finds it unlikely they served as the stimulus; those figures were not logged." with "Confound: the authors calculate that at 0.029 µT the maximum induced transient voltage gradient was 74.35 nV cm/s−1 at the tank periphery and that it 'remained above the 30 nV cm−1 median sensory threshold across more than half of the experimental arena' (Results, Electrical field measurement and calculation); the Discussion states 'Thus, we cannot definitively rule out the shark electrosense being involved in observed conditioned responses.' Counts were pooled across sharks because individuals could not be reliably identified (Materials and Methods, Data Collection and Analysis), so 'all sharks' is a group-level statement."

Uncounted:
- Line 4 `value`: "stationary targets: Abstract says shape change (disc vs diamond) perceived only above 1.9 degrees, but the Results show significant discrimination at 1.9 degrees (68%, p = 0.0232) and 3.1 degrees, none at 0.88 or 0.44 degrees; stationary threshold between 0.88 and 1.9 degrees".
- Line 5 `conditions`: replace "stimuli (disc vs diamond)" with "this test: moving disc against stationary disc, bees trained only to the stationary disc; stimuli".
- Line 6 `note`: append "Experiment 4 tested only 0.44 and 3.1 degrees; the stationary comparison is Experiment 1 (other bees). The paper's Experiment 4 statistics at 3.1 degrees repeat Experiment 3's at 0.44 degrees, a likely copying error that does not affect the 0.44-degree value. The moving target oscillates ±20 degrees, so this is shape discrimination of a moving target, not a static acuity."
- Lines 4 to 6 `note`: replace "(issued 2026-04-15)" with "(licence from 2026-04-22; issue date 2026-04-15)".

Main-side, for the owner (not desk-d183 records): fish-shark:164 should carry the same confound sentence as line 3's note and, optionally, line 2's p = 0.375 and sham caveat; oa-12:113 should note that the primary abstract gives 6.8 c/deg.

## Owner questions

1. Tiliqua rugosa on main has 7.3 cpd (Fleishman 2024 review, oa-12:113) and 6.8 cpd (Hauzman 2018, oa-2:3951), both citing New and Bull (2011), whose abstract (Flinders research portal) says "we calculate an upper limit of visual acuity of 6.8 c/deg." Should oa-12:113 be corrected to 6.8, or held as the review's misreport with a note? A wanted line for New and Bull 2011 (J Comp Physiol A 197(6): 703-709, DOI 10.1007/s00359-011-0635-8, closed) would settle the anatomical method.
2. Anderson 2017: should the main row fish-shark:164 be reopened to add the electrosense confound, given that its audit confirmed it without it?
3. Desai 2026: the Abstract and Results disagree on the stationary threshold. Should a view use the Results (0.88 to 1.9 degrees) as line 4's replacement does?

Progress note: accurate on what was read and refused. Its claim that the Abstract says the authors quantify artefacts and find them unlikely is incomplete (see line 3), and it did not check main for repeats of Anderson or Fleishman.

Verdict: 4 errors in 7 (57.1%), above the 5% bar; pooled 40.1%. Error lines: 1, 2, 3, 7. Lines 1, 2 and 7 are unfixable (drop as repeats of main); line 3 can merge with the counted text; lines 4, 5 and 6 can merge with the uncounted fixes.
