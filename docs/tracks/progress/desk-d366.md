# desk-d366 progress

Angle: multi-species frog/reptile morphometrics. 4 records from one paper, about 38 WebSearch/WebFetch calls. check.py: 0 problems.

## Filed (docs/views/evidence/desk-d366.jsonl)
- Zoosystematics and Evolution 93(2): 265-279 (10.3897/zse.93.11576): Choerophryne crucifer, C. multisyllaba, C. bisyllaba, Diagnosis ED/SUL ranges (sensory_anatomy, ratio); C. multisyllaba holotype TyD/ED 0.42.

## Weak spots
- Read through WebFetch summaries of the XML and article_preview pages, which truncate; the quotes are the tool's verbatim returns, not checked against raw text.
- Licence: the tool returned only the opening clause of the printed sentence; no Crossref check.
- Family from the ASW URL path on the C. crucifer page (the page states no family and notes a homonymy and Asterophrys use by Dubois et al. 2021); no page opened for the other two.
- Table 1-3 millimetre rows (holotype ED 1.8/1.9/1.9, TyD 0.6/0.8) not quoted: rows could not be read verbatim. Crucifer and bisyllaba tympanum sentences begin lowercase (possible run-in), so not filed.
- id=5411 article_preview returned this same paper, not the Raja Ampat Cophixalus paper its search title suggested.

## Not filed
- ZooKeys 1231 Hyloscirtus (10.3897/zookeys.1231.124926): taxonomic accounts truncated in every fetch.
- ZooKeys 1253 Cyrtodactylus Nepal: ED/HL sentences long run-ons; only one species' description readable.
- Single-species papers: Megophrys anlongensis, M. xianjuensis, Sphenomorphus puhoatensis (EL not ED), Eublepharis jhuma, Pristimantis fergusoni.
- Pristimantis sira (evolsyst.5.63674, CC0): Table 1 ED by sex for four species, not probed further.

## Desk disposition after audit 487 (2 November 2026)

Audit 487 found 1 of 4 records in error (25%), fixable: the Choerophryne bisyllaba ED/SUL range also covers a subadult (?) female, which the record did not state. Quotes, ratios, key, Microhylidae and the CC BY 4.0 licence held. No duplicates on main. Crossref refused the auditor twice, so the vor licence is unchecked. The paper's mm table would be a better source than the ratios (noted only, no records added). Replacement merged; check.py 0 problems.
