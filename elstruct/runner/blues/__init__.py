""" function to submit input file all electronic structure codes to Blues queue 
"""
import os
import subprocess
from mako.template import Template
from ... import params

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_PATH = os.path.join(DIR_PATH, 'templates')

TEMPLATE_FILES = {
    params.PROGRAM.PSI4: 'psi4.mako',
    params.PROGRAM.MOLPRO: 'molpro2015.mako',
}


def submit(program, hostnodes, ncores_per_node=1, njobs=1, 
           input_name='input.dat', output_name='output.dat', scratch='/scratch/$USER', 
           submit=True, background=False):
    if program not in TEMPLATE_FILES.keys():
      raise ValueError('Program requested is not currently supported')

    fill_vals = {
        'program': program,
        'hostnodes': hostnodes,
        'ncores_per_node': ncores_per_node,
        'njobs': njobs,
        'input': input_name,
        'output': output_name,
        'scratch': scratch,
        'submit': ('yes' if submit else 'no'),
        'background': ('yes' if background else 'no'),
    }

    # Check if input file exists
    if os.path.exists('./'+input_name) == False:
      raise ValueError('Input file does not exist in current submission directory')

    # Check if user wishes to allocate nodes using a machine file; reset hostnodes variable if so
    if hostnodes == 'machines':
      if os.path.exists('./machines'):
        with open('machines','r') as machinefile:
         nodes = '' 
         for line in machinefile:
            if line.strip() != '':
              nodes = nodes + line.strip() + ','
         hostnodes = nodes[:-1]
      else:
        raise ValueError('No machines file found. Please place desired nodes in a vertical list in a file named machines')

    # Determine the TOTAL number of nodes for calling MPI; if needed 
    fill_vals["nnodes"] = hostnodes.count('b')

    # Check for njobs > 2 and set appropriate variables and flag errors if other variables not set correctly
    if njobs > 1 and fill_vals["nnodes"] > 1:
      raise ValueError("Multiple job runs only allowed for a SINGLE NODE")
    if njobs > 1 and program != "molpro2015":
      raise ValueError("njobs > 1 only supported for molpro2015 calculations")

    # Determine the TOTAL number of cores for calling MPI; if needed 
    fill_vals["ncores_total"] = fill_vals["nnodes"] * ncores_per_node 

    #################################################

    template_file_name = TEMPLATE_FILES[program]
    template_file_path = os.path.join(TEMPLATE_PATH, template_file_name)

    substituted_template = Template(filename=template_file_path).render(**fill_vals)

    # Write the submission script in the working directory
    SUB_FILE = "run_"+program+"_blues.sh"
    with open(SUB_FILE,"w") as submissionfile:
      submissionfile.write(substituted_template)

    # Make the shell script an execuatable
    subprocess.call(["chmod", "+x", SUB_FILE])
    #print('\nCreated Blues Submission Script\n')

    #################################################


    ##### SUBMIT JOB IF -s FLAG SET TO TRUE ##### 
    if submit:
      return_code = subprocess.check_call(os.path.join('.', SUB_FILE))
    #  print('Job submitted to Blues node(s): '+hostnodes+'\n')

    #################################################


    #### END PROGRAM #####

