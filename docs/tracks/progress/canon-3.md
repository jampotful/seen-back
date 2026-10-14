# canon-3: logging open-access canon compilations, round 2 continued (14 October 2026)

Worktree /tmp/wscanon3, branch research/canon-3. Evidence goes to docs/views/evidence/canon-3.jsonl, wanted lines to docs/views/wanted/canon-3.jsonl (none of the nine in wanted/canon-2.jsonl repeated).

## Route
Following canon-2's notes: WebFetch only; PMC serves reCAPTCHA, eLife a JS challenge, doi.org and Springer gave 429. Trying repository PDFs, publisher open-access pages, bioRxiv full text first.

## Status by compilation
(started 14 October; see below)
- 10.1242/jeb.143883 stereopsis review: silverchair PDF read in full; no table; 10 species/genus statements logged (depth_cue). DONE.
- 10.1098/rstb.2009.0039 Jacobs 2009: ResearchGate PDF read in full (PMC = reCAPTCHA); Table 1 (34 genera, cone complements) and 5 text λmax records logged. DONE.
- 10.1098/rstb.2009.0044 Hunt 2009: royalsocietypublishing.org fetch failed; UCL Discovery has no file. WANTED.
- 10.1007/s10336-007-0213-6 Martin 2007: Illinois State PDF read in full; no table; Appendix 2 (32 species with field type) and 5 text values logged. DONE.
- 10.1017/S1464793102005985 Kelber 2003: Lund repository PDF (truncated past section VI but both tables read); Table 2 (behavioural colour vision, 88 species records) and Table 1 (receptor maxima, 58 records) logged. Quotes are rows as extracted; q-marks are the fetch tool's reading. DONE.
- Briscoe & Chittka 2001 (no DOI in canon.jsonl; 10.1146/annurev.ento.46.1.471): Chittka lab PDF; Table 1 read whole (about 158 rows); 302 records (λmax and receptor count per row). DONE.
- 10.1098/rspb.2020.1393 Thomas 2020 frogs: NSF PAR full text read; no species table in the main text (all per-species data in ESM table S1 / Dryad 10.5061/dryad.1zcrjdfq7); nothing logged. WANTED (canon-3 line).
- 10.1007/s00239-004-0294-2 Lariguet 2005: rero PDF read in full; no main table (supplement is an accession list); 8 species statements logged (sense_light_nonvisual, g). DONE.
- 10.3389/fpls.2015.00207 Weller & Ortega 2015: Frontiers HTML (truncated after Table 2); Table 1 is loci, not species; 12 records (photoperiod class per crop species, two gene records). DONE.
- 10.1007/s00359-007-0281-3 Necker 2007: author PDF read in full; Table 1 is by order (garbled columns); 25 records (species sentences m, family/order g). DONE.
- 10.5772/intechopen.74645 Hauzman 2018: IntechOpen HTML read in full (no 429 this time); Tables 1, 3, 4 (12 colubrid/dipsadid snakes plus two Philodryas) and 11 introduction statements logged, 51 records. The fetch tool re-headed the tables; values are the chapter's. DONE.
- 10.1016/j.tree.2009.09.010 Heil & Karban 2010: agrilife PDF read in full; Table 1 (14 plant species) logged. DONE.
- 10.1111/ele.12205 Karban 2014: eScholarship PDF read in full; no table (Table S1 in SI); 32 receiver species from Figure 1 labels logged as partial. DONE (SI not needed for the view).
- 10.1017/S0952523813000035 Nilsson 2013: Cambridge PDF read (truncated in references); only a parameter table; 7 group/genus eye_type statements logged. DONE.
- 10.1093/molbev/msw265 Emerling 2017: OUP PDF refused, paperity abstract only. WANTED.
- Healy 2013 (10.1016/j.anbehav.2013.06.018): TARA (TCD) bitstream read in full; Table 1 (34 species CFF) logged. figshare ndownloader needed a permission not granted. DONE.
- Futahashi 2015 dragonflies: PMC blocked; AIST press release only. WANTED.
- Hall 2012 eye shape (no DOI in canon; 10.1098/rspb.2012.2258): Royal Society routes refused. WANTED.
- 10.1038/ncomms8852 phytochrome diversity: nature.com HTML (truncated in Methods); no main table (species counts in Supplementary Tables 1-2); 7 statements logged (g). DONE for the main text.
- Brischoux 2010, Land 2015 (Springer paywall, no 429), Heesy & Hall 2010 (Karger refused), Hunt & Peichl 2014, Ollivier 2004 (Wiley refused), Warrant & Johnsen 2013 (cell.com refused): WANTED.
- Not attempted: 1KP (10.1038/s41586-019-1693-2; no species-trait table in the main text), Land 1997, Rutowski 2009, Hughes 1977 chapter, Heesy 2011, books.
- 10.1016/j.asd.2008.08.003 Rutowski 2009: Lund record abstract-only. WANTED.

## Stopped (14 October)
No 429 and no search-budget notice; stopped after the open-access list was exhausted. 724 records from 14 compilations in evidence/canon-3.jsonl (check.py: 0 problems); 12 wanted lines in wanted/canon-3.jsonl. Routes that worked this round: Lund lucris, Chittka lab, Illinois State, reinhold-necker.de, agrilife.org, eScholarship PDF, TARA (tcd.ie) bitstreams, NSF PAR, IntechOpen HTML, ResearchGate link PDF, silverchair PDF, Cambridge aop-cambridge-core PDF. Refused: royalsocietypublishing.org, academic.oup.com, cell.com, karger.com, onlinelibrary.wiley.com, figshare ndownloader (permission), PMC (reCAPTCHA).
