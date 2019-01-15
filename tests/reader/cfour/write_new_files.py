""" Script to generate new files from a simple RHF/UHF/ROHF/DFT files of Orca4
"""

__authors__ = "Kevin Moore"
__updated__ = "2019-01-13"

import os
import sys
import subprocess

# Line to change
OLD_FILES = {
    'rhf' : ['CALC=HF', 'rhf.inp'],
    'uhf' : ['CALC=HF', 'uhf.inp'],
    'rohf' : ['CALC=HF', 'rohf.inp']
}

# List of list where 
# elem 0 is new string to write
# elem 1 is new file name
NEW_FILES = {
    'rhf' : [
             ['CALC=MP2\n', 'rhf-mp2.inp'],
             ['CALC=CCSD\nCC_PROG=ECC\nABCDTYPE=AOBASIS\n', 'rhf-ccsd.inp'],
             ['CALC=CCSD(T)\nCC_PROG=ECC\nABCDTYPE=AOBASIS\n', 'rhf-ccsd_t.inp'],
             ['CALC=CCSDT\nCC_PROG=NCC\nABCDTYPE=AOBASIS\n', 'rhf-ccsdt.inp'],
             ['CALC=CCSDT(Q)\nCC_PROG=NCC\nABCDTYPE=AOBASIS\n', 'rhf-ccsdt_q.inp']
    ],
    'uhf' : [
             ['CALC=MP2\n', 'uhf-mp2.inp'],
             ['CALC=CCSD\nCC_PROG=ECC\nABCDTYPE=AOBASIS\n', 'uhf-ccsd.inp'],
             ['CALC=CCSD(T)\nCC_PROG=ECC\nABCDTYPE=AOBASIS\n', 'uhf-ccsd_t.inp']
    ],    
    'rohf' : [
             ['CALC=MP2\n', 'rohf-mp2.inp'],
             ['CALC=CCSD\nCC_PROG=VCC\nABCDTYPE=AOBASIS\n', 'rohf-ccsd.inp'],
             ['CALC=CCSD(T)\nCC_PROG=VCC\nABCDTYPE=AOBASIS\n', 'rohf-ccsd_t.inp']
    ]    
}

# Common keywords
#JOBTYPE = 'sp'
#COMMENT = 'CFOUR 2.0 Computation'
#BASIS = '6-31G*'
#CHARGE = 0
#UNITS = 'ANGSTROM'
#COORDS = 'CARTESIAN'
    #if ref == 'rhf_energy':
    #    GEOMETRY = 'O  0.0000000000  -0.0530229169  0.0000000000\nH  0.0000000000   0.5556614584  -0.7504910643\nH  0.0000000000   0.5556614584   0.7504910643\n\n'
    #    OPT_TYPE = 'SINGLE_POINT'
    #    VIBRATION = '0'
    #    CALC = 'HF'
    #    CCPROG = 'ECC'
    #    REFERENCE = 'RHF'
    #    SPIN = 3

# Loop through each input file and run the file
for ref in OLD_FILES.keys():
 
    # Loop through all the desired changes
    for i in range(len(NEW_FILES[ref])):
  
        # Set the old file name and new file name
        old_file_name = OLD_FILES[ref][1] 
        new_file_name = NEW_FILES[ref][i][1] 
        print(new_file_name)

        # Set the old method string and new method string
        old_file_str = OLD_FILES[ref][0] 
        new_file_str = NEW_FILES[ref][i][0] 

        # Empty list of lines for the loop
        old_file_lines = []
        new_file_lines = []
 
        # Read the contents of the original file
        with open(old_file_name, 'r') as old_file:
            old_file_lines = old_file.readlines()
    
        # Loop through the lines of the original file building a list of lines for the new file
        for line in old_file_lines:
            # If the line to change (line1) in current loop add altered line (line2) 
            if old_file_str in line:
                new_file_lines.append(new_file_str)
            # Otherwise just add the current line
            else:
                new_file_lines.append(line)

        # Write new file with the new lines (including the line change)
        with open(new_file_name, 'w') as new_file:
            for line in new_file_lines:
                new_file.writelines(line) 

