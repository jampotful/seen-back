# audit-387: desk-d296, evidence lines 1 to 5

Audited 1 November 2026 from the desk-d296 files present untracked in the worktree (docs/tracks/progress/desk-d296.md and docs/views/evidence/desk-d296.jsonl, 5 lines; neither committed here, neither edited). Line numbers are the file's (1-based). HEAD equals origin/main (8f9613c2). `python3 -I tools/senses/check.py | grep 'd296\.'`: "docs/views/evidence/desk-d296.jsonl: 5 records, 0 problems". Quote lengths (`len(q.split())`): 20, 2, 13, 13, 13, all within 40; no non-ASCII characters in any quote.

Sources opened (WebFetch): zookeys.pensoft.net/article/54958/download/xml/ (two passes); zookeys.pensoft.net/article/114072/download/xml/; zookeys.pensoft.net/article/75885/download/xml/ (two passes); Crossref single-DOI lookups api.crossref.org/v1/works/ for the three DOIs. All article URLs were returned by a WebSearch first. PMC, Plazi, DOAJ, BHL, zenodo, GBIF, antcat, bionames, optimap and news/blog hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 4 WebSearches.

## Bibliographic and licence

- Line 1 (Brassard, Leong, Chan, Guénard 2020). XML and Crossref same order (François Brassard, Chi-Man Leong, Hoi-Hou Chan, Benoit Guénard); title identical; ZooKeys 970: 63-116, no issue printed; issued 2020-09-21; Crossref CC BY 4.0 vor. XML prints the CC BY 4.0 licence sentence verbatim. Accepted. The record's url (article_preview.php?id=54958) was not returned by any search here, so it was not opened; the XML of the same DOI was read instead (uncounted; optional url replacement below).
- Line 2 (Wong, McRae 2024). XML and Crossref same order; title identical; ZooKeys 1197: 171-182, no issue; issued 2024-04-11; CC BY 4.0 vor; XML licence sentence verbatim. Accepted.
- Lines 3-5 (Zhang, Kang 2022). XML and Crossref same order (Xiao Zhang, Zehui Kang); title identical; ZooKeys 1085: 51-68, no issue; issued 2022-02-04; CC BY 4.0 vor; XML licence sentence verbatim. The record's url (article_preview.php?id=75885) was returned by search; the XML copy of the same DOI was read. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

All five species are described as new in the cited papers; names rest on the original descriptions (Plazi treatments surfaced in search for all five, not opened; no checklist opened). Formicidae/Hymenoptera (lines 1, 2; Strumigenys in Myrmicinae, Leptanilla in Leptanillinae, no subfamily field filed), Blephariceridae/Diptera (lines 3-5, as printed in the title). Names faults 0.

## Trait key

Line 1 uses ommatidia_count, which is not in check.py TRAITS but is used on main (desk-d270, d271, d272, d274, d291, oa-2, oa-3, oa-5, oa-6, oa-14, with units "ommatidia per eye" or "ommatidia/eye"); the note carries "new trait ommatidia_count (already used on main)", so check.py passes. The progress file's "No new key" is loose wording for the same fact (uncounted). Lines 2-5 use eye_type, an accepted key. The Blepharicera values are the printed ratios ("1/20 as large as", "as large as", "1/15 as large as") restated as "1/20 the size of" etc., not derived or computed values; the units field is empty, as for other eye_type strings on main.

## Duplicates

`git grep -i` on origin/main (8f9613c2) under docs/ (evidence, audit/corrected, audit/ALL, sheets, searched/ included) for "Strumigenys subterranea", "Leptanilla voldemort", gengdica, balangshana, kongsica, Blepharicera, and the DOI suffixes 970.54958, 1197.114072, 1085.75885 (and the bare ids 54958, 114072, 75885): no hit (one 54958 hit is a GBIF taxon id in a Florida CSV, unrelated). All 685 remote research/desk-* and research/audit-* branches (d296 and audit-387 excluded), under docs/, for the same species and DOI strings: no hit. Duplicate faults 0.

## Per line

### Line 1, Strumigenys subterranea, ommatidia_count 1

Worker description, Head: "In lateral view, eye with a single facet, inconspicuous, and located at the widest level of the head (Fig. 3E)." **Quote MATCH**, figure reference included. Diagnosis "eyes with a single ommatidium" and Comments "eyes with a single ommatidia" (tool pieces) concur. Type material: holotype pinned worker only, no paratypes; label "Coloane North East Hiking Trail. 78 m, 14v–4vi.2019" and "Subterranean Trap 12.5 cm depth"; Ecology: "baited with tuna mixed with honey", "A single worker from this species has been collected so far." Conditions (holotype worker only, n = 1, baited subterranean trap 12.5 cm, dates, no queens or males) match; value stays at one individual of one caste. Location in Results, Taxonomic accounts correct.

**Line 1 MATCH.**

### Line 2, Leptanilla voldemort, none (eyes absent)

Worker description, Head: "Eyes absent." **Quote MATCH.** Holotype 1 worker, Newman, Western Australia, ca 575 m, 8 Mar. 2023, subterranean scraping; paratype 1 worker, same data; "Male and gyne unknown." No Diagnosis section; Introduction calls workers "depigmented and blind" (tool piece). Conditions match.

**Line 2 MATCH.**

### Line 3, Blepharicera gengdica, dorsal division 1/20 of ventral (male)

Diagnosis of B. gengdica, first sentence: "Compound eye with dorsal division 1/20 as large as ventral division in male." **Quote MATCH**; the sentence sits under the gengdica heading and names no other species, so the attribution is right. Male Head agrees: "dorsal division contiguous with ventral division, 1/20 as large as ventral division" (piece). Holotype male only, Gengda, Fuyuan inn, light trap, 2016.V.24; "Female. Unknown." Conditions match.

**Line 3 MATCH.**

### Line 4, Blepharicera balangshana, dorsal division as large as ventral (male)

Diagnosis of B. balangshana, first sentence: "Compound eye with dorsal division as large as ventral division in the male." **Quote MATCH**; under the balangshana heading, no comparison species named. Male Head agrees (piece). Holotype male, paratypes 5 males, 1 female, Mount Balangshan, Xiaojin County, 3281 m, 2013.VII.9; conditions match. The female Head gives the same ratio ("dorsal division separated from ventral division, as large as ventral division", piece), so the male value is not contradicted; the record does not say the female agrees (uncounted; optional addition below).

**Line 4 MATCH.**

### Line 5, Blepharicera kongsica, dorsal division 1/15 of ventral (male)

Diagnosis of B. kongsica, first sentence: "Compound eye with dorsal division 1/15 as large as ventral division in male." **Quote MATCH**; under the kongsica heading, no comparison species named. Male Head agrees: "dorsal division contiguous with ventral division, 1/15 as large as ventral division" (piece). Holotype male, paratypes 1 male, 7 females, Kongse, Daofu County, 2976 m, 2013.VIII.5; conditions match on the types.

Error (omitted variation, sex): the Female Head of the same species prints "dorsal division separated from ventral division, as large as ventral division" (piece; "about 14 rows of ommatidia" in the dorsal division, tool summary). The female eye is not 1/15, and seven of the nine type specimens are female. The conditions say only that the Diagnosis sentence is about the male, which leaves a reader free to assume the female is similar or unknown. Fixable.

**Line 5 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Strumigenys subterranea, 1 facet per eye | MATCH | none | quote MATCH (20); holotype worker only, n = 1, as stated |
| 2 | Leptanilla voldemort, none | MATCH | none | quote MATCH (2); holotype + paratype workers, male and gyne unknown |
| 3 | Blepharicera gengdica, 1/20 (male) | MATCH | none | quote MATCH (13); gengdica Diagnosis, not a comparison; female unknown |
| 4 | Blepharicera balangshana, equal (male) | MATCH | none | quote MATCH (13); balangshana Diagnosis; female same ratio (unstated, uncounted) |
| 5 | Blepharicera kongsica, 1/15 (male) | FIXABLE | conditions | quote MATCH (13); female Head "as large as ventral division" omitted |

Errors 1 of 5 audited records (20%). By kind: quotes 0; value meaning 0; omitted variation 1 (line 5); sample composition 0; bibliographic 0; licence 0; names 0; trait key 0; duplicates 0. Fixable; nothing unfixable, nothing held out. Verdict: merge lines 1-5 with the Replacement applied (line 5 required; lines 1 and 4 optional).

Unchecked: figures not viewed; the Blepharicera male and female Head sentences were returned as pieces only (rows of ommatidia for the kongsica female rest on a tool summary); the record url article_preview.php?id=54958 was not opened; no checklist opened for current status of the five names.

## Replacement

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 5:
- `conditions`: "the Diagnosis sentence is about the male" -> "the Diagnosis sentence is about the male; the female differs: the Female Head prints \"dorsal division separated from ventral division, as large as ventral division\", so the 1/15 ratio is male only"

Line 4 (uncounted):
- `conditions`: "the Diagnosis sentence is about the male" -> "the Diagnosis sentence is about the male; the Female Head gives the same ratio (\"dorsal division separated from ventral division, as large as ventral division\")"

Line 1 (uncounted):
- `source.url`: "https://zookeys.pensoft.net/article_preview.php?id=54958" -> "https://zookeys.pensoft.net/article/54958/download/xml/"
