""" Script to change the lines for the input files of Orca4
"""

__authors__ = "Kevin Moore"
__updated__ = "2019-01-13"

import os
import sys
import subprocess


# Lines to change
old_file_list = [
    '# Running OrCa',
    'pal nprocs 8 end',
    'MaxCore 8000'
]
new_file_list = [
    '# Orca4 Single Point Energy Computation\n',
    'pal nprocs 1 end\n',
    'MaxCore 1000\n'
]


# Build a list with all of the input files
input_files = os.listdir('.')

# Loop through each input file and run the file
for input_file in input_files:
 
    # Loop through all the desired changes
    for i in range(len(old_file_list)):
  
        # Empty list of lines for the loop
        old_file_lines = []
        new_file_lines = []
 
        # Read the contents of the original file
        with open(input_file, 'r') as old_file:
            old_file_lines = old_file.readlines()
    
        # Loop through the lines of the original file building a list of lines for the new file
        for line in old_file_lines:
            # If the line to change (line1) in current loop add altered line (line2) 
            if old_file_list[i] in line:
                new_file_lines.append(new_file_list[i])
            # Otherwise just add the current line
            else:
                new_file_lines.append(line)

        # Write new file with the new lines (including the line change)
        with open(input_file, 'w') as new_file:
            for line in new_file_lines:
                new_file.writelines(line) 

