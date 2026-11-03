# desk-d530 progress

evidence_intake: evidence-kind-v2
intake_base: b347f2611a8c252c8d8697b0dff3cabc2ddd936f

Angle: new open papers with species-level echolocation parameters (sense_echolocation, evidence_kind physiological_response, one record per parameter). The superseded reptile/fish paragraph was not followed. 10 records in docs/views/evidence/desk-d530.jsonl. About 39 WebSearches.

## Filed
- Redgwell, Szewczak, Jones and Parsons 2009, Algorithms 2(3): 907-924 (10.3390/a2030907), Table 3 column Emax (frequency of maximum energy by FFT of the whole call), mean +- s.e.m., one record per species: Cnephaeus serotinus (printed Eptesicus serotinus; MDD name used) 33.88 kHz, Myotis bechsteinii 71.52, M. brandtii 55.16, M. daubentonii 55.57, M. mystacinus 56.59, M. nattereri 66.21, Nyctalus leisleri 31.02, N. noctula 24.30, Pipistrellus pygmaeus 52.79, Rhinolophus ferrumequinum 82.22. n comes from Table 5 "Calls" (24 to 99) plus the Methods sentence "Only one call was used from each individual bat recorded". Recordings are reused from Parsons and Jones 2000 (J Exp Biol, not filed); recording conditions are not stated in this paper. CC BY (3.0) sentence on the MDPI page; Crossref blocked. MDD pages reached from my own filtered searches (taxon ids 1005531, 1005375, 1005380, 1005395, 1005444, 1005445, 1005605, 1005607, 1005633, 1004684). Unfiltered search that reaches the full text: 'Classification of Echolocation Calls from 14 Species of Bat by Support Vector Machines and Ensembles of Neural Networks'.
- Not filed from the same paper: Barbastella barbastellus (on main), Pipistrellus pipistrellus (on main, other measure), Rhinolophus hipposideros (on main), Plecotus auritus (brief: pending audit; paper itself warns its P. auritus values are not indicative); duration, Fstart, Fend, Fcenter columns (same rows).

## Not filed and why
- Salsamendi 2012 Front Zool 9: 30: R. mehelyi 106.8 +- 1.5 kHz (n = 16), R. euryale 105.1 +- 1.2 (n = 24); both species on main; R. blasii not in the paper.
- Aldasoro 2024 Animals 14(22): 3303 (on brief list; no RF values in page text). Erbe 2026 Conservation 6(3): 99 fur seal audiogram is already on main (desk-d193).
- Pooled-station fixed recorders (no individuals): Burmeister's porpoise fmars.2025.1582414 (peak 132.12 +- 4.04 kHz, n = 5,451 clicks, F-POD), fmars.2018.00220 (C-POD click trains; no licence text).
- No per-species call values or no licence text in page reader output: Sci Rep s41598-017-00959-2 and s41598-017-04608-6, Taub 2023 Commun Biol s42003-023-05563-x, Smotherman 2022 fevo.2022.969350 (Tadarida brasiliensis on main), fevo 2022.934876, 2022.1031548, 2022.950951, 2019.00441, 2019.00373, 2018.00227, fphys.2013.00214, fmars.2021.664292, Sustainability 14: 13186; BMC Ecol Evol 14: 60 and Basic Appl Zool s41936-018-0041-7 (pages would not open); BDJ 165516 (site under maintenance).

## Weak spots
- Table 3 rows came through the WebFetch reader (two lines per row: values, then CVs; both lines are in each quote). Auditor should check digits on the page.
- The paper does not say how the bats were recorded; n = calls = bats is inferred from Table 5 plus the one-call-per-bat sentence.
