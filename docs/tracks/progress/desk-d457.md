# desk-d457 progress

Angle: non-spider unit (the brief's later paragraphs say this unit MUST be non-spider; its first paragraph lists spider angles, and the later instruction was followed, as desk-d455 did). Open-access frog papers that print eye diameter (ED) in millimetres per named specimen. 28 records (log docs/views/evidence/desk-d457.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement. check.py: 0 problems for desk-d457 (plain and --require-evidence-kind). About 38 WebSearches.

## Filed
- ZooKeys 1275: 43-61 (10.3897/zookeys.1275.186067) Odorrana yangi (Ranidae): holotype and 6 male paratypes plus the female paratype KIZ2025123 (8 records, Table 2 ED row; Methods 'eye diameter, between two corners of eye').
- Zoosystematics and Evolution 102(1): 71-85 (10.3897/zse.102.161437) Brachytarsophrys wui (Megophryidae): 7 type specimens (Table 2 ED row; 'diameter of exposed portion of eyeball').
- Zoosystematics and Evolution 101(3): 1213-1226 (10.3897/zse.101.155859) Boulenophrys changyangensis: holotype and 3 male paratypes named in the type text (Table 3 ED row).
- Biodiversity Data Journal 13: e153987 (10.3897/BDJ.13.e153987) Boulenophrys daxuemontis: holotype only, whole Table 3 row ID 2 quoted.
- Zoosystematics and Evolution 102(1): 253-269 (10.3897/zse.102.175462) Leptobrachella xinshaoensis: 3 males (Table 3 ED row).
- ZooKeys 1267: 15-30 (10.3897/zookeys.1267.177118) Leptobrachella deocaensis: holotype male and 4 female paratypes (Table 2 ED row).

## Weak spots
- All text came through the WebFetch summariser on Pensoft article_preview pages; column-to-code mappings are the tool's reading of the tables (ranges and means printed in the same rows agree where present). The 22-cell daxuemontis row was returned whole only when asked for that row alone.
- Species validity from Amphibian Species of the World pages opened from search results (none prints an explicit 'valid'). Crossref version of record not checked for any paper. No Class, Order or Family headings are printed on any of the pages.
- ZooKeys 1275 is a volume number on the avoid list (Pholcus paper); the Odorrana paper is a different article and is not on main.

## Not filed and why
- Boulenophrys changyangensis MT CY20220806003 (ED 3.6): in Table 3 but not named in the type-material text.
- Boulenophrys daxuemontis paratypes: the tool did not return whole rows for them, and one voucher code differs between the type list and the table.
- Odorrana feii (ZSE 101(4): 1949-1964): ED printed only as sex ranges and means.
- Sphenomorphus puhoatensis (ZooKeys 1279): no ED in the table.
- Leads not reached to a publisher page: Cyrtodactylus nebulicola (ZooKeys 1278, only figure pages and the Reptile Database page), Scincella ngati (ZooKeys 1275: 275-298), Leptobrachium mechuka and L. somani (PeerJ 14: e20397; no peerj.com article page in results), Leptobrachella ZooKeys and ZSE papers of 2026 listed on novataxa.blogspot.com.

## Desk disposition after audits (2 November 2026)
Audits 912-915 judged all 28 lines: every ED value matches its printed specimen-code column and sex, the Methods define ED in mm, Amphibian Species of the World accepts all six names, and nothing repeats main. Counted errors fixed with the auditors' lines: Brachytarsophrys wui (7 lines: conditions said seven paratypes where the paper prints six, and the holotype quote was misquoted and cut without a mark) and lines 16-23 (hyphen where the page prints an en dash in 7 quotes; units sentence misquoted in 4; quotation marks round unprinted type-material text in line 20). Other faults were licence sentences, notes and heading paths. Nothing is dropped. Counted errors: 15.
