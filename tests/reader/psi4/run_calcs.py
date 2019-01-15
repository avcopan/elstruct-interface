""" Script to run all of the tests for Orca4
"""

__authors__ = "Kevin Moore"
__updated__ = "2019-01-13"

import os
import sys
#import elstruct
import subprocess

# Build a list with all of the input files
input_files = os.listdir('.')

# Loop through each input file and run the file
for input_file in input_files:
    output_file = input_file.split('.')[0] + '.out'
    print(output_file)
    subprocess.check_call(['psi4', '-i', input_file, '-o', output_file])

