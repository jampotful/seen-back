# audit-425: desk-d316, evidence lines 7-12

Audited 1 November 2026 from the desk-d316 files present untracked in the worktree (docs/tracks/progress/desk-d316.md and docs/views/evidence/desk-d316.jsonl, 12 lines; neither committed here, neither edited). This audit covers file lines 7 to 12 only; another auditor takes lines 1 to 6. HEAD equals origin/main (af3bdffb4). `python3 -I tools/senses/check.py | grep d316`: "docs/views/evidence/desk-d316.jsonl: 12 records, 0 problems". Quote lengths (`len(q.split())`) for lines 7 to 12: 9, 23, 23, 23, 13, 14, all within 40.

Sources opened (WebFetch, every URL from a WebSearch result): www.mdpi.com/2075-4450/16/9/883 (two passes), zookeys.pensoft.net/article_preview.php?id=143063 (two passes), zookeys.pensoft.net/article/143063/download/xml/ (two passes), zookeys.pensoft.net/article_preview.php?id=181827 (two passes), hopperwiki.org/index.php/Diestramima, orthoptera.speciesfile.org/otus/1092293 and /otus/838346/overview. Crossref single-DOI lookups api.crossref.org/v1/works/: 10.3390/insects16090883 read on the first call; 10.3897/zookeys.1275.181827 rate-limited, read on the retry; 10.3897/zookeys.1231.143063 rate-limited twice and not worked around, so the bibliographic check for lines 8 to 10 rests on the publisher citation line printed on the page. PMC, GBIF, bionames, plazi, zenodo, library catalogue (kab.ac.ug) and optimap results were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 5 WebSearches.

## Bibliographic and licence

- Line 7 (Wang, Zhu, Yu, Liu, Wu, Huang 2025). Page byline and Crossref agree in order (Qingyun Wang, Yi Zhu, Yefei Yu, Liwei Liu, Hong Wu, Junhao Huang); "Insects 2025, 16(9), 883"; title printed in two pieces "A Review of the Newly Recorded Genus Proceroplatus Edwards, 1925 (Diptera: Keroplatidae) in China with Two New Species," / "and Its Characterization and Phylogenetic Implication of Mitogenomes", identical to the record. Issued 2025-08-25. Page has no licence sentence, metadata CC BY 3.0; Crossref CC BY 4.0 vor: accepted by ruling. Right.
- Lines 8 to 10 (Zhu, Xu, Yang, Shi 2025). Page citation line "Citation: Zhu Q, Xu H, Yang R, Shi F (2025) Notes on the genus Diestramima Storozhenko, 1990" ... "with description of three new species from China. ZooKeys 1231: 119-132."; the page title prints "(Orthoptera, Rhaphidophoridae)" between the two pieces (preview page, second pass). Record identical. Licence sentence "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0)," printed. Crossref not readable here (rate limit), so the record's Crossref CC BY 4.0 vor claim is unconfirmed by me; the page licence suffices. Right.
- Lines 11, 12 (Feng et al. 2026). The preview page DOES print a citation line: "Feng X-L, Zhao Z-X, Xiao J, Song X-H, Huang X-D, Chen H-L (2026)" / "Description of two new species of *Rhaphidophora* and *Diestramima* (Orthoptera, Rhaphidophoridae) from China." / "ZooKeys 1275: 299-309." Byline "Xue-Li Feng", "Zheng-Xue Zhao", "Jie Xiao", "Xiao-Hui Song", "Xiu-Dong Huang", "Hao-Lin Chen"; Crossref identical in order, pages 299-309, issued 2026-03-31, CC BY 4.0 vor. Title, volume, pages and year right; printed year 2026. **Fault (fixable, both lines):** the record's authors "Feng XL, Zhao ZX, Xiao J, Song XH, Huang XD, Chen HL" drop the printed hyphens in the initials (main keeps printed hyphenated initials, e.g. "Li F-W", "Nilsson D-E"; audit 397 counted a dropped/added name hyphen against the page byline), and the note's statement that the article "prints no citation line, so the author initials are assembled from the metadata" is wrong for the page. Licence sentence printed (CC BY 4.0). 

Bibliographic faults: lines 11 and 12; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

- Proceroplatus biemarginatus: order and family from the title "(Diptera: Keroplatidae)"; "Insecta" appears only in reference 3's title, so class blank is right. New species in a peer-reviewed paper. Right.
- Diestramima ligula, D. longzhouensis, D. napoensis: XML kwd-group "Taxon classification" Animalia, Orthoptera, Rhaphidophoridae for all three, as the note says; no class printed. Orthoptera Species File: D. longzhouensis Zhu & Shi, 2025 valid (otus/1092293, parent Diestramima, Rhaphidophoridae, Orthoptera); hopperwiki's Diestramima list (pointing to OSF) includes ligula, longzhouensis and napoensis. Right.
- Rhaphidophora jiaozishanensis and Diestramima (Baculitettix) phytophylacis: Taxon classification on the page "Orthoptera Oliver, 1789" / "Rhaphidophoridae Walker, 1869"; no class. Neither name was found in OSF (a search returned other Diestramima pages only; hopperwiki has no phytophylacis); both were described on 31 March 2026 and are not yet indexed, which I do not count. Subgenus Baculitettix Gorochov & Storozhenko, 2019 printed. Right.

## Repeats

`git grep -il -E` on origin/main (af3bdffb4) over the whole docs/ tree (evidence, audit/corrected, audit/ALL, sheets, searched, tracks) for biemarginatus, Proceroplatus, Diestramima, jiaozishan, phytophylac, insects16090883, 143063, 181827: one hit, docs/views/no-view-us-fl-alachua.csv line 36, a numeric id "8181827" on Tigrosa georgicola (spurious). The evidence files of all 316 origin/research/desk-d* branches (docs/views/evidence/desk-dN.jsonl via one `git cat-file --batch`) grepped for the same species and the three DOIs: hits only in desk-d316 itself. No repeats.

## Per line

### Line 7, Proceroplatus biemarginatus, compound eye medially emarginated, densely setose

Male Head: "Compound eye with emargination medially, covered with dense setae." Preceded by "Two ocelli, placed on raised dark brown ocellar tubercle." and followed by "Clypeus inverted triangular, bearing countable dark setae on surface." **Quote MATCH**, whole sentence, 9 words. Value says no more than the quote. Type material: Holotype "Male." "CHINA: Guangdong, Mt. Nanling (24.93° N, 113.00° E), 1210 m, 06.VII.2020, coll. Lei Qi, slide no. NL-9-48."; Paratype "1 male, the same data as holotype (NL-9-52)." As in conditions. No female described (tool summary); Diagnosis has no eye wording; no Remarks; the key has no eye couplet. P. dapanshanus: "Compound eye with slight invagination medially, covered with abundant pubescence." and three ocelli, so the conditions' contrast is right.

Not counted: key couplet 3 prints the ocellus states the other way round ("Two ocelli; ... P. dapanshanus sp. n." / "Three ocelli; ... P. biemarginatus sp. n."), contradicting both descriptions. Ocelli are not the filed value; an optional note is given below.

**Line 7 MATCH.**

### Line 8, Diestramima ligula, eyes ovoid, protruding forwards

Male Head, read on the preview page in two pieces: "Eyes ovoid, protruding forwards; median ocellus oval, located between antennal sockets, lateral ocelli nearly" / "circular, situated on lateral surface of basal rostral tubercles." Preceded by "Fastigium verticis with 2 conical tubercles, apices separated, obtusely rounded, pointing forwards." and followed by "Apical segment of maxillary palp obviously longer than subapical one, apex truncated." The joined text equals the printed sentence; one sentence, one section, no boundary crossed. **Quote MATCH**, 23 words. Material: Holotype "China • ♂, Yunnan Province, Wenshan Zhuang and Miao Autonomous Prefecture, Maguan County, 22.8576°N, 104.0042°E," / "alt. 1790 m, 19.VI.2024, Hao Xu leg."; Paratypes "1♂1♀, same data as for holotype." No habitat stated; "cave" occurs only in a reference title. Female: "Appearance is similar to male." Diagnosis (five sentences) has no eye wording. As in conditions.

**Line 8 MATCH.**

### Line 9, Diestramima longzhouensis, eyes ovoid, protruding forwards

XML: "Eyes ovoid, protruding forwards; median ocellus oval, located between antennal sockets," / "lateral ocelli nearly circular, situated on lateral surface of basal rostral tubercles." Next: "Apical segment of maxillary palp obviously longer than subapical one, apex inflated, globular." **Quote MATCH**, 23 words. Holotype "China • ♂, Guangxi Zhuang Autonomous Region, Longzhou County, Zhubu Town, 16.VII.2021, Meng An leg." (no coordinates); paratype 1♀ Nonggang, 22.4649°N, 106.9591°E, 260 m, 16 June 2024, Hao Xu (tool summary); other material 1♂ Dahua County, Yalong Town, Hongri Village, 700 m, 20 July 2024, Yueting Duan (tool summary). Female similar to male; Diagnosis on tergite and paraproct only. As in conditions.

Not counted: the conditions say the next sentence "differs"; it differs from D. ligula's ("apex truncated") but is identical in D. longzhouensis and D. napoensis ("apex inflated, globular"). Optional fix below.

**Line 9 MATCH.**

### Line 10, Diestramima napoensis, eyes ovoid, protruding forwards

XML: same two pieces and the same next sentence as line 9. **Quote MATCH**, 23 words. Holotype ♂ Napo County, Defu village, 23.2943°N, 105.8023°E, 1330 m, 13 August 2024, Hao Xu; paratypes four males and four females, same village, 11-14 August 2024 (tool summary). Female "Appearance is similar to male."; Diagnosis on tergite and paraproct. Type data right.

Not counted: other material (seven males and two females from Defu village; five males and six females from Baisheng Town, 1310 m, 15 August 2024; tool summary) is not in conditions, and the page has a habitat photograph, Figure 5 "Habitats of Diestramima napoensis Zhu & Shi, sp. nov. Photograph by Qianle Lu." The conditions' "does not describe the collecting habitat" is true of the text (the image was not read), and the Introduction's genus sentence ("These insects prefer dark, moist habitats and are typically nocturnal, active at night," / "but hiding under leaves or loose bark during the day.") is genus-level. Optional fixes below.

**Line 10 MATCH.**

### Line 11, Rhaphidophora jiaozishanensis, eyes reniform

Male Head, sentence 3 of the paragraph: "Eyes reniform, near upper portion of outer margin of antennal sockets (Fig. 1D)." **Quote MATCH**, whole sentence, 13 words. Holotype "China • 1 ♂; Guizhou Province, Anshun City, Xixiu District, Jiaozishan Town; 24 Aug. 2025; Xueli Feng & Zhengxue Zhao leg.; ASU ZooR20250802."; Paratype "China • 1 ♀; same data as holotype; ASU ZooR202508021." Sampling "in forested habitats by turning over fallen branches and leaf litter," "followed by manual capture of the specimens." Female "General appearance similar to that of male (Fig. 2A–C)," with no eye sentence; Diagnosis (epiproct, colour, size, tibial spines) has no eye wording; no Remarks.

Faults (one record error, fixable): (a) authors not as printed and the note's "no citation line" claim (see Bibliographic). (b) **Conditions misstate the page:** "The male ocellus sentence is longer than the quote limit and is not filed." The only ocellus sentence is "Lateral ocelli oval, occupying approximately three-quarters of lateral margins of entire tubercles" / "and situated at lateral base (Fig. 1D).", 18 words.

**Line 11 FIXABLE.**

### Line 12, Diestramima (Baculitettix) phytophylacis, eyes reniform

Male Head: "Eyes reniform, close to upper part of outer margin of antennal sockets (Fig. 4D)." **Quote MATCH**, whole sentence, 14 words. Holotype 1♂, Jiaozishan Town, 24 Aug. 2025, Xueli Feng & Zhengxue Zhao, ASU ZooD20250812; paratypes 1♂ (ZooD202508121) and 10♀ (ZooD202508122 to ZooD2025081211) with the same data (tool summary): as in conditions. Same sampling sentence (forest litter). Female "General appearance similar to males (Fig. 5A–C)." with no eye sentence; Diagnosis on the posteromedian process versus D. (B.) beybienkoi; no Remarks; etymology mentions no habitat.

Faults (one record error, fixable): (a) authors and note as line 11. (b) **Conditions misstate the page:** the ocellus sentence "Lateral ocelli oval, occupying approximately 3/4 of lateral margins of entire tubercles, situated at lateral base;" / "median ocellus located between antennal sockets (Fig. 4D)." is 22 words, within the limit.

**Line 12 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 7 | Proceroplatus biemarginatus, eye emarginate, setose | MATCH | | whole 9-word sentence; holotype and paratype males right |
| 8 | Diestramima ligula, eyes ovoid, protruding | MATCH | | joined text equals the printed sentence |
| 9 | Diestramima longzhouensis, eyes ovoid, protruding | MATCH | | same sentence; type and other material right |
| 10 | Diestramima napoensis, eyes ovoid, protruding | MATCH | | type material right; Fig. 5 habitat photo and non-type material optional |
| 11 | Rhaphidophora jiaozishanensis, eyes reniform | FIXABLE | authors, note, conditions | printed initials hyphenated, citation line exists; ocellus sentence is 18 words, not over the limit |
| 12 | Diestramima phytophylacis, eyes reniform | FIXABLE | authors, note, conditions | as line 11; ocellus sentence 22 words |

Errors: 2 of 6 records (33%); 2 fixable (lines 11, 12), 0 held out, 0 unfixable; no line to drop. Repeats: none. Verdict for desk-d316 lines 7 to 12: **ACCEPT AFTER REPLACEMENT** (lines 7 to 10 as filed; lines 11 and 12 with the replacements below, or dropped if they are not applied).

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 11:
- `source.authors`: "Feng XL, Zhao ZX, Xiao J, Song XH, Huang XD, Chen HL" -> "Feng X-L, Zhao Z-X, Xiao J, Song X-H, Huang X-D, Chen H-L"
- `note`: "The article XML prints no citation line, so the author initials are assembled from the metadata; year 2026 is the Crossref issue date (2026-03-31)." -> "Authors, year (2026), title and ZooKeys 1275: 299-309 as printed in the page citation line; Crossref issued 2026-03-31."
- `conditions`: "The male ocellus sentence is longer than the quote limit and is not filed." -> "The male ocellus sentence ('Lateral ocelli oval, occupying approximately three-quarters of lateral margins of entire tubercles and situated at lateral base (Fig. 1D).') is not filed; it concerns ocelli, not the compound eye."

Line 12:
- `source.authors`: "Feng XL, Zhao ZX, Xiao J, Song XH, Huang XD, Chen HL" -> "Feng X-L, Zhao Z-X, Xiao J, Song X-H, Huang X-D, Chen H-L"
- `note`: "The article XML prints no citation line, so the author initials are assembled from the metadata; year 2026 is the Crossref issue date (2026-03-31)." -> "Authors, year (2026), title and ZooKeys 1275: 299-309 as printed in the page citation line; Crossref issued 2026-03-31."
- `conditions`: "The male ocellus sentence is longer than the quote limit and is not filed." -> "The male ocellus sentence ('Lateral ocelli oval, occupying approximately 3/4 of lateral margins of entire tubercles, situated at lateral base; median ocellus located between antennal sockets (Fig. 4D).') is not filed; it concerns ocelli, not the compound eye."

Optional, not counted:
- Line 7 `conditions`: "P. dapanshanus has three)." -> "P. dapanshanus has three). The key (couplet 3) prints the ocellus states the other way round, contradicting both descriptions."
- Line 9 `conditions`: "The same eye sentence is printed for D. ligula, D. longzhouensis and D. napoensis; the next sentence (maxillary palp apex) differs." -> "The same eye sentence is printed for D. ligula, D. longzhouensis and D. napoensis; the next sentence (maxillary palp apex) reads 'apex inflated, globular' here and in D. napoensis and 'apex truncated' in D. ligula."
- Line 10 `conditions`: "The same eye sentence is printed for D. ligula, D. longzhouensis and D. napoensis; the next sentence (maxillary palp apex) differs." -> "The same eye sentence is printed for D. ligula, D. longzhouensis and D. napoensis; the next sentence (maxillary palp apex) reads 'apex inflated, globular' here and in D. longzhouensis and 'apex truncated' in D. ligula."
- Line 10 `conditions`: "The paper does not describe the collecting habitat of the types, so cave or surface status is not stated." -> "The text does not describe the collecting habitat of the types, so cave or surface status is not stated; Figure 5 is a photograph captioned 'Habitats of Diestramima napoensis Zhu & Shi, sp. nov.' (image not read)."
- Line 10 `conditions`: "11–14 August 2024." -> "11–14 August 2024; other material seven males and two females from Defu village and five males and six females from Baisheng Town, Napo County, 1310 m, 15 August 2024."
