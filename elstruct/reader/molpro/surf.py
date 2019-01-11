""" Reads in the surface properties
"""

__authors__ = "Kevin Moore, Andreas Copan"
__updated__ = "2019-01-11"

from ..rere import find as ref
from ..rere import pattern as rep
from ..rere import pattern_lib as relib
from ... import params


HESS_START_LINE = 'Force Constants (Second Derivatives of the Energy)'
HESS_END_LINE = 'Atomic Masses'

# partially from patools
def hessian(lines, symmetry=False):
    """ Reads the unprojected Cartesian Hessian from the output file.
        Returns the Hessian in a string; in UNITS
        TODO: (1) Grabber only works if job is run without symmetry
              (2) Convert Hessian to a full Hessian? or lower/upper Triangular?
    """

    # Isolate block of lines from output file containing the Hessian    
    start_line_num = io.get_line_number( HESS_START_LINE, lines=lines ) + 1
    end_line_num   = io.get_line_number( HESS_END_LINE, lines=lines ) - 2
    hess_lines = lines.split()[ start_line_num, end_line_num ] 
    if start_line < 0:
        return ''
    hess = ''

    # Read the Hessian
    if symmetry == False:

        for line in lines[sline+1:eline-2]:
            hessline = ''
            for val in line.split():
                if 'G'  in val:
                    if 'GX' in val:
                        add = 1
                        val = val.replace('GX', '')
                    elif 'GY' in val:
                        add = 2
                        val = val.replace('GY', '')
                    else:
                        add = 3
                        val = val.replace('GZ', '')
                val = str((int(val) - 1) * 3 + add)
            hessline += '\t' +  val
        hess +=  hessline + '\n'
    
    else:

        Code     

    return hess
