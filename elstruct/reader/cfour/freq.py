"""
Library of functions to retrieve frequency information from a CFour 2.0 output file.

Frequencies currently supported:
(1) Harmonic Vibrational Frequencies
(2) Harmonic Zero-Point Vibrational Energy

"""

__authors__ = "Kevin Moore, Andreas Copan"
__updated__ = "2019-01-15"

from ..rere import find as ref
from ..rere import pattern as rep
from ..rere import pattern_lib as relib
from ... import params


##### Series of functions to read the frequency information #####

def harm_vib_freqs_reader(output_string):
    """ Reads the harmonic vibrational frequencies from the output file.
        Returns the frequencies as a list of floats in cm-1.
    """

    freq_begin_pattern = 'Cartesian force constants:'
    freq_end_pattern = 'Zero-point energy:'

    freq_block = block(freq_begin_pattern,
                       freq_end_pattern,
                       output_string)

    freq_str_pat = (
        relib.INTEGER +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT + rep.maybe('i'))
    )
    
    # Obtain the frequencies for all degrees-of-freedom
    all_freqs = repar.list_float_from_string(harm_vib_freq_pattern, output_string)

    # Remove the zero frequencies
    vib_freqs = [freq for freq in all_freqs if freq != 0.0]

    return vib_freqs

def harm_zpve_reader(output_string):
    """ Reads the harmonic zero-point vibrational energy (ZPVE) from the output file.
        Returns the ZPVE as a float; in Hartrees.
    """

    zpve_pattern = (
        'Zero-point energy:' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
        'kcal/mol' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) +
        'kJ/mol' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.one_or_more(relib.FLOAT) +
        'cm-1'
    )

    # Obtain the ZPVE
    harm_zpve = repar.sing_float_from_string(zpve_pattern, output_string)

    return harm_zpve


##### Dictionary of functions to read frequency information in the files #####

FREQUENCY_READERS = {
    params.FREQUENCY.HARM_FREQ : harm_vib_freqs_reader,
    params.FREQUENCY.HARM_ZPVE : harm_zpve_reader
}


##### Frequency reader function called by external scripts #####

def frequency(freq, output_string):
    """ Returns a freq thing.
    """

    assert freq in FREQUENCY_READERS.keys()

    frequency = FREQUENCY_READERS[freq](output_string)

    return frequency
