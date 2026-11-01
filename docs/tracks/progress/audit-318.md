# audit-318: desk-d227, evidence lines 6 to 9

Audited 31 October 2026 from the desk-d227 files present untracked in the worktree (docs/tracks/progress/desk-d227.md and docs/views/evidence/desk-d227.jsonl, 9 lines; neither committed here, neither edited). HEAD and origin/main db3c6ecd (desk-d226). Audit 317 judges lines 1 to 5. `python3 -I tools/senses/check.py | grep d227`: "docs/views/evidence/desk-d227.jsonl: 9 records, 0 problems". Quote lengths (`len(q.split())`) for lines 6 to 9: 27, 22, 31, 30, all within 40. Evidence records only, so the brief's search-record parts do not apply; audits 314 to 316 are the format model.

Sources opened (WebFetch): www.mdpi.com/2076-2615/10/2/233 (two passes); journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0006831 (three passes); www.mdpi.com/2076-2615/12/19/2603 (two passes); api.crossref.org/v1/works for all three DOIs; for the Bufotes name, science.mnhn.fr/taxon/species/bufotes/balearicus, www.wikiwand.com/en/articles/Bufo_balearicus, and a treatment.plazi.org link that returned only a redirect notice. en.wikipedia.org/wiki/Bufotes_balearicus was blocked (permission not answered) and not retried. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 2 WebSearches and 14 WebFetch calls used.

## Bibliographic and licence

- Line 6, Ștefănescu et al. 2020, Crossref /v1: seven authors Raluca Ștefănescu to Mihai Musteata in the recorded order; title verbatim, with "procynoides" as printed; Animals 10(2), 233, issued and published online 2020-02-02; CC BY 4.0 vor; relation empty, no update-to. Page prints "distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license". Met.
- Line 7, Byamungu et al. 2018, Crossref /v1: eight authors Mechtilda Byamungu to Patrick M. Guerin in the recorded order; title verbatim (page, two pieces); PLOS Neglected Tropical Diseases 12(9), e0006831, issued 2018-09-25; CC BY 4.0 vor. Page: "This is an open access article distributed under the terms of the" "Creative Commons Attribution License". Met. Uncounted: Crossref carries an update-to of type "new_version" on the same DOI dated 2018-10-05, and the page header shows "Version 2 Version 1 Uncorrected Proof"; the page gives no correction notice. The record does not say it was read from Version 2; the desk may add that to `note`.
- Lines 8 and 9, Gazzola, Guadin, Balestrieri, Pellitteri-Rosa 2022, Crossref /v1: authors in the recorded order; title verbatim; Animals 12(19), 2603, issued 2022-09-28; CC BY 4.0 vor; relation empty, no update-to. Page prints the CC BY statement. Met.

Bibliographic faults 0; licence faults 0. source.access "open" right on all four.

## Names

- Line 6, Nyctereutes procyonoides (Canidae, Carnivora): right, and consistent with main (gaps cells.jsonl:20665 ff., "Mainland Raccoon Dog"; oa-2.jsonl:2427 to 2428). Wild-type check asked by the launch prompt: the species has no domestic breed; the animals were held in pens, the Methods saying verbatim "All individuals where captured and bred in captivity in pens placed in a forest environment." So this is the wild species kept captive (stock origin not stated further), not a domestic strain. No fur-farm statement on the page (tool summary of the Methods). The title's "procynoides" is a printed misspelling, noted in the record; harmless.
- Line 7, Glossina swynnertoni (Glossinidae, Diptera): right.
- Lines 8 and 9, Bufotes balearicus (Bufonidae, Anura): family and order right and consistent with main's Bufotes viridis rows. Status is not settled by a source I could reach: the paper uses "Bufotes balearicus" throughout with no taxonomic remark (tool summary); MNHN gives "Bufotes balearicus" "(Boettger, 1880)" with no status; Wikiwand treats it as a full species ("molecular genetic data now firmly support its status as a separate species"); a Plazi treatment titled "Bufotes viridis balearicus (Boettger, 1880)" appeared in search results but opened only a redirect notice, so a subspecies treatment exists somewhere in the literature. Main's gaps frog view lists Bufotes boulengeri, cypriensis, pewzowi and viridis but no balearicus, and gbif-names.tsv has no balearicus line. Not counted; owner question below.

Name faults 0 (one open question).

## Duplicates

git grep on origin/main across the whole docs tree (evidence, audit/corrected, audit/ALL.jsonl, searched, sheets, gaps, batches, progress notes) for "Nyctereutes", "procyonoides", "raccoon dog", "swynnertoni", "pntd.0006831", "Byamungu", "Bufotes", "balearicus", "green toad", "Gazzola", "ani10020233", "ani12192603", "10020233", "12192603". Nyctereutes procyonoides on main: oa-2.jsonl:2427 to 2428 (Banks et al. 2015, pupil), gaps vision cells, audit 70/71 vision leads; no sense_hearing row and not this DOI. swynnertoni and its DOI: absent. Bufotes: only B. viridis rows (canon-3.jsonl:127, oa-2.jsonl:259 to 261, gaps cells) and the oa-9 batch lead; balearicus and the DOI absent. "Gazzola" on main is a different paper (audit-315 line 8, desk-d225 Rana dalmatina, PLOS ONE 19(5)). Lines 8 and 9 are distinct results of one paper: line 8 is the activity response (chemical and combined cues lower activity; visual alone does not), line 9 the half-arena position response to the caged predator; different response variables, different models, different traits. Duplicate faults 0.

## Per-record findings

### Line 6, Nyctereutes procyonoides, BAEP waves I, II, III and V identified

Abstract, verbatim in two pieces: "Four waves (I, II, III and V) were identified and evaluated for latencies, morphologically" "similarity to those previously reported for other species (dogs, horses, cats, and ferret)." MATCH, 27 words; value says no more. Methods confirmed verbatim: nine "clinically healthy individuals (six males, three females) aged between 1 and 3 years," 5 to 6.6 kg; "Stimulus intensity was set at 90 dB SPL"; "alternating 0.1 ms click stimuli"; masking "white noise with an intensity of 50 dB SPL"; "Each waveform resulted was an average of 1000 stimulations."; two examinations "at a 5 min interval during one single general anesthesia"; "we assumed that wave IV was absent in any of the records". Latencies in the record agree with the Results (tool summary of the table). No repetition rate, no threshold, as recorded.

**Error (sample provenance misstated; stimulus bandwidth and the reliability nulls omitted).** (a) The record says "captive-bred adults"; the Methods say the animals were "captured and bred in captivity in pens placed in a forest environment", which includes captured animals. (b) The record's method says "0.1 ms broadband clicks"; verbatim "The broadband click included frequencies between 100 (low cut) and 3000 Hz (high cut).", so the waves were obtained with a click limited to 0.1 to 3 kHz, which bounds what the identification says about the species' hearing range. (c) Omitted: verbatim "no significant differences were noticed (p = 0.433)" for individuals and sex, "no significant differences were observed when the wave's latency values were compared" "after the right, left ear or binaural stimulation (p ≥ 0.661 for latencies)", amplitudes "(p ≥ 0.219)", and session-to-session p ≥ 0.817 (tool summary). The record lists left, right and binaural means without saying they did not differ. Fixable. Uncounted: the anaesthetic doses print as "xylazine (60 μg/kg i.m.) and ketamine (80 μg/kg i.m.)" (likely mg/kg); the record gives no doses, so nothing to correct.

### Line 7, Glossina swynnertoni, 0.5 m2 oblong not significantly lower than 1 m2 square

Abstract, verbatim in two pieces: "Landings by G. swynnertoni on 0.5 m2 blue-black oblong targets were likewise not significantly lower than" "on equivalent 1 m2 square targets." MATCH, 22 words; value says no more. Methods confirmed verbatim: "Tanzania, end of the wet season, July 2013.", Death Valley near Seronera Lodge, "Latin square design experiments of days x sites x" "treatments, with three simultaneous replicates.", adhesive film on both sides, "flies of each sex from each device were counted after 24 hours at each position." Statistics: "Analysis was performed on log (x+1) transformed data including day and position as additional explanatory parameters." and "Tukey contrasts were calculated to compare treatments." (tool summary for the join). The record's "in the unbaited trials" for Tanzania was not confirmed: the page's baited/unbaited sentences refer to Angola (uncounted; see Unchecked).

**Error (effect size, the contrary size result for squares, the edge-length confound and the colour results omitted).** Results fragments verbatim: "Landings on the 0.5 m2 blue/black oblong were particularly high for G. swynnertoni" "(90% of the daily landing rate on the 1 m2 square target)"; "landings were reduced by around 50% on the equivalent 0.5 m2 square targets" (the species scope of this sentence was not returned whole); oblong against square "most noticeably for G. swynnertoni (62% more) but this difference was not significant (P > 0.05)"; "with landings significantly lower for G. swynnertoni on the all-blue square target"; "with at least three times as many flies landing on blue compared to black" (Wilcoxon, P < 0.05 for all species, tool summary). The size null therefore holds for the horizontal oblong, and halving a square cut landings by about half; the Abstract ties landing to horizontal edge length ("The length of target horizontal edge was closely correlated with landing rate."), so the record's size comparison is confounded with shape and edge. The record carries none of the 90%, the 50% or the blue-portion bias, which is the paper's most direct visual result for this species. Fixable in conditions.

### Line 8, Bufotes balearicus, activity falls after chemical cues

Abstract, verbatim in three pieces: "The tadpole level of activity strongly decreased after exposure to either chemical cues alone" "or in combination with visual cues," "while visual cues alone apparently did not elicit any defensive response." MATCH, 31 words; value says no more. Methods confirmed verbatim: "In May 2020 six freshly laid green toad egg strings were collected from a network of canals"; "40 tadpoles were selected from each string (29–33 Gosner stage)"; "We tested 24 individuals for each of the four predator treatments (overall, n = 96 tadpoles)."; "Each tadpole was randomly assigned to a specific combination of sensory cues"; 5 min acclimation; "The olfactory stimulus consisted of 8 mL of the mixed solution,"; "The concentration of the cue (1:125)"; "predators were used 2–3 times each"; trial as the only random effect. Results verbatim: "tadpole post-stimulus activity was affected by both pre-stimulus activity (χ2 = 6.68, df = 1, p = 0.01)" "and treatment (χ2 = 98.23, df = 3, p < 0.0001)."; "Olfactory cues, both alone and in combination with visual cues, induced a significant decrease" "in tadpole activity in comparison to controls and visual cues."

**Error (sample composition omitted).** The record says "egg strings collected" without the number. The 96 tadpoles came from six egg strings, 40 drawn per string, and string was not a random effect in either model (only trial), so the treatment groups are drawn from six sibships with clutch unmodelled. That limits the effective sample and is a design confound under the desk rules (sample composition). Also omitted and added below: the pre-stimulus covariate, that the post hoc contrasts have no printed statistics, that per-treatment activity estimates are only in Figure 3, and that no power analysis is given. Fixable. Uncounted: the Abstract says recordings lasted "40 min" while the Methods say "We conducted trials of 45 min in total"; the record's 5 + 20 + 20 min agrees with the Methods.

### Line 9, Bufotes balearicus, position not affected by the caged predator (visual null)

Abstract, verbatim in two pieces: "The position of tadpoles inside the arena was not affected by visual cues, suggesting that green toad" "tadpoles mainly rely on olfactory cues to assess the level of predation risk." MATCH, 30 words; value says no more. Method confirmed: position coded per frame 0 in the predator half, 1 in the opposite half, analysed as "the proportion of far-from-predator observations", Gaussian GLMM with treatment and the pre-stimulus covariate, trial random.

Null design and power, as the launch prompt asked: the record gives the design (24 per arm, randomised, controls, single placement) and the statistic, but no power statement. The paper has no power analysis or sample-size justification (tool summary of a full read; the only sentence is the n = 96 one).

**Error (significant position shift in the multimodal arm and the side-bias statistics omitted; no power statement).** Results verbatim: "This tendency was, in general, further increased by cues, with the post-stimulus mean of the multimodal stimulus treatment" "differing significantly from the corresponding pre-stimulus (pre-post estimated difference = 0.09," "SE = 0.04, df = 182, t-ratio = 2.18, p = 0.02)."; "Tadpoles showed a general tendency to spend more time in the half of the arena where the transparent container was present" "(all means, for all treatments both pre- and post-stimulus, were <0.5);" "except for the pre-stimulus control and olfactory + visual treatments, these differences were significant" "(highest p = 0.03)."; and "Tadpole position was not affected by either treatment (χ2 = 0.41, df = 1, p = 0.51) or pre-stimulus distance" "(χ2 = 1.60, df = 3, p = 0.65); actually, the mean values of all treatments were similar" "to those recorded for the control group." The record files a visual null on position without the one significant position change the paper reports (the multimodal arm, with the predator visible, after the stimulus) and paraphrases the printed "either treatment" as "visual cue treatment". The direction of the multimodal shift is not stated in words; from the coding it is toward the container (my inference, not the paper's wording). The printed df = 3 for a single covariate looks like a reporting slip; harmless to carry as printed. Same six-egg-string omission as line 8. Fixable.

## Trait key

- Line 6, sense_hearing: fits (evoked auditory brainstem responses in a living animal).
- Line 7, behaviour_vision: fits (landing on visual targets of differing size, shape and colour).
- Line 8, sense_chemical: fits (behavioural response of living tadpoles to predator odour; the odour is diet-conditioned, stated).
- Line 9, behaviour_vision: fits as a behavioural visual null.

Trait key faults 0. Grading: `m` right on all four (one named species measured in each paper).

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 6 | Nyctereutes procyonoides, BAEP waves I, II, III, V | error, fixable | method, conditions | Quote MATCH (27 words); "captive-bred" for animals "captured and bred in captivity"; click stated as 100 to 3000 Hz shown only as "broadband"; ear, sex and session nulls omitted. Wild species, not a domestic strain |
| 7 | Glossina swynnertoni, 0.5 m2 oblong not lower than 1 m2 square | error, fixable | conditions | Quote MATCH (22 words); 90% effect size, ~50% fall for 0.5 m2 squares, 62% oblong advantage (ns), all-blue square significantly lower and 3x blue-portion landing bias omitted; size confounded with shape and edge |
| 8 | Bufotes balearicus, activity falls to chemical cues | error, fixable | conditions | Quote MATCH (31 words); six egg strings (40 per string, string not modelled) omitted; covariate, missing post hoc statistics and power not stated |
| 9 | Bufotes balearicus, position null to visual cue | error, fixable | conditions | Quote MATCH (30 words); significant multimodal pre-post position shift (p = 0.02) and side-bias statistics omitted; "either treatment" paraphrased; no power statement; egg strings omitted |

4 of 4 records in error (100%): scientific-context 4 (lines 6 to 9; line 6 also a factual misstatement of provenance); value beyond quote 0; quote form 0; duplicates 0; bibliographic 0 (line 7 version note uncounted); names 0 (Bufotes balearicus status left as an owner question); licence 0; trait key 0; grading 0. HOLD OUT: none.

Pooled with audits 172 to 316: 374 of 782 evidence records (47.8%), taking audit 316's 370 of 778 and adding 4 of 4 here; audit 317's lines 1 to 5 are not included and should be added when it reports.

## Replacement text

Line 6:
- `method`: replace "0.1 ms broadband clicks through foam earphones" with "alternating 0.1 ms clicks through foam earphones, the 'broadband click' stated to include frequencies between 100 (low cut) and 3000 Hz (high cut)".
- `conditions`: replace "nine clinically healthy captive-bred adults (six males, three females, about 1 to 3 years)" with "nine clinically healthy adults (six males, three females, aged 1 to 3 years, 5 to 6.6 kg) that 'where captured and bred in captivity in pens placed in a forest environment' (wild species held captive; stock origin not stated further)".
- `conditions`: replace "click repetition rate not reported;" with "click repetition rate not reported; the click spanned only 100 to 3000 Hz, so the response says nothing about higher frequencies; latencies did not differ between individuals or sexes (p = 0.433), among left, right and binaural stimulation (p ≥ 0.661; amplitudes p ≥ 0.219) or between the two sessions (p ≥ 0.817);".

Line 7:
- `conditions`: replace "this is a statement of no significant difference between sizes, not a spectral or acuity measurement;" with "the 0.5 m2 blue-black oblong took '90% of the daily landing rate on the 1 m2 square target' (P > 0.05), but 'landings were reduced by around 50% on the equivalent 0.5 m2 square targets', and horizontal oblongs beat equal-area squares 'most noticeably for G. swynnertoni (62% more) but this difference was not significant (P > 0.05)', so the size null holds for the oblong shape and is confounded with horizontal edge length, which the Abstract says was closely correlated with landing rate; landings were 'significantly lower for G. swynnertoni on the all-blue square target' (P < 0.05), and on blue-black targets 'at least three times as many flies' landed on blue as on black (Wilcoxon, P < 0.05); analysis on log (x+1) data with day and position as factors and Tukey contrasts; target dimensions are in Table 1 (image, not read); this is a statement of no significant difference between sizes, not a spectral or acuity measurement;".
- `note` (uncounted): replace "Abstract sentence copied whole from the PLOS page (returned in fragments)." with "Abstract sentence copied whole from the PLOS page (returned in fragments), Version 2 (Crossref update-to new_version, 2018-10-05; no correction notice on the page)."

Line 8:
- `conditions`: replace "egg strings collected in May 2020 from canals east of Milan, Italy" with "six egg strings collected in May 2020 from canals east of Milan, Italy, 40 tadpoles drawn per string, with string not entered as a random effect (only trial), so the 96 tadpoles come from six sibships".
- `conditions`: replace "treatment effect on activity chi2 = 98.23, df = 3, p < 0.0001;" with "treatment effect on activity chi2 = 98.23, df = 3, p < 0.0001, with pre-stimulus activity as covariate (chi2 = 6.68, df = 1, p = 0.01); olfactory cues alone and combined lowered activity relative to both controls and visual cues (post hoc contrasts, no test statistics printed); per-treatment activity estimates appear only in Figure 3; no power analysis or sample-size justification;".

Line 9:
- `conditions`: replace "egg strings collected in May 2020 from canals east of Milan, Italy" with "six egg strings collected in May 2020 from canals east of Milan, Italy, 40 tadpoles drawn per string, with string not entered as a random effect (only trial), so the 96 tadpoles come from six sibships".
- `conditions`: replace "visual cue treatment did not affect position (chi2 = 0.41, df = 1, p = 0.51);" with "'Tadpole position was not affected by either treatment (χ2 = 0.41, df = 1, p = 0.51)', with pre-stimulus distance printed as χ2 = 1.60, df = 3, p = 0.65, and treatment means similar to the control; in the pre/post model the multimodal (visual plus chemical) arm did shift position after the stimulus (pre-post estimated difference = 0.09, SE = 0.04, df = 182, t-ratio = 2.18, p = 0.02), the authors writing that the near-container tendency 'was, in general, further increased by cues'; no pre-post change is reported for the visual-only arm;".
- `conditions`: replace "tadpoles tended to spend more time on the container side across treatments;" with "tadpoles spent more time in the container half in every treatment before and after the stimulus (all means < 0.5), significantly so except in the pre-stimulus control and multimodal cells (highest p = 0.03);".
- `conditions`: replace "this is a null result for one predator species at a single distance and does not measure visual ability" with "this is a null from 24 tadpoles per arm with no power analysis or sample-size justification, a half-arena (0/1) position measure, one predator species and one container placement, and it does not measure visual ability".

Values marked "(tool summary)" in the findings and reused above (session p ≥ 0.817, the Wilcoxon test for the blue bias) should be confirmed against the page text when the desk applies them.

## Unchecked

- Line 7: whether the Tanzania trials were unbaited (the page's baited/unbaited sentences name Angola); the species scope of the "reduced by around 50%" sentence (returned as a fragment); target dimensions (Table 1 image); what changed between Version 1 and Version 2.
- Line 6: whether the captured animals were wild-caught in Romania or captive-born (the Methods sentence does not say); "foam earphones" in the record's method (not returned by the tool).
- Lines 8 and 9: "east of Milan" (the returned sentence ends at "a network of canals"); per-treatment activity and position means (figures only).
- Bufotes balearicus status: Wikipedia blocked; Plazi treatment "Bufotes viridis balearicus" not opened (redirect only); Amphibian Species of the World not reached.

## Owner questions

1. Bufotes balearicus: the paper's name; a full species on the sources read, but a subspecies treatment (Bufotes viridis balearicus) exists and main's gaps frog view lists no B. balearicus. Which authority settles the frog view, and does it accept B. balearicus?
2. The unit's question on subspecies (Glossina m. centralis): not affected here; line 7 is the full species.

## Progress note

Accurate on citations, licences, quotes and duplicates. The Records list repeats the faults above: the raccoon dogs as "captive-bred" with a "broadband" click; Glossina without the 90% figure and the square-target halving; Bufotes position null without the multimodal shift.

Verdict: 4 of 4 records in error (100%), above the 5% bar. Error lines 6, 7, 8 and 9, all fixable with the replacement text above; none held out. Pooled 374 of 782 (47.8%) before audit 317.

This report is model output and carries no authority.
