# harvest-18 progress (16 October 2026)

Harvest run 2. All 20 genera were screened in the given order: Calystegia, Dryopteris, Pyronia, Aphelocoma, Eurema, Dianthus, Cercyonis, Cydalima, Phaneroptera, Limnodromus, Crataegus, Acris, Bonasa, Calyptocarpus, Asarum, Cynanthus, Vitis, Petasites, Pulsatilla, Nezara. None had full search records in docs/views/searched/harvest-*.jsonl beforehand, so none was skipped.

- Evidence (docs/views/evidence/harvest-18.jsonl): 2 partial records read from abstracts, Dryopteris filix-mas (spore germination needs light, phytochrome the photoreceptor) and Dianthus caryophyllus (far-red advances flowering by 22 days). Both are sense_light_nonvisual.
- Search records (docs/views/searched/harvest-18.jsonl): 27 lines for 20 genera. For the seven plant genera with sense_chemical open (Calystegia, Dianthus, Calyptocarpus, Asarum, Petasites, Pulsatilla, Vitis) the harvest had no sense_chemical query, so a short own query, "<Genus> volatile perception", was run by hand through the OpenAlex API by web fetch and is noted in each record.
- Wanted (docs/views/wanted/harvest-18.jsonl): 2 lines, both Vitis (Garris et al. 2009, open access link that would not open; Zeng et al. 2024, closed).
- Aphelocoma: the western scrub jay visual field paper (10.1007/s00359-010-0570-0) is already marked read; its page opened only as a summary here, so no quote was logged and the binocular and field cells stay open.
- Fetch notes: the OpenAlex API through the web fetch was rate-limited several times; J-STAGE, ASHS and Wiley pages did not open.
