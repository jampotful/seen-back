# desk-d270 progress note

Records filed: 9 (docs/views/evidence/desk-d270.jsonl), all MDPI Insects, all from the paper page with Crossref single-DOI lookups giving CC BY 4.0 vor (pages print no licence sentence, metadata CC BY 3.0). check.py: 0 problems.

- Arge similis (Wen et al. 2022, Insects 13(2): 152, 10.3390/insects13020152): ommatidia_count male 2022 and female 2223 (abstract sentence, mean ± SE labelled); facet_diameter_um male 17.40 and female 18.26 (Section 3.1; trailing table reference cut and marked). Sexes kept as separate records. n = 3 per sex for SEM; adults lab-emerged from wild-collected larvae.
- Ceratosolen gravelyi (Xie et al. 2025, Insects 16(7): 682, 10.3390/insects16070682): ommatidia_count [228, 263] (abstract). Interommatidial angle for this paper already on main (sweep-66); facet diameter (9.3 to 13.5 um) held because the Results sentence is over 125 characters and the end could not be seen.
- Histia flabellicornis (Chen et al. 2025, Insects 16(8): 771, 10.3390/insects16080771): ommatidia_count "over 2000", facet_diameter_um female 24.45 and male 24.43 (n = 8 each, no significant difference), interommatidial_deg 4.08 (calculated D/R). Quotes assembled from fetch pieces; tails and final punctuation checked in a third pass. Lead was held by desk-d187 for name authority; Wikipedia and insecta.pro pages (Fabricius, 1775) seen in a search; species not in gbif-names.tsv.
- New trait keys used with "new trait" note: ommatidia_count, facet_diameter_um (both already in use on main).

## Held leads
- Lymantria xylina Insects 16(11): 1122: interommatidial_deg already on main (recheck-2, with ommatidia counts in its conditions); not refiled.
- Insects 17(2): 167 (insect eye review): review, not filed.
- Retinal ganglion cell topography papers (Hypomesus nipponensis J Anat; Hexagrammos octogrammus J Fish Biol; Port Jackson shark J Comp Neurol; Tripterygion delaisi on PMC): Wiley or PMC hosts, not opened (Wiley paywalled or refused; PMC refused). Not checked for open licence.
- Temnothorax albipennis ommatidia count (Sci Rep, nature.com): not retried.

## Queries that worked
- "number of ommatidia per eye worker ants compound eye Insects MDPI micro-CT facet count open access" (extended) returned two MDPI Insects eye-structure pages; "Insects MDPI ommatidia interommatidial angle compound eye ..." surfaced Histia. mdpi.com opens; Crossref single-DOI via WebFetch answered one page at a time (concurrent fetches were rate-limited).

## Owner questions
- Is a quote that ends with a cut-marked "[…]" for a trailing table reference acceptable (Arge facet records)?
- Per-sex records for sexes reported in one sentence: acceptable, or one record with both values?

## Desk disposition after audits 362 and 363
Audit 362 (lines 1-4, Arge similis): 0 errors; optional condition, unit and quote-ending edits applied. Audit 363 (lines 5-9): line 5 (Ceratosolen) fixable and fixed; lines 6-8 matched (SE/test text added); line 9 (Histia interommatidial_deg 4.08) held out as a repeat of desk-d215 on main. 8 filed.
