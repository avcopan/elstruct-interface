import sys
import argparse
import subprocess
from mako.template import Template


##### Get all the submission options from the user needed to build the submission script #####


# Create an ArgumentParser object to store the obtions for the program
cmd_line_parser = argparse.ArgumentParser()

# Establish positional argument to specify the program that is being run
cmd_line_parser.add_argument("program",help="Specify program you will be running (Supported: cfour2, g09e, molpro2015, molpro2015-mppx, mrcc2018, orca4)")
cmd_line_parser.add_argument("hostnodes",help="Specify the nodes you wish to submit to. Nodes are b431-b460. Enter as comma-delimited list: node1,node2,node3... ")

# Set additional arguments that one may one want to modify for their specific tasks 
cmd_line_parser.add_argument("-N","--nnodes"   ,default=1,type=int,help="Number of nodes (default: %(default)d)")
cmd_line_parser.add_argument("-n","--ncores_per_node",default=1,type=int,help="Number of cores for EACH node (default: %(default)d)")
cmd_line_parser.add_argument("-i","--input",default="input.dat",help="Name of input file (default: %(default)s)")
cmd_line_parser.add_argument("-o","--output",default="output.dat",help="Name of output file (default: %(default)s)")
cmd_line_parser.add_argument("-d","--scratch",default="/scratch/$USER",help="Set the scratch directory (default: %(default)s)")
cmd_line_parser.add_argument("-s","--submit",default=True,help="Automatically use the shell script to submit job (default: %(default)s)")

# Place all of the arguments needed to create the submission script into a dictionary
submit_options = cmd_line_parser.parse_args()
submit_options_dic = vars(submit_options)

# Add additional options to the dictionary determined by user input 
submit_options_dic["ncores_total"] = str( submit_options_dic["nnodes"] * submit_options_dic["ncores_per_node"] )

# Assess if options set correctly for multiple node runs
if submit_options_dic["hostnodes"].count('b') != submit_options_dic["nnodes"]:
  print('\n ERROR. NO JOB SUBMISSION: The number of Blues nodes requested must equal the value of -N\n')
  sys.exit()

##### Place the user-desired options in a submission script template #####


# Create object containing the template with the above user-specified options input
substituted_template = Template(filename="/home/kmoore/elstruct-interface/submission/templates/blues/"+submit_options.program+".mako").render(**submit_options_dic)

# Write the submission script in the working directory
with open("run_"+submit_options.program+"_blues.sh","w") as submissionfile:
  submissionfile.write(substituted_template)

# Make the shell script an execuatable
subprocess.call(["chmod", "+x", "run_"+submit_options.program+"_blues.sh"])
print('\nCreated Blues Submission Script\n')


###### If the user requests, submit the job immediately with sbatch #####


# Check if the user requests immediate submission by checking the -s flag
if submit_options.submit == True:
  subprocess.call(["./run_"+submit_options.program+"_blues.sh"])
  print('Job submitted to Blues node(s): '+submit_options.hostnodes+'\n')

##### END PROGRAM #####


