# desk-d190 progress

Animal sensory traits other than colour choice. 7 evidence records from 3 papers in docs/views/evidence/desk-d190.jsonl (sense_magnetic 3, sense_hearing 2, sense_vibration 2). No search or wanted files. 28 WebSearches used of 40.

## Records
- Bianco et al. 2022, J Comp Physiol A 208(1): 135-144, DOI 10.1007/s00359-021-01536-9 (Crossref CC BY 4.0; Springer page open access): Acrocephalus scirpaceus (accepted via the GBIF backbone entry for A. s. fuscus; other rows on main use it). Three sense_magnetic records: the abstract result (body alignment before sunset, shifting to NE-SW afterwards); the control group's NE-SW alignment through 3 h of dark; and the null at individual level (n = 16, all tests p > 0.05, substantial scatter). Confound kept in conditions: birds sat in the natural geomagnetic field and the Methods passages read describe no coil or shielding manipulation, so the alignment is not shown to depend on the field; the lamp schedule, cage and tracking method are given. Main holds other A. scirpaceus magnetic rows (s41598-018-30477-8, jeb.243337) but not this paper.
- Capshaw et al. 2024, Proc R Soc B 291(2034): 20241560, DOI 10.1098/rspb.2024.1560 (Crossref CC BY 4.0 vor): Eptesicus fuscus (valid in MDD taxon 1005519; MDD notes new species limits proposed by Monico and Soto-Centeno 2024 and a possible species complex). Two records, both read from the PubMed abstract only (access abstract, partial true): no hearing deficits up to 12.5 years (comparable thresholds, similar ABR and DPOAE amplitudes), and no histological cochlear ageing. Frequency range, n per age group and anaesthesia were not seen and are said so in conditions. Main holds no hearing row for this species. The preprint abstract was not used.
- Miller et al. 2026, Proc R Soc B 293(2073): 20260915, DOI 10.1098/rspb.2026.0915 (Crossref CC BY 4.0 vor; the Oxford ORA copy states CC BY 4.0): Grammostola pulchra (ACCEPTED in the World Spider Catalog). Two sense_vibration records from Results: distal leg segments' FRF magnitude close to 1 across 20-200 Hz; and noise below 20 Hz, no obvious resonances and low amplitude above 200 Hz. Confounds kept: one specimen only, vertical axis, single broadband square-wave pulse, mechanical transfer not a neural threshold. Main already holds one row from this paper (abstract claim, spider.jsonl in audit/corrected); these are different Results findings, not a repeat of it.

All quotes were rebuilt from fragments under about 100 characters (the fetch tool will not return whole sentences) and confirmed on at least two fetches; Miller line 2 and the Bianco night sentence were each seen on two fetches.

## Not filed
- Miller sentence "However, for the cephalothorax, abdomen and proximal leg segments, between 20 and 80 Hz ..." (49 words; a cut would leave the qualifier dangling).
- Tokay gecko vibration pathway (Han and Carr 2024, Curr Biol 34(21): 4908, DOI 10.1016/j.cub.2024.09.016): Crossref shows only the Elsevier open-access user licence, no CC licence.
- Qian et al. 2025 praying mantis photoreceptor classes (J Comp Physiol A 212(1), DOI 10.1007/s00359-025-01776-z): Crossref CC BY-NC-ND.
- Already on main: Moffitt 2023 armadillo ABR (desk-d166), Houser 2022 odontocete audiograms (desk-d171), Wang 2022 red-eared slider hearing (desk-d154), Huttner 2023 dolphin electroreception (desk-d143).
- Frontiers editorial fevo.2025.1732523 (not a primary paper).

## Refused or blocked (not retried)
Europe PMC REST search (permission request not answered); api.crossref.org through curl (proxy refused; WebFetch worked); royalsocietypublishing.org and PMC not tried after earlier units' refusals. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page opened.

## Not reached
Jumping spider, dragonfly, moth hearing, ray electroreception, lateral line, frogs: searches returned old, closed or already-filed papers.

## Desk disposition after audit 274

Audit 274: 2 of 7 records in error (28.6%; lines 1 and 7), none unfixable. Pooled audits 172 to 274: 224 of 550 (40.7%). All seven merged with the auditor's replacement text and the uncounted wording fixes.

- Bianco line 1 now carries the delayed lamp-off result (the shift followed the light schedule, 'sunset' is lamp-off). Miller line 7: the sub-20 Hz noise is stated as a measurement limit.

Owner questions: whether spontaneous alignment in an unmanipulated field stays under sense_magnetic; correct the author initials on main's spider.jsonl:194 Miller 2026 row at the next corrected-file pass; whether a full-text read of Capshaw 2024 is wanted (lines 4 and 5 rest on the abstract).
