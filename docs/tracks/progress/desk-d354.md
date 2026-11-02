# desk-d354 progress

Angle: Pensoft amphibian/reptile/mammal/marine-invertebrate new-species papers with sensory statements. 3 records filed (target 10), about 38 WebSearch/WebFetch calls. check.py: 0 problems on the new file.

## Filed (docs/views/evidence/desk-d354.jsonl)
- Phrynobatrachus bibita (ZooKeys 824: 53-70, 10.3897/zookeys.824.31570), male holotype SB440: "Tympanum not visible." and "Pupil horizontal." (two sensory_anatomy/anatomical_presence records).
- Pristimantis ashaninka (ZooKeys 645: 85-102, 10.3897/zookeys.645.11221), female holotype MUSM 36517: head sentence with one marked cut, "tympanic membrane and annulus absent".

## Weak spots
- Registry: ASW page not opened (AmphibiaWeb gave a robot check; not worked around). P. bibita family from the ASW URL path in a search result; P. ashaninka family unchecked (paper prints Craugastoridae, Strabomantidae filed; main has both for Pristimantis).
- The XML citation line of the bibita paper prints 2010; 2019 filed (publication-date metadata).
- Pupil shape filed under sensory_anatomy (no pupil key in check.py TRAITS).

## Not filed
- Eusirus carolinus (Zoosystematics and Evolution 100(2): 645-662, 10.3897/zse.100.114758): only the abstract "large, well-pigmented eyes" reachable; full text fetch blocked by permission and abstract not reproducible verbatim. Lead.
- Pristimantis milpe (ZooKeys 1286: 121-152, 10.3897/zookeys.1286.194383): the XML fetch never returned the species Description or Diagnosis. Lead.
- Nereis tricirrata (10.3897/zookeys.1134.94198) and Anguillosyllis: already on main (desk-d284).
- Xenophrys tongbiguanensis: Zenodo copy is CC0 (third-party copy); journal page not opened. Plazi pages redirect-only and unusable.
- Crossref list query failed (rate limit, then client error).

## Desk disposition after audit 468 (2 November 2026)

Audit 468 found 1 of 3 records in error (33%), fixable: the Pristimantis ashaninka note wrongly said main files P. achupalla under Strabomantidae and rested the family on memory; Strabomantidae is the registry family. Printed year 2019 confirmed for P. bibita (2010 is a citation-line typo). The ASW pages and Crossref did not open for the auditor. Replacement lines merged; check.py 0 problems.
