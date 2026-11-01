# audit-422: desk-d315, evidence lines 9 to 16

Audited 1 November 2026 from the desk-d315 files present untracked in the worktree (docs/tracks/progress/desk-d315.md and docs/views/evidence/desk-d315.jsonl, 24 lines; neither committed here, neither edited). This audit covers file lines 9 to 16 only; lines 1 to 8 and 17 to 24 go to two other auditors. Worktree based on origin/main (2bb4cdea5). `python3 -I tools/senses/check.py | grep d315`: "docs/views/evidence/desk-d315.jsonl: 24 records, 0 problems". Quote lengths (`len(q.split())`), lines 9 to 16: 6, 9, 4, 5, 4, 6, 6, 5, all within 40.

Sources opened (WebFetch, every URL from a WebSearch result): www.mdpi.com/1424-2818/17/9/637 (two passes), mdpi.com/2075-4450/13/3/272 (two passes), zookeys.pensoft.net/article/168015/download/xml/ (two passes), zookeys.pensoft.net/article_preview.php?id=75490 (two passes), zookeys.pensoft.net/article/75490/download/xml/ (one pass), phasmida.speciesfile.org otus 1022588, 1022589, 855803 (two passes) and 856618, cockroach.speciesfile.org otus 862411 and 862418/inaturalist, catalogueoflife.org taxon 4LDQW. Crossref single-DOI lookups (api.crossref.org/v1/works/) for the four DOIs, each answered on the first call. PMC, Zenodo and repository copies, agris, peeref, reviewer.ly and library catalogue records were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 11 WebSearches.

## Bibliographic and licence

- Line 9 (Qin, Cui, Bian 2025). Byline "Yanting Qin 1,2 , Zhenzhen Cui 1,2,* and Xun Bian 1,2,*"; Crossref same order. Title identical; citation line "Diversity 2025, 17(9), 637"; Crossref 17, issue 9, article 637, issued 2025-09-10. Page body prints no licence sentence, metadata CC BY 3.0; Crossref CC BY 4.0 vor. Accepted.
- Line 10 (Qi, Tihelka, Cai, Song, Ai 2022). Byline and Crossref identical in order. Title identical (Crossref splits it before "from"). "Insects2022, 13(3), 272" (printed without a space); Crossref 13(3) 272, issued 2022-03-10. Footer prints "This article is an open access article distributed under the terms and conditions of the Creative Commons" "Attribution (CC BY) license" with a 4.0 link, metadata CC BY 3.0; Crossref CC BY 4.0 vor. Accepted.
- Lines 11 to 13 (Ren, Han, Che, Wang 2025). XML contrib order and Crossref identical; citation "ZooKeys 1261: 337–358." (record hyphen for printed en dash, as earlier desks); no issue; published 2 December 2025. XML prints "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0),"; Crossref CC BY 4.0 vor. Accepted.
- Lines 14 to 16 (Xu, Jiang, Yang 2023). Byline "Fangling Xu‡, Yingjie Jiang§, Maofa Yang‡"; Crossref same order. Title identical; "ZooKeys 1176: 37-53"; issued 2023-08-22; no issue. Same CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.

None of these four papers is one where Crossref order differs from the page (the unit's remark concerns the two Diapriidae, lines 1 and 2, outside this range). Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

- **Pseudoparamenexenus beiliuensis (line 9): not accepted.** Phasmida Species File (otu 855803, valid name "Neoparamenexenus (Breviparamenexenus) balteatus (Chen & He, 2002)") lists "Pseudoparamenexenus beiliuensis Qin, Cui & Bian, 2025 (subjective synonym of Prosceles balteatus Chen & He, 2002)" "in Ho, 2025: 9", citing Ho 2025, Hong Kong Entomological Bulletin 17(1): 3–25 (tool summary for the bulletin citation). The genus page (otu 856618, Pseudoparamenexenus Ho, 2016) does not list beiliuensis. Under the rulings a synonym is an error. Re-filing the line under N. balteatus would rest on a subjective synonymy and a quote that names a different binomial, so I count it unfixable and drop it. The unit did not report the synonymy.
- Cnipsomorpha yunnanensis and C. yuxiensis: both valid in Phasmida Species File (otus 1022588, 1022589; Xu, Jiang & Yang, 2023; Phasmatidae, Clitumninae, Medaurini). Right.
- Pseudoeupolyphaga duani and P. menglianensis: described 2 December 2025. Cockroach Species File pages for the genus or species were not reached (the two CSF results were Eupolyphaga pages); no synonymy found. Not counted.
- Prolucanus beipiaoensis: no authority check beyond the page (fossil; Lucanidae). Not counted.
- Higher taxa: Lonchodidae and Phasmatodea are printed as Taxonomy headings ("Order: Phasmatodea Leach, 1815", "Lonchodidae Brunner von Wattenwyl, 1893"); Prolucanus prints "Order Coleoptera Linnaeus, 1758" and "Family Lucanidae Latreille, 1804" with no class heading; the Pseudoeupolyphaga and Cnipsomorpha XML taxon classification blocks print "Animalia", the order and the family, no class (the Cnipsomorpha article keywords list "Insecta", which is not a classification line, and the article_preview page shows no classification block). Class blank is right for all eight lines.

## Repeats

`git grep -in -E` on origin/main (2bb4cdea5) over the whole docs/ tree for Pseudoparamenexenus, beiliuensis, d17090637, Prolucanus, beipiaoensis, insects13030272, Pseudoeupolyphaga, menglianensis, zookeys.1261.168015, Cnipsomorpha, yuxiensis, zookeys.1176.75490, Neoparamenexenus, Prosceles: no hits. A looser pass (duani, yunnanensis, balteatus, 168015, 75490) hit only other species (Tomicus, Pinus, Nyssa, Paris yunnanensis; Episyrphus balteatus). Unmerged branches: see the branch note at the end.

## Per line

### Line 9, Pseudoparamenexenus beiliuensis, compound eyes prominent (female holotype)

Female Head: "Occiput flat." / "Compound eyes prominent, strongly hemispherical projecting." / "Ocelli lacking." **Quote MATCH**, whole telegraphic sentence, 6 words. Holotype line "Tpye material. Holotype: ♀, China, Guangxi, Darongshan, Beiliu, alt. 930 m, 5 August 2022, coll. Shan Li and Qianwen Zhang." (no paratypes; no depository printed); "Male. Unknown." Diagnosis and Discussion have no eye text. The five Hainan females (1 + 2 + 2, May 2024) are printed under the heading of Pseudoparamenexenus yangi after its Figure 1 caption (tool summary from layout), so the conditions' "their species is unclear" understates the placement; harmless. The line fails on the name alone (above).

**Line 9 DROP (synonym; unfixable).**

### Line 10, Prolucanus beipiaoensis, eyes large, nearly entire (fossil)

Description, Head: "Preocular angle rounded, preocular margin short." / "Eyes large, nearly entire, slightly divided by ocular canthus." / next sentence begins "Antenna geniculate with 10 antennomeres, ...". **Quote MATCH**, 9 words. Material: "Holotype: NIGP176633, probably female, a well-preserved and almost complete body collected from the Yixian Formation near the Huangbanjigou Village of Beipiao City, Liaoning Province, and is now housed in the Nanjing Institute of Geology and Palaeontology, Chinese Academy of Sciences, Nanjing, China." Part and counterpart (Figure 2 caption); "Early Cretaceous, circa 125 MYA"; Material and Methods "The present specimen originates from the fossiliferous yellowish tuffs of the Lower Cretaceous Yixian Formation". Formation and age are in the conditions; the Discussion caution and Conclusions "may be a plesiomorphic feature" are carried.

Faults (one record error, fixable): (a) **preservation not stated.** The task requires the fossil's preservation; the conditions give only "part and counterpart", and the note says preservation "is not stated", though the page prints "a well-preserved and almost complete body" in yellowish tuffs, "Ventral side clearly preserved." and a head figure "(A) Head ventral and prosternum."; the view from which the eyes were described is not stated. (b) **Diagnosis misattributed.** The species Diagnosis reads "Diagnosis. As for the genus, vide supra."; the eye phrase is in the genus Diagnosis (feature 2), not a species Diagnosis.

**Line 10 FIXABLE.**

### Line 11, Pseudoeupolyphaga duani, eyes and ocelli well-developed (male holotype)

Male, Head: "Head: Sub-rounded, nearly completely hidden under pronotum." / "Eyes and ocelli well-developed." / "Interocular space narrower than the distance between ocelli, the latter narrower than the distance between antennal sockets (Fig. 2G)." **Quote MATCH**, 4 words. Holotype "China • male (ZAFU); Yunnan Province, Pu'er City, Jinggu County; 1 Jun. 2025; Quan-Fu Duan leg; ZAFU-IC-200001."; paratypes "1 female & 2 nymphs (ZAFU); Luo-Jiang Liu leg; ... ZAFU-IC-200002 to 200004" and "1 female & 2 nymphs (SWU); Luo-Jiang Liu leg; ... SWU-B-CC-010074 to 010076."; Table 1 "Jinggu County, Pu'er City, Yunnan; 1 Jun. 25; Luo-Jiang Liu". All as in the conditions. Diagnosis and Remarks have no eye text.

**Line 11 MATCH.**

### Line 12, Pseudoeupolyphaga duani, ocelli degraded to two spots (female paratype)

Heading "Female paratype (mm)."; Body: "... Anterior whitish margin absent, bearing symmetrical black stripe medially (Fig. 2F)." / "Ocelli degraded to two spots." / "Interocular space almost equal to the distance between antennal sockets, both wider than the distance between ocelli." **Quote MATCH**, 5 words. Different sentence and different sex from line 11 (male: ocelli well-developed, interocular space narrower than ocelli distance); the conditions name the female paratype and the male contrast, and the eye field says ocelli. No double statement. The note "compound eyes of the female are not described" is right for morphology; the female Coloration prints "Vertex, eyes, space between ocelli and post-clypeus black." (optional fix).

**Line 12 MATCH.**

### Line 13, Pseudoeupolyphaga menglianensis, eyes and ocelli well-developed (male holotype)

Male, Head: "Sub-rounded, almost entirely hidden under pronotum." / "Eyes and ocelli well-developed." / "Ocelli ridge indistinct, bearing a row of slender setae along the upper edge." **Quote MATCH**, 4 words. Holotype "China • male (ZAFU); Yunnan Province, Pu'er City, Menglian County, Nayun Town, Mengwai Village; 6 May, 2025;" Zhong-Hong Luo leg; ZAFU-IC-200005; paratypes "1 female (pre-adult) & 4 nymphs (ZAFU)" and "1 male & 2 nymphs (SWU)"; Table 1 "6 Mar. 2025"; pre-adult female "Ocelli degraded to two spots." All as in the conditions.

**Line 13 MATCH.**

### Line 14, Cnipsomorpha yunnanensis, compound eyes spherical and protruding (female holotype)

Female Head: "Head oval, with irregular granules, without distinct tubercles." / "Compound eyes are spherical and protruding." / "There is one pair of spines on the vertex of the head, the apex leans forward." **Quote MATCH**, 6 words. Type material: "One Female. Fenshuiling Nature Reserve, Jinping County, China, alt. 2100 m, 18–19 May 2015, leg. Bin Yan." "Specimen code: YNJP150517001. Specimen used for DNA extraction."; no paratypes; "Male and eggs unknown." Right. The closing "sister species" in the conditions was not checked against the tree; optional rewording below.

**Line 14 MATCH.**

### Line 15, Cnipsomorpha yuxiensis, compound eyes large, spherical, protruding (female holotype)

Female Head: "Head nearly spherical, with sparse irregular granules." / "Compound eyes large, spherical, and protruding." / "Vertex of head with one pair of spines, apex pointed." **Quote MATCH**, 6 words. Holotype "One female. Ailaoshan Primeval Forest, Gasha, Xinping, Yuxi, Yunnan, China, alt. 2400 m. 8 May 2015." "Collectors: Bin Yan, Yunfei Wu. Specimen code: YNYX150508001-1."; allotype "One male. Same data as holotype. Specimen code: YNYX150508001-2." "Specimen used for DNA extraction."; paratype "One female. Jinshanyakou, Ailaoshan, Xinping, Yuxi, Yunnan, China. alt. 2377–2413 m, 17 May 2015, leg. Bin Yan." "Specimen code: YNYX150507002." (code as printed). All as in the conditions; the female description covers holotype and paratype, and the eye field says female holotype, which is the type of the female description.

**Line 15 MATCH.**

### Line 16, Cnipsomorpha yuxiensis, compound eyes spherical and protruding (male allotype)

Male Head: "Vertex of head with one pair of spines." / "Compound eyes spherical and protruding." / "Occiput without swelling, with four pairs of spine-like tubercles, two close to the middle, ...". **Quote MATCH**, 5 words. Male described under "Male (Fig. 2A, C, F, G) more slender than female, granulated."; the only male is the allotype; no male paratype. Lines 15 and 16 are different sentences for different sexes; the female says "large", the male does not, and both conditions say so. No double statement.

**Line 16 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 9 | Pseudoparamenexenus beiliuensis, eyes prominent | DROP | n/a | name is a subjective synonym of Prosceles (now Neoparamenexenus) balteatus in Phasmida Species File (Ho 2025) |
| 10 | Prolucanus beipiaoensis, eyes nearly entire (fossil) | FIXABLE | conditions, note | preservation printed but called unstated; eye phrase is in the genus Diagnosis, species Diagnosis is "As for the genus" |
| 11 | Pseudoeupolyphaga duani, male | MATCH | | |
| 12 | Pseudoeupolyphaga duani, female paratype ocelli | MATCH | | different sentence and sex from line 11 |
| 13 | Pseudoeupolyphaga menglianensis, male | MATCH | | |
| 14 | Cnipsomorpha yunnanensis, female | MATCH | | |
| 15 | Cnipsomorpha yuxiensis, female | MATCH | | |
| 16 | Cnipsomorpha yuxiensis, male | MATCH | | different sentence and sex from line 15 |

Errors: 2 of 8 records (25%); 1 fixable (line 10), 1 unfixable (line 9, drop), 0 held out for an unopened page. Repeats on main: none. Verdict for lines 9 to 16 of desk-d315: **ACCEPT AFTER REPLACEMENT** (lines 11 to 16 as filed; line 10 with the replacements below; line 9 dropped).

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Drop: line 9 (Pseudoparamenexenus beiliuensis; synonym).

Line 10:
- `conditions`: "Holotype NIGP176633 only (part and counterpart; sex given as probably female; no paratypes), Yixian Formation" -> "Holotype NIGP176633 only ('a well-preserved and almost complete body', part and counterpart, from the fossiliferous yellowish tuffs; 'Ventral side clearly preserved.'; the only head figure is 'Head ventral and prosternum' and the view from which the eyes were described is not stated; sex given as probably female; no paratypes), Lower Cretaceous Yixian Formation"
- `conditions`: "The Diagnosis repeats 'eyes large" -> "The species Diagnosis reads 'As for the genus, vide supra.'; the genus Diagnosis repeats 'eyes large"
- `note`: "Preservation as compression or impression is not stated." -> "The terms compression and impression are not used; the specimen is 'a well-preserved and almost complete body' in yellowish tuff (conditions)."

Optional, not counted:
- Line 12 `conditions`: "The sentence concerns the ocelli only; compound eyes of the female are not described." -> "The sentence concerns the ocelli only; compound-eye form of the female is not described (the female Coloration says only 'Vertex, eyes, space between ocelli and post-clypeus black.')."
- Line 14 `conditions`: "The sister species C. yuxiensis has large, spherical, protruding eyes." -> "The other species described here, C. yuxiensis, has 'Compound eyes large, spherical, and protruding.' (female)."
