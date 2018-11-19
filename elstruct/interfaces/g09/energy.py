""" interface to g09
"""
import os
import subprocess
from mako.template import Template
from ...util import xyz_string

TEMP_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')

TEMP_DCT = {
    'rhf': 'rhf-energy.mako'
}


def input_string(theory, basis, labels, coords, charge=0, mult=1, niter=100,
                 thresh_log=12):
    assert theory in TEMP_DCT

    geom = xyz_string(labels, coords)
    fill_vals = {
        'basis': basis,
        'thresh_log': thresh_log,
        'niter': niter,
        'charge': charge,
        'mult': mult,
        'geom': geom,
        'comment': 'RHF Energy'}

    fname = TEMP_DCT[theory]
    fpath = os.path.join(TEMP_PATH, fname)

    inp_str = Template(filename=fpath).render(**fill_vals)
    return inp_str
