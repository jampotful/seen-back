# desk-d365 progress

Angle: multi-species papers, sensory statements other than eyes. 10 records from two papers, about 45 WebSearch/WebFetch calls (many spent on probes that returned one-species papers). check.py: 0 problems.

## Filed (docs/views/evidence/desk-d365.jsonl)
- Vertebrate Zoology 75: 459-485 (10.3897/vz.75.e167008; page-printed CC BY 4.0, Crossref CC BY 4.0 vor): Nectophrynoides luhomeroensis, N. uhehe, N. saliensis; Table 1 species means for TYMP (sensory_anatomy, horizontal tympanum diameter) and ED (eye_diameter_mm). Sexes pooled, n = 8, 195, 6. Quote is the whole table row (it carries all four columns incl. N. viviparus s.s.).
- Evolutionary Systematics 9(1): 145-166 (10.3897/evolsyst.9.148522; page-printed CC BY 4.0): Pristimantis chinguelas, P. nunezcortezi; holotype TD and ED from the holotype Measurements sentence.

## Weak spots
- Both papers were read through the fetch tool in pieces; the Vertebrate Zoology table columns were read from the XML in markup order (n values sum to the 257 adults stated).
- Registry: ASW pages opened for luhomeroensis and uhehe (family read from URL path); saliensis ASW page blocked. No registry opened for the Pristimantis species; family omitted there.
- Pristimantis measurement sentence joined from two fetch pieces; no Crossref check for that DOI.
- No tympanum/absent statements exist in the Nectophrynoides XML read (it stops before the Taxonomy section).

## Not filed
- Pristimantis yonke: measurement sentence printed with an odd SVL ("19,6.3"); not trusted. Diagnosis and description tympanum sentences are over 40 words.
- EJT 993 Stenohya (8 new pseudoscorpions): trichobothria/eyes, publisher PDF blocked; earlier desk-d317 found sentences too long.
- Searches for loach barbels, scorpion pectines, katydid tympana returned single-species papers (Oreonectes andongensis ZooKeys 1196, Scorpiops doiphukha ZooKeys 1241, Dentotibium ramucantoris JOR).

## Desk disposition after audits 485 and 486 (2 November 2026)

Audit 485 (lines 1-6, Nectophrynoides luhomeroensis, uhehe, saliensis; Table 1 means) found 6 of 6 in error, all note faults: each note said only the table carries the figure, but the holotype descriptions print TYMP and ED. Table values, columns, n, quotes, keys, licence and bibliography held; the within-species unsexed mean was ruled acceptable. N. saliensis registry still unchecked. Audit 486 (lines 7-10, Pristimantis chinguelas and P. nunezcortezi) found 4 of 4 in error (5 faults): family was omitted on all four records, and line 7 left out that the P. chinguelas tympanic membrane is absent so TD measures the annulus. Overall 10 of 10 in error, none in quote or value.

Desk ruling on family: the auditor supplied Strabomantidae per audit 468, but the Amphibian Species of the World search paths it saw for both species show Craugastoridae, and main's Pristimantis rows are Craugastoridae 9, Strabomantidae 3. The merged lines carry Craugastoridae with a note saying so. Owner question: which family main should follow for Pristimantis (the Craugastoridae and Strabomantidae assignments disagree across main).

Replacement lines merged; check.py 0 problems.
