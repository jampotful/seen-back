# audit-451: desk-d336, evidence lines 1 to 3

Audited 1 November 2026 from the desk-d336 files present untracked in the worktree (docs/views/evidence/desk-d336.jsonl, 3 lines; docs/tracks/progress/desk-d336.md). Neither is committed here or edited. HEAD e0c48e94e (desk d332 merge after audits 446/447). `tools/senses/check.py --require-evidence-kind` on the file: 3 records, 0 problems. Quote word counts (check.py split): 13, 13, 9.

Sources opened (WebFetch, each URL taken from a WebSearch result): frontiersin.org/articles/10.3389/fevo.2022.1044565/full (Table 2 with footnote, Methods); frontiersin.org/articles/10.3389/fevo.2022.1044565 (row label glyphs, Results); frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.1044565/pdf (the record's copy: licence, citation, Table 2 rows, footnote); subtbiol.pensoft.net/article_preview.php?id=60691 (citation, licence, Results and Methods); doaj.org article 87dd5d7c249442f3a66e748576bd998a (Ituglanis bibliographic record); Catalog of Fishes (researcharchive.calacademy.org) spid 27651 and 67197. A Crossref list query for the Ituglanis DOI failed at the site (client_error) and was not retried. No PMC, proxy, mirror, repository copy (the City Research Online PDF in a result was not opened), ResearchGate or academia.edu page opened. 6 WebSearch, 8 WebFetch (one failed). WebFetch returns pieces of about 125 characters; quotes marked verified were returned as adjoining pieces.

Duplicates: grep of the whole docs/ tree (excluding desk-d336 files) for Dolichopteryx, Ituglanis, fevo.2022.1044565, 60691, subtbiol.31 and subtbiol.38. Dolichopteryx longipes appears nowhere under any trait. fevo.2022.1044565 is on main for Bathylychnops exilis (desk-d306 line 8, eye_type) and Rhynchohyalus natalensis, Opisthoproctus soleatus, Winteria telescopa (desk-d185 lines 1 to 3, eye_role and eye_type); different species. Ituglanis passensis appears only in desk-d280.md as a "checked and not filed" note (no row, no sheet value). Duplicates 0.

## Unit-wide rulings

- **Trait key for ganglion cell density (lines 1, 2).** check.py TRAITS holds no ganglion key. Main carries non-TRAITS keys `ganglion_density_mm2` (oa-4, oa-7, recheck-codex-b-fixed), `ganglion_cells_per_mm2` (intake-3), `peak_ganglion_cell_density_mm2` and `rgc_peak_density_per_mm2`. Every row read under them is a regional, peak or maximum density from cell counts (Bufo gargarizans "dorsal periphery"; Ochotona "Maximum in central retina"; Hippopotamus temporal and nasal areas; Didelphis "Peak density"; Hebel 1976 "the maximum is an approximate count"). The Wagner values are whole-structure means inferred from optic-nerve axon counts, and the paper itself says they "represent an average density, rather than the maximum density usually used to calculate optimal spatial resolution." Filing them under an existing key would set a whole-retina mean beside peak densities and invite a magnitude comparison the paper warns against. SENSORY-ANATOMY.md allows `sensory_anatomy` "when no existing anatomical trait fits"; none fits this quantity. Fit accepted. Owner question below.
- **Grade for the subtraction-derived 849 (line 1).** `grade` is the taxonomic grade (BRIEF.md: `m` when that species was measured). The paper measured D. longipes and prints 849 in its own table, so `m` is right; `i` would misstate the taxonomy. The derivation belongs in `measurement`/`conditions`, where the record already puts it.
- **Eye diameter as % SL (line 3).** `eye_diameter_mm` holds millimetres (293 rows); `relative_eye_size` holds 8 qualitative or body-mass rows. No main row holds eye diameter as a percentage of standard length. `sensory_anatomy` with structure, measurement and units named fits.
- **Header-plus-row Table 2 quotes (lines 1, 2).** The PDF prints the header cells "D. longipes" and "R. natalensis" (first cell blank) and the rows "Mean GC density main retina (mm−2)* 849 76.2" and "Mean GC density diverticular retina (mm−2) 1788 47.0". Each quote is the column header, a marked cut over the intervening rows, then one whole row with its label (the column meaning) and both values. That satisfies "whole table row" with the column meaning stated and the cut marked, as in audit 446's accepted header prefix. The HTML page renders the superscript sign as an en dash; the record follows the PDF (the copy read), which prints a minus sign. Not counted.

## Line 1, Dolichopteryx longipes, sensory_anatomy (mean RGC density, main retina, 849 per mm2): confirm

Bibliographic: the PDF citation reads "Wagner H-J, Genner MJ, Partridge JC, Chung W-S, Marshall NJ, Robison BH and Douglas RH (2022)" + "Diversity and evolution of optically complex eyes in a family of deep-sea fish:" + "Ocular diverticula in barreleye spookfish (Opisthoproctidae)." + "Front. Ecol. Evol. 10:1044565." + "doi: 10.3389/fevo.2022.1044565". Author order, title, volume and article number as recorded (also matches audit 269's Crossref read). Met.

Licence on the exact copy read (the record's PDF URL): "© 2022 Wagner, Genner, Partridge, Chung, Marshall, Robison and Douglas." + "This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY)." Matches the note. Met.

Quote: verified against the PDF, row text identical, asterisk after "(mm−2)". MATCH. Caption: "Quantitative analysis of the retinae within the diverticulum and main eye of Dolichopteryx longipes" + "(SL 102 mm) and Rhynchohyalus natalensis (SL 183 mm)." Rows verified: main retina 12.60 mm2, diverticular retina 1.95 mm2, optic nerve 14,182 axons, diverticular fascicle 3,487 axons. (14,182 − 3,487) / 12.60 = 849. Every number in `conditions` checks.

Context: Methods, axons counted "in ultrathin electron microscopic sections from areas distributed at random across the surface of the structures and covering at least 20% of their total area", extrapolated "by assuming the same density throughout the entire structure"; densities "represent an average density, rather than the maximum density". Results: histology on "a single eye from a large (SL 102 mm)" fish; two smaller fish (SL 93 and 52 mm) were used only for MRI. Fixation: "Most eyes were fixed immediately following capture in 4% paraformaldehyde and 2.5% glutaraldehyde", not confirmed for this eye, as the record says. One fish, one eye, mean not peak, and calculated by subtraction are all in `conditions`.

Flagged omission, left uncounted: the asterisk footnote adds that the subtraction "is an approximation" and, because the optic nerve also carries efferent fibres and fibres from the accessory retina, "the calculated ganglion cell density for the main retina will be an overestimate", then "the error will be small." The record already says the value is calculated by subtraction and not a direct count. The authors judge the bias small, so it does not change the magnitude or the 2:1 comparison with the diverticulum. Optional fix below.

Name: Catalog of Fishes, "Current status: Valid as Dolichopteryx longipes (Vaillant 1888)." + "Opisthoproctidae." Accepted. The note's "registry not reached" is now superseded (optional fix). Catalog distribution reads "Atlantic [possibly circumglobal in warm seas]" and the histology fish is from the South Pacific (Table 1, "FS Sonne 194"); identification rests on the authors. Not counted.

## Line 2, Dolichopteryx longipes, sensory_anatomy (mean RGC density, diverticular retina, 1788 per mm2): confirm

Bibliographic and licence: same PDF as line 1. Met.

Quote: "Mean GC density diverticular retina (mm−2) 1788 47.0" with the header prefix, verified on the PDF. MATCH. 3,487 / 1.95 = 1788. The R. natalensis comparison (47.0 against 76.2) is verified. The Results sentence after the Table 2 reference states that diverticular ganglion cell density "was approximately more than twice" the main retina's, which matches the record's "2.1 times" on line 1. Not a peak; one fish, one eye; fixed specimen: all stated. This row carries no asterisk and is a direct axon count divided by area, so the overestimate footnote does not apply. Name accepted as line 1.

## Line 3, Ituglanis passensis, sensory_anatomy (eye diameter 4.5% of SL at day 370, one lab individual): confirm

Bibliographic: article_preview prints "Secutti S, Trajano E (2021) Reproduction, development, asymmetry and late eye regression in the Brazilian cave catfish" + "Ituglanis passensis (Siluriformes, Trichomycteridae): evidence contributing to the neutral mutation theory." + "Subterranean Biology 38: 91-112." + "https://doi.org/10.3897/subtbiol.31.60691". DOAJ independently prints "Vol. 38", "pp. 91 – 112", "Apr 2021" and the same DOI with ".31.". The ".31." is the publisher's printed DOI, not a desk error. The volume is 38. desk-d280.md's "(Subterranean Biology 31)" note on main took the volume from the DOI; that is a note, not a row, and is not counted here. Met.

Licence: "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0)," + "which permits unrestricted use, distribution, and reproduction in any medium," + "provided the original author and source are credited." This is the publisher's own copy (the record's XML URL is the same Pensoft article, publisher-hosted). Met.

Quote: "At 370 days, diameters were around 4.5% of SL." returned whole in the Results paragraph on development and eye regression. MATCH, 9 words, one section. Surrounding text verified: "Curiously, with individual 12 and until the 370th day, no perceptible regression in eye diameter" + "(decrease in size in relation to SL) occurred."; "fluctuating asymmetry in eye-size, observed from the 350th on (Fig. 5)," + "without dominance in size in either the left or the right." Methods: "horizontal diameter of both eyes (40 × magnification), were measured"; adults "with eyes reduced to externally visible spots and diameters of approximately 0.85% of SL (Fig. 1)"; "Four adult I. passensis catfish were hand-netted in May, 2000, and afterwards transported to the laboratory"; "The study started with 12 larvae." The record's design (one lab-reared individual, age 370 days, young fish not adult condition, adults about 0.85% SL) is in `conditions`. The paper's next sentences ("In the second year, the increase in eye-size in relation to SL growth was slower"; right eye growing faster until "around the 550th day") describe later ages and do not qualify the day-370 value; uncounted. "On live fish" in `method` and "or no externally visible eyes" in `conditions` were not shown on the page read; unverified, not counted.

Name: Catalog of Fishes, "Current status: Valid as Ituglanis passensis Fernández & Bichuette 2002." Accepted.

Uncounted: the quote says "around 4.5%"; the record's `measurement` does not carry "around". The value says no more than the quote in substance. Optional fix below.

## Summary

| Line | Taxon | Value | Verdict | Reason |
|---|---|---|---|---|
| 1 | Dolichopteryx longipes | 849 per mm2 (main retina) | confirm | Quote, licence, bibliography verified on the PDF read; arithmetic checks; subtraction, mean, n = 1 stated; overestimate footnote uncounted (authors: error small) |
| 2 | Dolichopteryx longipes | 1788 per mm2 (diverticular retina) | confirm | Verified on the PDF; direct axon count / area; n = 1 stated |
| 3 | Ituglanis passensis | 4.5% of SL, day 370 | confirm | Whole sentence verified; DOI ".31." is as printed by publisher and DOAJ; one lab individual, young fish stated |

Errors 0 of 3 records (0%). By kind: quote 0; scientific context 0; taxon 0; grade 0; partial 0; trait key 0; bibliographic 0; licence 0; duplicates 0. None held out. Names: both valid in Catalog of Fishes (opened here).

## Replacement

None required. No record carries a counted error.

## Optional fixes (not counted)

Strings are decoded text; no new string contains a literal double quote. Each old string occurs once in its line.

- Line 1 `conditions`: "not a direct cell count (asterisked row: calculated by subtraction)." -> "not a direct cell count (asterisked row: calculated by subtraction; the Table 2 footnote calls it an approximation and an overestimate, because the optic nerve also carries efferent fibres and fibres from the accessory retina, but judges the error small)."
- Lines 1 and 2 `note`: replace the registry sentence ("Species validity not checked in Eschmeyer's Catalog of Fishes (registry not reached)." on line 1; "Species validity not checked in a registry." on line 2) with "Catalog of Fishes: Valid as Dolichopteryx longipes (Vaillant 1888), Opisthoproctidae (audit 451)."
- Line 3 `conditions`: "One individual; the sentence does not give a left/right split." -> "One individual; the sentence gives an approximate value (around 4.5% of SL) for both eyes without a left/right split."
- Line 3 `note`: "Name unchecked in Eschmeyer's Catalog of Fishes (not reached)." -> "Catalog of Fishes: Valid as Ituglanis passensis Fernández & Bichuette 2002 (audit 451)." and "both as returned by the tool for the page." -> "both as printed by the publisher and by DOAJ (audit 451); the volume is 38."
- Owner question: main holds five ganglion-density keys outside check.py TRAITS (`ganglion_density_mm2`, `ganglion_cells_per_mm2`, `peak_ganglion_cell_density_mm2`, `rgc_peak_density_per_mm2`, plus `fovea` rows in cells/mm2), all peak or regional. If whole-retina mean densities recur, a separate mean key would keep them apart from peaks. This audit invents none.
