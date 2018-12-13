import os
import sys
import subprocess

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
for i in range(len(names)):

  # Create and go into the directory
  os.mkdir(str(i+1)+'_'+names[i])
  os.chdir(str(i+1)+'_'+names[i])

  # Set the reference via the multiplicity (need to change if ROHF wanted)
  if mults[i] == '1':
    method = 'df-lccsd(t)'
  else:
    method = 'df-luccsd(t)'

  # Write the Orca input file
  with open('input.dat','w') as orcafile:
    orcafile.write('''memory,950,m
gthresh,energy=1.0d-10,orbital=1.0d-10

nosym
angstrom
Geometry = {\n''')
    for k in range(len(structs[i])):
      orcafile.writelines(structs[i][k])
    orcafile.write('''}}

set,charge=0
set,spin={0}

basis=cc-pVDZ
{{df-rhf,maxit=300}}
{{{1},maxit=150}}
edz = energy

basis=cc-pVTZ
{{df-rhf,maxit=300}}
{{{1},maxit=150}}
etz = energy

basis=cc-pVQZ
{{df-rhf,maxit=300}}
{{{1},maxit=150}}
eqz = energy

basis=cc-pV5Z
{{df-rhf,maxit=300}}
{{{1},maxit=150}}
e5z = energy

show,edz
show,etz
show,eqz
show,e5z

'''.format(str(int(mults[i])-1),method) )

  # Return to main directory with each job
  os.chdir('../')
