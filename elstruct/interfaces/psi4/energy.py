""" interface to psi4
"""
import os
import subprocess
from mako.template import Template
from ...util import xyz_string

TEMP_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')


def input_string(basis, labels, coords, charge=0, mult=1, niter=100,
                 thresh_log=12):
    geom = xyz_string(labels, coords)
    fill_vals = {
        'charge': charge,
        'mult': mult,
        'geom': geom,
        'basis': basis,
        'thresh_log': thresh_log,
        'niter': niter}

    fname = 'rhf-energy.mako'
    fpath = os.path.join(TEMP_PATH, fname)

    inp_str = Template(filename=fpath).render(**fill_vals)
    return inp_str
