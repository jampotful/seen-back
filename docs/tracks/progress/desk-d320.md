# desk-d320: measured eye values from comparative tables and Results sentences, 10 records

Branch research/desk-d320 from origin/main. About 52 WebSearches; WebFetch only on URLs returned by searches, plus Crossref list queries (prefix + month filter + title query; single-DOI /works/ URLs were refused with client_error and not worked around). `python3 -I tools/senses/check.py | grep d320`: 10 records, 0 problems. Traits: eye_axial_length_mm (2), eye_diameter_mm (9); all carry "new trait" in the note as check.py requires (keys already on main).

Repeat check: text index of origin/main docs/ (evidence, audit, sheets, searched, recheck, progress) plus evidence and progress files of all unmerged desk and audit branches, built 1 Nov 2026; species and DOI grepped before filing.

Filed (docs/views/evidence/desk-d320.jsonl):
1-2. Trachylepis quinquetaeniata (Scincidae): axial length 3.972 mm and transverse diameter 4.85 mm from one Results sentence, ten adults, freshly dissected (Zoological Letters 9(1): 7). Species and DOI are on main under eye_type/fovea; axial length and diameter are not.
3. Caretta caretta: eyeball rostrocaudal length 22.83 mm, live turtles, CT, n = 20 eyes (Animals 13(6): 1016).
4-7. Allosergestes pectinatus, Sergia tenuiremis, Phorcosergia grandis, Eusergestes arcticus (Sergestidae): species-mean eye diameter, Table 1 rows (Frontiers in Ecology and Evolution 10: 787315).
8-10. Benthosema glaciale, Ceratoscopelus maderensis, Centrobranchus andreae (Myctophidae): single-specimen eye diameter, Table 3 rows (PLoS ONE 8(3): e58519).

Dropped candidates:
- On main or already dropped: Temnothorax albipennis (pooled colonies, d276), Lymantria xylina, Eucryptorrhynchus, Asiophrida, Cacopsylla chinensis, Grapholita molesta, Arge similis, five honeybee species, Python bivittatus (BJVRAS 60: e213344), Dasyprocta prymnolopha (d308, 55-word list, no licence name).
- Licence: Eidolon helvum (Folia Morphologica, CC BY-NC-ND on the publisher page; the Online First PDF names no licence); Parantica sita and Owens et al. (JEB 2020, no open licence).
- Review: Kelber and Somanathan, Spatial Vision and Visually Guided Behavior in Apidae (Insects 10: 418; Table 2 facet counts, review-sourced).
- No usable species value: Currea et al. Commun Biol 6: 246 (method paper), Insects 14: 670 (Bombus DRA, no values), Animals 11: 2987 (chicken, domestic, values in tables), Ultrasound of snakes (BMC Vet Res 10: 313, spectacle not eye size), Collery et al. zebrafish SD-OCT (no numbers in text), Chen et al. anurans (aggregate), Muramoto et al. sea turtles ultrasonography (Table 1 not readable), Guiana and Clymene dolphin eyes (SciELO, Table III not returned, abstract and Methods specimen counts disagree), fossil decapod eye table (Zool Lett 2016), Sinocyclocheilus and Astyanax cavefish papers (BMC: figure pages only, values in supplements).
- Not reachable: PMC began returning a reCAPTCHA page mid-unit (not worked around; the PLoS ONE lanternfish page was read before that); revistas.usp.br abstract page and ajol.info (PROVENANCE_REQUIRED or empty); Frontiers in Zoology 2026 "Not all heads are the same" (only a Research Square preprint surfaced).

Weak spots for the auditor:
- Caretta: the paper's term is "length" of the eyeball (rostral to caudal), filed as eye_axial_length_mm; the quote is a 32-word Results sentence that also carries height and width.
- Trachylepis: same DOI as the eye_type row on main; page prints no section heading for the sentence; measuring method not named; authors from the Crossref list; no licence sentence on the page (Crossref CC BY 4.0 vor).
- Shrimp rows are Table 1 of Materials and Methods (Sampling), not Results; the row keeps the citation numbers in brackets; units and "mean" come from the caption and footnote. Only the four rows whose bracketed numbers were returned were filed. Preservation of expedition animals not read (collection animals were in about 70% ethanol).
- Myctophid rows: Table 3 mixes single values and ranges; cruise 8 (B. glaciale, C. maderensis) was measured after fixation in Karnovsky's fixative, cruise 1 (C. andreae) fresh; life stage "?" undefined for C. andreae. Crossref licence content-version is "unspecified" and the licence sentence was read on the PMC copy. Benthosema supralateralis/Bolinichthys naming in Table 3 was inconsistent in the tool output, so not filed.
- All text came through WebFetch summaries; quotes were re-requested for the key sentences but are not single uninterrupted passes.
- Class is from the group catalogue, not read on the page, for Trachylepis.

Questions: does a same-DOI, different-trait record (Trachylepis axial length, DOI on main for eye_type) count as a repeat of main?
