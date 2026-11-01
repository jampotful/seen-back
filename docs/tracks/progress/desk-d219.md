# desk-d219

Task: new animal sensory-trait evidence records (open or abstract sources), filed to docs/views/evidence/desk-d219.jsonl. Plant screening of the unit brief was set aside.

## Filed (5 records, check.py 0 problems for desk-d219)
- Odocoileus virginianus, behaviour_vision, Cohen et al. 2014, Wildlife Society Bulletin 38(3): 480-485 (10.1002/wsb.438). Abstract only (DOAJ record and a library catalogue record), no licence stated, flagged partial. Quote: UV sensitivity sentence.
- Lymantria xylina, behaviour_vision x2, Zhang et al. 2025, Insects 16: 338 (10.3390/insects16040338), CC BY 3.0 on the MDPI page. Lamp catch (363 nm lamp best for males) and indoor female phototaxis (14.6%, 0.6%).
- Culex tarsalis and Culex quinquefasciatus, sense_thermal, Reinhold et al. 2022, Insects 13(1): 92 (10.3390/insects13010092), CC BY 3.0 on the MDPI page. Heat-seeking contingent on CO2; one shared sentence names both species, so each record says so. Culex territans from the same paper was already on main.

## Method notes
- Built a species/trait/DOI index from origin/main plus origin/research/desk-d214 to d218 and checked every candidate against it (and against docs/tracks progress held-out lists) before opening it. Main is close to saturated for what open searches return: Trachemys hearing, Salamandra, Encarsia, Eretmochelys, Vespa/Vespula, Pogona, Sepia, Dicentrarchus, Tursiops, Phoca, Daubenton's bat and Culex territans were all already filed.
- WebFetch only opens URLs that already appeared in a tool result, and it returns only sentences of about 120 characters or fewer verbatim, so quotes are short whole sentences.

## Hosts that did not open (permission unanswered or denied)
journals.biologists.com (jeb166074 cuttlefish infrasound, Wilson et al. 2018; Crossref licence is the Biologists user licence 1.1), pubs.aip.org (Furuyama et al. 2018, Miniopterus fuliginosus ABR, CC BY 4.0 per Crossref, absent from main), nature.com (Sci Rep 2024 personal electric deterrents vs shark bites, 10.1038/s41598-024-66679-6, absent from main), frontiersin.org, link.springer.com (Nityananda 2015 Sphodromantis contrast sensitivity), core.ac.uk/works pages, afdpz.org PDF (denied as walled copy; not retried).

## Held out
- Crowell 2015 diving-bird ABR (no licence; already held in d162). Crotalus polystictus thermal reception (PeerJ preprint only). Greiner 2005 thesis (Apoica pallens, thesis). Paraglenea fortunei (d147 held). Tiger puffer, carp and catfish strobe (aquaculture or domestic/held lists). Johnston and Mitchell 2021 Diversity (kiwi, moa; anatomy, no trait key fits). Dryophytes japonicus colour change (not a sense trait).

## Leads for a reader with access
- Furuyama et al. 2018 JASA 144(5) EL436 (Miniopterus fuliginosus audiogram, best sensitivity 44 to 56 kHz per the Crossref abstract summary).
- Wilson et al. 2018 JEB 221(1) jeb166074 (Sepia, escape and colour-change thresholds at 3, 5 and 9 Hz).
- Zhang et al. 2025 Lymantria xylina Table 1 maps the L-labels to peak wavelengths; the other four lamps could be filed from it.

## Owner questions
- Is a lab-colony wild species (Culex JHB and YOLO strains) acceptable, or should colonies count as domestic? Filed as acceptable.
- Should the Odocoileus abstract-only record stay when the page shows only a copyright line and no open licence?

## Desk disposition after audit 305

Audit 305 (all 5 records): 5 of 5 in error (100%), 7 faults. Line 1 (Odocoileus virginianus behaviour_vision, Cohen 2014) dropped as a repeat of docs/views/audit/corrected/squirrel-deer-rabbit.jsonl:100 (same DOI and sentence); the unit's duplicate index missed the corrected folder. Lines 2 to 5 corrected: both Lymantria xylina rows gained issue 4, the first its peak-emergence null (p = 0.101) and the second the per-test female counts and the 57.7% male rate; both Culex rows gained the CO2 dose result and the species contrast (Chisq 15.22). Four records merged. Pooled audits 172 to 305: 322 of 722 (44.6%).

Owner questions: lab-colony strains (Culex JHB and YOLO) accepted at species rank, matching main's handling of Long-Evans rats and laboratory moth colonies; abstract-only records from closed journals may carry source.access "abstract" with partial true (Odocoileus met it but repeated main); optional enrichment of corrected/squirrel-deer-rabbit.jsonl:100 conditions ("7 deer, light-adapted; automated forced-choice discrimination of lit from unlit monochromatic LEDs, intensity lowered to threshold, logistic function per deer; abstract only, wavelengths and intensities not given"); main files Reinhold et al.'s Cx. territans null from the same CO2-gated heat-seeking assay under sense_chemical (desk-d195.jsonl:6) while these two Culex rows sit under sense_thermal, so one assay now sits under two keys and the owner may want the pair aligned; main's only Lymantria xylina row is interommatidial_deg from Jiang et al. 2025 (recheck-2-fixed.jsonl:8); Lymantria xylina is not in gbif-names.tsv.
