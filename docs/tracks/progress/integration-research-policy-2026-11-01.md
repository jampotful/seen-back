# Research-policy integration review — 1 November 2026

The owner authorized review and integration of #45, #47 and #48 after #53,
without repeating completed scientific investigations or changing scientific
dispositions. The review began from accepted main
`46aeaadd78f2f84d0f194d83e734873f1680e143` (twelve desk commits after #53).
The local review snapshot reproduced its complete Git tree exactly:
`a85ea11284bec76110b9031e97483a399f88cab3`.

## Review and order

| PR | Inspected original head | Review conclusion |
|---|---|---|
| #45 | `0d0350ae69a832048445b7b8ab2538eb4c2e6a08` | Integrate first: one source-result reconciliation per paper and final-record receipts. Documentation completeness is not scientific correctness. |
| #47 | `22bc1cc088faa57b93fe39a3ed76a8d3dac3bb86` | Integrate second: light exposure, observational association and interpretation remain distinct; reuse #45's receipt. |
| #48 | `a15f253e26bf4ac6c280a54fff4546395674178d` | Integrate third: chemical reception, response, release and signalling remain distinct; retain provenance holds and isolate the withdrawal proposal. |

Each original head had successful evidence-intake CI and no submitted reviews
or unresolved review threads. All three already contained #53 and its conflict
resolutions. Those resolutions were reused. Their shared BRIEF, desk-screen,
oa-read, desk-audit and oa-audit changes combine cleanly with current main.
The owner-authorized integration review approves these policies, not their
candidate observations, proposed withdrawals or historical reinterpretations.
Fresh CI on each updated PR is required before its sequential merge.

## Integration adjustments

- #45's preflight suite now runs in the existing evidence-intake workflow.
  Three additional tests cover a shared receipt across all eight kinds, hash
  invalidation after classification/scope changes, and method-label/trait-kind
  separation. The original 13 tests and receipt validator remain intact.
- Preflight instructions explicitly require the existing strict and delta intake
  checks alongside receipts. Renew hashes after final classification or edits.
  A receipt cannot waive a missing kind; a kind cannot certify an interpretation.
- LIGHT-RESPONSE's three method-basis labels are not new evidence kinds.
  Physiological associations retain their qualifications; neural, behavioural
  and inferred claims retain their own endpoint limits. No classifier guesses
  a kind from method text.
- `physiology_volatile_emission` is a nonfunctional trait, not a ninth kind.
  Baseline emission does not become a stimulus response by choosing a kind.
  The existing eight-kind validator and functional-field scope are unchanged.
- The `oa-14:52` withdrawal proposal is preserved byte-for-byte at
  [proposals/recheck-oa-14-chemical.jsonl](proposals/recheck-oa-14-chemical.jsonl),
  outside operational evidence, audit and recheck directories. Its pending
  status and original commit/hash remain intact. Policy approval does not
  authorize applying it. The investigation's link and rollout wording reflect
  this separation.

The original investigations and calibration findings were reused. No scientific
source retrieval or independent re-investigation was performed during integration.
The light report's seven legacy cases still need targeted disposition. All 165
Danum candidates remain held; both provenance ledgers are byte-identical to #48.
No new chemical rendering feature or `chemical_signalling` migration is enabled.

## Combined verification

| Check | Result |
|---|---|
| Scientific preflight | 16 tests pass |
| Evidence scope | 15 tests pass |
| Ecological outcomes, including corpus | 10 tests pass |
| Intake | 16 tests pass |
| Audiogram compatibility, classification required | 8 tests pass |
| Quote limits | 4 tests pass |
| Extraction | 14 tests pass |
| Gap consumers | 5 tests pass |
| Audit application, compiler and mocked row consumer | Pass |
| Submission gate against the exact accepted-main tree | 0 changed evidence files; 0 problems |
| Ordinary validation of 477 evidence logs | Same 9 existing diagnostics: 6 in intake-4-failed and 3 in intake-5-failed |
| Whitespace and changed Markdown links | Pass |

There are 88 unit tests in the counted suites. The local accepted-main snapshot
commit is `cf8656338761078a50a7b149862418590a17b72a`; its complete tree equals
the remote accepted main above. No arbitrary candidate baseline was substituted.
Fresh GitHub CI supplies the actual remote base for each PR's submission gate.
Evidence, corrected logs, historical audits, source logs, recheck files, queue,
dispatcher and published outputs have no integration changes. Test-only audit
application and row generation ran in disposable directories with mocked APIs.
No live model request, app build or publication was performed.

## Repository integration versus desk adoption

The existing `evidence-kind-v2` policy remains in force; these PRs do not create
a replacement classification version or another dispatcher. Their merge commits
are the policy cutovers, visible in the PR timelines. A repository merge alone
does not prove that the continuously operating private launcher supplied the
new instructions.

The twelve available desk progress notes d302–d313 were checked for a positive
v2/intake-base/scientific-review receipt; none supplied one. Their recent eye
traits include keys exempt from the mandatory functional-field rule, so absent
kinds alone do not establish a classification violation or justify retroactive
typing. Private-launcher adoption remains unverified.

For the next fresh relevant evidence unit, the existing desk should record the
accepted-main SHA and actual prompt paths supplied: BRIEF, EVIDENCE-INTAKE,
scientific-preflight, the task prompt, and LIGHT-RESPONSE/CHEMICAL-EVIDENCE when
applicable. Verify its typed candidates, one reconciliation per paper, final
hashes, strict/delta/preflight results and independent disposition. Report the
first three fresh units' review overhead as specified by #45. Keep running
units on their pinned prompts and use the existing returning-unit admission
process. Do not interrupt, relaunch or duplicate them. No queue or automation
was edited, and no live research unit was launched by this integration.
