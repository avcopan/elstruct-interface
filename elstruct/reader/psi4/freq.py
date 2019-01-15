""" 
Library of functions to retrieve frequency information from a Psi4 output file.

"""

__authors__ = "Kevin Moore, Andreas Copan"
__updated__ = "2019-01-14"

from ..rere import find as ref
from ..rere import pattern as rep
from ..rere import pattern_lib as relib
from ... import params


##### Series of functions to read the frequency information #####

def pattern_parser_1(pattern, output_string):
    """ Searches for pattern in output_string to capture a single value. 
        Returns the LAST instance of this value as a float.
    """

    # Locate the final energy in the output file
    freq_str = ref.last_capture(pattern, output_string)

    # Check if energy values is found, if so, convert to float
    freq_val = (None if freq_str is None else float(freq_str))

    return freq_val


def harm_vib_freqs_reader(output_string):
    """ Reads the harmonic vibrational frequencies from the output file.
        Returns the frequencies as a list of floats in cm-1.
    """

    # Pattern to locate all frequencies in a string
    harm_vib_freq_pattern = (
        'Freq \[cm^-1\]' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(
            rep.one_or_more(relib.FLOAT + 
            rep.one_or_more(relib.WHITESPACE))
        )
    )


def harm_zpve_reader(output_string):
    """ Reads the harmonic zero-point vibrational energy (ZPVE) from the output file.
        Returns the ZPVE as a float; in Hartrees.
    """

    # String pattern to retrieve the ZPVE
    zpve_pattern = (
        'Vibrational ZPE' +
        rep.one_or_more(relib.WHITESPACE) + 
        relib.FLOAT +
        rep.one_or_more(relib.WHITESPACE) + 
        '\[kcal/mol\]' +
        rep.one_or_more(relib.WHITESPACE) + 
        relib.FLOAT +
        rep.one_or_more(relib.WHITESPACE) + 
        '\[kJ/mol\]' +
        rep.one_or_more(relib.WHITESPACE) +
        relib.FLOAT +
        rep.one_or_more(relib.WHITESPACE) +
        '\[Eh\]'
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT) +
        rep.one_or_more(relib.WHITESPACE) +
        '\[cm^-1\]'
    )

    # Obtain the ZPVE
    harm_zpve = pattern_parser_1(zpve_pattern, output_string)

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
