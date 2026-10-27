# harvest-c17

## 2026-10-27

Desk screening only: no pages fetched and no evidence logged. OpenAlex skipped throughout this round after the coordinator received HTTP 429 (free IP budget exhausted); no OpenAlex scientific/common-name, citation, or family-review API step claimed. No null searched rows are written while those required steps remain incomplete. Old thin sweeps are not adopted as current completion. Harvest and screen_candidates run for each genus. Web titles/snippets supplied by search were screened (up to the first 20 returned); no claim of 20 when fewer were supplied. Plant eye_type follows owner point 10(b): none; focusing belongs to sense_light_nonvisual. Existing corrected evidence, wanted and owner statuses checked before adding requests.

### Scilla

Web screening finished for this round: four wanted leads added (germination/light, germination/GA3, daily anthesis, hormone-specific in-vitro response). AGRIS gives daily anthesis directly; no source text opened. Eye searches returned general plant-ocelli discussions and Scilla embryology without a genus-specific focusing measurement. Volatile searches supplied no Scilla signal experiment. Family-review search returned broad photoreceptor reviews and a Liriope growth study, no Scilla-specific review. Canon checked locally; not fetched. Full protocol incomplete because OpenAlex steps were skipped; 0 searched rows and 0 evidence records.

Queries run, word for word:

- `web: Scilla seed germination light dark`
- `web: Scilla germination gibberellin OR smoke OR dormancy`
- `web: Scilla floral scent volatiles`
- `web: Scilla flower opening time anthesis`
- `web: Siberian squill flower opening time anthesis`
- `web: Scilla plant ocelli lens-like epidermal cells eye`
- `web: Siberian squill plant ocelli lens-like epidermal cells eye`
- `web: Scilla response to airborne volatile signals`
- `web: Siberian squill response to airborne volatile signals`
- `web: Scilla light response photoperiod`
- `web: Siberian squill light response photoperiod`
- `web: Asparagaceae photoreceptor review`

### Diphasiastrum

Web screening finished for this round. One harvested chloroplast-movement thesis requested once across Polish/English duplicate titles; its exact Diphasiastrum coverage remains to be read. Mandatory germination queries returned general seed studies and Dipsacus false matches (Diphasiastrum is a spore plant); not adopted as Diphasiastrum evidence. Diel candidate 10.1101/2025.04.28.650909 measures Medicago leaflet motion, not this genus. Chemical candidate 10.3119/25-01 is a Rhodora correction with a journal-description abstract, no chemical experiment visible. Other listed light candidates concern Selaginella root evolution, general F-box regulation, reindeer grazing/community structure, and early angiosperm ecology, rather than a Diphasiastrum light-response measurement. Web pairs returned broad photoperiod/ocelli/volatile reviews and other genera; family-review query returned broad photoreceptor reviews. Canon checked locally. Full protocol remains incomplete because missing OpenAlex common-name and family/citation API steps were skipped; no null searched records.

Queries run, word for word:

- `web: Diphasiastrum seed germination light dark`
- `web: Diphasiastrum germination gibberellin OR smoke OR dormancy`
- `web: Diphasiastrum jasmonate herbivore`
- `web: Diphasiastrum flower opening time anthesis`
- `web: ground cedar flower opening time anthesis`
- `web: Diphasiastrum plant ocelli lens-like epidermal cells eye`
- `web: ground cedar plant ocelli lens-like epidermal cells eye`
- `web: Diphasiastrum response to airborne volatile signals`
- `web: ground cedar response to airborne volatile signals`
- `web: Diphasiastrum light response photoperiod`
- `web: ground cedar light response photoperiod`
- `web: Lycopodiaceae photoreceptor review`

Successful stored harvest queries reviewed, in stored order (not rerun):

- `Diphasiastrum phytochrome photoreceptor`
- `Diphasiastrum light perception`
- `Diphasiastrum phototropism`
- `Diphasiastrum flower opening time`
- `Diphasiastrum nyctinasty`
- `Diphasiastrum volatile signalling`
- `Diphasiastrum photoperiod`
- `Diphasiastrum circadian rhythm`
- `Diphasiastrum anthesis`
- `Diphasiastrum pollination biology`
- `Diphasiastrum epidermal lens cells`
- `Diphasiastrum epidermal focusing leaf optics`
- `Lycopodiaceae photoreceptor review` (stored family review)

Round checkpoint: 2 genera web-screened for this round, 0 full-protocol complete, 0 search rows, 5 wanted lines, 0 evidence records. Remaining unreviewed: 38; next Xanthium. OpenAlex refused at coordinator; no other service refused in this worker.
