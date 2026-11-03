# desk-d527 progress

Angle: new open papers with species-level echolocation parameters (sense_echolocation, evidence_kind physiological_response, one record per parameter). 13 records (log docs/views/evidence/desk-d527.jsonl). check.py: 0 problems (plain and --require-evidence-kind). About 38 WebSearches.

## Filed
- Dai et al. 2023, Frontiers in Ecology and Evolution 11: 1108514 (10.3389/fevo.2023.1108514): Rhinolophus osgoodi peak frequency 91.27 +/- 0.75 kHz (n = 28), Table 3 row. MDD page https://mammaldiversity.org/taxon/1004723 opened (Sanborn, 1939). Same row as the desk-d526 records.
- Thong et al. 2022, Diversity 14(4): 258 (10.3390/d14040258), Table 3 (iFM, tFM, PD; n = signals): Myotis hasseltii (first harmonic, n = 49), Myotis pilosus (first harmonic, n = 14), Taphozous melanopogon (second harmonic, n = 10); 9 records. MDD pages opened for all three. Table 3 prints no units (inferred kHz and ms, stated in each record).
- Caruso et al. 2022, Frontiers in Remote Sensing 3: 987105 (10.3389/frsen.2022.987105): Neophocaena phocaenoides click duration 90 +/- 23 us, peak frequency 123.6 +/- 4.4 kHz, centroid frequency 130.7 +/- 3.8 kHz (n = 2,654 clicks pooled over 51 files, eight stations); 3 records, the 46-word sentence cut with [...] marks.

## Weak spots
- All text through the WebFetch page reader (fragments joined; Table 3 cells flattened). Crossref was refused (PROVENANCE_REQUIRED), so no Crossref licence check; licence sentences are those the reader returned from the publisher page, possibly cut.
- Thong 2022: byline truncated on the MDPI page; full 11-name list from the Tuebingen repository record, which says it does not confirm byline order. n counts signals, not bats; recording situations are mixed.
- Neophocaena: peak frequency is not defined in the paper's Methods; the n is clicks, not animals.

## Not filed and why
- Thong et al. 2021 Diversity 13(8): 376: ranges only (R. marshalli CF2 43.5-45.6 kHz n = 12), no mean row, licence sentence absent on page.
- Zahn et al. 2021 Sci Rep 11: 22141 (beluga peak 68.7 +/- 10.1 kHz, narwhal 43.7 +/- 7.8 kHz): the one sentence holding the values is over 40 words, Table 2 cells not readable, no licence sentence on the page and Crossref refused.
- Tan et al. 2022 Animals 12: 3490 (R. ferrumequinum, sex split): two unlabelled tables through the reader, no n per row, column meaning unclear.
- Wang et al. 2022 Front Mar Sci 9: 915668 (Sousa chinensis train Fp): no licence sentence on page; species already on main from another DOI.
- Surlykke et al. 2013 (Trachops cirrhosus): the +/- is not said to be SD or SEM; Jakobsen 2013 and Brinklov 2013 are reviews or give ranges only; Vanderelst 2013 R. formosae: 'about 43 kHz' only; Lin et al. 2022 H. armiger: no per-population means; Kotila 2022: aggregate over 226 species; Sol 2024 and Gracic 2025: no species-level parameters.
- Not reachable: Leiser-Miller 2021 (Wiley), Rhinolophus affinis colonies Guo 2026 (Wiley), Lonchorhina aurita RSOS 182165 (Royal Society); Wiley and Royal Society refuse the reader.
- Swiftlet search returned only reviews and old non-open papers.

## Desk disposition after audits 1071, 1072 and 1073 (3 November 2026)
Audit 1071 (lines 1-4): 3 errors, 27 faults (Thong 2022 lines omitted the "three selected sound sequences" restriction and the contrast with published values; the quote lost parentheses the page does not print; stale "not on main" lead; incomplete licence quote). Audit 1072 (lines 5-10, Thong 2022): 6 errors, one shared cause (a tenth author "Luong NT" built from initials that no page names; the Tuebingen record lists 10 names, not 11). Audit 1073 (lines 11-13, Caruso 2022): 3 errors (omitted design confound: source position not considered, no on-axis selection) and 12 faults. All fixed from replacement blocks; all 13 records merged, none dropped.
