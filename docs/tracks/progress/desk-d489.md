# desk-d489 progress

Angle: lizards, geckos, snakes, turtles (Reptile Database page reached from my own search results) and fish with mm tables. 8 records (log docs/views/evidence/desk-d489.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement. check.py: 0 problems for this file (plain and --require-evidence-kind). About 32 WebSearches.

## Filed
- ZooKeys 1258: 9-33 (10.3897/zookeys.1258.161382, CC BY 4.0) Scincella tenuistriata (Scincidae): holotype QHU R2025009 (Description sentence and Table 4) and 7 paratypes (Table 4 ED row), all adult males. ED defined in Methods as the length of the palpebral cleft; Table 4 note "All measurements are in mm". Reptile Database page opened from search results.

## Weak spots
- Text came through the WebFetch reader on the ZooKeys article preview; the XML download returned only the front part. Column-to-code mapping is the reader's reading of the header and ED row. Licence sentence is cut by the reader and marked. Crossref not checked.

## Not filed and why
- Plagiopholis yangi (Evolutionary Systematics 10, 10.3897/evolsyst.10.188735): holotype ED 2.6 only, CC BY 4.0, but two searches found no Reptile Database page.
- Ablepharus tuolinensis: Reptile Database page exists but no open copy of the paper reached; the Herpetozoa 37 paper found is the A. eremchenkoi one (already d486), and its XML shows ED values that disagree with the preview for the same specimens.
- Hemiphyllodactylus puncak and H. jeraiensis (Vertebrate Zoology 76: 1-32): XML cut before morphology.
- Trimeresurus ciliaris (Vertebrate Zoology 73: 697-716, ED row in CSV, Reptile Database page in results): XML cut before the Methods and type material, so ED definition and types unverified.
- Claea dafangensis (ZSE 102(2)): Methods print no ED definition, abstract gives eye as % HL, text cut before tables.
- Rhinophis siruvaniensis (d487), Hemiphyllodactylus laowozhenensis (d483), Scincella qianica and S. verecunda (d477), Cyrtodactylus nebulicola (no ED), Scincella ngati and S. truongi (ED undefined / absent), Acanthosaura aurantiogularis (no ED row), Goniurosaurus wuzhengjuni (EE only), Hebius yangi (no ED row), Opisthotropis haihaensis and O. tamdaoensis (no ED row), Eublepharis jhuma (OD only): already on main or no usable ED.

## Desk disposition after audit 979 (3 November 2026)
- Audit 979 (lines 1-8, Scincella tenuistriata): 0 errors, 32 faults (4 per line: Mitutoyo 0.01 mm precision missing, heading path wrong, Type and Sex rows omitted, inaccurate "not on main" note). Replacements applied; nothing dropped.
- The Methods print "ED = eye diameter, the length of the palpebral cleft", so eye_diameter_mm stands.
- The DOI 10.3897/zookeys.1258.161382 appears on main only in the notes of four Scincella qianica records in desk-d477 (a different species and paper, DOI 10.3897/zse.101.157713), as a comparison; it is not a repeat.
