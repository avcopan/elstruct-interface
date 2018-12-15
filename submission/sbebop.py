#!/usr/bin/env python3

import os
import argparse
import subprocess
from mako.template import Template

##### TAKE IN JOB PARAMETERS FROM THE USER THAT WILL BE USED TO BUILD THE SUBMISSION SCRIPT #####

# Create an ArgumentParser object to store the user-desired parameters for job submission
cmd_line_parser = argparse.ArgumentParser()

# Use positional arguments to specify the program to be ran as well as the compute nodes 
cmd_line_parser.add_argument("program",
  help="Specify program you will be running (Supported: cfour2, g09e, molpro2015, molpro2015-mppx, mrcc2018, nwchem6, orca4)")
cmd_line_parser.add_argument("account",help="Name of the LCRC account to be charged for running on the Bebop queue")

# Set additional parameters for user may want to control job submission 
cmd_line_parser.add_argument("-p","--partition",default="bdwall",
  help="Bebop partition to submit to (default: %(default)s)")
cmd_line_parser.add_argument("-N","--nnodes"   ,default=1,type=int,
  help="Number of nodes (default: %(default)d)")
cmd_line_parser.add_argument("-J","--njobs",default=1,type=int,
  help="Run 'njobs' molpro2015 calcs on SINGLE node. Place each job calcn directory where 1<=n<=njobs. (default: %(default)d)")
cmd_line_parser.add_argument("-n","--ncores_per_node",default=1,type=int,
  help="Number of cores for EACH node (default: %(default)d)")
cmd_line_parser.add_argument("-t","--walltime",default="2:00:00",
  help="Maximum wall time requested in HH:MM:SS (default: %(default)s)")
cmd_line_parser.add_argument("-j","--jobname",default="run",
  help="Name your job will have on the Bebop queue (default: %(default)s)")
cmd_line_parser.add_argument("-i","--input",default="input.dat",
  help="Name of input file (default: %(default)s)")
cmd_line_parser.add_argument("-o","--output",default="output.dat",
  help="Name of output file (default: %(default)s)")
cmd_line_parser.add_argument("-d","--scratch",default="/scratch/$USER",
  help="Set the scratch directory (default: %(default)s)")
cmd_line_parser.add_argument("-s","--submit",default=True,type=bool,
  help="Automatically use the shell script to submit job? True/False (default: %(default)b)")

#################################################


##### PLACE OPTIONS IN A DIRECTORY AND ADD ADDITIONAL REQUIRED OPTIONS AND CHECK FOR ERRORS #####

# Place all of the parameters needed to create the submission script into a dictionary
SUBMIT_OPTIONS = vars(cmd_line_parser.parse_args())

# Check for njobs > 2 and set appropriate variables and flag errors if other variables not set correctly
if SUBMIT_OPTIONS["njobs"] > 1 and SUBMIT_OPTIONS["nnodes"] > 1:
  raise ValueError("Multiple job runs only allowed for a SINGLE NODE")
if SUBMIT_OPTIONS["njobs"] > 1 and SUBMIT_OPTIONS["program"] != "molpro2015":
  raise ValueError("njobs > 1 only supported for molpro2015 calculations")

# Determine the TOTAL number of cores for calling MPI; if needed 
SUBMIT_OPTIONS["ncores_total"] = SUBMIT_OPTIONS["nnodes"] * SUBMIT_OPTIONS["ncores_per_node"] 

#################################################


##### WRITE THE BATCH SCRIPT FILE FOR SUBMISSION #####
TEMPLATE_PATH = "/home/kmoore/elstruct-interface/submission/templates/bebop/"
TEMPLATE_FILE = SUBMIT_OPTIONS["program"]+'.mako'
substituted_template = Template(filename=os.path.join(TEMPLATE_PATH,TEMPLATE_FILE)).render(**SUBMIT_OPTIONS)

# Write the submission script in the working directory
SUB_FILE = "run_"+SUBMIT_OPTIONS["program"]+"_blues.sh"
with open(SUB_FILE,"w") as submissionfile:
  submissionfile.write(substituted_template)
print('\nCreated Bebop Submission Script\n')

#################################################


##### SUBMIT JOB IF -s FLAG SET TO TRUE ##### 

if SUBMIT_OPTIONS["submit"] == True:
  subprocess.call(["sbatch", SUB_FILE])
  print('')

#################################################


#### END PROGRAM #####


