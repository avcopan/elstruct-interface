import numpy
import elstruct
import importlib
from elstruct.params import FREQUENCY

# Program to test
PROGRAM = 'molpro'

FREQS = [
    FREQUENCY.HARM_FREQ,
    FREQUENCY.HARM_ZPVE
]

def test__freq():
    """ Test the frequency information from several different Molpro jobs.
    """

    # Change parentheses in the theory name for file reading
    THEORY_FILE = 'output.dat'

    # Open the file
    with open(THEORY_FILE, 'r') as outfile:
        OUTPUT_STR = outfile.read()

    # Set the reader module to user the reader for the desired program
    reader_module = importlib.import_module('elstruct.reader.'+PROGRAM)

    for FREQ in FREQS:

        print(FREQ)

        # Use the reader module to obtain the energy value
        VAL = reader_module.frequency(FREQ, OUTPUT_STR)

        print(VAL)

if __name__ == '__main__':
    test__freq()
