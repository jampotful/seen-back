# desk-d473 progress

Angle: amphibians and reptiles only (no spiders). Open-access Pensoft papers that print an eye measurement in millimetres per named specimen. 5 records (log docs/views/evidence/desk-d473.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement. check.py: 0 problems for desk-d473 (plain and --require-evidence-kind; problems reported only in other units' files). About 40 WebSearches.

## Filed
- Zoosystematics and Evolution 102(2): 649-658 (10.3897/zse.102.179377) Andrias yaoluopingensis (Cryptobranchidae): holotype HSA25201 (male) EL 4.38 and paratype HSA25202 (female) EL 4.65, Table 2 EL row. The Methods define 'greatest diameter of eye (EL)', measured with digital calipers to 0.01 mm.
- Biodiversity Data Journal 13: e153987 (10.3897/BDJ.13.e153987) Boulenophrys daxuemontis: three paratype rows of Table 3 (ID 1 CIB WX20230630006 ED 3.54, ID 4 CIB WX20230630007 ED 4.17, ID 5 CIB JL20230630025 ED 4.21), whole 22-cell rows. The holotype row (ED 4.15) is already on main as desk-d457.

## Weak spots
- All text came through the WebFetch page reader; the Andrias licence sentence came as its opening clause plus a summary, and the EL row cells and column mapping are the reader's reading of the XML. The article_preview URL for Andrias returned a different paper, so only the XML download was used.
- Boulenophrys rows are the reader's cell-by-cell output; ED agrees with its earlier column-wise listing. Paratype sex for CIB WX...006/007 comes from the table Sex cell (the type fields record none).
- ASW pages print no explicit 'valid'; Crossref not checked.

## Not filed and why
- Boulenophrys daxuemontis ID 3 row: voucher cell CIB WX20230630026 differs from the type list CIB JL20230630026.
- Trimeresurus liqibini (ZSE 102(1), CC0, holotype GXNU251216 ED 3.54, paratype 2.94 as read from a preview): no Reptile Database or ASW page appeared in my search results (only Wikispecies, Plazi, iNaturalist).
- Plagiopholis yangi (Evolutionary Systematics 10(1): 85-92, holotype KIZ2025059 ED 2.6, Table 3 and Description): no Reptile Database page in results.
- Scincella gigas (ZSE 102(4): 1047-1063) and Hebius yangi (ZooKeys 1289: 141-157): paper pages found, no Reptile Database page in results; text not read.
- Scincella jinchuanensis (ZSE 102(2) 575-588), Goniurosaurus wuzhengjuni (ZSE 102(2) 611-620): Methods and Tables 4 and 1 have no eye diameter row (Reptile Database pages reached). Tylototriton wufengensis (ZSE 102(1) 181-197): measurements only in a supplement. Tylototriton vietnamirabilis: eye length only (d345). Sphenomorphus lingnanensis: no eye measurement (d343).
- Cyrtodactylus nebulicola (ZooKeys 1278: 317-338; Reptile Database page reached): the article_preview id 186655 returned a spiders paper (Hahniidae) on three reads, so no gecko text was read. Leptobrachium mechuka (ASW page reached) and L. somani: no publisher page in results. Amolops kamal, A. minhlei, Oreonectes weii: no open publisher page reached.

## Desk disposition after audit 948 (3 November 2026)
Audited by a fresh Opus agent. All 5 records merged (Andrias yaoluopingensis holotype and paratype, ZSE 102(2); Boulenophrys daxuemontis paratypes ID 1, 4, 5, BDJ 13 e153987). ASW validity, values, codes, sexes and DOIs confirmed; nothing repeats main. Faults (Methods heading printed 'Material and methods', EL item inside a 309-word sentence, licence summarised instead of quoted whole, Table 3 caption cut without a mark, omitted caliper sentence, an unsupported claim about the Description) corrected with the auditor's replacement text.
