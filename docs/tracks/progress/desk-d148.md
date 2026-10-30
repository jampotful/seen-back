# desk-d148 progress (animal vein: thin sense_* cells in taxa not yet covered)

Scope: sense_hearing and sense_thermal. Main (evidence, audit, searched, wanted) was grepped for Gadus, Rhodnius, the Sand and Karlsen DOI and Desmodus before filing; Gadus and Rhodnius had no sense_* line (Desmodus has sense_infrared already). No search records and no wanted lines (the vein is sense traits, not harvest genera).

Records: 2 in docs/views/evidence/desk-d148.jsonl, grade m, one named species each, open full texts read (Results, Discussion), so no "partial" flags. GBIF species match ACCEPTED for both; Crossref gave authors, volume and issue for the Rhodnius paper and Sand and Karlsen (issue 1, pages 197-204).
- Gadus morhua sense_hearing (Sand and Karlsen 1986, J Exp Biol 125(1):197, 10.1242/jeb.125.1.197): threshold close to 1e-5 m/s2 at 0.1 Hz. The PDF text layer garbles the units and 0.1, so the value was checked against the journal-page abstract (10-5 m s-2 at 0.1 Hz). 11 cod, only six trainable to low frequencies; the authors say thresholds might be masked by tube background noise. Water temperature not stated.
- Rhodnius prolixus sense_thermal (Lienard et al. 2024, iScience 27(4):109541, 10.1016/j.isci.2024.109541, CC BY): RpTRPA5B activation threshold 53 C (Po 0.1), T0.5 58.6 C in the next sentence. In vitro HEK293T channel, not a whole-animal threshold, noxious range, no n in the legend, paralogs not tested.

Quote method: whole sentences under 40 words, reassembled from 125-character pieces and confirmed on a second fetch; the Rhodnius quote keeps the printed curly quotation marks.

Held-out leads:
- Schilman and Lazzari 2004, Acta Trop 90(1) (Rhodnius prolixus preferred temperature 25.0 C males, 25.4 C females): behavioural preference, not a threshold, and only a repository copy seen; not filed.
- Vampire bat TRPV1 (Gracheva et al. 2011, Nature, 10.1038/nature10245): Springer page only; Desmodus infrared already on main.
- Anopheles coluzzii swarming hearing (Univ. Greenwich record gala.gre.ac.uk/id/eprint/33875) and jeb208785 (J Exp Biol 222): found in the last search, not opened.
- Rojas-type PMC pages and Gryllus bimaculatus PMC5378147, PMC3896795: not opened.
- sense_taste still has no trait key.

## Desk disposition after audit 233
Audit 233 found 0 of 2 records in error. Both were merged. The auditor's uncounted additions were applied: the cod units now read "m/s2 (root-mean-square particle acceleration)" and the conditions carry the staircase method (3 dB steps at 50 % response probability, 2 to 3 days per frequency, mean ± S.D.) and the point that the lateral line was not blocked; the Rhodnius note carries the Discussion's remark that activation above 50 C lies outside the bug's ecological range and above its cited upper thermal tolerance of 50.5 C. The cod 1e-5 m/s2 figure was confirmed against the publisher HTML abstract (10−5 ms−2 at 0·1 Hz) after the PDF layer printed it garbled. The Rhodnius record is an in-vitro HEK293T channel (partial activation, paralogs untested), consistent with main's snake TRPA1 and Python regius channel lines. Leads: whole-animal Rhodnius heat-response papers (HAL hal-00657961, PMC1978521) were found by the auditor but not opened; hal-01323724 was blocked by a bot check. Other held-out leads: Rhodnius temperature preference (Schilman and Lazzari 2004), vampire bat TRPV1 (Nature), Anopheles coluzzii swarming hearing, J Exp Biol 222 jeb208785, Gryllus PMC pages.
