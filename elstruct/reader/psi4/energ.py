"""
Library of functions to retrieve electronic energies from a Molpro 2015 output file.

Energies currently supported:

This script has the user call the function 'energy' which accepts the theory method and output
file lines as input. The theoretical method serves as a key to a dictionary of functions. The
key corresponds to an energy-reader function which reads the output file for the appropriate
string pattern to return the user-requested energy.

"""

__authors__ = "Kevin Moore, Andreas Copan"
__updated__ = "2019-01-11"

from ..rere import find as ref
from ..rere import pattern as rep
from ..rere import pattern_lib as relib
from ... import params


##### Series of functions to read the electronic energy #####

def pattern_reader(pattern, output_string):
    """ Use pattern to retrieve the LAST electronic energy in the output file.
        Returns energy as float.
    """

    # Locate the final energy in the output file
    energy_str = ref.last_capture(pattern, output_string)

    # Check if energy values is found, if so, convert to float
    energy_val = (None if energy_str is None else float(energy_str))

    return energy_val

def scf_reader(output_string):
    """ Retrieves the RHF or UHF energy.
        Returns as a float. Units of Hartrees.
    """

    # Set the string pattern to find the RHF energy
    rhf_pattern = (
        '@RHF Final Energy:' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    uhf_pattern = (
        '@UHF Final Energy:' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    rohf_pattern = (
        '@ROHF Final Energy:' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    rks_pattern = (
        '@RKS Final Energy:' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    uks_pattern = (
        '@UKS Final Energy:' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    roks_pattern = (
        '@ROKS Final Energy:' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    alt_pattern = (
        'SCF energy' +
        rep.one_or_more(relib.WHITESPACE) +
        '(wfn)' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    alt_pattern_2 = (
        'Reference energy' +
        rep.one_or_more(relib.WHITESPACE) +
        '(file' +
        relib.INTEGER +
        ')' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    # check if for scf only or any energy (same for df-mp2)
    alt_pattern_3 = (
        'Total Energy =' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    return scf_energy

def mp2_reader(output_string):
    """ Grabs MP2 wiht any reference """

    # Check if same in higer correlation
    mp2_pattern = (
        '* MP2 total energy' +
        rep.one_or_more(relib.WHITESPACE) +
        '=' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    return mp2_energy

def ccsd_reader(output_string):
    """ Grabs MP2 wiht any reference """

    # Check if same in higer correlation
    ccsd_pattern = (
        '* CCSD total energy' +
        rep.one_or_more(relib.WHITESPACE) +
        '=' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    ccsd_pattern = (
        'Total CCSD energy' +
        rep.one_or_more(relib.WHITESPACE) +
        '=' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    return ccsd_energy

def ccsd_t_reader(output_string):
    """ Grabs MP2 wiht any reference """

    # Check if same in higer correlation
    ccsd_t_pattern = (
        '* CCSD(T) total energy' +
        rep.one_or_more(relib.WHITESPACE) +
        '=' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    return ccsd_t_energy

##### Dictionary of functions to read the energies in the files #####

ENERGY_READERS = {
}


##### Energy reader function called by external scripts #####

def energy(method, output_string):
    """ Calls the appropriate function to read in the energy
    """
    assert method in ENERGY_READERS.keys()

    energy = ENERGY_READERS[method](output_string)

    return energy
