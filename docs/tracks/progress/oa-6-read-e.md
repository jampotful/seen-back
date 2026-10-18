# oa-6 reading pass, reader E (18 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md`. Entries 40, 45, 58, 59, 62 and 72 of `docs/tracks/batches/oa-6.json`, read from the texts of the oa job (run 3 on `run/oa/read-e`, byte-identical to run 1 by checksum). Branch `agent/oa-read-e`. Every quote passed `tools/views/quotecheck.py` and `tools/views/oa_lint.py`; `tools/senses/check.py` passes.

## Papers read in full
| entry | paper | copy | records | m | g | partial |
|---|---|---|---|---|---|---|
| 40 | Boström et al. 2016, Ultra-rapid vision in birds | Europe PMC XML, published | 7 | 6 | 1 | 1 |
| 58 | Qian et al. 2026, Praying mantises possess multiple spectral photoreceptor classes | Europe PMC XML, published | 13 | 11 | 2 | 2 |
| 62 | Healy et al. 2013, Metabolic rate and body size ... temporal information | Europe PMC XML, published | 35 | 0 | 35 | 35 |
| 72 | Gracheva et al. 2010, Molecular basis of infrared detection by snakes | PMC page, author manuscript (said in each note and in the sources line) | 31 | 25 | 6 | 6 |

## Abstract pages only (no sources line written)
| entry | paper | what the oa job returned | records |
|---|---|---|---|
| 45 | Stavenga et al. 2001, Retinal regionalization and heterogeneity of butterfly eyes | University of Groningen repository page with the abstract; the full-text PDF it links was not fetched | 2 (g, partial, `access: abstract`) |
| 59 | Sontag 1971, Spectral sensitivity studies on the visual system of the praying mantis | PubMed Central page with the abstract; the scanned full text was not fetched (Europe PMC XML short, rupress 403) | 4 (m, partial, `access: abstract`) |

These two still need their full texts read; the owner's page should keep asking for them.

Total: 92 records (m 46, g 46), 50 partial, 6 from abstracts. No paper without a measurement.

## Notes
- Entry 62: the 34 rows of Table 1 are a compilation, so all are partial and `g`, each naming its data source from the table footnote; method (ERG or behaviour) and the compilers' optimum or suboptimum rating come from the superscripts. Canon-3 already holds the same table from another copy.
- Entry 72: the rat snake is mapped to Elaphe obsoleta lindheimeri from the paper's GenBank footnote (the Fig. 1 legend spells it Elaphe obsolete lindheimerii); its records use `sense_thermal`, the pit-bearing species `sense_infrared`.
- Entry 40: the abstract rounds the species means differently from the Results (129, 127, 137 Hz against 130.3, 128.1, 138.2 Hz); the Results values are logged. Values cited by number only (budgerigar, chicken) were not logged, since the text has no reference list.
