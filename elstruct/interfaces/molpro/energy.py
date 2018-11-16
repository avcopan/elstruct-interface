""" interface to molpro
"""
import os
import subprocess
from mako.template import Template
from ...chem import electron_count
from ...util import xyz_string

TEMP_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')


def input_string(basis, labels, coords, charge=0, mult=1, niter=100,
                 thresh_log=12):
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

    fname = 'rhf-energy.mako'
    fpath = os.path.join(TEMP_PATH, fname)

    inp_str = Template(filename=fpath).render(**fill_vals)
    return inp_str


if __name__ == '__main__':
    BASIS = 'STO-3G'
    CHARGE = 0
    MULT = 1
    LABELS = ('O', 'H', 'H')
    COORDS = ((0.000000000000,  0.000000000000, -0.143225816552),
              (0.000000000000,  1.638036840407,  1.136548822547),
              (0.000000000000, -1.638036840407,  1.136548822547))
    INP_STR = input_string(basis=BASIS, labels=LABELS, coords=COORDS,
            charge=CHARGE, mult=MULT)
    print(INP_STR)
