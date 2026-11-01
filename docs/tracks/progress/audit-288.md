# audit-288: desk-d204 (4 evidence records, no search records, no wanted lines)

Audited 31 October 2026 from the desk-d204 files present untracked in the worktree (docs/tracks/progress/desk-d204.md and 4 evidence lines in docs/views/evidence/desk-d204.jsonl; neither committed here, neither edited). HEAD 592c9260 equals origin/main. `tools/senses/check.py` on the evidence file: 4 records, 0 problems. Quote lengths (`len(q.split())`): 20, 10, 15, 19, all within 40. No searched or wanted file, so every record was judged and there is no sample to draw. Rules applied: oa-audit.md "Scientific context and counting (29 October 2026)", oa-read.md and BRIEF (whole sentence, 40 words, grade, `partial`), desk-audit.md (no 125-character limit) and the publisher-copy licence rule; the shared brief's plant-screening items are superseded for this animal unit, and /tmp/desk/unit_brief.md names no animal authority, so GBIF Backbone pages (the authority the record itself cites) were read for the earthworm. Duplicates checked with git grep on origin/main across docs/views (evidence, audit including corrected/ and ALL.jsonl, searched, wanted, gaps, sheets), views/, src/ and docs/tracks for "Sebastes schlegelii", "S. schlegelii", "black rockfish", "Sebastes", "Dendrobaena", "veneta", "hortensis", "Eisenia", "earthworm", "Lumbric", "Anoplophora glabripennis", "A. glabripennis", "Asian longhorn", the DOI suffixes 1257473, 1202410 and 16080781, and the title words "carbon dioxide detection" and "Host Plant Volatiles Evoking", every trait included, and the notes and conditions of the main rows found. 2 WebSearch and 9 WebFetch calls used.

Sources opened: api.crossref.org/works/10.3389/FMARS.2023.1257473, /10.3389/FEVO.2023.1202410 and /10.3390/INSECTS16080781 (all answered in uppercase, none robots_disallowed); the three record URLs (frontiersin.org PDFs for records 1 to 3, www.mdpi.com/2075-4450/16/8/781/htm for record 4), one pass each; for names gbif.org/species/7725323 (Dendrobaena hortensis), gbif.org/ru/species/5739805 (Dendrobaena veneta) and en.wikipedia.org/wiki/Dendrobaena_hortensis, all returned by my WebSearches; one plazi treatment page returned only a redirect notice (not followed). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries, so quotes were checked as MATCH/MISMATCH; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification.

## Bibliographic and licence

- Wang, Huang, Xing 2023 (line 1), fresh Crossref: Yining Wang, Liuyi Huang, Binbin Xing, in the recorded order; title "Experimental study on the effect of sound stimulation on hearing and behavior of juvenile black rockfish (Sebastes schlegelii)" as recorded (returned in two chunks that join to the recorded string); Frontiers in Marine Science 10, article number 1257473, no issue; issued and online 2023-12-05; licence CC BY 4.0 (vor); relation empty; no update-to.
- Smith et al. 2023 (lines 2, 3): Emily Jordan Smith, Jennifer L. Ryan, Sofia A. Lopresti, Dastan B. S. Haghnazari, Karleigh A. S. Anderson, Sarah J. Lipson, Erik C. Johnson, Wayne L. Silver, Cecil J. Saunders, in order; title "Mechanisms of carbon dioxide detection in the earthworm Dendrobaena veneta" verbatim; Frontiers in Ecology and Evolution 11, article number 1202410, no issue; issued 2023-11-29; CC BY 4.0 (vor); relation has-preprint 10.1101/2023.04.12.536649; no update-to.
- Zhang et al. 2025 (line 4): Rui Zhang, Jian-Ming Shi, Yi-Bei Jiang, Hui-Quan Sun, Dan-Dan Cao, Hui-Ling Hao, Jian-Rong Wei, in order; title verbatim as recorded; Insects 16(8), page 781; issued 2025-07-30; CC BY 4.0 (vor); relation empty; no update-to.

Licence on the copy read: both Frontiers PDFs carry "This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY)."; the MDPI page has no licence sentence in its text and a metadata rights field of CC BY 3.0, the site-wide tag audits 276 and 287 noted. Publisher's own CC BY copy on all four; met, and the notes state each correctly. Uncounted: the earthworm notes could mention the bioRxiv preprint relation.

Bibliographic faults 0; licence faults 0.

## Names

- Sebastes schlegelii (line 1) and Anoplophora glabripennis (line 4): the paper's names; A. glabripennis is in docs/views/gaps/gbif-names.tsv (EXACT ACCEPTED, 7572133). Sebastes schlegelii is not in the table and was not checked further here; no question raised about it. Accepted.
- Dendrobaena (lines 2, 3): **counted on both lines.** The paper names its worms Dendrobaena veneta and says the species was "previously known as Eisenia hortensis" (keywords list Eisenia hortensis too; tool summary with fragment). The records are filed as Dendrobaena hortensis because, the note says, GBIF 7725323 shows D. hortensis as accepted and "treats veneta as a synonym". It does not. GBIF 7725323, "Dendrobaena hortensis (Michaelsen, 1890)", lists as synonyms Allolobophora hortensis, Allolobophora subrubicunda hortensis, Allolobophora veneta hortensis, "Dendrobaena veneta hortensis Gerard, 1964", Eisenia hibernica, "Eisenia hortensis (Michaelsen, 1890)" and three Eisenia veneta trinomials; D. veneta itself is not among them. GBIF 5739805, "Dendrobaena veneta (Rosa, 1886)", is a separate species entry in the same Backbone with its own synonyms (Allolobophora veneta Rosa, 1886, Helodrilus venetus and others). So GBIF holds two species, and the paper's own two names point at different ones: its binomial is D. veneta, while its "previously Eisenia hortensis" points at D. hortensis. Wikipedia's D. hortensis page says the two are "probably not distinguished" in vermicomposting and that hortensis is the more common name in North America (tool summary). Which species the worms were cannot be settled from the paper. Filing under D. hortensis on a GBIF reading the page does not support is the fault; neither name is in gbif-names.tsv, so the final name is an owner question (below). Fix: taxon "Dendrobaena veneta" as printed, with the note below, unless the owner rules otherwise.

Name faults 2 (lines 2 and 3, one cause).

## Duplicates

- Sebastes schlegelii: no evidence or audit row on main under any trait. The same paper and value appear only in docs/tracks/progress/desk-d203.md lines 15, 27 and 34 as a held lead (quote not confirmable then). Not a repeat.
- Dendrobaena, Eisenia, the paper's DOI and title: none on main. Earthworm rows on main are Lumbricus terrestris (light, eye_type, behaviour_vision) and Diplocardia (vibration), other species and papers. Not a repeat.
- Lines 2 and 3 against each other: different findings from one paper (line 2 the dose-response to 0 to 100% CO2, line 3 the reduction of that response by acetazolamide). Not one finding twice. Confirm both as separate rows.
- Anoplophora glabripennis on main: desk-d192:5 and 6 (behaviour_vision, LED trapping, Jiang et al. 2023, Insects 14(5): 465) and oa-1:4370 to 4372 with their recheck copies (opsin_sequences_recovered, Sharkey et al. 2017; retracted for a citation fault in audit/ALL 5676 to 5678). No sense_chemical row, no row or note from Zhang et al. 2025 (DOI suffix 16080781 absent from main), and no EAG finding in the d192 notes. Not a repeat.

Duplicates 0. Contradictions 0.

## Per-paper findings

### Wang, Huang, Xing 2023, Sebastes schlegelii (line 1)

Results 3.1 "Sensitive sound frequency and hearing threshold", verbatim: "However, beyond 200 Hz and up to 500 Hz, the thresholds showed a tendency to rise, implying that the fish had higher auditory thresholds in this frequency range." then "Of particular interest is the lowest threshold observed at 200 Hz, which was measured to be 86.4 ± 3.4 dB.", which ends the paragraph. Abstract: "the most sensitive sound frequency was 200 Hz, with the lowest hearing threshold recorded at 86.4 ± 3.4 dB re 1 mPa." Methods (verbatim fragments): "standard length: 6.99 ± 0.51 cm; wet mass: 19.47 ± 2.93 g."; "short alternating tone bursts with frequencies of 100 Hz, 200 Hz, 300 Hz, and 500 Hz."; "The lowest sound pressure level (SPL) at which a repeatable AEP trace could be obtained was considered the threshold."; fish anaesthetised with MS-222 (1:14000) until movement ceased and then "temporarily immobilized by injecting gallamine triiodide" at 1.2 to 1.4 mg/g; 8 AEP cases, one death, waveforms from 7 fish (tool summary); 16 fish later split into "a noise-exposed group and a controlled and sheltered group" (200 Hz tones at 110 dB for 7 days); "Water temperature was 21.4-22.8°C" during rearing; fish from Dalian Tianzheng Industrial Co., Ltd. (acknowledgements).

Quote. MATCH, whole sentence, last of its paragraph, one section, 20 words, no cuts; contains the value; the value says no more. Quote-form 0.

Line 1. Counted (scientific context; fixable). `units` says the reference level is "not given in the quoted sentence", but the paper states it in the abstract's version of the same result ("dB re 1 mPa", as printed; µPa is the usual underwater reference and mPa is probably a misprint, which the record should say rather than leave the dB unreferenced). `conditions` also omits that the fish were anaesthetised with MS-222 and paralysed with gallamine triiodide for recording, a design fact that bears on any AEP threshold, and that the thresholds come from 7 fish with usable waveforms. Grade m right; `partial` false right.

Uncounted: "about 7 cm standard length" can carry the measured 6.99 ± 0.51 cm and 19.47 ± 2.93 g; the fish came from a commercial company (farm or wild origin not stated); the water temperature is stated for rearing, not the test.

### Smith et al. 2023, Dendrobaena (paper: D. veneta) (lines 2, 3)

Results, "CO2 aversion": "Earthworms excreted the most exudate in response to 100% CO2." is the section's first sentence; dose-dependent rise "(p<0.0001, n=12-20, two-way ANOVA)"; 25% CO2 gave no significant response; 0% is room air (tool summary). Methods and the Figure 1C caption call the CO2-series test one-way ANOVA (tool summary), as `conditions` says. Results, "Pharmacology": "The broad-spectrum CA inhibitor acetazolamide significantly muted the response to CO2" (Figure 7A, p<0.01, n=8-13). Pharmacology design (tool summary): worms soaked 10 minutes in 5 ml of blocker in a 10 ml conical tube, dried with a paper towel, then tested at 0, 50 and 100% CO2; acetazolamide 50 mM; vehicle water (Table 1); acetazolamide did not mute the response to the AITC positive control; amiloride, diminazene aceturate, ruthenium red and indisulam also muted the CO2 response, and diminazene and 5 mM amiloride also muted AITC. Abstract: "Earthworms excreted significantly more exudate in response to CO2 in a dosage-dependent manner." Worm source not stated; adults by visible clitellum.

Line 2. Quote MATCH, whole sentence, 10 words. Value matches. `conditions` is sound (n, p, the ANOVA inconsistency, the water-rinse result). Counted: name (see Names). Uncounted: add that 25% CO2 gave no significant response, which is the nearest the paper comes to a threshold.

Line 3. Quote MATCH, whole sentence including its parenthesis, 15 words; value matches the quote. Counted twice: name (see Names) and scientific context (fixable). `conditions` says "the quoted sentence does not give the CO2 concentration or the vehicle control" and leaves them out, but the paper states them: 10 minute soak in 50 mM acetazolamide with water as vehicle, then testing at 0, 50 and 100% CO2, and acetazolamide left the AITC positive-control response intact, which is the authors' evidence that the drug acted on CO2 detection rather than on exudation in general. A reader of the row cannot tell the dose, the exposure or that a specificity control exists. Grade m right on both; `partial` false right.

### Zhang et al. 2025, Anoplophora glabripennis (line 4)

Section "3.1. Adult EAG Responses to Eight Volatiles", verbatim in two chunks: "The mean values for EAG responses of female and male ALB to eight volatiles were positively correlated with concentration" / ", and different equations were fitted, as shown in Table 1." The sentence ends at "Table 1."; Table 1 follows. Volatiles: (Z)-3-hexenol, (Z)-3-hexenyl acetate, (E)-2-hexenal, 1-hexanol, β-caryophyllene, salicylaldehyde, hexyl acetate, 3-carene; five doses 1 ng/μL to 10 μg/μL, 20 μL on filter paper; n-hexane control; responses taken as sample minus control; each concentration three times on one antenna, number of beetles per sex not stated; adults emerged in the lab from infested Salix babylonica log segments collected in Baoding, Hebei, in early May 2024, age not stated (tool summary). Section 3.3.1 says "almost all values were over 0.01 mV".

Line 4. Counted (quote form; fixable). The sentence does not end where the quote does: it continues ", and different equations were fitted, as shown in Table 1." The quote stops mid-sentence with no cut mark and no final stop, which the quote rule does not allow; the progress note's owner question 2 anticipated this. The whole sentence is 29 words and contains the value, so the fix is to quote it whole. The value ("EAG amplitude rose with concentration for all eight host plant volatiles tested, in both sexes") says no more than the whole sentence. Grade m right; `partial` false right.

Uncounted: `conditions` "adults collected from infested willow (Salix babylonica) trunks" should say the adults emerged in the lab from infested log segments collected in Baoding, Hebei, May 2024; add the eight compound names, the 20 μL load and that responses are control-subtracted.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Sebastes schlegelii, lowest AEP threshold 86.4 ± 3.4 dB at 200 Hz | correct | units, conditions | Quote MATCH, citation and licence right; reference level reported as absent though the abstract gives "re 1 mPa" (as printed), and MS-222 anaesthesia, gallamine paralysis and n = 7 waveforms omitted |
| 2 | Dendrobaena (paper: D. veneta), exudate greatest at 100% CO2 | correct | taxon, note | Quote MATCH; filed as D. hortensis on a GBIF reading the page does not support (GBIF holds D. veneta as a separate species) |
| 3 | Dendrobaena (paper: D. veneta), acetazolamide muted the CO2 response | correct | taxon, note, conditions | Quote MATCH; same name fault; drug dose, soak, vehicle, CO2 levels and the AITC specificity control stated in the paper but called absent |
| 4 | Anoplophora glabripennis, EAG rose with concentration for eight volatiles | correct | quote | Sentence continues past the quote (", and different equations were fitted, as shown in Table 1."); quote it whole |

Errors per record: line 1: 1 (scientific context); line 2: 1 (name); line 3: 2 (name, scientific context); line 4: 1 (quote form). 5 faults in 4 records; 4 of 4 records in error.

Evidence errors: 4 of 4 records (100%): scientific-context faults 2 (lines 1, 3); name 2 (lines 2, 3); quote-form 1 (line 4); duplicates 0; licence 0; bibliographic 0; abstract-access grading 0. Unfixable records: none.

Pooled with audits 172 to 287: 269 of 626 evidence records (43.0%; audit 287's 265 of 622, and 4 of 4 here). No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Line 1:
- `units`: "dB re 1 mPa as printed in the abstract (re 1 µPa is the usual underwater reference; the paper writes mPa throughout, probably a misprint)"
- `conditions`: "juvenile fish, standard length 6.99 ± 0.51 cm, wet mass 19.47 ± 2.93 g, from a commercial company (Dalian Tianzheng Industrial Co., Ltd.; farm or wild origin not stated); 80 fish held, AEP run on 8, one died, waveforms from 7; anaesthetised with MS-222 (1:14000) and immobilised with gallamine triiodide (1.2-1.4 mg/g) for recording; rearing water 21.4-22.8 C; only four tone-burst frequencies tested (100, 200, 300, 500 Hz, chosen from offshore wind turbine noise), so this is the lowest of four points and not a full audiogram; thresholds tended to rise from 200 up to 500 Hz; hydrophone sensitivity -190 dB re 1 mPa as printed"

Lines 2 and 3:
- `taxon`: "Dendrobaena veneta" (pending the owner question below)
- `note`, replacing the name sentences: "The paper names the species Dendrobaena veneta and says it was previously known as Eisenia hortensis. GBIF holds both as separate species: Dendrobaena veneta (Rosa, 1886), gbif.org/species/5739805, and Dendrobaena hortensis (Michaelsen, 1890), gbif.org/species/7725323, whose synonyms include Eisenia hortensis and Dendrobaena veneta hortensis but not D. veneta. The paper's two names therefore point at different GBIF species and the worms' identity is uncertain; filed under the binomial the paper prints. Neither name is in gbif-names.tsv; owner to confirm." (keep the licence and aversion-proxy sentences)

Line 2, uncounted: append to `conditions` "25% CO2 gave no significant response".

Line 3 `conditions`: "adult worms (visible clitellum), source not stated; soaked 10 minutes in 5 ml of 50 mM acetazolamide (vehicle water) in a 10 ml tube, blotted dry, then tested in the one-minute exudate assay at 0, 50 and 100% CO2 (exudate release is the authors' aversion proxy); acetazolamide did not reduce the response to the AITC positive control; amiloride, diminazene aceturate, ruthenium red and indisulam also reduced the CO2 response (diminazene and 5 mM amiloride also reduced the AITC response)"

Line 4 `quote`: "The mean values for EAG responses of female and male ALB to eight volatiles were positively correlated with concentration, and different equations were fitted, as shown in Table 1."
- `note`: replace "which returned the quoted sentence without its final punctuation, so the sentence may continue" with "the sentence ends at 'Table 1.'"
- Uncounted, `conditions`: "adults emerged in the lab from infested Salix babylonica log segments collected in Baoding, Hebei, in early May 2024, age not stated; females and males; eight compounds ((Z)-3-hexenol, (Z)-3-hexenyl acetate, (E)-2-hexenal, 1-hexanol, β-caryophyllene, salicylaldehyde, hexyl acetate, 3-carene) at five concentrations (1 ng/ul to 10 ug/ul, 20 ul on filter paper); n-hexane control subtracted; each concentration three times on one antenna, number of beetles not stated; the Results text does not rank the compounds or name a lowest responsive concentration"

## Owner questions

1. Dendrobaena: the progress note's question 1 is answered no as asked. GBIF does not treat D. veneta as a synonym of D. hortensis; it holds both. The paper prints D. veneta and also equates it with Eisenia hortensis, a GBIF synonym of D. hortensis. File under D. veneta as printed (this report's fix), under D. hortensis, or hold both rows until a name ruling? Either name needs adding to gbif-names.tsv through the owner.
2. The progress note's question 2 is answered: the sentence does continue; replace the quote with the whole sentence above rather than drop the record.

## Progress note

Accurate on DOIs, licences and the record list. The "Already on main" list is right that none of the four is a repeat; it does not mention Anoplophora glabripennis's d192 rows, which are another trait and paper. Owner question 1 rests on a misreading of GBIF (above). Held-out leads were not re-checked (they are not filed records).

Verdict: 4 records in error of 4 (100%), 5 faults, above the 5% bar; pooled 43.0%. Error lines: 1, 2, 3, 4. All fixable with the replacement text; none needs dropping.

This report is model output and carries no authority.
