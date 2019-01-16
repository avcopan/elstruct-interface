"""
Library of functions to retrieve molecular properties from a CFour 2.0 output file.

Properties currently supported:
(1) Dipole Moment

"""

__authors__ = "Kevin Moore, Andreas Copan"
__updated__ = "2019-01-15"

from ..rere import parse as repar
from ..rere import find as ref
from ..rere import pattern as rep
from ..rere import pattern_lib as relib
from ... import params


##### Series of functions to read molecular properties #####

def dipole_moment_reader(output_string):
    """ Reads the Permanent Dipole moment from the output file.
        Returns the constants as a list of strings; in Debye.
    """

    dipole_mom_pattern = (
    )

    dipole_mom = repar.list_float(pattern, output_string)

    return dipole_mom


##### Dictionary of functions to read molecular properties in the files #####

PROPERTY_READERS = {
    params.PROPERTY.DIPOLE_MOM : dipole_moment_reader
}


##### Molecular property reader function called by external scripts #####

def mol_property(prop, output_string):
    """ Retrieves the desired molecular property.
    """

    mol_property = PROPERTY_READERS[prop](output_string)

    return mol_property
