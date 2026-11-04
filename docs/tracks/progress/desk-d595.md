# desk-d595 progress

Angle: per-specimen table rows (reptile eye or ear-opening, fish or other vertebrate eye diameter) in open-licence journals via publisher table CSVs. The OLD-ANGLE paragraph of the brief was ignored as superseded. Started 2026-11-03. Records: docs/views/evidence/desk-d595.jsonl (none yet).

## Log
- Started; rules and record form read (d459, d455).
- Filed 10 sensory_anatomy records: Cyrtodactylus luci (ZooKeys 1192: 83-102), orbital diameter and ear length rows of Table 2, five type specimens each.
- Filed 8 records: Scincella fansipanensis (BDJ 13: e161782), ED (eye_diameter_mm) and EL (ear opening, sensory_anatomy) for four Yunnan specimens.
- Filed 4 records: Achalinus sheni (ZooKeys 1209: 1-17), Table 3 ED row, four wild-collected specimens (one albinistic, stated in the record).

## Summary
22 records in docs/views/evidence/desk-d595.jsonl (check.py plain and --require-evidence-kind: 0 problems for this file). About 42 WebSearches. No Crossref, no proxy hosts, only URLs seen in own search results.

| Species | Paper | Records |
|---|---|---|
| Cyrtodactylus luci | ZooKeys 1192: 83-102, 10.3897/zookeys.1192.117135 | 10 (Table 2 OrbD and ED=ear length rows, sensory_anatomy) |
| Scincella fansipanensis | Biodiversity Data Journal 13: e161782, 10.3897/BDJ.13.e161782 | 8 (Table 2 ED eye_diameter_mm x4; EL ear opening sensory_anatomy x4) |
| Achalinus sheni | ZooKeys 1209: 1-17, 10.3897/zookeys.1209.128944 | 4 (Table 3 ED, one albinistic specimen) |

## Not filed
- Already on main (CSV pool is largely worked): Trimeresurus loong, Cyrtodactylus menglianensis, Rhinophis siruvaniensis, Hemiphyllodactylus ziegleri neighbours, Calamaria spp., Takydromus yunkaiensis, Scincella-ZooKeys 1258, Cyrtodactylus ZooKeys 1241 and others.
- Trimeresurus liqibini (ZSE csv 173390): unresolved, no Reptile Database page filed by earlier units.
- Fish CSVs found (ZooKeys 167436 Omobranchus-type blenny, 84171 Stolephorus, 160425, 8507, 72181, 170907, 122962, 7377): eye diameter printed only as % SL or % HL. Dead.
- ZSE 4971 (MNHN 3238/3239 lectotype/paralectotype, ED 1.7 / 1.4): article date unknown, species not identified, not pursued.
- ZooKeys 1251 Lycodon duytan: no ED data. BDJ 3: e4284 and BDJ 1: e1015: group statistics or no ED. Herpetozoa 34 Oligodon hamptoni: no table.
- Lead, unidentified: zookeys.pensoft.net/article/178070/download/csv/23/ (8 specimens IB R.6445-6452, Holotype + 7 paratypes, sexes M/F, rows ED and TD in mm; paper title not reached by search, not Hemiphyllodactylus ziegleri). Also ZooKeys 1148 "Four new species of the genus Diploderma" (97706): multi-species table, not read.
- Scincella fansipanensis original description is Zootaxa (dead venue).

## Notes
- addlog rejected trait eye_diameter_mm as unknown on the first Scincella ED line; the validator's own message says to write "new trait" in the note, as d459 did for the same key, which was done (note begins "new trait: eye_diameter_mm (same key as main)"). No other validator rejection occurred.
- Cyrtodactylus luci was held out by d510/d512 because ED means ear length; here it is filed as sensory_anatomy (ear length, and orbital diameter) with that stated in the note. Table 2 caption was only available paraphrased from the page reader.
