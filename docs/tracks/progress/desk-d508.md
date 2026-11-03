# desk-d508 progress

Angle: reptile eye_diameter_mm (no spiders). Open-licence descriptions printing eye diameter (ED) in millimetres per named specimen, with a Reptile Database species page reached from my own search results. 15 records (log docs/views/evidence/desk-d508.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement. check.py: 0 problems (plain and --require-evidence-kind). About 36 WebSearches.

## Filed
- Trimeresurus lanna (VZ 74: 303-342, 10.3897/vz.74.e113347): holotype AUP-00180 ED 4.5 mm (Description sentence). The Reptile Database page opened this time from a fresh search result (no redirect loop).
- Cnemaspis auriventralis (ZSE 98(2): 345-363, 10.3897/zse.98.89591): holotype and 4 paratypes, Table 4 ED row (5 records). Name check: the Reptile Database lists auriventralis under its own name and C. huaseesom as a separate species (Grismer et al. 2010, Zootaxa 2576); the 'huaseesom' line on the auriventralis page is a later citation, not a synonym. auriventralis is the valid name.
- Gekko paucituberculatus (VZ 74: 121-132, 10.3897/vz.74.e113899): holotype and paratype, Table 5 (2 records).
- Colubroelaps adleri (Herpetozoa 37: 379-390, 10.3897/herpetozoa.37.e137809): holotype ED 0.51 mm (1 record).
- Hemiphyllodactylus gengmaensis (ZooKeys 1197: 197-213, 10.3897/zookeys.1197.117359): holotype and 5 paratypes, Table 3 ED row (6 records).

## Not filed and why
- Colubroelaps nguyenvansangi (ZISP 25682 ED 0.8, ZMMU Re-15484 1.0, Re-15485 0.8, same Table 1): its Reptile Database species page was refused (permission), so held out.
- Cnemaspis fantastica, C. pachaimalaiensis, C. rudhira (VZ 72, 10.3897/vz.72.e94799): article_preview text ends at 95020 characters before Tables 9-11; element/2/118 is a figure page, CSV 21 is the GenBank table; tables never reached. Reptile Database rudhira page opened (valid-looking, p. 1173).
- Cnemaspis siamensis-group sister paper Cyrtodactylus monilatus (ZooKeys 1103): already a d507 species.
- Agasthyagama (VZ 74: 151-168), Cordylus momboloensis (VZ 73), Pseudotrapelus tuwaiqensis (VZ 73), Papuascincus (VZ 74), Dravidoseps (VZ 74: mensural data in supplement), Diploderma four species (ZooKeys 1148: SEL only), Sphenomorphus lingnanensis, Triplophysa Guizhou four species (ZooKeys 1185: ED in % HL or one species-level value), Protobothrops flavirostris (Herpetozoa 38: the preview URL id 146004 returned the Colubroelaps text; article page held no body), Lycodon subcinctus (no mm table), Paraxenodermus (no measurements): no usable ED in mm.
- Fish: no Catalog of Fishes route reached; the fish candidates returned were already on main or in % HL.

## Weak spots
- All text through the WebFetch reader; table cells and column-to-code mapping are the reader's reading. Licence sentences came back cut.
- Hemiphyllodactylus gengmaensis paratype 2298: one read printed 2.6, another 2.60 (same value).
- Warning for later units: article_preview.php?id=146004 on herpetozoa returned the Colubroelaps paper; check title and DOI on every read.

## Desk disposition after audits 1016-1019 (3 November 2026)
1 of 15 lines merged: line 9, Colubroelaps adleri holotype ED 0.51 mm (audit 1017 passed it after 7 fixable faults: licence sentence and holotype block cut without a cut mark, a wrong Reptile Database note, a Methods side statement left out). The other 14 lines were held out because the auditors could not reach the publisher's full text from their own search results, even on re-audit with domain-restricted searches: Trimeresurus lanna (1), Cnemaspis auriventralis (5), Gekko paucituberculatus (2) in audits 1016 and 1018; Hemiphyllodactylus gengmaensis (6) in audits 1017 and 1019. The corrected replacement lines are in /tmp/m311/audit-1018.md (lines 1-8) and /tmp/m311/audit-1019.md (lines 10-15) should a later auditor or unit reach those pages. Faults found on the held-out lines: licence sentence cut without a cut mark on every line; lines 4-6 named the holotype's 2.5 mm instead of their own value; the huaseesom entry sits in the auriventralis Synonym field of the Reptile Database as an earlier use of the name for this population (auriventralis is the valid name); lines 7-8 took type age, locality and date from the Reptile Database, not the paper; a "KIZ" code prefix the gengmaensis paper does not print; "Results" missing from heading paths. Owner question: pages that the fetch reader opens for a unit but that no search result surfaces for an auditor cost the desk most of this unit; a way to hand the auditor the unit's own URL would let these lines through.
