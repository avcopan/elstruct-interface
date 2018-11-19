#!/bin/bash
#SBATCH -p bdwall
#SBATCH -N 1
#SBATCH --ntasks-per-node=4
#SBATCH -t 8:00:00
#SBATCH -J run
#SBATCH -A STARTUP-KMOORE
#SBATCH -o job_%j.log
#SBATCH -e job_%j.err

echo "Setting runtime variables and loading necesary libraries"

# Set enviornmental variables for MPI
export I_MPI_FABRICS=shm:tmi
export NSLOTS=$SLURM_NTASKS_PER_NODE

# Load Molpro
module load molpro/2015.1_170920

# Set Molpro library directory
MOLPRO_LIB=/soft/molpro/2015.1_170920/bebop/molprop_2015_1_linux_x86_64_i8/lib/

# Set the scratch directory
export TMPDIR=/scratch/$USER

echo "Settting Molpro options"

# Set runtime options for Molpro
MOLPRO_OPTIONS="--nouse-logfile --no-xml-output -L $MOLPRO_LIB -d $TMPDIR -I $TMPDIR -W $TMPDIR -o output.dat"

echo "Creating scratch directory"
echo "Running Molpro2015"

# Run Molpro with mpirun for MPI parallelization
srun molpro.exe $MOLPRO_OPTIONS $SLURM_SUBMIT_DIR/input.dat

echo "Deleting scratch directory"

# Remove scratch directory
rm -rf $TMPDIR

echo "Job completion"

