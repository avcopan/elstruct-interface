""" Script to generate new files from a simple RHF/UHF/ROHF/DFT files of Orca4
"""

__authors__ = "Kevin Moore"
__updated__ = "2019-01-13"

import os
import sys
import subprocess


# Line to change
OLD_FILES = {
    'rhf' : ["energy('scf')", 'rhf.inp'],
    'uhf' : ["energy('scf')", 'uhf.inp'],
    'rohf' : ["energy('scf')", 'rohf.inp'],
}

# List of list where 
# elem 0 is new string to write
# elem 1 is new file name
NEW_FILES = {
    'rhf' : [
             ["energy('mp2')", 'rhf-mp2.inp'],
             ["energy('ccsd')", 'rhf-ccsd.inp'],
             ["energy('ccsd(t)')", 'rhf-ccsd_t.inp'],
             ["energy('wb97x-d')", 'wb97xd.inp'],
             ["energy('m06-2x')", 'm062x.inp'],
             ["energy('b2plyp-d3bj')", 'b2plyld3.inp'],
    ],
    'uhf' : [
             ["energy('mp2')", 'uhf-mp2.inp'],
             ["energy('ccsd')", 'uhf-ccsd.inp'],
             ["energy('ccsd(t)')", 'uhf-ccsd_t.inp'],
    ],    
    'rohf' : [
             ["energy('mp2')", 'rohf-mp2.inp'],
             ["energy('ccsd')", 'rohf-ccsd.inp'],
             ["energy('ccsd(t)')", 'rohf-ccsd_t.inp'],
    ]    
}


# Build a list with all of the input files
input_files = os.listdir('.')

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


