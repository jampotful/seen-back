# desk-d590 progress

evidence_intake: evidence-kind-v2
intake_base: c15fb1205cfba26385eda168cb6e05f0b8786072

Angle: older (2015-2021) open-licence Pensoft papers (ZooKeys, Zoosystematics and Evolution, Evolutionary Systematics, Herpetozoa, Vertebrate Zoology, Biodiversity Data Journal, Check List) with per-specimen tympanum diameter / ear length rows and eye diameter rows. The OLD-ANGLE paragraph in the brief was superseded and not followed. Log: docs/views/evidence/desk-d590.jsonl.

## Status
Started 3 November 2026. Batches 1-2 filed: 30 records.

## Filed
- ZooKeys 1008: 139-157 (10.3897/zookeys.1008.56412; Lyu et al., 2020) Leptobrachella bashaensis (Megophryidae): holotype GIB196403 and five paratype males, Table 3 rows TMP (tympanum diameter) and EYE (eye diameter), one record per specimen per structure (12). Female column GIB196405 not in the printed type list: not filed.
- ZooKeys 770: 211-226 (10.3897/zookeys.770.23526; Yu et al., 2018) Kurixalus yangi (Rhacophoridae): holotype KIZ 14102911 and 8 paratype males, Table 1 whole rows, TD and ED per specimen (18 records). ASW notes Kurixalus naso may be a senior synonym (disclosed in notes).

## Weak spots
- All text came through the WebFetch page reader (Pensoft article_preview and download/xml/csv pages from my own search results); table rows and column-to-specimen mappings are the reader's cell-by-cell readings. Leptobrachella bashaensis was read twice (a per-specimen layout and the transposed table) with identical values. Kurixalus yangi: a two-column extraction and the whole 17-column table agree.
- The reader returned licence sentences as opening clause plus a paraphrase or a second answer with the closing clause; Kurixalus yangi's closing clause is paraphrased only (disclosed in each note).
- Table cells carry no unit in either paper; mm comes from the captions (Leptobrachella) or the Methods precision sentence (Kurixalus yangi caption has no unit).
- No Class, Order or Family headings were reported by the reader for either paper.
- Crossref was not used. About 41 WebSearches.

## Not filed and why (leads)
- Mantophryne insignis (ZSE 92(1): 111-118, 10.3897/zse.92.7629, CC BY 4.0): Table 1 TyD (horizontal tympanum diameter) and ED rows for the holotype and two paratype males are readable and match the printed TyD/ED ratio row (0.55, 0.61, 0.58), but no ASW species page appeared in my search results (only the genus page, which lists no species). File if an ASW page is reached. The third column prints PNGNM / SJR 13932 without a registration number.
- Kurixalus lenquanensis (ZooKeys 694: 71-93, 10.3897/zookeys.694.12785): Table 4 ED and TD per voucher read in two columns (14 vouchers, holotype KIZ 170180Y), but the reader declined the whole rows and no ASW page was reached.
- Odorrana sangzhiensis (ZooKeys 1024: 91-115, 10.3897/zookeys.1024.56399): Table 1 ED row readable (holotype CSUFT 4308220051 5.2 and paratypes) but the TYD row is cut off in the XML and no ASW page was reached (AmphibiaWeb only).
- Cyrtodactylus arunachalensis (Evolutionary Systematics 5(1): 13-23, 10.3897/evolsyst.5.61667): Table 1 OD (eye diameter) and EL rows readable, but no Reptile Database page was reached; the text and the Sex row disagree for BNHS 2776 and 2777; the table labels EL 'ear diameter' while the Methods say 'ear length'.
- Pristimantis ashaninka (already on main, d354); Pristimantis sira (holotype ED only); Duttaphrynus ZSE 97(2): 451-470 (Table 1 TYD and EL = eye length, no holotype rows, text-table conflict for SDBDU 2006.6370; no ASW page); Leptobrachella 'GIB196405' (female not in printed type list); Takydromus yunkaiensis (no ED in the XML); Boulenophrys lichun (ZooKeys 1216, 2024, not older); a ZooKeys 2016 microhylid table (article 8295) with implausible ED/TD row values.

## Desk disposition after audits 1162 to 1166 (4 November 2026)
The two Leptobrachella bashaensis holotype lines (GIB196403, TMP 2.2 and EYE 2.9, file lines 5 and 6) were dropped: the holotype description prints TMP/EYE 0.60, EYE/HDL 0.35 and EYE/SNT 0.88 while Table 3 gives 0.76, 0.31 and 0.83, so text and table disagree (the printed ratios fit paratype GIB196404 better). Counted errors: 16 (the two holotype lines, plus lines in audits 1163 and 1164 counted as errors for wording faults: reader tooltip text in quotes, type material not quoted as printed, incomplete licence sentences, wrong where path, reader artefact cited as unit source). Values, specimen codes and sexes matched the publisher tables on every other line. Kurixalus yangi is valid on ASW (the K. naso senior-synonym comment is disclosed in each note). 28 of 30 merged. Desk lesson: a holotype record needs the holotype description ratios checked against the table before filing.
