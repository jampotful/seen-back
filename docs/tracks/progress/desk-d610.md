# desk-d610 progress

Angle: new-species papers on Asian, African and Neotropical frogs and salamanders that print an ED definition and per-specimen mm values (Pensoft previews and XML reached from my own searches; Amphibian Species of the World pages). The OLD-ANGLE paragraph of the brief was ignored. Trait eye_diameter_mm, evidence_kind anatomical_measurement. Log: docs/views/evidence/desk-d610.jsonl. 14 records. check.py: 0 problems (plain and --require-evidence-kind). 40 WebSearches.

## Filed
- ZooKeys 927: 127-151 (10.3897/zookeys.927.48733) Raorchestes rezakhani: 4 adult males (holotype JnUZool-A0419 and 3 paratypes), Table 3 row 4, 'ED eye diameter (horizontal diameter of the eye)' in the Methods list. 4 records.
- ZooKeys 914: 127-159 (10.3897/zookeys.914.36604) Nidirana guangdongensis: holotype and 7 paratypes (5 males, 3 females in total), Table 6 ED row. 8 records.
- Zoosystematics and Evolution 100(3): 1107-1120 (10.3897/zse.100.119662) Pristimantis ruidus: two newly collected adult females, Table 1 rows. 2 records. This is a rediscovery paper, not a new-species description; the third Table 1 row (holotype AMNH 17590, 4.5 mm) is Lynch's 1979 value and was not filed.

## Weak spots
- Text came through the WebFetch page reader (Pensoft article_preview pages and the XML reached with a search-result URL); table cell order and column-to-specimen mapping are the reader's reading. Quotes use the printed short forms (ED), not the reader's expanded abbreviations.
- Raorchestes Methods list entry is returned by the reader as 'ED (eye diameter) eye diameter (horizontal diameter of the eye);'; the printed layout of that bullet is not certain.
- Raorchestes rezakhani year 2020 and Nidirana 2020 are inside the 2019-2024 angle; Pristimantis ruidus is 2024.
- Neither ASW page prints an explicit 'valid'; each is described in the record note.

## Not filed and why
- Dendropsophus cannatellai (Evol. Syst. 9(1): 7-31, 10.3897/evolsyst.9.135431): only the holotype ED 3.34 mm is printed (no per-specimen table); ASW search returned only the genus page. Lead if an ASW species page appears.
- Stumpffia megsoni: ASW search returned only the genus page and other Stumpffia species.
- Hypselotriton huanggangensis (ZooKeys 1208: 331-346): ASW species page appeared in my results but fetch returned robots_disallowed (not retried); the paper prints holotype ED 3.63 and only sex ranges otherwise.
- Osteocephalus vasquezi (Evol. Syst. 7(2): 237-251): holotype 'eye diameter 5.3 mm' in Description of holotype is fileable text, ASW species page appeared in results but fetch gave robots_disallowed.
- Pristimantis kayi (ZooKeys 1180): no P. kayi holotype ED block in the page; Table 2 gives only ranges; no ASW page.
- Boulenophrys yezhongensis (Herpetozoa 38: 117-136, 2025): holotype ED only as % HL; Table 3 gives ranges and means.
- Leptobrachella wumingensis, L. kungfu, L. verrucosa, L. xinshaoensis and Kaloula discordia/laosensis (eye length, no table reached): no mm values reachable. Gracixalus liusanjieae, Amolops gudao, Quasipaa taoi, Pristimantis similaris, Pristimantis sira, Odorrana sangzhiensis, Megophrys anlongensis, Chimerella mira, Rhacophorus dulongensis, Ingerophrynus chrysolophus, Tylototriton umphangensis (no ED) and others: already on main or progress notes.
- Leptopelis diffidens (ZooKeys 1023): holotype ED given only as ratios; per-specimen data in a supplement.
- Leptobrachella aspera and L. dorsospina (ZooKeys 995): no ASW species page reached; tables not read.
- Pensoft public.pensoft.net redirects for PDFs (Herpetozoa 165088, ZSE 166556) were not followed (URL not from my search results).

## Desk disposition after audits 1227, 1228, 1229 (4 November 2026)
14 eye_diameter_mm records filed, 14 merged, 2 counted errors. Pristimantis ruidus (2 records, ZSE 100(3)): author initials corrected to "Salagaje M. LA", an unprinted "ruidis" spelling claim removed, and MUTPL 1613's adult status rested on the Table 1 State cell only (not the ovaries sentence about DHMECN 19106). Raorchestes rezakhani (4) and Nidirana guangdongensis (8) had 0 value errors; their wording faults (unprinted column headers, regrouped paratype list, missing heading authority and heading-absence note) were corrected. Nothing dropped. Not filed: Dendropsophus cannatellai (holotype only, no per-specimen table, no species ASW page), Osteocephalus vasquezi and Hypselotriton huanggangensis (ASW robots_disallowed, not worked around), Pristimantis kayi, Stumpffia megsoni.
