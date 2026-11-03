# desk-d513 progress

Angle: non-spider unit (reptiles and amphibians; no spiders searched or filed). Open-access Pensoft papers that print eye diameter in millimetres per named specimen. 10 records (log docs/views/evidence/desk-d513.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement. check.py: 0 problems for desk-d513 (plain and --require-evidence-kind). About 27 WebSearches.

## Filed
- ZooKeys 1227: 349-367 (10.3897/zookeys.1227.131357) Amolops gudao (Ranidae): holotype KIZ 053662 and 3 paratypes, Table 1 ED row (caption gives mm; Methods define ED as the distance between corners of the eye). ASW page opened from my own search.
- ZooKeys 1197: 93-113 (10.3897/zookeys.1197.104851) Zhangixalus thaoae (Rhacophoridae): holotype and 2 paratype males, Table 3 ED row (caption gives mm). ASW page opened.
- Zoosystematics and Evolution 100(3): 897-911 (10.3897/zse.100.125798) Calamaria berezowskii: lectotype ZISP 8823, GXNU DLR194 and DLR195, Table 4 'EyeD (mm)' row. Reptile Database page opened.

## Unfiltered title searches that reached the full text (tested)
- 'Amolops gudao sp. nov. ZooKeys 1227 new species torrent frog' returned article_preview.php?id=131357 and the ASW search 'Amolops gudao Yu, Wu, Lu & Che 2025 Amphibian Species of the World' the ASW page.
- '"Zhangixalus thaoae" new green treefrog species from Vietnam zookeys article_preview' returned article_preview.php?id=104851 (the XML hit alone lacked Table 3).
- 'Calamaria berezowskii Zoosystematics and Evolution 100 redescription' returned article_preview.php?id=125798; 'Calamaria berezowskii Günther 1896 Reptile Database' the Reptile Database page.

## Weak spots
- All text came through the WebFetch page reader; table rows and column-to-code mappings are its cell-by-cell reading; long sentences came back in pieces and were joined. Crossref licence not checked; licence sentences are the page-printed CC BY 4.0 sentence.
- Calamaria berezowskii: the paper is internally inconsistent. Lectotype and DLR195 descriptions say EyeD is 'larger than' eye-mouth distance although the numbers (0.7 vs 1.0, 0.7 vs 1.1) and the Diagnosis say smaller; the Variations section swaps the sexes of DLR194 and DLR195 against Table 4 and the Methods list. I filed only the Table 4 cells (with Table 4 and Methods sexes) and recorded both faults in the note. If an auditor judges the contradiction unresolved, drop lines 8-10. Caption attributes lectotype and syntype data to Gunther (1896) and Orlov.
- Reptile Database family for Calamaria is Colubridae (paper title also prints Colubridae); no page prints an explicit 'valid'.

## Not filed and why
- Zhangixalus matsuii (ZooKeys 1294): no ASW page reached and the header/Table 1 conflict on IB A.6606 and A.6598 was not resolved; not searched further.
- Trimeresurus liqibini (ZSE 102(1): 303-314, CC0, ED 3.54 and 2.94): desk-d475 on main records a paper synonymising it with T. loong, and no Reptile Database page for it was reached; held out. T. loong is already on main (d477).
- Cyrtodactylus makwanpurgadhiensis/C. chure (ZooKeys 1253: 131-160), Gekko tesselatus (ZSE 101(4)), Calamaria incredibilis, C. arnei: already on main. Cyrtodactylus pecelmadiun, Hebius ngoclinhensis: Zootaxa, no open page. Scincella ngati: eye length, not ED (d459). Boulenophrys daxuemontis (BDJ 13 e153987): not reached beyond the blog this session; d455 lead stands.
- Fish: two searches (loach/barb/catfish tables; Evolutionary Systematics) returned only Plazi treatments, Zootaxa and a Raffles Bulletin PDF; nothing with a per-specimen ED row in mm and an open page was reached within budget.

## Desk disposition after audits 1032-1033 (3 November 2026)
Audits judged 10 lines with 0 value errors and 24 text faults (authority in the where-path, heading path, summarised caption, missing sampling data, an XML claim the article does not print), all corrected from the auditors' replacement blocks. Audit 1033 confirmed the unit's resolution of the Calamaria berezowskii eye versus eye-mouth contradiction (printed EyeD 8.8%/8.4% of HL matches 0.7 mm). Nothing dropped. 10 records merged (Amolops gudao 4, Zhangixalus thaoae 3, Calamaria berezowskii 3).
