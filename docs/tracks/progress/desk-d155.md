# desk-d155 progress (animal vein: thin sense_* cells other than hearing in turtles/anurans)

Scope: sense_thermal, sense_vibration, sense_airflow, sense_hearing. Main evidence logs and audit/corrected were grepped by species and DOI first; none of the taxa below had a line for these traits from these papers (Gryllus bimaculatus and Apis mellifera appear on main only for other traits or for a different Apis vibration paper).

Records: 11 in docs/views/evidence/desk-d155.jsonl, all grade m, all from open full text (CC BY, licence confirmed on Crossref and on the page). No search or wanted lines. Authors and volume/article numbers from Crossref via WebFetch. GBIF match gave ACCEPTED for all three species.
- Agriotes obscurus sense_thermal x5 (Merivee et al. 2020, Front Behav Neurosci 14:1, 10.3389/fnbeh.2020.00001): CHN rate 25.8 to 12.1 spikes/s (20 to 35 C), DHN rate 30.6 to 57.5 (20 to 35 C) and its loss of sensitivity above 35 C, MHN flat from 20 to 40 C (null), burst onset above 25 (30) C. Sex not reported; about 260 beetles overall.
- Apis mellifera sense_vibration x4 (Chehaimi and Kirchner 2024, Apidologie 55(4):44, 10.1007/s13592-024-01091-7): thresholds 0.25 m/s2 pp (workers, virgin queens at 500 Hz), 0.55 (laying queens), 0.6 (drones). 'pp' is undefined in the text; tested 350 to 500 Hz only.
- Gryllus bimaculatus sense_airflow and sense_hearing (Lu et al. 2023, Front Physiol 14:1153913, 10.3389/fphys.2023.1153913): a modulation study. The airflow record is the single stimulus level used (1.00 m/s), not a threshold; the hearing record is a behavioural effect of one 15-kHz, 70 dB SPL tone, not an audiogram. Notes carry the nulls (no change in response probability, latency, velocity or distance).

Quote method: sentences reassembled from short chunks the fetch tool returned (it refuses sentences over 125 characters), each confirmed on a second fetch; cuts are marked with " … ". Statistics inside parentheses were cut with a marked ellipsis.

Held-out leads:
- Culex pipiens Johnston's organ frequency organization (J Exp Biol 220(21):3927): page showed no licence statement.
- Anopheles coluzzii swarming hearing thresholds (J Exp Biol, 10.1242/jeb.243535): accepted manuscript copy, only a copyright line, no licence.
- Homarus americanus sound detection (J Exp Biol 224(6), 10.1242/jeb.240747): Ifremer repository copy, no licence statement.
- Womack et al. 2017 earless toads (Proc R Soc B 284: 20171670): PMC page shows no open licence.
- Monochamus alternatus vibration: already on main (desk-d147).
- Gekko gecko brainstem (Tang et al., J Comp Neurol), PMC author manuscript: no licence.
- PMC12383940 (Austruca lactea vibration) and PMC12534725 (lizard hearing): permission-request/reCAPTCHA pages; not worked around, not read.
- curl to frontiersin.org was refused by the proxy; no workaround attempted.
