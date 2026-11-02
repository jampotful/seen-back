# desk-d215 (animal sense-trait screen, open-licence papers)

About 19 WebSearches and 45 WebFetches. Crossref list queries (api.crossref.org/works?query=...&filter=prefix:...) were used for discovery, and Crossref per-DOI calls for authors, volume, licence and corrections. Main was grepped by species and DOI (all evidence, audit and corrected files) before each paper was opened.

## Queries (web and Crossref)
- Crossref lists: JEB hearing (2015+); JEB visual acuity (2010+); JEB electroreception/sensitivity (2008+); PeerJ hearing thresholds, ERG/spectral sensitivity, opsin/vision (2012+); PLOS ONE audiogram/ABR; MDPI compound-eye morphology and spectral sensitivity; Frontiers electro/magnetoreception/lateral line; an unfiltered interommatidial-angle query (useless, human-medicine hits). Generic topic words without a taxon return human or non-biological papers; PeerJ/PLOS/Frontiers lists mostly returned papers already on main (Maiditsch, Moffitt, Piniak, Pita).
- WebSearch: sea snake AEP, lungfish hearing, shark AEP, glass catfish magnetic, monarch caterpillar hearing, Podarcis muralis acuity (twice), sunfish acuity, fiddler crab OKR, tilapia spectral sensitivity, mole-rat circadian light, stingray electroreception, Bourke's parrot colour threshold, Gymnotus omarorum waveform, Gerhardt Fukomys.

## Records (8, docs/views/evidence/desk-d215.jsonl, all grade m)
1. Kryptopterus vitreolus, sense_magnetic: avoids static fields over 20 uT (Hunt et al. 2021 PLOS ONE, 10.1371/journal.pone.0248141, CC BY printed on the PLOS page). Sham-arm confound and no pre-magnet baseline stated in conditions.
2. Histia flabellicornis, interommatidial_deg 4.08 (Chen et al. 2025 Insects, 10.3390/insects16080771, CC BY). Calculated from SEM facet diameter and eye radius.
3. Lepomis gibbosus, acuity_cpd 3.6 (Spratte et al. 2021 JEB, 10.1242/jeb.243068). Five of six fish; the sixth fish (0.32 deg) is excluded from the quoted mean.
4. Hypanus sabinus (published as Dasyatis sabina), sense_electric: median best-response fields 0.006 uV/cm (brackish-saltwater) and 1.4 uV/cm (freshwater) (McGowan and Kajiura 2009 JEB, 10.1242/jeb.025247).
5. Oreochromis niloticus, lambda_max_nm: four sensitivity peaks in ranges 380-420, 440-480, 500-600, 600-680 nm (Lisney et al. 2010 JEB, 10.1242/jeb.036897). In-vitro eyecup ERG.
6. Neopsephotus bourkii, colour_vision: intensity threshold 0.4 cd/m2 (Lind and Kelber 2009 JEB, 10.1242/jeb.035477).
7. Melopsittacus undulatus, colour_vision: intensity threshold 0.1 cd/m2 (same paper, same Results sentence, which states both species).
8. Fukomys mechowii, sense_hearing: best sensitivity at 1 and 1.4 kHz, 33 dB SPL (Gerhardt et al. 2017 JEB, 10.1242/jeb.164426; Correction 10.1242/jeb.175190 opened once, it changes only the title). The held lead from d213/d214 is resolved for F. mechowii.
Quotes came through WebFetch page summaries (output capped near 125 characters), assembled from consecutive pieces; quotecheck was not run. JEB copies are the publisher's own free pages on cob.silverchair.com; for the 2009, 2010 and 2017 papers Crossref carries no open-licence entry (2017: biologists.com user licence, accepted manuscript) and the copies print only the publisher copyright.

## Held out
- Taylor and Yack 2019 Danaus plexippus caterpillar hearing (jeb211862): already on main (audit/corrected/insect.jsonl, Danaus plexippus sense_hearing 50 to 900 Hz, under 10.1242/jeb.217513). Repeat, not filed.
- Kawamoto et al. 2025 Podarcis muralis acuity (jeb249422), Perez et al. 2023 fiddler crab OKR (jeb245799), Hoppe et al. 2024 sunfish moving targets (bio.060455), Chanel et al. 2024 Cryptomys hottentotus pretoriae circadian light (jeb247793), Zhou et al. 2026 Scythris sinensis compound eye (insects17070702): no publisher full-text page reached (only repositories or aggregators without a licence, PMC refused, or the MDPI page returned PROVENANCE_REQUIRED, not retried). Not on main.
- Chapuis et al. 2019 sea snakes AEP (jeb198184): journals.biologists.com page refused (PROVENANCE_REQUIRED); Adelaide repository copy has no printed licence. Not on main for sea snake hearing.
- Dondi et al. 2016 PeerJ 4:e2217 (flash VEP in four raptor species, CC BY): clinical sedated pilot; no trait key fits (VEP latencies). Not filed.
- Liang et al. 2024 Asiophrida xanthospilota ERG/phototaxis (insects15070532): species already on main (desk-d203, polarization); the ERG colour-response and phototaxis sentences would need a trait key for lamp-spectrum comparisons (behaviour finding at ca. 100 lux, quanta not matched); not filed.
- Rodriguez-Cattaneo et al. 2017 Gymnotus omarorum (jeb153379): receptor physiology (capacitive-load waveform responses), no threshold; not filed.
- Newland 2008 cockroach (per brief), Pita et al. 2015 PeerJ (zebrafish and golden shiner vision) already on main.
- Mooney murre: not searched; Gelasimus dampieri and pit viper thermography: already on main (Gelasimus dampieri CFF and absolute sensitivity; Crotalus oreganus jeb.244478).

## Owner questions
1. Add to docs/views/gaps/gbif-names.tsv: Kryptopterus vitreolus (family Siluridae given from memory of Eschmeyer, please confirm), Histia flabellicornis (Zygaenidae), Lepomis gibbosus (Centrarchidae), Oreochromis niloticus (Cichlidae), Hypanus sabinus (Dasyatidae); none of the first four is in the table.
2. Parrot family: main files Melopsittacus under Psittaculidae while the GBIF taxonomy table puts neighbouring parrot genera under Psittacidae; Neopsephotus bourkii was filed as Psittaculidae. Which authority?
3. Two records (6 and 7) share one Results sentence that names both parrot species. Keep as two records, or one?
4. Can a reader open journals.biologists.com for Chapuis 2019 (sea snakes), Kawamoto 2025 (Podarcis acuity) and Perez 2023 (fiddler crab OKR) to confirm licence and quotes? Is the single-target-acuity 3.6 cycles/deg (authors' conversion of a dot threshold) acceptable under acuity_cpd?
5. The Gerhardt 2017 sentence covers three Fukomys species; only F. mechowii (accepted in the name table) was filed.

## Desk disposition after audit 300

Audit 300 (all 8 records): 2 of 8 in error (25.0%), line 1 (glass catfish: sham ran in Arm 1 after the magnet trials, same school, authors blame the order) and line 5 (tilapia: the 440-480 nm peak comes only from CAP OFF recordings, opponency caveat missing); both corrected with the auditor's replacement text. Pooled audits 172 to 300: 299 of 694 (43.1%).

Line 3 (Lepomis gibbosus 3.6 cycles/degree) was dropped: the value and paper are already cited on main in docs/views/sheets/fish.md and fish.audit.md:9, and the desk rule treats a finding carried on main as a repeat. Seven records merged with the uncounted fixes (Mann-Whitney frame counts, stingray group pooling, Gerhardt note provenance and sex wording).

Owner questions: add Kryptopterus vitreolus (Siluridae), Histia flabellicornis (Zygaenidae), Oreochromis niloticus (Cichlidae) and Hypanus sabinus (Dasyatidae, unchecked) to gbif-names.tsv; Lepomis gibbosus order differs between the record (Centrarchiformes) and main's try-species.json (Perciformes); parrot family: Psittaculidae kept for Melopsittacus and Neopsephotus, and the GBIF taxonomy table files parrots in the old broad Psittacidae, so main's Platycercus, Barnardius, Eclectus, Psittacula and one Melopsittacus row are inconsistent and could be aligned in one pass; whether sheet citations count as "on main" for the duplicate check (applied here: yes); Histia value already sits in searched/sweep-52.jsonl:24 (a search record, not an evidence row); lines 6 and 7 stay two records.
