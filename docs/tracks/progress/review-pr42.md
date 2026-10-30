# Review of PR #42, "Stop rejecting evidence quotes solely for exceeding 125 characters", 28 October 2026

Branch `fix/evidence-quote-word-limit` at `2c90cf90` (one commit), against `origin/main` at `5bfa7088`. Eight files changed, 160 lines added, none removed. The reviewer did not write the work.

**Verdict: MERGE AFTER FIXES.** Two fixes are required (F1, F2). The other notes are advisory.

## 1. Validator behaviour

- The only change to `tools/senses/check.py` is two comment lines above `MAX_QUOTE_WORDS = 40`. No logic changes.
- `python3 -I tools/senses/test_quote_limit.py` on the PR: 4 tests, OK. The same test file run against main's unmodified `check.py` and `addlog.py`, copied into a scratch directory, also passes. That shows the test describes main's existing behaviour.
- `python3 -I tools/senses/check.py` (whole repository), main against PR: both exit 1 with the same nine pre-existing problems (`intake-4-failed.jsonl` lines 2–7, `intake-5-failed.jsonl` lines 1–3, "source needs a doi or a url"). The diff of the two outputs contains only absolute-path prefixes plus the added line `quote-limit-recovery.jsonl: 3 records, 0 problems`.
- `check.py` on both new JSONL files reports 3 + 3 records and 0 problems.

## 2. Origin of the 125-character figure

The PR's claim is true.

- Main's rule is a count of 40 whitespace-separated words. `check.py` defines `MAX_QUOTE_WORDS = 40` and tests `len(q.split())`; that has been in place since the earliest commit of the file (f6b71964). `addlog.py` and `quotecheck.py` contain no character cap. The record template in BRIEF says "at most 40 words".
- The earliest explanation is `audit-4.md` (commit 712f353e, 14 October), in its opening paragraph and closing point 2: "the fetch summariser now caps each quoted piece at 125 characters". It presents this as a property of WebFetch's output, and as a reason to ask for the sentence in pieces.
- The figure then hardened into an admission rule in desk and audit reports. Examples: desk-d10 ("returned only sentences under 125 characters"), audit 110, 111, 114 and 116, audit 118 evidence verdict 1 ("Since the whole sentence exceeds 125 characters, no compliant quote from it exists"), desk-d24, desk-d32 (Epacris, Melilotus and Scilla dropped), desk-d34 (Toxicodendron and Scilla dropped), and `docs/tracks/desk-queue.md` lines 89 and 94. About 60 files mention it.
- No prompt in `docs/tracks/prompts/`, no part of BRIEF, no tool and no CI file on main states a 125-character limit.
- Every commit whose diff adds a "125-character" or "125 char" string is authored "Claude" (60 commits). The reviewer found no statement of the limit by the owner, and no line attributing it to the owner. The owner never stated it as a rule.
- One addition to the PR's account: audit 4's prescribed workaround was to request a long sentence in pieces and reassemble it. The PR's new text forbids "pieces requested to bypass that cap". That makes the PR stricter than audit 4, and no current prompt prescribes the piecewise method, so nothing conflicts. Readers of historical audits should know the method changed.

## 3. Recovered evidence records (`docs/views/evidence/quote-limit-recovery.jsonl`)

The reviewer checked sources with WebSearch, then WebFetch of URLs those searches returned. A direct `curl` of PMC was refused by the egress proxy. The WebFetch summariser still will not quote more than 125 characters, so exact-match checks below are the summariser's yes/no on the full string, plus surrounding context. They are not a byte-level quotecheck by the reviewer.

None of the three records duplicates main. A grep of `docs/views/evidence/*.jsonl` on main finds no Toxicodendron vernicifluum, no Melilotus suaveolens, and neither DOI.

**Toxicodendron vernicifluum, GA3** (Nemoto, Watanabe, Yoshida, Nishihara 2022, PLOS ONE 17(8): e0272665; checked at pmc.ncbi.nlm.nih.gov/articles/PMC9371279, from a search result).
- Quote: 26 words, 162 characters. It is reported present as a complete sentence in Results, after "tested the effects of both GA3 and GA4" and before "In contrast, GA4 treatment…". It is the study's own result, with the non-significance qualification intact.
- Conditions confirmed: 150 μM GA from DMSO stocks; 0.15% DMSO mock; 0.2% Plant Preservative Mixture; continuous light; 20 °C; scored at 60 days; 30 min sulfuric acid; precipitated fraction used; at least 50 seeds; at least three biological replicates. No cold pretreatment is stated for the GA assay.
- The Fig 2A/2C discrepancy is real. Results cites 2A, while the caption and Discussion place GA in panel C. The record preserves it correctly.
- The paper does not define the ± terms, so leaving them undefined is correct.
- Minor: Methods say "soaked … for up to 7 days", and Results say 7 days. Advisory A1.
- Grade `m`, `partial: false`, `access: open` are correct. Licence CC BY 4.0. Authors and their order are correct.
- POWO: taxon 71819-1 (from a search result) is accepted. The fetched page gave the authority as "(Stokes) Lincz.", but the name is accepted either way.

**Toxicodendron vernicifluum, GA4** (same paper).
- Quote: 34 words, 218 characters. It is reported present as a complete sentence in the Results subsection "Inactivating seed dormancy in T. vernicifluum with GA4 and cold temperature treatment", which matches `where`.
- It is the study's own result. The "approximately 10 times" wording is the authors'.
- Conditions, grade, partial flag and provenance are as for the GA3 record, and correct.

**Melilotus suaveolens, light** (Lai, Chen, Jiang, Zhou, Zheng, Shimizu 2016, AoB PLANTS 8: plw031; checked at pmc.ncbi.nlm.nih.gov/articles/PMC4940479, from a search result).
- Quote: 28 words, 182 characters. It is reported present verbatim as the last sentence of the Results paragraph "Effects of photon irradiance on seed germination". It is the authors' own result: the preceding sentence excepts C. microphylla and M. suaveolens from the no-difference finding.
- Conditions confirmed: Horqin Sandy Land; collected October 2004 (Table 1 row: October, 12 months storage); 4 °C; no scarification; 25/15 °C; 60:50% relative humidity; darkness or 14 h light / 10 h dark; 30 days; five replicates of 25 seeds; irradiances 0, 15, 62.5, 250 and 1000; inspection under dim light of 10 µmol m−2 s−1.
- The value claims no direction of the light effect, which is correct because the sentence gives none.
- Grade `m`, `partial: false`, `access: open` and CC BY 4.0 are correct. Logging only M. suaveolens from a two-species sentence is noted in `note`.
- **POWO status is not established (F2).** The PR records no POWO check for this name. The reviewer's fetch of the POWO page linked from IPNI 507046-1 (Melilotus suaveolens Ledeb.) was blocked by a permission timeout and was not retried. GBIF (Catalogue of Life) shows the name as "Species Accepted". WFO lists "Melilotus officinalis subsp. suaveolens (Ledeb.) H.Ohashi" as a synonym without naming its accepted name. Desk practice has held leads whose POWO status was unconfirmed (desk-queue d32, Onopordum caricum), so this record should not enter evidence until POWO acceptance is confirmed.

## 4. Held candidates (`docs/views/drafts/quote-limit-candidates.jsonl`)

All three are correctly kept out of `docs/views/evidence/`. No tool found in the repository reads JSONL from `docs/views/drafts/`, and the whole-repository `check.py` run does not pick the file up.

Each candidate's note says it is not admitted and needs source-text retrieval and quotecheck. `access: abstract` with `partial: true` matches main's practice (1,756 records carry that pairing). Each value is limited to what its sentence states, and the notes warn against over-reading (no general light insensitivity; no obligate darkness; no numerical GA benefit).

- **Epacris tasmanica:** the CSIRO publisher page (from a search result) reports the 20-word sentence verbatim. Authors and pages match. No rule is broken.
- **Scilla paui, darkness:** the revistabosque.org article page (from a search result) reports the wording matching, with one character difference. The page has "º" (masculine ordinal) in "5 ºC" and "15/4 ºC", where the candidate has "°" (degree sign). The quote would fail quotecheck as it stands. Advisory A2: resolve against the source text before admission. This is a good example of why the record is held.
- **Scilla paui, gibberellic acid:** reported verbatim, apart from italics. The sentence opens "This record, along with…", which refers back to the previous sentence, and its main claim is a dormancy classification. Holding it is correct. On admission, the value should stay qualitative, as drafted.
- Minor: BRIEF item 4 names `docs/views/drafts/<unit>.md` as the drafts file. A `.jsonl` file there departs from that convention, though that is harmless for a holding file. Advisory A3.

## 5. Documentation edits

Nothing in the BRIEF, oa-read or desk-audit edits weakens the quotation-integrity, omission, provenance or scientific-support rules.

- The edits restate whole-sentence or whole-row quoting, " … " for omissions, retention of subject, value, units and qualifications, and the ban on capitalising a clause into a sentence or dropping a null result or condition.
- They state that a quotecheck match is not scientific support.
- They keep the taxon, conditions, grade, partial and provenance requirements.
- desk-audit adds "never reinstate a record solely because its length passes", which keeps historical rejections from being mass-reversed.
- On tool restrictions, the text tells agents to use legally obtained source text or record a retrieval gap. It explicitly forbids soliciting pieces to evade a tool cap. Nothing instructs evasion.

One defect:

- **F1 (required).** BRIEF gains four lines at line 51, which shifts every later line by four. `docs/tracks/prompts/oa-read.md` line 19 and `docs/tracks/prompts/oa-pass.md` line 26 both cite "BRIEF lines 62 and 170" for the grading rule.
  - On main those lines are the `opened` rule and "Where species-level evidence hides".
  - On the PR branch, line 62 is a code fence and line 170 is the `g` wording line.
  - The references should become lines 66 and 174, or better, section or bullet names that do not drift.

## Required fixes

- **F1.** Update "BRIEF lines 62 and 170" in `oa-read.md` and `oa-pass.md` to the shifted lines (66 and 174), or replace the numbers with named references.
- **F2.** Confirm POWO acceptance of Melilotus suaveolens Ledeb. (POWO record linked from IPNI 507046-1) and record the POWO identifier in that record's `note`. If POWO treats it as a synonym or infraspecific taxon, either re-file it under the accepted name with the appropriate grade or move it to the drafts file. Adding the Toxicodendron POWO identifier (71819-1) to the two GA records would be consistent.

## Advisory

- **A1.** For the Toxicodendron records, say "soaked in water for 7 days (Methods: up to 7 days)".
- **A2.** For the Scilla darkness candidate, check the "º"/"°" character against the source text before admission.
- **A3.** Consider a short pointer in the drafts JSONL's companion progress file, or a `.md` file, if the BRIEF drafts convention matters.
- The investigation report's hashes and quotecheck runs on its own downloads could not be reproduced here, because the proxy refuses PMC and the downloads were not committed, which is correct. The reviewer's independent checks above agree with the report's readings.

Nothing was merged and nothing was pushed to main or to the PR branch.
