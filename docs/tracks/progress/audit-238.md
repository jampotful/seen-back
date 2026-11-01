# audit-238: desk-d153 (3 evidence records, no search records, no wanted lines)

Audited 30 October 2026 from the desk-d153 files copied untracked into the worktree (progress note and 3 evidence lines; neither is committed here). `tools/senses/check.py` on the evidence file: 3 records, 0 problems. The unit wrote no searched or wanted file, so there is nothing for `screen_candidates.py --check` and no sample to draw; all 3 records were judged. Quote lengths (whitespace words as check.py counts), lines 1 to 3: 24, 27, 36, all within 40. Evidence judged under oa-audit.md, "Scientific context and counting (29 October 2026)", the quote rule and the licence rule (audits 178, 194, 223, 236; "a publisher's own free full text is acceptable"). 1 WebSearch and 7 WebFetch calls used.

Duplicates: git grep on origin/main (11eddb8d) of docs/views/evidence, docs/views/audit (corrected and ALL), docs/views/searched, docs/views/wanted and views for "notoides", "Idiosepi", "Xipholeptos", "fphys.2017.00105", "Chung W" and "pygmy squid". No hit for either name, the family or the DOI. "Chung W" hits only other papers: Chung and Marshall 2016 (10.1098/rspb.2016.1346, coleoid lambda_max lines, sea-invertebrates corrected 82 to 89) and the Loliginidae pupil line (corrected 134), plus two wanted lines (Chung et al. 2014 damselfish; Gagnon et al. 2016). None concerns this species or these traits. No repeat and no contradiction.

Sources opened: api.crossref.org/works/10.3389/fphys.2017.00105 (WebFetch); www.frontiersin.org/articles/10.3389/fphys.2017.00105/full (one pass); www.frontiersin.org/articles/10.3389/fphys.2017.00105/pdf (publisher PDF, three passes); public-pages-files-2025.frontiersin.org/journals/physiology/articles/10.3389/fphys.2017.00105/xml (version-of-record XML, one pass) and its /text sibling (returned the abstract only); api.gbif.org species match for both names. All were returned by my WebSearch for the title or are the Crossref and GBIF APIs. A PMC copy (PMC5323406) surfaced and was not needed. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy result was returned or opened.

## Licence (question 1)

Crossref carries no `license` entry for this DOI (only a vor similarity-checking link). The publisher's own copies state the licence: the PDF prints "Copyright © 2017 Chung and Marshall." and "This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY)."; the version-of-record XML carries the same statement with the licence URL creativecommons.org/licenses/by/4.0/. The HTML article page shows only "Copyright statement" and "Open access statement" links in the text my fetch returned. This differs from audit 236, where the copy was an author-made repository deposit with no licence anywhere; here the copy read is the publisher's own version of record and it prints CC BY, which is what audit 194 accepted and what the brief's rule ("a publisher's own free full text is acceptable") allows. A missing Crossref entry is a gap in the publisher's deposit, not a missing licence. `access` "open" is justified. No licence fault.

## Name (question 2)

GBIF match: "Idiosepius notoides S.S.Berry, 1921" SYNONYM, EXACT, usageKey 2289185, acceptedUsageKey 9458034; "Xipholeptos notoides (S.S.Berry, 1921)" ACCEPTED, EXACT, usageKey 9458034, Cephalopoda, Idiosepida, Idiosepiidae. The brief's rule is to file under the accepted name (a record filed under a synonym is an error, audits 86 and 88), and main records the printed synonym in the record (for example sea-invertebrates corrected 86, Doryteuthis pealeii "as Loligo pealeii"). All three notes state the printed name and the GBIF status. Taxon, family and order are right. No name fault. WoRMS was not consulted; GBIF is the authority the desk's prior animal audits used (235, 237).

## Citation (question 5)

Crossref: Wen-Sung Chung, N. Justin Marshall, "Complex Visual Adaptations in Squid for Specific Tasks in Different Environments", Frontiers in Physiology 8, published online 24 February 2017, no issue, no article number in the metadata. The PDF's first page prints "Front. Physiol. 8:105." Authors in printed order, year, volume, title and DOI match. The records' `journal` "Frontiers in Physiology 8" omits the printed article number 105, and each note says Crossref gives "no issue or article number" without adding that the PDF prints 8:105; metadata only, not counted (fix below).

## Checks common to all three

- Equations as printed in the PDF: (1) w = f × λ/A, (2) θ = 1.22 × λ/A, (3) R = f/2p; "p is center-to-center receptor separation (µm)"; wavelength "500 nm for the coastal species".
- Table 3, I. notoides row: focal length 740 um, aperture 580 um, receptor diameter 4, receptor length 200, absorption coefficient 0.0067, absolute sensitivity 4.78. Table 3 has no angular-size or resolution column.
- Table 1, Idiosepius notoides row: Day "10 (1–3 m)", Night "5 (1 m)", MRI "8 (ML8-14)", Histology "6 (ML8-14)", Immuno-histology "3 (ML10-14)", seine net, 0 to 10 m. The notes' "6 histology specimens" and ML 8 to 14 mm are right.
- Methods: "The individual which obtained the highest voxel resolution in each species was selected for further morphologic and quantitative analysis of eyes and brain lobes." The notes' one-individual statement is right. Focal distance "was determined from the MRI imagery" (lens centre to eyecup) on fixed specimens.
- Not in the records and bearing on resolution: the Results say the retinal bumps of the two coastal squid come from the enlarged optic lobe "pressing on the back of retina, forcing much of temporal retina close to the lens (Figures 4A,B)", and the Discussion opens "Here we documented a second coastal squid, I. notoides, has the retinal bump resulting in intentional hyperopic defocus over a half of the frontal scene." The bump persists in juvenile and mature animals (my paraphrase of the next sentences). The paper does not say whether the bump and the dorso-posterior patch overlap. On fixation it says only that the eye deformation "is not just the result of fixation shrinkage" (citing Chung and Marshall 2014); no shrinkage correction of rhabdom widths is reported.

## Acuity arithmetic (question 4)

- 92.5 cycles radian−1 is the printed figure (the quote, verbatim in the PDF and HTML). 740 / (2 × 4) = 92.5, so the desk's inference that p was set to the 4 um Table 3 receptor diameter holds, and is labelled as the desk's inference. 92.5 × π/180 = 1.6144, so 1.61 cycles/degree is right.
- Equation 2 with 500 nm and the 580 um aperture gives 1.22 × 0.000862 = 0.00105 rad, as the desk says. The printed 0.00086 rad is exactly λ/A (500 nm / 580 um = 0.000862) without the 1.22 factor, which the note does not observe; the note's "the paper does not explain the gap" is fair and labelled "my arithmetic". Better stated (not counted): see the replacement text.
- Grade: main grades acuity_cpd values converted from per-radian figures m when the source computed the per-radian value for a named species (66 of 70 converted acuity lines on main are m, for example the compiled Land figures). The author computed R; the desk did only a unit change. Grade m is consistent with main. The "calculated, one individual, not behavioural" labelling is honest in `method`, `conditions` and `note`.
- Fault: the Table 3 receptor diameter (4 um) and length (200 um) are exactly the dimensions of the dorso-posterior thin-rhabdom patch, the narrowest of the 4 to 7 um widths reported; with 7 um the same equation gives 52.9 cycles per radian, 0.92 cycles/degree (my arithmetic). So 1.61 is the best-case sampling figure for the patch region, yet `eye` reads "whole eye". And Equation 3 assumes a focused image, while the authors report hyperopic defocus over half of the frontal scene in this species. Both change the applicability and practical magnitude of the value as read in a species cell, so line 3 is counted. The note's "calculated optical limit" also misnames it: f/2p is the receptor sampling (Nyquist) limit, and the optical (diffraction) term is Equation 2.

## Per record

| line | trait / value | verdict | reason |
|---|---|---|---|
| 1 | rhabdom_um [4, 7] um | ok | Quote is the whole Results sentence ("Variations of Retinal Features"), verbatim with "(the red dash line in Figure 4A)" kept (24 words; the HTML prints Greek mu, the PDF the micro sign, a typographic difference). Value is the width range and says no more; `conditions` and note correctly say the number of sectioned animals is not stated, and that the range is not placed within or across eyes. Units "um" where main writes "µm" on 69 of 73 rhabdom_um lines (not counted) |
| 2 | fovea, dorso-posterior thin long rhabdom patch, high resolution if uncoupled | ok | Quote is the whole Results sentence, verbatim with the coupling condition (27 words). Value says no more and keeps the condition. The next sentence, "This forward-looking area, like the foveal regions in fish, is likely used in predation (Figure 4).", is in the Results as the note says, and is labelled the authors' supposition. Filing an area of high receptor density under fovea follows main's convention (acute zones are filed as fovea). Not counted: the paper reserves "fovea-like" for the two deep-sea squid and calls the coastal modification a retinal bump; suggested note text below |
| 3 | acuity_cpd 1.61 cycles/degree | error, fixable | Quote is the whole Results sentence, verbatim (36 words), contains 92.5; conversion and grade right. Faults (scientific meaning): `eye` "whole eye" where the computation uses the patch dimensions (4 um diameter, 200 um length), the thinnest of the reported 4 to 7 um widths, so the value is a best-case regional figure; and the record omits the authors' hyperopic defocus over half of the frontal scene in this species, which limits a focused-image sampling estimate |

Evidence errors: 1 of 3 (33%). Scientific-meaning faults: 1 (line 3). Quote-form faults: none. Licence faults: none. Name faults: none. Duplicates: none. Trait-key faults: none (rhabdom_um, fovea and acuity_cpd are in tools/senses/check.py; main has 73 rhabdom_um and 830 fovea lines in the form used here). Unit or exponent errors: none ("cycles/degree" is main's majority form; radian−1 is read correctly).

## Replacement text (exact, field by field)

Line 3, `eye`: "receptor mosaic of the dorso-posterior patch (Table 3 receptor diameter 4 um and length 200 um, the dimensions of that patch)".

Line 3, `note`: replace "This is a calculated optical limit, not a measured acuity." with "This is a calculated receptor sampling limit (focal length over twice the receptor separation), not a measured acuity."

Line 3, `note`: replace "the paper does not explain the gap, so the printed figures need caution." with "0.00086 equals wavelength over aperture (500 nm / 580 um = 0.000862) without the 1.22 factor (my arithmetic); the paper does not explain the gap, so the printed figures need caution."

Line 3, `note`: append " The 4 um diameter and 200 um length in Table 3 match the dorso-posterior patch, the narrowest of the 4 to 7 um rhabdom widths reported; with 7 um the same equation gives about 52.9 cycles per radian, 0.92 cycles/degree (my arithmetic), so 1.61 is a best-case value. The Discussion says the retinal bump of this species, from the optic lobe pressing much of the temporal retina toward the lens, results in 'intentional hyperopic defocus over a half of the frontal scene'; Equation 3 assumes a focused image, and the paper does not say whether the bump and the patch overlap. Focal length was measured on MRI images of fixed animals."

## Faults noted, not counted

- Lines 1 to 3, `source.journal`: "Frontiers in Physiology 8: 105"; and in each note replace "Crossref gives volume 8 and no issue or article number." with "Crossref gives volume 8 and no issue or article number; the PDF prints Front. Physiol. 8:105."
- Line 1, `units`: "µm", main's form.
- Line 2, `note`: suggested addition " The paper reserves 'fovea-like' for the two deep-sea squid and describes this species' eye as having a retinal bump (hyperopic defocus over half the frontal scene, Discussion); its definition of a fovea is 'a pit or mound as well as a local increase in photoreceptor density'."
- Progress note: "p inferred to be the 4 um receptor diameter" should add that 4 um and 200 um are the patch dimensions.

Search records: none in the unit (0 of 0). Wanted lines: none. Held-out leads in the progress note were not searched.

Pooled with audits 172 to 237: 114 of 282 evidence records (40.4%; audits 172 to 237 113 of 279 as audit 237 gives it, audit 238 1 of 3).

Verdict: lines 1 and 2 can be merged as they stand (the not-counted fixes are better applied); line 3 can be merged only with the replacement text above. `access` "open" stands on the publisher's CC BY statement. Error line numbers: 3.

No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page opened; no paper text committed. Stray files: the desk-d153 copies stay untracked.
