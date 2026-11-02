# desk-d318: eye states of Psychodidae, a brachypterous braconid, an enicocephalid bug, two polyclads and two syllids, 14 records

Branch research/desk-d318 from origin/main. About 38 WebSearches; WebFetch only on URLs returned by searches, plus Pensoft article XML at /article/ID/download/xml/ for IDs seen in search results or in Crossref list results, and Crossref single-DOI lookups (one at a time; list queries were rate-limited several times and not worked around). `python3 -I tools/senses/check.py | grep d318`: 14 records, 0 problems. Traits: eye_bridge_width_facets (7; note says "new trait" as check.py requires, key already on main from d297), eye_type (7).

Crossref answered for every DOI filed (10.3897/zookeys.1259.153178, 1296.199004, 1278.183769, 584.8319, 918.47061, 864.33955, 796.24538, 10.3897/BDJ.12.e116082, 10.5852/ejt.2024.935.2547): all vor CC BY 4.0 except the EJT paper (content version unspecified; the PDF prints the CC BY 4.0 licence sentence).

Repeat check: a text index of origin/main docs/ plus the evidence and progress files of every unmerged desk and audit branch (built once, 1 Nov 2026); every species and DOI was grepped before filing.

Filed (docs/views/evidence/desk-d318.jsonl):
1-2. Brunettia sinensis and B. zunyiensis (Psychodidae), Diagnosis sentences, 3 facet rows (ZooKeys 1259).
3-4. Thornburghiella sichuanensis (6 rows) and T. yintiaolingensis (5 rows), Diagnosis sentences (ZooKeys 1296).
5. Trichomyia sinensis, "eyes without eyebridge", male (ZooKeys 1278).
6. Keylimepie peckorum (Braconidae), "Eye small, its height 0.6 × head height.", brachypterous female (ZooKeys 584).
7-9. Eugenys micra, E. singularis, E. upsilon (Psychodidae), Head sentences with three, three and two-to-three facet rows (European Journal of Taxonomy 935).
10. Enchiridium daidai (Polycladida), cerebral eyespot clusters of 20-52 eyespots (ZooKeys 918).
11. Paraplehnia seisuiae (Polycladida), eyespots small, embedded, invisible in life (ZooKeys 864).
12-13. Parasphaerosyllis irregulata (new species) and P. indica (holotype re-description) (Syllidae), prostomial eyes (Biodiversity Data Journal 12: e116082).
14. Xenicocephalus tomhenryi (Enicocephalidae), eyes prominent, semiglobular, female holotype (ZooKeys 796).

Dropped candidates:
- On main: Elocomosta lilizheni (Hydrophilidae, desk-d307), Cixius palmirandus and C. theseus (desk-d297), Stylochus erytheius and S. marimarensis (d300), Exocelina saltusholmesensis (dropped by d302 as not an eye-state value; not refiled).
- Sentence too long or semicolon block over 40 words: Perithreticus neglectus (BDJ 10: e81205; the Head sentence runs through the wing), Armillipora bifida and A. nawak (Evolutionary Systematics 8; only clauses returned), Bryopharsos nine new species (EJT 1001; PDF URL blocked, see below).
- No eye sentence, genus-level only, or colour only: Nesoproxius kishimotoi (head vs eyes ratio), Dryinus georgianus (ocelli ratios), Tipula spp. (eyes black), Olecryptotendipes, Amazonopsis (genus-level eyes), Amazonothops aslaki (genus-level eyes), Atheta alesi (clause pieces from a species page), Orientilla tamaderai (measurement clauses; XML blocked).
- Not reachable: Micranops bolivianus (Neotropical Entomology, Springer, PMC only), Diversity 13(3): 131 (MDPI refused), Plehnia cascaisensis and the other Iberian polyclad species of ZSE 100 (XML truncated before the descriptions).
- Not searched out: ticks, Plecoptera, Trichoptera, Lepidoptera (as instructed); Cicadellidae, Miridae, Tingidae and Reduviidae new-species papers in ZooKeys appeared but eye text there is ratios and colour; Nudibranchia and echinoderms returned no eye sentence in the results.

URLs refused with PROVENANCE_REQUIRED (not retried): mdpi.com/1424-2818/13/3/131, jhr.pensoft.net/article/110590/download/xml/, alpento.pensoft.net/article/80349/download/xml/, europeanjournaloftaxonomy.eu/.../article/view/2951/13319, and first attempts at the BDJ 81205 and evolsyst 124213 XML before search results exposed them.

Weak spots for the auditor:
- Brunettia, Thornburghiella: the quotes are Diagnosis sentences that carry the antennal spines (Thornburghiella) or only the bridge. The Description Head has the same clause inside a longer semicolon sentence. The impossible latitude 143°46'53"N is printed (noted). Thornburghiella sichuanensis: Description says a few bridges have seven rows; value is the Diagnosis 6, variation in conditions. For yintiaolingensis the Diagnosis uses a comma, not a semicolon.
- Eugenys: the Head sentences are semicolon lists of 26-33 words starting after the "Head." label; upsilon's block is labelled "Head (holotype)". Type lists read from the publisher PDF by summary; paratype counts (micra 3, singularis 1, upsilon 7: six males, one female) taken from that.
- Keylimepie: the quote is a telegraphic fragment (accepted precedent). The author "Fernandez-Triana" is filed without the accent (byline and Crossref); the citation line prints the accent.
- Trichomyia sinensis: the quote carries head dimensions; it is filed as eye_type text, not a numeric 0 for the bridge.
- Enchiridium daidai: the 20-52 range is not assigned to specimens in the text; eyespots are not ommatidia, so eye_type text is used. Class is blank for the three flatworm records (not printed).
- Paraplehnia seisuiae: the collection date was not in the text returned.
- Parasphaerosyllis: class Polychaeta, order and family come from page metadata, not text headings; the paper's own title spacing differs from Crossref's.
- Xenicocephalus: the sentence ends in a measurement; a separate later sentence (eyes in ventral view) is noted but not quoted. Class blank.
- All summaries of pages came through WebFetch summarisation; every quote was re-requested at least twice or checked against its neighbours, but none was returned as one uninterrupted text.

Questions: none.

## Desk disposition after audits 428-429
Audit 428 (lines 1-7): 1 fixable error (line 3, Thornburghiella sichuanensis seven-row sentence split across clauses), fixed; the Keylimepie quote was judged a whole printed sentence. Audit 429 (lines 8-14): 1 fixable error (line 14, class Insecta printed in the Abstract taxon line), fixed; the Paraplehnia "not read" collection date is now stated as not printed anywhere in the paper. Optional fixes applied. 2 errors in 14 (14%); none dropped. The audit-428 auditor reached the Thornburghiella page through the Crossref record because it was not in search results; no proxy or unauthorized copy was involved.
