# desk-d501 progress

Angle: lizards, geckos, snakes, turtles (Reptile Database page from my own search results) and fish (Eschmeyer's Catalog of Fishes page from my own search results), eye diameter or eye length in millimetres for a named specimen. No spiders. 7 records (log docs/views/evidence/desk-d501.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement. check.py: 0 problems (plain and --require-evidence-kind). About 45 WebSearches.

## Filed
- ZooKeys 1226: 319-337 (10.3897/zookeys.1226.139655) Scincella truongi (Scincidae, Reptilia): holotype and 5 paratypes, Table 2 EL (eye length, "distance between anterior and posterior corners of eyelid") row, 6 records. Reptile Database page for the species opened from my own search; units from the Table 2 header cell "Measurements (in mm)". Earlier desk notes (d489) had it as "ED undefined/absent"; the EL row is printed per specimen. The printed Min-Max cell (2.7-3.2) is below the HUS.2024.04 value 3.24; individual cells logged, range cell not used (stated in each record).
- ZooKeys 1011: 85-100 (10.3897/zookeys.1011.57302) Sillago nigrofasciata (Sillaginidae, fish): holotype OUC_FEL178001 (151.2 mm SL), Table 3 "Eye diameter (ED)" row, 8.1 mm. Eschmeyer's Catalog of Fishes reference page (getref id 38073) reached from my own search. Methods give no eye definition (ED is labelled only in the table).

## Weak spots
- All text through the WebFetch reader on Pensoft preview, CSV and XML pages; column-to-code mappings are the reader's reading. The Sillago XML reading placed the percentage section under "% of SL" while the CSV and Description say % of HL; the mm row sits above both.
- Catalog of Fishes page prints no validity word for Sillago nigrofasciata; Reptile Database page for S. truongi likewise.
- Sillago paratypes (n = 107) are a range only and were not logged.

## Not filed and why
- Already on main: Hemiphyllodactylus (western Yunnan) LW2024R006 (d483), Rhinophis siruvaniensis BNHS 3387 (d487), Johnius javaensis (d343), Hemiphyllodactylus venkatadri (d478), Hemiphyllodactylus lungcuensis (BDJ 13 e173469 and ZooKeys 1167 per d500/d343), Scincella verecunda (dead per brief).
- Eublepharis jhuma (Herpetozoa 39): orbital diameter OD only; on main from d353.
- Sphenomorphus puhoatensis (ZooKeys 1279: 167-186; holotype EL 2.2 mm, CC BY 4.0): two more searches found no Reptile Database page. Scincella gigas: same.
- Anolis cyanophthalmus (Vertebrate Zoology 75: 441-457, 10.3897/vz.75.e162071): Methods define no eye measurement and the measurement file is a supplement.
- Diploderma bifluviale (ZooKeys 1251), Pareas dabieshanensis/orientalis (ZSE 101(4): 1621-1638, ED ranges only), Trachischium lalremsangai (no eye row), Sphenomorphus lingnanensis (no ED), Triplophysa baishuijiangensis, Triplophysa/Sillago-like tables printed as %SL or %HL.
- Cyrtodactylus fluvicavus, C. kochangensis, C. uthaiensis, C. rivularis (ZooKeys 1129: 109-162, 10.3897/zookeys.1129.90535, CC BY 4.0; ED defined as greatest horizontal diameter of the eyeball, nearest 0.1 mm): none on main; the per-specimen ED row exists as a Pensoft table CSV (/download/csv/25/) but the page reader showed only Tables 1-4 (Table 4 is size-normalised), so the caption and unit of the table could not be confirmed. Lead only.
- Dixonius sambhupura, Hemiphyllodactylus guangnanensis (Zootaxa): excluded.
- Johnius-type fish tables (zse 56247, 139205, 119520, 167436, zookeys 170907, 173359): eye diameter as % of SL or HL.
