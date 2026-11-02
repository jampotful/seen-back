# desk-d402 progress

Angle: spider eye-size sentences, more new papers. 40 records from three open papers (log docs/views/evidence/desk-d402.jsonl). check.py and check.py --require-evidence-kind: 0 problems.

## Filed
- EJT 947: 109-129 (10.5852/ejt.2024.947.2623; Korai and Jaeger 2024; Sparassidae): Heteropoda bawanglingensis, female holotype, AME/ALE/PME/PLE, 4 records, sensory_anatomy (Methods define no eye dimension). Lead from desk-d401; WSC page opened (accepted).
- BDJ 13: e144222 (10.3897/bdj.13.e144222; Liang, Liu, Yin, Xu 2025; Theridiidae): Episinus anfu (F holotype), E. implicatus (F holotype), E. pseudonubilus (M holotype, F paratype HNU819), 16 records, eye_diameter_mm (Methods: 'Eye diameters were taken at the widest point.'). Filed under the current WSC names Asiopisinus anfu, A. implicatus, A. pseudonubilus (transferred 2025-07-12); printed name given in conditions.
- EJT 968: 156-173 (10.5852/ejt.2024.968.2725; Liang, Yin, Xu 2024; Theridiidae): Meotipa lingulata (F holotype), M. pseudomultuma (F holotype, M paratype), M. tortuosa (F holotype, M paratype), 20 records, eye_diameter_mm (same Methods sentence).

## Weak spots
- Fetch tool returns short pieces; eye sentences joined from two pieces, neighbouring sentences and type blocks as returned (some truncated by the tool, said in conditions). Hyphen vs en dash in interdistance labels follows the tool output.
- Episinus type blocks are Darwin Core field lists; pseudonubilus paratype list condensed by the tool.
- Crossref version of record not read for any of the three papers (DOIs verified only as appearing in Crossref list queries); licence sentences from the tool (BDJ sentence truncated).
- Meotipa WSC: reference 18030 included-taxa page opened, no status word; species page 70671 not opened (UNCHECKED).

## Not filed and why (leads)
- Zodariidae EJT 1016 (Shafaie, Pekar, Osman 2025, DOI 10.5852/ejt.2025.1016.3063): article view page 3063 reached (CC BY 4.0), but the download URL from the search results (with trailing slash) failed; no full text read.
- Stethorrhagus EJT 1013 (12 new species; Xavier, Brescovit, Bonaldo 2025): download URL in search results failed; Cheiracanthium EJT 900 (Li and Zhang 2023): only view page reached, PDF link not in search results; Psechrus EJT 1081 (2026, four species): download URL in results (trailing slash) not tried after the same failure pattern.
- Yunguirius ZooKeys 1211 (Agelenidae, four females, 'Eye size and interdistance' printed): Methods print no unit for measurements; skipped rather than file UNITS NOT PRINTED.
- Oonopidae (ZooKeys 1286 Ischnothyreus) and Psilodercidae (ZooKeys 886, 862): descriptions print no per-eye measurements.

## Desk disposition after audits 665 to 669 (2 November 2026)
Five fresh Opus audits covered all 40 lines. Errors counted: audit 665 eight (lines 1 to 4 H. bawanglingensis where-path dropped every printed authority and the "Measurements" sub-heading; lines 5 to 8 A. anfu conditions gave the wrong next sentence, the page prints "Clypeus height 0.28."), audit 667 four (lines 21 to 24 M. lingulata where-path omitted Class Arachnida Cuvier, 1812 and Order Araneae Clerck, 1757), audit 668 eight (M. pseudomultuma, same omitted Class and Order headings). Audits 666 and 669 counted 0 errors; audit 669 found the same omitted Class and Order headings on M. tortuosa and listed them as fixable faults, not errors, so the count is inconsistent across auditors and the same fault is counted in 667 and 668 but not in 669. The desk's own flag wrongly called Meotipa an Araneidae genus: the World Spider Catalog places it in Theridiidae (audits 668, 669). Methods read whole: BDJ 13 e144222 and EJT 968 print "Eye diameters were taken at the widest point." with mm (eye_diameter_mm stands); EJT 947 prints no diameter definition (sensory_anatomy stands). Text faults (cut licence sentences, "inter-distances" for printed "interdistances", paraphrased Methods, wrong grep claim) fixed. All 40 lines were replaced with the auditors' text; no quote changed; nothing dropped. Open: Crossref not reached for any of the three papers; the BDJ taxon field carries the WSC name Asiopisinus (printed Episinus), citing the transfer "Hu et al., 2025a"; Meotipa species pages on WSC not opened by the desk.
