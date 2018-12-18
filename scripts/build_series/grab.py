import os
from esfile import molpro_lccsdt
from esfile import orca_dlpno


def sortfxn(string):
  return int(string.split('_')[0])

def read_energies():

  # Initialize energy string
  energy_str = ''
  time_str = ''

  # Check if output.dat exists and read data if it exists
  if os.path.exists('./output.dat'):
 
    with open('output.dat','r') as jobfile:
      jobdata = jobfile.readlines()      

    # Grab the CC energies while checking if job finished
    # Add the job wall time for completed jobs  
    for i in range(len(jobdata)):
      if 'SETTING EDZ' in jobdata[i]:   
        energy_str = energy_str + '  ' + jobdata[i].strip().split()[3] 
      if 'SETTING ETZ' in jobdata[i]:   
        energy_str = energy_str + '  ' + jobdata[i].strip().split()[3] 
      if 'SETTING EQZ' in jobdata[i]:   
        energy_str = energy_str + '  ' + jobdata[i].strip().split()[3] 
      if 'SETTING E5Z' in jobdata[i]:   
        energy_str = energy_str + '  ' + jobdata[i].strip().split()[3] 
    for i in reversed(range(len(jobdata))):    
      if 'REAL TIME' in jobdata[i]:
        time_str = time_str + '   ' + jobdata[i].strip().split()[3]
        break
  
  # Add a line for seperation
  energy_str = energy_str + '\n'
  time_str = time_str + '\n' 

  return energy_str,time_str

# Delete current .dat files
if os.path.exists('./energies.dat'):
  os.system('rm ./energies.dat')
if os.path.exists('./times.dat'):
  os.system('rm ./times.dat')

# Get the job directories in a list
jobdirs = os.listdir('.')
jobdirs.sort(key=sortfxn)

# Get empty list where everything stored
energies = []
times = []

# Loop through directories and grab everything
for dir in jobdirs:

  # Print the directory 
  print(dir)
  
  # Blank the job
  energy_str = ''
  time_str = ''
 
  # Go into directory
  os.chdir(dir)

  # Check if a redo directory exists for rerunning a job that failed
  if os.path.exists('./retry'):
    os.chdir('retry')
    energy, time = read_energies()
    energy_str = str(dir) + energy
    time_str = str(dir) + time
    os.chdir('../')
  else:
    energy, time = read_energies()
    energy_str = str(dir) + energy
    time_str = str(dir) + time
  
  # Append to energies list
  energies.append(energy_str)
  times.append(time_str)

  # Go back up a directory
  os.chdir('../')

# Write the energies and times to files
with open('energies.dat','w') as energyfile:
  for line in energies:
    energyfile.writelines(line)
with open('times.dat','w') as timefile:
  for line in times:
    timefile.writelines(line)


