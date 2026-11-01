# Evidence classification integration — 1 November 2026

## Boundary and order

The owner requested integration of the existing implementations, without repeating
scientific investigations or admitting their candidates. Baseline accepted main:
`23f6092872305f6cc98b82f4c641216d95d782b0` (desk-d301 / audit 393).
All seven source PRs were open. The inspected heads were:

| PR | Head | Base at inspection |
|---|---|---|
| #49 | `d5552710fb4cfca16dd02f85c9512d709168e67a` | main |
| #51 | `0dba9556a3f61d3dbd9c74692e619c48e9a0e3d8` | #49 branch at d555271 |
| #52 | `bce567d9d31d73e800208c3a890480397c832b62` | #49 branch at d555271 |
| #50 | `ef1bac785f8f1db5e3aad2814c0b19ea4197a19d` | main |
| #45 | `20c1e721298ef375850521db9c8dee5b6462dffe` | main |
| #47 | `febbd8e4cec0ee42e5a1fb071b9ad9135f48dd3b` | main |
| #48 | `a05124e945a8f97f0687e76430a3c49c9be985e4` | main |

GitHub confirmed #51 run 41285318093 succeeded at its current head; its last
update was 07:34:43 UTC. That was not a combined-stack validation.

The tested implementation order is #49 foundation, #51 intake, then #52 outcome
extension. Deploy these together through the integration PR, so strict append
validation is never activated without authoring instructions, and the ecological
category is never activated without a compatible collector. Both siblings start
at #49; applying #52 on #51 preserves their common ancestor once. Main receives
code, instructions, conservative use restrictions, original investigation reports
and isolated test fixtures. It receives **no new accepted observation or applied
correction**. Do not merge the original scientific payloads solely because this
code passes. The policy version is `evidence-kind-v2`; its cutover is the actual
integration merge SHA, not a date or unit number.

## Reconciliation and review findings

The #49/#51/#52 patches applied without a textual conflict. Actual combined
review found a semantic defect: the #51 collector preserved only evidence kind
and anatomical fields, discarding all five ecological scope fields required by
#52. A mock-collection regression failed with zero candidates instead of one.
The fix preserves endpoint, experimental unit, intervention, comparator and
mechanism limit; incomplete ecological scope still fails validation. The test
now passes. Cached old batches remain readable without invented classifications.

Authoring instructions, extractor trait help and worked examples now cover all
eight kinds. Fresh-launch markers consistently use v2. Observational qualification
and causal strength remain separate from evidence kind; no method-string classifier
was added. The old lamp-catch screening leads are preserved, with a prospective
clarification that a catch table alone does not establish spectral sensitivity or
visually mediated behaviour. Running units retain their pinned instructions;
returning candidates receive source-based classification before admission.

The independent original investigations were reused, not repeated. Their reports
are preserved verbatim. Conservative fingerprint restrictions are use guards,
not retroactive scientific dispositions. All 14 original restricted findings
remain unchanged. Typed sensory writer inputs retain full neural curves, method,
conditions, source locator and late taxonomic qualifications. Ecological outcomes
cannot supply sensory gaps, generic sensory prose or measured/calculated engine
parameters, including mixed-citation attempts. Scoped outcome prose and controlled
behavioural/null findings remain available for their actual claims.

## Candidate isolation

- #49's four proposed anatomy records are copied byte-for-byte only to
  `tools/senses/fixtures/anatomy-d208.jsonl` (blob `47b068c4ef5979edbd91122b8397a70aacc4e1e6`).
- #50's eight audiograms and companion are copied only to test fixtures (blobs
  `1a7f23f22a16014301b980e990bc46dcaa711b4d` and
  `18c85866e2e55825e0f1b70dd71bf07894d2fe47`). The original eight compatibility
  tests are reused with fixture paths. No audiogram is added to accepted logs.
- #52's five proposed corrections are copied byte-for-byte only to
  `tools/senses/fixtures/recheck-ecological-350.jsonl`. No ledger is installed in
  recheck/accepted-audit paths by this integration. Audit-application tests use
  disposable directories; they do not apply the proposal to repository records.

No accepted evidence, corrected evidence, historical audit, disposition count,
source log, queue, dispatcher, automation, runtime source, published gap table or
live view is changed. `views/PARAMS.md` changes documentation only. Schema and
consumer eligibility remain distinct from the independent scientific admission
gate. The existing nine missing-source diagnostics in held intake files remain
unresolved, not waived.

## Fresh validation

On the combined implementation and current-main corpus:

| Check | Result |
|---|---|
| `tools/senses/test_evidence_scope.py` | 15 pass |
| `tools/senses/test_ecological_outcomes.py --corpus` | 10 pass, no skips |
| `tools/senses/test_intake.py` | 16 pass |
| `tools/senses/test_melotte_2018.py --require-classification` | 8 pass, no skips |
| `tools/senses/test_quote_limit.py` | 4 pass |
| `tools/lit/test_extract.py` | 14 pass, including reproduced/fixed field-loss defect |
| `tools/views/test_gaps.py` | 5 pass |
| `tools/views/test_apply_audit.py` | pass |
| `tools/views/test_compile.py` | 0 failures |
| `tools/views/test_rows.py` | pass against full current corpus and mocked API |
| Strict checks on isolated anatomy/audiogram fixtures | 4 + 8 records, 0 problems |
| Submission gate against accepted main | 0 changed evidence files, 0 problems |
| Ordinary checker on 465 current evidence logs | Same 9 diagnostics as baseline, all in intake-4-failed / intake-5-failed |
| Whitespace and fixture hashes | pass |

The 33 accepted d250–d254 records remain unchanged and ordinary-valid; 32 require
a kind if submitted anew. The mixed legacy/new tests exercise direct writes,
append atomicity, corrected copies, revised qualifications, duplicate multiplicity,
ecological required fields and actual #50 records. #50 keeps its six m/two g
pattern, 107 thresholds, neural-versus-behavioural limits and modern-species holds.
No live model request, paper retrieval, app build or publication was performed.
Existing ResourceWarnings were suppressed for readable local test output, not
fixed or treated as new failures. CI now runs the combined scope/intake/consumer
suite read-only, in addition to the PR-base delta gate.

## Other pending instruction PRs

A separate validation worktree applied #45, then #47, then #48 over the combined
classification tree. The five #47/#51 shared files are BRIEF, desk-screen, oa-read,
desk-audit and oa-audit. Three real conflicts were resolved while retaining both
independently valid instruction blocks:

| PR | Conflict | Resolution |
|---|---|---|
| #45 | `docs/tracks/prompts/desk-screen.md` | Keep authorized evidence intake and source-result preflight; neither authorizes evidence in screening-only work |
| #47 | `docs/tracks/prompts/oa-read.md` | Keep endpoint typing and the exposure/provenance distinction, observational qualification and shared receipt |
| #48 | `docs/views/research/BRIEF.md` | Keep both ecological and emission rows in the trait table, both scope paragraphs and the anatomy section |

The #45 preflight tests pass (13), and the combined pending-instruction tree
passes the intake and extractor suites. No competing receipt, duplicate source
review or scientific readmission was introduced. The pending branches should be
updated against the accepted integration using these resolutions; their individual
reviews and #48's provenance/disposition holds remain separate. This integration
PR does not merge their additional policies or scientific proposals.

## Remaining scientific and operational decisions

1. Independently dispose of #49's four anatomy candidates; their partial-source
   limits and audit-292 provenance still matter.
2. Independently audit #50's eight AEP records, especially the Piaractus and Myleus
   modern-identity restrictions. Preserve desk-d206:3 as the same experiment's
   aggregate, not independent replication.
3. Independently dispose of #52's five corrections, confirm fingerprints and apply
   approved replacements through the normal reversible audit process. Preserve
   raw evidence and historical decisions; never append refiles as replications.
4. Review #45/#47/#48 under the existing workflow. The 165 OA-14 identities and
   withdrawal proposal remain held; no source provenance was resolved here.
5. The desk records the actual cutover SHA and inventories running units in its
   existing system. Verify private-launcher adoption with the first fresh unit's
   v2/base receipt, typed submission, checks and independent disposition. Repository
   instructions and CI do not establish live adoption; no unit was interrupted.
