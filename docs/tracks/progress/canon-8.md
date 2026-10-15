# canon-8 progress (15 October 2026)

Logged under unit canon-8 (docs/views/evidence/canon-8.jsonl):
- Johnson RA, Rutowski RL 2022, PLoS ONE 17(9): e0257779, DOI 10.1371/journal.pone.0257779 (the article behind Dryad 10.5061/dryad.nzs7h44v8), Europe PMC full text PMC9499225: 26 species rows, trait diel, from Table 1 (foraging time). Table cells were fetched as separate pieces, so each quote is the species cell and the foraging-time cell joined with " | ".

Not opened:
- Dryad 10.5061/dryad.nzs7h44v8 files (S3 to S8, .sav): the API gives the file list, but the file download fails through the fetch tool (client error), so interommatidial angle per species was not read. The paper's own text has the angles only in Figures 11 and 12 (bioRxiv version), not in a table.
- Proc R Soc B 2020, DOI 10.1098/rspb.2020.1393 (PMC7542830): Table S1 sits in the supplementary PDF (figshare article 12922196, file 24584882, 9 MB). The download redirects to a signed S3 URL that the fetch tool refuses (URL too long). The main text names species only for habitat in the Figure 1 caption, with no activity period, so nothing was logged. The publisher page and doi.org also failed to load.
- Dryad 10.5061/dryad.3xsj3txq7 (Ausprey and Ritland; related articles 10.1098/rspb.2021.0853 and 10.1111/1365-2656.14141): the API gives no file list and the download link fails. Not read.
- Dryad 10.5061/dryad.4b8gtht8x (related article 10.1093/aob/mcae121): no file list, download not available. Not read.
- PMC pages return a captcha or are disallowed to the fetch tool; Europe PMC REST worked between 429 responses.
