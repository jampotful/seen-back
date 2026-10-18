# oa-2 reading pass, reader F (18 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md`, with the control room's two later instructions (run `tools/views/oa_lint.py` before each commit; the corrected grade rule). Entry 47 of `oa-2`, read from the text the `oa` job fetched again for this reader (branch `run/oa/read-f`, run 8, `runs/oa/8-oa-2` on `ci`). The text decrypted with a matching checksum, and the checksum equals the rescue run's (`runs/oa/2-oa-2`), so the audit can use that text. Reading branch: `agent/oa-read-f`. This note is named `oa-2-read-f.md` because reader B writes `oa-2-read-b.md` for other `oa-2` entries at the same time.

## Counts

| Entry | Paper | Copy | Records | m | g | i | partial |
|---|---|---|---|---|---|---|---|
| 47 | Lariguet and Dunand 2005, Plant photoreceptors: phylogenetic overview (J Mol Evol 61: 559-569) | Archive ouverte UNIGE, published version | 48 | 12 | 2 | 34 | 17 |

One line added to `docs/views/sources/oa-2.jsonl`. Every record passes `quotecheck.py` (48 verbatim) and `oa_lint.py --text` against the paper. All records use `sense_light_nonvisual`.

## What was logged

- The paper's own survey of photoreceptor genes (cryptochromes, phototropins, phytochromes, ZTL and the putative UV-B receptor ULI3) in Chlamydomonas reinhardtii, Amborella tricopoda, Adiantum capillus-veneris, Lycopersicon esculantum, Pisum sativum, Vicia faba, Pinus sylvestris, Ceratopteris richardii, Brassica oleracea, Arabidopsis thaliana and the groups it names (angiosperms, monocots, eudicots, gymnosperms, pteridophytes, bryophytes, green plants, Brassicaceae): predictions from sequences, so `i`, with the prediction named in `method`. Absences carry the paper's own warning that small EST databases may hide sequences.
- Cited statements on Arabidopsis (phototropins, phytochromes and ZTL-family receptors, their wavelength ranges, the 550-660 nm gap of Fig. 1, and their roles in germination, shade avoidance, chloroplast movement and flowering) and Chlamydomonas phototaxis: `m` with `partial: true` and the cited studies in `note`.
- Two group statements that are not sequence predictions, `g` and `partial`: the cryptochromes' 320-520 nm range for plants in general, and phytochrome-mediated phototropism in mosses.

`docs/views/evidence/canon-3.jsonl` already holds eight records from this paper (graded `g` there).

## Not logged

- The phytochromes' 600-750 nm absorption range: the text breaks "600–" and "750" across a line, and `quotecheck.py` joins a dash at a line end, so no exact quote of the range can pass both checkers. The five-phytochromes record's note says so.
- The Supplemental Table (sequence names and accession numbers only), intron counts and the PKS and maximum-likelihood analyses: no BRIEF trait.

## Conventions and deviations

- Group names are written in their Latin forms (Angiospermae, Monocotyledoneae, Eudicotyledoneae, Gymnospermae, Pteridophyta, Bryophyta, Viridiplantae, Plantae) with the paper's own word in `note`. Where a sentence names only a genus (Adiantum, Lycopersicon, Pinus, Ceratopteris), the species is the one the Methods list gives for that sequence prefix, as each note says.
- The key pair lives in `/tmp/oa-f`, not `/tmp/oa`, because other readers share the machine. It was never committed or printed.
- Grades were first written under the prompt's narrower grade line (all `g`) and corrected in commit 07f33e1d after the control room's message.

Nothing in the paper was left unread.
