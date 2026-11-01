# desk-d205 progress

Task: 5 to 10 new animal sensory-trait records from open papers, aimed at groups thin on main.

## Coverage map (evidence + audit/corrected, species per order, sensory keys)
Thin or empty on main: Esox (none), Syngnathidae (none), Gobiidae (none), Mormyridae (1 species), Characiformes (1), Orthoptera 18, Blattodea 7, Opiliones 9, Scorpiones 13, Neuroptera 10, Cypriniformes 12, Testudines 27 (mostly hearing/colour of marine turtles), Trichoptera 1, Dermaptera 1, Ixodida 6, Trombidiformes 2, Crassiclitellata 4. Dendrobaena, Echinotriton and Tiliqua adelaidensis had no rows (grep of docs/views, including audit/corrected and audit/ALL, by genus and by paper title/DOI before filing).

## Records filed: 6 (docs/views/evidence/desk-d205.jsonl)
- Dendrobaena veneta, sense_chemical x2 (CO2 exudate dose response; acetazolamide) - Smith et al. 2023, Front Ecol Evol 11:1202410, CC BY (Crossref license verified).
- Tiliqua adelaidensis, sense_chemical - Daniell et al., Aust J Zool 68(2):76-84 (Crossref: issued 2021), CSIRO page footer CC BY-NC.
- Echinotriton chinhaiensis, behaviour_vision (visual cue), sense_chemical x2 (activity drop; null avoidance) - Feng et al. 2026, Animals 16(2):261, CC BY.

## Queries (WebSearch, about 27)
Turtle underwater hearing audiogram; tortoise/terrapin vision; cyprinid lateral line/hearing; cockroach/earwig/mole cricket/katydid; lizard/gecko/skink opsin; scorpion/harvestman/vinegaroon; fathead minnow/bitterling/carp/roach; Tiliqua rugosa short-wavelength; Frontiers turtle sensory; MDPI cockroach/cricket; PeerJ lizard/snake/gecko; seahorse/pipefish; northern pike; goby/mudskipper; Hippocampus MDPI/PLOS; mormyrid/arowana; stonefly/mayfly/caddisfly; flea/louse/bed bug/silverfish; lungfish/bichir/gar; Frontiers Zoology/BMC; RSOS/PeerJ gecko/snake/salamander; Frontiers fish larvae; Frontiers reptile cue; Frontiers cricket/cockroach; PeerJ salamander/newt; Chinhai spiny newt; Daniell reptile predator scent; earthworm Dendrobaena CO2; Jolly sleepy lizards.

## Held out (reason)
- Red-eared slider temperature hearing, fevo.2022.856660: already on main (desk-d154).
- Tiliqua rugosa blue-tongued skink spectral sensitivity, JEB 225(11) jeb244317: already on main (recheck-codex-b, opsin_classes/acuity), fetch showed no licence line; skipped.
- Tiliqua rugosa smoke/fire-sound study, Biology Letters 2025 (doi 10.1098/rsbl.2025.0364, CC BY per MQ page): only the abstract reached me (fetch paraphrased it, no verbatim sentences, full PDF fetch failed); open lead for a unit with a working route to the full text.
- Ephoron virgo larval negative phototaxis, JEB 227 jeb247142 (10.1242/jeb.247142): repository PDF shows only the Company of Biologists copyright line, no open licence; findings read (400 nm maximum, 517 and 743 nm null).
- Hippocampus abdominalis/taeniopterus visual resolution (Visual Neuroscience 28(4):351, 10.1017/S0952523811000149): Cambridge page blocked, abstract only via ANU portal, licence unknown. Hippocampus (seahorse) has no rows on main, a good target.
- Neon goby Elacatinus lori larval sensory development, Sci Rep 11 (10.1038/s41598-021-91640-2): nature.com is refused; no other copy found. Gobiidae has no rows on main.
- Paruroctonus utahensis peg sensilla, J Arachnol 52(1) JoA-S-22-052: title/authors/DOI did not come through the fetch; species is already heavily covered.
- Cimex hemipterus CO2 behaviour, J Econ Entomol 114(5) toab159: bioone page returned no text.
- Hippocampus barbouri optical development (UMS eprints 40838): master's thesis.
- Tiliqua rugosa spectral sensitivity bioRxiv 2022.03.25.485754: preprint.
- Crickets and wind escape (Gryllus bimaculatus, Sci Rep 7:15158): species heavily covered.
- Reviews (fevo.2021.667218, fevo.2021.641740, fevo.2024.1382933 editorial): no measured data of their own.

## Owner questions
1. The Dendrobaena CO2 result is an exudate (irritation) response, filed as sense_chemical with the 25% null in conditions; confirm that exudate output counts as a chemical-sense measurement for annelids.
2. The Tiliqua adelaidensis page footer says CC BY-NC while Crossref lists CC BY-NC-ND (2025 version of record); either is open for reading, but say if the NC-ND text should bar the record.
3. Echinotriton chinhaiensis is not in gbif-names.tsv; the species name is as the paper gives it.

## Desk disposition after audit 289

Audit 289: 6 of 6 records in error (100%). Pooled audits 172 to 289: 275 of 632 (43.5%). The two Dendrobaena veneta rows duplicated desk-d204:2 and :3 (the unit branched before d204 merged) and were dropped. The Tiliqua adelaidensis and three Echinotriton chinhaiensis rows merged with the auditor's replacement conditions: lizards were tested in the field at their burrows; the larval trials were run control first and cue second with the same larvae, so cue effect is confounded with trial order; the 4 min interaction text and Table 2 disagree.

Tiliqua licence: the CSIRO copy read prints "Open Access CC BY-NC", so the rule for CC BY-NC applies; Crossref's CC BY-NC-ND is the version-of-record licence from 2025-05-26.

Owner questions: Tiliqua adelaidensis and Echinotriton chinhaiensis are accepted names (Reptile Database; Amphibian Species of the World) but are not in gbif-names.tsv; whether earthworm exudate counts as sense_chemical (d204); whether a fixed control-then-cue order in the Echinotriton trials is acceptable for behaviour_vision and sense_chemical rows; seahorses and gobies remain uncovered.
