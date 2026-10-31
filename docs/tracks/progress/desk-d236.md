# desk-d236 (animal sensory records, 31 Oct 2026)

About 28 WebSearches. Each candidate DOI was grepped against the whole docs/ tree at origin/main and the d230 to d235 evidence (unmerged branches included) before opening. Crossref single-DOI lookups through WebFetch; OBIS taxon lookup (api.obis.org/v3/taxon) opens and gave family and order for fish and isopod.

## Filed (8 records, docs/views/evidence/desk-d236.jsonl)
1-2. Cyclopterus lumpus (Cyclopteridae), sense_magnetic: Durif et al. 2023, PeerJ 11: e14745, 10.7717/peerj.14745. Null for activity and distance travelled (abstract sentence in two pieces) and a 16% lower swimming speed with the coil on (three pieces, exactly 40 words). Hatchery fish, 24 per treatment, coil on/off trials alternated, field up to 230 uT measured with a smartphone magnetometer, ambient 51 uT. The authors say fish may have sensed the field or the induced electric field. Page prints CC Attribution License; Crossref CC BY 4.0 unspecified.
3-4. Empoasca onukii (Cicadellidae), lambda_max_nm: Bian et al. 2020, Insects 11(7): 426, 10.3390/insects11070426. ERG peaks 540 nm (primary) and 355 nm (secondary); fitted pigments 356, 435, 542 nm in conditions; sexes did not differ; insect number not stated; lab-reared. Page CC BY 3.0, Crossref CC BY 4.0 vor. Peaks are whole-eye ERG, not single-pigment values.
5. Deilephila elpenor (Sphingidae), behaviour_vision: van der Kooi and Kelber 2022, Front. Ecol. Evol. 10, 10.3389/fevo.2022.819436. 11 of 12 responders chose the brighter of two same-hue blue stimuli (p = 0.006), 3 non-responders excluded, 10 lux measured.
6. Macroglossum stellatarum (Sphingidae), behaviour_vision: same paper, 21 of 24 probed Light Blue (p < 0.01), 100 lux. This is a different paper from the held pone.0034629.
7-8. Cymodoce japonica (Sphaeromatidae, Isopoda), behaviour_vision: Suzuki et al. 2026, J. Mar. Sci. Eng. 14(19): 1858, 10.3390/jmse14191858. Dark v red no difference (p = 0.191, null); red longer than green and blue (p < 0.001 each). 30 active wild-caught isopods, inactive ones excluded, light set not measured. Resolves the d235 hold (family from OBIS; Results sentences read in two pieces).

## Held leads and why
- Argiope keyserlingi vibratory courtship (pone.0053057, Wignall and Herberstein 2013): family verified Araneidae (World Spider Catalog), but the female latency result is a correlation with male shudder rate; vision and contact are not separated from web vibration, no control group. Sentences read in two pieces.
- Apis mellifera 1 and 1.7 mT 50 Hz exposure (Animals 12(7): 855): artificial mT-level ELF field, not a geomagnetic-sense test; cage and bee counts inconsistent (10 cages x 6 bees against 9 per group).
- Dendrobatid frogs ERG (pone.0312578): no lambda max reported, per-species family not assigned, n per species not in text read.
- Maratus volans (pone.0025390): male signal production only, no female response measured.
- Already on main or unmerged: lumpfish nothing; Boute 2024 electric thresholds (all five species), Merivee 2020 elaterid heat (d155), Amalosia (unmerged), peerj.12351, 5819, 17962, 16379, pone.0001676, 0124728, 0123205, pone.0057588, 0067049 and the fish hearing papers.
- Not senses or review: Ketten et al. fevo.2021.661216 (anatomy, bats and cetaceans), fphys.2016.00150 (perspective), finsc.2025.1625155 (bibliometric), fmars.2023.1129057 (review), Mormyrid activity patterns (fevo.2022.870043), UV frog colouration (famrs.2025.1669704).
- Long-Evans/Brattleboro rat ABR (pone.0222096): domestic lab strains.

## Owner questions
1. Trait key for ERG peaks of a whole compound eye (records 3-4): lambda_max_nm as filed, or a whole_eye_spectral_peak_nm key (24 rows on main)? Main has that key.
2. Family for Sphingidae taken from the paper's Table 1 group row (records 5-6), which names no species: acceptable?
