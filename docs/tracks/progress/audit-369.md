# audit-369: desk-d277, evidence line 1

Audited 1 November 2026 from the desk-d277 files present untracked in the worktree (docs/tracks/progress/desk-d277.md and docs/views/evidence/desk-d277.jsonl, 1 line; neither committed here, neither edited). Worktree HEAD 3969746d ("Merge d276 after audit 368"). `python3 -I tools/senses/check.py | grep 'd277\.'` prints "docs/views/evidence/desk-d277.jsonl: 1 records, 0 problems".

Sources opened (WebFetch): academic.oup.com/iob/article/8/1/obag033/8722227 (four passes, all answered, URL from search results); api.crossref.org/works/10.1093/iob/obag033; api.obis.org/v3/taxon/Carcharhinus%20limbatus (answered; the desk had it refused). 6 WebSearches. Not opened: the FAU repository item fau.isle.flvc.org/node/46588 (the same title; likely the thesis, not the version of record), news items.

## Bibliographic and licence

Crossref: C L Sullivan, E R Gerstein, S M Kajiura, in the record's order; title "Orientation of Blacktip Sharks (*Carcharhinus limbatus*) to Underwater Sound" (italics markup only), identical to the record; Integrative Organismal Biology, volume 8, issue 1, article-number obag033, no page field; issued 2026 (published-print 2026-01-14, published online 2026-06-30); relation empty, no update-to. The page prints "Integrative Organismal Biology, Volume 8, Issue 1, 2026", article obag033, DOI 10.1093/iob/obag033. Record's `source` matches on every field; access "open" right.

Licence: the page body prints no Creative Commons sentence, only "© The Author(s) 2026. Published by Oxford University Press on behalf of the Society for Integrative and Comparative Biology."; page permissions metadata "CC BY". Crossref license: https://creativecommons.org/licenses/by/4.0/, content-version vor, start 2026-06-30. Accepted (publisher page with no licence sentence + Crossref CC vor; metadata tag does not conflict). Bibliographic faults 0; licence faults 0.

## Names

OBIS v3 taxon: scientificName "Carcharhinus limbatus", taxonomicStatus accepted, family Carcharhinidae, order Carcharhiniformes; authorship printed "(Valenciennes, 1839)". The desk's ALA/AFD authority prints "(Muller & Henle, 1839)". The record carries no authorship field, so the difference touches only the note (uncounted; replacement below). Main writes Carcharhinidae with Carcharhiniformes in 29 rows. The species is not in docs/views/gaps/gbif-names.tsv; docs/views/gaps/try-species.json line 1584 lists it (Carcharhinidae, Carcharhiniformes). Name faults 0.

## Duplicates

grep of the whole docs/ tree (incl. docs/views/audit/corrected, audit/ALL.jsonl, sheets, recheck, voice) for "limbatus" and "obag033": the only Carcharhinus limbatus row is corrected/fish-shark.jsonl line 117 (ALL.jsonl line 857), a pooled three-species behaviour_vision row from another source; no sense_hearing row, no obag033. git grep of all 90 origin/research/desk-d2* branches (evidence and progress) finds only origin/research/desk-d277 itself; of origin/research/audit-3* progress files, none names obag033 or Carcharhinus limbatus. Duplicates 0.

## Trait key and ruling

Ruling: fileable under sense_hearing. Audits 344 and 350 set the line: main files behavioural hearing responses where the stimulus at the animal is defined (band and level) with a per-animal response; audit 350 held out Phocoena because the deterrent was defined only at 1 m and the outcome was click-logger minutes, and audits 317/344/345 held out tank-occupancy or interaction scores without per-response stimulus. Here each scored response has a measured distance (speaker to snout, frame before the turn) and an estimated sound pressure level at the shark, obtained by subtracting a transmission-loss curve fitted to radial hydrophone measurements (about 1, 10, 20, 30 and 60 m) from the 1 m source level; the bands, waveform and source level (140 dB re 1 µPa at 1 m) are stated, and a 10 kHz control of the same output volume preceded every stimulus with no response (Results "(n = 209)"). Limits the record must carry: received level is printed only relative to peak ambient (16.0, 27.8, 44.6 dB), with no absolute ambient level printed; only sound pressure was measured ("Ideally, particle motion would have been measured as well, but this was not practical under the field conditions."), though sharks are particle-motion sensitive; the Discussion warns that energy below each band "would produce a near field stimulus". The Phocoena owner question stays open and does not decide this one: the difference is the per-response received estimate.

Units "m" (response distance) is new for sense_hearing on main (degrees: desk-d232 Tyto alba, desk-d238 Gryllus bimaculatus; the rest Hz/kHz/dB), but units are free text and the record marks "behavioural response, not a threshold". Uncounted; owner may prefer "m (distance from source at response)". Grade m fits.

## Per-record findings

### Line 1, Carcharhinus limbatus, responded from at least 62 m

Quote, Synopsis, one sentence returned whole with both ends: "Sharks responded to all frequencies from at least 62 m, and 71.6% of all responses (n = 209) occurred in the far field." MATCH, 24 words. The "(n = 209)" is the Synopsis's own error: Results "The majority (71.5%) of the 165 responses to the sound stimuli occurred from the acoustic far field."; 209 = 72 + 54 + 83 presentations. The record states this in conditions and does not use the 71.6%/209 figure. "At least 62 m" is the paper's pooled statement; the 400-800 Hz maximum is 61.8 m, so 62 is the authors' rounding; per-band ranges are carried. Not a pooled value across differing bands beyond what the paper itself states.

Verified, verbatim or close tool pieces: "The mean response distances were 40.7 m ± 10.69 m s.d. (range 15.0–74.0 m, n = 59)."; 41.0 ± 15.56 (12.4–66.1, n = 47); 30.0 ± 12.81 (11.1–61.8, n = 59); F = 15.014, P < 0.001; Scheffe P = 0.887; SPL at response 16.0, 27.8, 44.6 dB re peak ambient, F = 247.17, P < 0.001; responses 59/72, 47/54, 59/83; turns 77.3 ± 22.42, 66.6 ± 22.19, 72.2 ± 25.04 degrees, F = 2.060, P = 0.133; "The speaker was suspended 1 m below the ocean surface."; "drifted with the current to approximately 13–19 m off the stern of the boat."; "amplitude modulated, intermittent pulse trains of filtered random noise"; 5 s control "(10 kHz irregularly pulsed sound)", 5 s ambient, then "one of the three randomly chosen experimental stimuli"; "The output volume was kept the same for each stimulus throughout the study."; response "initiated a sudden change in trajectory" "immediately following the onset of the stimulus"; ImageJ speaker to snout tip; near field 3λ of the lowest frequency; "Experiments were conducted between 7:30 am and 12:30 pm on days with minimal wind."; Jupiter Beach, Palm Beach and Pompano Beach inlets; Synopsis "Sharks never responded to a high frequency (10 kHz) control stimulus of comparable volume." No chum, bait, sex or total length anywhere in the text; the authors call their stimulus "repulsive"; no individual identification.

Faults:
- Value says more than the quote. "orients away from low-frequency pulsed sound" rests on a different Synopsis sentence ("Upon detection, *C. limbatus* elicited a sudden 20–160° turn away from the speaker and rapidly swam away."); the logged quote says only "responded to all frequencies". The value must say no more than its quote.
- Design confounds and qualifiers omitted: boat anchored, "the engine was turned off", speaker distance chosen because it "minimized the effect of the presence of the boat"; drone "undetectable by the sharks" is the authors' claim from cited in-air literature, not measured here; sharks located as drone-spotted aggregations; sex and size not reported; trials "omitted during trials in which stimulus onset coincided with the presence of other variables" or ambiguous, number omitted not reported; pressure only, particle motion not measured; near-field bleed-over caveat; SPL at the shark is a model estimate (method says "propagation modelled", conditions present the levels as if measured).
- Uncounted: Discussion's single mean turn 72.7 degrees versus the per-band means; turn range 20–160 degrees (Synopsis) not carried.

**Line 1 error (value beyond its quote; boat/drone/aggregation, exclusions, pressure-only and estimated-level qualifiers omitted).** Fixable.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Carcharhinus limbatus, responded from at least 62 m | error, fixable | value, conditions | quote MATCH (24); "orients away" not in the quote; design confounds, exclusions, particle-motion and estimated-SPL qualifiers omitted; 10 kHz null and 209/165 split carried |

Errors 1 of 1 audited record (100%), above the 5% bar; none held out. By kind: scientific context 1 (value beyond quote; omitted confounds and qualifiers); quote form 0; bibliographic 0; licence 0; names 0; duplicates 0; trait key 0 (fileable, see ruling); grading 0.

Unchecked: figures and supplementary video; the pulse-rate details of the waveform sentence (tool cut); whether any trial was excluded for the drone itself; the absolute ambient levels behind "re peak ambient" (not printed); the cited drone-noise literature; the FAU repository copy.

Owner questions: (1) confirm that a playback avoidance response with a per-response distance and a received level estimated relative to ambient is fileable under sense_hearing (this audit rules yes, distinguishing audit 350); (2) units "m" for a sense_hearing behavioural distance.

## Replacement text

Each old string occurs exactly once in its field in line 1 (checked with `str.count` on the desk file, and applied to a scratch copy).

Line 1, counted:
- `value`: "orients away from low-frequency pulsed sound (100-800 Hz bands) from at least 62 m" -> "responded to all frequencies tested (the 100-200, 200-400 and 400-800 Hz bands) from at least 62 m"
- `conditions`: "no chum or bait mentioned," -> "no chum or bait mentioned, boat anchored with the engine off, drone at about 40-50 m stated by the authors to be undetectable by the sharks (drone noise not measured in this study), sharks located as aggregations, sex and size not reported,"
- `conditions`: "the sound pressure level eliciting a response rose" -> "the sound pressure level at the shark eliciting a response (estimated by subtracting fitted transmission loss from the 1 m source level) rose"
- `conditions`: "far field defined as beyond 3 lambda of the lowest frequency in each band" -> "far field defined as beyond 3 lambda of the lowest frequency in each band; trials were omitted when stimulus onset coincided with other variables or the response was ambiguous, the number omitted not reported; only sound pressure was measured (the authors state particle motion was not practical to measure), and the Discussion notes that energy below each band could give a near-field stimulus"

Line 1, uncounted:
- `note`: "agreed by marinebiodiversity.org.bd." -> "agreed by marinebiodiversity.org.bd and OBIS v3 (accepted, Carcharhinidae, Carcharhiniformes; OBIS prints the authorship as (Valenciennes, 1839)); audit 369."
