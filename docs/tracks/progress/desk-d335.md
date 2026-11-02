# desk-d335 progress

Angle: eye/ocelli statements in page-printed CC BY taxonomy papers for myriapods, scorpions, pseudoscorpions, Opiliones, Palpigradi/Diplura/Protura, cave beetles. 4 records filed (target 10 missed); about 40 WebSearch/WebFetch calls. check.py: no problems reported.

## Filed (docs/views/evidence/desk-d335.jsonl)

| Species | DOI | Trait | Value |
|---|---|---|---|
| Sphaeropoeus honbaensis | 10.3897/zookeys.930.47742 | sensory_anatomy / anatomical_measurement | ca. 65 ocelli per eye |
| Sphaeropoeus bidoupensis | 10.3897/zookeys.930.47742 | same | ca. 65 ocelli per eye |
| Sphaerobelum pumatense | 10.3897/zookeys.930.47742 | same | >75 ommatidia per eye |
| Scorpiops krachan | 10.3897/zookeys.1193.113398 | eyes_count | 3 pairs lateral eyes |

## Weak spots

- Quotes came through WebFetch summaries (pieces joined), not read on the page; the three Vietnam lines are telegraphic ("Head: eyes with ca. 65 ocelli.").
- No registry reached (MilliBase, Scorpion Files); names rest on being new species in the cited papers. Scorpiops (Euscorpiops) placement is unsettled.
- The two Sphaeropoeus values are identical and approximate; the Description covers both sexes, not the holotype alone.
- ommatidia_count is not in check.py TRAITS, so the millipede counts went under sensory_anatomy.
- The scorpion line states the median eyes without a count.

## Not filed

- On main: Euscorpiops lii (eye_type), Lithobius hualongensis, sui, varioporus, Geopselaphus bullonorum, Wanoblemus/Shenoblemus/Jujiroa (ZooKeys 923), Allochthonius bainiensis/pandus/xinqiaoensis, Spelaeochthonius wulibeiensis, Acherontiella nezamdoosti.
- No eye statement in the text read: Symphylella macropora/zhongi (ZooKeys 845), Scolopendrellopsis glabrus (789), Paratachycampa daidarabotchi/nipponica (SB 27), Glomeridesmus siamensis (1024), Scolopocryptops miyosii/brevisulcatus (EJT 908; genus blind in intro only).
- Mesomexovis caxcan (ZooKeys 1243.146978): lateral eye sentence too long to return whole; description covers type and paratypes.
- Scorpiops zhui (Zootaxa), Chthonius kirghisicus (Plazi redirect only), Palpigradi leads (Zootaxa/Plazi; SB 202620 not opened).

## Desk disposition after audit 450 (2 November 2026)
Audit 450: 1 of 4 in error, fixable. Scorpiops krachan refiled as Euscorpiops krachan under eye_type (median eye count not stated; lateral pairs do not belong in eyes_count). Lines 1 to 3 moved from sensory_anatomy to ommatidia_count, author initials corrected (Semenyuk I), type-series and licence notes applied. Merged 4 of 4. Names remain unchecked in MilliBase.
