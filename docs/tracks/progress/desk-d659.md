# desk-d659 progress

Angle: plant species groups (trees/shrubs, weeds, ornamentals/medicinals, aquatic). Unit field: desk-d659.
evidence_intake: evidence-kind-v2
intake_base: 24ee6bed44c4b8f82a7d220b207a1bcb78f457d1
Acknowledgement: checkout at the intake_base above; rules.md (31 Oct 2026) and the unit prompt read before drafting.

## Main grep (species with no evidence rows on main)
Quercus ilex, Eucalyptus globulus, Salix babylonica, Morus alba, Senecio vulgaris, Rosa chinensis, Tulipa gesneriana, Eichhornia crassipes, Azolla filiculoides.

## Filed
1 record (docs/views/evidence/desk-d659.jsonl): Posidonia oceanica, sense_thermal, physiological_response, Pazzaglia et al. 2020 (Front. Mar. Sci. 7: 564805), CC BY sentence read on the publisher PDF. Design: 12 aquaria, 3 per treatment, 24 C control vs 30 C, crossed with nutrients, 5 weeks, two sites; the temperature effect on shoot mortality is significant for the EU site only (Table 1, P = 0.01 vs OL P = 0.31); relative growth rate null. POWO and WFO pages opened from own search results (both accepted).

## Not filed (checked, with reason)
- Senecio vulgaris, PeerJ 2346 (Ndihokubwayo et al.): no light/dark or other sense comparison, one constant regime.
- Ambrosia artemisiifolia, Yair et al. 2020 Front. Agron. (10.3389/fagro.2020.573860): light/dark germination already on main (desk-d111); the temperature null (shoot biomass unaffected) could not be quoted because WebFetch returns only the first ~125 characters of the sentence.
- Zostera marina, Beca-Carretero et al. 2021 (Front. Mar. Sci. 8: 731152): no Creative Commons sentence found on the PDF text; no control temperature; held.
- Tulipa gesneriana scent vs temperature (Kishimoto et al., Hort. J.): cultivars, no CC sentence on the page.
- Pinus taeda bending (Dranski et al.): outside the species groups, only regression-estimated values readable, text and fitted curves disagree.
- Populus nigra bending (De Zio et al. 2020): no unbent control. Eucalyptus (Vilasboa et al.): other species. Lemna minor, Eichhornia, Salix, Morus: chemical or nutrient stress designs, not sense traits.
- Fagus sylvatica warming (Rubio et al., Plants 14: 1525): only PMC and a third-party mirror reached, not filed.
- Lolium perenne Frontiers 2023.1149832: page unreadable (binary).

Search total: about 38 WebSearches (unit asked for about 40). Results: 1 filed record, checks 0 problems (check.py, --require-evidence-kind, check_submission).
