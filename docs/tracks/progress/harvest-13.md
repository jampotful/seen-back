# Harvest 13 progress (16 October 2026)

Branch research/harvest-13, 20 genera in the order given. Harvest run 2 supplied the data for all of them (run 3 was cancelled and holds none of these genera). harvest_get.py ran in about a second, not slowly.

Harvest run 2 had given up on every search for Fagus, Chamaenerion, Coragyps, Oxalis, Orthetrum and Bellis, and on part of Fragaria. I ran those searches by hand through the OpenAlex API (WebFetch). The proxy rate-limited it to about one call a minute, so a few searches were not repeated, and each search record says which. Citation steps were run by hand through OpenAlex for Orthetrum, Fagus, Chamaenerion, Bellis and Fragaria.

No genus was skipped as already complete: each lacked a full search record for at least one open trait.

## Closed by a measurement (abstract only, partial true, access abstract)
- Fagus sylvatica and Fagus crenata, sense_light_nonvisual (photoperiod perception in buds).
- Euonymus japonicus, sense_light_nonvisual (response to the colour of night light).
- Oxalis triangularis, diel and sense_light_nonvisual (nyctinastic leaf movement).
- Medicago truncatula, sense_chemical (chitooligosaccharide receptors).
- Fragaria vesca, sense_chemical (response to live substrate through the air).

Abstracts came from the OpenAlex record (and nature.com for Medicago) through a page summary; no full text opened. Authors for the Fagus, Euonymus, Oxalis and Fragaria records, and the volume numbers, come from the OpenAlex record.

## Search records and wanted lines
Search records cover all 20 genera except where an earlier file already held the trait (Cornus light, Verbascum diel/eye_type/light, Medicago diel/eye_type, Sayornis cff_hz/interreceptor_deg). Two wanted lines: the takahe eye paper (Porphyrio) and "UVS is rare in seabirds" (Leucophaeus). Authors for both come from the OpenAlex record, not a publisher page.

## Blocked
Publisher pages (tandfonline, sciencedirect, wiley, oup, pmc, doi.org) were refused or rate-limited; mdpi.com, nature.com and journals.plos.org opened. The Cornus LED-seedling paper (10.3906/biy-1607-19) and the Fagus sylvatica blue-light paper (10.1007/s11099-009-0060-1) were not opened. A WebFetch with a filter= query string sometimes returned a stale earlier page, so only search= queries, /works/doi: records and one cites: filter checked against a different result were used.
