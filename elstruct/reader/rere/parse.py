""" set of parsers to return bits of info
"""

import find as ref
import pattern as rep
import pattern_lib as relib


##### HELPER FUNCTION TO RETRIEVE TEXT BLOCK  #####

def block(head_string, foot_string, string):
    """ Returns a block of text
    """
    head_pattern = rep.escape(head_string)
    foot_pattern = rep.escape(foot_string)
    block_pattern = rep.capturing(
        head_pattern + rep.one_or_more(relib.ANY_CHAR, greedy=False) +
        foot_pattern)
    return ref.last_capture(block_pattern, string)


##### Set of parser functions to return information from regex searching functions ####


def sing_float_from_string(pattern, output_string):
    """ Searches for pattern in output_string to capture a single value. 
        Returns the LAST instance of this value as a float.
    """
    
    # Capture the final energy in the output file
    energy_str = ref.last_capture(pattern, output_string)

    # Check if energy values is found, if so, convert to float
    energy_val = (None if energy_str is None else float(energy_str))

    return sing_float

def list_float_from_string(pattern, output_string):
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

    return list_float

def pattern_parser_1(pattern, output_string):
    """ xxxx.
    """

    # Obtain the xyz coordinates from the block
    struct_str = ref.all_captures(pattern, output_string)

    struct_val = (None if struct_str is None else '\n'.join(struct_str))

    return struct_val

def pattern_parser_2(pattern, output_string):
    """ xxxx.
    """

    # Obtain the xyz coordinates from the block
    struct_str = ref.all_captures(pattern, output_string)

    if struct_str is not None:
        struct_val_init = ['    '.join(elem) for elem in struct_str]
        struct_val = '\n'.join(struct_val_init)
    else:
        struct_val = None

    return struct_val

def pattern_parser_3(pattern, output_string):
    """ Searches for pattern in out_string to capture series of values.
        Return each instance of these values in a single list of floats.
    """

    # Locate the final energy in the output file
    struct_str = ref.last_capture(pattern, output_string)

    # Check if energy values is found, if so, convert to float
    if struct_str is not None:
        struct_val = [float(val.strip()) for string in struct_str for val in string.split()]
    else:
        struct_val = None

    return struct_val

