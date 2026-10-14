"""Shared word lists for the thoroughness tools: trait words found in free text, mapped to the trait keys of
docs/views/gaps/rows.json. A heuristic: it decides matching and windowing, never what a record says."""
import re

WORDS = {
    'acuity': ['acuity_cpd'], 'resolv': ['acuity_cpd'], 'cycles per degree': ['acuity_cpd'], 'cpd': ['acuity_cpd'],
    'flicker': ['cff_hz'], 'fusion': ['cff_hz'], 'cff': ['cff_hz'], 'temporal resolution': ['cff_hz', 'corner_hz'],
    'corner frequenc': ['corner_hz'], 'pupil': ['pupil_shape'], 'tapetum': ['tapetum'], 'fovea': ['fovea'],
    'area centralis': ['fovea'], 'visual streak': ['fovea'], 'ganglion cell': ['fovea', 'acuity_cpd'],
    'retinal topograph': ['fovea'], 'visual field': ['fov_h_deg', 'fov_v_deg', 'binocular_deg'],
    'field of view': ['fov_h_deg', 'fov_v_deg', 'binocular_deg'], 'binocular': ['binocular_deg'],
    'opsin': ['receptor_classes', 'lambda_max_nm'], 'visual pigment': ['receptor_classes', 'lambda_max_nm'],
    'photopigment': ['receptor_classes', 'lambda_max_nm'], 'spectral sensitiv': ['receptor_classes', 'lambda_max_nm', 'spectral_range_nm'],
    'max': ['lambda_max_nm'], 'colour vision': ['colour_vision', 'receptor_classes'], 'color vision': ['colour_vision', 'receptor_classes'],
    'dichromat': ['receptor_classes', 'colour_vision'], 'trichromat': ['receptor_classes', 'colour_vision'],
    'ultraviolet': ['spectral_range_nm'], 'oil droplet': ['oil_droplets'], 'ommatid': ['interommatidial_deg', 'acuity_cpd'],
    'interommatidial': ['interommatidial_deg'], 'acceptance angle': ['acceptance_deg'], 'rhabdom': ['acceptance_deg'],
    'polari': ['polarization'], 'absolute sensitiv': ['absolute_sensitivity'], 'f-number': ['f_number'],
    'eye movement': ['eye_movement'], 'saccad': ['eye_movement'], 'nocturnal': ['diel'], 'diurnal': ['diel'],
    'stereo': ['depth_cue'], 'motion detect': ['motion'],
}

def traits_in(text):
    """Trait keys named in a free-text field, by key or by word."""
    t = (text or '').lower()
    keys = {k for ks in WORDS.values() for k in ks if k in t}
    keys |= {k for w, ks in WORDS.items() if w != 'max' and w in t for k in ks}
    if re.search(r'(λ|lambda)\s*_?max', t): keys.add('lambda_max_nm')
    return keys
