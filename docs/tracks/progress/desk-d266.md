# desk-d266 progress note

Records filed: 0 (no evidence file created).

## Channel test (WebFetch only, no curl, no workarounds)
- api.crossref.org/v1/works/10.1242/jeb.249422 (single DOI): ACCEPTED. Returned title, authors (Kawamoto, Perez i de Lanuza, Vie Giner, Brejcha, Font), JEB 228(8), licence entry http://www.biologists.com/user-licence-1-1/ (vor, start 2025-04-15), and link entries to the publisher PDF https://journals.biologists.com/jeb/article-pdf/doi/10.1242/jeb.249422/3645947/jeb249422.pdf.
- api.openalex.org/works?search=...: REFUSED (PROVENANCE_REQUIRED; permission request unanswered).
- journals.biologists.com PDF URL (seen in Crossref output): REFUSED (PROVENANCE_REQUIRED; so a URL appearing in Crossref output does not unlock it in this session).
- doaj.org/api/search/articles/...: REFUSED (PROVENANCE_REQUIRED).
- api.semanticscholar.org/graph/v1/paper/search: REFUSED (PROVENANCE_REQUIRED).
- api.crossref.org/works?filter=prefix:10.1242,...&query=... (list query, retried once after the refusals): failed at site (client_error), nothing retrieved. Not retried with variants.
After the OpenAlex refusal every later new-host request returned "earlier permission request not answered"; I did not retry or route around any of them.

Conclusion: only single-DOI Crossref lookup works as a metadata channel, and it cannot discover candidates (a DOI must already be known from a search result). No usable discovery channel; no publisher page could be opened, so no record was read or filed. WebSearch fallback not run (session permission state blocked fetches).

## Held leads
- 10.1242/jeb.249422 (Podarcis muralis visual acuity, JEB 228(8)): Crossref confirms vor licence (biologists user-licence-1-1, not CC), publisher PDF unopened. Licence is not an accepted open licence unless the page prints a CC sentence or is the publisher's free full text; retry only if the PDF URL appears in a search result and the page is free to read.

## Owner questions
- Approve api.openalex.org, doaj.org, api.semanticscholar.org and journals.biologists.com for WebFetch if these should be tested properly.
