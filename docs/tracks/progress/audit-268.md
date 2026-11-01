# audit-268: desk-d184 (10 evidence records, no search records, no wanted lines)

Audited 31 October 2026 from the desk-d184 files present untracked in the worktree (docs/tracks/progress/desk-d184.md and 10 evidence lines in docs/views/evidence/desk-d184.jsonl; neither committed here, neither edited). `tools/senses/check.py` on the evidence file: 10 records, 0 problems. Quote lengths (`len(q.split())`), lines 1 to 10: 26, 16, 26, 17, 35, 21, 20, 34, 37, 37; all within 40. No searched or wanted file, so all ten records were judged. Rules applied: oa-audit.md "Scientific context and counting (29 October 2026)", oa-read.md (grade and `partial`), BRIEF quote rules, the publisher-copy licence rule and the name rule, in the form of audits 265 to 267. Duplicates checked with git grep on origin/main (4c024488) under docs/views/evidence, docs/views/audit/corrected, docs/views/audit/ALL.jsonl, docs/views/searched and docs/views/wanted for Amblydoras, Megalodoras, "Silurus glanis", "Cyprinus carpio", "Spheniscus humboldti", pone.0067049, pone.0108583, 82942, Zebedin, Maiditsch, Rößler/Rossler/Roessler. 4 WebSearch and 12 WebFetch calls used.

Sources opened: api.crossref.org/works/ 10.1371/JOURNAL.PONE.0067049, 10.1371/JOURNAL.PONE.0108583, 10.1038/S41598-024-82942-2; journals.plos.org for both PLOS DOIs (record URLs; the returned title was checked first each time and was the right article: Zebedin one pass, Maiditsch two passes); nature.com/articles/s41598-024-82942-2 (record URL, one pass); Catalog of Fishes spid 5640 and 5889 (returned by my WebSearches); gbif.org/uk/species/2337607 (returned by my WebSearch). Two further Catalog of Fishes pages returned by a search (spid 5471, 5514) were other Linnaean Silurus names (Clarias anguillaris, Ameiurus catus), so no Catalog of Fishes entry for Silurus glanis was read. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened; nothing was refused. WebFetch returns model summaries, so quotes were checked by MATCH/MISMATCH; points marked "(tool summary)" were not returned verbatim.

## Bibliographic and licence (Crossref, fresh)

- Zebedin: Angelika Zebedin, Friedrich Ladich; "Does the Hearing Sensitivity in Thorny Catfishes Depend on Swim Bladder Morphology?"; PLoS ONE 8, issue 6, e67049; issued and online 2013-06-25; licence creativecommons.org/licenses/by/4.0, content-version unspecified, from 2013-06-25; relation empty, no update-to. As recorded. Page: "This is an open-access article distributed under the terms of the Creative Commons Attribution License". Accepted.
- Maiditsch: Isabelle Pia Maiditsch, Friedrich Ladich; title as recorded; PLoS ONE 9, issue 9, e108583; issued 2014-09-25; CC BY 4.0, content-version unspecified; relation empty, no update-to. As recorded. Page prints the same Creative Commons Attribution statement. Accepted.
- Rößler: Helen Rößler, Anne May, Michael Dähne; title as recorded; Scientific Reports 14, issue 1, 30592; online 2024-12-23; CC BY 4.0 vor and tdm from 2024-12-23, delay 0; relation has-preprint 10.21203/rs.3.rs-4831042/v1; no update-to. As recorded. The page shows "Open access" and "2024 The Author(s)" but no licence line, as the record says; accepted on Crossref vor CC BY with the publisher's own free copy, as audit 249 accepted the same paper.

Bibliographic faults 0; licence faults 0.

## Names

- Amblydoras affinis: Catalog of Fishes spid 5640, "Current status: Valid as Amblydoras affinis (Kner 1855)." Doradidae: Doradinae. As recorded.
- Megalodoras uranoscopus: spid 5889, "Current status: Valid as Megalodoras uranoscopus (Eigenmann & Eigenmann 1888)." As recorded.
- Silurus glanis: GBIF backbone 2337607, Silurus glanis Linnaeus, 1758, Siluridae, shown as the main entry with synonyms beneath (my fetch did not return the word "Accepted" verbatim; the desk's page read did). Not in gbif-names.tsv. No doubt about the name; uncounted.
- Cyprinus carpio (4286975) and Spheniscus humboldti (5229386): EXACT, ACCEPTED in docs/views/gaps/gbif-names.tsv.
- Carp identity: Methods say the carp came from a private fish pond near Vienna (tool summary); no koi, ornamental strain or hybrid is mentioned. The catfish came from a hatchery (Fischzucht Pottenbrunn, Austria). Neither is a cultivar or hybrid record. The carp lines' note words "Domesticated common carp, juveniles" are not supported by any sentence I read (uncounted fix below).

Name faults 0; cultivar or pooled 0.

## Duplicates

- Rößler et al. 2024 is on main as docs/views/evidence/desk-d164.jsonl line 4 (merged after audit 249): Spheniscus humboldti, sense_hearing, value [250, 10000] Hz, same DOI, same Abstract quote. desk-d184 line 9 repeats it (same value, same quote). The main row's note already states "an unexpectedly low threshold at 0.250 kHz (mean 36.8 dB) after a rapid decline at 0.500 kHz (mean 64.1 dB)" and that the authors cannot say whether it is an artefact, and its conditions say "the 0.250 kHz mean rests on n = 3 (SD 2.4 dB)". desk-d184 line 10 is that same finding filed again as a record. Lines 9 and 10 repeat main. The desk's progress note ("none of these species-and-paper pairs is on main") is wrong for this paper.
- Zebedin 2013, Maiditsch 2014, Amblydoras, Megalodoras, Silurus glanis: nothing on main. Cyprinus carpio on main: lambda_max_nm rows (other papers) and one sense_hearing row, desk-d160 line 6 (Vetter et al. 2018, n = 3 reference carp, lowest threshold at 400 Hz among nine frequencies, 300 and 500 Hz not tested, 19 to 22 °C). Different paper; 400 Hz lies inside 0.3 to 1 kHz, so no repeat and no contradiction.

Duplicates: 2 (lines 9, 10).

## Per-paper findings

### Zebedin and Ladich 2013 (lines 1 to 3)

Quotes. Line 1 and 3 quote MATCH (Results, Auditory Sensitivity); line 2 MATCH (same section). Whole sentences. Lines 1 and 3 use one sentence for two species, each logging only its own species: allowed.

Context confirmed (tool summary): Methods, Animals give N = 7 for A. affinis and N = 9 for M. uranoscopus, with "three to nine for hearing measurements"; frequencies 0.07, 0.1, 0.3, 0.5, 1, 2, 3, 4, 5 and 6 kHz; 25 ± 1 °C; fish "mildly immobilized with Flaxedil"; test in a bowl-shaped tub 33 cm in diameter with 13 cm water depth, two speakers "installed 0.5 m above the fish", hydrophone 2 cm from the fish; sound pressure only, particle motion neither measured nor discussed. Species differed (two-way ANOVA F5,320 = 50.913, p<0.001); relative swim bladder length correlated with thresholds at 70 Hz, 100 Hz and 4 to 6 kHz, with "No significant relationship between relative swim bladder size and hearing ... between 0.3 and 3 kHz". M. uranoscopus's 1 kHz threshold is in Table 2, not read.

The best-frequency values (0.5 kHz, 1 kHz) and the 59.6 dB minimum lie inside the tested set (0.07 to 6 kHz) and match the sentences. Otophysan catfish detect sound pressure through the Weberian apparatus, so pressure-only thresholds are the appropriate measure; the small shallow tub with speakers in air is a known source of distorted fields but the paper gives no correction and the best-frequency reading does not depend on it. Uncounted: add temperature, tub and pressure-only to `conditions` (text below); the "per-species hearing n not read" clause can now be resolved to the Methods N.

### Maiditsch and Ladich 2014 (lines 4 to 8)

Title confirmed on both fetches. Quotes: line 4 MATCH (Results, Auditory sensitivities, Silurus glanis); line 5 MATCH (same); line 6 MATCH (Comparison between C. carpio and S. glanis; the same sentence is also in the Abstract); line 7 MATCH (Cyprinus carpio); line 8 MATCH (same). Whole sentences.

Unnamed species (lines 4 and 7). Each best-hearing sentence opens its paragraph directly under the species subheading ("Silurus glanis", "Cyprinus carpio") and names no species. The `where` field names the subsection and the note says the sentence does not name the species, so the taxon is traceable to the source's own structure, and the value (a frequency band) is contained in the quote. Accepted, as the desk handled it. Line 5 and line 8 are under the same subheadings and the notes say so.

Context confirmed (tool summary): both species tested at 0.1, 0.3, 0.5, 0.8, 1, 2 and 4 kHz; acclimated at 20 °C for over a month, changed 1 °C per day, at least three weeks at each test temperature; runs 15 °C, 25 °C, 15 °C repeated; the two 15 °C audiograms did not differ in either species; test tub 45 × 35 cm, 18 cm high, sand bottom, speaker 1 m above the tub, hydrophone about 2 cm from the fish; sound pressure only, no particle motion.

Verbatim from the Comparison subsection:
- "Both C. carpio and S. glanis showed no change in sensitivity at the lowest frequency measured (100 Hz) when the temperature increased from 15°C to 25°C (Repeated measures ANOVA)." (returned in two fragments, rejoined)
- "A significant increase was found at higher frequencies except for 4 kHz in the carp."
- "In C. carpio the main change in sensitivity was observed between 0.3 and 2 kHz, whereas in the S. glanis changes of more than 5 dB were found up to 4 kHz." (rejoined)
- "Hearing sensitivity improved to a higher degree in C. carpio at 1 and in S. glanis at 2 and 4 kHz."

Line 5 (S. glanis, sensitivity lower at lower temperatures). The value states a general lowering with an interaction term. The paper's null at 100 Hz (no change with temperature) is an exception that limits the claimed effect, and neither the value nor the note gives it; "Temperature shifts sensitivity" in the note implies it applies throughout. Counted scientific-context fault (fixable). Uncounted: the catfish interaction is printed F7,176 while the carp's is F12,168 with the same 3 temperatures × 7 frequencies design (expected interaction df 12); a likely printing slip in the paper, which the record copies faithfully.

Line 6 (S. glanis maximum gain 10.3 dB at 0.5 kHz). Value right. The quote does not say what increased; the value's "in sensitivity with temperature" comes from the preceding sentences of the same paragraph, and the note says so. Treated as a referent supplied from adjacent text that changes no number, so uncounted; the fix below moves the referent into `note` and keeps the value to the quote's words.

Line 7 (C. carpio best 0.3 to 1 kHz). Value right. Uncounted: replace "Domesticated common carp, juveniles" (not in the text I read) with the source's origin.

Line 8 (C. carpio sensitivity lower at 15 °C). Same omission as line 5, larger here: no change at 100 Hz and none at 4 kHz, so the temperature effect was significant at only five of seven frequencies, with the main change between 0.3 and 2 kHz. The note's "The effect is smaller in carp than in the catfish" is also too broad: the paper says carp improved more than the catfish at 1 kHz. Counted scientific-context fault (fixable).

### Rößler, May and Dähne 2024 (lines 9 and 10)

Quotes MATCH (Abstract), whole sentences. Results (tool summary of verbatim fragments): "mean sensitivity at 0.250 kHz was 37 dB rms re 20 µPa (SD ± 2.4 dB, n = 3"; 0.500 kHz "a mean value of 64 dB rms re 20 µPa (SD ± 9 dB, n = 4)"; Figure 3 caption: "Not all frequencies were usable for all individuals"; no 125 Hz result reported; Discussion: "Accuracy of all birds was already low at 10 kHz and 0.500 kHz at the loudest possible sound pressure level of the set up." Line 10's note says "n = 4, in air" for a mean that rests on n = 3, a misstatement (counted within the duplicate, not separately). Both lines are repeats of main desk-d164:4 and cannot be fixed by a field change: drop.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Amblydoras affinis, lowest thresholds at 0.5 kHz | confirm | (conditions; uncounted) | Quote MATCH, Results; 0.5 kHz inside 0.07 to 6 kHz tested set; tub, 25 °C, pressure-only could be added |
| 2 | Amblydoras affinis, 59.6 dB re 1 µPa at 0.5 kHz | confirm | (conditions; uncounted) | Quote MATCH; "lowest of the study" scoped to six species in note |
| 3 | Megalodoras uranoscopus, best at 1 kHz | confirm | (conditions; uncounted) | Quote MATCH; only own species logged |
| 4 | Silurus glanis, best 0.3 to 1 kHz | confirm | none | Quote MATCH under the species subheading; where and note say the sentence does not name the species |
| 5 | Silurus glanis, lower sensitivity at 15 °C | correct | value, note | Quote MATCH; omits the paper's no change at 100 Hz (Results, Comparison subsection), an exception limiting the claimed temperature effect |
| 6 | Silurus glanis, max gain 10.3 dB at 0.5 kHz | confirm | (value, note; uncounted) | Quote MATCH; "in sensitivity with temperature" supplied from adjacent sentences, number unchanged |
| 7 | Cyprinus carpio, best 0.3 to 1 kHz | confirm | (note; uncounted) | Quote MATCH under the species subheading; pond-origin carp, no koi or hybrid; "domesticated, juveniles" unsupported |
| 8 | Cyprinus carpio, lower sensitivity at 15 °C | correct | value, note | Quote MATCH; omits no change at 100 Hz and at 4 kHz (Results, Comparison subsection); note's "effect is smaller in carp" contradicted at 1 kHz |
| 9 | Spheniscus humboldti, 250 to 10000 Hz | duplicate (drop) | whole record | Same paper, trait, value and quote as main desk-d164:4 |
| 10 | Spheniscus humboldti, 36.8 dB at 0.25 kHz after 64.1 dB at 0.5 kHz | duplicate (drop) | whole record; note | Finding, values and artefact caveat already in main desk-d164:4 note and conditions; also gives n = 4 where the 0.25 kHz mean rests on n = 3 |

Evidence errors: 4 of 10 (40.0%): duplicates 2 (lines 9, 10); scientific-context faults 2 (lines 5, 8); quote-form 0; licence 0; bibliographic 0; name 0; pooled or cultivar 0. Unfixable records: lines 9 and 10 (drop as repeats of main). Lines 5 and 8 are fixable with the counted text below.

Pooled with audits 172 to 267: 203 of 506 evidence records (40.1%; audit 267's 199 of 496 plus 4 of 10 here). No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Counted (line 5):
- `value`: "auditory sensitivity significantly lower at the lower temperatures (two-factorial ANOVA F2,176 = 346.6, p<0.001), with a significant temperature by frequency interaction (F7,176 = 4.313, p≤0.001); no change at 100 Hz, the lowest frequency tested"
- `note`: replace "Temperature shifts sensitivity, so audiograms from other temperatures differ." with "Exception: 'Both C. carpio and S. glanis showed no change in sensitivity at the lowest frequency measured (100 Hz) when the temperature increased from 15°C to 25°C (Repeated measures ANOVA).' (Results, Comparison between C. carpio and S. glanis). Catfish changes exceeded 5 dB up to 4 kHz, and improved more than the carp at 2 and 4 kHz. The two 15 °C audiograms did not differ. The interaction df is printed as 7,176, against 12,168 for the carp's identical design; reproduced as printed."

Counted (line 8):
- `value`: "auditory sensitivity significantly lower at 15 °C (two-factorial ANOVA F2,168 = 36.9, p≤0.001), with a significant temperature by frequency interaction (F12,168 = 3.05, p≤0.001); no change at 100 Hz or at 4 kHz, main change between 0.3 and 2 kHz"
- `note`: replace "The effect is smaller in carp than in the catfish in the same paper (the carp maximum increase was 7.8 dB at 0.8 kHz)." with "Exceptions: no change at 100 Hz in either species (Repeated measures ANOVA) and 'A significant increase was found at higher frequencies except for 4 kHz in the carp.'; 'In C. carpio the main change in sensitivity was observed between 0.3 and 2 kHz' (Results, Comparison between C. carpio and S. glanis). Carp maximum increase 7.8 dB at 0.8 kHz; the improvement differed between species (F1,105 = 6.35, p<0.05) and was greater in carp at 1 kHz and in the catfish at 2 and 4 kHz."

Uncounted:
- Lines 1 to 3 `conditions`: replace "per-species hearing n not read)" with "hearing n per species within the stated three to nine); water 25 ± 1 °C; tested at 0.07, 0.1, 0.3, 0.5, 1, 2, 3, 4, 5 and 6 kHz in a bowl-shaped tub 33 cm in diameter, 13 cm deep, speakers in air 0.5 m above the fish, hydrophone 2 cm from the fish; sound pressure only, particle motion not measured".
- Lines 4 to 8 `conditions`: append "; tested at 0.1, 0.3, 0.5, 0.8, 1, 2 and 4 kHz in a 45 × 35 cm tub (18 cm high, sand bottom), speaker 1 m above, hydrophone about 2 cm from the fish; sound pressure only, particle motion not measured; at least three weeks at each test temperature; the two 15 °C audiograms did not differ".
- Line 6 `value`: "maximum increase at 0.5 kHz (10.3 dB)"; `note`: prepend "The increase is the gain in sensitivity from 15 °C to 25 °C (Results, Comparison between C. carpio and S. glanis, preceding sentences; also in the Abstract)."
- Line 7 `note`: replace "Domesticated common carp, juveniles; underwater sound." with "Carp from a private fish pond near Vienna (Methods); no strain, koi or hybrid stated; underwater sound."

## Owner questions

1. Line 10 type of repeat: the main row desk-d164:4 carries the 0.250 kHz finding in its note and conditions, not in its value. I counted a separate record of a finding already stated on main as a repeat (as audit 267 did for a finding carried in a main value). If the owner wants the 0.250 kHz threshold as its own row, it should be filed with n = 3 and the output-ceiling caveat, not as line 10 stands.
2. Maiditsch 2014 prints the catfish interaction as F7,176 and the carp's as F12,168 for the same 3 × 7 design. Keep as printed with the note, or drop the df from the value?

Progress note: accurate on what was read and on the species-heading handling; wrong that none of the species-and-paper pairs is on main (Rößler 2024 is desk-d164:4).

Verdict: 4 errors in 10 (40.0%), above the 5% bar; pooled 40.1%. Error lines: 5, 8, 9, 10. Lines 9 and 10 are unfixable (drop as repeats of main); lines 5 and 8 can merge with the counted text; lines 1 to 4, 6 and 7 can merge with the uncounted fixes.
