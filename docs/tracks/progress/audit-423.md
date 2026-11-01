# audit-423: desk-d315, evidence lines 17 to 24

Audited 1 November 2026 from the desk-d315 files present untracked in the worktree (docs/tracks/progress/desk-d315.md and docs/views/evidence/desk-d315.jsonl, 24 lines; neither committed here, neither edited). This audit covers file lines 17 to 24 only (five Cranopygia species, Diplatys sahyadriensis, Didymocorypha libaii, Arria muscoamicta); lines 1 to 16 go to two other auditors. HEAD equals origin/main (2bb4cdea5). `python3 -I tools/senses/check.py | grep d315`: "docs/views/evidence/desk-d315.jsonl: 24 records, 0 problems". Quote lengths (`len(q.split())`) for lines 17 to 24: 8, 8, 8, 8, 8, 8, 6, 9, all within 40.

Sources opened (WebFetch, every URL from a WebSearch result): zookeys.pensoft.net/article/175635/download/xml/ (two passes), zookeys.pensoft.net/article_preview.php?id=79416 (three passes), zookeys.pensoft.net/article_preview.php?id=47987 (two passes), zookeys.pensoft.net/article/47987/download/xml/ (two passes), zookeys.pensoft.net/article/62347/download/xml/ (two passes). Crossref single-DOI lookups (api.crossref.org/v1/works/) answered for 10.3897/zookeys.1262.175635, 10.3897/zookeys.1088.79416 and 10.3897/zookeys.1028.62347; 10.3897/zookeys.922.47987 failed with a client error and failed again on the one retry, so its bibliography was read from the publisher citation line and title on the article page (not worked around). Plazi treatments, PMC, GBIF, BHL, DOAJ, bionames, novataxa, zenodo, ebusca.uv.mx and reviewer.ly results were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 5 WebSearches.

## Bibliographic and licence

- Lines 17 to 21 (Chen, Jiang 2025). Byline "Zhi-Teng Chen", "Chao Jiang"; citation line "Chen Z-T, Jiang C (2025) Five new species of Cranopygia (Dermaptera, Pygidicranidae) from South China." with ZooKeys 1262: 335–354; Crossref same order, title identical, volume 1262, no issue, pages 335-354, issued 2025-12-10, CC BY 4.0 vor. Page licence sentence "...Creative Commons Attribution License (CC BY 4.0),". Accepted.
- Line 22 (Karthik, Kamimura, Kalleshwaraswamy 2022). Byline "Chikkabidare M. Karthik, Yoshitaka Kamimura, Chicknayakanahalli M. Kalleshwaraswamy"; citation "Karthik CM, Kamimura Y, Kalleshwaraswamy CM (2022)" ... "ZooKeys 1088: 53-64."; Crossref identical in order and title, issued 2022-03-07, CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 23 (Wu, Liu 2020). Crossref single-DOI lookup refused twice (client error), not worked around. Page byline "Chao Wu, Chun-Xiang Liu"; citation line "Wu C, Liu C-X (2020) New record of Didymocorypha Wood-Mason (Mantodea, Eremiaphilidae) from China" ... "ZooKeys 922: 51-64."; title printed "New record of Didymocorypha Wood-Mason (Mantodea, Eremiaphilidae) from China," / "with description of a new high-altitude wingless mantis species in Asia", matching the record; page prints the CC BY 4.0 sentence. Accepted on the page alone.
- Line 24 (Unnahachote, Shcherbakov, Pinkaew 2021). Authors in order as in the record; citation "Unnahachote T, Shcherbakov E, Pinkaew N (2021)" and "ZooKeys 1028: 49–60"; Crossref title identical, issued 2021-04-05, CC BY 4.0 vor; XML prints the CC BY 4.0 sentence. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout; no issue printed for any of the four ZooKeys papers.

## Names and higher taxa

- Cranopygia (lines 17 to 21): Taxon classification block "Animalia", "Dermaptera", "Pygidicranidae"; "Insecta" appears nowhere outside references (tool summary), so class blank is right. All five described as new in this paper.
- Diplatys sahyadriensis (line 22): Taxonomy headings "Order Dermaptera de Geer, 1773" ... "Family Diplatyidae Verhoeff, 1902"; class Insecta from the title. Right.
- Didymocorypha libaii (line 23): the XML treatment carries a "Taxon classification" block "Animalia", "Mantodea", "Eremiaphilidae" (the HTML preview showed none); "Insecta" only in references. Class blank right.
- Arria muscoamicta (line 24): block "Animalia", "Mantodea", "Mantidae"; title and headings Haaniidae (Arriini). The note discloses the conflict and uses the title's Haaniidae, which is the current placement of Arria. Accepted.

## Repeats

`git grep -il -E` on origin/main (2bb4cdea5) over the whole docs/ tree (evidence, audit/corrected, audit/ALL, sheets, searched, tracks) for Cranopygia, kongqueshana, lisu (as "Cranopygia lisu"), liuhuaishana, longibifurcata, shidianensis, 175635, sahyadriensis, zookeys.1088.79416, Didymocorypha, libaii, zookeys.922.47987, muscoamicta, zookeys.1028.62347: no hits. Unmerged origin/research/desk-d* branches other than d315 (314 branches) grepped with the same pattern over docs/, gaps copies excluded: completed, no hits.

## Per line

### Lines 17 to 21, Cranopygia kongqueshana, lisu, liuhuaishana, longibifurcata, shidianensis: "Eyes not prominent, about as long as genae."

The paper has no genus description or diagnosis of Cranopygia, the identification key carries no eye couplet, and the Introduction does not mention eyes (tool summary). Each of the five species' own "Male" Description, Head paragraph, prints the sentence for that species, preceded by its own suture sentence: kongqueshana "Frontal and coronal sutures obscure."; lisu "Frontal sutures invisible, coronal suture obscure."; liuhuaishana "Frontal and coronal sutures obscure."; longibifurcata "Frontal and coronal sutures distinct."; shidianensis "Frontal and coronal sutures distinct.", each followed by "Eyes not prominent, about as long as genae." So the identical sentence is species-level five times over, not a shared or genus sentence filed as species. **Quote MATCH** in all five, whole telegraphic Description sentences, 8 words. Liuhuaishana also has "small pale spot near antero-inner margin of each eye" (colour; not an eye state, not required).

Material examined as the page prints it: kongqueshana "Holotype: China • ♂; Yunnan Province, Nujiang Lisu Autonomous Prefecture, Dimaluo Village, Kongque Mountain;" "28.0732°N, 98.7320°E; 2500 m; 18.vii.2025." "Paratype: China • ♂; same data as holotype."; lisu holotype ♂ only, Fugong County, Nujiang Grand Canyon National Park, 1800 m, 24.viii.2025, Hu Xiao (tool summary for the leg. form); liuhuaishana "Holotype: China • ♂; Guangxi Province, Nanning City, Wuming District, Liuhuai Mountain;" "22.9774°N, 108.3370°E; 880 m; 20.v.2024."; longibifurcata holotype ♂ only, Mang City, Kongque Valley Forest Park, 1350 m, 6.vii.2025; shidianensis holotype ♂ and paratype ♀ same data, Guojiafenbaobao, 1210 m, 6.v.2025, Wei He (tool summary). Sex, type status, counts, localities, dates and collector statements all match the conditions; the shidianensis female description has no eye statement, as the conditions say.

Not counted: lines 17 to 20 say "Female unknown." The page prints no such sentence for these four species; their treatments describe the male only and list no female (tool summary). The statement is not contradicted by the page and touches no filed value, so it is listed as an optional wording fix.

**Lines 17, 18, 19, 20, 21 MATCH.**

### Line 22, Diplatys sahyadriensis, "Eyes prominent, distinctly longer than the post-ocular length."

Male (holotype) Description: preceding sentence "Head (Fig. 1a) slightly wider than long, widest in eye region; frons tumid but weakly depressed at apex;" ... "posterior margin strongly emarginated in middle."; then "Eyes prominent, distinctly longer than the post-ocular length."; then "Antennae (Fig. 1a, d) 17 segments or more ...". **Quote MATCH**, 8 words. Material examined: "Holotype (♂), India: Karnataka, Hosanagara-Shivamogga Road, Galigekola, 13°59'52.854"N, 75°22'42.576"E," "6.xi.2020, C.M. Karthik leg., ex. sugarcane."; no paratypes; "Female. Unknown."; voucher UAHSE19K in Materials and methods. Diagnosis (virga only), Key, Discussion, Etymology and Bioecology carry no eye wording; no Remarks section. Conditions right on all of this.

Fault: **placement misstated.** The `where` reads "Taxonomy, Order Dermaptera, Genus Diplatys, Description, Male (holotype)" and the conditions say "The sentence sits in the Description placed under the genus heading Diplatys in the Taxonomy section." The Taxonomy headings run "Genus Diplatys Audinet-Serville, 1831", then "Diplatys sahyadriensis Karthik, Kamimura & Kalleshwaraswamy, sp. nov.", then Material examined, Diagnosis, Description. The Description sits under the species heading, not the genus heading, and the record's wording invites the genus-level reading the brief warns against. The value itself is species-level and stands. One record error, fixable.

**Line 22 FIXABLE.**

### Line 23, Didymocorypha libaii, "Compound eyes long, oval, not bulging."

Male holotype Head: preceding "Paired juxtaocular bulges united into a conical extension with a complete median dorsal suture" ... "a deep vertical ventral groove (Fig. 4B)."; then "Compound eyes long, oval, not bulging."; then "Three ocelli, small, not obvious (Fig. 4B)." **Quote MATCH**, 6 words, read on the HTML preview and the XML. Material examined: Holotype "China • ♂; Tibet, Gyirong County; 28.404N, 85.332E; 3300 m; 20-VII-2017; Chao Wu leg.; IZCAS."; Paratypes "China • 4 ♂ 6 ♀; Tibet, Gyirong County; 28.397N, 85.351E; 2800~3300 m; 18~21-VII-2017; Chao Wu leg.; IZCAS", "3 ♂ 3 ♀; ditto; CWC • 1♀; ditto; CJZ", "1 ♀; Tibet, Gyirong County; 28.363N, 85.339E; 2672 m; 1-VIII-2018; Jin-Cheng Liu leg.; CWC." All as in conditions. Female: "Similar to male, but distinctly larger and stronger (Figs 1B, 5C)." with no eye sentence; wingless females from the Abstract ("both sexes are wingless") and genus diagnosis ("Female wingless"). Genus diagnosis contrast "Compound eyes large, oblong." and the species Diagnosis ocelli contrast are carried in conditions.

**Line 23 MATCH.**

### Line 24, Arria muscoamicta, "Wider than long, compound eyes strongly protruded antero-laterally, rounded."

Adult male: bold label "Head" with "(Fig. 3A)", then "Wider than long, compound eyes strongly protruded antero-laterally, rounded.", then "Ocellar tubercle elevated." **Quote MATCH**, 9 words, the label correctly excluded. Value repeats the eye clause only and says no more than the quote. Material examined: "Thailand – Nakhon Nayok Province • 1 ♂; Mueang district, Hin Tung subdistrict;" "01.IX.2018; alt. 1,240 m; W. Pathomwattananuruk leg.; THNHM-I-23353."; no paratypes; "Female. Unknown."; "Five nymphs were found on separate occasions by visual inspection in the moss close to where the holotype was collected." and "The nymphs could not be preserved." Winged male: holotype Forewing and Hindwing descriptions; the Introduction sentence ("the male has well-developed wings reaching beyond the tip of the abdomen, while the female is completely apterous") is about the genus, but the holotype description confirms wings. No genus diagnosis; the differential diagnosis and Discussion do not mention eyes. Section "Systematic accounts" right.

**Line 24 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 17 | Cranopygia kongqueshana, eyes not prominent | MATCH | | species' own male Head sentence; 1 ♂ holotype + 1 ♂ paratype right |
| 18 | Cranopygia lisu, eyes not prominent | MATCH | | species' own male Head sentence |
| 19 | Cranopygia liuhuaishana, eyes not prominent | MATCH | | species' own male Head sentence |
| 20 | Cranopygia longibifurcata, eyes not prominent | MATCH | | species' own male Head sentence |
| 21 | Cranopygia shidianensis, eyes not prominent | MATCH | | species' own male Head sentence; ♀ paratype has no eye text |
| 22 | Diplatys sahyadriensis, eyes prominent | FIXABLE | where, conditions | Description sits under the species heading, record says genus heading |
| 23 | Didymocorypha libaii, eyes long, oval, not bulging | MATCH | | genus contrast carried; type series right |
| 24 | Arria muscoamicta, eyes strongly protruded | MATCH | | Haaniidae vs block Mantidae disclosed |

Errors: 1 of 8 records (12.5%); 1 fixable (line 22), 0 held out, 0 unfixable; no line to drop. Repeats: none on main. The five identical Cranopygia sentences are each printed in that species' own male Description; none is a shared or genus sentence. Verdict for lines 17 to 24 of desk-d315: **ACCEPT AFTER REPLACEMENT** (lines 17 to 21, 23, 24 as filed; line 22 with the replacement below, or dropped if it is not applied).

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 22:
- `where`: "Taxonomy, Order Dermaptera, Genus Diplatys, Description, Male (holotype)" -> "Taxonomy, Diplatys sahyadriensis Karthik, Kamimura & Kalleshwaraswamy, sp. nov., Description, Male (holotype)"
- `conditions`: " The sentence sits in the Description placed under the genus heading Diplatys in the Taxonomy section." -> " The sentence sits in the Description under the species heading 'Diplatys sahyadriensis Karthik, Kamimura & Kalleshwaraswamy, sp. nov.' (after the genus heading); the Key, Discussion, Etymology and Bioecology have no eye wording."

Optional, not counted:
- Lines 17, 18, 19 and 20 `conditions`: "Female unknown. " -> "No female listed or described (the paper prints no female statement for this species). "
