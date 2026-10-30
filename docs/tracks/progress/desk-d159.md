# desk-d159 progress (animal vision vein, third pass)

Method: grepped main (evidence, audit/corrected, audit/ALL, searched, wanted) by species and DOI before reading; licence read from Crossref (CC BY URL) before opening the text; every quote reassembled from consecutive WebFetch pieces and checked on a second fetch.

Records: 10 in docs/views/evidence/desk-d159.jsonl, all lambda_max_nm, grade m, from 3 papers, check.py 0 problems.
- Savelli et al. 2018, Sci Rep 8:4763, 10.1038/s41598-018-23008-y (CC BY 4.0, Crossref; PMC5859124 copy): Platichthys stellatus large juveniles, MSP: S 459, M 526, M 548, L 557, rod 517 nm. The S 445 and M 536 pigments are described by the paper as mixtures of two pigments and are not logged. Accepted status of the name is not confirmed by a status line (FishBase 4249 and the GBIF species page show it as a main entry; WoRMS REST blocked).
- Stieb et al. 2019, Sci Rep 9:16459, 10.1038/s41598-019-52297-0 (CC BY 4.0, Crossref): Amphiprion akindynos MSP: rod 498, double-cone members 520 and 498, single cones 400 (the paper's own opsin estimates 370/408 do not match 400; stated in the note). The one-cell LWS value (541 nm, n = 1) is not logged. MSP details are in the Supplementary Information, not read.
- Garm et al. 2016, Front Physiol 7:99, 10.3389/fphys.2016.00099 (CC BY 4.0): Copula sivickisi ERG spectral sensitivity fitted with an opsin template, peak 458 nm (equal-quanta series 410 to 680 nm). A fitted template peak, not a pigment measurement; said so in the record.

Held out:
- Chappell and Speiser 2023 JEB 226 jeb244710 (Acanthopleura granulata, behavioural 6 deg): Crossref licence is the Company of Biologists user licence, not Creative Commons.
- Campbell and Loew 2024 (Anolis oil droplets, 10.3389/famrs.2024.1410763): already on main (oa-2).
- Streets et al. 2022 JEB 243699 (Haptosquilla, Gonodactylus), Chung and Marshall 2017, Garm 2016 acuity/cff, Stieb fovea (jeb.193334): on main.
- Graphium sarpedon (fevo.2016.00018): on main (sweep-28, canon-3).
- PMC6665397, PMC4795032: PMC returned a browser check; not worked around, not read.
- Dragonfly (Sympetrum/Libellula) interommatidial leads: results were old Springer/JEB papers with no open licence statement and two library-proxy hosts (not opened).
- Toad ganglion-cell acuity (Bufo gargarizans, Vision Res 2021): only catalogue records surfaced; no licence seen, not read.
- Searches for Dytiscus/Thermonectus, Lithobius, Dolomedes/Tegenaria, Centruroides, loliginid squid and mantis-shrimp morphology returned nothing open and not already on main.
- nature.com, GBIF API and WoRMS API fetches were refused by the permission layer; curl to GBIF returned a proxy 403; none worked around.

No search records or wanted lines written.
