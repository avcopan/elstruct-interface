#!/bin/bash
#SBATCH -p ${partition}
#SBATCH -N 1
#SBATCH --ntasks-per-node=${ncores_per_node}
#SBATCH -t ${walltime}
#SBATCH -J ${jobname}
#SBATCH -A ${account}
#SBATCH -o job_%j.log
#SBATCH -e job_%j.err

# Load Gaussian
module load gaussian/09-e.01

# Set sratch directory
export GAUSS_SCRDIR=${scratch}
mkdir -p $GAUSS_SCRDIR 

# Run Gaussian
g09 -scrdir=$GAUSS_SCRDIR < ${input} > ${output}

