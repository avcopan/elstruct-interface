""" input file writers for molpro
"""

import os
from mako.template import Template
from ...util import xyz_string
from ... import params


DIR_PATH = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_PATH = os.path.join(DIR_PATH, 'templates')

TEMPLATE_FILES = {
    params.METHOD.RHF: 'rhf-energy.mako',
}


def energy(theory, basis, labels, coords, charge=0, mult=1, niter=100,
           thresh_log=12, memory=8, comment='Single Point Energy'):
    """ Writes a single-point energy input file for Molpro 2015.
    """

    assert theory in TEMPLATE_FILES.keys()

    geom_str = xyz_string(labels, coords)
    spin = mult - 1
    memory = int(memory * (1000.0 / 8.0))
    fill_vals = {
        'charge': charge,
        'spin': spin,
        'geom': geom_str,
        'basis': basis,
        'thresh_log': thresh_log,
        'niter': niter,
        'memory': memory,
        'comment': comment}

    template_file_name = TEMPLATE_FILES[theory]
    template_file_path = os.path.join(TEMPLATE_PATH, template_file_name)

    input_str = Template(filename=template_file_path).render(**fill_vals)

    return input_str
