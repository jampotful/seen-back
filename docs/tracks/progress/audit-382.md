# audit-382: desk-d292, evidence lines 1 to 8

Audited 1 November 2026 from the desk-d292 files present untracked in the worktree (docs/tracks/progress/desk-d292.md and docs/views/evidence/desk-d292.jsonl, 15 lines; neither committed here, neither edited). Lines 9 to 15 belong to audit 383. Worktree HEAD and origin/main 14e50fbb (Merge desk d290 (7 records) after audit 379). `python3 -I tools/senses/check.py | grep 'd292\.'`: "docs/views/evidence/desk-d292.jsonl: 15 records, 0 problems". Quote lengths (`len(q.split())`) for lines 1 to 8: 14, 13, 3, 2, 2, 7, 6, 3, all within 40; no quote contains a non-ASCII character. Line numbers are the file's (1-based).

Sources opened (WebFetch): api.crossref.org/v1/works/10.3897/zookeys.692.11677; api.crossref.org/v1/works/10.3897/zookeys.734.15061 (client_error twice, so the Crossref record was read through a list query, api.crossref.org/works?filter=prefix:10.3897,from-pub-date:2018-01-01,until-pub-date:2018-12-31&query=Seven new species of Pinelema from Vietnam, which returned DOI 10.3897/zookeys.734.15061); zookeys.pensoft.net/article/15061/download/xml/ (truncated at the start of the P. zhenzhuang treatment); zookeys.pensoft.net/article_preview.php?id=15061; zookeys.pensoft.net/article_preview.php?id=11677. All page URLs were returned by a WebSearch first. GBIF, core.ac.uk, omicsdi, optimap, BHL, Plazi, bionames, zoobank and wsc.nmbe.ch hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 2 WebSearches.

Fetch-oddity check (the unit reported three article ids returning a previous page's text): both pages used here printed their own article's title and byline in the fetch, and the treatments read on them are the species of that article (ZooKeys 734: damtaoensis, nuocnutensis, laensis, pacchanensis, spirulata, xiezi, zhenzhuang; ZooKeys 692: cunfengensis, podiensis, qingfengensis). The ids 24432, 38967 and 38653 the unit named are not cited in lines 1 to 8.

## Bibliographic and licence

- Lines 1 to 5 (Zhao et al. 2018). Crossref (list query): Huifeng Zhao, Pham Dinh-Sac, Yang Song, Thi-Duyen Do, Shuqiang Li; ZooKeys 734, 13-42, no issue; issued 2018-02-05; CC BY 4.0 vor. Page title verbatim "Seven new species of Pinelema from Vietnam (Araneae, Telemidae)", byline in the same order, "ZooKeys 734: 13–42". Licence verbatim "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0),". Record "Zhao H, Pham D-S, Song Y, Do T-D, Li S", 2018, matches. Accepted.
- Lines 6 to 8 (Song et al. 2017). Crossref: Yang Song, Huifeng Zhao, Yufa Luo, Shuqiang Li; title identical; ZooKeys 692, 83-101, no issue; issued 2017-08-21; CC BY 4.0 vor. Page citation verbatim "Song Y, Zhao H, Luo Y, Li S (2017)" and "ZooKeys 692: 83-101."; licence sentence verbatim (CC BY 4.0). Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

No checklist reached; all eight species are described as new in the cited papers ("sp. n." headings; ZooKeys 692 treatments as "Zhao & Li, sp. n."), so the names rest on the original descriptions, as the desk says. Family Telemidae and order Araneae from both titles. Name faults 0.

## Duplicates

git grep on origin/main (14e50fbb) across the whole docs/ tree for Pinelema, each of the eight epithets, zookeys.734.15061, zookeys.692.11677, 15061 and 11677: no Pinelema or epithet hits except "laensis" as a substring of other names (N. arolaensis and Heteromysoides songkhlaensis in desk-d290.md, Neobuxbaumia mezcalaensis in oa-10.jsonl, and gaps files); "15061" only inside unrelated numbers (audit-184.md accession 20150613, a transmittance value in oa-1.jsonl, a foods DOI in searched/desk-c12.jsonl). Remote research/desk-* and research/audit-* branches grepped under docs/ for Pinelema and both DOIs (one git grep over all 675 refs other than research/desk-d292): no hits.

Duplicates 0.

## Per-record findings

### Line 1, Pinelema damtaoensis, eyes_count 6

Male Description verbatim "Six eyes encircled by black rings, well-developed, clypeus 0.08 long, ocular quadrangle 0.18 wide." **Quote MATCH**. Female Description verbatim "Six eyes, well-developed, clypeus 0.14 long, ocular quadrangle 0.21 wide.", as the conditions quote. Type material verbatim "Paratypes 3♂ and 5♀, same data as holotype." Genus comment verbatim "Six eyes are normally developed, vestigial, or in some species are completely absent."

Error (conditions): the record ends "cave spider", but the holotype line reads verbatim "Vietnam: Vinh Phuc Province: Dam Tao National Park: N21°27.62', E105°38.91', 999 m, leaf litter, 1.XI.2012, H.F. Zhao & Z.G. Chen leg." and the paratypes share its data. This is the one species of the seven in ZooKeys 734 collected from leaf litter rather than a named cave, so "cave spider" states a habitat the page contradicts. Fixable; replacement below.

**Line 1 ERROR (fixable).**

### Line 2, Pinelema laensis, eyes_count 6

Male Description verbatim "Six eyes encircled by black rings, clypeus 0.12 long, ocular quadrangle 0.19 wide." **Quote MATCH**. Female sentence verbatim "Six eyes encircled by black rings, clypeus 0.09 long, ocular quadrangle 0.18 wide.", as quoted in conditions. Holotype verbatim "Vietnam: Phu Tho Province: Xuan Son National Park: La Cave,"; paratypes "1♂ and 4♀, same data as holotype." Conditions match. Diagnosis separates it by "having distinct eyes".

**Line 2 MATCH.**

### Line 3, Pinelema nuocnutensis, eyes_count 4 (vestigial)

Male Description verbatim "Four vestigial eyes." **Quote MATCH**. Female verbatim "Eyes reduced to four vestigial spots."; paratypes "2♂ and 5♀, same data as holotype."; holotype from "Nuoc Nut Cave". Diagnosis "can be distinguished by the vestigial eyes". The value and eye key ("eyes (vestigial)") say no more than the quote. Read on the XML copy only (the article's own XML; title and byline matched).

**Line 3 MATCH.**

### Line 4, Pinelema pacchanensis, eye_type none

Male Description "Eyes absent." **Quote MATCH**. The female Description has no eye sentence (tool summary). Holotype from "Pac Chan Cave"; paratypes "2♂ and 5♀, same data as holotype." The nuocnutensis Diagnosis contrasts "(eyes completely reduced in" P. pacchanensis, consistent with the value. Male-only stated; attribution shown in the note.

**Line 4 MATCH.**

### Line 5, Pinelema zhenzhuang, eye_type none

Read on article_preview.php?id=15061 (the XML stops at this treatment). Male Description "Eyes absent." **Quote MATCH**. Holotype verbatim "Vietnam: Quang Binh Province: Phong Nha-Ke Bang National Park: Tien Duong Cave, N17°31.17', E106°13.38', 133 m, 18.V.2016, Z.G. Chen & Q.Y. Zhao leg."; paratypes "3♂ and 4♀, same data as holotype."; no eye sentence in the female Description or Diagnosis (tool summary). Conditions match.

**Line 5 MATCH.**

### Line 6, Pinelema cunfengensis, eyes_count 6

Male Description verbatim "Six eyes, all well-developed, ringed with black." **Quote MATCH**. Female Description has no eye sentence; it says "Coloration and pattern as in male." (tool summary for the absence). Holotype from "Cunfeng Cave"; paratypes "3♂ and 5♀, same data as holotype." Diagnosis "the well-developed eyes and greenish abdomen". Conditions match.

**Line 6 MATCH.**

### Line 7, Pinelema podiensis, eye_type reduced (white spots)

Male Description verbatim "Reduced eyes appear as white spots." **Quote MATCH**. Holotype from "Podi Cave"; paratypes "1♂ and 4♀, same data as holotype."; no female eye sentence (tool summary). The Diagnosis says "the strongly reduced eyes and pale yellow abdomen" and the cunfengensis Diagnosis "(eyes reduced to white spots, abdomen pale yellow in P. podiensis sp. n.)", consistent with the value; no count anywhere, as the note says.

Uncounted: the note could carry the Diagnosis wording "strongly reduced". Replacement below.

**Line 7 MATCH.**

### Line 8, Pinelema qingfengensis, eye_type entirely reduced

Male Description "Eyes entirely reduced." **Quote MATCH**. Holotype from "Qingfeng Cave"; paratypes "1♂ and 6♀, same data as holotype."; no female eye sentence (tool summary). Diagnosis "the completely reduced eyes and yellow abdomen". Value keeps the quote's wording.

**Line 8 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Pinelema damtaoensis, 6 | ERROR (fixable) | conditions | quote MATCH (14); type series from leaf litter, "cave spider" contradicts the page |
| 2 | Pinelema laensis, 6 | MATCH | none | quote MATCH (13); La Cave; female sentence quoted |
| 3 | Pinelema nuocnutensis, 4 vestigial | MATCH | none | quote MATCH (3); female "four vestigial spots" quoted |
| 4 | Pinelema pacchanensis, none | MATCH | none | quote MATCH (2); male only, stated |
| 5 | Pinelema zhenzhuang, none | MATCH | none | quote MATCH (2); read on preview page; male only, stated |
| 6 | Pinelema cunfengensis, 6 | MATCH | none | quote MATCH (7); male only, stated |
| 7 | Pinelema podiensis, reduced (white spots) | MATCH | none | quote MATCH (6); Diagnosis wording fix uncounted |
| 8 | Pinelema qingfengensis, entirely reduced | MATCH | none | quote MATCH (3); male only, stated |

Errors 1 of 8 audited records (12.5%). By kind: quotes 0; value exceeding quote 0; sample composition 0; habitat statement 1; bibliographic 0; licence 0; names 0; filing convention 0; duplicates 0. Unfixable errors to hold out: none. Verdict: merge lines 1 to 8 with the line 1 replacement applied (the line 7 replacement is optional).

Unchecked: no checklist entry for any species; figures not viewed; the absence of female eye sentences (lines 4 to 8) rests on tool summaries.

## Replacement

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 1 (counted):
- `conditions`: "; cave spider" -> "; holotype and paratypes from leaf litter at 999 m in Dam Tao National Park, not from a cave"

Line 7 (uncounted):
- `note`: "The paper gives no count." -> "The paper gives no count; the Diagnosis calls the eyes \"strongly reduced\"."
