# harvest-c18 progress

## 2026-10-27

This round is a partial protocol pass: 2 genera web-screened for this round (Malosma, Symphytum), 0 full-protocol genera completed, 0 evidence records, 0 searched records, and 6 new wanted lines. The remaining 38 genera start at Empetrum. Malosma and Symphytum still need missing OpenAlex common-name steps before any null result can be recorded. OpenAlex is unavailable for this round: the coordinator's initial probe returned HTTP 429 (free IP budget exhausted). It was not retried. No full-protocol completion or exhaustion is claimed. Only the search engine and stored harvest titles/abstracts were read; no source pages were fetched and no evidence was written, following desk-screen points 3 and 5.

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
