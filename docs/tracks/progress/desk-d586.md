# desk-d586 progress

evidence_intake: evidence-kind-v2
intake_base: 05910a8a69aa95e24b79a86c185065f609842165

Angle: tympanum diameter (anurans) and mammal ear/tragus length from Pensoft papers reached through my own WebSearch results. Trait sensory_anatomy, evidence_kind anatomical_measurement (same as main's tympanum and pinna rows). About 38 WebSearches. 9 records in docs/views/evidence/desk-d586.jsonl; check.py 0 problems (plain and --require-evidence-kind).

## Filed
- ZSE 101(3): 1023-1055 (10.3897/zse.101.144375) Murina beibengensis holotype XZ2024037: ear length 16.18 mm and tragus length 8.67 mm, same measurement line (cut marked). Text says adult male, Table 2 header says Holotype (Female); disclosed in conditions (an earlier note on main withheld it for this reason). MDD 1006943 opened.
- ZSE 101(3): 983-997 (10.3897/zse.101.147349) Murina chayuensis: E 14.82 mm, single female row of Table 2 (matches holotype XZ2023107 by FA and GTL; text never states sex). Two table rows quoted so the species label is printed. MDD 1006942 opened. desk-d525 had noted this paper as "no values".
- Evolutionary Systematics 9(2): 285-299 (10.3897/evolsyst.9.174833) Spinomantis lavabato (4 specimens) and S. lakolosy (2 specimens): TD (horizontal tympanum diameter) from Table 1, one record per specimen column. ASW pages for both opened. d580 filed only nostril records from this paper.

## Weak spots
- All text came through the WebFetch page reader (about 125 characters per sentence, pieces joined). Table 1 column mapping for Spinomantis (voucher, status, sex rows; 4 + 2 cells) and Murina Table 2 rows are the reader's cell-by-cell reading. The Murina measurement-line quote follows the form of d345's accepted medogensis record (abbreviation expansions left out as tooltips).
- The six Spinomantis records share one identical quoted table row.
- Murina yadongensis (same paper as beibengensis): the article_preview text cut off before its account and the XML stops in Results; not filed. M. rubella likewise.

## Not filed and why
- Brachytarsophrys wui (ZSE 102(1): 71-85): Table 2 has no tympanum row; tympanum hidden.
- Leptobrachella xinshaoensis, Odorrana yangi, Boulenophrys daxuemontis, L. weixinensis and other 2026 frogs: already on main.
- Oreoryzomys jumandi (PeerJ 20515): reader garbles Table 5 columns; only summary rows; byline not shown.
- ZooKeys 24557 and evolsyst 62661 CSVs: range or mean rows only, species unidentified.
- Zootaxa, Salamandra, Journal of Natural History, RZSI papers (Pristimantis Baudo, Leptobrachella cathaya, Afronycteris, Boophis samuelsabini): no open licence statement reached or dead venue.

## Desk disposition after audits 1147 and 1148 (4 November 2026)
Counted errors: 6 of 9 (Murina chayuensis holotype identity was inferred from matching measurements and was removed, so the record now describes the single female row only; Spinomantis lines 4-8 had the wrong account in where and omitted the TD/ED range conflict or the text-versus-table 60% against 0.56 conflict). All corrected with the auditors replacement text; 9 of 9 merged. Open owner question: the Murina beibengensis holotype sex conflict (text male, Table 2 header female) is filed with the conflict disclosed since the value is the holotypes either way.
