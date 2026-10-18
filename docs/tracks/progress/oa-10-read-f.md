# oa-10 reading pass, reader F (18 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md`, with the control room's two later instructions (run `tools/views/oa_lint.py` before each commit; the corrected grade rule). Entry 25 of `oa-10`, read from the text the `oa` job fetched again for this reader (branch `run/oa/read-f`, run 8, `runs/oa/8-oa-10` on `ci`). The text decrypted with a matching checksum, and the checksum equals the rescue run's (`runs/oa/2-oa-10`), so the audit can use that text. Reading branch: `agent/oa-read-f`. This note is named `oa-10-read-f.md` so that it cannot collide with another reader's note for the same batch. `docs/views/evidence/oa-10.jsonl` and `docs/views/sources/oa-10.jsonl` are new files on this branch.

## Counts

| Entry | Paper | Copy | Records | m | g | i | partial |
|---|---|---|---|---|---|---|---|
| 25 | Flores et al. 2011, seed photoblastism in cacti (Environ Exp Bot 71: 79-88) | CONICET repository PDF | 592 | 588 | 0 | 4 | 337 |

Every record passes `quotecheck.py` (592 verbatim) and `oa_lint.py --text` against the paper.

The repository and OpenAlex label the copy a submitted version, but the text is the typeset article with the journal's header, copyright line and page numbers, and it does not call itself a preprint or manuscript; the source line says so.

## What was logged

- Table 1 holds all 196 taxa (the title's 136 are the subset analysed). For each taxon three `sense_light_nonvisual` records: germination percentage in light, germination percentage in darkness, and the paper's Relative Light Germination, RLG = Gl/(Gd + Gl). RLG matches the two percentages in every row.
- 85 taxa are the paper's own data, marked "New data" in Table 1 (the Methods say 86): 30 d on agar at 25 °C, a 14-h photoperiod against foil-wrapped darkness, four replicates of 25 seeds. They are graded `m`. The other 111 are compiled from the study named in the row's References column; they are `m` with `partial: true` and that study in `note`.
- Four group means of RLG (dormant, non-dormant, cylindrical and globose taxa), reported with the analysis of covariance: model estimates, so `i`, `partial` because the analysis pools compiled values.

## Not logged

- Table 1's seed mass, dispersal syndrome, plant length, life form and country columns, Table 2's P values and Figures 1 to 4: no BRIEF trait, or graphical only.
- The batch entry asked after Pelecyphora (Escobaria) vivipara; it is not in Table 1. Pelecyphora strobiliformis and Escobaria emskoetteriana are.

## Conventions and deviations

- Each record quotes its taxon's row from the `=== LAYOUT ===` section, whitespace collapsed (the plain-text part prints the table column by column), with the column heads in `where`.
- Infraspecific names are written without the rank word (Ariocarpus bravoanus bravoanus for "Ariocarpus bravoanus ssp. bravoanus", rank `subspecies`, `variety` or `form`), because `oa_lint.py`'s one-species test does not accept "ssp.", "var." or "f."; each such record's note gives the name as printed. Printed misspellings are kept (Coryphanta radians, Maihuenia poeppiggi); ligatures in names are written out.
- The key pair lives in `/tmp/oa-f`, not `/tmp/oa`, because other readers share the machine. It was never committed or printed.
- Grades were first written under the prompt's narrower grade line (compiled rows `g`) and corrected in commit 07f33e1d after the control room's message.

Nothing in the paper was left unread.
