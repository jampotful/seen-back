# oa-12 reading pass, reader H2 (18 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md`, with the texts already fetched and decrypted on the machine (no key, no run branch). Entries in order: 13, 20, 38, 45, 53, 58, 64, 70, 71, 74. Texts: `/tmp/oa-shared/oa-12/oa-12-<entry>.txt` (not committed). Branch `agent/oa-read-h2`. Every record passed `tools/views/oa_lint.py --text` and `tools/views/quotecheck.py` against its own paper, and `tools/senses/check.py`; every quote is at most 40 words.

## Papers

| entry | paper | read | records |
|---|---|---|---:|
| 13 | Eckardt 2001, Auxin and the Power of the Proteasome in Plants (Plant Cell) | full text (PMC page) | 3 |
| 20 | Chan et al. 2024, eye morphology of Lepidoptera (Research Square preprint) | full text (PDF) | 10 |
| 38 | Swanton et al. 2026, light signaling in crop-weed competition (Weed Technology review) | full text (PDF) | 45 |
| 45 | Sondhi et al. 2024, day-night gene expression in two saturniid moths (Proc R Soc B) | full text (Europe PMC XML) | 2 |
| 53 | Douma et al. 2019, light quality and plant defence, a model of Brassica nigra (Plant Cell Environ) | full text (Europe PMC XML) | 3 |
| 58 | Tyrrell and Fernández-Juricic 2017, avian binocular vision and the anterior blind area (PLOS ONE) | full text (Europe PMC XML; S1 Table not included) | 14 |
| 64 | Troscianko et al. 2025, butterfly wing patterns and illusory motion (Research Square preprint) | full text (PDF) | 3 |
| 70 | Quan et al. 2018, UV-B and jasmonic acid in Scutellaria baicalensis (IJMS) | full text (Europe PMC XML; Tables 1 to 3 not included) | 7 |
| 71 | Pegiou et al. 2019, green and white asparagus (Metabolites review) | full text (Europe PMC XML) | 5 |
| 74 | Aidala et al. 2012, predicted SWS1 sensitivity in New Zealand cuckoos (Chinese Birds) | full text (PDF) | 13 |

## Counts

- Papers read: 10 of 10, all full texts; none was only an abstract or landing page, so no `access: abstract` record. Papers with no measurement of a BRIEF trait: none.
- Records: 105 in `docs/views/evidence/oa-12.jsonl`; grade `m` 87, `g` 18, `i` 0; `partial: true` 94.
- Sources lines: 10 in `docs/views/sources/oa-12.jsonl`.
- `g` records: predictions from gene sequences (SWS1 type in entry 74, a new trait key `sws1_type` as earlier logs use it), inferences from morphology or models (entries 20, 38 Rosa hybrida, 53), and values for part of a group (entries 20, 58, 64).

## Notes for the audit

- Entry 13: the PMC page prints pages 2161–2164; the source object keeps Crossref's 2161-2163 as `sources-r1.jsonl` gives it. The PMC copy is the published version although the lookup lists it as a submitted version.
- Entries 20 and 64 are Research Square preprints with no journal in `sources-r1.jsonl`; the journal field reads "Research Square (preprint)" and each note says so.
- Entry 20: its own measurements (eye position, relative eye size and inter-eye distance from specimen photographs) are indices with no BRIEF trait, so they are not logged; its diel and eye-type assignments come from the literature (Tables S1 to S3 are not in the text) and are logged as partial.
- Entry 38 is a review; all 45 records are partial and name the cited study. Records about growth and biochemistry under low R:FR are logged under `sense_light_nonvisual` with the light condition in `value` or `conditions`.
- Entry 58: the binocular widths of the 40 species are in its S1 Table, a supplementary DOCX not in the text read; fetching it would add species-level `binocular_deg` values.
- Entry 70: Tables 1 to 3 are not in the XML text; the logged percentages are those stated in the Results text.
- Table rows in entry 74 are quoted from the layout part of the file, where the rows of Table 1 are whole lines.
- Leads from the wanted list that the texts do not answer: Cynoglossum (entry 53), a measured R:FR response of Ambrosia (entry 38, where Ambrosia appears only in nitrogen and yield studies), acuity or interommatidial angles of Lerema and Pyrgus (entries 20 and 64), and Haliastur (entry 58).
- Commit 577058a is titled "entries 20 and 38" but carries entry 20 only; entry 38 is in d319838.
