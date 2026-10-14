# OA batch 8 (14 October 2026)

Work is on `research/oa-8`. No app setup, builds, or app tests are run. Only this batch's evidence and source status files are committed. Copies and lookup responses stay outside Git in `/tmp/oa/8`; scripts are in ignored `work/`.

The lookup script processed all 79 batch entries before any paper was read. It located 24 candidate free copies; 11 full texts downloaded. OpenAlex returned HTTP 429 on paper 3: the shared unauthenticated daily budget is exhausted until midnight UTC. Per BRIEF, no further requests were made to that service. Subsequent DOI entries were checked with Europe PMC and Semantic Scholar; title-only entries could not be resolved. Several publisher hosts returned HTTP 403 and were not retried. Old PMC full-text links for papers 31 and 54 led to robot challenges; alternate Europe PMC XML requests returned HTTP 500. These limits do not establish that the papers are closed.

Read and logged in batch order through paper 35 (rank 588): full papers 16, 20, 33, and 35; partial abstract evidence from papers 6, 10, 17, 21, 24, 25, 27, 29, and 30. There are 61 records (27 full-text, 34 partial). Every quote passed `quotecheck.py` against the retrieved XML text, PDF, or abstract before `addlog.py` appended it. Paper 33's free supplement was read; it contains the amplifier circuit and LED emission curves, with no additional biological measurements. Paper 35's primer supplement is blocked (MDPI HTTP 403).

Strong findings include Bombus impatiens receptor peaks and separate temporal processing measurements; Halyomorpha halys has two detected receptor classes, while behavioural colour discrimination was not tested. Abstract evidence remains partial and does not remove papers from the wanted list. Receptor impulse timing in milliseconds is explicitly distinguished from flicker fusion in hertz.

Next: read accessible full papers 42, 65, 66, 67, 69, 72, and 77, with any accessible supplements; log useful abstract measurements from intervening papers; write all unresolved source statuses and the final summary. Paper 66 is a bioRxiv preprint and must be marked as such, not as the final journal version.
