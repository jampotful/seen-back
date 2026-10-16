# harvest-19 progress (16 October 2026)

Genera done: all 20 (Tigrisoma, Mycelis, Pulmonaria, Ophrys, Scrophularia, Hamamelis, Phyla, Udea, Rhamnus, Odocoileus, Mythimna, Idia, Reynoutria, Pedicularis, Arctostaphylos, Thymelicus, Issoria, Chloroceryle, Cakile, Stelgidopteryx). None had a full search record in an earlier harvest file, so none was skipped. Harvest run named in every record: run 2.

Cells closed by a measurement (both partial, from the OpenAlex abstract record):
- Scrophularia kakudensis, sense_light_nonvisual (Manivannan et al. 2021, 10.3389/fpls.2020.607007).
- Cakile edentula, sense_chemical (Dudley and File 2007, 10.1098/rsbl.2007.0232).

Search records written: 30 (docs/views/searched/harvest-19.jsonl), including a hand-made sense_chemical query for each of the 11 plant genera, run through the OpenAlex API by WebFetch (the harvest had none). Wanted lines: 2 (Bhatt et al. 2010 and a full-text copy of Dudley and File 2007).

Notes. The fetch tool's summariser would not return long verbatim text, so quotes were taken only where it returned a whole abstract sentence in consecutive parts. WebFetch was rate limited (HTTP 429) when calls ran in parallel, so the hand queries ran one at a time. Odocoileus already has pupil shape on record for O. virginianus (10.1126/sciadv.1500391); the harvest still lists the cell as open, which may be a stale queue entry. Screened and set aside: Halali et al. 2026 (Issoria not named), Hasegawa 2022 (swallow face patterns, no vision measure), Chen and Han 2024 (Mythimna retina, no acuity or flicker), Falara et al. 2012 (Chiloglottis, not Ophrys).
