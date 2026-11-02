# desk-d197 progress

Unit brief task (plant screening) was superseded: animal sensory-trait records from open-access papers.

Records filed: 6 in docs/views/evidence/desk-d197.jsonl
- Portunus trituberculatus x2 (behaviour_vision, shelter colour choice and abandonment; Zhang et al. 2022, Fishes 7(5): 296). Limits carried: night-time null, no light intensity, colour and brightness not separated, authors say the choice does not prove colour vision.
- Bombus terrestris x2 (sense_chemical; EAG dose trend and Y-tube concentration dependence; He et al. 2025, Biology 14(11): 1570).
- Aphis gossypii x2 (sense_chemical; 16 of 31 compounds EAG-active, 14 repellent in Y-tube; Bian et al. 2025, Front Plant Sci 16: 1563752).

Held, not filed
- Petromyzon marinus review (Beausejour et al., Animals 15(14): 2012): the only whole sentences returned were body mass and spawning interval, not sensory values; licence line not returned.
- Epinephelus awoara ABR (Zhu et al. 2023): already on main (desk-d160).
- Ferrando et al. 2019 (Front Physiol 10: 245, 14 chondrichthyan olfactory organs): the abstract and Results range sentences exceed the fetch quoting length and Table 2 came back flattened, so no whole row; unfiled.
- Asiophrida xanthospilota (Insects 15(7): 532) and Xiphophorus hellerii acuity: already on main.
- Larimichthys crocea otolith (Zool Stud 60: 64): modelled, no licence line. Philippine bats echolocation (Phil J Sci 150(6B)): no DOI or licence. Varroa destructor papers: restricted or no licence on the copy read. Scylla paramamosain and Litopenaeus vannamei light papers: growth/colour effects, not sensory. Eriocheir sinensis personality (Animals 15(5): 757): behavioural personality, sentence over limit.

Refusals/limits: WebFetch PROVENANCE_REQUIRED for api.inaturalist.org (no retry). Quotes under about 125 characters only; long sentences were not filed. WebSearch used: 26 of 40.

## Desk disposition after audit 281

Audit 281: 4 of 6 records in error (66.7%; lines 1 to 4), none unfixable. Pooled audits 172 to 281: 252 of 596 (42.3%). All six merged with the auditor's replacement text; line 5 carries the suggested conditions addition.

- Portunus line 1 quote is now the 18-word part of a 46-word sentence with the cut marked; both Portunus rows state that Day 2 is the period with an intruder crab (alone, Day 1, colour had no effect) and that abandonment is counted per in-shelter encounter.
- Bombus line 3 states the six EAG-active compounds and dose range; line 4 carries the Results-level attract/repel pattern, which differs from the abstract.
- The unit's progress note still applies the abolished 125-character limit.

Owner questions: how to word an EAG result when the paper does not say whether "significant" is against the solvent control or across doses; whether Aphis gossypii and Portunus trituberculatus should go into taxonomy-extra.tsv (neither is in gbif-names.tsv).
