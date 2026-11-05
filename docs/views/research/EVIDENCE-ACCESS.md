# Evidence access, version 1

This governs new source-access decisions after desk integration. It separates
permission to obtain and read a particular copy, the material actually inspected,
scientific support, and permission to reuse protected content. It supersedes the
blanket open-licence requirement for repository copies expressed in audits 223
and 236. Those historical decisions and counts remain unchanged. Apply this rule
consistently to publisher, PMC, institutional and subject-repository copies.

## Decide on the exact copy and route

1. Match the title, authors, year and DOI (when present). Record the exact URL,
   host, version and inspection date. Distinguish a version of record, accepted
   manuscript, submitted manuscript/preprint and unknown version. A filename or
   registry flag alone cannot establish the version or scientific equivalence.
2. Establish a credible basis for authorized public access: the publisher's own
   public copy; an official PMC/Europe PMC archive record; or an identifiable
   institutional/subject repository deposit supported by its item record and
   deposit/access policy, publisher manuscript policy, or explicit permission.
   Record the supporting URL and relevant terms. A reputable host is evidence of
   provenance, not a guarantee overriding a conflicting item-specific notice.
   Trace aggregator links to their source; do not assert a CORE-to-repository
   relationship from a matching title alone.
3. Inspect the copy's rights panel and relevant host terms where available.
   Record the licence and version if explicitly stated. Otherwise distinguish
   `no open-reuse licence stated` from `rights panel not inspected`. Missing CC
   metadata and an all-rights-reserved notice do not, by themselves, disqualify
   authorized reading or cited factual extraction. An HTTP 200, an OA registry
   flag, a PMCID, or a downloadable PDF alone does not establish any reuse right.
4. Respect access controls, embargoes and restrictions on the retrieval method.
   No login/proxy or unauthorized-copy route prohibited by AGENTS.md becomes
   permissible. Do not bypass challenges or rate limits. Bulk/automated access
   must use the host's currently permitted service and eligible content subset;
   free individual reading does not authorize automated harvesting. A licence on
   linked code, data or supplements does not license the article.
5. If the copy's identity, provenance, version needed for the claim, or permitted
   route remains unresolved, hold that source-dependent claim and name the
   missing check. Try another permitted copy within the existing retrieval
   budget. An abstract may support only what is actually read there. Metadata,
   search snippets, a prior audit and a summariser's assurance cannot replace a
   required source read or quote check.

Unknown reuse permission does not mean unknown permission to read. Record those
uncertainties separately. Conversely, a known licence cannot repair unread
Methods, damaged table extraction, a misleading claim or an unverified quote.

## Use the existing fields accurately

No schema migration or new access enum is introduced.

| Existing field | Meaning under this rule |
|---|---|
| `source.access: open` | Supporting full-text passages were read through an authorized, freely accessible route. This is the legacy free-reading category; it does not assert an open-reuse licence or a complete paper read. |
| `source.access: abstract` | Only the abstract supports this record; retain `partial: true`. A known full-text URL does not upgrade it. |
| `source.access: closed` / `book` | Preserve BRIEF's existing owner-supplied paper/book meanings and explicit access authorization. This rule grants no new library-login access. |
| `opened` | The source material supporting the claim was actually read in this task, as BRIEF requires. Discovery metadata or search snippets cannot set it to true. |
| `partial`, grade, `evidence_kind` | Retain their scientific/provenance definitions. None is a rights classification or permission to ignore missing context. |
| Preflight `access.kind` | `full_text`, `abstract_only` or `incomplete` describes inspection coverage. It is separate from `source.access` and reuse rights. |

For each new/revised record, keep the actual copy in `source.url`, the supporting
passage in `where`, and a compact version/access/rights qualification in `note`.
For a non-openly-licensed source, say explicitly that it is free to read and that
open reuse has not been established. Do not silently relabel it CC BY or change
its source to a copy not read.

Reuse the existing per-paper scientific reconciliation and unit progress note;
do not create another receipt or queue. In preflight `access.inspected`, record
the exact copy, route, date, version and provenance/rights sources actually
inspected alongside the scientific sections. Keep `access.unavailable` for
unread scientific material and the retrieval failures causing that gap. Put
unread rights panels and unresolved permissions in the existing progress note
and record `note`, distinctly from scientific coverage. An unstated reuse
licence alone must not change `access.kind` to `incomplete`: the validator uses
that field for scientific reading gaps. A necessary unresolved authorization
check still holds the candidate outside the submission. For a unit without a
paper receipt, put the compact account in its existing progress note. A shared
provenance check can serve multiple records, while each retains its qualifiers.

## Keep extraction and republication separate

Cite factual measurements and write scientific explanations in the researcher's
own words. Facts and the source's protected expression have different copyright
status. Any retained quotation must meet BRIEF's exactness/context requirements,
the tools' restrictions and the applicable permission or legal exception.
BRIEF's 40-word ceiling is a format maximum, not a legal safe harbour; use a
stricter applicable limit. Consider the accumulated quotations from one paper
across records. Do not split a passage across records to evade a limit.

Without an adequate basis for the intended quotation, narrow it without losing
scientific meaning or hold the candidate for review. A paraphrase is not an exact
quote and cannot be substituted into `quote` to pass the checker. Research use
and attribution do not automatically authorize every reuse. Do not commit
article PDFs, full text/XML, copied figures or substantial table reproductions
under this workflow. Retain only permitted concise evidence and provenance;
source files stay outside the public repository. No repository licence grants
rights in third-party source material.

## Audit and rollout

Audit separately: (a) copy/route authorization and recorded uncertainty;
(b) inspection coverage and exact quotation; (c) scientific meaning and
classification; (d) rights for material retained publicly. Missing CC alone is
not an error. An unresolved required check is a hold, not a scientific null or
proof that a paper is closed. Count substantive record errors under oa-audit's
existing rules, once per affected record; state multiple reasons separately.

Fresh launches receive this file through desk-launch.md, with its blob version
in the existing supplied-instructions manifest and `evidence_access:
evidence-access-v1` in the progress note. Keep running units on their pinned
instructions; review returning unaccepted candidates under the integrated rule
without restarting them. Do not backfill accepted observations, change historical
audit counts or reopen completed work automatically. A prior licence-only hold
can receive a new targeted assessment. Admission still requires source checks,
normal validation, independent scientific audit and the desk's disposition.
An instruction merge alone does not establish delivery by the private launcher.

## Basis and case review

- [PMC Copyright Notice](https://pmc.ncbi.nlm.nih.gov/about/copyright/): free reading,
  default copyright, reuse restrictions and automated-retrieval restrictions.
- [PMC author manuscripts](https://pmc.ncbi.nlm.nih.gov/about/authorms/)
  and [article datasets](https://pmc.ncbi.nlm.nih.gov/tools/textmining/): deposited
  versions, dataset eligibility and permitted retrieval services.
- [US Copyright Office: copyright basics](https://copyright.gov/help/faq/faq-general.html)
  and [fair-use factors](https://www.copyright.gov/fair-use/): factual information
  is distinct from protected expression; no universal word-count exemption.
- [PR #46 case reconciliation](../../tracks/progress/reassessment-236-pmc.md):
  Ephoron, Echinacea, source-specific uncertainty and the separate scientific hold.

Consult the current host terms for a proposed retrieval/reuse; these references
are the basis for the distinction, not a blanket licence for every host or copy.
