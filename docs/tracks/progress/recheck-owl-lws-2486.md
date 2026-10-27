# Owl LWS citation correction: findings 2486 and 2501

26 October 2026. Base: 797b02eaa39c5505920c6f1b2528fb8ba9d03fbf.

## Verified identity and claim

The intended paper is Felipe Tadeu Galante Rocha de Vasconcelos, Maria Julia Vilani Naman, Einat Hauzman, Jerome Baron, Dora Fix Ventura and Daniela Maria Oliveira Bonci (2019), *LWS visual pigment in owls: Spectral tuning inferred by genetics*, Vision Research 165: 90–97. DOI: https://doi.org/10.1016/j.visres.2019.10.001. PMID 31706045; publisher PII S0042698919301841; OpenAlex W2985825623. The original abbreviated author list identifies these six authors; MEDLINE indexes Dora Fix Ventura as Fix Ventura D. No author substitution is needed.

Bibliographic identity and the complete abstract were read from the Europe PMC MEDLINE API response for PMID 31706045:
https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:31706045%20AND%20SRC:MED&format=json&resultType=core

Cross-checks:
- https://pubmed.ncbi.nlm.nih.gov/31706045/ (indexed bibliographic record and abstract retrieved by search; direct page returned a disclosure footer).
- https://www.sciencedirect.com/science/article/pii/S0042698919301841 (indexed publisher abstract and Table 3 retrieved by search; direct page returned HTTP 403).
- https://openalex.org/works/W2985825623 (work page opened; six authors, year, title and DOI agree).
- https://pubmed.ncbi.nlm.nih.gov/31678618/ and https://www.sciencedirect.com/science/article/pii/S0042698919301877 (indexed records identify the incorrect DOI as Dickinson, Green, Harkin, Tang and Badcock, *A new visual illusion of aspect-ratio context*, Vision Research 165: 80–83, 2019).

The opened MEDLINE abstract names Tyto furcata among the five sequenced species and among the four examined by immunohistochemistry. It assigns approximately 537 nm to Athene cunicularia and approximately 555 nm to the other studied species. This is a prediction from LWS opsin tuning-site sequences. Immunohistochemistry confirms L-cone presence, not the spectral peak. The full paper's methods and tables were not independently opened; access stays abstract and partial stays true. This correction retains value 555, species scope, method, conditions, quote and grade g. It does not infer behavioural colour vision or whole-eye spectral sensitivity.

## Application and provenance

- The original `docs/views/evidence/sweep-30.jsonl` remains byte-for-byte unchanged.
- `docs/views/recheck/recheck-owl-lws-2486.jsonl` records action correct, supersedes sweep-30:2, and the verified reason.
- `docs/views/evidence/recheck-owl-lws-2486-fixed.jsonl` is the active replacement, linked by rechecked. Only the citation DOI and verification note change, besides the correction unit/marker.
- An appended retract row in `docs/views/audit/ALL.jsonl` retires the superseded copy for evidence consumers. Here retract means replacement of this copy, not withdrawal of the observation. Its reason links the replacement and both findings. Existing audit rows are untouched.
- The triage entry links this correction without erasing the original finding.

Repository-wide search for the exact wrong DOI found only sweep-30:2 and the two historical findings files. No other evidence record, wanted entry, generated description or source index cited it. Existing oa-4 owl records, their recheck copies and sources/oa-none-4 already use the correct DOI and are unchanged. The same article's wanted/web-birds:46 omitted the DOI: the verified identifier and genetic-inference qualification are now added there and in its single wanted-merged.csv row. Other wanted papers, download status, ranking, species and scientific claims are unchanged. The CSV retains its existing CRLF format.

## Validation and precision audit

Passed:
- `python3 -I tools/senses/check.py docs/views/evidence/recheck-owl-lws-2486-fixed.jsonl`: 1 record, 0 problems.
- `python3 -I tools/views/oa_lint.py docs/views/evidence/recheck-owl-lws-2486-fixed.jsonl --text /tmp/owl-abstract.txt`: 1 record, 0 faults; text is the opened MEDLINE abstract with HTML tags removed. Temporary source text is not committed.
- `python3 -I tools/views/test_apply_audit.py`: ok.
- `python3 -I tools/views/test_rows.py`: ok, using its stand-in API; no live generation call.
- Applying ALL.jsonl to the original sweep-30 log in a temporary output retires exactly its second row and retains its first.
- Direct rows.py evidence-loader check: wrong DOI absent; replacement loaded exactly once; original scientific fields unchanged.
- Independent main-only gaps.py evidence-loader check: wrong DOI absent; replacement loaded exactly once. This check does not certify the unrelated research branches.
- Wanted JSONL and CSV agree; JSONL parse and diff whitespace checks pass (`git -c core.whitespace=cr-at-eol diff --check`).

Full `python3 -I tools/senses/check.py`: 182 files, 25,044 records, 9 problems. All nine already exist on the base commit: intake-4-failed.jsonl has six missing DOI/URL fields and intake-5-failed.jsonl has three. Both baseline files were checked separately and reproduce these counts. No new validation problem is introduced; failed intake data are outside this correction.

An independent reviewer checked every new scientific record (the complete batch of one), bibliographic identity, abstract support, preservation of scope/grade/uncertainty, supersession and wanted consistency: 0 errors / 1 record = 0%, below 5%. This is a census of this small correction batch, not a new estimate for the whole repository; earlier audit totals and acceptance thresholds are unchanged. No app build or deployment is part of this evidence-only correction.
