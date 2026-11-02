# Evidence-kind intake, version 2

Combined policy for PRs #49, #51 and #52. Activate the classification implementation,
ecological scope and these instructions together. Schema checks do not admit
evidence: independent source review and the existing audit disposition still do.

## Choose the kind of the finding

Read [SENSORY-ANATOMY.md](SENSORY-ANATOMY.md), including its eight allowed kinds,
and [ECOLOGICAL-OUTCOMES.md](ECOLOGICAL-OUTCOMES.md).
Every newly authored or scientifically revised `sense_*` or `behaviour_vision`
record must have `evidence_kind`. Choose from the actual endpoint and controls,
not the trait name, a method keyword, taxonomic grade, or the paper's general topic.
`sensory_anatomy` always needs its anatomical kind, structure, measurement,
method and conditions (and units for quantities). Other existing visual traits
are outside #49's mandatory functional-field rule; do not relabel them just to
make a count uniform. Optional kinds must still be valid.

| Observed endpoint | Kind to consider after reading the source | Required limit |
|---|---|---|
| Named organ observed / counted | `anatomical_presence` / `anatomical_measurement` | Use an existing precise anatomy trait or `sensory_anatomy`; no inferred modality |
| Passive hair displacement or resonance | `mechanical_response` | No neural or behavioural sensitivity established |
| Stimulus-locked receptor/nerve potential, AEP, EAG | `transduction` | Neural/receptor response; no behavioural threshold or specific molecular mechanism implied |
| Germination, growth or another physiological endpoint in a specified stimulus comparison | `physiological_response` | Retain treatment, controls or observational qualifications, and endpoint; do not invent receptor identity or causation |
| Choice, movement, discrimination, avoidance or their tested null | `behavioural_response` | Retain stimulus, controls and alternatives; null is protocol-specific |
| Source-attributed functional hypothesis/model | `inferred_function` | Keep explicitly inferred; no measured functional coverage |
| Catch, survey encounter rate or another ecological endpoint under an intervention | `ecological_outcome` | Use `ecological_intervention_outcome`; retain endpoint, experimental unit, intervention, comparator and mechanism limit; no sensory coverage or calibration |

Split different measured endpoints from the same paper. A trap count, encounter
rate, bycatch reduction or abundance change is not automatically an individual's
sensory response. If a source only measures an intervention outcome, preserve that
outcome as `ecological_intervention_outcome` / `ecological_outcome` and hold its
sensory interpretation for review. This category always requires `measured_endpoint`,
`experimental_unit`, `intervention`, `comparator`, `mechanism_limit`, `method`,
`conditions` and `units`. Do not label the measured
outcome `inferred_function` merely to pass validation: only an explicitly
attributed functional hypothesis belongs there. Use the established ecological
category when it fits; other new traits follow BRIEF's new-trait rule, with their
scientific basis reviewed before admission. Do not invent a category such
as `unknown` or copy one kind across a batch.

Evidence kind does not replace trait eligibility or establish causal strength.
Where the applicable trait policy admits an observational association, preserve
that qualification and its actual exposure comparison; a physiological kind
does not turn it into a controlled experiment. A measured emission remains
distinct from a chemical response. Reuse the existing source reconciliation
when applying the pending light/chemical clarifications; do not add a second
receipt or repeat a completed investigation.

Put a short classification rationale and the relevant source location in the
existing `note` / `where` fields. Retain the measured value, exact quote, method,
conditions, nulls, source access, grade, `partial`, identity restrictions and
provenance. If #45's source-result reconciliation is present, put the reasoning
there too and refresh its final-record hashes after classification; no second
receipt or replacement audit is required.

## Write and submit

At a fresh unit's launch, record `evidence_intake: evidence-kind-v2` and the
full accepted `origin/main` SHA as `intake_base` in its existing progress note.
The launcher must actually supply this policy, BRIEF and the task prompt. An
updated file on GitHub alone is not proof that a private/ad-hoc launcher read it.
Use the existing desk's [launch-recording procedure](../../tracks/prompts/desk-launch.md)
for the actual timestamp, dispatch/acknowledgment locator and supplied instruction
blob versions, and link final validation and audit evidence in the same progress
note. A candidate's Git parent establishes its submitted base, not its launch time
or the contents of a private prompt. Missing historical provenance stays unknown.

1. Draft the new records in a scratch JSONL file, using the worked examples in
   [evidence-intake-examples.json](evidence-intake-examples.json) as format-only
   examples. They are synthetic and must never be filed as research.
2. Run `python3 -I tools/senses/check.py --require-evidence-kind /tmp/new-records.jsonl`.
   Then check quotations against legally obtained source text with `quotecheck.py`
   and perform the existing scientific checks. Resolve an uncertain classification
   by source review or hold it; never guess a kind to silence the validator.
3. Append with `python3 -I tools/senses/addlog.py <unit> < /tmp/new-records.jsonl`.
   It validates the entire input before writing. It checks only incoming records,
   so old untyped lines already in the destination can remain unchanged.
4. Before committing, run
   `python3 -I tools/senses/check_submission.py --base-ref <intake_base> docs/views/evidence/<unit>.jsonl`.
   This also covers directly written JSONL, re-used logs and audit-generated
   corrected copies. Omit paths to inspect all changed/untracked evidence and
   corrected logs. It is read-only. Supply an accepted-main commit, never the
   candidate's own commit or a baseline manufactured from its records.
5. Report base SHA, files, unchanged/new counts, checks and classification holds
   in the existing unit progress note. Follow the task's branch/PR convention.

`check.py` without `--require-evidence-kind` remains ordinary validation for
historical records. Strict-check a **new-record file**, not the whole historical
corpus. The submission gate compares complete JSON records in the same file,
including notes and provenance, with multiplicity: changed or extra duplicate
records are new; whitespace, key-order and line-order changes alone are not.
This gate establishes schema scope, not claim correctness or duplicate eligibility.

The read-only `evidence-intake` PR workflow runs the offline tests and this gate
against the PR's base SHA. It has no write permission or merge action. The desk
must still run the gate when integrating branches outside the PR mechanism.
Repository checks are not claimed to be required branch-protection rules.

## Desk review and rollout

- Apply the combined #49/#51/#52 code and instructions together. Record the actual
  integration SHA as the cutover;
  neither 1 November nor desk-d254 is a universal cutoff. #50's eight audiograms
  remain a separately audited submission, already typed `transduction`.
- Before the next launch, inventory running unit branches and their launch/base
  commits in the desk's existing progress/queue system. Do not restart, rebase,
  cancel or replace a running unit's instructions/tools. Let it finish in its
  pinned old checkout and report the old schema. If it has already updated and
  addlog rejects an untyped input, retain the candidate in scratch/its permitted
  draft, and send it for classification; do not bypass addlog or discard it.
- Review returning old-format candidates in a separate integration worktree.
  The desk classifies new functional records from their sources, recording the
  rationale/correction and preserving the original submission commit and audit.
  If the endpoint or source cannot support a kind, hold that claim for review.
  Execution continues; admission waits on unresolved classification. There is no
  blanket exemption for a branch name, old unit name or old timestamp.
- At integration, rerun ordinary validation and the submission gate against the
  then-current accepted-main SHA. Independently inspect each new kind alongside
  the finding's source/design. Recheck after corrections, including output from
  `apply_audit.py`; a correction's replacement record must retain the approved
  kind and qualifications. Historical correction replay remains possible under
  ordinary validation; this does not authorize it as a new functional submission.
- Unchanged records already in accepted main are grandfathered for field
  presence, including desk-d250–d254. Do not bulk type them from method strings.
  Reclassification/re-filing follows independent source review and the existing
  correction/provenance process. Grandfathering does not affirm sensory function.
- Verify adoption from the first fresh unit's actual launch/base receipt, typed
  submission, strict/delta-check results and independent desk disposition. A PR
  or successful test alone is not a live-launcher adoption receipt.

The literature table extractor is an upstream candidate producer. New prompts
request kinds and preserve them when collecting replies. Its ordinary collection
mode remains compatible with already-running/cached batches; table records are
still unverified candidates. Before a table candidate becomes a new accepted
functional evidence record it must pass the same strict intake and source audit.
