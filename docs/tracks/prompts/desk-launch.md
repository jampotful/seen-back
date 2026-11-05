# Existing desk: launch and submission provenance

This is the launch-recording procedure for the existing research desk, including
its private/ad-hoc launcher. It implements [EVIDENCE-INTAKE.md](../../views/research/EVIDENCE-INTAKE.md)
and [scientific-preflight.md](scientific-preflight.md); it does not create another
dispatcher, authorize new assignments, or change scientific admission rules.

## Before the next fresh evidence unit

In the existing desk queue/progress system, inventory units actually running,
their original launch times, checkout/base commits, and instruction versions.
Use the launch/session log as the source. Preserve unavailable fields as
`unknown`; a commit date, merge date or stale queue heading is not a launch time.
Do not restart, rebase, cancel or change the instructions/tools of a running unit.
Retain its original submission and audit commits. Review its returning candidates
under the existing integration procedure in a separate worktree.

For each fresh unit authorized to write evidence:

1. Fetch accepted main in the launch/integration checkout, without updating any
   running unit. Pin its full SHA as `intake_base` and the unit's actual checkout
   SHA separately. Verify that the base was accepted main, not a candidate
   commit or a baseline made from the candidate's records.
2. Actually supply BRIEF, EVIDENCE-INTAKE, EVIDENCE-ACCESS, scientific-preflight
   and the applicable task/reading prompt from that checkout. Include SENSORY-ANATOMY and
   ECOLOGICAL-OUTCOMES, plus LIGHT-RESPONSE/CHEMICAL-EVIDENCE when applicable.
   Record each supplied file's path and Git blob SHA. For a private prompt such
   as `rules.md`, record its version/content digest and a stable private log
   locator; do not publish credentials, paper text or private transcript dumps.
   Repository availability alone is not evidence of delivery. A private prompt
   must not silently replace accepted intake requirements.
3. At actual dispatch, append the receipt below to the unit's existing progress
   note. Record the actual UTC time, existing session/unit identifier or safe
   log locator, and supplied-prompt manifest. Have the unit acknowledge the
   received checkout and prompt versions in that note before drafting evidence.
   A prepared manifest without dispatch/acknowledgment remains `prepared`, not
   proof of adoption. If the exact launch text is private, retain it privately
   with its digest and locator; never invent an acknowledgment after the fact.

Use these fields in the usual `docs/tracks/progress/<unit>.md` note (or the
unit's already-established progress path), not a second queue:

```yaml
evidence_intake: evidence-kind-v2
evidence_access: evidence-access-v1
launch_status: prepared # change to acknowledged only on actual evidence
launched_at_utc: unknown
launch_record: unknown # existing session/unit/log locator; no secrets
intake_base: unknown # full accepted-main commit
checkout_commit: unknown # actual unit checkout
supplied_instructions:
  - path: docs/views/research/BRIEF.md
    git_blob: unknown
  - path: docs/views/research/EVIDENCE-ACCESS.md
    git_blob: unknown
  # Include every instruction actually supplied, including the task prompt.
private_instruction_versions: [] # private path/version or digest/log locator
received_acknowledgment: unknown # observed acknowledgment and timestamp/locator
```

The example is deliberately incomplete. Replace `unknown` only with observed
facts; an unavailable launch receipt remains an unresolved provenance question.
For a Git-tracked instruction, `git rev-parse <checkout_commit>:<path>` identifies
the available blob, but cannot by itself prove that the launcher supplied it.

## Before submission and after audit corrections

Use one source-result reconciliation per paper, at the existing
`docs/views/progress/<unit>-scientific-review.jsonl` path. Inspect the actual
endpoint/design when choosing `evidence_kind`; a previously accepted record's
kind or a successful schema check is not the scientific rationale. Preserve
nulls, limitations and source access. Reuse completed source work and independent
audits; do not commission another audit merely to populate a receipt.

Record the exact command, candidate commit/blob, base SHA where applicable,
exit status and summary for each distinct check in the existing progress note:

| Check | Required evidence |
|---|---|
| Strict new-input validation | `check.py --require-evidence-kind` on only the new/revised input; record count and problems |
| Baseline-aware submission | `check_submission.py --base-ref <intake_base>` on final files; unchanged/new counts and problems |
| Scientific preflight | `scientific_preflight.py <final-file> --review <review-file>`; one paper receipt covering final canonical hashes |
| Quotations | Existing `quotecheck.py` result and legal source-text provenance, or explicit retrieval hold |
| Independent disposition | Immutable audit commit/path and desk decision, including corrections and holds |

At integration, record `integration_base` as the then-current accepted-main SHA,
rerun ordinary validation and the baseline-aware gate on the actual corrected
submission, and rerun preflight where required by the unit's launch policy.
After any correction, deletion or reordering, check physical line references and
final-record hashes, reread changed claims and update the existing paper receipt.
Do not copy new hashes onto stale reconciliation. Preserve the original candidate
and audit commits and link both from the disposition. Keep audit reports on their
established branches when that is the workflow; an immutable link is sufficient.

Classify the conclusion explicitly:

- **Verified fresh adoption:** actual post-cutover launch/base/prompt delivery and
  acknowledgment, final typed candidates, current reconciliation hashes, strict,
  delta and preflight results, and independent disposition are all evidenced.
- **Documented running-unit transition:** original launch evidence establishes
  the old instructions; returning candidates still need current integration
  classification/delta checks. Unchanged accepted historical records retain
  their separate grandfathering. Neither case authorizes blanket exemptions.
- **Unresolved provenance:** launch/delivery or required checks cannot be
  established. Do not label this a skipped check or invent a historical receipt.
  Preserve accepted observations and audit history. For a fresh unaccepted
  submission, resolve the missing required evidence before admission without
  stopping unrelated work or relaunching its research.

For the first three verified fresh units, retain the existing overhead report:
review minutes (or `not measured`), extra source calls and resulting holds.
An instruction merge or CI pass is not a live-launcher adoption receipt.
