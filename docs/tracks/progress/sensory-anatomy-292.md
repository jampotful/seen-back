# Sensory anatomy classification after audit 292

Work in progress on `codex/sensory-anatomy-292`, based on main `785f8504a8e78fb0e5caac6365ebc29e7dacb3bd` (31 October 2026).

Owner request: distinguish measured anatomy from demonstrated sensory function, inspect the actual presentation pipeline, preserve measurements and audit history, and implement through the repository review workflow.

Proposed rule: retain measured structures under `sensory_anatomy`, with explicit evidence-kind metadata. Organ presence, counts, passive mechanics and inferred function do not establish stimulus detection. Neural transduction and behavioural response remain separate evidence kinds. Taxonomic grade and source completeness remain independent axes.

Inspection: BRIEF, audit 292, desk-d208, the corrected bee, insect, spider, fish-shark and ground-invertebrate logs; gaps.py, rows.py, compile.py, views/PARAMS.md and existing view specs. The published records contain anatomy-only, mechanical, physiological and behavioural statements under the same functional trait keys. Some corrected copies retain unresolved audit flags; those are not treated as scientifically confirmed.

Next: implement validation and consumer guards, file the wasp counts as anatomy with explicit provenance, add regression coverage, and submit for research-desk review. Only the app thread merges into main (docs/HANDOFF.md); this branch does not change live views or release the audit hold by itself.
