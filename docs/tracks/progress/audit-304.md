# audit-304: desk-d218, evidence lines 1 to 4

Audited 31 October 2026 from the desk-d218 files present untracked in the worktree (docs/tracks/progress/desk-d218.md and docs/views/evidence/desk-d218.jsonl, 4 lines; neither committed here, neither edited). HEAD 5591be77 (desk-d217). `tools/senses/check.py` on the evidence file: 4 records, 0 problems. Quote lengths (`len(q.split())`), lines 1 to 4: 18, 21, 12, 20, all within 40. The unit has evidence records only, so the brief's search-record and plant-screening parts do not apply; audits 302 and 303 are the format model.

Duplicates: git grep on origin/main across docs (evidence, audit/corrected, audit/ALL.jsonl, searched, wanted, sheets, gaps, codex-findings, progress notes) for "Neophoca cinerea", "Australian sea lion", "ani16152342", "Equus caballus" (all traits, plus "horse" with hearing/Hz in evidence, corrected and sheets), "fvets.2020.00633", "Rørvang", "Heffner", "Astyanax mexicanus" (all traits), "d12100395", "Anas platyrhynchos" (all traits), "fphys.2022.921657", "Pekin", "Cairina". Note: a case-insensitive grep for "Neophoca" also hits Neophocaena; the only Neophoca cinerea hit on main is docs/views/gaps/try-species.json:1872.

Sources opened (WebFetch): mdpi.com 2076-2615/16/15/2342 (two passes), frontiersin.org fvets.2020.00633/xml (one pass), mdpi.com 1424-2818/12/10/395 (one pass), frontiersin.org fphys.2022.921657/xml (one pass); api.crossref.org/works for all four DOIs; lsu.edu/deafness/HearingRange.html and en.wikipedia.org/wiki/Astyanax_(fish), each returned by my WebSearch. Two utoledo.edu Heffner-lab URLs returned by my search redirected to a college homepage (no content). doi.org/10.1037/0735-7044.97.2.299 and a Europe PMC REST query were refused (PROVENANCE_REQUIRED) and not retried. A search result on an elogim.com proxy host was not opened. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries with verbatim pieces of about 120 characters, so quotes were checked as MATCH/MISMATCH from piecewise verbatim returns; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences, table rows and fragments quoted for verification. 4 WebSearch and 12 WebFetch calls used.

## Bibliographic and licence

- Line 1, Erbe et al. 2026, Crossref: Christine Erbe, Brad McKenzie, Jacob Stek, Lachlan Gill, Elysia Kriek, Malcolm Perry, Benjamin J. Pitcher, Evgenii Sidenko, David Slip, Adrienna van Gogh, Chong Wei, in the recorded order; title verbatim; Animals 16(15) 2342, issued 2026-08-01; CC BY 4.0 (vor); relation empty. Page: "Animals 2026, 16(15), 2342"; "This article is an open access article distributed under the terms and conditions of the" / "Creative Commons Attribution (CC BY) license"; metadata rights URL CC BY 3.0, footer link 4.0. Version difference, both CC BY: met.
- Line 2, Rørvang et al. 2020, Crossref: Maria Vilain Rørvang, Birte L. Nielsen, Andrew Neil McLean; title verbatim; Frontiers in Veterinary Science 7, article 633, issued 2020-09-09; CC BY 4.0 (vor); relation empty. Page licence line printed (CC BY). Met.
- Line 3, Blin et al. 2020, Crossref: Maryline Blin, Julien Fumey, Camille Lejeune, Maxime Policarpo, Julien Leclercq, Stéphane Père, Jorge Torres-Paz, Constance Pierre, Boudjema Imarazene, Sylvie Rétaux; title verbatim including "Astyanax Mexicanus" and "different"; Diversity 12(10) 395, issued 2020-10-13; CC BY 4.0 (vor); relation empty. Page: no printed licence line, metadata rights URL CC BY 3.0. Met (version difference).
- Line 4, West et al. 2022, Crossref: Aaron K. West, Emily M. Xu, Mitchell D. Nelson, Thomas R. Hart, Emelia M. Stricker, Alexandra G. Cones, Grace M. Martin, Kourtney Strickland, Devin L. Lambert, Lainey Burman, Bailey H. Zhu, Eve R. Schneider; title verbatim; Frontiers in Physiology 13, article 921657, issued 2022-06-14; CC BY 4.0 (vor); relation empty. Page licence line printed (CC BY). Met.

Bibliographic faults 0; licence faults 0. source.access "open" on all four: right.

## Names

- Equus caballus, Anas platyrhynchos (and A. p. domesticus): EXACT ACCEPTED in docs/views/gaps/gbif-names.tsv.
- Neophoca cinerea, Astyanax mexicanus: not in gbif-names.tsv; GBIF not queried. Accepted on the printed names (standard, no conflicting usage on main).
- Line 3 family: the record gives Characidae. Main files Astyanax mexicanus under "Acestrorhamphidae" in all 10 of its rows (desk-d162, d185, d187, d195), and Wikipedia's Astyanax (fish) taxobox, verbatim: "Family: Acestrorhamphidae", "Subfamily: Acestrorhamphinae". The record contradicts main's classification: counted fault.
- Line 4 rank: the domestic Pekin duck at species rank under Anas platyrhynchos is acceptable. Main already holds "Anas platyrhynchos domesticus" rows (lambda_max_nm) and files domestic chicken and quail at species rank ("Gallus gallus" 80 rows, "Gallus gallus domesticus" 48, "Coturnix japonica" 38), and the record names the domestic form in conditions.

Name faults 1 (line 3).

## Duplicates

- Line 1: no Neophoca cinerea evidence row and no ani16152342 on main (try-species.json only). Not a repeat.
- Line 2: Equus caballus on main has vision traits only (acuity_cpd, fovea, lambda_max_nm, cff_hz and others) and no sense_* row; no fvets.2020.00633; the Rørvang rows on main (intake-5) are from 10.3389/fanim.2024.1433181 (Bos taurus, Capra hircus). Heffner on main: localization and web-mammals wanted rows, none for horse hearing. The horse hearing review Timney and Macuda 2001 (10.2460/javma.2001.218.1567) is a wanted row only. Not a repeat.
- Line 3: Astyanax mexicanus on main: sense_airflow 4, sense_light_nonvisual 4, sense_hearing 1, absolute_sensitivity 1; no sense_chemical, no d12100395. Not a repeat.
- Line 4: Anas platyrhynchos on main has visual traits only; the only Anatidae sense_touch row is family-level (corrected/birds.jsonl:194); no fphys.2022.921657. Not a repeat.

Duplicates 0. Contradictions 0 (other than the line 3 family).

## Per-record findings

### Line 1, Neophoca cinerea, sense_hearing, Erbe et al. 2026

Results, verbatim: "Both individuals were most sensitive at 3.2 kHz, with thresholds of 13 and 14 dB re 20 µPa." Preceded by "The thresholds are also given in Table 1, together with ambient noise measurements." MATCH, whole sentence, 18 words; value says no more. Table 1 (frequency, Nala, Tarni, ambient noise 1/3 OBL, dB re 20 µPa), as returned: 100 Hz 72, 85, 34; 3200 Hz 13, 14, 11; 6400 Hz 14, 26, 12; 20,000 Hz 27, 51, 12. Methods, verbatim: "About 30–50% of trials were catch trials, with more catch trials near the emerging hearing threshold."; "The sound pressure level of the tone was decreased in 6 dB steps until the animal stopped responding;"; "The hearing threshold was computed as the mean of the reversal levels."; "Each frequency was tested in three sessions and the lowest threshold reported."; "We were unable to project tones >20 kHz (due to equipment limitations)". Results/Discussion, verbatim: "Across the experiment, Nala’s false alarm rate was ~20% and Tarni’s ~35%."; "Nala’s frequency band of best sensitivity (measured at 20 dB above the lowest threshold) extended from ~600 Hz to" / "probably just above 20 kHz."; the masking paragraph computes masked levels only at 6.4, 12.8 and 20 kHz and ends "However, the lowest level to which our animals responded was higher (i.e., 14 dB re 20 µPa) and hence not expected" / " to have been masked."

**Error (masking noise and false-alarm rates omitted).** At the value's frequency the chamber's ambient noise was 11 dB re 20 µPa (1/3-octave band), 2 to 3 dB under the 13 and 14 dB thresholds, and the paper's no-masking argument is made only for 6.4 to 20 kHz; the conditions give no ambient level at all. They also omit the catch-trial share and the false-alarm rates (about 20% and 35%), which bear on threshold validity, and say which animal had 13 dB "is not stated" when Table 1 gives it (Nala 13, Tarni 14), also calling the 100 Hz and 20 kHz assignments unread. Fixable.

Uncounted: the paper's "lowest level ... 14 dB" disagrees with Nala's 13 dB in Table 1 (worth a note); the method field could say threshold = mean of reversals. Grade m right (one species, two animals stated). Trait key sense_hearing fits.

Line 1: 1 fault.

### Line 2, Equus caballus, sense_hearing, Rørvang et al. 2020 (review)

Hearing section, verbatim: "The hearing ability of horses was first studied in the 1980's by Heffner and Heffner (46–48)" / "and surprisingly little research has been done on horse hearing since."; "The lowest frequency detectable by horses is 50 Hz, which is higher than the lowest human detection" / "threshold of 20 Hz." MATCH, whole sentence, 21 words. The quoted sentence carries no citation; the attribution sits on the sentence before it, to three references. Crossref's reference list for the review gives four Heffner entries: 1984 and 1986 sound-localization papers (10.1037/0735-7044.98.3.541, 10.1037/0735-7044.100.1.93), "Hearing in large mammals: horses (Equus caballus) and cattle (Bos taurus)" 1983 (10.1037/0735-7044.97.2.299), and "The hearing ability of horses" 1983 (Equine Pract., no DOI). I could not open the 1983 audiogram paper (doi.org refused, Heffner-lab pages redirected). The only independent figure I reached, the LSU hearing-range table (compiled "using data from Fay (1988) and Warfield (1973)"), gives verbatim "horse 55-33,500", not 50 Hz.

**Error (review-sourced value not a primary measurement; original not traced; no level criterion).** The value is a review's round-number restatement attributed collectively to three or four Heffner papers, two of them on localization. The record does not name the original measurement, the figure could not be checked against it, the one independent compilation reached gives 55 Hz, and a low-frequency limit without its sound-level criterion (the record says none is given) is not a fileable hearing limit. A review statement also does not support grade m. Unfixable from this source, drop; the owner should file Heffner and Heffner 1983 (10.1037/0735-7044.97.2.299, title as above, from the review's Crossref reference list) from the primary paper instead, with its level criterion and number of horses.

Line 2: 1 fault.

### Line 3, Astyanax mexicanus, sense_chemical, Blin et al. 2020

Abstract, verbatim: "Overall cavefish showed lower (i.e., better) olfactory detection thresholds than surface fish." Followed by "However, wild adult cavefish from the Pachón, Sabinos, Tinaja, Chica and Subterráneo caves showed highly variable" / "responses to the three different odorant molecules they were exposed to." MATCH, whole sentence, 12 words. The Conclusions repeat it with "Indeed, overall". Results 3.2, verbatim: "only Lab-Pachón showed a positive attractive response to the" / "low concentration of alanine 10−7 M"; "Lab-SF did not respond to alanine 10−7 M but were significantly attracted by the higher" / "concentration of 10−5 M alanine"; "Serine elicited very little, if any, response on surface and cave adult Astyanax". Discussion, verbatim: "The adult Lab-SF had a lower olfactory detection threshold than the Lab-Pachón". Methods, verbatim: "n = 8 plastic pools averaged for each graph, hence 64 fish were tested for each morphotype"; "behavioral tests were carried out in the dark (IR recordings) and in silence, in parallel," / "by three experimenters."; blinding not stated (tool summary). The record's conditions carry the contradicting Discussion sentence, the serine null, the chondroitin result, the Chica non-response and the field and lab samples. Value narrowed to Pachón is right, since only Lab-Pachón was compared with surface fish in the lab.

**Error (family).** Family "Characidae" contradicts main's 10 Astyanax mexicanus rows (Acestrorhamphidae) and the current genus placement. Fixable.

Uncounted: units "M" with a value that gives no concentration (set to ""); conditions could add 64 fish per morph, testing in the dark by three experimenters with blinding unstated, and the adult alanine result that supports the value (Lab-Pachón attracted at 1e-7 M, Lab-SF only at 1e-5 M); "(no morph difference)" for serine is the desk's inference, the paper gives no comparison. Grade m right (morphs of one species). Trait key sense_chemical fits.

Line 3: 1 fault.

### Line 4, Anas platyrhynchos (Pekin), sense_touch, West et al. 2022

Discussion, verbatim: "However, only Pekins were able to be conditioned using inedible objects of the same size and shape" / "but different hardness." MATCH, whole sentence, 20 words; value says no more. Results, verbatim: "only Pekins could successfully do the task on the unrewarded test trial" / ", spending an average of 76% of the time foraging in the correct bowl (t = 4.6, df = 8, p < 0.005, Figure 2D)."; "whereas Muscovies spent only an average of 27% of the time foraging in the correct bowl" / " and spent significantly more time foraging in the incorrect bowl (t = 3.3, df = 6, p < 0.05)."; "Thus, Pekins spent significantly more time in the correct bowl than Muscovies (t = 3.9, df = 7, p < 0.01, Figure 2E)."; "a significant difference" / " in foraging behavior between the species (Kruskal-Wallis test, p < 0.001)."; Pekins "almost exclusively used a “deep dabbling” strategy" while "Muscovy ducks shifted to a “surface dabbling” strategy". Earlier task, verbatim: "significantly more females than males were able to learn this task after 3–4 days of training" / " (Six females and one male for each species, nominal logistic fit, Chi2 = 16.7, p < 0.0001, Figure 2B)." Methods (tool summary): hard Roma plastiline against soft Prima Plastilina, no durometer or hardness values; the number of ducks on the hardness task is not stated.

**Error (effect sizes and a design confound omitted; sample misread).** The conditions give no effect size (76% against 27% time in the correct bowl, the t-tests above), omit that Muscovies spent significantly more time in the unrewarded soft bowl, and omit the species difference in foraging strategy on this very task (Kruskal-Wallis p < 0.001), which is an alternative to a tactile-discrimination reading of the Muscovy failure. They also read "Six females and one male for each species" as the earlier task's sample, when it is the count that learned that task (more females than males learning it). Fixable.

Uncounted: the df values (8 and 6) imply more ducks than the earlier task's seven successful learners per species; the paper does not reconcile them, so leave n as "not stated". Grade m right (Pekin is one named species; Muscovy is a comparison). Trait key sense_touch fits (bill tactile discrimination).

Line 4: 1 fault.

## Trait key

- Lines 1 and 2, sense_hearing: fit.
- Line 3, sense_chemical: fits (olfactory attraction).
- Line 4, sense_touch: fits.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Neophoca cinerea, sense_hearing, best 3.2 kHz, 13 and 14 dB | error, fixable | conditions, method | Quote MATCH (18 words); ambient noise at 3.2 kHz (11 dB, 2 to 3 dB below threshold) and false-alarm rates omitted; Table 1 animal assignment called unread |
| 2 | Equus caballus, sense_hearing, low limit 50 Hz | error, unfixable, drop | whole record | Quote MATCH (21 words) but a review restatement; original not named or traced, no level criterion, an independent compilation gives 55 Hz; file Heffner and Heffner 1983 instead |
| 3 | Astyanax mexicanus, sense_chemical, cavefish lower thresholds | error, fixable | family | Quote MATCH (12 words); family Characidae against main's Acestrorhamphidae (10 rows) |
| 4 | Anas platyrhynchos (Pekin), sense_touch, hardness discrimination | error, fixable | conditions | Quote MATCH (20 words); 76% vs 27% and t-tests omitted, Muscovy soft-bowl preference and foraging-strategy confound omitted, earlier-task count misread as sample |

Faults per record: line 1: 1; line 2: 1; line 3: 1; line 4: 1. 4 faults in 4 records; 4 of 4 records in error (100%): scientific-context 2 (lines 1, 4); review-sourced untraced 1 (line 2); name/classification 1 (line 3); duplicates 0; quote-form 0; licence 0; bibliographic 0; trait key 0; grading 0 counted separately (line 2's grade falls with the record).

Pooled with audits 172 to 303: 317 of 717 evidence records (44.2%; 313 of 713 before this audit, 4 of 4 here). No search records.

## Replacement text

Line 1:
- `conditions`, replace "(Table 1 gives 72 vs 85 dB at 100 Hz and 27 vs 51 dB at 20 kHz, which animal is which not read)" with "(Table 1: Nala 72 and Tarni 85 dB at 100 Hz, Nala 27 and Tarni 51 dB at 20 kHz)".
- `conditions`, replace "which animal had 13 and which 14 dB is not stated in the quote" with "Table 1 gives Nala 13 and Tarni 14 dB at 3.2 kHz; ambient noise in the chamber at 3.2 kHz was 11 dB re 20 uPa (1/3-octave band level), 2 to 3 dB below these thresholds, and the paper's critical-ratio argument against masking is made only at 6.4, 12.8 and 20 kHz (it says the lowest level the animals responded to was 14 dB, which disagrees with Nala's 13 dB in Table 1); 30 to 50% of trials were catch trials, and false alarm rates were about 20% for Nala and 35% for Tarni".
- `method`, replace "tone level lowered in 6 dB steps (staircase) until the animal stopped responding" with "tone level lowered and raised in 6 dB steps (staircase), threshold taken as the mean of the reversal levels".

Line 2: unfixable from this source, drop. Owner may file Heffner and Heffner 1983, "Hearing in large mammals: horses (Equus caballus) and cattle (Bos taurus)", DOI 10.1037/0735-7044.97.2.299 (as listed in the review's Crossref references), from the primary paper read on a permitted page, with its level criterion and number of horses.

Line 3:
- `family`, replace "Characidae" with "Acestrorhamphidae".
- `units` (uncounted), replace "M" with "".
- `conditions` (uncounted), replace "lab tests used 8 pools per morph" with "lab tests used 8 pools of 8 fish per morph (64 fish), run in the dark (IR recording) by three experimenters, blinding not stated; adult Lab-Pachon were attracted by alanine at 1e-7 M and Lab-SF only at 1e-5 M".
- `conditions` (uncounted), replace "(no morph difference)" with "(no morph comparison given)".

Line 4:
- `conditions`, replace "the number of ducks of each species trained or successful on the hardness task is not stated (the earlier two-choice task used six females and one male per species);" with "the number of ducks of each species on the hardness task is not stated (only ducks successful on the earlier task went on, and six females and one male per species learned that earlier task, more females than males, Chi2 = 16.7, p < 0.0001); in the unrewarded test Pekins spent on average 76% of the time foraging in the correct (hard-plastiline) bowl (t = 4.6, df = 8, p < 0.005) and Muscovies 27%, spending significantly more time in the soft-plastiline bowl (t = 3.3, df = 6, p < 0.05), Pekin against Muscovy t = 3.9, df = 7, p < 0.01; the species also foraged differently on this task (Pekins deep dabbling, Muscovies surface dabbling, Kruskal-Wallis p < 0.001), so the Muscovy result may reflect foraging strategy as well as tactile discrimination; hard Roma plastiline against soft Prima Plastilina, no hardness values measured;".
- `conditions`, replace "and Muscovy ducks could not perform this hardest tactile conditioning task" with "and Muscovy ducks failed only the unrewarded test".

## Owner questions (the unit's, answered where I could)

1. Names not GBIF-checked: Equus caballus and Anas platyrhynchos (and A. p. domesticus) are EXACT ACCEPTED in gbif-names.tsv; Neophoca cinerea and Astyanax mexicanus are not in it and are accepted as printed. Astyanax family should be Acestrorhamphidae, as main files it.
2. Domestic forms: the Pekin record at species rank matches main's handling (Gallus gallus, Coturnix japonica, and existing "Anas platyrhynchos domesticus" rows); not held out.
3. CC BY 3.0 page metadata against CC BY 4.0 in Crossref (lines 1, 3): accepted as a version difference, per the caller's rule.
4. Review-sourced values: on this unit's evidence, no. The horse value could not be traced to a measurement, the review cites three or four papers for it collectively, and the one independent figure reached (55 Hz) differs. File primary audiograms.
5. The unit's prompt-injection note (fphys.2022.798382 page text asking for citation extractions, not followed): noted; that page was not opened here.

## Progress note

Accurate on citations, licences and the duplicate checks. Its "only Neophocaena rows" duplicate remark is right in substance (a bare "Neophoca" grep matches Neophocaena; the only Neophoca cinerea hit is try-species.json). The Records list repeats the family-free summaries and does not carry the faults above; the horse bullet's "partial true because the primary papers were not read" misuses partial, which marks abstract-only reads.

Verdict: 4 of 4 records in error (100%), 4 faults, above the 5% bar; pooled 317 of 717 (44.2%). Error lines: 1, 2, 3 and 4. Lines 1, 3 and 4 are fixable with the replacement text above; line 2 should be dropped.

This report is model output and carries no authority.
