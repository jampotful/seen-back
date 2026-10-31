# desk-d195 progress

Unit brief task (plant screening) was superseded: animal sensory-trait records from open-access papers.

Records filed: 6 in docs/views/evidence/desk-d195.jsonl
- Coloeus monedula (paper prints Corvus monedula): colour_vision x1 (Results, both birds above chance), colour_vision x1 and behaviour_vision x1 (abstract sentences, partial) - Lingstadt, Apostel, Rose 2025, Front Physiol 16:1543469
- Astyanax mexicanus: sense_hearing (Results 3.1), absolute_sensitivity null (ERG, Results 3.3) - Enriquez et al. 2023, Front Ecol Evol 11:1085975
- Culex territans: sense_chemical null (no flight to CO2 at 2100 and 30,000 ppm) - Reinhold et al. 2022, Insects 13(1):92

Held, not filed
- Ixodes scapularis, Faraone et al. 2020 Insects 11(8):502: abstract sentence on concentration-response was seen whole and Crossref was checked, but no reachable authority confirmed the species name (ITIS pages returned an unrelated cached record; Catalogue of Life blocked as provenance).
- Culex territans thermopreference, Culex quinquefasciatus/tarsalis: sentences over 40 words or returned as fragments.
- Oophaga pumilio retinal thresholds (Walkowski et al. 2024, PLoS ONE 19(11): e0312578): only fragments returned.
- Bufo bufo orientation arena (Pail et al., Herpetozoa 33): sentences seen but no fitting trait (not magnetic-specific).
- Pham et al. 2021 Vietnam bats: doi.org URL refused as provenance. Athetis dissimilis EAG, Tripneustes gratilla LED behaviour: abstracts returned only as paraphrase.
- Dybowski frog tadpole light (Animals 15:2066), honey bee hive RH (Insects 15:800), saw-whet owl (Karger, not open): not sensory records or not open.

Refusals/limits: WebFetch returned PROVENANCE_REQUIRED for derived or redirected MDPI URLs, FishBase, doi.org/10.3390/d13010018 and a Catalogue of Life search; ITIS servlet gave an unrelated cached page. WebFetch often refused whole sentences over about 125 characters; only sentences returned in full were filed. WebSearch use reached about 41 calls (cap 40), one over.

## Desk disposition after audit 279

Audit 279: 2 of 6 records in error (33.3%; lines 5 and 6), none unfixable. Pooled audits 172 to 279: 247 of 589 (41.9%). All six merged with the auditor's replacement text and uncounted fixes (lines 2 and 3 keep partial as filed).

- Astyanax line 5 now states that the ERG comparison is relative to each fish's own 425 nm b-wave, with sample sizes and the p = 0.054 and 0.055 trend; it stays under absolute_sensitivity pending owner question 1. Culex line 6 carries the CO2-pulse design, the authors' two explanations and the species contrast.
- The progress note's remark that no fish authority was reachable is superseded: Catalog of Fishes lists Astyanax mexicanus as valid. The unit used 41 WebSearches against a cap of 40.

Owner questions: where relative ERG spectral-sensitivity comparisons belong (absolute_sensitivity, a new key, or held); whether Lingstädt 2025 lines 2 and 3 (one finding from two adjacent abstract sentences) are both kept; whether GBIF Backbone plus the Mosquito Taxonomic Inventory suffices for Culicidae.
