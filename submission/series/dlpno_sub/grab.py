import os

def sortfxn(string):
  return int(string.split('_')[0])

def read_energies():

  # Initialize energy string
  energy_str = ''

  # Check if output.dat exists and read data if it exists
  if os.path.exists('./output.dat'):
 
    with open('output.dat','r') as jobfile:
      jobdata = jobfile.readlines()      

    # Grab the CC energies while checking if job finished
    # Add the job wall time for completed jobs  
    count = 0
    for i in range(len(jobdata)):
      if 'E(CCSD(T))' in jobdata[i]:
        count = count + 1
        if count == 1:
          energy_str = energy_str + '  ' + jobdata[i].strip().split()[2] 
        if count == 2:
          energy_str = energy_str + '  ' + jobdata[i].strip().split()[2] 
        if count == 3:
          energy_str = energy_str + '  ' + jobdata[i].strip().split()[2] 
        if count == 4:
          energy_str = energy_str + '  ' + jobdata[i].strip().split()[2] 
      #if 'TOTAL RUN TIME' in jobdata[i]:
      #  energies.append(jobdata[i])

    # Add a line for seperation
    energy_str = energy_str + '\n'

  return energy_str


# Get the job directories in a list
jobdirs = os.listdir('.')
jobdirs.sort(key=sortfxn)

# Get empty list where everything stored
energies = []

# Loop through directories and grab everything
for dir in jobdirs:

  # Print the directory 
  print(dir)
  
  # Blank the job
  energy_str = ''
 
  # Go into directory
  os.chdir(dir)

  # Check if a redo directory exists for rerunning a job that failed
  if os.path.exists('./retry'):
    os.chdir('retry')
    energy_str = str(dir) + read_energies()
    os.chdir('../')
  else:
    energy_str = str(dir) + read_energies()
  
  # Append to energies list
  energies.append(energy_str)

  # Go back up a directory
  os.chdir('../')

# Write the energies to a file
with open('energies.dat2','w') as energyfile:
  for line in energies:
    energyfile.writelines(line)


