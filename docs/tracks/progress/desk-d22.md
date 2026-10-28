# desk-d22 (plant genera Salix to Pinus; web fetches mostly blocked)

About 33 WebSearches and 25 WebFetches used. Many publisher, PubMed and PMC pages returned a bot check, client_error or a permission request (PROVENANCE_REQUIRED) and were not retried; search results gave titles only.

## Recorded (docs/views/evidence/desk-d22.jsonl, 4 lines)
- Pinus sylvestris sense_chemical, Hilker et al. 2002 (JEB 205: 455, 10.1242/jeb.205.4.455): sawfly-egg-induced volatiles attract the egg parasitoid; full Results text (Silverchair copy). Closes wanted lead harvest-c13.
- Pinus sylvestris sense_chemical, Lundborg et al. 2016 (10.1007/s10886-016-0790-z), PMC full text: methyl jasmonate spray, beta-pinene up in phloem, total basal-phloem monoterpenes not up. Journal not shown on the page, so left out of the record.
- Salix cinerea sense_chemical, Mrazova and Sam 2017 (10.1007/s11829-017-9558-9): 30 mM MeJA spray; abstract only.
- Daucus carota sense_chemical, Fatelnig et al. 2026 (Planta 263: 35, 10.1007/s00425-025-04900-0): gibberellin/ABA priming of mericarps; abstract only.

## Search records
None written. Findings that decided this:
- Hemerocallis, Chromolaena, Cichorium, Larrea and Salix already have eye_type search records on main (desk-d4, desk-c12) with the same two-query shape; I wrote duplicates first and withdrew them before committing the final state. Eye_type cells stay open on the queue whatever search records exist (canon step), so another null adds nothing.
- Asparagus has no open trait in the harvest view (fully searched).
- Chamaenerion: the harvest shows "error gave up" on its first queries; skipped as the brief says.
- Cerastium, Larrea, Lotus, Castilleja, Daucus, Urtica, Salix light/diel: each open cell is held by a lead on main's wanted list (harvest-c12, c13, desk-c12, desk-d4), so no null was written.

## Leads tried and not recorded (no whole sentence of 125 characters or fewer on the measurement)
- Tussilago farfara, Bostock 1978 (Oecologia 36: 113-126, 10.1007/BF00344576): abstract says light, nitrate, alternating temperature and seed age all affected germination except in T. farfara (157-character sentence). Substance: no light effect on coltsfoot germination. A reader with the full text could log it.
- Lotus japonicus MeJA (Nakagawa and Kawaguchi 2006, Plant Cell Physiol 47: 176, 10.1093/pcp/pci222): shoot-applied MeJA suppressed nodulation; every abstract sentence over 125 characters.
- Pinus resinosa MeJA frost (Connolly and Orrock 2018, Botany 96, 10.1139/cjb-2018-0108): 1 mmol/L MeJA gave 18% less foliar damage; the MeJA sentences are 136 to 314 characters.
- Salix caprea diel (Jurgens et al. 2014, 10.1111/boj.12183): Wiley and OUP pages blocked.
- Daucus (Nissinen et al. 2005, 10.1021/jf0511897), Pinus sylvestris MeJA (Heijari et al. 2005), Larrea (Mahall and Callaway 1992; Barbour 1968; FEIS only repeats Barbour: germination about twice as high in darkness), Urtica trichome induction: pages blocked or no abstract returned.
- Not used: Larrea tridentata VOC emission paper (10.5194/acp-10-12191-2010), since emission rates are not a signal response.
