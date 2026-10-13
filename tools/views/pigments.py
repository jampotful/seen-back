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


def main():
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
