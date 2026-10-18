# OA reading pass, batch oa-12, reader k (18 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md`. Entries 6, 10, 12, 26, 29, 34, 35, 41, 48, 60 and 67, read in that order. Branch `agent/oa-read-k`.

Texts: the control room's decrypted oa-12 texts at `/tmp/oa-shared/oa-12/` (run oa12-r1). Every one of the eleven matched its `text_sha256` in that run's `lookup.jsonl`. No run branch was pushed: the classifier refused replacing `ci/oa/pub.pem`, and the control room then pointed readers at the shared texts. Every record passed `oa_lint.py --text`, `quotecheck.py` and `check.py` against its own text before it was appended.

## Counts

- Papers read: 11. Full text 9; abstract or landing page only 2 (entries 12 and 35).
- Records logged: 58. Grades: m 57, g 1, i 0. Partial: 15 (12 abstract-only values from entries 12 and 35, 2 cited values in entry 34, 1 cited value in entry 41).
- Sources lines in `docs/views/sources/oa-12.jsonl`: 9 (entries 12 and 35 have none, as the launch prompt says for abstract-only copies).
- Papers with no measurement of a BRIEF trait: 2 (entries 29 and 48), each with a `"records": 0` sources line.

## Per paper

| Entry | Paper | Records | Notes |
|---|---|---|---|
| 6 | Yang et al. 2023, Artemisia baimaensis allelopathy on Elymus nutans | 7 (m) | sense_chemical: litter-extract germination and seedling growth, and growth beside living A. baimaensis (volatiles). Antioxidant-enzyme and osmolyte figures not logged (stress chemistry, no sensing claim). |
| 10 | Finlayson et al. 1998, phytochrome B and circadian ethylene in sorghum | 8 (m) | diel 2, sense_light_nonvisual 5, sense_thermal 1: daily and free-running ethylene rhythm, light plus temperature entrainment, phyB mutant amplitude, far-red shade phenocopy, elongation 1.3 times. |
| 12 | Yatsuhashi et al. 1982, UV action spectrum for anthocyanin in broom sorghum | 8 (m, partial, access abstract) | PMC holds only the abstract and page scans. Four action peaks, far-red tests, the phytochrome-free UV spectrum. No sources line. |
| 26 | Kaur et al. 2025, Phalaris minor germination | 12 (m) | Light/dark germination (means and Table 1 cells at three temperatures), radicle emergence onset and percentage. Seedling length, dry weight and vigour indices not logged (growth, not a light-sensing measure); Table 3 time series not logged cell by cell. |
| 29 | Yamashita and Tsuihiji 2022, lizard eye hard and soft tissue | 0 | Lens, scleral ring, axial length and eyeball dimensions only; no acuity, field or activity measurement. No basilisk acuity can be derived without receptor spacing. |
| 34 | Abacı et al. 2026, Ficus carica micropropagation | 6 (m; 2 partial) | White LED (4500 lx) versus 2:1 red-blue LED (600 lx): spectrum and intensity are confounded, said in each note. Two cited Black Jack values (Parab et al. 2021). |
| 35 | Stavenga and Arikawa 2006, butterfly colour vision review | 4 (m, partial, access abstract) | Groningen portal page with the abstract only. Tapetum, nymphalid receptor classes, Papilionidae and Pieridae screening pigments. No sources line. |
| 41 | Pons and de Jong-van Berkel 2004, R:FR gradient in canopies | 11 (m; 1 partial) | Supplemental far-red effects on five species, none in Carex; Ficus and Hedera leaf-shade null; Phaseolus abscission 22 d versus 17 d; cited Juglans (Frak et al. 2001). |
| 48 | Shenkutie et al. 2024, Sorghum phyB photosensory module crystallization | 0 | Expression, purification and crystals; no absorbance maxima are reported. |
| 60 | Zhang 2013, thesis on Phalaris arundinacea growth and climate | 1 (m) | sense_thermal: warming brought leaf senescence about 10 days earlier. No day-length or light treatment. |
| 67 | Zheng et al. 2022, Elymus sibiricus flowering transcriptome | 1 (g) | Photoperiod-pathway and clock genes predicted from annotation; no light treatment compared. |

## Source metadata changed from `sources-r1.jsonl`

- Entry 41: Crossref lists one author; the paper's first page names two, so `authors` is "Pons TL, de Jong-van Berkel YEM" (said in each note).
- Entry 60: Crossref gives "Chao Z"; the thesis citation line (page 3) reads "Zhang, C. 2013 … Dissertationes Forestales 162. 32 p.", so `authors` is "Zhang C" and the journal string carries "32 p." for the missing pages.

## For the audit

- Entry 41's PDF text drops decimal points (R:FR "105" for 1·05, chlorophyll a/b "42 to 37" for 4·2 to 3·7), so no value resting on those figures was logged.
- Entry 41's Phaseolus abscission sentence is split by a page break in the text; the quote marks that break with "…" and leaves out no words.
- Table rows (entries 26 and 34) are quoted from the layout part of the text, with column heads in `where`.
