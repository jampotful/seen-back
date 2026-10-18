# Review 55, 18 October 2026

Population: the latest version of each of the 499 records in `recheck-42-fixed` to `recheck-52-fixed` (retracted ids replaced by their `recheck-53-fixed` and then `recheck-54-fixed` corrections; `requote-partial.jsonl` applied). Grades: 131 m, 346 g, 22 i. Every record was read against the four fault types from quote, where, note, method, value, units, taxon and trait alone; no source was opened. Worktree `/tmp/wsr55`, branch `research/review-55`, cut from `research/repair-crossref`.

Output: `docs/views/recheck/recheck-55.jsonl`, 101 rows (95 correct, 6 retract) covering 101 distinct records. No evidence file or ALL.jsonl was edited and `apply_recheck` was not run. Ids below are the latest-version ids (`recheck-N-fixed:LINE`) used in `supersedes`.

## Counts per fault type

A row can carry more than one fault, so the counts overlap.

| fault | records |
|---|---|
| (1) value broader or narrower than the quote supports (corrected) | 45 |
| (1) value unsupported (retracted) | 6 |
| (2) grade too high | 58 |
| (3) unmarked cut | 5 |
| (4) author field ends "et al." | 7 (listed, no row) |

## (1) Value faults, corrected
42-fixed:19, 54-fixed:10, 43-fixed:19, 53-fixed:25, 44-fixed:3, 44-fixed:9, 54-fixed:53, 54-fixed:54, 45-fixed:53, 53-fixed:74, 45-fixed:71, 45-fixed:73, 53-fixed:80, 54-fixed:93, 53-fixed:95, 53-fixed:96, 53-fixed:99, 53-fixed:100, 53-fixed:106, 53-fixed:115, 53-fixed:117, 53-fixed:120, 53-fixed:121, 53-fixed:122, 53-fixed:123, 54-fixed:103, 47-fixed:85, 54-fixed:107, 54-fixed:108, 49-fixed:30, 49-fixed:36, 49-fixed:37, 53-fixed:160, 53-fixed:177, 53-fixed:179, 53-fixed:197, 53-fixed:198, 53-fixed:206, 50-fixed:75, 51-fixed:25, 53-fixed:214, 53-fixed:215, 54-fixed:122, 54-fixed:123, 52-fixed:48

Typical faults: a number or finding from another sentence of the paper (15 and 21 days, 50-60% light, kinetin 1 mg/L), a mean taken from Table 1 where the quote gives a rounded figure (Orgyia 1.92 and 3.03 against the quoted 1.9 and 3.0, and the cpd values computed from them), a bound written as a measurement (at least 2 m, 0.5 s upper bound), a classification the quote does not use (acute zone, area centralis, camera-type), and a regional statement written as a whole-eye one (Lycaena rubidus, Apis mellifera drone).

## (1) Retracted
54-fixed:52, 46-fixed:34, 49-fixed:26, 54-fixed:117, 53-fixed:213, 52-fixed:43

- `recheck-54-fixed:52` (Calendula arvensis): the quote is a general photoperception sentence that names no species.
- `recheck-46-fixed:34` (Panicum miliaceum): the quote describes the design (genotypes exposed to 16 h and 8 h photoperiods) and states no result.
- `recheck-49-fixed:26` (Marmota monax): the quote concerns the alpine marmot and gives the woodchuck no value of its own.
- `recheck-54-fixed:117` (Pseudemys nelsoni, 36-month retention): the quote says the turtles were tested and retrained, not that they retained the task.
- `recheck-53-fixed:213` (Galium aparine): the quote describes the growth regimes only.
- `recheck-52-fixed:43` (Bothrops jararaca juvenile "acute zone"): the quote puts juvenile cones in the ventral retina.

## (2) Grade faults

Quote names no species (m to g): 56 rows.
42-fixed:20, 53-fixed:25, 44-fixed:1, 44-fixed:2, 44-fixed:3, 44-fixed:4, 44-fixed:5, 44-fixed:6, 44-fixed:7, 44-fixed:12, 53-fixed:27, 45-fixed:71, 45-fixed:73, 53-fixed:78, 53-fixed:79, 53-fixed:120, 53-fixed:122, 47-fixed:76, 47-fixed:77, 47-fixed:78, 47-fixed:79, 53-fixed:124, 53-fixed:125, 53-fixed:135, 49-fixed:29, 49-fixed:36, 49-fixed:37, 53-fixed:195, 53-fixed:196, 53-fixed:201, 53-fixed:202, 53-fixed:203, 53-fixed:204, 53-fixed:205, 53-fixed:206, 53-fixed:207, 53-fixed:209, 50-fixed:75, 51-fixed:25, 53-fixed:219, 53-fixed:222, 53-fixed:223, 53-fixed:224, 53-fixed:225, 53-fixed:226, 53-fixed:227, 53-fixed:228, 53-fixed:229, 53-fixed:230, 53-fixed:231, 53-fixed:237, 53-fixed:244, 53-fixed:245, 53-fixed:246, 53-fixed:247, 52-fixed:42

This is the largest group and a judgement the caller may reverse as a block: the quote contains no scientific or common name, only "the animals", "this study", "these creatures", "Generally" or a bare trait statement, so by the rule "m only for one named species with its own value in the quote" it cannot be m. Single-species papers (Deilephila elpenor, Deinopis spinosa, Bubo virginianus, Meleagris gallopavo) account for most rows. Records whose quote carries a common name (loggerhead, leatherback, black kite, Harris's hawk, American crow, jungle crow, pot marigold, Pallas's cat, bilberry, sandwort) kept m.

Other grade changes: 53-fixed:99, 53-fixed:160.
- `recheck-53-fixed:99` (Lycaena rubidus, 3 classes) and `recheck-53-fixed:160` (Salticidae acuity) go to i because the value is arithmetic on stated numbers. `recheck-43-fixed:19` (Pelodiscus 19-bp deletion) goes to i because inactivation is inferred.

Kept at m after thought: sentences naming two species that each carry their own value ("80% and 85% respectively", Harris's hawk and black kite pairs, O. wendtii and O. pumila). If the caller reads the rule as one species per quote, these go to g: recheck-46-fixed:8 and :16, recheck-51-fixed:1-8, recheck-53-fixed:74-75.

Group statements already regraded by recheck-54 were not found again; no residual "all N species" statement graded m remained once the named-species test above was applied.

## (3) Unmarked cuts
53-fixed:71, 53-fixed:72, 47-fixed:83, 49-fixed:12, 49-fixed:13

- `recheck-53-fixed:71`, `:72` (Menemerus confusus): the sentence continues after "Tateda, 1976)"; closing ellipsis added and `where` updated.
- `recheck-49-fixed:12`, `:13` (snake SWS1 site 86): the quote ends at "respectively" and the sentence goes on; closing ellipsis added.
- `recheck-47-fixed:83` (Vaccinium angustifolium): the quote opens "Percival and MacKenzie, 2007) noted" mid-citation; leading ellipsis added.

No other quote began lower-case without a marked cut or stopped without terminal punctuation or ellipsis.

## (4) Needs author list

Author field ends "et al.": `recheck-44-fixed:12` (Fang Y, Qin X, Liao Q, Du R, Luo X, et al.; genome of the maidenhair fern) and `recheck-54-fixed:71` to `:76` (Schott RK ... Loew ER, et al., Bell RC; frog visual opsins; audit 34 counted 29 printed authors). No names were guessed.

## Not changed, noted

- Eye-specific quotes for Hasarius adansoni (`recheck-53-fixed:46` to `:49`): the record's `eye` field says ALE or PLE where the sentence names no eye; the value label "RH3/RH4" follows the paper's note that the antibody cannot separate them. Left as is.
- Journal fields lacking an issue or missing (audits 34 and 35) are outside the four fault types and were not touched.
