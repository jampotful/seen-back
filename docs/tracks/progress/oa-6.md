# OA batch 6

## 2026-10-14

First-pass metadata lookup attempted for all 79 assigned entries. OpenAlex returned 429 after three successful DOI responses (entries 1, 2, 4); the first title search, entry 3, was refused. Semantic Scholar returned 404 for entry 1 and 429 for entry 4; further calls to either refusing host were stopped. Europe PMC successfully answered 56 DOI queries. These API failures are unresolved searches, never evidence of no free copy.

So far: 79 papers checked or attempted; 6 candidate free XML texts found; 4 papers read fully; 183 records logged (including 4 abstract-only records); 1 paper with no free copy (entry 2, book chapter, successful OpenAlex-only check permitted by the prompt). Entries 1 and 3–31 remain unresolved, including entry 4 whose OpenAlex response marked the JEB paper closed. No negative marker has been written for these entries.

Completed entry 32, Lu and Kronforst, *Cellular innovations and diversity in the lepidopteran compound eye*. Read the full Europe PMC XML, all six figures, and the supplementary XLSX retrieved from Europe PMC's supplementaryFiles endpoint. All 47 quotes passed quotecheck. Records are explicitly secondary review evidence and conservatively graded g; physiological spectral classes are distinguished from behavioural colour dimensionality. Supplementary table S1 lists opsin gene copy counts, not measured receptor-class numbers; these were not equated. No full text, PDF, XML, image, or spreadsheet was committed.

Completed entry 40, *Ultra-rapid vision in birds*: full XML, figures, spectral-stimulus PDF and individual-level CSV read. Added 86 quotechecked records (6 species summaries, 75 individual luminance-specific thresholds, 5 explicitly secondary comparative values). Main-text mean CFF values supersede the inconsistent rounded abstract means; individual threshold records preserve luminance, sex, season, and bird ID. The supplementary movie illustrates sampled fly trajectories and supplies no additional measurement.

Completed entry 58, *Praying mantises possess multiple spectral photoreceptor classes*: full XML, all three figures and Table 1 read, 11 verified records. These are dorsal-eye population-ERG/model peaks and candidate pigment components, never a behavioural demonstration of colour vision. Hymenopus UV has an internal discrepancy (Table 1: 352 nm; Fig. 3: 342); retained Table 1 and flagged it.

Entry 59: abstract read and 4 partial records logged with access abstract. XML has no body; its listed free Europe PMC PDF returned 403, and publisher DOI returned 503. It remains unresolved, with neither a full-read nor a no-free-copy marker.

Completed entry 62, Healy et al. 2013: full XML, all 34 species rows, appendix and six figures read. Logged 34 secondary CFF values and the cited tiger-beetle stop–start pursuit behaviour. Table method classes and typical habitat-light classes are kept distinct from measured test luminance; original cat/seal citation ambiguity is flagged.

Entry 72 (PMC2855400) is a free-copy candidate, but its fullTextXML route returned HTTP 500; retrieval remains unresolved. No paper text was read and no marker was written for it.

Pass finished between papers: 5 of 79 entries settled (2, 32, 40, 58, 62), with 74 remaining, including abstract-only entry 59. Remaining positions: 1, 3–31, 33–39, 41–57, 59–61, 63–79. Resume with API checks when hosts are available, and retrieve the known free copies for 59 and 72. Final counts this round: 79 checked/attempted; 6 candidate free copies identified; 4 full papers plus 1 abstract read; 183 records logged; 1 no-free-copy chapter. Counts include 75 individual bird thresholds rather than just species summaries. Current downloads and raw lookup responses are under /tmp/oa/oa6 (ephemeral, not committed).
