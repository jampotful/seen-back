# audit-381: desk-d291, evidence lines 9 to 15

Audited 1 November 2026 from the desk-d291 files present untracked in the worktree (docs/tracks/progress/desk-d291.md and docs/views/evidence/desk-d291.jsonl, 15 lines; neither committed here, neither edited). Lines 1 to 8 are audit 380's. Worktree HEAD and origin/main 14e50fbb (Merge desk d290 (7 records) after audit 379). `python3 -I tools/senses/check.py | grep 'd291\.'`: "docs/views/evidence/desk-d291.jsonl: 15 records, 0 problems". Quote lengths (`len(q.split())`) for lines 9-15: 12, 12, 12, 12, 12, 2, 19, all within 40; no quote contains a non-ASCII character. Line numbers are the file's (1-based).

Sources opened (WebFetch): api.crossref.org/v1/works/ for 10.3897/zookeys.1230.140159, 10.3897/zookeys.1010.58436 and 10.3897/zookeys.963.55843; zookeys.pensoft.net/article/140159/download/xml/ (truncated before the treatments); zookeys.pensoft.net/article_preview.php?id=140159 (three passes); zookeys.pensoft.net/article_preview.php?id=58436; zookeys.pensoft.net/article/55843/download/xml/; zookeys.pensoft.net/article_preview.php?id=55843. All URLs were returned by a WebSearch first. PMC, Plazi, GBIF, DOAJ, BHL, core.ac.uk, optimap and library catalogue hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 3 WebSearches.

## Bibliographic and licence

- Lines 9-12 (Chen, Yu, Yi 2025). Crossref: Chao Chen, Yu Yu, Chuanhui Yi; title identical; ZooKeys 1230, 247-286, no issue; issued 2025-03-06; CC BY 4.0 vor. Page byline verbatim "Chao Chen, Yu Yu, Chuanhui Yi"; licence verbatim "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0),". Methods verbatim "Eye diameter: the maximum diameter of the eye." and "All measurements are expressed in millimeters." Accepted.
- Lines 13-14 (Bharti, Rilta, Dhadwal 2021). Crossref: Himender Bharti, Joginder Singh Rilta, Tarun Dhadwal; title identical; ZooKeys 1010, 165-183, no issue; issued 2021-01-13; CC BY 4.0 vor. Page byline same order; licence sentence verbatim (CC BY 4.0). Accepted.
- Line 15 (Scheffrahn, Pinzón Florian 2020). Crossref: Rudolf H. Scheffrahn, Olga Patricia Pinzón Florian; title identical; ZooKeys 963, 37-44, no issue; issued 2020-08-24; CC BY 4.0 vor. Page byline same order; licence verbatim (CC BY 4.0). Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

No checklist reached; all five species are described as new in the cited papers (both Ooceraea per the title "Two new species"), so the names rest on the original descriptions.

- Brachyponera, Ooceraea: Formicidae, Hymenoptera, from the titles. Met.
- Rugitermes tinto: the taxon classification block prints "Blattodea" (order) and "Kalotermitidae" (family) (tool summary for the block layout); the title prints Isoptera. Main files termites under Blattodea ("family": "Termitidae", "order": "Blattodea"), and no evidence file on main uses "Isoptera" as an order. The record's "order": "Isoptera" is a filing error (line 15, fixable).

Name faults 1 (line 15).

## Duplicates

git grep on origin/main (14e50fbb) across the whole docs/ tree for Brachyponera candida, myops, joshii, decamera, Ooceraea, Rugitermes and the three article ids: "myops" hits are other genera only (sea-invertebrate audit files, gaps, world-orders, sweep-30; none Brachyponera); "55843" only inside iNaturalist observation numbers in docs/eval; no other hits. Remote research/desk-* and research/audit-* branches grepped under docs/ for the five binomials and three DOIs (674 branches, research/desk-d291 excluded): no file hits.

Duplicates 0.

## Per-record findings

### Lines 9-10, Brachyponera myops, ommatidia_count 5 and eye_diameter_mm 0.07

Description verbatim "Eye small, and maximum diameter consists of five ommatidia (ED 0.07 mm)." **Quote MATCH**. Type material: holotype worker KIZ20231049, 5 paratype workers; holotype "ED 0.07", paratypes (n = 5) "ED 0.06–0.07" (tool summary for the layout). Abstract: new species "described from China based on the worker caste." Units "ommatidia across the maximum eye diameter" and the linear-count note match the sentence.

Line 9 error (omitted variation): the paper's own worker key gives the species a range. Couplet 4, second half, leading to "B. myops Chen, Yu & Yi, sp. nov.", reads verbatim "Eye relatively small, with 4 or 5 ommatidia along longest axis (Fig. 4A);" (couplet 3 first half: "Eye small with 2–5 ommatidia along longest axis (ED 0.07 mm) (Fig. 4A, B)"). The record files 5 and says nothing of the 4-5 range printed for the same species. Fixable by conditions text (the value stays the description's 5). Replacement below.

Line 10: ED 0.07 is the holotype value as the note says; paratype range 0.06-0.07 in conditions; the key also prints "(ED 0.07 mm)". **Line 10 MATCH.**

### Lines 11-12, Brachyponera candida, ommatidia_count 11 and eye_diameter_mm 0.17

Description verbatim "Eye medium and maximum diameter consists of eleven ommatidia (ED 0.17 mm)." **Quote MATCH**. Holotype worker KIZ20230168, 5 paratype workers; holotype "ED 0.17", paratypes "ED 0.15–0.17" (tool summary for layout). The couplet leading to B. candida (15) is petiole-based, verbatim "Petiolar node thick (PL > 0.40 mm); in dorsal view, petiole long trapezoidal shape (Fig. 14A) (China)"; the eye couplet on its branch says "> 7 ommatidia along longest axis (ED > 0.10 mm)", consistent with 11. No other eye count for the species (tool summary). **Lines 11 and 12 MATCH.**

### Line 13, Ooceraea joshii, ommatidia_count 2

Worker description verbatim "Eyes present, small in size, with two ommatidia, parafrontal ridge prominently produced." **Quote MATCH** (whole sentence, 12 words). Type material verbatim "Holotype worker and one paratype worker, both India, Kerala, Periyar Tiger Reserve 9.5627°N, 77.2348°E, 780 m," and "leaf litter, Winkler, 21 January 2017, Tarun Dhadwal leg. [PUAC]." "Queen. Unknown." and "Male. Unknown." Recognition verbatim "presence of ommatidia (present in O. joshii sp. nov. and absent in O. decamera sp. nov.)", as the note says. Units "ommatidia per eye" fit "with two ommatidia". **Line 13 MATCH.**

### Line 14, Ooceraea decamera, eye_type none

Worker description verbatim "Eyes absent." **Quote MATCH**; attribution shown in `where` and the note. Holotype verbatim "Holotype worker, India, Madras, Alagarkovil, 21 km N Madurai, 10.02308°N, 77.833333°E, 250–350 m alt.;" and "2 November 1972; Besuchet Lobt Mussard leg. (Specimen number/barcode: MCZ-ENT00649398) [MCZC]."; no paratypes; key couplet 12 "eyes absent". Conditions match. **Line 14 MATCH.**

### Line 15, Rugitermes tinto, eye_diameter_mm 0.32

The unit's quote was stitched. Two fetches: the XML returned verbatim "Measurements (maximum, mm): head width 1.31, pronotum width 1.43, eye diameter 0.32," and "ocellus diameter 0.01, and body length 7.9."; the preview page returned the overlapping segment verbatim "eye diameter 0.32, ocellus diameter 0.01, and body length 7.9.", which joins the two pieces with nothing between them. The preceding sentence is "Arolium present."; the Measurements sentence ends the Imago description, followed by "Soldier (Figs 2C, D, 3)." **Quote MATCH** as one whole printed sentence (19 words). Type material: holotype "(soldier)"; imago verbatim "one damaged female imago", UFTC no. CO919; "Single female damaged: distal half of left wings torn, right wings absent." Other imago eye text "Compound eye small, nearly circular." Conditions and value match.

Error (filing): "order": "Isoptera". The page's classification block prints Blattodea and main files termites under Blattodea; the note's "Order printed as Isoptera in the paper's title" is true of the title only. Fixable. Replacement below.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 9 | Brachyponera myops, ommatidia_count 5 | ERROR (fixable) | conditions | quote MATCH (12); key couplet 4 gives "4 or 5 ommatidia along longest axis", omitted |
| 10 | Brachyponera myops, eye_diameter_mm 0.07 | MATCH | none | quote MATCH (12); holotype ED, paratype range stated |
| 11 | Brachyponera candida, ommatidia_count 11 | MATCH | none | quote MATCH (12); key branch "> 7" consistent |
| 12 | Brachyponera candida, eye_diameter_mm 0.17 | MATCH | none | quote MATCH (12); holotype ED, paratype range stated |
| 13 | Ooceraea joshii, ommatidia_count 2 | MATCH | none | quote MATCH (12); holotype + one paratype worker |
| 14 | Ooceraea decamera, eye_type none | MATCH | none | quote MATCH (2); single holotype, attribution in where/note |
| 15 | Rugitermes tinto, eye_diameter_mm 0.32 | ERROR (fixable) | order, note | stitched quote confirmed whole by overlapping second fetch; order Isoptera should be Blattodea |

Errors 2 of 7 audited records (29%). By kind: quotes 0; value exceeding quote 0; omitted variation 1 (line 9); sample composition 0; bibliographic 0; licence 0; names/higher taxa 1 (line 15); duplicates 0. Both errors are fixable with the replacements below; nothing in lines 9-15 is held out. Verdict: merge lines 9-15 after applying the replacements.

Unchecked: no checklist entry for any species; figures not viewed; type-material layouts for Brachyponera and the Rugitermes classification-block layout rest on tool summaries.

## Replacement

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 9:
- `conditions`: "the ommatidia number is not tied to one specimen" -> "the ommatidia number is not tied to one specimen; the paper's worker key (couplet 4) gives B. myops 'Eye relatively small, with 4 or 5 ommatidia along longest axis'"

Line 15:
- `order`: "Isoptera" -> "Blattodea"
- `note`: "Order printed as Isoptera in the paper's title (termites are now placed in Blattodea)." -> "The title prints Isoptera; the taxon classification block prints Blattodea, used here."
