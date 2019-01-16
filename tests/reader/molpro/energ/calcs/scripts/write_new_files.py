""" Script to generate new files from a simple RHF/UHF/ROHF/DFT file
"""

__authors__ = "Kevin Moore"
__updated__ = "2019-01-13"

import os
import sys
import subprocess


# Line to change
OLD_FILES = {
    'rhf' : ['{rhf}', 'rhf.inp'],
    'uhf' : ['{uhf}', 'uhf.inp'],
    'rohf' : ['{rhf}', 'rohf.inp']
}

# List of list where 
# elem 0 is new string to write
# elem 1 is new file name
NEW_FILES = {
    'rhf' : [
             ['{rhf}\n{mp2}\n', 'rhf-mp2.inp'],
             ['{rhf}\n{ccsd}\n', 'rhf-ccsd.inp'],
             ['{rhf}\n{ccsd(t)}\n', 'rhf-ccsd_t.inp']
    ],
    'uhf' : [
             ['{uhf}\n{ump2}\n', 'uhf-ump2.inp']
    ],    
    'rohf' : [
              ['{rhf}\n{rmp2}\n', 'rohf-rmp2.inp'],
              ['{rhf}\n{rccsd}\n', 'rohf-rccsd.inp'],
              ['{rhf}\n{rccsd(t)}\n', 'rohf-rccsd_t.inp'],
              ['{rhf}\n{uccsd}\n', 'rohf-uccsd.inp'],
              ['{rhf}\n{uccsd(t)}\n', 'rohf-uccsd_t.inp']
    ]    
}


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
