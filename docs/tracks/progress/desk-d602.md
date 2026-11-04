# desk-d602 progress

Angle: novataxa Pensoft XML search route (ZooKeys 2017-2024, ZSE, Evolutionary Systematics, Herpetozoa) for families Microhylidae, Gekkonidae, Scincidae, Lamprophiidae, Dipsadidae, Hylidae, Strabomantidae, Leptodactylidae. Trait eye_diameter_mm (anatomical_measurement) only where Methods define ED. Log: docs/views/evidence/desk-d602.jsonl. 15 records (log docs/views/evidence/desk-d602.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement. check.py plain and --require-evidence-kind: 0 problems for this file. About 38 WebSearches.

## Filed
- Pristimantis nebulosus (ZSE 98(2): 213-232, 10.3897/zse.98.84963): holotype (value in parentheses, flagged by the paper) and 3 topotypes, Table 1 ED row, 4 records.
- Pristimantis mallii (ZooKeys 832: 113-133, 10.3897/zookeys.832.30874): holotype QCAZ 52473, holotype measurements sentence, 1 record.
- Cophixalus rajampatensis (ZSE 91(2): 199-213, 10.3897/zse.91.5411): 8 type specimens, Table 1 ED row, 8 records.

- Pristimantis cajanuma and P. quintanai (ZooKeys 864: 111-146, 10.3897/zookeys.864.35102): holotype 'Measurements of holotype' lists, 1 record each (2).

## Not filed and why
- On main already (found only after fetching): Scincella verecunda (Herpetozoa 39, d477), Raorchestes malipoensis (d597), Pristimantis fergusoni, P. etsa, P. similaris, P. milpe, Charadrahyla viruela, Eleutherodactylus franzi.
- Platypelis laetus: held out by d591 (stale ASW entry, current name Cophyla laeta page robots_disallowed).
- Cyrtodactylus arnei, zhenkangensis, menglianensis, nangunhe: Methods define ED as ear diameter; eye is OD (orbit diameter). C. thongphaphumensis: ED defined but only p-values printed.
- Dendropsophus bilobatus (ZooKeys 942): ED defined and Table 3 per-specimen values exist, but the holotype sentence is over 40 words and the page reader would not return a verbatim table row; Table 3 holotype row also disagrees with the holotype sentence on TL and FL. Lead for a unit that can read the row.
- Pristimantis donnelsoni (ZooKeys 1180): holotype list (ED 1.9) is over 40 words; P. kayi list not reached.
- Atractus paulus: eye diameter 2.9 mm in the holotype description but Methods do not define ED.
- Scincidae and Microhylidae XML pages (Sphenomorphus, Scincella, Micryletta, Kaloula, Microhyla): Methods define EL (eye length) or no eye measure, or the XML is cut before the measurements.
- Pristimantis vrazi, P. mallii Table 1 (ranges only), P. nebulosus holotype: the nebulosus holotype value is filed with the paper's own parenthesis caveat.
- Licence and byline read on the Pensoft article_preview pages for all five filed papers; ASW pages opened for all five species. No Class/Order/Family headings are printed on the pages; families follow ASW URL paths (Craugastoridae for Pristimantis; the papers say Strabomantidae).
- Weak spot: table rows and column-to-specimen mappings are the page reader's cell-by-cell reading; Cophixalus ASW prints vol. 92 where the paper prints 91(2).

## Desk disposition after audits 1202, 1203, 1204 (4 November 2026)
All 15 records merged. Counted errors: 15 (audit 1202: 5; 1203: 8; 1204: 2), all fixable wording faults, and the auditors' replacement text was applied.
- The page reader's tooltip expansions had been quoted as printed on lines 1-13 (the printed row label is "ED"; "ED (eye diameter: ...)" is the hover definition). Audit 1202 line 5 (Pristimantis mallii) gives the printed text as "SVL 28.7" by inference from the reader's pattern, because no XML was in the auditor's own search results; that one printed-text claim is inferred, not read.
- Pristimantis nebulosus holotype ZFMK 27643 ED 4.0 is printed in parentheses and the caption says to read such values with reservations; audit 1202 kept it filed with the paper's caveat in the note.
- Heading paths now run from Class Amphibia down to the genus where printed (audit 1204: the desk's claim that no such headings are printed was false for ZooKeys 864). ASW prints Zoosyst. Evol. vol. 92 for Cophixalus rajampatensis; the paper prints 91(2), and the paper's volume is used. Families follow ASW (Craugastoridae for Pristimantis; the papers say Strabomantidae).
- Not filed (leads): Dendropsophus bilobatus ZooKeys 942 (holotype sentence over 40 words, Table 3 holotype row disagrees with the holotype sentence on TL and FL), Pristimantis donnelsoni ZooKeys 1180, Atractus paulus (ED undefined); Cyrtodactylus arnei, zhenkangensis, menglianensis and nangunhe define ED as ear diameter.
