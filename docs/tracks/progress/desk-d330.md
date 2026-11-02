# desk-d330 progress

Angle A: retry of open-access leads lost to PLOS and Nature rate limiting. Six records filed in docs/views/evidence/desk-d330.jsonl (check.py: 6 records, 0 problems). Stopped early because PLOS rate-limited most fetches (repeated limits, a pause of about two minutes between attempts did not clear it every time).

## Filed

| Species | DOI | Trait | Note |
|---|---|---|---|
| Philaenus spumarius | 10.1371/journal.pone.0190454 | sense_chemical (transduction) | EAG, all 50 VOCs gave responses in both sexes; female range and sex differences in conditions; page CC licence plus Crossref CC BY 4.0 vor |
| Crotalus durissus | 10.1371/journal.pone.0090622 | sensory_anatomy (anatomical_presence) | papillae absent (null) while present in Bothrops and Lachesis relatives; Crossref fetch refused, licence rests on page statement |
| Pipistrellus pipistrellus | 10.1371/journal.pone.0060752 | sense_echolocation (behavioural_response) | largest real scanning angle 42 deg, array-limited; bats and sex not reported; 33 vs 32 sequences discrepancy |
| Rhinolophus ferrumequinum | 10.1371/journal.pone.0062710 | sense_echolocation (behavioural_response) | RF call frequency drift up to over 900 Hz per day against constant SCF; captive, printed subspecies tragatus |
| Rhinolophus clivosus | 10.1371/journal.pone.0187769 | sense_echolocation (behavioural_response) | RF site means 80 to 100 kHz, 112 wild adults; body size and sex no effect |
| Rhinolophus clivosus | 10.1371/journal.pone.0199703 | sense_echolocation (behavioural_response) | null: 3 of 10 trials discriminated, not different from control |

## Not read (PLOS rate limit RATE_LIMIT_EXCEEDED on every retry, stopped)

pone.0056889 (swallow-tailed gull), pone.0043565 (elephant seal), pone.0054086 (turtle middle ear). Found through WebSearch; open for another unit.

## Not read (Nature: fetch failed, client_error)

srep39395 (Malacosteus niger), s41598-025-91987-w. s41598-018-25599-y appeared in search only as a nature.com epdf link carrying an author access token (not opened); its title is a daytime eyeshine paper, so not an eye-size lead.

## Not searched or opened

pbio.0050301 (Gymnotus sensory volumes) and pone.0099032 (honeybee hygroreceptors): not reached. For pone.0099032 no humidity trait key exists; list as a gap unless an existing key genuinely fits.

## Angle B (eye size, nocturnal against diurnal)

Searches (BMC, Frontiers, MDPI, PeerJ) gave no species-level open values in text: Fleishman 2024 lizard review (famrs.2024.1426675) and the mole-rat rhythm review (fevo.2022.878533) are reviews; the anuran eye size paper (fevo.2021.755818) keeps per-species data in a supplement; the kakapo paper (pone.0022945) takes eye values from earlier work and prints none in text; the kestrel and little owl paper (BMC Vet Res 2024) and the reef fish paper (BMC Evol Biol 2011) redirect to springer.com, refused. Pita et al. 2015 (peerj.1113) is already on main.

## Weak spots

- Crossref was read only for pone.0190454 (vor, CC BY 4.0); other licences rest on the page's printed Creative Commons statement.
- Family and order left blank everywhere; MDD not opened for the bat names.
- Rhinolophus ferrumequinum is the species of the printed subspecies tragatus.
- Methods for the bat records are partly summarised from truncated fetch pieces (noted in each record).

## Desk disposition after audit 444

Audit 444 held line 1 (Philaenus spumarius EAG, pone.0190454) out as unverifiable: journals.plos.org refused the page four times; the DOAJ record confirms authors, title and 12(12): e0190454, and the Abstract prints "(Hemiptera, Aphrophoridae)"; the page also reports a dose series, and the record gives only the 10 ug/uL dose. A re-reader should open it when PLOS answers. The other five lines carried 11 errors (8 if blank-but-printed family is not counted), all fixed from the auditor's text: Crotalus durissus (15 catalogued specimens listed in the Methods; family Viperidae), Pipistrellus pipistrellus (evidence_kind physiological_response), the bat printed as Rhinolophus ferrumequinum tragatus refiled as Rhinolophus nippon per the Mammal Diversity Database (its 8 analysed bats were the only ones that produced communication calls, out of 13 males and 7 females paired), Rhinolophus clivosus resting frequency (physiological_response; family Rhinolophidae), and Rhinolophus clivosus playback null (the other own-foreign pair p = 0.056, 6 of 8, and longer attentive behaviour in the test than at the end of habituation added). Optional note fixes applied. 5 of 6 merged.

Owner questions: should beam-scanning and other emission parameters take physiological_response (as main does) rather than behavioural_response; blank-but-printed family/order was counted by audit 441 and not by audit 438; add Rhinolophus nippon and Rhinolophus clivosus to gbif-names.tsv. Leads still open: pone.0056889 (swallow-tailed gull), pone.0043565 (elephant seal), pone.0054086 (turtle ear), pbio.0050301 (Gymnotus), pone.0099032 (honeybee hygroreceptors; no humidity key), srep39395 and s41598-025-91987-w (nature.com client_error). Angle B (eye size versus activity pattern) again gave nothing fileable.
