# audit-435: desk-d323 (7 evidence records, no search records, no wanted lines)

Audited 1 November 2026 from the desk-d323 files copied untracked into the worktree (evidence file, 7 lines, and the progress note; neither is committed here). `python3 -I tools/senses/check.py docs/views/evidence/desk-d323.jsonl`: 7 records, 0 problems. Quote lengths (whitespace words as check.py counts), lines 1 to 7: 22, 26, 8, 8, 13, 13, 19. 10 WebSearch and 14 WebFetch calls used.

Sources opened (all URLs from my WebSearch results or the single-DOI Crossref API): link.springer.com/article/10.1186/2041-9139-2-6 (three passes; the fetch content is truncated in the Methods and does not reach References or Rights and permissions) and link.springer.com/doi/10.1186/2041-9139-2-6; evodevojournal.biomedcentral.com/track/pdf/10.1186/2041-9139-2-6 (302 to a link.springer.com content/pdf URL, not followed); www.frontiersin.org/articles/10.3389/fphys.2017.00105/pdf (two passes); dx.doi.org/10.1186/s40851-022-00188-0 (three passes, BMC article page); api.crossref.org/works for 10.1186/2041-9139-2-6 and 10.1186/s40851-022-00188-0; obis.org/taxon/341818, 130543, 130544; bie.ala.org.au/species/Liocranchia+reinhardti. The Purschke search also returned a springerlink.bibliotecabuap.elogim.com PDF and 0-zoologicalletters-biomedcentral-com.brum.beds.ac.uk figure pages: library proxies, not opened. PMC results surfaced and were not opened. No ResearchGate, academia.edu, Sci-Hub or LibGen page opened. WebFetch returns pieces of about 125 characters; sentences below were reassembled from pieces and points marked "(tool paraphrase)" were not returned verbatim. No paper text committed beyond single sentences and short fragments.

## Repeats of main

grep of the whole docs/ tree (evidence, audit/ALL, audit/corrected, sheets, searched, wanted, gaps, notes) for Terebratalia, Bathyteuthis, Liocranchia (both spellings), Owenia, Galathowenia, Myriochele, Leachia, Passamaneck, Purschke, 2041-9139-2-6 and s40851-022-00188-0: no hit outside desk-d323. 10.3389/fphys.2017.00105 is on main for Xipholeptos notoides only (desk-d153 rhabdom_um, fovea, acuity_cpd; audit/ALL and sea-invertebrates corrected for Loliginidae eye_type). No repeat, no contradiction.

## Names

- Terebratalia transversa (Sowerby, 1846): accepted (search results; no synonym found). OK.
- Bathyteuthis abyssicola Hoyle, 1885: accepted. OK.
- Liocranchia reinhardti: the paper's spelling. OBIS (WoRMS-backed, AphiaID 341818) gives Liocranchia reinhardtii (Steenstrup, 1856), family Cranchiidae, order Oegopsida; ALA (AFD authority) gives accepted Liocranchia reinhardtii Steenstrup, 1856 and lists "Liocranchia reinhardti (Steenstrup, 1856)" among synonyms; the GBIF result title (not opened) also reads reinhardtii. The record is filed under a non-accepted spelling. Error (line 4).
- Galathowenia oculata (Zachs, 1923): OBIS shows Myriochele oculata Zachs, 1923 as unaccepted with accepted name Galathowenia oculata. OK.
- Owenia fusiformis Delle Chiaje, 1844: OBIS lists it with WoRMS ID 130544 and family Oweniidae; status not printed there, no synonymy found. OK.

## Licence

- 10.1186/2041-9139-2-6: Crossref record has no licence field. The Springer page shows "Open access" and "You have full access to this open access article", with "2011 Passamaneck et al; licensee BioMed Central Ltd." in its metadata; my fetches did not reach a "Creative Commons" sentence (content truncated before Rights and permissions), so the note's "page prints Creative Commons Attribution License" is unverified by me. The copy is the publisher's own free full text, which the licence rule accepts. Not counted; optional note fix below.
- 10.3389/fphys.2017.00105: Crossref no licence field (audit 238); the Frontiers PDF prints "This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY)." Accepted.
- 10.1186/s40851-022-00188-0: Crossref licence CC BY 4.0, vor and tdm, start 2022-01-25; the BMC page states Creative Commons Attribution 4.0 International License (tool paraphrase). Accepted.

## Citations

- Passamaneck et al.: Crossref and the Springer page give Yale J Passamaneck, Nina Furchheim, Andreas Hejnol, Mark Q Martindale, Carsten Lüter, in that order; title verbatim; EvoDevo volume 2, article 6, 2011 (Crossref issue 1). Record matches.
- Chung and Marshall: PDF prints "Front. Physiol. 8:105."; authors, title, year, DOI match. `journal` "Frontiers in Physiology 8" omits the printed article number (main's desk-d153 lines read "Frontiers in Physiology 8: 105"; audit 238 flagged the same, not counted). Optional.
- Purschke et al.: Crossref gives Günter Purschke, Stepan Vodopyanov, Anjilie Baller, Tim von Palubitzki, Thomas Bartolomaeus, Patrick Beckers, in that order; title verbatim with the en dash; Zoological Letters volume 8, issue 1, article number 3; online 2022-01-25. `journal` "Zoological Letters 8" omits article 3 (and issue 1). Optional.

## Per line

| line | taxon / trait / value | verdict | evidence |
|---|---|---|---|
| 1 | Terebratalia transversa / sensory_anatomy / 2 putative photoreceptor cells per eye | OK | Quote verified in pieces on the Springer page under Results, "Ultrastructure of Terebratalia eyes": "Ultrastructural analysis demonstrated that the pigment spots are part of a simple eye" + " composed of two putative photoreceptor cells" + " (Figure 1D, E)" (single space between "eye" and "composed"; the figure reference follows directly). Whole sentence, 22 words, starts at sentence start, contains the value. Abstract: "We show that these pigment-cup eyes consist of a lens cell and a shading pigment cell," "both of which are putative photoreceptors". Methods: "Embedded three-lobed stage larvae of Terebratalia transversa" for TEM; fixation "published elsewhere" (Stricker and Reed 1985); age and temperature given only for the Figure 1A-B larvae. Conditions are accurate. No existing trait carries a photoreceptor-cell count per eye (receptor_count is not in check.py TRAITS), so sensory_anatomy with anatomical_measurement is right. Family/order not seen printed. |
| 2 | Terebratalia transversa / sensory_anatomy / enlarged ciliary membranes (ciliary photoreceptor cells) | fixable | Quote verified in pieces: "Both cells possess enlarged ciliary membranes, characteristic of ciliary photoreceptor cells," + " located between the lens and the shading pigment" + " (Figure 1E, F, I; Additional File 1A-K)" (the tool returned this parenthesis verbatim on request). Whole sentence, 26 words. Faults: (a) trait. SENSORY-ANATOMY.md says use sensory_anatomy only when no existing anatomical trait fits and that eye_type remains appropriate; main files photoreceptor membrane type under eye_type (Acoela "paired eyespots whose receptors lack microvillar or ciliary membrane extensions"; Octopus vulgaris "camera (... everted retina of rhabdomeric receptors"). This finding belongs under eye_type. (b) value "(ciliary photoreceptor cells)" asserts the cells are ciliary photoreceptors; the sentence says the membranes are "characteristic of" them and the Abstract calls the cells "putative photoreceptors". |
| 3 | Bathyteuthis abyssicola / rhabdom_um / 600 | fixable | Table 3 caption "Optical properties of squid visual system."; header "Receptor length (µm)"; row "B. abyssicola 1,836 1,530 4 600 0.0067 6.73" matches the quote (whole row). Unit µm as headed. Rhabdom semantics: the paper's Eq. 4 uses "l is the length of photoreceptor", the Methods measure "Lengths of the rhabdom" in Fiji, and the I. notoides Table 3 length (200) equals the Results' "long rhabdom (200 µm) patch", so Table 3 receptor length is a rhabdom length; main files rhabdom lengths under rhabdom_um (Vespula, Polyrhachis, Grapholita, "µm (length)"). Faults: (a) omitted contrary figure: the Figure 5 caption (tubular eyes and fovea of B. abyssicola) reads "(D) A histological section of the fovea which the longest photoreceptor is c.a. 500 µm.", below the tabled 600; the record cites only the Results ">500 µm" patch as "consistent". (b) `eye` "retina of the camera-type eye": the Results describe B. abyssicola's eye as tubular with a foveal pit and the long receptors as a patch on the central axis; with the I. notoides match, the Table 3 figure is likely regional, and the record presents it as a retina value. Conditions (both B. abyssicola specimens among the four aged, ethanol-stored, rehydrated animals; Table 1 histology "2 (ML15, 64)") verified. Family: "Bathyteuthidae" does not appear in the paper; blank is right. |
| 4 | Liocranchia reinhardti / rhabdom_um / 150 | fixable | Row "L. reinhardti 5,770 4,560 4 150 0.0067 3.91" matches the quote; Table 1 histology "4 (ML25-95)". Faults: (a) taxon filed under the spelling reinhardti; accepted is Liocranchia reinhardtii (see Names). (b) family left blank and note says Cranchiidae "is not printed", but the Discussion prints "The cranchid squid, L. reinhardti, possesses nonhemispherical eyes (Figure 4)." and the text names Cranchiidae. (c) note copied from line 3 discusses only B. abyssicola; the record omits that the Discussion says cranchids change eye shape during development so the non-hemispherical eye may be juvenile (tool paraphrase), relevant to specimens of ML 25-95 mm, and that the retinal region of the 150 um figure is not stated. Rhabdom semantics as line 3. |
| 5 | Owenia fusiformis / eye_type / flat pigment spot | OK | Results, "The general structure of eyes": "In Owenia fusiformis and Galathowenia oculata, eyes are represented by flat pigment spots." returned verbatim, 13 words. Next sentence (qualifier, not dropped from the quote): "These spots are continuous with the epidermal epithelium and not distinctly set off from the surrounding cells." Methods: "small adult individuals were chosen"; "the oweniids Galathowenia oculata (Zachs, 1923) and Owenia fusiformis Delle Chiaje, 1844" prints the family. Order not printed (Palaeoannelida is named only as a grade). Shared sentence: it names both species and asserts the same measured state of each; filing it once per species follows main's practice (Vespula germanica and V. vulgaris rhabdom_um lines share one sentence) and passes the quote rule. |
| 6 | Galathowenia oculata / eye_type / flat pigment spot | OK | Same sentence and checks as line 5. |
| 7 | Galathowenia oculata / sensory_anatomy / two PSC types | OK | Results, "The pigmented supportive cells (PSCs)": "Only in G. oculata can two types of PSCs be distinguished by the different distribution of their pigment granules." verbatim, 19 words. No existing trait covers supporting-cell types, so sensory_anatomy with anatomical_presence is right. Fixation "2.5% glutaraldehyde in Milling phosphate buffer" (record: "in phosphate buffer", fine). The eye species are four (two oweniids, two chaetopterids; Psammodrilus balanoglossoides was sectioned only "For comparison or proof of the absence of adult eyes"), so "the only species of the four" is right. The page gives no PRC or PSC counts per eye (note right). |

Evidence errors: 3 of 7 (lines 2, 3, 4), all fixable. Trait-key faults: 1 (line 2). Scientific-meaning faults: 2 (lines 2, 3). Omitted contrary result: 1 (line 3). Name faults: 1 (line 4). Family faults: 1 (line 4). Quote-form faults: 0. Licence faults: 0. Repeats: 0. Search records: none in the unit. Wanted lines: none.

Process: the desk's progress note reports one WebFetch to springerlink.bibliotecabuap.elogim.com (a university proxy host) that redirected to a login and was not read from. Nothing in the filed records rests on it (all three papers were read on publisher hosts here). Noted, not counted against the records.

## Replacement

Every old string below occurs exactly once in its line (checked by script); check.py passes on the edited lines.

Line 2 (multi-field raw JSON edit; apply all five):
- `"trait": "sensory_anatomy"` -> `"trait": "eye_type"`
- `"value": "enlarged ciliary membranes (ciliary photoreceptor cells)"` -> `"value": "both eye cells with enlarged ciliary membranes, characteristic of ciliary photoreceptor cells"`
- `"structure": "larval pigment-cup eye"` -> `"eye": "larval pigment-cup eye"`
- `"evidence_kind": "anatomical_presence", ` -> `` (delete)
- `"measurement": "photoreceptor type (ciliary membrane morphology)", ` -> `` (delete)

Line 3:
- `"eye": "retina of the camera-type eye"` -> `"eye": "retina of the tubular eye; region not stated in Table 3 (the Results place a patch of very long photoreceptors, >500 um, on the eye axis in the foveal pit)"`
- `"note": "Receptor length from the table row` -> `"note": "Contrary figure: the Figure 5 caption, on a histological section of the B. abyssicola fovea, says the longest photoreceptor is c.a. 500 um, below the 600 um in Table 3; the paper does not reconcile the two. For I. notoides the Table 3 length (200 um) equals the dorso-posterior patch length given in the Results, so Table 3 lengths may be regional rather than retina-wide values. Receptor length from the table row`

Line 4:
- `"taxon": "Liocranchia reinhardti"` -> `"taxon": "Liocranchia reinhardtii"`
- `"family": ""` -> `"family": "Cranchiidae"`
- `"conditions": "histology specimens of mantle length 25-95 mm (four animals)` -> `"conditions": "histology specimens of mantle length 25-95 mm (four animals; life stage not stated, and the Discussion says cranchids change eye shape during development, so the non-hemispherical eye may be juvenile)`
- `For B. abyssicola the Results text separately says a patch of very long photoreceptors (>500 um) lies on the eye axis, which is consistent but is a different statement.` -> `The paper prints the name L. reinhardti; the accepted name is Liocranchia reinhardtii (Steenstrup, 1856) (AFD via ALA lists L. reinhardti as a synonym spelling; OBIS, WoRMS-backed, uses reinhardtii). The retinal region the 150 um length describes is not stated.`
- `Family from the species genus (Bathyteuthidae/Cranchiidae) is not printed in the page text read, so it is left blank.` -> `Family from the Discussion ('The cranchid squid, L. reinhardti').`

## Optional fixes (not counted)

- Lines 3 and 4, `units`: `"um (receptor length)"` -> `"µm (length)"` (main's form for rhabdom lengths).
- Lines 3 and 4, `source.journal`: `"Frontiers in Physiology 8"` -> `"Frontiers in Physiology 8: 105"` (printed "Front. Physiol. 8:105"; main's desk-d153 form).
- Line 3, note: `Family from the species genus (Bathyteuthidae/Cranchiidae) is not printed in the page text read, so it is left blank.` -> `Bathyteuthidae is not printed in the paper, so family is left blank.`
- Lines 5 to 7, `source.journal`: `"Zoological Letters 8"` -> `"Zoological Letters 8: 3"` (Crossref article number 3).
- Lines 5 and 6, note: `Family taken from the paper title (Oweniidae)` -> `Family from the Methods ('the oweniids Galathowenia oculata (Zachs, 1923) and Owenia fusiformis Delle Chiaje, 1844')`; and append ` The next sentence adds that these spots are continuous with the epidermal epithelium and not distinctly set off from the surrounding cells.`
- Lines 1 and 2, note: `Licence: page prints Creative Commons Attribution License; Crossref has no licence field.` (line 1 only) -> `Licence: publisher's own open-access full text (Springer page marked Open access); Crossref has no licence field; the auditor's fetch did not reach a Creative Commons sentence.`

Verdict: lines 1, 5, 6 and 7 can be merged as they stand; lines 2, 3 and 4 only with the replacements above. Error line numbers: 2, 3, 4.
