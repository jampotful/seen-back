# audit-390: desk-d298, evidence lines 1 to 4

Audited 1 November 2026 from the desk-d298 files present untracked in the worktree (docs/tracks/progress/desk-d298.md and docs/views/evidence/desk-d298.jsonl, 4 lines; neither committed here, neither edited; identical to origin/research/desk-d298). Line numbers are the file's (1-based). HEAD equals origin/main (9ca73c1c). `python3 -I tools/senses/check.py | grep 'd298\.'`: "docs/views/evidence/desk-d298.jsonl: 4 records, 0 problems". Quote lengths (`len(q.split())`): 14, 3, 3, 6, all within 40; the only non-ASCII character is the ellipsis closing line 1.

Sources opened (WebFetch): zookeys.pensoft.net/article/130885/download/xml/ (two passes); journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0057756 (the record's url; three rate-limited attempts on the www.plosone.org search result, which then redirected to the journal home page; the record's url then opened once); eres.library.adelaide.edu.au/dspace/bitstream/2440/106056/2/hdl_106056.pdf (search result; publisher-formatted PDF of the same article in the University of Adelaide repository, used only to read the type lists, Variation and Introduction while the PLOS page was rate limited; not a licence basis); zookeys.pensoft.net/article_preview.php?id=122265 (two passes); zse.pensoft.net/article/90520/download/xml/ (two passes); amphibiansoftheworld.amnh.org Microcaecilia dermatophaga page; Crossref single-DOI lookups api.crossref.org/v1/works/ for the four DOIs. PMC, Plazi, FishBase, DOAJ, novataxa, news and wiki hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 7 WebSearches.

## Bibliographic and licence

- Line 1 (Hibino, Ho 2024). Page and Crossref same order (Yusuke Hibino, Hsuan-Ching Ho); title identical; ZooKeys 1220: 45-62, no issue; issued 2024-12-09; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 2 (Wilkinson, Sherratt, Starace, Gower 2013). Page and Crossref same order; title identical; PLoS ONE 8(3): e57756; issued 2013-03-06; Crossref CC BY 4.0 content-version unspecified; the PLOS page prints "This is an open-access article distributed under the terms of the Creative Commons Attribution License," so accepted under the "unspecified + page-printed" rule.
- Line 3 (Ribeiro, Santos Jr, Martins, Oliveira, Graboski, Da Silveira, Benício, Vaz-Silva 2024). Page and Crossref same order; title identical; ZooKeys 1213: 1-27, no issue; issued 2024-09-24; Crossref CC BY 4.0 vor; page prints CC BY 4.0 (tool summary). Accepted.
- Line 4 (Roberts, Iova, Austin 2022). Page and Crossref same order; title identical; Zoosystematics and Evolution 98(2): 399-409; issued 2022-10-05; Crossref CC BY 4.0 vor; XML prints CC BY 4.0 (tool summary). Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

Yirrkala nkust, Amphisbaena amethysta and Toxicocalamus longhagen are described as new in the cited papers; names rest on the original descriptions (FishBase and Reptile Database not opened). Microcaecilia dermatophaga: Amphibian Species of the World lists it as the current name under Gymnophiona/Siphonopidae/Microcaecilia, original citation the cited PLoS ONE paper, no synonymy or generic reassignment shown (tool summary); the brief's suspected taxonomic change was not found. Ophichthidae/Anguilliformes (title), Siphonopidae/Gymnophiona (title), Amphisbaenidae/Squamata (title), Elapidae/Squamata (title). Names faults 0.

## Trait keys

All four use eye_type with descriptive text; line 2's "none visible externally (eyes not visible)" keeps the "not visible, not absent" sense. Trait-key faults 0.

## Duplicates

`git grep -i` on origin/main (9ca73c1c) under docs/ (evidence, audit/corrected, audit/ALL, sheets, searched/ included) for nkust, Yirrkala, dermatophaga, Microcaecilia, amethysta, longhagen, Toxicocalamus and the DOI strings zookeys.1220.130885, pone.0057756, zookeys.1213.122265, zse.98.90520: the only hit for any of the four species or DOIs is desk-d295.md line 19, which lists Microcaecilia dermatophaga as "Text not reached ... (PLoS ONE, rate limited)", so nothing filed. Broader Amphisbaena hits are A. alba (oa-1 opsin predictions, gaps, sweep-69/72), unrelated. All 1474 remote branches grepped under docs/ for the species names and DOI strings: hits only on research/desk-d298 itself and copies of desk-d295.md on desk-d295/d297/d298 and audit-387/388/389. Duplicate faults 0.

## Per line

### Line 1, Yirrkala nkust, eye_type "small, covered by a transparent skin"

XML, Results, Yirrkala nkust sp. nov., Description: "Eye small, covered by a transparent skin; center of eye anterior to mid-jaw (Figs 1B, 2B)." The quote "Eye small, covered by a transparent skin; center of eye anterior to mid-jaw …" drops only the trailing figure reference and the full stop; the ellipsis marks a real cut and no qualifier goes with it. The semicolon is inside the quote, not at the cut. **Quote MATCH.** Value is the first clause and says no more. Type material as filed: holotype NMMB-P38652, 496 mm TL, 12 July 2021; paratypes NMMB-P38645 (315 mm), NMMB-P39317 (462 mm), KMNH VR 100650 (297 mm); no sex printed for any specimen. The Description gives ranges with holotype values in parentheses ("3.4–3.7 times eye diameter (3.7 in holotype)") and Table 1 has holotype and paratype columns, so "not specific to the holotype" holds. Diagnosis, Remarks and comparisons do not mention the eye. Not counted: Y. kaupii in the same paper reads "Eye moderate in size, covered by a transparent skin; center of eye anterior to mid-jaw (Fig. 4C).", so "small" is the species' contrast with its congener; optional addition below.

**Line 1 MATCH.**

### Line 2, Microcaecilia dermatophaga, eye_type "none visible externally (eyes not visible)"

PLOS page and PDF, Description of the holotype: "Eyes not visible." follows the snout/lip sentence. **Quote MATCH.** The account has no Results heading and follows Materials and Methods, so the `where` is right. Holotype "BMNH 2008.715, a mature male", kept "alive in captivity until July 2012", as filed.

Faults:
1. Conditions. Paratypes are BMNH 2008.716-720 and MNHNP 2010.0190, BMNH 2008.721 and BMNH 2008.722 (eight). The Variation reads "There are two size classes, with six mature specimens with total lengths of between 148 and 164 mm" and "three much smaller and less attenuate immature specimens (BMNH 2008.718–720)": six plus three is nine, the holotype included, so the paratypes are five mature and three immature, not "six mature, three immature". Table 1 gives a sex entry for each mature specimen ("Specimens without sex data are immature."; tool summary), so "individual sexes not stated" is also wrong. Fixable.
2. Note. The Introduction identifies this species, not only the genus, "as a Microcaecilia on the basis of having eyes under bone": the eyes are present and covered. The note files this as "genus-level", which misreports the species-level statement that explains "not visible". Fixable (counted with fault 1 as one record error).

**Line 2 FIXABLE.**

### Line 3, Amphisbaena amethysta, eye_type "eyes slightly visible"

Results, Amphisbaena amethysta sp. nov., Description of the holotype: "Eyes slightly visible." directly after the ocular-shield sentence. **Quote MATCH.** Holotype CEPB 2311 male, Caetité, 1 November 2022; paratypes CEPB 2301, 2303, 2308, 2327, 2331, 2381 females and 2302, 2346, 2379 males, as filed. Intraspecific variation, paratype lists, Table 2, Diagnosis, comparisons and Abstract carry no eye-visibility statement (tool summary); the only other "ocular" in the comparisons is the A. cubana shield fusion. Holotype-only stated.

**Line 3 MATCH.**

### Line 4, Toxicocalamus longhagen, eye_type "small eye, round pupil"

Results, Toxicocalamus longhagen sp. nov., Description of the holotype: "Eye small (diameter 1.6); pupil round." **Quote MATCH.** Holotype PNGM 22160, "Adult male confirmed by µCT scans", Dobel, Mt. Hagen Town, 1,650 m, 25 February 1967; "only known from the holotype". The diameter is not logged, so the unstated axis and side do not touch the value. Not counted: the note says the unit was "not confirmed on the page read", but Materials and methods prints "All measurements were taken in millimeters and reported to the first decimal"; optional correction below.

**Line 4 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Yirrkala nkust, small, transparent skin | MATCH | none | quote MATCH (14); cut is the figure ref only; four types, no sexes printed |
| 2 | Microcaecilia dermatophaga, none visible externally | FIXABLE | conditions, note | paratype maturity miscounted (holotype in the "six mature"); species-level "eyes under bone" filed as genus-level |
| 3 | Amphisbaena amethysta, slightly visible | MATCH | none | quote MATCH (3); holotype-only and all paratypes stated |
| 4 | Toxicocalamus longhagen, small, round pupil | MATCH | none | quote MATCH (6); single specimen stated |

Errors 1 of 4 audited records (25%). By kind: quotes 0; location 0; value meaning 0; omitted variation 0; sample composition 1 (line 2); bibliographic 0; licence 0; names 0; trait key 0; duplicates 0. Fixable; nothing unfixable, nothing held out. Verdict: merge lines 1-4 with the Replacement applied (line 2 required; lines 1 and 4 optional).

Unchecked: figures not viewed; Table 1 of the PLoS ONE paper read only through the tool (sex symbols not rendered), so the individual sexes of the mature paratypes were not read; no checklist opened for Y. nkust, A. amethysta or T. longhagen.

## Replacement

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 2:
- `conditions`: "The paper lists eight paratypes (six mature, three immature as printed; individual sexes not stated) but does not describe their eyes" -> "The paper lists eight paratypes (BMNH 2008.716-722 and MNHNP 2010.0190): five mature and three immature (BMNH 2008.718-720); the Variation's 'six mature specimens' counts the holotype, and Table 1 gives sex for the mature specimens only. The paratypes' eyes are not described"
- `note`: "Elsewhere the Introduction describes the genus as having small eyes covered with bone (genus-level, outside the Description; not logged)." -> "The Introduction says the genus has small eyes covered with bone and identifies this species 'as a Microcaecilia on the basis of having eyes under bone', so the eyes are present but covered by bone (outside the Description; not logged separately)."

Line 1 (uncounted):
- `note`: "the Diagnosis and Abstract do not mention the eye." -> "the Diagnosis and Abstract do not mention the eye. The congener Y. kaupii in the same paper has 'Eye moderate in size, covered by a transparent skin; center of eye anterior to mid-jaw (Fig. 4C).'"

Line 4 (uncounted):
- `note`: "(unit not confirmed on the page read)" -> "(Materials and methods: 'All measurements were taken in millimeters', so 1.6 mm; axis and side not stated)"
