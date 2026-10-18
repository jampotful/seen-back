# oa-6 reading pass, reader F (18 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md`, with the control room's two later instructions (run `tools/views/oa_lint.py` before each commit; the corrected grade rule). Entry 33 of `oa-6`, read from the text the `oa` job fetched again for this reader (branch `run/oa/read-f`, run 8, `runs/oa/8-oa-6` on `ci`). The text decrypted with a matching checksum, and the checksum equals the rescue run's (`runs/oa/2-oa-6`), so the audit can use that text. Reading branch: `agent/oa-read-f`. This note is named `oa-6-read-f.md` so that it cannot collide with another reader's note for the same batch.

## Counts

| Entry | Paper | Copy | Records | m | g | i | partial |
|---|---|---|---|---|---|---|---|
| 33 | Brooke, Hanley and Laughlin 1999, eye size and body mass in birds (Proc R Soc B 266: 405-412) | Europe PMC PDF, published version | 26 | 13 | 10 | 3 | 11 |

One line added to `docs/views/sources/oa-6.jsonl` (DOI 10.1098/rspb.1999.0652 from `ci/oa/sources-r1.jsonl`; the batch entry has no DOI). Every record passes `quotecheck.py` (26 verbatim) and `oa_lint.py --text` against the paper.

## What was logged

- Eye diameter by the paper's Plasticine method for seven species, graded `m`: the five rows of Table 1 (Struthio camelus, Puffinus puffinus, Aquila audax, Strix aluco, Columba livia) and the two ends of the size range named in the Discussion (Acanthiza pusilla 6 mm, Haliaetus albicilla 46 mm, genus spelled as printed).
- The axial lengths Table 1 takes from the literature (six values, four studies named in its footnotes), `m` with `partial: true`.
- Raptors' and owls' eyes 1.4 and 2.2 times the eye mass of an average bird of the same weight, and the equation log(eye mass) = 0.68 log(body mass) - log(23.9): values from the paper's allometric equations, so `i`, with the model named in `method`.
- Relative eye size of kiwis, penguins and the four large ratites against the flying-bird regression (`g`, collective or group statements; the kiwi sentence cites Walls 1942, so it alone is `partial`), and four further group records, all `g` and `partial`: the diel statements for owls, parrots and kiwis, and the raptors' deep foveal pit cited from Snyder and Miller (1978).

Eye size has no key in BRIEF's list; the records use the existing new-trait keys `eye_diameter_mm` and `eye_axial_length_mm` and two new ones, `relative_eye_size` and `eye_mass_allometry`, each with "new trait" and its reason in `note`.

## Not logged

- Table 2 (scaling exponents per order by three methods), the skull-width and skull-length regressions, and the flight-speed argument: statistics of allometry, not traits of a taxon.
- Per-species points in Figures 1 to 4: graphical only.

## Conventions and deviations

- Table rows are quoted as one line of the `=== LAYOUT ===` section, whitespace collapsed, because the plain-text part prints Table 1 column by column. The text layer prints the paper's ligatures as ¢, £, ¡ and ¤ and its equals sign as U+0088; quotes keep these characters exactly.
- The key pair lives in `/tmp/oa-f`, not `/tmp/oa`, because other readers share the machine. It was never committed or printed.
- Grades were first written under the prompt's narrower grade line and corrected in commit 07f33e1d after the control room's message: cited values on the record's own species are `m` with `partial: true`; values from an allometric equation are `i`.

Nothing in the paper was left unread.
