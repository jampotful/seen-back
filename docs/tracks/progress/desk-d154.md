# desk-d154 progress (animal vein: thin sense cells, hearing)

Scope: the gap table (tools/views/gaps.py) holds only vision traits plus sense_chemical and sense_light_nonvisual, so the sense cells were chosen by grepping main (evidence, audit/corrected, audit/ALL) for sense_hearing, sense_vibration, sense_airflow, sense_electric, sense_magnetic, sense_infrared, sense_thermal and sense_echolocation. Hearing in turtles and anurans had few or no primary records.

Records: 8 in docs/views/evidence/desk-d154.jsonl, all grade m, three papers, all open with a Crossref licence entry read through WebFetch.
- Piniak et al. 2016, PLOS ONE 11(10): e0159711, 10.1371/journal.pone.0159711 (CC0): Chelonia mydas AEP hearing, underwater 50 to 1600 Hz and in air 50 to 800 Hz (2 records). Quotes seen on two fetches.
- Cobo-Cuan et al. 2022, J Comp Physiol A 209(1), 10.1007/s00359-022-01569-8 (CC BY 4.0): Odorrana tormota DPOAE response span, female 2 to 7.4 kHz, male 2.5 to 20 kHz (2 records, one shared sentence). DPOAE is an inner-ear emission, not a behavioural range; stated in each record.
- Wang et al. 2022, Front Ecol Evol 10: 856660, 10.3389/fevo.2022.856660 (CC BY 4.0): Trachemys scripta elegans ABR bandwidth at 10, 20, 30, 40 C (4 records, one shared sentence). Stimulus set 0.2 to 1.5 kHz bounds the range edges; stated.

Names: Odorrana tormota (Wu, 1977), Chelonia mydas and Trachemys scripta elegans (subspecies, Wied 1838) are GBIF accepted names (match calls through WebFetch). Main was grepped by species and DOI before filing: no repeat (Chelonia hearing on main is the Southwood 2008 review; Trachemys hearing on main is Christensen-Dalsgaard 2012).

Held out:
- Georgiades et al. 2023, Nat Commun 14: 4338 (Anopheles gambiae flagellar receiver, CC BY per Crossref): values are octopamine pharmacology (control SSO about 350 Hz, quiescent best frequency about 500 Hz after octopamine), no baseline hearing range; not logged.
- Lauridsen et al. 2021, JEB (Pelophylax esculentus, Rana temporaria ABR): Crossref fetch failed and the page states only a copyright line; not read further.
- Ordiway et al. 2024 (chicken hatchling ABR, Neuroscience Insights): the copy reached was a Northwestern lab deposit; Crossref fetch failed; held out as an unlicensed author deposit.
- Schrode 2014 and Lohr 2013 (PMC): NIH manuscript copies, no licence statement; Hyla chrysoscelis hearing is on main already.
- Holgate et al. 2023, Sci Rep (goldfish): hearing curve is pooled from 23 earlier studies; only the startle optimum (250 Hz) is new, a behaviour result.
- Sun et al. 2020 Bioacoustics (Amolops torrentis): no open licence stated.
- Penna et al. 2026 Gayana (Chilean anurans): compilation of earlier audiograms, no DOI, CC BY-NC.
- Bats (Eptesicus fuscus echolocation): already on main; the Frontiers bat papers read reported no new frequency values.
- PMC pages for Spalax magnetic work and a thermal paper returned a browser-check page; not worked around.
curl to Crossref and Europe PMC is refused by the sandbox (proxy 403); WebFetch only. Crossref fetches failed for some DOIs on a first try and worked with an upper-case DOI in the URL.

No search records and no wanted lines.

## Desk disposition after audit 239
Audit 239 judged 8 records: 5 errors (lines 1, 2, 3, 4, 8), all fixable. Lines 1 and 2 now carry the tested-frequency set (50 Hz is the lowest tone tested). Lines 3 and 4 refiled on the primary-frequency spans (2.27 to 6.73 kHz females, 3.09 to 14.73 kHz males) with replacement quotes. Line 8 carries the 40 C heat-limit context. Lines 5 to 8 add the 3 h exposure and 85 dB SPL ceiling. Journal pages added on lines 3 and 4; second review named on line 1. Merged 8 records.
