""" 
Library of functions to retrieve frequency information from a Molpro 2015 output file.

Frequencies currently supported:
(1) Harmonic Vibrational Frequencies
(2) Harmonic Zero-Point Vibrational Energy

"""

__authors__ = "Kevin Moore, Andreas Copan"
__updated__ = "2019-01-14"

from ..rere import find as ref
from ..rere import pattern as rep
from ..rere import pattern_lib as relib
from ... import params


##### Series of functions to read the frequency information #####

def pattern_parser_2(pattern, output_string):
    """ Searches for pattern in out_string to capture series of values.
        Return each instance of these values in a single list of floats.  
    """

    # Locate the final energy in the output file
    freq_str = ref.all_captures(pattern, output_string)

    # Check if energy values is found, if so, convert to float
    if freq_str is not None:
        freq_val = [float(val.strip()) for string in freq_str for val in string.split()]
    else:
        freq_val = None

    return freq_val

def harm_vib_freqs_reader(output_string):
    """ Reads the harmonic vibrational frequencies from the output file.
        Returns the frequencies as a list of floats in cm-1.
    """

    harm_vib_freq_pattern = (
        'Frequencies --' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(
            rep.one_or_more(relib.FLOAT + 
            rep.one_or_more(relib.WHITESPACE))
        )
    )

    # Obtain the frequencies for all degrees-of-freedom
    all_freqs = pattern_parser_2(harm_vib_freq_pattern, output_string)
    
    # Remove the zero frequencies
    vib_freqs = [freq for freq in all_freqs if freq != 0.0]

    return vib_freqs

def harm_zpve_reader(output_string):
    """ Reads the harmonic zero-point vibrational energy (ZPVE) from the output file.
        Returns the ZPVE as a float; in Hartrees.
    """

    harm_zpve_pattern_1 = ( 
        'Zero-point correction=' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) 
        '(Hartree/Particle)' 
    )

    return harm_zpve

def anharm_zpve_reader(output_string):
    """ Reads the anharmonic zero-point vibrational energy (ZPVE) from the output file.
        Returns the ZPVE as a float; in Hartrees.
    """
 
    anharm_zpve_pattern = ( 
        'ZPE(harm) =' +
        FLOAT +
        D-02 +
        'KJ/mol' +
        'ZPE(anh) =' +
        FLOAT +
        D-02 +
        'KJ/mol' 
    )

    return anharm_zpve



