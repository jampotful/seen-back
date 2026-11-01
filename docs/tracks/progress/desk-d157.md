# desk-d157: plant cells (touch, thermal, magnetic, vibration)

Branch research/desk-d157. 7 records in docs/views/evidence/desk-d157.jsonl from 4 open CC BY papers; check.py: 0 problems.

## Filed
- Arabidopsis thaliana sense_vibration x2: Body et al. 2019, Front Plant Sci 10: 810, 10.3389/fpls.2019.00810 (hormones; volatiles).
- Arabidopsis thaliana sense_touch: Cazzonelli et al. 2014, Front Plant Sci 5: 533, 10.3389/fpls.2014.00533.
- Arabidopsis thaliana sense_thermal: Shao et al. 2021, Front Plant Sci 12: 753148, 10.3389/fpls.2021.753148.
- Solanum lycopersicum sense_magnetic; Lactuca sativa sense_magnetic x2 (300 mT germination, 45 mT length): Koukounaras et al. 2023, Seeds 2(4): 394-405, 10.3390/seeds2040030.

Names: Arabidopsis thaliana POWO 277970-1 accepted, WFO wfo-0000541830 accepted. Solanum lycopersicum POWO page 316947-2 accepted, WFO wfo-0001029216 accepted (2021-12 snapshot page). Lactuca sativa POWO 228239-1 accepted, WFO wfo-0000128816 accepted (2024-12). Arabidopsis already had touch/magnetic records; these species were chosen because both authorities could be opened, not because they are thin.

## Held out
- Gentianopsis paludosa sense_thermal, Hou et al. 2022 (10.1002/ece3.8490, CC BY 4.0, text read, abstract quote confirmed twice): POWO page would not open (client error, then blocked) and WFO status not reached. Hold until both open.
- Eruca sativa (Koukounaras 2023, rocket at 150 mT): name not checked; likely a synonym of Eruca vesicaria. Not filed.
- Triticum (Hindhaugh et al. 2021, Ann Bot 128(5): 589-603, 10.1093/aob/mcab070, CC BY): paper names only Triticum sp.; Methods do not name T. aestivum. Not filed.
- Dionaea muscipula touch (Suda et al. 2025, Nat Commun, 10.1038/s41467-025-63419-w): nature.com full text blocked; Crossref/abstract only through a RePEc page. Not filed.
- Lettuce thermodormancy and GA3 (J Seed Sci 2022, scielo.br): page shows only an "Open-access" label, no CC statement, no authors or DOI. Not filed.
- Appel and Cocroft 2014 (Oecologia 175: 1257-1266, Arabidopsis vibration): page says only "freely available", no named licence. Held.

## Notes
- Body 2019 volatile N was read as 24 in one fetch and 22 in another, so not carried. Hormone N = 12 sets of three plants.
- Cazzonelli article number 533 comes from the DOI and the Frontiers page; Crossref returned no article number.
- Plant diel and light_nonvisual cells not worked; WebFetch limits made quote assembly slow.

## Desk disposition after audit 242
Audit 242 judged 7 records: 5 errors (lines 1 to 5, all fixable). Lines 1 and 2 now carry the 2.5 mm/s peak amplitude and the airborne-sound caveat; line 2's value narrowed to 5% and 11% with 4 of 21 volatiles detectable and N = 24 per treatment. Lines 3 to 5 carry the cultivars ('Ace 55 VF', 'Paris Island'), the weak residual field in the control, and the tomato and lettuce contrary results (150 and 300 mT lowered tomato germination; lettuce germination not positively affected per the Conclusions). Line 6 licence wording set to CC BY without a version. Owner question raised: airborne sound as sense_vibration. WFO for Solanum lycopersicum read at the 2021-12 snapshot only. Merged 7 records.
