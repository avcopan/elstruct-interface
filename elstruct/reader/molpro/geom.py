"""
Library of functions to retrieve structural information from a Molpro 2015 output file

Geometries currently supported: 
(1) Final Geometry in Cartesian (xyz) 
(2) Final Geometry in Internal Coordinates
(3) Equilibrium Rotational Constants 

"""

__authors__ = "Kevin Moore, Andreas Copan"
__updated__ = "2019-01-11"

from ..rere import find as ref
from ..rere import pattern as rep
from ..rere import pattern_lib as relib


##### HELPER FUNCTION TO RETRIEVE TEXT BLOCK; TODO: Move to rere library #####

def block(head_string, foot_string, string):
    head_pattern = rep.escape(head_string)
    foot_pattern = rep.escape(foot_string)
    block_pattern = rep.capturing(
        head_pattern + rep.one_or_more(relib.ANY_CHAR, greedy=False) +
        foot_pattern)
    return ref.last_capture(block_pattern, string)


##### Dictionary for strings to find the energies in the files #####

STRUCTURE_READERS = {
    GEOM_XYZ: geom_xyz_reader,
    GEOM_INT: geom_internal_reader,
    EQUIL_ROT_CONST: equil_rot_const_reader,
}

##### For lazy testing #####

if __name__ == '__main__':
    STRING = open('output.dat').read()
    print(block('Current geometry', '***********', STRING))
