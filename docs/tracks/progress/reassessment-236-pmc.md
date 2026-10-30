# Audit 236 follow-up: Ephoron virgo and PMC9043733

30 October 2026. Repository baseline: `374b607c34ae1ebc6ed6ffb95b6cb54f96378801`.

## Disposition

**All six records remain held; this change admits no evidence.** The newly identified official PMC source has a supported access route under the existing instructions and an actual merged PMC precedent. A blanket claim that every PMC source needs a Creative Commons licence is not consistent with that precedent. Nevertheless, this session could retrieve the article's registry metadata and abstract, not its full methods/results or exact copyright panel. It therefore cannot independently verify and refile the six numerical records.

This is a source-specific reassessment and documented retrieval hold, not a reversal of [audit 236](audit-236.md). That audit's rejection of the CORE/REAL copy, six errors, historical pooled count and [desk-d151 disposition](desk-d151.md) are preserved. No access rule is amended. No article, figure, PDF, XML or full text is added to the public repository.

## What was independently established

The supplied lead is [PMC9043733](https://pmc.ncbi.nlm.nih.gov/articles/PMC9043733/). A successful [Europe PMC core-metadata request](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1098/rspb.2022.0318&resultType=core&format=json) returned one matching paper:

- DOI `10.1098/rspb.2022.0318`; PMID `35473376`; PMCID `PMC9043733`.
- Egri, Mészáros and Kriska, *Spectral sensitivity transition in the compound eyes of a twilight-swarming mayfly and its visual ecological implications*, 2022; volume 289, issue 1973; first publication 27 April 2022.
- `inPMC: Y`, `inEPMC: Y`, `authMan: N`, `isOpenAccess: N`; no `license` field returned.
- Free full-text links to PMC and Europe PMC, including the [Europe PMC article](https://europepmc.org/articles/PMC9043733).

These fields corroborate the article's identity and its availability through the official PMC archive. `authMan: N` distinguishes the archive record from an author-manuscript flag; it is not a substitute for inspecting the displayed version. `isOpenAccess: N` and an absent licence field do not establish either piracy or permission to redistribute. They also do not justify describing the article as openly licensed.

The owner's supplied account reports an **All rights reserved** statement. This session did not independently retrieve that panel; its wording must remain attributed to the supplied lead. The exact archived response to the Europe PMC metadata request had SHA-256 `9060bb4345b261150140dd33ebe36b5d590687fdcf9480373948f8dced3b2453` (temporary local metadata only).

## Access and reuse: comparison with the existing rules

| Rule or precedent, read from main | What it actually establishes | Application here |
|---|---|---|
| [oa-pass.md](../prompts/oa-pass.md), Finding a free copy / Writing what you find | Explicitly includes PubMed Central and Europe PMC among legal free-copy routes; uses the schema value `access: open`; prohibits committing article text. | Official PMC provenance is an existing route, not a new exception invented for these six records. The enum is not a redistribution licence. |
| [BRIEF.md](../../views/research/BRIEF.md), evidence log / Rules; [AGENTS.md](../../../AGENTS.md) | Requires a source actually opened in this session and legal access; forbids committing the paper's full text or PDF. | Registry metadata and a prior audit cannot stand in for reading the results that support a new record. |
| [Audit 178](audit-178.md) | Held an institutional deposit's full text whose authorisation was unstated; allowed abstract-derived records. | Supports the original caution about CORE/REAL; does not decide the status of an official PMC version. |
| [Audit 194](audit-194.md) | The NSF PAR article was an acceptable source because the PDF and Crossref establish CC BY. The submitted records still had other faults. | Shows one way to establish repository rights, not that all legal reading requires CC BY. |
| [Audit 195](audit-195.md), Licence / Verdict, and the actual [desk-d105 record](../../views/evidence/desk-d105.jsonl) | Describes PMC1646994 as a lawful NIH public-access manuscript without a stated open licence. Its only counted error was the missing DOI. It authorised a refile with the DOI and truthful access provenance; the corrected record is on main with the PMC URL and `access: open`. | This is a directly relevant, actually merged non-CC PMC precedent. The access label was a noted limitation, not grounds for exclusion. |
| [Audit 186](audit-186.md), line 2; [audit 202](audit-202.md), line 1; [audit 223](audit-223.md), Licence and access | Accept publisher-hosted free text without a printed CC licence. Audit 223 separately states a stricter repository rule. | The publisher exception alone cannot be transferred to every repository. But audit 223's summary of audit 195 omits the latter's explicit refile verdict and the actual merged PMC record. |
| [Audit 235](audit-235.md), Citations | Accepts the publisher's free version under the Company of Biologists user licence without CC; explains that `open` is the permitted schema value. | Reinforces the need to distinguish free reading from an open reuse licence in the record's note. |

**Access assessment:** the PMC route is eligible for legal reading and limited evidence extraction under oa-pass and the merged audit-195 precedent, provided the exact copy is inspected and its restrictions are recorded. Do not relabel this paper CC BY, treat PMC membership as blanket redistribution permission, or retrofit this finding onto the different CORE/REAL copy. Any eventual `access: open` record must explain that it means freely readable via PMC, not an established open reuse licence; the schema offers no separate free-to-read enum.

**Remaining policy ambiguity:** audit 223/236's general repository-licence language and audit 195's actual PMC disposition are not fully reconciled. If the desk treats that general language as superseding its accepted PMC practice, the precise question is whether official, authorised PMC copies may supply cited factual measurements and the existing short evidence quotations without an open redistribution licence. It is not whether the article may be republished in full. This follow-up does not silently resolve that conflict by weakening the rule or asserting new rights. It records the positive PMC precedent for the independent desk reviewer.

## Scientific refile checklist: inherited, not independently reverified here

The following six candidates and corrections come from audit 236. They are a checklist for a future source read, **not new evidence records**. None of these numbers occurs in the abstract retrieved this session.

| Former desk-d151 line | Candidate peak, nm | Group | Required correction/check before refile |
|---|---:|---|---|
| 1 | 373, UV | Female larvae, n = 14 | Preserve female-specific peak comparison and tests below. |
| 2 | 530, green | Female larvae, n = 14 | Include the significant female green-peak shift. |
| 3 | 379, UV | Male larvae, n = 5 | Do not attach the female larva–adult test to males. |
| 4 | 522, green | Male larvae, n = 5 | Same restriction; no male adult curve was fitted. |
| 5 | 364, UV | Female adults, n = 13 | Identify the reproductive subimago and adult collection conditions. |
| 6 | 516, green | Female adults, n = 13 | Include green-peak test and adult-specific conditions. |

For a lawful full-text re-read and independent audit:

1. Verify the six peak values in Results, the three group sizes in Methods, the two A1 pigment-template fits to mean extracellular ERG sensitivity, and the distinction between model-estimated peaks and directly isolated receptor measurements. Retain the absence of reported peak confidence limits/goodness-of-fit statistics and the source's uncertainty about mechanism, blue receptors and a possible polarization-sensitive UV contribution.
2. For female larvae versus female adults, retain both the authors' practical-similarity interpretation and the UV test `p = 0.047, z = -1.990`; it is not an unqualified null. Include the green-peak shift `p < 0.01, z = -2.669`. Audit 236 says these tests use per-preparation fits, whose means matched the mean-curve peaks within 1 nm. Verify that distinction rather than treating a test of peak position as a test of sensitivity amplitude.
3. Keep the female comparison out of male inference. Audit 236 reports that male and female larvae differed only at 516 nm, and that the single adult male was not fitted. Do not invent a male larva–adult test.
4. Verify the female reproductive subimago identification. Use larval collection at the river Ipoly near Letkés, mornings 3 June–5 August 2020, kept at 10°C, for larval records. Use adult collection at urban lights after sunset, 6–16 August 2020, and recordings around 05:00 UTC+2, 5–6 hours after collection, for adult records. Remove the adult recording time from larval conditions.
5. Verify the exact version's citation, accepted taxon, full sentences and numerical context from the source. Reconstruct the six lines if necessary; the original JSONL is not present on the inspected main tree. Do not claim to have recovered the original untracked records.

The retrieved abstract describes an amplitude difference between life stages; it does not state the six peak positions or the peak-shift tests. It cannot independently validate this checklist or substitute for the missing results. No abstract-only numerical refile is warranted.

## Retrieval limits and validation

- PMC HTML through the local HTTP client returned HTTP 203 with a cookie/browser challenge rather than article text. The connected URL reader returned HTTP 403. No challenge was solved and no proxy/login route was used.
- Europe PMC's core metadata and abstract were retrieved successfully. Its full-text XML endpoint returned HTTP 500; the linked Europe PMC article returned HTTP 403. The Royal Society DOI page returned HTTP 403. These failures were not treated as proof that the archive lacks the paper or that the paper is legally closed.
- Both web-search backends returned tool errors without source content. No invented web citation or claimed full-text read fills that gap.
- Checked the relevant rules, audit 236, desk-d151, and the actual merged desk-d105 record against main. The pertinent files were unchanged between initial main `e8a17e0` and the baseline above. The queue records d105 merged after DOI correction and d151 zero records merged.
- This submission adds only this follow-up. No evidence, source-completion receipt, queue yield, historical audit, admission standard or validator is changed. PR #45's seven-file upstream scientific-verification work is untouched.
- No evidence JSONL was created; `check.py` and `quotecheck.py` therefore have no new records to validate. Running them on audit-derived reconstructions would create false confidence about a source not read. No application build or repository-wide test is claimed.

## Integration handoff

Submit this report through the existing Codex PR lane in [desk-queue.md](../desk-queue.md). The desk audits and integrates through the branch; this report does not merge itself or accept its own evidence. On successful exact-source retrieval, resolve the documented access-language conflict against the actual PMC precedent, independently verify the six candidates and corrections, create a new refile unit, run `tools/senses/check.py` and `tools/views/quotecheck.py` against the legally obtained text, and submit it for independent audit. Preserve audit 236 and the original d151 zero-yield entry throughout.
