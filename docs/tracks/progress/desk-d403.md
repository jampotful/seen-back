# desk-d403 progress

Angle: spider eye-size sentences, more new papers. 60 records from three open Pensoft papers (log docs/views/evidence/desk-d403.jsonl). check.py and check.py --require-evidence-kind: 0 problems for this file.

## Filed
- ZooKeys 1218: 251-286 (10.3897/zookeys.1218.135249; Zamani, Kaya, Marusik 2024; Agelenidae): Maimuna antalyensis (M, F), Tegenaria ballarini (M, F), T. beyazcika (M only; female unknown), T. egrisiana (M, F), T. hoeferi (M, F). 36 records, sensory_anatomy (sentence prints 'Eye sizes:'; Methods give no eye dimension). Description labels read only 'Male.' and 'Female.' with no specimen code, said in each record.
- ZooKeys 1224: 175-186 (10.3897/zookeys.1224.135572; Guo, Li, Zhang 2025; Clubionidae): Clubiona longyangensis and C. multiprocessa, male holotype and female paratype each. 16 records, eye_diameter_mm (Methods sentence 'Eye diameters as AME, ALE, PME, PLE and interdistances as ...'; the eye sentence itself prints 'Eye sizes').
- ZooKeys 1183: 205-217 (10.3897/zookeys.1183.113075; Xu, Mu, Zhang, Zhang 2023; Phrurolithidae): Grandilithus chongzuo, male holotype and female paratype. 8 records, sensory_anatomy.

## Weak spots
- Fetch tool returns short pieces; type blocks for ZooKeys 1218 are partly summaries (paratype lines not verbatim), some neighbouring sentences cut by the tool (marked).
- eye_diameter_mm for Clubiona rests on a Methods sentence that lists the eye numbers as 'Eye diameters'; no sentence says how the diameter was taken. Owner may prefer sensory_anatomy.
- Clubiona: HTML preview prints no Order/Family heading; XML returned 'Araneae' and 'Clubionidae' without authorities.
- WSC opened: Tegenaria ballarini (70752), T. beyazcika (70753), Clubiona longyangensis (71177), C. multiprocessa (71178), Grandilithus chongzuo (62393), all accepted. Not opened (UNCHECKED): Maimuna antalyensis, Tegenaria egrisiana, T. hoeferi.
- Crossref queried one paper at a time for all three DOIs (vor, CC BY 4.0).

## Not filed and why (leads)
- Grandilithus xiaohuangshan and G. lanxi (ZooKeys 1183, both sexes, values retrieved, 16 more records): left out by the 60-line cap.
- Otacilia tongboshan (BDJ 13 e144804, Phrurolithidae, Jiang et al. 2025): male eye sentence seen in summary only, not filed.
- Zodariidae EJT 1016: only the sciencepress.mnhn.fr abstract page reached, no full text. Stethorrhagus EJT 1013 (Corinnidae, excluded family anyway): view page reached (CC BY 4.0), PDF links not in search results, download URL failed. Cheiracanthium EJT 900: searches returned only Plazi/Zenodo/DOAJ copies; no journal page.
- Oonopidae ZooKeys 1052 and EJT 748 (Trilacuna): no per-eye measurements. Philodromidae ZooKeys 1221 Sinodromus already on main (desk-d395/396).

## Desk disposition after audits 670 to 677 (2 November 2026)
Eight fresh Opus audits covered all 60 lines. Errors counted: audit 675 eight (C. longyangensis female and C. multiprocessa male: the printed "Clubiona corticalis group" heading missing from where), audit 676 eight (C. multiprocessa female paratype: same missing heading; plus licence cut and a false Crossref claim on the Grandilithus lines, counted as faults). Audits 670, 672, 673, 674 and 677 counted 0 errors. Audit 671 labelled all eight T. ballarini lines errors for the false Crossref claim; the desk counts it as a text fault, as audit 665 did, so it is not in the yield. Ruling by audits 674, 675 and 676: the ZooKeys 1224 Methods sentence "Eye diameters as AME, ALE, PME, PLE and interdistances as AME-AME, AME-ALE, PME-PME, PME-PLE." counts as a diameter definition, so eye_diameter_mm stands for the Clubiona lines (it does not say how the diameters were taken). ZooKeys 1218 and ZooKeys 1183 define no eye dimension and "diameter" never appears (sensory_anatomy stands). Maimuna antalyensis: the paper prints one male holotype and ten female paratypes. Text faults fixed on all lines: false Crossref claims removed, cut licence sentences completed, paratype blocks that were tool summaries replaced by printed text, the author initials of Marusik normalised, WSC pages now cited (all accepted: Agelenidae, Clubionidae). All 60 lines replaced with the auditors' text; no quote changed; nothing dropped. Open: Crossref not read for any of the three papers; Grandilithus xiaohuangshan and G. lanxi (ZooKeys 1183) and Otacilia tongboshan (BDJ 13 e144804) still unfiled leads.
