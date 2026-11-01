# desk-d292: spider eye states and counts in Pensoft CC BY papers (Telemidae, Dysderidae, Agelenidae, Nesticidae), 15 records

Branch research/desk-d292 from origin/main. About 40 WebSearches (2 extended) plus fetches. `python3 -I tools/senses/check.py | grep 'd292\.'`: 15 records, 0 problems. Quote lengths 2 to 14 words. Crossref read for all five DOIs (author order matches the pages; all CC BY 4.0 vor). Every page URL fetched was returned by a WebSearch first. Whole-docs grep on main and all research/desk-* and audit-* evidence and progress files, by genus and DOI: no repeats. Where a sentence names no species, `where` gives the treatment.

Filed (docs/views/evidence/desk-d292.jsonl), all Araneae:
1-3. Pinelema damtaoensis (six eyes), P. laensis (six eyes), P. nuocnutensis (four vestigial eyes), ZooKeys 734. Male holotype sentences; the female sentences are quoted in conditions.
4-5. P. pacchanensis, P. zhenzhuang: "Eyes absent." male holotype; the female Description has no eye sentence (stated in conditions), ZooKeys 734.
6-8. P. cunfengensis (six eyes), P. podiensis (white spots), P. qingfengensis ("entirely reduced"), ZooKeys 692. Male holotype only; female Descriptions have no eye sentence.
9-10. Dysderocrates kibrisensis ("Eyes well developed") and Harpactea kalavachiana ("Eyes reduced"), female holotypes, males unknown, ZooKeys 825.
11. Troglocoelotes sinanensis, eyes strongly degenerated, female holotype, BDJ 11.
12-13. Typhlonesticus angelicus (female holotype) and T. santinellii (male holotype), eyes reduced, no corneal lenses visible, Arthropod Systematics & Phylogeny 81.
14-15. Eye diameter lines (AME, ALE, PME, PLE) for T. angelicus female holotype and T. santinellii female paratype; new trait eye_diameter_mm (as d291), units from the Methods sentence "All measurements are given in mm."; the labelled line is not a table row and prints no unit.

Dropped:
- Ochyrocera ritxoco, O. ritxoo (ZooKeys 1031): on main. Ochyrocera varys, atlachnacha, laracna, aragogue (ZooKeys 726): sentences give eye shapes, no count or state.
- Hahnia jiangkou (BDJ 11 e113400): "Eye sizes: AME 0.06, ..." the paper does not say whether sizes are diameters.
- Speleoticus hei (BDJ 11 e107751): female diameter line reached the tool in two pieces; "all eight eyes" is an item (3) of a list, starting mid-sentence.
- Euscorpiops lii (ZooKeys 968): the lateral-ocelli sentence reached the tool as two clauses. Chaerilus pseudoconchiformus (ZooKeys 495): no median count, "a pair of lateral eyes" ambiguous.
- Orchestina (ZooKeys 1249, ZSE 100): eyes "well developed, PME largest" only as fragments; Trilacuna (EJT): no counts. Leptonetidae (ZooKeys 1247): "Eye sizes and interdistances" labels only. Callosa (BDJ): description not on page.
- Merizocera (ZooKeys 961): no eye text on the page returned. Selachochthonius naledi: on main. Iandumoema smeagol: on main. Spaeleoleptes (EJT 2409), Orphnaecus pellitus (SB 52): no usable eye sentence or only a comparison caption.
- Mekonglema, Troglohnia, Typhlohnia, Sinoderces, Telemidae revision (ZooKeys 933): Plazi, Zenodo or optimap copies only, or no page returned; not used.
- Harvestmen, whip spiders, mites, scorpions beyond the above: searches returned only Plazi, Zenodo, PMC, closed or non-open-access journals; nothing filed.
- Fetch oddity: three article_preview ids (24432, 38967, 38653) returned the text of a previous page; nothing from them used.

Names: no checklist opened; each species is described as new in the cited paper.

## Desk disposition after audits 382 and 383

Audit 382 (lines 1-8): 1 error (line 1, wrongly called a cave spider). Audit 383 (lines 9-15): 2 errors (lines 14 and 15, empty where). All fixed with the auditor replacements; all 15 merged.
