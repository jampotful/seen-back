# audit-308: desk-d221, evidence lines 7 to 11

Audited 31 October 2026 from the desk-d221 files present untracked in the worktree (docs/tracks/progress/desk-d221.md and docs/views/evidence/desk-d221.jsonl, 11 lines; neither committed here, neither edited). This audit judges lines 7 to 11 only; audit 307 judges lines 1 to 6. HEAD 1b7e0508 (desk-d220). `tools/senses/check.py` on the evidence file: 11 records, 0 problems. Quote lengths (`len(q.split())`), lines 7 to 11: 10, 16, 18, 20, 15, all within 40. The unit has evidence records only, so the brief's search-record and plant-screening parts do not apply; audits 305 and 306 are the format model.

Duplicates: git grep on origin/main across docs (evidence, audit/corrected, audit/ALL.jsonl, searched, sheets, gaps, batches, codex-findings, progress notes) for "cavitympanum", "Huia", "journal.pone.0005413", "Narins", "Gridi-Papp", "ultrasonic", "Pieris rapae" and "Pieris" (all traits), "pgen.1009527", "sinigrin", "glucosinolate", "Chrysomela", "fphys.2019.00343", "Pentzold", "Marion-Poll", "salicin".

Sources opened (WebFetch): api.crossref.org/works for the three DOIs; journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0005413 (two passes); journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1009527 (two passes; one rate-limited and retried once); www.frontiersin.org .../fphys.2019.00343/full (one pass, no licence line returned) and .../fphys.2019.00343/pdf (two passes, the record's URL); amphibiansoftheworld.amnh.org Huia cavitympanum page (returned by my WebSearch). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of about 125 characters, so long sentences were checked from consecutive pieces; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 1 WebSearch and 9 WebFetch calls used.

## Bibliographic and licence

- Lines 7 and 8, Arch et al. 2009, Crossref: Victoria S. Arch, T. Ulmar Grafe, Marcos Gridi-Papp, Peter M. Narins, in the recorded order; title "Pure Ultrasonic Communication in an Endemic Bornean Frog" verbatim; PLoS ONE 4(4) e5413, issued 2009-04-29; licence CC BY 4.0 (content-version unspecified); relation empty. Page citation line: "Arch VS, Grafe TU, Gridi-Papp M, Narins PM (2009) Pure Ultrasonic Communication in an Endemic Bornean Frog." / "PLoS ONE 4(4): e5413." Page licence: "This is an open-access article distributed under the terms of the Creative Commons" / "Attribution License". Met.
- Line 9, Yang et al. 2021, Crossref: Jun Yang, Hao Guo, Nan-Ji Jiang, Rui Tang, Guo-Cheng Li, Ling-Qiao Huang, Joop J. A. van Loon, Chen-Zhu Wang, in the recorded order; title verbatim; PLOS Genetics 17(7) e1009527, 2021-07-15; CC BY 4.0 (vor); relation empty. Page: "PLoS Genet 17(7): e1009527"; "© 2021 Yang et al. This is an open access article distributed under the terms of the Creative Commons Attribution License,". Met. (The record's journal string "PLoS Genetics" against Crossref "PLOS Genetics" is typographic, not counted.)
- Lines 10 and 11, Pentzold et al. 2019, Crossref: Stefan Pentzold, Frédéric Marion-Poll, Veit Grabe, Antje Burse, in the recorded order; title verbatim; Frontiers in Physiology 10, article 343, 2019-03-28; CC BY 4.0 (vor); relation empty. The /full page returned no licence line; the /pdf (the URL the record cites) printed "Copyright © 2019 Pentzold, Marion-Poll, Grabe and Burse. This is an open-access article distributed under the terms" / "of the Creative Commons Attribution License (CC BY)." and the citation "Front. Physiol. 10:343." Met on the exact copy cited.

Bibliographic faults 0; licence faults 0. source.access "open" right on all five.

## Names

- Huia cavitympanum: Amphibian Species of the World, verbatim heading "Huia cavitympanum (Boulenger, 1893)", breadcrumb "Family: Ranidae" > "Genus: Huia". Main's docs/views/gaps/taxonomy-gbif.tsv:874 gives "Huia	Ranidae	Anura" (GBIF backbone match 2026-10-19, usageKey 2426624). Accepted, family right. The progress note's "from memory ... not checked" is answered.
- Pieris rapae: EXACT ACCEPTED in docs/views/gaps/gbif-names.tsv (genus Pieris); Pieridae on main.
- Chrysomela populi: the paper prints "Poplar leaf beetles (C. populi, Linnaeus, Chrysomelidae, Coleoptera, Insecta)"; main's gaps files carry it under Chrysomelidae (cells.jsonl:33500 onward). Not in gbif-names.tsv; no conflicting usage on main (main's only other Chrysomela name, C. fastuosa, is a synonym of Chrysolina fastuosa and unrelated).

Name faults 0.

## Duplicates

None of the three DOIs is on main. No row on main for Huia (any species) or Chrysomela populi under any trait; Huia appears only in gaps/queue/sweep files (Huia masonii, and sweep-83's Huia, the extinct New Zealand bird genus). Pieris rapae and P. rapae crucivora rows on main are lambda_max_nm, receptor_classes, filter_pigments, behaviour_vision, eye_type, tapetum, rhabdom_um, facet_diameter_um, f_number and polarization; none is sense_chemical; "sinigrin" appears on main only in searched/sweep-4.jsonl:10 (Alliaria). Main's ultrasonic frog rows (desk-d154 lines 3, 4) are Odorrana tormota, another species and paper. Lines 7 and 8 do not duplicate each other (midbrain AEP amplitude versus tympanic membrane velocity, different sentences and values); lines 10 and 11 do not duplicate each other (subtype 2 firing rate versus subtype 1 null). Duplicates 0; contradictions 0.

Uncounted: line 9's note says the P. rapae crucivora rows on main are "lambda_max and receptor_classes"; main also has P. rapae under filter_pigments, behaviour_vision, eye_type and tapetum (no effect on the duplicate finding).

## Per-record findings

### Line 7, Huia cavitympanum, sense_hearing, AEP maximum 20 to 28 kHz

Results, Electrophysiology, verbatim: "Sensitivity is maximal between approximately 20 kHz and 28 kHz." MATCH, whole sentence, 10 words. Preceded by "AEP peak-to-peak amplitude is used as an index of auditory sensitivity, and the results from the H. cavitympanum TS" / "show a broad range of high sensitivity spanning 6–33 kHz, with a slight dip between ∼14 kHz and 18 kHz." and followed by "Although sensitivity of the auditory midbrain decreases for frequencies greater than 30 kHz, AEPs were consistently" / "observed up to 34 kHz, and were measurable up to 38 kHz in five of the males tested." Methods, verbatim: "Huia cavitympanum males (n = 6) were anesthetized by immersion in a 0.2% solution of tricaine methanesulphonate" / "(MS-222; Sigma) and placed on crushed ice to minimize bleeding during surgery."; immobilised with "d-tubocurarine chloride"; tone bursts "spanning 2–∼40 kHz" / "(the upper limit of stimulus frequency differed ±3 kHz between frogs) with a 1 kHz step size."; "Tones were calibrated to reach the position of the frogs' TM at the behaviorally relevant sound levels" / "of 80 (n = 2) or 90 (n = 4) dB SPL (re 20 µPa rms)."; "(3–5 recording positions per frog)"; no threshold criterion and no temperature stated (tool summary). Grade m right.

**Error (omitted qualifying result and stimulus level; misattributed statistic).** (a) The value's "(ultrasonic)" maximum is read without the sentence just before it: the broad high-sensitivity range runs 6 to 33 kHz, with a dip at about 14 to 18 kHz, so the frog's midbrain is also sensitive well inside the audible band; the record carries neither the range nor the dip. (b) The conditions say the paper "reports a calibration level only" but do not give it; stimuli were 80 dB SPL for two frogs and 90 dB SPL for four, so the amplitude curve mixes two stimulus levels, a design confound for an amplitude-based maximum. (c) The playback clause attributes "Wilcoxon Signed Ranks P = .043" to ultrasound against "background" in seven males; the page gives that P for US blocks against "the average number produced" / "during the PreBKG-NS blocks", while the US against BKG comparison is "(Friedman ANOVA: χ2 = 11.791, P = .008, n = 5)" on the five same-rate trials. Fixable. Uncounted: "with the head placed on crushed ice" should read "placed on crushed ice" (the page does not say head).

Line 7: 1 record in error (three faults, one category).

### Line 8, Huia cavitympanum, sense_hearing, eardrum wideband sensitivity 7 to 30 kHz

Results, Tympanic membrane vibration, verbatim: "These measurements reveal a wideband region of high sensitivity between approximately 7 kHz and 30 kHz." MATCH, whole sentence, 16 words. Also verbatim: "Between 1.8 kHz and 40 kHz, the mean curve was calculated from 11 trials performed on eight ears of six male frogs."; "Values below 1.8 kHz are from a single ear."; "Above 30 kHz, the velocity amplitude drops off, matching the pattern of auditory midbrain sensitivity." Methods: "Stimuli were calibrated to reach the frog's TM at 80 dB SPL (±1 dB) using VibroToolbox"; the frogs were "immediately re-anesthetized by immersion in MS-222 (0.3%)" / "for measurements of their tympanic membrane vibration spectra" after the AEP sessions. Grade m right; sample and single-ear caveat carried.

**Error (stimulus level and preparation omitted).** The conditions give neither the 80 dB SPL stimulus level nor that the measures are TM velocity amplitude taken from the same six males re-anaesthetised after the midbrain recording sessions (surgery, curare). The brief lists stimulus intensity among required conditions. Fixable. The cross-reference to the AEP record adds no value beyond the quote and is acceptable.

Line 8: 1 fault.

### Line 9, Pieris rapae, sense_chemical, sinigrin PI 0.89 at 1e-4 M

Results, "Feeding stimulation by glucosinolates in P. rapae larvae", verbatim in consecutive pieces: "At the concentration of 10−4 M, sinigrin was the most effective feeding stimulant (PI = 0.89 ± 0.030)," / " followed by gluconasturtiin (0.86 ± 0.030), gluconapin (0.70 ± 0.070), glucobrassicin (0.68 ± 0.087)," / " and glucoiberin (0.62 ± 0.079)." Also verbatim: "The stimulatory activity of sinigrin, gluconapin, glucoiberin and gluconasturtiin to larval feeding started at" / " the dose of 10−5 M (Fig 1A–1C, and 1E), whereas that of glucobrassicin started at 10−4 M (Fig 1D)." Methods "Feeding choice test" confirm the dish, disc size, 20 μL, cowpea, fifth instar, "Treated and control discs were alternately placed.", end point "When the total feeding area was larger than 25% or after 24 h feeding", and the PI formula. Figure 1 legend: "n represents the replicates of larvae and are labeled in the figures."; "paired Student's t-test"; "Data are presented as mean ± SEM."

**Error (quote truncated and presented as whole; effect sizes of the value's own comparison omitted).** (a) The quote ends "(PI = 0.89 ± 0.030)." with a full stop, but the sentence continues with a comma into the runners-up; the quote is a mid-sentence cut presented as a whole sentence, with the cut unmarked. The whole sentence is 37 words and fits the 40-word rule. (b) "Most effective" rests on a margin of 0.89 ± 0.030 against gluconasturtiin 0.86 ± 0.030, which the record does not carry; the ranking is not shown to be significant in the text. Fixable. Also: "± is not defined" should be replaced by "mean ± SEM (Figure 1 legend)", and "number of larvae not stated" by "n per dose given in the figures only". The electrophysiology paraphrase in conditions is partial: the page says the lateral larval sensillum neuron "responded with equal frequency to sinigrin," / "gluconapin, glucoiberin, glucobrassicin and gluconasturtiin at a concentration of 10 mM", and that adult medial tarsal sensilla responded to all tested glucosinolates, with a sinigrin threshold ten times that of glucobrassicin (females) or gluconasturtiin (males); stating only the lateral tarsal null slants the adult result (folded into this fault).

Trait key: a two-choice leaf-disc result is a behavioural feeding preference of a living animal; sense_chemical fits, and the record's method makes clear it is behaviour, not a receptor response. Grade m right. Line 9: 1 record in error.

### Line 10, Chrysomela populi, sense_chemical, subtype 2 at 19.6 Hz to salicin

/pdf, verbatim: "Finally, using salicin at 100 mM, spike discharges were recorded from s. chaetica subtype 2 at 19.6 Hz (±2.3 s.e.m.)." MATCH, whole sentence, 20 words. Control: "Using 30 mM KCl that served as positive control and solvent for tastants, mean frequency of s. chaetica subtype 2" / "was 16.7 Hz ± 1.3 s.e.m. (Figure 2)." Methods: "sucrose (1, 100 and 300 mM; n = 9 insects), fructose (100 and 300 mM; n = 4 insects) and salicin (100 mM, n = 2);" / " as positive control 30 mM KCl were used (n = 3)." Origin: beetles "were collected in the north of Jena close" / "to Dornburg-Camburg ... Germany and reared in a climate chamber provided with fresh twigs of poplar" / "under a 16 h:8 h light:dark cycle at 20◦C."; "beetles between three and 15 days old". Sucrose and fructose values as the record carries. Discussion: "Recordings on s. chaetica subtype 1 may evoke physiological responses when using other compounds than those tested."

**Error (value says more than the quote; n units misstated).** (a) The value adds "close to the 16.7 Hz (±1.3 s.e.m.) of the 30 mM KCl solvent alone", which is from another sentence, and the judgement "close to" is the unit's, with no test in the text; the record's own note concedes the quote does not contain the control. The comparison belongs in conditions. (b) The conditions say "salicin n = 2 insects and KCl n = 3 insects (Methods give n per tastant as insects)"; the Methods print "insects" only for sucrose and fructose and give salicin and KCl as bare "n = 2" and "n = 3". Fixable. Uncounted: origin (field-collected near Jena, held in a climate chamber on poplar) and stimulus protocol ("Each stimulus was applied twice, i.e., with a time interval of 30 s to avoid adaptation"; order randomisation not stated) could be added.

Grade m right (one named species). Line 10: 1 record in error.

### Line 11, Chrysomela populi, sense_chemical, subtype 1 null

/pdf, verbatim: "In contrast, s. chaetica subtype 1 did not respond to any of the tested tastants." MATCH, whole sentence, 15 words. The value says no more than the quote; the conditions carry the tastants, the n values as printed (no unit claim for salicin), age, sex not stated, and the Discussion caveat that the null holds only for the compounds used.

No fault. Uncounted: the paper does not report how many subtype 1 sensilla or insects were recorded, or whether subtype 1 responded to the 30 mM KCl positive control (tool summary); the conditions could say so, since the n values cover the stimuli overall. Origin as for line 10 could be added.

Line 11: 0 faults.

## Trait key

- Lines 7 and 8, sense_hearing: fit (midbrain evoked potentials; eardrum mechanics, labelled as such in conditions).
- Line 9, sense_chemical: fits (behavioural feeding preference on living larvae; the record does not present it as a receptor response).
- Lines 10 and 11, sense_chemical: fit (gustatory receptor-neuron recordings on living beetles).

Ruling asked by the unit (line 6, judged by audit 307, not counted here): odour-reward conditioning (PER) belongs under sense_chemical when the conditions state it measures learned discrimination between odours, not an innate preference or a detection threshold; a successful discrimination shows the odours are detected and told apart by a living animal, which is within the living-response reading. A conditioning record that reads the difference in PER rates as a preference between the odours overstates it.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 7 | Huia cavitympanum, sense_hearing, AEP maximum 20 to 28 kHz | error, fixable | value, conditions | Quote MATCH (10 words); broad 6 to 33 kHz range and dip omitted, 80 or 90 dB SPL stimulus levels omitted, playback P value misattributed |
| 8 | Huia cavitympanum, sense_hearing, eardrum 7 to 30 kHz | error, fixable | conditions | Quote MATCH (16 words); 80 dB SPL stimulus level and post-surgery re-anaesthetised preparation omitted |
| 9 | Pieris rapae, sense_chemical, sinigrin PI 0.89 | error, fixable | quote, conditions | Quote truncated mid-sentence and presented as whole; runner-up gluconasturtiin 0.86 ± 0.030 omitted; SEM and n mis-stated as absent |
| 10 | Chrysomela populi, sense_chemical, subtype 2 19.6 Hz to salicin | error, fixable | value, conditions | Quote MATCH (20 words); value adds KCl control and "close to" from outside the quote; salicin and KCl n called insects when unlabelled |
| 11 | Chrysomela populi, sense_chemical, subtype 1 null | stands | none | Quote MATCH (15 words); null scoped to tested tastants, Discussion caveat carried |

Faults per record: line 7: 1 category (three faults); line 8: 1; line 9: 1 category (quote-form and scientific-context); line 10: 1 category (value and design). 4 of 5 records in error (80.0%): scientific-context 4 (lines 7, 8, 9, 10), quote-form 1 (line 9), value beyond quote 1 (line 10); duplicates 0; bibliographic 0; names 0; licence 0; trait key 0; grading 0.

Pooled with audits 172 to 306: 328 of 730 evidence records (44.9%; 324 of 725 before this audit, 4 of 5 here). No search records.

## Replacement text

Line 7:
- `value`: replace "midbrain auditory evoked potentials most sensitive between about 20 and 28 kHz (ultrasonic)" with "midbrain auditory evoked potentials most sensitive between about 20 and 28 kHz".
- `conditions`: replace "animals were surgically prepared with the head placed on crushed ice to limit bleeding; no threshold criterion and no threshold in dB SPL are reported (the paper reports a calibration level only)" with "animals were anaesthetised with MS-222, placed on crushed ice to limit bleeding during surgery and immobilised with d-tubocurarine; tones were calibrated at the eardrum to 80 dB SPL in two frogs and 90 dB SPL in four, so the amplitude curve pools two stimulus levels; no threshold criterion is reported; the preceding Results sentence gives a broad range of high sensitivity spanning 6 to 33 kHz with a slight dip between about 14 and 18 kHz, and AEPs were measurable up to 38 kHz in five males".
- `conditions`: replace "in the field playback (seven males with complete data sets) males called more to ultrasound-only broadcasts than to background, Wilcoxon Signed Ranks P = .043 (ending of a longer sentence, page summary)" with "in the field playback (complete data sets from seven males) the five same-rate trials gave more calls during ultrasound blocks than other blocks (Friedman ANOVA chi2 = 11.791, P = .008, n = 5), and ultrasound blocks exceeded the PreBKG-NS blocks (Wilcoxon Signed Ranks P = .043)".

Line 8:
- `conditions`: append "; stimuli calibrated to 80 dB SPL (±1 dB) at the eardrum; the measure is tympanic membrane velocity amplitude, taken from the same males re-anaesthetised with MS-222 immediately after the midbrain recordings".

Line 9:
- `quote`: replace with "At the concentration of 10−4 M, sinigrin was the most effective feeding stimulant (PI = 0.89 ± 0.030), followed by gluconasturtiin (0.86 ± 0.030), gluconapin (0.70 ± 0.070), glucobrassicin (0.68 ± 0.087), and glucoiberin (0.62 ± 0.079)." (37 words, whole sentence).
- `conditions`: replace "the Methods do not state the number of larvae per replicate or any starvation period (page summary); the ± term is not defined in the quoted sentence;" with "values are mean ± SEM and n (replicate larvae) is given only in the figures (Figure 1 legend); differences between treated and control discs were tested by paired t-test; no starvation period is stated; sinigrin's lead over gluconasturtiin (0.86 ± 0.030) at 1e-4 M is small and not tested in the text;".
- `conditions`: replace "electrophysiology in the same paper: larval lateral sensilla styloconica responded to sinigrin at 10 mM while medial sensilla did not, and adult lateral tarsal sensilla did not respond at 10 mM (paraphrased, spike values only in figures)" with "electrophysiology in the same paper: one neuron in the larval lateral sensilla styloconica responded with equal frequency to all five glucosinolates at 10 mM and medial sensilla did not respond to sinigrin; adult lateral tarsal sensilla did not respond to sinigrin at 10 mM, while adult medial tarsal sensilla did, with a threshold ten times higher than for glucobrassicin (females) or gluconasturtiin (males) (paraphrased, spike values only in figures)".

Line 10:
- `value`: replace with "antennal sensilla chaetica subtype 2 fired at 19.6 Hz (±2.3 s.e.m.) to salicin at 100 mM".
- `conditions`: replace "salicin n = 2 insects and KCl n = 3 insects (Methods give n per tastant as insects); the 16.7 Hz KCl value is the ending of a longer Results sentence;" with "salicin n = 2 and KCl n = 3 (the Methods label n as insects only for sucrose and fructose); the 30 mM KCl solvent alone gave 16.7 Hz (±1.3 s.e.m.) in subtype 2 (another Results sentence; no test of salicin against KCl in the text); beetles field-collected near Jena and held in a climate chamber on poplar twigs; each stimulus applied twice 30 s apart;". Delete "the quote itself does not contain the KCl control" (no longer needed).

Line 11 (uncounted, optional): append to `conditions` "; the number of subtype 1 sensilla recorded and their response to the KCl control are not reported; beetles field-collected near Jena and held in a climate chamber on poplar twigs".

## Owner questions (the unit's, answered where I could)

1. Crossref CC BY plus a truncated Frontiers page: rule applied here: a licence statement printed on the copy read is preferred; where the page fetch ends before it, a Crossref licence entry with content-version "vor" deposited for that DOI counts as licence evidence for source.access "open", provided the text read is the publisher's own version of record (as audit 306 accepted for its line 1). It does not cover a preprint, repository or aggregator copy. For lines 10 and 11 the question is moot: the /pdf cited prints "Creative Commons Attribution License (CC BY)". On this rule Trypodendron and Ips can be filed once their quotes are read whole on the publisher's page.
2. Melipona conditioning under sense_chemical: see Trait key (line 6 is audit 307's).
3. Huia family: Ranidae confirmed (Amphibian Species of the World page; main's taxonomy-gbif.tsv:874). Anomalops is audit 307's.
4. PLoS ONE 2009 page "Creative Commons Attribution License" with Crossref CC BY 4.0: accepted, both CC BY.

## Progress note

Accurate on citations, licences, names and duplicates for lines 7 to 11. The Records list does not carry the faults above: it gives the Huia AEP maximum without the broad 6 to 33 kHz range or the two stimulus levels, and the Chrysomela subtype 2 record "close to the KCl control" as part of the value. The note "Taxon families ... Huia (Ranidae) are from memory" is now answered from ASW and main.

Verdict: 4 of 5 judged records in error (80.0%), above the 5% bar. Error lines: 7, 8, 9 and 10, all fixable with the replacement text above. Line 11 stands. Pooled 328 of 730 (44.9%).

This report is model output and carries no authority.
