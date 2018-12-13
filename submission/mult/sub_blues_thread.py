from thread import tag_team_starmap

def submit(path,worker_id):
  ''' Function uses info to run the sblues script '''


 return


# Read in the machines file to get nodes
worker_id = []
with open('machines','r') as machinefile:
  for line in machinefile:
    if line.strip() != '':
      line.split(':') 




tag_team_starmap(submit,

