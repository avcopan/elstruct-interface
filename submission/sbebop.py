#!/usr/bin/env python3

import argparse
import subprocess
from mako.template import Template


# Create an ArgumentParser object to store the user-desired parameters for job submission
cmd_line_parser = argparse.ArgumentParser()

# Use positional arguments to specify the program to be ran as well as the compute nodes 
cmd_line_parser.add_argument("program",help="Specify program you will be running (Supported: cfour2, g09e, molpro2015, molpro2015-mppx, mrcc2018, nwchem6, orca4)")
cmd_line_parser.add_argument("account",help="Name of the LCRC account to be charged for running on the Bebop queue")

# Set additional parameters for user may want to control job submission 
cmd_line_parser.add_argument("-p","--partition",default="bdwall",help="Bebop partition to submit to (default: %(default)s)")
cmd_line_parser.add_argument("-N","--nnodes"   ,default=1,type=int,help="Number of nodes (default: %(default)d)")
cmd_line_parser.add_argument("-n","--ncores_per_node",default=1,type=int,help="Number of cores for EACH node (default: %(default)d)")
cmd_line_parser.add_argument("-t","--walltime",default="2:00:00",help="Maximum wall time requested in HH:MM:SS (default: %(default)s)")
cmd_line_parser.add_argument("-j","--jobname",default="run",help="Name your job will have on the Bebop queue (default: %(default)s)")
cmd_line_parser.add_argument("-i","--input",default="input.dat",help="Name of input file (default: %(default)s)")
cmd_line_parser.add_argument("-o","--output",default="output.dat",help="Name of output file (default: %(default)s)")
cmd_line_parser.add_argument("-d","--scratch",default="/scratch/$USER",help="Set the scratch directory (default: %(default)s)")
cmd_line_parser.add_argument("-s","--submit",default=True,help="Automatically use the shell script to submit job? True/False (default: %(default)s)")

# Place all of the parameters needed to create the submission script into a dictionary
submit_options = cmd_line_parser.parse_args()
submit_options_dic = vars(submit_options)

# Determine the TOTAL number of nodes for calling MPI; if needed 
submit_options_dic["ncores_total"] = str( submit_options_dic["nnodes"] * submit_options_dic["ncores_per_node"] )

# Place the user-desired options in a submission script template
substituted_template = Template(filename="/home/kmoore/elstruct-interface/submission/templates/bebop/"+submit_options.program+".mako").render(**submit_options_dic)

# Write the submission script in the working directory
with open("run_"+submit_options.program+"_bebop.sh","w") as submissionfile:
  submissionfile.write(substituted_template)
print('\nCreated Bebop Submission Script\n')

# Check if the user requests immediate submission by checking the -s flag
if submit_options.submit == True:
  subprocess.call(["sbatch", "run_"+submit_options.program+"_bebop.sh"])
  print('')

