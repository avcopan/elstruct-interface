"""
Library of functions to retrieve electronic energies from a Molpro 2015 output file.

Energies currently supported:
(1) RHF, ROHF, and UHF;
(2) RHF, ROHF, and UHF reference MP2, UMP2, RMP2, CCSD, UCCSD, RCCSD, CCSD(T), UCCSD(T), RCCSD(T);
(3) multireference CASSCF, CASPT2, icCASPT2, MRCISD_Q; and
(4) custom, user-defined energies.

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

def rhf_reader(output_string):
    """ Retrieves the RHF or ROHF energy.
        Returns as a float. Units of Hartrees.
    """

    # Set the string pattern to find the RHF energy
    rhf_pattern = (
        '!RHF STATE' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) +
        rep.one_or_more(relib.WHITESPACE) +
        'Energy' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    # Obtain the RHF energy
    rhf_energy = pattern_reader(rhf_pattern, output_string)

    return rhf_energy

def uhf_reader(output_string):
    """ Retrieves the UHF energy.
        Returns as a float. Units of Hartrees.
    """

    # Set the string pattern to find the UHF energy
    uhf_pattern = (
        '!UHF STATE' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) +
        rep.one_or_more(relib.WHITESPACE) +
        'Energy' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    # Obtain the UHF energy
    uhf_energy = pattern_reader(uhf_pattern, output_string)

    return uhf_energy

def rhf_mp2_reader(output_string):
    """ Retrieves the RHF-MP2 or RHF-UMP2 energy.
        Returns as a float. Units of Hartrees.
    """

    mp2_pattern = (
        'MP2 total energy:' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    ump2_pattern = (
        '!RHF-UMP2 energy' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    # Obtain the RHF-MP2 or RHF-UMP2 energy
    mp2_energy = pattern_reader(mp2_pattern, output_string)
    if mp2_energy is None:
        mp2_energy = pattern_reader(ump2_pattern, output_string)

    return mp2_energy

def uhf_ump2_reader(output_string):
    """ Retrieves the UHF-UMP2 energy.
        Returns as a float. Units of Hartrees.
    """

    mp2_pattern = (
        'MP2 total energy:' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    ump2_pattern = (
        '!UHF-UMP2 energy' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    # Obtain the UHF-MP2 energy
    mp2_energy = pattern_reader(mp2_pattern, output_string)
    if mp2_energy is None:
        mp2_energy = pattern_reader(ump2_pattern, output_string)

    return mp2_energy

def rohf_rmp2_reader(output_string):
    """ Retrieves the ROHF-RMP2 energy.
        Returns as a float. Units of Hartrees.
    """

    mp2_pattern = (
        'MP2 total energy:' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    rmp2_pattern = (
        '!RHF-RMP2 energy' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    # Obtain the ROHF-RMP2 energy
    mp2_energy = pattern_reader(mp2_pattern, output_string)
    if mp2_energy is None:
        mp2_energy = pattern_reader(rmp2_pattern, output_string)

    return mp2_energy

def rhf_rohf_ccsd_uccsd_reader(output_string):
    """ Retrieves the RHF-CCSD, RHF-UCCSD, or ROHF-UCCSD energy.
        Returns as a float. Units of Hartrees.
    """

    ccsd_pattern = (
        'CCSD total energy:' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    uccsd_pattern = (
        '!RHF-UCCSD energy' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    # Obtain the RHF-CCSD, RHF-UCCSD, ROHF-UCCSD energy
    ccsd_energy = pattern_reader(ccsd_pattern, output_string)
    if ccsd_energy is None:
        ccsd_energy = pattern_reader(uccsd_pattern, output_string)

    return ccsd_energy

def rohf_rccsd_reader(output_string):
    """ Retrieves the ROHF-RCCSD energy.
        Returns as a float. Units of Hartrees.
    """

    ccsd_pattern = (
        'CCSD total energy:' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    rccsd_pattern = (
        '!RHF-RCCSD energy' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    # Obtain the ROHF-RCCSD energy
    ccsd_energy = pattern_reader(ccsd_pattern, output_string)
    if ccsd_energy is None:
        ccsd_energy = pattern_reader(rccsd_pattern, output_string)

    return ccsd_energy

def rhf_rohf_ccsd_t_uccsd_t_reader(output_string):
    """ Retrieves the RHF-CCSD(T), RHF-UCCSD(T), or ROHF-UCCSD(T) energy.
        Returns as a float. Units of Hartrees.
    """

    ccsd_t_pattern = (
        'CCSD(T) total energy:' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    uccsd_t_pattern = (
        '!RHF-UCCSD(T) energy' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    # Obtain the RHF-CCSD(T), RHF-UCCSD(T), or ROHF-UCCSD(T) energy
    ccsd_t_energy = pattern_reader(ccsd_t_pattern, output_string)
    if ccsd_t_energy is None:
        ccsd_t_energy = pattern_reader(uccsd_t_pattern, output_string)

    return ccsd_t_energy

def rohf_rccsd_t_reader(output_string):
    """ Retrieves the ROHF-RCCSD(T) energy.
        Returns as a float. Units of Hartrees.
    """

    ccsd_t_pattern = (
        'CCSD total energy:' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    rccsd_t_pattern = (
        '!RHF-RCCSD(T) energy' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    # Obtain the ROHF-RCCSD(T) energy
    ccsd_t_energy = pattern_reader(ccsd_t_pattern, output_string)
    if ccsd_t_energy is None:
        ccsd_t_energy = pattern_reader(rccsd_t_pattern, output_string)

    return ccsd_t_energy

def casscf_reader(output_string):
    """ Retrieves the CASSCF energy.
        Returns as a float. Units of Hartrees.
    """

    # Set the string pattern to find the RHF energy
    casscf_pattern = (
        '!MCSCF STATE' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) +
        rep.one_or_more(relib.WHITESPACE) +
        'Energy' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    # Obtain the CASSCF energy
    casscf_energy = pattern_reader(casscf_pattern, output_string)

    return casscf_energy

def caspt2_reader(output_string):
    """ Retrieves the CASPT2/ic-CASPT2 energy.
        Returns as a float. Units of Hartrees.
    """

    # Set the string pattern to find the RHF energy
    caspt2_pattern = (
        '!RSPT2 STATE' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) +
        rep.one_or_more(relib.WHITESPACE) +
        'Energy' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    # Obtain the CASPT2/ic-CASPT2 energy
    casscf_energy = pattern_reader(caspt2_pattern, output_string)

    return casscf_energy

def mrcisd_q_reader(output_string):
    """ Retrieves the Davidson-corrected MRCISD energy.
        Returns as a float. Units of Hartrees.
    """

    # Set the string pattern to find the RHF energy
    mrcisd_q_pattern = (
        'Cluster corrected energies' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT) +
        rep.one_or_more(relib.WHITESPACE) +
        '(Davidson, fixed reference)'
    )

    # Obtain the CASPT2/ic-CASPT2 energy
    mrcisd_q_energy = pattern_reader(mrcisd_q_pattern, output_string)

    return mrcisd_q_energy

def custom_e_reader(output_string):
    """ Retrieves the custom energy.
        Returns as a float. Units of Hartrees.
    """

    # Set the string pattern to find the RHF energy
    custom_e_pattern = (
        'SETTING E_' +
        rep.capturing(relib.WHITESPACE) +
        '=' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )

    # Obtain the custom energy
    custom_energy = pattern_reader(custom_e_pattern, output_string)

    return custom_energy


##### Dictionary of functions to read the energies in the files #####

ENERGY_READERS = {
    params.METHOD.RHF: rhf_reader,
    params.METHOD.ROHF: rhf_reader,
    params.METHOD.UHF: uhf_reader,
    params.METHOD.RHF_MP2: rhf_mp2_reader,
    params.METHOD.UHF_UMP2: uhf_ump2_reader,
    params.METHOD.ROHF_RMP2: rohf_rmp2_reader,
    params.METHOD.RHF_CCSD: rhf_rohf_ccsd_uccsd_reader,
    params.METHOD.ROHF_UCCSD: rhf_rohf_ccsd_uccsd_reader,
    params.METHOD.ROHF_RCCSD: rohf_rccsd_reader,
    params.METHOD.RHF_CCSD_T: rhf_rohf_ccsd_t_uccsd_t_reader,
    params.METHOD.ROHF_UCCSD_T: rhf_rohf_ccsd_t_uccsd_t_reader,
    params.METHOD.ROHF_RCCSD_T: rohf_rccsd_t_reader,
    params.METHOD.CASSCF: casscf_reader,
    params.METHOD.CASPT2: caspt2_reader,
    params.METHOD.icCASPT2: caspt2_reader,
    params.METHOD.MRCISD_Q: mrcisd_q_reader,
    params.METHOD.CUSTOM: custom_e_reader,
}


##### Energy function called by external scripts which calls the Energy Reader Dictionary #####

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
