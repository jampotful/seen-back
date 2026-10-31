# audit-306: desk-d220, evidence lines 1 to 4

Audited 31 October 2026 from the desk-d220 files present untracked in the worktree (docs/tracks/progress/desk-d220.md and docs/views/evidence/desk-d220.jsonl, 4 lines; neither committed here, neither edited). HEAD 561327e0 (desk-d219), equal to origin/main. `tools/senses/check.py` on the evidence file: 4 records, 0 problems. Quote lengths (`len(q.split())`), lines 1 to 4: 13, 16, 10, 18, all within 40. The unit has evidence records only, so the brief's search-record and plant-screening parts do not apply; audits 304 and 305 are the format model.

Duplicates: git grep on origin/main across docs (evidence, audit/corrected, audit/ALL.jsonl, searched, sheets, gaps, codex-findings, progress notes) for "Trialeurodes", "whitefl", "insects11020094", "Trichogramma japonicum", "Trichogramma", "insects17080798", "Orius" (word and species forms), "maxidentex", "Celosia", "Anthocoridae", "Aleyrodidae", "biology15080658", "Papilio polytes", "insects17050452", and the compounds "linalool", "citral", "bisabolene" in evidence and audit/corrected.

Sources opened (WebFetch): api.crossref.org/works for all four DOIs (line 1 twice, the second for the deposited abstract); www.mdpi.com/2075-4450/17/8/798 (three passes); www.mdpi.com/2079-7737/15/8/658 (two passes); www.mdpi.com/2075-4450/17/5/452 (two passes). Refused (PROVENANCE_REQUIRED, not retried): www.mdpi.com/2075-4450/11/2/94 (the line 1 publisher page), pmc.ncbi.nlm.nih.gov/articles/PMC7074224 and pubmed.ncbi.nlm.nih.gov/32024157 (both returned by my WebSearch). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened (one search returned an academia.edu result; left alone). WebFetch returns model summaries with verbatim pieces of about 120 characters, so quotes were checked as MATCH/MISMATCH from piecewise verbatim returns; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 3 WebSearch and 12 WebFetch calls used.

## Bibliographic and licence

- Line 1, Zhang et al. 2020, Crossref: Jihong Zhang, Huyin Li, Maorong Liu, Huan Zhang, Hai Sun, Hongtuo Wang, Lin Miao, Miaomiao Li, Ruihao Shu, Qilian Qin, in the recorded order; title verbatim (returned in two pieces, ending "Monitoring and Control of" / "Trialeurodes vaporariorum"); Insects 11, issue 2, article 94, issued 2020-02-01; CC BY 4.0 (vor); relation empty. The publisher page could not be opened, so the printed citation line and page licence were not seen; the unit's CC BY 3.0 metadata and CC BY 4.0 footer are unchecked. Met on Crossref.
- Line 2, Yang et al. 2026, Crossref: An-Na Yang, Yu-Xin Feng, Ke Li, Hang Li, Su Wang, Yuan-Xi Li; title verbatim; Insects 17(8) 798, published 2026-07-31; CC BY 4.0 (vor); relation empty. Page: "Insects 2026, 17(8), 798", metadata CC BY 3.0. Met (version difference, both CC BY).
- Line 3, Liu et al. 2026, Crossref: Yinyi Liu, Wei Gan, Xia Shi, Zhengpei Ye, Fan Song, Hu Li, Wanzhi Cai, Jianyun Wang, Junyu Chen; title verbatim; Biology 15(8) 658, published 2026-04-21; CC BY 4.0 (vor); relation empty. Page: "Biology 2026, 15(8), 658", metadata CC BY 3.0, no printed licence line (tool summary). Met.
- Line 4, Wu et al. 2026, Crossref: Xue Wu, Zengxin Chen, Yaqi Yang, Huaijian Liao, Yunwei Ju, Chufei Tang; title verbatim (two pieces); Insects 17(5) 452, published 2026-04-24; CC BY 4.0 (vor); relation empty. Page: "Insects 2026, 17(5), 452", metadata CC BY 3.0 and MDPI's CC BY reuse statement. Met.

Bibliographic faults 0; licence faults 0. source.access "open" right on all four.

## Names

- Papilio polytes: EXACT ACCEPTED in docs/views/gaps/gbif-names.tsv; main files it under Papilionidae (intake-3.jsonl:30). Family right; the note's "by general knowledge" is answered by main.
- Orius maxidentex: the Biology page's Abstract prints "Orius maxidentex Ghauri (Hemiptera: Anthocoridae)" (verbatim). My WebSearch returned Plazi treatments titled "Orius (Dimorphella) maxidentex Ghauri, 1972" and an article titled "Orius maxidentex (Hemiptera: Anthocoridae) from Iran". Accepted, family right. The note's "not from the page" is wrong (uncounted).
- Trichogramma japonicum: not in gbif-names.tsv; my WebSearch returned a GBIF entry titled "Trichogramma japonicum Ashmead, 1904". Trichogrammatidae is on main (corrected/bee.jsonl Megaphragma rows). Accepted.
- Trialeurodes vaporariorum: named in the Crossref title and abstract ("the greenhouse whitefly Trialeurodes vaporariorum"). Accepted. Aleyrodidae is not on main (git grep empty), contrary to the progress note's "printed by the papers or already on main"; the page that might print it was refused, so the family is unchecked (uncounted; standard placement, no conflicting usage on main).

Name faults 0.

## Duplicates

No row on main for Trialeurodes vaporariorum, Trichogramma japonicum or Orius maxidentex under any trait, and none of the four DOIs is on main. Main's only Orius mention is a suggested addition in audit-215.md:29 (Orius laevigatus, another species and paper). Papilio polytes is on main only under cff_hz (intake-3.jsonl:30, oa-1.jsonl:5595, oa-3.jsonl:106, oa-6.jsonl:66) and diel (oa-1.jsonl:5596); no sense_chemical row. Main's linalool, citral and bisabolene rows concern other species. Duplicates 0; contradictions 0.

## Per-record findings

### Line 1, Trialeurodes vaporariorum, behaviour_vision, Zhang et al. 2020

Crossref abstract, verbatim: "Green LEDs were more attractive than yellow LEDs, UV LEDs and green-UV combinations." MATCH, whole sentence, 13 words; preceded by "The results showed that the LED water pan trap was too inefficient to be useful." and followed by "Regardless of sunny or cloudy conditions, the green LED trap caught more than twice the number of whiteflies" / "than the yellow sticky card alone under summer shading conditions." Grade m right. Trait behaviour_vision fits (trap choice).

**Unchecked (Results not reachable).** The mdpi.com page and the PMC and PubMed copies were all refused, so the conditions drawn from the Results (F3,32 = 8.450 and 7.125, rotated positions, 3 days per set, yellow LED no different from the unlit card, UV adding nothing to green, Figure 6 means) could not be verified. No fault found in what was read. Uncounted suggestion: the abstract's own effect size (green LED trap more than twice the yellow card alone) could go into `conditions`.

Line 1: unchecked, 0 faults found.

### Line 2, Trichogramma japonicum, sense_chemical, Yang et al. 2026

Section 3.2, verbatim: "Furthermore, citral (0.001 μg/μL) (Figure 2S) and linalool (0.1 μg/μL) (Figure 2N) also attracted T. japonicum." MATCH, whole sentence with both figure call-outs, 16 words. Preceded by the β-ionone sentence; the paragraph opens "Plant-derived volatile compounds triggered distinct behavioral responses of T. japonicum." Methods confirmed: four-arm olfactometer "18.0 cm × 18.0 cm", two opposite chambers odorant and two n-hexane, arena "rotated 90° counterclockwise", "Thirty wasps were tested per concentration for each of the 20 odorants", "mated fresh (<12 h old) female wasps", Corcyra cephalonica eggs as host. Subsampling: "which yielded a 5th percentile of 8 s, 10 s, and 12 s, respectively"; "When the threshold time was set to 10 s, all three odorants had no effect on T. japonicum in the olfactometer assay."; "The C. suppressalis sex pheromone was attractive at 1 μg/μL". No p values in the text for citral or linalool (tool summary). The Discussion lists citral among "certain plant volatiles", so the record sits within the owner's living-signal reading as main already accepts single synthetic host volatiles (desk-d197.jsonl:3, desk-d217.jsonl:12).

**Error (contrary result omitted; stated as unavailable).** The conditions say the text "does not report the other concentrations of these two compounds". Section 3.1 does, verbatim: "Similarly, 10 μg/μL linalool was not repellent at thresholds of 0 or 15 s," / "but significant repellence was observed at 30 s and 60 s thresholds". The same compound repels at the top concentration under longer stay criteria, which is the threshold-dependence the paper is about; its 10 s result is in Table 7, not the text (tool summary). Section 3.3 also names "citral at 1 μg/μL" and "citral at 0.01 μg/μL" among odorants "which had yielded consistent results across different temporal thresholds in the olfactory tests", carried into an oviposition assay whose effects "were fully consistent" / "with the results obtained in the four-arm olfactometer"; the direction for those citral concentrations is not stated in the text. Fixable.

Grade m right. Line 2: 1 fault.

### Line 3, Orius maxidentex, sense_chemical, Liu et al. 2026

Section 3.5, verbatim: "Thus, 10 μg/μL β-bisabolene was the most attractive single volatile." MATCH, whole sentence, 10 words. Methods 2.5, verbatim: "while 100 μL of liquid paraffin was applied identically to the filter paper in the control bottle."; "Each compound treatment was tested with a total of 60 female individuals."; "starved for 3 h prior to testing"; "26 ± 1 °C and 75 ± 5% RH"; arms swapped "After every 10 individuals". Section 3.4 against control: 10 μg/μL χ2 = 9.000, p = 0.003; 100 μg/μL χ2 = 4.000, p = 0.046; no preference at 0.01, 0.1 and 1 μg/μL. EAG: "All six tested compounds elicited significant, dose-dependent EAG responses from the antennae of O. maxidentex."; methyl salicylate "(F = 2.163, df = 4, p = 0.089)". All as the record carries.

**Error (effect sizes of the value's own comparison omitted; stated as unavailable).** The value is a ranking ("the most attractive"), resting on the head-to-head tests printed just before it in Section 3.5, verbatim: "At a concentration of 10 μg/μL, β-bisabolene significantly attracted O. maxidentex compared with 1,3-diethenylbenzene" / "(χ2 = 4.840, df = 1, p = 0.028), trans-cinnamaldehyde (χ2 = 10.240, df = 1, p = 0.001)," / "and methyl salicylate (χ2 = 9.000, df = 1, p = 0.003)." The note says these "appear only in the first summary and are not carried"; they are printed on the page, and the narrowest margin (p = 0.028 against 1,3-diethenylbenzene) is what bounds "most attractive". Fixable.

Uncounted: the note's family remark is wrong (the Abstract prints Anthocoridae). The EAG caveat could add that nonanal's amplitude also did not differ between 0.1 and 100 μg/μL (tool summary). Grade m right. Line 3: 1 fault.

### Line 4, Papilio polytes, sense_chemical, Wu et al. 2026

Section 3.3: "Linalool, citronellol, and citronellal were significantly attractive to females at the highest dose of 1 × 10⁶ ng." MATCH (the page prints a superscript 6; the record's "106" is the flattened superscript, typographic and not counted, as in audit 241), whole sentence, 18 words. Preceded by "Among the nine individual volatile compounds tested, six elicited significant attraction or repellence." and followed by "Caryophyllene oxide and β-bisabolene attracted females at intermediate doses of 1 × 10⁴ to 1 × 10⁵ ng."; also "(E)-β-Farnesene repelled males at 1 × 10⁴ ng."; "No other significant attraction or repellence was detected for individual VOCs."; sex "did not exert a significant main effect, nor did it interact significantly with compound or dose" (no statistic in text). Methods confirmed verbatim: "inner diameter: 12 cm; arm length: 30 cm; branching angle: 60°"; "maintained at a constant 800 mL/min"; the 30 s and 10 min choice rule; 1 × 10³ ng dropped for an EAG "below 0.1 mV"; "Larvae were fed exclusively with fresh lemon (Citrus limon (Linnaeus)) leaves."; ">5 generations at 25.0 ± 1.0 °C, 75 ± 5% RH, 14:10 L:D"; "2 days post-eclosion", "unfed"; "25 males and 25 females"; "treatment and control positions randomly assigned for each replicate", positions switched every five trials; "complete darkness"; 10:00 to 18:00. Per-dose percentages are only in Figure 2 (tool summary). Frass and host-plant volatiles fit the living-signal reading.

No fault. Uncounted: "loaded as 1000 ug" is the unit's own conversion of 10⁶ ng; "10 uL of compound" should read "10 uL of test solution" (the page's "equal volumes (10 μL) of test solution"); the conditions could say that per-dose choice proportions are only in Figure 2. The mixture result ("Among binary mixtures, linalool and citronellal attracted males only at 1 × 104 ng") is optional, as it concerns a mixture.

Line 4: 0 faults.

## Trait key

- Line 1, behaviour_vision: fits (trap attraction, not spectral sensitivity, as the note says).
- Lines 2 to 4, sense_chemical: fit; single synthetic host or frass volatiles tested on living insects, as main accepts (desk-d197, desk-d217).

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Trialeurodes vaporariorum, behaviour_vision, green LED beats yellow and UV LEDs | unchecked, no fault found | none | Quote MATCH on the Crossref abstract (13 words); publisher, PMC and PubMed pages refused, Results-based conditions unverified |
| 2 | Trichogramma japonicum, sense_chemical, citral 0.001 and linalool 0.1 ug/uL attract | error, fixable | conditions | Quote MATCH (16 words); 10 ug/uL linalool repellent at 30 and 60 s thresholds omitted, and the text called silent on other concentrations |
| 3 | Orius maxidentex, sense_chemical, 10 ug/uL beta-bisabolene most attractive | error, fixable | conditions, note | Quote MATCH (10 words); the head-to-head chi-square tests behind "most attractive" (p = 0.028, 0.001, 0.003) omitted and called unavailable |
| 4 | Papilio polytes, sense_chemical, females attracted to three compounds at 10^6 ng | stands | none | Quote MATCH (18 words, flattened superscript); design, nulls, sex GLM and other compounds carried |

Faults per record: line 1: 0 (unchecked); line 2: 1; line 3: 1; line 4: 0. 2 faults in the 3 records judged; 2 of 3 in error (66.7%): scientific-context 2 (lines 2, 3); duplicates 0; bibliographic 0; names 0; quote-form 0; licence 0; trait key 0; grading 0. Counting line 1 as judged with no fault found would give 2 of 4 (50.0%).

Pooled with audits 172 to 305: 324 of 725 evidence records (44.7%; 322 of 722 before this audit, 2 of 3 here). With line 1 counted: 324 of 726 (44.6%). No search records.

## Replacement text

Line 2:
- `conditions`: replace "and does not report the other concentrations of these two compounds, so the quoted concentrations are those the text names as attractive, not a threshold;" with "Section 3.1 reports 10 ug/uL linalool not repellent at stay thresholds of 0 or 15 s but significantly repellent at 30 and 60 s (its 10 s result is in Table 7, not read); Section 3.3 names citral at 1 and 0.01 ug/uL among odorants with results consistent across thresholds, carried into an oviposition assay that agreed with the olfactometer, without stating the direction in the text; the quoted concentrations are those the text names as attractive at the 10 s threshold, not a response threshold;".

Line 3:
- `conditions`: after "the olfactory responses are attraction in a walking assay, not thresholds" append "; Section 3.5 head-to-head tests: 10 ug/uL beta-bisabolene was chosen significantly over 1,3-diethenylbenzene (chi2 = 4.840, p = 0.028), trans-cinnamaldehyde (chi2 = 10.240, p = 0.001) and methyl salicylate (chi2 = 9.000, p = 0.003)".
- `note`: replace "the head-to-head p values for beta-bisabolene against the other three compounds appear only in the first summary and are not carried" with "the head-to-head chi-square values for beta-bisabolene are printed in Section 3.5 and are carried in conditions"; replace "family as stated for Orius (Anthocoridae) by general knowledge, not from the page: check if the family matters" with "family printed in the Abstract: Orius maxidentex Ghauri (Hemiptera: Anthocoridae)".

Line 4 (uncounted, optional): in `method` replace "10 uL of compound on filter paper" with "10 uL of test solution on filter paper"; in `value` replace "(1 x 10^6 ng, loaded as 1000 ug)" with "(1 x 10^6 ng)"; append to `conditions` "; per-dose choice proportions are in Figure 2 only".

Line 1 (uncounted, optional): append to `conditions` "; the Abstract adds that the green LED trap caught more than twice the number of whiteflies than the yellow sticky card alone under summer shading, in sunny or cloudy weather".

## Owner questions (the unit's, answered where I could)

1. Families: Papilionidae is on main for Papilio polytes (gbif-names.tsv EXACT ACCEPTED; intake-3.jsonl:30). Anthocoridae is printed in the Orius paper's Abstract. Trichogrammatidae is on main. Aleyrodidae is not on main and was not confirmed on a page here (the line 1 page was refused); standard placement, no conflict.
2. CC BY 3.0 page metadata against CC BY 4.0 on Crossref: accepted as a version difference under the caller's ruling (both CC BY); it should not hold a record.

## Progress note

Accurate on citations, licences, names and duplicates; the 125-character reading limit is real, and the unit handled it by confirming whole sentences. Two notes overstate what the page lacks: the Trichogramma record says the text gives no other concentrations of linalool or citral (Section 3.1 gives 10 ug/uL linalool repellence), and the Orius note says the head-to-head statistics are not on the page (they are printed in Section 3.5). The family remark for Orius is wrong (printed), and the claim that Aleyrodidae is "already on main" is wrong (absent). The Records list does not carry the faults above.

Verdict: 2 of 3 judged records in error (66.7%), 2 faults, above the 5% bar; line 1 unchecked (no fault found in the abstract). Pooled 324 of 725 (44.7%). Error lines: 2 and 3, both fixable with the replacement text above. Line 4 stands; line 1 can stand subject to a Results check.

This report is model output and carries no authority.
