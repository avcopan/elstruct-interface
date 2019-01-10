#!/bin/bash
#SBATCH -p bdwall
#SBATCH -N 1
#SBATCH --ntasks-per-node=8
#SBATCH -t 2:00:00
#SBATCH -J run
#SBATCH -A PACC
#SBATCH -o job_%j.log
#SBATCH -e job_%j.err

# Set variables for NWChem
export NWCHEMEXE=/soft/nwchem/bebop/bdw-casper/bin/nwchem 

# Set MPI
export I_MPI_FABRICS=shm:tmi
export I_MPI_OFI_PROVIDER=psm2

# Include Casper library in LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/soft/nwchem/bebop/bdw-casper/lib/libcasper.so

# Set the scratch directory
export TMPDIR=/scratch/$USER

# Run NWCHEM with MPI
srun $NWCHEMEXE $SLURM_SUBMIT_DIR/input.dat > $SLURM_SUBMIT_DIR/output.dat 

