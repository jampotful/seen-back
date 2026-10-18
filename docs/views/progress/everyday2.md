# Progress: everyday2 (the dog and the home share's weight)

Task: the two weak spots left by build 34 (`tools/species/EVERYDAY.md`, "Where it is weak"), within the marks of `docs/tracks/prompts/burst13-everyday.md`. Branch: `agent/everyday2`. Clone: `/home/claude/wt-everyday2`. Started 18 October 2026 at 20:35 UTC; time limit 150 minutes.

## Done

- Cloned `main` at build 34 (`45358a6`) and opened the branch.
- The cause of the dog, read locally from the shipped files and the photo vectors of `runs/everyday/4-build`: GBIF lists `Canis familiaris` as a synonym, so build 34 gave the dog a new row of that name and put its home share there. The world row `Canis lupus` (English name Domestic Dog) matches dog photos better in BioCLIP 2 and got no home share. The dog's probability splits between the two rows, the cat's single row (wild records and a home share) takes the rest, and the kinds head says `other` for most dog photos. Moving the home share to `Canis lupus` gave the kind right on 19 of 20 dog test photos in a local check; a larger beta alone left it at 9 of 20.
- `tools/species/everyday_build.py` measures two rules (`own`, as build 34, and `accepted`, where a synonym takes the world row of GBIF's accepted species when that row has the same English name) over betas up to 3,000, with the world test at every beta, and stages the files for `--rule`. The softmax is exact, with the rows without a home share summed once a photo.
- `run/everyday/pocket-2`: the pocket model's kinds by species, and the dog's and cat's photos one by one.

## Next

- `run/everyday/again-pub-1` on a build machine (the photo vectors of run 4, no new embedding), then the manifest, the checks, `BUILD`, `EVERYDAY.md`, `docs/LOG.md` and the merge if every mark passes.
