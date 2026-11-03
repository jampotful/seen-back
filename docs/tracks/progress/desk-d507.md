# desk-d507 progress

evidence_intake: evidence-kind-v2
intake_base: 4b191ea4353c33b1e98df62264db2ff826e28e9b

Angle: lizards, geckos and snakes (no spiders), continuing the d455/d459/d506 eye_diameter_mm pipeline. 34 records (log docs/views/evidence/desk-d507.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement, one record per labelled specimen. check.py: 0 problems (plain and --require-evidence-kind). About 33 WebSearches. No fish record was filed.

## Filed
- Vertebrate Zoology 72: 1137-1186 (10.3897/vz.72.e94799): Cnemaspis salimalii (9: Table 3 ED row, holotype and 8 paratypes) and C. agayagangai (9: Table 6 ED row).
- Vertebrate Zoology 73: 433-450 (10.3897/vz.73.e101871): Hemidactylus quartziticolus (10: Table 3 ED row).
- Vertebrate Zoology 71: 155-174 (10.3897/vz.71.e60225): Cyrtodactylus raglai (3: Table 6 ED row).
- Vertebrate Zoology 74: 359-379 (10.3897/vz.74.e112132): Oligodon speleoserpens (2: Table 1 EyeD row, holotype and paratype).
- ZooKeys 1103: 139-169 (10.3897/zookeys.1103.84672): Cyrtodactylus monilatus (1: Table 4 holotype column; paratypes only as ranges).

## Weak spots
- All text came through the WebFetch page reader on Pensoft article_preview pages; rows and column-to-code mappings are its cell-by-cell reading, and licence sentences came back in pieces and were joined. Crossref not checked.
- Oligodon speleoserpens and the Cnemaspis papers list "eye diameter (EyeD/ED)" without a separate definition; the label itself is the definition. Oligodon and Cyrtodactylus raglai: raglai female ED values differ by 2.2 mm as printed.
- Reptile Database pages (opened from my own search results) print no explicit "valid"; each lists the name with no true synonyms.

## Not filed and why
- Cnemaspis fantastica, C. pachaimalaiensis, C. rudhira (same VZ 72 paper): page text reached stopped inside the C. fantastica diagnosis; tables not read.
- Cnemaspis auriventralis (ZSE 98(2): 345-363, 10.3897/zse.98.89591): ED row read (holotype 2.5), but the Reptile Database page lists Cnemaspis huaseesom (Yodthong et al. 2022, ZooKeys 1103) as a synonym under it; priority and validity unclear, held out.
- Trimeresurus lanna (VZ 74: 303-342, holotype ED 4.5 mm in Description sentence): Reptile Database page redirect loop in WebFetch; not opened.
- Trimeresurus ciliaris (VZ 73): already on main (desk-d490). Pachydactylus maiatoi (OrbD only), Heliobolus bivari/crawfordi (no ED row), Angolan Hemidactylus (OD only), Cyrtodactylus rukhadeva (adjusted log values), Platyceps josephi (no ED table), Balitora anlongensis, Claea (no mm table), Trachischium lalremsangai, Hemiphyllodactylus puncak/jeraiensis, Cnemaspis (ZSE 97) Sri Lanka: page text held no table or body.

## Desk disposition after audits 1010-1015 (3 November 2026)
All 34 lines merged with the auditors' replacement text; nothing dropped. Audit 1011 (lines 9-16) could not reach the Methods, tables or licence sentence (only the publisher's article list tab) and held the eight lines out; audit 1015 re-audited the same lines after a title search restricted to the publisher domain surfaced the article_preview page, read the Methods, Tables 3 and 6, type text and licence, and passed all eight with fixes, so 1015's replacement lines were merged in place of 1011's. Errors counted by the auditors: 1010 (lines 1-8) 8 of 8; 1015 (9-16) 8 of 8; 1012 (17-24) 8 of 8; 1013 (25-31) 7 of 7; 1014 (32-34) 3 of 3. The recurring fault was the eye field saying "side not stated" where the Methods print a body side (right for Cnemaspis, left for Hemidactylus quartziticolus and Cyrtodactylus); others were notes naming the holotype's mm value for paratypes, paratype locality and date, Table heading paths, and the Oligodon label printed EyeD. Values matched the printed cells digit for digit on every line. Methods define ED as a diameter in every paper.
