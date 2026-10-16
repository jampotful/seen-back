# Precision audit 20, 16 October 2026

Scope: 20 records from 14 evidence files that no earlier audit table, recheck file or retract row had touched: external-5 (2), external-6 (2), external-7 (1), canon-9 (1), oa-5 (2), reread-1 (1), sweep-18 (1), sweep-26 (2), sweep-33 (1), sweep-34 (1), sweep-39 (1), sweep-41 (1), sweep-42 (3), sweep-43 (1). Taxa: birds 5, insects 6, mammals 3, reptiles 3, plants 3. Seventeen at `m`, three at `g` before the audit.

Method as in audits 13 to 19: each source opened with WebFetch (WebSearch only to locate a paper or an open copy) and asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces. Metadata checked against the opened page or the journal's own record. A change to the partial flag, the grade or a bibliographic field counts as `correct`. Corrections are in `docs/views/recheck/recheck-20.jsonl` in the recheck-5 schema. No evidence file, no wanted file and not `docs/views/audit/ALL.jsonl` was edited.

## Table

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| external-5:1 | Ptilonorhynchus violaceus / lambda_max_nm 410.2 | m | confirm | Published paper opened (author copy on the Borgia lab site, science.umd.edu): Table 4, p. 1096, VS single cone 410.2 ± 2.8, N = 3, means ± 1 s.d. Matches the dissertation row logged. JEB 215:1090-1105 printed on the PDF |
| external-5:7 | Ptilonorhynchus violaceus / lambda_max_nm 503.1 (rod) | m | confirm | Same table: rod 503.1 ± 1.2, N = 11 |
| sweep-18:10 | Spizelloides arborea / acuity_cpd 7.03 | m | correct | JEB PDF opened. The quote was a summariser's paraphrase; Table 1 (species in columns) gives "Visual acuity (cycles/deg) 7.03". Requoted, method states the sampling-theorem estimate, `partial` to false, Fernández-Juricic restored |
| sweep-26:2 | Uria aalge / fov_h_deg | m | correct | NERC manuscript opened. Logged quote is a paraphrase and not in the paper; requoted to the Results sentence with "310 and 305° ... in the Puffins and Guillemots, respectively". 167° (plane of the optic axes) and axes 10° below horizontal confirmed. `partial` to false |
| sweep-33:16 | Rissa tridactyla / binocular_deg 35.1 | g | confirm | Tethys PDF: verbatim, "35.1° ± 1.2°", mean of all three gulls combined; n = 3 kittiwakes. Ibis 167(2):386-396 |
| external-6:1 | Tharsalea rubidus / lambda_max_nm 360 | m | confirm | JEB page: Summary sentence verbatim (λ for "lambda"). Full text is on the page; Results attribute 360 nm to epi-microspectrophotometry of eyeshine. `access: abstract` and `partial: true` are conservative; the journal field lacks volume and pages (209(16):3079-) |
| external-6:5 | Tharsalea heteronea / lambda_max_nm 360 | m | confirm | PMC51323 page: abstract sentence verbatim; both species named. Full text there is the scanned PDF, not read; `partial: true` stands |
| canon-9:1 | Orthetrum albistylum / opsin_gene_count 5 SW | g | correct | PMC4371951: abstract quote verbatim. Results: O. albistylum RNA-seq "yielded the same set of 20 opsin genes", so the SW count was measured in the species; canon-7:11 logs its total at `m` from the same sentence. Grade to `m` |
| sweep-26:6 | Oecophylla smaragdina / cff_hz 132 | m | confirm | JCU manuscript: abstract sentence verbatim; Results, Temporal resolution: 132 ± 3 Hz (mean ± s.e.m., n = 5); major workers stated in Results. JCPA 209:489-498 |
| sweep-42:1 | Adoxophyes orana / lambda_max_nm [344, 481, 533] | m | confirm | BMC PDF (PMC blocked): sentence verbatim but for "fn"; fit to dark-adapted Niigata ERG data, Results "Contribution of screening pigments". Zool Lett 3:14 |
| external-7:1 | Lasioglossum inconspicuum / interommatidial_deg 3.37 | m | confirm | NSF PAR copy: Table 1 row verbatim (Df 3.37, ref. 42). The numbered list behind "42" is in Table S2, not opened, so the note's attribution to Jander & Jander 2002 is unconfirmed (Perdita minima and Protoxaea gloriosa share ref. 42, which fits that paper) |
| sweep-34:2 | Ochotona princeps / lambda_max_nm ~430 (SWS1) | g | confirm | OUP page (PMC blocked): sentence verbatim; 430 nm is the mouse SWS1 carrying pika A86 and N93, said to recover the pika tuning; the wild-type pika value is not in the text. Record already says so |
| oa-5:5 | Vulpes vulpes / lambda_max_nm 555 | m | confirm | Abstract (openpolar.no Crossref record): "each has one cone pigment with peak sensitivity of about 555 nm", four species named one per genus, ERG flicker photometry. Per-species statement, so `m` from the abstract holds; `partial: true` right |
| oa-5:301 | Camelus dromedarius / cornea_diameter_mm 29.1 | m | correct | Journal PDF and abstract page: sole author Mohammad Ali Ebrahimi Saadatlou, not Karabag, Alkan & Mendes. Quote was a subjectless fragment; requoted to the whole p. 912 sentence. Value and 23(6):911-915 confirmed |
| reread-1:6 | Anolis carolinensis / cff_hz [33.0, 36.1] | m | unverifiable | Vision Research 1974, closed; no open copy found. Not reached by any other route |
| sweep-43:9 | Crotaphytus dickersonae / lambda_max_nm 359 | m | confirm | JEB PDF: Introduction sentence verbatim; Table 1 row "Crotaphytus dickersonae (Tiburon collared lizard) 359 MSP Macedonia et al., 2009" |
| sweep-42:6 | Psammodromus algirus / receptor_classes (oil droplets) | m | confirm | Same PDF: Results sentence verbatim; Methods list six species examined for droplets, P. algirus among them |
| sweep-41:11 | Echinocactus platyacanthus / sense_light_nonvisual | m | confirm | IPICYT repository PDF: sentence verbatim; Table 2 "90 ± 7.9 a 0 b Positive". J PACD 12:12-19 |
| sweep-39:1 | Sagittaria platyphylla / sense_light_nonvisual | m | confirm | MDPI: verbatim in 2.2; temperatures 15/5, 25/15, 30/20 °C. Plants 14(20):3138 |
| sweep-42:2 | Hemerocallis fulva / diel | m | confirm | MDPI HTML (PMC blocked): verbatim in 2.2; authors and 14(13):1996 confirmed |

**Rate: 4 errors in 19 verifiable records, 21%** (1 unverifiable). By verdict: 0 requote, 4 correct, 0 retract; 15 confirm.

## Checks

- **Quotes.** Two quotes were summariser paraphrases that appear nowhere in the paper (sweep-18:10, sweep-26:2); both came from files logged "through a summariser". One was a fragment without its subject (oa-5:301).
- **Metadata.** oa-5:301 named the wrong authors; the PDF also prints a "Karabag K, Alkan S, Mendes M" line that the logger must have taken for the citation. The journal's own record has one author.
- **Grade.** canon-9:1 was graded `g` for a count the Results state for the species; canon-9:2 to 9:4 carry the same reasoning (O. albistylum LW; L. fulva SW and LW, Results "identified the same set of 20 opsin genes") and should be raised to `m` with it; not separately rechecked here.
- **Partial flag.** No missing flags in this draw: the abstract-only records (external-6, oa-5:5) carry `partial: true`, and the open-text records were read in full.
- **Review tables.** external-7:1 and sweep-43:9 take values from review tables (Feller 2021, Pérez i de Lanuza & Font 2014); both name the primary source, and both values match the tables.

## Rows written

`recheck-20.jsonl`: 4 rows: sweep-18:10, sweep-26:2, canon-9:1, oa-5:301 (all `correct`).

## Blocked pages

- Robots disallowed: europepmc.org/article/MED/16888057 and /2011588.
- Rate limited (HTTP 429): pubmed.ncbi.nlm.nih.gov/2011588; www.ebi.ac.uk Europe PMC REST for 10.1242/jeb.02360 and 10.1073/pnas.88.7.2783; doi.org/10.9775/kvfd.2017.17976.
- PubMed 16888057 captcha.
- Permission step not answered: pmc.ncbi.nlm.nih.gov PMC5575869 and PMC10075062; api.drum.lib.umd.edu dissertation bitstream; zoologicalletters.biomedcentral.com article 10.1186/s40851-023-00205-w (Trachylepis, sweep-34:12, dropped from the draw).
- curl through the agent proxy returns 403 for Europe PMC, so WebFetch was the only route.
