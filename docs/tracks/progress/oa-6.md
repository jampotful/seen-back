# Open-access pass, batch 6

Updated 14 October 2026. Work follows `AGENTS.md` and `docs/tracks/prompts/oa-pass.md`. No app setup, build, server or app checks were run. Lookup responses, downloaded papers, extracts and temporary scripts stay outside the repository under `/tmp/oa/6`.

- Papers in batch: 79. Lookup pass attempted for all 79.
- Papers with indexed free-copy candidates: 20.
- Papers read in full and marked read: 7.
- Evidence records logged: 436; 100 are explicitly abstract-only.
- Papers with no free copy located by completed lookups: 24.
- Incomplete lookups: 35.
- Indexed free-copy candidates that could not be read: 13.

OpenAlex returned HTTP 429 at batch index 34 (owner rank 430); further requests to that host stopped. Europe PMC and Semantic Scholar were still checked for supplied DOIs. No-DOI entries require a matching OpenAlex title, first author and year before a DOI is accepted. Incomplete and inaccessible statuses are distinct from `no free copy`; none is marked read. Publisher HTTP 403 responses, broken links, bot-check pages, and Europe PMC HTTP 500 responses were retained as access failures.

Completed full reads:
- Cellular innovations and diversity in the lepidopteran compound eye: 67 records.
- The scaling of eye size with body mass in birds: 0 records.
- Ultra-rapid vision in birds: 86 records.
- Night light-adaptation strategies for photosynthetic apparatus in yellow-poplar (Liriodendron tulipifera L.) exposed to artificial night lighting: 79 records.
- Praying mantises possess multiple spectral photoreceptor classes: 49 records.
- Spectral Sensitivity Studies on the Visual System of the Praying Mantis, Tenodera sinensis: 20 records.
- Metabolic rate and body size are linked with perception of temporal information: 35 records.

The butterfly review records are secondary evidence with original-study attribution. Opsin gene counts in its supplementary table were not treated as receptor-class measurements. For the rapid-vision bird paper, the raw supplemental FFF values agree with main-text means, which differ from the abstract.

This pass has finished every retrieved readable full paper. All 436 final evidence quotes passed `quotecheck.py`; `addlog.py` validated each record before appending it. Only the four batch 6 output files were changed, and no paper PDF, XML, extracted text, raw dataset or temporary script was added to the repository.

The recent mantis paper’s 16 public Figshare files were retrieved, including normalized ERG curves, reflectance spectra, morphometry and the README. Table 1’s fixed peaks and model contributions were logged; raw normalized curves were not recast as absolute thresholds or behavioural colour vision. The 1971 mantis scan and bird eye-size scan were recovered through Europe PMC’s PDF service after their XML responses proved unusable. No record or source is labelled an accepted manuscript because the copies used were published versions.

Follow-up work:
1. In a later task, complete the 35 incomplete lookups once OpenAlex allows requests again; preserve the title/first-author/year rule for papers without DOIs.
2. Revisit the 13 inaccessible candidates through their legal publisher or repository routes. The Figshare candidate for the Vicia faba paper contains no attached files; a metadata record is not a free full-text copy.
3. Have the research desk sample the evidence, especially model-inferred mantis receptor classes, the butterfly review’s secondary peaks, and the cat ERG attribution in Healy et al. Table 1. Nothing was merged to main and no pull request was opened.
