# Targeted reassessment of audits 158 and 159

29 October 2026. Reviewed against main at `863737cac3565edced71f439e360705d6161aef7` at the owner's request. Scope: `desk-d68:1` and `desk-d69:3`, their source publications, and the evidence-audit counting instructions. This is a targeted reassessment, not a random sample or a new audit of either entire batch.

## Decisions

| Record | Verdict | Scientific interpretation |
|---|---|---|
| `desk-d68:1`, Arbutus unedo | `correct`, one counted record | The relative treatment improvement stands, but omitting the low absolute emergence changes its practical interpretation. The full-text Methods also distinguish four GA3 genotypes from five stratification genotypes. Both corrections are now in the record. |
| `desk-d69:3`, Poa alpina | `correct`, one counted record | The omitted temperature-duration result limits the general photoperiod claim. The crossed design is not confounded. Flowering was assessed after transfer, not during the cold treatment. The correction does not claim photoperiod independence at every temperature, duration or flowering endpoint, or establish an interaction test unavailable in the abstract. |

Neither decision invalidates the study or removes its measured-species grade. Arbutus now records full-text access and clears `partial` after reading the publisher's paper; Poa remains abstract-only and `partial: true`.

## Sources independently read

- Demirsoy et al. (2010), DOI [10.17221/28/2009-HORTSCI](https://doi.org/10.17221/28/2009-HORTSCI): [publisher abstract](https://hortsci.agriculturejournals.cz/artkey/hor-201001-0007_seed-treatment-with-ga3-or-stratification-enhances-emergence-of-some-strawberry-tree-genotypes-short-communica.php) and [publisher PDF](https://hortsci.agriculturejournals.cz/pdfs/hor/2010/01/07.pdf). Read the paper; visually checked Methods and Tables 1-2 on printed pp. 35-36. The low-outcome qualification is explicit in the abstract and discussion. The existing quote is verbatim in the HTML, including its duplicated GA token; it was not silently replaced with the PDF typography.
- Pahl and Darroch (1997), DOI [10.4141/p96-108](https://doi.org/10.4141/p96-108): [publisher-deposited Crossref record](https://api.crossref.org/works/10.4141/p96-108), publisher `Canadian Science Publishing`, member `155`. Read the full `message.abstract`, including the experimental, transfer and conditional-result sentences. The DOI, title, authors, year and pagination match. Publisher landing/full-text routes were inaccessible during this review. The registry's deposited abstract was retrieved directly; no full-text access is claimed. The original quote passes against that abstract after whitespace normalization.

Retrieved-source SHA-256 fingerprints (source files kept outside the repository):

| Source | SHA-256 |
|---|---|
| Arbutus publisher PDF | `b483c437b0fdc2304b47f5f2bacd8c73844bb2cff4f20876f2d9ddb9e092dbdc` |
| Arbutus publisher HTML | `a5ba48157c9bcde92b4f62628d5d200b70ebd6cb29320dd0981fb934c367cc82` |
| Poa Crossref JSON | `fcc0b10fd5f833c2bf2d28b85e22b23162f9e075af449bc9bd89d6111a6f5e34` |

## Why the earlier counts missed these faults

Audit 158 explicitly lists the qualification as uncounted but supplies no materiality rationale. Audit 159 explicitly treats the quote's `and/or` as a sufficient hedge. Its disposition repeats that rationale while acknowledging that the conditions field should say crossed. These are documented decisions, not evidence of an absence of the qualifications in the sources.

The inherited instructions help explain those choices: audit 16 excludes changes to `method` and `conditions` from counting, and the previous opening of `oa-audit.md` defines a wrong value chiefly in relation to the chosen quote. Those rules encourage checking individual statements while leaving contextual omissions outside the count. This is an inference from the written rules and decisions, not a claim about an auditor's unrecorded reasoning.

The desk's own practice was inconsistent with treating such faults as harmless: audit 155 counted no errors for two omitted dark-only conditions, but the desk subsequently dropped those two records (`desk-queue.md`, d65 disposition). That precedent was inspected only to evaluate the counting convention; no additional evidence record was reassessed or changed here.

Under the clarified rule, each targeted record contributes one error, regardless of the number of affected fields. Holding all other original judgments fixed would change audit 158 from 0/5 to 1/5 and audit 159 from 0/3 to 1/3. These are counterfactual counts, not replacements for the historical reports. No historical pooled rate is recomputed, and no wider error rate is inferred from this selected pair.

## Narrow instruction change and history

`oa-audit.md` now tests scientific interpretation across the value, methods and conditions, and distinguishes consequential omissions from harmless compression. Each uncounted flagged omission needs a reason. A confirmed consequential fault must be repaired before that record is accepted, even when a pooled rate passes. `desk-audit.md` points its evidence audits to this rule, preserving the separate search-record rules and thresholds.

Both exact quote strings, DOIs, grades and record identities are unchanged. Each corrected record carries `audit.was` with every replaced field, the base commit, date and links to both the original audit and this reassessment. Reapplying those prior fields and removing the new audit object reconstructs the original record exactly at the JSON-object level. The other six evidence lines are byte-for-byte unchanged. Original audit reports, desk dispositions, queue, automation and runtime code are untouched.

## Validation

- `python3 -I tools/senses/check.py docs/views/evidence/desk-d68.jsonl docs/views/evidence/desk-d69.jsonl`: eight records, zero problems.
- `quotecheck.py` against separately retrieved publisher HTML / deposited abstract: both targeted quotes pass verbatim; no table fallback.
- `python3 -I tools/views/test_apply_audit.py`: pass.
- `python3 -I tools/views/test_gaps.py`: all five tests pass; existing resource-close warnings remain.
- `python3 -I tools/views/test_compile.py`: zero failed.
- `python3 -I tools/views/test_rows.py`: pass, using its stand-in API and temporary outputs.
- Scope/history check: only the two named evidence lines changed, exact quotes/DOIs/grades retained, previous records reconstructible, historical reports/dispositions/desk queue unchanged. `git diff --check`: pass.

`oa_lint.py` is **not green**: before the patch it flagged two of eight records (Arbutus's 300 and unrelated Lavandula figures absent from the selected quote); afterward it flags three, adding Poa's 10 and 3. This diagnostic checks numbers only against `quote`, not the other source passages identified in `where`. The Arbutus dose is verified in the publisher abstract and Methods; Poa's added duration and temperature are verified in the deposited abstract. Both existing quotes remain intact. No linter was weakened, and the unrelated Lavandula record was not edited. These flags are manually reconciled for the two targeted records, not reported as an automated pass.
