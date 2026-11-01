# audit-414: desk-d311, evidence file lines 36 to 42

Audited 1 November 2026 from the desk-d311 files present untracked in the worktree (docs/tracks/progress/desk-d311.md and docs/views/evidence/desk-d311.jsonl, 50 lines; neither committed here, neither edited). This audit covers file lines 36 to 42 only; six other auditors take the rest. HEAD equals origin/main (095e055d8). `python3 -I tools/senses/check.py | grep d311`: "docs/views/evidence/desk-d311.jsonl: 50 records, 0 problems". Quote lengths (`len(q.split())`) for lines 36 to 42: 16, 15, 15, 15, 15, 15, 15, all within 40.

All seven lines come from one paper: Yin, Hlaváč, Li 2013, ZooKeys 275: 23-65, 10.3897/zookeys.275.4571. It was read once (six WebFetch passes on zookeys.pensoft.net/article_preview.php?id=3726, a URL returned by a WebSearch) and every line is judged from it. Crossref single-DOI lookup api.crossref.org/v1/works/10.3897/zookeys.275.4571 read on the first call. Not opened: optimap, BHL, species-id.net, the ebusca.uv.mx library catalogue record. No curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 1 WebSearch.

## Bibliographic and licence

- Byline "Zi-Wei Yin, Peter Hlaváč, Li-Zhen Li"; Crossref Yin, Hlavac, Li in the same order. Record "Yin Z-W, Hlaváč P, Li L-Z" right (accent as printed).
- Title identical on page and Crossref: "Further studies on the Pselaphodes complex of genera from China (Coleoptera, Staphylinidae, Pselaphinae)".
- Citation line "ZooKeys 275: 23–65, doi: 10.3897/zookeys.275.4571", published 4 March 2013; Crossref volume 275, no issue, page 23-65, issued 2013-03-04. Record journal "ZooKeys 275: 23-65", year 2013 right.
- Licence: page "This is an open access article distributed under the terms of the Creative Commons Attribution License 3.0 (CC-BY),"; Crossref CC BY 3.0, vor. Accepted; source.access "open" right.

Bibliographic faults 0; licence faults 0.

## Names and higher taxa

Order, family and subfamily printed in the title (Coleoptera, Staphylinidae, Pselaphinae); the records file Staphylinidae, Coleoptera. The page prints neither "Insecta" nor "Animalia" and has no Taxon classification line (tool summary), so class blank is right. All seven are described as new in this paper by its authors; no later synonymy is claimed in the unit and none was found in the search results. Not counted.

## Repeats

`git grep -il` on origin/main (095e055d8) over the whole docs/ tree for "Labomimus simplicipalpus", simplicipalpus, "Pselaphodes anhuianus", anhuianus, "Pselaphodes daii", daii, grebennikovi, hainanensis, kuankuoshuiensis, longilobus, zookeys.275.4571, zookeys.275. The only hits are for the DOI: desk-d302 line 1 (Dayao emeiensis female, ommatidia_count), its progress file and audit-394; a different species, as the notes say. No species hit. Unmerged origin/research/desk-d* and audit-* branches (717, d311 excluded): one `git grep -il -E` per branch over docs/views/evidence, audit and sheets for the seven species and the DOI, d302 copies excluded; result given in the grep line below.

## Per line

All seven quotes are the opening sentence of the "Male." paragraph of each species' Description, in the paper's telegraphic style (head dimensions, semicolon, eye count); the sentence is whole and starts at its printed start, as the audit-395/403 precedent accepts. Each was returned verbatim by the tool with en dashes in the ranges. In every species the Diagnosis, Comparative notes and Distribution say nothing about eyes, and the Abstract, Material and methods, genus diagnoses, keys and Discussion say nothing about facets (Methods mention eyes only in "HW–width of the head across eyes"; tool summary for the absence). "about" kept in every value; counts are per eye ("eyes each composed of") and none is shown as a total.

### Line 36, Labomimus simplicipalpus, about 40 facets per male eye

Male: "Head slightly longer than wide, HL 0.65, HW 0.59; eyes each composed of about 40 facets." **Quote MATCH.** Female: "Female. Unknown." Holotype ♂ "CHINA: Sichuan, Luding County / Hailuogou N. R.," 2200–2300 m, 27 July 2006, Hu & Tang (SNUC); no paratype entry (tool summary). Conditions right.

**Line 36 MATCH.**

### Line 37, Pselaphodes anhuianus, about 50 facets per male eye

Male: "Head longer than wide, HL 0.66–0.72, HW 0.60–0.64; eyes each composed of about 50 facets." **Quote MATCH.** Type material "(2 ♂♂, 1 ♀)"; holotype Tianzhu Shan National Park, Qianshan County, Anhui, 2006.iv.23; 1 ♀ with holotype data; 1 ♂ Dabieshan, Hubei, 11–21 June 2008 (tool summary). Female "Eyes each composed of about 26 facets." carried. Conditions right. "about half the male count" is the desk's own arithmetic, not printed (optional fix).

**Line 37 MATCH.**

### Line 38, Pselaphodes daii, about 30 facets per male eye

Male: "Head longer than wide, HL 0.78–0.81, HW 0.62–0.65; eyes each composed of about 30 facets." **Quote MATCH.** "(19 ♂♂, 10 ♀♀)"; holotype Er'lang Shan, Tianquan County, 2800 m, 2012.vii.13. Paratype entries read in full: 6 ♂♂ 5 ♀♀ + 2 ♂♂ (Er'lang Shan 2012), 1 ♂ "1999.VI.22 / leg. M. Schülke", and Gongga Shan 2011 entries 2 ♂♂, 5 ♂♂ 2 ♀♀, 1 ♂ 1 ♀, 1 ♀, 1 ♀, 1 ♂: 18 ♂♂, 10 ♀♀. Female "Eyes each composed of about 25 facets." Conditions right.

**Line 38 MATCH.**

### Line 39, Pselaphodes grebennikovi, about 40 facets per male eye

Male: "Head longer than wide, HL 0.76–0.80, HW 0.66–0.69; eyes each composed of about 40 facets." **Quote MATCH.** "(2 ♂♂, 5 ♀♀)"; holotype "Cang Shan at Dali", 2.VII.2011, 2714 m; paratypes 1 ♂ 5 ♀♀ same data. Female "Eyes each composed of about 25 facets." Conditions right.

**Line 39 MATCH.**

### Line 40, Pselaphodes hainanensis, about 40 facets per male eye

Male: "Head longer than wide, HL 0.69–0.72, HW 0.63–0.65; eyes each composed of about 40 facets." **Quote MATCH.** "(24 ♂♂, 8 ♀♀)"; holotype Yuanmeng near Yinggezui Station, Baisha County, 660 m, 2011.iv.26. Paratype entries sum to 23 ♂♂, 8 ♀♀ from Yuanmeng (7 ♂♂ with the holotype data), Wuzhishan, Diaoluoshan, Jianfengling and Limu Shan (tool summary of the entries). Conditions list the four other localities but omit that 7 male paratypes share the holotype locality (optional). Female "Eyes each composed of about 30 facets." Conditions right.

**Line 40 MATCH.**

### Line 41, Pselaphodes kuankuoshuiensis, about 40 facets per male eye

Male: "Head longer than wide, HL 0.71–0.72, HW 0.64–0.65; eyes each composed of about 40 facets." **Quote MATCH.** Two males, three females (tool summary of the totals); holotype Baishaogou, Kuankuoshui N. R., Suiyang County, 750–900 m, 2010.VI.05; paratypes 1 ♂ 2 ♀♀ same data and 1 ♀ "2010.VI.03". Conditions "4 paratypes (1 male, 3 females, same locality)" right. Female "Eyes each composed of about 25 facets."

**Line 41 MATCH.**

### Line 42, Pselaphodes longilobus, about 25 facets per male eye

Male: "Head longer than wide, HL 0.71–0.73, HW 0.63–0.64; eyes each composed of about 25 facets." **Quote MATCH.** Four males, five females (tool summary); holotype Jizushan, 28.VI.2011, 3216 m; paratypes 1 ♂ 4 ♀♀ Jizushan 30.VI.2011, 2875 m, and 2 ♂♂ 1 ♀ Dabieshan, Hubei, 11–21.VI.2008, 640 m. Conditions "8 paratypes (3 males, 5 females; Jizushan, Yunnan, and Dabieshan, Hubei)" right. Female "Eyes each composed of about 20 facets."

**Line 42 MATCH.**

## Verdict

| line | taxon / value | verdict | reason |
|---|---|---|---|
| 36 | Labomimus simplicipalpus, about 40 facets per male eye | MATCH | whole Male sentence; holotype only, female unknown |
| 37 | Pselaphodes anhuianus, about 50 | MATCH | type series and female 26 right |
| 38 | Pselaphodes daii, about 30 | MATCH | 18 ♂♂ 10 ♀♀ paratypes, 1999 and Gongga Shan confirmed |
| 39 | Pselaphodes grebennikovi, about 40 | MATCH | type series and female 25 right |
| 40 | Pselaphodes hainanensis, about 40 | MATCH | 23 ♂♂ 8 ♀♀ paratypes confirmed |
| 41 | Pselaphodes kuankuoshuiensis, about 40 | MATCH | type series and female 25 right |
| 42 | Pselaphodes longilobus, about 25 | MATCH | type series and female 20 right |

Errors: 0 of 7 records (0%); 0 fixable, 0 held out, 0 unfixable; no line to drop. Repeats: none on main. Verdict for desk-d311 lines 36 to 42: **ACCEPT** (pooled verdict rests with the six other audits of this unit).

## Replacement

None required. Optional, not counted (each old string occurs once in its line):

- Line 37 `conditions`: "'Eyes each composed of about 26 facets', about half the male count." -> "'Eyes each composed of about 26 facets'."
- Line 40 `conditions`: "and 31 paratypes (23 males, 8 females; Wuzhishan," -> "and 31 paratypes (23 males, 8 females; 7 males with the holotype data, others from Wuzhishan,"
