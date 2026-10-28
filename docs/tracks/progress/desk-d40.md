# desk-d40: queue batches 33 and 34 (plant genera)

Branch research/desk-d40. WebSearch only (OpenAlex returns 403); fetches limited to URLs that a search or the harvest output returned (doi.org, PMC, Europe PMC and bioRxiv abstract pages were refused).

## Genera done (13)
Ballota, Dodonaea, Heliotropium, Coptis, Borago, Amaranthus, Osteospermum, Ribes, Fritillaria, Hippophae, Shepherdia, Zantedeschia, Sanguisorba.

## Evidence (8 lines, all abstract-only, partial)
- Dodonaea viscosa sense_light_nonvisual (Al-Namazi et al. 2020)
- Heliotropium europaeum sense_chemical (GA3; Veiga-Barbosa and Perez-Garcia 2016)
- Amaranthus viridis sense_chemical (gibberellin 1000 ppm; Alazmani and Ghorbanli 2009)
- Coptis omeiensis sense_chemical (GA3 5.0 mg/L; Zhang et al. 2009)
- Hippophae salicifolia sense_chemical (GA3; Airi et al. 2009)
- Fritillaria raddeana sense_chemical (GA priming; Alipour et al. 2019)
- Zantedeschia (genus, grade g) sense_chemical (GA3; Naor et al. 2004)
- Sanguisorba officinalis sense_chemical (GA 200 mg/L; Jiang et al. 2008)

## Search records: 31 (genus level, one per genus and trait), wanted lines: 12
Traits left out of a genus's record sit on the wanted list (Heliotropium, Coptis, Borago, Ribes, Hippophae, Shepherdia light or chemical or diel). Wanted leads where the quote limit (125 characters) blocked a record: Borago microgreens PPFD (10.15544/rd.2013.2.057), Hippophae salicifolia light colours (10.36808/if/2013/v139i5/33520), Borago GA thesis (Solis Fuentes 2006). Ribes nigrum rhythmic floral volatiles (10.1111/j.1365-3040.1994.tb02030.x) is a diel lead from the harvest abstract only.

## Not reached (17 genera)
Campanulastrum, Hieracium, Castanea, Sanicula, Eriophyllum, Chamaedaphne, Tiarella, Menyanthes, Corallorhiza, Mimosa, Tribulus, Schizachyrium, Tellima, Echinochloa (budget); Ophrys, Pulsatilla, Pedicularis skipped: full searches dated 16 Oct already on main for every open cell.

## Notes for the main session
- Pre-existing check.py problems in intake-4-failed and intake-5-failed (not this unit).
- Several wanted DOIs came from the harvest listing only (Ribes 1994, Heliotropium arborescens 2000, Ribes 1973); none was fetchable.
