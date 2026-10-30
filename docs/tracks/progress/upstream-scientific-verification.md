# Upstream scientific verification investigation

30 October 2026. Investigation snapshot: `75546c727eab9d0e2258ba22ca5519aaa558679c`. Implementation rebased onto inspected main `8337ef754e1989333c9f0a3df701c795d86489d3` after PRs [42](https://github.com/jampotful/seen-back/pull/42) and [44](https://github.com/jampotful/seen-back/pull/44) merged. This is a process improvement and a retrospective, informed replay, not a fresh disposition or a blind estimate of prevention accuracy.

## Finding

The records can satisfy a structural validator and contain authentic quotations while misrepresenting the paper. The existing upstream rules require accurate sourced values and, on the OA route, whole-paper/table reading. Recent desk evidence units instead report reading through WebFetch summaries, selecting short abstract sentences, and validating their literal wording. The audit then does the missing comparison among endpoints, controls, definitions and contrary findings. Some authors already noticed one conflict in a paper while missing another in the same Results section. The failure is therefore not explained solely by unavailable sources or lack of an instruction to read tables.

Audits 172–180 report 17 counted errors among 42 candidates (40.5%) for that nine-audit window. This does not estimate the whole project's failure rate. In the selected replay window 177–180, 11 of 19 original candidates were rejected. Neither historical count is changed here, and no passing record is readjudicated.

## What instructions and workflow can actually be established

| Layer | Versioned instruction or observed behavior | Interpretation |
|---|---|---|
| [BRIEF](../../views/research/BRIEF.md), pre-change | Every research agent reads it; accurate values, source access, grades, at most 40 quote words; extracted-text search before logging. Economical reading focuses on passages near matches. | Accuracy/provenance already required. No explicit per-paper reconciliation receipt or metric-direction/control checklist. |
| [oa-pass](../prompts/oa-pass.md), [oa-read](../prompts/oa-read.md), pre-change | Whole paper, tables, captions/supplements; direct legal source text; quotecheck; source/partial rules; own branch and desk audit. | Table reading and quote verification were not missing requirements on this route. These files describe an encrypted OA-fetch/local-text workflow, not proof that desk-d87–d90 followed it. |
| [desk-screen](../prompts/desk-screen.md), pre-change | Search/wanted screening; explicitly no evidence in that screening round; owner's trait-scope rulings include applied hormones/growth regulators and nitrate germination trials. | Its search gate cannot stand in for an evidence gate. Lead-reading units had evolved beyond the original screening assignment. |
| [desk queue](../desk-queue.md) | Progression to lead-reading, per-unit audit and selective branch integration; Codex PRs reviewed through their branches. | Preserves independent review. Its old “Running” heading is not a reliable live process inventory. We did not change it or the dispatcher. |
| [d87](desk-d87.md), [d88](desk-d88.md), [d89](desk-d89.md), [d90](desk-d90.md) | WebFetch-mediated reading; proxy failures; preference for sentences under 125 characters; d89 explicitly says Results came through a summary; d87 records a successful check.py run. | Direct observation from committed notes, not an inference that all source pages were inaccessible or all requirements ignored. The 125-character issue is PR #42's work. |
| [Audits 177](audit-177.md), [178](audit-178.md), [179](audit-179.md), [180](audit-180.md) | Empty search/wanted files pass the mechanical gate; quote wording checked through WebFetch/yes-no requests; source interpretation independently rechecked; failures removed at disposition. | The counted omissions and reversals were found after submission. A yes/no summariser reply is not a local source-text quotecheck run. |

The exact ad-hoc launch messages for desk-d87–d90 are **not present in the inspected versioned files**. Their named branches, submitted records, progress notes and audits are recoverable; that does not establish which prompt version was actually loaded into each agent or whether it received an additional private instruction. We did not access the running desk session. New launches must now record the checkout commit and prompt paths, and the desk-screen handoff explicitly names the evidence preflight. This closes an observability gap without pretending the missing launch transcript was recovered.

### Missing requirements versus failures to comply

- **Already required:** faithful quotation and provenance; accurate values on the right taxon; OA whole-paper/table reading; access limitations and partial provenance. Calling a variance increase greater uniformity, or presenting a summary as verified raw text, does not become acceptable because there was no dedicated checklist.
- **Explicit in audit precedent but not operationalized upstream:** carry material nulls, contrary results and qualifications. Audits [162](audit-162.md), [164](audit-164.md) and [176](audit-176.md) already apply this standard; 177–180 repeatedly cite it. We cannot prove every researcher saw those precedents.
- **New upstream requirement:** before drafting, document endpoint definitions/direction, like-for-like controls and conditions, significance for the specific endpoint, relevant treatment combinations and reconciliation with the whole accessible abstract/Results. Bind a final author check to the exact submitted record, including conditions and notes.
- **Still a compliance/judgment risk:** an author can write a complete but false reconciliation. No schema or hash can establish that a source was understood. The independent audit remains necessary.

### What the existing tools actually validate

| Tool | Checks | Does not establish |
|---|---|---|
| `tools/senses/check.py` / `addlog.py` | Required keys, trait/grade, source metadata/access enum, opened flag, nonempty quote and word count. addlog supplies unit/opened defaults. | Correct metric direction, control, significance, omitted results or source truth. All 19 recovered candidates pass. |
| `tools/views/screen_candidates.py --check` | Searched/wanted coverage against harvest candidates and evidence. | Scientific support for evidence; it has no evidence input. The local CLI attempt could not run without the CI harvest branch; the empty-file passes are reported by the original audits, not claimed as reproduced here. No harvest was started. |
| `tools/views/quotecheck.py` | Normalized substring/ellipsis matching, or a table-number/taxon fallback. | That a matched quote supports every field or captures contradictory findings. Exact wording alone cannot prevent the observed errors. |
| `tools/views/oa_lint.py` | Quote shape, numeric overlap, metadata and partial heuristics. | Statistical interpretation or contextual completeness. Not demonstrated as run by these recent units. Its quote-only numeric heuristic is unchanged. |

## Implemented safeguard

[scientific-preflight.md](../prompts/scientific-preflight.md) is required through BRIEF and the OA/desk handoffs for **fresh evidence launches after integration**. One compact JSONL review per paper shares source access, design, metric definitions, located results and reconciliation across its records. Each record receives its own final claim check, decision and canonical JSON fingerprint.

`tools/views/scientific_preflight.py` creates an intentionally incomplete, held skeleton and checks completed documentation without network calls or writes. Missing, duplicate, wrong-source or stale receipts fail. A held claim cannot submit. Abstract-only status must retain abstract access and partial=true. Limited claims must preserve the exact limitation in the evidence's note or conditions; an unread relevant table cannot be called full-text verification. This does not redefine partial for reviews or figure-derived values.

The gate checks documentation, not semantics. It neither adds accepted evidence nor runs an automated scientific classifier. It is deliberately not installed as a retrospective schema requirement in addlog/check.py: that would disrupt running units and existing logs. Operational enforcement is the new-launch instruction and the pre-submission command, followed by the established independent audit. Integration alone cannot prove the external desk launcher adopted the prompt; its first new-unit receipt is the observable adoption check.

## Replay against audits 177–180

The original candidate files were read at these immutable branch heads, not reconstructed from the surviving main evidence:

| Unit | Original commit | Records / papers |
|---|---|---|
| desk-d87 | [f7cda57a](https://github.com/jampotful/seen-back/blob/f7cda57a60892b036b6dc20937e9e2b63b135a06/docs/views/evidence/desk-d87.jsonl) | 6 / 5 |
| desk-d88 | [2a734dd0](https://github.com/jampotful/seen-back/blob/2a734dd061d23a852c81c6dce0958b210fde4c3e/docs/views/evidence/desk-d88.jsonl) | 6 / 3 |
| desk-d89 | [8473730f](https://github.com/jampotful/seen-back/blob/8473730fac4be9f228129a2b6c3f1507e53ef6d5/docs/views/evidence/desk-d89.jsonl) | 1 / 1 |
| desk-d90 | [1ba16a3d](https://github.com/jampotful/seen-back/blob/1ba16a3d9da35334e0452dafb7db6b1734ebc531/docs/views/evidence/desk-d90.jsonl) | 6 / 4 |

The following is a manual checklist replay with known audit findings. “Plausible prevention” means an honest execution of the named check would expose a concrete discrepancy; it is not a measured detection rate. The code itself cannot independently find any of these eleven scientific errors.

| Audit:line | Check that exposes the submitted fault | Plausible prevention and residual judgment |
|---|---|---|
| 177:2, Prunus | Results check includes adverse stem/root outcomes in Table 2, not only best germination and growth. | Plausibly prevents a promotion-only summary. Requires reading the correct column/control and deciding which growth qualifiers bear on the record. |
| 177:4–5, Ferula | Design/results inventory distinguishes GA3 alone, chilling alone and combined GA-chilling, separately for each species. | Plausibly prevents omission of the combinations and unsupported substitution of GA3 for chilling. The relevant combined findings were already in the abstract. |
| 178:1–2, Laggera light | Reconciliation compares the pooled timing statement with subgroup acceleration claims; final check also reads conditions. | Plausibly exposes the sign reversal/omission. Retain the apparent disagreement; deciding whether aggregation or another design distinction explains it requires scientific judgment. |
| 178:3, Laggera chemical | Record KNO3's pooled null, subgroup result and interactions, with their experimental context. | Plausibly prevents one-sided wording. A non-significant main effect can coexist with a subgroup effect; the gate must not automatically label that a contradiction. |
| 179:1, Aristotelia | Compare onset with the control separately from final maximum; reconcile the English abstract, Spanish summary and Results. | Plausibly prevents interpreting higher final germination as earlier onset and omitting later FLU onset. Translation/curve interpretation and absence of a reported test still need judgment. |
| 180:1, Astilboides light | Inventory includes timing as well as percentage; name the unread figure instead of implying complete inspection. | Plausibly prevents the timing omission. Figure extraction and partial provenance remain separate decisions. |
| 180:2, Astilboides chemical | Separate final percentage, energy, mean time and T50; compare abstract with body; check letters for the specific endpoint. | Plausibly prevents extending a percentage null to every endpoint and treating every numeric increase as significant. Text/table and dose inconsistencies must remain visible. |
| 180:3, Catolobus | Read the GU definition/formula and comparison letters before interpreting its numerical direction. | Plausibly prevents the variance reversal. The researcher must actually understand the index and same-letter null; a filled metrics field is insufficient. |
| 180:5, Hydrangea chemical | Check all in-scope treatments and endpoints for reductions and delays; restrict significance claims to their column. | Plausibly prevents omission of adverse kinetin/nitrate results and transfer of percentage significance to energy. Resolve or preserve conflicting dose units; do not invent a repair. |

All 11 rejected candidates have an explicit corresponding check. That is coverage of known failure modes, not proof of prospective prevention. Eight historically passing candidates are not newly certified. In particular, the protocol still allows an honest abstract-only Impatiens record, and does not require inventing absent temperatures/replicates or fetching a subscription paper to complete a checklist.

### Independent source spot-check and access limits

- **Astilboides:** inspected the [publisher's full-text XML rendering](https://www.hst-j.org/articles/xml/YBLv/), Methods, Results, Discussion and table captions. The body distinguishes final germination from improved energy/timing under nitrate and reports shorter germination duration in light. This confirms the endpoint/reconciliation failure without relying solely on the audit. Table cells are images; image links were returned, but their cells were not independently visually reverified here. Detailed table values/letters in the replay remain attributed to audit 180.
- **Laggera:** inspected [publisher Methods and Results 3.1–3.2](https://link.springer.com/article/10.1007/s44372-025-00295-0). They contain the pooled delay and acceleration language, and pooled KNO3 null alongside form-specific effects/interactions. The replay preserves those distinctions without adjudicating the paper's internal consistency. Table links resolved to the article without exposing separate cells; no table-cell verification is claimed.
- **Impatiens:** inspected the [publisher abstract](https://link.springer.com/article/10.1007/BF00024800), explicitly subscription-preview only. It supports a limited-access positive control; no full-text verification is claimed.
- **Remaining replay:** the KoreaScience PDFs for Catolobus, Hydrangea and Astilboides did not open through the retrieval tool; Astilboides was recovered via the publisher route above. Aristotelia's [publisher abstract](https://revistabosque.org/index.php/bosque/article/view/394) opened, but not the PDF text; Prunus and Ferula full-text attempts also failed. Their detailed numerical/translation comparisons are audit-derived. We did not retrieve unauthorized copies, copy paper text into the repository, or refile any failed record.

## Cost and validation

The historical set groups into 13 paper reviews for 19 records; shared design/results are not repeated for every trait. The gate is local and makes zero source calls. The 13-test suite runs in about 0.1 seconds here. Researcher overhead is the targeted scientific reading and a short note, not this script. The original units reported approximately 25 searches/45 fetches (d87), 45 searches/40 pages plus Crossref queries (d88), 60 searches/75 fetches (d89), and 25 searches/35 pages (d90). Those are self-reported counts, not a controlled timing baseline.

The safeguard does not mandate another literature search or second agent. It should add modest work when source passages are already available; difficult tables or translations can be expensive. **No live time/token benchmark was run, so disproportionate overhead has not been ruled out empirically.** The protocol asks the first three fresh units to report review minutes (or not measured), extra source calls and holds, alongside total reading cost. A hold preserves uncertainty; it is not a successful scientific verification or an error-correction count.

Validation performed:

- Existing `check.py`: all 19 original candidates pass, zero problems. This reproduces the structural/semantic gap.
- New gate without receipts: all 19 are blocked for missing documentation. This verifies mandatory coverage, not eleven-error semantic detection.
- `test_scientific_preflight.py`: 13 tests pass, covering stale conditions, missing/duplicate/wrong-source receipts, holds, access/status consistency, limitations in the evidence, malformed inputs, physical line numbering and read-only CLI behavior. One boundary test explicitly shows that a complete but false assurance is not detected.
- PR #42's `test_quote_limit.py` on the current checker/addlog: all four tests pass. No quote length or existing validator behavior changes.
- Clean three-way integration of changed instruction files with current main; `git diff --check` passes. PR #44's files are disjoint from this change. Original audits, dispositions, accepted evidence, provenance, queue, automations and publication files are outside the patch.

Only a focused file snapshot was needed locally; no whole-app build or repository-wide validation is claimed. Submit this as a Codex PR for the desk's normal branch review/integration. No direct main merge or live launcher change is part of this work.
