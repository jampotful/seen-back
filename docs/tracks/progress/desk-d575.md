# desk-d575 progress

Angle: sensory_anatomy (tympanum) from Pensoft new-species descriptions (OLD-ANGLE paragraph ignored). 10 records (log docs/views/evidence/desk-d575.jsonl), trait sensory_anatomy, structure tympanum, evidence_kind anatomical_measurement. check.py: 0 problems (plain and --require-evidence-kind). About 40 WebSearches; no Crossref, no proxy hosts, every WebFetch URL came from my own search results.

## Filed (all CC BY 4.0 sentence read on the Pensoft/ARPHA article_preview page; ASW species page opened)
- Gephyromantis marokoroko, ZSE 97(2): 483-495 (10.3897/zse.97.73630): holotype KU 343230, whole sentence "Tympanic annulus distinct and round, small, TD 64.5% of ED; ..." and Table 2 TD row (holotype 2.5 mm). Search: "A fantastic new species of secretive forest frog discovered from forest fragments near Andasibe, Madagascar" Zoosystematics and Evolution 97 article preview.
- Gephyromantis lomorina, ZSE 94(2): 247-261 (10.3897/zse.94.21037): holotype ZSM 419/2016, sentence "Tympanum distinct, fairly small, 53% of eye diameter." and Table 1 holotype row (TD 2.1 mm). Search: the exact title "A distinctive new frog species (Anura, Mantellidae) supports the biogeographic linkage ..." plus Zoosystematics and Evolution.
- Pristimantis asimus, ZSE 100(2): 565-582 (10.3897/zse.100.119143): holotype MUSM 41241, whole tympanum sentence (membrane length slightly less than half eye diameter) and Table 1 row (TD 1.9 mm). Search: exact title "Similar looking sisters: ..." plus Zoosystematics and Evolution article preview.
- Litoria hastula, Vertebrate Zoology 73: 127-139 (10.3897/vz.73.e91111): holotype MZB Amph.32873, whole sentence (tympanum less than half eye diameter, TYM/EYE 0.35) and Table 1 TYM row (1.4 mm). Search: "Litoria hastula new species New Guinea Oliver Iskandar Richards Vertebrate Zoology 73 article preview".
- Gephyromantis fiharimpe and G. oelkrugi, Vertebrate Zoology 72: 271-309 (10.3897/vz.72.e78830): holotype rows of Table 1 (HTD 1.7 and 2.3 mm). Search: "Integrative taxonomic revision Gephyromantis malagasius archival DNA four new Malagasy mantellid frogs Vertebrate Zoology 72 article preview ...".

## Weak spots
- All text came through the WebFetch page reader (about 125 characters per quote); sentences and table rows are reassembled from pieces, column mappings are the reader's cell-by-cell reading. Sentence boundaries were checked by asking for the 125 characters before and after (marokoroko, lomorina, hastula).
- Vences 2022: Methods say "horizontal tympanum diameter (TD)", Table 1 column is HTD; Table 1 sits under the heading "Gephyromantis horridus > Note".
- Litoria hastula: ASW lists the species under Litoria (opened) and under Amnihyla (provisional transfer 27 June 2025); filed under the paper's name; family Pelodryadidae as printed.
- Pristimantis asimus: family Craugastoridae from the ASW URL path; paper prints Strabomantidae.

## Not filed and why
- Pristimantis prometeii (ZooKeys 606): ASW lists it as a synonym of P. hampatusami.
- Gephyromantis matsilo (same Vences paper): text says tympanum 77% of eye diameter, table HTD/ED is 1.7/3.4 (about 50%); text and table disagree. G. portonae: no ASW species page reached.
- Stumpffia froschaueri (ZooKeys 933: 139-164, CC BY): sentence and Table 1 TD 1.1 mm were read, but no ASW species page reached; lead.
- Odorrana yangi (ZooKeys 1275): ED already on main (d457); species not refiled.
- Scincella ngati (ZooKeys 1275: 275-298): diagnosis says external ear opening without lobules, holotype description says indistinct lobules; skipped. Sphenomorphus lingnanensis: reader returned no holotype description.
- Boulenophrys anlongensis (on main, d490), Zhangixalus thaoae (d513), Leptobrachella deocaensis (d457), L. yachangensis (d480): already used by other units.
- Noblella madreselva (ZooKeys 516): named in d572 progress, not re-checked.
- Zobodat PDFs surfaced in search were used only to find titles (third-party copies, not cited).

## Desk disposition after audits 1125, 1126 (4 November 2026)
Nine of ten lines merged with the auditors' replacement text; line 8 (Litoria hastula Table 1 TYM row, 1.4 mm) dropped: audit 1126 found the cell repeats the sentence record's ratio (1.4 / 4 = 0.35). Audit 1125 ruled the paired sentence and table records for marokoroko, lomorina and asimus to be different quantities (a share of eye diameter versus a holotype millimetre value), not duplicates and not pooled. Faults fixed: paratypes and preservation missing on all lines, holotype sex missing, ratios stored as text rather than a number as main does, the unflagged 64.5% (text) versus 65.8% (Table 2) for marokoroko, a misspelled caliper brand, missing "Results >" in a heading path, paraphrased preservation, and the taxon name, which becomes Amnihyla hastula (the current ASW name; the paper uses Litoria hastula). 10 of 10 counted as errors (8 fixable and merged, 1 fixable and merged by 1126 as line 7, 1 dropped).
