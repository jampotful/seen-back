# desk-d455 progress

Angle: non-spider unit (the brief's later paragraph says this unit MUST be non-spider; its first paragraph lists spider angles, and the later instruction was followed). Open-access amphibian and reptile papers that print eye diameter in millimetres. 10 records (log docs/views/evidence/desk-d455.jsonl), trait eye_diameter_mm. check.py: 0 problems for desk-d455 (the --require-evidence-kind and plain runs report problems only in other units' files). About 40 WebSearches.

## Filed
- PeerJ 13: e19760 (10.7717/peerj.19760; Reyes-Puig et al., 2025) Osornophryne backshalli (Bufonidae): six type-series specimens (2 males, holotype female and 3 paratype females) from the Table 2 ED row; caption gives mm.
- PeerJ 13: e20512 (10.7717/peerj.20512; Loza-Carvajal et al., 2025) Pristimantis paganus: holotype female ED 3.92 (heading 'Measurements (in mm) of holotype'). ED is defined only by the Table 3 row label 'Horizontal eye diameter (ED)'; the Methods text returned does not define it (judgment call, stated in conditions).
- ZooKeys 1253: 255-275 (10.3897/zookeys.1253.161412) Calamaria synergis: paratype ANU ZR25021 EyeD 0.8 mm (Variation sentence).
- Zoosystematics and Evolution 102(2): 701-718 (10.3897/zse.102.188045) Calamaria incredibilis: holotype eye diameter 0.8 mm.
- ZooKeys 1277: 245-280 (10.3897/zookeys.1277.187107) Calamaria similis: holotype eye diameter 0.8 mm.

## Weak spots
- All text came through the WebFetch summariser (PeerJ pages and PDFs, Pensoft article_preview pages); quotes and neighbouring sentences are tool-returned pieces. The Osornophryne column-to-code mapping is the tool's reading of Table 2 (male and female range columns agree with it).
- Calamaria incredibilis: no Reptile Database page reached (validity UNCHECKED). Calamaria synergis and C. similis: Reptile Database pages opened; both print family Colubridae in the table and Calamariidae in the reference, the paper's Calamariidae used.
- Crossref version of record not checked for any paper. Licence sentences came as opening clauses.
- No Class, Order or Family headings are printed on the Calamaria pages (ranks only in the title).

## Not filed and why
- Calamaria synergis holotype (EyeD 1.2 mm): inside a long semicolon-joined Description sentence over 40 words.
- Boulenophrys daxuemontis (BDJ 13 e153987, CC BY 4.0, ED in Table 3 in mm, per-specimen values read): the tool could not return whole table rows (22 columns) and the only text eye sentence is a percentage; the paratype code CIB JL20230630026 in the type list shows as CIB WX20230630026 in the table. Lead: file the holotype CIB JL20230630024 (ED 4.15) if the whole table row can be quoted.
- Calamaria hunanensis (Zoological Research: Diversity and Conservation 3(1): 1-12): page metadata says CC BY 3.0 while the PDF prints a Non-Commercial licence (conflicting tag); holotype EyeD 0.7 mm in a long list.
- Pensoft Dasypeltis albigularis (Herpetozoa 39: 343-366): no eye measurement. ZooKeys Odorrana feii, Brachytarsophrys wui, Boulenophrys changyangensis, PeerJ Leptobrachium (e20397), Nyctibatrachus (PeerJ 14 e20895), Luperosaurus alvarezi (PeerJ 14 e20504): no publisher article page appeared in search results.

## Desk disposition after audits (2 November 2026)
Audit 906 confirmed the six Osornophryne backshalli lines (each ED value sits under its printed specimen-code header; the quote now stops before the pooled means). Audit 907 corrected Pristimantis paganus (ED defined only by the Table 3 row label 'Horizontal eye diameter (ED)', in mm) and the family of the Calamaria lines (Colubridae, Calamariinae per the Reptile Database, not Calamariidae); Calamaria incredibilis (line 9) is dropped because no Reptile Database page was reached. 9 records merged. The Calamaria Methods do not define eye diameter; the lines stay eye_diameter_mm because the quoted sentence prints "eye diameter 0.8 mm" (same open owner question as d452). Counted errors: 3 (the three Calamaria family faults, one of them dropped).
