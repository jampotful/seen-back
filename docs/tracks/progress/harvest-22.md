# Harvest 22 progress (16 October 2026)

Branch research/harvest-22, 20 genera in the order given. Harvest run 4 supplied the data (Verbascum came from run 2 and Pinus from run 1, which the harvest merged).

## Skipped
- Verbascum: diel, eye_type and sense_chemical already carry search records (harvest-7, -13, -15) and sense_light_nonvisual is already measured in Verbascum phlomoides (harvest-7, -10).
- Pinus: diel and eye_type already carry search records (harvest-1) and sense_light_nonvisual is already measured (harvest-12 and earlier). Only sense_chemical is open.

## Written
18 search records in docs/views/searched/harvest-22.jsonl, one per genus, each with the harvest's queries word for word and found "none". The plant records cover diel, eye_type and sense_light_nonvisual. The bird and insect records cover every open optics trait. One wanted line: Verma, Gantait, Jeong and Hwang 2018 on Digitalis purpurea under LED light (10.1038/s41598-018-36113-9). No evidence records.

## Not done: sense_chemical for the plant genera
The harvest sent no sense_chemical query for plants. The hand OpenAlex query could not be run: WebFetch refused api.openalex.org and every other address that had not come from WebSearch, and curl through the proxy returned 403. So no sense_chemical search record was written for the 15 plant genera that still have the cell open (Digitalis, Epilobium, Filipendula, Cypripedium, Frangula, Clematis, Liriodendron, Apocynum, Sorbus, Pilosella, Verbesina, Carduus, Anthriscus, Lythrum, Pinus). Verbascum's is already on record.

## Blocked
Only pages returned by WebSearch could be opened (doi.org and the Gyeongsang repository for the Digitalis paper, both as summaries; PMC returned a reCAPTCHA page). No full text was read, so no measurement was logged. Candidates noted in the search records but left unlogged because their bylines could not be confirmed: Epilobium seed germination under intermittent light (10.15281/jplantres1887.78.452), Sorbus tianschanica under coloured films (10.1371/journal.pone.0354303), foxglove seedlings under far-red LED light (10.21273/horttech04661-20).
