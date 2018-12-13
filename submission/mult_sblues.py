import os
import sys
import argparse
import subprocess
from mako.template import Template


# Create an ArgumentParser object to store the user-desired parameters for job submission
cmd_line_parser = argparse.ArgumentParser()

# Use positional arguments to specify the program to be ran as well as the compute nodes 
cmd_line_parser.add_argument("program",help="Specify program you will be running (Supported: cfour2, g09e, molpro2015, molpro2015-mppx, mrcc2018, orca4)")

# Set additional parameters for user may want to control job submission 
cmd_line_parser.add_argument("-n","--ncores_per_node",default=1,type=int,help="Number of cores for EACH node (default: %(default)d)")
cmd_line_parser.add_argument("-d","--scratch",default="/scratch/$USER",help="Set the scratch directory (default: %(default)s)")
cmd_line_parser.add_argument("-s","--submit",default=True,help="Automatically use the shell script to submit job? True/False (default: %(default)s)")

# Place all of the parameters needed to create the submission script into a dictionary
submit_options = cmd_line_parser.parse_args()
submit_options_dic = vars(submit_options)

# Check if user wishes to allocate nodes using a machine file; reset hostnodes variable if so
if submit_options_dic["hostnodes"] == 'machines':
  if os.path.exists('./machines'):
    with open('machines','r') as machinefile:
     nodes = '' 
     for line in machinefile:
        if line.strip() != '':
          nodes = nodes + line.strip() + ','
     submit_options_dic["hostnodes"] = nodes[:-1]
  else:
    print('No machines file found. Please place desired nodes in a vertical list in a file named machines')
    sys.exit()

# Determine the TOTAL number of nodes for calling MPI; if needed 
submit_options_dic["nnodes"] = submit_options_dic["hostnodes"].count('b')
submit_options_dic["ncores_total"] = str( submit_options_dic["nnodes"] * submit_options_dic["ncores_per_node"] )

# Place the user-desired options in a submission script template
substituted_template = Template(filename="/home/kmoore/elstruct-interface/submission/templates/blues/"+submit_options.program+".mako").render(**submit_options_dic)

# Write the submission script in the working directory
with open("run_"+submit_options.program+"_blues.sh","w") as submissionfile:
  submissionfile.write(substituted_template)

# Make the shell script an execuatable
subprocess.call(["chmod", "+x", "run_"+submit_options.program+"_blues.sh"])
print('\nCreated Blues Submission Script\n')

# Check if the user requests immediate submission by checking the -s flag
if submit_options.submit == True:
  subprocess.call(["./run_"+submit_options.program+"_blues.sh"])
  print('Job submitted to Blues node(s): '+submit_options.hostnodes+'\n')

