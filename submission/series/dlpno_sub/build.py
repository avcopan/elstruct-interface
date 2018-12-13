import os
import sys
import subprocess

# Read the structure file name from the user
infilename = sys.argv[1]
outdir = sys.argv[2]

# Read in the structures from the desired structure file
with open(infilename,'r') as inputfile:
  data = inputfile.readlines() 

# Make major directory
subprocess.call(['mkdir','-p',outdir])
os.chdir(outdir)

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
    reference = 'RHF'
  else:
    reference = 'UHF'

  # Set the basis sets reset for augmented basis sets
  basis_sets = ['cc-pVDZ cc-pVDZ/C', 'cc-pVTZ cc-pVTZ/C', 'cc-pVQZ cc-pVQZ/C', 'cc-pV5Z cc-pV5Z/C']

  # Write the Orca input file
  with open('input.dat','w') as orcafile:
    for j in range(len(basis_sets)): 
      orcafile.write('''#{0}
% pal nprocs 8 end
% MaxCore 12500
! {1} DLPNO-CCSD(T) RIJCOSX GridX5   
! {2} AutoAux
! TightSCF TightPNO
%base"/scratch/kmoore/test{3}" 
* xyz 0 {4}\n'''.format(names[i],reference,basis_sets[j],str(j),mults[i]))
      for k in range(len(structs[i])):
        orcafile.writelines(structs[i][k])
      if j != (len(basis_sets) - 1):
        orcafile.write('*\n$new_job\n')
      else:
        orcafile.write('*\n')

  # Return to main directory with each job
  os.chdir('../')
