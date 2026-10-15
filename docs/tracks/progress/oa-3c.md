# oa-3c: entries 46, 52, 56 of batch 3 (2026-10-15)

No records logged and no source or oa-none lines written, because no free full text was opened and no second service confirmed absence.

- Entry 46, Brischoux, Pizzatto and Shine 2010: OpenAlex lists the Wiley publishedVersion (onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1420-9101.2010.02046.x) as open access, but the fetch failed with a generic error and doi.org returned HTTP 429. The Macquarie page shows no file. The paper is unread and still needed; a retry of the Wiley link later is worth one attempt.
- Entry 52, Casalia et al. 2021: OpenAlex lists a Figshare deposit (article 13521423, CC BY, file temu_a_1857652_sm9482.pdf, probably supplementary material) and the CONICET handle 11336/172826 is restricted access. The Figshare file redirects to a signed, ten-second S3 URL that the fetch tool rejects as too long, and the proxy blocks curl. oa-none-4 already holds a line for this DOI. Unread.
- Entry 56, Schiviz et al. 2008: OpenAlex shows no open location (closed, both locations is_oa false). Europe PMC returned HTTP 429 and Semantic Scholar errored, so only one service was reached and no oa-none line is written.
