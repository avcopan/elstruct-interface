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

def rhf_uhf_reader(output_string):
    """ Retrieves the RHF or UHF energy.
        Returns as a float. Units of Hartrees.
    """

    # Set the string pattern to find the RHF energy
    rhf_uhf_pattern = (
        'E(SCF)=' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) 
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) + 
        'D' +
        rep.one_or_more(relib.INTEGER) 
    )

    return rhf_energy

def rohf_reader(output_string):
    """ Retrieves the ROHF energy.
        Returns as a float. Units of Hartrees.
    """

    # Set the string pattern to find the UHF energy
    rohf_pattern = (
    'E(ROHF)=' +
    rep.one_or_more(relib.WHITESPACE) +
    rep.one_or_more(relib.FLOAT) 
    rep.one_or_more(relib.WHITESPACE) +
    rep.one_or_more(relib.FLOAT) + 
    'D' +
    rep.one_or_more(relib.INTEGER) 
    )
    
    return rohf_energy

def mp2_reader(output_string):
    """ Retrieves the RHF-MP2 or UHF-MP2 energy.
        Returns as a float. Units of Hartrees.
    """

    mp2_pattern = (
        'MP2 energy' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )
    
    return mp2_energy

def ccsd_reader(output_string):
    """ Retrieves the RHF-CCSD or UHF-CCSD energy.
        Returns as a float. Units of Hartrees.
    """

    ccsd_pattern = (
        'CCSD energy' + 
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) 
    )

    return ccsd_energy

def ccsd_t_reader(output_string):
    """ Retrieves the RHF-CCSD(T) or UHF-CCSD(T) energy.
        Returns as a float. Units of Hartrees.
    """

    ccsd_t_pattern = (
        'CCSD(T) energy' + 
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) 
    )

    return ccsd_energy


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


##### For lazy testing #####

if __name__ == '__main__':
    with open('open_output.dat', 'r') as outfile:
        OUTPUT_STR = outfile.read()
    print(energy('rmp2', OUTPUT_STR))
