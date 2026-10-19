# Audit 74: harvest-57 (branch research/harvest-57, commit 8f2f9dc2)

Gate: `screen_candidates.py --check` on the 17 records and 4 wanted lines prints "0 problems".

## Sample (seed 74)

The unit holds 17 records, fewer than 20, so the sample is the whole unit: lines 1 to 17. Because the unit is its own sample, the "check 15 more after an error" rule is already met.

## Method

For every record I ran `harvest_get.py` for the genus and compared `queries` with the harvest's query and family-review lines (all 17 match word for word, then the "web: " searches), compared `chased` with the citation-step lines, compared `canon` with docs/views/research/canon.jsonl by trait and taxon (script), read the `screened` abstracts that harvest_get prints, and ran about 17 WebSearches and 4 fetches of URLs my searches returned. No library proxy, ResearchGate or academia.edu page was opened. Ten `screened` ids (e.g. 10.3390/insects16111122, 10.1242/jeb.115923) come only from `screen_candidates.py`, as in earlier audits, and were judged from the record's own description and, for jeb.104281, from the paper.

## Verdicts

| Line | Record | Verdict |
|---|---|---|
| 1 | Phigalia acuity_cpd; interommatidial_deg | ok. Queries and citation steps match. Own searches (ommatidia, facet number, geometrid eye) found no Phigalia paper. Seven canon items named, none omitted. |
| 2 | Phigalia cff_hz; corner_hz | ok. Three screened moth-melanism papers hold no flicker data. |
| 3 | Euproctis acuity_cpd; interommatidial_deg | ok. Lymantria xylina eye paper is another genus and names no Euproctis in its abstract. |
| 4 | Euproctis cff_hz; corner_hz | ok. |
| 5 | Bucorvus cff_hz | ok. No ground hornbill flicker value found. |
| 6 | Bucorvus lambda_max_nm; spectral_range_nm | ok. Twelve canon items named, none omitted. No hornbill pigment found; Assessing the use of genomic DNA as a predictor of avian SWS1 lambda max (agris record) is a lead (species list unseen). |
| 7 | Opisthocomus cff_hz | ok. |
| 8 | Opisthocomus acuity_cpd; interreceptor_deg | ok. Burton 2008 (visres.2008.08.001) is eye-size scaling, no cell spacing. |
| 9 | Teira acuity_cpd; fovea | ok. jeb.104281 holds oil-droplet histology of six other lacertids and no fovea or acuity value. |
| 10 | Teira fov_h_deg | ok. |
| 11 | Teira lambda_max_nm; receptor_classes | ERROR. The screened entry for 10.1242/jeb.104281 (Perez i de Lanuza and Font 2014) says "no Teira pigment or receptor class is recorded". The paper sequences the SWS1 opsin of Teira dugesii (GenBank JQ917096) and reports all 13 UV-tuning residues (fetch of the publisher PDF). Main logs exactly this kind of row as lambda_max_nm grade g from the same paper for Meroles knoxii (recheck-10-fixed, sweep-73), Ophisops occidentalis (sweep-65) and Iberolacerta cyreni (sweep-67). The record's own note that main's rows "name" other genera with "no Teira row" shows the omission, not a measurement-free paper. |
| 12 | Teira pupil_shape | ok. Reptile Database account of Teira dugesii and the 2022 LJMU thesis (Jordan) state no pupil; no genus diagnosis found. Canon list omits The nocturnal bottleneck (Heesy and Hall 2010, covers "other amniotes", uncounted lead). |
| 13 | Menura acuity_cpd | ok. |
| 14 | Menura cff_hz | ok. Six screened behaviour and ecology papers hold no flicker data. |
| 15 | Menura binocular_deg; fov_h_deg | ok. Canon items named, none omitted. |
| 16 | Kokkocynips receptor_classes | ok. Own searches found no cynipid ommatidium or ERG paper beyond the Trybliographa rapae behavioural paper (another genus). |
| 17 | Neoconocephalus spectral_range_nm | ok. A katydid, so point 9 does not apply; a lamp search found only patents and a taxon-dependent attraction paper (lead below). |

## Count

- Errors: 1 in 17 = 5.9% (record 11). Over the 5% line: the unit fails on its own rate.
- Pooled with audits 43 to 51 and 55 to 73 (7 errors in 647): 8/664 = 1.2%.
- Fix for the desk: log the Teira dugesii SWS1 row from jeb.104281 (lambda_max_nm, grade g) and remove lambda_max_nm; receptor_classes needs re-screening for Teira (the paper's retinal oil droplets cover other species only).

## Point 9 (light-trap table)

The Phigalia and Euproctis records are acuity_cpd, interommatidial_deg, cff_hz and corner_hz, and `harvest_get.py` lists no open spectral_range_nm for either genus, so no spectral_range_nm record exists to test. Neoconocephalus is a katydid. No error under point 9. Whether Nowinszky et al. 2022 lists these moths is unseen (lead).

## "Main already holds" claims (six genera)

Read in docs/views/audit/corrected, docs/views/evidence and gbif-names.tsv, under old and new names.

- Gonatodes (fovea, pupil_shape): held. Fovea by sweep-49:1 (genus, grade g) and recheck-7-fixed:1 (partial); pupil_shape by sweep-49:2 (partial, a family-level statement about sphaerodactylid geckos, the note says "not measured in an adult Gonatodes"). The pupil hold is the weakest of the six.
- Trachemys (fovea): held by corrected/herps:112 (Pseudemys scripta elegans, streak; GBIF accepted name Trachemys scripta), canon-3:620, intake-7:6 and partial oa rows.
- Dasyprocta (fovea): held by corrected/squirrel-deer-rabbit:161, canon-3:622 (printed D. aguti, now D. leporina), oa-1:3614, partial oa-2:3966.
- Dromaius (spectral_range_nm): held by oa-9:366, grade m: lower limit about 335 nm, upper limit not stated. Held by the letter; the cell is half a range.
- Zanda (formerly Calyptorhynchus): held only by sweep-33:5, grade g (opsin-inferred, no Zanda sequenced). Calyptorhynchus rows in canon-5, oa-1, oa-2 and oa-4 are other traits. No row under the old name for spectral_range_nm.
- Psephotus: held only by sweep-43:5, grade g (order-level inference). Psephotellus has no row.

No false claim of the Equus kind or the Fowlea kind: each open trait has a row on main. Zanda and Psephotus hold the trait with inferred rows only. Tockus: fov_h_deg is open on main (canon-3:79-80 hold Bucorvus and Tockus binocular_deg only); Lophoceros has no rows. The wanted line for Martin and Coetzee covers it.

## Wanted lines (faults listed, not counted)

1. Martin and Coetzee, Ibis 146:18-26, DOI 10.1111/j.1474-919x.2004.00211.x: the Birmingham record gives year 2004; the line says 2003. Authors, DOI and the two species (Bucorvus leadbeateri, Tockus leucomelas, retinal fields by ophthalmoscopic reflex, binocular field about 30 deg) check out.
2. Cardiff thesis (W2162946311): not opened; no check possible.
3. BMC Genomics 2015 opsin paper: not opened.
4. bioRxiv 2025.12.19.695568: the fetched text names only the degu as a studied species and not the hoatzin; the line's hoatzin claim looks unsupported (my fetch gave no title or authors).

## Leads (compilations whose species lists I could not see)

- Lind et al. "Lens and cornea limit UV vision of birds" (jeb.243129) and Odeen and Hastad 2013: may bear on Zanda, Psephotus and Dromaius spectral_range_nm and on Bucorvus and Opisthocomus lambda_max_nm and spectral_range_nm (records 6, held genera).
- Assessing genomic DNA as a predictor of avian SWS1 lambda max (agris record): bears on records 6 and the Opisthocomus cells.
- Haarlem et al. 2026, Healy et al. 2013: bear on every cff_hz record (2, 4, 5, 7, 14).
- Tyrrell and Fernandez-Juricic 2017 S1 Table, Martin 2007: bear on record 15, 10 and the Opisthocomus field cells.
- Peitsch et al. 1992 (Hymenoptera spectral inputs): bears on record 16.
- Nowinszky et al. 2022: Phigalia, Euproctis (no open spectral_range_nm cell today).
- Intensity and colour of artificial light at night affect insect attraction in a taxon-dependent manner: bears on record 17 only if it lists Neoconocephalus.
