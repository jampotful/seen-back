# Precision audit 23, 16 October 2026

Scope: 20 records that no earlier audit table, recheck file or retract row (nor any row of `docs/views/audit/ALL.jsonl`) had touched, then 18 follow-up records from the two files where errors turned up. Harvest-1 to harvest-11 had no untouched records left (harvest-4 to harvest-6 do not exist), and sweep-105 has no evidence file, so the recent draw is sweep-106:1 with sweep-104:1. Main draw by file: sweep-10 (3), external-2 (1), external-6 (1), external-7 (1), canon-2 (1), canon-7 (1), oa-5 (1), oa-7 (1), oa-8 (2), sweep-104 (1), sweep-106 (1), sweep-13 (1), sweep-27 (1), sweep-29 (1), sweep-38 (1), sweep-41 (1), sweep-53 (1). Taxa: insects 9, plants 5, birds 3, fish 2, mammals 1, reptiles 1. All twenty at `m` before the audit.

The spread leans to insects and plants because most mammal, reptile and fish sources on the candidate list could not be opened in this session (see Blocked pages), and the search budget ran out before open copies could be located. The blocked records were dropped before any check and replaced from hosts that answered.

Method as in audits 13 to 21: each source opened with WebFetch and asked first whether the exact quote string appears, then for the page's own sentence or row; metadata checked against the opened page. A change to the partial flag, the grade, the method or a bibliographic field counts as `correct`. A fragment that carries the value passes, and a degree sign or λ rendered differently by the fetch tool is treated as a rendering difference. Following audit 21 (sweep-63:8), lost diacritics in an author list count as a bibliographic error. Corrections are in `docs/views/recheck/recheck-23.jsonl` in the recheck-5 schema. No evidence file, no wanted file and not `docs/views/audit/ALL.jsonl` was edited.

## Table

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| sweep-106:1 | Lophura nycthemera / binocular_deg 39, 41 | m | confirm | Author copy of the published PDF: section 3(c) sentence read in pieces that match the logged quote; one male and one female silver pheasant; ophthalmoscopic reflex technique. Five authors, Biol Lett 21: 20250405 confirmed |
| sweep-104:1 | Hydrochoerus hydrochaeris / fovea | m | confirm | Cambridge abstract page: sentence verbatim. Retinae flat-mounted, Nissl-stained, cells counted on a matrix over the whole retina. Three authors with diacritic, 2(3):221-235 confirmed; purchase marked unavailable, so `partial: true` stands |
| external-2:3 | Hemicordulia tau / interommatidial_deg 0.9 | m | confirm | NSF PAR accepted manuscript, Table 1: row verbatim under the headings "BL (cm) Df (deg) Dr (deg) CPD Ref."; seven authors and article 101002 confirmed |
| external-7:2 | Lasioglossum noctivagum / interommatidial_deg 2.75 | m | confirm | Same table: "Halictidae Lasioglossum noctivagum apposition 0.43 2.75 5.50 0.18 42" verbatim |
| canon-7:1 | Mnais costalis / opsin_gene_count 15 | m | confirm | PMC4371951: sentence verbatim in the paragraph that opens "How and when have so many opsin genes emerged"; M. costalis was one of the ten species sequenced by RNA-seq |
| external-6:2 | Tharsalea rubidus / lambda_max_nm 437 | m | confirm | JEB article page: abstract prints "blue (B; λmax=437 nm and 500 nm, respectively)"; the logged "lambdamax" is a rendering difference. Four authors confirmed; the journal field lacks 209(16):3079-3090 |
| sweep-10:6 | Malva sylvestris / sense_light_nonvisual | m | confirm | MDPI: abstract opens "In the present study, the diaheliotropic leaf movement pattern … is presented", so the quote is verbatim. Three field plants, readings about every two hours from dawn to sunset, October 2004 to July 2005; 12(13):2484 confirmed |
| oa-7:750 | Dascyllus trimaculatus / receptor_classes 4 | m | confirm | Springer abstract: "have four classes of cone photoreceptors" verbatim, naming D. trimaculatus; ERG and microspectrophotometry. Five authors confirmed; journal field lacks 189(3):213-220 |
| oa-5:1039 | Carcharhinus plumbeus / cff_hz 19 | m | confirm | Springer abstract via doi.org: verbatim apart from "~9–12" printed with an en dash. The ~19 Hz belongs to spiny dogfish and is stated equal to the sandbar shark's, so the value for C. plumbeus is read through that equality; sandbar experiments at 25 °C as the conditions say. 200(12):997-1013 |
| oa-8:112 | Pituophis m. melanoleucus / lambda_max_nm 481 | m | confirm | bioRxiv PDF: "Pine snake rhodopsin has a λmax of 481nm (Fig 2B)"; one adult, HEK293T expression, regenerated with 11-cis retinal. Five authors as printed ("Benedict Darren") |
| sweep-10:5 | Opuntia ficus-indica / diel | m | confirm | Springer abstract: "by opening their stomata during the cool, desert nights and closing them during the hot, dry days" verbatim, in the sentence naming O. ficus-indica. Sole author Lee JS, review, 53(1):19-23 |
| sweep-10:10 | Datura wrightii / diel | m | confirm | Springer abstract: "Datura flowers open at dusk and wilt by the following noon" verbatim. 91(7):329-333. The page did not say whether the measurements were made in the field |
| sweep-27:3 | Albizia julibrissin / diel | m | confirm | Springer abstract opens "The rapid nyctinastic movements of Albizzia julibrissin pinnules are under the control of phytochrome"; closure in the dark and reopening both described. "Greenhouse-grown" could not be checked on the abstract page |
| oa-8:52 | Halyomorpha halys / lambda_max_nm 519 | m | correct | Springer PDF: abstract sentence verbatim, ending "with sensitivity maxima at 519 nm and 367 nm, respectively."; ERG on chromatic-adapted eyes. Authors printed "Ádám Egri, Ádám Mészáros, György Kriska, József Fail"; the record had dropped the diacritics (Meszaros). Restored |
| sweep-13:14 | Vanellus armatus / binocular_deg 19 | m | correct | Author PDF: printed "with a maximum width of approximately 19° (Fig. 2b) and vertical extent of 76° (Fig. 2c)."; the logged "about 19 degrees, vertical extent of 76 degrees" is a summariser's paraphrase. Requoted. The empty DOI is now the printed 10.1111/ibi.12725. Three captive birds at Birdworld confirmed |
| sweep-38:11 | Hieraaetus pennatus / receptor_classes 4 | m | confirm | Springer abstract: sentence verbatim in two pieces; light and electron microscopy. Three authors, 137:177-190 |
| sweep-41:7 | Nepeta nuda / sense_light_nonvisual | m | confirm | MDPI: abstract sentence verbatim, and the join the logger could not confirm is now confirmed. Authors are honestly marked "et al" (the page shows ten names and an ellipsis before the last, Vassileva). 14(15):2285 |
| canon-2:115 | Xylocopa tranquebarica / absolute_sensitivity | m | confirm | JEB article page, section "Activity periods": "a bee capable of foraging even on the darkest moonless nights when light levels can be as low as 10–5 cd m–2". A review citing three field studies; 211(11):1737-1746 |
| sweep-29:1 | Gryllus bimaculatus / lambda_max_nm 332 | m | confirm | Springer abstract: fragment verbatim after "Three spectral types … were found with"; spectral scanning and flash methods. Journal field lacks the issue (5) |
| sweep-53:1 | Popa spurca / lambda_max_nm | m | confirm | Springer: Results sentence verbatim as far as the tool would quote, with the rest paraphrased to match; adult females; 350-650 nm; 530 nm adaptation among three used. 212(1):79-85, online 8 November 2025 |

**Rate: 2 errors in 20 records, 10%** (none unverifiable). By verdict: 2 correct, 0 requote, 0 retract; 18 confirm.

### Follow-up draw (errors found, so more from the same files)

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| oa-8:53 | Halyomorpha halys / lambda_max_nm 367 | m | correct | Same sentence as oa-8:52; the 367 nm maximum is the one revealed under green adaptation, as the conditions say. Author diacritics restored |
| oa-8:54 | Halyomorpha halys / receptor_classes 2 | m | correct | Same sentence. Author diacritics restored |
| oa-8:55 | Halyomorpha halys / lambda_max_nm 523 | m | correct | "The peak wavelength of each fitted pigment template was" λdark G = 523 nm and λdark UV = 371 nm; 45 min dark adaptation, 8 females and 8 males (Fig. 4 caption). Author diacritics restored |
| oa-8:56 | Halyomorpha halys / lambda_max_nm 371 | m | correct | As oa-8:55 |
| oa-8:57 | Halyomorpha halys / behaviour_vision | m | correct | "all wavelengths elicited a significant positive phototactic reaction, except for the 743 nm infrared light" verbatim; 14 LEDs, 368-743 nm; at least 90 min dark adaptation. Author diacritics restored |
| oa-8:58 | Halyomorpha halys / behaviour_vision | m | correct | "The highest number of flight attempts was registered for 455 nm" verbatim. Author diacritics restored |
| oa-8:113 | Pituophis m. melanoleucus / lambda_max_nm 370 | m | confirm | bioRxiv PDF: "…SWS1 pigment absorbs in the UV range with a λmax of 370nm." The figure reference (Fig 2C) is in the sentence before |
| oa-8:114 | Pituophis m. melanoleucus / lambda_max_nm 534 | m | confirm | "Fit to A1 templates gave a λmax of 534nm."; the fragment carries the value. All three pigments regenerated with 11-cis retinal |
| oa-8:115 | Pituophis m. melanoleucus / receptor_classes 3 | m | confirm | Abstract sentence verbatim |
| sweep-13:15 | Vanellus armatus / fov_h_deg | m | correct | Printed "results in this species having a cyclopean field of 313° in the horizontal plane (Fig. 2b)."; the logged "about 313 degrees horizontally" was a paraphrase. Monocular 166° and blind area 53° at 40° confirmed. Requoted; DOI added as for sweep-13:14 |
| sweep-13:8 | Ardeidae / binocular_deg 20 | g | correct | Illinois State copy of Martin 2007: "In herons, the maximum width of the frontal binocular field is 20°" and the bittern sentence confirmed. Empty DOI now 10.1007/s10336-007-0213-6; pages S547-S562 added |
| sweep-13:9 | Scolopax rusticola / binocular_deg | m | correct | Same PDF: "with a maximum width of between 5° and 10° in the approximate horizontal plane", Woodcock and Mallard named as Type 2 examples. DOI and pages added as for sweep-13:8 |
| sweep-13:7 | Adiantum capillus-veneris / sense_light_nonvisual | m | requote | Nature abstract page: the logged sentence is absent and "mediates" occurs nowhere on the page. The abstract's "We identify here a function of phy3 for red-light-induced phototropism and for red-light-induced chloroplast photorelocation" carries the value. Requoted; eight authors and 421:287-290 confirmed |
| sweep-13:2 | Saponaria officinalis / diel | m | unverifiable | Thieme abstract page not reached (permission step not answered) |
| sweep-13:13 | Rhododendron maximum / sense_light_nonvisual | m | unverifiable | VTechWorks record not reached (permission step not answered) |
| sweep-13:6 | Rhamnus cathartica / sense_light_nonvisual | m | unverifiable | UMN Experts record not reached (permission step not answered) |
| sweep-13:1 | Lycorma delicatula / spectral_range_nm | m | unverifiable | Ewha repository record not reached (permission step not answered) |
| oa-8:82 | Bombus terrestris dalmatinus / photoreceptor_time_to_peak_ms | m | unverifiable | J Neurosci PDF not reached (permission step not answered) |

**Follow-up rate: 11 errors in 13 verifiable records, 85%** (5 unverifiable). Six of the eleven are the one author-list fault repeated across the Egri et al. 2024 rows of oa-8.

**Combined: 13 errors in 33 verifiable records, 39%** (5 unverifiable).

## Checks

- **Quotes.** The sweep-13 records read "through a summariser" carry paraphrases logged as quotes: the two Blacksmith Lapwing rows turn the printed degree signs and "approximately" into "about … degrees", and sweep-13:7 logs a sentence that is not on the Nature page at all. The remaining sweep-13 summariser rows (13:1, 13:2, 13:5, 13:6, 13:11, 13:12, 13:13) are likely to share this and should be reread when their pages open.
- **Metadata.** Three empty DOIs filled from the opened pages (sweep-13:8, 13:9 and 13:14 with 13:15 sharing one). The oa-8 Egri rows print Meszaros for Mészáros; the other three authors carry diacritics only in their given names, which the initials form drops anyway. Not counted: journal strings that omit an issue or pages (external-6:2, oa-7:750, oa-5:1039, sweep-29:1), sweep-10:10's "Van Haren" where the page prints "van Haren", and sweep-41:7's honestly labelled "et al".
- **Grade and partial flag.** No wrong grades or flags found. sweep-41:7 stays `partial: true`: the join its `where` doubted is now confirmed, but only the abstract was read.
- **Value through equality.** oa-5:1039 gives the sandbar shark 19 Hz because the abstract says the spiny dogfish's ~19 Hz is "equal to that of sandbar shark". This is right, but the quote's "their" refers to the dogfish; a note saying so would help a later reader.
- **Out of scope.** canon-3:11 and canon-3:12 cite a ResearchGate URL as their source. They were not opened, as the method forbids; the URL should be replaced by a permitted copy.

## Rows written

`recheck-23.jsonl`: 12 rows. `correct`: oa-8:52 to 8:58 (7), sweep-13:14, 13:15, 13:8, 13:9. `requote`: sweep-13:7.

## Blocked pages

Records whose pages could not be opened were dropped from the main draw before any check, and replaced.

- Permission step not answered: api.drum.lib.umd.edu bitstream a3cce236 (external-5:2); raw.githubusercontent.com elife-15675 XML (canon-7:41); elifesciences.org/articles/81050 (external-2:2); pmc.ncbi.nlm.nih.gov PMC9499225 (canon-8:18) and PMC3863422 (oa-5:176); journals.plos.org printable PDF and portal.research.lu.se for the hornet paper (sweep-10:3); bmcevolbiol.biomedcentral.com and bmcecolevol tables/1 (oa-8:116); openaccess.city.ac.uk eprint 21664 (oa-4:217); frontiersin.org fevo.2019.00352 (canon-2:40); hal.science hal-03132841 (oa-3:523); biorxiv 2026.03.10.710949 (oa-7:541) and 2026.06.05.730304 (oa-4:71); cob.silverchair.com JEB 220/14/2502 (canon-3:3); thieme-connect, vtechworks, experts.umn.edu, pure.ewha.ac.kr and jneurosci.org (follow-up rows above).
- Rate limited (HTTP 429): www.ebi.ac.uk supplementaryFiles for PMC11254976 (oa-2:3271) and PMC11968189 (oa-1:3632); doi.org for 10.1242/jeb.209031 (oa-3:6) and 10.9775/kvfd.2017.17976 (oa-5:302).
- Robots disallowed: europepmc.org (external-6:2 first route, oa-7:663); jstage.jst.go.jp (oa-5:244); link.springer.com tables page for 10.1186/s12862-017-1110-0.
- Browser check: pubmed.ncbi.nlm.nih.gov 16888057; pmc.ncbi.nlm.nih.gov PMC3134451 and PMC5725783.
- Fetch error: royalsocietypublishing.org rspb.2011.0118 (oa-7:663).
- Opened but not checkable: the JEB page for Potier et al. 2018 (oa-3:523) gives the turkey vulture binocular width only in Fig. 1 and Table 1, which are images; the Springer page for Hauzman et al. 2017 (oa-8:116) confirms "the primarily diurnal Chironius bicarinatus" in Methods but does not render Table 1, so the logged row could not be matched. journals.plos.org returned an unrelated article (van der Merwe et al. 2018) for 10.1371/journal.pone.0021892, as audit 21 found for another DOI.
- WebSearch budget for the turn was used up partway through.
