# audit-388: desk-d297, evidence lines 1 to 5

Audited 1 November 2026 from the desk-d297 files present untracked in the worktree (docs/tracks/progress/desk-d297.md and docs/views/evidence/desk-d297.jsonl, 9 lines; neither committed here, neither edited). Line numbers are the file's (1-based). This audit judges lines 1 to 5 only; audit-389 covers lines 6 to 9. HEAD equals origin/main (a85bc4ef). `python3 -I tools/senses/check.py docs/views/evidence/desk-d297.jsonl`: "9 records, 0 problems". Quote lengths (`len(q.split())`) for lines 1-5: 5, 13, 11, 15, 12, all within 40.

Sources opened (WebFetch): subtbiol.pensoft.net/article_preview.php?id=144111 (two passes); zookeys.pensoft.net/article_preview.php?id=136907 (two passes); dez.pensoft.net/article/8432/download/xml/; Crossref single-DOI lookups api.crossref.org/v1/works/ for the three DOIs (the Subterranean Biology lookup was rate-limited once and succeeded on retry). All article URLs were returned by a WebSearch first. Plazi, DOAJ (library.kab.ac.ug), BHL, digituma.uma.pt repository copies, optimap, species-id, novataxa and news/blog hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 3 WebSearches.

## Bibliographic and licence

- Lines 1-2 (Hoch, López, Naranjo, Aguín-Pombo, Oromí 2025). Page and Crossref same order (Hannelore Hoch, Heriberto López, Manuel Naranjo, Dora Aguín-Pombo, Pedro Oromí); title identical; Subterranean Biology 51: 61-101, no issue printed or in Crossref; issued 2025-03-28; Crossref CC BY 4.0 vor; page prints the CC BY 4.0 licence sentence. Accepted. Line 1's url (article/144111/download/xml/) was not returned by my searches, so the preview page of the same DOI (returned by search) was read instead (uncounted).
- Lines 3-4 (Li, Liu, Chen, Wei, Yue, Qiu 2025). Page and Crossref same order (Ting-Ting Li, De-Xing Liu, Jian Chen, Xiao-Ya Wei, Qiao-Yun Yue, De-yi Qiu); title identical; ZooKeys 1232: 267-284, no issue; issued 2025-03-19; CC BY 4.0 vor; page licence sentence verbatim. Accepted.
- Line 5 (Hoch, Ferreira 2016). XML and Crossref same order; title identical; Deutsche Entomologische Zeitschrift 63(2): 171-181, issued 2016-06-06; CC BY 4.0 vor; XML prints the CC BY 4.0 licence sentence. Accepted. The XML prints the second author as "Rodrigo Lopes Ferreira" while the record has "Ferreira R" (Crossref gives "Rodrigo Ferreira"); main elsewhere writes "Ferreira RL" for this author (uncounted, identity unchanged; optional replacement below). The record's url (article_preview.php?id=8432) was not returned by my search; the XML copy of the same DOI was read (uncounted).

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

All five species are described as new in the cited papers; names rest on the original descriptions (Plazi treatments surfaced in search for Cixius theseus, Nocticola appendiculata, N. cordiformis and Iuiuia caeca, not opened; no checklist opened). Cixiidae/Hemiptera (lines 1-2, as in the title), Nocticolidae/Blattodea (lines 3-4, as in the title; Corydioidea not filed), Kinnaridae/Hemiptera (line 5, as in the title). Names faults 0.

## Trait key

Lines 1-5 use eye_type, an accepted key. Values are the printed states ("absent", "reduced", "well developed"). The new key eye_bridge_width_facets belongs to line 9 (audit-389).

## Duplicates

`git grep` on origin/main (a85bc4ef) under docs/ (evidence, audit/corrected, audit/ALL, sheets, searched/ included) for "Cixius theseus", palmirandus, "Nocticola appendiculata", cordiformis, Iuiuia and the DOI suffixes subtbiol.51.144111, zookeys.1232.136907, dez.63.8432: hits only for Heloecius cordiformis (crab, canon-4) and Carya cordiformis (searched/sweep-16, gaps, desk-d11); Nocticola on main appears only in docs/tracks/progress/desk-d291.md (N. gonzalezi, set aside). The 80 most recently committed remote research/* branches (d297, audit-388 and audit-389 excluded), under docs/views/evidence and docs/tracks/progress, for the same species and DOI strings: no hit. Duplicate faults 0.

## Per line

### Line 1, Cixius theseus, none (compound eyes and ocelli absent)

Head paragraph of C. theseus, sixth sentence: "Compound eyes and ocelli absent." (verbatim, ends at the period). **Quote MATCH.** Habitus sentence repeats the state, as the note says. Material examined: holotype male (IPNA), paratype female same data (DZUL 50354), one III-instar and three IV-instar nymphs same data, provisionally assigned and described as "unpigmented, eyeless cixiid nymphs" (piece); the Head paragraph carries female-specific details (rostrum, antennal plaque organs), so the state covers both sexes. Diagnosis names no eye character (tool summary). Conditions match; the nymph state agrees, so nothing contrary is omitted.

**Line 1 MATCH.**

### Line 2, Cixius palmirandus, none (compound eyes absent)

Habitus: "Strongly troglomorphic with compound eyes absent, tegmina, wings and bodily pigmentation strongly reduced." **Quote MATCH.** Head sentence begins "Compound eyes and ocelli absent," and continues with the former position of the lateral ocelli (22 words, tool summary), as the note says. Holotype male only (DZUL 50353, Cueva Honda de Miranda, La Palma, 17 Oct 2015); female unknown, no nymphs. Conditions match; value is not stretched beyond the one male.

**Line 2 MATCH.**

### Line 3, Nocticola appendiculata, reduced

Male Description: "Head: vertex of head exposed; eyes reduced; ocelli absent (Fig. 7D)." **Quote MATCH**, bold "Head:" label and figure reference printed. Holotype male ZSCTC-LI-0033, Xiaofu Village, Lingchuan County, 26 April 2024; paratypes 1 male, 1 female same data and 2 males Edi Village, Lingui District, 29 April 2024, so 3 males and 1 female as filed. Diagnosis has no eye sentence; female description does not mention eyes; eye field says adult male. Genus Diagnosis sentence "Eyes well developed, variably reduced or absent; ocelli present or absent." confirmed. Discussion: "Nocticola cordiformis sp. nov. and N. appendiculata sp. nov. were found under rocks at the roadside." Conditions match.

**Line 3 MATCH.**

### Line 4, Nocticola cordiformis, well developed

Male Description: "Head: vertex of head exposed; Eyes well developed, with heptagon concave; ocelli absent (Fig. 5F)." **Quote MATCH**, capital "Eyes" as printed. Diagnosis: "eyes well developed, while in N. xiai eyes reduced (Fig. 1B)" (piece), as the note says. Holotype male ZSCTC-LI-0028, Yanzi Cave, Edi Village, Lingui District, 13 Dec 2023; paratypes 1 male and 1 female Lingjiaodi Village 30 Dec 2023 and 2 males Edi Village 29 April 2024, so 3 males and 1 female as filed. The conditions give both the cave holotype locality and the Discussion's roadside statement, which is accurate.

**Line 4 MATCH.**

### Line 5, Iuiuia caeca, none (compound eyes absent)

Genus Description, Head: "Compound eyes absent, their former position recognizable by a shallow, vaulted area." **Quote MATCH**; next sentence "Median (frontal) ocellus absent, lateral ocelli vestigial." Species Diagnosis: "Strongly troglomorphic species, predominantly yellowish body pigmentation, compound eyes and ocelli absent." Both are recorded in the conditions and note; only the compound-eye state is logged. The genus is monotypic in this paper, so the genus-heading attribution and the 'where' are accurate. Holotype male 7 Aug 2013, paratypes 2 males same data, 5 males and 2 females 9 July 2014, Toca Lapa do Baixão, Iuiu, Bahia; conditions match. Nymphs (4th and 5th instar) were not assigned to the species and no eye state is given for them.

**Line 5 MATCH.**

## Result

Errors: 0 of 5 lines (rate 0%).

## Replacement

No fixable errors. Optional (uncounted):
- Line 5, source.authors, old "Hoch H, Ferreira R", new "Hoch H, Ferreira RL" (XML prints Rodrigo Lopes Ferreira; main's convention for this author).

## Held out

None.

## Verdict

Lines 1-5 pass; mergeable as filed, subject to audit-389 on lines 6-9.
