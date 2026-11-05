# Access-policy reconciliation: Ephoron, Echinacea and PR #46

2 November 2026. Accepted-main baseline: `074589ee524b1d243b2371c765715f81be9215f7`.
This updates PR #46 through the existing Codex findings lane. The original
30 October investigation remains available at [commit f00ca5b1](https://github.com/jampotful/seen-back/blob/f00ca5b1df8369633ac71483a26479165193ec75/docs/tracks/progress/reassessment-236-pmc.md).

## Decision and scope

**The blanket requirement for an open-reuse licence is inconsistent with the
accepted PMC precedent and the written free-copy routes.** Missing CC alone does
not justify rejecting a source that can legitimately be read. The original
CORE/REAL copy still requires its own provenance/version/route assessment; a
PMC record cannot retroactively establish those facts for another copy.

**All six Ephoron candidates remain held.** Audit 236 identified material
scientific-context errors independently of its licence objection. This change
clarifies prospective access decisions; it creates no evidence, source-completion
receipt, rendering parameter or automatic refile. Accepted numerical observations,
audit reports/counts and desk-d151's zero-yield disposition remain unchanged.

[EVIDENCE-ACCESS.md](../../views/research/EVIDENCE-ACCESS.md) is the proposed shared
rule. BRIEF, intake, reader/auditor prompts, scientific preflight and the existing
launch manifest now point to it. It becomes operational through the desk's normal
branch review/integration and actual prompt delivery at a fresh launch. No live
launcher, running unit, queue or automation is changed here.

## Case comparison

| Question | Ephoron: original CORE/REAL copy | Ephoron: PMC9043733 | Echinacea: PMC1646994 |
|---|---|---|---|
| Copy and route | Audit 236 opened a CORE PDF and REAL item 141896. The PDF describes an author-made version adjusted to the published paper. CORE harvesting REAL was explicitly an inference. | PR #46 identified the matching official archive record. Its October metadata had `authMan: N` and `isOpenAccess: N`; neither proves the displayed version or reuse permission. | Audit 195 read a PMC author manuscript, NIHMS11809, publicly available from 17 November 2006. |
| Rights actually evidenced | Audit 236 found no licence on the copy/item or an article-reuse licence in Crossref; it called the deposit lawful-looking. This session did not retrieve that exact item/file. | This session's indexed PMC result displays © 2022 The Author(s), followed by “Published by the Royal Society. All rights reserved.” Direct opening returned a challenge, so this is indexed corroboration, not a newly inspected live panel or complete source read. | Audit 195 explicitly recorded no open licence in PMC or Crossref. This session's indexed PMC result corroborates the author-manuscript identity; a direct opening returned a challenge. No new licence is asserted. |
| Scientific disposition | Six licence errors, with six additional fixable scientific-meaning faults, counted once per record. | Existence/metadata cannot verify the six peaks, their context or the corrections. | Only the missing DOI was counted. Audit 195 authorized refile after adding it; desk-d105 merged with DOI `10.21273/hortsci.40.6.1751`. |
| Access conclusion | A missing CC statement is insufficient grounds for exclusion. Verify this specific deposit and permitted retrieval method before using it. | Eligible official-archive route for a new source read subject to the actual terms and scientific checks; no open-reuse claim. | Accepted non-CC PMC precedent. It establishes previous access treatment, not universal scientific validation or permission to republish. |

Copy locators: [REAL item 141896](https://real.mtak.hu/141896/),
[Ephoron PMC9043733](https://pmc.ncbi.nlm.nih.gov/articles/PMC9043733/), and
[Echinacea PMC1646994](https://pmc.ncbi.nlm.nih.gov/articles/PMC1646994/).

Repository evidence: [audit 236](audit-236.md), [desk-d151](desk-d151.md),
[audit 195](audit-195.md), [desk-d105 disposition](desk-d105.md), and the
[accepted record](../../views/evidence/desk-d105.jsonl). The accepted record still
has `access: open`, `partial: true` and WebFetch-summary provenance. Audit 195
noted limitations in the access/partial/unit wording; this policy investigation
neither endorses every field nor edits that historical observation.

## Why the earlier distinction does not settle the question

[oa-pass.md](../prompts/oa-pass.md) expressly included PMC, Europe PMC and
institutional repositories among free-copy routes. BRIEF used the ambiguous
phrase “Open access only” while also allowing specific owner-supplied papers.
The schema had only `open`, `abstract`, `closed` and `book`; it had no separate
free-to-read-with-restricted-reuse value.

[Audit 178](audit-178.md) held an unverified repository PDF while admitting
abstract-derived observations. That is a defensible provenance hold, but does
not establish that CC is necessary. [Audit 194](audit-194.md) verified CC BY on
an NSF PAR copy; that establishes one sufficient route. [Audit 223](audit-223.md)
then stated a general repository-licence requirement, cited audit 195's label
concern, but did not reconcile its explicit refile permission and actual merge.
Audit 223 also called the non-CC PMC Gyrostemon hold cautious rather than required.
The later blanket formulation therefore was not applied consistently even in
that audit. Audit 236 followed it, while independently finding scientific errors.

The hosts are different and justify different provenance checks. They do not
justify equating the absence of an open-reuse licence with prohibited reading.
The six-record hold remains scientifically justified. Its licence-only rationale
needs a prospective replacement rather than deletion of the historical audit.

## External policy checks and retrieval limits

Sources consulted on 2 November:

- [PMC Copyright Notice](https://pmc.ncbi.nlm.nih.gov/about/copyright/) distinguishes
  free access from open reuse, treats unstated rights as standard copyright,
  describes author-manuscript reading and fair-use possibilities, and restricts
  systematic downloading. [Author-manuscript guidance](https://pmc.ncbi.nlm.nih.gov/about/authorms/)
  explains the deposit/approval process. Neither turns every PMC article into an
  openly licensed work. Use current [dataset/service guidance](https://pmc.ncbi.nlm.nih.gov/tools/textmining/)
  for automated access; an archive identifier does not guarantee endpoint eligibility.
- [REAL policies](https://real.mtak.hu/policies.html) provide for research/study use
  of single copies with attribution and retained notices, describe accredited
  depositors and embargo handling, and restrict robotic harvesting except for
  transient indexing. Item-specific conditions can differ. These terms provide
  relevant institutional provenance and undermine an automatic no-CC rejection;
  they do not establish this item's version, rights clearance, unrestricted
  public redistribution, or permission for the desk's automated extraction.
  The live policy was read now; its exact wording on 30 October was not established.
- [US Copyright Office FAQ](https://copyright.gov/help/faq/faq-general.html) separates
  facts from protected expression. Its [fair-use guidance](https://www.copyright.gov/fair-use/)
  requires a contextual assessment, with no automatic safe word count. Concise
  factual evidence and extensive article republication are different uses.
- Direct article opens for both PMC IDs returned browser challenges. REAL item
  141896 timed out. The Europe PMC metadata endpoint could not be opened by the
  web reader. Search-indexed PMC content corroborated identities and the Ephoron
  notice, but was not used to set `opened`, verify quotes, or certify a full read.
  No access challenge, prohibited route or host retrieval restriction was bypassed.

The October Europe PMC fields above are attributed to PR #46's earlier successful
metadata request; they were not freshly retrieved here. The exact CORE/REAL file
and its source relationship likewise remain audit-derived. These limitations
prevent claims of a new complete source verification.

## Operational rule and PR review

The original PR correctly kept evidence held, separated access from reuse and
identified an accepted precedent. It could not settle adoption because it changed
no rule. Its statement that the exact copyright notice had not been retrieved
was accurate for that session; the indexed corroboration above adds evidence
without erasing the live-retrieval limitation.

The revised rule makes four decisions explicit: legitimacy of the exact copy and
retrieval route; what was actually read; support for the scientific claim; and
rights for content retained publicly. `source.access: open` remains compatible
with existing code but is defined as authorized free reading. Rights, version,
provenance and uncertainty use existing notes and the one paper reconciliation.
Absence of CC alone is not a failure; unresolved necessary authorization or scientific
verification remains a hold. Quote limits and audit requirements remain in force.

Policy delivery is recorded in the existing launch manifest as
`evidence_access: evidence-access-v1`, including the new file's blob SHA. Do not
restart running units or invent delivery acknowledgments. Returning unaccepted
candidates receive the integrated policy review at disposition. Do not mass-rewrite
accepted evidence or automatically re-admit licence-held candidates. The new
instructions are not proof of private-launcher adoption until the real receipt
and acknowledgment exist.

## Separate requirements for the six Ephoron candidates

The following is an **audit-derived verification target**, not new evidence or a
completed scientific audit. Recover the original untracked JSONL if available;
otherwise reconstruct candidates from a newly read source and label that fact.

| Former d151 lines | Candidate fitted maxima (nm) | Group/sample to verify |
|---|---|---|
| 1–2 | 373 UV; 530 green | Female larvae, n = 14 |
| 3–4 | 379 UV; 522 green | Male larvae, n = 5 |
| 5–6 | 364 UV; 516 green | Female adults, n = 13 |

1. Inspect the permitted exact copy, identity, version and rights. Read the
   relevant Methods, Results, figures/captions and available supplements; log
   unread material. Verify every candidate value and whole-sentence quote
   against that copy. Neither a PMCID nor the abstract supports these six values.
2. Verify the extracellular ERG method and two A1-template fits to mean group
   sensitivity. Keep model-estimated peaks distinct from isolated receptor
   measurements, opsin identities and demonstrated colour vision. The independent
   auditor must decide trait/grade suitability under current BRIEF; do not
   automatically treat a fitted component as a directly measured receptor class.
   Retain stimulus/adaptation conditions, uncertainty and unsupported mechanisms.
3. Correct the female comparison using the source: audit 236 reports UV
   `p = 0.047, z = -1.990` alongside the authors' practical-similarity wording,
   and green-peak `p < 0.01, z = -2.669`. Distinguish per-preparation peak tests
   from mean-curve fitted peaks and sensitivity amplitude. Do not convert the
   UV finding into an unqualified null or conflate peak position with amplitude.
4. Keep the female larva–adult comparison off the male-larva claims; verify the
   single adult male and absence of a fitted male-adult curve. Check the female
   reproductive subimago description and each group's collection/recording
   conditions. Remove adult timing from larval records and add adult collection
   context. Verify the source's limitations on fit uncertainty, blue receptors,
   polarization contribution and perception versus ERG.
5. Recheck accepted taxonomy and duplicates against the then-current accepted
   main. Draft a new, separately traceable refile unit with current launch/base
   provenance, one source reconciliation and all scientific qualifications in
   the records. Keep audit 236 and d151's original zero-yield history intact.
6. Run strict new-input validation, `quotecheck.py` against legally obtained
   source text, final baseline-aware `check_submission.py`, and
   `scientific_preflight.py` with current hashes. Record commands and actual
   outcomes separately. A source/quote retrieval gap is a hold, not a checker pass.
7. Submit all six corrected candidates to an independent source-reading auditor
   who did not author them. Audit copy/route, quotations and every scientific
   correction; retain per-record dispositions and immutable candidate/audit
   commits. The existing desk integrates only the candidates that pass. This
   report and policy approval do not substitute for that audit.

## Validation and handoff

This change is documentation only. Validation against the baseline above:

- All 32 relative Markdown links in the eight changed/new documents resolve.
- Six existing reader/auditor/intake/launch documents reference the shared rule;
  the launch example includes its version and supplied-file blob entry.
- `git diff --check HEAD` passes.
- `python3 -I tools/senses/check_submission.py --base-ref 074589ee524b1d243b2371c765715f81be9215f7`
  reports 0 evidence files, 0 new/changed records and 0 problems. This confirms
  the absence of evidence edits; it is not scientific verification.
- The accepted d105 record, audits 195/236, d151 disposition and desk queue are
  byte-for-byte unchanged; the final change set contains only eight documents.
- No application build, new numerical audit, source-completion receipt,
  `quotecheck.py` result or scientific-preflight pass is claimed.

Policy review also checked the distinct outcomes for a licensed but unread
source, a readable non-CC official archive, an untraceable aggregator copy,
abstract-only support and a free copy with a prohibited automated route.
Scientific and quotation failures remain holds regardless of licence.

Continue through the [Codex lane](../desk-queue.md#codex-lane-26-october-2026):
the desk reviews the findings and integrates the branch, then closes the PR.
No GitHub merge-button action or self-admission is performed by this submission.
