""" function to submit input file all electronic structure codes to Bebop queue 
"""
import os
import subprocess

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
SCRIPT_FILE = os.path.join(DIR_PATH, 'sbebop.py')

def submit(program, account, partition='bdwall', nnodes=1, njobs=1, ncores_per_node=1,
           walltime='2:00:00', jobname='run', input='input.dat', output='output.dat', 
           scratch='/scratch/$USER', submit=True, background=False):
  """ Calls the Python bebop submission script using the user-desired runtime options 
  """

  subprocess.call(
                  [
                   'python', 
                   SCRIPT_FILE,
                   '{0}'.format(program), 
                   '{0}'.format(account),
                   '-p', '{0}'.format(partition), 
                   '-N', '{0}'.format(str(nnodes)), 
                   '-J', '{0}'.format(str(njobs)), 
                   '-n', '{0}'.format(str(ncores_per_node)), 
                   '-t', '{0}'.format(walltime), 
                   '-j', '{0}'.format(jobname), 
                   '-i', '{0}'.format(input), 
                   '-o', '{0}'.format(output), 
                   '-d', '{0}'.format(scratch), 
                   '-s', '{0}'.format(submit), 
                   '-b', '{0}'.format(background), 
                  ]
                 )

  return
