# desk-d343 progress

Angle: morphometric tables in ichthyology and herpetology with an eye column. 8 records filed (target 10), about 40 WebSearch/WebFetch calls. check.py: 0 problems on desk-d343.

## Filed (docs/views/evidence/desk-d343.jsonl)

All rows come from Pensoft's own CSV export of the paper's table (returned by WebFetch), with the licence sentence read on the same article's article_preview page (ZooKeys, CC BY 4.0 except two CC0 papers).
- Johnius javaensis (ZooKeys 1259, 10.3897/zookeys.1259.160425): eye_diameter_mm holotype 6.5 (paratypes 5.1-7.0, n 4) and sensory_anatomy 18.9% of HL (sentence; paratypes 22.2-22.6%).
- Cyrtodactylus phnomchiensis (ZooKeys 926, CC0): EyeD holotype 5.1 mm.
- Cyrtodactylus peninsularis (ZooKeys 1241): ED holotype 7.0 mm.
- Hemiphyllodactylus lungcuensis (ZooKeys 1167, CC0): EyeD holotype 1.8 mm.
- Ranitomeya aquamarina (ZooKeys 1236): male mean 2.0 mm (n 7); holotype printed 1.0, flagged.
- Pristimantis pluvialis (ZooKeys 594): holotype 0.8 mm, unusually small, flagged.
- Pristimantis pulchridormientes (ZooKeys 610): male mean 2.6 mm (n 9).

## Weak spots

- Quotes are CSV rows, not page text; cells joined with spaces. Auditor should compare with the HTML table.
- Registry: Reptile Database header opened only for C. phnomchiensis; ASW pages opened for R. aquamarina and P. pulchridormientes; C. peninsularis, H. lungcuensis, P. pluvialis only appear as registry entries in search results; Eschmeyer shows J. javaensis reference without a status line.
- CC0 dedications on two papers (rule list names CC BY; auditor to rule). Licence wording for P. pluvialis and P. pulchridormientes is the tool's paraphrase.
- P. pulchridormientes row has no unit in the CSV; mm inferred. Holotype header-vs-type labelling in the H. lungcuensis CSV inferred from the text's holotype number.

## Not filed

- Cyrtodactylus zhenkangensis (ZooKeys 1021, 10.3897/zookeys.1021.60402): the table's ED is ear diameter, not eye.
- Pensoft zse CSV tables for article ids 139205, 56247, 146027, 176660 (fish with an eye diameter row): the zse article_preview returned another paper (Sphenomorphus lingnanensis, no eye data) for every id, so the species could not be identified. Same for CSV zookeys 7377, 11261, 67747, 84171, evolsyst 61667, 62661, herpetozoa 186246 (not opened).
- Sphenomorphus lingnanensis (zse 102): no eye measurement.
