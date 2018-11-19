#!/bin/bash
#SBATCH -p bdwall
#SBATCH -N 4
#SBATCH --ntasks-per-node=4
#SBATCH -t 8:00:00
#SBATCH -J run
#SBATCH -A CMRP
#SBATCH -o job_%j.out
#SBATCH -e job_%j.err

# Load Molpro
module load molpro/2015.1_170920

# Set Molpro library directory
MOLPRO_LIB=/soft/molpro/2015.1_170920/bebop/molprop_2015_1_linux_x86_64_i8/lib/

# Set the Molpro scratch directory
MOLPRO_SCR=/scratch/$USER

# Set runtime options for Molpro
MOLPRO_OPTIONS="--mppx --nouse-logfile --no-xml-output -L $MOLPRO_LIB -d $MOLPRO_SCR -o output.dat"

# Run Molpro with srun for MPI parallelization
srun molpro.exe $MOLPRO_OPTIONS input.dat


