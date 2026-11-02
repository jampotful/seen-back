# Research-desk intake adoption investigation — 2 November 2026

## Finding and limits

**Partial classification adoption is evidenced; full live-launcher adoption is
not verified.** The original d325 and d326 candidate commits both have accepted
main `f7fda79502c5270b52e3e4cc04916832a9d9e268` as their sole parent. That commit
was made at 2026-11-02 01:25:02 UTC and contains all four policy integrations.
Both original candidates were already typed; this was not just a merge-time
addition. Audit 436 records an actual strict check of d325's nine candidates.

This establishes a post-cutover submitted checkout, **not an exact launch time
or delivered private instruction version**. Git ancestry cannot exclude an
older launch whose checkout was subsequently moved. No such move or legitimate
old-launch exception is established by the inspected evidence. Neither an
automatic grandfathering verdict nor a proven failure to supply instructions is
justified. All accepted observations and historical audit decisions are preserved.

A concrete repository-recording gap is established: neither original nor final
progress note records `intake_base`, `evidence_intake`, actual launch timestamp,
prompt manifest/delivery acknowledgment, baseline-aware result or scientific
preflight receipt. No `*-scientific-review.jsonl` exists in either original
candidate tree or the inspected accepted-main snapshot. Private copies or logs
may exist; they have not been obtained. Independent audits are substantive source
review, but do not substitute for the required author reconciliation and final
record binding when the fresh-launch policy applies.

Repository inspection is pinned to accepted main
`f6a49f8ac7d5199e04d3e5a2c2bffe28ad346998` (2026-11-02 12:38:08 UTC), not a
claim about later desk work. The original candidate/audit refs were recovered
through GitHub. The private Claude Code session named in their commit trailers
requires sign-in in the available browser, so its actual dispatch messages,
private `rules.md`, unit starts and command logs remain unavailable. A targeted
check of the connected Mac did not locate a Regards checkout or matching Claude
project; no process or runtime configuration was changed.

## Cutovers and recovered provenance

| Policy | Accepted merge | UTC time, 1 November 2026 |
|---|---|---|
| [#53](https://github.com/jampotful/seen-back/pull/53), evidence-kind-v2 | `0c6d4f2dbc3344de76bc8ff0f07c648644a9e80b` | 15:33:50 |
| [#45](https://github.com/jampotful/seen-back/pull/45), scientific preflight | `c831c188a61f2080005303648869b9af0decd098` | 21:37:08 |
| [#47](https://github.com/jampotful/seen-back/pull/47), light response | `e427d00a8e799e93e68394b43335eca612706da9` | 21:38:00 |
| [#48](https://github.com/jampotful/seen-back/pull/48), chemical evidence | `12a26b88b9fb2fc0d9c738d4c7147018dddcd4a9` | 21:38:52 |

| Unit | Original candidate | Candidate commit UTC, 2 November | Accepted integration | Integration UTC |
|---|---|---|---|---|
| d325 | [ea81acbd](https://github.com/jampotful/seen-back/commit/ea81acbd1d3e0efa43fce6f24acbeead095d3c05) | 01:35:02 | [b9b3c824](https://github.com/jampotful/seen-back/commit/b9b3c824b36232b78624b6d7ec515589276b7a67) | 01:42:30 |
| d326 | [3024326a](https://github.com/jampotful/seen-back/commit/3024326af803ad90506b064d5774c827a237f42f) | 01:48:14 | [6dd1541c](https://github.com/jampotful/seen-back/commit/6dd1541c15a6a26cb50425ec90c682178d410d5b) | 01:54:20 |

These are commit times, **not launch times**. Both candidates' sole parent is
`f7fda79502c5270b52e3e4cc04916832a9d9e268`. The accepted d325 integration's
parent is also f7fda795; d326's integration parent is b9b3c824. The latter is an
integration base, not d326's original candidate base. All are on accepted main's
history; the #48 cutover is an ancestor of f7fda795.

The independent audits remain available on their original branches, even though
main contains only the desk's disposition summaries:

- [Audit 436](https://github.com/jampotful/seen-back/blob/746da5d31e2326934daeaba3f9a52386f37b512e/docs/tracks/progress/audit-436.md): d325 original lines 1–5; two errors, one fixable and one held out. Explicit `--require-evidence-kind`: 9 records, 0 problems. Its report identifies HEAD/origin-main as f7fda795.
- [Audit 437](https://github.com/jampotful/seen-back/blob/4d8362422506280080c34b58a1ad551986f75567/docs/tracks/progress/audit-437.md): d325 lines 6–9; two fixable errors, taxonomy and scan coverage. Ordinary check: 9 records, 0 problems.
- [Audit 438](https://github.com/jampotful/seen-back/blob/e3ed3df8a8d1286731ab71ef63a58977edcefda3/docs/tracks/progress/audit-438.md): d326, two records; three fixable errors covering pseudoreplication/regression basis, a dropped quote qualifier, and specimen/site details. Ordinary check: 2 records, 0 problems. Its parent is b9b3c824.

The final records include the required audit corrections and preserve the
omitted d325 finding as a lead in the progress note. The reports refer to private
`rules.md`; its actual version/content cannot be recovered from these Git trees.
No audit has been rewritten or moved, and no scientific retrieval was repeated.

## Instruction versions available, not proven supplied

Both original candidate commits change only their evidence and progress files.
The following versions were therefore available in both candidate checkouts.
This is a version inventory, **not a delivery receipt**; the applicable private
launch/task prompt remains unknown.

| Path | Git blob at candidate base |
|---|---|
| `docs/views/research/BRIEF.md` | `c828a6f3282b7f76d4470509879095567b745e12` |
| `docs/views/research/EVIDENCE-INTAKE.md` | `8d65ec4dff9fcda3582243e054ee60da89a3c5fd` |
| `docs/tracks/prompts/scientific-preflight.md` | `91c8363a120b1053da020a9e6441adbbf112c804` |
| `docs/tracks/prompts/desk-screen.md` | `914e74f0fa02c07e31cbe426b92688c0fe1739c6` |
| `docs/tracks/prompts/oa-read.md` | `0660d352c8a87fab22c1d2a6e7f649d35123fb61` |
| `docs/views/research/LIGHT-RESPONSE.md` | `096ebe4026d17cd5ecc0fb54572c91f1c4403879` |
| `docs/views/research/CHEMICAL-EVIDENCE.md` | `f26dd896ff206bd12c8dcf3038b25b65db118393` |

## Checks and source reconciliation

The read-only checks below were performed during this investigation on
2 November. They are **new diagnostic results**, not reconstructed historical
execution receipts or proof that the desk ran them before admission.

| Check | Result |
|---|---|
| Strict check, original d325 | 9 records; 0 problems |
| Strict check, original d326 | 2 records; 0 problems |
| Strict check, accepted d325 | 8 records; 0 problems |
| Strict check, accepted d326 | 2 records; 0 problems |
| Final delta against f7fda795, both files | 0 unchanged legacy; 10 new/changed; 0 problems |
| Final d326 delta against integration parent b9b3c824 | 0 unchanged legacy; 2 new/changed; 0 problems |
| Scientific preflight and matching final hashes | Not verifiable: required review files absent from inspected trees; private receipts unknown |
| Historical quotecheck executions | No command receipt established by inspected progress/audit records; audits describe their own source comparisons |

Commands for the final checks:

```sh
python3 -I tools/senses/check.py --require-evidence-kind docs/views/evidence/desk-d325.jsonl docs/views/evidence/desk-d326.jsonl
python3 -I tools/senses/check_submission.py --base-ref f7fda79502c5270b52e3e4cc04916832a9d9e268 docs/views/evidence/desk-d325.jsonl docs/views/evidence/desk-d326.jsonl
python3 -I tools/senses/check_submission.py --base-ref b9b3c824b36232b78624b6d7ec515589276b7a67 docs/views/evidence/desk-d326.jsonl
```

The accepted ten records comprise four `physiological_response`, three
`anatomical_measurement` and three `anatomical_presence` classifications. The
original eleven included one further `physiological_response` record, dropped
by audit 436. Counts establish schema presence, not scientific correctness.

The existing audits inspect Methods/Results and recover important limitations,
including d326's regression estimate, unknown individual count, pseudoreplication
and shrew provenance. They provide useful independent reconciliation evidence.
However, there is no author paper-receipt set covering the final files. Audit 438
also justifies the echolocation kind by matching earlier accepted records; that
alone is not the required endpoint/control rationale. Its accepted record calls
the value baseline call structure. The existing desk should resolve that narrow
classification rationale from its already-inspected sources if a further review
is needed; this investigation neither reclassifies it nor invalidates its
measured observation. The non-detection question already raised in audit 437 is
also retained without inventing a new kind.

## Inspection fingerprints (not scientific-review receipts)

Accepted evidence blobs: d325 `4c41ff7bc3e57e5dcfbd18ed25a5ef66e98da665`;
d326 `a82f899d6ecbe9314b792308c88e3d25e8088e3a`. They match the original accepted
integration blobs. Canonical JSON SHA-256 values below use the preflight
validator's serialization. No review exists here against which to validate them;
computing a digest does not establish a final claim check.

| Final physical line | Canonical SHA-256 |
|---|---|
| desk-d325:1 | `6f03721db0e1169d969f59d4edcf72d21938dc3421dcc210fc871f816670533b` |
| desk-d325:2 | `413452daf6bdc9a77b638901c552d6bb8742c0017ae28479a4fdae1c56953c62` |
| desk-d325:3 | `d6c7e5be69fef7dbb01a95c3825658be81c3216c5156e0ce077d80bd046e3cda` |
| desk-d325:4 | `b6bd517e8923b3e80bbd24540cefccb6c72e17756c37efaf1fb79857b23ab5c9` |
| desk-d325:5 | `b0295d9c70739242b0d5b1b961a939a664c843bd6103d831ef9cfe602b7c2612` |
| desk-d325:6 | `245f249dfef4aa5dac8034d102a68f7230d8f8e22c3c9c82bc119b1831c8a435` |
| desk-d325:7 | `ebaca837bf823f982e778840e116d3d402dead1e4d0da45447b027c5b53e3b38` |
| desk-d325:8 | `7520302f1803ecfb545ab13293ab0ec2bb9229316877d2707fb17d588f86f4f2` |
| desk-d326:1 | `e34b0beb93c5df5d7119ab47726bf12923cf78d78cf816f8ee853a19a015c0c5` |
| desk-d326:2 | `6a08143eee603fae5d6dbd15c930dd2a23e9de248e69049413b424a414979fef` |

## Focused repair and remaining acceptance condition

The change adds [desk-launch.md](../prompts/desk-launch.md) and links it from the
existing desk queue's check-in instructions and EVIDENCE-INTAKE. It makes actual
launch time, accepted-main/checkout distinction, supplied Git/private prompt
versions, acknowledgment, separate check results, corrected-file hashes and
immutable audit links explicit in the existing progress note. It also states
how to record an unresolved launch without inventing a failure or grandfathering.
It does not add a scheduler, change queue assignments, touch the Codex dispatcher,
restart units, generate historical source reviews or edit accepted observations.

This repairs repository launch/provenance instructions. It **does not certify
private-launcher activation**. Completion requires the existing desk's actual
session/launch logs:

1. Recover d325/d326 dispatch times, original checkout/base and exact supplied
   instructions (including private rules), plus any preflight/delta/quotecheck
   command logs and final reconciliation receipts. Record a late recovery as
   such, with its source; do not backdate it.
2. If an original pre-cutover launch is documented, record the legitimate
   running-unit transition and its current integration checks. If a fresh
   post-cutover launch is documented without the required supply/receipts,
   record the adoption failure and correct the existing private launcher for
   subsequent launches. Preserve already accepted science and audit history.
3. Observe one demonstrably fresh post-cutover unit through actual dispatch,
   acknowledgment, final typed submission, source-result reconciliation, final
   hashes, strict/delta/preflight results and independent disposition. Track the
   first three fresh units' existing review-overhead measures.

A merge of this repair, successful repository checks, recent commit timestamp
or continued throughput must not be reported as completion of step 3.
