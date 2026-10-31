# audit-274: desk-d190 (7 evidence records, no search records, no wanted lines)

Audited 31 October 2026 from the desk-d190 files present untracked in the worktree (docs/tracks/progress/desk-d190.md and 7 evidence lines in docs/views/evidence/desk-d190.jsonl; neither committed here, neither edited). `tools/senses/check.py` on the evidence file: 7 records, 0 problems. Quote lengths (`len(q.split())`), lines 1 to 7: 19, 28, 30, 28, 25, 30, 27; all within 40. No searched or wanted file, so all seven records were judged. Rules applied: oa-audit.md "Scientific context and counting (29 October 2026)", oa-read.md (grade and `partial`), BRIEF quote rules, the publisher-copy and repository-licence rule and the name rule, in the form of audits 270 to 273. Duplicates checked with git grep on origin/main (d47aa23b) under docs/views/evidence, docs/views/audit (corrected, ALL.jsonl and the unit audit files), docs/views/searched and docs/views/wanted for "Acrocephalus scirpaceus", scirpaceus, Bianco, "Eptesicus fuscus", Capshaw, Grammostola, Mortimer, "body alignment", "age-related hearing" and the three DOIs. 2 WebSearch and 12 WebFetch calls used.

Sources opened: api.crossref.org/works/10.1098/RSPB.2024.1560 and /10.1098/RSPB.2026.0915; api.crossref.org/works/10.1007/s00359-021-01536-9 (the uppercase form returned client_error; the lowercase form answered); link.springer.com/article/10.1007/s00359-021-01536-9 (record URL, three passes); pubmed.ncbi.nlm.nih.gov/39500378/ (record URL); ora.ox.ac.uk/objects/uuid:e940b4a5-30d9-4340-9abb-dd504723c0a1 (record URL) and its version-of-record PDF file linked from that page; mammaldiversity.org/taxon/1005519 and wsc.nmbe.ch/species/37438 (both from WebSearch results). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries, so quotes were checked by MATCH/MISMATCH; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification.

## Bibliographic and licence

- Bianco et al. 2022 (lines 1 to 3), fresh Crossref: Giuseppe Bianco, Robin Clemens Köhler, Mihaela Ilieva, Susanne Åkesson; title as recorded; Journal of Comparative Physiology A 208(1): 135-144; issued 2022-01, online 2022-01-07; CC BY 4.0 tdm from 2022-01-01 and vor from 2022-01-07; relation empty; no update-to. As recorded. Springer page: "Open access", "2022 The Author(s)"; the returned excerpt did not include the Rights and permissions licence sentence. Publisher's own free copy with a Crossref CC BY vor licence, so the licence rule is met.
- Capshaw et al. 2024 (lines 4, 5), fresh Crossref: Grace Capshaw, Clarice A. Diebold, Danielle M. Adams, Jack G. Rayner, Gerald S. Wilkinson, Cynthia F. Moss, Amanda M. Lauer; title as recorded; Proc R Soc B 291(2034): 20241560; published online 2024-11-06; CC BY 4.0 vor and tdm from 2024-11-01; has-preprint 10.1101/2024.07.15.603592; no update-to. PubMed 39500378 gives the same authors and citation line. As recorded. Read from the PubMed abstract only, graded access "abstract" with `partial: true`, as the rule requires.
- Miller et al. 2026 (lines 6, 7), fresh Crossref: Thomas Miller, Stephen Rogers, Jun Wu, Alice Cicirello, Graham Keith Taylor, Beth Mortimer; title as recorded; Proc R Soc B 293(2073): 20260915; issued 2026-06-17; CC BY 4.0 vor from 2026-06-17; only has-review relations; no update-to. As recorded. ORA page: "Version of record", "CC Attribution (CC BY)"; the PDF reads "Published by the Royal Society under the terms of the Creative Commons Attribution License" (fragment), linked to CC BY 4.0. Met on the exact copy read.

Bibliographic faults 0; licence faults 0.

## Names

- Acrocephalus scirpaceus (lines 1 to 3): gbif-names.tsv holds "Acrocephalus scirpaceus fuscus EXACT ACCEPTED Acrocephalus scirpaceus" (5845861), and main's desk-d172 rows file the species at species rank. First-year migrants at a Swedish stopover; no subspecies is inferred. Accepted.
- Eptesicus fuscus (lines 4, 5): MDD taxon 1005519, "Eptesicus fuscus (Palisot de Beauvois, 1796)", valid, living; MDD notes that "further research into whether E. fuscus as currently defined represents a species complex is needed" (fragment). gbif-names.tsv EXACT ACCEPTED (2432352). Accepted; the record's note on the species-complex question is fair.
- Grammostola pulchra (lines 6, 7): World Spider Catalog, "Grammostola pulchra Mello-Leitão, 1921", Theraphosidae, valid; gbif-names.tsv EXACT ACCEPTED (2153716). Accepted.

Name faults 0.

## Duplicates

- Acrocephalus scirpaceus on main: three sense_magnetic rows in desk-d172 (10.1038/s41598-018-30477-8, virtual displacement; 10.1242/jeb.243337, forehead magnets, two rows) and SWS1 rows (oa-2:3105, oa-4:393, subspecies fuscus). 10.1007/s00359-021-01536-9, Bianco and "body alignment" are absent from main under any trait and in searched and wanted. Not a repeat.
- Eptesicus fuscus on main: sense_echolocation, acuity_cpd and absolute_sensitivity (mammal-groups:55 to 63), fovea (oa-1:3527, retracted), eye_axial_length_mm and diel (oa-1). No sense_hearing row; rspb.2024.1560 and Capshaw absent. Not a repeat.
- Grammostola pulchra on main: one sense_vibration row from this paper's abstract (docs/views/audit/corrected/spider.jsonl:194; ALL.jsonl spider:198, verdict confirm): "the non-rigid legs damp the body's own resonances, raising signal-to-noise for substrate vibration at the leg tips". Lines 6 and 7 are the frequency-specific Results findings (distal FRF near 1 across 20-200 Hz; the band limits), which the main row does not state in its value, quote or note. Not a repeat, as the desk says.

Duplicates 0.

## Per-paper findings

### Bianco et al. 2022 (lines 1 to 3)

Quotes: line 1 MATCH (Abstract); line 2 MATCH (Results and discussion), preceded by "However, the body alignment was not coinciding anymore with the W–E geomagnetic axis after the sunset." and followed by "Such SW-alignment direction (230°–241° when corrected for local magnetic declination)" (fragment); line 3 MATCH (Results and discussion), preceded by the sentence on the individual tendency to align W–E before sunset and followed by "Hence, to handle this challenge, we decided to build a series of Bayesian circular mixed-effects models" (fragment). Whole sentences, one section each, no cuts.

Methods confirmed (verbatim fragments): "between 4 and 9 September 2019"; "Birds were divided in 4 groups of 4 individuals each"; "Cages were 500 mm diameter by 700 mm height."; "built in non-magnetic material"; "the semi-transparent roof covering the experimental houses"; "for a total of 14 days"; "turn the lamps off at 19:30 (local sunset time) in the 2 control houses and 2 h later (21:30) in the 2 experimental houses"; "using a supervised machine learning algorithm"; "averaged the body-axis angles in 10-min intervals (n = 3383)". The model result "rotated by 10º toward the magnetic N–S direction" is as the records give it. The facility has Merritt coils, but the authors "did not include in our experimental design any change of the geomagnetic field polarity" (fragment); the field was recorded by a magnetometer only. The records' confound (alignment not shown to depend on the field) is therefore right, though "no coils or shielding are described" understates that coils were present and unused.

Line 1. Counted (scientific context, fixable). The paper's one manipulation is the 2 h delayed lamp-off, and its result is: "In other words, the experimental birds showed the same alignment behaviour after sunset but delayed" "by 2 h following the manipulated later sunset time" (Results and discussion, two verbatim fragments of one sentence). Experimental birds showed no preferred direction from 20:30 to 21:30 and a weaker pre-sunset alignment, which the authors suggest may reflect the unnaturally long days (tool summary). The record describes the delayed-sunset design but never gives this result, and its value says alignment shifts "afterwards" relative to "sunset" without saying that sunset here means lamp-off and that the shift followed lamp-off rather than local sunset or clock time. That changes the causal reading of the record's own headline (the paper's question is the time of day), so it is material under the 29 October rule.

Line 2. Confirm. Control group only, as the record says; the value stays within the quote.

Line 3. Confirm. Null at the individual level, with the -22 degree mean shift (confirmed: "− 22° on average", fragment) and the reason stated; it is filed as its own record beside the positive model result.

### Capshaw et al. 2024 (lines 4, 5)

Both quotes MATCH the PubMed abstract and are whole sentences. The abstract says the authors "used DNA methylation to estimate the ages of wild-caught big brown bats" (fragment), gives no sample sizes and no frequencies, reports no measure that differed with age, and closes on "minimal evidence for age-related hearing loss" (fragment). Grade m, access abstract and `partial: true` are right; the records say no more than the abstract, and the conditions name what the abstract leaves out.

Line 4. Confirm. Uncounted: the value reads "no hearing deficits up to 12.5 years"; the quote says "no evidence for hearing deficits". The conditions already state "a finding of no evidence for deficits", so the limitation is conveyed elsewhere in the record; tighten the value (below).
Line 5. Confirm. Uncounted: the shared conditions text describes ABR and DPOAE and not the histology; harmless, since `method` names the histology.

### Miller et al. 2026 (lines 6, 7)

Both quotes MATCH in Section 3 (Results), whole sentences; line 7's sentence opens the Results. Methods (Section 2a): "We used one specimen of G. pulchra Mello-Leitão, 1921." (verbatim); from the authors' captive lab population; alive, not tethered or restrained, not anaesthetised (Figure 1 caption, tool summary); mass measured but not reported, sex not stated (tool summary); Modal Shop K2004E01 shaker, aluminium plate 95 mm diameter and 4 mm thick, square-wave pulse of about 0.0005 s, 50 vertical points, three repeats per point (two for 3 points), Polytec VibroOne, vertical axis, 25.6 kHz sampling (tool summary). The proximal and body segments show FRF magnitude above 1 from 20 to 80 Hz and below 1 above 80 Hz (tool summary), which is the contrast the main row's abstract claim rests on. "Biologically relevant up to 1000 Hz" was not checked.

Line 6. Confirm. The value stays within the quote; the one-specimen, vertical-axis and mechanical-not-neural limits are stated. Uncounted: say the spider was alive and unrestrained, and that mass was measured but not reported (the record says "not stated").
Line 7. Counted (scientific meaning, fixable). The first half of the value, "below 20 Hz the FRFs of all segments are dominated by noise", is a property of the measurement (the paper's reason for analysing 20-200 Hz only), and says nothing about how the spider's body moves below 20 Hz. Filed as a sense_vibration value for the species, with a note calling it "a limit of the measurement as well as of the spider's body response", it reads as a finding that the spider's body does not respond below 20 Hz. The note's claim is not in the text. Only the above-200 Hz half (no obvious resonances, low amplitude) describes the body.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Acrocephalus scirpaceus, alignment shifts after sunset | correct | value, conditions | Quote MATCH; the delayed-lamp-off result (shift came 2 h later, following lamp-off) is omitted, so "sunset" is not shown to mean lamp-off |
| 2 | Acrocephalus scirpaceus, controls keep NE-SW through the dark | confirm | (conditions; uncounted) | Quote MATCH; control group only, said so |
| 3 | Acrocephalus scirpaceus, individual-level null | confirm | (conditions; uncounted) | Quote MATCH; null filed with reason and the -22 degree mean |
| 4 | Eptesicus fuscus, no hearing deficit to 12.5 years | confirm | (value; uncounted) | Quote MATCH in abstract; "no evidence for" already carried in conditions |
| 5 | Eptesicus fuscus, no histological cochlear ageing | confirm | none | Quote MATCH in abstract |
| 6 | Grammostola pulchra, distal FRF near 1 across 20-200 Hz | confirm | (conditions; uncounted) | Quote MATCH; one specimen and mechanical limits stated |
| 7 | Grammostola pulchra, noise below 20 Hz, low amplitude above 200 Hz | correct | value, note | Quote MATCH; the sub-20 Hz half is measurement noise, presented as a body response in the note |

Evidence errors: 2 of 7 (28.6%): scientific-context or meaning faults 2 (lines 1, 7); quote-form 0; name 0; duplicates 0; licence 0; bibliographic 0; abstract-access grading 0. Unfixable records: none.

Pooled with audits 172 to 273: 224 of 550 evidence records (40.7%; audit 273's 222 of 543 plus 2 of 7 here; any audit running concurrently is not included). No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Counted (line 1):
- `value`: "magnetic body alignment occurs prior to sunset and shifts to a more northeast-southwest alignment afterwards (pooled model: about 10 degrees toward magnetic N-S); 'sunset' is lamp-off, and in birds given a 2 h delayed lamp-off the same shift came 2 h later"
- `conditions`: replace "The abstract sentence is a pooled model result;" with "The abstract sentence is a pooled model result. In the experimental houses the same alignment change came after the delayed lamp-off: 'the experimental birds showed the same alignment behaviour after sunset but delayed ... by 2 h following the manipulated later sunset time' (Results and discussion), so the shift followed the light schedule rather than local sunset; the experimental birds' pre-sunset alignment was weaker, which the authors suggest may reflect the 2 h longer days;"

Counted (line 7):
- `value`: "above 200 Hz the FRFs of all segments show no obvious resonances and have low amplitude; below 20 Hz no body response was resolved (FRFs dominated by measurement noise), so the analysis band is 20-200 Hz"
- `note`: replace "Sets the analysis band (20-200 Hz) used for the other findings; a limit of the measurement as well as of the spider's body response." with "Sets the analysis band (20-200 Hz) used for the other findings. The sub-20 Hz noise is a limit of the measurement and says nothing about the body's response there; only the above-200 Hz half describes the body."

Uncounted:
- Lines 1 to 3 `conditions`: replace "circular cage (500 mm by 700 mm)" with "circular cage (500 mm diameter, 700 mm high)"; replace "in the Methods passages read no coils or shielding are described, so" with "the facility's Merritt coils were not used and the field was not changed in either group, so".
- Line 4 `value`: replace "no hearing deficits up to 12.5 years of age" with "no evidence for hearing deficits up to 12.5 years of age".
- Lines 6 and 7 `conditions`: replace "sex and mass are not stated in the Methods passages read" with "the spider was alive, unrestrained and not anaesthetised; sex is not stated and mass was measured but not reported"; add "plate 95 mm diameter, 4 mm thick; 25.6 kHz sampling".

## Owner questions

1. Bianco 2022 measures alignment in an unmanipulated geomagnetic field (coils available, not used). Should spontaneous alignment without a field manipulation stay under sense_magnetic, as the desk filed it with the confound stated, or be held for a field-manipulation study?
2. Main's spider.jsonl:194 row from Miller 2026 gives "Miller TE" and "Wu JJ"; Crossref has "Thomas Miller" and "Jun Wu" with no middle initials. Correct the main row's initials at the next corrected-file pass?
3. Lines 4 and 5 rest on the abstract only. Is a full-text read (royalsocietypublishing.org or PMC, both refused in earlier units) wanted before merge, to check for frequency-specific exceptions the abstract does not report?

Progress note: accurate on sources, licences, names and the not-a-repeat reasoning; it omits the delayed-sunset result in its Bianco summary and lists the sub-20 Hz noise among the spider's Results findings.

Verdict: 2 errors in 7 (28.6%), above the 5% bar; pooled 40.7%. Error lines: 1, 7. No unfixable records; lines 1 and 7 can merge with the counted text, and lines 2 to 6 as they stand or with the uncounted fixes.

This report is model output and carries no authority.
