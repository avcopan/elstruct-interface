""" Test the electronic energy from several different Molpro jobs.
"""

import numpy
import elstruct
import importlib
from elstruct.params import METHOD

# Program to test
PROGRAM = 'molpro'

# Theories to test
THEORIES = [
    METHOD.RHF,
    METHOD.UHF,
    METHOD.ROHF,
    METHOD.RHF_MP2,
    METHOD.UHF_UMP2,
    METHOD.ROHF_RMP2,
    METHOD.RHF_CCSD,
    METHOD.ROHF_UCCSD,
    METHOD.ROHF_RCCSD,
    METHOD.RHF_CCSD_T,
    METHOD.ROHF_UCCSD_T,
    METHOD.ROHF_RCCSD_T
]


def test__energy():
    """ Reads the energy from the output file and compares to a given values.
    """

    # Get a theory method
    for THEORY in THEORIES:

        # Change parentheses in the theory name for file reading
        THEORY_FILE = './calcs/'+ THEORY.replace('(','_').replace(')','') + '.out'

        # Open the file
        with open(THEORY_FILE, 'r') as outfile:
            OUTPUT_STR = outfile.read()

        # Set the reader module to user the reader for the desired program
        reader_module = importlib.import_module('elstruct.reader.'+PROGRAM)

        # Use the reader module to obtain the energy value
        ENERGY = reader_module.energy(THEORY, OUTPUT_STR)
        #print(THEORY + '\t' +str(ENERGY))

        # Set values of the test energy
        if THEORY == METHOD.RHF:
            ecomp = -76.008350415635
        elif THEORY == METHOD.UHF:
            ecomp = -38.378808076235
        elif THEORY == METHOD.ROHF:
            ecomp = -38.915219602947
        elif THEORY == METHOD.RHF_MP2:
            ecomp = -76.193792345214
        elif THEORY == METHOD.UHF_UMP2:
            ecomp = -38.491613632745
        elif THEORY == METHOD.ROHF_RMP2:
            ecomp = -39.001040622628
        elif THEORY == METHOD.RHF_CCSD:
            ecomp = -76.203026494077
        elif THEORY == METHOD.ROHF_UCCSD:
            ecomp = -39.019955499482
        elif THEORY == METHOD.ROHF_RCCSD:
            ecomp = -39.019816454488
        elif THEORY == METHOD.RHF_CCSD_T:
            ecomp = -76.204810205863
        elif THEORY == METHOD.ROHF_UCCSD_T:
            ecomp = -39.021374161079
        elif THEORY == METHOD.ROHF_RCCSD_T:
            ecomp = -39.021254228020

        # Test the energy
        assert numpy.isclose(ENERGY, ecomp, atol=1e-4)


if __name__ == '__main__':
    test__energy()
