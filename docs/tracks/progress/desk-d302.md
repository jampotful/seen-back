# desk-d302: eye states and facet counts of soil, litter and cave beetles in CC BY new-species papers, 6 records

Branch research/desk-d302 from origin/main. About 40 WebSearches (2 extended), WebFetch only on URLs returned by a search (Crossref single-DOI lookups via api.crossref.org/v1/works, one at a time because parallel calls were rate limited). `python3 -I tools/senses/check.py | grep 'd302\.'`: 6 records, 0 problems. New trait note: ommatidia_count is not in the check.py list but is already used on main; the records say "New trait" in the note and log a facet count (the papers print "facets"; one facet per ommatidium is an assumption stated in the note).

Repeat check after filing: grep of main docs/ (whole tree) by species and DOI for all six, and git grep over every origin/research/desk-* and audit-* branch (docs/views/evidence and docs/tracks/progress) for Dayao, tendothorax, zhouchaoi, gejzadunayi, Wanoblemus and ponoricum: no hits (Duvalius appears only in desk-d287.md, which dropped ZooKeys 278 as unreadable). A final run over the remaining DOI strings on all branches was still running at commit time; main shows none.

Filed (docs/views/evidence/desk-d302.jsonl):
1. Dayao emeiensis (Staphylinidae, Pselaphinae), "Eyes each composed of about 15 facets." female sentence; holotype male, paratype female; male about 25, a Notes female about 20; ZooKeys 275.
2. Linan tendothorax (Staphylinidae), "Eyes each composed of about 16 facets." female sentence; 3 males and 14 females sifted from litter; male about 17; ZooKeys 251.
3. Batrisodes zhouchaoi (Staphylinidae), "Each eye composed of about 55 facets." male only (2 males, female unknown), from ant colonies; ZooKeys 694.
4. Duvalius gejzadunayi (Carabidae, Trechini), "Eyes completely reduced, in some specimens present as a dark spot."; holotype male, 6 male and 7 female paratypes; key says "eyes totally absent", Diagnosis "anophthalmous", Abstract "totally reduced eyes"; ZooKeys 278.
5. Wanoblemus huangshanicus (Carabidae, Trechini), Diagnosis sentence "A rather small eyeless trechine beetle, ..."; Description has no eye sentence; 33 type specimens of both sexes; ZooKeys 923.
6. Protopholeuon (Pachyandrus) ponoricum (Leiodidae, Leptodirini), "Head: Longer than wider (HL/HW: 1:1.18), non-retractable, without eyes (Figure 6J,K)."; holotype male plus 12 paratypes; Insects 16(8) 806; page prints no licence sentence (metadata CC BY 3.0), Crossref CC BY 4.0 vor.

Dropped:
- On main or other branches already: Ptomaphaginus troglodytes (ZooKeys 749), Geopselaphus bullonorum (d282, Subterranean Biology 43), Domene lizeyui (ZooKeys 1216).
- Eye sentence over 40 words or only a clause: Ptomaphaginus troglodytes (41 words, filed elsewhere anyway), Jujiroa inexpectata ("eyes very small, slight convex" inside a longer sentence), Tribasodites spinacaritus male sentence (over the tool limit), Euconnus imparitus and E. magnoculus (ZooKeys 1231, head sentences returned only as paraphrase).
- Arrived in pieces: Oodinotrechus (Pingleotrechus) yinae (ZooKeys 545, "Head anophthalmic, ...", returned as two quotes).
- No species-level eye sentence: Anillinus relictus and A. felicianus (ZooKeys 1016, description has no eye wording; CC0), Beronaphaenops paphlagonicus (eye text in genus description only), Shenoblemus minusculus (Diagnosis sentence is long), Harden and Caterino Appalachian Anillini (ZooKeys 1209, XML ends before the species descriptions), Exocelina saltusholmesensis (Subterranean Biology 19; eye length measurement and "small", holotype female only, not an eye-state value), Duvalius semecensis tarensis (subspecies; "composed of a few (5-8) ommatidia").
- Not new species: Leptotyphlus kovaci male (ZooKeys 509), Andújar et al. raymondionymine phylogenomics (no new species).
- Licence or access: Tychobythinus antojandro, Chenotrechus and relatives (Zootaxa, not open), zobodat, Plazi and repository copies not used.
- ZooKeys 1016 and 61397 PDF links were refused (PROVENANCE_REQUIRED) and not retried.

Retrieval notes: species-id.net wiki pages (Pensoft) led to the Pselaphodes-complex papers; article_preview.php pages returned the type lists and the eye sentences in tabular form, with a second pass on the XML or preview for each filed sentence. One fetch (zookeys id 142538 preview) returned a different article's text and was discarded.
