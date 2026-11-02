# audit-313: desk-d224, evidence lines 6 to 9

Audited 31 October 2026 from the desk-d224 files present untracked in the worktree (docs/tracks/progress/desk-d224.md and docs/views/evidence/desk-d224.jsonl, 9 lines; neither committed here, neither edited). HEAD and origin/main 785f8504 (desk-d223). Audit 312 judges lines 1 to 5; this report judges lines 6 to 9 only. `tools/senses/check.py` on the evidence file: 9 records, 0 problems. Quote lengths (`len(q.split())`) for lines 6 to 9: 14, 16, 14, 11, all within 40. The unit has evidence records only, so the brief's search-record and plant-screening parts do not apply; audits 310 and 311 are the format model.

Sources opened (WebFetch): www.mdpi.com/2075-4450/13/7/655 (four passes), www.mdpi.com/2075-4450/11/4/231 (two passes), www.mdpi.com/2075-4450/13/3/290 (two passes); api.crossref.org/works for 10.3390/insects11040231 and 10.3390/insects13030290, and api.crossref.org/v1/works for 10.3390/insects13070655 (the /works URL refused once; the /v1 path opened). Bash curl to Crossref was refused by the session proxy and not retried. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 2 WebSearches used.

## Bibliographic and licence

- Line 6, Romero et al. 2022, Crossref (/v1): Patricia Romero, Luis A. Ibarra-Juárez, Daniel Carrillo, José A. Guerrero-Analco, Paul E. Kendra, Ana L. Kiel-Martínez, Larissa Guillén, in the recorded order; title verbatim (second half returned as "Xyleborus ferrugineus (Fabricius) (Coleoptera: Curculionidae: Scolytinae) to Ethanol and Bark Volatiles of Three Host-Plant" "Species"); Insects 13(7), page 655, issued 2022-07-21; licence CC BY 4.0, content-version vor. MDPI page carries the same citation and authors; its only licence data is the dc.rights metadata link to CC BY 3.0, with no licence sentence in the body. Licence acceptable on the publisher's page plus the Crossref vor licence (audits 307/308/310/311).
- Line 7, Cai et al. 2020, Crossref: nine authors Pumo Cai to Qinge Ji in the recorded order; title verbatim; Insects 11(4), page 231, issued 2020-04-07; CC BY 4.0, vor. The page prints MDPI's general statement "For articles published under an open access Creative Common CC BY license, any part of the article may be reused without permission provided that the original article is clearly cited." Acceptable (publisher page plus Crossref vor).
- Lines 8 and 9, Carraretto et al. 2022, Crossref: Davide Carraretto, Laura Soresinetti, Irene Rossi, Anna R. Malacrida, Giuliano Gasperi, Ludvik M. Gomulski, in the recorded order; title verbatim; Insects 13(3), page 290, issued 2022-03-15; CC BY 4.0, vor. Page prints the same MDPI general statement; metadata CC BY 3.0. Acceptable.

Bibliographic faults 0; licence faults 0. source.access "open" right on all four.

## Names

- Xyleborus ferrugineus: Plazi treatments "Xyleborus ferrugineus (Fabricius, 1801)" (returned by my WebSearch) use the name as accepted; the paper prints "Xyleborus ferrugineus (Fabricius)". Main has no Xyleborus row; main files Scolytinae and other weevils (Rynchophorus ferrugineus, audit/corrected/methods.jsonl:944 to 947) under Curculionidae, so Curculionidae, Coleoptera is right. The paper's own title gives "Coleoptera: Curculionidae: Scolytinae".
- Fopius arisanus: Plazi "Fopius arisanus (Sonan, 1932)" (WebSearch) accepted; Braconidae, Hymenoptera as main's other Braconidae (Cotesia vestalis, evidence/oa-1.jsonl:4544). Right.
- Aedes albopictus: the paper uses Aedes albopictus throughout; main uses Aedes albopictus (docs/views/gaps/gbif-names.tsv:76 "Aedes albopictus EXACT ACCEPTED"), and "Stegomyia" appears nowhere on main. Culicidae, Diptera as main. Right.

Name faults 0.

## Duplicates

git grep on origin/main across the whole docs tree (evidence, audit/corrected, audit/ALL.jsonl, searched, sheets, gaps, wanted, codex-findings, progress notes) for "Xyleborus", "ferrugineus", "Fopius", "arisanus", "albopict", "Stegomyia", "Carraretto", "Romero", "decanoic", "Bactrocera dorsalis", "Scolytinae", and the three DOIs (insects13070655, insects11040231, insects13030290). None of the three DOIs is on main. No Xyleborus or Fopius row. Aedes albopictus on main: acuity_cpd (evidence/canon-4.jsonl:36) and lambda_max_nm 515 nm (audit/corrected/methods.jsonl:705; audit/ALL.jsonl:3168), no sense_chemical row; Aedes sense_chemical on main is Ae. aegypti only (desk-d201.jsonl:1, DEET EAG). "decanoic" on main is a Chromolaena floral volatile list (sweep-42.jsonl:13). "Romero" on main is other authors. Line 8's note "the species appears on main only for acuity" is wrong: it misses the lambda_max_nm row in audit/corrected (part of the line 8 fix, not a repeat). Lines 8 and 9 are different sexes and different results from one paper; they do not duplicate each other. Line 6 is the X. ferrugineus half of a two-species sentence; under audits 299/300 that is fine when the record states its half and the value is the species' own, which it is ("In both X. affinis and X. ferrugineus"). Duplicates 0; contradictions 0.

## Per-record findings

### Line 6, Xyleborus ferrugineus, sense_chemical, 70% ethanol strongest EAG

Section 3.1 ("EAG responses of Wild and Laboratory-Reared Insects"), verbatim and whole: "In both X. affinis and X. ferrugineus, 70% ethanol elicited the strongest antennal responses." MATCH, 14 words. The Abstract ("Ethanol elicited the strongest olfactory responses in both species.") and Conclusions ("Ethanol vapor triggered the largest amplitude EAG responses in both X. affinis and X. ferrugineus.") say the same in other words; the note's "also repeated in Conclusions" is loose (different wording), uncounted. The X. ferrugineus origin contrast is verbatim "the only difference found in the contrast tests corresponds to 70% ethanol (t = 6.64, df = 596, p < 0.001)", as recorded. Numbers verbatim: "A mean (+ S.E.) of 12 ± 2 beetles was tested for each bark aging period", "the entire assay was performed on three different occasions,", "using a total of 108 ± 18 individuals per origin." Grade m right.

**Error (EAG normalisation, data exclusion, temperature/humidity and age omitted; a second control invented).** (a) Normalisation, verbatim: "the value corresponding to its negative control (air) was subtracted"; exclusion, verbatim: "When the air values exceeded the treatment values, a non-response was recorded and the observation was discarded." Neither is carried, though the brief names EAG normalisation as a required design point and discarding non-responses bears on the per-stimulus n. (b) Holding and rearing conditions, verbatim: wild beetles "kept at controlled conditions (28 ± 1 °C and 68 ± 5% r.h.) until the next day for testing."; lab colony "at 26 ± 1 °C and 60 ± 5% r.h. and darkness"; omitted. (c) Age, verbatim: "approximately 1–10-day-old beetles were collected for use in EAG assays" (lab); wild age unknown (tool summary); omitted, though the record's main contrast is wild against lab. (d) The record's method lists "an empty jar (negative control) and an air blank" as two controls; the paper has one: "For EAG and GC–MS, an empty jar was used as a negative control." and "the negative control (air) in a randomized sequence." (e) Also not carried: "Finally, an additional injection of 70% ethanol was administered to evaluate antennal viability.", so ethanol was both the positive control and the viability check. The record's lab-colony source is right as far as it goes (verbatim "adults were obtained from the Molecular Entomology Laboratory of the BioMimic® Cluster at INECOL."; field origin of the founders not stated). Fixable.

### Line 7, Fopius arisanus, sense_chemical, oviposition damage made citrus and peaches more attractive

Abstract, verbatim and whole: "For citrus fruits and peaches, oviposition damage caused them to be more attractive to parasitoid females." MATCH, 16 words. Value says no more than the quote. Experiment 1 Results, verbatim: "fruits infested by B. dorsalis were obviously attractive for F. arisanus in comparison to healthy fruits". Groups verbatim: "one group of 10 parasitoids aged 7–12 days was gently transferred into the opening of the olfactometer". Grade m right.

**Error (contrary mango result omitted, comparison arms incomplete, F value misattributed, colony generations omitted).** (a) The Abstract, verbatim: "infested mangoes did not attract more female parasitoids compared to healthy or mechanically damaged fruits". The record says females "were significantly attracted to mangoes" without saying that oviposition damage made no difference for mango, the one fruit where the recorded effect failed. (b) Comparisons: verbatim "Purified air was used as the control group in this dual-choice experiment."; infested fruit was tested against healthy fruit, mechanically damaged fruit and purified air (tool summary). The record names only healthy and mechanically damaged fruit. (c) The record's example "peach F4,40 = 5.31, p = 0.002" is from the infestation-age experiment (fruit 1 to 5 days after infestation; tool summary), not the infested-versus-healthy test the value reports, whose choice percentages appear only in Figure 1 (tool summary); citrus in that experiment, verbatim, "citrus fruits exhibited a repelling effect 5 days postinfestation." (d) Colony, verbatim: "Emerged adults were subsequently supplemented with B. dorsalis eggs for 10–30 generations."; a lab colony of up to 30 generations, not carried. (e) Not carried: 200 mL/min per arm (verbatim "The airflow was 200 mL/min per arm."), first choice only, percentages computed from responders only and non-responders not reported, 10 wasps released together per run so the 9 replicates (not 90 wasps) are the independent units, bioassay temperature and humidity not reported (rearing 25 ± 1 °C, 75 ± 5% RH) (all tool summary except the airflow). Fixable.

### Line 8, Aedes albopictus, sense_chemical, decanoic acid attractive to males at an intermediate concentration

Abstract (also the Simple Summary), verbatim and whole: "One compound, decanoic acid, acted as an attractant for males at an intermediate concentration." MATCH, 14 words. Methods as recorded for strain, 400 µL hexane on filter paper, 20 per run, "Compounds were tested with at least six replicate runs for each concentration.", "The position of the test stimuli and control in each arm was alternated for each replicate." Grade m right.

**Error (same compound repellent to males at the high dose omitted; dose not stated though printed; no multiple-comparison correction; rearing conditions given as test conditions).** (a) Results, verbatim: "there was significant attraction of males (p = 0.025)" at 10^-4, and "At the high concentration, the compound acted as a repellent (10−2, p = 0.027)." The record omits that decanoic acid itself repelled males at 10^-2, the result that most limits the value, while citing other compounds' repellency. (b) The record says the concentration is not stated in numbers; the Results give it (10^-4, 0.01%). (c) At least 84 compound-by-dilution paired t tests (28 compounds, at least three dilutions each; my count) with significance at p < 0.05 and no correction described (tool summary), and the authors call the data preliminary (verbatim "Some considerations emerge from these preliminary data."); a single p = 0.025 attraction among them is not flagged. (d) "26 C and 65-70% RH" is the rearing and holding condition (verbatim "were maintained at 26 °C and 65–70% relative humidity."); the olfactometer temperature, verbatim "The temperature within the olfactometer was 27 ± 0.72 °C.", was recorded in the validation test, and the compound-assay temperature is not stated (tool summary); 3 L/min is likewise given in the validation section only (tool summary). (e) Note: main does hold Aedes albopictus outside acuity (lambda_max_nm 515 nm, audit/corrected/methods.jsonl:705). Fixable.

### Line 9, Aedes albopictus, sense_chemical, no significant female response to decanoic acid

Abstract (also the Simple Summary), verbatim and whole: "Decanoic acid did not elicit a significant response from female mosquitoes." MATCH, 11 words. Results, verbatim: "No significant response to any dilution was recorded." Females not blood-fed, verbatim "The females used in our assays were not blood-fed.", as recorded. The null is scoped to the assay. Grade m right.

**Error (female mating status and housing omitted; rearing conditions given as test conditions).** (a) Verbatim "Male and females were maintained together in cages (sex ratio approximately 1:1)."; mating status is not stated, so the females were very likely mated but unfed, a host-seeking state that bears directly on a female null. Not carried. (b) As line 8 (d): 26 °C and 65 to 70% RH are holding conditions; the compound-assay temperature is not stated. (c) Not carried: the null has no p values and no female-specific replicate count in the text (Figure 3 and Dataset S2 only; tool summary). Fixable.

## Trait key

- Line 6, sense_chemical: fits (EAG of living antennae to volatile headspace).
- Line 7, sense_chemical: fits (Y-tube behaviour of living wasps to fruit volatiles).
- Lines 8 and 9, sense_chemical: fit (olfactometer choices of living mosquitoes to volatile compounds on filter paper; a single compound applied as a volatile, not an extract).

Trait key faults 0.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 6 | Xyleborus ferrugineus, 70% ethanol strongest EAG | error, fixable | method, conditions | Quote MATCH (14 words); air subtraction and discarded non-responses, temperature/RH and age omitted; a second "air blank" control invented |
| 7 | Fopius arisanus, oviposition damage attracts (citrus, peach) | error, fixable | conditions | Quote MATCH (16 words); infested mango not more attractive than healthy omitted; purified-air arm omitted; F value from a different experiment; 10 to 30 generations omitted |
| 8 | Aedes albopictus, decanoic acid attracts males at intermediate dose | error, fixable | conditions, note | Quote MATCH (14 words); decanoic acid repelled males at 10^-2 (p = 0.027) omitted; 10^-4 said unstated; no multiple-comparison correction; rearing conditions given as test conditions |
| 9 | Aedes albopictus, female null to decanoic acid | error, fixable | conditions | Quote MATCH (11 words); females caged with males (mating unstated) omitted; rearing conditions given as test conditions |

4 of 4 records in error (100.0%): scientific-context 4 (lines 6 to 9); value beyond quote 0; quote form 0; duplicates 0; bibliographic 0; names 0; licence 0; trait key 0; grading 0.

Pooled with audits 172 to 311: 353 of 757 evidence records (46.6%; 349 of 753 before this audit, 4 of 4 here). Audit 312's lines 1 to 5 are not included.

## Replacement text

Line 6:
- `method`: replace "an empty jar (negative control) and an air blank, in randomised order two minutes apart" with "an empty jar (negative control, air), in randomised order two minutes apart, with a final 70% ethanol injection to check antennal viability; each response had the air (negative control) response subtracted, and responses below the air value were recorded as non-responses and discarded; data log(x+1) transformed".
- `conditions`: after "laboratory-reared females (4 generations on Platanus mexicana sawdust medium" insert ", colony obtained from the INECOL Molecular Entomology Laboratory, field origin not stated; lab beetles about 1 to 10 days old, wild beetles of unknown age; wild beetles held at 28 ± 1 C and 68 ± 5% RH until testing the next day, lab colony at 26 ± 1 C and 60 ± 5% RH in darkness".

Line 7:
- `conditions`: replace "the abstract sentence does not name the comparison fruit (healthy or mechanically damaged fruit were the other treatments in the study);" with "the abstract sentence does not name the comparison; infested fruit was tested against healthy fruit, mechanically damaged fruit and purified air ('Purified air was used as the control group in this dual-choice experiment.'), and Experiment 1 found infested peaches and citrus more attractive than healthy fruit; for mango the effect failed: 'infested mangoes did not attract more female parasitoids compared to healthy or mechanically damaged fruits' (Abstract);".
- `conditions`: replace "percent-choice values are not given in the text I read, only ANOVA F values (for example peach F4,40 = 5.31, p = 0.002);" with "percent-choice values are in Figure 1 only; the ANOVA values in the text are from other experiments (for example infestation age, peach F4,40 = 5.31, p = 0.002, fruit 5 days after infestation less attractive than 1 to 3 days, and citrus repellent 5 days after infestation);".
- `conditions`: replace "parasitoids from a colony started from rotten guava collected in Zhangzhou, Fujian, China;" with "parasitoids from a laboratory colony started from rotten guava collected in Zhangzhou, Fujian, China, and reared on B. dorsalis eggs for 10 to 30 generations; 200 mL/min per arm; first choice only, percentages computed from responding wasps, non-responders not reported; the 10 wasps of a run were released together, so the 9 runs are the replicates; bioassay temperature and humidity not reported (rearing 25 ± 1 C, 75 ± 5% RH);".

Line 8:
- `conditions`: replace "the sentence does not state the concentration in numbers, and the same paper reports repellency at the high concentration for some other compounds (for example 1-octen-3-ol and nonanal, p = 0.025)" with "the Results give the attractive dilution as 10^-4 (0.01%) (p = 0.025), no effect at 10^-6, and repellency to males by decanoic acid itself at 10^-2 ('At the high concentration, the compound acted as a repellent (10−2, p = 0.027).'); other compounds were also repellent at the high concentration (for example 1-octen-3-ol and nonanal, p = 0.025); at least 84 compound-by-dilution paired t tests at p < 0.05 with no correction for multiple comparisons described, and the authors call the data preliminary".
- `conditions`: replace "Rimini laboratory strain (established in 2004 from field-collected eggs, kept in Pavia since 2013), 26 C and 65-70% RH," with "Rimini laboratory strain (established in 2004 from field-collected eggs, kept in Pavia since 2013), reared and held at 26 C and 65-70% RH; olfactometer temperature (27 ± 0.72 C) and the 3 L/min airflow are given for the validation test only, compound-assay temperature not stated;".
- `note`: replace "the species appears on main only for acuity" with "the species appears on main for acuity_cpd (canon-4) and lambda_max_nm (audit/corrected/methods.jsonl:705), not sense_chemical".

Line 9:
- `conditions`: the same replacement for the strain and temperature clause as line 8; replace "females were not blood-fed;" with "females were not blood-fed but were kept with males in cages (sex ratio about 1:1), mating status not stated; the text gives no p values or female replicate count for the null (Figure 3 and Dataset S2);".

## Owner questions (the unit's, answered for lines 6 to 9)

1. Xyleborus pair, one two-species sentence filed once per species: right, under audits 299/300; the sentence states the result of each species ("In both ..."), and line 6 carries X. ferrugineus's own origin contrast. A genus-level record would lose the per-species statement. Line 6's own faults are the design omissions above.
2. MDPI licences (dc.rights CC BY 3.0 on the page, Crossref CC BY 4.0 vor): acceptable for lines 6 to 9 under the audits 307/308/310/311 rule; the Crossref vor licence governs where the page and Crossref differ in version number.

## Progress note

Accurate on citations, licences, names, quotes and duplicates for lines 6 to 9. The Records list repeats the faults above: Fopius without the mango failure; the male decanoic acid record without the same compound's repellency at the high dose. The progress note's claim that every MDPI DOI was confirmed on Crossref agrees with what I found.

Verdict: 4 of 4 judged records (lines 6 to 9) in error (100.0%), above the 5% bar. Error lines: 6, 7, 8 and 9, all fixable with the replacement text above. Pooled 353 of 757 (46.6%).

This report is model output and carries no authority.
