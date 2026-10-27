# harvest-c18 progress

## 2026-10-27

This round is a partial protocol pass: 6 genera web-screened for this round (Malosma, Symphytum, Empetrum, Holcus, Petasites, Calypso), 0 full-protocol genera completed, 0 evidence records, 0 searched records, and 27 new wanted lines. The remaining 34 genera start at Epigaea. Malosma and Symphytum still need missing OpenAlex common-name steps before any null result can be recorded. OpenAlex is unavailable for this round: the coordinator's initial probe returned HTTP 429 (free IP budget exhausted). It was not retried. No full-protocol completion or exhaustion is claimed. Only the search engine and stored harvest titles/abstracts were read; no source pages were fetched and no evidence was written, following desk-screen points 3 and 5.

Required AGENTS, codex-round, round4-harvest, desk-screen points 1–10, THOROUGH, BRIEF Round 2, round3-sweep and audits 53/54 were consulted. The coordinator refreshed main and origin/ci and provided the shared branch; no checkout, pushes, PRs, tool changes or operational-state changes were made. Canon lists no plant-trait compilation applicable here. Existing wanted/evidence was checked; thin sweep searches were not treated as current coverage. Owner n/a sources and issue-28/c22/c23 work are excluded from adoption.

### Malosma: web-screened; OpenAlex incomplete

`harvest_get.py Malosma` and `screen_candidates.py Malosma` ran; harvest/candidate outputs were read. Successful harvest queries in order: `Malosma phytochrome photoreceptor`; `Malosma light perception`; `Malosma phototropism`; `Malosma flower opening time`; `Malosma nyctinasty`; `Malosma volatile signalling`; `Malosma photoperiod`; `Malosma circadian rhythm`; `Malosma anthesis`; `Malosma pollination biology`; `Malosma epidermal lens cells`; `Malosma epidermal focusing leaf optics`. Harvest family review: `Anacardiaceae photoreceptor review`. No genus citation step was printed. Exact additional web searches:

- `web: Malosma seed germination light dark`
- `web: Malosma germination gibberellin OR smoke OR dormancy`
- `web: Malosma floral scent volatiles`
- `web: Malosma flower opening time anthesis`
- `web: laurel sumac flower opening time anthesis`
- `web: Malosma plant ocelli epidermal focusing leaf optics`
- `web: laurel sumac plant ocelli epidermal focusing leaf optics`
- `web: Malosma light perception photoperiod`
- `web: laurel sumac light perception photoperiod`
- `web: Malosma chemical response volatile signal`
- `web: laurel sumac chemical response volatile signal`
- `web: Anacardiaceae photoreceptor review`

Search titles/snippets exposed two direct experimental shade studies, now wanted, plus the harvested review on light-dependent leaf hydraulics. Seasonal phenology in `10.1093/jpe/rtv066` remains a light-response lead to inspect before any null. The nutrient paper `10.4067/s0717-66432019000200208` concerns Chilean shrubs, the weight-room carbonyl study concerns room air, and honeybee/Polygonum/mango family results concern other taxa. None supports a Malosma chemical or diel measurement on the supplied abstract. Plant eye_type follows the owner’s none reading; epidermal focusing would instead be sense_light_nonvisual. Generic plant-ocelli search hits did not name Malosma. No null record was written.

### Symphytum: web-screened; OpenAlex incomplete

`harvest_get.py Symphytum` and `screen_candidates.py Symphytum` ran; harvest/candidate outputs were read. Successful harvest queries in order: `Symphytum phytochrome photoreceptor`; `Symphytum light perception`; `Symphytum phototropism`; `Symphytum flower opening time`; `Symphytum nyctinasty`; `Symphytum anthesis`; `Symphytum pollination biology`; `Symphytum volatile signalling`; `Symphytum epidermal lens cells`; `Symphytum epidermal focusing leaf optics`. Harvest family review: `Boraginaceae photoreceptor review`. Exact additional web searches:

- `web: Symphytum seed germination light dark`
- `web: Symphytum germination gibberellin OR smoke OR dormancy`
- `web: Symphytum floral scent volatiles`
- `web: Symphytum flower opening time anthesis`
- `web: comfrey flower opening time anthesis`
- `web: Symphytum plant ocelli epidermal focusing leaf optics`
- `web: comfrey plant ocelli epidermal focusing leaf optics`
- `web: Symphytum chemical response volatile signal`
- `web: comfrey chemical response volatile signal`
- `web: Boraginaceae photoreceptor review`

Two anthesis sources from the harvest and the independently found floral-volatile ant experiment are now wanted. Search snippets also showed leaf histology (`10.1177/1934578X1100601017`), describing epidermal heights and anatomy, without focusing; it does not establish an animal eye. Comfrey extract chemistry, distilled profiles and pharmacology do not count as living chemical response. Harvest `10.2478/v10182-012-0013-z` describes annual and interannual canopy development, not a demonstrated chemical response in the supplied abstract; `10.1111/oik.07301` concerns bacterial volatiles and an aphid parasitoid; Echium/Pontechium and ant family-review results do not establish Symphytum response. No null record was written. The search result of a potentially relevant Symphytum morphology/flowering PDF at `https://static.uni-graz.at/fileadmin/_Persoenliche_Webseite/teppner_herwig/Publicationen/Teppner-Phyton-50-2-Symphytum.pdf` was not fetched; its shown anthesis text concerns Onosma rather than establishing a Symphytum diel measurement.

Before commit, the required own-file screening check printed `0 problems`; empty searched file is intentional because required steps are incomplete.

### Empetrum: web-screened; OpenAlex incomplete

Required harvest_get and screen_candidates ran and their stored results were screened. Successful harvested queries in order: `Empetrum phytochrome photoreceptor`; `Empetrum light perception`; `Empetrum phototropism`; `Empetrum flower opening time`; `Empetrum nyctinasty`; `Empetrum volatile signalling`; `Empetrum photoperiod`; `Empetrum circadian rhythm`; `Empetrum anthesis`; `Empetrum pollination biology`; `Empetrum epidermal lens cells`; `Empetrum epidermal focusing leaf optics`. Exact additional web searches:

- `web: Empetrum seed germination light dark`
- `web: Empetrum germination gibberellin OR smoke OR dormancy`
- `web: Empetrum floral scent volatiles`
- `web: Empetrum flower opening time anthesis`
- `web: crowberry flower opening time anthesis`
- `web: Empetrum plant ocelli epidermal focusing leaf optics`
- `web: crowberry plant ocelli epidermal focusing leaf optics`
- `web: Empetrum chemical response volatile signal`
- `web: crowberry chemical response volatile signal`
- `web: Empetrum light perception photoperiod`
- `web: crowberry light perception photoperiod`
- `web: Ericaceae photoreceptor review`

Adopted existing light-response wanted coverage: harvest-25 line 3 (`10.1046/j.1365-2745.2002.00709.x`), not requested again. New germination, growth-regulator, red-light rooting, shading/BVOC and diel flux leads are wanted. Crowberry steam-distillation profiles and leaf-extract phenolics are tissue chemistry and do not establish living response or signalling. Generic epidermal-ocelli results and human eye antioxidant reviews do not establish Empetrum optical measurements; focusing would belong under sense_light_nonvisual. No source pages were fetched, no evidence extracted and no null search records written. Missing OpenAlex common-name steps remain unavailable.

### Holcus: web-screened; OpenAlex incomplete

Required harvest_get and screen_candidates ran and their stored results were screened. Successful harvested queries in order: `Holcus phytochrome photoreceptor`; `Holcus light perception`; `Holcus phototropism`; `Holcus flower opening time`; `Holcus nyctinasty`; `Holcus anthesis`; `Holcus pollination biology`; `Holcus volatile signalling`; `Holcus photoperiod`; `Holcus circadian rhythm`; `Holcus epidermal lens cells`; `Holcus epidermal focusing leaf optics`. Exact additional web searches:

- `web: Holcus seed germination light dark`
- `web: Holcus germination gibberellin OR smoke OR dormancy`
- `web: Holcus floral scent volatiles`
- `web: Holcus flower opening time anthesis`
- `web: velvetgrass flower opening time anthesis`
- `web: Holcus plant ocelli epidermal focusing leaf optics`
- `web: velvetgrass plant ocelli epidermal focusing leaf optics`
- `web: Holcus chemical response volatile signal`
- `web: velvetgrass chemical response volatile signal`
- `web: Holcus light perception photoperiod`
- `web: velvetgrass light perception photoperiod`

New primary leads cover anthesis, growth regulators, light/dark and red/far-red/nitrate germination, light pollution and living volatile emission. The Canadian weeds review and pollen-periodicity snippets corroborate daily anthesis leads, but no values were extracted. The dried-grass GC-MS headspace survey (`10.1556/1326.2022.01099`) is tissue chemistry, not a living plant signal. Generic plant-ocelli and unrelated animal eyes in web results supply no Holcus eye measurement; focusing would instead belong under sense_light_nonvisual. Harvest Poaceae review was screened; independent `web: Poaceae photoreceptor review` search also ran and its titles/snippets showed general plant-photoreceptor reviews, without a new Holcus-specific lead. Missing OpenAlex common-name steps also remain unavailable. No null records or evidence written.

### Petasites: web-screened; OpenAlex incomplete

Required harvest_get and screen_candidates ran and their stored results were screened. Successful harvested queries in order: `Petasites phytochrome photoreceptor`; `Petasites light perception`; `Petasites phototropism`; `Petasites volatile signalling`. Exact additional web searches:

- `web: Petasites seed germination light dark`
- `web: Petasites germination gibberellin OR smoke OR dormancy`
- `web: Petasites floral scent volatiles`
- `web: Petasites chemical response volatile signal`
- `web: butterbur chemical response volatile signal`
- `web: Asteraceae photoreceptor review`

Only sense_chemical is currently open in screen_candidates. Two direct living-plant leads are wanted: field floral headspace signalling and gibberellic-acid rootstock response. Essential oil and flower-stalk constituent papers concern tissue chemistry and are excluded under owner reading 10(a). The Ostrinia paper measures moth sex pheromone, not Petasites response; the Centaurea root-volatile study concerns another genus; butterbur broomrape is Orobanche, not Petasites. No source page fetched, evidence written or null record made; OpenAlex completion remains unavailable.

### Calypso: web-screened; OpenAlex incomplete

Required harvest_get and screen_candidates ran and their stored results were screened. Successful harvested queries in order: `Calypso phytochrome photoreceptor`; `Calypso light perception`; `Calypso phototropism`; `Calypso flower opening time`; `Calypso nyctinasty`; `Calypso volatile signalling`; `Calypso photoperiod`; `Calypso circadian rhythm`; `Calypso anthesis`; `Calypso pollination biology`; `Calypso epidermal lens cells`; `Calypso epidermal focusing leaf optics`. Exact additional web searches:

- `web: Calypso seed germination light dark`
- `web: Calypso germination gibberellin OR smoke OR dormancy`
- `web: Calypso floral scent volatiles`
- `web: Calypso flower opening time anthesis`
- `web: fairy slipper flower opening time anthesis`
- `web: Calypso bulbosa chemical response volatile signal`
- `web: fairy slipper chemical response volatile signal`
- `web: Calypso bulbosa light perception photoperiod`
- `web: fairy slipper light perception photoperiod`
- `web: Calypso bulbosa plant ocelli epidermal focusing leaf optics`
- `web: fairy slipper plant ocelli epidermal focusing leaf optics`
- `web: Orchidaceae photoreceptor review`

The required genus-first germination searches were heavily contaminated by Calypso bean, cilantro and ornamental cultivar names. Full scientific name Calypso bulbosa disambiguated the subsequent paired trait searches. Perfume brands, mango/bean cultivars, Poa bulbosa, hermit crabs, human gut and vitiligo papers, and other orchid genera do not establish Calypso measurements. The embryo-development paper times ovule development relative to anthesis and the bumblebee-learning paper manipulates seasonal flowering dates, not demonstrated daily opening hours on the supplied abstracts. One seven-year forest-cover/light-environment lead is wanted. Search snippets also showed a University of Washington propagation protocol (https://courses.washington.edu/esrm412/protocols/2010/CABU.pdf), but no experiment comparing light or hormone treatments was supplied in the snippet. Generic ocelli/leaf-lens results do not name a Calypso focusing measurement; plant eye_type follows the owner none reading. No pages fetched, evidence written or null records made. Missing OpenAlex common-name steps remain unavailable.
