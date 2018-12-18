#!/bin/bash
#SBATCH -p bdwall
#SBATCH -N 1
#SBATCH --ntasks=8
#SBATCH -t 2:00:00
#SBATCH -J run
#SBATCH -A PACC
#SBATCH -o job_%j.log
#SBATCH -e job_%j.err

# Add executables for executable
export PATH=$PATH:/lcrc/project/PACC/brossdh/mrcc/
MRCCEXE=$(which dmrcc)

# Load Intel parallel studio 
module load intel-parallel-studio/cluster.2018.1-egcacag

# Set num threads for OpenMP
export OMP_NUM_THREADS=$SLURM_NTASKS

# Create the scratch irectory
export TMPDIR=/scratch/$USER
mkdir -p $TMPDIR

# Set variable that includes ampersand if run in the background
BACKGROUND=""

# Copy file from scratch
cp $SLURM_SUBMIT_DIR/input.dat $TMPDIR/MINP

# Change into scratch directory
cd $TMPDIR

# Run MRCC with srun for MPI para
$MRCCEXE >& $SLURM_SUBMIT_DIR/output.dat 

# Go back to working directory
cd $SLURM_SUBMIT_DIR


