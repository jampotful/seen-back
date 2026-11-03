# desk-d509 progress

Angle: reptile eye_diameter_mm (no spiders). Open-licence descriptions printing eye diameter (ED) in millimetres per named specimen, with a Reptile Database species page reached from my own search results. 22 records (log docs/views/evidence/desk-d509.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement. check.py: 0 problems (plain and --require-evidence-kind). About 33 WebSearches.

## Filed
- Colubroelaps nguyenvansangi (Herpetozoa 37: 379-390, 10.3897/herpetozoa.37.e137809): ZISP 25682 (holotype, female) 0.8, ZMMU Re-15484 (male) 1.0, ZMMU Re-15485 (male) 0.8, Table 1 ED (mm) row. The Reptile Database page opened from a fresh search result (d508 was refused). 3 records.
- Cyrtodactylus santana (ZooKeys 1139: 107-126, 10.3897/zookeys.1139.96508): holotype and 9 paratypes, Table 4 ED row. Unit comes from the Supplementary material 1 note (no unit beside the table). 10 records.
- Cnemaspis umashaankeri (VZ 72: 823-837, 10.3897/vz.72.e89324): holotype and 3 paratypes, Table 1 ED row; unit from the 0.1 mm caliper sentence. 4 records.
- Lycodon truongi (VZ 72: 371-384, 10.3897/vz.72.e82201): holotype, Table 3 ED row ('All measurements are in millimeters'). 1 record.
- Bungarus sagittatus (ZSE 100(1): 141-154, 10.3897/zse.100.116601): holotype, 2 paratypes and 1 referred specimen, Table 1 ED row. 4 records.

## Not filed and why
- Lycodon anakradaya (same paper as L. truongi): Reptile Database returned 'not found' for that spelling.
- Cyrtodactylus arunachalensis (Evol Syst 5(1), 10.3897/evolsyst.5.61667): measurement is OD, and the paratype sexes in Table 1 and the Type material section conflict; no Reptile Database species page reached.
- Hemidactylus pfindaensis (VZ 71, 10.3897/vz.71.e64781): holotype 'Eye diameter (2.96 mm)' but the Methods list 'orbital diameter (OD)', and the paper prints the holotype as female while the Reptile Database prints male.
- Cyrtodactylus phamiensis, Cyrtodactylus rukhadeva, Trimeresurus ayeyarwadyensis, Leptobrachella darongshanensis: ED only as ratio or in supplements. Calotes thailandensis/maehongsonensis, Ovophis zhaoermii, Pedioplanis, Dasypeltis albigularis, Hebius, Gonyosoma coeruleum, Scincella jinchuanensis/maerkangensis, Calumma roaloko, Lycodon pictus: no ED value in the text. Dixonius fulbrighti (Evol Syst 7, CC0): measurement table not in the XML the reader returned.
- Scincella qianica and S. verecunda, Gekko/Goniurosaurus/Trimeresurus ZSE 102 and others: already on main.
- Fish: no Catalog of Fishes species page reached from searches that also gave a mm table; none filed.
- Several Evolutionary Systematics article_preview ids (105850, 72564, 83290) returned the Gonyosoma coeruleum text; the XML or /article/ pages were used to confirm titles.

## Weak spots
- All text through the WebFetch reader; column-to-code mappings are the reader's reading of Pensoft tables. Licence sentences came back in pieces (Bungarus: first clause only).
- Units not printed beside the ED row for santana and umashaankeri (see records). Crossref not checked.

## Desk disposition after audits 1020-1022 (3 November 2026)
7 of 22 lines merged: Colubroelaps nguyenvansangi (lines 1-3, three different specimens, audit 1020: 9 fixable faults; the "not on main" claim was stale because desk-d508 filed the adleri holotype from the same paper) and Bungarus sagittatus (lines 19-22, audit 1022: 22 fixable faults including a whole licence sentence, the "Methods" heading and the caliper qualifier). Held out, 15 lines, because no auditor reached the publisher full text from its own search results: Cyrtodactylus santana (lines 4-13, audits 1020 and 1021), Cnemaspis umashaankeri (14-17, audits 1021 and 1022) and Lycodon truongi (18, audit 1022). The corrected replacement lines are in /tmp/m311/audit-1020.md (lines 4-8), audit-1021.md (9-16) and audit-1022.md (17-18). The Pensoft landing page (zookeys.pensoft.net/article/NNNNN/) carries only the abstract and a table of contents; the Methods and tables are on the article_preview and /download/xml/ pages, which surface in a search only occasionally. Auditors that found the Herpetozoa and ZSE full text passed; auditors for ZooKeys and VZ papers mostly did not.
