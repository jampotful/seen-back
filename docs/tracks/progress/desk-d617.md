# desk-d617 progress

Angle: reptile new-species papers in European Journal of Taxonomy and Journal of Threatened Taxa, 2015-2025, with ED defined in the Methods and a per-specimen table (Reptile Database authority). Trait eye_diameter_mm, evidence_kind anatomical_measurement. 7 records in docs/views/evidence/desk-d617.jsonl. check.py: 0 problems for this file (plain and --require-evidence-kind). About 40 WebSearches.

## Filed (Reptile Database species page opened from my own search results for each; neither prints an explicit 'valid')
- Eur J Taxon 930: 20-52 (10.5852/ejt.2024.930.2489), Idiiatullina et al. 2024, CC BY 4.0 sentence: Trimeresurus kraensis, holotype AUP-02036 and 3 paratypes, Table 4 row 'ED (mm)' (Methods 'ED = horizontal eye diameter'). 4 records. Reached by search 'Another new species of karst-associated pitviper (Serpentes, Viperidae: Trimeresurus) from the Isthmus of Kra, Peninsular Thailand' (download 2489/11117).
- Eur J Taxon 729: 54-73 (10.5852/ejt.2020.729.1191), Bhosale et al. 2020, CC BY 4.0 sentence: Pareas kaduri, three paratypes (BNHS 3575, NCBS BH655, NCBS BH656), Table 1 ED row (Methods 'ED = eye diameter, widest diameter of the eye'). 3 records. Reached by search 'A new species of snail-eating snakes of the genus Pareas Wagler, 1830 (Reptilia: Serpentes) from eastern Himalayas, India' (download 1191/3349).

## Weak spots
- Text came through the WebFetch page reader on EJT PDFs; table cells are the reader's reading (two reads agreed for both tables). The Pareas table came back jumbled, flagged in the notes; range and mean agree with the four values.
- Pareas kaduri holotype BNHS 3574 not filed: Table 1 ED 3.5 conflicts with the holotype description 'Eye large, circular, 3.13 mm' in the same paper. Unresolved; an auditor may decide whether to add the row.
- Pareas Table 1 prints no unit; mm comes from the Methods caliper sentence. Trimeresurus Table 4 row label prints (mm).

## Not filed and why (ED not an eye measure, or no per-specimen table)
- ED = ear diameter: Cyrtodactylus chungi (EJT 731), C. chumuensis and C. arndti (EJT 875). OD (orbit): Cyrtodactylus exercitus and C. siahaensis (EJT 794), Dravidogecko (horizontal orbit diameter, EJT 2125), Cnemaspis flaviventralis (JoTT 8(14)). EYE: Acanthosaura cuongi (EJT 976, no mm table).
- No ED defined or no eye mm column: Scincella honbaensis/auranticaudata (EJT 989), Liolaemus kulinko (EJT 890), Potamites hydroimperator (EJT 760), Anadia mcdiarmidi (2011, out of range), Uropelts rajendrani and Uropeltis jerdoni (JoTT, text only), Herpetoreas davidi (EJT 932: ED defined but only the holotype in text, no specimen table).
- Out of range (2026): Hemidactylus cairnicola/koyaorum (EJT 1102), Cyrtodactylus jayadityai (EJT 1048), Cyrtodactylus dimaensis (JoTT 18(10)).
- No open PDF reached: Goniurosaurus review (EJT 751; only a Frankfurt repository copy), Micrurus review.
- Already known dead: listed in the brief; not retried.
- JoTT reptile new-species papers returned by search were few and none defined ED with a specimen table.

## Desk disposition after audits (4 November 2026)
Audit 1245 judged all 7 lines: 1 counted error (line 3, paratype ZMMU Re-17665 printed "1 ♀ subadult", omitted by the record; fixed with the auditor's replacement text), plus uncounted faults (heading paths, type material as printed, ♀/♂ in Sex row quotes). 7 merged with the corrections. The Pareas kaduri holotype BNHS 3574 stays unfiled (Table 1 ED 3.5 vs text 3.13 mm), an owner question.
