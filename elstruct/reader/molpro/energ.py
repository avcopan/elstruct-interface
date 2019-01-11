"""
Library of functions to retrieve electronic energies from a Molpro 2015 output file

Energies currently supported: 
RHF, UHF, RHF_MP2, UHF_MP2, RHF_RMP2, RHF_CCSD, RHF_RCCSD, RHF_CCSD(T), RHF_RCCSD(T), 
CASSCF, CASPT2, icCASPT2, MRCISD_Q,
CUSTOM

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
    
    # Check if energy is found, if so, convert to float
    energy = ( None if energy_str is None else float(energy_str) )    

    return energy
    
def rhf_reader(output_string):
    """ Returns the RHF energy as a float. 
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
    """ Returns the UHF energy as a float. 
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
    """ Returns the RHF-MP2/RHF-UMP2 energy as a float. 
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
    
    # Obtain the MP2 energy
    mp2_energy = pattern_reader(mp2_pattern, output_string)
    if mp2_energy is None:
        mp2_energy = pattern_reader(ump2_pattern, output_string)

    return mp2_energy

def uhf_mp2_reader(output_string):
    """ Returns the UHF-MP2 energy as a float. 
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
    
    # Obtain the MP2 energy
    mp2_energy = pattern_reader(mp2_pattern, output_string)
    if mp2_energy is None:
        mp2_energy = pattern_reader(ump2_pattern, output_string)

    return mp2_energy

def rhf_rmp2_reader(output_string):
    """ Returns the RHF-MP2 energy as a float. 
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
    
    # Obtain the MP2 energy
    mp2_energy = pattern_reader(mp2_pattern, output_string)
    if mp2_energy is None:
        mp2_energy = pattern_reader(rmp2_pattern, output_string)

    return mp2_energy

def rhf_ccsd_reader(output_string):
    """ Returns the RHF-CCSD/RHF-UCCSD energy as a float. 
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
    
    # Obtain the RHF-CCSD energy
    ccsd_energy = pattern_reader(ccsd_pattern, output_string)
    if ccsd_energy is None:
        ccsd_energy = pattern_reader(uccsd_pattern, output_string)

    return ccsd_energy

def rhf_rccsd_reader(output_string):
    """ Returns the RHF-RCCSD energy as a float. 
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
    
    # Obtain the RHF-RCCSD energy
    ccsd_energy = pattern_reader(ccsd_pattern, output_string)
    if ccsd_energy is None:
        ccsd_energy = pattern_reader(rccsd_pattern, output_string)

    return ccsd_energy

def rhf_ccsd_t_reader(output_string):
    """ Returns the RHF-CCSD(T)/RHF-UCCSD(T) energy as a float. 
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
    
    # Obtain the RHF-CCSD(T) energy
    ccsd_t_energy = pattern_reader(ccsd_t_pattern, output_string)
    if ccsd_t_energy is None:
        ccsd_t_energy = pattern_reader(uccsd_t_pattern, output_string)

    return ccsd_t_energy

def rhf_rccsd_t_reader(output_string):
    """ Returns the RHF-RCCSD(T) energy as a float. 
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
    
    # Obtain the RHF-RCCSD(T) energy
    ccsd_t_energy = pattern_reader(ccsd_t_pattern, output_string)
    if ccsd_t_energy is None:
        ccsd_t_energy = pattern_reader(rccsd_t_pattern, output_string)

    return ccsd_t_energy

def casscf_reader(output_string):
    """ Returns the CASSCF energy as a float. 
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
    """ Returns the CASPT2/ic-CASPT2 energy as a float. 
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
    """ Returns the Davidson-corrected MRCI energy as a float. 
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
    mrcisd_q__energy = pattern_reader(mrcisd_q_pattern, output_string)

    return mrcisd_q_energy

def custom_e_reader(output_string):
    """ Returns the custom energy as a float. 
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
    params.METHOD.UHF: uhf_reader,
    params.METHOD.RHF_MP2: rhf_mp2_reader,
    params.METHOD.UHF_MP2: uhf_mp2_reader,
    params.METHOD.RHF_RMP2: rhf_rmp2_reader,
    params.METHOD.RHF_CCSD: rhf_ccsd_reader,
    params.METHOD.RHF_RCCSD: rhf_rccsd_reader,
    params.METHOD.RHF_CCSD_T: rhf_ccsd_t_reader,
    params.METHOD.RHF_RCCSD_T: rhf_rccsd_t_reader,
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
        output_str = outfile.read()
    print( energy('rmp2', output_str) )    

