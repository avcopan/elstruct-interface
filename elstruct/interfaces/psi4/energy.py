""" interface to psi4
"""
import os
import subprocess
from mako.template import Template
from ...util import xyz_string

INP_NAME = 'input.dat'
OUT_NAME = 'output.dat'

TEMP_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')

TEMP_DCT = {
    'rhf': 'rhf-energy.mako'
}


def energy(runner, theory, basis, labels, coords, charge=0, mult=1, niter=100,
           thresh_log=12):

    inp_str = _input_string(theory, basis, labels, coords, charge, mult,
                            niter, thresh_log)
    with open(INP_NAME, 'w') as inp_fle:
        inp_fle.write(inp_str)

    runner()

    with open(OUT_NAME) as out_fle:
        out_str = out_fle.read()

    return -99


def _input_string(theory, basis, labels, coords, charge=0, mult=1, niter=100,
                 thresh_log=12):
    assert theory in TEMP_DCT

    geom = xyz_string(labels, coords)
    fill_vals = {
        'charge': charge,
        'mult': mult,
        'geom': geom,
        'basis': basis,
        'thresh_log': thresh_log,
        'niter': niter}

    fname = TEMP_DCT[theory]
    fpath = os.path.join(TEMP_PATH, fname)

    inp_str = Template(filename=fpath).render(**fill_vals)
    return inp_str
