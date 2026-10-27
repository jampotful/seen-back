#!/usr/bin/env python3
"""Gap-index regressions, using only temporary repositories and the standard library."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('gaps', HERE / 'gaps.py')
gaps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gaps)


def record(**fields):
    return dict(unit='intake', taxon='Arenaria interpres', rank='species', family='Scolopacidae',
                order='Charadriiformes', trait='pupil_shape', value='round', grade='m', opened=True,
                source={'doi': '10.example/test'}, quote='round', **fields)


def write(root, name, text):
    path = Path(root) / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


def evidence(root, filename, records):
    write(root, 'docs/views/evidence/' + filename + '.jsonl', ''.join(json.dumps(r) + '\n' for r in records))


class GapsTests(unittest.TestCase):
    def test_pending_branches_require_explicit_flag_and_skip_held(self):
        with tempfile.TemporaryDirectory() as root:
            def git(*args):
                subprocess.run(['git', '-C', root, *args], check=True, capture_output=True)
            git('init', '-q')
            evidence(root, 'intake-1', [record()])
            git('add', '.')
            git('-c', 'user.name=Test', '-c', 'user.email=test@example.org', 'commit', '-qm', 'base')
            evidence(root, 'pending', [dict(record(), taxon='Arenaria pending')])
            evidence(root, 'pending-failed', [dict(record(), taxon='Arenaria held')])
            git('add', '.')
            git('-c', 'user.name=Test', '-c', 'user.email=test@example.org', 'commit', '-qm', 'pending')
            git('update-ref', 'refs/remotes/origin/research/pending', 'HEAD')
            git('reset', '--hard', 'HEAD~1')
            # Default must not inspect branch refs at all.
            with patch.object(gaps, 'git', side_effect=AssertionError('branch read')):
                recs, _ = gaps.load_evidence(root, gaps.Tax(), set())
            self.assertEqual([r['_id'] for r in recs], ['intake-1#1'])
            recs, _ = gaps.load_evidence(root, gaps.Tax(), set(), with_branches=True)
            self.assertEqual([r['_id'] for r in recs], ['intake-1#1', 'pending#1'])

    def test_scratch_output_reads_repository_taxonomy_and_row_inputs(self):
        with tempfile.TemporaryDirectory() as root:
            write(root, 'docs/views/gaps/rows.json', json.dumps({
                'classes': {'genus': ['pupil_shape']},
                'views': {v: {'Pupil': ['pupil_shape']} for v in gaps.VIEWS}}))
            write(root, 'docs/views/gaps/taxonomy-gbif.tsv',
                  'genus\tfamily\torder\tsource\nArenaria\tScolopacidae\tCharadriiformes\tGBIF\n')
            def show(repo, ref, path):
                if path == 'rows.tsv':
                    return 'sci\ten\trecords\tgroup\nArenaria interpres\tTurnstone\t12\tbird\n'
                return json.dumps({'species': []})
            with patch.object(gaps, 'show', side_effect=show), patch('sys.argv', [
                    'gaps.py', '--repo', root, '--out', 'scratch', '--no-lit']):
                gaps.main()
            cells = [json.loads(line) for line in (Path(root) / 'scratch/cells.jsonl').read_text().splitlines()]
            self.assertEqual([(c['family'], c['order']) for c in cells], [('Scolopacidae', 'Charadriiformes')])
            self.assertFalse((Path(root) / 'docs/views/gaps/cells.jsonl').exists())

    def test_filename_retractions_fixes_and_regraded_copies(self):
        with tempfile.TemporaryDirectory() as root:
            evidence(root, 'intake-7', [record()])
            evidence(root, 'intake-8', [record()])  # shared unit/content, distinct file
            evidence(root, 'intake-8-failed', [record()])
            copies = [dict(record(), unit='oa-1', taxon='Arenaria species' + str(i)) for i in range(6)]
            evidence(root, 'oa-regraded', copies)
            write(root, 'docs/views/fixes/test.jsonl', json.dumps({'id': 'intake-8:1', 'partial': True}))
            retracted = {'intake-7:1'} | {'oa-1:' + str(n) for n in range(1, 7)}
            recs, _ = gaps.load_evidence(root, gaps.Tax(), retracted)
            self.assertEqual(len(recs), 7)
            self.assertEqual(recs[0]['_id'], 'intake-8#1')
            self.assertTrue(recs[0]['partial'])
            self.assertEqual(sum(r['_id'].startswith('oa-regraded#') for r in recs), 6)

    def test_homonyms_have_their_own_family_and_do_not_carry(self):
        tax = gaps.Tax()
        pairs = [('Arenaria', 'Scolopacidae', 'Charadriiformes', 'bird', 'Caryophyllaceae', 'Caryophyllales'),
                 ('Morus', 'Sulidae', 'Suliformes', 'wader', 'Moraceae', 'Rosales'),
                 ('Aquarius', 'Gerridae', 'Hemiptera', 'insect', 'Alismataceae', 'Alismatales')]
        for genus, family, order, view, plant_family, plant_order in pairs:
            tax.add(genus, plant_family, plant_order)
            tax.add(genus, family, order)
            self.assertEqual(tax.family(genus, view), family)
            self.assertEqual(tax.order(genus, view), order)
            self.assertEqual(tax.family(genus, 'plant'), plant_family)
            self.assertEqual(tax.family(genus), '')
        tax.add('Sus', 'Suidae', 'Artiodactyla', view='other')
        tax.add('Bos', 'Bovidae', 'Artiodactyla')
        self.assertEqual(tax.family('Bos', 'deer'), 'Bovidae')
        with tempfile.TemporaryDirectory() as root:
            evidence(root, 'plant', [dict(record(), family='Caryophyllaceae', order='Caryophyllales')])
            recs, index = gaps.load_evidence(root, tax, set())
            sp = dict(sci='Arenaria interpres', genus='Arenaria', family='Scolopacidae', order='Charadriiformes', view='bird')
            self.assertEqual(gaps.cell(sp, 'pupil_shape', 'genus', index, gaps.order_evidence(recs), tax, [])['state'], 'i')

    def test_gbif_input_is_independent_of_output_and_synonyms_are_view_scoped(self):
        with tempfile.TemporaryDirectory() as root:
            base = 'docs/views/gaps/'
            write(root, base + 'taxonomy-gbif.tsv', 'genus\tfamily\torder\tsource\nFowlea\tNatricidae\tSquamata\tGBIF\n')
            write(root, base + 'taxonomy-extra.tsv', 'genus\tfamily\torder\tsource\nFowlea\tWrong\tSquamata\town\n')
            tax = gaps.Tax()
            tax.load_tables(root)  # absent synonyms is valid
            self.assertEqual(tax.placement('Fowlea', 'reptile'), ('Natricidae', 'Squamata'))
            write(root, base + 'synonyms.tsv', 'old_genus\tcurrent_genus\tview\tsource_url\nXenochrophis\tFowlea\treptile\thttps://example.org/name\n')
            tax.load_tables(root)
            tax.add('Xenochrophis', 'Colubridae', 'Squamata')
            self.assertEqual(tax.placement('Xenochrophis', 'reptile'), ('Natricidae', 'Squamata'))
            self.assertEqual(tax.aliases('Xenochrophis piscator', 'plant'), {'Xenochrophis piscator'})
            evidence(root, 'snake', [dict(record(), taxon='Fowlea piscator', family='Natricidae', order='Squamata')])
            recs, index = gaps.load_evidence(root, tax, set())
            sp = dict(sci='Xenochrophis piscator', genus='Xenochrophis', family='Natricidae', order='Squamata', view='reptile')
            self.assertEqual(gaps.cell(sp, 'pupil_shape', 'genus', index, gaps.order_evidence(recs), tax, [])['state'], 'm')
            sp['sci'] = 'Xenochrophis other'
            self.assertEqual(gaps.cell(sp, 'pupil_shape', 'genus', index, gaps.order_evidence(recs), tax, [])['state'], 'g')
            sp.update(sci='Fowlea piscator', genus='Fowlea')
            evidence(root, 'snake', [dict(record(), taxon='Xenochrophis piscator', family='Natricidae', order='Squamata')])
            recs, index = gaps.load_evidence(root, tax, set())
            self.assertEqual(gaps.cell(sp, 'pupil_shape', 'genus', index, gaps.order_evidence(recs), tax, [])['state'], 'm')


if __name__ == '__main__':
    unittest.main()
