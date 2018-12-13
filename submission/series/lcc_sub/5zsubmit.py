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

# Initialize a counter to control the submission limit
sub_count = 0
      
# Loop through the job directories, check to see if the job is submitted, if not, submit job
# Loop exits when 100 jobs have been submitted
for dir in job_dirs:
  if sub_count == 85:
    sys.exit()
  else:
    os.chdir(dir)
    os.chdir('5Z')
    if os.path.exists('./run_molpro2015_bebop.sh'):
      os.chdir('../../')
    else:
      subprocess.call( ['python', '/lcrc/project/PACC/submission/submit_bebop.py', 'molpro2015', 'PACC', '-n', '8', '-t', '72:00:00', '-p', 'bdwd'] )
      sub_count = sub_count + 1
      os.chdir('../../')
    

