"""Screening aid for the desk's search records (audits 40 to 42: a "none" record was written while a work in the harvest
output, or a record already on main, reported the measurement).

For each genus it lists, per open trait, the harvest works (genus queries, extra queries, citation step and family
review) whose title or abstract holds a word of that trait, and the evidence already on main for a species of the genus
and that trait. With --check it reads a searched file and fails every record that calls a trait searched while one of
those candidates is unaddressed or main already holds a value for it.

Usage:
  python3 -I tools/views/screen_candidates.py Genus [Genus ...]
  python3 -I tools/views/screen_candidates.py --check docs/views/searched/<unit>.jsonl [--wanted docs/views/wanted/<unit>.jsonl]

A search record addresses a candidate by naming it in "screened", an object from the candidate's DOI (or, for a work with
no DOI, its OpenAlex id such as W2030104807) to a short reason it holds no measurement of the trait; a candidate on the
wanted file given with --wanted is addressed too, and the record should then leave that trait out.
"""
import glob, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harvest_get as hg  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

WORDS = {
    'spectral': r'spectral|opsin|photoreceptor|photopigment|rhodopsin|\bcones?\b|lambda|\bnm\b|ultraviolet|\bUV\b|'
                r'colou?r vision|oil droplet|ocular media|lens|transmi|chromatic|microspectrophotometr|electroretinogra',
    'temporal': r'flicker|temporal resolution|temporal|electroretinogra|\bERG\b|\bHz\b|photoreceptor (response|kinetics)|'
                r'response speed|frequency',
    'acuity': r'acuity|resolution|ganglion cell|retina|retinal|fovea|interommatidial|ommatidi|facet|cycles per degree|'
              r'eye size|eye morpholog|grating|optomotor|optokinetic|spatial vision|photoreceptor density',
    'field': r'visual field|binocular|field of view|eye position|ophthalmoscop|panoramic|blind (area|spot)|eye placement',
    'diel': r'nocturnal|diurnal|crepuscular|cathemeral|activity (pattern|rhythm|time)|daily activity|circadian|time of day|'
            r'flower(ing)? open|anthesis|nyctinast|at night|night-time|nighttime|daytime',
    'eye': r'\beyes?\b|ocell|compound eye|camera eye|superposition|apposition|stemmata|eyespot|eyeless',
    'chemical': r'olfact|chemorecept|chemosens|odou?r|pheromon|antenna|volatile|gustat|taste|smell|vomeronasal|sensill',
    'light_nonvisual': r'photoperiod|phototrop|circadian|\blight\b|phytochrome|cryptochrome|phototropin|gravitrop|shade|'
                       r'blue light|red light|photomorpho|flowering time|day ?length|short-day|long-day|extraocular|'
                       r'dermal photo|photosensitiv',
    'pupil': r'pupil',
    'motion': r'motion|looming|optic flow|movement detect|directional selectiv|collision',
    'eye_movement': r'eye movement|saccad|head movement|vergence|nystagmus|gaze',
    'tapetum': r'tapetum|eyeshine|eye-shine|reflective layer',
    'sensitivity': r'absolute sensitivity|dim light|threshold|quantum|photon|scotopic|night vision|low light',
    'depth': r'depth|stereo|distance (estimation|judg)|parallax|range ?finding',
}
TRAIT_WORDS = {
    'lambda_max_nm': ['spectral'], 'receptor_classes': ['spectral'], 'spectral_range_nm': ['spectral'],
    'colour_vision': ['spectral'], 'cff_hz': ['temporal'], 'corner_hz': ['temporal'], 'acuity_cpd': ['acuity'],
    'interreceptor_deg': ['acuity'], 'interommatidial_deg': ['acuity'], 'fovea': ['acuity'],
    'fov_h_deg': ['field'], 'binocular_deg': ['field'], 'diel': ['diel'], 'eye_type': ['eye'],
    'sense_chemical': ['chemical'], 'sense_light_nonvisual': ['light_nonvisual'], 'pupil_shape': ['pupil'],
    'motion': ['motion'], 'eye_movement': ['eye_movement'], 'tapetum': ['tapetum'],
    'absolute_sensitivity': ['sensitivity'], 'depth_cue': ['depth'],
}


def trait_list(s):
    return [t for t in re.split(r'[;,\s]+', str(s or '')) if t]


def works_of(d, families):
    """(work id, work, step) for every work the harvest returned for the genus, once each."""
    out, seen = [], set()
    def add(ids, pool, step):
        for wid in ids:
            if wid in seen or wid not in pool: continue
            seen.add(wid); out.append((wid, pool[wid], step))
    for q in d.get('queries', []): add(q.get('ids', []), d['works'], 'query "%s"' % q.get('q'))
    for x in d.get('extra', []):
        pool = dict(d['works']); pool.update(x.get('works', {}))
        for q in x.get('queries', []): add(q.get('ids', []), pool, 'query "%s"' % q.get('q'))
    for c in d.get('chase', []): add(c.get('ids', []), d['works'], 'citation step (cites %s)' % c.get('cited_doi'))
    f = families.get(d.get('family')) if d.get('family') else None
    if f: add((f.get('query') or {}).get('ids', []), f.get('works', {}), 'family review "%s"' % (f.get('query') or {}).get('q'))
    return out


def candidates(d, families, trait):
    pats = [re.compile(WORDS[k], re.I) for k in TRAIT_WORDS.get(trait, [])]
    hits = []
    for wid, w, step in works_of(d, families):
        text = (w.get('title') or '') + ' ' + (w.get('abstract') or '')
        found = sorted({m.group(0).lower() for p in pats for m in p.finditer(text)})
        if found: hits.append((wid, w, step, found))
    return hits


def main_evidence():
    ev = {}
    for p in sorted(glob.glob(os.path.join(ROOT, 'docs/views/evidence/*.jsonl'))):
        for i, l in enumerate(open(p, encoding='utf-8'), 1):
            try: r = json.loads(l)
            except ValueError: continue
            g = str(r.get('taxon', '')).split(' ')[0]
            for t in trait_list(r.get('trait')):
                ev.setdefault((g, t), []).append('%s:%d %s %s%s' % (os.path.basename(p)[:-6], i, r.get('taxon'), r.get('value'),
                                                                 ' (partial)' if r.get('partial') else ''))
    return ev


def key(wid, w):
    return (w.get('doi') or '').lower() or wid


def show(genera, families, names):
    ev = main_evidence()
    for g in names:
        d = genera.get(g)
        if not d: print('## %s: not in the harvest' % g); continue
        print('## %s (%s): open traits %s' % (g, d.get('family') or 'no family', ', '.join(d['traits'])))
        for t in d['traits']:
            hits = candidates(d, families, t)
            print('  %s: %d candidates' % (t, len(hits)))
            for wid, w, step, found in hits:
                print('    - %s | %s (%s) | %s | words: %s' % (key(wid, w), w.get('title'), w.get('year'), step, ', '.join(found)))
            for e in ev.get((g, t), []): print('    = on main: ' + e)


def check(path, wanted):
    runs, genera, families, _ = hg.load(); ev = main_evidence()
    want = set()
    if wanted and os.path.exists(wanted):
        for l in open(wanted, encoding='utf-8'):
            try: r = json.loads(l)
            except ValueError: continue
            if r.get('doi'): want.add(r['doi'].lower().strip())
            if r.get('openalex'): want.add(r['openalex'])
    bad = 0
    for i, l in enumerate(open(path, encoding='utf-8'), 1):
        try: r = json.loads(l)
        except ValueError: continue
        g = str(r.get('taxon', '')).split(' ')[0]; d = genera.get(g)
        if not d: continue
        screened = {k.lower() if k.startswith('10.') else k for k in (r.get('screened') or {})}
        for t in trait_list(r.get('trait')):
            for wid, w, step, found in candidates(d, families, t):
                k = key(wid, w)
                if k in want and k not in screened:
                    bad += 1; print('%s:%d %s %s: candidate %s is on the wanted list, so the trait waits for its reading | %s (%s)' % (path, i, g, t, k, w.get('title'), w.get('year')))
                elif k not in screened:
                    bad += 1; print('%s:%d %s %s: unaddressed candidate %s | %s (%s) | words: %s' % (path, i, g, t, k, w.get('title'), w.get('year'), ', '.join(found)))
            for e in ev.get((g, t), []):
                bad += 1; print('%s:%d %s %s: main already holds %s' % (path, i, g, t, e))
    print('%d problems' % bad)
    return 1 if bad else 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    if a[0] == '--check':
        w = a[a.index('--wanted') + 1] if '--wanted' in a else None
        sys.exit(check(a[1], w))
    runs, genera, families, _ = hg.load()
    show(genera, families, a)
