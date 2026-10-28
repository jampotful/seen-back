# desk-d35: plant genera screen, queue batches 26 and 27 (28 October 2026, branch research/desk-d35)

## Genera
Worked (24): Phlox, Solidago, Gleditsia, Clinopodium, Hylocomium, Holodiscus, Dasiphora, Ampelopsis, Phleum, Ferocactus, Spiraea, Galanthus, Sarracenia, Angelica, Echinocystis, Silybum, Spinulum, Houstonia, Leonurus, Buddleja, Verbena, Hepatica, Medeola, Viscum.
Skipped, every open trait already held by evidence or a full (harvest or desk) search record on main: Cakile, Prosopis, Origanum, Dianthus, Helminthotheca.
Skipped, POWO synonym: Hypopitys (POWO pages for Hypopitys names say "synonym of Monotropa hypopitys").
Rule used per trait: worked unless main held evidence, a desk/harvest/web-labelled search record, or a wanted lead for that genus and trait. Old sweep-era records (no web queries) were treated as half-searched.

## Evidence (4 records, all abstract-level, partial)
- Phlox pilosa sense_light_nonvisual (Madeiras et al. 2007, HortScience 42(5): 1263-1267).
- Phlox longifolia sense_chemical (Ridout and Tripepi 2009, Native Plants J 10(2): 80-90, DOI 10.2979/NPJ.2009.10.2.80): smoke and KNO3 failed to induce germination.
- Echinocystis lobata sense_light_nonvisual (Filar 2023 thesis, Jagiellonian University).
- Hepatica asiatica sense_light_nonvisual (Jeong et al. 2015, shading levels; POWO lists H. asiatica as accepted).

## Search records: 24 lines (docs/views/searched/desk-d35.jsonl), one per genus listing the traits left open after leads and evidence.
## Wanted lines: 8 (Solidago Walck 1997 part 3; Ferocactus Chihuahuan cacti GA3/light; Galanthus and Narcissus germination; Angelica archangelica GA3; Silybum Moradi 2024; Hepatica asiatica GA3 Chon 2015; Hepatica nobilis flower ecology; Viscum album Biological Flora). Four have no DOI and no authors (Ferocactus, Galanthus, Angelica, zenodo Hepatica has DOI only) and will be held by the desk until a registry fills them.

## Faults and limits
- OpenAlex is blocked (proxy 403), so every step beyond the harvest's cached queries is a labelled "web: " WebSearch. Family reviews: one pooled family search (listed word for word) returned Li and Mathews 2016 (DOI 10.1007/s10265-016-0785-4, page opened); harvest genera name their harvest family-review search in `chased`.
- Focusing (eye_type) was searched with three pooled genus-list queries, each listed word for word.
- The WebSearch tool returns titles and links only, so results were screened by title and opened where a title looked like a measurement. Fetches refused or blocked: powo Spinulum page, doi.org Walck 1997 part 3, nva.sikt.no (Angelica GA3), zenodo 161177, Cambridge Chihuahuan cacti light paper, centaur.reading.ac.uk (bot check), biblat, PMC4485155.
- Not filed: Solidago hybrida hort. flower hours 7:00 to 16:00 (hybrid name); Walck 1997 part 2 darkness sentence (does not state a light comparison); Phlox pilosa GA3 sentence (OCR-garbled units); Leonurus sibiricus light/dark design (abstract gives no dark result; Leonurus light already on main); Silybum and Hepatica GA3 abstracts (sentences over 125 characters).
