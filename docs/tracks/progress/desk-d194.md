# desk-d194 (31 October 2026)

Animal sensory-trait records from open-access MDPI pages (WebFetch of the publisher page; DOIs and author lists checked on Crossref).

Records filed (8, all grade m):
- Austruca lactea, 250 Hz vibration: leg-muscle ATP lower, lactate higher (Joo et al. 2025, Biology 14(8): 962). Abstract and Results disagree on 120 Hz lactate; only the 250 Hz abstract sentence is filed.
- Carcinus maenas, no antennae or antennule response to mechanical stimuli (Kasiouras et al. 2024, Biology 13(11): 851).
- Lycorma delicatula, no EAG response at 0.5 ng (Faal and Cooperband 2024, Insects 15(3): 162).
- Schizothorax kozlovi, green preference (Wang et al. 2026, Fishes 11(4): 200).
- Sebastiscus marmoratus, three records (Qi et al. 2024, Animals 14(11): 1701): wild red preference, hatchery-reared null (abstract says weaker response, Results says none), negative phototaxis in yellow and blue.
- Canis familiaris hearing thresholds at 0.5, 4 and 20 kHz (Guerineau et al. 2024, Vet Sci 11(2): 67); abstract and Results differ at 4 kHz (14.0 vs 14.5).

Held out:
- Schizopygopsis malacanthus (same Fishes sentence): FishBase notes S. chengi is valid in ECoF, so the accepted name is unsettled.
- Eilerts 2018 Aedes aegypti (mdpi 2075-4450/9/4/147): fetch blocked (PROVENANCE_REQUIRED), not retried.
- Pham 2021 Vietnam bats (Diversity 13(1): 18): the fetch returned table rows with columns elided and headers not seen; Discussion values were fragments.
- Zhang 2025 Anoplophora glabripennis EAG (Insects 16(8): 781): species already filed by d192; sentences too long.
- Rana dybowskii light spectrum (Animals 15(14): 2066): sex ratio and hormones, not a sense trait.
- Niklaus rat ERG, Faraone Ixodes: no open page reached.

Name checks: FishBase pages for Sebastiscus marmoratus and Schizothorax kozlovi list them as main entries without an explicit validity line; Austruca lactea, Carcinus maenas and Lycorma delicatula already stand in main logs. Fetches to catalogue hosts (checklistbank, fishbase search) were denied by permission; not retried.

Searches: 23 WebSearch calls. No search or wanted records written.

## Desk disposition after audit 278

Audit 278: 5 of 8 records in error (62.5%; lines 1, 2, 3, 6, 7), none unfixable. Pooled audits 172 to 278: 245 of 583 (42.0%). All eight merged with the auditor's replacement text and uncounted fixes.

- Line 8 is filed as Canis lupus familiaris (subspecies), matching views/dog.json and most main rows, because the paper's Canis familiaris is a synonym in gbif-names.tsv. Family Sebastidae on the Sebastiscus rows follows OBIS; Catalog of Fishes gives Scorpaenidae: Sebastinae.
- Austruca line 1 now carries stimulus level and exposure time and describes a metabolic exposure response, not a sensory one. Carcinus and Lycorma nulls state their limits (1.0 g maximum hair, acid applied first; responses from 5 ng).

Owner questions: dog naming (move the 18 main rows under Canis familiaris to Canis lupus familiaris?); whether GBIF Backbone suffices for Schizothorax kozlovi; whether Joo 2025 leg-tissue metabolite results belong under sense_vibration.
