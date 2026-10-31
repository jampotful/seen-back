# audit-275: desk-d191 (8 evidence records, no search records, no wanted lines)

Audited 31 October 2026 from the desk-d191 files present untracked in the worktree (docs/tracks/progress/desk-d191.md and 8 evidence lines in docs/views/evidence/desk-d191.jsonl; neither committed here, neither edited). `tools/senses/check.py` on the evidence file: 8 records, 0 problems. Quote lengths (`len(q.split())`), lines 1 to 8: 16, 18, 15, 17, 18, 15, 13, 20; all within 40. No searched or wanted file, so all eight records were judged. Rules applied: oa-audit.md "Scientific context and counting (29 October 2026)", oa-read.md (grade and `partial`), BRIEF quote rules, the publisher-copy licence rule and the name rule, in the form of audits 270 to 274. Duplicates checked with git grep on origin/main (637f49a3) under docs/views/evidence, docs/views/audit (corrected, ALL.jsonl and the unit audit files), docs/views/searched and docs/views/wanted for Megalopta, Baird, Fernandez, Wcislo, "Danio rerio", zebrafish, Guggiana, "UV avoidance", phototaxis, chokh, TeNT and both DOIs. 2 WebSearch and 12 WebFetch calls used.

Sources opened: api.crossref.org/works/10.3389/FPHYS.2015.00305 and /10.3389/FNBEH.2016.00160 (both answered in uppercase); api.crossref.org/works/10.1098/rstb.2016.0077 (uppercase returned client_error; lowercase answered; used only to identify the source of a main row); frontiersin.org/articles/10.3389/fphys.2015.00305/pdf (record URL, five passes); www.frontiersin.org/journals/behavioral-neuroscience/articles/10.3389/fnbeh.2016.00160/pdf (record URL, three passes); pubmed.ncbi.nlm.nih.gov/26578977 (from a WebSearch result; the tool summarised the abstract and would not return it verbatim). Refused or blocked, not retried and not worked around: www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2015.00305/full (permission not answered); pmc.ncbi.nlm.nih.gov/articles/PMC4990545 (reCAPTCHA interstitial). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries, so quotes were checked by MATCH/MISMATCH, with longer sentences returned in chunks of at most 12 words; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification.

## Bibliographic and licence

- Baird et al. 2015 (lines 1, 2), fresh Crossref: Emily Baird, Diana C. Fernandez, William T. Wcislo, Eric J. Warrant; title as recorded; Frontiers in Physiology 6; issued 2015-10-28; no issue or article-number field (305 is the DOI's article number); no licence field; relation empty; no update-to. As recorded. Copy read (record URL, Frontiers PDF): "Copyright © 2015 Baird, Fernandez, Wcislo and Warrant." and "This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY)." Publisher's own copy with a printed CC BY statement; met. Uncounted: line 1's conditions give the copyright line as "Copyright 2015 Baird et al."; print the names as on the copy.
- Guggiana-Nilo & Engert 2016 (lines 3 to 8), fresh Crossref: Drago A. Guggiana-Nilo, Florian Engert; title as recorded; Frontiers in Behavioral Neuroscience 10; issued 2016-08-19; no issue or article-number field (160 from the DOI); no licence field; relation empty; no update-to. As recorded. Copy read (record URL, Frontiers PDF): "Copyright © 2016 Guggiana-Nilo and Engert." and the same CC BY sentence. Met.

Bibliographic faults 0; licence faults 0.

## Names

- Megalopta genalis (lines 1, 2): the paper studies "Megalopta genalis" (fragment), at Barro Colorado Island, Panama; gbif-names.tsv "Megalopta genalis EXACT ACCEPTED" (1352158). Accepted.
- Danio rerio (lines 3 to 8): gbif-names.tsv "Danio rerio EXACT ACCEPTED" (9797255; Brachydanio rerio is its synonym). Wild-type TLAB, chokh-/- and Tg(sws1:CFP-TeNT) larvae, 5-7 dpf. Accepted. Uncounted: lines 3 to 8 have no `family` field, which lines 1 and 2 carry; check.py does not require it.

Name faults 0.

## Duplicates

- Megalopta genalis on main: absolute_sensitivity, acceptance_deg, acuity_cpd, diel, eye_role, eye_type, fovea, interommatidial_deg and relative_optical_sensitivity rows, and two behaviour_vision rows: "learned visual landmarks guide foraging and homing" (Warrant 2008, 10.1242/jeb.015396) and oa-13b.jsonl:240, "flight and landing performance retained under starlight intensities", from Honkanen et al. 2017 (10.1098/rstb.2016.0077), "Cited from the review's reference 3". Crossref's reference list for that review gives its third reference as 10.1016/j.cub.2004.07.057, not this paper, so oa-13b:240 reports an earlier study; Baird, Fernandez, Wcislo and 10.3389/fphys.2015.00305 are absent from main under any trait, and in searched and wanted. Not a repeat.
- Danio rerio on main: lambda_max_nm (Govardovskii 2000; Endeman 2013), spectral_range_nm (Matsuo 2021), sense_magnetic (null, juveniles) and an oa-5 row filed under "zebrafish" (common name) for UV-improved prey capture from a review. No row from Guggiana-Nilo or 10.3389/fnbeh.2016.00160, and no UV-avoidance or phototaxis row for Danio rerio. Not a repeat.

Duplicates 0.

## Per-paper findings

### Baird et al. 2015 (lines 1, 2)

Line 1 quote MATCH (Abstract), whole sentence. Line 2 quote MISMATCH in form: the sentence does not end at "Figure 3C)."; it continues "Figure 3C), although the average of 116 [46] ms is lower than the value" "of 200 [80] ms recorded for the much larger ring pattern," "suggesting that the size and visual saliency of the landing surface" "is another factor that affects the timing of leg extension in Megalopta." (four chunks as returned; 64 whitespace tokens in all by the tool's count). The record files the first 18 tokens as the whole sentence with no cut marked. The unit's own progress note says only sentences of about 125 characters were filed, and this one was cut to fit.

Context confirmed (tool summary unless quoted): tunnel flights in March and April 2013, "Fifty-one flights from 19 individuals from 11 nest sticks" (verbatim), nests attached at the tunnel's end, 0.0014-40.4 lux; disc landings "Sixty-one landings (27 for the ring pattern, 34 for the radial pattern) from 10 individuals from four nest sticks" (verbatim), ring 0.0018-3.58 lux (rs = −0.02, P = 0.91, n = 27), radial 0.00094-19.94 lux; TC differed with pattern (ring 200 ms against radial 120 ms; Wilcoxon z = 3.3); natural nest-stick landings in March and April 2009, 0.0007-0.95 lux (measured in cd m-2, converted). Flight: ground speed rs = 0.24, P = 0.09; absolute lateral position rs = −0.06, P = 0.69; and in the Results section "Changes in Light Intensity Affect Flight Control in Bombus But not in Megalopta": "There is a suggestion, however, that the within-flight variance of lateral position" "is weakly affected by light intensity" (verbatim, two chunks; rs = 0.26, p = 0.06). Bombus terrestris was tested at 190 or 19 lux: ground speed fell with light (rs = 0.46, P < 0.001) and TC shortened (rs = 0.4, p = 0.0016), while lateral position and its variance were not affected.

Line 1. Counted (scientific context, fixable). The value states a categorical null, "light intensity does not affect flight and landing precision", but the authors themselves qualify it for within-flight lateral variance, a precision measure, as weakly affected (p = 0.06), and the value gives no tested range. The null holds over about 0.0007 to 40 lux, more than four orders of magnitude, against one order of magnitude for Bombus; the range is what gives the null its scale, and the authors' "suggestion" is an exception that limits it. Under the 29 October rule both belong in the record. Uncounted: "(contrast with Bombus, where it does)" holds for Bombus flight speed and landing TC, not for Bombus lateral precision; say which.

Line 2. Counted (quote form, fixable). Unmarked cut of a 64-token sentence, filed as whole. The value stays within the kept part, and the taxon is right: the dropped clause ends "in Megalopta", and the section and Methods tie the result to natural nest-stick landings of M. genalis, so the value says no more than the sentence. The dropped clause is a second factor (landing-surface size) rather than a light effect, so it does not limit the null; add it to the note. The whole sentence is over 40 words, so the fix is a marked cut.

### Guggiana-Nilo & Engert 2016 (lines 3 to 8)

All six quotes MATCH, whole sentences, in the sections the records name (Abstract for lines 3 and 4; Results, "Phototaxis and UV Avoidance Interact to Determine Turning Direction", for line 5; Figure 2 and Figure 4 caption titles for lines 6 and 7; Discussion for line 8). Methods (verbatim fragments): "Five–seven dpf male and female zebrafish larvae."; "Zebrafish swam in a 10 cm petri dish."; LEDs 606, 463 and 397 nm (tool summary). Sample sizes (tool summary): N = 19 (Fig 1E), 21 and 20 (Fig 2A, 2B), 18 (Fig 3A, chokh), 8 (Fig 3B, TeNT), 14 TLAB fish over two trials (Fig 4B-C), 23 (Fig 4D-G). The authors note that the stimuli cannot isolate single cone types, so the UV stimulus also partly drives S and M cones (tool summary).

Line 3. Confirm. The note gives the Discussion's "so weak when presented on its own against darkness" (fragment), so the strength is conveyed in the record. Uncounted: put "weak" into the value and give N = 19.

Line 4. Confirm. The abstract claim is carried by both lines: in Tg(sws1:CFP-TeNT) "the responses to UV stimuli were abolished" (fragment), with visible phototaxis like wild-type siblings, and chokh-/- larvae, which lack eyes, show "an extremely erratic response" (fragment) and no consistent phototaxis. Uncounted: name chokh and the TeNT N = 8; say the transgenic's UV response "seems to have an inverse sign" (fragment) without reaching significance.

Line 5. Counted (scientific context, fixable). The null is the Figure 2A design, UV increased on one side against a constant visible stimulus on the other. The next paragraph's Figure 2B experiment is its exception: with darkness on one side and a visible-plus-UV mixture on the other, "As shown in Figure 2B the preference of the animal for the" "light side decreased as a function of the intensity of the" "UV stimulus." (verbatim chunks). The value "no modulation of the response with increasing levels of UV light", without the pairing, reads as UV intensity never changing the choice, which the paper's next result contradicts. The method names the 2A pairing, but the value does not, and nothing in this record carries the 2B result.

Line 6. Confirm. Figure 2 caption title; it is the 2A and 2B results together. Uncounted: note the cone-isolation caveat above, which the authors give as a reason the UV avoidance may look weaker.

Line 7. Confirm. Figure 4 caption title, with the full-field null in the value. Uncounted: the note's "Reused animals across two trials per experiment (design confound)" overstates the Methods, which average two trials per experiment over 14 TLAB fish; the text does not say fish were reused across stimulus conditions (tool summary). Replace with that description.

Line 8. Confirm. Uncounted: the value drops the authors' "seems to be"; the note states the hedge ("Hedged by the authors ('seems to be')"), so the limitation is conveyed elsewhere in the record, as in audit 274's line 4. Tighten the value.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Megalopta genalis, light does not affect flight and landing precision | correct | value, conditions | Quote MATCH; authors' own weak lateral-variance effect (p = 0.06) and the 0.0007-40 lux range omitted from a categorical null |
| 2 | Megalopta genalis, no effect of light on TC (nest sticks) | requote | quote, note | Unmarked cut: sentence continues ", although ... in Megalopta." (64 tokens) |
| 3 | Danio rerio, intensity-dependent UV avoidance against darkness | confirm | (value; uncounted) | Quote MATCH; weakness carried in note |
| 4 | Danio rerio, UV avoidance needs eyes with functional UV cones | confirm | (conditions; uncounted) | Quote MATCH |
| 5 | Danio rerio, no modulation with increasing UV | correct | value, conditions | Quote MATCH; Figure 2B (UV mixed into the light side) did lower preference with UV intensity; value gives no pairing |
| 6 | Danio rerio, UV avoided like darkness, competes with phototaxis | confirm | (note; uncounted) | Quote MATCH |
| 7 | Danio rerio, contrast but not full field has wavelength effects | confirm | (note; uncounted) | Quote MATCH; "design confound" overstated |
| 8 | Danio rerio, phototaxis shallow, UV avoidance sharp with contrast | confirm | (value; uncounted) | Quote MATCH; "seems to be" carried in note |

Evidence errors: 3 of 8 (37.5%): scientific-context faults 2 (lines 1, 5); quote-form 1 (line 2); name 0; duplicates 0; licence 0; bibliographic 0; abstract-access grading 0. Unfixable records: none.

Pooled with audits 172 to 274: 227 of 558 evidence records (40.7%; audit 274's 224 of 550 plus 3 of 8 here; any audit running concurrently is not included). No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Counted (line 1):
- `value`: "light intensity does not significantly affect flight and landing precision over about 0.0007-40 lux (contrast with Bombus terrestris, whose flight speed and landing timing changed between 190 and 19 lux); the authors note a suggestion that within-flight lateral variance is weakly affected (rs = 0.26, p = 0.06)"
- `conditions`: replace "Copyright 2015 Baird et al." with "Copyright © 2015 Baird, Fernandez, Wcislo and Warrant"; after the 51-flights sentence add "tunnel flights 0.0014-40.4 lux (ground speed rs = 0.24, P = 0.09); disc landings, 61 from 10 individuals from four nest sticks, ring 0.0018-3.58 lux and radial 0.00094-19.94 lux; natural nest-stick landings 0.0007-0.95 lux (2009). Barro Colorado Island, Panama; nests attached at the tunnel's end."
- `where`: "Abstract; Results, Changes in Light Intensity Affect Flight Control in Bombus But not in Megalopta (lateral variance)".

Counted (line 2):
- `quote`: "Again, we found no effect of light intensity on TC (rs = −0.05, p = 0.81, Figure 3C), ..." (19 tokens; the cut is the rest of the sentence).
- `note`: add "The sentence goes on to say that mean TC on nest sticks (116 ms) is lower than on the much larger ring pattern (200 ms), so landing-surface size and saliency is another factor in the timing of leg extension; that is a surface effect, not a light effect. Light range 0.0007-0.95 lux."

Counted (line 5):
- `value`: "with a constant visible stimulus on the other side, no modulation of the response with increasing levels of UV light; when UV was mixed into the visible side against darkness, preference for the light side decreased with UV intensity (Figure 2B)"
- `conditions`: add "N = 21 (Figure 2A, this result); the Figure 2B exception is in the next paragraph of the same Results section."
- `note`: replace "Null result." with "Null result for the Figure 2A pairing only; Figure 2B shows UV intensity does change the choice when UV is on the light side."

Uncounted:
- Line 3 `value`: "weak, intensity-dependent avoidance of UV light presented against darkness"; `conditions`: add "N = 19 (Figure 1E)".
- Line 4 `conditions`: replace "blind mutant (N = 18)" with "blind mutant chokh-/-, which lacks eyes (N = 18), erratic responses; Tg(sws1:CFP-TeNT) N = 8, UV responses abolished, visible phototaxis as in wild-type siblings".
- Line 6 `note`: add "The authors note the UV stimulus also partly drives S and M cones, which could weaken the apparent avoidance."
- Line 7 `note`: replace "Reused animals across two trials per experiment (design confound)." with "Averaged over two trials per experiment and 14 TLAB fish (Figure 4B-C); N = 23 for Figure 4D-G."
- Line 8 `value`: "phototaxis to visible stimuli seems to be a shallow function of contrast while UV avoidance shows a sharp change".
- Lines 3 to 8: add `family` as on main's other Danio rerio rows.

## Owner questions

1. Line 2's sentence is 64 tokens, so only a marked cut fits the 40-word limit. The clause after the cut ends "in Megalopta" and so names the taxon. Is a cut that leaves out the one taxon-naming phrase acceptable when the section heading and Methods fix the taxon, or should the record use a shorter second cut that keeps "in Megalopta"?
2. Main's oa-13b.jsonl:240 (Honkanen 2017, M. genalis "flight and landing performance retained under starlight intensities") cites the review's reference 3, which Crossref gives as 10.1016/j.cub.2004.07.057. Should that main row's note name the primary DOI, so that later units can check it against primary records like line 1?
3. The progress note says four Frontiers papers went unfiled because Crossref returned robots_disallowed. Both of this unit's Crossref lookups answered here in uppercase. Should the next unit retry those four DOIs rather than leave them as leads?

Progress note: accurate on sources, licences, DOIs and refusals; its "only whole sentences of that length were filed" is wrong for line 2, which was cut from a longer sentence.

Verdict: 3 errors in 8 (37.5%), above the 5% bar; pooled 40.7%. Error lines: 1, 2, 5. No unfixable records; lines 1, 2 and 5 can merge with the counted text, and lines 3, 4, 6, 7 and 8 as they stand or with the uncounted fixes.

This report is model output and carries no authority.
