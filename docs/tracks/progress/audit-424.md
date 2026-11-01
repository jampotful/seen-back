# audit-424: desk-d316, evidence lines 1 to 6

Audited 1 November 2026 from the desk-d316 files present untracked in the worktree (docs/tracks/progress/desk-d316.md and docs/views/evidence/desk-d316.jsonl; neither committed here, neither edited). This audit covers file lines 1 to 6 (Catocha jingfui, C. manmiaoe, C. shengfengi, Planetella taiwanensis, Asioditomyia bruneicola from Insects 13(1): 19; Proceroplatus dapanshanus from Insects 16(9): 883); lines 7 to 12 go to another auditor. HEAD equals origin/main (af3bdffb4). `python3 -I tools/senses/check.py | grep d316`: "docs/views/evidence/desk-d316.jsonl: 12 records, 0 problems". Quote lengths (`len(q.split())`), lines 1 to 6: 10, 10, 10, 3, 8, 10, all within 40.

Sources opened (WebFetch, every page URL from a WebSearch result): www.mdpi.com/2075-4450/13/1/19/html (four passes), www.mdpi.com/2075-4450/16/9/883 (two passes), wiki.krisyotam.com Catocha mirror (one pass, for name spellings). Crossref single-DOI lookups api.crossref.org/v1/works/ for both DOIs (10.3390/insects16090883 rate-limited once, read on the retry). PMC, GBIF, DOAJ and library catalogue records (katalog.lib.cas.cz, libmast.utm.my), the p.gyb.elementfx.com mirror, peeref and bionames were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 6 WebSearches.

## Bibliographic and licence

- Lines 1 to 5 (Ševčík, Hippa, Burdíková). Byline "Jan Ševčík", "Heikki Hippa", "Nikola Burdíková", same order in Crossref; title identical to Crossref; page citation line "Insects 2022, 13(1), 19;"; Crossref issued 2021-12-23, printed year 2022 used, right. Licence: the page prints no licence sentence (tool reports none in the read text; only meta-dc.rights https://creativecommons.org/licenses/by/3.0/); Crossref CC BY 4.0, vor. Accepted under the CC BY 3.0 page / CC BY 4.0 Crossref ruling.
- Line 6 (Wang, Zhu, Yu, Liu, Wu, Huang). Byline order matches Crossref (Qingyun Wang, Yi Zhu, Yefei Yu, Liwei Liu, Hong Wu, Junhao Huang); citation line "Insects 2025, 16(9), 883"; first part of the title read verbatim on the page, full title identical to Crossref; issued 2025-08-25. Page: no "Creative Commons Attribution" sentence, meta-dc.rights CC BY 3.0 and an Open Access badge; Crossref CC BY 4.0 vor. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout; no CC BY-NC-ND.

## Names and higher taxa

- Family and order: "3.2. Family Cecidomyiidae" (Catocha under 3.2.1, Planetella under 3.2.2) and "3.4. Family Ditomyiidae" (Asioditomyia under 3.4.1) printed as section headings; "(Diptera)" in the Insects 13 title; "(Diptera: Keroplatidae)" in the Insects 16 title. Right. Class: the Insects 16 page prints "Insecta" only in reference 3's title ("Catalog of the Keroplatidae of the World (Insecta: Diptera)"), not in the body (tool summary); no class seen on the Insects 13 page. Class blank is right.
- Spelling of two Catocha epithets (open item, not counted). The paper prints "Catocha manmiaoe sp. nov." and "Catocha shengfengi sp. nov." consistently in headings, Abstract and body, with ZooBank LSIDs, and the Etymology names Dr. Man-Miao Yang and Dr. Sheng-Feng Lin. A Wikipedia mirror (wiki.krisyotam.com, March 2026 dump) lists "Catocha manmiaoae" and "Catocha shengfengae" Ševčík, Hippa & Burdiková, 2021, and "Catocha jingfui". That mirror is not the group authority; Catalogue of Life / Systema Dipterorum were not reached (GBIF refused under the desk rules; two searches returned no CoL or Systema Dipterorum page). My own reading, with no source checked here, is that ICZN Articles 31.1.3 and 32.5.1 keep a patronym's original ending, so the printed spellings would stand; I have not verified which spelling the group authority uses. The merger should check Systema Dipterorum before filing lines 2 and 3 and use its accepted spelling if it differs.
- Planetella taiwanensis, Asioditomyia bruneicola and Proceroplatus dapanshanus: no competing spelling met; not checked against an authority page either (no budget spent; nothing suggested a problem).

## Repeats

`git grep -il -E` on origin/main (af3bdffb4) over the whole docs/ tree (evidence, audit/corrected, audit/ALL, sheets, searched, tracks and the rest) for Catocha, Planetella, Asioditomyia, Proceroplatus, jingfui, manmiao, shengfeng, bruneicola, dapanshan, insects13010019, insects16090883: no hit. The 315 other unmerged origin/research/desk-dN branches: each branch's docs/views/evidence/desk-dN.jsonl read with one `git cat-file --batch` (14 branches have no such file) and grepped for the same terms: no hit. No repeats.

## Per line

### Line 1, Catocha jingfui, eye bridge 3–4 facets wide

Male Head: "Eye bridge complete, 3–4 facets wide, similar medially and laterally." followed by "3 ocelli present, all well-developed." **Quote MATCH**: its own whole sentence in the Description, telegraphic but complete, not a heading or caption, 10 words, en dash as printed. Value [3, 4] is the range as printed; the bridge is one structure, so the count is per bridge as the sentence gives it; male as printed. Type material: "Holotype: male, Taiwan (China), Nantou, Yuan Feng, 2700 m, 2–23.iv.2019, Malaise trap 1," "Paratype: female, the same data as holotype". Conditions right (altitude 2700 m not given; optional). Female: "Similar to male in most respects." with no eye sentence; carried. Diagnosis compares aedeagal teeth and flagellomere necks with C. shengfengi, no eyes; carried. Genus section prints nothing on eye bridges.

**Line 1 MATCH.**

### Line 2, Catocha manmiaoe, eye bridge 3–4 facets wide

Same sentence in the male Head, followed by "No ocelli observable but the specimen is broken on the vertex." **Quote MATCH**, 10 words. Type material: holotype male "Nantou, Yuan Feng, 2700 m, 23–28.iv.2019, Malaise trap 2"; "Paratype: male, the same data as holotype" (read on the second pass). "Female. Unknown." No Diagnosis heading; the Discussion begins "Catocha manmiaoe sp. nov. belongs to C. latipes group". Conditions right, including the broken vertex. Spelling open item above.

**Line 2 MATCH.**

### Line 3, Catocha shengfengi, eye bridge 3–4 facets wide

Same sentence, followed by "3 ocelli present, all well-developed." **Quote MATCH**, 10 words. Holotype male "Nantou, Yuan Feng, 2700 m, 2–23.iv.2019, Malaise trap 1"; "Paratype: male, the same data as holotype"; "Female. Unknown."; Diagnosis "It is very similar to C. jingfui sp. nov. For distinguishing characters, see under the latter." with no eye text (the remaining diagnosis sentences were only summarized by the tool). Conditions right. Spelling open item above.

**Line 3 MATCH.**

### Line 4, Planetella taiwanensis, eye bridge lacking

"Eye bridge lacking." is its own period-terminated sentence in the Head part of the male Description, between "Brown, antenna pale yellowish brown, scape and pedicel little darker than flagellum, maxillary palpus pale yellowish brown." and "Antennal flagellum with 12 binodal tricircumfilial flagellomeres" (tool summary for its standing as a sentence, verbatim neighbours). Not a heading, caption or fragment. **Quote MATCH**, 3 words. Value "no eye bridge" says no more than the quote; eye_type fits a state with no count, and the note says why it is not filed under eye_bridge_width_facets. Type material: "Holotype: male, Taiwan (China), Nantou, Taitung, Tianlong trail, broad-leaved evergreen secondary forest, 920 m," "5.v.–8.vi.2016, Malaise trap, W. T. Yang leg."; no paratypes; "Female. Unknown."; Diagnosis has no eye text (tool summary). Conditions right; the printed "Nantou, Taitung" is the oddity the conditions disclose.

**Line 4 MATCH.**

### Line 5, Asioditomyia bruneicola, compound eye semiglobular

Male Head: "Frontal suture present." / "Compound eye semiglobular, not emarginated around antennal base." / "Maxillary palpus yellowish brown, consisting of one segment." **Quote MATCH**, whole sentence, 8 words; value matches it. Holotype "male, Brunei, Ulu Temburong National Park, Kuala Belalong Field Studies Centre, 10.–12.1.2014," "Malaise trap (G2M), J. Ševčík leg."; "Paratype: male, the same data as holotype, except for 7.–12.1.2014, Malaise trap (MT3),". Conditions right. Diagnosis compares gonostylus with A. lacii and A. japonica, no eyes (tool summary). The page prints "Female. Unknown."; the conditions say only that a female statement was not seen. The record is already scoped to males and two male types, so nothing filed is wrong; optional fix below.

**Line 5 MATCH.**

### Line 6, Proceroplatus dapanshanus, compound eye with slight medial invagination

Male Head: "Compound eye with slight invagination medially, covered with abundant pubescence.", followed by "Clypeus inverted triangular, rounded apically, bearing several dark bristles posteriorly and laterally."; the preceding sentence gives three ocelli "placed on slightly raised dark brown ocellar tubercle" (the "triangle" in the conditions was not returned verbatim). **Quote MATCH**, whole sentence, 10 words. Type material (tool summary of the long lines, with verbatim counts): holotype male, Dapanshan National Nature Reserve, Zhejiang, 1,245 m, 16 August 2023, Shuai Zhang, slide DPS-2-1; "2 males and 10 females" with the holotype data; further paratypes at Longwangshan "31 males and 22 females", Tianmushan "1 female", Dinghu "4 males and 4 females", Wugui "7 males and 3 females", Dayaoshan "2 males", Huaping "1 female", Leigong "2 females", Fanjing "2 males", Meitan "1 female", Honghuagang "2 males": 50 male and 44 female paratypes, as the conditions say. Female description has no eye sentence; Diagnosis and key have none; no Remarks section. Conditions right.

Fault: **qualifier dropped in the value.** The value "medially invaginated, covered with abundant pubescence" drops "slight" from "with slight invagination medially", so the value says more than the quote. One record error, fixable.

**Line 6 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Catocha jingfui, eye bridge 3–4 facets | MATCH | | whole telegraphic sentence; male holotype, female paratype; female "Similar to male" carried |
| 2 | Catocha manmiaoe, eye bridge 3–4 facets | MATCH | | male paratype confirmed; broken vertex carried; spelling open item |
| 3 | Catocha shengfengi, eye bridge 3–4 facets | MATCH | | male holotype and paratype; spelling open item |
| 4 | Planetella taiwanensis, no eye bridge | MATCH | | "Eye bridge lacking." is its own sentence; holotype only |
| 5 | Asioditomyia bruneicola, eye semiglobular | MATCH | | whole sentence; female "Unknown." not carried (optional) |
| 6 | Proceroplatus dapanshanus, eye invagination | FIXABLE | value | value drops "slight" |

Errors: 1 of 6 records (16.7%); 1 fixable (line 6), 0 held out, 0 unfixable; no line to drop. Repeats: none. Open item, not counted: Catocha manmiaoe / C. shengfengi spelling against Systema Dipterorum (a Wikipedia mirror has -ae endings); check before filing lines 2 and 3. Verdict for desk-d316 lines 1 to 6: **ACCEPT AFTER REPLACEMENT** (lines 1 to 5 as filed; line 6 with the replacement below, or dropped if it is not applied).

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 6:
- `value`: "medially invaginated, covered with abundant pubescence" -> "slight invagination medially, covered with abundant pubescence" (old string as the whole JSON field `"value": "medially invaginated, covered with abundant pubescence"`, which occurs once)

Optional, not counted:
- Line 5 `conditions`: "A female statement was not seen (page text read ended inside the Description)." -> "Female 'Unknown.'"
- Lines 1 and 3 `conditions`: "Holotype male: Nantou, Yuan Feng, 2–23.iv.2019" -> "Holotype male: Taiwan, Nantou, Yuan Feng, 2700 m, 2–23.iv.2019"
- Line 2 `conditions`: "Holotype male: Nantou, Yuan Feng, 23–28.iv.2019" -> "Holotype male: Taiwan, Nantou, Yuan Feng, 2700 m, 23–28.iv.2019"
