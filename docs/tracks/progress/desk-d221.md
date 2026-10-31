# desk-d221 progress

Scope: animal sensory-trait records from open full text (MDPI, Frontiers, PLOS). Records are in docs/views/evidence/desk-d221.jsonl; check.py reports 0 problems for the unit. Species and DOI were checked against origin/main (evidence, audit/corrected, audit/ALL, sheets, progress notes) before opening each paper, and Crossref confirmed authors, volume, article number and licence for every DOI filed.

## Records (11)
- Serangium japonicum (Insects 17(7): 661), behaviour_vision: negative phototaxis at 400 nm reached 57.14 ± 7.14% at 600 uW cm-2 (Y-tube; side randomisation and sex not stated).
- Anomalops katoptron (PLoS ONE 13(7): e0198765), three records: recombinant RH1/RH2 lambda max about 490 nm (abstract sentence), whole-retina ERG peak at 480 nm (new trait erg_peak_nm, as oa-4 used it), attraction to low-intensity blue but not red light (behaviour_vision; fish also associated red with feeding).
- Xenopus laevis (Front. Behav. Neurosci. 14: 71), behaviour_vision: stage 48/49 tadpoles most often found with 3 or 4 of 10 in the green quadrant; percentages are in conditions as paraphrase.
- Melipona eburnea (Insects 10(11): 412), sense_chemical: conditioned PER higher to guava than to mango odour; number of bees not stated in the paper.
- Huia cavitympanum (PLoS ONE 4(4): e5413), two sense_hearing records: torus semicircularis AEP most sensitive between about 20 and 28 kHz (six males), eardrum vibration wideband sensitivity about 7 to 30 kHz (eight ears, six males).
- Pieris rapae (PLoS Genet. 17(7): e1009527), sense_chemical: fifth-instar larvae, sinigrin PI 0.89 ± 0.030 at 1e-4 M in a two-choice leaf-disc assay.
- Chrysomela populi (Front. Physiol. 10: 343), two sense_chemical records: sensilla chaetica subtype 2 at 19.6 Hz to salicin 100 mM (close to the KCl control, stated in conditions) and a null for subtype 1.

## Held out
- Crematogaster scutellaris trail pheromone (Sci. Rep. 14: 7883): page showed only "Open access", no licence sentence; abstract (1 ng/uL) and Results (0.1 ng/uL) disagree.
- Trypodendron lineatum (Front. Physiol. 14: 1155129) and Ips acuminatus / I. cembrae (Front. For. Glob. Change 2025.1588866): sensilla-recording papers not on main, but the fetched /full pages ended before the licence sentence; /pdf forms needed permission. A reader with the page could file the lineatin class (37 of 90 strongly responding OSNs) and the Ips acuminatus IAc6 class (> 80 Hz to alpha-isophorone, n = 6).
- Odontoponera transversa and termite signals (Insects 17(5): 501): key sentences over the quote limit; stimuli are gland extracts and live termites mixed.
- Haemaphysalis darjeeling Haller's organ (Biosensors 15(6): 358): internal inconsistencies in values and compound names.
- Carausius morosus antennal lobe (Front. Physiol. 2026.1873043): no licence line returned.
- Snakes (PLoS ONE 18: e0281285) and the corn snake / nine-species scent paper (Front. Ethol.): results pooled by genus or species.
- Copepod internal-wave paper: mixed population of three species. Neoseiulus californicus (Insects 17(2): 157): nulls only, no unbaited control. Cells 15(20): 1886 dark-reared G. charrua and medaka: acuity values in figures, medaka is a lab strain.
- African mole-rat bone conduction (Audiol. Res. 15(3): 64): review, no new data.
- Fully blocked or failing: PeerJ pages (21421 owls, 21156 walleye) client error; journals.biologists.com (JEB 251857 butterfly olfactory, 249258 harbour seal vortex, Biol. Open 062674 cichlid) refused earlier by other units and not retried; mdpi Animals 16(12):1799 lizard retina asked via a built URL, permission not answered.
- Already on main by species or DOI: Gekko gecko, Eublepharis, Phoca vitulina, Chelonia mydas, Babina daunchina, Odorrana tormota, Salamandra, Pardosa astrigera, Greenland shark, odontocete audiograms, cichlid and catfish hearing, wallaby colour vision (Macropus eugenii), Frankliniella occidentalis, Protaetia, Lymnaea, planarian phototaxis.

## Owner questions
- Frontiers /full pages come back truncated before the licence sentence in the fetch tool; Crossref gives CC BY 4.0 for all of them. Should a Crossref CC BY plus a publisher open-access page count as the licence statement, so Trypodendron and Ips can be filed?
- Melipona eburnea records an odour-reward conditioning result under sense_chemical; say if learned-response papers belong there.
- Page metadata versus Crossref licence versions: Serangium (page 3.0, Crossref 4.0), Melipona (3.0 versus 4.0). Accepted as CC BY.
- Anomalops lambda_max_nm is a recombinant GIRK activation maximum in HEK293 cells, filed with that stated in eye and conditions.
- Taxon families for Anomalops (Anomalopidae, Beryciformes) and Huia (Ranidae) are from memory of current usage, not checked against GBIF or ASW (refused or not reachable).
