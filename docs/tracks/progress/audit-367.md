# audit-367: desk-d275, evidence line 1

Audited 1 November 2026 from the desk-d275 files present untracked in the worktree (docs/tracks/progress/desk-d275.md and docs/views/evidence/desk-d275.jsonl, 1 line; neither committed here, neither edited). Worktree HEAD and origin/main 83288436 (d272 merged after audit 365). `python3 -I tools/senses/check.py | grep 'd275\.'`: "docs/views/evidence/desk-d275.jsonl: 1 records, 0 problems". Quote length (`len(q.split())`): 22. No non-ASCII in quote or value. Format model audit-358.md; desk-audit.md evidence clause (40-word limit; no 125-character limit).

Sources opened (WebFetch): academic.oup.com/jinsectscience/article/18/3/16/5035339 (four passes); api.crossref.org/v1/works/10.1093/jisesa/iey029; names: www.fws.gov/taxonomic-tree/3437496 (ITIS lineage), zenodo.org/record/8407567 (Plazi treatment), hoppers.speciesfile.org/otus/12713 (genus page), bellatlas.umn.edu taxon 832398, and two catalogueoflife.org pages that turned out to be other Okanagana names (4928T O. hesperia, 8J9Q7 O. tristis rubrobasalis; not used). Not opened: GBIF, the core.ac.uk and jlupub.ub.uni-giessen.de repository copies, Wikipedia and its mirrors. No curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 9 WebSearches.

## Bibliographic and licence

Crossref: Joscha A Alt, Reinhard Lakes-Harlan, in that order; title "Sensing of Substrate Vibrations in the Adult Cicada Okanagana rimosa (Hemiptera: Cicadidae)", identical to the record; Journal of Insect Science, volume 18, issue 3, no article number in the record; issued and published-print 2018-05-01, published-online 2018-06-09; one licence entry only, "http://creativecommons.org/licenses/by-nc/4.0/", content-version vor, delay 39 days, start 2018-06-09; relation empty; no update-to (no correction or retraction). Page (tool summary): byline Joscha A. Alt and Reinhard Lakes-Harlan; "Volume 18, Issue 3, May 2018, Article 16"; copyright line "© The Author(s) 2018. Published by Oxford University Press on behalf of Entomological Society of America."; no licence sentence in the body; the permissions link names CC BY-NC (no conflicting tag). Licence accepted under the rules (publisher page without a licence sentence plus Crossref CC licence for vor; CC BY-NC accepted). Printed year 2018 agrees with Crossref. "Journal of Insect Science 18(3): 16" and access "open" right. Faults 0.

## Names

Okanagana rimosa is absent from docs/views/gaps/gbif-names.tsv. The record rests family and order on the GBIF Backbone page (refused for fetching) and says the page states no status. Independent sources:
- Cole, Chatfield-Taylor, Smeds, Cooley, Gonzalez and Wong 2023, Zootaxa 5346(5): 501-531, "Phylogeny of North America's largest cicada radiation redefines Tibicinoides and Okanagana", treatment of Okanagana Distant 1905 (Plazi, zenodo 8407567; record details tool summary). Verbatim lines: "Type Species: Cicada rimosa Say, 1830"; "rimosa rimosa (Say, 1830), rimosa ohioensis Davis, 1942". Family Cicadidae (subfamily Tibicininae in the citation, tool summary). The species is included as valid in the current revision of the genus (type species), with two subspecies.
- ITIS via the US FWS taxonomic tree: Okanagana rimosa, rank Species, TSN 847181, lineage "Order Hemiptera > Suborder Auchenorrhyncha > ... Superfamily Cicadoidea > Subfamily Tibicininae > Tribe Tibicinini > Genus Okanagana" with 2 subspecies (tool summary; no status word and no family rank printed).
- Hopper species file genus page: Okanagana Distant, 1905 under Tibicinini, Tibicininae, Cicadidae, Hemiptera (tool summary).

Okanagana rimosa (Say, 1830), Cicadidae, Hemiptera is right and is the name in current use; no synonym is filed. The paper does not name a subspecies for the Pellston animals; filing at species rank is not pooling. Fault: the note's name sourcing (GBIF page, status not stated) should name these checklists; counted with the record's error below.

## Duplicates

git grep on origin/main (83288436) across the whole docs/ tree (evidence, audit/ALL, audit/corrected, sheets, searched, gaps, progress) for Okanagana, iey029, jisesa/iey and Lakes-Harlan: Okanagana rimosa appears only as the host in desk-d229 line 10 (Emblemasoma auditrix, sense_hearing) and in audit-322.md's check of that line; Lakes-Harlan only for other papers (2014 E. auditrix, 2015 RSOS bushcricket in desk-d173). Branch-only additions of all 163 origin/research/desk-d2* and audit-3* branches: Okanagana or iey029 only in research/desk-d275 itself, research/desk-d229 and research/audit-322 (the same host mention). No audit-3*.md hold-out names this species or DOI. Duplicates 0.

## Trait key and grading

sense_vibration is a main key. Units "m/s2" follow main (Apis mellifera behavioural thresholds "0.25 m/s2 pp at 500 Hz", units "m/s2"; Monochamus alternatus "m/s2 (acceleration)"; Pagurus bernhardus "m/s2 RMS (vertical axis)"). Neural thresholds are already filed under sense_vibration at grade m: Eurycea lucifuga and Gyrinophilus porphyriticus "best seismic sensitivity" by "masked auditory brainstem response to substrate vibration", units "dB re 1 m s-2". A whole-nerve extracellular threshold is a measured physiological threshold, not a modelled one, so grade m without a model disclosure is right. The paper states the leg nerve carries the axons of both the femoral chordotonal organ (about 20 cells) and the subgenual organ (two cells) (tool summary), so the threshold is the pooled nerve response, not a single organ's; the method should say so (uncounted). Grading 0 faults.

## Per-record finding

### Line 1, Okanagana rimosa, threshold in the range of 1 m/s2, minimum at 1,000 Hz

Quote, Results (neurophysiology), verbatim in two abutting pieces in one response: "Thresholds to stimuli with different carrier frequencies are in the range of 1 ms2 with a minimum at 1,000 Hz" | " ([Fig. 3B](javascript:;))." (link markup is the page's). Sentence before: "For threshold analyses, the responses were analyzed as all-or-nothing response."; sentence after: "The overall threshold is broadly tuned to vibrations from 200 to 5,000 Hz ([Fig. 3B](javascript:;))." **Quote MATCH**, 22 words, whole sentence with its figure reference, one section; "ms2" as printed. Value says no more than the quote; the 'ms2' to m/s2 reading is disclosed and the Abstract confirms the unit: "Recordings from the leg nerve show that the vibrational response is broadly tuned with a threshold of about 1 m/s2" | " and a minimum latency of about 6 ms." The text prints no per-frequency threshold numbers; values exist only in Fig. 3B.

Verified, verbatim: "Adult females of the protoperiodical cicada O. rimosa were caught in the open aspen forest around the Biological Station of the University of Michigan, Pellston, MI, in July 2013 and June 2017."; "The vibrational response of midlegs was determined by recording extracellularly from the leg nerve."; "The leg nerve was placed on a tungsten hook electrode (WPI, Sarasota, FL, Type TM33B05)."; tibia "attached with superglue to a lever" at "about 70°"; "minishaker (Brüel and Kjær, Odense, Denmark, Type 4810)"; "Stimuli had carrier frequencies from 200 to 8,000 Hz."; "The duration of the stimuli was 100 ms and the repetition rate was 2/s."; "Each stimulus was given four times before the amplitude was increased by 6 dB"; threshold "the lowest stimulus intensity at which the nerve responded to at least three out of the four stimuli per frequency–amplitude presentations"; "Responses from 13 animals were analyzed."; animals "used within 2 or 3 d for the experiments". No recording temperature is stated (the 4-7 C figure belongs to the tracing; tool summary). Only substrate vibration was presented; no airborne sound (tool summary). Only females; no males tested.

Faults:
- Omitted null result from the Abstract: "The vibratory sense of cicadas might be used in predator avoidance and intraspecific communication," | " although no tuning to the peak frequency of the calling song (9 kHz) could be found." The Discussion adds "This wide range and lack of high-frequency tuning indicates no tuning to species specific signals." and "with a decrease of sensitivity at higher frequency." The record's conditions carry the broad 200 to 5,000 Hz tuning but not the absence of tuning at the song peak.
- Statistic not described: Fig. 3 legend, verbatim: "Data represent mean and SEM from 13 animals." The threshold curve and its 1,000 Hz minimum are of the mean across animals; the record says only "responses from 13 animals analysed" and does not say the values are means, nor that the text gives no per-frequency n or numbers.
- Name sourcing (see Names): the note rests on a GBIF page with no status.

Uncounted: collection dates (July 2013 and June 2017) and holding (cages with fresh aspen or acer branches, used within 2 or 3 d); recording temperature not stated; tibia-femur angle about 70°; the leg nerve carries both feCO and SGO axons; substrate vibration only. The latency remark is right (Fig. 3C latencies "from five animals each (mean and SEM)").

**Line 1 error (calling-song null omitted; threshold curve is a mean of 13 animals, not said; name source lacks status).** Fixable.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Okanagana rimosa, threshold in the range of 1 m/s2, minimum at 1,000 Hz | error, fixable | conditions, note | quote MATCH (22); no tuning at the 9 kHz song peak omitted; mean and SEM of 13 animals not said; name sourced to GBIF without status |

Errors 1 of 1 audited record (100%), above the 5% bar; none held out. By kind: omitted null result 1; statistic undescribed 1 (same record); name sourcing 1 (same record); bibliographic 0; licence 0; duplicates 0 against main, 163 desk-d2* and audit-3* branches and audit-3* hold-outs; trait key and grading 0.

Unchecked: the Fig. 3B threshold values themselves (figure not read; no numbers in text); whether all 13 animals were tested at every frequency; the full Fig. 3 legend (over 900 characters; tool summary apart from the mean-and-SEM sentence); the subspecies of the Pellston population; an explicit "accepted" status word in a checklist (Cole et al. 2023 include the species as valid; ITIS page via FWS prints no status); the page's permissions-link licence text (tool summary only).

## Replacement text

Each old string occurs exactly once in its field (checked with `str.count` on the desk file).

Line 1, counted:
- `conditions`: "responses from 13 animals analysed;" -> "responses from 13 animals analysed; the threshold curve (Fig. 3B) is the mean and SEM of the 13 animals, and the text gives no per-frequency threshold numbers or per-frequency n;"
- `conditions`: "no sex comparison (females only)" -> "no sex comparison (females only); the Abstract adds that no tuning to the peak frequency of the calling song (9 kHz) could be found, and the Discussion reports a decrease of sensitivity at higher frequency"
- `note`: "Family and order from GBIF Backbone Taxonomy page for Okanagana rimosa (Say, 1830) (gbif.org/species/8277348; status not stated on page) and the paper title." -> "Name Okanagana rimosa (Say, 1830), Cicadidae, Hemiptera: included as a valid species (type species of Okanagana, subspecies rimosa rimosa and rimosa ohioensis) in the Okanagana treatment of Cole et al. 2023, Zootaxa 5346(5): 501-531 (Plazi); ITIS TSN 847181 places it in Hemiptera, Cicadoidea, Tibicininae; the paper names no subspecies (audit 367)."

Line 1, uncounted:
- `method`: "from the midleg leg nerve of restrained females" -> "from the midleg main leg nerve (carrying the femoral chordotonal and subgenual organ axons) of restrained females"
- `conditions`: "adult females caught in open aspen forest around the Biological Station of the University of Michigan (Pellston, MI);" -> "adult females caught in open aspen forest around the Biological Station of the University of Michigan (Pellston, MI) in July 2013 and June 2017, kept in cages with fresh aspen or acer branches and used within 2 or 3 d; recording temperature not stated; substrate vibration only (no airborne sound);"
