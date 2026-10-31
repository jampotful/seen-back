# desk-d241

Sonnet 5.5 desk unit. Nine records in docs/views/evidence/desk-d241.jsonl (check.py: 0 problems). About 26 WebSearches. Candidate DOIs and species were grepped against main, the d230 to d240 evidence files and the unmerged unit branches before opening; a DOI hit in any docs/ file other than desk-queue was treated as already covered.

## Records

1. Alouatta caraya, peak_ganglion_cell_density_mm2 (Muniz et al. 2014, PLoS ONE 9(12): e115291, 10.1371/journal.pone.0115291): mean ganglion cell density at 0.5 mm from the fovea, 40,673 to 44,963 cells/mm2 by direction. Captive-bred adult males from the CENP colony; six retinas from five animals; no shrinkage correction; abstract range (45,200) differs slightly from Results means (stated in conditions). Earlier held in d239 for PLOS rate limits; this was a retry.
2 and 3. Sylvia atricapilla, sense_magnetic (Schwarze et al. 2016, Sci Rep 6: 33805, 10.1038/srep33805): oriented at 5 degrees inclination as well as at 67 degrees (abstract), and randomly oriented in the horizontal field (null, abstract). Wild-caught blackcaps, N per condition and Rayleigh results in conditions, including the bimodal spring-2014 0 degree NMF group.
4. Sylvia borin, sense_magnetic (Bojarinova et al. 2020, Sci Rep 10: 3473, 10.1038/s41598-020-60383-x): not disoriented with the oscillating-field device on (n = 14, r = 0.49, P = 0.03). The device-off control group was itself only P = 0.056, and the 5 nT stationary-coil group was disoriented; both are in conditions.
5. Erithacus rubecula, sense_magnetic (Alert et al. 2015, Sci Rep 5: 14323, 10.1038/srep14323): indoor control robins without celestial cues remained unable to orient (null). The paper prints P = 0.004 (Results) and P = 0.017 (Fig. 2 caption) for the experimental group; noted in conditions.
6 to 9. Rhinolophus affinis, Taphozous melanopogon, Cynopterus sphinx, Rousettus leschenaultii, absolute_sensitivity (Liu et al. 2015, Sci Rep 5: 11531, 10.1038/srep11531): f-VEP absolute visual thresholds -1.90, -3.71, -6.30, -6.37 log cd/m2 s. One Results sentence, four records. Wild-caught bats, n 2 to 4 per species, display luminance not stated as measured.

Names: Alouatta caraya and Sylvia atricapilla and Erithacus rubecula in gbif-names.tsv (ACCEPTED); Sylvia borin as used on main; the four bats checked on mammaldiversity.org taxon pages.

## Held leads and why

- Wood mouse magnetoreception (srep09917, wild-caught Apodemus sylvaticus, radiofrequency sweep changed nest bearing from north-south to east-west): n per condition is only in Table 1, which the page tool does not return; the sweep-condition Rayleigh p = 0.066 and Larmor null are known. Held for n.
- Goutte 2017 Brachycephalus hearing (s41598-017-12145-5): already on main (herps.jsonl, pooled species; audit 259).
- Archerfish face discrimination (srep27523): page failed to load twice (client error).
- Exorista japonica (pone.0160441): PLOS rate limit again.
- Springer-hosted BMC lungfish MSP (1472-6785-8-21): redirect to springer, refused.
- Zoo primate colour vision (Animals 14(13): 1979): proof of concept, 8 animals, no control condition, hybrid spider monkey; held.
- Alouatta acuity: the paper reports no cycles-per-degree value.
- Already covered, found by search: Strongylocentrotus intermedius phototaxis, Nilaparvata magnetic, fish hearing PLoS papers (d143, d160, d184, d216), shark and ray electroreception, Gekko subpalmatus, Amphiprion akindynos, Hippoglossus, Anguilla marmorata, Euxesta and Chaetopsis.

## Owner questions

1. Is a categorical null from an abstract sentence ("remained unable to orient", "completely randomly oriented") acceptable as a sense_magnetic value, or should only sentences carrying a statistic be filed? The statistics are in conditions in each case.
2. Records 6 to 9 share one sentence across four species; is one record per species with the same quote the wanted form?
3. absolute_sensitivity on main holds cd/m2 values; these are log cd/m2 s from f-VEP. Same key, or a separate one?
