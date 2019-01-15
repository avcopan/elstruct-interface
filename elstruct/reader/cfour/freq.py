""" Vibrational properties
"""

__authors__ = "Kevin Moore, Andreas Copan"
__updated__ = "2019-01-11"

from ..rere import find as ref
from ..rere import pattern as rep
from ..rere import pattern_lib as relib
from ... import params

##### HELPER FUNCTION TO RETRIEVE TEXT BLOCK; TODO: Move to rere library #####

def block(head_string, foot_string, string):
    """ Returns a block of text
    """
    head_pattern = rep.escape(head_string)
    foot_pattern = rep.escape(foot_string)
    block_pattern = rep.capturing(
        head_pattern + rep.one_or_more(relib.ANY_CHAR, greedy=False) +
        foot_pattern)
    return ref.last_capture(block_pattern, string)


##### Patterns #####

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
