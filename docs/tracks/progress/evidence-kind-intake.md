# Scientific evidence intake and PR #49

1 November 2026. Implementation companion on `codex/evidence-kind-intake`,
stacked on #49 at `d5552710fb4cfca16dd02f85c9512d709168e67a`. Current-main
inspection pinned to `832884366160e258cbc7b3c30e61e807927b4e7d`; main had already
reached desk-d272/audit 365. The five batches in the request are a compatibility
sample, not a cutoff for a continuously moving desk.

## Findings and writing paths

| Path | Observed role | Change / intake boundary |
|---|---|---|
| `tools/senses/addlog.py` | Explicit append command in BRIEF, oa-read, oa-pass, external-sweep and round3-sweep; validates all incoming lines before appending | Keep #49's strict functional-field requirement; document kind selection and mixed old/new destinations |
| `docs/tracks/prompts/oa-read.md`, `oa-pass.md` | OA reader instructions, source access, quotation and submission checks | Add the shared policy, launch/base receipt, strict new-input and baseline-aware final check |
| `tools/views/codex_queue.py` -> `codex-round.md` -> task prompts | Printed assignments; harvest-c explicitly overrides search-only screening to permit evidence through addlog | Printed assignments now carry policy/version/base/check instruction; coordinator validates final submissions |
| `desk-screen.md`, external/harvest/sweep and intake/filing prompts | Search handoff and other authoring routes; the standing desk-screen prompt itself forbids evidence unless a launch overrides it | Link policy at the writing handoff without widening search-only assignments |
| Direct JSONL authoring / scratch builders | The schema can be bypassed by writing files directly; historical `ev.py` builds a record without a kind and then calls addlog in hard-coded `/tmp/ws8` | Final submission gate covers new/changed rows regardless of writer; old scratch helpers are not a supported new-record template |
| `tools/lit/extract.py` | Upstream model extraction, `finish_record` whitelists fields, collection writes candidate tables using ordinary validation | Request kinds and preserve supplied kind/structure/measurement. Old cached batches remain collectable; intake must classify candidates before admission |
| `tools/views/apply_audit.py` | Writes corrected copies, using replacement records and preserving audit provenance | Do not rewrite historical audit machinery; audit instructions require kind/context in new replacement records and final delta validation |
| `oa-audit.md`, `desk-audit.md` | Independent scientific disposition, corrections, counting | Review endpoint/kind fit; structural success cannot substitute for source review |
| `ci/oa/oa.py`, `.github/workflows/oa.yml` | Fetch and encrypt legal source text, not evidence authoring or desk launching | No change |

Searched repository prompts and senses/view/literature Python tools for writing
paths; read the relevant writers, small root helper scripts, AGENTS, HANDOFF,
CONTRACTS, LOG, STATUS, the desk queue and CODEX-DISPATCH, plus the five accepted
logs and their progress reports.
Those reports show `check.py 0 problems` and audit dispositions 345–350, but do
not retain the exact d250–d254 writer commands or live launch prompts. No claim
is made that every desk unit used addlog, or that a hidden launcher was updated.
The active private Claude launch session is outside the retrieved repository
sources. Printed Codex queue instructions are a verified repository path, not
proof that the private desk uses that queue.

## Delivered policy and gate

[EVIDENCE-INTAKE.md](../../views/research/EVIDENCE-INTAKE.md) defines endpoint-based
kind selection, synthetic worked examples, strict append/pre-commit checks,
direct-write coverage, grandfathering, and a non-interrupting transition.
`check_submission.py --base-ref <accepted-main-sha>` compares complete records
with multiplicity in the same file. New/changed functional records need kinds;
unchanged accepted records retain ordinary validation. The script does not guess
a classification, alter a record, or decide scientific admission. A changed note,
qualification or extra duplicate is not hidden behind an old unit/filename.

The PR workflow runs offline checks and the gate against the PR's base SHA, with
read-only permissions, no API-funded generation and no automatic merge. The
manual gate remains necessary for the desk's branch-integration workflow. No
branch-protection requirement is asserted or installed.

## The 33-record replay and grandfathering decision

| Accepted log | Records | Functional under #49 | Ordinary problems | Missing kinds if submitted anew |
|---|---:|---:|---:|---:|
| desk-d250 | 7 | 7 | 0 | 7 |
| desk-d251 | 6 | 6 | 0 | 6 |
| desk-d252 | 4 | 4 | 0 | 4 |
| desk-d253 | 9 | 8 | 0 | 8 |
| desk-d254 | 7 | 7 | 0 | 7 |
| Total | 33 | 32 | 0 | 32 |

[Record inventory](evidence-intake-recent.csv) identifies every accepted physical
line, taxon/trait, source snapshot, content hash and review focus. All 33 remain
unchanged and grandfathered for field presence. The exception to the mandatory
functional-field rule is `desk-d253:4`, *Ephoron virgo*, `polarization`; this says
nothing about the scientific strength of that finding. No mass classification
or source-verification claim is made for these records.

Three scratch-only typed copies exercise realistic schema compatibility:
`desk-d250:1` and `desk-d252:2` with `behavioural_response`, `desk-d251:6` with
`transduction`. Their original values, quotations, conditions, grades and
provenance survive append unchanged. These are record-based format replays,
not primary-source audits or proposed amendments to accepted data. All other
classifications wait for independent review. In particular, `desk-d254:2`
measures green-turtle net bycatch, not independently observed visual avoidance;
the new guidance requires resolving that endpoint/claim fit instead of applying
`behavioural_response` or `inferred_function` as a convenient default.

The test manifest pins the five accepted blobs and commit. A full-history clone
can retrieve them from that immutable commit even if later independent work
changes a live log, or if the stacked #49 branch predates these batches. No
duplicate accepted-evidence fixture is committed.

## Validation

- `python3 -I tools/senses/test_intake.py`: 14 tests pass. Seven synthetic kind
  examples append and strict-check; mixed batches reject before writing; typed
  append preserves old bytes; direct writes, modified qualifications, duplicates,
  untracked/corrected outputs, bad bases/paths, malformed JSON/fields and the
  precise mandatory trait boundary are covered. Actual 33-record replay passes.
- `test_quote_limit.py`: four tests pass, retaining the 40-word rule and atomic
  rejection from #49.
- `tools/lit/test_extract.py`: 13 tests pass, including scope-field preservation,
  old cached-record compatibility and rejection of an invalid kind rather than
  silently stripping it into a legacy pass. Existing file/socket ResourceWarnings
  remain; these are not test failures.
- `tools/views/test_apply_audit.py`: passes, preserving historical correction
  behavior. No audit script or accepted log was changed.
- Combined with #50 at `ef1bac785f8f1db5e3aad2814c0b19ea4197a19d`,
  `test_melotte_2018.py --require-classification`: eight tests pass, no skips.
  Its 107 thresholds, eight records, grades, restrictions, neural-vs-behavioural
  scope, full writer context and unaudited state are retained.
- `git diff --check` passes. No whole-corpus scientific audit, live launcher
  adoption, API generation, app build, published view/gap regeneration or new
  scientific admission is claimed.

## Integration handoff

Review/apply this companion with #49, through the established research-desk
review and app-thread integration process (HANDOFF; CODEX-DISPATCH). The stacked
PR targets #49's branch so the intake diff stays separate from its ontology and
proposed anatomy records. If #49 lands first, retarget this companion to main
and recheck the combined tree; otherwise apply both after review. This branch
does not merge #49's proposed evidence into accepted main.

#50 remains a separate submission: its eight typed AEP records still need the
independent scientific disposition, including the two identity restrictions.
No #50 file is part of this companion's changes. If #45's source-result receipt
work is applied too, use the same receipt and refresh its hashes after typing;
these instructions add no competing scientific-review form.

Before cutover the desk records actual running unit/base commits in its existing
progress system. They finish their pinned old tools/prompts; the desk classifies
their returning new functional records in an integration worktree, preserves
original commits/audits, and holds unresolved claims rather than relaunching work.
Fresh units receive evidence-kind-v1 plus the real accepted-main base SHA. The
first such unit must provide a launch/version receipt, typed records, strict and
delta-check output, and an independent disposition to demonstrate adoption.
This task neither changes the dispatcher/queue nor invents those operational
receipts. Accepted records accumulating on main before cutover remain legacy;
the integration reviewer must refresh main and rerun the gate.
