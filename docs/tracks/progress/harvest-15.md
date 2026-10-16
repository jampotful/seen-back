# Harvest 15 progress (16 October 2026)

Twenty genera were assigned. Pinus was skipped: harvest-1, harvest-12 and sweep-1 already hold full records for all four of its open traits. Medicago and Euonymus needed one cell each and Quercus needed sense_chemical only; harvest-11, harvest-8 and harvest-13 had the rest.

Web access was narrow. WebFetch opened the OpenAlex API (rate-limited with 429 after bursts) and MDPI. Every other host (Nature, Wiley, Frontiers, PMC, Science, journal sites, theses) was refused with a permission error, so papers were read through abstracts on the OpenAlex work record or the MDPI page, always through a page summary. Every evidence record is therefore `partial: true` with access "abstract".

## Evidence (docs/views/evidence/harvest-15.jsonl, 8 records)

- Prunella vulgaris, sense_light_nonvisual (far-red in vitro, Agronomy 2023). Prunella is a homonym and the harvest ran bird-style queries (dunnock hits); the plant family (Lamiaceae) review returned nothing on the open traits.
- Epipactis veratrifolia, sense_light_nonvisual (light spectrum and protocorm embryogenesis, Horticulturae 2023).
- Geranium robertianum, sense_light_nonvisual (no far-red elongation, Plant Direct 2018). The G. pyrenaicum record from the same paper was already in harvest-3 and was not repeated.
- Silene gallica, sense_light_nonvisual (red:far-red germination under wheat, Functional Ecology 2000).
- Medicago truncatula, sense_chemical (chitooligosaccharide perception, Nature Communications 2019).
- Achillea gypsicola, sense_light_nonvisual (cell-culture light response, 2021).
- Cirsium setidens, sense_light_nonvisual (LED spectrum, 2025).
- Euonymus japonicus, sense_light_nonvisual (light at night, Forests 2024; a gas-exchange response, with the weakness stated in the note).

## Search records (docs/views/searched/harvest-15.jsonl, 19 lines)

Prunella (2), Rana, Populus, Cirsium, Verbascum, Geranium, Silene, Lamium, Quercus (sense_chemical), Linaria (2, bird and plant), Poecile, Epipactis, Coreus, Oxythyrea, Ortalis, Achillea, Phoebis. For the plant genera the harvest's three queries are all light queries, so I added one by-hand OpenAlex chemical-sense query for Cirsium, Verbascum, Geranium, Quercus and Linaria and named them in `where`. Lamium, Achillea, Epipactis, Silene and Populus have no by-hand chemical query (rate limit); their sense_chemical records rest on the harvest queries alone and should be read that way.

## Wanted (docs/views/wanted/harvest-15.jsonl, 2 lines)

Howe et al. 1998 (Populus trichocarpa phytochrome loci) and Li and Blande 2017 (hybrid aspen volatile signalling). Authors, year and DOI come from OpenAlex work records.

## Left undone

- Populus euphratica phototropism (10.52586/5003, Frontiers in Bioscience-Landmark, gold): the OpenAlex lookup was rate-limited twice, so authors were never confirmed and no line was written.
- Rana: the frog-vision papers worth opening (Fite 1973, Maturana et al. 1960) are on Rana pipiens, which the queue files under Lithobates, so they were not wanted for Rana.
- Phoebis: the Carleton flicker-fusion thesis names nine species and no Phoebis.
- Poecile: two avian-vision theses (Purdue 2014, Cardiff 2009) may tabulate Paridae but have no DOI.
- Medicago truncatula: diel and eye_type were already searched; sense_light_nonvisual is already in harvest-11.
