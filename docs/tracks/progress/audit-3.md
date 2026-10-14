# Precision audit 3, 14 October 2026 (continuation of audit 2)

Continuation of `audit-2.md` by Opus: the same 60-record sample (seed 20261014), records 33, 34 and 37 to 60, then a full recheck of the eight batches audit 2 marked (sweep-12, sweep-6, sweep-11, sweep-8, sweep-22, insects-met, sweep-15, sweep-19). Method as in audit 2: each source URL opened with WebFetch and asked for the exact string; a page blocked by a bot wall, robots rule or proxy refusal is `unverifiable`, never guessed. Corrections go to `docs/views/recheck/recheck-3.jsonl`; no evidence file is edited.

## Sample, continued

| # | id | view | taxon / trait | grade | partial | verdict | note |
|---|---|---|---|---|---|---|---|
| 33 | intake-8:6 | birds | Strix aluco / lambda_max_nm | m | no | unverifiable | two searches found no open copy of Hoglund et al. 2019 (Elsevier, closed); the PubMed lookup was refused by the proxy (429) |
| 34 | intake-4:30 | birds | Grus americana / eye_movement | m | no | pending | not reached: run stopped at record 49 on repeated 429 refusals |
| 37 | intake-7:27 | mammals | Camelus dromedarius / tapetum | m | no | unverifiable | doi.org link for 10.32819/2020.82018 refused by the proxy (429); not retried |
| 38 | sweep-29:4 | mammals | Oryctolagus cuniculus / tapetum | m | yes | correct | quote verbatim on the IVIS page ("Rabbits have a non-reflective retina (no tapetum lucidum)."); the page says "rabbits" and never names Oryctolagus cuniculus, as the note already says |
| 39 | intake-6:18 | mammals | Myocastor coypus / fovea | m | yes | correct | quote verbatim in the Zoological Studies abstract (doi.org resolved to zoolstud.sinica.edu.tw) |
| 40 | intake-8:35 | mammals | Capra hircus / tapetum | m | yes | correct | quote verbatim in the KoreaScience English abstract; 30 Korean native goats |
| 41 | intake-5:31 | mammals | Capra hircus / fov_h_deg | m | no | correct | string on the page: "estimated to be 290 – 313° in sheep (Piggins and Phillips, 1996; Kendrick, 2008); 320 – 340° in goats"; the review calls the 320 to 340 figure a "wide monocular field of vision", which at that size is the whole horizontal field; secondary (Piggins and Phillips 1996) |
| 42 | intake-6:16 | mammals | Myocastor coypus / pupil_shape | m | yes | correct | quote verbatim in the abstract |
| 43 | intake-3:3 | mammals | Bos taurus / acuity_cpd | m | no | unverifiable | ScienceDirect refuses the fetcher (robots); one search found no other copy of Entsu et al. 1992 |
| 44 | intake-3:5 | mammals | Bos taurus / fov_h_deg | m | no | unverifiable | same page as 43 |
| 45 | intake-5:24 | mammals | Bos taurus / lambda_max_nm | m | no | correct | exact string present in the SLU repository copy (pub.epsilon.slu.se/id/document/20443609); the Frontiers HTML page delivered to the fetcher ends inside section 2.3.2, before the cattle colour section; the review attributes the value to Jacobs et al. 1998 |
| 46 | sweep-27:9 | mammals | Equus caballus / receptor_classes | m | yes | pending | not reached |
| 47 | mammals-met:7 | mammals | Kerodon rupestris / pupil_shape | m | no | unverifiable | doi.org link for 10.4322/jms.058813 returned a fetch error; not retried |
| 48 | intake-7:24 | mammals | Bos taurus / colour_vision | m | no | unverifiable | ScienceDirect refuses the fetcher (robots) |
| 49 | herps-met:19 | herps | Bufo bufo / lambda_max_nm | m | no | unverifiable | Wiley doi link returned a fetch error; PMC8820127 answered with a browser-check interstitial; the Europe PMC XML service was refused by the proxy (429); run stopped here |
| 50 | sweep-6:5 | herps | Trachemys scripta elegans / lambda_max_nm | m | no | pending | not reached |
| 51 | intake-8:28 | herps | Triturus cristatus / depth_cue | m | no | pending | not reached |
| 52 | sweep-19:2 | herps | Rhinella marina / motion | m | yes | pending | not reached |
| 53 | sweep-7:12 | herps | Bufo japonicus / motion | m | no | pending | not reached |
| 54 | herps-met:23 | herps | Dryophytes cinereus (as Hyla cinerea) / receptor_classes | g | no | pending | not reached (same source as 49) |
| 55 | intake-3:50 | herps | Anura / pupil_shape | g | no | pending | not reached |
| 56 | herps-met:17 | herps | Rana temporaria / lambda_max_nm | m | no | pending | not reached (same source as 49) |
| 57 | sweep-6:35 | herps | Trachemys scripta elegans (as Pseudemys scripta elegans) / acuity_cpd | m | no | pending | not reached |
| 58 | sweep-17:14 | herps | Chelonia mydas / lambda_max_nm | m | yes | pending | not reached |
| 59 | sweep-17:12 | herps | Chelonia mydas / fovea | m | yes | pending | not reached |
| 60 | sweep-7:10 | herps | Bufo bufo / motion | m | no | pending | not reached |

## Error rate

Audit 2 and this continuation together: opened 46 of 60; verifiable 37 (31 from audit 2, 6 here); wrong 12 (all from audit 2): **32%**. The six verifiable records here were all correct; all six are abstract-page or repository reads where the logger copied a sentence, the pattern audit 2 noted.

Unverifiable so far: 12 (audit 2's three, plus 33, 37, 43, 44, 47, 48, 49 here). Pending: 14 (34, 46, 50 to 60).

By batch, this run only (verifiable / wrong): intake-5 2/0, intake-6 2/0, intake-8 1/0, sweep-29 1/0.

## Where this run stopped

The fetch proxy answered 429 three times (PubMed for record 33, doi.org for record 37, the Europe PMC service for record 49), each on a different host and each after other fetches had succeeded, so the refusals look like per-host rate limits rather than a used-up search budget; WebSearch itself answered every query (four queries used). The brief says to stop on repeated 429s and not retry, so the run stopped at record 49 after 14 fetches and 4 searches. Nothing of the batch recheck (part 2) has been started. `docs/views/recheck/recheck-3.jsonl` is not created because no correction was found.

A resumed run should take records 34, 46 and 50 to 60 first (14 records, of which 54 and 56 share the Schott et al. 2022 source with 49, PMC8820127, which needs a non-interstitial route), then recheck the eight batches whole: sweep-12 (10 lines), sweep-6 (36), sweep-11 (17), sweep-8 (24), sweep-22 (6), insects-met (52), sweep-15 (14), sweep-19 (20), skipping the ids already corrected in `recheck-2.jsonl` (sweep-19:14, sweep-12:4, sweep-11:7, sweep-15:13, sweep-8:9, insects-met:37, sweep-12:10, sweep-11:15, sweep-22:6, sweep-6:32, sweep-6:10, sweep-12:8) and any retracted in `docs/views/audit/ALL.jsonl`.

## Patterns (this run)

1. Nothing new on wording: the six records checked were verbatim copies from pages the logger could see.
2. Page delivery, not page content, is now the main obstacle: ScienceDirect refuses robots outright (three records), PMC serves a browser check, Wiley doi links fail, and the proxy rate-limits new hosts. A recheck of the eight batches will meet the same walls on every Elsevier and Wiley record, so a route to those (owner PDFs through `quotecheck.py`, or Europe PMC once the limit clears) is worth settling before the batch recheck starts.
3. Frontiers HTML pages reach the fetcher truncated (84,333 characters, ending mid-section); a repository copy of the same article (SLU) carried the full text. When a Frontiers quote cannot be found, try the repository copy before marking it absent.
