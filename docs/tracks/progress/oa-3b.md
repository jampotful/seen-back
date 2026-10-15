# OA batch 3, second pass (entries 37, 42, 46, 52, 56, 58, 70)

Research pass dated 2026-10-15 on `research/oa-3b`. Seven entries checked; no free copy was read and no evidence records were logged.

- Closed by OpenAlex (title or DOI search): entries 37, 42, 58 and 70.
- Entry 46 (Brischoux et al. 2010) has a bronze Wiley link listed by OpenAlex, and entry 52 (Casalia et al.) has a green figshare copy. WebFetch could not retrieve either, so neither was read.
- Entry 56 (Schiviz et al. 2008) was not looked up: OpenAlex and Europe PMC both returned HTTP 429 and the proxy asked that they not be requested again.
- Europe PMC and Semantic Scholar were not reached for the other entries because of the same rate limit, so every line in `oa-none-3.jsonl` records the services actually checked.
- Entries 46, 52 and 56 are worth retrying from a session with direct network access.
