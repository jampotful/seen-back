# desk-d480 progress

Angle: reptiles and fish (the brief), widened to amphibians after the reptile and fish leads failed; no spiders. Eye measurements in millimetres per named specimen from open-licence descriptions. 17 records (log docs/views/evidence/desk-d480.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement. check.py: 0 problems (plain and --require-evidence-kind). About 30 WebSearches and about 35 WebFetches.

## Filed
- ZooKeys 1278: 111-133 (10.3897/zookeys.1278.169620) Occidozyga nishikawai (Dicroglossidae): 15 type-series specimens (holotype IB A.6287, 4 male paratypes, 8 female paratypes, 2 juveniles), Table 3 row EL (Methods: 'EL: Eye diameter'; caption 'Measurements (mm)'). The quote is the whole EL row including the two O. lingnanica cells (not filed). Values and the code and sex rows come from the Table 3 CSV download shown in my search results, read through the page reader; the preview reader's cell-by-cell reading agrees. Material examined prints a female as IB A.6494 where Table 3 prints IB A.6294 (a discrepancy inside the paper; the table code is used and the discrepancy is in each record).
- Herpetozoa 39: 145-160 (10.3897/herpetozoa.39.e191333) Vietnamophryne abscondita (Microhylidae): holotype VRTC NAP-12097 (EL 1.65) and paratype ZMMU A-8446 (EL 1.87), Measurements entries headed '(in mm):'. The paper measures eye length (anterior to posterior corner of the eye), not a diameter; the record says so.

## Weak spots
- All text came through the WebFetch page reader; the Occidozyga EL row came from the CSV file the reader returned, with the reader declining to reproduce Table 3 rows verbatim from the preview.
- Species validity from Amphibian Species of the World pages opened from my search results; neither prints an explicit 'valid'. Crossref not checked.
- No class, order or family headings are printed on either article page; families come from the ASW path.

## Not filed and why
- Gekko asahi (ZSE 102(2) 557-574, 10.3897/zse.102.186960): XML read in full by the reader; molecular paper only (Table 1 is GenBank accessions, no morphology, no ED). Dead lead.
- Calotes thailandensis (ZooKeys 1281): Reptile Database page reached; article_preview id 175455 returned the Johnius javaensis paper, the XML link was refused (provenance), optimap and figure pages carry no text. Still unread.
- Hemiphyllodactylus pakhaensis (ZooKeys 1268.177040): article preview read correctly (ED 'the greatest horizontal diameter of the eyeball', calipers 0.1 mm; Table 3 'Mensural (in mm)': holotype VNUF R.2025.32 male 1.95, paratypes R.2025.31 female 1.83, R.2025.33 female 2.38, R.2025.34 subadult male 1.92; CC BY 4.0). Not filed: no Reptile Database page appeared in three searches, and the table rows were given as a reader summary only. Lead for a unit that reaches the species page.
- Scincella dabieshanensis (ZSE 102(4) 10.3897/zse.102.187997): Methods define eye width (EW), holotype EW 1.88 mm, no EW table row; no Reptile Database page. Scincella jinchuanensis and S. maerkangensis (184613): no eye measurement at all.
- Trimeresurus liqibini: no Reptile Database page in two more searches. Goniurosaurus wuzhengjuni (177343): records SE and EE only, no eye diameter.
- Triplophysa zhijinensis and T. dafangensis (ZooKeys 1281.186268): eye diameter printed only as % HL (mm values would be calculated); Catalog of Fishes reference page 43124 reached but names no species. Johnius javaensis: already on main (d343).
- Boulenophrys youran (ZSE 102.175092): ED only as a ratio, mm in a supplement. Tylototriton wufengensis (173283): measurements only in supplements. Pseudoeurycea euguii, natsii, parraoleae (Vertebrate Zoology 76, 10.3897/vz.76.e167783): page returned without Methods or tables. Nanorana wenshanensis (179415): preview returned the Occidozyga paper (pollution).
- Leptobrachella yachangensis (Herpetozoa 38.e165088; Methods define EYE) and Boulenophrys yezhongensis (38.e155430): XML reads stop before the holotype description and measurement tables at every offset tried; previews return the Vietnamophryne paper. Not on main; leads.
- Odorrana nagao and Liurana menba: not opened beyond ASW and gap-file hits.
- Insects and crustaceans (ommatidia counts): not reached.
