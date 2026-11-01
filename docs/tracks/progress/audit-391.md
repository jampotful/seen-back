# audit-391: desk-d299, evidence lines 1 to 6

Audited 1 November 2026 from the desk-d299 files present untracked in the worktree (docs/tracks/progress/desk-d299.md and docs/views/evidence/desk-d299.jsonl, 6 lines; neither committed here, neither edited; the jsonl is identical to origin/research/desk-d299). Line numbers are the file's (1-based). HEAD equals origin/main (dbb0cb96). `python3 -I tools/senses/check.py | grep 'd299\.'`: "docs/views/evidence/desk-d299.jsonl: 6 records, 0 problems". Quote lengths (`len(q.split())`): 19, 5, 7, 19, 17, 18, all within 40; the only non-ASCII characters are the en dash and the ellipsis in line 5.

Sources opened (WebFetch, every URL from a WebSearch result): subtbiol.pensoft.net/article/4563/download/xml/ (three passes); zse.pensoft.net/article/185791/download/xml/ (two passes); subtbiol.pensoft.net/article/35559/download/xml/ and subtbiol.pensoft.net/article_preview.php?id=35559; zse.pensoft.net/article/121692/download/xml/ (two passes; the XML returned to the tool stops inside the holotype's uropod 3) and zse.pensoft.net/article_preview.php?id=121692 (two passes); europeanjournaloftaxonomy.eu/index.php/ejt/article/download/1783/6775 (two passes); mdpi.com/1424-2818/16/9/564; bdj.pensoft.net/article_preview.php?id=1000 (Golovatch 2013, for glomerid ocellus wording only); Crossref single-DOI lookups api.crossref.org/v1/works/ for the six DOIs. Plazi, Zenodo, BHL, zobodat, GBIF, DOAJ and repository copies were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 9 WebSearches.

## Bibliographic and licence

- Line 1 (Sidorov, Kovtun 2015). Page "Sidorov DA, Kovtun OA (2015)"; Crossref Dmitry A. Sidorov, Oleg A. Kovtun; title as filed (both parts read); Subterranean Biology 15: 11-27, no issue; issued 2015-02-06; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 2 (Jiang, Liu, Chen 2026). Page and Crossref Xuankong Jiang, Bangyou Liu, Huiming Chen; title identical; Zoosystematics and Evolution 102(3): 767-782; issued 2026-05-28; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 3 (Liu, Wynne 2019). Page and Crossref Weixin Liu, J. Judson Wynne ("Wynne JJ" right); title identical; Subterranean Biology 30: 57-94, no issue; issued 2019-07-02; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 4 (Baytaşoğlu, Aksu, Özbek 2024). Page and Crossref Hazel Baytaşoğlu, İsmail Aksu, Murat Özbek; title identical; Zoosystematics and Evolution 100(3): 989-1004; issued 2024-07-11; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Accepted.
- Line 5 (Antić, Makarov 2022). Page and Crossref Dragan Antić, Slobodan Makarov; title identical; European Journal of Taxonomy 819: 90-107, no issue; issued 2022-05-13; Crossref CC BY 4.0 content-version unspecified; page prints "This work is licensed under a Creative Commons Attribution License (CC BY 4.0)." Accepted under the "unspecified + page-printed" rule. (The species is "Caucaseuma strasseri Antić sp. nov.", Antić alone; not a record field.)
- Line 6 (Wang, Sha, Ren 2024). Page and Crossref Yanrong Wang, Zhongli Sha, Xianqiu Ren; title identical; Diversity 16(9): 564; issued 2024-09-10; Crossref CC BY 4.0 vor; page states "Creative Commons Attribution (CC BY) license" (footer CC BY 4.0, page metadata CC BY 3.0; tool summary), accepted under the 3.0-page/4.0-Crossref rule. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

All six are described as new in the cited papers; names rest on the original descriptions (no checklist opened). Higher taxa as printed: Order Amphipoda / Family Crangonyctidae (line 1); Order Glomerida / Family Glomeridae (lines 2, 3); Gammaridae, Amphipoda (title, line 4); Class Diplopoda / Order Chordeumatida / Family Anthroleucosomatidae (line 5); Iphimedioidea, Laphystiopsidae, Amphipoda (title, line 6; the order rank is not printed separately). Order is filed as order, not class, in every line. Names faults 0.

## Trait keys

ommatidia_count (lines 1, 5), eyes_count (lines 2, 3) and eye_type (lines 4, 6) are all on main; no new key. Trait-key faults 0.

## Duplicates

`git grep -i` on origin/main (dbb0cb96) under docs/ (evidence, audit/corrected, audit/ALL, sheets, searched/ included) for odessana, Synurella, erecta, rukouqu, sezgini, strasseri, Caucaseuma, longicarpus, Phoxirostus and the six DOI strings: no Synurella, Hyleoglomeris erecta, rukouqu, sezgini, Caucaseuma or Phoxirostus hit; "erecta" hits are plants (gaps, searched, harvest files) and "longicarpus" is Mictyris longicarpus (canon-4), unrelated. No DOI hit. The 102 remote desk-d250 and later, desk-d3xx and audit-350 to 399 branches (desk-d299 excluded) grepped under docs/ for the six species names and DOI strings: no hit. Duplicate faults 0.

## Per line

### Line 1, Synurella odessana, ommatidia_count "7 (detached, black; per-eye reading not stated)"

Description, run-in "Male", "Head.": "Eyes (Figures 2, 3A) vestigial 7 detached ommatidia, black; yellow mass located on dorsolateral surface of head between eyes." **Quote MATCH** (no comma after the figure reference, as filed). Value and per-eye caveat right. Diagnosis "Eyes black, with reduced number of ommatidia; yellow mass located on the dorsolateral surface of the head between eyes."; female description and Variability silent on eyes; Discussion "the eyes are not lost, whereas" / "E. catacumbae, described from a similar habitat, is blind"; all as the note says.

Fault: the male description opens "*Male*, 11.5 mm long, [X42024/Cr-1541-FEFU].", the holotype's catalogue number and length (Material examined "Holotype: male, 11.5 mm, X42024/Cr-1541-FEFU,"). The count is therefore the holotype's, and the record's "does not say which specimen was counted" is wrong; the record must say the 7 is one specimen's (holotype male) and that no paratype count is given. Fixable.

**Line 1 FIXABLE.**

### Line 2, Hyleoglomeris erecta, eyes_count "6(9)+1"

Description: "Antennae brown, legs yellowish-brown (Fig. 3)." then "Ocelli 6(9)+1, lenses convex, black." then "Tömösváry organ transverse strongly horseshoe-shaped, ca 1.3 times as long as broad." **Quote MATCH.** The Description opens with holotype and paratype measurements ("Holotype length ca.15.9 mm ..."; "Paratypes length ca. 14.9–20.0 mm (males), 15.7–27.4 mm (females); ..."), so it covers the type series, as the record's "measurements as ranges" says. "Ocelli" occurs once in the paper and "eyes" never; the paper does not define the notation (terminology after Golovatch et al. 2012 and Golovatch 2013a, b; tool summary). The record files the notation as printed and says the paper gives neither side nor the meaning of the bracket, which is what the page supports; this matches the H. halang precedent (d289, audit 378). Type material: holotype male; paratypes 6 males and 14 females in total (5 males and 7 females with the holotype data; 1 female Zhengjiashan; 4 females Shibao, Qingxigou; 1 male and 1 female Maluba; 1 female Gangou; tool summary). The record's "plus further females" is not wrong but leaves the totals out; optional fix below. Not counted.

**Line 2 MATCH.**

### Line 3, Hyleoglomeris rukouqu, eyes_count "at least 7+1"

Description ("Based on type specimens."), Head: "Ommatidium at least 7+1, lenses rather convex." **Quote MATCH**; "at least" kept. Holotype male and 1 female paratype (SCAU), same data, as filed.

Fault: the note says "The paper gives eye text only for this species among its six new ones." The same paper prints, for H. xuxiakei sp. nov., "Ommatidium at least 5(6) + 1, translucent, barely visible (Fig. 7C)." with a Notes sentence reading the translucent ommatidia as troglobiont, and for Glyphiulus maocun sp. nov. "Each eye patch with about 8–12 ommatidium arranged in three irregular vertical rows (Figs 18A, 19A)." (tool summary for the exact wording of the second). The congener's wording is the contrast the record needs (same notation, bracketed variant, translucent lenses in a troglobiont against this species' dark-brownish ommatidia). Fixable.

**Line 3 FIXABLE.**

### Line 4, Gammarus sezgini, eye_type "kidney-shaped"

Results, Gammarus sezgini sp. nov., "Description of male holotype", Head: "Eyes kidney-shaped; length is slightly shorter than the diameter of the first peduncular segment of antenna 1 (Fig. 2)." **Quote MATCH.** Holotype male 9.8 mm, allotype female, paratypes 38 males and 34 females, as filed.

Faults:
1. Omitted variation. The species' Variability section reads "Some of the paratypes are immature." then "The eyes are kidney-shaped, or elongated, and oval." The note says "no variability statement about the eyes was found", and the conditions present the holotype shape without the paratypes' range. The value stays the holotype's, but the record must state that the paratypes' eyes are kidney-shaped or elongated-oval. The Discussion also says the species resembles G. komareki "by the presence and the shape of the eyes" (not used to separate them). Fixable.
2. Location wording: the printed headings are "Results" and "Description of male holotype", not "Systematics" and "Description of the holotype male". Fixable (counted with fault 1 as one record error).

**Line 4 FIXABLE.**

### Line 5, Caucaseuma strasseri, ommatidia_count "20-25 (mainly 23)"

Description, HEAD: "Number of ommatidia: 20–25 (mainly 23) in 6 rows in both sexes, arranged in irregular subtriangle (Figs 2C, 3C)." The quote cuts only the figure reference to "(…)." **Quote MATCH**; range and mode both printed; the en dash is as printed. Holotype male (ZMUM), paratypes 6 males and 1 female, other material 3 females and 30 juveniles; the juveniles' ommatidia are not described (the sentence says "both sexes"), so the conditions are right. Coloration "Ommatidia brownish (Fig. 2B–C)." supports the eye field. Remarks "reduced body and ommatidia pigmentation"; Discussion "the number of ommatidia does not differ significantly between cavernicolous and epigean Caucaseuma"; C. elephantum "11–12 vs 20–25"; all as the note says.

**Line 5 MATCH.**

### Line 6, Phoxirostus longicarpus, eye_type "reniform, bulging laterally"

3.1. Taxonomy, Phoxirostus longicarpus sp. nov., Description: "The rostrum present, acute, reaching to half-length of peduncular article 1 of antenna 1; eyes reniform, bulging laterally." **Quote MATCH.** Holotype female 6.0 mm, dissected (MBM 286818); no paratypes; genus Diagnosis "Rostrum acute; eye large."; P. yapensis "eyes bulging laterally, nearly as large as head."; all as the note says. The record does not say that no paratypes exist or that a second specimen with the same data was used only for DNA (tool summary); optional addition below. Not counted.

**Line 6 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Synurella odessana, 7 ommatidia | FIXABLE | conditions | male description is the holotype by catalogue number; record says the specimen is not stated |
| 2 | Hyleoglomeris erecta, 6(9)+1 | MATCH | none | quote MATCH (5); notation filed as printed, meaning and side truthfully reported as unstated |
| 3 | Hyleoglomeris rukouqu, at least 7+1 | FIXABLE | note | note claims no other species in the paper has eye text; H. xuxiakei and Glyphiulus maocun do |
| 4 | Gammarus sezgini, kidney-shaped | FIXABLE | where, conditions, note | Variability "kidney-shaped, or elongated, and oval" omitted; headings misquoted |
| 5 | Caucaseuma strasseri, 20-25 (mainly 23) | MATCH | none | quote MATCH (17); range and mode printed; all type material stated |
| 6 | Phoxirostus longicarpus, reniform | MATCH | none | quote MATCH (18); single type specimen |

Errors 3 of 6 audited records (50%). By kind: quotes 0; location 0 counted (line 4 headings folded into its variation fault); value meaning 0; omitted variation 1 (line 4); sample composition 1 (line 1); omitted contrasting wording 1 (line 3); bibliographic 0; licence 0; names 0; trait key 0; duplicates 0. All fixable; nothing unfixable, nothing held out. Verdict: merge lines 1-6 with the Replacement applied (lines 1, 3, 4 required; lines 2 and 6 optional).

Unchecked: figures not viewed; the female and Variability parts of the G. sezgini paper were read only on the article_preview page; the grep of all 1476 remote branches had not finished, so older unmerged branches (before desk-d250 and audit-350) were not searched; no checklist opened for any of the six names.

## Replacement

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 1:
- `conditions`: "the sentence does not say whether 7 is per eye or the total, and does not say which specimen was counted" -> "the sentence does not say whether 7 is per eye or the total; the male description opens 'Male, 11.5 mm long, [X42024/Cr-1541-FEFU].', the holotype's number and length, so the count is the holotype male's, and no paratype or female count is given"

Line 3:
- `note`: "The paper gives eye text only for this species among its six new ones." -> "Two other new species in the paper have eye text: the congener H. xuxiakei 'Ommatidium at least 5(6) + 1, translucent, barely visible (Fig. 7C).' (read as a troglobiont from its translucent ommatidia) and Glyphiulus maocun, about 8-12 ommatidia per eye patch in three irregular rows."

Line 4:
- `where`: "Systematics, Gammarus sezgini sp. nov., Description of the holotype male, Head" -> "Results, Gammarus sezgini sp. nov., Description of male holotype, Head"
- `conditions`: "the sentence is the holotype description;" -> "the sentence is the holotype description and the value is the holotype's; the species' Variability section says 'The eyes are kidney-shaped, or elongated, and oval.' (paratypes, some immature);"
- `note`: "the quote is the holotype sentence and no variability statement about the eyes was found." -> "the quote is the holotype sentence; the Variability section widens the shape to kidney-shaped or elongated-oval, and the Discussion says the species resembles G. komareki 'by the presence and the shape of the eyes'."

Line 2 (uncounted):
- `conditions`: "plus further females and one male and one female from Maluba" -> "plus 1 female from Zhengjiashan, 4 females from Shibao (Qingxigou), 1 male and 1 female from Maluba and 1 female from Gangou (paratypes 6 males and 14 females in all)"

Line 6 (uncounted):
- `conditions`: "holotype female 6.0 mm (MBM 286818);" -> "holotype female 6.0 mm (MBM 286818), no paratypes (a second specimen with the same data was used only for DNA extraction);"
