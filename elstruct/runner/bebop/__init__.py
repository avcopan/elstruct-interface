""" function to submit input file all electronic structure codes to Bebop queue 
"""
import os
import subprocess

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
SCRIPT_FILE = os.path.join(DIR_PATH, 'sbebop.py')

def submit(program, account, partition='bdwall', nnodes=1, njobs=1, ncores_per_node=1,
           walltime='2:00:00', jobname='run', input='input.dat', output='output.dat', 
           scratch='/scratch/$USER', submit='yes', background='no'):
  """ Calls the Python bebop submission script using the user-desired runtime options 
  """

  subprocess.check_call(
                  [
                   'python', 
                   SCRIPT_FILE,
                   program, 
                   account,
                   '-p', partition, 
                   '-N', str(nnodes), 
                   '-J', str(njobs), 
                   '-n', str(ncores_per_node), 
                   '-t', walltime, 
                   '-j', jobname, 
                   '-i', input, 
                   '-o', output, 
                   '-d', scratch, 
                   '-s', submit, 
                   '-b', background, 
                  ]
                 )

  return
