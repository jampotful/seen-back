# OA batch 6

## 2026-10-14

First-pass metadata lookup attempted for all 79 assigned entries. OpenAlex returned 429 after three successful DOI responses (entries 1, 2, 4); the first title search, entry 3, was refused. Semantic Scholar returned 404 for entry 1 and 429 for entry 4; further calls to either refusing host were stopped. Europe PMC successfully answered 56 DOI queries. These API failures are unresolved searches, never evidence of no free copy.

So far: 79 papers checked or attempted; 6 candidate free XML texts found; 2 papers read fully; 133 records logged; 1 paper with no free copy (entry 2, book chapter, successful OpenAlex-only check permitted by the prompt). Entries 1 and 3–31 remain unresolved, including entry 4 whose OpenAlex response marked the JEB paper closed. No negative marker has been written for these entries.

Completed entry 32, Lu and Kronforst, *Cellular innovations and diversity in the lepidopteran compound eye*. Read the full Europe PMC XML, all six figures, and the supplementary XLSX retrieved from Europe PMC's supplementaryFiles endpoint. All 47 quotes passed quotecheck. Records are explicitly secondary review evidence and conservatively graded g; physiological spectral classes are distinguished from behavioural colour dimensionality. Supplementary table S1 lists opsin gene copy counts, not measured receptor-class numbers; these were not equated. No full text, PDF, XML, image, or spreadsheet was committed.

Completed entry 40, *Ultra-rapid vision in birds*: full XML, figures, spectral-stimulus PDF and individual-level CSV read. Added 86 quotechecked records (6 species summaries, 75 individual luminance-specific thresholds, 5 explicitly secondary comparative values). Main-text mean CFF values supersede the inconsistent rounded abstract means; individual threshold records preserve luminance, sex, season, and bird ID. The supplementary movie illustrates sampled fly trajectories and supplies no additional measurement.

Next free texts in order: entries 58 (PMC13038772), 59 (PMC2203092), 62 (PMC3791410), 72 (PMC2855400). Entry 59's XML appears abstract-only and requires a legal scan before any full-read marker. Current downloads and raw lookup responses are under /tmp/oa/oa6 (ephemeral, not committed).
