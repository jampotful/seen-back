# audit-380: desk-d291, evidence lines 1 to 8

Audited 1 November 2026 from the desk-d291 files present untracked in the worktree (docs/tracks/progress/desk-d291.md and docs/views/evidence/desk-d291.jsonl, 15 lines; neither committed here, neither edited). Lines 9 to 15 belong to audit 381. Worktree HEAD and origin/main 14e50fbb (Merge desk d290 (7 records) after audit 379). `python3 -I tools/senses/check.py | grep 'd291\.'`: "docs/views/evidence/desk-d291.jsonl: 15 records, 0 problems". Quote lengths (`len(q.split())`) for lines 1-8: 11, 8, 13, 11, 12, 11, 21, 18, all within 40; no quote contains a non-ASCII character. Line numbers are the file's (1-based).

Sources opened (WebFetch): api.crossref.org/v1/works/ for the three DOIs (zookeys.1115.86477 rate-limited once, answered on retry); jhr.pensoft.net/article/82490/download/xml/; dez.pensoft.net/article/171173/download/xml/ (ended before the C. bifida account); dez.pensoft.net/article_preview.php?id=171173 (two passes); zookeys.pensoft.net/article/86477/download/xml/. All URLs were returned by a WebSearch first. Plazi, AntWiki, BHL, DOAJ, NSM repository and library-catalogue hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 3 WebSearches.

## Bibliographic and licence

- Lines 1-2 (Hosoishi, Yamane, Sokh 2022). Crossref: Shingo Hosoishi, Seiki Yamane, Heng Sokh; title identical; Journal of Hymenoptera Research 91, 357-374, no issue; issued 2022-06-30; CC BY 4.0 vor. Page byline same order; licence verbatim "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0),". Accepted.
- Lines 3-6 (Matsuura, Hosoishi, Pham 2025). Crossref: Kohei Matsuura, Shingo Hosoishi, Hong Thai Pham; title verbatim "Taxonomic revision of the Carebara oni species group, with descriptions of two new species from Vietnam (Hymenoptera, Formicidae, Myrmicinae)", matching the record; DEZ 72(2), 377-393; issued 2025-11-14; CC BY 4.0 vor. Page title in the same two pieces; licence verbatim (CC BY 4.0). Accepted.
- Lines 7-8 (Jaitrong, Xu, Khachonpisitsak 2022). Crossref: Weeyawat Jaitrong, Zhenghui Xu, Salinee Khachonpisitsak; title identical; ZooKeys 1115, 151-168, no issue; issued 2022-08-01; CC BY 4.0 vor. Page byline same order; licence verbatim (CC BY 4.0). Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

No checklist reached. Carebara colobopsis, C. eguchii, C. bifida and Platythyrea homasawini are described as new in the cited papers; P. janyai was described by "Phengsi, Jaitrong, Ruangsittichai & Khachonpisitsak, 2018" (as the ZooKeys page cites it, tool summary). Family Formicidae, order Hymenoptera on every line; the pages place Carebara in Myrmicinae ("the tribe Crematogastrini of the subfamily Myrmicinae") and Platythyrea in Ponerinae (title), and no subfamily is filed as family. Name faults 0.

## Trait key

ommatidia_count is not in TRAITS in tools/senses/check.py, but 52 records on main already use it (desk-d270, d271, d272, d274, oa-2, oa-3, oa-5, oa-6, oa-14, recheck-9-fixed), and every line flags it as a new trait. Filing convention met.

## Duplicates

git grep on origin/main (14e50fbb) across the whole docs/ tree for colobopsis, eguchii, "Carebara bifida", homasawini, janyai, the three DOIs and the article ids 82490, 171173, 86477: no species or DOI hits. "82490" appears only inside hash strings in canon-7.jsonl and web-mammals.jsonl, "86477" only inside a hash in harvest-c11.md, "bifida" only as Furcula bifida (a moth) in oa-13a.jsonl. All remote research/desk-* and research/audit-* branches other than desk-d291 grepped under docs/ for the same patterns: only the same hash and Furcula hits. Duplicates 0.

## Per-record findings

### Line 1, Carebara colobopsis, ommatidia_count 5-6 (major worker)

Under "Description of major worker.": "Compound eyes small, consisting of five to six ommatidia (EL 0.05)." **Quote MATCH**. Holotype "(major worker)"; paratypes verbatim "2 major workers (collection code KUECANT032, KUECANT033)" and "4 minor workers (collection code KUECANT034, KUECANT035, KUECANT036, KUECANT037)". Major paratypes EL 0.04-0.05 (tool summary). No eye variation statement. Conditions and caste match; value [5, 6] says no more than the quote.

**Line 1 MATCH.**

### Line 2, Carebara colobopsis, ommatidia_count 1 (minor worker)

Under "Description of minor worker.": "Eyes present, consisting of one ommatidium (EL 0.01)." **Quote MATCH**. Four paratype minors, no minor holotype, as conditions say.

**Line 2 MATCH.**

### Line 3, Carebara eguchii, ommatidia_count 2-3 (major worker)

Under "Description of worker", heading "Major worker.": "Eyes with two or three ommatidia, situated at anterior one-third of head, laterally." **Quote MATCH**. Holotype verbatim "Holotype: Vietnam • major worker;" (KUECCRB011); paratypes verbatim "Paratypes: Vietnam • 2 major workers and 2 minor workers;". No non-type material for this species (tool summary). Diagnosis, key and remarks carry no eye statement (tool summary). Conditions match.

**Line 3 MATCH.**

### Line 4, Carebara eguchii, ommatidia_count 2 (minor worker)

Under "Minor worker.": "Eyes with two ommatidia, situated at anterior one-third of lateral head." **Quote MATCH**. Two paratype minors, as conditions say.

**Line 4 MATCH.**

### Line 5, Carebara bifida, ommatidia_count 10 visible (major worker)

Major worker description: "Eyes large, ten ommatidia visible, situated at anterior one-third of lateral head." **Quote MATCH**. Holotype "Vietnam • major worker"; paratypes verbatim "Vietnam • 2 major workers and 10 minor workers"; EL holotype 0.10, major paratypes 0.10-0.12. Units "ommatidia visible" keep the paper's qualifier. No eye statement in the diagnoses or Remarks (tool summary).

Uncounted: the page also lists non-type material, "1 major worker and 1 minor worker" and "1 minor worker" from other Vietnamese localities (tool summary for the grouping), which the conditions omit. Whether the description draws on them is not stated. Replacement below.

**Line 5 MATCH.**

### Line 6, Carebara bifida, ommatidia_count 1 (minor worker)

Minor worker description: "Eyes with one ommatidium, situated laterally at anterior one-third of head." **Quote MATCH**. Ten paratype minors (EL 0.01). Same non-type omission as line 5, uncounted. Replacement below.

**Line 6 MATCH.**

### Line 7, Platythyrea homasawini, ommatidia_count 7-8 along longest axis

Description of workers: "Eyes flat, located at anterior 1/3 of head length, moderately large, each with 7 or 8 ommatidia along its longest axis." **Quote MATCH**. Holotype verbatim "Holotype worker (THNHM-I-26225)"; paratypes verbatim "29 workers (THNHM-I-26226 to THNHM-I-26250, THNHM-I-24977 to THNHM-I-24979, and THNHM-I-26445)". Units say a linear count, as the quote does. Elsewhere the comparison with P. clypeata gives a single figure, verbatim "4) eye larger (EI = 15, with 7 ommatidia in P. homasawini; EI = 11, with 5 ommatidia in P. clypeata)"; it sits inside the stated range and is not contrary.

Uncounted: the conditions omit three non-type workers (one from Yunnan, China; two from Thailand, THNHM-I-02463 and THNHM-I-02454). Replacement below.

**Line 7 MATCH.**

### Line 8, Platythyrea janyai, ommatidia_count 11 along longest axis

Description of workers: "Eye slightly convex, located anterior to mid-length of head, relatively large, with 11 ommatidia on the longest axis." **Quote MATCH**. Type lines verbatim "Holotype (THNHM-I-02392) and three paratypes (THNHM-I-02393 to THNHM-I-02395) workers,"; non-type workers from Malaysia (1) and Thailand (2 + 5) are listed, as conditions say ("adds non-type material"). The P. clypeata comparison repeats verbatim "EL 0.20 mm long with 11 ommatidia on longest axis in P. janyai". No variation reported.

Uncounted: the note says the species was "named in an earlier paper by other authors"; the describers are Phengsi, Jaitrong, Ruangsittichai and Khachonpisitsak (2018), two of whom (Jaitrong, Khachonpisitsak) are authors of the cited paper. Replacement below.

**Line 8 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Carebara colobopsis, 5-6 (major) | MATCH | none | quote MATCH (11); major caste, type series stated |
| 2 | Carebara colobopsis, 1 (minor) | MATCH | none | quote MATCH (8); four paratype minors stated |
| 3 | Carebara eguchii, 2-3 (major) | MATCH | none | quote MATCH (13); no non-type material |
| 4 | Carebara eguchii, 2 (minor) | MATCH | none | quote MATCH (11); two paratype minors stated |
| 5 | Carebara bifida, 10 visible (major) | MATCH | none | quote MATCH (12); "visible" kept; non-type omission uncounted |
| 6 | Carebara bifida, 1 (minor) | MATCH | none | quote MATCH (11); non-type omission uncounted |
| 7 | Platythyrea homasawini, 7-8 along longest axis | MATCH | none | quote MATCH (21); linear count stated; non-type omission uncounted |
| 8 | Platythyrea janyai, 11 along longest axis | MATCH | none | quote MATCH (18); note's "other authors" wrong, uncounted |

Errors 0 of 8 audited records (0%). By kind: quotes 0; value exceeding quote 0; sample composition 0; bibliographic 0; licence 0; names 0; filing convention 0; duplicates 0. Nothing from lines 1-8 is held out. Verdict: merge lines 1 to 8 (the uncounted replacements below are optional); lines 9 to 15 rest on audit 381.

Unchecked: no checklist entry for any species; figures not viewed; the C. bifida non-type grouping, the absence of eye statements in diagnoses and remarks, and the P. janyai describer citation rest on tool summaries.

## Replacement

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). All uncounted.

Line 5:
- `conditions`: "type series is one holotype major worker, two paratype major workers and ten paratype minor workers" -> "type series is one holotype major worker, two paratype major workers and ten paratype minor workers; non-type material of one major and two minor workers from other Vietnamese localities is also listed"

Line 6:
- `conditions`: "the minor workers in the type series are ten paratypes (no minor-worker holotype)" -> "the minor workers in the type series are ten paratypes (no minor-worker holotype); two non-type minor workers are also listed"

Line 7:
- `conditions`: "holotype worker THNHM-I-26225 and 29 paratype workers" -> "holotype worker THNHM-I-26225 and 29 paratype workers, plus three non-type workers (one from Yunnan, China, two from Thailand); the comparison with P. clypeata cites 7 ommatidia for this species"

Line 8:
- `note`: "named in an earlier paper by other authors" -> "named by Phengsi, Jaitrong, Ruangsittichai and Khachonpisitsak 2018, two of whom are authors here"
