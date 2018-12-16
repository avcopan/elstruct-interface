import os
import argparse
import subprocess
from mako.template import Template

##### TAKE IN JOB PARAMETERS FROM THE USER THAT WILL BE USED TO BUILD THE SUBMISSION SCRIPT #####

# Create an ArgumentParser object to store the user-desired parameters for job submission
cmd_line_parser = argparse.ArgumentParser()

# Use positional arguments to specify the program to be ran as well as the compute nodes 
cmd_line_parser.add_argument("program",
  help="Program to run (Supported: cfour2, g09e, molpro2015, molpro2015-mppx, mrcc2018, orca4, psi4)")
cmd_line_parser.add_argument("hostnodes",
  help="Options: (1) Enter as list: node1,node2,node3...; (2) List nodes in a 'machines' file")

# Set additional parameters for user may want to control job submission 
cmd_line_parser.add_argument("-J","--njobs",default=1,type=int,
  help="Run 'njobs' molpro2015 calcs on SINGLE node. Put jobs in calcn directory where 1<=n<=njobs. (default: %(default)d)")
cmd_line_parser.add_argument("-n","--ncores_per_node",default=1,type=int,
  help="Number of cores for EACH node (default: %(default)d)")
cmd_line_parser.add_argument("-i","--input",default="input.dat",
  help="Name of input file (default: %(default)s)")
cmd_line_parser.add_argument("-o","--output",default="output.dat",
  help="Name of output file (default: %(default)s)")
cmd_line_parser.add_argument("-d","--scratch",default="/scratch/$USER",
  help="Set the scratch directory (default: %(default)s)")
cmd_line_parser.add_argument("-s","--submit",default=True,
  help="Automatically submit job? True/False (default: %(default)s)")
cmd_line_parser.add_argument("-b","--background",default=True,
  help="Run job in the background? True/False (default: %(default)s)")

# Place all of the parameters needed to create the submission script into a dictionary
SUBMIT_OPTIONS = vars(cmd_line_parser.parse_args())

#################################################


##### CHECK FOR ERRORS WITH THE INPUT AND SET OTHER NEEDED RUNTIME OPTIONS  #####

# Check if requested program is supported by script
supported_programs = [ 'cfour2', 'g09e', 'molpro2015', 'molpro2015-mppx', 'mrcc2018', 'orca4', 'psi4' ]
if SUBMIT_OPTIONS["program"] not in supported_programs:
  raise ValueError('Program requested is not currently supported')

# Check if input file exists
if os.path.exists('./'+SUBMIT_OPTIONS["input"]) == False:
  raise ValueError('Input file does not exist in current submission directory')

# Check if user wishes to allocate nodes using a machine file; reset hostnodes variable if so
if SUBMIT_OPTIONS["hostnodes"] == 'machines':
  if os.path.exists('./machines'):
    with open('machines','r') as machinefile:
     nodes = '' 
     for line in machinefile:
        if line.strip() != '':
          nodes = nodes + line.strip() + ','
     SUBMIT_OPTIONS["hostnodes"] = nodes[:-1]
  else:
    raise ValueError('No machines file found. Please place desired nodes in a vertical list in a file named machines')

# Determine the TOTAL number of nodes for calling MPI; if needed 
SUBMIT_OPTIONS["nnodes"] = SUBMIT_OPTIONS["hostnodes"].count('b')

# Check for njobs > 2 and set appropriate variables and flag errors if other variables not set correctly
if SUBMIT_OPTIONS["njobs"] > 1 and SUBMIT_OPTIONS["nnodes"] > 1:
  raise ValueError("Multiple job runs only allowed for a SINGLE NODE")
if SUBMIT_OPTIONS["njobs"] > 1 and SUBMIT_OPTIONS["program"] != "molpro2015":
  raise ValueError("njobs > 1 only supported for molpro2015 calculations")

# Determine the TOTAL number of cores for calling MPI; if needed 
SUBMIT_OPTIONS["ncores_total"] = SUBMIT_OPTIONS["nnodes"] * SUBMIT_OPTIONS["ncores_per_node"] 

#################################################


##### WRITE THE BATCH SCRIPT FILE FOR SUBMISSION #####

# Place the user-desired options in a submission script template
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_FILE = DIR_PATH + '/templates/' + SUBMIT_OPTIONS["program"]+'.mako'
substituted_template = Template(filename=TEMPLATE_FILE).render(**SUBMIT_OPTIONS)

# Write the submission script in the working directory
SUB_FILE = "run_"+SUBMIT_OPTIONS["program"]+"_blues.sh"
with open(SUB_FILE,"w") as submissionfile:
  submissionfile.write(substituted_template)

# Make the shell script an execuatable
subprocess.call(["chmod", "+x", SUB_FILE])
print('\nCreated Blues Submission Script\n')

#################################################


##### SUBMIT JOB IF -s FLAG SET TO TRUE ##### 
if SUBMIT_OPTIONS["submit"] == True:
  subprocess.call(["./"+SUB_FILE])
  print('Job submitted to Blues node(s): '+SUBMIT_OPTIONS["hostnodes"]+'\n')

#################################################


#### END PROGRAM #####

