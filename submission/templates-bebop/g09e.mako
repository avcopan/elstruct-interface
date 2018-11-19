#!/bin/bash
#SBATCH -p ${partition}
#SBATCH -N 1
#SBATCH --ntasks-per-node=${ncores_per_node}
#SBATCH -t ${walltime}
#SBATCH -J ${jobname}
#SBATCH -A ${account}
#SBATCH -o job_%j.log
#SBATCH -e job_%j.err

echo "Setting runtime variables and loading necesary libraries"

# Load Gaussian
module load gaussian/09-e.01

echo "Creating scratch directory"

# Set sratch directory
export GAUSS_SCRDIR=/scratch/$USER
mkdir -p $GAUSS_SCRDIR 

echo "Running Gaussian09 Version E"

# Run Gaussian
g09 < ${input} > ${output}

echo "Deleting the scratch directory"
echo "Job completion"


