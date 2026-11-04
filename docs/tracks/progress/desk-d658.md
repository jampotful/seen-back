# desk-d658 progress

Unit: desk-d658. Angle: (A) three held lines from d657 (Hordeum vulgare sense_magnetic, Triticum aestivum sense_thermal, Solanum lycopersicum sense_thermal) once a WFO species page opens; (B) crop and model plant species by species.
evidence_intake: evidence-kind-v2
intake_base: 6829f5cefdf6f0fbea6ae4721c72991ff85fe507

## Status (in progress)
- WFO pages reached from own WebSearch results and opened with WebFetch (wfoplantlist.org taxon pages opened for this unit; no workaround used):
  - Hordeum vulgare: wfoplantlist.org/taxon/wfo-0000875054-2019-05 (accepted, species, older snapshot flag)
  - Triticum aestivum: wfoplantlist.org/taxon/wfo-0000905667-2023-06 (accepted, species, Linnaeus 1753, older snapshot flag)
  - Solanum lycopersicum: wfoplantlist.org/taxon/wfo-0001029216-2021-12 (accepted, older snapshot flag)

## Batch 1 (part A): 3 records filed in docs/views/evidence/desk-d658.jsonl
- Hordeum vulgare, sense_magnetic, physiological_response (Shabrangy et al. 2021, Front Plant Sci 12: 622795). Contrary result kept in conditions: on MS medium prolonged exposure decreased germination; 7 mT was the optimized choice among several untabulated treatments; no germination percentages in the text.
- Triticum aestivum, sense_thermal, physiological_response (Fan et al. 2021, Front Plant Sci 12: 706567). Yield minus 17% under post-anthesis night warming; 3 blocks, two cultivars pooled in the quoted figure, passive membranes confound humidity and wind.
- Solanum lycopersicum, sense_thermal, physiological_response (Ohtaka et al. 2020, Front Plant Sci 11: 577235). n = 7; chamber replication not stated.
- All three: POWO accepted pages and wfoplantlist.org taxon pages opened with WebFetch from own search results (no workaround used; pages carry an older-snapshot warning). CC BY sentence read on each publisher PDF.

## Part B checked, not filed (about 37 WebSearches used in total, no classifier denial, no PMC/ncbi fetch)
- Setaria viridis cold stress (Carvalho et al. 2022, Pesq Agropec Bras 57: e02424, CC BY read on SciELO page): POWO accepted page opened, but only WFO genus Setaria and S. verticillata pages surfaced (wfoplantlist), no species page for S. viridis in three searches; held. Note for a later unit: biomass not significantly reduced in the vegetative stage, minus 25% in the reproductive stage, against an abstract that states a decrease without that qualifier; n only 'five or ten replicates', abrupt cold used a second chamber.
- Linum usitatissimum static magnetic field (Calic et al. 2023, Agriculture 13(11): 2120): the page text printed no Creative Commons sentence (only a rights metadata tag), so held.
- Brachypodium distachyon ambient temperature (Li et al. 2019, Front Plant Sci 10: 1011) and Fragaria vesca flowering (Front Plant Sci 2022): panels of accessions pooled, held. Prunus persica base temperature (Bielenberg and Gasic 2022): 54 accessions, no control, held.
- Camellia sinensis shade against cold (Zaman et al. 2023, Front Plant Sci 14: 1114988): shade against low temperature in one field season, replicate counts inconsistent, held. Camellia heat (Sci Rep 2024): no unstressed control, held.
- Coffea arabica warm temperature (Oliveira et al. 2020, Front Plant Sci 11: 1113): transcript focus, one chamber per temperature, no clear physiological endpoint, held.
- Vicia faba heat (Bishop et al. 2016, J Agron Crop Sci 202: 508): only a repository copy and PMC reachable, no publisher page, held.
- Lotus japonicus cold (transcriptome only), Pisum sativum magnetic (non-CC Egyptian and Indian journals), Sorghum bicolor, Beta vulgaris, Nicotiana benthamiana, Medicago truncatula, Cannabis sativa, Allium cepa, Phaseolus vulgaris volatiles, Solanum tuberosum touch: no open primary paper with a publisher page surfaced.

## Final
3 records filed (check.py and --require-evidence-kind: 0 problems; check_submission: 3 new, 0 problems). Scratch folder deleted.
