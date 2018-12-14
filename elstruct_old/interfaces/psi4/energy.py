""" interface to psi4
"""
import os
import subprocess
from mako.template import Template
from ... import params as par
from ...util import xyz_string
from ...rere.find import captures
from ...rere.pattern import capturing
from ...rere.pattern import one_or_more
from ...rere.pattern_lib import WHITESPACE
from ...rere.pattern_lib import FLOAT

TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')

TEMPLATE_DCT = {
    par.METHOD.RHF: 'rhf-energy.mako',
    par.METHOD.CCSD: 'ccsd-energy.mako'
}

PATTERN_DCT = {
    par.METHOD.RHF: (
        'Final Energy:' + one_or_more(WHITESPACE) + capturing(FLOAT)
    ),
    par.METHOD.CCSD: (
        'CCSD total energy' + one_or_more(WHITESPACE) + '=' +
        one_or_more(WHITESPACE) + capturing(FLOAT)
    )
}


def energy(runner, theory, basis, labels, coords, charge=0, mult=1, niter=100,
           thresh_log=12):
    inp_str = _input_string(theory, basis, labels, coords, charge, mult,
                            niter, thresh_log)
    out_str = runner(inp_str)
    en = _read_energy(out_str, theory)
    return en


def _input_string(theory, basis, labels, coords, charge=0, mult=1, niter=100,
                 thresh_log=12):
    assert theory in TEMPLATE_DCT

    geom = xyz_string(labels, coords)
    fill_vals = {
        'charge': charge,
        'mult': mult,
        'geom': geom,
        'basis': basis,
        'thresh_log': thresh_log,
        'niter': niter}

    fname = TEMPLATE_DCT[theory]
    fpath = os.path.join(TEMPLATE_PATH, fname)

    inp_str = Template(filename=fpath).render(**fill_vals)
    return inp_str


def _read_energy(output, theory):
    assert theory in PATTERN_DCT
    pattern = PATTERN_DCT[theory]
    caps = captures(pattern, output)

    if not caps:
        raise ValueError("No energy found")

    cap = caps[-1]
    energy = float(cap)
    return energy
