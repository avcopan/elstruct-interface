#!/bin/bash
#SBATCH -p bdwall
#SBATCH -N 1
#SBATCH --cpus-per-task=8
#SBATCH -t 2:00:00
#SBATCH -J run
#SBATCH -A CMRP
#SBATCH -o job_%j.log
#SBATCH -e job_%j.err

echo "Setting runtime variables and loading necesary libraries"

# Set enviornmental variables for MPI
export I_MPI_FABRICS=shm:tmi

# Load Molpro
module load molpro/2015.1_170920

# Set Molpro library directory
MOLPRO_LIB=/soft/molpro/2015.1_170920/bebop/molprop_2015_1_linux_x86_64_i8/lib/

# Set the scratch directory
export TMPDIR=/scratch/$USER

echo "Settting Molpro options"

echo "Creating scratch directory"
echo "Running Molpro2015"

# Run Molpro with mpirun for MPI parallelization
OPTIONS1="--nouse-logfile --no-xml-output -L $MOLPRO_LIB -d $TMPDIR -I $TMPDIR -W $TMPDIR -o $SLURM_SUBMIT_DIR/p1/output.dat"
OPTIONS2="--nouse-logfile --no-xml-output -L $MOLPRO_LIB -d $TMPDIR -I $TMPDIR -W $TMPDIR -o $SLURM_SUBMIT_DIR/p2/output.dat"
OPTIONS3="--nouse-logfile --no-xml-output -L $MOLPRO_LIB -d $TMPDIR -I $TMPDIR -W $TMPDIR -o $SLURM_SUBMIT_DIR/p3/output.dat"
OPTIONS4="--nouse-logfile --no-xml-output -L $MOLPRO_LIB -d $TMPDIR -I $TMPDIR -W $TMPDIR -o $SLURM_SUBMIT_DIR/p4/output.dat"
INPUT1="$SLURM_SUBMIT_DIR/p1/input.dat"
INPUT2="$SLURM_SUBMIT_DIR/p2/input.dat"
INPUT3="$SLURM_SUBMIT_DIR/p3/input.dat"
INPUT4="$SLURM_SUBMIT_DIR/p4/input.dat"

srun -c 1 -n 4 --exclusive molpro.exe $OPTIONS1 $INPUT1 &
srun -c 1 -n 4 --exclusive molpro.exe $OPTIONS2 $INPUT3 &
srun -c 1 -n 4 --exclusive molpro.exe $OPTIONS3 $INPUT3 &
srun -c 1 -n 4 --exclusive molpro.exe $OPTIONS4 $INPUT4 &
wait

echo "Deleting scratch directory"
echo "Job completion"

