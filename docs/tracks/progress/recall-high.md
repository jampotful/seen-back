# Search recall test — high

Found evidence for **9 of 10 cells**, with 11 value records. `Onitis / interommatidial_deg` remains `found: []`.

The literature-search phase took approximately **25 minutes**, timed from the first scholarly API searches through writing these results. Initial workspace startup, updating the stale checkout and reading the instructions preceded that timer.

The search was blind: the only file read under `docs/views/` was `research/THOROUGH.md`. Scientific-name and English-name queries used OpenAlex and Europe PMC, with up to the first 25 results and their available abstracts screened; each cell also has an OpenAlex citation check. Further sources were followed through references. OpenAlex searches used the connected Mac after the cloud network's shared anonymous search budget was exhausted; free DOI lookups also worked in the cloud. Crossref confirmed journal DOIs/titles, and DataCite confirmed the thesis DOI/title.

Evidence details:

- `Chelostoma` and `Xiphydria`: measured species-level wavelengths reproduced in the open Annual Reviews supplement, with worksheet rows and source attribution recorded in `where`. Quotes are literal spreadsheet cell contents.
- `Cupiennius`: three spectral photoreceptor classes from the retrieved 1996 intracellular-recording abstract. `Vanessa`: three visual-pigment classes from the retrieved 2003 abstract.
- `Octopus`: 72 Hz is explicitly a pooled mean for *O. vulgaris* and *O. briareus*, at the stated stimulus intensity.
- `Phidippus`: anatomical resolution for *P. johnsoni*. The source reports an approximately 8 arcmin inter-receptor angle; approximately 3.75 cycles/degree is an explicit Nyquist conversion, 60/(2×8), rather than a directly reported cpd threshold.
- `Phelsuma`: the open thesis histologically describes the adult *P. laticauda* fovea. `Ovis`: the EFSA review reports a binocular-field range of 4–77° for sheep.
- `Onitis`: relevant papers and an open thesis were located, but no numeric interommatidial angle was verified. The acceptance-angle measurement in the maturation paper was excluded because it measures another trait. The null records a retrieval result, with source-access limitations documented in `where`.

All retained quotations were checked against the retrieved abstracts, worksheet cells or extracted source text, and are at most 40 words. PDFs and working files stayed outside the repository. App setup, builds, servers and app tests were skipped. Only the two requested `high` result files were written in the repository.
