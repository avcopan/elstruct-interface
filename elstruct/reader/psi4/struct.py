"""
Library of functions to retrieve structural information from a Psi4 output file

"""

__authors__ = "Kevin Moore, Andreas Copan"
__updated__ = "2019-01-14"

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
    """ xxxx.
    """

    # Obtain the xyz coordinates from the block
    struct_str = ref.all_captures(pattern, output_string)

    struct_val = (None if struct_str is None else '\n'.join(struct_str))

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

def opt_geom_xyz_reader(output_string):
    """ Retrieves the optimized geometry in Cartesian xyz coordinates.
        Units of Angstrom.
    """

    # Pattern to idetify block of output string where optimized geometry is located
    opt_geom_xyz_begin_pattern = 'Final (previous) structure:'
    opt_geom_xyz_end_pattern = 'Saving final (previous) structure'

    # Obtain block of output string containing the optimized geometry in xyz coordinates
    opt_geom_xyz_block = block(opt_geom_xyz_begin_pattern,
                               opt_geom_xyz_end_pattern,
                               output_string)

    # Pattern for the xyz coordinate of each atom
    opt_geom_xyz_pattern = (
        rep.capturing(
            relib.UPPERCASE_LETTER +
            rep.one_or_more(relib.WHITESPACE) +
            relib.FLOAT +
            rep.one_or_more(relib.WHITESPACE) +
            relib.FLOAT +
            rep.one_or_more(relib.WHITESPACE) +
            relib.FLOAT
        )
    )

    # Obtain the xyz coordinates from the block
    opt_geom_xyz = pattern_parser_1(opt_geom_xyz_pattern, opt_geom_xyz_block)

    return opt_geom_xyz

def opt_geom_internal_reader(output_string):
    """ Retrieves the optimized geometry in internal coordinates.
        Units of Angstrom and degrees.
        TODO Grab stuff for the initial coords
    """

    # internal coords of optimized geom
    opt_geom_internal_begin_pattern = 'OPTKING Finished Execution'
    opt_geom_internal_end_pattern = 'Removing binary optimization data file.'

    # Obtain block of output string containing the optimized geometry in xyz coordinates
    opt_geom_internal_block = block(opt_geom_internal_begin_pattern,
                                    opt_geom_internal_end_pattern,
                                    output_string)

    # Pattern for the xyz coordinate of each atom
    opt_geom_zmat_pattern = (
        rep.capturing(
            rep.one_or_more(relib.UPPERCASE_LETTER) +
            rep.one_or_more(relib.DIGIT) +
            '=' +
            rep.one_or_more(relib.WHITESPACE) +
            relib.FLOAT
        )
    )

    opt_geom_coords_pattern - (
        rep.capturing(
            rep.one_or_more(relib.ANY_CHAR) +
            rep.one_or_more(relib.WHITESPACE) +
            '=' +
            rep.one_or_more(relib.WHITESPACE) +
            relib.FLOAT
        )
    )

    # Obtain the xyz coordinates from the block
    opt_geom_zmat = pattern_parser_1(opt_geom_internal_pattern, opt_geom_internal_block)
    opt_geom_coords = pattern_parser(opt_geom_coords_pattern, opt_geom_internal_block)


    # Combine the two together

    return opt_geom_internal

def equil_rot_constant_reader(output_string):
    """ Retrieves the equilibrium rotational constant of the optimized geometry.
        Units of cm-1.
    """

    equil_rot_const_pattern = (
        'Rotational constants:' +
        rep.one_or_more(relib.WHITESPACE) +
        'A =' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT) +
        rep.one_or_more(relib.WHITESPACE) +
        'B =' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT) +
        rep.one_or_more(relib.WHITESPACE) +
        'C =' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT) +
        rep.one_or_more(relib.WHITESPACE) +
        '\[cm^-1\]'
    )

    # Obtain equil_const string
    all_rot_consts = pattern_parser_3(equil_rot_const_pattern, output_string)

    # Remove any instances of 0.0000s as well as duplicates
    equil_rot_const = list(set([const for const in all_rot_consts if const != 0.0]))

    return equil_rot_const

##### Dictionary for strings to find the geometries in the files #####

STRUCTURE_READERS = {
    params.STRUCTURE.OPT_GEOM_XYZ: opt_geom_xyz_reader,
    params.STRUCTURE.OPT_GEOM_INT: opt_geom_internal_reader,
    params.STRUCTURE.EQUIL_ROT_CONST: equil_rot_constant_reader,
}


##### Structure function called by external scripts #####

def structure(struct, output_string):
    """ Calls the appropriate function to read in the energy
    """

    assert struct in STRUCTURE_READERS.keys()

    struct = STRUCTURE_READERS[struct](output_string)

    return struct
