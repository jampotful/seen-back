# desk-d535 progress

Angle: animal sense_thermal, sense_magnetic, sense_vibration and sense_touch in open-licence papers (the OLD-ANGLE reptile/fish eye-diameter paragraph was not followed). 3 records (docs/views/evidence/desk-d535.jsonl), all sense_magnetic, evidence_kind behavioural_response. About 36 WebSearches. check.py: 0 problems (plain and --require-evidence-kind).

## Filed
- Periplaneta americana, Sci Rep 11: 12221 (10.1038/s41598-021-91815-x): activity higher in rotated Earth-strength field (p = 0.028, N = 29 v 29), null at 5 G (p = 0.222, N = 16).
- Apis mellifera, Sci Rep 6: 23657 (10.1038/srep23657): PER conditioning to a 200 microtesla, 5 Hz field, day 2 7.9 v day 1 2.4 of 20 (n = 10); nerve-cord cut abolished it.
- Erithacus rubecula, Front Behav Neurosci 10: 55 (10.3389/fnbeh.2016.00055): weak broadband field disoriented birds (N = 16 per field, autumn 2013).

## Weak spots
- All text through the WebFetch reader: numbers come from its readings of Results and tables. No licence sentence was returned for any of the three pages (publisher's own open-access full text); Crossref licences could not be read (api.crossref.org list queries return no licence field; a permission prompt blocked a direct works URL). Species names not checked against an authority page.
- Honey bee author list: the reader showed four names with an ellipsis; byline needs checking.

## Not filed and why
- Crotalus cerastes ambush orientation (s41598-019-40466-0): already on main (audit/corrected/herps.jsonl).
- Garden warbler Sjoberg and Muheim (10.3389/fnbeh.2016.00029): no whole abstract sentence recoverable, Table 1 only.
- Wood mouse (srep09917): n only in Table 1, previously held by d241. Zebrafish (srep00727): CC BY-NC-SA and a laboratory strain.
- Aedes aegypti / Ae. japonicus thermal preference (s41598-024-63625-4): laboratory colony, author list truncated by the reader. Drosophila novamexicana/virilis/ezoana thermal preference (s42003-023-05280-5): no numeric preferred temperatures and the sentence names two species.
- Bactericera cockerelli playbacks (10.3390/insects11050299): laboratory colony; seal whiskers (s41598-019-49243-5) and canine vibrissae: fetch failed or domestic; rat whisker papers: laboratory strains; elephant bone conduction (fauot.2026.1744613): hearing, cadaver ears; reviews (Miller and Mortimer, Cokl et al., Bosman et al.) not fileable.
- No sense_thermal, sense_vibration or sense_touch record filed: no usable open primary paper reached with a whole quotable sentence, a wild species and a full author list.

## Desk disposition after audits 1080 and 1081 (3 November 2026)
Audit 1080 held out lines 1 and 2 (Periplaneta americana, Sci Rep 11: 12221; Apis mellifera, Sci Rep 6: 23657): no licence sentence was read on either page and no Crossref licence was reachable; the audit also found 7 errors (authors not in "Surname Initials" form; values beyond the quotes; cockroaches reused across runs so each N counts runs; honey bee byline incomplete, the page shows an ellipsis and the PDF failed). Both are dropped; the auditor's corrected Replacement text is kept in the audit report for a later auditor who can read a licence sentence on the exact page. Audit 1081 (line 3, Erithacus rubecula, Front Behav Neurosci 10: 55): 1 fixable error (value said more than the quote; spring 2014 and spring 2012 null results, the 48 nT narrow-band caveat, pre-selected birds, no broadband-versus-control comparison and calculated broadband intensity were added; the publisher PDF does print a CC BY sentence). The corrected line is merged; 1 of 3 records merged.
