# audit-266: desk-d182 (8 evidence records, no search records, no wanted lines)

Audited 30 October 2026 from the desk-d182 files present untracked in the worktree (progress note docs/tracks/progress/desk-d182.md and 8 evidence lines in docs/views/evidence/desk-d182.jsonl; neither is committed here, neither was edited). `tools/senses/check.py` on the evidence file: 8 records, 0 problems. The unit wrote no searched or wanted file, so there is nothing for `screen_candidates.py --check` and no sample to draw; all eight records were judged. Quote lengths (`len(q.split())`, as check.py counts), lines 1 to 8: 30, 38, 38, 16, 38, 22, 18, 35; all within 40. Evidence judged under oa-audit.md "Scientific context and counting (29 October 2026)", the oa-read.md and BRIEF quote rules (whole sentence or table row, at most 40 words, one section, not starting mid-sentence, every cut marked " … ", contains the value, value says no more than the quote), the licence rule (publisher's own free full text accepted; a repository copy needs an open licence statement on that copy) and the name rule, in the form of audits 262 to 264. 4 WebSearch and 17 WebFetch calls used (counting refused fetches).

Sources opened: api.crossref.org/works/ 10.1038/S41598-018-29646-6, 10.3389/FPHYS.2021.622126, 10.3389/FMARS.2023.1286149; nature.com/articles/s41598-018-29646-6 (record URL); frontiersin.org fphys.2021.622126/full (record URL; three passes); frontiersin.org fmars.2023.1286149/full (record URL); mammaldiversity.org/taxon/1004650, 1004916, 1005012 (the IDs the records cite); obis.org/taxon/127149 (cited by the record) and obis.org/taxon/154712 (returned by my WebSearch); gbif.org/ja/species/5214139 (returned by my WebSearch); conchsoc.org/taxonomy/term/995 (returned by my WebSearch); researcharchive.calacademy.org Catalog of Fishes entries spid=7545 and spid=7546 (returned by my WebSearch).

Blocked and not retried: obis.org/taxon/127160 and obis.org/taxon/141444 (permission not answered); molluscabase.org taxdetails 141444 (permission not answered). A third-party blob-storage copy of the Li PMC PDF (rcastoragev2.blob.core.windows.net) surfaced in a search and was left alone as an unauthorised mirror. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries, so quotes were checked by MATCH/MISMATCH and fragment questions; points marked "(tool summary)" were not returned verbatim.

## Bibliographic and licence (Crossref, fresh)

- Li: Longfei Li, Hai Chi, Haonan Liu, Yu Xia, David M. Irwin, Shuyi Zhang, Yang Liu; Scientific Reports 8, issue 1, article 11933; issued and online 2018-08-09; CC BY 4.0 (vor and tdm, from 2018-08-09); relation empty, no update-to. As recorded.
- Goerger: Alice Goerger, Anne-Sophie Darmaillacq, Nadav Shashar, Ludovic Dickel; Frontiers in Physiology 12, article 622126, no issue; issued 2021-02-10; CC BY 4.0 (vor, delay 0); relation empty, no update-to. Title verbatim. As recorded.
- Boute: Pim G. Boute, Andres Hagmayer, Koen Smid, Remco P. M. Pieters, Martin J. Lankheet; Frontiers in Marine Science 10, article 1286149, no issue; issued and online 2024-01-29 (the DOI carries 2023); CC BY 4.0 (vor, delay 0); relation empty, no update-to. Year 2024 as recorded, and the note explains it.

Licence of the exact copy: all three are the publisher's own free full text (nature.com labels the article "Open access", "© 2018 The Author(s)"; the Frontiers pages as fetched printed no licence line, tool summary) with Crossref vor CC BY 4.0. Accepted under the publisher-copy rule (audits 223, 257, 264). Bibliographic faults 0; licence faults 0.

## Duplicates

git grep on origin/main (f55ee1c5) under docs/views/evidence, docs/views/audit/corrected, docs/views/audit/ALL.jsonl, docs/views/searched, docs/views/wanted and views for Megaderma, Leptonycteris, Artibeus, "lesser false vampire", Lyroderma, "Sepia officinalis", Goerger, Shashar, Scophthalmus, Psetta, turbot, Solea, "common sole", Boute, and the DOI fragments 29646, fphys.2021.622126, 1286149.
- Li 2018 on main: one row only, docs/views/audit/corrected/mammal-groups.jsonl line 83, taxon "Chiroptera (eight species)", rank multiple, lambda_max_nm [357, 359], quote "Our results demonstrate that SWS1 from all eight bat species examined are UV-sensitive with λmax values ranging from 357 to 359 nm". The three per-species rows (357, 358, 358) are not on main under any trait; they sit inside the pooled range and do not contradict it. They add the species-level values the pooled row cannot carry, so they are new, not repeats. Other Megaderma and Artibeus rows on main are other species or other traits (M. lyra fovea and acuity; A. lituratus/planirostris/obscurus acuity, fovea, tapetum from Antonio et al.; A. jamaicensis, A. cinereus). Leptonycteris is absent.
- Goerger 2021: not on main. Sepia officinalis has many main rows, including polarization (Venables et al., Sepia with Carcinus, caustic flicker) and eye_movement (Messenger, optomotor nystagmus after statocyst removal); none from this paper and none on turbidity rearing. No repeat or contradiction.
- Boute 2024: on main only as desk-d147 lines 7 to 9 (Scyliorhinus canicula, Raja clavata, Dicentrarchus labrax). No Scophthalmus or Solea row on main under any trait.
Duplicates 0.

## Names

- Megaderma spasma (Linnaeus, 1758): mammaldiversity.org/taxon/1004650, own species page in genus Megaderma, Megadermatidae, "Listed in MSW3 2005", original name Vespertilio spasma; no validity word printed. Accepted for filing.
- Leptonycteris yerbabuenae Martínez & Villa-Ramírez, 1940: mammaldiversity.org/taxon/1004916, own species page, Phyllostomidae, Glossophaginae. Accepted for filing.
- Artibeus lituratus (Olfers, 1818): mammaldiversity.org/taxon/1005012, own species page, Phyllostomidae, Stenodermatinae; MDD says A. intermedius "is still regularly considered a synonym of A. lituratus" but treats it as separate. As filed. Owner question 2 below (which population the paper's sequence came from was not checked).
- Sepia officinalis Linnaeus, 1758: conchsoc.org/taxonomy/term/995 names it with Sepiidae and cites MolluscaBase AphiaID 141444 as source; no validity label there, and MolluscaBase and OBIS pages for 141444 were refused. The genus is not in doubt and main holds the species widely. Sufficient for filing.
- Scophthalmus maximus (Linnaeus, 1758): obis.org/taxon/127149 (WoRMS 127149) gives the name, Scophthalmidae, Pleuronectiformes, no status label. Eschmeyer's Catalog of Fishes (calacademy spid 7545 and 7546) prints "Current status: Synonym of Scophthalmus maximus (Linnaeus 1758)" for two older names, so the Catalog's current name is the filed one (the older genus Psetta is not current there). Accepted.
- Solea solea (Linnaeus, 1758): obis.org/taxon/154712 (Solea vulgaris Quensel, 1806) states "The accepted taxon for Solea vulgaris Quensel, 1806 is Solea solea" (AphiaID 127160), Soleidae, Pleuronectiformes; GBIF Backbone (gbif.org/species/5214139) lists Pleuronectes solea and Solea vulgaris as synonyms. Accepted. This fills the gap the desk reported (no OBIS page found for S. solea).
Name faults 0.

## Per-paper findings

### Li et al. 2018 (lines 1 to 3), lambda_max_nm

Quotes. Line 1 MATCH (Results and Discussion). Lines 2 and 3 MATCH (Results and Discussion) except that the page carries a reference marker ([29]) after "sanguivorous mammals", which the quote omits. Reference markers dropped from a text layer are harmless (audit 21 practice); uncounted. Values 357 and 358 nm are in the quotes.

Context confirmed (tool summary): eight species expressed from their own SWS1 sequences, plus a resurrected bat ancestor (358 nm, inferred with CODEML under JTT+I+Γ); HEK293T, pcDNA3.1, Xfect; 11-cis-retinal; Rho 1D4 purification; Hitachi U-3900; dark-minus-acid difference spectra; no replicate number; the text gives individual values only for M. spasma, L. yerbabuenae, A. lituratus and the ancestor, and only the 357 to 359 nm range for the rest; the Fig. 2 legend says λmax is "indicated" on the spectra but prints no numbers; full names printed in the first Results and Discussion paragraph and Methods. All as the records say. The method and conditions state that these are recombinant pigments, not retina. No contrary λmax for these three species on main or in my search.

Uncounted: line 1's quoted sentence follows the finding that its congener's SWS1 is a pseudogene ("We re-sequenced part of the SWS1 coding region from this species and confirmed that it is a pseudogene", fragment). That is why the paper writes "However, a congener species"; the note could say so. It does not limit the M. spasma value. Note typography: line 1 has a double space before "accepted"; line 3 has "Discussion.; the MDD notes ..." with no full stop before "The quoted sentence".

### Goerger et al. 2021 (lines 4 to 6), Sepia officinalis

Quotes. Line 4: the whole sentence is 45 tokens (tool count), so a cut was needed; the record keeps the opening through "(BW)" and the closing "(Figure 2).", with the cut marked " … ". Line 5: whole sentence 47 tokens; the cut removes "(70–80%) in HT and LT groups (70 and 80%, respectively)" and the text resumes "with significant PS difference between the group LT" (verbatim fragment), as the record has it. Line 6: whole sentence, printed exactly. All in Results. Quote faults 0.

Line 4 value. "all animals responded at both ages" is the quote. "no difference between rearing groups" rests on the cut statistics (Fisher-Freeman-Halton P = 1.00 at both ages), which the note gives; it also follows from "all animals". Harmless.

Line 5 value. LT 80% against C 30%, P = 0.0044, nLT = 22, nC = 20: MATCH. No HT against C test is reported (tool summary); the note's "so HT was 70%" is accurate and claims no test. Uncounted additions: at 1 month the text gives no between-group PS comparison, and it says "in clear water PS improved with development, especially in group C" (Fisher P = 0.019) (tool summary). The 7-day group difference therefore cannot be carried to 1 month. The value already says "at 7 days", so the scope is stated.

Line 6 value and the stripe-type question. The sentence names no pattern. My checks: (a) it sits in the polarization paragraph, after "Polarization sensitivity in turbid water was significantly lower than in clear water" (McNemar, 7 days: C χ² = 4.17, P = 0.042; LT χ² = 16.06, P < 0.001; HT χ² = 8.64, P = 0.0033); (b) a Results sentence in the intensity paragraph says "Indeed, under turbid conditions only 70% (group C) to 85% (group HT) of the 1-week old cuttlefish showed a response." (verbatim), so 7-day animals did respond to the BW stripes in turbid water; (c) my own calculation: with C at 30% of 20 (6 animals) and LT at 80% of 22 (about 18) responding to Pol in clear water and none in turbid water, McNemar with continuity correction gives (6 − 1)²/6 = 4.17 and (18 − 1)²/18 = 16.06, the printed values. So the "no OMR" sentence concerns the polarized pattern only. Taken alone, "no animal showed any optomotor response" is contradicted by (b). The record files it under polarization, and the note says the preceding sentence "places it with the polarized pattern" and that intensity responses in turbid water were always higher. The limitation is therefore conveyed in the record, so this is not counted, but the value should name the pattern and give the BW figure (replacement below). The paper's own wording is ambiguous; that belongs in the note.

Grey control: the Methods define the grey sheet as a control the animals were expected to ignore; the Results report no grey-control data (tool summary). The notes say so. Methods details in `method`/`conditions` (40 cm outer cylinder, 30°/s both directions, 10 mm stripes, six trials up to 15 min, 180° criterion, n by age and group, 0.1 and 0.5 g/l clay at 50-80 and 300-400 NTU, tested in clear then low-turbidity water): all MATCH (tool summary). Uncounted: the inner animal cylinder is 12 cm and the water cylinder 24 cm.

### Boute et al. 2024 (lines 7, 8), sense_electric

Quotes. Line 7 MATCH and line 8 MATCH (Results, Behavioural response thresholds); both whole sentences. Values and CIs in the quotes.

Context confirmed (tool summary): seven turbot and seven sole started; two turbot aborted and excluded; no sole exclusion stated; 45 Hz, 0.3 ms pulses, 3 s stimulus; 2.5 m circular tank, 14 electrodes stimulated as opposite pairs (seven pairs); 5 S/m in the field simulation; 5 V steps from 5 V; Bayesian Bernoulli GLMM, ROC cut-off at the highest Youden index; between-individual SD 2.36 V/m (within-individual 0.13); turbot against seabass β = −2.458, P_MCMC = 0.027, against sole β = −2.397, P_MCMC = 0.037; catshark against sole β = −3.867, P_MCMC = 0.001; electroreceptive against non-electroreceptive species not different (β = 1.921, P_MCMC = 0.332), which the authors attribute to a frequency mismatch (most pulse energy above 100 Hz, receptors most sensitive at about 1 to 8 Hz); "Any visible change in behaviour, e.g. changing speed or direction of swimming," scored as a response. All as recorded or consistent with the notes.

Uncounted additions: turbot were wild, caught by commercial pulse trawlers in the North Sea; sole came from aquaculture (Stichting Zeeschelp, Kamperland); mean standard length 27 cm (turbot) and 30 cm (sole). Turbot origin means possible prior pulse-field exposure, which the paper does not test; worth stating, not counted. The shared note on line 8 (sole) says "Turbot is a flatfish without electroreceptors"; on the sole record it should name sole. The electroreceptive-against-non-electroreceptive null (P_MCMC = 0.332) is conveyed by "the authors find electroreceptive species not more sensitive"; adding the statistic is optional.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Megaderma spasma, SWS1 357 nm | confirm | (note; uncounted) | Quote MATCH; recombinant in vitro stated; new per-species row inside main's pooled 357-359 range; congener pseudogene context and a typo |
| 2 | Leptonycteris yerbabuenae, SWS1 358 nm | confirm | (quote marker; uncounted) | Quote MATCH bar the [29] reference marker; name on MDD; not on main |
| 3 | Artibeus lituratus, SWS1 358 nm | confirm | (note; uncounted) | As line 2; MDD intermedius note right; note punctuation |
| 4 | Sepia officinalis, BW optomotor all respond in clear water | confirm | none | Cut marked; value is the quote plus the cut P = 1.00, given in the note; grey control unreported, said so |
| 5 | Sepia officinalis, Pol 7 d LT 80% vs C 30% | confirm | (note; uncounted) | Quote MATCH with marked cut; HT 70% untested, said fairly; 1-month development could be added |
| 6 | Sepia officinalis, turbid water 7 d no OMR but one | confirm | (value, note; uncounted) | Quote MATCH; sentence is about the polarized pattern (paragraph and McNemar arithmetic); BW 70-85% responded in turbid water; limitation conveyed in note, value should name pattern |
| 7 | Scophthalmus maximus, 8.4 V/m | confirm | (conditions; uncounted) | Quote MATCH; method, stats and authors' frequency explanation right; wild pulse-trawl origin could be added; name current in Catalog of Fishes |
| 8 | Solea solea, 6.0 V/m | confirm | (note, conditions; uncounted) | Quote MATCH; note's "Turbot is a flatfish" should name sole; name accepted via OBIS/WoRMS synonym page |

Evidence errors: 0 of 8 (0%). Scientific-meaning faults 0; quote-form faults 0; licence faults 0; bibliographic faults 0; name faults 0; duplicates 0; pooled or cultivar faults 0. Unfixable records: none.

Pooled with audits 172 to 264: 192 of 479 evidence records (40.1%; 188 of 458 through audit 262, plus 4 of 6 in audit 263, 0 of 7 in audit 264, 0 of 8 here; the concurrent audit 265 is not included). No search records, so nothing to pool with audits 83 to 90.

## Replacement text (all uncounted)

- Line 1 `note`: append "The quoted sentence follows the finding that its congener's SWS1 is a pseudogene (preceding sentence, Results and Discussion)." Replace "(also GBIF 2433352, Catalogue of Life,  accepted)" with "(also GBIF 2433352, Catalogue of Life, accepted)".
- Lines 2 and 3 `note`: append "The printed sentence carries a reference marker (29) after 'sanguivorous mammals', omitted from the quote."
- Line 3 `note`: replace "The sentence is from Results and Discussion.; the MDD notes A. intermedius is often treated as a synonym of A. lituratus The quoted sentence" with "The sentence is from Results and Discussion. The MDD notes A. intermedius is often treated as a synonym of A. lituratus. The quoted sentence".
- Line 5 `note`: append "At 1 month the text gives no between-group PS comparison; it says PS improved with development in clear water, especially in group C (Fisher P = 0.019), so the 7-day group difference is not shown to persist."
- Line 6 `value`: "in turbid water at 7 days no animal showed any optomotor response to the polarized stripes except one cuttlefish from the HT group (the sentence names no pattern; it sits in the polarization paragraph, and 70% (group C) to 85% (group HT) of 7-day animals still responded to the intensity stripes in turbid water)". `note`: replace "Null result in turbid test water." with "Null result for the polarized pattern in turbid test water. The paper's sentence is ambiguous as printed; a Results sentence in the intensity paragraph reads 'Indeed, under turbid conditions only 70% (group C) to 85% (group HT) of the 1-week old cuttlefish showed a response.' The McNemar values for C (4.17) and LT (16.06) match 6 and about 18 clear-water Pol responders falling to none (audit 266's calculation)."
- Lines 7 and 8 `conditions`: append "; turbot wild-caught by commercial pulse trawlers in the North Sea, sole from aquaculture (Stichting Zeeschelp, Kamperland); mean standard length 27 cm (turbot) and 30 cm (sole)".
- Line 8 `note`: replace "Turbot is a flatfish without electroreceptors;" with "Sole, like turbot, is a flatfish described as non-electroreceptive;". Replace "OBIS page for this species was not found." with "accepted in WoRMS via OBIS (obis.org/taxon/154712: 'The accepted taxon for Solea vulgaris Quensel, 1806 is Solea solea', AphiaID 127160)."
- Line 7 `note`: replace "OBIS page gave no explicit accepted label." with "OBIS page gave no explicit accepted label; Eschmeyer's Catalog of Fishes gives Scophthalmus maximus (Linnaeus 1758) as the current name for its synonyms."

## Owner questions

1. Li 2018: main keeps a pooled "Chiroptera (eight species)" row [357, 359] alongside the three new per-species rows. Should the pooled row stay, or be narrowed to the five species without a printed value?
2. Artibeus lituratus: MDD now separates A. intermedius, which many still treat as a synonym. I did not check where the paper's A. lituratus sequence came from. Filed name stands unless the owner wants the sample's origin checked.
3. Sepia officinalis line 6: the paper's own sentence names no pattern. I read it as the polarized pattern from paragraph position and the McNemar arithmetic. If the owner wants records only where the paper names the pattern, line 6 should be held.

Progress note: accurate on what was read and refused. Its "no OBIS page was found for Solea solea" is now answered above.

Verdict: 0 errors in 8 (0%), under the 5% bar; pooled 40.1%. All eight lines can merge, with the uncounted replacement text above. Error line numbers: none.
