# Requote chunk 3, 17 October 2026

Work list: `docs/views/repair/chunks/chunk-3.jsonl` (97 lines). Output: `docs/views/recheck/recheck-43.jsonl`.

Counts: fixed 63, retracted 0, table rows 20, unfixed 14.

## Fixed (63, action "correct")

- Emerling 2017, Mol Biol Evol 34: 666-676 (Whittier PDF, opened through WebFetch): oa-1:9284-9302, 9305-9307, 9312, 9321, 9326-9352, 9377, 9378, 9382, 9383, 9384. Sentence text came from targeted WebFetch extractions, which returned each sentence in short pieces; the pieces were joined without gaps. oa-1:9377, 9382, 9383 and 9384 sit in sentences over 40 words and carry a clause-bounded excerpt with every cut marked by an ellipsis and described in `where`.
- oa-1:9296-9301: grade changed from m to g, because the sentence covers all four turtle species together (audit 32 row 19). Other rows quoting an "all four crocodylian species" sentence (9312, 9321, 9326, 9328-9335, 9336-9351) keep grade m; the desk may want to review those on the same logic.
- oa-1:9336-9351: the sentence opens "Both genes" and the genes are not named inside it; the record's trait and value stand, but the quote depends on the preceding sentence for its referent.
- Lariguet and Dunand 2005, J Mol Evol (rero.ch PDF): oa-2:9552, 9553, 9554, 9555, 9558. oa-2:9558 `where` corrected to p.560. oa-2:9555 keeps the "ﬁ" ligature of the original record.
- Frontiers in Plant Science 2016 (Viscum album): harvest-c4:38. The sentence is in a figure caption in the Results, Circadian Rhythm subsection; the page extraction named Figure 8, the old `where` said Figure 4 and Table 3, so `where` now says "figure caption" only.
- Bristol research-information record of the cuttlefish polarisation paper (Curr Biol 22): oa-5:1257.

## Table rows (20, nothing written)

Table of microspectrophotometry peaks, p. 669 (rows of "species | cone class | nm"): oa-1:9354, 9355, 9356, 9357, 9359, 9360, 9361, 9362, 9363, 9364, 9366, 9367, 9368, 9369, 9370, 9372, 9373, 9374, 9375, 9376.

## Unfixed (14)

- oa-2:3963, 3964, 3965, 9012 (Karl et al. 2018, Exp Eye Res, caiman): PMC page stops at a browser check; the OUCI page has no abstract. oa-2:9012 also has `where` "4.3" and a value 5.3 that could not be checked.
- oa-1:8662, 8663, 8664 (Argiope amoena, Cell Tissue Res): no page with the abstract came back from search; the Springer search hit was a different paper (scorpion).
- harvest-c3:108, 109 (Potentilla norvegica, Plant Physiol 68: 1385): PMC page stops at a browser check; Europe PMC URL was refused by the fetch tool.
- oa-5:1254, 1255 (Peichl, Mus and Apodemus, Cell Tissue Res): search returned no page carrying the abstract.
- harvest-c1:58 (Vaccinium myrtillus, Plant Cell Environ): the repository page redirected to a host the fetch tool would not open; Wiley mirror hits were proxies and were not used.
- harvest-c2:21 (Castilleja tenuiflora review, Plants 14: 2029): PMC page redirected to an unopened host; the MDPI page returned was the review report only.
- harvest-c3:62 (Asclepias curassavica, J Pollination Ecology): the article page carries only the abstract ("primarily during daylight hours"); the quoted phrase is in the PDF body, which was not reachable.
