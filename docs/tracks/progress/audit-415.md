# audit-415: desk-d311, evidence file lines 43 to 50

Audited 1 November 2026 from the desk-d311 files present untracked in the worktree (docs/tracks/progress/desk-d311.md and docs/views/evidence/desk-d311.jsonl, 50 lines; neither committed here, neither edited). This audit covers file lines 43 to 50 only; six other auditors take lines 1 to 42. HEAD equals origin/main (095e055d8). `python3 -I tools/senses/check.py | grep d311`: "docs/views/evidence/desk-d311.jsonl: 50 records, 0 problems". Quote lengths (`len(q.split())`): 15, 15, 7, 7, 13, 7, 7, 7, all within 40.

The eight lines come from two papers, each read once and every line judged from that reading:
- Lines 43 and 44: Yin, Hlaváč, Li 2013, ZooKeys 275: 23-65, 10.3897/zookeys.275.4571.
- Lines 45 to 50: Jiang, Yin 2017, ZooKeys 694: 11-30, 10.3897/zookeys.694.13802.

Sources opened (WebFetch, every URL from a WebSearch result): zookeys.pensoft.net/article/13802/download/xml/ (publisher's own full-text XML, two passes), zookeys.pensoft.net/article/3726/download/xml/ (one pass; the tool's copy stopped inside the Pselaphodes hainanensis treatment, so it gave byline, licence and Introduction only), zookeys.pensoft.net/article_preview.php?id=3726 (two passes). Crossref single-DOI lookups api.crossref.org/v1/works/ for both DOIs, each read on the first call. Library catalogue records (utm.my, uv.mx, ufrj.br), optimap, bionames, BHL, omicsdi and DOAJ were not opened; no curl, proxy, PMC, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters. 2 WebSearches.

## Bibliographic and licence

- Lines 43 and 44 (ZooKeys 275). Byline "Zi-Wei Yin, Peter Hlaváč, Li-Zhen Li"; Crossref same order (Hlavac without the accent; the record keeps the printed háček, right). Title verbatim as printed and in Crossref. "ZooKeys 275: 23–65"; Crossref volume 275, pages 23-65, no issue; issued 2013-03-04; year 2013 right. Licence: XML prints "Creative Commons Attribution License 3.0 (CC-BY)"; Crossref CC BY 3.0 vor. Accepted.
- Lines 45 to 50 (ZooKeys 694). Byline "Ri-Xin Jiang, Zi-Wei Yin"; Crossref same order. Title verbatim. Crossref volume 694, pages 11-30, no issue; issued 2017-08-28; year 2017 right. Licence: XML prints "Creative Commons Attribution License (CC BY 4.0)"; Crossref CC BY 4.0 vor. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout. Both `url` fields (zookeys.pensoft.net/article/3726/ and /article/13802/) are the publisher's article pages.

## Names and higher taxa

Order and family as printed: ZooKeys 275 prints "(Coleoptera, Staphylinidae, Pselaphinae)" in the title and "Staphylinidae: Pselaphinae: Tyrini" in the Introduction; ZooKeys 694 prints the title "(Coleoptera, Staphylinidae, Pselaphinae)" and the treatment classification lines "Order: Coleoptera", "Family: Staphylinidae". No class is printed in either; class blank is right. The eight species are described as new in these papers (Pselaphodes tiantongensis and P. wrasei "Yin & Li, sp. n." in the ZooKeys 275 Abstract; the six Batrisodes as sp. n. in ZooKeys 694); the names are the original combinations. Not counted: the line 45 to 50 notes say "The page prints Order Coleoptera, Family Staphylinidae, Subfamily Pselaphinae"; the treatment classification lines carry Order and Family only, and Pselaphinae appears in the title and keywords (tool summary). The fields are right; optional fix below.

## Repeats

`git grep -il -E` on origin/main (095e055d8) over the whole docs/ tree for the eight epithets (tiantongensis, wrasei, "Batrisodes grossus", qiului, simianshanus, tianmuensis, xuhaoi, zethus) and both DOIs. Hits: docs/views/evidence/desk-d302.jsonl carries both DOIs, but for other species only (Dayao emeiensis from ZooKeys 275, Batrisodes zhouchaoi from ZooKeys 694), as the notes say; "zethus" hits are the wasp genus Zethus (gaps, queue, sweep-59, codex-findings), a different taxon. No filed species is on main under any trait. Unmerged origin/research/desk-d* and audit-* branches (all except desk-d311) were grepped over docs/views/evidence, docs/views/audit and docs/views/sheets for the eight binomials in one `git grep -il -E`: completed, no hits.

## Per line

### Line 43, Pselaphodes tiantongensis, about 35 facets per eye (male)

Male Description: "Male (Fig. 16B). Length 3.34–3.45." then "Head longer than wide, HL 0.75–0.77, HW 0.67–0.68; eyes each composed of about 35 facets." **Quote MATCH**, whole sentence beginning at its capital after the preceding full stop, en dashes as printed, 15 words, returned identically on two passes. Value keeps "about" and "each eye", and the sentence sits under the Male heading, so "of the male" is what the page says. Type material: "Holotype: ♂, labeled 'CHINA: Zhejiang, Ningbo City / Yinzhou District, Tiantong Shan", 600 m, "2009.iv.26, Ting Feng leg."; "Paratypes: 4 ♂♂, 2 ♀♀, same label data as holotype (SNUC)." The ranges (HL 0.75–0.77) show the male description covers the male series, consistent with "6 paratypes (4 males, 2 females, same locality)". Female: "Similar to male in general; BL 3.28–3.37, ..." then "Eyes each composed of about 30 facets." (standalone sentence), carried in conditions. No Diagnosis, Comments or Remarks sentence mentions eyes or facets (tool summary).

**Line 43 MATCH.**

### Line 44, Pselaphodes wrasei, about 45 facets per eye (male)

Male Description: "Male (Fig. 19A). Length 3.32." then "Head longer than wide, HL 0.75, HW 0.68; eyes each composed of about 45 facets." **Quote MATCH**, 15 words, two passes. Single values (no ranges) fit a single male, the holotype; conditions say "no paratype males". Type material: holotype "36 km ESE Zhongdian, 3500–3550 m", "23–24.VIII.2003 Wrase"; "4 ♀♀, same label data as holotype (pcMS); 1 ♀, same label data, except '24.VIII.2003, M. Schülke' (pcMS)." Conditions ("5 female paratypes from the Zhongdian area") are accurate, if less precise than the page. Female: "Eyes each composed of about 25 facets." standalone, carried. No Diagnosis or Comments eye sentence.

**Line 44 MATCH.**

### Line 45, Batrisodes grossus, about 50 facets per eye (male)

Male Description: the head sentence ends "... extending from level of eyes to head base, lacking median vertexal carina." then "Each eye composed of about 50 facets." then "Antennomeres II–X (Fig. 3A) moniliform, ...". **Quote MATCH**, whole telegraphic sentence (precedent audit-395/403), 7 words, two passes. Type material "(5 exs). Holotype: CHINA: ♂, labeled 'China: Guangxi, Jinxiu County (金秀县), Dayao Mountain (大瑶山), 16 km (十六公里), ... beech forest, rotten wood, colony of ant, 1100 m, 17.vii.2014, Zhong Peng leg.' (SNUC). Paratypes: CHINA: 4 ♀♀, same label data as the holotype (SNUC)." Biology: "All adults were collected from an Odontomachus colony in a tree hole (Fig. 12)." So the tree hole in the conditions is from the Biology section and right; the male count is the holotype alone, which the conditions imply ("male holotype ... and 4 female paratypes"). Female clause "each eye composed of about 40 facets;" inside the sentence beginning "Similar to male, antennomere III–V normal;", carried. No Diagnosis eye sentence; the paper has no Comments, Remarks or key.

**Line 45 MATCH.**

### Line 46, Batrisodes qiului, about 60 facets per eye (male)

"Each eye composed of about 60 facets." follows the head sentence ending "lateral longitudinal carinae unobvious, lacking median vertexal carina." **Quote MATCH**, 7 words. Holotype ♂ only: "Sichuan, Luzhou City, Gulin County (古蔺县), Honglong Lake (红龙湖)", 1620 m, 30.iv.2017, ant nest in rotten wood, Lu Qiu leg.; host Pheidole sp.; female unknown. Conditions right.

**Line 46 MATCH.**

### Line 47, Batrisodes simianshanus, about 60 facets per eye and one ocular spine (male)

"Each eye composed of about 60 facets and with one short ocular spine." follows the head sentence ending "lateral longitudinal carinae slight, extending from level of eyes to head base." **Quote MATCH**, 13 words; value says no more than the quote. Type material "(8 exs)": holotype ♂ "Sunzigou (笋子沟), ... 751 m, 06.iii.2016, ant nest under rock, XU Hao & QIU Jianyue leg."; "Paratypes: CHINA: 1 ♂, 3 ♀♀, same label data as the holotype (SNUC); 2 ♂♂, 1 ♀, labeled '... Motianling (摩天岭), ant nest under rock, ... 1220 m, 30.iv.2016 ...'". Conditions "7 paratypes (3 males, 4 females; 3 of them from Motianling)" right; host Aphaenogaster sp. Female clause "each eye composed of about 50 facets;" carried. The Diagnosis has "ocular canthi present" (tool summary); a different structure from the facet count, no contrasting count. Not counted.

**Line 47 MATCH.**

### Line 48, Batrisodes tianmuensis, about 55 facets per eye (male)

"Each eye composed of about 55 facets." after the head sentence. **Quote MATCH**, 7 words. Holotype ♂ only, "Zhejiang, Linan County, West Tianmushan", 13.iv.2017, 310 m, ant nest under rock; host Ectomomyrmex sp.; female unknown. Conditions right.

**Line 48 MATCH.**

### Line 49, Batrisodes xuhaoi, about 50 facets per eye (male)

"Each eye composed of about 50 facets." after the head sentence ending "lateral longitudinal carinae short and slight, extending from level of eyes to head base, lacking median vertexal carina." **Quote MATCH**, 7 words. Holotype ♂ "Gonggashan N. R. (贡嘎山自然保护区), Hongshitan (红石滩)", 2740 m, 24.vi.2016, ant nest under rock; three male and one female paratypes with the same label data; host Lasius sp. Female clause "each eye composed of about 40 facets;" in the sentence beginning "General habitus similar to male, antennomere XI lacking basal denticle;", carried. Conditions right.

**Line 49 MATCH.**

### Line 50, Batrisodes zethus, about 60 facets per eye (male)

"Each eye composed of about 60 facets." after the head sentence ending "lacking lateral longitudinal carinae and median vertexal carina." **Quote MATCH**, 7 words. Holotype ♂ only, "Hunan, Liuyang City, Daweishan National Forest Park", 1391 m, 03.vi.2017; no host ant ("This new species was collected from leaf litter."); female unknown. Conditions right.

**Line 50 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 43 | Pselaphodes tiantongensis, about 35 facets (male) | MATCH | | whole sentence with head dimensions; 4 male paratypes; female 30 carried |
| 44 | Pselaphodes wrasei, about 45 facets (male) | MATCH | | whole sentence; holotype the only male; female 25 carried |
| 45 | Batrisodes grossus, about 50 facets (male) | MATCH | | tree hole from Biology; female 40 carried |
| 46 | Batrisodes qiului, about 60 facets (male) | MATCH | | holotype only |
| 47 | Batrisodes simianshanus, about 60 facets + ocular spine (male) | MATCH | | paratype split 1+3 Sunzigou, 2+1 Motianling right |
| 48 | Batrisodes tianmuensis, about 55 facets (male) | MATCH | | holotype only |
| 49 | Batrisodes xuhaoi, about 50 facets (male) | MATCH | | 3 male, 1 female paratypes right |
| 50 | Batrisodes zethus, about 60 facets (male) | MATCH | | holotype only, leaf litter |

Errors: 0 of 8 records (0%); 0 fixable, 0 held out, 0 unfixable; no line to drop. Repeats: none. Verdict for desk-d311 lines 43 to 50: **ACCEPT** (all eight as filed), to be pooled with the six other audits of this unit.

## Replacement

No counted fault; no required replacement. Each old string below is copied from the desk file and occurs once in the line named.

Optional, not counted:
- Lines 45, 46, 47, 48, 49, 50 `note`: "The page prints Order Coleoptera, Family Staphylinidae, Subfamily Pselaphinae; class left blank." -> "The treatment prints Order: Coleoptera and Family: Staphylinidae; Pselaphinae is in the title; class left blank."
- Line 45 `conditions`: "from an Odontomachus sp. colony in a tree hole)" -> "from an Odontomachus sp. colony in a tree hole, per the Biology section; label 'beech forest, rotten wood, colony of ant')"
- Line 44 `conditions`: "and 5 female paratypes from the Zhongdian area;" -> "and 5 female paratypes (4 with the holotype's label data, 1 the same except 24 Aug. 2003, M. Schülke);"
