# oa-1 reading pass, reader C (18 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md`. Entries 19, 30, 32, 39, 59, 60, 66, 67, 68 and 71 of `oa-1`, read in that order from the free copies the `oa` job fetched again for this reader (branch `run/oa/read-c`, run 4, results in `runs/oa/4-oa-1` on `ci`). All ten texts arrived and decrypted with matching checksums; none failed. Reading branch: `agent/oa-read-c`.

## Counts

577 records in `docs/views/evidence/oa-1.jsonl`: grade `m` 332, `g` 245, `i` 0; `partial: true` 224. One line per paper in `docs/views/sources/oa-1.jsonl`.

| Entry | Paper | Copy | Records | m | g | partial |
|---|---|---|---|---|---|---|
| 19 | Futahashi et al. 2015, dragonfly opsins (PNAS) | PubMed Central, published version | 25 | 18 | 7 | 6 |
| 30 | Caves et al. 2024, bird acuity data (Dryad) | Dryad landing page | 0 | | | |
| 32 | Cantlay et al. 2025, gull visual fields (Ibis) | publisher's PDF, Birmingham repository | 12 | 6 | 6 | 1 |
| 39 | Rockwell et al. 2014, algal phytochromes (PNAS) | PubMed Central, published version | 16 | 11 | 5 | 4 |
| 59 | Simões et al. 2016, snake pigments and ocular filters (MBE) | accepted manuscript with supplementary tables, City repository | 350 | 165 | 185 | 96 |
| 60 | Para 2026, butterfly flicker fusion (Carleton MSc thesis) | published thesis PDF | 87 | 75 | 12 | 83 |
| 66 | Ödeen et al. 2011, passerine UV vision (BMC Evol Biol) | Europe PMC, published version | 13 | 3 | 10 | 10 |
| 67 | Schott et al. 2024, frog opsins (MBE) | Europe PMC, published version | 25 | 7 | 18 | 16 |
| 68 | Pecsics and Csörgő 2023, diving-bird visual fields (Ornis Hungarica) | publisher's PDF | 40 | 39 | 1 | 4 |
| 71 | Wada et al. 2012, iguana parietal eye (PLoS ONE) | Europe PMC, published version | 9 | 8 | 1 | 4 |

Paper with no measurement of a BRIEF trait in the copy: entry 30. The copy is the Dryad landing page (abstract, README, methods); `Bird_Acuity_Data.csv` itself was not fetched. `oa-1` already holds the article's Tables S1 and S2 (10.1242/jeb.246063).

## What the copies lacked

- 19: the SI appendix and Dataset S1. Per-species opsin counts come from the text only (Fig. 6B is an image).
- 32: Supporting Tables S1 to S3. The main text gives pooled values for the three gulls (logged `g`) and the vertical extent of the binocular field per species.
- 39: the supporting table of peak wavelengths. NpyrPHY1, PcolPHY1 and DtenPHY1 have only a group range in the text plus each one's photocycle colours from the Fig. 2 caption.
- 60: each species' mean CFF appears only in a boxplot (Fig. 2.4), which was not read. The thesis's own values are logged as colour-class ranges and one example recording; Appendix A's compiled insect CFFs and light levels are logged as partial.
- 66: Additional file 1, the per-species SWS1 list. Only group statements and the two Fig. 1 example birds are logged.
- 67: supplementary table S2, file S1 and Fig. 5. The paper's own MSP values are logged as group ranges, except the two species the text names (Callimedusa tomopterna 411 nm, Dendrobates auratus 441 nm).
- 71: the copy has no reference list, so cited studies are named by their numbers.

## Conventions

- Values predicted from opsin sequence or read from a gene's identity are `g` at most and say so in `method` and `note` (entry 59 Tables S3 to S5, entries 66, 67 and 71). They are the paper's own predictions, so they are not `partial`.
- Values that a paper cites for one named species are `m` with `partial: true`, naming the original in `note`, as in the desk's repaired logs. Group statements are `g`.
- Entry 68's Table 1 values are model estimates from skulls with schematic eyeballs. They are graded `m` because each is for one named species in this paper, and `method` and `note` say they are not ophthalmoscopic measurements.
- In PDFs, table rows are quoted from the `=== LAYOUT ===` part, where each row is one line. The plain part scrambles those tables, so 321 table-row quotes (entry 59 Tables S2, S3, S4, S5 and S22; entry 68 Table 1, binocular row) exist only in the layout part. Every quote passes `quotecheck.py` as verbatim (577 of 577), and `oa_lint.py --since-main HEAD` reports no fault.
- Trait keys beyond BRIEF's list, each with "new trait" in `note`, reuse keys from earlier rounds: `opsin_gene_count`, `whole_eye_spectral_peak_nm`, `binocular_vertical_extent_deg`, `monocular_sector_width_deg`, `blind_area_deg`, `ocular_media_lambda_t50_nm`, `ocular_media_uva_transmittance_pct`, `optic_axes_divergence_deg`, `pupil_shape`.

## Left out on purpose

- Entry 59: the measured Anolis carolinensis SWS1 value, which the text prints run into its footnote number ("UVS (3591)"), and table cells that give only a shift or a question mark ("-6|-20", "-6|?", "419|?", "-4|?", "?*"). Ancestral reconstructions are also left out.
- Entry 60: values given only by common name with no scientific name in the thesis (peregrine falcon 129 Hz, humans 60 Hz). Entry 59's guinea pig SWS1 value is left out for the same reason.
- Entry 66: the Rifleman's Leu93 residue, whose effect on tuning is unknown.
- Entry 68: the general sentence giving 20 to 30 degrees of binocular width in birds, because a line-end dash in the text defeats `quotecheck.py`.

## Setup note

The key and texts were kept in `/tmp/oa/c` (priv.pem, txt/), inside `/tmp/oa`, so that readers sharing a machine do not overwrite one another's key. Nothing from `/tmp/oa` was committed.
