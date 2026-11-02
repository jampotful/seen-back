# desk-d344 progress

evidence_intake: evidence-kind-v2; intake_base: HEAD of research/desk-d344 at launch (9c8b219e0, after the d341 merge).

Angle: hydrobiology and bird/mammal OA papers with per-species sensory measurements in running text. 8 records filed (target 10), about 33 WebSearch/WebFetch calls. check.py: 0 problems for desk-d344.

## Filed (docs/views/evidence/desk-d344.jsonl)

All from PeerJ new-species descriptions (CC BY, page-printed licence sentence), one holotype per species, "Measurements of (the) holotype (in mm)" sentence:
- Pristimantis achupalla (10.7717/peerj.11878): ED 1.3 (eye_diameter_mm), TD 0.3 (sensory_anatomy, tympanum).
- Noblella thiuni (10.7717/peerj.6780): ED 1.5.
- Phasmahyla lisbella (10.7717/peerj.4900): ED 4.29, TD 1.61; quote cut with [...].
- Phrynopus remotum (10.7717/peerj.9433): ED 2.8.
- Leptodactylus apepyta (10.7717/peerj.7869): ED 5.70, TYD 4.00.

## Weak spots

- Registry check is thin: ASW page opened only for P. achupalla (valid, but family not printed in the text returned). The ASW pages for the other four species could not be opened (permission refused), AmphibiaWeb is behind a bot check; GBIF page for P. remotum only. Names and families (Craugastoridae vs Strabomantidae for Pristimantis, Phrynopus, Noblella) are flagged unchecked in each note.
- Abbreviations ED and TD are not expanded on the pages the tool returned for lisbella; inferred from percentage statements in the same description.
- Holotypes are single individuals, not species means; stated in conditions. Measurement side and instrument not read.
- Quotes for lisbella, remotum and apepyta were joined from two consecutive page-tool pieces; the auditor should confirm on the page.
- Phasmahyla and Phrynopus Crossref author lists were read; Crossref licence content-version is "unspecified" with the page-printed Creative Commons Attribution License sentence (accepted route).

## Not filed

- Odorrana kweichowensis (peerj.5695) and Allobates kamilae (peerj.13751): proportions only, no mm value.
- Shark and ray ampullary pore, lateral-line neuromast and marine mammal lens papers: searches and Crossref queries returned no OA PeerJ item with per-species values in running text; sawfish pore papers (JCU repository copies) are third-party copies.
- Not opened for lack of calls: peerj.14985 (Eleutherodactylus), peerj.9979 (Allobates), peerj.20930 and peerj.21618 (Pristimantis), peerj.20397 (Leptobrachium).
