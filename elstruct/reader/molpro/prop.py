""" Molecular Properties
"""

__authors__ = "Kevin Moore, Andreas Copan"
__updated__ = "2019-01-11"

#from ..rere import find as ref
#from ..rere import pattern as rep
#from ..rere import pattern_lib as relib
#from ... import params


# Patterns for other molecular properties
DIPOLE_MOM_PATTERN = 'Permanent Dipole Moment [debye]'

def dipole_moment(lines):
    """ Reads the Permanent Dipole moment from the output file.
        Returns the constants as a list of strings; in Debye.
    """

    # Locate the last instance of the dipole moment
    lines = lines.splitlines()
    dipole_line = DIPOLE_MOM_PATTERN.split()

    # Read the dipole moment
    if len(dipole_line) > 1:
        dipole_mom = dipole_line.strip.split()[2:]
    else:
        dipole_mom = ''
        print('No Dipole Moment Found in File')

    return dipole_mom
