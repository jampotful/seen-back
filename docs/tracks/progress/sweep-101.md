# sweep-101 (Round 3 genus sweep, batch sweep-2)

Reached genus index 39 of 39 (all 40 genera, Eudynamys to Lithosia). Two searches per genus (about 80 WebSearch calls), plus page fetches of candidate papers.

Records
- Evidence log: 2 lines. Linepithema humile interommatidial_deg 15.3 deg (m, Clifton et al 2020, full text open; the authors compute it from facet count). Thalassarche fov_h_deg 270 deg (g, pooled grey-headed and black-browed albatrosses, Martin 1998, abstract only, partial).
- Search records: 40, one per genus, in docs/views/searched/sweep-101.jsonl. Every `chased` names an opened paper's DOI or the "none" string. Where the batch's closest record sits in a log that is not on this branch (Damaliscus, Axis, Hystrix), the chased paper is a different opened work on the nearest group, and the line says so.
- Wanted: 1 line (Martin 1998 full text, to split the pooled albatross values).

Cells closed by a measurement: Linepithema interommatidial_deg (m); Thalassarche fov_h_deg (g). Everything else stays open and is recorded as searched with nothing found at genus level.

Not logged on purpose
- Machovsky Capuska et al 2011 (SWS1 of seabirds, Caspian and white-fronted terns violet-type): landing pages gave no DOI, so no line. A DOI would let it support the Sternidae pigment cells (opsin-inferred, g).
- Grosser et al 2023 (kea RH2 gene intact): an intact-gene result, no peak wavelength or range.
- Martin 1998 binocular width 26 to 32 deg: only a sentence fragment could be quoted.

Notes for the next sweep
- Publisher PDFs on cob.silverchair.com opened through WebFetch; curl and PMC were refused. Many insect genera of the batch (Lepidoptera, Hemiptera, Odonata) have no species-level eye work; family-level Table 1 of Feller et al 2021 names none of them.
- Chatterjee et al 2020 (flicker, Lepidoptera) full text is the one compilation that might name Indian or European moth genera of this batch (for example Tirumala); the abstract page does not list species.
