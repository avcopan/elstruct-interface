import os
import sys
import subprocess
from series_molpro import write_lccsdt
#from series_orca import write_dlpno_ccsdt    ### Needs editing

# Read the structure file name from the user
infilename = sys.argv[1]

# Read in the structures from the desired structure file
with open(infilename,'r') as inputfile:
  data = inputfile.readlines() 

# Get the lines for each structure
mult_lines = []
for i in range(len(data)):
  if 'mult' in data[i]:
    mult_lines.append(int(i))

# Get the names and structs
names = []
mults = []
structs = []
for linenum in mult_lines:
  names.append(data[linenum-1].strip())
  mults.append(data[linenum].strip().split()[1])
  for j in range(linenum,linenum+100):
   if data[j].strip() == '':
      struct_end = j - 1
      break
  structs.append( [ data[k] for k in range(linenum+1,struct_end+1) ] )
    
# Create the job directories
count = 0
for i in range(len(names)):

  if count == 20:
    sys.exit()

  # Create and go into the directory
  os.mkdir(str(i+1)+'_'+names[i])
  os.chdir(str(i+1)+'_'+names[i])

  # Call the writer function
  write_lccsdt(structs[i], mults[i])

  # Return to main directory with each job
  os.chdir('../')
  
  count = count + 1


