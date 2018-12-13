#!/bin/bash
#SBATCH -p bdwall
#SBATCH -N 1
#SBATCH --ntasks-per-node=8
#SBATCH -t 2:00:00
#SBATCH -J run
#SBATCH -A PACC
#SBATCH -o job_%j.log
#SBATCH -e job_%j.err

# Load Gaussian
module load gaussian/09-e.01

# Set sratch directory
export GAUSS_SCRDIR=/scratch/$USER
mkdir -p $GAUSS_SCRDIR 

# Run Gaussian
g09 -scrdir=$GAUSS_SCRDIR < input.dat > output.dat

