# audit-236: desk-d151 (6 evidence records, no search records, no wanted lines)

Audited 30 October 2026 from the desk-d151 files copied untracked into the worktree (progress note and 6 evidence lines; neither is committed here). `tools/senses/check.py` on the evidence file: 6 records, 0 problems. The unit wrote no searched or wanted file, so there is nothing for `screen_candidates.py --check` and no sample to draw; all 6 records were judged. Quote lengths (whitespace words as check.py counts): lines 1 and 2, 19; lines 3 and 4, 25; lines 5 and 6, 15. Evidence judged under oa-audit.md, "Scientific context and counting (29 October 2026)", the quote rule, and the licence rule for repository copies (audits 178, 194, 223). 7 WebSearch and 10 WebFetch calls used.

Duplicates: git grep on origin/main (acf67337) of docs/views/evidence, docs/views/audit (corrected and ALL), docs/views/searched, docs/views/wanted and views for "Ephoron", "rspb.2022.0318", "Polymitarcyidae", "Egri", "Kriska", "Mészáros" and "virgo". No hit for Ephoron, the DOI or the family. Egri, Kriska and Mészáros hit only other papers by the same group (Halyomorpha halys in oa-8 and its rechecks, and others); "virgo" hits only Calopteryx virgo, Anthropoides virgo and Eucarta virgo. No repeat and no contradiction.

Sources opened: api.crossref.org/works/10.1098/rspb.2022.0318 (WebFetch); real.mtak.hu/141896 (REAL repository record, returned by my WebSearch); core.ac.uk/download/511548348.pdf (four passes: first-page notes and licence keywords; the three quoted sentences, n, stimuli, fitting, limits; peak-shift tests and mechanism; Methods collection and stimuli); zenodo.org/records/6469890 and ecolres.hun-ren.hu (the authors' institute publication page), both returned by my WebSearch; api.gbif.org species match. Blocked: doi.org/10.1098/rspb.2022.0318 (permission request not answered; not retried). No PMC or Europe PMC copy surfaced in my searches. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy result was opened.

Name: GBIF match ACCEPTED, EXACT, "Ephoron virgo (Olivier, 1791)", Ephemeroptera, Polymitarcyidae, usageKey 4481291. Family and order fields match. No name fault.

Citation: Crossref gives Ádám Egri, Ádám Mészáros, György Kriska, "Spectral sensitivity transition in the compound eyes of a twilight-swarming mayfly and its visual ecological implications", Proceedings of the Royal Society B: Biological Sciences 289(1973), article 20220318, published print and online 27 April 2022. Authors in printed order, year, volume, issue, article number, title (no printed quotation marks) and DOI match the records.

## Licence and provenance (decides the unit)

- Crossref carries one licence entry: royalsociety.org/journals/ethics-policies/data-sharing-mining/, content version tdm, from 27 April 2022. That is the Royal Society's text-and-data-mining policy, not a Creative Commons or other open licence; Crossref gives no vor or am licence.
- The CORE file is not the publisher's PDF. Its first page prints the authors' own note "The contents of this document was adjusted to exactly match the contents of the published paper:" followed by "Proc. R. Soc. B. 289, 20220318. (doi:10.1098/rspb.2022.0318)". It is an author-made copy. My keyword pass found no "©", no "licen", no "Creative Commons", no "Royal Society" and no "manuscript" anywhere in it.
- The same paper is deposited in REAL, the repository of the Library of the Hungarian Academy of Sciences (real.mtak.hu/141896, file EVirgoVisEcol_PROCB_published.pdf, status "In Press"). The record states no licence, rights statement, open-access label or version. I infer that CORE harvested this REAL deposit; I did not open a CORE record page that names its source, so that link is an inference.
- The authors' institute page (ecolres.hun-ren.hu) gives the citation and a DOI link only, with no licence. The Zenodo record 6469890 is the paper's supplementary software (software.zip, MIT licence), not the article. The publisher page was blocked here as it was for the desk.

Judgement: the copy is a lawful-looking author deposit in an institutional repository. It is not a pirate or proxy copy, and nothing suggests it was reached through an unauthorized route. But the rule the desk works under requires an institutional or funder repository copy to carry a stated open licence (audit 178 held a deposit without one; audit 194 accepted the NSF PAR copy only because it prints CC BY; audit 223 restates the rule). No open licence is stated on the paper, on the REAL record or on Crossref, and none could be established from the publisher page. `"access": "open"` is therefore not justified, and under the licence rule all six records are errors and are dropped. If the owner later rules this deposit authorised, or the Royal Society page is found to carry CC BY, the records can be refiled with the replacement text below.

## Content check (for a refile; does not change the count)

- Quotes: line 1/2 "Maxima of the fitted templates for the female larvae are λUVmax = 373 nm, and λGmax = 530 nm." and line 5/6 "For the female adults λUVmax = 364 nm, and λGmax = 516 nm were obtained." are whole Results sentences, verbatim apart from the PDF's math-italic lambda glyphs. Line 3/4 "Sensitivity maxima of the simultaneously fit two pigment templates for the male larvae are λUV max = 379 nm, and λG max = 522 nm." opens its sentence and ends with the values; the tool returned the subscripts elided, the opening words and both numbers confirmed. Each record's value is in its quote and says no more. Units nm.
- n: Methods "19 larval (14 females + 5 males) and 14 adult (13 females + 1 male)"; "No curve was fitted to the spectral sensitivity of the single measured male." Labels and n per group right; three separately fitted groups, two peaks each, six records, nothing pooled (main's one-line-per-peak convention, audit 235).
- Method: "fitted to the mean spectral sensitivity of female and male larvae and female adults", "two A1-based pigment templates", "downhill simplex method"; 12 listed wavelengths 346 to 641 nm (the Methods say the source could make 14 stimuli, then list 12); tungsten microelectrodes; 30 min dark adaptation; photon flux 2.5×10^10 to 7.6×10^14 photons cm-2 s-1. All as filed. Larval collection (river Ipoly near Letkés, mornings 3 June to 5 August 2020, kept at 10°C) and "Recordings on adults were started at dawn around 5:00 (UTC + 2 h; 5-6 h after collection)" confirmed.
- Limits confirmed as the paper gives them: polarization-sensitive UV contribution and blue receptors as suggestions only, extracellular recording, no goodness-of-fit statistic and no confidence limits on the fitted maxima, mechanism (opsin expression, pigment concentration, green-receptor number) proposed but not determined, adults "practically all females" because they were collected at urban lights and only females make the compensatory upstream flight, and "the subjective measure of visual perception sensed by the insect may differ from the ERG-determined sensitivities". The notes carry these on all six lines, identically.
- Fault (scientific meaning, would make each line an error on its own): every note says "Adults and larvae did not differ in the UV". The paper also fitted each preparation separately and compared peak wavelengths with Mann-Whitney U tests: the UV peak of larvae and adults was "practically similar (p = 0.047, z = -1.990)", nominally below 0.05, and "the shift in peak wavelength of the assumed green receptor was significant (p < 0.01, z = -2.669)". The note states the authors' conclusion as a null without the test, and it omits that the green λmax shift itself was tested and significant (the note mentions only lower green sensitivity). For lambda_max records that changes how far the adult UV value (364 nm) can be read as equal to the larval one (373 nm). On lines 3 and 4 the sentence also attaches to male larvae a comparison the paper made between female larvae and female adults.
- Not counted: the notes say adult stage (subimago or imago) was not found; the Introduction says males need an additional moult to become imagos and "in the case of females the sub-imago is the reproductive stage", so the female adults recorded are by the paper's account the reproductive subimago (the paper calls them "adults" throughout). Lines 1 to 4 carry the adult recording time in `conditions`, and lines 5 and 6 omit the adults' own collection ("Adults were collected at evenings after sunset between 6 and 16 August 2020", at urban lights).

## Per record

| line | taxon / trait / value | verdict | reason |
|---|---|---|---|
| 1 | Ephoron virgo / lambda_max_nm 373 (UV, female larvae, n = 14) | error (licence), drop | Read in a repository copy with no open licence stated on the paper, the REAL record or Crossref; `access` "open" not justified. Content otherwise right except the UV/green peak-shift note fault above (fixable) |
| 2 | Ephoron virgo / 530 (green, female larvae) | error (licence), drop | As line 1 |
| 3 | Ephoron virgo / 379 (UV, male larvae, n = 5) | error (licence), drop | As line 1; the larva-adult note sentence also misattributes a female-only comparison to male larvae |
| 4 | Ephoron virgo / 522 (green, male larvae) | error (licence), drop | As line 3 |
| 5 | Ephoron virgo / 364 (UV, female adults, n = 13) | error (licence), drop | As line 1 |
| 6 | Ephoron virgo / 516 (green, female adults) | error (licence), drop | As line 1 |

Evidence errors: 6 of 6 (100%). Licence faults: 6. Scientific-meaning faults (fixable, same six lines, each record counted once): 6. Quote-form faults: none. Name faults: none. Duplicates: none. Unit or exponent errors: none.

## Replacement text for a refile (exact, field by field), only if the licence is established

Lines 1, 2, 5 and 6, `note`: replace "Adults and larvae did not differ in the UV; the green sensitivity of adults was lower than that of larvae." with "Separate fits for each female larva and adult, compared by Mann-Whitney U tests, gave a UV peak the authors call practically similar (p = 0.047, z = -1.990) and a significant shift of the green peak (p < 0.01, z = -2.669); the means of the separate fits matched the mean-curve peaks within 1 nm. The abstract says sensitivity was the same in the UV, and at 516 nm the adult eye was about 3.3 times less sensitive than the larval eye."

Lines 3 and 4, `note`: replace "Adults and larvae did not differ in the UV; the green sensitivity of adults was lower than that of larvae." with "Male and female larvae differed significantly only at 516 nm. The larva-adult comparisons were made on female larvae and female adults (UV peak practically similar, p = 0.047; green peak shift significant, p < 0.01); no male adult curve was fitted, so no male larva-adult comparison exists."

Lines 1 to 6, `note` (not counted, better applied): replace "Adult stage (subimago or imago) was not found in the Methods passages read." with "The paper says males need an additional moult to become imagos and that in females the subimago is the reproductive stage; it calls the recorded animals adults." And replace "the full text was read in a repository copy (core.ac.uk), not on the publisher page." with "the full text was read in an author-made copy deposited in the REAL repository (real.mtak.hu/141896) and harvested by CORE; neither states a licence."

Lines 5 and 6, `conditions` (not counted): replace "larvae collected from the river Ipoly near Letkés on several mornings between 3 June and 5 August 2020 and kept at 10 C; adults recorded" with "adults collected at urban lights in the evenings after sunset between 6 and 16 August 2020 and recorded". Lines 1 to 4, `conditions` (not counted): delete "; adults recorded from about 5:00 at dawn, 5 to 6 h after collection".

`access`: stays "open" only if an open licence is found; check.py allows only open, abstract, closed or book.

## Faults noted, not counted

- Lines 1 to 6, `conditions`: the stray ".;" after the n sentence.
- Progress note: "Read in a CORE repository copy ... access filed as open" should say the copy states no licence and is an author-made deposit (REAL).

Search records: none in the unit (0 of 0). Wanted lines: none. Held-out leads in the progress note were not searched.

Pooled with audits 172 to 235: 110 of 274 evidence records (40.1%; audits 172 to 235 104 of 268 as audit 235 gives it, audit 236 6 of 6).

Verdict: none of lines 1 to 6 can be merged; drop all six under the licence rule. Error line numbers: 1, 2, 3, 4, 5, 6.

No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page opened; no paper text committed. Stray files: the desk-d151 copies stay untracked.
