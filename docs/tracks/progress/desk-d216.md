# desk-d216 progress

Scope: animal sensory-trait records from open full text (PeerJ CC BY, PLOS ONE CC BY). Records are in docs/views/evidence/desk-d216.jsonl; check.py reports 0 problems for the unit. Species and DOI were checked against origin/main (evidence, audit/ALL, audit/corrected, progress notes) before opening each paper.

## Records
- Scylla paramamosain (mud crab), PeerJ 9: e11248, two records from the same two abstract sentences: sense_chemical and sense_touch (appendage map from ECG and behaviour; sugarcane juice the only chemical stimulus).
- Trabala vishnou (subspecies gigantina), PeerJ 13: e20124, sense_chemical: Table 3 row, female relative EAG response to hexyl 2-methyl butyrate 0.33 to 2.53 across five concentrations.
- Ateles geoffroyi (spider monkey), PLoS ONE 8(11): e80621, sense_chemical: predator-odour thresholds at or below 1 ppb gas phase (group threshold, four animals).
- Platydoras armatulus (striped Raphael catfish), PLoS ONE 6(10): e26479, sense_hearing: best hearing at 0.5 and 1 kHz at 22 and 30 C (thresholds sit in Table 3, not read).
- Cyprinella venusta (blacktail shiner), PLoS ONE 10(9): e0137290, sense_hearing: control AEP thresholds 85 dB at 300 Hz and 82 dB at 400 Hz. The page summary printed no licence line; Crossref registers CC BY 4.0 (flagged in the note).
- Megalechis thoracata (armoured catfish), PLoS ONE 10(3): e0121219, sense_hearing: best sensitivities 0.2 to 1 kHz in both sexes; sex difference (females better 0.1 to 1 kHz) recorded in conditions.

## How the search went
- Crossref free-text queries returned mostly noise (human audiology) and were often rate limited; WebSearch with allowed_domains (peerj.com, journals.plos.org, mdpi.com, biomedcentral.com) surfaced real animal papers and worked better.
- The page-summary tool caps verbatim quotes at 125 characters, so only short whole sentences or table rows could be filed.
- journals.biologists.com and cob.silverchair.com returned PROVENANCE_REQUIRED (permission unanswered) for every JEB lead tried: frogs (jeb.246150), Podarcis (jeb.249422). Do not retry; JEB leads need another unit or a different route.

## Held out
- Grass carp and common carp pulsed DC (PeerJ 12: e17962, Miller et al.): only short usable sentence ('At field strengths higher than 0.4 V/cm both cyprinid species exhibited unvolitional tetany') covers two species together; pooled, not filed.
- PeerJ 3595 (ERG model selection): velvet worm Principapillatus hitoyensis lambda_max 484 nm is a reanalysis of Beckmann 2015 data with two model values (481 and 484) and no animal numbers; method paper, not filed.
- Tigriopus japonicus phototaxis (JEMBE 518: 151183): repository copy is CC-BY-NC-ND.
- Not opened (PLOS fetches rate limited repeatedly): Asian and African cichlid swim bladder and hearing (pone.0042292), Intermittent noise stress in a coastal marine fish (pone.0139157, not a sensory trait lead).
- Already on main, skipped: Betta splendens, Dicentrarchus labrax, Tiliqua rugosa, Xiphophorus hellerii, Euxesta eluta, Epinephelus awoara, Amblyomma americanum ticks (PLoS ONE 14: e0221659, in audit/corrected), Electrogena lateralis, Canis familiaris magnet (peerj.6117), Sminthopsis, walleye (Keyler 2026, still unfiled in evidence).

## Owner questions
- Scylla paramamosain, Trabala vishnou, Ateles geoffroyi and Platydoras armatulus are not in docs/views/gaps/gbif-names.tsv; names could not be checked against GBIF or WoRMS (refused). All four are the names printed in the papers.
- Trabala vishnou record is at species rank for the subspecies gigantina; say if subspecies-level taxa are wanted instead.
- Scylla paramamosain: two traits from one pair of sentences (chemical, touch); say if one record is preferred.

## Desk disposition after audit 301

Audit 301 (all 7 records): 6 of 7 in error (85.7%), 7 faults, all fixable and corrected with the auditor's replacement text: Scylla lines 1 and 2 (the "63 attempts" were feeding videos, not ECG attempts; the antennae's lack of chemosensitivity rests on cauterised antennules), Trabala (response at 50 and 100 ug/uL did not differ for one compound, so no "not a saturation point"), Ateles (predator-odour framing), Platydoras (the two 22 C audiograms differed, an order confound), Cyprinella ("a separate set of fish" is not in the paper). Line 7 merged with uncounted fixes. Pooled audits 172 to 301: 305 of 701 (43.5%). All seven records merged.

Owner questions: names absent from gbif-names.tsv (Scylla paramamosain, Portunidae; Trabala vishnou, Lasiocampidae; Ateles geoffroyi, Atelidae; Platydoras armatulus, Doradidae; Cyprinella venusta, Leuciscidae), none GBIF-checked; subspecies convention (Trabala vishnou gigantina filed at species rank with the subspecies in conditions, matching main's Gallus and Coturnix rows, while main also has subspecies-rank rows); Megalechis thoracata changed meaning in 2005 (the former M. thoracata is now M. picta) and the paper does not say which usage its fish follow; Scylla kept as two records, one per trait.
