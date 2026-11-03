# desk-d525 progress

evidence_intake: evidence-kind-v2

Angle used: echolocation (sense_echolocation, evidence_kind physiological_response, one record per labelled value); the superseded reptile/fish paragraph was not followed. About 34 WebSearches; WebFetch only on URLs seen in search results. 10 records in docs/views/evidence/desk-d525.jsonl. check.py plain and --require-evidence-kind: 0 problems for the file.

## Filed
- Salsamendi E, Garin I, Arostegui I, Goiti U, Aihartza J 2012, Frontiers in Zoology 9: 30, 10.1186/1742-9994-9-30 (publisher page prints the Creative Commons Attribution License sentence; the licence URL is empty in the page text and no version is stated). Rhinolophus mehelyi RF 106.8 +/- 1.5 kHz (n = 16) and R. euryale RF 105.1 +/- 1.2 kHz (n = 24), hand-held at 30 cm, Results sentence and Table 1 row. Search that reaches the publisher PDF unfiltered: "What mechanism of niche segregation allows the coexistence of sympatric sibling rhinolophid bats? Salsamendi" (returns frontiersinzoology.biomedcentral.com/track/pdf/10.1186/1742-9994-9-30; the page itself came from an allowed_domains search). Authority pages mammaldiversity.org/taxon/1004713 and 1004682.
- Vu et al. 2025, BDJ 13: e165516, 10.3897/BDJ.13.e165516 (CC BY 4.0 sentence on the XML). Hipposideros griffini, Rhinolophus thomasi, R. perniger, Tylonycteris tonkinensis: peak frequency and mean call duration each (8 records), MDD pages 1004603, 1004754, 1004726, 1005782 reached from my own searches. Unfiltered search 'Vu 2025 Biodiversity Data Journal e165516 echolocation Hipposideros griffini Rhinolophus thomasi perniger Tylonycteris tonkinensis' returns the XML and article preview. Number of calls and the meaning of the +/- are not printed; T. tonkinensis names no individual or recording mode.

## Not filed and why
- PLOS ONE pone.0041744, pone.0148053, pone.0082614, river dolphins pone.0059284: journals.plos.org returned RATE_LIMIT_EXCEEDED on every fetch (5 tries, spaced by other work); not read.
- Pteronotus rubiginosus / P. alitonus (Filippi-Codaccioni 2018, BMC Evol Biol 18: 175, CC BY 4.0; MDD pages 1004867, 1004852 opened): the only values sentence (53.73 and 59.64 kHz, with 95% CI, n = 60 and 67) runs to about 60 words and opens with the exclusion of 15 hybrids and four outliers, so it cannot be quoted whole within 40 words without dropping a qualifier. Lead for an auditor with a table or shorter sentence.
- Guo 2026 R. affinis (ece3.73485), Maluleke 2017 (ece3.3251), Springer Yoh 2020 phyllostomids (s13364-020-00503-0), Vietnamese bats Sci Rep 2024 (nature.com; already held out CC BY-NC-ND by d326): Wiley, Springer, Nature fetches failed or tables were not returned.
- Greater horseshoe bat Animals 12: 3490: tables are images; no values in text. Aldasoro 2024 Animals 14: 3303: no RF values in text. Frontiers fevo.2022.908209 (R. sinicus parasites): model estimates only, no licence on the page. fevo.2022.934876: 226-species dataset, no per-species rows. Peerj 15292 (Patagonia): pooled clicks of unknown species. Sci Rep 2017 s41598-017-00959-2: literature review values. BDJ 34754 (Sierra Leone): n = 1 to 4 per species, aff. names. BDJ 141801: no values. ZSE 147349 and 144375, ZooKeys 145290: no values or already on main (d345/d347). fmars.2022.984333: already on main (d202).
- Diversity 13(1): 18 Vietnamese urban bats: already on main (d517).

## Weak spots
- All text came through the page reader (fragments of at most 125 characters, joined where marked). Crossref was not checked; licence rests on the printed sentence.
- Salsamendi Table 1 F value prints as '37. 2'; the sex split of the 40 bats is not stated.
