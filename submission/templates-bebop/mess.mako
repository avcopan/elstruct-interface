#!/bin/bash
#SBATCH -p ${partition}
#SBATCH -N 1
#SBATCH --ntasks-per-node=${ncores}
#SBATCH -t ${walltime}
#SBATCH -J ${jobname}
#SBATCH -A ${account}
#SBATCH -o job_%j.log
#SBATCH -e job_%j.err

# Set Path to MESS Executable in Sarah's directories
MESSEXE=/home/elliott/bin/mess

# Run MESS executable
$MESSEXE ${input}

