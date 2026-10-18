# oa-10 reading pass, reader E (18 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md`, with the control room's corrected grade rule. Entries 1, 2, 4, 5, 11, 13, 15, 16, 21, 23, 31, 42, 49 and 51 of `docs/tracks/batches/oa-10.json`, read from the texts of the oa job (run 3 on `run/oa/read-e`, byte-identical to run 1 by checksum). Branch `agent/oa-read-e`. Every quote passed `tools/views/quotecheck.py`, `tools/views/oa_lint.py` reports no fault on the branch's lines, and `tools/senses/check.py` passes.

## Papers read in full
| entry | paper | copy | records | m | g | i | partial |
|---|---|---|---|---|---|---|---|
| 1 | Fornazari et al. 2016, the eye of the aoudad | Europe PMC XML | 25 | 8 | 17 | 0 | 20 |
| 2 | Seiko et al. 2020, opsin genes in sea snakes | Europe PMC XML | 8 | 5 | 0 | 3 | 0 |
| 4 | Tashiro et al. 2022, retinas of Bothrops jararaca and Crotalus durissus | Europe PMC XML | 40 | 28 | 8 | 4 | 22 |
| 5 | Rigosi et al. 2026, photoreceptor acuity in solitary bees | Europe PMC XML | 43 | 43 | 0 | 0 | 0 |
| 11 | Kott et al. 2010, light perception in two mole-rats | Europe PMC XML | 8 | 6 | 0 | 2 | 0 |
| 13 | Streinzer et al. 2016, dim-light foraging in stingless bees | Europe PMC XML | 8 | 8 | 0 | 0 | 0 |
| 15 | Smirnakou et al. 2017, oak seedlings under LED spectra | Europe PMC XML | 3 | 3 | 0 | 0 | 0 |
| 16 | Dudley and File 2007, kin recognition in Cakile edentula | Europe PMC XML | 2 | 2 | 0 | 0 | 0 |
| 21 | Molina-Contreras et al. 2019, shade responses in Cardamine and Arabidopsis | UAB repository PDF, accepted manuscript (in each note and the sources line) | 10 | 10 | 0 | 0 | 0 |
| 31 | Ishida et al. 2009, brood-site pollination in Macaranga | PMC page, published | 0 | | | | |
| 42 | Martin 2014, visual fields of birds (review) | PMC page, published | 10 | 1 | 9 | 0 | 10 |
| 49 | Fox et al. 2007, phototaxis in Collembola | Europe PMC XML | 20 | 18 | 2 | 0 | 2 |

## Abstract pages only (no sources line written)
| entry | paper | what the oa job returned | records |
|---|---|---|---|
| 23 | Garrett, The pollination biology of papaw (thesis, CQUniversity) | Figshare landing page with the abstract; the 22.6 MB thesis PDF was not fetched | 2 (g, partial, `access: abstract`) |
| 51 | Simões et al. 2020, Spectral diversification ... in snakes (Current Biology) | University of Bristol repository page with the abstract; the accepted manuscript PDF it links was not fetched | 2 (i, partial, `access: abstract`) |

These two still need their full texts read; the owner's page should keep asking for them.

Total: 181 records (m 132, g 38, i 11), 58 partial, 4 from abstracts. Paper with no BRIEF measurement: entry 31 (pollinator identity, rewards and behaviour only; sources line with `"records": 0`).

## Notes
- `g` records are group values (Aves, ducks and shorebirds, Viperidae, marine Elapidae, Philodryas, nocturnal dipsadids, Crotalinae, Collembola), a range pooled over two taxa (Aipysurus laevis with Philodryas), or cited animals the papers name only by a lowercase or plural common name (aoudad paper: cattle, sheep, goats, cow, horse, foal, chinchilla, rabbit, giraffes and others; Martin: New Caledonian crows, mallards, woodcocks), since an `m` here needs a taxon written as one species. Guinea pig and Canada goose are `m`.
- `i` records: λmax predicted from sequences (sea snake LWS, viper LWS and SWS1 after Bittencourt et al. 2019, Hydrophis SWS1 alleles), receptor classes predicted from intact opsin genes (Emydocephalus ijimae, Elapidae), and the mole-rat S-opsin peak inferred from behaviour; each names the prediction in `method`.
- Entry 1 logs pupil shape under `pupil_shape`, marked "new trait" (the key the evidence logs use; BRIEF's list has none), because the batch asked for it.
- Entry 4: acuity is given twice for each species and age, from the hexagonal and the square ganglion-cell array.
- Entry 5: honeybee acceptance angles and the drone rhabdom diameter in Table 1 come from the authors' earlier papers, cited by number only, so they were not logged; the honeybee interommatidial angles and forager rhabdom diameter measured here were.
- Entry 21 is an accepted manuscript whose text carries line numbers; the few that fall inside a quote are kept as the file holds them, and each such note says so.
- Metadata gaps: entry 15 (pages) and entry 21 (volume) could not be filled, because the text read shows no article number or volume on its first page; the sources-r1 journal string is kept. For entry 23 the author, item type and year were taken from the Figshare page (the year is the posting date, 2017).
- Values that papers cite by reference number only, with no reference list in the text (sea snake, mole-rat and bee papers), were not logged.
