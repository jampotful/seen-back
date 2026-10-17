# oa-9 progress

## 2026-10-16

This round: all56 assigned entries received EuropePMC REST discovery and title-keyword web/repository searches before full-text reading. OpenAlex, Semantic Scholar and Crossref were excluded after round-wide rate limits; publisher and repository refusals in `work/round-services.json` were honored. No app checks ran.

Completed requested items:2. Entry3 is the requested NHM January2022 DATASET release: all1293 CSV rows plus full ReadMe and reference DOCX were retrieved and parsed. Its ledger note explicitly distinguishes this release from the published1294-species article and does not claim the associated paper/OUP supplements fully read. Entry4 is the complete five-page nocturnal-bee paper; the Smithsonian ORIGINAL bundle contains only that PDF and the paper cites no supplement. One paper fully read plus one requested dataset complete.

Evidence added:2122 records, including2033 conservative g dataset records (1293 adult pupil classifications,92 larval pupil classifications,648 binary activity categories),7 bee records,41 dragon-lizard main-text records, and41 abstract-only records. All new quotes pass quotecheck against the actual downloaded/extracted source; schema validation passes. Dataset rows preserve original attributions and raw classes, with no inferred ancestral states, no NA converted to observations, and no larval `none` converted to pupil absence. Non-diurnal is a binary category combining arrhythmic/cathemeral/crepuscular/nocturnal and must not become nocturnal. Four bee corner frequencies are actual species/adaptation measurements, not flicker fusion. Abstract records carry `partial:true` and `source.access:abstract`; none enter the full-read ledger.

Terminal discovery outcomes:34, comprising23 limited-source no-free-copy outcomes,8 known-free inaccessible outcomes and3 unresolved lookups. Every row names its actual limited checks and limitations; none retires an owner wanted item or marks a full read. New refusals reported to root: `www.coraciiformestag.com` HTTP403 and `www.ski.org` HTTP406. Other actual retrieval failures: SCIRP503, RNGR502, Adelaide indexed thesis item404, EuropePMC fullTextXML500 for26/50/53. Springer6 PDF request returned subscription/abstract HTML, not a PDF.

Pending20 entries:5,8,9,15,17,18,19,23,26,34,35,36,38,39,41,43,48,50,51,53. Entry5 main text is read and41 records logged, but statistical supplement TableS1 remains unavailable, so its full-read ledger is withheld. OUP supplementary parts A–F for the article associated with dataset3 remain unread and separate from the completed requested dataset. Accessible cached unread papers remain pending, never skipped for time.

Resume from these actual files and metadata:
- Paper PDF/XML/full text is only under `/tmp/oa/oa9`; no papers or full text were committed. PDF main files4,5,8,15; XML9,17,18,19,23; additional PDFs34,36,51. City published main for3 is `03-city.pdf`; requested dataset files are `03-amphibian_pupils.csv`, `03-readme.docx`, `03-references.docx`.
- Discovery and URL/status metadata/scripts are under `work/oa9`: `discovery.txt`, `main-urls.json`, `more-urls.json`, `retrieval.txt`, `more-retrieval.txt`. ANU item pages for43/48 are cached HTML;41 has an OpenPrairie record,35 an OhioLink thesis candidate,38 an UNESP record,39 indexed reagent-company/conference PDF candidates. These require actual legal retrieval and reading before completion.
- Next work: finish supplement availability for5; read8 with any free supplements; read9 with its free species-data supplements. Recheck the shared refusal list before fetching another host.

Commits this round before final status update:5fc7a9f6,dc76e18e,4eb99a22.
