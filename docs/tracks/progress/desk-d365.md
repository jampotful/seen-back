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
