# desk-d451 progress

Angle: non-spider unit. Open-access amphibian and reptile papers that print eye diameter (ED) in millimetres. 21 records (log docs/views/evidence/desk-d451.jsonl), trait eye_diameter_mm (the Methods of every paper define ED as eye diameter; same key as main). check.py: 0 problems, also with --require-evidence-kind. About 30 WebSearches.

## Filed
- ZooKeys 1291: 93-110 (10.3897/zookeys.1291.193210) Vitreorana micaelae: holotype line ED 2.1 and Table 1 male mean ED 2.1 (n = 10).
- ZooKeys 1282: 205-228 (10.3897/zookeys.1282.187506) Pristimantis etsa: holotype female ED 4.0.
- ZooKeys 1269: 83-105 (10.3897/zookeys.1269.162260) Pristimantis fergusoni: holotype female ED 2.3; Table 3 female mean 2.38 (n = 6) and male mean 1.83 (n = 8).
- Zoosystematics and Evolution 101(4): 1397-1408 (10.3897/zse.101.148507) Leptobrachella weixinensis: Table 1 ED of holotype and two male paratypes (3.6, 3.6, 3.9).
- ZooKeys 1253: 131-160 (10.3897/zookeys.1253.161933) Cyrtodactylus makwanpurgadhiensis holotype 3.6; C. chure holotype 4.1 and three paratypes (3.7, 3.6, 3.8), from the single combined Table 2 ED row.
- Zoosystematics and Evolution 101(4): 2251-2266 (10.3897/zse.101.166556) Boulenophrys nebulosa: seven specimens (3 males, 4 females) from Table 2.

## Weak spots
- All text came through the WebFetch summariser (article_preview pages), so quotes and neighbouring sentences are tool-returned pieces. Table rows are quoted as cells joined by single spaces; specimen-to-value mapping comes from the header and Sex rows as returned.
- Licence sentences came as opening clauses; Crossref version of record not checked.
- Validity: ASW and Reptile Database species pages opened from search results list each name as an entry; none states the word "valid".
- P. fergusoni: paper says Strabomantidae, ASW path says Craugastoridae (family used); the paratype list counts 6 females but the tool saw 5 codes; the holotype line ends in garbled items (cut and marked).
- P. etsa male paratype (ED 2.8) sits in a Variation sentence over 40 words: not filed. Vitreorana micaelae page prints no Class, Order or Family heading.
- Cyrtodactylus: d366 skipped this paper for run-on sentences; the Table 2 row is short, so used. Other makwanpurgadhiensis paratypes (384-389) not filed.

## Leads not filed
- Same-search ZSE papers Odorrana feii (ZSE 101(4): 1949-1964, 10.3897/zse.101.161151), Brachytarsophrys wui (ZSE 102(1): 71-85, 10.3897/zse.102.161437), Boulenophrys changyangensis (ZSE 101(3): 1213-1226, 10.3897/zse.101.155859): only truncated XML copies and figure pages reached, no article_preview page in search results.
- PeerJ 14 e20397 Leptobrachium mechuka, L. somani (10.7717/peerj.20397): no peerj.com page in search results.
- Non-open or other: Limnonectes meratusensis (Species Diversity 30(2)), Rhacophorus hujianshengi (Pakistan J. Zool.), Pristimantis papers on novataxa not opened.
- Harvestman, scorpion, mite, insect and crustacean searches returned only repository copies or non-open items; no eligible paper reached.

## Desk disposition after audits (2 November 2026)
Audits 890-892 judged all 21 lines. Lines 2, 5 and 6 (Table means with ranges and SD for Vitreorana micaelae and Pristimantis fergusoni) are pooled records and are dropped. Line 1 had a quote cut without a cut mark (fixed). All other faults were licence-sentence cuts, heading paths and note wording, fixed with the auditors' replacement lines. 18 records merged. Counted errors: 4 (3 dropped, 1 quote cut).
