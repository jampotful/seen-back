# desk-d572 progress

Angle: pupil_shape from Pensoft species descriptions (Herpetozoa, ZooKeys, Zoosystematics and Evolution) that print the pupil in the holotype text; the OLD-ANGLE paragraph of the brief was ignored. 9 records (docs/views/evidence/desk-d572.jsonl), trait pupil_shape, no evidence_kind (as d571; not a sense_* trait). check.py: 0 problems (plain, and --require-evidence-kind on the new file). 39 WebSearches. No Crossref, no proxy hosts, WebFetch only on URLs from my own search results.

## Open question for the desk
pupil_shape is not in the TRAITS list of tools/senses/check.py although main holds about 1700 rows under it. check.py accepts it only when the note says "new trait"; every record carries that declaration with the reason (same route as d571). If the desk wants the key rejected, hold all nine.

## Filed (one holotype sentence per species, whole sentence, 2 to 37 words)
- Gekko tesselatus (ZSE 101(4): 2221-2242, 10.3897/zse.101.175246): vertical with crenulated edges.
- Charadrahyla viruela (Herpetozoa 39: 49-79, 10.3897/herpetozoa.39.e184954; Amphibia, ASW page): horizontal.
- Cnemaspis vangoghi and Cnemaspis sathuragiriensis (ZooKeys 1196: 209-242, 10.3897/zookeys.1196.117947): round.
- Cyrtodactylus makwanpurgadhiensis and Cyrtodactylus chure (ZooKeys 1253: 131-160, 10.3897/zookeys.1253.161933): vertical, crenulated margins.
- Trimeresurus nujiang (ZSE 101(4): 1653-1668, 10.3897/zse.101.162424): vertically elliptic.
- Trimeresurus lii (ZSE 102(1): 285-302, 10.3897/zse.102.178601): vertically elliptical.
- Hemiphyllodactylus ziegleri (ZooKeys 1268: 75-94, 10.3897/zookeys.1268.174678): vertical.
Main grep (whole docs/ tree) found no pupil_shape row for these species or DOIs; eight of the nine species already have eye_diameter_mm rows from the same papers (Charadrahyla viruela has none on main). Reptile Database pages (reptiles) and the ASW page (Charadrahyla) opened from own search results; none prints an explicit "valid".

## Per-paper search that reached the full text (unfiltered WebSearch strings are also in each note)
- Gekko tesselatus: "Gekko tesselatus new rock-dwelling gecko Sichuan Japonigekko pupil holotype description Zoosystematics and Evolution"
- Charadrahyla viruela: "\"A new treefrog of the genus Charadrahyla (Anura, Hylidae) from Oaxaca, Mexico\" Charadrahyla viruela herpetozoa article preview"
- Cnemaspis vangoghi / sathuragiriensis: "\"Two new species of the Cnemaspis galaxia complex\" Cnemaspis vangoghi Western Ghats ZooKeys article preview"
- Cyrtodactylus Nepal pair: "\"Description of two new species of Cyrtodactylus Gray, 1827 (Squamata, Gekkonidae) from Nepal\" Cyrtodactylus chure makwanpurgadhiensis ZooKeys article preview"
- Trimeresurus nujiang: "\"A new species of the genus Trimeresurus Lacépède, 1804 (Reptilia, Squamata, Viperidae) from Southwestern China\" Trimeresurus nujiang article preview"
- Trimeresurus lii: "\"A new species of the genus Trimeresurus\" \"western Sichuan Province, China\" Trimeresurus lii article preview"
- Hemiphyllodactylus ziegleri: "Hemiphyllodactylus ziegleri sp. nov. new karst-dwelling gecko Son La Province Vietnam ZooKeys article preview"
Method that worked: fig-page URLs from generic searches give only titles; a second search on the exact title plus "article preview" returns the article_preview.php URL.

## Weak spots
- All text came through the WebFetch page reader (about 125 characters per quoted fragment); sentences were joined from consecutive pieces and the reader's own word counts checked against check.py. The licence sentence was returned as start plus end words; the middle clause is the reader's paraphrase (noted in each record).
- Holotype text does not say whether the pupil is described live or preserved; stated in conditions.
- Species validity: neither the Reptile Database nor ASW prints "valid".

## Read, not filed
- Cyrtodactylus luci (ZooKeys 1192): pupil sentences run far over 40 words.
- Boulenophrys yezhongensis (Herpetozoa 38: 117): holotype sentence 80 words.
- Cnemaspis enneaporus (ZooKeys 1226): 169-word sentence. Cyrtodactylus arnei (ZooKeys 1253: 195): about 370 words. Cyrtodactylus khlonghatensis (ZooKeys 1211): 324 words. Hemiphyllodactylus venkatadri (Herpetozoa 38: 333): 118 words.
- No pupil printed: Cyrtodactylus sungaiupe/wangkhramensis (ZooKeys 1179), Cyrtodactylus peninsularis (ZooKeys 1241), Hyloscirtus (ZooKeys 1141), Protobothrops flavirostris (Herpetozoa 38: 43), Noblella madreselva (ZooKeys 516), Pristimantis ashaninka (iris only).
- Cnemaspis gituen: Zootaxa. Plazi pages are redirect stubs; not used.
- Unchecked leads: Boulenophrys youran, nebulosa, changyangensis; Cyrtodactylus awalriyantoi (ZooKeys 98724, only fig pages reached); Gekko alpinus (unresolved per brief).

## Desk disposition after audits 1120, 1121 (3 November 2026)
All 9 lines merged with the auditors' replacement text. Values, quotes, names, citations and DOIs were correct on every line, no line repeats main (eight species have eye_diameter_mm rows from the same papers, a different trait; the nujiang eye_diameter_mm row quotes the same sentence), and the CC BY 4.0 sentence was read verbatim on each paper's own copy. Faults fixed on all nine records: incomplete heading paths, missing or wrong preservation and paratype details (Charadrahyla viruela prints n = 6 but lists seven), nujiang's wrong "male only" claim, ziegleri's holotype code not as printed, and no verified licence sentence in the notes. 9 of 9 counted as errors; all fixed.
