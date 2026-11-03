# desk-d531 progress

Angle: new open papers with species-level echolocation parameters (sense_echolocation, evidence_kind physiological_response, one record per species and parameter). 10 records (log docs/views/evidence/desk-d531.jsonl). check.py: 0 problems for this file (plain and --require-evidence-kind). About 31 WebSearches.

## Filed
- Thong VD, Limbert H, Limbert D 2022, Diversity 14(7): 534, "First Records of Bats (Mammalia: Chiroptera) from the World's Largest Cave in Vietnam" (10.3390/d14070534), Table 2, whole species rows (n = signals, mean ± SD and range): Aselliscus stoliczkanus (CF, tFM, PD; n 31, second harmonic), Hipposideros scutinares (CF, tFM, PD; n 32, second harmonic), Mops plicatus (iFM, tFM, BW, PD; n 47, first harmonic). Free-flying bats inside Son Doong Cave before the mist nets. MDD pages: mammaldiversity.org taxon 1004561, 1004633, 1005158 (all living, valid). None of the three species is on main; the DOI is not on main.

## Weak spots
- Table 2 prints no units and does not spell out iFM, CF, tFM, BW, PD in the header; kHz and ms are inferred from the Results text and from BW = iFM - tFM (Mops plicatus). Each record says so.
- Table 2 caption names "Ha Long Bay and Ben Tre province" (printed caption error); each record says so.
- n is the number of signals in 5000 ms selected recordings, not bats (1 to 2 bats captured per species); pooled signals.
- Table cells read through the WebFetch reader cell by cell; Crossref not read. Licence: page prints the CC BY link (metadata says 3.0, page text 4.0).
- Mops plicatus nomenclature (Tadarida/Chaerephon) is "still under discussion" in the paper; MDD uses Mops plicatus.
- The unfiltered search that reaches the page: "Son Doong Cave bats Thong Limbert 2022 First Records of Bats (Mammalia: Chiroptera) from the World's Largest Cave in Vietnam".

## Not filed and why
- Cat Ba review (Diversity 13(8): 376): species-account ranges in text only, review, R. affinis on main.
- Dai 2023 Front Ecol Evol 11: 1108514 (Table 3, five Rhinolophus): all on main or excluded.
- Bittencourt 2025 fmars.2025.1641888 (Pontoporia): already on main (d519).
- Urban Science 10(8): 474 (Tacna bats): Table 1 is an image, rows not readable. Animals 13(16): 2560 and Forests 8(9): 317: no call-parameter tables. Frontiers fevo 2018.00227, 2021.661216, 2022.877579, 2022.907751, 2020.00265, ffgc 2023.1082427, fetho 2026.1891633, fcosc 2026.1896568, frsen 2022.941838, fmars 2019.00066: no per-species mean ± SD rows or no licence sentence. PeerJ 10551 (one species, no table). Pensoft pages were under maintenance throughout.
