import os
import sys
import subprocess

def sortfxn(string):
  return int(string.split('_')[0])

# Get the job directories in a list
jobdirs = os.listdir('.')
jobdirs.sort(key=sortfxn)
      
# Loop through directories and grab everything
for dir in jobdirs:

  # Go into directory
  print(dir)
  os.chdir(dir)

  # Check if job needs to be redone and resubmit with changes 
  if os.path.exists('./output.dat'):
    
    # Read in the contents of the old input file and submisssion file
    with open('output.dat','r') as jobfile:
      out_lines = jobfile.readlines()      
    with open('input.dat','r') as jobfile:
      old_inp_lines = jobfile.readlines()      
    with open('run_orca4_bebop.sh','r') as subfile:
      old_sub_lines = subfile.readlines() 

    # Search for error messages to figure out how to rebuild files
    rebuild_mem = False
    rebuild_par = False
    for line in out_lines:
      if 'failed to add matrix to PNO4' in line or 'not enough memory for MDCI' in line:
        rebuild_mem = True
        break
    for line in out_lines:
      if 'Number of processes in parallel calculation exceeds number of pairs' in line:
        rebuild_par = True
        break

    # Rebuild files where memory was an issue
    if rebuild_mem == True:
      print('rebuild for mem')
      subprocess.call( ['mkdir', '-p', 'retry'] )
      os.chdir('retry')
      with open('input.dat','w') as new_infile:
        for line in old_inp_lines:
          if 'MaxCore' in line:
            new_infile.write('% MaxCore 25000\n')
          elif 'nprocs' in line:
            new_infile.write('% pal nprocs 4 end\n')
          else:
            new_infile.write(line)
      with open('run_orca4_bebop.sh','w') as new_subfile:
        for line in old_sub_lines:
          if '#SBATCH --ntasks-per-node' in line:
            new_subfile.write('#SBATCH --ntasks-per-node=4\n')
          else:
            new_subfile.write(line)
      os.chdir('../')
 
  
    # Rebuild files where parallelization was an issue
    if rebuild_par == True:
      print('rebuild for par')
      subprocess.call( ['mkdir', '-p', 'retry'] )
      os.chdir('retry')
      with open('input.dat','w') as new_infile:
        for line in old_inp_lines:
          if 'MaxCore' in line:
            new_infile.write('% MaxCore 25000\n')
          elif 'nprocs' in line:
            new_infile.write('% pal nprocs 1 end\n')
          else:
            new_infile.write(line)
      with open('run_orca4_bebop.sh','w') as new_subfile:
        for line in old_sub_lines:
          if '#SBATCH --ntasks-per-node' in line:
            new_subfile.write('#SBATCH --ntasks-per-node=1\n')
          else:
            new_subfile.write(line)
      os.chdir('../')

  # Return to main directory with each job
  os.chdir('../')
