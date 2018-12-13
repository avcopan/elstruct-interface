import sys
import os
import subprocess

def sortfxn(string):
  return int(string.split('_')[0])

# Get the path to the directory containing all of the job directories
main_path = os.getcwd()+'/../'

# Obtain a sorted list of all of the job directories
job_dirs = os.listdir('.')
job_dirs.sort(key=sortfxn)

# Initialize a counter to control the submission limit
sub_count = 0

# Loop through the job directories, check to see if the job is submitted, if not, submit job
# Loop exits when 100 jobs have been submitted
for dir in job_dirs:
  if sub_count == 95:
    sys.exit()
  else:
    os.chdir(dir)
    if os.path.exists('./retry'):
      os.chdir('./retry')
      if os.path.exists('./run_orca4_bebop.sh') and os.path.exists('./output.dat'):
        os.chdir('../../')
      else:
        subprocess.call( ['sbatch', 'run_orca4_bebop.sh'] )
        sub_count = sub_count + 1
        os.chdir('../../')
    else:
      os.chdir('../')
