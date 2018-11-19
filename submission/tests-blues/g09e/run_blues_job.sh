#!/bin/bash

echo "Setting runtime variables and loading necesary libraries" >> job_status.log

# Load Gaussian
soft add +g09-e.01

# Set variable to contain appropriate scratch directory
export GAUSS_SCRDIR=/scratch/$USER

echo "Settting MPI options" >> job_status.log

# Set runtime options for MPI
MPI_OPTIONS="-n 1 -ppn 1 -hosts b437"

mpirun $MPI_OPTIONS g09 input.dat -scrdir=$GAUSS_SCRDIR &

echo "Job completion"


