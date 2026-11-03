# desk-d553 progress

Angle: sense_hearing as behavioural_response in wild vertebrates (playback and field studies). 9 records so far in docs/views/evidence/desk-d553.jsonl; check.py 0 problems (plain and --require-evidence-kind).

## Filed
- Melo, Both, Brasileiro 2024, Front Amphib Reptile Sci 2: 1457928 (10.3389/famrs.2024.1457928): Physalaemus cuvieri, 2 nulls (position/call continuity; calling rate). Search: "Melo Both Brasileiro "Novel sounds, native responses" Eleutherodactylus johnstonei invasion urban areas".
- Deshpande, van de Waal, Zuberbuhler 2023, Anim Cogn 26: 1199-1208 (10.1007/s10071-023-01767-0): Chlorocebus pygerythrus, 3 records. Search: "wild vervet OR baboon OR macaque OR lemur free-ranging responses to calls Scientific Reports Creative Commons" (springer pdf link in results).
- Baotic, Szipl 2025, Front Ecol Evol 13: 1634218 (10.3389/fevo.2025.1634218): Giraffa giraffa, 3 Table 4 rows. Search: "reptile playback experiment wild tortoise OR crocodile OR alligator OR lizard calls response field open access Frontiers" (pdf link in results).
- Chabert et al. 2015, Sci Rep 5: 15547 (10.1038/srep15547): Crocodylus niloticus wild playback, 1 record. Same search as the giraffe paper.

## Not filed
- Liu et al. 2023 Animals 13(5): 845 (roe deer, wild boar, ABR playback): MDPI page prints no "Creative Commons" sentence (only a metadata link), and Crossref was not used; held out on licence.
- Dryophytes (Hyla) chrysoscelis, Tanner and Bee 2020 Front Ecol Evol 8: 256 (wild-caught gravid females tested in a lab chamber): the reader returned only truncated sentences; only a complete sentence on synergism was usable. Lead.
- Scinax imbegue (Melo et al.): sentences truncated by the reader.
- Alytes obstetricans (Sci Rep 2019, 19456) already on main (sense_vibration); Bercy 2025 horses (semi-feral, no CC sentence); Tropical Life Sci Res elephant paper (captive); harbor seal PeerJ papers (captive or rehabilitated).

## Weak spots
Text came through the WebFetch reader, which returns about 125 characters per quoted sentence; short whole sentences and table rows were used and cuts are marked. Full-sentence verification against the page was not possible beyond the reader output.

## Risk flagged for the desk
Audits 317, 344, 345, 350 held out behavioural hearing responses where the stimulus at the animal is not defined (level only at 1 m from the source). Melo (75 dB, speaker about 1 m from the male) is closest to defined; giraffe (85 dB, point of measurement not stated), Nile crocodile (63 dB at 1 m, animals 10 to 30 m away) and vervet (no level seen) carry that limit, stated in each record's conditions.

## More leads not filed
- Soltis et al. 2014 PLoS ONE (African elephant, Samburu voices vs bee sounds): complete short Results sentences usable ("Distance moved in response to Samburu voices and bee sounds was similar (U = 102, n1 = 14, n2 = 13, p = 0.914)."), but the reader returned only a paraphrase of the licence sentence, so held out; Mammal Diversity Database page for Loxodonta africana not opened.
- Shannon et al. 2022 Animals 12(4): 495 (elephants, one vs three lions): MDPI page prints no Creative Commons sentence.
- Chabert et al. captive crocodile experiments, Chapuis et al. 2019 shark paper (white shark already held out by audit 345).
- A Springer copy host (biomedcentral...saludcastillayleon.es) was refused by the classifier and not retried.
About 38 WebSearches used.

## Desk disposition after audits 1096, 1097, 1098 (3 November 2026)
Audit 1096 kept both Physalaemus cuvieri lines (Melo, Both, Brasileiro 2024): line 1 had one error (significant call-parameter changes in the same males omitted), line 2 minor faults; the 75 dB level at about 1 m from the speaker, where the male sat, meets the stimulus-level precedent (audits 317, 344, 345, 350). Audit 1097 held out all three Chlorocebus pygerythrus lines (Deshpande et al. 2023): the paper gives no dB level, only call amplitudes matched to natural calls at 30 to 50 m. Audit 1098 held out all four lines (three Giraffa giraffa Table 4 rows, one Crocodylus niloticus): the giraffe 85 dB has no measurement point and the crocodile 63 dB is at 1 m with animals 10 to 30 m away. Merged lines 1 and 2; lines 3 to 9 dropped (corrected replacement text is saved in the audit reports /tmp/m311/audit-1097.md and audit-1098.md for a later ruling). Note: Crocodylus niloticus is on main under lambda_max_nm only, and Physalaemus cuvieri under visual traits only, so neither was a repeat.
