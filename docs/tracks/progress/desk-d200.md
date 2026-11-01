# desk-d200

Task: animal sensory-trait records from open-access papers (the plant-screening task in the unit brief is superseded). 6 records filed in docs/views/evidence/desk-d200.jsonl from 3 papers. WebSearch used: 19 of 40.

## Filed
- Diaphorina citri (3): Paris et al. 2017, Insects 8(3): 88. Walking distance toward UV/blue light; polarized vs unpolarized 405 nm (greater, no plane effect); polarized vs unpolarized 500 nm (null). Quotes are Abstract sentences read whole twice. Intensity not matched across wavelengths.
- Amblyomma americanum and Ixodes scapularis (2): Otalora-Luna et al. 2022, Insects 13(2): 130. Flying T choice with a 32 C Peltier element, n = 30 per stage and sex per species; shared Discussion sentence; Peltier gives infrared and convective heat together.
- Pogona vitticeps (1): Nishimura 2020, Animals 10(3): 489. Tail-lift response to an extremely low frequency EMF with a 380 nm cut-off filter; electric and magnetic components not separated; 8 lizards.

## Held out
- Pelteobagrus fulvidraco (Zou et al. 2024, Animals 14(1583)): usable whole sentences, but the Catalog of Fishes page lists fulvidraco as a synonym of Tachysurus sinensis (Cheng et al. 2021) and no other authority was reachable, so the name is unsettled.
- Echolocation of four Vietnamese bats (Pham et al. 2021, Diversity 13(1): 18): values only in Table 2 rows and Discussion sentences over 40 words or over what the fetch returns whole.
- Gonatus onyx (Vision 8(2): 26), Pholidobolus montium (Animals 11(11): 3022), Lucilia cuprina/Chrysomya rufifacies (Insects 17(3): 283, no white control, inconsistent counts): result sentences too long to read whole.
- PeerJ 21156 (walleye): fetch failed (client_error).
- Vespula/Vespa (Animals 14(11): 1543) already on main.

## Desk disposition after audit 284

Audit 284: 4 of 6 records in error (66.7%; lines 1, 4, 5, 6), none unfixable. Pooled audits 172 to 284: 262 of 612 (42.8%). All six merged with the auditor's replacement text and suggested additions.

- Diaphorina line 1 note corrected: the authors argue the response followed wavelength, not intensity (brighter long-wavelength targets drew no response above darkness). Ticks: the servosphere test used an infrared LED to which both species oriented, and I. scapularis females oriented to it, so the Peltier null is stated for the flying T only; the printed male statistic (z = 1.64, p < 0.010) is flagged as inconsistent. Pogona: exposure was 11 h a day for 5 days.

Owner questions: whether the sex-specific tick "attracted" claim rests on an inconsistent statistic and should be limited to females and nymphs; whether heat from a Peltier (infrared plus convection) takes sense_thermal or sense_infrared (main files Carr and Salgado's heated plate under sense_infrared); whether sense_magnetic suits an extremely low frequency field with unseparated electric and magnetic parts; whether Pogona vitticeps goes into taxonomy-extra.tsv.
