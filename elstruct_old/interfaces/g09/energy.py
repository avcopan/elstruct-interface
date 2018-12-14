""" interface to g09
"""
import os
import subprocess
from mako.template import Template
from ... import params as par
from ...util import xyz_string
from ...rere.find import captures
from ...rere.pattern import escape
from ...rere.pattern import capturing
from ...rere.pattern import one_or_more
from ...rere.pattern_lib import WHITESPACE
from ...rere.pattern_lib import FLOAT

INP_NAME = 'input.dat'
OUT_NAME = 'output.dat'

TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')

TEMPLATE_DCT = {
    par.METHOD.RHF: 'rhf-energy.mako'
}

PATTERN_DCT = {
    par.METHOD.RHF: (
        escape('E(RHF) =') + one_or_more(WHITESPACE) + capturing(FLOAT)
    )
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

    en = _read_energy(out_str, theory)
    return en


def _input_string(theory, basis, labels, coords, charge=0, mult=1, niter=100,
                 thresh_log=12):
    assert theory in TEMPLATE_DCT

    geom = xyz_string(labels, coords)
    fill_vals = {
        'basis': basis,
        'thresh_log': thresh_log,
        'niter': niter,
        'charge': charge,
        'mult': mult,
        'geom': geom,
        'comment': 'RHF Energy'}

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
