#!/bin/bash
#SBATCH -p ${partition}
#SBATCH -N ${nnodes}
#SBATCH --ntasks-per-node=${ncores}
#SBATCH -t ${walltime}
#SBATCH -J ${jobname}
#SBATCH -A ${account}
#SBATCH -o job_%j.log
#SBATCH -e job_%j.err

echo "Setting runtime variables and loading necesary libraries"
 
# Set variables for NWChem
export NWCHEMEXE=/soft/nwchem/bebop/bdw-casper/bin/nwchem 

# Set MPI
export I_MPI_FABRICS=shm:tmi
export I_MPI_OFI_PROVIDER=psm2

# Include Casper library in LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/soft/nwchem/bebop/bdw-casper/lib/libcasper.so

echo "Creating scratch directory"

# Set the scratch directory
export TMPDIR=/scratch/$USER

echo "Running NWCHEM 6.6"

# Run NWCHEM with MPIs
srun $NWCHEMEXE $SLURM_SUBMIT_DIR/input.dat > $SLURM_SUBMIT_DIR/output.dat 

echo "Deleting the scratch directory"
echo "Job completion"

