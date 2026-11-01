# audit-352: desk-d256, evidence lines 1 to 7

Audited 31 October 2026 from the desk-d256 files present untracked in the worktree (docs/tracks/progress/desk-d256.md and docs/views/evidence/desk-d256.jsonl, 7 lines; neither committed here, neither edited). Worktree HEAD and origin/main 6c4d6091 (desk-d255 after audit 351). `python3 -I tools/senses/check.py | grep 'd256\.'`: "docs/views/evidence/desk-d256.jsonl: 7 records, 0 problems". Quote lengths (`len(q.split())`): 20, 28, 40, 24, 18, 35, 30, all within 40 (line 3 exactly at the limit); non-ASCII in quotes only "±" (line 2) and "χ" (lines 3, 4), both as printed. Format model audits 350 and 351; desk-audit.md evidence clause (40-word limit, no 125-character limit); abutting pieces judged under the six conditions of audit-324.md, cuts under audit-331.md.

Sources opened (WebFetch): api.crossref.org/v1/works/ for all four DOIs (10.3390/insects13030220, 10.7717/peerj.13566, 10.3390/insects15060427, 10.3389/fmars.2021.719670; one pass each, all answered, none robots_disallowed); mdpi.com/2075-4450/13/3/220 (first attempt timed out on permission, then reached from a WebSearch result, two passes); peerj.com/articles/13566 (two passes) and peerj.com/articles/13566.pdf (byline only); mdpi.com/2075-4450/15/6/427 (four passes); frontiersin.org/articles/10.3389/fmars.2021.719670 (three passes); api.obis.org/v3/taxon/<name> for Paracentrotus lividus (answered), Monochamus galloprovincialis, Anthonomus pomorum and Lasioglossum villosulum (total 0, terrestrial); catalogueoflife.org taxon 7HHCG and 7HHCH (Monochamus subspecies); gd.eppo.int ANTHPO; two plazi treatment links (redirect placeholders only, no content). No curl, mirror, PMC, repository copy, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. Points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 13 WebSearch and 23 WebFetch calls used.

## Bibliographic and licence

- Lines 1, 2 (Sukovata et al., insects13030220). Crossref: Lidia Sukovata, Aleksander Dziuk, Radosław Plewa, Tomasz Jaworski; title identical; Insects 13(3) 220; issued 2022-02-22; CC BY 4.0 vor; relation empty; no update-to. Page body has no licence sentence; metadata "meta-dc.rights: https://creativecommons.org/licenses/by/3.0/". Accepted (CC BY 3.0 page vs CC BY 4.0 Crossref). Faults 0.
- Lines 3, 4 (Henneberg et al., peerj.13566). Crossref: Benjamin Henneberg, Torsten Meiners, Karsten Mody, Elisabeth Obermaier; title identical; PeerJ 10 e13566, no issue; issued 2022-07-15; CC BY 4.0, content-version unspecified; relation has-review only; no update-to. HTML page prints only "© 2022 Henneberg et al."; the publisher PDF byline prints "Benjamin Henneberg, Torsten Meiners, Karsten Mody and Elisabeth Obermaier", the record's order. Page licence: "This is an open access article distributed under the terms of the Creative Commons Attribution License,". Accepted (Crossref unspecified + page-printed Creative Commons Attribution License). Faults 0 (note updated, uncounted).
- Lines 5, 6 (Heuel et al., insects15060427). Crossref: Kim C. Heuel, Tim A. Haßlberger, Manfred Ayasse, Hannah Burger; title identical ("Floral Trait Preferences of Three Common wild Bee Species", lower-case "wild" as in Crossref); Insects 15(6) 427; issued 2024-06-06; CC BY 4.0 vor. Page byline same order; body "All articles published by MDPI are made immediately available worldwide under an open access license."; metadata CC BY 3.0. Accepted. Faults 0.
- Line 7 (Luis and Gago, fmars.2021.719670). Crossref: Orlando J. Luis, João M. Gago; title identical; Frontiers in Marine Science 8, 719670, no issue; issued 2021-10-04; CC BY 4.0 vor; relation empty. Page byline same; no licence sentence. Accepted. Faults 0.

Bibliographic faults 0; licence faults 0. source.access "open" right for all seven.

## Names

- Monochamus galloprovincialis (lines 1, 2): not in gbif-names.tsv; OBIS total 0 (terrestrial). Catalogue of Life 7HHCG lists "Monochamus galloprovincialis cinerascens Motschulsky, 1860" as an accepted infraspecific name under the species, Cerambycidae, Coleoptera (the species page itself not opened). The paper names no subspecies; species rank right. Met.
- Anthonomus pomorum (lines 3, 4): not in gbif-names.tsv; OBIS total 0; EPPO ANTHPO uses "Anthonomus pomorum" (no authority shown). Family and order printed in the paper's title "(Coleoptera: Curculionidae)". Met (accepted-status page with authority not reached; listed under Unchecked).
- Lasioglossum villosulum (lines 5, 6): not in gbif-names.tsv; OBIS total 0. The paper: "Lasioglossum villosulum belongs to the species-rich taxon of halictid bees."; Hymenoptera is never stated (tool summary), so the order rests on main's Halictidae row, as the note says. Plazi treatment titles in search results read "Lasioglossum (Hemihalictus) villosulum (Kirby, 1802)" (pages themselves did not load). Met (listed under Unchecked).
- Paracentrotus lividus (line 7): gbif-names.tsv:3555 EXACT ACCEPTED; OBIS 124316 "Paracentrotus lividus" "(Lamarck, 1816)", accepted, class Echinoidea, order Camarodonta, family Parechinidae. Owner question answered: Parechinidae confirmed. The paper gives no family or order (title "(Echinodermata: Echinoidea)"). Met.

Name faults 0.

## Duplicates

git grep on origin/main (6c4d6091) across the whole docs/ tree (evidence, audit incl. audit/corrected and audit/ALL, sheets, searched, gaps, wanted, progress) for each DOI suffix (insects13030220, peerj.13566, 13566, insects15060427, fmars.2021.719670, 719670), first authors (Sukovata, Henneberg, Heuel, Luis), and each binomial (galloprovincialis, pomorum, villosulum, Paracentrotus lividus); then the branch-only additions (`git diff origin/main...<branch>`) of every remote branch matching origin/research/desk-d2* or origin/research/audit-3*; and the audit-3*.md hold-outs.

- insects13030220 on main only as a searched/harvest-c22b screened entry (Reseda row); galloprovincialis only in a wanted row of a different paper (Szmigielski et al. 2012, volatiles). pomorum only in searched/harvest-36 (Polydrusus rows). villosulum absent. Paracentrotus lividus on main as acuity_cpd (sea-invertebrates:225, corrected row) only; 719670 only in desk-d218.md as a held lead. Henneberg on main is a different person (Lorenz Henneberg, a germination paper).
- Branches: desk-d218 (the d218 hold note for 719670), desk-d228 and desk-d230 (Paracentrotus named as not retried / not readable), desk-d256 itself. No audit-3*.md names any of these DOIs or species.
- Lines 1 and 2 are not duplicates of each other (2019 and 2020 experiments, different colour sets, different values); lines 3 and 4 are separate comparisons (twig v control, twig v twig); lines 5 and 6 different traits.

Duplicates 0.

## Trait keys and rulings

- behaviour_vision, lure-baited colour traps (lines 1, 2): acceptable on the audit-351 line 6 footing (lure identical across colours, colour the manipulated variable, catch outcome stated). The lure confound is disclosed. What is not disclosed, and is required: the authors "did not measure the reflectance of the coroplast painted using acrylic spray paints of different colors" (colours rest on theoretical RAL values, Table 1), and painted vanes carry paint plus PTFE treatment while the reference is unpainted coroplast; in 2020 painted pure white caught significantly fewer beetles than unpainted white, so the surface treatment itself changes catches. This is the calculated-vs-measured stimulus and intensity-matching confound of the rules.
- sense_chemical, twig-odour dual choice (lines 3, 4): acceptable (volatiles from living twigs, still-air arena, control v blank run). The odour source being plants does not make this a plant record; the taxon is the weevil.
- behaviour_vision and sense_chemical, flight-cage first choices (lines 5, 6): acceptable. Wild: "placed above a nesting aggregation in the Botanical Garden of the University of Ulm" (the bees are the free-flying aggregation's females, not a colony product). Total n ruling: no total number of bees or choices for L. villosulum is printed in the text or any figure caption (Figure 6 gives n only for the other two species' depth test: "Bombus: 9 runs in 2 colonies, Osmia: 6 runs."); only "approximately 30 female bees of the relevant species were active in the flight cage" and "repeated three to four times because of low participation numbers", unmarked bees ("some individuals might have participated in more than one experiment"). The records disclose all of this; fileable with the disclosure, the n gap left to the supplement (Unchecked).
- sense_chemical, contact chemoreception (line 7): acceptable (dissolved compounds on cloth simulacra placed among the spines, stimulus v blank on the same urchin).
- Grade `m` right for all seven.

## Per-record findings

### Line 1, Monochamus galloprovincialis, 2019 null

Results sentence verbatim in one piece: "We found no significant difference in the catches of M. galloprovincialis of either sex when compared to the white traps." **Quote MATCH**, 20 words; value says no more (the colour list is the 2019 design).

Verified, verbatim: "Traps were set up in a randomized complete block design across 14 blocks (replicates)"; "each block containing one of each color variant."; "Traps within and between blocks were separated by approximately 100 m."; "They were suspended on metal hooks from dead branches on trees, 4–6 m above the ground,"; "The traps were baited with Galloprotect Pack lures (SEDQ, Barcelona, Spain),"; "Traps were set on 24 and 25 June and checked and emptied on 1 and 9 July."; GLMM "with a Conway–Maxwell–Poisson, a generalized Poisson, or a negative binomial distribution"; "The block was considered as a random factor."; Wald 𝜒2; Dunnett against unpainted white (tool summary); "𝛼 = 0.05"; "The catches of females (40.7 ± 4.50 beetles/trap, i.e., estimated marginal mean ± SE)"; "beetles were least numerous in the cyan blue traps (28.7 ± 3.65 beetles/trap"; males 4.6 ± 0.88 to 6.2 ± 1.08.

Misstated or not carried, verbatim: 2019 site: "The studies were conducted in the Międzychód FD (N 52.6794, E 15.6944)," in two 83-year-old pine stands (tool summary for the stand age); Wronki FD enters only in 2020, while the record places the 2019 trial in both districts. Paint and reflectance: "the vanes were painted twice with mattish ColorMatic acrylic spray paints," then PTFE, "the treated surfaces appeared shiny, due to the presence of mineral oil in the lubricant composition."; "we did not measure the reflectance of the coroplast painted using acrylic spray paints of different colors." The means are model estimates ("estimated marginal mean ± SE"), not raw means; both sexes "(46.8 ± 4.87 beetles/trap) in the unpainted white traps were slightly higher than in the other traps". Unverified: "pure Scots pine" (the text read says pine stands; left unchanged).

**Error (site misstated; unmeasured reflectance and paint/PTFE surface confound omitted).** Fixable.

### Line 2, Monochamus galloprovincialis, 2020 unpainted white highest

Results sentence verbatim in two abutting pieces, twice ("The unpainted white traps captured the highest numbers of females (14.0 ± 2.32 beetles/trap)," | "males (4.7 ± 1.11 beetles/trap), and beetles of both sexes (18.6 ± 3.08 beetles/trap)."). **Quote MATCH**, 28 words.

Value says more than the quote: "trap colour had a significant effect on females, males and totals (p < 0.0001, 0.0079, < 0.0001)" comes from a different sentence ("the trap color had the significant effect on the catches of M. galloprovincialis females (𝜒2 = 36.6, df = 5, p < 0.0001)"; males "(𝜒2 = 15.6, df = 5, p = 0.0079)"; totals "(𝜒2 = 29.5, df = 5, p < 0.0001)"); the statistics are already in conditions and must leave the value.

Verified, verbatim: "The experiment was conducted in the Międzychód FD (N 52.6684, E 15.8630) and Wronki FD (N 52.7608, E 16.2576),"; "Traps were deployed on 29 and 30 June, and then checked and emptied on 15 and 29 July."; colours deep orange, light blue, pine green, jet black, pure white, unpainted white; female differences "light blue traps," "pure white traps, and pine green traps (5.3 ± 1.12, 5.6 ± 1.15, and 6.6 ± 1.30 beetles/trap, respectively)"; jet black "(8.9 ± 1.61 beetles/trap) was nearly significant (p = 0.0528)."; "the catches of M. galloprovincialis males were significantly lower only in the pure white and light blue traps".

Misstated or not carried, verbatim: design: "Color treatments were tested in 10 blocks, and two block conformations were used, either 3 × 2 or 6 × 1, as dictated by the terrain relief."; "The materials and experimental design were similar to those used in 2019." (2020 spacing and within-block placement not stated; the record states the 2019 design as if measured for 2020). Paint: glossy acrylic paints, twice, then dry PTFE twice; "the final color looked rather yellowish" for pure white (tool summary for the paint brands); reflectance unmeasured (sentence quoted under line 1); the "lower-reflection series" is the authors' choice of "orange, blue, and green colors with lower reflectance values than those tested in 2019", from theoretical values. Means are estimated marginal means (units say "mean"). Laboratory two-plate tests: "Surprisingly, none of the colors tested appeared more attractive than the unpainted white coroplast." (not used, uncounted).

**Error (value exceeds quote; unmeasured reflectance and paint/PTFE confound omitted; 2020 block layout misstated).** Fixable.

### Line 3, Anthonomus pomorum, M. sylvestris v control preferred, M. domestica null

Results sentence, two passes, the second asked for punctuation explicitly: "Weevils that were tested in bioassays for their preference for volatiles from apple blossom buds versus controls, significantly preferred M. sylvestris (χ2 = 6.53; p = 0.01), but not M. domestica over the controls (χ2 = 0.57; p = 0.45)." The tool confirmed "a comma follows" after "versus controls" and after "(χ2 = 6.53; p = 0.01)". The record's quote drops both commas. **Quote error (two commas dropped)**; 40 words with or without them. Value says no more; the M. domestica null is carried.

Verified, verbatim: "The study was conducted in 2017 in the Ecological-Botanical Garden of the University of Bayreuth"; "As many post-diapause A. pomorum imagines as possible were collected from M. domestica trees by limb-jarring"; "from mid-March to mid-April."; "Olfactory bioassays were performed as still-air dual-choice experiments in plastic Petri dishes"; "Two holes (10 mm diameter, 70 mm apart)"; "or an appropriate control in the form of a model of an apple twig made out of wire."; "Conditions in the test chamber were kept constant at 16 °C and 70% RH."; "the weevils were deprived of food for 24 h"; "and allowed to acclimatize to the conditions in the test chamber for 90 min."; "Bioassays were run for 180 min, after which the choice of each weevil was recorded"; "Each weevil was only used once in bioassays."; "New apple twigs and a clean Petri dish were used for each bioassay."; "was assessed against controls (n = 50)"; "the controls were also tested against blanks (n = 30)"; "one-sample chi2 tests"; responsiveness "(56–62%)" and "(23.3%)"; control v blank "(χ2 = 0.14; p = 0.71)". No randomisation or position switching and no choice-zone definition in the text (tool, twice). All as recorded. Unverified: twig length and bud count, sex not recorded (left).

Uncounted additions: twigs came from "a subset of the individuals used for the infestation analysis", M. domestica cultivars "“Roter Boskoop”, “Blauacher Wädenswil”, and “James Grieve”" and M. sylvestris genotypes "“Destuben”, “Schlehenmühle”, and “Lochau 2”"; the weevils' collection host (M. domestica) is a prior-experience point worth naming in the "not naive" clause.

**Error (quote punctuation).** Fixable.

### Line 4, Anthonomus pomorum, M. sylvestris over M. domestica

Results sentence verbatim (punctuation pass): "Likewise, weevils that could choose directly between odors from M. domestica and M. sylvestris, significantly preferred M. sylvestris (χ2 = 3.90; p = 0.048)." The tool confirmed the comma after "M. domestica and M. sylvestris"; the record's quote drops it. **Quote error (comma dropped)**, 24 words. n verified: "Twigs of M. domestica and M. sylvestris were also compared directly in bioassays" "so that weevils could choose between the two host-plant species (n = 50)." Design as line 3. Value says no more.

**Error (quote punctuation).** Fixable.

### Line 5, Lasioglossum villosulum, yellow over blue

Results 3.1.2 sentence verbatim in one piece, twice: "Lasioglossum villosulum (p < 0.001) and B. terrestris (p < 0.001) both strongly preferred yellow over blue flowers." **Quote MATCH**, 18 words; value says no more.

Verified, verbatim: "placed above a nesting aggregation in the Botanical Garden of the University of Ulm."; "Experiments were undertaken when approximately 30 female bees of the relevant species were active in the flight cage."; "between 8 am and 1 pm during the years 2022 and 2023."; "except in L. villosulum experiments, which were repeated three to four times because of low participation numbers."; "some individuals might have participated in more than one experiment."; "three pairs of artificial flowers of one type were placed on a wooden board."; "the board was turned by 90° every 10 min."; "Artificial flowers were renewed every 20 min."; "First, we built one binomial generalized linear model (GLM) per tested trait, resulting in a total of five global models."; "resulting in a similar achromatic contrast (blue: 0.217 units; yellow: 0.234 units)."; "had a color angle of 146°."; "The blue cardboard showed almost maximum opposition".

Misattributed and not carried, verbatim: the contrast caveat is the authors' reading of the bumblebee result ("However, they did prefer yellow over blue artificial flowers," "a result that might be explained by the slightly higher contrast of yellow artificial flowers" "against the provided green background.", after "In our experiments, B. terrestris bees were not trained prior to testing."), not a statement about L. villosulum; and the species' own achromatic-contrast test is omitted: "For L. villosulum, we found no preference when analyzing all interactions (p = 0.227)" and "there was a preference for yellow over light-yellow artificial flowers (p = 0.0121)". The bee responds to achromatic differences, so the unmatched contrast (0.217 v 0.234) is a live confound for this record; the record gives the numbers but attributes the caveat wrongly and leaves out the evidence that makes it consequential.

**Error (intensity-matching confound misattributed, species' contrast result omitted).** Fixable. `where` "Results 3.1, hue" is the parent section; the sentence is under "3.1.2. Color Hue Preferences" (uncounted).

### Line 6, Lasioglossum villosulum, scent-complexity null

Results 3.2.1 sentence verbatim in two abutting pieces ("We did not observe a general preference of any of the species for the complex mixture over the simple mixtures" | "(O. bicornis: p = 0.429; L. villosulum: p = 0.269; B. terrestris: p = 0.197)."), same join on the hue/scent passes. **Quote MATCH**, 35 words; value says no more (compound counts are design).

Verified, verbatim: "The complex mixture contained all 12 VOCs, whereas the three simple mixtures contained 4 VOCs out of the 12"; "an aliquot of 30 µL of the dilution (30 ng substance) was applied per artificial flower"; "For the ‘scent’ model, we added the mixture (mix 1, 2, or 3) as a random factor into our models."; "6 antennae of L. villosulum, all from different females, were tested."; "Only 66% of the L. villosulum antennae exhibited electrophysiological activity for myrcene in mixture 3."; "Most of the 12 tested VOCs were electrophysiologically active in all tested antennae of the wild bee species." No per-mixture behavioural result for L. villosulum (tool summary). Design and n disclosure as line 5; the record's own caveat on the null is right.

`where` wrong: there is no Results 3.4; the headings are "3.2. Preferences for Scent Complexity and Antennal Responses to Scents" and "3.2.1. Scent Complexity Preferences", and the sentence sits under 3.2.1. "most other compounds responded in all antennae" slightly overstates "Most of the 12 tested VOCs" (uncounted wording fix).

**Error (locator field false).** Fixable.

### Line 7, Paracentrotus lividus, soluble starch over blank

Results sentence verbatim in two abutting pieces ("However, regardless of diet, when soluble starch was the tested stimulus, the sea urchins clearly showed a preference" | " for the respective simulacrum relative to the blank one (*P* < 0.05)."), consistent with the desk's join. **Quote MATCH**, 30 words.

Value says more than the quote: the nulls ("glucose, sucrose, olive oil and a 22-amino acid mixture did not differ from blanks (P > 0.05)") come from the preceding sentence "This was the case for the 22-amino acid mixture, olive oil, sucrose, and glucose (*P* > 0.05)." (the note calls it "the next sentence"); they are already in conditions and must leave the value.

Verified, verbatim: "Each chemical stimulus, glucose 10% (Merck, Darmstadt, Germany), soluble starch 10% (Darmstadt, Germany), " "sucrose 10% (cane sugar), olive oil 10%, and a 22-amino acid 1 mM mixture, was tested on 30 sea urchins" " from each of the three diets as well as on an equal number of wild sea urchins recollected 15 days prior to testing" " and were kept unfed."; "(N = 150 sea urchins under each dietary regime)"; "Responsiveness to each chemical stimulus was analysed by the χ2 tests, and within responses, preference for one" " or the other simulacrum was compared using binomial tests."; "In the first case, only behaviours involving the transportation of simulacra to the mouth were compared,"; following sentence "Blank simulacra, irrespective of sea urchin diet, were chosen as frequently as stimulus-carrying simulacra," " except when this was starch."; Cabo Raso, Cascais, September, 40 to 50 mm test diameter, 8 months on maize, kombu or both, sex and position randomisation not reported (tool summary); 41 stimuli with 30 carried to the mouth more often than blanks and sucrose among the nine like blanks (tool summary of Table 4 and text). Wild-collected, not farmed.

Misstated or not carried, verbatim: the first sentence of the subsection is "The frequency of feeding responses is independent of the kind of chemical stimulus presented (*P* > 0.05, df = 3)," " but is clearly dependent on the nutritional state of the sea urchins (*P* < 0.001, df = 3)." (the record says it is about stimuli being chosen indistinguishably); "When fed with seaweed fronds exclusively, the sea urchins showed a greater response frequency toward simulacra " "(either test and/or blank) than those fed with any of the other diets tested or even the unfed ones (*P* < 0.001, df = 1)." (significant diet effect omitted); "In many instances, the sea urchins did not convey any of the presented simulacra to the mouth." The units' "simulacrum chosen" should name the scored response (carried to the mouth).

**Error (value exceeds quote; significant diet effect on responsiveness omitted and first sentence misreported).** Fixable.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Monochamus galloprovincialis, 2019 null | error, fixable | conditions | quote MATCH (20 words); 2019 in Międzychód only; reflectance unmeasured, paint/PTFE surface confound; EMMs |
| 2 | Monochamus galloprovincialis, 2020 white highest | error, fixable | value, units, conditions | quote MATCH (28 words); colour-effect p values not in the quote; reflectance unmeasured, painted v unpainted white; 2020 block layout |
| 3 | Anthonomus pomorum, M. sylvestris v control | error, fixable | quote, conditions, note | two printed commas dropped; byline confirmed on publisher PDF |
| 4 | Anthonomus pomorum, M. sylvestris v M. domestica | error, fixable | quote, conditions | printed comma dropped |
| 5 | Lasioglossum villosulum, yellow over blue | error, fixable | conditions, where | quote MATCH (18 words); contrast caveat is the authors' B. terrestris reading; species' contrast-test result (p = 0.0121) omitted |
| 6 | Lasioglossum villosulum, scent null | error, fixable | where, conditions | quote MATCH (35 words); no Results 3.4 (sentence under 3.2.1) |
| 7 | Paracentrotus lividus, starch over blank | error, fixable | value, units, conditions, note | quote MATCH (30 words); nulls in value come from another sentence; diet effect on responsiveness omitted |

Errors 7 of 7 records (100%), above the 5% bar: scientific-context 4 (lines 1, 2, 5, 7: calculated-vs-measured/intensity-matching stimulus 3 on lines 1, 2, 5; significant result omitted 1 on line 7; site/design misstated on lines 1 and 2 within the same lines); value exceeds quote 2 (lines 2, 7); quote 2 (lines 3, 4, punctuation); locator 1 (line 6); bibliographic 0; licence 0; names 0; duplicates 0 against main, all desk-d2* and audit-3* branches and the audit-3* hold-outs; grading 0. HOLD OUT: none. Lines 3, 4 and 6 are minor faults; lines 1, 2, 5 and 7 carry substantive omissions.

Answers to the desk-d256 owner questions.
1. Lured-trap catches by trap colour under behaviour_vision: acceptable (lure constant across colours, as audit 351 line 6), provided the records say the painted traps' reflectance was not measured and that painted and unpainted surfaces differ.
2. Anthonomus twig-odour dual choice under sense_chemical: keep.
3. Lasioglossum villosulum: order Hymenoptera from main's Halictidae row is acceptable (the paper never states it); flight-cage tests over a wild nest aggregation count as wild.
4. Paracentrotus lividus family: Parechinidae, Camarodonta, Echinoidea on OBIS 124316.

## Unchecked

- Lines 1, 2: "pure Scots pine" stands; Table 1 theoretical reflectance values; Supplementary Table S2 (raw totals); whether the unpainted reference vanes were PTFE-treated; the Introduction's printed family/order (Catalogue of Life used instead).
- Lines 3, 4: twig length and bud count; whether sex was recorded; the choice zone; per-test numbers of responders.
- Lines 5, 6: the supplement (possible n of choices); reflectance spectra; accepted-name page with authority for L. villosulum (plazi pages did not load).
- Line 4/3: accepted-name page with authority for A. pomorum (EPPO gives the name only).
- Line 7: the heading "Contact Food Detection"; Table 4 per-stimulus counts; the year of collection (not printed in the text read).

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file; the joined replacements leave all quotes within 40 words). Empty new string deletes the old string.

- Line 1, `conditions`: "(Poland, Międzychód and Wronki Forest Districts);" -> "(Poland; the 2019 experiment in two 83-year-old pine stands of Międzychód Forest District only, the 2020 experiment in Międzychód and Wronki Forest Districts);"
- Line 1, `conditions`: "Trap counts are a capture outcome," -> "Trap colour was set by painting the coroplast vanes (2019: twice with mattish acrylic spray paints, then a PTFE treatment that left the surfaces shiny); the authors did not measure the reflectance of the painted traps and give only theoretical colour values, so brightness and UV reflectance were neither matched nor measured, and painted traps differ from the unpainted white reference in surface as well as colour. Trap counts are a capture outcome,"
- Line 1, `conditions`: "Mean females 40.7 +/- 4.50 per white trap," -> "Estimated marginal means +/- SE: females 40.7 +/- 4.50 per white trap,"
- Line 1, `conditions`: "mean males 4.6 +/- 0.88 (cyan blue) to 6.2 +/- 1.08 (pastel yellow)." -> "males 4.6 +/- 0.88 (cyan blue) to 6.2 +/- 1.08 (pastel yellow); both sexes 46.8 +/- 4.87 in unpainted white traps, slightly higher than in the other traps."
- Line 2, `value`: "; trap colour had a significant effect on females, males and totals (p < 0.0001, 0.0079, < 0.0001)" -> ""
- Line 2, `units`: "beetles per trap (mean +/- SE); Wald chi-square p values for colour" -> "beetles per trap (estimated marginal mean +/- SE)"
- Line 2, `conditions`: "Randomized complete block design, one trap of each colour per block, traps about 100 m apart; the text does not say how colours were placed within a block." -> "The 2020 materials and design are said to be similar to 2019 (randomized complete block design, one trap of each colour per block, traps about 100 m apart); in 2020 the 10 blocks were laid out 3 x 2 or 6 x 1 as the terrain dictated, and 2020 spacing and within-block placement are not stated."
- Line 2, `conditions`: "Trap counts are a capture outcome," -> "Vanes were painted twice with glossy acrylic paints and treated twice with dry PTFE, and the pure white looked rather yellowish on the traps; the authors did not measure the reflectance of the painted traps, so brightness and UV reflectance were neither matched nor measured; painted pure white caught significantly fewer females and males than unpainted white, so painting changed catches apart from hue. Trap counts are a capture outcome,"
- Line 2, `conditions`: "(the lower-reflection series)" -> "(chosen as colours with lower theoretical reflectance values than those of 2019, not measured)"
- Line 3, `quote`: "versus controls significantly preferred M. sylvestris (χ2 = 6.53; p = 0.01) but not" -> "versus controls, significantly preferred M. sylvestris (χ2 = 6.53; p = 0.01), but not"
- Line 3, `conditions`: "so field-collected, not naive" -> "so field-collected from M. domestica, not naive"
- Line 3, `note`: "PeerJ page text gave only Henneberg et al." -> "PeerJ page text gave only Henneberg et al.; the publisher PDF byline prints Benjamin Henneberg, Torsten Meiners, Karsten Mody and Elisabeth Obermaier in this order (audit 352)"
- Line 4, `quote`: "M. domestica and M. sylvestris significantly preferred" -> "M. domestica and M. sylvestris, significantly preferred"
- Line 4, `conditions`: "so field-collected, not naive" -> "so field-collected from M. domestica, not naive"
- Line 5, `conditions`: "so the authors note yellow's slightly higher contrast may add to the preference." -> "and the authors offer yellow's slightly higher contrast against the green background as a possible explanation of the B. terrestris yellow preference, a difference that applies equally to this test; in the same paper's achromatic-contrast test L. villosulum showed no overall preference (p = 0.227) but preferred yellow over light-yellow flowers (p = 0.0121), so achromatic contrast may contribute to its yellow choice."
- Line 5, `where`: "Results 3.1, hue" -> "Results 3.1.2, Color Hue Preferences"
- Line 6, `where`: "Results 3.4, scent complexity" -> "Results 3.2.1, Scent Complexity Preferences"
- Line 6, `conditions`: "most other compounds responded in all antennae." -> "most of the 12 compounds were active in all tested antennae of the wild bee species."
- Line 7, `value`: "; glucose, sucrose, olive oil and a 22-amino acid mixture did not differ from blanks (P > 0.05)" -> ""
- Line 7, `units`: "categorical (simulacrum chosen, binomial and chi-square tests; contact chemoreception of dissolved compounds)" -> "categorical (simulacrum carried to the mouth, stimulus versus blank by binomial test within responses; responsiveness by chi-square; contact chemoreception of dissolved compounds)"
- Line 7, `conditions`: "The first sentence of the same Results passage says that for most stimuli the urchins chose test and blank simulacra indistinguishably, and the sentence ending" -> "The first sentence of the same Results passage says that the frequency of feeding responses was independent of the stimulus (P > 0.05, df = 3) but clearly dependent on nutritional state (P < 0.001, df = 3); urchins fed only kombu fronds responded more often than those on any other diet or unfed ones (P < 0.001, df = 1); in many instances the urchins carried neither simulacrum to the mouth; and the sentence ending"
- Line 7, `note`: "The nulls come from the next sentence, not the quote." -> "The nulls come from the preceding sentence, not the quote, and are carried in conditions only."
