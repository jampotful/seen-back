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

### Calamagrostis

Web screening finished for this round: new leads include C. arenaria germination under light conditions, C. canadensis regrowth in light/dark, an acclimation paper with a truncated search title, a verified C. arundinacea CO2-response experiment, and a root-volatiles thesis whose host coverage remains to be verified. Common name reed grass is broad: Phalaris and Phragmites results were not treated as Calamagrostis. Mandatory germination/JA searches returned much general seed and jasmonate literature without a genus-specific hormone trial. Diel candidates mostly report seasonal anthesis or other genera, not daily flower-opening time. Epidermal morphology result 10.1360/aps050053 describes taxonomic epidermal variation, not an eye or a verified focusing measurement. Harvest chemical candidate 10.1556/1326.2022.01099 is dried-grass headspace chemistry (owner 10(a)), so not a living signal; existing replant-1 request not duplicated. Other harvested chemical candidates include botanical etymology, Cunninghamia, Ocimum, ash fluoride, sandal and studies on other genera. Family web query returned broad photoreceptor reviews and grass phytochrome sequence work; no Calamagrostis measurement visible in the snippets. Canon checked locally. Required missing OpenAlex steps skipped; full protocol remains incomplete and no null search rows written.

Queries run, word for word:

- `web: Calamagrostis seed germination light dark`
- `web: Calamagrostis germination gibberellin OR smoke OR dormancy`
- `web: Calamagrostis jasmonate herbivore`
- `web: Calamagrostis flower opening time anthesis`
- `web: reed grass flower opening time anthesis`
- `web: Calamagrostis plant ocelli lens-like epidermal cells eye`
- `web: reed grass plant ocelli lens-like epidermal cells eye`
- `web: Calamagrostis response to airborne volatile signals`
- `web: reed grass response to airborne volatile signals`
- `web: Calamagrostis light response photoperiod`
- `web: reed grass light response photoperiod`
- `web: Poaceae photoreceptor review`

Successful stored harvest queries reviewed, in stored order (not rerun):

- `Calamagrostis phytochrome photoreceptor`
- `Calamagrostis light perception`
- `Calamagrostis phototropism`
- `Calamagrostis flower opening time`
- `Calamagrostis nyctinasty`
- `Calamagrostis volatile signalling`
- `Calamagrostis photoperiod`
- `Calamagrostis circadian rhythm`
- `Calamagrostis anthesis`
- `Calamagrostis pollination biology`
- `Calamagrostis epidermal lens cells`
- `Calamagrostis epidermal focusing leaf optics`
- `Poaceae photoreceptor review` (stored family review)

Final checkpoint for this worker: 6 genera web-screened for the round (Scilla through Calamagrostis), all partial under the full protocol; 0 full-protocol complete, 0 searched rows, 23 wanted lines, 0 evidence. Stopped between genera for handoff. Remaining unreviewed: 34, exact next Marrubium. All 40 remain without a complete new OpenAlex protocol. Only refused service: OpenAlex, coordinator HTTP 429; skipped throughout. No page fetches or paper text committed. Gate must print 0 problems before commit.

### Marrubium (2026-10-27 continuation)

Web screening performed for this round. Six new chemical-response leads added (two GA3 seed studies, GA3/nitrate species survey, nutrient-solution treatment, CO2/bacteria and lead adaptation). Existing M. vulgare light/dark germination evidence sweep-25#8 is adopted; light-only germination leads are not requested again. Diel results gave seasonal flowering and morphology, without daily opening hours. Eye results gave general ocelli discussions and medicinal histology with lens-shaped stomata, without a focusing experiment; plant eye_type is none under owner 10(b). Harvest eye candidates concern Leonurus and Derris, other genera. Chemical keyword hits on rosemary, Dracocephalum, Rosa and Salvia concern other genera; Marrubium distilled-oil and extract studies are excluded under 10(a). Family query produced broad photoreceptor and Lamiaceae reviews, without a Marrubium measurement in the snippets.

Web result titles/snippets exposed in tool output were screened; counts vary and no guaranteed 20 results per query is claimed. Some combined execution outputs were truncated; these remain partial screens, never exhaustion claims. Canon, existing evidence, wanted and owner papers-status checked locally. OpenAlex missing API steps skipped after coordinator HTTP 429; full protocol incomplete, no null searched rows. No evidence or paper assets written.

Queries run, word for word:

- `web: Marrubium seed germination light dark`
- `web: Marrubium germination gibberellin OR smoke OR dormancy`
- `web: Marrubium floral scent volatiles`
- `web: Marrubium flower opening time anthesis`
- `web: white horehound flower opening time anthesis`
- `web: Marrubium plant ocelli lens-like epidermal cells eye`
- `web: white horehound plant ocelli lens-like epidermal cells eye`
- `web: Marrubium response to airborne volatile signals`
- `web: white horehound response to airborne volatile signals`
- `web: Lamiaceae photoreceptor review`

Successful stored harvest queries reviewed, in stored order (not rerun):

- `Marrubium phytochrome photoreceptor`
- `Marrubium light perception`
- `Marrubium phototropism`
- `Marrubium flower opening time`
- `Marrubium nyctinasty`
- `Marrubium anthesis`
- `Marrubium pollination biology`
- `Marrubium volatile signalling`
- `Marrubium epidermal lens cells`
- `Marrubium epidermal focusing leaf optics`
- `Lamiaceae photoreceptor review` (stored family review)
- citation step: works citing 10.1111/een.12947 that name Marrubium: 0
- citation step: works citing 10.1016/j.isci.2022.104455 that name Marrubium: 0

Checkpoint: 7 genera web-screened for the round, all protocol-partial; 0 new full-protocol completions, 0 searched rows, 29 wanted lines total, 0 evidence. Remaining unreviewed 33; exact next Lycopus.

### Lycopus (2026-10-27 continuation)

Web screening performed for this round with two new hormone/germination reading leads. Existing L. europaeus light/dark germination evidence sweep-25#10 is adopted; light-only germination papers are not re-requested. Gypsywort was chosen as a specific common name to avoid Ajuga bugleweed ambiguity. Diel snippets gave seasonal flowering; harvested Disguises in Bud Arrangement concerns architecture, and the interval-camera paper concerns pollinator monitoring with no Lycopus daily-opening result in the stored abstract. Harvest eye candidates are Sorbarieae and Leonurus anatomy in other genera. No genus-specific focusing experiment emerged; plant eye_type is none under 10(b). The chemical harvest hits are broad reviews, soil/vegetation surveys, animal biofilm/cancer work or extracts of other genera; none establishes a living Lycopus volatile-response result. Essential-oil composition of harvested Lycopus material is excluded under 10(a). Family review query supplied broad photoreceptor reviews and Lamiaceae material without a Lycopus measurement visible in snippets.

Web result titles/snippets exposed in tool output were screened; counts vary and no guaranteed 20 results per query is claimed. Some combined execution outputs were truncated; these remain partial screens, never exhaustion claims. Canon, existing evidence, wanted and owner papers-status checked locally. OpenAlex missing API steps skipped after coordinator HTTP 429; full protocol incomplete, no null searched rows. No evidence or paper assets written.

Queries run, word for word:

- `web: Lycopus seed germination light dark`
- `web: Lycopus germination gibberellin OR smoke OR dormancy`
- `web: Lycopus floral scent volatiles`
- `web: Lycopus flower opening time anthesis`
- `web: gypsywort flower opening time anthesis`
- `web: Lycopus plant ocelli lens-like epidermal cells eye`
- `web: gypsywort plant ocelli lens-like epidermal cells eye`
- `web: Lycopus response to airborne volatile signals`
- `web: gypsywort response to airborne volatile signals`
- `web: Lamiaceae photoreceptor review`

Successful stored harvest queries reviewed, in stored order (not rerun):

- `Lycopus phytochrome photoreceptor`
- `Lycopus light perception`
- `Lycopus phototropism`
- `Lycopus flower opening time`
- `Lycopus nyctinasty`
- `Lycopus anthesis`
- `Lycopus pollination biology`
- `Lycopus volatile signalling`
- `Lycopus epidermal lens cells`
- `Lycopus epidermal focusing leaf optics`
- `Lamiaceae photoreceptor review` (stored family review)
- citation step: works citing 10.1111/een.12947 that name Lycopus: 0
- citation step: works citing 10.1016/j.isci.2022.104455 that name Lycopus: 0

Checkpoint: 8 genera web-screened for the round, all protocol-partial; 0 new full-protocol completions, 0 searched rows, 31 wanted lines total, 0 evidence. Remaining unreviewed 32; exact next Allium.

### Allium (2026-10-27 continuation)

Web screening performed for this round. Both required tools report no stored harvest. Twenty-one new leads cover seed germination, GA/ethylene responses, floral emission, herbivory-induced emissions, daily anthesis and garlic/light experiments. Existing A. cepa photoperiod evidence sweep-8#19 and A. ursinum illumination evidence oa-14#10/#12 are adopted; neither supplies all congeners. Already-wanted Herbivory-induced systemic signals are likely to be evolutionarily conserved in euphyllophytes (harvest-c8, 10.1093/jxb/erab349, spring-onion chemical cue/response experiment) and Plant volatiles as cues and signals in plant communication (harvest-c11, 10.1111/pce.13910, onion donor and potato receiver) are adopted without duplicate requests. Nothoscordum/Allium comparison already wanted under harvest-c10 is also retained for reader verification of Allium coverage. Food aroma, frying, freshly cut onion chemistry and tissue metabolomics are excluded under 10(a). Eye queries returned anatomy, fluorescent-cell chemistry and general ocelli essays without an Allium focusing experiment; plant eye_type is none under 10(b). Family-review search produced general photoreceptor reviews and an Amaryllidaceae phytochemistry review, no additional genus-specific measurement in the snippets. Common name wild onion is broad within this genus; actual species were kept when provided.

Web result titles/snippets exposed in tool output were screened; counts vary and no guaranteed 20 results per query is claimed. Some combined execution outputs were truncated; these remain partial screens, never exhaustion claims. Canon, existing evidence, wanted and owner papers-status checked locally. OpenAlex missing API steps skipped after coordinator HTTP 429; full protocol incomplete, no null searched rows. No evidence or paper assets written.

Queries run, word for word:

- `web: Allium seed germination light dark`
- `web: Allium germination gibberellin OR smoke OR dormancy`
- `web: Allium floral scent volatiles`
- `web: Allium flower opening time anthesis`
- `web: wild onion flower opening time anthesis`
- `web: Allium plant ocelli lens-like epidermal cells eye`
- `web: wild onion plant ocelli lens-like epidermal cells eye`
- `web: Allium response to airborne volatile signals`
- `web: wild onion response to airborne volatile signals`
- `web: Allium light response photoperiod`
- `web: wild onion light response photoperiod`
- `web: Amaryllidaceae photoreceptor review`

Successful stored harvest queries reviewed, in stored order (not rerun):


Checkpoint: 9 genera web-screened for the round, all protocol-partial; 0 new full-protocol completions, 0 searched rows, 52 wanted lines total, 0 evidence. Remaining unreviewed 31; exact next Orchis.

### Orchis (2026-10-27 continuation)

Web screening performed for this round with six new leads: militaris light/PGR cultures, italica germination light regimes, mascula hormone trials cited in Biological Flora, emitted scent of mascula/simia, Basilicata scent survey and anthropophora scent review. No stored harvest reported by either required tool. Existing O. mascula floral emission sweep-16#3 adopted. The already-wanted Goodyera/Orchis germination study (10.1016/j.sjbs.2017.10.021 in this batch) explicitly includes O. mascula light and exogenous-carbon cultures and is adopted without duplication. Orchis coriophora snippets involve a possible Anacamptis taxonomic fork, left unassigned rather than inventing Orchis species coverage. Bletilla, Chloraea, Phalaenopsis and Chiloglottis experiments concern other genera. Diel results describe seasons, flower longevity and sequence along inflorescences, not a verified daily opening hour. Epidermal anatomy and spur papillae do not establish focusing or an eye; eye_type is none under owner 10(b). Distilled essential oils and tissue aroma are excluded under 10(a), while live floral sampling is marked for reader verification where method context is thin. Family review search returned Physiological diversity of orchids (10.1016/j.pld.2018.06.003) and orchid genomic reviews, with no new Orchis experiment in the snippets. One proxy-mirror OUP result (0-academic-oup-com.legcat.gov.ns.ca) was not opened.

Web result titles/snippets exposed in tool output were screened; counts vary and no guaranteed 20 results per query is claimed. Some combined execution outputs were truncated; these remain partial screens, never exhaustion claims. Canon, existing evidence, wanted and owner papers-status checked locally. OpenAlex missing API steps skipped after coordinator HTTP 429; full protocol incomplete, no null searched rows. No evidence or paper assets written.

Queries run, word for word:

- `web: Orchis seed germination light dark`
- `web: Orchis germination gibberellin OR smoke OR dormancy`
- `web: Orchis floral scent volatiles`
- `web: Orchis flower opening time anthesis`
- `web: early purple orchid flower opening time anthesis`
- `web: Orchis plant ocelli lens-like epidermal cells eye`
- `web: early purple orchid plant ocelli lens-like epidermal cells eye`
- `web: Orchis response to airborne volatile signals`
- `web: early purple orchid response to airborne volatile signals`
- `web: Orchis light response photoperiod`
- `web: early purple orchid light response photoperiod`
- `web: Orchidaceae photoreceptor review`

Successful stored harvest queries reviewed, in stored order (not rerun):


Checkpoint: 10 genera web-screened for the round, all protocol-partial; 0 new full-protocol completions, 0 searched rows, 58 wanted lines total, 0 evidence. Remaining unreviewed 30; exact next Diplacus.

### Diplacus (2026-10-27 continuation)

Web screening performed for this round with three new leads: day-length response of Mimulus douglasii (taxonomic fork explicitly held for the reader), D. aurantiacus sun/shade study, and direct SO2 fumigation response. Already-wanted Deno germination compilation in this batch has its Diplacus reading scope appended from the mandatory first query. Already-wanted light-intensity meta-analysis 10.1111/nph.15754 (harvest-c12) is adopted as a table lead; exact Diplacus species coverage remains unverified. Dipsacus, Diplachne, Diplomorpha and Diplodium search hits are different genera. Erythranthe/Mimulus guttatus, lewisii and cardinalis experiments are not assigned to Diplacus. Diel snippets mostly give seasonal flowering or stigma closure, without a daily flower-opening hour. The harvested broad CO2 review gives no Diplacus-specific diel measurement in the stored abstract. Eye candidate Hypoxis is a pollinator-vision study of another genus, and general lens papers name other plants; plant eye_type is none under 10(b). Harvest scent candidates concern Helleborus, Jaborosa, Molineria, Clarkia/hawkmoth antennae or broad yeast and monkeyflower reviews. Jaborosa web snippets mention Diplacus in relation to flower colour and pollinator identity, not a Diplacus scent assay. Family search returned broad photoreceptor reviews without a genus-specific measurement in snippets. No source page was opened; proxy-mirror OUP result skipped.

Web result titles/snippets exposed in tool output were screened; counts vary and no guaranteed 20 results per query is claimed. Some combined execution outputs were truncated; these remain partial screens, never exhaustion claims. Canon, existing evidence, wanted and owner papers-status checked locally. OpenAlex missing API steps skipped after coordinator HTTP 429; full protocol incomplete, no null searched rows. No evidence or paper assets written.

Queries run, word for word:

- `web: Diplacus seed germination light dark`
- `web: Diplacus germination gibberellin OR smoke OR dormancy`
- `web: Diplacus floral scent volatiles`
- `web: Diplacus flower opening time anthesis`
- `web: sticky monkeyflower flower opening time anthesis`
- `web: Diplacus plant ocelli lens-like epidermal cells eye`
- `web: sticky monkeyflower plant ocelli lens-like epidermal cells eye`
- `web: Diplacus response to airborne volatile signals`
- `web: sticky monkeyflower response to airborne volatile signals`
- `web: Diplacus light response photoperiod`
- `web: sticky monkeyflower light response photoperiod`
- `web: Phrymaceae photoreceptor review`

Successful stored harvest queries reviewed, in stored order (not rerun):

- `Diplacus phytochrome photoreceptor`
- `Diplacus light perception`
- `Diplacus phototropism`
- `Diplacus flower opening time`
- `Diplacus nyctinasty`
- `Diplacus volatile signalling`
- `Diplacus photoperiod`
- `Diplacus circadian rhythm`
- `Diplacus anthesis`
- `Diplacus pollination biology`
- `Diplacus epidermal lens cells`
- `Diplacus epidermal focusing leaf optics`
- `Phrymaceae photoreceptor review` (stored family review)

Checkpoint: 11 genera web-screened for the round, all protocol-partial; 0 new full-protocol completions, 0 searched rows, 61 wanted lines total, 0 evidence. Remaining unreviewed 29; exact next Amelanchier.

### Amelanchier (2026-10-27 continuation)

Web screening performed for this round with eleven new leads. Direct live-response candidates include auxin/spermidine/GA, ABA, cytokinin/light, jasmonate elicitation and GA/BA cultures, with in-vitro limitations explicit. Seed germination title retained under 10(e), without claiming a light contrast when snippet shows only fixed conditions. Diel primary Observations on shoot morphology and anthesis is held for full-text timing verification; other harvest anthesis hits report fruit-development intervals, frost injury, floral organogenesis or other genera, and web snippets mainly give seasonal bloom. No genus-specific focusing experiment surfaced; leaf epidermis anatomy is not an eye and eye_type is none under 10(b). Fruit/biscuit/yogurt aroma, phytochemical extracts and dried powders are excluded under10(a). Harvest light candidates on Vaccinium, Prunus, Kalmia, cucumber, Populus and strawberry concern other genera; human retinal and rock-art matches are irrelevant. Broad light-culture review is a potential citation route, not evidence of a named Amelanchier measurement. The Rockwool study stored abstract gives culture setup but no demonstrated contrast; not used to claim an absent response. Rosaceae web review query returned broad plant and animal photoreceptor reviews rather than a new Amelanchier experiment. No existing Amelanchier evidence or wanted request was found locally.

Web result titles/snippets exposed in tool output were screened; counts vary and no guaranteed 20 results per query is claimed. Some combined execution outputs were truncated; these remain partial screens, never exhaustion claims. Canon, existing evidence, wanted and owner papers-status checked locally. OpenAlex missing API steps skipped after coordinator HTTP 429; full protocol incomplete, no null searched rows. No evidence or paper assets written.

Queries run, word for word:

- `web: Amelanchier seed germination light dark`
- `web: Amelanchier germination gibberellin OR smoke OR dormancy`
- `web: Amelanchier floral scent volatiles`
- `web: Amelanchier flower opening time anthesis`
- `web: serviceberry flower opening time anthesis`
- `web: Amelanchier plant ocelli lens-like epidermal cells eye`
- `web: serviceberry plant ocelli lens-like epidermal cells eye`
- `web: Amelanchier response to airborne volatile signals`
- `web: serviceberry response to airborne volatile signals`
- `web: Amelanchier light response photoperiod`
- `web: serviceberry light response photoperiod`
- `web: Rosaceae photoreceptor review`

Successful stored harvest queries reviewed, in stored order (not rerun):

- `Amelanchier phytochrome photoreceptor`
- `Amelanchier light perception`
- `Amelanchier phototropism`
- `Amelanchier flower opening time`
- `Amelanchier nyctinasty`
- `Amelanchier volatile signalling`
- `Amelanchier photoperiod`
- `Amelanchier circadian rhythm`
- `Amelanchier anthesis`
- `Amelanchier pollination biology`
- `Amelanchier epidermal lens cells`
- `Amelanchier epidermal focusing leaf optics`
- `Rosaceae photoreceptor review` (stored family review)

Checkpoint: 12 genera web-screened for the round, all protocol-partial; 0 new full-protocol completions, 0 searched rows, 72 wanted lines total, 0 evidence. Remaining unreviewed 28; exact next Orthilia.

### Orthilia (2026-10-27 continuation)

Web screening performed for this round with two new leads: pyroloid seed-culture light/chemical experiments and the named flower-biology source behind BSBI protandry observations (daily opening hour unverified). No existing Orthilia evidence or wanted request found locally. Common-name wintergreen queries produce Gaultheria and generic methyl-salicylate information, which was not assigned to Orthilia. Harvest light hit on site preparation is vegetation/silviculture rather than a controlled Orthilia light response. Pollen morphology light microscopy is an instrument, not light sensing. The already-requested chloroplast-movement thesis in this batch remains an unverified broad Ericaceae table/source lead, not a demonstrated Orthilia experiment. Harvest family eye hits concern human retinal protection and Vaccinium extract; the diel hit concerns animal visual transitions. No genus-specific focusing experiment surfaced; plant eye_type is none under10(b). Harvest Oidiodendron, seaweed, Calendula/Fagopyrum, Vaccinium, Sedum, Pseudorchis and Campanula results concern other organisms or ecological occurrence. Herbicide-toxicity thesis returned by photoperiod query names no Orthilia treatment in its stored abstract, so no negative response claim is based on it. Family web query returned broad photoreceptor reviews rather than a new genus-specific experiment. Floral-scent and chemical web searches returned general reviews without a verified Orthilia emission assay.

Web result titles/snippets exposed in tool output were screened; counts vary and no guaranteed 20 results per query is claimed. Some combined execution outputs were truncated; these remain partial screens, never exhaustion claims. Canon, existing evidence, wanted and owner papers-status checked locally. OpenAlex missing API steps skipped after coordinator HTTP 429; full protocol incomplete, no null searched rows. No evidence or paper assets written.

Queries run, word for word:

- `web: Orthilia seed germination light dark`
- `web: Orthilia germination gibberellin OR smoke OR dormancy`
- `web: Orthilia floral scent volatiles`
- `web: Orthilia flower opening time anthesis`
- `web: sidebells wintergreen flower opening time anthesis`
- `web: Orthilia plant ocelli lens-like epidermal cells eye`
- `web: sidebells wintergreen plant ocelli lens-like epidermal cells eye`
- `web: Orthilia response to airborne volatile signals`
- `web: sidebells wintergreen response to airborne volatile signals`
- `web: Orthilia light response photoperiod`
- `web: sidebells wintergreen light response photoperiod`
- `web: Ericaceae photoreceptor review`

Successful stored harvest queries reviewed, in stored order (not rerun):

- `Orthilia phytochrome photoreceptor`
- `Orthilia light perception`
- `Orthilia phototropism`
- `Orthilia flower opening time`
- `Orthilia nyctinasty`
- `Orthilia volatile signalling`
- `Orthilia photoperiod`
- `Orthilia circadian rhythm`
- `Orthilia anthesis`
- `Orthilia pollination biology`
- `Orthilia epidermal lens cells`
- `Orthilia epidermal focusing leaf optics`
- `Ericaceae photoreceptor review` (stored family review)

Checkpoint: 13 genera web-screened for the round, all protocol-partial; 0 new full-protocol completions, 0 searched rows, 74 wanted lines total, 0 evidence. Remaining unreviewed 27; exact next Viola.

### Viola (2026-10-27 continuation)

Web screening performed for this round. Only sense_chemical is open in the required tool output; seven reading leads added for GA3 seed response, timed living floral emission, V. etrusca in-vivo scent, CaCl2 treatment, GA signalling, and two mandatory germination-title leads whose chemical treatments need verification. Existing canon-3#672 receiver experiment for V. odorata is adopted; its species-specific effect direction is only partial. The old genus-level photoperiod row sweep-5#15 is explicitly retracted in audit ALL, so it is not treated as valid measured evidence; existing pansy light evidence harvest-9#1 is distinct. No null record is written for a trait already bearing evidence. Viola music, violist, Bill Viola art and software-name results are unrelated. Extracts, hydrolates, absolutes and food sensory profiles are excluded under10(a). Borage/pansy food-volatiles paper has no stored abstract, so it is not used as negative evidence; the verified in-vivo emission leads are retained instead. Other harvest scent keywords include other organisms, fluorescence wording, general methods, a broad pathogen review, and an existing canon meta-analysis. Family web query returned general plant photoreceptor reviews and Viola taxonomy rather than another specific chemical-response experiment. No additional searches were run on already-covered trait groups.

Web result titles/snippets exposed in tool output were screened; counts vary and no guaranteed 20 results per query is claimed. Some combined execution outputs were truncated; these remain partial screens, never exhaustion claims. Canon, existing evidence, wanted and owner papers-status checked locally. OpenAlex missing API steps skipped after coordinator HTTP 429; full protocol incomplete, no null searched rows. No evidence or paper assets written.

Queries run, word for word:

- `web: Viola seed germination light dark`
- `web: Viola germination gibberellin OR smoke OR dormancy`
- `web: Viola floral scent volatiles`
- `web: Viola response to airborne volatile signals`
- `web: violet response to airborne volatile signals`
- `web: Violaceae photoreceptor review`

Successful stored harvest queries reviewed, in stored order (not rerun):

- `Viola phytochrome photoreceptor`
- `Viola light perception`
- `Viola phototropism`
- `Viola volatile signalling`
- `Violaceae photoreceptor review` (stored family review)
- citation step: works citing 10.1111/ele.12205 that name Viola: 0
- citation step: works citing 10.1093/aobpla/plag030 that name Viola: 0
- citation step: works citing 10.1038/144514b0 that name Viola: 2

Checkpoint: 14 genera web-screened for the round, all protocol-partial; 0 new full-protocol completions, 0 searched rows, 81 wanted lines total, 0 evidence. Remaining unreviewed 26; exact next Anemonastrum.

### 2026-10-27 worker 8 handoff

New genera screened in this worker: Marrubium, Lycopus, Allium, Orchis, Diplacus, Amelanchier, Orthilia, Viola (8). Adopted prior six: Scilla, Diphasiastrum, Xanthium, Goodyera, Lysichiton, Calamagrostis. Cumulative round web-screened-for-round coverage is 14/40, all protocol-partial; this is not a complete full-protocol or exhaustion count. Some combined tool outputs were truncated, explicitly qualifying the exposed-title/snippet screening; no null search row was authorized. New wanted lines 58; batch total 81. Two existing requests gained confirmed extra reading scope (Orchis in the Goodyera germination paper and Diplacus in the Deno compilation). Searched rows 0; evidence 0.

Stopped between genera at context checkpoint. Remaining genuinely untouched: 26. Exact next: Anemonastrum, then Polypodium, Arctium, Galinsoga, Anthyllis, Opuntia, Maclura, Armeria, Hesperoyucca, Ericameria, Rhododendron, Yucca, Arum, Asarum, Corydalis, Lycopodium, Cylindropuntia, Hordeum, Hydrophyllum, Draba, Adenostoma, Claytosmunda, Larix, Amauropelta, Umbellularia, Veratrum. OpenAlex remains skipped after the coordinator HTTP 429; no additional service refusal occurred. No source pages fetched, no full text or evidence assets written.


## 2026-10-27 — issue38 coordinator shared Deno target

Worker17 c11 germination search returned indexed Deno1.pdf text naming Senecio aureus and a germination light requirement (retained Packera-web5.json). UTK Smart Yards title explicitly pairs Packera aurea with Senecio aureus. Expanded existing wanted line16 for Packera aurea, preserving Lysichiton/Diplacus requests, original source metadata and all prior provenance. No new wanted line, source-page fetch or measurement. Packera queue count used for ranking; source-level species/table verification stays with the reader. Wanted count81, searched/evidence0.
