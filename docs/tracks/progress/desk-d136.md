# desk-d136 (30 October 2026): second WFO name-check attempt for held-out plant leads

Filed: 0 evidence records, 0 wanted lines. No lead could be released: with the new phrasings (a) "wfoplantlist.org taxon <Genus> <species>", (b) "list.worldfloraonline.org <Genus> <species>" and (c) "<Genus> <species> <authority> WFO accepted name", WebSearch never surfaced a WFO species page of snapshot 2022-06 or later for the accepted name. I opened every WFO candidate URL that search returned, and none was the target. I did not build URLs from IDs, and did not work around anything. No paper text was re-read (names are the gate); POWO status for Picea abies, Fagus sylvatica (d134) and Solanum tuberosum (d129) stays as those units recorded it.

Per species (3 to 4 searches each, pages opened):
- Picea abies: surfaced wfo-0000482007 (P. abies var. abies, accepted variety, Dec 2023), wfo-0000482012 (var. acuminata), wfo-1200027230 (Abies subgen. Picea, unplaced), wfo-0000510976 (Abies alba), genus-level 4000029600 and 4000046838. No species page.
- Fagus sylvatica: wfo-0000966434 appeared only as 2019-03 and 2019-05 snapshots; other hits were F. orientalis (wfo-0000966486), F. crenata (wfo-0000966414), infraspecific pages. No snapshot 2022-06 or later.
- Solanum tuberosum: surfaced S. etuberosum (wfo-0001027872), S. wittmackii, S. brevicaule, Solanecio tuberosus (wfo-0000062230) and a synonym variety page (S. tuberosum var. brachystylum, wfo-0001032045, Dec 2023, no accepted species named). No species page.
- Kobresia humilis: only wfo-0000407101, which is Carex alatauensis. No species page.
- Alyssum montanum: surfaced subspecies gmelinii (wfo-0000529669) and atlanticum (wfo-0000529665), prole humile (unplaced, wfo-1200108868), A. wulfenianum, A. pluscanescens, A. fastigiatum, genus 4000001442. No species page.
- Oryza sativa: genus 4000027352 and varieties/subspecies of O. sativa (synonym pages for subsp. communis, var. saginata, var. parasepica); wfo-0000882438 only as 2019 snapshots. No species page.

Duplicate check on main (docs/views/evidence and docs/views/audit/corrected, any trait): only the species names were grepped; none of Meischner, Shi, Wala or Shiojiri-Oryza lines found earlier by d129/d130/d134 changed, and I filed nothing, so no overlap arises.

## Held out (all six leads; resume when a WFO species page, snapshot 2022-06 or later, surfaces)
1. Picea abies and Fagus sylvatica, Meischner et al. 2025, Physiologia Plantarum 177(4): e70432 (10.1111/ppl.70432). Species must be checked separately. Audit 221's rule applies: do not call emission "herbivore-induced" unless the paper does; shoot JA treatment, total terpenoid emissions p = 0.010 and p = 0.020, no change in indirectly treated branches.
2. Kobresia humilis, Shi et al. 2022, Plants 11(22): 3102 (10.3390/plants11223102). Carry the non-significant tillers, height, Pn and pigments, and Table 4 flower number p = 0.021. POWO not read.
3. Solanum tuberosum, Ninkovic et al. 2013, PLoS ONE 8(7): e69431. Cultivar Sava named in conditions; carry DMNT not significant and overall blend P = 0.04.
4. Alyssum montanum KNO3, Wala et al. 2021, PLOS ONE 16: e0244737. WFO may place only subspecies pages in the surfaced results; the species page itself still has to surface. Carry the water-control zero germination and the 10-50 mM window.
5. Oryza sativa, Shiojiri et al. 2021, Front Plant Sci 12: 692924. Cultivar Koshihikari; carry grain weight and leaf number not significant.

## Desk disposition
0 records filed, so no audit is due. check.py shows 0 problems for desk-d136 (no file written).
