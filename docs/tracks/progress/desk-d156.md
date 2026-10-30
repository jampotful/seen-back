# desk-d156 progress (animal vein: thin sense cells, infrared, bat hearing, magnetic)

Scope: main (evidence, audit/corrected, audit/ALL) was grepped for sense_infrared, sense_electric, sense_magnetic, sense_airflow, sense_vibration, sense_thermal and sense_hearing. Thin groups picked: mosquito infrared (no Culicidae sense_infrared), bat hearing (only Rousettus), passerine magnetic compass beyond Erithacus/Sylvia/Catharus.

Records: 7 in docs/views/evidence/desk-d156.jsonl, all grade m, three papers, all open with a Crossref licence entry read through WebFetch.
- Chandel et al. 2024, Nature 633(8030): 615-623, 10.1038/s41586-024-07848-5 (CC BY 4.0; eScholarship copy read): Aedes aegypti infrared preference up to 70 cm, 34 C source PI 0.56, trpA1 mutant null (3 records); Anopheles stephensi landing bias PI 0.96 (1 record). Conditions carry CO2 5 percent and human odour in both zones, 29.5 C ambient, 80 females, 5 min; behavioural, not a recording.
- Lattenkamp et al. 2021, Proc R Soc B 288(1942): 20202600, 10.1098/rspb.2020.2600 (CC BY 4.0): Desmodus rotundus low-frequency ABR sensitivity (below 10 kHz) and Thyroptera tricolor ABR peak in the social-call range 49.2 to 78.4 kHz (2 records). Tested carriers 5 to 120 kHz, stated as the edges; physiological ABR, not behavioural.
- Tyagi and Bhardwaj 2021, Animals 11(6): 1541, 10.3390/ani11061541 (CC BY 4.0 per Crossref, CC BY 3.0 per page metadata): Emberiza bruniceps magnetic compass heading 236 deg in a rotated field (1 record).

Names: all GBIF accepted and exact matches (WebFetch of api.gbif.org species/match). Main was grepped by species and DOI before filing: no repeat.

Held out:
- Boute et al. 2023 Frontiers Mar Sci (fish electric thresholds): already on main (desk-d147).
- Jezequel et al. 2021 JEB (Homarus americanus hearing 80 to 250 Hz tested, best 80-120 Hz): Crossref lists only the Biologists user licence, not CC; held out.
- Dinh and Radford (Alpheus richardsoni particle motion): only a Dryad dataset page reached, no article licence; held out.
- Beatini et al. 2018 J Comp Physiol A (Aegolius acadicus ABR, 0.7 to 8.6 kHz): no licence statement on the page reached; held out.
- Geipel et al. 2021 PNAS (12 gleaning bats): licence read only as the PNAS license; not checked further; held out.
- Alvarado et al. 2024 Heliyon (Wistar rat ABR ageing): CC BY-NC and no baseline range; held out.
- Briceno and Bonilla 2009 (Centruroides courtship vibration): signal production, not reception; incomplete licence text.
- Several PMC pages returned a browser-check page and were not worked around.
- Lattenkamp S. bilineata sentence (echolocation 44.3 to 48.9 and social 17.7 to 22.1 kHz peaks): whole sentence about 60 words, too long to quote without distorting it; not logged.

Crossref via curl is refused; WebFetch worked (upper-case DOI needed for the Animals DOI). WebFetch returns pieces under 125 characters, so long sentences were reassembled from consecutive pieces and each quote was seen on at least two fetches.

No search records and no wanted lines.

## Desk disposition after audit 241
Audit 241 judged 7 records: 4 errors (lines 1 to 4, all Chandel 2024, all fixable). The assay transmits thermal IR only (cage 4 cm from the plate wall, convection and conduction blocked); the false "convective heat and infrared both present" clause is replaced. Line 1 now carries the 0.22 m2 source, PE film and n = 6 cages; line 2 the correct mid-range test and the shallow 33/37/40 C PIs; line 3 the intact odour navigation and retained heat preference in the mutants; line 4 the 27 C ambient and the rare probing after landing. Lines 5 to 7 merged as filed. Merged 7 records.
