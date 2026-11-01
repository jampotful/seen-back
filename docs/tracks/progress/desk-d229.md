# desk-d229

Unit d229, 31 October 2026. Branch research/desk-d229. Evidence: docs/views/evidence/desk-d229.jsonl. Every species and DOI below was grepped across docs/views (evidence, audit, corrected, sheets, searched, gaps) on origin/main before filing. Each DOI was checked on api.crossref.org/works/<doi> and in the opened PLOS page.

## Records filed

| Species | Trait | Source (PLoS ONE) | Licence evidence |
|---|---|---|---|
| Anguilla marmorata (5 lines: rod 493 glass, 489 cultured yellow, 489 wild yellow; cone 508, 517) | lambda_max_nm | Wang et al. 2014, 9(8): e103953 | Crossref CC BY 4.0, content-version unspecified, plus page "Creative Commons Attribution License" |
| Careproctus rhodomelas (480 nm eyeball extract) | lambda_max_nm | Sakata et al. 2015, 10(8): e0135888 | Crossref CC BY 4.0 vor |
| Magallana gigas (10 to <1000 Hz valve response, best 10-200 Hz) | sense_hearing | Charifi et al. 2017, 12(10): e0185353 | Crossref CC BY 4.0 vor |
| Porichthys notatus (larval AEBR thresholds) | sense_hearing | Alderks and Sisneros 2013, 8(12): e82182 | Crossref CC BY 3.0 vor |
| Coregonus kiyi, Salvelinus namaycush (siscowet), Myoxocephalus thompsonii (ERG peak 525 nm each) | lambda_max_nm | Harrington et al. 2015, 10(2): e0116173 | Crossref CC BY 4.0 vor |
| Emblemasoma auditrix (hearing tuned to 5 kHz, both sexes) | sense_hearing | Lakes-Harlan et al. 2014, 9(1): e87211 | Crossref CC BY 4.0 vor |

Notes for the auditor:
- Anguilla marmorata: the abstract sentence is the only place the 508 and 517 nm cone values appear; the Results say a single cone class was seen only in cultured and wild yellow eels. The abstract's "yellow" is read as the cultured yellow eels (Methods and Results use "cultured yellow"). n = 9 glass, 4 cultured yellow and 2 wild yellow eels.
- Careproctus: family and order from the Fig 1A caption; fish number not stated; the 410 nm component (P414) is recorded in conditions.
- Magallana gigas: name used in the paper and on main's try-species list. Owner question below.
- Porichthys: abstract threshold range (140-150 dB) differs from the Results' 133-151 dB at best frequency; both are in conditions. Larval stage.
- Lake Superior fishes: family and order for the two non-salmonid and salmonid taxa come from main (Salmonidae/Salmoniformes) and GBIF backbone species/2333811 (Cottidae/Scorpaeniformes); the paper prints "thompsoni" and "Salvelinus namaycush siscowet" (logged at species level, morph named in eye field and note).

## Held leads and why

- Lumpfish (Cyclopterus lumpus) magnetic coil, PeerJ 11: e14745: page opened, abstract sentence reads whole only if no comma follows "on" (tool reported none), 40 words exactly; family and order not in the paper or on main; already listed as held in desk-d224. Not filed.
- Mysis relicta lake and sea (PLoS ONE 9: e88107): 554 and 529 nm are cited from earlier microspectrophotometry, the paper's own measurement is HPLC chromophore identity. Not filed.
- Principapillatus hitoyensis and other taxa in PeerJ 5: e3595 (Lessios): model-fitted peaks from earlier ERG data; held as a reanalysis.
- Walleye (Sander vitreus) scotopic sensitivity, PeerJ peerj.21156: page failed to open three times (client_error). Held.
- Podarcis muralis acuity (JEB 10.1242/jeb.249422 per an aggregator page): publisher page denied (permission prompt), no licence seen. Held.
- Miniopterus fuliginosus ABR: JASA, no open licence seen. Held.
- Exorista japonica (PLoS ONE e0160441): lambda_max already on main from a review (audit methods:763-764). Not used.
- Siganus guttatus hearing, Dasypus, Betta splendens, Trichopsis, Sminthopsis, Tursiops electroreception, Chelonia colour: already on main.
- Emblemasoma and tettigoniid cercal paper (PLoS ONE e0012698): the latter not opened (PLOS rate limit); still a lead.
- Meriones unguiculatus ERG (e0147318): laboratory rodents, domestic stock. Not used.

## Owner questions

1. Magallana gigas valve closure to tones: sense_hearing or sense_vibration (the oyster has no pressure receptor; the paper itself calls it hearing and measures shell acceleration)?
2. Salvelinus namaycush siscowet: keep at species level, or treat a named morph as pooled?
3. Anguilla marmorata: should the glass-eel and yellow-eel rod values be kept as three lines from one sentence, or merged?

## Search budget

About 35 WebSearches. Crossref list queries returned mostly human audiology; PLOS fetches were rate-limited repeatedly.

## Desk disposition after audits 321 and 322

Lines 7 and 8 (Magallana gigas, Porichthys notatus) repeat the d228 records already on main (DOIs 10.1371/journal.pone.0185353 and 10.1371/journal.pone.0082182) and were dropped without audit. Audit 321 (lines 1-6): all six in error, fixable. Audit 322 (lines 9-12): all four in error, fixable; siscowet lake trout accepted at species rank (trinomial is a synonym). Replacement text applied; 10 records merged, check.py 0 problems. Careproctus rhodomelas order set to Perciformes (FishBase, OBIS, main). Anguilla cone values 508 and 517 nm are logged from the abstract because the Table 1 cells did not render. Open owner question: Myoxocephalus thompsonii family/order from GBIF only (some classifications use Psychrolutidae); Emblemasoma female curve is carried from a 1999 paper.
