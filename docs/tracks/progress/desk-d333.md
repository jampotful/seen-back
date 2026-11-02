# desk-d333 progress

Angle: arthropod groups d332 did not cover (Collembola, pseudoscorpions, Opiliones, Palpigradi, Diplura, millipedes, scorpions, cave beetles) in page-printed CC BY Pensoft and EJT articles. 4 records filed (target 12 missed); about 40 WebSearch/WebFetch calls used. check.py: 0 problems.

## Filed (docs/views/evidence/desk-d333.jsonl, trait eyes_count, same key as main's Coecobrya rows)

| Species | DOI | Value |
|---|---|---|
| Coecobrya urbana | 10.3897/subtbiol.49.120956 | 0 ("Eyes absent.") |
| Pygmarrhopalites sietae | 10.3897/subtbiol.49.120956 | 1+1, unpigmented |
| Acheroxenylla lipsae | 10.3897/subtbiol.34.50673 | 2+2 |
| Entomobrya virginiae | 10.3897/subtbiol.38.66254 | 8 (per side not stated) |

## Weak spots

- All four quotes were returned by WebFetch's summariser, not read on the page; they are telegraphic description lines (verb elided), whole lines but fragments in grammar.
- No registry checked for any of the four names (GBIF/WoRMS not reached); acceptance rests on being new species in the cited papers; Plazi lists P. sietae in a search result.
- Licence: page-printed CC BY 4.0 sentence returned for 120956; for 50673 and 66254 the tool reported CC BY 4.0 without the exact sentence. Auditor should confirm on the pages.
- Entomobrya virginiae: value 8 without "per side" in the line.

## Not filed

- Already on main (grep by species and DOI): Pseudosinella altamirensis (989.52361), P. hartnerae and huetheri (1063.73094), Acherontiella nezamdoosti (1255.164170), Wanoblemus huangshanicus (923.47322), Iandumoema smeagol (537.6073), Oncopodura moghanensis (49.118293), Spelaeochthonius yinae/Allochthonius lini (d289 declined clauses).
- Allochthonius lini and A. xuae (EJT 861.2065, 10.5852/ejt.2023.861.2065): only complete sentence is the Discussion "The two new species collected inside the cave still have well-developed eyes and are troglophiles."; qualitative, addlog refused sensory_anatomy without units, so held. The count (4 well-developed eyes) sits in a clause of a sentence beginning mid-description.
- Harmonicon cerberus (10.3897/zookeys.389.6693, spider): "In contrast, the AME of the new species bears a milky crystalline and no trace of a retina or pigmentation are visible behind it." Context of the contrast not read; not filed.
- Hou 2023 (zookeys.1153.99537) Tyrannochthonius capito/calvatus: eye statements are clauses. Taylor and Probert Waitomo harvestmen, Desmoxytes (185.3082), Illacme (626.9681), Protaphorura (620.9372), Eukoenenia (subtbiol 57.202620), Pacificampa (27.28575), Canary Diplura (34.50231): no eye sentence for a named species. Scorpion Mesomexovis paper (1243.146978): ocelli figure caption only.
- Folsomides cf. ayllonensis (5+5 eyes) skipped as "cf.".
