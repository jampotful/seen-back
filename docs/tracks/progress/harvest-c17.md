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

### Xanthium

Web screening finished for this round: five wanted leads added (daily leaf movements, CO2/stomatal sensitivity, applied auxin, CO2/flowering, applied germination regulators). Existing sense_light_nonvisual evidence adopted: recheck-1-fixed:8 Xanthium strumarium achenes collected right after maturation germinated in daily natural greenhouse light at 24 to 30 C and did not germinate in darkness; red and far-red light had little effect, and buried achenes did not develop a red-light requirement; in the field, shade intensity explained 77% of the variation in emergence and 95% shade cut emergence by 72 to 88% (partial). Light-only germination studies found by the mandatory first searches are not re-requested for this already-covered trait. Open traits remain diel, eye_type, sense_chemical. General ocelli papers do not establish a Xanthium eye; lens-like focusing would belong under sense_light_nonvisual. Harvest diel candidates on soybean/Cannabis, Phaseolus, Linum and Goniothalamus are other genera; Xanthium flowering-date/biotype studies give no daily opening hour in the stored abstract. Simulated volatile signaling preprint does not show a live cue response in its truncated stored abstract, so not used as negative evidence; chemical null is held in any event. Tissue/extract phytochemistry is excluded under owner 10(a). Family web query returned general photoreceptor reviews, not a Xanthium-specific review. Full protocol incomplete: missing OpenAlex common-name/citation/family API steps skipped; no null search record written.

Queries run, word for word:

- `web: Xanthium seed germination light dark`
- `web: Xanthium germination gibberellin OR smoke OR dormancy`
- `web: Xanthium jasmonate herbivore`
- `web: Xanthium flower opening time anthesis`
- `web: common cocklebur flower opening time anthesis`
- `web: Xanthium plant ocelli lens-like epidermal cells eye`
- `web: common cocklebur plant ocelli lens-like epidermal cells eye`
- `web: Xanthium response to airborne volatile signals`
- `web: common cocklebur response to airborne volatile signals`
- `web: Asteraceae photoreceptor review`

Successful stored harvest queries reviewed, in stored order (not rerun):

- `Xanthium phytochrome photoreceptor`
- `Xanthium light perception`
- `Xanthium phototropism`
- `Xanthium flower opening time`
- `Xanthium nyctinasty`
- `Xanthium anthesis`
- `Xanthium pollination biology`
- `Xanthium volatile signalling`
- `Xanthium epidermal lens cells`
- `Xanthium epidermal focusing leaf optics`
- stored citation step: 10.1016/j.tree.2009.09.010; 0 returned works
- `Asteraceae photoreceptor review` (stored family review)

Round checkpoint: 3 genera web-screened for round; 0 full-protocol complete; 0 search rows; 10 wanted lines; 0 evidence. Remaining unreviewed: 37; next Goodyera.

### Goodyera

Web screening finished for this round. Five new reading leads: floral scent, original light/dark germination study, irradiance/carbon-nitrogen exchange experiment, USFS germination review leading to its source, and harvested orchid germination/light review. Chloroplast-movement thesis already requested in this batch is adopted as a broad candidate rather than requested again; its Goodyera species coverage needs verification. Diel searches supplied seasonal flowering periods, not a daily opening hour. Eye searches supplied general ocelli discussions and Goodyerinae anatomy, not a verified Goodyera focusing experiment. Harvest keyword candidates on Cattleya, Cucumis, Calanthe, Disa, Ludisia, Cymbidium, Spathoglottis, Paphiopedilum, Spiranthes, Cypripedium and Macodes concern different genera; the 1899 rattlesnake-plantain item has a journal-editorial abstract, so that abstract gives no chemical result. Rostellum review discusses post-pollination ethylene generally without naming a Goodyera experiment in the stored text. Family-review web search found Physiological diversity of orchids (10.1016/j.pld.2018.06.003); no Goodyera measurement visible in returned snippet. Canon checked locally. Required OpenAlex missing steps skipped; full protocol incomplete and no null searched rows.

Queries run, word for word:

- `web: Goodyera seed germination light dark`
- `web: Goodyera germination gibberellin OR smoke OR dormancy`
- `web: Goodyera floral scent volatiles`
- `web: Goodyera flower opening time anthesis`
- `web: rattlesnake plantain flower opening time anthesis`
- `web: Goodyera plant ocelli lens-like epidermal cells eye`
- `web: rattlesnake plantain plant ocelli lens-like epidermal cells eye`
- `web: Goodyera response to airborne volatile signals`
- `web: rattlesnake plantain response to airborne volatile signals`
- `web: Goodyera light response photoperiod`
- `web: rattlesnake plantain light response photoperiod`
- `web: Orchidaceae photoreceptor review`

Successful stored harvest queries reviewed, in stored order (not rerun):

- `Goodyera phytochrome photoreceptor`
- `Goodyera light perception`
- `Goodyera phototropism`
- `Goodyera flower opening time`
- `Goodyera nyctinasty`
- `Goodyera anthesis`
- `Goodyera pollination biology`
- `Goodyera volatile signalling`
- `Goodyera photoperiod`
- `Goodyera circadian rhythm`
- `Goodyera epidermal lens cells`
- `Goodyera epidermal focusing leaf optics`
- `Orchidaceae photoreceptor review` (stored family review)

Round checkpoint: 4 genera web-screened for round; 0 full-protocol complete; 0 search rows; 15 wanted lines; 0 evidence. Remaining unreviewed: 36; next Lysichiton.

### Lysichiton

Web screening finished for this round: three wanted leads (light/dark germination compilation, exact primary odor/pollination citation surfaced by WFO, and secondary source naming the Lysichiton spathe odor and beetle pollinator). Harvest_get and screen_candidates both report no stored harvest, so there are no stored harvest queries or candidates to adopt. Mandatory germination queries returned the light/dark compilation and horticultural information; no named hormone trial for this genus appeared. Common-name searches frequently returned Symplocarpus foetidus or S. renifolius (including thermogenic oscillations, PEBP genes and damaged-plant odors); those concern different genera and are excluded. Lisianthus lighting results concern Eustoma, also excluded. Diel results gave seasonal anthesis or flower/spathe description, no verified daily opening hour. Eye pair returned general ocelli work without a genus-specific focusing experiment. Family-review query returned broad plant/algal photoreceptor reviews and Araceae morphology; none supplied a Lysichiton measurement in the returned snippet. Canon checked locally. OpenAlex steps omitted after coordinator 429; no full protocol/exhaustion claim, no null search record.

Queries run, word for word:

- `web: Lysichiton seed germination light dark`
- `web: Lysichiton germination gibberellin OR smoke OR dormancy`
- `web: Lysichiton floral scent volatiles`
- `web: Lysichiton flower opening time anthesis`
- `web: western skunk cabbage flower opening time anthesis`
- `web: Lysichiton plant ocelli lens-like epidermal cells eye`
- `web: western skunk cabbage plant ocelli lens-like epidermal cells eye`
- `web: Lysichiton response to airborne volatile signals`
- `web: western skunk cabbage response to airborne volatile signals`
- `web: Lysichiton light response photoperiod`
- `web: western skunk cabbage light response photoperiod`
- `web: Araceae photoreceptor review`

Round checkpoint: 5 genera web-screened for round (Scilla, Diphasiastrum, Xanthium, Goodyera, Lysichiton), all partial under the full protocol. 0 full-protocol complete; 0 searched rows; 18 wanted lines; 0 evidence. Remaining unreviewed: 35; exact next Calamagrostis. OpenAlex skipped for the round after coordinator HTTP 429; no additional service refusals. No pages fetched, no PDFs/full text committed.
