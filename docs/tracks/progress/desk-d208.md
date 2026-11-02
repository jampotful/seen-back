# desk-d208 progress

Screen of open-licence animal sensory-trait records. Five records filed in docs/views/evidence/desk-d208.jsonl (check.py: 0 problems). Most search hits were already on main (DOI present in docs/views), so the yield is low.

## Records filed
- Pygocentrus nattereri (Characiformes), behaviour_vision x3, Agrillo and Pecunioso 2024, Animals 14(22): 3187, 10.3390/ani14223187 (MDPI, CC BY). Black vs white learning for each of two juveniles (fixed side, so response plus place learning) and the red vs green null.
- Scolia hirta (Scoliidae, parasitoid wasp), interommatidial_deg, Ferrari and Polidori 2026, Insects 17(2): 160, 10.3390/insects17020160 (MDPI, CC BY). Males have more ommatidia and a smaller interommatidial angle (categorical; angle computed from ommatidia number).
- Megaphragma viggianii (Trichogrammatidae), sense_hearing, Diakova et al. 2022, Scientific Reports 12: 20172, 10.1038/s41598-022-24390-4 (CC BY 4.0 per the article page). 19 Johnston's organ scolopidia (anatomy only).

## Queries (WebSearch, about 37 of 40)
Plecoptera drumming; pit viper infrared threshold; Pacific rattlesnake IR 2018; Trichoptera larvae vision; Opiliones photoreceptor; Gobiidae sensory; Characiformes sensory; Odonata larva sensory; Danionella; Nasonia/parasitoid; piranha/neon tetra; Hogna/Lycosidae vibration; bat vision opsin; scorpion UV/vibration; centipede/millipede eyes; Anguilla/moray; Orthoptera hearing (x2); site-restricted peerj/mdpi/frontiers/plos queries for spiders, Orthoptera, reptiles, fish, rodents/marsupials/bats; Rhinogobius/Gobiusculus; rodent/marsupial/Cypriniformes/bird hearing; Acheta/Gryllodes; stonefly nymph; Python infrared; caddisfly larvae; damselfly larvae; frontiers dragonfly/harvestman; mdpi parasitoid antennae; mdpi reptile; turtle sensory; bat Pteropodidae; salticid; scorpion substrate; bushcricket; mole-rat; Schizocosa/Pardosa; Trichogramma/Cotesia; mudskipper; stonefly light.

## Held out (already on main by DOI or species/trait)
10.3389/fevo.2023.1085975 (Astyanax), 10.1186/s12983-016-0182-9 (harvestmen), 10.3389/fevo.2022.856660 (Trachemys hearing), 10.1371/journal.pone.0108583 (carp and catfish hearing), 10.3389/fphys.2013.00248 (bat vision and echolocation), 10.1098/rsos.230907 (jumping spider stripes), 10.3389/fevo.2022.939133 (Schizocosa retrorsa), 10.1371/journal.pone.0006390 (bat UV cones), Jeb 2018 Crotalus oreganus IR (species and trait on main).

## Held out (other reasons)
- Elacatinus lori larval sensory development, Sci Rep 2021, 10.1038/s41598-021-91640-2 (from a DOAJ page): nature.com refused the single try (permission not answered), not read. Goby gap remains open; try again with another session.
- Anagyrus vladimiri antennal sensilla, Insects 13(12): 1138, 10.3390/insects13121138 (CC BY): counts such as about 28 multiporous plate sensilla on the apical antennomere sit in sentences that the fetch tool returns only in pieces, and the quoted sentence names neither the sensillum type nor the species. Needs a full-text reading.
- Scolia hirta sensilla (seven female and nine male types) and ocellus size: no trait key fits cleanly and the function statement is in a joined abstract sentence.
- Schizocosa crassipalpata and S. bilineata mating (Frontiers in Ethology 3: 1460323, 10.3389/fetho.2024.1460323, CC BY): species not in gbif-names.tsv, and the results are mating outcomes with ornament manipulation, not a sensory measurement.
- Hu et al. 2022 mudskipper cornea, 10.3389/fevo.2022.871370 (CC BY): gene-evolution and corneal microstructure, no sensory value that fits a trait key.
- Vonk et al. 2025 snake scent null (Frontiers in Ethology 4: 1634578): nine species pooled.
- Tian et al. 2022 marsupial vision genes (10.3389/fevo.2022.982073) and Fossesca et al. 2023 bird auditory review (10.3389/fevo.2023.1233911): genomics and review, no species measurement.
- Korsunovskaya and Zhantiev 2022, PeerJ 10: e13749: sound production, not reception.
- Springer, PMC and Anubis-blocked pages not retried (centipede 10.1186/s12983-021-00442-9, Frontiers in Zoology; bat PLoS ONE pdf mirror).
- Unreached target groups with no usable hit: Plecoptera, Trichoptera, Odonata larvae, Opiliones, Myriapoda, Anguilliformes, snake pit organs, rodent and marsupial vision.

## Owner questions
1. Pygocentrus nattereri, Scolia hirta and Megaphragma viggianii are absent from docs/views/gaps/gbif-names.tsv (Megaphragma viggianii appears on main only as "(female)" in the bee audit). Please confirm accepted names.
2. Megaphragma record uses sense_hearing for a Johnston's organ scolopidia count (anatomy, no physiology). If you want a dedicated organ-presence trait or sense_airflow instead, say so.
3. The piranha records are two juveniles and partly a null result. Keep, or drop as too weak?
4. The Serrasalmidae family hearing record from d206 is a different paper (10.1038/s41598-018-19812-1).

## Desk disposition after audit 292

Audit 292: 4 of 5 records in error (80%): two fixable, two held out. Pooled audits 172 to 292: 283 of 648 (43.7%) with audit 291 counted. Merged with the auditor's replacement text: the two Pygocentrus nattereri black-versus-white records (each fish's rewarded stimulus sat on a fixed side that matched its earlier side bias, so response and place learning are confounded; Little José's value no longer carries a figure absent from his sentence) and the red-versus-green null (RGB values, no luminance matching, randomised side).

Held out: line 4 (Scolia hirta), because the angle is computed from the ommatidia count, so the grade would be i and the row holds no degree value until Table 1 is read; line 5 (Megaphragma viggianii), because a Johnston's organ scolopidia count is anatomy with no function tested and sense_hearing records a Hz range.

Owner questions: add Pygocentrus nattereri, Scolia hirta and Megaphragma viggianii to gbif-names.tsv; a trait key for sense-organ anatomy with no function tested (for example chordotonal_organs) or a ruling that such counts are not filed; whether a computed interommatidial angle is graded i and whether a comparison without a degree value may sit in interommatidial_deg.
