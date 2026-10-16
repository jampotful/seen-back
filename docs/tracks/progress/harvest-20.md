# Harvest 20 progress (16 October 2026)

Branch research/harvest-20, 22 genera in the order given. Harvest run 2 supplied the data for all of them, and harvest_get.py ran in about a second. No genus was skipped: each lacked a full search record for at least one open trait.

## Closed by a measurement (abstract only, partial true, access abstract)
- Phacelia tanacetifolia, sense_light_nonvisual, two records: seeds germinate less in light than in darkness (Tiryaki and Keles 2011), and red light promotes loop formation in seedlings (Rollin 1966).
- Osmunda cinnamomea, sense_light_nonvisual: phytochrome acts in chlorophyll synthesis in cultured leaf primordia (Haight and Kuehnert 1970).

The abstracts come from the harvest's OpenAlex record, and quotes are copied from that stored abstract. Authors, volume and pages come from the OpenAlex work record (raw_author_name) read through WebFetch. No full text was opened.

## Search records and wanted lines
32 search records. For the ten plant genera the harvest sent no sense_chemical query, so I ran one by hand for each through the OpenAlex search API ("<Genus> volatile chemical signal perception") and wrote it as its own record. Three wanted lines: Nishimura et al. 2023 on Asio flammeus retinal ganglion cells, and the two Crozier, Wolf and Zerrahn-Wolf flicker papers on Anax larvae (1937, 1938). The Hibiscus rosa-sinensis ethylene paper (10.1093/jxb/err218) was not logged because its stored abstract is cut mid-sentence.

## Blocked
WebFetch refused any URL it had not seen in an earlier result (rupress.org, bioone.org after the doi.org redirect), WebSearch had no budget left, and the OpenAlex API returned 429 about once every three calls and gave a stale answer for a multi-DOI filter, so only single /works/doi: records and search= queries were used. The family-review papers for the dragonflies (colour vision, opsin genes) were screened by title only.
