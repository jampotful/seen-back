"""Module 2, spectrum: colour matrices from an animal's pigment peaks (docs/ENGINE-DESIGN.md, module 2).

For every matrix in views/*.json (and in a spec's "trial" block) that gives "from_pigments": [peak, ...] in nanometres, this
writes "rows" (3 by 4: screen red, green and blue from the camera's red, green, blue and the shader's invented ultraviolet
channel) and "q" (4 by 4: the animal's classes, padded with zeros, from the same four inputs), which the colour wheel and the
neutral band read. Run with: python3 -I tools/views/pigments.py

What is measured and what is the app's own:
- The pigment curve is the A1 template of Govardovskii and colleagues (2000, Visual Neuroscience 17: 509-528), alpha and beta
  bands, with the constants as the paper gives them (entered from memory in this session; they should be checked against it).
- The camera's channels are taken to be Gaussians at 600, 535 and 460 nm (widths 32, 38 and 30 nm) and the shader's ultraviolet
  channel a Gaussian at 365 nm (width 18). INVENTED: phones do not publish their sensors' curves, and the ultraviolet channel is
  guessed from blue-ness and brightness in the shader. A pixel is read as the sum of those four curves weighted by its values.
- Each class is scaled so that white (all four inputs at 1) gives 1, as an eye adapted to the light would.
- The display mapping is INVENTED (the atlas's "shifted spectrum"): classes sorted by peak; one class shows as grey; two show as
  blue and yellow; three as blue, green and red; four as blue (the shortest), blue-green, green and red. Each screen row is then
  scaled so that white stays white.
"""
import json, math, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
CAMERA = [(600, 32), (535, 38), (460, 30), (365, 18)]   # r, g, b, the invented ultraviolet: (centre, width) in nm, INVENTED

# Pigment peaks for the views that had none in a spec (burst 4), each with the log line it comes from. The logs are on the research
# branches (docs/views/evidence/<unit>.jsonl); "L" is the line. A peak with no source would be marked invented; none is.
# python3 -I tools/views/pigments.py --trials writes a trial block from these for any view in the table that has none yet.
PEAKS = {
    'cat': {'cones': [450, 550], 'rod': 501, 'grade': 'm', 'invented': False,
            'src': 'research/cat-dog evidence L69, L70, L71: Guenther and Zrenner 1993 (S cone 450 nm, L cone 550 nm, rods 501 nm)'},
    'deer': {'cones': [455, 537], 'rod': 497, 'grade': 'm', 'invented': False,
             'src': 'research/squirrel-deer-rabbit evidence L117, L118, L120: Jacobs, Deegan and Neitz 1994, white-tailed deer (S cone about 450 to 460 nm, taken as 455; M cone 537 nm; rods 497 nm)'},
    'rabbit': {'cones': [425, 523], 'rod': 498, 'grade': 'm', 'invented': False,
               'src': 'research/squirrel-deer-rabbit evidence L79, L80, L81: Nuboer, van Nuys and Wortel 1983, wild rabbit (cones 425 and 523 nm, rods 498 nm)'},
    'squirrel': {'cones': [444, 543], 'rod': 502, 'grade': 'm', 'invented': False,
                 'src': 'research/squirrel-deer-rabbit evidence L128, L129, L130: Blakeslee, Jacobs and Neitz 1988, eastern grey squirrel (cones 444 and 543 nm, rods about 502 nm)'},
    'insect': {'cones': [360, 420, 520], 'rod': None, 'grade': 'g', 'invented': False,
               'src': 'research/insect evidence L1 and L190 to L192: van der Kooi and Stavenga 2021 (most insects studied have ultraviolet, blue and green receptors; the peaks are the seven-spot ladybird\'s, 360, 420 and 520 nm)'},
}


def template(peak, lam):
    x = peak / lam
    a = 0.8795 + 0.0459 * math.exp(-((peak - 300) ** 2) / 11940)
    alpha = 1 / (math.exp(69.7 * (a - x)) + math.exp(28 * (0.922 - x)) + math.exp(-14.9 * (1.104 - x)) + 0.674)
    lb, bb = 189 + 0.315 * peak, -40.5 + 0.195 * peak
    return alpha + 0.26 * math.exp(-(((lam - lb) / bb) ** 2))


def catches(peaks):
    lams = range(300, 751, 2)
    q = []
    for p in peaks:
        row = [sum(template(p, l) * math.exp(-0.5 * ((l - c) / w) ** 2) for l in lams) for c, w in CAMERA]
        s = sum(row)
        q.append([v / s for v in row])
    return q


def display(n):
    """Screen rows (red, green, blue) from n classes sorted shortest first. INVENTED."""
    return {1: [[1], [1], [1]],
            2: [[0, 1], [0, 1], [1, 0]],
            3: [[0, 0, 1], [0, 1, 0], [1, 0, 0]],
            4: [[0, 0, 0, 1], [0, 0.5, 1, 0], [1, 0.5, 0, 0]]}[n]


def matrix(peaks):
    peaks = sorted(peaks)
    q = catches(peaks)
    D = display(len(peaks))
    rows = []
    for d in D:
        r = [sum(d[i] * q[i][c] for i in range(len(q))) for c in range(4)]
        s = sum(r) or 1
        rows.append([round(v / s, 5) for v in r])
    qq = [[round(v, 5) for v in r] for r in q] + [[0, 0, 0, 0]] * (4 - len(q))
    return rows, qq


def fmt(v, ind=''):
    """As tools/views/fmt.js: short objects and arrays on one line."""
    flat = json.dumps(v, ensure_ascii=False, separators=(',', ':'))
    if len(flat) + len(ind) <= 120 or not isinstance(v, (dict, list)):
        return flat
    nxt = ind + '  '
    if isinstance(v, list):
        return '[\n' + ',\n'.join(nxt + fmt(x, nxt) for x in v) + '\n' + ind + ']'
    return '{\n' + ',\n'.join(nxt + json.dumps(k, ensure_ascii=False) + ': ' + fmt(x, nxt) for k, x in v.items()) + '\n' + ind + '}'


def fill(mats):
    n = 0
    for m in (mats or {}).values():
        if isinstance(m, dict) and m.get('from_pigments'):
            m['rows'], m['q'] = matrix(m['from_pigments'])
            n += 1
    return n


TOOL = 'tools/views/pigments.py (template: Govardovskii 2000; camera curves invented)'


def trial_for(key, pk):
    """A trial block: the cones as the view's colour, the rods as its dark-adapted colour, the colour wheel and neutral band."""
    name = key.upper()
    mats = {name: {'from_pigments': pk['cones'], 'grade': pk['grade'], 'invented': True, 'src': [pk['src'], TOOL]}}
    spec = {'q': name, 'neutral': {'value': 1, 'grade': 'i', 'invented': True, 'src': [], 'range': [0, 2]}}
    rows = [['i', 'Being tried: colour from pigments', "On this trial the colours come from the measured receptor peaks (%s nm). The camera's colours and the display are the app's." % ', '.join(map(str, pk['cones'])),
             [pk['src'].split(': ', 1)[1].split(' (')[0], 'param:spectrum.neutral', 'param:matrices.' + name, 'param:M']]]
    if pk['rod']:
        mats[name + '_ROD'] = {'from_pigments': [pk['rod']], 'grade': pk['grade'], 'invented': True, 'src': [pk['src'], TOOL]}
        spec['dark'] = name + '_ROD'
        spec['adaptAt'] = {'value': [-2, -1], 'grade': 'i', 'invented': True, 'src': [], 'range': [-3, 0]}
        rows.append(['i', 'Being tried: dusk', "As the light falls, the colours drift toward what the rods take in, which peak near %d nm. The peak is measured; where the change happens is the app's guess." % pk['rod'],
                     [pk['src'].split(': ', 1)[1].split(' (')[0], 'param:spectrum.adaptAt', 'param:matrices.' + name + '_ROD']])
    draw = {'spectrum': [{'name': 'shift', 'invented': True, 'note': "each class on one of the screen's three, the guessed ultraviolet in the bluest slot (atlas 5)"},
                         {'name': 'neutral', 'invented': True, 'note': 'where the animal sees no colour and a person does, a faint shimmer like heat haze (atlas 4)'},
                         {'name': 'wheel', 'invented': True, 'note': 'a finger dragged across the picture turns which classes are shown (atlas 5)'}]}
    return {'matrices': mats, 'params': {'M': {'value': name, 'grade': pk['grade'], 'invented': True, 'src': [pk['src']]}},
            'spectrum': spec, 'draw': draw, 'rows': rows}


def trials():
    for key, pk in PEAKS.items():
        f = ROOT / 'views' / (key + '.json')
        spec = json.loads(f.read_text(encoding='utf-8'))
        if spec.get('trial'):
            print(key, 'already has a trial; left alone')
            continue
        t = trial_for(key, pk)
        t['rows'] = spec['rows'] + t['rows']
        spec['trial'] = t
        f.write_text(fmt(spec) + '\n', encoding='utf-8')
        print(key, 'trial written')


def main():
    if '--trials' in sys.argv:
        trials()
    changed = 0
    for f in sorted((ROOT / 'views').glob('*.json')):
        if f.name == 'index.json':
            continue
        spec = json.loads(f.read_text(encoding='utf-8'))
        n = fill(spec.get('matrices')) + fill((spec.get('trial') or {}).get('matrices'))
        for g in ((spec.get('by') or {}).get('genus') or {}).values():
            n += fill(g.get('matrices'))
        if n:
            f.write_text(fmt(spec) + '\n', encoding='utf-8')
            changed += 1
            print(f.name, n)
    return 0


if __name__ == '__main__':
    sys.exit(main())
