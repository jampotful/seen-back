# audit-309: desk-d222, evidence lines 1 to 3

Audited 31 October 2026 from the desk-d222 files present untracked in the worktree (docs/tracks/progress/desk-d222.md and docs/views/evidence/desk-d222.jsonl, 3 lines; neither committed here, neither edited). HEAD 64ee99fb (desk-d221). `tools/senses/check.py` on the evidence file: 3 records, 0 problems. Quote lengths (`len(q.split())`): 18, 16, 15, all within 40. The unit has evidence records only, so the brief's search-record and plant-screening parts do not apply; audits 307 and 308 are the format model.

Duplicates: git grep on origin/main across docs (evidence, audit/corrected, audit/ALL.jsonl, searched, sheets, gaps, codex-findings, progress notes) for "Stygoparn", "comalensis", "Comal Spring", "dryopid", "Dryopidae", "Elmidae", "riffle beetle", "peerj.20507", "Pintar", "Podarcis lilfordi", "lilfordi", "Lilford", "Podarcis" (all traits), "peerj.2828", "Mencía", "Mencia", "tongue-flick", "Pimephales", "fathead", "copper", "anosmi", "peerj.13988", "Fatima".

Sources opened (WebFetch): peerj.com/articles/20507/ (three passes), peerj.com/articles/2828/ (two passes), peerj.com/articles/13988/ (two passes); api.crossref.org/works for the three DOIs; gbif.org/species/1033454 and www.fws.gov/taxonomic-tree/34191 (both returned by my WebSearch). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 1 WebSearch and 12 WebFetch calls used.

## Bibliographic and licence

- Line 1, Pintar 2025, Crossref: Matthew R. Pintar (sole author); title "Experimental tests of habitat preferences in the Comal Springs dryopid beetle, Stygoparnus comalensis" verbatim; PeerJ 13, e20507, issued 2025-12-16; licence CC BY 4.0 (content-version unspecified); relation empty. Page: citation "PeerJ, 13, article e20507" and a Creative Commons Attribution License statement (tool summary). Met.
- Line 2, Mencía et al. 2017, Crossref: Abraham Mencía, Zaida Ortega, Valentín Pérez-Mellado, in the recorded order; title verbatim; PeerJ 5, e2828, issued 2017-01-17; CC BY 4.0 (unspecified); relation has-review only. Page: "Mencía et al." and a Creative Commons Attribution License statement (tool summary). Met. Uncounted: the note says the tool printed the surname "with a stray accent"; Crossref prints "Mencía", so the accent is right and the record's "Mencía A" is correct.
- Line 3, Fatima et al. 2022, Crossref: Rubab Fatima, Robert Briggs, William A. Dew, in the recorded order; title verbatim; PeerJ 10, e13988, issued 2022-09-26; CC BY 4.0 (unspecified); relation has-review only. Page, verbatim: "This is an open access article distributed under the terms of the Creative Commons Attribution License". Met.

Bibliographic faults 0; licence faults 0 (licence printed on each peerj.com page read, which is the version of record; Crossref CC BY agrees). source.access "open" right on all three.

## Names

- Stygoparnus comalensis: GBIF backbone (species 1033454) classification "Order: Coleoptera / Family: Dryopidae / Genus: Stygoparnus"; US Fish and Wildlife Service taxonomic tree 34191 gives "Comal Springs dryopid beetle", Coleoptera > Dryopidae > Stygoparnus. Main has no Stygoparnus row; its only Dryopidae rows are Dryops sp. AD-2015 (oa-1.jsonl:4367 to 4369, opsin_sequences_recovered), which put Dryopidae under Coleoptera as the record does. Dryopidae confirmed; the unit's inference from the title is now backed by an authority.
- Podarcis lilfordi: main's gaps files carry it under Lacertidae, Squamata (cells.jsonl:47371 onward). Accepted, family right.
- Pimephales promelas: main's docs/views/no-view-us-fl-alachua.csv:854 gives Cypriniformes, Cyprinidae (GBIF key 2367742). Accepted, family right.

Name faults 0.

## Duplicates

None of the three DOIs is on main. No row on main for Stygoparnus under any trait. Podarcis lilfordi appears on main only in gaps/queue cells; main's Podarcis evidence rows are P. muralis (colour_vision, behaviour_vision, receptor_classes), none sense_chemical. Pimephales promelas appears on main only as prey in desk-d207.jsonl:3 (Esox masquinongy) and in the Alachua species list; no copper or anosmia row exists. The unit's held-out line "Already on main: Stygoparnus excluded" is unexplained (no Stygoparnus string anywhere on main); it does not affect the duplicate finding. Duplicates 0; contradictions 0.

## Per-record findings

### Line 1, Stygoparnus comalensis, behaviour_vision, 90% on dark side under UVA

Results, verbatim: "Ninety percent of S. comalensis were on the dark side in UV light, indicating avoidance of UV light." Returned whole in each of two passes, 99 characters, so not a truncation. MATCH, whole sentence, 18 words. Preceding text, verbatim pieces: "Significantly fewer S. comalensis were recorded on the light side for all other light types" and "approximately 50% (no preference between light and dark) were observed on each side". Table 1 rows, verbatim: White "10 | 2 | 18 | 10.0"; Blue "9 | 13 | 14 | 48.1 | −3.84 | −2.07 | 0.038"; Green "9 | 15 | 11 | 57.7 | −4.82 | −2.29 | 0.022"; Red "9 | 3 | 15 | 16.7 | −0.65 | −0.37 | 0.71"; UV "10 | 18 | 2 | 90.0 | −7.90 | −3.15 | 0.0017"; No light "10 | 9 | 10 | 47.4 | −3.85 | −2.02 | 0.043". The record's counts and P values match. Methods, verbatim: "all experimental chambers had the treatment (open light end) on the same side for this experiment."; "I included experimental container and day (day 1 or 2 of the experiment) as random effects"; "six separate and consecutively conducted experiments were performed"; "Although some beetles were reused in subsequent experiments" / "individuals could not be tracked between the studies."; "The UV light was produced by 9W LED UVA 395–400 nm bulbs."; "water entered via a tube at the top center of each chamber at a rate of approximately 1.5 mL/s". Discussion, verbatim: "The positive response to white light could just be a response to the red component of light emitted by those lights." The value says no more than the quote and Table 1; grade m right.

**Error (sex, light intensity and treatment order omitted).** (a) The page prints "All S. comalensis in this experiment were females (determined following Kosnicki, 2019)"; the record says nothing about sex, and the brief lists sexes among required conditions. (b) The page gives bulb wattage and the UV waveband only; no intensity, irradiance or photon flux is reported or matched across the 9 W bulbs, and no experimental temperature is given (tool summary: none found). The UV-against-white contrast therefore may carry an unmeasured intensity difference, and the record does not say so. (c) The six light types were run as "separate and consecutively conducted experiments", one light type at a time, with no stated randomisation of treatment order, on beetles partly reused without tracking; the record carries the reuse but not that treatments were sequential. Fixable.

Line 1: 1 record in error (three omissions, one category).

### Line 2, Podarcis lilfordi, sense_chemical, null to three snake odours

Results, verbatim: "Thus, P. lilfordi lizards did not recognize the odour of the potential predatory snakes of Menorca." Returned whole, 97 characters. MATCH, whole sentence, 16 words. Preceding sentence, verbatim: "There were no significant differences for any variable in the three studied populations of the Balearic lizard" (Tables 1 to 3). Tables (tool summary of rows): tongue-flick means Colom 72.75 / 74.08 / 74.79 / 69.33, Friedman P 0.765; Aire 66.25 / 69.37 / 58.13 / 69.96, P 0.244; Binicodrell 89.79 / 92.96 / 84.42 / 79.08, P 0.1098. Sixteen behavioural variables (tool summary), so "tongue-flick and 15 other" is right. Methods (tool summary): 24 lizards per population (12 males, 12 females), noosed on Menorca in summer 2013; snakes wild-caught on Menorca; absorbent paper impregnated by a snake placed in the terrarium 24 h before and removed two minutes before each trial; 15 min trials, dark room, 75 W bulb, 30 °C; each lizard got each of four treatments once in random order; Friedman tests; no positive control; no power analysis or sample-size justification. Discussion, verbatim pieces: P. siculus was "recognizing the scent of the potential predatory snake (M. mauritanicus)" with "clear antipredatory behaviours", and P. siculus differed in all variables "except for 'rubbing' and 'TF'". The record carries these. Grade m right.

**Error (population snake exposure omitted).** The page prints "Islets on which the Balearic lizard is found are snake-free except for the islet of Colom." The record names the three islets without saying two are snake-free and one (Colom) has snakes, which is the design variable that gives the null its meaning: the lack of response holds in a snake-exposed population too, not only in predator-naive ones. Fixable. Uncounted: Binicodrell's Friedman P is printed 0.1098 (record 0.110); the odour-delivery protocol (paper impregnated for 24 h, snake removed 2 min before) and the absence of a power analysis could be stated.

The null is scoped right: the value says "no recognition", the note says the paper reports no response rather than an inability to smell, and the P. siculus response to Macroprotodon shows the odour treatment was capable of eliciting behaviour in a congener under the same protocol.

Line 2: 1 record in error.

### Line 3, Pimephales promelas, sense_chemical, avoidance of copper requires olfaction

Abstract, verbatim: "The evidence demonstrates that an intact olfactory system is required for copper sensing in fish." Last Abstract sentence, returned whole. MATCH, whole sentence, 15 words; the value restates it for the species tested and adds the anosmic result from the preceding Abstract sentence ("Fish in a control group or a mock-anosmic group avoided copper," / "anosmic fish did not."), which is within one section. Results, verbatim: "but not in the anosmic group (t(13) = 1.23, p = 0.24, n = 14, df = 13, d = 0.33)"; "An n = 14 per group (the experimental unit was an individual fish) was used for the behavioural trials". Methods (tool summary): adults from a breeding colony; Otonabee River water, 3 L per maze; 20 °C; 12:12 light:dark; copper about 10 µg/L calculated, not measured; copper end by coin flip; MS-222 plus 1–2 µL tissue glue per naris, at least 24 h recovery; anosmia not verified; one-sample t tests against 0 with Holm-Bonferroni correction. Discussion: copper effect possibly "not due to copper being an odorant"; earlier whitefish avoidance attributed to a "concentration gradient of copper in the behavioral maze". Group statistics in the record match. Grade m right.

**Error (unblinded scoring, effect sizes and the between-group test omitted).** (a) The page prints "The identity of the group a fish belonged to was known to researchers at all times,"; observers were not blind to the treatment whose effect is the finding, and the record does not say so. (b) Effect sizes are printed for every group (control d = −0.97, mock-anosmic d = −1.52, anosmic d = 0.33, preliminary d = −0.85) and none is carried. (c) The claim that olfaction is "required" rests on the anosmic group's non-significant one-sample test; the paper's direct comparison, verbatim "the anosmic group was significantly different from both the mock anosmic and control group" with "F(2,39) = 1.78, p < 0.001, n = 42 (14 per group), df = (2,39)", is not carried, and the printed F and p are inconsistent with each other. Fixable.

Line 3: 1 record in error (three omissions, one category).

## Trait key

- Line 1, behaviour_vision: fits (light-side choice of whole living beetles under named wavebands).
- Line 2, sense_chemical: fits. A null belongs as a record: it is a measurement on one named species (72 lizards in three populations, each lizard exposed to every treatment), scoped by the paper to "did not recognize", and main already carries behavioural chemosensory nulls in squamates (audit/ALL.jsonl:1257, herps:95, Anolis carolinensis "no sign of detecting"). It should stay worded as no differential behavioural response to these three odours under this protocol; it is not evidence that the lizards cannot detect snake odour, and the record says so.
- Line 3, sense_chemical: fits. The owner's living-response reading is met because the measure is the behaviour of living fish, and the ablation contrast ties the response to the olfactory organ; the "pollutant injury" exclusion covers damage measured as tissue or growth injury (written for plants), and here injury is only one of the authors' candidate mechanisms for a behavioural avoidance. The record must keep the Discussion caveat (copper may act by damaging the epithelium rather than as an odorant) and the note that this is avoidance of a dissolved metal, which it does.

Trait key faults 0.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Stygoparnus comalensis, behaviour_vision, 90% dark side under UVA | error, fixable | conditions | Quote MATCH (18 words); all-female sample, unreported and unmatched light intensity, and sequential treatment order omitted |
| 2 | Podarcis lilfordi, sense_chemical, null to snake odours | error, fixable | conditions | Quote MATCH (16 words); omits that Aire and Binicodrell are snake-free while Colom has snakes |
| 3 | Pimephales promelas, sense_chemical, copper avoidance needs olfaction | error, fixable | conditions | Quote MATCH (15 words); unblinded observers, Cohen's d values and the between-group test (printed F and p inconsistent) omitted |

3 of 3 records in error (100.0%): scientific-context 3 (lines 1, 2, 3); quote-form 0; value beyond quote 0; duplicates 0; bibliographic 0; names 0; licence 0; trait key 0; grading 0.

Pooled with audits 172 to 308: 336 of 739 evidence records (45.5%; 333 of 736 before this audit, 3 of 3 here). No search records.

## Replacement text

Line 1:
- `conditions`: replace "wild-collected adults from the Comal Springs system (2023-2024);" with "wild-collected adults from the Comal Springs system (2023-2024), all female (the page: 'All S. comalensis in this experiment were females');".
- `conditions`: append "; light intensity is not reported or matched across the 9 W LED bulbs, so the UV against white contrast may include an intensity difference, and no experimental temperature is given; the six light types were run as separate consecutive experiments, one light type at a time, with no stated randomisation of treatment order".

Line 2:
- `conditions`: replace "from Colom, Aire and Binicodrell islets," with "from Colom, Aire and Binicodrell islets (Aire and Binicodrell are snake-free, Colom has snakes, so the null includes a snake-exposed population),".
- `conditions` (uncounted, optional): replace "0.110" with "0.1098"; append "; odour treatment was absorbent paper impregnated by a wild-caught Menorcan snake for 24 h, the snake removed two minutes before each trial; no positive control in P. lilfordi and no power analysis".
- `note` (uncounted): replace "(the tool printed the first author's surname with a stray accent; the page copyright line reads Mencia et al.)" with "(Crossref prints Abraham Mencía)".

Line 3:
- `conditions`: append "; observers knew each fish's group throughout (the page: 'The identity of the group a fish belonged to was known to researchers at all times'); effect sizes control d = -0.97, mock-anosmic d = -1.52, anosmic d = 0.33, preliminary d = -0.85; one-sample t tests against 0 with Holm-Bonferroni correction; the between-group comparison is printed as F(2,39) = 1.78, p < 0.001 (F and p inconsistent as printed), with the anosmic group differing from both other groups and control and mock-anosmic not differing; fish held at 20 C on 12:12 h light:dark".

## Owner questions (the unit's, answered where I could)

1. Dryopidae for Stygoparnus: confirmed by GBIF backbone (species 1033454) and the US Fish and Wildlife Service taxonomic tree (34191); consistent with main's Dryopidae rows under Coleoptera. Cyprinidae for Pimephales: main's Alachua list (GBIF key 2367742), accepted.
2. Pimephales copper avoidance under sense_chemical: yes, see Trait key; it is the behaviour of living fish with an olfactory-ablation contrast, provided the record keeps the authors' damage-versus-odorant caveat.

## Progress note

Accurate on citations, licences, names and duplicates. The Records list does not carry the faults above: Stygoparnus is given without the all-female sample and the unreported light intensity, the Podarcis null without the populations' snake status, and the Pimephales result without unblinded scoring or the between-group test. "Already on main: Stygoparnus excluded" is not supported by any string on main and should be removed or explained.

Verdict: 3 of 3 judged records in error (100.0%), above the 5% bar. Error lines: 1, 2 and 3, all fixable with the replacement text above. Pooled 336 of 739 (45.5%).

This report is model output and carries no authority.
