# desk-d612 progress

evidence_intake: evidence-kind-v2
intake_base: 324e2eed73a6b44f501623463e2d898f20944f75

Angle: frogs and salamanders (Pensoft XML/preview with WebFetch offset), eye_diameter_mm, anatomical_measurement. Started 2026-11-04. No records yet.

Batch 1: 8 records (Leptobrachella aspera, ZooKeys 995, Table 4 EYE row, 4 specimens; Raorchestes rezakhani, ZooKeys 927, Table 3 ED row, 4 adult males). Log docs/views/evidence/desk-d612.jsonl.

Final: 8 records, check.py 0 problems (plain and --require-evidence-kind). About 40 WebSearches. Records: Leptobrachella aspera (ZooKeys 995: 97-125, 10.3897/zookeys.995.55939, ASW page opened) 4 specimens; Raorchestes rezakhani (ZooKeys 927: 127-151, 10.3897/zookeys.927.48733, ASW page opened) 4 adult males. Table column-to-specimen mappings are the page reader's.

## Not filed and why
- Leptobrachella dorsospina: its measurement table was not reachable (preview text covers only L. aspera; XML at 85469 characters carries only the GenBank table); no ASW page.
- Hypselotriton huanggangensis (ZooKeys 1208, holotype ED 3.63 in Table 2): ASW species page refused (robots_disallowed), not retried.
- Odorrana sangzhiensis (ED row read): ASW page is only Rana sangzhiensis Shen 1986, identity unresolved (as d591).
- Paroedura manongavato (ZooKeys 1181): Table 2 lists the holotype under P. rennerae columns and ED is NA for the manongavato column; not filed.
- Cnemaspis lineatubercularis (ZooKeys 932): XML (85685 characters) holds only the specimen/GenBank table; offset reads found no morphometric table.
- Cyrtodactylus meersi / myintkyawthurai (PeerJ 6:e5575): peerj.com page returned no byline and no Creative Commons sentence at offset 0 or 80000; dead.
- Already on main: Pristimantis similaris (d594), Hyloscirtus tolkieni (d576), Amolops dafangensis (d604). Blommersia nataliae Table 1 row pools two species (29 values), not quotable. Kurixalus berylliniris/wangi Table 1 row pools two species. Tylototriton umphangensis and T. pasmansi: no ED/orbit row. Odorrana nagao, O. feii, Tylototriton vietnamirabilis, T. gaowangjienensis: page text stops at the abstract. Stumpffia megsoni: on main (d605).
- Finding: Pensoft /download/xml/ pages in this reader mostly drop the tables; article_preview.php URLs carry them. The offset parameter returns nothing useful when the page is under 100000 characters.
