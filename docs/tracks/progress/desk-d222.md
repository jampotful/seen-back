# desk-d222 progress

Scope: animal sensory-trait records from open full text. Records are in docs/views/evidence/desk-d222.jsonl; check.py reports 0 problems for the unit. About 33 WebSearches and 55 WebFetch pages. Every species and DOI was checked against origin/main (evidence, audit, searched, sheets, progress notes) before a paper was opened.

Host access this session: peerj.com opened for pages up to about e20507 (newest article numbers e21156 and e21231 returned a client error); api.crossref.org opened intermittently (rate limited); mdpi.com, frontiersin.org (opened once, then not), biologists.com, nature.com, biomedcentral.com and plos.org (rate limited) returned PROVENANCE_REQUIRED or rate-limit errors and were not retried.

## Records (3)
- Stygoparnus comalensis (Dryopidae), PeerJ 13: e20507, behaviour_vision: 90% of adults on the dark side under UVA light (395-400 nm). Conditions carry the unrandomised light side, repeated checks on the same beetles, the white/red/blue/green/no-light rows of Table 1 and the Discussion caveat.
- Podarcis lilfordi (Lacertidae), PeerJ 5: e2828, sense_chemical: null result, no recognition of three snake odours in three islet populations (24 lizards each, random treatment order, sexes pooled).
- Pimephales promelas (Cyprinidae), PeerJ 10: e13988, sense_chemical: an intact olfactory system is required for copper sensing; group statistics, tissue-glue anosmia, unverified nominal concentration and the authors' mechanism caveat are in conditions.

## Held out
- Acheta domesticus predator-odour (PeerJ e4923): page shows no licence line or volume; female result sentences over 125 characters; commercially bred stock.
- Thamnophis melanogaster neonates (PeerJ 8: e8718): population comparison, key sentences truncated.
- Littorina/Littoraria irrorata climbing response (PeerJ 6: e5744): no whole sentence carries the cue-versus-control result; page prints Littorina.
- Maylandia zebra unimodal cues (PeerJ 5: e3643): Abstract sentences over 125 characters and a Discussion that says holding water makes fish aware of a contestant while Results report no agonistic effect.
- Cosmopolites sordidus fungal VOC (PeerJ 13: e19414): licence is the Open Government Licence and the text and means disagree in direction for Experiment 4.
- Rana aurora tadpoles (PeerJ 12: e17307): only a p value sentence fits; tadpole differences are in longer sentences.
- Principapillatus hitoyensis ERG (PeerJ 5: e3595): re-analysis of other labs' data and nm sentences over 125 characters.
- Inia araguaiaensis click frequency (PeerJ 7: e6670 and 11105): species status unclear and opportunistic wild recordings.
- Walleye (PeerJ e21156) and bat ultrasonic stimuli (PeerJ e21231): client error from peerj.com.
- Fire ant sensilla basiconica (Insects 17(2): 129), Anoplophora Elaeagnus volatiles (Insects 17(7): 666), Anthrenus verbasci (Sci Rep 2025), seabream hypoxia olfaction (JEB 249771), harbour seal vortex rings (JEB 249258), euglossine EAG, Chelostoma floral cues, honey bee taste (Frontiers fevo 2021): host blocked; open leads for a unit with access.
- Already on main: Stygoparnus excluded; slipper lobsters, armadillo ABR, Daubenton's bat, Trabala, sea turtle colour, boute pulsed fields, Bemisia/Serangium, raptor FVEP not filed (pooled).

## Advice
Main is saturated for PeerJ items that web searches surface; Crossref title queries (query.title=) over prefix 10.7717 returned the least noise but are rate limited. Species-level nulls and single-species behavioural choice tests with short results sentences are the fileable ones.

## Owner questions
- Dryopidae for Stygoparnus is inferred from the title word "dryopid"; the page does not print the family. Cyprinidae for Pimephales is from the species list on main.
- Pimephales copper avoidance is behavioural avoidance of a dissolved metal; say if that should count as sense_chemical.
