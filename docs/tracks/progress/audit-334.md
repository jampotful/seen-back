# audit-334: desk-d240, evidence lines 1 to 7

Audited 31 October 2026 from the desk-d240 files present untracked in the worktree (docs/tracks/progress/desk-d240.md and docs/views/evidence/desk-d240.jsonl, 7 lines; neither committed here, neither edited). HEAD and origin/main 74387818 (desk-d239). `python3 -I tools/senses/check.py | grep 'd240\.'`: "docs/views/evidence/desk-d240.jsonl: 7 records, 0 problems". Quote lengths (`len(q.split())`): 33, 39, 39, 38, 35, 38 and 39 words, all within 40. Evidence records only; audits 332 and 333 are the format model, and the desk-audit.md evidence clause applies (40-word limit, no 125-character limit). Quotes returned in abutting pieces are judged under the six conditions in audit-324.md; cuts under audit-331.md.

Sources opened (WebFetch): api.crossref.org/v1/works/ for 10.3390/insects11110729, 10.3390/insects12040355, 10.7717/peerj.8718 and 10.1371/journal.pone.0112694 (one pass each); www.mdpi.com/2075-4450/11/11/729 (three passes); www.mdpi.com/2075-4450/12/4/355 (three passes); peerj.com/articles/8718/ (one pass); journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0112694 (three passes) and www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0112694 (one pass, publisher's own legacy host, returned by a WebSearch); reptile-database.reptarium.cz/Thamnophis/melanogaster. WoRMS and GBIF not opened (refused per rules). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened; the Linköping thesis and poster results of one WebSearch were not opened (theses). WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 2 WebSearches and 14 WebFetch calls used.

## Bibliographic and licence

- Line 1. Crossref: Joyce P. S. Leung, Jenny S. Cory, J. Todd Kabaluk, Alida F. Janmaat; title as recorded; Insects 11(11), 729; issued and published online 2020-10-26; journal-article; relation empty, no update-to. Page byline same four names in the same order. Licence: page "All articles published by MDPI are made immediately available worldwide under an open access license.", rights metadata CC BY 3.0 (tool summary); Crossref CC BY 4.0, vor. Accepted. Faults 0.
- Lines 2, 3. Crossref: Dae-Yun Kim, Theerachart Leepasert, Michael J. Bangs, Theeraphap Chareonviriyaphap; "Dose–Response Assay for Synthetic Mosquito (Diptera: Culicidae) Attractant Using a High-Throughput Screening System" (en dash as recorded); Insects 12(4), 355; issued 2021-04-16; journal-article; relation empty, no update-to (update-policy only). Page byline same order. Licence: page rights metadata CC BY 3.0 (tool summary); Crossref CC BY 4.0, vor. Accepted. Faults 0.
- Lines 4, 5. Crossref: Javier Manjarrez, Constantino Macías Garcia, Hugh Drummond; "Congenital feeding response to a novel prey in a Mexican gartersnake"; PeerJ 8, e8718, no issue; issued 2020-03-05; relation empty, no update-to. Licence: page "This is an open access article distributed under the terms of the Creative Commons Attribution License,"; Crossref CC BY 4.0, unspecified. Accepted. Faults 0.
- Lines 6, 7. Crossref: Sara Nilsson, Johanna Sjöberg, Mats Amundin, Constanze Hartmann, Andrea Buettner, Matthias Laska; title as recorded; PLoS ONE 9(11), e112694; issued 2014-11-10; relation empty, no update-to. Page byline same order (tool summary). Licence: page open access under the Creative Commons Attribution License, "permits unrestricted use, distribution, and reproduction in any medium"; Crossref CC BY 4.0, unspecified. Accepted. Faults 0.

source.access "open" right for all seven; years as printed. Bibliographic faults 0; licence faults 0.

## Names

- Agriotes obscurus (line 1): family and order from the title "(Coleoptera: Elateridae)". Not in main's gbif-names.tsv (grep "Agriotes": no row), so the note's "GBIF ACCEPTED in gbif-names.tsv" is wrong; audit-240.md:19 records GBIF ACCEPTED, EXACT, usageKey 5878773, Elateridae, Coleoptera, and main files it so (desk-d155). Name met; note wording fix uncounted.
- Culex quinquefasciatus (line 2): gbif-names.tsv:1314 EXACT ACCEPTED. Aedes aegypti (line 3): gbif-names.tsv:75 EXACT ACCEPTED. Culicidae, Diptera as on main. Met.
- Thamnophis melanogaster (lines 4, 5): not in gbif-names.tsv; Reptile Database "Thamnophis melanogaster (Peters, 1864)", higher taxa "Colubridae (Natricinae)", four subspecies; the paper names no subspecies (tool summary). Main's cells.jsonl and reptile.md file the species under Colubridae, Squamata. Met.
- Cuon alpinus (line 6): gbif-names.tsv:1317 EXACT ACCEPTED. Speothos venaticus (line 7): gbif-names.tsv:4522 EXACT ACCEPTED; taxonomy-extra.tsv:178 Speothos Canidae Carnivora. Met.

## Domestic status, origin and rulings asked

- Lab colonies (lines 2, 3). NIH Culex quinquefasciatus colony from the National Institute of Health, Thailand (obtained 2015, maintained nearly 40 years); USDA Aedes aegypti colony from Gainesville, Florida, maintained over 50 years; Pu Teuy Aedes aegypti collected as immatures in Kanchanaburi Province, January 2019 (tool summary). Main accepts laboratory colonies of wild species at species rank (audit 305 for Culex quinquefasciatus JHB and YOLO strains; audits 314, 332, 333). A strain is not a breed here; acceptable. Line 3 gives the two strains as separate values, not a pooled value; acceptable.
- BG-lure (lines 2, 3). Page: commercial Biogents product, about 20 to <40% L-(+)-lactic acid, 20 to <40% ammonium hydrogen carbonate, 5 to <10% hexanoic acid plus inert ingredients (tool summary). It is a synthetic blend attractant; the measured quantity is the mosquitoes' behavioural choice, which is a living response. The "living responses and volatile signalling only" ruling in rules.md is written for plant sense_chemical; it does not bar an animal behavioural response to a synthetic blend, and main's Aedes aegypti sense_chemical row (desk-d201, EAG to DEET) is the same kind. Acceptable.
- Shared sentence (lines 2, 3). Each line quotes the whole 39-word abstract sentence, and each value is confined to its own clause. Nothing in the quote rule bars one sentence serving two species records. Allowed. But line 2's value says "strongest", which the quote does not say ("greater positive percent attraction"); "strongest" is the Results wording (below). Counted in line 2.
- Lines 4, 5 (Thamnophis). Gravid females wild-caught at crayfish-eating (Acambay) and non-crayfish-eating (El Cerrillo, San Pedro Tlaltizapán) sites, "collected under a scientific collecting permit issued by the federal institution" "(Secretaría de Medio Ambiente y Recursos Naturales, FAUT-0188)."; ethics committee approval numbers printed. Neonates born in captivity, unfed until testing, wild species. Acceptable. The null line (C localities, F2,42) does not duplicate line 4 (NC localities, F2,99): different neonates, different test.
- Lines 6, 7 (zoo canids). Captive groups at Kolmården Wildlife Park, each a breeding pair plus offspring; birth origin not stated (tool summary). Acceptable at species rank.

## Duplicates

git grep on origin/main (74387818) across the whole docs/ tree (evidence, audit incl. audit/corrected and audit/ALL, sheets, searched, sources, wanted, gaps, progress) for the four DOIs (full and numeric parts), "Leepasert", "Manjarrez", "BG-lure", "Leung, ", and the six species names. A git grep of all 729 remote branches not merged into main (audit branches excluded) over docs/views/evidence, docs/views/audit and docs/views/sheets for the same DOIs and names.

- Agriotes obscurus: main only desk-d155 sense_thermal (10.3389/fnbeh.2020.00001). Not a repeat.
- Culex quinquefasciatus: canon-4:49 acuity_cpd, desk-d219:3,4 sense_thermal; no sense_chemical row; no 12040355 hit. Aedes aegypti: desk-d201:1 sense_chemical, another DOI. Not repeats.
- Thamnophis melanogaster: main only gaps files and a Schaeffel and de Queiroz 1990 vision lead (wanted, sources); unmerged grade-54 etc. recheck-33-fixed:7529 eye_diameter_mm. Not a repeat.
- Cuon alpinus, Speothos venaticus: oa-2:2377,2378,2397,2398 pupil rows (Banks et al. 2015); unmerged oa-13c:131 Speothos lambda_max_nm. Not repeats.
- The only branch hit for a d240 DOI is origin/research/desk-d240 itself.

Duplicate faults 0.

## Trait key and grading

sense_chemical is on main for animals (desk-d201). Grade `m` right for all seven: one named species measured by the authors. eye "" right.

## Quote and cut rulings

- Line 1. Printed sentence returned in three abutting pieces in one response: "As expected, beetles exposed to pheromone walked 72% faster and 31% farther than beetles in the blank control" "(speed: F1,67 = 27.0, p =< 0.001; distance: F1,67 = 28.52, p < 0.001)" "and also spent a greater proportion of time moving (F1,68 = 4.92, p = 0.030)." The tool's other pass gave "p ≤ 0.001" in a summary and, asked for the printed symbol, "=<"; the quote's "=<" stands. 47 words whole, so a cut is needed; the trailing cut drops a third result, not a qualifier, and the dropped result is carried in conditions. Acceptable under audit 331. The value's "both p < 0.001" restates the speed statistic as strict where the paper prints "=<" (counted with line 1's error; value fix below).
- Lines 2, 3. Abstract sentence returned in three abutting pieces, identical to the record. MATCH.
- Line 4. Printed: "In the neonates from NC localities, ln-TFAS for soft crayfish (0.91 ± 0.36) and hard crayfish (0.88 ± 0.35)" "were 1.3 and 1.2 times higher, respectively, than for the control water" "(0.69 ± 0.33; F2,99 = 3.28, P = 0.04; Fig. 1)." Whole sentence 42 words; the two cuts drop the stimulus means only. Acceptable. MATCH.
- Line 5. Printed: "In neonates of C localities, the ln-TFAS for soft crayfish (1.05 ± 0.47.) and hard crayfish (0.90 ± 0.25)" "were similar to the control (0.91 ± 0.32; F2,42 = 0.52, P = 0.60; Fig. 1A)." Whole, stray full stop as printed. MATCH.
- Lines 6, 7. Only the opening of each sentence was returned verbatim, on three passes ("A comparison between the four odor stimuli showed that the Asian wild dogs displayed a significantly higher number of" and "A comparison between the four odor stimuli showed that the South American bush dogs displayed a significantly higher number"); the tool declined the rest as over its limit. The statistics in the quotes (29.49, 67.41, P<0.0001) and the dropped fruity comparisons (15.02, 35.44) match the tool's summaries of the Results. The tail of each quote is unverified; the cuts, as described in the notes, drop a stimulus object and a second comparison, not a qualifier, and would be acceptable. Not counted; listed under unchecked, and the desk should re-verify the tails under audit-324's conditions before filing.

## Per-record findings

### Line 1, Agriotes obscurus, walking speed +72% and distance +31% with pheromone

Design verified: field-collected males from pheromone-baited pitfall traps, Agassiz, April and May 2014, March to May 2015, "It is not possible to know the age of the field-collected beetles,"; Petri-dish arenas 140 x 15 mm; 0.03 g of granules; white 0.8 klux, red 0 lux; 9 to 12 beetles per combination over six days; light null verbatim "The presence of visible light had no impact on any movement parameter, nor did it affect the response to pheromone."

**Error (omitted significant and null results of the same experiment; storage confound; misstated statistic).** (a) Same experiment, not in the record: "In the pheromone treatment, 24% more beetles reached the granule zone, compared with the blank control" "(Wald χ2 = 8.98, p = 0.003)."; "individuals exposed to pheromone had 75.9% more contacts," "(F1,46 = 6.49, p = 0.014)."; and the null "However, pheromone did not increase the duration of contact with the granule zone (F1,45 = 0.56, p = 0.457)." (b) Collection month in this experiment: "Beetles collected in April walked faster and farther than beetles collected in May" "(walking speed: F1,67 = 6.24, p = 0.015; distance: F1,67 = 5.62, p = 0.025),"; "Beetles collected in May spent 85.1% more time in the granule zone, compared to those collected in April" "(F1,46 = 7.47, p = 0.009)." The record's "collection month changed activity but not the pheromone response (other experiments)" omits that in Experiment 1 the May beetles showed no pheromone effect: "but this effect was not seen in beetles collected in May (pheromone: F1,63 = 0.00, p = 0.961;", with month confounded with storage time (tool summary). (c) Beetles were held "at 10 °C in darkness" until testing and the light experiment ran in August 2014 (tool summary), so April and May beetles had months of storage; assay temperature and treatment order are not stated (tool summary). (d) Value "both p < 0.001" against printed "p =< 0.001" for speed. Fixable.

### Line 2, Culex quinquefasciatus, 88.9% at 0.025 g

Design verified: 20 females per replicate, nine replicates per dose, 10 min, the index formula, ten doses 0.005 to 10 g, dry ice 76.0% +/- 26.3%, 10 g -50.2%, 0.5 g 10.0%, 0.005 g 75.9%.

**Error (value outruns quote; negative control misstated; responder basis, starvation and test timing omitted).** (a) The value's "strongest" is not in the quote, which says "greater positive percent attraction (88.9%) at 0.025 g"; the Results sentence that says it is "At 0.025 g, mosquitoes produced the strongest attraction response (88.9%), with a mean number of females" " in the treated cylinder at 6.0 ± 3.7." (one pass only, so not proposed as a replacement quote). (b) The record says the paper "does not report the no-lure negative control"; the Methods list "(3) one without lure as a negative control." and no result for it is given (tool summary). (c) The index counts only females that entered a cylinder: at the optimum a mean 6.0 +/- 3.7 of 20 were in the treated cylinder, so most females did not respond; the record does not say so. (d) "'starved' 12 h before testing (provided water only)."; Culex tested 18:00 to 24:00, Aedes 06:00 to 12:00 (tool summary). (e) No test separates 0.025 g (88.9%) from 0.005 g (75.9%); Kruskal-Wallis across doses, Mann-Whitney within and between species, mean +/- SD (tool summary). The per-dose Table 1 is an image and was not read. Fixable.

### Line 3, Aedes aegypti, optimum 0.005 g, 72.6% (USDA) and 58.9% (Pu Teuy)

Verified: 10 g -96.3% and -100% "(p = 0.317)", 0.05 g against 0.005 g "it was not statistically significant (p = 0.287).", USDA dry ice 12.2% "(p = 0.002)".

**Error (generation misstated; dose series omitted; negative control misstated).** (a) "For Ae. aegypti field mosquitoes (Pu Teuy), F2 to F3 generation females were used." in the HITSS assay; the record's "F1 to F3" is the susceptibility assay. (b) The USDA series given in the text is not monotonic and shows repellency well below 1 g: 0.025 g 21.3%, 0.05 g 53.5%, 0.1 g -29.3%, 0.15 g 3.5%, 0.2 g -51.9%, 0.5 g -22.2%, 1.0 g -40.0%, 5.0 g -87.0% (tool summary of Results text); the record carries only the abstract's "repelled from 1.0 g to 10.0 g". Only the 0.005 g Pu Teuy value is in the text; Pu Teuy dry ice not reported. (c) Negative control and starvation as in line 2. Fixable.

### Line 4, Thamnophis melanogaster, NC neonates 1.3 and 1.2 times control

Design verified: 253 neonates from 34 NC females and 65 from 15 C females, 14 days old, random order, 20 to 40 min interval, 60 s maximum, "TFAS = TF + (60 - L)", ln-transformed; relative-response t47 = 0.53, P = 0.70.

**Error (attack results and model omitted).** Same test, not in the record: "Only 3.1% of neonates from C and 11.5% from NC attacked a swab."; "NC neonates attacked in similar percentages to soft and hard crayfish swabs," "but did not attack the control-water swabs."; "The number of attacks towards soft crayfish swabs (N = 328) was higher than hard crayfish swabs" "(N = 151; G = 5.34, df = 1, P = 0.02) in both T. melanogaster populations." Model: "a generalized linear mixed model (ANOVA) with TFAS toward each stimulus being repeated measures variables", "sex, litter (considered as random factors)" "and population type (C/NC) as fixed factor."; no pairwise test of each crayfish swab against water was returned (tool summary). Neonates unfed ("From birth to two weeks, neonates were not fed because they are born with a yolk reserve."). Swabs were "immersing and turning" "in water with crayfish (volume 1:1) for 30 s", not soaked in the crayfish. Fixable.

### Line 5, Thamnophis melanogaster, C neonates null

Quote whole. **Error (contrary attack result and baseline omitted).** The soft-over-hard attack difference (G = 5.34, P = 0.02) is reported "in both T. melanogaster populations", and 3.1% of C neonates attacked; the record's conditions give neither, nor the relative-response comparison (C 0.14 +/- 0.54, NC 0.21 +/- 0.25; t47 = 0.53, P = 0.70) or that the C control score (0.91 +/- 0.32) stood above the NC control (0.69 +/- 0.33). Model as line 4. Fixable.

### Line 6, Cuon alpinus, blood vs blank chi2 = 29.49

Design verified (tool summary): 12 animals (7 F, 5 M, 1 to 8 years), 2,900 m2 enclosure; 0.5 ml per spruce log (48 x 7 x 4.5 cm), five logs a day, five presentations per stimulus in "pseudo-randomized order", at least two days apart, 3 h morning and 3 h afternoon; blood vs component chi2 = 0.07, P = 0.786; fruity vs blank chi2 = 2.10, P = 0.147.

**Error (omitted significant results; analysis basis omitted).** The blood odour component alone drew more interactions than the fruity odour (chi2 = 17.86, P < 0.0001) and the blank (chi2 = 33.39, P < 0.0001) (tool summary); this is the paper's central result and the record gives only the blood-vs-component null. Verbatim "Across the 20 experimental days, a total of 458 interactions with the odorized logs was observed."; "As the number of animals differed between species, we calculated the number of interactions per animal" by dividing totals by group size; individual animals are not tracked separately in the text read, so the chi-square counts pool one group (tool summary). Habituation null for this species (Spearman, P > 0.05) and unstated observer blinding not carried. Fixable.

### Line 7, Speothos venaticus, blood vs blank chi2 = 67.41

Design as line 6; 10 animals (5 F, 5 M, 1 to 6 years), 1,000 m2; blood vs component chi2 = 0.14, P = 0.712; fruity vs blank chi2 = 4.86, P = 0.028; Spearman rs = -0.54, P = 0.0193 (tool summary).

**Error (omitted significant results; analysis basis omitted).** Component vs fruity chi2 = 30.70 and vs blank chi2 = 60.82, both P < 0.0001 (tool summary), not carried; "a total of 1582 interactions with the odorized logs was observed." and the per-animal division as line 6. Fixable.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Agriotes obscurus, +72% speed, +31% distance | error | value, conditions | granule-zone results and contact-duration null, month effects, Exp 1 May null, storage omitted; "=<" restated as "<" |
| 2 | Culex quinquefasciatus, 88.9% at 0.025 g | error | value, conditions | "strongest" not in quote; negative control misstated; 6.0 of 20 responder basis, starvation, timing omitted |
| 3 | Aedes aegypti, 72.6% / 58.9% at 0.005 g | error | conditions | Pu Teuy F2-F3 in HITSS; non-monotonic USDA series omitted; negative control misstated |
| 4 | Thamnophis melanogaster, NC 1.3x / 1.2x | error | conditions | attack results (G = 5.34) and mixed model omitted |
| 5 | Thamnophis melanogaster, C null | error | conditions | attack result in both populations and control baseline omitted |
| 6 | Cuon alpinus, chi2 = 29.49 | error | conditions | component-alone results omitted; group-pooled counts, habituation null |
| 7 | Speothos venaticus, chi2 = 67.41 | error | conditions | component-alone results omitted; group-pooled counts |

Errors 7 of 7 records (100%), above the 5% bar; all fixable with the text below; none held out. Bibliographic, licence, name and duplicate checks pass; the shared abstract sentence, the lab colonies, the BG-lure blend and the trailing cuts are ruled acceptable. Unchecked: the tails of the line 6 and 7 quotes (beyond the first ~115 characters; desk to re-verify before filing); Kim et al. Table 1 (image) and the full Culex and Pu Teuy dose series; the Agriotes Supplementary Information 1 and 2 (light statistics); the PeerJ Table S1 (birth years) and figures; the PLOS Table 1 ethogram and observer blinding; the canids' birth origin (not printed). Desk owner questions: (1) cut convention: trailing cuts that drop a separate result are acceptable (audit 331) provided the dropped result is in conditions, as it is in lines 1, 6, 7; (2) one sentence for two species: allowed, each value confined to its clause; (3) Solenopsis peerj.11943: not audited; rules.md lists CC BY-NC as accepted.

## Replacement text

Each old string occurs exactly once in its field (checked with `str.count`).

Line 1 (counted):
- `value`: "(speed F1,67 = 27.0, distance F1,67 = 28.52, both p < 0.001)" -> "(speed F1,67 = 27.0, p =< 0.001 as printed; distance F1,67 = 28.52, p < 0.001)"
- `conditions`: "collection month changed activity but not the pheromone response (other experiments)." -> "in this experiment April-collected beetles walked faster and farther than May-collected beetles (speed F1,67 = 6.24, p = 0.015; distance F1,67 = 5.62, p = 0.025) and May beetles spent 85.1% more time in the granule zone (F1,46 = 7.47, p = 0.009); in Experiment 1 (moving air) April beetles walked faster with pheromone but May beetles showed no pheromone effect (pheromone F1,63 = 0.00, p = 0.961), with collection month confounded with storage time; Experiment 3 found collection month affected activity but not the pheromone response."
- `conditions`: "cut from the quote." -> "cut from the quote. In the pheromone treatment 24% more beetles reached the granule zone (Wald chi2 = 8.98, p = 0.003) and those that reached it made 75.9% more contacts (F1,46 = 6.49, p = 0.014), but pheromone did not increase the duration of contact with the granule zone (F1,45 = 0.56, p = 0.457). Beetles were held at 10 C in darkness until testing and this experiment ran in August 2014 on April- and May-collected beetles, so storage lasted months; assay temperature and the order of treatments are not stated."
- `note` (uncounted): "GBIF ACCEPTED in gbif-names.tsv." -> "Agriotes obscurus is not in gbif-names.tsv; GBIF ACCEPTED, EXACT, usageKey 5878773 per audit 240, as filed on main (desk-d155)."

Line 2 (counted):
- `value`: "strongest attraction to BG-lure at 0.025 g: 88.9% positive percent attraction" -> "greater positive percent attraction to BG-lure at 0.025 g: 88.9%"
- `conditions`: "Positive control 1 g dry ice; the paper does not report the no-lure negative control." -> "Positive control 1 g dry ice; the Methods list a no-lure negative control but report no result for it. Females were sugar-fed, then starved 12 h (water only) before testing; Culex was tested 18:00 to 24:00, Aedes 06:00 to 12:00. The index counts only females that entered a cylinder: at 0.025 g a mean 6.0 +/- 3.7 of 20 females were in the treated cylinder (Results), so most did not respond. The per-dose Table 1 (mean +/- SD) is an image and was not read; the order of doses is not stated."
- `conditions`: "The abstract gives no test statistic for the Culex optimum; the p > 0.05 in the quote refers to Ae. aegypti." -> "The abstract gives no test statistic for the Culex optimum, and the Results give none separating 0.025 g (88.9%) from 0.005 g (75.9%); whether the abstract's 'without significant difference within species (p > 0.05)' covers Culex is not stated. Kruskal-Wallis across doses, Mann-Whitney within and between species."

Line 3 (counted):
- `conditions`: "assays on F1 to F3 generations." -> "F2 to F3 generation females in the HITSS assay (F1 to F3 in the permethrin susceptibility assay)."
- `conditions`: "Positive control 1 g dry ice; the paper does not report the no-lure negative control." -> "Positive control 1 g dry ice; the Methods list a no-lure negative control but report no result for it. Females were sugar-fed, then starved 12 h (water only); Aedes was tested 06:00 to 12:00, Culex 18:00 to 24:00. The USDA series in the Results text is not monotonic and shows repellency below 1 g: 0.005 g 72.6%, 0.025 g 21.3%, 0.05 g 53.5%, 0.1 g -29.3%, 0.15 g 3.5%, 0.2 g -51.9%, 0.5 g -22.2%, 1.0 g -40.0%, 5.0 g -87.0%, 10 g -96.3%; for Pu Teuy the text gives only the 0.005 g value (Table 1 is an image, not read), and its response to dry ice is not reported. The order of doses is not stated."

Line 4 (counted):
- `conditions`: "(t47 = 0.53, P = 0.70)." -> "(t47 = 0.53, P = 0.70). Attacks were rare: 11.5% of NC and 3.1% of C neonates attacked a swab; NC neonates attacked soft and hard crayfish swabs in similar percentages but did not attack control-water swabs, and attacks on soft crayfish swabs (N = 328) outnumbered those on hard (N = 151; G = 5.34, df = 1, P = 0.02) in both populations. Analysis: generalized linear mixed model (repeated-measures ANOVA) on ln-TFAS with sex and litter as random factors and population type as fixed factor; no pairwise test of each crayfish swab against water is reported in the text read. Neonates were unfed from birth (yolk reserve). Collected under SEMARNAT scientific collecting permit FAUT-0188."
- `conditions`: "soaked in freshly molted crayfish, unmolted crayfish or distilled-water control" -> "saturated by 30 s immersion in water holding freshly molted or unmolted crayfish (1:1 volume), or distilled water as control"

Line 5 (counted):
- `conditions`: "(F2,99 = 3.28, P = 0.04; previous line)." -> "(F2,99 = 3.28, P = 0.04; previous line). The relative response to control did not differ between C (0.14 +/- 0.54) and NC neonates (0.21 +/- 0.25; t47 = 0.53, P = 0.70), and the C control score (0.91 +/- 0.32) stood above the NC control (0.69 +/- 0.33). Attacks: only 3.1% of C neonates attacked a swab, and attacks on soft crayfish swabs outnumbered those on hard in both populations (G = 5.34, df = 1, P = 0.02). Analysis: generalized linear mixed model with sex and litter as random factors and population type as fixed factor; neonates unfed from birth."
- `conditions`: "soaked in freshly molted crayfish, unmolted crayfish or distilled-water control" -> "saturated by 30 s immersion in water holding freshly molted or unmolted crayfish (1:1 volume), or distilled water as control"

Line 6 (counted):
- `conditions`: "fruity odour against blank: no significant difference (chi2 = 2.10, P = 0.147)." -> "fruity odour against blank: no significant difference (chi2 = 2.10, P = 0.147). The blood odour component alone also drew more interactions than the fruity odour (chi2 = 17.86, P < 0.0001) and the blank (chi2 = 33.39, P < 0.0001). 458 interactions in all over the 20 days; counts were taken for the group and converted to interactions per animal by dividing by group size, and individuals are not tracked separately in the text read, so the chi-square counts pool one group (breeding pair and offspring, 2,900 m2 enclosure). No significant decline in interactions across sessions (Spearman, P > 0.05). Observer blinding not stated."

Line 7 (counted):
- `conditions`: "fruity odour against blank: higher interaction (chi2 = 4.86, P = 0.028)." -> "fruity odour against blank: higher interaction (chi2 = 4.86, P = 0.028). The blood odour component alone also drew more interactions than the fruity odour (chi2 = 30.70, P < 0.0001) and the blank (chi2 = 60.82, P < 0.0001). 1582 interactions in all over the 20 days; counts were taken for the group and converted to interactions per animal by dividing by group size, and individuals are not tracked separately in the text read, so the chi-square counts pool one group (breeding pair and offspring, 1,000 m2 enclosure). Observer blinding not stated."

Before filing lines 6 and 7, the desk re-verifies each quote's tail on the page under audit-324's conditions; if it cannot, hold the line out.
