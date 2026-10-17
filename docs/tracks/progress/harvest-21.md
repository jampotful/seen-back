# Harvest 21 progress (16 October 2026)

Branch research/harvest-21, 20 genera in the order given. The harvest data (run 2 for Medicago, run 4 for the rest) supplied every title and abstract start; harvest_get.py ran in about a second.

## What blocked the work
Every WebFetch call (publisher pages, repository pages, jeb.biologists.org, api.openalex.org) ended with "permission request not answered", and curl through the proxy was refused for api.openalex.org and the repository hosts. WebSearch returns links only. So no work was opened in full or from its abstract page, and no author byline or OpenAlex work record could be read. Under the audit rules that leaves no evidence records and no wanted lines (a wanted line needs authors confirmed from an opened page or the OpenAlex record). The harvest records carry no author field.

## Done
- 20 search records in docs/views/searched/harvest-21.jsonl (one per genus, traits grouped as in earlier harvest files), all `found` "none", each saying that the title and abstract start of every listed work were screened and none was opened.
- Medicago: diel and eye_type already have records (harvest-8, harvest-11), and M. truncatula is logged for sense_light_nonvisual (harvest-11), so only a sense_light_nonvisual search record was written. Oxalis was not skipped: harvest-13 logged only O. triangularis measurements, and no Oxalis genus search record existed.
- Cells closed by a measurement: 0. Wanted lines: 0.

## Not done
- sense_chemical for the plant genera (Medicago, Tussilago, Campanula, Daucus, Stellaria, Rumex, Dipsacus, Caltha, Primula, Hypericum): the harvest sent no query for it and the OpenAlex API was unreachable, so no hand query was run and no record was written. Those cells stay untouched.
- Coverage line (coverage.py) hung on this machine and was not run.

## Candidates for the next round (DOI from the harvest record; authors, volume and pages unconfirmed)
- Milvus migrans (cff_hz, fov_h_deg, interreceptor_deg): 10.1242/jeb.142083 (acuity, fovea, visual fields in black kite and Harris's hawk; open PDF at jeb.biologists.org/content/jexbio/219/17/2639.full.pdf), 10.1242/jeb.177295 (visual fields of 15 raptors), 10.1038/s41598-020-63039-y, 10.1002/cne.24190.
- Bubulcus ibis: 10.1159/000006596 (retina and visual function in wading birds, Brain Behav Evol 1999), 10.4314/aja.v11i1.2.
- Rumex obtusifolius (sense_light_nonvisual): 10.1104/pp.77.3.731 (open PDF at academic.oup.com), 10.1111/j.1399-3054.1986.tb02456.x (copy at research.wur.nl).
- Oxalis corymbosa (diel, sense_light_nonvisual): 10.1080/00219266.2005.9655968; Daucus carota nodding (diel): 1912 paper at hdl.handle.net/1811/1748, no DOI.
- Primula vulgaris 10.1111/plb.12849; Hypericum perforatum 10.1126/sciadv.adq6505 (gold) and 10.1016/j.envexpbot.2022.104797; Prunus cerasus 10.1111/j.1751-1097.1992.tb02198.x; Medicago sativa 10.1111/tpj.14333; Lycaena eye-morphology preprint 10.21203/rs.3.rs-4203706/v1.
