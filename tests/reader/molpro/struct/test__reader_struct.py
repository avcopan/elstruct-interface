import numpy
import elstruct
import importlib
from elstruct.params import STRUCTURE

# Program to test
PROGRAM = 'molpro'

STRUCTS = [
    STRUCTURE.OPT_GEOM_XYZ,
    STRUCTURE.OPT_GEOM_INT,
    STRUCTURE.INIT_GEOM_XYZ,
    STRUCTURE.EQUIL_ROT_CONST
]


def test__struct():
    """ Test the electronic energy from several different Molpro jobs.
    """

    # Change parentheses in the theory name for file reading
    THEORY_FILE = 'output.dat'

    # Open the file
    with open(THEORY_FILE, 'r') as outfile:
        OUTPUT_STR = outfile.read()

    # Set the reader module to user the reader for the desired program
    reader_module = importlib.import_module('elstruct.reader.'+PROGRAM)

    for STRUCT in STRUCTS:

        print(STRUCT)

        # Use the reader module to obtain the energy value
        VAL = reader_module.structure(STRUCT, OUTPUT_STR)
        print(VAL)

if __name__ == '__main__':
    test__struct()
