# audit-384: desk-d293, evidence lines 1 to 7

Audited 1 November 2026 from the desk-d293 files present untracked in the worktree (docs/tracks/progress/desk-d293.md and docs/views/evidence/desk-d293.jsonl, 7 lines; neither committed here, neither edited). Line numbers are the file's (1-based). `python3 -I tools/senses/check.py | grep 'd293\.'`: "docs/views/evidence/desk-d293.jsonl: 7 records, 0 problems". Quote lengths (`len(q.split())`): 9, 15, 2, 2, 2, 2, 2, all within 40; no non-ASCII characters in any quote.

Sources opened (WebFetch): api.crossref.org/v1/works/ for the four DOIs; zookeys.pensoft.net/article/73094/download/xml/; zookeys.pensoft.net/article/52361/download/xml/; zookeys.pensoft.net/article/31635/download/xml/ and zookeys.pensoft.net/article_preview.php?id=31635; subtbiol.pensoft.net/article/76926/download/xml/ (returned C. whitteni only) and subtbiol.pensoft.net/issue/3555/pdf/823967 (the three other species). All URLs were returned by a WebSearch first. Plazi, Zenodo, GBIF, PMC, optimap, bionames, BHL, DOAJ, novataxa, university repository and catalogue hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 4 WebSearches.

## Bibliographic and licence

- Line 1 (Winkler, Németh, Fiera 2021). Crossref: Daniel Winkler, Márton Tamás Németh, Cristina Fiera; title identical to the record; ZooKeys 1063, 121-137, no issue; issued 2021-10-20; CC BY 4.0 vor. Page byline same order; licence "open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0)". Accepted.
- Line 2 (Baquero, Jordana, Labrada, Luque 2020). Crossref: Enrique Baquero, Rafael Jordana, Lucía Labrada, Carlos G. Luque; title identical; ZooKeys 989, 39-54, no issue; issued 2020-11-09; CC BY 4.0 vor. Page byline same order; licence CC BY 4.0 (tool summary; sentence over the quote limit) plus Crossref vor CC BY 4.0. Accepted.
- Line 3 (Jantarit, Satasook, Deharveng 2019). Crossref: Sopark Jantarit, Chutamas Satasook, Louis Deharveng; title identical; ZooKeys 824, 21-44, no issue; issued 2019-02-12; CC BY 4.0 vor. Page licence Creative Commons Attribution License (CC BY 4.0) (tool summary) plus Crossref vor. Accepted.
- Lines 4-7 (Nilsai, Detcharoen, Godeiro, Jantarit 2021). Crossref: Areeruk Nilsai, Matsapume Detcharoen, Nerivania Nunes Godeiro, Sopark Jantarit; title verbatim in two pieces "Four new species of troglomorphic Coecobrya Yosii, 1956 (Collembola, Entomobryidae) from Thailand" + "based on morphological and molecular evidence, with an updated key of Thai troglomorphic species", identical to the record; Subterranean Biology 41, 1-42, no issue; issued 2021-12-10; CC BY 4.0 vor. Page licence "Creative Commons Attribution License (CC BY 4.0)". Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

All seven species are described as new in the cited papers; names rest on the original descriptions (no checklist opened). The ZooKeys 824 page prints the heading chain Class Collembola, Order Entomobryomorpha, Family Entomobryidae, Subfamily Entomobryinae, Genus Coecobrya (tool summary); the three other titles print "(Collembola, Entomobryidae)". Entomobryidae and Entomobryomorpha are right for Pseudosinella and Coecobrya; class Collembola right. Name faults 0.

## Trait key

eyes_count is on main. Values 5 (lines 1-2) and 0 (lines 3-7). No new key.

## Duplicates

`git grep -i` on origin/main under docs/ (evidence, audit/corrected, audit/ALL, sheets, searched/ included) for the seven epithets, "Coecobrya" and the four DOI suffixes: no hit (one false hit, "Jobellisiales" in docs/views/world-orders.csv). Remote desk-* and audit-* branches (docs/views/evidence, docs/tracks) for the same patterns, d293 excluded: see the branch note at the end. Duplicate faults 0.

## Per line

### Line 1, Pseudosinella hartnerae, eyes_count 5 (per side)

Description, Head: "With 5+5 eyes (ABCDH, with H only slightly smaller)." **Quote MATCH**. Diagnosis verbatim "5+5 ocelli."; Habitus "Eye patches dark blue." The paper prints no variation in eye number. Type material verbatim: holotype "♀ on slide (Nr. HNHM collpr-896), Bátorliget, ..."; paratypes "Two ♀ and one ♂ on slide (Nr. HNHM collpr-896);" "two ♀ and one specimen with sex not visible (Nr.: HNHM collpr-897);" "two ♀ (Nr. WD–coll–113 and WD–coll–114); same data as holotype."; deposition "The holotype and four paratypes are deposited in the Hungarian Natural History Museum (HNHM), Budapest." (six paratypes listed under HNHM numbers, so the desk's "do not reconcile" is fair). Conditions match. "5+5" as five per side is the standard notation and is confirmed by the Diagnosis; the paper does not write "per side" in words, which the note does not claim. Units "pairs (5+5)" and eye "per side" say the same count (five on each side).

**Line 1 MATCH.**

### Line 2, Pseudosinella altamirensis, eyes_count 5

Description, Head: "With five eyes (ABDEF or ABCDF; C and F smaller, almost imperceptible in some specimens)." **Quote MATCH**; variation kept in quote and conditions. Holotype female, Altamira Cave (tool summary for the block, which is over the quote limit); paratype sexes not stated (tool summary). No juveniles mentioned.

Error (value meaning): conditions say "the paper does not say in this sentence whether five is per side or per head" and the note says the sentence "does not state per side or total; the value is logged as printed". The sentence alone does not, but the paper does: Diagnosis verbatim "5 + 5 ocelli." and Table 2 legend verbatim "C2: number of eyes per side." (P. altamirensis C2 = 5, tool summary). The record leaves open a question the paper answers, while its own `units` field says "eyes (per side)". Fixable from the page text; replacements below.

**Line 2 FIXABLE.**

### Line 3, Coecobrya sirindhornae, eyes_count 0

Under the species' Description, subheading Habitus: "No scales." then "Eyes absent." then "Colour: pale yellow to whitish in alcohol, without pigments." (tool summary for the order of sentences, the quoted sentences verbatim). **Quote MATCH**; the sentence sits in the C. sirindhornae Description, and the paper has no Diagnosis section. Abstract: "the absence of eyes and pigmentation." Type material (verbatim pieces): holotype "male on slide", Tham Rusri; first event "one male, one female and three subadults in slides, three in ethanol" (nine stated, eight itemised); later events subadults on slides and unsexed specimens in ethanol. Conditions name the holotype male, a female, subadults and ethanol specimens and the non-reconciling counts. Uncounted: the conditions omit the one paratype male ("other type specimens include a female"); no sex or stage is missing, so not an error. Optional replacement below.

**Line 3 MATCH.**

### Line 4, Coecobrya whitteni, eyes_count 0

Description, Habitus: "No scales." then "Eyes absent." then "Color: whitish in alcohol, without pigmentation." **Quote MATCH**, inside the C. whitteni Description, not a Diagnosis. Holotype female on slide, Tham Nayn Noi, Chum Phae district, Khon Kaen; 11 paratypes on slides (three females, eight subadults); three specimens in ethanol (tool summary). Conditions match.

**Line 4 MATCH.**

### Line 5, Coecobrya troglobia, eyes_count 0

Verbatim "Description. Habitus (Fig. 1B). Medium size Entomobryidae. Body length 2.0–2.4mm (holotype 2.4mm). No scales. Eyes absent. Color: whitish in alcohol, without pigmentation." **Quote MATCH**. Holotype female on slide, Tham Phaya Nakharat, Khon Kaen; 7 paratypes on slides (3 females, 4 subadults); 6 in ethanol (tool summary). Conditions match.

**Line 5 MATCH.**

### Line 6, Coecobrya ellisi, eyes_count 0

Verbatim "Description. Habitus (Fig. 1C). ... No scales. Eyes absent. Color: whitish in alcohol, with orange pigmentation on head, body, legs and furca." **Quote MATCH**. Holotype male on slide, Tham Tho, Phetchabun; 12 paratypes on slides (1 male, 4 females, 7 subadults); 8 in ethanol (tool summary). Conditions match.

**Line 6 MATCH.**

### Line 7, Coecobrya phitsanulokensis, eyes_count 0

Verbatim "Description. Habitus (Fig. 1D). ... No scales. Eyes absent. Color: whitish in alcohol, without pigmentation." **Quote MATCH**. Holotype female on slide, Tham Yai Nakarat, Phitsanulok; 7 paratypes on slides (3 females, 4 subadults); 13 in ethanol (tool summary). Conditions match.

**Line 7 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Pseudosinella hartnerae, 5 per side | MATCH | none | quote MATCH (9); 5+5 confirmed by Diagnosis; no variation printed |
| 2 | Pseudosinella altamirensis, 5 | FIXABLE | conditions, note | record says per side/total is unstated; Diagnosis "5 + 5" and Table 2 "per side" settle it |
| 3 | Coecobrya sirindhornae, 0 | MATCH | none | quote MATCH (2) in its Habitus; paratype male omitted, uncounted |
| 4 | Coecobrya whitteni, 0 | MATCH | none | quote MATCH (2) in its Habitus; type block matches |
| 5 | Coecobrya troglobia, 0 | MATCH | none | quote MATCH (2) in its Habitus; type block matches |
| 6 | Coecobrya ellisi, 0 | MATCH | none | quote MATCH (2) in its Habitus; type block matches |
| 7 | Coecobrya phitsanulokensis, 0 | MATCH | none | quote MATCH (2) in its Habitus; type block matches |

Errors 1 of 7 audited records (14.3%). By kind: quotes 0; value meaning 1 (line 2); sample composition 0; bibliographic 0; licence 0; names 0; filing convention 0; duplicates 0. Fixable; nothing unfixable, nothing held out. Verdict: merge lines 1-7 with the Replacement applied (line 2 required; line 3 optional).

Unchecked: figures not viewed; the altamirensis holotype and paratype blocks, its Table 2 value, the Subterranean Biology type blocks and the sirindhornae sentence order rest on tool summaries; no checklist gave current status of the seven names.

## Replacement

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 2:
- `conditions` (counted): "; the paper does not say in this sentence whether five is per side or per head" -> "; the sentence does not say per side, but the Diagnosis reads \"5 + 5 ocelli.\" and the Table 2 legend reads \"C2: number of eyes per side.\", so five is per side (ten in all)"
- `note` (counted): "The sentence says only 'five eyes' and does not state per side or total; the value is logged as printed." -> "The sentence says only 'five eyes'; the Diagnosis (\"5 + 5 ocelli.\") and the Table 2 legend (\"C2: number of eyes per side.\") show the count is per side."

Line 3 (uncounted):
- `conditions`: "other type specimens include a female, subadults and unsexed specimens in ethanol" -> "other type specimens include one male, one female, subadults and unsexed specimens in ethanol"
