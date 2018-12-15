""" function to submit input file all electronic structure codes to Blues queue 
"""
import os
import subprocess

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
SCRIPT_FILE = os.path.join(DIR_PATH, 'sblues.py')

def submit(program, hostnodes, ncores_per_node=1, njobs=1, 
           input='input.dat', output='output.dat', scratch='/scratch/$USER', 
           submit=True, background=False):
  """ 
  Calls the sblues python script and feeds in the runtime options the user requests
  """

  subprocess.call(
                  [
                   'python', 
                   SCRIPT_FILE,
                   '{0}'.format(program), 
                   '{0}'.format(hostnodes),
                   '-J', '{0}'.format(str(njobs)), 
                   '-n', '{0}'.format(str(ncores_per_node)), 
                   '-i', '{0}'.format(input), 
                   '-o', '{0}'.format(output), 
                   '-d', '{0}'.format(scratch), 
                   '-s', '{0}'.format(submit), 
                   '-b', '{0}'.format(background)
                  ]
                 )

  return None

