# desk-d44: rework set and queue batch 35 (plant)

Branch research/desk-d44. WebSearch and WebFetch only (OpenAlex 403; POWO, PMC, archive.org pages mostly refused). None of these genera is in a harvest run, so every query is a labelled "web: " line and `chased` is "none: ..." where the family photoreceptor-review search returned only general reviews (Helenium uses the Asteraceae review 10.1007/s44372-025-00446-3, as audited for d42).

## Rework set (audit 132 drops)
- Menyanthes sense_light_nonvisual: Martz et al. 2009 (UVB exclusion, 10.1016/j.envpol.2009.06.022) has no abstract sentence of 125 characters or fewer; wanted line, no null.
- Hieracium sense_chemical: Di Gristina et al. 2020 abstract names three taxa and says GA3 tests gave "similar" germination (no response); POWO status of the taxa could not be checked (POWO fetch refused); wanted line, no genus-level record. Hieracium lucidum (PeerJ 2024, 10.7717/peerj.16839) has no GA3 or light comparison in its abstract.
- Echinochloa diel and Schizachyrium diel: archive.org biostor-137766 still unreadable (permission unanswered); wanted line. Other anthesis searches returned nothing for either genus.
- Tribulus diel: evidence (Suvarna Raju and Solomon Raju 2023, flowers open 0600 to 0800 h). Tribulus sense_chemical and sense_light_nonvisual stay on the existing wanted lines (Vietnamese papers; hcmue 4010 reports a 20 h photoperiod with 97% in vitro germination, abstract in Vietnamese only).
- Mimosa diel: evidence filed under Mimosa setosa (the thesis writes M. paludosa; POWO accepts M. setosa; the variety could not be confirmed).

## Batch 35
Done: Carpobrotus, Helenium, Nuphar, Pistacia, Alisma, Bunias, Ipomopsis.
Skipped (search records with web queries or evidence on all open cells): Uvularia. Not reached: Alloberberis, Epifagus, Marah, Adelinia, Chlorogalum, Malus (eye_type only), Gymnadenia (eye, light) and everything from batch 36.

## Evidence (6 lines)
Tribulus terrestris diel; Mimosa setosa diel; Carpobrotus edulis light (Podda 2018); Helenium light (company guide, genus level, grade g); Pistacia khinjuk GA3 (Acar 2017); Alisma plantago-aquatica diel (Vislobokov 2022).

## Leads (no null written)
Nuphar diel (Schneider and Moore 1977), Pistacia lentiscus light (Luis Diaz 2009), Ipomopsis floral scent (Bischoff 2013, Wu 2023), Menyanthes, Hieracium, biostor-137766 as above.

## Desk disposition after audit 134
Audit 134 failed the unit (3 errors in 22 records). Dropped: search line 1 (Carpobrotus chemical, missed a herbivore-induced defence response) and line 6 (Nuphar chemical, missed a GA3 trial on Nuphar variegata); evidence line 2 (Mimosa setosa quote was part of a longer sentence). Kept: 5 evidence, 14 search, 7 wanted. Carpobrotus and Nuphar chemical cells are open again.
