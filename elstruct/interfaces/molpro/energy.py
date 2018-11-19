""" interface to molpro
"""
import os
from mako.template import Template
from ...chem import electron_count
from ...util import xyz_string
from ...rere.find import single_capture
from ...rere.pattern import escape
from ...rere.pattern import capturing
from ...rere.pattern import one_or_more
from ...rere.pattern_lib import WHITESPACE
from ...rere.pattern_lib import FLOAT

TEMP_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')

TEMP_DCT = {
    'rhf': 'rhf-energy.mako'
}


def input_string(theory, basis, labels, coords, charge=0, mult=1, niter=100,
                 thresh_log=12):
    assert theory in TEMP_DCT

    geom = xyz_string(labels, coords)
    nelec = electron_count(labels, charge)
    spin = mult - 1
    fill_vals = {
        'thresh_log': thresh_log,
        'geom': geom,
        'basis': basis,
        'niter': niter,
        'nelec': nelec,
        'irrep': 1,
        'spin': spin,
        'charge': charge}

    fname = TEMP_DCT[theory]
    fpath = os.path.join(TEMP_PATH, fname)

    inp_str = Template(filename=fpath).render(**fill_vals)
    return inp_str


def read_energy(output, theory, basis):
    theory = theory.upper()
    basis = basis.upper()
    pattern = (theory + escape('/') + basis + one_or_more(WHITESPACE) +
               'energy=' + one_or_more(WHITESPACE) + capturing(FLOAT))
    capture = single_capture(pattern, output)

    if not capture:
        raise ValueError("No energy found")

    energy = float(capture)
    return energy
