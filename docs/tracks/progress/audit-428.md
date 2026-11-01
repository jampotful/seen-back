# audit-428: desk-d318, evidence lines 1-7

Audited 1 November 2026 from the desk-d318 files present untracked in the worktree (docs/tracks/progress/desk-d318.md and docs/views/evidence/desk-d318.jsonl; neither committed here, neither edited). HEAD equals origin/main (b5e93f6e4). Lines 8-14 belong to another auditor. `python3 -I tools/senses/check.py | grep d318`: "docs/views/evidence/desk-d318.jsonl: 14 records, 0 problems". Quote lengths (`len(q.split())`) for lines 1-7: 7, 12, 14, 15, 20, 8, 28, all within 40.

Sources opened (WebFetch): zookeys.pensoft.net/article/153178/download/xml/ (two passes), /article/183769/download/xml/, /article/8319/download/xml/ and europeanjournaloftaxonomy.eu/index.php/ejt/article/download/2547/11497, each URL returned by a WebSearch. zookeys.pensoft.net/article/199004/download/xml/ (Thornburghiella, published 29 Oct 2026) was not returned by two WebSearches (the paper is three days old and not yet indexed); the ID came from the Crossref record of the filed DOI, as the unit did, and the fetch was answered without refusal. Crossref single-DOI lookups api.crossref.org/v1/works/ for all five DOIs, each answered on the first call. PMC, PubMed, Plazi, GBIF, BHL, repository copies (uni-frankfurt, nordopen) and the uv.mx catalogue record were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 9 WebSearches.

## Bibliographic and licence

- Lines 1-2 (ZooKeys 1259: 277-286). Byline "Shuai-Lai Yang", "Xin-Ming Yin", "Yu-Qiang Xi"; Crossref same order; "Yang S-L, Yin X-M, Xi Y-Q" right. Title identical. Crossref issued 2025-11-11, no issue; vor CC BY 4.0; page prints "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0),". Accepted.
- Lines 3-4 (ZooKeys 1296: 77-90). Byline "Shuailai Yang, Yining Xi, Pei Wang, Xinming Yin, Yuqiang Xi" (no hyphens); Crossref same; "Yang S, Xi Y, Wang P, Yin X, Xi Y" right. Title identical. Issued 2026-10-29; vor CC BY 4.0; page CC BY 4.0 sentence. Accepted.
- Line 5 (ZooKeys 1278: 305-315). Byline Shuai-Lai Yang, Yi-Da Guo, Zhen Wang, Xin-Ming Yin, Yu-Qiang Xi; Crossref same; filed "Yang S-L, Guo Y-D, Wang Z, Yin X-M, Xi Y-Q" right. Title identical. Issued 2026-04-30; vor CC BY 4.0; page CC BY 4.0 sentence. Accepted.
- Line 6 (ZooKeys 584: 95-107). Byline "Jose Fernandez-Triana", "Caroline Boudreault" (unaccented); citation line "Fernández-Triana J, Boudreault C (2016)"; Crossref unaccented. Filing the byline spelling is within "as printed on the byline/citation line" and the note discloses both. Title verbatim including "gen. n. and sp. n., (Hymenoptera" and "U.S.,". Issued 2016-04-26; vor CC BY 4.0; page CC BY 4.0 sentence. Accepted.
- Line 7 (EJT 935: 81-100). Byline "Santiago JAUME-SCHINKEL", "Gunnar Mikalsen KVIFTE"; citation line "Jaume-Schinkel S. & Kvifte G.M. 2024. ... European Journal of Taxonomy 935: 81–100."; Crossref same order, no pages, licence CC BY 4.0 content version unspecified; PDF prints "This work is licensed under a Creative Commons Attribution License (CC BY 4.0)." Accepted by ruling.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

All five genera and seven species are printed as described in these papers (Psychodidae new species, Keylimepie peckorum gen. n. sp. n.); a WebSearch for "Trichomyia sinensis" / "Brunettia sinensis" returned only these papers and their derivatives, no senior homonym. Order Diptera / Hymenoptera and family Psychodidae / Braconidae from the Taxon classification keywords (all four ZooKeys papers); class blank right there (not printed). Line 7 class Insecta, order Diptera, family Psychodidae from the printed headings "Class Insecta Linnaeus, 1758", "Order Diptera Linnaeus, 1758", "Family Psychodidae Newman, 1834". Trait keys: eye_bridge_width_facets is on main (desk-d297, desk-d316); eye_type text for lines 5 and 6 fits.

## Repeats

`git grep -il -E` on origin/main (b5e93f6e4) over the whole docs/ tree for Brunettia, Thornburghiella, Trichomyia, Keylimepie, Eugenys and the five DOIs: no hits. Unmerged branches: every origin/research/desk-d* evidence file read through one `git cat-file --batch` and grepped for the same terms: only the desk-d318 lines themselves. No repeats.

## Per line

### Line 1, Brunettia sinensis, eye bridge 3 facet rows

Diagnosis, first sentence: "Eye bridge of three facet rows, contiguous." **Quote MATCH**, 7 words. Head: "Eye bridge of three facet rows, contiguous; interocular suture inverted Y-shaped; ..." one longer semicolon sentence; description "(N = 1)", no variation reported (tool summary). "Female. Unknown." Type material: holotype "1 ♂, China, Jilin, Changchun, Jingyuetan, 143°46'53"N, 125°27'48"E, 246 m, 2022.VIII.16, leg. Yuqiang Xi"; paratypes 1 ♂ Taimu Mt. 591 m Malaise Trap 2024.IV.26-V.10; 6 ♂♂ Huangren Mt. 260 m same dates Malaise Trap; 1 ♂ Fuzhou National Forest Park 230 m 2024.VI.23 leg. Rong Huang; 2 ♂♂ same park 253 m 2024.VI.30 leg. Shuailai Yang; 1 ♂ Shaanxi, Shimen Mt. 1670 m 2019.VII.24 (Qicheng Yang). Eleven male paratypes as filed. Remarks "eye bridge contiguous;" vs "In B. spinistoma Tokunaga & Komyo, the eye bridge is minute;" carried. Small slip, not counted: "with 4–6 ocular setae" ends the preceding Head sentence ("Head (Fig. 1A) about the same length as width; vertex about 1/4 times length of head; with 4–6 ocular setae."), not the eye-bridge sentence the conditions attach it to (optional fix).

**Line 1 MATCH.**

### Line 2, Brunettia zunyiensis, eye bridge 3 facet rows

Diagnosis first sentence: "Eye bridge of three facet rows, separated by about 1 facet diameter." **Quote MATCH**, 12 words. Head "Eye bridge of three facet rows, separated about 1 facet diameters;" as in conditions. Holotype 1 ♂ Kuankuoshui National Nature Reserve, 2016.VII.22, 1147 m, "leg. Malaise Trap"; paratype "1 ♂, same data as for holotype."; "Female. Unknown."; Remarks "In B. napaea Duckhouse, the eye bridge has four facet rows;". All right.

**Line 2 MATCH.**

### Line 3, Thornburghiella sichuanensis, eye bridge 6 facet rows

Diagnosis first sentence: "Eye bridge of 6 facet rows; flagellomere 1 with row of 6 strong spines." **Quote MATCH**, 14 words, whole semicolon-joined Diagnosis sentence. Value 6 is the Diagnosis count. Holotype 1 ♂ Wanglang National Nature Reserve, Changbaigou, 2403 m a.s.l., 2016.VII.17, leg. Yuqiang Xi; paratype "1 ♂ China: same data as holotype."; "Female. Unknown."; Remarks "eye bridge separated by about 5 facet diameters;". Right.

Fault: **variation misquoted.** The Description Head prints one clause run: "Eye bridge of 6 facet rows, in the anterior three columns of the eye bridge, a few eye bridges exhibit seven facet rows, separated by about 5 facet diameters;". The conditions cut it into 'Eye bridge of 6 facet rows, in the anterior three columns of the eye bridge' and 'a few eye bridges exhibit seven facet rows, separated by about 5 facet diameters', which attaches "in the anterior three columns" to the six rows and the separation to the seven-row bridges. As printed, the seven rows occur in the anterior three columns, and the separation belongs to the bridge as a whole. One record error, fixable.

**Line 3 FIXABLE.**

### Line 4, Thornburghiella yintiaolingensis, eye bridge 5 facet rows

Diagnosis: "Eye bridge of 5 facet rows, flagellomere 1 length bearing row of 6 long spines." **Quote MATCH**, 15 words (comma as printed). Head "Eye bridge of 5 facet rows, separated by about 3.46 facet diameter;"; Remarks "about 3.46 facet diameters"; holotype 1 ♂ Yintiaoling National Nature Reserve, Guanshan Protection Station, Pianyanwu, 2410 m a.s.l., 2025.V.9, leg. Shuailai Yang; paratype 1 ♂ same data; "Female. Unknown." All right.

**Line 4 MATCH.**

### Line 5, Trichomyia sinensis, eyes without eyebridge

Male Head: "Head (Figs 2A, 3A) suboval in frontal view, width 0.392 mm, length 0.287 mm; vertex 0.098 mm; eyes without eyebridge." **Quote MATCH**, 20 words, whole sentence between "Wing length 1.97 mm, width 0.809 mm." and "Supraocular bristles arranged in multiple rows." Diagnosis, key, Remarks, Discussion without eye wording; Introduction "with the eye bridge absent" for the subfamily (tool summary). Holotype 1♂ Baligou Scenic Area, Xilian Scenic Area, 871 m, 2025.VIII.16; paratypes 1♂ Baligou 717 m 2025.VIII.15 leg. Kailin Wang and 1♂ Tianchishan National Forest Park, Tourist Reception Center, 1020 m, 2025.VI.29; "Female. Unknown."; measurements "(N = 1)" without naming the specimen, as the conditions say. Collector spelled "Shuailai Yang" in the tool summary vs "Shuai-Lai Yang" filed; the summary may have normalised it, not counted.

**Line 5 MATCH.**

### Line 6, Keylimepie peckorum, eye small 0.6 × head height

Female Description, Head paragraph, sentence 6 of 10: "Eye small, its height 0.6 × head height." between "Malar line long, more than 2.8 × mandibular width." and "Ocelli relatively small, diameter of posterior ocelli about half of both OOL and POL." It is a whole printed sentence with its own capital and period, not cut from a longer sentence; it is telegraphic only. Judged strictly: **Quote MATCH**, 8 words; the unit's word "fragment" in the progress note means telegraphic, which the rules accept. Value "small (eye height 0.6 x head height)" says no more than the quote. Holotype "Female, CNC. UNITED STATES, Florida, Monroe County, North Key Largo, ... 3.IV.1985, Malaise trap, S. & J. Peck (colls)." voucher CNC483649; paratypes "3 ♀, 56 ♂ (CNC)" at Big Pine Key, Everglades NP, Fat Deer Key, North Key Largo, Sugar Loaf Key, Vaca Key (flight interception trap), 1985-1986; male description "As in female except for ..." with no eye wording; "Eye height: 0.27 mm."; genus Diagnosis "eye and ocelli small", Description "Eyes and ocelli small.", Comments "relatively small eyes and long malar space present interesting evolutionary questions." All carried. Not in conditions (optional): the putative autapomorphies include "reduced eyes".

**Line 6 MATCH.**

### Line 7, Eugenys micra, eye bridge 3 facet rows

Male Description, Head: "About 2 × as wide as long; eye bridge contiguous, eye bridge with three facet rows; no enlarged alveoli on postocular area (Fig. 4A); interocular suture appears absent." **Quote MATCH**, 28 words, whole semicolon-joined sentence after the "Head." label. Holotype 1 ♂ Ecuador, Pichincha, Pedro Vicente Maldonado, Roadway to Pachijal, alt. 750 m, 1–9 Feb. 2022, I. Kilian; paratypes 3 ♂ Costa Rica, Limón, Hitoy-Cerere Biological Reserve, alt. 100–200 m, 17–26 Feb. 1999, L.W. Quate (tool summary). "Female Unknown." Diagnosis without eye wording; no species Remarks; genus differential diagnosis "eyes contiguous, eye bridge with three facet rows."; E. singularis three rows; E. upsilon "two facet rows on narrowest part and three facet rows on remaining part of bridge". All right. "Limon" in conditions lacks the printed accent (optional fix, not counted).

**Line 7 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Brunettia sinensis, 3 rows | MATCH | | whole Diagnosis sentence; 11 male paratypes right |
| 2 | Brunettia zunyiensis, 3 rows | MATCH | | whole Diagnosis sentence |
| 3 | Thornburghiella sichuanensis, 6 rows | FIXABLE | conditions | seven-row variation cut so the "anterior three columns" location and the separation attach to the wrong clause |
| 4 | Thornburghiella yintiaolingensis, 5 rows | MATCH | | whole Diagnosis sentence |
| 5 | Trichomyia sinensis, eyes without eyebridge | MATCH | | whole Head sentence |
| 6 | Keylimepie peckorum, eye small 0.6 × head height | MATCH | | whole printed (telegraphic) sentence, not a cut fragment |
| 7 | Eugenys micra, 3 rows | MATCH | | whole Head sentence |

Errors: 1 of 7 records (14.3%); 1 fixable (line 3), 0 held out, 0 unfixable; no line to drop. Repeats: none. Verdict for desk-d318 lines 1-7: **ACCEPT AFTER REPLACEMENT** (lines 1, 2, 4-7 as filed; line 3 with the replacement below, or dropped if it is not applied). Pool with the other auditor's lines 8-14 for the unit rate.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 3:
- `conditions`: "the Description Head says 'Eye bridge of 6 facet rows, in the anterior three columns of the eye bridge' and 'a few eye bridges exhibit seven facet rows, separated by about 5 facet diameters'" -> "the Description Head says 'Eye bridge of 6 facet rows, in the anterior three columns of the eye bridge, a few eye bridges exhibit seven facet rows, separated by about 5 facet diameters;' (seven rows in the anterior three columns of a few bridges; the bridge is separated by about 5 facet diameters)"

Optional, not counted:
- Line 1 `conditions`: "inside a longer semicolon sentence (with 4-6 ocular setae)" -> "inside a longer semicolon sentence (the preceding Head sentence ends 'with 4–6 ocular setae')"
- Line 6 `conditions`: "pose evolutionary questions." -> "pose evolutionary questions; 'reduced eyes' is listed among the putative autapomorphies."
- Line 7 `conditions`: "Costa Rica, Limon," -> "Costa Rica, Limón,"
