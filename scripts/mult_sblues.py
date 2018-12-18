import sys
import os
import subprocess
from fxn_thread import tag_team_starmap

def sort_fxn(string):
  return int(string.split('_')[0])

def submit_fxn(jobpath, command, worker_id):
  ''' Function uses info to run the sblues script '''

  # Change into the jobdir
  os.chdir(jobpath)

  # Replace HOST with worker_id and split string into list to put into subprocess
  subcommand = command.replace('HOST', worker_id).split()

  # Run the submission command replacing HOST with the node
  subprocess.call( subcommand )
   
  return None

# Get the lsit of directories containing each job
mainpath = os.getcwd()+'/'

# Get the initial list of the job directories
jobdirs = os.listdir('.')

# Check for a jop params file and exit if it does not exist
if os.path.exists('err'):
  jobdirs.remove('err')
if os.path.exists('./job_params.dat'):
  jobdirs.remove('job_params.dat')
else:
  print('Need a job_params.dat file specifying job params')
  sys.exit()

# Sort the jobdirectoires and append the prepend the rest of the path  
jobdirs.sort(key=sort_fxn)
jobpaths = [ mainpath+jobdir for jobdir in jobdirs ]  

# Open the thread file and read in the job parameters
with open('job_params.dat','r') as paramfile:
  for line in paramfile:
    if 'hostnodes =' in line:
      worker_ids = line.strip().split()[2:]
    if 'command =' in line:
      command = line.strip().split('=')[1]
commands = [ command for i in range(len(jobpaths)) ]

# Zip the paths and commands to pass into submission function
submit_args = tuple(zip(jobpaths, commands))

# Call the submssion function
tag_team_starmap(submit_fxn, submit_args, worker_ids)

