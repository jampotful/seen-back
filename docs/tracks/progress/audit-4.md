# Precision audit 4, 14 October 2026 (continuation of audit 3)

Continuation of `audit-3.md`: the same 60-record sample (seed 20261014), records 34, 46 and 50 to 60, to be followed by a full recheck of the eight batches audit 2 marked (sweep-12, sweep-6, sweep-11, sweep-8, sweep-22, insects-met, sweep-15, sweep-19). Method as in audits 2 and 3: each source URL opened with WebFetch and asked for the exact string, then for the full sentence in pieces (the fetch summariser now caps each quoted piece at 125 characters, so a long sentence comes back in consecutive pieces; the split points are recorded in `where`). Raw fetching (curl) is refused by the egress proxy for every host tried, so the summariser is the only route. A page blocked by a bot wall, robots rule or proxy refusal is `unverifiable`, never guessed. Corrections go to `docs/views/recheck/recheck-4.jsonl`; no evidence file is edited.

## Sample, continued

| # | id | view | taxon / trait | grade | partial | verdict | note |
|---|---|---|---|---|---|---|---|
| 34 | intake-4:30 | birds | Grus americana / eye_movement | m | no | unverifiable | Springer shows the abstract only ("preview of subscription content"); the USGS record has the abstract and no PDF; neither carries "heads fixed most of the time", "relative thrust speed" or "0.7 m", which the record places in the full-text Introduction or Discussion |
| 46 | sweep-27:9 | mammals | Equus caballus / receptor_classes | m | yes | correct | quote is the title, verbatim on the LUP page; the abstract confirms the two-choice task and "There was no evidence for a categorical boundary at the neutral point or elsewhere."; the abstract never says in so many words that horses are dichromats, which the record's note already flags (title-level statement) |
| 49 | herps-met:19 | herps | Bufo bufo / lambda_max_nm | m | no | unverifiable | Schott et al. 2022: PMC8820127 serves a reCAPTCHA interstitial (both the old and new PMC hosts); the Wiley full-text page returns a fetch error; the SFASU ScholarWorks PDF and the bioRxiv full-text HTML were refused at the permission step; the bioRxiv preprint PDF delivers only the captions of Tables 1 and 2 (rows deferred to Zenodo); Europe PMC's PDF route is robots-blocked and its XML service answered 429 |
| 50 | sweep-6:5 | herps | Trachemys scripta elegans / lambda_max_nm | m | no | requote | 617 nm confirmed; the quote ("617 nm or red; 515 nm or green; ...") is not on the Cambridge page the DOI resolves to; page: "There are four cone visual pigments, with λmax = 617 nm (red sensitive), 515 nm (green sensitive), 458 nm (blue sensitive), and 372 nm (UV-sensitive)."; rod value not in the abstract |
| 51 | intake-8:28 | herps | Triturus cristatus / depth_cue | m | no | unverifiable | the Springer page for 10.1007/BF00657609 was refused by the proxy (429) twice, 90 s apart, while neighbouring Springer pages opened; closed paper, quote placed in the Discussion |
| 52 | sweep-19:2 | herps | Rhinella marina / motion | m | yes | correct | quote verbatim in the UNE repository abstract; strip, right hemifield and "at 1.7 revolutions/min" confirmed |
| 53 | sweep-7:12 | herps | Bufo japonicus / motion | m | no | requote | value confirmed; the quote is the fetch tool's rendering (the note said so); page: "The present study showed that (1) the majority of the toad's tectal neurons exhibit properties of the ‘local motion detectors’ as defined above, and (2) these properties can be explained from the receptive field structure revealed in the present experiments." |
| 54 | herps-met:23 | herps | Dryophytes cinereus (as Hyla cinerea) / receptor_classes | g | no | unverifiable | same source as 49; the only text reached (preprint Discussion) says anurans "generally possess four of the visual opsins common to vertebrates", consistent with the value but not the Table 2 row |
| 55 | intake-3:50 | herps | Anura / pupil_shape | g | no | unverifiable | royalsocietypublishing.org returned a fetch error; the CONICET repository copy is restricted access and its page does not carry "10.8%"; no open copy found in two searches |
| 56 | herps-met:17 | herps | Rana temporaria / lambda_max_nm | m | no | unverifiable | same source as 49 |
| 57 | sweep-6:35 | herps | Trachemys scripta elegans (as Pseudemys scripta elegans) / acuity_cpd | m | no | requote | 4.4 to 9.9 confirmed; the quote is a rewording; page: "High spatial-frequency cutoffs ranged from 4.4–9.9 cycle/deg in different animals, the highest values corresponding to the intercone spacing in the area centralis and to behavioral measures of acuity in a related species." |
| 58 | sweep-17:14 | herps | Chelonia mydas / lambda_max_nm | m | yes | requote | values confirmed; the quote drops "It was found that", swaps "between" for "at roughly" and hyphens for en dashes; the page cites four primary sources (Witherington & Bjorndal 1991 added) |
| 59 | sweep-17:12 | herps | Chelonia mydas / fovea | m | yes | requote | value confirmed; quote is a paraphrase; page: "Three species of sea turtles (Chelonia mydas, Caretta caretta, and Dermochelys coriacea) possess a visual streak located along the horizontal mid-line of the retina, although they differed in streak development." |
| 60 | sweep-7:10 | herps | Bufo bufo / motion | m | no | requote | value confirmed, with "expansion" as the page's word; the quote is the fetch tool's rendering; page: "In the thalamus/pretectal region (mainly the caudal dorsal thalamus; see Fig. 3) units with circular excitatory receptive fields (ERF) of about 46 ° diameter were investigated." (space before the degree sign on the page) |

## Error rate

Sample complete: 60 of 60 opened. Verifiable 45 (31 in audit 2, 6 in audit 3, 8 here); wrong 18 (12 in audit 2, 6 here, all requote): **40%**. Unverifiable 15 (audit 2's three; 33, 37, 43, 44, 47, 48, 49 from audit 3; 34, 51, 54, 55, 56 here). No record in this run needed a regrade or a retract: every verifiable value stood, and the error is wording.

By batch, this run only (verifiable / wrong): sweep-27 1/0, sweep-19 1/0, sweep-6 2/2, sweep-7 2/2, sweep-17 2/2.

Whole sample by batch (verifiable / wrong), updating audit 2's table: sweep-6 5/4, sweep-7 2/2, sweep-17 2/2, sweep-12 3/3, sweep-11 3/2, sweep-8 1/1, sweep-22 1/1, sweep-15 3/1, sweep-19 4/1, insects-met 2/1, sweep-27 1/0, intake-5 2/0, intake-6 2/0, intake-8 1/0, sweep-29 3/0, sweep-9 1/0, sweep-13 1/0, sweep-14 1/0, sweep-16 1/0, sweep-20 3/0, sweep-31 1/0, intake-3 1/0. By the THOROUGH rule (over 5% wrong, or two or more wrong), sweep-7 and sweep-17 join the eight batches already due a whole recheck.

## Batch recheck

Not started. The run stopped before part 2 (see below). Batches due: sweep-12 (10 lines), sweep-6 (36), sweep-11 (17), sweep-8 (24), sweep-22 (6), insects-met (52), sweep-15 (14), sweep-19 (20), plus sweep-7 (18) and sweep-17 (14) from this run; skip ids already corrected in `recheck-2.jsonl` and `recheck-4.jsonl` (sweep-6:5, sweep-6:35, sweep-17:14, sweep-17:12, sweep-7:12, sweep-7:10) and any retracted in `docs/views/audit/ALL.jsonl`.

| batch | records checked | errors | error rate |
|---|---|---|---|
| sweep-12 | 0 | 0 | not started |
| sweep-6 | 0 | 0 | not started |
| sweep-11 | 0 | 0 | not started |
| sweep-8 | 0 | 0 | not started |
| sweep-22 | 0 | 0 | not started |
| insects-met | 0 | 0 | not started |
| sweep-15 | 0 | 0 | not started |
| sweep-19 | 0 | 0 | not started |

## Where this run stopped

Three proxy 429 refusals: the Europe PMC XML service (record 49), then the Springer page for record 51 twice (the second after a 90 s wait, while two other Springer pages opened in between). The brief says to stop on repeated 429s, so the run stopped after record 51's second refusal, with 20 fetches and 5 searches used. Nothing of the batch recheck has been started.

## Patterns (this run)

1. Six of eight verifiable records were requotes, and all six had the same shape: the value is right, the quote is the fetch summariser's rendering of the abstract (two of the six said so in their own note). Three were in sweep-7 and sweep-17, batches audit 2 had not sampled as wrong.
2. The summariser now caps every quoted piece at 125 characters. A sentence longer than that must be asked for in pieces, with the split points stated, and then reassembled; asking "does this exact string appear" first, and only then for the sentence, keeps the answer honest.
3. Page delivery remains the main obstacle, as audit 3 said: PMC (both hosts) serves a reCAPTCHA, Wiley and Royal Society pages fail outright, Springer closed papers show the abstract only, and permission-gated hosts (ScholarWorks, bioRxiv HTML) time out. Europe PMC is robots-blocked for PDFs and rate-limited for XML. The Schott et al. 2022 table rows (records 49, 54, 56) need an owner PDF through `quotecheck.py`.
4. The proxy's 429s look per-URL as much as per-host: one Springer page was refused twice while others on the same host opened.
