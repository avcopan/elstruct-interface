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
        TODO: change last capture
    """

    
    # Locate the final energy in the output file
    energy_str = ref.last_capture(pattern, output_string)

    # Check if energy values is found, if so, convert to float
    energy_val = (None if energy_str is None else float(energy_str))

    return energy_val

def hf_reader(output_string):
    """ Retrieves the RHF, UHF, or ROHF energy.
        Returns as a float. Units of Hartrees.
    """

    # Set the string pattern to find the RHF energy
    hf_pattern = (
        '***FINAL HARTREE-FOCK ENERGY:' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) 
        rep.one_or_more(relib.WHITESPACE) +
        '[AU]' 
    )    
    
    rohf_pattern_2 = (
    '***SEMICANONICAL ROHF ENERGY:' +
    rep.one_or_more(relib.WHITESPACE) +
    rep.one_or_more(relib.FLOAT) 
    rep.one_or_more(relib.WHITESPACE) +
    '[AU]' 
    )

    # Obtain the RHF energy
    hf_energy = pattern_reader(hf_pattern, output_string)
    
    return hf_energy

def rhf_mp2_reader(output_string):
    """ Retrieves the RHF, UHF, or ROHF energy.
        Returns as a float. Units of Hartrees.
    """

    rhf_mp2_pattern1 = (
        'MP2 energy [au]:' 
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) 
    )

    rhf_mp2_pattern2 = (
        'Total MP2 energy [au]:' 
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) 
    )

    return mp2_energy    

def rhf_ccsd_reader(output_string):
    """ Retrieves the RHF, UHF, or ROHF energy.
        Returns as a float. Units of Hartrees.
    """

    rhf_ccsd_pattern = (
    'Total CCSD energy [au]:' 
    rep.one_or_more(relib.WHITESPACE) +
    rep.one_or_more(relib.FLOAT) 
    )

    return ccsd_energy

def rhf_ccsd_t_reader(output_string):
    """ Retrieves the RHF, UHF, or ROHF energy.
        Returns as a float. Units of Hartrees.
    """

    rhf_ccsd_t_pattern = (
        'CCSD(T) total energy [au]:' 
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) 
    )

    return ccsd_t_energy

def rhf_ccsdt_reader(output_string):
    """ Retrieves the RHF, UHF, or ROHF energy.
        Returns as a float. Units of Hartrees.
    """

    rhf_ccsdt_pattern = (
        'Total CCSDT energy [au]:' 
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) 
    )

    return ccsdt_energy

def rhf_ccsdt_q_reader(output_string):
    """ Retrieves the RHF, UHF, or ROHF energy.
        Returns as a float. Units of Hartrees.
    """

    rhf_ccsdt_q_pattern = (
        'Total CCSDT(Q) energy [au]:' 
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) 
    )

    return ccsdt_q_energy

ENERGY_READERS = {
    params.METHOD.RHF: hf_reader,
    params.METHOD.ROHF: hf_reader,
    params.METHOD.UHF: hf_reader,
}

##### Energy reader function called by external scripts #####

def energy(method, output_string):
    """ Calls the appropriate function to read in the energy
    """
    assert method in ENERGY_READERS.keys()

    energy = ENERGY_READERS[method](output_string)

    return energy
