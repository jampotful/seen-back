# desk-d643 progress

Angle: species-specific amphibian pupil_shape searches for the listed leads, then further amphibians with an eye row on main and no pupil row (OLD-ANGLE paragraph not followed). Started 4 November 2026. About 38 WebSearches, all species-specific; WebFetch only on URLs from my own results; no classifier denial; no Crossref, Plazi, zenodo, PMC, zobodat or blog fetch. Log docs/views/evidence/desk-d643.jsonl: 7 records, trait pupil_shape, no evidence_kind (as the untyped pupil_shape rows on main). check.py: 0 problems for desk-d643 (plain and --require-evidence-kind).

## Filed (value; paper)
- Scutiger kanjiroba, vertical (ZooKeys 1210: 229-246, 10.3897/zookeys.1210.127106; holotype description, marked cuts; ASW opened)
- Rhacophorus qiongica, horizontal (ZSE 100(2): 625-643, 10.3897/zse.100.118879; holotype description, marked cuts; ASW opened)
- Theloderma khoii, circular (EJT 794: 72-90, 10.5852/ejt.2022.794.1655; labelled holotype entry 'PUPIL. Circular.'; ASW opened)
- Scutiger khumbu, vertical (EJT 989: 189-214, 10.5852/ejt.2025.989.2893; nominate holotype Head entry; ASW opened; subspecies makalu not filed)
- Vietnamophryne abscondita, round (Herpetozoa 39: 145-160, 10.3897/herpetozoa.39.e191333; ASW opened; the Methods define EL, not ED)
- Odontophrynus toledoi, horizontally elliptical (EJT 847: 160-193, 10.5852/ejt.2022.847.1991; holotype in-life sentence, iris colour cut; ASW opened)
- Phyllodytes gravata, horizontal (EJT 1048: 62-83, 10.5852/ejt.2026.1048.3235; holotype sentence, middle cut as one marked cut because the reader would not print it; ASW opened)

## Not filed and why
- Boulenophrys nebulosa: pupil_shape already on main (desk-d630).
- Leptobrachella aspera, L. bashaensis, Kurixalus lenquanensis, Xenophrys yingjiangensis (two differently worded searches each): only figure pages, Plazi, PMC, DOAJ and mirror sites; no publisher article page. Gracixalus yunnanensis: publisher XML returned truncated before the description (no 'pupil' in the part read). Gracixalus damingshanensis and Brachytarsophrys guilinensis: ZSE pages returned a "Site under maintenance" notice.
- Pupil sentence not found or no page: Phrynopus remotum (PeerJ page has no 'pupil'); Odorrana leishanensis, Nidirana guangxiensis, N. shyhhuangi, Amolops dafangensis, Quasipaa taoi, Odorrana sudianensis, Physalaemus araxa, Adenomera guarani, Pseudopaludicola coracoralinae, Guibemantis albomaculatus, Amnihyla grinpela, Ingerophrynus chrysolophus (no publisher text page reached; ASW pages exist for most). Scutiger khumbu makalu (subspecies) left out.

## Weak spots for the auditors
- Text came through the WebFetch page reader (about 125 characters per sentence, long sentences returned in pieces and joined; tooltip expansions cut). Phyllodytes gravata: the middle of the holotype sentence was not printed by the reader (first 12 and last 25 words read); the quote cuts the whole middle.
- Theloderma khoii quote is a labelled entry ('PUPIL. Circular.'), not a full prose sentence.
- Odontophrynus toledoi: pupil is described in the 'Coloration in life' sentence with iris colours (cut).

## Desk disposition after audits (4 November 2026)

Audits 1343 to 1346 judged all 7 lines (Scutiger kanjiroba, Rhacophorus qiongica, Theloderma khoii, Scutiger khumbu, Vietnamophryne abscondita, Odontophrynus toledoi, Phyllodytes gravata): every line fixable, none held out or dropped; the auditors' replacement text was merged (7 records; check.py 0 problems both variants). Audit counts: 1343 reported 2 of 2 in error (Results heading missing; a cut mark where the paper prints "(ED)"; Methods fragment made the whole printed sentence); 1344 reported 1 of 2 (Theloderma khoii: where field lacked printed Class, Order, Family and genus authorities; the desk-d588 row for the paper is a tympanum row, not an eye row; the labelled entry "PUPIL. Circular." was accepted as the quote; Scutiger khumbu matched, nominate holotype); 1345 reported 1 of 2 (Vietnamophryne abscondita: Methods sentence cut without a mark, and the "preserved or live is unstated" claim was wrong because the holotype description opens "specimen in good state of preservation"; Odontophrynus toledoi passed); 1346 (Phyllodytes gravata): 4 uncounted faults; the unread middle of the holotype sentence was read by the auditor and holds no pupil qualifier, so the quote stands. By the auditors' count 4 of 7 lines were errors, all fixable wording, heading-path or cut-mark faults; none was a value, licence or repeat error. Merged under the desk's practice for wording-only faults and disclosed as above the 5% line.

Unit notes: no slip and no classifier denial. The unit read the first 12 and last 25 words of the Phyllodytes gravata holotype sentence and cut the whole middle with one marked cut; audit 1346 read the middle and the cut stands. Leads that failed: Boulenophrys nebulosa is already on main (desk-d630); the S. khumbu subspecies makalu (also prints pupil vertical) is left unfiled; several species had no publisher text page in the unit's results (carried to d644).
