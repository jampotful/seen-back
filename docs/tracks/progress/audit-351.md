# audit-351: desk-d255, evidence lines 1 to 7

Audited 31 October 2026 from the desk-d255 files present untracked in the worktree (docs/tracks/progress/desk-d255.md and docs/views/evidence/desk-d255.jsonl, 7 lines; neither committed here, neither edited). Worktree HEAD and origin/main c1e7dd86 (desk-d254 after audit 350). `python3 -I tools/senses/check.py | grep 'd255\.'`: "docs/views/evidence/desk-d255.jsonl: 7 records, 0 problems". Quote lengths (`len(q.split())`): 40, 27, 26, 29, 30, 22, 23, all within 40 (line 1 exactly at the limit); non-ASCII only "…" (twice) and "°" (twice) in line 1, both checked against the page. Format model audits 349 and 350; desk-audit.md evidence clause (40-word limit, no 125-character limit); abutting pieces judged under the six conditions of audit-324.md, cuts under audit-331.md.

Sources opened (WebFetch): api.crossref.org/v1/works/ for all six DOIs (10.3390/fishes8120596, 10.3389/fmars.2022.1036979, 10.3390/insects13110993, 10.3389/fevo.2022.838076, 10.3390/insects17040354, 10.3389/fevo.2021.786557; one pass each, all answered, none robots_disallowed); mdpi.com/2410-3888/8/12/596 (one pass); frontiersin.org fmars.2022.1036979 (two passes); mdpi.com/2075-4450/13/11/993 (two passes); frontiersin.org fevo.2022.838076 (two passes); mdpi.com/2075-4450/17/4/354 (two passes); frontiersin.org fevo.2021.786557 (three passes); mammaldiversity.org/taxon/1001261 (Cryptomys pretoriae) and /taxon/1001257 (Cryptomys hottentotus); api.obis.org/v3/taxon/<name> for Pseudopleuronectes yokohamae, Sebastes schlegelii, Gadus morhua, Culex pipiens, Calonectris borealis (answered) and Cydia pomonella (total 0). The query form api.obis.org/v3/taxon?scientificname=<name> failed four times (client_error); the path form answered and is what audit 331 used; no other workaround. No curl, mirror, PMC, repository copy, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 1 WebSearch and 30 WebFetch calls used.

## Bibliographic and licence

- Line 1 (Schakmann et al., fishes8120596). Crossref: Mathias Schakmann, Emil Aputsiaq Flindt Christensen, John Fleng Steffensen, Morten Bo Søndergaard Svendsen; title identical; Fishes 8(12) 596; issued 2023-12-02; CC BY 4.0 vor; relation empty; no update-to. Page licence "This article is an open access article distributed under the terms and conditions of the Creative Commons" "Attribution (CC BY) license". Accepted. Faults 0.
- Lines 2 and 3 (Yu et al., fmars.2022.1036979). Crossref: Mengjie Yu, Changdong Liu, Liyou Zhang, Yanli Tang; Frontiers in Marine Science 9, 1036979, no issue; issued 2022-11-28; CC BY 4.0 vor. Crossref title not returned verbatim (length); page title verbatim in two pieces ("Application of light-emitting diodes (LEDs) fishing lights to improve catch rates of small-scale trammel net" | " fishery in the Yellow Sea, China"), identical to the record; byline same order. No licence sentence on the page. Accepted (page without licence sentence + Crossref CC vor). Faults 0.
- Line 4 (Hellhammer et al., insects13110993). Crossref: four authors in the record's order; title identical; Insects 13(11) 993; issued 2022-10-29; CC BY 4.0 vor. Page: MDPI's generic "open access Creative Common CC BY license" sentence. Accepted. Faults 0.
- Line 5 (Lutermann et al., fevo.2022.838076). Crossref: Heike Lutermann, Kemba B. Butler, Nigel C. Bennett; title identical; Frontiers in Ecology and Evolution 10, 838076, no issue; issued 2022-03-03; CC BY 4.0 vor. No licence sentence on the page. Accepted. Faults 0.
- Line 6 (Knight and Basoalto, insects17040354). Crossref: Alan Lee Knight, Esteban Basoalto; title identical; Insects 17(4) 354; issued 2026-03-24; CC BY 4.0 vor. Page metadata CC BY 3.0, no licence sentence in the body (tool summary). Accepted (CC BY 3.0 page vs CC BY 4.0 Crossref). Faults 0.
- Line 7 (Rodríguez et al., fevo.2021.786557). Crossref: Airam Rodríguez, Beneharo Rodríguez, Yarci Acosta, Juan J. Negro; title identical; Frontiers in Ecology and Evolution 9, 786557; issued and published online 2022-01-18 (volume 9 is the 2021 volume, the DOI says 2021; the record's 2022 follows the issued date; the page's printed year was not separately read, uncounted). CC BY 4.0 vor; no licence sentence on the page. Accepted. Faults 0.

Bibliographic faults 0; licence faults 0. source.access "open" right for all seven.

## Names

- Gadus morhua (line 1): not in gbif-names.tsv; OBIS 126436 "Gadus morhua Linnaeus, 1758", accepted, Gadidae, Gadiformes. Met.
- Sebastes schlegelii (line 2): not in gbif-names.tsv; OBIS 274849 "Sebastes schlegelii Hilgendorf, 1880", accepted, Sebastidae, Perciformes (as main's sense_hearing row). Met.
- Pseudopleuronectes yokohamae (line 3): not in gbif-names.tsv; OBIS 275360 "Pseudopleuronectes yokohamae (Günther, 1877)", accepted, family Pleuronectidae, order Pleuronectiformes. The record's family and order are right; the note's family-level route (Hippoglossus row) is superseded by this species-level source (note replacement, uncounted). Owner question answered: Pleuronectiformes, not Carangiformes, on OBIS.
- Culex pipiens (line 4): gbif-names.tsv:1312 "Culex pipiens molestus EXACT ACCEPTED Culex pipiens" (an accepted subspecies rolled to the species, not a synonym as the note says, uncounted); OBIS 1629456 accepted, Culicidae, Diptera. One form (biotype molestus) from two northern German collections, not a pooled complex; species-rank filing follows audits 315 and 333 and main's desk-d225:8. Laboratory strain accepted at species rank (audit 332 ruling). Met.
- Cryptomys hottentotus (line 5): **error.** The animals are highveld mole-rats from suburban Pretoria; the paper's Introduction and Table 1 footnote name them C. h. pretoriae (the Abstract says "highveld mole-rat (Cryptomys hottentotus hottentotus)", an internal conflict). MDD 1001261: "Cryptomys pretoriae" "(A. Roberts, 1913)", "Highveld Mole-rat", Bathyergidae, Rodentia, type locality "Skinners Court Valley, Pretoria, South Africa.", note "split from C. hottentotus". MDD 1001257 (C. hottentotus, "Common Mole-rat") says the species "previously included natalensis, mahali, pretoriae, and nimrodi". The common name, the locality (the pretoriae type locality) and the paper's own subspecies name all place these animals in C. pretoriae; filing under C. hottentotus files a pre-split name. Fixable: taxon Cryptomys pretoriae (not on main or in gbif-names.tsv), family and order from MDD, with the Abstract's conflicting name disclosed. MDD also says the Cryptomys synonymy "is highly tentative"; the owner may prefer to hold the line out instead.
- Cydia pomonella (line 6): gbif-names.tsv:1346 EXACT ACCEPTED; Tortricidae, Lepidoptera on main; OBIS returned no record (terrestrial). Met.
- Calonectris borealis (line 7): not in gbif-names.tsv; OBIS 1348497 "Calonectris borealis (Cory, 1881)", accepted, Procellariidae, Procellariiformes; the paper uses "Cory's shearwater (Calonectris borealis)". Met. The note's "main has only the congener Calonectris diomedea" is wrong: main has two C. borealis behaviour_vision rows (oa-13b.jsonl:409, 410, Atchoi et al. 2024 y-maze, jeb.247665) with Procellariidae, Procellariiformes (uncounted note fault; different paper, so no duplicate).

Name faults 1 (line 5).

## Duplicates

git grep on origin/main (c1e7dd86) across the whole docs/ tree (evidence, audit incl. audit/corrected and audit/ALL, sheets, searched, gaps, wanted, progress) for each DOI suffix (fishes8120596, 1036979, insects13110993, 838076, insects17040354, 786557), first authors (Schakmann, Hellhammer, Lutermann, Knight/Basoalto, "Airam Rodr"), Mathevotaenia and pretoriae, and for each binomial with its traits; then the branch-only additions (`git diff origin/main...<branch>`) of all 128 remote branches matching origin/research/desk-d2* or origin/research/audit-3* for the same strings; and the audit-3*.md hold-outs.

- No DOI of this unit is on main or on any other branch except research/desk-d255 itself; the audit-32 to 38 branch hits are "Knight" in unrelated rows. "Airam Rodr" on main matches only the Atchoi et al. 2024 wanted row and its oa-13b evidence (a different paper). pretoriae on main only in a desk-d215 progress line naming another Cryptomys paper.
- Species and traits on main: Gadus morhua sense_hearing only; Sebastes schlegelii sense_hearing only; Pseudopleuronectes yokohamae absent; Culex pipiens acuity_cpd (canon-4, molestus and pipiens), lambda_max_nm (desk-d225), sense_hearing (desk-d239), no behaviour_vision; Cryptomys hottentotus vision traits only; Cydia pomonella vision traits and diel, no behaviour_vision; Calonectris borealis behaviour_vision from Atchoi et al. (different paper). No audit-3* hold-out names any of these DOIs.

Duplicates 0.

## Trait keys and rulings

- sense_thermal (line 1): owner question. Main files gradient Tpref under sense_thermal (desk-d230 Phymaturus; audit 350 lines 7, 8). This paper's Tpref is not a gradient choice: one tank whose whole water body was warmed stepwise, Tpref "determined ... as the local minima in activity along the temperature gradient" of a calculated core temperature. It is still a behavioural thermal response and fileable under sense_thermal, but the record must not call it a selected temperature (error below).
- behaviour_vision, fishing gear (lines 2, 3): acceptable as filed, on the audit-350 footing for the Chelonia nets (defined LEDs at the net, peak wavelengths and intensity given, CPUE against unlit nets, the record saying it is a catch outcome).
- behaviour_vision, lured traps (line 6): acceptable; moth lamp-spectrum comparisons are behaviour findings (rules), and the lure confound is disclosed.
- behaviour_vision, lab feeding choice (line 4): acceptable (colour choice with positions rotated), with the ink-odour and brightness confounds disclosed (error below).
- sense_chemical, mate-choice odour (line 5): acceptable; a discrimination between two urine odours by time spent, like main's predator-odour preference rows; no threshold claimed.
- behaviour_vision, grounding vs satellite light (line 7): **not fileable as filed; HOLD OUT.** The "stimulus" is upward night-time radiance from VIIRS composites along each track ("as a proxy of light pollution", units not stated), not light at the bird; the analysis is a univariate binomial GLM on 43 tracks ("Given our sample size (n = 43), we ran univariate GLMs to avoid overparameterization."), so light pollution is not adjusted for flight straightness and speed, which also predicted grounding and which themselves varied with light ("Flights were more tortuous with high light pollution levels"); there is no lamp, no manipulation and no unlit comparison. This is a behavioural correlate without a defined stimulus at the animal, the same footing on which audit 350 held out the porpoise deterrent line (audits 317, 344, 345). Main's C. borealis behaviour_vision rows are y-maze choices with defined lights, which is the usage this record does not meet.
- Grade `m` right for all seven.

## Per-record findings

### Line 1, Gadus morhua, Tpref 6.4 to 18.7 C

Results sentence verbatim in three abutting pieces in one response ("We experimentally determined the temperature preference (Tpref) of 29 Atlantic cod (Gadus morhua) ranging from 4 g to 2625 g" | "and found that Tpref ranged from 6.4 °C to 18.7 °C and correlated negatively with fish body mass in a logarithmical fashion" | "(Figure 3; one-way ANOVA, F(1) = 119.527, p < 0.001)."). The two cuts drop the mass range (carried in conditions) and the figure reference and F statistic; neither is a qualifier of the range (audit-331 conditions met); "6.4 °C" spacing and "°" as printed. **Quote MATCH**, 40 words. The range is the spread of the 29 individuals' Tpref, as the record says; the two-number range is right.

Verified: capture "in February 2017, through trawling and beach-seining activities" "conducted in Oresund, Helsingør, Denmark"; "10 °C, 30‰ sea water"; three weeks; herring three times a week; fasting "five to nine days"; tank start "between 4 and 6 °C"; "incrementally increasing by 2 °C (at a rate of 3.4 °C per hour)"; "a 15 min deactivation period" at each step; end at 20 °C; width of preferred range "on average 5.8 °C (SD: ± 1.3 °C) and was independent of body mass". No r2 or equation printed (tool summary).

Misstated or not carried, verbatim: Tpref is not a selected temperature: "We determined Tpref as the local minima in activity along the temperature gradient"; it was located on core temperature, not water temperature: "The average core temperature over the 15 min observation period, calculated using Newton’s law of cooling" "for all the fish regardless of size, was subsequently used to determine Tpref and Tpejus." The "gradient" is a temporal ramp of the whole tank ("individual fish were carefully situated within a circular tank, the diameter of which varied between 90 and 150 cm"; depth "approximately 20 cm"; "an acclimation period of two hours"), so the fish could not choose a temperature; the record's value ("selected temperatures"), units and method ("position observed") describe a choice gradient that this study did not use. Lower and upper Tpejus also fell with body size: "(one-way ANOVA, F(1) = 58.781, p < 0.001 and F(1) = 11.465, p < 0.004)". The 2635 g figure is in Methods 2.3 ("for the largest fish at 2635 g."), not the Discussion (tool summary that the Discussion has no such figure).

**Error (stimulus and response misdescribed; calculated vs measured temperature not stated; Tpejus results omitted).** Fixable.

### Line 2, Sebastes schlegelii, LED nets up 21 to 53%, red down 14%

Results sentence verbatim in two abutting pieces, twice ("The BT, GT, and WT harvested significantly higher CPUE (21%-53%) than CT (p<0.001), while RT caught 14% fewer individuals," | " and this difference was significant (p=0.001; Table S2)."); unspaced "p<0.001" and "(21%-53%)" reproduced as printed. **Quote MATCH**, 27 words; value says no more.

Verified, verbatim: "A total of 33 valid hauls were conducted, 11 hauls for Rizhao, 13 hauls for Weihai, and 9 hauls for Yantai"; trial dates September 6 to October 27; "after 12 h of soaking time,"; "Fifteen trammel net units were used in each study area, three for each treatment."; "Each trammel net treatment was deployed 200 m apart"; "Peak wavelengths were 465 nm for blue lights, 516 nm for green lights, 633 nm for red lights, and 456 nm for white lights."; "luminous intensity of 4.8 cd."; GLMM negative binomial, trip random effect (tool summary); interaction "found it to be insignificant;"; no randomisation described; stone flounder "the GT and RT harvested significantly higher CPUE (40% and 62%)" "and no significant difference was observed for BT and WT."; swimming crab "The RT harvested significantly higher CPUE (86%) than CT (p<0.001), while no significant difference was found" "for BT, GT, and WT." **MATCH.** Uncounted additions: "Ten LEDs were attached to the float line of each test group with nylon cable ties, with an interval of 4.85 m,"; CPUE "the total number of certain species captured per trammel net deployment."; Table 2 row "| Black rockfish a,b,c | 33 | 972 | 1280 (933) | 1487 (985) | 837 | 1178 (877) |" (meaning of the bracketed values not read).

### Line 3, Pseudopleuronectes yokohamae, green and red up, blue and white null

Results sentence verbatim in two abutting pieces ("The GT and RT harvested significantly higher CPUE (47% and 58%) than CT (p<0.001), while no significant difference" | " was detected for BT and WT (Table S2)."); same join as the desk's three pieces. **Quote MATCH**, 26 words; value says no more and carries the nulls.

Not carried, verbatim: the species occurred in one region only. Table 2: "| Marbled flounder b | 13 | 389 | 392 | 571 | 614 | 381 |" with the footnote "b, indicating occurrence in Weihai."; the Discussion speaks of "the five commercial species that occurred in Weihai"; and Weihai's sites were "unevenly designed along the coast" (other areas "evenly distributed"). The record's conditions give the 33 hauls in three regions as this species' sample and say the flounder's hauls are "not stated", where Table 2 gives 13 Weihai hauls.

**Error (sample composition misstated: 13 hauls in one region, not 33 in three).** Fixable. Owner question on order: answered above (OBIS, Pleuronectiformes).

### Line 4, Culex pipiens, red over blue in a dyed-sugar choice

Results 3.2 sentence verbatim in two abutting pieces, twice ("A significant preference for red over blue was found for both female and male mosquitoes" | "at light intensities higher than 0 lx (adjusted p < 0.0001 in all cases)."). **Quote MATCH**, 29 words; value says no more.

Verified, verbatim: "Laboratory strains of a Culex pipiens biotype molestus (Forskal, 1775) derived from mosquitoes" "collected in Northern Germany (Langenlehsten and Wendland) in 2012 and 2013."; "An average of around 200 mixed-sex mosquitoes, which were up to three-days-old and unfed,"; "Bugdorm cages (30 cm × 30 cm × 30 cm)"; "Every bioassay was repeated six times with independent mosquito batches."; "21.5 mL/L ink in 8% (w/v) fructose."; arrangement "changed in each replicate" "to avoid position-based effects."; 1600 lx, 130 lx, 0 lx; multinomial logit, Bonferroni; "6555 mosquitoes (including 2643 females)"; red vs green above 0 lx "and additionally at 0 lx for male mosquitoes"; "In this red-vs.-black assay, the red preference was not observed (adjusted p < 0.0001)." with the black preference confirmed "over all light intensities and both sexes (except 0 lx)" (Discussion).

Not carried or overstated, verbatim: the authors' own caveat, "Detected color preferences may be due to olfactory stimuli emanating from the ink." (the record mentions dye chemistry only as possible); no brightness or reflectance matching is reported for the foraging inks (spectra in Figs. S1, S2, tool summary), while the blue oviposition ink was diluted "to avoid a color too dark (for human eye)"; scoring "after two days" of "the pure colors", "the mixed colors (fed from different colors) and the uncolored mosquitoes (not fed but with water access)"; "the highest proportion of 76.9% of colored mosquitoes". The record's "at 0 lx the red-blue preference was not found" is not stated: the Results test red vs blue only above 0 lx, and the Discussion's "the 0 lx assays where no color preference was detected (except red vs. blue)" may refer to the foraging or the oviposition assay (oviposition red was preferred "to blue at 0 lx (one-sided Wald test, adjusted p < 0.05)").

**Error (intensity matching and the authors' ink-odour caveat omitted; 0 lx outcome overstated).** Fixable.

### Line 5, Cryptomys hottentotus (pretoriae), healthy females prefer infested-male urine

Results sentence verbatim in two abutting pieces ("Healthy females spend significantly more time with the odor of the parasitized male than that of the healthy male" | " (t = 2.94, df = 28, p = 0.032, Figure 2)."); "Figure 2" confirmed inside the parentheses. **Quote MATCH**, 30 words; value says no more.

Verified: Pretoria suburbs, October 2008 to September 2009, modified Hickman live traps (tool summary); 25 ± 1 °C, 12L:12D; 30 non-breeding females (15/15) and 30 donor males (15/15); proglottids in faeces, confirmed by a second examination two weeks later; ivermectin 2 µl/g for healthy, saline for infested; 1 ml urine on 20 g sawdust; 15 min acclimation, 20 min test, 6 h isolation; infested side alternated; each male's urine used twice; no blank control; infested females "(t = 0.30, df = 28, p = 0.990)"; female status F = 0.00, p = 1.00, male status F(1, 27) = 0.74, p = 0.396, interaction F(1, 27) = 15.19 (tool summary); entries 15.1 ± 1.0 vs 6.0 ± 0.7 arms and 7.5 ± 0.5 vs 3.53 ± 0.5 chambers (tool summary).

Not carried, verbatim: the authors' own reading: "The observed odor preferences of both healthy (i.e., living with healthy males) and infested females" "(i.e., living with infested males) may reflect a preference for unfamiliar male odors" "(i.e., infested for healthy females, healthy for infested females) rather than a preference" "or avoidance of odors of infested males."; the Abstract's "rather than discriminate between infestation status of males."; the Conclusion repeats the overstatement ("whereas" "infested females prefer those of healthy males."); Table 1 prints p < 0.0001 for the interaction against 0.0006 in the text (tool summary). Uncounted: the printed p values (0.032 for t = 2.94, 0.990 for t = 0.30, df = 28) are larger than unadjusted two-tailed values (about 0.007 and 0.77, auditor's calculation), so they look adjusted; the text read does not say how.

**Error (name; authors' unfamiliar-odour interpretation omitted).** Fixable by renaming to Cryptomys pretoriae (Names) and adding the omissions.

### Line 6, Cydia pomonella, UV-A LEDs on lured traps

Abstract sentence verbatim in two abutting pieces, twice ("However, UV-A LEDs, when used with these two lures, significantly increased total moth catches 7- and 3-fold" | "in July and August, respectively."). **Quote MATCH**, 22 words; value says no more than the quote.

Verified: Tieton and Wapato, WA; ten trials, 2024 and 2025; 5 to 13 and 27 to 53 replicates; orange delta traps at "ca. 3 m"; replicates "randomly spaced 30 m apart,"; CM4K and PH1X ("a red septum loaded with 1.0 mg codlemone", tool summary); six UV units 365 to 397 nm, BGR and green; "Treatments with zero catches were excluded from the analysis."; "Traps with LEDs emitting at a peak of 395 nm with 1000–2000 mW/m2 were the most effective."; early-season null "Adding the UV-A lights did not increase moth catches early in the season with either the PH1X or CM4K lures."; Trial 5 BGR, UV10 and green not above unlit (tool summary); non-targets up.

Not carried, verbatim: the Results do not support the Abstract's figures as worded. July: "In comparison, CM male catches were 7-fold higher in traps with the UV LED in July." (PH1X trial, males, tool summary for Trial 2 and UV1); August: the late-season CM4K trial "had significantly more (4-fold) total moths caught with the LED" (Trial 4, tool summary), not 3-fold, and its unlit traps caught no females (tool summary) while zero-catch treatments were dropped from analysis; no test statistics for either comparison in the text (Table 3 not read). The irradiance drop is "98.5–99.8" at 15 cm, which the record gives as "more than 90%".

**Error (abstract-Results inconsistency and the lure/sex basis of each fold change omitted).** Fixable.

### Line 7, Calonectris borealis, grounding vs overflown light pollution

Results sentence verbatim: first piece "The probability of being grounded decreased with the straightness and the speed of the bird flight," (two passes), then ", but it increased with light pollution levels" and, on a third pass, the remainder verbatim "([Table 4](#T4) and [Figure 2](#F2))." (rendered "(Table 4 and Figure 2)."). The record's quote ends "light pollution levels." and drops the trailing "(Table 4 and Figure 2)" without an ellipsis: **quote error (unmarked trailing cut)**; the join itself was not returned in one response as two abutting pieces on any pass, so audit-324 condition 3 is not cleanly met either.

Verified: 277 fledglings "87 GPS-tagged, 92 tape-labelled, and 98 control birds"; 37 of 277 recovered; "(Pearson's Chi-squared test = 5.166, df = 2, p-value = 0.076)"; "Seventy-one of the 87 deployed GPS devices recorded positions, but we got complete tracks" "from just 43 birds."; VIIRS "Three cloud-free composite of VIIRS nighttime lights corresponding to November 2017–2019"; release "in a natural cave (simulating a natural burrow) situated 8 km inland"; random allocation; binomial GLM with logit link.

Not carried: "Given our sample size (n = 43), we ran univariate GLMs to avoid overparameterization."; Table 4 estimates with 95% confidence limits (no SE or p printed): mean 1.45 (0.61 to 2.56), SD 1.54 (0.62 to 2.81), maximum 1.65 (0.59 to 3.36) (tool summary of the table); irradiance units not stated (tool summary).

**Error, HOLD OUT (trait/stimulus ruling above; quote cut unmarked; univariate design and effect sizes omitted).** Not fixable by text replacement while the trait ruling stands.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Gadus morhua, Tpref 6.4 to 18.7 C | error, fixable | value, units, method, conditions, note | quote MATCH (40 words, two marked cuts); Tpref is an activity minimum on calculated core temperature in a warmed tank, not a selected temperature; Tpejus results omitted |
| 2 | Sebastes schlegelii, LED CPUE | MATCH | conditions (uncounted) | quote MATCH (27 words); LED spacing, CPUE definition, catch counts uncounted |
| 3 | Pseudopleuronectes yokohamae, LED CPUE | error, fixable | conditions, note | quote MATCH (26 words); species caught in Weihai only (13 hauls), not 33 hauls in three regions |
| 4 | Culex pipiens, red over blue | error, fixable | conditions, note | quote MATCH (29 words); brightness not matched and authors' ink-odour caveat omitted; 0 lx outcome overstated |
| 5 | Cryptomys pretoriae (filed as C. hottentotus), odour choice | error, fixable | taxon, conditions, note | quote MATCH (30 words); MDD name C. pretoriae; authors' unfamiliar-odour reading omitted |
| 6 | Cydia pomonella, UV-A on lured traps | error, fixable | conditions | quote MATCH (22 words); July 7-fold is male PH1X catch, Results give 4-fold not 3-fold in August, zero-catch exclusion |
| 7 | Calonectris borealis, grounding vs light | error, HOLD OUT | whole record | satellite proxy, univariate correlation, no stimulus at the bird; quote's trailing cut unmarked |

Errors 6 of 7 records (86%), above the 5% bar: scientific-context 6 (lines 1, 3, 4, 5, 6, 7), of which calculated-vs-measured stimulus 1 (line 1), sample composition 1 (line 3), intensity matching 1 (line 4), internal inconsistency omitted 1 (line 6), trait/stimulus hold-out 1 (line 7); names 1 (line 5); quote 1 (line 7); bibliographic 0; licence 0; duplicates 0 against main, all desk-d2* and audit-3* branches and the audit-3* hold-outs; grading 0. HOLD OUT: line 7.

Answers to the desk-d255 owner questions.
1. LED trammel-net CPUE under behaviour_vision: acceptable, as for the Chelonia nets in audit 350.
2. Mate-choice odour discrimination under sense_chemical: acceptable, with the authors' unfamiliar-odour reading carried.
3. Calonectris grounding against satellite light pollution under behaviour_vision: not acceptable as a covariate without a defined stimulus at the animal; held out (audit 350 line 4 footing).
4. Pseudopleuronectes yokohamae order: Pleuronectiformes, confirmed at species level on OBIS 275360.
5. (Launch question) Tpref key: sense_thermal fits, but this paper's Tpref is an activity minimum during forced warming, not a gradient choice, and the record must say so.

## Unchecked

- Line 1: Figure 3 and the regression form (no equation printed); the cod Discussion was read only by tool summary for the 2635 g point.
- Line 2: the bracketed values in Table 2 (BT, GT, WT); Table S2.
- Line 3: Table S2; whether the Weihai flounder hauls are all 13 Weihai hauls or a subset (Table 2 gives 13).
- Line 4: Figs. S1 and S2 (spectra) and Figure 6 (per-intensity proportions); the 0 lx red-blue foraging result.
- Line 5: the hidden synonym list on MDD 1001257 and 1001261; how p values were adjusted.
- Line 6: Tables 2 and 3 (per-trial durations, counts and tests); which UV unit gave each fold change beyond the tool summary.
- Line 7: the page's printed year (record 2022 from Crossref issued; DOI 2021, volume 9); irradiance units.

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). For blank fields the form is field = new string.

Line 1, counted:
- `value`: "selected temperatures (Tpref) of 29 individuals" -> "Tpref of 29 individuals"
- `units`: "preferred temperature in a rising gradient" -> "Tpref as the local minimum in activity during stepwise warming of the whole tank"
- `method`: "individual fish in a circular tank with a stepwise rising temperature gradient, position observed for 15 min at each step" -> "individual fish in a circular tank (90 to 150 cm across, water about 20 cm deep) whose water was warmed stepwise, behaviour observed for 15 min at each step with the heater off; Tpref taken as the local minimum in activity along the fish's calculated core temperature"
- `conditions`: "(Discussion gives 2635 g in one place)" -> "(Methods 2.3 gives 2635 g for the largest fish)"
- `conditions`: "so the gradient ran one way only and no order or side counterbalancing is described." -> "after a two-hour acclimation in the tank; the whole tank changed temperature over time (no spatial gradient, so the fish could not choose a temperature), the ramp ran one way only and no order counterbalancing is described. Tpref is not a selected or occupied temperature: the authors determined it as the local minimum in activity along the temperature series, located on each fish's average core temperature over the 15 min period, calculated from water temperature with Newton's law of cooling (not measured in the fish). The lower and upper pejus temperatures (Tpejus) also fell with body size (F(1) = 58.781, p < 0.001 and F(1) = 11.465, p < 0.004)."
- `note` (uncounted): "Preferred temperature in a rising gradient;" -> "Tpref from activity minima during stepwise warming of the whole tank, not a spatial choice (audit 351);"

Line 2, uncounted:
- `conditions`: "LED luminous intensity 4.8 cd each." -> "LED luminous intensity 4.8 cd each; ten LEDs on the float line of each net at 4.85 m intervals. CPUE is the number of a species caught per net deployment; rockfish catches per treatment were CT 972, BT 1280, GT 1487, RT 837 and WT 1178 (Table 2; bracketed values for BT, GT and WT not read)."

Line 3, counted:
- `conditions`: "Same design as the rockfish record: wild fish, 33 valid hauls in three regions in autumn 2021," -> "Same design as the rockfish record, but marbled flounder occurred only in Weihai: its CPUE rests on the 13 Weihai hauls (26 September to 8 October 2021; Table 2), not on all 33 valid hauls in three regions, and the Weihai sites were unevenly placed along the coast; catches per treatment CT 389, BT 392, GT 571, RT 614, WT 381 (Table 2); wild fish,"
- `conditions`: "Hauls with this species not stated for the flounder alone in the text read." -> "Single-region sample, so the region effect cannot be checked for this species."
- `note` (uncounted): "order Pleuronectiformes is not stated for this species there and is taken from main's Hippoglossus hippoglossus Pleuronectidae row (same family), which is a family-level source." -> "family Pleuronectidae and order Pleuronectiformes confirmed for this species on OBIS (taxonID 275360, Pseudopleuronectes yokohamae (Günther, 1877), accepted) by audit 351."

Line 4, counted:
- `conditions`: "at 0 lx the red-blue preference was not found." -> "the Results test red vs blue only above 0 lx and do not state the 0 lx outcome (the Discussion's 'no color preference was detected (except red vs. blue)' at 0 lx does not say which assay it means). Mosquitoes were scored after two days as pure-colour, mixed-colour (fed from more than one colour) or uncoloured (not fed; sugar-free uncoloured water available); 76.9% were coloured in the red-blue assay (2,643 of the 6,555 were females)."
- `conditions`: "Feeding on a coloured sugar solution under dye, so dye chemistry is a possible confound; dye vs plain controls were run in oviposition only." -> "Feeding on a coloured sugar solution under dye, so dye chemistry is a possible confound, and the authors themselves say the detected colour preferences may be due to olfactory stimuli emanating from the ink; dye vs plain controls were run in oviposition only. The foraging inks were not matched for brightness or reflectance (spectra in Figs. S1 and S2, not read); only the blue oviposition ink was diluted, to avoid a colour too dark to the human eye."
- `note` (uncounted): "(molestus listed as synonym in gbif-names.tsv)" -> "(gbif-names.tsv:1312 maps Culex pipiens molestus, EXACT ACCEPTED, to the species Culex pipiens; laboratory colony accepted at species rank under audit 332, as main's desk-d225:8)"

Line 5, counted:
- `taxon`: "Cryptomys hottentotus" -> "Cryptomys pretoriae"
- `conditions`: "the abstract names C. h. hottentotus, the introduction and results C. h. pretoriae." -> "the abstract names C. h. hottentotus, the introduction and the Table 1 footnote C. h. pretoriae; MDD (taxon 1001261) treats the highveld mole-rat as Cryptomys pretoriae (A. Roberts, 1913), split from C. hottentotus, type locality Pretoria, and the record follows MDD."
- `conditions`: "only the interaction (F = 15.19, p = 0.0006)." -> "only the interaction (F(1,27) = 15.19, p = 0.0006 in the text; Table 1 prints p < 0.0001). The Conclusion repeats the abstract's claim that infested females prefer healthy males' odours. The authors read both groups' results as possibly a preference for unfamiliar male odours (healthy females lived with healthy males, infested females with infested males) rather than a preference for or avoidance of infested males' odours, and the abstract says the females may prefer unfamiliar odours rather than discriminate infestation status."
- `note`: "Family and order from main (Cryptomys hottentotus, Bathyergidae, Rodentia)." -> "Name, family and order from MDD 1001261 (Cryptomys pretoriae, Bathyergidae, Rodentia; split from C. hottentotus); main's Cryptomys hottentotus rows are vision rows from other papers (audit 351)."

Line 6, counted:
- `conditions`: "Same abstract: adding UV-A lights did not increase moth catches early in the season with either lure;" -> "The Results do not match the abstract's figures as worded: the July 7-fold is for male catches in the codlemone-lure (PH1X) trial ('CM male catches were 7-fold higher in traps with the UV LED in July'), and the late-season CM4K trial reports 'significantly more (4-fold) total moths' with the LED where the abstract says 3-fold; unlit CM4K traps in that trial caught no females, and treatments with zero catches were excluded from analysis; no test statistics for these comparisons appear in the text read (Table 3 not read). Same abstract: adding UV-A lights did not increase moth catches early in the season with either lure;"
- `conditions`: "Irradiance fell more than 90% at 15 cm." -> "Irradiance dropped 98.5 to 99.8% at 15 cm from the source."

Line 7: HOLD OUT, no counted replacement. Reason: grounding probability against satellite-derived upward radiance along the track (a proxy, units not stated) in univariate GLMs on 43 birds is a behavioural correlate without a defined light stimulus at the animal and without manipulation or an unlit comparison; it does not separate visual attraction from route, terrain or other correlates of flying over lit coast (audit 350 line 4; audits 317, 344, 345). If the owner overrules, uncounted fixes:
- `quote`: "but it increased with light pollution levels." -> "but it increased with light pollution levels (Table 4 and Figure 2)."
- `conditions`: "Flight analysis uses only the 43 complete GPS tracks." -> "Flight analysis uses only the 43 complete GPS tracks, each variable in a separate univariate GLM because of the sample size, so the light effect is not adjusted for straightness or speed; Table 4 estimates (95% confidence limits, no SE or p printed): mean light pollution 1.45 (0.61 to 2.56), SD 1.54 (0.62 to 2.81), maximum 1.65 (0.59 to 3.36); irradiance units not stated."
- `note`: "main has only the congener Calonectris diomedea." -> "main also has two C. borealis behaviour_vision rows from a y-maze study (oa-13b:409, 410, jeb.247665), a different paper; family and order also on OBIS 1348497."

Verdict: 6 of 7 audited records in error (86%), above the 5% bar; lines 1, 3, 4, 5 and 6 fixable with the replacement text above; line 7 held out; line 2 MATCH with uncounted additions.
