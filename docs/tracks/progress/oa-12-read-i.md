# oa-12 reading pass, reader i (18 October 2026)

Entries, in launch order: 16, 22, 23, 24, 37, 39, 55, 56, 59, 68. All ten were read. Texts came from the control room's decrypted copies of run oa12-r1 (`/tmp/oa-shared/oa-12/`), and each one matched the checksum in that run's `lookup.jsonl`. No run branch was pushed, on the control room's instruction. Every record passed `tools/views/oa_lint.py` (with `--text`), `tools/views/quotecheck.py` and `tools/senses/check.py` before its commit.

## Totals

- Papers read: 10 (9 full texts, 1 abstract only).
- Records logged: 137 in `docs/views/evidence/oa-12.jsonl`. Grades: m 116, g 21, i 0. Partial: 96 (both reviews in full, cited values, the abstract-only paper and one reanalysed data set).
- Sources lines: 9 in `docs/views/sources/oa-12.jsonl`. Entry 16 has none because its copy is only an abstract.
- Papers with no measurement of a BRIEF trait: none. Entries 55 and 59 hold no light measurement on their own species: 55 gives a heterologous Arabidopsis result (logged as g), and 59 gives only vernalization expression from a reanalysed data set (logged as partial).
- Could not read: nothing. Entry 16's free copy is a PubMed Central landing page carrying only the abstract, because the scanned full text was not in the fetch.

## By paper

| entry | paper | copy | records | note |
|---|---|---|---|---|
| 16 | Kraft 1988, J Physiol 404: 199-213 | abstract only (PMC landing page) | 4 | logged as `access: abstract`, `partial: true`; no sources line |
| 22 | Fleishman 2024, Front Amphib Reptile Sci 2: 1426675 | published PDF | 36 | review, so every record is partial; Figs. 6 and 7 (λmax by species) are images |
| 23 | Tyrrell et al. 2018, Front Neurosci 12: 16 | Europe PMC XML | 15 | binocular widths are pooled for the two species (g); eye movement is given per species |
| 24 | Llorens et al. 2023, Plants 12(18): 3219 | Europe PMC XML | 5 | flowers closed at night (both species) and cited insect responses to volatiles (partial). Three β-ionone records were left out because that sentence starts with 'β' and fails quote-shape |
| 37 | Tao et al. 2026, Plant Commun 7(6): 101848 | Europe PMC XML | 35 | review, so every record is partial; covers germination, de-etiolation, flowering, shade avoidance, leaf senescence and temperature sensing by crop species |
| 39 | Troscianko et al. 2012, Nat Commun 3: 1110 | published PDF | 18 | Table 1 gives binocular overlap and eye movement for six Corvus species, and cites the American crow. No chough value |
| 55 | Zhou et al. 2026, Plant Cell Environ 49(9): 6621-6634 | PMC HTML (published version) | 2 | no light measurement on E. sibiricus itself; the heterologous Arabidopsis result is logged as g and a cited Arabidopsis transcriptome as partial |
| 56 | Nolet and Wolyn 2020, Can J Plant Sci 100(4): 380-391 | accepted manuscript PDF | 4 | no light treatment was tested; logged the fall-cue statement, the inferred soil-temperature sensing (g) and two cited studies |
| 59 | Hu et al. 2018, PLOS ONE 13(9): e0204137 | Europe PMC XML | 2 | no light treatment in radish; vernalization expression (reanalysed, partial) and one Arabidopsis background statement |
| 68 | Ma et al. 2024, Front Plant Sci 15: 1488649 | Europe PMC XML | 16 | twelve light-quality responses of S. baicalensis and four cited studies |

## For the auditor

- Entry 22: grades follow the taxon. Statements about lizards, chameleons or Anolis as a whole are graded m. Statements about nocturnal or diurnal geckos (a part of Gekkota), the six Ctenophorus species and the three Anolis species in the flicker study are graded g.
- Entry 23: the four eye-movement species from the Discussion (Tufted Titmouse, Song Sparrow, Carolina Chickadee, American Goldfinch) are named only by common name in the paper. Their scientific names are mine, and each note says so.
- Entry 37: species named only by common name (maize, rice, sorghum, pea, cucumber, wheat, barley, soybean, tomato, lettuce, potato) carry scientific names, and each note says so.
- Entry 39: Table 1 rows are quoted from the layout part of the text, with whitespace normalized.
