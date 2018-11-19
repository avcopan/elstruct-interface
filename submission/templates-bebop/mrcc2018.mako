#!/bin/bash
#SBATCH -p ${partition}
#SBATCH -N 1
#SBATCH --ntasks=${ncores}
#SBATCH -t ${walltime}
#SBATCH -J ${jobname}
#SBATCH -A ${account}
#SBATCH -o job_%j.log
#SBATCH -e job_%j.err

echo "Setting runtime variables and loading necesary libraries"

# Add executables for executable
export PATH=$PATH:/lcrc/project/PACC/brossdh/mrcc/
MRCCEXE=$(which dmrcc)

# Load Intel parallel studio 
module load intel-parallel-studio/cluster.2018.1-egcacag

# Set num threads for OpenMP
export OMP_NUM_THREADS=$SLURM_NTASKS

echo "Creating scratch directory"

# Create the scratch irectory
export TMPDIR=/scratch/$USER
mkdir -p $TMPDIR

echo "Copying the input file to node"

# Copy file from scratch
cp $SLURM_SUBMIT_DIR/${input} $TMPDIR/MINP

echo "Running MRCC 2018-10-18"

# Change into scratch directory
cd $TMPDIR

# Run MRCC with srun for MPI para
$MRCCEXE >& $SLURM_SUBMIT_DIR/${output}

# Go back to working directory
cd $SLURM_SUBMIT_DIR

echo "Deleting the scratch directory"
echo "Job completion"


