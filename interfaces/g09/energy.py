""" interface to g09
"""
import os
import subprocess
from mako.template import Template

PATH = os.path.dirname(os.path.realpath(__file__))


def input_string(basis, labels, coords, charge=0, mult=1, niter=100,
                 thresh_log=12):
    geom = xyz_string(labels, coords)
    fill_vals = {
        'basis': basis,
        'thresh_log': thresh_log,
        'niter': niter,
        'charge': charge,
        'mult': mult,
        'geom': geom,
        'comment': 'RHF Energy'}

    fname = 'rhf-energy.mako'
    fpath = os.path.join(PATH, fname)

    inp_str = Template(filename=fpath).render(**fill_vals)
    return inp_str


def xyz_string(labels, coords):
    """ .xyz format string for this cartesian geometry
    :param labels: optional labels for the beginnings of atom lines, by index
    :type labels: dict
    """
    assert len(labels) == len(coords)
    dxyz = '\n'.join(
        '{:s} {:s} {:s} {:s}'.format(asymb, *map(repr, xyz))
        for asymb, xyz in zip(labels, coords))
    return dxyz


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
