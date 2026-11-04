# desk-d603 progress

Angle: novataxa Pensoft XML route (searches shaped like novataxa "Journal: <journal>" <taxa> new species pensoft download xml) for sensory_anatomy records: tympanum diameter (TD/TYD) and lizard ear diameter, in ZooKeys, Evolutionary Systematics, Herpetozoa and Biodiversity Data Journal. 38 records (log docs/views/evidence/desk-d603.jsonl), trait sensory_anatomy, evidence_kind anatomical_measurement, one record per specimen. check.py: 0 problems (plain and --require-evidence-kind). About 36 WebSearches. The OLD-ANGLE paragraph was not followed.

## Filed
- ZooKeys 1117 (10.3897/zookeys.1117.85787) Rhacophorus napoensis (Rhacophoridae): 5 males, Table 2 TD row ('the maximum diameter of tympanum'); holotype YU000172 TD 3.4. Same paper's ED rows are d596.
- ZooKeys 1227 (10.3897/zookeys.1227.131357) Amolops gudao (Ranidae): holotype and 3 paratypes, Table 1 TD row (ED rows are d513).
- Herpetozoa 37: 149-156 (10.3897/herpetozoa.37.e121610) Amolops truongi (Ranidae): 4 non-type adult males from China, Table 2 TD row.
- Evolutionary Systematics 7(1): 183-194 (10.3897/evolsyst.7.102425) Scinax pyroinguinis (Hylidae): holotype and paratopotype, Table 1 TD row (Methods list 'tympanum diameter (TD)').
- ZooKeys 1021 (10.3897/zookeys.1021.60402) Cyrtodactylus zhenkangensis and ZooKeys 1084 (10.3897/zookeys.1084.72868) C. menglianensis (Gekkonidae): 5 and 4 type specimens, Table 2 ED row where ED is EAR diameter ('ear diameter, greatest diameter of ear').
- Biodiversity Data Journal 11: e101986 (10.3897/BDJ.11.e101986) Nidirana chongqingensis (Ranidae): holotype and one paratype, Table 2 TD row (printed with a space after the decimal point, quote keeps it).
- ZooKeys 1266 (10.3897/zookeys.1266.176724) Sphenomorphus tamchucensis (Scincidae): 11 type specimens, Table 1 TYD row (EL rows d476, ear-opening description d574).
- ZooKeys 1268 (10.3897/zookeys.1268.174678) Hemiphyllodactylus ziegleri (Gekkonidae): holotype only, Table 2 EarD row (paratype sexes conflict between type list and table, so not filed).

## Weak spots
- All table cells and column-to-code mappings are the WebFetch page reader's cell-by-cell reading of Pensoft XML or article_preview pages; licence sentences and Methods wording came back in pieces and were joined.
- Several rows are ones whose same paper already has eye_diameter_mm rows on main (d596, d513, d476, d482); the tympanum or ear measure is a different trait value, as d600 did for Amnihyla kikori.
- Methods for Scinax pyroinguinis and Nidirana chongqingensis list 'tympanum diameter (TD)' as a variable name with at most a short gloss.
- Scinax pyroinguinis Figure 4 caption prints the paratopotype as CORBIDI 24700; Table 1 and the type list print 24670.

## Not filed and why
- Zhangixalus thaoae (ZooKeys 1197), Raorchestes hekouensis (d580), Gracixalus truongi (d588), Raorchestes malipoensis, Pristimantis etsa, Spinomantis lavabato/lakolosy (d586), Hyloscirtus tolkieni (d576), Amolops dafangensis (XML cut before the description): on main or no values reachable.
- Ansonia karen (Vertebrate Zoology 71): table column TD is not defined (Methods define HTD and VTD), so not filed.
- Nidirana guibeiensis (ZooKeys 1135): TD only as a male range plus a single-female cell inside a summary row; Nidirana chongqingensis paratype SWU0001435 missing from the type list.
- Odorrana sangzhiensis (ZooKeys 1024): no matching ASW page (d591). Sphenomorphus puhoatensis, Hemiphyllodactylus lungcuensis, Cyrtodactylus nangunhe (no morphometric table in XML): value rows not reached.
