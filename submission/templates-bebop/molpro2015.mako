#!/bin/bash
#SBATCH -p ${partition}
#SBATCH -N ${nnodes}
#SBATCH --ntasks-per-node=${ncores_per_node}
#SBATCH -t ${walltime}
#SBATCH -J ${jobname}
#SBATCH -A ${account}
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

# Set runtime options for Molpro
%if nnodes == 1:
MOLPRO_OPTIONS="--nouse-logfile --no-xml-output -L $MOLPRO_LIB -d $TMPDIR -I $TMPDIR -W $TMPDIR -o ${output}"
%else:
MOLPRO_OPTIONS="--mppx --nouse-logfile --no-xml-output -L $MOLPRO_LIB -d $TMPDIR -I $TMPDIR -W $TMPDIR -o ${output}"
echo "Running Molpro with --mppx flag for parallelization across ${nnodes} nodes"
%endif

echo "Creating scratch directory"
echo "Running Molpro2015"

# Run Molpro with mpirun for MPI parallelization
srun molpro.exe $MOLPRO_OPTIONS $SLURM_SUBMIT_DIR/${input}

echo "Deleting scratch directory"
echo "Job completion"

