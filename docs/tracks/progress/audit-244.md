# audit-244: desk-d159 (10 evidence records, no search records, no wanted lines)

Audited 30 October 2026 from the desk-d159 files present untracked in the worktree (progress note and 10 evidence lines; neither is committed here, neither was edited). `tools/senses/check.py` on the evidence file: 10 records, 0 problems. The unit wrote no searched or wanted file, so there is nothing for `screen_candidates.py --check` and no sample to draw; all 10 records were judged. Quote lengths (whitespace words as check.py counts, `len(q.split())`), lines 1 to 10: 22, 28, 28, 17, 26, 34, 31, 32, 29, 37, all within 40. Evidence judged under oa-audit.md, "Scientific context and counting (29 October 2026)", the oa-read.md quote rule (cuts marked " … " allowed, no mid-sentence start) and the licence rule, in the form of audits 241 to 243. 5 WebSearch and 15 WebFetch calls used (one redirect notice, one refusal).

Sources opened: api.crossref.org/works for the three DOIs (lower-case, WebFetch); pmc.ncbi.nlm.nih.gov/articles/PMC5859124 (Savelli et al., three fetches); link.springer.com/content/pdf/10.1038/s41598-019-52297-0.pdf (Stieb et al., two fetches); www.frontiersin.org/articles/10.3389/fphys.2016.00099/full (Garm et al.); obis.org/taxon/154781 (WoRMS AphiaID); fishbase.se/summary/4249; species.biodiversitydata.se/species/Platichthys_stellatus (GBIF backbone mirror); gbif.org/species/191882227 (a checklist dataset, not the backbone). Not reached: pmc.ncbi.nlm.nih.gov/articles/PMC6848076, reached by redirect from www.ncbi.nlm.nih.gov (permission request not answered; not retried). No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. WebFetch returns model summaries and will not reproduce long sentences, so each quote was checked by submitting the record's quote for a MATCH/MISMATCH answer against the page; points marked "(tool summary)" were not returned verbatim.

## Duplicates

Searched origin/main (3f8e4789) docs/views/evidence, docs/views/audit, docs/views/audit/corrected and docs/views/audit/ALL.jsonl for the three DOIs, the three titles and the three species under any trait.
- Platichthys stellatus, Pleuronectidae: no record on main under any trait.
- Amphiprion akindynos: oa-5:1071 (fovea, Carleton et al. 2020, J Exp Biol jeb193334, a review); a different paper and trait. Stieb et al. 2019 (10.1038/s41598-019-52297-0) is nowhere on main.
- Copula sivickisi: the same paper (Garm et al. 2016, 10.3389/fphys.2016.00099) is on main as sea-invertebrates acuity_cpd (corrected/sea-invertebrates.jsonl:198), cff_hz (:199, whose quote includes "a single opsin peaking around 460 nm") and behaviour_vision (:200); ALL.jsonl verdicts correct, stands, stands. No lambda_max_nm for Copula on main, so line 10 adds a trait and does not repeat a finding; 458 nm (fit) and the abstract's "around 460 nm" agree, so no contradiction.
No repeat by species and paper under the same trait; no contradiction.

## Citation and licence

- Savelli et al. 2018: Crossref authors Ilaria Savelli, Iñigo Novales Flamarique, Tom Iwanicki, John S. Taylor (order as recorded); title split by Crossref at the colon into title and subtitle, joined text as recorded; Scientific Reports 8(1), article-number 4763; online 2018-03-19; licence creativecommons.org/licenses/by/4.0 (tdm and vor); relation empty. The PMC copy states CC BY 4.0. `access` "open" stands.
- Stieb et al. 2019: Crossref authors Sara M. Stieb, Fanny de Busserolles, Karen L. Carleton, Fabio Cortesi, Wen-Sung Chung, Brian E. Dalton, Luke A. Hammond, N. Justin Marshall (order as recorded); title as recorded; Scientific Reports 9(1), article-number 16459; online 2019-11-11; licence CC BY 4.0; relation empty. Springer PDF states CC BY 4.0. `access` "open" stands.
- Garm et al. 2016: Crossref authors Anders Garm, Jan Bielecki, Ronald Petie, Dan-Eric Nilsson (order as recorded); title as recorded; Frontiers in Physiology volume 7; no issue, page, article number or licence field; online 2016-03-30; relation empty. The Frontiers page prints Front. Physiol. 7:99 and a Creative Commons Attribution License (CC BY). "7: 99" verified on the page; `access` "open" stands.
- Uncounted: line 10's note says "Crossref/Frontiers state CC BY 4.0". Crossref has no licence field for this DOI, and the Frontiers page summary gave "CC BY" without a version. Replace "Licence: Crossref/Frontiers state CC BY 4.0 (the article says it is distributed under the Creative Commons Attribution License)." with "Licence: the Frontiers page states the article is distributed under the Creative Commons Attribution License (CC BY); Crossref carries no licence field for this DOI."

## Names

- Platichthys stellatus (Pallas, 1787): "Accepted Name (Source: GBIF Backbone Taxonomy)" on species.biodiversitydata.se, with Pleuronectes stellatus Pallas, 1787, Platichthys rugosus Girard, 1854 and Pseudoplatichthys oshorensis Hikita, 1934 (pro parte) listed as its synonyms; OBIS (WoRMS AphiaID 154781) prints the name in Pleuronectidae, Pleuronectiformes with no status word; FishBase 4249 uses it as the species name. The name is not a synonym of a name in another genus; the desk's unconfirmed status is now confirmed. Family and order right.
- Amphiprion akindynos: ACCEPTED EXACT, 5212068 (docs/views/gaps/gbif-names.tsv). Order Perciformes matches the other 17 Pomacentridae records on main.
- Copula sivickisi: ACCEPTED EXACT, 5842331 (gbif-names.tsv); Tripedaliidae, Carybdeida as on main.

## Checks per paper

Savelli et al. 2018 (lines 1 to 5). All four quote pieces MATCH and are contiguous in one Results sentence ("These consisted of two S visual pigments ... (n = 17), three M visual pigments ... (n = 18), one L visual pigment ... (n = 5), and a rod visual pigment ... Fig. 1)."), preceded by "Using microspectrophotometry, we found six cone visual pigments and one rod visual pigment ..." (tool summary of its end), so no quote starts mid-sentence and every cut is marked. Values match Table 1 (large juveniles: S 445 (19), 459 (17); M 526 (14), 536 (5), 548 (18); L 557 (5); rod 517 (16)). Fish sizes confirmed: large juveniles 196.2 ± 7.5 g, 22.6 ± 1.6 cm, n = 3; small 5.4 g, n = 5. MSP on isolated photoreceptors; no MSP temperature or dark adaptation given (3 h dark adaptation is for HPLC); killed 13:00 to 14:00. Mixtures: bleaching split S(445) into S(437) and S(456) and M(536) into M(527) and M(545), and the Discussion places the mixtures in "some single cones" and "one member of some double cones"; the desk's exclusion of 445 and 536 is right and stated in the notes. Table 1 marks S(459) as similar to S(456), M(526) to M(527) and M(548) to M(545). HPLC found only A1 chromophore; the authors call the 517 nm rod higher than an A1 rod pigment would predict and suggest an unconfirmed second rod opsin (tool summary). Line 5's note says the rod shifts with size, which is right and does not misstate the cause. No counted fault.

Flagged, not counted:
- Line 1 `eye` says "single cones". For large juveniles the paper assigns no cone type to S(459) (tool summary); the assignment rests on the small juveniles' single cones with S(456)/S(437) and the Discussion's single cones for S(445). Harmless (the receptor class S is right and the inference is the paper's own pattern), but more exact: "S (short-wavelength) cones, S (459) pigment; cone type not stated for large juveniles (S pigments are in single cones in the paper's small juveniles and in the Discussion's S (445) cells)". Lines 2 to 4 assign no cone type, so the records do not carry the photoreceptor class identically; this edit makes them consistent.
- The Figure 1 legend reads "Mean absorbance spectra from a total of 5–9 cells from 3 fish", which disagrees with the n of 14 to 19 in Table 1 and the Results sentence (tool summary). The records follow the Results sentence and Table 1; the conflict is the paper's and should be noted, not resolved here.
- The Results say "six cone visual pigments" for large fish and the Discussion "only five" (tool summary); the records log four cone pigments and the rod and do not depend on the count.

Stieb et al. 2019 (lines 6 to 9). On the Springer PDF all four quotes match apart from spacing around "±", "nm" and "=" (the PDF text layer prints "498±4 nm (n=12)"; the desk read the HTML page, which the PMC fetch could not confirm) and a dropped "Th" ligature ("Tis") in the PDF layer; these are text-layer differences, not wording differences. Line 6 is two whole sentences, preceded by a whole sentence about Table S4; lines 7 and 8 are halves of one sentence, contiguous at the cut, each cut marked; line 9 is a whole sentence that ends its paragraph. Values match. MSP fish: 3, kept in aquaria for 4 months (n = 1) or 6 months (n = 2); MSP has its own main-text Methods subsection citing a standard protocol, with detail in the Supplementary Information; no chromophore fit stated; long-wavelength double-cone member 541 nm, n = 1 (LWS estimate 554 nm). The MSP results sit under the Results heading "Spectral sensitivity" (records' `where`: "Results, visual pigments"; harmless, replacement below).

Line 9 (scientific-meaning: applicability and interpretation). The note says the 400 nm single-cone value fits neither opsin estimate and "may be a mixture or a mixed sample (the sentence gives no reason)". The paper does give a reading: the Discussion reports "a consistent λmax of ~ 400 nm for single cones in fishes that were kept under laboratory conditions for an extended period of time", longer than the 370 nm SWS1 estimate and shorter than the 408 nm SWS2B estimate, and interprets it as "single cones in fishes kept under artificial lighting coexpressed SWS2B and SWS1 across the retina", while "under natural lighting conditions coexpression was restricted to a specific small region in the temporal part of the retina", so "a substantial change in gene expression likely occurred when transferring animals to the laboratory" (PDF phrases, tool summary). The value is therefore, on the authors' reading, a captivity-induced mixed SWS1/SWS2B pigment, not a single-opsin λmax that applies to wild fish. The record files it as the single cones' λmax with conditions that do not say the captivity changed the measured class. The same unit excluded the paper-identified mixtures in Savelli (lines 1 to 3 notes), so the unit's own rule also bears on this line. Counted. The co-expression in the MSP fish is the authors' inference, not measured in those fish, and the replacement says so.

Garm et al. 2016 (line 10). Quote MATCH; the cut replaces "to theoretical absorption curves of opsins (Govardovskii et al., 2000)," and is marked; the sentence before it ("They had a single peak in the deep blue part of the visual spectrum around 460 nm (Figure 5).") makes this a sentence start. Methods confirmed: equal-quanta series 410 to 680 nm in 20 steps, 6 × 10^18 photons/s/sr/m2, 15 min dark adaptation, 25 ms flashes, 29 °C, 33 psu, seven upper and seven lower lens eyes from 11 adults of both sexes; only lens eyes recorded ("We focused on the lens eyes since they are the only image forming eyes."); no stimulus below 410 nm. The record states plainly that 458 nm is a template peak fitted to ERG spectral sensitivity, not a pigment measurement, and that the series ends at 410 nm; BRIEF.md defines lambda_max_nm as "peak sensitivity of one receptor class", and main carries ERG-based lambda_max values, so filing it there is right. Grade m right. Uncounted: the tool summary says the spectral-sensitivity animals were juveniles raised to maturity in the laboratory; "11 adults" is right as far as it goes and was not checked further.

## Per record

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Platichthys stellatus, S 459 nm | ok | (eye, uncounted) | Quote MATCH, cut marked; Table 1 459 (n = 17); large-juvenile context, MSP n and mixture exclusion stated; cone type inferred (flag above) |
| 2 | Platichthys stellatus, M 526 nm | ok | | Quote MATCH, contiguous pieces; 526 (n = 14); 536 mixture excluded and said so |
| 3 | Platichthys stellatus, M 548 nm | ok | | Quote MATCH; 548 (n = 18) |
| 4 | Platichthys stellatus, L 557 nm | ok | | Quote MATCH; 557 (n = 5), the same value in small juveniles (n = 6) |
| 5 | Platichthys stellatus, rod 517 nm | ok | | Quote MATCH, sentence end with full parenthetical; 517 (n = 16); small-juvenile rod 507 stated |
| 6 | Amphiprion akindynos, rod 498 nm | ok | (where, uncounted) | Two whole sentences, MATCH bar PDF spacing; 498 ± 4, n = 23; estimate 496 |
| 7 | Amphiprion akindynos, double-cone green 520 nm | ok | (where, uncounted) | First half of one sentence, cut marked; 520 ± 5, n = 13; RH2A estimates 516/518/523 |
| 8 | Amphiprion akindynos, double-cone blue 498 nm | ok | (where, uncounted) | Second half of the same sentence, cut marked; 498 ± 4, n = 12; one RH2B estimate 498 |
| 9 | Amphiprion akindynos, single cones 400 nm | error, fixable | eye, conditions, note, where | Quote MATCH; the Discussion reads the ~400 nm as SWS1/SWS2B co-expression in single cones of aquarium-held fish, a captivity change, and the note says the paper gives no reason (scientific-meaning: applicability) |
| 10 | Copula sivickisi, 458 nm template fit | ok | (note licence, uncounted) | Quote MATCH, cut marked; ERG fit stated as such; range 410 to 680 nm, lens eyes only |

Evidence errors: 1 of 10 (10.0%). Scientific-meaning faults 1 (line 9); quote-form faults 0. Licence faults: none counted (one licence-source wording fault, line 10, uncounted). Name faults: none. Duplicates: none. Values against Table 1 and the printed sentences: all match; no µm/nm garbling.

## Replacement text (exact)

Line 9, `eye`: replace "single cones" with "single cones of aquarium-held fish (on the authors' reading, cells co-expressing SWS1 and SWS2B)".

Line 9, `conditions`: replace "3 fish kept in aquaria for 4 to 6 months; MSP temperature, adaptation state and preparation in the Supplementary Information (not read)" with "3 fish kept in aquaria for 4 months (n = 1) or 6 months (n = 2) under laboratory lighting, which the authors think changed single-cone opsin expression; MSP temperature, adaptation state and preparation in the Supplementary Information (not read)".

Line 9, `note`: replace "The paper does not say which opsin the six single cones used; the opsin-based estimates are 370 nm (SWS1) and 408 nm (SWS2B), so the MSP value fits neither and may be a mixture or a mixed sample (the sentence gives no reason)." with "The MSP value fits neither opsin-based estimate, 370 nm (SWS1) or 408 nm (SWS2B). The Discussion reads the consistent ~400 nm in fish kept under laboratory conditions for an extended period as single cones co-expressing SWS2B and SWS1 across the retina, and says that under natural lighting co-expression was restricted to a small temporal region of the retina, so gene expression likely changed after transfer to the laboratory. Co-expression was not measured in the three MSP fish; it is the authors' interpretation. The value describes single cones of captive fish, probably a mixed SWS1/SWS2B pigment, and is not a single-opsin λmax for wild fish."

Line 9, `where`: "Results, Spectral sensitivity (MSP against opsin-based estimates); Discussion (single-cone SWS1/SWS2B co-expression under laboratory lighting)".

Lines 6 to 8, `where` (uncounted): "Results, Spectral sensitivity (MSP against opsin-based estimates)".

Line 1, `eye` (uncounted): see the flag under Savelli et al.

Line 10, `note` licence sentence (uncounted): see Citation and licence.

## Faults noted, not counted

- Line 1: cone type of S(459) inferred, not stated for large juveniles.
- Lines 1 to 5: the paper's Figure 1 legend (5 to 9 cells from 3 fish) conflicts with the Table 1 and Results n values the records carry.
- Lines 6 to 8: `where` names a "visual pigments" section; the heading is "Spectral sensitivity".
- Line 10: Crossref carries no licence; the CC BY version was not shown on the page summary.
- Progress note: "Accepted status of the name is not confirmed by a status line" is now settled (GBIF backbone: Accepted Name).

Search records: none in the unit (0 of 0). Wanted lines: none. Held-out leads in the progress note were not searched.

Pooled with audits 172 to 243: 144 of 332 evidence records (43.4%; audits 172 to 241 132 of 308 as audit 241 gives it, audit 242 5 of 7, audit 243 6 of 7, audit 244 1 of 10).

Verdict: lines 1 to 8 and 10 can be merged as they stand (the uncounted edits are optional). Line 9 can be merged only with the replacement text above; a flagged scientific-meaning fault must be corrected before acceptance. Error line numbers: 9.

No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page opened; no paper text committed beyond single sentences and short phrases quoted for verification. The desk-d159 copies stay untracked and unedited. This report is model output and carries no authority.
