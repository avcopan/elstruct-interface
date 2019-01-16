""" Script to run all of the tests for a given program
"""

__authors__ = "Kevin Moore"
__updated__ = "2019-01-13"

import os
import sys
#import elstruct
import subprocess

# Get the program and node from the user
program = 'molpro2015'
hostnode = 'b450'

# Build a list with all of the input files
input_files = os.listdir('.')

# Loop through each input file and run the file
for input_file in input_files:
    subprocess.check_call(['python', '/home/kmoore/elstruct-interface/submission/sblues.py', program, hostnode, '-i', input_file, '-b', 'no'])

