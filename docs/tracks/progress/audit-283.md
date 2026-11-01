# audit-283: desk-d199 (6 evidence records, no search records, no wanted lines)

Audited 31 October 2026 from the desk-d199 files present untracked in the worktree (docs/tracks/progress/desk-d199.md and 6 evidence lines in docs/views/evidence/desk-d199.jsonl; neither committed here, neither edited). HEAD 9705f91f equals origin/main. `tools/senses/check.py` on the evidence file: 6 records, 0 problems. Quote lengths (`len(q.split())`): 21, 16, 11, 16, 15, 10, all within 40. No searched or wanted file, so all six records were judged whole. Rules applied: oa-audit.md "Scientific context and counting (29 October 2026)", oa-read.md (quote, grade, `partial`), desk-audit.md (no 125-character limit), BRIEF trait table (`sense_chemical` and `sense_touch` under "other senses"; `behaviour_vision`: "a behaviour that shows what is seen (... colour choice)"), the publisher-copy licence rule and the name rule, in the form of audits 270 to 282. Duplicates checked with git grep on origin/main across docs/views (evidence, audit including corrected/ and ALL.jsonl, searched, wanted, gaps) and views/ for Tetranychus urticae, Varroa, Anoeconeossa, Anoeconesossa, bundoorensis, the three DOI suffixes, the first-author strings and the Farnier title. 1 WebSearch and 9 WebFetch calls used.

Sources opened: api.crossref.org/works/10.3389/FAGRO.2023.1212705, /10.1051/PARASITE/2023049, /10.3389/FEVO.2014.00067 (uppercase answered each time); the record URLs www.frontiersin.org/articles/10.3389/fagro.2023.1212705/pdf (two passes), www.parasite-journal.org/articles/parasite/pdf/2023/01/parasite230012.pdf (two passes), www.frontiersin.org/articles/10.3389/fevo.2014.00067/pdf (one pass); species.biodiversitydata.se/species/2188249 (from my WebSearch). api.gbif.org/v1/species/match?name=Varroa%20destructor returned PROVENANCE_REQUIRED (permission not answered) and was not retried. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries, so quotes were checked as MATCH/MISMATCH; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification.

## Bibliographic and licence

- Gaudet et al. 2023, fresh Crossref: Kayla Gaudet, Nicoletta Faraone, Neil Kirk Hillier, in the recorded order; title as recorded; Frontiers in Agronomy 5, no issue, article 1212705; issued 2023-07-04; CC BY 4.0 (vor, from 2023-07-04); relation empty. PDF: "© 2023 Gaudet, Faraone and Hillier." and "This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY)." Met.
- Piou et al. 2023, fresh Crossref: Vincent Piou, Caroline Vilarem, Solène Blanchard, Catherine Armengaud, Philipp Heeb, Angélique Vétillard, in the recorded order; title as recorded; Parasite 30, article 49; online 2023-11-12; CC BY 4.0 (vor); relation empty. PDF: "V. Piou et al., published by EDP Sciences, 2023" and CC BY 4.0 (tool summary of the licence sentence). Met.
- Farnier et al. 2014, fresh Crossref: Kevin Farnier, Adrian G. Dyer, Martin J. Steinbauer, in the recorded order; title as recorded; Frontiers in Ecology and Evolution 2; issued 2014-10-22; no article number and no licence in Crossref, as the note says. PDF header: "Frontiers in Ecology and Evolution | Behavioral and Evolutionary Ecology October 2014 | Volume 2 | Article 67"; "Copyright © 2014 Farnier, Dyer and Steinbauer." and "This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY)." Licence met on the exact copy; article number as printed.

Bibliographic faults 0; licence faults 0.

## Names

- Tetranychus urticae: gbif-names.tsv "Tetranychus urticae EXACT ACCEPTED ... 2130185". Accepted.
- Varroa destructor: not in gbif-names.tsv (main's docs/views/no-view-us-fl-alachua.csv carries it with GBIF key 2188249, Varroidae, Mesostigmata). species.biodiversitydata.se/species/2188249 (GBIF-backed): "Accepted name", Varroidae, Mesostigmata, citing Anderson and Trueman (2000) (tool summary). NZOR and Plazi were not reopened. Accepted; not counted.
- Anoeconeossa bundoorensis: gbif-names.tsv row "Anoeconesossa bundoorensis EXACT SYNONYM Anoeconeossa bundoorensis Anoeconeossa 9261664"; the PDF prints "Anoeconeossa" throughout. Accepted spelling right. Uncounted: the note's "earlier main rows" is one row (canon-4:72).

Name faults 0.

## Duplicates

- Tetranychus urticae on main: canon-3:87 (colour_vision, Kelber et al. 2003 compilation) and oa-12:163 (sense_chemical, ionone repellence cited in Llorens et al. 2023, Plants 12(18): 3219). Neither is Gaudet et al. nor butyric acid, eucalyptol or tarsal electrophysiology. Not a repeat, no contradiction.
- Varroa: no evidence, audit, searched or wanted row on main (only the Alachua checklist line).
- Anoeconeossa/Anoeconesossa: only canon-4:72 (acuity_cpd 0.09 cpd from the Feller et al. 2021 compilation) and genus-level mentions in search records for other genera (sweep-41:26 etc.). No Farnier row under either spelling or any trait. Not a repeat.
- DOIs fagro.2023.1212705, parasite/2023049, fevo.2014.00067 and the strings Gaudet, Piou, Farnier, Steinbauer, "Related but not alike": absent from main.

Duplicates 0.

## Per-paper findings

### Gaudet et al. 2023, Tetranychus urticae (lines 1 to 3)

Design (tool summary with verbatim fragments). Two experiments are electrophysiological. (i) Puff ETG ("Screening for ETG-active compounds"): 0.3 s puffs at 3.54 L/min, 30 s apart, doses 10 ng, 100 ng, 1 mg, 10 mg in hexane, n = 20 per compound (Figure 3, Table 1); Figure 3 responses are standardised by subtracting the hexane response; "Peak ETG amplitudes were significantly different among compounds" with F(7,20) = 5.76, p < 0.001; butyric acid at 10000 ng 0.923 ± 1.011 mV, Tukey against hexane p < 0.001 (Table 1). Eucalyptol is not in the puff ETG list or Table 1. (ii) GC-ETD ("Gas chromatography-linked electrotarsal detection"): splitless 1 µL injections of master mixes in hexane, carboxylic acids and aldehydes at 1 mg/mL (n = 7), essential-oil compounds (linalool, thymol, eucalyptol) at 100 ng/mL (n = 6) (Figure 5 legend). The ± is not defined. Behaviour: half-leaf dip at 10 or 100 ng/mL in 0.1% v/v Tween-80, 5 mm filter-paper strip on the primary vein, one adult female per replicate for 20 min, non-responders excluded, binomial test against 50%, n = 50 (Figure 6 legend). Eucalyptol: "Tetranychus urticae was not significantly repelled by eucalyptol at 10 ng/mL or at 100 ng/mL (p = 0.4; p = 0.2)." Isovaleric acid ran the other way: "Isovaleric acid was repellent at 10 ng/mL (p < 0.0001), but not at 100 ng/mL (p = 0.7)."

Line 1. Confirm. Quote MATCH (two passes). Value says no more than the quote; method and conditions match the design (adult females, Tween carrier, n = 50, 20 min). Uncounted: add that non-responders were excluded and the test is binomial against 50%, so the effective n per dose is below 50 and not printed in text; the carrier "itself not repellent" and "no compound was reported attractive" were not seen here and stay unverified. The isovaleric reversal concerns another compound and does not limit this one.

Line 2. Counted (scientific context, fixable). Quote MATCH; it sits in the GC-ETD subsection (preceding sentence: "Two-spotted spider mites responded to a series of carboxylic acids via stimulation from GC effluent (Figures 4A, 5A)" plus a list; following: "Carboxylic acids with 4 carbons had a smaller mean peak amplitude."). `method` describes the puff ETG (0.3 s puffs, 3.54 L/min) that did not produce this value; `conditions` says the dose was "not seen" and lists the puff ETG dilutions, though the GC-ETD stimulus is a 1 µL splitless injection of a 1 mg/mL master mix; and it attaches the puff-ETG ANOVA (F7,20 = 5.76) to a GC-ETD amplitude. This changes what the amplitude measures and its scale (a GC-effluent peak from about 1 µg injected, without a reported solvent baseline or test against one, against a hexane-subtracted puff ETG with n = 20 and a Tukey test against hexane). The puff ETG figure for butyric acid at 10 mg (0.923 ± 1.011 mV, p < 0.001 against hexane) is the response actually compared with a null.

Line 3. Counted (scientific context, fixable). Quote MATCH; GC-ETD subsection, essential-oil mix at 100 ng/mL, n = 6. Same method misdescription as line 2 (puff ETG in `method`, dose "not seen"). Eucalyptol was never in the puff ETG and has no comparison with hexane anywhere in the paper, so "a measurable tarsal response" in the note rests on a GC-ETD peak with no baseline test, at a master-mix concentration 10 000 times lower than the acid mix of line 2; read side by side, lines 2 and 3 invite a compound comparison the design does not support. The note's behavioural null for eucalyptol is right (verified sentence above) and should stay.

Grade m right for all three; access open, `partial` absent, right (PDF read). Trait `sense_chemical` fits tarsal electrophysiology and odour-driven choice in an animal; the plant-only readings do not apply (the responding organism is the mite).

### Piou et al. 2023, Varroa destructor (lines 4 and 5)

Design (tool summary with verbatim fragments): sense deprivation by black nail polish on the foreleg tips of cold-anaesthetised females, controls with polish on the dorsal scutum; two mites per chamber "containing a blue dyed PBS bubble", feeding scored by blue dye in the gut at 24 h; analysis per mite (n = 44 and 37), non-independence of chamber mates not addressed. 86.4% (95% CI 72.6 to 94.8) against 81.1% (64.8 to 92.0), GLM χ² = 0.42, p = 0.52. Discussion: "its main olfactory organ (i.e., the sensory pit on the forelegs)". Feeding designs: no-rubbing control 100% (N = 32) against 92.9% for chambers rubbed with a pigmented bee pupa (N = 140), across four treatments bias-reduced GLM χ² = 4.25, p = 0.24. Arena: bubble against disc, both blue PBS under Parafilm, no bee odour described; time on bubble 55.2 ± 6.1% against 4.9 ± 1.3% of 10 min, N = 32, post hoc V = 462, p < 0.001. Abstract after the quoted sentence: "The detection of the food source seems to be shape-related" / "as a 3D membrane triggers arrestment and exploration more than a 2D membrane." The authors note Parafilm may pass small volatiles.

Line 4. Confirm. Quote MATCH; value within the quote; conditions carry both percentages, both n and the null; the note limits the null to the artificial set-up. Uncounted: add two mites per chamber analysed per mite, the 24 h window, and that only the sensory pit was covered (other chemosensilla not blocked); these do not change the direction or reading the record already gives.

Line 5. Counted (value says more than the quote; dropped qualifier). Quote MATCH (abstract). The quote is a capacity in artificial conditions ("is still able to feed only guided by physical cues"); the value turns it into the mechanism of feeding ("females feed guided by physical cues only") and adds "(shape of the membrane over the food)", which comes from the next abstract sentence and is hedged there ("seems to be shape-related"). `where` says Abstract while `conditions` carries Results figures without naming the subsection; the null across odour treatments (χ² = 4.25, p = 0.24), the direct evidence for "without host odour", is absent. Trait `sense_touch` is acceptable for the bubble-against-disc arrestment (the authors suggest touch), with the Parafilm caveat the note keeps.

Grade m right for both; access open, `partial` absent, right. Trait `sense_chemical` fits line 4 (an olfactory-deprivation test).

### Farnier et al. 2014, Anoeconeossa bundoorensis (line 6)

Design (tool summary with verbatim fragments): Experiment 3 offered six greys (G45, G90, G135, G180, G195, G225), 4 × 4 cm, "presenting a relatively similar and constant reflectance across the spectrum", on a G166 background ("35% light reflecting") whose perimeter was "four-fold greater" than each stimulus; reflectance measured 300 to 800 nm (UV included, Figure 2B), intensity contrast computed (Equations 1 and 2); no matching of brightness or UV claimed (greys differ in intensity by design). Result: G²(113, 6) = 71.4, p < 0.001; G45 against each of G90, G135, G166, G180, G195 at p < 0.001, against G225 at p < 0.05 (sequential Bonferroni). Following sentence: "The brightest gray stimulus (G225) was the second most attractive while G135 was the least attractive gray." Glycaspis brimblecombei: G²(115, 6) = 17.0, p < 0.01, no significant attraction to a specific grey.

Line 6. Counted (scientific context, fixable). Quote MATCH. The value "in preference to lighter greys" with no ranking reads as a darkness preference, but the brightest grey was second and a mid grey (G135, nearest the G166 background) least, so the pattern follows contrast against the background as much as darkness; the record omits the ranking, the background and the paper's intensity-contrast calculation, which changes the causal reading. `conditions` gives n = 92 from Experiment 1 and says the Experiment 3 n was not seen; it is printed (G²(113, 6)). The note's "target reflectance spectra were not seen" should say the spectra were measured (300 to 800 nm, Figure 2B) and the greys are spectrally flat. The Glycaspis line in `conditions` is right.

Grade m right; access open, `partial` absent, right. Trait `behaviour_vision` fits a target-choice behaviour.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Tetranychus urticae, repelled by butyric acid at 100 not 10 ng/mL | confirm | (conditions, uncounted) | Quote MATCH; design and n as printed; binomial test and non-responder exclusion worth adding |
| 2 | Tetranychus urticae, 0.132 mV to butyric acid | correct | method, conditions | Quote MATCH; value is a GC-ETD peak (1 µL of 1 mg/mL mix, n = 7), but method describes the puff ETG, dose called "not seen", and the puff-ETG ANOVA attached; no baseline test for this amplitude |
| 3 | Tetranychus urticae, 0.0973 mV to eucalyptol | correct | method, conditions, note | Quote MATCH; GC-ETD at 100 ng/mL mix (n = 6), misdescribed as puff ETG; eucalyptol has no hexane comparison anywhere; behavioural null right |
| 4 | Varroa destructor, sensory-pit-blocked females still fed | confirm | (conditions, uncounted) | Quote MATCH; percentages, n and null right; two mites per chamber worth adding |
| 5 | Varroa destructor, feeding guided by physical cues only | correct | value, conditions, where | Value drops "still able"/artificial conditions and adds the hedged shape claim from the next sentence; odour-treatment null omitted |
| 6 | Anoeconeossa bundoorensis, chose darkest grey | correct | value, conditions, note | Quote MATCH; brightest grey second and mid grey last (contrast against G166 background) omitted; Experiment 3 n = 113 printed; spectra were measured |

Evidence errors: 4 of 6 (66.7%): scientific-context faults 3 (lines 2, 3, 6), value-beyond-quote fault 1 (line 5); quote-form 0; name 0; duplicates 0; licence 0; bibliographic 0; abstract-access grading 0. Unfixable records: none.

Pooled with audits 172 to 282: 258 of 606 evidence records (42.6%; audit 280's 248 of 590, audit 281's 4 of 6, audit 282's 2 of 4, and 4 of 6 here). No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Counted (line 2):
- `method`: "gas chromatography-linked electrotarsal detection (GC-ETD): adult female mounted dorsally on a Syntech fork electrode, foretarsi in electrode gel under the recording electrode; stimulus is GC effluent from a 1 µL splitless injection of a carboxylic-acid master mix at 1 mg/mL in hexane (DB-5 column, helium 1.2 mL/min)"
- `conditions`: "n = 7 (Figure 5A); ± not defined; no solvent baseline or test against one reported for GC-ETD amplitudes. Separately, in the puff ETG screen (0.3 s puffs, 10 ng to 10 mg, hexane-subtracted, n = 20) butyric acid at 10000 ng gave 0.923 ± 1.011 mV, different from hexane (Tukey p < 0.001, Table 1), and amplitudes differed among compounds (F7,20 = 5.76, p < 0.001)"
- `where`: "Results, Gas chromatography-linked electrotarsal detection; Figure 5A"
- `note`: keep the licence, reading and name sentences and the tarsal (not antennal) sentence; keep the behavioural cross-reference.

Counted (line 3):
- `method`: "gas chromatography-linked electrotarsal detection (GC-ETD): as for butyric acid, but the stimulus is GC effluent from a 1 µL splitless injection of an essential-oil master mix (linalool, thymol, eucalyptol) at 100 ng/mL per compound in hexane"
- `conditions`: "n = 6 (Figure 5C); ± not defined; master mix 10 000 times more dilute than the carboxylic-acid mix, so not comparable with the butyric-acid amplitude; eucalyptol was not in the puff ETG screen and no comparison with hexane is reported for it"
- `where`: "Results, Gas chromatography-linked electrotarsal detection; Figure 5C"
- `note`: replace "so a measurable tarsal response did not give a repellency effect here" with "the GC-ETD peak has no reported baseline test, so the paper does not show a tarsal response distinguishable from solvent; behaviourally eucalyptol was not repelled at 10 or 100 ng/mL (p = 0.4; p = 0.2)".

Counted (line 5):
- `value`: "in artificial feeding chambers without honey bee odour, females were still able to feed guided only by physical cues"
- `conditions`: "feeding in chambers not rubbed with a bee pupa 100% (N = 32) against 92.9% in rubbed chambers (N = 140), no difference across four odour treatments (bias-reduced GLM, df = 3, χ² = 4.25, p = 0.24); in arenas (blue PBS under Parafilm, no bee odour) time on a 3D bubble 55.2 ± 6.1% against 4.9 ± 1.3% of 10 min on a flat disc (N = 32, p < 0.001); the authors say detection 'seems to be shape-related'; Parafilm may pass small volatiles"
- `where`: "Abstract; Results (feeding designs; behavioural observations)"

Counted (line 6):
- `value`: "chose the darkest grey target (G45) over the five lighter greys and the background grey; the brightest grey (G225) was second and the mid grey G135 least attractive"
- `conditions`: "Experiment 3: six spectrally flat greys (G45 to G225, 4 × 4 cm) on a G166 background (35% reflecting), reflectance measured 300 to 800 nm (Figure 2B), intensity contrast computed; n = 113, G²(113, 6) = 71.4, p < 0.001; G45 against G225 p < 0.05, against the others p < 0.001 (sequential Bonferroni); illumination about 5180 lux, arena rotated between trials; Glycaspis brimblecombei showed no significant attraction to a specific grey"
- `note`: replace "whose target reflectance spectra were not seen" with "the greys are spectrally flat and differ in intensity; the ranking (darkest first, brightest second) fits contrast against the background as well as darkness"; replace "earlier main rows" with "the earlier main row (canon-4:72)".

Uncounted (line 1), suggested:
- `conditions`: add "non-responders excluded; binomial test against 50%; responder count per dose not given in text".

Uncounted (line 4), suggested:
- `conditions`: add "two mites per chamber, analysed per mite; feeding scored by blue dye in the gut at 24 h; only the foreleg sensory pit was covered".

## Owner questions

1. GC-ETD amplitudes printed without a solvent baseline or test against one (lines 2 and 3): should such values be filed at all as `sense_chemical` measurements, or only the puff ETG values that a paper compares with the solvent control?
2. Varroa destructor is absent from gbif-names.tsv while the Alachua checklist carries GBIF key 2188249; should the owner add it to taxonomy-extra.tsv?

Progress note: accurate on the DOIs, licences, Crossref gaps and names, and on the eucalyptol behavioural null. It does not notice that both mV values come from GC-ETD rather than the puff ETG the records describe, and it again cites the abolished 125-character limit as a filing constraint ("the summarising fetch returns only sentences of about 125 characters or fewer"); that is a tool limit, which calls for an explicit retrieval gap or a marked cut within 40 words (the held-out Hayasaka sentence was not reopened here).

Verdict: 4 errors in 6 (66.7%), above the 5% bar; pooled 42.6%. Error lines: 2, 3, 5, 6. No unfixable records; lines 2, 3, 5 and 6 can merge with the counted text, lines 1 and 4 as filed.

This report is model output and carries no authority.
