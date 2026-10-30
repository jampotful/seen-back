# Integration of PRs 42 and 44, 30 October 2026

The owner requested integration of the two existing contributions without repeating their completed investigations. The integration baseline was main `75546c727eab9d0e2258ba22ca5519aaa558679c`, after desk-d105 / audit 195. Main was 76 commits beyond PR 42's common ancestor and 46 beyond PR 44's. Every existing file changed by either contribution still matched its common-ancestor version at that baseline.

## PR 42 disposition

The original PR branch was fast-forwarded to the independently reviewed correction commit `cea49ef4059585a0488f2dcc206842312d55a9a1`; that commit was exactly one ahead of `2c90cf902b99525c1a0878651bdf5ef77c1ce495`. Integration commit `d4ea2b624fccdf4a53c06a93da0139ea33aa8aad` retains both that ancestry and current main. PR 42 was merged through GitHub as `598aea23d75ba269cb59c9e86b9e8e8d49850b7e`.

The independent review from `0bae7f085124e731189727a69336677104c3da07` is copied verbatim to `review-pr42.md`. Its original verdict and investigation report remain historical records. The corrected numeric BRIEF references were replaced with named sections. Melilotus suaveolens remains in drafts, with an explicit taxonomic hold in its note and a companion disposition. Only the two reviewed Toxicodendron vernicifluum records enter accepted evidence; the GA3 non-significance and Fig 2A/2C discrepancy remain intact.

## PR 44 scientific review and instruction reconciliation

The existing reassessment, evidence changes and recorded source fingerprints were reviewed. Arbutus retains the relative GA3 response while restoring low absolute emergence and distinguishing four GA3 genotypes from five stratification genotypes. Poa restores the conditional 3 C / 10-week result, with flowering assessed after transfer to warm long days, and corrects the experimental factors to crossed. Neither record claims a general photoperiod-independent response. Poa remains abstract-only and partial.

The two added desk-audit paragraphs merge cleanly and remain intact: the 40-word rule and faithful-quotation requirements coexist with scientific-context/error counting. A narrow clarification in oa-read makes the documented exception explicit: a source-verified qualification may supplement the selected quote for the same finding, with a supporting passage identified and each remaining linter flag explained. It does not admit unrelated results, unsupported numbers or context inferred from inaccessible text. No validator or linter was relaxed.

The eight-record numeric-linter result remains **3 flagged, compared with 2 at baseline**:

| Record | Diagnostic | Disposition |
|---|---|---|
| Arbutus, desk-d68:1 | 300 absent from selected quote | Verified dose in the original reassessment's publisher abstract and full-text Methods; source location retained. |
| Poa, desk-d69:3 | 10 and 3 absent from selected quote | Verified duration and temperature in the publisher-deposited abstract, as documented in the reassessment; source location retained. |
| Lavandula, desk-d68:2 | 96.2, 10 and 25 absent from selected quote | Pre-existing and outside this targeted reassessment. Left unchanged and unresolved here; no scientific clearance is implied. |

These are manual, passage-specific dispositions, not an automated linter pass or a general waiver. No new source download or quotecheck against paper text was claimed in this integration; the completed investigations and independent review supply that provenance.

## Fresh integration validation

Validation used GitHub-fetched, commit-pinned files in a local validation snapshot. It did not use an old checkout or modify the research desk's working branches.

- `test_quote_limit.py`: four tests pass through the actual validator, addlog and checker CLIs, including 40/41 words.
- `test_apply_audit.py`: passes.
- `test_gaps.py`: five tests pass; existing resource-close warnings remain.
- `test_compile.py`: zero failed, with current-main specs and engine schema.
- Schema checks: two admitted quotation-recovery records, four held candidates, and eight desk-d68/d69 records; zero problems.
- `oa_lint.py`: two admitted Toxicodendron records pass; the targeted eight-record run has exactly the three diagnostics above.
- Validator AST matches current main; its only change is comments. Both main and integrated checkers report the same nine existing missing DOI/URL faults in intake-4-failed and intake-5-failed.
- Both corrected records reconstruct their current-main originals exactly by restoring `audit.was` and removing the new audit object. Original quotes, DOIs, grades, taxa, traits and unit identifiers remain; the other six evidence lines are byte-identical.
- Both desk-audit additions are retained exactly. The original investigations, reassessment, independent review and original audit reports are preserved. Patch whitespace checks pass.

The data-dependent `test_rows.py` and repository-wide evidence scan were not repeated in this focused integration; their prior results remain attributed to the original contributions. The fresh checks above are the validation claimed here. GitHub exposed no required checks or rulesets, and no CI check runs for the updated PR 42 head.

## Remaining questions and protected scope

Melilotus accepted name/rank is unresolved. Epacris and both Scilla observations remain held for permitted source-text retrieval and verification, including Scilla's possible degree/ordinal-character mismatch. Poa full-text questions, including an interaction test, remain beyond its abstract-only evidence. The unrelated Lavandula warning is unresolved here.

Historical audits and their counts, desk dispositions and queues, dispatch state, automations, source full texts, published coverage, and runtime code are untouched. No broader failure rate or automatic reinstatement of historical rejected evidence follows from these merges.
