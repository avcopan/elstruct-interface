#!/bin/bash

# Set path
CWD=$(pwd)

echo "Setting job to run on Blues node(s): b440" >> $CWD/job_status.log

# Set host node to the one specified by the user
HOST=b440

echo "Setting runtime variables and loading necesary libraries" >> $CWD/job_status.log

# Set the scratch directory
export GAUSS_SCRDIR=/scratch/$USER                                

echo "Running Gaussian09 Version E" >> $CWD/job_status.log

# SSH into the Blues node (b4xx) while feeding as series of commands:
# Calls g09 executable on input file
# Removes scratch directory
ssh $HOST " soft add +g09-e.01 ; mkdir -p $GAUSS_SCRDIR ; g09 < $CWD/input.dat > $CWD/output.dat " 

