""" Molecular Properties
"""

__authors__ = "Kevin Moore, Andreas Copan"
__updated__ = "2019-01-14"

from ..rere import find as ref
from ..rere import pattern as rep
from ..rere import pattern_lib as relib
from ... import params


def pattern_reader():
    """ Returns pattern.
    """

    return val

def dipole_moment_reader(output_string):
    """ Reads the Permanent Dipole moment from the output file.
        Returns the constants as a list of strings; in Debye.
    """

    dipole_mom_pattern = (
        'Dipole Moment: \[D\]' +
        rep.one_or_more(relib.WHITESPACE) +
        'X:'
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT) +
        'Y:'
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT) +
        'Z:'
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT) +
        'Total:'
        rep.one_or_more(relib.WHITESPACE) +
        relib.FLOAT
    )
   
    dipole_mom = pattern_reader(pattern, output_string) 

    return dipole_mom


##### Dictionary of functions to read molecular properties in the files #####

PROPERTY_READERS = {
    params.PROPERTY.DIPOLE_MOM : dipole_moment_reader
}


##### Molecular property reader function called by external scripts #####

def mol_property(output_string):
    """ Returns some propert.
    """
    
    mol_property = PROPERTY_READERS[](output_string) 

    return mol_property
    

