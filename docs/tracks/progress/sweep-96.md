# sweep-96 (15 October 2026)

Round 3 genus sweep over 40 genera (17 insects, 8 vertebrates, 15 plants and kelp), in the batch's order. Each genus had two searches (scientific name, then common name or family) and every genus has a search record in `docs/views/searched/sweep-96.jsonl` with `chased` filled.

Logged (`docs/views/evidence/sweep-96.jsonl`, 8 records):
- Egregia menziesii, sense_light_nonvisual, m, from the full text of a 2026 San Jose State thesis.
- Sideroxylon obtusifolium, sense_light_nonvisual, m, full text (a congener of S. lanuginosum). The paper prints no DOI, so the URL stands in.
- Epacris tasmanica, sense_chemical (smoke), m, partial (abstract only; congener of E. impressa).
- Malaclemys terrapin, receptor_classes (4) and spectral_range_nm (modelled 355-640), m, partial (abstract of an open-access dissertation the fetch tool could not read in full).
- Agelaius phoeniceus, binocular_deg, fov_h_deg and acuity_cpd, m, full text. Found while chasing Dolichonyx; it is a different genus, so nothing carries.

Wanted (`docs/views/wanted/sweep-96.jsonl`): Baskin and Baskin 1992 (Polemonium reptans germination), Gilmour et al 2000 (Epacris tasmanica, full text), Dominy 2015 (terrapin dissertation, open access).

Nothing found for 28 of the genera. Limits met: the fetch tool refused doi.org, Europe PMC and many PMC pages, so citing lists were not available; `chased` says what was opened in each case. The Feller et al 2021 supplementary Table S3 (genus-level insect acuity curation) was not in the copy opened.
