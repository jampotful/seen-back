# desk-d615 progress

Angle: amphibian new-species papers in European Journal of Taxonomy, Journal of Threatened Taxa, Zoological Research, Asian Herpetological Research and Check List with ED in the Methods and an ED table row. Trait eye_diameter_mm, evidence_kind anatomical_measurement. 48 records in docs/views/evidence/desk-d615.jsonl. check.py: 0 problems (plain and --require-evidence-kind). About 38 WebSearches.

## Filed (ASW species page opened from my own search results for each)
- Eur J Taxon 451: 1-20 (10.5852/ejt.2018.451), Lehtinen et al. 2018, CC BY 3.0 sentence: Guibemantis albomaculatus (15 specimens, whole Table 1 rows) and G. woosteri (14 specimens). Methods list 'ED = horizontal eye diameter'. 29 records. Reached by search 'Two new Pandanus frogs (Guibemantis: Mantellidae: Anura) from northern Madagascar' (EJT download 582/1329).
- Eur J Taxon 989: 189-214 (10.5852/ejt.2025.989.2893), Hofmann et al. 2025, CC BY 4.0 sentence: Scutiger khumbu, holotype and 18 paratype rows of Table 3 (ED column; rows cut after ED with a marked cut). Methods 'ED = horizontal diameter of eye'. 19 records. Reached by search 'Resolving taxonomic ambiguities in extant Himalayan lazy toads: A new species of the genus Scutiger ... European Journal of Taxonomy' (download 2893/13119).

## Weak spots
- All text came through the WebFetch page reader on EJT PDF downloads; row and column mapping is the reader's cell reading (two to three separate reads agreed on every ED value). Scutiger Table 3 is a 38-column multi-species table; the N and E cells are blank for the khumbu rows. The Table 3 unit comes from the Methods caliper sentence.
- Guibemantis header prints W4TD where Methods define W4FD (noted in the records). ED is the eleventh numeric cell.
- S. khumbu makalu (two rows) and Guibemantis albolineatus rows not filed.

## Not filed and why
- Already on main: Theloderma khoii, Pseudopaludicola coracoralinae, Physalaemus araxa, Odontophrynus toledoi, Pristimantis flavus/fouqueti, Adenomera guarani, Raorchestes ghatei (desk-d332), Phyllodytes gravata (d584, other trait).
- EL not ED: Microhyla hmongorum/xodangorum, Pristimantis jamescameroni/imthurni (EJT 60), Sphaerotheca pashchima (JoTT), Indirana chiravasi (JoTT). Pristimantis Paria five species (JoTT 7(4)): Methods define neither ED nor EL, measurement printed as EYE.
- No ASW species page reached: Platypelis ravus (now Cophyla ravus; ASW genus page lists no species names). Table text not returned: Pseudophilautus dilmah (ED defined, table missing from reader text), Nyctibatrachus mewasinghi (EL). Pseudophilautus conniffae (JoTT 11(1)): Methods print no ED definition, not filed.
- Zoological Research (Amolops chaochin, Amolops from Yunnan and Myanmar): pages print no Creative Commons sentence, bodies not returned; Myanmar page gave a security verification page. Not retried.
- Asian Herpetological Research: search with allowed_domains returned no links. Check List: only distribution records returned, no new-species descriptions.
- One WebFetch (EJT view 450/0, Pristimantis from Yanachaga) was refused by the classifier and not retried.
- Non-amphibian EJT hits (tardigrades, snails, beetles) fetched by mistake from title-less search results: EJT 1043, 1055, 1007, 947.

## Desk disposition after audits 1238 to 1243 (4 November 2026)
48 eye_diameter_mm records filed, 44 merged, 4 counted errors (Guibemantis woosteri lines 24 to 27). Held out (4): UMMZ 191339, 191340, 191343 and 191344, the Ambatovaky referred specimens that the paper assigns to G. woosteri only "possibly" and "tentatively", pending confirmation by molecular data (the unit filed them as the species with no qualifier). Under the rule that taxon-ambiguous rows are dropped they are not merged; the auditors' corrected text with the qualifier is saved in audit-1240 (line 24) and audit-1241 (lines 25 to 27). The other 44 records (Guibemantis albomaculatus 15, G. woosteri 10, Scutiger khumbu 19) had 0 value errors; wording faults (ASW citation paraphrased as a quote, curly apostrophe in d'Ambre, heading path and Class authority, paratype counts, Table 1 page range inside the albomaculatus account) were corrected. EJT 451 is CC BY 3.0 (sentence read whole); Scutiger khumbu CC BY 4.0; Table 3 prints no unit, so mm comes from the Methods caliper sentence. Owner question: keep or restore the four tentatively assigned G. woosteri rows with the qualifier. Not filed: Scutiger khumbu makalu (2 rows), Platypelis ravus (no ASW species page), Zoological Research Amolops pages (no CC sentence), EJT Pristimantis from Yanachaga (classifier refusal, not retried).
