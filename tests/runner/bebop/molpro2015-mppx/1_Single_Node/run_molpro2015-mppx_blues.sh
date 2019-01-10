#!/bin/bash
#SBATCH -p bdwall
#SBATCH -N 1
#SBATCH --ntasks-per-node=8
#SBATCH -t 2:00:00
#SBATCH -J run
#SBATCH -A PACC
#SBATCH -o job_%j.log
#SBATCH -e job_%j.err

# Set enviornmental variables for MPI
export I_MPI_FABRICS=shm:tmi

# Load Molpro
module load molpro/2015.1_170920

# Set Molpro library directory
MOLPRO_LIB=/soft/molpro/2015.1_170920/bebop/molprop_2015_1_linux_x86_64_i8/lib/

# Set the scratch directory
export TMPDIR=/scratch/$USER

# Set runtime options for Molpro
MOLPRO_OPTIONS="--mppx --nouse-logfile --no-xml-output -L $MOLPRO_LIB -d $TMPDIR -I $TMPDIR -W $TMPDIR -o output.dat"

# Run Molpro with mpirun for MPI parallelization
srun molpro.exe $MOLPRO_OPTIONS $SLURM_SUBMIT_DIR/input.dat

