# desk-d164 progress (vision traits and bird/mammal hearing)

Records filed: 11, in docs/views/evidence/desk-d164.jsonl (check.py: 0 problems). Four open papers.

- Ruser et al. 2014, PLoS ONE 9(3): e90824 (CC BY, Crossref): Halichoerus grypus in-air ABR, 3 sense_hearing records (Carnivora had none).
- Rößler, May, Dähne 2024, Sci Rep 14: 30592 (CC BY 4.0 per Crossref; licence paragraph not visible in the page text read): Spheniscus humboldti behavioural audiogram, 1 record.
- Egri, Jásdi, Kriska 2025, Sci Rep 15: 29465 (CC BY 4.0 on the page): Electrogena lateralis ERG peaks 536, 366, 353 nm and dorsal-eye flicker fusion 148.7 Hz, 4 records. Crossref could not be fetched for this DOI (client error on every try); authors, volume and article number are from the Nature page citation.
- Allan 2026, PLoS One 21(4): e0346423 (CC0 per page and Crossref): Euxesta eluta ERG peaks and colour-card behaviour, 3 records.

Held out
- Chaetopsis massyla (same Allan paper): name not confirmed on a GBIF/CoL page (GBIF page would not load; BugGuide and PestInfo are not authorities).
- Electrogena female (104.5 Hz) and male ventral (104.1 Hz) flicker fusion, larval template-fit peaks (375, 544 nm): sentences could not be retrieved whole, or are template fits of hypothetical receptors.
- Stoessel et al. 2023 Sci Rep chimpanzee middle-ear transfer function: no chimpanzee threshold values; licence not named on page.
- Lohr et al. 2013 woodpecker ABR (JASA): PMC copy has no licence statement.
- Underwater grey seal audiogram, Biology Open 14(8): bio062059: fetch blocked (permission not answered).
- Larus audouinii retina (Birds 6(1):7, CC BY 3.0): histology only, no BRIEF trait with a value.
- PMC pages (reCAPTCHA) not worked around; Crossref reachable only through WebFetch.
- Not repeated: Heliconius (acuity), Rhabdomys, Tiliqua, Melopsittacus, Bufo gargarizans are already in main.

Quote status: each quote reassembled from consecutive WebFetch segments and seen on two fetches, except the Electrogena abstract sentences (segments plus an earlier fetch) and the Euxesta behaviour sentence (two fetches). No full text was available to quotecheck.py.

## Desk disposition after audit 249
Audit 249 judged 11 records: 4 errors (lines 5 to 8, all Egri 2025 mayfly, fixable). The preparation is intact adults, not excised eyes. Lines 5 to 7 are mean Govardovskii template peaks for hypothetical photoreceptors, not peaks read from the ERG curve, and the method says so. Line 8 now carries the 1.2 × 10^15 photons cm-2 s-1 UV flicker intensity. Uncounted fixes applied on lines 1 to 4 (tone-pip distortion, n = 3 at 0.25 kHz, absent 125 Hz), 9 and 10 (preparation, stimulus range, 355 nm caption discrepancy), 11 (lamps, temperature, N) and the journal issue. Owner question raised: whether Govardovskii-template receptor peaks from ERG belong under lambda_max_nm. Merged 11 records.
