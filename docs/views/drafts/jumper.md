# Sensing sheet: jumping spiders (family Salticidae), draft

Started 12 October 2026, 20:15 EDT; round 3 research under way from 12 October 2026, 21:44 EDT (this note will be replaced by the full sheet), from the literature gathered tonight (the collection on `pub/lit-t1`, topics `spider-day` and `spider-general`), read on disk. The evidence log is `docs/views/evidence/jumper.jsonl`; every row below names the log lines behind it. Papers from the owner's university library were not yet read when this draft stopped, so the acuity, receptor-tiering and spectral rows still lean on reviews.

## 1. Scope

Family Salticidae holds 23.4% of world spider records and 23.8% of Alachua's (earlier sheet `docs/views/sheets/spider.md`, GBIF facets of 11 October 2026). Alachua's most recorded jumping spiders include the Twin-flagged Jumping Spider (*Anasaitis canosa*, 284 records) and the Regal Jumping Spider (*Phidippus regius*, 109).

**Where the view should split.** One view can carry the family's shared architecture (eight eyes in four pairs with divided tasks), and colour must differ by species: most measured species have ultraviolet and green receptors only, *Saitis barbipes* among them (Glenszczyk et al. 2021), while *Habronattus pyrrithrix* adds a red-filtered class and sees red (Zurek et al. 2015, as summarized by Glenszczyk et al. 2021). Gawel et al. 2023 state the same variation for the family. Recommendation: one `jumper` view with a colour setting chosen per genus where measured (dichromat by default, trichromat for *Habronattus* and any other genus shown to see red), applied when the full database names the species.

**On "split views."** The evidence describes a modular system whose parts hand work to one another, and none of it describes a divided picture. Six eyes register motion and the two principal eyes are moved to inspect what they find (De Agrò, Rößler and Shamble 2024). The front side eyes (ALEs) pick out the coherent motion of living things, while the rear side eyes (PLEs) answer to any movement (same paper). After the principal eyes take a target, the ALEs withdraw attention from that place for about 5 seconds and watch elsewhere (Ferrante et al. 2024). The principal eyes' scanning changes with the kind of motion the side eyes report, which suggests motion and form processing interact (De Agrò et al. 2025, preprint). In the brain, the principal and secondary eyes feed separate first stages (arcuate body and mushroom body pathways), and one second-order neuropil may join the secondary eyes' inputs (Steinhoff et al. 2020). What a spider experiences cannot be measured; what can be drawn truthfully is one continuous picture whose parts differ in detail, colour and what draws attention, with attention moving between them. The picture to aim for is a wide field in which motion keeps calling for the narrow, detailed gaze.

## 2. The view `jumper`

### Rows (draft)

- `['m', 'Eight eyes, one picture', 'Six of a jumping spider's eyes watch for movement all around it, and two large front eyes swing toward whatever they report to look closely.']` Log: De Agrò et al. 2024 (eye_role AME; fov PLE).
- `['m', 'Living things stand out', 'The front side eyes pick out the jointed, rhythmic movement of living things, and the rear side eyes answer to anything that moves.']` Log: De Agrò et al. 2024 (ALE, PLE).
- `['m', 'Looking away on purpose', 'Once the front eyes lock on, the side eyes ignore that spot for about five seconds so that something new can catch them.']` Log: Ferrante et al. 2024.
- `['m', 'Colour', 'Most jumping spiders see ultraviolet and green. Some, like Habronattus, also see red through a filter in the eye.']` Log: Glenszczyk et al. 2021; Gawel et al. 2023. (Grade `g` for species not measured.)
- `['g', 'Flicker', 'Jumping spiders have been reported to follow flicker up to about 40 a second, a little slower than you.']` Log: Tan et al. 2023 citing Clark and Uetz 1990 (to be confirmed in the original).
- `['m', 'Fast stripes vanish', 'Thin stripes moving fast blur into grey for a jumping spider, so some prey hide by running.']` Log: Tan et al. 2026.
- `['m', 'Sleep', 'At night a resting jumping spider's retinas twitch in bouts, much like the eye movements of a person dreaming.']` Log: Rößler et al. 2022.
- Rows on sharpness, field, depth, hearing and ultraviolet carry over from the earlier sheet's checked `jumper` section until batch 1 is read.
- `x` row: hearing of low airborne sound through leg hairs (earlier sheet, Shamble et al. 2016), and chemical cues on the ground (Humbel et al. 2024; to log).

### The picture (proposal)

One continuous frame, no split screen:

1. **The surround (secondary eyes).** Nearly the whole circle, compressed into the screen (PLE responses to ±180°, ALE span about 100°). Drawn coarse and monochrome green (side eyes have green receptors only, per the earlier sheet's sources), with high temporal response. Anything moving glows; in the front 100° (the ALE zone) the jointed motion of living things glows brighter than random flicker, and behind it any motion glows alike.
2. **The gaze (principal eyes).** A narrow upright strip, about 5° wide per eye, sharp and in the species' colours (ultraviolet and green by default; red added for *Habronattus*), that jumps to the brightest glow, scans it with small sweeps, then holds. While it holds, the surround's glow at that place fades for five seconds and other movements win attention.
3. **Ultraviolet.** The phone does not record it well; an invented ultraviolet channel (from the blue channel and surface cues) is drawn as a false colour and said so in an `i` row.
4. **Night.** When the phone lies still in the dark, the gaze strip twitches in bouts (the sleep-like retinal movements).

New engine work: an upright sharp strip that moves (a saccade controller driven by a motion-salience map), per-zone colour (strip coloured, surround monochrome), per-zone motion gating, a "biological motion" detector (local coherent motion, approximated by optical-flow coherence), and inhibition of return (a decaying mask at the last gaze position). All are shader and small-state work on the camera image; none needs new permissions.

## 3. Open items

- Read batch 1 (Harland et al. 2012; Blest et al. 1981; Yamashita and Tateda 1976; Williams and McIntyre 1980; Taylor et al. 2015 and 2014) and log acuity, tiering, spectral classes and field figures from primary sources.
- Confirm the 40 Hz flicker figure in Clark and Uetz 1990.
- Species colour table: which genera are dichromats, which trichromats, which unmeasured.
- Powell, Stalcup and Taylor 2026 (Behavioral Ecology, doi 10.1093/beheco/arag110): colour vision and foraging success.
