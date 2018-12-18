import os
import sys
import subprocess

def sortfxn(string):
  return int(string.split('_')[0])

# Get the job directories in a list
job_dirs = os.listdir('.')
if os.path.exists('./energies.dat'):
  job_dirs.remove('energies.dat')
if os.path.exists('./times.dat'):
  job_dirs.remove('times.dat')
job_dirs.sort(key=sortfxn)
      
# Loop through directories and grab everything
for dir in job_dirs:

  # Go into directory
  print(dir)
  os.chdir(dir)

  # Make the 5Z directory
  os.mkdir('5Z')
  os.chdir('5Z')

  # Read in the contents of the old input file and submisssion file
  with open('../input.dat','r') as jobfile:
    old_inp_lines = jobfile.readlines()      

  # Write new file with 5Z
  with open('input.dat','w') as new_infile:
    for i in range(len(old_inp_lines)):
      if 'basis=cc-pVDZ' in old_inp_lines[i]:
        new_infile.write('basis=cc-pV5Z\n')
        new_infile.write(old_inp_lines[i+1])
        new_infile.write(old_inp_lines[i+2])
        new_infile.write('e5z = energy\n\n')
        break
      else:
        new_infile.write(old_inp_lines[i])
  
  # Go up to DZ-QZ part of dir
  os.chdir('../../')

