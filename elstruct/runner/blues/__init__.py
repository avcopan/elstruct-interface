""" function to submit input file all electronic structure codes to Blues queue 
"""
import os
import subprocess

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
SCRIPT_FILE = os.path.join(DIR_PATH, 'sblues.py')

def submit(program, hostnodes, ncores_per_node=1, njobs=1, 
           input='input.dat', output='output.dat', scratch='/scratch/$USER', 
           submit='yes', background='no'):
  """ 
  Calls the sblues python script and feeds in the runtime options the user requests
  """

  subprocess.check_call(
                  [
                   'python', 
                   SCRIPT_FILE,
                   program, 
                   hostnodes,
                   '-J', str(njobs), 
                   '-n', str(ncores_per_node), 
                   '-i', input, 
                   '-o', output, 
                   '-d', scratch, 
                   '-s', submit, 
                   '-b', background
                  ]
                 )

  return None

