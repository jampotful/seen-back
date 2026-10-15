# Precision audit 16, 15 October 2026

Scope: every evidence record in sweep-98 (1), canon-13 (3), sweep-100 (2), sweep-101 (2), harvest-1 (2) and harvest-2 (2), 12 records in all, and the five wanted lines of the same units (sweep-98 and sweep-100 have no wanted file). No sampling; all were opened.

Method as in audits 13 to 15: each source opened with WebFetch and asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces of at most about 125 characters. Verdicts: `confirm`, `requote`, `correct`, `retract`, `unverifiable`. Typographic differences (italics, a page-break hyphen) count as `confirm`; a change to the partial flag or the grade counts as `correct`; changes to `method`, `conditions`, location or metadata are written as rows that are not counted. Corrections are in `docs/views/recheck/recheck-16.jsonl` in the recheck-5 schema. No evidence file, no wanted file and not `docs/views/audit/ALL.jsonl` was edited.

## Table

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| sweep-98:1 | Richardia brasiliensis / sense_light_nonvisual | m | confirm | verbatim on the SciELO page, Results 3.1; the sentence opens "With regard to photoperiod," before the quoted words, which carry the result. Table 1 in light: 20.0, 20.5, 40.0, 63.5%. The `method` field says "constant temperatures"; Methods 2.1 use four alternating regimes (20-25, 20-30, 20-35, 15-35 °C). Fixed in a row that is not counted |
| canon-13:1 | Physcomitrella patens / sense_light_nonvisual | g | confirm | verbatim (gene names italic on the page). Gene survey, so `g` |
| canon-13:2 | Ceratodon purpureus / sense_light_nonvisual | g | confirm | verbatim; the page's sentence ends with a full stop the quote leaves off |
| canon-13:3 | Anthoceros punctatus / sense_light_nonvisual | g | requote | the quote drops "(20X; Li et al.18)" from mid-sentence without marking the cut. Requoted to the whole sentence (21 words); value stands |
| sweep-100:1 | Mentha piperita / sense_light_nonvisual | m | confirm | verbatim in the ASHS PDF (Discussion); the 13 h per 24 h treatment sentence is in the Abstract. No DOI is printed on the PDF; the ASHS article page did not load, so the blank field stays |
| sweep-100:2 | Sesuvium portulacastrum / diel | m | confirm | verbatim on PMC (Results, "Experiments with potted plants"; the record says "CO2 exchange paragraph"). ΔH+ 1.3 ± 0.9 (wet, n = 15 d) and 7.7 ± 3.2 μmol g−1 FM (dry, n = 8 d) confirmed from the outdoor garden-bed results. PMC gives "2018 Dec 7" and issue date 2019 Nov 15; the record's 2018 and 70(22) match |
| sweep-101:1 | Linepithema humile / interommatidial_deg 15.3 | m | confirm | verbatim, p. 5. The `method` field calls 41,253 deg² a hemisphere; the paper gives it as the full sphere and assumes a hemispherical field. Fixed in a row that is not counted |
| sweep-101:2 | Thalassarche / fov_h_deg 270 | g | confirm | verbatim (NORA abstract); the sentence continues ", but there is a 60 ° blind sector above the head". Two species pooled (as Diomedea melanophris and D. chrysostoma), so `g` is right. NORA says "Full text not available from this repository"; `partial: true` correct |
| harvest-1:1 | Branta sandvicensis / spectral_range_nm | m | confirm | verbatim on the open Springer page (full text). "no UV light transmitted below 331 nm" (Results) and "(331–700 nm)" (Discussion) back the value. One bird for ocular media |
| harvest-1:2 | Branta sandvicensis / lambda_max_nm | m | confirm | the abstract sentence matches. The Results sentence with the four cone peaks runs to 62 words, so the 40-word limit leaves the abstract sentence as the quote; 413 ± 6.50, 483 ± 3.41, 505 ± 5.50, 568 ± 8.00 nm, rod 503 ± 1.13 nm, and filtered 415, 498, 544, 603 nm all match |
| harvest-2:1 | Libellula quadrimaculata / spectral_range_nm | m | confirm | the open PDF (eje.cz) loaded this time and was read in full: verbatim across the page break inside "measure-ments" (pp. 477-478). 14 filters from 300 to 700 nm, 150 W xenon arc lamp, subcorneal dorsal electrode. "Adult males" in `conditions` belongs to the field observations; the ERG section gives no sex. Fixed in a row that is not counted; `partial` false stands |
| harvest-2:2 | Plantago lanceolata / sense_light_nonvisual | m | confirm | the scielo.cl PDF is still refused by robots, but the journal's own open PDF (gayanabotanica.cl) was read in full: the quote is in the English abstract; Table 6 gives leaf area up to 59.9% and length, width and height about 30.8, 24, 30.9%; pigments and UV-B absorbing compounds unchanged. First author is Roberto Niculcar (record has "M"). Metadata row, not counted; `partial` false stands |

**Rate: 1 error in 12 verifiable records, 8%** (0 unverifiable). The one error is a quote joined from two pieces that dropped a mid-sentence parenthetical without marking it.

## Checks the desk asked for

- **The two harvest-2 records read through page summaries.** Both full texts were read in this audit: the Libellula PDF opened at eje.cz, and the Plantago paper opened through the journal's own site after scielo.cl refused it. Both values hold, so neither needs `partial: true`.
- **Abstract-only records carry `partial: true`.** The one abstract record (sweep-101:2) does. Every other record was read in full text (SciELO, Nature, ASHS PDF, PMC, JEB PDF, Springer, eje.cz, gayanabotanica.cl).
- **Pooled or unnamed-species records are `g`.** sweep-101:2 (two albatrosses pooled) is `g`. The three canon-13 gene surveys are `g` by the gene-inferred rule. Every other record names one measured species and is `m`.
- **Values quoted from another study.** None.
- **Converted or estimated values.** sweep-101:1 is the authors' facet-count estimate, labelled so in `method` and `note`.
- **Encyclopedia and database sources.** None.

## Wanted lines (not edited)

- **canon-13, Li and Mathews 2016.** Confirmed on the Springer page: Li, F-W., Mathews, S.; J Plant Res 129: 115-122; 10.1007/s10265-016-0785-4. The page leaves the issue blank, so "129(2)" is unchecked; no open access label.
- **harvest-1, Jane and Bowmaker 1988.** Confirmed on the Springer page: S. D. Jane, J. K. Bowmaker; J Comp Physiol A 162: 225-235; 10.1007/BF00606087. The abstract gives "about 420 nm, 452 nm, 502 nm and 570 nm", as the `why` says.
- **harvest-2, Guillemain, Martin and Fritz 2002.** Not checked against an opened page: doi.org failed to fetch, and the HAL record (hal-00192043) and the CAS catalogue returned bot-protection pages. A search lists the title on HAL. The line gives no volume or pages.
- **harvest-2, Hart, Partridge and Cuthill 1999.** Not checked against an opened page: doi.org redirected to Elsevier's linking hub, which was refused at the permission step, and Europe PMC rate-limited the fetch tool.
- **sweep-101, Martin 1998.** Confirmed on NORA (eprint 504191): Martin, G. R.; Proc. R. Soc. B 265(1397): 665-671; 10.1098/rspb.1998.0345. NORA offers "Request a copy" only.

## Rows written

`recheck-16.jsonl`: 5 rows.

- Counted: canon-13:3 (`requote`, quote and where).
- Not counted: sweep-98:1 (`correct`, method), sweep-101:1 (`correct`, method), harvest-2:1 (`correct`, conditions and note), harvest-2:2 (`correct`, authors, journal pages, url and note).

## Blocked pages

- pmc.ncbi.nlm.nih.gov/PMC4532828 (Li et al. 2015) and linkinghub.elsevier.com (Hart et al. 1999): permission step not answered.
- Europe PMC REST: HTTP 429, rate limited. api.crossref.org: refused by the egress proxy.
- hal.archives-ouvertes.fr and katalog.lib.cas.cz: bot-protection pages. doi.org/10.1046/j.1365-2435.2002.00652.x and the ASHS article page: fetch error.
- scielo.cl PDF for Niculcar et al.: robots.

## Patterns (this run)

1. Quotes joined from fetch-tool pieces can lose words at the seam (canon-13:3). A join should be checked against one more request for the whole sentence before filing.
2. `method` and `conditions` fields drift from the paper where the paper's own wording is unusual: alternating temperatures written as constant (sweep-98:1), a full-sphere constant called a hemisphere (sweep-101:1), field-observation animals carried into the ERG conditions (harvest-2:1). None changes a value, but each would mislead a reader of the record.
3. When a repository refuses by robots, the journal's own site often serves the same open PDF (harvest-2:2). One search for the journal's article page at filing would have given full text and the correct author initial.
