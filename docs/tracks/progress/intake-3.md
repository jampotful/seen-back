# Intake 3 progress note (round 2 Drive intake)

Branch: research/intake-3, cut from main. Launch prompt: docs/tracks/prompts/round2-intake.md.

## Files (ten named in the launch prompt, keyed by sha1 of the Drive id)
Status: not yet downloaded. Each file: download, decode, pdftotext -layout, match to wanted lines, log, quotecheck.

| sha1 key | file | DOI | status |
|---|---|---|---|
| e61667cd6e3d | Chatterjee 2020 | 10.1007/s00359-020-01429-3 | pending |
| 101b48fd7a6c | Cervino 2021 | 10.1098/rspb.2021.1402 | pending |
| e3ec00e406be | Odeen 2003 | 10.1093/molbev/msg108 | pending |
| dd1efaef2dfe | Martinez 2022 Ophthalmology of Crocodilia (partial) | none listed | pending |
| 78d5a3419d9c | Hebel 1976 | 10.1007/bf00346285 | pending |
| 611f5baf89d7 | Gaffney 2003 | 10.1016/s0042-6989(03)00304-3 | pending |
| 321a986fc9c5 | Entsu 1992 | 10.1016/s0168-1591(05)80052-8 | pending |
| cbf0d73ac4c0 | Porter 2014 | 10.1242/jeb.108456 | pending |
| 5c425bae3a47 | Nakagaki 1996 | 10.1111/j.1751-1097.1996.tb01847.x | pending |
| 9e9b56a8ddba | Braekevelt 1990 | no DOI | pending |

drive.jsonl: no line on main for any of these keys (checked 13 October).

## Progress
- Branch created. Nothing downloaded or logged yet.

## Next
1. Download and extract the ten files to the scratchpad.
2. Match each to docs/views/wanted/*.jsonl, log records, run quotecheck.
3. Append drive.jsonl lines; add wanted lines for partial file references.
