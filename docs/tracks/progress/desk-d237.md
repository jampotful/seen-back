# desk-d237

Desk unit d237, 31 October 2026. About 38 WebSearches; 4 records in docs/views/evidence/desk-d237.jsonl (check.py: 4 records, 0 problems).

## Records
1. Poecilia parae, lambda_max_nm, rod 503 nm (MSP), Hurtado-Gonzales, Loew, Uy 2014, PLoS ONE 9(7) e101497, 10.1371/journal.pone.0101497. Whole Results sentence.
2. Poecilia parae, lambda_max_nm, UV single cone 355 nm, same paper. Quote cut after the value (marked).
3. Poecilia parae, lambda_max_nm, double cones 456 to 553 nm, same paper. Quote cut after the range (marked).
4. Gasterosteus aculeatus, erg_peak_nm, 500 nm most sensitive of nine tested wavelengths, Shao et al. 2014, PLoS ONE 9(6) e100330, 10.1371/journal.pone.0100330. Quote cut after "500 nm" (marked); flagged "new trait key" in note because check.py lacks erg_peak_nm although main uses it. Retries the held "stickleback" lead.

## Held leads and why
- Walleye (peerj.21156): peerj.com client error again.
- Amalosia lesueurii (fevo.2021.727602): tool again cannot return the Results sentence whole; the topic is preferred body temperature after feeding, not thermal sensing. Not filed.
- Budgerigar brightness discrimination (pone.0054650): the Results sentence is cut before "at 72.5% correct choices", which is a qualifier of the 0.09 threshold; the abstract sentence is cut too. Not filed.
- Hatchetfish photoreceptor density (fevo.2016.00025, receptor_density_mm2): peak sentences continue with "however, A. sladeni showed the highest peak density", n = 1 retina per species, page has no licence sentence and the Crossref lookup was rate limited. Not filed.
- Neoconocephalus triops (biology 13(12) 1026, phonotaxis preferences): behaviour preference, F1 lab-reared, multi-condition; trait fit to sense_hearing doubtful.
- Snakes airborne/groundborne sound (pone.0281285): genus-level results, text inconsistency on Oxyuranus, correction issued 2025.
- Ictalurus nebulosus electroreceptors (pone.0032786): name is a synonym of Ameiurus nebulosus; sentences long.
- Melanophila IR model (pone.0037627): modelled, genus level. Helicops scale sensilla (famrs.2024.1412004): preserved specimens, no numbers. Anuran playback of tit alarm calls (ani 12(24) 3537): null behaviour, not a hearing measure. Lateral-line cichlid cfos paper (fnbeh.2016.00093): multi-endpoint, no clean single value.
- Searched and found already on main or d229 to d236: most fish ABR/AEP, ERG-insect, tick and mosquito thermal papers, Anolis/rats acuity.

## Owner questions
- check.py TRAITS lacks erg_peak_nm, erg_spectral_peak_nm, receptor_density_mm2 and other keys used on main; should the list be extended so units need not write "new trait"?
- Is a quote cut after the value (trailing " …") acceptable when the dropped text is a per-class n or a flux value? Records 2 to 4 rely on it.
- Crossref was reachable only through WebFetch (curl refused by the proxy).
